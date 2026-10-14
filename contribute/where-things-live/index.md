<!-- https://defra.github.io/architecture/contribute/where-things-live/ | maturity: draft | site version 0.3.0 | generated from contribute/where-things-live.md -->

# Where things live

<p class="lead">Where to find the guidance, where to suggest a change and where work is tracked - and how this site and the Defra Digital Service Manual share the work, so each fact has one home.</p>

!!! warning "Draft - to be confirmed"
    Parts of this page, such as names, timings and thresholds, are still being confirmed by the architecture team. Use it as a guide, and check with your solution design authority before relying on the detail.



## Where to find and change things

All guidance lives in this repository and is published as this site. Everything else is for talking about it and tracking changes to it.

| Place | Use it to | Who uses it |
| --- | --- | --- |
| **This site** | Read the guidance. It is the published version of the repository. | Everyone |
| **[The repository](https://github.com/DEFRA/architecture)** | Change the guidance through a pull request, and see who changed what and why in the history. | Contributors and maintainers |
| **[Issues](https://github.com/DEFRA/architecture/issues)** | Report a mistake, suggest a change, answer an open question, or pick up an item from the [guardrail backlog](https://defra.github.io/architecture/about/roadmap/#guardrail-backlog). One issue for each piece of work. | Anyone with a GitHub account |
| **GitHub Project** | See what is planned, in progress and done across all issues and pull requests. The [roadmap](https://defra.github.io/architecture/about/roadmap/) links to it. | Maintainers, and anyone following progress |
| **Discussions** | Ask a question or float an idea before it is ready to be an issue. | Anyone with a GitHub account |
| **[Releases](https://github.com/DEFRA/architecture/releases)** | Find a fixed version and its PDF to cite in a contract. | Commercial and delivery partners |

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** turn on Issues and Discussions for the repository, switch off the wiki, create the GitHub Project for the roadmap, and add their addresses here and on the roadmap.

### Why we do not use the GitHub wiki

We do not use the repository's GitHub wiki, and guidance never goes there:

- **Wiki edits skip review.** Changes here go through a pull request that someone else approves.
- **Wiki edits skip the checks.** Every pull request is checked for broken links, accessibility, unchanged guardrail ids and missing evidence. A wiki has none of these.
- **The wiki is not versioned with releases.** A contract cites a release; a wiki page could change underneath it.
- **The wiki is not part of this site.** People would have to search two places, and the two would drift apart.

If you find guidance that only exists somewhere else, such as a wiki, a slide deck or a SharePoint page, raise an issue to bring it here or link to it from here.

## This site or the manual?

| Put it in the [Defra Digital Service Manual](https://digital.defra.gov.uk/) | Put it on this site |
| --- | --- |
| How to do a task, step by step | Guardrails: what a service must, should or could do, and why |
| Who to contact, team mailboxes and support channels | Architecture decisions, and how to raise one |
| How to use a common tool or platform | Which platform or capability to use, and when an exception is needed |
| Service assessments, delivery governance and assurance processes | The evidence architecture asks for in each phase |
| Design, content, research, accessibility and sustainability practice | The architecture choices that make that practice possible |

If you find the same fact in both places, keep it where the table says it belongs and link to it from the other. If the two disagree, the owner of the fact decides; until then, add a "To be confirmed" box on this site.

## Matching links

At each of these points, this site links to the manual. A test checks that the page on this site still links to the manual page, and the link check checks the manual page still exists.

| Topic | On this site | In the manual |
| --- | --- | --- |
| Getting architecture help | [The architecture team](https://defra.github.io/architecture/about/team/) | [Architecture](https://digital.defra.gov.uk/architecture) |
| Working with architects | [Working with architects](https://defra.github.io/architecture/deliver/working-with-architects/) | [Architecture](https://digital.defra.gov.uk/architecture) |
| Approved technologies | [GR-DEV-01](https://defra.github.io/architecture/guardrails/software-development/#gr-dev-01) | [Approved technologies and languages](https://digital.defra.gov.uk/software-development#approved-technologies-and-languages) |
| Core Delivery Platform | [GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01) | [Core Delivery Platform](https://digital.defra.gov.uk/architecture-and-software-development/core-delivery-platform) |
| Platforms and common tools | [Getting onto Defra platforms](https://defra.github.io/architecture/deliver/platforms/) | [Defra Interactive Map](https://digital.defra.gov.uk/architecture-and-software-development/defra-accessible-maps) |
| Sign-in | [GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01) | [Defra Customer Identity](https://digital.defra.gov.uk/architecture-and-software-development/defra-customer-identity) |
| Forms | [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04) | [Defra Forms](https://digital.defra.gov.uk/architecture-and-software-development/defra-forms) |
| Accessibility | [GR-FE-01](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-01) | [Make sure everyone can use the service](https://digital.defra.gov.uk/accessibility) |
| Sustainability | [Sustainability guardrails](https://defra.github.io/architecture/guardrails/sustainability/) | [Deliver a sustainable service](https://digital.defra.gov.uk/sustainability) |
| AI | [AI guardrails](https://defra.github.io/architecture/guardrails/ai/) | [AI digital toolkit](https://digital.defra.gov.uk/ai-toolkit) |
| User research data | [GR-DATA-10](https://defra.github.io/architecture/guardrails/data/#gr-data-10) | [User research standards and guidance](https://digital.defra.gov.uk/user-research/standards-and-guidance) |
| Security | [Secure by Design](https://defra.github.io/architecture/security/secure-by-design/) | [Security](https://digital.defra.gov.uk/security) |
| Service assessments | [Deliver a service](https://defra.github.io/architecture/deliver/) | [Service assessments](https://digital.defra.gov.uk/service-assessments) |
| Delivery group governance | [Solution design authorities](https://defra.github.io/architecture/governance/solution-design-authorities/) | [Governance model](https://digital.defra.gov.uk/delivery-groups/follow-delivery-governance/governance-model) |
| Non-functional requirements | [Non-functional requirements](https://defra.github.io/architecture/nfrs/) | [Non-functional requirements](https://digital.defra.gov.uk/business-analysis/non-functional-requirements) |
| Design patterns | [Architecture patterns](https://defra.github.io/architecture/patterns/) | [Components and patterns](https://digital.defra.gov.uk/design/components-and-patterns) |

<div id="tbc-2"></div>

!!! warning "To be confirmed"
    **TODO:** whether the Defra Digital Service Manual will link back to this site at the matching points, and who owns that change in the manual.

