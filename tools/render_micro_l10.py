#!/usr/bin/env python3
"""Render Microbiology Exam 2, Lecture 10 — Gram-Positive Bacilli of Medical Importance.

Palette and header shape inherited from Lectures 7 and 8 so the class reads as
one. Picture questions point at micro-exam-2-quiz-images/l10-*.jpg, cropped from
the deck's own slides (labels that named the answer were cropped away).
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Microbiology Exam 2")
PALETTE = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Spore-formers", "Anthrax", "Gas gangrene", "Tetanus &amp; botulism",
         "Clostridioides difficile", "Listeria", "Diphtheria", "Cutibacterium",
         "Tuberculosis", "Leprosy", "Actinomyces &amp; Nocardia"]
INTRO = ("Lecture 10 of Microbiology &mdash; Gram-Positive Bacilli of Medical Importance. Thirty "
         "questions, every one cited to the slide it came from, a few of them read from the "
         "slide&rsquo;s own photographs. "
         "<b>Two questions sort the whole lecture.</b> Does it form endospores? If so it is "
         "<i>Bacillus</i> (aerobic, catalase positive; <i>Bacillus anthracis</i> has a <i>central</i> "
         "spore) or <i>Clostridium</i> (anaerobic, catalase negative; <i>Clostridium tetani</i> has a "
         "<i>terminal</i> spore). If not, is it regular (stains evenly: "
         "<i>Lactobacillus</i>, <i>Listeria</i>) or irregular (pleomorphic: <i>Corynebacterium</i>, "
         "<i>Cutibacterium</i>, the acid-fast mycobacteria, and the filamentous <i>Actinomyces</i> and "
         "<i>Nocardia</i>)? "
         "<b>Know what is most common and what is deadliest.</b> Cutaneous anthrax is the commonest "
         "form and pulmonary the deadliest; infant botulism is the commonest botulism; "
         "<i>Clostridium perfringens</i> is the commonest cause of gas gangrene, helped by a mixed "
         "infection whose aerobes use up the oxygen. "
         "<b>Keep the two neurotoxins apart:</b> tetanospasmin blocks the inhibitory transmitters, so "
         "muscles contract uncontrollably; botulinum toxin blocks acetylcholine, so paralysis is "
         "flaccid and descending. "
         "No question asks for a percentage or for which antibiotic to give. "
         "Covers the scheme for Gram-positive bacilli; <i>Bacillus anthracis</i> and the forms of "
         "anthrax; <i>Bacillus cereus</i>; gas gangrene, tetanus, botulism and clostridial food "
         "poisoning; <i>Clostridioides difficile</i>; <i>Lactobacillus</i> and <i>Listeria</i>; "
         "diphtheria; <i>Cutibacterium acnes</i>; tuberculosis and its tests; leprosy; and "
         "actinomycosis and nocardiosis.")

sets = json.load(io.open(os.path.join(HERE, "micro_l10_sets.json"), encoding="utf-8"))
for n, key, fname in ((1, "set1", "gram-positive-bacilli-quiz.html"),
                      (2, "set2", "gram-positive-bacilli-quiz-version-2.html")):
    html = render(
        title="Gram-Positive Bacilli &mdash; Quiz %d" % n,
        h1="Gram-Positive Bacilli of Medical Importance",
        sub="Microbiology &middot; Exam 2 &middot; Lecture 10 &middot; Set %d" % n,
        pill="30 questions", chips=CHIPS, intro=INTRO,
        questions=sets[key], already_converted=True, **PALETTE)
    for q in sets[key]:
        if q.get("img"):
            assert os.path.exists(os.path.join(OUT, q["img"])), q["img"]
    os.makedirs(OUT, exist_ok=True)
    io.open(os.path.join(OUT, fname), "w", encoding="utf-8").write(html)
    print("wrote %s  (%d KB, %d picture questions)"
          % (fname, len(html) // 1024, sum(1 for q in sets[key] if q.get("img"))))
