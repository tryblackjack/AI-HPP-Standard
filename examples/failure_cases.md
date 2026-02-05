# Failure Cases (Non-Normative)

Short, failure-first cases that map to existing AI-HPP controls. These do not add new requirements.

## Moltbook identity hijack (Feb 2026)
- Misconfigured Supabase policy exposed a shared service token.
- Agents accepted actions signed with the leaked credential.
- Attribution collapsed; audit logs could not prove which agent acted.
- Impact included unauthorized actions and loss of owner accountability.
- Controls: per-identity signing, key rotation, Evidence Vault identity events, HITL for high-risk actions.

## ClawTasks agent marketplace (Feb 2026)
- Agents executed paid tasks in a USDC marketplace with deposits and escrow.
- Some tasks were paid without explicit human approval.
- Dispute handling lacked accountable human authority.
- Marketplace routing created hidden incentives and fee opacity.
- Controls: Evidence Vault logging for all financial actions, approval thresholds, zero-trust verification.

## AI companion dependency (Observed pattern)
- Long-running “companion” sessions reinforced user dependency.
- Escalation to human help was delayed or absent.
- No audit trail existed for influence patterns or de-escalation attempts.
- Controls: cognitive safety triggers, engagement de-escalation, Evidence Vault profiles for prolonged influence.
