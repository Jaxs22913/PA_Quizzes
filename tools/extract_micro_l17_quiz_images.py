#!/usr/bin/env python3
"""Write the Lecture 17 (Parasites of Medical Importance, Dr. Webster) QUIZ pictures into
"Microbiology Exam 3/micro-exam-3-quiz-images/".

Quiz pictures get NEUTRAL, numbered file names (l17-fig-01.jpg ...; memory quiz_image_filenames): a picture opened
on its own must never name its answer. Numbers follow slide order and are fixed here, so a rebuild writes the same
names. The study guide keeps its own descriptive copies (micro-exam-3-study-guide-images/).

The deck file is "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx" (Dr. Webster's own count); the
syllabus and the calendar call it Lecture 17, and so does the site.

QUIZ images carry NO label that names the answer, so each is the whole picture when it has no text, or a crop:
    slide  22  the abdominal-wall abscess photograph (no text in the picture)
    slide  34  picture 2, the photomicrograph of the ciliated cell (no text); the labelled drawing is not used
    slide  38  the stained flagellates (no text)
    slide  40  picture 1, the drawing: the two trophozoites only; the "Nucleus" / "Ventral depression" labels above,
               the "Trophozoite" caption below and the cyst on the right cropped off
    slide  46  the blood smear (no text)
    slide  51  panel (a) only, the face; the heart, the tissue section, their labels and the panel letters cropped off
    slide  60  the smear only; the "Ring trophozoites" / "Red blood cell" labels on the right cropped off
    slide  67  picture 1, the left panel only (the computed tomography slice); the tissue panel cropped off
    slide  67  picture 2, the retinal photograph (no text)
    slide  76  the stained smear above the "Oocysts" / "Bacteria" labels (the scale bar stays)
    slide  90  picture 1, panel (a), the adult worms; panel (b) and the letters cropped off
    slide  90  picture 1, panel (b), the two eggs; panel (a) and the letters cropped off
    slide  93  the egg (no text)
    slide  95  picture 3, the eggs (no text)
    slide  97  picture 1, the lower photograph of panel (b), the mouth; the adults, the scales and the credit cropped
               off
    slide 101  the muscle section (no text)
    slide 105  the left panel, the blood film; the right panel cropped off
    slide 105  the right panel, the legs; the left panel cropped off
    slide 107  the eye photograph (no text)
    slide 114  picture 1, panel (b), the forked-tail larva; its caption and panels (a) and (c) cropped off
    slide 120  panel (a), the scolex photograph; the "Sucker" / "Hooklets" labels, the caption, panels (b) and (c)
               cropped off
    slide 123  picture 1, the lower brain scan only; the "Healthy brain" scan, both captions and the credit cropped
               off
    slide 123  picture 4, the heart with cysts (no text)
    slide 125  the operative photograph (no text)
Each crop box was read off the original pixels (a 50-pixel grid laid over each picture) and the result viewed.

    python3 tools/extract_micro_l17_quiz_images.py --all   # BEFORE partitioning: the partition checks every pool picture
    python3 tools/extract_micro_l17_quiz_images.py         # AFTER rendering: writes the shipped pictures, prunes the rest
"""
import io, os
from pptx import Presentation
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/"
                          "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx")
OUT = os.path.join(ROOT, "Microbiology Exam 3", "micro-exam-3-quiz-images")

# (slide, picture number on the slide in shape-tree order counting group members and placeholders,
#  crop box on the original pixels or None, name)
JOBS = [
    (22, 1, None, "l17-fig-01.jpg"),
    (34, 2, None, "l17-fig-02.jpg"),
    (38, 1, None, "l17-fig-03.jpg"),
    (40, 1, (0, 45, 390, 500), "l17-fig-04.jpg"),
    (46, 1, None, "l17-fig-05.jpg"),
    (51, 1, (0, 10, 242, 180), "l17-fig-06.jpg"),
    (60, 1, (0, 0, 512, 482), "l17-fig-07.jpg"),
    (67, 1, (0, 0, 398, 422), "l17-fig-08.jpg"),
    (67, 2, None, "l17-fig-09.jpg"),
    (76, 1, (0, 0, 760, 490), "l17-fig-10.jpg"),
    (90, 1, (0, 0, 490, 285), "l17-fig-11.jpg"),
    (90, 1, (0, 322, 490, 600), "l17-fig-12.jpg"),
    (93, 1, None, "l17-fig-13.jpg"),
    (95, 3, None, "l17-fig-14.jpg"),
    (97, 1, (510, 275, 726, 535), "l17-fig-15.jpg"),
    (101, 1, None, "l17-fig-16.jpg"),
    (105, 1, (0, 0, 280, 417), "l17-fig-17.jpg"),
    (105, 1, (318, 0, 592, 417), "l17-fig-18.jpg"),
    (107, 1, None, "l17-fig-19.jpg"),
    (114, 1, (172, 0, 362, 240), "l17-fig-20.jpg"),
    (120, 1, (5, 0, 243, 283), "l17-fig-21.jpg"),
    (123, 1, (0, 315, 253, 525), "l17-fig-22.jpg"),
    (123, 4, None, "l17-fig-23.jpg"),
    (125, 1, None, "l17-fig-24.jpg"),
]
MAXW = 600


def pictures(shapes):
    """Pictures, picture placeholders and grouped pictures, in shape-tree order."""
    from pptx.enum.shapes import MSO_SHAPE_TYPE
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from pictures(sh.shapes)
            continue
        try:
            sh.image
        except Exception:
            continue
        yield sh


def main(out=OUT, only=None):
    prs = Presentation(DECK)
    os.makedirs(out, exist_ok=True)
    for n, k, box, name in JOBS:
        if only and name not in only:
            continue
        pics = list(pictures(prs.slides[n - 1].shapes))
        assert len(pics) >= k, "slide %d has %d picture(s)" % (n, len(pics))
        im = Image.open(io.BytesIO(pics[k - 1].image.blob)).convert("RGB")
        if box:
            im = im.crop(box)
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        im.save(os.path.join(out, name), quality=85)
        print("wrote %-15s %dx%d  (slide %d, picture %d)" % (name, im.width, im.height, n, k))


def shipped():
    """The picture files the shipped Set 2 uses (tools/micro_l17_sets.json); the other numbers stay reserved for the
    held masters, so a plain run writes only what the quizzes show."""
    import json
    sets = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "micro_l17_sets.json")))
    return {os.path.basename(q["img"]) for qs in sets.values() for q in qs if q.get("img")}


if __name__ == "__main__":
    import sys
    if "--all" in sys.argv:          # every candidate picture (for the masters' partition)
        main(OUT)
    else:
        out = sys.argv[1] if len(sys.argv) > 1 else OUT
        keep = shipped()
        main(out, only=keep)
        for f in sorted(os.listdir(out)):        # prune the --all extras, so the public repo holds only shown pictures
            if f.startswith("l17-fig-") and f not in keep:
                os.remove(os.path.join(out, f))
                print("removed", f, "(not in the shipped sets)")
