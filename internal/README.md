# Internal Maintainer Layer

This directory contains non-normative maintainer materials used to operate, audit, and evolve the repository. These files support implementation and governance work but are not part of the normative inspection baseline.

## Contents

### `meta-audits/`
Repository audit and health reports previously stored at the root. These reports are maintained for traceability and historical review.

### `adr/`
Architecture Decision Records documenting maintainer decisions and rationale.

### `governance/`
Governance support materials, including decision-integrity artifacts, enterprise-governance references, and compliance-oriented governance files.

### `registry/`
Maintainer registries and internal index artifacts used for tracking and repository operations.

### `orchestrators/`
Reference orchestrator assets and interfaces used for internal tooling and implementation support.

### `agent/` and `agent_safety/`
Maintainer-oriented agent operation and safety materials.

### `examples/`
Implementation examples not required in the root public inspection surface.

### `legacy-top/`
Previously top-level directories retained without deletion for continuity and historical path preservation.

## Normative precedence
Internal documentation is non-normative and must not override the canonical normative content in `standard/` and `annex/`.

For inspection entrypoints, use `BASELINE-v3.16.md`, `INDEX.md`, `standard/`, and `annex/`.
