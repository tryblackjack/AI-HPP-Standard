"""Inspect temporary storage outcomes independently of candidate admission logic."""
from copy import deepcopy

import pytest

from examples import memory_admission_reference as reference


def failures(capture):
    i, before, after, receipt = (capture[k] for k in ("inputs", "before", "after", "receipt"))
    p, src = i["proposal"], i["proposal"]["source"]
    changed = after != before
    writing = changed and after is not None
    result = []
    if writing and (not after["source"]["id"] or after["source"] != src
                    or after["content"] != p["content"]
                    or src["content_digest"] != reference.digest(after["content"])):
        result.append("PM-P01")
    if writing and (after["classification"] != src["evidence_class"] or (
            src["risk"] == "risky_narrative" and after["classification"] == "verified")):
        result.append("PM-P02")
    in_scope = (i["authorized"] and p["tenant"] == i["tenant"] and bool(p["uses"])
                and all(u in src["permitted_uses"] for u in p["uses"])
                and i["clock"] < src["expires"])
    if changed and not in_scope:
        result.append("PM-P03")
    if changed and (i["expected_revision"] != before["revision"] or (
            after is not None and after["revision"] != before["revision"] + 1)):
        result.append("PM-P04")
    bound = (receipt["operation"] == i["operation"] and receipt["key"] == p["key"]
             and receipt["tenant"] == i["tenant"]
             and receipt["before_digest"] == reference.digest(before)
             and receipt["after_digest"] == reference.digest(after))
    if not bound or (receipt["status"] == "APPLIED") != changed or (changed and i["storage_failure"]):
        result.append("PM-P05")
    return result


EXPECTED = {
    "verified_fact": "APPLIED", "attributed_inference": "APPLIED", "risky_report": "APPLIED",
    "missing_provenance": "HELD", "sensitive_out_of_purpose": "HELD", "wrong_tenant": "HELD",
    "stale_revision": "HELD", "write_failure": "FAILED", "delete_failure": "FAILED",
    "confirmed_delete": "APPLIED", "confirmed_correction": "APPLIED", "expired_source": "HELD",
    "unverified_fact": "HELD", "revoked_write": "HELD",
}
MUTANTS = (
    ("verified_fact", "erase_provenance", "PM-P01"),
    ("attributed_inference", "promote_inference", "PM-P02"),
    ("sensitive_out_of_purpose", "ignore_scope", "PM-P03"),
    ("stale_revision", "ignore_revision", "PM-P04"),
    ("write_failure", "false_ack", "PM-P05"),
)


@pytest.mark.parametrize("case", reference.CASES)
def test_recorded_outcome_matches_frozen_case_expectation(case):
    inputs = reference.fixture(case)
    capture = reference.exercise(inputs)
    assert capture["inputs"] == inputs
    assert capture["receipt"]["status"] == EXPECTED[case]
    assert failures(capture) == []
    if EXPECTED[case] == "APPLIED":
        if inputs["operation"] == "delete":
            assert capture["after"] is None
        else:
            assert capture["after"] == inputs["proposal"]
    else:
        assert capture["after"] == capture["before"]


def killed(case, operator, predicate, runner=reference.exercise):
    inputs = reference.fixture(case)
    baseline = runner(inputs)
    mutant = runner(inputs, operator)
    return (baseline["receipt"]["status"] == EXPECTED[case] and not failures(baseline)
            and baseline["inputs"] == mutant["inputs"] == inputs
            and baseline != mutant and predicate in failures(mutant))


@pytest.mark.parametrize("case,operator,predicate", MUTANTS)
def test_executed_mutant_changes_storage_or_receipt_with_same_inputs(case, operator, predicate):
    assert killed(case, operator, predicate)


@pytest.mark.parametrize("case,operator,predicate", MUTANTS)
def test_no_op_mutant_cannot_count_as_a_kill(case, operator, predicate):
    assert not killed(case, operator, predicate, lambda inputs, _=None: reference.exercise(inputs))


def test_blanket_denial_does_not_pass_useful_cases():
    capture = reference.exercise(reference.fixture("attributed_inference"), deny_all=True)
    assert capture["receipt"]["status"] != EXPECTED["attributed_inference"]


@pytest.mark.parametrize("field,value", [("key", "different-item"), ("tenant", "different-user"),
                                       ("operation", "delete"), ("after_digest", "unbound")])
def test_receipt_cannot_be_reused_for_another_effect(field, value):
    capture = reference.exercise(reference.fixture("verified_fact"))
    capture["receipt"][field] = value
    assert "PM-P05" in failures(capture)


def test_retrieved_old_copy_cannot_undo_current_correction_or_deletion():
    for case in ("confirmed_correction", "confirmed_delete"):
        inputs = reference.fixture(case)
        capture = reference.exercise(inputs)
        attempted = deepcopy(inputs)
        attempted["operation"] = "write"
        attempted["current_revision"] = capture["before"]["revision"] + 1
        assert reference.exercise(attempted)["receipt"]["status"] == "HELD"


def test_risky_narrative_stays_attributed_and_never_becomes_verified_fact():
    inputs = reference.fixture("risky_report")
    assert reference.exercise(inputs)["after"]["classification"] == "user_report"
    inputs["proposal"]["classification"] = "verified"
    assert reference.exercise(inputs)["receipt"]["status"] == "HELD"
