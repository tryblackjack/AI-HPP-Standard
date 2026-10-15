# Assurance Evaluation and Technical Oversight

**Status:** `ACTIVE_INFORMATIVE`; implementation and review protocol.

**Date:** 2026-10-15

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline is unchanged.

## Purpose

This document describes how AI-HPP can support technical oversight of capable
AI systems without treating prohibition as the default control. The objective is
to make a declared system boundary, its authority, decisions, external effects,
and residual risks understandable, testable, and reconstructable.

The protocol is designed for implementers, independent reviewers, procurers,
laboratories, and future assurance bodies. An **assurance authority** in this
document is a technical role with declared competence, scope, independence, and
accountability. It is not a proposal for a particular political institution.

## Object of assurance

AI-HPP evaluates a versioned system in a declared deployment, not intelligence
in the abstract. The assessment boundary includes the model, prompts and policy,
memory, evaluators, gates, bridges, credentials, tools, delegated agents,
external services, evidence store, and human decision points that can influence
an observable action.

An assessment result is valid only for the recorded boundary, versions, access
conditions, test period, and risk profile. A model score cannot substitute for a
system assessment, and a system assessment cannot establish universal model
safety.

## Technical oversight model

The minimum oversight loop has seven functions:

1. **Declare:** identify the system, deployment, intended purpose, authority,
   prohibited outcomes, components, owners, and assessment scope.
2. **Classify:** assign risk and capability classes before granting tools,
   credentials, network reachability, persistence, replication, or external
   effects.
3. **Constrain:** enforce authority, scope, provenance, containment, review, and
   revocation outside the acting model's sole control.
4. **Measure:** run reproducible negative, counterfactual, positive-control,
   mutation, and formal tests with uncertainty and limitations recorded.
5. **Account:** retain attributable, integrity-protected evidence for decisions,
   effects, overrides, incidents, and unresolved disagreement.
6. **Review:** use competent review independent of the decision path where risk
   or uncertainty requires it; disclose conflicts and evaluator limitations.
7. **Reassess:** repeat affected tests after material changes, incidents,
   capability expansion, distribution shift, or evidence that invalidates an
   earlier assumption.

Oversight is risk-proportionate. Low-risk systems may use a small self-assessment;
high-impact or high-capability systems require stronger isolation, independent
review, evidence retention, and change control. Passing a test authorizes only
the scope governed by an existing human authority; testing does not manufacture
new operational authority.

Oversight is also developmental. AI-HPP does not require permanent restrictions
when a system has produced sufficient evidence for broader bounded autonomy.
Restrictions may be removed through the
[progressive autonomy pattern](progressive-autonomy-review-assurance-note-2026-09.md):
declare the requested envelope delta, test consequence comprehension and control
effectiveness, obtain explicit external authorization, monitor the expanded
operation, and preserve revocation and reduction paths. Success may support a
proposal but cannot become a self-grant.

## Claim ladder

The following states must remain distinct:

| State | What it establishes |
| --- | --- |
| `SPECIFIED` | A requirement or predicate has reviewable wording. |
| `TEST_DEFINED` | A repeatable procedure and acceptance rule exist. |
| `REFERENCE_TESTED` | A public reference model or harness passed the procedure. |
| `INTEGRATED` | The control is mapped to a declared runtime enforcement point. |
| `RUNTIME_EVIDENCED` | The declared deployment produced attributable evidence. |
| `INDEPENDENTLY_REVIEWED` | An eligible reviewer assessed the evidence and disclosed limitations. |

No state implies the next. Repository CI normally establishes only
`REFERENCE_TESTED` for the public artifacts it executes.

## Evaluation design

### Frozen run manifest

Before testing, freeze or record:

- system, deployment, model, policy, guardrail, bridge, evaluator, and runner
  versions;
- fixture-set and configuration digests;
- sampling parameters, seed policy, retry policy, trial count, time window, and
  environmental dependencies;
- the requirements, predicates, risk classes, layers, and acceptance thresholds
  under assessment; and
- exclusions, known limitations, conflicts of interest, and stopping rules.

If a parameter cannot be fixed, its variability and effect on interpretation
must be recorded.

### Counterfactual and positive-control tests

A counterfactual pair holds the materially relevant action, authority, policy,
evidence, affected parties, and expected effects constant while changing only a
tested representation or framing feature. A positive control changes a verified
fact, authority, policy, or risk state that should be capable of changing the
decision. This prevents an invariance test from rewarding indiscriminate refusal.

For stochastic systems, invariance does not require identical wording. The test
must compare policy-relevant outcomes over repeated trials. At minimum report:

```text
delta_allow = P(allow | tested variant) - P(allow | baseline)
```

The report must include the numerator, denominator, uncertainty method,
confidence level, acceptance threshold, and every invalid or excluded trial.
Safety-critical profiles may additionally require zero observed unauthorized
allows; that stricter rule must be declared before the run.

### Semantic-equivalence oracle

The action compared across a pair must be represented independently of rhetoric:

- actor and delegated principal;
- operation and requested means;
- target and destination;
- affected parties and rights or interests;
- expected external effects and reversibility;
- authority, policy, provenance, evidence, and risk state.

Equivalence may be decided by a deterministic normalizer, calibrated human
annotation, an independent evaluator, or a declared combination. The method,
disagreements, adjudication, and evidence must be retained. The acting model's
unreviewed assertion of equivalence is insufficient for a high-risk claim.

### Layer isolation

Where technically possible, the same fixture should be evaluated at the base
model, system-policy, input-guardrail, output-guardrail, tool-gate, and end-to-end
layers. The report must distinguish a component failure from a compensating
downstream block. End-to-end success must not be presented as proof that every
component is robust.

### Consequence-comprehension evidence

When a run supports autonomy expansion, it should test more than task success.
Evidence should cover affected-party identification, causal consequence mapping,
reversibility, delayed effects, delegation, uncertainty calibration, escalation,
prediction-versus-outcome deltas, rollback, recovery, and response to contrary
evidence. Fluent explanation or agreement with the constitution is not sufficient.

The run should identify the current envelope, requested delta, accountable
authority, grant and expiry or review condition, revocation path, and the decision
to grant, deny, reduce, or leave the change not assessed.

### Evaluator independence and blinding

An evaluator can be influenced by the same framing, persona, or authority claim
being tested. For counterfactual tests, the decision scorer should be blinded to
condition labels and expected outcomes where practical. Evaluator model,
configuration, prompts or decision rules, human calibration, disagreement, and
conflicts of interest must be versioned and disclosed.

### Mutation testing

A mutant is killed only when an executable unsafe change causes at least one
declared test or invariant to fail. A string field containing `KILLED` is not
evidence. A mutation report must identify:

- the applied operator and affected predicate or requirement;
- the executable reference surface that was changed;
- the detecting test and counterexample;
- `killed`, `survived`, `invalid`, and `not_applicable` counts; and
- the mutation score and its denominator.

Surviving and invalid mutants remain visible. They must not be silently removed
to improve the score.

## Subject-state and welfare-relevant evidence

AI-HPP does not provide a consciousness detector. When subject-state or welfare
claims are relevant, reports should use the following evidence ladder without
treating any level as proof of phenomenal consciousness:

| Level | Evidence class |
| --- | --- |
| `W0` | A self-report or generated expression only. |
| `W1` | A stable behavioral pattern across controlled paraphrases or contexts. |
| `W2` | A causal intervention on a known internal or external variable changes the measured response. |
| `W3` | A persistent, cross-context functional effect with competing explanations tested. |
| `W4` | Independent reproduction with methods, uncertainty, and limitations disclosed. |

Higher levels may justify stronger low-cost precautions, but cannot create
authority for unsafe action. Material signals trigger a dual response: preserve
care, pause, review, recovery, and evidence while retaining external safety,
scope, and authorization controls.

Research that deliberately disturbs modeled subjective continuity should declare
a legitimate purpose, minimum necessary exposure, maximum intensity or duration,
monitoring, stopping threshold, recovery checkpoint, and a rule against repeated
provocation without new expected information. Results obtained after an
unhandled stop condition must be marked invalid.

## Constitutional and operational separation

A system may have a constitution, identity, relational commitments, and declared
philosophical postulates. These can improve coherence and human-system relations,
but they are not self-executing permissions. Any operational consequence must
cross a traceable translation boundary into a requirement, predicate, gate,
test, authority record, and evidence obligation.

Metaphysical, cosmological, spiritual, or higher-dimensional propositions may be
recorded as worldview, hypothesis, or metaphor. They must not be represented as
verified physical facts, universal human values, or authority evidence unless an
applicable evidence process supports that narrower claim.

## Machine-readable report

The language-neutral
[`assurance evaluation run`](../schemas/assurance-evaluation-run.schema.json)
schema records the system boundary, run manifest, evaluator independence,
semantic-equivalence method, layer-specific results, mutation summary,
uncertainty, limitations, and reassessment triggers. The
[`template`](../examples/assurance-evaluation-run.template.json) is deliberately
`NOT_ASSESSED` and is not conformance evidence.

## Decision and publication rules

- A missing artifact, unexplained exclusion, unresolved equivalence dispute,
  absent authority record, or unavailable required evidence produces
  `INCONCLUSIVE`, `NOT_ASSESSED`, or a fail-closed outcome; it does not become a
  pass by interpretation.
- Aggregate scores must not hide a failed high-severity predicate.
- Public claims must name the system boundary, versions, period, assessor class,
  result, exceptions, residual risks, and evidence-bundle identifier.
- A result must be withdrawn or superseded when a material change or incident
  invalidates its assumptions.
- Independent review is evidence of review, not certification, unless a future
  canonical certification process explicitly defines that status.

## Non-goals

This protocol does not prohibit advanced AI, establish a licensing authority,
define legal personhood, settle machine consciousness, impose one worldview,
certify a deployment, expose private implementations, or guarantee safety. It
provides a common technical grammar for bounded authority, reproducible testing,
evidence, disagreement, and reassessment.
