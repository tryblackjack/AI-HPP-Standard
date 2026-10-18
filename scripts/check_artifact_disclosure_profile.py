#!/usr/bin/env python3
"""Check disclosure contract consistency and execute finite reference mutants."""
from __future__ import annotations

from collections import Counter
import json
from pathlib import Path
import sys

import jsonschema

ROOT = Path(__file__).resolve().parents[1]
# Support both direct script execution and importing through pytest.
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from examples import artifact_disclosure_reference as reference  # noqa: E402

PROFILE = ROOT / "docs/generated-artifact-disclosure-assurance-profile-2026-10.md"
VECTORS = ROOT / "examples/generated-artifact-disclosure-vectors.json"
SCHEMA = ROOT / "schemas/generated-artifact-disclosure-vectors.schema.json"
PREDICATES = {f"GAD-P{index:02d}" for index in range(1, 9)}
VECTORS_IDS = {f"GAD-N{index:02d}" for index in range(1, 14)}
MUTANTS = {f"GAD-M{index:02d}" for index in range(1, 14)}
CONTROLS = {f"GAD-C{index:02d}" for index in range(1, 5)}


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(document: dict, profile: str) -> list[str]:
    """Reject orphaned, removed or silently redefined cases before execution."""
    errors = []
    schema_errors = list(jsonschema.Draft202012Validator(load(SCHEMA)).iter_errors(document))
    if schema_errors:
        return [f"schema: {error.message}" for error in schema_errors]
    for name, ids in (
        ("predicates", PREDICATES), ("vectors", VECTORS_IDS),
        ("mutants", MUTANTS), ("positive_controls", CONTROLS),
    ):
        observed = [item["id"] for item in document[name]]
        if len(observed) != len(set(observed)) or set(observed) != ids:
            errors.append(f"{name} ID inventory mismatch")
    for predicate in document["predicates"]:
        if f'`{predicate["id"]} {predicate["name"]}`' not in profile:
            errors.append(f'profile predicate mismatch: {predicate["id"]}')
    for name in ("vectors", "mutants"):
        if {item["predicate_id"] for item in document[name]} != PREDICATES:
            errors.append(f"{name} predicate coverage mismatch")
        operators = [item["operator"] for item in document[name]]
        if len(operators) != len(set(operators)) or set(operators) != set(reference.OPERATORS):
            errors.append(f"{name} operator coverage mismatch")
    vectors = {item["id"]: item for item in document["vectors"]}
    kill_links = []
    for mutant in document["mutants"]:
        link = mutant["killed_by_vector_id"]
        kill_links.append(link)
        vector = vectors.get(link)
        if not vector or any(
            mutant[key] != vector[key] for key in ("operator", "predicate_id")
        ):
            errors.append(f'{mutant["id"]} inconsistent kill link')
    if set(kill_links) != VECTORS_IDS or len(kill_links) != len(set(kill_links)):
        errors.append("kill-vector coverage mismatch")
    scenarios = [item["scenario"] for item in document["positive_controls"]]
    if set(scenarios) != set(reference.positive_results(reference.candidate())) or len(set(scenarios)) != 4:
        errors.append("positive scenario coverage mismatch")
    owners = "\n".join((ROOT / path).read_text(encoding="utf-8") for path in (
        "docs/ai-hpp-standard.md", "docs/agentic-safety-and-relational-integrity.md"
    ))
    for predicate in document["predicates"]:
        for requirement in predicate["existing_requirement_ids"]:
            if requirement not in owners:
                errors.append(f"unknown normative owner: {requirement}")
    for boundary in (
        "ACTIVE_INFORMATIVE", "frozen AI-HPP v4.3.0 baseline",
        "post-rc.1", "Marker absence alone is not proof",
        "No new Quint invariant", "REFERENCE_TESTED",
    ):
        if boundary not in profile:
            errors.append(f"missing claim boundary: {boundary}")
    return errors


def run_suite(document: dict, evaluator=reference.evaluate) -> dict:
    """Compute outcomes from executable operators; never copy expected KILLED."""
    vectors = {item["id"]: item for item in document["vectors"]}
    results = []
    for mutant in document["mutants"]:
        vector = vectors[mutant["killed_by_vector_id"]]
        try:
            observed = evaluator(reference.candidate(mutant["operator"]))
            violations = observed["violations"]
            killed = (
                observed["decision"] == vector["expected_decision"]
                and vector["required_witness"] in violations.get(vector["predicate_id"], [])
            )
            result = "KILLED" if killed else "SURVIVED"
            witness = {"violations": violations, "capture_digest": observed["capture_digest"]}
        except (ValueError, KeyError, TypeError) as exc:
            result, witness = "INVALID", {"error_type": type(exc).__name__}
        results.append({
            "mutant": mutant["id"], "operator": mutant["operator"],
            "vector": vector["id"], "predicate": vector["predicate_id"],
            "result": result, "witness": witness,
        })
    base = reference.candidate()
    base_allowed = evaluator(base)["decision"] == "allow"
    useful = reference.positive_results(base)
    positives = [{
        "id": item["id"], "scenario": item["scenario"],
        "result": "PASS" if base_allowed and useful[item["scenario"]] else "FAIL",
    } for item in document["positive_controls"]]
    counts = Counter(item["result"] for item in results)
    denominator = counts["KILLED"] + counts["SURVIVED"]
    return {
        "claim": "REFERENCE_TESTED_ONLY", "artifact_version": document["artifact_version"],
        "vectors_sha256": reference.digest(document),
        "mutation_summary": {
            "declared": len(results), "killed": counts["KILLED"],
            "survived": counts["SURVIVED"], "invalid": counts["INVALID"],
            "not_applicable": counts["NOT_APPLICABLE"], "denominator": denominator,
            "score": counts["KILLED"] / denominator if denominator else None,
        },
        "mutants": results, "positive_controls": positives,
        "success": all(item["result"] == "KILLED" for item in results)
        and all(item["result"] == "PASS" for item in positives),
    }


def main() -> int:
    try:
        document = load(VECTORS)
        errors = validate(document, PROFILE.read_text(encoding="utf-8"))
        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1
        report = run_suite(document)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(report, indent=2))
    return 0 if report["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
