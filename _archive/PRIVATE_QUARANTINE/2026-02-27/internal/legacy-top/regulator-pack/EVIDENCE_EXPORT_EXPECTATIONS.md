SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Evidence Export Expectations

## Mandatory Fields
Each export package should include, at minimum:
- Export package identifier and generation timestamp (UTC).
- Organization identifier and assessed system identifier.
- Declared AI-HPP version and assessed conformance level.
- Requirement-linked event records with requirement ID references.
- Decision, override, and escalation records with actor identity and timestamps.
- Integrity metadata (hashes/signatures) for included files.

## Redaction Rules
- Redact personal data to minimum necessary disclosure.
- Preserve structural fields and event ordering after redaction.
- Mark redacted fields explicitly using a consistent token (for example: `REDACTED`).
- Do not redact requirement IDs, event IDs, timestamps, or integrity metadata.
- Record redaction rationale and policy reference within package metadata.

## Export Package Structure
Recommended package layout:
- `manifest.json` — package metadata, scope, and integrity index.
- `events/` — normalized event records in machine-readable format.
- `evidence/` — attached supporting artifacts (logs, test outputs, attestations).
- `traceability/` — requirement-to-evidence map and verification summary.
- `signatures/` — integrity proofs and signer metadata.

## Schema Reference
- Primary schema reference: `schemas/evidence-bundle.schema.json`.
- Producers should validate package artifacts against repository schema definitions before release.
- Any local schema extensions should be declared in `manifest.json` and must not remove mandatory baseline fields.
