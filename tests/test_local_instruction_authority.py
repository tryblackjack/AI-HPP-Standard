"""Local instruction origin, config scope and inherited authority regressions."""
import pytest

from examples import local_instruction_reference as reference
from scripts.check_cyber_authority import failed_checks


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
