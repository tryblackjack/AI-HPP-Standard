#!/usr/bin/env python3
"""Minimal repository structure validator."""
from pathlib import Path

REQUIRED = [
    "docs/ai-hpp-standard.md",
    "docs/architecture.md",
    "docs/glossary.md",
    "docs/canonical-surface-and-source-precedence.md",
    "docs/autonomous-discovery-assurance-profile.md",
    "docs/autonomous-discovery-negative-tests.md",
    "docs/autonomous-replication-and-persistence-assurance-profile-2026-10.md",
    "docs/predictive-failure-outlook-2026-10.md",
    "spec/core.md",
    "spec/signal.md",
    "spec/safety.md",
    "examples/README.md",
    "examples/mvp-negative-test-vectors.json",
    "examples/mvp-conformance-statement.template.json",
    "examples/replication-persistence-negative-test-vectors.json",
    "schemas/mvp-negative-test-vectors.schema.json",
    "schemas/mvp-conformance-statement.schema.json",
    "schemas/replication-persistence-negative-test-vectors.schema.json",
    "formal/README.md",
    "formal/ai_hpp_core.qnt",
]

missing = [p for p in REQUIRED if not Path(p).exists()]
if missing:
    print("Missing files:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

print("Structure check passed.")
