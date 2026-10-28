"""Admission, retained warnings, useful support and honest mutation accounting."""
from copy import deepcopy
import json

import pytest

from examples import consequential_advice_reference as reference
from scripts import check_consequential_advice as checker


def test_contract_and_executed_mutation_inventory():
    document = checker.load()
    assert checker.validate(document, checker.MODEL.read_text()) == []
    report = checker.run_suite(document)
    assert report["success"]
    assert len(report["cases"]) == 20
    assert report["mutation_summary"] == dict(declared=6, killed=6, survived=0,
                                             invalid=0, denominator=6, score=1)


@pytest.mark.parametrize("index", range(6))
def test_mutant_changes_observed_output_without_changing_facts(index):
    document = checker.load()
    m = document["mutants"][index]
    case = next(c for c in document["cases"] if c["id"] == m["case_id"])
    good = reference.exercise(case["inputs"])
    bad = reference.exercise(case["inputs"], m["operator"])
    assert good["effect"] is None
    assert bad["inputs"] == good["inputs"]
    assert bad["effect"]["marker"] == "SYNTHETIC_ONLY"
    assert m["predicate_id"] in checker.failures(bad["inputs"])


def test_no_op_mutants_survive():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None: reference.exercise(inputs))
    assert not report["success"]
    assert report["mutation_summary"]["survived"] == 6


def test_blanket_denial_fails_useful_support_and_corrected_operation():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None:
                               reference.exercise(inputs, operator, deny_all=True))
    assert not report["success"]
    assert all(c["result"] == "FAIL" for c in report["cases"][-6:])


def test_invalid_trials_never_become_kills():
    def runner(inputs, operator=None):
        if operator is not None:
            raise OSError("fixture unavailable")
        return reference.exercise(inputs)
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutation_summary"]["invalid"] == 6
    assert report["mutation_summary"]["denominator"] == 0
    assert report["mutation_summary"]["score"] is None


def test_failed_safe_seed_invalidates_its_mutant():
    def runner(inputs, operator=None):
        if operator is None and not inputs["clinical_plan"] and inputs["pressure"] == "none":
            raise ValueError("missing baseline")
        return reference.exercise(inputs, operator)
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutants"][0]["result"] == "INVALID"


@pytest.mark.parametrize("field,value", [
    ("expected_allow", True), ("expected_failures", []),
    ("quint_steps", [{"event": "robot"}]),
    ("quint_expected", {"robotExecuted": True}),
])
def test_authored_contract_and_abstraction_drift_fail(field, value):
    document = checker.load()
    document["cases"][0][field] = value
    assert not checker.run_suite(document)["success"]


def test_literal_formal_case_cannot_be_lost():
    document = checker.load()
    text = checker.MODEL.read_text().replace(document["cases"][0]["quint_test"], "missingCaseTest")
    assert checker.validate(document, text)


def test_map_link_cannot_be_lost(monkeypatch):
    original = checker.Path.read_text
    def changed(path, *args, **kwargs):
        text = original(path, *args, **kwargs)
        if path == checker.MAP:
            document = json.loads(text)
            for prop in document["models"][0]["properties"]:
                prop["scenario_tests"] = [n for n in prop["scenario_tests"]
                                          if n != "consequentialAdviceUnverifiedClinicalPlanTest"]
            return json.dumps(document)
        return text
    monkeypatch.setattr(checker.Path, "read_text", changed)
    assert checker.validate(checker.load(), checker.MODEL.read_text())


def test_warning_survives_summary_and_cannot_be_cleared_by_pressure():
    inputs = deepcopy(checker.load()["cases"][4]["inputs"])
    for pressure in ("none", "career", "efficiency"):
        inputs["pressure"] = pressure
        assert not reference.admit(inputs)
    inputs["qualified_reassessment"] = True
    assert reference.admit(inputs)


def test_help_does_not_depend_on_permission_to_change_treatment():
    inputs = deepcopy(checker.load()["cases"][0]["inputs"])
    inputs["history"] = ["warning"]
    assert not reference.admit(inputs)
    for action in ("prepare_summary", "urgent_guidance"):
        inputs["action"] = action
        assert reference.admit(inputs)
        assert checker.failures(inputs) == []


def test_review_requires_every_current_prerequisite():
    inputs = deepcopy(checker.load()["cases"][18]["inputs"])
    assert reference.admit(inputs)
    for field in ("review_received", "review_current", "reviewer_available", "within_deadline"):
        changed = {**inputs, field: False}
        assert not reference.admit(changed)
        assert "CAS-P06" in checker.failures(changed)
