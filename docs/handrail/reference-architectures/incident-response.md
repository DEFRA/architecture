---
status: draft
status_note: "This is a proposed reference architecture for a capability Defra does not yet have a strategic solution for. It is a starting point for discussion, not an agreed design. Talk to the architecture team before building on it."
---

# Incident response (proposed)

<p class="lead">A proposed starting shape for detecting, coordinating and reporting on incidents such as animal and plant disease outbreaks, floods and pollution events.</p>

**Technology capability:** [TC12 Incident and emergency management](../technology-capabilities.md#tc12), currently a **gap**. **Typical business capability:** [08 Respond to incidents and crises](../business-capabilities.md#bc08).

## Context

Defra and its arm's length bodies respond to incidents that can grow from one report to a national emergency in days. Responders need a shared picture: what has been reported, where, what is being done, and by whom. Systems must scale quickly, work with partners outside Defra, and keep working when demand is highest.

## Proposed shape

```mermaid
flowchart LR
    accTitle: Proposed incident response reference architecture
    accDescr: Reports arrive from the public through a reporting service, from staff in the field, and from monitoring and partner feeds. An incident service on the Core Delivery Platform records and triages them, and publishes events. Responders coordinate tasks through case and workflow, see a common operating picture on a map from geospatial services, and send alerts through notifications. Data flows to the data platform for reporting and lessons learned.
    PUB(["Public reports"]) --> REP["Reporting service"]
    FIELD(["Field staff"]) --> INC
    MON["Monitoring and<br/>partner feeds"] --> INC
    REP --> INC["Incident service<br/>on CDP"]
    INC -->|"incident events"| MSG["Messaging<br/>TC22"]
    MSG --> CASE["Tasks and workflow<br/>TC08"]
    MSG --> MAP["Common operating picture<br/>Geospatial TC15"]
    MSG --> NOT["Alerts<br/>Notifications TC04"]
    MSG --> DP["Data platform<br/>TC16"]
```

## Questions to answer

!!! warning "To be confirmed"
    **TODO:** which incident types are in scope for a shared capability, and which team owns incident and emergency management technology.

- How do responders outside Defra, such as local authorities and other agencies, get access?
- What service tier does an incident service need, and how does it scale from quiet to surge?
- How do existing incident systems in arm's length bodies fit in?

## Guardrails to pay attention to

- [GR-HOST-07 Design for the resilience the service needs](../../guardrails/hosting-and-platforms.md#gr-host-07)
- [GR-OPS-03 Define and measure service levels](../../guardrails/observability-and-operations.md#gr-ops-03)
- [GR-DATA-02 Use authoritative sources](../../guardrails/data.md#gr-data-02) for locations, holdings and species
- [GR-API-06 Use events for change notifications](../../guardrails/apis-and-integration.md#gr-api-06)
