<!-- https://defra.github.io/architecture/adr/0001-mkdocs-material-with-hooks/ | maturity: published | site version 0.3.0 | generated from adr/0001-mkdocs-material-with-hooks.md -->

# 0001. Build the site with MkDocs Material and generate lists with hooks

- Status: Accepted
- Date: 2026-10-01
- Decided by: site maintainers
- Guardrails: GR-TECH-01 (met), GR-OPEN-01 (met), GR-FE-01 (met)

## Context

The site needs to be easy for architects, designers and partners to edit in pull requests, accessible, searchable, and published in the open. Much of it is lists - guardrails, capabilities, NFRs, checklists - that drift if they are maintained by hand in several places.

## Options considered

- **MkDocs with Material for MkDocs** - Markdown in the repository, good accessibility and search, widely used across government documentation.
- **A content management system** - easier for some editors, but no review in pull requests and harder to keep in the open.
- **A custom static site generator** - full control, but more to build and support.

## Decision

We will use MkDocs and Material for MkDocs, with small Python hooks in `hooks/` that read YAML data and page front matter to generate lists, tables and checklists, and fail the build when references are broken.

## Consequences

- Generated content is never edited by hand: change the data and the page follows.
- Material for MkDocs is pinned at 9.7.7 because MkDocs 2.0 removes the plugin system the site depends on. Revisit when Material publishes a supported upgrade path.

