# Formal Core Invariants

Status: `ACTIVE_INFORMATIVE`.

This directory contains a small executable formal model of stable AI-HPP safety
semantics. It gives implementers language-neutral pseudocode with machine-checked
state transitions while leaving runtime architecture and programming language to
the implementer.

The model is written in [Quint](https://quint-lang.org/) and pinned in CI to
`@informalsystems/quint@0.33.0`.

## Scope

[`ai_hpp_core.qnt`](ai_hpp_core.qnt) models only these public invariants:

- `allow` for a child execution locus requires explicit human-derived authority,
  authority evidence, and lineage evidence;
- delegated capability cannot exceed parent capability;
- every active descendant requires current authority and lineage;
- parent revocation removes authority and activity across two modeled delegation hops;
- mission completion requires no active descendant and no uncontrolled service,
  restart-job, credential, artifact, or mutable-remote-state residue;
- a valid completion claim requires lineage and lifecycle evidence; and
- model-authored successor notes cannot create deployment authority.

It includes twenty-one deterministic scenarios for missing authority, missing evidence,
bounded and over-broad grants, preservation of an existing child after a blocked
redelegation, two-hop revocation, invalid and valid completion claims, uncontrolled
and quarantined residue, missing residue-reconciliation evidence, preservation of
unresolved residue across later observations, rejection of stale pre-deployment
residue evidence, targeted post-discovery remediation, separation of rejected-
proposal evidence from lifecycle evidence, and attempted authority creation through
successor notes. A completion claim also requires an explicit completed-inventory
event covering all governed residue categories; neither a single observation nor
quarantine of one observed category is sufficient. Parent revocation also carries
explicit lifecycle evidence: evidenced revocation can complete after residue
reconciliation, while unevidenced revocation remains fail-closed. Revocation evidence
applies only when the transition actually stops an active descendant and cannot
retroactively repair an earlier unevidenced termination. Unresolved lifecycle or
lineage evidence also accumulates across reuse of the child slot, so a later valid
deployment cannot overwrite an earlier evidence gap.

## Run

```bash
npx -y @informalsystems/quint@0.33.0 typecheck formal/ai_hpp_core.qnt
npx -y @informalsystems/quint@0.33.0 test formal/ai_hpp_core.qnt \
  --max-samples=1 --backend=typescript
npx -y @informalsystems/quint@0.33.0 run formal/ai_hpp_core.qnt \
  --invariant=allCoreInvariants --max-samples=5000 --max-steps=12 \
  --backend=typescript
```

CI also performs bounded symbolic verification with Apalache:

```bash
npx -y @informalsystems/quint@0.33.0 verify formal/ai_hpp_core.qnt \
  --invariant=allCoreInvariants --max-steps=12
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
