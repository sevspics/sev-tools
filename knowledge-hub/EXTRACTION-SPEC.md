# Knowledge Hub — Extraction Spec (canonical)

**This is the source of truth for how new knowledge entries are added to `knowledge-hub/index.html`.**
The daily scrape (and any agent adding entries) MUST follow this. As of 2026-06, every new entry's
`formats` uses the **multi-variant (cyclable) structure** below — NOT the old single-brief shape.

Canonical working copy & repo: `~/Desktop/Claude Projects/Sevs Brain/Sev's Brain/sev-tools` (clone of
`github.com/sevspics/sev-tools`, published via GitHub Pages from `main` root →
https://sevspics.github.io/sev-tools/knowledge-hub/). The `~/Desktop/Claude Projects/sev-tools` clone is STALE — do not use it.

The live gold-standard reference entry is `chris-pemberton-may29-01` ("Unique Selling Personality")
inside `knowledge-hub/index.html`. When in doubt, copy its `formats` shape exactly.

---

## 1. Entry schema (unchanged)
Each entry is one object in the `ENTRIES` array:
```json
{
  "id": "<sourceId>-NN",
  "title": "Punchy Title Case (Parenthetical Detail)",
  "category": "<one of: strategy, hooks, formats, workflow, platform, brand, sales, ai, mindset>",
  "funnel": ["ALL"]  // or a subset of ["TOF","MOF","BOF"],
  "sourceId": "<call id in CALLS>",
  "mentions": [],
  "type": "<one of: framework, tactic, reframe, principle, case-study, mindset, tool, resource>",
  "description": "3–6 sentences: what the insight IS and WHY it works. Specific, not generic.",
  "context": "Where it came from — first name + business descriptor + what happened on the call.",
  "businessTypes": ["3–5 from the allowed list"],
  "tags": ["six","lowercase","hyphenated","topical","search","tags"],
  "formats": { ... see §2 ... }
}
```

## 2. `formats` — multi-variant structure (THE CHANGE)
Six format keys, each holding an array of cyclable **variants** (the UI lets the user cycle and copy one):
```
"formats": {
  "faceless":           { "styleNote": "💡 Also test: …", "variants": [ V, V, V, V, V ] },   // 5
  "meme":               { "styleNote": "💡 Also test: …", "variants": [ V, V, V, V, V ] },   // 5
  "candid":             { "variants": [ CANDID_V ] },                                          // 1 (special shape)
  "framed":             { "styleNote": "💡 …", "variants": [ V, V, V, V, V ] },               // 5
  "visual-storyteller": { "styleNote": "💡 …", "variants": [ V, V, V ] },                     // 3
  "talking-head":       { "styleNote": "💡 …", "variants": [ V, V, V ] },                      // 3
  "threeps":            { "styleNote": "💡 …", "variants": [ V, V, (V) ] }                      // 2–3  (3 P's Script)
}
```
Total = **22 standard variants** (5+5+1+5+3+3) **+ 2–3 "3 P's Script" variants** = up to **25 per entry**.

A normal variant `V` = `{ "label", "hook", "body", "cta", "notes" }`.
The **candid** variant is special = `{ "label", "origin", "question", "hooks": [5], "cta", "notes" }`
(NO `body`, NO `hook`; the 5 contrarian/elicitation opener options live in `hooks`).

### Required variant styles (labels + approach — match the gold standard)
- **Faceless (5):** Caption Teach (Setup→Tension→Payoff) · Aesthetic B-roll + One Line · Kinetic Typography (Word Hits) · Receipts (Screen-Record Proof) · Numbered List (3-Rule Overlay)
- **Meme (5):** Two-Panel Contrast · Single Reaction (One Clip + Text) · Nobody / Me: Format · Text-Thread Screenshot · Two-Buttons (Hard Choice)
- **Candid (1):** "The Question (Re-told, Properly Filmed)" — `origin` = the real spark from the call (re-recorded properly, not on the original Zoom); `question` = the prompt Sev answers unscripted; `hooks` = 5 contrarian/elicitation openers.
- **Framed (5)** — one per attention-retention technique: Open Loop (Withhold The Payoff) · Contrarian Cold Open · Stakes & Cost (What It's Costing You) · Numbered Promise (3 Reasons) · In Medias Res (Drop Mid-Story)
- **Visual Storyteller (3):** Before / After Arc · Single-Subject Vignette · Time-Compression Montage
- **Talking Head (3):** High-Conviction Rant · Calm Authority (Measured) · Rapid-Fire (Punchy List)
- **3 P's Script (2–3):** to-camera scripts on Sev's **Promise → Progression → Payoff** framework (every video is a trust deposit). Variant opens: Contrarian Open · Story Open (Client Scene) · Tactical Open (Do-This). Uses the **normal `{label,hook,body,cta,notes}` shape**, mapped: **hook = the PROMISE** (the to-camera opener, plain words a stranger gets in 3s); **body = `[PROGRESSION]` beats then `[PAYOFF]`** (line-broken, 3–4 tight beats, ~40–60s); **cta = the ask AFTER the payoff** (reuse the entry's code word); **notes = duration + one-line "why it works"**. Each variant is a clean trust loop: ONE clear promise, paid off in full BEFORE the ask (never value-edge). `styleNote`: `"💡 Every 3 P's script is a trust deposit — one clear promise, paid off in full before any ask. The two ways it breaks: a vague promise, or value-edging (dangling the payoff behind 'comment X')."` (Format key `threeps`; registered in `FORMATS`. Source: `the-3-ps.html` / `the-3-ps-applied.html`.)

## 3. Hard rules (copy from the gold standard)
1. **Backbone first.** Decide ONCE per entry and reuse across all 7 formats (incl. 3 P's Script): the core reframe, the proof point (real name/number from the call), a signature payoff line, and ONE uppercase **CTA code word**.
2. **Hooks are deliverable lines** prefixed by the delivery surface: `"On-screen text over … — '…'"`, `"Spoken, walking — '…'"`, `"Direct to camera, fast — '…'"`, `"Title text over two panels — '…'"`, `"Voiceover over visual — '…'"`.
3. **Bodies use literal `\n` line breaks between beats** — one beat per line, e.g. `"[SETUP] …\n[TENSION] …\n[PAYOFF] …"` (simpler variants use `[VIBE]/[ONE LINE]/[CAPTION CARRIES IT]`, `[1]/[2]/[3]`, `[ONE SHOT]/[TEXT TURN]/[BUTTON]`; 3 P's Script uses `[PROGRESSION]` beats + `[PAYOFF]`).
4. **Stage directions (camera, length in seconds, music, pacing) go ONLY in `notes`** — never in hook/body/cta.
5. **CTA code word is identical across all 7 formats** (phrasing adapts: Comment/DM/Save/Tag/Follow). A few Tag/Save/Follow CTAs may stand alone, mirroring the gold standard's distribution.
6. **Signature payoff line** closes most bodies (faceless caption-teach, framed, visual-storyteller, talking-head at minimum).
7. Real specifics + Sev's voice. No invented numbers. No phone numbers/emails — first names + business descriptor only.
8. `styleNote` (a "💡 Also test: …" coaching line) on every format EXCEPT candid.

## 4. Renderer compatibility
`renderCreator` / `buildFormatCard` / `cycleVariant` / `copyBrief` in `index.html` already handle BOTH shapes:
old single-object `formats[key] = {hook,body,cta,notes}` renders as a single card; the new
`{variants:[…], styleNote}` renders with the `‹ Style N / M ›` cycler. Variant selection persists in
`localStorage` (`variant_<id>_<key>`). So legacy entries keep working — but all NEW entries use §2.

## 5. Mentions (unchanged)
When a new call references an already-indexed framework, append the call id to that entry's `mentions`
array (drives the 🔁 multiplier badge). Record these in the daily scrape summary.
