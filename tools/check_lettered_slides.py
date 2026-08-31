#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Find slides whose text explains several pictures ONE AT A TIME.

Jaxon, 2026-08-31: "sometimes images on slides have letters and the same letters
on the slide with explanations are for that image respectively." And later the
same day: "sometimes images will also have above and below with descriptors for
images that are on that slide" -- so the pointer can be POSITIONAL as well as
lettered. A cataract slide reads "ABOVE Acquired nuclear, BELOW Acquired
cortical" over two stacked photographs.

Positional captions are the more dangerous of the two, because resolving them
needs the picture's GEOMETRY and every extractor here numbers images by their
order in the slide's .rels file -- which is relationship order, not top-to-bottom.
s012_1.jpg is simply the first relationship, and may be the lower picture. So
this tool reads each <p:pic>'s x/y offset and reports which numbered file is
actually ABOVE, BELOW, LEFT and RIGHT.

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
# The same thing with NO punctuation. PowerPoint keeps each figure label in its
# own text run, so a slide reading "A / soft drusen / B / hard drusen" joins to
# "A soft drusen B hard drusen" and the punctuated pattern above finds nothing.
# This missed every lettered slide in the Chronic Vision Loss deck.
BARE = re.compile(r'(?:^|\|\s*|\s)([A-F])\s+(?=[a-z])')
# "ABOVE x, BELOW y" -- a position used as the pointer instead of a letter.
POS = re.compile(r'\b(ABOVE|BELOW|TOP|BOTTOM|LEFT|RIGHT|UPPER|LOWER|MIDDLE|CENTER|CENTRE)\b', re.I)
OPPOSITES = (("ABOVE", "BELOW"), ("TOP", "BOTTOM"), ("UPPER", "LOWER"), ("LEFT", "RIGHT"))
EMU = 914400.0  # English Metric Units per inch, for readable coordinates
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


def picture_geometry(z, slide_no):
    """[(rels_index, inches_x, inches_y)] -- rels_index is what the extractors name a file.

    The extractors do `enumerate(findall(Target=...media/...), 1)` over the .rels
    file, so file _k is the k-th relationship. That order has nothing to do with
    where the picture sits, which is why this has to be read from the slide XML."""
    rel = "ppt/slides/_rels/slide%d.xml.rels" % slide_no
    if rel not in z.namelist():
        return []
    rx = z.read(rel).decode("utf8", "replace")
    # relationship order == the extractors' numbering
    order = {}
    for k, m in enumerate(re.finditer(r'Id="(rId\d+)"[^>]*Target="\.\./media/([^"]+)"', rx), 1):
        order[m.group(1)] = k
    out = []
    sx = z.read("ppt/slides/slide%d.xml" % slide_no).decode("utf8", "ignore")
    for blk in re.findall(r'<p:pic>.*?</p:pic>', sx, re.S):
        rid = re.search(r'r:embed="(rId\d+)"', blk)
        off = re.search(r'<a:off x="(-?\d+)" y="(-?\d+)"', blk)
        if rid and off and rid.group(1) in order:
            out.append((order[rid.group(1)], int(off.group(1)) / EMU, int(off.group(2)) / EMU))
    return out


def resolve(geom):
    """{'ABOVE': k, 'BELOW': k, 'LEFT': k, 'RIGHT': k} from the pictures' positions."""
    if len(geom) < 2:
        return {}
    by_y = sorted(geom, key=lambda g: g[2])
    by_x = sorted(geom, key=lambda g: g[1])
    out = {"ABOVE": by_y[0][0], "TOP": by_y[0][0], "UPPER": by_y[0][0],
           "BELOW": by_y[-1][0], "BOTTOM": by_y[-1][0], "LOWER": by_y[-1][0],
           "LEFT": by_x[0][0], "RIGHT": by_x[-1][0]}
    if len(by_y) >= 3:
        mid = by_y[len(by_y) // 2][0]
        out["MIDDLE"] = out["CENTER"] = out["CENTRE"] = mid
    return out


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
        if len(letters) < 2:
            bare = sorted(set(m.group(1) for m in BARE.finditer(txt)))
            # require the run to start at A and be contiguous, or it is just prose
            if len(bare) >= 2 and bare[0] == "A" and \
               bare == [chr(ord("A") + i) for i in range(len(bare))]:
                letters = bare
        words = set(m.group(0).upper() for m in POS.finditer(txt))
        positional = [w for a, b in OPPOSITES if a in words and b in words for w in (a, b)]
        if positional:
            for extra in ("MIDDLE", "CENTER", "CENTRE"):
                if extra in words:
                    positional.append(extra)
        if nimg >= 2 and not MNEMONIC.search(txt) and (len(letters) >= 2 or positional):
            kind = ("letters " + "/".join(letters)) if len(letters) >= 2 else ""
            if positional:
                kind = (kind + "  " if kind else "") + "position " + "/".join(positional)
            out.append((i, kind, nimg, re.sub(r"\s+", " ", txt)[:160],
                        resolve(picture_geometry(z, i)) if positional else {}))
    return out


def kept_count(course, slide_no):
    """How many extracted images from this slide survive in the repo.

    Extractors drop metafiles and small files, and the prune scripts keep a
    hand-written list. Optic neuritis shipped a brain MRI because slide 23's
    fundus photograph was an EMF that got dropped and then pruned, leaving one
    picture to stand for a three-part figure."""
    n = 0
    for d in glob.glob(os.path.join(ROOT, "*", "*-images")):
        if class_token(d) != course:
            continue
        for f in os.listdir(d):
            if re.search(r'(?:^|-)s0*%d_\d+\.' % slide_no, f):
                n += 1
    return n


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
        for sl, kind, nimg, txt, pos in rows:
            total += 1
            where = used.get((course, sl), [])
            in_use = bool(where)
            if not head:
                print("\n%s" % name)
                head = True
            mark = "  <-- SITE SHIPS AN IMAGE FROM THIS SLIDE" if in_use else ""
            if in_use:
                flagged += 1
            print("   slide %-4d %d pictures, %s%s" % (sl, nimg, kind, mark))
            print("      %s" % txt)
            if pos:
                seen, bits = set(), []
                for w in ("ABOVE", "BELOW", "LEFT", "RIGHT"):
                    k = pos.get(w)
                    if k and (w, k) not in seen:
                        seen.add((w, k))
                        bits.append("%s = _%d" % (w, k))
                print("      resolved by position: %s" % ",  ".join(bits))
            if in_use:
                print("      used by: %s" % ", ".join(sorted(set(where))))
                print("      CHECK the filenames: slide numbers repeat across a "
                      "course's decks,\n           so this can be another lecture's "
                      "slide %d rather than this one's." % sl)
                kept = kept_count(course, sl)
                if kept and kept < nimg:
                    print("      ONLY %d of the %d pictures on this slide were kept. If the "
                          "caption\n           describes a different one, the wrong picture is "
                          "shipped." % (kept, nimg))
    print("\n%d lettered slide(s) across the decks; %d of them are slides the site "
          "takes a picture from." % (total, flagged))
    if flagged:
        print("For those, the caption must come from the picture's OWN letter, and if the "
              "letters are stages of one condition, show more than one of them.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
