# CMS I Exam 7 (Respiratory Block Exam II, Lectures 39-45): how to add a lecture

Exam 7 (Monday 2026-11-16) is built a lecture or two at a time. Every exam-level page is ASSEMBLED from
per-lecture pieces, so adding a lecture means dropping files in, never hand-editing a built page.
Folder: `Clinical Medicine and Surgery I Exam 7/`. Palette: bronze (navy `#5e4123`, indigo `#92693f`, gold
`#c08a2e`, ice `#faf6ee`), set in `tools/render_cms_e7.py` and `tools/cms_e7_guide/_head.html`.

Lectures so far (branch `feat/cms-e7-l39-41`): 39 Phases of Sleep and 40 Obstructive Sleep Apnea and Obesity
Hypoventilation Syndrome (Shah), 41 Inflammatory Lung Diseases (Gray, guest lecturer, narrated deck).
Still to come: 42-45. Masters are HELD until Lecture 45 is in (memory `master_exam_sizing`).

## Weighting (5 questions per scheduled lecture hour, calendar-data.js)

| Lecture | Topic | Hours | Master questions per 60 (when built) |
|---|---|---|---|
| 39 | Phases of Sleep (Shah) | 1 | 5 per hour, share of the block's total hours |
| 40 | Obstructive Sleep Apnea and Obesity Hypoventilation (Shah) | 1 | |
| 41 | Inflammatory Lung Diseases (Gray) | 2 | |
| 42-45 | add each lecture's hours from calendar-data.js | | |

The masters (5 forms x 60, memory `master_exam_sizing`) are sized by hours once all seven lectures are in.
Within a lecture, emphasis is weighted by MINUTES spoken (`TOPIC_MINUTES` in the scope file, read by the
partition), never by word count; time spoken never adds off-deck content.

## 1. Quizzes (per lecture, your own prefix)

Per lecture `NN`: `tools/cms_e7lNN_scope.py` (verbatim syllabus IOs, EXCLUDED_SLIDES, SCOPE_BANNED, NAMED,
optional REQUIRED and TOPIC_MINUTES; the docstring records the recording's emphasis and every slide conflict),
pools `tools/cms_e7lNN_pool_*.py` and `tools/cms_e7lNN_vig_*.py`, then

```bash
python3 tools/cms_e7_partition.py lNNio      # and lNNvig  -> tools/cms_e7lNN_sets.json / _vig_sets.json
python3 tools/render_cms_e7.py lNNio         # and lNNvig  -> the four HTML pages
```

`cms_e7_partition.py` already has GUARDED keys `l39`-`l45` (io and vig). Lecture-specific lead-ins live in its
`LEADS` extras (l45 acid-base: etiology, compensation, classify, with DX_CAP 12). Add the lecture's four pages
to `render_cms_e7.py` SPEC. Explanations follow `tools/question_writing/EXPLAIN_DEEP.md`.

## 2. Study guide: one fragment per lecture

Write `tools/cms_e7_guide/lNN.html`: ONE `<section class="deck" id="<slug>">` that opens with
`<h2 class="deck-title">K &middot; Title</h2>`, where K = NN - 38 (L42 is 4, L45 is 7; the builder asserts it).
Copy `l40.html` for the markup: `p.lecturer`, `div.io-box` (syllabus objectives verbatim), the emphasis
`div.callout`, the `div.callout.warn` "Where the slides are loose or disagree", `h3.sub` subsections with ids
starting `lNN-`, starred `div.prof-flag` / `mark.prof-highlight`, a `div.cond` eight-point block per disease.
Then `python3 tools/build_cms_e7_guide.py` (writes `cms-exam-7-study-guide.html`).

## 3. Cram sheet

Write `tools/cms_e7_cram/lNN.py` defining `CRITERIA` (one table per criteria set, score, cut-off or staging on
the slides, each with a labeled memory aid; memory `cram_criteria_tables`) and `TOPICS` (a gold `#b8860b`
"★ Emphasized" card first). Add the lecture's short name to `NAMES` in `tools/build_cms_e7_cram.py`, then
`python3 tools/build_cms_e7_cram.py`. A Sonnet checker compares every table cell with the slides.

## 4. Clin Med Pro

Append a lecture object to `tools/clinmedpro/cms-e7.json` (`lectures`, in lecture order): `lecture`, `title`,
`lecturer`, `deck`, `note`, `conditions` (each `id` "lNN-...", `name`, `prof`, `prof_note`, the ten `fields`,
and `slides`, a per-field map of slide numbers). Uncovered fields are exactly "Not covered in the lecture";
`[[★ phrase]]` marks emphasis. Lecture 39 has no disease and so no conditions. `python3 tools/build_cms_clinmedpro.py 7`.

## 5. Arcade

Write `tools/cms_e7_arcade/lNN.json` (decks `{"id": "cms-e7-lNN-<topic>", "name", "color", "icon", "cards"}`,
atomic facts only, memory `arcade_content_policy`). `python3 tools/add_cms_e7_arcade.py` rewrites the fenced
CMSE7-DECKS block in `arcade.js` and the CMS group's "Exam 7" entry (test first with `ARCADE_JS=<scratch copy>`).

## 6. Pip cards

`python3 tools/build_pip_data.py`, then `python3 tools/pip_explain.py units clinical-medicine-and-surgery-i-exam-7
--out DIR`; a writer drafts cards for the NEW units, an independent Sonnet checker verifies every sentence, then
`assemble` into `pip/explain/clinical-medicine-and-surgery-i-exam-7.json` and `check` (0 errors, 0 stale).

## 7. Registration (shared files: add your lines, keep the others')

- `index.html`: inside `<details class="exam-section" data-examid="cms1-exam7">`, the lecture's four quiz links
  with `<span class="quiz-tag quiz-tag--new" data-added="YYYY-MM-DD">New</span>`; a "Master Exams" divider when
  the masters ship.
- `guides.html`: the `data-class="cms-1" data-exam="7"` subgroup holds the three Exam 7 cards; update their
  descriptions to name the new lecture.
- `tools/question_writing/scope.json` already globs `Clinical Medicine and Surgery I Exam 7/*-quiz*.html` and
  `*-vignettes*.html`.

## 8. Before committing

```bash
python3 tools/add_stable_qids.py "Clinical Medicine and Surgery I Exam 7"
python3 tools/build_quiz_index.py; python3 tools/build_group_quizzes.py; python3 tools/build_cram_personal.py
python3 tools/build_planner_resources.py; python3 tools/build_exam_spines.py
python3 tools/build_guide_docx.py "Clinical Medicine and Surgery I Exam 7/cms-exam-7-study-guide.html"   # and the cram + Clin Med Pro, count 1 each
```

Review: blind export -> Sonnet judges (REVIEW_BLIND.md) -> import -> audit export `--from` -> judges
(REVIEW_AUDIT.md) -> import -> one Opus repair per flag -> re-review `--ids`. Guide links:
`tools/guide_additions/clinical-medicine-and-surgery-i-exam-7.json`, `apply_guide_additions.py` +
`verify_guide_additions.py`; re-run `apply_guide_additions.py` and `check_guide_additions_inline.py` after EVERY
`build_cms_e7_guide.py`. Then `build_guide_links.py`, `audit_guide_links.py`, `check_guide_links.py --strict`,
and `python3 tools/check_all.py "Clinical Medicine and Surgery I Exam 7"`: 0 hard failures.

Never run `check_console_errors.py`, `check_answer_distribution.py` or `check_dark_contrast.py`.
