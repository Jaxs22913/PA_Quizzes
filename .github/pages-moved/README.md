# GitHub Pages "PA Quizzes has moved" page — NOT LIVE until cutover

`site/` is what https://jaxs22913.github.io/PA_Quizzes/ will serve **after** Jaxon
approves the cutover to https://pa-quizzes.com (timed by Jaxon).
Until then GitHub Pages keeps serving the full site and nothing in this folder is
deployed anywhere (`actions/upload-pages-artifact` skips `.github/`).

## What it does

- `site/index.html` and `site/404.html` are the same page. GitHub Pages serves
  `404.html` for every path that no longer exists, so every old address (bookmarks,
  class messages, a deep link to one quiz) shows the notice and points at **the same
  page** on pa-quizzes.com, whose addresses are identical
  (`/PA_Quizzes/<folder>/<page>.html`, query string and `#hash` kept).
- Shows "PA Quizzes has moved!", the new address as plain selectable text, a large
  **Go to PA Quizzes** button and a bookmark reminder. `noindex` + a canonical link to
  pa-quizzes.com, so search engines drop github.io.
- **Brings the student's saved progress along.** Browser storage is per address, so
  a student who never signed in would otherwise start empty. Pressing the button opens
  `https://pa-quizzes.com/PA_Quizzes/import.html` (from `cloudflare/import.html`),
  which merges the old address's `localStorage` (newer copy wins per key, using
  cloud-sync's own timestamps; Firebase session keys are skipped) and then this tab
  moves to the new address. Signed-in students' data also arrives through cloud sync
  after they sign in once at the new address.
- Automatic redirect after 10 s (with a "Stay here" link) **only when the student has
  nothing saved here or has already brought it over**; otherwise it waits for the
  button so nothing is left behind. A "Download a backup" link is the fallback; the
  import page accepts that file.
- Self-contained: no theme.js, so no Firebase and no cloud-sync on the old address.

Tested 2026-10-08 in headless Chrome across two real origins (22 checks: merge rules,
sync record, deep-link mapping, countdown, cancel, spoofed-message rejection).

## Cutover checklist (only with Jaxon's explicit go-ahead)

1. https://pa-quizzes.com works, HTTPS valid, Google sign-in tested there, progress
   reads and writes checked, smoke test passed.
2. In `cloudflare/_headers`, delete the `X-Robots-Tag: noindex` line under `/*` (keep
   the workers.dev rule) so pa-quizzes.com can be found by search engines.
3. Switch GitHub Pages to this page: in `.github/workflows/pages.yml` change
   `path: "."` to `path: ".github/pages-moved/site"`. Commit as
   "Cutover: GitHub Pages serves the moved page" and push. Within about a minute
   every github.io address shows the notice.
4. Tell the class the new address.
5. Keep `jaxs22913.github.io` in Firebase's authorized domains for as long as rollback
   should stay possible.

## Rollback

`git revert <the cutover commit>` and push. The GitHub Pages workflow uploads the whole
site again and https://jaxs22913.github.io/PA_Quizzes/ is the full site within about a
minute. Nothing is deleted at cutover, so nothing has to be restored. Students' data on
pa-quizzes.com stays there; signed-in students get it on github.io again by signing in.
