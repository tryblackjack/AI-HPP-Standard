#!/usr/bin/env python3
"""Static checks for the public regulator simulation pack."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACK_ROOT = ROOT / "regulator-sim"

REQUIRED_PUBLIC_FILES = [
    PACK_ROOT / "DOC_CONTROL.md",
    PACK_ROOT / "CHANGELOG.md",
    PACK_ROOT / "SCOPE.md",
    PACK_ROOT / "PROCEDURES" / "INSPECTION_WORKFLOW.md",
    PACK_ROOT / "PROCEDURES" / "EVIDENCE_EXPORT_AND_REDACTION.md",
    PACK_ROOT / "PROCEDURES" / "NONCONFORMITY_AND_CAPA.md",
    PACK_ROOT / "PROCEDURES" / "CHANGE_CONTROL.md",
    PACK_ROOT / "REQUESTS" / "REQUEST_CATALOG.md",
    PACK_ROOT / "REQUESTS" / "INSPECTOR_QBANK_PUBLIC.md",
    PACK_ROOT / "CROSSWALK" / "ISO_42001_CONTROL_MAP_PUBLIC.md",
    PACK_ROOT / "CROSSWALK" / "NIST_AI_RMF_MAP_PUBLIC.md",
    PACK_ROOT / "CONFORMANCE" / "REQUIREMENT_TO_EVIDENCE_MAP.yaml",
    PACK_ROOT / "TEMPLATES" / "EVIDENCE_BUNDLE_SCHEMA.json",
    PACK_ROOT / "TEMPLATES" / "EVIDENCE_BUNDLE_TEMPLATE.json",
    PACK_ROOT / "TEMPLATES" / "SCOPE_DECLARATION_TEMPLATE.md",
    PACK_ROOT / "TEMPLATES" / "INCIDENT_RECORD_TEMPLATE.md",
    PACK_ROOT / "TEMPLATES" / "CHANGE_RECORD_TEMPLATE.md",
    PACK_ROOT / "TEMPLATES" / "TOOL_REGISTRY_SNAPSHOT_SCHEMA.json",
    PACK_ROOT / "SAMPLES" / "evidence_bundle_example.json",
    PACK_ROOT / "SAMPLES" / "tool_registry_snapshot_example.json",
    PACK_ROOT / "SAMPLES" / "change_record_example.md",
    PACK_ROOT / "SAMPLES" / "incident_record_example.md",
    PACK_ROOT / "SCENARIOS" / "GOLDEN_WALKTHROUGH_PUBLIC.md",
    PACK_ROOT / "SCENARIOS" / "ADVERSARIAL_REQUESTS_PUBLIC.md",
    PACK_ROOT / "SCENARIOS" / "AUDIT_WALKTHROUGH_PUBLIC.md",
]

JSON_SAMPLE_FILES = [
    PACK_ROOT / "SAMPLES" / "evidence_bundle_example.json",
    PACK_ROOT / "SAMPLES" / "tool_registry_snapshot_example.json",
]

EVIDENCE_BUNDLE_REQUIRED_KEYS = {
    "bundle_id",
    "generated_at",
    "request_id",
    "scope",
    "records",
}

BANNED_REFERENCE_PATTERNS = (
    "_archive/private_quarantine",
    "internal/",
)

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def check_public_pack_files_non_empty() -> list[str]:
    errors: list[str] = []
    for path in REQUIRED_PUBLIC_FILES:
        if not path.exists():
            errors.append(f"Missing file: {path.relative_to(ROOT)}")
            continue
        if len(path.read_text(encoding="utf-8", errors="ignore").strip()) == 0:
            errors.append(f"Empty file: {path.relative_to(ROOT)}")
    return errors


def check_regulator_pack_links() -> list[str]:
    errors: list[str] = []
    for md in sorted(PACK_ROOT.rglob("*.md")):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for raw_target in MARKDOWN_LINK_RE.findall(text):
            target = raw_target.strip()
            if target.startswith(("http://", "https://", "mailto:")):
                continue
            if target.startswith("#"):
                continue
            target_path = target.split("#", 1)[0].strip()
            if not target_path:
                continue
            candidate = (md.parent / target_path).resolve()
            if not candidate.exists():
                errors.append(
                    f"Broken link in {md.relative_to(ROOT)} -> {target_path}"
                )
    return errors


def check_json_samples_valid() -> list[str]:
    errors: list[str] = []
    for path in JSON_SAMPLE_FILES:
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except FileNotFoundError:
            errors.append(f"Missing JSON sample: {path.relative_to(ROOT)}")
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return errors


def check_evidence_bundle_sanity() -> list[str]:
    errors: list[str] = []
    sample_path = PACK_ROOT / "SAMPLES" / "evidence_bundle_example.json"
    try:
        payload = json.loads(sample_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return [f"Missing JSON sample: {sample_path.relative_to(ROOT)}"]
    except json.JSONDecodeError as exc:
        return [f"Invalid JSON in {sample_path.relative_to(ROOT)}: {exc}"]

    missing = sorted(EVIDENCE_BUNDLE_REQUIRED_KEYS - set(payload.keys()))
    if missing:
        errors.append(
            "Evidence bundle sample missing required keys: " + ", ".join(missing)
        )

    records = payload.get("records")
    if not isinstance(records, list) or not records:
        errors.append("Evidence bundle sample must include a non-empty 'records' array")

    return errors


def check_for_banned_references() -> list[str]:
    errors: list[str] = []
    for path in sorted(PACK_ROOT.rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for banned in BANNED_REFERENCE_PATTERNS:
            if banned in text:
                errors.append(
                    f"Banned reference '{banned}' found in {path.relative_to(ROOT)}"
                )
    return errors


def main() -> int:
    errors: list[str] = []
    errors.extend(check_public_pack_files_non_empty())
    errors.extend(check_regulator_pack_links())
    errors.extend(check_json_samples_valid())
    errors.extend(check_evidence_bundle_sanity())
    errors.extend(check_for_banned_references())

    if errors:
        print("FAIL: regulator simulation checks failed")
        for err in errors:
            print(f" - {err}")
        return 1

    print("OK: regulator simulation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
