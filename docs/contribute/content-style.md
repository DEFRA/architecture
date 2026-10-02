---
status: draft
---

# Content style

<p class="lead">How we write for this site, so every page reads the same way and busy delivery teams find what they need quickly. It builds on the GOV.UK style guide; it only adds what is specific to this site.</p>

## House rules

We follow the [GOV.UK style guide](https://www.gov.uk/guidance/style-guide) and [writing for GOV.UK](https://www.gov.uk/guidance/content-design/writing-for-gov-uk). On top of that:

- **Lead with what the reader needs to do.** Put the action first and the background after.
- **Plain English, short sentences, active voice.** "The TDA reviews it", not "it is reviewed by the TDA".
- **Sentence case for every heading, title and button**, including page titles and table headings. Keep capitals for proper nouns, such as Defra, GOV.UK and Core Delivery Platform.
- **Expand an abbreviation the first time you use it on a page**, for example "Technical Design Authority (TDA)", and add it to `includes/abbreviations.md` - see [add an abbreviation](index.md#add-an-abbreviation).
- **Never guess a Defra fact.** If you do not know a name, contact, address, lead time, approval or product name, write a "To be confirmed" box instead - see [flag a fact that is not confirmed](index.md#flag-a-fact-that-is-not-confirmed). Every box is listed on the [open questions](../about/open-questions.md) page.
- **Link, do not repeat.** If the [Defra Digital Service Manual](https://digital.defra.gov.uk/) or GOV.UK already says it, link to it. See [where things live](where-things-live.md).
- **Descriptive link text.** Say where the link goes ("see [service tiers](../nfrs/service-tiers.md)"), never `click here` or `read more`.
- **Dates and numbers:** write dates as "2 October 2026", use numerals for numbers, and "to" rather than a dash in ranges ("10 to 15 days").
- **No `please`, `simply`, `just` or `obviously`**, and avoid `e.g.` and `i.e.` - write "for example" and "that is".
- **Must, Should and Could** have the meanings in [how to read a guardrail](../guardrails/index.md#how-to-read-a-guardrail). Do not use them loosely elsewhere.

## How to write a guardrail

The mechanics - front matter, ids and metadata - are in [add or change a guardrail](index.md#add-or-change-a-guardrail). For the words:

- **Title:** a short instruction in sentence case, starting with a verb where you can - "Protect the main branch", not "Main branch protection".
- **Statement:** one or two sentences saying what a team does, in the active voice, that a team could show it has met. Avoid "should" in a Must, and "must" in a Should.
- **Why:** the reason in one or two sentences, in terms of users, risk or cost. If it comes from law or mandatory policy, name it.
- **How to meet it:** practical steps a team can take themselves, linking to the platform, pattern or manual page that helps.
- **Evidence:** what a team shows at an assessment, specific to each phase - an intent in discovery, a design in alpha, something built and tested in beta, and how it is operated in live.
- **New guardrails** take the next free id in their area, start as `status: draft` and end with the "draft proposal" line asking for comments.

## How to write a pattern

Follow [add a pattern](index.md#add-a-pattern). A pattern describes a proven technical solution, so:

- **Context:** the problem, in a Defra setting, in two or three short paragraphs.
- **Solution:** one diagram and numbered steps a team can follow.
- **What users see, content to design and what to test with users:** written with a designer, a content designer and a user researcher. Link to [GOV.UK Design System](https://design-system.service.gov.uk/) patterns where they exist; never invent one.
- **When not to use it:** be honest about where it does not fit.

## Diagrams

- Use a `mermaid` block, and give every diagram an `accTitle` and an `accDescr` that describes what it shows in full sentences, for people using screen readers. The tests fail without them.
- Show the real mechanism - what calls what, and in which order - rather than a cloud of boxes.
- Label boxes in sentence case with the names used elsewhere on the site, such as the capability or platform name.
- Keep a diagram to about a dozen boxes. Split it if it needs more.
- Do not rely on colour alone to carry meaning.

## Glossary

Terms we use with a specific meaning on this site. Definitions of services and capabilities are still being agreed, so they live on [services and capabilities](../handrail/services-and-capabilities.md), which uses Defra's service taxonomy.

| Term | Meaning on this site |
| --- | --- |
| **DDTS doctrine** | The non-negotiables that guide all Digital, Data and Technology Services work - see [DDTS doctrine](../principles/doctrine.md) |
| **Architecture principle** | How the doctrine applies to technology change - see [architecture principles](../principles/architecture-principles.md) |
| **Guardrail** | A default every team follows, labelled Must, Should or Could, with a stable id such as GR-HOST-01 |
| **Handrail** | The capability models and reference architectures that help teams find what already exists - see [the handrail](../handrail/index.md) |
| **Business capability** | What Defra does, independent of how - see [business capabilities](../handrail/business-capabilities.md) |
| **Technology capability** | The technology that supports business capabilities, with Defra's strategic option for each - see [technology capabilities](../handrail/technology-capabilities.md) |
| **Architecture pattern** | A proven technical solution to a recurring problem - see [architecture patterns](../patterns/index.md). Not the same as the design patterns in the Defra Digital Service Manual. |
| **Reference architecture** | A starting design for a common kind of service, built from the capabilities and patterns |
| **Architecture decision record (ADR)** | A short record of one significant decision, its options and consequences - see [architecture decision records](../governance/architecture-decision-records.md) |
| **Exception** | An agreed, time-limited departure from a Must guardrail - see [exceptions](../governance/exceptions.md) |
| **Solution design authority (SDA)** | Where a principal architect assures decisions for a delivery group, with authority from the TDA - see [solution design authorities](../governance/solution-design-authorities.md) |
| **Service tier** | How critical a service is, which sets its non-functional requirements - see [service tiers](../nfrs/service-tiers.md) |
| **Open question** | A fact we do not know yet, shown in a "To be confirmed" box and listed on [open questions](../about/open-questions.md) |

## Prose checks

Every pull request runs two prose checks and shows what they find as **warnings** on the pull request. They never stop a merge: a reviewer decides whether to change the wording.

| Check | What it looks for | Run it locally |
| --- | --- | --- |
| [Vale](https://vale.sh/), with the house rules in `.vale/styles/Defra` | Words to avoid, filler words such as `please` and `simply`, and exclamation marks | [Install Vale](https://vale.sh/docs/install), then `vale docs` |
| `scripts/heading_case.py` | Headings that are not in sentence case | `python scripts/heading_case.py` |

If a check flags a proper noun, add it to the exceptions - `PROPER_NOUNS` in `scripts/heading_case.py`, or the vocabulary in `.vale/styles/config/vocabularies/Defra/accept.txt` - rather than changing the name. The doctrine and principles use Defra's agreed wording, so Vale does not suggest rewording them.
