#!/usr/bin/env python3
"""Render the two PDM I Lecture 7 (Electrocardiography) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pdm_l7_sets.json"), encoding="utf-8"))
# The PDM palette, taken from render_pdm_l6.py rather than invented.
PALETTE = dict(navy="#2f5d50", indigo="#4e8a76", gold="#b8862f", ice="#eef5f1")
CHIPS = ["Cell properties", "Action potential", "Conduction system",
         "Leads &amp; vectors", "Paper &amp; deflections", "Waves &amp; intervals", "Rate"]
INTRO = (
  "Thirty questions on the electrocardiogram from first principles: what the cardiac cell does, "
  "how the impulse travels, what the leads are actually measuring, and what every wave, segment "
  "and interval on the tracing represents. "
  "<b>The five phases do not run in numerical order</b> &mdash; rest is phase four, and the "
  "upstroke that follows it is phase zero &mdash; which is why they are asked as a sequence "
  "rather than as a list. The same logic runs through the conduction system: each pacemaker has "
  "its own intrinsic rate, so a rate in the forties with no sinus activity tells you which one "
  "has taken over. "
  "<b>Numbers are part of this lecture, unlike the rest of the course.</b> The objectives say to "
  "determine heart rate and to measure and interpret the intervals, so the figures are the "
  "material. What the questions do is give you what you would actually have in front of you "
  "&mdash; the strip, the count, the interval in small boxes &mdash; and ask what follows from "
  "it. Eight complexes in six seconds is a rate; seven small boxes of PR is a prolonged interval. "
  "<b>One thing worth carrying out of here:</b> an electrocardiogram cannot tell you whether your "
  "patient has a pulse. It shows electrical activity, and electrical activity without a pulse is "
  "a real and lethal state. "
  "<b>Built from the slides</b>, with the recording queued behind the exams that come sooner; "
  "every question cites the slide it came from."
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "electrocardiography-quiz.html" if n == 1 else "electrocardiography-quiz-version-2.html"
    html = render(
        title="Electrocardiography Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Principles of Electrocardiography",
        sub="Principles of Diagnostic Medicine I &middot; Exam 2 &middot; Lecture 7",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-42s %d questions" % (fn, len(qs)))
