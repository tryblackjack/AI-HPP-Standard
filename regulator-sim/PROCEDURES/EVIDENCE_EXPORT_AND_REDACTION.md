# Procedure: Evidence Export and Redaction

## Export rules

- Export only synthetic or public-safe records.
- Preserve immutable timestamps and record hashes where available.
- Include schema version and export operator ID.

## Redaction rules

- Remove secrets, tokens, and user identifiers.
- Replace environment-specific hostnames and paths with placeholders.
- Mark each redaction with reason code: `privacy`, `security`, or `legal`.

## Verification checklist

- JSON structure valid.
- Required keys present.
- No sensitive literal values.
- Traceability preserved using stable synthetic IDs.
