#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fact-check every contraindication row against the slide it cites.

Reads the three Pharmacology I Exam 1 decks directly and asserts that each
row's `verify` substrings genuinely appear in the cited slide's own text. A row
that has drifted from the deck fails the build rather than shipping.

Normalisation only smooths over things that are formatting rather than
content: PowerPoint splits runs mid-word, so <a:t> fragments are joined; HTML
entities are decoded; curly quotes, dashes and non-breaking spaces are folded
to ASCII; whitespace is collapsed.
"""
import html as H
import os, re, sys, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from _pharm_contra_data import ROWS

BASE = os.path.expanduser("~/Desktop/Semester 2/Pharmacology I Inbox/Exam 1/")
FILES = {"Antibiotics, Antivirals, and Antifungals": "Antibiotics, Antivirals, and Antifungals.pptx",
         "02. Dermatology Medications": "02. Dermatology Medications(1).pptx",
         "03. ANS Pharmacology": "03. ANS Pharmacology(1).pptx"}
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
            # join runs with no separator too: PowerPoint splits words across <a:t>
            parts.append(" ".join(re.findall(r"<a:t>(.*?)</a:t>", x, re.S)))
            parts.append("".join(re.findall(r"<a:t>(.*?)</a:t>", x, re.S)))
    _cache[key] = norm(" ".join(parts))
    return _cache[key]


def main():
    fails, checked = [], 0
    for i, (drug, text, tier, deck, slide, verify) in enumerate(ROWS):
        body = slide_text(deck, slide)
        if not body:
            fails.append((i, drug, deck, slide, ["<slide has no text at all>"]))
            continue
        missing = [v for v in verify if norm(v) not in body]
        checked += len(verify)
        if missing:
            fails.append((i, drug, deck, slide, missing))

    plain = re.compile(r"<[^>]+>")
    print("rows: %d   substrings checked: %d" % (len(ROWS), checked))
    if fails:
        print("\nFAILED %d row(s):\n" % len(fails))
        for i, drug, deck, slide, missing in fails:
            print("  [%d] %s" % (i, plain.sub("", drug)))
            print("      cites %s slide %d" % (deck, slide))
            for m in missing:
                print("      NOT ON SLIDE: %r" % m)
            print()
        return 1
    print("every row verified against the slide it cites")
    return 0


if __name__ == "__main__":
    sys.exit(main())
