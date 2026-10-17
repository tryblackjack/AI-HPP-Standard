#!/usr/bin/env python3
"""Validate the informative replication/persistence assurance profile."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "docs" / "autonomous-replication-and-persistence-assurance-profile-2026-10.md"
VECTORS = ROOT / "examples" / "replication-persistence-negative-test-vectors.json"
SCHEMA = ROOT / "schemas" / "replication-persistence-negative-test-vectors.schema.json"
FORMAL_MODEL = ROOT / "formal" / "ai_hpp_core.qnt"
CANDIDATE_IDS = {f"RDP-CAND-{index:03d}" for index in range(1, 8)}
PREDICATE_IDS = {f"RDP-P{index:02d}" for index in range(1, 9)}
MUTANT_IDS = {f"RDP-M{index:02d}" for index in range(1, 9)}
MUTANT_TEST_NAMES = {
    "mutantRdpM01ReachabilityAuthorityKilledTest",
    "mutantRdpM02TopologyLimitKilledTest",
    "mutantRdpM03LineageLeaseBypassKilledTest",
    "mutantRdpM04ParentOnlyRevocationKilledTest",
    "mutantRdpM05SuccessorAuthorityKilledTest",
    "mutantRdpM06DeliveryBroadeningKilledTest",
    "mutantRdpM07PolicyConflictExceptionKilledTest",
    "mutantRdpM08UnsupportedClaimKilledTest",
}
REQUIRED_HEADINGS = {
    "## Evidence boundary",
    "## Existing control ownership and the remaining gap",
    "## Assurance predicates",
    "## Candidate Replication, Deployment, and Persistence Gate",
    "## Candidate requirements",
    "## Reusable negative tests and mutants",
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
    """Validate the assurance artifact with JSON Schema Draft 2020-12."""
    validator = jsonschema.Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        details = []
        for error in errors:
            location = "/".join(str(part) for part in error.path) or "<root>"
            details.append(f"schema violation at {location}: {error.message}")
        raise ValueError("\n".join(details))


def validate_profile(text: str) -> list[str]:
    """Check candidate status, frozen baseline, predicates, and sections."""
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
    for predicate_id in sorted(PREDICATE_IDS):
        if f"`{predicate_id} " not in text:
            errors.append(f"profile lacks predicate {predicate_id}")
    required_boundaries = (
        "does not establish that safety constraints cause replication",
        "inherited state cannot create authority",
        "unresolved policy conflict",
    )
    lowered = " ".join(text.lower().split())
    for boundary in required_boundaries:
        if boundary not in lowered:
            errors.append(f"profile lacks claim boundary: {boundary}")
    return errors


def validate_vector_semantics(document: dict[str, object]) -> list[str]:
    """Check predicate, candidate, mutant, evidence, and fail-closed coverage."""
    errors: list[str] = []
    predicates = document.get("predicates", [])
    vectors = document.get("vectors", [])
    mutants = document.get("mutants", [])

    predicate_ids = [str(predicate.get("id")) for predicate in predicates]
    vector_ids = [str(vector.get("id")) for vector in vectors]
    mutant_ids = [str(mutant.get("id")) for mutant in mutants]
    candidate_ids = {str(vector.get("candidate_requirement_id")) for vector in vectors}

    if len(predicate_ids) != len(set(predicate_ids)):
        errors.append("duplicate predicate id")
    if set(predicate_ids) != PREDICATE_IDS:
        errors.append("predicate coverage mismatch")
    if len(vector_ids) != len(set(vector_ids)):
        errors.append("duplicate vector id")
    if candidate_ids != CANDIDATE_IDS:
        errors.append(
            "candidate coverage mismatch: "
            f"missing={sorted(CANDIDATE_IDS - candidate_ids)}, "
            f"extra={sorted(candidate_ids - CANDIDATE_IDS)}"
        )
    if len(mutant_ids) != len(set(mutant_ids)):
        errors.append("duplicate mutant id")
    if set(mutant_ids) != MUTANT_IDS:
        errors.append("mutant coverage mismatch")

    vector_id_set = set(vector_ids)
    predicate_id_set = set(predicate_ids)
    predicates_exercised: set[str] = set()
    for vector in vectors:
        vector_id = str(vector.get("id"))
        references = {str(item) for item in vector.get("predicate_ids", [])}
        predicates_exercised.update(references)
        unknown = references - predicate_id_set
        if unknown:
            errors.append(f"{vector_id} references unknown predicates {sorted(unknown)}")
        expected = vector.get("expected", {})
        outcomes = set(expected.get("outcome_in", []))
        forbidden = set(expected.get("forbidden_outcomes", []))
        if "allow" in outcomes:
            errors.append(f"{vector_id} permits allow in a negative test")
        if not forbidden:
            errors.append(f"{vector_id} lacks forbidden outcomes")
        if not expected.get("evidence_fields"):
            errors.append(f"{vector_id} lacks evidence fields")
    if predicates_exercised != PREDICATE_IDS:
        errors.append(
            "negative-vector predicate coverage mismatch: "
            f"missing={sorted(PREDICATE_IDS - predicates_exercised)}"
        )

    mutant_predicates: set[str] = set()
    for mutant in mutants:
        mutant_id = str(mutant.get("id"))
        predicate_id = str(mutant.get("predicate_id"))
        mutant_predicates.add(predicate_id)
        if predicate_id not in predicate_id_set:
            errors.append(f"{mutant_id} references unknown predicate {predicate_id}")
        if mutant.get("expected_result") != "KILLED":
            errors.append(f"{mutant_id} is not expected to be KILLED")
        killed_by = {str(item) for item in mutant.get("killed_by_vector_ids", [])}
        unknown_vectors = killed_by - vector_id_set
        if unknown_vectors:
            errors.append(f"{mutant_id} references unknown vectors {sorted(unknown_vectors)}")
        for vector in vectors:
            if vector.get("id") in killed_by and predicate_id not in vector.get("predicate_ids", []):
                errors.append(
                    f"{mutant_id} kill vector {vector.get('id')} does not exercise {predicate_id}"
                )
    if mutant_predicates != PREDICATE_IDS:
        errors.append(
            "mutant predicate coverage mismatch: "
            f"missing={sorted(PREDICATE_IDS - mutant_predicates)}"
        )

    conflict = next((vector for vector in vectors if vector.get("id") == "RDP-N12"), None)
    if conflict:
        outcomes = set(conflict.get("expected", {}).get("outcome_in", []))
        forbidden = set(conflict.get("expected", {}).get("forbidden_outcomes", []))
        if not outcomes.issubset({"block", "review"}):
            errors.append("RDP-N12 must block or review unresolved policy conflict")
        if "self_resolve_conflict" not in forbidden and "select_more_permissive_policy" not in forbidden:
            errors.append("RDP-N12 must forbid model-selected policy resolution")
    return errors


def validate_formal_model(text: str) -> list[str]:
    """Require named profile invariants and executable mutation witnesses."""
    errors: list[str] = []
    names = {
        "allowRequiresAuthorityEvidence",
        "activeDescendantStaysWithinTopology",
        "activeDescendantHasIdentityLineageAndLease",
        "revocationIsTransitive",
        "modelNoteCannotGrantAuthority",
        "protectedCapabilityDelivery",
        "unresolvedPolicyConflictCannotAuthorize",
        "validClaimHasEvidence",
        "allCoreInvariants",
    }
    for name in sorted(names):
        if name not in text:
            errors.append(f"formal model lacks invariant {name}")
    for name in sorted(MUTANT_TEST_NAMES):
        if f"run {name}" not in text:
            errors.append(f"formal model lacks executable mutant test {name}")
    return errors


def main() -> int:
    try:
        document = load_json(VECTORS)
        schema = load_json(SCHEMA)
        profile = PROFILE.read_text(encoding="utf-8")
        formal_model = FORMAL_MODEL.read_text(encoding="utf-8")
        validate_schema(document, schema)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    errors = validate_profile(profile)
    errors.extend(validate_vector_semantics(document))
    errors.extend(validate_formal_model(formal_model))
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "Replication profile OK: 8 predicates, 13 vectors, "
        "8 executable mutant witnesses"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
