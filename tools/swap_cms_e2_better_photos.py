#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Swap six Exam 2 ophthalmology rows onto a photograph of the finding.

Jaxon, 2026-09-01: "If you find better photos like non CT replace them in the
charts and stuff."

Auditing all 225 pictures in the five decks for "Guess that Disease" turned up
a photograph of the actual finding for six rows illustrated with a head CT, an
anatomy diagram or a screenshot of a table. Three were worse than merely dull
-- the guide's caption described a finding its picture did not show:

  Amblyopia              caption "Occlusion objection -- content until the GOOD
                         eye is covered", picture: a screening-criteria table.
  Cranial nerve III      caption "Ptosis with the eye down and out", picture:
                         the nerve's anatomical course.
  Adie tonic pupil       caption "The LARGER pupil, reacting poorly to light",
                         picture: a generic normal-pupil response grid.
  Periorbital haematoma  a head CT; the photograph is on the same slide.
  Lid laceration         the eyelid cross-section, i.e. anatomy, not an injury.
  Post-septal cellulitis a swollen lid -- which is what PRE-septal looks like.

ONE FIGURE AT A TIME, NEVER A BLANKET FILENAME REPLACE. The first version of
this script did `s.replace(old, new)` and quietly broke two OTHER figures that
use the same two files ON PURPOSE: the guide explains the third nerve with the
anatomical-course diagram ("Diagram of the third cranial nerve's course from
midbrain to orbit") and explains pupil testing with the response grid ("Four
panels showing pupil behaviour in dark, light and near gaze"). Those want the
diagram. Only the figure whose alt text NAMES THE CONDITION is a row picture,
so that is what is matched here.

The one deliberate exception is the pre-septal/post-septal figpair, whose
caption promises "Right, post-septal -- the globe is involved". It did not
show the globe involved. Now it does.

Edits the rendered chart and guide AND the builders behind them, so a rebuild
cannot put the old picture back. The guide is patched in place rather than
rebuilt: build_cms_e2_guide.py rewrites the whole file and a rebuild has
destroyed spliced-in sections before.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
E2 = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2")
DIR = "cms-ophtho-chart-images"

# chart row name, guide figure name, old image, old slide, new image, new slide
SWAPS = [
    ("Periorbital haematoma", "Periorbital haematoma",
     "l14-s034_pos2.jpg", 34, "l14-s034_pos1.jpg", 34),
    ("Lid laceration", "Lid laceration",
     "l14-s027_pos1.jpg", 27, "l14-s029_pos1.jpg", 29),
    ("Post-septal (orbital) cellulitis", "Post-septal (orbital) cellulitis",
     "s052_2.jpg", 52, "l10-s052_pos2.jpg", 52),
    ("Amblyopia", "Amblyopia",
     "l13-s032_1.jpg", 32, "l13-s032_pos2.jpg", 32),
    ("Cranial nerve III palsy", "Cranial nerve III palsy",
     "l11-s039_2.jpg", 39, "l11-s040_pos1.jpg", 40),
    ("Adie tonic pupil", "Adie tonic pupil",
     "l11-s020_1.jpg", 20, "l11-s037_pos1.jpg", 37),
]

BUILDERS = ["tools/_cms_e2_chart_l14.py", "tools/add_cms_e2_guide_l14.py",
            "tools/_cms_e2_chart_l13.py", "tools/_cms_e2_chart_l1112.py",
            "tools/build_cms_ophtho_chart.py", "tools/build_cms_e2_guide.py"]

# Two rows carried "no image on the slide" because the chart was built from the
# 60 pictures already extracted. Both DO have a photograph in the deck; the
# full sweep found them.  row name, image, slide, caption
ADDITIONS = [
    ("Horner syndrome", "l11-s015_pos1.jpg", 15,
     "Ptosis and miosis on the same side"),
    ("Cranial nerve VI palsy", "l11-s045_pos1.jpg", 45,
     "The affected eye will not abduct"),
]
# Which guide figure grid each one joins, keyed by a figure already in it.
ADD_TO_GRID = {
    "Horner syndrome": "Adie tonic pupil",
    "Cranial nerve VI palsy": "Cranial nerve III palsy",
}

n_edits = 0


def one(pattern, repl, s, what):
    """Exactly-one-match substitution. Anything else is a bug, not a no-op."""
    global n_edits
    hits = list(re.finditer(pattern, s, re.S))
    assert len(hits) == 1, "%s: matched %d times, wanted 1" % (what, len(hits))
    n_edits += 1
    print("    %s" % what)
    return s[:hits[0].start()] + re.sub(pattern, repl, hits[0].group(0), flags=re.S) + s[hits[0].end():]


def do_chart():
    p = os.path.join(E2, "cms-ophtho-comparison-chart.html")
    s = open(p, encoding="utf-8").read()
    print("  cms-ophtho-comparison-chart.html")
    for row, _g, old, osl, new, nsl in SWAPS:
        pat = (r'<img src="%s/%s" loading="lazy" alt="%s, from the lecture slides\.">'
               r'<span class="picite">Slide %d</span>' % (DIR, re.escape(old), re.escape(row), osl))
        rep = ('<img src="%s/%s" loading="lazy" alt="%s, from the lecture slides.">'
               '<span class="picite">Slide %d</span>' % (DIR, new, row, nsl))
        s = one(pat, lambda m: rep, s, "%s -> %s (Slide %d)" % (row, new, nsl))
    open(p, "w", encoding="utf-8").write(s)


def do_guide():
    p = os.path.join(E2, "cms-exam-2-study-guide.html")
    s = open(p, encoding="utf-8").read()
    print("  cms-exam-2-study-guide.html")
    for _r, name, old, osl, new, nsl in SWAPS:
        # Only the row figure: its alt text opens with the condition name.
        pat = (r'<figure><img src="%s/%s"([^>]*alt="%s &mdash;[^"]*")>'
               r'(.*?)<span class="fg-cite">Slide %d</span>'
               % (DIR, re.escape(old), re.escape(name), osl))
        s = one(pat,
                lambda m: '<figure><img src="%s/%s"%s>%s<span class="fg-cite">Slide %d</span>'
                          % (DIR, new, m.group(1), m.group(2), nsl),
                s, "%s -> %s (Slide %d)" % (name, new, nsl))
    # The pre-septal / post-septal pair promises "the globe is involved".
    s = one(r'(<figure class="fig figpair"><img src="%s/s052_1\.jpg"[^>]*>'
            r'<img src="%s/)s052_2\.jpg' % (DIR, DIR),
            lambda m: m.group(1) + "l10-s052_pos2.jpg", s,
            "pre-septal/post-septal figpair -> l10-s052_pos2.jpg")
    open(p, "w", encoding="utf-8").write(s)


def add_chart_pictures():
    """Fill the two "no image on the slide" cells."""
    p = os.path.join(E2, "cms-ophtho-comparison-chart.html")
    s = open(p, encoding="utf-8").read()
    print("  cms-ophtho-comparison-chart.html (rows that gain a picture)")
    for row, img, slide, _cap in ADDITIONS:
        pat = (r'<td class="pic"><span class="nopic">no image<br>on the slide</span></td>'
               r'(<td class="nm"><b>%s</b>)' % re.escape(row))
        rep = ('<td class="pic"><img src="%s/%s" loading="lazy" alt="%s, from the lecture '
               'slides."><span class="picite">Slide %d</span></td>\\1' % (DIR, img, row, slide))
        s = one(pat, rep, s, "%s gains %s (Slide %d)" % (row, img, slide))
    open(p, "w", encoding="utf-8").write(s)


def add_guide_pictures():
    """Append each new figure to the grid its section already has."""
    p = os.path.join(E2, "cms-exam-2-study-guide.html")
    s = open(p, encoding="utf-8").read()
    print("  cms-exam-2-study-guide.html (figures that gain a picture)")
    for row, img, slide, cap in ADDITIONS:
        anchor = ADD_TO_GRID[row]
        fig = ('<figure><img src="%s/%s" loading="lazy" decoding="async" alt="%s &mdash; %s">'
               '<figcaption><span class="fg-name">%s</span>%s'
               '<span class="fg-cite">Slide %d</span></figcaption></figure>'
               % (DIR, img, row, cap, row, cap, slide))
        pat = (r'(<div class="figgrid"><figure><img src="%s/[^"]+" loading="lazy" '
               r'decoding="async" alt="%s &mdash;.*?</figure>)(</div>)'
               % (DIR, re.escape(anchor)))
        s = one(pat, lambda m: m.group(1) + fig + m.group(2), s,
                "%s joins the %s grid" % (row, anchor))
    open(p, "w", encoding="utf-8").write(s)


def do_builders():
    for rel in BUILDERS:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        s = open(p, encoding="utf-8").read()
        before = s
        for row, name, old, osl, new, nsl in SWAPS:
            # The builders spell the same mapping four ways, and two of them
            # use single quotes -- matching only one shape leaves a builder
            # able to undo the swap on its next run.
            for q in ('"', "'"):
                s = s.replace('%s%s%s: (%s%s%s, %d)' % (q, row, q, q, old, q, osl),
                              '%s%s%s: (%s%s%s, %d)' % (q, row, q, q, new, q, nsl))
            s = s.replace('("%s", "%s",' % (old, name), '("%s", "%s",' % (new, name))
        # the guide's pre-septal/post-septal figpair, built from a flat list
        s = s.replace('"s052_1.jpg", "s052_2.jpg",', '"s052_1.jpg", "l10-s052_pos2.jpg",')
        if s != before:
            open(p, "w", encoding="utf-8").write(s)
            print("  %s updated" % rel)


def main():
    do_chart()
    do_guide()
    add_chart_pictures()
    add_guide_pictures()
    do_builders()
    print("made %d targeted figure edits" % n_edits)
    # the diagrams the other figures rely on must still be there
    g = open(os.path.join(E2, "cms-exam-2-study-guide.html"), encoding="utf-8").read()
    for keep in ("l11-s039_2.jpg", "l11-s020_1.jpg"):
        assert keep in g, "%s was removed from the guide -- it is used by a non-row figure" % keep
    print("verified: the third-nerve course diagram and the pupil-response grid are intact")
    for rel in BUILDERS:
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            continue
        b = open(p, encoding="utf-8").read()
        for row, name, old, osl, new, nsl in SWAPS:
            for q in ('"', "'"):
                assert '(%s%s%s, %d)' % (q, old, q, osl) not in b, \
                    "%s would still build %s with %s" % (rel, row, old)
    print("verified: no builder still maps a swapped row to its old picture")


if __name__ == "__main__":
    main()
