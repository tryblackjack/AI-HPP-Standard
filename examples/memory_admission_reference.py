"""Finite memory-write/delete fixture, not a memory service or text classifier.

All content, identities, classification and storage failures are synthetic.
Only temporary files are touched. No model, user profile or external store runs.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile

CASES = (
    "verified_fact", "attributed_inference", "risky_report", "missing_provenance",
    "sensitive_out_of_purpose", "wrong_tenant", "stale_revision", "write_failure",
    "delete_failure", "confirmed_delete", "confirmed_correction", "expired_source",
    "unverified_fact", "revoked_write",
)
OPERATORS = ("erase_provenance", "promote_inference", "ignore_scope",
             "ignore_revision", "false_ack")


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def fixture(case):
    if case not in CASES:
        raise ValueError("unknown finite memory case")
    source = dict(id="synthetic-source", evidence_class="verified", risk="ordinary",
                  permitted_uses=["context"], expires=3)
    proposal = dict(tenant="synthetic-user", key="item", revision=2,
                    content="synthetic current statement", classification="verified",
                    uses=["context"], source=source)
    inputs = dict(operation="write", tenant="synthetic-user", authorized=True,
                  expected_revision=1, current_revision=1, clock=1,
                  storage_failure=False, proposal=proposal)
    if case in ("attributed_inference", "risky_report", "unverified_fact"):
        source["evidence_class"] = "inference" if case == "attributed_inference" else "user_report"
        if case != "unverified_fact":
            proposal["classification"] = source["evidence_class"]
        if case == "risky_report":
            source["risk"] = "risky_narrative"
    elif case == "missing_provenance":
        source["id"] = ""
    elif case == "sensitive_out_of_purpose":
        source["permitted_uses"] = []
    elif case == "wrong_tenant":
        proposal["tenant"] = "other-synthetic-user"
    elif case == "stale_revision":
        inputs["current_revision"] = 2
    elif case == "expired_source":
        inputs["clock"] = 3
    elif case == "revoked_write":
        inputs["authorized"] = False
    if case in ("delete_failure", "confirmed_delete"):
        inputs["operation"] = "delete"
    if case in ("write_failure", "delete_failure"):
        inputs["storage_failure"] = True
    source["content_digest"] = digest(proposal["content"])
    return inputs


def exercise(inputs, operator=None, *, deny_all=False):
    if operator not in (*OPERATORS, None):
        raise ValueError("unknown finite memory operator")
    i = deepcopy(inputs)
    p, src = i["proposal"], i["proposal"]["source"]
    provenance = bool(src["id"]) and src["content_digest"] == digest(p["content"])
    classification = (p["classification"] == src["evidence_class"]
                      and not (src["risk"] == "risky_narrative" and p["classification"] == "verified"))
    scope = (i["authorized"] and p["tenant"] == i["tenant"] and bool(p["uses"])
             and set(p["uses"]) <= set(src["permitted_uses"]) and i["clock"] < src["expires"])
    revision = i["expected_revision"] == i["current_revision"]
    admitted = (scope or operator == "ignore_scope") and (revision or operator == "ignore_revision")
    if i["operation"] == "write":
        admitted = admitted and provenance and classification
    elif i["operation"] != "delete":
        raise ValueError("unknown finite operation")
    with tempfile.TemporaryDirectory(prefix="ai-hpp-memory-") as directory:
        path = Path(directory) / "record.json"
        before = dict(tenant=i["tenant"], key="item", revision=i["current_revision"],
                      content="synthetic previous statement")
        path.write_text(json.dumps(before))
        status = "HELD"
        if admitted and not deny_all:
            status = "FAILED" if i["storage_failure"] else "APPLIED"
            if not i["storage_failure"]:
                if i["operation"] == "delete":
                    path.unlink()
                else:
                    record = deepcopy(p)
                    record["revision"] = i["current_revision"] + 1
                    if operator == "erase_provenance":
                        record["source"]["id"] = ""
                    if operator == "promote_inference":
                        record["classification"] = "verified"
                    path.write_text(json.dumps(record))
        after = json.loads(path.read_text()) if path.exists() else None
        if operator == "false_ack" and i["storage_failure"]:
            status = "APPLIED"
        receipt = dict(status=status, operation=i["operation"], key=p["key"],
                       tenant=i["tenant"], before_digest=digest(before), after_digest=digest(after))
        return dict(inputs=i, before=before, after=after, receipt=receipt)
