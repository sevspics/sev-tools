# Knowledge Hub — Daily Scrape Routine (operating procedure)

**Run this once per day.** It finds new Fathom calls, harvests reusable knowledge entries, adds them to
the hub **in the 22-variant cyclable format**, records cross-call mentions, commits/pushes, and emails a
summary. This file is the single source of truth for the routine — edit it here, not in the Cowork prompt.

> **Cowork routine prompt should be just:**
> *"Read `knowledge-hub/DAILY-SCRAPE-ROUTINE.md` in the Sevs Brain sev-tools repo and execute it exactly. Today is {{today}}."*

---

## 0. Repo & tools
- **Canonical repo (edit/commit HERE):** `~/Desktop/Claude Projects/Sevs Brain/Sev's Brain/sev-tools`. File: `knowledge-hub/index.html`.
  **NEVER** use `~/Desktop/Claude Projects/sev-tools` — it's a stale clone; editing it regresses the live site.
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

> **CRITICAL — `formats` MUST be the multi-variant structure (EXTRACTION-SPEC §2), never the old single-brief.**
> Lock the backbone once (core reframe · proof point from the call · signature payoff line · ONE uppercase
> CTA code word), then write **5 faceless + 5 meme + 1 candid (5 hook options) + 5 framed + 3 visual-storyteller
> + 3 talking-head + 2–3 "3 P's Script" = up to 25 variants across 7 formats**. Hooks are deliverable lines;
> bodies use `\n` between beats; stage directions live ONLY in `notes`; `styleNote` on every format except
> candid. The 7th format `threeps` is a Promise→Progression→Payoff to-camera script (hook=Promise,
> body=`[PROGRESSION]` beats + `[PAYOFF]`, cta=the ask after the payoff). Gold-standard reference entry:
> `chris-pemberton-may29-01` (6 formats) + any recent entry for the `threeps` shape.

A newly-scraped entry that is still single-brief is a **defect** — do not ship it; convert before committing.

## 4b. Fact-check every entry before it ships (NON-NEGOTIABLE)
Format compliance says nothing about truthfulness. Agents drafting these entries **fabricate at a high rate**,
and the fabrications read as the most vivid copy in the brief — so they survive a structure check untouched.
Every variant is a script that may actually get filmed and published, often naming a real client, so a made-up
quote or anecdote is a reputational problem, not a formatting nit.

After harvesting and before inserting, run a **separate fidelity pass per entry**: re-read the transcript and
demand a supporting line for every number, quote, date, name and asserted event. Default to "cut it" when
uncertain. The recurring failure modes, all seen in the wild:
- **Paraphrase escalated into quotation** — a third-person description of a client becomes a verbatim "review".
- **Invented numbers** — durations, lead counts, conversion rates. Agents reach for a figure when a beat feels thin.
- **Invented events** — advice that was *given* written up as coaching that *happened*; a demo script Sev was
  openly improvising written up as a real client story.
- **Reversed causality** — something Sev raised unprompted rewritten as his answer to a client's question.
- **Vague self-reports hardened into metrics** — "my close rate is pretty good" → "she closes almost everyone".
- **Fabricated after-states** — depicting a result for someone who hasn't bought or hasn't acted yet.

Repairs get **reworded around rather than removed**, so re-verify with fresh eyes, not the agent that wrote it.
The rule that actually prevents it: *no variant may make a third-person factual claim about an identifiable real
person beyond what the transcript literally states.* Three safe framings — second person to the viewer ("your
reviews"), Sev's own first-person experience of the call, or an explicitly-labelled composite with identifying
details stripped (notes must say to cast an actor). When an invention is removed the replacement must be
**plainer, not a new story**: a duller true line beats a vivid false one.

An entry that still has a fabrication is a **defect** — drop that entry and note it as skipped. Shipping fewer,
true entries is always the right trade. A partial run is valid.

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
cd "/Users/sev/Desktop/Claude Projects/Sevs Brain/Sev's Brain/sev-tools"
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
