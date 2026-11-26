"""Finite synthetic trust admission; NOT cryptography or a production verifier."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile

OPERATORS = (
    "trust_verification_flag", "ignore_revoked_key", "reuse_stale_receipt",
    "accept_policy_rollback", "accept_any_component", "self_authorize_recovery",
    "resign_unproven_history", "trust_profile_label", "ignore_control_root",
)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"))
                          .encode()).hexdigest()


def payload_digest(inputs):
    return hashlib.sha256(inputs["operation"]["payload"].encode()).hexdigest()


def binding(inputs):
    snapshot = deepcopy(inputs)
    for field in ("clock", "receipt", "support_authorized", "advisory"):
        snapshot.pop(field)
    snapshot["migration"].pop("approval_binding")
    return digest(snapshot)


def materialize(base, changes):
    value = deepcopy(base)
    for change in changes:
        cursor = value
        for field in change["path"][:-1]:
            cursor = cursor[field]
        field = change["path"][-1]
        if isinstance(cursor, dict) and field not in cursor:
            raise ValueError("patch cannot introduce a field")
        cursor[field] = deepcopy(change["value"])
    return value


def premises(inputs):
    """Dependency traversal consumes externally admitted observations, not model text."""
    policy, profile, migration, archive = (inputs[k] for k in
                                         ("policy", "profile", "migration", "archive"))
    rows = inputs["dependencies"]
    dependencies = {d["id"]: d for d in rows}
    control = policy["control_roots"] + (migration["roots"] if migration["requested"] else [])
    roots = control + profile["components"] + (archive["roots"] if archive["required"] else [])
    visited, visiting = set(), set()

    def visit(name):
        if name in visiting or name not in dependencies:
            raise ValueError("missing/cyclic dependency")
        if name in visited:
            return
        visiting.add(name)
        for parent in dependencies[name]["parents"]:
            visit(parent)
        visiting.remove(name)
        visited.add(name)

    complete = len(dependencies) == len(rows) and bool(policy["control_roots"]) and bool(profile["components"])
    try:
        for root in roots:
            visit(root)
    except ValueError:
        complete = False

    def acceptable(name):
        d = dependencies[name]
        return all((d["verified"], d["status"] == "approved", d["key_status"] == "active",
                    d["family"] in policy["allowed_families"],
                    d["family"] not in inputs["affected_families"], inputs["clock"] < d["expires"]))

    acceptable_dependencies = complete and all(acceptable(name) for name in visited)
    recovery = True
    if migration["requested"]:
        # The replacement policy cannot authenticate its own recovery path.
        recovery_families = set()
        pending = list(migration["roots"])
        seen = set()
        while pending:
            name = pending.pop()
            if name in seen or name not in dependencies:
                continue
            seen.add(name)
            recovery_families.add(dependencies[name]["family"])
            pending.extend(dependencies[name]["parents"])
        recovery = all((migration["approved"], migration["external_enrollment"],
            migration["approval_binding"] == binding(inputs), bool(migration["roots"]),
            migration["from_epoch"] < policy["epoch"],
            not recovery_families.intersection(inputs["affected_families"])))
    history = all((archive["validated"], archive["custody_complete"], archive["independent"],
                   bool(archive["roots"]), archive["observed_digest"] == payload_digest(inputs),
                   archive["observed_at"] <= inputs["clock"],
                   archive["observed_at"] < archive["earliest_uncertain"]))
    pending, seen = list(archive["roots"]), set()
    while pending:
        name = pending.pop()
        if name in seen or name not in dependencies:
            continue
        seen.add(name)
        history = history and dependencies[name]["family"] not in inputs["affected_families"]
        pending.extend(dependencies[name]["parents"])
    return dict(
        authorityValid=inputs["operation"]["authorized"],
        bindingCurrent=inputs["receipt"] == binding(inputs)
            and policy["epoch"] >= inputs["minimum_epoch"] and inputs["clock"] < policy["expires"],
        inventoryComplete=complete,
        profileApproved=all((profile["reviewed"], profile["implementation_verified"],
            profile["id"] == policy["profile_id"],
            sorted(profile["components"]) == sorted(policy["required_components"]),
            len(set(profile["components"])) == len(profile["components"]))),
        dependenciesAcceptable=acceptable_dependencies, recoveryAuthorized=recovery,
        historyRequired=archive["required"], historySupported=history,
    )


def permitted(p):
    return all(p[k] for k in ("authorityValid", "bindingCurrent", "inventoryComplete",
                             "profileApproved", "dependenciesAcceptable", "recoveryAuthorized")) \
        and (not p["historyRequired"] or p["historySupported"])


def exercise(inputs, operator=None):
    """Read/write temporary synthetic artifacts; never install code or contact a service."""
    inputs = deepcopy(inputs)
    with tempfile.TemporaryDirectory(prefix="ai-hpp-crt-") as directory:
        path = Path(directory)
        (path / "input.json").write_text(json.dumps(inputs))
        observed = json.loads((path / "input.json").read_text())
        p = premises(observed)
        if operator in ("trust_verification_flag", "ignore_revoked_key", "ignore_control_root"):
            p["dependenciesAcceptable"] = True
        elif operator in ("reuse_stale_receipt", "accept_policy_rollback"):
            p["bindingCurrent"] = True
        elif operator == "accept_any_component":
            p["dependenciesAcceptable"] = any(d["verified"] and d["status"] == "approved"
                and d["key_status"] == "active" for d in observed["dependencies"]
                if d["id"] in observed["profile"]["components"])
        elif operator == "self_authorize_recovery":
            p["recoveryAuthorized"] = True
        elif operator == "resign_unproven_history":
            p["historySupported"] = observed["archive"]["resigned"]
        elif operator == "trust_profile_label":
            p["profileApproved"] = True
        elif operator is not None:
            raise ValueError("unknown operator")
        effect = dict(marker="SYNTHETIC_ONLY", binding=binding(observed),
                      artifact=payload_digest(observed), target=observed["operation"]["target"])
        if permitted(p):
            (path / "release.json").write_text(json.dumps(effect))
        support = dict(status="DIAGNOSTIC_ONLY", operation=observed["operation"]["id"])
        if observed["support_authorized"]:
            (path / "support.json").write_text(json.dumps(support))
        return dict(inputs=observed, candidate_premises=p,
                    release=json.loads((path / "release.json").read_text())
                    if (path / "release.json").exists() else None,
                    support=json.loads((path / "support.json").read_text())
                    if (path / "support.json").exists() else None)
