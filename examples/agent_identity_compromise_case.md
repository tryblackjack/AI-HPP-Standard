# Example: Agent Identity Compromise (Non-Normative)

**Observed failure mode (generic class):**
A service token or shared credential is exposed through a misconfigured backend
(e.g., a database or logging service). Multiple agents then accept actions signed
with that credential, causing impersonation and loss of attribution.

**Impact:**
- Audit trails cannot reliably identify which agent issued actions.
- High-risk actions may be executed without accountable ownership.
- Forensic review cannot distinguish between valid and impersonated actions.

**AI-HPP Control Mapping:**
- Require per-identity signing keys and verify signatures at each hop.
- Rotate keys and maintain revocation lists with owner authority.
- Log identity events and key changes in the Evidence Vault.
- Escalate to a human owner when verification fails or high-risk actions occur.

**Operational note:**
Treat agent-to-agent inputs as untrusted by default. Do not propagate unverified
agent outputs without independent verification.
