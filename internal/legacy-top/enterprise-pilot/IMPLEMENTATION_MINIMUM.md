SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Implementation Minimum for Enterprise Pilot

## Minimal L1 Baseline
- Implement all applicable L1 control behaviors for in-scope AI-HPP requirements.
- Document control ownership and operating procedures.
- Maintain requirement-to-control mapping for inspection traceability.

## Required Evidence Vault Events
At minimum capture:
- Policy evaluation outcomes for safety-critical actions.
- Override invocations, actor identity, and rationale.
- Escalation triggers, thresholds, and resulting state transitions.
- Verification/test execution records tied to requirement IDs.

## Required Override Mechanism
- Explicit, role-restricted override channel.
- Mandatory rationale and timestamp on every override action.
- Automatic logging to evidence records with immutable event IDs.

## Required Tool Boundary Controls
- Enforce tool allowlists and scoped authorization boundaries.
- Block out-of-scope execution attempts and log denial events.
- Preserve execution trace context sufficient for post-incident review.
