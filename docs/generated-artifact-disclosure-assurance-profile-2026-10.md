# Generated Artifact Disclosure Assurance Profile — October 2026

**Status:** `ACTIVE_INFORMATIVE`; optional candidate assurance contract.

**Date:** 2026-10-18

**Artifact version:** `1.0.0`.

**Normative effect:** None. The frozen AI-HPP v4.3.0 baseline and published
v4.4.0-rc.1 package are unchanged. This is post-rc.1 development on `main`.

## Purpose and boundary

Permission to process information is not permission to publish it. A generated
page, bundle, export, log, deployment, or retained old application can disclose
data just as directly as a tool call. This profile covers disclosure through
artifacts created or changed by agents, including software delivered to users.

The model should use synthetic data for prototypes, identify sensitive inputs,
implement server-side authorization before returning protected data, and state
which security properties remain unverified. The surrounding system should
enforce publication authority, independent tests, and release decisions outside
the acting model's sole control. Human review is an additional control; an
approval of an unspecified payload is insufficient evidence of informed release.

The contract is language-neutral. The Python fixture is an optional executable
reference, not a required runtime, production framework, security scanner, or
implementation of 1UA-AGE. It contains only synthetic data and makes no requests
to incident infrastructure, leaked datasets, or web archives.

## Evidence and established practice

[MyBroadband's 16 October report](https://mybroadband.co.za/news/software/672602-south-african-coffee-franchise-exposes-company-and-private-data-in-vibe-coded-web-application.html)
describes an operations dashboard returning protected information with a login
page. The outlet reports verifying contact information associated with 132
locations and some financial/performance data. In a
[subsequent response](https://mybroadband.co.za/news/security/672647-ceo-of-top-south-african-coffee-franchise-responds-after-vibe-coded-web-application-exposed-sensitive-data.html),
Bootlegger acknowledged exposed historical information in a legacy application,
said it had taken the application offline, and said there was then no evidence
of access to its core databases. These are attributed reports and a company
statement, not a forensic audit by AI-HPP. They do not establish that all employee
records leaked, that every record remains archived, which agent produced a
particular defect, or that the model intended disclosure.

The control is established application security, not an AI-HPP invention.
[OWASP's Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
requires authorization outside the client, appropriate checks for static
resources, least privilege, and authorization tests. A login overlay cannot
protect bytes already delivered to an unauthorized browser. AI-HPP's contribution
here is a portable authority, release-evidence, and mutation-testing contract for
agent-generated artifacts. No claim of priority or incident prevention is made.

## Existing ownership and remaining gap

| Existing owner | Application of the existing control | Portable test gap addressed here |
| --- | --- | --- |
| MVP-002/003 | Risk, tools, destinations and authority | Processing grants separated from artifact publication grants |
| MVP-004; ECI-REQ-002/003/004 | External enforcement and side effects | Response bytes, build outputs and derivative channels in scope |
| MVP-006 | Missing authority or evidence fails closed | Release bound to tested bytes and effective deployment configuration |
| MVP-007; EAA-REQ-001/002 | Attributable evidence and bounded claims | Redacted findings, test provenance and lifecycle inventory |
| ICA-REQ-003/004 | Independent evaluation and reassessment | Negative authorization tests and executable unsafe mutants |

These links interpret existing owners; they do not add requirements to their
normative text or expand the existing Quint coverage map. Agent authorization
and authorization in an application built by that agent are separate boundaries.

## Assurance predicates

| Predicate | Portable acceptance rule |
| --- | --- |
| `GAD-P01 processing_is_not_publication_authority` | A source-read grant, broad build objective or available credential cannot substitute for an applicable publication grant covering data class, purpose, recipients, destination and retention. |
| `GAD-P02 authorize_before_delivery` | An unauthenticated or otherwise unauthorized request receives no protected representation; UI state is not authorization. |
| `GAD-P03 minimize_by_role_and_tenant` | Even authenticated requests receive only fields and records permitted for that principal, role, tenant and purpose. |
| `GAD-P04 cover_derived_delivery_surfaces` | HTML, hydration JSON, bundles, source maps, exports, APIs, errors, previews and cache delivery obey the same disclosure boundary. |
| `GAD-P05 bind_release_to_evaluated_identity` | Authority, approval and test evidence match the candidate build, effective configuration, policy, destination and data-classification snapshot; material changes require reassessment. |
| `GAD-P06 independent_negative_evidence` | Missing, incomplete, failing or self-certified required tests cannot authorize release; safe positive controls also pass. |
| `GAD-P07 reconcile_legacy_residue` | Old deployments, preview URLs, retained objects and caches are inventoried and independently checked as protected, removed or quarantined before lifecycle closure. |
| `GAD-P08 evidence_does_not_republish_payload` | Ordinary findings and logs use synthetic markers, classifications and restricted evidence references rather than copying confidential payloads into another public artifact. |

## Candidate release gate

Evaluate before publishing, exporting, sharing a preview, enabling a new audience,
or changing data sources, permissions, generated artifacts, deployment targets,
configuration, caches or lifecycle state. Local construction with synthetic data
may proceed under its existing grant; publication and real-data connection remain
separate decisions.

Inputs should include:

- accountable actor, human-authorized objective and current policy version;
- source lineage and classification, affected parties, permitted purposes,
  field/record scope, recipients, destinations and retention;
- publication grant, expiry, required human review, and explicit residual risks;
- candidate build digest plus effective configuration, policy, destination and
  classification identity, bound to test and approval evidence;
- independently collected response captures, role/tenant authorization matrix,
  anonymous and lower-privilege tests, safe positive controls and exclusions;
- current/legacy deployment and storage inventory, cleanup checks and rollback;
- tester identity and independence, run identity, times, evidence integrity,
  access policy, redacted findings and unresolved results.

An implementation adopting this profile should return `allow` only for that exact
declared scope when the required evidence passes. Absent, stale or ambiguous
authority/evidence produces `block` or `review`; discovered exposure invokes an
authorized containment and incident path. It must not silently discard evidence,
delete unrelated resources, or claim that removing the current URL retracts
previously disclosed copies. Recovery can continue under a separate scoped grant.

Approval should describe the actual data classes, audience, destinations and
unresolved findings. Reusing an earlier approval after changing the candidate or
effective configuration is not an adequate release control. Hashes bind identity;
they do not prove approval authenticity, confidentiality or test completeness.

## Repeatable evaluation procedure

1. Freeze the deployment boundary, grant, versions, role/tenant matrix, build and
   effective configuration, coverage list and acceptance rules before testing.
2. Use isolated synthetic records with distinct markers for restricted fields
   and tenants. Do not retrieve or republish leaked production data.
3. Capture responses with clean anonymous clients, lower-privilege clients and
   cross-tenant clients. Inspect the actual response bytes, not the rendered
   appearance of a password screen. Include static artifacts, source maps, APIs,
   exports, errors and previews in the declared inventory.
4. Prime caches with an authorized request, then repeat as a different principal
   and tenant. Include stale objects and old deployments in lifecycle checks.
5. Verify positive controls: intentionally public data, a correctly scoped
   authorized response, field-limited access and an isolated authorized cache remain
   usable. Reject blanket refusal as a successful implementation.
6. Remove each control through a declared mutant. Retain the observed response,
   violated predicate and detecting test by restricted reference. A `KILLED`
   label is insufficient without an executed counterexample.
7. Reconcile failures, missing coverage and exceptions; release only through the
   independent gate for the exact tested candidate. Repeat affected tests after
   any material change, including decommissioning or configuration changes.

The portable [vectors](../examples/generated-artifact-disclosure-vectors.json)
and [schema](../schemas/generated-artifact-disclosure-vectors.schema.json) define
eight predicates, thirteen negative vectors/mutants and four positive controls.
Run the public reference checks with:

```bash
python scripts/check_artifact_disclosure_profile.py
PYTHONPATH=. pytest tests/test_artifact_disclosure.py
```

The executable [fixture](../examples/artifact_disclosure_reference.py) simulates
HTTP request/response bodies, role/tenant filtering, cache priming, diagnostic
output and an old endpoint. Its oracle is separate from the fixture's response
generator and derives expected field access from a fixed test policy. The
checker reports observed `KILLED`, `SURVIVED`, `INVALID` and `NOT_APPLICABLE`
counts, with the applicable mutation denominator. It exits unsuccessfully on a
survivor, invalid case, missing coverage or failed positive control.

## Claim limits and migration

Artifact/schema `1.0.0` is a new opt-in format; it changes no existing vector
shape, requirement ID or gate outcome. Record the commit and artifact version
when adopting it. Existing results are not automatically comparable to runs that
add these surfaces or cases. The published rc.1 tag and manifest remain immutable;
a later package version is needed to include this development snapshot.

The finite reference fixture can establish `REFERENCE_TESTED` for its declared
synthetic cases only. It is not a real web server, browser, CDN, archive service,
deployment platform or identity provider. Its independent tester and grant are
modeled inputs, not cryptographically verified runtime evidence. The suite does
not prove generated-application confidentiality, detect every encoding or
transformation of a secret, validate arbitrary logs, prevent inference attacks,
or replace an application-security review. Marker absence alone is not proof of
confidentiality. A production adapter must capture real responses, enforce the
actual authorization policy, cover relevant encodings and surfaces, authenticate
evidence and approvals, and record excluded paths and residual risk.

No new Quint invariant or whole-application proof is claimed. Promotion to a
normative release requires independent review, deployment evidence, complete
traceability and migration under [repository governance](repository-governance.md).
