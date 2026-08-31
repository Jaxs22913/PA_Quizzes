#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Splice Lecture 13 into the CMS I Exam 2 study guide.

Additive and fenced, like the Lecture 11/12 adder, and for the same reason: a
guide rebuild once destroyed hand-written content that had to be recovered from
git. This inserts between its OWN fence pair and touches nothing else.

The separate toc/body fences matter. A single shared pair made the second splice
find and overwrite the first, which dropped both sections inside <nav> and
deleted the table of contents.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _cms_e2_guide_l13 import SECTION as S13, TOC as T13, TEST as Q13

GUIDE = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                     "cms-exam-2-study-guide.html")
FENCES = {"toc":  ("<!--CMSE2L13-TOC-->",  "<!--/CMSE2L13-TOC-->"),
          "body": ("<!--CMSE2L13-BODY-->", "<!--/CMSE2L13-BODY-->")}


def splice(text, key, block, before):
    op, cl = FENCES[key]
    fenced = op + block + cl
    pat = re.compile(re.escape(op) + ".*?" + re.escape(cl), re.S)
    if pat.search(text):
        return pat.sub(lambda _: fenced, text, count=1)
    assert text.count(before) == 1, "anchor %r is not unique" % before
    return text.replace(before, fenced + before)


def main():
    t = io.open(GUIDE, encoding="utf-8").read()
    before = len(t)

    t = splice(t, "toc", "\n" + T13, "</nav>")
    t = splice(t, "body", "\n" + S13 + "\n", "</main>")

    anchor = "  var TEST_YOURSELF = {\n"
    assert t.count(anchor) == 1
    if "    cvl: [" not in t:
        t = t.replace(anchor, anchor + Q13)

    io.open(GUIDE, "w", encoding="utf-8").write(t)
    print("guide %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    folder = os.path.dirname(GUIDE)
    missing = [s for s in re.findall(r'src="(cms-ophtho-chart-images/[^"]+)"', t)
               if not os.path.exists(os.path.join(folder, s))]
    assert not missing, "missing images: %s" % missing

    # the earlier sections and their table of contents must survive
    for need in ('id="chronic-vision-loss"', "TEST_YOURSELF.cvl", "    cvl: [",
                 'id="neuro-ophthalmology"', 'id="acute-vision-loss"',
                 'href="#e2l1-approach"', 'href="#e2l4-melanoma"'):
        assert need in t, "missing after splice: %s" % need

    # structural: the new section sits inside <main>, its links inside <nav>
    nav_a, nav_b = t.index('<nav class="toc">'), t.index("</nav>")
    main_a, main_b = t.index("<main"), t.index("</main>")
    sec = t.index('id="chronic-vision-loss"')
    assert main_a < sec < main_b, "section landed outside <main>"
    link = t.index('href="#e2l4-iih"')
    assert nav_a < link < nav_b, "table of contents link landed outside <nav>"
    print("verified: section inside <main>, links inside <nav>, earlier sections intact")


if __name__ == "__main__":
    main()
