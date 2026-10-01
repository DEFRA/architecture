/* Accessibility check for the built site.
 *
 * Serves ./site, opens every page in Chromium (light and dark colour schemes)
 * and runs axe-core against WCAG 2.2 A and AA rules. Exits non-zero if any
 * violation is found, so CI fails before an inaccessible change is published.
 *
 *   mkdocs build --strict && npm test
 */

"use strict";

const fs = require("fs");
const http = require("http");
const path = require("path");
const { chromium } = require("playwright");

const SITE = path.resolve(__dirname, "..", "site");
const AXE = require.resolve("axe-core/axe.min.js");
const TAGS = ["wcag2a", "wcag2aa", "wcag21a", "wcag21aa", "wcag22aa"];
const TYPES = { ".html": "text/html", ".css": "text/css", ".js": "text/javascript", ".json": "application/json", ".png": "image/png", ".svg": "image/svg+xml" };

function pages(dir, base = "") {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const rel = path.posix.join(base, entry.name);
    if (entry.isDirectory()) return pages(path.join(dir, entry.name), rel);
    return entry.name === "index.html" ? ["/" + base + (base ? "/" : "")] : [];
  });
}

function serve() {
  return new Promise((resolve) => {
    const server = http.createServer((req, res) => {
      let file = path.join(SITE, decodeURIComponent(req.url.split("?")[0]));
      if (file.endsWith("/")) file = path.join(file, "index.html");
      fs.readFile(file, (err, body) => {
        if (err) { res.writeHead(404); res.end(); return; }
        res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream" });
        res.end(body);
      });
    }).listen(0, "127.0.0.1", () => resolve(server));
  });
}

(async () => {
  const server = await serve();
  const origin = `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const urls = pages(SITE).filter((u) => u !== "/search/");
  let failures = 0;

  for (const scheme of ["light", "dark"]) {
    const page = await browser.newPage({ colorScheme: scheme, viewport: { width: 1280, height: 900 } });
    // Mermaid diagrams load from a CDN; block third-party requests so results are repeatable.
    await page.route(/^https?:\/\/(?!127\.0\.0\.1)/, (route) => route.abort());
    for (const url of urls) {
      await page.goto(origin + url, { waitUntil: "load" });
      await page.addScriptTag({ path: AXE });
      const { violations } = await page.evaluate((tags) =>
        // Diagrams are drawn at runtime by Mermaid from a CDN, which this test blocks.
        // The unrendered source is left in a bare <pre>; skip it. Every diagram
        // carries accTitle/accDescr, checked by tests/test_content.py.
        window.axe.run({ exclude: [[".mermaid"], ['pre[class=""]']] }, { runOnly: { type: "tag", values: tags } }), TAGS);
      for (const v of violations) {
        failures += v.nodes.length;
        console.log(`\n[${scheme}] ${url}\n  ${v.id} (${v.impact}): ${v.help}`);
        v.nodes.slice(0, 5).forEach((n) => console.log(`    ${n.target.join(" ")}\n      ${n.failureSummary.split("\n").slice(1, 2).join(" ").trim()}`));
      }
    }
    await page.close();
  }

  await browser.close();
  server.close();
  console.log(failures ? `\n${failures} accessibility issue(s) found across ${urls.length} pages.` : `\nNo accessibility issues found across ${urls.length} pages in light and dark mode.`);
  process.exit(failures ? 1 : 0);
})();
