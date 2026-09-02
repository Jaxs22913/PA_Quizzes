#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Flag words in our content that are in neither the dictionary nor the decks.

A medical page is full of words no dictionary carries, so a plain spell check
drowns in false positives. The trick here is that the SOURCE POWERPOINTS are a
domain wordlist: a word we wrote that appears in no dictionary AND in none of
the decks it was written from is very likely a typo we introduced.

British spellings are accepted by rule rather than by list -- the dictionary is
American, so -ise/-isation/-aemia/-oedema forms are normalised before lookup.

    python3 tools/check_spelling.py "Clinical Medicine and Surgery I Exam 2" \
        ~/Desktop/"Semester 2"/"Clinical Medicine and Surgery I Inbox"/"Exam 2"

FOUR FALSE-POSITIVE SHAPES, so a hit list is quick to read rather than alarming:

  1. STYLED FIRST LETTERS. "<strong>V</strong>isual" and "HYPOchromic" split at
     the case boundary, giving "isual" and "Ochromic". Both render correctly.
  2. HTML ENTITIES. "M&uuml;ller's" and "caf&eacute;-au-lait" surface as
     "uuml", "ller", "caf" and "lait".
  3. PROPER NOUNS AND CITATIONS -- author surnames, journal names, eponyms the
     dictionary does not carry.
  4. QUOTED SPEECH. A lecturer's "gonna", "okay" or "schmutz" is correct as
     quoted and must not be tidied.

Everything left after those is worth reading. On its first run over CMS Exam 2
and PDM Exam 1 it found exactly one real defect, "Xanthalasma" for
"Xanthelasma", against 26 correct uses elsewhere on the same site.
"""
import os, re, sys, zipfile
from xml.etree import ElementTree as ET

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
WORD = re.compile(r"[A-Za-z][a-z]{2,}(?:['\u2019][a-z]+)?")


def dictionary():
    words = set()
    with open("/usr/share/dict/words", encoding="utf8", errors="ignore") as fh:
        for line in fh:
            words.add(line.strip().lower())
    return words


def deck_words(folder):
    out = set()
    for fn in os.listdir(folder):
        if not fn.endswith(".pptx"):
            continue
        z = zipfile.ZipFile(os.path.join(folder, fn))
        for n in z.namelist():
            if not re.match(r"ppt/(slides/slide|notesSlides/notesSlide)\d+\.xml$", n):
                continue
            for t in ET.fromstring(z.read(n)).iter(A + "t"):
                if t.text:
                    for w in WORD.findall(t.text):
                        out.add(w.lower())
    return out


def stems(w):
    """The word plus every inflected form stripped back to a plausible root.

    /usr/share/dict/words carries base forms only, so without this every
    ordinary plural and past tense reads as a misspelling.
    """
    out = {w}
    w = re.sub(r"['\u2019]s$", "", w)          # possessive
    out.add(w)
    for suf, repls in (("ies", ["y"]), ("es", ["", "e"]), ("s", [""]),
                       ("ed", ["", "e"]), ("ing", ["", "e"]),
                       ("er", ["", "e"]), ("est", ["", "e"]),
                       ("ly", [""]), ("ness", [""])):
        if w.endswith(suf) and len(w) > len(suf) + 2:
            root = w[:-len(suf)]
            for r in repls:
                out.add(root + r)
            if len(root) > 2 and root[-1] == root[-2]:   # dropped -> drop
                out.add(root[:-1])
    return out


def variants(w):
    """American forms of a British spelling, so the US dictionary can match."""
    base = set()
    for x in stems(w):
        base.add(x)
        for a, b in (("ae", "e"), ("oe", "e"), ("ise", "ize"), ("isa", "iza"),
                     ("yse", "yze"), ("our", "or"), ("lling", "ling"),
                     ("lled", "led"), ("lling", "ling"), ("re", "er")):
            if a in x:
                base.add(x.replace(a, b))
    for x in list(base):
        base |= stems(x)
    return base


def main():
    target, inbox = sys.argv[1], os.path.expanduser(sys.argv[2])
    D = dictionary()
    deck = deck_words(inbox)
    known = D | deck
    suspect = {}
    for fn in sorted(os.listdir(target)):
        if not fn.endswith(".html"):
            continue
        text = open(os.path.join(target, fn), encoding="utf8").read()
        text = re.sub(r"<script.*?</script>", " ", text, flags=re.S)
        text = re.sub(r"<style.*?</style>", " ", text, flags=re.S)
        text = re.sub(r"<[^>]+>", " ", text)
        text = re.sub(r"&[a-z]+;|&#\d+;", " ", text)
        # split hyphenated compounds -- each half is checked on its own
        text = text.replace("-", " ").replace("\u2013", " ").replace("\u2014", " ")
        for w in WORD.findall(text):
            lw = w.lower()
            if any(v in known for v in variants(lw)):
                continue
            suspect.setdefault(lw, set()).add(fn)
    print("%d word(s) in neither the dictionary nor the decks:\n" % len(suspect))
    for w in sorted(suspect):
        files = sorted(suspect[w])
        print("  %-26s %s%s" % (w, files[0][:44],
                                "  (+%d more)" % (len(files) - 1) if len(files) > 1 else ""))


if __name__ == "__main__":
    main()
