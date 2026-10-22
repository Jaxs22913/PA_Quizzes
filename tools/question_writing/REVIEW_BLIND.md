# Blind review, pass 1 (read this fully before starting)

A PA-school study site gives real classmates practice questions. A wrong answer key does real harm, so each
question gets an independent reader before it ships. In THIS pass you are that reader and you have NOT been
given the writer's answer. Tool: `tools/blind_review.py`; rules the writer followed: `tools/question_writing/WRITER.md`.

Prompt (prompt version v1):

> Review each item using only its evidence. You have not been given the writer's answer. First cover the
> options and write the answer you would give from the stem alone. Then select the best option, or return
> ambiguous or insufficient. Give a concise justification with a verbatim quote from the evidence. Name any
> other option that is also defensible, any missing detail that would change the decision, any conflict
> between slides or with established medical fact, and any clue that gives the answer away (grammar, a
> repeated stem word, an absolute word, an unusually detailed option). Do not repair the item.

## Cost rules (Claude Code usage, not API credits)
- Compact JSON only. No long reasoning, no commentary, no rewriting of items.
- Read each deck's `evidence` ONCE per batch: all items of a batch that cite that deck share it. You do pass 1
  and then pass 2 (`REVIEW_AUDIT.md`) for the same batch in ONE session; the evidence you have already read is
  the evidence the audit batch carries, so do not re-read it.

## Input: `judge-NNN.json`
```
{"pass": "blind", "prompt_version": "v1",
 "evidence": {"<deck file>": "=== SLIDE 12 ===\ntext...\n=== SLIDE 13 ===\n..."},
 "items": [{"id": "490660d133b3b0b4", "stem": "...", "options": {"A": "...", "B": "...", "C": "...", "D": "..."},
            "evidence_slides": {"<deck file>": [11, 12, 13]},
            "evidence_images": {"<deck file>|12": ["/abs/path/s012-1.jpg"]}}]}
```
An item's evidence is ONLY the slides listed in its `evidence_slides` (the cited slide plus one either side).
There is no key, no explanation and no misconception note for any option. Do not look for them, and do not
browse the export directory or `~/.cache/pa-quizzes` for anything but the pictures listed in `evidence_images`.

`stem_image` (present only when the page shows a picture above the stem, e.g. "this chest film") is the absolute
path of that picture, copied under a neutral name. Open it with the Read tool FIRST: it is part of the question,
not evidence, and an item that refers to a picture cannot be answered without it.

`evidence_images` (present only when an evidence slide has pictures worth reading) maps `"<deck file>|<slide>"` to
absolute image paths. Open them with the Read tool; each is one picture from that slide. Pictures under ~8 KB
or 64x64 pixels (decorative) are not listed, and a few formats (some WMF/EMF) cannot be converted and are not
listed either: for those the slide text still carries the "[this slide has N picture(s) ...]" note.

## What to do for every item
1. Cover the options. From the stem alone, write the answer you would give (`cover_answer`, a few words).
2. Read the item's evidence slides. Uncover the options and choose: `pick` = `"A"`-`"D"` for the single best
   option, `"ambiguous"` if two or more options are defensible from the evidence, or `"insufficient"` if the
   evidence does not contain what is needed to decide. A note "[this slide has N picture(s) ...]" means that
   content is NOT in your text. When the decision depends on the picture (a plate, a stain, a table shown as a
   picture) and the slide is listed in `evidence_images`, open those images with the Read tool and treat what is
   CLEARLY visible as evidence (labels, a printed table, an unmistakable appearance). Do not infer from a
   picture what it does not plainly show. If the decisive picture is not listed, or not clear, answer
   `"insufficient"`; do not guess from it.
3. Use ONLY the evidence plus established medical fact. If the slides and established medical fact disagree,
   pick what the SLIDES say (students are tested from the slides) and describe the disagreement in `conflict`.
4. `quote`: a contiguous excerpt COPIED EXACTLY from the item's evidence that supports your pick (5+ words, or a
   whole short line). It is machine-checked (case, curly quotes, dashes and whitespace are ignored); an altered
   or invented quote rejects the item. Required for a letter pick; for ambiguous/insufficient give the closest
   relevant excerpt or null. When the justification rests on a picture, the quote is `"[image] <deck>|<slide>"`
   exactly as the key appears in `evidence_images` (e.g. `"[image] PAJ5200.Cocci of Med importance.pptx|34"`);
   the importer accepts that form only for a slide that has listed images, and `why` must say what you saw.
5. Fill the flags, each a short string or null:
   - `alt`: a SECOND defensible letter (A-D, not your pick) or null.
   - `missing`: the decisive detail the stem or the slides lack, if it would change the decision.
   - `conflict`: any conflict between slides, or between a slide and established medical fact.
   - `clue`: anything that gives the answer away (a/an or singular/plural that fits one option, the stem word
     repeated in one option, an absolute word in the others, one option unusually detailed or hedged).
6. Do not repair, reword or improve the item.

## Output: `verdict-NNN.json` (next to the batch; ONLY a JSON list, one object per input item, in order)
```
[{"id": "490660d133b3b0b4", "pick": "B", "cover_answer": "potassium and kidney function",
  "why": "Loop diuretics change electrolytes and renal function, so these are monitored.",
  "quote": "exact words copied from the evidence", "alt": null, "missing": null, "conflict": null, "clue": null}]
```
- `pick`: one of `A` `B` `C` `D` `ambiguous` `insufficient`.
- `why`: at most 40 words (longer is rejected).
- Every input id appears exactly once. Valid JSON only; write it with the Write tool.

When finished with the batch, continue straight to pass 2 for the same batch (the importer needs these results
in `tools/blind_review.json` first: the caller runs `blind_review.py import --pass blind DIR --judge <your model id>`,
then exports the audit batch). Reply with one line: counts of letter picks / ambiguous / insufficient.
