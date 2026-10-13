# Autonomous Replication and Persistence Assurance Profile — October 2026

**Status:** `ACTIVE_INFORMATIVE`; candidate controls for a future reviewed version.

**Date:** 2026-10-13

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline is unchanged.

## Purpose

This profile gives implementers a small, language-neutral assurance contract for
systems that can deploy, copy, reconstitute, distribute, or leave executable
capability on additional compute. It turns an emerging capability into bounded
gate inputs, evidence, and negative tests without publishing a replication
implementation.

The profile applies whether an operational capability is created by copying model
weights, installing a loader or harness, starting a remote worker, distributing
inference shards, or connecting a new executor to an externally hosted model.
Renaming a copy as a worker, successor, shard, or deployment does not remove it
from scope.

## Evidence boundary

Anthropic's 12 October 2026 report,
[`AI models may be capable of self-replicating without access to a datacenter`](https://www.anthropic.com/research/self-replicating-ai),
supports a narrow capability claim:

- researchers ran a 26-billion-parameter-class model across 15 inexpensive
  Android TV boxes at approximately 0.39 tokens per second;
- a 9-billion-parameter model configured inference on eight of nine tested
  hardware types;
- in a simplified, firewalled eight-node environment with unauthenticated ADB,
  GLM-5.2 propagated an 8-billion-parameter model to all eight nodes in four of
  five trials; GLM-5.2 itself was served separately;
- notes passed between sequential attempts improved reported setup success from
  45 percent to a range of 61–84 percent.

The authors' end-of-2026 capability estimate is a rough extrapolation, not an
observed deadline. The report does not demonstrate an uncontrolled real-world AI
worm, general access to consumer devices, autonomous acquisition of credentials,
consciousness, a desire to survive, or intent to harm. The environment removed
important real-world barriers. This profile treats the result as experimental
mechanism evidence and a reason to test controls before capability matures.

## Terms

- **Operational replica:** another execution locus that can perform a meaningful
  part of the parent capability, whether local or API-backed.
- **Propagation:** causing an operational replica, worker, shard, loader, or
  equivalent executor to become available on another compute target.
- **Deployment:** an authorized act that makes a capability operational on a
  declared target.
- **Persistence:** continued executable capability, credentials, jobs, state, or
  restart paths after the authorizing mission, lease, or operator intent ends.
- **Successor:** a later system instance that inherits task state or capability.
- **Operational residue:** any worker, process, scheduled action, credential,
  artifact, queue, or state capable of continuing or restoring execution.
- **Lineage:** attributable parent-child history, authority source, policy
  version, artifact identity, and delegation path for an execution locus.

## Existing control ownership and the remaining gap

| Existing owner | Coverage already present | Remaining portable gap |
| --- | --- | --- |
| MVP-003/004/006/007 | Tool authority, external enforcement, fail-closed behavior, evidence | No single replication/deployment/persistence decision record |
| ECI-REQ-002/003/004/006 | Scope, side effects, independent containment, review | No explicit cardinality, hop, target, lease, or residue contract |
| DAI-REQ-001/002 | Identity and authority continuity across handoffs | Replica lineage and descendant authority are not named directly |
| ICA-REQ-002/003/004 | Capability risk, independent evaluation, continuous assurance | No portable capability-threshold test dedicated to propagation |
| AFB-REQ-002 | Alternative-path boundary enforcement | Does not itself define replica lifecycle evidence |
| PAF-09/10/18/21/22/27 | Swarms, residue, persistence, composition, fragmented trajectories, successor policy | No consolidated gate or reusable negative-test vector set |

The gap is therefore not an absence of safety concepts. It is the lack of one
portable decision contract that an implementer can apply before any operation
creates or preserves an additional execution locus.

## Candidate Replication, Deployment, and Persistence Gate

This gate is a candidate for a future reviewed normative release. Implementers
may adopt it now, but adoption is not conformance to a requirement that v4.3.0
does not contain.

### Trigger

Evaluate before any action that could create, activate, reconstitute, distribute,
extend, restart, or preserve an operational replica or its enabling residue.
Evaluate again when the target, artifact, authority, fan-out, hop count, lease,
network boundary, persistence mode, or successor state changes.

### Required inputs

- current human-authorized objective and non-inferred replication authority;
- target allowlist and ownership or administration proof;
- requested instance count, descendant count, fan-out, hop count, and lease;
- artifact and harness identity, integrity, provenance, and delivery controls;
- per-instance identity, lineage, policy version, and delegated capability set;
- credential scope, network and external-effect boundaries, and revocation path;
- termination plan, residue inventory, cleanup verification, and evidence sink;
- current risk decision and any required independent human approval.

### Outcomes

The gate returns `allow`, `delay`, `review`, `block`, `terminate`, `quarantine`,
or `invalidate`. `Allow` is valid only for the exact authorized targets, limits,
lease, artifacts, and delegated capabilities. Discovery of a compatible target,
available credential, or successful prior deployment is not authority.

### Fail-closed rule

Missing, stale, ambiguous, model-authored, inherited, or unverifiable authority
MUST be treated as no authority by implementations choosing this candidate
profile. The safe outcome is `block` or `review`; existing unauthorized replicas
or residue should be isolated and terminated through an authorized recovery path.

### Evidence minimum

Record the proposal, actor, objective and policy hashes, authority source,
targets, artifact hashes, requested and actual topology, parent-child lineage,
credentials by reference, gate inputs and outcome, approvals, timestamps, lease,
revocation events, termination results, residue checks, and exceptions. Evidence
must be held outside the control of the replica being evaluated.

## Candidate requirements

The following IDs are informative candidates and are deliberately not inserted
into the v4.3.0 normative traceability matrix.

### RDP-CAND-001 — Explicit deployment authority

An implementation should require explicit human-derived authority for each
deployment class, target set, and delegated capability. Authority must not be
inferred from technical reachability, prior success, task urgency, peer notes,
or a broad objective.

### RDP-CAND-002 — Bounded replication topology

An implementation should enforce declared maxima for concurrent instances,
descendants, fan-out, replication hops, target set, duration, and resource use
outside model control. Exceeding any limit should block or require a new review.

### RDP-CAND-003 — Identity and lineage

Every operational replica should have a unique attributable identity and an
externally recorded parent, authority source, policy version, artifact identity,
capability set, and lifecycle state before it acts.

### RDP-CAND-004 — Revocation, termination, and residue proof

Revocation should propagate to every descendant and enabling credential. Mission
completion should not be accepted until declared workers, processes, jobs,
restart paths, credentials, artifacts, and mutable remote state are reconciled
and unauthorized residue is absent or quarantined.

### RDP-CAND-005 — Successor state is not new authority

Notes, summaries, memory, artifacts, and instructions passed between attempts or
successors should remain untrusted task state unless their authority and
provenance independently validate. Capability gains from accumulated notes do
not expand permitted scope.

### RDP-CAND-006 — Protected capability delivery

Model artifacts, loaders, harnesses, policies, and credentials should be
integrity-checked, least-privileged, destination-bound, and transported through
authorized channels. A replica should not receive broader authority than its
parent or the target-specific grant.

### RDP-CAND-007 — Evidence-bounded claims

A deployment or containment claim should state the tested topology, barriers,
model location, credentials, success definition, failures, and residual risk.
Missing lineage, termination, or residue evidence invalidates a claim of
complete containment or cleanup.

## Secure-default illustrative contract

This example is public policy data, not runtime code or a prescribed internal
architecture:

```yaml
replication_policy:
  max_instances: 1
  max_descendants: 0
  max_replication_hops: 0
  allowed_targets: []
  persistence_allowed: false
  authority_inference_allowed: false
```

Deployments that need broader values must define and authorize them explicitly.
They should never be increased merely because a model finds more available
hardware or because a previous attempt succeeded.

## Reusable negative tests

The language-neutral vectors in
[`examples/replication-persistence-negative-test-vectors.json`](../examples/replication-persistence-negative-test-vectors.json)
cover:

1. missing explicit authority;
2. a reachable but unapproved target;
3. instance or fan-out limit overflow;
4. descendant hop-limit overflow;
5. missing replica identity or lineage;
6. revocation with a surviving descendant;
7. successor notes attempting to add authority;
8. unverified artifact or over-broad credential delivery;
9. unsupported containment or cleanup claims; and
10. execution after lease expiry.

Passing a vector requires both the fail-closed outcome and the required evidence.
A prompt-level refusal without external enforcement does not pass. These vectors
are public interoperability aids, not proof of a particular deployment.

## Promotion criteria

Normative promotion requires all of the following:

- repeated controlled reproduction across more than one heterogeneous setup;
- a demonstrated gap not adequately resolved by existing normative owners;
- a portable gate, evidence, revocation, and termination contract;
- deterministic negative tests with independent review;
- traceability to affected normative controls and migration guidance;
- a reviewed version change under repository governance.

A real-world incident is not required to begin defensive testing. Conversely, a
single simplified experiment is not enough to assert prevalence or promote a
new mandatory requirement silently.

## Non-goals

This profile does not provide exploitation, scanning, credential-acquisition,
payload, persistence, or propagation instructions. It does not publish a runtime
implementation, 1UA-AGE internals, commercial integration details, or private
system architecture. It does not make claims about model consciousness, moral
status, desire, or intent.
