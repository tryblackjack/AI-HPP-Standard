#!/usr/bin/env python3
"""Local wording hygiene check for promotional language."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORDS = [
    "revolutionary",
    "game-changing",
    "world-class",
    "cutting-edge",
    "disruptive",
    "magic",
    "guaranteed",
]


def main() -> int:
    flagged = []
    for md in ROOT.rglob("*.md"):
        rel = md.relative_to(ROOT)
        if str(rel).startswith("docs/archive/"):
            continue
        text = md.read_text(encoding="utf-8", errors="ignore").lower()
        for w in WORDS:
            if w in text:
                flagged.append((rel, w))
    if flagged:
        for rel, w in flagged:
            print(f"FLAG: {rel} contains '{w}'")
        return 1
    print("OK: no slop words detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
