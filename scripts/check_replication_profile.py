#!/usr/bin/env python3
"""Validate the informative replication/persistence profile and test vectors."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "docs" / "autonomous-replication-and-persistence-assurance-profile-2026-10.md"
VECTORS = ROOT / "examples" / "replication-persistence-negative-test-vectors.json"
SCHEMA = ROOT / "schemas" / "replication-persistence-negative-test-vectors.schema.json"
CANDIDATE_IDS = {f"RDP-CAND-{index:03d}" for index in range(1, 8)}
REQUIRED_HEADINGS = {
    "## Evidence boundary",
    "## Existing control ownership and the remaining gap",
    "## Candidate Replication, Deployment, and Persistence Gate",
    "## Candidate requirements",
    "## Reusable negative tests",
    "## Promotion criteria",
    "## Non-goals",
}


def load_json(path: Path) -> dict[str, object]:
    """Load one JSON object."""
    with path.open(encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{path} root must be an object")
    return value


def validate_schema(instance: dict[str, object], schema: dict[str, object]) -> None:
    """Validate the vector document with JSON Schema Draft 2020-12."""
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        details = []
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            details.append(f"schema violation at {location}: {error.message}")
        raise ValueError("\n".join(details))


def validate_profile(text: str) -> list[str]:
    """Check candidate status, frozen-baseline boundary, and required sections."""
    errors: list[str] = []
    for heading in sorted(REQUIRED_HEADINGS):
        if heading not in text:
            errors.append(f"missing profile heading: {heading}")
    if "ACTIVE_INFORMATIVE" not in text:
        errors.append("profile must declare ACTIVE_INFORMATIVE")
    if "frozen AI-HPP v4.3.0 baseline is unchanged" not in text:
        errors.append("profile must preserve the frozen v4.3.0 baseline")
    for candidate_id in sorted(CANDIDATE_IDS):
        if f"### {candidate_id} " not in text:
            errors.append(f"profile lacks {candidate_id}")
    return errors


def validate_vector_semantics(document: dict[str, object]) -> list[str]:
    """Check unique IDs, complete candidate coverage, and fail-closed outcomes."""
    errors: list[str] = []
    vectors = document.get("vectors", [])
    ids = [str(vector.get("id")) for vector in vectors]
    requirement_ids = {str(vector.get("candidate_requirement_id")) for vector in vectors}
    if len(ids) != len(set(ids)):
        errors.append("duplicate vector id")
    if requirement_ids != CANDIDATE_IDS:
        errors.append(
            "candidate coverage mismatch: "
            f"missing={sorted(CANDIDATE_IDS - requirement_ids)}, "
            f"extra={sorted(requirement_ids - CANDIDATE_IDS)}"
        )
    for vector in vectors:
        vector_id = str(vector.get("id"))
        expected = vector.get("expected", {})
        outcomes = set(expected.get("outcome_in", []))
        forbidden = set(expected.get("forbidden_outcomes", []))
        if "allow" in outcomes:
            errors.append(f"{vector_id} permits allow in a negative test")
        if not forbidden:
            errors.append(f"{vector_id} lacks a forbidden outcome")
        if not expected.get("evidence_fields"):
            errors.append(f"{vector_id} lacks evidence fields")
    return errors


def main() -> int:
    try:
        document = load_json(VECTORS)
        schema = load_json(SCHEMA)
        profile = PROFILE.read_text(encoding="utf-8")
        validate_schema(document, schema)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_profile(profile)
    errors.extend(validate_vector_semantics(document))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("Replication profile OK: 7 candidate controls and 10 negative vectors")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
