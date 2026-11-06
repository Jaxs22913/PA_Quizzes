#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draw the yellow highlight boxes into the Pulmonary OSCE chart's test
pictures, the way the Cardiac OSCE chart's 12-leads are boxed (Jaxon,
2026-11-06: "If it calls for anything like X-ray, EKG or whatever include it
like you did for the cardiac one and explain it").

Reads the clean pictures from outside the repo (written by
tools/extract_pd2_pulm_osce_images.py), writes the boxed ones into
Physical Diagnosis 2 Exam 2/pd2-pulm-osce-images/. Boxes are drawn into the
pixels, not overlaid in HTML, so the click-to-enlarge view, the PDF and the
Word copy all show them. Box coordinates live in _pd2_pulm_osce_images.

    python3 tools/box_pd2_pulm_osce_images.py [--clean DIR] [--preview DIR]
"""
import argparse, os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pd2_pulm_osce_images import IMAGES, PICS

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(_REPO, "Physical Diagnosis 2 Exam 2", "pd2-pulm-osce-images")
CLEAN = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Physical Diagnosis 2 Inbox/"
                           "Pulm OSCE images (clean)")
EDGE = (245, 190, 0)          # the cardiac chart's highlighter yellow
FILL = (255, 221, 0, 40)      # a light wash, so the film under it stays readable
# Dark films (CT, black backgrounds) and color pictures read better with the outline alone.
NO_WASH = {"ct-pneumothorax.jpg", "ct-consolidation.jpg", "ct-hypersensitivity-pneumonitis.jpg",
           "ct-lung-tumor.jpg", "pet-ct-nodule.jpg", "hrct-honeycombing.jpg", "vq-scan-and-ct-angiogram.jpg",
           "tuberculin-skin-test-reading.jpg", "cxr-copd-hyperinflation.jpg", "cxr-pulmonary-edema.jpg"}


def boxed(src, boxes, wash_on=True):
    im = Image.open(src).convert("RGB")
    w = max(3, round(max(im.width, im.height) / 260))
    wash = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(wash)
    for x0, y0, x1, y1 in boxes:
        assert 0 <= x0 < x1 <= im.width and 0 <= y0 < y1 <= im.height, \
            "%s: box %r falls outside %r" % (os.path.basename(src), (x0, y0, x1, y1), im.size)
        if wash_on:
            d.rectangle((x0, y0, x1, y1), fill=FILL)
    im = Image.alpha_composite(im.convert("RGBA"), wash).convert("RGB")
    d = ImageDraw.Draw(im)
    for x0, y0, x1, y1 in boxes:
        d.rounded_rectangle((x0, y0, x1, y1), radius=max(4, w * 2), outline=EDGE, width=w)
    return im


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--clean", default=CLEAN)
    ap.add_argument("--preview", help="write here instead of the site folder")
    a = ap.parse_args()
    used = {p["file"] for ps in PICS.values() for p in ps if p.get("file")}
    assert used == set(IMAGES), "pictures without a row, or rows without a picture: %r" % (used ^ set(IMAGES))
    out = a.preview or OUT
    os.makedirs(out, exist_ok=True)
    for fn, (_, boxes) in sorted(IMAGES.items()):
        src = os.path.join(a.clean, fn)
        assert os.path.exists(src), "clean picture missing: %s" % src
        im = boxed(src, boxes, fn not in NO_WASH)
        dst = os.path.join(out, fn)
        if fn.endswith(".png"):
            im.save(dst, "PNG", optimize=True)
        else:
            im.save(dst, "JPEG", quality=86, optimize=True, progressive=True)
        print("%-42s %d box%s" % (fn, len(boxes), "" if len(boxes) == 1 else "es"))


if __name__ == "__main__":
    main()
