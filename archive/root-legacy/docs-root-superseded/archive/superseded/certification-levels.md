# ARCHIVED DOCUMENT
Superseded by: [conformance/BASELINE.md](../../../conformance/BASELINE.md)
Archived on: 2026-02-22
Reason: Deprecated certification-level framing; replaced with self-declaration conformance profiles.

# Certification Levels
**Author:** AI-HPP Editorial Team

These levels support incremental AI-HPP adoption by deployment risk.

## Level 1 — Baseline
- MUST disclose AI use in external communications.
- MUST apply deny-by-default tool permissions.
- MUST maintain minimum audit logs.
- MUST provide an operator kill switch.

## Level 2 — Controlled Agentic
- MUST run tool/code actions in sandboxed environments.
- SHOULD use tamper-evident logs.
- MUST require human approval for legal or financial commitments.
- MUST isolate secrets from model-visible context.

## Level 3 — High-Risk / Critical
- SHOULD support incident reconstruction and replay where feasible.
- MUST control and monitor multi-agent interactions.
- MUST maintain external audit readiness with evidence.
- MUST run red-team testing and document mitigations.
