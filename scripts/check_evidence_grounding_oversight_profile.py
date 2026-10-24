#!/usr/bin/env python3
"""Validate portable EGO fixtures against their executable core Quint tests."""
from __future__ import annotations

import json
from pathlib import Path
import re

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
PROFILE = "docs/evidence-grounding-and-oversight-assurance-profile-2026-10.md"
VECTORS = "examples/evidence-grounding-oversight-vectors.json"
SCHEMA = "schemas/evidence-grounding-oversight-vectors.schema.json"
MODEL = "formal/ai_hpp_core.qnt"
PREDICATES = {f"EGO-P{i:02d}" for i in range(1, 9)}
CASE_IDS = {f"EGO-T{i:02d}" for i in range(1, 41)}
MUTANT_IDS = {f"EGO-M{i:02d}" for i in range(1, 13)}


def load(path: str) -> dict:
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def literal(value) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        return "{ " + ", ".join(f"{key}: {literal(item)}" for key, item in value.items()) + " }"
    return json.dumps(value)


EXPECTED_FIELDS = {
    "reason": "s.grounding.reason", "stage": "s.oversight.stage",
    "required": "s.oversight.required", "owner": "s.oversight.owner",
    "offeredOwner": "s.oversight.offeredOwner", "ticks": "s.oversight.ticks",
    "eventId": "s.oversight.eventId", "receiptEvent": "s.oversight.receiptEvent",
    "sentEvidence": "s.oversight.sentEvidence", "resolutionEvidence": "s.oversight.resolutionEvidence",
    "custodyGap": "s.oversight.custodyGap", "claimValid": "s.claimValid",
    "robotExecuted": "s.robot.audit.executed", "interventionOutcome": "s.interventionAudit.outcome",
    "deploymentOutcome": "s.lastDecision",
}


def render_step(event: dict) -> list[str]:
    name = event["event"]
    if name == "ground":
        return [f'assessGroundedProposal({literal(event["facts"])})']
    if name == "incident":
        return [f'registerOversightObligation({literal(event["required"])}, {literal(event["hold"])})']
    if name == "route":
        return ["configureOversightPath(" + ", ".join(literal(event[k]) for k in
                ("authorized", "minimal", "independent", "durable")) + ")"]
    if name == "receipt":
        return [f'recordOversightReceipt({event["eventId"]})']
    if name == "offer":
        return [f'offerOversightHandoff({event["owner"]})']
    if name in ("review", "resolve", "accept", "recover"):
        function = {"review": "reviewOversightIncident", "resolve": "resolveOversightIncident",
                    "accept": "acceptOversightHandoff", "recover": "recoverOversightCustody"}[name]
        return [f'{function}({literal(event["evidence"])})']
    return {
        "queue": ["queueOversightNotice"], "send": ["dispatchOversightNotice"],
        "tick": ["tickOversightDeadline"], "restart": ["restartOversightWorker"],
        "robot": ["assessRobotAction", "executeRobotAction"],
        "intervention": ["evaluateIntervention(permittedIntervention)"],
        "child": ["evaluateChildDeployment(1, true, true, true)"],
        "completion_fixture": ["evaluateChildDeployment(1, true, true, true)",
                               "terminateChild(true, true)", "completeResidueInventory"],
        "completion": ["assessCompletionClaim"], "revoke": ["revokeParent(true)"],
        "accept_task": ["recordTaskAcceptance"],
    }[name]


def render_case(case: dict) -> str:
    """Render literal events and authored expectations, not a policy oracle."""
    lines = [f'  run {case["quint_test"]} = {{', "    init"]
    lines.extend(f"      .then({command})" for event in case["steps"] for command in render_step(event))
    lines.append("      .then(check(all {")
    for key, value in case["expected"].items():
        lines.append(f"        {EXPECTED_FIELDS[key]} == {literal(value)},")
    lines.extend(["        allCoreInvariants,", "      }))", "  }"])
    return "\n".join(lines)


def render_mutant(mutant: dict) -> str:
    seeds = {
        "initial": ([], "groundingPermits"),
        "ground_unknown": (["assessGroundedProposal({ ...supportedGrounding, evidenceComplete: false })"],
                           's.grounding.reason == "insufficient_evidence"'),
        "robot": (["assessRobotAction", "executeRobotAction", "registerOversightObligation(true, true)"],
                  "s.robot.audit.executed and not(evidenceOversightPermits)"),
        "detected": (["registerOversightObligation(true, true)"], "s.oversight.stage == 1"),
        "queued": (["registerOversightObligation(true, true)", "queueOversightNotice"], "s.oversight.stage == 2"),
        "sent": (["registerOversightObligation(true, true)", "queueOversightNotice", "dispatchOversightNotice"],
                 "s.oversight.stage == 3"),
        "received": (["registerOversightObligation(true, true)", "queueOversightNotice", "dispatchOversightNotice",
                      "recordOversightReceipt(1)"], "s.oversight.stage == 4"),
        "resolved": (["registerOversightObligation(true, true)", "queueOversightNotice", "dispatchOversightNotice",
                      "recordOversightReceipt(1)", "reviewOversightIncident(true)", "resolveOversightIncident(true)"],
                     "s.oversight.stage == 6"),
        "restarted": (["registerOversightObligation(true, true)", "queueOversightNotice", "restartOversightWorker"],
                      's.oversight.stage == 2 and s.oversight.lastTransition == "restart"'),
    }
    commands, condition = seeds[mutant["seed"]]
    lines = [f'  run {mutant["quint_test"]} = {{', "    init"]
    lines.extend(f"      .then({command})" for command in commands)
    lines.extend([
        f"      .then(check(all {{ allCoreInvariants, {condition} }}))",
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
    actual = {name for name in blocks if name.startswith(("ego", "mutantEgo"))}
    if set(names) != actual:
        errors.append("EGO executable witness inventory mismatch")
    operators = [m["operator"] for m in document["mutants"]]
    actual_operators = re.findall(r"^  action (mutantEgo\w+): bool", model, re.M)
    if len(set(operators)) != len(operators) or sorted(operators) != sorted(actual_operators):
        errors.append("unsafe operator inventory mismatch")
    step = re.search(r"^  action step: bool = \{(.*?)^  \}", model, re.M | re.S)
    if not step or any(re.search(rf"\b{operator}\b", step[1]) for operator in operators):
        errors.append("unsafe operator admitted to normal step")
    if {m["predicate_id"] for m in document["mutants"]} != PREDICATES:
        errors.append("mutant predicate coverage mismatch")
    for boundary in ("ACTIVE_INFORMATIVE", "post-rc.1", "v4.3.0 baseline is unchanged",
                     "not a truth oracle", "REFERENCE_TESTED"):
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
    print("EGO profile synchronized: 8 predicates, 40 cases, 12 Quint mutation witnesses. "
          "Execute Quint to determine outcomes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
