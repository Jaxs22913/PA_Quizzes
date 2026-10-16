#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Microbiology Exam 2 Master Exams: five cumulative forms of 60 (Lectures 7-13).

The questions come from tools/micro_e2_masters_partition.py (Microbiology Exam 2/master-exams.json); this
only renders them with the class palette (Lectures 7-13 share it). Pattern: tools/render_micro_masters.py.
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render

D = "Microbiology Exam 2"
OUT = os.path.join(os.path.dirname(HERE), D)
S = json.load(io.open(os.path.join(OUT, "master-exams.json"), encoding="utf-8"))
PAL = dict(navy="#1f4d2b", indigo="#3f8a55", gold="#c2903a", ice="#e8f4ea")
CHIPS = ["Disorders in immunity", "Diagnosing infections", "Cocci", "Gram-positive bacilli",
         "Novel antimicrobial therapy", "Epidemiology", "Miscellaneous bacterial agents"]
INTRO = ("Sixty questions drawn from all seven lectures of the Exam 2 block, in proportion to class time "
         "rather than at random. <b>Every lecture had two hours on the timetable, so each one gives eight or "
         "nine questions to every form</b>; which four lectures get the ninth question rotates from form to "
         "form. <b>Every form also carries at least one question on each item Dr. Webster put at "
         "&ldquo;know cold&rdquo; in her Exam 2 review</b>: the four types of hypersensitivity, allergy, "
         "ABO and Rh, primary versus secondary immunodeficiency and immunotherapy; <i>Bacillus anthracis</i>, "
         "where the spore sits, <i>Clostridium perfringens</i>, <i>Clostridium botulinum</i>, "
         "<i>Clostridioides difficile</i>, <i>Listeria</i>, diphtheria and leprosy; and descriptive versus "
         "analytic studies, the history of epidemiology, morbidity and mortality, association versus "
         "causation, and endemic, epidemic and herd immunity. Her &ldquo;know it&rdquo; material fills the "
         "rest of her lectures, and Dr. Fair&rsquo;s four lectures are weighted by time alone. "
         "<b>No question appears in more than one form</b>, so the five forms give you 300 distinct "
         "questions. Most are the topic quizzes&rsquo; questions word for word; a few come from the same "
         "question pools and appear only here. Every question cites its slide.")

for name in ("A", "B", "C", "D", "E"):
    fn = "micro-exam-2-master-exam-form-%s.html" % name.lower()
    for q in S[name]:
        if q.get("img"):
            assert os.path.exists(os.path.join(OUT, q["img"])), q["img"]
    html = render(title="Microbiology Exam 2 Master Exam &mdash; Form %s" % name,
                  h1="Microbiology &mdash; Comprehensive Master Exam",
                  sub="Exam 2 &middot; Lectures 7&ndash;13 &middot; Form %s" % name,
                  pill="60 questions", chips=CHIPS, intro=INTRO,
                  questions=S[name], already_converted=True, **PAL)
    io.open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-46s %d questions, %d pictures" % (fn, len(S[name]), sum(1 for q in S[name] if q.get("img"))))
