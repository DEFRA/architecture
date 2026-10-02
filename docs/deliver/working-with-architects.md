# Working with architects

<p class="lead">For service designers, interaction designers, content designers and user researchers: when to involve an architect, what to bring, and what you can expect in return.</p>

## Why this matters to designers and researchers

Many decisions that shape the user experience are architecture decisions too. They are cheap to change in discovery and alpha, and expensive afterwards. For example:

- **Sign-in and acting on behalf of others** - who can do what for which business or holding. See [acting on behalf of an organisation or holding](../patterns/acting-on-behalf.md).
- **A forms platform or a bespoke front end** - what you can design depends on the choice. See [GR-FE-04](../guardrails/front-end-and-accessibility.md#gr-fe-04).
- **Processing in the background** - whether users get an answer straight away or a reference number and an email later. See [asynchronous submission](../patterns/async-submission.md).
- **Uploading files** - what users wait for while files are checked, and what happens when one is rejected. See [file upload with malware scanning](../patterns/file-upload.md).
- **Working offline** - what field users can do without a signal. See [field working and devices](../guardrails/field-working-and-devices.md).
- **AI** - what users are told, and how they challenge a decision. See [GR-AI-03](../guardrails/ai.md#gr-ai-03) and [GR-AI-04](../guardrails/ai.md#gr-ai-04).

If you design or research any of these, involve an architect early. The guardrails each role leads are on the pages for [service designers](roles/service-designer.md), [interaction designers](roles/interaction-designer.md), [content designers](roles/content-designer.md) and [user researchers](roles/user-researcher.md).

## When to involve an architect, and what to bring

This page covers the architecture touchpoints only. For how to run each phase and do research, use the [Defra Digital Service Manual](https://digital.defra.gov.uk/service-manual) and the [GOV.UK Service Manual](https://www.gov.uk/service-manual).

### Discovery

Bring:

- the current journey, mapped against the systems, teams and organisations behind each step
- the information you ask users for, so an architect can tell you what Defra already holds and where the [authoritative sources](../data/defra-on-a-page.md) are ([GR-DATA-02](../guardrails/data.md#gr-data-02), [GR-DATA-04](../guardrails/data.md#gr-data-04))
- what you are learning about users' devices, connectivity and who acts for whom

### Alpha

Bring:

- your riskiest assumptions on the user side, so you can test them alongside the riskiest technical assumptions rather than separately
- the prototypes that depend on a technical choice, such as sign-in, file upload or a forms platform - prototype these on the real platforms where it matters, so research tests what users will actually get
- anything that would mean departing from the [GOV.UK Design System](../guardrails/front-end-and-accessibility.md#gr-fe-02)

### Beta

Bring:

- what users see when a dependency is slow or fails, such as a payment provider or a back-office system, and the content for it ([GR-OPS-04](../guardrails/observability-and-operations.md#gr-ops-04))
- confirmation and status content: what happens next, how long it takes and how users find out - based on how long processing really takes
- findings from research with assistive technology users that need a technical fix

### Live

Bring:

- how you will tell users about incidents and planned downtime, and who sends those messages
- research findings that point to a change in how the service works, not just how it looks - these may be a [significant change](significant-change.md)

## What architects do in return

Architects working with your team should:

- **come to show and tells and research playbacks**, so they hear from users directly
- **join design critiques** for journeys with technical constraints, such as sign-in, payments or file upload
- **record decisions that affect the user experience as ADRs**, with the designer or researcher named as a contributor, so the reasons are kept alongside the technical ones - see [architecture decision records](../governance/architecture-decision-records.md)
- **explain constraints in plain English**, and say which ones are fixed and which can be challenged
- **raise it early** when a technical decision will change what users see

## How to ask

- **If your team has an architect**, talk to them first.
- **If not**, ask your delivery manager to put you in touch with your [solution design authority](../governance/solution-design-authorities.md), or use the routes on [the architecture team](../about/team.md) page, which also describes the architecture drop-in sessions.

!!! warning "To be confirmed"
    **TODO:** when and where the architecture drop-in sessions run, how designers and researchers book them, and the channel to use to ask an architect a question.
