#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 15 and 16 (ENT) chart images.

ORDERED BY POSITION ON THE SLIDE, not by relationship order -- the same trap
recorded in [[lettered_slide_images]] and handled the same way as the Lecture 14
extractor: l15-sNNN_posK.jpg, top-to-bottom then left-to-right.

TWO DECKS, SO THE PREFIX IS NOT OPTIONAL. Lecture 15 has 72 slides and Lecture
16 has 99; they number independently, so a bare sNNN would collide on more than
sixty slides.

Run with --all to dump every picture in both decks into the scratchpad for
review. Nothing is assigned to a chart row until it has been LOOKED AT --
this block's decks put unlabelled differential photographs beside the real
thing exactly as the ophthalmology deck did.
"""
import os, re, sys, zipfile
from xml.etree import ElementTree as ET
from io import BytesIO
from PIL import Image

P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 3",
                   "cms-ent-chart-images")
REVIEW = ("/private/tmp/claude-501/-Users-jaxonluke/"
          "8623a091-045a-42b8-8052-ca7d2eb04188/scratchpad/ent-images")
INBOX = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 3")
DECKS = {
  "l15": os.path.join(INBOX, "Disorders External and Middle Ear 9-2026.pptx"),
  "l16": os.path.join(INBOX, "16. Disorders of Inner Ear 2026 - Dr. Jaquith.pptx"),
  "l17": os.path.join(INBOX, "hughie Nose & Paranasal Sinuses fall 2026.pptx"),
}
ROW_TOL = 400000          # EMU; two pictures within this are the same visual row

# Filled in after the review pass. EVERY ONE OF THE 77 PICTURES IN THE TWO
# DECKS WAS VIEWED on a contact sheet before anything was assigned, and the
# three image-only slides were resolved against the slide BEFORE them:
#   L16 slide 49 follows "Exostosis"     -> exostoses, not a normal canal
#   L16 slide 51 follows "Glomus Tumors" -> the vascular middle ear mass
#   L16 slide 59 follows "Barotrauma"    -> haemotympanum
# Getting those wrong was the live risk: all three carry no caption at all.
# See [[image_only_slides]].
#
# WHAT IS DELIBERATELY LEFT OUT. Slide 29 of Lecture 15 is five product
# photographs (Debrox, a Walgreens kit, an irrigation tip, curettes), slide 50
# is a tray of instruments and slide 60 is a two-part drug table -- treatment
# kit, not a picture of a disease. Lecture 16 slides 7, 37, 38, 55 and 98 are
# stock cartoons and a meme. None of those belong in a cell that says "this is
# what the condition looks like". The Lecture 15 slide 58 canal photograph with
# pale streaks across it is also skipped: it is otitis externa by its slide,
# but it reads as fungal at thumbnail size and sits two slides from the real
# otomycosis picture.
WANT = {
  "l15": {9: [1], 16: [1, 2], 26: [2], 35: [2], 40: [1], 43: [1], 47: [1],
          49: [1], 52: [1], 58: [2], 61: [1], 63: [1], 65: [1], 69: [1]},
  "l16": {5: [1], 19: [1], 39: [1], 43: [1], 49: [2], 51: [1], 59: [1], 73: [1]},
  # Lecture 17. All 47 pictures were viewed on contact sheets first. Left out:
  # the neti-pot and saline-spray product shots (24, 25), the instrument table
  # (55), the before/after cosmetic septoplasty pairs (33, 34) which show a
  # RESULT rather than a finding, and the "nasal packing" title card (52 pos1).
  "l17": {7: [1], 15: [1], 36: [1], 38: [1], 42: [1, 2], 44: [1], 47: [2],
          52: [2], 53: [2], 58: [3], 61: [1], 62: [1], 63: [1]},
}


def pictures(z, slide):
    root = ET.fromstring(z.read("ppt/slides/slide%d.xml" % slide))
    rels = {r.get("Id"): r.get("Target") for r in
            ET.fromstring(z.read("ppt/slides/_rels/slide%d.xml.rels" % slide))}
    out = []
    for pic in root.iter(P + 'pic'):
        blip = pic.find('.//' + A + 'blip')
        xfrm = pic.find('.//' + A + 'xfrm')
        if blip is None or xfrm is None:
            continue
        off = xfrm.find(A + 'off')
        tgt = rels.get(blip.get(R + 'embed'))
        if not tgt:
            continue
        out.append((int(off.get('y')), int(off.get('x')), tgt.split("/")[-1]))
    out.sort(key=lambda t: (round(t[0] / ROW_TOL), t[1]))   # reading order
    return out


def save(z, src, dest, width=600):
    raw = z.read("ppt/media/" + src)
    try:
        im = Image.open(BytesIO(raw))
    except Exception as e:
        print("  ! cannot decode %s (%s)" % (src, e))
        return False
    im = im.convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    im.save(dest, "JPEG", quality=80)
    return True


def main():
    dump_all = "--all" in sys.argv
    target = REVIEW if dump_all else OUT
    os.makedirs(target, exist_ok=True)
    total = 0
    for pref, deck in DECKS.items():
        assert os.path.exists(deck), "deck not found: %s" % deck
        z = zipfile.ZipFile(deck)
        n_slides = len([n for n in z.namelist()
                        if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)])
        for s in range(1, n_slides + 1):
            pics = pictures(z, s)
            for k, (_y, _x, src) in enumerate(pics, 1):
                if not dump_all and k not in WANT[pref].get(s, []):
                    continue
                fn = "%s-s%03d_pos%d.jpg" % (pref, s, k)
                if save(z, src, os.path.join(target, fn)):
                    total += 1
        z.close()
    print("wrote %d images to %s" % (total, target))


if __name__ == "__main__":
    main()
