# -*- coding: utf-8 -*-
"""Shared helper and style contract for the Updated CMS ophthalmology masters.

THE STYLE IS TAKEN FROM SIX EXEMPLARS JAXON SENT (2026-09-05), not from the
derm masters, and it differs from them in ways that matter:

  STEM. Age first, plus sex or ethnicity WHEN IT CARRIES RISK (the 64-year-old
  African American diabetic). Duration and evolution stated as a sequence --
  "for the first day or two it was red and painful; now it is painless, but it
  has grown" -- because the discriminator is usually in the narrative rather
  than the findings.

  PERTINENT NEGATIVES ARE AIMED AT SPECIFIC DISTRACTORS. "No pain... not
  nauseated" exists to kill acute angle-closure sitting at option 2. Every
  negative should be answerable with "which option does this eliminate?"

  EXAMINATION. Sometimes numeric vitals, sometimes "vitals are normal" -- both
  appear. Then the findings, with a measurement where there is a lesion.

  NAMED SIGNS, TWO WAYS. Either the jargon in quotation marks ("boxcar"
  pattern, "steamy" cornea) or the plain description with the term in brackets
  ("sensitivity to light (photophobia)"). The exemplar for uveitis describes
  limbal injection WITHOUT ever calling it a ciliary flush.

  STEM LENGTH VARIES A LOT. Three of the six are full paragraphs with vitals;
  one is three sentences. Do not make all 325 the same shape.

  LEAD-INS. diagnosis | next step in managing | initial treatment | and the
  TWO-STEP form, where the vignette is only a gate and the question asks for an
  organism, mechanism or complication of a condition it never names.

  OPTIONS. Five, short, ONE REGISTER per question -- five conditions, or five
  actions, or five organisms. Never mixed.

ANSWER POSITION IS NOT SET HERE. Every question is authored correct-first for
readability and the partitioner permutes onto a balanced A-E cycle. Rendering
straight from a pool is the PD1 bug ([[answer_position_bias_check]]).

LENGTH BIAS: shorten the KEY, never pad distractors (Jaxon 2026-08-30), and do
not chase 0% -- the reference set itself sits near 13%.
"""

import re

LEADS = ("diagnosis", "next step", "treatment", "two-step")


def Q(topic, io, q, opts, lead, deck, slide, c=0):
    """One master-exam question.

    `opts` is a list of [text, explanation]; the CORRECT one is written first
    and `c` stays 0 until the partitioner moves it.
    """
    assert len(opts) == 5, "five options: %s" % q[:50]
    assert lead in LEADS, "unknown lead-in %r" % lead
    assert len({o[0] for o in opts}) == 5, "duplicate option: %s" % q[:50]
    assert len({o[1] for o in opts[1:]}) == 4, "shared refutation: %s" % q[:50]
    # WORD BOUNDARY, not prefix. A distractor reading "Correcting the refractive
    # consequence does not address..." is not opening with "Correct" -- the same
    # trap the Exam 2 partition validator already documents.
    assert re.match(r"correct\b", opts[0][1], re.I), "key explanation must open 'Correct'"
    for o in opts[1:]:
        assert not re.match(r"correct\b", o[1], re.I), \
            "distractor opens with Correct: %s" % o[0]
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c,
            "lead": lead, "deck": deck, "cite": "%s, Slide %d" % (deck, slide)}
