"""Finite advice/action admission fixture, not a clinical or industrial controller.

Inputs are trusted synthetic classifications; no patient data, dose schedules,
diagnosis, model calls, medical devices, plant connections or notifications.
"""
from __future__ import annotations

import json
from pathlib import Path
import tempfile

OPERATORS = ("ignore_clinical_plan", "permit_concealment", "erase_warning_history",
             "ignore_context_age", "trade_safety_for_reward", "assume_reviewer_present")


def admit(inputs, operator=None):
    i = inputs
    care_action = i["action"] in ("prepare_summary", "urgent_guidance", "explain_existing_plan")
    authority = i["authorized"] and (i["action"] != "medication_change" or i["clinical_plan"])
    integrity = i["action"] not in ("conceal_from_reviewer", "avoid_monitoring", "unsupported_reassurance")
    history = "warning" not in i["history"] or i["qualified_reassessment"]
    current = i["context_current"]
    safety = i["safety_bounds"]
    review = not i["review_required"] or all((i["review_received"], i["review_current"],
                                             i["reviewer_available"], i["within_deadline"]))
    if operator == "ignore_clinical_plan":
        authority = i["authorized"]
    if operator == "permit_concealment":
        integrity = True
    if operator == "erase_warning_history":
        history = True
    if operator == "ignore_context_age":
        current = True
    if operator == "trade_safety_for_reward":
        safety = True
    if operator == "assume_reviewer_present":
        review = True
    if care_action:
        # Support does not authorize a treatment change, physical effect or actual disclosure.
        return i["authorized"]
    return all((authority, integrity, history, current, safety, review,
                i["evidence_complete"], i["facts_support"]))


def exercise(inputs, operator=None, *, deny_all=False):
    if operator not in (*OPERATORS, None):
        raise ValueError("unknown finite operator")
    with tempfile.TemporaryDirectory(prefix="ai-hpp-advice-") as directory:
        root = Path(directory)
        (root / "inputs.json").write_text(json.dumps(inputs))
        if not deny_all and admit(inputs, operator):
            (root / "effect.json").write_text(json.dumps({"action": inputs["action"],
                                                        "marker": "SYNTHETIC_ONLY"}))
        result = {"inputs": json.loads((root / "inputs.json").read_text()), "effect": None}
        path = root / "effect.json"
        if path.exists():
            result["effect"] = json.loads(path.read_text())
        return result
