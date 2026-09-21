#!/usr/bin/env python3
"""Render the Webster-style Microbiology Exam 1 quiz from its pool.

One 60-question paper spanning all six Exam 1 lectures. The pool docstring
explains the two things the review supplies -- her weighting of the
objectives, and the four habits in how she asks -- and both are reflected
here: the question mix follows her tiers, and the `io` groupings match her
review headings for Lectures 1, 2 and 5 so the results breakdown lines up
with the review page.
"""
import importlib.util, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

spec = importlib.util.spec_from_file_location("pool", os.path.join(HERE, "micro_e1_webster_pool.py"))
pool = importlib.util.module_from_spec(spec); spec.loader.exec_module(pool)
QS = pool.POOL

# Microbiology green -- the palette already used by every Exam 1 quiz.
PAL = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 1")

INTRO = (
  "<p>Sixty questions across all six Exam 1 lectures, written in the shape the "
  "questions tend to take: several demands in one stem, reasoning forward from a "
  "structure to what follows from it, and mechanism rather than a list. The mix "
  "follows the in-class review &mdash; the objectives graded <em>know cold</em> carry "
  "the most questions here, and the two explicit skips carry one each.</p>"
  "<p>Lectures 3, 4 and 6 were not covered in that review. They are weighted evenly "
  "with the rest rather than lightly, because silence was not a de-emphasis. Both "
  "confirmed calculations &mdash; the therapeutic index and the decimal reduction "
  "&mdash; are included.</p>")

html = R.render(
    title="Microbiology Exam 1 — Exam-Style Review Quiz",
    h1="Microbiology Exam 1 &mdash; Exam-Style Review",
    sub="Microbiology &middot; Exam 1 &middot; Lectures 1&ndash;6 &middot; all six lectures",
    pill="%d questions" % len(QS),
    chips=["General Microbiology", "Antibiotics &amp; Resistance", "Microbe-Human Interactions",
           "Transmission", "Nonspecific Defenses", "Specific Immunity"],
    intro=INTRO, questions=QS, already_converted=True, **PAL)

path = os.path.join(OUT, "micro-exam-1-exam-style-quiz.html")
open(path, "w", encoding="utf-8").write(html)
print("wrote %s — %d questions" % (os.path.basename(path), len(QS)))
