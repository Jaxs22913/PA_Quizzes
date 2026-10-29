#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 19 (Acid-Base Balance and Blood Gas Interpretation) figures for PDM I Exam 4.

Deck: "Acid Base Balance and Blood Gas Interpretation mbf2026sc.pptx" (Megan B. Finck, MMS, PA-C, title slide;
27 October 2026). All 56 slides were read: 51 are text only (placeholders, no tables, charts or groups;
checked shape by shape), and the deck holds five pictures, every one viewed at full size before use:
  slide 6   three photographs of the Allen test (the slide's own source line names Bates' Chapter 17);
  slide 38  the oxygen-hemoglobin dissociation curve, with "Oxygenated blood leaving the lungs" and
            "Reduced blood returning from tissues" bracketed on it;
  slide 39  the curve at pH 7.6, 7.4 and 7.2 with the list "Shift to right: (1) Increased hydrogen ions
            (2) Increased CO2 (3) Increased temperature (4) Increased BPG". (The picture's left axis carries a
            duplicated 0-100 scale; the curves and labels are what is read.)
Slide images are cleared for use provided the slide is cited.

QUIZ images carry NO label that names the answer, and are numbered (quiz_image_filenames):
  l19-fig-01  slide 6, the three photographs side by side (nothing to mask: they carry no text).
  l19-fig-02  slide 39 with the "Shift to right" list removed (the pH labels stay: the item asks for
              another cause of the right shift, which the removed list names).
  l19-fig-03  slide 38 with both bracket labels removed (the brackets stay; the item asks which blood the
              lower, low-pressure bracket marks).
Text is removed box by box and the light grid through the box is redrawn from just outside it.
The guide keeps every picture whole, under descriptive names.
"""
import io, os, zipfile
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Principles of Diagnostic Medicine I Inbox/Exam 4/"
    "Acid Base Balance and Blood Gas Interpretation mbf2026sc.pptx")
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
QUIZ = os.path.join(FOLDER, "pdm-exam-4-quiz-images")
GUIDE = os.path.join(FOLDER, "pdm-exam-4-study-guide-images")
WHITE = (255, 255, 255)

# label boxes in each picture's own pixels; only the dark lettering inside is removed
S38_LABELS = [(376, 54, 586, 108), (228, 218, 502, 280)]
S39_LIST = [(330, 262, 762, 462)]
# slide 38's grid, every 20 mm Hg and every 20%: two-pixel lines measured on the picture
S38_GRID = ((165, 166, 243, 244, 321, 322, 399, 400, 477, 478, 555, 556), (91, 92, 169, 170, 247, 248))
GRID = (199, 199, 199)


def blobs():
    """{(slide, shape id): bytes}, read straight from the package."""
    out = {}
    prs = Presentation(DECK)
    z = zipfile.ZipFile(DECK)
    for i, s in enumerate(prs.slides, 1):
        rels = {r.rId: r.target_ref for r in s.part.rels.values()}
        for sh in s.shapes:
            emb = sh._element.xpath('.//a:blip/@r:embed')
            tgt = rels.get(emb[0]) if emb else None
            if tgt and "media/" in tgt:
                out[(i, sh.shape_id)] = z.read("ppt/media/" + tgt.split("media/")[-1])
    return out


def rgb(b):
    im = Image.open(io.BytesIO(b))
    if im.mode in ("P", "RGBA", "LA") or "transparency" in im.info:
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, WHITE)
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def erase_text(im, boxes, grid=((), ())):
    """White out each box, then redraw the light grid lines (columns, rows: measured on the picture) that
    ran through it, so only the lettering goes."""
    im = im.copy()
    px = im.load()
    cols, rows = grid
    for x0, y0, x1, y1 in boxes:
        for x in range(x0, x1):
            for y in range(y0, y1):
                px[x, y] = WHITE
        for x in cols:
            if x0 <= x < x1:
                for y in range(y0, y1):
                    px[x, y] = GRID
        for y in rows:
            if y0 <= y < y1:
                for x in range(x0, x1):
                    px[x, y] = GRID
    return im


def side_by_side(parts, gap=12):
    h = max(p.height for p in parts)
    out = Image.new("RGB", (sum(p.width for p in parts) + gap * (len(parts) - 1), h), WHITE)
    x = 0
    for p in parts:
        out.paste(p, (x, 0)); x += p.width + gap
    return out


def save(im, path, scale=1):
    if scale != 1:
        im = im.resize((im.width * scale, im.height * scale), Image.LANCZOS)
    im.save(path, quality=90)
    print("%-62s %4dx%-4d %3d KB" % (os.path.relpath(path, ROOT), im.width, im.height, os.path.getsize(path) // 1024))


def main():
    os.makedirs(QUIZ, exist_ok=True)
    os.makedirs(GUIDE, exist_ok=True)
    B = blobs()
    allen = side_by_side([rgb(B[(6, n)]) for n in (4, 5, 6)])
    s38, s39 = rgb(B[(38, 1026)]), rgb(B[(39, 4)])
    save(allen, os.path.join(GUIDE, "l19-allen-test.jpg"), 2)
    save(s38, os.path.join(GUIDE, "l19-oxygen-curve.jpg"))
    save(s39, os.path.join(GUIDE, "l19-curve-shift.jpg"))
    save(allen, os.path.join(QUIZ, "l19-fig-01.jpg"), 2)
    save(erase_text(s39, S39_LIST), os.path.join(QUIZ, "l19-fig-02.jpg"))
    save(erase_text(s38, S38_LABELS, S38_GRID), os.path.join(QUIZ, "l19-fig-03.jpg"))


if __name__ == "__main__":
    main()
