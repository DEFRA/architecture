<!-- https://defra.github.io/architecture/adr/0003-no-versioned-urls/ | maturity: published | site version 0.3.0 | generated from adr/0003-no-versioned-urls.md -->

# 0003. Release versions as tags and PDFs, not versioned URLs

- Status: Accepted
- Date: 2026-10-01
- Decided by: site maintainers
- Guardrails: GR-API-04 (met in spirit: deliberate versioning)

## Context

Contracts and assessments need to cite a fixed version of the guardrails. Tools such as mike can publish every version of a MkDocs site side by side, with the version in the address.

## Options considered

- **Versioned URLs with mike** - old versions browsable, but every address includes a version, links in decision records and other sites go stale, and several copies must stay accessible and secure.
- **Tags and an archived PDF for each release** - one live site with stable addresses, and a permanent record of each version in the repository and its releases.

## Decision

We will tag each release, attach a PDF of every guardrail to a GitHub release, and show the version in force on every page. We will not publish versioned URLs.

## Consequences

- People cite a version as its tag plus the PDF. See [contracting with this site](https://defra.github.io/architecture/partners/contracting/#cite-a-fixed-version).
- If people need to browse old versions as a website, we will revisit this decision.

