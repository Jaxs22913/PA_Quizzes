#!/usr/bin/env python3
"""Splice Lectures 2 and 3 into the Pharmacology I Exam 1 study guide.

ADDITIVE, NOT A REBUILD, and that is deliberate. Re-running build_pharm_guide.py
destroys work: the committed guide carries content the builder no longer
produces -- a prof-flag block quoting Dr. Wood's own emphasis marker from the
Lecture 1 recording -- and the builder also re-points the Word-download link at
the Microbiology donor it lifts its skeleton from. A rebuild silently reverted
both. So this edits the guide in place instead.

Idempotent: everything written is fenced in <!--PHARML23--> markers and stripped
before re-inserting, so running twice is the same as running once.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _pharm_guide_l23 import TOC_ADD, BODY_ADD, TY_ADD

GUIDE = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 1",
                     "pharm-exam-1-study-guide.html")
OPEN, CLOSE = "<!--PHARML23-->", "<!--/PHARML23-->"


def strip(s):
    return re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE) + r"\s*", "", s, flags=re.S)


def main():
    s = io.open(GUIDE, encoding="utf-8").read()
    before_sections = s.count('<section class="deck"')
    s = strip(s)

    # 1. table of contents
    i = s.rindex("</nav>")
    s = s[:i] + OPEN + "\n" + TOC_ADD + CLOSE + "\n" + s[i:]

    # 2. the two sections, before the close of main
    i = s.rindex("</main>")
    s = s[:i] + OPEN + BODY_ADD + CLOSE + "\n\n" + s[i:]

    # 3. the Test Yourself banks
    key = "var TEST_YOURSELF = {"
    i = s.index(key) + len(key)
    # The whitespace AFTER the close fence has to be written explicitly rather
    # than inherited. strip() consumes it on a re-run, so leaving the original
    # indentation in place made the first run differ from every later one by
    # five bytes -- stable, but not actually idempotent.
    s = s[:i] + OPEN + "\n" + TY_ADD + "\n" + CLOSE + "\n    " + s[i:].lstrip()

    # 4. the header still claims the guide covers Lecture 1 only
    s = re.sub(r"Covers Lecture 1[^<]*?drug dosages are not tested",
               "Covers all three Exam 1 lectures &mdash; antimicrobials, dermatology medications "
               "and autonomic pharmacology &middot; Instructional Objectives (IOs) taken verbatim "
               "from the syllabus &middot; drug dosages are not tested", s, count=1)

    io.open(GUIDE, "w", encoding="utf-8").write(s)
    after = s.count('<section class="deck"')
    print("sections %d -> %d" % (before_sections, after))
    print("subsections:", s.count('<h3 class="sub"'))
    print("io-boxes:", s.count('class="io-box"'))
    print("test-yourself buttons:", s.count("test-yourself-btn"))
    print("prof-flag blocks preserved:", s.count('prof-flag"'))
    print("docx link still pharm's:", "pharm-exam-1-study-guide.docx" in s)
    print("%d KB" % (len(s) // 1024))


if __name__ == "__main__":
    main()
