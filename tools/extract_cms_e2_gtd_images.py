#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the seven Exam 2 ophthalmology pictures the chart never used.

WHY THESE SEVEN. Building "Guess that Disease" meant looking at all 225
pictures in the five Exam 2 decks, not just the 60 the comparison chart had
already picked. That audit turned up photographs the chart had passed over in
favour of a diagram, a table or a CT -- fine for a reference chart, useless for
an image the student is asked to name, and in three cases simply a worse
picture of the finding:

  l10-s052_pos2  post-septal (orbital) cellulitis -- PROPTOSIS with the globe
                 displaced. The chart's picture (s052_2) is a swollen lid,
                 which is what pre-septal looks like too.
  l11-s015_pos1  Horner syndrome -- ptosis with miosis. The chart had NO
                 picture for this row at all.
  l11-s040_pos1  cranial nerve III palsy -- the ptosis photograph. The chart
                 used the anatomical-course diagram (l11-s039_2).
  l11-s045_pos1  cranial nerve VI palsy in the nine cardinal gazes.
  l14-s029_pos1  lid laceration, before and after repair. The chart used the
                 eyelid cross-section (l14-s027_pos1), which is anatomy, not
                 an injury.
  l10-s033_pos1  bacterial conjunctivitis -- PAPILLAE on the everted lid.
  l10-s042_pos2  chlamydial conjunctivitis -- FOLLICLES on the everted lid.
                 Papillae vs follicles is the discrimination the block teaches
                 and neither was visible in the plain red-eye pictures.

POSITIONAL NAMING, per [[lettered_slide_images]]. Relationship order is not
visual order. `_posK` is top-to-bottom then left-to-right, the same scheme
tools/extract_cms_e2_l14_images.py uses -- and the same scheme that reproduced
slide 45's speaker note ("Top left: hemotympanum ... Bottom right: battle
sign") picture-for-picture, which is what validated it here.

900 px wide rather than the folder's usual 600: these are the pictures the
student is asked to identify, and theme.js's click-to-enlarge is the whole
point of the exercise.
"""
import os, re, struct, zipfile
from io import BytesIO
from xml.etree import ElementTree as ET
from PIL import Image

P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                   "cms-ophtho-chart-images")
INBOX = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2")
DECKS = {
    'l10': "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx",
    'l11': "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx",
    'l13': "Chronic Vision Loss & Tumors - Dr Rappa.pptx",
    'l14': "CMS I Ocular Trauma - Shah Fallsv.pptx",
}
# (deck, slide, position) -> output basename
WANT = [
    ('l10', 33, 1, 'l10-s033_pos1.jpg'),
    ('l10', 42, 2, 'l10-s042_pos2.jpg'),
    ('l10', 52, 2, 'l10-s052_pos2.jpg'),
    ('l11', 15, 1, 'l11-s015_pos1.jpg'),
    ('l11', 40, 1, 'l11-s040_pos1.jpg'),
    ('l11', 45, 1, 'l11-s045_pos1.jpg'),
    ('l14', 29, 1, 'l14-s029_pos1.jpg'),
    # Two more that only the chart and the guide use: the row's existing
    # picture is a document rather than a depiction of the finding.
    ('l11', 37, 1, 'l11-s037_pos1.jpg'),   # Adie tonic pupil, light-near dissociation
    ('l13', 32, 2, 'l13-s032_pos2.jpg'),   # amblyopia, the occlusion objection test
]
ROW_TOL = 400000          # EMU; two pictures within this are the same visual row
MAXW = 900
EMR_STRETCHDIBITS = 81


def emf_dib(data):
    """Lift the bitmap out of an .emf record, same path the chart extractor
    uses. Several of this deck's clinical photographs are stored as metafiles
    that CoreGraphics and Pillow both refuse -- the orbital-cellulitis picture
    is one of them, so without this the swap silently loses its best image."""
    off = 0
    while off + 8 <= len(data):
        itype, nsize = struct.unpack_from("<II", data, off)
        if nsize < 8:
            break
        if itype == EMR_STRETCHDIBITS and off + 64 <= len(data):
            ob, cb, obits, cbits = struct.unpack_from("<IIII", data, off + 48)
            if cb and cbits and off + obits + cbits <= len(data):
                bmi = data[off + ob: off + ob + cb]
                bits = data[off + obits: off + obits + cbits]
                return (b"BM" + struct.pack("<IHHI", 14 + len(bmi) + len(bits),
                                            0, 0, 14 + len(bmi)) + bmi + bits)
        off += nsize
    return None


def pictures(z, slide):
    """Every picture on a slide, in reading order."""
    root = ET.fromstring(z.read("ppt/slides/slide%d.xml" % slide))
    rels = {r.get("Id"): r.get("Target") for r in
            ET.fromstring(z.read("ppt/slides/_rels/slide%d.xml.rels" % slide))}
    out = []
    for pic in root.iter(P + 'pic'):
        blip = pic.find('.//' + A + 'blip')
        xfrm = pic.find('.//' + A + 'xfrm')
        if blip is None or xfrm is None:
            continue
        off = xfrm.find(A + 'off')
        if off is None:
            continue
        tgt = rels.get(blip.get(R + 'embed'))
        if not tgt:
            continue
        out.append((int(off.get('y')), int(off.get('x')), tgt))
    out.sort(key=lambda t: (round(t[0] / ROW_TOL), t[1]))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    zips = {}
    n = 0
    for deck, slide, pos, name in WANT:
        path = os.path.join(INBOX, DECKS[deck])
        assert os.path.exists(path), "deck not found: %s" % path
        z = zips.setdefault(deck, zipfile.ZipFile(path))
        pics = pictures(z, slide)
        assert len(pics) >= pos, "%s slide %d has %d pictures, wanted #%d" % (
            deck, slide, len(pics), pos)
        member = "ppt/media/" + pics[pos - 1][2].split("/")[-1]
        raw = z.read(member)
        if member.rsplit(".", 1)[-1].lower() in ("emf", "wmf"):
            raw = emf_dib(raw)
            assert raw, "could not decode metafile %s" % member
        im = Image.open(BytesIO(raw)).convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        im.save(os.path.join(OUT, name), "JPEG", quality=85, optimize=True)
        print("  %-22s %4dx%-4d  %s slide %d, picture %d"
              % (name, im.width, im.height, deck, slide, pos))
        n += 1
    print("wrote %d images" % n)


if __name__ == "__main__":
    main()
