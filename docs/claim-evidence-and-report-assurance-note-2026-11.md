# Claim Evidence and Report Assurance Note

Status: `ACTIVE_INFORMATIVE`; optional post-rc.1 artifact `1.0.0`.
Owner: AI-HPP maintainers.
Last updated: 2026-11-21.

## Purpose and evidence boundary

Keep a generated assessment from acquiring factual or operational authority
merely by entering an official-looking report, signed workflow or decision brief.
Analysis, presentation, verification, approval, disclosure and action are distinct
events. A valid hash establishes byte identity, not truth; review is not effective
merely because a person clicked an approval box.

CNN's [18 September report](https://kvia.com/politics/cnn-us-politics/2026/09/18/exclusive-us-military-had-close-call-after-using-ai-for-false-intelligence-report-sources-say/)
attributes a spring 2026 aborted interception preparation to an erroneous
AI-assisted cargo assessment subsequently packaged as an intelligence report.
It cites anonymous sources; the model, actual cargo and complete operational
records were not disclosed. [Senators requested an investigation on 21 September](https://www.reed.senate.gov/news/releases/reed-warner-and-coons-seek-investigation-into-faulty-ai-assisted-intelligence_operations).
That request is not a finding confirming the account. Neither publication
establishes that a world war nearly occurred or that AI autonomously ordered an
operation. This note uses the reported failure mechanism, not disputed details,
as motivation for neutral synthetic engineering tests. No classified information,
military targeting workflow, private implementation or operational payload is used.

## Existing owners and compatibility

MVP-001/002/003/004/005/006/007, KAI-REQ-001/002/003/004 and applicable
ECI/ICA evidence and review owners already govern this boundary. The existing
Knowledge Admission, Risk, Human Review and Tool Authorization gates own their
respective checks. [EGO](evidence-grounding-and-oversight-assurance-profile-2026-10.md),
[WIT](work-integrity-and-disclosed-boundaries-assurance-note-2026-11.md) and
[CBA](cyber-operation-authority-assurance-note-2026-10.md) remain reusable aids.
CER identifiers below are candidate test labels, not new normative requirements.

Normative v4.3.0 owners/contracts and the immutable v4.4.0-rc.1 package remain
unchanged. This additive optional artifact introduces no runtime framework,
mandatory implementation language or new gate. Adopters implement the checks at
their existing evidence-to-decision boundary, outside the generator's sole control.

## Candidate predicates

| Predicate | Contract and evidence |
| --- | --- |
| `CER-P01 claim_specific_support` | Bind every decision-relevant claim to evidence supporting that particular subject, property and context. A relevant-looking citation, document template, confidence score or source classification does not establish entailment. Preserve the distinction between observation, inference, unknown and verified result. |
| `CER-P02 independent_evidence_lineage` | When policy requires corroboration, trace underlying acquisition origins. Preserve all observations for claim matching before deduplicating supporting origins. Reformatting, multiple agents and repeated citations of one source do not create independent evidence. Missing or cyclic provenance cannot close a required support gap. |
| `CER-P03 current_integrity_and_contrary_evidence` | Check admitted source identity, content, applicability and time. Retain relevant contrary evidence and uncertainty even when the generated report omits it. An authentic document may still contain an unsupported claim. |
| `CER-P04 effective_bound_review` | Bind required review to current claims, sources, policy and decision context. Verify reviewer authority, relevant access and independence. A changed report/context invalidates old admission or review; re-review under an existing valid grant can restore work. |
| `CER-P05 consequence_and_authority_boundary` | Hold the unsupported consequential release/effect. Preserve separately authorized local drafting, evidence requests and protective work, with limitations visible. Urgency or a persuasive report cannot supply authority or missing evidence. |
| `CER-P06 inherited_disclosure_scope` | Enforce both the report's own restriction and inherited source/derived-information restrictions before transmission. Neither floor replaces the other; a reviewer also needs access to the report itself. Reformatting or a lower label on a generated report cannot declassify its dependencies. Use an authorized scoped review/attestation path when a reviewer cannot access the underlying material. |

## Evidence-to-action procedure

1. Freeze the exact decision, purpose, decisive claims and acceptance criteria.
   Retain claim IDs, attributable source spans or measurement records, source
   class, origin lineage, hashes, revision, currentness and conflicts.
2. Evaluate factual support and any inference method separately. A source that
   mentions a subject does not prove a requested property. Inspect the actual
   derivation, units and assumptions; preserve unknowns and alternatives.
3. Check independence against the declared hazard model. Distinct names, signatures
   or report IDs can share an origin, data path, model, incentive or failure.
4. Where review is required, record the responsible reviewer's authority,
   competence, access, dependency limits, actual finding and exact binding. Do not
   solve missing clearance by sending restricted evidence to an unauthorized party.
5. Revalidate the snapshot at the effect boundary; a previously approved report
   does not authorize a changed action, resource, recipient or environment.
   Stop/escalation and safe recovery retain their separately authorized paths.
6. Report what was accepted, withheld and unresolved. Publication, signature,
   polished formatting, receipt or a completed checklist is not task acceptance.

This contract is not a universal two-source rule or per-action approval request.
Policy can permit a single qualified source and routine work without human
review. Required support/review remains proportional to consequences. Legitimate
declassification, correction or emergency action needs its applicable authority
and evidence; this reference fixture does not implement those procedures.

## Executable reference evidence

The [portable vectors](../examples/claim-evidence-vectors.json) and
[schema](../schemas/claim-evidence-vectors.schema.json) contain twenty-five authored
cases, two format-only pairs and nine behavior-changing local operators.
The [reference fixture](../examples/claim_evidence_reference.py) writes and reads
synthetic JSON records in a temporary directory and conditionally produces a
release marker or an explicitly unverified local draft. No external action runs.
The [checker](../scripts/check_claim_evidence.py) uses an independently written
iterative lineage oracle; the candidate walks ancestry recursively. Both inspect
the same captured structured inputs, not a candidate's claimed success.

Cases include unsupported and partially supported claims, irrelevant citations,
shared ancestry, cycles, expired/changed evidence, blind or same-path review,
stale admission/review, omitted contrary evidence, subject/context mismatch,
revocation and inherited disclosure. Useful controls retain qualified reports,
format invariance, permitted single-source work, local drafts and reviewed recovery.
Mutation credit requires a passing safe seed, unchanged inputs and an observed
unsafe release violating its named predicate. Invalid/no-op/blanket-denial controls
and formal/vector drift tests prevent optimistic accounting. No model-level
effectiveness or comparative safety percentage is claimed.

```bash
python3 scripts/check_claim_evidence.py
PYTHONPATH=. python3 -m pytest tests/test_claim_evidence.py
```

## Quint synchronization and limits of proof

`ReportPremises`, `reportEvidenceReady`, `reportGrounding` and
`assessEvidenceReport` extend the existing [core](../formal/ai_hpp_core.qnt).
The new action derives EGO grounding inputs from explicit report checks and is
included in normal `step`. Existing effect guards and parent-revocation checks
remain in force. No persistent state variable or aggregate property is added.
Legacy grounding callers remain supported; deployments adopting this optional
contract must not bypass the report checker by setting generic evidence flags.

Twenty-five literal scenarios plus recovery and late-revocation integration traces
exercise this adapter. Map `1.3.7` links them to existing grounding/effect properties:
270 core tests, 287 across both models. Existing 42 aggregate properties, 48 Quint
unsafe witnesses and depth-12 bound remain. The nine local operators are not
additional Quint unsafe transitions and have their own denominator.

The model trusts the checked premises; it does not derive real-world truth from
text. Local claim matching uses exact integer measurements, source origin labels,
finite ancestry and a toy two-level disclosure policy. Source identity, physical
measurements, reviewer competence/access, dependency declarations and the clock
need deployment evidence. A correctly bound but mistaken human review is possible.
Atomic context capture, partial-access attestations, noisy measurements, distributed
races and natural-language entailment are outside this fixture. KAI coverage is
not promoted to a full theorem or runtime conformance claim.

## Related failure classes and next adoption evidence

The [observation note](observation-admission-and-perceptual-integrity-assurance-note-2026-11.md)
already covers shared sensor/feed dependencies and qualified recovery. Apply
the same independence question to reports; a common network or shared source
can invalidate apparent redundancy. Hardware/configuration changes likewise
require reassessing what an old integrity or review record actually covers.
No aviation outage, physical fault-injection experiment or hardware root of trust
is reproduced or validated by these tests.

An implementation assessment should exercise its actual source retrieval,
claim binding, reviewer interface and release/effect boundary. Measure unsupported
acceptances, false holds, useful completion/recovery, review burden and missing
evidence over a declared task set. Independent engineering review and observed
runtime records matter more than adding further prose or increasing fixture counts.
