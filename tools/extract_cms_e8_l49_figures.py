#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 49 (Hematologic Malignancies Part I, Nicole Gannon) figures for the CMS I Exam 8 study guide.

    python3 tools/extract_cms_e8_l49_figures.py [RENDER_DIR]

Deck: "49. Hematologic Malignancies Part I - Gannon.pptx" (67 slides). Every slide was viewed at 1920 px before
choosing. Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e8_guide/l49.html
carries its slide number. Most figures are the deck's own picture blobs (cropped as the slide crops them,
transparency flattened onto white; slide 18's picture is rotated 90 degrees on the slide and is turned to match).
Five slides draw their teaching marks (circles, ovals, labeled boxes) as separate shapes on top of the picture, so
those figures are cropped from the 1920 px slide render instead (RENDER_DIR holds sNNN.png, the Keynote PDF render;
default: the session scratchpad render/l49_hi). The render is not in the repo; the crops it made are.

Taken (embedded blobs):
  slide 5   "Normal Hematopoiesis" diagram: stem cell -> myeloid and lymphoid progenitors -> mature cells
  slide 6   clonality / tumorigenesis diagram: healthy stem cells -> mutated stem cell -> clonal expansion ->
            clinical consequences (hematologic malignancy, inflammation, age-related disease)
  slide 9   risk factor panel (genetic, environmental, immune system disorders, lifestyle, age)
  slide 10  ECOG (Eastern Cooperative Oncology Group) performance status table, grades 0-5 (also an HTML table)
  slide 11  bone marrow biopsy diagram (biopsy needle into the back of the hip bone)
  slide 14  leukemia cells crowding the blood (drawing)
  slide 15  lymphatic system and lymph node drawing ("Lymphocytes that mutate into cancer cells")
  slide 16  multiple myeloma drawing: normal plasma cells and antibodies vs myeloma cells
  slide 18  acute lymphoblastic leukemia smear (sheets of lymphoblasts); rotated as on the slide
  slide 20  Philadelphia chromosome drawing (chromosomes 9 and 22 break and swap); slide 57 shows the same picture
            (identical blob), so the one file serves both slides
  slide 32  FAB (French-American-British) M0-M7 table picture (also an HTML table)
  slide 36  acute myeloid leukemia smear, two arrows on Auer rods (arrows are inside the blob)
  slide 51  myeloproliferative neoplasm lineage diagram (essential thrombocythemia, polycythemia vera, primary
            myelofibrosis, chronic myeloid leukemia boxed by the cell line they come from)
  slide 52  polycythemia vera smear (crowded red cells)
  slide 56  chronic myelogenous leukemia smear (granulocytes at every stage)
  slide 64  CML milestone table (A) and BCR-ABL1 response graph (B) (also an HTML table)
Cropped from the render (the teaching marks are separate shapes):
  slide 7   the hematopoiesis diagram with the four colored ovals: acute leukemias, chronic leukemias, lymphomas,
            myeloma and other plasma cell disorders
  slide 19  blood cell lineage diagram with the lymphoid stem cell -> lymphoblast branch circled
  slide 31  acute myeloid leukemia smear with the red circle on the Auer rod
  slide 33  FAB lineage diagram with M0-M1 AML, APL, AMML and acute monocytic boxes
  slide 45  myelodysplastic syndrome marrow with the dysplastic cell circled

Held as HTML tables instead (text on the slide): 10 (ECOG), 32 (FAB), 62 (CML phases), 64 (milestones);
the pictures of 10, 32 and 64 are kept too because the slide's version is a picture.

Left out:
  slides 1-4, 13, 17, 30, 44, 50, 55  title, objective, disclosure and section-divider slides
  slide 8   epidemiology pie chart and top-ten cancer table (case counts the guide does not key; text kept)
  slide 23  flow cytometry plots, captioned "This image is for illustration purposes only" on the slide
  slides 26, 39  "Management for PA Students ... Just kidding....": full treatment protocols shown as a joke
  slide 67  closing meme
"""
import io, os, sys
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 8/"
                          "49. Hematologic Malignancies Part I - Gannon.pptx")
RENDER = (sys.argv[1] if len(sys.argv) > 1 else
          "/private/tmp/claude-501/-Users-jaxonluke/e06779a5-ab02-4065-a6fc-fe88e20d1bfd/scratchpad/render/l49_hi")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 8", "cms-e8-images")
MAXW = 1400
MAXH = 1100

# (slide, picture shape id, output name, degrees to rotate clockwise as the slide shows it)
FIGS = [
    (5, 15, "l49-s005-hematopoiesis.png", 0),
    (6, 2052, "l49-s006-clonality.jpg", 0),
    (9, 4098, "l49-s009-risk-factors.jpg", 0),
    (10, 6146, "l49-s010-ecog-table.png", 0),
    (11, 5122, "l49-s011-bone-marrow-biopsy.jpg", 0),
    (14, 3078, "l49-s014-leukemia-cells.jpg", 0),
    (15, 2050, "l49-s015-lymphoma-lymphatics.jpg", 0),
    (16, 1026, "l49-s016-myeloma-plasma-cells.jpg", 0),
    (18, 13, "l49-s018-all-smear.jpg", 90),
    (20, 8194, "l49-s020-philadelphia-chromosome.jpg", 0),
    (32, 15, "l49-s032-fab-table.png", 0),
    (36, 20482, "l49-s036-aml-auer-rods.jpg", 0),
    (51, 12290, "l49-s051-mpn-lineage.jpg", 0),
    (52, 13314, "l49-s052-pv-smear.jpg", 0),
    (56, 4098, "l49-s056-cml-smear.jpg", 0),
    (64, 1026, "l49-s064-cml-milestones.png", 0),
]
# (slide, box on the 1920 x 1080 render, output name)
CROPS = [
    (7, (30, 256, 1290, 996), "l49-s007-malignancy-families.png"),
    (19, (1071, 251, 1882, 856), "l49-s019-lineage-lymphoblast.png"),
    (31, (1112, 124, 1869, 1028), "l49-s031-aml-auer-rod-circled.jpg"),
    (33, (1038, 210, 1866, 1010), "l49-s033-fab-lineage.png"),
    (45, (987, 203, 1862, 1009), "l49-s045-mds-dysplastic-cell.jpg"),
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
    if im.height > MAXH:  # tall smears (slides 18, 52): no taller than they need to be on a page
        im = im.resize((round(im.width * MAXH / im.height), MAXH), Image.LANCZOS)
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
    for n, sid, name, rot in FIGS:
        im = picture(slides[n - 1], n, sid)
        if rot:
            im = im.rotate(-rot, expand=True)
        save(im, name)
    for n, box, name in CROPS:
        src = os.path.join(RENDER, "s%03d.png" % n)
        if not os.path.exists(src):
            raise SystemExit("missing render %s (pass the render folder as the first argument)" % src)
        im = Image.open(src).convert("RGB")
        if im.size != (1920, 1080):
            raise SystemExit("%s is %dx%d, expected 1920x1080" % (src, im.width, im.height))
        save(im.crop(box), name)


if __name__ == "__main__":
    main()
