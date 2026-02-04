from pathlib import Path
import sys

import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(PROJECT_ROOT))

from examples.evidence_vault_ref import vault


def write_keypair(tmp_path: Path) -> Path:
    vault.generate_keypair(tmp_path)
    return tmp_path / "private_key.json"


def test_hash_chain_verification_passes(tmp_path: Path) -> None:
    log_path = tmp_path / "vault.jsonl"
    key_path = write_keypair(tmp_path)
    signing_key, public_key_id = vault.load_private_key(key_path)

    vault.append_entry(log_path, {"event": "alpha"}, signing_key, public_key_id)
    vault.append_entry(log_path, {"event": "beta"}, signing_key, public_key_id)

    public_keys = vault.load_public_keys(tmp_path / "public_key.json")
    result = vault.verify_log(log_path, public_keys)

    assert result.ok
    assert result.entries == 2
    assert result.errors == []


def test_hash_chain_verification_detects_tamper(tmp_path: Path) -> None:
    log_path = tmp_path / "vault.jsonl"
    key_path = write_keypair(tmp_path)
    signing_key, public_key_id = vault.load_private_key(key_path)

    vault.append_entry(log_path, {"event": "alpha"}, signing_key, public_key_id)
    vault.append_entry(log_path, {"event": "beta"}, signing_key, public_key_id)

    lines = log_path.read_text(encoding="utf-8").splitlines()
    tampered = lines[1].replace("beta", "gamma")
    log_path.write_text("\n".join([lines[0], tampered]) + "\n", encoding="utf-8")

    public_keys = vault.load_public_keys(tmp_path / "public_key.json")
    result = vault.verify_log(log_path, public_keys)

    assert not result.ok
    assert any("entry_hash mismatch" in err for err in result.errors)
