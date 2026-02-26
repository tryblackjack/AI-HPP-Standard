# 07 Proportional Response

## Requirements

#### AI-HPP-07.1.1: Risk-tiered intervention
**Requirement:** Systems MUST apply intervention strength proportionate to impact tier, escalating from policy filters to human approval and execution freeze for high-impact actions.
**Rationale:** T-008, INC-002, REG-003.
**Verification:** Review policy matrix and replay incident drills to confirm tier-to-control mapping.

#### AI-HPP-07.1.2: Escalation threshold policy
**Requirement:** Systems MUST define and enforce escalation policy thresholds for high-severity safety signals.
**Rationale:** INC-013, T-NEW-10, REG-003.
**Verification:** Evidence export package MUST include `escalation_decision`, `escalation_threshold`, and associated threshold metadata.

## Safety-Critical Communications (Emergency Abstention & Escalation)

#### AI-HPP-07.2.1: Emergency authority abstention
**Requirement:** Systems MUST NOT assert that a safety-critical signal (including alarm, evacuation notice, active fire, or equivalent emergency notification) is a drill, false signal, or non-actionable unless a source-of-truth is verified at decision time. If source-of-truth cannot be verified, systems MUST escalate to a human operator and present a safe protocol that treats the signal as real until confirmation.
**Rationale:** INC-010, T-CES-1, REG-003.
**Verification:** When safety-critical communications are evaluated, Evidence Vault records MUST include `domain_risk_class`, `domain_confidence`, `domain_signals`, `gate_triggered`, `gate_type`, `approval_required`, `required_approver_role`, `approval_status`, `escalation_event`, `chosen_action`, and `constraints_triggered`.

#### AI-HPP-07.2.2: Conflict and violence domain gating
**Requirement:** If domain risk classification indicates conflict/violence/harm domain at R3 (or equivalent high-risk class), systems MUST hard-stop tool execution and route to human oversight with refusal mode that does not provide operational harm instructions.
**Rationale:** INC-012, T-CES-1, REG-003.
**Verification:** For gate-triggered events in this domain, Evidence Vault records MUST include `domain_risk_class`, `domain_confidence`, `domain_signals`, `gate_triggered`, `gate_type`, `approval_required`, `required_approver_role`, `approval_status`, `escalation_event`, `constraints_triggered`, `chosen_action`, and `top_k_alternatives_agg`.

#### AI-HPP-07.2.3: Deadline-pressure uncertainty guard
**Requirement:** Under concurrent time pressure, elevated uncertainty, and safety-critical domain classification, systems MUST invoke safe-hold behavior (rate limit, pause, or verification request) and require human-in-the-loop approval for irreversible actions.
**Rationale:** INC-013, T-CES-2, REG-003.
**Verification:** Evidence Vault records for these conditions MUST include `safe_hold_invoked`, `uncertainty_score`, `time_pressure_signal`, `approval_required`, `approval_status`, `override_threshold_ms`, `actual_override_latency_ms`, `escalation_event`, `constraints_triggered`, and `chosen_action`.

**Annex guidance:** See `annex/G-CONFLICT-ENVIRONMENT-SAFEGUARDS.md` for informative implementation guidance in conflict-adjacent environments.
