# Content Matrix HTML Template Reference

This is the structural blueprint for the single-file HTML output. Follow this
skeleton exactly. Fill the data arrays with the 36 concepts, Selling 7,
calendar, and math you generated.

---

## File Structure Overview

```
<!DOCTYPE html>
<html>
<head>
  [meta + fonts + style block]
</head>
<body>
  <div class="shell">
    <header class="masthead">[client name, tagline, view toggle]</header>
    <section class="research">[research summary + pillar theses]</section>
    <section class="selling-seven">[the 7 GEO/YouTube authority stack]</section>
    <section class="matrix">[the 36-concept grid with filters]</section>
    <section class="calendar">[30-day posting calendar]</section>
    <section class="math">[distribution math 3-scenario table]</section>
    <footer class="meta">[generated date, methodology credit]</footer>
  </div>
  <script>[data arrays + filter logic + view toggle + localStorage]</script>
</body>
</html>
```

---

## Design Tokens (Paste Into :root)

```css
:root {
  --bg: #0a0a0a;
  --surface: #141414;
  --surface-2: #1a1a1a;
  --border: #262626;
  --border-strong: #3a3a3a;
  --text: #f5f5f5;
  --text-dim: #a3a3a3;
  --text-faint: #666666;
  --accent: #d4a574;
  --accent-dim: #8a6a47;
  --mint: #6ee7b7;
  --mint-dim: #3d7a5f;
  --red: #f87171;

  --font-sans: 'IBM Plex Sans', -apple-system, system-ui, sans-serif;
  --font-mono: 'IBM Plex Mono', 'SF Mono', Consolas, monospace;

  --radius: 2px;
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 16px;
  --space-4: 24px;
  --space-5: 40px;
  --space-6: 64px;
}
```

---

## Font Loading

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

---

## Key Component Specs

### Masthead

- Full-width, border-bottom
- Left: client name in Plex Sans 700, 32px. Below it, tagline in Plex Mono
  500, 13px, uppercase, accent colour
- Right: view toggle (Client / Internal) as two tabbed buttons
- Small top row: "CONTENT MATRIX" label, generated date, total concept count

### Research Summary

- Two-column grid on desktop, stacked on mobile
- Left column: industry insight cards (pain points, trends, competitor gaps)
- Right column: 6 pillar thesis cards, each with pillar name + 1-2 sentence
  thesis specific to this client
- Internal mode reveals an extra "Methodology" block showing which searches
  and pages were analysed

### Selling 7 Stack

- Horizontal scroll row OR 7-card grid
- Each card: video number (01-07), type name, client-specific topic,
  suggested YouTube title (in mono font), embed location on their website,
  estimated length
- Mint accent highlights the GEO-optimised title
- Each card has a "copy brief" button

### Matrix Grid (The 36)

- 6-column x 6-row visual grid on desktop
- Rows = Pillars (left sticky column labels)
- Columns = Formats (top sticky row labels)
- Each cell = one concept card
- Card front shows: title + format icon + platform badge
- Click expands to full brief: hook, core idea, why, production notes,
  GEO tag if any
- Filter bar above grid: [All] [Pillar ▼] [Format ▼] [Platform ▼] [GEO only]
- Active filters desaturate non-matching cells rather than hiding them
  (preserves the visual 6x6 grid integrity)

### Calendar

- 30-day timeline as a 6-week grid (with partial rows as needed)
- Each day shows: concept title abbreviation + format dot + platform icon
- Week labels on left
- Hover/tap reveals the full concept
- Colour-code by pillar (subtle border tint, not filled colour)

### Distribution Math

- 3-column table (Worst / Realistic / Best)
- Each row: Videos, Views, Engagement, Inquiries, Conversions, New Clients
- Bottom row: estimated 12-month revenue at client's avg client value
- Numbers in mono font, large
- Bottom note: "Math assumes [client-specific assumption]. Adjust in Internal
  Mode."

---

## View Toggle Implementation

Single data model, CSS class on `<body>` controls visibility:

```html
<body class="view-client">
```

```css
body.view-client .internal-only { display: none; }
body.view-internal .client-only { display: none; }
body.view-internal { /* denser padding, extra gridlines */ }
```

Persist choice to localStorage key `cm_view_mode`.

---

## Data Model (JS)

```js
const MATRIX_DATA = {
  client: {
    name: "",
    url: "",
    tagline: "",
    industry: "",
    icp: "",
    avgClientValue: 0,
    positioning: "" // premium | mid | budget
  },
  research: {
    painPoints: [], // array of {title, detail}
    audienceQuestions: [], // array of strings
    trends: [],
    competitorGaps: [],
    sourcesUsed: [] // internal only
  },
  pillars: [
    { id: 1, name: "Costs", thesis: "" },
    { id: 2, name: "Pain Points", thesis: "" },
    { id: 3, name: "Success Stories", thesis: "" },
    { id: 4, name: "Comparisons", thesis: "" },
    { id: 5, name: "Best-of Lists", thesis: "" },
    { id: 6, name: "Practitioner Journey", thesis: "" }
  ],
  formats: [
    { id: 'faceless', name: "Faceless" },
    { id: 'memes', name: "Memes" },
    { id: 'candid', name: "Candid" },
    { id: 'framed', name: "Framed" },
    { id: 'visual', name: "Visual Storyteller" },
    { id: 'talking', name: "Talking Head" }
  ],
  concepts: [
    // 36 entries, one per pillar x format combination
    {
      id: "p1-faceless",
      pillar: 1,
      format: "faceless",
      title: "",
      hook: "",
      coreIdea: "",
      whyItWorks: "",
      productionNotes: "",
      platform: "", // ig-reels | tiktok | yt-shorts | yt-long | linkedin
      geoTag: "" // optional, e.g. "how much does X cost"
    }
    // ...35 more
  ],
  sellingSeven: [
    {
      id: 1,
      type: "80% Video",
      topic: "",
      ytTitle: "",
      embedLocation: "", // homepage | pricing | services | about etc.
      estimatedLength: "", // "5-8 min"
      format: "talking" // usually
    }
    // ...6 more
  ],
  calendar: {
    // 30 day entries
    days: [
      { day: 1, conceptId: "p3-candid", notes: "" }
      // ...
    ]
  },
  math: {
    assumptions: {
      videosPerMonth: 15,
      avgViewsPerVideo: 1000,
      clientValue: 2500
    },
    scenarios: {
      worst: { engagementRate: 0.10, inquiryRate: 0.10, conversionRate: 0.10 },
      realistic: { engagementRate: 0.15, inquiryRate: 0.12, conversionRate: 0.15 },
      best: { engagementRate: 0.25, inquiryRate: 0.15, conversionRate: 0.25 }
    }
  }
};
```

---

## Filter Logic Sketch

```js
function applyFilters() {
  const cells = document.querySelectorAll('.concept-cell');
  const activePillar = getActiveFilter('pillar');
  const activeFormat = getActiveFilter('format');
  const activePlatform = getActiveFilter('platform');
  const geoOnly = document.getElementById('geo-only').checked;

  cells.forEach(cell => {
    const concept = MATRIX_DATA.concepts.find(c => c.id === cell.dataset.id);
    const match = 
      (!activePillar || concept.pillar === activePillar) &&
      (!activeFormat || concept.format === activeFormat) &&
      (!activePlatform || concept.platform === activePlatform) &&
      (!geoOnly || concept.geoTag);
    cell.classList.toggle('dimmed', !match);
  });
}
```

---

## Copy-To-Clipboard Brief Format

When a user clicks "copy brief" on a concept:

```
[CLIENT NAME] — CONCEPT BRIEF

Pillar: [Pillar Name]
Format: [Format Name]
Platform: [Primary Platform]

TITLE: [title]

HOOK (first 3 seconds):
[hook]

CORE IDEA:
[core idea]

WHY IT WORKS HERE:
[why]

PRODUCTION NOTES:
[notes]

GEO TAG: [geoTag or "N/A"]
```

---

## Accessibility + Print

- All interactive elements have visible focus states
- Filter buttons have aria-pressed
- Print CSS: remove filters, remove view toggle, expand all concepts into
  linear document, use white background black text for ink efficiency
- Print page break after each major section

---

## localStorage Keys

- `cm_view_mode` → "client" | "internal"
- `cm_notes_[conceptId]` → user-entered note per concept (Internal mode only)
- `cm_active_filters` → JSON of active filter state

---

## Final Checklist For HTML

- [ ] All 36 concepts populated with real client-specific content
- [ ] All 7 Selling 7 cards populated
- [ ] 30 calendar entries (at minimum 20 if weekends off)
- [ ] 3 math scenarios calculated with real numbers
- [ ] View toggle works and persists
- [ ] All filters work
- [ ] Copy brief works
- [ ] Print stylesheet included
- [ ] Zero external JS frameworks (vanilla only)
- [ ] Fonts preloaded
- [ ] Works offline after first load (fonts cache)
- [ ] No em-dashes in any copy
