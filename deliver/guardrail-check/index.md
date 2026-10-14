<!-- https://defra.github.io/architecture/deliver/guardrail-check/ | maturity: prototype | site version 0.3.0 | generated from deliver/guardrail-check.md -->

# Check your repository automatically

<p class="lead">A GitHub Action that checks a repository against the guardrails a tool can check, and writes a report that names each guardrail. Add it on day one and fix the gaps before anyone has to ask.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## What it checks

| Guardrail | Check |
| --- | --- |
| [GR-OPEN-02 Licence clearly](https://defra.github.io/architecture/guardrails/open-source/#gr-open-02) | A `LICENCE` file with the Open Government Licence or MIT licence |
| [GR-DEV-08 Document as you go](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-08) | The README explains how to run, test and deploy the service, and links to its ADRs |
| [GR-API-02 Describe APIs with open specifications](https://defra.github.io/architecture/guardrails/apis-and-integration/#gr-api-02) | OpenAPI 3 and AsyncAPI documents in the repository are well formed |
| [GR-OPEN-03 Publish safely](https://defra.github.io/architecture/guardrails/open-source/#gr-open-03) | Secret scanning and push protection are on |
| [GR-DEV-03 Protect the main branch](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-03) | The default branch is protected |
| [GR-DEV-06 Manage dependencies actively](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-06) | Dependabot or Renovate is configured |
| [GR-DEV-09 Record significant decisions as ADRs](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-09) | Decision records in `docs/adr` |

Each check passes, fails or is unknown - for example when the token cannot read a repository setting, or the repository has no API. The report goes in the job summary, and the step fails only when a check fails.

The same checks are listed as the **automated check** for each guardrail in the [guardrail library](https://defra.github.io/architecture/guardrails/library/).

!!! note "Passing is not the same as meeting the guardrails"
    Most guardrails need a person to judge them - whether an API is secure, or a design suits its users. The check catches the basics so that conversations with your solution design authority can focus on what matters.

## Add it to your repository

Add a workflow such as `.github/workflows/guardrail-check.yml`:

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
          fail-on-error: "false"
```

Pin both actions to a full commit SHA, as the [Defra software development standards](https://defra.github.io/software-development-standards/) ask. Start with `fail-on-error: "false"` to see the report without blocking pull requests, then remove it once the gaps are fixed.

The README in `tools/guardrail-check` in the [repository](https://github.com/DEFRA/architecture) lists every input and explains how to run the check on your own computer.

## Ideas for more checks

Tell us which guardrails you would like checked next by [opening an issue](https://github.com/DEFRA/architecture/issues). Checks need to be reliable from the repository alone, or from settings a token can read.

