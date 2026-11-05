#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 9 (Diuretics and Heart Failure Drugs) figures for the Pharmacology I Exam 3 study guide.

Deck: "Diuretics and Heart Failure Drugs.pptx" (83 slides; Adam Wood, Pharm.D., DABAT). Every slide was rendered at
1920 px and viewed, and every picture in the deck was looked at full size, before these were chosen. Slide images
are cleared for use provided the slide is cited (each figure in _pharm_e3_guide_l9.py cites its slide).

TAKEN (file in "Pharmacology I Exam 3/pharm-e3-images/", slide, why):
  l09-slide-06-kidney-nephron.jpg       6   the kidney and one nephron, labeled: where every diuretic site sits.
                                            Two pictures on the slide, joined side by side at one height.
  l09-slide-07-nephron-sites.jpg        7   the nephron with the sodium and water arrows and the aldosterone and
                                            antidiuretic hormone arrows (slides 8 to 11 repeat this same picture
                                            beside each site's facts, so it is shown once).
  l09-slide-12-thick-ascending-limb.jpg 12  the loop diuretic target, the sodium-potassium-2 chloride carrier.
  l09-slide-21-distal-tubule.jpg        21  the thiazide target, the sodium-chloride transporter.
  l09-slide-30-collecting-tubule.jpg    30  the potassium-sparing target, the principal cell's sodium channel, with
                                            the aldosterone and antidiuretic hormone receptors (slide 34 repeats it).
  l09-slide-41-proximal-tubule-ca.jpg   41  the proximal tubule without and with carbonic anhydrase inhibitors (two
                                            pictures on the slide, joined side by side).
  l09-slide-49-heart-failure-cascade.jpg 49 the heart failure vicious circle. The slide is an embedded Word drawing
                                            whose only picture is a vector EMF, which the deck render leaves blank;
                                            drawn with tools/emf_render.py and checked word for word against
                                            tools/emf_text.py.
  l09-slide-62-digoxin-mechanism.jpg    62  digitalis on the sodium-potassium ATPase and the sodium-calcium exchanger;
                                            the same kind of embedded Word drawing (EMF), drawn the same way.
  l09-slide-70-digoxin-ecg.jpg          70  lead V6 in digoxin toxicity: normal sinus beats alternating with premature
                                            ventricular beats, the depressed ST segment arrowed.

LEFT OUT: slide 61 (the digoxin chemical structure) and slide 74 (milrinone and inamrinone structures): chemical
structures teach nothing the exam asks. Slides 8 to 11 and 34: duplicates of slides 7 and 30. Everything else is
text on the deck template. No slide in this deck carries a dose in a picture, and the deck has no guideline table.

    python3 tools/extract_pharm_e3_l9_figures.py
"""
import io, os, sys
from PIL import Image
from pptx import Presentation
from pptx.enum.shapes import MSO_SHAPE_TYPE

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
INBOX = os.path.expanduser("~/Desktop/PA Quizzes/Semester 2/Pharmacology I Inbox/Exam 3")
DECK = os.path.join(INBOX, "Diuretics and Heart Failure Drugs.pptx")
OUT = os.path.join(ROOT, "Pharmacology I Exam 3", "pharm-e3-images")
MAXW = 1400


def _walk(shapes):
    for s in shapes:
        if s.shape_type == MSO_SHAPE_TYPE.GROUP:
            yield from _walk(s.shapes)
        else:
            yield s


def slide_blobs(prs, n):
    """The pictures on slide n (1-based), top to bottom then left to right, as (bytes, extension, shape)."""
    out = []
    for s in _walk(prs.slides[n - 1].shapes):
        try:
            im = s.image
        except Exception:
            continue
        out.append((im.blob, im.ext, s))
    out.sort(key=lambda t: (round(t[2].top / 400000), t[2].left))
    return out


def slide_ole_emf(deck_zip, n):
    """The EMF preview picture of the embedded object on slide n (an OLE object has no shape.image)."""
    import zipfile, re
    z = zipfile.ZipFile(deck_zip)
    rels = z.read("ppt/slides/_rels/slide%d.xml.rels" % n).decode("utf-8")
    emfs = re.findall(r'Target="\.\./media/([^"]+\.emf)"', rels)
    assert len(emfs) == 1, "slide %d: expected one EMF, found %r" % (n, emfs)
    return z.read("ppt/media/" + emfs[0])


def picture(blob, shape=None):
    """Open a blob as RGB (transparent areas on white) and apply the slide's crop, if any."""
    im = Image.open(io.BytesIO(blob))
    if im.mode in ("RGBA", "LA", "P"):
        im = im.convert("RGBA")
        bg = Image.new("RGB", im.size, "white")
        bg.paste(im, mask=im.split()[3])
        im = bg
    else:
        im = im.convert("RGB")
    if shape is not None:
        l, t, r, b = shape.crop_left, shape.crop_top, shape.crop_right, shape.crop_bottom
        if any((l, t, r, b)):
            w, h = im.size
            im = im.crop((round(w * l), round(h * t), round(w * (1 - r)), round(h * (1 - b))))
    return im


def side_by_side(ims, gap=24):
    h = max(i.height for i in ims)
    ims = [i if i.height == h else i.resize((round(i.width * h / i.height), h), Image.LANCZOS) for i in ims]
    c = Image.new("RGB", (sum(i.width for i in ims) + gap * (len(ims) - 1), h), "white")
    x = 0
    for i in ims:
        c.paste(i, (x, 0))
        x += i.width + gap
    return c


def save(im, name, quality=88):
    if im.width > MAXW:
        im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
    path = os.path.join(OUT, name)
    im.save(path, "JPEG", quality=quality, subsampling=0, optimize=True)
    print("  %-40s %4dx%-4d %4d KB" % (name, im.width, im.height, os.path.getsize(path) // 1024))
    return im.size


def main():
    from emf_render import emf_to_image
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    os.makedirs(OUT, exist_ok=True)
    prs = Presentation(DECK)

    def one(n):
        pics = slide_blobs(prs, n)
        assert len(pics) == 1, "slide %d: expected one picture, found %d" % (n, len(pics))
        return picture(pics[0][0], pics[0][2])

    def all_of(n, count):
        pics = slide_blobs(prs, n)
        assert len(pics) == count, "slide %d: expected %d pictures, found %d" % (n, count, len(pics))
        return [picture(b, s) for b, _, s in pics]

    save(side_by_side(all_of(6, 2)), "l09-slide-06-kidney-nephron.jpg")
    save(one(7), "l09-slide-07-nephron-sites.jpg", 92)
    save(one(12), "l09-slide-12-thick-ascending-limb.jpg")
    save(one(21), "l09-slide-21-distal-tubule.jpg")
    save(one(30), "l09-slide-30-collecting-tubule.jpg")
    save(side_by_side(all_of(41, 2)), "l09-slide-41-proximal-tubule-ca.jpg")
    save(emf_to_image(slide_ole_emf(DECK, 49), 1400), "l09-slide-49-heart-failure-cascade.jpg", 90)
    save(emf_to_image(slide_ole_emf(DECK, 62), 1400), "l09-slide-62-digoxin-mechanism.jpg", 90)
    save(one(70), "l09-slide-70-digoxin-ecg.jpg")


if __name__ == "__main__":
    main()
