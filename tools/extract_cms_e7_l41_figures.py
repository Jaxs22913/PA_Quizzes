#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 41 (Inflammatory Lung Diseases, Gray) figures for the CMS I Exam 7 study guide.

    python3 tools/extract_cms_e7_l41_figures.py

Deck: "Inflammatory Lung Disease 2026.pptx" (74 slides). Every slide was viewed at 1920 px before anything
was chosen. Slide images are cleared for use provided the slide is cited (each figure cites it). Every file
is built from the original embedded blobs (no slide-render crops), uncropped, with watermarks, source lines
and the arrows already in the pictures kept. Where the slide covers part of a picture with a design shape
(slides 5, 43, 45, 53) the whole blob is used. Small blobs are enlarged with Lanczos so labels read.

Taken (guide subsection):
  slide 5   normal lungs against lungs with idiopathic pulmonary fibrosis (labeled drawing): 3.1
  slide 7   pathogenesis of pulmonary fibrosis (flowchart): 3.1
  slide 8   two unlabeled specimen pictures (cut lung A/B, microscope section): 3.1
  slide 12  the classification chart that the guide's slide-12 table transcribes: 3.1
  slide 27  the two chest X-rays side by side (the right picture carries the slide's IPF label): 3.3
  slide 29  the volume-time curves and the flow-volume loops side by side: 3.3
  slide 36  high-resolution CT of idiopathic (fibrosing) interstitial pneumonia: 3.4
  slide 41  the immune response drawing (antigen to granuloma and fibrosis): 3.6
  slide 43  the multi-organ sarcoidosis drawing (labels name the exam findings): 3.6
  slide 28  sarcoidosis chest X-ray with the arrows at the hila and right paratracheal area: 3.6
  slide 45  the chest X-ray beside the sarcoid stage list (the slide names no stage for it): 3.6
  slide 53  coal workers' pneumoconiosis chest X-ray with the upper-zone arrows: 3.7
  slide 58  asbestosis: CT lung window, chest X-ray, CT soft-tissue window: 3.8
  slide 63  silicosis chest X-ray (eggshell hilar nodes at the white arrows): 3.9
  slide 67  the hypersensitivity pneumonitis signs chart (a picture; the guide holds it as a table): 3.10
  slide 70  hypersensitivity pneumonitis CT and histology: 3.10
  slides 72-74  the three generated acute respiratory distress syndrome pictures that 3.11 is read
            from (dense graphics; the guide's tables transcribe them): 3.11

Left out:
  slide 1   title art.          slide 21  zebra cartoon (decoration).
  slide 10  a picture of a plain two-column table, transcribed cell by cell into the guide's slides 9-10
            table instead (the picture adds nothing the table does not hold).
  every other slide is text, or a real slide table (9, 15) that the guide holds as an HTML table.
"""
import io, os, sys
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 7/"
    "Inflammatory Lung Disease 2026.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-e7-images")
MAXW = 1400

# (output file, [(slide, picture shape id), ...], scale). Two or more pictures are set side by side at a
# common height on white, in slide order left to right.
FIGS = [
    ("l41-s005-fibrosis-normal-vs-ipf.jpg", [(5, 14)], 1.5),
    ("l41-s007-fibrosis-pathogenesis.png", [(7, 2)], 1.0),
    ("l41-s008-specimen-gross.jpg", [(8, 2)], 1.0),
    ("l41-s008-specimen-micro.jpg", [(8, 3)], 1.0),
    ("l41-s012-ild-classification.png", [(12, 4)], 2.0),
    ("l41-s027-cxr-ipf-lower-fields.jpg", [(27, 7), (27, 6)], 1.0),
    ("l41-s029-pft-curves-loops.png", [(29, 4), (29, 5)], 1.0),
    ("l41-s036-hrct-ipf-honeycombing.jpg", [(36, 4)], 1.5),
    ("l41-s041-sarcoid-immune-response.png", [(41, 4)], 1.0),
    ("l41-s043-sarcoid-organs.jpg", [(43, 5)], 1.5),
    ("l41-s028-cxr-sarcoid-hilar.jpg", [(28, 7)], 1.0),
    ("l41-s045-cxr-sarcoid.jpg", [(45, 6)], 1.0),
    ("l41-s053-cxr-coal-workers.jpg", [(53, 7)], 1.0),
    ("l41-s058-ct-asbestos-lung-window.jpg", [(58, 6)], 1.0),
    ("l41-s058-cxr-asbestos.jpg", [(58, 4)], 1.0),
    ("l41-s058-ct-asbestos-soft-tissue.jpg", [(58, 5)], 1.0),
    ("l41-s063-cxr-silicosis.jpg", [(63, 4)], 1.5),
    ("l41-s067-hp-signs-chart.png", [(67, 4)], 1.0),
    ("l41-s070-ct-hp-fibrosis.jpg", [(70, 4)], 1.0),
    ("l41-s070-histology-hp-granulomas.jpg", [(70, 5)], 0.75),
    ("l41-s072-ards-etiology.jpg", [(72, 3)], 1.0),
    ("l41-s073-ards-diagnosis.jpg", [(73, 3)], 1.0),
    ("l41-s074-ards-management.jpg", [(74, 3)], 1.0),
]
GAP = 24


def pictures(prs):
    """{(slide number, shape id): image bytes}, recursing into groups."""
    out = {}

    def walk(n, shapes):
        for sh in shapes:
            if sh.shape_type == 6:
                walk(n, sh.shapes)
            elif sh._element.tag.endswith("}pic"):
                out[(n, sh.shape_id)] = sh.image.blob

    for n, slide in enumerate(prs.slides, 1):
        walk(n, slide.shapes)
    return out


def flat(im):
    """RGB on white (transparent PNG corners must not turn black)."""
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def side_by_side(ims):
    h = max(i.height for i in ims)
    ims = [i if i.height == h else i.resize((round(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    out = Image.new("RGB", (sum(i.width for i in ims) + GAP * (len(ims) - 1), h), (255, 255, 255))
    x = 0
    for i in ims:
        out.paste(i, (x, 0))
        x += i.width + GAP
    return out


def save(im, path):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    if path.endswith(".png"):
        im.quantize(colors=128, method=Image.MEDIANCUT, dither=Image.NONE).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    return im.size, os.path.getsize(path)


def main():
    if not os.path.exists(DECK):
        sys.exit("deck not found: " + DECK)
    os.makedirs(OUT, exist_ok=True)
    pics = pictures(Presentation(DECK))
    total = 0
    for name, parts, scale in FIGS:
        ims = []
        for key in parts:
            if key not in pics:
                sys.exit("missing picture: slide %d shape %d" % key)
            ims.append(flat(Image.open(io.BytesIO(pics[key]))))
        im = ims[0] if len(ims) == 1 else side_by_side(ims)
        if scale != 1:
            im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        (w, h), size = save(im, os.path.join(OUT, name))
        total += size
        print("%-42s %4dx%-4d %6.1f KB" % (name, w, h, size / 1024))
    print("total %.1f KB" % (total / 1024))


if __name__ == "__main__":
    main()
