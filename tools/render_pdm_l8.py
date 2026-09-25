#!/usr/bin/env python3
"""Render the two PDM I Lecture 8 (Cardiac Imaging) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pdm_l8_sets.json"), encoding="utf-8"))
# The PDM palette, taken from render_pdm_l6.py rather than invented.
PALETTE = dict(navy="#2f5d50", indigo="#4e8a76", gold="#b8862f", ice="#eef5f1")
CHIPS = ["Chest radiograph", "Vascular ultrasound", "Echocardiography",
         "Stress testing", "CT &amp; nuclear", "MRI", "Invasive studies"]
INTRO = (
  "Thirty questions on the cardiac imaging modalities, and the thread running through them is "
  "<b>which study answers which question</b>. Chest radiography is rarely the study you order "
  "and often the study you already have. Ultrasound shows anatomy and flow with no radiation but "
  "depends entirely on the operator. Echocardiography is the functional study; computed "
  "tomography is the anatomical one and explicitly <b>cannot assess function</b>. Nuclear "
  "perfusion imaging answers a question none of the others can &mdash; whether muscle is alive "
  "&mdash; and magnetic resonance avoids both radiation and iodinated contrast. Angiography is "
  "the gold standard, and the only one that can treat what it finds. "
  "<b>You are not asked to recall a threshold or to calculate anything.</b> The two figures that "
  "matter &mdash; the cardiothoracic ratio and the 85 percent of predicted maximum heart rate "
  "that makes a stress test valid &mdash; are supplied in the stem, and the question is what "
  "follows from them. A ratio you can recite but not apply to a film is worth nothing. "
  "<b>Built from the slides.</b> The recording for this lecture is queued behind the exams that "
  "come sooner, so every question cites the slide it came from and spoken emphasis will be "
  "layered in once the transcript lands."
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "cardiac-imaging-quiz.html" if n == 1 else "cardiac-imaging-quiz-version-2.html"
    html = render(
        title="Cardiac Imaging Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Cardiac Imaging &amp; Vascular Studies",
        sub="Principles of Diagnostic Medicine I &middot; Exam 2 &middot; Lecture 8",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-42s %d questions" % (fn, len(qs)))
