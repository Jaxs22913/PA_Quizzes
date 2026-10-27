#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Microbiology Exam 3 study guide (Lectures 14-19; Lecture 14 so far).

Skeleton lifted from the Microbiology Exam 1 guide -- head, styles, back bar, pull-to-refresh, footer and
scripts -- exactly as tools/build_micro_e2_guide.py does, so the class reads as one thing; only the title,
header, table of contents, body and TEST_YOURSELF bank change. The forest-green palette is kept on purpose: the
Exam 3 quizzes share the class palette.

Sections are numbered by LECTURE (14, 15, ...) as the earlier Microbiology guides are, and each lecture's
instructional objectives are quoted verbatim from the syllabus and answered in order. Later Exam 3 lectures get
their own tools/micro_e3/_micro_e3_guide_lN.py and a line in SECTIONS below.

Figures are re-extracted from the decks each run by each module's extract() (python-pptx, by slide and picture
index, pictures, placeholders and grouped pictures alike) into micro-exam-3-study-guide-images/, and every one
cites its slide. Each was viewed at full size before being captioned. Every <img> width and height is checked
against the written file.

    python3 tools/build_micro_e3_guide.py
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
sys.path.insert(0, os.path.join(HERE, "micro_e3"))
import _micro_e3_guide_l14 as L14

SECTIONS = [L14]
DONOR = os.path.join(ROOT, "Microbiology Exam 1", "micro-exam-1-study-guide.html")
OUTDIR = os.path.join(ROOT, "Microbiology Exam 3")
OUT = os.path.join(OUTDIR, "micro-exam-3-study-guide.html")
IMGDIR = os.path.join(OUTDIR, "micro-exam-3-study-guide-images")

# No abbreviations in guide prose (no_abbreviations_content_policy): the nucleic acids are written out, as the
# earlier guides do.
PROSE_FIXES = [
    (r"(?<![\w(\[])DNA(?![\w)\]]| \[)", "deoxyribonucleic acid"),
    (r"(?<![\w(\[])RNA(?![\w)\]]| \[)", "ribonucleic acid"),
]


def main():
    n_img = sum(s.extract(IMGDIR) for s in SECTIONS)
    donor = io.open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap"')]
    foot = donor[donor.index('<footer class="guide-foot">'):donor.index("</footer>") + len("</footer>")]
    tail = donor[donor.index("</main>"):]
    ts = tail.index("var TEST_YOURSELF = {")
    te = tail.index("\n  };", ts)
    bank = "".join(s.TEST for s in SECTIONS).rstrip().rstrip(",")
    tail = tail[:ts] + "var TEST_YOURSELF = {\n" + bank + "\n" + tail[te:]

    head = re.sub(r"<title>.*?</title>",
                  "<title>Microbiology &middot; Exam 3 &mdash; Study Guide</title>", head, count=1, flags=re.S)
    head = re.sub(r"<header class=\"top\">.*?</header>",
        '<header class="top">\n  <h1>Microbiology &middot; Exam 3 &mdash; Study Guide</h1>\n'
        '  <p>PAJ 5200 Microbiology &middot; Class of 2028</p>\n'
        '  <p>Covers Lecture 14 so far &mdash; Gram-Negative Bacilli of Medical Importance &middot; the Exam 3 '
        'block is Lectures 14&ndash;19 &middot; Exam 3 is on Wednesday 2 December 2026 &middot; Instructional '
        'Objectives (IOs) taken verbatim from the syllabus</p>\n</header>',
        head, count=1, flags=re.S)
    # the Word-export link is re-added by tools/build_guide_docx.py for THIS page
    head = re.sub(r'\n?\s*<link rel="alternate" type="application/vnd\.openxmlformats[^>]*>', "", head)

    toc = '<nav class="toc">\n  <h2>Contents</h2>' + "".join(s.TOC for s in SECTIONS) + "</nav>"
    body = "<main>\n" + "\n".join(s.SECTION for s in SECTIONS) + "\n" + foot + "\n"
    for pat, rep in PROSE_FIXES:
        body = re.sub(pat, rep, body)
    html = head + '<div class="layout wrap" data-readable>\n' + toc + "\n\n" + body + tail

    # guards: structure the rest of the site relies on
    assert html.count('<section class="deck"') == len(SECTIONS)
    assert "guide-back-bar" in html and "window.reportMistake()" in html and "../index.html" in html
    assert "data-audio-dir" not in html
    assert "micro-exam-1" not in body, "an Exam 1 path leaked into the body"
    for m in re.finditer(r'href="#([\w-]+)"', toc):
        assert 'id="%s"' % m.group(1) in html, "TOC anchor without target: " + m.group(1)
    from PIL import Image
    for m in re.finditer(r'<img width="(\d+)" height="(\d+)"[^>]*src="(micro-exam-3-study-guide-images/[^"]+)"',
                         html):
        path = os.path.join(OUTDIR, m.group(3))
        assert os.path.exists(path), m.group(3)
        size = Image.open(path).size
        assert size == (int(m.group(1)), int(m.group(2))), "%s is %dx%d, page says %sx%s" % (
            m.group(3), size[0], size[1], m.group(1), m.group(2))
    used = set(re.findall(r'src="micro-exam-3-study-guide-images/([^"]+)"', html))
    written = set(os.listdir(IMGDIR))
    assert used == written, "figures written but unused: %s; used but not written: %s" % (
        sorted(written - used), sorted(used - written))
    for s in SECTIONS:
        key = re.search(r"TEST_YOURSELF\.(\w+)", s.SECTION).group(1)
        assert key + ":" in html, "no TEST_YOURSELF bank for " + key

    io.open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d figures)" % (os.path.relpath(OUT, ROOT), len(html) // 1024, n_img))


if __name__ == "__main__":
    main()
