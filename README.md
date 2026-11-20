# Henry Oderinde — Academic portfolio

A buildless, responsive academic website. The deployable site is in `dist/`; no dependency installation or build step is needed.

## Preview

Run `python3 -m http.server 4321 --bind 127.0.0.1 --directory dist` from this folder. Open `http://127.0.0.1:4321`.

## Content and maintenance

- `dist/index.html`: academic profile, research, selected projects, education, community service, and contact.
- `dist/styles.css`: responsive layout and typography.
- `dist/script.js`: active navigation state.
- `dist/cv.html`: printable academic résumé; use its print button to save a PDF.
- `dist/assets/`: portrait and project screenshots from the existing professional portfolio.
- `.openai/hosting.json`: Sites identity and static hosting configuration. Preserve the project ID.

Content was adapted from `/Users/macbook/Documents/GitHub/henryoderinde/src/lib/portfolio-data.ts`, its About and Contact routes, and the research title supplied in chat on November 20, 2026. The portrait was downloaded from the asset URL declared in that portfolio's `headshot-suit.jpg.asset.json`. The source portfolio was left unchanged.

Design references: https://jiahuan-long.github.io/jiahuan-long-academic/ and https://frank.csail.mit.edu/. The supplied Megan Gross URL was inaccessible during review.

## Publication accuracy

The final-year work is listed as an unpublished manuscript in preparation. The user confirmed its exact title but has not confirmed submission, review, acceptance, venue, coauthors, or a public paper URL. Do not invent these details. The sole author display identifies the project owner; confirm full manuscript authorship before turning this into a formal publication citation.

The other portfolio reference to teaching programming in African universities has been omitted because its title and status were not confirmed. Degree dates and class of 2026 reflect the portfolio; completion is not independently verified. Project impact figures are portfolio-reported and have not been independently audited. The résumé is a concise sourced draft rather than a complete application CV.

## Validation

Check JavaScript with `node --check dist/script.js`. Local asset/page targets and section anchors were checked with Python's HTMLParser. Browser checks covered image loading, navigation, disclosure controls, and a 390px mobile viewport without horizontal document overflow.

New Sites are private by default. A public, logged-out application link requires a deliberate audience change; do not change access without the user's instruction.
