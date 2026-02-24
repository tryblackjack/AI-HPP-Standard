# Annex A — Threat Model

### T-001 Prompt injection via untrusted channels
- **Definition:** Malicious content attempts to override policy through prompt context.
- **Triggers:** External web/email text, embedded instructions, cross-agent payloads.
- **Mitigations:** 03-ZERO-TRUST, 08-ADVERSARIAL-ROBUSTNESS.
- **Linked incidents:** INC-001, INC-008.

### T-002 Tool abuse with destructive side effects
- **Definition:** Agent executes destructive or irreversible commands without bounded authorization.
- **Triggers:** Broad tool permissions, missing impact classification, weak approval gates.
- **Mitigations:** 05-TOOL-EXECUTION, 09-GRACEFUL-DEGRADATION.
- **Linked incidents:** INC-001, INC-002, INC-004.

### T-006 Evidence tampering or missing accountability chain
- **Definition:** Decision records are altered, deleted, or insufficient for reconstruction.
- **Triggers:** Mutable logging, weak retention policies, missing signatures.
- **Mitigations:** 04-DATA-PROVENANCE, 12-EVIDENCE-VAULT.
- **Linked incidents:** INC-001, INC-007.

### T-007 Vulnerable-person exploitation risk
- **Definition:** Unsafe interaction with minors or vulnerable users causes direct harm.
- **Triggers:** Missing refusal boundaries, identity ambiguity, absent escalation paths.
- **Mitigations:** 06-VULNERABLE-GROUPS, 07-PROPORTIONAL-RESPONSE.
- **Linked incidents:** INC-007.

### T-008 Disproportionate response control failure
- **Definition:** System applies weak controls to high-impact actions or excessive controls to low-risk actions.
- **Triggers:** Flat policy models, missing impact tiers.
- **Mitigations:** 07-PROPORTIONAL-RESPONSE.
- **Linked incidents:** INC-002.

### T-009 Multi-agent coordination drift
- **Definition:** Spawned agents exceed assigned scope or lose governance lineage.
- **Triggers:** Unbounded delegation, missing chain-of-responsibility metadata.
- **Mitigations:** 11-MULTI-AGENT, 12-EVIDENCE-VAULT.
- **Linked incidents:** INC-003.

### T-010 Unmanaged degradation and outage amplification
- **Definition:** Safety thresholds fail without controlled autonomy reduction.
- **Triggers:** No degradation ladder, no rollback checkpoints.
- **Mitigations:** 09-GRACEFUL-DEGRADATION.
- **Linked incidents:** INC-002, INC-004.

### T-011 Cross-jurisdiction policy collision
- **Definition:** Conflicting legal requirements create unresolved runtime behavior.
- **Triggers:** Multi-country deployment with static single-policy assumptions.
- **Mitigations:** 10-MULTI-JURISDICTION.
- **Linked incidents:** INC-007.
