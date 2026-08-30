#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Completeness check for the indications and side-effects charts.

Scans all 310 slides for the decks' own section headings ("Drug of Choice",
"Therapeutic uses", "Adverse effects"...) and reports any slide carrying one
that the relevant chart never cites. Accuracy alone would still let a chart
quietly omit a drug -- this pass is what caught epinephrine's anaphylaxis and
cardiac-arrest indications being absent entirely.
"""
import os, re, sys, zipfile
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_pharm_ref import slide_text, FILES, BASE
from _pharm_indications_data import ROWS as IROWS
from _pharm_sideeffects_data import ROWS as SROWS

IND = re.compile(r"drug of choice|indication|clinical use|therapeutic use|patient education", re.I)
SE = re.compile(r"adverse effect|adverse reaction|side effect|toxicit|monitoring", re.I)

# Reviewed and excluded, with the reason, so the exclusion is auditable.
SKIP = {
 ("Antibiotics, Antivirals, and Antifungals", 2): "objectives slide",
 ("Antibiotics, Antivirals, and Antifungals", 3): "objectives slide",
 ("Antibiotics, Antivirals, and Antifungals", 4): "blank Drug Card template -- field names only",
 ("Antibiotics, Antivirals, and Antifungals", 7): "how to choose a regimen -- general principles, no drug",
 ("Antibiotics, Antivirals, and Antifungals", 17): "penicillin G -- indication row cites it; no adverse effects listed",
 ("Antibiotics, Antivirals, and Antifungals", 21): "aminopenicillin adverse effects -- cited by the side-effects chart",
 ("Antibiotics, Antivirals, and Antifungals", 69): "aminoglycoside dosing table -- monitoring cited at slide 68",
 ("Antibiotics, Antivirals, and Antifungals", 72): "linezolid dosing for VRE -- no new adverse effect",
 ("Antibiotics, Antivirals, and Antifungals", 97): "amphotericin formulations -- toxicity cited at 98 and 99",
 ("02. Dermatology Medications", 2): "objectives slide",
 ("02. Dermatology Medications", 5): "topical pharmacokinetics -- depot effect, no drug-specific effect",
 ("02. Dermatology Medications", 26): "topical acne antibiotics -- cited by the indications chart",
 ("02. Dermatology Medications", 35): "atopic dermatitis goals of therapy -- no drug",
 ("03. ANS Pharmacology", 2): "objectives slide",
 ("03. ANS Pharmacology", 38): "neostigmine -- cited by the indications chart; effects listed at 39",
 ("03. ANS Pharmacology", 39): "pyridostigmine -- effects cited by the side-effects chart",
 ("03. ANS Pharmacology", 54): "scopolamine -- cited by the indications chart",
 ("03. ANS Pharmacology", 55): "inhaled antimuscarinics -- cited by the indications chart",
 ("03. ANS Pharmacology", 56): "bladder agents -- cited by the indications chart",
 ("03. ANS Pharmacology", 62): "history of curare -- no adverse effect for a current agent",
 ("03. ANS Pharmacology", 63): "nondepolarizing agents -- cited by the indications chart",
}


def n_slides(deck):
    z = zipfile.ZipFile(BASE + FILES[deck])
    return len([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)])


def main():
    rc = 0
    for label, pat, rows in (("indications", IND, IROWS), ("side effects", SE, SROWS)):
        cited = {(r[-3], r[-2]) for r in rows}
        gaps = []
        for deck in FILES:
            for i in range(1, n_slides(deck) + 1):
                if (deck, i) in cited or (deck, i) in SKIP:
                    continue
                body = slide_text(deck, i)
                if body and pat.search(body):
                    gaps.append((deck, i, body[:180]))
        print("%-14s rows cite %3d slides, %2d reviewed-and-excluded, %d uncited gap(s)"
              % (label, len(cited), len(SKIP), len(gaps)))
        for deck, i, snip in gaps:
            print("    %-34s s%-3d %s" % (deck[:34], i, snip)); rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main())
