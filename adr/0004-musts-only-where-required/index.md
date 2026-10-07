<!-- https://defra.github.io/architecture/adr/0004-musts-only-where-required/ | maturity: published | site version 0.3.0 | generated from adr/0004-musts-only-where-required.md -->

# 0004. Keep Must guardrails to what is required

- Status: Accepted
- Date: 2026-10-02
- Decided by: site maintainers, at the request of the site owner
- Guardrails: all guardrail levels

## Context

By October 2026 the site had 55 Must guardrails out of 99, and alpha alone listed 37 Musts. Every Must that a team cannot meet needs an approved exception, so a long list of Musts makes governance heavier, encourages box-ticking and hides the few requirements that really matter. The guardrails are new and have not yet been tested with teams.

## Options considered

- **Keep the Musts as they are** - clear, but heavy, and likely to generate many exceptions before we know which rules are right.
- **Keep Musts only where they are required** - lighter, and easier to defend; some good practice becomes a Should until experience shows it needs to be a Must.

## Decision

A guardrail is a Must only where at least one of these is true:

1. **law or mandatory government policy** requires it - for example accessibility, data protection, records management, the Welsh Language Standards, coding in the open, the Algorithmic Transparency Recording Standard and spend control
2. it is a **baseline security control** - for example Secure by Design, threat modelling, encryption, secrets, least privilege, security testing and monitoring
3. it puts a **DDTS doctrine non-negotiable** into practice - for example the strategic platforms, the strategic identity services and looking for something to reuse first

Everything else is a Should. We changed 26 Musts to Shoulds and kept 29.

## Consequences

- Departing from a Should needs a recorded reason in an ADR, not an exception, so governance is lighter.
- Guardrail ids, statements and evidence did not change. Only the level changed.
- We will make a guardrail a Must again when feedback, exceptions or incidents show teams need it - through [how guardrails change](https://defra.github.io/architecture/guardrails/#how-guardrails-change).
- New guardrails start as Shoulds unless one of the three tests above applies.

