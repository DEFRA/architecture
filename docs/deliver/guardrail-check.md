# Check your repository automatically

<p class="lead">A GitHub Action that checks a repository against the guardrails a tool can check, and writes a report that names each guardrail. Add it on day one and fix the gaps before anyone has to ask.</p>

## What it checks

| Guardrail | Check |
| --- | --- |
| [GR-OPEN-02 Licence clearly](../guardrails/open-source.md#gr-open-02) | A `LICENCE` file with the Open Government Licence or MIT licence |
| [GR-DEV-08 Document as you go](../guardrails/software-development.md#gr-dev-08) | The README explains how to run, test and deploy the service, and links to its ADRs |
| [GR-API-02 Describe APIs with open specifications](../guardrails/apis-and-integration.md#gr-api-02) | OpenAPI 3 and AsyncAPI documents in the repository are well formed |
| [GR-OPEN-03 Publish safely](../guardrails/open-source.md#gr-open-03) | Secret scanning and push protection are on |
| [GR-DEV-03 Protect the main branch](../guardrails/software-development.md#gr-dev-03) | The default branch is protected |
| [GR-DEV-06 Manage dependencies actively](../guardrails/software-development.md#gr-dev-06) | Dependabot or Renovate is configured |
| [GR-DEV-09 Record significant decisions as ADRs](../guardrails/software-development.md#gr-dev-09) | Decision records in `docs/adr` |

Each check passes, fails or is unknown - for example when the token cannot read a repository setting, or the repository has no API. The report goes in the job summary, and the step fails only when a check fails.

The same checks are listed as the **automated check** for each guardrail in the [guardrail library](../guardrails/library.md).

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
