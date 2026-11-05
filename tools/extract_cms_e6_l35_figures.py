#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 35 (Asthma, Prof. Finck) figures for the CMS I Exam 6 study guide.

    python3 tools/extract_cms_e6_l35_figures.py

Deck: "PAJ5500 CMSI Asthma MBF 2026sc.pptx" (108 slides). Every slide was viewed at 1920 px before choosing.
Slide images are cleared for use provided the slide is cited; every figure in tools/cms_e6_guide/l35.html
carries its slide number. Each picture is the deck's own embedded blob (the slide's crop applied, any
transparency flattened onto white), except slide 95, whose cascade is built from slide shapes (SmartArt) and
is cut from the 1920 px render (RENDER below), as is slide 7's flowchart (the slide shows only a
315 px crop of its picture, so the render's copy is the legible one).

Taken:
  slide 7   pathophysiology flowchart (inflammation -> airway hyper-responsiveness -> symptoms; triggers)
  slide 8   normal versus asthmatic bronchiole (drawing)
  slide 26  the allergy (immunoglobulin E) cascade, first and second exposure
  slide 55  spirometry with obstructive disease: a table that exists only as a picture (also an HTML table)
  slide 56  volume-time curve and flow-volume loop, normal versus asthma
  slide 57  before and after a bronchodilator: curves and the result table (a worked example, picture only)
  slide 61  the peak flow meter photograph; the peak flow meter in use with the graph of normal readings
  slide 62  Classification of Asthma Severity, 12 years and older (picture; the guide holds it as tables)
  slide 72  nebulizer and metered-dose inhaler with spacer
  slides 88, 89  the two asthma action plans (pictures; the zones are also an HTML table)
  slide 95  exercise-induced bronchospasm cascade (render crop)

Left out:
  slides 6, 54  YouTube video poster frames (a cartoon title card; a spirometry video still)
  slides 16, 17, 21, 22  epidemiology maps and charts (the lecturer: epidemiologic statistics are not tested);
            slides 15, 18-20 are slide tables of the same statistics
  slide 33  hygiene-hypothesis handwashing clip art (decoration)
  slide 38  dust mite micrograph; slide 65 Aspergillus micrograph: organism pictures with no finding to point at
  slides 9, 44, 67  text-only shapes (the airflow box, the history/physical/objective boxes, a "no" symbol)
  slide 69  respiratory treatments poster (product packaging and brand names)
  slide 97  "Asthma Care Quick Reference" cover art (title art)
  slides 101-105  the emergency-department algorithm: the lecturer said emergency management is not testable
            and the slides are for reference only, and the guide has no emergency section to put it beside
  slide 56  the McGraw-Hill logo (a separate small picture; the publisher credit inside the chart is kept)
"""
import io, os
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 6/"
                          "PAJ5500 CMSI Asthma MBF 2026sc.pptx")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6", "cms-e6-images")
# The 1920 px slide renders (LibreOffice export of the same deck); slides 7 and 95 are cut from them.
RENDER = os.environ.get("CMS_E6_RENDER_L35", "/private/tmp/claude-501/-Users-jaxonluke/"
                        "85b16e35-5425-4d68-aee8-6236b2cfbe15/scratchpad/render/l35_hi")
MAXW = 1400

# (slide, shape id or ("render", box), file name)
FIGS = [
    (7, ("render", (100, 112, 965, 917)), "l35-s007-pathophysiology-flowchart.png"),
    (8, 3074, "l35-s008-normal-vs-asthmatic-bronchiole.jpg"),
    (26, 4, "l35-s026-allergy-ige-cascade.png"),
    (55, 5122, "l35-s055-spirometry-obstruction-table.png"),
    (56, 8, "l35-s056-spirometry-normal-vs-asthma.png"),
    (57, 2051, "l35-s057-bronchodilator-response.png"),
    (61, 6147, "l35-s061-peak-flow-meter.jpg"),
    (61, 6146, "l35-s061-peak-flow-use-and-normals.png"),
    (62, 7170, "l35-s062-severity-classification.png"),
    (72, 6, "l35-s072-nebulizer.jpg"),
    (72, 7, "l35-s072-mdi-with-spacer.jpg"),
    (88, 12290, "l35-s088-action-plan.png"),
    (89, 13314, "l35-s089-action-plan-traffic-light.png"),
    (95, ("render", (740, 70, 1830, 1000)), "l35-s095-exercise-bronchospasm-cascade.png"),
]


def walk(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes)
        else:
            yield sh


def flat(im):
    im.load()
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        return bg
    return im.convert("RGB")


def picture(slide, n, shape_id):
    for sh in walk(slide.shapes):
        if sh.shape_id == shape_id:
            im = flat(Image.open(io.BytesIO(sh.image.blob)))
            w, h = im.size
            l, t = round(sh.crop_left * w), round(sh.crop_top * h)
            r, b = w - round(sh.crop_right * w), h - round(sh.crop_bottom * h)
            return im.crop((max(l, 0), max(t, 0), min(r, w), min(b, h)))
    raise SystemExit("slide %d: no picture with shape id %s" % (n, shape_id))


def render_crop(n, box):
    p = os.path.join(RENDER, "s%03d.png" % n)
    if not os.path.exists(p):
        raise SystemExit("missing render %s (set CMS_E6_RENDER_L35 to the 1920 px render folder)" % p)
    return flat(Image.open(p)).crop(box)


def save(im, name):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    path = os.path.join(OUT, name)
    if name.endswith(".png"):  # line art and tables: a 128-color palette keeps them small and sharp
        im.convert("P", palette=Image.ADAPTIVE, colors=128).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    print("%-48s %4dx%-4d %6.1f KB" % (name, im.width, im.height, os.path.getsize(path) / 1024))


def main():
    os.makedirs(OUT, exist_ok=True)
    slides = list(Presentation(DECK).slides)
    for n, src, name in FIGS:
        if isinstance(src, tuple) and src[0] == "render":
            im = render_crop(n, src[1])
        else:
            im = picture(slides[n - 1], n, src)
        save(im, name)


if __name__ == "__main__":
    main()
