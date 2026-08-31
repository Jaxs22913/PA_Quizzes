#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find slides whose text explains several pictures LETTER BY LETTER.

Jaxon, 2026-08-31: "sometimes images on slides have letters and the same letters
on the slide with explanations are for that image respectively."

Why this needs a tool. Every image pipeline on this site pairs a picture with
the text of the slide it came from. That is right for a slide with one picture
and wrong for a slide with four, because the caption then describes the slide
rather than the photograph. It is silent when it goes wrong -- the picture is
real, the words are real, and only someone who opens the deck sees that they
belong to different letters. Two captions shipped wrong before this existed:

  L10 slide 18: "A. Blepharitis" / "B. Meibomitis". The shipped picture is A,
  and its caption had borrowed B's toothpaste-like meibomian secretion.
  L12 slide 45: a four-stage series, A acute with haemorrhages through D
  atrophic. One picture was standing for the whole condition under a caption
  describing a different stage.

What it reports. Every deck slide carrying two or more lettered explanations
AND two or more pictures, then which of those slides the site actually ships an
image from -- those are the ones that need a per-letter caption. A slide nobody
uses is listed as context, not as a problem.

    python3 tools/check_lettered_slides.py            # every Semester 2+ deck
    python3 tools/check_lettered_slides.py "Micro"    # decks matching a string
"""
import os, re, sys, zipfile, glob
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INBOX = os.path.expanduser("~/Desktop")

# "A. Something", "A) Something", "(A) Something" -- a label followed by prose.
LABEL = re.compile(r'(?:^|\s|\()([A-F])[\.\)\:]\s+(?=[A-Za-z])')
# mnemonics enumerate letters as the CONTENT, not as picture labels
MNEMONIC = re.compile(r"asymmetry|border irregularity|colou?r variation|diameter|evolving"
                      r"|onset|provocation|quality|radiation|severity|timing", re.I)


# Semester 2 forward only (Jaxon, 2026-08-31). Semester 1 is finished and frozen,
# so a lettered slide in a Physiology deck is not a defect anyone will act on --
# scanning it only produces noise to scroll past.
SEMESTERS = ("Semester 2", "Semester 3", "Semester 4")


def decks(filter_str=None):
    out = []
    for sem in SEMESTERS:
        base = os.path.join(INBOX, sem)
        if not os.path.isdir(base):
            continue
        for root, _, fs in os.walk(base):
            if "recordings" in root:
                continue
            for f in fs:
                if f.lower().endswith(".pptx") and not re.search(r"syllabus", f, re.I):
                    p = os.path.join(root, f)
                    if not filter_str or filter_str.lower() in p.lower():
                        out.append(p)
    return sorted(out)


def lettered(path):
    """[(slide_no, [letters], n_images, text)] for slides that look lettered."""
    z = zipfile.ZipFile(path)
    names = sorted((n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)),
                   key=lambda s: int(re.search(r'\d+', s.split('/')[-1]).group()))
    out = []
    for i, n in enumerate(names, 1):
        x = z.read(n).decode("utf8", "ignore")
        txt = " ".join(re.findall(r'<a:t>(.*?)</a:t>', x))
        rels = "ppt/slides/_rels/slide%d.xml.rels" % i
        nimg = 0
        if rels in z.namelist():
            nimg = len(re.findall(r'Target="\.\./(media/[^"]+)"',
                                  z.read(rels).decode("utf8", "ignore")))
        letters = sorted(set(m.group(1) for m in LABEL.finditer(txt)))
        if len(letters) >= 2 and nimg >= 2 and not MNEMONIC.search(txt):
            out.append((i, letters, nimg, re.sub(r"\s+", " ", txt)[:160]))
    return out


def class_token(path):
    """The course name a deck or a site folder belongs to, for matching them up.

    Matching on slide number alone is not enough: ophthalmology slide 18 and a
    physiology slide 18 both exist, and pairing them flagged a frozen Semester 1
    deck that nothing actually references."""
    for part in path.split(os.sep):
        m = re.match(r"(.+?) (?:Inbox|Exam \d+)$", part)
        if m:
            return m.group(1).lower()
    return ""


def shipped_slides():
    """{(course, slide number): [site files]} for every image the site displays."""
    used = defaultdict(list)
    for f in glob.glob(os.path.join(ROOT, "*", "*.html")):
        course = class_token(f)
        s = open(f, encoding="utf8", errors="ignore").read()
        for src in set(re.findall(r'src="([^"]*-images/[^"]+)"', s)):
            m = re.search(r'(?:^|/|-)(?:l(\d+)-)?s(\d{2,3})_\d+\.', src)
            if m:
                used[(course, int(m.group(2)))].append(os.path.basename(f))
    return used


def main(argv):
    filt = argv[1] if len(argv) > 1 else None
    used = shipped_slides()
    total = flagged = 0
    for p in decks(filt):
        rows = lettered(p)
        if not rows:
            continue
        name = os.path.basename(p)
        course = class_token(p)
        head = False
        for sl, letters, nimg, txt in rows:
            total += 1
            where = used.get((course, sl), [])
            in_use = bool(where)
            if not head:
                print("\n%s" % name)
                head = True
            mark = "  <-- SITE SHIPS AN IMAGE FROM THIS SLIDE" if in_use else ""
            if in_use:
                flagged += 1
            print("   slide %-4d %d pictures, labels %s%s" % (sl, nimg, "/".join(letters), mark))
            print("      %s" % txt)
            if in_use:
                print("      used by: %s" % ", ".join(sorted(set(where))))
    print("\n%d lettered slide(s) across the decks; %d of them are slides the site "
          "takes a picture from." % (total, flagged))
    if flagged:
        print("For those, the caption must come from the picture's OWN letter, and if the "
              "letters are stages of one condition, show more than one of them.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
