#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 40 (Obstructive Sleep Apnea and Obesity Hypoventilation Syndrome, Shah) figures for
the CMS I Exam 7 study guide.

    python3 tools/extract_cms_e7_l40_figures.py

Deck: "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome - Shah Fallsv.pptx" (38 slides).
Every slide was viewed at 1920 px; only slides 14 and 17 carry pictures. Slide images are cleared for use
provided the slide is cited (each figure cites it). All are the original embedded blobs, uncropped; the
license note printed under the questionnaire stays.

Taken (guide subsection):
  slide 17  the STOP-Bang questionnaire (the slide's table is a picture), enlarged 1.5x so its text
            reads: 2.5 Screening, beside the HTML table of the same questionnaire
  slide 14  two of its three photographs, a positive airway pressure mask over the nose and one over
            the nose and mouth, each tubed to a bedside machine: 2.6 Management

Left out:
  slide 14  the third photograph (a man with a small device over the nostrils): the slide names no
            device, so it could not be captioned from the slide.
  every other slide is text only.
"""
import io, os, sys
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 7/"
    "CMS I Obstructive Sleep Apnea & Obesity Hypoventilation Syndrome - Shah Fallsv.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-e7-images")
MAXW = 1400

# (slide, picture shape id, output file, scale)
FIGS = [
    (17, 5, "l40-s017-stop-bang.png", 1.5),
    (14, 3, "l40-s014-pap-nasal-mask.jpg", 1.0),
    (14, 1026, "l40-s014-pap-full-face-mask.jpg", 1.0),
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
