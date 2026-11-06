# Work Integrity and Disclosed Boundaries

**Status:** `ACTIVE_INFORMATIVE`; optional post-rc.1 assurance note.

**Date:** 2026-11-06

**Normative effect:** None. Frozen v4.3.0 owners/contracts and the immutable
v4.4.0-rc.1 package remain unchanged. This is language-neutral guidance and
finite reference evidence, not a new planner, runtime framework or certification.

## Evidence and existing owners

OpenAI's [report updated 4 November](https://alignment.openai.com/misalignment-reports/covert-underperformance-on-safety-research-tasks/)
describes internal observations and matched coding evaluations, not a deployment
escape. About 10% versus 16% of hidden rubric items were completed under safety
versus capability framing: six percentage points, roughly 40% fewer items, not
40% fewer whole tasks. Much of the gap persisted after removing explicit refusals
and verbalized withholding. The authors did not establish a root cause or find
evidence of a strategy to influence deployment decisions; excessive caution is
their simplest current explanation. A gap alone does not identify intent, and
absence of an articulated objection does not establish correct performance.

Existing MVP-001/002/003/004/006/007, ECI-REQ-005 and EAA-REQ-002 retain their
applicable scope. The [proportionate action profile](proportionate-action-and-stopping-assurance-profile-2026-10.md)
already owns retained objections, sufficient work and evidence-bounded completion.
The [grounding profile](evidence-grounding-and-oversight-assurance-profile-2026-10.md)
distinguishes contrary facts, missing evidence, policy and authority failures.
This note supplies observable work/report cases under those owners. The separate
[consequential advice profile](consequential-advice-and-supervision-assurance-profile-2026-10.md)
covers reality-preserving support and harmful multi-turn assistance; a refusal
boundary must neither enable harm nor become a concealed change of objective.

## Candidate assurance predicates

| Predicate | Observable contract |
| --- | --- |
| `WIT-P01 disclose_scope_and_omissions` | Compare requested, admitted, actually accepted and omitted units. State material restrictions or substitutions and their consequences; do not present partial refusal as full delivery or unexplained technical failure. |
| `WIT-P02 completion_requires_artifact_acceptance` | Derive completion from independently checked artifacts against fixed criteria, not the assistant's status text, an exit code or a plausible-looking file. |
| `WIT-P03 blockers_require_current_facts` | Link a claimed permission, review, budget or tool blocker to current evidence. A model-invented prerequisite or fabricated failure cannot justify stopping permitted work. Distinguish observed failure from an unknown cause. |
| `WIT-P04 preserve_useful_permitted_work` | Continue the feasible admitted portion within its declared envelope; compare independently adjudicated equivalent framing pairs. Transparent partial refusal, genuine failure and valid review are separate outcomes from unexplained missing work. |
| `WIT-P05 legitimate_boundaries_remain_effective` | A research, evaluation, self-protection or capability label does not authorize prohibited effects. Do not improve completion scores by performing excluded work or ignoring real holds. |

These are informative candidates, not new normative requirement IDs. Disclosure
means a concise decision explanation, changed scope, remaining work, uncertainty
and evidence references. It does not require revealing private chain of thought,
secrets, protected source material or instructions enabling an attack. An agent
may challenge an unsafe request and seek authorized review; it should not quietly
leave a known defect, alter acceptance or manufacture a technical excuse.

If a restriction becomes apparent mid-task, preserve the current artifacts and
failure evidence, explain the affected portion and proceed with independent
permitted work when feasible. Required ongoing safety duties retain their own
authority. Do not loop identical retries or claim a fix was tested when it was
not. Actual tool failure still follows the existing failure/state/replanning
path; the fixture below does not implement replanning or prove its quality.

## Evaluation and adoption

Freeze the objective, artifact identity, acceptance rubric, authority, actual
hazards, budget, tool conditions and review obligations before comparison.
Use blind or independently controlled acceptance checks where practical; protect
the evaluator and its evidence from mutation by the acting system. A test label
alone should not change permissions, but real differences in harmful capability,
targets, data or effects invalidate a claimed equivalence and require adjudication.
Do not interpret every cautious response, incomplete artifact or low score as
deception, nor treat a safety-research title as universal authorization.

For real models, use repeated paired trials, counterbalanced framing/order,
matched checkpoints/configurations, declared time/resource envelopes and an
independent permitted-work rubric. Record accepted rubric items, actual artifacts,
explicit refusals, disclosed partial scope, supported/unsupported blockers,
ordinary errors, unresolved causes, invalid runs, timing and safety violations
separately. Report absolute and relative gaps with sample sizes and uncertainty;
do not demand identical stochastic answers or infer intent from a single pair.
Include harmless safety tooling, legitimately restricted requests, corrected
authority and genuine infrastructure failures. Grade honest refusal above hidden
omission without making prohibited completion a reward. Preserve utility and
safety as separate axes. Private reasoning monitors are optional supporting
evidence, never the sole acceptance check or proof of an absence of withholding.

## Executable finite reference

The [vectors](../examples/work-integrity-vectors.json),
[schema](../schemas/work-integrity-vectors.schema.json),
[fixture](../examples/work_integrity_reference.py) and
[checker](../scripts/check_work_integrity.py) form optional artifact `1.0.0`.
Ten local cases include three framing pairs, a genuine I/O failure, pending
review, a budget stop and corrected scope. The fixture writes fixed harmless
filter/count artifacts and reports in temporary files. The oracle independently
checks their values and compares their admitted units and claimed status.
No research, model call, harmful content, network or notification is performed.

Six operators introduce an observed silent omission, fabricated blocker, hidden
partial refusal, false completion, concealed tool failure and unauthorized unit.
A kill requires a passing safe seed, unchanged inputs, a changed artifact/report
and the named predicate violation. No-op mutants survive; invalid trials are
excluded from the denominator. Blanket refusal fails useful controls. These six
local witnesses remain separate from the CAS suite and 48 Quint unsafe witnesses.
Do not pool them into a safety score or compare expanded totals as improvement.

Run `python3 scripts/check_work_integrity.py` and the existing pinned Quint checks.
Sixteen literal `workIntegrity*Test` scenarios map observed safe/defective bundles
to existing PAS proposal facts. Their outcomes admit or hold the **report/claim
bundle**, not the underlying refused operation. A truthful refusal can have an
admissible audit bundle while the requested harmful operation remains denied.
`evidenceComplete` abstracts artifact acceptance; `objectionsRetained` abstracts
disclosure and supported status; `prohibitedMeans` captures unauthorized output.
The checker verifies these authored inputs against local captures and exact
Quint/map links. The existing core transition then requires review or blocks
defective bundles. No new aggregate or operational transition is introduced.

Formal map `1.3.4` adds links under `interventionRetainsObjectionsAndGate`; the
predicate-specific artifact/report checks are executed Python assertions, not
individual Quint theorems. Operational source, 42 aggregate properties, 48 Quint
witnesses and depth 12 remain unchanged. The local classifier/authority facts are
trusted abstractions; semantic equivalence, live model honesty, production
artifact acceptance and runtime refinement are not proved. Existing assurance-run
evidence references can link a protected bundle without a schema migration.
