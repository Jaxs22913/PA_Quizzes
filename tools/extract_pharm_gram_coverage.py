#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pull the gram-coverage traffic lights out of the antibiotics deck.

THE DECK ALREADY ANSWERS THIS QUESTION, in a form nobody reads as data. Most
antibiotic class slides carry a small three-column table -- Gram Positive,
Gram Negative, Anaerobes -- with a coloured circle under each heading:

    008000 dark green    = covers it        (39 circles)
    00B050 medium green  = covers it        (3 -- macrolides, polymyxins)
    92D050 light green   = moderate         (3 -- tetracyclines only)
    FFFF00 yellow        = partial/limited  (9 circles)
    FF0000 red           = does not cover   (27 circles)

THE DECK USES TWO INTERCHANGEABLE GREENS and one distinctly lighter one. The
two full greens are treated as the same verdict here; the light green is kept
separate because it appears on exactly one class -- tetracyclines, on all three
columns at once -- which reads as deliberate rather than as a colour slip.

Nothing in the slide TEXT says which colour sits under which heading; the
association is purely positional. So each circle is matched to a heading by
comparing x-coordinates, which is the same reading-order problem recorded in
[[lettered_slide_images]] and solved the same way.

This is the lecturer's own judgement of coverage, not an inference from prose,
which is what makes it worth building a page on.
"""
import json, os, re, zipfile
from xml.etree import ElementTree as ET

P = '{http://schemas.openxmlformats.org/presentationml/2006/main}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
DECK = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/"
                          "Antibiotics, Antivirals, and Antifungals.pptx")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "pharm_gram_coverage.json")
COLOUR = {"008000": "yes", "00B050": "yes", "92D050": "moderate",
          "FFFF00": "partial", "FF0000": "no"}


def shapes(root):
    out = []
    for sp in root.iter(P + 'sp'):
        xfrm = sp.find('.//' + A + 'xfrm')
        if xfrm is None:
            continue
        off, ext = xfrm.find(A + 'off'), xfrm.find(A + 'ext')
        if off is None or ext is None:
            continue
        prst = sp.find('.//' + A + 'prstGeom')
        fill = sp.find('.//' + A + 'solidFill/' + A + 'srgbClr')
        txt = " ".join(t.text or "" for t in sp.iter(A + 't')).strip()
        out.append(dict(x=int(off.get('x')), y=int(off.get('y')),
                        w=int(ext.get('cx')), h=int(ext.get('cy')),
                        geom=prst.get('prst') if prst is not None else None,
                        fill=(fill.get('val').upper() if fill is not None else None),
                        text=txt))
    return out


def main():
    assert os.path.exists(DECK), "deck not found: %s" % DECK
    z = zipfile.ZipFile(DECK)
    n = len([x for x in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", x)])
    found = {}
    for i in range(1, n + 1):
        root = ET.fromstring(z.read("ppt/slides/slide%d.xml" % i))
        sh = shapes(root)
        heads = [s for s in sh if s["text"] in ("Gram Positive", "Gram Negative", "Anaerobes")]
        dots = [s for s in sh if s["geom"] == "ellipse" and s["fill"] in COLOUR]
        if len(heads) < 2 or not dots:
            continue
        title = next((t.text for t in root.iter(A + 't') if t.text), "").strip()
        cov = {}
        for d in dots:
            cx = d["x"] + d["w"] / 2
            # nearest heading whose column contains this circle's centre
            best = min(heads, key=lambda h: abs((h["x"] + h["w"] / 2) - cx))
            cov[best["text"]] = COLOUR[d["fill"]]
        found[i] = dict(title=title, coverage=cov)
    json.dump(found, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("slides with a coverage widget: %d" % len(found))
    for i, v in sorted(found.items(), key=lambda kv: int(kv[0])):
        c = v["coverage"]
        print("  s%-4d %-42s +:%-8s -:%-8s anaer:%s"
              % (i, v["title"][:42], c.get("Gram Positive", "-"),
                 c.get("Gram Negative", "-"), c.get("Anaerobes", "-")))


if __name__ == "__main__":
    main()
