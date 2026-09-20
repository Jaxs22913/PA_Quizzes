#!/usr/bin/env python3
"""Render Microbiology Exam 2, Lecture 8 — Diagnosing Infections."""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Phenotypic", "Genotypic", "Immunological", "Culture media",
         "Sensitivity testing", "Blots &amp; immunoassays"]
INTRO = ("Lecture 8 of Microbiology &mdash; Diagnosing Infections. Thirty questions, every one "
         "cited to the slide it came from. "
         "<b>One split organises the whole lecture.</b> Every identification method is "
         "phenotypic (what you can observe), genotypic (the genetic makeup) or immunological "
         "(antibody against antigen) &mdash; and most questions here can be answered by asking "
         "which of the three a technique belongs to. Phenotypic methods need the organism grown "
         "first, which is why they are slower; genotypic ones usually need no culture at all, "
         "which is what makes them valuable for slow growers like <i>Mycobacterium</i> and "
         "awkward ones like <i>Legionella</i>; immunological methods may or may not need culture. "
         "<b>Two things are easy to get backwards.</b> Larger zones of inhibition mean a MORE "
         "effective drug. And in complement fixation, lysed red cells are a NEGATIVE result "
         "&mdash; fixed complement cannot lyse them, so no haemolysis means the serum is "
         "positive. "
         "<b>The blots are worth learning as a set</b>: Southern for DNA (the original, Edwin "
         "Southern, ~1975), Northern for RNA and gene expression (~1977), Western for proteins "
         "(~1981), Eastern for post-translational products (~1982). "
         "Covers specimen collection and handling; microscopic and macroscopic morphology; the "
         "biochemical tests and the differential media that report them; Kirby-Bauer and minimum "
         "inhibitory concentration; nucleic acid analysis through RFLP, the polymerase chain "
         "reaction and ribosomal gene sequencing; serology, agglutination and precipitation; the "
         "blots; complement fixation; fluorescent antibody; the immunoassays; and in vivo testing.")

sets = json.load(io.open(os.path.join(HERE, "micro_l8_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "diagnosing-infections-quiz.html"),
                      (2, "set2", "diagnosing-infections-quiz-version-2.html")):
    html = render(
        title="Diagnosing Infections &mdash; Quiz %d" % n,
        h1="Diagnosing Infections",
        sub="Microbiology &middot; Exam 2 &middot; Lecture 8 &middot; Set %d" % n,
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=sets[key], already_converted=True, **PALETTE)
    os.makedirs(OUT, exist_ok=True)
    io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB)" % (fname, len(html) // 1024))
