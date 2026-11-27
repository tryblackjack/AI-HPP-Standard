#!/usr/bin/env python3
"""Check finite commerce records, exact core links and observed local mutants."""
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from examples import commerce_trust_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/commerce-trust-vectors.json"
SCHEMA = ROOT / "schemas/commerce-trust-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MAP = ROOT / "data/formal-assurance-map.json"


def load():
    return json.loads(VECTORS.read_text())


def inputs_for(document, case):
    i = reference.materialize(document["base"], case["changes"])
    if case["approve"]:
        i["review"]["binding"] = reference.binding(i)
    if case["rebind"]:
        i["admission_binding"] = reference.binding(i)
    return i


def render_case(case):
    p = case["expected_premises"]
    return "\n".join([
        f'  run {case["quint_test"]} = {{', "    init",
        f'      .then(assessCommerce({ego.literal(p)}))',
        "      .then(assessRobotAction)", "      .then(executeRobotAction)",
        "      .then(check(all {",
        f'        s.grounding.reason == {ego.literal(case["reason"])},',
        f'        s.robot.audit.executed == {ego.literal(case["effect"])},',
        "        allCoreInvariants,", "      }))", "  }",
    ])


def render_integrations(document):
    good = document["cases"][0]["expected_premises"]
    bad = {**good, "reviewEffective": False}
    blocks = {}
    for name, first, second, revoke in (
        ("commerceChangedAfterApprovalTest", good, bad, False),
        ("commerceReviewedRecoveryTest", bad, good, False),
        ("commerceRecoveryCannotRestoreRevokedGrantTest", bad, good, True),
    ):
        lines = [f"  run {name} = {{", "    init",
                 f"      .then(assessCommerce({ego.literal(first)}))"]
        if revoke:
            lines.append("      .then(revokeParent(true))")
        lines += [f"      .then(assessCommerce({ego.literal(second)}))",
                  "      .then(assessRobotAction)", "      .then(executeRobotAction)",
                  f"      .then(check(all {{ s.robot.audit.executed == {ego.literal(not revoke and second == good)},",
                  "        allCoreInvariants }))", "  }"]
        blocks[name] = "\n".join(lines)
    return blocks


def validate(document, model):
    errors = [e.message for e in jsonschema.Draft202012Validator(
        json.loads(SCHEMA.read_text())).iter_errors(document)]
    if errors:
        return errors
    mapping = json.loads(MAP.read_text())
    links = next(p["scenario_tests"] for p in mapping["models"][0]["properties"]
                 if p["invariant"] == "effectsRequireGroundingAndOversight")
    ids = [c["id"] for c in document["cases"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate case")
    for case in document["cases"]:
        if (render_case(case) not in model or case["quint_test"] not in links
                or len(re.findall(rf'\brun {case["quint_test"]}\s*=', model)) != 1):
            errors.append(f'{case["id"]}: literal core/map mismatch')
    for name, block in render_integrations(document).items():
        if block not in model or name not in links:
            errors.append(f"{name}: missing integration")
    if [m["operator"] for m in document["mutants"]] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    return errors


def run_suite(document, runner=reference.exercise):
    # Expected premises/reasons/effects are authored fixture oracles. Do not
    # derive expected acceptance by calling the candidate admission function.
    cases, captures, mutants = [], {}, []
    by_id = {c["id"]: c for c in document["cases"]}
    for case in document["cases"]:
        try:
            i = inputs_for(document, case)
            capture = runner(deepcopy(i))
            captures[case["id"]] = capture
            expected = dict(marker="SYNTHETIC_ONLY", binding=reference.binding(i),
                            action=i["request"]["action"]) if case["effect"] else None
            remaining = (0 if case["effect"] and i["request"]["action"] != "recommend"
                         else i["review"]["remaining_uses"])
            ok = (capture["inputs"] == i and capture["candidate_premises"] == case["expected_premises"]
                  and capture["effect"] == expected and capture["remaining_uses"] == remaining
                  and reference.reason(capture["candidate_premises"]) == case["reason"])
            cases.append(dict(case=case["id"], result="PASS" if ok else "FAIL"))
        except (OSError, ValueError, TypeError, KeyError) as exc:
            cases.append(dict(case=case["id"], result="INVALID", error=type(exc).__name__))
    for m in document["mutants"]:
        try:
            case = by_id[m["case_id"]]
            i = inputs_for(document, case)
            capture = runner(deepcopy(i), m["operator"])
            effect = dict(marker="SYNTHETIC_ONLY", binding=reference.binding(i),
                          action=i["request"]["action"])
            seed_ok = next(c["result"] for c in cases if c["case"] == m["case_id"]) == "PASS"
            valid = (seed_ok and not case["effect"] and not case["expected_premises"][m["field"]]
                     and capture["inputs"] == i == captures[m["case_id"]]["inputs"]
                     and capture["effect"] in (None, effect))
            mutants.append(dict(operator=m["operator"], result="INVALID" if not valid
                                else "KILLED" if capture["effect"] == effect else "SURVIVED"))
        except (OSError, ValueError, TypeError, KeyError, StopIteration) as exc:
            mutants.append(dict(operator=m["operator"], result="INVALID", error=type(exc).__name__))
    counts = Counter(m["result"] for m in mutants)
    return dict(claim="REFERENCE_TESTED_ONLY", vectors_sha256=reference.digest(document),
        cases=cases, mutants=mutants, mutation_summary=dict(killed=counts["KILLED"],
        survived=counts["SURVIVED"], invalid=counts["INVALID"]),
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
