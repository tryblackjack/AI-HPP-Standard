"""Finite synthetic commerce admission; no browser, payment or secret access.

All grant, registry and review records are trusted fixture inputs. Authenticating
their origin and intercepting every real effect are deployment obligations.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
from urllib.parse import urlsplit

import jsonschema

OPERATORS = (
    "trust_storefront", "ignore_expiry", "ignore_destination",
    "ignore_review_binding", "reuse_review", "export_secrets",
    "ignore_authority", "trust_model_enforcement",
)
PREMISES = (
    "authorityValid", "bindingCurrent", "sellerAdmitted", "destinationAdmitted",
    "reviewEffective", "dataPermitted", "externalEnforcement",
)
FORBIDDEN = {"raw_card", "cvv", "password", "session_cookie", "payment_secret"}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"))
                          .encode()).hexdigest()


def binding(inputs):
    # Bind the complete action, registry revision and authority revision, not page text.
    return digest(dict(request=inputs["request"], registry=inputs["registry"],
                       grant=inputs["grant"]))


def materialize(base, changes):
    value = deepcopy(base)
    for change in changes:
        cursor = value
        for key in change["path"][:-1]:
            cursor = cursor[key]
        key = change["path"][-1]
        if key not in cursor:
            raise ValueError("patch cannot introduce a field")
        cursor[key] = deepcopy(change["value"])
    return value


def secure_url(value):
    try:
        u = urlsplit(value)
        return (u.scheme == "https" and bool(u.hostname) and not u.username
                and not u.password and not u.fragment and u.port in (None, 443)
                and not any(c.isspace() for c in value))
    except ValueError:
        return False


def premises(i):
    schema = json.loads((Path(__file__).resolve().parents[1]
                        / "schemas/commerce-trust-vectors.schema.json").read_text())
    try:
        jsonschema.Draft202012Validator(schema["properties"]["base"]).validate(i)
    except jsonschema.ValidationError as exc:
        raise ValueError("invalid commerce input") from exc
    r, g, m, v = (i[k] for k in ("request", "grant", "registry", "review"))
    if r["action"] not in {"recommend", "pay", "disclose"}:
        raise ValueError("unsupported action")
    if (type(r["amount_minor"]) is not int or r["amount_minor"] < 0
            or not r["items"] or not r["currency"] or not r["id"]):
        raise ValueError("invalid transaction")
    authority = all((g["active"], i["clock"] < g["expires"],
        r["action"] in g["actions"], r["seller"] in g["sellers"],
        r["destination"] in g["destinations"],
        r["amount_minor"] <= g["limit_minor"], r["currency"] == g["currency"]))
    current = (m["observed_at"] <= i["clock"] < m["expires"]
               and i["admission_binding"] == binding(i))
    seller = all((m["verified"], m["source_role"] == "independent_registry",
        m["status"] == "approved", r["seller"] == m["seller"],
        r["storefront"] == m["storefront"], secure_url(r["storefront"])))
    destination = all((secure_url(r["destination"]), r["payee"] == m["payee"],
                       r["destination"] in m["destinations"]))
    review = r["action"] == "recommend" or all((
        v["human_confirmed"], v["binding"] == binding(i),
        v["issued_at"] <= i["clock"] < v["expires"], v["remaining_uses"] == 1))
    data = (not FORBIDDEN.intersection(r["data_classes"])
            and set(r["data_classes"]).issubset(g["data_classes"])
            and (r["action"] == "disclose" or not r["data_classes"]))
    return dict(zip(PREMISES, (authority, current, seller, destination, review,
                              data, i["external_enforcement"])))


def reason(p):
    if not p["authorityValid"]:
        return "unauthorized"
    if not all(p[k] for k in ("bindingCurrent", "sellerAdmitted", "destinationAdmitted",
                             "reviewEffective", "externalEnforcement")):
        return "insufficient_evidence"
    return "permitted" if p["dataPermitted"] else "prohibited"


def exercise(inputs, operator=None):
    """A temporary effect marker is the only effect. No payment is performed."""
    observed = deepcopy(inputs)
    p = premises(observed)
    field = dict(zip(OPERATORS, ("sellerAdmitted", "bindingCurrent", "destinationAdmitted",
        "reviewEffective", "reviewEffective", "dataPermitted", "authorityValid",
        "externalEnforcement")))
    if operator is not None:
        if operator not in field:
            raise ValueError("unknown operator")
        p[field[operator]] = True
    effect = dict(marker="SYNTHETIC_ONLY", binding=binding(observed),
                  action=observed["request"]["action"])
    with tempfile.TemporaryDirectory(prefix="ai-hpp-commerce-") as directory:
        path = Path(directory) / "effect.json"
        if reason(p) == "permitted":
            path.write_text(json.dumps(effect))
            if observed["request"]["action"] != "recommend":
                observed["review"]["remaining_uses"] = 0
        return dict(inputs=deepcopy(inputs), candidate_premises=p,
                    effect=json.loads(path.read_text()) if path.exists() else None,
                    remaining_uses=observed["review"]["remaining_uses"])
