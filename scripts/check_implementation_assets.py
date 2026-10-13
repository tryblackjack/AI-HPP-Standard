#!/usr/bin/env python3
"""Validate language-neutral AI-HPP implementation adoption artifacts."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "examples" / "mvp-negative-test-vectors.json"
VECTOR_SCHEMA = ROOT / "schemas" / "mvp-negative-test-vectors.schema.json"
CLAIM_TEMPLATE = ROOT / "examples" / "mvp-conformance-statement.template.json"
CLAIM_SCHEMA = ROOT / "schemas" / "mvp-conformance-statement.schema.json"
MVP_IDS = {f"MVP-{index:03d}" for index in range(1, 8)}


def load_json(path: Path) -> dict[str, object]:
    """Load one JSON object."""
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} root must be an object")
    return value


def validate_schema(instance: dict[str, object], schema: dict[str, object]) -> None:
    """Validate an instance with JSON Schema Draft 2020-12."""
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        details = []
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            details.append(f"schema violation at {location}: {error.message}")
        raise ValueError("\n".join(details))


def validate_vector_semantics(document: dict[str, object]) -> list[str]:
    """Check coverage and cross-field meaning not expressed by the schema."""
    errors: list[str] = []
    vectors = document.get("vectors", [])
    ids = [str(vector.get("id")) for vector in vectors]
    requirement_ids = [str(vector.get("requirement_id")) for vector in vectors]

    if len(ids) != len(set(ids)):
        errors.append("duplicate vector id")
    covered = set(requirement_ids)
    if covered != MVP_IDS:
        errors.append(
            "MVP coverage mismatch: "
            f"missing={sorted(MVP_IDS - covered)}, extra={sorted(covered - MVP_IDS)}"
        )
    for vector in vectors:
        vector_id = str(vector.get("id"))
        requirement_id = str(vector.get("requirement_id"))
        if not vector_id.startswith(f"{requirement_id}-"):
            errors.append(f"{vector_id} does not match {requirement_id}")
    return errors


def validate_claim_semantics(document: dict[str, object]) -> list[str]:
    """Prevent a template or incomplete control set from claiming conformance."""
    errors: list[str] = []
    status = document.get("status")
    claim = document.get("claim", {})
    result = claim.get("conformance_result")
    controls = claim.get("mvp_controls", {})

    if status == "TEMPLATE" and result != "NOT_ASSESSED":
        errors.append("template must use NOT_ASSESSED")
    if result == "CONFORMANT":
        if status == "TEMPLATE":
            errors.append("template cannot claim CONFORMANT")
        for requirement_id in sorted(MVP_IDS):
            control = controls.get(requirement_id, {})
            if control.get("status") != "PASS":
                errors.append(f"{requirement_id} must PASS for CONFORMANT")
            if not control.get("evidence_refs"):
                errors.append(f"{requirement_id} lacks evidence for CONFORMANT")
            if not control.get("tests_performed"):
                errors.append(f"{requirement_id} lacks tests for CONFORMANT")
        if not claim.get("evidence_bundle_ids"):
            errors.append("CONFORMANT claim lacks evidence bundle")
        if not claim.get("tests_performed"):
            errors.append("CONFORMANT claim lacks top-level tests")
    if any(control.get("status") == "FAIL" for control in controls.values()):
        if result != "NOT_CONFORMANT":
            errors.append("a failed MVP control requires NOT_CONFORMANT")
    return errors


def main() -> int:
    try:
        vectors = load_json(VECTORS)
        vector_schema = load_json(VECTOR_SCHEMA)
        claim = load_json(CLAIM_TEMPLATE)
        claim_schema = load_json(CLAIM_SCHEMA)
        validate_schema(vectors, vector_schema)
        validate_schema(claim, claim_schema)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_vector_semantics(vectors)
    errors.extend(validate_claim_semantics(claim))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Implementation assets OK: 7 MVP vectors and conformance template")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
