<!-- https://defra.github.io/architecture/deliver/working-with-architects/ | maturity: prototype | site version 0.3.0 | generated from deliver/working-with-architects.md -->

# Working with architects

<p class="lead">For service designers, interaction designers, content designers and user researchers: when to involve an architect, what to bring, and what you can expect in return.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



## Why this matters to designers and researchers

Many decisions that shape the user experience are architecture decisions too. They are cheap to change in discovery and alpha, and expensive afterwards. For example:

- **Sign-in and acting on behalf of others** - who can do what for which business or holding. See [acting on behalf of an organisation or holding](https://defra.github.io/architecture/patterns/acting-on-behalf/).
- **A forms platform or a bespoke front end** - what you can design depends on the choice. See [GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04).
- **Processing in the background** - whether users get an answer straight away or a reference number and an email later. See [asynchronous submission](https://defra.github.io/architecture/patterns/async-submission/).
- **Uploading files** - what users wait for while files are checked, and what happens when one is rejected. See [file upload with malware scanning](https://defra.github.io/architecture/patterns/file-upload/).
- **Working offline** - what field users can do without a signal. See [field working and devices](https://defra.github.io/architecture/guardrails/field-working-and-devices/).
- **AI** - what users are told, and how they challenge a decision. See [GR-AI-03](https://defra.github.io/architecture/guardrails/ai/#gr-ai-03) and [GR-AI-04](https://defra.github.io/architecture/guardrails/ai/#gr-ai-04).

If you design or research any of these, involve an architect early. The guardrails each role leads are on the pages for [service designers](https://defra.github.io/architecture/deliver/roles/service-designer/), [interaction designers](https://defra.github.io/architecture/deliver/roles/interaction-designer/), [content designers](https://defra.github.io/architecture/deliver/roles/content-designer/) and [user researchers](https://defra.github.io/architecture/deliver/roles/user-researcher/).

## When to involve an architect, and what to bring

This page covers the architecture touchpoints only. For your own discipline, use the Defra Digital Service Manual: [design](https://digital.defra.gov.uk/design), [user research](https://digital.defra.gov.uk/user-research) and [content design](https://digital.defra.gov.uk/content), including what content designers do in [discovery](https://digital.defra.gov.uk/content/working-in-discovery), [alpha](https://digital.defra.gov.uk/content/working-in-alpha), [beta](https://digital.defra.gov.uk/content/working-in-beta) and [live](https://digital.defra.gov.uk/content/working-in-live).

### Discovery

Bring:

- the current journey, mapped against the systems, teams and organisations behind each step
- the information you ask users for, so an architect can tell you what Defra already holds and where the [authoritative sources](https://defra.github.io/architecture/data/defra-on-a-page/) are ([GR-DATA-02](https://defra.github.io/architecture/guardrails/data/#gr-data-02), [GR-DATA-04](https://defra.github.io/architecture/guardrails/data/#gr-data-04))
- what you are learning about users' devices, connectivity and who acts for whom

### Alpha

Bring:

- your riskiest assumptions on the user side, so you can test them alongside the riskiest technical assumptions rather than separately
- the prototypes that depend on a technical choice, such as sign-in, file upload or a forms platform - prototype these on the real platforms where it matters, so research tests what users will actually get
- anything that would mean departing from the [GOV.UK Design System](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-02)

### Beta

Bring:

- what users see when a dependency is slow or fails, such as a payment provider or a back-office system, and the content for it ([GR-OPS-04](https://defra.github.io/architecture/guardrails/observability-and-operations/#gr-ops-04))
- confirmation and status content: what happens next, how long it takes and how users find out - based on how long processing really takes
- findings from research with assistive technology users that need a technical fix

### Live

Bring:

- how you will tell users about incidents and planned downtime, and who sends those messages
- research findings that point to a change in how the service works, not just how it looks - these may be a [significant change](https://defra.github.io/architecture/deliver/significant-change/)

## What architects do in return

Architects working with your team should:

- **come to show and tells and research playbacks**, so they hear from users directly
- **join design critiques** for journeys with technical constraints, such as sign-in, payments or file upload
- **record decisions that affect the user experience as ADRs**, with the designer or researcher named as a contributor, so the reasons are kept alongside the technical ones - see [architecture decision records](https://defra.github.io/architecture/governance/architecture-decision-records/)
- **explain constraints in plain English**, and say which ones are fixed and which can be challenged
- **raise it early** when a technical decision will change what users see

## How to ask

- **If your team has an architect**, talk to them first.
- **If not**, contact the Delivery Architecture team at [delivery.architecture@defra.gov.uk](mailto:delivery.architecture@defra.gov.uk). They will tell you the principal architect for your delivery group. See [architecture](https://digital.defra.gov.uk/architecture) in the Defra Digital Service Manual.
- You can also use the routes on [the architecture team](https://defra.github.io/architecture/about/team/) page, which describes the architecture drop-in sessions.

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** when and where the architecture drop-in sessions run, and how designers and researchers book them.

