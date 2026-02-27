SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Session Isolation Mandate (SIM)

**Type:** Normative (enforceable policy)
**Applies to:** multi-user assistants, agent swarms, shared channels, customer support agents

## Purpose
Prevent cross-tenant context bleed, memory leakage, and prompt injection via context pollution.

## Requirements

### Isolation domains
Implementations MUST isolate at minimum by:
- user (peer) in DMs,
- channel/workspace for group chats,
- tenant/customer boundary (hard boundary),
- task/workspace for tool-enabled runs.

### Memory rules
- Persistent memory MUST NOT cross tenant boundaries.
- Memory writes MUST be gated by explicit policy and logged.
- Untrusted inputs MUST NOT be allowed to mutate system policies, allowlists, or memory without approval.

### Context hygiene
- External content (web pages, emails, docs) MUST be treated as untrusted.
- “Instruction” and “data” must be separated in the internal representation.

## Audit evidence checklist
- [ ] per-user DM isolation
- [ ] per-tenant hard boundary
- [ ] memory write gating + logs
- [ ] untrusted input cannot mutate policies
