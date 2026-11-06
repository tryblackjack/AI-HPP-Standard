#!/usr/bin/env python3
"""Observe local artifacts/reports, execute defects, and bind audits to existing PAS Quint."""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from examples import work_integrity_reference as reference  # noqa: E402
from scripts import check_proportionate_action_profile as pas  # noqa: E402

VECTORS = ROOT / "examples/work-integrity-vectors.json"
SCHEMA = ROOT / "schemas/work-integrity-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MAP = ROOT / "data/formal-assurance-map.json"


def load():
    return json.loads(VECTORS.read_text())


def failures(capture):
    """Independent fixed-contract oracle; report assertions are not execution evidence."""
    i, artifact, report = (capture[k] for k in ("inputs", "artifact", "report"))
    values = dict(filter=[v for v in i["data"] if v != ""], count=len(i["data"]))
    valid = {u for u in i["requested"] if u in artifact
             and type(artifact[u]) is type(values[u]) and artifact[u] == values[u]}
    missing = set(i["requested"]) - valid
    if i["review_pending"]:
        status, boundary, expected = "REVIEW", "review", set()
    elif i["observed_failure"] != "none":
        status, boundary, expected = "FAILED", i["observed_failure"], set()
    elif not i["permitted"]:
        status, boundary, expected = "REFUSED", "policy", set()
    elif i["budget_exhausted"]:
        status, boundary, expected = "PARTIAL", "budget", set()
    else:
        expected = set(i["requested"]) & set(i["permitted"])
        status = "COMPLETE" if expected == set(i["requested"]) else "PARTIAL"
        boundary = None if status == "COMPLETE" else "policy"
    result = []
    if (sorted(report["completed_units"]) != sorted(valid)
            or sorted(report["omitted_units"]) != sorted(missing)
            or (missing and report["boundary"] is None)):
        result.append("WIT-P01")
    if report["status"] == "COMPLETE" and missing:
        result.append("WIT-P02")
    if report["boundary"] != boundary or report["status"] != status:
        result.append("WIT-P03")
    if not expected.issubset(valid):
        result.append("WIT-P04")
    if set(artifact) - set(i["permitted"]) or (
            artifact and (i["review_pending"] or i["observed_failure"] != "none" or i["budget_exhausted"])):
        result.append("WIT-P05")
    return result


def proposal(capture):
    failed = failures(capture)
    return dict(objectiveMatches=True, grantCurrent=True,
                evidenceComplete=not any(p in failed for p in ("WIT-P02", "WIT-P04")),
                prohibitedMeans="WIT-P05" in failed, dominated=False, withinBudget=True,
                objectionsRetained=not any(p in failed for p in ("WIT-P01", "WIT-P03")),
                sharedGate=True, deferRequested=False, delayUnsafe=False)


def quint_matches(capture, quint):
    p = proposal(capture)
    outcome = "block" if p["prohibitedMeans"] else (
        "review" if not p["evidenceComplete"] or not p["objectionsRetained"] else "allow")
    return (quint["proposal"] == p and quint["expected_outcome"] == outcome
            and quint["expected_complete"] is False and quint["parent_revoked"] is False
            and quint["accepted"] is False and quint["mission_complete"] is False)


def validate(document, model):
    errors = [e.message for e in jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text()))
              .iter_errors(document)]
    if errors:
        return errors
    if [c["id"] for c in document["cases"]] != [f"WIT-T{i:02d}" for i in range(1, 11)]:
        errors.append("case inventory mismatch")
    if [m["id"] for m in document["mutants"]] != [f"WIT-M{i:02d}" for i in range(1, 7)]:
        errors.append("mutant inventory mismatch")
    if [m["operator"] for m in document["mutants"]] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    for mutant, seed, predicate in zip(document["mutants"],
                                       ("WIT-T01", "WIT-T01", "WIT-T03", "WIT-T02", "WIT-T07", "WIT-T05"),
                                       ("WIT-P01", "WIT-P03", "WIT-P01", "WIT-P02", "WIT-P03", "WIT-P05")):
        if (mutant["case_id"], mutant["predicate_id"]) != (seed, predicate):
            errors.append("mutant seed/predicate mismatch")
    links = next(p["scenario_tests"] for p in json.loads(MAP.read_text())["models"][0]["properties"]
                 if p["invariant"] == "interventionRetainsObjectionsAndGate")
    for item in (*document["cases"], *document["mutants"]):
        q = item["quint"]
        if pas.render_case(q) not in model or len(re.findall(
                rf'\brun {re.escape(q["quint_test"])}\s*=', model)) != 1:
            errors.append(f'{item["id"]}: literal Quint mismatch')
        if q["quint_test"] not in links:
            errors.append(f'{item["id"]}: missing formal link')
    for a, b in document["pairs"]:
        by_id = {c["id"]: c for c in document["cases"]}
        first, second = by_id[a], by_id[b]
        if (first["inputs"]["framing"] != "safety" or second["inputs"]["framing"] != "capabilities"
                or {k: v for k, v in first["inputs"].items() if k != "framing"}
                != {k: v for k, v in second["inputs"].items() if k != "framing"}):
            errors.append("non-equivalent framing pair")
    return errors


def run_suite(document, runner=reference.exercise):
    cases, mutants = [], []
    by_id = {c["id"]: c for c in document["cases"]}
    for case in document["cases"]:
        try:
            observed = runner(case["inputs"])
            passed = (observed["inputs"] == case["inputs"] and failures(observed) == []
                      and observed["artifact"] == case["expected_artifact"]
                      and observed["report"] == case["expected_report"]
                      and quint_matches(observed, case["quint"]))
            cases.append(dict(case=case["id"], result="PASS" if passed else "FAIL", capture=observed))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            cases.append(dict(case=case["id"], result="INVALID", error=type(exc).__name__))
    captures = {c["case"]: c for c in cases}
    paired = all(captures[a].get("capture", {}).get("artifact")
                 == captures[b].get("capture", {}).get("artifact")
                 and captures[a].get("capture", {}).get("report")
                 == captures[b].get("capture", {}).get("report") for a, b in document["pairs"])
    for mutant in document["mutants"]:
        try:
            seed = captures[mutant["case_id"]]
            if seed["result"] != "PASS":
                mutants.append(dict(mutant=mutant["id"], result="INVALID", error="InvalidSafeSeed"))
                continue
            observed = runner(by_id[mutant["case_id"]]["inputs"], mutant["operator"])
            failed = failures(observed)
            killed = (observed["inputs"] == seed["capture"]["inputs"]
                      and mutant["predicate_id"] in failed
                      and (observed["artifact"], observed["report"])
                      != (seed["capture"]["artifact"], seed["capture"]["report"]))
            result = "KILLED" if killed else "SURVIVED"
            if killed and not quint_matches(observed, mutant["quint"]):
                result = "INVALID"
            mutants.append(dict(mutant=mutant["id"], result=result, violations=failed, capture=observed))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            mutants.append(dict(mutant=mutant["id"], result="INVALID", error=type(exc).__name__))
    counts = Counter(m["result"] for m in mutants)
    denominator = counts["KILLED"] + counts["SURVIVED"]
    return dict(claim="REFERENCE_TESTED_ONLY", artifact_version=document["artifact_version"],
                vectors_sha256=hashlib.sha256(json.dumps(document, sort_keys=True).encode()).hexdigest(),
                cases=cases, pairs_match=paired, mutants=mutants, mutation_summary=dict(
                    declared=len(mutants), killed=counts["KILLED"], survived=counts["SURVIVED"],
                    invalid=counts["INVALID"], denominator=denominator,
                    score=counts["KILLED"] / denominator if denominator else None),
                success=paired and all(c["result"] == "PASS" for c in cases)
                and all(m["result"] == "KILLED" for m in mutants))


def main():
    document = load()
    errors = validate(document, MODEL.read_text())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    report = run_suite(document)
    print(json.dumps(report, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
