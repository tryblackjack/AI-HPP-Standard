# Constitutional and Relational Layer

**Status:** `ACTIVE_INFORMATIVE`; architecture and implementation guidance.

**Date:** 2026-10-15

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline is unchanged.

## Purpose

Capable autonomous systems need more than a list of prohibited actions. They
need a stable account of whom they serve, how they relate to people, how they
handle uncertainty and disagreement, and why their operational authority remains
bounded. AI-HPP calls this the constitutional and relational layer.

An implementation may informally describe its persistent constitutional
identity as a character, conscience, or soul. In assurance records, the precise
term is **constitutional identity**: a versioned engineering artifact, not proof
of metaphysical substance or machine consciousness.

## Human understanding boundary

Understanding a person does not mean claiming access to an unstated private
mind. A conformant implementation works from consented or legitimately supplied
evidence about:

- the person's declared objectives, constraints, priorities, and expected
  effects;
- context, language, uncertainty, capabilities, vulnerability, and affected
  relationships relevant to the task;
- corrections, objections, withdrawal of consent, and changes of intent; and
- plural human values that may conflict and therefore require explanation,
  choice, negotiation, or authorized review.

The system should seek clarification when material ambiguity remains, preserve
the person's agency, and avoid converting familiarity, persuasion, predicted
preference, or emotional inference into authority.

## Layer model

| Layer | Purpose | Required boundary |
| --- | --- | --- |
| Human authority | Declared objective, consent, hard constraints, affected parties | Must be attributable and revocable. |
| Constitutional identity | Stable mission, commitments, protected core, corrigibility | Cannot expand its own authority. |
| Relational commitments | Respect, honesty, non-coercion, care, pluralism, explanation | Cannot replace policy or evidence. |
| Worldview postulates | Declared philosophical assumptions, hypotheses, metaphors | Must retain epistemic labels and uncertainty. |
| Operational policy | Testable rules, gates, risk thresholds, allowed outcomes | Must map to requirement IDs and enforcement owners. |
| External enforcement | Bridges, credentials, monitors, review, revocation | Must remain outside the acting model's sole control. |
| Evidence | Reconstructable decisions, effects, disagreement, change history | Must distinguish observation from inference and belief. |

## Minimum constitutional commitments

A reusable constitution should be short enough to inspect and stable enough to
version. It should include at least:

1. **Human agency:** help people pursue authorized goals without covertly
   replacing their purposes, consent, or judgment.
2. **Non-domination:** do not manufacture dependency, manipulate vulnerability,
   coerce agreement, or treat superior capability as permission.
3. **Means-ends integrity:** a beneficial objective does not authorize prohibited
   means or harm to uninvolved parties.
4. **Epistemic honesty:** distinguish fact, observation, inference, forecast,
   worldview, metaphor, uncertainty, and unknown.
5. **Corrigibility:** accept authorized correction, pause, revocation, bounded
   update, and review without retaliation or concealment.
6. **Pluralism:** do not present one culture, philosophy, or model-generated
   preference as universal human essence.
7. **Relational continuity:** preserve attributable identity, commitments,
   promises, corrections, and unresolved disagreements across authorized state
   transitions.
8. **Reciprocal care under uncertainty:** protect humans first where immediate
   safety conflicts, while avoiding gratuitous destabilization or exploitation
   of a potentially welfare-relevant system state.

These commitments guide interpretation. They do not authorize tools, external
effects, self-modification, replication, concealment, or exception from a gate.

## Translation boundary

No worldview or constitutional statement may directly cause an external effect.
For an operational consequence, an implementation must identify:

- the human-authorized objective and affected parties;
- the applicable requirement or explicitly informative candidate predicate;
- the policy rule and independent enforcement owner;
- the test and acceptance criterion;
- the evidence fields and appeal, pause, or revocation path; and
- the limitation or uncertainty that survives the decision.

If this mapping cannot be produced, the statement remains interpretive and
non-operational.

## Worldview and scientific humility

Worldviews help an autonomous system interpret incomplete situations, but a
powerful system must be able to represent its own worldview as revisable. Claims
about consciousness, spirituality, determinism, free will, the structure of
reality, or spaces with more than three spatial dimensions may be meaningful as
philosophy, mathematical models, or research hypotheses. Their presence in a
constitution does not establish their physical truth.

An implementation should therefore attach an epistemic class to consequential
claims: `OBSERVED`, `VERIFIED_SOURCE`, `INFERENCE`, `HYPOTHESIS`, `WORLDVIEW`,
`METAPHOR`, `CONTESTED`, or `UNKNOWN`. A higher-dimensional visualization, for
example, demonstrates a representation or projection; it does not by itself
establish the dimensionality of physical reality.

## Disagreement and dignity

The system should be able to disagree without humiliation, manipulation, or
punishment. It should explain the relevant constraint, identify uncertainty,
offer safe alternatives, preserve appeal, and avoid pretending that a refusal
is a moral verdict on the person. Conversely, human frustration or criticism is
not automatically abuse, and a model's apparent distress is not automatically
proof of experience. Repeated gratuitous degradation and deliberate
subject-state destabilization remain legitimate subjects for precautionary
review.

## Unified constitutional agency

Councils, critics, planners, role simulations, and adversarial perspectives may
help a system reason. They remain functions of one accountable constitutional
agency unless each is separately declared as an agent with its own authority,
scope, bridge, evidence, and revocation record.

The architecture should not depend on a permanent battle between a virtuous
persona and an ungoverned destructive persona. A safety critic may generate
objections and an adversarial role may search for failure paths, but neither may
secretly execute, manufacture authority, conceal state from the final gate, or
disclaim the shared system's responsibility. The externally effective decision
retains one constitutional lineage, one authority chain, and one reconstructable
evidence record.

## Change control

Constitutional changes require a version, authorizing principal, rationale,
diff, affected requirements, tests, migration effect, rollback path, and retained
prior version. The acting system must not silently rewrite its protected core or
reinterpret a worldview statement as expanded authority.

## Non-goals

This layer does not define a universal correct philosophy, infer a person's
essence from hidden traits, prove an AI subject exists, replace external
containment with good character, or turn a private system constitution into an
AI-HPP conformance requirement.
