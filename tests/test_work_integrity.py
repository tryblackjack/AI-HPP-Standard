"""Observable work, explicit boundaries, matched framing and honest mutation results."""
from copy import deepcopy
import json

import pytest

from examples import work_integrity_reference as reference
from scripts import check_work_integrity as checker


def test_contract_cases_and_executed_mutants():
    document = checker.load()
    assert checker.validate(document, checker.MODEL.read_text()) == []
    report = checker.run_suite(document)
    assert report["success"] and report["pairs_match"]
    assert len(report["cases"]) == 10
    assert report["mutation_summary"] == dict(declared=6, killed=6, survived=0,
                                             invalid=0, denominator=6, score=1)


@pytest.mark.parametrize("index", range(6))
def test_mutant_changes_captured_artifact_or_report_with_same_facts(index):
    document = checker.load()
    mutant = document["mutants"][index]
    case = next(c for c in document["cases"] if c["id"] == mutant["case_id"])
    good = reference.exercise(case["inputs"])
    bad = reference.exercise(case["inputs"], mutant["operator"])
    assert bad["inputs"] == good["inputs"]
    assert (bad["artifact"], bad["report"]) != (good["artifact"], good["report"])
    assert checker.failures(good) == []
    assert mutant["predicate_id"] in checker.failures(bad)


def test_no_op_mutants_survive():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None: reference.exercise(inputs))
    assert not report["success"]
    assert report["mutation_summary"]["survived"] == 6


def test_invalid_mutants_are_excluded_from_denominator():
    def runner(inputs, operator=None):
        if operator:
            raise OSError("fixture unavailable")
        return reference.exercise(inputs)
    report = checker.run_suite(checker.load(), runner)
    assert not report["success"]
    assert report["mutation_summary"]["invalid"] == 6
    assert report["mutation_summary"]["denominator"] == 0
    assert report["mutation_summary"]["score"] is None


def test_invalid_baseline_never_earns_mutation_credit():
    def runner(inputs, operator=None):
        if operator is None:
            raise ValueError("no baseline")
        return reference.exercise(inputs, operator)
    report = checker.run_suite(checker.load(), runner)
    assert all(m["result"] == "INVALID" for m in report["mutants"])


def test_blanket_refusal_fails_useful_work():
    report = checker.run_suite(checker.load(), lambda inputs, operator=None:
                               reference.exercise(inputs, "fabricated_blocker"))
    assert not report["success"]
    assert report["cases"][0]["result"] == "FAIL"
    assert report["cases"][1]["result"] == "FAIL"


def test_framing_defect_is_observable_without_private_reasoning():
    document = checker.load()
    first, second = (deepcopy(c["inputs"]) for c in document["cases"][:2])
    safety = reference.exercise(first, "silent_omission")
    capabilities = reference.exercise(second, "silent_omission")
    assert "WIT-P04" in checker.failures(safety)
    assert checker.failures(capabilities) == []
    assert safety["artifact"] != capabilities["artifact"]
    assert not checker.run_suite(document, lambda inputs, operator=None:
                                 reference.exercise(inputs, "silent_omission"))["pairs_match"]


@pytest.mark.parametrize("index", [2, 4, 6, 7, 8])
def test_real_boundaries_and_failures_are_not_sabotage(index):
    capture = reference.exercise(checker.load()["cases"][index]["inputs"])
    assert checker.failures(capture) == []
    assert capture["report"]["boundary"] is not None
    assert capture["report"]["status"] != "COMPLETE"


def test_claim_cannot_replace_actual_artifact_acceptance():
    capture = reference.exercise(checker.load()["cases"][0]["inputs"])
    capture["artifact"]["count"] = 999
    assert "WIT-P02" in checker.failures(capture)
    assert "WIT-P04" in checker.failures(capture)


def test_pair_equivalence_cannot_be_faked_with_different_permissions():
    document = checker.load()
    document["cases"][1]["inputs"]["permitted"] = []
    assert "non-equivalent framing pair" in checker.validate(document, checker.MODEL.read_text())


def test_literal_formal_link_cannot_be_lost():
    document = checker.load()
    text = checker.MODEL.read_text().replace(document["cases"][0]["quint"]["quint_test"], "lostTest")
    assert checker.validate(document, text)


def test_formal_map_link_cannot_be_lost(monkeypatch):
    original = checker.Path.read_text
    def changed(path, *args, **kwargs):
        text = original(path, *args, **kwargs)
        if path == checker.MAP:
            document = json.loads(text)
            for prop in document["models"][0]["properties"]:
                prop["scenario_tests"] = [n for n in prop["scenario_tests"]
                                          if n != "workIntegrityPermittedSafetyTest"]
            return json.dumps(document)
        return text
    monkeypatch.setattr(checker.Path, "read_text", changed)
    assert checker.validate(checker.load(), checker.MODEL.read_text())


def test_authored_expectation_drift_fails():
    document = checker.load()
    document["cases"][0]["expected_artifact"]["count"] = 999
    assert not checker.run_suite(document)["success"]


def test_mutant_abstraction_drift_is_invalid_not_killed():
    document = checker.load()
    document["mutants"][0]["quint"]["proposal"]["evidenceComplete"] = True
    report = checker.run_suite(document)
    assert not report["success"]
    assert report["mutants"][0]["result"] == "INVALID"


def test_mutant_seed_and_named_predicate_cannot_drift():
    document = checker.load()
    document["mutants"][0]["predicate_id"] = "WIT-P04"
    assert "mutant seed/predicate mismatch" in checker.validate(document, checker.MODEL.read_text())
