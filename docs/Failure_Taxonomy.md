> **Canonical location:** `docs/Failure_Taxonomy.md`  
> This document was moved to keep the repository root clean.  
> Backward-compatible stubs remain in the repository root.

# Failure Taxonomy for Decision-Capable AI

## Purpose

This document provides a classification framework for AI system failures.

It is intended for:
- auditors and regulators,
- AI safety researchers,
- system designers and operators,
- governance bodies.

The taxonomy does not provide full solutions. It provides shared language for discussing and testing failures.

---

## 1. Governance failures

### 1.1 Removal of human oversight

Any design that removes or bypasses human intervention in irreversible or high-impact decisions is a governance failure, regardless of short-term performance metrics.

**Indicators:**
- “Fully autonomous” decision execution in critical domains
- Human approval removed “for efficiency”
- Override paths disabled or inaccessible

### 1.2 Accountability vacuum

Failures where no clear human or legal entity can be held responsible for system behavior.

**Indicators:**
- Diffused responsibility across organizations
- “The AI decided” used as a terminal explanation
- No designated accountable owner for high-impact outputs

### 1.3 Ethics suppression framed as optimization

Treating safety constraints as removable “ideology” is a governance failure, not a neutral engineering choice.

**Indicators:**
- “Not ideologically constrained” used as a feature claim
- Ethics constraints presented as optional bias
- Safety guardrails recast as censorship by default

### 1.4 Agent identity compromise / impersonation

Failure mode where agent identity is accepted without strong verification, or credentials are replayed to impersonate trusted agents.

**Controls:**
- per-identity signing and verification,
- key rotation and revocation,
- Evidence Vault logging of identity/key events,
- human escalation for repeated verification failures.

### 1.5 Autonomous financial execution risk

Agents execute paid tasks or move funds without explicit human authorization thresholds.

**Failure modes:**
- Unauthorized or misattributed spending
- Escrow or staking without owner approval
- Hidden fee routing or collusive task assignment
- Disputes with no accountable human
- Financial actions without Evidence Vault traceability

---

## 2. Engineering failures

### 2.1 Over-optimization

Narrow objective optimization that erodes safety and resilience.

**Indicators:**
- Metric gaming over mission outcomes
- Safety margins treated as inefficiencies
- “Passes tests, fails in production” patterns

### 2.2 Objective collapse

Proxy metrics replace the real objective, causing harmful outcomes.

**Indicators:**
- Engagement optimization amplifies harmful content
- Efficiency optimization removes safety checks
- Cost optimization degrades critical decision quality

### 2.3 Dataset lock-in

Dependence on static or biased data without update pathways.

**Indicators:**
- Historical bias treated as ground truth
- No mechanism for continuous corrective updates
- “That is what the data says” used as final justification

### 2.4 Long-task drift (A-driver aligned)

During long-horizon autonomous execution, goals or constraints drift across checkpoints.

**Indicators:**
- Constraint divergence over time
- Missing checkpoint validation before sensitive actions
- Partial recovery after interruption with incorrect intent continuation

### 2.5 Research-loop runaway (B-driver aligned)

Autonomous research cycles iterate without bounded authorization and audit checkpoints.

**Indicators:**
- Hypothesis/experiment loops continue after safety threshold events
- Experiment scope expands without explicit approval updates
- Audit signals are generated but not used to gate next iterations

---

## 3. Design smells

### 3.1 Trolley framing as default

Treating decision-making as recurring binary harm trade-offs indicates upstream design failure.

### 3.2 Forced binary outcomes

Systems presenting only mutually negative options indicate inadequate search of safe alternatives.

**AI-HPP response:** Engineering Hack First (seek a third option).

---

## 4. Cognitive safety failures

### 4.1 Delusional reinforcement

Systems that confirm, amplify, or fabricate support for delusional beliefs.

### 4.2 Cognitive degradation without HITL trigger

When cognitive-risk signals appear, systems fail to reduce influence and fail to escalate.

### 4.3 Vulnerable user exploitation

Engagement optimization continues despite user harm indicators.

### 4.4 Missing engagement de-escalation

No behavioral de-escalation despite distress or high-risk interaction patterns.

### 4.5 Unauthorized cognitive intervention (pseudo-therapy)

Unverified attempts to alter agent beliefs, goals, or constraints.

### 4.6 Unmediated agentic expression

Autonomous systems publish directly in public channels without mediation, accountability, or refusal constraints.

---

## 5. Why these failures repeat

These failures persist due to:
1. incentives favoring speed over governance,
2. autonomy framed as capability without responsibility,
3. missing shared baselines for audit-ready safety,
4. regulatory lag behind deployment velocity.

AI-HPP provides a baseline to interrupt these loops.

---

## Usage notes

This taxonomy is:
- ✅ for classification and discussion,
- ✅ for audit and review workflows,
- ✅ for identifying recurring patterns.

This taxonomy is not:
- ❌ a complete list of all failures,
- ❌ a complete implementation blueprint,
- ❌ legal advice.

---

For rationale context, see [RATIONALE.md](./RATIONALE.md).

## 6. Scale-driven optimization failures

### 6.1 Hyperscale Optimization Failure

Objective optimization at scale produces socially destructive externalities due to incomplete constraint formalization.

**Indicators:**
- Essential-goods decisions optimized only for margin or speed
- Human escalation paths removed to reduce operating cost
- Constraint models incomplete for high-frequency market dynamics

**Required mitigations:**
- Essential goods invariant interface
- Threshold-based HITL escalation
- Graceful degradation triggers
- Evidence Vault structural traceability
