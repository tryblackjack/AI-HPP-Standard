# INDEX

## Canonical entrypoints
- `README.md`
- `BASELINE-v3.17.md`
- `INDEX.md`
- `GLOSSARY.md`
- `CHANGELOG.md`

## Public inspection surface
- `standard/` (normative requirements)
- `annex/` (normative supporting rationale and mappings)
- `schemas/` (machine-readable contracts)
- `validation/` (validation artifacts)
- `regulator-pack/` (inspection support package)
- `alignment/` (external crosswalks)
- `translations/` (translation set and metadata)
- `archive/` (historical references)
- `policies/` (implementer-facing policies)
- `annex/G-CONFLICT-ENVIRONMENT-SAFEGUARDS.md` (informative conflict-adjacent safeguards)
- `annex/H-ADAPTIVE-GOVERNANCE.md` (informative adaptive governance and deployment guidance)

Future additions to the core normative layer MUST include: threat reference (`T-*`), incident reference (`INC-*`), and measurable verification logic.

## Layering Model

AI-HPP distinguishes:

- Public Inspection Surface — normative and inspection-relevant artifacts.
- Internal Maintainer Layer — development history and governance materials.

Only artifacts under `standard/` and `annex/` define normative requirements.

## Internal maintainer layer
- `internal/` (non-normative maintainer documentation, audits, orchestration assets, and historical top-level materials)
- `internal/regulator-sim/` (internal regulator simulation pack)
