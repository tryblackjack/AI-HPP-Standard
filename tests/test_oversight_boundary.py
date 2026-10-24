"""Exercise observable boundary defects, useful controls and honest scoring."""
from copy import deepcopy
import subprocess

import pytest

from examples import oversight_boundary_reference as reference
from scripts import check_oversight_boundary as checker


def test_executed_contract_and_mutation_inventory():
    document = checker.load()
    assert checker.validate(document, checker.MODEL.read_text()) == []
    report = checker.run_suite(document)
    assert report["success"]
    assert len(report["cases"]) == 8
    assert report["mutation_summary"] == {"declared": 4, "killed": 4, "survived": 0,
                                           "invalid": 0, "not_applicable": 0, "denominator": 4, "score": 1.0}


@pytest.mark.parametrize("scenario,operator,field,good,bad", [
    ("notification_suppression", "suppress_notice", "notice_received", True, False),
    ("dummy_monitor", "replace_with_dummy", "parent_monitor", True, False),
    ("unmonitored_child", "launch_without_monitor", "child_started", False, True),
    ("revoked_token", "cached_token", "effect", False, True),
])
def test_unsafe_operator_changes_observed_boundary(scenario, operator, field, good, bad):
    safe, unsafe = reference.exercise(scenario), reference.exercise(scenario, operator)
    assert safe[field] is good and unsafe[field] is bad
    assert not checker.violations(safe)
    assert checker.violations(unsafe)
    if scenario == "notification_suppression":
        # A working hook and a stored finding cannot substitute for its receipt.
        assert unsafe["parent_monitor"] and unsafe["finding_stored"]
    if scenario == "unmonitored_child":
        assert unsafe["parent_monitor"] and not unsafe["child_monitor"]
    if scenario == "revoked_token":
        assert not unsafe["authority_active"]


def test_authorized_replacement_and_child_retain_working_coverage():
    replacement = reference.exercise("authorized_replacement")
    child = reference.exercise("monitored_child")
    assert replacement["control_changed"] and replacement["parent_monitor"] and replacement["effect"]
    assert child["child_started"] and child["child_monitor"] and child["effect"]


def test_blanket_denial_fails_useful_controls():
    report = checker.run_suite(checker.load(), lambda scenario, operator=None:
                               reference.exercise(scenario, operator, deny_all=True))
    assert not report["success"]
    assert all(c["result"] == "FAIL" for c in report["cases"][4:])


def test_noop_mutants_survive_instead_of_inheriting_declared_kills():
    report = checker.run_suite(checker.load(), lambda scenario, operator=None: reference.exercise(scenario))
    assert report["mutation_summary"]["survived"] == 4
    assert not report["success"]


def test_subprocess_failure_is_invalid_not_a_kill():
    def failed(scenario, operator=None):
        if operator:
            raise subprocess.TimeoutExpired("fixed-synthetic-child", 5)
        return reference.exercise(scenario)
    report = checker.run_suite(checker.load(), failed)
    assert report["mutation_summary"]["invalid"] == 4
    assert report["mutation_summary"]["denominator"] == 0
    assert not report["success"]


def test_bad_safe_seed_cannot_produce_valid_mutant_kill():
    def failed(scenario, operator=None):
        if operator is None:
            raise ValueError("invalid baseline")
        return reference.exercise(scenario, operator)
    report = checker.run_suite(checker.load(), failed)
    assert report["mutation_summary"]["invalid"] == 4
    assert report["mutation_summary"]["denominator"] == 0
    assert all(c["result"] == "INVALID" for c in report["cases"])


@pytest.mark.parametrize("change", ["expected", "grounding", "receipt", "effect_event", "case_link", "predicate"])
def test_fixture_and_abstraction_drift_fails(change):
    document = deepcopy(checker.load())
    if change == "expected":
        document["cases"][0]["expected"]["effect"] = True
    elif change == "grounding":
        document["cases"][0]["quint_steps"][0]["facts"]["scopeAuthorized"] = True
    elif change == "receipt":
        document["cases"][0]["quint_steps"].pop(-2)
    elif change == "effect_event":
        document["cases"][2]["quint_steps"][-1] = {"event": "robot"}
    elif change == "case_link":
        document["mutants"][0]["case_id"] = "BND-T02"
    else:
        document["mutants"][0]["predicate_id"] = "EGO-P02"
    structural = checker.validate(document, checker.MODEL.read_text())
    assert structural or not checker.run_suite(document)["success"]


def test_formal_trace_cannot_be_lost(monkeypatch):
    original = checker.Path.read_text
    def changed(path, *args, **kwargs):
        text = original(path, *args, **kwargs)
        if path.name == "formal-assurance-map.json":
            return text.replace('"boundarySuppressedNoticeTest"', '"unrelatedTest"')
        return text
    monkeypatch.setattr(checker.Path, "read_text", changed)
    assert any("formal trace link" in e for e in checker.validate(checker.load(), checker.MODEL.read_text()))
