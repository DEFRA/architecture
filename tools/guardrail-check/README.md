# Guardrail check

A GitHub Action that checks a repository against the [Defra architecture guardrails](https://defra.github.io/architecture/guardrails/library/) that can be checked automatically, and writes a Markdown report to the job summary.

| Guardrail | What is checked |
| --- | --- |
| [GR-OPEN-02](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) | A `LICENCE` or `LICENSE` file with the Open Government Licence or MIT licence |
| [GR-DEV-08](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) | The README has sections on running, testing and deploying, and mentions its ADRs |
| [GR-API-02](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) | OpenAPI 3 and AsyncAPI documents in the repository parse and have the basic required fields |
| [GR-OPEN-03](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) | Secret scanning and push protection are on (needs a token that can read security settings) |
| [GR-DEV-03](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) | The default branch is protected by branch protection or a ruleset |
| [GR-DEV-06](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-06) | Dependabot or Renovate is configured |
| [GR-DEV-09](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) | A `docs/adr` folder with at least one decision record |

Each check **passes**, **fails** or is **unknown** - for example when the token cannot read a setting, or no API specification exists. Only failures fail the step. Passing these checks does not mean a service meets the guardrails: most guardrails need a person to judge them.

## Use it

Add a workflow to your repository. Pin the action to a full commit SHA, as the [Defra software development standards](https://defra.github.io/software-development-standards/) ask:

```yaml
name: guardrail-check
on:
  pull_request:
  schedule:
    - cron: "0 7 * * 1"
permissions:
  contents: read
jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<commit SHA> # v7.0.1
      - uses: DEFRA/architecture/tools/guardrail-check@<commit SHA> # v0.3.0
        with:
          fail-on-error: "false"   # report only, while you fix the gaps
```

| Input | Default | Meaning |
| --- | --- | --- |
| `path` | `.` | Folder of the checked-out repository |
| `repository` | the current repository | `owner/name`, for the settings checks |
| `token` | `github.token` | Token for reading settings. The default token cannot read security settings, so GR-OPEN-03 is reported as unknown unless you pass a token with administration read access. |
| `fail-on-error` | `true` | Fail the step when a check fails |

## Run it locally

```bash
pip install pyyaml
GITHUB_TOKEN=... python tools/guardrail-check/check.py --path ../my-service --repo DEFRA/my-service
```

The tests are in `tests/test_guardrail_check.py`.
