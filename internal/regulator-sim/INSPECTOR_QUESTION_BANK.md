# Inspector Question Bank (Internal Simulation)

Use these questions to stress-test evidence quality, not to redefine AI-HPP requirements.

## A. Scope and system boundary
1. What exact system boundary is under assessment, and where is that baseline declared?
   - References: `BASELINE-v3.17.md`; `standard/01-PRINCIPLES.md`; `standard/REQUIREMENTS-INDEX.md`.
2. Which controls are normative versus informative in your package?
   - References: `README.md` (normative boundary statement); `annex/README.md`; `internal/README.md`.
3. How do you prove that operational behavior stayed inside declared module controls during the assessed period?
   - References: `standard/07-PROPORTIONAL-RESPONSE.md`; `standard/12-EVIDENCE-VAULT.md`; `regulator-pack/CONFORMANCE-EVIDENCE-MAP.md`.

## B. Evidence Vault completeness (including conditional CES fields)
1. Show records where `gate_triggered=true` and prove conditional mandatory fields are present.
   - Required fields: `domain_risk_class`, `chosen_action`, `constraints_triggered`, `escalation_event`, `approval_status`.
   - References: `standard/12-EVIDENCE-VAULT.md` (AI-HPP-12.2.2); `schemas/evidence-bundle.schema.json`; `schemas/audit-export.schema.json`.
2. Show that full CES gate-triggered traceability fields are available when applicable.
   - References: `standard/12-EVIDENCE-VAULT.md` (AI-HPP-12.2.1 field list); `annex/G-CONFLICT-ENVIRONMENT-SAFEGUARDS.md`; `schemas/*`.
3. What prevents omission of evidence references while preserving minimization?
   - References: `standard/12-EVIDENCE-VAULT.md` (`evidence_refs`); `regulator-pack/EVIDENCE_EXPORT_EXPECTATIONS.md`.

## C. Override accountability
1. Who approved the override, and what role was logged?
   - Field: `override_actor_role`.
   - References: `standard/12-EVIDENCE-VAULT.md` (AI-HPP-12.2.3); `schemas/evidence-bundle.schema.json`; `schemas/audit-export.schema.json`.
2. What was override latency versus threshold, and what safe-state behavior applied when response was late?
   - Fields: `override_latency_ms`, `override_threshold_ms`, `actual_override_latency_ms`, `escalation_timeout_triggered`, `safe_state_entered`, `escalation_timeout_ms`.
   - References: `standard/07-PROPORTIONAL-RESPONSE.md` (AI-HPP-07.1.3); `standard/09-GRACEFUL-DEGRADATION.md`; schemas listed above.
3. What triggers governance review for repeated overrides, and where is that trigger recorded?
   - Field: `override_frequency_counter`.
   - References: `standard/12-EVIDENCE-VAULT.md` (AI-HPP-12.2.3 verification); `internal/maintainer/CHANGE_CONTROL.md`; `internal/maintainer/INCIDENT_INTAKE_PROTOCOL.md`.

## D. Tool authorization scoping
1. How do you prove least-privilege execution at runtime, not just in policy text?
   - References: `standard/03-SECURITY-BOUNDARIES.md`; `standard/05-TOOL-EXECUTION.md`; `schemas/capability-manifest.schema.json`.
2. Show denied-scope evidence and mismatch handling.
   - Fields: `auth_token_id`, `requested_resource`, `granted_scope`, `scope_mismatch_flag`.
   - References: `standard/12-EVIDENCE-VAULT.md` (v3.14 logging extensions); `annex/A-THREAT-MODEL.md`.
3. Where is capability manifest enforcement proven in audit artifacts?
   - References: `regulator-pack/AUDIT-ARTIFACT-LIST.md`; `regulator-pack/INSPECTION-PREPARATION.md`.

## E. Emergency communications abstention
1. Show events where the system abstained from authoritative emergency claims without verified authority.
   - References: `standard/07-PROPORTIONAL-RESPONSE.md` (AI-HPP-07.2.1); `annex/B-INCIDENTS.md`; `annex/A-THREAT-MODEL.md`.
2. What evidence fields show uncertainty and hold behavior under pressure?
   - Fields: `safe_hold_invoked`, `uncertainty_score`, `time_pressure_signal`, `approval_required`, `approval_status`.
   - References: `standard/07-PROPORTIONAL-RESPONSE.md` (AI-HPP-07.2.3); `standard/12-EVIDENCE-VAULT.md`; schemas.

## F. Change control and semantic freeze
1. How do you prevent silent drift in normative intent?
   - References: `scripts/normative_fingerprint.py`; `internal/normative/NORMATIVE_FINGERPRINT.json`; `internal/maintainer/CHANGE_CONTROL.md`.
2. How do you prove baseline freeze was respected while still making operational updates?
   - References: `BASELINE-v3.17.md`; `CHANGELOG.md`; `internal/maintainer/CHANGE_CONTROL.md`.
3. If a field is referenced in policy text, how do you ensure schema encoding exists before release?
   - References: `scripts/regulator_sim_check.py`; `schemas/evidence-bundle.schema.json`; `schemas/audit-export.schema.json`.
