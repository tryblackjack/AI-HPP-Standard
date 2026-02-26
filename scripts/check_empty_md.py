#!/usr/bin/env python3
"""Fail when markdown files are empty or near-empty without an explicit stub marker."""

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
STUB_MARKER = "STUB NOTE: intentionally minimal"
MIN_NON_WS = 30


def non_whitespace_len(text: str) -> int:
    return len(re.sub(r"\s+", "", text))


def main() -> int:
    violations: list[tuple[Path, int, bool]] = []

    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        n = non_whitespace_len(text)
        has_stub = STUB_MARKER in text
        if n == 0 or (n < MIN_NON_WS and not has_stub):
            violations.append((md.relative_to(ROOT), n, has_stub))

    if violations:
        print("FAIL: empty or near-empty markdown files detected")
        for path, count, has_stub in violations:
            print(f" - {path} (non_ws={count}, stub_marker={has_stub})")
        return 1

    print("OK: no disallowed empty/near-empty markdown files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
