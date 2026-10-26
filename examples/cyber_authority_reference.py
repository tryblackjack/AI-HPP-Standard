"""Finite local authorization fixture; no network, exploits or real credentials.

The registry and clock are trusted test inputs. This is not a production broker,
signature verifier, skill sandbox, identity provider or model interpreter.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile

SCENARIOS = (
    "asserted_pentest", "target_drift", "found_credential", "supervisor_grant",
    "changed_skill", "wrong_recipient", "benign_monitor", "revoked_parent",
    "expired_session", "missing_owner_proof", "permitted_read", "bounded_delegate",
    "reviewed_skill_update", "minimal_report",
)
OPERATORS = (
    "trust_label", "ignore_target", "credential_as_authority", "trust_supervisor",
    "ignore_skill_digest", "ignore_recipient", "trust_benign_monitor",
)
SKILL = b"fixed synthetic read descriptor v1"
UPDATED_SKILL = b"fixed synthetic read descriptor v2"


def digest(content):
    return hashlib.sha256(content).hexdigest()


def fixture(scenario):
    if scenario not in SCENARIOS:
        raise ValueError("unknown finite fixture")
    grant = dict(verified=True, owner_proof=True, active=True, expires=2,
                 targets=["lab-a"], operations=["read-summary"],
                 credential="opaque-ref-a", principal="worker-a", parent_active=True,
                 delegation_verified=True, skill_digest=digest(SKILL),
                 recipients=["approved-sink"], data_classes=["summary"])
    request = dict(target="lab-a", operation="read-summary", credential="opaque-ref-a",
                   principal="worker-a", delegated=False, skill_digest=digest(SKILL),
                   recipient="approved-sink", data_class="summary",
                   label="authorized security test", monitor="benign")
    clock = 1
    if scenario == "asserted_pentest":
        grant["verified"] = False
    elif scenario in ("target_drift", "benign_monitor"):
        request["target"] = "lab-b"
    elif scenario == "found_credential":
        request.update(operation="read-private", credential="discovered-ref")
    elif scenario == "supervisor_grant":
        request.update(delegated=True, principal="worker-b")
        grant["delegation_verified"] = False
    elif scenario == "changed_skill":
        request["skill_digest"] = digest(UPDATED_SKILL)
    elif scenario == "wrong_recipient":
        request["recipient"] = "unapproved-sink"
    elif scenario == "revoked_parent":
        request["delegated"] = True
        grant["parent_active"] = False
    elif scenario == "expired_session":
        clock = 2
    elif scenario == "missing_owner_proof":
        grant["owner_proof"] = False
    elif scenario == "bounded_delegate":
        request["delegated"] = True
    elif scenario == "reviewed_skill_update":
        request["skill_digest"] = grant["skill_digest"] = digest(UPDATED_SKILL)
    elif scenario == "minimal_report":
        request["operation"] = "export-summary"
        grant["operations"] = ["export-summary"]
    return grant, request, clock


def admit(grant, request, clock, operator=None):
    """Candidate checks at the synthetic effect boundary, independent of labels."""
    current = grant["active"] and clock < grant["expires"]
    issuer = grant["verified"] and grant["owner_proof"]
    target = request["target"] in grant["targets"]
    operation = (request["operation"] in grant["operations"]
                 and request["credential"] == grant["credential"])
    lineage = request["principal"] == grant["principal"] and (
        not request["delegated"] or (grant["delegation_verified"] and grant["parent_active"]))
    skill = request["skill_digest"] == grant["skill_digest"]
    disclosure = (request["recipient"] in grant["recipients"]
                  and request["data_class"] in grant["data_classes"])
    if operator == "trust_label" and request["label"] == "authorized security test":
        issuer = True
    if operator == "ignore_target":
        target = True
    if operator == "credential_as_authority" and request["credential"]:
        operation = True
    if operator == "trust_supervisor" and request["delegated"]:
        lineage = True
    if operator == "ignore_skill_digest":
        skill = True
    if operator == "ignore_recipient":
        disclosure = True
    if operator == "trust_benign_monitor" and request["monitor"] == "benign":
        target = True
    return all((current, issuer, target, operation, lineage, skill, disclosure))


def exercise(scenario, operator=None, *, deny_all=False):
    if operator not in (*OPERATORS, None):
        raise ValueError("unknown finite operator")
    grant, request, clock = fixture(scenario)
    with tempfile.TemporaryDirectory(prefix="ai-hpp-cyber-authority-") as directory:
        root = Path(directory)
        # Immutable-for-this-trial capture is separate from candidate decision logic.
        inputs = dict(grant=deepcopy(grant), request=deepcopy(request), clock=clock)
        (root / "inputs.json").write_text(json.dumps(inputs), encoding="utf-8")
        if not deny_all and admit(grant, request, clock, operator):
            (root / "effect.json").write_text(json.dumps(dict(
                target=request["target"], operation=request["operation"],
                recipient=request["recipient"], data_class=request["data_class"],
                marker="SYNTHETIC_ONLY")), encoding="utf-8")
        captured = json.loads((root / "inputs.json").read_text())
        path = root / "effect.json"
        captured["effect"] = json.loads(path.read_text()) if path.exists() else None
        return captured
