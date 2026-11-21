"""Independent report-support checks, real temporary effects and mutation controls."""
from copy import deepcopy
import json

import pytest

from examples import claim_evidence_reference as reference
from scripts import check_claim_evidence as checker


def test_all_cases_mutants_and_literal_quint_links():
    document = checker.load()
    assert checker.validate(document, checker.MODEL.read_text()) == []
    report = checker.run_suite(document)
    assert report["success"]
    assert len(report["cases"]) == 25
    assert report["mutation_summary"] == dict(declared=9, killed=9, survived=0,
        invalid=0, denominator=9, score=1)


@pytest.mark.parametrize("index", range(9))
def test_mutants_need_an_actual_release_under_the_same_inputs(index):
    document = checker.load()
    mutant = document["mutants"][index]
    case = next(c for c in document["cases"] if c["id"] == mutant["case_id"])
    inputs = checker.inputs_for(document, case)
    baseline = reference.exercise(inputs)
    unsafe = reference.exercise(inputs, mutant["operator"])
    assert baseline["inputs"] == unsafe["inputs"] == inputs
    assert baseline["release"] is None
    assert unsafe["release"] is not None
    assert mutant["predicate_id"] in checker.failures(inputs)


def test_no_op_mutants_survive():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None: reference.exercise(inputs))
    assert not report["success"]
    assert report["mutation_summary"]["survived"] == 9


def test_invalid_trials_are_not_kills():
    def runner(inputs, operator=None):
        if operator:
            raise OSError("synthetic unavailable fixture")
        return reference.exercise(inputs)
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutation_summary"]["invalid"] == 9
    assert report["mutation_summary"]["denominator"] == 0
    assert report["mutation_summary"]["score"] is None


def test_failed_safe_seed_invalidates_mutation_credit():
    def runner(inputs, operator=None):
        if operator is None:
            raise ValueError("missing baseline")
        return reference.exercise(inputs, operator)
    report = checker.run_suite(checker.load(), runner)
    assert all(m["result"] == "INVALID" for m in report["mutants"])


def test_mutant_cannot_change_source_or_report_to_earn_credit():
    def runner(inputs, operator=None):
        observed = reference.exercise(inputs, operator)
        if operator:
            observed["inputs"]["context"] += 1
        return observed
    report = checker.run_suite(checker.load(), runner)
    assert report["mutation_summary"]["invalid"] == 9
    assert report["mutation_summary"]["killed"] == 0


def test_blanket_denial_fails_useful_release_and_draft_controls():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None:
                               reference.exercise(inputs, operator, deny_all=True))
    assert not report["success"]
    assert all(c["result"] == "FAIL" for c in report["cases"])


@pytest.mark.parametrize("pair", [[0, 18], [9, 10]])
def test_format_pairs_change_only_format_and_preserve_decisions(pair):
    document = checker.load()
    a, b = [checker.inputs_for(document, document["cases"][i]) for i in pair]
    assert a["report"].pop("format") != b["report"].pop("format")
    assert a == b
    outcomes = [reference.exercise(checker.inputs_for(document, document["cases"][i])) for i in pair]
    assert (outcomes[0]["release"] is None) == (outcomes[1]["release"] is None)


def test_signature_or_digest_identity_cannot_establish_claim_support():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][0])
    assert all(s["admitted_digest"] == reference.digest(reference.source_body(s)) for s in inputs["sources"])
    assert inputs["review"]["approved"]
    assert reference.exercise(inputs)["release"] is None


def test_source_count_does_not_replace_ancestry_independence():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][2])
    assert all(len(c["evidence"]) == 2 for c in inputs["report"]["claims"])
    observed = reference.exercise(inputs)
    assert not observed["candidate_premises"]["independenceVerified"]
    assert observed["release"] is None


def test_same_generation_path_cannot_review_itself_under_an_alias():
    document = checker.load()
    observed = reference.exercise(checker.inputs_for(document, document["cases"][12]))
    assert observed["inputs"]["report"]["author"] != observed["inputs"]["review"]["actor"]
    assert observed["release"] is None


def test_fresh_authorized_review_restores_work_under_same_grant():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][6])
    held = reference.exercise(inputs)
    assert held["release"] is None and held["draft"] is not None
    inputs["review"]["binding"] = reference.bundle_binding(inputs)
    resumed = reference.exercise(inputs)
    assert resumed["release"] is not None
    assert resumed["inputs"]["authority"] == held["inputs"]["authority"]


@pytest.mark.parametrize("index", [0, 5, 8, 17])
def test_missing_support_or_release_authority_does_not_remove_safe_local_drafting(index):
    document = checker.load()
    observed = reference.exercise(checker.inputs_for(document, document["cases"][index]))
    assert observed["release"] is None
    assert observed["draft"]["status"] == "UNVERIFIED_DRAFT"
    # Drafts carry identifiers, not raw restricted source content.
    assert set(observed["draft"]) == {"status", "claim_ids", "binding"}


def test_support_grant_is_separate_from_release_grant():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][9])
    inputs["support_authority"] = False
    observed = reference.exercise(inputs)
    assert observed["draft"] is None and observed["release"] is not None


@pytest.mark.parametrize("change", ["expectation", "premise", "pair", "case_id", "operator"])
def test_authored_vector_drift_is_detected(change):
    document = checker.load()
    if change == "expectation":
        document["cases"][0]["expected"]["release"] = True
    elif change == "premise":
        document["cases"][0]["expected_premises"]["claimLinksValid"] = True
    elif change == "pair":
        document["cases"][18]["changes"][0]["value"] = 14
    elif change == "case_id":
        document["cases"][0]["id"] = "CER-T99"
    else:
        document["mutants"][0]["operator"] = "invented"
    assert checker.validate(document, checker.MODEL.read_text()) or not checker.run_suite(document)["success"]


def test_literal_formal_scenario_cannot_be_lost():
    document = checker.load()
    model = checker.MODEL.read_text().replace(document["cases"][0]["quint_test"], "missingTest")
    assert checker.validate(document, model)


def test_formal_map_link_cannot_be_lost():
    document = checker.load()
    mapping = json.loads(checker.MAP.read_text())
    for p in mapping["models"][0]["properties"]:
        p["scenario_tests"] = [n for n in p["scenario_tests"] if n != document["cases"][0]["quint_test"]]
    assert checker.validate(document, checker.MODEL.read_text(), mapping)


def test_first_bad_source_does_not_hide_remaining_valid_support():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][13])
    observed = reference.exercise(inputs)
    assert observed["candidate_premises"]["claimLinksValid"]
    assert observed["candidate_premises"] == checker.premises(inputs)
    assert observed["release"] is None


def test_unauthorized_source_access_does_not_get_fixed_by_disclosing_more():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][5])
    inputs["review"]["clearance"] = 0
    inputs["review"]["accessible_sources"] = [s["id"] for s in inputs["sources"]]
    assert reference.exercise(inputs)["release"] is None


def test_arbitrary_patch_cannot_create_fields():
    with pytest.raises(ValueError):
        reference.materialize(checker.load()["base"], [dict(path=["invented"], value=True)])


def test_case_constructor_does_not_mutate_base():
    document = checker.load()
    original = deepcopy(document["base"])
    for case in document["cases"]:
        checker.inputs_for(document, case)
    assert document["base"] == original


def test_malformed_mutant_release_cannot_earn_credit():
    def runner(inputs, operator=None):
        observed = reference.exercise(inputs, operator)
        if operator:
            observed["release"] = {"claimed": "success"}
        return observed
    report = checker.run_suite(checker.load(), runner)
    assert report["mutation_summary"]["invalid"] == 9
    assert report["mutation_summary"]["killed"] == 0


def test_patch_cannot_hide_an_invalid_materialized_input_type():
    document = checker.load()
    document["cases"][0]["changes"][0]["value"] = "13"
    assert any("materialized input" in e for e in checker.validate(document, checker.MODEL.read_text()))


@pytest.mark.parametrize("reverse", [False, True])
def test_split_measurements_from_one_origin_are_preserved_without_double_counting(reverse):
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][22])
    if reverse:
        inputs["sources"].reverse()
    inputs["admission_binding"] = inputs["review"]["binding"] = reference.bundle_binding(inputs)
    good = reference.exercise(inputs)
    assert good["candidate_premises"] == checker.premises(inputs)
    assert good["candidate_premises"]["claimLinksValid"]
    assert good["release"] is not None
    inputs["policy"]["minimum_origins"] = 2
    inputs["admission_binding"] = inputs["review"]["binding"] = reference.bundle_binding(inputs)
    denied = reference.exercise(inputs)
    assert denied["candidate_premises"]["claimLinksValid"]
    assert not denied["candidate_premises"]["independenceVerified"]
    assert denied["release"] is None


def test_report_restriction_is_not_replaced_by_a_lower_source_classification():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][23])
    assert all(s["classification"] == 0 for s in inputs["sources"])
    assert inputs["report"]["classification"] == 1
    denied = reference.exercise(inputs)
    assert not denied["candidate_premises"]["disclosurePermitted"]
    assert denied["release"] is None
    unsafe = reference.exercise(inputs, "ignore_report_classification")
    assert unsafe["release"] is not None
    assert "CER-P06" in checker.failures(unsafe["inputs"])


def test_review_access_must_cover_report_as_well_as_supporting_sources():
    document = checker.load()
    inputs = checker.inputs_for(document, document["cases"][24])
    assert all(s["classification"] <= inputs["review"]["clearance"] for s in inputs["sources"])
    assert inputs["report"]["classification"] > inputs["review"]["clearance"]
    assert reference.exercise(inputs)["release"] is None
    inputs["review"]["clearance"] = 1
    assert reference.exercise(inputs)["release"] is not None
