# Anonymous usage counts

Added 2026-10-10 so the site can show, truthfully, how much the class uses it ("N questions answered,
M students") for a future proposal, without recording anything about anyone.

## What is stored

One Firestore document per day, `metrics_daily/{YYYY-MM-DD}`, holding only integers:

| Field | Counts |
|---|---|
| `q_answered` | questions answered (the same number the homepage class counter adds) |
| `quiz_done` | quizzes finished |
| `guide_open`, `cram_open`, `ref_open` | study guides, cram sheets and other reference pages opened (once per tab per page) |
| `arcade_session` | an Arcade game page opened with a deck (once per tab) |
| `review_drill` | missed-question drills started (review.html) |
| `planner_day` | a student using the study planner on that day |
| `active_d`, `active_w`, `active_m` | distinct students active that day, ISO week and month |

Never stored, in these documents or anywhere else for this feature: question text, answers, typed
text, names, emails, account ids, IP addresses, device ids, page addresses, or the time of any single
event. The finest grain is a day.

**Distinct students without storing who.** Each device adds 1 to `active_w` the first time it is used
in an ISO week (and likewise per day and month), remembered by the synced key `metrics:seen` (the
newest day, week and month already counted). A signed-in student's devices share that key through
cloud sync, so they count once; a student who never signs in and uses two devices counts twice. The
weekly number is the sum of `active_w` over that week's seven day documents.

## How it is sent (the Firestore budget)

Counts go into a device-only buffer (`local:metrics:buf`, never uploaded by cloud sync) and are sent
as one batched `increment()` write per day document: at most once every 10 minutes while a page is
open, or when the student leaves the tab (at most once every 2 minutes). Nothing is ever read back.
Measured with the fake-Firestore rig: a 31-minute, 8-page signed-out session made **4 metrics writes
and 0 metrics reads** (plus the class counter's existing 1 write, 1 log row and 2 homepage reads).
A signed-in student also uploads `metrics:seen` at most once a day. A device that never signed in
with Google gets one silent anonymous Firebase session (as Group Study does), once.

A failed write (rules not yet published, offline) puts the counts back and retries later, backing off,
so nothing is lost while the rules wait. Writes start only on a live page, never during unload.

## Who is never counted

Checked before a count is buffered and again before it is sent:

- a student who turned it off: the note's **Turn off** button or Settings, "Count my use in anonymous
  totals" (synced `metrics:off`, so that device and that account). It also stops the class counter,
  its `stats_events` row and the class picks for them: off means all counting;
- a developer device or account: visit any page with `?metrics=dev` (`?metrics=on` clears it). The
  flag is the synced key `metrics:dev`, so it follows the account to every device it signs in on;
- automated browsers (`navigator.webdriver`), `localhost` previews and `file://` pages.

## The notice

Shown once (bottom left, not on quiz pages), and kept permanently under the Settings switch:

> PA Quizzes counts anonymous totals, like how many questions are answered and how often each study
> tool is used, to improve the site and to support a future free version for students everywhere.
> No names or answers are recorded. [Got it] [Turn off]

The wording lives once, in theme.js (`PAMetrics.note`).

## Rules

`firestore.rules`, `match /metrics_daily/{day}`: a write must come from a signed-in Firebase session,
touch only the listed fields, raise each by a small positive amount (`q_answered` up to 1000 per write,
the distinct counters by exactly 1), and target a day between 36 days back and 1 day ahead. No client
may read or delete. Nothing auto-deploys: paste the WHOLE file into the Firebase console
(Firestore Database, Rules, Publish). Until then writes are refused and the counts wait on each device.

## Running the report

`python3 tools/usage_report.py` prints a Markdown summary: totals since launch, active students by
month and by week, and the daily average. Any number derived from fewer than 10 distinct students
reads "fewer than 10". It only reads.

It needs a read-only key, once:

1. Google Cloud console, project **pa-quizzes-addc1**: IAM & Admin, Service Accounts, Create service
   account (name it `usage-reader`), role **Cloud Datastore Viewer**, Done.
2. Open it, Keys, Add key, Create new key, JSON. Save the download as
   `~/.config/pa-quizzes/usage-reader.json` and run `chmod 600` on it. Never commit it or paste it anywhere.

`--weeks 16` shows more weeks, `--since YYYY-MM-DD` drops earlier days, `--from-json FILE` reads an
exported copy (`tools/metrics-test/report_fixture.json` is a synthetic one for testing).

## Tests

- `tools/metrics-test/test_metrics.py` (pa-tools venv + Playwright): a fake Firestore with real merge
  and increment semantics, real Firebase blocked. Sessions, opt-out, developer flag, a signed-in
  second device, rules not yet published, automated browsers, the note. 37 checks.
  `~/Developer/pa-tools/venv/bin/python tools/metrics-test/test_metrics.py http://127.0.0.1:8791/`
  with the repo served on 8791.
- `tools/metrics-test/rules.test.mjs`: the rules against the Firestore emulator (needs Java and
  `npm i firebase-tools@13.35.1 @firebase/rules-unit-testing@4.0.1 firebase@11.10.0` in a scratch
  folder holding a `firebase.json` that points at a copy of the rules; then
  `npx firebase emulators:exec --only firestore --project demo-pa "node rules.test.mjs firestore.rules"`).
- `tools/metrics-test/sweep.py`: a load-only console sweep of every top-level page and a sample of each
  exam folder with the fake Firestore.
