#!/usr/bin/env python3
"""Generate semantic fingerprints for normative requirement blocks."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STANDARD_DIR = REPO_ROOT / "standard"
OUTPUT_FILE = REPO_ROOT / "regulator-sim" / "CONFORMANCE" / "NORMATIVE_FINGERPRINT.json"
HEADER_PATTERN = re.compile(r"^####\s+(AI-HPP-\d+\.\d+\.\d+):")


def normalize_block(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def extract_requirement_blocks(content: str) -> list[tuple[str, str]]:
    lines = content.splitlines()
    blocks: list[tuple[str, str]] = []
    i = 0

    while i < len(lines):
        match = HEADER_PATTERN.match(lines[i])
        if not match:
            i += 1
            continue

        req_id = match.group(1)
        start = i
        i += 1
        while i < len(lines) and not lines[i].startswith("#### "):
            i += 1

        block_text = "\n".join(lines[start:i])
        blocks.append((req_id, block_text))

    return blocks


def build_fingerprint() -> dict[str, dict[str, str]]:
    fingerprint: dict[str, dict[str, str]] = {}

    for md_file in sorted(STANDARD_DIR.glob("*.md")):
        content = md_file.read_text(encoding="utf-8")
        for req_id, block in extract_requirement_blocks(content):
            normalized = normalize_block(block)
            digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
            fingerprint[req_id] = {
                "file": md_file.relative_to(REPO_ROOT).as_posix(),
                "hash": digest,
            }

    return dict(sorted(fingerprint.items()))


def main() -> None:
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    fingerprint = build_fingerprint()
    OUTPUT_FILE.write_text(json.dumps(fingerprint, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
