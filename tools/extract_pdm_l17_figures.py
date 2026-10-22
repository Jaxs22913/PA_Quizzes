#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 17 (Pulmonary Imaging) figures for PDM I Exam 4: the films and scans the
quizzes ask the student to read, and the teaching figures for the guide.

Deck: "17. Pulmonary Imaging - Prof. Fowler (GUEST).pptx" (Professor Fowler, guest lecturer,
title slide; 20 October 2026). All 88 slides were rendered and every picture in the deck was
viewed before it was chosen here. Slide images are cleared for use provided the slide is cited.

QUIZ images carry NO label that names the answer. What was done to each:
  slide 17  lateral soft-tissue neck: GUIDE ONLY. The slide's letter boxes (A to I, in the order the
            slide lists them) are redrawn where they sit on the slide; a box beside a structure is not
            precise enough to build a "what is marked" question on, so the quizzes ask in words.
  slide 22  the plain posteroanterior film: one arrow each, drawn by us, to the aortic knob, the
            right costophrenic angle and the gastric bubble (positions checked at 2x zoom).
  slides 29/30  the exposure trio: single films cropped away from their "mAs" captions.
  slide 32  the poor-inspiration film keeps the slide's own rib count (1 and 6).
  slide 48  the coronal and sagittal reconstructions cropped apart, scanner text and the scout
            inset cropped off so the plane is read from the anatomy. The transverse example is
            slide 50's lung-window slice (first frame of the animation; only "A" and "P" on it).
  slide 51  panel A only (the slide crops panel B away); one arrow at the rib the slide's
            "Bone: High Attenuation" connector ends on.
  slide 54  the lower row (fused axial slice and whole-body projection), cropped above the
            "MPR FUSION" and uptake-scale captions.
  slide 61  panels A and B (ventilation and perfusion) side by side; panel C (contrast scan with
            the arrowed clot) alone. The view names printed on the scans stay.
  slide 74  one arrow at the descending aorta (the slide's "DAo" box sits on it).
  slide 78  the bacterial pneumonia film cut away from its caption.
  slide 80  the "Effusions" film cut away from the title and caption.
  slide 82  the pulmonary edema film with every word masked; the coloured arrows stay.
  slide 84  the pneumothorax film with its legend masked; the yellow and red outlines stay.
  slide 85  the pneumothorax scan with "Air compressing lung" and "Compressed lung" masked.
  slides 79, 81, 83, 86, 87  unlabeled as they stand (79: panel a only).

Left out: slide 1 (icon), slides 10, 21, 45, 64 (stock photographs and an unlabeled M-mode
strip), slide 76 (pulmonary vein variants: anatomy the lecture said is left to the radiologist).
"""
import io, os, zipfile
from PIL import Image, ImageDraw, ImageFilter, ImageFont
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Principles of Diagnostic Medicine I Inbox/Exam 4/"
    "17. Pulmonary Imaging - Prof. Fowler (GUEST).pptx")
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
QUIZ = os.path.join(FOLDER, "pdm-exam-4-quiz-images")
GUIDE = os.path.join(FOLDER, "pdm-exam-4-study-guide-images")
MAXW = 1200
FONT = "/System/Library/Fonts/Helvetica.ttc"

# The slide-17 letters, converted from the slide's text-box centres into the picture's own pixels
# (the picture is cropped 2.4% top and 12.2% bottom on the slide, which the conversion undoes).
NECK = {"A": (564, 132), "B": (547, 221), "C": (514, 551), "D": (618, 412), "E": (590, 340),
        "F": (673, 394), "G": (592, 496), "H": (297, 576), "I": (524, 683)}
NECK_NAMES = {"A": "Nasopharyngeal space", "B": "Retropharyngeal space", "C": "Retrotracheal space",
              "D": "Epiglottis", "E": "Vallecula", "F": "Hyoid bone", "G": "Vocal cords",
              "H": "C7", "I": "Trachea"}
BLACK, WHITE, GRAY = (0, 0, 0), (255, 255, 255), (60, 60, 60)

# (slide, picture shape id, output stem, destinations, ops)
# ops: crop=(x0,y0,x1,y1) in the picture's own pixels, applied LAST; masks=[(box, colour)];
# arrows=[(tail, head)]; letters=[(x, y, text)]; tags=[(x, y, text)] (small captions on dark).
FIGS = [
 # ---- anatomy and the upper airway
 (9, 232, "l17-lobes-anterior", "G", {}),
 (9, 233, "l17-lobes-posterior", "G", {}),
 (15, 274, "l17-waters-view", "G", {}),
 (16, 281, "l17-lateral-face", "G", {}),
 (17, 287, "l17-neck-lateral-lettered", "G", {"letters": list((x, y, k) for k, (x, y) in NECK.items()),
                                              "crop": (0, 25, 843, 899)}),
 (20, 317, "l17-laryngoscopy", "G", {}),
 # ---- the chest radiograph
 (22, 332, "l17-cxr-normal", "G", {}),
 (22, 332, "l17-cxr-arrow-aortic-knob", "Q", {"arrows": [((790, 140), (630, 258))]}),
 (22, 332, "l17-cxr-arrow-costophrenic", "Q", {"arrows": [((250, 700), (92, 930))]}),
 (22, 332, "l17-cxr-arrow-gastric-bubble", "Q", {"arrows": [((930, 700), (790, 885))]}),
 (25, 354, "l17-pa-vs-ap", "G", {}),
 (27, 368, "l17-radiographic-anatomy", "G", {}),
 (29, 381, "l17-exposure-trio", "G", {}),
 (29, 381, "l17-film-underexposed", "Q", {"crop": (27, 33, 251, 278)}),
 (29, 381, "l17-film-overexposed", "Q", {"crop": (509, 39, 728, 278)}),
 (32, 401, "l17-inspiration-poor", "QG", {}),
 (32, 402, "l17-inspiration-good", "G", {}),
 (33, 410, "l17-rotation", "G", {}),
 (35, 420, "l17-scan-path-pa", "G", {}),
 (36, 425, "l17-scan-path-lateral", "G", {}),
 (38, 436, "l17-one-third-two-thirds", "G", {"crop": (0, 0, 629, 506),
                                           "tags": [(252, 432, "1/3"), (418, 441, "2/3")]}),
 (38, 437, "l17-cxr-rib-anatomy", "G", {"crop": (0, 518, 629, 1024)}),
 (39, 446, "l17-lateral-cxr", "G", {}),
 (40, 457, "l17-cxr-annotated", "G", {}),
 (41, 462, "l17-cxr-labeled", "G", {}),
 (42, 471, "l17-hila", "G", {}),
 # ---- ultrasound
 (46, 501, "l17-lung-ultrasound", "G", {"crop": (150, 40, 786, 506)}),
 (47, 508, "l17-lung-ultrasound-labeled", "G", {}),
 # ---- computed tomography, nuclear medicine, magnetic resonance
 (48, 515, "l17-ct-planes", "G", {}),
 (48, 515, "l17-ct-coronal", "Q", {"crop": (0, 0, 262, 204)}),
 (48, 515, "l17-ct-sagittal", "Q", {"crop": (0, 250, 276, 438)}),
 (50, 528, "l17-ct-axial", "Q", {}),
 (50, 528, "l17-ct-lung-window", "G", {}),
 (51, 533, "l17-ct-attenuation", "G", {"crop": (0, 48, 860, 797), "arrows": [
     ((300, 180), (101, 246)), ((790, 230), (712, 347)), ((520, 560), (589, 385)), ((330, 700), (240, 627))],
     "tags": [(300, 168, "Bone: high"), (760, 212, "Gas: low"), (500, 578, "Heart: normal"),
              (330, 718, "Coagulated blood: normal to low")]}),
 (51, 533, "l17-ct-arrow-rib", "Q", {"crop": (0, 48, 860, 797), "arrows": [((300, 180), (104, 244))]}),
 (54, 563, "l17-pet-ct-full", "G", {}),
 (54, 563, "l17-pet-ct", "Q", {"crop": (212, 990, 1827, 1866)}),
 (57, 583, "l17-sagittal-cta-mri", "G", {}),
 (58, 591, "l17-ct-anatomy-key", "G", {}),
 (59, 596, "l17-ct-apices", "G", {}),
 (61, 608, "l17-vq-ventilation-perfusion", "QG", {"stack": [(0, 0, 492, 351), (113, 363, 492, 739)]}),
 (61, 608, "l17-cta-clot", "QG", {"crop": (0, 752, 492, 1090)}),
 (63, 626, "l17-vq-normal", "G", {}),
 (67, 650, "l17-mri-lung-mass", "G", {}),
 (68, 659, "l17-mri-axial-anatomy", "G", {}),
 (71, 674, "l17-pulmonary-vessels", "G", {}),
 (74, 691, "l17-cta-labeled", "G", {"letters_small": [(420, 400, "DAo"), (348, 216, "AsAo")]}),
 (74, 691, "l17-cta-arrow-descending-aorta", "Q", {"arrows": [((560, 470), (440, 410))]}),
 (75, 703, "l17-pulmonary-veins", "G", {}),
 # ---- the five patterns
 (78, 723, "l17-pneumonia-cxr-panel", "G", {}),
 (78, 723, "l17-pneumonia-cxr", "Q", {"crop": (703, 40, 1246, 516)}),
 (79, 729, "l17-pneumonia-ct", "QG", {"crop": (0, 0, 405, 290)}),
 (79, 729, "l17-pneumonia-ct-panel", "G", {}),
 (80, 740, "l17-effusion-cxr-pair", "G", {}),
 (80, 740, "l17-effusion-cxr", "Q", {"crop": (326, 133, 573, 371)}),
 (81, 747, "l17-effusion-ct", "QG", {}),
 (82, 754, "l17-edema-cxr", "G", {}),
 (82, 754, "l17-edema-cxr-unlabeled", "Q", {"masks": [
     ((28, 195, 145, 265), "blur"), ((198, 215, 390, 280), "blur"), ((222, 290, 412, 320), "blur"),
     ((108, 436, 530, 470), "blur")]}),
 (83, 762, "l17-edema-ct", "QG", {}),
 (84, 769, "l17-pneumothorax-cxr", "G", {}),
 (84, 769, "l17-pneumothorax-cxr-outlined", "Q", {"masks": [((55, 28, 410, 118), "sample")]}),
 (85, 776, "l17-pneumothorax-ct", "G", {}),
 (85, 776, "l17-pneumothorax-ct-unlabeled", "Q", {"masks": [((620, 70, 835, 102), "blur"),
                                                            ((808, 380, 972, 462), "blur")]}),
 (86, 784, "l17-ild-cxr", "QG", {}),
 (87, 790, "l17-ild-ct", "QG", {}),
]


def blobs():
    """{(slide, shape id): bytes}, read straight from the package so nothing is retyped."""
    out = {}
    prs = Presentation(DECK)
    z = zipfile.ZipFile(DECK)
    for i, s in enumerate(prs.slides, 1):
        rels = {r.rId: r.target_ref for r in s.part.rels.values()}
        for sh in s.shapes:
            emb = sh._element.xpath('.//a:blip/@r:embed')
            if not emb:
                continue
            tgt = rels.get(emb[0])
            if tgt and "media/" in tgt:
                out[(i, sh.shape_id)] = z.read("ppt/media/" + tgt.split("media/")[-1])
    return out


def font(px):
    return ImageFont.truetype(FONT, max(12, int(px)))


def arrow(d, tail, head, w):
    """A yellow arrow with a dark outline, head at `head`."""
    import math
    (x0, y0), (x1, y1) = tail, head
    ang = math.atan2(y1 - y0, x1 - x0)
    hl = w * 4.2
    bx, by = x1 - hl * math.cos(ang), y1 - hl * math.sin(ang)
    left = (bx + hl * 0.55 * math.sin(ang), by - hl * 0.55 * math.cos(ang))
    right = (bx - hl * 0.55 * math.sin(ang), by + hl * 0.55 * math.cos(ang))
    for col, extra in ((BLACK, 3), ((255, 214, 0), 0)):
        d.line((x0, y0, bx, by), fill=col, width=w + extra)
        d.polygon([(x1, y1), left, right], fill=col, outline=col)


def apply(im, ops):
    d = ImageDraw.Draw(im)
    for box, col in ops.get("masks", []):
        if col == "blur":                       # coloured or black lettering on a grey film: find the
            reg = im.crop(box)                  # lettering, widen it 3 px (anti-aliased edges), fill it
            px = reg.load()                     # with the film's own grey, then soften the patch
            def ink(c):
                return max(c) - min(c) >= 24 or sum(c) / 3 <= 80 or sum(c) / 3 >= 232
            m = Image.new("L", reg.size, 0)
            mp = m.load()
            keep = []
            for x in range(reg.width):
                for y in range(reg.height):
                    if ink(px[x, y]):
                        mp[x, y] = 255
                    else:
                        keep.append(px[x, y])
            m = m.filter(ImageFilter.MaxFilter(7))
            keep.sort(key=sum)
            fill = Image.new("RGB", reg.size, keep[len(keep) // 2] if keep else (128, 128, 128))
            reg.paste(fill, (0, 0), m)
            im.paste(reg.filter(ImageFilter.GaussianBlur(4)), box[:2])
            continue
        if col == "sample":                     # paint with the background just outside the box
            col = im.getpixel((max(0, box[0] - 4), max(0, box[1] - 4)))
        elif col is None:                       # median of the box's own border: blends into film
            px = [im.getpixel((x, box[1])) for x in range(box[0], box[2], 3)]
            px.sort(key=sum)
            col = px[len(px) // 2]
        d.rectangle(box, fill=col)
    w = max(3, round(im.width / 220))
    for tail, head in ops.get("arrows", []):
        arrow(d, tail, head, w)
    for x, y, t in ops.get("letters", []):
        f = font(im.width / 30)
        bw, bh = d.textlength(t, font=f) + 14, f.size + 12
        d.rectangle((x - bw / 2, y - bh / 2, x + bw / 2, y + bh / 2), outline=(255, 70, 70), width=3)
        d.text((x - bw / 2 + 7, y - bh / 2 + 4), t, fill=(255, 90, 90), font=f)
    for x, y, t in ops.get("letters_small", []):
        f = font(im.width / 45)
        d.text((x, y), t, fill=(255, 214, 0), font=f, anchor="mm", stroke_width=2, stroke_fill=BLACK)
    for x, y, t in ops.get("tags", []):
        f = font(im.width / 34)
        d.text((x, y), t, fill=(255, 214, 0), font=f, anchor="mm", stroke_width=3, stroke_fill=BLACK)
    if "stack" in ops:                          # panels side by side, top-aligned on white
        parts = [im.crop(b) for b in ops["stack"]]
        out = Image.new("RGB", (sum(p.width for p in parts) + 12 * (len(parts) - 1),
                                max(p.height for p in parts)), WHITE)
        x = 0
        for p in parts:
            out.paste(p, (x, 0)); x += p.width + 12
        return out
    if "crop" in ops:
        im = im.crop(ops["crop"])
    return im


def main():
    os.makedirs(QUIZ, exist_ok=True)
    os.makedirs(GUIDE, exist_ok=True)
    B = blobs()
    for slide, sid, stem, dest, ops in FIGS:
        assert (slide, sid) in B, "slide %d has no picture %d" % (slide, sid)
        im = Image.open(io.BytesIO(B[(slide, sid)]))
        if getattr(im, "is_animated", False):
            im.seek(0)                          # the first frame of an animation
        if im.mode in ("P", "RGBA", "LA"):
            im = im.convert("RGBA")
            bg = Image.new("RGB", im.size, WHITE)
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        im = apply(im, ops)
        if im.width < 600:                      # small scans read badly at natural size
            f = min(3, -(-700 // im.width))
            im = im.resize((im.width * f, im.height * f), Image.LANCZOS)
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        for dd in ([QUIZ] if "Q" in dest else []) + ([GUIDE] if "G" in dest else []):
            p = os.path.join(dd, stem + ".jpg")
            im.save(p, quality=88)
            print("%-5s slide %2d  %-44s %4dx%-4d %3d KB" % ("quiz" if dd == QUIZ else "guide", slide,
                  os.path.basename(p), im.width, im.height, os.path.getsize(p) // 1024))


if __name__ == "__main__":
    main()
