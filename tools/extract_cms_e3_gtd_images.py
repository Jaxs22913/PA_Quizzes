#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the thirteen ENT pictures the comparison chart never used.

WHY THESE THIRTEEN. Building "Guess that Disease" for Exam 3 meant looking at
all 218 pictures in the five ENT decks, not just the 64 the comparison chart
had already picked. Most of what the audit turned up was unusable -- see the
bank's docstring for the three categories the inclusion bar throws out -- but
these thirteen are photographs of a finding that the chart passed over, usually
because the chart only needed one picture per row and this is a second one, or
because the chart's pick has the diagnosis printed across it.

The ones worth naming:

  l15-s034_pos1  cholesteatoma. The chart and guide use the deck's other
                 cholesteatoma pictures, and every one of those has "Primary
                 cholesteatoma" or "Early congenital cholesteatoma" printed in
                 the image. This black-and-white otoscopy is the ONLY one in
                 the block that does not, so without it the condition cannot
                 be asked at all.
  l19-s089_pos3  oral candidiasis on the tongue -- curd-like plaque on an
                 erythematous base, which is the description the slide gives.
                 The chart's candidiasis picture is a palate view where the
                 plaque is much harder to read.
  l19-s097_pos1  peritonsillar abscess WITHOUT the annotation. The deck's other
                 picture of it has "Right Tonsil / Displaced Uvula / Abscess /
                 Left Tonsil" drawn on in red.
  l19-s133_pos3  leukoplakia as a homogeneous white plaque. Deliberately NOT
                 s133_pos1/pos2, which show a lacy reticular pattern -- that is
                 what Wickham striae look like, and asking it as leukoplakia
                 would be teaching the wrong thing even though the deck files
                 those images under leukoplakia.

900 px wide rather than the folder's usual 600: these are the pictures the
student is asked to identify, and theme.js's click-to-enlarge is the point.
"""
import os
import sys
import zipfile
import importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
CHART = os.path.join(HERE, "extract_cms_e3_chart_images.py")

spec = importlib.util.spec_from_file_location("chart", CHART)
chart = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(chart)
except SystemExit:
    pass

OUT = chart.OUT
MAXW = 900

WANT = [
    ("l15", 34, 1),   # cholesteatoma -- the only un-annotated one in the block
    ("l15", 40, 2),   # auricular haematoma, second view
    ("l15", 43, 2),   # auricular laceration, the bleeding ear
    ("l15", 49, 2),   # foreign body in the canal -- the blue bead
    ("l15", 69, 2),   # keloid of the auricle, single lesion
    ("l17", 44, 2),   # epistaxis, anterior bleed
    ("l19", 10, 2),   # Fordyce granules on buccal mucosa
    ("l19", 83, 4),   # infectious mononucleosis, tonsillar exudate
    ("l19", 89, 3),   # oral candidiasis on the tongue
    ("l19", 97, 1),   # peritonsillar abscess, un-annotated
    ("l19", 122, 3),  # periodontitis
    ("l19", 133, 3),  # leukoplakia as a homogeneous plaque
    ("l19", 135, 2),  # erythroplakia
]


def main():
    os.makedirs(OUT, exist_ok=True)
    made, missing = 0, []
    for lec, slide, pos in WANT:
        name = "%s-s%03d_pos%d.jpg" % (lec, slide, pos)
        dest = os.path.join(OUT, name)
        z = zipfile.ZipFile(chart.DECKS[lec])
        pics = chart.pictures(z, slide)
        if len(pics) < pos:
            missing.append("%s (slide has %d picture(s))" % (name, len(pics)))
            continue
        chart.save(z, pics[pos - 1][2], dest, MAXW)
        made += 1
        print("  %s" % name)
    if missing:
        print("\nNOT FOUND -- the deck changed, re-run the audit:")
        for m in missing:
            print("  %s" % m)
        return 1
    print("\n%d image(s) written to %s" % (made, os.path.basename(OUT)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
