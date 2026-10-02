## What does this change?

<!-- One or two sentences. Link the issue it closes, for example "Closes #12". -->

## Type of change

- [ ] Content correction or clarification
- [ ] New or changed guardrail
- [ ] New, stricter or relaxed **Must** guardrail - needs TDA review and TGB approval before merging (see MAINTAINERS.md)
- [ ] New or changed NFR or service tier
- [ ] Pattern or capability model change
- [ ] Answers an open question
- [ ] Site design, tooling or tests

## Checklist

- [ ] **Guardrail ids unchanged** - no id renumbered, renamed, deleted or reused. New guardrails take the next free id and start as `status: draft`.
- [ ] **Changelog updated** - significant changes are in `CHANGELOG.md` under `Unreleased` and in `docs/about/changelog.md`.
- [ ] **All checks run locally** - `ruff check`, `npm run lint`, `pytest`, `mkdocs build --strict` and, for page or style changes, `npm test`.
- [ ] **No guesses** - any Defra fact I could not confirm (a name, contact, address, lead time, approval or product) is in a "To be confirmed" box, not made up.
- [ ] Plain English, following the [content style](https://howellsr.github.io/architecture/contribute/content-style/).
- [ ] No secrets, internal hostnames, personal data or sensitive security detail.
