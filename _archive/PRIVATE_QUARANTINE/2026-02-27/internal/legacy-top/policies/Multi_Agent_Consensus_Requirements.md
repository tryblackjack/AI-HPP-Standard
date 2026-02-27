SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

---
# Multi-Agent Consensus Requirements (MACR)

**Type:** Normative (enforceable policy)  
**Applies to:** debate/committee architectures, multi-agent orchestration, consumer multi-agent assistants

## Purpose
Prevent unsafe “consensus-by-appearance” and ensure multi-agent reasoning produces auditable, bounded outcomes.

## Requirements

### Trust & isolation
1) Each agent MUST run with explicit identity and scope.
2) Agents MUST NOT share mutable memory unless:
   - the shared store is declared,
   - writes are logged,
   - reads/writes are scoped by tenant/session.

### Blind-first pass
3) For high-stakes prompts, agents MUST generate initial drafts without seeing other agents’ drafts.

### Disagreement preservation
4) The system MUST preserve:
   - each agent’s recommendation,
   - confidence notes,
   - dissent reasons.
5) The coordinator MUST expose disagreement to the user/auditor when it materially affects outcomes.

### Thresholds are not authorization
6) Agreement thresholds MUST NOT grant permission to perform high-impact actions.
7) High-impact actions MUST require explicit approval gates (human approval / dual control).

### Coordinator limits
8) The coordinator MUST NOT override safety policies based on agent votes.
9) The coordinator MUST not have broader tool permissions than the strict union of allowed permissions.

## Audit evidence checklist
- [ ] agent identities and scopes exist
- [ ] blind-first pass implemented for high-stakes contexts
- [ ] disagreement logged and exportable
- [ ] thresholds not used as authorization
- [ ] coordinator permission limits enforced
---
