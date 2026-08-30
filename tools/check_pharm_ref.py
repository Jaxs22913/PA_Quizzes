#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fact-check any Pharmacology I Exam 1 reference dataset against its decks.

Generalises check_pharm_contra.py to all three charts. Every dataset's rows end
with (..., deck, slide, verify) whatever else they carry, so one checker covers
contraindications, indications/education and side effects alike.

    python3 check_pharm_ref.py contra | indications | sideeffects | all
"""
import html as H
import os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

BASE = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/")
FILES = {"Antibiotics, Antivirals, and Antifungals": "Antibiotics, Antivirals, and Antifungals.pptx",
         "02. Dermatology Medications": "02. Dermatology Medications(1).pptx",
         "03. ANS Pharmacology": "03. ANS Pharmacology(1).pptx"}
DATASETS = {"contra": ("_pharm_contra_data", "contraindications"),
            "indications": ("_pharm_indications_data", "indications & patient education"),
            "sideeffects": ("_pharm_sideeffects_data", "side effects")}
_cache = {}


def norm(s):
    s = H.unescape(s)
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), ("−", "-"), ("\xa0", " "),
                 ("…", "..."), ("​", "")):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def slide_text(deck, n):
    key = (deck, n)
    if key in _cache:
        return _cache[key]
    z = zipfile.ZipFile(BASE + FILES[deck])
    parts = []
    for member in ("ppt/slides/slide%d.xml" % n, "ppt/notesSlides/notesSlide%d.xml" % n):
        if member in z.namelist():
            x = z.read(member).decode("utf-8", "ignore")
            runs = re.findall(r"<a:t>(.*?)</a:t>", x, re.S)
            parts.append(" ".join(runs))   # runs separated
            parts.append("".join(runs))    # runs joined -- PowerPoint splits words
    _cache[key] = norm(" ".join(parts))
    return _cache[key]


def check(key):
    mod, label = DATASETS[key]
    ROWS = __import__(mod).ROWS
    fails, checked = [], 0
    for i, row in enumerate(ROWS):
        deck, slide, verify = row[-3], row[-2], row[-1]
        body = slide_text(deck, slide)
        if not body:
            fails.append((i, row[0], deck, slide, ["<slide has no text>"])); continue
        missing = [v for v in verify if norm(v) not in body]
        checked += len(verify)
        if missing:
            fails.append((i, row[0], deck, slide, missing))
    plain = re.compile(r"<[^>]+>")
    print("%-30s rows: %3d   substrings checked: %4d   %s"
          % (label, len(ROWS), checked, "OK" if not fails else "FAILED %d" % len(fails)))
    for i, drug, deck, slide, missing in fails:
        print("    [%d] %s  -- cites %s slide %d" % (i, plain.sub("", drug), deck[:28], slide))
        for m in missing:
            print("        NOT ON SLIDE: %r" % m)
    return 0 if not fails else 1


if __name__ == "__main__":
    which = sys.argv[1] if len(sys.argv) > 1 else "all"
    keys = list(DATASETS) if which == "all" else [which]
    rc = 0
    for k in keys:
        try:
            rc |= check(k)
        except ImportError:
            print("%-30s (dataset not written yet)" % DATASETS[k][1])
    sys.exit(rc)
