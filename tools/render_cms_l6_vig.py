#!/usr/bin/env python3
"""Render CMS I Lecture 6 Set 2 — the two vignette quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l6_set2.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Tinea by site", "Nail &amp; fold disease", "Varicella &amp; zoster",
         "Herpes simplex", "Molluscum &amp; warts"]
INTRO = ("Thirty patient vignettes on cutaneous viral and fungal infections. Each one gives you a "
         "presentation and asks for the diagnosis, the next step, the test, the treatment or the "
         "counselling point &mdash; and the lead-in decides the answer, so read it before you read "
         "the choices. The wrong options are the neighbouring condition in the same differential or "
         "the right condition at the wrong phase, not obviously absurd. "
         "<b>Where the lecture audio and the slide disagree on a fact, the slide wins.</b> "
         "This is the vignette set; the objective questions are separate. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = ("cutaneous-viral-and-fungal-infections-vignettes.html" if n == 1
          else "cutaneous-viral-and-fungal-infections-vignettes-version-2.html")
    html = render(title=f"Cutaneous Viral and Fungal Infections Vignettes {n} &mdash; CMS I Exam 1",
                  h1="Cutaneous Viral and Fungal Infections",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 6 &middot; Vignettes",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
