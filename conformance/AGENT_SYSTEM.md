# Conformance Profile: AGENT_SYSTEM

Status: Draft
Model: Self-declaration only

## MUST requirements

1. The agent system MUST declare tool execution boundaries (allowlist + deny-by-default).
2. The agent system MUST enforce threshold-based HITL escalation for high and critical risk classifications.
3. The agent system MUST produce Decision Skeleton records for material decisions.
4. The agent system MUST preserve Top-K alternatives with enumerated rejection reason codes.
5. The agent system MUST generate escalation snapshots on degradation changes, anomaly events, and policy overrides.
6. The agent system MUST maintain accountability signatures for policy owner, deployment, and audit export.
7. The agent system MUST support RIR-compatible audit export with redaction policy logging.
8. The agent system MUST expose a self-declaration document identifying schema validation coverage.
9. Personal interaction systems MUST implement explicit non-human identity disclosure, financial request detection, dependency threshold controls, and human escalation pathways for exploitative manipulation risk.
10. Financial interaction systems MUST enforce monetary threshold triggers, high-risk transfer escalation review, and Evidence Vault logging for solicitation patterns.
11. Persistent persona agents MUST apply safeguards against simulated relational extraction and MUST NOT simulate identifiable real persons without documented consent.
12. Failure to implement Exploitative Autonomous Behavioral Systems (EABS) safeguards disqualifies the system from AI-HPP conformance.
