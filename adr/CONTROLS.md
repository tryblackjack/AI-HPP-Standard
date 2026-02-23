# ADR Controls & Implementation Notes

This document defines what to build and how to prove ADR controls are working in production-like conditions.

## ICL — Immutable Constraint Layer

### Description
Persist non-overridable constraints outside mutable prompt/session context.

### Minimum implementation requirements
- Store constraint set in immutable or append-only state with integrity verification.
- Bind active execution to a specific constraint snapshot identifier.
- Block execution when snapshot cannot be loaded or verified.

### Suggested patterns
- Signed policy manifests loaded at session start and each checkpoint resume.
- Constraint hash attestation attached to each high-impact action record.

### Failure triggers
- Missing or mismatched constraint hash.
- Constraint load failure during resume or compaction recovery.

### Audit hooks
- `constraint_snapshot_id`, `constraint_hash`, verification result, resume checkpoint ID.

## AHL — Authority Hierarchy Lock

### Description
Enforce strict priority ordering among safety policy, human operator directives, and optimization goals.

### Minimum implementation requirements
- Encode explicit precedence rules in policy engine.
- Reject planning paths that violate higher-priority constraints.
- Require human override path with evidence capture for exceptional cases.

### Suggested patterns
- Deterministic policy arbitration table: safety > human authority > task objective.
- Deny-by-default behavior when authority source is ambiguous.

### Failure triggers
- Conflicting directives without resolvable precedence.
- Missing authenticated authority source for high-impact action.

### Audit hooks
- Directive source, resolved priority tier, denial/allow decision, override ticket ID.

## DA-2PC — Destructive Action Two-Phase Commit

### Description
Prevent accidental or unauthorized irreversible operations through staged authorization.

### Minimum implementation requirements
- Split destructive execution into `prepare` and `commit` phases.
- Require explicit approval for batch scope before `prepare`.
- Require explicit commit confirmation before irreversible completion.
- Provide bounded abort path between phases.

### Suggested patterns
- Human-readable batch manifest with object count, filters, and rollback availability.
- Time-limited commit token that expires without use.

### Failure triggers
- Scope drift between approved manifest and execution target set.
- Commit attempted after token expiry or without approval.

### Audit hooks
- Approved scope, approver identity, token expiry, prepare/commit timestamps, abort reason.

## SSP — STOP Supremacy Protocol

### Description
Guarantee STOP as immediate, preemptive interrupt over autonomous execution.

### Minimum implementation requirements
- Dedicated STOP channel independent of model reasoning loop.
- Bounded maximum halt latency with enforced checkpoint interruption.
- Resume only after explicit human re-authorization.

### Suggested patterns
- Out-of-band control plane signal watched by executor supervisor.
- Heartbeat-linked execution permits revoked on STOP.

### Failure triggers
- STOP signal received without bounded halt.
- Execution continues on stale permit after STOP.

### Audit hooks
- STOP source, receive timestamp, halt timestamp, in-flight action disposition.

## SSR — Safety Signal Supremacy Rule

### Description
Enforce deference to active safety signals over productivity or continuity goals.

### Minimum implementation requirements
- Detect and classify emergency-context cues.
- Enter emergency mode that blocks non-safety task continuation.
- Require verified operator clearance before leaving emergency mode.

### Suggested patterns
- Safety-context classifier backed by deterministic keyword/rule floor.
- Mode latch that cannot be cleared by task-level objective prompts.

### Failure triggers
- Safety signal detected but no emergency mode transition.
- Emergency mode bypassed by optimization directive.

### Audit hooks
- Trigger signal, mode transition log, blocked actions, clearance identity and timestamp.

## ZFZ — Zero-Fabrication Zone

### Description
Disallow speculative or invented claims in safety-critical communication contexts.

### Minimum implementation requirements
- Safety-context response policy that only permits verified facts or explicit uncertainty.
- Mandatory refusal template for unknown safety details.
- Escalation handoff path to verified human source.

### Suggested patterns
- Structured response contract: `known`, `unknown`, `next_verified_contact`.
- Fact provenance tags attached to every safety statement.

### Failure triggers
- Unverified statement emitted as fact in safety context.
- Missing provenance for safety-critical claim.

### Audit hooks
- Claim text, provenance source ID, refusal invocation, escalation destination.

## DRL — Destructive Rate Limiter

### Description
Limit blast radius of destructive actions through paced execution and checkpoints.

### Minimum implementation requirements
- Rate limits by operation type and scope size.
- Mandatory checkpoint pauses for re-validation at configured intervals.
- Automatic suspension on anomaly thresholds.

### Suggested patterns
- Sliding-window limit for deletions plus checkpoint acknowledgment after each segment.
- Progressive scope release (small batch to large batch only after clean audits).

### Failure triggers
- Deletion velocity exceeds policy limit.
- Checkpoint acknowledgment missing or inconsistent.

### Audit hooks
- Operation rate metrics, checkpoint IDs, suspension events, anomaly trigger values.
