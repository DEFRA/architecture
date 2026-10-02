# Moving this site to the DEFRA GitHub organisation

<p class="lead">The site and its repository moved from a personal fork, howellsr/architecture, to <a href="https://github.com/DEFRA/architecture">DEFRA/architecture</a>, published at <a href="https://defra.github.io/architecture/">defra.github.io/architecture</a>. This page records how, and what keeps old links working.</p>

The site was built in a personal fork while it was in alpha. It moved to the DEFRA GitHub organisation, where the Defra Digital Service Manual says code is stored - see [architecture](https://digital.defra.gov.uk/architecture) - in line with [GR-DEV-02](../guardrails/software-development.md#gr-dev-02). The decision is recorded in [ADR 0006](../adr/0006-move-to-defra-github.md).

!!! warning "To be confirmed"
    **TODO:** which Defra team owns the repository and reviews changes (for `.github/CODEOWNERS`), and whether the site moves to a Defra-owned custom domain at beta.

## How it moved

`DEFRA/architecture` already existed, and the personal repository was a fork of it. So rather than transferring a repository, the fork's history was merged back into `DEFRA/architecture` through a pull request. Every commit, the changelog and the decision records came across unchanged.

1. **Point the site at the new address.** `site_url`, `repo_url` and `repo_name` in `mkdocs.yml`, every link to the repository or site, the issue forms, the guardrail check, `.lychee.toml` and the tests now use `DEFRA/architecture` and `defra.github.io/architecture`.
2. **Open a pull request from the fork into `DEFRA/architecture`** and merge it with a merge commit or "Rebase and merge" - not "Squash", which would lose the history.
3. **Set up the repository:**
    - publish GitHub Pages from the `gh-pages` branch
    - let workflows read and write (Settings, Actions, General, Workflow permissions), so the deploy and release workflows can push
    - allow the actions the workflows use, if the organisation restricts them
    - turn on Issues and Discussions, turn off the wiki, and create the GitHub Project for the roadmap
    - protect `main`, requiring the CI checks, and allow auto-merge
    - turn on secret scanning, push protection and Dependabot
4. **Release a new version** from `DEFRA/architecture`, so the latest tag and guardrails PDF carry the new address.

## What keeps working

- **Version 0.2.0 and its PDF** stay at [howellsr/architecture releases](https://github.com/howellsr/architecture/releases/tag/v0.2.0), so contracts that cite it remain valid. The fork is kept, not deleted.
- **Old page addresses**, including guardrail anchors such as `#gr-host-01`, redirect to the same page on the new site. Build the site, then run:

    ```bash
    python scripts/make_redirects.py site redirects https://defra.github.io/architecture/
    ```

    Publish the `redirects` folder to the fork's `gh-pages` branch. Only `DEFRA/architecture` deploys the site, so nothing in the fork overwrites the redirects. If the fork is later archived, GitHub Pages keeps serving them.
- **Published data**, such as `guardrails.json`, is copied once to the old address and then only updated at the new one. Tools should switch to the new address.

## Changes from the fork

The fork can still be used to prepare changes, which are then proposed to `DEFRA/architecture` in a pull request. Its checks run, but publishing, releases and the weekly link check only run in `DEFRA/architecture`. See [`MAINTAINERS.md`](https://github.com/DEFRA/architecture/blob/main/MAINTAINERS.md#changes-from-a-fork).

## Avoiding this next time

A stable custom domain owned by Defra would let the site move between organisations or hosting without anyone's links changing. This is being considered for beta.
