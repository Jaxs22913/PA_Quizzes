#!/usr/bin/env python3
"""Render CMS I Lecture 4 Set 2 — the two Cutaneous Bacterial Infections vignette quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l4_set2.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Clinical vignettes", "Diagnosis", "Next step", "Testing", "Patient education"]
INTRO = ("Thirty clinical vignettes on cutaneous bacterial infections. Each case carries a presentation, "
         "the clues that narrow it &mdash; age, exposure, occupation, comorbidity &mdash; and the "
         "defining feature it turns on. The lead-in varies deliberately: some ask for the diagnosis, "
         "others for the next step, the treatment, the test, or what you would tell the patient. Read "
         "the lead-in carefully; recognising the organism and answering the question are two separate "
         "acts. Several cases hinge on discriminations this lecture makes explicitly &mdash; erysipelas "
         "against cellulitis by the border, furuncle against abscess by origin, acute against chronic "
         "paronychia by timescale, and cellulitis against necrotizing fasciitis by pain out of "
         "proportion to examination. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "cutaneous-bacterial-infections-vignettes.html" if n == 1 else "cutaneous-bacterial-infections-vignettes-version-2.html"
    html = render(title=f"Cutaneous Bacterial Infections Vignettes {n} &mdash; CMS I Exam 1",
                  h1="Cutaneous Bacterial Infections &mdash; Vignettes",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 4 &middot; Vignette set",
                  pill="30 vignettes", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
