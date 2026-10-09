# -*- coding: utf-8 -*-
"""Section 9 of the Microbiology Exam 2 guide -- Cocci of Medical Importance (Dr. Fair).

Exposes the same names as tools/_micro_e2_guide_l7.py and _l8.py (FIG, DECK, TOC, SECTION, TEST) plus
IMAGES in the build_micro_e2_guide.py tuple shape, read from the hand-written fragments beside it:
  l9_guide.html      the <section>          (edit here)
  l9_guide_toc.html  the table-of-contents links
  l9_guide_test.js   the TEST_YOURSELF bank entry (key cocciMedicalImportance)

Attribution: the deck names no lecturer (title slide: "Cocci of Medical Importance: Gram positive and Gram
negative"); the calendar row for 2026-10-02 names Dr. Fair, and the recording is not Dr. Webster's ("with
Dr. Webster earlier, you had the gram-positive rods", 32:08) and promises the class "next Friday" on
antibiotic alternatives, which is Lecture 11, Dr. Fair's.

Instructional objectives are VERBATIM from the syllabus (Micro.pdf, page 4): the two numbered objectives
under "Cocci of Medical Importance - see Appendix 2 for full list of organisms"; the fifteen Appendix 2
organisms (page 8) are listed in the opening callout.

AUDIO: the one 59:37 recording (micro-cocci-paj5200-cocci-of-med-importance-2026-10-02-part1), read in
BOTH transcripts (local faster-whisper, 2026-10-05, and Notability's) and diffed 2026-10-08 (word-level
agreement 0.97, no content disagreement). Every quote in the section appears in both; timestamps are the
local transcript's.

FIGURES: tools/extract_micro_l9_figures.py writes the l9-* files into micro-exam-2-study-guide-images/
(re-encoded JPEG, at most 900 px wide; slide 26 comes out 900 x 544 from a 1200 x 725 original). The
IMAGES tuples below also work with build_micro_e2_guide.py's raw-blob extract_images(): every one is a
single JPEG picture on its slide.
"""
import io, os

HERE = os.path.dirname(os.path.abspath(__file__))
FIG = "micro-exam-2-study-guide-images"
DECK = "PAJ5200.Cocci of Med importance.pptx"


def _read(name):
    return io.open(os.path.join(HERE, name), encoding="utf-8").read()


TOC = "\n" + _read("l9_guide_toc.html")
SECTION = "\n" + _read("l9_guide.html")
TEST = _read("l9_guide_test.js")

# (slide, picture index on that slide, published file name) -- add to IMAGES in build_micro_e2_guide.py
# as (DECK9, slide, index, name).
IMAGES = [
    (4, 1, "l9-s04-staphylococci.jpg"),
    (11, 1, "l9-s11-furuncle-carbuncle.jpg"),
    (18, 1, "l9-s18-catalase-coagulase.jpg"),
    (22, 1, "l9-s22-streptococci.jpg"),
    (24, 1, "l9-s24-hemolysis-flowchart.jpg"),
    (26, 1, "l9-s26-streptococcus-table.jpg"),
    (29, 1, "l9-s29-group-a-envelope.jpg"),
    (42, 1, "l9-s42-camp-test.jpg"),
    (49, 1, "l9-s49-pneumococci.jpg"),
    (69, 1, "l9-s69-ascending-gonorrhea.jpg"),
    (72, 1, "l9-s72-gonococci.jpg"),
    (75, 1, "l9-s75-meningococcus.jpg"),
]

if __name__ == "__main__":
    import re
    assert SECTION.count('<section class="deck"') == 1
    for m in re.finditer(r'href="#([\w-]+)"', TOC):
        assert 'id="%s"' % m.group(1) in SECTION, "TOC anchor without target: " + m.group(1)
    srcs = re.findall(r'src="(%s/[^"]+)"' % FIG, SECTION)
    assert sorted(s.split("/")[-1] for s in srcs) == sorted(n for _, _, n in IMAGES), "figures and IMAGES differ"
    root = os.path.dirname(os.path.dirname(HERE))
    for s in srcs:
        assert os.path.exists(os.path.join(root, "Microbiology Exam 2", s)), s
    assert "TEST_YOURSELF.cocciMedicalImportance" in SECTION and TEST.lstrip().startswith("cocciMedicalImportance:")
    print("ok: %d TOC links, %d figures, section %d KB" % (TOC.count("<a "), len(srcs), len(SECTION) // 1024))
