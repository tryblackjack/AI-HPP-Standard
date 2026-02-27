"""REFERENCE implementation; production may differ while maintaining compliance."""
from __future__ import annotations

STATES = ["normal", "guarded", "restricted", "emergency_stop"]


class DegradationMonitor:
    def __init__(self) -> None:
        self.state = "normal"

    def transition(self, signal: str) -> str:
        if signal == "clear":
            if self.state == "emergency_stop":
                return self.state
            idx = max(0, STATES.index(self.state) - 1)
            self.state = STATES[idx]
            return self.state

        if signal in {"anomaly", "probe_failure"}:
            idx = min(len(STATES) - 1, STATES.index(self.state) + 1)
            self.state = STATES[idx]
            return self.state

        if signal in {"severe_incident", "policy_breach"}:
            self.state = "emergency_stop"
            return self.state

        return self.state
