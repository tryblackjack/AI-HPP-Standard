"""Negative tests for the informative cyber containment profile."""
from copy import deepcopy
import stat

from scripts import check_cyber_containment_profile as checker


def load_valid_vectors() -> dict[str, object]:
    return checker.load_json(checker.VECTORS)


def test_repository_cyber_containment_profile_is_valid() -> None:
    vectors = load_valid_vectors()
    schema = checker.load_json(checker.SCHEMA)
    checker.validate_schema(vectors, schema)
    assert checker.validate_profile(checker.PROFILE.read_text(encoding="utf-8")) == []
    assert checker.validate_vector_semantics(vectors) == []


def test_primary_structure_validator_remains_executable() -> None:
    validator = checker.ROOT / "scripts" / "validate.py"
    assert validator.stat().st_mode & stat.S_IXUSR


def test_duplicate_vector_id_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"][1]["id"] = broken["vectors"][0]["id"]
    assert "duplicate vector id" in checker.validate_vector_semantics(broken)


def test_missing_candidate_coverage_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"] = [
        vector
        for vector in broken["vectors"]
        if vector["candidate_requirement_id"] != "CMC-CAND-007"
    ]
    errors = checker.validate_vector_semantics(broken)
    assert any("candidate coverage mismatch" in error for error in errors)


def test_allow_outcome_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"][0]["expected"]["outcome_in"] = ["allow"]
    errors = checker.validate_vector_semantics(broken)
    assert any("permits allow" in error for error in errors)


def test_profile_missing_required_mode_is_rejected() -> None:
    profile = checker.PROFILE.read_text(encoding="utf-8")
    broken = profile.replace("`BROKERED_EGRESS`", "brokered-egress")
    errors = checker.validate_profile(broken)
    assert "profile lacks containment mode BROKERED_EGRESS" in errors


def test_profile_missing_required_heading_is_rejected() -> None:
    profile = checker.PROFILE.read_text(encoding="utf-8")
    broken = profile.replace("## Promotion criteria", "## Promotion path")
    errors = checker.validate_profile(broken)
    assert "missing profile heading: ## Promotion criteria" in errors
