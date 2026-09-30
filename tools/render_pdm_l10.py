#!/usr/bin/env python3
"""Render the two PDM I Lecture 10 (Coagulation and Hemostasis Testing) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 2")
SETS = json.load(open(os.path.join(HERE, "pdm_l10_sets.json"), encoding="utf-8"))
# The exam's palette, copied from its sibling render_pdm_l8.py rather than invented.
PALETTE = dict(navy="#2f5d50", indigo="#4e8a76", gold="#b8862f", ice="#eef5f1")
CHIPS = ["Hemostasis vocabulary", "Platelet count and function", "Bleeding time", "von Willebrand studies",
         "Prothrombin time", "International normalized ratio", "Activated partial thromboplastin time",
         "Thrombin time and fibrinogen", "Mixing studies", "D-dimer", "Pattern recognition",
         "Bleeding versus thrombotic workups"]
INTRO = (
  "Thirty questions on <b>testing the balance between clot formation and clot breakdown</b>. "
  "Platelets make the plug (primary hemostasis), coagulation factors make the fibrin (secondary "
  "hemostasis) and plasmin takes the clot apart (fibrinolysis), and each laboratory test evaluates one "
  "of these. Expect the platelet count and function tests, the prothrombin time, the international "
  "normalized ratio, the activated partial thromboplastin time, thrombin time and fibrinogen, mixing "
  "studies, D-dimer, the patterns that tie the results together (disseminated intravascular "
  "coagulation, liver disease, vitamin K antagonists, heparin, hemophilia, von Willebrand disease) "
  "and the difference between a bleeding workup and a thrombotic workup. "
  "<b>Every laboratory value comes with the scale that reads it</b> &mdash; you are never asked to "
  "recall a reference range, and <b>nothing in this topic is calculated</b>."
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "coagulation-hemostasis-quiz.html" if n == 1 else "coagulation-hemostasis-quiz-version-2.html"
    html = render(
        title="Coagulation &amp; Hemostasis Testing Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Coagulation &amp; Hemostasis Testing",
        sub="Principles of Diagnostic Medicine I &middot; Exam 2 &middot; Lecture 10",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-50s %d questions" % (fn, len(qs)))
