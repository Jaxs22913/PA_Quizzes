#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Splice the Session 7-10 sections into the Interpretation of Medical Literature study guide.

The six fragments live in tools/medlit_guide_s7_10/<key>.html (one <section class="deck"> each).
This inserts them before the Quick-Reference section, adds their contents entries, and updates the
"Covers N lecture decks" line. Idempotent: earlier insertions are removed first (they sit between
begin/end markers). Re-run tools/build_guide_links.py, dark_tokens.py and build_guide_docx.py after.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
GUIDE = os.path.join(ROOT, "Interpretation of Medical Literature Exam 1", "medical-literature-study-guide.html")
FRAG = os.path.join(HERE, "medlit_guide_s7_10")
ORDER = [("risk", "7", "Risk &amp; Ratios"), ("prognosis", "8", "Prognosis &amp; Outcomes"),
         ("prevention", "9", "Prevention &amp; Screening"), ("trials", "10", "Research &amp; Trials"),
         ("stats", "11", "Statistics, Correlation &amp; Causation"), ("reviews", "12", "Clinical Questions &amp; Reviews")]
B, E = "<!-- medlit-s7-10 begin -->", "<!-- medlit-s7-10 end -->"

s = open(GUIDE, encoding="utf-8").read()
s = re.sub(re.escape(B) + r".*?" + re.escape(E) + r"\n?", "", s, flags=re.S)
s = re.sub(r'[ \t]*<a href="#[a-z]+" data-s710="1">[^\n]*</a>\n', "", s)
blocks, toc = [], []
for key, num, label in ORDER:
    p = os.path.join(FRAG, key + ".html")
    if not os.path.exists(p):
        continue
    blocks.append(open(p, encoding="utf-8").read().strip())
    toc.append('  <a href="#%s" data-s710="1">%s &middot; %s</a>\n' % (key, num, label))
if blocks:
    marker = "<!-- ============ QUICK REFERENCE ============ -->"
    assert marker in s, "quick-reference marker missing"
    s = s.replace(marker, B + "\n" + "\n\n".join(blocks) + "\n" + E + "\n\n" + marker, 1)
    t = '  <a href="#quickref">'
    assert t in s, "contents anchor missing"
    s = s.replace(t, "".join(toc) + t, 1)
    n = 5 + len(blocks)
    s = re.sub(r"Covers \d+ lecture decks \([^)]*\)", "Covers %d lecture decks (sessions 1\u20134 and 7\u201310)" % n, s, count=1)
open(GUIDE, "w", encoding="utf-8").write(s)
print("spliced %d section(s) into %s" % (len(blocks), os.path.basename(GUIDE)))
