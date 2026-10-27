#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Microbiology Exam 3 cram sheet (Lectures 14-19; Lecture 14 so far).

Condensed ONLY from the Exam 3 study guide (tools/micro_e3/_micro_e3_guide_lN.py), which is itself built from the
decks, in the shape of tools/build_micro_e2_cram.py. Each lecture is a JSON fragment, tools/micro_e3/lN_cram.json
({id, label, color, rows}). Rows marked with a star carry emphasis: for Lecture 14 so far only the slide's own
asterisks, until the recording has been read (the audio pass rewrites the "What the Slides Flag" topic).
Add a fragment per later Exam 3 lecture as it lands.

    python3 tools/build_micro_e3_cram.py
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

OUT = os.path.join(ROOT, "Microbiology Exam 3", "micro-exam-3-cram-sheet.html")
FRAGMENTS = ["l14_cram.json"]

topics = []
for frag in FRAGMENTS:
    topics += json.load(io.open(os.path.join(HERE, "micro_e3", frag), encoding="utf-8"))
ids = [t["id"] for t in topics]
assert len(ids) == len(set(ids)), "duplicate topic id"

html = render(
    title="Cram Sheet — Microbiology Exam 3",
    kicker="Microbiology · Exam 3 · Class of 2028",
    h1="Microbiology Exam 3 Cram Sheet",
    sub="Lecture 14 so far — Gram-Negative Bacilli of Medical Importance (the Exam 3 block is Lectures 14–19). ★ = emphasized on the slides. Exam 3 is Wednesday 2 December 2026.",
    topics=topics,
    guide_href="micro-exam-3-study-guide.html",
    footer_note="Condensed from the Microbiology Exam 3 Study Guide (Class of 2028). For the full explanation and figures behind any of these, see the full guide.",
)
io.open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.relpath(OUT, ROOT), len(html) // 1024,
      len(topics), sum(len(t["rows"]) for t in topics)))
