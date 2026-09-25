#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract the Clinical Pathophysiology I Exam 2 guide figures from the decks.

Lecture 6 (Cardiac) and Lecture 7 (Vascular). Every figure is read straight out
of the .pptx by slide number, so the slide citation in the guide can never
drift from the picture. Slide images are cleared for use when cited
(media_asset_licensing); third-party marks baked into the pixels are left in.

Every figure below was viewed at full size before it was chosen
(image_only_slides). Two carry content that exists in NO text form in the deck:
  Lecture 6 slide 24 -- the six features of the vulnerable plaque
  Lecture 6 slide 25 -- an animated GIF comparing stable against vulnerable;
                        frame 180 is the one with every label present
Lecture 7 slide 15 is also image-only (a textbook "Key Concepts" box); it is
transcribed into the guide as text rather than shipped as a picture of text.

Idempotent: rewrites the two image folders from the decks each run.
"""
import io, os, re, zipfile
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUTDIR = os.path.join(ROOT, "Clinical Pathophysiology I Exam 2")
INBOX = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Pathophysiology I Inbox/Exam 2")
L6 = os.path.join(INBOX, "6. Cardiac Pathophysiology  for posting.pptx")
L7 = os.path.join(INBOX, "SV Vascular Pathophys I Fall 2026.pptx")

# (deck, slide, media name inside ppt/media, output name, gif frame or None)
FIGS = [
    (L6, 6, "image2.jpeg", "cp-exam-2-l6-images/coronary-arteries.jpg", None),
    (L6, 7, "image3.jpeg", "cp-exam-2-l6-images/coronary-schematic.jpg", None),
    (L6, 18, "image6.jpeg", "cp-exam-2-l6-images/plaque-formation-steps.jpg", None),
    (L6, 19, "image7.jpeg", "cp-exam-2-l6-images/atherosclerosis-initiation.jpg", None),
    (L6, 24, "image12.jpeg", "cp-exam-2-l6-images/vulnerable-plaque-features.jpg", None),
    (L6, 25, "image13.gif", "cp-exam-2-l6-images/stable-vs-vulnerable.png", 180),
    (L6, 32, "image14.jpeg", "cp-exam-2-l6-images/cardiac-ischemia.jpg", None),
    (L6, 47, "image15.jpeg", "cp-exam-2-l6-images/mitral-stenosis.jpg", None),
    (L6, 52, "image16.jpeg", "cp-exam-2-l6-images/aortic-stenosis.jpg", None),
    (L7, 9, "image8.png", "cp-exam-2-l7-images/vessel-structure.jpg", None),
    (L7, 11, "image10.jpeg", "cp-exam-2-l7-images/capillary-types.jpg", None),
    (L7, 14, "image11.png", "cp-exam-2-l7-images/neointimal-response.jpg", None),
    (L7, 21, "image15.jpeg", "cp-exam-2-l7-images/blood-pressure-regulation.jpg", None),
    (L7, 23, "image16.jpeg", "cp-exam-2-l7-images/hyaline-hyperplastic.jpg", None),
    (L7, 26, "image17.png", "cp-exam-2-l7-images/atheroma.jpg", None),
    (L7, 27, "image18.png", "cp-exam-2-l7-images/aneurysm-types.jpg", None),
    (L7, 31, "image20.png", "cp-exam-2-l7-images/fibromuscular-dysplasia.jpg", None),
    (L7, 33, "image21.jpeg", "cp-exam-2-l7-images/raynaud.jpg", None),
    (L7, 36, "image24.jpeg", "cp-exam-2-l7-images/varicose-veins.jpg", None),
    (L7, 38, "image28.jpeg", "cp-exam-2-l7-images/deep-vein-thrombosis.jpg", None),
]
MAXW = 1100


def slide_media(z, slide):
    rel = z.read("ppt/slides/_rels/slide%d.xml.rels" % slide).decode()
    return set(re.findall(r'Target="\.\./media/([^"]+)"', rel))


def main():
    sizes = {}
    zips = {}
    for deck, slide, media, out, frame in FIGS:
        z = zips.setdefault(deck, zipfile.ZipFile(deck))
        # Guard: the media file must really belong to that slide, or the
        # citation would be wrong.
        assert media in slide_media(z, slide), "%s is not on slide %d of %s" % (media, slide, deck)
        im = Image.open(io.BytesIO(z.read("ppt/media/" + media)))
        if frame is not None:
            im.seek(frame)
        im = im.convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        path = os.path.join(OUTDIR, out)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        if out.endswith(".png"):
            im.save(path, optimize=True)
        else:
            im.save(path, quality=85, optimize=True)
        sizes[out] = im.size
        print("%-58s %4dx%-4d slide %d" % (out, im.width, im.height, slide))
    return sizes


if __name__ == "__main__":
    main()
