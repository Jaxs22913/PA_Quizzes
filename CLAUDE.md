# PA_Quizzes — orientation for a new session

**Written 2026-09-22, trimmed 2026-10-15.** Claude Code reads this automatically. It is the map, not the
territory: read what it points at rather than trusting the summary. Class-specific detail lives in memories.

## 1. What this is

A static study site Jaxon builds for his PA-school cohort (Class of 2028, Nova Southeastern, Jacksonville):
quizzes, study guides, cram sheets, an Arcade, group study, a practicum atlas, the study planner, and Pip,
the study companion. Everything is per class and per exam.

- **Real people use it for real exams.** A wrong key is not cosmetic; run the checkers (§6) on every build.
- **The repository is PUBLIC.** Anything committed is republished. Lecture audio, transcripts and raw decks
  stay OUT of the repo (they live in `~/Desktop/PA Quizzes/`, §4); verify image licences from the asset's page.

## 2. Read first: the memory index

Knowledge lives in `~/.claude/projects/-Users-jaxonluke/memory/`; `MEMORY.md` there is the index and loads
automatically. **Open the specific memory before acting in an area**; the index line is only a pointer.
Before content work: `quiz_build_prompt.md`, `exam_standard.md`, `guide_design_system.md`,
`reference_question_style.md`, `pa_quizzes_hosting.md`, `site_bug_sweep_tools.md`. Each class has its own spec
memory (`cms_exam_spec.md`, `pharmacology_exam_spec.md`, ...), which **overrides the general one on conflict**.
Memories are point-in-time: verify a named file, function or flag still exists before relying on it.
Session state (in-progress work, decisions, exam dates) is in the newest folder under
`~/Developer/PA_Quizzes-handoff/` and the START HERE / PENDING entries at the top of the index.

## 3. How the site runs

- Clone: `~/Developer/PA_Quizzes`, branch `main` (moved out of `~/Documents` in July 2026 because iCloud
  spawned conflict copies; do not move it back).
- Live: `https://pa-quizzes.com/PA_Quizzes/` (Cloudflare Workers Static Assets, `cloudflare/build.mjs`,
  `docs/HOSTING_CLOUDFLARE.md`). Every `jaxs22913.github.io/PA_Quizzes/` address shows only the "moved" page
  (`.github/pages-moved/`), which hands saved progress to pa-quizzes.com.
- Each push to `main` runs `cloudflare.yml` and `pages.yml` (about a minute). **A push is not a deploy**: during
  a GitHub outage pushes created no workflow run. After pushing, `curl` the changed file on pa-quizzes.com and
  grep for a string only the new version has.

### Pip
`pip/*.js` (sprites `immutable/pip/v1/`), loaded by the end of `theme.js` on pa-quizzes.com only (every
theme.js page, plus five self-contained Semester 2 pages with their own loader; never the 11 frozen
self-contained Semester 1 files). Behaviour rules: memory `pip_behavior_rule.md`; current work:
`pip_overhaul_next.md`. In short: paused on an open quiz question; for a student who can use Claude, every real
question gets a short answer Claude writes after reading the WHOLE study guide of the exam it is about (helper
mode "guide", Haiku 5.5; the helper fetches the public pip/data/guide/<slug>.json, numbers its lines, caches it
for an hour; "Used: [n]" names the lines, sent back as cites that Pip links; the search's picks go along as
candidates and hints; the usual answer is the fallback, mode "answer" when guide mode isn't there). Follow-ups: the
last 2 Claude exchanges stay in memory only (dropped after 15 min idle or a page change) and go as `prior` when a
question refers back (`followUp()`: it keeps the earlier exam and searches with the earlier question's words too).
Guide answers stream into the bubble, and with the Citations API each cite carries `q`, the exact guide sentence,
shown under the answer and passed to `openGuidePanel({..., quote})`. Answers come in two
labelled parts, "From your
class" (his checked cards in `pip/explain/<exam>.json`, guide passages from every exam that holds the
question's words, misspellings fixed, definitions, "the X of each Y" lists, compare dissections) and "From
general knowledge" (Claude, labelled, only when the class materials fall short); guide links open
`window.openGuidePanel`. Generated data `pip/data/` is never committed: the deploy runs
`tools/build_pip_data.py`, which fails loudly on a page it cannot parse (fix the page, never skip it).
After a guide edit, cards whose section changed show as stale (`python3 tools/pip_explain.py check`, then
`rehash` once re-checked). Checks: `node tools/check_pip_answers.js` (answer kinds, guide exam, follow-ups; no browser),
`node tools/pip_explain_match.js` (card matching), `tools/check_pip_launch.py` (built `dist/`). Never run real
models in tests or send question sets through any model (memory `no_bulk_model_runs.md`). The Claude helper is
a private Worker; its source is not in this repo.

## 4. Where the inputs live (not in the repo)

```
~/Desktop/PA Quizzes/Semester 2/<Class> Inbox/{Syllabus/, Exam N/ (.pptx), Exam N/recordings/}
~/Desktop/PA Quizzes/Calendars/<Semester>/<Month>.pdf
```
`PA Quizzes` has a space; quote it. A new class auto-gets an Inbox (`class_inbox_convention`).
`calendar-data.js` is generated from the calendar PDFs by `tools/gen_calendar_data.py` (never hand-edit); its
lecturer names have been wrong several times, so attribute a lecture from the deck and the recording
(`academic_calendar_pipeline`). Recordings come out of Notability (`notability_audio_pipeline`); transcribe with
`tools/pull_lecture_segments.py`, `tools/lecture_transcript.py` or `tools/transcribe_long.py`, and keep the
second opinion next to ours (`<stem>.notability.txt`, or `<stem>.youtube-captions.txt` for Pharm).

## 5. Building things

**Know which layer you edit:** `question pool -> partition script -> sets.json -> tools/quiz-template/render.py
-> shipped HTML`. Editing a pool changes nothing until you re-render (46 pages once kept old text this way).
Partition scripts are seeded. One-off quizzes skip partitioning (example: `tools/micro_e1_hours_pool.py` +
`tools/render_micro_e1_hours.py`). The `/new-exam-build` skill is the compact runbook.

Quizzes:
1. Read `quiz_build_prompt.md`, the class spec memory (it decides question TYPES and counts) and
   `tools/question_writing/WRITER.md` (how each item is written and checked).
2. Ground every question in the deck (`python-pptx`, `=== SLIDE N ===` markers, cite exact filename + slide).
3. Use the mandatory engine `tools/quiz-template/render.py` (`quiz_engine_standardization`).
4. Register in `index.html` under the right class/exam with a self-expiring New tag (`new_exam_tag`).
5. After any render, BEFORE committing: `python3 tools/add_stable_qids.py`, `tools/build_group_quizzes.py`
   (never hand-edit the Group Study bank), and for Semester 2 `tools/build_guide_links.py "<folder>"` then
   `tools/check_guide_links.py --strict` (links are keyed to the exact question text).
6. **Blind review** every new or changed question before it ships (`tools/blind_review.py`, Sonnet judges per
   `tools/question_writing/REVIEW_BLIND.md` then `REVIEW_AUDIT.md`; judges never see the key or a manifest before
   their blind verdicts are imported). One Opus repair per flagged item, re-review with `export --ids`, else
   drop and replace. A blind pick that differs from the key is a possible wrong key.
7. Run the checkers (§6), then commit and push: for quiz builds pushing is part of the spec.

Guides: `guide_design_system` + `guide_verbatim_io_rule` (the objectives box quotes the syllabus verbatim and
answers each objective in order). Cram sheets: `tools/cram-sheet-template/` (`cram_sheets_feature`). Arcade:
`arcade_content_policy`, `arcade_integration`. Study planner (`calendar.html`, `planner-engine.js`,
`planner-ui.js`): memory `study_planner.md`; `node tools/test_planner.js` must pass after any engine change.
Med Lit Book Questions: memory `medlit_book_questions.md`. RPG mode was scrapped; do not resume it.

## 6. The checkers: run them, do not trust memory

```bash
python3 tools/check_all.py "<Class Exam N>" [--fast]   # keys, exam standard, self-contained, lead-ins, length
                                                      # bias, pool cites, US spelling, accordions, guide links
```
plus a load-only look with `~/Developer/pa-tools/bin/pa-shot <page> [--dark] [--mobile]` and
`bin/pa-sweep <pages>` (contrast + 390 px overflow). **Never run `check_console_errors.py`,
`check_answer_distribution.py` or `check_dark_contrast.py`**: they open live pages with Firebase unblocked.
`pool cites`, `accordions closed` and `guide links --strict` are site-wide, so a failure may be another exam's.
Others worth knowing: `check_ppt_grounding`, `check_truncated_keys`, `check_slot_coverage`,
`check_master_pairing`, `check_index_sections`; use `check_length_bias_fast.py`, not the slow headless one.
Run `check_pool_cites` BEFORE any render (a stale sets file puts citations back). Always read the denominator.

## 7. Content rules that are always on

Each has a memory with the full story.
- **Four options**, site-wide. **Every stem asks exactly ONE thing** and is **self-contained** (never cite the
  lecture, deck, professor or syllabus; never build on a lecture's worked example).
- **Every option gets its own explanation** that refutes AND supplies the replacing fact (60+ characters).
- **Distractors match the key's length and style**; shorten the key, never pad distractors.
- **Permute answer positions** before shipping. **No abbreviations**, or `ABBREV (full term)`.
- **Slides-only grounding**: a lecturer's aside does not add content the deck lacks, and speaker notes do not count. **Truth wins on conflict**.
- **Every Semester 2 question links to a passage in its own class's guide that STATES the fact, and a
  separate reader verified it** (word overlap is not enough). For a new or changed question:
  1. write a missing fact into the guide via `tools/guide_additions/` + `tools/apply_guide_additions.py` (text only
     from the question's vetted explanation; `tools/verify_guide_additions.py`);
  2. `python3 tools/build_guide_links.py`;
  3. `python3 tools/audit_guide_links.py authored`, then `export --set new --out DIR`, judges read the batches
     under `tools/audit_guide_links_JUDGE.md` (each PASS needs a machine-checked verbatim quote), `import DIR`;
  4. PARTIAL/FAIL: write the fact into the guide and repeat;
  5. `python3 tools/check_guide_links.py --strict` must pass.
  A judge finding that the guide CONTRADICTS the key is a possible wrong key: check the slides and the truth first.
- **Semester 1 exams are frozen.** **US spelling** in Semester 2+ (keep taxonomic names such as *Haemophilus*).

## 8. How to work here

- **Verify empirically**: when you report a number, have run the thing that produced it.
- **Match the existing pattern** before inventing one; nearly everything has a precedent in `tools/`.
- **Flag rather than silently resolve** contradictions (say so in the output and the commit message).
- **Diff after every rule change** in bulk rewrites.
- **Saving tokens (Jaxon, 2026-10-15)**: one owner per change; an independent review only for risky changes
  (theme.js runs on every page; exam days); quick checks then push; scripts report exit status + failing tail.
  Never hotfix a file another running agent is editing: `git log -3` + `git status` right before every commit.
- Standing push permission since 2026-07-16, but say what you pushed.
