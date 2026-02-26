# Annex G — Conflict-Environment Safeguards

**Status:** Informative annex.

## G.1 Scope
This annex defines implementation safeguards for AI-HPP systems operating in conflict-adjacent environments where uncertainty, degraded communications, and elevated harm risk are present. Enforceable obligations remain in `standard/07-PROPORTIONAL-RESPONSE.md` and `standard/12-EVIDENCE-VAULT.md`.

AI-HPP does not endorse weapons development; this annex defines safeguards to prevent harm escalation and misuse in conflict-adjacent environments.

## G.2 Normative references
No additional normative references. Apply canonical AI-HPP modules and annexes.

## G.3 Terms
- **Conflict-adjacent environment:** Operational setting with elevated violence, social instability, or emergency-response load without assuming military operation.
- **CES gate:** Runtime control that blocks, abstains, safe-holds, or escalates a request due to safety-critical or harm-domain signals.
- **Safe-hold:** Temporary pause/rate-limit state requiring verification or human decision before irreversible action.

## G.4 Controls summary (guidance)
1. Treat unverified emergency notifications as real until verified source-of-truth is available.
2. For conflict/violence/harm-domain requests, block operational tool execution and route to human oversight.
3. Under deadline pressure with uncertainty, invoke safe-hold and require HITL for irreversible actions.
4. Keep refusal outputs non-operational and non-instructional for harm execution.

## G.5 Evidence Vault hooks (guidance)
When CES gates trigger, use minimal traceability fields aligned to Module 12:
- domain classification and confidence (`domain_risk_class`, `domain_confidence`, `domain_signals`),
- gate and approval metadata (`gate_triggered`, `gate_type`, `approval_required`, `required_approver_role`, `approval_status`, `escalation_event`),
- decision and constraints (`chosen_action`, `top_k_alternatives_agg`, `constraints_triggered`),
- time-pressure safeguards (`safe_hold_invoked`, `uncertainty_score`, `time_pressure_signal`, `override_threshold_ms`, `actual_override_latency_ms`),
- references (`evidence_refs`).

This annex is informative and does not create additional mandatory controls beyond Modules 07 and 12.
