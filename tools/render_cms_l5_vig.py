#!/usr/bin/env python3
"""Render CMS I Lecture 5 Set 2 — the two Dermatological Infestations vignette quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l5_set2.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Clinical vignettes", "Diagnosis", "Next step", "Testing", "Patient education"]
INTRO = ("Thirty clinical vignettes on dermatological infestations. Each case carries a presentation, "
         "the clues that narrow it &mdash; travel, geography, season, occupation, age &mdash; and the "
         "defining feature it turns on. The lead-in varies deliberately: some ask for the diagnosis, "
         "others for the next step, the treatment, the test, or what you would tell the patient. "
         "Geography does a lot of work in this lecture &mdash; the brown recluse in the Midwest and "
         "Southeast against the hobo spider in the Pacific Northwest, Lyme disease in the Northeast "
         "against Rocky Mountain spotted fever in the Southeast, tungiasis after tropical travel "
         "against cutaneous larva migrans from the same beach. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "dermatological-infestations-vignettes.html" if n == 1 else "dermatological-infestations-vignettes-version-2.html"
    html = render(title=f"Dermatological Infestations Vignettes {n} &mdash; CMS I Exam 1",
                  h1="Dermatological Infestations &mdash; Vignettes",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 5 &middot; Vignette set",
                  pill="30 vignettes", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
