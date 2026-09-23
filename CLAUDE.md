# PA_Quizzes — orientation for a new session

**Written 2026-09-22.** Claude Code reads this file automatically at the start
of every session in this repo. It is the map, not the territory: it tells you
what exists and where the real detail lives, so read the things it points at
rather than trusting the summary.

---

## 1. What this is, and who it is for

A static study site Jaxon builds for his PA-school cohort (Class of 2028, Nova
Southeastern, Jacksonville). Quizzes, study guides, cram sheets, an Arcade of
games, group study, a practicum atlas. Everything is per-class and per-exam.

**Real people use it to study for real exams.** A wrong answer key is not a
cosmetic bug. That is the reason for the checker suite in §6 and the standing
rule that you run it on every build.

**The repository is PUBLIC.** Anything committed is republished at the live URL.
That governs image licensing, and it means lecture audio, transcripts and raw
decks stay OUT of the repo — they live on the Desktop (§4).

---

## 2. Read this first: the memory index

The accumulated knowledge is **not** in this repo. It is in

```
~/.claude/projects/-Users-jaxonluke/memory/
```

`MEMORY.md` there is the index — one line per memory — and it loads into context
automatically. **When a task touches an area, open the specific memory file
before acting.** The index line is a pointer, not the content.

The ones worth reading before almost any content work:

| Memory | Why |
|---|---|
| `quiz_build_prompt.md` | Jaxon's verbatim standing spec for building any quiz |
| `exam_standard.md` | the standard every exam is built to; a checker enforces it |
| `guide_design_system.md` | the shared structural template for guides and quizzes |
| `reference_question_style.md` | the 40 exemplars he supplied; four options site-wide |
| `pa_quizzes_hosting.md` | deploy, and why "pushed" ≠ "live" |
| `site_bug_sweep_tools.md` | the checkers you must run |

Each class also has its own spec memory (`microbiology_exam_spec.md`,
`cms_exam_spec.md`, `pharmacology_exam_spec.md`, …). **A class-specific spec
overrides the general one on conflict.**

Memories are point-in-time notes. If one names a file, function or flag, verify
it still exists before relying on it.

---

## 3. How the site runs

- Local clone: `~/Developer/PA_Quizzes`, branch `main`.
  (It was moved out of `~/Documents` in July 2026 — iCloud sync was spawning
  conflict copies mid-build and twice a wrong copy nearly shipped. Do not move
  it back.)
- Live: `https://jaxs22913.github.io/PA_Quizzes/`
- Every push to `main` fires a GitHub Actions workflow that deploys in ~50s.

**A successful push is not a deploy.** During a GitHub outage three pushes
landed with no workflow run created at all, and the live site served the old
build for hours while the push output looked fine. After pushing, check the live
URL — `curl` the changed file and grep for a string only the new version has.

Pages serves with a **10-minute cache**, so "I pushed but don't see it" is
usually that window. Hard refresh or a private window confirms it.

---

## 4. Where the inputs live (not in the repo)

```
~/Desktop/Semester 2/<Class> Inbox/
    Syllabus/
    Exam N/                    ← the .pptx decks
    Exam N/recordings/         ← lecture audio + transcripts
~/Desktop/Calendars/<Semester>/<Month>.pdf   ← the printed academic calendar
```

- A new class auto-gets an Inbox folder (`class_inbox_convention`).
- `calendar-data.js` in the repo is **generated** from those calendar PDFs by
  `tools/gen_calendar_data.py`. Never hand-edit it. It is also the only source
  that **names the lecturer for each lecture** — the syllabus does not.
- Lecture recordings come out of Notability; `tools/pull_notability_audio.py`
  and the `notability_audio_pipeline` memory cover the extraction, including two
  traps that make a recording that IS there read as absent.

---

## 5. Building things

### The layered pipeline — know which layer you are editing

For most exams the chain is:

```
question pool  →  partition script  →  sets.json  →  renderer  →  shipped HTML
tools/*_pool*.py                                    tools/quiz-template/render.py
```

**Editing a pool does not change the website.** The pool feeds a partition
script that writes `sets.json`, and only re-rendering reaches the HTML. This has
bitten before: a full cleanup of 233 question pools left 46 shipped pages still
carrying the old text because they were never re-rendered. Partition scripts are
seeded, so regenerating reproduces the same selection with only text changed.

Simpler one-off quizzes skip the partition step: pool → renderer → HTML. The
Micro Exam 1 timetable quiz (§8) is the clean example to copy —
`tools/micro_e1_hours_pool.py` + `tools/render_micro_e1_hours.py`.

### Quizzes

1. Read `quiz_build_prompt.md` and the class's own spec memory.
2. Ground every question in the deck. Extract slide text with `python-pptx`,
   keep `=== SLIDE N ===` markers, and cite **exact filename + slide number**.
3. Use the mandatory engine: `tools/quiz-template/render.py`
   (`quiz_engine_standardization`). Do not roll a new one.
4. Register the quiz in `index.html` under the right class/exam section, with a
   self-expiring New tag (`new_exam_tag`).
5. Re-run `tools/build_group_quizzes.py` — **required after any quiz change.**
   The Group Study bank is generated from the quiz files; never hand-edit it.
6. Run the checkers (§6), fix, then commit and push. For quiz builds
   specifically, pushing is part of the spec — you do not need to wait to be
   asked.

### Guides, cram sheets, Arcade, RPG

- Guides: `guide_design_system` + `guide_verbatim_io_rule` (the objectives box
  must quote the syllabus verbatim and answer each one in order).
- Cram sheets: `tools/cram-sheet-template/`, one per exam, GREEN badge on
  `guides.html` (`cram_sheets_feature`).
- Arcade: `arcade_content_policy` and `arcade_integration`.
- RPG: local only, **do not push** (`rpg_local_art_pipeline`).

---

## 6. The checkers — run them, do not trust memory

33 live in `tools/check_*.py`. The standing minimum after any quiz build:

```bash
python3 tools/check_answer_key_consistency.py "<file>"   # keys must be right
python3 tools/check_exam_standard.py --new
python3 tools/check_self_contained.py "<Class Exam N>"
python3 tools/check_leadin_present.py "<file>"
python3 tools/check_console_errors.py "<file>"
python3 tools/check_answer_distribution.py "<file>"
```

Others worth knowing: `check_length_bias`, `check_ppt_grounding`,
`check_truncated_keys`, `check_accordions_closed`, `check_spelling`,
`check_slot_coverage`, `check_pool_cites`.

`check_length_bias.py` drives headless Chrome and is slow and fragile; a
node-based literal extractor does the same job vastly faster and was validated
to produce identical numbers.

---

## 7. Content rules that are always on

These are the ones most often broken. Each has a memory with the full story.

- **Four options.** Site-wide, no exceptions (the earlier five-option rule was
  reversed 2026-09-13).
- **Every stem asks exactly ONE thing.** Stacked stems test three things at once
  and tell the student nothing about which part they missed.
- **Every stem is self-contained.** Never cite the lecture, the deck, the
  professor or the syllabus; never build a question on a lecture's worked
  example. A question that stops making sense without the deck open is broken.
- **Every option gets its own explanation** that refutes AND supplies the
  replacing fact, ≥60 characters.
- **Distractors match the key's length and style.** When the key is too long,
  **shorten the key** — never pad the distractors.
- **Permute answer positions** before shipping. Authoring every key in position
  A and shipping it has happened more than once.
- **No abbreviations**, or write them as `ABBREV (full term)`.
- **Slides-only grounding.** Content comes from the deck. A lecturer's aside
  does not add content the deck lacks.
- **Semester 1 exams are frozen** — never modify them.

---

## 8. State as of 2026-09-22

- **Microbiology Exam 1 was sat 2026-09-21** (Lectures 1–6). Two papers exist
  for it: the objective-weighted `micro-exam-1-exam-style-quiz.html` (77 q) and
  the timetable-weighted `micro-exam-1-timetable-weighted-quiz.html` (65 q,
  five per scheduled lecture hour). See `timetable_weighted_exams`.
  - Per the standing `guides_fan_past_exams` rule, a sat exam's `guides.html`
    sub-group should get `data-stack="1"` so its cards fan into a stack. **Not
    yet done for Micro Exam 1.**
- All 292 question banks are free of lecture/professor citations as of
  2026-09-20 — but **46 shipped quiz pages still carry old citations** because
  their topics were never re-rendered (§5). Flagged, not done.
- Micro Lecture 6 audio was recovered 2026-09-20 and transcribed; Lectures 1–6
  all have transcripts now.
- Micro has two lecturers: **Webster** (1, 2, 5, 7, 10, 12, 14, 17, 18) and
  **Fair** (3, 4, 6, 8, 9, 11, 13, 15, 16, 19). Webster reviews in class and
  signposts; Fair gives **no** examinability signposting across ~205 measured
  minutes, so weight his lectures by time-on-topic instead
  (`transcript_emphasis_measurement`).

### Open items, none of them started

- Guides and cram sheets for the four new Exam 2 topics.
- Master exams for Exam 2 blocks (held by standing rule until block content is
  complete).
- Thin CMS Exam 3 master-exam stems (median 38 words against a 78-word
  reference).
- A factual error flagged for Jaxon's decision in `pdm_l2_pool_c`: the keyed
  answer says contrast dyes "are technically radioactive", which is false. The
  key was left alone because it is what the deck teaches; the explanation now
  states the accurate position.

---

## 9. How to work here

- **Verify empirically.** Measure rather than assert; when you report a number,
  have run the thing that produced it.
- **Match the existing pattern before inventing one.** Nearly everything has a
  precedent in `tools/`.
- **Flag rather than silently resolve.** When a source contradicts itself or the
  arithmetic does not close, say so in the output and the commit message. A
  recent example: an exam's scheduled hours predicted 70 questions but the exam
  had 65, and the honest move was to apportion the real 65 and name the gap.
- **Diff after every rule change** when doing bulk rewrites. Regenerating and
  diffing against the previous run is what catches the defect classes that
  reading the rule never will.
- Standing push permission since 2026-07-16 — but say what you pushed.
