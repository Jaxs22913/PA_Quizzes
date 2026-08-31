#!/usr/bin/env python3
"""Put photographs of the disease processes into the CMS I Exam 2 study guide.

Jaxon, 2026-08-30: "for all the main guides for CMS add these sections like you
did for derm i really liked them." This is the ophthalmology counterpart of
add_guide_derm_images.py, and it follows the same three rules.

WHERE THE IMAGES COME FROM. Not from a fresh extraction. This reads the
generated ophthalmology comparison chart and reuses the exact image-to-condition
mapping already committed there, because that mapping has been audited at full
size one photograph at a time. Deriving from the chart rather than re-deriving
from the decks means the guide and the chart cannot drift apart, and a later
correction to one is a correction to both. It also costs zero new bytes: both
files sit in the same directory, so the guide points at
cms-ophtho-chart-images/ directly.

ATTRIBUTION TRAVELS. Four of these pictures are not from a slide -- they are
CC BY / public domain images with a named author and licence. The chart carries
that credit in its <span class="picite">, and it is copied through verbatim
rather than replaced with a slide number, because the repository is public and
dropping it would republish them unattributed.

LETTERED SLIDES. Jaxon, 2026-08-31: some slides carry several photographs
labelled A, B, C, and the text underneath explains each letter separately. The
caption for one of those pictures must come from ITS OWN letter, not from the
slide as a whole. Two captions here were wrong for exactly that reason before
this note existed:
  L10 slide 18 is "A. Blepharitis" and "B. Meibomitis" -- the shipped picture is
  A, so its caption may not borrow B's toothpaste-like meibomian secretion.
  L12 slide 45 is a four-stage series: A acute with haemorrhages, B acute with
  cotton wool spots, C chronic with disc elevation, D atrophic. One picture
  cannot stand for the condition, so A and C are both shown, each labelled.
tools/check_lettered_slides.py finds these slides so the next build sees them.

RUN ORDER. After build_cms_e2_guide.py and build_cms_ophtho_chart.py.
Idempotent: every block is fenced in <!--OPHTHOFIG--> markers and stripped
before re-inserting, so running twice is the same as running once.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2")
GUIDE = os.path.join(DIR, "cms-exam-2-study-guide.html")
CHART = os.path.join(DIR, "cms-ophtho-comparison-chart.html")

ROW = re.compile(
    r'<td class="pic">(?:<img src="cms-ophtho-chart-images/([^"]+)"[^>]*>'
    r'(?:<span class="picite">(.*?)</span>)?'
    r'|<span class="nopic">.*?</span>)</td>'
    r'<td class="nm"><b>(.*?)</b>', re.S)


def chart_images():
    """{condition name: (filename, citation)} for the rows that have a picture."""
    src = open(CHART, encoding="utf-8").read()
    out = {}
    for img, cite, name in ROW.findall(src):
        if not img:
            continue
        cite = " ".join(re.sub(r"\s+", " ", cite or "").split())
        # slide pictures cite "Slide N"; sourced ones carry author and licence,
        # which is copied through as-is
        out[name] = (img, cite)
    assert len(out) >= 30, "only parsed %d pictured rows -- chart markup changed?" % len(out)
    return out


# Which conditions illustrate which subsection, keyed by the h3's own id, in the
# teaching order of that subsection rather than the chart's slide order.
PLACEMENT = [
 ("e2l1-lids", ["Entropion", "Ectropion", "Dermatochalasis", "Xanthelasma",
                "Blepharitis / Meibomitis", "Chalazion", "Hordeolum (stye)"]),
 ("e2l1-lacrimal", ["Dacryoadenitis", "Dacryocystitis"]),
 ("e2l1-surface", ["Pinguecula", "Pterygium", "Subconjunctival haemorrhage", "Chemosis"]),
 ("e2l1-conjunctivitis", [
   "Allergic conjunctivitis", "Viral conjunctivitis", "Bacterial conjunctivitis",
   "Gonococcal conjunctivitis", "Chlamydial conjunctivitis &mdash; adult inclusion",
   "Chlamydial conjunctivitis &mdash; neonatal", "Trachoma", "Autoimmune conjunctivitis"]),
 ("e2l1-sclera", ["Episcleritis", "Scleritis"]),
 ("e2l1-cornea", ["Keratitis", "Herpes simplex keratitis", "Herpes zoster keratitis",
                  "Corneal ulcer"]),
 ("e2l1-uveitis", ["Anterior uveitis (iritis, iridocyclitis)",
                   "Posterior uveitis (choroiditis, retinitis)"]),
 ("e2l1-cellulitis", ["Pre-septal (periorbital) cellulitis",
                      "Post-septal (orbital) cellulitis"]),
 ("e2l2-nystagmus", ["Nystagmus"]),
 ("e2l2-pupils", ["Adie tonic pupil"]),
 ("e2l2-cn", ["Cranial nerve III palsy"]),
 ("e2l3-glaucoma", ["Acute angle-closure glaucoma", "Chronic open-angle glaucoma"]),
 ("e2l3-neuritis", ["Optic neuritis"]),
 ("e2l3-detachment", ["Retinal detachment"]),
 ("e2l3-papilledema", ["Papilledema"]),
 # ---- Lecture 13, Chronic Vision Loss & Tumors ----
 ("e2l4-amd", ["Age-related macular degeneration &mdash; dry",
               "Age-related macular degeneration &mdash; wet"]),
 ("e2l4-amblyopia", ["Amblyopia"]),
 ("e2l4-cataract", ["Cataract &mdash; nuclear", "Cataract &mdash; cortical",
                    "Cataract &mdash; pediatric"]),
 ("e2l4-retinoblastoma", ["Retinoblastoma"]),
 ("e2l4-melanoma", ["Uveal melanoma", "Iris nevus", "Conjunctival melanoma"]),
]

# Slide 20 carries BOTH systems at once: "Hordeolum. LEFT External hordeolum,
# RIGHT Internal hordeolum" and separately "A, B Chalazion". The shipped
# hordeolum picture is the RIGHT one, so it is the INTERNAL hordeolum pointing on
# the conjunctival surface -- not a stye at the lash line, which is what its
# caption used to claim. The chalazion picture is external lid swelling rather
# than a nodule everted into view. Both captions now describe their own
# photograph, and the tender / non-tender distinction the exam turns on is kept.
#
# A caption is a name plus a one-line "what you are looking at". Recognition is
# the skill being taught, so the caption says what to LOOK for rather than
# repeating the diagnosis the label already gives. Each is the finding the
# comparison chart names for that row, written as an instruction to the eye.
LOOK = {
 "Entropion": "Lid margin rolled IN, so the lashes sit against the globe",
 "Ectropion": "Lid margin rolled OUT, exposing the inner surface",
 "Dermatochalasis": "Excess folds of upper lid skin hanging over the lashes",
 "Xanthelasma": "Oval yellow plaques on the nasal side of the lid",
 "Blepharitis / Meibomitis": "Crusting and collarettes at the base of the lashes",
 "Chalazion": "Focal, NON-tender lid swelling built over days to weeks",
 "Hordeolum (stye)": "TENDER nodule &mdash; internal, pointing on the inner lid surface",
 "Dacryoadenitis": "Swelling of the outer third of the UPPER lid",
 "Dacryocystitis": "Swelling BELOW the medial canthal tendon, pus from the punctum",
 "Pinguecula": "Yellow nodule on the conjunctiva that STOPS at the limbus",
 "Pterygium": "Wing of tissue that has CROSSED onto the cornea",
 "Subconjunctival haemorrhage": "Flat sheet of blood under the conjunctiva, cornea clear",
 "Chemosis": "The conjunctiva itself swollen and ballooning",
 "Allergic conjunctivitis": "Cobblestone papillae under the lid, and no node",
 "Viral conjunctivitis": "Follicles plus watery discharge; the node is tender",
 "Bacterial conjunctivitis": "Papillae with thick yellow discharge gluing the lashes",
 "Gonococcal conjunctivitis": "Severe purulent discharge, hyperacute over hours",
 "Chlamydial conjunctivitis &mdash; adult inclusion": "Follicles persisting beyond a month",
 "Chlamydial conjunctivitis &mdash; neonatal": "Conjunctivitis in a neonate, days after birth",
 "Trachoma": "Upper lid follicles, then scarring that turns the lid in",
 "Autoimmune conjunctivitis": "Recurrent redness with scarring of the fornix",
 "Episcleritis": "Sectoral redness; the vessels move when swept",
 "Scleritis": "Deep violaceous hue; the vessels do NOT move",
 "Keratitis": "Corneal opacification with ciliary flush around the limbus",
 "Herpes simplex keratitis": "Branching dendrite with TERMINAL END BULBS on fluorescein",
 "Herpes zoster keratitis": "Pseudodendrite without end bulbs, in a dermatomal rash",
 "Corneal ulcer": "White corneal infiltrate with an overlying epithelial defect",
 "Anterior uveitis (iritis, iridocyclitis)": "Ciliary flush with an irregular pupil",
 "Posterior uveitis (choroiditis, retinitis)": "Vitreous haze obscuring the retinal detail",
 "Pre-septal (periorbital) cellulitis": "Lids swollen but THE EYE ITSELF IS WHITE",
 "Post-septal (orbital) cellulitis": "PROPTOSIS with restricted, painful eye movement",
 "Nystagmus": "Involuntary rhythmic oscillation, named for the FAST beat",
 "Adie tonic pupil": "The LARGER pupil, reacting poorly to light",
 "Cranial nerve III palsy": "Ptosis with the eye down and out, pupil dilated",
 "Acute angle-closure glaucoma": "HAZY cornea with a fixed mid-dilated pupil",
 "Chronic open-angle glaucoma": "OPTIC NERVE CUPPING, with the rim thinned",
 "Optic neuritis": "Disc swelling &mdash; but it looks like any swollen disc, so it is not diagnostic",
 "Retinal detachment": "Elevated grey retina thrown into folds",
 "Papilledema": "Acute: blurred disc margins with flame haemorrhages",
 # Lecture 13. Each picture was matched to its slide's own A/B/C/D or ABOVE/BELOW
 # label by geometry -- on the drusen slide the extraction order maps to labels
 # A, D, C, B, so picking by number would caption soft drusen as a scar.
 "Age-related macular degeneration &mdash; dry":
   "Soft drusen &mdash; large, pale, indistinct deposits at the macula",
 "Age-related macular degeneration &mdash; wet":
   "Haemorrhage from new choroidal vessels bleeding into the retina",
 "Amblyopia": "Occlusion objection &mdash; content until the GOOD eye is covered",
 "Cataract &mdash; nuclear": "The lens centre yellowed and dense",
 "Cataract &mdash; cortical": "Spokes running in from the lens edge",
 "Cataract &mdash; pediatric": "Polar cataract &mdash; a discrete opacity at the lens pole",
 "Retinoblastoma": "Leukocoria &mdash; one pupil red, the other white",
 "Uveal melanoma": "Choroidal melanoma &mdash; a dome of pigment under the retina",
 "Iris nevus": "Flat, under 3 mm, and no vessel of its own",
 "Conjunctival melanoma": "Raised and vascular, unlike the flat cystic nevus",
}

# Figures the chart cannot supply because it holds one row per condition while
# the slide teaches a series. Keyed by the condition they follow.
# (filename, citation, caption, label appended to the name)
EXTRA = {
 "Papilledema": [("l12-s045_3.jpg", "Slide 45",
                  "Chronic: disc elevation and blurred margins, no haemorrhages",
                  "Papilledema &mdash; chronic")],
 # Slide 23 is labelled ABOVE / MIDDLE / BELOW. The disc photograph is the
 # ophthalmoscopic finding; the FLAIR is the demyelination behind it, and the
 # slide's own point is that the disc alone is not diagnostic.
 "Optic neuritis": [("l12-s023_3.jpg", "Slide 23",
                     "Periventricular T2 FLAIR lesions &mdash; the demyelination behind it",
                     "Optic neuritis &mdash; the MRI")],
}

CSS = """
<style>
  .figgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(158px,1fr));
           gap:16px 14px;margin:10px 0 20px;padding:14px 14px 4px;border-radius:10px;
           background:var(--band,#f4f5fb)}
  .figgrid figure{margin:0;text-align:center;display:flex;flex-direction:column}
  .figgrid img{width:100%;height:132px;object-fit:contain;border-radius:6px;
               background:#fff;border:1px solid var(--rule,#d3d8ea)}
  .figgrid figcaption{margin-top:7px;font-size:12px;line-height:1.35;color:var(--soft)}
  .figgrid .fg-name{display:block;font-weight:700;color:var(--ink);font-size:12.5px;
                    margin-bottom:2px}
  .figgrid .fg-cite{display:block;font-size:10.5px;margin-top:3px;opacity:1;color:var(--soft)}
  .figgrid-h{font-size:12.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
             color:var(--soft);margin:18px 0 2px}
  @media (max-width:520px){.figgrid{grid-template-columns:repeat(auto-fill,minmax(132px,1fr))}
    .figgrid img{height:112px}}
  @media print{.figgrid{break-inside:auto;background:#f7f8fd}
    .figgrid figure{break-inside:avoid;page-break-inside:avoid}
    .figgrid img{break-inside:avoid}}
</style>
"""

FENCE_OPEN, FENCE_CLOSE = "<!--OPHTHOFIG-->", "<!--/OPHTHOFIG-->"


def strip_old(src):
    return re.sub(re.escape(FENCE_OPEN) + r".*?" + re.escape(FENCE_CLOSE), "", src, flags=re.S)


def fig(img, name, look, cite):
    plain = re.sub(r"<[^>]+>", "", name)
    return ('<figure><img src="cms-ophtho-chart-images/%s" loading="lazy" decoding="async" '
            'alt="%s &mdash; %s">'
            '<figcaption><span class="fg-name">%s</span>%s'
            '<span class="fg-cite">%s</span></figcaption></figure>'
            % (img, H.escape(plain), H.escape(re.sub(r"<[^>]+>", "", look)), name, look, cite))


def build_strip(names, imgs):
    figs = []
    for n in names:
        if n not in imgs:
            continue
        img, cite = imgs[n]
        look = LOOK[n]
        label = {"Papilledema": "Papilledema &mdash; acute",
                 "Optic neuritis": "Optic neuritis &mdash; the disc"}.get(n, n)
        figs.append(fig(img, label, look, cite))
        for x_img, x_cite, x_look, x_name in EXTRA.get(n, []):
            figs.append(fig(x_img, x_name, x_look, x_cite))
    if not figs:
        return ""
    return ('%s\n  <p class="figgrid-h">What these look like</p>\n  <div class="figgrid">%s</div>\n  %s'
            % (FENCE_OPEN, "".join(figs), FENCE_CLOSE))


def main():
    imgs = chart_images()
    missing = [n for _, ns in PLACEMENT for n in ns if n not in imgs]
    assert not missing, "no chart picture for: %s" % missing
    nolook = [n for _, ns in PLACEMENT for n in ns if n not in LOOK]
    assert not nolook, "no caption written for: %s" % nolook

    src = strip_old(open(GUIDE, encoding="utf-8").read())
    if "figgrid" not in src:
        src = src.replace("</head>", CSS + "</head>", 1)

    placed = 0
    for hid, names in PLACEMENT:
        m = re.search(r'<h3[^>]*id="%s"[^>]*>.*?</h3>' % re.escape(hid), src, re.S)
        assert m, "no h3 with id %r in the guide" % hid
        strip = build_strip(names, imgs)
        if not strip:
            continue
        src = src[:m.end()] + "\n  " + strip + src[m.end():]
        placed += sum(1 for n in names if n in imgs)

    # the strips must land in the body, never inside the table of contents
    for m in re.finditer(re.escape(FENCE_OPEN), src):
        nav = src.rfind("<nav", 0, m.start())
        assert nav == -1 or src.find("</nav>", nav) < m.start(), \
            "a figure strip landed inside the table of contents"

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("wrote %s" % os.path.basename(GUIDE))
    print("  %d photographs across %d sections" % (placed, len(PLACEMENT)))
    ext = sum(1 for n, (i, c) in imgs.items() if i.startswith("ext-"))
    print("  %d of the chart's pictures are sourced outside the deck; their credit is carried through" % ext)


if __name__ == "__main__":
    main()
