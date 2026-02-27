# POST-MERGE OPERATOR CHECKLIST

> Moving files in Git does **not** remove prior history. Treat this as emergency cleanup + follow-up hardening.

## 1) Extract quarantine locally (secure storage)
1. Clone/fetch the merged branch in a secure environment.
2. Copy approved release artifacts to encrypted local storage.
3. Confirm integrity (hashes/checksum) of extracted content.

## 2) Remove quarantine from public repository
1. Create follow-up branch.
2. Verify no non-public material remains in the repository tree.
3. Update docs if any temporary quarantine links remain.
4. Merge and deploy.

## 3) Purge Git history (required)
Because historical commits may already contain sensitive content, run a history rewrite:

- Preferred: `git filter-repo`
- Alternative: BFG Repo-Cleaner

Example with `git filter-repo` (adapt to your policy):
```bash
git filter-repo --path internal --invert-paths
```
Then force-push rewritten refs and coordinate with all collaborators to re-clone.

## 4) Rotate potentially exposed secrets
1. Rotate API keys/tokens/certs that might have been present.
2. Invalidate old credentials.
3. Verify new credentials are not committed.
4. Audit external systems for suspicious access.

## 5) Re-tag and publish v0.3 release notes
1. Prepare release notes summarizing quarantine and safety hardening.
2. Create/refresh tag for public v0.3.
3. Note that history was purged and secrets rotated.
4. Link to `SECURITY.md` for reporting process.
