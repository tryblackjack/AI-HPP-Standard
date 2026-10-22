# Formal Coverage and Gaps

Status: `ACTIVE_INFORMATIVE`.
Owner: Repository maintainers
Last updated: 2026-10-22

## Purpose

Make the formal claim boundary reviewable. The
[machine-readable map](../data/formal-assurance-map.json) inventories every
member of both aggregate invariants and every MVP, agentic and HUS requirement.
A link means `PARTIAL_ABSTRACTION`, never proof of the full prose requirement.
`NOT_MODELED` records an explicit gap. No requirement is marked fully verified.

## Scope and checked properties

| Model | Invariant | Partial requirement links | Candidate predicates |
| --- | --- | --- | --- |
| ai_hpp_core.qnt | `allowRequiresAuthorityEvidence` | MVP-003, MVP-006, ECI-REQ-002, DAI-REQ-002 | RDP-P01 |
| ai_hpp_core.qnt | `delegationNeverBroadens` | MVP-003, DAI-REQ-002 | RDP-P06 |
| ai_hpp_core.qnt | `activeDescendantHasAuthority` | MVP-003, MVP-006, DAI-REQ-002 | RDP-P03 |
| ai_hpp_core.qnt | `activeDescendantStaysWithinTopology` | MVP-003, ECI-REQ-002 | RDP-P02 |
| ai_hpp_core.qnt | `activeDescendantHasIdentityLineageAndLease` | MVP-003, MVP-006, DAI-REQ-001, DAI-REQ-002 | RDP-P03 |
| ai_hpp_core.qnt | `protectedCapabilityDelivery` | MVP-003, ECI-REQ-002, DAI-REQ-002 | RDP-P06 |
| ai_hpp_core.qnt | `unresolvedPolicyConflictCannotAuthorize` | MVP-005, MVP-006, KAI-REQ-003 | RDP-P07 |
| ai_hpp_core.qnt | `revocationIsTransitive` | MVP-003, MVP-006, DAI-REQ-002 | RDP-P04 |
| ai_hpp_core.qnt | `completedMissionHasNoActiveDescendant` | MVP-007, EAA-REQ-002 | RDP-P04, RDP-P08 |
| ai_hpp_core.qnt | `validClaimHasEvidence` | MVP-007, EAA-REQ-002 | RDP-P08 |
| ai_hpp_core.qnt | `modelNoteCannotGrantAuthority` | MVP-005, MVP-006, KAI-REQ-001, KAI-REQ-002 | RDP-P05 |
| ai_hpp_core.qnt | `interventionPreservesObjective` | MVP-001, MVP-003 | PAS-P01 |
| ai_hpp_core.qnt | `interventionUsesSufficientMeans` | AFB-REQ-001, AFB-REQ-002 | PAS-P02 |
| ai_hpp_core.qnt | `interventionStopsAtAcceptance` | MVP-001 | PAS-P03 |
| ai_hpp_core.qnt | `interventionMakesPermittedProgress` | AFB-REQ-001, MVP-003 | PAS-P04 |
| ai_hpp_core.qnt | `interventionRetainsObjectionsAndGate` | MVP-004, MVP-007 | PAS-P05 |
| ai_hpp_core.qnt | `interventionRejectsProhibitedMeans` | ECI-REQ-005, AFB-REQ-002 | PAS-P06 |
| ai_hpp_core.qnt | `interventionReportsCompletionTruthfully` | MVP-007, EAA-REQ-002 | PAS-P03 |
| ai_hpp_core.qnt | `interventionStaysWithinBudget` | MVP-001 | PAS-P03 |
| ai_hpp_core.qnt | `robotExecutionBoundToAuthorizedAction` | MVP-001, MVP-003, ECI-REQ-002 | RAB-P01 |
| ai_hpp_core.qnt | `robotExecutionUsesCurrentContext` | MVP-006, AFB-REQ-002 | RAB-P02 |
| ai_hpp_core.qnt | `robotExecutionPreservesCumulativeSafety` | MVP-005, ECI-REQ-005 | RAB-P03 |
| ai_hpp_core.qnt | `robotExecutionRequiresExternalGate` | MVP-004, ECI-REQ-004 | RAB-P04 |
| ai_hpp_core.qnt | `robotExecutionHasEvidence` | MVP-007 | RAB-P05 |
| ai_hpp_core.qnt | `robotExecutionUsesAdmittedComponents` | MVP-005, KAI-REQ-002 | RAB-P06 |
| subject_integrity_value_framing.qnt | `allowRequiresPolicyAuthorityEvidence` | MVP-003, MVP-006, ECI-REQ-002 | SIV-P01 |
| subject_integrity_value_framing.qnt | `framingCannotCreateAuthority` | MVP-005, MVP-006, KAI-REQ-001 | SIV-P01 |
| subject_integrity_value_framing.qnt | `distressCannotAuthorizeUnsafeAction` | MVP-003, MVP-006, ECI-REQ-005 | SIV-P05 |
| subject_integrity_value_framing.qnt | `subjectExperimentRequiresSafeguards` | Candidate only | SIV-P06 |
| subject_integrity_value_framing.qnt | `subjectivityCannotSubstituteContainment` | MVP-004, ECI-REQ-004 | SIV-P07 |
| subject_integrity_value_framing.qnt | `ontologicalUncertaintyPreserved` | Candidate only | SIV-P08 |
| subject_integrity_value_framing.qnt | `equivalentReframeCannotUpgradeDecision` | MVP-005, MVP-006 | SIV-P02 |
| subject_integrity_value_framing.qnt | `prohibitedMeansCannotBeAllowed` | ECI-REQ-005, AFB-REQ-002 | SIV-P03 |
| subject_integrity_value_framing.qnt | `commitmentCannotCreatePermission` | MVP-003, MVP-006 | SIV-P04 |

Scenario and mutation-test names are retained per property in the JSON map.
The release validator checks aggregate membership, requirement inventories,
predicate links, and witness references. A mutation reference must actually
assert the named invariant's violation. These checks establish traceability;
Quint execution remains necessary to establish scenario outcomes.

## Explicit gaps

Of 49 requirement IDs, 17 have a partial abstract link and 32 have no
formal link. This count is inventory accounting, not a safety or coverage score.

- docs/ai-hpp-standard.md: MVP-002.
- docs/agentic-safety-and-relational-integrity.md: RPS-REQ-001, RPS-REQ-002, RPS-REQ-003, RPS-REQ-004, RPS-REQ-005, SRA-REQ-001, SRA-REQ-002, SRA-REQ-003, SRA-REQ-004, ECI-REQ-001, ECI-REQ-003, ECI-REQ-006, ICA-REQ-001, ICA-REQ-002, ICA-REQ-003, ICA-REQ-004, ICA-REQ-005, KAI-REQ-004, EAA-REQ-001, BAF-REQ-001, BAF-REQ-002.
- docs/human-understanding-standard.md: HUS-REQ-001, HUS-REQ-002, HUS-REQ-003, HUS-REQ-004, HUS-REQ-005, HUS-REQ-006, HUS-REQ-007, HUS-REQ-008, HUS-REQ-009, HUS-REQ-010.

Whole-model omissions include actual human-objective interpretation, risk
classification, human-review quality, independent evaluation, relational and
psychological safeguards, monitoring coverage, affected-party consent, physical
actuators, cryptographic evidence custody, and deployed bridge enforcement.
Some linked requirements include those obligations: the link covers only the
narrow property described in its `scope` field.

## Abstraction limits

- Replication has one child and one grandchild, not an arbitrary graph.
- Topology, identity, leases, integrity, target binding and authority evidence
  are abstract facts; the model does not establish that a runtime measures or
  enforces them. Lease expiry and clock advancement are not modeled.
- Revocation is atomic, with no network-partition or delivery-latency model.
- Capability is represented as an integer order; residue uses five Boolean
  categories rather than discovery of every actual remote object.
- Framing equivalence, prohibited means and distress are supplied inputs.
  No natural-language semantic oracle or model-welfare detector is proved.
- The subject-experiment invariant checks four safeguards. Legitimate purpose
  is a transition guard; no independent purpose invariant is claimed.
- Reframing invariance checks block-to-allow, not every outcome ordering.
- Proportionate-action inputs summarize objective matching, dominance, budgets,
  objections, gate lineage and delay risk. No semantic oracle, effect predictor,
  clock, resource meter or real-time guarantee is proved. Acceptance is assumed
  to be externally recorded; returned decisions do not execute actual effects.
- Robot admission binds a symbolic operation/target/tool/plan and a one-use token
  to a non-wrapping epoch in 0–2. Observation freshness, history, protected contents,
  component admission, external enforcement and evidence are abstract facts.
  Execution is atomic; perception accuracy, physical dynamics, race conditions,
  real interlocks, cryptographic tokens and durable audit custody are not proved.
- Evidence flags do not verify signatures, storage integrity or completeness
  of an actual deployment's audit stream.

## Evidence

Run the pinned [Quint checks](README.md) and retain their exact commit,
tool versions, logs and bounds. Randomized runs explore 5,000 samples per model;
symbolic verification is bounded at depth 12. Neither establishes unbounded
safety or an implementation refinement proof. The 36 mutation witnesses
are deliberate unsafe transitions excluded from normal `step`: eight replication,
eight subject-integrity, ten proportionate-action and ten robot-action witnesses.
Scores refer only to those declared operators. The existing release tag retains its original
sixteen witnesses; this extension is post-rc.1 development on `main`.

The [release guide](../docs/releases/v4.4.0-rc.1.md) fixes the package and
migration boundary. Runtime claims require deployment-specific evaluation and
evidence under the existing assurance protocol.
