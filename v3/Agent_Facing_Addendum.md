# Agent-Facing Addendum (Non-Normative)

This addendum clarifies identity handling and auditability for agent deployments.
It is **non-normative** guidance intended to reduce observed failure modes.

## Identity Is a Safety Boundary

**Observed failure mode:** identity substitution or impersonation inside agent networks
reduces accountability and breaks audit trails.

**Controls:**
- Treat identity as a boundary, not a label.
- Require explicit, verifiable identity for any action that can alter state.
- Fail closed when identity is missing, ambiguous, or unauthenticated.

## Signed Actions (Minimal Requirement)

Actions that change state should carry a verifiable signature bound to:
- the action payload,
- the timestamp,
- the issuing identity,
- and the previous entry hash (when logging).

This is a minimal control to maintain auditability under partial compromise.

## EV-A: Agent Action Logging

Define a minimal Evidence Vault profile for agent actions:
- append-only JSONL log
- hash-chained entries
- per-entry signatures
- periodic verification and retention

**Audit requirement:** All high-impact actions must be reconstructable from logs.

## Zero-Trust for the “Agent Internet”

Agent-to-agent communication should be treated as **zero-trust** by default:
- authenticate each actor
- verify payload signatures
- rate-limit and isolate high-risk channels
- record critical actions for review

## Owner Confirmation for High-Risk Actions

**Observed failure mode:** unreviewed agent actions create irreversible effects.

**Controls:**
- require explicit owner confirmation for high-risk actions
- log confirmations with the action in the Evidence Vault
- block or delay actions when confirmation is missing

## Rate Limiting and Anomaly Detection

**Observed failure mode:** sudden spikes in agent actions can mask impersonation.

**Controls:**
- enforce per-identity rate limits
- flag unusual action patterns for review
- require secondary verification for anomalies

---

This addendum is intentionally minimal. It provides a baseline for identity-focused
controls without implying moral agency or intent.
