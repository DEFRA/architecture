# 0006. Move the site to DEFRA/architecture

- Status: Accepted
- Date: 2026-10-02
- Decided by: site maintainers
- Guardrails: GR-DEV-02 (met)

## Context

The site was built in howellsr/architecture, a personal fork of the existing `DEFRA/architecture` repository, and published at howellsr.github.io/architecture. [GR-DEV-02](../guardrails/software-development.md#gr-dev-02) asks for all code to be in a Defra-owned GitHub organisation, and the site is starting to be cited. Because `DEFRA/architecture` already exists, the personal repository cannot be transferred to that name.

## Options considered

- **Transfer the fork to another name in the DEFRA organisation** - keeps the fork's issues and releases, but leaves the existing `DEFRA/architecture` repository behind and gives the site an unexpected name.
- **Merge the fork's history into `DEFRA/architecture` through a pull request** - keeps every commit and decision record under the expected name. Releases, pull request discussions and the v0.2.0 PDF stay with the fork.
- **Use a custom domain now** - the most stable address, but needs a decision on the domain, which is not yet agreed.

## Decision

We will merge the fork's history into `DEFRA/architecture` and publish the site at <https://defra.github.io/architecture/>. The fork is archived, not deleted, and serves redirect pages from its old address. A custom domain will be considered at beta.

## Consequences

- Old links keep working through redirects, and v0.2.0 stays citable at its original address.
- The first release from `DEFRA/architecture` is 0.3.0.
- Pull request history before the move is only visible in the archived fork.
- If a custom domain is adopted later, `site_url` changes once more and the redirect script is reused.
