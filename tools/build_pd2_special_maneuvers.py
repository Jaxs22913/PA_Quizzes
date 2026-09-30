#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Physical Diagnosis 2, Exam 2 "Special Maneuvers" guide.

    python3 tools/build_pd2_special_maneuvers.py

Source: the class handout on special maneuvers (a photographed sheet, Jaxon 2026-09-30), transcribed in its own
order and wording: Valsalva, standing, squatting, raised legs while supine, sustained hand grip -- each with
what the maneuver does to the heart and what it does to aortic stenosis, mitral valve prolapse and
hypertrophic obstructive cardiomyopathy. Only the abbreviation MVP is expanded (site rule: ABBREV (full term)).
The lecture deck (slides 58-63) is cross-checked in a callout; where it says more or differs, the page says so
rather than resolving it silently.

Skeleton: the Exam 2 study guide's head and tail (same design system, back bar and footer links).
Writes "Physical Diagnosis 2 Exam 2/pd2-exam-2-special-maneuvers.html". Then run tools/build_guide_docx.py and
tools/dark_tokens.py (this build strips the Word link and the dark tokens).
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2")
DONOR = os.path.join(FOLDER, "pd2-exam-2-study-guide.html")
OUT = os.path.join(FOLDER, "pd2-exam-2-special-maneuvers.html")
DECK = "PD II Advanced Cardiovascular & Peripheral Vascular System - Fall 2026.pptx"

AS = "aortic stenosis"
MVP = "mitral valve prolapse (MVP)"
HOCM = "hypertrophic obstructive cardiomyopathy (HOCM)"

# (id, heading, mechanism lines, [(direction, finding)])
MANEUVERS = [
    ("sm-valsalva", "Valsalva",
     ["Decreases left ventricular filling; increases intrathoracic pressure (decreases preload)"],
     [("Decreases", AS), ("Increases", MVP), ("Increases", HOCM)]),
    ("sm-standing", "Standing position",
     ["Decreases venous return to the right and left ventricles (preload) and decreases systemic arterial pressure (afterload)"],
     [("Decreases", AS), ("Increases", MVP), ("Increases", HOCM)]),
    ("sm-squatting", "Squatting position",
     ["Increases venous return to heart (preload) and increases systemic arterial pressure (afterload)"],
     [("Increases", AS), ("Decreases", MVP), ("Decreases", HOCM)]),
    ("sm-legs", "Raised legs while in a supine position",
     ["Increases venous return (preload) to the right and left ventricles"],
     [("Increases", AS), ("Decreases", MVP), ("Decreases", HOCM)]),
    ("sm-grip", "Sustained hand grip",
     ["Increases systemic arterial pressure (afterload) and venous return (preload)"],
     [("Decreases", AS), ("Decreases", MVP), ("Decreases", HOCM)]),
]

# the at-a-glance grid: (maneuver, preload, afterload, AS, MVP, HOCM). "not listed" = the handout does not say.
GRID = [
    ("Valsalva", "Decreases", "Not listed", "Decreases", "Increases", "Increases"),
    ("Standing position", "Decreases", "Decreases", "Decreases", "Increases", "Increases"),
    ("Squatting position", "Increases", "Increases", "Increases", "Decreases", "Decreases"),
    ("Raised legs, supine", "Increases", "Not listed", "Increases", "Decreases", "Decreases"),
    ("Sustained hand grip", "Increases", "Increases", "Decreases", "Decreases", "Decreases"),
]

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#special-maneuvers">Special maneuvers</a>
  <a href="#sm-valsalva">1 &middot; Valsalva</a>
  <a href="#sm-standing">2 &middot; Standing position</a>
  <a href="#sm-squatting">3 &middot; Squatting position</a>
  <a href="#sm-legs">4 &middot; Raised legs while in a supine position</a>
  <a href="#sm-grip">5 &middot; Sustained hand grip</a>
  <a href="#sm-glance">6 &middot; All five at a glance</a>
  <a href="#sm-deck">7 &middot; Checked against the lecture</a>
</nav>'''


def maneuver_block(n, m):
    mid, title, mech, finds = m
    h = '  <h3 class="sub" id="%s">%d &middot; %s</h3>\n  <ul>\n' % (mid, n, title)
    for line in mech:
        h += "    <li>%s</li>\n" % line
    h += '    <li>Auscultation findings\n      <ul>\n'
    for d, f in finds:
        h += "        <li>%s %s</li>\n" % (d, f)
    h += "      </ul>\n    </li>\n  </ul>\n"
    return h


def build_body():
    b = '''<main>

<section class="deck" id="special-maneuvers">
  <h2 class="deck-title">Special Maneuvers</h2>
  <p class="lecturer">Lecture 5 &middot; Advanced Cardiovascular &amp; Peripheral Vascular Examination &middot; the class handout on maneuvers, as written</p>
  <div class="io-box">
    <h3>Instructional Objective</h3>
    <p class="tag">Advanced Cardiac and Peripheral Vascular System Medical History and Examination</p>
    <ol type="a" start="9">
      <li>Demonstrate the proper clinical skills for maneuvers to evaluate murmurs.</li>
    </ol>
  </div>

  <div class="callout"><p><b>Five maneuvers, three murmurs.</b> Each maneuver changes how much blood returns to the heart (preload) or how hard the
  heart pumps against (afterload), and that changes how loud a murmur is. The handout tracks the same three conditions through every maneuver:
  aortic stenosis, mitral valve prolapse (MVP) and hypertrophic obstructive cardiomyopathy (HOCM). Sections 1&ndash;5 are the handout in its own order and
  wording; section 6 puts all five side by side.</p></div>

'''
    for i, m in enumerate(MANEUVERS, 1):
        b += maneuver_block(i, m) + "\n"
    b += '''  <h3 class="sub" id="sm-glance">6 &middot; All five at a glance</h3>
  <table>
    <tr><th>Maneuver</th><th>Preload</th><th>Afterload</th><th>Aortic stenosis</th><th>Mitral valve prolapse (MVP)</th><th>Hypertrophic obstructive cardiomyopathy (HOCM)</th></tr>
'''
    for row in GRID:
        b += "    <tr>" + "".join("<td>%s</td>" % c for c in row) + "</tr>\n"
    b += '''  </table>
  <p>&ldquo;Not listed&rdquo; means the handout does not state it for that maneuver.</p>
  <div class="callout"><p><b>What to notice when you read across.</b> Aortic stenosis and hypertrophic obstructive cardiomyopathy move in <em>opposite</em>
  directions on every maneuver except hand grip: Valsalva and standing decrease aortic stenosis and increase hypertrophic obstructive cardiomyopathy; squatting and
  raised legs do the reverse. Mitral valve prolapse moves with hypertrophic obstructive cardiomyopathy every time. Sustained hand grip is the one that decreases all three.</p></div>

  <h3 class="sub" id="sm-deck">7 &middot; Checked against the lecture</h3>
  <p>The lecture deck covers the same maneuvers on slides 58&ndash;63 and agrees with the handout where they overlap:</p>
  <ul>
    <li><b>Valsalva</b> (slide 61): forceful expiration against a closed airway raises intrathoracic pressure and decreases left ventricular filling (preload). The hypertrophic
    cardiomyopathy murmur increases; the aortic stenosis murmur gets softer or does not change.</li>
    <li><b>Standing quickly from a squatting position</b> (slide 62): blood moves to the legs and less returns to the heart, which decreases left ventricular preload. The hypertrophic
    cardiomyopathy murmur becomes louder; the aortic stenosis murmur gets softer.</li>
    <li><b>Squatting from a standing position, or leg raise</b> (slide 62): venous return and preload increase. The hypertrophic cardiomyopathy murmur gets softer, because the outflow
    obstruction lessens; the aortic stenosis murmur gets louder, because more blood rushes past the narrow valve. Mitral valve prolapse is moved later in systole.</li>
  </ul>
  <p><b>Where the deck says more.</b> On <b>isometric hand grip</b> (slide 63) the deck lists a different set of murmurs: it increases the systolic murmurs of mitral regurgitation,
  pulmonic stenosis and ventricular septal defect, and the diastolic murmurs of aortic regurgitation and mitral stenosis. The handout&rsquo;s hand grip entry covers only aortic stenosis,
  mitral valve prolapse and hypertrophic obstructive cardiomyopathy, so the two lists complement each other rather than conflict.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Marked in the lecture</span>
    <p>On the maneuvers slide about hypertrophic obstructive cardiomyopathy (slide 60) the deck states, in capitals:
    <em>&ldquo;IMPORTANT TO LEARN THIS MURMUR SO YOU DON&rsquo;T SIGN OFF INCORRECTLY ON A SPORTS PHYSICAL.&rdquo;</em> The deck also says the maneuvers help
    distinguish the murmurs of mitral valve prolapse and hypertrophic obstructive cardiomyopathy from aortic stenosis.</p>
  </div>

  <footer class="guide-foot">Source: the class handout on special maneuvers (transcribed as written, with abbreviations spelled out), cross-checked against
  <em>''' + DECK + '''</em> (Lauren Reynolds, MSPA, PA-C), Slides 58&ndash;63, and the PAJ 5310 syllabus instructional objectives.</footer>
</section>

<footer class="guide-foot">
  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
  <p style="text-align:center;">Built from your PAJ 5310 lecture decks for personal study &middot; Class of 2028.</p>
  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</footer>
'''
    return b


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap"')]
    tail = donor[donor.index("</main>") + len("</main>"):]
    ty0 = tail.index("var TEST_YOURSELF = {")
    ty1 = tail.index("\n  };", ty0) + len("\n  };")
    tail = tail[:ty0] + "var TEST_YOURSELF = {};" + tail[ty1:]
    head = re.sub(r'\s*<link rel="alternate" type="application/vnd\.openxmlformats[^>]*>', "", head)
    head = re.sub(r"<title>.*?</title>", "<title>Physical Diagnosis 2 &middot; Exam 2 &mdash; Special Maneuvers</title>", head, count=1, flags=re.S)
    head = re.sub(r'<header class="top">.*?</header>',
        '<header class="top">\n'
        '  <h1>Special Maneuvers</h1>\n'
        '  <p>PAJ 5310 Physical Diagnosis II &middot; Class of 2028 &middot; Exam 2 is Friday 20 November</p>\n'
        '  <p>Lecture 5 &middot; Valsalva, standing, squatting, raised legs and hand grip: what each does to aortic stenosis, mitral valve prolapse and hypertrophic cardiomyopathy</p>\n'
        '</header>', head, count=1, flags=re.S)
    head = head.replace("</style>", "  @media(max-width:700px){main table{display:block;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;}}\n</style>", 1)
    html = head + '<div class="layout wrap" data-readable>\n' + TOC + "\n\n" + build_body() + tail
    for need in ('class="guide-back-bar"', "window.reportMistake()", "../theme.js", 'data-dark-kind="guide"'):
        assert need in html, "missing chrome: %r" % need
    for bad in ("Exam 2 &mdash; Study Guide</h1>", "TEST_YOURSELF.cardiovascular", "pd2-exam-2-study-guide.docx"):
        assert bad not in html, "donor residue: %r" % bad
    text = re.sub(r"<[^>]+>", " ", html.split("<main>")[1].split("</main>")[0])
    assert "MVP" not in text.replace("(MVP)", ""), "bare MVP left"
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))


if __name__ == "__main__":
    main()
