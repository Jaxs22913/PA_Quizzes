#!/usr/bin/env python3
"""Render CMS I Lecture 7 Set 2 — the two Benign Skin Lesions vignette quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l7_set2.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Clinical vignettes", "Diagnosis", "Next step", "Staging", "Patient education"]
INTRO = ("Thirty clinical vignettes on benign skin lesions. Each case carries a presentation and the "
         "one feature it turns on. The lead-in varies deliberately &mdash; some ask for the diagnosis, "
         "others for the next step, the treatment, the test, or what you would tell the patient. "
         "Several cases hinge on the pairs this lecture most invites confusion between: <b>keloid "
         "against hypertrophic scar</b> by whether it leaves the wound margin, <b>corn against callus "
         "against wart</b> by the skin lines and which direction of pressure hurts, <b>infantile "
         "hemangioma against nevus flammeus</b> by whether it involutes, and <b>sinus against "
         "fistula</b> by where the track ends. The pressure injury cases work through all six stages. "
         "Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "benign-skin-lesions-vignettes.html" if n == 1 else "benign-skin-lesions-vignettes-version-2.html"
    html = render(title=f"Benign Skin Lesions Vignettes {n} &mdash; CMS I Exam 1",
                  h1="Benign Skin Lesions &mdash; Vignettes",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 7 &middot; Vignette set",
                  pill="30 vignettes", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
