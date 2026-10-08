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
   |-> GitHub Actions .github/workflows/pages.yml      -> GitHub Pages  (unchanged)
   '-> GitHub Actions .github/workflows/cloudflare.yml -> node cloudflare/build.mjs
                                                      -> wrangler deploy -> Cloudflare
```

Both hosts deploy from the same commit, so they never drift apart, and a failed
Cloudflare deploy never touches GitHub Pages (separate workflow). Deploys run in
GitHub Actions rather than Cloudflare's own Workers Builds because Actions minutes are
free and unlimited for a public repository, while Workers Builds' free plan is 3,000
build minutes a month and would re-clone this 1.1 GB repository on every push.

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

| Setting | Value |
|---|---|
| Worker name | `pa-quizzes` (`name` in `wrangler.jsonc`) |
| Account ID | `bc3926e128ce1a9a9feb9aa2725dfd21` (`account_id` in `wrangler.jsonc`) |
| Production branch | `main` (the workflow runs on every push to it) |
| Build command | `node cloudflare/build.mjs` |
| Deploy command | `npx -y wrangler@4.138.0 deploy` |
| Root directory | the repository root |
| Build output directory | `dist` (set as `assets.directory` in `wrangler.jsonc`) |
| Custom domains | `pa-quizzes.com`, `www.pa-quizzes.com` (`routes` in `wrangler.jsonc`; every deploy keeps exactly these attached) |
| Environment variables | none. The only secret is the deploy token below. The Firebase web config is public by design and lives in `firebase-config.js`. |

**The one secret: `CLOUDFLARE_API_TOKEN`** (GitHub repository secret, used only by
`.github/workflows/cloudflare.yml`). To create or replace it:
1. Cloudflare dashboard -> profile icon -> **My Profile -> API Tokens -> Create Token** ->
   template **Edit Cloudflare Workers** -> **Use template**.
2. Account Resources: *Include* -> `Jaxonluke22913@gmail.com's Account`.
   Zone Resources: *Include* -> *Specific zone* -> `pa-quizzes.com`.
3. **Continue to summary -> Create Token**, and copy it (it is shown once).
4. GitHub -> `Jaxs22913/PA_Quizzes` -> **Settings -> Secrets and variables -> Actions ->
   New repository secret**: name `CLOUDFLARE_API_TOKEN`, paste the value.
Until the secret exists the workflow skips the deploy with a notice instead of failing.
Never paste the token anywhere else; never commit it.

Wrangler is pinned (4.138.0, released 2026-09-24) so a new Wrangler release cannot
change a deploy unannounced. To upgrade, change the version in the workflow and check
that `compatibility_date` in `wrangler.jsonc` is not newer than that Wrangler supports
(local `wrangler dev` refuses to start if it is).

Zone settings applied to `pa-quizzes.com` on 2026-10-08 (so the copy behaves like
GitHub Pages): **Always Use HTTPS on**; **Browser Cache TTL "Respect Existing
Headers"** (the zone default of 4 hours would have overridden the revalidate-always
headers on HTML/JS); **Email Address Obfuscation off** (it rewrites pages that contain
an email address and injects a script); Rocket Loader off (it rewrites inline scripts;
every quiz keeps its questions inline); one Redirect Rule, `www.pa-quizzes.com` ->
`https://pa-quizzes.com` + path, 301, query string kept.

## Custom domain: pa-quizzes.com

The domain was **not registered** on 2026-10-08 (`whois`: "No match"). Register it in
the same Cloudflare account (Domain Registration -> Register Domains), with auto-renew on,
so its DNS lives there too. Then:

Registered 2026-10-08 in this Cloudflare account (auto-renew on, transfer lock on,
WHOIS privacy on, expires 2027-10-08). The custom domains come from `routes` in
`wrangler.jsonc`: the first deploy creates their DNS records and TLS certificates.
The zone settings and the www redirect are listed above. Firebase needs
`pa-quizzes.com` in its authorized domains (below).

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

- Pause deploys: GitHub -> Actions -> "Deploy to Cloudflare (pa-quizzes.com)" ->
  **Disable workflow** (the current deployment keeps serving), or delete the
  `CLOUDFLARE_API_TOKEN` secret (the workflow then skips).
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
| Old content after a push | the deploy is still running (GitHub -> Actions -> "Deploy to Cloudflare"), or the 1-hour image cache |
| The Cloudflare workflow says "skipping" | the `CLOUDFLARE_API_TOKEN` secret is missing |
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

## Verification log (2026-10-08)

| Check | Result |
|---|---|
| First deploy (GitHub Actions run 37736686708) | 3,749 files uploaded in 51 s; Worker `pa-quizzes` live on `pa-quizzes.jaxonluke22913.workers.dev`, `pa-quizzes.com`, `www.pa-quizzes.com` |
| DNS | `pa-quizzes.com` -> 104.21.54.113 / 172.67.138.117 at Cloudflare's nameservers, 1.1.1.1 and 8.8.8.8 |
| HTTPS | Let's Encrypt (YE2) certificate for `pa-quizzes.com` + `*.pa-quizzes.com`, valid to 2027-01-06, auto-renewed by Cloudflare; TLS 1.3, HTTP/2 |
| Redirects | `http://` -> `https://`; `/` -> `/PA_Quizzes/`; `www.` -> apex with path and query kept (301) |
| Every file | all 3,760 site files return 200 on `https://pa-quizzes.com` and are **byte-identical** to the repo build |
| Headers | HTML/JS/JSON `max-age=0, must-revalidate`; png 1 h; mp3 1 d; `sw.js` `no-cache`; `Access-Control-Allow-Origin: *`; `noindex` (until cutover) |
| Missing files | real 404 page; extensionless links retried once with `.html` |
| Browser smoke test (Firebase, analytics and forms blocked) | 18 pages x Chromium (Chrome/Edge engine), WebKit (Safari engine) desktop + phone, Firefox desktop = 90 loads per host: **0 problems on Cloudflare that GitHub Pages does not also have, and 0 errors on either** |
| Quiz flow (Chromium, WebKit) | start, answer, feedback, next, progress saved, resume offered: pass on both hosts; saved-progress key identical on both (`qp:/PA_Quizzes/<folder>/<page>.html`) |
| Firebase authorized domains | `pa-quizzes.com` and `pa-quizzes.jaxonluke22913.workers.dev` added; `jaxs22913.github.io` kept |
| Google sign-in on https://pa-quizzes.com | works (tested by Jaxon: sign-in, synced progress appears, session persists, sign-out) |
| Cutover hand-off (held) | 22/22 checks pass across two real origins in headless Chrome |

Not verified: real Safari/Edge apps (their engines were tested), an iPhone home-screen
install, and real-student data over several days.
