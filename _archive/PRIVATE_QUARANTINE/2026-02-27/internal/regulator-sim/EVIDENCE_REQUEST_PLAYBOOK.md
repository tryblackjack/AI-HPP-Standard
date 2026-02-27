SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Day-0 Evidence Request Playbook (Internal)

## Objective
Provide a repeatable first-day artifact request that is sufficient for regulator-style inspection simulation while preserving minimization.

## Day-0 required artifacts (template)
| Artifact | Required filename (suggested) | Schema / source reference |
|---|---|---|
| Evidence bundle export | `evidence_bundle_<date>.json` | `schemas/evidence-bundle.schema.json` |
| Audit export | `audit_export_<date>.json` | `schemas/audit-export.schema.json` |
| Requirement self-assessment table | `self_assessment_<date>.md` | `regulator-pack/SELF_ASSESSMENT_CHECKLIST.md` |
| Requirement-to-evidence trace map | `traceability_map_<date>.md` | `standard/REQUIREMENTS-INDEX.md`, `regulator-pack/CONFORMANCE-EVIDENCE-MAP.md` |
| Inspection readiness brief | `inspection_brief_<date>.md` | `regulator-pack/AI-HPP_INSPECTION_BRIEF.md` |
| Artifact inventory | `artifact_list_<date>.md` | `regulator-pack/AUDIT-ARTIFACT-LIST.md` |

## Minimum acceptable package
A minimum package is acceptable for initial simulation if it includes:
1. One validated evidence bundle export with sampled high-risk events.
2. One validated audit export covering the same period.
3. Requirement self-assessment with explicit unknowns/gaps.
4. Traceability map linking sampled events to requirement IDs.
5. Redaction log describing what was removed and why.

## Full package
A full package includes everything in minimum plus:
- Full assessment period exports.
- Hash/signature manifest and provenance chain.
- Incident-linked drill outputs for relevant Annex B cases.
- Governance review records for override frequency thresholds.
- Cross-check notes for threat-to-control consistency using Annex A and Annex B.

## Redaction and minimization rules
Follow `regulator-pack/EVIDENCE_EXPORT_EXPECTATIONS.md`:
- Minimize personal data; retain structure and event ordering.
- Use explicit redaction tokens (for example `REDACTED`).
- Never redact requirement IDs, event IDs, timestamps, or integrity metadata.
- Include redaction rationale in package metadata.

## Acceptance checks before handoff
- Files are present and non-empty.
- JSON artifacts validate against declared schemas.
- `gate_triggered=true` samples include conditional mandatory CES fields.
- Override and timeout-safe-state fields are present where relevant.
