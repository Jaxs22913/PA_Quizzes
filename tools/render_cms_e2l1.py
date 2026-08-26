#!/usr/bin/env python3
"""Render the four CMS I Exam 2 Lecture 1 quizzes -- two objective sets and
two vignette sets, as [[cms_exam_spec]] requires for every CMS topic."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2")
os.makedirs(OUT, exist_ok=True)
S = json.load(open(os.path.join(HERE, "cms_e2l1_sets.json"), encoding="utf-8"))
V = json.load(open(os.path.join(HERE, "cms_e2l1_vig_sets.json"), encoding="utf-8"))

# Exam 2 gets its own palette. Exam 1's dermatology quizzes are TEAL
# (#17494b), so a teal here would be near-indistinguishable at a glance and the
# two blocks would blur together in the quiz list. Indigo instead.
PAL = dict(navy="#2d3f7a", indigo="#5566b5", gold="#c08a2e", ice="#eef0fa")

CHIPS = ["Eyelid &amp; lacrimal", "Conjunctiva &amp; surface", "Sclera, cornea &amp; uvea",
         "Cellulitis", "Diagnostics", "Red eye triage"]

INTRO_BASE = (
  "Common ophthalmological disorders &mdash; the first lecture of Exam 2. Covers the eyelid and "
  "lacrimal conditions, the whole conjunctivitis family including chlamydial disease and "
  "trachoma, episcleritis against scleritis, keratitis and corneal ulcer, herpetic eye disease, "
  "anterior and posterior uveitis, pre-septal against post-septal cellulitis, the diagnostic "
  "modalities, and the red-eye triage framework. "
  "<b>This is the management half.</b> Clinical Pathophysiology I Lecture 4 covers almost this "
  "exact condition list from the mechanism side; this one asks what it looks like, what to order, "
  "what to give and when to refer. "
  "<b>Where the speaker notes soften a slide, the notes win.</b> Imaging is not automatic for "
  "dacryoadenitis, dacryocystitis or clearly pre-septal cellulitis, and haematology referral is "
  "not automatic for a recurrent subconjunctival haemorrhage &mdash; the slides read as though "
  "they are, and the notes on the same slides say otherwise. Every question cites its slide.")

INTRO_1 = ("Thirty questions on the instructional objectives. " + INTRO_BASE)
INTRO_2 = ("Thirty clinical vignettes. Professor Jaquith described her exam as "
           "<i>&ldquo;pretty much all clinical vignettes &hellip; recognize conditions by the "
           "vignette&rdquo;</i>, with <i>&ldquo;SOME diagnosis but A LOT are next management "
           "plan, first line treatment, patient education&rdquo;</i> &mdash; so diagnosis "
           "lead-ins are deliberately capped at a fifth of each set and the rest ask what to do "
           "next. <b>Named findings carry their description in brackets</b>, so a term like "
           "ciliary flush is never the only handle on the finding. "
           "<b>Every stem stands on its own</b> &mdash; no question refers to another, because "
           "the question order is shuffled. " + INTRO_BASE)

JOBS = [
 ("ophthalmology-i-quiz.html", 1, S["set1"], INTRO_1, "Quiz 1", "30 questions"),
 ("ophthalmology-i-quiz-version-2.html", 2, S["set2"], INTRO_1, "Quiz 2", "30 questions"),
 ("ophthalmology-i-vignettes.html", 1, V["set1"], INTRO_2, "Vignettes 1", "30 vignettes"),
 ("ophthalmology-i-vignettes-version-2.html", 2, V["set2"], INTRO_2, "Vignettes 2", "30 vignettes"),
]

for fn, n, qs, intro, label, pill in JOBS:
    html = render(
        title=f"Common Ophthalmological Disorders {label} &mdash; CMS I Exam 2",
        h1=f"Common Ophthalmological Disorders &mdash; {label}",
        sub="Clinical Medicine and Surgery I &middot; Exam 2 &middot; Lecture 1",
        pill=pill, chips=CHIPS, intro=intro,
        questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(qs))
