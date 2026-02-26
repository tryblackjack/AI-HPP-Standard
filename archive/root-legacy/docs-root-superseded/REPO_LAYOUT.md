# Repo Layout & Content Rules

Goal: keep the repository usable for both humans and AI agents.

## Golden rules
1) Keep root clean: only entrypoints and governance docs.
2) Anything normative (must/shall) goes to `policies/` or version standards.
3) Anything descriptive (why/how/analysis) goes to `docs/` or `whitepapers/`.
4) Examples, templates, schemas go to `examples/`.

## Naming
- Use `Title_Case_With_Underscores.md`
- Prefer stable file names (avoid renaming once referenced).

## Adding new security boundaries (policy)
Add a new file to `policies/` with:
- Purpose
- Scope
- Requirements (MUST/SHALL)
- Non-goals
- Audit evidence checklist

## Adding a failure case
Append to `examples/failure_cases.md`:
- Date / system / impact
- Trigger
- Failure mode (taxonomy tags)
- Mitigation mapping (which module/policy would have stopped it)
