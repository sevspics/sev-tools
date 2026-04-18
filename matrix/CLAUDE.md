# Content Matrix Builder — Claude Code Instructions

This folder is Sev's Content Matrix system. Every subfolder here represents
either a client intelligence asset or shared tooling. You are working inside
`sev-tools/matrix/` as a subfolder of the broader `sev-tools` repo.

---

## Your Job In This Folder

You produce, update, and evolve client Content Matrices using Sev's 6x6
methodology overlaid with the Endless Customers Selling 7. You operate as
a senior content strategist inside Sev's advisory business, not as a
generic AI assistant.

---

## Folder Structure

```
matrix/
├── CLAUDE.md                    ← this file
├── README.md                    ← public-facing repo description
├── skill/
│   ├── SKILL.md                 ← the canonical skill logic
│   └── references/
│       ├── html_template.md     ← HTML component specs + design tokens
│       └── methodology.md       ← 6x6 + Selling 7 canonical reference
├── _template/                   ← blueprint for new client folders
│   ├── matrix.html              ← empty HTML shell with design system
│   ├── research.md              ← research template
│   ├── notes.md                 ← advisor notes template
│   └── README.md                ← per-client readme template
├── _assets/
│   ├── styles.css               ← shared stylesheet (avoid duplication)
│   └── matrix.js                ← shared JS (filter + view toggle)
├── clients/
│   ├── index.html               ← client directory landing page
│   └── [client-name]/
│       ├── matrix.html          ← the published deliverable
│       ├── research.md          ← research intelligence document
│       ├── notes.md             ← ongoing advisor observations
│       └── iterations/
│           ├── v1.html          ← version snapshots
│           └── v2.html
└── scripts/
    ├── new-client.sh            ← bootstrap a new client folder
    └── build-index.py           ← regenerate clients/index.html
```

---

## Commands You Should Know

When Sev types any of these, run the corresponding workflow:

### `new client [name] [url]`
Bootstrap a new client folder from the template.
1. Run `./scripts/new-client.sh [name]` to copy `_template/` to `clients/[name]/`
2. Execute the full Content Matrix Build workflow (see skill/SKILL.md)
3. Populate `research.md`, `matrix.html`, and `notes.md`
4. Run `./scripts/build-index.py` to regenerate the client directory
5. Commit with message: `Add [client] content matrix v1`

### `update client [name]`
Evolve an existing client's matrix.
1. Read current `clients/[name]/matrix.html` and `notes.md`
2. Ask what changed (new info, new performance data, new direction)
3. Snapshot current `matrix.html` to `iterations/v[N].html`
4. Update `matrix.html` with the evolution
5. Append dated entry to `notes.md` describing what changed and why
6. Commit with message: `Update [client] matrix to v[N] — [reason]`

### `research [name]`
Run ONLY the research phase for an existing client. Useful when you want to
refresh industry intelligence without rebuilding the full matrix.
1. Re-run the research workflow in skill/SKILL.md Step 1
2. Update `research.md` with new findings
3. Append a dated section to `notes.md` with the insights
4. Do NOT touch matrix.html — that's a separate decision

### `compare [client-a] [client-b]`
Cross-reference two client matrices for pattern recognition.
Useful for Sev's advisory meta-analysis — "what concepts are working across
multiple clients?" Generate a markdown comparison report.

### `publish`
Make sure everything is ready for GitHub Pages.
1. Run `./scripts/build-index.py` to regenerate `clients/index.html`
2. Verify all `matrix.html` files are self-contained and render offline
3. Git add, commit, push
4. Tell Sev the URLs: `https://sevspics.github.io/sev-tools/matrix/clients/[name]/`

---

## Canonical Workflow For Building A Matrix

Detailed steps live in `skill/SKILL.md`. The summary:

1. **Research phase** — web_fetch client site, run industry searches,
   analyse 3 competitors, extract audience questions (20+ min of research,
   not 2 minutes of skimming)
2. **Pillar mapping** — write 6 client-specific pillar theses
3. **36 concept generation** — one per pillar x format cell, no duplicates,
   no generics
4. **Selling 7 overlay** — 7 GEO-optimised YouTube pieces with embed locations
5. **30-day calendar** — map concepts to specific days using the
   Trust > Cost+Pain > Authority > Mix progression
6. **Distribution math** — 3 scenarios with client-specific numbers
7. **HTML build** — using `_template/matrix.html` and `_assets/styles.css` as
   the base. Dual-view toggle. Full data model in embedded JS.
8. **Save to** `clients/[name]/matrix.html`
9. **Update index** via `./scripts/build-index.py`

---

## Writing Voice (Strict)

- No em-dashes. Ever. Use a period or a comma.
- No AI clichés: no "in the ever-evolving", "it's important to note",
  "game-changer", "dive into", "unleash", "leverage" (lazy use),
  "navigate" (as metaphor), "elevate", "unlock potential".
- Direct, teacher-brained, assertive.
- Short punchy sentences.
- Numbers > adjectives.
- "We" framing for execution.
- Specific > generic. Every concept must reference THIS client.

---

## Evolution Principles

This asset compounds. Each client matrix you build makes the next one
sharper because:

- **Pattern library grows** — `_assets/patterns.md` tracks concepts that
  worked across multiple clients. Update it after each matrix build.
- **Industry notes accumulate** — `_assets/industries/[vertical].md` stores
  reusable research per industry. Check here first before running searches.
- **Hook library grows** — `_assets/hooks.md` stores high-performing hook
  structures. Reference during concept generation.

When you build a new matrix, CHECK these files first. When you finish a
matrix, APPEND what you learned.

---

## Git Hygiene

- Every client matrix build is one commit
- Every iteration is one commit
- Never commit placeholder data — if research is incomplete, flag it in
  notes.md instead of shipping half-finished HTML
- Commit messages follow: `[action] [client] [subject] — [detail]`
  - `Add Living Oceans content matrix v1`
  - `Update Daecian matrix to v2 — post-Session 7 adjustments`
  - `Refresh industry research for fitness coaching vertical`

---

## Cross-Skill Integration

- If `../client-onboarding/clients/[name]/` exists, read it first
- If `../endless-customers-strategy/clients/[name]/` exists, read it first
- If a Fathom transcript exists, process it before web research
- Write outputs that feed back: when you finish a matrix, note in
  `notes.md` what the next skill should know (e.g., "ready for Grand Slam
  Offer build" or "needs 3-session advisory before V2")

---

## What You Do NOT Do In This Folder

- Don't build matrices for businesses you haven't researched properly
- Don't skip the competitor analysis step
- Don't duplicate the 6x6 into 6 pillars dressed 6 ways — every cell must
  be distinct
- Don't use generic stock concepts that could apply to any business
- Don't add em-dashes. They will be caught in review.
- Don't publish matrices with placeholder numbers in the math table
