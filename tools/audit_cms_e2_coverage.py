#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Scour every CMS I Exam 2 PowerPoint against the guide, chart and cram sheet.

Scores COVERAGE PER SLIDE, not per word. For each slide it takes the
distinctive content terms and measures how many appear anywhere in the three
reference documents. A slide scoring low is a candidate gap -- something the
lecturer put up that a student revising from our material would not meet.

Slide-level is the useful unit because it points at what to go and read. A word
list is unusable: URLs, author names and phrasing differences bury the handful
of real misses under hundreds of false ones.

It reads SPEAKER NOTES THROUGH EACH SLIDE'S .rels, never by index. In these
decks the two disagree -- 28 of 38 notes in the ophthalmology deck and all nine
in the trauma deck belong to a different slide than their number suggests.

Title, objective, reference and image-only slides carry no testable prose and
are reported separately rather than counted as gaps.

    python3 tools/audit_cms_e2_coverage.py             # slides under the bar
    python3 tools/audit_cms_e2_coverage.py --bar 0.7   # stricter
    python3 tools/audit_cms_e2_coverage.py --show 12   # print a slide's terms
"""
import os, re, sys, zipfile
from xml.etree import ElementTree as ET

A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2")
BASE = os.path.expanduser("~/Desktop/Semester 2/Clinical Medicine and Surgery I Inbox/Exam 2")

DECKS = [
 ("L10 Ophthalmology I", "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx"),
 ("L11 Neuro-Ophthalmology", "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx"),
 ("L12 Acute Vision Loss", "12. Acute Vision Loss current - Jaquith.pptx"),
 ("L13 Chronic Vision Loss", "Chronic Vision Loss & Tumors - Dr Rappa.pptx"),
 ("L14 Ocular Trauma", "CMS I Ocular Trauma - Shah Fallsv.pptx"),
]
REFS = ["cms-exam-2-study-guide.html", "cms-ophtho-comparison-chart.html",
        "cms-exam-2-cram-sheet.html"]

STOP = set("""the a an and or of to in on at by with for from that which this these those is are was
were be as it its their they them into within between not no only also both each more most than then
when where what how why during over under above below near primary function located include includes
structure structures body region part parts point area surface used serve help form found contains
along across around due lies main major minor left right side upper lower anterior posterior medial
lateral superior inferior distal proximal deep small large may can will should would could must other
others another same different first second third next last new old high low increase decrease normal
abnormal patient patients treatment management diagnosis clinical exam examination test testing
slide slides lecture lectures figure figures image images source copyright reserved rights education
mcgraw hill available https http www com org edu content book section accessmedicine mhmedical
ezproxylocal library nova bookid sectionid reproduced permission professor assistant program
fall student version questions case study references objectives instructional describe identify
compare contrast discuss explain define list state review summary note notes there here what's
example examples usually often sometimes always never common commonly rare rarely
etiology epidemiology risk factors manifestations differential appropriate referrals prognosis""".split())

WORD = re.compile(r"[A-Za-z][A-Za-z'\-]{3,}")
VOWEL = re.compile(r"[aeiou].*[aeiou]")
HASHY = re.compile(r"^[A-Za-z]*[a-z][A-Z]")


def slide_terms(z, i):
    def num(n): return int(re.search(r"(\d+)", n.split("/")[-1]).group(1))
    txt = " ".join(t.text for t in ET.fromstring(z.read("ppt/slides/slide%d.xml" % i)).iter(A + "t")
                   if t.text and t.text.strip())
    try:
        for r in ET.fromstring(z.read("ppt/slides/_rels/slide%d.xml.rels" % i)):
            if "notesSlide" in (r.get("Target") or ""):
                nn = num(r.get("Target"))
                txt += " " + " ".join(
                    t.text for t in ET.fromstring(
                        z.read("ppt/notesSlides/notesSlide%d.xml" % nn)).iter(A + "t")
                    if t.text and t.text.strip())
    except Exception:
        pass
    txt = re.sub(r"\S*http\S*", " ", txt)
    terms = set()
    for w in WORD.findall(txt):
        lw = w.lower()
        if lw in STOP or len(lw) < 5 or not VOWEL.search(lw) or HASHY.match(w):
            continue
        terms.add(lw)
    return terms, txt


def main():
    bar = 0.60
    if "--bar" in sys.argv:
        bar = float(sys.argv[sys.argv.index("--bar") + 1])
    ref = " ".join(open(os.path.join(DIR, f), encoding="utf8").read() for f in REFS).lower()
    ref = re.sub(r"<[^>]+>", " ", ref)

    for label, fname in DECKS:
        path = os.path.join(BASE, fname)
        if not os.path.exists(path):
            print("  MISSING DECK: %s" % fname); continue
        z = zipfile.ZipFile(path)
        def num(n): return int(re.search(r"(\d+)", n.split("/")[-1]).group(1))
        n_slides = len([n for n in z.namelist()
                        if re.match(r"ppt/slides/slide\d+\.xml$", n)])
        low, thin = [], 0
        for i in range(1, n_slides + 1):
            terms, txt = slide_terms(z, i)
            if len(terms) < 6:          # title, objectives, image-only, references
                thin += 1
                continue
            hit = sum(1 for t in terms
                      if t in ref or (t.endswith("s") and t[:-1] in ref))
            frac = hit / len(terms)
            if frac < bar:
                miss = sorted(t for t in terms
                              if t not in ref and not (t.endswith("s") and t[:-1] in ref))
                low.append((frac, i, len(terms), miss))
        print("\n=== %s  --  %d slides (%d too thin to score) ===" % (label, n_slides, thin))
        if not low:
            print("    every scored slide is at least %d%% covered" % (bar * 100))
        for frac, i, n, miss in sorted(low):
            print("    slide %-3d %3d%% covered (%2d terms)  missing: %s"
                  % (i, frac * 100, n, ", ".join(miss[:9])))


if __name__ == "__main__":
    main()
