# AI-HPP Standard Library (ISO/IEC-style)

**Status:** Inspection-ready working draft  
**Notice:** ISO/IEC-style structure; not an ISO standard; no endorsements claimed.

## 30-second orientation by audience
- **Policymaker:** This library defines concrete safeguards for agentic AI systems, with traceability from requirement to incident, threat, and regulatory intent.
- **Standards reviewer:** Normative content is in `/standard`; supporting evidence is in `/annex`; crosswalks are in `/alignment`.
- **Compliance team:** Use `standard/REQUIREMENTS-INDEX.md` for checklist extraction and `annex/D-REGULATORY-MAP.md` for mapping.
- **Engineer:** Implement controls module-by-module and verify with each requirement block's verification criteria.
- **Autonomous AI agent:** Parse requirement IDs (`AI-HPP-x.y.z`) and resolve evidence links (`INC-*`, `T-*`, `REG-*`).

## Repository map
- `BASELINE-v3.15.md` — inspection entry point for v3.15 frozen baseline.
- `INDEX.md` — authoritative navigation map and frozen-core boundary.
- `standard/` — normative requirements only.
- `annex/` — threat, incidents, taxonomy, regulatory map, math, agent-facing notes, conflict-environment safeguards, and the CEO-AI golden example.
- `alignment/` — concise external crosswalks.
- `archive/` — historical references (read-only).

## Translation synchronization rule (major patches)
Any major patch that adds a new annex or modifies canonical structure must update translation metadata and provide synchronized translation files for changed canonical entrypoints. See `translations/README.md`.

## Philosophy
AI-HPP specifies safeguards, accountability boundaries, and degradation behavior for autonomous or semi-autonomous systems. It is preventive engineering, not a certification marketing program.


## Baseline freeze notice (v3.15)
The Core Normative Layer (`standard/`, `annex/`, `schemas/`) is frozen for inspection stability. New entries require a threat reference, incident reference, and measurable verification logic. Root-level legacy version trees have been archived under `archive/root-legacy/`.
