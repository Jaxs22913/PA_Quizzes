#!/usr/bin/env python3
"""Render Microbiology Exam 3, Lecture 15 (Dr. Fair), from tools/micro_l15_sets.json.

Palette and header shape as Lecture 14 (tools/render_micro_l14.py) so the exam reads as one. Set 1 is text-only
(it stays in Group Study); Set 2 carries the picture questions (tools/extract_micro_l15_l16_quiz_images.py).
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 3")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["True vs opportunistic", "Thermal dimorphism", "Priority list", "Portals &amp; levels", "Diagnosis",
         "Amphotericin B", "<i>Histoplasma</i>", "<i>Coccidioides</i>", "<i>Blastomyces</i>",
         "<i>Paracoccidioides</i>", "<i>Sporothrix</i>", "Tinea (the Latin names)", "Superficial mycoses",
         "<i>Candida</i>", "<i>Cryptococcus</i>", "<i>Pneumocystis</i>", "<i>Aspergillus</i>", "Mucormycosis",
         "Mycotoxins"]
TITLE, H1, FILES = "Fungi of Medical Importance", "Fungi of Medical Importance", (
    "fungi-of-medical-importance-quiz.html", "fungi-of-medical-importance-quiz-version-2.html")
LECTURE = 15

sets = json.load(io.open(os.path.join(HERE, "micro_l15_sets.json"), encoding="utf-8"))
# `mis` (each distractor's misconception) and `ordered` (numeric options, never rotated) are pipeline metadata;
# they stay in the sets file and never reach the page.
sets = {k: [{f: v for f, v in q.items() if f not in ("mis", "ordered")} for q in qs] for k, qs in sets.items()}
sys.path.insert(0, HERE)
from micro_l15_intro import INTRO
os.makedirs(OUT, exist_ok=True)
for n, key, fname in ((1, "set1", FILES[0]), (2, "set2", FILES[1])):
    html = render(
        title="%s &mdash; Quiz %d" % (TITLE, n),
        h1=H1,
        sub="Microbiology &middot; Exam 3 &middot; Lecture %d &middot; Set %d" % (LECTURE, n),
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=sets[key], already_converted=True, **PALETTE)
    for q in sets[key]:
        if q.get("img"):
            assert os.path.exists(os.path.join(OUT, q["img"])), q["img"]
    io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB, %d picture questions)"
          % (fname, len(html) // 1024, sum(1 for q in sets[key] if q.get("img"))))
