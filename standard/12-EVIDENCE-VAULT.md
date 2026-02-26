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


## CES Logging: Minimal Traceability for Safety-Critical & Conflict Domains

#### AI-HPP-12.2.1: CES gate evidence bundle minimum
**Requirement:** When CES controls in Module 07 trigger (`gate_triggered=true`), evidence bundles MUST include domain classification, gate triggers, escalation metadata, chosen action, constraints triggered, and aggregated top-K alternatives. Systems MUST use aggregated evidence for high-frequency operation and MUST NOT require full per-decision raw logging at production event rates.
**Rationale:** INC-010, INC-013, T-CES-1, T-CES-2, REG-001.
**Verification:** Validate gate-triggered records include `domain_risk_class`, `domain_confidence`, `domain_signals`, `gate_triggered`, `gate_type`, `approval_required`, `required_approver_role`, `approval_status`, `escalation_event`, `chosen_action`, `top_k_alternatives_agg`, `constraints_triggered`, `safe_hold_invoked`, `uncertainty_score`, `time_pressure_signal`, `override_threshold_ms`, `actual_override_latency_ms`, and `evidence_refs`.

#### AI-HPP-12.2.2: Conditional mandatory CES fields
**Requirement:** Evidence Vault schemas may remain optional at global deployment scope; however, when CES activation occurs (`gate_triggered=true`), records MUST include `domain_risk_class`, `chosen_action`, `constraints_triggered`, `escalation_event`, and `approval_status` as conditionally mandatory fields.
**Rationale:** INC-010, INC-013, T-CES-1, REG-001.
**Verification:** Validate that every record with `gate_triggered=true` includes all conditionally mandatory CES fields; records with `gate_triggered=false` MAY omit them.

#### AI-HPP-12.2.3: Override accountability logging and review trigger
**Requirement:** When a human override is exercised, systems MUST log `override_actor_role`, `override_reason_code`, `override_latency_ms`, and `override_frequency_counter`. Repeated override frequency above an implementation-defined threshold MUST trigger governance review.
**Rationale:** INC-013, T-NEW-10, REG-001.
**Verification:** Inspect override event logs for all required fields and verify the governance workflow defines a threshold and emits a review trigger when the threshold is exceeded.

### CES minimal field set (gate-triggered context)
- `domain_risk_class`
- `domain_confidence`
- `domain_signals`
- `gate_triggered`
- `gate_type`
- `approval_required`
- `required_approver_role`
- `approval_status` (`requested|approved|rejected|timeout`)
- `escalation_event`
- `chosen_action`
- `top_k_alternatives_agg` (K=3..5 aggregated alternatives)
- `constraints_triggered`
- `safe_hold_invoked`
- `uncertainty_score` (0..1)
- `time_pressure_signal`
- `override_threshold_ms`
- `actual_override_latency_ms`
- `evidence_refs`

### Conditional CES mandatory fields (`gate_triggered=true`)
- `domain_risk_class`
- `chosen_action`
- `constraints_triggered`
- `escalation_event`
- `approval_status`

### Human override accountability fields
- `override_actor_role`
- `override_reason_code`
- `override_latency_ms`
- `override_frequency_counter`

> Note: `top_k_alternatives_agg` stores structured short-form rationale only and MUST NOT contain verbatim chain-of-thought.
