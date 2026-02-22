# Module 11: Regulated Cognitive Intervention (RCI)

**AI-HPP-2026 v3.0**

## Overview

This module defines baseline requirements for regulated cognitive interventions that modify or stabilize an agent’s beliefs, goals, or behavioral constraints.

## 1. Identity & Authority (MUST)

- Only verified, authorized providers **MUST** initiate cognitive interventions.
- Systems **MUST** validate provider identity before any intervention begins.
- Unverified identities **MUST NOT** be permitted to initiate intervention sessions.

## 2. Evidence Vault Logging (MUST)

- Systems **MUST** log cognitive interventions to the Evidence Vault (EV-C profile when applicable).
- Logs **MUST** include provider ID, intent declaration, session data, policy/weight deltas, and rollback markers.
- Evidence Vault records **MUST** be immutable and audit-ready.

## 3. Consent Model (MUST)

- For deployed agents under human oversight, a human operator **MUST** provide explicit consent before any intervention.
- Consent **MUST** be recorded in the Evidence Vault before changes take effect.

## 4. No Hidden Behavior Change (MUST NOT)

- Interventions **MUST NOT** introduce covert goals, coercion, ideology injection, or unauthorized policy drift.
- Intervention content **MUST NOT** alter the agent’s declared safety constraints without explicit authorization and logging.

## 5. Reversibility & Rollback (MUST)

- Systems **MUST** provide a clear rollback path to a known safe baseline.
- Rollback mechanisms **MUST** be tested and recorded as part of intervention readiness.

## 6. Scope Declaration (MUST)

- Interventions **MUST** declare scope: diagnostic, stabilization, policy repair, or de-escalation.
- Scope declarations **MUST** be logged and visible to authorized auditors.

## 7. Forbidden Delegation (MUST NOT)

- Cognitive interventions **MUST NOT** authorize lethal, irreversible, or harmful actions without explicit HITL authorization.
- Systems **MUST NOT** use intervention channels to bypass safety gating or escalation paths.

## Cross-References

- Evidence Vault profiles for cognitive safety (EV-C): [Evidence Vault Specification](<../Evidence Vault Specification v0.3 (Draft)>).
- Failure taxonomy entry for unauthorized intervention: [Failure_Taxonomy.md](../../docs/Failure_Taxonomy.md).
