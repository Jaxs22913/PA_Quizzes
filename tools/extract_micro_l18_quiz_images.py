#!/usr/bin/env python3
"""Write the Lecture 18 (DNA Viruses of Medical Importance, Dr. Webster) QUIZ pictures into
"Microbiology Exam 3/micro-exam-3-quiz-images/".

Quiz pictures get NEUTRAL, numbered file names (l18-fig-01.jpg ...; memory quiz_image_filenames): a picture opened
on its own must never name its answer. Numbers follow slide order and are fixed here. The study guide keeps its own
descriptive copies (micro-exam-3-study-guide-images/). Same machinery as tools/extract_micro_l17_quiz_images.py.

QUIZ images carry NO label that names the answer, so each is the whole picture when it has no text, or a crop:
    slide  45  panel (b), the arm with pustules; panel (a), the letters and the credits cropped off
    slide  46  picture 2, the face with tumor-like growths (no text)
    slide  47  picture 2, the four-photograph panel of pustular rash (no text)
    slide  53  the two arm photographs (only the letters A and B)
    slide  54  picture 2, the ulcerated hand (no text)
    slide  62  the vesicular skin photograph (no text)
    slide  63  the cluster of vesicles (no text)
    slide  65  the infant (a faint caption line along the top cropped off)
    slide  67  the Pap smear micrograph; the "Giant cell with multiple nuclei", "Normal cells" and "Inclusion" labels
               cropped off (leader lines remain)
    slide  70  the left panel, the child with a vesicular rash; the diagram and the right panel cropped off
    slide  70  the right panel, the rash across one shoulder and arm; the rest and the "(c)" cropped off
    slide  76  picture 1, the throat (labels Rash, Tonsil, Exudate only)
    slide  80  panel (b), the large atypical lymphocyte; panel (a) and the label row above cropped off
    slide  84  picture 2, the purple oral lesion (no text)
    slide  98  panel (a), the hand with warts; panel (b) and its "Condylomata acuminata" label cropped off
    slide 100  the Pap smear; the "Koilocyte" / "Normal cervical cell" labels cropped off (leader lines remain)
Each crop box was read off the original pixels (a 50-pixel grid laid over each picture) and the result viewed.

    python3 tools/extract_micro_l18_quiz_images.py --all   # BEFORE partitioning: the partition checks every pool picture
    python3 tools/extract_micro_l18_quiz_images.py         # AFTER rendering: writes the shipped pictures, prunes the rest
"""
import io, os
from pptx import Presentation
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/"
                          "Lecture 18  Dr. Webster -  DNA viruses of medical importance.pptx")
OUT = os.path.join(ROOT, "Microbiology Exam 3", "micro-exam-3-quiz-images")

# (slide, picture number on the slide in shape-tree order counting group members and placeholders,
#  crop box on the original pixels or None, name)
JOBS = [
    (45, 1, (360, 0, 940, 378), "l18-fig-01.jpg"),
    (46, 2, None, "l18-fig-02.jpg"),
    (47, 2, None, "l18-fig-03.jpg"),
    (53, 1, None, "l18-fig-04.jpg"),
    (54, 2, None, "l18-fig-05.jpg"),
    (62, 1, None, "l18-fig-06.jpg"),
    (63, 1, None, "l18-fig-07.jpg"),
    (65, 1, (0, 8, 812, 467), "l18-fig-08.jpg"),
    (67, 1, (100, 55, 550, 435), "l18-fig-09.jpg"),
    (70, 1, (50, 8, 270, 330), "l18-fig-10.jpg"),
    (70, 1, (700, 8, 962, 230), "l18-fig-11.jpg"),
    (76, 1, None, "l18-fig-12.jpg"),
    (80, 1, (45, 300, 300, 520), "l18-fig-13.jpg"),
    (84, 2, None, "l18-fig-14.jpg"),
    (98, 1, (80, 0, 460, 230), "l18-fig-15.jpg"),
    (100, 1, (25, 30, 535, 444), "l18-fig-16.jpg"),
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
    """The picture files the shipped Set 2 uses (tools/micro_l18_sets.json); the other numbers stay reserved for the
    held masters, so a plain run writes only what the quizzes show."""
    import json
    sets = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "micro_l18_sets.json")))
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
            if f.startswith("l18-fig-") and f not in keep:
                os.remove(os.path.join(out, f))
                print("removed", f, "(not in the shipped sets)")
