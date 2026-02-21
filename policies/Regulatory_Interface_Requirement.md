---
# Regulatory Interface Requirement (RIR)

**Type:** Normative (enforceable policy)  
**Applies to:** consumer AI products, image/video generators, platforms with user-generated prompts, high-risk deployments

## Purpose
Make AI systems “audit-ready” before regulators force emergency oversight. Provide a controlled evidence export path that preserves privacy while enabling accountability.

## Requirements

### Evidence export capability
1) Systems MUST implement an exportable **Evidence Bundle** for safety-relevant events and high-impact outputs:
   - timestamped request metadata,
   - safety policy decisions (allow/deny/approve),
   - tool calls and outcomes (if any),
   - model/agent identifiers and versions,
   - redacted content snapshots.

### Category telemetry (privacy-preserving)
2) Systems MUST maintain privacy-preserving telemetry on generation categories (e.g., image generation modes, sexual content flags, minor-risk classifiers):
   - aggregated counts,
   - trend detection,
   - anomaly alerts.
3) Telemetry MUST be stored in a way that supports audits without exposing personal data.

### Minor-risk escalation
4) If minor-risk patterns are detected (classifier flags, user reports, or anomaly spikes), the system MUST:
   - tighten safeguards,
   - rate-limit related generation modes,
   - require stronger verification or approvals for sensitive transformations,
   - generate an internal incident report (Evidence Bundle reference).

### Data retention & preservation holds
5) For active investigations or credible harm reports, systems MUST support a preservation hold:
   - keep relevant Evidence Bundles,
   - ensure tamper resistance,
   - document access events.

### Access control
6) Evidence export MUST be access-controlled:
   - least privilege,
   - auditable access logs,
   - redaction by default.

## Audit evidence checklist
- [ ] Evidence Bundle export exists
- [ ] category telemetry exists (aggregated, privacy-preserving)
- [ ] minor-risk escalation procedure exists
- [ ] preservation hold supported
- [ ] access control + audit logs in place
---
