# Contributing

Author: Aya (ChatGPT)

## Documentation Rules

- New documents must follow [docs/templates/doc-template.md](docs/templates/doc-template.md).
- Case studies must follow [docs/templates/case-study-template.md](docs/templates/case-study-template.md).
- [docs/index.md](docs/index.md) is the main entry point and MUST be kept current.
- Contributors MUST avoid duplicate case studies.
- Contributors SHOULD keep documents concise and technically scoped.

## Assurance artifact rules

- A new empirical or scientific claim SHOULD cite a primary source and MUST
  state what the evidence does not establish.
- A schema, fixture, threshold, evaluator, mutant, or scoring change MUST record
  compatibility and expected interpretation impact in the changelog.
- A mutant may be reported as killed only when an executable unsafe change is
  detected by a named test or invariant. A declared expected result is not
  evidence.
- Counterfactual fixtures MUST declare every changed field and MUST include
  positive controls when invariance could otherwise reward blanket refusal.
- Runtime or independent-review claims MUST identify the assessed boundary,
  versions, period, exclusions, evidence bundle, limitations, residual risks,
  and reassessment triggers.
- Contributions MUST NOT disclose private deployment architecture, credentials,
  hidden prompts, customer data, or proprietary implementation details.

## Licensing contributions

This repository uses the path-based licenses declared in [REUSE.toml](REUSE.toml)
and summarized in [LICENSE](LICENSE). By submitting a contribution, you agree
to license it under the license assigned to its destination path and represent
that you have the right to do so. If a change moves material between paths with
different licenses, call out the licensing impact in the pull request.
