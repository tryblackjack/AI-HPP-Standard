"""REFERENCE implementation; production may differ while maintaining compliance."""
from __future__ import annotations
import hashlib
import json
from datetime import datetime, timezone


def redact_record(record: dict, fields: list[str]) -> dict:
    out = dict(record)
    for field in fields:
        if field in out:
            out[field] = "[REDACTED]"
    return out


def generate_export(export_id: str, records: list[dict], redaction_fields: list[str]) -> dict:
    redacted = [redact_record(r, redaction_fields) for r in records]
    payload = {
        "export_id": export_id,
        "rir_profile": "RIR-v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "records": redacted,
        "redaction_policy": {
            "policy_id": "default-redaction",
            "rules": [f"redact:{x}" for x in redaction_fields],
        },
    }
    serialized = json.dumps(payload, sort_keys=True).encode("utf-8")
    payload["integrity"] = {
        "hash_algorithm": "sha256",
        "hash_value": hashlib.sha256(serialized).hexdigest(),
        "signature": "SIGNATURE_PLACEHOLDER",
    }
    return payload
