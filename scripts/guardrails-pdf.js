/* Make the PDF of every guardrail that is attached to each release.
 *
 * Opens the built print page (site/print/guardrails/index.html) in Chromium
 * and saves it as an A4 PDF with page numbers.
 *
 *   mkdocs build --strict && node scripts/guardrails-pdf.js dist/guardrails.pdf
 */

'use strict'

const fs = require('fs')
const path = require('path')
const { pathToFileURL } = require('url')
const { chromium } = require('playwright')

const PAGE = path.resolve(__dirname, '..', 'site', 'print', 'guardrails', 'index.html')

async function main () {
  const out = process.argv[2]
  if (!out) throw new Error('Usage: node scripts/guardrails-pdf.js <output.pdf>')
  if (!fs.existsSync(PAGE)) throw new Error(`${PAGE} not found - run mkdocs build first`)
  fs.mkdirSync(path.dirname(path.resolve(out)), { recursive: true })

  const browser = await chromium.launch()
  try {
    const page = await browser.newPage()
    await page.emulateMedia({ media: 'print', colorScheme: 'light' })
    await page.goto(pathToFileURL(PAGE).href, { waitUntil: 'load' })
    await page.pdf({
      path: out,
      format: 'A4',
      printBackground: true,
      margin: { top: '18mm', bottom: '18mm', left: '15mm', right: '15mm' },
      displayHeaderFooter: true,
      headerTemplate: '<span></span>',
      footerTemplate: '<div style="width:100%;font-size:8px;text-align:center;color:#505a5f">' +
        'Defra architecture guardrails - page <span class="pageNumber"></span> of <span class="totalPages"></span></div>'
    })
  } finally {
    await browser.close()
  }
  console.log(`Saved ${out}`)
}

main().catch(function (err) {
  console.error(err.message)
  process.exit(1)
})
