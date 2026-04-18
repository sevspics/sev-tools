---
name: content-matrix-builder
description: >
  Generates a complete 6x6 Content Matrix (36 concepts) for any client from
  just a website URL, using deep industry research, competitor analysis, and
  target-audience pain-point mapping. Produces a single self-contained HTML
  asset that functions as both a client-facing "already built" deliverable
  and an internal execution planner. Use this skill whenever the user says
  anything like: "build a content matrix", "generate 36 content ideas",
  "run the matrix for this client", "do the content blitz for [business]",
  "build the 6x6", or provides a client URL and asks for content concepts.
  Also trigger when a user asks for a content plan anchored in the Daecian
  6-pillars-x-6-formats methodology, or when they want a done-for-you content
  concept deliverable that integrates the Endless Customers Selling 7 for
  YouTube/GEO searchability. This skill sits DOWNSTREAM of client-onboarding
  and endless-customers-strategy-builder — it can run standalone from just a
  URL, or consume their outputs if available.
---

# Content Matrix Builder

Takes a client website URL and produces a ready-to-execute 36-concept Content
Matrix (6 Pillars x 6 Formats) with industry research, competitor analysis,
pain-point mapping, hook suggestions, a 30-day posting calendar, distribution
math projection, and an embedded Selling 7 YouTube/GEO layer — all in one
self-contained HTML file that the client sees as "already built, just press go."

---

## When To Use

Trigger on any of these:
- "Build the content matrix for [client/URL]"
- "Run the 6x6 on [URL]"
- "Generate 36 content concepts for [business]"
- "I need the content blitz for this client"
- User pastes a URL and asks for content ideas or a content plan
- User finishes the client-onboarding skill and wants the next deliverable
- Any request that implies "turn a website into a filmable content plan"

---

## Inputs

The user provides:

1. **Client website URL** (mandatory) — the one input required to run
2. **Client-onboarding output** (optional) — if it exists from a prior run,
   read it from `/mnt/user-data/uploads/` or the conversation context
3. **Industry context notes** (optional) — user may add colour: "they're
   premium", "they hate being salesy", "target audience is 45+ women"

If only a URL is provided, proceed. Do not stall asking for more — the
research phase compensates.

---

## Workflow

### Step 1 — Deep Research Phase

This is the phase that makes the output feel "already done." Do not skip.

**1a. Website intelligence** — Use `web_fetch` on the homepage, then spider:
- About / Our Story
- Services / Products / Shop
- Pricing page (flag if missing)
- Blog / Resources (note topics and recency)
- FAQ page (GOLD for content ideas — these are the literal questions)
- Testimonials / Case Studies
- Contact / Booking
- Any existing YouTube or video content

Extract:
- **What they sell** (exact services/products, in their own words)
- **Who they serve** (ICP — industry, demographics, geography)
- **How they position** (premium, mid, budget — tone, language)
- **Their stated differentiators** (from homepage headline + about page)
- **Current content maturity** (blog frequency, video presence, social)
- **Proof bank** (testimonials, awards, case study depth)
- **Their voice** (formal/casual, technical/plain, corporate/personal)

**1b. Industry research** — Run `web_search` queries like:
- `"[industry] biggest customer complaints"`
- `"[industry] common questions buyers ask"`
- `"how to choose a [service provider]"`
- `"[service] cost" OR "[service] price"`
- `"[industry] red flags"` / `"[industry] scams"`
- `"[industry] trends 2026"`

Extract:
- Top 5 industry pain points (in customer language)
- Top 10 questions target audience is actively asking
- Common misconceptions and objections
- What buyers fear getting wrong
- Emerging trends and shifts (for topical concepts)

**1c. Competitor analysis** — Identify 3 direct competitors from:
- Client website (if they mention any)
- Google searches like `"best [service] in [location]"`
- Industry "versus" searches

For each competitor, briefly note:
- What content they're producing (if any)
- Content gaps — what are they NOT talking about
- Price positioning relative to the client

**1d. GEO angle** — For the Selling 7 YouTube layer, identify:
- What questions AI search engines (ChatGPT, Perplexity, Google AI Overviews)
  are likely to cite
- Long-tail, plain-language questions that map to GEO-friendly YouTube titles
- Format: "How much does X cost?", "Is X worth it?", "X vs Y: which is better?"

---

### Step 2 — Map The 6 Content Pillars To This Client

The pillars are fixed. Your job is to contextualise them with real, specific
subject matter from the research.

| Pillar | What Goes Here | Research Source |
|---|---|---|
| **1. Costs** | Pricing transparency, "how much does X cost", why prices vary, cost breakdowns, cheap vs premium comparison, ROI framing | Pricing page + industry cost searches |
| **2. Pain Points** | The actual problems this audience has, warning signs, things that go wrong, what people regret, anti-pitfall content | Industry pain-point searches + FAQ page |
| **3. Success Stories** | Case studies, transformations, results, before/afters, specific client wins with numbers | Testimonials + case studies page |
| **4. Comparisons** | Them vs competitor, product A vs B, DIY vs professional, premium vs budget options, in-house vs outsource | Competitor analysis + versus searches |
| **5. Best-of Lists** | "Best [service] in [location]", top 5 features to look for, best tools/products, expert picks | Best-in-class searches + client authority |
| **6. Practitioner Journey** | Behind the scenes, day-in-the-life, founder story, why they do this, team introductions, process walkthroughs | About page + client's voice/personality |

For each pillar, write a 1-2 sentence **pillar thesis** specific to this client
— what this pillar looks like for THEIR business.

---

### Step 3 — Generate 36 Concepts (6 x 6 Matrix)

For every Pillar (6), produce one concept in each Format (6). That gives 36.

**The 6 formats and how to execute each:**

| Format | Description | Best For |
|---|---|---|
| **Faceless** | No on-camera presence. Voiceover + B-roll, screen record, text-on-screen. | When founder hates camera, or content is process-heavy |
| **Memes** | Text-based humour, reactions, relatable punchlines, visual gags. | Mass reach, relatability, TOF |
| **Candid** | Phone-shot, raw, behind-the-scenes, unpolished. | Trust, humanness, authenticity |
| **Framed** | Intentional B-roll, shot-listed, edited with style. Documentary-feel. | Mid-funnel trust building, showcasing craft |
| **Visual Storyteller** | Animation, diagrams, kinetic typography, illustrated explainers. | Explaining complex concepts, standing out in feed |
| **Talking Head** | Direct-to-camera, authority delivery. Podcast clip style or standalone. | Authority, MOF/BOF, YouTube long-form |

**For each of the 36 concepts, produce:**
- **Title** — punchy working title (not final)
- **Hook** — first 2-5 seconds, front-loaded with keywords (Andromeda rule)
- **Core idea** — 1-2 sentences on what the content is actually about
- **Why it works** — specific reason this pillar + format combo lands here
- **Production notes** — what's needed to shoot it (location, props, talent)
- **Primary platform** — IG Reels / TikTok / YouTube Shorts / YouTube long-form / LinkedIn
- **GEO tag** — if applicable, the plain-language search query this answers

**Quality rules:**
- No generic concepts. Every idea must reference THIS client's industry,
  audience, offer, or voice.
- No repeat angles. 36 distinct ideas, not 6 ideas dressed 6 ways.
- Hooks must pass the Andromeda test: front-load keywords the target audience
  uses in their own language (avoid jargon unless the audience speaks it).
- If a pillar + format combo genuinely doesn't fit for this client, flag it
  and propose the closest viable swap rather than forcing a bad concept.

---

### Step 4 — Overlay The Selling 7 (GEO Layer)

The Selling 7 are non-negotiables for YouTube + website GEO searchability.
These sit ABOVE the matrix as the "must-film" authority pieces.

The 7 videos (always produced, always posted to YouTube, always embedded on
the client's website):

1. **80% Video** — The top 10 questions every prospect asks, answered in one
   video. QQPP opening. 5-10 minutes. Embedded on home page or sales page.

2. **Cost & Price Video** — Honest pricing conversation. Ranges, what drives
   cost, why cheap is risky, Law of the Coin. Embedded on pricing page.

3. **Product/Service-Fit** — Who this is for, who this isn't for. Disarmament
   opening. Embedded on services pages.

4. **Landing Page Video** — Short conversion-focused video per key landing
   page. 60-90 seconds. "Here's what you'll get, here's who this is for."

5. **Customer Journey** — Jake Standard format. Hero's journey case study
   with the client as guide. Embedded on case studies page.

6. **Bio / Founder Video** — Who the founder/team is, why they do this.
   Embedded on About page. Humanises the brand.

7. **Claims We Make** — Every bold claim on the website gets a companion
   video proving it. "We say X. Here's the proof."

**For each Selling 7 video, produce:**
- Specific topic tailored to the client
- Suggested YouTube title (GEO-optimised, plain language)
- Which page of their website it embeds on
- Estimated length
- Production format (usually Framed or Talking Head)

---

### Step 5 — Build The 30-Day Posting Calendar

Use the 80/20 rule: 80% proven, 20% experimental.

**Cadence target:**
- 15-20 short-form posts over 30 days (matrix concepts)
- 2-4 YouTube long-form uploads (Selling 7 + expanded matrix)
- Distributed across the client's confirmed platforms

**Structure the calendar:**
- Week 1: Foundation week — lead with Success Stories + Practitioner Journey
  to build immediate trust
- Week 2: Pain Points + Costs (the two highest-converting pillars)
- Week 3: Comparisons + Best-of (authority and education)
- Week 4: Mix + republish winners + test 20% experimental

Map specific concepts from the 36 to specific days. Do not be vague.

---

### Step 6 — Project The Distribution Math

Use Sev's worst-case framework, contextualised to this client:

```
[X] videos/month → [Y]K total views → [Z]% engagement 
  → [A]% enquire → [B]% convert = [N] clients
```

Use conservative numbers:
- 10K views per 10 videos at minimum (unless audience is tiny/hyperlocal)
- 10% engagement rate
- 10% of engaged audience inquires
- 10% of inquiries convert (adjusted for B2B higher-ticket scenarios)

Include THREE scenarios on the HTML:
- **Worst case** (10/10/10/10)
- **Realistic** (15% engagement, 12% inquiry, 15% conversion)
- **Best case** (25% engagement, 15% inquiry, 25% conversion)

Multiply through to new clients per month and 12-month revenue projection
using the client's known or estimated average client value.

---

### Step 7 — Build The HTML Output

Read `references/html_template.md` for the full design system, CSS variables,
and component specs. The output is a single self-contained `.html` file with
TWO view modes toggleable via a top-right switch:

**View A — Client Mode** (default):
- Polished, editorial, "this is already built"
- Hero section with client name + tagline
- Research summary (concise, confident)
- The 36-concept grid (visual, filterable by pillar + format)
- Selling 7 section (displayed as a YouTube "authority stack")
- 30-day calendar (visual timeline)
- Distribution math (interactive sliders optional, static acceptable)
- Zero internal jargon

**View B — Internal Mode**:
- Same content, extra technical detail revealed
- Production notes expanded
- Pillar theses visible
- Research methodology visible (sources used, searches run)
- Pre-shoot checklist per concept
- Internal shot list templates

Both views share the same data model — toggle just shows/hides fields and
changes the styling density.

**Design system:**
- IBM Plex Sans (body) + IBM Plex Mono (accents) OR DM Sans + DM Serif Display
  — match whatever the client-onboarding HTML used if it exists for this
  client, otherwise default to IBM Plex Sans + IBM Plex Mono
- Dark industrial palette (matches Sev's existing tools):
  - Background: `#0a0a0a`
  - Surface: `#141414`
  - Border: `#262626`
  - Text primary: `#f5f5f5`
  - Text secondary: `#a3a3a3`
  - Accent: `#d4a574` (warm gold — authority, not salesy)
  - Accent secondary: `#6ee7b7` (mint — highlights GEO tags and wins)
- Monospace accents for numbers, dates, IDs
- Heavy use of visible structure — grids, borders, row separators
- No gradients, no glassmorphism, no drop shadows beyond 1px borders

**Technical requirements:**
- Self-contained single HTML file (no external JS frameworks)
- localStorage for view mode persistence and any user notes per concept
- Filter buttons: by Pillar, by Format, by Platform, by GEO-tagged only
- Each concept is a card with a "copy to clipboard" button for its brief
- Print-friendly CSS for when the client wants to print it

Save to `/mnt/user-data/outputs/[client-name]-content-matrix.html`

---

### Step 8 — Save And Present

Save the HTML to outputs. Optionally save a markdown companion with the same
concepts in plain text for advisor reference.

Call `present_files` with the HTML path first.

Close with a concise summary: what was built, what's next (usually: film the
80% Video and one Success Story in the first week, then batch-produce the
matrix concepts in a single shoot day).

---

## Cross-Skill Integration

- **Upstream**: If `client-onboarding` has already run for this client, read
  its markdown output to pre-fill the research phase and skip redundant
  website fetching.
- **Downstream**: After this skill runs, offer:
  - "Want me to turn the top 5 concepts into full scripts?"
  - "Want me to build the Endless Customers full strategy layer on top?"
  - "Want me to generate the Grand Slam Offer page that this content drives
    traffic to?"

---

## Writing Voice Rules (Sev's Preferences)

- No em-dashes, anywhere, ever
- No AI-cliché phrases ("in the ever-evolving", "it's important to note",
  "game-changer", "dive into", "unleash", "leverage" used lazily)
- Direct, assertive, teacher-brained tone
- Short punchy sentences
- "We" not "you" when framing execution
- Numbers > adjectives
- Specific > generic, always

---

## Quality Checklist

Before saving:

- [ ] Website was fetched and multiple key pages researched (not just homepage)
- [ ] At least 5 industry-specific web_search queries were run
- [ ] 3 competitors were identified and briefly analysed
- [ ] All 6 pillar theses are specific to this client (not generic)
- [ ] All 36 concepts have unique angles (not repeats)
- [ ] Every concept has title + hook + core idea + why + production + platform
- [ ] Hooks are front-loaded with plain-language keywords
- [ ] All 7 Selling 7 videos have client-specific topics and YouTube titles
- [ ] 30-day calendar maps specific matrix concepts to specific days
- [ ] Distribution math uses client-specific assumptions (not defaults)
- [ ] Both Client Mode and Internal Mode views render correctly
- [ ] Filters work: Pillar, Format, Platform, GEO-tagged
- [ ] localStorage persists view mode and notes
- [ ] No em-dashes anywhere in the output
- [ ] File is self-contained and opens offline
- [ ] File is saved to /mnt/user-data/outputs/
- [ ] present_files was called
