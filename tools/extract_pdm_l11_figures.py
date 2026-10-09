#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the PDM I Lecture 11 (Rhythm Analysis and Sinus Rhythms, Scott Mathis) figures.

Two destinations, both inside "Principles of Diagnostic Medicine I Exam 3/":
  pdm-exam-3-quiz-images/         strips shown ABOVE a question stem. Every on-image
                                  label that names the rhythm is CROPPED AWAY here
                                  (the Mobitz title on slide 59, the "Sinus Block" and
                                  "SA Exit Block" titles on slides 87 and 89, the
                                  descriptive caption under the slide 53 strip).
  pdm-exam-3-study-guide-images/  figures for the guide, labels KEPT (the guide is
                                  where the strip is named and explained).

Files are keyed by the deck's own MEDIA filename (stable, unlike the .rels order; see
memory lettered_slide_images) and every entry asserts the slide really carries that
media, so a re-exported deck fails loudly instead of quietly swapping a strip.
Output files are named for what they show, prefixed l11- so they cannot collide with
the other Exam 3 lectures' figures.

Every picture below was viewed at full size before it was listed (2026-10-08):
  * The deck's "Sinus pause" and "Sinus arrest" criteria slides (92 and 96) are a
    PICTURE of the sinus exit block criteria table, not a table of their own.
  * Slides 50 and 51 (count-down method examples) state no rate, so they are not used.
  * Slide 93's sinus pause strip measures about 3.2 R to R intervals across the pause,
    too close to a whole multiple to tell from exit block by eye, so the quizzes use the
    slide 91 diagram strip (a gap of about 1.4 cycles) instead.
  * The slide 87 strip's arrows mark the marched-out schedule, which is the answer to any
    exit block question, so the quizzes use the slide 89 strip with its tick marks and
    second labels cropped off ("-plain"), alongside the labeled copy ("-timed").
  * Small strips are upscaled (Lanczos, up to 3x) so they read at quiz width; nothing
    is redrawn.
"""
import io, os, re, zipfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 3")
QUIZ = os.path.join(DIR, "pdm-exam-3-quiz-images")
GUIDE = os.path.join(DIR, "pdm-exam-3-study-guide-images")
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Principles of Diagnostic Medicine I Inbox/Exam 3/"
    "11. Rhythm Analysis and Sinus Rhythm.pptx")

# (slide, deck media file, destination, output name, crop box (l, t, r, b) or None)
Q, G = "quiz", "guide"
FIGS = [
    # ---- quiz strips (labels that give the answer away are cropped) ----
    (45, "image28.jpeg", Q, "l11-s045-six-second-strip-nine-complexes.jpg", None),
    (46, "image29.jpeg", Q, "l11-s046-six-second-strip-fourteen-complexes.jpg", None),
    (47, "image30.jpeg", Q, "l11-s047-six-second-strip-thirteen-complexes.jpg", None),
    (53, "image32.jpeg", Q, "l11-s053-regular-strip-four-large-boxes.jpg", (0, 0, 440, 99)),
    (56, "image38.jpeg", Q, "l11-s056-irregular-strip.jpg", None),
    (58, "image41.jpeg", Q, "l11-s058-normal-sinus-rhythm.jpg", None),
    (59, "image42.jpeg", Q, "l11-s059-lengthening-pr-interval.jpg", (0, 20, 427, 118)),
    (61, "image44.jpeg", Q, "l11-s061-wide-qrs-lead-v1.jpg", None),
    (76, "image56.png", Q, "l11-s076-sinus-bradycardia.png", None),
    (79, "image57.jpeg", Q, "l11-s079-sinus-tachycardia.jpg", None),
    (83, "image59.png", Q, "l11-s083-sinus-arrhythmia.png", (0, 0, 355, 119)),
    (87, "image61.jpeg", Q, "l11-s087-sinus-exit-block-marked.jpg", (0, 40, 413, 122)),
    (89, "image62.jpeg", Q, "l11-s089-sinus-exit-block-timed.jpg", (0, 17, 496, 101)),
    (93, "image65.jpeg", Q, "l11-s093-sinus-pause.jpg", (0, 0, 397, 112)),
    # 2026-10-08 fact-check: the slide 87 strip's arrows draw the march-out answer, and the slide
    # 93 pause is about 3.2 cycles long (too close to a whole multiple to refute exit block by
    # eye). These two crops replace them in the quizzes: slide 89 without its tick marks and
    # second labels, and the slide 91 diagram above its timing line (gap about 1.4 cycles).
    (89, "image62.jpeg", Q, "l11-s089-sinus-exit-block-plain.jpg", (0, 17, 496, 74)),
    (91, "image63.jpg", Q, "l11-s091-sinus-pause-strip.jpg", (0, 0, 1038, 117)),
    (99, "image70.jpg", Q, "l11-s099-sinus-arrest.jpg", None),
    # ---- guide figures (labels kept) ----
    (8, "image4.png", G, "l11-s008-atrial-conduction-system.png", None),
    (12, "image6.png", G, "l11-s012-left-bundle-fascicles.png", None),
    (17, "image8.png", G, "l11-s017-action-potential-phases.png", None),
    (27, "image13.png", G, "l11-s027-waves-segments-intervals.png", None),
    (30, "image16.png", G, "l11-s030-pr-interval-conduction.png", None),
    (37, "image22.png", G, "l11-s037-refractory-periods.png", None),
    (40, "image24.jpeg", G, "l11-s040-tp-segment.jpg", None),
    (48, "image31.png", G, "l11-s048-count-down-method.png", None),
    (62, "image45.png", G, "l11-s062-einthoven-triangle.png", None),
    (68, "image53.jpg", G, "l11-s068-precordial-lead-placement.jpg", None),
    (70, "image55.jpg", G, "l11-s070-contiguous-leads.jpg", None),
    (58, "image41.jpeg", G, "l11-s058-normal-sinus-rhythm.jpg", None),
    (76, "image56.png", G, "l11-s076-sinus-bradycardia.png", None),
    (79, "image57.jpeg", G, "l11-s079-sinus-tachycardia.jpg", None),
    (81, "image58.png", G, "l11-s081-sinus-arrhythmia-respiration.png", None),
    (85, "image60.jpg", G, "l11-s085-sinus-exit-block-diagram.jpg", None),
    (89, "image62.jpeg", G, "l11-s089-sinus-exit-block.jpg", None),
    (91, "image63.jpg", G, "l11-s091-sinus-pause-diagram.jpg", None),
    (95, "image66.jpg", G, "l11-s095-sinus-arrest-diagram.jpg", None),
    (99, "image70.jpg", G, "l11-s099-sinus-arrest.jpg", None),
    (45, "image28.jpeg", G, "l11-s045-six-second-strip.jpg", None),
    (83, "image59.png", G, "l11-s083-sinus-arrhythmia.png", None),
    (93, "image65.jpeg", G, "l11-s093-sinus-pause.jpg", None),
]

MIN_W = 900          # upscale narrow strips to at least this width, capped at 3x


def slide_media(z, n):
    rels = z.read("ppt/slides/_rels/slide%d.xml.rels" % n).decode("utf-8")
    return set(re.findall(r'Target="\.\./media/([^"]+)"', rels))


def save(img, path):
    if path.endswith(".png"):
        img.save(path, optimize=True)
    else:
        img.convert("RGB").save(path, quality=90, optimize=True)


def main():
    os.makedirs(QUIZ, exist_ok=True)
    os.makedirs(GUIDE, exist_ok=True)
    z = zipfile.ZipFile(DECK)
    for slide, media, dest, name, box in FIGS:
        assert media in slide_media(z, slide), "slide %d no longer carries %s" % (slide, media)
        im = Image.open(io.BytesIO(z.read("ppt/media/" + media)))
        im = im.convert("RGBA")
        flat = Image.new("RGBA", im.size, "white")       # transparent PNGs go dark in dark mode
        flat.alpha_composite(im)
        im = flat.convert("RGB")
        if box:
            im = im.crop(box)
        if im.width < MIN_W:
            k = min(3.0, MIN_W / im.width)
            im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        out = os.path.join(QUIZ if dest == Q else GUIDE, name)
        save(im, out)
        print("%-6s %-52s %4dx%-4d slide %d" % (dest, name, im.width, im.height, slide))


if __name__ == "__main__":
    main()
