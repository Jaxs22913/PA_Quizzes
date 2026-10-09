#!/usr/bin/env python3
"""Render Microbiology Exam 2, Lecture 9 — Cocci of Medical Importance.

Palette and header shape inherited from Lectures 7 and 8 so the exam reads as one. Set 2 carries
the picture questions (Gram stains, blood agar, a skin photograph); Set 1 is text only, which
keeps it in Group Study.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Staphylococci", "Coagulase-negative staph", "Streptococci", "Hemolysis",
         "Group A &amp; B", "Viridans &amp; pneumococcus", "Neisseria", "Moraxella &amp; Acinetobacter"]
INTRO = ("Lecture 9 of Microbiology &mdash; Cocci of Medical Importance. Thirty questions, every one "
         "cited to the slide it came from. "
         "<b>Two bench tests sort the Gram-positive cocci before anything else.</b> Staphylococci grow in "
         "irregular clusters and are <i>catalase positive</i>; streptococci grow in chains and are "
         "<i>catalase negative</i>. Among the staphylococci, <i>coagulase</i> separates "
         "<i>Staphylococcus aureus</i> from the coagulase-negative species. Among the streptococci, "
         "hemolysis on blood agar comes next: beta is complete (a clear zone), alpha is partial (green, "
         "hence <i>viridans</i>). Bacitracin then picks out group A among the beta-hemolytic streptococci, "
         "and optochin picks out <i>Streptococcus pneumoniae</i> among the alpha-hemolytic ones. "
         "<b>Lancefield groups A and B are the two to know.</b> Group A, <i>Streptococcus pyogenes</i>, "
         "is strictly human, resists phagocytosis through M-protein, and leaves rheumatic fever and "
         "glomerulonephritis behind; group B, <i>Streptococcus agalactiae</i>, reaches the newborn during "
         "vaginal delivery, which is why pregnant women are screened. "
         "<b>The Gram-negative cocci are Neisseria</b>: bean-shaped diplococci, strict human parasites "
         "grown on chocolate agar in a carbon dioxide-enriched candle jar. The gonococcus is presumed "
         "from diplococci inside neutrophils; the meningococcus spreads in close quarters and kills "
         "through endotoxin. Covers every organism on the syllabus list, from <i>Staphylococcus "
         "hominis</i> to <i>Acinetobacter baumannii</i>.")

sets = json.load(io.open(os.path.join(HERE, "micro_l9_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "cocci-of-medical-importance-quiz.html"),
                      (2, "set2", "cocci-of-medical-importance-quiz-version-2.html")):
    intro = INTRO + (" <b>This set includes picture questions</b>: Gram stains, blood agar plates "
                     "and a skin photograph, each with its labels removed." if n == 2 else "")
    html = render(
        title="Cocci of Medical Importance &mdash; Quiz %d" % n,
        h1="Cocci of Medical Importance",
        sub="Microbiology &middot; Exam 2 &middot; Lecture 9 &middot; Set %d" % n,
        pill="30 questions", chips=CHIPS, intro=intro,
        questions=sets[key], already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB)" % (fname, len(html) // 1024))
