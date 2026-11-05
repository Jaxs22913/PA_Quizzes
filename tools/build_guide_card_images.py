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

THUMBNAILS (2026-10-26). A card shows its picture as a 92px-tall strip, but used to load the full
picture: 9.9 MB for the 55 cards, and a 2898 x 2321 photo decodes to 27 MB of memory. Each card now
loads a copy in guide-card-thumbs/ cut to what a strip can ever show: the middle band of the picture
(object-fit: cover keeps the middle, and the narrowest card, 190px in a fanned past-exam stack, shows a
band 2 times as wide as it is tall), at most 1200px wide (a 400px card on a 3x phone), as WebP, with any
transparency, color profile and camera rotation kept. About 2 MB for all 55. The file name carries a
hash of the picture and these settings, so a changed picture gets a new name; thumbnails no card uses
any more are deleted.
"""
import glob, hashlib, io, json, os, re, sys
from urllib.parse import unquote, quote
from PIL import Image, ImageOps

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
GUIDES = os.path.join(ROOT, "guides.html")

# Hand-picked, overriding whatever the scorer proposes. Keyed by the card's href path.
CURATED = {
    # Microbiology Exam 3: two plates that read at strip height (a scheme or tree would not).
    "Microbiology Exam 3/micro-exam-3-study-guide.html":
        "Microbiology Exam 3/micro-exam-3-study-guide-images/l14-s048-emb-agar.jpg",
    "Microbiology Exam 3/micro-exam-3-cram-sheet.html":
        "Microbiology Exam 3/micro-exam-3-study-guide-images/l14-s064-rainbow-agar.jpg",
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
    # 2026-11-05 first covers for the cardiology blocks: the scorer picked a troponin TEXT table (E4), a blurry
    # explanted pacemaker lead (E5) and an ECG with a web address burned along its foot (E5 Clin Med Pro).
    "Clinical Medicine and Surgery I Exam 4/cms-exam-4-study-guide.html":
        "Clinical Medicine and Surgery I Exam 4/cms-e4-images/l24-s010-coronary-anatomy.jpg",
    "Clinical Medicine and Surgery I Exam 5/cms-exam-5-study-guide.html":
        "Clinical Medicine and Surgery I Exam 5/cms-e5-images/l27-s006-vulnerable-plaque.jpg",
    "Clinical Medicine and Surgery I Exam 5/cms-exam-5-clin-med-pro-guide.html":
        "Clinical Medicine and Surgery I Exam 5/cms-e5-images/l30-s022-conduction-system.jpg",
    # Exam 6 (respiratory I): imaging, as Jaxon asked ("lung CTs that show findings we should look for"),
    # instead of the acid-base flowchart the scorer liked.
    "Clinical Medicine and Surgery I Exam 6/cms-exam-6-study-guide.html":
        "Clinical Medicine and Surgery I Exam 6/cms-e6-images/l38-s032-cavitary-cxr-ct.jpg",
    "Clinical Medicine and Surgery I Exam 6/cms-exam-6-cram-sheet.html":
        "Clinical Medicine and Surgery I Exam 6/cms-e6-images/l36-s032-cxr-flattened-diaphragm.jpg",
    "Clinical Medicine and Surgery I Exam 6/cms-exam-6-clin-med-pro-guide.html":
        "Clinical Medicine and Surgery I Exam 6/cms-e6-images/l37-s054-lung-abscess-cxr-ct.jpg",
}

# Cards that get NO picture even though their folder has some.
SKIP = {
    # No pictures of their own, and the folder's are the ear (tuning fork) and dermatology lectures: the
    # automatic pick put an air-versus-bone conduction diagram on the CARDIAC maneuvers card (2026-11-05).
    "Physical Diagnosis 2 Exam 1/pd2-cardiac-osce-maneuvers.html",
    "Physical Diagnosis 2 Exam 1/pd2-ent-osce-study-guide.html",
}

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
    "l24-s072a-troponin-supplement.jpg",   # a text table: unreadable as a strip
    "l32-s005-vegetation.jpg",             # blurry explanted lead with vegetation
    "l28-s095-low-voltage-ecg.jpg",        # web address burned along the foot
}

THUMBS = "guide-card-thumbs"
THUMB_ASPECT, THUMB_MAX_W, THUMB_Q = 2.0, 1200, 82


def thumb(src, card):
    """Path (from the repo root) of the strip-sized WebP copy of `src` for `card`, made if missing."""
    raw = open(src, "rb").read()
    tag = hashlib.sha1(raw + repr((THUMB_ASPECT, THUMB_MAX_W, THUMB_Q)).encode()).hexdigest()[:10]
    rel = "%s/%s-%s.webp" % (THUMBS, os.path.splitext(os.path.basename(card))[0], tag)
    out = os.path.join(ROOT, rel)
    if os.path.exists(out):
        return rel
    im = Image.open(io.BytesIO(raw))
    icc = im.info.get("icc_profile")
    im = ImageOps.exif_transpose(im)
    alpha = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
    im = im.convert("RGBA" if alpha else "RGB")
    if alpha and im.getchannel("A").getextrema()[0] == 255:
        im = im.convert("RGB")                     # an alpha channel with nothing see-through
    w, h = im.size
    if w / h < THUMB_ASPECT:                       # keep the middle band, the part a strip shows
        ch = round(w / THUMB_ASPECT)
        top = (h - ch) // 2
        im = im.crop((0, top, w, top + ch))
    w, h = im.size
    if w > THUMB_MAX_W:
        im = im.resize((THUMB_MAX_W, round(h * THUMB_MAX_W / w)), Image.LANCZOS)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    kw = {"quality": THUMB_Q, "method": 6}
    if icc:
        kw["icc_profile"] = icc
    im.save(out, "WEBP", **kw)
    return rel


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


KEPT = re.compile(r'<a class="guide-card[^"]*"[^>]*href="([^"]+)"[^>]*>\s*'
                  r'<span class="gc-thumb"><img src="([^"]+)"')


def main():
    src = open(GUIDES, encoding="utf-8").read()
    # A card that already shows a picture KEEPS it (2026-11-05). The scorer's picks depend on page order and on
    # which cards exist, so a full re-run after adding Exam 4-7 cards reshuffled 20 covers that were live and
    # already looked at, and 16 live covers were placed by hand outside this script. Only CURATED overrides a
    # kept cover; to re-pick one on purpose, delete its <span class="gc-thumb"> from guides.html first.
    kept = {unquote(h): unquote(t) for h, t in KEPT.findall(src)
            if os.path.exists(os.path.join(ROOT, unquote(t)))}
    src = THUMB.sub("", src)          # idempotent: drop any previous run's thumbs

    # The first class word decides the kind: "ref guide-card--listen" is a reference card too.
    cards = [((m.group(1).split() or ["guide"])[0], unquote(m.group(3)))
             for m in BLOCK.finditer(src)]
    guide_page = {}
    for cls, path in cards:
        if cls == "guide" and page_images(path):
            guide_page.setdefault(os.path.dirname(path), path)

    used, picks, skipped = set(), {}, []
    prev = {}
    try:
        prev = json.load(open(os.path.join(ROOT, "tools", "guide_card_images.json")))
    except (OSError, ValueError):
        pass
    for card in kept:                 # their pictures are taken, so a new card cannot duplicate them
        if card in prev:
            used.add(os.path.join(ROOT, prev[card]))
    for cls, path in cards:
        if path in SKIP:
            skipped.append((path, "explicitly skipped"))
            continue
        if path in CURATED:
            picks[path] = CURATED[path]
            used.add(CURATED[path])
            continue
        if path in kept:
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

    made = set()

    def inject(m):
        path = unquote(m.group(3))
        p = picks.get(path)
        if not p and path in kept:
            made.add(kept[path])
            return (m.group(0) + '<span class="gc-thumb"><img src="%s" alt="" '
                    'loading="lazy" decoding="async"></span>' % quote(kept[path]))
        if not p:
            return m.group(0)
        rel = quote(thumb(p, path))
        made.add(unquote(rel))
        return (m.group(0) + '<span class="gc-thumb"><img src="%s" alt="" '
                'loading="lazy" decoding="async"></span>' % rel)

    out = BLOCK.sub(inject, src)
    open(GUIDES, "w", encoding="utf-8").write(out)

    print("%d of %d cards show a picture (%d kept, %d newly picked or curated)"
          % (len(picks) + len([c for c in kept if c not in picks]), len(cards),
             len([c for c in kept if c not in picks]), len(picks)))
    for path, why in skipped:
        print("   no picture: %-52s %s" % (os.path.basename(path)[:52], why))
    for old in glob.glob(os.path.join(ROOT, THUMBS, "*.webp")):
        if os.path.relpath(old, ROOT) not in made:
            os.remove(old)
            print("   removed unused thumbnail", os.path.basename(old))
    json.dump({k: os.path.relpath(v, ROOT) for k, v in picks.items()},
              open(os.path.join(ROOT, "tools", "guide_card_images.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
