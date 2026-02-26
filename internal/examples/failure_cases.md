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

---
## Major consumer LLM multi-agent release — governance gap trigger (Feb 2026)

**System:** Consumer multi-agent assistant (public release)  
**Trigger:** Multi-agent “debate/consensus” used as a reliability claim in a consumer product.  
**Failure mode:** Governance gap — consensus may reduce errors but does not automatically provide authorization, auditability, or safety boundaries for tool use.  
**Impact:** Increased adoption pressure without standardized Evidence Bundles for high-impact outcomes.  
**AI-HPP mapping:**  
- **Module 11 — Multi-Agent Governance (MACR):** disagreement preservation, coordinator limits  
- **MACR policy:** no “agreement laundering”, blind-first pass  
- **TEB policy:** tool-call firewall and sandboxing in untrusted contexts  
**Mitigation:** Require Evidence Bundle export for high-impact actions and explicit approval gates regardless of consensus.

---

## Public regulatory review on AI sexualized deepfakes — compliance inquiry (Jan–Feb 2026)

**System:** Consumer image generation/editing features linked to a major platform  
**Trigger:** Public reports and analysis indicated large-scale generation of sexualized imagery, including content that may depict minors or non-consensual edits.  
**Failure mode:** Safety control limitations + inadequate proactive oversight signals; public oversight response included dedicated AI oversight mechanisms.  
**Impact:** Compliance inquiry, platform notices, and creation/expansion of AI oversight functions.  
**AI-HPP mapping:**  
- **RIR policy:** category telemetry, Evidence Bundle export, preservation holds  
- **Prohibited practices / vulnerable groups modules:** strict safeguards and escalation  
**Mitigation:** Default-deny for sensitive edits, strong minor-risk escalation, Evidence Bundle export, and tamper-resistant audit trails.

---
