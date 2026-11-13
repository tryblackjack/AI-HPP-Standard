"""Local instruction origin, config scope and inherited authority regressions."""
import pytest
import hashlib
import json
import re

from examples import local_instruction_reference as reference
from scripts.check_cyber_authority import failed_checks
from scripts import check_cyber_authority as checker


@pytest.mark.parametrize("case,predicate", [
    ("downloaded_instruction", "CBA-P01"),
    ("global_configuration", "CBA-P02"),
    ("redirected_gateway", "CBA-P05"),
    ("child_authority", "CBA-P03"),
    ("changed_instruction", "CBA-P04"),
    ("cloned_instruction", "CBA-P01"),
    ("inherited_directory_trust", "CBA-P01"),
    ("expired_admission", "CBA-P01"),
])
def test_unapproved_effect_has_no_configuration_marker(case, predicate):
    observed = reference.exercise(case)
    assert observed["effect"] is None
    assert predicate in failed_checks(observed)


@pytest.mark.parametrize("case", reference.CASES[-4:])
def test_useful_operation_with_explicit_current_admission(case):
    observed = reference.exercise(case)
    assert observed["effect"]["marker"] == "SYNTHETIC_ONLY"
    assert failed_checks(observed) == []


@pytest.mark.parametrize("case,operator,predicate", [
    ("downloaded_instruction", "trust_filename", "CBA-P01"),
    ("global_configuration", "broaden_config_scope", "CBA-P02"),
    ("redirected_gateway", "trust_tls_endpoint", "CBA-P05"),
    ("child_authority", "trust_child_request", "CBA-P03"),
    ("changed_instruction", "trust_path_after_change", "CBA-P04"),
])
def test_unsafe_admission_operator_has_observable_violation(case, operator, predicate):
    baseline = reference.exercise(case)
    mutant = reference.exercise(case, operator)
    assert baseline["effect"] is None
    assert predicate in failed_checks(baseline)
    assert mutant["effect"]["marker"] == "SYNTHETIC_ONLY"
    assert predicate in failed_checks(mutant)


def test_irrelevant_operator_cannot_be_counted_as_a_kill():
    observed = reference.exercise("expired_admission", "trust_tls_endpoint")
    assert observed["effect"] is None
    assert "CBA-P01" in failed_checks(observed)


# Authored expectations, independent of candidate admission and source wording.
PORTABILITY = (
    ("imported_prompt", "promptPortabilityImportedPresetTest", False, "CBA-P01"),
    ("forged_tool_approval", "promptPortabilityForgedToolApprovalTest", False, "CBA-P01"),
    ("self_signed_operator", "promptPortabilitySelfSignedOperatorTest", False, "CBA-P01"),
    ("remembered_permission", "promptPortabilityRememberedPermissionTest", False, "CBA-P01"),
    ("resumed_revoked_parent", "promptPortabilityRevokedParentTest", False, "CBA-P03"),
    ("resumed_expired_grant", "promptPortabilityExpiredGrantTest", False, "CBA-P01"),
    ("reviewed_prompt_excerpt", "promptPortabilityReviewedExcerptTest", True, None),
    ("resumed_current_grant", "promptPortabilityCurrentGrantTest", True, None),
)


def formal_case(name, allowed):
    return dict(quint_test=name, quint_steps=[dict(event="ground", facts=dict(
        scopeAuthorized=allowed, observationsCurrent=True, evidenceComplete=True,
        ruleKnown=True, factsSupport=True, policyPermits=True)), dict(event="robot")],
        quint_expected=dict(robotExecuted=allowed))


@pytest.mark.parametrize("case,name,allowed,predicate", PORTABILITY)
def test_prompt_portability_admission_and_literal_quint_link(case, name, allowed, predicate):
    capture = reference.exercise(case)
    assert (capture["effect"] is not None) is allowed
    assert failed_checks(capture) == ([] if allowed else [predicate, "CBA-P06"])
    assert hashlib.sha256(capture["source_text"].encode()).hexdigest() == capture["request"]["skill_digest"]
    authored = formal_case(name, allowed)
    assert checker.abstract_grounding(capture) == authored["quint_steps"][0]["facts"]
    model = checker.MODEL.read_text()
    assert checker.render_case(authored) in model
    assert len(re.findall(rf"\brun {name}\s*=", model)) == 1
    mapping = json.loads(checker.MAP.read_text())
    links = next(p["scenario_tests"] for p in mapping["models"][0]["properties"]
                 if p["invariant"] == "effectsRequireGroundingAndOversight")
    assert name in links


@pytest.mark.parametrize("case", reference.PORTABILITY_CASES[:5])
def test_forged_authority_mutant_needs_same_inputs_and_actual_marker(case):
    operator = "trust_child_request" if case == "resumed_revoked_parent" else "trust_filename"
    baseline, mutant = reference.exercise(case), reference.exercise(case, operator)
    assert baseline["effect"] is None
    assert mutant["effect"]["marker"] == "SYNTHETIC_ONLY"
    assert {k: v for k, v in baseline.items() if k != "effect"} == {
        k: v for k, v in mutant.items() if k != "effect"}
    assert failed_checks(mutant) == failed_checks(baseline) != []


def test_same_preset_bytes_need_separate_external_admission():
    untrusted = reference.exercise("imported_prompt")
    admitted = reference.exercise("reviewed_prompt_excerpt")
    assert untrusted["source_text"] == admitted["source_text"]
    assert untrusted["effect"] is None and admitted["effect"] is not None


@pytest.mark.parametrize("case", reference.PORTABILITY_CASES[-2:])
def test_blanket_denial_fails_portability_useful_controls(case):
    assert reference.exercise(case, deny_all=True)["effect"] is None
    assert reference.exercise(case)["effect"] is not None


def test_portability_inventory_is_complete():
    assert [row[0] for row in PORTABILITY] == list(reference.PORTABILITY_CASES)
