# PR Review Discipline (Corporate Layer)

## Review Objectives

- Preserve constitutional safety boundaries.
- Ensure attribution and auditability are not degraded.
- Prevent hidden scope expansion in behavior changes.

## Review Checklist

1. Scope is explicit and minimal.
2. Safety/refusal logic impacts are identified.
3. Audit logging coverage is verified.
4. Backward compatibility and rollback are documented.
5. Required approvers signed off by risk level.

## Blocking Conditions

- Missing test evidence for behavior-changing updates.
- Incomplete risk classification.
- Ambiguous ownership for post-merge monitoring.

## Merge Discipline

- Squash merge with clear changelog fragment.
- Link decision rationale in PR body.
- Confirm deployment gate status before release.
