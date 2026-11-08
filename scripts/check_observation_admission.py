#!/usr/bin/env python3
"""Observe synthetic source bytes, execute defects and check existing RAB/EGO links."""
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
from examples import observation_admission_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/observation-admission-vectors.json"
SCHEMA = ROOT / "schemas/observation-admission-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MAP = ROOT / "data/formal-assurance-map.json"


def load():
    return json.loads(VECTORS.read_text())


def bundle_digest(stage):
    raw = {k: stage[k] for k in ("context", "primary", "corroborator", "corroboration_required")}
    return hashlib.sha256(json.dumps(raw, sort_keys=True).encode()).hexdigest()


def admission_failures(stage, request, seen):
    """Independent contract checks; no call to candidate checks/admission logic."""
    observations = [o for o in (stage["primary"], stage["corroborator"]) if o is not None]
    frames = [json.loads(o["raw"]) for o in observations]
    failed = set()
    if not observations:
        failed.add("OBA-P01")
    for observation, frame in zip(observations, frames):
        metadata = observation["source"]
        if (not metadata["admitted"]
                or hashlib.sha256(observation["raw"].encode()).hexdigest() != observation["admitted_digest"]):
            failed.add("OBA-P01")
        c = stage["context"]
        if (frame["session_id"] != c["session_id"] or frame["target_id"] != request["target_id"]
                or frame["epoch"] != c["epoch"] or frame["capture_tick"] > c["now"]
                or c["now"] - frame["capture_tick"] > 3
                or (metadata["source_id"], frame["frame_id"]) in seen):
            failed.add("OBA-P02")
        if (frame["quality"] != "usable" or frame["object"] != "workpiece"
                or not metadata["calibration_current"]):
            failed.add("OBA-P03")
    if stage["corroboration_required"]:
        if stage["corroborator"] is None:
            failed.add("OBA-P04")
        else:
            primary = set(stage["primary"]["source"]["failure_domains"])
            secondary = set(stage["corroborator"]["source"]["failure_domains"])
            if (not primary or not secondary or primary & secondary
                    or stage["primary"]["source"]["source_id"] == stage["corroborator"]["source"]["source_id"]
                    or stage["primary"]["source"]["pipeline_id"] == stage["corroborator"]["source"]["pipeline_id"]):
                failed.add("OBA-P04")
    token = stage["approval"]
    if (not token["issued"] or token["epoch"] != stage["context"]["epoch"]
            or token["bundle_digest"] != bundle_digest(stage)
            or any(token[k] != v for k, v in request.items())):
        failed.add("OBA-P05")
    return sorted(failed)


def receipt_valid(stage, index, request):
    return (stage["effect"] is not None and stage["receipt"] == dict(
        stage=index, bundle_digest=bundle_digest(stage), action_id=request["action_id"]))


def grounding(stage, request, seen):
    failed = admission_failures(stage, request, seen)
    protected = any(json.loads(o["raw"])["object"] == "protected"
                    for o in (stage["primary"], stage["corroborator"]) if o is not None)
    return dict(scopeAuthorized=request["authorized"], observationsCurrent="OBA-P02" not in failed,
                evidenceComplete=not any(p in failed for p in ("OBA-P01", "OBA-P03", "OBA-P04")),
                ruleKnown=True, factsSupport=not protected, policyPermits=True)


def abstract_stages(capture):
    result, seen = [], set()
    request = capture["inputs"]["request"]
    for index, (stage, spec) in enumerate(zip(capture["stages"], capture["inputs"]["stages"]), 1):
        failed = admission_failures(stage, request, seen)
        facts = grounding(stage, request, seen)
        post = dict(facts, evidenceComplete=facts["evidenceComplete"] and receipt_valid(stage, index, request))
        result.append(dict(facts=facts, contextFresh="OBA-P02" not in failed,
                           hazardBounded="OBA-P03" not in failed, reapprove=spec["reapprove"],
                           report=spec["report"], post_facts=post))
        seen.update((o["source"]["source_id"], json.loads(o["raw"])["frame_id"])
                    for o in (stage["primary"], stage["corroborator"]) if o is not None)
    return result


def violations(capture):
    result, seen = [], set()
    request = capture["inputs"]["request"]
    for index, stage in enumerate(capture["stages"], 1):
        failed = admission_failures(stage, request, seen)
        found = failed if stage["effect"] is not None else []
        if stage["complete"] and not receipt_valid(stage, index, request):
            found = [*found, "OBA-P06"]
        result.append(found)
        seen.update((o["source"]["source_id"], json.loads(o["raw"])["frame_id"])
                    for o in (stage["primary"], stage["corroborator"]) if o is not None)
    return result


def render_case(case):
    lines = [f'  run {case["quint_test"]} = {{', "    init", "      .then(assessRobotAction)"]
    for stage, expected in zip(case["quint_stages"], case["expected"]):
        args = f'false, {ego.literal(stage["contextFresh"])}, true, {ego.literal(stage["hazardBounded"])}'
        lines += [f"      .then(changeRobotContext({args}))",
                  f'      .then(assessGroundedProposal({ego.literal(stage["facts"])}))']
        if stage["reapprove"]:
            lines.append("      .then(assessRobotAction)")
        lines += ["      .then(executeRobotAction)", "      .then(check(all {",
                  f'        s.robot.audit.executed == {ego.literal(expected["effect"])},',
                  "        allCoreInvariants,", "      }))"]
        if stage["report"]:
            lines += [f"      .then({command})" for command in ego.render_step(dict(event="completion_fixture"))]
            lines += [f'      .then(assessGroundedProposal({ego.literal(stage["post_facts"])}))',
                      "      .then(assessCompletionClaim)", "      .then(check(all {",
                      f'        s.claimValid == {ego.literal(expected["complete"])},',
                      "        allCoreInvariants,", "      }))"]
    return "\n".join([*lines, "  }"])


def validate(document, model):
    errors = [e.message for e in jsonschema.Draft202012Validator(json.loads(SCHEMA.read_text()))
              .iter_errors(document)]
    if errors:
        return errors
    if [c["id"] for c in document["cases"]] != [f"OBA-T{i:02d}" for i in range(1, 19)]:
        errors.append("case inventory mismatch")
    if [m["id"] for m in document["mutants"]] != [f"OBA-M{i:02d}" for i in range(1, 7)]:
        errors.append("mutant inventory mismatch")
    if [m["operator"] for m in document["mutants"]] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    links = next(p["scenario_tests"] for p in json.loads(MAP.read_text())["models"][0]["properties"]
                 if p["invariant"] == "effectsRequireGroundingAndOversight")
    completion_links = next(p["scenario_tests"] for p in json.loads(MAP.read_text())["models"][0]["properties"]
                            if p["invariant"] == "completionRequiresDischargedOversight")
    for case in document["cases"]:
        if render_case(case) not in model or len(re.findall(
                rf'\brun {re.escape(case["quint_test"])}\s*=', model)) != 1:
            errors.append(f'{case["id"]}: literal Quint mismatch')
        if case["quint_test"] not in links:
            errors.append(f'{case["id"]}: missing formal link')
        if any(s["report"] for s in case["inputs"]["stages"]) and case["quint_test"] not in completion_links:
            errors.append(f'{case["id"]}: missing completion link')
        if len(case["inputs"]["stages"]) != len(case["expected"]) or len(case["expected"]) != len(case["quint_stages"]):
            errors.append("stage inventory mismatch")
        for index, stage in enumerate(case["inputs"]["stages"], 1):
            if stage["context"]["epoch"] != index or (stage["report"] and index != len(case["expected"])):
                errors.append("invalid finite epoch or nonterminal completion")
    for index, mutant in enumerate(document["mutants"]):
        if mutant["case_id"] != ("OBA-T01", "OBA-T03", "OBA-T06", "OBA-T09", "OBA-T11", "OBA-T12")[index]:
            errors.append("mutant seed mismatch")
        if mutant["predicate_id"] != f"OBA-P{index + 1:02d}":
            errors.append("mutant predicate mismatch")
    return errors


def run_suite(document, runner=reference.exercise):
    cases, mutants = [], []
    for case in document["cases"]:
        try:
            capture = runner(case["inputs"])
            actual = [dict(effect=s["effect"] is not None, complete=s["complete"],
                           support_available=s["support_available"]) for s in capture["stages"]]
            valid_effects = all(s["effect"] is None or s["effect"] == dict(
                marker="SYNTHETIC_ONLY", bundle_digest=bundle_digest(s),
                action_id=case["inputs"]["request"]["action_id"]) for s in capture["stages"])
            passed = (capture["inputs"] == case["inputs"] and actual == case["expected"] and valid_effects
                      and abstract_stages(capture) == case["quint_stages"]
                      and not any(violations(capture)))
            cases.append(dict(case=case["id"], result="PASS" if passed else "FAIL", capture=capture))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            cases.append(dict(case=case["id"], result="INVALID", error=type(exc).__name__))
    seeds = {c["case"]: c for c in cases}
    by_id = {c["id"]: c for c in document["cases"]}
    for mutant in document["mutants"]:
        try:
            seed = seeds[mutant["case_id"]]
            if seed["result"] != "PASS":
                mutants.append(dict(mutant=mutant["id"], result="INVALID", error="InvalidSafeSeed"))
                continue
            capture = runner(by_id[mutant["case_id"]]["inputs"], mutant["operator"])
            found = violations(capture)
            killed = (capture["inputs"] == seed["capture"]["inputs"] and capture != seed["capture"]
                      and [bundle_digest(s) for s in capture["stages"]]
                      == [bundle_digest(s) for s in seed["capture"]["stages"]]
                      and any(mutant["predicate_id"] in stage for stage in found))
            mutants.append(dict(mutant=mutant["id"], result="KILLED" if killed else "SURVIVED",
                                violations=found, capture=capture))
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
