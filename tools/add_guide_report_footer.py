#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Give the six newest study guides the page-level footer the older ones have.

THE GAP: guides built on the newer template carry a per-SECTION
<footer class="guide-foot"> citing that lecture's deck, but never gained the
page-level footer that the older guides end with -- the one holding "Back to
Homepage" and, more importantly, the REPORT-A-MISTAKE link.

That link is the standing convention for all content (see the report feature
note): every page must offer window.reportMistake(). Eight of the fourteen
guides had it and six did not, purely as an artifact of which template they were
built from. Found by checking rather than assuming, after the CMS Lecture 9 and
PDM Lecture 3-4 builds.

The per-section source footers are LEFT ALONE. They do a different job -- they
cite the deck a section was built from -- and the page-level footer is added
after the last of them, immediately before </main>.

Idempotent: skips any guide that already has a reportMistake link.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# course code per class, taken from each guide's own syllabus citations
GUIDES = [
 ("Clinical Medicine and Surgery I Exam 1/cms-exam-1-study-guide.html", "PAJ 5500"),
 ("Clinical Pathophysiology I Exam 1/cp-exam-1-study-guide.html", "PAJ 5101"),
 ("Microbiology Exam 1/micro-exam-1-study-guide.html", "PAJ 5200"),
 ("Pharmacology I Exam 1/pharm-exam-1-study-guide.html", "PAJ 5410"),
 ("Physical Diagnosis 2 Exam 1/pd2-exam-1-study-guide.html", "PAJ 5310"),
 ("Principles of Diagnostic Medicine I Exam 1/pdm-exam-1-study-guide.html", "PAJ 5600"),
]

FOOTER = """
<footer class="guide-foot">
  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
  <p style="text-align:center;">Built from your %s lecture decks for personal study &middot; Class of 2028.</p>
  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</footer>
"""


def main():
    changed = skipped = 0
    for rel, code in GUIDES:
        path = os.path.join(ROOT, rel)
        assert os.path.exists(path), "guide not found: %s" % rel
        s = open(path, encoding="utf-8").read()
        if "reportMistake" in s:
            skipped += 1
            print("  already has it, skipped: %s" % os.path.basename(rel))
            continue
        assert s.count("</main>") == 1, "%s: expected exactly one </main>" % rel
        i = s.index("</main>")
        s = s[:i] + FOOTER + s[i:]
        # theme.js is what defines window.reportMistake, so the page must load it
        assert re.search(r'src="\.\./theme\.js"', s), \
            "%s does not load theme.js, so reportMistake would be undefined" % rel
        open(path, "w", encoding="utf-8").write(s)
        changed += 1
        print("  added: %-52s (%s)" % (os.path.basename(rel), code))
    print("\n%d guide(s) updated, %d already had it" % (changed, skipped))


if __name__ == "__main__":
    main()
