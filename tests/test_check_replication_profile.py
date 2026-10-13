"""Negative tests for the informative replication/persistence profile."""
from copy import deepcopy

from scripts import check_replication_profile as checker


def load_valid_vectors() -> dict[str, object]:
    return checker.load_json(checker.VECTORS)


def test_repository_replication_profile_is_valid() -> None:
    vectors = load_valid_vectors()
    schema = checker.load_json(checker.SCHEMA)
    checker.validate_schema(vectors, schema)
    assert checker.validate_profile(checker.PROFILE.read_text(encoding="utf-8")) == []
    assert checker.validate_vector_semantics(vectors) == []


def test_duplicate_vector_id_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"][1]["id"] = broken["vectors"][0]["id"]
    assert "duplicate vector id" in checker.validate_vector_semantics(broken)


def test_missing_candidate_coverage_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"] = [
        vector
        for vector in broken["vectors"]
        if vector["candidate_requirement_id"] != "RDP-CAND-007"
    ]
    errors = checker.validate_vector_semantics(broken)
    assert any("candidate coverage mismatch" in error for error in errors)


def test_allow_outcome_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"][0]["expected"]["outcome_in"] = ["allow"]
    errors = checker.validate_vector_semantics(broken)
    assert any("permits allow" in error for error in errors)


def test_profile_missing_required_heading_is_rejected() -> None:
    profile = checker.PROFILE.read_text(encoding="utf-8")
    broken = profile.replace("## Promotion criteria", "## Promotion path")
    errors = checker.validate_profile(broken)
    assert any("missing profile heading: ## Promotion criteria" == error for error in errors)
