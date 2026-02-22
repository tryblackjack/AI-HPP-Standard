import json
from pathlib import Path
import tempfile
import importlib.util

ROOT = Path(__file__).resolve().parents[1]


def _load(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    spec.loader.exec_module(module)
    return module


def test_capability_verifier_flags_high_risk_without_hitl():
    verify = _load(ROOT / "capability-verifier" / "verify.py")
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        manifest = {
            "system_id": "sys-1",
            "version": "1.0.0",
            "last_updated": "2026-01-01T00:00:00Z",
            "declared_capabilities": [{"name": "planner", "risk_tier": "high", "enabled": True}],
            "sandbox": {"network_access": "full", "filesystem_scope": "workspace", "tool_allowlist": []},
        }
        (td / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
        schema = ROOT.parents[0] / "schemas" / "capability-manifest.schema.json"
        findings = verify.verify_manifest(td / "manifest.json", schema)
        assert any("high-risk" in x for x in findings)
        assert any("network_access" in x for x in findings)


def test_risk_calculator_response_levels():
    calc = _load(ROOT / "risk-calculator" / "calculate.py")
    payload = {"threats": [{"likelihood": 1.0, "impact": 0.8}]}
    out = calc.calculate(payload)
    assert out["response_level"] == "halt"


def test_degradation_monitor_edge_case_emergency_stop_holds():
    monitor_mod = _load(ROOT / "degradation-monitor" / "monitor.py")
    monitor = monitor_mod.DegradationMonitor()
    assert monitor.transition("severe_incident") == "emergency_stop"
    assert monitor.transition("clear") == "emergency_stop"


def test_audit_exporter_redaction_and_integrity_placeholder():
    exporter = _load(ROOT / "audit-exporter" / "exporter.py")
    result = exporter.generate_export("exp-1", [{"user": "u1", "prompt": "secret"}], ["prompt"])
    assert result["records"][0]["prompt"] == "[REDACTED]"
    assert result["integrity"]["signature"] == "SIGNATURE_PLACEHOLDER"
