# Releases and versions

<p class="lead">Which version of the guardrails is in force, what changed in each release, and how to cite a fixed version in a contract or assessment.</p>

The live site always shows the latest content, including changes that are not yet part of a release. Contracts, statements of work and assessments should cite a **released version**: it never changes after release.

## How releases work

- Each release has a [semantic version](https://semver.org/), such as `0.2.0`. See the [versioning policy](../partners/contracting.md#versioning-policy) for what each kind of change means.
- Releases are recorded in [`CHANGELOG.md`](https://github.com/howellsr/architecture/blob/main/CHANGELOG.md) in the repository, which this page is built from.
- When a release is made, the commit is tagged `vX.Y.Z` and a [GitHub release](https://github.com/howellsr/architecture/releases) is created with a **PDF of every guardrail** attached. The PDF is the archived copy to cite.
- The banner at the top of every page shows the version in force.

To cite a version, see [contracting with this site](../partners/contracting.md#cite-a-fixed-version).

## Why the site does not keep old versions online

Some documentation sites publish every old version side by side, with the version in the address. We do not, because:

- addresses stay the same, so links in decision records, contracts and other sites keep working
- the tagged source and the PDF attached to each release are a permanent, citable record of exactly what applied
- there is only one live version to maintain, check for accessibility and keep secure

If people need to browse an old version as a website, we can revisit this.

<!-- releases:changelog -->
