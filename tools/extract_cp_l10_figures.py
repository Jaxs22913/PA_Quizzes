#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract the Lecture 10 (Pathophysiology of Blood Disorders) guide figures.

Two kinds, every one viewed at full size before it was chosen (image_only_slides,
guide_teaching_images_rule):

  MEDIA  pictures stored in the deck, read straight out of the .pptx by slide number with
         extract_cp_e2_figures.slide_media as the guard, so the cited slide can never drift.
  CROPS  three diagrams the deck draws with native shapes (slide 5 lineage, slide 24 B- and
         T-cell development, slide 43 coagulation key reactions), which exist as no picture
         file. They are cropped from a Keynote PDF export of the deck rendered at 1920 px:
             python3 tools/extract_cp_l10_figures.py /path/to/deck-export.pdf
         Without the PDF argument only the MEDIA figures are written.

The deck's tables (slides 8, 18, 22, 33, 34, 46, 50) are rebuilt as HTML tables in the guide
rather than shipped as pictures of text.
"""
import io, os, sys, zipfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_cp_e2_figures import slide_media, OUTDIR, INBOX, MAXW

L10 = os.path.join(INBOX, "Pathophysiology of Blood Disorders SV Fall 2026.pptx")
D = "cp-exam-2-l10-images/"

MEDIA = [
    (4, "image3.jpg", "marrow-hematopoiesis.jpg"),
    (6, "image4.gif", "wbc-distribution.png"),
    (9, "image5.jpg", "neutrophils-smear.jpg"),
    (10, "image6.png", "band-neutrophil.png"),
    (11, "image9.png", "monocyte.png"),
    (12, "image11.jpg", "eosinophil.jpg"),
    (13, "image13.jpg", "basophil.jpg"),
    (14, "image15.jpg", "lymphocyte.jpg"),
    (15, "image16.jpg", "b-cell-development.jpg"),
    (16, "image18.jpg", "clonality-pcr.jpg"),
    (26, "image21.png", "neoplasm-lineages.png"),
    (39, "image22.jpeg", "spherocytosis-sequence.jpg"),
]
# (slide, (left, top, right, bottom) as fractions of the slide, output)
CROPS = [
    (5, (0.02, 0.17, 0.97, 0.98), "hematopoiesis-lineage.png"),
    (24, (0.06, 0.18, 0.92, 0.99), "b-t-development.png"),
    (43, (0.05, 0.22, 0.97, 0.98), "coagulation-reactions.png"),
]


def main():
    z = zipfile.ZipFile(L10)
    os.makedirs(os.path.join(OUTDIR, D), exist_ok=True)
    for slide, media, out in MEDIA:
        assert media in slide_media(z, slide), "%s is not on slide %d" % (media, slide)
        im = Image.open(io.BytesIO(z.read("ppt/media/" + media))).convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        p = os.path.join(OUTDIR, D, out)
        im.save(p, optimize=True) if out.endswith(".png") else im.save(p, quality=85, optimize=True)
        print("%-48s %4dx%-4d slide %d" % (D + out, im.width, im.height, slide))
    if len(sys.argv) > 1:
        import pymupdf
        doc = pymupdf.open(sys.argv[1])
        assert len(doc) == 51, "expected the 51-slide deck export"
        for slide, (l, t, r, b), out in CROPS:
            page = doc[slide - 1]
            zoom = 1920 / page.rect.width
            pix = page.get_pixmap(matrix=pymupdf.Matrix(zoom, zoom))
            im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
            im = im.crop((round(l * im.width), round(t * im.height), round(r * im.width), round(b * im.height)))
            if im.width > MAXW:
                im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
            im.save(os.path.join(OUTDIR, D, out), optimize=True)
            print("%-48s %4dx%-4d slide %d (crop)" % (D + out, im.width, im.height, slide))


if __name__ == "__main__":
    main()
