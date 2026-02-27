#!/usr/bin/env python3
"""Public-safe markdown link checker for local relative links."""

from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")

# Keep checks scoped to public docs and avoid generated/private trees.
SKIP_DIRS = {
    ".git",
    ".github",
    ".venv",
    "node_modules",
    "archive",
    "translations",
}



def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        rel = path.relative_to(REPO_ROOT)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        files.append(path)
    return files


def normalize_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    return target


def is_local_relative_link(target: str) -> bool:
    if not target:
        return False
    if target.startswith("#"):
        return False
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
        # URL-like schemes, e.g. http:, https:, mailto:, data:
        return False
    if target.startswith("//"):
        return False
    if target.startswith("/"):
        # Treat root-absolute links as out of scope for this local checker.
        return False
    return True


def check_links() -> list[str]:
    errors: list[str] = []

    for md in iter_markdown_files():
        text = md.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            target = normalize_target(match.group(1))
            if not is_local_relative_link(target):
                continue

            target_path_part, *_ = target.split("#", 1)
            target_path_part, *_ = target_path_part.split("?", 1)
            if not target_path_part:
                continue

            resolved = (md.parent / target_path_part).resolve()
            if not resolved.exists():
                errors.append(
                    f"Broken link in {md.relative_to(REPO_ROOT)} -> {target_path_part}"
                )

    return errors


def main() -> int:
    errors = check_links()
    if errors:
        for error in errors:
            print(error)
        return 1

    print("Local relative markdown links look good.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
