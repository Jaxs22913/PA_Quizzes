# Hosting PA Quizzes on Cloudflare

Written 2026-10-08. GitHub stays the source of truth for code; Cloudflare serves the
website; Firebase (project `pa-quizzes-addc1`) stays the backend for sign-in and
student data. Nothing in Firebase moves.

| | |
|---|---|
| Production address (once the domain is registered) | **https://pa-quizzes.com** (`www.` redirects to it) |
| Cloudflare preview address | https://pa-quizzes.jaxonluke22913.workers.dev |
| GitHub Pages (live for students until cutover, then the "moved" page) | https://jaxs22913.github.io/PA_Quizzes/ |
| Cloudflare account | `Jaxonluke22913@gmail.com's Account` (`bc3926e128ce1a9a9feb9aa2725dfd21`) |
| Cloudflare product | Workers Static Assets (a Worker with no script), named `pa-quizzes` |

## Why Cloudflare, and why Workers Static Assets rather than Pages

- Cloudflare's current guidance (agent-setup instructions and its `cloudflare` skill,
  2026-10-08) recommends **Workers Static Assets for new static sites**; Pages is now
  the option for maintaining existing Pages projects.
- More importantly, **Pages always redirects `/page.html` to `/page`** and cannot be
  told not to. PA Quizzes stores quiz progress (`qp:`/`qc:`, on 924 pages), missed
  questions (`qm:`), shuffles, guide highlights and drawings (`guideHl:`, `guideInk:`),
  and the Firestore `presence` / `sharedHighlights` documents under keys built from
  `location.pathname`. Dropping `.html`, or dropping the `/PA_Quizzes/` prefix, changes
  every key: a student who signs in on the new site would download their synced
  progress and the site would never find it. Fixing that in code means editing 924+
  pages, half of them in the frozen Semester 1.
- Workers Static Assets with `html_handling: "none"`, and the site published under
  `/PA_Quizzes/`, serves **exactly the same addresses as GitHub Pages**
  (`https://pa-quizzes.com/PA_Quizzes/<folder>/<page>.html`). Every key matches, so
  signed-in students' progress syncs between both hosts while both are up, and
  "studying now" presence sees students on either host. `pa-quizzes.com/` redirects to
  `/PA_Quizzes/`, so typing the bare domain lands on the homepage.
- There is no Worker script, so no code runs per request: static asset requests are free
  and unlimited, and there are no serverless costs.

## How a change reaches the site

```
edit -> commit -> push to GitHub main
   |-> GitHub Actions (.github/workflows/pages.yml) -> GitHub Pages   (unchanged)
   '-> Cloudflare Workers Builds -> node cloudflare/build.mjs -> wrangler deploy -> Cloudflare
```

Both hosts deploy from the same commit, so they never drift apart.

### What the build does

`cloudflare/build.mjs` (Node, no dependencies, about 2 s):
- copies every **git-tracked** file into `dist/PA_Quizzes/`, byte for byte;
- leaves out tooling no page links to: `tools/`, `.github/`, `cloudflare/`, `docs/`,
  `CLAUDE.md`, `firestore.rules`, `wrangler.jsonc`, `.gitignore`, `.nojekyll`;
- copies `cloudflare/_redirects`, `cloudflare/_headers` and `cloudflare/404.html` to the
  `dist/` root, where Cloudflare reads them;
- fails the build if any file is over 25 MiB or the total is over 20,000 files
  (Workers Free limits). On 2026-10-08: 3,763 files, 466.7 MiB.

`dist/` is git-ignored and never committed.

### Hosting rules (all in `cloudflare/`)

- `_redirects`: `/`, `/index.html` and `/PA_Quizzes` -> `/PA_Quizzes/` (301);
  `/PA_Quizzes/` is served from `/PA_Quizzes/index.html` (200 rewrite, because
  `html_handling: "none"` does not serve folder indexes on its own).
- `_headers`: HTML, JS, CSS and JSON keep Cloudflare's default
  `public, max-age=0, must-revalidate` (file names carry no content hash, and class
  content must never go stale); images cache for 1 hour and mp3 for 1 day;
  `sw.js` is `no-cache`; every `*.workers.dev` response carries `X-Robots-Tag: noindex`
  so search engines index only pa-quizzes.com.
- `404.html`: missing files return a real 404 page, never the homepage (so a missing
  JSON file fails loudly instead of parsing HTML).

## Cloudflare settings (the exact values)

Workers & Pages -> **Create** -> **Import a repository** (Workers, not Pages):

| Setting | Value |
|---|---|
| Git account / repository | `Jaxs22913/PA_Quizzes` |
| Project (Worker) name | `pa-quizzes` (must match `name` in `wrangler.jsonc`) |
| Production branch | `main` |
| Build command | `node cloudflare/build.mjs` |
| Deploy command | `npx wrangler@4.138.0 deploy` |
| Root directory | *(blank: the repository root)* |
| Build output directory | none to enter: `wrangler.jsonc` sets `assets.directory` to `./dist` |
| Builds for non-production branches | off |
| Environment variables | none (there are no secrets; the Firebase web config is public by design and lives in `firebase-config.js`) |

Wrangler is pinned (4.138.0, released 2026-09-24) so a new Wrangler release cannot
change a deploy unannounced. To upgrade, change the version in the deploy command and
check that `compatibility_date` in `wrangler.jsonc` is not newer than that Wrangler
supports (local `wrangler dev` refuses to start if it is).

Workers Builds free plan: 3,000 build minutes a month, one build at a time,
20-minute timeout. If the minutes ever run short, deploy from GitHub Actions instead
(free for public repositories): add a job running `cloudflare/build.mjs` then
`cloudflare/wrangler-action` with a `CLOUDFLARE_API_TOKEN` repository secret, and
disconnect the Git integration.

## Custom domain: pa-quizzes.com

The domain was **not registered** on 2026-10-08 (`whois`: "No match"). Register it in
the same Cloudflare account (Domain Registration -> Register Domains), with auto-renew on,
so its DNS lives there too. Then:

1. Worker `pa-quizzes` -> **Settings -> Domains & Routes -> Add -> Custom domain**:
   add `pa-quizzes.com`, then `www.pa-quizzes.com`. Cloudflare creates the DNS records
   and the TLS certificates.
2. Zone `pa-quizzes.com` -> **Rules -> Redirect Rules** -> create from the template
   "Redirect from WWW to root": request URL `https://www.*` -> target `https://${1}`,
   301, preserve query string.
3. Zone -> **SSL/TLS -> Edge Certificates**: turn **Always Use HTTPS** on (HTTP -> HTTPS).
   Leave **Rocket Loader** off: it rewrites inline scripts, and every quiz page keeps its
   questions in an inline script.
4. Firebase (below): add `pa-quizzes.com`.

## Firebase requirements

Firebase Console -> project **pa-quizzes-addc1** -> **Authentication -> Settings ->
Authorized domains -> Add domain**:

| Domain | When | Why |
|---|---|---|
| `pa-quizzes.jaxonluke22913.workers.dev` | now | Google sign-in on the preview |
| `pa-quizzes.com` | when the domain is attached | covers `www.pa-quizzes.com` too (an entry also allows its subdomains) |
| `jaxs22913.github.io`, `localhost`, `pa-quizzes-addc1.firebaseapp.com`, `pa-quizzes-addc1.web.app` | keep | GitHub Pages rollback, local development, the sign-in handler |

Never add a bare `workers.dev` or `pages.dev`: entries cover their subdomains, so that
would let every site on those hosts use this project's sign-in.

Verified 2026-10-08 (read-only): the web API key has **no** HTTP-referrer restriction,
App Check is **off**, and the Firestore rules do not depend on origin, so only the
authorized-domains list needs changing. If a referrer restriction is ever added
(Google Cloud Console -> APIs & Services -> Credentials -> Browser key -> Websites),
list `https://jaxs22913.github.io/*`, `https://pa-quizzes.com/*`,
`https://*.pa-quizzes.com/*`, `https://pa-quizzes.jaxonluke22913.workers.dev/*`,
`http://localhost:*/*` and `https://pa-quizzes-addc1.firebaseapp.com/*`.

Sign-in is `signInWithPopup` with the default `authDomain`
(`pa-quizzes-addc1.firebaseapp.com`), so no OAuth redirect URI changes are needed. Keep
the default authDomain: `firebase-config.js` is shared by every host.

**Sign-in does not carry across hosts.** Browser storage and the Firebase session are
per origin, so each student signs in once on the new address. Synced progress then
downloads under the same keys and appears where it should. Students who never sign in
keep their data only in that browser; the cutover hand-off page (below) moves it.

Other services checked: the Formspree (`xdaqleod`) and Forminit (`q1jz9v74p78`) report
forms answer CORS for any origin. If either dashboard has a domain restriction set,
add the new hosts there. Google Analytics (`G-2K06TXC2KK`) needs nothing.

## Cutover and rollback

Until cutover (planned to ship together with the Pip AI), **GitHub Pages remains the
site students use**, and Cloudflare is a parallel copy deployed from the same commits.
Nothing about the GitHub site changes.

Cutover, in order, only with Jaxon's explicit approval:
1. pa-quizzes.com attached, HTTPS working, Google sign-in tested there.
2. Students told the new address.
3. GitHub Pages switched to the "PA Quizzes has moved" page, which also offers to carry
   a student's saved data to pa-quizzes.com (see `.github/pages-moved/README.md`).

**Rollback** (if Cloudflare fails): students go back to
https://jaxs22913.github.io/PA_Quizzes/. If GitHub Pages had already been switched to
the moved page, revert that commit and push; the full site redeploys in about a minute
(the switch only changes which folder the GitHub Pages workflow uploads; no content is
deleted). Keep `jaxs22913.github.io` in Firebase's authorized domains for as long as
rollback is wanted.

## Turning Cloudflare off

- Pause deploys: Worker `pa-quizzes` -> Settings -> Build -> disconnect the repository
  (the current deployment keeps serving).
- Take the site down: Worker `pa-quizzes` -> Settings -> Domains & Routes -> disable
  `workers.dev` and remove the custom domains; or delete the Worker.
- GitHub Pages is unaffected either way.

## Local development

- Exactly as before: `python3 -m http.server` from the repo root, open
  http://localhost:8000/ (keys there have no `/PA_Quizzes/` prefix, as before).
- To run the Cloudflare copy locally: `node cloudflare/build.mjs && npx wrangler@4.138.0 dev`
  then open http://127.0.0.1:8787/ (it redirects to `/PA_Quizzes/`).

## Troubleshooting

| Symptom | Likely cause |
|---|---|
| A page 404s on Cloudflare but works on GitHub | the link omits `.html` (GitHub Pages also serves `page` for `page.html`; Cloudflare does not, on purpose) |
| Google sign-in shows "This domain is not authorized" | the host is missing from Firebase authorized domains |
| Old content after a push | the build is still running (Workers & Pages -> pa-quizzes -> Deployments), or the 1-hour image cache |
| Build fails "over 25 MiB" | a new file is too big for Cloudflare; compress it or host it elsewhere |
| `wrangler dev` says the compatibility date is too new | lower `compatibility_date` or raise the pinned Wrangler |

## Found during the audit, not fixed (outside this migration)

These are bugs on the current site, unchanged by the move:
- `medals.js:29/61` and `exam-countdown.js:40` build keys without `/PA_Quizzes/`, so
  medals never show and the calendar's "Next up" reads 0 quizzes done on GitHub Pages
  (both work on localhost).
- `progress.html:156-161` files every quiz under one row named "PA_Quizzes".
- GitHub Pages also serves extensionless addresses (`/PA_Quizzes/review`), and visits
  made that way write keys the homepage cannot find.
A path normaliser (`paqKeyPath`, specified in the 2026-10-08 audit) would fix all four.
