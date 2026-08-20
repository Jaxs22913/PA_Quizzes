#!/usr/bin/env python3
"""Render CMS I Lecture 6 Set 1 — the two objective-style quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
S = json.load(open(os.path.join(HERE, "cms_l6_set1.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Antifungal classes", "Tinea by body site", "Onychomycosis",
         "Candidiasis &amp; versicolor", "Varicella &amp; zoster", "Herpes simplex, molluscum, warts"]
INTRO = ("Thirty questions on cutaneous viral and fungal infections, drawn from the syllabus "
         "instructional objectives. Covers the allylamine and azole antifungal classes and how they "
         "differ, every tinea by body site, onychomycosis, the id reaction and tinea incognito, "
         "candidal intertrigo and pityriasis versicolor, then varicella, herpes zoster with "
         "postherpetic neuralgia, zoster ophthalmicus and Ramsay Hunt syndrome, herpes simplex and "
         "herpetic whitlow, molluscum contagiosum and warts. "
         "<b>Where the lecture audio and the slide disagree on a fact, the slide wins</b> &mdash; "
         "every question here is grounded in the PowerPoint. "
         "This is the objective-style set; the vignettes are separate. Every question cites its slide.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = ("cutaneous-viral-and-fungal-infections-quiz.html" if n == 1
          else "cutaneous-viral-and-fungal-infections-quiz-version-2.html")
    html = render(title=f"Cutaneous Viral and Fungal Infections Quiz {n} &mdash; CMS I Exam 1",
                  h1="Cutaneous Viral and Fungal Infections",
                  sub="Clinical Medicine and Surgery I &middot; Exam 1 &middot; Lecture 6 &middot; Objective set",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
