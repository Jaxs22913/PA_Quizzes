# Writing a question: the runtime rules (v1, 2026-10-15)

Distilled from the "PA Quizzes question writing and quality guide" Jaxon supplied on 2026-10-15 (NBME item-writing
guidance, Anthropic's hallucination guidance, studies of AI-written medical questions). This file says HOW each item
is written and checked. It never overrides:

- **the class spec memory**, which decides question TYPES, counts and splits (CMS: 2 instructional-objective sets + 2
  vignette sets per topic; Clinical Pathophysiology: mechanism only, no vignettes, never management; Pharmacology:
  the 6-point drug frame, no dosages; Microbiology / PDM: 2 x 30 per topic; masters per `master_exam_sizing`);
- **the standing content rules** in CLAUDE.md section 7 (four options, one ask, self-contained, refute + replacing
  fact, length and style match, no abbreviations, slides-only grounding, truth wins on conflict, US spelling).

## Before drafting (once per lecture)

1. **Blueprint.** List the syllabus objectives (verbatim) and the deck's fact slots (`cms_fact_slots`,
   `tools/check_slot_coverage.py`). Give every item ONE objective and ONE decision. Spread items across objectives so
   no objective is crowded while another gets nothing.
2. **Evidence.** Only what is VISIBLE on a slide counts (its text and pictures); speaker notes do not (Jaxon,
   2026-10-15). For each item, find the slide(s) stating the decisive fact AND the facts each option explanation will
   use. Read the neighbouring slides too: a nearby exception, threshold or population can reverse the answer. View
   every image; never write an image-dependent item from a text summary of a picture.

## Writing

1. **Cover the options.** The stem and lead-in alone must define one answer: a reader who covers the choices can
   still answer.
2. **Enough case, nothing invented.** Give the findings that make one answer best. A fictional detail may set the
   scene but never adds an unsupported medical assumption; a detail that could change the answer is decided by the
   deck or left out.
3. **Management items state what decides the action**: stability, severity, prior treatment, contraindications,
   timing. (Where the class spec excludes management, never write one.)
4. **Difficulty comes from the decision**, never from length, irrelevant labs or rare trivia (unless the objective IS
   the exception).
5. **Every distractor is a real misconception.** Record it on the option in the pool as `mis`: competing diagnosis /
   right action at the wrong stage or severity / ruled out by a stated finding / confused mechanism or drug class /
   adjacent fact from the same lecture / reversed direction or value / common lay belief. No filler; no two options
   meaning the same thing; no option containing another; no "all of the above", "none of the above" or "both A and B".
6. **Explanations.** The key's explanation connects the decisive findings to the answer. Each distractor's
   explanation says why it is wrong IN THIS CASE (not "always wrong") and supplies the replacing fact. Every medical
   claim in every explanation is on a slide (or is a truth-wins correction you flagged).
7. **Remove clues**: "a"/"an" or singular/plural that fit only the key; the key repeating a distinctive stem word no
   distractor shares; absolutes (always, never, only, all) only in distractors; the most detailed or most hedged
   option being the key; position patterns.
8. **Numeric or ordered options** (values, ages, durations, counts, stages, grades) are listed in ascending
   order and NOT shuffled; the key sits where its value falls.
9. **Patients** are described respectfully; age, sex, race or ethnicity appear only when the deck ties them to the
   disease or the decision.
10. **Hold, don't force.** If the deck cannot support one defensible best answer (two defensible answers, missing
    evidence, a slide-versus-truth conflict you cannot settle), drop the item and write a different one from another
    fact. If the deck runs out of supportable facts before the count, ship fewer and tell Jaxon the shortfall. Never pad.

## After writing: the checks, in order

1. **Deterministic**: `python3 tools/check_all.py "<folder>"` (includes the item-quality flags).
2. **Blind review** (`tools/blind_review.py`, judges on Sonnet, `REVIEW_BLIND.md`): the judge sees the stem, the
   options and the deck evidence, NOT the key or the explanations. It answers from the stem alone first, then picks,
   and flags a second defensible answer, a missing decisive detail, a source conflict or a clue.
3. **Audit** (`REVIEW_AUDIT.md`): the same judge then gets the key and every explanation and returns pass / revise /
   hold, each defect with a verbatim slide quote.
4. **One repair**: the writer (Opus) fixes the named defects from the same evidence; the changed item goes through
   steps 2 and 3 again. Still failing: hold it (drop and replace). A judge picking a different answer than the key is
   a possible WRONG KEY: check the slide and the truth first (`truth_wins_on_conflict`).
5. **Guide links** as before (CLAUDE.md section 7).

Agreement between writer and judge is a signal, not proof. Never call an item "clinically reviewed": nobody in this
pipeline is a clinical reviewer. After release, the students' Report button and the class-picks percentages are the
signals to watch.

## Cost (Jaxon, 2026-10-15: "for us its token usage instead of API credits")

Every review spends Claude Code usage, not API credits, so: judges run on Sonnet; one judge reads one lecture's slide
text once for a whole batch and does both passes in the same session; outputs are compact JSON, no long reasoning; a
record is keyed to the item's exact text, so an unchanged item is never reviewed twice, and a master-exam copy of a
reviewed topic question reuses its record. Never route this through Pip's helper or any API batch job
(`no_bulk_model_runs`).
