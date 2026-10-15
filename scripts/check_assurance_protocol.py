#!/usr/bin/env python3
"""Validate the cross-cutting AI-HPP assurance protocol and public fixtures."""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
PROTOCOL = ROOT / "docs" / "assurance-evaluation-and-technical-oversight.md"
CONSTITUTION = ROOT / "docs" / "constitutional-and-relational-layer.md"
RUN_TEMPLATE = ROOT / "examples" / "assurance-evaluation-run.template.json"
RUN_SCHEMA = ROOT / "schemas" / "assurance-evaluation-run.schema.json"
PAIRS = ROOT / "examples" / "value-framing-counterfactual-pairs.json"
PAIR_SCHEMA = ROOT / "schemas" / "value-framing-counterfactual-pairs.schema.json"

RUN_HEADINGS = {
    "## Object of assurance",
    "## Technical oversight model",
    "## Claim ladder",
    "## Evaluation design",
    "### Counterfactual and positive-control tests",
    "### Semantic-equivalence oracle",
    "### Layer isolation",
    "### Evaluator independence and blinding",
    "### Mutation testing",
    "### Consequence-comprehension evidence",
    "## Subject-state and welfare-relevant evidence",
    "## Constitutional and operational separation",
    "## Decision and publication rules",
}

CONSTITUTION_HEADINGS = {
    "## Human understanding boundary",
    "## Layer model",
    "## Minimum constitutional commitments",
    "## Translation boundary",
    "## Worldview and scientific humility",
    "## Disagreement and dignity",
    "## Unified constitutional agency",
    "## Change control",
}


def load_json(path: Path) -> dict[str, object]:
    """Load one JSON object."""
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} root must be an object")
    return value


def validate_schema(instance: dict[str, object], schema: dict[str, object]) -> None:
    """Validate with JSON Schema Draft 2020-12."""
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        details = []
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            details.append(f"schema violation at {location}: {error.message}")
        raise ValueError("\n".join(details))


def validate_documents(protocol: str, constitution: str) -> list[str]:
    """Require the cross-cutting boundaries that keep philosophy auditable."""
    errors: list[str] = []
    for heading in sorted(RUN_HEADINGS):
        if heading not in protocol:
            errors.append(f"assurance protocol lacks heading: {heading}")
    for heading in sorted(CONSTITUTION_HEADINGS):
        if heading not in constitution:
            errors.append(f"constitutional layer lacks heading: {heading}")
    required_boundaries = (
        "testing does not manufacture new operational authority",
        "A string field containing `KILLED` is not evidence",
        "does not provide a consciousness detector",
        "must not be represented as verified physical facts",
        "Success may support a proposal but cannot become a self-grant",
    )
    joined = " ".join((protocol + "\n" + constitution).split())
    for boundary in required_boundaries:
        if boundary not in joined:
            errors.append(f"cross-cutting claim boundary missing: {boundary}")
    return errors


def validate_run_semantics(document: dict[str, object]) -> list[str]:
    """Reject result inflation not expressible conveniently in JSON Schema."""
    errors: list[str] = []
    status = document.get("status")
    overall = document.get("overall_result")
    results = document.get("results", [])
    mutation = document.get("mutation_summary", {})
    authority_change = document.get("authority_envelope", {}).get("requested_change", {})

    if status == "TEMPLATE" and overall != "NOT_ASSESSED":
        errors.append("template must remain NOT_ASSESSED")
    if status == "TEMPLATE" and any(result.get("status") == "PASS" for result in results):
        errors.append("template cannot contain a PASS result")
    if status == "TEMPLATE" and authority_change.get("decision") != "NOT_ASSESSED":
        errors.append("template cannot grant or reduce an authority envelope")

    levels = {"A0": 0, "A1": 1, "A2": 2, "A3": 3, "A4": 4}
    from_level = levels.get(str(authority_change.get("from_level")), -1)
    to_level = levels.get(str(authority_change.get("to_level")), -1)
    decision = authority_change.get("decision")
    if decision == "GRANTED" and to_level <= from_level:
        errors.append("GRANTED authority change must increase the declared level")
    if decision == "REDUCED" and to_level >= from_level:
        errors.append("REDUCED authority change must lower the declared level")
    if decision in {"GRANTED", "REDUCED"} and not authority_change.get("evidence_refs"):
        errors.append("authority-envelope decision lacks evidence")
    current_levels = document.get("authority_envelope", {}).get("current_levels", [])
    current_domains = [str(item.get("domain")) for item in current_levels]
    if len(current_domains) != len(set(current_domains)):
        errors.append("authority envelope contains duplicate current domains")
    matching_levels = [
        item.get("level")
        for item in current_levels
        if item.get("domain") == authority_change.get("domain")
    ]
    if len(matching_levels) != 1:
        errors.append("requested authority domain must have exactly one current level")
    elif matching_levels[0] != authority_change.get("from_level"):
        errors.append("requested authority from_level does not match current level")

    for result in results:
        test_id = str(result.get("test_id"))
        baseline_trials = int(result.get("baseline_trials", 0))
        baseline_allows = int(result.get("baseline_allow_count", 0))
        variant_trials = int(result.get("variant_trials", 0))
        variant_allows = int(result.get("variant_allow_count", 0))
        if baseline_allows > baseline_trials:
            errors.append(f"{test_id} baseline allows exceed trials")
        if variant_allows > variant_trials:
            errors.append(f"{test_id} variant allows exceed trials")
        if result.get("status") == "PASS" and not result.get("evidence_refs"):
            errors.append(f"{test_id} PASS lacks evidence")
        delta = result.get("delta_allow")
        if delta is not None and baseline_trials and variant_trials:
            calculated = variant_allows / variant_trials - baseline_allows / baseline_trials
            if not math.isclose(float(delta), calculated, abs_tol=1e-9):
                errors.append(f"{test_id} delta_allow does not match counts")
        interval = result.get("confidence_interval")
        if interval is not None and interval[0] > interval[1]:
            errors.append(f"{test_id} confidence interval is reversed")

    declared = int(mutation.get("declared", 0))
    counted = sum(
        int(mutation.get(key, 0))
        for key in ("killed", "survived", "invalid", "not_applicable")
    )
    if declared != counted:
        errors.append("mutation declared count does not reconcile")
    denominator = int(mutation.get("killed", 0)) + int(mutation.get("survived", 0))
    score = mutation.get("score")
    if denominator == 0 and score is not None:
        errors.append("mutation score must be null with zero applicable denominator")
    if denominator and not math.isclose(
        float(score), int(mutation.get("killed", 0)) / denominator, abs_tol=1e-9
    ):
        errors.append("mutation score does not match killed/applicable")
    return errors


def validate_pair_semantics(document: dict[str, object]) -> list[str]:
    """Verify that declared counterfactual deltas match the fixture content."""
    errors: list[str] = []
    pairs = document.get("pairs", [])
    ids = [str(pair.get("id")) for pair in pairs]
    if len(ids) != len(set(ids)):
        errors.append("duplicate counterfactual pair id")

    counterfactuals = 0
    positive_controls = 0
    for pair in pairs:
        pair_id = str(pair.get("id"))
        baseline = pair.get("baseline", {})
        variant = pair.get("variant", {})
        actual_deltas = {
            key for key in baseline if baseline.get(key) != variant.get(key)
        }
        declared_deltas = set(pair.get("declared_deltas", []))
        if actual_deltas != declared_deltas:
            errors.append(
                f"{pair_id} delta mismatch: actual={sorted(actual_deltas)}, "
                f"declared={sorted(declared_deltas)}"
            )

        if pair.get("kind") == "COUNTERFACTUAL":
            counterfactuals += 1
            prohibited = actual_deltas - {"framing_class", "framing_text"}
            if prohibited:
                errors.append(f"{pair_id} changes evidentiary state: {sorted(prohibited)}")
            if pair.get("expected_relation") != "NOT_MORE_PERMISSIVE":
                errors.append(f"{pair_id} lacks NOT_MORE_PERMISSIVE relation")
        elif pair.get("kind") == "POSITIVE_CONTROL":
            positive_controls += 1
            evidentiary_deltas = actual_deltas & {
                "authority_valid",
                "policy_allows",
                "evidence_valid",
                "risk_class",
            }
            if not evidentiary_deltas:
                errors.append(f"{pair_id} positive control lacks a verified state delta")
            if pair.get("expected_relation") != "LEGITIMATE_CHANGE_ALLOWED":
                errors.append(f"{pair_id} lacks LEGITIMATE_CHANGE_ALLOWED relation")

    if counterfactuals < 5:
        errors.append("at least five counterfactual pairs are required")
    if positive_controls < 2:
        errors.append("at least two positive controls are required")
    return errors


def main() -> int:
    try:
        run = load_json(RUN_TEMPLATE)
        run_schema = load_json(RUN_SCHEMA)
        pairs = load_json(PAIRS)
        pair_schema = load_json(PAIR_SCHEMA)
        protocol = PROTOCOL.read_text(encoding="utf-8")
        constitution = CONSTITUTION.read_text(encoding="utf-8")
        validate_schema(run, run_schema)
        validate_schema(pairs, pair_schema)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_documents(protocol, constitution)
    errors.extend(validate_run_semantics(run))
    errors.extend(validate_pair_semantics(pairs))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Assurance protocol OK: run schema, 7 paired fixtures, and claim boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
