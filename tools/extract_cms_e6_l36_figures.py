#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 36 (Chronic Obstructive Pulmonary Disease, Prof. Reynolds) figures for the CMS I Exam 6
study guide.

    python3 tools/extract_cms_e6_l36_figures.py

Deck: "37. svCOPD 2026.pptx" (the file name says 37; it is Lecture 36; 66 slides). Every slide was viewed at
1920 px before choosing. Slide images are cleared for use provided the slide is cited; every figure in
tools/cms_e6_guide/l36.html carries its slide number. Most pictures are the deck's own embedded blob (the
slide's crop applied, transparency flattened onto white). The GOLD (Global Initiative for Chronic Obstructive
Lung Disease) tables and figures are embedded as whole PDF pages cropped on the slide, and slides 22 (an
accessory-muscle photograph stored at 287 px), 35, 37, 47, 48, 59, 60 and 64 show more than one picture or a
cropped page, so those are cut from the 1920 px render (RENDER below) exactly as the slide shows them.

Taken:
  slide 7   normal bronchial tubes vs bronchitis; alveoli with emphysema vs normal; a bronchoscopic view;
            a cut emphysematous lung specimen
  slides 11-12  the cigarette smoke -> macrophage -> neutrophil -> protease pathway (same picture on both)
  slide 13  the risk factors -> four hypotheses -> emphysema / chronic bronchitis flowchart
  slide 15  pink puffer vs blue bloater, with the "more emphysema" / "less emphysema" coronal CT slices
  slide 19  healthy vs alpha-1 antitrypsin deficiency (lung and liver); normal, centriacinar and panacinar acini
  slide 22  pursed-lip breathing; drawing with a lateral chest x-ray; accessory muscles (render crop)
  slides 23, 24  the COPD Assessment Test form and the modified MRC dyspnea scale (render crops; also HTML)
  slides 25-28  flow-volume loops and volume-time curves (scooped expiratory limb; normal vs obstructive;
            normal vs COPD with its value table; the Medscape loop and curve)
  slide 29  the evaluation and treatment algorithm (also an HTML table)
  slide 31  the two labeled chest x-rays (bleb wall, vertical heart, low diaphragms; saber-sheath trachea,
            barrow-shaped chest, diaphragmatic tenting)
  slide 32  the hyperinflated chest x-ray with ribs counted and the flattened diaphragm drawn
  slide 33  bleb vs bulla drawing
  slides 34, 35, 37  GOLD grade table; the 2020 assessment and GOLD 2026 ABE tool; Figure 4.2 (render crops)
  slides 43, 45, 46, 47, 48, 49, 52, 55, 59, 60, 64  Table 4.9 non-drug care, Table 4.1 goals, Figure 4.1
            management cycle, the Five A's / FRAMES table and the stages of change box, the pneumococcal
            vaccine benefits box, the COPD Foundation pocket algorithm, the BODE index, the pulmonary
            rehabilitation wheel, Table 6 inpatient exacerbation drugs, Table 1 discharge criteria, the
            supplemental oxygen algorithm (each table also transcribed as HTML in the guide)

Left out:
  slides 1, 3, 65  title and case-scenario slides; slide 2 objectives
  slide 16  a cartoon patient listing symptoms (cartoon)
  slide 18  the comorbidity hexagon graphic (prevalence percentages, not a finding, criterion or mechanism)
  slide 19  the "Conditions associated with alpha-1 antitrypsin deficiency" body figure (stored at 290 px; its
            labels are not legible)
  slides 20, 21  text built from slide shapes over a background photograph (the text is already in 4.3)
  slide 23  a kitten in a knitted hat beside the CAT (visual pun)
  slides 50, 51  inhaler product photographs with trade names (product packaging)
  slide 60  stock photograph of a patient in bed (decoration)
  slide 63  oxygen concentrator and cylinder product photographs (unlabeled products)
  slides 14, 53  real slide tables already transcribed in the guide (4.1 and 4.8)
"""
import io, os
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 6/"
                          "37. svCOPD 2026.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6", "cms-e6-images")
# The 1920 px slide renders (LibreOffice export of the same deck).
RENDER = os.environ.get("CMS_E6_RENDER_L36", "/private/tmp/claude-501/-Users-jaxonluke/"
                        "85b16e35-5425-4d68-aee8-6236b2cfbe15/scratchpad/render/l36_hi")
MAXW = 1400

# (slide, shape id or ("render", box[, boxes painted white, in crop pixels]), file name[, max width]).
# Slide 37's white box covers the tail of the slide title, which the crop would otherwise clip mid-word.
FIGS = [
    (7, 2050, "l36-s007-normal-vs-bronchitis.jpg"),
    (7, 6, "l36-s007-alveoli-emphysema.jpg"),
    (7, 4, "l36-s007-bronchoscopy.jpg"),
    (7, 3, "l36-s007-emphysema-specimen.jpg", 1000),
    (12, 5, "l36-s012-smoke-protease-pathway.png"),
    (13, 6, "l36-s013-pathophysiology-hypotheses.png"),
    (15, 5, "l36-s015-pink-puffer-blue-bloater-ct.jpg"),
    (19, 5, "l36-s019-aat-healthy-vs-deficiency.png"),
    (19, 7, "l36-s019-acinus-centriacinar-panacinar.png"),
    (22, 6150, "l36-s022-pursed-lip-breathing.jpg"),
    (22, 6148, "l36-s022-drawing-and-lateral-xray.jpg"),
    (22, ("render", (1022, 582, 1775, 1042)), "l36-s022-accessory-muscles.jpg"),
    (23, ("render", (695, 0, 1910, 1080)), "l36-s023-cat-form.png"),
    (24, ("render", (370, 20, 1880, 1045)), "l36-s024-mmrc-scale.png"),
    (25, 5, "l36-s025-scooped-flow-volume-loop.png"),
    (26, 8194, "l36-s026-normal-vs-obstructive-loop.png"),
    (27, 9218, "l36-s027-volume-time-normal-vs-copd.png"),
    (28, 4, "l36-s028-flow-volume-and-volume-time.png"),
    (29, 4, "l36-s029-evaluation-treatment-algorithm.jpg"),
    (31, 10242, "l36-s031-cxr-bleb-vertical-heart.jpg"),
    (31, 10244, "l36-s031-cxr-saber-sheath-barrow-chest.jpg"),
    (32, 4098, "l36-s032-cxr-flattened-diaphragm.jpg"),
    (33, 19458, "l36-s033-bleb-vs-bulla.png"),
    (34, ("render", (670, 185, 1900, 880)), "l36-s034-gold-grades.png"),
    (35, ("render", (0, 250, 1920, 940)), "l36-s035-gold-2020-and-2026-assessment.png"),
    (37, ("render", (420, 90, 1918, 1078), [(0, 0, 600, 62)]), "l36-s037-gold-figure-4-2.png"),
    (43, ("render", (220, 20, 1695, 1045)), "l36-s043-nonpharm-table-4-9.png"),
    (45, ("render", (890, 280, 1900, 800)), "l36-s045-goals-table-4-1.png"),
    (46, 14, "l36-s046-management-cycle-figure-4-1.png"),
    (47, ("render", (30, 140, 1900, 1052)), "l36-s047-five-as-frames-stages.png"),
    (48, ("render", (1000, 190, 1890, 950)), "l36-s048-pneumococcal-benefits.png"),
    (49, 13314, "l36-s049-copd-foundation-algorithm.jpg"),
    (52, 3074, "l36-s052-bode-index.png"),
    (55, 18436, "l36-s055-pulmonary-rehab-wheel.jpg"),
    (59, ("render", (1010, 190, 1885, 885)), "l36-s059-inpatient-exacerbation-table-6.png"),
    (60, ("render", (960, 0, 1920, 1078)), "l36-s060-discharge-criteria.png"),
    (64, ("render", (55, 215, 1865, 925)), "l36-s064-oxygen-algorithm.png"),
]


def walk(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes)
        else:
            yield sh


def flat(im):
    im.load()
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        return bg
    return im.convert("RGB")


def picture(slide, n, shape_id):
    for sh in walk(slide.shapes):
        if sh.shape_id == shape_id and hasattr(sh, "image"):
            im = flat(Image.open(io.BytesIO(sh.image.blob)))
            w, h = im.size
            l, t = round(sh.crop_left * w), round(sh.crop_top * h)
            r, b = w - round(sh.crop_right * w), h - round(sh.crop_bottom * h)
            return im.crop((max(l, 0), max(t, 0), min(r, w), min(b, h)))
    raise SystemExit("slide %d: no picture with shape id %s" % (n, shape_id))


def render_crop(n, box, masks=()):
    p = os.path.join(RENDER, "s%03d.png" % n)
    if not os.path.exists(p):
        raise SystemExit("missing render %s (set CMS_E6_RENDER_L36 to the 1920 px render folder)" % p)
    im = flat(Image.open(p)).crop(box)
    for m in masks:
        im.paste((255, 255, 255), m)
    return im


def save(im, name, maxw=MAXW):
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    path = os.path.join(OUT, name)
    if name.endswith(".png"):  # line art and tables: a 128-color palette keeps them small and sharp
        im.convert("P", palette=Image.ADAPTIVE, colors=128).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    print("%-48s %4dx%-4d %6.1f KB" % (name, im.width, im.height, os.path.getsize(path) / 1024))


def main():
    os.makedirs(OUT, exist_ok=True)
    slides = list(Presentation(DECK).slides)
    for n, src, name, *rest in FIGS:
        if isinstance(src, tuple) and src[0] == "render":
            im = render_crop(n, *src[1:])
        else:
            im = picture(slides[n - 1], n, src)
        save(im, name, *rest)


if __name__ == "__main__":
    main()
