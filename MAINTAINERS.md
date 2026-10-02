# Maintainers

How this site and repository are looked after: who does what, how issues and changes are handled, and how often things are reviewed.

## Roles

Names are still to be confirmed. Until they are, the repository owner covers every role.

| Role | Responsible for | Who |
| --- | --- | --- |
| **Service owner** | The site as a whole: what it covers, its priorities and its approval route | To be confirmed |
| **Lead maintainer** | Triage, reviewing and merging pull requests, releases and the CI setup | To be confirmed |
| **Guardrail area owners** | Keeping one guardrail area accurate and reviewed - the `owner` field in each guardrail's metadata | To be confirmed for each area |
| **Content designer** | Plain English, the [writing style](docs/contribute/index.md#writing-style) and page structure | To be confirmed |
| **Approvers for Must guardrails** | Reviewing (Technical Design Authority) and approving (Technology Governance Board) new or changed Musts | The TDA and the TGB |

`.github/CODEOWNERS` asks for a review from the right people automatically. Replace its placeholders as names are confirmed.

## Triage

- **Target:** every new issue and pull request is triaged within **two weeks**, as the site promises in [how guardrails change](docs/guardrails/index.md#how-guardrails-change).
- **Triage means:** add a type label and, where useful, an area label from [`.github/labels.yml`](.github/labels.yml); remove `needs-triage`; reply with what happens next; and close duplicates with a link to the original.
- **Open questions:** an issue that answers a "To be confirmed" box gets the `open-question` label. Once it is answered, the box is deleted in a pull request that closes the issue.

### Labels

| Label | Use it for |
| --- | --- |
| `needs-triage` | New and not yet looked at (added automatically by the issue forms) |
| `content` | Something wrong, unclear or out of date |
| `guardrail-change` | A new or changed guardrail |
| `must-change` | A new, stricter or relaxed Must - needs the TDA and TGB |
| `new-pattern` | A proposed architecture pattern |
| `open-question` | Answers a "To be confirmed" box |
| `feedback` | Feedback from a user of the site, by role |
| `guardrail-backlog` | An item from the [guardrail backlog](docs/about/roadmap.md#guardrail-backlog) |
| `site` | Site design, tooling, CI or tests |
| `dependencies` | Dependency updates from Dependabot |

The labels are defined in `.github/labels.yml`. A test checks that every label used in an issue form or workflow is defined there.

## Changing a Must guardrail

1. Open a pull request with the change and the `must-change` label. Do not merge it.
2. The [Technical Design Authority](docs/governance/tda.md) reviews it.
3. The [Technology Governance Board](docs/governance/tgb.md) approves or rejects it.
4. Record the decision in [`registers/approvals.yaml`](registers/approvals.yaml), merge, and release it - a new or stricter Must is a major version from 1.0.0 (minor while the site is in alpha).

Guardrail ids are stable and may be cited in contracts. Never renumber, rename or delete one.

## Deprecating a guardrail

Set `status: deprecated` and `replaced_by:` the guardrail that replaces it. Leave the guardrail on its page. The build fails if a deprecated guardrail has no replacement, or the replacement does not exist.

## Releases

Releases follow [`CHANGELOG.md`](CHANGELOG.md) and [semantic versioning](https://semver.org/). To release, rename `## [Unreleased]` to `## [X.Y.Z] - YYYY-MM-DD` and add a new empty `## [Unreleased]` section. When that reaches `main`, the release workflow tags it, builds a PDF of every guardrail and publishes a GitHub release. See [releases and versions](docs/about/releases.md).

## Cadence

| How often | What |
| --- | --- |
| Every two weeks | Triage new issues and pull requests |
| Monthly | Review open pull requests and the [open questions](docs/about/open-questions.md); release if `Unreleased` has changes |
| Quarterly | Review [guardrails health](docs/governance/guardrails-health.md) and exceptions, the [guardrail backlog](docs/about/roadmap.md#guardrail-backlog) and the roadmap |
| Yearly | Review every guardrail. CI warns about any guardrail whose `last_reviewed` date is more than 12 months old. |

## Changes from a fork

Anyone can propose a change from a fork of `DEFRA/architecture`: push a branch to the fork, then open a pull request into `DEFRA/architecture`. The checks run in the fork as well, so problems show up before the pull request is opened.

Only `DEFRA/architecture` publishes the site, makes releases and runs the weekly link check, so a fork can never overwrite the site, its own `gh-pages` branch or a release. Tests keep those workflows limited to `DEFRA/architecture`.

The repository moved from a fork in October 2026 - see [moving to the DEFRA GitHub organisation](docs/about/moving-to-defra.md).
