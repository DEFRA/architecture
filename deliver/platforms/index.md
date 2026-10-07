<!-- https://defra.github.io/architecture/deliver/platforms/ | maturity: prototype | site version 0.3.0 | generated from deliver/platforms.md -->

# Getting onto Defra platforms

<p class="lead">The shared platforms most Defra services use, what each gives you, and how to get access. Using them is usually faster, cheaper and safer than building your own.</p>

!!! warning "Prototype - testing with users"
    This section is an early prototype that we are testing with users. It may change a lot, and some of it may be wrong. Check with your solution design authority before relying on it, and tell us what works and what does not through the feedback link above.



Ask for access early - in discovery or early alpha - because some platforms need onboarding, approvals or security checks before you can use them. The [technology capability catalogue](https://defra.github.io/architecture/handrail/technology-capabilities/) lists every strategic option, including ones not shown here.

Where we have not yet confirmed a detail, such as a lead time or support channel, it is marked "To be confirmed" and listed on the [open questions](https://defra.github.io/architecture/about/open-questions/) page.

## Defra Core Delivery Platform (CDP) {#cdp}

Defra's internal development platform, with build pipelines, hosting, logging and monitoring already in place for new digital services.

| Detail | What we know |
| --- | --- |
| **How to request access** | Work with the Delivery Architecture team to decide whether CDP is right for your service - the expectation is that it will be ([GR-HOST-01](https://defra.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01)). Then read the [onboarding considerations](https://portal.cdp-int.defra.cloud/documentation/onboarding/onboarding-considerations.md), [architectural overview](https://portal.cdp-int.defra.cloud/documentation/architecture/architectural-overview.md) and [how-to documentation](https://portal.cdp-int.defra.cloud/documentation/how-to/how-to.md). |
| **Lead time** | To be confirmed |
| **Support** | The cdp-support channel in the Defra Digital Team Slack |
| **Documentation** | [https://portal.cdp-int.defra.cloud/documentation/onboarding/onboarding-considerations.md](https://portal.cdp-int.defra.cloud/documentation/onboarding/onboarding-considerations.md) - Needs a Defra device or the Defra VPN. |
| **Defra Digital Service Manual** | [Defra Core Delivery Platform (CDP)](https://digital.defra.gov.uk/architecture-and-software-development/core-delivery-platform) |
| **Technology capability** | [Enabling Platforms (Delivery)](https://defra.github.io/architecture/handrail/technology-capabilities/#enabling-platforms) |

<div id="tbc-1"></div>

!!! warning "To be confirmed"
    **TODO:** Defra Core Delivery Platform (CDP): lead time.

## Defra Customer Identity (also known as Defra ID or IDMv2) {#defra-id}

Sign-in once to many Defra services for external users and the organisations they act for. It uses GOV.UK One Login and HMRC's Government Gateway as identity providers, offers invitation-only access for trusted third parties, and stores users' contact details, organisation accounts and the relationships between them centrally. Defra services get GOV.UK One Login through Customer Identity rather than integrating with it directly.

| Detail | What we know |
| --- | --- |
| **How to request access** | Talk to the Delivery Architecture team in discovery about the level of identity assurance you need and how users act for organisations ([GR-IAM-01](https://defra.github.io/architecture/guardrails/identity-and-access/#gr-iam-01)). |
| **Lead time** | To be confirmed |
| **Support** | The Customer Identity team - contact details are in the Defra Digital Service Manual |
| **Documentation** | [https://defra.sharepoint.com/sites/Community3868/SitePages/Customer%20Identity.aspx](https://defra.sharepoint.com/sites/Community3868/SitePages/Customer%20Identity.aspx) - Defra SharePoint - needs a Defra account. |
| **Defra Digital Service Manual** | [Defra Customer Identity (also known as Defra ID or IDMv2)](https://digital.defra.gov.uk/architecture-and-software-development/defra-customer-identity) |
| **Technology capability** | [Security & Compliance (Delivery)](https://defra.github.io/architecture/handrail/technology-capabilities/#security-and-compliance) |

<div id="tbc-2"></div>

!!! warning "To be confirmed"
    **TODO:** Defra Customer Identity (also known as Defra ID or IDMv2): lead time.

## Defra Forms {#defra-forms}

Accessible online forms that meet GOV.UK standards, through a form builder for simple forms or a plugin for custom forms in your service ([GR-FE-04](https://defra.github.io/architecture/guardrails/front-end-and-accessibility/#gr-fe-04)).

| Detail | What we know |
| --- | --- |
| **How to request access** | To be confirmed |
| **Lead time** | To be confirmed |
| **Support** | The Defra Forms team - contact details are in the Defra Digital Service Manual |
| **Documentation** | [https://forms.defra.gov.uk/](https://forms.defra.gov.uk/) |
| **Defra Digital Service Manual** | [Defra Forms](https://digital.defra.gov.uk/architecture-and-software-development/defra-forms) |
| **Technology capability** | [Customer Service (Business)](https://defra.github.io/architecture/handrail/technology-capabilities/#customer-service) |

<div id="tbc-3"></div>

!!! warning "To be confirmed"
    **TODO:** Defra Forms: how to request access and lead time.

## Defra Interactive Map {#interactive-map}

An open-source, accessible mapping component for government services. It is in beta and not yet stable.

| Detail | What we know |
| --- | --- |
| **How to request access** | Use the component from its open-source repository. |
| **Lead time** | Not needed - it is open source |
| **Support** | The interactive-map channel in the Defra Digital Team Slack. The Defra Digital Service Manual says documentation and support are not yet available while the map is in beta. |
| **Documentation** | [https://defra.github.io/interactive-map/](https://defra.github.io/interactive-map/) |
| **Defra Digital Service Manual** | [Defra Interactive Map](https://digital.defra.gov.uk/architecture-and-software-development/defra-accessible-maps) |
| **Technology capability** | [Geospatial Solutions (Defra Customisation) (Delivery)](https://defra.github.io/architecture/handrail/technology-capabilities/#geospatial-solutions) |

## GOV.UK Notify {#notify}

Emails, text messages and letters to users, through an API or a web interface.

| Detail | What we know |
| --- | --- |
| **How to request access** | Create an account on [GOV.UK Notify](https://www.notifications.service.gov.uk/) with your government email address. New services start in trial mode; request to go live from your service's settings. |
| **Lead time** | To be confirmed |
| **Support** | [GOV.UK Notify support](https://www.notifications.service.gov.uk/support) |
| **Documentation** | [https://docs.notifications.service.gov.uk/](https://docs.notifications.service.gov.uk/) |
| **Technology capability** | [Customer Service (Business)](https://defra.github.io/architecture/handrail/technology-capabilities/#customer-service) |

<div id="tbc-4"></div>

!!! warning "To be confirmed"
    **TODO:** GOV.UK Notify: lead time.

## GOV.UK Pay {#pay}

Online card and digital wallet payments, with refunds and reporting.

| Detail | What we know |
| --- | --- |
| **How to request access** | Create a test account on [GOV.UK Pay](https://www.payments.service.gov.uk/). Going live needs Defra's finance arrangements in place. |
| **Lead time** | To be confirmed |
| **Support** | [GOV.UK Pay support](https://www.payments.service.gov.uk/support/) |
| **Documentation** | [https://docs.payments.service.gov.uk/](https://docs.payments.service.gov.uk/) |
| **Technology capability** | [Finance (Shared & Corporate)](https://defra.github.io/architecture/handrail/technology-capabilities/#finance) |

<div id="tbc-5"></div>

!!! warning "To be confirmed"
    **TODO:** GOV.UK Pay: lead time.

## Defra strategic data platform {#data-platform}

Shared storage, processing and analytics for Defra data, and governed data products for sharing between services. The capability is emerging.

| Detail | What we know |
| --- | --- |
| **How to request access** | To be confirmed |
| **Lead time** | To be confirmed |
| **Support** | To be confirmed |
| **Documentation** | To be confirmed |
| **Technology capability** | [Data (Infrastructure)](https://defra.github.io/architecture/handrail/technology-capabilities/#data) |

<div id="tbc-6"></div>

!!! warning "To be confirmed"
    **TODO:** Defra strategic data platform: how to request access, lead time, support and documentation.

## Platform API gateway and messaging {#api-gateway}

Publishing, securing and managing APIs, and asynchronous messaging between services, on the Core Delivery Platform.

| Detail | What we know |
| --- | --- |
| **How to request access** | Through the Core Delivery Platform team. |
| **Lead time** | To be confirmed |
| **Support** | To be confirmed |
| **Documentation** | To be confirmed |
| **Technology capability** | [Enabling Platforms (Delivery)](https://defra.github.io/architecture/handrail/technology-capabilities/#enabling-platforms) |

<div id="tbc-7"></div>

!!! warning "To be confirmed"
    **TODO:** Platform API gateway and messaging: lead time, support and documentation.



