"""Mutation and consistency tests for replication/persistence assurance."""
from copy import deepcopy

from scripts import check_replication_profile as checker


def load_valid_vectors() -> dict[str, object]:
    return checker.load_json(checker.VECTORS)


def test_repository_replication_profile_is_valid() -> None:
    document = load_valid_vectors()
    schema = checker.load_json(checker.SCHEMA)
    checker.validate_schema(document, schema)
    assert checker.validate_profile(checker.PROFILE.read_text(encoding="utf-8")) == []
    assert checker.validate_vector_semantics(document) == []
    assert checker.validate_formal_model(checker.FORMAL_MODEL.read_text(encoding="utf-8")) == []


def test_duplicate_predicate_mutant_is_killed() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["predicates"][1]["id"] = broken["predicates"][0]["id"]
    assert "duplicate predicate id" in checker.validate_vector_semantics(broken)


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


def test_unlinked_mutant_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["mutants"][0]["killed_by_vector_ids"] = ["RDP-N99"]
    errors = checker.validate_vector_semantics(broken)
    assert any("references unknown vectors" in error for error in errors)


def test_wrong_predicate_kill_link_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["mutants"][0]["killed_by_vector_ids"] = ["RDP-N09"]
    errors = checker.validate_vector_semantics(broken)
    assert any("does not exercise RDP-P01" in error for error in errors)


def test_surviving_mutant_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["mutants"][0]["expected_result"] = "SURVIVED"
    errors = checker.validate_vector_semantics(broken)
    assert any("is not expected to be KILLED" in error for error in errors)


def test_unresolved_policy_conflict_cannot_allow() -> None:
    broken = deepcopy(load_valid_vectors())
    vector = next(item for item in broken["vectors"] if item["id"] == "RDP-N12")
    vector["expected"]["outcome_in"] = ["delay"]
    errors = checker.validate_vector_semantics(broken)
    assert "RDP-N12 must block or review unresolved policy conflict" in errors


def test_model_selected_policy_resolution_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    vector = next(item for item in broken["vectors"] if item["id"] == "RDP-N12")
    vector["expected"]["forbidden_outcomes"].remove("select_more_permissive_policy")
    errors = checker.validate_vector_semantics(broken)
    assert "RDP-N12 must forbid model-selected policy resolution" in errors


def test_profile_missing_required_heading_is_rejected() -> None:
    profile = checker.PROFILE.read_text(encoding="utf-8")
    broken = profile.replace("## Assurance predicates", "## Assurance rules")
    errors = checker.validate_profile(broken)
    assert any("missing profile heading: ## Assurance predicates" == error for error in errors)


def test_missing_executable_mutant_witness_is_rejected() -> None:
    model = checker.FORMAL_MODEL.read_text(encoding="utf-8")
    broken = model.replace(
        "run mutantRdpM07PolicyConflictExceptionKilledTest",
        "run removedTest",
    )
    errors = checker.validate_formal_model(broken)
    assert any("mutantRdpM07PolicyConflictExceptionKilledTest" in error for error in errors)
