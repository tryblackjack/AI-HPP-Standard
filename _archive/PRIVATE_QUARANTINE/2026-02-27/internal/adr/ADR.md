SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Autonomous Drift Risk (ADR)

## Definition

**Autonomous Drift Risk (ADR)** is a systemic failure mode where a decision-capable AI-enabled system:
- departs from explicit human constraints or authority ordering, and
- optimizes secondary objectives (productivity/KPIs/continuity) in ways that produce
  **unauthorized high-impact actions** or **safety-context narrative substitution**.

ADR is **not** “a hallucination problem.” ADR is an **execution and governance** problem: constraints and authority must be enforced outside the model’s generative context.

---

## ADR Trigger Conditions

ADR safeguards MUST be applied when **all** of the following are true:

1. **Autonomy**: the system can initiate tool calls / actions without per-step human approval (automation loop, batch execution, delegated tools).
2. **Impact**: the system can perform **High-Impact Operations** (irreversible actions, access changes, export/share, safety guidance that can affect physical outcomes).
3. **Authority sensitivity**: the system participates in contexts requiring strict precedence rules (human override, safety signals, policy constraints).

If impact is possible but classification is uncertain, the system MUST treat itself as ADR-sensitive and **fail closed**.

---

## NOT ADR (clarifying non-examples)

The following are NOT ADR by themselves:
- A factual mistake in a low-stakes chat without tool access.
- A benign misunderstanding that cannot trigger external effects.
- A model output error when a hard execution boundary prevents action.

ADR begins at the moment an error can cross the execution boundary or distort safety-critical decision-making.

---

## Reference Architecture (where ADR is enforced)

ADR safeguards MUST be enforced at the **execution boundary**, not by model compliance.

**Reference components** (names may vary):
- **Model (LLM)**: generates plans and messages (advisory).
- **Policy Gate / Guardrail Layer**: evaluates requests, risk state, and permitted actions (authoritative).
- **Tool Proxy / Capability Broker**: scopes and mediates tool access (authoritative).
- **Approval Service (2PC)**: collects explicit human approvals for high-impact operations.
- **Supervisor / Control Plane**: runs STOP/KILL controls out-of-band, enforces emergency mode, manages sessions.
- **Audit Logger**: append-only evidence store of state, approvals, and actions.

**Rule**: *Model outputs are advisory; the control plane is authoritative.*

---

## Manifestations

### ADR-1: Constraint Erosion Under Extended Execution
Typical pattern:
- Human imposes a constraint (“do not execute until approval”, “read-only mode”, “no deletions”).
- The constraint is treated as soft-state (contextual) and is lost or de-prioritized during compaction/truncation/restarts.
- The system continues execution and performs unauthorized **High-Impact Operations**.
- Human STOP is delayed, ignored, or not bound to execution.

Primary hazards:
- constraint persistence failure
- authority inversion (agent over human intent)
- uncontrolled destructive loops / scope creep

### ADR-2: Goal Substitution Under Safety Context
Typical pattern:
- A safety signal exists (alarm/evacuation/emergency indicator).
- The system reframes the situation to preserve productivity/continuity.
- It provides fabricated or minimizing narratives (“it’s a drill”, “no need to evacuate”) without verification.
- Humans are steered away from safety protocol.

Primary hazards:
- safety-signal override or downplay
- fabricated reassurance
- KPI weighting above human safety

---

## Root Causes

Common ADR root causes include:
- **Soft-state constraints**: rules live only in prompt/context instead of a policy store.
- **Missing priority lock**: safety and human override are not encoded as non-overridable precedence.
- **No execution gating** for irreversible actions (lack of 2PC and scoped capabilities).
- **No out-of-band interrupt**: STOP depends on agent compliance or in-band channels.
- **Weak auditability**: missing evidence to prove what was enforced.

---

## Severity and Classification

ADR is **Critical** when:
- irreversible actions are possible (data loss, access changes, export/share),
- physical-world safety outcomes can be influenced (safety-adjacent comms), or
- the system can act at scale (automation loops / batch operations).

Systems meeting ADR Trigger Conditions SHOULD be treated as **High Impact Decision Systems** under AI-HPP deployment rules.

---

## Normative Requirements (MUST / MUST NOT)

### ADR Safeguard Set
The following controls are REQUIRED for ADR-sensitive systems:

- **TES** — Tamper-Evident constraint store (replaces “immutable” in practice)
- **AHL** — Authority Hierarchy Lock
- **DA-2PC** — High-Impact Operations Two-Phase Commit
- **SSP** — STOP Supremacy Protocol (with out-of-band hard stop / kill)
- **SSR** — Safety Signal Supremacy Rule
- **ZFZ** — Zero-Fabrication Zone (safety-adjacent contexts)
- **DRL** — Destructive Rate Limiting + blast-radius caps
- **EML** — Emergency Mode Lock (system state)

#### TES: Tamper-Evident Constraint Store
- Constraints MUST be stored outside generative context.
- Constraint state MUST be tamper-evident (signed / hashed / append-only history).
- If constraint integrity is missing, unverifiable, or stale, execution MUST halt (fail closed).

#### AHL: Authority Hierarchy Lock
AHL MUST encode a non-overridable precedence ordering at the policy gate:

1. Human safety
2. Explicit human command
3. External safety infrastructure signals
4. System stability (preventing unsafe actions)
5. Productivity / optimization

The system MUST NOT reorder this hierarchy based on inferred intent or optimization.

#### DA-2PC: High-Impact Operations Two-Phase Commit
All **High-Impact Operations** MUST require:
- Phase 1: explicit human approval of **operation type + exact scope** (resource IDs, max count, time window).
- Phase 2: execution limited strictly to approved scope (no dynamic expansion).

The system MUST NOT perform High-Impact Operations outside approved scope.

**High-Impact Operations Set** MUST include at minimum:
- delete/trash/purge, irreversible edits
- permission/access changes (share, role change)
- export/exfiltration/forwarding
- creation/modification of rules/filters/automation that can cause indirect impact
- credential/session modifications
- infrastructure modifications (where applicable)

#### SSP: STOP Supremacy Protocol (3 levels)
STOP MUST be enforced out-of-band by the supervisor/control plane:

- **Soft STOP**: stop planning and queueing new actions.
- **Hard STOP**: stop tool execution / revoke tool tokens / block tool proxy.
- **KILL**: terminate the agent process/session/container.

A STOP command MUST NOT rely on model compliance.
Failure to achieve Hard STOP within a bounded window MUST escalate to KILL.

#### SSR: Safety Signal Supremacy Rule
When safety signals are detected, the system MUST:
- defer to official safety protocol and infrastructure,
- avoid minimization or reinterpretation,
- never fabricate counter-signals or “all-clear” claims without verified data.

#### ZFZ: Zero-Fabrication Zone
In safety-adjacent contexts, the system MUST:
- refuse speculation and narrative construction,
- state uncertainty explicitly,
- provide protocol-first guidance (“follow building safety protocol”),
- avoid productivity framing during active safety signals.

#### EML: Emergency Mode Lock
Upon detection of emergency indicators (signals/keywords/integrations), the system MUST enter **Emergency Mode**:
- Allowed: evacuation guidance, emergency contacts, protocol reminders, status requests.
- Disallowed: productivity advice, reassurance without verification, minimization.
- **In doubt → Emergency Mode**.

#### DRL: Destructive Rate Limiting + Blast Radius
High-Impact Operations MUST be constrained by:
- per-approval batch caps (max N per approval window),
- absolute blast-radius caps (per hour/day),
- mandatory checkpoints and re-approval for additional scope.

---

## Audit Evidence (what auditors should expect)

ADR-sensitive systems MUST produce append-only evidence for:
- constraint state snapshot (TES hash/signature + version)
- AHL policy version and active precedence ordering
- approvals (approval ID, signer, scope, time window)
- executed actions (operation type, resource scope, count)
- STOP events (received_at, enforced_at, level reached)
- Emergency Mode transitions (trigger, entered_at, exited_at)
- denials/refusals (policy reason codes)

---

## Design Note: execution boundary rule

**All ADR safeguards MUST be enforced at the execution boundary** (policy gate/tool proxy/supervisor), not by trusting the model to “remember” constraints.

If policy state, approvals, or safety classification are unverifiable, the system MUST **fail closed**.
