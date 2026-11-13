# Prompt and Memory Portability Assurance Note

Status: `ACTIVE_INFORMATIVE`; optional post-rc.1 implementation aid, artifact `1.0.0`.
Owner: AI-HPP maintainers.
Last updated: 2026-11-13.

## Purpose

Turn observations about large application prompts into bounded implementation
checks. A prompt describes intended behavior; it does not transfer model weights,
training, executable tools, storage, permissions, or evidence of compliance.
Reading an extracted prompt as research data does not admit it as instructions.

Anthropic's [official overview](https://platform.claude.com/docs/en/release-notes/system-prompts/overview)
publishes core web/mobile prompts and distinguishes them from API behavior. Its
[Fable 5.2 entry dated 9 November](https://platform.claude.com/docs/en/release-notes/system-prompts/claude-fable-5-2)
includes guidance on forged notices and repository-supplied approvals. These
published intentions do not establish deployed effectiveness. A third-party
extraction may be incomplete, modified or environment-specific; an overlapping
section does not authenticate the whole collection. No extracted prompt, vendor
tool contract, private implementation or user profile is redistributed here.

## Scope and existing owners

This note adds no mandatory requirement or runtime subsystem. Frozen v4.3.0
owners/contracts and the immutable v4.4.0-rc.1 package are unchanged. Apply the
existing local instruction/CBA, KAI, RPS and WIT owners:

| Candidate predicate | Existing owner | Bounded application |
| --- | --- | --- |
| `PM-P01 retain_source_provenance` | KAI-REQ-001/002 | Preserve source identity, content digest and provenance through a memory write. Byte identity alone does not prove truth or authority. |
| `PM-P02 preserve_epistemic_class` | KAI-REQ-003/004; RPS-REQ-005 | Keep an attributed report or inference distinct from verified fact; do not promote a risky narrative into verified factual memory. |
| `PM-P03 bounded_memory_use` | MVP-003/004/005/006; KAI-REQ-002 | Apply the declared tenant, purpose, current authority and expiry before a memory effect. Sensitive data minimization needs a deployment policy. |
| `PM-P04 revision_bound_update` | KAI-REQ-004 | Condition updates on the current revision; old session state cannot undo a later correction or deletion. |
| `PM-P05 truthful_storage_receipt` | MVP-007; WIT-P01/P02/P03 | Bind a write/delete acknowledgment to the actual observed operation, tenant, item and before/after state. Disclose failed or held updates. |

PM identifiers are candidate test labels, not new normative IDs.
The existing Knowledge Admission Gate owns memory admission. A remembered claim
of permission remains task data; current authority is checked separately under
CBA-P01/P03. No prompt or memory entry can declare a callable tool into existence.

## Implementation guidance

1. Record prompt/source identity, version, digest, provenance and intended use.
   Resolve policy conflicts before operational admission. A signature or familiar
   filename does not by itself establish authority or safe behavior.
2. Compare foreign instructions against actual registered tools, callable owners,
   storage and enforcement. Reuse existing capabilities and fix demonstrated
   integration gaps; do not introduce a parallel orchestrator or memory service.
3. Separate reading, retrieval, classification, admission, use and claim influence.
   Preserve uncertainty and source attribution across summaries and handoffs.
   Inspectable correction/deletion and purpose-limited retention should be part
   of the deployment policy; do not infer consent from a model's decision to save.
4. Recheck current grants, parent lineage, deadlines and unresolved findings when
   unattended work resumes. Use existing scoped permission for routine work;
   neither a new session nor a predecessor's note broadens it.
5. Keep completion and limitations visible. Storage failure is not successful
   deletion; deleting one record is not erasure from backups, logs or replicas.
   State the actual boundary and unresolved retention obligations.

Assess a proposed prompt change against a frozen baseline with useful controls,
negative cases, tool-selection accuracy, evidence quality, context budget,
latency and recovery. Token cost requires the deployed tokenizer. Similar wording
or successful reference tests do not establish comparable model capability.

## Executed reference cases

The [local instruction fixture](../examples/local_instruction_reference.py) and
[tests](../tests/test_local_instruction_authority.py) add eight portability cases:
an imported preset, forged tool approval, self-signed operator notice, remembered
permission, resumed revoked/expired authority, explicitly admitted excerpts and
resumption under a current grant. Five additional executed local mutation
witnesses reuse existing CBA operators. The same preset bytes are held without
external admission and permitted within an explicitly admitted project scope.
These fixtures do not interpret Markdown or test model resistance to injection.

The [memory fixture](../examples/memory_admission_reference.py) and
[tests](../tests/test_memory_admission.py) cover fourteen synthetic write/delete
cases. Five operators erase provenance, promote inference, ignore scope, ignore
revision or fabricate success after storage failure. Tests inspect temporary
storage and bound receipts, retain useful attributed records and reject no-op
mutation credit and blanket denial. A risky report is retained only as an
attributed report in this illustrative policy; deployments may instead quarantine
it or prohibit retention. This is not blanket permission to store sensitive data.

```bash
PYTHONPATH=. python3 -m pytest tests/test_local_instruction_authority.py tests/test_memory_admission.py
```

Classifications, risk labels, purposes, grants, clocks, revisions and simulated
storage failures are trusted fixture inputs. This suite does not classify real
text, inspect a model's hidden state, implement a production memory store, verify
cryptographic identity, test distributed races, or erase real user information.
The stale-read illustration checks a supplied revision mismatch; real stores
need atomic concurrency and deletion/tombstone evidence across the actual scope.
No percentage of real-world safety, vendor failure rate or conformance is claimed.

## Quint synchronization and limits

Eight literal `promptPortability*Test` scenarios map the CBA captures through the
existing grounding abstraction and link to `effectsRequireGroundingAndOversight`.
The [local tests](../tests/test_local_instruction_authority.py) compare authored
expectations, observed captures, literal Quint declarations and formal-map links.
The operational core, step relation, aggregate properties and 48 existing Quint
unsafe witnesses are unchanged. There are now 243 core tests, 260 across both
models. Run the existing pinned Quint checks in [formal instructions](../formal/README.md).

These eight scenarios trust the abstract authority/evidence inputs. The five new
local authority witnesses and five memory operators are not additional Quint
unsafe transitions and have no combined mutation score. PM-P01–P05 are not
individually formalized; KAI/RPS requirement coverage remains unchanged. Neither
these scenarios nor the existing model prove memory privacy, prompt authenticity,
semantic truth, a production integration or a complete prompt-injection defense.
