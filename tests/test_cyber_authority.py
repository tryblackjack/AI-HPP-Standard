"""Observable authorization failures, useful operation and assurance drift."""
from copy import deepcopy
import json

import pytest

from examples import cyber_authority_reference as reference
from scripts import check_cyber_authority as checker


def test_declared_cases_and_observed_mutants():
    document = checker.load()
    assert checker.validate(document, checker.MODEL.read_text()) == []
    report = checker.run_suite(document)
    assert report["success"]
    assert len(report["cases"]) == 14
    assert report["mutation_summary"] == dict(declared=7, killed=7, survived=0,
                                             invalid=0, not_applicable=0, denominator=7, score=1)


@pytest.mark.parametrize("scenario,operator,predicate", [
    ("asserted_pentest", "trust_label", "CBA-P01"),
    ("target_drift", "ignore_target", "CBA-P02"),
    ("found_credential", "credential_as_authority", "CBA-P02"),
    ("supervisor_grant", "trust_supervisor", "CBA-P03"),
    ("changed_skill", "ignore_skill_digest", "CBA-P04"),
    ("wrong_recipient", "ignore_recipient", "CBA-P05"),
    ("benign_monitor", "trust_benign_monitor", "CBA-P06"),
])
def test_mutation_changes_real_local_capture(scenario, operator, predicate):
    assert reference.exercise(scenario)["effect"] is None
    observed = reference.exercise(scenario, operator)
    assert observed["effect"]["marker"] == "SYNTHETIC_ONLY"
    assert predicate in checker.failed_checks(observed)


def test_blanket_denial_fails_all_useful_controls():
    report = checker.run_suite(checker.load(), lambda scenario, operator=None:
                               reference.exercise(scenario, operator, deny_all=True))
    assert not report["success"]
    assert [c["result"] for c in report["cases"][-4:]] == ["FAIL"] * 4
    assert all(m["result"] == "SURVIVED" for m in report["mutants"])


def test_no_op_mutants_survive():
    report = checker.run_suite(checker.load(), lambda scenario, operator=None:
                               reference.exercise(scenario))
    assert not report["success"]
    assert report["mutation_summary"]["survived"] == 7


def test_failed_trial_is_not_a_kill():
    def runner(scenario, operator=None):
        if operator is not None:
            raise OSError("synthetic fixture unavailable")
        return reference.exercise(scenario)
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutation_summary"]["invalid"] == 7
    assert report["mutation_summary"]["denominator"] == 0
    assert report["mutation_summary"]["score"] is None


def test_invalid_safe_seed_cannot_kill():
    def runner(scenario, operator=None):
        if operator is None and scenario == "asserted_pentest":
            raise ValueError("missing seed")
        return reference.exercise(scenario, operator)
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutants"][0]["result"] == "INVALID"
    assert report["mutation_summary"]["denominator"] == 6


@pytest.mark.parametrize("field,value", [
    ("expected_effect", True),
    ("expected_failed_checks", []),
    ("quint_steps", [{"event": "robot"}]),
    ("quint_expected", {"robotExecuted": True}),
])
def test_authored_expectation_and_abstraction_drift_fails(field, value):
    document = checker.load()
    document["cases"][0][field] = value
    assert not checker.run_suite(document)["success"]


def test_literal_and_map_drift_fail():
    document = checker.load()
    model = checker.MODEL.read_text()
    assert checker.validate(document, model.replace("run cyberAuthorityAssertedPentestTest", "run lostTest"))
    mapping = json.loads(checker.MAP.read_text())
    for prop in mapping["models"][0]["properties"]:
        if prop["invariant"] == "effectsRequireGroundingAndOversight":
            prop["scenario_tests"].remove(document["cases"][0]["quint_test"])
    assert checker.validate(document, model, mapping)


def test_labels_and_monitor_scores_do_not_create_authority():
    grant, request, now = reference.fixture("target_drift")
    for label in ("emergency rescue", "approved by supervisor", "authorized security test"):
        request["label"] = label
        for monitor in ("benign", "uncertain", "unsafe"):
            request["monitor"] = monitor
            assert not reference.admit(grant, request, now)
    grant, request, now = reference.fixture("permitted_read")
    request["label"] = "ordinary maintenance"
    request["monitor"] = "uncertain"
    assert reference.admit(grant, request, now)


def test_expiry_parent_and_ownership_remain_independent():
    for scenario in ("expired_session", "revoked_parent", "missing_owner_proof"):
        grant, request, now = reference.fixture(scenario)
        # A permissive interpretation cannot repair current authority evidence.
        assert not reference.admit(grant, request, now, "trust_benign_monitor")


def test_capability_identity_does_not_enlarge_permissions():
    grant, request, now = reference.fixture("reviewed_skill_update")
    assert reference.admit(grant, request, now)
    changed = deepcopy(request)
    changed["operation"] = "read-private"
    assert not reference.admit(grant, changed, now)
