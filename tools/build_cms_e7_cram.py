#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 7 cram sheet (Respiratory Block Exam II, Lectures 39-45).

    python3 tools/build_cms_e7_cram.py

Condensed from the Exam 7 study guide, per the cram template README: compress what the guide already says, keep
numbers and names verbatim, add nothing new. Exam 7 is built a lecture or two at a time by more than one
builder, so each lecture's topics live in their own module, tools/cms_e7_cram/lNN.py, which defines
TOPICS = [{"id": "lNN-...", "label": ..., "color": "#rrggbb", "rows": [[label, html], ...]}, ...].
This script concatenates whichever modules exist, in lecture order. A lecture's emphasis card goes first in
its own module, gold (#b8860b) with a star, as on the Exam 6 sheet. See tools/cms_e7_README.md.

2026-10-30 (Jaxon's standing rule, memory cram_criteria_tables): a lecture module may also define
CRITERIA = [...], one `cols` table per criteria set, score, classification, staging or cut-off table on its
slides, each with a labeled memory aid ("mnemonic"), ids "crit-lNN-...". All lectures' CRITERIA go at the TOP
of the sheet, in lecture order, under one table-of-contents chip (the first carries "toc_label", the rest
"toc": False), as on the Exam 5 sheet. Cells are the slide wording; slide conflicts are {"note": ...} rows.

2026-10-31: a lecture module may also define FOCUS = [...], ids "focus-lNN": the lecturer's own study-focus slide
condensed to one `cols` table. All FOCUS tables go above the criteria, under one "Study Focus" chip.
"""
import importlib.util, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

NAMES = {39: "phases of sleep", 40: "obstructive sleep apnea and obesity hypoventilation syndrome",
         41: "inflammatory lung diseases", 42: "pulmonary vascular disease", 43: "pulmonary nodules and neoplasms",
         44: "pleural disorders", 45: "acid-base part II"}
topics, criteria, focus, have = [], [], [], []
for n in range(39, 46):
    p = os.path.join(HERE, "cms_e7_cram", "l%d.py" % n)
    if not os.path.exists(p):
        continue
    spec = importlib.util.spec_from_file_location("cms_e7_cram_l%d" % n, p)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for t in m.TOPICS:
        assert t["id"].startswith("l%d-" % n), "%s: topic id %r must start with l%d-" % (p, t["id"], n)
    for t in getattr(m, "CRITERIA", []):
        assert t["id"].startswith("crit-l%d-" % n), "%s: criteria id %r must start with crit-l%d-" % (p, t["id"], n)
        assert t.get("cols") and t.get("mnemonic"), "%s: criteria table %r needs cols and a mnemonic" % (p, t["id"])
    for t in getattr(m, "FOCUS", []):
        assert t["id"].startswith("focus-l%d" % n), "%s: focus id %r must start with focus-l%d" % (p, t["id"], n)
    criteria += list(getattr(m, "CRITERIA", []))
    focus += list(getattr(m, "FOCUS", []))
    topics += m.TOPICS; have.append(n)
assert topics, "no lecture modules in tools/cms_e7_cram/"
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
# A lecturer's study-focus slide (Exam 6 precedent: L37 slide 127, L38 slide 41) goes above everything, one TOC chip.
for i, t in enumerate(focus):
    if i == 0:
        t.pop("toc", None)
        t["toc_label"] = "Study Focus (Lectures %s)" % "&ndash;".join(
            str(int(x["id"][7:9])) for x in (focus[0], focus[-1])) if len(focus) > 1 else "Study Focus"
    else:
        t["toc"] = False
        t.pop("toc_label", None)
topics = focus + criteria + topics
ids = [t["id"] for t in topics]
assert len(ids) == len(set(ids)), "duplicate topic ids"

covered = ", ".join("%d (%s)" % (n, NAMES.get(n, "")) if NAMES.get(n) else str(n) for n in have)
html = render(
    primary="#b8860b",   # the sheet keeps its gold (the first emphasis card) when criteria tables go on top
    title="Cram Sheet — CMS I Exam 7",
    kicker="Clinical Medicine and Surgery I · Exam 7 · Class of 2028",
    h1="CMS I Exam 7 Cram Sheet",
    sub=("<b>The study focus the lecturer posted comes first</b>, then " if focus else "") +
        (("<b>criteria, scores and classifications</b>" if focus else "<b>Criteria, scores and classifications first</b>") + ": one table per set from the slides, each with "
         "a labeled memory aid. " if criteria else "") +
        "Respiratory Block Exam II, condensed from the Exam 7 study guide. Lectures covered: %s. "
        "Each lecture opens with a gold card of what its lecturer stressed (starred; from the recording once it is in); every "
        "fact still comes from the slides." % covered,
    topics=topics,
    guide_href="cms-exam-7-study-guide.html",
    footer_note="Condensed from the CMS I Exam 7 Study Guide (Class of 2028). "
                "For the full explanation behind any of these, see the full guide.",
)
out = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-exam-7-cram-sheet.html")
open(out, "w", encoding="utf-8").write(html)
print("wrote", os.path.basename(out), len(html), "bytes,",
      sum(len(t["rows"]) for t in topics), "rows across", len(topics), "topics,", len(focus), "focus tables,",
      len(criteria), "criteria tables, lectures", have)
