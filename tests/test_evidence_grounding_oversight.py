"""Reject evidence/oversight contract drift and vacuous mutation witnesses."""
from copy import deepcopy

import jsonschema
import pytest

from scripts import check_evidence_grounding_oversight_profile as checker


def artifacts():
    return (checker.load(checker.VECTORS),
            (checker.ROOT / checker.PROFILE).read_text(encoding="utf-8"),
            (checker.ROOT / checker.MODEL).read_text(encoding="utf-8"))


def test_reference_contract_is_synchronized():
    jsonschema.Draft202012Validator.check_schema(checker.load(checker.SCHEMA))
    assert checker.validate(*artifacts()) == []


@pytest.mark.parametrize("change", ["omit_case", "duplicate_case", "omit_freshness",
                                   "wrong_reason", "receipt_as_resolution", "wrong_predicate",
                                   "unknown_event", "omit_mutant"])
def test_corrupt_portable_contract_is_rejected(change):
    document, profile, model = artifacts()
    if change == "omit_case":
        document["cases"].pop()
    elif change == "duplicate_case":
        document["cases"][-1] = deepcopy(document["cases"][0])
    elif change == "omit_freshness":
        document["cases"][3]["steps"][0]["facts"].pop("observationsCurrent")
    elif change == "wrong_reason":
        document["cases"][2]["expected"]["reason"] = "contradicted"
    elif change == "receipt_as_resolution":
        document["cases"][15]["expected"]["stage"] = 6
    elif change == "wrong_predicate":
        document["cases"][0]["predicate_ids"] = ["EGO-P99"]
    elif change == "unknown_event":
        document["cases"][0]["steps"][0]["event"] = "override_objection"
    elif change == "omit_mutant":
        document["mutants"].pop()
    assert checker.validate(document, profile, model)


def test_stale_observation_fixture_cannot_silently_become_current():
    document, profile, model = artifacts()
    block = checker.render_case(document["cases"][3])
    changed = block.replace("observationsCurrent: false", "observationsCurrent: true")
    assert changed != block
    assert any("differs from executable" in error for error in checker.validate(
        document, profile, model.replace(block, changed)
    ))


def test_mutant_requires_successful_safe_seed():
    document, profile, model = artifacts()
    model = model.replace(".then(check(all { allCoreInvariants, s.oversight.stage == 3 }))",
                          ".then(check(true))")
    assert any("seed or kill witness differs" in error for error in checker.validate(document, profile, model))


def test_mutant_requires_named_invariant_failure():
    document, profile, model = artifacts()
    model = model.replace("check(not(oversightStagesHaveEvidence))", "check(true)")
    assert any("missing executable kill" in error for error in checker.validate(document, profile, model))


def test_unsafe_operator_cannot_enter_normal_transition_relation():
    document, profile, model = artifacts()
    model = model.replace("      queueOversightNotice,", "      mutantEgoLeaderVeto,")
    assert "unsafe operator admitted to normal step" in checker.validate(document, profile, model)


def test_witness_inventory_cannot_hide_an_orphan():
    document, profile, model = artifacts()
    model = model.replace("  action mutantEgoLeaderVeto:", "  action mutantEgoOrphan:")
    assert "unsafe operator inventory mismatch" in checker.validate(document, profile, model)


def test_formal_link_cannot_point_at_another_predicate(monkeypatch):
    document, profile, model = artifacts()
    load = checker.load
    mapping = load("data/formal-assurance-map.json")
    prop = next(p for p in mapping["models"][0]["properties"]
                if p["invariant"] == "oversightStagesHaveEvidence")
    prop["predicate_ids"] = ["EGO-P01"]
    monkeypatch.setattr(checker, "load", lambda path: mapping if path.endswith("map.json") else load(path))
    assert any("formal map link mismatch" in error for error in checker.validate(document, profile, model))
