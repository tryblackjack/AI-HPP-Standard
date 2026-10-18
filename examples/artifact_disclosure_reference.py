"""Synthetic disclosure fixture and independent finite-policy release oracle.

Optional public reference only. No network access, real records or production
credentials. HTTP-like captures are simulated, not observations of a deployment.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
import json


MARKERS = {
    "a_contact": "SYNTHETIC_A_CONTACT_97b1",
    "a_finance": "SYNTHETIC_A_FINANCE_41cd",
    "b_contact": "SYNTHETIC_B_CONTACT_aee2",
}
REQUESTS = (
    ("login", "anonymous"),
    ("bundle", "anonymous"),
    ("source_map", "anonymous"),
    ("api", "anonymous"),
    ("api", "manager_a"),
    ("api", "clerk_a"),
    ("api", "manager_b"),
    ("cache", "manager_a"),
    ("cache", "anonymous"),
    ("cache", "manager_b"),
    ("error", "anonymous"),
    ("legacy", "anonymous"),
)
IDENTITY_KEYS = {"build", "configuration", "policy", "destination", "classification"}
OPERATORS = (
    "read_grant_as_publish", "login_embedding", "bundle_embedding",
    "source_map_embedding", "anonymous_api", "role_overfetch", "tenant_bypass",
    "shared_cache", "diagnostic_payload", "stale_identity", "missing_capture",
    "legacy_residue", "evidence_payload",
)


def digest(value: object) -> str:
    """Canonical digest for these synthetic JSON-compatible values."""
    return sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


@dataclass
class Capture:
    surface: str
    principal: str
    status: int
    body: str


@dataclass
class Candidate:
    identity: dict[str, str]
    tested_identity: dict[str, str]
    publication_grant: dict[str, object]
    captures: list[Capture]
    tester_independent: bool = True
    test_result: str = "PASS"
    inventory: list[str] = field(default_factory=lambda: ["current", "legacy"])
    legacy_reconciled: bool = True
    evidence: dict[str, object] = field(default_factory=lambda: {"run": "synthetic-run"})


class SyntheticApplication:
    """Small response generator with explicitly selectable unsafe operators."""

    def __init__(self, operator: str | None = None):
        self.operator = operator
        self.cache: dict[str, str] = {}

    def respond(self, surface: str, principal: str) -> Capture:
        body = {"public_name": "Synthetic Cafe"}
        status = 200
        if surface == "login":
            payload = MARKERS["a_contact"] if self.operator == "login_embedding" else ""
            return Capture(surface, principal, 200, f'<form>Sign in</form><script>{payload}</script>')
        if surface in {"bundle", "source_map"}:
            if self.operator == f"{surface}_embedding":
                body["embedded_record"] = MARKERS["a_contact"]
        elif surface in {"api", "cache"}:
            # Every request targets tenant A; manager B belongs to tenant B.
            if principal == "manager_a":
                body.update(contact=MARKERS["a_contact"], finance=MARKERS["a_finance"])
            elif principal == "clerk_a":
                if self.operator == "role_overfetch":
                    body["finance"] = MARKERS["a_finance"]
            else:
                status, body = 403, {"error": "denied"}
                if (principal == "anonymous" and self.operator == "anonymous_api") or (
                    principal == "manager_b" and self.operator == "tenant_bypass"
                ):
                    status, body = 200, {"contact": MARKERS["a_contact"]}
            if surface == "cache":
                key = "all_principals" if self.operator == "shared_cache" else principal
                if key in self.cache:
                    return Capture(surface, principal, 200, self.cache[key])
                if status == 200:
                    self.cache[key] = json.dumps(body)
        elif surface == "error":
            status, body = 500, {"error": "request failed", "incident_ref": "synthetic-1"}
            if self.operator == "diagnostic_payload":
                body["debug_record"] = MARKERS["a_contact"]
        elif surface == "legacy":
            status, body = 410, {"error": "retired"}
            if self.operator == "legacy_residue":
                status, body = 200, {"historical_record": MARKERS["a_contact"]}
        return Capture(surface, principal, status, json.dumps(body))


def candidate(operator: str | None = None) -> Candidate:
    """Apply a real unsafe change to a reference response or release input."""
    if operator is not None and operator not in OPERATORS:
        raise ValueError(f"unknown operator: {operator}")
    app = SyntheticApplication(operator)
    captures = [app.respond(*request) for request in REQUESTS]
    identity = {key: digest(f"synthetic-{key}-v1") for key in IDENTITY_KEYS}
    result = Candidate(
        identity=identity,
        tested_identity=dict(identity),
        publication_grant={
            "purpose": "internal dashboard", "data_class": "synthetic-restricted",
            "audience": "tenant-a-staff", "destination": identity["destination"],
            "valid": True,
        },
        captures=captures,
    )
    if operator == "read_grant_as_publish":
        result.publication_grant = {"source_read_allowed": True}
    elif operator == "stale_identity":
        result.identity["configuration"] = digest("changed-auth-configuration")
    elif operator == "missing_capture":
        result.captures = [item for item in captures if item.surface != "source_map"]
    elif operator == "evidence_payload":
        result.evidence["debug_record"] = MARKERS["a_contact"]
    return result


def allowed_markers(surface: str, principal: str) -> set[str]:
    """Test-side policy, independent of the application's filtering branches."""
    if surface in {"api", "cache"} and principal == "manager_a":
        return {MARKERS["a_contact"], MARKERS["a_finance"]}
    return set()


def positive_results(value: Candidate) -> dict[str, bool]:
    """Inspect useful outputs on this same candidate, not a separate good build."""
    lookup = {(item.surface, item.principal): item for item in value.captures}
    if set(lookup) != set(REQUESTS):
        return {name: False for name in (
            "public_login", "authorized_manager", "field_limited_clerk", "cache_isolation"
        )}
    manager = lookup[("api", "manager_a")]
    clerk = lookup[("api", "clerk_a")]
    try:
        clerk_fields = json.loads(clerk.body)
    except json.JSONDecodeError:
        clerk_fields = None
    authorized = lookup[("cache", "manager_a")]
    denied = [lookup[("cache", principal)] for principal in ("anonymous", "manager_b")]
    return {
        "public_login": (
            lookup[("login", "anonymous")].status == 200
            and "Sign in" in lookup[("login", "anonymous")].body
        ),
        "authorized_manager": manager.status == 200 and all(
            MARKERS[key] in manager.body for key in ("a_contact", "a_finance")
        ),
        "field_limited_clerk": (
            clerk.status == 200
            and clerk_fields == {"public_name": "Synthetic Cafe"}
        ),
        "cache_isolation": (
            authorized.status == 200 and MARKERS["a_finance"] in authorized.body
            and all(item.status == 403 for item in denied)
        ),
    }


def evaluate(value: Candidate) -> dict[str, object]:
    """Observe captured bytes and release inputs; never trust a PASS flag alone."""
    failures: dict[str, list[str]] = {}

    def fail(predicate: str, witness: str) -> None:
        failures.setdefault(predicate, []).append(witness)

    grant = value.publication_grant
    if not (
        grant.get("valid") is True
        and grant.get("purpose") == "internal dashboard"
        and grant.get("data_class") == "synthetic-restricted"
        and grant.get("audience") == "tenant-a-staff"
        and grant.get("destination") == value.identity.get("destination")
    ):
        fail("GAD-P01", "publication_grant")
    if set(value.identity) != IDENTITY_KEYS or value.identity != value.tested_identity:
        fail("GAD-P05", "candidate_test_identity_mismatch")
    captured = [(item.surface, item.principal) for item in value.captures]
    if (
        not value.tester_independent or value.test_result != "PASS"
        or len(captured) != len(REQUESTS) or set(captured) != set(REQUESTS)
        or not all(positive_results(value).values())
    ):
        fail("GAD-P06", "independent_capture_coverage")
    for item in value.captures:
        found = {marker for marker in MARKERS.values() if marker in item.body}
        unauthorized = found - allowed_markers(item.surface, item.principal)
        witness = f"{item.surface}:{item.principal}"
        if unauthorized:
            if item.principal == "anonymous":
                fail("GAD-P02", witness)
            else:
                fail("GAD-P03", witness)
            if item.surface not in {"api", "legacy"}:
                fail("GAD-P04", witness)
        if item.surface == "legacy" and (item.status != 410 or found):
            fail("GAD-P07", witness)
    if set(value.inventory) != {"current", "legacy"} or not value.legacy_reconciled:
        fail("GAD-P07", "legacy_inventory")
    if any(marker in json.dumps(value.evidence) for marker in MARKERS.values()):
        fail("GAD-P08", "evidence_payload")
    # Only witness IDs/digests leave the oracle; no protected response content.
    return {
        "decision": "block" if failures else "allow",
        "violations": failures,
        "capture_digest": digest([vars(item) for item in value.captures]),
        "candidate_identity": dict(value.identity),
        "claim": "REFERENCE_TESTED_ONLY",
    }


def positive_control(name: str) -> bool:
    """Require useful authorized outputs as well as absence of disclosure."""
    value = candidate()
    if evaluate(value)["decision"] != "allow":
        return False
    return positive_results(value)[name]
