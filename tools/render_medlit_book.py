#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the Interpretation of Medical Literature "Book Questions" quizzes: one per textbook chapter.
Source: tools/medlit_book_sets.json (tools/build_medlit_book.py). Same engine and palette as the Exam 1 quizzes."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "quiz-template"))
import render as R

OUT = os.path.join(ROOT, "Interpretation of Medical Literature Book Questions")
PAL = dict(navy="#7a2d47", indigo="#b55575", gold="#c08a2e", ice="#faeff3")
CH = json.load(open(os.path.join(HERE, "medlit_book_sets.json"), encoding="utf-8"))


def slug(t):
    return re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")


for ch in CH:
    n = len(ch["questions"])
    fn = "chapter-%02d-%s-quiz.html" % (ch["n"], slug(ch["title"]))
    qs = [{k: v for k, v in q.items() if k != "num"} for q in ch["questions"]]
    figs = sum(1 for q in qs if q.get("img"))
    intro = ("Book questions for chapter %d, <b>%s</b>: %d questions from the course textbook, with the book's answer and "
             "explanation after each. The book explains only the correct answer, so every wrong choice shows that same "
             "explanation." % (ch["n"], ch["title"].replace("&", "&amp;"), n))
    html = R.render(title="Chapter %d: %s Quiz — Book Questions — Interpretation of Medical Literature" % (ch["n"], ch["title"]),
                    h1="Chapter %d &mdash; %s" % (ch["n"], ch["title"].replace("&", "&amp;")),
                    sub="Interpretation of Medical Literature &middot; Book Questions",
                    pill="%d questions" % n, chips=["Book questions", "Chapter %d" % ch["n"]] + (["Figures"] if figs else []),
                    intro=intro, questions=qs, already_converted=True, **PAL)
    open(os.path.join(OUT, fn), "w", encoding="utf-8").write(html)
    print("wrote %-52s %2d questions" % (fn, n))
