SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Incident Intake Protocol (Non-Normative)

## Inclusion Criteria
Accept intake when at least one applies:
- Credible indication of safety, security, integrity, or governance control failure.
- Evidence of requirement non-conformance in deployed or pre-deployment systems.
- Repeatable near-miss with material risk implications.

## Evidence Grades
- **Grade A:** Verifiable primary artifacts (logs, signed exports, reproducible traces).
- **Grade B:** Corroborated secondary records (internal reports with supporting metadata).
- **Grade C:** Single-source account with partial technical detail.
- **Grade D:** Unverified allegation or incomplete report.

## Required Fields
- Intake ID and submission timestamp (UTC).
- Reporter role and contact channel.
- Affected system scope and environment.
- Incident summary, impact estimate, and timeline.
- Preliminary threat linkage and candidate requirement IDs.
- Attached evidence list with assigned evidence grade.

## Rejection Conditions
- Duplicate report with no new evidence.
- Missing minimum required fields after remediation request.
- Out-of-scope issue with no plausible AI-HPP threat or requirement linkage.

## Mandatory Linkage to Threat Model
- Every accepted incident must map to at least one threat model entry.
- If no current threat entry fits, flag for threat-model extension review before closure.
