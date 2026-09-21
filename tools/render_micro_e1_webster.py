#!/usr/bin/env python3
"""Render the Webster-style Microbiology Exam 1 quiz from its pool.

One paper spanning all six Exam 1 lectures, weighted by her own review: her
"know cold" objectives carry the most questions and her two explicit skips
one each, while the three lectures she did not review are weighted evenly
rather than lightly.

Every stem asks exactly ONE thing. Her spoken style stacks several demands
in a breath, and an earlier version of this copied that into the stems --
which tests three things at once and tells a student nothing about which
part they missed. The stacked items are split instead, which is why this is
longer than the objective count alone would need.

The `io` groupings match her review headings for Lectures 1, 2 and 5, so the
results breakdown lines up with the review page.
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
  "<p>Every question asks one thing. The mix follows the in-class review &mdash; the "
  "objectives graded <em>know cold</em> carry the most questions here, and the two "
  "explicit skips carry one each &mdash; and the groupings match that review's "
  "headings, so the score breakdown at the end tells you which objective to go back to.</p>"
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
