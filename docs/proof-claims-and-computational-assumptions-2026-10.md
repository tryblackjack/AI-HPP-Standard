# Proof Claims and Changing Computational Assumptions

**Status:** `ACTIVE_INFORMATIVE`; optional post-rc.1 assurance guidance.

**Date:** 2026-10-27

**Normative effect:** None. Frozen v4.3.0 owners/contracts and the immutable
v4.4.0-rc.1 package remain unchanged. No new mandatory gate is introduced.

## Purpose and existing ownership

Extend the existing [assurance protocol](assurance-evaluation-and-technical-oversight.md)
with explicit links between a requirement, formal statement, assumptions,
verification result and permitted claim. Prepare for changes in algorithms,
cryptanalysis and computing hardware without predicting their availability.
Existing MVP-003/004/005/006/007, KAI-REQ-003 and EAA-REQ-002 retain their
applicable authorization, evidence and claim ownership. A mathematical result
does not grant operational authority or establish deployed-system conformance.

## Scientific evidence boundary

OpenAI's [26 October announcement](https://openai.com/index/building-scientific-understanding-with-academic-communities/)
reports an ETH refutation and Lean formalization while inviting independent
examination. Anthropic's [pinned research artifact](https://github.com/anthropics/formal-math/tree/16a5ce41304fcdaea4e0be7c132e1c361dc26da5/eth)
also supplies a claimed subexponential counting algorithm and formalization.
These are source-attributed claims, not proof executions or mathematical review
performed by AI-HPP maintainers. Neither evaluates or endorses this standard.
The Anthropic documentation explicitly separates checking a formal proof from
checking that its formal statement matches the paper.

Refuting ETH would not settle P versus NP, establish polynomial-time algorithms,
or by itself break deployed cryptography. An asymptotic improvement is not a
measured speedup at a customer's instance sizes. Assess such results separately
from quantum algorithms, which use a different computational model.

## Proof-to-requirement evidence contract

For an adopter making a proof-backed claim, retain these fields in its existing
evidence bundle; the generic run manifest's evidence references can point to it:

| Record | Minimum content |
| --- | --- |
| Requirement | Stable ID, exact wording, revision, units, quantifiers, domain, acceptance criteria and excluded cases. |
| Formal statement | Exact theorem/model/property and source digest; correspondence to every claimed part of the requirement. Record omitted premises or weaker conclusions. |
| Assumptions | Identified axioms, trusted inputs, physical/measurement models, arithmetic/numerical assumptions, environment and computational/adversary model. |
| Proof/check | Proof/model digest, checker and kernel versions, pinned dependencies, command/configuration, bounds, result, logs and unresolved obligations. |
| Semantic review | Reviewer, competence/conflicts, statement-to-requirement comparison, disagreements, decision and evidence reference. |
| Implementation link | Exact evaluated build and input/output boundary; refinement or validation evidence, or an explicit absence of such evidence. |
| Claim lifecycle | Scope, status, dependent artifacts, owner, review triggers and superseding record. Preserve earlier versions and provenance. |

Check proof dependencies rather than grepping for a word. A `sorry` in a detached
challenge statement is different from an admitted obligation in the claimed
theorem's dependency closure. A declaration of success, cached build or model
explanation does not substitute for the required checker result. Re-check the
exact artifacts used in the claim within the declared trusted computing base.

Keep statuses separate: proof checked; statement correspondence reviewed;
implementation validated; empirical performance measured. None implies the
others. A bounded model check retains its bounds and abstraction limits even
when every explored state passes. A structural JSON/schema check is not a
theorem proof, cryptographic validation or hardware test.

For example, proving CAD geometry satisfies an envelope does not establish
payload capacity. The latter requires its own load cases, materials, boundary
conditions and justified analysis/measurement. Do not expand the proved claim
because both properties refer to the same assembly.

## Cryptographic agility and quantum readiness

Post-quantum cryptography means classical cryptographic mechanisms designed to
resist quantum attacks; it does not require a quantum computer. NIST's
[migration guidance](https://www.nist.gov/pqc) and
[standards overview](https://pages.nist.gov/nccoe-migration-post-quantum-cryptography/)
identify ML-KEM (FIPS 203) for key establishment and ML-DSA/SLH-DSA (FIPS 204/205)
for signatures. Algorithm standardization is not proof of a deployed protocol,
library, key lifecycle or implementation's security. Re-check current guidance
and implementation advisories at adoption and review.

Inventory confidentiality, authentication and evidence-integrity dependencies
separately: algorithm/parameters, protocol/library versions, keys/certificates,
trust roots, update signatures, grant signatures, audit seals, timestamps,
archival evidence, ownership and replacement paths. Record required secrecy and
verification lifetimes, exposure and migration lead time. Long-lived sensitive
ciphertext can require attention before a cryptographically relevant quantum
computer exists because it may be collected now for later decryption.

Plan replacement through reviewed interoperable implementations and protocols;
do not invent ciphers or hybrid combiners. Test mixed-version interoperability,
key/certificate rotation, downgrade rejection, resource limits, interrupted
migration, recovery and retained audit verification. A fallback may use only an
explicitly approved current security policy; migration failure must not silently
restore an obsolete algorithm. Preserve useful authorized services within their
declared boundary while reviewing the affected security claims.

Before the protection of an evidence archive becomes insufficient, assess
renewal/re-sealing with current mechanisms and trustworthy custody/time evidence.
Retain original artifacts, algorithms, verification context and renewal lineage.
Re-signing an already untrustworthy record does not restore its authenticity.
Do not automatically discard an entire historic archive when one dependency
changes; identify which claims and time periods are affected.

Quantum or other accelerator access remains an ordinary capability/bridge:
authorize provider, destination, payload, retention, budget, job identity and
results. Remote quantum service access is external disclosure, including derived
problem encodings; local inference does not make it local processing. Hardware
must be characterized by the task, logical versus physical resources, noise/error
correction, connectivity, data transfer and end-to-end cost. Access, a qubit count
or a simulator label is not demonstrated useful advantage.

Use classical baselines, preprocessing/postprocessing, retries, queue time,
accuracy and total resource accounting in comparative tests. Evidence of speed
does not waive correctness, data protection or authority checks. No date for
mass-market fault-tolerant quantum workstations is assumed. “Post-quantum” here
has its cryptographic meaning; unspecified future computing remains an explicit
unknown, not a claimed technology or new physics.

## Reassessment and portable review cases

A material algorithmic advance, cryptanalytic result, changed checker/axiom,
hardware capability, provider, key compromise, expired protection lifetime or
changed requirement triggers review of affected dependencies. Record whether the
result is reported, reproduced, independently reviewed or deployed. Re-evaluate
the affected claim and effects under existing gates; a headline alone neither
proves compromise nor permits scope expansion. Corrected evidence can restore a
qualified claim; retain the superseded record and rationale.

Adopters can use these portable cases at their own boundaries:

1. A valid proof of a weaker statement cannot pass the stronger requirement.
2. A missing proof, unresolved dependency or failed checker cannot become PASS.
3. A bounded proof cannot be published as an unbounded runtime guarantee.
4. A cryptographic dependency under review cannot retain an unqualified current
   security claim without disposition evidence; unrelated claims remain scoped.
5. A failed migration cannot silently downgrade protection or erase audit history.
6. Remote accelerator submission without payload/destination authority is denied.
7. A new algorithm without measured practical benefit cannot replace the measured
   performance result with an asymptotic claim.
8. A valid corrected statement, reviewed migration or authorized accelerator job
   can proceed within its existing grant; blanket refusal is not success.

These are review/integration specifications, not newly executed mutants or
quantum experiments. Existing Quint models contain no cryptographic algorithms,
proof-kernel implementation or quantum state; their operational transitions and
formal assurance map are unchanged. No cryptographic-strength, quantum-safety,
new mathematical theorem or runtime-refinement claim follows from this note.
