#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Microbiology Exam 3 cram sheet (Lectures 14-19; Lectures 14-16 so far).

Condensed ONLY from the Exam 3 study guide (tools/micro_e3/_micro_e3_guide_lN.py), which is itself built from the
decks, in the shape of tools/build_micro_e2_cram.py. Each lecture is a JSON fragment, tools/micro_e3/lN_cram.json
({id, label, color, rows}). Rows marked with a star carry emphasis: for Lecture 14 the slide's own
asterisks plus what the recording stressed (audio pass, 27 October: the "What the Lecturer Flagged" topic).
Add a fragment per later Exam 3 lecture as it lands.

2026-10-30 (Lectures 15 and 16, Dr. Fair, slides phase): CRITERIA fragments (tools/micro_e3/lN_criteria.json) go
FIRST, one table per classification, comparison or cut-off set on the slides, each with a labeled memory aid that
maps one-to-one onto the table's rows (Jaxon's standing rule, memory cram_criteria_tables). They share one TOC chip
(the first carries "toc_label"). Every cell and every memory-aid key was checked against the slides by an
independent reader. Lecture 14's sheet predates the rule and has no criteria tables yet.

    python3 tools/build_micro_e3_cram.py
"""
import io, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

OUT = os.path.join(ROOT, "Microbiology Exam 3", "micro-exam-3-cram-sheet.html")
CRITERIA = ["l15_criteria.json", "l16_criteria.json"]
FRAGMENTS = ["l14_cram.json", "l15_cram.json", "l16_cram.json"]

topics = []
for frag in CRITERIA + FRAGMENTS:
    topics += json.load(io.open(os.path.join(HERE, "micro_e3", frag), encoding="utf-8"))
ids = [t["id"] for t in topics]
assert len(ids) == len(set(ids)), "duplicate topic id"

html = render(
    title="Cram Sheet — Microbiology Exam 3",
    kicker="Microbiology · Exam 3 · Class of 2028",
    h1="Microbiology Exam 3 Cram Sheet",
    primary="#1f4d2b",   # the sheet's colour before the criteria tables went on top
    sub="Lectures 14–16 so far — Gram-Negative Bacilli, Fungi of Medical Importance, Food Safety (the Exam 3 block is Lectures 14–19). <b>Tables and memory aids come first</b>: one per classification, comparison or cut-off set on the Lecture 15 and 16 slides. ★ = emphasized in the lecture recording or flagged on a slide. Exam 3 is Wednesday 2 December 2026.",
    topics=topics,
    guide_href="micro-exam-3-study-guide.html",
    footer_note="Condensed from the Microbiology Exam 3 Study Guide (Class of 2028). For the full explanation and figures behind any of these, see the full guide.",
)
io.open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.relpath(OUT, ROOT), len(html) // 1024,
      len(topics), sum(len(t["rows"]) for t in topics)))
