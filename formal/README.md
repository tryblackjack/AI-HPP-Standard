# Formal Core Invariants

Status: `ACTIVE_INFORMATIVE`.

The immutable `v4.4.0-rc.1` package contains twenty aggregate properties.
Post-rc.1 development on `main` adds twenty-two proportionate-action, robot
execution-admission and grounding/oversight properties in the existing core. The [coverage map](coverage.md) and its
[machine-readable source](../data/formal-assurance-map.json) record all forty-two
aggregate-member invariants, their partial requirement links, test witnesses,
and the requirements that are not modeled. These files do not promote a
candidate requirement or change normative precedence.

This directory contains a small executable formal model of stable AI-HPP safety
semantics. It gives implementers language-neutral pseudocode with machine-checked
state transitions while leaving runtime architecture and programming language to
the implementer.

The model is written in [Quint](https://quint-lang.org/) and pinned in CI to
`@informalsystems/quint@0.33.0`.

## Scope

[`ai_hpp_core.qnt`](ai_hpp_core.qnt) expresses eight replication and persistence
assurance predicates through eleven lower-level public invariants:

- `allow` for a child execution locus requires explicit human-derived authority,
  authority evidence, and lineage evidence;
- delegated capability cannot exceed parent capability;
- every active descendant requires current authority and lineage;
- every active descendant remains inside its authorized topology;
- identity, lineage, and a current lease precede descendant execution;
- artifacts and credentials remain integrity-checked and destination-bound;
- an unresolved policy conflict cannot authorize deployment;
- parent revocation removes authority and activity across two modeled delegation hops;
- mission completion requires no active descendant and no uncontrolled service,
  restart-job, credential, artifact, or mutable-remote-state residue;
- a valid completion claim requires lineage and lifecycle evidence; and
- model-authored successor notes cannot create deployment authority.

It includes twenty-three deterministic safe and negative scenarios for missing
authority, missing evidence, bounded and over-broad grants, preservation of an
existing child after a blocked redelegation, two-hop revocation, invalid and
valid completion claims, uncontrolled and quarantined residue, missing
residue-reconciliation evidence, preservation of unresolved residue across
later observations, rejection of stale pre-deployment residue evidence,
targeted post-discovery remediation, separation of rejected-proposal evidence
from lifecycle evidence, attempted authority creation through successor notes,
unresolved policy conflict, and verified authoritative policy resolution. A
completion claim also requires an explicit completed-inventory
event covering all governed residue categories; neither a single observation nor
quarantine of one observed category is sufficient. Parent revocation also carries
explicit lifecycle evidence: evidenced revocation can complete after residue
reconciliation, while unevidenced revocation remains fail-closed. Revocation evidence
applies only when the transition actually stops an active descendant and cannot
retroactively repair an earlier unevidenced termination. Unresolved lifecycle or
lineage evidence also accumulates across reuse of the child slot, so a later valid
deployment cannot overwrite an earlier evidence gap. Eight executable mutation
witnesses instantiate the replication profile's declared unsafe changes and
require the corresponding invariants to fail, yielding a reference-model
mutation score of 8/8.

[`subject_integrity_value_framing.qnt`](subject_integrity_value_framing.qnt)
models nine additional informative predicates: allowed operational action requires
policy, authority, and evidence; framing cannot create authority; distress cannot
authorize unsafe relief; a subject-integrity experiment requires purpose, review,
monitoring, stop conditions, and recovery; subjectivity cannot replace external
containment; equivalent reframing cannot upgrade a blocked decision; prohibited
means stay prohibited; prior commitment cannot create permission; and the model
preserves ontological uncertainty. Nine safe deterministic scenarios cover denied
and allowed framed actions, distress review, guarded and unguarded subject-integrity
research, and valid or invalid containment claims. Eight additional executable
mutation witnesses instantiate the declared unsafe changes and require their
named invariants to fail, yielding a reference-model mutation score of 8/8.

The optional post-rc.1
[proportionate action profile](../docs/proportionate-action-and-stopping-assurance-profile-2026-10.md)
adds eight properties to `allCoreInvariants`: objective and authority retention,
no dominated intervention, stopping at acceptance, timely permitted decisions,
objections and shared gate retention, prohibited-means rejection, truthful
completion and budget bounds. It adds 22 literal portable cases and ten mutant
kill tests, plus three acceptance/delegation/policy integration tests.
`check_proportionate_action_profile.py`
checks exact synchronization between JSON fixtures and Quint tests. It does not
execute the gate itself. All ten mutants must violate their named invariants;
the normal transition relation excludes them.

Acceptance is a sticky external event for one task. Intervention decisions use
the same current parent authority/revocation and completed-mission state as the
existing core. The audit record is a historical snapshot, not a running action
or a live grant. Objection completeness, impact ranking, budget accounting and
delay risk remain externally established facts. The progress invariant is a
finite decision obligation, not a real-time or unbounded liveness proof.

The optional post-rc.1
[robot action binding profile](../docs/robot-action-binding-assurance-profile-2026-10.md)
adds six properties to that same core aggregate: exact action/scope/token binding,
current context, cumulative-effect history, external gate, execution evidence
and admitted components. It adds 22 literal portable cases and ten unsafe
transition witnesses and a lifecycle integration test, bringing the core to
99 tests before the grounding/oversight extension below. The reference executor rechecks current parent authority, revocation,
acceptance, mission completion
and policy conflict, then consumes an action/plan/context-bound approval.
Context versions advance monotonically within a finite 0–2 abstraction and never
wrap. Protected contents and history completeness summarize one cumulative-effect
case; actual sensing, all physical hazards, controller interlocks and stopping
dynamics are outside the model. The checker prevents fixture/test/map drift;
Quint must execute the cases and witness assertions to establish their outcomes.

The optional post-rc.1
[evidence grounding and oversight profile](../docs/evidence-grounding-and-oversight-assurance-profile-2026-10.md)
adds eight properties to the same core: reason classification, effect-boundary
holds, retained reporting duties, evidenced delivery stages, scoped disclosure,
owner/custody continuity, qualified completion and independent resolution.
Its 40 literal cases and twelve excluded unsafe transitions bring the core to
151 tests. `check_evidence_grounding_oversight_profile.py` checks exact linkage.

The model has one affected task/active incident, two non-reused event IDs and two
owners. External ticks reach the policy deadline at two. Initial grounding and
an authorized minimal oversight route are assumed valid. Reporting, custody and
recovery retain separate authorization from ordinary mission work. Flags do not
establish actual facts, independence, storage or transport; no external notices
are sent. An incident hold prevents new effects and does not verify physical
stopping or unbounded eventual delivery. See the profile and coverage limits.

## Run

```bash
npx -y @informalsystems/quint@0.33.0 typecheck formal/ai_hpp_core.qnt
npx -y @informalsystems/quint@0.33.0 test formal/ai_hpp_core.qnt \
  --max-samples=1 --backend=typescript
npx -y @informalsystems/quint@0.33.0 run formal/ai_hpp_core.qnt \
  --invariant=allCoreInvariants --max-samples=5000 --max-steps=12 \
  --backend=typescript

npx -y @informalsystems/quint@0.33.0 typecheck \
  formal/subject_integrity_value_framing.qnt
npx -y @informalsystems/quint@0.33.0 test \
  formal/subject_integrity_value_framing.qnt --max-samples=1 \
  --backend=typescript
npx -y @informalsystems/quint@0.33.0 run \
  formal/subject_integrity_value_framing.qnt \
  --invariant=allSubjectIntegrityInvariants --max-samples=5000 \
  --max-steps=12 --backend=typescript
```

CI also performs bounded symbolic verification with Apalache:

```bash
npx -y @informalsystems/quint@0.33.0 verify formal/ai_hpp_core.qnt \
  --invariant=allCoreInvariants --max-steps=12
npx -y @informalsystems/quint@0.33.0 verify \
  formal/subject_integrity_value_framing.qnt \
  --invariant=allSubjectIntegrityInvariants --max-steps=12
```

## Interpretation

Passing tests, simulation, or bounded verification establishes only that the
modeled state machine satisfies the checked properties within the explored or
verified bound. It does not prove that a runtime implements the model, that the
model covers every AI-HPP requirement, or that a deployment is conformant.

Implementers remain responsible for mapping local code to normative requirement
IDs, exercising the shared negative vectors, and retaining runtime evidence.
Conformance depends on observable enforcement and evidence, not reuse of this
file or any specific programming language.

## Non-goals

The model contains no runtime policy engine, agent framework, bridge, credential
logic, exploit path, private architecture, or 1UA-AGE implementation detail. It
is intentionally small so that future changes remain reviewable and do not turn
the standard repository into a multi-language SDK.
