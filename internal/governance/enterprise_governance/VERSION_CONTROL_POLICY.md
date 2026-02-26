SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Version Control Policy (Corporate Layer)

## Branching

- `main` is protected and release-oriented.
- Feature branches MUST be short-lived and scoped to a single change objective.

## Commit Standards

- Commits MUST be atomic and reversible.
- Messages MUST describe intent and affected safety/governance surfaces.

## Release Tagging

- Semantic versioning is required for externally visible governance changes.
- Tags MUST reference changelog and review artifacts.

## Traceability

- Every merged PR MUST map to:
  - risk classification,
  - reviewer approvals,
  - validation evidence,
  - deployment decision.

## Prohibited Practices

- Force-push to protected branches.
- Unreviewed merges for behavior-changing updates.
- Retroactive edits to released tags.
