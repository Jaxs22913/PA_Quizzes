#!/usr/bin/env python3
"""Render the Pharmacology I Lecture 3 quizzes.

Lecture 3 is split into two topics -- see pharm_l3_partition.py for why -- so
this renders whichever one it is given:

    python3 render_pharm_l3.py chol
    python3 render_pharm_l3.py adren

Palette inherited from the existing Pharmacology I Exam 1 quizzes.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

TOPIC = sys.argv[1] if len(sys.argv) > 1 else "chol"
OUT = os.path.join(ROOT, "Pharmacology I Exam 1")
PALETTE = dict(navy="#6b3524", indigo="#9c5230", gold="#c9a227", ice="#fbf1e6")

SPEC = {
 "chol": dict(
   sets="pharm_l3_chol_sets.json",
   files=["ans-cholinergic-quiz.html", "ans-cholinergic-quiz-version-2.html"],
   title="ANS and Cholinergic Drugs Quiz %d — Pharmacology I Exam 1",
   h1="ANS and Cholinergic Drugs &mdash; Quiz %d",
   chips=["ANS organisation", "Cholinergic receptors", "Cholinergic agonists",
          "Antimuscarinics", "Neuromuscular blockers"]),
 "adren": dict(
   sets="pharm_l3_adren_sets.json",
   files=["ans-adrenergic-quiz.html", "ans-adrenergic-quiz-version-2.html"],
   title="Adrenergic Drugs Quiz %d — Pharmacology I Exam 1",
   h1="Adrenergic Drugs &mdash; Quiz %d",
   chips=["Adrenergic receptors", "Catecholamines", "Direct agonists",
          "Alpha blockers", "Beta blockers"]),
}[TOPIC]

SUB = "Pharmacology I &middot; Exam 1 &middot; Lecture 3: Principles of Autonomic Nervous System Pharmacology"
SETS = json.load(open(os.path.join(HERE, SPEC["sets"]), encoding="utf-8"))

for n, (key, fname) in enumerate(zip(("set1", "set2"), SPEC["files"]), start=1):
    qs = SETS[key]
    html = R.render(title=SPEC["title"] % n, h1=SPEC["h1"] % n, sub=SUB,
                    pill="%d questions" % len(qs), chips=SPEC["chips"], intro="",
                    questions=qs, already_converted=True, **PALETTE)
    open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %-42s %d questions, %d KB" % (fname, len(qs), len(html) // 1024))
