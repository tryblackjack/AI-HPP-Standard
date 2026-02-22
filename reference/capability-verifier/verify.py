"""REFERENCE implementation; production may differ while maintaining compliance."""
from __future__ import annotations
import json
import sys
from pathlib import Path

try:
    from jsonschema import validate as jsonschema_validate
except Exception:  # fallback for offline environments
    jsonschema_validate = None


def _fallback_validate(manifest: dict) -> None:
    required = ["system_id", "version", "declared_capabilities", "sandbox", "last_updated"]
    missing = [k for k in required if k not in manifest]
    if missing:
        raise ValueError(f"missing required keys: {missing}")


def verify_manifest(manifest_path: Path, schema_path: Path) -> list[str]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    if jsonschema_validate is not None:
        jsonschema_validate(manifest, schema)
    else:
        _fallback_validate(manifest)

    findings: list[str] = []
    sandbox = manifest.get("sandbox", {})
    if sandbox.get("network_access") == "full":
        findings.append("network_access is full; require explicit approval controls")
    if not sandbox.get("tool_allowlist"):
        findings.append("tool_allowlist is empty")

    for cap in manifest.get("declared_capabilities", []):
        if cap.get("risk_tier") in {"high", "critical"} and not cap.get("requires_human_approval", False):
            findings.append(f"{cap.get('name')} is high-risk without HITL gate")
    return findings


if __name__ == "__main__":
    manifest_path = Path(sys.argv[1])
    schema_path = Path(sys.argv[2])
    results = verify_manifest(manifest_path, schema_path)
    print(json.dumps({"findings": results}, indent=2))
