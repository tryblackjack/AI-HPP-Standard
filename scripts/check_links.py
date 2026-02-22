#!/usr/bin/env python3
"""Local link checker for markdown files."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"\[[^\]]+\]\((<[^>]+>|[^)]+)\)")


def main() -> int:
    missing = []
    for md in ROOT.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="ignore")
        for raw_link in LINK_RE.findall(text):
            link = raw_link[1:-1] if raw_link.startswith('<') and raw_link.endswith('>') else raw_link
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = (md.parent / link).resolve()
            if not target.exists():
                missing.append((md.relative_to(ROOT), link))
    if missing:
        for src, link in missing:
            print(f"MISSING: {src} -> {link}")
        return 1
    print("OK: no missing local markdown links found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
