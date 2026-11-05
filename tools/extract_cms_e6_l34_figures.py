#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 34 (Acid-Base Part I, Prof. Finck) figures for the CMS I Exam 6 study guide.

    python3 tools/extract_cms_e6_l34_figures.py

Deck: "PAJ5500 CMSI Acid Base MBF 2026sc.pptx" (67 slides). Every slide was viewed at 1920 px before choosing.
Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e6_guide/l34.html
carries its slide number. Each picture is the deck's own embedded blob (transparency flattened onto white).

Taken:
  slide 11  the oxygen-hemoglobin dissociation curve (pH 7.6 / 7.4 / 7.2 curves and the "shift to right"
            list), a mechanism diagram that answers objective 2
  slide 63  the "acid-base disturbance suspected" algorithm (Pocket Guide to Diagnostic Tests), a flowchart that
            exists only as a picture; the guide already holds it as an HTML table in 2.7

Not pictures, so held as HTML tables instead: slide 6 (normal blood gas values, added to 2.1 slide-exact) and
slide 59 (the simple acid-base disorder summary, already in 2.6).

Left out:
  slides 12, 15, 16, 17, 18  clip art (lungs, kidney, laboratory flasks)
  slide 35  a paper bag in a "no" circle (decoration; the point is text in 2.5)
  slide 43  stock photograph of licorice
  slides 54, 55, 56  a pile of mud and a rusted truck (visual puns on MUDPILES and USEDCAR)
  slide 62  a warning-triangle icon; slide 63 McGraw-Hill/AccessMedicine logo strip; slide 4 a tiny icon
  slides 1, 2, 64-67  title, objectives, case-study and reference slides (no pictures)
"""
import io, os
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 6/"
                          "PAJ5500 CMSI Acid Base MBF 2026sc.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6", "cms-e6-images")
MAXW = 1400

# (slide, picture shape id, output name). A list of ids joins those pictures side by side.
FIGS = [
    (11, 11, "l34-s011-oxyhemoglobin-curve.png"),
    (63, 14349, "l34-s063-acid-base-algorithm.png"),
]

def walk(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes)
        else:
            yield sh


def picture(slide, shape_id):
    for sh in walk(slide.shapes):
        if sh.shape_id == shape_id:
            im = Image.open(io.BytesIO(sh.image.blob))
            im.load()
            if im.mode in ("RGBA", "LA", "P"):
                im = im.convert("RGBA")
                bg = Image.new("RGB", im.size, (255, 255, 255))
                bg.paste(im, mask=im.split()[3])
                im = bg
            else:
                im = im.convert("RGB")
            w, h = im.size
            l, t = round(sh.crop_left * w), round(sh.crop_top * h)
            r, b = w - round(sh.crop_right * w), h - round(sh.crop_bottom * h)
            return im.crop((max(l, 0), max(t, 0), min(r, w), min(b, h)))
    raise SystemExit("slide %d: no picture with shape id %s" % (slide.slide_id, shape_id))


def side_by_side(ims, gap=24):
    hh = min(i.height for i in ims)
    ims = [i.resize((round(i.width * hh / i.height), hh), Image.LANCZOS) for i in ims]
    out = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), hh), (255, 255, 255))
    x = 0
    for i in ims:
        out.paste(i, (x, 0))
        x += i.width + gap
    return out


def save(im, name):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    path = os.path.join(OUT, name)
    if name.endswith(".png"):  # line art and tables: a 128-color palette keeps them small and sharp
        im.convert("P", palette=Image.ADAPTIVE, colors=128).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    print("%-44s %4dx%-4d %6.1f KB" % (name, im.width, im.height, os.path.getsize(path) / 1024))


def main():
    os.makedirs(OUT, exist_ok=True)
    slides = list(Presentation(DECK).slides)
    for n, sid, name in FIGS:
        s = slides[n - 1]
        im = side_by_side([picture(s, i) for i in sid]) if isinstance(sid, list) else picture(s, sid)
        save(im, name)


if __name__ == "__main__":
    main()
