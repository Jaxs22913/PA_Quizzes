#!/usr/bin/env python3
"""Two changes to the CMS I Exam 1 study documents.

1. THE TOP OF THE GUIDE. It said only "Covers Lectures 1-5 and 8", which does
   not tell you what is actually in it now that the dermatology block is five
   sections deep, and it did not point at the companion documents built
   alongside it. The header now names each lecture, links to the comparison
   chart and the cram sheet and the quizzes, and explains the star-flagged
   blocks -- those come from the lecture recordings and are the highest-value
   thing in the document, but nothing told a reader that.

2. SAVE / DOWNLOAD. The site ALREADY has this: theme.js adds a
   "Download as PDF" corner button to any page carrying `.guide-back-bar`, and
   it handles two things a naive window.print() does not -- iOS Safari ignores
   a print() call deferred out of the tap gesture, and a dark-mode user would
   otherwise get a dark, ink-hungry PDF, so it forces light theme and restores
   it afterwards.

   The study guide and cram sheet already had it. THE NEW COMPARISON CHART DID
   NOT, because it was built without `.guide-back-bar`. So the fix is to opt the
   chart in rather than to write a second button -- a first draft here did add
   its own, which would have shipped a worse duplicate of a tested feature next
   to the real one.

   The chart needs print rules of its own on top of theme.css -- it is a wide
   table in a horizontal scroll box and theme.css only un-clips `.table-scroll`
   -- and it must NOT lazy-load its photographs: an export before that was
   fixed carried 10 of 84 images, because a lazy image that never entered the
   viewport is absent from the print output. Both of those live in
   build_cms_derm_chart.py, because the chart is generated and anything patched
   in here would be wiped by the next build. This script only verifies them.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(D, "cms-exam-1-study-guide.html")
CHART = os.path.join(D, "cms-derm-comparison-chart.html")

NEW_HEADER = """<header class="top">
  <h1>Clinical Medicine and Surgery I &middot; Exam 1 &mdash; Study Guide</h1>
  <p>PAJ 5500 Clinical Medicine and Surgery I &middot; Class of 2028 &middot; Exam 28 August</p>
  <p><b>Lecture 1</b> clinical reasoning, then the dermatology block &mdash;
     <b>2</b> General Dermatology I &middot; <b>3</b> Dermatology II &middot;
     <b>4</b> Cutaneous Bacterial Infections &middot; <b>5</b> Dermatological Infestations &middot;
     <b>8</b> Pigmented Skin Lesions</p>
  <p style="opacity:.9">Sections 6, 7 and 9 are added when those decks are posted &middot;
     Instructional Objectives quoted verbatim from the syllabus and answered in order</p>
  <p class="hdr-note">&#9733; <b>Starred blocks are things the professor said out loud</b> in the
     lecture recordings &mdash; what she will and will not ask, and the questions she said she would
     write. They are not on the slides.</p>
  <div class="hdr-links">
    <a href="cms-derm-comparison-chart.html">Dermatology Comparison Chart &rarr;</a>
    <a href="cms-exam-1-cram-sheet.html">Cram Sheet &rarr;</a>
    <a href="../index.html#cms-1">Quizzes &rarr;</a>
  </div>
  <p class="hdr-save">Use the <b>Download as PDF</b> button, top right, to keep this offline.</p>
</header>"""

HEADER_CSS = """
  header.top .hdr-note{margin-top:12px;font-size:.86rem;background:rgba(255,255,255,.14);
    display:inline-block;padding:7px 13px;border-radius:9px;}
  header.top .hdr-links{margin-top:14px;display:flex;flex-wrap:wrap;gap:9px;justify-content:center;}
  header.top .hdr-links a{font-size:.83rem;font-weight:700;color:#fff;text-decoration:none;
    border:1.5px solid rgba(255,255,255,.55);border-radius:999px;padding:6px 14px;}
  header.top .hdr-links a:hover{background:rgba(255,255,255,.16);}
  header.top .hdr-save{margin-top:12px;font-size:.8rem;opacity:.85;}
  @media print{ header.top .hdr-links, header.top .hdr-save{display:none !important;} }
"""

# The chart is a wide table inside its own scroll box; theme.css only un-clips



def main():
    # ---- 1. guide header
    s = open(GUIDE, encoding="utf-8").read()
    old = re.search(r'<header class="top">.*?</header>', s, re.S).group()
    if "hdr-links" in old:
        print("guide header: already applied")
    else:
        s = s.replace(old, NEW_HEADER, 1)
        anchor = "  header.top p{margin:2px 0;color:#f5e6ec;font-size:.95rem;}"
        assert s.count(anchor) == 1, "guide header css anchor not found"
        s = s.replace(anchor, anchor + HEADER_CSS, 1)
        open(GUIDE, "w", encoding="utf-8").write(s)
        print("guide header: lecture list, star explanation, 3 companion links, save hint")
    # the guide's figures must not lazy-load either, for the same reason
    g = open(GUIDE, encoding="utf-8").read()
    assert 'loading="lazy"' not in g, "guide has lazy images; they will not print"

    # ---- 2. the chart is a GENERATED file
    # Its back bar, print rules and save hint used to be injected here, which
    # meant the next run of build_cms_derm_chart.py silently wiped them. They
    # now live in that builder's own template, where regeneration keeps them.
    c = open(CHART, encoding="utf-8").read()
    assert 'class="guide-back-bar"' in c and "@media print" in c, (
        "chart is missing its back bar or print rules -- re-run build_cms_derm_chart.py")
    print("chart: back bar and print rules confirmed (owned by build_cms_derm_chart.py)")

    # ---- verification
    for path in (GUIDE, CHART):
        s = open(path, encoding="utf-8").read()
        for tag in ("style", "script", "header", "div", "table", "tr", "td", "p", "a"):
            o = len(re.findall(r"<%s[ >]" % tag, s))
            cl = s.count("</%s>" % tag)
            assert o == cl, "%s: %s %d/%d" % (os.path.basename(path), tag, o, cl)
        assert 'class="guide-back-bar"' in s, "%s: no back bar, so no PDF button" % path
        ids = set(re.findall(r'id="([^"]+)"', s))
        bad = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
        assert not bad, "%s dangling: %r" % (os.path.basename(path), bad)
    # the cram sheet already had the back bar and therefore the button
    cram = open(os.path.join(D, "cms-exam-1-cram-sheet.html"), encoding="utf-8").read()
    print("cram sheet already had the button:", 'class="guide-back-bar"' in cram)
    print("tag balance and anchors verified")


if __name__ == "__main__":
    main()
