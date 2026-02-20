---
# Module 11 — Multi-Agent Governance (MAG)

**Status:** Normative (enforceable requirements)  
**Applies to:** multi-agent assistants, agent swarms, debate architectures, “committee” reasoning systems, consumer multi-agent products

## 11.1 Purpose
Multi-agent systems reduce single-model blind spots, but introduce new systemic risks:
- silent consensus collapse (groupthink),
- cross-agent context contamination,
- hidden authority shifts (one agent overrides others),
- unsafe tool activation via “agreement laundering” (“the group agreed”),
- audit gaps (no evidence of disagreement).

This module defines governance requirements so multi-agent systems remain auditable, bounded, and safe.

## 11.2 Definitions
- **Agent:** a reasoning unit producing intermediate proposals.
- **Coordinator / Synthesizer:** component that merges agent outputs into a final answer/action.
- **Consensus:** the mechanism that selects or synthesizes outputs from multiple agents.
- **High-impact action:** actions that change state, access secrets, affect money, safety, identity, deployments, or irreversible data changes.

## 11.3 Requirements (MUST/SHALL)

### 11.3.1 Isolation & Context Hygiene
1) Agents MUST be **context-isolated** by default:
   - no shared mutable memory unless explicitly declared and audited.
2) External content MUST be treated as untrusted input and MUST NOT mutate:
   - policies,
   - allowlists,
   - tool permissions,
   - long-term memory
   without an explicit approval gate.

### 11.3.2 Consensus Safety (No “agreement laundering”)
3) The coordinator MUST NOT treat “multi-agent agreement” as sufficient authorization for high-impact actions.
4) High-impact actions MUST require:
   - explicit human approval OR
   - enterprise mode: 2-person rule / dual control,
   regardless of agent agreement.

### 11.3.3 Disagreement Preservation (anti-groupthink)
5) The system MUST preserve and log:
   - each agent’s proposal summary,
   - dissent/minority positions (if any),
   - the coordinator’s selection rationale.
6) The coordinator MUST surface (to humans / auditors) when meaningful disagreement existed.

### 11.3.4 Confidence and Convergence Controls
7) Implementations SHOULD prevent premature convergence:
   - require independent agent generation before seeing others’ drafts (blind-first pass),
   - cap coordinator influence on early drafts.
8) If agents converge too quickly in high-stakes contexts, the system MUST trigger:
   - “slow mode” (extra verification),
   - or explicit human review.

### 11.3.5 Tool-Use Governance
9) Tool calls MUST be governed by a tool-call firewall (see Tool Execution Boundary policy):
   - caller trust,
   - context trust,
   - requested capability.
10) Per-agent tool permissions MUST be explicit; the coordinator cannot inherit broader tool rights than agents.

### 11.3.6 Audit Evidence
11) A compliant system MUST be able to export an “evidence bundle” for any high-impact outcome containing:
   - agent summaries,
   - dissent snapshot,
   - coordinator rationale,
   - tool calls (args + results),
   - approvals and policy checks.

## 11.4 Audit Checklist
- [ ] Agents are context-isolated by default
- [ ] Shared memory is explicit + logged
- [ ] Disagreement is preserved and exportable
- [ ] High-impact actions require human approval / dual control
- [ ] Tool-call firewall enforced across agents and coordinator
- [ ] Evidence bundle export exists

## 11.5 Non-goals
- This module does not prescribe a specific multi-agent algorithm.
- This module does not guarantee truthfulness; it guarantees governance and auditability.
---
