#!/usr/bin/env python3
"""Render Microbiology Exam 3, Lecture 14 — Gram-Negative Bacilli of Medical Importance (Dr. Webster).

Palette and header shape inherited from the Exam 1 and Exam 2 quizzes so the class reads as one (the homepage spine
tells the exams apart; tools/build_exam_spines.py OVERRIDES). Set 1 is text-only (it stays in Group Study); Set 2
carries the picture questions, whose crops tools/extract_micro_l14_quiz_images.py writes into
micro-exam-3-quiz-images/ under numbered names.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 3")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Endotoxin", "Sorting the rods", "<i>Pseudomonas</i> &amp; relatives", "<i>Brucella</i> &amp; <i>Francisella</i>",
         "Pertussis", "<i>Legionella</i>", "Enteric media &amp; antigens", "<i>Escherichia coli</i> pathotypes",
         "Other coliforms", "<i>Proteus</i>", "<i>Salmonella</i> &amp; typhoid", "<i>Shigella</i>", "Plague",
         "<i>Pasteurella</i> &amp; <i>Haemophilus</i>"]

sets = json.load(io.open(os.path.join(HERE, "micro_l14_sets.json"), encoding="utf-8"))
# `mis` (the misconception each distractor stands for) is review metadata for tools/blind_review.py;
# it stays in the sets file and never reaches the page.
sets = {k: [{f: v for f, v in q.items() if f != "mis"} for q in qs] for k, qs in sets.items()}
sys.path.insert(0, HERE)
from micro_l14_intro import INTRO
os.makedirs(OUT, exist_ok=True)
for n, key, fname in ((1, "set1", "gram-negative-bacilli-quiz.html"),
                      (2, "set2", "gram-negative-bacilli-quiz-version-2.html")):
    html = render(
        title="Gram-Negative Bacilli &mdash; Quiz %d" % n,
        h1="Gram-Negative Bacilli of Medical Importance",
        sub="Microbiology &middot; Exam 3 &middot; Lecture 14 &middot; Set %d" % n,
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=sets[key], already_converted=True, **PALETTE)
    for q in sets[key]:
        if q.get("img"):
            assert os.path.exists(os.path.join(OUT, q["img"])), q["img"]
    io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB, %d picture questions)"
          % (fname, len(html) // 1024, sum(1 for q in sets[key] if q.get("img"))))
