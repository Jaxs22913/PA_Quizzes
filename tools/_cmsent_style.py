# -*- coding: utf-8 -*-
"""Shared helper and style contract for the CMS I Exam 3 (ENT) master exams.

Jaxon, 2026-09-08, with eleven worked vignettes attached:

    "Master exams 50 questions each. Give deep explanations for each question
     answer that tells why the correct answers are correct and why the
     distractors are incorrect not just 'this isnt correct because its not
     correct.'"

and, a moment later, "You can just do 4 answer choices not 5" -- which
overrides the five-option rule in [[reference_question_style]] for this block.

THE EXPLANATION IS THE DELIVERABLE HERE, not the question. The ophthalmology
masters got away with distractor notes like "Both are painless." -- true, and
useless to someone who picked it. So the contract below is enforced rather than
intended:

  * four options, all distinct
  * every explanation at least MIN_EXPL characters, so a one-clause dismissal
    cannot pass
  * the key's explanation opens "Correct" and states the MECHANISM, not a
    restatement of the option
  * each distractor explanation is unique, and must not be built out of the
    vacuous phrases in BANNED -- "not correct", "this is wrong", "does not
    apply" and friends
  * a distractor explanation has to mention something the option does not
    already say, checked crudely by requiring it to be meaningfully longer than
    the option text it explains

The vignette style follows Jaxon's examples: a case paragraph with age and
relevant history, then a lead-in that varies -- what finding is expected, what
is the most likely cause, what is the most direct method, what is the next
step, what additional finding is likely -- rather than "most likely diagnosis"
forty times.
"""
import re

LEADS = ("diagnosis", "finding", "cause", "next step", "treatment", "testing", "mechanism")

MIN_EXPL = 90          # characters; a real reason does not fit in less
MIN_KEY_EXPL = 120     # the key gets the mechanism, so it is held higher

BANNED = re.compile(
    r"(?i)\b("
    r"not correct|this is wrong|is incorrect|does not apply|not applicable|"
    r"not the answer|wrong answer|not right|incorrect because|"
    r"not this one|nope|obviously"
    r")\b")

# A distractor note that only restates the option teaches nothing.
def _adds_something(option, expl):
    o = set(re.findall(r"[a-z]{4,}", option.lower()))
    e = set(re.findall(r"[a-z]{4,}", expl.lower()))
    return len(e - o) >= 6


def Q(topic, io, q, opts, lead, deck, slide, c=0):
    assert len(opts) == 4, "four options, got %d: %s" % (len(opts), q[:60])
    assert lead in LEADS, "unknown lead-in %r" % lead
    assert len({o[0].strip().lower() for o in opts}) == 4, "duplicate option: %s" % q[:60]
    assert len({o[1].strip() for o in opts}) == 4, "two options share an explanation: %s" % q[:60]

    key = opts[c]
    assert re.match(r"correct\b", key[1], re.I), \
        "the key's explanation must open 'Correct': %s" % q[:60]
    assert len(key[1]) >= MIN_KEY_EXPL, \
        "key explanation is %d chars, needs %d -- give the mechanism: %s" \
        % (len(key[1]), MIN_KEY_EXPL, q[:60])

    for i, o in enumerate(opts):
        if i == c:
            continue
        assert not re.match(r"correct\b", o[1], re.I), \
            "distractor explanation opens with 'Correct': %s" % o[0]
        assert len(o[1]) >= MIN_EXPL, \
            "explanation for %r is %d chars, needs %d" % (o[0][:40], len(o[1]), MIN_EXPL)
        assert not BANNED.search(o[1]), \
            "vacuous phrasing in the explanation for %r: %s" % (o[0][:40], o[1][:70])
        assert _adds_something(o[0], o[1]), \
            "explanation for %r only restates the option" % o[0][:40]

    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c,
            "lead": lead, "deck": deck, "cite": "%s, Slide %d" % (deck, slide)}
