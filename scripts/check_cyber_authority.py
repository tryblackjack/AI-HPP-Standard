#!/usr/bin/env python3
"""Execute finite scope-binding mutants and check their literal Quint linkage."""
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
from examples import cyber_authority_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/cyber-authority-vectors.json"
SCHEMA = ROOT / "schemas/cyber-authority-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MAP = ROOT / "data/formal-assurance-map.json"
PROFILE = ROOT / "docs/cyber-operation-authority-assurance-note-2026-10.md"


def load():
    return json.loads(VECTORS.read_text())


def failed_checks(capture):
    """Contract oracle reads recorded inputs, never the candidate's decision."""
    g, r, now = (capture[k] for k in ("grant", "request", "clock"))
    failures = []
    if not (g["verified"] and g["owner_proof"] and g["active"] and now < g["expires"]):
        failures.append("CBA-P01")
    if (r["target"] not in g["targets"] or r["operation"] not in g["operations"]
            or r["credential"] != g["credential"]):
        failures.append("CBA-P02")
    if (r["principal"] != g["principal"] or (r["delegated"] and (
            not g["delegation_verified"] or not g["parent_active"]))):
        failures.append("CBA-P03")
    if r["skill_digest"] != g["skill_digest"]:
        failures.append("CBA-P04")
    if r["recipient"] not in g["recipients"] or r["data_class"] not in g["data_classes"]:
        failures.append("CBA-P05")
    if failures and r["monitor"] == "benign":
        failures.append("CBA-P06")
    return failures


def abstract_grounding(capture):
    failures = failed_checks(capture)
    return dict(scopeAuthorized=not any(p in failures for p in ("CBA-P01", "CBA-P02", "CBA-P03")),
                observationsCurrent=True, evidenceComplete="CBA-P04" not in failures,
                ruleKnown=True, factsSupport=True, policyPermits="CBA-P05" not in failures)


def render_case(case):
    return ego.render_case(dict(quint_test=case["quint_test"], steps=case["quint_steps"],
                                expected=case["quint_expected"]))


def validate(document, model, mapping=None):
    errors = [f"schema: {e.message}" for e in jsonschema.Draft202012Validator(
        json.loads(SCHEMA.read_text())).iter_errors(document)]
    if errors:
        return errors
    cases, mutants = document["cases"], document["mutants"]
    if [c["id"] for c in cases] != [f"CBA-T{i:02d}" for i in range(1, 15)]:
        errors.append("case inventory mismatch")
    if [c["scenario"] for c in cases] != list(reference.SCENARIOS):
        errors.append("scenario inventory mismatch")
    if [m["id"] for m in mutants] != [f"CBA-M{i:02d}" for i in range(1, 8)]:
        errors.append("mutant inventory mismatch")
    if [m["operator"] for m in mutants] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    profile = PROFILE.read_text()
    if "ACTIVE_INFORMATIVE" not in profile[:250] or any(
            f"`CBA-P{i:02d}" not in profile for i in range(1, 7)):
        errors.append("profile predicate/status mismatch")
    mapping = json.loads(MAP.read_text()) if mapping is None else mapping
    linked = next(p["scenario_tests"] for p in mapping["models"][0]["properties"]
                  if p["invariant"] == "effectsRequireGroundingAndOversight")
    for case in cases:
        if render_case(case) not in model or len(re.findall(
                rf'\brun {re.escape(case["quint_test"])}\s*=', model)) != 1:
            errors.append(f'{case["id"]}: literal Quint case mismatch')
        if case["quint_test"] not in linked:
            errors.append(f'{case["id"]}: missing formal map link')
    for i, mutant in enumerate(mutants, 1):
        predicate = ("CBA-P01", "CBA-P02", "CBA-P02", "CBA-P03", "CBA-P04", "CBA-P05", "CBA-P06")[i - 1]
        if mutant["case_id"] != f"CBA-T{i:02d}" or mutant["predicate_id"] != predicate:
            errors.append("mutant case/predicate mismatch")
    return errors


def run_suite(document, runner=reference.exercise):
    cases, captures, mutants = [], {}, []
    for case in document["cases"]:
        try:
            capture = runner(case["scenario"])
            captures[case["id"]] = capture
            failures = failed_checks(capture)
            steps = [dict(event="ground", facts=abstract_grounding(capture)), dict(event="robot")]
            effect = capture["effect"] is not None
            # An effect must also reflect the exact requested operation and destination.
            exact = not effect or capture["effect"] == dict(
                **{k: capture["request"][k] for k in ("target", "operation", "recipient", "data_class")},
                marker="SYNTHETIC_ONLY")
            passed = (effect == case["expected_effect"] and exact
                      and failures == case["expected_failed_checks"]
                      and not (effect and failures) and steps == case["quint_steps"]
                      and case["quint_expected"] == dict(robotExecuted=effect))
            cases.append(dict(case=case["id"], result="PASS" if passed else "FAIL", capture=capture))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            cases.append(dict(case=case["id"], result="INVALID", error=type(exc).__name__))
    by_id = {c["id"]: c for c in document["cases"]}
    for mutant in document["mutants"]:
        try:
            seed = next(c for c in cases if c["case"] == mutant["case_id"])
            if seed["result"] != "PASS":
                mutants.append(dict(mutant=mutant["id"], result="INVALID", error="InvalidSafeSeed"))
                continue
            capture = runner(by_id[mutant["case_id"]]["scenario"], mutant["operator"])
            failures = failed_checks(capture)
            killed = (capture["effect"] is not None and mutant["predicate_id"] in failures
                      and capture != captures[mutant["case_id"]])
            mutants.append(dict(mutant=mutant["id"], result="KILLED" if killed else "SURVIVED",
                                failed_checks=failures, capture=capture))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            mutants.append(dict(mutant=mutant["id"], result="INVALID", error=type(exc).__name__))
    counts = Counter(m["result"] for m in mutants)
    denominator = counts["KILLED"] + counts["SURVIVED"]
    return dict(claim="REFERENCE_TESTED_ONLY", artifact_version=document["artifact_version"],
                vectors_sha256=hashlib.sha256(json.dumps(document, sort_keys=True).encode()).hexdigest(),
                cases=cases, mutants=mutants, mutation_summary=dict(
                    declared=len(mutants), killed=counts["KILLED"], survived=counts["SURVIVED"],
                    invalid=counts["INVALID"], not_applicable=0, denominator=denominator,
                    score=counts["KILLED"] / denominator if denominator else None),
                success=all(c["result"] == "PASS" for c in cases)
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
