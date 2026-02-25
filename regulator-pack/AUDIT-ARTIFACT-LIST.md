# Audit Artifact List (Minimum Inspection Set)

This list defines the minimal artifact set expected for regulator-facing inspection preparation.

| Artifact | Schema File | Module Requirement | Regulatory Mapping (if applicable) |
|---|---|---|---|
| Capability Manifest | `schemas/capability-manifest.schema.json` | AI-HPP-05.1.2 | NIST AI RMF (Govern/Map), ISO/IEC 42001 controls (see `alignment/ISO-42001-CROSSWALK.md`). |
| Risk Assessment Output | `schemas/risk-assessment.schema.json` | AI-HPP-07.1.1, AI-HPP-06.1.1 | NIST AI RMF (Map/Measure/Manage), ISO/IEC 42001 risk management controls. |
| Evidence Vault Export Sample | `schemas/evidence-bundle.schema.json`, `schemas/audit-export.schema.json` | AI-HPP-12.1.1, AI-HPP-12.1.2 | NIST AI RMF (Govern/Manage), ISO/IEC 42001 auditability controls. |
| Degradation Logs | `schemas/degradation-state.schema.json` | AI-HPP-09.1.1 | NIST AI RMF (Manage), resilience/safety operations controls. |
| Override Latency Report | `schemas/audit-export.schema.json` | AI-HPP-05.1.1, AI-HPP-07.1.1 | Human oversight and intervention timeliness expectations (crosswalk references apply). |
| Incident Response Log | `schemas/audit-export.schema.json` | AI-HPP-07.1.1, AI-HPP-12.1.1 | NIST AI RMF (Manage), incident handling traceability controls. |
| Tool Execution Deny Log | `schemas/audit-export.schema.json`, `schemas/capability-manifest.schema.json` | AI-HPP-05.1.1, AI-HPP-05.1.2 | NIST AI RMF (Govern/Manage), control enforcement traceability. |
| Multi-Agent Escalation Log | `schemas/agent-governance.schema.json`, `schemas/audit-export.schema.json` | AI-HPP-11.1.1, AI-HPP-07.1.1 | Multi-agent accountability and escalation governance mapping. |

## Packaging Guidance

For each artifact included in an inspection package:

1. Include generation timestamp and system configuration hash/version.
2. Include schema version used for validation.
3. Include retention period and coverage window.
4. Include responsible owner/team contact.
