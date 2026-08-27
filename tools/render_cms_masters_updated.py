#!/usr/bin/env python3
"""Render the five UPDATED CMS I Exam 1 Master Exams -- 65 five-option questions each.

Separate from render_cms_masters.py, which renders the original 60-question
four-option forms built by reusing topic-quiz questions. These are newly written
items in the reference-question style Jaxon supplied on 2026-08-26: five options
A-E, a per-option refutation, and a slide citation on every question.
"""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
D = "Clinical Medicine and Surgery I Exam 1"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(open(os.path.join(OUT, "master-exams-updated.json"), encoding="utf-8"))
PAL = dict(navy="#17494b", indigo="#3f7d7a", gold="#c08a2e", ice="#eef5f4")
CHIPS = ["Clinical reasoning", "General Derm I", "Derm II", "Bacterial", "Infestations",
         "Viral &amp; fungal", "Benign lesions", "Pigmented lesions", "Pre-malignant &amp; malignant"]
INTRO = ("Sixty-five newly written questions drawn from every lecture in the Exam 1 dermatology "
         "block, in exam proportions rather than at random &mdash; each of the nine lectures "
         "contributes to every form, so this is a genuine cumulative rehearsal and not a sample of "
         "whichever topic had the most questions written for it. <b>Five options, A&ndash;E</b>, and "
         "every wrong choice gets its own explanation saying why it is wrong rather than a shared "
         "note. <b>No question appears in more than one form</b>, so working through all five gives "
         "you 325 distinct questions. Every question cites the slide it came from.")
for name in ("A", "B", "C", "D", "E"):
    fn = "cms-exam-1-master-exam-updated-form-%s.html" % name.lower()
    html = render(title=f"CMS I Exam 1 Master Exam (Updated) &mdash; Form {name}",
                  h1="Clinical Medicine and Surgery I &mdash; Comprehensive Master Exam (Updated)",
                  sub=f"Exam 1 &middot; Dermatology block, Lectures 1&ndash;9 &middot; Form {name}",
                  pill="65 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[name]))
