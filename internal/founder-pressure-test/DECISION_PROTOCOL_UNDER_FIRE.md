SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Decision Protocol Under Fire (Internal)

Use this one-page sequence when pressure is high and decision quality is at risk.

## Step 0 — Stabilize
- Timebox the decision window.
- Reduce active autonomy to conservative/safe mode.
- If escalation timeout conditions are active, enforce safe-state behavior before any irreversible action.

## Step 1 — Evidence first
- Export a minimum package immediately (do not wait for perfect completeness).
- Do not “log everything”; log what is required and sufficient with minimization.
- Preserve integrity markers and ordering for later audit reconstruction.

## Step 2 — Classify
- Run incident intake triage using: `internal/maintainer/INCIDENT_INTAKE_PROTOCOL.md`.
- Classify severity, domain risk, and immediate containment needs.
- Mark whether governance-trigger conditions are met (override frequency, unresolved drift, repeated timeout paths).

## Step 3 — Decide
- Select only approved options within current governance boundaries.
- Record why rejected options were rejected.
- If requested action implies autonomy/tool-scope expansion, stop and route to formal governance review first.

## Step 4 — After-action
- Trigger governance review when thresholds are met.
- Land remediation through controlled PRs under: `internal/maintainer/CHANGE_CONTROL.md`.
- Preserve original evidence; append corrections with provenance.

## Hard constraints
- No bypass of semantic freeze.
- No unsanctioned authority or runtime scope expansion.
- No suppression, alteration, or retroactive rewriting of evidence.
