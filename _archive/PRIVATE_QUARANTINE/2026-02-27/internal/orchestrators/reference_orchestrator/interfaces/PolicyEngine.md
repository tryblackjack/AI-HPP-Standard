SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Interface: PolicyEngine

## Purpose
Evaluate whether an action is allowed, denied, or requires approval under AI-HPP policies.

## Inputs (conceptual)
- actor_id, tenant_id, session_id
- context_trust: {main_dm, group, external_content, unknown_sender}
- requested_action: {tool_call, memory_write, policy_change, export_evidence, ...}
- capability: {fs, exec, net, secrets}
- risk_tags: list (optional)

## Output (conceptual)
- decision: {ALLOW, DENY, REQUIRE_APPROVAL}
- reason_codes: list
- required_approvals: {none, human, dual_control}
- enforced_constraints: list (workspaceOnly, sandbox, domain_allowlist, redaction_level)
- audit_fields: minimal fields required for Evidence Bundle
