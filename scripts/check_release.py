#!/usr/bin/env python3
"""Validate release composition and partial formal traceability."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
VERSION = "4.4.0-rc.1"
MANIFEST = "data/releases/v4.4.0-rc.1.json"
MAP = "data/formal-assurance-map.json"
OWNERS = {
    "docs/ai-hpp-standard.md": "ACTIVE_NORMATIVE",
    "docs/agentic-safety-and-relational-integrity.md": "ACTIVE_NORMATIVE",
    "docs/human-understanding-standard.md": "USABLE_DRAFT",
}
CONTRACTS = {"spec/core.md", "spec/signal.md", "spec/safety.md"}
PROFILE_PATHS = {
    "docs/autonomous-replication-and-persistence-assurance-profile-2026-10.md",
    "docs/cyber-capable-model-containment-assurance-profile-2026-10.md",
    "docs/subject-integrity-and-value-framing-assurance-profile-2026-10.md",
    "docs/assurance-evaluation-and-technical-oversight.md",
}
ACTIVE_DIRS = {
    ".github", "docs", "spec", "formal", "data", "schemas", "examples",
    "scripts", "tests", "LICENSES",
}
ROOT_FILES = {
    "README.md", "CONTRIBUTING.md", "CITATION.cff", "LICENSE", "REUSE.toml",
    "TRADEMARKS.md", "LICENSING_PROVENANCE_MATRIX.csv", ".gitignore",
    ".markdownlint.json", "eslint.config.mjs", "requirements-ci.txt",
}
SKIP = {"__pycache__", "node_modules", ".pytest_cache", ".ruff_cache", "_apalache-out"}


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def active_paths(root: Path) -> list[str]:
    paths = []
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in SKIP for part in rel.parts) or not path.is_file():
            continue
        name = rel.as_posix()
        if name == MANIFEST or name.startswith("data/releases/"):
            continue
        if name in ROOT_FILES or rel.parts[0] in ACTIVE_DIRS:
            paths.append(name)
    return sorted(paths)


def role(path: str) -> str:
    if path in OWNERS:
        return OWNERS[path]
    if path in CONTRACTS:
        return "NORMATIVE_CONTRACT"
    if path.startswith(("scripts/", "tests/", ".github/")):
        return "VALIDATION_TOOLING"
    return "ACTIVE_INFORMATIVE"


def validate_manifest(document: dict, root: Path, frozen: bool = False) -> list[str]:
    errors = []
    expected = {
        "schema_version": "1.0.0", "package_version": VERSION,
        "tag": f"v{VERSION}", "normative_baseline": "4.3.0",
        "maturity": "USABLE_DRAFT", "release_kind": "prerelease",
        "quint_version": "0.33.0", "java_version": "21",
        "random_samples_per_model": 5000, "symbolic_depth": 12,
    }
    for key, value in expected.items():
        if document.get(key) != value:
            errors.append(f"manifest {key} must be {value}")
    if not re.fullmatch(r"[0-9a-f]{40}", document.get("source_snapshot", "")):
        errors.append("source_snapshot must identify an immutable commit")
    entries = document.get("files", [])
    paths = [entry.get("path", "") for entry in entries]
    if paths != sorted(set(paths)):
        errors.append("manifest file paths must be unique and sorted")
    required = set(OWNERS) | CONTRACTS | PROFILE_PATHS | {
        MAP, "formal/ai_hpp_core.qnt", "formal/subject_integrity_value_framing.qnt",
        "formal/coverage.md", "docs/releases/v4.4.0-rc.1.md", "CITATION.cff",
    }
    if required - set(paths):
        errors.append(f"manifest missing required files: {sorted(required - set(paths))}")
    for entry in entries:
        name = entry.get("path", "")
        rel = Path(name)
        if rel.is_absolute() or ".." in rel.parts or not name or name == MANIFEST:
            errors.append(f"invalid manifest path: {name}")
            continue
        if name not in ROOT_FILES and rel.parts[0] not in ACTIVE_DIRS:
            errors.append(f"out-of-scope manifest path: {name}")
        if entry.get("role") != role(name):
            errors.append(f"role mismatch: {name}")
        if not re.fullmatch(r"[0-9a-f]{64}", entry.get("sha256", "")):
            errors.append(f"invalid sha256: {name}")
        # Normative files cannot silently drift even on a development checkout.
        if frozen or name in OWNERS or name in CONTRACTS:
            path = root / name
            if not path.is_file() or digest(path) != entry.get("sha256"):
                errors.append(f"file missing or changed: {name}")
    if frozen and set(paths) != set(active_paths(root)):
        errors.append("frozen manifest does not match complete active-file inventory")
    for name in PROFILE_PATHS:
        path = root / name
        if path.is_file() and "ACTIVE_INFORMATIVE" not in path.read_text()[:250]:
            errors.append(f"candidate/informative status lost: {name}")
    citation = yaml.safe_load((root / "CITATION.cff").read_text())
    if str(citation.get("version")) != VERSION:
        errors.append("citation package version mismatch")
    return errors


def requirement_inventory(root: Path) -> dict[str, str]:
    result = {}
    for owner in OWNERS:
        text = (root / owner).read_text(encoding="utf-8")
        pattern = r"\*\*(MVP-\d{3}) —" if owner.endswith("/ai-hpp-standard.md") else r"^### ([A-Z]+-REQ-\d{3})"
        for req_id in re.findall(pattern, text, re.M):
            result[req_id] = owner
    return result


def validate_map(document: dict, root: Path) -> list[str]:
    errors = []
    if document.get("status") != "ACTIVE_INFORMATIVE":
        errors.append("formal map must stay informative")
    if document.get("normative_baseline") != "4.3.0":
        errors.append("formal map baseline mismatch")
    expected_models = {
        "formal/ai_hpp_core.qnt": "allCoreInvariants",
        "formal/subject_integrity_value_framing.qnt": "allSubjectIntegrityInvariants",
    }
    models = document.get("models", [])
    if [m.get("path") for m in models] != list(expected_models):
        errors.append("formal model inventory mismatch")
    inventory = requirement_inventory(root)
    links: dict[str, list[dict]] = {key: [] for key in inventory}
    predicates = {}
    for name in ("replication-persistence-negative-test-vectors.json",
                 "subject-integrity-value-framing-vectors.json",
                 "proportionate-action-vectors.json",
                 "robot-action-binding-vectors.json"):
        artifact = read_json(root / "examples" / name)
        predicates.update({p["id"]: artifact for p in artifact["predicates"]})
    for model in models:
        path = model.get("path")
        if path not in expected_models:
            continue
        text = (root / path).read_text(encoding="utf-8")
        aggregate = expected_models[path]
        match = re.search(rf"val {aggregate}: bool = all \{{([^}}]+)\}}", text)
        members = re.findall(r"\b(\w+)\s*,", match.group(1)) if match else []
        properties = model.get("properties", [])
        names = [p.get("invariant") for p in properties]
        if model.get("aggregate") != aggregate or names != members:
            errors.append(f"aggregate/property inventory mismatch: {path}")
        test_blocks = dict(re.findall(
            r"^  run (\w+) = \{(.*?)^  \}", text, re.M | re.S
        ))
        for prop in properties:
            invariant = prop["invariant"]
            if not prop.get("scope"):
                errors.append(f"missing abstraction scope: {invariant}")
            for req_id in prop.get("requirement_ids", []):
                if req_id not in links:
                    errors.append(f"unknown requirement: {req_id}")
                else:
                    links[req_id].append({"model": path, "invariant": invariant})
            if not prop.get("predicate_ids") or any(
                p not in predicates for p in prop.get("predicate_ids", [])
            ):
                errors.append(f"unknown/missing predicate: {invariant}")
            for test in prop.get("scenario_tests", []) + prop.get("mutation_tests", []):
                if test not in test_blocks:
                    errors.append(f"missing executable witness: {test}")
            for test in prop.get("mutation_tests", []):
                block = test_blocks.get(test, "")
                if f"check(not({invariant}))" not in block or ".then(mutant" not in block:
                    errors.append(f"mutant does not assert named violation: {test}")
        mapped_mutants = [t for p in properties for t in p.get("mutation_tests", [])]
        actual_mutants = sorted(t for t in test_blocks if t.startswith("mutant"))
        if sorted(mapped_mutants) != actual_mutants:
            errors.append(f"mutation witness inventory mismatch: {path}")
    rows = document.get("requirements", [])
    ids = [row.get("id") for row in rows]
    if len(ids) != len(set(ids)) or set(ids) != set(inventory):
        errors.append("complete requirement inventory mismatch")
    for row in rows:
        req_id = row.get("id")
        if req_id not in inventory:
            continue
        owner = inventory[req_id]
        expected_coverage = "PARTIAL_ABSTRACTION" if links[req_id] else "NOT_MODELED"
        if row.get("owner") != owner or row.get("status") != OWNERS[owner]:
            errors.append(f"requirement owner/status mismatch: {req_id}")
        if row.get("coverage") != expected_coverage or row.get("properties") != links[req_id]:
            errors.append(f"false formal coverage: {req_id}")
    return errors


def refresh(root: Path) -> None:
    manifest = read_json(root / MANIFEST)
    # Explicit generation is only allowed before the candidate tag exists.
    result = subprocess.run(
        ["git", "show-ref", "--verify", "--quiet", f"refs/tags/v{VERSION}"],
        cwd=root, check=False,
    )
    if result.returncode == 0:
        raise ValueError("published candidate tag exists; create a new version")
    baseline_errors = validate_manifest(manifest, root)
    if baseline_errors:
        raise ValueError("\n".join(baseline_errors))
    manifest["files"] = [
        {"path": name, "role": role(name), "sha256": digest(root / name)}
        for name in active_paths(root)
    ]
    (root / MANIFEST).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--frozen", action="store_true", help="require exact release bytes")
    parser.add_argument("--refresh", action="store_true", help="generate unpublished candidate hashes")
    args = parser.parse_args()
    try:
        if args.refresh:
            refresh(ROOT)
        errors = validate_manifest(read_json(ROOT / MANIFEST), ROOT, args.frozen)
        errors.extend(validate_map(read_json(ROOT / MAP), ROOT))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"Release {VERSION}: composition and partial formal mapping valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
