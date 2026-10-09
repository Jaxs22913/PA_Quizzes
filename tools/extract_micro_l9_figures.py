#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 9 (Cocci of Medical Importance) figures for Microbiology Exam 2: the
picture-question images for Set 2 of the quiz and the teaching figures for the guide.

Deck: "PAJ5200.Cocci of Med importance.pptx" (79 slides, 29 pictures; the title slide names
no lecturer). EVERY picture in the deck was extracted and viewed at full size before any was
chosen here. Slide images are cleared for use provided the slide is cited.

QUIZ images carry NO label that names the answer. Baked-in labels were cropped or erased:
  slide 4   left panel only (the Gram stain); the scanning micrograph and credits cropped off
  slide 22  banner and credit cropped; nothing on the photograph names the organism
  slide 24  panel (a): the "Streptococcus pyogenes with zones of beta-hemolysis" label sits
            above the photograph and is cropped off; its two leader lines are erased
  slide 24  panel (b): cropped clean, nothing on it
  slide 34  panel (a): the "(a)" letter cropped off
  slide 42  the "(+) CAMP test" label and its bracket cropped off the right edge; the
            "SXT" and "Bacitracin" disc labels stay (they name the discs, not the result)
  slide 49  the "Pneumococci" and "Phagocyte" labels cropped off the top and their leader
            lines erased; the inset drawing of the cell shape stays
  slide 72  the "Gonococci" and "Neutrophil" labels cropped off and their leader lines and
            bracket erased

Left out, after looking: slides 1 (title-slide micrographs, decoration), 58 (a stock
photograph of anaerobic jars with a watermark), 60 and 66 (jokes), 62-65 (sexually
transmitted infection rate maps and a trend graph the lecturer used for anecdote, no objective
rides on them), 15 (scalded skin and impetigo plates at 300 pixels wide, too small to teach
from), 13 (osteomyelitis drawing; the one fact it adds, the metaphysis, is on slide 12's text).

    python3 tools/extract_micro_l9_figures.py
"""
import io, os
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 2/PAJ5200.Cocci of Med importance.pptx")
FOLDER = os.path.join(ROOT, "Microbiology Exam 2")
QUIZ = os.path.join(FOLDER, "micro-exam-2-quiz-images")
GUIDE = os.path.join(FOLDER, "micro-exam-2-study-guide-images")
MAXW = 900


def grey_line(sub):
    """Near-black, unsaturated pixels: leader lines on a pale stained smear."""
    return (sub.mean(axis=2) <= 125) & (sub.max(axis=2) - sub.min(axis=2) <= 45)


def dark_on_orange(sub):
    """Leader lines drawn over an orange blood-agar photograph: the red channel drops."""
    return sub[..., 0] < 190


def erase_lines(im, box, pred=grey_line, grow=2):
    """Erase thin dark-gray leader lines inside box. Core pixels (dark AND unsaturated: the
    lines are near-black, stained cells are saturated pink or purple) are found, grown by a
    couple of pixels to take the anti-aliased halo, then filled inward from their unmasked
    neighbors (simple diffusion inpainting)."""
    import numpy as np
    a = np.asarray(im).astype(float)
    x0, y0, x1, y1 = box
    core = pred(a[y0:y1, x0:x1])
    mask = np.zeros(a.shape[:2], bool)
    mask[y0:y1, x0:x1] = core
    for _ in range(grow):
        m = mask.copy()
        m[1:, :] |= mask[:-1, :]; m[:-1, :] |= mask[1:, :]
        m[:, 1:] |= mask[:, :-1]; m[:, :-1] |= mask[:, 1:]
        mask = m
    keep = ~mask
    while mask.any():
        acc = np.zeros_like(a); cnt = np.zeros(a.shape[:2])
        for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            sh_keep = np.roll(keep, (dy, dx), axis=(0, 1))
            sh_val = np.roll(a, (dy, dx), axis=(0, 1))
            acc += sh_val * sh_keep[..., None]
            cnt += sh_keep
        fill = mask & (cnt > 0)
        a[fill] = acc[fill] / cnt[fill][:, None]
        keep = keep | fill
        mask = mask & ~fill
    return Image.fromarray(a.clip(0, 255).astype("uint8"))


# (slide, output name, crop box or None, [(line-erase box in ORIGINAL coordinates, detector)])
QUIZ_FIGS = [
    (4, "l9-s04-gram-stain.jpg", (0, 20, 386, 456), []),
    (22, "l9-s22-gram-stain.jpg", (0, 22, 800, 578), []),
    (24, "l9-s24a-blood-agar.jpg", (0, 51, 386, 307), [((190, 51, 252, 108), dark_on_orange)]),
    (24, "l9-s24b-blood-agar.jpg", (412, 48, 800, 307), []),
    (34, "l9-s34a-skin.jpg", (0, 16, 385, 268), []),
    (42, "l9-s42-blood-agar.jpg", (0, 20, 604, 572), []),
    (49, "l9-s49-sputum.jpg", (18, 60, 753, 562), [((300, 60, 330, 330), grey_line),
                                                   ((580, 60, 700, 112), grey_line)]),
    (72, "l9-s72-urethral-pus.jpg", (0, 60, 668, 582),
     [((228, 60, 262, 282), grey_line), ((336, 180, 376, 372), grey_line),
      ((370, 262, 668, 286), grey_line)]),
]

# Guide figures: (slide, output name, crop box or None). Banners and photographer credits are
# kept on teaching figures; the figure caption carries the copyright line as L7/L8 do.
GUIDE_FIGS = [
    (4, "l9-s04-staphylococci.jpg", None),
    (11, "l9-s11-furuncle-carbuncle.jpg", None),
    (18, "l9-s18-catalase-coagulase.jpg", None),
    (22, "l9-s22-streptococci.jpg", None),
    (24, "l9-s24-hemolysis-flowchart.jpg", None),
    (26, "l9-s26-streptococcus-table.jpg", None),
    (29, "l9-s29-group-a-envelope.jpg", None),
    (42, "l9-s42-camp-test.jpg", None),
    (49, "l9-s49-pneumococci.jpg", None),
    (69, "l9-s69-ascending-gonorrhea.jpg", None),
    (72, "l9-s72-gonococci.jpg", None),
    (75, "l9-s75-meningococcus.jpg", None),
]


def picture(prs, slide):
    pics = [sh for sh in prs.slides[slide - 1].shapes if sh.shape_type == 13]
    assert len(pics) == 1, "slide %d has %d pictures" % (slide, len(pics))
    return Image.open(io.BytesIO(pics[0].image.blob)).convert("RGB")


def save(im, path):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    im.save(path, quality=86, optimize=True)
    return im.size


def main():
    prs = Presentation(DECK)
    assert len(prs.slides) == 79, len(prs.slides)
    os.makedirs(QUIZ, exist_ok=True)
    os.makedirs(GUIDE, exist_ok=True)
    out = {}
    for slide, name, box, lines in QUIZ_FIGS:
        im = picture(prs, slide)
        for lb, pred in lines:
            im = erase_lines(im, lb, pred)
        if box:
            im = im.crop(box)
        out["quiz/" + name] = save(im, os.path.join(QUIZ, name))
    for slide, name, box in GUIDE_FIGS:
        im = picture(prs, slide)
        if box:
            im = im.crop(box)
        out["guide/" + name] = save(im, os.path.join(GUIDE, name))
    for k, (w, h) in out.items():
        print("%-42s %4d x %4d" % (k, w, h))


if __name__ == "__main__":
    main()
