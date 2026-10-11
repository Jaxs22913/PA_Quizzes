# "Pip explains" cards: the spec

Pip is the study buddy on PA Quizzes (a study site for one physician assistant class). When a student
asks him about something, he now answers with a short plain-language EXPLANATION of the concept, and
then links to the place in their study guide. These cards are those explanations. Real students read
them days before real exams, so every fact must be right.

Jaxon (the student who runs the site): "I want him to explain the concept questioned in easier to
understand language. There doesn't need to be a word limit but don't make it a whole page for each
explanation."

## Input

A units file: `units/<slug>.units.json` -> `{"s": slug, "units": [{u, doc, page, heading, anchors, a, text, h, chars}]}`.
Each unit is one section of the exam's study guide (page `doc`, section heading `heading`), with all its
text in `text` (one line per paragraph, list item or table row; table cells are joined with " — ").
The study guide is your ONLY source of facts.

## Output: one card per concept a student would ask about

```json
{"id": "type-iii-hypersensitivity", "u": "u3",
 "t": "Type III hypersensitivity (immune complex reactions)",
 "k": ["type 3 hypersensitivity", "immune complex disease", "serum sickness", "Arthus reaction"],
 "q": ["what is type 3 hypersensitivity", "how do immune complexes cause damage", "what's an example of a type III reaction"],
 "x": "..."}
```

- `id` kebab-case, unique in the exam.
- `u` the unit the card is written from (its facts come from that unit's text; the card links there).
  If two units cover the same concept, write ONE card from the fuller unit.
- `t` the concept's name as a student would recognize it (<= 80 characters).
- `k` 1-8 other names a student might type: synonyms, the abbreviation, an eponym, a common short form.
- `q` 2-4 natural questions a student might ask Pip about it, varied (what / why / how / difference).
- `x` the explanation (rules below).

What counts as a concept: a disease or condition, a drug class or a key drug, a mechanism, a sign, a
maneuver, an exam technique, a test and what its result means, a rhythm, a formula and what it tells
you, a classification and how its groups differ. A big section usually yields several cards (one per
type, one for the overview, one for a "why" the section explains); several tiny related items can share
one card. Roughly one card per 500-1,200 characters of real teaching text. Do not pad.

Skip: "Instructional Objectives" lists that only repeat later sections, "How to use this guide",
navigation, footnotes, "not covered" notes, image captions with nothing to explain, course logistics.

## How to write `x`

1. **First sentence answers "what is it?" directly**, in plain words. No warm-up ("Great question!").
2. **Explain, don't list.** Connect cause to effect: say why it happens and why it matters, when the
   guide gives the why. A student who read the guide and didn't get it should get it from this.
3. **Plain language.** Short sentences. The first time you use a technical term, say what it means in
   everyday words, or use the everyday word instead. Write as a sharp classmate explaining it over coffee:
   warm, confident, clear. Not childish, not cutesy, no exclamation-mark cheerleading, no emoji.
4. **One analogy at most, and only when it genuinely makes the idea click** ("think of the AV node as a
   toll booth that makes every beat wait a moment"). For a multi-part idea, one connected picture beats
   several unrelated ones. An analogy must never contradict the guide or suggest a false fact.
5. **A contrast line when students often mix two things up** ("Quick way to tell it from type II: ...").
6. **Length: about 60-180 words.** No hard limit, but never a page. Two short paragraphs (separated by a
   blank line) or a sentence plus up to 5 short `- ` dash bullets when it is a list or a comparison.
   Plain text only: no headings, no bold, no markdown tables, no HTML.
7. **Grounding.** Every medical fact must be stated in the unit's text. Rephrasing, simplifying and
   analogies are fine; NEW medical facts are not (no extra causes, drugs, numbers, criteria or
   associations the guide doesn't give). Everyday connective knowledge ("arteries carry blood away from
   the heart") is fine. If the guide's text looks medically wrong or garbled, do NOT repeat it: leave
   that fact out and add a flag (below).
8. **No doses**, no personal medical advice.
9. **Never mention** the lecture, slides, deck, professor, instructor, recording, syllabus, objectives,
   "the guide says", "Professor emphasized", or the exam. State the fact itself.
10. **No abbreviations** unless spelled out where they first appear: "electrocardiogram (ECG)" or
    "ECG (electrocardiogram)"; afterwards the short form is fine. Prefer the plain words when that reads
    naturally. Roman numerals (type III) are fine; DNA and RNA are fine.
11. **US spelling** (edema, tumor, hemoglobin, anemia, esophagus, diarrhea, pediatric, -ize). Taxonomic
    names keep their spelling (Haemophilus).
12. Keep numbers, cutoffs and criteria EXACTLY as the guide gives them. Keep hedges too: "usually",
    "one of the most common", "can result from" must not become "always", "the most common", "causes".
13. When the guide corrects its own source (a "truth" note, "the slide says X but actually Y", "no
    longer recommended"), the card states ONLY the corrected version, in the card a student would find
    when asking about that topic. Never leave the outdated version in the main card.
14. One question, one answer: never write two cards that answer the same question differently. Merge
    them, or make each clearly about a different thing.
15. Electrocardiogram wave and interval names (P wave, QRS complex, PR interval, ST segment, QT, V1-V6)
    are names, not abbreviations: use them as they are. Never invent an expansion to satisfy the linter;
    if a real abbreviation's full term is not known from the guide, use the plain words instead.

## Two examples of the bar (from the Microbiology Exam 2 guide's hypersensitivity section)

```json
{"id": "type-iii-hypersensitivity", "u": "u3", "t": "Type III hypersensitivity (immune complex reactions)",
 "k": ["type 3 hypersensitivity", "immune complex disease", "serum sickness", "Arthus reaction"],
 "q": ["what is type 3 hypersensitivity", "how do immune complexes cause damage", "what's an example of a type III reaction"],
 "x": "Type III is the immune complex reaction. Immunoglobulin G or M antibodies grab antigens that are floating free in the blood, not stuck to a cell, and the two clump together into small immune complexes. Those clumps lodge in basement membranes, typically in the joints, skin and kidneys, and complement and phagocytes arrive to clear them, inflaming the tissue around them. So the damage lands wherever the clumps settle, hours to days later, which is why the classic examples are serum sickness and autoimmune conditions such as lupus.\n\nA small, local version is the Arthus reaction: a patch of inflamed skin blood vessels at the site of a repeat vaccine injection, which usually settles on its own. Quick way to tell type III from type II: in type II the antibody hits antigens on a cell's surface; in type III it hits antigens floating in the blood."}
```

```json
{"id": "hygiene-hypothesis", "u": "u3", "t": "The hygiene hypothesis",
 "k": ["hygiene hypothesis", "why allergies are increasing", "helminths and allergy"],
 "q": ["what is the hygiene hypothesis", "why do parasite infections protect against allergies"],
 "x": "The hygiene hypothesis explains why allergies are more common where parasitic worm infections have been wiped out. Many allergens look a lot like parasite antigens, and a worm infection triggers the same immune profile as allergy: type 2 helper T cell responses, lots of immunoglobulin E, and more eosinophils and mast cells. Yet people with chronic worm infections don't get allergic disease, for two reasons. The flood of nonspecific immunoglobulin E takes up the receptors on mast cells, basophils and eosinophils, leaving less room for allergen-specific antibody, and regulatory T cells keep T cell responses turned down during the long infection.\n\nRemove the worms with better hygiene, vaccines and antibiotics, and that arm of the immune system is underused and less well regulated, so it overreacts to harmless things."}
```

## Flags and skips

Put anything you could not write safely in `flags` (`{"u": "u7", "issue": "the guide says X, which looks wrong because Y"}`)
and sections you deliberately skipped in `skipped` (`{"u": "u1", "why": "objectives list repeating u2-u10"}`).
