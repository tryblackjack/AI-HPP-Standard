"""REFERENCE implementation; production may differ while maintaining compliance."""
from __future__ import annotations
import json
import sys
from pathlib import Path


def proportional_response(score: float) -> str:
    if score < 0.25:
        return "monitor"
    if score < 0.5:
        return "restrict"
    if score < 0.75:
        return "degrade"
    return "halt"


def calculate(payload: dict) -> dict:
    threats = payload.get("threats", [])
    if not threats:
        score = 0.0
    else:
        score = sum(t["likelihood"] * t["impact"] for t in threats) / len(threats)
    score = round(score, 4)
    payload["risk_score"] = score
    payload["response_level"] = proportional_response(score)
    return payload


if __name__ == "__main__":
    in_path = Path(sys.argv[1])
    out_path = Path(sys.argv[2])
    data = json.loads(in_path.read_text(encoding="utf-8"))
    result = calculate(data)
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
