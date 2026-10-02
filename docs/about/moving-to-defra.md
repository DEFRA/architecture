# Moving this site to a Defra GitHub organisation

<p class="lead">How to move the site and its repository from howellsr/architecture to a Defra-owned GitHub organisation, without breaking the links in contracts, decision records and other sites.</p>

The site is published from a personal account while it is in alpha. It should move to a Defra-owned organisation before it is used widely in contracts - in line with [GR-DEV-02](../guardrails/software-development.md#gr-dev-02), which asks for all code to be in Defra source control.

The Defra Digital Service Manual says code is stored in the [Defra GitHub organisation](https://github.com/DEFRA) - see [architecture](https://digital.defra.gov.uk/architecture) - so that is the expected destination.

!!! warning "To be confirmed"
    **TODO:** confirm the move is to the DEFRA GitHub organisation, and the repository name, the new published address (including whether to use a custom domain), who owns the repository after the move, and when the move happens.

## What has to keep working

- **Releases, tags and PDFs cited in contracts**, such as `github.com/howellsr/architecture/releases/tag/v0.2.0`. Transferring the repository moves releases and tags with it, and GitHub redirects the old repository address. Do not create a new repository with the old name, or the redirect stops.
- **Pages and guardrail anchors on the site**, such as `howellsr.github.io/architecture/guardrails/hosting-and-platforms/#gr-host-01`. Publish redirect pages at the old address (see below).
- **The published data**, such as `guardrails.json`. It is copied to the old address once, then updated only at the new one. Tools should switch to the new address.
- **Clones and forks** of the repository. GitHub redirects them after a transfer.

## Steps

1. **Agree the target** organisation, repository name and published address, and record the decision in an ADR.
2. **Transfer the repository** to the Defra organisation using GitHub's repository transfer, rather than copying it. This keeps the history, issues, pull requests, releases and tags, and redirects the old repository address.
3. **Update the settings** in the repository: `site_url`, `repo_url` and `repo_name` in `mkdocs.yml`, links in `README.md` and `CHANGELOG.md`, the link-check exclusions in `.lychee.toml`, and any other occurrence of `howellsr` (`grep -rn howellsr .`).
4. **Turn on publishing and protection** in the new repository: GitHub Pages from the `gh-pages` branch, branch protection on `main`, secret scanning and push protection, the dependency graph and Dependabot.
5. **Publish redirects at the old address.** Build the site, then run:

    ```bash
    python scripts/make_redirects.py site redirects https://NEW-ADDRESS/
    ```

    This writes a page at every old address that sends readers to the same page at the new address, keeping anchors such as `#gr-host-01`, and a 404 page that does the same for any other address. Publish the `redirects` folder as the `architecture/` folder of the `howellsr.github.io` user site repository. Using the user site, rather than a new repository called `architecture`, keeps GitHub's redirect of the old repository address working.
6. **Release a new version** from the new location, so the latest PDF and tag carry the new address.
7. **Tell people** - announce the move in [what's new](changelog.md), and ask commercial teams to use the new address in new contracts. Existing contracts do not need to change: their links still work.

## Avoiding this next time

A stable custom domain owned by Defra would let the site move between organisations or hosting in future without anyone's links changing. Consider it as part of this move.
