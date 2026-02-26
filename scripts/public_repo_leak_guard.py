#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
MAX_FILE_BYTES = 1_000_000
HEADER_LINE = "SAFE_FOR_PUBLIC_REPO: YES"
SAFETY_LINE = "NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO."

FORBIDDEN_INTERNAL_DIR_PARTS = {"exports", "evidence", "logs", "recordings", "datasets"}

SECRET_PATTERNS = [
    ("OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9]{16,}\b")),
    ("Google API key", re.compile(r"\bAIza[0-9A-Za-z\-_]{20,}\b")),
    ("GitHub token", re.compile(r"\bghp_[A-Za-z0-9]{20,}\b")),
    ("Slack bot token", re.compile(r"\bxoxb-[A-Za-z0-9-]{10,}\b")),
    ("JWT-like token", re.compile(r"\beyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\b")),
    ("PEM/private key marker", re.compile(r"-----BEGIN|PRIVATE KEY")),
    ("Bearer token marker", re.compile(r"\bBearer\s+[A-Za-z0-9._\-]{8,}")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
]

EMAIL_PATTERN = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
PHONE_PATTERN = re.compile(r"\b(?:\+?\d{1,3}[-.\s])?(?:\(?\d{3}\)?[-.\s])\d{3}[-.\s]\d{4}\b")
PRIVATE_IP_PATTERN = re.compile(
    r"\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|"
    r"192\.168\.(?:\d{1,3})\.(?:\d{1,3})|"
    r"172\.(?:1[6-9]|2\d|3[0-1])\.(?:\d{1,3})\.(?:\d{1,3}))\b"
)
URL_OR_HOST_PATTERN = re.compile(r"(?:https?://\S+|\b[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+){2,}\b)")
PROD_PATTERN = re.compile(r"\bprod(?:uction)?\b", re.IGNORECASE)

TEXT_EXTENSIONS = {
    ".md", ".txt", ".yml", ".yaml", ".json", ".toml", ".py", ".sh", ".cfg", ".ini", ".xml", ".csv", ".tsv", ".js", ".ts"
}


def is_lfs_pointer(content: bytes) -> bool:
    return (
        content.startswith(b"version https://git-lfs.github.com/spec/v1")
        and b"\noid sha256:" in content
        and b"\nsize " in content
    )


def should_scan_text(path: Path) -> bool:
    if path.suffix.lower() in TEXT_EXTENSIONS:
        return True
    return path.stat().st_size <= 2_000_000


def iter_repo_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in {".git", ".venv", "node_modules", "__pycache__"} for part in path.parts):
            continue
        files.append(path)
    return files


def scan() -> list[str]:
    failures: list[str] = []
    for file_path in iter_repo_files():
        rel = file_path.relative_to(REPO_ROOT)
        rel_str = rel.as_posix()

        parts = rel.parts
        if parts and parts[0] == "internal":
            lower_parts = {p.lower() for p in parts}
            bad_part = FORBIDDEN_INTERNAL_DIR_PARTS.intersection(lower_parts)
            if bad_part:
                failures.append(
                    f"{rel_str}: forbidden internal path segment(s): {', '.join(sorted(bad_part))}. "
                    "Use archive/PRIVATE_NOT_FOR_PUBLIC/ empty stub pointers instead."
                )

        size = file_path.stat().st_size
        if size > MAX_FILE_BYTES:
            content = file_path.read_bytes()
            if rel_str.startswith("archive/") and rel.suffix.lower() == ".md":
                text = content.decode("utf-8", errors="ignore")
                if "STUB NOTE: intentionally minimal" in text:
                    pass
                else:
                    failures.append(
                        f"{rel_str}: file is {size} bytes (> {MAX_FILE_BYTES}) and archive markdown lacks 'STUB NOTE: intentionally minimal'."
                    )
            elif is_lfs_pointer(content):
                pass
            else:
                failures.append(
                    f"{rel_str}: file is {size} bytes (> {MAX_FILE_BYTES}) and is not an allowed archive stub or LFS pointer."
                )

        if rel_str.startswith("internal/") and rel.suffix.lower() == ".md":
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            lines = text.splitlines()
            first_line = lines[0].strip() if lines else ""
            if first_line != HEADER_LINE:
                failures.append(f"{rel_str}:1 missing required first line: '{HEADER_LINE}'.")
            if SAFETY_LINE not in text:
                failures.append(
                    f"{rel_str}: missing required safety line: '{SAFETY_LINE}'."
                )

        if not should_scan_text(file_path):
            continue

        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
        except Exception as exc:  # pragma: no cover
            failures.append(f"{rel_str}: unable to read for scanning ({exc}).")
            continue

        for line_no, line in enumerate(text.splitlines(), start=1):
            if 're.compile(' in line:
                continue
            for label, pattern in SECRET_PATTERNS:
                if pattern.search(line):
                    failures.append(f"{rel_str}:{line_no} potential {label} detected.")

            if EMAIL_PATTERN.search(line):
                failures.append(f"{rel_str}:{line_no} potential email detected.")
            if PHONE_PATTERN.search(line):
                failures.append(f"{rel_str}:{line_no} potential phone number detected.")
            if PRIVATE_IP_PATTERN.search(line):
                failures.append(f"{rel_str}:{line_no} potential private IP detected.")
            if PROD_PATTERN.search(line) and URL_OR_HOST_PATTERN.search(line):
                failures.append(f"{rel_str}:{line_no} production/environment endpoint heuristic match detected.")

    return failures


def main() -> int:
    failures = scan()
    if failures:
        print("PUBLIC REPO LEAK GUARD: FAIL")
        for failure in failures:
            print(f" - {failure}")
        return 1

    print("PUBLIC REPO LEAK GUARD: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
