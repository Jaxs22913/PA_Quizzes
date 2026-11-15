#!/usr/bin/env python3
"""Write the pictures for the two Microbiology Exam 3 Webster Review master exams into
"Microbiology Exam 3/micro-exam-3-quiz-images/".

Professor Webster said in her Exam 3 review (13 November 2026): "if I showed you a picture of them, it's possible
that you could need to identify the picture" and, closing the parasites, "if I give you a picture, be able to
recognize it". These are deck pictures for picture-identification items.

Neutral numbered names (memory quiz_image_filenames): wr3-fig-NN.jpg never names the answer. Each picture is the
whole embedded image when it carries no text naming the answer, or a crop that removes such text (crop boxes from
tools/extract_micro_l17_quiz_images.py, which read them off the original pixels).

Decks (outside the repo): Lecture 14 (Gram-negative bacilli), "Lecture 16 Dr. Webster Parasites ..." (= site
Lecture 17), Lecture 18 (DNA viruses).

    python3 tools/extract_micro_e3_webster_quiz_images.py --all   # every candidate (writers choose from these)
    python3 tools/extract_micro_e3_webster_quiz_images.py         # only the pictures the shipped exams use; prune rest
"""
import glob, io, os, re, sys
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
INBOX = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Microbiology Inbox/Exam 3/")
DECKS = {
    14: "Lecture 14  Dr. Webster Gram Negative Bacilli of Medical Importance.pptx",
    17: "Lecture 16 Dr. Webster Parasites of Medical Importance.pptx",
    18: "Lecture 18  Dr. Webster -  DNA viruses of medical importance.pptx",
}
OUT = os.path.join(ROOT, "Microbiology Exam 3", "micro-exam-3-quiz-images")
MAXW = 600

# (lecture, slide, picture number on the slide in shape-tree order counting group members, crop or None, name)
JOBS = [
    (14, 48, 2, None, "wr3-fig-01.jpg"),            # colonies with a metallic green sheen on a dark agar plate
    (14, 71, 2, None, "wr3-fig-02.jpg"),            # concentric swarming growth over an agar plate
    (17, 15, 2, None, "wr3-fig-03.jpg"),            # amebas in tissue (stained section)
    (17, 28, 1, None, "wr3-fig-04.jpg"),            # free-living ameba trophozoites (stained)
    (17, 38, 1, None, "wr3-fig-05.jpg"),            # stained flagellates from secretions
    (17, 40, 2, None, "wr3-fig-06.jpg"),            # pear-shaped flagellate in a stool smear
    (17, 40, 3, None, "wr3-fig-07.jpg"),            # oval cysts in a stool smear
    (17, 46, 1, None, "wr3-fig-08.jpg"),            # flagellates swimming between red blood cells
    (17, 60, 1, (0, 0, 512, 482), "wr3-fig-09.jpg"),  # ring forms inside red blood cells; labels cropped off
    (17, 76, 1, (0, 0, 760, 490), "wr3-fig-10.jpg"),  # acid-fast fecal smear; labels cropped off
    (17, 95, 3, None, "wr3-fig-11.jpg"),            # flattened-side eggs (no text)
    (17, 101, 1, None, "wr3-fig-12.jpg"),           # larvae coiled in muscle (no text)
    (17, 107, 1, None, "wr3-fig-13.jpg"),           # worm in the eye (no text)
    (17, 123, 2, None, "wr3-fig-14.jpg"),           # brain slice with cysts (no text)
    (17, 125, 1, None, "wr3-fig-15.jpg"),           # large cyst at surgery (no text)
    (18, 61, 1, None, "wr3-fig-16.jpg"),            # vesicular lesion of one finger (no text)
    (18, 84, 1, None, "wr3-fig-17.jpg"),            # discolored skin lumps on a patient (no text)
    (18, 105, 1, None, "wr3-fig-18.jpg"),           # red cheek rash on a child (no text)
    (18, 76, 2, None, "wr3-fig-19.jpg"),            # child with a grossly swollen jaw and cheek (no text)
    (18, 82, 1, None, "wr3-fig-20.jpg"),            # faint rash on a baby's trunk (no text)
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


def main(only=None):
    os.makedirs(OUT, exist_ok=True)
    decks = {}
    for lec, n, k, box, name in JOBS:
        if only is not None and name not in only:
            continue
        prs = decks.setdefault(lec, Presentation(INBOX + DECKS[lec]))
        pics = list(pictures(prs.slides[n - 1].shapes))
        assert len(pics) >= k, "L%d slide %d has %d picture(s)" % (lec, n, len(pics))
        im = Image.open(io.BytesIO(pics[k - 1].image.blob)).convert("RGB")
        if box:
            im = im.crop(box)
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        im.save(os.path.join(OUT, name), quality=85)
        print("wrote %-15s %dx%d  (L%d slide %d, picture %d)" % (name, im.width, im.height, lec, n, k))


def shipped():
    used = set()
    for f in glob.glob(os.path.join(ROOT, "Microbiology Exam 3", "micro-exam-3-webster-review-master-exam-*.html")):
        used |= set(re.findall(r"wr3-fig-\d\d\.jpg", open(f, encoding="utf-8").read()))
    return used


if __name__ == "__main__":
    if "--all" in sys.argv:
        main()
    else:
        keep = shipped()
        assert keep, "no rendered exam uses a wr3 picture; render first"
        main(only=keep)
        for f in sorted(os.listdir(OUT)):
            if f.startswith("wr3-fig-") and f not in keep:
                os.remove(os.path.join(OUT, f))
                print("removed", f, "(not in the shipped exams)")
