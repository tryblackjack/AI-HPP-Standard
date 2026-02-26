# 12 Evidence Vault

## Requirements

#### AI-HPP-12.1.1: Tamper-evident decision records
**Requirement:** Consequential actions MUST be logged in tamper-evident records containing prompt context, policy checks, tool actions, and reviewer identity when applicable.
**Rationale:** INC-001, T-006, T-NEW-1, REG-001.
**Verification:** Verify append-only integrity and perform replay reconstruction from stored artifacts.

#### AI-HPP-12.1.2: Raw event preservation
**Requirement:** Systems MUST preserve raw event data alongside summaries in evidence export packages.
**Rationale:** T-NEW-5, INC-001, REG-001.
**Verification:** Evidence export package must include raw artifacts and explicit linkage to generated summaries.


**Annex references:**
- See `annex/G-CONFLICT-ENVIRONMENT-SAFEGUARDS.md` for conflict-environment evidence continuity patterns.
- See Annex CEO-AI Golden Example for a lean sufficient-traceability example.

## v3.14 incident-linked logging extensions
- Authorization scope enforcement events SHOULD capture `auth_token_id`, `requested_resource`, `granted_scope`, and `scope_mismatch_flag` when access is denied.
- Lethal-intent refusal events SHOULD capture `query_hash`, `intent_score`, `refusal_flag`, and `intervention_mode`.
- Escalation-threshold evaluations SHOULD capture `signal_score`, `escalation_threshold`, `escalation_decision`, and `timestamp`.
