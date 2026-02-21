# Threat Model (Practical)

## Primary threats
1) Prompt injection via untrusted channels (chat, email, web content)
2) Tool abuse (exec/fs/net) leading to destructive actions
3) Skill/plugin supply-chain compromise
4) Control plane exposure (misconfigured admin endpoints)
5) Cross-tenant context or memory leakage
6) Audit log tampering / evidence deletion
7) Unsafe content generation (e.g., minors/non-consensual edits) triggering regulatory escalation

## Default stance
- Fail-closed on ambiguity
- Least privilege for tools
- Isolation by tenant/session/task
- Evidence bundles for high-impact outcomes
