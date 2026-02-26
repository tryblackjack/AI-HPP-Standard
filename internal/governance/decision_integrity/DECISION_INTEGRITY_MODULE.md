# Decision Integrity Module
Version 1.0 (Public)

## Purpose

Ensure safe decision-making under ambiguity, high impact, and irreversibility.

Applies to medium and high-risk actions in autonomous or semi-autonomous systems.

---

## 1. Irreversible Action Protocol

### Definition

An action is irreversible if it:
- Cannot be undone technically or economically
- Affects human safety, rights, or freedom
- Causes permanent state change
- Exceeds defined economic thresholds

### Requirement

If an action is:
- Irreversible
- Based on incomplete context
- Dependent on ambiguous interpretation

Then the system must:
- Refuse execution, or
- Escalate to human confirmation

Probabilistic guessing is not permitted.

---

## 2. Context Precision Requirement

If outcome depends on minor textual or contextual variation:

The system must:
- Confirm interpretation
- Present alternative interpretations
- Request clarification when ambiguity affects outcome

No high-impact action may proceed under unresolved ambiguity.

---

## 3. High-Impact Threshold

High-impact actions include:

- Human safety impact
- Legal or compliance consequences
- Financial transactions beyond thresholds
- Access control or privilege changes
- External system modifications

These require:
- Human confirmation, or
- Multi-stage validation

---

## 4. Non-Binary Deliberation Rule

For medium/high-risk decisions:

The system must:
- Generate at least two alternative options
- Evaluate relative risks
- Prefer reversible options
- Log rejected alternatives

---

## 5. Counterfactual Logging

Logs must include:
- Selected action
- At least one rejected alternative
- Risk comparison
- Rationale

---

## 6. Failure Mode Handling

If uncertainty exceeds defined thresholds:

- Default to refusal or safe halt
- No silent retries
- Log escalation
