# Contributing

## Purpose

Contribution workflow for a public, draft AI safety standard.

## Baseline requirements

- Keep PR scope clear and reviewable.
- Update `CHANGELOG.md` for material changes.
- Preserve canonical terminology from `docs/GLOSSARY.md`.
- Keep immutable core principles unchanged.
- Human review required before merge.

## Translation review workflow

1. Add or update translated file under `translations/<lang>/`.
2. Include required disclaimer block (target language + English fallback).
3. Keep `# TODO: Native speaker verification needed` until reviewed.
4. Open PR with line-level notes for terms that need native validation.
5. After native review, update status in `translations/README.md`.

## Schema contribution rules

- Place schemas in `schemas/`.
- Target JSON Schema Draft 2020-12.
- Prefer backward-compatible updates:
  - Add optional fields instead of changing required fields.
  - Avoid breaking enum removals unless version bump is justified.
- Document schema purpose in `schemas/README.md`.

## Reference implementation rules

- Location: `reference/`.
- Language/runtime: Python 3.10+.
- Dependencies: stdlib + `jsonschema` + `pytest` only.
- Implementations must be local/stateless (no cloud/DB coupling).
- Include module README and tests for each implementation.
- Mark each implementation as reference-grade, not production mandate.

## Issue categories (use as templates)

- Translation error
- Schema bug
- Compliance question
- New proposal

When opening an issue, include affected file paths and expected behavior.
