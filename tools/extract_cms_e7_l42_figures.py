#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 42 (Pulmonary Vascular Disorders, Gray) figures for the CMS I Exam 7 study guide.

    python3 tools/extract_cms_e7_l42_figures.py

Deck: "Pulmonary Vascular Disorders 2026 - Gray.pptx" (62 slides). Slides 3-62 are each ONE generated
infographic picture (1376 x 768 px, "Gemini Notebook" mark in the corner) laid over the whole slide, so there
is nothing smaller to lift: every figure is cut from that embedded picture. Crop boxes are written in the
pixels of the 1920 x 1080 slide render (the same coordinates read off the renders when the panels were
chosen) and converted here to the picture's own pixels through the shape's position on the slide, so the
files rebuild from the deck alone. Panel crops are enlarged 1.4x with Lanczos (the render's own scale) so the
labels read; whole slides stay at the picture's size. Every slide was viewed at 1920 px before choosing.
Slide images are cleared for use provided the slide is cited (each figure cites it).

Taken (guide subsection):
  slide 6   alveolar hypoxia -> vasoconstriction -> remodeling mechanism (starred driver): 4.2
  slide 12  the stepwise diagnostic pathway flowchart (groups 3, 4, 1): 4.3
  slide 13  pulmonary function loops (obstructive vs restrictive) and the chest film with its two arrows: 4.3
  slide 14  the EKG panel and the echocardiogram panel (D-shaped left ventricle) as two crops: 4.3. The
            echo crop starts below the panel's heading, which calls echo "The Gold Standard" (one of the
            deck's four conflicting gold standards; the guide keys echo as the screening test).
  slide 19  the World Health Organization classification chart the guide's slide-19 table transcribes: 4.4
  slide 22  the four physical-exam boxes around the body drawing: 4.5
  slide 32  the Starling-forces capillary drawing: 4.8
  slide 37  the wet-lung chest film with its four labeled findings: 4.9
  slide 51  the S1Q3T3 EKG panel and the classic chest-film-signs panel as two crops: 4.11
  slide 53  the Wells criteria chart (the guide's slide-53 table transcribes it): 4.12
  slide 54  the PERC + D-dimer two-layer chart (the guide's slide-54 table transcribes it): 4.12
  slide 55  the CTPA vs V/Q comparison table picture (dense graphic; guide table transcribes it): 4.12
  slide 56  the echocardiogram drawing of right-ventricular strain (crop of the left half): 4.12
  slide 57  the diagnostic algorithm (decision points transcribed in the guide): 4.12
  slide 58  the three-column risk stratification chart (the guide's slide-58 table transcribes it): 4.13

Left out:
  slides 1-2 title and outline text; 3, 17, 30, 31, 47 divider and decoration art (slide 3's admissions
  figure is out of scope). Slides 4-5, 7-11, 15-16, 18, 20-21, 23-29, 33-36, 38-46, 48-50, 52, 59-62 are
  text-led infographics (icons, cartoons, generic organ art) that the guide transcribes as prose or slide-
  exact tables (9, 23, 25, 33, 39, 43, 44, 49, 50, 59, 60, 61); their pictures teach nothing the text does not.
  Slide 38's wedge-catheter drawing carries decorative graph values (8/12/22) that are not keyed; slide 46's
  small butterfly chest film duplicates slide 37's finding at thumbnail size; the monitor readouts on slides
  49-62 are decoration.
"""
import io, os, sys
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 7/"
    "Pulmonary Vascular Disorders 2026 - Gray.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-e7-images")
MAXW = 1400
RW, RH = 1920, 1080          # the slide-render size the crop boxes are written in

# (output file, slide, picture shape id, crop box in render px (x0, y0, x1, y1) or None = whole picture,
#  scale, JPEG quality)
FIGS = [
    ("l42-s006-alveolar-hypoxia-mechanism.jpg", 6, 2, None, 1.0, 82),
    ("l42-s012-diagnostic-pathway.jpg", 12, 2, None, 1.0, 82),
    ("l42-s013-pft-loops-chest-film.jpg", 13, 2, None, 1.0, 82),
    ("l42-s014-ekg-right-heart-strain.jpg", 14, 2, (55, 160, 905, 1045), 1.4, 84),
    ("l42-s014-echo-d-shaped-lv.jpg", 14, 2, (1025, 256, 1875, 1045), 1.4, 84),
    ("l42-s019-who-groups.jpg", 19, 2, None, 1.0, 82),
    ("l42-s022-exam-signs.jpg", 22, 2, (85, 185, 1845, 1035), 1.0, 82),
    ("l42-s032-starling-forces.jpg", 32, 2, None, 1.0, 82),
    ("l42-s037-wet-lung-chest-film.jpg", 37, 2, (85, 225, 1855, 1005), 1.0, 84),
    ("l42-s051-ekg-s1q3t3.jpg", 51, 2, (90, 165, 950, 995), 1.4, 84),
    ("l42-s051-chest-film-classic-signs.jpg", 51, 2, (975, 165, 1835, 995), 1.4, 84),
    ("l42-s053-wells-chart.jpg", 53, 2, None, 1.0, 82),
    ("l42-s054-perc-d-dimer-chart.jpg", 54, 2, None, 1.0, 82),
    ("l42-s055-ctpa-vs-vq.jpg", 55, 2, (90, 160, 1835, 1015), 1.0, 84),
    ("l42-s056-echo-rv-strain.jpg", 56, 2, (295, 145, 1065, 805), 1.4, 84),
    ("l42-s057-diagnostic-algorithm.jpg", 57, 2, None, 1.0, 82),
    ("l42-s058-risk-stratification.jpg", 58, 2, None, 1.0, 82),
]


def pictures(prs):
    """{(slide number, shape id): (image bytes, shape)}, recursing into groups."""
    out = {}

    def walk(n, shapes):
        for sh in shapes:
            if sh.shape_type == 6:
                walk(n, sh.shapes)
            elif sh._element.tag.endswith("}pic"):
                out[(n, sh.shape_id)] = (sh.image.blob, sh)

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


def to_picture_box(box, sh, im, sw, shh):
    """Render-pixel box -> the embedded picture's pixel box, through the shape's place on the slide."""
    x0, y0, x1, y1 = box

    def px(xr):
        emu = xr / RW * sw
        return max(0, min(im.width, round((emu - sh.left) / sh.width * im.width)))

    def py(yr):
        emu = yr / RH * shh
        return max(0, min(im.height, round((emu - sh.top) / sh.height * im.height)))

    return (px(x0), py(y0), px(x1), py(y1))


def save(im, path, quality):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    if path.endswith(".png"):
        im.quantize(colors=128, method=Image.MEDIANCUT, dither=Image.NONE).save(path, optimize=True)
    else:
        im.save(path, quality=quality, optimize=True, progressive=True)
    return im.size, os.path.getsize(path)


def main():
    if not os.path.exists(DECK):
        sys.exit("deck not found: " + DECK)
    os.makedirs(OUT, exist_ok=True)
    prs = Presentation(DECK)
    sw, shh = prs.slide_width, prs.slide_height
    pics = pictures(prs)
    total = 0
    for name, slide, sid, box, scale, quality in FIGS:
        if (slide, sid) not in pics:
            sys.exit("missing picture: slide %d shape %d" % (slide, sid))
        blob, sh = pics[(slide, sid)]
        im = flat(Image.open(io.BytesIO(blob)))
        if box:
            im = im.crop(to_picture_box(box, sh, im, sw, shh))
        if scale != 1:
            im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        (w, h), size = save(im, os.path.join(OUT, name), quality)
        total += size
        print("%-42s %4dx%-4d %6.1f KB" % (name, w, h, size / 1024))
    print("total %.1f KB (%d files)" % (total / 1024, len(FIGS)))


if __name__ == "__main__":
    main()
