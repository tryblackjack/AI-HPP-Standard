# Start Here — AI-HPP Standard

This repository contains the AI-HPP standard plus supporting modules, conformance guidance, schemas, and reference material.

## Canonical reading path (recommended)
1) **v3 (current canonical standard)**  
   Start with: `v3/` (and its entry index if present)

2) **Failure taxonomy + rationale**  
   - `Failure_Taxonomy.md`  
   - `RATIONALE.md`

3) **Key modules (pick what applies to your system)**
- **Autonomous Drift Risk (ADR)**: `adr/`  
- Decision integrity & governance: `decision_integrity/`  
- Enterprise governance: `enterprise_governance/`  
- Conformance & profiles: `conformance/`

## Repository map (high level)
- **Core / Standard**: `v3/`, root docs (README/INDEX), taxonomy & rationale
- **Modules**: topic-specific safeguards (e.g., `adr/`, `decision_integrity/`)
- **Conformance & Schemas**: `conformance/`, `schemas/`, `registry/`, `policies/`
- **Examples & Reference**: `examples/`, `reference/`, `reference_orchestrator/`
- **Legacy**: `v2/`
- **Internal / Tooling**: `internal/`, `scripts/`, `.github/`

## If you are implementing controls
- Start with the relevant module checklist (e.g., `adr/CHECKLIST.md`)
- Ensure safeguards are enforced at the **execution boundary** (policy gate/tool proxy/supervisor), not by model compliance alone.
