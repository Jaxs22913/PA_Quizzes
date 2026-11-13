#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 46 (Cytopenias and Hemochromatosis, Matt Ward) figures for the CMS I Exam 8 study guide.

    python3 tools/extract_cms_e8_l46_figures.py

Deck: "Cytopenias_Hemochromatosis_Objectives_Enhanced.pptx" (107 slides). Every slide was viewed at 1920 px before
choosing. Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e8_guide/l46.html
carries its slide number. All figures are the deck's own picture blobs (cropped as the slide crops them,
transparency flattened onto white); the arrows on slides 40 and 78 are inside the blobs, so no render crop is needed.

Taken (embedded blobs):
  slide 12  koilonychia, two photographs: the Medscape thumb (spoon-shaped, concave nail) and a thumbnail photo
  slide 16  the Hemoccult kit (fecal occult blood test, stool guaiac test)
  slide 36  gums with a dark lead line (lead poisoning; text on slide 35)
  slide 40  two smears of megaloblastic anemia: macro-ovalocytes and a hypersegmented neutrophil; the PathPedia smear
            marks the neutrophil (arrowhead) and macro-ovalocytes (arrows)
  slide 43  "Absorption of Vitamin B12" diagram (stomach, intrinsic factor, terminal ileum, liver)
  slide 46  glossitis, two photographs (smooth, red tongue)
  slide 66  extravascular against intravascular hemolysis diagram (macrophage, unconjugated bilirubin, haptoglobin,
            kidney, hemoglobinuria)
  slide 68  smear with schistocytes (Wright stain, x1000)
  slide 72  Coombs (direct antiglobulin) test diagram: patient erythrocytes + antiserum -> agglutination
  slide 75  two smears A and B beside "Genetic causes of hemolytic anemia" (membrane defects)
  slide 78  bite cells (arrows) and Heinz bodies on a supravital stain (arrows), G6PD deficiency
  slide 87  face of a patient with thalassemia (skeletal changes). The blob is small (187 x 269) and kept at its size.
  slide 91  world map of births with sickle cell anemia per 100,000 births (follows the malaria belt)
  slide 94  chest CT of acute chest syndrome
  slide 95  body diagram of the acute and chronic complications of sickle cell disease

Held as HTML tables instead (text on the slide): 7 (indices), 27 (chronic disease against iron deficiency, arrows),
41 (megaloblastic CBC), 52 (chronic kidney disease CBC), 59 (neutropenia classes), 103 (cut-offs), 105-107.

Left out:
  slide 1-5, 9, 22, 28, 37, 51, 54, 84, 99  title, objective and section-divider slides (slide 9's iron nugget and
            the blood-cell art are decoration)
  slide 42  folate food photograph (decoration)
  slide 61  scanning electron picture of a red cell (decoration beside the text)
  slide 69  blood tubes in a gloved hand (decoration)
  slide 83  UpToDate partial list of drugs in G6PD deficiency: it puts chloroquine under "safe", against slide 79's
            trigger list; excluded from the guide's figures (the conflict is named in the warn callout)
  slide 90, 96  hemoglobin tetramer model (illustration only; the text gives the chain make-up)
"""
import io, os, sys
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 8/"
                          "Cytopenias_Hemochromatosis_Objectives_Enhanced.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 8", "cms-e8-images")
MAXW = 1400

# (slide, picture shape id, output name)
FIGS = [
    (12, 9, "l46-s012-koilonychia-spoon-nail.jpg"),
    (12, 4, "l46-s012-koilonychia-thumb.jpg"),
    (16, 7, "l46-s016-hemoccult-kit.jpg"),
    (36, 5, "l46-s036-lead-line-gums.jpg"),
    (40, 11, "l46-s040-megaloblastic-smear.jpg"),
    (40, 9, "l46-s040-hypersegmented-neutrophil.jpg"),
    (43, 5, "l46-s043-b12-absorption.jpg"),
    (46, 72707, "l46-s046-glossitis-1.jpg"),
    (46, 72708, "l46-s046-glossitis-2.jpg"),
    (66, 7, "l46-s066-extravascular-intravascular-hemolysis.jpg"),
    (68, 5, "l46-s068-schistocytes.jpg"),
    (72, 5, "l46-s072-coombs-test.png"),
    (75, 6, "l46-s075-membrane-defect-smears.jpg"),
    (78, 4, "l46-s078-bite-cells.jpg"),
    (78, 5, "l46-s078-heinz-bodies.jpg"),
    (87, 2050, "l46-s087-thalassemia-facies.jpg"),
    (91, 6, "l46-s091-sickle-cell-map.jpg"),
    (94, 5, "l46-s094-acute-chest-syndrome-ct.jpg"),
    (95, 4, "l46-s095-sickle-cell-complications.jpg"),
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
    if name.endswith(".png"):  # line art: a 128-color palette keeps it small and sharp
        im.convert("P", palette=Image.ADAPTIVE, colors=128).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    print("%-52s %4dx%-4d %6.1f KB" % (name, im.width, im.height, os.path.getsize(path) / 1024))
    return im.size


def main():
    os.makedirs(OUT, exist_ok=True)
    slides = list(Presentation(DECK).slides)
    for n, sid, name in FIGS:
        save(picture(slides[n - 1], n, sid), name)


if __name__ == "__main__":
    main()
