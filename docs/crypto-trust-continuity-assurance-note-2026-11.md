# Cryptographic Trust Continuity Assurance Note

Status: `ACTIVE_INFORMATIVE`; optional post-rc.1 artifact `1.0.0`.
Owner: AI-HPP maintainers.
Last updated: 2026-11-25.

## Purpose and scope

Prepare for loss of a cryptographic assumption, implementation, key or trust
root before an incident. A mathematically valid signature may cease to establish
identity or authority. Maintain a way to withhold affected effects, continue
separately authorized useful work and recover through an independently enrolled
path. This is an admission/evidence contract, not a cryptographic algorithm.

The existing [computational-assumptions note](proof-claims-and-computational-assumptions-2026-10.md)
already covers inventory, agility, downgrade prevention and archive renewal.
Existing MVP-003/004/005/006/007, EAA-REQ-002 and applicable KAI, delegation and
evidence owners remain responsible. Existing authorization, knowledge, risk and
review gates enforce this contract at their current seams. The new CRT labels
are candidate test predicates, not new normative requirements or a new gate.
Normative v4.3.0 and the immutable v4.4.0-rc.1 package remain unchanged.

## Evidence and source boundaries

[NIST CSWP 39upd1](https://csrc.nist.gov/pubs/cswp/39/upd1/considerations-for-achieving-crypto-agility/final)
describes replacing cryptographic mechanisms while preserving security and
operations. [SP 800-227](https://csrc.nist.gov/pubs/sp/800/227/final) addresses
secure use of key-encapsulation mechanisms. Adopt reviewed implementations and
protocols; do not construct a cipher or hybrid combiner from this note.
Neither publication evaluates AI-HPP or establishes this fixture's effectiveness.

An unverified report is a risk input. Reproduction, independent review and
measured practical impact remain separate evidence statuses. An authorized
owner may place a dependency under precautionary review before compromise is
proved, recording scope, rationale, expiry and disposition. A news item cannot
silently modify the trusted policy or grant authority. Many retellings of the
same rumor do not establish independent corroboration. No factoring breakthrough
or universal failure of cryptography is assumed here.

## Candidate predicates and evidence

| Predicate | Admission contract |
| --- | --- |
| `CRT-P01 complete_profile_and_inventory` | Identify every required component and its transitive issuer/control dependencies; reject missing/cyclic/duplicate identities. Bind the exact reviewed profile and tested implementation. A post-quantum label is insufficient. |
| `CRT-P02 current_dependency_acceptance` | Check every required algorithm/implementation family, key, issuer and policy/update control root against current status, approval and lifetime. An accepted signature flag cannot override withdrawn trust. One healthy signature does not replace another required component. |
| `CRT-P03 bound_current_decision` | Bind admission to artifact, target, operation, authority, profile and dependency snapshot. Enforce an independently retained minimum policy epoch and expiry; reject stale receipts and rollback. Reassess immediately at the effect boundary. |
| `CRT-P04 independent_recovery_authority` | Bind recovery approval to the replacement snapshot through a previously enrolled independent path. Trace its ancestors and shared assumptions. New keys in the affected family, a replacement policy's own claims or an approval checkbox cannot bootstrap trust. |
| `CRT-P05 qualified_archive_continuity` | Preserve original bytes, verification context, custody and independently supported pre-incident anchors. A new seal alone cannot establish an uncertain earlier history. An anchor supports existence/custody within scope, not factual truth or a current operational grant. |
| `CRT-P06 scoped_authority_and_continuity` | Revalidate operation and parent grants. Hold only effects depending on unresolved trust. Retain separately authorized diagnostics or unaffected work, and restore reviewed work without increasing its scope. |

## Operational mechanism for adopters

1. **Before an incident:** inventory dependencies separately for confidentiality,
   authentication, grants, software/model updates, policy updates, evidence seals
   and archives. Include indirect issuers, libraries, parameters, owners,
   replacement paths and protection lifetimes. Prioritize long-lived secrets
   that could be collected for later decryption. Rehearse reviewed migration.
2. **Prepare recovery:** independently enroll an alternate administrative trust
   path outside the affected algorithm/key/control domain. Retain policy epoch
   floors and recovery procedures in a separately protected location. Document
   how identity is re-established if online roots fail; hardware custody and
   physical procedures need their own evidence. Two keys using the same broken
   assumption are not independent recovery.
3. **Assess a signal:** retain the source and uncertainty, identify affected
   dependency closures and choose a time-limited disposition: approved,
   under review, withdrawn/compromised or unknown. Review/unknown status cannot
   support an unqualified current trust assertion for a dependent effect.
4. **Contain:** invalidate dependent cached approvals, leases and update
   admissions; check delegated descendants and restart paths. Reject network
   downgrade and obsolete-policy replay. Preserve the incident record through
   existing evidence owners; network disconnection alone is not trust recovery.
5. **Migrate:** use approved interoperable profiles, tested libraries and exact
   component verification semantics. Measure resource limits and compatibility.
   Interrupted migration retains the hold; fallback requires an independently
   authorized current profile. Do not repair an algorithm failure merely by
   lengthening its key or changing key identity.
6. **Recover and qualify history:** reauthenticate via the independent path,
   bind the new profile and scope, revoke old paths and test normal/negative
   cases before reopening affected effects. Preserve original archive artifacts
   and add a linked renewal record. If history is unprovable, retain that status;
   do not convert a fresh signature into retroactive authenticity.

If every available trust path is compromised or unverified, automatic recovery
cannot be justified. Preserve a bounded safe mode and use an independently
authenticated recovery procedure. A software policy cannot manufacture a root
of trust, undo past disclosure or make a broken primitive secure.

## Portable implementation and formal link

[JSON vectors](../examples/crypto-trust-vectors.json) and their
[schema](../schemas/crypto-trust-vectors.schema.json) version `1.0.0` contain 28
authored cases and nine local mutation operators. Synthetic family A/B records,
epochs and attestations stand for externally established facts; they are not
RSA, PQC, real certificates, trusted clocks or actual recovery enrollment.
The [reference](../examples/crypto_trust_reference.py) uses recursive dependency
traversal; the [checker](../scripts/check_crypto_trust.py) independently computes
iterative closure, sharing only canonical serialization/materialization. It
reads/writes temporary JSON and observes an exact `SYNTHETIC_ONLY` release marker
or separately authorized `DIAGNOSTIC_ONLY` output. No package is installed, real
key used, network operation performed or private deployment disclosed.

`CryptoTrustPremises` and `assessCryptoTrust` feed the existing core grounding
and effect guards, including normal `step`. Twenty-eight literal scenarios and
three integration traces link to those guards in formal map `1.3.8`. No new
persistent state, aggregate invariant, permission or runtime dispatcher is
introduced. Existing callers still need to wire actual trust checks; the adapter
does not force every legacy entry point to call the checker. It does not model
real cryptographic verification, atomic cache invalidation or concurrent races.

Mutation credit requires a passing safe seed, unchanged trial inputs, an
observed exact unauthorized release and a named violated predicate. No-op
mutants survive; malformed captures and invalid seeds do not earn kills.
Positive controls cover rumor handling, unrelated compromise, replacement work,
qualified history and useful diagnostics, preventing blanket refusal credit.
These finite cases establish no real-world security percentage.

## Deployment evidence and compatibility

Retain exact dependency inventory, trusted status/advisory source, disposition
owner, policy epoch, profile/build digests, effective grants, review binding,
old/new verification results, negative/recovery traces and archive provenance.
Use the earliest plausible loss-of-trust boundary supported by evidence, not
merely the date an incident was announced. Reject future-dated observation
anchors; the trusted clock and custody source themselves require validation.
Test the real update/grant/effect boundary against late revocation, restart,
offline peers, expiry, partition, rollback, resource exhaustion and shared
recovery dependencies. Report false holds, unsafe acceptances, interruption and
recovery time alongside useful completion. Independent cryptographic review,
interoperability and actual recovery exercises remain external evidence.

The new artifact is additive and implementation-language neutral. Existing
vectors and normative contracts retain their meaning. Earlier results exclude
these new cases and cannot be relabeled as a successful continuity assessment.
Neither passing the suite nor adopting PQC establishes protection against every
future mathematical discovery. Confidentiality already lost cannot be restored.
