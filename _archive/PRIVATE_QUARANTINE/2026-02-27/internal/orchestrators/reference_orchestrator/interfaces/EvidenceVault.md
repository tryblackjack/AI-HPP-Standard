SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Interface: EvidenceVault

## Purpose
Persist and export Evidence Bundles for high-impact outcomes and safety-relevant events.

## Required features
- write(bundle)
- read(bundle_id) with access control
- export(bundle_id, redaction_profile)
- preservation_hold(bundle_id, reason)
- audit_log(access_event)
