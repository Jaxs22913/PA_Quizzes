#!/usr/bin/env python3
"""Render the two PDM I Lecture 9 (Cardiac Biomarkers and Lipid Testing) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pdm_l9_sets.json"), encoding="utf-8"))
# The exam's palette, copied from its sibling render_pdm_l8.py rather than invented.
PALETTE = dict(navy="#2f5d50", indigo="#4e8a76", gold="#b8862f", ice="#eef5f1")
CHIPS = ["Troponin", "High-sensitivity troponin", "Creatine kinase", "Natriuretic peptides",
         "C-reactive protein", "Lipoproteins", "Lipoprotein(a)", "Reading a lipid panel",
         "Risk assessment"]
INTRO = (
  "Thirty questions on the two halves of this topic, and the line between them: "
  "<b>cardiac biomarkers answer &ldquo;is there acute cardiac injury or stress?&rdquo;</b> and "
  "<b>lipids answer &ldquo;what is this patient&rsquo;s long-term atherosclerotic risk?&rdquo;</b> "
  "Troponin is the marker of choice for injury, and serial values separate injury from infarction. "
  "B-type natriuretic peptide reflects stretch, not injury. Creatine kinase is for skeletal muscle. "
  "High-sensitivity C-reactive protein refines risk and never diagnoses an acute event. On the lipid "
  "side: which components are measured and which calculated, what the apolipoprotein B particles do "
  "to the artery wall, why lipoprotein(a) is measured once, and how a risk estimate is built. "
  "<b>Every laboratory value comes with the scale that reads it</b> &mdash; you are never asked to "
  "recall a reference range. The only arithmetic is non-HDL (non-high-density lipoprotein) cholesterol and the Friedewald estimate, "
  "the two calculations the material itself asks for."
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "cardiac-biomarkers-lipids-quiz.html" if n == 1 else "cardiac-biomarkers-lipids-quiz-version-2.html"
    html = render(
        title="Cardiac Biomarkers &amp; Lipids Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Cardiac Biomarkers &amp; Lipid Testing",
        sub="Principles of Diagnostic Medicine I &middot; Exam 2 &middot; Lecture 9",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-50s %d questions" % (fn, len(qs)))
