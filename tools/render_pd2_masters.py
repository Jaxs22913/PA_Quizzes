#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the PD2 Exam 1 Master Exams -- five cumulative forms.

The forms are not all the same length. Forms B and C hold 60 questions; forms
A, D and E hold 59, because on 2026-09-22 Jaxon removed (without replacing)
three Lecture 1 course-mechanics questions, one from each of those forms. So
the pill, the intro's question count, the per-lecture shares and the
"distinct questions" total are all COMPUTED from each form's contents here,
never typed in. Each question's lecture is read from the deck its `cite`
names; a question citing an unknown source stops the render.
"""
import sys, os, json
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Physical Diagnosis 2 Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["Clinical reasoning &amp; documentation", "Dermatology",
         "Advanced ocular exam", "Advanced ENT exam"]

# cite prefix -> lecture
DECKS = [("Intro to PD II - Elwaya", "cr"), ("PD II Derm - Beck", "derm"),
         ("PD II Advanced Exam Ocular Lecture - Beck", "ocular"), ("PD II ENT 2026", "ent")]


def lecture(q):
    hits = [lec for prefix, lec in DECKS if q.get("cite", "").startswith(prefix)]
    assert len(hits) == 1, "cannot tell which lecture this cite belongs to: %r" % q.get("cite")
    return hits[0]


WORDS = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven",
         8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
         14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen",
         19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty"}


def words(n):
    if n in WORDS:
        return WORDS[n]
    assert 20 < n < 70, n
    return "%s-%s" % (WORDS[n - n % 10], WORDS[n % 10])


def share_sentence(n):
    """The three big lectures, then clinical reasoning, from the form's own counts."""
    big = [("Dermatology", n["derm"]), ("ocular", n["ocular"]), ("ENT", n["ent"])]
    if len({v for _, v in big}) == 1:
        s = "Dermatology, ocular and ENT contribute %s questions each" % words(big[0][1])
    else:
        s = "Dermatology contributes %s, ocular %s and ENT %s" % tuple(words(v) for _, v in big)
    return s + "; clinical reasoning contributes %s" % words(n["cr"])


TOTAL = sum(len(v) for v in S.values())
ALL_STEMS = [q["q"] for v in S.values() for q in v]
assert len(set(ALL_STEMS)) == TOTAL, "a question appears in more than one form"


def intro(form):
    n = Counter(lecture(q) for q in form)
    cr = words(n["cr"])
    return (
        "%s questions drawn from every lecture in the Exam 1 block, in proportion rather than "
        "at random. <b>%s</b> &mdash; that lecture is a 24-page introduction, much of "
        "it course mechanics, which the house rule keeps out of questions, so %s is an honest "
        "share rather than a shortfall. "
        "<b>No question appears in more than one form</b>, so working through all five gives you "
        "%d distinct questions. These are drawn from the full authored pools, not just the two "
        "topic quizzes per lecture &mdash; over half the written material never reaches a topic "
        "quiz, and this is where it goes. "
        "<b>This is a physical diagnosis course</b>, so the questions ask what you find and what "
        "finding it means; the mechanism behind these conditions belongs to Clinical "
        "Pathophysiology and their management to Clinical Medicine and Surgery. The tuning fork "
        "block carries extra weight throughout, because the class was told it is worth three "
        "points on test day. Every question cites its slide."
        % (words(len(form)).capitalize(), share_sentence(n), cr, TOTAL))


for name in ("A", "B", "C", "D", "E"):
    fn = "pd2-exam-1-master-exam-form-%s.html" % name.lower()
    html = render(title="PD2 Exam 1 Master Exam &mdash; Form %s" % name,
                  h1="Physical Diagnosis 2 &mdash; Comprehensive Master Exam",
                  sub="Exam 1 &middot; Lectures 1&ndash;4 &middot; Form %s" % name,
                  pill="%d questions" % len(S[name]), chips=CHIPS, intro=intro(S[name]),
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-42s %d questions" % (fn, len(S[name])))
