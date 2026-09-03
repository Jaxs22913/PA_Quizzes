#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the Lecture 2 and Lecture 3 figures the pharm study guide was missing.

Jaxon, 2026-09-03. The guide had six figures and ALL SIX were antibacterial or
antifungal -- the autonomic chapter, which is the one most in need of a
picture, had none, and dermatology had none either. Meanwhile the two decks
hold 64 usable images between them.

All 64 were rendered as contact sheets and looked at before these ten were
chosen. What they were chosen FOR:

  l3-s014  the master map -- which transmitter and which receptor sit at every
           synapse, autonomic and somatic, including the adrenal medulla. This
           is the figure the whole chapter hangs off.
  l3-s078  the deck's own adrenoceptor effects table. It says the same thing as
           the stimulate/block table added to 3.2 in the previous commit, in
           the lecturer's own words -- corroboration, not duplication.
  l3-s011  every organ, red for sympathetic and blue for parasympathetic.
  l3-s021  acetylcholine's six steps with the drug that blocks each one.
  l3-s049  the atropine DOSE LADDER -- slight cardiac slowing at 0.5 mg through
           to hallucinations and coma above 10. It illustrates the
           dose-response section added in the previous commit exactly.
  l3-s089  the norepinephrine tracing. Pulse, pressure and peripheral
           resistance on one time axis, and you can SEE the reflex bradycardia
           rather than being told about it.
  l3-s033  the same eye treated with pilocarpine and with atropine.
  l2-s020  acne's three factors as a Venn, with every drug placed on the factor
           it targets. The best single figure in the dermatology lecture.
  l2-s013  the acne cascade, normal follicle through to nodule.
  l2-s040  the topical steroid potency staircase, mild to very potent.

Deliberately not taken: the product photographs (a tube of tretinoin teaches
nothing), the iPLEDGE logo, the dense care-plan table, and the several
near-duplicate nervous-system tree slides that differ only in which branch is
highlighted.
"""
import os, re, struct, zipfile
from io import BytesIO
from xml.etree import ElementTree as ET
from PIL import Image

P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 1",
                   "pharm-exam-1-study-guide-images")
INBOX = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1")
DECKS = {"l2": "02. Dermatology Medications(1).pptx",
         "l3": "03. ANS Pharmacology(1).pptx"}

# (deck, slide, position-in-reading-order, output name)
WANT = [
    ("l3", 14, 1, "007.png"),
    ("l3", 78, 1, "008.png"),
    ("l3", 11, 1, "009.png"),
    ("l3", 21, 1, "010.png"),
    ("l3", 49, 1, "011.png"),
    ("l3", 89, 1, "012.png"),
    ("l3", 33, 1, "013.png"),
    ("l2", 20, 1, "014.png"),
    ("l2", 13, 1, "015.png"),
    ("l2", 40, 1, "016.png"),
]
ROW_TOL = 400000
MAXW = 620          # the guide lays figures out at 500-560px; this leaves headroom
EMR_STRETCHDIBITS = 81


def emf_dib(data):
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
    """Reading order: top to bottom, then left to right."""
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
        tgt = rels.get(blip.get(R + 'embed'))
        if off is None or not tgt:
            continue
        out.append((int(off.get('y')), int(off.get('x')), tgt))
    out.sort(key=lambda t: (round(t[0] / ROW_TOL), t[1]))
    return out


def main():
    os.makedirs(OUT, exist_ok=True)
    zips, sizes = {}, {}
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
        im.save(os.path.join(OUT, name), "PNG", optimize=True)
        sizes[name] = (im.width, im.height, deck, slide)
        print("  %-8s %4dx%-4d  %s slide %d" % (name, im.width, im.height, deck, slide))
    print("wrote %d figures" % len(WANT))
    return sizes


if __name__ == "__main__":
    main()
