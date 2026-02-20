# Tool Execution Boundary (TEB)

**Type:** Normative (enforceable policy)
**Applies to:** file tools, shell/exec tools, patch/apply tools, CI integrations

## Purpose
Prevent prompt-injection from escalating into arbitrary code execution or destructive file operations.

## Requirements

### Workspace-only by default
File write/edit/patch operations MUST be restricted to workspace by default:
- `workspaceOnly = true` (or equivalent)
- attempts to access outside workspace MUST fail-closed and log.

### Non-main sandboxing
For non-owner contexts (groups, shared channels, unknown senders):
- exec/shell MUST run in an isolated sandbox (container/VM) per session/task.
- network access from sandbox MUST be deny-by-default (allowlist only).

### Tool-call firewall
Before any privileged tool call, the system MUST evaluate:
- caller trust (paired/allowlisted vs unknown)
- context trust (DM main vs group vs external content)
- requested capability (fs/net/exec/secrets)
and either:
1) allow, or
2) require explicit human approval, or
3) deny.

### High-impact actions
Define and protect high-impact actions:
- deleting files, rewriting configs, modifying policies,
- credential access,
- remote network calls to unknown domains,
- deployment actions.
High-impact actions MUST require explicit approval (two-step or 2-person rule in enterprise mode).

## Audit evidence checklist
- [ ] workspace-only enforced
- [ ] per-session sandbox for untrusted contexts
- [ ] network allowlists for tool calls
- [ ] approval gates for high-impact actions
- [ ] logs capture tool-call intent + outcome
