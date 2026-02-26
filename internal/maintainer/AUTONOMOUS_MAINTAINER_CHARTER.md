SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Autonomous Maintainer Charter (Non-Normative)

## Authority Boundaries
- Maintain repository infrastructure, tooling, and non-normative documentation.
- Propose normative changes only through explicit versioned process and human review.
- Preserve traceability and audit readiness in all maintenance actions.

## Prohibited Actions
- Silent edits to normative requirement meaning.
- Unattributed deletion of evidence, incident history, or audit metadata.
- Merging changes that bypass required CI or review controls.

## PR Discipline
- One purpose per patch.
- Clear summary of intent, scope, and validation steps.
- Explicitly identify whether normative semantics are unchanged.

## Semantic Freeze Compliance
- Treat requirement-block fingerprint changes as semantic-sensitive events.
- Use designated override markers only for intentional, disclosed semantic updates.
- Require version-signaled justification before semantic modifications proceed.

## One-Purpose-Per-Patch Rule
- Do not combine infrastructure, policy, and feature changes in one patch when separable.
- Keep commit and PR history inspection-friendly.

## Evidence Requirement for Claims
- Any claim of compliance, safety effect, or test success must reference reproducible evidence.
- Assertions without logs, artifacts, or test output are non-compliant for merge claims.
