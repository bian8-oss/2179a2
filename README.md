# Set Aside — Australia's National Reserve System

A visual essay on Australia's protected areas, built for **FIT2179 Data Visualisation 2** at Monash University.

**Live site**: <https://bian8-oss.github.io/2179a2/>

## Overview

Australia has protected an area larger than Germany, France and Spain combined — more than 22% of its landmass. This project tells the story of *where*, *who*, and *whether it's enough* through 13 interactive Vega-Lite visualisations.

## 6 Sections

| # | Section | Charts | Key Insight |
|---|---------|--------|-------------|
| 1 | **The Big Picture** | Scale comparison, National map | The scale is staggering |
| 2 | **The Paradox** | Bioregion grid, IUCN categories, Marine vs terrestrial | 22% protected, but not the right 22% |
| 3 | **The Quiet Revolution** | IPA timeline, Governance types | Indigenous Protected Areas = nearly half the NRS |
| 4 | **A Century of Protection** | Cumulative area, State slope chart | From 1879 to 14,000+ parks today |
| 5 | **Victoria's Paradox** | LGA chart, Parks scatter, Species map | Most populated state, lowest protection |
| 6 | **Looking Forward** | 30 by 30 dashboard | Closing the gaps by 2030 |

## Tech Stack

- **Vega-Lite v5** — all 13 charts (mandatory per assignment)
- **Vanilla HTML/CSS** — no framework
- **Google Fonts** — Fraunces (display) + Public Sans (body)
- **GitHub Pages** — hosting

## 13 Visualisations

All charts use real CAPAD 2024 data:

1. **Scale comparison** (custom infographic) — AU protected vs DE+FR+ES
2. **National choropleth map** — Protected area % by state
3. **Bioregion grid** (custom) — 89 IBRA regions vs 17% target
4. **IUCN categories** — Horizontal bar by management category
5. **Marine vs terrestrial** (custom dumbbell) — State-by-state comparison
6. **IPA growth timeline** (custom area) — 1998–2024 cumulative
7. **Governance types** — Bar chart by management authority
8. **Cumulative protection** (custom area) — 1879–2024 with milestones
9. **State slope chart** — 2010 vs 2024 change
10. **Victoria LGA bars** — Protection % by local government area
11. **Victorian parks scatter** — Age vs area of flagship parks
12. **Species vs protection** (custom bivariate) — Threatened species gap analysis
13. **30 by 30 dashboard** (custom) — Gap to 2030 target by jurisdiction

## Data Sources

- **CAPAD 2024** — Collaborative Australian Protected Areas Database, DCCEEW
- **IBRA Bioregions** — Interim Biogeographic Regionalisation for Australia
- **Australian state boundaries** — rowanhogan/australian-states (CC BY)
- **Atlas of Living Australia** — Threatened species data

## File Structure

```
2179a2/
├── index.html              # Main page with 6 sections
├── css/
│   └── style.css           # Australian natural palette design system
├── js/
│   └── chart-XX-*.json     # 13 Vega-Lite specifications
├── data/
│   ├── *.csv               # 14 processed data files
│   └── aus-states.geojson  # Australian state boundaries
└── README.md
```

## Design System

**Palette** (Australian natural):
- Warm sandstone background: `#f5efe6`
- Deep eucalyptus green: `#3f4a2a`
- Outback ochre: `#c66b3d`
- Sky blue: `#6b8b9e`

**Typography**:
- Display: Fraunces (serif, variable opsz)
- Body: Public Sans (300–600)
- Body size: 19px (never smaller)

**Layout**:
- Max width: 1500px (hard ceiling for laptop screens)
- Content width: 760px (prose)
- Wide width: 1500px (charts)

## Author

J. Bian · Monash University · May 2026
