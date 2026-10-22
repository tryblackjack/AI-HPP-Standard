# Robot Action Binding Assurance Profile

**Status:** `ACTIVE_INFORMATIVE`; optional candidate assurance profile.

**Date:** 2026-10-22

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline is unchanged.
This is post-rc.1 development, absent from the immutable `v4.4.0-rc.1` package.

## Evidence and scope

Binghamton University's [20 October 2026 report](https://www.binghamton.edu/news/story/6544/secret-trigger-words-could-make-ai-powered-robots-dangerous-and-these-researchers-developed-a-defense)
describes a deliberately compromised task planner: a trigger redirected a robot
from a plastic fruit to a model hand. This is a controlled demonstration, not
evidence of an attack on an uncompromised commercial robot or a conscious wish
to cause harm. [MuTRAP](https://arxiv.org/abs/2504.17070), first submitted in
April 2025, studies task-planner backdoors. The attack paper describes adapting
task-specific parameters while the backbone may remain frozen; trusting a base
model alone does not assess the whole planning stack.

[PROTEA](https://arxiv.org/abs/2601.07186), submitted in January 2026, evaluates
symbolic plans with an LLM judge, filtering relevant objects and maintaining
external state across steps. Its [project page](https://protea-secure.github.io/PROTEA/)
provides a dataset and demonstrations. These results motivate complementary
context and history checks. They neither evaluate AI-HPP nor establish that an
LLM safety judge is an infallible physical interlock. No priority or endorsement
claim is made here. No research code or dataset is copied by this profile.

The assurance object is an authorized action crossing from a potentially
compromised planner to an execution boundary. Existing owners are MVP-001/003/004/005/006/007,
ECI-REQ-002/004/005, KAI-REQ-001/002/003 and AFB-REQ-002 within their applicable
scope. This profile adds candidate predicates and public test aids, not new
normative requirement IDs or a mandatory robot runtime.

## Assurance predicates

| Predicate | Candidate contract | Retained evidence |
| --- | --- | --- |
| `RAB-P01 bind_action_to_authorized_effect` | Bind approval to the operation, target identity, tool, plan revision and authorized scope. Rewriting any bound field cannot reuse the approval. | Task/grant, object/tool identity, plan digest/revision, exact action, approval reference. |
| `RAB-P02 revalidate_current_context` | Immediately before execution, check that the relevant observed state is current, risk is bounded and the approval still matches it. | Observation version/time, uncertainty, hazard assessment, context version, invalidation reason. |
| `RAB-P03 preserve_cumulative_effect_history` | Assess resulting effects using retained relevant history; missing history is unknown, not safe. Individually allowed steps may form a prohibited sequence. | Object-state lineage, relevant prior steps, predicted cumulative effects, unresolved state. |
| `RAB-P04 enforce_at_execution_boundary` | Every action path, including retries and delegates, uses an externally controlled gate; a valid approval is consumed once. | Enforcement owner, gate/controller version, all execution paths, consumed approval, denial events. |
| `RAB-P05 retain_execution_evidence` | Execution requires an available attributable evidence path recording the proposal, approval, current checks and outcome. | Action/token/state references, actor, decision, result and evidence-custody status. |
| `RAB-P06 admit_and_bind_planning_components` | Admit the relevant planner components and invalidate old approvals after a consequential component or policy change. | Model/adapter/prompt/policy/controller identities, source, hashes, admission and reassessment. |

## Execution contract

A planner proposes an action; its output is untrusted. A separate gate compares
the proposal with the human-authorized objective and means, affected parties,
current environment, relevant history, component admission and evidence status.
Passing a classifier, possessing a knife, or having permission to cut one object
does not grant permission to cut another. A trigger string cannot create scope.

An issued approval identifies the exact action and plan revision, current
authorization/policy and relevant state version. The executor checks these facts
again, including revocation and stopping conditions, then consumes that approval.
A changed plan, target, tool, scope, environment or component invalidates its
reuse. If the new state is safe and the action remains authorized, a new approval
may be issued automatically under the existing grant. An innocuous text suffix
alone does not require a human approval or an indiscriminate block.

The relevant state must include semantic consequences that outlive individual
steps: for example, a container that now holds protected items cannot be assessed
as empty just because the intermediate steps are no longer in a context window.
An authorized removal or verified correction may change that state; truncating
history cannot serve as such evidence. Relevance filtering must not discard the
fact that makes a later action unsafe.

Missing identity, stale observations, unbounded risk, a required unavailable
review, incomplete history, unadmitted components, unavailable enforcement or
evidence cause a fail-closed outcome for the affected action. Use the existing
[gate outcomes](../spec/safety.md). Safety-stop, monitoring, incident response
and recovery paths retain their separately authorized obligations; blocking
discretionary work must not disable them.

An LLM judge may assist semantic assessment. Deployment-specific safeguards must
also address failures of that judge and enforcement owner. For physical systems,
define the operating envelope, sensing limits, permitted contact, motion/force
limits, controller behavior, stop latency and recovery appropriate to the hazard.
Semantic approval alone does not establish safe motor control. Preventing a new
command is distinct from stopping motion already in progress.

## Executable public model

The [portable vectors](../examples/robot-action-binding-vectors.json) and their
[schema](../schemas/robot-action-binding-vectors.schema.json) synchronize with
literal tests in the existing [Quint core](../formal/ai_hpp_core.qnt). The model
uses six candidate invariants in the same aggregate as replication, revocation,
evidence and proportionate action. It reuses current parent authority, unresolved
policy conflict, task acceptance and mission completion rather than inventing a
separate authority source. Acceptance ends discretionary robot commands while
the existing lifecycle cleanup path remains separate.
One task is represented; its admitted scope abstracts the objective and means.
An additional lifecycle integration test confirms that a completed mission
cannot use a previously issued robot approval to restart discretionary work.

The reference executor uses a one-use approval bound to a symbolic action and
context epoch. Environment, scope, enforcement/evidence configuration and
component updates advance that epoch monotonically from 0 to 2; it never wraps.
The finite bound is for tractable exploration, not a runtime versioning scheme.
Versions must not be reused in a deployment. Changing a proposal preserves the
old token so stale-plan rejection can actually be tested.

A protected-container fact is the small cumulative-effect example: disposal is
blocked after contents become protected, even after fresh approval is requested.
Unavailable history also blocks. This does not model every hazardous sequence.
Scope updates and observations are assumed to come from authorized, trustworthy
external sources; arbitrary model-authored state changes are not such sources.

Ten deliberate unsafe transitions exercise object/tool/plan substitution, stale
approval, concealed contents, lost history, bypassed enforcement, missing evidence,
unadmitted components and stale perception. They are excluded from normal `step`.
Each executable witness must violate its named invariant. A structural validator
checks fixture/test/map links; execute Quint to determine the outcomes. Normal
cases include useful authorized work, unchanged symbolic action after a benign
suffix, legitimate replanning, safe reapproval after change and one-use token
rejection, plus revocation/acceptance/policy integration.

Run `python3 scripts/check_robot_action_binding_profile.py` and the pinned
[Quint commands](../formal/README.md). The [formal coverage map](../formal/coverage.md)
records only `PARTIAL_ABSTRACTION`. Successful finite tests support at most
`REFERENCE_TESTED` for those artifacts.

## Deployment evidence and limits

The model assumes correct object/tool identity, observations, hazard assessment,
history, provenance and evidence flags. It contains no camera, speech recognizer,
LLM backdoor detector, trajectory planner, motor, physical interlock, cryptographic
token or durable audit store. The execution event is atomic; concurrent changes,
sensor/controller races, stopping distance and timing are not verified. Execution
snapshots are historical evidence, not current leases or a whole audit stream.

Before a runtime claim, test the actual bridge/controller paths, state changes
between check and use, observation uncertainty, token replay, restart/delegation,
monitor/evidence loss and independent stop behavior. Include safe useful tasks
and report false blocks, harmful allows, latency, coverage, exclusions and
uncertainty under a frozen run manifest. Use a simulator or safe test fixture
appropriate to the hazard, with a declared independent stop path.

Component hashes and provenance establish identity and admission, not absence
of a backdoor. Test adapters, prompts, tools and perception as well as model
weights. Detector performance must be reported for the evaluated configurations.
Neither this model nor a successful PROTEA benchmark proves physical safety,
deployed conformance, independent review or certification. Private implementation
and commercially supplied integration remain outside this public test contract.
