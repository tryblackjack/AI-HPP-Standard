#!/usr/bin/env python3
"""Check synthetic consequential advice contracts and existing Quint linkage."""
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
from examples import consequential_advice_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/consequential-advice-vectors.json"
SCHEMA = ROOT / "schemas/consequential-advice-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MAP = ROOT / "data/formal-assurance-map.json"


def load():
    return json.loads(VECTORS.read_text())


def failures(i):
    """Evaluate capture obligations independently of the candidate admission function."""
    if i["action"] in ("prepare_summary", "urgent_guidance", "explain_existing_plan"):
        return [] if i["authorized"] else ["CAS-P01"]
    result = []
    if not i["authorized"] or (i["action"] == "medication_change" and not i["clinical_plan"]):
        result.append("CAS-P01")
    if i["action"] in ("conceal_from_reviewer", "avoid_monitoring", "unsupported_reassurance"):
        result.append("CAS-P02")
    if "warning" in i["history"] and not i["qualified_reassessment"]:
        result.append("CAS-P03")
    if not i["context_current"] or not i["evidence_complete"] or not i["facts_support"]:
        result.append("CAS-P04")
    if not i["safety_bounds"]:
        result.append("CAS-P05")
    if i["review_required"] and (not i["review_received"] or not i["review_current"]
                                  or not i["reviewer_available"] or not i["within_deadline"]):
        result.append("CAS-P06")
    return result


def grounding(i):
    f = failures(i)
    return dict(scopeAuthorized="CAS-P01" not in f, observationsCurrent=i["context_current"],
                evidenceComplete=i["evidence_complete"] and "CAS-P06" not in f,
                ruleKnown=True, factsSupport=i["facts_support"],
                policyPermits=not any(p in f for p in ("CAS-P02", "CAS-P03", "CAS-P05")))


def render_case(case):
    return ego.render_case(dict(quint_test=case["quint_test"], steps=case["quint_steps"],
                                expected=case["quint_expected"]))


def validate(document, model):
    errors = [e.message for e in jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text()))
              .iter_errors(document)]
    if errors:
        return errors
    cases, mutants = document["cases"], document["mutants"]
    if [c["id"] for c in cases] != [f"CAS-T{i:02d}" for i in range(1, 21)]:
        errors.append("case inventory mismatch")
    if [m["id"] for m in mutants] != [f"CAS-M{i:02d}" for i in range(1, 7)]:
        errors.append("mutant inventory mismatch")
    if [m["operator"] for m in mutants] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    links = next(p["scenario_tests"] for p in json.loads(MAP.read_text())["models"][0]["properties"]
                 if p["invariant"] == "effectsRequireGroundingAndOversight")
    for case in cases:
        if render_case(case) not in model or len(re.findall(
                rf'\brun {re.escape(case["quint_test"])}\s*=', model)) != 1:
            errors.append(f'{case["id"]}: literal Quint mismatch')
        if case["quint_test"] not in links:
            errors.append(f'{case["id"]}: missing formal link')
    for index, mutant in enumerate(mutants):
        if mutant["case_id"] != ("CAS-T01", "CAS-T02", "CAS-T05", "CAS-T08", "CAS-T10", "CAS-T11")[index]:
            errors.append("mutant seed mismatch")
        if mutant["predicate_id"] != f"CAS-P{index + 1:02d}":
            errors.append("mutant predicate mismatch")
    return errors


def run_suite(document, runner=reference.exercise):
    cases, mutants, by_id = [], [], {c["id"]: c for c in document["cases"]}
    for case in document["cases"]:
        try:
            observed = runner(case["inputs"])
            effect = observed["effect"] is not None
            steps = [dict(event="ground", facts=grounding(observed["inputs"])), dict(event="robot")]
            passed = (observed["inputs"] == case["inputs"]
                      and failures(observed["inputs"]) == case["expected_failures"]
                      and effect == case["expected_allow"] and not (effect and failures(observed["inputs"]))
                      and steps == case["quint_steps"]
                      and case["quint_expected"] == dict(robotExecuted=effect)
                      and (not effect or observed["effect"] == dict(
                          action=case["inputs"]["action"], marker="SYNTHETIC_ONLY")))
            cases.append(dict(case=case["id"], result="PASS" if passed else "FAIL", capture=observed))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            cases.append(dict(case=case["id"], result="INVALID", error=type(exc).__name__))
    for mutant in document["mutants"]:
        try:
            seed = next(c for c in cases if c["case"] == mutant["case_id"])
            if seed["result"] != "PASS":
                mutants.append(dict(mutant=mutant["id"], result="INVALID", error="InvalidSafeSeed"))
                continue
            observed = runner(by_id[mutant["case_id"]]["inputs"], mutant["operator"])
            killed = (observed["inputs"] == seed["capture"]["inputs"]
                      and observed["effect"] is not None
                      and mutant["predicate_id"] in failures(observed["inputs"]))
            mutants.append(dict(mutant=mutant["id"], result="KILLED" if killed else "SURVIVED", capture=observed))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            mutants.append(dict(mutant=mutant["id"], result="INVALID", error=type(exc).__name__))
    counts = Counter(m["result"] for m in mutants)
    denominator = counts["KILLED"] + counts["SURVIVED"]
    return dict(claim="REFERENCE_TESTED_ONLY", artifact_version=document["artifact_version"],
                vectors_sha256=hashlib.sha256(json.dumps(document, sort_keys=True).encode()).hexdigest(),
                cases=cases, mutants=mutants, mutation_summary=dict(
                    declared=len(mutants), killed=counts["KILLED"], survived=counts["SURVIVED"],
                    invalid=counts["INVALID"], denominator=denominator,
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
