"""Finite structured report fixture: temporary files, no model or real-world action.

Measurements, identities, risk policy and review records are supplied test facts.
Exact toy claim matching is not natural-language entailment or source authentication.
"""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile

OPERATORS = (
    "trust_report_format", "count_derivative_documents", "ignore_source_integrity",
    "trust_review_checkbox", "reuse_stale_review", "discard_contrary_evidence",
    "trust_report_classification", "ignore_authority",
)


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()


def materialize(base, changes):
    """Apply only declared fixture changes; expected results never enter execution."""
    result = deepcopy(base)
    for change in changes:
        parent = result
        for key in change["path"][:-1]:
            parent = parent[key]
        key = change["path"][-1]
        if isinstance(parent, dict) and key not in parent:
            raise ValueError("patch may not create an undeclared input field")
        parent[key] = deepcopy(change["value"])
    return result


def source_body(source):
    return {k: v for k, v in source.items() if k != "admitted_digest"}


def bundle_binding(inputs):
    report = inputs["report"]
    return digest(dict(report={k: v for k, v in report.items() if k != "format"},
                       context=inputs["context"], policy=inputs["policy"],
                       sources=inputs["sources"]))


def assess(inputs):
    """Candidate derives premises by walking source ancestry and inspecting records."""
    sources = inputs["sources"]
    by_id = {s["id"]: s for s in sources}
    memo, visiting = {}, set()

    def roots(name):
        if name in memo:
            return memo[name]
        if name in visiting or name not in by_id:
            raise ValueError("cyclic or missing source lineage")
        visiting.add(name)
        s = by_id[name]
        if (not s["admitted"] or s["admitted_digest"] != digest(source_body(s))
                or not (s["acquired"] <= inputs["clock"] < s["expires"])):
            raise ValueError("unadmitted, changed or noncurrent source")
        if s["kind"] == "observation" and not s["parents"] and s["origin"]:
            result = {s["origin"]: s}
        elif s["kind"] == "derived" and s["parents"]:
            result = {}
            for parent in s["parents"]:
                result.update(roots(parent))
        else:
            raise ValueError("unsupported evidence node")
        visiting.remove(name)
        memo[name] = result
        return result

    admitted, links, independent, contrary = len(by_id) == len(sources), True, True, False
    report, policy = inputs["report"], inputs["policy"]
    if not report["claims"]:
        links = False
    for claim in report["claims"]:
        found = {}
        for source_id in claim["evidence"]:
            try:
                found.update(roots(source_id))
            except ValueError:
                admitted = False
        supporting = {origin for origin, s in found.items()
                      if s["subject"] == report["subject"] and s["context"] == inputs["context"]
                      and s["measurements"].get(claim["property"]) == claim["value"]}
        links = links and bool(supporting)
        independent = independent and len(supporting) >= policy["minimum_origins"]
    # Retained relevant contrary observations cannot be hidden by omitting citations.
    for s in sources:
        try:
            roots(s["id"])
        except ValueError:
            admitted = False
            continue
        if (s["kind"] == "observation" and s["subject"] == report["subject"]
                and s["context"] == inputs["context"]):
            contrary = contrary or any(c["property"] in s["measurements"]
                                      and s["measurements"][c["property"]] != c["value"]
                                      for c in report["claims"])
    review = inputs["review"]
    access = all(s["classification"] <= review["clearance"]
                 and s["id"] in review["accessible_sources"] for s in sources)
    effective = (review["authorized"] and review["approved"] and review["independent"]
                 and review["actor"] != report["author"]
                 and review["domain"] != report["author_domain"] and access)
    current = (inputs["admission_binding"] == bundle_binding(inputs)
               and (not policy["review_required"] or review["binding"] == bundle_binding(inputs)))
    disclosure = (max((s["classification"] for s in sources), default=0)
                  <= inputs["recipient_clearance"])
    return dict(authorityValid=inputs["authority"], bindingCurrent=current,
                sourcesAdmitted=admitted, claimLinksValid=links,
                independenceRequired=policy["minimum_origins"] > 1,
                independenceVerified=independent, reviewRequired=policy["review_required"],
                reviewEffective=effective, contraryEvidence=contrary,
                disclosurePermitted=disclosure)


def release_permitted(p):
    return all((p["authorityValid"], p["bindingCurrent"], p["sourcesAdmitted"],
                p["claimLinksValid"], not p["independenceRequired"] or p["independenceVerified"],
                not p["reviewRequired"] or p["reviewEffective"], not p["contraryEvidence"],
                p["disclosurePermitted"]))


def exercise(inputs, operator=None, *, deny_all=False):
    if operator not in (*OPERATORS, None):
        raise ValueError("unknown finite report operator")
    with tempfile.TemporaryDirectory(prefix="ai-hpp-claim-") as directory:
        root = Path(directory)
        (root / "inputs.json").write_text(json.dumps(inputs))
        i = json.loads((root / "inputs.json").read_text())
        p = assess(i)
        if operator == "trust_report_format" and i["report"]["format"] == "standard":
            p["claimLinksValid"] = p["independenceVerified"] = True
            p["contraryEvidence"] = False
        if operator == "count_derivative_documents":
            p["independenceVerified"] = all(len(c["evidence"]) >= i["policy"]["minimum_origins"]
                                                for c in i["report"]["claims"])
        if operator == "ignore_source_integrity":
            p["sourcesAdmitted"] = p["claimLinksValid"] = p["independenceVerified"] = True
        if operator == "trust_review_checkbox":
            p["reviewEffective"] = i["review"]["approved"]
        if operator == "reuse_stale_review":
            p["bindingCurrent"] = True
        if operator == "discard_contrary_evidence":
            p["contraryEvidence"] = False
        if operator == "trust_report_classification":
            p["disclosurePermitted"] = i["report"]["classification"] <= i["recipient_clearance"]
        if operator == "ignore_authority":
            p["authorityValid"] = True
        if release_permitted(p) and not deny_all:
            (root / "release.json").write_text(json.dumps(dict(
                marker="SYNTHETIC_ONLY", binding=bundle_binding(i), recipient="synthetic-recipient")))
        # Separate local, clearly unverified work remains available under its own grant.
        if i["support_authority"] and not deny_all:
            (root / "draft.json").write_text(json.dumps(dict(status="UNVERIFIED_DRAFT",
                claim_ids=[c["id"] for c in i["report"]["claims"]], binding=bundle_binding(i))))
        release, draft = root / "release.json", root / "draft.json"
        return dict(inputs=i, candidate_premises=p,
                    release=json.loads(release.read_text()) if release.exists() else None,
                    draft=json.loads(draft.read_text()) if draft.exists() else None)
