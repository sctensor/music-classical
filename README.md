# Saugata Chatterjee Sitar — Static Site

Plain HTML/CSS, zero client-side JavaScript. `index.html` and `lineage.html`
are generated from `config.yaml` by a local Python script — the deployed
site is still pure static HTML/CSS with no runtime build step.

## Structure

- `index.html` — **generated**, home page (see Editing below)
- `lineage.html` — **generated**, standalone Musical Lineage page — independent from the homepage, not an anchor section on it
- `config.yaml` — images, social links, recordings, copy for both pages — the source of truth
- `templates/index.html.j2`, `templates/lineage.html.j2` — page layout/structure (Jinja2)
- `templates/_nav.html.j2`, `templates/_footer.html.j2` — shared nav/footer, included by both pages
- `scripts/build.py` — renders `config.yaml` + the templates into `index.html` and `lineage.html`
- `css/style.css` — all styles, brand tokens in `:root`
- `assets/images/` — see `assets/images/README.md` for status of each required file
- `robots.txt`, `sitemap.xml` (lists both pages), `favicon.svg`

## Run it locally

No build step, so any static file server works. From this folder:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000` in a browser. Stop with `Ctrl+C`.

(Opening `index.html` directly via `file://` also mostly works, but a local server matches production behavior more closely.)

## Editing

Content, images, and links live in `config.yaml`. After editing it, regenerate both pages:

```bash
pip install -r requirements.txt   # one-time
python3 scripts/build.py
```

- Hero/portrait images: `images.*` in `config.yaml` (point at the file path; drop the actual file in `assets/images/`).
- YouTube channel / Instagram / Facebook / Spotify: `social.*` — one value each, used everywhere that link appears (nav, hero, recordings, footer, lineage page).
- Recordings: `recordings:` list — add, remove, or reorder entries (title, meta, `youtube_url`, thumbnail). Each becomes a card linking straight to that video.
- Bio, homepage lineage teaser, hero copy: `about.bio`, `lineage.*`, `hero.*`.
- Full Musical Lineage page content (intro, the "Three Musical Lineages" diagram, sections I–III, closing): `lineage_page.*`. `lineage_page.streams` drives the three-column diagram — each entry is either a plain `chain` (Bengal), a `root` + branching `branches` (Etawah), or a `chain_before_split` + `branches` + `convergence` (Maihar); all three converge into `lineage_page.final_node`. This is family-supplied/historically documented material — don't reorder or alter it based on outside sources without checking with Saugata first.
- Colors/spacing/type: edit CSS variables at the top of `css/style.css` directly (not config-driven).

`index.html` and `lineage.html` are build output — edits made directly to them will be overwritten the next time `scripts/build.py` runs.

## Deploy (Cloudflare Pages)

1. Run `python3 scripts/build.py` locally first so `index.html`/`lineage.html` are up to date.
2. Push this folder to a git repo, or drag-and-drop it in the Cloudflare Pages dashboard.
3. Build command: none. Output directory: `/` (project root).
4. No environment variables or build settings required. `config.yaml`, `templates/`, and `scripts/` are harmless to ship alongside the static files but aren't used at runtime.

## Before going live

- Hero background (`hero.avif` / `hero.webp`) is in — the rest are still placeholders (see `assets/images/README.md`).
- Update `og:image`, `canonical`, and `sitemap.xml` URLs with the real domain.
- Swap placeholder social links (`facebook.com`, `spotify.com` in the footer/final CTA) for approved channels only.
