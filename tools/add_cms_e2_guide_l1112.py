#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Splice Lectures 11 and 12 into the CMS I Exam 2 study guide.

ADDITIVE, and deliberately not a rebuild. Re-running a guide builder once
destroyed hand-written content in the pharmacology guide -- a prof-flag block
quoting the lecturer went with it, and it had to come back out of git. So this
inserts between fences and touches nothing else, and it is idempotent: running
it twice replaces the fenced block rather than stacking a second copy.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _cms_e2_guide_l11 import SECTION as S11, TOC as T11, TEST as Q11
from _cms_e2_guide_l12 import SECTION as S12, TOC as T12, TEST as Q12

GUIDE = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                     "cms-exam-2-study-guide.html")
# Each insertion point gets its OWN fence pair. A single shared pair would make
# the second splice find and overwrite the first one's block -- which it did,
# dropping both new sections inside <nav> and deleting the table of contents.
FENCES = {"toc":  ("<!--CMSE2L1112-TOC-->",  "<!--/CMSE2L1112-TOC-->"),
          "body": ("<!--CMSE2L1112-BODY-->", "<!--/CMSE2L1112-BODY-->")}


def splice(text, key, block, before):
    """Replace this key's fenced block, or insert it before `before`."""
    op, cl = FENCES[key]
    fenced = op + block + cl
    pat = re.compile(re.escape(op) + ".*?" + re.escape(cl), re.S)
    if pat.search(text):
        return pat.sub(lambda _: fenced, text, count=1)
    assert text.count(before) == 1, "anchor not unique: %r" % before[:40]
    return text.replace(before, fenced + before)


def main():
    t = io.open(GUIDE, encoding="utf-8").read()
    before = len(t)

    # 1. table of contents -- new entries at the end of the existing nav
    t = splice(t, "toc", "\n" + T11 + T12, "</nav>")
    # 2. the two sections, immediately before </main>
    t = splice(t, "body", "\n" + S11 + S12 + "\n", "</main>")
    # 3. the Test-yourself banks, appended inside the TEST_YOURSELF object
    anchor = "  var TEST_YOURSELF = {\n"
    assert t.count(anchor) == 1
    if "    neuro: [" not in t:
        t = t.replace(anchor, anchor + Q11 + Q12)

    io.open(GUIDE, "w", encoding="utf-8").write(t)
    print("guide %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    # verification: every referenced image must exist, and both sections present
    folder = os.path.dirname(GUIDE)
    missing = [s for s in re.findall(r'src="(cms-ophtho-chart-images/[^"]+)"', t)
               if not os.path.exists(os.path.join(folder, s))]
    assert not missing, "missing images: %s" % missing
    for need in ('id="neuro-ophthalmology"', 'id="acute-vision-loss"',
                 "TEST_YOURSELF.neuro", "TEST_YOURSELF.avl", "    neuro: [", "    avl: [",
                 'href="#e2l2-nystagmus"', 'href="#e2l3-aion"',
                 'href="#e2l1-approach"'):   # the ORIGINAL toc must survive too
        assert need in t, "missing after splice: %s" % need

    # structural: every new section must sit inside <main>, not inside <nav>
    nav_a, nav_b = t.index("<nav class=\"toc\">"), t.index("</nav>")
    main_a, main_b = t.index("<main class=\"content\">"), t.index("</main>")
    for sid in ("neuro-ophthalmology", "acute-vision-loss"):
        i = t.index('<section class="deck" id="%s"' % sid)
        assert main_a < i < main_b, "%s is outside <main>" % sid
        assert not (nav_a < i < nav_b), "%s landed inside <nav>" % sid
    for href in ("#e2l2-nystagmus", "#e2l3-aion"):
        j = t.index('href="%s"' % href)
        assert nav_a < j < nav_b, "toc link %s is outside <nav>" % href
    print("verified: sections inside <main>, toc links inside <nav>, "
          "original toc intact, both question banks, all images present")


if __name__ == "__main__":
    main()
