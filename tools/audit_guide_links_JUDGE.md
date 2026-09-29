# Judging guide links (read this fully before starting)

A PA-school study site links each practice question to the passage of the class study
guide that is supposed to EXPLAIN the concept behind the correct answer. Your job is to
check, independently and strictly, that it really does. Students' grades depend on this.

## Input
A JSON list. Each item:
- `id` — copy it back unchanged
- `question`, `answer` (the correct answer), `explanation` (the author's explanation of why it is correct)
- `paragraphs` — up to six numbered paragraphs (`n`, `text`) from the guide section the question links to

## For every item decide ONE verdict
- **PASS** — at least one paragraph STATES the fact/concept that makes `answer` correct. The
  wording may differ, but the CLAIM must be the same, including any number, threshold,
  negation ("not", "only", "no"), direction (higher/lower), and scope ("in children", "first-line").
  A student who read that paragraph would be able to answer the question correctly from it.
- **PARTIAL** — right topic (same disease/drug/structure), but no paragraph actually states the
  fact needed. It only mentions the subject, or states a neighboring fact, or is missing the key
  number/qualifier.
- **FAIL** — the paragraphs are about a different concept.

Be strict. When in doubt between PASS and PARTIAL, choose PARTIAL. A paragraph that merely
contains the same words is NOT a PASS if it does not make the claim. A paragraph that
contradicts the answer is a FAIL. Do NOT use your own medical knowledge to fill a gap: only what
the paragraph itself says counts.

## For PASS you MUST give proof
- `para`: the number `n` of the paragraph that states it (pick the best one)
- `quote`: a contiguous excerpt COPIED EXACTLY, character for character, from that paragraph's
  `text` (at least 6 words, ideally the single sentence or clause that states the fact). It is
  machine-checked; an invented or altered quote turns your PASS into a rejection. Do not
  include the trailing " ..." that marks a truncated paragraph.

## Output
Write ONLY a JSON list to the output path you are given, one object per input item, in order:
`{"id": "...", "verdict": "PASS", "para": 3, "quote": "exact words from paragraph 3"}`
or `{"id": "...", "verdict": "PARTIAL"}` or `{"id": "...", "verdict": "FAIL"}`.
Use the Write tool. Valid JSON only. Every input item must appear exactly once.

## Example
question: "Where is minoxidil primarily effective?" answer: "In the crown region of the scalp"
- paragraph says "Minoxidil works at the crown of the scalp; it slows loss and may regrow hair." -> PASS, quote "Minoxidil works at the crown of the scalp".
- paragraph says "Minoxidil is a topical treatment for hair loss." -> PARTIAL (topic right, region not stated).
- paragraph about finasteride only -> FAIL.

When you finish, reply with one line: counts of PASS / PARTIAL / FAIL.
