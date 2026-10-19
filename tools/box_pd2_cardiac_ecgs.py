#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Draw the yellow highlight boxes into the Cardiac OSCE chart's 12-lead
pictures (Jaxon, 2026-10-19: "put like a highlight yellow box around the leads
where the changes occur").

Reads the clean pictures from outside the repo, writes the boxed ones into
Physical Diagnosis 2 Exam 1/pd2-cardiac-osce-chart-images/. Boxes are drawn
into the pixels, not overlaid in HTML, so the click-to-enlarge view, the PDF
and the Word copy all show them. Box coordinates live in _pd2_cardiac_osce_ecgs.

    python3 tools/box_pd2_cardiac_ecgs.py [--clean DIR] [--preview DIR]
"""
import argparse, os, sys
from PIL import Image, ImageDraw

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pd2_cardiac_osce_ecgs import IMAGES, ECGS

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(_REPO, "Physical Diagnosis 2 Exam 1", "pd2-cardiac-osce-chart-images")
CLEAN = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Physical Diagnosis 2 Inbox/"
                           "Cardiac OSCE ECGs (clean)")
EDGE = (245, 190, 0)          # highlighter yellow, dark enough to read on white and pink paper
FILL = (255, 221, 0, 48)      # a light wash, so the tracing under it stays crisp
# A photographed tracing on brown paper turns olive under the wash: outline only.
NO_WASH = {"ecg-pvc-bigeminy.jpg"}


def boxed(src, boxes, wash_on=True):
    im = Image.open(src).convert("RGB")
    w = max(3, round(im.width / 400))
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
    used = {e["file"] for e in ECGS.values()}
    assert used == set(IMAGES), "pictures without a row, or rows without a picture: %r" % (used ^ set(IMAGES))
    out = a.preview or OUT
    os.makedirs(out, exist_ok=True)
    for fn, (_, boxes) in sorted(IMAGES.items()):
        src = os.path.join(a.clean, fn)
        assert os.path.exists(src), "clean picture missing: %s" % src
        boxed(src, boxes, fn not in NO_WASH).save(os.path.join(out, fn), "JPEG", quality=86, optimize=True, progressive=True)
        print("%-40s %d box%s" % (fn, len(boxes), "" if len(boxes) == 1 else "es"))


if __name__ == "__main__":
    main()
