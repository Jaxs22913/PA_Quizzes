#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Pharmacology I Exam 3 study guide (Lectures 9 to 13; only Lecture 9 is built so far).

Same skeleton-lift as build_pharm_e2_guide.py: take the Exam 1 guide's head and tail so the chrome, design
system (the Pharmacology brown palette, dark tokens) and theme wiring come for free, and splice in a fresh
table of contents and body.

BUILT INCREMENTALLY, AND THE PAGE SAYS SO. The syllabus puts LECTURES 9 TO 13 in Exam 3 (Thursday 2026-12-03).
Section 1 (Lecture 9, diuretics and heart failure drugs) lives in _pharm_e3_guide_l9.py. Each later lecture is one
more module (_pharm_e3_guide_l10.py ...) added to SECTIONS below, exactly as the Exam 2 guide grew.

Objectives are VERBATIM from the syllabus, not from the deck (the deck's slide 2 drops "molecular" from
objective 2; [[guide_verbatim_io_rule]] says the syllabus wins).

Deliberately NO data-audio-dir (removed site-wide) and no Test Yourself bank (Exam 1's would answer nothing here).
"""
_REPO = __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__)))
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _pharm_e3_guide_l9 as L9

SECTIONS = [L9]          # append _pharm_e3_guide_l10 ... as those lectures are built
ROOT = _REPO
DONOR = os.path.join(ROOT, "Pharmacology I Exam 1/pharm-exam-1-study-guide.html")
OUT = os.path.join(ROOT, "Pharmacology I Exam 3/pharm-exam-3-study-guide.html")

TOC = '''<nav class="toc">
  <h2>Contents</h2>
@@MORE_TOC@@
</nav>'''

INTRO = '''<main>

<div class="callout" id="built-incrementally"><strong>This guide is built as the lectures are delivered.</strong> The syllabus puts Lectures 9 to 13
in Exam 3, which is on Thursday, December 3, 2026. <strong>Lecture 9 (diuretics and heart failure drugs) is in</strong>; Lectures 10 to 13
(antiarrhythmic drugs; pulmonary infections, asthma and COPD; hematological drugs; oncology drugs) are added as they are delivered.
Master exams are held until the whole block is in.</div>
@@MORE_BODY@@
</main>'''


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap"')]
    tail = donor[donor.index("</main>") + len("</main>"):]

    i = tail.find("TEST_YOURSELF")
    assert i != -1, "donor has no Test Yourself block; check the donor guide"
    ts = tail.rfind("<script", 0, i)
    te = tail.index("</script>", i) + len("</script>")
    assert ts != -1 and ts < i < te, "could not bound the Test Yourself script"
    tail = tail[:ts] + tail[te:]
    assert "TEST_YOURSELF" not in tail, "Test Yourself survived removal"

    alt = re.compile(r'\s*<link rel="alternate"[^>]*pharm-exam-1[^>]*>')
    head = re.sub(r"<title>.*?</title>", "<title>Pharmacology I Exam 3 Study Guide &mdash; Lectures 9 to 13</title>", head, count=1, flags=re.S)
    head = re.sub(r'<header class="top">.*?</header>',
                  '<header class="top">\n  <h1>Pharmacology I Exam 3 Study Guide</h1>\n'
                  '  <p>Lectures 9 to 13 &middot; Diuretics and Heart Failure Drugs (built so far) &middot; Class of 2028</p>\n'
                  '  <p>Adam Wood, Pharm.D., DABAT</p>\n</header>', head, count=1, flags=re.S)
    head = re.sub(r'\s*data-audio-dir="[^"]*"', "", head)
    head = alt.sub("", head)

    toc = TOC.replace("@@MORE_TOC@@", "\n".join(m.TOC for m in SECTIONS))
    body = INTRO.replace("@@MORE_BODY@@", "".join(m.BODY for m in SECTIONS))
    html = head + '<div class="layout wrap" data-readable>' + "\n" + toc + "\n\n" + body + tail

    for tag in ("div", "section", "p", "h2", "h3", "h4", "ol", "ul", "li", "nav", "main", "strong", "em", "table", "mark"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert "data-audio-dir" not in html, "audio dir survived"
    assert "TEST_YOURSELF" not in html, "Exam 1 question bank survived"
    assert "pharm-exam-1" not in html, "a link to Exam 1 survived"
    assert html.count('class="io-box"') == len(SECTIONS), "objective box count"
    assert "@@" not in html, "placeholder survived"
    assert '<section class="deck" id="diuretics-hf">' in html
    # every TOC link must hit an id
    for m in re.finditer(r'<a (?:class="top-link" )?href="#([^"]+)"', toc):
        assert 'id="%s"' % m.group(1) in html, "TOC target missing: " + m.group(1)

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d subsections)" % (os.path.basename(OUT), len(html) // 1024, len(re.findall(r'<h3 class="sub"', html))))


if __name__ == "__main__":
    main()
