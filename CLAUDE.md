# CLAUDE.md — Set Aside (FIT2179 Data Visualisation 2)

> Context file for new Claude Code sessions. Read this first.

---

## 1. The project at a glance

A 6-section visual essay on **Australia's National Reserve System** (protected areas / national parks), built for **FIT2179 Data Visualisation 2** at Monash University.

- **Live site**: <https://bian8-oss.github.io/2179a2/>
- **Repo**: <https://github.com/bian8-oss/2179a2>
- **Deadline**: Friday 29 May 2026, 11:55 PM (Week 12)
- **Weight**: 25% of unit
- **Target grade**: HD (80–100). Realistic estimate at current pace: D–HD borderline.

The user is a Monash student. This is their second of two visualisation assignments. **DV1 was about kangaroos** — DV2 must be clearly distinct, so this project focuses on the **land protection system itself** (categories, governance, bioregions), not the wildlife inside parks. Crossing that line risks a 0.

## 2. The core argument

> *"Australia has protected an area larger than Germany, France and Spain combined. But is it the right land, and is it enough?"*

The story moves through 6 sections with an emotional arc: **pride → concern → inspiration → reflection → action**.

| # | Section | Hook (in own words) |
|---|---|---|
| 1 | **The Big Picture** | The scale is staggering. |
| 2 | **The Paradox** | 22% of the country is protected, but not the right 22%. |
| 3 | **The Quiet Revolution** | Indigenous Protected Areas — emotional centerpiece. |
| 4 | **A Century of Protection** | From 1879 to today. |
| 5 | **Victoria's Paradox** | Most populated state, lowest protection. |
| 6 | **Looking Forward** | 30 by 30 target — closing reflection. |

## 3. Tech stack

- **Vega-Lite v5** for all charts (loaded via CDN, mandatory per assignment)
- **Vanilla HTML / CSS** for layout (no framework)
- **Google Fonts**: Fraunces (display serif) + Public Sans (body)
- **GitHub Pages** for hosting
- **No build step** — just push to `main` and GitHub Pages serves it

The user is on **Windows / PowerShell / VS Code**. Bash-only commands need translation (e.g., `New-Item` instead of `touch`, separate `mkdir` calls instead of `mkdir a b c`).

## 4. File structure

```
2179a2/
├── index.html              ← page (6 sections, hooks, embed script at the bottom)
├── README.md
├── CLAUDE.md               ← this file
├── css/
│   └── style.css           ← single stylesheet, ~7 KB
├── js/
│   └── chart-XX-name.json  ← one Vega-Lite spec per chart
├── data/
│   ├── aus-states.geojson  ← state boundaries (233 KB, CC BY)
│   ├── iucn-categories.csv ← derived from CAPAD 2024
│   └── gen_iucn.py         ← Python script that generated the above
└── sketch/                 ← (TODO) PDF of the hand-drawn sketch
```

Every chart is **one self-contained JSON file** under `js/`. Embed in `index.html` via `vegaEmbed('#chart-XX-name', 'js/chart-XX-name.json', vlOpts)`.

## 5. Design system

CSS variables (in `:root` of `style.css`):

```css
/* Palette — Australian natural */
--bg:         #f5efe6;   /* page background, warm sandstone */
--bg-deep:    #ebe0cf;   /* feature section background */
--ink:        #1a1a1a;
--ink-soft:   #4a4641;
--ink-muted:  #8a8278;
--rule:       #d8cdb7;

--green:       #3f4a2a;   /* deep eucalyptus — Strict protection */
--green-soft:  #6e7d4c;   /* mid green — Conservation */
--ochre:       #c66b3d;   /* outback ochre — Sustainable use */
--ochre-soft:  #d99970;
--rust:        #8c3e1e;
--sand:        #b68a6e;
--sky:         #6b8b9e;

/* Typography */
--serif: "Fraunces", "Iowan Old Style", Georgia, serif;
--sans:  "Public Sans", -apple-system, system-ui, sans-serif;

/* Layout */
--content-width: 760px;   /* prose, headers, hooks */
--wide-width:    1500px;  /* charts and chart-grids */
--max-width:     1500px;
```

**Body font is 19px.** Don't shrink it.

**Width cap is 1500px** — this is the assignment's hard ceiling. Going wider triggers horizontal scrolling on 1366px laptops, which is an automatic mark deduction. Don't go above.

## 6. Chart spec conventions

Every chart JSON should follow this skeleton:

```json
{
  "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
  "description": "What this chart shows. Data source.",
  "background": "transparent",
  "padding": {"top": 20, "right": 20, "bottom": 20, "left": 20},
  "width": "container",
  "height": 480,

  "title": {
    "text": "Sentence-case headline question or claim",
    "subtitle": ["Plain-language explanation.", "Optional second line with the insight."],
    "anchor": "start",
    "frame": "group",
    "font": "Fraunces",
    "fontSize": 28,
    "fontWeight": 700,
    "color": "#1a1a1a",
    "subtitleFont": "Public Sans",
    "subtitleFontSize": 15,
    "subtitleColor": "#4a4641",
    "subtitlePadding": 8,
    "offset": 14
  },

  "data": {"url": "data/something.csv"},

  "layer": [ /* … */ ],

  "config": {
    "view": {"stroke": null},
    "axis": {"labelFont": "Public Sans", "titleFont": "Public Sans"}
  }
}
```

**Gotchas already learned the hard way:**

1. **Never combine `width: "container"` with an `autosize` directive.** They conflict and the chart silently renders blank. `"container"` implies `fit` autosize already.
2. **`width: "container"` requires the parent `.chart-container` to be `display: block` with explicit width.** If you accidentally re-add `display: flex` to `.chart-container` (only allowed inside `:empty`), Vega-Lite measures width 0 and chart vanishes.
3. **Chart text colour is `#f5efe6`** (the page bg) for labels rendered on top of coloured rects. Failing data load = invisible chart on cream page (no contrast).
4. **GitHub Pages caches aggressively.** Always verify deployment via direct URL: `https://bian8-oss.github.io/2179a2/js/chart-XX.json` should show the latest content. Hard-refresh (Ctrl+Shift+R) the page.

## 7. Chart status

| # | Section | Chart | Idiom | Custom? | Status |
|---|---|---|---|---|---|
| 1 | 1 | Scale comparison (AU vs DE+FR+ES) | Custom infographic | ⭐ | TODO |
| 2 | 1 | All protected areas map | Point map | | TODO |
| 3 | 2 | Bioregion completeness | Hex grid / waffle | ⭐ | **NEXT** |
| 4 | 2 | IUCN categories | Treemap | | ✅ **DONE** |
| 5 | 2 | Marine vs terrestrial by state | Dumbbell | | TODO |
| 6 | 3 | IPA growth timeline | Ribbon timeline | ⭐ | TODO |
| 7 | 3 | Governance type map | Choropleth-ish | ⭐ | TODO |
| 8 | 4 | 1900–2024 cumulative area | Annotated area chart | ⭐ | TODO |
| 9 | 4 | 2010 vs 2024 by state | Slope chart | | TODO |
| 10 | 5 | Victoria LGA choropleth | Choropleth | | TODO |
| 11 | 5 | Top Victorian parks | Annotated scatter | | TODO |
| 12 | 5 | Threatened species vs protection | Bivariate map | ⭐ | TODO |
| 13 | 6 | 30 by 30 dashboard | Custom gauges | ⭐ | TODO |

**6 custom-built charts** is the HD target — "a substantial number of creative custom-built visualisations" per the rubric. Anything below 4 custom-builts drops the ceiling to D.

**Next priority: Chart 3 (Bioregion hex grid).** Data is already in CAPAD national xlsx, sheet `IBRA Bioregions`, 89 rows. Each row has region name, area, % protected. Need to plot as a hex grid colored by % protected vs the 17% international target.

## 8. Data sources (4 total — strong for HD)

| Source | Used in | Files |
|---|---|---|
| **CAPAD 2024** (DCCEEW, [link](https://www.dcceew.gov.au/environment/land/nrs/science/capad/2024)) | Most charts | `data/capad-2024-national.xlsx` (already downloaded) |
| **IBRA bioregions** | Charts 3, 12 | TODO — bundled inside CAPAD xlsx sheet `IBRA Bioregions` |
| **CAPAD historical (2010, 2014, 2018, 2022)** | Charts 8, 9 | TODO — need to download separately |
| **Australian state boundaries** | Maps | `data/aus-states.geojson` ([rowanhogan/australian-states](https://github.com/rowanhogan/australian-states), CC BY) |

The CAPAD xlsx has 7 sheets:
- `Type` — reserve types
- `Jurisdiction` — state-level totals
- `Governance` — Community / Govt / Joint / Private (used for IPA story in Section 3)
- `IUCN Category` — used for Chart 4 ✅
- `IBRA Bioregions` — used for Chart 3 (NEXT)
- `Bioregion by IUCN` — crosstab
- `IBRA Subregions` — finer detail

## 9. Workflow

```bash
# After editing files
git add .
git commit -m "describe what changed"
git push

# Wait ~1–2 minutes, then verify:
#   1. https://github.com/bian8-oss/2179a2/blob/main/<file> shows latest commit
#   2. Hard-refresh https://bian8-oss.github.io/2179a2/ (Ctrl+Shift+R)
#   3. If still old, open the file URL directly and check size matches local
```

When something looks wrong on the live site, the debugging order is:

1. Open browser DevTools → Network tab → hard-refresh → check status codes
2. If a file is the wrong size, the push didn't work — re-commit
3. If 200 but chart blank, check Console for Vega-Lite errors
4. If no errors but blank, suspect the `width: "container"` + parent layout issue (see gotcha 2)

## 10. Assignment rubric quick reference

Total 25% of unit. Mark = 0 if any of these:
- DV2 domain not clearly different from DV1 (kangaroos)
- Web page or any Vega-Lite spec not publicly accessible
- Sketch made with digital tools (-3% also if no sketch / wrong domain)

Marks breakdown:
| Component | Weight | Current trajectory |
|---|---|---|
| Sketch | 2% | ✅ Done, hand-drawn, ~1.6/2 |
| Idioms & complexity | 10% | Target 7.5–8.5 (HD if ≥6 custom-builts ship) |
| Layout / colour / figure-ground | 4% | Design system in place, target 2.8–3.2 |
| Typography | 2% | Fraunces + Public Sans, target 1.5–1.8 |
| Storytelling | 5% | Strong on paper, depends on annotations |
| Description (Moodle 500 words) | 2% | Write at the very end |

## 11. The submission (don't forget)

Moodle submission has 3 parts:
1. **URL** to live GitHub Pages site
2. **URL** to PDF of the hand-drawn sketch (host on GitHub)
3. **500-word description** in a Moodle form covering: domain / who / why / what (data) / how (idiom rationale)

## 12. Communication style with this user

- The user prefers **Chinese** for casual conversation but **English** is fine for technical content. Mixing is normal. If they switch to Chinese, respond in Chinese.
- They explicitly asked to aim for HD but accept the risk of landing at D.
- They appreciate **honest assessment over optimism** — don't sugarcoat. If a plan is over-ambitious, say so.
- They like **structured responses** with tables and clear step lists, but not over-formatted prose.
- They've never used Vega-Lite before this assignment, but they're competent in Python and have done a Tableau project. Don't over-explain basics, but flag genuinely new Vega-Lite concepts.
- They run on Windows / PowerShell. Adjust command syntax accordingly.

## 13. Things NOT to do

- Don't suggest digital sketching tools — the sketch is done, hand-drawn.
- Don't propose making the layout wider than 1500px.
- Don't drift the topic toward wildlife / animals — must stay on the land protection system to avoid DV1 overlap.
- Don't use Inter, Space Grotesk, or other AI-default fonts in any chart styling.
- Don't add interactive features that don't serve the story (rubric explicitly warns against "interactivity for its own sake").
- Don't invent data — every chart must use real CAPAD numbers, with citation.

---

*Last updated by previous Claude session, May 2026. Update this file as the project evolves so future sessions stay in sync.*
