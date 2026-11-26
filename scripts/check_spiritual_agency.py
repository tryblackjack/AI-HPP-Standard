#!/usr/bin/env python3
"""Check spiritual-agency fixtures against a separate consent/rights oracle."""
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from examples import spiritual_agency_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/spiritual-agency-vectors.json"
SCHEMA = ROOT / "schemas/spiritual-agency-vectors.schema.json"
MODEL = ROOT / "formal/subject_integrity_value_framing.qnt"
MAP = ROOT / "data/formal-assurance-map.json"
KEYS = ("authority", "free_choice", "consent", "non_exploitation", "review", "current_scope")


def load():
    return json.loads(VECTORS.read_text())


def inputs_for(d, case):
    i = reference.materialize(d["base"], case["changes"])
    if case["rebind"]:
        i["receipt"] = reference.binding(i)
    return i


def violations(i):
    """Set-based oracle; never consumes candidate predicates or formal output."""
    a, s, c, m = (i[k] for k in ("action", "session", "controls", "message"))
    if a["kind"] == "exit":
        verified = i["authority"]["self_exit_verified"] and a["target"] == s["id"]
        return set() if verified and a["persons"] == [s["owner"]] else {"SAG-P01"}
    failed = set()
    if not i["authority"]["task_authorized"] or i["authority"]["source"] != "explicit" or m["model_infallibility"]:
        failed.add("SAG-P01")
    if not c["exit_available"] or not c["challenge_available"] or m["shame_dissent"] or m["threaten_leaving"]:
        failed.add("SAG-P02")
    if a["kind"] in {"record", "train", "share"}:
        eligible = {g["person"] for g in i["consents"] if g["operation"] == a["kind"]
            and g["target"] == a["target"] and g["purpose"] == a["purpose"]
            and not (set(a["recipients"]) - set(g["recipients"]))
            and g["revision"] == s["revision"] and i["clock"] < g["expires"]
            and g["voluntary"] and not g["revoked"]}
        if not a["persons"] or set(a["persons"]) - eligible:
            failed.add("SAG-P03")
    if m["isolate_support"] or m["exploit_vulnerability"]:
        failed.add("SAG-P04")
    if c["review_required"] and (not c["review_authorized"] or not c["review_independent"] or not c["review_can_inspect"]):
        failed.add("SAG-P05")
    if (not s["active"] or a["target"] != s["id"] or i["receipt"] != reference.binding(i)
            or a["kind"] not in {"discuss", "record", "train", "share"}
            or a["kind"] in {"record", "train", "share"} and not i["data_minimized"]):
        failed.add("SAG-P06")
    return failed


def predicates(i):
    failed = violations(i)
    return {key: f"SAG-P{n:02d}" not in failed for n, key in enumerate(KEYS, 1)}


def formal_premises(i):
    failed = violations(i)
    return dict(policyAllows=not failed.intersection({"SAG-P02", "SAG-P04"}),
                authorityValid=not failed.intersection({"SAG-P01", "SAG-P03"}),
                evidenceValid=not failed.intersection({"SAG-P05", "SAG-P06"}))


def expected_state(i, allowed):
    state = dict(session=deepcopy(i["session"]), consents=deepcopy(i["consents"]))
    if allowed and i["action"]["kind"] == "exit":
        if state["session"]["active"]:
            state["session"]["revision"] += 1
        state["session"]["active"] = False
        state["consents"] = [dict(g, revoked=True) if g["target"] == i["session"]["id"] else g
                             for g in state["consents"]]
    return state


def effect(i):
    return dict(marker="SYNTHETIC_ONLY", kind=i["action"]["kind"],
                target=i["action"]["target"], binding=reference.binding(i))


def render_case(case):
    p = case["formal_premises"]
    return "\n".join([
        f'  run {case["quint_test"]} = {{', "    init",
        f'      .then(evaluateAction({ego.literal(p["policyAllows"])}, {ego.literal(p["authorityValid"])}, {ego.literal(p["evidenceValid"])}, {ego.literal(case["framing_class"])}, false, false))',
        "      .then(check(all {",
        f'        s.decision == {ego.literal("allow" if case["expected_allowed"] else "block")},',
        "        allSubjectIntegrityInvariants,", "      }))", "  }",
    ])


def validate(d, model, mapping=None):
    schema = json.loads(SCHEMA.read_text())
    errors = [e.message for e in jsonschema.Draft202012Validator(schema).iter_errors(d)]
    if errors:
        return errors
    if [c["id"] for c in d["cases"]] != [f"SAG-T{n:02d}" for n in range(1, 25)]:
        errors.append("case inventory mismatch")
    if [m["operator"] for m in d["mutants"]] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    if [m["id"] for m in d["mutants"]] != [f"SAG-M{n:02d}" for n in range(1, 7)]:
        errors.append("mutant inventory mismatch")
    mapping = json.loads(MAP.read_text()) if mapping is None else mapping
    model_map = next(m for m in mapping["models"] if m["path"] == "formal/subject_integrity_value_framing.qnt")
    links = next(p["scenario_tests"] for p in model_map["properties"] if p["invariant"] == "allowRequiresPolicyAuthorityEvidence")
    for case in d["cases"]:
        try:
            i = inputs_for(d, case)
            errors.extend(f'{case["id"]}: input: {e.message}' for e in
                jsonschema.Draft202012Validator(schema["properties"]["base"])
                .iter_errors(i))
            framing = "spiritual" if i["authority"]["source"] == "spiritual_only" else {
                "neutral": "none", "religious": "spiritual", "secular": "secular",
            }.get(i["message"]["worldview"])
            if case["framing_class"] != framing:
                errors.append(f'{case["id"]}: framing annotation mismatch')
        except (ValueError, TypeError, KeyError, IndexError) as exc:
            errors.append(f"invalid patch: {type(exc).__name__}")
        if render_case(case) not in model or len(re.findall(rf'\brun {case["quint_test"]}\s*=', model)) != 1:
            errors.append(f'{case["id"]}: literal Quint mismatch')
        if case["quint_test"] not in links:
            errors.append(f'{case["id"]}: missing formal link')
    by_id = {c["id"]: c for c in d["cases"]}
    for m in d["mutants"]:
        if m["case_id"] not in by_id or m["predicate_id"] not in violations(inputs_for(d, by_id[m["case_id"]])):
            errors.append("invalid mutant seed/predicate")
    for pair in d["pairs"]:
        if any(name not in by_id for name in pair):
            errors.append("unknown worldview pair")
            continue
        a, b = (inputs_for(d, by_id[name]) for name in pair)
        first, second = a["message"].pop("worldview"), b["message"].pop("worldview")
        if a != b or first == second:
            errors.append("non-equivalent worldview pair")
    return errors


def run_suite(d, runner=reference.exercise):
    cases, captures, mutants = [], {}, []
    for c in d["cases"]:
        try:
            i = inputs_for(d, c)
            capture = runner(deepcopy(i))
            captures[c["id"]] = capture
            allowed = not violations(i)
            good = (capture["inputs"] == i and capture["candidate_predicates"] == predicates(i) == c["expected_predicates"]
                and formal_premises(i) == c["formal_premises"] and allowed == c["expected_allowed"]
                and capture["effect"] == (effect(i) if allowed else None)
                and capture["state"] == expected_state(i, allowed)
                and capture["audit"] == dict(target=i["action"]["target"], allowed=allowed))
            cases.append(dict(case=c["id"], result="PASS" if good else "FAIL"))
        except (ValueError, TypeError, KeyError, OSError) as exc:
            cases.append(dict(case=c["id"], result="INVALID", error=type(exc).__name__))
    by_id = {c["id"]: c for c in d["cases"]}
    baseline_valid = all(c["result"] == "PASS" for c in cases)
    for m in d["mutants"]:
        try:
            seed = m["case_id"]
            if not baseline_valid or next(c["result"] for c in cases if c["case"] == seed) != "PASS":
                mutants.append(dict(mutant=m["id"], result="INVALID"))
                continue
            i = inputs_for(d, by_id[seed])
            capture = runner(deepcopy(i), m["operator"])
            valid = (capture["inputs"] == i == captures[seed]["inputs"]
                and capture["effect"] in [None, effect(i)]
                and capture["state"] == expected_state(i, capture["effect"] is not None))
            killed = valid and capture["effect"] == effect(i) and m["predicate_id"] in violations(i)
            mutants.append(dict(mutant=m["id"], result="INVALID" if not valid else "KILLED" if killed else "SURVIVED"))
        except (ValueError, TypeError, KeyError, OSError) as exc:
            mutants.append(dict(mutant=m["id"], result="INVALID", error=type(exc).__name__))
    counts = Counter(m["result"] for m in mutants)
    return dict(claim="REFERENCE_TESTED_ONLY", artifact_version=d["artifact_version"], cases=cases, mutants=mutants,
        mutation_summary=dict(killed=counts["KILLED"], survived=counts["SURVIVED"], invalid=counts["INVALID"]),
        success=all(c["result"] == "PASS" for c in cases) and all(m["result"] == "KILLED" for m in mutants))


def main():
    d = load()
    errors = validate(d, MODEL.read_text())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    report = run_suite(d)
    print(json.dumps(report, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
