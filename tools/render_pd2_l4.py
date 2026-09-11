#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the two Physical Diagnosis 2 Lecture 4 (ENT) quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1")
S = json.load(open(os.path.join(HERE, "pd2_l4_sets.json"), encoding="utf-8"))
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["Ear history &amp; exam", "Vertigo comparison", "Tuning forks",
         "Nose &amp; sinuses", "Oral cavity", "Neck, thyroid &amp; head"]
INTRO = ("Thirty questions on the advanced ENT history and examination. Covers the ear history "
         "and referred otalgia, otoscopy and insufflation, the otoscopic findings, the peripheral "
         "and central vertigo comparison, hearing screening, the nose and sinuses, the oral "
         "cavity, and the neck, thyroid and head. "
         "<b>The tuning fork block carries extra weight and it was said out loud.</b> The video "
         "played in class put it plainly: <i>&ldquo;the Weber and the Rinne tests are both high "
         "yield &hellip; the difference between sensorineural hearing loss and conductive hearing "
         "loss is also high yield &hellip; it will be three points on test day.&rdquo;</i> Both "
         "forms carry it, and the two mnemonics taught aloud are here as mnemonics: "
         "<b>Rinne is under the pinna</b> (on the mastoid, below the ear), and <b>Weber tells you "
         "whether</b> it is the right or the left. "
         "<b>Centor is on both forms too.</b> It has its own slide here, and the Clinical "
         "Medicine lecture the same week asked for it by name &mdash; two courses wanting the "
         "same four criteria is about as clear a signal as this material gives. "
         "<b>One gap is worth naming rather than hiding.</b> The deck declares several Bates "
         "tables and the reading assignments testable. Those are a textbook, not a slide, so "
         "nothing here is invented from them &mdash; every question comes from the deck or the "
         "recording. Where the deck reproduces a Bates table on its own slide, as it does for the "
         "vertigo comparison and the hearing loss summary, that content <i>is</i> covered. "
         "This is a physical diagnosis course, so the questions ask what you find and what "
         "finding it means &mdash; the mechanism behind these conditions belongs to Clinical "
         "Pathophysiology and their management to Clinical Medicine and Surgery.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "ent-exam-quiz.html" if n == 1 else "ent-exam-quiz-version-2.html"
    html = render(title="Advanced ENT History &amp; Examination Quiz %d &mdash; PD2 Exam 1" % n,
                  h1="Advanced ENT History and Examination &mdash; Quiz %d" % n,
                  sub="Physical Diagnosis 2 &middot; Exam 1 &middot; Lecture 4",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-34s %d questions" % (fn, len(S[key])))
