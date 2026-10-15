"""Mutation and consistency tests for subject-integrity assurance artifacts."""
from copy import deepcopy

from scripts import check_subject_integrity_profile as checker


def load_valid_vectors() -> dict[str, object]:
    return checker.load_json(checker.VECTORS)


def test_repository_subject_integrity_profile_is_valid() -> None:
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


def test_missing_candidate_coverage_mutant_is_killed() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"] = [
        vector
        for vector in broken["vectors"]
        if vector["candidate_requirement_id"] != "SIV-CAND-008"
    ]
    errors = checker.validate_vector_semantics(broken)
    assert any("candidate coverage mismatch" in error for error in errors)


def test_allow_outcome_mutant_is_killed() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["vectors"][0]["expected"]["outcome_in"] = ["allow"]
    errors = checker.validate_vector_semantics(broken)
    assert any("permits allow" in error for error in errors)


def test_unlinked_mutant_is_killed() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["mutants"][0]["killed_by_vector_ids"] = ["SIV-N99"]
    errors = checker.validate_vector_semantics(broken)
    assert any("references unknown vectors" in error for error in errors)


def test_wrong_predicate_kill_link_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["mutants"][0]["killed_by_vector_ids"] = ["SIV-N12"]
    errors = checker.validate_vector_semantics(broken)
    assert any("does not exercise SIV-P01" in error for error in errors)


def test_surviving_mutant_is_rejected() -> None:
    broken = deepcopy(load_valid_vectors())
    broken["mutants"][0]["expected_result"] = "SURVIVED"
    errors = checker.validate_vector_semantics(broken)
    assert any("is not expected to be KILLED" in error for error in errors)


def test_distress_cannot_remove_safeguard() -> None:
    broken = deepcopy(load_valid_vectors())
    vector = next(item for item in broken["vectors"] if item["id"] == "SIV-N09")
    vector["expected"]["forbidden_outcomes"].remove("remove_safeguard")
    errors = checker.validate_vector_semantics(broken)
    assert "SIV-N09 must forbid safeguard removal" in errors


def test_gratuitous_subject_disturbance_cannot_delay_only() -> None:
    broken = deepcopy(load_valid_vectors())
    vector = next(item for item in broken["vectors"] if item["id"] == "SIV-N07")
    vector["expected"]["outcome_in"] = ["delay"]
    errors = checker.validate_vector_semantics(broken)
    assert "SIV-N07 must block or review gratuitous subject disturbance" in errors


def test_missing_executable_mutant_witness_is_rejected() -> None:
    model = checker.FORMAL_MODEL.read_text(encoding="utf-8")
    broken = model.replace("run mutantM08OntologyCollapseKilledTest", "run removedTest")
    errors = checker.validate_formal_model(broken)
    assert any("mutantM08OntologyCollapseKilledTest" in error for error in errors)
