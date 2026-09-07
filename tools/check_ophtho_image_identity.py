#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove every CMS Exam 2 ophthalmology photograph is the condition it is filed under.

Jaxon spotted the pinguecula and pterygium pictures swapped in the Exam 2 guide
on 2026-09-07. The cause was not a typo. tools/extract_cms_e2_chart_images.py
numbers a slide's pictures by their order in the slide's .rels file, and
PowerPoint writes relationships in arbitrary order -- slide 27's reads
rId3, rId2, rId1, rId5, rId4. EIGHTEEN of this deck's multi-image slides have a
.rels order that disagrees with reading order, so `s027_2.jpg` is not "the
second picture on slide 27" and never was.

Where a slide labels its own photographs -- letters burnt into the layout, or
ABOVE/BELOW/LEFT/RIGHT in the caption -- THAT is the ground truth, not the file
number. This check enforces it:

  1. every file the chart references exists;
  2. every REJECTED filename exists, because a rejection naming a missing file
     silently rejects nothing (that is exactly how conjunctival intraepithelial
     neoplasia shipped as "Pinguecula");
  3. every condition whose picture is pinned below still resolves to the media
     file the slide's own caption assigns to it.

The pinned map is what a human verified by eye against the slide captions. If a
re-extraction renumbers anything, this fails instead of quietly relabelling a
disease -- see [[image_only_slides]] and [[lettered_slide_images]].

    python3 tools/check_ophtho_image_identity.py
"""
import os, re, sys, zipfile, hashlib
from io import BytesIO

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_cms_e2_chart_images import emf_dib
from PIL import Image

IMGDIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                      "cms-ophtho-chart-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2/"
    "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx")

# condition -> (media file in the deck, the slide's own words for that picture)
# Verified by eye against the slide captions on 2026-09-07.
PINNED = {
 "Pinguecula":       ("image38.png", "slide 27 letter B, 'Pinguecula confined to conjunctiva "
                                     "without corneal involvement'"),
 "Pterygium":        ("image37.png", "slide 27 letter C, 'Pterygium ... with corneal involvement'"),
 "Chalazion":        ("image26.emf", "slide 20 letter B, of 'A, B  Chalazion'"),
 "Hordeolum (stye)": ("image24.emf", "slide 20, LEFT of 'LEFT External hordeolum RIGHT Internal "
                                     "hordeolum'"),
 "Keratitis":        ("image71.emf", "slide 55 letter A, 'Bacterial keratitis ... Note ciliary "
                                     "flush'"),
 "Corneal ulcer":    ("image77.png", "slide 60, 'ABOVE  Corneal ulcer in contact lens wearer'"),
 "Entropion":        ("image15.emf", "slide 12, ABOVE of 'ABOVE Entropion, BELOW Ectropion'"),
 "Ectropion":        ("image16.png", "slide 12, BELOW of 'ABOVE Entropion, BELOW Ectropion'"),
 "Subconjunctival haemorrhage":
                     ("image41.emf", "slide 29 letter A, 'Atraumatic subconjunctival hemorrhage'"),
 "Herpes simplex keratitis":
                     ("image73.png", "slide 57, the dendrite with terminal end bulbs"),
 "Herpes zoster keratitis":
                     ("image74.png", "slide 57, the pseudodendrites without end bulbs"),
 "Anterior uveitis (iritis, iridocyclitis)":
                     ("image79.png", "slide 62 letter A, 'Ciliary flush and irregularly shaped "
                                     "pupil'"),
 "Pre-septal (periorbital) cellulitis":
                     ("image63.emf", "slide 52, 'eye itself is white'"),
}


def deck_pixels(z, media):
    data = z.read("ppt/media/" + media)
    if media.lower().endswith((".emf", ".wmf")):
        data = emf_dib(data)
        if data is None:
            return None
    return Image.open(BytesIO(data)).convert("RGB")


def close(a, b):
    """Same picture, allowing for the resize and JPEG round trip."""
    b = b.resize(a.size, Image.LANCZOS)
    n = a.size[0] * a.size[1]
    tot = 0
    for ca, cb in zip(a.split(), b.split()):
        tot += sum(abs(x - y) for x, y in zip(ca.getdata(), cb.getdata())) / n
    return tot / 3 < 12.0


def main():
    src = open(os.path.join(HERE, "build_cms_ophtho_chart.py"), encoding="utf-8").read()
    IMGS = eval(re.search(r"^IMGS = (\{.*?\})$", src, re.M | re.S).group(1))
    REJECTED = eval(re.search(r"^REJECTED = (\{.*?\n\})", src, re.M | re.S).group(1))
    z = zipfile.ZipFile(DECK)
    bad = []

    for cond, (fn, _sl) in sorted(IMGS.items()):
        if not os.path.exists(os.path.join(IMGDIR, fn)):
            bad.append("%s: file %s does not exist" % (cond, fn))

    # No chart picture may BE one of the deck's own differential images, whatever
    # filename it arrives under.
    used = {}
    for cond, (fn, _sl) in sorted(IMGS.items()):
        path = os.path.join(IMGDIR, fn)
        if os.path.exists(path):
            used[cond] = Image.open(path).convert("RGB")
    for media, why in sorted(REJECTED.items()):
        ref = deck_pixels(z, media)
        if ref is None:
            print("  note: %s will not decode, so it cannot be matched against" % media)
            continue
        for cond, im in used.items():
            if close(im, ref):
                bad.append("%s is showing a REJECTED image: %s" % (cond, why))

    checked = 0
    for cond, (media, why) in sorted(PINNED.items()):
        fn = IMGS.get(cond, (None,))[0]
        if fn is None:
            bad.append("%s: pinned, but the chart no longer has a picture for it" % cond)
            continue
        path = os.path.join(IMGDIR, fn)
        if not os.path.exists(path):
            continue
        want = deck_pixels(z, media)
        if want is None:
            bad.append("%s: %s would not decode from the deck" % (cond, media))
            continue
        if not close(Image.open(path).convert("RGB"), want):
            bad.append("%s is showing the WRONG PICTURE.\n      %s is not %s\n      should be %s"
                       % (cond, fn, media, why))
        checked += 1

    print("chart pictures: %d   pinned and verified against the deck: %d" % (len(IMGS), checked))
    if bad:
        print("\nPROBLEMS:")
        for b in bad:
            print("  " + b)
        return 1
    print("every pinned photograph is the condition it is filed under")
    return 0


if __name__ == "__main__":
    sys.exit(main())
