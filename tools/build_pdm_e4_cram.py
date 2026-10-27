#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Principles of Diagnostic Medicine I, Exam 4 cram sheet.

Condensed from the Exam 4 study guide and nothing else, per cram_sheets_feature: the topic rows are
written by the per-lecture builders in tools/pdm_e4/l<N>_cram.json, each condensed from that
lecture's guide fragment. This script opens with one "How this exam is written" topic and evens the
topic colours onto the Exam 4 palette. Lectures 17-21 as they arrive (lecture content only).
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render  # noqa: E402

OUT = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4/pdm-exam-4-cram-sheet.html")
FRAG = os.path.join(HERE, "pdm_e4")
# Slate, x-ray blue, dark amber, deep teal: every one carries white header text.
CYCLE = ["#26384a", "#3a6797", "#8a5a1c", "#2f5d62"]

SCOPE = {"id": "scope", "label": "How This Exam Is Written", "color": "#26384a", "rows": [
    ["Reference ranges are GIVEN", "“I'm not going to just throw a random number at you” — a creatinine or any value in a stem comes with the range that reads it."],
    ["Tests over diagnoses", "“More related to the tests themselves”: which study, why, its cautions, and what normal looks like on it."],
    ["Next-best-test", "In imaging it is a study: radiograph first; angiogram first for a suspected pulmonary embolism; computed tomography when the radiograph is inconclusive; ventilation/perfusion when contrast can't be given."],
    ["Images in play", "Expect a film or a slice with the vignette. Technique first, then structures, then the pattern."],
]}


def main():
    topics = [SCOPE]
    lectures = []
    for n in range(17, 22):
        p = os.path.join(FRAG, "l%d_cram.json" % n)
        if not os.path.exists(p):
            continue
        lectures.append(n)
        topics += [dict(t) for t in json.load(open(p, encoding="utf-8"))]
    assert lectures, "no lecture rows"
    for i, t in enumerate(topics[1:]):
        t["color"] = CYCLE[i % len(CYCLE)]
    ids = [t["id"] for t in topics]
    assert len(ids) == len(set(ids)), "duplicate topic ids"
    for t in topics:
        for r in t["rows"]:
            assert len(r) == 2 and all(x.strip() for x in r), (t["id"], r)

    html = render(
        title="Cram Sheet — Principles of Diagnostic Medicine I Exam 4",
        kicker="Principles of Diagnostic Medicine I Exam 4 · Class of 2028",
        h1="Principles of Diagnostic Medicine I Exam 4 Cram Sheet",
        sub="Lectures 17 to 21, the pulmonary block, built lecture by lecture. So far: pulmonary imaging (the landmarks, the normal film, the upper airway films, technique, choosing the study and its cautions, reading computed tomography, and the five patterns) and pulmonary function testing (the equipment, the volumes and capacities, spirometry, indications, obstruction against restriction, reading a report, each test's role, and oxygenation). Opens with how the exam is written.",
        topics=topics,
        guide_href="pdm-exam-4-study-guide.html",
        footer_note="Condensed from the Principles of Diagnostic Medicine I Exam 4 Study Guide (Class of 2028). Covers Lecture%s %s so far (lecture content). Emphasis rows quote the 20 and 26 October 2026 recordings; ★ = emphasized in a recording." % ("s" if len(lectures) > 1 else "", ", ".join(map(str, lectures))),
    )
    assert not re.search(r"(?i)ha[e]m|(?<!angi)o[e]dem|tumo[u]r|colo[u]r|cent[r]e|ana[e]m|o[e]soph", html)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.basename(OUT), len(html) // 1024,
          len(topics), sum(len(t["rows"]) for t in topics)))


if __name__ == "__main__":
    main()
