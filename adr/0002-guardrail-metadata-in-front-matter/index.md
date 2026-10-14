<!-- https://defra.github.io/architecture/adr/0002-guardrail-metadata-in-front-matter/ | maturity: published | site version 0.3.0 | generated from adr/0002-guardrail-metadata-in-front-matter.md -->

# 0002. Keep guardrail metadata in each page's front matter

- Status: Accepted
- Date: 2026-10-01
- Decided by: site maintainers
- Guardrails: GR-DEV-08 (met)

## Context

Each guardrail needs structured metadata - status, phases, evidence, automated check, mappings to the Service Standard, Technology Code of Practice and Secure by Design, owner and dates - so that phase pages, checklists, the library and contracts can be generated from it.

## Options considered

- **Front matter on each guardrail page** - the data sits next to the prose it describes, and one pull request changes both.
- **A separate YAML file per area** - tidier pages, but the data and prose drift apart and reviewers must look in two places.
- **One big data file** - easy for tools, hard for people to review.

## Decision

We will keep metadata in a `guardrails:` block in each page's front matter, with shared values in `guardrail_defaults`. `hooks/guardrails.py` validates it and publishes it as `guardrails.json` for tools.

## Consequences

- The build fails if a guardrail has no metadata, a value is unknown, or a Must has no evidence.
- Front matter on guardrail pages is long. The contribution guide explains each field.

