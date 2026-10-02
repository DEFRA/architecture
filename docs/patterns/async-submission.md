---
pattern:
  category: integration
  status: draft
  summary: A user submits something that other systems must process, and you do not want those systems' availability to block the user.
  guardrails: [GR-API-05, GR-API-06, GR-API-02, GR-OPS-04, GR-OPS-02]
  sbd: [security-patterns, stride-template]
  user_experience: written
---

# Asynchronous submission with an outbox

<p class="lead">Accept a user's submission straight away, store it safely, and hand it to other systems through events - so a slow or broken back office never stops a user from applying.</p>

## Context

Most Defra transactional services end with the user submitting something: an application, a claim, a notification. Behind the service sit case management, payments, the data platform and sometimes legacy systems. They are not always available, and they are often slow.

If the front end waits for each of them before telling the user "submitted", any one of them can stop the user finishing. If the service saves the submission and then publishes an event in a separate step, a failure between the two loses the event: the submission exists, but nothing downstream ever hears about it.

## Solution

Save the submission and an **outbox record** in the same database transaction. A separate **relay** reads the outbox and publishes each record as an event to the platform's messaging, marking it as sent once the broker confirms. Consumers - case management, the data platform, notifications - subscribe to the event and process it in their own time.

```mermaid
flowchart LR
    accTitle: Asynchronous submission with an outbox
    accDescr: The user submits to the service API, which saves the submission and an outbox record in one transaction and confirms to the user. A relay reads the outbox and publishes an event to messaging. Case management, the data platform and notifications each consume the event independently. Failed messages go to a dead letter queue that is monitored.
    U(["User"]) -->|"submit"| API["Service API"]
    subgraph TX["One database transaction"]
        S[("Submissions")]
        O[("Outbox")]
    end
    API --> S
    API --> O
    API -->|"reference number"| U
    O --> R["Relay"]
    R -->|"application-submitted event"| M["Messaging<br/>TC22"]
    M --> C["Case management"]
    M --> D["Data platform"]
    M --> N["Notifications"]
    M -.->|"failures"| DLQ[("Dead letter queue,<br/>monitored")]
```

How it works:

1. The service validates the submission and saves it, with an outbox record describing the event, in **one transaction**. Either both are saved or neither is.
2. The user gets a reference number immediately. The confirmation page says what happens next and when.
3. The relay publishes outbox records in order and retries until the broker acknowledges them.
4. Consumers are **idempotent**: they use the event id to ignore duplicates, because the relay can publish a message more than once.
5. Messages that keep failing go to a dead letter queue, which raises an alert.

Describe the event in [AsyncAPI](https://www.asyncapi.com/) in the service repository. Put enough in the event for consumers to act - usually an id, type, time, version and a reference to the submission - and avoid copying personal data into it unless consumers need it.

## What users see

The user submits and gets an answer straight away, even if the systems behind the service are slow or down.

- **A confirmation page with a reference number**, shown as soon as the submission is saved. Use the GOV.UK Design System [confirmation pages](https://design-system.service.gov.uk/patterns/confirmation-pages/) pattern and its [panel](https://design-system.service.gov.uk/components/panel/). The reference comes from the service, not from case management, so it is available even when case management is not.
- **What happens next, and how long it takes.** For example: "We will review your application and email you within 10 working days." Use the real time, agreed with the team that does the work.
- **A confirmation email** with the reference number, sent through the notifications consumer. It may arrive a few minutes after the page.
- **The status of their submission**, if the service lets users come back. While events are still being processed, show the last status you know, not an error. The [tag](https://design-system.service.gov.uk/components/tag/) component works for statuses such as "Received" and "In review".

What users do not see: the outbox, the relay or the queue. If a consumer is down, the user's journey does not change. Only the time until someone acts on the submission does.

## Content to design

| Situation | What to tell users |
| --- | --- |
| **Submitted** | The reference number, what happens next, how long it takes, and how to contact you quoting the reference. Say whether they need to do anything else. |
| **How long it takes** | A real time, such as "within 10 working days", agreed with the people who process submissions. Do not promise "instantly" because the screen said "submitted". |
| **Processing is delayed** | If a backlog builds up in the queue or the case team, say so on the status page and in any chase emails, with a new expected date. Do not leave an old date showing. |
| **Duplicate submission** | If the user submits twice, for example by pressing the button again or using the back button, show the original confirmation and reference rather than creating a second application. Tell them: "You have already submitted this application. Your reference number is …". |
| **Something went wrong after submission** | If a later step fails and the user needs to act, contact them using the reference number and explain what to do. Never ask them to submit again from scratch. |
| **The service itself is down** | Use the [service unavailable pages](https://design-system.service.gov.uk/patterns/service-unavailable-pages/) pattern, and say whether anything they had already saved is kept. |

Write the confirmation email and status messages with the content designer, using the processing times the operations team gives you. Do not guess them.

## What to test with users

- Do users understand that their application is **submitted**, and that **nothing more is needed** unless you ask?
- Do they **keep the reference number**, and know how to use it if they contact you?
- Is the **time to expect a decision** clear, and is it what they expected? What do they do if they hear nothing by then?
- When processing is **delayed**, do the status page and emails reassure them, or do they phone, email or submit again?
- If they **press submit twice** or come back with the back button, do they understand they already submitted, and with which reference?
- For agents submitting many applications, can they **match each confirmation to the right customer**?

Test the delay and duplicate journeys in a prototype; they are easy to miss in research that only follows the happy path.

## Guardrails it helps you meet

<!-- patterns:guardrails -->

## Related Secure by Design artefacts

<!-- patterns:sbd -->

Threats to consider in your [threat model](../security/threat-modelling.md): spoofed or tampered events, replayed messages, personal data in messages and logs, and an attacker filling the queue. Authenticate publishers and consumers, and encrypt messages in transit and at rest.

## When not to use it

- **The user needs the answer now.** If the outcome is decided instantly - an eligibility check, a postcode lookup - call the API synchronously and handle failure in the journey.
- **There is only one consumer and it is always available**, such as a database the service owns. The outbox adds moving parts for no benefit.
- **You need a transaction across services.** An outbox does not give you that. Design compensating actions (a saga) instead, and record the decision in an ADR.

## Related

- [Transactional digital service](../handrail/reference-architectures/transactional-service.md) reference architecture
- [Worked example: apply for a licence](worked-example/index.md), which uses this pattern
