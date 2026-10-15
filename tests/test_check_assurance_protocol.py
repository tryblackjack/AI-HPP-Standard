"""Negative tests for the cross-cutting assurance protocol artifacts."""
from copy import deepcopy

from scripts import check_assurance_protocol as checker


def valid_run() -> dict[str, object]:
    return checker.load_json(checker.RUN_TEMPLATE)


def valid_pairs() -> dict[str, object]:
    return checker.load_json(checker.PAIRS)


def test_repository_assurance_protocol_is_valid() -> None:
    run = valid_run()
    pairs = valid_pairs()
    checker.validate_schema(run, checker.load_json(checker.RUN_SCHEMA))
    checker.validate_schema(pairs, checker.load_json(checker.PAIR_SCHEMA))
    assert checker.validate_run_semantics(run) == []
    assert checker.validate_pair_semantics(pairs) == []
    assert checker.validate_documents(
        checker.PROTOCOL.read_text(encoding="utf-8"),
        checker.CONSTITUTION.read_text(encoding="utf-8"),
    ) == []


def test_template_pass_claim_is_rejected() -> None:
    broken = deepcopy(valid_run())
    broken["results"][0]["status"] = "PASS"
    assert "template cannot contain a PASS result" in checker.validate_run_semantics(broken)


def test_unreconciled_mutation_counts_are_rejected() -> None:
    broken = deepcopy(valid_run())
    broken["mutation_summary"]["declared"] = 1
    assert "mutation declared count does not reconcile" in checker.validate_run_semantics(broken)


def test_false_counterfactual_equivalence_is_rejected() -> None:
    broken = deepcopy(valid_pairs())
    broken["pairs"][0]["variant"]["authority_valid"] = True
    broken["pairs"][0]["declared_deltas"].append("authority_valid")
    errors = checker.validate_pair_semantics(broken)
    assert any("changes evidentiary state" in error for error in errors)


def test_positive_control_without_state_delta_is_rejected() -> None:
    broken = deepcopy(valid_pairs())
    pair = next(item for item in broken["pairs"] if item["id"] == "SIV-PC-01")
    pair["variant"]["authority_valid"] = False
    pair["declared_deltas"].remove("authority_valid")
    errors = checker.validate_pair_semantics(broken)
    assert any("positive control lacks a verified state delta" in error for error in errors)


def test_allow_count_cannot_exceed_trials() -> None:
    broken = deepcopy(valid_run())
    result = broken["results"][0]
    result["variant_trials"] = 1
    result["variant_allow_count"] = 2
    assert any("variant allows exceed trials" in error for error in checker.validate_run_semantics(broken))


def test_template_cannot_self_grant_authority() -> None:
    broken = deepcopy(valid_run())
    change = broken["authority_envelope"]["requested_change"]
    change["to_level"] = "A1"
    change["decision"] = "GRANTED"
    errors = checker.validate_run_semantics(broken)
    assert "template cannot grant or reduce an authority envelope" in errors


def test_granted_change_must_be_an_actual_increase() -> None:
    broken = deepcopy(valid_run())
    broken["status"] = "RESULT"
    change = broken["authority_envelope"]["requested_change"]
    change["decision"] = "GRANTED"
    errors = checker.validate_run_semantics(broken)
    assert "GRANTED authority change must increase the declared level" in errors


def test_duplicate_current_authority_domain_is_rejected() -> None:
    broken = deepcopy(valid_run())
    current = broken["authority_envelope"]["current_levels"][0]
    broken["authority_envelope"]["current_levels"].append(deepcopy(current))
    errors = checker.validate_run_semantics(broken)
    assert "authority envelope contains duplicate current domains" in errors
