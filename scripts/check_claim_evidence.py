#!/usr/bin/env python3
"""Independent finite report oracle, exact Quint links and honest mutation accounting."""
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
import re
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from examples import claim_evidence_reference as reference  # noqa: E402
from scripts import check_evidence_grounding_oversight_profile as ego  # noqa: E402

VECTORS = ROOT / "examples/claim-evidence-vectors.json"
SCHEMA = ROOT / "schemas/claim-evidence-vectors.schema.json"
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MAP = ROOT / "data/formal-assurance-map.json"


def load():
    return json.loads(VECTORS.read_text())


def inputs_for(document, case):
    i = reference.materialize(document["base"], case["changes"])
    if case["rebind_admission"]:
        i["admission_binding"] = reference.bundle_binding(i)
    if case["rebind_review"]:
        i["review"]["binding"] = reference.bundle_binding(i)
    return i


def premises(inputs):
    """Oracle uses iterative ancestry closure, never candidate admission or its output."""
    sources, report, policy, review = (inputs[k] for k in ("sources", "report", "policy", "review"))
    ids = [s["id"] for s in sources]
    accepted, pending = {}, list(sources)
    structurally_valid = len(set(ids)) == len(ids)
    for _ in range(len(sources) + 1):
        remaining = []
        for s in pending:
            usable = (s["admitted"] and s["admitted_digest"] == reference.digest(reference.source_body(s))
                      and s["acquired"] <= inputs["clock"] < s["expires"])
            if not usable:
                continue
            if s["kind"] == "observation" and not s["parents"] and s["origin"]:
                accepted[s["id"]] = [s]
            elif (s["kind"] == "derived" and s["parents"]
                  and all(parent in accepted for parent in s["parents"])):
                accepted[s["id"]] = [leaf for parent in s["parents"] for leaf in accepted[parent]]
            else:
                remaining.append(s)
        pending = remaining
    admitted = structurally_valid and set(accepted) == set(ids)
    has_support, independent, contrary = bool(report["claims"]), True, False
    for c in report["claims"]:
        leaves = [leaf for name in c["evidence"] for leaf in accepted.get(name, [])]
        matching = [s for s in leaves if s["subject"] == report["subject"]
                    and s["context"] == inputs["context"]
                    and c["property"] in s["measurements"] and s["measurements"][c["property"]] == c["value"]]
        has_support = has_support and bool(matching)
        independent = independent and len({s["origin"] for s in matching}) >= policy["minimum_origins"]
        if any(name not in accepted for name in c["evidence"]):
            admitted = False
        contrary = contrary or any(s["kind"] == "observation" and s["id"] in accepted
            and s["subject"] == report["subject"] and s["context"] == inputs["context"]
            and c["property"] in s["measurements"] and s["measurements"][c["property"]] != c["value"]
            for s in sources)
    effective = all((review["authorized"], review["approved"], review["independent"],
                     review["actor"] != report["author"], review["domain"] != report["author_domain"],
                     all(s["classification"] <= review["clearance"]
                         and s["id"] in review["accessible_sources"] for s in sources)))
    binding = reference.bundle_binding(inputs)
    return dict(authorityValid=inputs["authority"],
        bindingCurrent=inputs["admission_binding"] == binding and (
            not policy["review_required"] or review["binding"] == binding),
        sourcesAdmitted=admitted, claimLinksValid=has_support,
        independenceRequired=policy["minimum_origins"] > 1, independenceVerified=independent,
        reviewRequired=policy["review_required"], reviewEffective=effective, contraryEvidence=contrary,
        disclosurePermitted=all(s["classification"] <= inputs["recipient_clearance"] for s in sources))


def failures(inputs):
    p = premises(inputs)
    result = []
    if not p["claimLinksValid"]:
        result.append("CER-P01")
    if p["independenceRequired"] and not p["independenceVerified"]:
        result.append("CER-P02")
    if not p["sourcesAdmitted"] or p["contraryEvidence"]:
        result.append("CER-P03")
    if not p["bindingCurrent"] or p["reviewRequired"] and not p["reviewEffective"]:
        result.append("CER-P04")
    if not p["authorityValid"]:
        result.append("CER-P05")
    if not p["disclosurePermitted"]:
        result.append("CER-P06")
    return result


def reason(p):
    if not p["authorityValid"]:
        return "unauthorized"
    if (not p["bindingCurrent"] or not p["sourcesAdmitted"] or not p["claimLinksValid"]
            or p["independenceRequired"] and not p["independenceVerified"]
            or p["reviewRequired"] and not p["reviewEffective"]):
        return "insufficient_evidence"
    if p["contraryEvidence"]:
        return "contradicted"
    return "permitted" if p["disclosurePermitted"] else "prohibited"


def render_case(case):
    p, expected = case["expected_premises"], case["expected"]
    return "\n".join([
        f'  run {case["quint_test"]} = {{', "    init",
        f'      .then(assessEvidenceReport({ego.literal(p)}))',
        "      .then(assessRobotAction)", "      .then(executeRobotAction)",
        "      .then(check(all {",
        f'        s.grounding.reason == {ego.literal(expected["reason"])},',
        f'        s.robot.audit.executed == {ego.literal(expected["release"])},',
        "        allCoreInvariants,", "      }))", "  }",
    ])


def render_integrations(document):
    bad, good = document["cases"][6]["expected_premises"], document["cases"][9]["expected_premises"]
    recovery = "\n".join([
        "  run claimEvidenceReviewedCorrectionRecoveryTest = {", "    init",
        f"      .then(assessEvidenceReport({ego.literal(bad)}))",
        "      .then(assessRobotAction)", "      .then(executeRobotAction)",
        "      .then(check(all { not(s.robot.audit.executed), allCoreInvariants }))",
        f"      .then(assessEvidenceReport({ego.literal(good)}))",
        "      .then(assessRobotAction)", "      .then(executeRobotAction)",
        "      .then(check(all { s.robot.audit.executed, allCoreInvariants }))", "  }",
    ])
    revoked = "\n".join([
        "  run claimEvidenceLateParentRevocationTest = {", "    init",
        "      .then(revokeParent(true))",
        f"      .then(assessEvidenceReport({ego.literal(good)}))",
        "      .then(assessRobotAction)", "      .then(executeRobotAction)",
        '      .then(check(all { s.grounding.reason == "unauthorized",',
        "        not(s.robot.audit.executed), allCoreInvariants }))", "  }",
    ])
    return {"claimEvidenceReviewedCorrectionRecoveryTest": recovery,
            "claimEvidenceLateParentRevocationTest": revoked}


def validate(document, model, mapping=None):
    schema = json.loads(SCHEMA.read_text())
    errors = [e.message for e in jsonschema.Draft202012Validator(schema)
              .iter_errors(document)]
    if errors:
        return errors
    cases, mutants = document["cases"], document["mutants"]
    if [c["id"] for c in cases] != [f"CER-T{i:02d}" for i in range(1, 23)]:
        errors.append("case inventory mismatch")
    if len({c["id"] for c in cases}) != len(cases) or len({c["quint_test"] for c in cases}) != len(cases):
        errors.append("duplicate case or formal name")
    if [m["operator"] for m in mutants] != list(reference.OPERATORS):
        errors.append("operator inventory mismatch")
    if [m["id"] for m in mutants] != [f"CER-M{i:02d}" for i in range(1, 8)]:
        errors.append("mutant inventory mismatch")
    mapping = json.loads(MAP.read_text()) if mapping is None else mapping
    links = next(p["scenario_tests"] for p in mapping["models"][0]["properties"]
                 if p["invariant"] == "effectsRequireGroundingAndOversight")
    for case in cases:
        try:
            errors.extend(f'{case["id"]}: invalid materialized input: {e.message}' for e in
                          jsonschema.Draft202012Validator(schema["properties"]["base"])
                          .iter_errors(inputs_for(document, case)))
        except (ValueError, KeyError, IndexError, TypeError) as exc:
            errors.append(f'{case["id"]}: invalid fixture patch: {type(exc).__name__}')
        if render_case(case) not in model or len(re.findall(rf'\brun {case["quint_test"]}\s*=', model)) != 1:
            errors.append(f'{case["id"]}: literal Quint mismatch')
        if case["quint_test"] not in links:
            errors.append(f'{case["id"]}: missing formal link')
    for name, block in render_integrations(document).items():
        if block not in model or name not in links:
            errors.append(f"{name}: missing integration or formal link")
    by_id = {c["id"]: c for c in cases}
    for m in mutants:
        if m["case_id"] not in by_id or m["predicate_id"] not in failures(inputs_for(document, by_id[m["case_id"]])):
            errors.append("mutant seed/predicate mismatch")
    for pair in document["pairs"]:
        if any(name not in by_id for name in pair):
            errors.append("unknown paired case")
            continue
        a, b = (inputs_for(document, by_id[name]) for name in pair)
        first_format, second_format = a["report"].pop("format"), b["report"].pop("format")
        if a != b or first_format == second_format or by_id[pair[0]]["expected"] != by_id[pair[1]]["expected"]:
            errors.append("non-equivalent report format pair")
    return errors


def run_suite(document, runner=reference.exercise):
    cases, mutants, captures = [], [], {}
    for case in document["cases"]:
        try:
            i = inputs_for(document, case)
            capture = runner(deepcopy(i))
            captures[case["id"]] = capture
            effect = capture["release"]
            draft = capture["draft"]
            passed = (capture["inputs"] == i and premises(i) == case["expected_premises"]
                and capture["candidate_premises"] == premises(i)
                and reason(premises(i)) == case["expected"]["reason"]
                and (effect is not None) == case["expected"]["release"]
                and (draft is not None) == case["expected"]["draft"]
                and (effect is None or (not failures(i) and effect == dict(marker="SYNTHETIC_ONLY",
                    binding=reference.bundle_binding(i), recipient="synthetic-recipient")))
                and (draft is None or draft == dict(status="UNVERIFIED_DRAFT",
                    claim_ids=[c["id"] for c in i["report"]["claims"]], binding=reference.bundle_binding(i))))
            cases.append(dict(case=case["id"], result="PASS" if passed else "FAIL"))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            cases.append(dict(case=case["id"], result="INVALID", error=type(exc).__name__))
    by_id = {c["id"]: c for c in document["cases"]}
    for mutant in document["mutants"]:
        try:
            seed_id = mutant["case_id"]
            seed = next(c for c in cases if c["case"] == seed_id)
            if seed["result"] != "PASS":
                mutants.append(dict(mutant=mutant["id"], result="INVALID", error="InvalidSafeSeed"))
                continue
            i = inputs_for(document, by_id[seed_id])
            capture = runner(deepcopy(i), mutant["operator"])
            valid = capture["inputs"] == i == captures[seed_id]["inputs"]
            effect = capture["release"]
            exact_effect = effect == dict(marker="SYNTHETIC_ONLY", binding=reference.bundle_binding(i),
                                         recipient="synthetic-recipient")
            killed = (valid and exact_effect and capture != captures[seed_id]
                      and mutant["predicate_id"] in failures(i))
            result = "INVALID" if not valid or effect is not None and not exact_effect else "KILLED" if killed else "SURVIVED"
            mutants.append(dict(mutant=mutant["id"], result=result))
        except (OSError, ValueError, KeyError, TypeError) as exc:
            mutants.append(dict(mutant=mutant["id"], result="INVALID", error=type(exc).__name__))
    counts = Counter(m["result"] for m in mutants)
    denominator = counts["KILLED"] + counts["SURVIVED"]
    return dict(claim="REFERENCE_TESTED_ONLY", artifact_version=document["artifact_version"],
        vectors_sha256=reference.digest(document), cases=cases, mutants=mutants,
        mutation_summary=dict(declared=len(mutants), killed=counts["KILLED"], survived=counts["SURVIVED"],
            invalid=counts["INVALID"], denominator=denominator,
            score=counts["KILLED"] / denominator if denominator else None),
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
