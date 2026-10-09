#!/usr/bin/env python3
"""Render the two PDM I Lecture 16 (Pericardial Disease, Electrolytes, Drug Effects, and Special ECG
Patterns) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 3")
SETS = json.load(open(os.path.join(HERE, "pdm_l16_sets.json"), encoding="utf-8"))
_P = json.load(open(os.path.join(HERE, "pdm_e3", "palette.json"), encoding="utf-8"))
PALETTE = {k: _P[k] for k in ("navy", "indigo", "gold", "ice")}
CHIPS = ["Pericarditis", "Early repolarization", "Lead V6 ratio", "Brugada syndrome",
         "Bundle branch block, pacing and Sgarbossa", "Hypothermia", "Wolff-Parkinson-White",
         "Reentrant tachycardias", "Potassium and calcium", "Thyroid", "Digoxin, amiodarone, tricyclics",
         "Pulmonary embolism"]
INTRO = (
  "Thirty questions on <b>the ST-elevation mimics and the special patterns</b>, and about half of them "
  "show you the tracing. Tell pericarditis (PR depression, global concave elevation, no reciprocal "
  "depression) from benign early repolarization (J-point notch, the lead V6 ratio) and from an "
  "infarction; recognize Brugada in V1 to V3, paced rhythms and Sgarbossa's criteria, Osborn waves, "
  "the Wolff-Parkinson-White triad and its reentrant tachycardias; and read potassium, calcium, "
  "thyroid, drug and pulmonary embolism changes. <b>Every laboratory value comes with its reference "
  "range.</b> Tap any tracing to enlarge it."
)

for n in (1, 2):
    qs = SETS["set%d" % n]
    fn = "pericarditis-electrolytes-drugs-quiz.html" if n == 1 else "pericarditis-electrolytes-drugs-quiz-version-2.html"
    html = render(
        title="Pericarditis, Electrolytes, Drugs &amp; Special Patterns Quiz %d &mdash; Principles of Diagnostic Medicine I" % n,
        h1="Pericarditis, Electrolytes, Drugs &amp; Special Patterns",
        sub="Principles of Diagnostic Medicine I &middot; Exam 3 &middot; Lecture 16",
        pill="%d questions" % len(qs), chips=CHIPS, intro=INTRO,
        questions=qs, already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-55s %d questions (%d with a tracing)" % (fn, len(qs), sum(1 for q in qs if q.get("img"))))
