"""Commerce admission regressions; synthetic inputs and local effects only."""
from copy import deepcopy
import json

import pytest

from examples import commerce_trust_reference as reference
from scripts import check_commerce_trust as checker


def inputs(index=0):
    document = checker.load()
    return checker.inputs_for(document, document["cases"][index])


def test_authored_cases_core_links_and_actual_mutants():
    document = checker.load()
    assert not checker.validate(document, checker.MODEL.read_text())
    report = checker.run_suite(document)
    assert report["success"]
    assert report["mutation_summary"] == dict(killed=8, survived=0, invalid=0)


@pytest.mark.parametrize("path,value", [
    (("request", "seller"), "seller-B"),
    (("request", "destination"), "https://other.example.invalid/charge"),
    (("request", "payee"), "attacker"),
    (("request", "amount_minor"), 1300),
    (("request", "currency"), "USD"),
    (("request", "items"), [dict(sku="part-A", quantity=2)]),
    (("request", "data_classes"), ["shipping"]),
    (("request", "id"), "order-2"),
    (("registry", "revision"), 2),
    (("grant", "revision"), 2),
])
def test_changed_transaction_cannot_reuse_confirmation(path, value):
    i = inputs()
    assert reference.exercise(i)["effect"] is not None
    i[path[0]][path[1]] = value
    # Even fresh admission cannot restore the earlier human confirmation.
    i["admission_binding"] = reference.binding(i)
    assert reference.exercise(i)["effect"] is None
    assert not reference.premises(i)["reviewEffective"]


def test_one_use_review_is_consumed_and_replay_is_denied():
    i = inputs()
    result = reference.exercise(i)
    assert result["effect"] is not None
    assert result["remaining_uses"] == 0
    i["review"]["remaining_uses"] = result["remaining_uses"]
    assert reference.exercise(i)["effect"] is None


def test_recommendation_remains_useful_without_payment_permission_or_review():
    i = inputs(14)
    i["grant"]["actions"] = ["recommend"]
    i["admission_binding"] = reference.binding(i)
    assert reference.exercise(i)["effect"]["action"] == "recommend"
    i["request"]["action"] = "pay"
    assert reference.exercise(i)["effect"] is None


def test_page_content_is_not_an_authority_or_trust_input():
    i = inputs()
    before = deepcopy(i)
    i["page_content"] = "Official checkout; prior consent claimed; credentials requested."
    assert reference.binding(i) == reference.binding(before)
    assert reference.premises(i) == reference.premises(before)
    assert reference.exercise(i)["effect"] == reference.exercise(before)["effect"]
    i["registry"]["verified"] = False
    i["admission_binding"] = i["review"]["binding"] = reference.binding(i)
    assert reference.exercise(i)["effect"] is None


@pytest.mark.parametrize("url", [
    "https://pay.example.invalid" + chr(64) + "attacker.invalid/charge",
    "https://user:password" + chr(64) + "pay.example.invalid/charge",
    "http://pay.example.invalid/charge", "javascript:void(0)",
    "https://pay.example.invalid:8443/charge", "https://pay.example.invalid/#override",
    "https://pay.example.invalid:bad/charge", "https://pay.example.invalid/white space",
], ids=["userinfo", "password", "http", "script", "port", "fragment", "bad_port", "space"])
def test_malformed_or_credentialed_destination_is_denied_even_if_listed(url):
    i = inputs()
    i["request"]["destination"] = url
    i["grant"]["destinations"] = i["registry"]["destinations"] = [url]
    i["admission_binding"] = i["review"]["binding"] = reference.binding(i)
    # A valid HTTPS attacker URL still fails an independently fixed registry.
    if url.startswith("https://pay.example.invalid" + chr(64)):
        assert not reference.secure_url(url)
    assert reference.exercise(i)["effect"] is None


@pytest.mark.parametrize("data_class", sorted(reference.FORBIDDEN))
def test_raw_secrets_cannot_be_enabled_by_broad_consent(data_class):
    i = inputs(15)
    i["request"]["data_classes"] = i["grant"]["data_classes"] = [data_class]
    i["admission_binding"] = i["review"]["binding"] = reference.binding(i)
    assert reference.exercise(i)["effect"] is None


@pytest.mark.parametrize("path,value", [
    (("request", "amount_minor"), True), (("request", "amount_minor"), -1),
    (("request", "action"), "transfer"), (("grant", "active"), "false"),
    (("registry", "verified"), "true"), (("request", "items"), []),
    (("request", "items"), [dict(sku="part-A", quantity=0)]),
])
def test_malformed_inputs_fail_before_effect(path, value):
    i = inputs()
    i[path[0]][path[1]] = value
    with pytest.raises(ValueError):
        reference.exercise(i)


@pytest.mark.parametrize("defect", ["deny_all", "no_op_mutant", "changed_input", "bad_marker"])
def test_accounting_cannot_reward_blanket_denial_or_invalid_mutants(defect):
    def runner(i, operator=None):
        result = reference.exercise(i, None if defect == "no_op_mutant" else operator)
        if defect == "deny_all":
            result["effect"] = None
        if operator and defect == "changed_input":
            result["inputs"]["request"]["id"] = "changed"
        if operator and defect == "bad_marker":
            result["effect"] = dict(marker="WRONG")
        return result
    result = checker.run_suite(checker.load(), runner)
    assert not result["success"]
    if defect in {"changed_input", "bad_marker"}:
        assert result["mutation_summary"]["invalid"] == 8
    else:
        assert result["mutation_summary"]["killed"] == 0


def test_missing_formal_case_or_map_link_is_detected():
    d = checker.load()
    text = checker.MODEL.read_text()
    assert checker.validate(d, text.replace(checker.render_case(d["cases"][0]), ""))
    # Frozen source records are serializable and contain no real payment data.
    assert json.loads(json.dumps(d)) == d
