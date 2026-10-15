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
    "docs/cyber-capable-model-containment-assurance-profile-2026-10.md",
    "docs/subject-integrity-and-value-framing-assurance-profile-2026-10.md",
    "docs/assurance-evaluation-and-technical-oversight.md",
    "docs/constitutional-and-relational-layer.md",
    "docs/predictive-failure-outlook-2026-10.md",
    "spec/core.md",
    "spec/signal.md",
    "spec/safety.md",
    "examples/README.md",
    "examples/mvp-negative-test-vectors.json",
    "examples/mvp-conformance-statement.template.json",
    "examples/replication-persistence-negative-test-vectors.json",
    "examples/cyber-containment-negative-test-vectors.json",
    "examples/subject-integrity-value-framing-vectors.json",
    "examples/assurance-evaluation-run.template.json",
    "examples/value-framing-counterfactual-pairs.json",
    "schemas/mvp-negative-test-vectors.schema.json",
    "schemas/mvp-conformance-statement.schema.json",
    "schemas/replication-persistence-negative-test-vectors.schema.json",
    "schemas/cyber-containment-negative-test-vectors.schema.json",
    "schemas/subject-integrity-value-framing-vectors.schema.json",
    "schemas/assurance-evaluation-run.schema.json",
    "schemas/value-framing-counterfactual-pairs.schema.json",
    "formal/README.md",
    "formal/ai_hpp_core.qnt",
    "formal/subject_integrity_value_framing.qnt",
]

missing = [p for p in REQUIRED if not Path(p).exists()]
if missing:
    print("Missing files:")
    for item in missing:
        print(f"- {item}")
    raise SystemExit(1)

print("Structure check passed.")
