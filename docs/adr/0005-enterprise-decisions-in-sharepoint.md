# 0005. Record enterprise decisions in a SharePoint register, not in this repository

- Status: Accepted
- Date: 2026-10-02
- Decided by: site maintainers
- Guardrails: GR-DEV-09 (met)

## Context

This site said that decisions taken by the Technical Design Authority (TDA) and Technology Governance Board (TGB) were recorded in this repository. Many people who bring decisions do not use GitHub. Some decisions include information that should not be public, and Defra records management applies to them. Team decisions are different: Defra's software development standards and [GR-DEV-09](../guardrails/software-development.md#gr-dev-09) expect them to live with the code.

## Options considered

- **Everything in this repository** - one place, but it needs GitHub, is public, and sits outside Defra records management.
- **Everything in SharePoint** - easy for anyone in Defra, but team ADRs would be separated from the code they explain.
- **Team decisions in repositories, enterprise decisions in a SharePoint list** - each decision is kept where the people who use it work.

## Decision

Team and solution design authority decisions stay as ADRs in each service repository. TDA and TGB decisions are recorded in an architecture decision register, a SharePoint list on the Defra architecture SharePoint site. Anyone can raise a decision by email. A Power Automate flow adds it to the list as proposed, and an architect triages it. This site explains the route and does not hold a copy of the register.

## Consequences

- People can raise a decision without a GitHub account.
- The register's address and the owner of the flow are still to be confirmed. Until then, the site showed a holding address.
- Update, 2 October 2026: decisions are emailed to StrategicEnterpriseArchitecture@defra.gov.uk.
- This repository's own ADRs, in `docs/adr`, are about this site and stay here.
