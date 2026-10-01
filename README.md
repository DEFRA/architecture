# Defra architecture

Source for the Defra architecture site at [https://howellsr.github.io/architecture](https://howellsr.github.io/architecture/): guardrails, the business-to-technology capability handrail, governance, and enterprise data and security architecture, for Defra product and platform teams and delivery partners.

## What is here

| Path | Contents |
| --- | --- |
| `docs/` | Site content in Markdown, one folder per section |
| `capabilities/` | Business and technology capability models (YAML) |
| `nfrs/` | Service tiers and the non-functional requirements catalogue (YAML) |
| `hooks/` | Build-time scripts that validate the data and generate the capability map, guardrail library, NFR tables and draft banners |
| `overrides/`, `docs/stylesheets/`, `docs/javascripts/` | Home page hero, theme, decision check and library filter |
| `tests/` | Content checks (`pytest`) and the WCAG 2.2 AA accessibility check (`npm test`) |
| `.github/` | CI workflow, pull request and issue templates, Dependabot |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
mkdocs serve
```

Open http://127.0.0.1:8000. Before raising a pull request run `pytest` and `mkdocs build --strict`. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to add guardrails, NFRs and capabilities.

## Publishing

The site is published with GitHub Pages at <https://howellsr.github.io/architecture/>.

- Every push to `main` runs `.github/workflows/ci.yml`: content tests, a strict build and an accessibility check. If all pass, `mkdocs gh-deploy` pushes the built site to the `gh-pages` branch.
- GitHub Pages serves the `gh-pages` branch. One-off setup (repository admin): **Settings → Pages → Build and deployment → Source: Deploy from a branch → Branch: `gh-pages` / `(root)` → Save**.
- If the site shows this README instead of the home page, Pages is serving `main`. Change the branch to `gh-pages` as above.
- To republish without a code change, run the **ci** workflow manually from the **Actions** tab (**Run workflow** on `main`).
- Pull requests run the same checks but never publish.

If the site moves to another organisation or custom domain, update `site_url`, `repo_url` and `repo_name` in `mkdocs.yml` and the links in this README.

## Contributing

Issues and pull requests are welcome from Defra staff and delivery partners. See the [contribution guide](https://howellsr.github.io/architecture/contribute/).

## Licence

THIS INFORMATION IS LICENSED UNDER THE CONDITIONS OF THE OPEN GOVERNMENT LICENCE found at:

<http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3>

The following attribution statement MUST be cited in your products and applications when using this information.

>Contains public sector information licensed under the Open Government license v3
