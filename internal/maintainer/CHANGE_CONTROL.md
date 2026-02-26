# Change Control (Non-Normative)

## Version Bump Rules
- Patch: non-semantic corrections, tooling, documentation, or packaging updates.
- Minor: added requirements, annex structures, or materially expanded governance scope.
- Major: breaking normative semantics, removed requirements, or incompatible conformance expectations.

## Semantic Change Process
1. Declare intent and affected requirement IDs.
2. Include explicit semantic-change marker in commit or PR metadata.
3. Regenerate normative fingerprint and review diff.
4. Update changelog with rationale and impact statement.
5. Require human reviewer confirmation before merge.

## Required Testing Before Merge
- Run repository integrity checks.
- Run semantic fingerprint generation and ensure expected state.
- Validate changed schemas or scripts when applicable.
- Confirm no unintended edits in `standard/` and `annex/` for non-semantic patches.

## CI Compliance
- CI failures block merge until resolved.
- Override markers authorize intentional semantic drift only; they do not bypass failing tests.
- Merged changes must leave the default branch in a fully passing state.
