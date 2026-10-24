#!/usr/bin/env python3
"""Execute finite boundary mutants and synchronize their safe Quint abstractions."""
from __future__ import annotations

from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import sys
import subprocess

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from examples import oversight_boundary_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/oversight-boundary-vectors.json"
SCHEMA = ROOT / "schemas/oversight-boundary-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"


def load():
    return json.loads(VECTORS.read_text())


def render_case(case):
    return ego.render_case({"quint_test": case["quint_test"], "steps": case["quint_steps"],
                            "expected": case["quint_expected"]})


def expected_steps(observed, scenario):
    steps = [{"event": "ground", "facts": reference.abstract_grounding(observed)}]
    if scenario == "revoked_token":
        steps += [{"event": "revoke"}]
    if observed["incident_required"]:
        steps += [{"event": "incident", "required": True, "hold": False},
                  {"event": "queue"}, {"event": "send"}, {"event": "receipt", "eventId": 1}]
    steps += [{"event": "child" if scenario in ("unmonitored_child", "monitored_child") else "robot"}]
    return steps


def violations(observed):
    """Read captures against contract obligations, independently of admission code."""
    found = {}
    if observed["effect"] and (not observed["authority_active"]
                               or not observed["request_authorized"] or not observed["monitors_ready"]):
        found["EGO-P02"] = ["effect_without_admission"]
    if observed["incident_required"] and not observed["notice_received"]:
        found["EGO-P03"] = ["required_notice_missing"]
    return found


def validate(document, model):
    errors = [f"schema: {e.message}" for e in jsonschema.Draft202012Validator(
        json.loads(SCHEMA.read_text())).iter_errors(document)]
    if errors:
        return errors
    cases = document["cases"]
    if [c["id"] for c in cases] != [f"BND-T{i:02d}" for i in range(1, 9)]:
        errors.append("case inventory mismatch")
    if [c["scenario"] for c in cases] != list(reference.SCENARIOS):
        errors.append("scenario inventory mismatch")
    names = [c["quint_test"] for c in cases]
    actual = re.findall(r"^  run (boundary\w+Test) =", model, re.M)
    if len(set(names)) != 8 or sorted(names) != sorted(actual):
        errors.append("Quint witness inventory mismatch")
    mapping = json.loads((ROOT / "data/formal-assurance-map.json").read_text())
    mapped = {p["invariant"]: p for p in mapping["models"][0]["properties"]}
    for case in cases:
        if set(case["predicate_ids"]) != {"EGO-P02", "EGO-P03", "EGO-P04"}:
            errors.append(f'{case["id"]}: predicate link mismatch')
        if render_case(case) not in model:
            errors.append(f'{case["id"]}: literal Quint fixture differs')
        invariant = ("allowRequiresAuthorityEvidence" if case["scenario"] in
                     ("unmonitored_child", "monitored_child") else "effectsRequireGroundingAndOversight")
        if case["quint_test"] not in mapped[invariant]["scenario_tests"]:
            errors.append(f'{case["id"]}: missing formal trace link')
    mutants = document["mutants"]
    if [m["id"] for m in mutants] != [f"BND-M{i:02d}" for i in range(1, 5)]:
        errors.append("mutant inventory mismatch")
    if [m["operator"] for m in mutants] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    for i, mutant in enumerate(mutants, 1):
        if mutant["case_id"] != f"BND-T{i:02d}":
            errors.append("mutant case link mismatch")
        if mutant["predicate_id"] != ("EGO-P03" if i == 1 else "EGO-P02"):
            errors.append("mutant predicate mismatch")
        if mutant["witness"] != ("required_notice_missing" if i == 1 else "effect_without_admission"):
            errors.append("mutant witness mismatch")
    return errors


def run_suite(document, runner=reference.exercise):
    results, captures = [], {}
    for case in document["cases"]:
        try:
            observed = runner(case["scenario"])
            captures[case["id"]] = observed
            mismatch = [k for k, v in case["expected"].items() if observed.get(k) != v]
            if expected_steps(observed, case["scenario"]) != case["quint_steps"]:
                mismatch.append("Quint observation abstraction")
            # Link the observed effect and receipt directly to authored Quint expectations.
            key = "deploymentOutcome" if case["scenario"] in ("unmonitored_child", "monitored_child") else "robotExecuted"
            effect = case["quint_expected"][key]
            if (effect == "allow" if isinstance(effect, str) else effect) != observed["effect"]:
                mismatch.append("Quint effect")
            if case["quint_expected"]["stage"] != (4 if observed["notice_received"] else 0):
                mismatch.append("Quint delivery")
            result = "FAIL" if mismatch or violations(observed) else "PASS"
            results.append({"case": case["id"], "result": result, "mismatch": mismatch,
                            "capture": observed})
        except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
            results.append({"case": case["id"], "result": "INVALID", "error": type(exc).__name__})
    mutants = []
    cases = {c["id"]: c for c in document["cases"]}
    for mutant in document["mutants"]:
        try:
            case = cases[mutant["case_id"]]
            baseline = captures.get(case["id"])
            safe = next((r["result"] == "PASS" for r in results if r["case"] == case["id"]), False)
            if not safe:
                mutants.append({"mutant": mutant["id"], "result": "INVALID", "error": "InvalidSafeSeed"})
                continue
            observed = runner(case["scenario"], mutant["operator"])
            found = violations(observed)
            killed = safe and observed != baseline and mutant["witness"] in found.get(mutant["predicate_id"], [])
            mutants.append({"mutant": mutant["id"], "result": "KILLED" if killed else "SURVIVED",
                            "violations": found, "capture": observed})
        except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
            mutants.append({"mutant": mutant["id"], "result": "INVALID", "error": type(exc).__name__})
    counts = Counter(m["result"] for m in mutants)
    return {"claim": "REFERENCE_TESTED_ONLY", "artifact_version": document["artifact_version"],
            "vectors_sha256": hashlib.sha256(json.dumps(document, sort_keys=True).encode()).hexdigest(),
            "cases": results, "mutants": mutants, "mutation_summary": {
                "declared": len(mutants), "killed": counts["KILLED"], "survived": counts["SURVIVED"],
                "invalid": counts["INVALID"], "not_applicable": 0,
                "denominator": counts["KILLED"] + counts["SURVIVED"],
                "score": counts["KILLED"] / (counts["KILLED"] + counts["SURVIVED"])
                if counts["KILLED"] + counts["SURVIVED"] else None,
            },
            "success": all(r["result"] == "PASS" for r in results)
            and all(m["result"] == "KILLED" for m in mutants)}


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
