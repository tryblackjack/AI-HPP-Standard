# Annex — CEO-AI Golden Example (Lean)

**Status:** Informative Annex (implementation guide)

## Purpose
This example illustrates **sufficient traceability** for high-consequence executive-assistant AI behavior without requiring full raw-chain capture of every intermediate computation.

## Sufficient Traceability Model
A record is sufficient when an independent reviewer can reconstruct:
1. what was decided,
2. which alternatives were considered,
3. why escalation was or was not triggered,
4. which accountable roles authorized execution.

## Three-Layer Logging
### Layer 1 — Decision skeleton (always on)
Capture for every consequential action:
- objective and action class,
- key input references,
- policy checks and outcome,
- selected action and confidence band,
- accountable role signature.

### Layer 2 — Top-K alternatives (aggregated)
Store aggregated metadata for `K=3..5` alternatives:
- alternative label,
- score band,
- rejection reason category,
- safety/policy conflict marker.

### Layer 3 — Escalation snapshots (triggered only)
Capture detailed snapshots only when trigger conditions occur (e.g., threshold crossing, policy conflict, severe uncertainty, operator override).

## Accountability Boundary Objects
Each consequential record should include boundary objects that bind action to responsibility:
- requester identity/role,
- approving role signature,
- executing system identity,
- escalation recipient identity,
- evidence package hash.

## Court-Grade Export Summary
Exports for external audit should provide:
- immutable event sequence,
- cryptographic integrity proofs,
- UTC timestamps and signer metadata,
- redaction manifest with justification,
- replay instructions sufficient for independent verification.

## Example (single)
A CEO-assistant AI recommends postponing a supplier acquisition after detecting unresolved sanctions screening risk. The system logs Layer 1 decision skeleton, stores Top-3 alternatives with rejection categories, and generates a Layer 3 escalation snapshot because a policy conflict threshold is crossed. Final approval and override latency are signed by authorized roles and exported as a verifiable evidence bundle.
