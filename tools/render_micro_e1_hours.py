#!/usr/bin/env python3
"""Render the hours-weighted Microbiology Exam 1 quiz from its pool.

Sized to the timetable rather than the objective list: the exam is 65 questions
and the course allots five per scheduled lecture hour, so each lecture carries
its own contact time. Topics inside a lecture are chosen by what the lecturer
actually spent minutes on, measured from the recordings. See the pool's
docstring for the two emphases deliberately not followed.
"""
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

spec = importlib.util.spec_from_file_location(
    "pool", os.path.join(HERE, "micro_e1_hours_pool.py"))
pool = importlib.util.module_from_spec(spec); spec.loader.exec_module(pool)
QS = pool.POOL

# Microbiology green -- the palette already used by every Exam 1 quiz.
PAL = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 1")

INTRO = (
  "<p>Sixty-five questions, split the way the exam is: five per scheduled lecture "
  "hour, so the two three-hour lectures &mdash; Microbe-Human Interactions and "
  "Specific Immunity &mdash; carry fourteen each and together make up "
  "<strong>43% of the paper</strong>, while each two-hour lecture carries nine or ten.</p>"
  "<p>Which topics come up inside each lecture is set by what the lecturer actually "
  "spent time on, measured from the recordings: resistance dominates Lecture 2, water "
  "and food dominate Lecture 4, and antibodies and antigens dominate Lecture 6. "
  "Transmission is the best return on your time &mdash; three objectives carrying "
  "nine questions.</p>")

html = R.render(
    title="Microbiology Exam 1 — Timetable-Weighted Quiz",
    h1="Microbiology Exam 1 &mdash; Timetable-Weighted",
    sub="Microbiology &middot; Exam 1 &middot; Lectures 1&ndash;6 &middot; five questions per lecture hour",
    pill="%d questions" % len(QS),
    chips=["General Microbiology", "Antibiotics &amp; Resistance", "Microbe-Human Interactions",
           "Transmission", "Nonspecific Defenses", "Specific Immunity"],
    intro=INTRO, questions=QS, already_converted=True, **PAL)

path = os.path.join(OUT, "micro-exam-1-timetable-weighted-quiz.html")
open(path, "w", encoding="utf-8").write(html)
print("wrote %s — %d questions" % (os.path.basename(path), len(QS)))
