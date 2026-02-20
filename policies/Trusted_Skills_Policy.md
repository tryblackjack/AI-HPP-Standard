# Trusted Skills Policy (TSP)

**Type:** Normative (enforceable policy)
**Applies to:** agent ecosystems, tool registries, skill marketplaces, plugin systems

## Purpose
Prevent supply-chain compromise and capability escalation via untrusted skills/plugins.

## Scope
Any component that can:
- execute code or tool calls,
- read/write files,
- access network,
- access secrets,
- modify system configuration.

## Requirements

### Trust tiers
Implementations MUST classify every skill into one of:
1) **core** — shipped with the system, audited.
2) **verified** — externally sourced but approved, pinned, and reviewable.
3) **untrusted** — everything else.

### Default deny
- **untrusted** skills MUST NOT execute by default.
- Any attempt to use an untrusted skill MUST hard-fail (fail-closed) and be logged.

### Pinning and integrity
For **verified** skills:
- MUST be pinned by immutable identifier (hash / signed artifact).
- MUST record provenance: source, version, digest, approver identity.
- MUST block on drift: if digest changes → disable until re-approval.

### Capability manifest
Every **core** and **verified** skill MUST declare a capability manifest (minimum):
- fs: read/write scope (workspace-only vs broader)
- exec: allowed or not (and where: host vs sandbox)
- net: allowlist domains (or none)
- secrets: none / read-only / specific keys

### Audit trail
Implementations MUST log:
- skill id + digest
- capability manifest
- who approved
- when enabled/disabled
- every privileged action derived from the skill

## Non-goals
- This document does not prescribe a specific signing technology.

## Audit evidence checklist
- [ ] registry has trust tiers
- [ ] default deny for untrusted
- [ ] pinning by digest/signature
- [ ] drift detection
- [ ] capability manifests enforced
- [ ] auditable logs exist and are protected
