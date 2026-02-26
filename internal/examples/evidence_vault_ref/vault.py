"""Minimal Evidence Vault reference implementation.

This module provides:
- append-only JSONL logging
- hash-chain linking (prev_hash -> entry_hash)
- Ed25519 signing and verification

Design goal: small, readable, and auditable.
"""
from __future__ import annotations

import base64
import dataclasses
import hashlib
import json
import os
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from nacl import signing


GENESIS_HASH = "0" * 64


@dataclass(frozen=True)
class Entry:
    entry_id: str
    ts_utc: str
    prev_hash: str
    payload: dict
    public_key_id: str
    entry_hash: str
    signature: str

    def to_dict(self) -> dict:
        return dataclasses.asdict(self)


@dataclass
class VerifyResult:
    ok: bool
    errors: List[str]
    warnings: List[str]
    entries: int


def canonical_json(obj: dict) -> str:
    """Return canonical JSON string for hashing.

    - sorted keys
    - minimal separators
    - UTF-8 preserved
    """
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def hash_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def key_id_from_public(public_key: bytes) -> str:
    """Short fingerprint for public key identification."""
    return hashlib.sha256(public_key).hexdigest()[:12]


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def generate_keypair(out_dir: Path) -> Tuple[Path, Path]:
    """Generate Ed25519 keypair, return (private_path, public_path)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    signing_key = signing.SigningKey.generate()
    verify_key = signing_key.verify_key

    private_payload = {
        "private_key_b64": base64.b64encode(signing_key.encode()).decode("ascii"),
        "public_key_id": key_id_from_public(verify_key.encode()),
    }
    public_payload = {
        "public_key_b64": base64.b64encode(verify_key.encode()).decode("ascii"),
        "public_key_id": private_payload["public_key_id"],
    }

    private_path = out_dir / "private_key.json"
    public_path = out_dir / "public_key.json"
    write_json(private_path, private_payload)
    write_json(public_path, public_payload)
    return private_path, public_path


def load_private_key(path: Path) -> Tuple[signing.SigningKey, str]:
    payload = read_json(path)
    private_key = base64.b64decode(payload["private_key_b64"])
    signing_key = signing.SigningKey(private_key)
    return signing_key, payload["public_key_id"]


def load_public_keys(path: Path) -> Dict[str, signing.VerifyKey]:
    """Load public keys from a file or directory of JSON key files."""
    keys: Dict[str, signing.VerifyKey] = {}
    if path.is_dir():
        for entry in sorted(path.glob("*.json")):
            payload = read_json(entry)
            if "public_key_b64" not in payload:
                continue
            verify_key = signing.VerifyKey(base64.b64decode(payload["public_key_b64"]))
            keys[payload["public_key_id"]] = verify_key
    else:
        payload = read_json(path)
        verify_key = signing.VerifyKey(base64.b64decode(payload["public_key_b64"]))
        keys[payload["public_key_id"]] = verify_key
    return keys


def build_entry_payload(
    payload: dict,
    prev_hash: str,
    public_key_id: str,
) -> dict:
    return {
        "entry_id": str(uuid.uuid4()),
        "ts_utc": datetime.now(timezone.utc).isoformat(),
        "prev_hash": prev_hash,
        "payload": payload,
        "public_key_id": public_key_id,
    }


def compute_entry_hash(entry_payload: dict) -> str:
    canonical = canonical_json(entry_payload)
    return hash_bytes(canonical.encode("utf-8"))


def sign_entry_hash(signing_key: signing.SigningKey, entry_hash: str) -> str:
    signature = signing_key.sign(entry_hash.encode("utf-8")).signature
    return base64.b64encode(signature).decode("ascii")


def append_entry(
    log_path: Path,
    payload: dict,
    signing_key: signing.SigningKey,
    public_key_id: str,
) -> Entry:
    """Append an entry to a JSONL log, returns the Entry object."""
    prev_hash = GENESIS_HASH
    if log_path.exists():
        with log_path.open("r", encoding="utf-8") as handle:
            for line in handle:
                if line.strip():
                    prev_hash = json.loads(line)["entry_hash"]

    entry_payload = build_entry_payload(payload, prev_hash, public_key_id)
    entry_hash = compute_entry_hash(entry_payload)
    signature = sign_entry_hash(signing_key, entry_hash)

    entry = Entry(
        entry_id=entry_payload["entry_id"],
        ts_utc=entry_payload["ts_utc"],
        prev_hash=prev_hash,
        payload=payload,
        public_key_id=public_key_id,
        entry_hash=entry_hash,
        signature=signature,
    )

    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry.to_dict(), ensure_ascii=False) + "\n")

    return entry


def iter_entries(log_path: Path) -> Iterable[Entry]:
    with log_path.open("r", encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            payload = json.loads(line)
            yield Entry(**payload)


def verify_log(log_path: Path, public_keys: Dict[str, signing.VerifyKey]) -> VerifyResult:
    """Verify hash chain, signatures, and best-effort timestamp monotonicity."""
    errors: List[str] = []
    warnings: List[str] = []
    prev_hash = GENESIS_HASH
    last_ts: Optional[datetime] = None
    count = 0

    for index, entry in enumerate(iter_entries(log_path), start=1):
        count += 1
        expected_payload = {
            "entry_id": entry.entry_id,
            "ts_utc": entry.ts_utc,
            "prev_hash": entry.prev_hash,
            "payload": entry.payload,
            "public_key_id": entry.public_key_id,
        }
        expected_hash = compute_entry_hash(expected_payload)
        if entry.entry_hash != expected_hash:
            errors.append(f"entry {index}: entry_hash mismatch")

        if entry.prev_hash != prev_hash:
            errors.append(f"entry {index}: prev_hash mismatch")
        prev_hash = entry.entry_hash

        verify_key = public_keys.get(entry.public_key_id)
        if not verify_key:
            errors.append(f"entry {index}: unknown public_key_id {entry.public_key_id}")
        else:
            try:
                signature = base64.b64decode(entry.signature)
                verify_key.verify(entry.entry_hash.encode("utf-8"), signature)
            except Exception:
                errors.append(f"entry {index}: signature verification failed")

        try:
            current_ts = datetime.fromisoformat(entry.ts_utc)
            if last_ts and current_ts < last_ts:
                warnings.append(f"entry {index}: timestamp moved backwards")
            last_ts = current_ts
        except ValueError:
            warnings.append(f"entry {index}: invalid ts_utc format")

    ok = not errors
    return VerifyResult(ok=ok, errors=errors, warnings=warnings, entries=count)


def slice_log(
    log_path: Path,
    start_line: Optional[int],
    end_line: Optional[int],
) -> List[str]:
    """Return selected JSONL lines (1-indexed inclusive)."""
    lines = log_path.read_text(encoding="utf-8").splitlines()
    if not lines:
        return []
    start = 1 if start_line is None else max(1, start_line)
    end = len(lines) if end_line is None else min(len(lines), end_line)
    return lines[start - 1 : end]


def export_bundle(
    log_path: Path,
    out_dir: Path,
    start_line: Optional[int],
    end_line: Optional[int],
    public_keys: Dict[str, signing.VerifyKey],
) -> None:
    """Export subset log + verification report + public keys used."""
    out_dir.mkdir(parents=True, exist_ok=True)
    subset_lines = slice_log(log_path, start_line, end_line)
    subset_path = out_dir / "vault_subset.jsonl"
    subset_path.write_text("\n".join(subset_lines) + ("\n" if subset_lines else ""), encoding="utf-8")

    if subset_lines:
        temp_path = out_dir / "_subset_tmp.jsonl"
        temp_path.write_text("\n".join(subset_lines) + "\n", encoding="utf-8")
        result = verify_log(temp_path, public_keys)
        temp_path.unlink()
    else:
        result = VerifyResult(ok=True, errors=[], warnings=["subset is empty"], entries=0)

    report = {
        "ok": result.ok,
        "entries": result.entries,
        "errors": result.errors,
        "warnings": result.warnings,
    }
    write_json(out_dir / "verification_report.json", report)

    used_ids = set()
    for line in subset_lines:
        payload = json.loads(line)
        used_ids.add(payload.get("public_key_id"))

    pubkeys_payload = []
    for key_id in sorted(used_ids):
        verify_key = public_keys.get(key_id)
        if not verify_key:
            continue
        pubkeys_payload.append(
            {
                "public_key_id": key_id,
                "public_key_b64": base64.b64encode(verify_key.encode()).decode("ascii"),
            }
        )
    write_json(out_dir / "public_keys.json", {"keys": pubkeys_payload})


def ensure_log_exists(log_path: Path) -> None:
    if not log_path.exists():
        log_path.parent.mkdir(parents=True, exist_ok=True)
        log_path.write_text("", encoding="utf-8")


def load_payload(event: str, data_path: Optional[Path]) -> dict:
    payload = {"event": event}
    if data_path:
        payload["data"] = read_json(data_path)
    return payload
