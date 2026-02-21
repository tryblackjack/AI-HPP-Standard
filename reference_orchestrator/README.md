# reference_orchestrator (Reference Skeleton)

This folder contains a **reference implementation skeleton** aligned with AI-HPP.
It is intentionally **non-operational** (no production integrations, no secrets).
Purpose: provide stable interfaces and data formats so a hardened/closed implementation can be built later.

## Components (conceptual)
- Input Gateway (untrusted channels)
- Policy Engine (fail-closed)
- Tool Registry + Tool Firewall
- Evidence Vault (Evidence Bundle export)
- HITL / Approvals (dual control for high-impact actions)
- Session Isolation

## What is included
- Interface contracts (stubs)
- Evidence Bundle schema + example
- Compliance checklists for audits

## What is NOT included
- Production credentials, endpoints, or vendor secrets
- Real corporate integrations (email/CRM/payments/deploy pipelines)
- Any bypassable “demo mode” safety shortcuts
