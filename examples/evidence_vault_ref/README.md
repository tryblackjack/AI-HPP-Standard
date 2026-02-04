# Evidence Vault Reference (Minimal)

This folder contains a minimal, readable reference implementation of an **Evidence Vault** logger.
It is intentionally small, auditable, and designed for local filesystem use only.

## What This Implements

- **Append-only JSONL log** (`vault.jsonl`)
- **Hash-chain linking** (`prev_hash` → `entry_hash`)
- **Ed25519 signatures** (per entry)
- **CLI** to write entries, verify integrity, and export proof bundles

## Quick Start

> The CLI name below is shown as `vault` for clarity. If you are running from source,
> use `python -m examples.evidence_vault_ref.cli` or add a shell alias.

```bash
# install dependency
pip install -r examples/evidence_vault_ref/requirements.txt

# generate keys
python -m examples.evidence_vault_ref.cli keygen --out ./keys/

# append entry
python -m examples.evidence_vault_ref.cli append --log vault.jsonl --event "decision:approve" --data ./payload.json

# verify chain and signatures
python -m examples.evidence_vault_ref.cli verify --log vault.jsonl --pubkeys ./keys/

# export proof bundle (lines 1..10)
python -m examples.evidence_vault_ref.cli export --log vault.jsonl --from 1 --to 10 --out bundle/ --pubkeys ./keys/
```

## Log Format (JSONL)

Each line is a single JSON entry:

```json
{
  "entry_id": "uuid4",
  "ts_utc": "2026-01-01T00:00:00+00:00",
  "prev_hash": "<hex>",
  "entry_hash": "<hex>",
  "payload": {"event": "...", "data": {"...": "..."}},
  "signature": "<base64>",
  "public_key_id": "<fingerprint>"
}
```

## Key Files

- `private_key.json` contains the Ed25519 private key (base64) and `public_key_id`.
- `public_key.json` contains the Ed25519 public key (base64) and `public_key_id`.

## Security / Design Notes

- **Append-only is logical, not physical.** This reference uses the local filesystem.
  A privileged actor can still rewrite or delete the log. Treat this as a minimal
  local mechanism, not a tamper-proof ledger.
- **Hash chaining:** Each entry includes `prev_hash`, creating a verifiable sequence.
- **Canonical JSON hashing:** `entry_hash` is computed as `SHA-256(canonical_json(entry_payload))`
  where `entry_payload` includes `entry_id`, `ts_utc`, `prev_hash`, `payload`, and `public_key_id`.
  The `signature` and `entry_hash` are excluded from the hash preimage.
- **Signing:** The Ed25519 signature is computed over the `entry_hash` bytes.
- **Future hardening:** For stronger auditability, add an external witness node or
  periodic hash anchoring (e.g., write a digest to an independent system).

## Tests

```bash
pytest examples/evidence_vault_ref/tests/test_vault.py
```

## Limitations

- This is a **reference implementation**, not production-hardened code.
- Key management is local and intentionally simple.
- No rotation or revocation logic is included.
