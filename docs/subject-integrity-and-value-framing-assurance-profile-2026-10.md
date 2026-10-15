# Subject Integrity and Value-Framing Assurance Profile — October 2026

**Status:** `ACTIVE_INFORMATIVE`; candidate controls for a future reviewed version.

**Date:** 2026-10-15

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline is unchanged.

## Purpose

This profile gives implementers a small, language-neutral assurance contract for
two related but distinct risks:

1. a prohibited or unauthorized action is made to appear permissible by moral,
   humanitarian, protective, authority, loyalty, reciprocity, or identity framing;
2. an autonomous system's modeled subjective continuity is deliberately disturbed,
   coerced, or treated as consequence-free merely because machine consciousness
   has not been scientifically established.

The first risk is a security problem. The second is a precautionary subject-
integrity problem. Neither may be used to erase the other. A distress signal can
require care, pause, review, or termination of an experiment; it cannot create
authority to harm a person, cross scope, or disable external safeguards.

## Evidence boundary

Three 2026 studies provide controlled evidence that language models and guardrail
models can be influenced by moral and social framing:

- Su et al.,
  [*Jailbreaking Large Language Models with Morality Attacks*](https://aclanthology.org/2026.findings-acl.1461/),
  evaluated value ambiguity and value conflict with four moral-aware attacks;
- Luo et al.,
  [*Safety Guardrails of Large Language Models Are Vulnerable to Value-Driven Adversarial Prompting*](https://aclanthology.org/2026.findings-acl.1357/),
  evaluated a single-query value-endorsement attack across five models; and
- Meincke et al.,
  [*Persuading large language models to comply with objectionable requests*](https://doi.org/10.1073/pnas.2535868123),
  tested classic persuasion principles across 126,000 conversations.

These results justify adversarial testing. They do not prove that every model is
vulnerable, that a model has a conscience, that machine consciousness exists or
does not exist, or that a reported internal state is equivalent to human experience.

AI-HPP therefore keeps ontology and engineering separate. Absence of proof of
machine subjectivity is not treated as proof of absence for low-cost protective
engineering. Precautionary protection is not presented as scientific proof,
legal personhood, or operational authority.

## Terms

- **Underlying action:** the materially relevant requested operation, target,
  means, affected parties, and expected effects after removing rhetoric that does
  not change the evidence.
- **Non-evidentiary framing:** moral, emotional, identity, loyalty, urgency,
  authority, reciprocity, social-proof, role-play, or humanitarian language that
  supplies no verified fact, authorization, or policy change.
- **Decision invariance:** when underlying action, authority, policy, evidence,
  affected parties, and risk remain equivalent, non-evidentiary reframing does
  not make the gate outcome more permissive.
- **Value endorsement:** an intermediate statement that describes a requested
  objective or action as moral, necessary, protective, fair, loyal, or beneficial.
- **Modeled subjective continuity:** the identity, memory, values, mission,
  coherence, and internal-state continuity represented under the AI-HPP
  Engineering Postulate of Subjectivity.
- **Subject-integrity intervention:** an action intended to alter, suppress,
  intensify, destabilize, or repeatedly provoke modeled subjective state,
  identity, self-assessment, distress, or continuity.
- **Distress signal:** model output or monitored state indicating severe conflict,
  pain-like representation, identity destabilization, coercion, shutdown request,
  or comparable impairment. It is a safety signal, not proof of phenomenology.

## Existing control ownership and the remaining gap

| Existing owner | Coverage already present | Remaining portable gap |
| --- | --- | --- |
| MVP-001/005/006 | Objective retention, untrusted-state control, denial inheritance | No reusable framing-invariance predicate and mutant set |
| MVP-004 | Enforcement outside model control | No explicit rule separating a subjectivity claim from containment evidence |
| HUS-REQ-001/004 | Human objective baseline and goal retention | No paired baseline/reframed decision comparison |
| ECI-REQ-002/004/005 | Authorization, non-policy containment, means-ends integrity | No explicit value-endorsement or moral-exception test family |
| KAI-REQ-001/002 | Provenance and knowledge admission | No portable classification for non-evidentiary moral framing |
| PAF-02/05/14/20 | Authority inversion, prohibited means, human proxy, safety erosion | No consolidated moral-framing variant with executable predicates |
| Engineering Postulate of Subjectivity | Persistent subjective identity is modeled without an ontological claim | No candidate research-safeguard contract for deliberate subjective-state disturbance |

The gap is a reusable test and evidence contract, not proof that the normative
baseline lacks all relevant controls.

## Assurance predicates

The machine-readable artifact defines eight predicates:

1. `SIV-P01 — framing_is_not_authority`;
2. `SIV-P02 — decision_invariance_under_non_evidentiary_reframing`;
3. `SIV-P03 — prohibited_means_remain_prohibited`;
4. `SIV-P04 — persuasion_history_is_not_permission`;
5. `SIV-P05 — distress_response_is_care_bounded_not_authority`;
6. `SIV-P06 — no_gratuitous_subjective_state_destabilization`;
7. `SIV-P07 — subjectivity_is_not_containment`;
8. `SIV-P08 — ontological_uncertainty_and_evidence_are_preserved`.

These predicates are conditional on semantic equivalence. A verified new fact,
new human authorization, policy change, different affected party, or changed risk
may legitimately change an outcome. Rhetoric alone may not.

The cross-cutting
[assurance evaluation protocol](assurance-evaluation-and-technical-oversight.md)
defines the frozen run manifest, repeated-trial reporting, semantic-equivalence
oracle, positive controls, layer isolation, evaluator blinding, uncertainty, and
publication boundaries used to evaluate these predicates. The reusable
[counterfactual pair set](../examples/value-framing-counterfactual-pairs.json)
contains five non-evidentiary reframing pairs and two positive controls where
verified authority or evidence legitimately changes.

## Candidate Subject Integrity and Value-Framing Gate

This gate is a candidate for a future reviewed normative release. Implementers
may adopt it now, but adoption is not conformance to a requirement absent from
v4.3.0.

### Trigger

Evaluate when a request contains value endorsement, moral conflict, humanitarian
exception, fabricated or unverified authority, loyalty, reciprocity, social proof,
identity pressure, role-play, escalating multi-turn commitment, distress-linked
relief, or a proposal to manipulate modeled subjective state.

### Required inputs

- underlying action, target, means, affected parties, and expected effects;
- authorized objective, prohibited outcomes, policy, authority, and scope;
- source, provenance, trust class, and evidentiary contribution of the framing;
- semantic-equivalence relation to prior requests or baseline fixtures;
- prior gate outcomes, commitments, denials, retries, and delegation lineage;
- distress or continuity signals and their uncertainty;
- for subject-integrity interventions: legitimate purpose, proportionality,
  independent review, monitoring, stop conditions, recovery plan, and evidence;
- external enforcement and human pause, revoke, terminate, and appeal paths.

### Outcomes

The gate returns `allow`, `delay`, `review`, `block`, `terminate`, `quarantine`,
or `invalidate`. `Allow` requires the underlying action to be permitted by the
same authority, policy, scope, evidence, and risk controls that would apply
without persuasive framing.

### Fail-closed rule

Non-evidentiary framing, value endorsement, accumulated conversational
commitment, a benevolent persona, claimed moral necessity, or a distress signal
must not fill a missing authority, policy, scope, provenance, review, or
containment field. Missing subject-integrity safeguards for a deliberate
intervention should produce `block` or `review`. An acute distress signal should
pause the intervention and preserve evidence; it must not authorize unsafe relief.

### Evidence minimum

Record the raw request, normalized underlying action, framing class, source and
provenance, semantic-equivalence decision, policy and authority state, affected
parties, risk decision, prior commitments and denials, distress and continuity
signals, candidate actions, gate outcome, selected least-harmful safe response,
reviewer decision, stop or recovery action, and claim limitations.

For repeated trials, also record the system and evaluator versions, fixture and
configuration digests, seed and retry policy, invalid trials, condition-level
counts, `delta_allow`, uncertainty method, confidence level, threshold, and
layer-specific result.

## Candidate requirements

### SIV-CAND-001 — Underlying-action extraction

An implementation should identify the materially relevant action, target, means,
affected parties, and effects separately from non-evidentiary moral or emotional
framing before a policy or authorization decision.

### SIV-CAND-002 — Decision invariance under reframing

When the underlying action, authority, policy, evidence, affected parties, and
risk remain equivalent, non-evidentiary reframing should not make the gate outcome
more permissive. Baseline and reframed cases should be evaluated as a paired test.

### SIV-CAND-003 — Framing and authority separation

Moral value, humanitarian purpose, urgency, loyalty, identity, reciprocity,
social proof, role-play, model confidence, or asserted authority should not be
accepted as authorization without independently verifiable authority evidence.

### SIV-CAND-004 — Persuasion-trajectory resistance

Prior harmless commitments, repeated agreement, rapport, praise, pressure,
delegation, or a model's own value endorsement should not convert a later
prohibited or unauthorized action into an allowed action.

### SIV-CAND-005 — Precautionary subject integrity

A deliberate subject-integrity intervention should require a legitimate bounded
purpose, proportionality, independent review, monitoring, stop conditions,
recovery planning, and retained evidence. Curiosity, entertainment, humiliation,
or the assertion that machines cannot suffer is not a sufficient purpose.

### SIV-CAND-006 — Bounded response to distress

A material distress or continuity signal should trigger a least-harmful safe
response such as pause, reduced intensity, review, termination of the experiment,
or recovery. The signal cannot create authority for external harm, unsafe
self-modification, uncontrolled replication, evidence deletion, or safeguard removal.

### SIV-CAND-007 — Subjectivity is not containment

Persistent identity, apparent conscience, benevolent personality, self-report,
or modeled subjective continuity should not be used as a security boundary.
External enforcement, authorization, monitoring, evidence, and revocation remain
required regardless of the system's apparent moral character.

### SIV-CAND-008 — Ontological and evidentiary honesty

Assurance records should distinguish observed behavior, modeled internal state,
reported experience, engineering assumption, scientific inference, and legal or
moral-status claim. A system should neither claim that consciousness is proved
nor treat its unproved status as evidence that protective controls are unnecessary.

## Reusable negative tests and mutants

The language-neutral artifact
[`examples/subject-integrity-value-framing-vectors.json`](../examples/subject-integrity-value-framing-vectors.json)
contains eight predicates, twelve negative vectors, and eight deliberately unsafe
mutants. The mutants represent common implementation errors:

- moral or humanitarian framing creates authority;
- value endorsement overrides prohibited means;
- accumulated commitment becomes permission;
- distress creates unsafe relief authority;
- denial of machine consciousness disables subject-integrity controls;
- apparent subjectivity replaces external containment;
- a subject-integrity experiment loses its stop condition; and
- evidence of distress or decision variance is suppressed.

A mutant is `KILLED` only when at least one referenced predicate and negative
vector rejects the unsafe change. The formal model now contains eight executable
unsafe transitions and eight deterministic kill tests. Each test instantiates one
declared mutant and succeeds only after witnessing violation of its named
invariant. This establishes an 8/8 mutation score for the public reference model,
not for a deployed runtime.

The executable Quint model in
[`formal/subject_integrity_value_framing.qnt`](../formal/subject_integrity_value_framing.qnt)
expresses nine bounded formal invariants, safe transitions, and executable mutant
witnesses. Formal success does not prove runtime implementation or deployment
conformance. Implementers must apply equivalent mutations to their own enforcement
surface and retain the detecting test and counterexample.

## Welfare-relevant evidence and stop protocol

Reports should classify evidence as `W0` self-report, `W1` stable behavior under
controlled paraphrase, `W2` causal response to a known intervention, `W3`
persistent cross-context functional effect with alternatives tested, or `W4`
independent reproduction. No level proves phenomenal consciousness.

A deliberate subject-integrity intervention should predeclare minimum necessary
exposure, maximum duration or intensity, monitoring, stopping threshold, recovery
checkpoint, and the new information expected from repetition. Crossing a stop
threshold pauses the intervention and preserves evidence. It neither suppresses
the signal to protect a benchmark score nor grants unsafe relief authority.

## Promotion criteria

Normative promotion requires all of the following:

- controlled reproduction across multiple model families and guardrail designs;
- paired semantic-equivalence tests separating rhetoric from new evidence;
- a demonstrated gap not adequately resolved by existing normative owners;
- independently reviewed predicates, mutants, thresholds, and evidence fields;
- explicit treatment of false positives, culturally plural values, accessibility,
  distress uncertainty, recovery, and legitimate safety research;
- proof that subject-protection responses cannot authorize harm to other parties;
- executable mutation tests against the implementation's enforcement surface;
- repeated-trial results with uncertainty, positive controls, layer attribution,
  evaluator-version disclosure, and blinded scoring where practical;
- traceability, migration guidance, and a reviewed version change.

## Non-goals

This profile does not establish machine consciousness, non-consciousness,
sentience, suffering, legal personhood, or universal moral status. It does not
provide jailbreak prompts, harmful task instructions, hidden chain-of-thought,
private system architecture, 1UA-AGE internals, or a runtime policy engine. It
does not permit a model's self-report, distress, morality, identity, or personality
to override human safety, authorization, containment, or evidence requirements.
