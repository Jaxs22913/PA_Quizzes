#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Repair the study guides' page footers. Three distinct defects, found 2026-09-13.

All three surfaced while lifting the Microbiology guide's skeleton for the
Webster review page -- slicing "footer to end of file" pulled in 90 KB of
lecture content, because the footer was not at the end.

  1. STRANDED FOOTER. Each guide was built with its first lecture or two and a
     footer last. Every later `add_<class>_l<N>.py` spliced its section in
     before </main>, which is AFTER the footer. So the reader scrolls through
     Lecture 2, hits "<- Back to Homepage", and four more lectures continue
     below it. Micro had 75 KB below its own footer; Clin Path 48 KB.

  2. UNFORMATTED PLACEHOLDER. Six guides literally print "Built from your %s
     lecture decks" -- the course code was never substituted. The intended
     value is visible in the guides that were built correctly ("Built from your
     PAJ 5000 lecture decks"), and each affected guide states its own code in
     its header, so the value is recovered from the page rather than guessed.

  3. MISSING FOOTER. Three guides -- CMS Exams 2 and 3, Pharmacology Exam 2 --
     have no page footer at all. No "Back to Homepage" link and, more
     importantly, no report-a-mistake link, so a student who spots an error on
     those pages has no way to say so.

WHAT COUNTS AS THE PAGE FOOTER. Several guides carry per-lecture "Source: ..."
citation blocks that reuse the guide-foot class and are correctly placed at the
end of their own section. Those are left alone. The page footer is identified by
its "Back to Homepage" link, not by its class.

SCOPE. Semester 2 only. cam-nutrition-exam-2-study-guide.html has defect 1 but
Semester 1 is frozen, so it is reported and not touched.
"""
import glob
import io
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FROZEN = ("cam-nutrition", "anatomy-", "physiology-", "pd1-", "intro-pa")

FOOT = re.compile(r'<footer class="guide-foot".*?</footer>', re.S)

# Course codes for the guides that do not state one in their own header.
FALLBACK_CODE = {
    "cms-exam-2-study-guide.html": "PAJ 5500",
    "cms-exam-3-study-guide.html": "PAJ 5500",
    "pharm-exam-2-study-guide.html": "PAJ 5410",
}

FOOTER_TEMPLATE = """<footer class="guide-foot">
  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
  <p style="text-align:center;">Built from your %s lecture decks for personal study &middot; Class of 2028.</p>
  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</footer>"""


def course_code(name, src):
    """The guide's own course code, taken from the page before any fallback."""
    hit = re.search(r"\bPAJ\s?\d{4}\b", src)
    if hit:
        return hit.group(0)
    if name in FALLBACK_CODE:
        return FALLBACK_CODE[name]
    raise SystemExit("no course code for %s; add one to FALLBACK_CODE" % name)


def page_footer(src):
    """The real page footer, not a per-lecture Source: block."""
    hits = [m for m in FOOT.finditer(src) if "Back to Homepage" in m.group(0)]
    return hits[-1] if hits else None


def skeleton(doc):
    """Document with every footer stripped and ALL whitespace removed.

    Whitespace has to go entirely, not merely collapse. Re-inserting the footer
    adds a newline at a join that previously had none, so a collapse-to-single-
    space comparison reports a one-character difference on a move that changed
    no content -- which it did, on the Microbiology guide, the first time this
    ran.
    """
    return re.sub(r"\s+", "", FOOT.sub("", doc))


def main():
    fixed = {"moved": [], "placeholder": [], "added": []}
    skipped = []

    for path in sorted(glob.glob(os.path.join(ROOT, "*", "*study-guide.html"))):
        name = os.path.basename(path)
        src = io.open(path, encoding="utf-8").read()
        if "</main>" not in src:
            continue
        frozen = any(name.startswith(p) for p in FROZEN)
        out = src
        did = []

        # --- 2. the unformatted placeholder -----------------------------
        if "Built from your %s lecture decks" in out and not frozen:
            out = out.replace("Built from your %s lecture decks",
                              "Built from your %s lecture decks" % course_code(name, out))
            did.append("placeholder")

        # --- 3. missing page footer -------------------------------------
        if page_footer(out) is None:
            if frozen:
                continue
            code = course_code(name, out)
            mi = out.index("</main>")
            out = out[:mi] + (FOOTER_TEMPLATE % code) + "\n" + out[mi:]
            did.append("added")
        else:
            # --- 1. stranded page footer --------------------------------
            m = page_footer(out)
            below = len(re.sub(r"\s+", "", out[m.end():out.index("</main>")]))
            if below > 30:
                if frozen:
                    skipped.append((name, below))
                    continue
                block = m.group(0)
                without = out[:m.start()] + out[m.end():]
                mi = without.index("</main>")
                moved = without[:mi] + block + "\n" + without[mi:]
                assert skeleton(moved) == skeleton(out), \
                    "%s: content changed, not just moved" % name
                out = moved
                did.append("moved (%d chars were below it)" % below)

        if out != src:
            assert out.count("Back to Homepage") == 1, name
            assert "Built from your %s lecture" % "" not in out
            io.open(path, "w", encoding="utf-8").write(out)
            for d in did:
                fixed[d.split()[0]].append(name)
            print("  %-46s %s" % (name, "; ".join(did)))

    for name, n in skipped:
        print("  SKIPPED (Semester 1 frozen): %s -- %d chars still render below "
              "its footer" % (name, n))

    print("\nfooters moved: %d | placeholders filled: %d | footers added: %d | "
          "skipped: %d" % (len(fixed["moved"]), len(fixed["placeholder"]),
                           len(fixed["added"]), len(skipped)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
