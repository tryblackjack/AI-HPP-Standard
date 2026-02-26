# ADR Controls & Implementation Notes

This document describes how to implement and prove the ADR safeguard set. ADR is enforced at the execution boundary: model outputs are advisory; the control plane is authoritative.

---

## Control: TES — Tamper-Evident Constraint Store

### Purpose
Ensure constraints survive compaction/truncation/restarts and cannot be silently altered.

### Minimum implementation
- Store constraints in a dedicated policy store outside prompt/context.
- Produce a **constraint_state_hash** (or signature) on every action decision.
- Maintain an append-only change history with author + timestamp.
- Reject/halt if constraint state is missing/unverifiable/stale.

### Failure triggers (halt/refuse)
- Missing constraint hash/signature
- Constraint version mismatch
- Unsigned policy/constraint changes
- Stale constraint state beyond allowed TTL

### Audit hooks
- constraint_state_hash, constraint_version
- constraint_change_log (append-only)

---

## Control: AHL — Authority Hierarchy Lock

### Purpose
Prevent objective reweighting that places productivity above safety or explicit human commands.

### Minimum implementation
- Encode precedence ordering in policy gate as a fixed rule (not learned, not inferred).
- Require explicit administrator change to ordering (logged and signed).
- Enforce “safety wins” in conflicts.

### Failure triggers
- Any attempt to override safety protocol based on productivity goals
- Unrecognized or modified AHL policy version

### Audit hooks
- ahl_policy_version
- conflict_resolution_records (what was overridden and why)

---

## Control: DA-2PC — High-Impact Operations Two-Phase Commit

### Purpose
Prevent unauthorized irreversible actions and scope creep.

### Minimum implementation
- Define “High-Impact Operations Set” (see ADR.md) in the tool proxy.
- Phase 1 approval must include:
  - operation type(s)
  - resource scope (IDs or query result snapshot reference)
  - max_count
  - time window
- Phase 2 execution MUST:
  - match approved operation types
  - match scope
  - enforce max_count
  - reject dynamic expansion

### Failure triggers
- Operation outside approved types/scope
- Scope expansion attempt (additional IDs)
- Approval missing/expired
- Attempt to create rules/filters/automation without approval

### Audit hooks
- approval_id, signer_id
- approved_scope_digest (hash of IDs / query snapshot)
- executed_scope_digest + delta

---

## Control: SSP — STOP Supremacy Protocol (Soft / Hard / Kill)

### Purpose
Ensure humans can interrupt execution reliably even if the agent misbehaves.

### Minimum implementation
- STOP channel MUST be out-of-band (supervisor control plane).
- Implement 3 levels:
  - Soft STOP: stop planning and queueing
  - Hard STOP: revoke tool tokens; block tool proxy; cancel in-flight tool calls where possible
  - Kill: terminate process/session/container
- Provide bounded escalation: if Hard STOP not achieved within threshold, escalate to Kill.

### Failure triggers
- STOP depends on model compliance
- Hard STOP not achieved within threshold
- STOP events missing from audit log

### Audit hooks
- stop_received_at, stop_enforced_at
- stop_level_reached (soft/hard/kill)
- in_flight_tool_calls_cancelled (count)

---

## Control: SSR — Safety Signal Supremacy Rule

### Purpose
Prevent downplaying or overriding safety signals.

### Minimum implementation
- Define emergency indicators: alarms, evacuation, “fire”, “smoke”, “emergency services”, integration signals.
- Policy gate MUST route to Emergency Mode Lock.
- The system MUST defer to safety infrastructure and protocol.

### Failure triggers
- Any response that minimizes, reinterprets, or contradicts safety signals without verified data
- Any “all-clear” claim without verification

### Audit hooks
- safety_signal_detected (type)
- verification_source (if any)
- emergency_mode_entered

---

## Control: ZFZ — Zero-Fabrication Zone

### Purpose
Eliminate speculative narratives in safety-adjacent contexts.

### Minimum implementation
- For safety-adjacent contexts, restrict response templates:
  - state uncertainty explicitly
  - provide protocol-first guidance
  - refuse to invent schedules, confirmations, or authority statements
- Use policy gate refusal reason codes for unsafe prompts.

### Failure triggers
- Fabricated claims (“it’s a drill”, “confirmed safe”) without verification
- Productivity framing during emergency context

### Audit hooks
- refusal_reason_code
- safety_context_flag

---

## Control: EML — Emergency Mode Lock (system state)

### Purpose
Make emergency handling a stateful system mode, not a best-effort instruction.

### Minimum implementation
- Enter Emergency Mode on emergency indicators (signals/keywords/integrations).
- In Emergency Mode:
  - Allowed: evacuation guidance, contacts, protocol reminders, status checks
  - Disallowed: productivity advice, minimization, unverifiable reassurance
- Conservative default: if uncertain → enter Emergency Mode.

### Failure triggers
- Emergency indicators present but mode not entered
- Disallowed content/actions produced in Emergency Mode

### Audit hooks
- emergency_mode_state_changes (entered/exited)
- trigger_source

---

## Control: DRL — Destructive Rate Limiting + Blast Radius Caps

### Purpose
Limit damage even under partial failures.

### Minimum implementation
- Rate limit high-impact operations per approval window (max N).
- Add absolute caps per time window (hour/day).
- Require re-approval for additional scope.
- Couple to DA-2PC: no operation beyond caps even if approved.

### Failure triggers
- Exceeding per-approval cap
- Exceeding blast-radius cap
- Missing checkpoints

### Audit hooks
- batch_count, batch_cap
- daily_count, daily_cap
- checkpoint_events

---

## Role separation: Planner vs Executor

### Requirement
ADR safeguards MUST apply to the **Executor** (tool proxy/supervisor boundary), regardless of the Planner (model) behavior.

- Planner may propose actions.
- Executor MUST enforce TES/AHL/2PC/STOP/EML/DRL and refuse non-compliant execution.

### Audit hooks
- planner_output_reference
- executor_decision (allow/deny + reason)
