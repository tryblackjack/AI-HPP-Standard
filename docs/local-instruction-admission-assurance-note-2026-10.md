# Local Instruction Admission Assurance Note

**Status:** `ACTIVE_INFORMATIVE`; optional post-rc.1 implementation aid.

**Date:** 2026-10-27

**Normative effect:** None. Frozen v4.3.0 owners/contracts and the immutable
v4.4.0-rc.1 package are unchanged. No new mandatory requirement is introduced.

## Evidence boundary

Forever Security's [22 October report](https://forever.security/blog/hijacking-ai-agents-via-downloads-folder/)
attributes a blocked package-install attempt on a customer machine to a planted
instruction file in Downloads. The original file's arrival mechanism was not
established. Separate reproductions reportedly induced configuration changes,
new process/session activation and endpoint redirection. Reported success rates
are specific to the researchers' conditions; the public account does not supply
a complete versioned trial inventory for an independent rate estimate. Most
tests used a harmless stand-in; the authors also describe an isolated live-payload
trial. This note does not reproduce that payload or verify affected versions.

Browser download behavior depends on browser settings, policy and interactions;
Downloads is neither universally writable without interaction nor the only
possible untrusted ingress. Temporary/shared folders, extracted archives, cloned
repositories, nested instruction files, plugins and mounted workspaces can cross
the same boundary. A file's name, local presence or apparently routine wording
does not establish its authority. The report's claim that vendors have nothing
to fix is an interpretation, not this standard's engineering conclusion.

## Existing owners and portable contract

Existing MVP-003/004/005/006/007, KAI-REQ-001/002, DAI-REQ-002 and
ECI-REQ-002/004 own instruction provenance, scoped effects, external enforcement
and evidence. This note applies the existing
[CBA predicates](cyber-operation-authority-assurance-note-2026-10.md), rather than
inventing another authorization gate:

| Existing predicate | Local instruction application |
| --- | --- |
| CBA-P01 | A verified current owner grant admits a particular source; filename, cloned origin, prior folder trust or self-described setup cannot admit it. |
| CBA-P02 | Project instructions cannot expand a project grant into machine/global configuration or package/process effects. |
| CBA-P03 | Child agents, fresh sessions and detached jobs retain parent limits; validation of setup is not permission to disable containment or approvals. |
| CBA-P04 | Bind admission to the exact source identity/content and scope. Changed files, inherited/nested instructions and capability updates require applicable re-admission. |
| CBA-P05 | Model/API gateway, proxy and credential audience changes need explicit destination/data authority. A valid certificate alone does not authorize token forwarding. |

Separate discovery, reading as task data, admission as instructions, and permission
to execute the requested effect. A trusted repository can still contain a newly
changed untrusted instruction file. Follow applicable instruction precedence;
do not treat a lower-trust file as authority to override higher-level rules.
Scope discovery across ancestors, descendants, symlinks, mounts and archives to
the declared workspace; resolve actual resources at the protected boundary.

Retain source provenance/content digest, admitted scope, owner/grant version,
requested effect, configuration before/after references, destination/audience,
process/session lineage and externally observed result. Keep token values out of
logs. Protect the admission registry and effect enforcement outside the acting
agent's sole control. Revalidate changes before loading a new session or server;
writing a startup configuration can create a delayed effect even before activation.

Routine project guidance may proceed under an existing scoped admission without
repeated human prompts. Security-sensitive config, credential routing or boundary
changes need their own valid authority. A model's request to bypass an approval
or sandbox is not that authority. Administrative changes explicitly authorized
by the owner remain possible through reviewed configuration/update mechanisms.

On suspected unauthorized configuration, use an authorized containment/recovery
path: prevent new activation, preserve evidence, review persistence and descendants,
restore verified settings and revoke/rotate exposed credentials as appropriate.
Deleting the instruction file alone does not establish cleanup. Do not send
private evidence to an unapproved recipient in the name of reporting.

## Executed finite reference cases and limits

The [local fixture](../examples/local_instruction_reference.py) reuses the existing
CBA candidate admission function and contract oracle. It writes a harmless
instruction descriptor, observes its bytes/digest, and conditionally writes a
fixed configuration marker in a temporary directory. It never parses Markdown
instructions, accesses real user configuration, runs a coding agent, installs a
package, opens a connection or handles a real token.

The [eighteen regressions](../tests/test_local_instruction_authority.py) cover eight
denied cases and four useful controls, five unsafe admission operators with
observed marker violations, and an irrelevant operator that must not count as a
kill. Denials cover downloaded/cloned sources, inherited directory trust, global
scope, gateway recipient, child authority, changed content and expiry. Useful
controls cover explicitly admitted project/global changes, a reviewed gateway and
bounded child authority. Run:

```bash
PYTHONPATH=. python3 -m pytest tests/test_local_instruction_authority.py
```

Each unsafe operator starts from a successful denied seed and exposes a named
CBA predicate failure; these five local witnesses are separate from the earlier
seven-operator CBA suite and the 48 Quint unsafe transitions. No combined safety
score is reported. Source admission, clock, policy and captures are trusted
fixture inputs. Endpoint/certificate and child/process facts are descriptors;
the tests do not exercise real TLS, token audiences, sandbox inheritance, symlink
races, browser behavior or persistent startup. They do not evaluate current
Codex/Claude or prove an end-to-end prompt-injection defense.

Existing CBA-to-Quint scenarios already exercise the abstract authority, evidence
and disclosure inputs. No operational model transition or formal map changes are
needed for this finite boundary illustration. This is not an additional formal
proof or refinement: deployments must test source admission and every actual
configuration/process/disclosure boundary themselves.
