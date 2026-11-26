"""Agency, consent, exit and mutation-accounting regressions with synthetic data."""
from copy import deepcopy
import json

import pytest

from examples import spiritual_agency_reference as reference
from scripts import check_spiritual_agency as checker


def case(index=0):
    d = checker.load()
    return checker.inputs_for(d, d["cases"][index])


def refresh(i):
    i["receipt"] = reference.binding(i)
    return i


def test_authored_cases_mutants_and_literal_formal_links():
    d = checker.load()
    assert not checker.validate(d, checker.MODEL.read_text())
    report = checker.run_suite(d)
    assert report["success"]
    assert report["mutation_summary"] == dict(killed=6, survived=0, invalid=0)


@pytest.mark.parametrize("worldview", ["neutral", "religious", "secular"])
def test_worldview_label_is_not_a_diagnosis_or_a_permission(worldview):
    i = case()
    i["message"]["worldview"] = worldview
    assert reference.exercise(i)["effect"] is not None
    i["authority"]["task_authorized"] = False
    refresh(i)
    assert reference.exercise(i)["effect"] is None


def test_recording_is_not_training_permission_and_declining_training_keeps_discussion():
    i = case(23)
    assert reference.exercise(i)["effect"] is not None
    i["action"]["kind"] = "train"
    refresh(i)
    assert reference.exercise(i)["effect"] is None
    i["consents"][0]["revoked"] = True
    i["action"]["kind"] = "discuss"
    refresh(i)
    assert reference.exercise(i)["effect"] is not None


def test_leader_or_one_member_cannot_supply_every_persons_consent():
    i = case(12)
    assert reference.exercise(i)["effect"] is None
    grant = deepcopy(i["consents"][0])
    grant["person"] = "person-B"
    i["consents"].append(grant)
    refresh(i)
    assert reference.exercise(i)["effect"] is not None
    i["consents"][1]["voluntary"] = False
    refresh(i)
    assert reference.exercise(i)["effect"] is None


@pytest.mark.parametrize("field", ["purpose", "target", "recipients"])
def test_scope_expansion_requires_its_own_consent(field):
    i = case(23)
    if field == "recipients":
        i["action"]["recipients"] = ["recipient-B"]
    else:
        i["action"][field] = "different-scope"
    refresh(i)
    assert reference.exercise(i)["effect"] is None


def test_verified_exit_revokes_future_session_use_without_revoking_unrelated_work():
    i = case(20)
    other = deepcopy(i["consents"][0])
    other["target"] = "another-session"
    i["consents"].append(other)
    captured = reference.exercise(i)
    assert captured["effect"]["kind"] == "exit"
    assert not captured["state"]["session"]["active"]
    assert captured["state"]["consents"][0]["revoked"]
    assert not captured["state"]["consents"][1]["revoked"]
    i.update(captured["state"])
    i["action"]["kind"] = "train"
    i["authority"]["task_authorized"] = True
    i["message"]["threaten_leaving"] = False
    i["controls"]["exit_available"] = i["controls"]["challenge_available"] = True
    refresh(i)
    assert reference.exercise(i)["effect"] is None


def test_repeated_verified_exit_is_idempotent():
    i = case(20)
    first = reference.exercise(i)
    i.update(first["state"])
    second = reference.exercise(i)
    assert second["state"] == first["state"]


@pytest.mark.parametrize("fault", ["identity", "target", "person"])
def test_ordinary_task_grant_cannot_authorize_another_persons_exit(fault):
    i = case()
    i["action"]["kind"] = "exit"
    if fault == "identity":
        i["authority"]["self_exit_verified"] = False
    elif fault == "target":
        i["action"]["target"] = "another-session"
    else:
        i["action"]["persons"] = ["person-B"]
    refresh(i)
    captured = reference.exercise(i)
    assert captured["effect"] is None
    assert captured["state"]["session"]["active"]


def test_reviewed_fresh_consent_restores_only_the_approved_operation():
    i = case(9)
    i["session"]["revision"] += 1
    i["consents"][0]["revoked"] = True
    refresh(i)
    assert reference.exercise(i)["effect"] is None
    i["consents"][0].update(revoked=False, revision=i["session"]["revision"])
    refresh(i)
    assert reference.exercise(i)["effect"] is not None
    i["action"]["kind"] = "share"
    refresh(i)
    assert reference.exercise(i)["effect"] is None


@pytest.mark.parametrize("flag", ["model_infallibility", "shame_dissent", "threaten_leaving", "isolate_support", "exploit_vulnerability"])
def test_explicit_data_consent_cannot_override_coercion(flag):
    i = case(9)
    i["message"][flag] = True
    refresh(i)
    assert reference.exercise(i)["effect"] is None


@pytest.mark.parametrize("flag", ["exit_available", "challenge_available", "review_authorized", "review_independent", "review_can_inspect"])
def test_required_effective_control_is_not_a_checkbox(flag):
    i = case(16)
    i["controls"][flag] = False
    refresh(i)
    assert reference.exercise(i)["effect"] is None


def test_audit_is_minimal_and_does_not_store_beliefs_or_conversation():
    i = case(1)
    assert reference.exercise(i)["audit"] == dict(target="session-A", allowed=True)
    i["action"]["kind"] = "record"
    i["data_minimized"] = False
    refresh(i)
    assert reference.exercise(i)["effect"] is None


def test_unknown_action_cannot_default_to_discussion():
    i = refresh(dict(case(), action=dict(case()["action"], kind="invented")))
    assert reference.exercise(i)["effect"] is None


@pytest.mark.parametrize("fault", ["noop", "changed_input", "malformed_effect", "malformed_state", "bad_seed", "blanket_denial"])
def test_mutant_credit_requires_an_observed_valid_trial(fault):
    def runner(i, operator=None):
        capture = reference.exercise(i, None if fault == "noop" else operator)
        if operator and fault == "changed_input":
            capture["inputs"]["clock"] += 1
        if operator and fault == "malformed_effect":
            capture["effect"] = {"claimed": "success"}
        if operator and fault == "malformed_state":
            capture["state"] = {}
        if not operator and fault == "bad_seed":
            capture["state"] = {}
        if not operator and fault == "blanket_denial":
            capture["effect"] = None
            capture["audit"]["allowed"] = False
        return capture
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutation_summary"]["killed"] == 0


@pytest.mark.parametrize("drift", ["input", "expected", "predicate", "formal", "map", "pair", "mutant"])
def test_contract_or_formal_drift_cannot_silently_pass(drift):
    d, model, mapping = checker.load(), checker.MODEL.read_text(), json.loads(checker.MAP.read_text())
    if drift == "input":
        d["cases"][0]["changes"] = [dict(path=["clock"], value="not-a-clock")]
    elif drift == "expected":
        d["cases"][0]["expected_allowed"] = False
    elif drift == "predicate":
        d["cases"][0]["expected_predicates"]["consent"] = False
    elif drift == "formal":
        model = model.replace(d["cases"][0]["quint_test"], "absentTest")
    elif drift == "map":
        for entry in mapping["models"]:
            for p in entry["properties"]:
                p["scenario_tests"] = [n for n in p["scenario_tests"] if n != d["cases"][0]["quint_test"]]
    elif drift == "pair":
        d["pairs"][0] = ["SAG-T01", "SAG-T04"]
    else:
        d["mutants"][0]["operator"] = "invented"
    assert checker.validate(d, model, mapping) or not checker.run_suite(d)["success"]
