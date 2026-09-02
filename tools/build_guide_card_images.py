#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Put a cover picture on the guides.html cards.

Jaxon, 2026-09-02: "guides.html is a wall of text cards. You now own hundreds
of audited clinical photographs — one representative image per card would
transform that page."

THE RULE, arrived at after auditing an automatic pick for all 59 cards:

  Study Guide and Cram Sheet cards get a picture from their own exam's
  folder. Quick Reference cards get one ONLY if that reference page contains
  pictures itself.

That last clause is the important one. The three ENT / cardiac / pulmonary
OSCE sheets have no pictures of their own, and the only images in their folder
are dermatological -- so an automatic pick put ACNE on the cardiac OSCE card.
Same for Pharmacology's four reference sheets and Anatomy Exam 3's four. A
missing picture is fine; a wrong one is worse than none.

PICKS ARE NOT AUTOMATIC EITHER. The scorer below only proposes; every card was
looked at as a rendered 16:9 crop before shipping, and the CURATED table
overrides it wherever the proposal was bad. Three kinds of bad came up:

  * Front-door images that were clinically fine but unpleasant as cover art --
    neonatal gonococcal conjunctivitis on the ophthalmology guide, a pyoderma
    gangrenosum ulcer on the dermatology one. A guide index is not the place.
  * Pictures nobody can read at 92px tall -- a full antibiotic classification
    tree, a dense inflammation cascade.
  * Duplicates. Pharmacology has six cards and its folder has six usable
    images, so the last card fell through to a picture already used.

Run after adding a guide, a cram sheet or a new images folder; rewrites the
block of <span class="gc-thumb"> elements inside guides.html in place.
"""
import glob, json, os, re, sys
from urllib.parse import unquote, quote
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
GUIDES = os.path.join(ROOT, "guides.html")

# Hand-picked, overriding whatever the scorer proposes. Keyed by the card's href path.
CURATED = {
    # Clean and unmistakable, instead of the neonatal gonococcal discharge.
    "Clinical Medicine and Surgery I Exam 2/cms-exam-2-study-guide.html":
        "Clinical Medicine and Surgery I Exam 2/cms-ophtho-chart-images/l12-s028_1.jpg",
    "Clinical Medicine and Surgery I Exam 2/cms-exam-2-cram-sheet.html":
        "Clinical Medicine and Surgery I Exam 2/cms-ophtho-chart-images/l13-s037_1.jpg",
    "Clinical Medicine and Surgery I Exam 2/cms-ophtho-comparison-chart.html":
        "Clinical Medicine and Surgery I Exam 2/cms-ophtho-chart-images/s016_1.jpg",
    # Tinea corporis instead of the pyoderma gangrenosum ulcer.
    "Clinical Medicine and Surgery I Exam 1/cms-exam-1-study-guide.html":
        "Clinical Medicine and Surgery I Exam 1/cms-derm-chart-images/l6_s024_2.jpg",
    "Clinical Medicine and Surgery I Exam 1/cms-exam-1-cram-sheet.html":
        "Clinical Medicine and Surgery I Exam 1/cms-derm-chart-images/l8_s017_2.jpg",
    # Full-bleed. The cherry-angioma picture the scorer liked has hard white
    # bands baked down both sides, and object-fit:cover cannot crop those away
    # on a portrait source -- the card ended up photo-in-a-box.
    "Clinical Medicine and Surgery I Exam 1/cms-derm-comparison-chart.html":
        "Clinical Medicine and Surgery I Exam 1/cms-derm-chart-images/l6_s076_1.jpg",
    # The layers diagram reads far better small than a close-up of excoriation.
    "Physical Diagnosis 2 Exam 1/pd2-exam-1-study-guide.html":
        "Physical Diagnosis 2 Exam 1/pd2-exam-1-study-guide-images/01-skin-layers.jpg",
    # Was a duplicate of the study guide's picture -- only six images, six cards.
    "Pharmacology I Exam 1/pharm-exam-1-cram-sheet.html":
        "Pharmacology I Exam 1/pharm-exam-1-study-guide-images/004.png",
}

# Cards that get NO picture even though their folder has some.
SKIP = set()

# Never cover art. All of these are perfectly good teaching pictures and stay
# in the guides and charts -- they are just not what a study-aids index should
# open with, and excluding them by NAME rather than by card stops the problem
# migrating: curating the dermatology guide away from the pyoderma ulcer simply
# handed that ulcer to the cram sheet card next to it.
EXCLUDE = {
    "l3_s056_2.jpg",                       # pyoderma gangrenosum, ulcerated
    "l3_s081_2.jpg", "l3_s086_1.jpg",      # Stevens-Johnson, toxic epidermal necrolysis
    "l4_s124_2.jpg",                       # necrotising fasciitis
    "l9_s062_4.jpg",                       # Kaposi sarcoma, intraoral
    "ext-gonococcal-conjunctivitis.jpg",   # neonatal purulent discharge
    "l6_s103_1.jpg",                       # herpes zoster ophthalmicus, crusted
    "l14-s017_pos1.jpg", "l14-s029_pos1.jpg",  # globe rupture, lid laceration
}

BLOCK = re.compile(r'<a class="guide-card([^"]*)"([^>]*)href="([^"]+)"([^>]*)>(\s*)')
THUMB = re.compile(r'\s*<span class="gc-thumb"><img[^>]*></span>')


def page_images(path):
    folder = os.path.dirname(path)
    out = []
    if not os.path.exists(path):
        return out
    for m in re.finditer(r'<img[^>]+src="([^"]+)"', open(path, encoding="utf-8").read()):
        src = m.group(1)
        if src.startswith(("data:", "http")):
            continue
        full = os.path.normpath(os.path.join(folder, src))
        if os.path.exists(full) and full.lower().endswith((".jpg", ".jpeg", ".png")):
            out.append(full)
    seen = set()
    return [i for i in out if not (i in seen or seen.add(i))]


def folder_images(folder):
    out = []
    for d in sorted(glob.glob(glob.escape(folder) + "/*")):
        if os.path.isdir(d):
            out += [os.path.join(d, f) for f in sorted(os.listdir(d))
                    if f.lower().endswith((".jpg", ".jpeg", ".png"))]
    return out


def shape(p):
    """Usable as a wide cover strip?"""
    try:
        w, h = Image.open(p).size
    except Exception:
        return None
    if min(w, h) < 180:
        return None
    ar = w / h
    return (w, h, ar) if 0.5 <= ar <= 2.8 else None


def main():
    src = open(GUIDES, encoding="utf-8").read()
    src = THUMB.sub("", src)          # idempotent: drop any previous run's thumbs

    cards = [(m.group(1).strip() or "guide", unquote(m.group(3)))
             for m in BLOCK.finditer(src)]
    guide_page = {}
    for cls, path in cards:
        if cls == "guide" and page_images(path):
            guide_page.setdefault(os.path.dirname(path), path)

    used, picks, skipped = set(), {}, []
    for cls, path in cards:
        if path in SKIP:
            skipped.append((path, "explicitly skipped"))
            continue
        if path in CURATED:
            picks[path] = CURATED[path]
            used.add(CURATED[path])
            continue
        own = page_images(path)
        # A reference sheet with no pictures of its own gets none: the only
        # images near it belong to a different topic.
        if cls == "ref" and not own:
            skipped.append((path, "reference sheet with no pictures of its own"))
            continue
        cands = own or page_images(guide_page.get(os.path.dirname(path), "")) \
            or folder_images(os.path.dirname(path))
        scored = []
        for i, p in enumerate(cands):
            if os.path.basename(p) in EXCLUDE:
                continue
            s = shape(p)
            if not s:
                continue
            w, h, ar = s
            scored.append((-abs(ar - 1.6) * 2 + min(w * h, 810000) / 810000
                           + (0.25 if i else 0), p))
        scored.sort(reverse=True)
        pick = next((p for _, p in scored if p not in used), None)
        if pick:
            picks[path] = pick
            used.add(pick)
        else:
            skipped.append((path, "no unused image left in its folder"))

    def inject(m):
        path = unquote(m.group(3))
        p = picks.get(path)
        if not p:
            return m.group(0)
        rel = quote(os.path.relpath(p, ROOT))
        return (m.group(0) + '<span class="gc-thumb"><img src="%s" alt="" '
                'loading="lazy" decoding="async"></span>' % rel)

    out = BLOCK.sub(inject, src)
    open(GUIDES, "w", encoding="utf-8").write(out)

    print("%d of %d cards get a picture" % (len(picks), len(cards)))
    for path, why in skipped:
        print("   no picture: %-52s %s" % (os.path.basename(path)[:52], why))
    json.dump({k: os.path.relpath(v, ROOT) for k, v in picks.items()},
              open(os.path.join(ROOT, "tools", "guide_card_images.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
