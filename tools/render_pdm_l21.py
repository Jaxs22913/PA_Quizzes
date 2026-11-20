#!/usr/bin/env python3
"""Render the two PDM I Lecture 21 (Transfusion Medicine and Blood Banking Fundamentals) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 4")
SETS = json.load(open(os.path.join(HERE, "pdm_l21_sets.json"), encoding="utf-8"))
# One palette for the whole of Exam 4, kept in tools/pdm_e4/palette.json.
_P = json.load(open(os.path.join(HERE, "pdm_e4", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Pre-transfusion safety", "ABO antigens and antibodies", "Compatibility", "Emergency release", "Rh factor",
         "Hemolytic disease of the newborn", "ABO typing", "Antibody screen", "Crossmatch", "Antiglobulin tests",
         "Ordering and specimens", "Reaction protocol", "Acute hemolytic", "Delayed hemolytic",
         "Febrile non-hemolytic", "Allergic", "Anaphylactic"]
INTRO = (
  "Thirty questions on <b>transfusion medicine and blood banking</b>. Know why pre-transfusion testing and the "
  "bedside check matter, the ABO antigens and antibodies and the red cell and plasma compatibility rules "
  "(they run in opposite directions), the RhD antigen and hemolytic disease of the fetus and newborn, how to read "
  "forward and reverse typing, the antibody screen, the three crossmatch tiers, the direct against the indirect "
  "antiglobulin test, type and screen against type and crossmatch with the 3-day specimen rule, and the "
  "laboratory fingerprint of each of the five transfusion reactions. <b>Any lab value in a question comes with "
  "its normal range.</b>"
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "transfusion-medicine-blood-bank-quiz.html" if n == 1 else "transfusion-medicine-blood-bank-quiz-version-2.html"
    html = render(
        title="Transfusion Medicine and Blood Banking Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Transfusion Medicine and Blood Banking Fundamentals",
        sub="Principles of Diagnostic Medicine I &middot; Exam 4 &middot; Lecture 21",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-55s %d questions" % (fn, len(qs)))
