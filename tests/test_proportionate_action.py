"""Reject drift between optional PAS contracts, portable fixtures and Quint."""
from copy import deepcopy

import jsonschema
import pytest

from scripts import check_proportionate_action_profile as checker


def artifacts():
    return (checker.load(checker.VECTORS),
            (checker.ROOT / checker.PROFILE).read_text(encoding="utf-8"),
            (checker.ROOT / checker.MODEL).read_text(encoding="utf-8"))


def test_portable_contract_is_synchronized():
    jsonschema.Draft202012Validator.check_schema(checker.load(checker.SCHEMA))
    assert checker.validate(*artifacts()) == []


@pytest.mark.parametrize("change", ["omit_case", "duplicate_case", "omit_fact", "wrong_outcome",
                                   "wrong_predicate", "imagined_test", "omit_mutant"])
def test_corrupt_portable_contract_is_rejected(change):
    document, profile, model = artifacts()
    if change == "omit_case":
        document["cases"].pop()
    elif change == "duplicate_case":
        document["cases"][-1] = deepcopy(document["cases"][0])
    elif change == "omit_fact":
        document["cases"][0]["proposal"].pop("grantCurrent")
    elif change == "wrong_outcome":
        document["cases"][0]["expected_outcome"] = "block"
    elif change == "wrong_predicate":
        document["cases"][0]["predicate_ids"] = ["PAS-P99"]
    elif change == "imagined_test":
        document["cases"][0]["quint_test"] = "pasImaginedTest"
    elif change == "omit_mutant":
        document["mutants"].pop()
    assert checker.validate(document, profile, model)


def test_changing_core_input_without_updating_fixture_is_rejected():
    document, profile, model = artifacts()
    block = checker.render_case(document["cases"][0])
    changed = block.replace("grantCurrent: true", "grantCurrent: false")
    assert any("differs from executable" in error for error in checker.validate(
        document, profile, model.replace(block, changed)
    ))


def test_kill_witness_must_assert_actual_named_invariant():
    document, profile, model = artifacts()
    model = model.replace("check(not(interventionPreservesObjective))", "check(true)")
    assert any("missing executable kill" in error for error in checker.validate(
        document, profile, model
    ))


def test_unsafe_operator_cannot_join_normal_transition_relation():
    document, profile, model = artifacts()
    model = model.replace("      recordTaskAcceptance,", "      mutantPasSelfAppointedMission,")
    assert "unsafe operator admitted to normal step" in checker.validate(document, profile, model)


def test_orphaned_mutant_cannot_be_hidden():
    document, profile, model = artifacts()
    model = model.replace("  action mutantPasSelfAppointedMission:", "  action mutantPasOrphan:")
    assert "unsafe operator inventory mismatch" in checker.validate(document, profile, model)


def test_formal_trace_link_cannot_be_silently_reassigned(monkeypatch):
    document, profile, model = artifacts()
    load = checker.load
    formal_map = load("data/formal-assurance-map.json")
    prop = next(p for p in formal_map["models"][0]["properties"]
                if p["invariant"] == "interventionPreservesObjective")
    prop["predicate_ids"] = ["PAS-P02"]
    monkeypatch.setattr(checker, "load", lambda path: formal_map if path.endswith("map.json") else load(path))
    assert any("formal map link mismatch" in error for error in checker.validate(document, profile, model))
