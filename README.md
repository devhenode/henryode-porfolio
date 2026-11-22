# Henry Oderinde — Academic portfolio

A buildless, responsive academic website. The deployable site is in `dist/`; no dependency installation or build step is needed.

## Preview

Run `python3 -m http.server 4321 --bind 127.0.0.1 --directory dist` from this folder. Open `http://127.0.0.1:4321`.

## Deploy on GitHub Pages

Use this `academic-site` folder as the root of your GitHub repository: `.github/`, `scripts/`, and `dist/` must sit at the repository root.

1. Push the files to the repository's `main` branch.
2. In the repository, open **Settings → Pages → Build and deployment → Source**, and choose **GitHub Actions**.
3. Open **Actions → Deploy academic site to GitHub Pages → Run workflow**, selecting `main`. Later changes to site files on `main` deploy automatically.

The workflow packages the public files in `dist/` with no dependency installation, then publishes through GitHub's Pages actions. It derives the canonical URL and social preview image URL from GitHub's Pages configuration, including a repository subpath when needed. Existing relative links work at both project and user site addresses. Only the packaged static files are uploaded; source notes and legacy hosting metadata are excluded.

For the existing GitHub username `devhenode`, a repository called `henry-academics` produces `https://devhenode.github.io/henry-academics/`. For the shorter `https://devhenode.github.io/`, use a repository named `devhenode.github.io`. The workflow supports either choice without changing source URLs. These are expected URL patterns, not confirmation of a live deployment.

To check the package locally, run:

```sh
python3 scripts/prepare_pages.py --base-url https://devhenode.github.io/henry-academics
python3 -m http.server 4322 --bind 127.0.0.1 --directory _site
```

The `_site` output must be absent or empty before packaging. Regular local editing can keep using the `dist` preview described above.

Official setup references: [GitHub Pages publishing source](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [custom Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

## Optional Vercel compatibility

Push this folder to your own repository and import it in Vercel. The included `vercel.json` serves `dist` directly with no build or install step. If you push the containing `henry-academics` folder instead, its root configuration serves `academic-site/dist`.

Keep Framework Preset set to Other. No environment variables are needed. After choosing your final domain, make `og:image` in `dist/index.html` an absolute image URL on that domain for social sharing.

Do not publish or sync to ChatGPT Sites. The original private Sites deployment has not been unpublished because no unpublish capability was available; its identity is retained locally only for tracking that cleanup.

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

Hosting preference (November 21, 2026): GitHub Pages. The user handles the repository push and enabling Pages. Preparing the workflow does not publish the site; it deploys when the user runs it or pushes site changes to `main` after enabling Pages. Do not push or deploy from this session.

Browser-review updates: the user corrected LeAi reach to 10,000+ students, confirmed Python backend/algorithms and React/TypeScript frontend, and expanded ATC Africa leadership to six programs, managing leads across three Ogun State campuses, team check-ins, facilitation, and speaking. These user corrections supersede the older portfolio figures.
