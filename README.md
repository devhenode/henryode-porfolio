# Henry Oderinde — Academic portfolio

A buildless, responsive academic website. The deployable site is in `dist/`; no dependency installation or build step is needed.

## Preview

Run `python3 -m http.server 4321 --bind 127.0.0.1 --directory dist` from this folder. Open `http://127.0.0.1:4321`.

## Deploy on Vercel

Push this folder to your own repository and import it in Vercel. The included `vercel.json` serves `dist` directly with no build or install step. If you push the containing `henry-academics` folder instead, its root configuration serves `academic-site/dist`.

Keep Framework Preset set to Other. No environment variables are needed. After choosing your final domain, make `og:image` in `dist/index.html` an absolute image URL on that domain for social sharing.

Do not publish or sync to ChatGPT Sites. The original private Sites deployment remains online because this session has no unpublish tool; take it offline through the Sites management UI. Its identity is retained locally only for tracking that cleanup.

## Content and maintenance

- `dist/index.html`: academic profile, research, selected projects, education, community service, and contact.
- `dist/styles.css`: responsive layout and typography.
- `dist/script.js`: active navigation state.
- `dist/cv.html`: printable academic résumé; use its print button to save a PDF.
- `dist/assets/`: portrait and project screenshots from the existing professional portfolio.
- `.openai/hosting.json`: legacy Sites identity retained for cleanup tracking; excluded from Vercel uploads.

Content was adapted from `/Users/macbook/Documents/GitHub/henryoderinde/src/lib/portfolio-data.ts`, its About and Contact routes, and the research title supplied in chat on November 20, 2026. The portrait was downloaded from the asset URL declared in that portfolio's `headshot-suit.jpg.asset.json`. The source portfolio was left unchanged.

Design references: https://jiahuan-long.github.io/jiahuan-long-academic/ and https://frank.csail.mit.edu/. The supplied Megan Gross URL was inaccessible during review.

## Publication accuracy

The academic profile and résumé were updated from the user's November 20, 2026 clarification: interests in AI, ML, and NLP; strong frontend/backend and scalable systems experience; team contributions to QwamPay; comfort with AI workflow tools; research, analytical thinking, collaboration, and consistent personal development. Formal teaching experience is a six-month Teaching Practice internship teaching SS3 Computer Science, averaging five 45-minute periods per week. School name and placement dates were not supplied and are omitted. Total classroom hours are now estimated at 97.5, using five 45-minute periods weekly over an assumed 26 teaching weeks; this is not an attendance-verified total. No student outcomes are inferred.

The final-year work is listed as an unpublished manuscript in preparation. The user confirmed its exact title but has not confirmed submission, review, acceptance, venue, coauthors, or a public paper URL. Do not invent these details. The sole author display identifies the project owner; confirm full manuscript authorship before turning this into a formal publication citation.

The other portfolio reference to teaching programming in African universities has been omitted because its title and status were not confirmed. Degree dates and class of 2026 reflect the portfolio; completion is not independently verified. Project impact figures are portfolio-reported and have not been independently audited. The résumé is a concise sourced draft rather than a complete application CV.

## Validation

Check JavaScript with `node --check dist/script.js`. Local asset/page targets and section anchors were checked with Python's HTMLParser. Browser checks covered image loading, navigation, disclosure controls, and a 390px mobile viewport without horizontal document overflow.

Hosting preference: the user will push to their own repository and deploy on Vercel. Do not deploy automatically.

Browser-review updates: the user corrected LeAi reach to 10,000+ students, confirmed Python backend/algorithms and React/TypeScript frontend, and expanded ATC Africa leadership to six programs, managing leads across three Ogun State campuses, team check-ins, facilitation, and speaking. These user corrections supersede the older portfolio figures.
