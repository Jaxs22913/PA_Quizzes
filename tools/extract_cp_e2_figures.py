#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Extract the Clinical Pathophysiology I Exam 2 guide figures from the decks.

Lecture 6 (Cardiac), Lecture 7 (Vascular), Lecture 8 (Immunity) and Lecture 9
(Pulmonary). Every figure is read straight out
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

Lecture 8 is read from the slides-only copy of the 3 GB narrated deck (the inbox
file "Immunity_Lecture_Recorded.pptx" with its narration videos zeroed; same media,
same slides), falling back to the inbox file. Lecture 9's deck was rebuilt from the
lecture video and its slide PART files are not numbered in show order (the seven
added slides are slide105-111.xml), so every slide number is resolved through
presentation.xml -- the number cited is always the slide's position in the show.

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
L8 = os.path.expanduser("~/.cache/pa-quizzes/decks/cp-l8-immunity-slides-only.pptx")
if not os.path.exists(L8):
    L8 = os.path.join(INBOX, "Immunity_Lecture_Recorded.pptx")
L9 = os.path.join(INBOX, "9. Pulmonary Pathophysiology - Ward 2026 (rebuilt from recording).pptx")

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
    (L8, 7, "image8.jpg", "cp-exam-2-l8-images/lymphatic-capillary.jpg", None),
    (L8, 14, "image17.jpeg", "cp-exam-2-l8-images/blood-cell-formation.jpg", None),
    (L8, 17, "image22.jpeg", "cp-exam-2-l8-images/granulocytes-agranulocytes.jpg", None),
    (L8, 23, "image32.png", "cp-exam-2-l8-images/clonal-selection.jpg", None),
    (L8, 26, "image36.jpeg", "cp-exam-2-l8-images/phagocytosis.jpg", None),
    (L8, 37, "image51.png", "cp-exam-2-l8-images/primary-secondary-response.jpg", None),
    (L8, 42, "image59.png", "cp-exam-2-l8-images/antibody-structure.jpg", None),
    (L8, 45, "image64.png", "cp-exam-2-l8-images/antibody-classes.jpg", None),
    (L8, 59, "image89.jpg", "cp-exam-2-l8-images/antibody-functions.jpg", None),
    (L8, 71, "image102.png", "cp-exam-2-l8-images/complement-pathways.png", None),
    (L8, 75, "image110.gif", "cp-exam-2-l8-images/complement-overview.png", 0),
    (L9, 4, "image2.jpeg", "cp-exam-2-l9-images/respiratory-membrane.jpg", None),
    (L9, 12, "image7.jpg", "cp-exam-2-l9-images/ards-alveolus.jpg", None),
    (L9, 16, "image9.png", "cp-exam-2-l9-images/pulmonary-hypertension.jpg", None),
    (L9, 19, "image13.jpeg", "cp-exam-2-l9-images/capillary-forces.jpg", None),
    (L9, 41, "image19.jpeg", "cp-exam-2-l9-images/asthma-airway.jpg", None),
    (L9, 56, "image21.jpeg", "cp-exam-2-l9-images/emphysema.jpg", None),
    (L9, 58, "image22.jpeg", "cp-exam-2-l9-images/emphysema-types.jpg", None),
    (L9, 63, "image23.jpeg", "cp-exam-2-l9-images/bronchiectasis-types.jpg", None),
    (L9, 91, "image25.jpeg", "cp-exam-2-l9-images/pneumothorax.jpg", None),
    (L9, 97, "image26.jpeg", "cp-exam-2-l9-images/pleural-fluids.jpg", None),
]
MAXW = 1100


def slide_part(z, slide):
    """The part file of the slide at position `slide` in the SHOW (presentation.xml order)."""
    pres = z.read("ppt/presentation.xml").decode()
    rels = z.read("ppt/_rels/presentation.xml.rels").decode()
    target = {}
    for tag in re.findall(r"<Relationship [^>]*>", rels):
        i = re.search(r'Id="([^"]+)"', tag); t = re.search(r'Target="([^"]+)"', tag)
        if i and t:
            target[i.group(1)] = t.group(1)
    order = re.findall(r'<p:sldId [^>]*r:id="([^"]+)"', pres)
    return os.path.basename(target[order[slide - 1]])


def slide_media(z, slide):
    rel = z.read("ppt/slides/_rels/%s.rels" % slide_part(z, slide)).decode()
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
