# Content Matrix Builder

> Sev's 6×6 Content Matrix system for advisory clients. Generates
> industry-researched, audience-informed, filmable content plans that
> clients see as "already built, just press go."

**Live directory:** https://sevspics.github.io/sev-tools/matrix/clients/

---

## What This Is

A system that turns a client website URL into a complete 36-concept content
plan, with:

- 6 content pillars × 6 production formats = 36 concepts
- Selling 7 YouTube authority stack for GEO searchability
- 30-day posting calendar
- 3-scenario distribution math
- Dual-view HTML: polished for clients, detailed for internal execution

---

## How To Use It

Open this folder in Claude Code. The `CLAUDE.md` at the top tells Claude
everything it needs to know. Then use these commands:

```
new client [slug] [url]       # Build a fresh matrix for a new client
update client [slug]          # Evolve an existing client's matrix
research [slug]               # Refresh industry intel only
compare [slug-a] [slug-b]     # Cross-reference two clients
publish                       # Push to GitHub Pages
```

---

## Folder Map

```
matrix/
├── CLAUDE.md             Claude Code's instructions for this folder
├── README.md             This file
├── skill/                The canonical skill logic + references
├── _template/            Blueprint copied when creating a new client
├── _assets/              Shared CSS, JS, patterns, hooks, industry intel
├── clients/              One folder per client (+ index.html directory)
└── scripts/              new-client.sh, build-index.py
```

---

## The Methodology

Built on Sev's 6×6 Content Matrix (established with Daecian Sparkes-Young
in Session 1, refined through Sessions 2-7) overlaid with Marcus Sheridan's
Endless Customers Selling 7 for GEO searchability.

Full methodology: `skill/references/methodology.md`

---

## Publishing

All client matrices auto-publish to GitHub Pages at:

```
https://sevspics.github.io/sev-tools/matrix/clients/[client-slug]/
```

The directory index is at:

```
https://sevspics.github.io/sev-tools/matrix/clients/
```

The index regenerates automatically via `scripts/build-index.py` whenever
a new client is added or updated.
