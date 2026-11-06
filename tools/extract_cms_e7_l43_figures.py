#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 43 (Pulmonary Nodules and Neoplasms, Gray) figures for the CMS I Exam 7 study guide.

    python3 tools/extract_cms_e7_l43_figures.py

Deck: "Pulmonary Nodules and Neoplasms 2026.pptx" (50 slides). Every slide was viewed at 1920 px before anything
was chosen. Slide images are cleared for use provided the slide is cited (each figure cites it). Every file is
built from the original embedded blobs (no slide-render crops: every picture on these slides is a single blob, and
the tables and algorithms that are pictures are whole blobs too), uncropped, with watermarks, source lines and the
arrows already in the pictures kept. Small blobs are enlarged with Lanczos so labels read. Two or more pictures
from one slide are set side by side at a common height on white, in the order given.

Taken (guide subsection):
  slide 4   pie of lung cancer cell types, each split smoker / non-smoker: 5.6
  slide 6   lung cross-section with the neuroendocrine cells lining the bronchioles: 5.6 (his paraneoplastic set-up)
  slide 8   type I and type II pneumocytes (labeled drawing): 5.6
  slide 10  growth sequence A-E (altered cell, hyperplasia, dysplasia, in situ, invasive, metastases): 5.6
  slide 11  the new solid nodule 8-30 mm algorithm (a picture; the guide also holds it as a table): 5.1
  slide 14  the CT pair A/B (needle into a nodule) and the bronchoscopy / chest-wall biopsy drawings: 5.4
  slide 15  the fit-for-surgery biopsy and treatment algorithm (picture + table): 5.4
  slide 16  the incidental nodule chest film (arrow) and the benign / malignant calcification strip: 5.2
  slide 17  CT and PET-CT of a nodule with high uptake: 5.4
  slide 19  Fleischner table A, solid nodules (picture + table): 5.3
  slide 20  Fleischner table B, subsolid nodules (picture + table): 5.3
  slide 21  the three benign CT findings (hamartoma, healed granuloma, nodule at the minor fissure): 5.2
  slide 22  TNM 8th edition table (picture + table): 5.8
  slides 23-29  the eleven stage pictures (1A, 1B, 2A, 2B, 3A x2, 3B x2, 3C, 4A, 4B) and the slide 25
            8th-edition stage classification drawing: 5.8
  slide 30  the location table (picture + table) and the small cell / non-small cell drawing: 5.9
  slide 32  CT of the spiculated peripheral nodule (invasive adenocarcinoma): 5.10
  slide 34  CT of the cavitated peripheral large cell mass and the two histology pictures: 5.11
  slide 35  the stage-treatment table (picture + table) and the resection drawing: 5.13
  slide 38  the two checkpoint-inhibitor drawings (how immunotherapy works; PD-1 / PD-L1): 5.13
  slide 40  CT of the cavitated, spiculated squamous cell lesion (arrows, circle): 5.12
  slide 42  the two small cell CTs and the crushed-biopsy histology (its own caption): 5.14
  slide 43  the small cell response-assessment flowchart (picture + table): 5.14
  slide 44  the linear accelerator and the two treatment-planning pictures: 5.14
  slide 47  the Lambert-Eaton myasthenic syndrome infographic: 5.16
  slide 48  the carcinoid syndrome body diagram: 5.15

Left out:
  slide 1   title art.                 slide 50  awareness-ribbon picture (decoration).
  slide 5   lymph node station map: an excluded slide ("nobody's expecting you to, like, number these").
  slide 7   labeled bronchus and alveolus histology: an excluded slide (no teaching text, 15 s on screen).
  slide 10  the right-hand research diagram (neutrophils, sRAGE, osteoblast activation): never narrated, banned
            from the quizzes; only the A-E growth sequence beside it is taken.
  slide 36  the adenocarcinoma mutation pie: he cut the gene detail ("don't go crazy about details on this"); the
            guide states the slide's genes in text.
  slide 37  the NICE drug-by-marker flowchart: he cut it ("I do not expect you to know absolutely specific drugs");
            the guide states the slide's own text (genetic markers -> chemotherapy, protein markers ->
            checkpoint inhibitors).
  every other slide is text only.
"""
import io, os, sys
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 7/"
    "Pulmonary Nodules and Neoplasms 2026.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-e7-images")
MAXW = 1400

# (output file, [(slide, picture shape id), ...], scale, common height for side-by-side parts or None).
FIGS = [
    ("l43-s004-celltype-pie.png", [(4, 7170)], 2.0, None),
    ("l43-s006-neuroendocrine-cells.jpg", [(6, 1026)], 1.0, None),
    ("l43-s008-pneumocytes.jpg", [(8, 5122)], 1.5, None),
    ("l43-s010-growth-sequence.jpg", [(10, 6148)], 1.5, None),
    ("l43-s011-nodule-algorithm.png", [(11, 10242)], 2.0, None),
    ("l43-s014-ct-guided-biopsy.jpg", [(14, 14338)], 1.5, None),
    ("l43-s014-bronchoscopy-thoracoscopy.jpg", [(14, 6), (14, 5)], 1.0, 612),
    ("l43-s015-biopsy-algorithm.png", [(15, 18434)], 1.0, None),
    ("l43-s016-cxr-incidental-nodule.jpg", [(16, 9220)], 0.75, None),
    ("l43-s016-calcification-patterns.png", [(16, 5)], 2.0, None),
    ("l43-s017-pet-ct.jpg", [(17, 11268)], 1.5, None),
    ("l43-s019-fleischner-solid.png", [(19, 7)], 1.5, None),
    ("l43-s020-fleischner-subsolid.png", [(20, 7)], 1.5, None),
    ("l43-s021-ct-hamartoma.jpg", [(21, 13314)], 1.5, None),
    ("l43-s021-ct-healed-granuloma.jpg", [(21, 13316)], 1.5, None),
    ("l43-s021-ct-minor-fissure.jpg", [(21, 8)], 1.5, None),
    ("l43-s022-tnm-table.png", [(22, 15362)], 2.0, None),
    ("l43-s023-stage-1a.jpg", [(23, 23554)], 1.5, None),
    ("l43-s023-stage-1b.jpg", [(23, 23556)], 1.5, None),
    ("l43-s024-stage-2a.jpg", [(24, 24578)], 1.5, None),
    ("l43-s024-stage-2b.jpg", [(24, 24580)], 1.5, None),
    ("l43-s025-stage-classification.jpg", [(25, 16386)], 1.5, None),
    ("l43-s026-stage-3a-no-nodes.jpg", [(26, 22532)], 1.5, None),
    ("l43-s026-stage-3a-nodes.jpg", [(26, 22534)], 1.5, None),
    ("l43-s027-stage-3b-large.jpg", [(27, 25602)], 1.5, None),
    ("l43-s027-stage-3b-small.jpg", [(27, 25604)], 1.5, None),
    ("l43-s028-stage-3c.jpg", [(28, 26626)], 1.5, None),
    ("l43-s029-stage-4a.jpg", [(29, 27650)], 1.5, None),
    ("l43-s029-stage-4b.jpg", [(29, 27652)], 1.5, None),
    ("l43-s030-location-table.png", [(30, 5)], 1.0, None),
    ("l43-s030-small-vs-nonsmall-cells.jpg", [(30, 11)], 2.0, None),
    ("l43-s032-ct-adenocarcinoma.jpg", [(32, 17410)], 1.5, None),
    ("l43-s034-ct-large-cell.jpg", [(34, 29698)], 2.0, None),
    ("l43-s034-histology-large-cell-50x.jpg", [(34, 6)], 0.35, None),
    ("l43-s034-histology-large-cell-high.jpg", [(34, 5)], 2.0, None),
    ("l43-s035-stage-treatment-table.jpg", [(35, 21506)], 2.5, None),
    ("l43-s035-resection-types.jpg", [(35, 7)], 2.0, None),
    ("l43-s038-checkpoint-inhibitors.jpg", [(38, 8), (38, 6)], 1.0, 560),
    ("l43-s040-ct-squamous.jpg", [(40, 28676)], 1.0, None),
    ("l43-s042-ct-small-cell-central.jpg", [(42, 33796)], 0.7, None),
    ("l43-s042-ct-small-cell-arrow.jpg", [(42, 7)], 0.85, None),
    ("l43-s042-histology-small-cell.jpg", [(42, 33794)], 0.7, None),
    ("l43-s043-sclc-flowchart.png", [(43, 5)], 1.3, None),
    ("l43-s044-linear-accelerator.jpg", [(44, 31746)], 1.0, None),
    ("l43-s044-radiotherapy-planning.jpg", [(44, 31748), (44, 7)], 1.0, 400),
    ("l43-s047-lambert-eaton.png", [(47, 35842)], 1.2, None),
    ("l43-s048-carcinoid-syndrome.png", [(48, 34818)], 1.5, None),
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


def side_by_side(ims, h):
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
    for name, parts, scale, height in FIGS:
        ims = []
        for key in parts:
            if key not in pics:
                sys.exit("missing picture: slide %d shape %d" % key)
            ims.append(flat(Image.open(io.BytesIO(pics[key]))))
        im = ims[0] if len(ims) == 1 else side_by_side(ims, height)
        if scale != 1:
            im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        (w, h), size = save(im, os.path.join(OUT, name))
        total += size
        print("%-44s %4dx%-4d %6.1f KB" % (name, w, h, size / 1024))
    print("%d files, total %.1f KB" % (len(FIGS), total / 1024))


if __name__ == "__main__":
    main()
