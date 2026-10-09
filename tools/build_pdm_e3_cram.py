#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Principles of Diagnostic Medicine I, Exam 3 cram sheet.

Condensed from the Exam 3 study guide and nothing else, per cram_sheets_feature:
the topic rows are written by the per-lecture builders in
tools/pdm_e3/l<N>_cram.json, each condensed from that lecture's guide fragment.
This script opens with one "How this exam is written" topic, keeps only the
lecture-specific rows of the per-lecture scope topics (the general ones are
merged into the opener), and evens the topic colours onto the Exam 3 palette.
Lectures 11-16; no lab content (Jaxon, 2026-10-08: "Lectures only").
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render  # noqa: E402

OUT = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3/pdm-exam-3-cram-sheet.html")
FRAG = os.path.join(HERE, "pdm_e3")
# Charcoal, ECG red, dark gold, wine: every one carries white header text.
CYCLE = ["#33363d", "#b23a48", "#8a6420", "#7a2e3b"]

SCOPE = {"id": "scope", "label": "How This Exam Is Written", "color": "#33363d", "rows": [
    ["Reference ranges are GIVEN", "“I'm not going to just throw a random number at you” — a rate, an interval or a potassium in a stem comes with the range that reads it."],
    ["★ Name the rhythm", "Rhythm naming is fair game, and most questions show the strip or the 12-lead with the vignette. Read every strip the same five ways: rate, regularity, P waves, PR interval, QRS."],
    ["Next-best-test", "Often another lead: posterior leads V7–V9 for isolated ST depression in V1–V4; V4R for an inferior infarction with hypotension."],
    ["No treatment", "Lecture 12 is “solely about rhythm interpretation and diagnosis”; Lecture 11 leaves treatment out too. Know what the tracing shows and means."],
]}
# Rows of the per-lecture scope topics already said by the opener.
MERGED = {"Name the rhythm", "Values come with ranges", "Strips first"}


def main():
    topics = [SCOPE]
    for n in range(11, 17):
        for t in json.load(open(os.path.join(FRAG, "l%d_cram.json" % n), encoding="utf-8")):
            t = dict(t)
            if t["id"].endswith("-scope"):
                t["rows"] = [r for r in t["rows"] if r[0] not in MERGED]
                assert t["rows"], t["id"]
            topics.append(t)
    for i, t in enumerate(topics[1:]):
        t["color"] = CYCLE[i % len(CYCLE)]
    ids = [t["id"] for t in topics]
    assert len(ids) == len(set(ids)), "duplicate topic ids"
    for t in topics:
        for r in t["rows"]:
            assert len(r) == 2 and all(x.strip() for x in r), (t["id"], r)

    html = render(
        title="Cram Sheet — Principles of Diagnostic Medicine I Exam 3",
        kicker="Principles of Diagnostic Medicine I Exam 3 · Class of 2028",
        h1="Principles of Diagnostic Medicine I Exam 3 Cram Sheet",
        sub="Lectures 11 to 16, the electrocardiography block. Rhythm analysis and the sinus rhythms; premature beats, escape rhythms and the supraventricular dysrhythmias; the ventricular rhythms and the atrioventricular blocks; axis, bundle branch blocks and chamber enlargement; ischemia, injury and infarction; pericarditis, electrolytes, drug effects and special patterns. Opens with how the exam is written.",
        topics=topics,
        guide_href="pdm-exam-3-study-guide.html",
        footer_note="Condensed from the Principles of Diagnostic Medicine I Exam 3 Study Guide (Class of 2028). Covers Lectures 11–16 (lecture content). Emphasis rows quote the 5, 6 and 7 October 2026 recordings; ★ = emphasized in a recording.",
    )
    assert not re.search(r"(?i)ha[e]m|o[e]dem|tumo[u]r|colo[u]r|cent[r]e|ana[e]m|o[e]soph", html)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.basename(OUT), len(html) // 1024,
          len(topics), sum(len(t["rows"]) for t in topics)))


if __name__ == "__main__":
    main()
