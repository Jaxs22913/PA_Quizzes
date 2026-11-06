#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 44 (Pleural Disorders, Gray) figures for the CMS I Exam 7 study guide.

    python3 tools/extract_cms_e7_l44_figures.py

Deck: "Pleural Disorders 2026.pptx" (120 slides). Every slide was viewed at 1920 px before anything was chosen.
Slide images are cleared for use provided the slide is cited (each figure cites it). Every file is built from the
original embedded blobs (no slide-render crops), with watermarks, source lines and the arrows already in the
pictures kept. Where the slide itself crops a picture (slides 68, 91, 109) the same crop is applied, so the file
shows what the slide shows. Small blobs are enlarged with Lanczos so labels read. Two or three pictures that share
one caption are set side by side at a common height on white, in slide order left to right.

Taken (guide subsection 6.N):
  slide 3   parietal and visceral pleura drawing: 6.1           slide 4   pleural cavity drawing: 6.1
  slide 6   breathing mechanics with the pressures: 6.1        slide 7   intrapleural pressure drawing: 6.1
  slide 15  normal versus collapsed lung drawing (the title art beside it left out): 6.3
  slide 18  pulmonary blebs drawing, thoracoscopic view of a large apical bulla, bullous emphysema specimen: 6.3
  slide 26  chest X-ray, pneumothorax (visceral pleural line): 6.4
  slide 27  chest X-ray and the magnified apex with the apical subpleural blebs: 6.4
  slide 28  apex-to-cupola diagram (a, b) and the chest X-ray with A and B: 6.4
  slide 29  supine portable chest X-ray, deep sulcus sign: 6.4
  slide 30  lung ultrasound (rib, intercostal space, pleura line, comet tail): 6.4
  slide 33  thoracic CT of a pneumothorax: 6.4
  slide 34  the generated testing-and-severity picture (dense graphic, read in 6.4's table): 6.4
  slide 38  catheter aspiration set-up (needle-catheter, tubing, large syringe): 6.5
  slide 40  Heimlich valve diagram; the chest tube / valve / drainage bag drawing: 6.5
  slides 43-44  drainage collection systems (reference only; he passed over them): 6.5
  slide 46  thoracoscopic views under the mechanical and the chemical pleurodesis columns: 6.5
  slide 48  video-assisted thoracoscopic surgery drawing (stapler, videothoracoscope, monitor): 6.5
  slide 58  the generated treatment-continuum picture (its matrix is transcribed in 6.6): 6.6
  slide 60  the generated recovery-guide picture (read in 6.6's education table): 6.6
  slide 62  closed and open pneumothorax drawings: 6.7      slide 63  tension pneumothorax, inspiration/expiration: 6.7
  slide 65  chest X-ray, tension pneumothorax: 6.7
  slide 67  needle decompression site diagram and the over-the-needle catheter drawing: 6.7
  slide 68  needle (A) and chest tube (B) site drawing: 6.7
  slide 70  hemothorax drawing: 6.8        slide 71  hemopneumothorax drawing (straight line, no meniscus): 6.8
  slide 72  chest X-ray, hemopneumothorax: 6.8   slide 73  tube placed to drain air versus fluid: 6.8
  slide 74  the generated hemothorax picture (read in 6.8): 6.8
  slide 78  the two unlabeled neck CT pictures (coronal, axial) in the pneumomediastinum section: 6.9
  slide 83  the generated effusion etiology picture (read in 6.10): 6.10
  slide 87  tactile fremitus drawing: 6.10   slide 88  back diagram, dull / diminished / bronchial: 6.10
  slide 89  infiltrate versus effusion (sponges in beakers): 6.10
  slide 90  lateral and frontal chest X-rays, blunted costophrenic angles: 6.11
  slide 91  lateral decubitus film: 6.11
  slide 92  free-flowing versus loculated fluid films: 6.11  slide 93  chest X-ray and contrast CT, bilateral effusions: 6.11
  slide 94  CT, loculated left effusion: 6.11   slide 95  ultrasound, anechoic effusion and septations: 6.11
  slide 97  the generated effusion work-up picture (its lab table and management column transcribed in 6.11, 6.13)
  slide 98  pleural fluid color guide (the same picture repeats on slide 99): 6.11
  slide 112 the Light's criteria chart (transcribed beside it): 6.11
  slide 104 thoracic duct and cisterna chyli drawing: 6.12  slide 105 milky fluid in a bottle: 6.12
  slide 107 parapneumonic effusion drawing: 6.12  slide 109 fibrin membranes, ultrasound (A) and thoracoscopy (B): 6.12
  slide 114 indwelling tunneled pleural catheter drawing: 6.13
  slide 119 the generated pleurodynia picture (read in 6.14): 6.14

Left out:
  slide 1 title art; slide 15's metal-font title; slide 100 "Transudate vs Exudate" title art; slide 115 title
  drawing (decoration). Slides 9, 19, 52 stock photographs of people in pain; slide 85 cartoon (dyspnea); slides 61
  and 77 cartoons (crying lung; the cereal-box characters beside the Hamman crunch); slide 36 "GOAL" clip art.
  Slides 41, 55 chest tube product photo and slide 66 needle-device product photo (packaging, no teaching).
  Slide 42 video still with a timestamp; slides 31-32 embedded videos (no picture in the file). Slide 40's
  patient photograph (the two diagrams carry the teaching). Slide 87's photo of hands on a back (technique only).
  Slide 78's picture behind the two CTs (mostly covered on the slide). Slide 91's patient-position drawing (the
  text says it: lying on the side, effusion side down). Slide 99 (duplicate of slide 98's picture).
  Slides 101, 110 lightbulb icons. Every other slide is text.
"""
import io, os, sys
from PIL import Image
from pptx import Presentation

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser(
    "~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 7/"
    "Pleural Disorders 2026.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 7", "cms-e7-images")
MAXW = 1400

# (output file, [(slide, picture shape id), ...], scale[, JPEG quality, default 85; 80 for the seven generated
# 2752 px infographics so each stays near 250 KB])
FIGS = [
    ("l44-s003-pleura-layers.png", [(3, 16388)], 2.0),
    ("l44-s004-pleural-cavity.jpg", [(4, 16390)], 1.0),
    ("l44-s006-breathing-pressures.jpg", [(6, 24580)], 1.0),
    ("l44-s007-intrapleural-pressure.png", [(7, 4)], 1.0),
    ("l44-s015-collapsed-lung.jpg", [(15, 9)], 1.0),
    ("l44-s018-blebs-drawing.jpg", [(18, 3)], 1.0),
    ("l44-s018-bulla-thoracoscopy.jpg", [(18, 12)], 1.25),
    ("l44-s018-bullous-emphysema.jpg", [(18, 11)], 1.0),
    ("l44-s026-cxr-visceral-pleural-line.jpg", [(26, 2)], 0.6),
    ("l44-s027-cxr-apical-blebs.jpg", [(27, 35843), (27, 35844)], 1.0),
    ("l44-s028-size-apex-cupola.jpg", [(28, 8), (28, 6)], 1.0),
    ("l44-s029-cxr-deep-sulcus.jpg", [(29, 1026)], 1.0),
    ("l44-s030-us-lung-pleura-line.jpg", [(30, 6)], 1.0),
    ("l44-s033-ct-pneumothorax.jpg", [(33, 2)], 0.4),
    ("l44-s034-testing-severity.jpg", [(34, 4)], 1.0, 80),
    ("l44-s038-catheter-aspiration.jpg", [(38, 4)], 0.5),
    ("l44-s040-heimlich-valve.png", [(40, 8)], 1.5),
    ("l44-s040-heimlich-drawing.jpg", [(40, 7)], 1.0),
    ("l44-s043-drainage-system.jpg", [(43, 83972)], 1.0),
    ("l44-s044-bottle-systems.jpg", [(44, 64515)], 1.0),
    ("l44-s046-pleurodesis-mechanical.jpg", [(46, 69636)], 1.5),
    ("l44-s046-pleurodesis-chemical.jpg", [(46, 69637)], 1.5),
    ("l44-s048-vats-drawing.jpg", [(48, 3)], 1.0),
    ("l44-s058-treatment-continuum.jpg", [(58, 4)], 1.0, 80),
    ("l44-s060-recovery-guide.jpg", [(60, 6)], 1.0, 80),
    ("l44-s062-closed-open.jpg", [(62, 10), (62, 9)], 1.0),
    ("l44-s063-tension-one-way-valve.jpg", [(63, 3)], 1.0),
    ("l44-s065-cxr-tension.jpg", [(65, 108547)], 2.0),
    ("l44-s067-needle-site.png", [(67, 74756)], 1.25),
    ("l44-s067-over-needle-catheter.png", [(67, 88071)], 1.25),
    ("l44-s068-needle-vs-tube-sites.jpg", [(68, 111620)], 1.0),
    ("l44-s070-hemothorax-drawing.jpg", [(70, 120835)], 1.0),
    ("l44-s071-hemopneumothorax-drawing.jpg", [(71, 99330)], 1.0),
    ("l44-s072-cxr-hemopneumothorax.jpg", [(72, 101379)], 0.6),
    ("l44-s073-tube-air-vs-fluid.jpg", [(73, 10)], 1.0),
    ("l44-s074-hemothorax-guide.jpg", [(74, 6)], 1.0, 80),
    ("l44-s078-ct-neck-air.jpg", [(78, 3), (78, 5)], 0.75),
    ("l44-s083-effusion-etiology.jpg", [(83, 4)], 1.0, 80),
    ("l44-s087-fremitus-drawing.png", [(87, 131076)], 1.0),
    ("l44-s088-effusion-exam-map.jpg", [(88, 84996)], 1.0),
    ("l44-s089-infiltrate-vs-effusion.jpg", [(89, 6)], 0.7),
    ("l44-s090-cxr-lateral-frontal.jpg", [(90, 6), (90, 134146)], 1.0),
    ("l44-s091-cxr-decubitus.jpg", [(91, 5)], 1.5),
    ("l44-s092-cxr-free-vs-loculated.jpg", [(92, 4)], 0.8),
    ("l44-s093-cxr-ct-bilateral.jpg", [(93, 5)], 1.75),
    ("l44-s094-ct-loculated.jpg", [(94, 2)], 1.0),
    ("l44-s095-us-septations.jpg", [(95, 2)], 0.8),
    ("l44-s097-effusion-workup.jpg", [(97, 6)], 1.0, 80),
    ("l44-s098-fluid-color-guide.jpg", [(98, 4)], 1.25),
    ("l44-s104-thoracic-duct.jpg", [(104, 2)], 0.3),
    ("l44-s105-chyle-milky.jpg", [(105, 3)], 1.0),
    ("l44-s107-parapneumonic.jpg", [(107, 3)], 1.0),
    ("l44-s109-fibrin-membranes.jpg", [(109, 3)], 0.8),
    ("l44-s112-lights-chart.jpg", [(112, 1026)], 1.0),
    ("l44-s114-indwelling-catheter.jpg", [(114, 5)], 1.0),
    ("l44-s119-pleurodynia-guide.jpg", [(119, 4)], 1.0, 80),
]
GAP = 24


def pictures(prs):
    """{(slide number, shape id): (image bytes, slide crop l/t/r/b)}, recursing into groups."""
    out = {}

    def walk(n, shapes):
        for sh in shapes:
            if sh.shape_type == 6:
                walk(n, sh.shapes)
            elif sh._element.tag.endswith("}pic"):
                try:
                    blob = sh.image.blob
                except Exception:
                    continue  # embedded video (slides 31, 32, 42)
                crop = tuple(max(0.0, v) for v in (sh.crop_left, sh.crop_top, sh.crop_right, sh.crop_bottom))
                out[(n, sh.shape_id)] = (blob, crop)

    for n, slide in enumerate(prs.slides, 1):
        walk(n, slide.shapes)
    return out


def decode(blob, crop):
    """The picture as the slide shows it (the slide's own crop applied)."""
    im = Image.open(io.BytesIO(blob))
    l, t, r, b = crop
    if l or t or r or b:
        w, h = im.size
        im = im.crop((round(l * w), round(t * h), round(w - r * w), round(h - b * h)))
    return im


def flat(im):
    """RGB on white (transparent PNG corners must not turn black)."""
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[-1])
        return bg
    return im.convert("RGB")


def side_by_side(ims):
    h = max(i.height for i in ims)
    ims = [i if i.height == h else i.resize((round(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    out = Image.new("RGB", (sum(i.width for i in ims) + GAP * (len(ims) - 1), h), (255, 255, 255))
    x = 0
    for i in ims:
        out.paste(i, (x, 0))
        x += i.width + GAP
    return out


def save(im, path, quality=85):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    if path.endswith(".png"):
        im.quantize(colors=128, method=Image.MEDIANCUT, dither=Image.NONE).save(path, optimize=True)
    else:
        im.save(path, quality=quality, optimize=True, progressive=True)
    return im.size, os.path.getsize(path)


def main():
    if not os.path.exists(DECK):
        sys.exit("deck not found: " + DECK)
    os.makedirs(OUT, exist_ok=True)
    pics = pictures(Presentation(DECK))
    total = 0
    for name, parts, scale, *q in FIGS:
        ims = []
        for key in parts:
            if key not in pics:
                sys.exit("missing picture: slide %d shape %d" % key)
            ims.append(flat(decode(*pics[key])))
        im = ims[0] if len(ims) == 1 else side_by_side(ims)
        if scale != 1:
            im = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
        (w, h), size = save(im, os.path.join(OUT, name), *q)
        total += size
        print("%-42s %4dx%-4d %6.1f KB" % (name, w, h, size / 1024))
    print("%d files, total %.1f KB" % (len(FIGS), total / 1024))


if __name__ == "__main__":
    main()
