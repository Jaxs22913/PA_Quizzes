#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the PDM I Lecture 12 (Ectopy, Escape Rhythms and Supraventricular Dysrhythmias,
Scott Mathis) figures.

Same contract as extract_pdm_l11_figures.py:
  pdm-exam-3-quiz-images/         strips above a stem; labels that NAME the rhythm or the
                                  finding are cropped away:
                                    slide 7  "Premature Atrial Contraction (PAC)" title
                                    slide 9  "Atrial Trigeminy" title
                                    slide 16 the "wandering atrial pacemaker - ECGpedia"
                                             watermark (bottom right) -- it is the answer
                                    slide 47 the "Inverted P wave" caption
                                    slide 48 the "Absent P wave" caption
  pdm-exam-3-study-guide-images/  guide figures, labels kept.

Keyed by the deck's MEDIA filename and asserted against the slide's own relationships.
Two deck files are not what their extension says: image2 is saved as ".crdownload"
(an interrupted browser download) but is a complete JPEG, and the .jfif files are
JPEGs; all are re-saved under honest extensions.

Every picture was viewed at full size first (2026-10-08). Left out of the quiz on purpose:
  slide 17 (MAT title and criteria printed on the strip), slide 52 ("Junctional Escape
  Beat" title), slide 53 ("Sinus beat failed to materialize" / "Junctional escape"
  captions), slides 50/51's inverted-P PJC strips (image38, image39: at deck resolution
  the inverted P waves cannot be made out), slide 72's R-on-T panel (labelled
  "Polymorphic ventricular tachycardia"). The labelled ones go to the guide instead.
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
    "12. Ectopy, Escape Rhythms and Supraventricular Dysrhythmias.pptx")

Q, G = "quiz", "guide"
FIGS = [
    # ---- quiz strips ----
    (7, "image4.jpeg", Q, "l12-s007-premature-atrial-complexes.jpg", (0, 14, 378, 133)),
    (7, "image5.jpeg", Q, "l12-s007-premature-atrial-complexes-arrowed.jpg", None),
    (8, "image6.jpeg", Q, "l12-s008-atrial-bigeminy.jpg", None),
    (9, "image7.jpeg", Q, "l12-s009-atrial-trigeminy.jpg", (0, 14, 378, 133)),
    (10, "image8.jpeg", Q, "l12-s010-ventricular-quadrigeminy.jpg", None),
    (13, "image11.jpeg", Q, "l12-s013-wandering-atrial-pacemaker.jpg", None),
    (16, "image14.png", Q, "l12-s016-wandering-atrial-pacemaker-b.png", (0, 0, 1500, 258)),
    (19, "image16.jpeg", Q, "l12-s019-multifocal-atrial-tachycardia.jpg", None),
    (21, "image17.jpeg", Q, "l12-s021-multifocal-atrial-tachycardia-b.jpg", None),
    (24, "image19.jpeg", Q, "l12-s024-atrial-flutter-five-to-one.jpg", None),
    (29, "image22.jpeg", Q, "l12-s029-atrial-flutter-three-to-one.jpg", None),
    (30, "image23.jpeg", Q, "l12-s030-atrial-flutter-variable-conduction.jpg", None),
    (34, "image25.jpeg", Q, "l12-s034-atrial-fibrillation.jpg", None),
    (36, "image26.jpeg", Q, "l12-s036-atrial-fibrillation-b.jpg", None),
    (38, "image28.gif", Q, "l12-s038-reentry-tachycardia-onset.png", None),
    (39, "image29.png", Q, "l12-s039-pseudo-s-waves.png", None),
    (41, "image30.jpeg", Q, "l12-s041-atrioventricular-nodal-reentrant-tachycardia.jpg", None),
    (43, "image31.jpeg", Q, "l12-s043-atrioventricular-nodal-reentrant-tachycardia-b.jpg", None),
    (47, "image34.jpeg", Q, "l12-s047-junctional-inverted-p-waves.jpg", (0, 0, 417, 86)),
    (48, "image35.jpeg", Q, "l12-s048-junctional-absent-p-waves.jpg", (0, 0, 417, 88)),
    (49, "image36.jpg", Q, "l12-s049-p-wave-after-qrs.jpg", None),
    (50, "image37.jpg", Q, "l12-s050-premature-junctional-complexes.jpg", None),
    (51, "image40.jfif", Q, "l12-s051-premature-junctional-complex-retrograde-p.jpg", None),
    (55, "image43.jfif", Q, "l12-s055-junctional-escape-rhythm.jpg", None),
    (57, "image44.jfif", Q, "l12-s057-junctional-escape-rhythm-b.jpg", None),
    (60, "image45.jfif", Q, "l12-s060-accelerated-junctional-rhythm.jpg", None),
    (62, "image46.jfif", Q, "l12-s062-accelerated-junctional-rhythm-b.jpg", None),
    (65, "image47.jfif", Q, "l12-s065-junctional-tachycardia.jpg", None),
    (67, "image48.jfif", Q, "l12-s067-junctional-tachycardia-b.jpg", None),
    (70, "image49.gif", Q, "l12-s070-premature-ventricular-complex.png", None),
    (71, "image50.jfif", Q, "l12-s071-multifocal-pvc-couplet.jpg", None),
    (71, "image51.jfif", Q, "l12-s071-unifocal-pvc-quadruplet-and-triplet.jpg", None),
    (71, "image52.jfif", Q, "l12-s071-run-of-ventricular-tachycardia.jpg", None),
    (73, "image57.jfif", Q, "l12-s073-trigeminal-pvcs.jpg", None),
    (74, "image58.jfif", Q, "l12-s074-ventricular-escape-complex.jpg", None),
    (77, "image60.jpg", Q, "l12-s077-idioventricular-rhythm.jpg", None),
    (79, "image61.png", Q, "l12-s079-idioventricular-rhythm-b.png", None),
    (82, "image62.png", Q, "l12-s082-accelerated-idioventricular-rhythm.png", None),
    (84, "image63.jfif", Q, "l12-s084-accelerated-idioventricular-rhythm-b.jpg", None),
    # ---- guide figures (labels kept) ----
    (6, "image2.crdownload", G, "l12-s006-premature-atrial-complex-diagram.jpg", None),
    (7, "image3.jpeg", G, "l12-s007-premature-atrial-complexes-labeled.jpg", None),
    (11, "image9.png", G, "l12-s011-wandering-atrial-pacemaker-diagram.png", None),
    (17, "image15.jpg", G, "l12-s017-multifocal-atrial-tachycardia.jpg", None),
    (23, "image18.png", G, "l12-s023-atrial-flutter-circuit.png", None),
    (24, "image19.jpeg", G, "l12-s024-atrial-flutter-sawtooth.jpg", None),
    (32, "image24.jpg", G, "l12-s032-atrial-fibrillation-diagram.jpg", None),
    (34, "image25.jpeg", G, "l12-s034-atrial-fibrillation.jpg", None),
    (38, "image27.png", G, "l12-s038-avnrt-circuit.png", None),
    (39, "image29.png", G, "l12-s039-pseudo-s-waves.png", None),
    (41, "image30.jpeg", G, "l12-s041-avnrt.jpg", None),
    (47, "image34.jpeg", G, "l12-s047-junctional-inverted-p-wave.jpg", None),
    (52, "image41.jpg", G, "l12-s052-junctional-escape-beat.jpg", None),
    (53, "image42.jfif", G, "l12-s053-junctional-escape-rhythm-onset.jpg", None),
    (55, "image43.jfif", G, "l12-s055-junctional-escape-rhythm.jpg", None),
    (60, "image45.jfif", G, "l12-s060-accelerated-junctional-rhythm.jpg", None),
    (67, "image48.jfif", G, "l12-s067-junctional-tachycardia.jpg", None),
    (70, "image49.gif", G, "l12-s070-premature-ventricular-complex.png", None),
    (71, "image50.jfif", G, "l12-s071-multifocal-pvc-couplet.jpg", None),
    (71, "image52.jfif", G, "l12-s071-run-of-ventricular-tachycardia.jpg", None),
    (72, "image55.png", G, "l12-s072-r-on-t.png", None),
    (74, "image58.jfif", G, "l12-s074-ventricular-escape-complex.jpg", None),
    (77, "image60.jpg", G, "l12-s077-idioventricular-rhythm.jpg", None),
    (82, "image62.png", G, "l12-s082-accelerated-idioventricular-rhythm.png", None),
    (8, "image6.jpeg", G, "l12-s008-atrial-bigeminy.jpg", None),
    (9, "image7.jpeg", G, "l12-s009-atrial-trigeminy.jpg", None),
    (10, "image8.jpeg", G, "l12-s010-ventricular-quadrigeminy.jpg", None),
    (13, "image11.jpeg", G, "l12-s013-wandering-atrial-pacemaker.jpg", None),
    (30, "image23.jpeg", G, "l12-s030-atrial-flutter-variable-conduction.jpg", None),
    (50, "image37.jpg", G, "l12-s050-premature-junctional-complexes.jpg", None),
    (57, "image44.jfif", G, "l12-s057-junctional-escape-rhythm-no-p.jpg", None),
    (73, "image57.jfif", G, "l12-s073-trigeminal-pvcs.jpg", None),
]

MIN_W = 900
# Slide 48's caption sits in red under the strip; after the crop a few red pixels of its top
# edge (and the small red marker it pointed from) survive, so red is painted out of this one.
DE_RED = {"l12-s048-junctional-absent-p-waves.jpg"}


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
        im.seek(0)
        im = im.convert("RGBA")
        flat = Image.new("RGBA", im.size, "white")
        flat.alpha_composite(im)
        im = flat.convert("RGB")
        if box:
            im = im.crop(box)
        if name in DE_RED:
            px = im.load()
            for y in range(im.height):
                for x in range(im.width):
                    r, g, b = px[x, y]
                    if r > 150 and g < 130 and b < 130:
                        px[x, y] = (255, 255, 255)
        if im.width < MIN_W:
            k = min(3.0, MIN_W / im.width)
            im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
        out = os.path.join(QUIZ if dest == Q else GUIDE, name)
        save(im, out)
        print("%-6s %-60s %4dx%-4d slide %d" % (dest, name, im.width, im.height, slide))


if __name__ == "__main__":
    main()
