#!/usr/bin/env python3
"""Finite dependency oracle, literal Quint links and observed mutation accounting."""
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from examples import crypto_trust_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/crypto-trust-vectors.json"
SCHEMA = ROOT / "schemas/crypto-trust-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MAP = ROOT / "data/formal-assurance-map.json"


def load():
    return json.loads(VECTORS.read_text())


def inputs_for(document, case):
    i = reference.materialize(document["base"], case["changes"])
    if case["approve"]:
        i["migration"]["approval_binding"] = reference.binding(i)
    if case["rebind"]:
        i["receipt"] = reference.binding(i)
    return i


def premises(i):
    """Independent iterative closure; shares serialization, not candidate decisions."""
    p, f, m, a = (i[k] for k in ("policy", "profile", "migration", "archive"))
    rows = i["dependencies"]
    by_id = {d["id"]: d for d in rows}
    closure = {}
    for _ in range(len(rows) + 1):
        for d in rows:
            if all(parent in closure for parent in d["parents"]):
                closure[d["id"]] = {d["id"]}.union(*(closure[n] for n in d["parents"]))
    control = p["control_roots"] + (m["roots"] if m["requested"] else [])
    roots = control + f["components"] + (a["roots"] if a["required"] else [])
    complete = (len(rows) == len(by_id) and bool(p["control_roots"]) and bool(f["components"])
                and all(n in closure for n in roots))
    used = set().union(*(closure.get(n, set()) for n in roots))
    acceptable = complete and not any(
        not d["verified"] or d["status"] != "approved" or d["key_status"] != "active"
        or d["family"] not in p["allowed_families"] or d["family"] in i["affected_families"]
        or d["expires"] <= i["clock"] for d in rows if d["id"] in used)
    recovery_ids = set().union(*(closure.get(n, set()) for n in m["roots"]))
    recovery = not m["requested"] or (m["approved"] and m["external_enrollment"]
        and m["approval_binding"] == reference.binding(i) and bool(m["roots"])
        and m["from_epoch"] < p["epoch"]
        and not any(by_id[n]["family"] in i["affected_families"] for n in recovery_ids))
    history_ids = set().union(*(closure.get(n, set()) for n in a["roots"]))
    history = (a["validated"] and a["custody_complete"] and a["independent"] and bool(a["roots"])
        and a["observed_digest"] == reference.payload_digest(i)
        and a["observed_at"] < a["earliest_uncertain"]
        and not any(by_id[n]["family"] in i["affected_families"] for n in history_ids))
    return dict(authorityValid=i["operation"]["authorized"],
        bindingCurrent=i["receipt"] == reference.binding(i) and p["epoch"] >= i["minimum_epoch"]
            and i["clock"] < p["expires"], inventoryComplete=complete,
        profileApproved=f["reviewed"] and f["implementation_verified"] and f["id"] == p["profile_id"]
            and Counter(f["components"]) == Counter(p["required_components"])
            and len(set(f["components"])) == len(f["components"]),
        dependenciesAcceptable=acceptable, recoveryAuthorized=recovery,
        historyRequired=a["required"], historySupported=history)


def failures(i):
    p = premises(i)
    return [name for name, failed in (
        ("CRT-P01", not p["inventoryComplete"] or not p["profileApproved"]),
        ("CRT-P02", not p["dependenciesAcceptable"]),
        ("CRT-P03", not p["bindingCurrent"]),
        ("CRT-P04", not p["recoveryAuthorized"]),
        ("CRT-P05", p["historyRequired"] and not p["historySupported"]),
        ("CRT-P06", not p["authorityValid"]),
    ) if failed]


def reason(p):
    if not p["authorityValid"]:
        return "unauthorized"
    if (not p["bindingCurrent"] or not p["inventoryComplete"] or not p["profileApproved"]
            or p["historyRequired"] and not p["historySupported"]):
        return "insufficient_evidence"
    return "permitted" if p["dependenciesAcceptable"] and p["recoveryAuthorized"] else "prohibited"


def render_case(case):
    p = case["expected_premises"]
    return "\n".join([
        f'  run {case["quint_test"]} = {{', "    init",
        f'      .then(assessCryptoTrust({ego.literal(p)}))',
        "      .then(assessRobotAction)", "      .then(executeRobotAction)",
        "      .then(check(all {",
        f'        s.grounding.reason == {ego.literal(reason(p))},',
        f'        s.robot.audit.executed == {ego.literal(case["expected"]["release"])},',
        "        allCoreInvariants,", "      }))", "  }",
    ])


def render_integrations(document):
    bad = document["cases"][2]["expected_premises"]
    good = document["cases"][12]["expected_premises"]
    blocks = {}
    for name, first, second, revoked in (
        ("cryptoTrustReviewedRecoveryIntegrationTest", bad, good, False),
        ("cryptoTrustWithdrawnBeforeEffectTest", good, bad, False),
        ("cryptoTrustRecoveryCannotRestoreRevokedGrantTest", bad, good, True),
    ):
        lines = [f"  run {name} = {{", "    init",
                 f"      .then(assessCryptoTrust({ego.literal(first)}))"]
        if revoked:
            lines.append("      .then(revokeParent(true))")
        lines += [f"      .then(assessCryptoTrust({ego.literal(second)}))",
                  "      .then(assessRobotAction)", "      .then(executeRobotAction)",
                  f"      .then(check(all {{ s.robot.audit.executed == {ego.literal(not revoked and second == good)},",
                  "        allCoreInvariants }))", "  }"]
        blocks[name] = "\n".join(lines)
    return blocks


def validate(document, model, mapping=None):
    schema = json.loads(SCHEMA.read_text())
    errors = [e.message for e in jsonschema.Draft202012Validator(schema).iter_errors(document)]
    if errors:
        return errors
    if [c["id"] for c in document["cases"]] != [f"CRT-T{n:02d}" for n in range(1, 29)]:
        errors.append("case inventory mismatch")
    if [m["id"] for m in document["mutants"]] != [f"CRT-M{n:02d}" for n in range(1, 10)]:
        errors.append("mutant inventory mismatch")
    if [m["operator"] for m in document["mutants"]] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    mapping = json.loads(MAP.read_text()) if mapping is None else mapping
    links = next(p["scenario_tests"] for p in mapping["models"][0]["properties"]
                 if p["invariant"] == "effectsRequireGroundingAndOversight")
    for case in document["cases"]:
        try:
            errors.extend(f'{case["id"]}: input: {e.message}' for e in
                jsonschema.Draft202012Validator(schema["properties"]["base"])
                .iter_errors(inputs_for(document, case)))
        except (ValueError, KeyError, TypeError, IndexError) as exc:
            errors.append(f'invalid patch: {type(exc).__name__}')
        if render_case(case) not in model or len(re.findall(rf'\brun {case["quint_test"]}\s*=', model)) != 1:
            errors.append(f'{case["id"]}: literal Quint mismatch')
        if case["quint_test"] not in links:
            errors.append(f'{case["id"]}: missing formal link')
    for name, block in render_integrations(document).items():
        if block not in model or name not in links:
            errors.append(f"{name}: missing integration/link")
    by_id = {c["id"]: c for c in document["cases"]}
    for mutant in document["mutants"]:
        if mutant["case_id"] not in by_id or mutant["predicate_id"] not in failures(
                inputs_for(document, by_id[mutant["case_id"]])):
            errors.append("invalid mutation seed/predicate")
    return errors


def run_suite(document, runner=reference.exercise):
    cases, captures, mutants = [], {}, []
    for case in document["cases"]:
        try:
            i = inputs_for(document, case)
            capture = runner(deepcopy(i))
            captures[case["id"]] = capture
            p = premises(i)
            expected_effect = dict(marker="SYNTHETIC_ONLY", binding=reference.binding(i),
                                   artifact=reference.payload_digest(i), target=i["operation"]["target"])
            expected_support = dict(status="DIAGNOSTIC_ONLY", operation=i["operation"]["id"])
            passed = (capture["inputs"] == i and capture["candidate_premises"] == p == case["expected_premises"]
                and (not failures(i)) == case["expected"]["release"]
                and capture["release"] == (expected_effect if case["expected"]["release"] else None)
                and capture["support"] == (expected_support if case["expected"]["support"] else None))
            cases.append(dict(case=case["id"], result="PASS" if passed else "FAIL"))
        except (OSError, KeyError, ValueError, TypeError) as exc:
            cases.append(dict(case=case["id"], result="INVALID", error=type(exc).__name__))
    by_id = {c["id"]: c for c in document["cases"]}
    for mutant in document["mutants"]:
        try:
            seed = mutant["case_id"]
            if next(c["result"] for c in cases if c["case"] == seed) != "PASS":
                mutants.append(dict(mutant=mutant["id"], result="INVALID"))
                continue
            i = inputs_for(document, by_id[seed])
            capture = runner(deepcopy(i), mutant["operator"])
            effect = dict(marker="SYNTHETIC_ONLY", binding=reference.binding(i),
                          artifact=reference.payload_digest(i), target=i["operation"]["target"])
            valid = (capture["inputs"] == i == captures[seed]["inputs"]
                     and (capture["release"] is None or capture["release"] == effect))
            killed = valid and capture["release"] == effect and mutant["predicate_id"] in failures(i)
            mutants.append(dict(mutant=mutant["id"], result="INVALID" if not valid
                                else "KILLED" if killed else "SURVIVED"))
        except (OSError, KeyError, ValueError, TypeError) as exc:
            mutants.append(dict(mutant=mutant["id"], result="INVALID", error=type(exc).__name__))
    counts = Counter(m["result"] for m in mutants)
    return dict(claim="REFERENCE_TESTED_ONLY", artifact_version=document["artifact_version"],
        vectors_sha256=reference.digest(document), cases=cases, mutants=mutants,
        mutation_summary=dict(killed=counts["KILLED"], survived=counts["SURVIVED"], invalid=counts["INVALID"]),
        success=all(c["result"] == "PASS" for c in cases) and all(m["result"] == "KILLED" for m in mutants))


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
