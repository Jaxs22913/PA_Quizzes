#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 38 (Mycobacterial Infections including Tuberculosis, Prof. Bobilin) figures for the CMS I
Exam 6 study guide.

    python3 tools/extract_cms_e6_l38_figures.py

Deck: "38. Mycobacterial Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx" (the revised deck
of 31 October, 46 slides; slide 41 is his Study Focus slide). Every slide was viewed at 1920 px before choosing.
Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e6_guide/l38.html
carries its slide number. Each picture is the deck's own embedded blob (the slide's crop applied).

Taken:
  slide 12  the Robbins natural-history diagram (primary complex, healed and latent lesions, reactivation and
            reinfection to secondary tuberculosis, massive hematogenous dissemination to miliary tuberculosis)
  slide 20  reading a Mantoux tuberculin skin test with a millimeter ruler on the forearm
  slide 30  chest X-ray, the slide's "radiographic example" (the slide crops off the film's handwritten date;
            the same crop is applied here)
  slide 31  chest X-ray with two arrows: bilateral abnormalities and possible cavitation
  slide 32  cavitary lung disease: posteroanterior chest X-ray and coronal CT (one picture on the slide), and
            the latent / cavitary / miliary tuberculosis illustration (its stock-library watermark kept)

Not pictures: the stages (slides 9-10), skin-test thresholds (22), regimens (34-37), the nontuberculous
diagnostic criteria (39) and the Study Focus (41) are slide text, and the guide already holds each as an HTML
table or list.

Left out:
  slide 11  a Khan Academy video title card (decoration)
  slide 16  a film still from "Moulin Rouge" (decoration)
  slide 18  a film still of Doc Holliday on the differential-diagnosis slide (decoration)
  slides 34, 35  stock photographs of pills
  slide 43  a footer strip image; slides 1-3, 42-46  title, objectives, video link, questions, references
"""
import io, os
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 6/"
                          "38. Mycobacterial Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6", "cms-e6-images")
MAXW = 1400

# (slide, picture shape id, output name). A list of ids joins those pictures side by side.
FIGS = [
    (12, 5, "l38-s012-tb-natural-history.jpg"),
    (20, 23557, "l38-s020-tst-reading.jpg"),
    (30, 33797, "l38-s030-cxr-example.jpg"),
    (31, 34822, "l38-s031-cxr-bilateral-arrows.jpg"),
    (32, 7, "l38-s032-cavitary-cxr-ct.jpg"),
    (32, 5, "l38-s032-latent-cavitary-miliary.jpg"),
]

def walk(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes)
        else:
            yield sh


def picture(slide, shape_id):
    for sh in walk(slide.shapes):
        if sh.shape_id == shape_id:
            im = Image.open(io.BytesIO(sh.image.blob))
            im.load()
            if im.mode in ("RGBA", "LA", "P"):
                im = im.convert("RGBA")
                bg = Image.new("RGB", im.size, (255, 255, 255))
                bg.paste(im, mask=im.split()[3])
                im = bg
            else:
                im = im.convert("RGB")
            w, h = im.size
            l, t = round(sh.crop_left * w), round(sh.crop_top * h)
            r, b = w - round(sh.crop_right * w), h - round(sh.crop_bottom * h)
            return im.crop((max(l, 0), max(t, 0), min(r, w), min(b, h)))
    raise SystemExit("slide %d: no picture with shape id %s" % (slide.slide_id, shape_id))


def side_by_side(ims, gap=24):
    hh = min(i.height for i in ims)
    ims = [i.resize((round(i.width * hh / i.height), hh), Image.LANCZOS) for i in ims]
    out = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), hh), (255, 255, 255))
    x = 0
    for i in ims:
        out.paste(i, (x, 0))
        x += i.width + gap
    return out


def save(im, name):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    path = os.path.join(OUT, name)
    if name.endswith(".png"):  # line art and tables: a 128-color palette keeps them small and sharp
        im.convert("P", palette=Image.ADAPTIVE, colors=128).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    print("%-44s %4dx%-4d %6.1f KB" % (name, im.width, im.height, os.path.getsize(path) / 1024))


def main():
    os.makedirs(OUT, exist_ok=True)
    slides = list(Presentation(DECK).slides)
    for n, sid, name in FIGS:
        s = slides[n - 1]
        im = side_by_side([picture(s, i) for i in sid]) if isinstance(sid, list) else picture(s, sid)
        save(im, name)


if __name__ == "__main__":
    main()
