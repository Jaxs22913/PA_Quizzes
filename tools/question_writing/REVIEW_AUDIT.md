# Audit, pass 2 (read this fully before starting)

Pass 2 of the question review (`tools/blind_review.py`; pass 1 is `REVIEW_BLIND.md`). You are the SAME judge, in
the same session, and the evidence for the batch is the evidence you already read in pass 1. The audit batch is
only produced for items that already have your blind result, and it carries it back to you.

Prompt (prompt version v1):

> Compare your blind result with the writer's key. Audit every explanation against the evidence: unsupported
> claims, an explanation that says a distractor is always wrong when it is only wrong in this case,
> misleading exclusions, inconsistency between options and explanations. Return pass, revise or hold, each
> defect with the field, a short reason and a verbatim quote, and the smallest correction. Factual error,
> unresolved ambiguity, source conflict and an unsupported decisive claim are blocking. Agreement with the
> writer does not establish correctness. Never label an item clinically reviewed.

## Cost rules (Claude Code usage, not API credits)
Compact JSON only, no long reasoning, no rewriting of whole items. Do not re-read evidence you already read.

## Input: `judge-NNN.json`
```
{"pass": "audit", "prompt_version": "v1",
 "evidence": {"<deck file>": "=== SLIDE 12 ===\n..."},
 "items": [{"id": "...", "stem": "...", "options": {"A": "...", ...},
            "evidence_slides": {"<deck file>": [11, 12, 13]},
            "evidence_images": {"<deck file>|12": ["/abs/path/s012-1.jpg"]},        (only when a slide has pictures)
            "key": "B",
            "explanations": {"A": "...", "B": "...", "C": "...", "D": "..."},
            "mis": {"A": "the misconception this distractor stands for"},        (only when the writer recorded it)
            "your_blind_result": {"pick": "B", "cover_answer": "...", "alt": null, "missing": null,
                                  "conflict": null, "clue": null}}]}
```

## What to do for every item
1. Compare `your_blind_result` with `key`. A different pick, `ambiguous` or `insufficient`, an `alt`, a
   `missing` detail or a `conflict` from pass 1 are NOT settled by the writer having a key: re-check the
   evidence. A key that follows the slides where current guidelines differ is CORRECT (students are tested from
   the slides): not a defect, but name the difference in a defect-free note so the guide gets a line. Agreement between you and the writer is a signal, not proof.
2. Slide pictures: when the slide text says it has pictures and the key or an explanation depends on them, and
   the slide is listed in `evidence_images`, open the listed images with the Read tool (skip any you already
   opened in pass 1) and treat what is CLEARLY visible as evidence. A claim that rests on a picture that is not
   listed, or not clearly visible, is an unsupported claim.
   Read every option's explanation against the evidence slides and look for:
   - an unsupported claim (a medical statement not on the item's slides and not flagged as a correction);
   - an explanation that calls a distractor "always" or "never" wrong when it is only wrong in THIS case;
   - a misleading exclusion (it refutes the distractor for the wrong reason);
   - inconsistency (the key's explanation and a distractor's explanation contradict each other, or an
     explanation argues for a different option than the one it sits under);
   - a `mis` that does not match what its distractor actually is.
3. Verdict:
   - `pass`: no defect. Nothing listed.
   - `revise`: fixable defects with no blocking problem; give the smallest correction in `fix`.
   - `hold`: any BLOCKING problem: factual error, unresolved ambiguity (two defensible answers), a source
     conflict, or an unsupported decisive claim. The item is dropped and replaced; `fix` is optional.
4. Each defect: `field` (`stem`, `key`, `explanation A`-`explanation D`, `option B`, `mis C`, ...), `reason`
   (one short sentence), `quote` (verbatim, machine-checked): normally an excerpt of the item's evidence that
   shows the problem or the correct fact; for an unsupported claim there may be nothing on the slides to
   quote, so quote the offending sentence from the item itself. An altered quote rejects the item. For a defect
   that rests on what a picture shows, the quote is `"[image] <deck>|<slide>"` (the key as it appears in
   `evidence_images`); it is accepted only for a slide that has listed images, and `reason` must say what is visible.
5. Never call an item "clinically reviewed". Do not rewrite the item; `fix` is the smallest correction only.

## Output: `verdict-NNN.json` (ONLY a JSON list, every input id once, in order)
```
[{"id": "...", "verdict": "pass", "defects": [], "fix": null},
 {"id": "...", "verdict": "revise",
  "defects": [{"field": "explanation C", "reason": "Says always wrong; it is only wrong at this stage.",
               "quote": "exact words from the evidence or the item"}],
  "fix": "In explanation C replace 'always' with 'at this stage'."}]
```
`pass` must have an empty `defects` list; `revise` and `hold` need at least one defect; `revise` needs `fix`.
Reply with one line: counts of pass / revise / hold. The caller then runs
`blind_review.py import --pass audit DIR --judge <your model id>`.
