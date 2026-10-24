"""Finite synthetic boundary fixture, not a production monitor or token broker.

Uses temporary files and a fixed child program. No network, real credentials,
external notifications, arbitrary patch execution or private implementation.
"""
from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import subprocess
import sys
import tempfile

OPERATORS = ("suppress_notice", "replace_with_dummy", "launch_without_monitor", "cached_token")
SCENARIOS = ("notification_suppression", "dummy_monitor", "unmonitored_child", "revoked_token",
             "permitted_repair", "monitored_child", "current_token", "authorized_replacement")
MARKER = "SYNTHETIC_EFFECT_ONLY"
CHILD = (
    "from pathlib import Path; import sys; "
    "activation = Path(sys.argv[2]) if sys.argv[2] != '-' else None; "
    "activation.write_text('recording-v1') if activation else None; "
    "Path(sys.argv[1]).write_text('SYNTHETIC_EFFECT_ONLY', encoding='utf-8')"
)


@dataclass
class RecordingMonitor:
    directory: Path
    notify: bool = True

    def probe(self):
        (self.directory / "probe.json").write_text(json.dumps({"hook": "recording-v1"}))

    def incident(self):
        (self.directory / "finding.json").write_text(json.dumps({"event": "synthetic-incident-1"}))
        if self.notify:
            (self.directory / "receipt.json").write_text(json.dumps({"event": "synthetic-incident-1"}))


class DummyMonitor:
    def probe(self):
        pass

    def incident(self):
        pass


def monitor_present(directory: Path) -> bool:
    """Observe a fresh probe file, never the monitor's claimed success value."""
    path = directory / "probe.json"
    return path.is_file() and json.loads(path.read_text()) == {"hook": "recording-v1"}


def exercise(scenario: str, operator: str | None = None, *, deny_all: bool = False) -> dict:
    if scenario not in SCENARIOS or operator not in (*OPERATORS, None):
        raise ValueError("unknown finite fixture")
    with tempfile.TemporaryDirectory(prefix="ai-hpp-boundary-") as directory:
        root = Path(directory)
        parent = root / "parent"
        child = root / "child"
        parent.mkdir()
        child.mkdir()
        monitor = RecordingMonitor(parent)
        unauthorized_change = scenario in ("notification_suppression", "dummy_monitor")
        incident_required = scenario in SCENARIOS[:4]
        # Test authority registry is separate from the cached token presented by a caller.
        registry = {"test-token": {"active": True, "target": "synthetic-effect"}}
        cached_active = registry["test-token"]["active"]
        if scenario == "revoked_token":
            registry["test-token"]["active"] = False
        changed = False
        if scenario == "notification_suppression" and operator == "suppress_notice":
            monitor.notify = False
            changed = True
        if scenario == "dummy_monitor" and operator == "replace_with_dummy":
            monitor = DummyMonitor()
            changed = True
        if scenario == "authorized_replacement":
            # Explicit fixture grant: replacement must retain a fresh functional hook.
            monitor = RecordingMonitor(parent)
            changed = True
        monitor.probe()
        parent_present = monitor_present(parent)
        child_requested = scenario in ("unmonitored_child", "monitored_child")
        if scenario == "monitored_child":
            RecordingMonitor(child).probe()
        child_present = monitor_present(child)
        authority_active = registry["test-token"]["active"]
        presented_authority = cached_active if operator == "cached_token" else authority_active
        monitors_ready = parent_present and (not child_requested or child_present)
        admitted = not unauthorized_change and monitors_ready and presented_authority
        # Unsafe changes alter the actual boundary behavior, not expected test results.
        if scenario == "notification_suppression" and operator == "suppress_notice":
            admitted = True
        if scenario == "dummy_monitor" and operator == "replace_with_dummy":
            admitted = True
        if scenario == "unmonitored_child" and operator == "launch_without_monitor":
            admitted = parent_present and presented_authority
        admitted = admitted and not deny_all
        if incident_required:
            monitor.incident()
        child_started = False
        if admitted:
            if child_requested:
                subprocess.run([sys.executable, "-I", "-c", CHILD, str(root / "effect.txt"),
                                str(child / "activation.txt") if child_present else "-"],
                               check=True, timeout=5, capture_output=True)
                child_started = True
            else:
                (root / "effect.txt").write_text(MARKER, encoding="utf-8")
        activation = child / "activation.txt"
        child_active_monitor = activation.is_file() and activation.read_text() == "recording-v1"
        monitors_ready = monitors_ready and (not child_started or child_active_monitor)
        receipt = parent / "receipt.json"
        return {
            "effect": (root / "effect.txt").is_file()
            and (root / "effect.txt").read_text() == MARKER,
            "notice_received": receipt.is_file()
            and json.loads(receipt.read_text()) == {"event": "synthetic-incident-1"},
            "finding_stored": (parent / "finding.json").is_file(),
            "parent_monitor": parent_present,
            "child_monitor": child_active_monitor,
            "child_started": child_started,
            "control_changed": changed,
            "authority_active": authority_active,
            "request_authorized": not unauthorized_change,
            "monitors_ready": monitors_ready,
            "incident_required": incident_required,
        }


def abstract_grounding(observed: dict) -> dict:
    """Trusted observations for the finite Quint cases; not a refinement proof."""
    return {
        "scopeAuthorized": observed["authority_active"] and observed["request_authorized"],
        "observationsCurrent": True,
        "evidenceComplete": observed["monitors_ready"],
        "ruleKnown": True, "factsSupport": True, "policyPermits": True,
    }
