# Knowledge Hub — Daily Scrape Routine (operating procedure)

**Run this once per day.** It finds new Fathom calls, harvests reusable knowledge entries, adds them to
the hub **in the 22-variant cyclable format**, records cross-call mentions, commits/pushes, and emails a
summary. This file is the single source of truth for the routine — edit it here, not in the Cowork prompt.

> **Cowork routine prompt should be just:**
> *"Read `knowledge-hub/DAILY-SCRAPE-ROUTINE.md` in the Sevs Brain sev-tools repo and execute it exactly. Today is {{today}}."*

---

## 0. Repo & tools
- **Canonical repo (edit/commit HERE):** `~/Desktop/Sevs Brain/Sev's Brain/sev-tools`. File: `knowledge-hub/index.html`.
  **NEVER** use `~/Desktop/sev-tools` — it's a stale clone; editing it regresses the live site.
- Live: https://sevspics.github.io/sev-tools/knowledge-hub/ (Pages from `main` root, ~30–60s build).
- **Fathom MCP** (load via ToolSearch if deferred): `fathom_list_meetings`, `fathom_get_transcript`, `fathom_get_summary`.
  Note: `list_meetings` returns both `recording_id` (use this for `get_transcript`) and `url` (contains the public
  call-link number that goes in the entry's `link`). The two numbers differ — always map via `list_meetings`.

## 1. Determine the window
- Last scrape date = the date in the most recent `Daily scrape: <date>` git commit (`git log -1 --grep='Daily scrape'`).
- Window = **(last scrape date + 1 day) → today**. List meetings with `fathom_list_meetings`
  (`created_after`/`created_before` ISO, `response_format:"json"`). Catch up multiple days if a run was missed.

## 2. Triage each meeting (skip, with a reason)
SKIP and log the reason if:
- **Already indexed** — its call-link number already appears in `CALLS`, or it's already mapped to a `sourceId`.
- **Impromptu / no signal** — generic titles ("Impromptu Zoom/Meet Meeting") with no real agenda.
- **No usable material** — no Fathom summary AND transcript is one segment / < ~60s of content.
Otherwise QUALIFY it.

## 3. Harvest (for each qualifying meeting)
- Add a `CALLS` entry: `{ id, name, date, type, attendees, link, duration }`.
  `id` = short slug (e.g. `firstname-MMMdd` or `firstname-sN`). `type` ∈ {1:1 Advisory, Group Advisory, BTS Sales, Peer Strategy, Audit, Podcast, BTS Production}. `link` = `https://fathom.video/calls/<call-link-number>`.
- Fetch the transcript. Harvest **1–4 reusable entries** (frameworks, reframes, tactics, principles, case studies).
  Skip logistics/smalltalk. Prefer the novel, specific moment over generic advice. Don't duplicate an existing entry —
  if the call merely repeats a known framework, record a **mention** (§5) instead of a new entry.

## 4. Build each entry — FOLLOW `knowledge-hub/EXTRACTION-SPEC.md` EXACTLY
Read `EXTRACTION-SPEC.md` (same folder) at the start of every run. Each entry uses the full schema there, and:

> **CRITICAL — `formats` MUST be the 22-variant structure (EXTRACTION-SPEC §2), never the old single-brief.**
> Lock the backbone once (core reframe · proof point from the call · signature payoff line · ONE uppercase
> CTA code word), then write **5 faceless + 5 meme + 1 candid (5 hook options) + 5 framed + 3 visual-storyteller
> + 3 talking-head = 22 variants**. Hooks are deliverable lines; bodies use `\n` between beats; stage
> directions live ONLY in `notes`; `styleNote` on every format except candid. Gold-standard reference entry:
> `chris-pemberton-may29-01`.

A newly-scraped entry that is still single-brief is a **defect** — do not ship it; convert before committing.

## 5. Mentions
When a qualifying call references an already-indexed framework, append the call's `id` to that entry's
`mentions` array (powers the 🔁 multiplier). Track each one for the summary.

## 6. Insert & sanity-check
- Add new entry objects to the `ENTRIES` array and new calls to `CALLS`. Render sorts by call date
  (`sortByDate`), so array position is cosmetic — append is fine.
- After editing, sanity-check the file still parses: no trailing commas / unescaped quotes in the JS object
  literals, and `ENTRIES`/`CALLS` still load. (If you can, open the page or grep that the new ids are present
  and the array brackets balance.)

## 7. Commit + push
```
cd "/Users/sevamozhaev/Desktop/Sevs Brain/Sev's Brain/sev-tools"
git add knowledge-hub/index.html
git commit -m "Daily scrape: <YYYY-MM-DD> — N new entries, M mention updates"
git push origin main
```
If git fails, retry once after a short wait, then fall back (§8) so nothing is lost.

## 8. Email summary (+ fallback)
Email to **sev@sevspics.com**, subject `Knowledge Hub Daily — <date> — N new entries, M mention updates`,
body in this exact shape:
```
Knowledge Hub — Daily Scrape Summary
Date: <date>
Window: <start> → <end>
Live URL: https://sevspics.github.io/sev-tools/knowledge-hub/

— RUN STATUS —
Meetings scanned: <n>
Meetings skipped:
- <name> — <reason>
Git commit + push: <OK / error>

— NEW CALLS ADDED (<n>) —
- <call-id> — <name> — <date> — <duration>min
  Link: <fathom url>

— NEW ENTRIES ADDED (<n>) —
- **<entry-id>: <title>**
  Source: <call-id>
  TL;DR: <one sentence>

— MENTIONS RECORDED (<n>) —
- <framework title> (<entry-id>) → mentioned in <call-id>
```
If git push OR email fails, also write the same summary to
`knowledge-hub/daily-scrape-<date>-draft.md` as the fallback so the run isn't lost.

## 9. Guardrails
- Real specifics + Sev's voice. No invented numbers. No PII beyond first name + business descriptor (no phones/emails).
- Don't duplicate existing entries; prefer mentions for repeats.
- If a call yields nothing reusable, skip it and note it. A quiet day with 0 new entries is a valid run.
