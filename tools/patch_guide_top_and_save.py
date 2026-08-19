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

   The chart does need print rules of its own on top of theme.css: it is a wide
   table in a horizontal scroll box, and theme.css only un-clips `.table-scroll`.
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
# `.table-scroll`, so it needs these to export as anything but a clipped strip.
CHART_PRINT_CSS = """
  @media print{
    .filterbar, .savehint{display:none !important;}
    .wrap{max-width:none !important;padding:0 !important;}
    .scroll{overflow:visible !important;border:0 !important;}
    table{min-width:0 !important;width:100% !important;font-size:7.4pt !important;
      table-layout:fixed;}
    td,th{padding:4px 5px !important;}
    thead th{position:static !important;background:#17494b !important;color:#fff !important;
      -webkit-print-color-adjust:exact;print-color-adjust:exact;}
    tr.sec td{position:static !important;background:#3f7d7a !important;color:#fff !important;
      -webkit-print-color-adjust:exact;print-color-adjust:exact;}
    td.pic{width:150px !important;min-width:150px !important;}
    td.pic img{max-height:96px !important;width:auto !important;}
    td.pic figcaption{font-size:5.6pt !important;}
    .pt{font-size:7pt !important;}
    td.name{width:110px !important;min-width:110px !important;}
    tr,figure{break-inside:avoid;page-break-inside:avoid;}
    .howto{break-inside:avoid;}
    @page{size:A4 landscape;margin:10mm 8mm;}
  }
"""

# theme.js gates the Download-as-PDF corner button on this element.
BACKBAR = """<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
"""


def main():
    # ---- 1. guide header
    s = open(GUIDE, encoding="utf-8").read()
    old = re.search(r'<header class="top">.*?</header>', s, re.S).group()
    assert "hdr-links" not in old, "guide header already updated"
    s = s.replace(old, NEW_HEADER, 1)
    anchor = "  header.top p{margin:2px 0;color:#f5e6ec;font-size:.95rem;}"
    assert s.count(anchor) == 1, "guide header css anchor not found"
    s = s.replace(anchor, anchor + HEADER_CSS, 1)
    open(GUIDE, "w", encoding="utf-8").write(s)
    print("guide header: lecture list, star explanation, 3 companion links, save hint")

    # ---- 2. opt the chart in to the existing corner Download-as-PDF button
    c = open(CHART, encoding="utf-8").read()
    assert "guide-back-bar" not in c, "chart already opted in"
    marker = '<div class="wrap">'
    assert c.count(marker) == 1, "chart wrap not found"
    c = c.replace(marker, BACKBAR + marker, 1)
    css_anchor = "  .filterbar{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:0 0 16px;}"
    assert c.count(css_anchor) == 1, "chart css anchor not found"
    c = c.replace(css_anchor, css_anchor + CHART_PRINT_CSS, 1)
    c = c.replace("<p>__NROWS__", "<p>__NROWS__")   # no-op guard, template already rendered
    hint = ('<p style="margin-top:10px;font-size:.82rem;opacity:.8">Use the '
            '<b>Download as PDF</b> button, top right, to keep this offline '
            '&mdash; it prints landscape with every row intact.</p>')
    c = c.replace("</header>", hint + "\n</header>", 1)
    open(CHART, "w", encoding="utf-8").write(c)
    print("chart: opted in to the existing corner Download-as-PDF button + landscape print rules")

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
