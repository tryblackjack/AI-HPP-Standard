# Control Plane Exposure Policy (CPEP)

**Type:** Normative (enforceable policy)
**Applies to:** agent gateways, admin panels, orchestration dashboards, API control planes

## Purpose
Prevent takeover via exposed admin surfaces and misconfigured endpoints.

## Requirements

### Loopback-only default
Control plane services MUST bind to loopback by default (localhost).

### No public exposure
Public internet exposure is PROHIBITED unless:
- explicitly enabled,
- protected by strong authentication (MFA),
- short-lived tokens are used,
- network access is restricted (VPN/Tailscale/allowlisted IPs),
- audited and logged.

### Secrets hygiene
- No secrets in plaintext config files in repo/workspace.
- Secrets must be stored in OS keychain / vault / HSM equivalents.
- Logs must redact tokens and credentials.

## Audit evidence checklist
- [ ] loopback-only default
- [ ] public exposure requires explicit opt-in + MFA
- [ ] restricted network access path
- [ ] secrets never stored in plaintext in workspace
- [ ] redaction in logs
