#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Prove every ophthalmology master question is grounded in the slides.

Jaxon, 2026-09-06: "only use content from the slides". An audit that day found
nineteen terms in the pools that appear in NO ophthalmology deck -- whole
conditions the block never teaches (dacryostenosis, retrobulbar haemorrhage,
traumatic iritis, pseudostrabismus, anisometropia, neuroblastoma) alongside
correct-but-unused vocabulary (Seidel, phacoemulsification, brachytherapy).
Eleven questions had an OFF-SLIDE KEY, which is the serious kind: the answer
itself was untaught.

This checks the medical NOUNS in every question against the combined text of
the five decks. It is deliberately noun-level rather than sentence-level,
because the wording is ours and only the content has to be theirs.

    python3 tools/check_cmsophtho_grounding.py

Exits non-zero if any term is unfound, so the build can depend on it.
"""
import os, re, sys, zipfile
from xml.etree import ElementTree as ET

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
HERE = os.path.dirname(os.path.abspath(__file__))
INBOX = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2")
DECKS = ["CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx",
         "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx",
         "12. Acute Vision Loss current - Jaquith.pptx",
         "Chronic Vision Loss & Tumors - Dr Rappa.pptx",
         "CMS I Ocular Trauma - Shah Fallsv.pptx"]
POOLS = ["cmsophtho_l10_pool", "cmsophtho_l10b_pool", "cmsophtho_l10c_pool", "cmsophtho_l10d_pool",
         "cmsophtho_l11_pool", "cmsophtho_l11b_pool",
         "cmsophtho_l12_pool", "cmsophtho_l12b_pool", "cmsophtho_l12c_pool",
         "cmsophtho_l13_pool", "cmsophtho_l13b_pool", "cmsophtho_l13c_pool",
         "cmsophtho_l14_pool", "cmsophtho_l14b_pool", "cmsophtho_l14c_pool"]

# Clinical nouns worth checking. Ordinary English is not checked -- only the
# terms that would represent CONTENT if they were absent from the decks.
WATCH = """
dacryostenosis dacryocystitis dacryoadenitis chalazion hordeolum blepharitis
entropion ectropion dermatochalasis xanthelasma pinguecula pterygium chemosis
conjunctivitis trachoma episcleritis scleritis keratitis uveitis iritis
iridocyclitis choroiditis retinitis hypopyon cellulitis dendrite
amaurosis glaucoma tonometry iridotomy trabeculoplasty papilledema
detachment occlusion neuritis arteritis claudication cataract drusen
macular degeneration retinoblastoma melanoma nevus naevus strabismus amblyopia
myopia hyperopia astigmatism presbyopia esotropia exotropia nystagmus
anisocoria ptosis miosis mydriasis anhidrosis hyphema abrasion
proptosis enophthalmos entrapment emphysema chemical irrigation
horner argyll adie marcus gunn hutchinson
acyclovir aciclovir ceftriaxone erythromycin olopatadine acetazolamide
seidel phacoemulsification brachytherapy pituitary neuroblastoma
oculocardiac retrobulbar pseudostrabismus anisometropia monomeric epicanthic
""".split()


def deck_text():
    out = []
    for fn in DECKS:
        p = os.path.join(INBOX, fn)
        if not os.path.exists(p):
            sys.exit("deck not found: %s" % fn)
        z = zipfile.ZipFile(p)
        n = len([x for x in z.namelist() if re.fullmatch(r"ppt/slides/slide\d+\.xml", x)])
        for i in range(1, n + 1):
            root = ET.fromstring(z.read("ppt/slides/slide%d.xml" % i))
            out.append(" ".join(t.text for t in root.iter(A + "t") if t.text))
    return re.sub(r"\s+", " ", " ".join(out)).lower()


def main():
    sys.path.insert(0, HERE)
    import importlib
    deck = deck_text()
    absent = {w for w in WATCH if w not in deck}

    bad, n = [], 0
    for m in POOLS:
        for i, q in enumerate(importlib.import_module(m).QUESTIONS):
            n += 1
            key = (q["q"] + " " + q["opts"][0][0] + " " + q["opts"][0][1]).lower()
            dis = " ".join(o[0] + " " + o[1] for o in q["opts"][1:]).lower()
            for w in absent:
                if re.search(r"\b%s" % re.escape(w), key):
                    bad.append("KEY  %s[%d] uses %r, which is in no deck" % (m, i, w))
                elif re.search(r"\b%s" % re.escape(w), dis):
                    bad.append("dist %s[%d] uses %r, which is in no deck" % (m, i, w))

    print("checked %d questions against %d decks" % (n, len(DECKS)))
    print("watched terms absent from every deck: %s"
          % (", ".join(sorted(absent)) if absent else "none"))
    if bad:
        print("\nFAILED -- off-slide content:")
        for b in bad:
            print("  " + b)
        return 1
    print("every question is grounded in the slides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
