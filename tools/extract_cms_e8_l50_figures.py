#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 50 (Hematologic Malignancies Part II, Nicole Gannon) figures for the CMS I Exam 8 study guide.

    python3 tools/extract_cms_e8_l50_figures.py [RENDER_DIR]

Deck: "50. Hematologic Malignancies Part II - Gannon.pptx" (58 slides). Every slide was viewed at 1920 px before
choosing. Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e8_guide/l50.html
carries its slide number. Most figures are the deck's own picture blobs (cropped as the slide crops them,
transparency flattened onto white). Three slides draw a marker ON TOP of the picture as a separate slide shape (the
circle on slides 5 and 45, the red arrow on slide 36); those three are cropped from the 1920 px slide render
(Keynote PDF export, one PNG per slide named sNNN.png) so the marker stays. RENDER_DIR defaults to the session render
folder; pass another folder that holds s005.png, s036.png and s045.png at 1920 x 1080 to re-run.

Taken (embedded blobs):
  slide 4   chronic lymphocytic leukemia smear (sheets of small mature lymphocytes); slide 15 reuses the same picture
            beside the non-Hodgkin definition, so it is taken once
  slide 10  the Rai staging table picture (stages 0-IV; "*Organomegaly = hepatomegaly and/or splenomegaly"); the blob
            is 343 px wide and is doubled for legibility (the guide also holds it as an HTML table)
  slide 26  "Stages of Non-Hodgkin's Lymphoma" (stage 1-4 body maps with the diaphragm line); the same picture sits on
            slides 19 and 40 (slide 26 crops off the source logo, so slide 26's crop is used)
  slide 31  child with a large jaw swelling (Burkitt lymphoma)
  slide 32  "starry sky" histology (Burkitt lymphoma)
  slide 44  MGUS / smoldering multiple myeloma / multiple myeloma marrow drawings (spectrum of plasma cell disorders)
  slide 47  the "S.Li.M C.R.A.B." drawing (presentation of multiple myeloma)
  slide 48  skull radiograph with osteolytic "punched out" lesions
  slide 51  the R-ISS table picture ("Table 2. R-ISS for MM"), doubled for legibility (also an HTML table)
  slide 52  the course of multiple myeloma graph (M protein over time: MGUS or smoldering, active myeloma, remission,
            relapse, relapsed refractory)
Taken (render crops, marker drawn on the slide):
  slide 5   hematopoiesis diagram with the B lymphocyte circled (where chronic lymphocytic leukemia arises)
  slide 36  Reed-Sternberg cells, the red arrow from "Binucleated, neoplastic B cells" ending on one
  slide 45  hematopoiesis diagram with the plasma cell circled (where multiple myeloma arises)

Held as HTML tables instead (text on the slide): 8-9 (chronic lymphocytic leukemia against monoclonal B
lymphocytosis), 10 (Rai), 26/40 (stage captions), 27 and 41 (management by type / stage), 28 (tumor lysis), 30
(poor-prognosis factors), 47 (CRAB and SLiM), 50/56/57 (MGUS against smoldering against myeloma), 51 (R-ISS).

Left out:
  slides 1-3, 14, 35, 43  title, objective and section-divider slides (no pictures)
  slide 15  the same smear as slide 4 (taken once)
  slides 19, 40  the same staging picture as slide 26 (taken once)
  slide 58  closing cartoon ("I'm afraid my brain has left for the day") and stock clip art: decoration
"""
import io, os, sys
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 8/"
                          "50. Hematologic Malignancies Part II - Gannon.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 8", "cms-e8-images")
RENDERS = (sys.argv[1] if len(sys.argv) > 1 else
           "/private/tmp/claude-501/-Users-jaxonluke/e06779a5-ab02-4065-a6fc-fe88e20d1bfd/scratchpad/render/l50_hi")
MAXW = 1400
EMU_W = 12192000  # slide width; the renders are 1920 px wide

# (slide, picture shape id, output name, upscale)
FIGS = [
    (4, 4, "l50-s004-cll-smear.jpg", 1),
    (10, 9218, "l50-s010-rai-staging-table.png", 2),
    (26, 4, "l50-s026-lymphoma-stages.jpg", 1),
    (31, 5, "l50-s031-burkitt-jaw.jpg", 1),
    (32, 16386, "l50-s032-starry-sky.jpg", 1),
    (44, 18434, "l50-s044-plasma-cell-spectrum.jpg", 1),
    (47, 21506, "l50-s047-slim-crab.jpg", 1),
    (48, 22530, "l50-s048-punched-out-skull.jpg", 1),
    (51, 11268, "l50-s051-riss-table.png", 2),
    (52, 1026, "l50-s052-myeloma-course.png", 1),
]

# (slide, shape ids whose frames are joined, output name, fixed pixel box or None): the crop is the union of the
# picture's frame and the marker's frame, clipped to the slide, taken from the 1920 px render so the marker stays.
# Slide 36's picture frame runs off the slide and the render shows it narrower than the frame, so its box is the
# visible picture measured on the render (x 1300-1832, y 208-1036; the arrow tip sits at about x 1371, y 813).
RENDER_CROPS = [
    (5, (8198, 7), "l50-s005-hematopoiesis-b-cell.jpg", None),
    (36, (2050,), "l50-s036-reed-sternberg.jpg", (1300, 208, 1832, 1036)),
    (45, (4, 5), "l50-s045-hematopoiesis-plasma-cell.jpg", None),
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


def shape(slide, n, shape_id):
    for sh in walk(slide.shapes):
        if sh.shape_id == shape_id:
            return sh
    raise SystemExit("slide %d: no shape with id %s" % (n, shape_id))


def picture(slide, n, shape_id):
    sh = shape(slide, n, shape_id)
    im = flatten(Image.open(io.BytesIO(sh.image.blob)))
    w, h = im.size
    l, t = round(sh.crop_left * w), round(sh.crop_top * h)
    r, b = w - round(sh.crop_right * w), h - round(sh.crop_bottom * h)
    return im.crop((max(l, 0), max(t, 0), min(r, w), min(b, h)))


def render_crop(slide, n, shape_ids, fixed):
    path = os.path.join(RENDERS, "s%03d.png" % n)
    if not os.path.exists(path):
        raise SystemExit("missing render %s (pass a render folder as the first argument)" % path)
    page = Image.open(path).convert("RGB")
    if fixed:
        return page.crop(fixed)
    k = page.width / EMU_W
    shs = [shape(slide, n, i) for i in shape_ids]
    box = (round(min(s.left for s in shs) * k), round(min(s.top for s in shs) * k),
           round(max(s.left + s.width for s in shs) * k), round(max(s.top + s.height for s in shs) * k))
    box = (max(box[0], 0), max(box[1], 0), min(box[2], page.width), min(box[3], page.height))
    return page.crop(box)


def save(im, name):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    path = os.path.join(OUT, name)
    if name.endswith(".png"):  # line art and tables: a 128-color palette keeps it small and sharp
        im.convert("P", palette=Image.ADAPTIVE, colors=128).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    print("%-44s %4dx%-4d %6.1f KB" % (name, im.width, im.height, os.path.getsize(path) / 1024))
    return im.size


def main():
    os.makedirs(OUT, exist_ok=True)
    slides = list(Presentation(DECK).slides)
    for n, sid, name, up in FIGS:
        im = picture(slides[n - 1], n, sid)
        if up > 1:
            im = im.resize((im.width * up, im.height * up), Image.LANCZOS)
        save(im, name)
    for n, sids, name, fixed in RENDER_CROPS:
        save(render_crop(slides[n - 1], n, sids, fixed), name)


if __name__ == "__main__":
    main()
