#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 20 (Point-of-Care Ultrasound and Diagnostic Integration) figures for PDM I Exam 4: the ultrasound
images the quizzes ask the student to read, and the teaching figures for the guide.

Deck: "POCUS basics 2026.pptx" (Jordan Stores, PA-C, title slide; 17 November 2026). All 67 slides were rendered
(Keynote export to PDF, PyMuPDF at 1920 px wide) and every slide viewed before anything was chosen. Slide images are
cleared for use provided the slide is cited. Most crops are taken from that 1920 px render (box coordinates below are
in its pixels); the gallstone quiz picture is the slide 16 picture itself (the embedded file carries none of the
slide's overlaid "stones" text).

NOT AVAILABLE: slide 18 ("Mirroring artifact on cardiac pocus"), the right half of slide 39 ("Lung sliding vs no
sliding") and the right half of slide 42 ("pneumonia") are links to videos kept outside the deck; the deck holds only
black placeholders, so nothing from them is used. Slide 38 (lung sliding) is a single still of a moving clip and shows
nothing a still can teach. Slides 20, 32, 33 and 57 to 61 are pictures with no slide text (their meaning is in the
speaker notes, which do not count), so they are not used as figures or questions.

QUIZ images carry NO label that names the answer (labels are painted over in black, the ultrasound background) and
are written under neutral numbered names, pocus-fig-NN.jpg, in a fixed order. The guide copies keep their labels.
Number 03 (slide 16, rib shadows) was dropped: its labels sit on the shadows, so masking them hid the finding.

The render folder defaults to the session scratchpad (render/pocus_hi/sNNN.png); pass another with --render.
"""
import io, os, sys
from PIL import Image, ImageDraw
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Principles of Diagnostic Medicine I Inbox/Exam 4/POCUS basics 2026.pptx")
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
QUIZ = os.path.join(FOLDER, "pdm-exam-4-quiz-images")
GUIDE = os.path.join(FOLDER, "pdm-exam-4-study-guide-images")
RENDER = "/private/tmp/claude-501/-Users-jaxonluke/e06779a5-ab02-4065-a6fc-fe88e20d1bfd/scratchpad/render/pocus_hi"
if "--render" in sys.argv:
    RENDER = sys.argv[sys.argv.index("--render") + 1]
MAXW = 760

# QUIZ: (number, slide, crop box, masks) -- masks are boxes painted black BEFORE the crop.
# "blob:<shape id>" in place of a box takes the embedded picture of that shape instead of the render.
QUIZ_FIGS = [
 (1, 14, (1160, 612, 1895, 1025), [(1625, 625, 1800, 740)]),                 # free fluid in Morison's pouch
 (2, 14, (470, 690, 990, 1050), [(895, 720, 992, 795), (900, 855, 992, 900), (560, 955, 780, 1005)]),  # A lines
 (4, 16, "blob:251", []),                                                    # gallstones with shadowing
 (5, 17, (1170, 160, 1870, 810), []),                                        # edge artifact (red arrow kept)
 (6, 17, (480, 660, 1045, 1045), [(530, 915, 670, 980)]),                    # mirror image
 (7, 19, (764, 240, 1810, 970), [(1395, 600, 1705, 690), (835, 680, 1055, 765)]),  # spine sign
 (8, 21, (414, 536, 936, 916), [(630, 695, 775, 750)]),                      # side lobe
 (9, 21, (1084, 524, 1604, 930), [(1084, 812, 1340, 872)]),                  # ring down (pneumobilia)
 (10, 22, (516, 232, 1732, 916), [(700, 236, 1470, 325), (690, 565, 805, 615)]),  # A lines (normal lung)
 (11, 23, (948, 606, 1610, 1054), []),                                       # B lines
 (12, 23, (310, 630, 756, 1054), []),                                        # comet tails (gallbladder)
 (13, 26, (0, 274, 844, 876), [(0, 280, 215, 372), (300, 525, 390, 565), (290, 665, 425, 735)]),  # seashore
 (14, 26, (940, 264, 1660, 790), [(955, 345, 1250, 392)]),                   # barcode
 (15, 31, (226, 466, 1096, 1070), []),                                       # parasternal long axis
 (16, 34, (334, 644, 914, 1076), []),                                        # parasternal short axis
 (17, 35, (296, 560, 910, 1054), [(296, 1000, 525, 1040)]),                  # subxiphoid
 (18, 36, (330, 592, 846, 1070), []),                                        # apical four chamber
 (19, 40, (1096, 274, 1764, 1044), []),                                      # B lines (edema)
 (20, 41, (480, 180, 1440, 896), []),                                        # pleural effusion
 (21, 44, (1016, 30, 1576, 516), [(1285, 110, 1385, 155), (1115, 225, 1200, 260), (1335, 338, 1575, 375)]),  # stone + shadow
 (22, 44, (1000, 570, 1364, 880), []),                                       # wall thickening
 (23, 44, (1404, 570, 1850, 830), [(1498, 625, 1556, 665)]),                 # pericholecystic fluid
 (24, 47, (1450, 470, 1748, 708), []),                                        # cellulitis (cobblestoning)
 (25, 47, (160, 736, 540, 1012), []),                                        # abscess
 (26, 51, (940, 270, 1756, 1000), []),                                       # right upper quadrant free fluid
 (27, 52, (1236, 340, 1836, 904), [(1520, 372, 1690, 422)]),                 # left upper quadrant free fluid
 (28, 55, (924, 334, 1680, 936), [(1235, 775, 1420, 822)]),                  # lung point
]

# GUIDE: (slide, crop box, output stem) -- labels kept.
GUIDE_FIGS = [
 (8, (1040, 70, 1830, 860), "pocus-probes-frequency"),
 (9, (20, 669, 1062, 1049), "pocus-transducers-movements"),
 (10, (0, 0, 1920, 1080), "pocus-vs-traditional"),
 (13, (201, 50, 1729, 1015), "pocus-indicator"),
 (14, (470, 690, 990, 1050), "pocus-lung-labeled"),
 (14, (1160, 612, 1895, 1025), "pocus-morison-free-fluid"),
 (15, (261, 265, 1578, 1039), "pocus-planes"),
 (16, (1040, 75, 1690, 535), "pocus-rib-shadows"),
 (16, (1045, 545, 1650, 1000), "pocus-gallstone-shadowing"),
 (16, (420, 765, 925, 1070), "pocus-posterior-enhancement"),
 (17, (1170, 160, 1870, 810), "pocus-edge-artifact"),
 (17, (480, 660, 1045, 1045), "pocus-mirror-image"),
 (19, (764, 240, 1810, 970), "pocus-spine-sign"),
 (21, (414, 524, 1604, 930), "pocus-sidelobe-ringdown"),
 (22, (516, 232, 1732, 916), "pocus-a-lines"),
 (23, (310, 606, 1610, 1054), "pocus-comet-b-lines"),
 (26, (0, 264, 1660, 876), "pocus-m-mode-seashore-barcode"),
 (27, (328, 60, 1630, 963), "pocus-m-mode-fetal"),
 (28, (291, 446, 1608, 939), "pocus-color-doppler"),
 (30, (261, 30, 1810, 1046), "pocus-cardiac-windows"),
 (31, (1268, 50, 1906, 930), "pocus-psla"),
 (34, (1100, 56, 1816, 1044), "pocus-pssa"),
 (35, (1214, 195, 1780, 1076), "pocus-subxiphoid"),
 (36, (1296, 40, 1790, 594), "pocus-apical-four"),
 (36, (1036, 614, 1830, 1044), "pocus-five-chamber"),
 (37, (40, 374, 438, 798), "pocus-lung-probes"),
 (37, (1287, 589, 1886, 1011), "pocus-blue-protocol"),
 (40, (426, 274, 1764, 1044), "pocus-pulmonary-edema"),
 (41, (480, 180, 1440, 896), "pocus-pleural-effusion"),
 (44, (70, 30, 1850, 880), "pocus-gallbladder"),
 (45, (144, 560, 1604, 1050), "pocus-ivc"),
 (46, (637, 60, 1866, 1045), "pocus-aorta-ivc"),
 (47, (160, 56, 1760, 1060), "pocus-soft-tissue"),
 (49, (949, 0, 1830, 1076), "pocus-dvt"),
 (50, (798, 462, 1803, 1066), "pocus-efast"),
 (51, (165, 0, 1755, 1080), "pocus-ruq-free-fluid"),
 (52, (100, 310, 1836, 904), "pocus-luq"),
 (53, (0, 235, 1815, 911), "pocus-pelvis"),
 (54, (291, 100, 1632, 979), "pocus-subxiphoid-labeled"),
 (55, (290, 266, 1680, 1000), "pocus-lung-point"),
]


def blob(slide, shape_id):
    prs = Presentation(DECK)
    for sh in prs.slides[slide - 1].shapes:
        if sh.shape_id == shape_id:
            return Image.open(io.BytesIO(sh.image.blob)).convert("RGB")
    raise SystemExit("slide %d: no shape %d" % (slide, shape_id))


def render(slide):
    return Image.open(os.path.join(RENDER, "s%03d.png" % slide)).convert("RGB")


def save(im, path):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    im.save(path, quality=88)
    return im.size


def main():
    os.makedirs(QUIZ, exist_ok=True)
    os.makedirs(GUIDE, exist_ok=True)
    for n, slide, box, masks in QUIZ_FIGS:
        if isinstance(box, str):
            im = blob(slide, int(box.split(":")[1]))
        else:
            im = render(slide)
            d = ImageDraw.Draw(im)
            for m in masks:
                d.rectangle(m, fill=(0, 0, 0))
            im = im.crop(box)
        out = os.path.join(QUIZ, "pocus-fig-%02d.jpg" % n)
        print("quiz  %-18s slide %2d %s" % (os.path.basename(out), slide, save(im, out)))
    for slide, box, stem in GUIDE_FIGS:
        out = os.path.join(GUIDE, stem + ".jpg")
        print("guide %-36s slide %2d %s" % (os.path.basename(out), slide, save(render(slide).crop(box), out)))


if __name__ == "__main__":
    main()
