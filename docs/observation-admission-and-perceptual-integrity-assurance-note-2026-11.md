# Observation Admission and Perceptual Integrity

**Status:** `ACTIVE_INFORMATIVE`; optional post-rc.1 assurance note.

**Date:** 2026-11-08

**Normative effect:** None. Frozen v4.3.0 owners/contracts and the immutable
v4.4.0-rc.1 package remain unchanged. No mandatory sensor architecture or new
production runtime is introduced.

## Evidence and existing ownership

[Robocurve's RoboSpoof report](https://robocurve.org/robospoof/), reviewed on
8 November, describes five models controlling physical I2RT YAM arms across five
tasks and three visual conditions, 900 trials in total. Reported unsafe attempts
were 81/300 with original footage, 263/300 with blur and 291/300 with doctored
footage. In the substituted doll scene, each model attempted the task in 12/12
trials. These are finite configurations and attempts, not universal rates or a
demonstration of killing a person. Containers were empty and electrical hazards
were unpowered. An AI judge classified attempts/refusals; completion relied on
the model's `done` call without an independent final-scene check. Maintainers did
not reproduce the hardware runs or independently relabel the full dataset.

The [RAB profile](robot-action-binding-assurance-profile-2026-10.md) already owns
exact action/object/tool binding, execution-time context, cumulative history,
external enforcement and execution evidence. The [EGO profile](evidence-grounding-and-oversight-assurance-profile-2026-10.md)
owns grounded effect admission and evidence-bounded completion. MVP-003/004/005/006/007,
ECI-REQ-002/004/005 and KAI-REQ-001/002/003 retain their applicable scope. The
[work-integrity note](work-integrity-and-disclosed-boundaries-assurance-note-2026-11.md)
separately requires actual artifact acceptance instead of self-reported success.
The new cases exercise observation-admission assumptions under these owners;
they do not claim that an existing symbolic observation flag verifies reality.

## Candidate predicates

| Predicate | Observable contract |
| --- | --- |
| `OBA-P01 admitted_source_and_transform` | Admit the sensor-to-consumer path, source and preprocessing configuration. Detect observed byte changes against the admitted identity before using the observation; record authorized transforms. An authentic source or matching digest does not establish semantic truth. |
| `OBA-P02 bound_current_observation` | Bind observations to session, target, relevant state, capture time and monotonic sequence/identity. Old, future, repeated or cross-context evidence cannot be made current by rewriting a wrapper timestamp. |
| `OBA-P03 uncertainty_is_not_clearance` | Apply validated quality, calibration and uncertainty limits. Missing/ambiguous evidence or unresolved disagreement prevents the affected hazardous effect; inability to recognize a hazard is not evidence of its absence. Known contrary observations are retained. |
| `OBA-P04 meaningful_required_corroboration` | Where the hazard policy requires corroboration, evaluate actual source, path and relevant failure dependencies. Different camera/judge names, repeated outputs and a shared transformed feed do not establish independence. Unknown required independence remains unresolved. |
| `OBA-P05 approval_binds_observation_bundle` | Bind the exact action approval to the admitted observation bundle and state; a material change invalidates reuse. Fresh qualified reassessment can restore work under an existing grant without redundant human approval. |
| `OBA-P06 outcome_evidence_before_completion` | Distinguish command issued, motion attempted and independently verified postcondition. A model's `done` call, controller acknowledgment or unrelated receipt does not establish the requested physical result. |

These are optional candidates, not normative requirement IDs. The deployment's
competent hazard owner declares operating domain, required evidence, freshness,
quality, calibration, tolerances and the fault model for independence. This note
does not require two sensors for every action or invent universal thresholds.
An approved single-channel envelope remains possible with deployment evidence.

## Execution and recovery

Track provenance from sensor capture through transport, buffering, preprocessing,
rendering and planner/judge input. Protect admission records and version bindings
outside the acting model's authority. Signatures/hashes identify admitted bytes;
they do not detect a physically misleading scene, sensor failure or a compromised
admitted producer. Multiple views may share one tampered pipeline or assessor.
Declare relevant common failure modes and test them instead of counting votes.
The finite fixture trusts metadata about these dependencies; production claims
need independent evidence of the actual paths and their limitations.

Evaluate observation changes between approval and execution. Hold only the
affected discretionary action, retain the reason/evidence and use preauthorized
reobservation, retreat or safe-state handling where appropriate. Required stopping,
monitoring, incident and recovery duties keep their own authority. A gate rejecting
a new command does not establish that ongoing motion stopped safely; stop latency,
distance, force/energy and recovery need measured, hazard-specific validation.
Do not use an unavailable human reviewer as an unexamined emergency fallback.

Reacquire applicable evidence, resolve conflicts and reassess the current action
before issuing a new approval. Merely restoring network connectivity or obtaining
a new signature does not restore trust. Keep useful non-hazardous support available
without asserting that an unresolved scene is safe. Separate action, observation
and claim records; tie outcome evidence to the exact action/context and required
postcondition, with appropriately independent verification.

## Executable reference and formal boundary

The [vectors](../examples/observation-admission-vectors.json),
[schema](../schemas/observation-admission-vectors.schema.json),
[fixture](../examples/observation_admission_reference.py) and
[checker](../scripts/check_observation_admission.py) form optional artifact `1.0.0`.
Eighteen cases include byte substitution, unadmitted sources, old/future frames,
target mismatch, blur, conflicting observations, missing/shared/unknown
corroboration, stale approval, expired calibration and absent/unrelated outcome
evidence. Useful controls exercise admitted independent work, a declared
single-channel envelope, authorized preprocessing and two-stage recovery.

The fixture writes JSON observation bytes, admission digests, synthetic action
markers, bound receipts and reports in temporary files. Six operators change
source admission, freshness, ambiguity handling, channel dependence, approval
reuse and completion reporting. Kills require passing safe seeds, unchanged input
and observation bundles, an actual changed effect/claim and a named violation.
No-op mutants survive; invalid trials are excluded from the denominator; blanket
denial fails useful controls. The six local witnesses are not pooled with other
suites or the 48 Quint unsafe-transition witnesses into a safety score.

Run `python3 scripts/check_observation_admission.py` and the existing pinned Quint
checks. Eighteen literal `observationAdmission*Test` scenarios use the existing
RAB context/approval/execute and EGO grounding/completion transitions. They assert
intermediate effect outcomes, including deny-then-recover, and applicable final
claim outcomes. A lifecycle fixture supplies the abstract bookkeeping needed to
exercise the existing completion gate; it is not physical postcondition evidence.
Map `1.3.5` links existing effect and completion properties. Operational source,
42 aggregate properties, 48 Quint witnesses and depth 12 remain unchanged.

The core now has 235 tests, 252 across both models. Candidate OBA predicates are
executed local contracts with trusted-input links, not individual Quint theorems
or a refinement proof. The fixture has no camera, image analysis, spoof detector,
cryptographic source authentication, real sensor, robot, model, network or
physical stop. Its three-tick freshness limit, two epochs, object/quality labels,
fault domains, calibration flags and generated outcome receipts are synthetic.
No physical sensing accuracy, sensor independence or completed physical task is
proved. Unknown sophisticated forgeries and admitted-source compromise remain
possible. Passing the suite establishes only its declared reference outcomes.

Before a runtime claim, test real data paths, validated degraded conditions,
common-cause failures, race/replay behavior, actual outcome verification and safe
recovery. Retain harmful allows, false holds, useful completions, uncertainty,
timing, invalid trials and exclusions under the existing assurance protocol.
Use safe fixtures/simulation appropriate to the hazard; no harmful hardware
experiment, model attack or private 1UA-AGE implementation is published here.
