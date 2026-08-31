# -*- coding: utf-8 -*-
"""Which picture on a Lecture 13 slide is which, resolved by GEOMETRY.

Chronic Vision Loss & Tumors labels its figures A/B/C/D and ABOVE/BELOW, and the
extractors number images by their order in the slide's .rels file -- which has
nothing to do with where they sit. On slide 11 the relationship order 1,2,3,4
maps to labels A,D,C,B. Trusting the numbering here would have captioned soft
drusen as scar tissue.

Resolved by reading each <p:pic>'s x/y offset and each label shape's x/y, then
pairing a label to the picture directly above it in the same column. Spot-checked
by eye: l13-s011_1 is the dashed-circle macula full of soft drusen, which is
label A.

See [[lettered_slide_images]] and tools/check_lettered_slides.py.
"""

# slide -> {label: extracted-file suffix}
LABELS = {
    11: {"A": 1, "B": 4, "C": 3, "D": 2},   # AMD: soft drusen / hard drusen /
                                            # CNV haemorrhage / disciform scar
    44: {"A": 2, "B": 3, "C": 4, "D": 5},   # uveal melanoma: melanotic iris /
                                            # partly amelanotic iris / choroidal /
                                            # ciliary body. _1 carries no label.
    48: {"A": 2, "B": 1, "C": 5, "D": 3, "E": 4},  # iris: nonpigmented nevus /
                                            # pigmented nevus x2 / freckles /
                                            # Lisch nodules in neurofibromatosis 1
}

# slide -> {"ABOVE": suffix, "BELOW": suffix}
POSITIONS = {
    37: {"ABOVE": 1, "BELOW": 2},   # acquired: nuclear above, cortical below
    38: {"ABOVE": 2, "BELOW": 1},   # pediatric: polar above, nuclear below -- REVERSED
    52: {"ABOVE": 1, "BELOW": 2},   # conjunctival melanoma above, nevus below
}

# What each figure actually shows, for captions. Recognition is the skill, so
# these say what to look for rather than restating the label.
LOOK = {
    ("s011", "A"): "Soft drusen &mdash; large, pale, indistinct deposits at the macula",
    ("s011", "B"): "Hard drusen &mdash; small, discrete, sharply defined yellow dots",
    ("s011", "C"): "Haemorrhage from choroidal neovascularisation bleeding into retina",
    ("s011", "D"): "The disciform scar that haemorrhage leaves behind",
    ("s037", "ABOVE"): "Acquired nuclear cataract &mdash; the lens centre yellowed and dense",
    ("s037", "BELOW"): "Acquired cortical cataract &mdash; spokes running in from the edge",
    ("s038", "ABOVE"): "Pediatric polar cataract &mdash; a discrete opacity at the lens pole",
    ("s038", "BELOW"): "Pediatric nuclear cataract &mdash; central clouding in an infant lens",
    ("s044", "A"): "Melanotic iris melanoma &mdash; a raised pigmented mass on the iris",
    ("s044", "B"): "Partly amelanotic iris melanoma &mdash; pigment only in places",
    ("s044", "C"): "Choroidal melanoma &mdash; a dome of pigment under the retina",
    ("s044", "D"): "Ciliary body melanoma &mdash; note the sentinel vessel on the sclera",
    ("s048", "A"): "Nonpigmented iris nevus &mdash; flat and pale, not raised",
    ("s048", "B"): "Pigmented iris nevus &mdash; flat, under 3 mm, inferior iris",
    ("s048", "D"): "Iris freckles &mdash; surface pigment only, no stromal mass",
    ("s048", "E"): "Lisch nodules &mdash; tan domes, and a pointer to neurofibromatosis 1",
    ("s052", "ABOVE"): "Conjunctival melanoma &mdash; raised, vascular, often at the limbus",
    ("s052", "BELOW"): "Conjunctival nevus &mdash; flat, with clear cysts inside it",
}


def filename(slide, label):
    """l13-s011_1.png style name for a slide/label pair."""
    table = LABELS.get(slide) or POSITIONS.get(slide) or {}
    n = table.get(label)
    return None if n is None else "l13-s%03d_%d" % (slide, n)
