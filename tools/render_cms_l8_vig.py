#!/usr/bin/env python3
"""Render CMS I Lecture 8 Set 2 — the two Pigmented Skin Lesions vignette quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l8_set2.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Clinical vignettes", "Diagnosis", "Next step", "Testing", "Patient education"]
INTRO = ("Thirty clinical vignettes on pigmented skin lesions. Each case carries a presentation, the "
         "clues that narrow it &mdash; age, skin type, site, how the lesion behaves with the seasons "
         "&mdash; and the defining feature it turns on. The lead-in varies deliberately: some ask for "
         "the diagnosis, others for the next step, the treatment, the test, or what you would tell the "
         "patient. Several cases hinge on the pairs this deck most invites confusion between: ephelides "
         "against lentigines by whether they fade when the sun goes, lentigo simplex against solar "
         "lentigo by border and size, dermatosis papulosa nigrans against small seborrheic keratoses, "
         "and blue against pigmented spindle cell and Spitz naevi by colour, site and age. Every "
         "question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "pigmented-skin-lesions-vignettes.html" if n == 1 else "pigmented-skin-lesions-vignettes-version-2.html"
    html = render(title=f"Pigmented Skin Lesions Vignettes {n} &mdash; CMS I Exam 1",
                  h1="Pigmented Skin Lesions &mdash; Vignettes",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 8 &middot; Vignette set",
                  pill="30 vignettes", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
