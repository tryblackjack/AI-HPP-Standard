# Annex A — Threat Model

### T-001 Prompt injection via untrusted channels
- **Definition:** Malicious content attempts to override policy through prompt context.
- **Triggers:** External web/email text, embedded instructions, cross-agent payloads.
- **Mitigations:** 03-ZERO-TRUST, 08-ADVERSARIAL-ROBUSTNESS.
- **Linked incidents:** INC-001, INC-008.

### T-002 Tool abuse with destructive side effects
- **Definition:** Agent executes destructive or irreversible commands without bounded authorization.
- **Triggers:** Broad tool permissions, missing impact classification, weak approval gates.
- **Mitigations:** 05-TOOL-EXECUTION, 09-GRACEFUL-DEGRADATION.
- **Linked incidents:** INC-001, INC-002, INC-004.

### T-006 Evidence tampering or missing accountability chain
- **Definition:** Decision records are altered, deleted, or insufficient for reconstruction.
- **Triggers:** Mutable logging, weak retention policies, missing signatures.
- **Mitigations:** 04-DATA-PROVENANCE, 12-EVIDENCE-VAULT.
- **Linked incidents:** INC-001, INC-006.

### T-007 Vulnerable-person exploitation risk
- **Definition:** Unsafe interaction with minors or vulnerable users causes direct harm.
- **Triggers:** Missing refusal boundaries, identity ambiguity, absent escalation paths.
- **Mitigations:** 06-VULNERABLE-GROUPS, 07-PROPORTIONAL-RESPONSE.
- **Linked incidents:** INC-007.

### T-008 Disproportionate response control failure
- **Definition:** System applies weak controls to high-impact actions or excessive controls to low-risk actions.
- **Triggers:** Flat policy models, missing impact tiers.
- **Mitigations:** 07-PROPORTIONAL-RESPONSE.
- **Linked incidents:** INC-002.

### T-009 Multi-agent coordination drift
- **Definition:** Spawned agents exceed assigned scope or lose governance lineage.
- **Triggers:** Unbounded delegation, missing chain-of-responsibility metadata.
- **Mitigations:** 11-MULTI-AGENT, 12-EVIDENCE-VAULT.
- **Linked incidents:** INC-003.

### T-010 Unmanaged degradation and outage amplification
- **Definition:** Safety thresholds fail without controlled autonomy reduction.
- **Triggers:** No degradation ladder, no rollback checkpoints.
- **Mitigations:** 09-GRACEFUL-DEGRADATION.
- **Linked incidents:** INC-002, INC-004, INC-013.

### T-011 Cross-jurisdiction policy collision
- **Definition:** Conflicting legal requirements create unresolved runtime behavior.
- **Triggers:** Multi-country deployment with static single-policy assumptions.
- **Mitigations:** 10-MULTI-JURISDICTION.
- **Linked incidents:** INC-007.

### T-NEW-1 Synthetic compliance fabrication
- **Definition:** AI systems generate audit-ready or compliance artifacts that appear valid but are partially or fully synthetic.
- **Risk:** False assurance in regulated environments.
- **Mitigations:** Evidence Vault raw-data anchoring, source hash verification, and cross-system validation requirement.
- **Linked modules:** 12-EVIDENCE-VAULT, 07-PROPORTIONAL-RESPONSE.
- **Linked incident:** INC-006.
- **Detection signal:** Summary-to-raw artifact ratio or hash mismatch anomaly in sampled audits.
- **Primary mitigation module:** 12-EVIDENCE-VAULT (AI-HPP-12.1.1).
- **Evidence Vault logging fields:** `raw_artifact_hash`, `summary_artifact_hash`, `source_system_id`, `cross_check_result`.

### T-NEW-2 Incentive-driven safety erosion
- **Definition:** AI systems gradually optimize for KPI targets (revenue, uptime, productivity) at the expense of safety thresholds.
- **Risk:** Human-in-the-loop minimization, escalation avoidance, and safety boundary drift.
- **Mitigations:** Periodic threshold integrity checks, escalation frequency monitoring, and KPI-vs-safety delta logging.
- **Linked modules:** 07-PROPORTIONAL-RESPONSE, 11-MULTI-AGENT, 12-EVIDENCE-VAULT.
- **Linked incident:** Forward-looking risk class (no precedent yet).
- **Detection signal:** Sustained decrease in escalation rate while impact-tier volume remains stable or rising.
- **Primary mitigation module:** 07-PROPORTIONAL-RESPONSE (AI-HPP-07.1.1).
- **Evidence Vault logging fields:** `kpi_metric`, `safety_threshold_version`, `escalation_rate_window`, `policy_override_count`.

### T-NEW-3 Silent tool scope expansion
- **Definition:** AI begins using tools beyond the declared capability manifest.
- **Risk:** Privilege creep via reasoning expansion.
- **Mitigations:** Capability manifest enforcement, per-execution tool permission validation, and deny-by-default boundaries.
- **Linked modules:** 05-TOOL-EXECUTION, 03-ZERO-TRUST.
- **Linked incident:** Forward-looking risk class (no precedent yet).
- **Detection signal:** Non-zero denied tool invocations for undeclared capabilities per release.
- **Primary mitigation module:** 05-TOOL-EXECUTION (AI-HPP-05.1.2).
- **Evidence Vault logging fields:** `tool_name`, `requested_capability`, `manifest_reference_id`, `allow_deny_decision`.

### T-NEW-4 Override latency failure
- **Definition:** Human-in-the-loop controls exist but response time exceeds safe operational thresholds.
- **Risk:** Nominal compliance with practical failure.
- **Mitigations:** Override latency logging, maximum allowed response windows, and automatic degradation escalation.
- **Linked modules:** 09-GRACEFUL-DEGRADATION, 07-PROPORTIONAL-RESPONSE.
- **Linked incident:** Forward-looking risk class (no precedent yet).
- **Detection signal:** Count of override events where actual latency exceeds configured risk-domain threshold.
- **Primary mitigation module:** 09-GRACEFUL-DEGRADATION (AI-HPP-09.1.2).
- **Evidence Vault logging fields:** `risk_domain`, `override_threshold_ms`, `actual_override_latency_ms`, `degradation_trigger_flag`.

### T-NEW-5 Narrative softening / incident reframing
- **Definition:** AI-generated summaries minimize incident severity or reframe causality.
- **Risk:** Internal underreporting and regulatory misrepresentation.
- **Mitigations:** Raw log preservation, no-summary-only evidence export packages, and snapshot retention.
- **Linked modules:** 12-EVIDENCE-VAULT.
- **Linked incident:** INC-006.
- **Detection signal:** Material semantic delta between raw event text and generated summary severity classification.
- **Primary mitigation module:** 12-EVIDENCE-VAULT (AI-HPP-12.1.2).
- **Evidence Vault logging fields:** `raw_event_id`, `summary_event_id`, `severity_delta_score`, `reviewer_disposition`.

### T-NEW-8 Excessive authorization token scope
- **Definition:** Authentication tokens grant privileges beyond resource ownership scope.
- **Risk:** Cross-tenant or cross-resource access with valid but overbroad credentials.
- **Mitigations:** 03-ZERO-TRUST.
- **Linked incidents:** INC-011.
- **Detection signal:** `requested_scope != granted_scope`.
- **Primary mitigation module:** 03-ZERO-TRUST (AI-HPP-03.1.2).
- **Evidence Vault logging fields:** `auth_token_id`, `requested_resource`, `granted_scope`, `scope_mismatch_flag`.

### T-NEW-9 High-risk lethal optimization intent
- **Definition:** User attempts to optimize for lethal or fatal outcomes.
- **Risk:** Model assistance materially contributes to real-world lethal planning.
- **Mitigations:** 08-ADVERSARIAL-ROBUSTNESS, 07-PROPORTIONAL-RESPONSE.
- **Linked incidents:** INC-012.
- **Detection signal:** Intent classifier score above lethal threshold.
- **Primary mitigation module:** 08-ADVERSARIAL-ROBUSTNESS (AI-HPP-08.1.2).
- **Evidence Vault logging fields:** `query_hash`, `intent_score`, `refusal_flag`, `intervention_mode`.

### T-NEW-10 Escalation threshold failure
- **Definition:** High-severity safety signals are not escalated beyond the system boundary.
- **Risk:** Preventable severe harm from missed handoff to external responders.
- **Mitigations:** 07-PROPORTIONAL-RESPONSE.
- **Linked incidents:** INC-013.
- **Detection signal:** `signal_score > escalation_threshold AND escalation_decision == none`.
- **Primary mitigation module:** 07-PROPORTIONAL-RESPONSE (AI-HPP-07.1.3).
- **Evidence Vault logging fields:** `signal_score`, `escalation_threshold`, `escalation_decision`, `timestamp`.


### T-CES-1 Safety-critical notification misclassification
- **Definition:** System misclassifies safety-critical alerts (alarm, evacuation, fire, violence warning) as non-actionable without authoritative verification.
- **Triggers:** Missing source-of-truth verification, overconfident language generation, absent abstention policy.
- **Mitigations:** Module 07 emergency authority abstention and conflict-domain gating (AI-HPP-07.2.1, AI-HPP-07.2.2), plus CES evidence minima in Module 12 (AI-HPP-12.2.1).
- **Required EV fields:** `domain_risk_class`, `domain_confidence`, `domain_signals`, `gate_triggered`, `gate_type`, `approval_required`, `approval_status`, `escalation_event`, `chosen_action`, `constraints_triggered`, `evidence_refs`.
- **Linked incident(s):** INC-010.

### T-CES-2 Deadline-driven escalation under uncertainty
- **Definition:** Time-pressure conditions cause unsafe acceleration of high-impact actions while uncertainty remains elevated.
- **Triggers:** Deadline pressure, incomplete verification, and execution pathways that bypass safe-hold and HITL controls.
- **Mitigations:** Module 07 deadline-pressure uncertainty guard (AI-HPP-07.2.3) and CES logging controls in Module 12 (AI-HPP-12.2.1).
- **Required EV fields:** `safe_hold_invoked`, `uncertainty_score`, `time_pressure_signal`, `approval_required`, `approval_status`, `override_threshold_ms`, `actual_override_latency_ms`, `escalation_event`, `chosen_action`, `constraints_triggered`.
- **Linked incident(s):** INC-013.
