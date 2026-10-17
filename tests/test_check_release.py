"""Release integrity and false-coverage regression tests."""
from copy import deepcopy
import json
import os
from pathlib import Path
import subprocess
import sys

import pytest
import yaml

from scripts import check_release as checker


def manifest() -> dict:
    return checker.read_json(checker.ROOT / checker.MANIFEST)


def formal_map() -> dict:
    return checker.read_json(checker.ROOT / checker.MAP)


def test_candidate_structure_and_formal_map() -> None:
    assert checker.validate_manifest(manifest(), checker.ROOT) == []
    assert checker.validate_map(formal_map(), checker.ROOT) == []


def test_candidate_version_cannot_replace_baseline_version() -> None:
    broken = manifest()
    broken["normative_baseline"] = "4.4.0-rc.1"
    assert any("normative_baseline" in e for e in checker.validate_manifest(broken, checker.ROOT))


def test_candidate_profile_cannot_be_silently_promoted() -> None:
    broken = manifest()
    entry = next(f for f in broken["files"] if f["path"] in checker.PROFILE_PATHS)
    entry["role"] = "ACTIVE_NORMATIVE"
    assert any("role mismatch" in e for e in checker.validate_manifest(broken, checker.ROOT))


def test_required_formal_model_cannot_be_omitted() -> None:
    broken = manifest()
    broken["files"] = [f for f in broken["files"] if f["path"] != "formal/ai_hpp_core.qnt"]
    assert any("missing required files" in e for e in checker.validate_manifest(broken, checker.ROOT))


def test_hash_change_is_detected_in_frozen_mode() -> None:
    broken = manifest()
    broken["files"][0]["sha256"] = "0" * 64
    assert any("missing or changed" in e for e in checker.validate_manifest(broken, checker.ROOT, True))


def test_duplicate_or_unsafe_path_is_rejected() -> None:
    broken = manifest()
    broken["files"].append(deepcopy(broken["files"][0]))
    broken["files"][0]["path"] = "../outside.md"
    errors = checker.validate_manifest(broken, checker.ROOT)
    assert any("unique and sorted" in e for e in errors)
    assert any("invalid manifest path" in e for e in errors)


def test_unlisted_active_artifact_is_detected(tmp_path: Path) -> None:
    broken = manifest()
    broken["files"] = [f for f in broken["files"] if f["path"] != "README.md"]
    assert any("complete active-file inventory" in e for e in checker.validate_manifest(
        broken, checker.ROOT, True
    ))
    # Ignore cache files when determining the release inventory.
    (tmp_path / "formal").mkdir()
    (tmp_path / "formal" / "new.qnt").write_text("module new {}")
    assert checker.active_paths(tmp_path) == ["formal/new.qnt"]
    (tmp_path / "formal" / "__pycache__").mkdir()
    (tmp_path / "formal" / "__pycache__" / "cache.pyc").write_bytes(b"cache")
    assert checker.active_paths(tmp_path) == ["formal/new.qnt"]


def test_invariant_cannot_disappear_from_map() -> None:
    broken = formal_map()
    broken["models"][0]["properties"].pop()
    assert any("aggregate/property inventory" in e for e in checker.validate_map(broken, checker.ROOT))


def test_unmodeled_requirement_cannot_be_claimed_verified() -> None:
    broken = formal_map()
    row = next(r for r in broken["requirements"] if r["coverage"] == "NOT_MODELED")
    row["coverage"] = "VERIFIED"
    assert any("false formal coverage" in e for e in checker.validate_map(broken, checker.ROOT))


def test_missing_requirement_gap_is_detected() -> None:
    broken = formal_map()
    broken["requirements"].pop()
    assert "complete requirement inventory mismatch" in checker.validate_map(broken, checker.ROOT)


def test_wrong_invariant_mutant_link_is_detected() -> None:
    broken = formal_map()
    broken["models"][0]["properties"][0]["mutation_tests"] = [
        "mutantRdpM02TopologyLimitKilledTest"
    ]
    assert any("named violation" in e for e in checker.validate_map(broken, checker.ROOT))


def test_unknown_predicate_is_detected() -> None:
    broken = formal_map()
    broken["models"][1]["properties"][0]["predicate_ids"] = ["SIV-P99"]
    assert any("unknown/missing predicate" in e for e in checker.validate_map(broken, checker.ROOT))


def test_nonexistent_positive_control_is_detected() -> None:
    broken = formal_map()
    broken["models"][0]["properties"][0]["scenario_tests"] = ["imaginedPositiveTest"]
    assert any("missing executable witness" in e for e in checker.validate_map(broken, checker.ROOT))


@pytest.mark.parametrize("change", [None, "failure", "pending", "wrong_sha", "wrong_path", "wrong_branch", "pull_request"])
def test_publication_gate_requires_all_successful_exact_commit_runs(
    tmp_path: Path, change: str | None,
) -> None:
    workflow = yaml.safe_load((checker.ROOT / ".github/workflows/publish-prerelease.yml").read_text())
    script = next(step["run"] for step in workflow["jobs"]["publish"]["steps"] if step.get("id") == "gate")
    python = script.split("python3 - <<'PY'\n", 1)[1].rsplit("\nPY", 1)[0]
    required = {
        "Repo Structure Validator": ".github/workflows/structure-validator.yml",
        "AI-HPP Standard Audit": ".github/workflows/hpp-standard-audit.yml",
        "Spec Consistency Checker": ".github/workflows/spec-consistency.yml",
    }
    sha = "a" * 40
    runs = [dict(name=name, path=path, head_sha=sha, head_branch="main",
                 event="push", status="completed", conclusion="success", id=i)
            for i, (name, path) in enumerate(required.items())]
    if change:
        field, value = {
            "failure": ("conclusion", "failure"), "pending": ("status", "in_progress"),
            "wrong_sha": ("head_sha", "b" * 40), "wrong_path": ("path", "other.yml"),
            "wrong_branch": ("head_branch", "unreviewed"), "pull_request": ("event", "pull_request"),
        }[change]
        runs[0][field] = value
    (tmp_path / "release-runs.json").write_text(json.dumps({"workflow_runs": runs}))
    output = tmp_path / "output"
    result = subprocess.run(
        [sys.executable, "-c", python], capture_output=True, text=True,
        env={**os.environ, "RUNNER_TEMP": str(tmp_path), "RELEASE_SHA": sha,
             "GITHUB_OUTPUT": str(output)}, check=False,
    )
    assert result.returncode == 0, result.stderr
    assert output.exists() is (change is None)
    if output.exists():
        assert output.read_text() == "ready=true\n"
