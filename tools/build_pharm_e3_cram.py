#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Pharmacology I Exam 3 cram sheet (Lecture 9 so far; Lectures 10 to 13 are added as delivered).

REFUSES TO WRITE unless every row verifies: each `verify` substring must appear on the slide it cites
(pharm_e3_lib.slide_text, picture-slide text included) and each `quotes` substring in the recording transcript
(check_pharm_e3_wood.transcript). No row may carry a milligram dose or a source word, and the HTML must be
well formed. Topics live in _pharm_e3_cram_l9.py (one module per lecture, appended in order).
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render
sys.path.insert(0, HERE)
import pharm_e3_lib as L
import check_pharm_e3_wood as W
import _pharm_e3_cram_l9 as C9

OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 3/pharm-exam-3-cram-sheet.html")
T = C9.T
REG = C9.REG

DOSE = re.compile(r"\b\d+(\.\d+)?\s*(mg|mcg|µg)\b", re.I)
BRIT = re.compile(r"\b(colour|flavour|oedema|anaemia|haemoglobin|paediatric|foetus|oestrogen|litre|behaviour|centre|programme|tumour)\w*", re.I)


def verify():
    fails, nsub, nq = [], 0, 0
    for label, pairs, quotes in REG:
        for slide, subs in pairs:
            body = L.slide_text("L9", slide)
            if not body:
                fails.append((label, "slide %d has no text" % slide)); continue
            for v in subs:
                nsub += 1
                if L.norm(v) not in body:
                    fails.append((label, "NOT ON SLIDE %d: %r" % (slide, v)))
        for q in quotes:
            nq += 1
            if W.norm(q) not in W.transcript("L9"):
                fails.append((label, "NOT IN TRANSCRIPT: %r" % q))
    for t in T:
        for label, html in t["rows"]:
            plain = re.sub(r"<[^>]+>|&[a-z#0-9]+;", " ", label + " " + html)
            if DOSE.search(plain):
                fails.append((label, "milligram dose: %r" % DOSE.search(plain).group(0)))
            if BRIT.search(plain):
                fails.append((label, "British spelling: %r" % BRIT.search(plain).group(0)))
    return fails, nsub, nq


fails, nsub, nq = verify()
print("cram rows: %d   slide substrings: %d   transcript quotes: %d   %s"
      % (sum(len(t["rows"]) for t in T), nsub, nq, "OK" if not fails else "FAILED %d" % len(fails)))
for label, why in fails[:80]:
    print("   [%s] %s" % (re.sub("<[^>]+>|&[a-z#0-9]+;", "", label)[:40], why))
if fails:
    sys.exit("cram verification failed -- refusing to write the page")

html = render(
    title="Pharmacology I Exam 3 Cram Sheet &mdash; Lecture 9 so far",
    kicker="Pharmacology I &middot; Exam 3 &middot; Class of 2028",
    h1="Pharmacology I Exam 3 Cram Sheet",
    sub="Lecture 9 (diuretics and heart failure drugs), Adam Wood Pharm.D. DABAT. "
        "Lectures 10 to 13 are added as delivered. "
        "&#9733; = professor emphasized (from the recording); a star only sets weight and adds no fact the slides lack. "
        "Rows marked FLAG say where a slide and the pharmacology disagree.",
    topics=T,
    guide_href="pharm-exam-3-study-guide.html",
    footer_note="Exam 3 covers Lectures 9 to 13 &mdash; this sheet covers Lecture 9 so far. "
                "The <a href=\"pharm-exam-3-study-guide.html\">study guide</a> has the full "
                "treatment.")

for tag in ("div", "section", "p", "h2", "table", "tr", "td", "th", "b", "i", "a", "ul", "li"):
    o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
    assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)"
      % (os.path.basename(OUT), len(html) // 1024, len(T), sum(len(t["rows"]) for t in T)))
