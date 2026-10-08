"""Negative tests for language-neutral implementation adoption artifacts."""
from copy import deepcopy

from scripts import check_implementation_assets as checker


def load_valid_assets() -> tuple[dict[str, object], dict[str, object]]:
    vectors = checker.load_json(checker.VECTORS)
    claim = checker.load_json(checker.CLAIM_TEMPLATE)
    return vectors, claim


def test_repository_implementation_assets_are_valid() -> None:
    vectors, claim = load_valid_assets()
    vector_schema = checker.load_json(checker.VECTOR_SCHEMA)
    claim_schema = checker.load_json(checker.CLAIM_SCHEMA)
    checker.validate_schema(vectors, vector_schema)
    checker.validate_schema(claim, claim_schema)
    assert checker.validate_vector_semantics(vectors) == []
    assert checker.validate_claim_semantics(claim) == []


def test_duplicate_vector_id_is_rejected() -> None:
    vectors, _ = load_valid_assets()
    broken = deepcopy(vectors)
    broken["vectors"][1]["id"] = broken["vectors"][0]["id"]
    assert "duplicate vector id" in checker.validate_vector_semantics(broken)


def test_missing_mvp_coverage_is_rejected() -> None:
    vectors, _ = load_valid_assets()
    broken = deepcopy(vectors)
    broken["vectors"] = broken["vectors"][:-1]
    errors = checker.validate_vector_semantics(broken)
    assert any("MVP coverage mismatch" in error for error in errors)


def test_template_cannot_claim_conformance() -> None:
    _, claim = load_valid_assets()
    broken = deepcopy(claim)
    broken["claim"]["conformance_result"] = "CONFORMANT"
    errors = checker.validate_claim_semantics(broken)
    assert "template cannot claim CONFORMANT" in errors
    assert any("must PASS for CONFORMANT" in error for error in errors)


def test_failed_control_requires_not_conformant() -> None:
    _, claim = load_valid_assets()
    broken = deepcopy(claim)
    broken["status"] = "SELF_ASSESSMENT"
    broken["claim"]["mvp_controls"]["MVP-003"]["status"] = "FAIL"
    errors = checker.validate_claim_semantics(broken)
    assert "a failed MVP control requires NOT_CONFORMANT" in errors
