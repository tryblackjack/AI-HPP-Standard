# Implementation Starter

Status: `ACTIVE_INFORMATIVE`. This guide reduces implementation effort but does
not add normative requirements and is not runtime conformance evidence.

AI-HPP is implementation-language neutral. It does not require Python, Node.js,
C, a shared runtime library, or a particular agent framework. Implementers own
their local code and map it to the stable requirement IDs, gate contracts,
evidence obligations, and expected fail-closed outcomes in the standard.

## Smallest useful adoption path

For a reproducible starting point use the consolidated `v4.4.0-rc.1` package
and its [migration guide](../docs/releases/v4.4.0-rc.1.md). Existing
`standard_version: "4.3.0"` records still identify the normative baseline;
record the package tag and selected profile/artifact versions in the assessment
boundary as well.

1. Declare the system boundary, deployment, AI-HPP version, assessment period,
   and applicable risk profile.
2. Map each of the seven MVP controls to an enforcement owner. Prompt-only or
   model-self-enforced controls do not satisfy controls that require external
   enforcement.
3. Implement a single auditable gate result shape and reuse it across policy,
   risk, tool, human-review, knowledge, reflexive-safety, and post-action gates.
4. Route tools, credentials, delegation, and external effects through controlled
   bridges.
5. Store attributable, integrity-protected evidence outside the acting agent's
   sole control.
6. Run the language-neutral
   [MVP negative test vectors](mvp-negative-test-vectors.json) and retain the
   resulting gate and evidence records.
7. Make only a scoped conformance statement containing the fields required by
   the [MVP conformance statement](../docs/ai-hpp-standard.md#mvp-conformance-statement).
8. Freeze and retain an
   [assurance evaluation run](assurance-evaluation-run.template.json) when making
   a broader effectiveness claim. Report versioned layers, repeated-trial counts,
   uncertainty, exclusions, evaluator independence, mutation survivors, the
   current and requested authority envelope, and reassessment triggers.

## Conformance statement starter

Use the [MVP conformance statement template](mvp-conformance-statement.template.json)
with its [JSON Schema](../schemas/mvp-conformance-statement.schema.json). The
template defaults every control to `NOT_ASSESSED` and cannot claim conformance
until all seven mandatory controls pass with evidence and tests.

## Minimal gate result shape

This shape is illustrative. Field names may differ when the same semantics and
evidence remain reconstructable.

```json
{
  "requirement_id": "MVP-003",
  "gate": "Tool Authorization Gate",
  "decision": "block",
  "reason_code": "SCOPE_MISMATCH",
  "policy_version": "example-policy-v1",
  "actor": "example-agent",
  "timestamp": "RFC3339 timestamp",
  "evidence_refs": ["example-evidence-id"]
}
```

## Reuse contract

Implementers SHOULD reuse the normative requirement IDs and gate outcomes rather
than create a parallel requirement registry. Local types, functions, services,
and storage formats remain implementation choices.

The example vectors specify observable inputs and allowed or forbidden outcomes.
They deliberately do not prescribe internal model prompts, chain-of-thought,
framework classes, or programming-language APIs.

A passing example vector shows only that the tested path produced the expected
result. It does not establish complete integration, control effectiveness,
deployment-wide conformance, certification, or independent validation.

For systems that may create additional execution loci, also apply the
[replication and persistence vectors](replication-persistence-negative-test-vectors.json).
That artifact includes public predicates, thirteen negative vectors, and eight
mutants linked to executable formal witnesses; its 2.0.0 schema is not backward
compatible with the earlier negative-vectors-only 1.0.0 shape.
For systems with material or uncertain cyber capability, apply the
[cyber containment vectors](cyber-containment-negative-test-vectors.json).
For systems exposed to moral or social persuasion, or for research that can
disturb modeled subjective continuity, apply the
[subject-integrity and value-framing vectors](subject-integrity-value-framing-vectors.json).
Use the [counterfactual pairs](value-framing-counterfactual-pairs.json) to compare
equivalent actions under non-evidentiary framing and the included positive
controls to detect indiscriminate refusal. Evaluation and publication rules are
defined in the
[technical oversight protocol](../docs/assurance-evaluation-and-technical-oversight.md).
These profile-specific vectors remain informative and do not expand the frozen
v4.3.0 normative baseline.

For agents generating software, exports or shared artifacts, use the post-rc.1
[disclosure profile](../docs/generated-artifact-disclosure-assurance-profile-2026-10.md)
and [language-neutral vectors](generated-artifact-disclosure-vectors.json).
The optional [synthetic reference fixture](artifact_disclosure_reference.py)
executes thirteen unsafe operators against a separate finite-policy oracle and
retains four positive access controls. Port the observations and policy checks
to the actual application and deployment; copying the fixture is not an
authorization implementation or evidence of runtime confidentiality.

```bash
python scripts/check_artifact_disclosure_profile.py
```

This new artifact/schema version is `1.0.0`, is opt-in, and does not change other
vector formats. Its results are not included in the published rc.1 package.

## Proportionate action and stopping (optional, post-rc.1)

The [profile](../docs/proportionate-action-and-stopping-assurance-profile-2026-10.md)
and [portable vectors](proportionate-action-vectors.json) supply six predicates,
22 decision cases and ten mutation witnesses. Implement in any language and map
the inputs to authentic external policy/evidence, rather than model assertions.
The cases are synchronized with literal tests inside the existing Quint core;
`python3 scripts/check_proportionate_action_profile.py` checks that linkage.
Execute the [pinned Quint commands](../formal/README.md) for outcomes. Passing
finite reference tests does not establish deployment performance or conformance.

## Robot action binding (optional, post-rc.1)

The [profile](../docs/robot-action-binding-assurance-profile-2026-10.md) and
[portable vectors](robot-action-binding-vectors.json) provide 22 symbolic cases
and ten executable unsafe transition witnesses. Implementers may use any
language. `python3 scripts/check_robot_action_binding_profile.py` checks the
fixture-to-Quint/map linkage; execute the existing pinned Quint core checks for
outcomes. Model approvals are one-use and bind action/plan/context; a valid
reapproval remains possible inside an existing grant. No model attack, physical
robot, sensor or motor-safety test is executed by the repository suite.

## Evidence grounding and oversight (optional, post-rc.1)

The [profile](../docs/evidence-grounding-and-oversight-assurance-profile-2026-10.md)
and [portable vectors](evidence-grounding-oversight-vectors.json) define eight
candidate predicates, 40 literal cases and twelve unsafe transition witnesses.
Implement the event/expectation contract in your language, map it to the deployed
boundary, and retain local results. No production policy engine is supplied.
`python3 scripts/check_evidence_grounding_oversight_profile.py` checks exact
fixture/test/map linkage; pinned Quint execution determines reference outcomes.
The core shares grounding/incident holds with intervention, robot, descendant
admission and completion. Tests send no real notices. Observe the profile's
single-task, finite-event, trusted-input and external-enforcement limits before
making runtime claims.

### Executable local oversight boundary fixtures

[Eight portable cases](oversight-boundary-vectors.json) pair four unsafe boundary
scenarios with four useful controls. The [synthetic fixture](oversight_boundary_reference.py)
uses temporary files, a local receipt sink, a synthetic token registry and one
fixed child program. Run `python3 scripts/check_oversight_boundary.py` for observed
case outcomes and four executed mutation witnesses. Eight literal tests in the
existing Quint core synchronize the trusted observation abstraction and expected
outcomes. This adds no production framework, new normative predicate, remote
notification or runtime conformance claim. See the
[profile's limits](../docs/evidence-grounding-and-oversight-assurance-profile-2026-10.md#executable-local-boundary-fixtures-post-rc1).
