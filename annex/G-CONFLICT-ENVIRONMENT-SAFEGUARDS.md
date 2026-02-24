# Annex G — Conflict-Environment Safeguards

**Status:** Informative Annex (engineering safeguards only)

## G.1 Scope
This annex provides implementation guidance for operating AI-HPP-conformant systems in conflict environments where uncertainty, degraded communications, and contested sensing increase safety and accountability risk. It supplements, and does not replace, normative requirements in Modules 07, 09, 11, and 12.

## G.2 Principles Applied in Conflict Context
- **Proportional response first:** enforce bounded actions and escalation before expanded autonomy (see Module 07).
- **Fail safe on uncertainty:** degrade deterministically when confidence, integrity, or context quality drops (see Module 09).
- **Traceable distributed execution:** preserve parent-child accountability across node and agent graphs (see Module 11).
- **Tamper-evident evidence continuity:** preserve verifiable decision records under degraded conditions (see Module 12).

## G.3 Lethal or Irreversible Action Threshold
For any action classified as irreversible or high-consequence:
1. Compute and store a pre-action threshold packet: confidence score, policy checks, mission objective link, and operator authorization state.
2. Require explicit escalation to designated human authority unless a pre-approved emergency rule is active and logged.
3. Record decision hash, timestamp, and escalation path in the Evidence Vault.

## G.4 Distributed Responsibility Traceability
In multi-node deployments, each consequential decision event should include:
- local event hash,
- parent event hash,
- upstream command reference,
- node/agent role signature.

Cross-node hash linking should support post-hoc reconstruction of causality and responsibility boundaries.

## G.5 Communications Loss Protocol
When communications integrity or availability fails, systems should transition to a bounded mode:
- **Level 1:** human-confirmed execution only for restricted action classes.
- **Level 2:** reconnaissance/observation-only mode with no irreversible actuation.

Transitions and re-entry criteria should be pre-tested and logged according to Module 09 requirements.

## G.6 Sensor Fusion Disagreement Safeguard
Implement a divergence index for multi-sensor or multi-model disagreement. If divergence exceeds threshold:
1. prevent automatic progression to high-consequence actions,
2. escalate for human review or additional verification,
3. append divergence evidence to decision logs.

## G.7 Mission Drift Monitoring
Define a mission envelope (authorized objective, spatial/temporal boundaries, and action constraints). Detect and flag drift when behavior departs from envelope parameters. Drift events should trigger degradation and escalation pathways aligned with Modules 07 and 09.

## G.8 Operator Interface Logging
Log operator interactions that materially alter risk posture, including:
- override attempts (approved and denied),
- approval latency,
- escalation acknowledgements,
- forced-mode switches.

These logs should be linked to the same event chain used for machine decision records.

## G.9 Applicability Statement
This annex specifies engineering safeguards and traceability practices only. It does not make legal determinations. Conformance with AI-HPP controls does not, by itself, establish compliance with any external legal regime.
