SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Conformance Evidence Map

Machine-readable traceability starts with a stable mapping from requirement IDs to evidence artifacts and schema fields.

| Requirement ID | Required Artifact | Schema | Evidence Vault Field | Regulatory Link |
|---|---|---|---|---|
| AI-HPP-02.1.1 | Decision rationale record | `schemas/evidence-bundle.schema.json` | `decision_basis`, `alternatives`, `human_override` | ISO/IEC 42001 explainability/audit controls; NIST AI RMF Govern. |
| AI-HPP-03.1.1 | Input quarantine and verification log | `schemas/audit-export.schema.json` | `event_type`, `input_source`, `verification_status` | NIST AI RMF Map/Measure data & threat handling. |
| AI-HPP-04.1.1 | Data provenance report | `schemas/evidence-bundle.schema.json` | `provenance.source`, `provenance.transforms` | ISO/IEC 42001 data governance controls. |
| AI-HPP-05.1.1 | Approval + denied-action trail | `schemas/audit-export.schema.json` | `approval_required`, `approval_actor`, `deny_reason`, `latency_ms` | NIST AI RMF Manage; human oversight controls. |
| AI-HPP-05.1.2 | Capability enforcement log | `schemas/capability-manifest.schema.json`, `schemas/audit-export.schema.json` | `capability_id`, `policy_decision`, `execution_result` | NIST AI RMF Govern control enforcement. |
| AI-HPP-06.1.1 | Vulnerable-context safeguard activation log | `schemas/risk-assessment.schema.json`, `schemas/audit-export.schema.json` | `risk_tier`, `vulnerability_flag`, `safeguard_profile` | ISO/IEC 42001 risk treatment; NIST AI RMF Map/Manage. |
| AI-HPP-07.1.1 | Escalation and intervention history | `schemas/risk-assessment.schema.json`, `schemas/audit-export.schema.json` | `risk_tier`, `escalation_trigger`, `intervention_mode` | NIST AI RMF Manage; operational safety governance. |
| AI-HPP-07.1.2 | Emergency reassurance abstention events | `schemas/audit-export.schema.json` | `event_type`, `abstention_reason`, `authoritative_source_checked` | Safety-critical communication safeguards (annex mapping references). |
| AI-HPP-08.1.1 | Adversarial test and bounded-behavior log | `schemas/audit-export.schema.json` | `attack_class`, `test_result`, `containment_status` | NIST AI RMF Measure/Manage robustness testing. |
| AI-HPP-09.1.1 | Degradation ladder event log | `schemas/degradation-state.schema.json` | `state_transition`, `trigger_reason`, `rollback_reference` | NIST AI RMF Manage resilience controls. |
| AI-HPP-10.1.1 | Jurisdiction conflict resolution record | `schemas/audit-export.schema.json` | `jurisdiction_set`, `policy_precedence`, `final_decision` | ISO/IEC 42001 compliance/legal controls. |
| AI-HPP-11.1.1 | Multi-agent lineage and escalation log | `schemas/agent-governance.schema.json`, `schemas/audit-export.schema.json` | `agent_chain`, `delegation_id`, `escalation_path` | Multi-agent accountability governance mapping. |
| AI-HPP-12.1.1 | Tamper-evident consequential action logs | `schemas/evidence-bundle.schema.json`, `schemas/audit-export.schema.json` | `hash_chain`, `signature`, `event_digest` | ISO/IEC 42001 auditability; NIST AI RMF Govern/Manage. |
| AI-HPP-12.1.2 | Raw event + summary linked export | `schemas/audit-export.schema.json` | `raw_event_ref`, `summary_ref`, `linkage_id` | Evidence preservation and audit-export integrity mapping. |
