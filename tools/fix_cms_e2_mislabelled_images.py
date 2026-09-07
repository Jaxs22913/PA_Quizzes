#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-extract the six CMS Exam 2 chart photographs that were filed under the
wrong condition, naming each after WHAT IT IS instead of where it sat.

Jaxon, 2026-09-07: "on this part of exam 2 guide i think you got pteryingium
and pingicuium images mixed up". He was right, and the cause was systematic.

WHAT WENT WRONG. tools/extract_cms_e2_chart_images.py numbers each slide's
pictures with `enumerate(re.findall(...))` over the slide's .rels file. That is
neither rId order nor visual order -- PowerPoint writes relationships in
whatever order it likes. Slide 27's .rels reads rId3, rId2, rId1, rId5, rId4,
so the extractor produced s027_1 = image36 (the BOTTOM picture) and
s027_2 = image38 (the TOP one). EIGHTEEN of this deck's multi-image slides have
a .rels order that disagrees with reading order.

That alone is only a naming quirk. It became wrong content because slide 27
labels its photographs B, C and D in the pixels and captions them underneath --
so the ground truth was never the file number, it was the letter. The chart
ended up showing conjunctival intraepithelial neoplasia (the slide's own DDX,
letter D) as "Pinguecula", and the real pinguecula (letter B) as "Pterygium".
The actual pterygium, image37, was never extracted at all.

An audit of all 27 chart photographs against the slides' own letters and
ABOVE/BELOW/LEFT/RIGHT captions found five more of the same kind:

  Pinguecula     was image36 = letter D, "DDX Conjunctival intraepithelial
                 neoplasia"                              -> image38, letter B
  Pterygium      was image38 = letter B, the pinguecula   -> image37, letter C
  Chalazion      was image25 = the RIGHT of "LEFT External hordeolum RIGHT
                 Internal hordeolum"                      -> image26, letter B
  Hordeolum      was image28, a 128x114 thumbnail the slide never captions
                                                          -> image24, "LEFT
                 External hordeolum"
  Keratitis      was image68 = letter E, "scarred cornea as sequela" -- the end
                 state, not the disease                   -> image71, letter A,
                 "Bacterial keratitis. Hazy, can't see details of iris. Note
                 ciliary flush", which is what the chart row promises
  Corneal ulcer  was image75 = the "BELOW Scar (with calcification) of healed
                 corneal ulcer"                           -> image77, "ABOVE
                 Corneal ulcer in contact lens wearer appears as white spot"

Verified correct and left alone: entropion/ectropion (slide 12 ABOVE/BELOW),
dermatochalasis (one combined before/after picture), subconjunctival haemorrhage
(letter A), herpes simplex vs zoster keratitis (slide 57 -- the dendrite with
terminal end bulbs is on the left, the pseudodendrites on the right, and the
chart has them that way round), pre-septal cellulitis (white eye), scleritis
(violaceous hue), anterior uveitis (letter A).

Files are named after the CONDITION, not a position index, precisely so this
cannot recur: `l10-s027-pterygium.jpg` cannot silently come to mean something
else the way `s027_2.jpg` did. Verified by tools/check_ophtho_image_identity.py.

    python3 tools/fix_cms_e2_mislabelled_images.py
"""
import os, sys, zipfile
from io import BytesIO
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_cms_e2_chart_images import emf_dib

OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                   "cms-ophtho-chart-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2/"
    "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx")

# dest filename -> (slide, media file, the slide's own words for this picture)
WANT = {
 "l10-s027-pinguecula.jpg":
   (27, "image38.png", "B  Pinguecula confined to conjunctiva without corneal involvement"),
 "l10-s027-pterygium.jpg":
   (27, "image37.png", "C  Pterygium with characteristic triangular insect wing shape "
                       "with corneal involvement"),
 "l10-s027-conjunctival-neoplasia.jpg":
   (27, "image36.png", "D  DDX Conjunctival intraepithelial neoplasia -- kept only so the "
                       "REJECTED list can name a file that exists"),
 "l10-s020-chalazion.jpg":
   (20, "image26.emf", "B, of 'A, B  Chalazion'"),
 "l10-s020-hordeolum.jpg":
   (20, "image24.emf", "LEFT, of 'Hordeolum. LEFT External hordeolum RIGHT Internal hordeolum'"),
 "l10-s055-keratitis.jpg":
   (55, "image71.emf", "A  Bacterial keratitis. Hazy, can't see details of iris. "
                       "Note ciliary flush (limbus is NOT spared)"),
 "l10-s060-corneal-ulcer.jpg":
   (60, "image77.png", "ABOVE  Corneal ulcer in contact lens wearer appears as white spot "
                       "with surrounding corneal irregularity"),
}


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    z = zipfile.ZipFile(DECK)
    for dest, (slide, media, why) in sorted(WANT.items()):
        member = "ppt/media/" + media
        assert member in z.namelist(), "%s missing from the deck" % media
        data = z.read(member)
        if media.lower().endswith((".emf", ".wmf")):
            data = emf_dib(data)
            assert data is not None, "%s: metafile would not decode" % media
        im = Image.open(BytesIO(data)).convert("RGB")
        if im.width > 600:
            im = im.resize((600, round(im.height * 600 / im.width)), Image.LANCZOS)
        p = os.path.join(OUT, dest)
        im.save(p, "JPEG", quality=85, optimize=True)
        print("  %-40s slide %-3d %-13s %dx%d  %d KB"
              % (dest, slide, media, im.width, im.height, os.path.getsize(p) // 1024))
        print("      %s" % why)


if __name__ == "__main__":
    main()
