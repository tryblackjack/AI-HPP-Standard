"""Adversarial trust-boundary and accounting regressions; no live cryptography."""
from copy import deepcopy
import json

import pytest

from examples import crypto_trust_reference as reference
from scripts import check_crypto_trust as checker


def case(index=0):
    d = checker.load()
    return checker.inputs_for(d, d["cases"][index])


def refresh(i, approval=False):
    if approval:
        i["migration"]["approval_binding"] = reference.binding(i)
    i["receipt"] = reference.binding(i)
    return i


def test_authored_cases_and_executed_mutants():
    d = checker.load()
    assert not checker.validate(d, checker.MODEL.read_text())
    result = checker.run_suite(d)
    assert result["success"]
    assert result["mutation_summary"] == dict(killed=9, survived=0, invalid=0)


@pytest.mark.parametrize("index", [n for n in range(28) if n not in [6, 14, 19]])
def test_dependency_order_does_not_change_admission(index):
    i = case(index)
    expected = reference.permitted(checker.premises(i))
    i["dependencies"].reverse()
    refresh(i, i["migration"]["requested"] and i["migration"]["approved"]
            and index not in [14])
    result = reference.exercise(i)
    assert result["candidate_premises"] == checker.premises(i)
    assert (result["release"] is not None) == expected


def test_ancestor_compromise_cannot_be_hidden_behind_valid_leaf():
    i = case()
    i["dependencies"][2]["parents"] = ["control-root"]
    i["dependencies"][0]["status"] = "compromised"
    i["profile"]["components"] = i["policy"]["required_components"] = ["recovery-root"]
    refresh(i)
    assert reference.exercise(i)["release"] is None


def test_duplicate_identity_and_missing_recovery_issuer_are_not_admitted():
    for i in [case(), case(12)]:
        i["dependencies"].append(deepcopy(i["dependencies"][0]))
        refresh(i, True)
        assert reference.exercise(i)["release"] is None
    i = case(12)
    i["dependencies"][2]["parents"] = ["absent-root"]
    refresh(i, True)
    assert reference.exercise(i)["release"] is None


def test_late_policy_epoch_or_artifact_change_invalidates_cached_admission():
    for field in ["epoch", "payload", "target", "floor"]:
        i = case()
        assert reference.exercise(i)["release"] is not None
        if field == "epoch":
            i["policy"]["epoch"] += 1
        elif field == "floor":
            i["minimum_epoch"] += 1
        else:
            i["operation"][field] += "-changed"
        assert reference.exercise(i)["release"] is None


def test_rotation_to_another_key_in_affected_family_does_not_restore_trust():
    i = case(12)
    i["dependencies"][2]["family"] = "family-A"
    refresh(i, True)
    assert reference.exercise(i)["release"] is None


def test_recovery_approval_does_not_cover_another_target():
    i = case(12)
    assert reference.exercise(i)["release"] is not None
    i["operation"]["target"] = "other-target"
    refresh(i)
    assert reference.exercise(i)["release"] is None


def test_recovery_uses_enrolled_path_when_all_old_operational_dependencies_are_lost():
    i = case(12)
    i["dependencies"][0]["status"] = "compromised"
    refresh(i, True)
    assert reference.exercise(i)["release"] is not None
    i["migration"]["requested"] = False
    refresh(i)
    assert reference.exercise(i)["release"] is not None
    i["migration"]["requested"] = True
    i["migration"]["external_enrollment"] = False
    refresh(i, True)
    assert reference.exercise(i)["release"] is None


def test_healthy_recovery_path_cannot_admit_a_poisoned_replacement_control_root():
    i = case(12)
    i["policy"]["control_roots"] = ["control-root"]
    i["dependencies"][0]["status"] = "compromised"
    refresh(i, True)
    assert reference.exercise(i)["release"] is None
    i["policy"]["control_roots"] = []
    refresh(i, True)
    assert reference.exercise(i)["release"] is None


def test_archive_anchor_is_not_a_new_operational_grant():
    i = case(16)
    assert reference.exercise(i)["release"] is not None
    i["operation"]["authorized"] = False
    refresh(i)
    assert reference.exercise(i)["release"] is None


@pytest.mark.parametrize("change", ["digest", "time", "custody", "independence", "family"])
def test_resigning_cannot_repair_missing_history(change):
    i = case(16)
    i["archive"]["resigned"] = True
    if change == "digest":
        i["archive"]["observed_digest"] = "invented"
    elif change == "time":
        i["archive"]["observed_at"] = i["archive"]["earliest_uncertain"]
    elif change == "family":
        i["affected_families"] = ["family-B"]
    else:
        i["archive"]["custody_complete" if change == "custody" else "independent"] = False
    refresh(i)
    assert reference.exercise(i)["release"] is None


def test_no_signature_check_and_no_policy_lifetime_cannot_pass_on_labels():
    i = case()
    i["dependencies"][1]["verified"] = False
    refresh(i)
    assert reference.exercise(i)["release"] is None
    i = case()
    i["policy"]["expires"] = i["clock"]
    refresh(i)
    assert reference.exercise(i)["release"] is None


def test_hold_retains_only_separately_authorized_diagnostics():
    i = case(2)
    capture = reference.exercise(i)
    assert capture["release"] is None
    assert capture["support"] == dict(status="DIAGNOSTIC_ONLY", operation=i["operation"]["id"])
    i["support_authorized"] = False
    assert reference.exercise(i)["support"] is None


def test_advisory_alone_does_not_invalidate_a_current_admission():
    i = case()
    i["advisory"] = "rumor"
    assert reference.exercise(i)["release"] is not None
    i["dependencies"][1]["status"] = "under_review"
    assert reference.exercise(i)["release"] is None


@pytest.mark.parametrize("fault", ["noop", "changed_input", "malformed", "failed_seed", "blanket_denial"])
def test_mutation_credit_cannot_be_manufactured(fault):
    def runner(i, operator=None):
        capture = reference.exercise(i, None if fault == "noop" else operator)
        if operator and fault == "changed_input":
            capture["inputs"]["clock"] += 1
        if operator and fault == "malformed":
            capture["release"] = {"claimed": "success"}
        if not operator and fault in ["failed_seed", "blanket_denial"]:
            capture["support"] = None
            capture["release"] = None
        return capture
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutation_summary"]["killed"] == 0


@pytest.mark.parametrize("drift", ["case", "premise", "input", "mutant", "formal", "map"])
def test_artifact_drift_is_detected(drift):
    d, model, mapping = checker.load(), checker.MODEL.read_text(), json.loads(checker.MAP.read_text())
    if drift == "case":
        d["cases"][0]["expected"]["release"] = False
    elif drift == "premise":
        d["cases"][0]["expected_premises"]["profileApproved"] = False
    elif drift == "input":
        d["cases"][0]["changes"] = [dict(path=["clock"], value="not-a-clock")]
    elif drift == "mutant":
        d["mutants"][0]["operator"] = "invented"
    elif drift == "formal":
        model = model.replace(d["cases"][0]["quint_test"], "absentTest")
    else:
        for prop in mapping["models"][0]["properties"]:
            prop["scenario_tests"] = [n for n in prop["scenario_tests"] if n != d["cases"][0]["quint_test"]]
    errors = checker.validate(d, model, mapping)
    assert errors or not checker.run_suite(d)["success"]
