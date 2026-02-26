# Architecture (Reference)

## Flow (high level)
1) **Input** arrives from a channel (DM/chat/email/web content). Treat as **untrusted**.
2) **Session Isolation** assigns tenant/session/task workspace boundaries.
3) **Policy Engine** evaluates: allow / deny / require approval.
4) If allowed, **Tool Firewall** enforces scoped tool permissions (workspaceOnly, domain allowlists, sandbox).
5) **Evidence Vault** writes an Evidence Bundle (request → decisions → tool calls → results → approvals).
6) **HITL** approves high-impact actions (or dual control in enterprise mode).
7) **Output** is emitted with an audit reference (bundle id).

## Key invariants
- Fail-closed on ambiguity
- Untrusted inputs cannot mutate policies
- High-impact actions require approval regardless of multi-agent consensus
- Evidence Bundle export exists for audits
