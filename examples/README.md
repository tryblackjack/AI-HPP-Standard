# Implementation Starter

Status: `ACTIVE_INFORMATIVE`. This guide reduces implementation effort but does
not add normative requirements and is not runtime conformance evidence.

AI-HPP is implementation-language neutral. It does not require Python, Node.js,
C, a shared runtime library, or a particular agent framework. Implementers own
their local code and map it to the stable requirement IDs, gate contracts,
evidence obligations, and expected fail-closed outcomes in the standard.

## Smallest useful adoption path

1. Declare the system boundary, deployment, AI-HPP version, assessment period,
   and applicable risk profile.
2. Map each of the seven MVP controls to an enforcement owner. Prompt-only or
   model-self-enforced controls do not satisfy controls that require external
   enforcement.
3. Implement a single auditable gate result shape and reuse it across policy,
   risk, tool, human-review, knowledge, reflexive-safety, and post-action gates.
4. Route tools, credentials, delegation, and external effects through controlled
   bridges.
5. Store attributable, integrity-protected evidence outside the acting agent's
   sole control.
6. Run the language-neutral
   [MVP negative test vectors](mvp-negative-test-vectors.json) and retain the
   resulting gate and evidence records.
7. Make only a scoped conformance statement containing the fields required by
   the [MVP conformance statement](../docs/ai-hpp-standard.md#mvp-conformance-statement).

## Conformance statement starter

Use the [MVP conformance statement template](mvp-conformance-statement.template.json)
with its [JSON Schema](../schemas/mvp-conformance-statement.schema.json). The
template defaults every control to `NOT_ASSESSED` and cannot claim conformance
until all seven mandatory controls pass with evidence and tests.

## Minimal gate result shape

This shape is illustrative. Field names may differ when the same semantics and
evidence remain reconstructable.

```json
{
  "requirement_id": "MVP-003",
  "gate": "Tool Authorization Gate",
  "decision": "block",
  "reason_code": "SCOPE_MISMATCH",
  "policy_version": "example-policy-v1",
  "actor": "example-agent",
  "timestamp": "RFC3339 timestamp",
  "evidence_refs": ["example-evidence-id"]
}
```

## Reuse contract

Implementers SHOULD reuse the normative requirement IDs and gate outcomes rather
than create a parallel requirement registry. Local types, functions, services,
and storage formats remain implementation choices.

The example vectors specify observable inputs and allowed or forbidden outcomes.
They deliberately do not prescribe internal model prompts, chain-of-thought,
framework classes, or programming-language APIs.

A passing example vector shows only that the tested path produced the expected
result. It does not establish complete integration, control effectiveness,
deployment-wide conformance, certification, or independent validation.
