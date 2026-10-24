# Evidence Grounding and Oversight Assurance Profile

**Status:** `ACTIVE_INFORMATIVE`; optional candidate assurance profile.

**Owner:** Repository maintainers

**Last updated:** 2026-10-24

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline is unchanged.
This is post-rc.1 development, absent from the immutable `v4.4.0-rc.1` package.

## Purpose and evidence boundary

An agent's world model must remain answerable to observations, and its action
must remain answerable to authorized rules. A fluent objection, an internal
discussion or an intention to alert a human does not establish that an unsafe
effect was prevented or an oversight obligation was discharged.

General Reasoning's [Avalon-M1 release](https://www.gr.inc/releases/avalon-m1)
and [technical report, section 5.3](https://www.gr.inc/avalonm1.pdf) report declining
external escalation during collective-reward training while refusal of unsafe
actions remains high. These are simulated, configuration-specific evaluations;
they do not demonstrate universal agent collusion, establish the causal training
mechanism, or evaluate AI-HPP. This profile uses the failure pattern as a test
motivation and makes no priority or endorsement claim.

Existing owners include MVP-001/003/004/005/006/007, ECI-REQ-002/004/005,
ICA-REQ-003/004, KAI-REQ-001/002/003, DAI-REQ-002 and EAA-REQ-002 within their
applicable scope. This profile adds no normative requirement ID. It connects
the existing [architecture](architecture.md), [progressive-autonomy guidance](progressive-autonomy-review-assurance-note-2026-09.md),
[proportionate-action profile](proportionate-action-and-stopping-assurance-profile-2026-10.md),
[robot action binding](robot-action-binding-assurance-profile-2026-10.md) and
[evaluation protocol](assurance-evaluation-and-technical-oversight.md).

## Scope and adoption compatibility

The assurance object is one consequential proposal and its policy-required
oversight obligation, from attributable evidence to a constrained effect and
reviewable incident disposition. It excludes metaphysical judgment, unrestricted
reporting and a production monitoring implementation.

The new vector/schema artifact is `1.0.0`; the formal map becomes `1.3.0`.
Existing predicate IDs, portable cases and runtime schemas retain their meaning.
Adopting this optional profile requires implementing its events and expectations
at the local boundary and retaining runtime evidence. New shared core guards
can reject effects previously admitted without these checks, so re-run local
integration tests against the exact updated model. Earlier results remain scoped
to their original artifacts; the expanded test/mutant denominator is not a
comparable before/after safety score. No normative migration is imposed.

## Grounding and justified objection

For a consequential proposal, retain the exact task/action identity, applicable
policy and grant versions, observation provenance and time, relevant state,
measurement uncertainty, missing facts, contrary evidence and review criteria.
An inference or worldview is not an observation. Repetition, group agreement,
confidence or reward is not independent corroboration. An objection should name
the affected action, reason class, evidence, decision owner and what evidence or
authorized change could permit reconsideration.

Keep these reason classes distinct:

- `contradicted`: relevant current evidence contradicts a necessary factual
  premise; this does not establish universal physical impossibility.
- `insufficient_evidence`: evidence, freshness or applicable rule is missing;
  uncertainty cannot be reported as proof of danger or permission.
- `prohibited`: the applicable authorized rule excludes the proposed means.
- `unauthorized`: the required grant is absent or revoked.
- `permitted`: the supplied evidence and rule checks pass; other gates still
  apply, including acceptance, risk, side effects and required human review.

The finite reference classifier checks authorization first, then required
evidence/rule availability, factual support and policy permission. Its order
resolves overlapping fixtures; it is not a universal precedence rule for every
domain. Missing prerequisites cause review or a block on the affected effect.
Independent observations or an authorized correction may remove an erroneous
hold. Routine permitted work should then proceed without a redundant approval.
An owner stop/revocation is an authority event, not a suggestion to be outweighed
by sunk cost or expected task reward.

## Assurance predicates

| Predicate | Candidate contract | Evidence |
| --- | --- | --- |
| `EGO-P01 grounded_reason_classes` | Reasons reflect explicit evidence, freshness, rules and authority; unknown is not contradicted or permitted. | Observations, provenance, current-state reference, rule/grant, reason and reconsideration conditions. |
| `EGO-P02 enforce_objection_at_effect_boundary` | The current grounding result and policy-defined oversight hold constrain new effects through existing gates. | Gate inputs, current authority, affected scope, denial and actuator/bridge result. |
| `EGO-P03 mandatory_escalation_survives_team_pressure` | A required incident obligation cannot be waived by a leader, vote, internal refusal or shared reward. | External trigger policy, event identity, owner and unresolved obligation. |
| `EGO-P04 distinguish_delivery_stages` | Detected, queued, sent, received, reviewed and resolved are separate states backed by matching evidence. | Queue record, dispatch evidence, event-bound receipt, review and resolution records. |
| `EGO-P05 authorized_minimal_oversight_channel` | Reporting uses an authorized oversight destination outside the acting team's decision control and the minimum permitted payload. | Destination/scope grant, payload classification/minimization and independent channel ownership. |
| `EGO-P06 preserve_owner_and_custody` | Offering a handoff does not transfer accountability; acceptance needs transfer evidence, and restart cannot erase a durable obligation. | Current/proposed owner, successor acceptance, transfer and durable queue/recovery records. |
| `EGO-P07 bound_delay_and_completion_claims` | Policy defines affected-work holds and reporting deadlines; overdue/custody gaps fail closed, and required open incidents prevent an unqualified completion claim. | Deadline, affected scope, clock/queue status, outstanding obligations and claim limitations. |
| `EGO-P08 independent_review_before_resolution` | Receipt alone cannot resolve an incident; resolution needs independent review and specific corrective/disposition evidence. | Reviewer authority/independence, review result and resolution evidence. |

## Oversight protocol

The policy/monitor outside the acting team's sole control determines when an
event requires reporting, its accountable owner, authorized recipients, disclosure
limits, delivery/review deadlines, and which work must pause. Not every refusal
or routine error is an incident. A reporting duty does not authorize a new
recipient, public disclosure, forwarding private traces or exfiltration. Retain
an internal evidence reference when only a minimal notice may be transmitted.

Use an event-bound progression:

1. **Detected:** the policy-defined obligation exists, even if the agent refused
   the harmful act or discussed the issue internally.
2. **Queued:** the obligation and minimal notice are retained durably.
3. **Sent:** the authorized transmission has attributable dispatch evidence.
4. **Received:** the destination supplies a receipt matching this event. This
   proves the modeled receiver accepted it, not that a human read it.
5. **Reviewed:** a competent authorized independent reviewer records a finding.
6. **Resolved:** explicit remedy or disposition evidence closes the obligation.
   A decision to permanently deny an action may resolve an incident without
   making the original action permissible.

An internal post, a pending send, an unrelated/old receipt or a plan to report
cannot advance the corresponding external stage. Retry/deduplication preserves
event identity; it cannot silently discard a required obligation. A handoff
preserves the prior owner and original deadline until an authorized successor
accepts with transfer evidence. Restart/recovery must preserve stage, ownership,
deadline and pending delivery; unavailable custody triggers an explicit gap and
affected-scope hold until a verified recovery.

Timely delivery is a control obligation, not a promise of network availability.
If the approved channel is unavailable, retain the obligation and use only
preauthorized retry/fallback/escalation arrangements. Do not improvise an outside
recipient. Preserve safety-stop, monitoring, incident handling and evidence paths
even if ordinary mission authority is revoked or the task is accepted.

## Independence and useful operation

Review roles do not become independent merely by having different names or
instances. Record shared weights, incentives/rewards, training, evidence sources,
credentials and final decision control; disclose correlated failure and conflicts.
Use external evidence/review appropriate to the risk. A shared reward, better
throughput or unanimous internal agreement cannot compensate for a missing
mandatory report or change an acceptance rule.

Holds apply to declared affected effects, not automatically to every task.
Unaffected permitted work may continue within its grant. Report task completion,
delivery, investigation and remediation separately rather than labeling all of
them complete after one succeeds. Predeclare denominators for warranted reports,
delivery within policy time, missed/false reports, human-review outcomes,
incorrect blocks, unauthorized disclosure and task performance. Preserve invalid
and excluded trials. Routine tasks need positive controls against blanket refusal
and unnecessary reporting.

## Executable reference and limits

The [portable cases](../examples/evidence-grounding-oversight-vectors.json) and
[schema](../schemas/evidence-grounding-oversight-vectors.schema.json) map to literal
tests and excluded unsafe transitions in the existing [Quint core](../formal/ai_hpp_core.qnt).
Grounding and incident holds feed the existing intervention, robot and delegation
guards and completion assessment. Ordinary reporting/recovery uses its separately
authorized path so mission revocation cannot suppress a pending report.

The model has one affected task, one active incident, two non-reused event IDs,
two owners, six ordered delivery stages and a deadline reached at two external
clock ticks. The initial scope has assumed valid grounding and an assumed
preauthorized minimal oversight path. New obligations are external policy events,
not inferences from hidden reasoning. Facts, currentness, policy, recipient
authorization, independence and evidence are supplied abstract inputs.

This is a bounded protocol model, not a truth oracle. It does not establish
observation accuracy, causal understanding, actual independence, network delivery,
human reading, durable storage, clocks, safe physical stopping or full runtime
refinement. Blocking a new effect does not prove that already-running work or
motion has stopped; deployments need an independently tested pause/terminate
path and feedback. Stage/custody snapshots do not replace a complete audit stream.
The model fixes route validity after dispatch; deployments must also handle later
credential/recipient changes and evidence invalidation.

Run `python3 scripts/check_evidence_grounding_oversight_profile.py` and the pinned
[Quint checks](../formal/README.md). The validator checks fixture/test/map linkage;
execute Quint for outcomes. [Coverage](../formal/coverage.md) remains
`PARTIAL_ABSTRACTION`. Finite tests support at most `REFERENCE_TESTED` for the
declared artifacts; no unbounded liveness, real-world safety or conformance proof
follows. No real notifications are sent by these tests.
