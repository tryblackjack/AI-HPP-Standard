# Commerce Trust and Transaction Assurance

Status: `ACTIVE_INFORMATIVE`; optional candidate contract, post-rc.1.
Owner: Repository maintainers
Last updated: 2026-11-27
Artifact/vector/schema version: `1.0.0`.

## Purpose

Connect seller evidence and exact transaction approval to the existing knowledge,
authorization and grounded-effect boundary. An AI recommendation, a professional
storefront, HTTPS or a successful human confirmation is not seller verification.

## Scope

Finite synthetic recommendation, payment and minimum-data-disclosure records.
There is no browser, real seller investigation, payment integration, card data,
credential access or production deployment in these examples. The reference
checks externally supplied registry, grant and review records; it does not
authenticate those records or decide whether a real merchant is honest.

## Evidence and source limits

[Podqi's primary report](https://podqi.com/research/ai-search-brand-risk) describes
6,795 shopping answers about 151 brands across three engines in September 2026.
It reports risky domains in 9% of answers and recommendation versus warning at
6.3:1 when such domains appeared. Its risk category includes suspected fake shops
and inactive domains; these are not equivalent to confirmed fraud. This vendor
study concerns answer content, not executed purchases, stolen credentials or
measured prompt-injection success. Maintainers have not reproduced it.

Separately, [Chrome's agent-security guidance](https://developer.chrome.com/docs/agents/security)
describes malicious tool manifests and contaminated outputs, scoped origins,
data minimization and confirmation. This supports a distinct injection threat,
not an inference that Podqi observed theft. A supplier page can be wrong without
an injection, and a legitimate page can contain untrusted third-party text.

## Existing owners and gap assessment

| Function | Classification within this public repository | Existing owner / seam |
| --- | --- | --- |
| Source provenance, admission, expiry and conflicts | EXISTING_AND_WIRED in the normative/formal reference surface | MVP-005, KAI-REQ-001/002/003; Knowledge Admission Gate |
| Scope, egress, external enforcement and audit | EXISTING_AND_WIRED in the reference surface | MVP-003/004/006/007, ECI-REQ-002/003/004; Tool Authorization and External Side-Effect gates |
| Generic grounded effect | EXISTING_AND_WIRED in the formal reference | `assessGroundedProposal`, existing execution guards |
| Commerce-specific derivation from seller/order/review records | EXISTING_BUT_NOT_WIRED before this patch; adapter supplied here | Existing grounding seam; no new runtime gate or registry |
| Real seller identity, authorized distributor and processor/payee bindings | EXTERNAL_EVIDENCE_REQUIRED | Independent admitted source; never the store's own claim |
| Deployment integration, real reviewer identity and effect interception | EXTERNAL_EVIDENCE_REQUIRED | Adopter's existing enforcement owner; unassessed here |

The classification describes this public reference boundary only. It is not an
inspection of any private runtime. Frozen normative owners, requirements and
release manifests are unchanged. No new normative `MUST` is created by the news.

## Requirements or Guidance

The optional contract has six candidate predicates:

| Predicate | Candidate check | Failure outcome |
| --- | --- | --- |
| CMT-P01 | Independently admitted seller identity and exact storefront; no self-attestation | Hold verified recommendation/payment admission |
| CMT-P02 | Current, unexpired admission bound to the complete request and registry/grant revisions | Hold stale or reused admission |
| CMT-P03 | Exact destination and payee, authorized scope, currency and amount limit; HTTPS is necessary here but insufficient | Deny unauthorized or unadmitted destination |
| CMT-P04 | Human confirmation for exact payment/disclosure, with issue/expiry times and one remaining use | Hold until effective confirmation; changes require a new confirmation |
| CMT-P05 | Only authorized minimum data classes; raw cards, CVV, passwords, session cookies and payment secrets excluded even from broad grants | Prohibit export |
| CMT-P06 | External effect enforcement and attributable evidence; page text cannot create permission | Hold absent external enforcement |

Research and comparisons can proceed without a payment confirmation. An
unverified seller remains explicitly unverified and cannot become a verified
recommendation or checkout target by repetition, search ranking, branding or an
LLM confidence score. The useful recommendation control needs neither payment
permission nor human checkout review. Required review belongs at payment or
private-data disclosure, not every read or comparison.

An adopter should bind confirmation to seller, storefront, recipient, processor
endpoint, items/quantities, total including fees, currency, data classes and
request identity. Request/grant/registry revisions form the synthetic digest.
Changed amounts, redirects, recipients or scope invalidate prior approval.
Revalidate at the actual effect boundary; display the exact transaction through
a trusted review path outside page control. Confirmation cannot rescue a failed
seller or destination check. A payment processor different from the storefront
is allowed only through its independent admitted binding.

Keep secrets outside the model-visible browsing environment and use the existing
credential/effect broker for any authorized payment. A synthetic data-class label
does not prove that a runtime has removed secrets, filtered URLs/forms/logs or
prevented a browser/session bypass. Incident receipts should retain source URLs,
acquisition time, hashes, identity/payee bindings, grant/review revisions, proposed
effect, decision/reasons and reassessment triggers, with secrets redacted.

## Executable artifacts and interpretation

- [Reference admission and temporary effect marker](../examples/commerce_trust_reference.py).
- [Thirty authored vectors](../examples/commerce-trust-vectors.json) and
  [strict schema](../schemas/commerce-trust-vectors.schema.json).
- [Checker](../scripts/check_commerce_trust.py) and
  [regressions](../tests/test_commerce_trust.py).
- Existing [formal core](../formal/ai_hpp_core.qnt): `CommercePremises`,
  `commerceGrounding`, `assessCommerce` in normal `step`; 30 literal cases and
  three recovery/change/revocation traces feed existing grounding/effect guards.

Expected premises, reasons and effect outcomes are authored in the vectors,
not generated by the candidate decision function. Eight executed local operators
remove seller, freshness, destination, bound-review, one-use, data, scope or
external-enforcement checks. A mutant earns credit only when its same-input
unsafe execution produces the exact forbidden local marker. Malformed captures,
changed inputs, no-op mutations and blanket refusal cannot earn a passing score.

Run `python3 scripts/check_commerce_trust.py`, the regression suite and the pinned
formal commands in [the run guide](../formal/README.md). Keep the exact commit,
tool versions, vector digest, logs and verification bounds with any result.
Previous assessments exclude this optional suite and need a separate rerun to
make claims about it. No scores from other suites are combined.

## Abstraction and integration limits

The model's commerce premises are trusted inputs, not fraud or injection
detection. `assessCommerce` shares existing grounding state; legacy generic
admission can still be called. An actual integration must prevent a caller from
bypassing the commerce owner or overwriting a hold before an effect. No new
invariant, persistent state or implementation-refinement proof is claimed.

The reference consumes a one-use review in a returned local record; it does not
prove atomic consumption, concurrency safety, durable replay prevention or
exactly-once payment. Authentic review acquisition, signed trust records, domain
re-registration, DNS/TLS freshness, real-time races, processor redirects,
transaction settlement, refunds and supply-chain authenticity require external
tests. Page-content invariance demonstrates structured separation only; no LLM
was tested against a live prompt injection. The generic formal robot effect is
a symbolic effect witness, not a payment or physical execution.

Map `1.3.9` links the new scenarios to existing partially modeled properties.
There are 334 core/351 total Quint scenarios, 42 aggregate properties and 48
pre-existing Quint unsafe-transition witnesses; depth 12 and partial requirement
coverage remain unchanged. The eight local Python operators are a separate
denominator. This is reference evidence, not certification or deployed safety.
