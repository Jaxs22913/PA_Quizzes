# CMS I Exam 6 (Respiratory Block Exam I, Lectures 33-38): how to add a lecture

Exam 6 is built a lecture or two at a time, by more than one builder. Every exam-level page is ASSEMBLED from
per-lecture pieces, so adding a lecture means dropping files in, never hand-editing a built page.
Folder: `Clinical Medicine and Surgery I Exam 6/`. Palette: crimson (navy `#7a2d30`, indigo `#b45357`, gold
`#c08a2e`, ice `#faefee`), set in `tools/render_cms_e6.py` and `tools/cms_e6_guide/_head.html`.

Lectures so far: 33 Oxygen Delivery (Reynolds) and 34 Acid-Base Part I (Finck), branch `feat/cms-e6-l33-34`;
35 Asthma and 36 COPD on `feat/cms-e6-l35-36`. Masters are HELD until Lectures 37 and 38 are in
(memory `master_exam_sizing`).

## 1. Quizzes (per lecture, your own prefix)

Per lecture `NN`: `tools/cms_e6lNN_scope.py` (verbatim syllabus IOs, EXCLUDED_SLIDES, SCOPE_BANNED, NAMED, optional
REQUIRED), pools `tools/cms_e6lNN_pool_*.py` and `tools/cms_e6lNN_vig_*.py`, then

```bash
python3 tools/cms_e6_partition.py lNNio      # and lNNvig  -> tools/cms_e6lNN_sets.json / _vig_sets.json
python3 tools/render_cms_e6.py lNNio         # and lNNvig  -> the four HTML pages
```

`cms_e6_partition.py` already has GUARDED keys `l33`-`l38` (io and vig) and runs the WRITER rules for all six
lectures. Add the lecture's four pages to `render_cms_e6.py` SPEC. Explanations follow
`tools/question_writing/EXPLAIN_DEEP.md` (key opens "Correct.", names the decisive clue; each wrong choice: the
clue it misses, the replacing fact, a "Tell:").

## 2. Study guide: one fragment per lecture

Write `tools/cms_e6_guide/lNN.html`: ONE `<section class="deck" id="<slug>">` that opens with
`<h2 class="deck-title">K &middot; Title</h2>`, where K = NN - 32 (L35 is 3, L36 is 4, L37 is 5, L38 is 6; the
builder asserts it). Inside, in this order (copy `l34.html` for the markup):

- `p.lecturer`, the `div.io-box` with the SYLLABUS objectives verbatim (`guide_verbatim_io_rule`);
- a `div.callout` of what the lecturer stressed (recording emphasis only; facts still from the slides);
- a `div.callout.warn` "Where the slides are loose or disagree";
- `h3.sub` subsections, each with an id starting `lNN-` (they become the table of contents), answering the IOs
  in order; starred emphasis in `div.prof-flag` with `id` + `data-toc` (shown starred in the contents) and
  `mark.prof-highlight`;
- for each disease, a `div.cond` block with the eight points in `dl.eight` (definition, who gets it, risk
  factors, classic signs and symptoms, physical exam, diagnostics, first-line treatment, complications) and
  `p.src` slide numbers.

Then `python3 tools/build_cms_e6_guide.py` (writes `cms-exam-6-study-guide.html`, generated contents, dark
palette for this page only; it fails on duplicate ids or a dangling `#` link).

## 3. Cram sheet

Write `tools/cms_e6_cram/lNN.py` defining `TOPICS` (copy `l34.py`): a gold `#b8860b` "★ Professor Emphasized"
card first, then topic cards, every topic id starting `lNN-`. Condense the guide; add nothing new.
`python3 tools/build_cms_e6_cram.py`. Add the lecture's short name to `NAMES` in that script.

## 4. Clin Med Pro

Append a lecture object to `tools/clinmedpro/cms-e6.json` (`lectures` list, in lecture order): `lecture`,
`title`, `lecturer`, `deck`, `note`, `conditions` (each `id` "lNN-...", `name`, `prof`, `prof_note`, the ten
`fields`, `slides`). A field the deck does not cover is exactly "Not covered in the lecture"; `[[★ phrase]]`
marks emphasis. `python3 tools/build_cms_clinmedpro.py 6` (rebuild only exam 6).

## 5. Arcade

Write `tools/cms_e6_arcade/lNN.json`: a list of decks `{"id": "cms-e6-lNN-<topic>", "name", "color":
"accent1|accent2|accent3", "icon": "<svg paths>", "cards": [[prompt, answer], ...]}`, atomic facts only
(`arcade_content_policy`). `python3 tools/add_cms_e6_arcade.py` rewrites the fenced block in `arcade.js` and the
CMS group's "Exam 6" entry from every lecture file present (test first with `ARCADE_JS=<scratch copy>`).

## 6. Pip cards

`python3 tools/build_pip_data.py`, then `python3 tools/pip_explain.py units clinical-medicine-and-surgery-i-exam-6
--out DIR`. A writer drafts cards for the NEW units only (`pip_explain_STYLE.md`, `lint` each part), an
independent fact-checker verifies every sentence, then `assemble` into
`pip/explain/clinical-medicine-and-surgery-i-exam-6.json` and `check`. After a guide edit, `check` lists stale
cards; re-read them, then `rehash`.

## 7. Registration (shared files: add your lines, keep the others')

- `index.html`: inside `<details class="exam-section" data-examid="cms1-exam6">`, add the lecture's four
  quiz links with `<span class="quiz-tag quiz-tag--new" data-added="YYYY-MM-DD">New</span>` (`new_exam_tag`).
- `guides.html`: the `data-class="cms-1" data-exam="6"` subgroup already holds the three Exam 6 cards; update
  their descriptions to name the new lecture.
- `tools/question_writing/scope.json` already globs `Clinical Medicine and Surgery I Exam 6/*-quiz*.html` and
  `*-vignettes*.html`.

## 8. Before committing

```bash
python3 tools/add_stable_qids.py "Clinical Medicine and Surgery I Exam 6"
python3 tools/build_quiz_index.py; python3 tools/build_group_quizzes.py
python3 tools/build_guide_docx.py "Clinical Medicine and Surgery I Exam 6/cms-exam-6-study-guide.html"   # and the cram + Clin Med Pro
```

Review (`/new-exam-build`, CLAUDE.md section 5-7): blind export -> Sonnet judges (REVIEW_BLIND.md) -> import ->
audit export `--from` -> judges (REVIEW_AUDIT.md) -> import -> one Opus repair per flag -> re-review `--ids`.
Guide links: `tools/guide_additions/clinical-medicine-and-surgery-i-exam-6.json` (append your lecture's
additions), `apply_guide_additions.py` + `verify_guide_additions.py`. A guide rebuild drops the added lines;
re-run `apply_guide_additions.py` (idempotent, same ids) and `check_guide_additions_inline.py` after EVERY
`build_cms_e6_guide.py`. Then `build_guide_links.py`,
`audit_guide_links.py`, `check_guide_links.py --strict`. Finally `python3 tools/check_all.py "Clinical
Medicine and Surgery I Exam 6"`: 0 hard failures.

Never run `check_console_errors.py`, `check_answer_distribution.py` or `check_dark_contrast.py`.
