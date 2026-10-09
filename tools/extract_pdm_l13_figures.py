#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 13 (Ventricular Dysrhythmias and Atrioventricular Blocks) figures
for PDM I Exam 3: the rhythm strips for the quizzes and the teaching figures for the guide.

Deck: "13. Ventricular Dysrhythmias and Atrioventricular Blocks.pptx" (Scott Mathis, title
slide). Every picture in the deck was extracted and viewed at full size before it was
chosen here. Slide images are cleared for use provided the slide is cited.

QUIZ strips carry NO label that names the rhythm. Most deck strips are bare already (the
deck lays its own labels over them as separate text boxes, which extraction leaves behind);
three were cropped because the label is baked into the picture:
  slide 16  the PEA picture carries the slide title and an "IF NO PULSE WITH THIS RHYTHM?"
            box -- cropped to the strip above the box
  slide 20  "Ventricular pacing" bar across the top -- cropped off
  slide 21  "Atrial and ventricular pacing" bar across the top -- cropped off
  slide 23  the 1-degree AV block teaching card -- cropped to its strip (title, heart
            diagram and criteria removed)
  slide 11  the green two-strip torsades tracing -- top strip only

Left out of the quizzes: slide 12 (a video poster of an echocardiogram), slide 17's second
picture (paroxysmal standstill: arrows and a monitor "PULSE 108" reading would mislead
without context; it goes in the guide), the labeled Mobitz II and third-degree teaching
diagrams (slides 36, 43) and the four-panel summary (slide 49) -- all guide-only.

THE PAIR ON SLIDES 31 AND 38 LOOKS IDENTICAL AND IS NOT. Both are the same three-beat
drawing with a dropped QRS; measured at 3x, slide 31's PR intervals lengthen beat to beat
(Wenckebach) and slide 38's stay fixed (Mobitz II). They are a deliberate contrast pair and
both are used, each keyed to its own slide's answer table (32 and 39).

GUIDE figures keep their labels (the guide names the rhythm; the quizzes never do).
"""
import io, os, re, zipfile
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Principles of Diagnostic Medicine I Inbox/Exam 3/"
    "13. Ventricular Dysrhythmias and Atrioventricular Blocks.pptx")
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3")
QUIZ = os.path.join(FOLDER, "pdm-exam-3-quiz-images")
GUIDE = os.path.join(FOLDER, "pdm-exam-3-study-guide-images")
MAXW = 1200

# (slide, picture shape id, output stem, destinations, crop box or None, white masks)
FIGS = [
 (5, 5, "l13-ventricular-tachycardia-a", "QG", None, []),
 (7, 5, "l13-ventricular-tachycardia-b", "QG", None, []),
 (9, 6, "l13-ventricular-tachycardia-c", "Q", None, []),
 (5, 4, "l13-torsades-a", "QG", None, []),
 (11, 5, "l13-torsades-b", "Q", (0, 0, 570, 150), []),
 (11, 6, "l13-torsades-c", "QG", None, []),
 (11, 4, "l13-torsades-d", "Q", None, []),
 (14, 4, "l13-ventricular-fibrillation-a", "QG", None, []),
 (14, 5, "l13-ventricular-fibrillation-b", "QG", None, []),
 (14, 6, "l13-ventricular-fibrillation-c", "Q", None, []),
 (15, 5, "l13-vf-to-asystole", "QG", None, []),
 (15, 4, "l13-asystole-a", "Q", None, []),
 (15, 6, "l13-asystole-b", "QG", None, []),
 (16, 4, "l13-pea-organized-rhythm", "Q", (125, 200, 845, 445), []),
 (16, 4, "l13-pea-slide", "G", None, []),
 (17, 4, "l13-ventricular-standstill", "QG", None, []),
 (17, 5, "l13-paroxysmal-ventricular-standstill", "G", None, []),
 (19, 5, "l13-atrial-paced", "QG", None, []),
 (20, 5, "l13-ventricular-paced", "Q", (0, 46, 1024, 162), []),
 (20, 5, "l13-ventricular-paced-labeled", "G", None, []),
 (21, 5, "l13-atrial-ventricular-paced", "Q", (0, 44, 1024, 203), []),
 (21, 5, "l13-atrial-ventricular-paced-labeled", "G", None, []),
 (23, 5, "l13-first-degree-cartoon", "G", None, []),
 (23, 7, "l13-first-degree-block-c", "Q", (343, 135, 858, 263), []),
 (25, 6, "l13-first-degree-block-a", "QG", None, []),
 (27, 8, "l13-first-degree-block-b", "Q", None, []),
 (29, 5, "l13-wenckebach-diagram", "G", None, []),
 (31, 6, "l13-wenckebach-a", "QG", None, []),
 (33, 6, "l13-wenckebach-b", "Q", None, []),
 (36, 5, "l13-mobitz-ii-diagram", "G", None, []),
 (38, 6, "l13-mobitz-ii-a", "QG", None, []),
 (40, 6, "l13-mobitz-ii-b", "Q", None, []),
 (43, 5, "l13-third-degree-diagram", "G", None, []),
 (45, 6, "l13-third-degree-block-a", "QG", None, []),
 (47, 6, "l13-third-degree-block-b", "Q", None, []),
 (49, 5, "l13-heart-block-summary", "G", None, []),
]


def blobs():
    """{(slide, shape id): bytes}, including pictures python-pptx cannot type (.bin media)."""
    out = {}
    prs = Presentation(DECK)
    z = zipfile.ZipFile(DECK)
    for i, s in enumerate(prs.slides, 1):
        rels = {r.rId: r.target_ref for r in s.part.rels.values()}
        for sh in s.shapes:
            el = sh._element
            emb = el.xpath('.//a:blip/@r:embed')
            if not emb:
                continue
            tgt = rels.get(emb[0])
            if not tgt or "media/" not in tgt:
                continue
            path = "ppt/media/" + tgt.split("media/")[-1]
            out[(i, sh.shape_id)] = z.read(path)
    return out


def main():
    os.makedirs(QUIZ, exist_ok=True)
    os.makedirs(GUIDE, exist_ok=True)
    B = blobs()
    for slide, sid, stem, dest, crop, masks in FIGS:
        assert (slide, sid) in B, "slide %d has no picture %d" % (slide, sid)
        im = Image.open(io.BytesIO(B[(slide, sid)]))
        fmt = im.format
        if im.mode in ("P", "RGBA", "LA"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, "white")
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        if crop:
            im = im.crop(crop)
        for box in masks:
            im.paste((255, 255, 255), box)
        if im.width < 700:                         # small deck strips read badly at natural size
            f = min(4, -(-800 // im.width))
            im = im.resize((im.width * f, im.height * f), Image.LANCZOS)
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        ext = ".jpg" if fmt == "JPEG" and not masks else ".png"
        for d in ([QUIZ] if "Q" in dest else []) + ([GUIDE] if "G" in dest else []):
            p = os.path.join(d, stem + ext)
            if ext == ".jpg":
                im.save(p, quality=92)
            else:
                im.save(p, optimize=True)
                if os.path.getsize(p) > 200 * 1024:      # a photographed tracing: JPEG is a tenth the size
                    os.remove(p)
                    p = p[:-4] + ".jpg"
                    im.save(p, quality=90)
            print("%-6s slide %2d  %-44s %4dx%-4d %3d KB" % (os.path.basename(d)[11:16], slide, os.path.basename(p),
                  im.width, im.height, os.path.getsize(p) // 1024))


if __name__ == "__main__":
    main()
