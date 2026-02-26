#!/usr/bin/env python3
"""Static checks for the internal regulator simulation pack."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SCHEMA_FILES = [
    ROOT / "schemas" / "evidence-bundle.schema.json",
    ROOT / "schemas" / "audit-export.schema.json",
]

V319_FIELDS = {
    "escalation_timeout_triggered",
    "safe_state_entered",
    "escalation_timeout_ms",
    "override_actor_role",
    "override_reason_code",
    "override_latency_ms",
    "override_frequency_counter",
}

CONDITIONAL_CES_FIELDS = {
    "domain_risk_class",
    "chosen_action",
    "constraints_triggered",
    "escalation_event",
    "approval_status",
}

REQUIRED_INTERNAL_FILES = [
    ROOT / "internal" / "regulator-sim" / "README.md",
    ROOT / "internal" / "regulator-sim" / "INSPECTOR_QUESTION_BANK.md",
    ROOT / "internal" / "regulator-sim" / "EVIDENCE_REQUEST_PLAYBOOK.md",
    ROOT / "internal" / "regulator-sim" / "AUDIT_WALKTHROUGH.md",
    ROOT / "internal" / "regulator-sim" / "ADVERSARIAL_REGULATOR_ATTACK.md",
]

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def collect_keys(node: object, sink: set[str]) -> None:
    if isinstance(node, dict):
        for key, value in node.items():
            sink.add(key)
            collect_keys(value, sink)
    elif isinstance(node, list):
        for item in node:
            collect_keys(item, sink)


def check_schema_fields() -> list[str]:
    errors: list[str] = []
    required = V319_FIELDS | CONDITIONAL_CES_FIELDS
    for schema_path in SCHEMA_FILES:
        if not schema_path.exists():
            errors.append(f"Missing schema file: {schema_path.relative_to(ROOT)}")
            continue
        data = json.loads(schema_path.read_text(encoding="utf-8"))
        keys: set[str] = set()
        collect_keys(data, keys)
        missing = sorted(required - keys)
        if missing:
            errors.append(
                f"Schema {schema_path.relative_to(ROOT)} missing fields: {', '.join(missing)}"
            )
    return errors


def check_regulator_pack_links() -> list[str]:
    errors: list[str] = []
    for md in sorted((ROOT / "regulator-pack").glob("*.md")):
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


def check_internal_files_non_empty() -> list[str]:
    errors: list[str] = []
    for path in REQUIRED_INTERNAL_FILES:
        if not path.exists():
            errors.append(f"Missing file: {path.relative_to(ROOT)}")
            continue
        if len(path.read_text(encoding="utf-8", errors="ignore").strip()) == 0:
            errors.append(f"Empty file: {path.relative_to(ROOT)}")
    return errors


def main() -> int:
    errors = []
    errors.extend(check_schema_fields())
    errors.extend(check_regulator_pack_links())
    errors.extend(check_internal_files_non_empty())

    if errors:
        print("FAIL: regulator simulation checks failed")
        for err in errors:
            print(f" - {err}")
        return 1

    print("OK: regulator simulation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
