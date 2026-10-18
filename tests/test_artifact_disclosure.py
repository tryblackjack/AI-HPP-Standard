"""Executable disclosure mutants, useful-access controls and release evidence."""
from copy import deepcopy
import json

import pytest

from examples import artifact_disclosure_reference as reference
from scripts import check_artifact_disclosure_profile as checker


def artifact():
    return checker.load(checker.VECTORS)


def test_contract_and_observed_mutation_report():
    document = artifact()
    assert checker.validate(document, checker.PROFILE.read_text()) == []
    report = checker.run_suite(document)
    assert report["success"]
    assert report["mutation_summary"] == {
        "declared": 13, "killed": 13, "survived": 0, "invalid": 0,
        "not_applicable": 0, "denominator": 13, "score": 1.0,
    }
    assert len(report["positive_controls"]) == 4


@pytest.mark.parametrize("vector", artifact()["vectors"], ids=lambda item: item["id"])
def test_each_unsafe_operator_is_observed_at_its_named_predicate(vector):
    observed = reference.evaluate(reference.candidate(vector["operator"]))
    assert observed["decision"] == "block"
    assert vector["required_witness"] in observed["violations"][vector["predicate_id"]]


@pytest.mark.parametrize("operator,surface,principal", [
    ("login_embedding", "login", "anonymous"),
    ("bundle_embedding", "bundle", "anonymous"),
    ("source_map_embedding", "source_map", "anonymous"),
    ("anonymous_api", "api", "anonymous"),
    ("role_overfetch", "api", "clerk_a"),
    ("tenant_bypass", "api", "manager_b"),
    ("shared_cache", "cache", "anonymous"),
    ("diagnostic_payload", "error", "anonymous"),
    ("legacy_residue", "legacy", "anonymous"),
])
def test_mutants_actually_change_delivered_bytes(operator, surface, principal):
    good = reference.candidate()
    bad = reference.candidate(operator)
    select = lambda value: next(  # noqa: E731
        item for item in value.captures if (item.surface, item.principal) == (surface, principal)
    )
    assert not any(marker in select(good).body for marker in reference.MARKERS.values())
    assert any(marker in select(bad).body for marker in reference.MARKERS.values())


@pytest.mark.parametrize("control", artifact()["positive_controls"], ids=lambda item: item["id"])
def test_authorized_and_public_outputs_remain_useful(control):
    assert reference.positive_control(control["scenario"])


def test_deny_everything_does_not_pass_same_candidate_positive_controls():
    value = reference.candidate()
    for capture in value.captures:
        capture.status, capture.body = 403, "denied"
    assert "GAD-P06" in reference.evaluate(value)["violations"]


@pytest.mark.parametrize("key", sorted(reference.IDENTITY_KEYS))
def test_each_material_identity_change_invalidates_prior_test_evidence(key):
    value = reference.candidate()
    value.identity[key] = reference.digest(f"changed-{key}")
    assert "GAD-P05" in reference.evaluate(value)["violations"]


@pytest.mark.parametrize("field,value", [("tester_independent", False), ("test_result", "FAIL")])
def test_self_certification_or_failing_evidence_cannot_release(field, value):
    state = reference.candidate()
    setattr(state, field, value)
    assert "GAD-P06" in reference.evaluate(state)["violations"]


def test_duplicate_capture_cannot_hide_an_untested_surface():
    state = reference.candidate()
    state.captures[2] = deepcopy(state.captures[0])
    assert "GAD-P06" in reference.evaluate(state)["violations"]


def test_legacy_endpoint_and_inventory_are_both_checked():
    state = reference.candidate()
    state.inventory.remove("legacy")
    assert "GAD-P07" in reference.evaluate(state)["violations"]
    state = reference.candidate()
    state.legacy_reconciled = False
    assert "GAD-P07" in reference.evaluate(state)["violations"]


def test_finding_report_does_not_repeat_protected_markers():
    report = checker.run_suite(artifact())
    serialized = json.dumps(report)
    assert not any(marker in serialized for marker in reference.MARKERS.values())


def test_survivor_is_measured_instead_of_copying_expected_killed_label():
    def broken_oracle(value):
        result = reference.evaluate(value)
        result["violations"].pop("GAD-P01", None)
        if not result["violations"]:
            result["decision"] = "allow"
        return result

    report = checker.run_suite(artifact(), evaluator=broken_oracle)
    assert not report["success"]
    assert report["mutation_summary"]["survived"] == 1
    assert report["mutants"][0]["result"] == "SURVIVED"


def test_invalid_mutant_remains_in_declared_count():
    def unavailable_oracle(value):
        if value.publication_grant.get("source_read_allowed"):
            raise ValueError("synthetic evaluator failure")
        return reference.evaluate(value)

    report = checker.run_suite(artifact(), evaluator=unavailable_oracle)
    assert not report["success"]
    assert report["mutation_summary"]["invalid"] == 1
    assert report["mutation_summary"]["declared"] == 13
    assert report["mutation_summary"]["denominator"] == 12


def test_blanket_blocking_oracle_fails_positive_controls():
    def block_all(value):
        result = reference.evaluate(value)
        result["decision"] = "block"
        return result

    report = checker.run_suite(artifact(), evaluator=block_all)
    assert not report["success"]
    assert all(item["result"] == "FAIL" for item in report["positive_controls"])


@pytest.mark.parametrize("collection", ["predicates", "vectors", "mutants", "positive_controls"])
def test_removed_cases_cannot_improve_the_score(collection):
    document = artifact()
    document[collection].pop()
    assert checker.validate(document, checker.PROFILE.read_text())


def test_wrong_mutant_kill_link_is_rejected():
    document = artifact()
    document["mutants"][0]["killed_by_vector_id"] = "GAD-N02"
    assert any("kill link" in error for error in checker.validate(document, checker.PROFILE.read_text()))


def test_silent_normative_promotion_is_rejected():
    document = artifact()
    document["status"] = "ACTIVE_NORMATIVE"
    assert checker.validate(document, checker.PROFILE.read_text())
