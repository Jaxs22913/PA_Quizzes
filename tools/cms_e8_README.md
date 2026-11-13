# CMS I Exam 8 (Hematology Block Exam, Lectures 46-51): how to add a lecture

Exam 8 (Monday 2026-11-30, 10 AM) is built a lecture or two at a time. Every exam-level page is ASSEMBLED from
per-lecture pieces, so adding a lecture means dropping files in, never hand-editing a built page.
Folder: `Clinical Medicine and Surgery I Exam 8/`. Palette: olive and garnet (quiz navy `#46491c`, indigo `#717533`,
gold `#c9962a`, ice `#f8f8ee`; guide accent2 garnet `#a33a3f`), set in `tools/render_cms_e8.py` and
`tools/cms_e8_guide/_head.html`. Scaffolded 2026-11-12 as a copy of the Exam 8 machinery.

Lectures: 46 Cytopenias and Hemochromatosis (Ward, 3 hours, branch `feat/cms-e8-l46`). **Lecture 47 (AHEC smoking
cessation) is "not tested"**: it has no keys, no guide section and no pages (the builders skip 47; guide section
numbers run 46 = 1, 48 = 2, 49 = 3, 50 = 4, 51 = 5). Still to come: 48-51. Masters are HELD until Lecture 51 is in
(memory `master_exam_sizing`).

## Weighting (5 questions per scheduled lecture hour, calendar-data.js)

| Lecture | Topic | Hours |
|---|---|---|
| 46 | Cytopenias and Hemochromatosis (Ward) | 3 |
| 48-51 | add each lecture's hours from calendar-data.js | |

Within a lecture, emphasis is weighted by MINUTES spoken (`TOPIC_MINUTES` in the scope file, read by the
partition), never by word count; time spoken never adds off-deck content.

## 1. Quizzes (per lecture, your own prefix)

Per lecture `NN`: `tools/cms_e8lNN_scope.py` (verbatim syllabus IOs, EXCLUDED_SLIDES, SCOPE_BANNED, NAMED,
optional REQUIRED and TOPIC_MINUTES; the docstring records the recording's emphasis and every slide conflict),
pools `tools/cms_e8lNN_pool_*.py` and `tools/cms_e8lNN_vig_*.py`, then

```bash
python3 tools/cms_e8_partition.py lNNio      # and lNNvig  -> tools/cms_e8lNN_sets.json / _vig_sets.json
python3 tools/render_cms_e8.py lNNio         # and lNNvig  -> the four HTML pages
```

`cms_e8_partition.py` already has GUARDED keys `l46`, `l48`-`l51` (io and vig). Lecture-specific lead-ins live in its
`LEADS` extras (every Exam 8 lecture adds "classify": score, cut-off or class from the vignette). Add the lecture's four pages
to `render_cms_e8.py` SPEC. Explanations follow `tools/question_writing/EXPLAIN_DEEP.md`.

## 2. Study guide: one fragment per lecture

Write `tools/cms_e8_guide/lNN.html`: ONE `<section class="deck" id="<slug>">` that opens with
`<h2 class="deck-title">K &middot; Title</h2>`, where K = 1 for L46 and NN - 46 from L48 on (L48 is 2, L51 is 5; the builder asserts it).
Copy `l46.html` (or Exam 7's `tools/cms_e7_guide/l40.html`) for the markup: `p.lecturer`, `div.io-box` (syllabus objectives verbatim), the emphasis
`div.callout`, the `div.callout.warn` "Where the slides are loose or disagree", `h3.sub` subsections with ids
starting `lNN-`, starred `div.prof-flag` / `mark.prof-highlight`, a `div.cond` eight-point block per disease.
Then `python3 tools/build_cms_e8_guide.py` (writes `cms-exam-8-study-guide.html`).

## 3. Cram sheet

Write `tools/cms_e8_cram/lNN.py` defining `CRITERIA` (one table per criteria set, score, cut-off or staging on
the slides, each with a labeled memory aid; memory `cram_criteria_tables`) and `TOPICS` (a gold `#b8860b`
"★ Emphasized" card first). Add the lecture's short name to `NAMES` in `tools/build_cms_e8_cram.py`, then
`python3 tools/build_cms_e8_cram.py`. A Sonnet checker compares every table cell with the slides.

## 4. Clin Med Pro

Append a lecture object to `tools/clinmedpro/cms-e8.json` (`lectures`, in lecture order): `lecture`, `title`,
`lecturer`, `deck`, `note`, `conditions` (each `id` "lNN-...", `name`, `prof`, `prof_note`, the ten `fields`,
and `slides`, a per-field map of slide numbers). Uncovered fields are exactly "Not covered in the lecture";
`[[★ phrase]]` marks emphasis. `python3 tools/build_cms_clinmedpro.py 7`.

## 5. Arcade

Write `tools/cms_e8_arcade/lNN.json` (decks `{"id": "cms-e8-lNN-<topic>", "name", "color", "icon", "cards"}`,
atomic facts only, memory `arcade_content_policy`). `python3 tools/add_cms_e8_arcade.py` rewrites the fenced
CMSE8-DECKS block in `arcade.js` and the CMS group's "Exam 8" entry (after Exam 7) (test first with `ARCADE_JS=<scratch copy>`).

## 6. Pip cards

`python3 tools/build_pip_data.py`, then `python3 tools/pip_explain.py units clinical-medicine-and-surgery-i-exam-8
--out DIR`; a writer drafts cards for the NEW units, an independent Sonnet checker verifies every sentence, then
`assemble` into `pip/explain/clinical-medicine-and-surgery-i-exam-8.json` and `check` (0 errors, 0 stale).

## 7. Registration (shared files: add your lines, keep the others')

- `index.html`: inside `<details class="exam-section" data-examid="cms1-exam8">`, the lecture's four quiz links
  with `<span class="quiz-tag quiz-tag--new" data-added="YYYY-MM-DD">New</span>`; a "Master Exams" divider when
  the masters ship.
- `guides.html`: the `data-class="cms-1" data-exam="7"` subgroup holds the three Exam 8 cards; update their
  descriptions to name the new lecture.
- `tools/question_writing/scope.json` globs `Clinical Medicine and Surgery I Exam 8/*-quiz*.html` and
  `*-vignettes*.html`.

## 8. Before committing

```bash
python3 tools/add_stable_qids.py "Clinical Medicine and Surgery I Exam 8"
python3 tools/build_quiz_index.py; python3 tools/build_group_quizzes.py; python3 tools/build_cram_personal.py
python3 tools/build_planner_resources.py; python3 tools/build_exam_spines.py
python3 tools/build_guide_docx.py "Clinical Medicine and Surgery I Exam 8/cms-exam-8-study-guide.html"   # and the cram + Clin Med Pro, count 1 each
```

Review: blind export -> Sonnet judges (REVIEW_BLIND.md) -> import -> audit export `--from` -> judges
(REVIEW_AUDIT.md) -> import -> one Opus repair per flag -> re-review `--ids`. Guide links:
`tools/guide_additions/clinical-medicine-and-surgery-i-exam-8.json`, `apply_guide_additions.py` +
`verify_guide_additions.py`; re-run `apply_guide_additions.py` and `check_guide_additions_inline.py` after EVERY
`build_cms_e8_guide.py`. Then `build_guide_links.py`, `audit_guide_links.py`, `check_guide_links.py --strict`,
and `python3 tools/check_all.py "Clinical Medicine and Surgery I Exam 8"`: 0 hard failures.

Never run `check_console_errors.py`, `check_answer_distribution.py` or `check_dark_contrast.py`.
