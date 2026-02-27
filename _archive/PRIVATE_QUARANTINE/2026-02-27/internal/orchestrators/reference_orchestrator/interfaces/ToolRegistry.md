SAFE_FOR_PUBLIC_REPO: YES
NO PRODUCTION DATA. NO SECRETS. NO CUSTOMER INFO.

# Interface: ToolRegistry

## Purpose
Provide a catalog of tools and their declared capability manifests.

## Tool manifest (minimum)
- tool_id
- trust_tier: {core, verified, untrusted}
- capabilities:
  - fs: {read_scope, write_scope}
  - exec: {allowed, environment: host|sandbox}
  - net: {allowed_domains}
  - secrets: {allowed_keys}
- version / digest (pinning)
