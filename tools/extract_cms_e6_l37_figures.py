"""Pull the Lecture 37 (Respiratory Infections, Prof. Bobilin) figures for the CMS I Exam 6 study guide.

    python3 tools/extract_cms_e6_l37_figures.py

Deck: "37. Respiratory Infections - Bobilin - 10-29-2026 SV.pptx" (the revised deck of 31 October, 133 slides;
slides 127-128 are his study-focus slides). Every slide was viewed at 1920 px before choosing. Slide images are
cleared for use provided the slide is cited; every figure in tools/cms_e6_guide/l37.html carries its slide number.
Each picture is the deck's own embedded blob (none of these is cropped on the slide; transparency flattened onto
white), never redrawn. The one exception is slide 30, whose calculator is three separate pictures laid out on the
slide: it is cut from the 1920 px render (RENDER below) so the score list and the class table stay together.

Taken (imaging, teaching diagrams, and every table that exists on the slide only as a picture):
  slide 21  the two AAFP tables (Table 3, managing expectations; Table 2, reducing antibiotic use), side by side;
            the guide also holds both as HTML tables
  slide 29  the CURB-65 admission algorithm (flowchart; the guide holds the CURB-65 tables)
  slide 30  the Pneumonia Severity Index calculator and its class table (render crop; also an HTML table)
  slide 31  the CURB-65 calculator picture (the guide holds it as a table)
  slide 32  chest X-ray, no label          slide 36  two chest X-rays, no label (kept as two files)
  slide 33  the "Classification of pneumonia according to CXR" table with its four films (also an HTML table)
  slide 34  frontal and lateral chest X-rays (the box and the "major fissure" arrows are in the picture)
  slide 35  right upper lobe Klebsiella consolidation with the bulging fissure (the slide's caption text is in the
            picture itself)
  slide 37  the "Cavities" film from the chest CT slide
  slide 41  "Table 1. Risk Factors and Pathogens in Community-Acquired Pneumonia" (the guide's HTML table of it
            already existed; the picture is added beside it)
  slide 48  the ventilator-associated pneumonia sources diagram
  slide 50  "Aspiration pneumonia in the elderly patient" diagram
  slide 51  "Pneumonitis vs. Pneumonia" diagram
  slide 52  two aspiration pneumonia chest X-rays (kept as two files)
  slide 54  lung abscess chest X-ray and CT with their arrows, set side by side as one picture
  slide 55  lung abscess chest X-ray and CT (one picture on the slide)
  slide 56  the four lung abscess CT panels a-d (one picture on the slide)
  slide 69  bronchoalveolar lavage diagram and lung biopsy diagram
  slide 70  Pneumocystis chest X-ray
  slide 75  the histoplasmosis map of the United States
  slide 106 influenza pneumonia chest X-ray (the deck's blob is 241 px wide; upscaled, still soft)
  slide 115 "Clinical presentation of patients with CoVID-19" body diagram
  slide 118 four COVID-19 chest X-rays, panels A-D with their arrows (one picture on the slide)

Left out:
  slides 14, 57, 74, 79, 90, 111  section title art (a glowing anatomy figure, a parrot, a virus rendering)
  slide 15  airway cross-section diagram on the acute bronchitis slide: it is labeled "During Asthma Symptoms"
            (normal vs asthma airway), so it shows asthma, not bronchitis
  slide 20  cough-syrup packaging (product photographs)
  slide 23  the "Typical community acquired pneumonia" medcomic cartoon
  slides 80, 81  pirate and parrot pictures and an album cover (visual puns on "parrot fever")
  slide 96  a one-week influenza-like-illness activity map (2023-24 season, week 43): a surveillance snapshot,
            not a finding or a mechanism
  slide 99  stock photograph of a stopwatch
  slide 117 stock photograph of a nasal swab
  slides 1-2, 127-133  title, objectives, study focus (text, already a table in the guide), questions, references
"""
import io, os
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DECK = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 6/"
                          "37. Respiratory Infections - Bobilin - 10-29-2026 SV.pptx")
# The 1920 px slide renders (LibreOffice export of the same deck); only slide 30 is cut from them.
RENDER = os.environ.get("L37_RENDER", "/private/tmp/claude-501/-Users-jaxonluke/"
                        "85b16e35-5425-4d68-aee8-6236b2cfbe15/scratchpad/render/l37_hi")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 6", "cms-e6-images")
MAXW = 1400
MINW = 700          # small scans are upscaled to about this width so they do not read as a smudge

# (slide, shape id or [ids side by side] or ("render", box), file name)
FIGS = [
    (21, [2050, 2052], "l37-s021-bronchitis-aafp-tables.jpg"),
    (29, 4100, "l37-s029-curb65-algorithm.jpg"),
    (30, ("render", (40, 0, 1800, 935)), "l37-s030-psi-calculator.png"),
    (31, 8, "l37-s031-curb65-calculator.png"),
    (32, 5, "l37-s032-pneumonia-cxr.jpg"),
    (33, 4, "l37-s033-cxr-classification.jpg"),
    (34, 18434, "l37-s034-frontal-lateral-cxr.jpg"),
    (35, 11266, "l37-s035-klebsiella-bulging-fissure.jpg"),
    (36, 15362, "l37-s036-pneumonia-cxr-a.jpg"),
    (36, 15364, "l37-s036-pneumonia-cxr-b.jpg"),
    (37, 4, "l37-s037-cavities.jpg"),
    (41, 20482, "l37-s041-cap-risk-pathogen-table.jpg"),
    (48, 22530, "l37-s048-vap-sources.jpg"),
    (50, 7, "l37-s050-aspiration-elderly.jpg"),
    (51, 9, "l37-s051-pneumonitis-vs-pneumonia.jpg"),
    (52, 7, "l37-s052-aspiration-cxr-a.jpg"),
    (52, 6, "l37-s052-aspiration-cxr-b.jpg"),
    (54, [8194, 8198], "l37-s054-lung-abscess-cxr-ct.jpg"),
    (55, 9218, "l37-s055-lung-abscess-cxr-ct.jpg"),
    (56, 12290, "l37-s056-lung-abscess-ct-panels.jpg"),
    (69, 3074, "l37-s069-bronchoalveolar-lavage.jpg"),
    (69, 3076, "l37-s069-lung-biopsy.jpg"),
    (70, 78853, "l37-s070-pneumocystis-cxr.jpg"),
    (75, 2050, "l37-s075-histoplasmosis-map.png"),
    (106, 2, "l37-s106-influenza-pneumonia-cxr.jpg"),
    (115, 6146, "l37-s115-covid-presentation.jpg"),
    (118, 5122, "l37-s118-covid-cxr-panels.jpg"),
]


def walk(shapes):
    for sh in shapes:
        if sh.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from walk(sh.shapes)
        else:
            yield sh


def flatten(im):
    if getattr(im, "is_animated", False):
        im.seek(0)                              # first frame of a GIF
    if im.mode in ("RGBA", "LA", "P", "PA"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, (255, 255, 255))
        bg.paste(im, mask=im.split()[3])
        return bg
    return im.convert("RGB")


def picture(slide, n, shape_id):
    for sh in walk(slide.shapes):
        if sh.shape_id == shape_id:
            im = Image.open(io.BytesIO(sh.image.blob))
            im.load()
            im = flatten(im)
            w, h = im.size
            l, t = round(sh.crop_left * w), round(sh.crop_top * h)
            r, b = w - round(sh.crop_right * w), h - round(sh.crop_bottom * h)
            return im.crop((max(l, 0), max(t, 0), min(r, w), min(b, h)))
    raise SystemExit("slide %d: no picture with shape id %s" % (n, shape_id))


def side_by_side(ims, gap=24):
    hh = max(i.height for i in ims)
    ims = [i.resize((round(i.width * hh / i.height), hh), Image.LANCZOS) for i in ims]
    out = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), hh), (255, 255, 255))
    x = 0
    for i in ims:
        out.paste(i, (x, 0))
        x += i.width + gap
    return out


def save(im, name):
    if im.width < MINW:
        f = MINW / im.width
        im = im.resize((MINW, round(im.height * f)), Image.LANCZOS)
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    path = os.path.join(OUT, name)
    if name.endswith(".png"):
        im.quantize(256, dither=Image.Dither.NONE).save(path, optimize=True)
    else:
        im.save(path, quality=85, optimize=True, progressive=True)
    print("%-44s %4dx%-4d %6.1f KB" % (name, im.width, im.height, os.path.getsize(path) / 1024))


def main():
    os.makedirs(OUT, exist_ok=True)
    slides = list(Presentation(DECK).slides)
    for n, sid, name in FIGS:
        s = slides[n - 1]
        if isinstance(sid, tuple):
            im = Image.open(os.path.join(RENDER, "s%03d.png" % n)).convert("RGB").crop(sid[1])
        elif isinstance(sid, list):
            im = side_by_side([picture(s, n, i) for i in sid])
        else:
            im = picture(s, n, sid)
        save(im, name)


if __name__ == "__main__":
    main()
