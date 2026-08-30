#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The completeness half of the fact-check.

check_pharm_contra.py proves every row is TRUE. This proves the page is not
MISSING anything: it scans all 310 slides across the three decks for
contraindication-grade signal words and reports any slide carrying one that no
row cites. Accuracy without coverage would still let the page quietly omit a
contraindication the exam asks about.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pharm_contra_data import ROWS
from check_pharm_contra import slide_text, FILES, BASE
import zipfile

# Strong signals only -- "adverse effects" alone appears on ~half the deck and
# would drown the report. These are the words that mark a real prohibition.
SIGNAL = re.compile(
    r"contraindicat|black box|boxed warning|do not use|don't use|avoid|can't use|cannot use|"
    r"teratogen|pregnan|breastfeed|nursing|not be used|caution", re.I)

cited = {(d, s) for _, _, _, d, s, _ in ROWS}

# Reviewed and deliberately excluded, with the reason recorded so the exclusion
# is auditable rather than silent. Each of these trips a signal word without
# carrying a drug contraindication.
EXCLUDED = {
 ("Antibiotics, Antivirals, and Antifungals", 2):
   "objectives slide -- lists 'contraindications' as a heading of what will be taught",
 ("Antibiotics, Antivirals, and Antifungals", 3):
   "objectives slide -- same, for the antivirals and antifungals",
 ("Antibiotics, Antivirals, and Antifungals", 4):
   "the blank Drug Card template -- 'Contraindications (relative/absolute)' is a field name",
 ("02. Dermatology Medications", 2):
   "learning objectives slide",
 ("02. Dermatology Medications", 8):
   "vehicle/formulation comparison table -- 'avoid' is about cosmetic feel, not safety",
 ("02. Dermatology Medications", 16):
   "acne goals of therapy -- 'avoid psychological suffering'",
 ("02. Dermatology Medications", 36):
   "atopic dermatitis non-drug advice -- 'avoid overheating', a comfort measure",
 ("03. ANS Pharmacology", 2):
   "objectives slide -- lists 'contraindications' as a heading",
}


def n_slides(deck):
    z = zipfile.ZipFile(BASE + FILES[deck])
    return len([n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n)])


def main():
    gaps = []
    total = 0
    for deck in FILES:
        for i in range(1, n_slides(deck) + 1):
            total += 1
            body = slide_text(deck, i)
            if not body or not SIGNAL.search(body):
                continue
            if (deck, i) in cited or (deck, i) in EXCLUDED:
                continue
            hits = sorted(set(m.group(0).lower() for m in SIGNAL.finditer(body)))
            gaps.append((deck, i, hits, body))
    print("slides scanned: %d   rows cite %d distinct slides   "
          "%d reviewed and excluded" % (total, len(cited), len(EXCLUDED)))
    if not gaps:
        print("no uncited slide carries a contraindication signal")
        return 0
    print("\n%d slide(s) carry a signal word but are not cited by any row --\n"
          "review each and either add a row or record why it is out of scope:\n" % len(gaps))
    for deck, i, hits, body in gaps:
        print("  %s slide %d  signals=%s" % (deck[:34], i, hits))
        print("      %s\n" % body[:300])
    return 0


if __name__ == "__main__":
    sys.exit(main())
