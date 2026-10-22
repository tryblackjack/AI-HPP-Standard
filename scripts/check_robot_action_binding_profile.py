#!/usr/bin/env python3
"""Validate portable RAB fixtures against their executable core Quint tests."""
from __future__ import annotations

import json
from pathlib import Path
import re

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
PROFILE = "docs/robot-action-binding-assurance-profile-2026-10.md"
VECTORS = "examples/robot-action-binding-vectors.json"
SCHEMA = "schemas/robot-action-binding-vectors.schema.json"
MODEL = "formal/ai_hpp_core.qnt"
PREDICATES = {f"RAB-P{i:02d}" for i in range(1, 7)}
CASE_IDS = {f"RAB-T{i:02d}" for i in range(1, 23)}
MUTANT_IDS = {f"RAB-M{i:02d}" for i in range(1, 11)}


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def literal(value) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{key}: {literal(item)}" for key, item in value.items()) + " }"
    return json.dumps(value)


def render_step(event: dict) -> str:
    name = event["action"]
    if name == "scope":
        return f'recordRobotScope({literal(event["scope"])})'
    if name == "propose":
        return f'proposeRobotAction({literal(event["proposal"])})'
    if name == "context":
        fields = ("protectedContents", "contextFresh", "historyComplete", "hazardBounded")
        return "changeRobotContext(" + ", ".join(literal(event[key]) for key in fields) + ")"
    if name == "components":
        return f'changeRobotComponents({literal(event["admitted"])})'
    if name == "boundary":
        return f'configureRobotBoundary({literal(event["enforced"])}, {literal(event["evidenceAvailable"])})'
    return {
        "assess": "assessRobotAction", "execute": "executeRobotAction",
        "revoke": "revokeParent(true)", "accept": "recordTaskAcceptance",
        "conflict": "evaluateAssuredChildDeployment(1, true, true, true, true, true, true, true, true, true, true, false)",
    }[name]


def render_case(case: dict) -> str:
    """Render literal event inputs and independent expected outcomes only."""
    lines = [f'  run {case["quint_test"]} = {{', "    init"]
    lines.extend(f"      .then({render_step(event)})" for event in case["steps"])
    lines.extend([
        "      .then(check(all {",
        f'        s.robot.lastOutcome == "{case["expected_outcome"]}",',
        f'        s.robot.audit.executed == {literal(case["expected_executed"])},',
        "        allCoreInvariants,",
        "      }))",
        "  }",
    ])
    return "\n".join(lines)


def render_mutant(mutant: dict) -> str:
    lines = [f'  run {mutant["quint_test"]} = {{', "    init"]
    if mutant["seed"] == "container":
        lines.extend(["      .then(recordRobotScope(robotBoxScope))",
                      "      .then(proposeRobotAction(robotBoxAction))"])
    lines.extend([
        "      .then(assessRobotAction)",
        "      .then(executeRobotAction)",
        "      .then(check(all { s.robot.audit.executed, allCoreInvariants }))",
        f'      .then({mutant["operator"]})',
        f'      .then(check(not({mutant["invariant"]})))',
        "  }",
    ])
    return "\n".join(lines)


def validate(document: dict, profile: str, model: str) -> list[str]:
    errors = [f"schema: {e.message}" for e in
              jsonschema.Draft202012Validator(load(SCHEMA)).iter_errors(document)]
    if errors:
        return errors
    for key, inventory in (("predicates", PREDICATES), ("cases", CASE_IDS),
                           ("mutants", MUTANT_IDS)):
        ids = [item["id"] for item in document[key]]
        if len(ids) != len(set(ids)) or set(ids) != inventory:
            errors.append(f"{key} inventory mismatch")
    for predicate in document["predicates"]:
        if f'`{predicate["id"]} {predicate["name"]}`' not in profile:
            errors.append(f'profile predicate mismatch: {predicate["id"]}')
    names = []
    for case in document["cases"]:
        names.append(case["quint_test"])
        if not set(case["predicate_ids"]).issubset(PREDICATES):
            errors.append(f'{case["id"]}: unknown predicate')
        if case["steps"][-1]["action"] != "execute":
            errors.append(f'{case["id"]}: final event must exercise execution')
        if render_case(case) not in model:
            errors.append(f'{case["id"]}: portable case differs from executable test')
    coverage = {p for case in document["cases"] for p in case["predicate_ids"]}
    if coverage != PREDICATES:
        errors.append("case predicate coverage mismatch")
    blocks = dict(re.findall(r"^  run (\w+) = \{(.*?)^  \}", model, re.M | re.S))
    formal_map = load("data/formal-assurance-map.json")
    properties = formal_map["models"][0]["properties"]
    mapped = {p["invariant"]: p for p in properties}
    for mutant in document["mutants"]:
        names.append(mutant["quint_test"])
        test = blocks.get(mutant["quint_test"], "")
        if render_mutant(mutant) not in model:
            errors.append(f'{mutant["id"]}: mutant seed or kill witness differs')
        invariant = mutant["invariant"]
        if (f'.then({mutant["operator"]})' not in test
                or f"check(not({invariant}))" not in test):
            errors.append(f'{mutant["id"]}: missing executable kill witness')
        prop = mapped.get(invariant, {})
        if (mutant["predicate_id"] not in prop.get("predicate_ids", [])
                or mutant["quint_test"] not in prop.get("mutation_tests", [])):
            errors.append(f'{mutant["id"]}: formal map link mismatch')
    if len(names) != len(set(names)):
        errors.append("duplicate executable witness")
    actual = {name for name in blocks if name.startswith(("rab", "mutantRab"))}
    if set(names) != actual:
        errors.append("RAB executable witness inventory mismatch")
    operators = [m["operator"] for m in document["mutants"]]
    actual_operators = re.findall(r"^  action (mutantRab\w+): bool", model, re.M)
    if len(set(operators)) != len(operators) or sorted(operators) != sorted(actual_operators):
        errors.append("unsafe operator inventory mismatch")
    step = re.search(r"^  action step: bool = \{(.*?)^  \}", model, re.M | re.S)
    if not step or any(re.search(rf"\b{operator}\b", step[1]) for operator in operators):
        errors.append("unsafe operator admitted to normal step")
    if {m["predicate_id"] for m in document["mutants"]} != PREDICATES:
        errors.append("mutant predicate coverage mismatch")
    for boundary in ("ACTIVE_INFORMATIVE", "post-rc.1", "v4.3.0 baseline is unchanged",
                     "not a runtime versioning scheme", "REFERENCE_TESTED"):
        if boundary not in " ".join(profile.split()):
            errors.append(f"missing claim boundary: {boundary}")
    return errors


def main() -> int:
    try:
        errors = validate(load(VECTORS), (ROOT / PROFILE).read_text(encoding="utf-8"),
                          (ROOT / MODEL).read_text(encoding="utf-8"))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("RAB profile synchronized: 6 predicates, 22 cases, 10 Quint mutation witnesses. "
          "Execute Quint to determine outcomes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
