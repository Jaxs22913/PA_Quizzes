#!/usr/bin/env python3
"""Write the Lecture 18 (DNA Viruses of Medical Importance, Dr. Webster) pictures used by the Exam 3 Webster review
page into "Microbiology Exam 3/micro-exam-3-study-guide-images/" (descriptive names, guide copies; the quiz copies
have neutral numbered names, tools/extract_micro_e3_webster_quiz_images.py).

Lecture 14 and Lecture 17 pictures on the review page reuse the study guide's existing copies.
The deck stays outside the repo; only these pictures are written.

    python3 tools/extract_micro_e3_webster_guide_images.py
"""
import io, os
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/"
                          "Lecture 18  Dr. Webster -  DNA viruses of medical importance.pptx")
OUT = os.path.join(ROOT, "Microbiology Exam 3", "micro-exam-3-study-guide-images")
MAXW = 900

JOBS = [  # (slide, picture number in shape-tree order, name)
    (10, 1, "l18-s010-naked-and-enveloped.jpg"),
    (17, 1, "l18-s017-phage-cycles.jpg"),
    (22, 1, "l18-s022-animal-virus-entry.jpg"),
    (23, 1, "l18-s023-dna-virus-replication.jpg"),
    (27, 1, "l18-s027-effects-on-host-cells.jpg"),
    (30, 1, "l18-s030-dna-virus-groups.jpg"),
    (33, 1, "l18-s033-poxvirus.jpg"),
    (45, 1, "l18-s045-smallpox.jpg"),
    (56, 1, "l18-s056-herpesvirus.jpg"),
    (61, 1, "l18-s061-herpetic-whitlow.jpg"),
    (70, 1, "l18-s070-varicella-zoster.jpg"),
    (76, 2, "l18-s076-burkitt-lymphoma.jpg"),
    (82, 1, "l18-s082-roseola.jpg"),
    (84, 1, "l18-s084-kaposi-sarcoma.jpg"),
    (105, 1, "l18-s105-fifth-disease.jpg"),
]


def pictures(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from pictures(sh.shapes)
            continue
        try:
            sh.image
        except Exception:
            continue
        yield sh


def main():
    prs = Presentation(DECK)
    for n, k, name in JOBS:
        pics = list(pictures(prs.slides[n - 1].shapes))
        im = Image.open(io.BytesIO(pics[k - 1].image.blob))
        if im.mode in ("RGBA", "LA", "P"):
            bg = Image.new("RGB", im.size, "white")
            im = im.convert("RGBA")
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        im.save(os.path.join(OUT, name), quality=85)
        print("wrote %-40s %dx%d" % (name, im.width, im.height))


if __name__ == "__main__":
    main()
