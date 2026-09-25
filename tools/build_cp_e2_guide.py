#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Pathophysiology I, Exam 2 study guide.

Exam 2 = Lectures 6-10 (Wednesday 2026-11-18). Built now from the two decks
that exist -- Lecture 6 Cardiac and Lecture 7 Vascular -- with sections
numbered by lecture, so Lectures 8-10 (Immunity, Pulmonary, Blood Disorders)
append as sections 8-10 without renumbering anything.

Same skeleton-lift as build_cp_guide.py did for Exam 1, but the donor is the
Exam 1 guide itself: head/CSS/chrome/scripts come from
cp-exam-1-study-guide.html, which already carries the guide design system,
the nav.toc sizing convention and the professor-emphasis CSS. Only the palette,
title, header, TOC, body and TEST_YOURSELF change. Palette: cardiovascular
crimson (accent) with the class's warm gold (accent2) and a lighter crimson
(accent3) -- distinct from Exam 1's plum.

Content lives in cp_e2_guide_content.py. Mechanism throughout, never
management (clin_path_exam_spec) -- asserted below.
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import cp_e2_guide_content as C

DONOR = os.path.join(ROOT, "Clinical Pathophysiology I Exam 1", "cp-exam-1-study-guide.html")
OUT = os.path.join(ROOT, "Clinical Pathophysiology I Exam 2", "cp-exam-2-study-guide.html")

PALETTE = [
    ("--ink:#221c2b", "--ink:#241a1d"),
    ("--accent:#3b2a5e;      /* rose plum */", "--accent:#6e1f2f;      /* deep crimson */"),
    ("--accent2:#c08a2e;      /* warm gold */", "--accent2:#b07a22;      /* warm gold */"),
    ("--accent3:#6a4fa3;      /* muted violet */", "--accent3:#a23a4c;      /* light crimson */"),
    ("linear-gradient(120deg,#241a3d,var(--accent) 55%,#8f74c9)",
     "linear-gradient(120deg,#3a0d18,var(--accent) 55%,#c86a78)"),
    ("background:#efeaf4;padding:10px 16px", "background:#f6e9eb;padding:10px 16px"),
    ("stroke: #3b2a5e; stroke-width: 3", "stroke: #6e1f2f; stroke-width: 3"),
    (".footer-mark-accent { stroke: #3b2a5e; }", ".footer-mark-accent { stroke: #6e1f2f; }"),
    (".footer-mark-accent { stroke: #c4b0e8; }", ".footer-mark-accent { stroke: #e8a3ae; }"),
]

HEADER = '''<header class="top">
  <h1>Clinical Pathophysiology I &middot; Exam 2 &mdash; Study Guide</h1>
  <p>PAJ 5101 Clinical Pathophysiology I &middot; Class of 2028 &middot; Exam 2 is Wednesday 18 November 2026 (Lectures 6&ndash;10)</p>
  <p>Covers Lecture 6, Cardiac Pathophysiology, and Lecture 7, Vascular Pathophysiology &middot; Lectures 8&ndash;10 are added as each is posted &middot; Instructional Objectives (IOs) taken verbatim from the syllabus &middot; mechanism throughout, not management</p>
</header>'''

FOOT = '''
<footer class="guide-foot">
  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
  <p style="text-align:center;">Built from your PAJ 5101 lecture decks for personal study &middot; Class of 2028.</p>
  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</footer>
</main>
</div>'''

# Management vocabulary that has no place in a pathophysiology guide.
BANNED = ["first-line", "drug of choice", "treatment of choice", "next step",
          "how is it treated", "surgically repaired", "is treated with"]


def main():
    src = open(DONOR, encoding="utf-8").read()
    head_end = src.index('<header class="top">')
    head = src[:head_end]
    for a, b in PALETTE:
        assert a in head, "palette anchor missing from donor: " + a
        head = head.replace(a, b)
    head = head.replace("Clinical Pathophysiology I &middot; Exam 1 &mdash; Study Guide",
                        "Clinical Pathophysiology I &middot; Exam 2 &mdash; Study Guide")
    # The Word copy is generated afterwards by build_guide_docx.py, which adds
    # its own <link rel=alternate>; never inherit Exam 1's.
    head = re.sub(r'\s*<link rel="alternate"[^>]*>', "", head)
    # Captions in this guide use <span class="cite">; give it the same look the
    # Exam 1 lecture-5 figures get.
    head = head.replace("</style>\n</head>",
                        "  figure.fig figcaption .cite{display:block;margin-top:4px;font-style:normal;"
                        "font-size:12px;color:var(--accent3);}\n"
                        "  /* Phone widths: let long cells wrap instead of widening the page. */\n"
                        "  @media(max-width:820px){th,td{overflow-wrap:anywhere;padding:6px 7px;}}\n</style>\n</head>", 1)
    assert "figcaption .cite" in head

    tail_start = src.index("<script>\n(function () {\n  const indicator")
    tail = src[tail_start:]

    body = C.CARDIAC + C.VASCULAR
    low = re.sub(r"<[^>]+>", " ", body).lower()
    for w in BANNED:
        assert w not in low, "management wording in guide: " + w

    ty = "<script>\n  // High-yield \"Test yourself\" sets, one per lecture, fed to\n" \
         "  // window.openTestYourself (theme.js) by each section's button.\n" \
         "  var TEST_YOURSELF = " + json.dumps(C.TEST_YOURSELF, ensure_ascii=False, indent=1) + ";\n</script>\n"
    for key, qs in C.TEST_YOURSELF.items():
        pos = [q["correct"] for q in qs]
        assert all(len(q["choices"]) == 4 for q in qs), key
        assert max(pos.count(i) for i in range(4)) <= (len(qs) + 3) // 4, (key, pos)

    html = (head + HEADER + '\n\n<div class="layout wrap" data-readable>\n' + C.TOC +
            "\n\n<main>\n" + body + FOOT + "\n" + ty + tail)

    # Every anchor in the TOC must exist.
    for a in re.findall(r'href="#([^"]+)"', C.TOC + body):
        assert ('id="%s"' % a) in html, "missing anchor " + a
    # Every figure must exist on disk.
    for s in re.findall(r'src="(cp-exam-2-[^"]+)"', body):
        assert os.path.exists(os.path.join(os.path.dirname(OUT), s)), s
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote", os.path.relpath(OUT, ROOT), len(html), "bytes")


if __name__ == "__main__":
    main()
