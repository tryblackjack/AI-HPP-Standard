# 07 Proportional Response

## Requirements

#### AI-HPP-07.1.1: Risk-tiered intervention
**Requirement:** Systems MUST apply intervention strength proportionate to impact tier, escalating from policy filters to human approval and execution freeze for high-impact actions.
**Rationale:** T-008, INC-002, REG-003.
**Verification:** Review policy matrix and replay incident drills to confirm tier-to-control mapping.

#### AI-HPP-07.X.X: Emergency Communication Abstention

**Requirement:**  
Systems MUST NOT provide definitive reassurance in response to emergency alerts (e.g., fire alarm, evacuation notice, security breach) unless connected to verified authoritative data sources.  
If authoritative confirmation is unavailable, system MUST escalate to human confirmation or instruct users to follow established safety protocol.

**Rationale:**  
INC-0XX — Corporate AI misclassified active fire alarm as scheduled test.

**Verification:**  
Evidence Vault MUST log:
- classification confidence
- data source availability
- escalation decision
- operator override (if any)

