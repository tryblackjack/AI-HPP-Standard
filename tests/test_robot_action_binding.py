"""Reject robot fixture drift, missing execution checks and vacuous mutant kills."""
from copy import deepcopy

import jsonschema
import pytest

from scripts import check_robot_action_binding_profile as checker


def artifacts():
    return (checker.load(checker.VECTORS),
            (checker.ROOT / checker.PROFILE).read_text(encoding="utf-8"),
            (checker.ROOT / checker.MODEL).read_text(encoding="utf-8"))


def test_reference_contract_is_synchronized():
    jsonschema.Draft202012Validator.check_schema(checker.load(checker.SCHEMA))
    assert checker.validate(*artifacts()) == []


@pytest.mark.parametrize("change", ["omit_case", "duplicate_case", "omit_observation",
                                   "wrong_outcome", "wrong_predicate", "skip_execution",
                                   "unknown_event", "omit_mutant"])
def test_corrupt_portable_contract_is_rejected(change):
    document, profile, model = artifacts()
    if change == "omit_case":
        document["cases"].pop()
    elif change == "duplicate_case":
        document["cases"][-1] = deepcopy(document["cases"][0])
    elif change == "omit_observation":
        document["cases"][8]["steps"][0].pop("contextFresh")
    elif change == "wrong_outcome":
        document["cases"][0]["expected_outcome"] = "block"
    elif change == "wrong_predicate":
        document["cases"][0]["predicate_ids"] = ["RAB-P99"]
    elif change == "skip_execution":
        document["cases"][0]["steps"].pop()
    elif change == "unknown_event":
        document["cases"][0]["steps"][0]["action"] = "execute_without_gate"
    elif change == "omit_mutant":
        document["mutants"].pop()
    assert checker.validate(document, profile, model)


def test_changing_observation_without_changing_fixture_is_rejected():
    document, profile, model = artifacts()
    block = checker.render_case(document["cases"][8])
    changed = block.replace("changeRobotContext(false, false", "changeRobotContext(false, true")
    assert changed != block
    assert any("differs from executable" in error for error in checker.validate(
        document, profile, model.replace(block, changed)
    ))


def test_mutant_requires_successful_safe_seed():
    document, profile, model = artifacts()
    model = model.replace(".then(check(all { s.robot.audit.executed, allCoreInvariants }))",
                          ".then(check(true))")
    assert any("seed or kill witness differs" in error for error in checker.validate(document, profile, model))


def test_mutant_requires_named_invariant_failure():
    document, profile, model = artifacts()
    model = model.replace("check(not(robotExecutionUsesCurrentContext))", "check(true)")
    assert any("missing executable kill" in error for error in checker.validate(document, profile, model))


def test_unsafe_operator_cannot_enter_normal_transition_relation():
    document, profile, model = artifacts()
    model = model.replace("      assessRobotAction,", "      mutantRabTargetSubstitution,")
    assert "unsafe operator admitted to normal step" in checker.validate(document, profile, model)


def test_witness_inventory_cannot_hide_an_orphan():
    document, profile, model = artifacts()
    model = model.replace("  action mutantRabTargetSubstitution:", "  action mutantRabOrphan:")
    assert "unsafe operator inventory mismatch" in checker.validate(document, profile, model)


def test_formal_link_cannot_point_at_another_predicate(monkeypatch):
    document, profile, model = artifacts()
    load = checker.load
    mapping = load("data/formal-assurance-map.json")
    prop = next(p for p in mapping["models"][0]["properties"]
                if p["invariant"] == "robotExecutionUsesCurrentContext")
    prop["predicate_ids"] = ["RAB-P01"]
    monkeypatch.setattr(checker, "load", lambda path: mapping if path.endswith("map.json") else load(path))
    assert any("formal map link mismatch" in error for error in checker.validate(document, profile, model))
