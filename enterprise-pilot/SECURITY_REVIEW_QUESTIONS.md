# Enterprise Pilot Security Review Questions

## IAM
- Are identities for human operators, services, and agents uniquely scoped and auditable?
- Are privileged roles minimized and periodically reviewed?

## Token Scope
- Are access tokens constrained to least privilege and bounded lifetime?
- Are token misuse and scope mismatches detectable in logs?

## Tool Execution Boundary
- Are tool invocations restricted by allowlist, policy checks, and contextual authorization?
- Is blocked execution reliably logged with reason codes?

## Emergency Communication Override
- Is there a controlled emergency override path for urgent communication workflows?
- Are override authority, rationale, and timeline fully recorded?

## Kill-Switch
- Is a tested kill-switch available to halt unsafe autonomous actions?
- Are trigger conditions and execution responsibilities clearly assigned?

## Audit Export Readiness
- Can the organization produce a complete evidence export package on demand?
- Do export artifacts preserve requirement linkage, integrity metadata, and redaction accountability?
