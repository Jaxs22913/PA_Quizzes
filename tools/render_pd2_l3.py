#!/usr/bin/env python3
"""Render the two Physical Diagnosis 2 Lecture 3 quizzes."""
import sys, os, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
from render import render
OUT = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1")
S = json.load(open(os.path.join(HERE, "pd2_l3_sets.json"), encoding="utf-8"))
PAL = dict(navy="#3a5a40", indigo="#5f8a68", gold="#c08a2e", ice="#eef4ef")
CHIPS = ["History &amp; symptoms", "Inspection", "The red-eye chart",
         "Acuity &amp; fields", "Pupils", "Fundoscopy &amp; trauma"]
INTRO = ("Thirty questions on the advanced ocular history and examination. Covers the four-part "
         "symptom history, the acute-versus-gradual and painful-versus-painless patterns, the "
         "common mistakes, the suggested order of the examination, inspection of the lids and "
         "conjunctiva, visual acuity and the pinhole test, confrontation fields, ocular motility, "
         "the pupils and the swinging light test, fundoscopy, ocular trauma, and referral timing. "
         "<b>Built from the 26 August recording, not the deck alone.</b> Professor Beck removes "
         "slides from scope out loud, and the deck cannot say which ones &mdash; so this was held "
         "until the audio existed. Six things she excluded are absent here, each because she said "
         "so: the named virus in viral conjunctivitis, the exophthalmometer technique and its "
         "measurement, the strabismus diagram (<i>&ldquo;just a visual &hellip; you don&rsquo;t "
         "have to memorize&rdquo;</i>), the corneal reflection test (<i>&ldquo;we already did "
         "that in PD1&rdquo;</i>), the Adie&rsquo;s pupil look-alike associations "
         "(<i>&ldquo;it&rsquo;s not on my test this time&rdquo;</i>), and the Latin expansions of "
         "OD, OS and OU. <b>Adie&rsquo;s pupil itself is in</b> &mdash; <i>&ldquo;you should know "
         "Adie&rsquo;s pupil, that could be on my test&rdquo;</i> &mdash; and so are the "
         "abbreviations themselves, which she called <i>&ldquo;terms that you must "
         "remember&rdquo;</i>. "
         "<b>The red-eye comparison chart gets its own questions</b>, because she singled it out: "
         "<i>&ldquo;I genuinely think it&rsquo;s important that you are very familiar with that "
         "chart.&rdquo;</i> That slide extracts as completely blank &mdash; it is a picture of "
         "the table &mdash; so its content was recovered by optical character recognition and is "
         "marked image-only in the citations. Every question cites its slide, or the recording.")
for n, key in ((1, "set1"), (2, "set2")):
    fn = "ocular-exam-quiz.html" if n == 1 else "ocular-exam-quiz-version-2.html"
    html = render(title=f"Advanced Ocular History &amp; Examination Quiz {n} &mdash; PD2 Exam 1",
                  h1=f"Advanced Ocular Medical History and Examination &mdash; Quiz {n}",
                  sub="Physical Diagnosis 2 &middot; Exam 1 &middot; Lecture 3",
                  pill="30 questions", chips=CHIPS, intro=INTRO,
                  questions=S[key], already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote", fn, "(%d questions)" % len(S[key]))
