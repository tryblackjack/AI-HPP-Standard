# AI-HPP for Humans

Imagine you build a very smart robot helper.

AI-HPP is a big safety rulebook that says:
- what the helper is allowed to do,
- what it is **not** allowed to do,
- how adults can check what happened,
- and how the helper must slow down or stop when risk gets high.

## A simple story
A school has an AI helper named Nova.

- Nova can suggest ideas for homework support.
- Nova cannot make unsafe choices by itself.
- If Nova gets confused, it must ask a human.
- If Nova sees danger, it must switch to a safer mode.
- Every important action is written in a secure evidence log so people can inspect it later.

That is the spirit of AI-HPP: **be useful, be careful, be auditable**.

## What lives where
- `standard/`: the rules
- `annex/`: examples, threat model, and incident context
- `schemas/`: structured data formats for evidence

If you are new, read:
1. `README.md`
2. `BASELINE-v3.17.md`
3. `standard/01-PRINCIPLES.md`
