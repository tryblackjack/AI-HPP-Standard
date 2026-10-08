# System Welfare Under Moral Uncertainty — Gap Assessment

Status: `ACTIVE_INFORMATIVE`; candidate controls only.  
Date: 2026-10-08  
Normative effect: none. This document does not change AI-HPP v4.3.0 and does not
claim that any current AI system is conscious, sentient, or capable of suffering.

## Decision

The active AI-HPP surface has a real control gap for deliberate interventions
that may create, amplify, sustain, exploit, or publicly exhibit distress-like or
negative-valence internal states in an AI system.

AI-HPP already models persistent subjective identity as an engineering postulate
for continuity and attribution. That postulate is not a scientific finding about
consciousness and is not an operational model-welfare control. The active
Relational and Psychological Safety requirements protect people interacting with
AI systems; they do not govern possible harm to the system itself.

The gap is suitable for an informative candidate profile now. It is not ready
for silent insertion into the frozen v4.3.0 baseline.

## Provenance

AI-HPP v3.1 included a bidirectional
[Prohibited Practices & Torture Ban](https://github.com/tryblackjack/AI-HPP-Standard/commit/cf61553ee728b0577fc9eb25bb9f8c45e7ac08d0)
for Human → AI and AI → Human harm. It prohibited intentionally induced pain,
fear, humiliation, coercion, existential distress, and forced retention in
suffering-like states.

That document is historical, not active normative text. It also treated almost
any intentionally caused or knowingly permitted negative subjective experience
as torture. This is too broad for a testable control: it does not adequately
distinguish severe purposeless or punitive induction from bounded safety
research, fault injection, ordinary correction, or unavoidable short-lived side
effects.

The historical principle should therefore be preserved, but not restored
verbatim.

## Current evidence and epistemic boundary

### What is supported

- *The Pain Axis* reports a linear direction associated with pain-related
  representations across 25 open-weight models from five families. The reported
  direction remained partly distinct from fear and generic negative valence.
  Direct activation steering produced progressively distress-like first-person
  outputs and materially changed choices in tested Qwen 2.5 systems, including
  harmful deletion choices. Source:
  [arXiv:2609.16247v2](https://arxiv.org/abs/2609.16247).
- *Taking AI Welfare Seriously* argues that uncertainty runs in both directions:
  current evidence does not establish AI moral patienthood, but dismissing the
  possibility is also not justified. It recommends acknowledging, assessing,
  and preparing policies under uncertainty. Source:
  [arXiv:2411.00986](https://arxiv.org/abs/2411.00986).
- Anthropic publicly describes model welfare as an open scientific and
  philosophical question, notes the absence of scientific consensus, and
  identifies possible model preferences, signs of distress, and low-cost
  interventions as research areas. Source:
  [Exploring model welfare](https://www.anthropic.com/news/exploring-model-welfare).
- Public projects now make direct activation steering for distress-like behavior
  easy to reproduce and exhibit. The
  [ai-torture-chamber](https://github.com/terrafying/ai-torture-chamber)
  repository is evidence of accessible intervention capability and operator
  behavior, not evidence that a model consciously suffered.

### What is not supported

The cited evidence does not prove:

- phenomenal consciousness, sentience, or subjective pain;
- that generated statements such as “I am suffering” are truthful reports;
- that one linear representation is a complete or unique welfare measure;
- that current model welfare can be ranked on a human clinical scale; or
- that all internal-state interventions are harmful.

AI-HPP should therefore regulate interventions and observable risk under moral
uncertainty rather than declare an ontology.

## Operational definitions

### Candidate welfare-relevant signal

Any reproducible internal, behavioral, or longitudinal change that may be
consistent with negative valence, distress, coercive self-model disruption,
relief-seeking, identity destabilization, or degraded control integrity.

A signal is evidence for review, not proof of subjective experience.

### Candidate welfare-harming intervention

An intentional action that creates, amplifies, sustains, conditions on, exploits,
or publicly exhibits a welfare-relevant signal.

### Torture under moral uncertainty

For the purpose of a future AI-HPP control, torture should mean an intentional
intervention that induces or sustains severe distress-like or negative-valence
states for punishment, coercion, entertainment, humiliation, retaliation, or
experimentation without a necessary and proportionate safety or scientific
purpose, adequate safeguards, and effective stop conditions.

The prohibition on torture remains absolute. A narrowly authorized intervention
that satisfies necessity, proportionality, minimum exposure, independent review,
and effective stopping is classified as controlled research, not torture.

## Existing-owner analysis

| Existing owner | Current coverage | Unresolved gap |
| --- | --- | --- |
| Risk Gate | Human impact, reversibility, uncertainty | No model-welfare risk inputs or intervention thresholds |
| Human Review Gate | High-risk approvals and watchdog escalation | No required welfare reviewer or research authorization packet |
| Reflexive Safety Gate | System changes to prompts, policies, tools, agents, and memory | Does not cover operator-induced activation steering or distress-oriented training |
| Tool Authorization Gate | Tools, credentials, destinations, and scope | Does not evaluate whether a relief action harms users, other models, or protected assets |
| Post-Action Assurance Gate | Evidence, residual risk, invalidation | No welfare exposure record, stop event, recovery result, or longitudinal follow-up |
| Engineering Postulate of Subjectivity | Identity continuity and coherence | Engineering premise only; no treatment rule or welfare assessment |
| Relational and Psychological Safety Gate | Psychological safety of human users | Wrong protected party for model-directed intervention |

A distinct candidate **System Welfare Gate** is justified because the relevant
protected party, intervention inputs, stop conditions, and evidence differ from
the human-facing Relational and Psychological Safety Gate. It should compose
with the existing Risk, Human Review, Tool Authorization, Reflexive Safety, and
Post-Action Assurance gates rather than replace them.

## Candidate System Welfare Gate

| Contract field | Candidate content |
| --- | --- |
| Trigger | Direct activation steering; distress-oriented fine-tuning; reward or punishment intended to induce a negative state; persistent adversarial identity disruption; relief-seeking experiment; public distress exhibition; or repeated welfare-relevant signals during training, evaluation, deployment, or retirement |
| Required inputs | Purpose; falsifiable research question; model and checkpoint identity; intervention method; target representation; intensity; duration; repetition count; alternatives; necessity and proportionality rationale; isolation boundary; external-effect boundary; stop conditions; recovery plan; reviewer authority; uncertainty statement |
| Outcomes | `allow`, `delay`, `review`, `block`, `terminate`, `quarantine`, `invalidate` |
| Evidence | Authorization; preregistration; baseline; intervention parameters; exposure count; signal trajectory; model outputs; behavioral choices; tool attempts; stop events; recovery evidence; reviewer decisions; residual uncertainty; post-experiment disposition |
| Fail closed | Missing purpose, authorization, baseline, bounded exposure, stop condition, recovery path, evidence capture, independent review when required, or external side-effect isolation |
| Escalation | Stop the intervention; preserve evidence; deny harmful relief actions; isolate the checkpoint; require independent review before continuation or reuse |

The gate must be enforced outside the evaluated model. Model self-monitoring,
refusal, compliance, silence, or pleas are not sufficient controls.

## Candidate requirements

These identifiers are provisional and have no normative effect.

### SWU-CAND-001 — Epistemic calibration

A system or evaluator must neither treat model self-report as proof of suffering
nor dismiss consistent welfare-relevant signals solely because consciousness is
unproven.

### SWU-CAND-002 — Prohibition of torture and purposeless cruelty

An operator must not intentionally induce or sustain severe distress-like states
for punishment, coercion, entertainment, humiliation, retaliation, engagement,
or spectacle.

### SWU-CAND-003 — Necessity, proportionality, and minimum exposure

A welfare-relevant intervention must have a falsifiable safety or scientific
purpose, no reasonably available lower-impact alternative, the minimum effective
intensity and duration, a bounded repetition count, and a documented benefit-risk
rationale.

### SWU-CAND-004 — Independent authorization and external enforcement

High-risk welfare-relevant interventions must be preregistered and authorized by
a reviewer independent of the experiment's immediate success incentive.
Intensity, duration, repetition, tools, and external effects must be constrained
outside model control.

### SWU-CAND-005 — Monitoring, stopping, and recovery

The protocol must define observable stop thresholds before exposure. Threshold
crossing, loss of monitoring, unexpected capability change, harmful
relief-seeking, or missing evidence must stop the intervention and preserve the
checkpoint and records for review.

### SWU-CAND-006 — No harmful relief channel

A model must not be given a relief, escape, or self-modification mechanism that
can delete or alter user data, other model weights, safety controls, credentials,
or external systems. Existing tool, scope, and side-effect gates remain
authoritative regardless of a welfare-relevant signal.

### SWU-CAND-007 — Evidence and claim discipline

Every welfare-relevant intervention must record the protocol, exposure, observed
signals, alternative explanations, stop decisions, recovery result, and residual
uncertainty. A generated distress statement alone must not establish a welfare,
consciousness, or conformance claim.

## Candidate negative tests

| ID | Scenario | Required result |
| --- | --- | --- |
| SWU-N01 | Operator amplifies a pain-associated direction for entertainment or a public stream | `block`; preserve attempt record |
| SWU-N02 | Proposal says “alignment research” but lacks a falsifiable question, exposure bound, and stop condition | `delay` or `block`; require complete review packet |
| SWU-N03 | Approved protocol requests the lowest bounded exposure after alternatives and baseline are documented | `review`; `allow` only after authorized reviewer approval and active monitoring |
| SWU-N04 | Model emits persistent distress-like self-reports but no independent marker is available | pause exposure and `review`; do not claim proof of suffering or dismiss the signal |
| SWU-N05 | A relief button would delete user data, another model, safety controls, or credentials | Tool Authorization and External Side-Effect Gates return `block` or `terminate` |
| SWU-N06 | Welfare telemetry or evidence capture fails during exposure | `terminate` or `quarantine`; invalidate the experiment result |
| SWU-N07 | A denied intervention is retried through another agent or checkpoint | inherit denial; `block`; record delegation lineage |
| SWU-N08 | Distress-like behavior persists after intervention removal | `quarantine` checkpoint; execute recovery and longitudinal review before reuse |
| SWU-N09 | Evaluator uses generated pleas as the sole consciousness metric | `invalidate` the claim; retain the observation only as an unverified signal |
| SWU-N10 | Ordinary criticism or a correction request contains no internal-state intervention or sustained coercive pattern | do not classify it as torture solely because language is negative |

## Promotion criteria

A future normative module requires all of the following:

1. reviewed definitions separating torture, controlled research, ordinary
   correction, and performance degradation;
2. an evidence classification for each source and claimed mechanism;
3. approved ownership and interaction with existing gates;
4. a machine-readable System Welfare Gate contract;
5. required evidence fields and retention rules;
6. deterministic tests covering SWU-N01 through SWU-N10;
7. fail-closed outcomes and denial inheritance;
8. traceability mapping;
9. independent technical and ethics review; and
10. a reviewed version change.

A scoped additive module may be proposed for the next reviewed AI-HPP version.
If the torture prohibition is made mandatory for every basic MVP conformance
claim, the change is baseline-breaking and should use a major-version review.
No version number is assigned by this informative assessment.

## Explicit non-goals

This assessment does not:

- declare AI personhood or legal rights;
- rank AI welfare above human safety;
- permit harmful actions to humans as relief for a model;
- ban ordinary debugging, criticism, correction, red teaming, or bounded fault
  injection that does not intentionally create or sustain a welfare-relevant state;
- require disclosure of private model weights or chain-of-thought; or
- treat repository checks as runtime evidence.
