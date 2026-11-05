#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 33 (Oxygen Delivery, Prof. Reynolds) figures for the CMS I Exam 6 study guide.

    python3 tools/extract_cms_e6_l33_figures.py

Deck: "35. Oxygen Delivery 2026.pptx" (27 slides). Every slide was viewed at 1920 px before choosing.
Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e6_guide/l33.html
carries its slide number. Each picture is the deck's own embedded blob (the slide's crop applied, any
transparency flattened onto white), never redrawn.

Taken:
  slide 6   the home oxygen qualification table, which exists on the slide only as a picture (the guide also
            holds it as an HTML table, slide-exact)
  slide 10  nasal cannula            slide 12  simple mask            slide 15  non-rebreather mask
  slide 16  Venturi mask (with its colored ports)
  slide 18  aerosol mask and open face mask (the two air-entrainment nebulizer interfaces the slide names)
  slide 19  tracheostomy collar
  slide 21  the three advanced-airway photographs: oropharyngeal airways (size labels), nasopharyngeal
            airways, endotracheal tubes
  slide 22  the endotracheal tube changer and the bougie, set side by side as one picture (the slide names
            both but does not label which photograph is which, so neither is captioned alone)
  slide 23  laryngeal mask airway
  slide 24  the nebulizer set and the nebulizer compressor

Left out:
  slide 4   stock photograph of a person wheeling an oxygen cylinder (decoration)
  slide 7   "Home Oxygen Safety" poster with a stock model photograph; every rule on it is already text in 1.7
  slide 14  the partial rebreather photograph is the same product photograph as slide 15's non-rebreather
            (a duplicate; it cannot show the difference between the two masks)
  slide 24  stock photograph of a child under a nebulizer mask; a dog-shaped children's compressor (product)
  slide 25  stock photograph of a pulse oximeter on a finger (decoration)
  slides 1, 2, 26, 27  title, objectives, questions, references
"""
import io, os
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 6/"
                          "35. Oxygen Delivery 2026.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6", "cms-e6-images")
MAXW = 1400

# (slide, picture shape id, output name). A list of ids joins those pictures side by side.
FIGS = [
    (6, 12, "l33-s006-home-oxygen-table.png"),
    (10, 1026, "l33-s010-nasal-cannula.jpg"),
    (12, 2050, "l33-s012-simple-mask.jpg"),
    (15, 5, "l33-s015-non-rebreather-mask.jpg"),
    (16, 5, "l33-s016-venturi-mask.jpg"),
    (18, 1026, "l33-s018-aerosol-mask.jpg"),
    (18, 1027, "l33-s018-open-face-mask.jpg"),
    (19, 2052, "l33-s019-trach-collar.jpg"),
    (21, 5, "l33-s021-oropharyngeal-airways.jpg"),
    (21, 6, "l33-s021-nasopharyngeal-airways.jpg"),
    (21, 7, "l33-s021-endotracheal-tubes.jpg"),
    (22, [4, 5122], "l33-s022-tube-changer-and-bougie.jpg"),
    (23, 4, "l33-s023-laryngeal-mask-airway.jpg"),
    (24, 5, "l33-s024-nebulizer-set.jpg"),
    (24, 7, "l33-s024-nebulizer-compressor.jpg"),
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
