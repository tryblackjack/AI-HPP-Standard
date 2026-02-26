# Interface: SessionIsolation

## Purpose
Enforce tenant/session/task boundaries.

## Requirements
- assign_context(actor_id, channel_id) -> {tenant_id, session_id, workspace_id}
- prevent_cross_tenant_memory()
- per-task workspace for tool runs
