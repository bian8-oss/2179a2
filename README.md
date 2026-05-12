# Set Aside — Australia's National Reserve System

A visual essay on Australia's protected areas for **FIT2179 Data Visualisation 2** (Monash University, Semester 1 2026).

🔗 **Live site**: https://bian8-oss.github.io/2179a2/

## Domain

How much of Australia is set aside for nature — and is it the right land?

## Tech

- [Vega-Lite](https://vega.github.io/vega-lite/) for all charts and maps
- Vanilla HTML / CSS for layout and typography
- Hosted on GitHub Pages

## Data sources

- **CAPAD 2024** — Collaborative Australian Protected Areas Database (DCCEEW). [Source](https://www.dcceew.gov.au/environment/land/nrs/science/capad/2024)
- **IBRA bioregions** — Interim Biogeographic Regionalisation for Australia.
- **State boundaries** — derived from the ABS via [rowanhogan/australian-states](https://github.com/rowanhogan/australian-states), CC BY.

## Structure

```
├── index.html          ← The web page
├── css/style.css       ← Styles
├── js/                 ← Vega-Lite JSON specifications
└── data/               ← CSVs, GeoJSONs, etc.
```

## Author

J. Bian — Monash University, May 2026.
