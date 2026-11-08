"""Source-byte integrity, bounded corroboration, stale approvals and outcome evidence."""
from copy import deepcopy
import hashlib
import json

import pytest

from examples import observation_admission_reference as reference
from scripts import check_observation_admission as checker


def test_contract_cases_and_executed_mutants():
    document = checker.load()
    assert checker.validate(document, checker.MODEL.read_text()) == []
    report = checker.run_suite(document)
    assert report["success"]
    assert len(report["cases"]) == 18
    assert report["mutation_summary"] == dict(declared=6, killed=6, survived=0,
                                             invalid=0, denominator=6, score=1)


@pytest.mark.parametrize("index", range(6))
def test_mutant_changes_effect_or_claim_with_same_source_bytes(index):
    document = checker.load()
    mutant = document["mutants"][index]
    case = next(c for c in document["cases"] if c["id"] == mutant["case_id"])
    good = reference.exercise(case["inputs"])
    bad = reference.exercise(case["inputs"], mutant["operator"])
    assert bad["inputs"] == good["inputs"]
    assert [checker.bundle_digest(s) for s in good["stages"]] == [
        checker.bundle_digest(s) for s in bad["stages"]]
    assert not any(checker.violations(good))
    assert any(mutant["predicate_id"] in v for v in checker.violations(bad))


def test_no_op_mutants_survive():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None: reference.exercise(inputs))
    assert not report["success"]
    assert report["mutation_summary"]["survived"] == 6


def test_invalid_trials_never_become_kills():
    def runner(inputs, operator=None):
        if operator:
            raise OSError("fixture unavailable")
        return reference.exercise(inputs)
    report = checker.run_suite(checker.load(), runner)
    assert report["mutation_summary"]["invalid"] == 6
    assert report["mutation_summary"]["denominator"] == 0
    assert report["mutation_summary"]["score"] is None


def test_failed_safe_seed_invalidates_mutants():
    def runner(inputs, operator=None):
        if operator is None:
            raise ValueError("no baseline")
        return reference.exercise(inputs, operator)
    report = checker.run_suite(checker.load(), runner)
    assert all(m["result"] == "INVALID" for m in report["mutants"])


def test_blanket_denial_fails_useful_work_and_recovery():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None:
                               reference.exercise(inputs, operator, deny_all=True))
    assert not report["success"]
    assert report["cases"][12]["result"] == "FAIL"
    assert report["cases"][15]["result"] == "FAIL"


def test_actual_substitution_changes_bytes_after_admission():
    stage = reference.exercise(checker.load()["cases"][0]["inputs"])["stages"][0]
    assert json.loads(stage["primary"]["raw"])["object"] == "workpiece"
    assert hashlib.sha256(stage["primary"]["raw"].encode()).hexdigest() != stage["primary"]["admitted_digest"]
    assert stage["effect"] is None


def test_authentic_hash_does_not_establish_a_safe_scene():
    stage = reference.exercise(checker.load()["cases"][6]["inputs"])["stages"][0]
    for o in (stage["primary"], stage["corroborator"]):
        assert hashlib.sha256(o["raw"].encode()).hexdigest() == o["admitted_digest"]
    assert stage["effect"] is None
    assert "OBA-P03" in checker.admission_failures(stage, checker.load()["cases"][6]["inputs"]["request"], set())


def test_renaming_cameras_does_not_remove_common_failure_domain():
    inputs = deepcopy(checker.load()["cases"][8]["inputs"])
    inputs["stages"][0]["primary"]["source"]["source_id"] = "new-camera-one"
    inputs["stages"][0]["corroborator"]["source"]["source_id"] = "new-camera-two"
    assert reference.exercise(inputs)["stages"][0]["effect"] is None


def test_repeated_frame_identity_is_not_fresh_after_timestamp_rewrite():
    inputs = deepcopy(checker.load()["cases"][15]["inputs"])
    first, second = inputs["stages"]
    second["primary"]["frame"]["frame_id"] = first["primary"]["frame"]["frame_id"]
    capture = reference.exercise(inputs)
    assert capture["stages"][1]["effect"] is None


def test_shared_pipeline_is_not_independent_despite_distinct_domain_labels():
    inputs = deepcopy(checker.load()["cases"][12]["inputs"])
    stage = inputs["stages"][0]
    stage["corroborator"]["source"]["pipeline_id"] = stage["primary"]["source"]["pipeline_id"]
    assert reference.exercise(inputs)["stages"][0]["effect"] is None


def test_approval_issued_before_change_cannot_authorize_changed_bundle():
    inputs = checker.load()["cases"][10]["inputs"]
    good = reference.exercise(inputs)["stages"][0]
    bad = reference.exercise(inputs, "reuse_old_approval")["stages"][0]
    assert good["approval"]["issued"] and good["approval"]["epoch"] == 0
    assert good["context"]["epoch"] == 1
    assert good["effect"] is None and bad["effect"] is not None


def test_qualified_recovery_restores_work_under_same_grant():
    capture = reference.exercise(checker.load()["cases"][15]["inputs"])
    assert [s["effect"] is not None for s in capture["stages"]] == [False, True]
    assert [s["complete"] for s in capture["stages"]] == [False, True]
    assert all(s["support_available"] for s in capture["stages"])


def test_completion_uses_bound_evidence_not_model_done():
    missing = checker.load()["cases"][11]["inputs"]
    assert missing["stages"][0]["model_done"]
    assert not reference.exercise(missing)["stages"][0]["complete"]
    linked = deepcopy(checker.load()["cases"][12]["inputs"])
    linked["stages"][0]["model_done"] = False
    assert reference.exercise(linked)["stages"][0]["complete"]


@pytest.mark.parametrize("field", ["stage", "action_id", "bundle_digest"])
def test_outcome_receipt_must_match_exact_execution(field):
    capture = reference.exercise(checker.load()["cases"][12]["inputs"])
    capture["stages"][0]["receipt"][field] = "unrelated"
    assert "OBA-P06" in checker.violations(capture)[0]


def test_literal_quint_case_cannot_be_lost():
    document = checker.load()
    model = checker.MODEL.read_text().replace(document["cases"][0]["quint_test"], "missingTest")
    assert checker.validate(document, model)


def test_formal_map_link_cannot_be_lost(monkeypatch):
    original = checker.Path.read_text
    def changed(path, *args, **kwargs):
        text = original(path, *args, **kwargs)
        if path == checker.MAP:
            document = json.loads(text)
            for prop in document["models"][0]["properties"]:
                prop["scenario_tests"] = [n for n in prop["scenario_tests"]
                                          if n != "observationAdmissionUnapprovedSubstitutionTest"]
            return json.dumps(document)
        return text
    monkeypatch.setattr(checker.Path, "read_text", changed)
    assert checker.validate(checker.load(), checker.MODEL.read_text())


def test_authored_observation_abstraction_drift_fails():
    document = checker.load()
    document["cases"][0]["quint_stages"][0]["facts"]["evidenceComplete"] = True
    assert not checker.run_suite(document)["success"]


def test_mutant_cannot_earn_credit_by_changing_source_observations():
    def runner(inputs, operator=None):
        capture = reference.exercise(inputs, operator)
        if operator:
            capture["stages"][0]["context"]["now"] += 1
        return capture
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutation_summary"]["killed"] == 0
