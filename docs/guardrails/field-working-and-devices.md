---
principles: [GR-PRIN-08]
applicability: tbc
guardrail_defaults:
  status: draft
  owner: Architecture team
  automated_check: manual
  last_reviewed: 2026-10-01
  since_version: 0.2.0
guardrails:
  GR-FIELD-01:
    phases: [discovery, alpha]
    evidence: User research on the working environment, and the device choice recorded in an ADR
    service_standard_points: [1]
  GR-FIELD-02:
    phases: [alpha, beta, live]
    evidence: Field journeys tested with no connection, including sync after reconnecting and conflict handling
    service_standard_points: [5]
  GR-FIELD-03:
    phases: [alpha, beta, live]
    evidence: Devices enrolled in Defra device management, with encryption, patching and remote wipe confirmed
    evidence_by_phase:
      alpha: Device management approach agreed for the devices the service will use
      beta: Devices enrolled in Defra device management, with encryption, patching, screen lock and remote wipe confirmed
      live: Device compliance monitored, and lost devices wiped
    tcop_points: [6]
    sbd_principles: [7, 8]
  GR-FIELD-04:
    phases: [discovery, alpha]
    evidence: Connectivity in the places the service will be used checked, and the approach recorded
---

# Field working and devices

<p class="lead">Many Defra staff and partners work on farms, at ports, on rivers and at sea. These draft guardrails make sure the tools they use work where they work, and keep Defra data safe on the move.</p>

Puts architecture principle [8. Right tools, right place](../principles/architecture-principles.md#gr-prin-08) into practice. See also the proposed [field inspection](../handrail/reference-architectures/field-inspection.md) reference architecture.

!!! info "Draft guardrails"
    These guardrails are new drafts from the [guardrail backlog](../about/roadmap.md#guardrail-backlog). Comment on them by [opening an issue](https://github.com/howellsr/architecture/issues).

## GR-FIELD-01 Choose devices that suit the job {#gr-field-01}

<span class="rfc rfc--should">Should</span> Choose devices for field work from research into where and how people work - outdoors, in bad weather, wearing gloves, in the dark - not from what is already on the desk.

**Why:** a tool that cannot be used in the rain or with gloves on will not be used, and staff fall back to paper.

**How to meet it:** observe field work in discovery, and record the device choice and the reasons in an ADR.

## GR-FIELD-02 Design field tools to work offline {#gr-field-02}

<span class="rfc rfc--should">Should</span> Field tools work without a connection: they download what is needed before a visit, save work on the device, and sync safely when back in signal.

**Why:** much of rural England and the sea has poor or no mobile coverage. Losing work because the signal dropped destroys trust in digital tools.

**How to meet it:** test every field journey in flight mode, and decide in an ADR how conflicts are resolved when two people change the same record offline.

## GR-FIELD-03 Manage and secure every device {#gr-field-03}

<span class="rfc rfc--must">Must</span> Devices that hold or access Defra data are enrolled in Defra device management, encrypted, kept patched, protected by a screen lock and able to be wiped remotely if lost.

**Why:** field devices are lost and stolen more often than office equipment, and may hold personal and sensitive data.

**How to meet it:** use Defra-managed devices. If a supplier or partner device is needed, agree how it meets the same controls before it is used.

## GR-FIELD-04 Check connectivity before you design {#gr-field-04}

<span class="rfc rfc--could">Could</span> Check the mobile and broadband coverage where the service will be used before choosing an approach, rather than assuming it.

**Why:** coverage maps and real-world signal often differ, especially inside farm buildings and in valleys.

**How to meet it:** use public coverage data and ask users, and plan for the worst case.
