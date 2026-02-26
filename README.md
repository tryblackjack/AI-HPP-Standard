# AI-HPP Standard Library (ISO/IEC-style)

**Status:** Inspection-ready working draft  
**Notice:** ISO/IEC-style structure; not an ISO standard; no endorsements claimed.

## 30-second orientation by audience
- **Policymaker:** This library defines concrete safeguards for agentic AI systems, with traceability from requirement to incident, threat, and regulatory intent.
- **Standards reviewer:** Normative content is in `standard/`; supporting evidence is in `annex/`; crosswalks are in `alignment/`.
- **Compliance team:** Use `standard/REQUIREMENTS-INDEX.md` for checklist extraction and `annex/D-REGULATORY-MAP.md` for mapping.
- **Engineer:** Implement controls module-by-module and verify with each requirement block's verification criteria.
- **Autonomous AI agent:** Parse requirement IDs (`AI-HPP-x.y.z`) and resolve evidence links (`INC-*`, `T-*`, `REG-*`).

## Repository Structure (Public Inspection Surface)

AI-HPP is structured in two layers:

### Public Inspection Baseline
- `BASELINE-v3.17.md` — inspection entry point
- `standard/` — normative engineering requirements
- `annex/` — threat model and incident registry
- `schemas/` — machine-verifiable logging schemas
- `validation/` — conformance and validation artifacts
- `regulator-pack/` — structured inspection materials
- `policies/` — implementer-facing enforcement policies
- `translations/` — language variants
- `archive/` — historical versions

### Internal Maintainer Layer
- `internal/` — non-normative maintainer artifacts (ADR, governance, audit reports, legacy stubs)

Canonical normative text exists only in `standard/` and `annex/`.
Internal materials do not override normative modules.

## Start here
1. `BASELINE-v3.17.md`
2. `standard/01-PRINCIPLES.md`
3. `annex/B-INCIDENTS.md`
4. `standard/REQUIREMENTS-INDEX.md`
5. `schemas/` and `validation/`

- CES safeguards are covered in `standard/07-PROPORTIONAL-RESPONSE.md`, `standard/12-EVIDENCE-VAULT.md`, and `annex/G-CONFLICT-ENVIRONMENT-SAFEGUARDS.md`.
- Adaptive governance guidance is available in `annex/H-ADAPTIVE-GOVERNANCE.md` (AGL + HSDF; informative only).

## Translation synchronization rule (major patches)
Any major patch that adds a new annex or modifies canonical structure must update translation metadata and provide synchronized translation files for changed canonical entrypoints. See `translations/README.md`.

## Vendor and Trademark Neutrality
AI-HPP is implementation-agnostic and does not reference proprietary systems in normative content. Public inspection materials use neutral terminology for the Autonomous System Implementation, including "Reference Autonomous System," "High-Risk Autonomous System," "Deployed AI System," and "Implementing Organization."

## Philosophy
AI-HPP specifies safeguards, accountability boundaries, and degradation behavior for autonomous or semi-autonomous systems. It is preventive engineering, not a certification marketing program.

## Baseline freeze notice (v3.17)
The Core Normative Layer (`standard/`, `annex/`, `schemas/`) remains inspection-stable. v3.17 adds CES safeguards through Module 07 and Module 12, with Annex G as informative guidance and no new modules added. New entries require a threat reference, incident reference, and measurable verification logic.
