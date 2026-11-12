#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 45 (Acid-Base Disorders II, Prof. Finck) figures for the CMS I Exam 7 study guide.

    python3 tools/extract_cms_e7_l45_figures.py [RENDER_DIR]

Deck: "PAJ5510 Acid Base Disorders II MBF2026sc.pptx" (64 slides). Every slide was viewed at 1920 px before
choosing. Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e7_guide/l45.html
carries its slide number. Embedded pictures are the deck's own blobs (transparency flattened onto white).

Taken (embedded blobs):
  slide 25  the acid-base nomogram (Harrison's, via the slide): arterial pH against plasma bicarbonate with carbon
            dioxide isobars and the shaded bands for each simple disorder. She said to CALCULATE on the exam, not read
            the nomogram, so the guide shows it as a picture only.
  slide 58  "Figure 1: Identifying the Primary Process" flowchart (pH low / normal / high, then carbon dioxide and
            bicarbonate). The blob is small (513 px wide) and is kept at its own size.
  slide 59  "Evaluation of Acid-Base Disturbances" flowchart (Pearson 2011): pH below 7.35 or above 7.45, then
            bicarbonate against 24 mM or carbon dioxide against 40 mm Hg, then the expected compensation.

Taken (cropped from the 1920 px Keynote render, because the content is not one picture):
  slide 43  the whole slide, MUDPILES beside a pile of mud and USEDCAR beside a rusted truck: her memory aid, the
            same art as Lecture 34's slide 54 (l34-s054-mudpiles-usedcar.jpg). Box (110, 95, 1560, 940), JPEG 85.
  slide 50  the change in anion gap against the change in bicarbonate rules, typeset as equations (no text the
            extractor can read); the guide also holds them as an HTML table. Box (90, 50, 1660, 945), PNG.
  The render folder defaults to the session scratchpad's render/l45_hi (sNNN.png). Without it the two crops are
  skipped (the files already written are kept).

Not pictures, so held as HTML tables instead: slide 6 (normal blood gas values), 10 (identifying the primary
disorder), 24 (compensation summary), 27 (change in anion gap, change in bicarbonate; text in equation objects, the
same rules as slide 50), 28-30 (mixed-disorder tables with their examples), 44-48 (cause lists).

Left out:
  slides 15, 16, 17  laboratory flasks, lungs and kidney clip art beside the buffering equation (the equation is text)
  slides 18, 19      lungs and kidney clip art (decoration)
  slide 44           the mud pile again plus a pair of pliers beside the MUDPILES list (the guide's text notes the
                     slide's bolded R of renal failure and rhabdomyolysis; slide 43's picture already carries the art)
  slide 46           the rusted truck again (slide 43 carries it)
  slides 11, 13, 20-22, 31-42, 45, 47-55, 63  small vector icons ("Graphic" shapes, no raster image); decoration
  slides 1, 2, 60-62, 64  title, objectives, case-study titles, external links, references (no pictures)
"""
import io, os, sys
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 7/"
                          "PAJ5510 Acid Base Disorders II MBF2026sc.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-e7-images")
RENDER = (sys.argv[1] if len(sys.argv) > 1 else
          "/private/tmp/claude-501/-Users-jaxonluke/e06779a5-ab02-4065-a6fc-fe88e20d1bfd/scratchpad/render/l45_hi")
MAXW = 1400

# (slide, picture shape id, output name)
FIGS = [
    (25, 4, "l45-s025-nomogram.png"),
    (58, 78850, "l45-s058-primary-process-flowchart.png"),
    (59, 5122, "l45-s059-evaluation-flowchart.jpg"),
]
# (slide, crop box on the 1920 px render, output name)
CROPS = [
    (43, (110, 95, 1560, 940), "l45-s043-mudpiles-usedcar.jpg"),
    (50, (90, 50, 1660, 945), "l45-s050-change-in-gap-rules.png"),
]


def walk(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes)
        else:
            yield sh


def flatten(im):
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        return bg
    return im.convert("RGB")


def picture(slide, n, shape_id):
    for sh in walk(slide.shapes):
        if sh.shape_id == shape_id:
            im = flatten(Image.open(io.BytesIO(sh.image.blob)))
            w, h = im.size
            l, t = round(sh.crop_left * w), round(sh.crop_top * h)
            r, b = w - round(sh.crop_right * w), h - round(sh.crop_bottom * h)
            return im.crop((max(l, 0), max(t, 0), min(r, w), min(b, h)))
    raise SystemExit("slide %d: no picture with shape id %s" % (n, shape_id))


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
        save(picture(slides[n - 1], n, sid), name)
    for n, box, name in CROPS:
        src = os.path.join(RENDER, "s%03d.png" % n)
        if not os.path.exists(src):
            print("skip %s (no render at %s)" % (name, src))
            continue
        save(flatten(Image.open(src)).crop(box), name)


if __name__ == "__main__":
    main()
