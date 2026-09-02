#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 14 (Ocular Trauma) chart images.

ORDERED BY POSITION ON THE SLIDE, NOT BY RELATIONSHIP ORDER. The Lecture 11/12
extractor numbers images by the order they appear in the slide's .rels, and
that order does NOT match where they sit on the slide -- the trap recorded in
[[lettered_slide_images]]. This deck labels its pictures by POSITION in the
speaker notes ("Upper left", "Bottom left 1", "Top middle"), so the filename
carries the reading-order position instead: l14-sNNN_posK.jpg, top-to-bottom
then left-to-right.

AND THE NOTES THEMSELVES DO NOT MAP BY INDEX. All nine notes in this deck
belong to a different slide than their notesSlideN number suggests; they are
resolved through each slide's .rels here. Getting that wrong would have put
the orbital-fracture labels on the hyphema slide.

Downscaled to 600 px wide, JPEG quality 80 -- the same treatment the other
lectures' chart images get. The chart displays them at 180 px.
"""
import os, re, zipfile
from xml.etree import ElementTree as ET
from io import BytesIO
from PIL import Image

P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                   "cms-ophtho-chart-images")
DECK = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/"
                          "Exam 2/CMS I Ocular Trauma - Shah Fallsv.pptx")

# Only the slides whose pictures a chart row or the guide actually uses.
WANT = [15, 17, 18, 21, 24, 27, 32, 34, 37, 38, 40, 42, 45, 46]
ROW_TOL = 400000          # EMU; two pictures within this are the same visual row


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
        src = rels[blip.get(R + 'embed')].split("/")[-1]
        out.append((int(off.get('y')), int(off.get('x')), src))
    out.sort(key=lambda t: (round(t[0] / ROW_TOL), t[1]))   # reading order
    return out


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    os.makedirs(OUT, exist_ok=True)
    z = zipfile.ZipFile(DECK)
    n = 0
    for slide in WANT:
        for k, (_y, _x, src) in enumerate(pictures(z, slide), 1):
            member = "ppt/media/" + src
            if member not in z.namelist():
                continue
            im = Image.open(BytesIO(z.read(member))).convert("RGB")
            if im.width > 600:
                im = im.resize((600, round(im.height * 600 / im.width)), Image.LANCZOS)
            dest = os.path.join(OUT, "l14-s%03d_pos%d.jpg" % (slide, k))
            im.save(dest, "JPEG", quality=80, optimize=True)
            n += 1
            print("  l14-s%03d_pos%d.jpg  (%s, %d KB)"
                  % (slide, k, src, os.path.getsize(dest) // 1024))
    print("%d image(s) written to %s" % (n, os.path.basename(OUT)))


if __name__ == "__main__":
    main()
