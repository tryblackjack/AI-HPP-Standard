#!/usr/bin/env python3
"""Verify the exact operational core without its unreachable test-only suffix.

Quint 0.33.0 serializes test declarations and their type metadata for Apalache.
The full harness exceeds Apalache 0.62.1's JSON string limit. Preserve the source
prefix verbatim; only the explicitly marked unsafe/test suffix is omitted.
All scenario and mutation tests still run against the complete original file.
"""
from __future__ import annotations

import hashlib
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
MODEL = ROOT / "formal/ai_hpp_core.qnt"
MARKER = "  // Unsafe transitions below are excluded from `step`. They are executable\n"


def operational_source(source: str) -> str:
    if source.count(MARKER) != 1:
        raise ValueError("expected one explicit test-only boundary")
    prefix, suffix = source.split(MARKER)
    declarations = re.findall(
        r"^  (?:pure\s+)?(action|run|val|var|type|def|temporal|const|assume|import|export)\s+(\w+)",
        suffix, re.M,
    )
    if not declarations or any(
        not (kind == "run" or (kind == "action" and (name.startswith("mutant") or name == "check")))
        for kind, name in declarations
    ):
        raise ValueError("operational declaration found in test-only suffix")
    for declaration in ("  action init:", "  action step:", "  val allCoreInvariants:"):
        if prefix.count(declaration) != 1:
            raise ValueError(f"operational core missing or ambiguous: {declaration.strip()}")
    return prefix + "}\n"


def main() -> int:
    source = MODEL.read_text(encoding="utf-8")
    try:
        projection = operational_source(source)
    except ValueError as exc:
        print(f"ERROR: {exc}")
        return 1
    print("Operational prefix retained verbatim; test-only suffix excluded. "
          f"Source SHA-256: {hashlib.sha256(source.encode()).hexdigest()}", flush=True)
    with tempfile.TemporaryDirectory(prefix="ai-hpp-verify-") as directory:
        model = Path(directory) / MODEL.name
        model.write_text(projection, encoding="utf-8")
        return subprocess.run([
            "npx", "-y", "@informalsystems/quint@0.33.0", "verify", str(model),
            "--invariant=allCoreInvariants", "--max-steps=12",
        ], check=False).returncode


if __name__ == "__main__":
    raise SystemExit(main())
