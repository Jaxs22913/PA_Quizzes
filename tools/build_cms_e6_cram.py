#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 6 cram sheet (Respiratory Block Exam I, Lectures 33-38).

    python3 tools/build_cms_e6_cram.py

Condensed from the Exam 6 study guide, per the cram template README: compress what the guide already says, keep
numbers and names verbatim, add nothing new. Exam 6 is built a lecture or two at a time by more than one
builder, so each lecture's topics live in their own module, tools/cms_e6_cram/lNN.py, which defines
TOPICS = [{"id": "lNN-...", "label": ..., "color": "#rrggbb", "rows": [[label, html], ...]}, ...].
This script concatenates whichever modules exist, in lecture order. A lecture's emphasis card goes first in
its own module, gold (#b8860b) with a star, as on the Exam 5 sheet. See tools/cms_e6_README.md.

2026-10-30 (Jaxon's standing rule, memory cram_criteria_tables): a lecture module may also define
CRITERIA = [...], one `cols` table per criteria set, score, classification, staging or cut-off table on its
slides, each with a labeled memory aid ("mnemonic"), ids "crit-lNN-...". All lectures' CRITERIA go at the TOP
of the sheet, in lecture order, under one table-of-contents chip (the first carries "toc_label", the rest
"toc": False), as on the Exam 5 sheet. Cells are the slide wording; slide conflicts are {"note": ...} rows.
"""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

NAMES = {33: "oxygen delivery", 34: "acid-base part I", 35: "asthma", 36: "chronic obstructive pulmonary disease",
         37: "respiratory infections and vaccines", 38: "mycobacterial infections including tuberculosis"}
topics, criteria, have = [], [], []
for n in range(33, 39):
    p = os.path.join(HERE, "cms_e6_cram", "l%d.py" % n)
    if not os.path.exists(p):
        continue
    spec = importlib.util.spec_from_file_location("cms_e6_cram_l%d" % n, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for t in m.TOPICS:
        assert t["id"].startswith("l%d-" % n), "%s: topic id %r must start with l%d-" % (p, t["id"], n)
    for t in getattr(m, "CRITERIA", []):
        assert t["id"].startswith("crit-l%d-" % n), "%s: criteria id %r must start with crit-l%d-" % (p, t["id"], n)
        assert t.get("cols") and t.get("mnemonic"), "%s: criteria table %r needs cols and a mnemonic" % (p, t["id"])
    criteria += list(getattr(m, "CRITERIA", []))
    topics += m.TOPICS; have.append(n)
assert topics, "no lecture modules in tools/cms_e6_cram/"
# One TOC chip for the whole run of criteria tables; narrow tables (3 columns or fewer) fit a 390 px phone.
for i, t in enumerate(criteria):
    if i == 0:
        t.pop("toc", None)
        t["toc_label"] = "Criteria &amp; Scores (Lectures %d&ndash;%d)" % (have[0], have[-1])
    else:
        t["toc"] = False
        t.pop("toc_label", None)
    if len(t["cols"]) <= 3:
        t.setdefault("min_width", "0")
topics = criteria + topics
ids = [t["id"] for t in topics]
assert len(ids) == len(set(ids)), "duplicate topic ids"

covered = ", ".join("%d (%s)" % (n, NAMES.get(n, "")) if NAMES.get(n) else str(n) for n in have)
html = render(
    primary="#b8860b",   # the sheet keeps its gold (the first emphasis card) when criteria tables go on top
    title="Cram Sheet — CMS I Exam 6",
    kicker="Clinical Medicine and Surgery I · Exam 6 · Class of 2028",
    h1="CMS I Exam 6 Cram Sheet",
    sub=("<b>Criteria, scores and classifications come first</b>: one table per set from the slides, each with "
         "a labeled memory aid. " if criteria else "") +
        "Respiratory Block Exam I, condensed from the Exam 6 study guide. Lectures covered: %s. "
        "Each lecture opens with a gold card of what its lecturer stressed on the recording (starred); every "
        "fact still comes from the slides." % covered,
    topics=topics,
    guide_href="cms-exam-6-study-guide.html",
    footer_note="Condensed from the CMS I Exam 6 Study Guide (Class of 2028). "
                "For the full explanation behind any of these, see the full guide.",
)
out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6", "cms-exam-6-cram-sheet.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", os.path.basename(out), len(html), "bytes,",
      sum(len(t["rows"]) for t in topics), "rows across", len(topics), "topics,", len(criteria),
      "criteria tables, lectures", have)
