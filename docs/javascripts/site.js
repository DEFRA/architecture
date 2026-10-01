/* Defra architecture - interactive pieces.
 *
 * Material's instant navigation swaps pages without a full reload, so each
 * feature initialises from document$ and checks its own markup is present.
 */

(function () {
  'use strict'

  function onPage (fn) {
    if (window.document$ && typeof window.document$.subscribe === 'function') {
      window.document$.subscribe(fn)
    } else {
      document.addEventListener('DOMContentLoaded', fn)
    }
  }

  function esc (value) {
    return String(value || '').replace(/[&<>"']/g, function (c) {
      return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]
    })
  }

  /* ---------------- Guardrail library filter ---------------- */

  function initLibrary () {
    const root = document.querySelector('[data-guardrail-library]')
    if (!root) return
    const search = root.querySelector('#gl-search')
    const area = root.querySelector('#gl-area')
    const phase = root.querySelector('#gl-phase')
    const status = root.querySelector('#gl-status')
    const levels = root.querySelectorAll('input[name="gl-level"]')
    const cards = root.querySelectorAll('.gl-card')
    const shown = root.querySelector('#gl-shown')
    const empty = root.querySelector('.gl-empty')

    function apply () {
      const terms = search.value.toLowerCase().split(/\s+/).filter(Boolean)
      const wanted = {}
      levels.forEach(function (box) { wanted[box.value] = box.checked })
      let count = 0
      cards.forEach(function (card) {
        const text = card.dataset.search
        const match = wanted[card.dataset.level] &&
          (!area.value || card.dataset.area === area.value) &&
          (!phase.value || card.dataset.phases.split(' ').indexOf(phase.value) !== -1) &&
          (!status.value || card.dataset.status === status.value) &&
          terms.every(function (t) { return text.indexOf(t) !== -1 })
        card.hidden = !match
        if (match) count++
      })
      shown.textContent = count
      empty.hidden = count !== 0
    }

    search.addEventListener('input', apply)
    area.addEventListener('change', apply)
    phase.addEventListener('change', apply)
    status.addEventListener('change', apply)
    levels.forEach(function (box) { box.addEventListener('change', apply) })
    const hash = decodeURIComponent((window.location.hash || '').slice(1))
    if (/^gr-/i.test(hash)) search.value = hash.toUpperCase()
    apply()
  }

  /* ---------------- Decision check ---------------- */

  // Ordered from most to least significant route.
  const ROUTES = {
    tgb: {
      rank: 4,
      tone: 'red',
      title: 'Technology Governance Board',
      who: 'Technology Governance Board, normally after review by the TDA',
      body: "This changes Defra's technology direction. Talk to the architecture team, who will help you take it to the TDA first and then the TGB.",
      link: 'tgb'
    },
    tda: {
      rank: 3,
      tone: 'red',
      title: 'Technical Design Authority',
      who: 'Technical Design Authority',
      body: 'This needs a cross-cutting view. Book a conversation with an architect, then complete a TDA submission. Come early: it is cheaper to change direction now.',
      link: 'tda'
    },
    sda: {
      rank: 2,
      tone: 'amber',
      title: 'Solution design authority',
      who: 'Your solution design authority',
      body: 'Record the decision as an ADR, explain any departure from the default, and agree it with your solution design authority.',
      link: 'sda'
    },
    advice: {
      rank: 1,
      tone: 'amber',
      title: 'Get targeted advice',
      who: 'Delivery team, after advice from an architect',
      body: 'Nothing is definitely outside the guardrails, but some answers are uncertain. Ask an architect about just those points, then come back and re-run the check.',
      link: 'advice'
    },
    team: {
      rank: 0,
      tone: 'green',
      title: 'Your team decides',
      who: 'Delivery team',
      body: 'You are inside the guardrails. Make the decision, record it as an ADR and carry on. Re-run the check if the scope or risk changes.',
      link: 'team'
    }
  }

  const QUESTIONS = [
    {
      id: 'strategy',
      route: 'tgb',
      title: 'Technology direction',
      text: "Does it create, replace or retire a strategic platform, change Defra's technology strategy, or change a Must guardrail?",
      guardrails: ['GR-PRIN-03']
    },
    {
      id: 'must',
      route: 'tda',
      title: 'Must guardrails',
      text: 'Would you be unable to meet a Must guardrail? For example hosting off the Core Delivery Platform, building your own sign-in, or keeping code private.',
      guardrails: ['GR-HOST-01', 'GR-IAM-01', 'GR-OPEN-01']
    },
    {
      id: 'novel',
      route: 'tda',
      title: 'Something new to Defra',
      text: 'Does it introduce a technology, supplier, integration pattern or use of AI that Defra has not used before?',
      guardrails: ['GR-TECH-01', 'GR-AI-06']
    },
    {
      id: 'cross',
      route: 'tda',
      title: 'Impact beyond your service',
      text: "Will other services, teams or arm's length bodies depend on it or be affected by it, such as a shared API, shared data or a change to identity?",
      guardrails: ['GR-API-05', 'GR-DATA-02']
    },
    {
      id: 'risk',
      route: 'tda',
      title: 'Security and data risk',
      text: 'Is there a high security or data protection risk, or a security control you cannot meet?',
      guardrails: ['GR-SEC-02', 'GR-SEC-09', 'GR-DATA-06']
    },
    {
      id: 'default',
      route: 'sda',
      title: 'Departing from a default',
      text: 'Are you choosing something other than the strategic option in the technology capabilities, or departing from a Should guardrail?',
      guardrails: ['GR-TECH-02', 'GR-DEV-01']
    },
    {
      id: 'reverse',
      route: 'sda',
      title: 'Hard to reverse',
      text: 'Would it be expensive or slow to reverse, for example a long contract, significant lock-in or a data migration, without an exit plan?',
      guardrails: ['GR-TECH-03']
    }
  ]

  function initDecisionCheck () {
    const root = document.querySelector('[data-decision-check]')
    if (!root) return
    // Links are written in the page's Markdown so MkDocs resolves and checks them.
    function href (key) {
      const a = root.querySelector('.dc-links a[data-route="' + key + '"]')
      return a ? a.getAttribute('href') : '#'
    }
    const library = href('library')
    let answers = {}
    const list = root.querySelector('.dc-questions')
    const bar = root.querySelector('.dc-progress span')
    const counter = root.querySelector('.dc-counter')
    const result = root.querySelector('.dc-result')
    const record = root.querySelector('.dc-record')
    const status = root.querySelector('.dc-copy-status')

    list.innerHTML = QUESTIONS.map(function (q, i) {
      const name = 'dc-' + q.id
      return '<fieldset class="dc-q" data-q="' + q.id + '"><legend><span class="dc-q__n">' + (i + 1) +
        '</span><span><strong>' + esc(q.title) + '</strong><span class="dc-q__text">' + esc(q.text) +
        '</span></span></legend><div class="dc-opts">' +
        ['No', 'Unsure', 'Yes'].map(function (v) {
          return '<label class="dc-opt"><input type="radio" name="' + name + '" value="' + v + '"><span>' + v + '</span></label>'
        }).join('') + '</div></fieldset>'
    }).join('')

    function guardrailLinks (ids) {
      return ids.map(function (id) {
        return '<a href="' + library + '#' + id.toLowerCase() + '"><code>' + id + '</code></a>'
      }).join(' ')
    }

    function evaluate () {
      const yes = QUESTIONS.filter(function (q) { return answers[q.id] === 'Yes' })
      const unsure = QUESTIONS.filter(function (q) { return answers[q.id] === 'Unsure' })
      let route = ROUTES.team
      yes.forEach(function (q) { if (ROUTES[q.route].rank > route.rank) route = ROUTES[q.route] })
      if (!yes.length && unsure.length) route = ROUTES.advice
      return { route, yes, unsure }
    }

    function render () {
      const answered = Object.keys(answers).length
      bar.style.width = (answered / QUESTIONS.length * 100) + '%'
      counter.textContent = answered + ' of ' + QUESTIONS.length + ' answered'
      root.querySelector('.dc-waiting').hidden = answered === QUESTIONS.length
      if (answered < QUESTIONS.length) {
        result.hidden = true
        record.hidden = true
        return
      }
      const r = evaluate()
      const flagged = r.yes.concat(r.unsure)
      result.className = 'dc-result dc-result--' + r.route.tone
      result.innerHTML =
        '<p class="dc-result__label">Suggested route</p><h3>' + r.route.title + '</h3><p>' + r.route.body + '</p>' +
        (flagged.length
          ? '<p><strong>What triggered this</strong></p><ul>' + flagged.map(function (q) {
            return '<li><strong>' + esc(q.title) + '</strong> (' + answers[q.id].toLowerCase() + ') &middot; see ' + guardrailLinks(q.guardrails) + '</li>'
          }).join('') + '</ul>'
          : '<p>No boundaries were triggered.</p>') +
        '<p><a class="md-button md-button--primary" href="' + href(r.route.link) + '">Next: ' + r.route.title + '</a></p>'
      result.hidden = false

      const title = root.querySelector('#dc-title').value.trim() || 'Untitled decision'
      const team = root.querySelector('#dc-team').value.trim()
      const context = root.querySelector('#dc-context').value.trim()
      const today = new Date().toISOString().slice(0, 10)
      const lines = [
        '# NNNN. ' + title,
        '',
        '- Status: Proposed',
        '- Date: ' + today,
        '- Team: ' + (team || '(add team)'),
        '- Decided by: ' + r.route.who,
        '- Guardrails considered: ' + (flagged.length ? flagged.map(function (q) { return q.guardrails.join(', ') }).join(', ') : 'none triggered'),
        '',
        '## Context',
        '',
        context || '(Describe the problem, the user and business need, and the constraints.)',
        '',
        '## Decision check',
        ''
      ].concat(QUESTIONS.map(function (q) { return '- ' + q.title + ': ' + answers[q.id] }), [
        '',
        'Suggested route: ' + r.route.title,
        '',
        '## Options considered',
        '',
        '## Decision',
        '',
        '## Consequences',
        ''
      ])
      record.querySelector('textarea').value = lines.join('\n')
      record.hidden = false
    }

    root.addEventListener('change', function (event) {
      const input = event.target
      if (input.type === 'radio') {
        answers[input.name.slice(3)] = input.value
        input.closest('.dc-q').classList.add('dc-q--done')
      }
      render()
    })
    root.addEventListener('input', function (event) {
      if (event.target.matches('#dc-title, #dc-team, #dc-context')) render()
    })
    root.querySelector('.dc-copy').addEventListener('click', function () {
      const area = record.querySelector('textarea')
      function fallback () {
        area.focus()
        area.select()
        status.textContent = 'Selected - press Ctrl+C or Cmd+C to copy'
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(area.value).then(function () {
          status.textContent = 'Copied'
        }, fallback)
      } else {
        fallback()
      }
    })
    root.querySelector('.dc-reset').addEventListener('click', function () {
      answers = {}
      root.querySelectorAll('input[type=radio]').forEach(function (r) { r.checked = false })
      root.querySelectorAll('.dc-q').forEach(function (q) { q.classList.remove('dc-q--done') })
      status.textContent = ''
      render()
      root.scrollIntoView({ behavior: 'smooth' })
    })
    render()
  }

  /* ---------------- Home page search button ---------------- */

  function initSearchButton () {
    document.querySelectorAll('[data-open-search]').forEach(function (button) {
      button.addEventListener('click', function () {
        const toggle = document.getElementById('__search')
        const input = document.querySelector('.md-search__input')
        if (toggle) toggle.checked = true
        if (input) setTimeout(function () { input.focus() }, 50)
      })
    })
  }

  onPage(function () {
    initSearchButton()
    initLibrary()
    initDecisionCheck()
  })
})()
