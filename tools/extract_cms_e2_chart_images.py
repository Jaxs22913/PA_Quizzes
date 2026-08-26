#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract the CMS I Exam 2 ophthalmology chart images from the lecture deck.

STANDING RULE, per [[media_asset_licensing]]: any image in a course PowerPoint
may be used in PA_Quizzes content <b>as long as the slide is cited</b>. Marks
baked into the pixels -- EYEROUNDS.ORG, "(c) 2011 Logical Images, Inc." -- are
LEFT VISIBLE on purpose; they ride along as part of citing the slide. Every row
of the chart prints its deck and slide number.

SIXTEEN OF THIS DECK'S CLINICAL PHOTOGRAPHS ARE STORED AS .emf METAFILES that
CoreGraphics cannot open. They are decoded through the same EMR_STRETCHDIBITS
path tools/ocr_deck_images.py uses -- without it the entropion, dermatochalasis,
xanthelasma, chalazion, subconjunctival haemorrhage, episcleritis, scleritis,
cellulitis, keratitis and uveitis pictures would all be missing.

EVERY IMAGE IS VIEWED BEFORE IT IS ASSIGNED TO A ROW, per [[image_only_slides]].
This deck in particular labels several pictures "DDX" in the slide caption --
slide 27 carries conjunctival intraepithelial neoplasia as a differential, and
slide 29 carries traumatic haemorrhage and hyphaema as differentials. Filing one
of those under the row's own condition would be a factual error in the chart,
not merely an ugly picture.
"""
import os, re, struct, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                   "cms-ophtho-chart-images")
DECK = os.path.expanduser(
    "~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2/"
    "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx")
EMR_STRETCHDIBITS = 81


def emf_dib(data):
    off = 0
    while off + 8 <= len(data):
        itype, nsize = struct.unpack_from("<II", data, off)
        if nsize < 8:
            break
        if itype == EMR_STRETCHDIBITS and off + 64 <= len(data):
            ob, cb, obits, cbits = struct.unpack_from("<IIII", data, off + 48)
            if cb and cbits and off + obits + cbits <= len(data):
                bmi = data[off + ob: off + ob + cb]
                bits = data[off + obits: off + obits + cbits]
                return (b"BM" + struct.pack("<IHHI", 14 + len(bmi) + len(bits),
                                            0, 0, 14 + len(bmi)) + bmi + bits)
        off += nsize
    return None


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    os.makedirs(OUT, exist_ok=True)
    z = zipfile.ZipFile(DECK)
    n_img = n_emf = 0
    for i in range(1, 74):
        rel = "ppt/slides/_rels/slide%d.xml.rels" % i
        if rel not in z.namelist():
            continue
        for k, name in enumerate(re.findall(r'Target="\.\./media/([^"]+)"',
                                            z.read(rel).decode("utf8", "replace")), 1):
            member = "ppt/media/" + name
            if member not in z.namelist():
                continue
            data = z.read(member)
            ext = name.rsplit(".", 1)[-1].lower()
            if ext in ("emf", "wmf"):
                dib = emf_dib(data)
                if dib is None:
                    continue
                data, ext = dib, "bmp"
                n_emf += 1
            elif ext not in ("png", "jpg", "jpeg"):
                continue
            if len(data) < 12000:
                continue
            with open(os.path.join(OUT, "s%03d_%d.%s" % (i, k, ext)), "wb") as fh:
                fh.write(data)
            n_img += 1
    print("wrote %d images (%d decoded from metafiles)" % (n_img, n_emf))


if __name__ == "__main__":
    main()
