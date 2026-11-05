#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 39 (Phases of Sleep, Shah) figures for the CMS I Exam 7 study guide.

    python3 tools/extract_cms_e7_l39_figures.py

Deck: "CMS 1 Phases of Sleep - Shah Fallsv.pptx" (31 slides). Every slide was viewed at 1920 px before
anything was chosen. Slide images are cleared for use provided the slide is cited (each figure cites it).
Every picture is the original embedded blob (none is built from shapes). These are small line drawings
(230 to 610 px wide), so each is enlarged 1.5-2x with Lanczos so it reads at guide width; nothing is
cropped or retouched.

Taken (guide subsection):
  slide 7   the night's sleep-stage graph (hypnogram): 1.2 Sleep architecture
  slide 21  the four normal EEG waveforms on one time scale: 1.7 The four waveforms
  slide 24  the eyes-open / eyes-closed trace (alpha replaced, then back): 1.7
  slide 29  the EEG from alert wakefulness down to stage 4 sleep: 1.8 EEG changes

Left out:
  slide 4         five memes / cartoons (decoration).
  slides 22, 23, 25, 26  each is one strip cut from the slide 21 picture (duplicates).
  slide 28        a real slide table, already in the guide as an HTML table (1.8); no picture needed.
  all other slides are text only.
"""
import io, os, sys
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 7/"
    "CMS 1 Phases of Sleep - Shah Fallsv.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-e7-images")
MAXW = 1400

# (slide, picture shape id, output file, scale)
FIGS = [
    (7, 5, "l39-s007-hypnogram.png", 2.0),
    (21, 5, "l39-s021-eeg-four-waves.png", 1.5),
    (24, 5, "l39-s024-alpha-eyes-open-closed.png", 2.0),
    (29, 5, "l39-s029-eeg-wake-to-deep-sleep.png", 2.0),
]


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


def save(im, path):
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        im = bg
    im = im.convert("RGB")
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
    for slide, sid, name, scale in FIGS:
        if (slide, sid) not in pics:
            sys.exit("missing picture: slide %d shape %d" % (slide, sid))
        im = Image.open(io.BytesIO(pics[(slide, sid)]))
        if scale != 1:
            im = im.convert("RGBA").resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        (w, h), size = save(im, os.path.join(OUT, name))
        total += size
        print("%-40s %4dx%-4d %6.1f KB" % (name, w, h, size / 1024))
    print("total %.1f KB" % (total / 1024))


if __name__ == "__main__":
    main()
