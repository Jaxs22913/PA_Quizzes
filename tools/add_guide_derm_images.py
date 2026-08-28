#!/usr/bin/env python3
"""Put photographs of the disease processes into the CMS I Exam 1 study guide.

Jaxon, 2026-08-20: "in the guides like CMS you should include images of the
disease processes." A dermatology guide without pictures is the wrong shape --
half of what the exam asks is recognition, and prose cannot teach that.

WHERE THE IMAGES COME FROM. Not from a fresh extraction. This reads the
generated dermatology comparison chart and reuses the exact image-to-condition
mapping already committed there, because that mapping has been audited at full
size, one photograph at a time, after three wrong ones shipped on 2026-08-19
(one was a dog). Deriving from the chart rather than re-deriving from the decks
means the guide and the chart cannot drift apart, and a future correction to one
is a correction to both. It also means zero new bytes -- both files sit in the
same directory, so the guide points at cms-derm-chart-images/ directly.

RUN ORDER. After build_cms_guide.py and build_cms_guide_derm.py, and after
build_cms_derm_chart.py. Idempotent: every block it writes is fenced in
<!--DERMFIG--> markers and stripped before re-inserting, so running twice is the
same as running once.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
CHART = os.path.join(DIR, "cms-derm-comparison-chart.html")
IMGDIR = os.path.join(DIR, "cms-derm-chart-images")

# ---------------------------------------------------------------- the mapping
# The trailing <span class="deck"> is captured, not discarded, because it is the
# only place the ATTRIBUTION lives for the pictures that did not come from a
# slide. Those are CC BY / CC BY-SA and the credit has to travel with the image
# into the guide -- dropping it here would republish them unattributed.
ROW = re.compile(
    r'<tr><td class="pic">(?:<figure><img src="cms-derm-chart-images/([^"]+)"[^>]*>'
    r'<figcaption>(.*?)<span class="deck">(.*?)</span></figcaption></figure>'
    r'|<div class="nopic">.*?</div>)</td><td class="name">(.*?)</td>', re.S)


def chart_images():
    """{condition name: (image filename, 'Lecture N &middot; Slide M')}."""
    src = open(CHART, encoding="utf-8").read()
    out = {}
    for img, cite, deck, name in ROW.findall(src):
        # slide pictures cite "Lecture N - Slide M"; sourced pictures cite their
        # author, source and licence instead, carried over verbatim with its link
        if img.startswith("ext-"):
            cite = deck
        # keep the "also Lecture N" badge text -- it is the only thing that
        # tells the two solar lentigo rows apart
        name = " ".join(re.sub(r"<[^>]+>", " ", name).split())
        # Actinic keratosis genuinely occupies two chart rows, Lecture 3 and
        # Lecture 9, and unlike solar lentigo it carries no "also Lecture N"
        # badge to tell them apart. Both rows hold a real actinic keratosis
        # photograph, so the first is kept rather than failing the run -- this
        # assert had quietly made the whole script unrunnable, which is why the
        # guide's pictures had stopped tracking the chart.
        if name in out:
            assert out[name] is not None and img, \
                "duplicate chart row %r and one of them has no image" % name
            continue
        out[name] = (img, cite) if img else None
    assert len(out) >= 80, "only parsed %d chart rows -- markup changed?" % len(out)
    return out


# Which conditions illustrate which subsection of the guide, keyed by the h3's
# own id. The order here is the order they appear in the strip, and it is the
# teaching order of the subsection rather than the chart's slide order.
PLACEMENT = [
 ("gd1-eczema", [
   "Atopic dermatitis", "Irritant contact dermatitis", "Allergic contact dermatitis",
   "Seborrheic dermatitis", "Nummular eczema", "Dyshidrotic eczema", "Stasis dermatitis",
   "Diaper dermatitis", "Perioral dermatitis", "Xeroderma (xerosis)"]),
 ("gd1-bullous", ["Bullous pemphigoid", "Pemphigus (vulgaris)"]),
 ("gd1-papulo", [
   "Psoriasis &mdash; plaque", "Psoriasis &mdash; guttate", "Psoriasis &mdash; pustular",
   "Pityriasis rosea", "Lichen planus", "Lichen simplex chronicus"]),
 ("gd1-alopecia", ["Alopecia areata", "Androgenetic alopecia"]),
 ("gd2-reactive", [
   "Erythema multiforme", "Urticaria", "Erythema nodosum", "Granuloma annulare",
   "Pyoderma gangrenosum", "Acne rosacea", "Hyperhidrosis", "Dermatitis herpetiformis",
   "Acanthosis nigricans", "Epidermolysis bullosa"]),
 ("gd2-sjsten", ["Stevens-Johnson syndrome", "Toxic epidermal necrolysis"]),
 ("gd2-photo", [
   "Sunburn", "Drug-induced photosensitivity", "Polymorphous light eruption",
   "Dermatoheliosis (photoaging)", "Actinic keratosis", "Solar lentigo also Lecture 8",
   "Photodermatitis (phytophotodermatitis)"]),
 ("cbi-acne", ["Acne vulgaris"]),
 ("cbi-follicular", [
   "Folliculitis", "Pseudomonas (&ldquo;hot tub&rdquo;) folliculitis",
   "Pseudofolliculitis barbae", "Furuncle", "Carbuncle", "Hidradenitis suppurativa",
   "Erythrasma"]),
 ("cbi-spreading", [
   "Impetigo &mdash; non-bullous", "Impetigo &mdash; bullous", "Ecthyma", "Erysipelas",
   "Cellulitis", "Abscess"]),
 ("cbi-nailnec", ["Acute paronychia", "Chronic paronychia", "Necrotizing fasciitis"]),
 ("di-scabies", [
   "Scabies", "Crusted (hyperkeratotic) scabies", "Pediculosis capitis (head lice)",
   "Pediculosis corporis (body lice)", "Pediculosis pubis (crabs)"]),
 ("di-bites", ["Bedbugs", "Tungiasis (fleas)", "Caterpillars (lepidopterism)"]),
 ("di-larva", ["Cutaneous larva migrans", "Cercarial dermatitis (swimmer's itch)"]),
 ("di-spiders", ["Black widow spider", "Brown recluse spider", "Hobo spider"]),
 ("di-ticks", ["Lyme disease", "Rocky Mountain spotted fever"]),
 ("psl-flat", ["Ephelides (freckles)", "Lentigines", "Solar lentigo also Lecture 3"]),
 ("psl-keratoses", ["Seborrheic keratosis", "Dermatosis papulosa nigrans"]),
 ("psl-vitiligo", ["Vitiligo"]),
 ("psl-naevi", [
   "Common acquired melanocytic naevus (mole)", "Congenital melanocytic naevus",
   "Naevus spilus", "Blue naevus", "Spitz naevus", "Pigmented spindle cell naevus (Reed)",
   "Dysplastic melanocytic naevus"]),
]

# A caption is a name plus a one-line "what you are looking at". Recognition is
# the skill being taught, so the caption says what to LOOK for rather than
# repeating the diagnosis the label already gives.
LOOK = {
 "Atopic dermatitis": "Ill-defined erythema in a flexure, excoriated and lichenified from scratching",
 "Irritant contact dermatitis": "Erythema confined to the exposed surface, no spread beyond it",
 "Allergic contact dermatitis": "Sharp geometric margins in the shape of the contactant",
 "Seborrheic dermatitis": "Greasy yellow scale on erythema in a sebum-rich site",
 "Nummular eczema": "Discrete coin-shaped plaques with a clear edge",
 "Dyshidrotic eczema": "Deep-seated tapioca-like vesicles along the sides of the fingers",
 "Stasis dermatitis": "Gaiter-area pigmentation and oedema, bilateral",
 "Diaper dermatitis": "Involves convex surfaces and spares the folds",
 "Perioral dermatitis": "Papules around the mouth that spare the vermilion border",
 "Xeroderma (xerosis)": "Dry cracked plating of the skin, worst on shins",
 "Bullous pemphigoid": "Tense bullae on an urticarial base; they do not rupture easily",
 "Pemphigus (vulgaris)": "Flaccid bullae and erosions, mucosa involved",
 "Psoriasis &mdash; plaque": "Sharply marginated plaques with thick silvery scale on extensors",
 "Psoriasis &mdash; guttate": "Small drop-like papules scattered over the trunk",
 "Psoriasis &mdash; pustular": "Sterile pustules on an erythematous base",
 "Pityriasis rosea": "Herald patch, then a scaly eruption along skin lines",
 "Lichen planus": "Flat-topped violaceous polygonal papules",
 "Lichen simplex chronicus": "Thickened skin with exaggerated markings from chronic rubbing",
 "Alopecia areata": "Smooth round patch of loss with no scarring or scale",
 "Androgenetic alopecia": "Patterned thinning, temples and vertex in men, part width in women",
 "Erythema multiforme": "Target lesions with three zones, acral first",
 "Urticaria": "Transient oedematous wheals; each one moves within a day",
 "Erythema nodosum": "Tender red nodules on the shins that never ulcerate",
 "Granuloma annulare": "Ring of firm papules with an intact, non-scaly centre",
 "Pyoderma gangrenosum": "Ulcer with a violaceous undermined border",
 "Acne rosacea": "Central facial erythema with telangiectasia, no comedones",
 "Hyperhidrosis": "Visible sweat beyond thermal need, focal and symmetric",
 "Dermatitis herpetiformis": "Grouped intensely itchy vesicles on extensor surfaces",
 "Acanthosis nigricans": "Velvety thickened hyperpigmentation in a flexure",
 "Epidermolysis bullosa": "Blistering and erosions at sites of mechanical friction",
 "Stevens-Johnson syndrome": "Dusky macules and mucosal erosion, under a tenth of the surface",
 "Toxic epidermal necrolysis": "Sheet-like detachment of the epidermis, over three tenths",
 "Sunburn": "Erythema sharply limited to exposed skin, tender to touch",
 "Drug-induced photosensitivity": "Exaggerated burn in exposed areas after a drug",
 "Polymorphous light eruption": "Itchy papules appearing hours to days after the first strong sun",
 "Dermatoheliosis (photoaging)": "Deep furrowing and yellow leathering of chronically exposed skin",
 "Actinic keratosis": "Rough sandpaper texture, easier to feel than to see",
 "Solar lentigo also Lecture 8": "Uniform tan macule on chronically exposed skin",
 "Acne vulgaris": "Comedones alongside papules and pustules in sebaceous areas",
 "Folliculitis": "Pustules centred on hair follicles",
 "Pseudomonas (&ldquo;hot tub&rdquo;) folliculitis": "Follicular pustules under the swimsuit area after a tub",
 "Pseudofolliculitis barbae": "Papules in the beard from hairs re-entering the skin",
 "Furuncle": "One tender nodule around a single follicle",
 "Carbuncle": "Several furuncles coalescing, draining from multiple points",
 "Hidradenitis suppurativa": "Nodules, sinus tracts and scarring in apocrine-bearing skin",
 "Erythrasma": "Well-demarcated brown patch in a fold; coral-red under Wood's lamp",
 "Impetigo &mdash; non-bullous": "Honey-coloured crust on a superficial erosion",
 "Impetigo &mdash; bullous": "Flaccid bullae leaving a collarette of scale",
 "Ecthyma": "Punched-out ulcer under the crust, deeper than impetigo",
 "Erysipelas": "Raised, sharply demarcated bright erythema",
 "Cellulitis": "Erythema with an indistinct border, warm and tender",
 "Abscess": "Fluctuant collection, often with a pointing head",
 "Acute paronychia": "Painful erythematous swelling of one nail fold",
 "Chronic paronychia": "Retracted cuticle and nail dystrophy over months",
 "Necrotizing fasciitis": "Skin changes that lag far behind the pain, with dusky discolouration",
 "Scabies": "Burrows in web spaces and wrists, itch worst at night",
 "Crusted (hyperkeratotic) scabies": "Thick hyperkeratotic crusting, enormous mite burden",
 "Pediculosis capitis (head lice)": "Nits cemented to hair shafts near the scalp",
 "Pediculosis corporis (body lice)": "Excoriations on the trunk; the louse lives in clothing",
 "Pediculosis pubis (crabs)": "Bite macules scattered over the lower abdomen and coarse hair",
 "Bedbugs": "Grouped bites on skin left uncovered overnight, classically in a line",
 "Tungiasis (fleas)": "Papule with a central black dot, usually on the foot",
 "Caterpillars (lepidopterism)": "Linear urticarial streaks where the hairs brushed the skin",
 "Cutaneous larva migrans": "Serpiginous raised track that advances day to day",
 "Cercarial dermatitis (swimmer's itch)": "Itchy papules on skin that was uncovered in the water",
 "Black widow spider": "The slide shows the spider: glossy black, red hourglass underneath",
 "Brown recluse spider": "Red, white and blue lesion progressing to a necrotic eschar",
 "Hobo spider": "The slide shows the spider: brown, and with no violin on its back",
 "Lyme disease": "Erythema migrans: an expanding red patch, often clearing centrally",
 "Rocky Mountain spotted fever": "Rash starting at wrists and ankles and moving inwards, palms and soles",
 "Ephelides (freckles)": "Small tan macules that darken with sun and fade without it",
 "Lentigines": "Uniform brown macules that do not fade in winter",
 "Solar lentigo also Lecture 3": "Larger tan patch on chronically exposed skin",
 "Seborrheic keratosis": "Waxy stuck-on plaque with visible follicular plugging",
 "Dermatosis papulosa nigrans": "Small dark papules on the malar cheeks, skin of colour",
 "Vitiligo": "Sharply marginated depigmented, not merely hypopigmented, patches",
 "Common acquired melanocytic naevus (mole)": "Small, symmetric, one uniform colour, stable",
 "Congenital melanocytic naevus": "Present at birth, often large and hair-bearing",
 "Naevus spilus": "Tan patch with darker speckles inside it",
 "Blue naevus": "Blue-grey papule, colour from pigment deep in the dermis",
 "Spitz naevus": "Pink to red-brown dome, typically in a child, rapid onset",
 "Pigmented spindle cell naevus (Reed)": "Very dark, sharply circumscribed, symmetric",
 "Dysplastic melanocytic naevus": "Larger than 6mm with irregular borders and mixed colours",
 "Photodermatitis (phytophotodermatitis)": "Bizarre streaks and drips where plant sap met sun",
}

CSS = """
  /* Disease photograph strips (added 2026-08-20). Images are shared with the
     dermatology comparison chart -- same directory, same files, no duplicates.
     Images here are eager, never lazy: an image that never scrolled into view
     is absent from Download as PDF, which cost 74 of 84 photographs on the
     chart before it was caught. */
  .figgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(158px,1fr));
    gap:12px;margin:16px 0;padding:14px;background:#f2e9eb;border-radius:10px;
    border:1px solid var(--line)}
  .figgrid figure{margin:0;text-align:center;display:flex;flex-direction:column}
  .figgrid img{width:100%;height:132px;object-fit:contain;border-radius:6px;
    background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.1)}
  .figgrid .fg-nopic{width:100%;height:132px;border-radius:6px;background:#fff;
    border:1px dashed var(--line);display:flex;align-items:center;
    justify-content:center;font-size:11.5px;color:var(--soft);padding:8px;
    line-height:1.35;box-sizing:border-box}
  .figgrid figcaption{margin-top:7px;font-size:12px;line-height:1.35;color:var(--soft)}
  .figgrid .fg-name{display:block;font-weight:700;color:var(--ink);font-size:12.5px;
    margin-bottom:2px}
  .figgrid .fg-cite{display:block;font-size:10.5px;margin-top:3px;opacity:1;color:var(--soft)}
  .figgrid-h{font-size:12.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
    color:var(--soft);margin:0 0 4px}
  @media (max-width:520px){.figgrid{grid-template-columns:repeat(auto-fill,minmax(132px,1fr))}
    .figgrid img,.figgrid .fg-nopic{height:112px}}
  /* The GRID must be allowed to break -- a ten-condition strip is taller than a
     page, so `break-inside:avoid` on the grid cannot be honoured and Chrome
     splits it through the middle of a figure instead, clipping the photograph
     and orphaning its caption. Let the grid fragment between rows and protect
     the individual figure, which always fits. */
  @media print{.figgrid{break-inside:auto;background:#f7f2f3}
    .figgrid figure{break-inside:avoid;page-break-inside:avoid}
    .figgrid img,.figgrid .fg-nopic{break-inside:avoid}}
"""

FENCE_OPEN, FENCE_CLOSE = "<!--DERMFIG-->", "<!--/DERMFIG-->"


def strip_old(src):
    return re.sub(re.escape(FENCE_OPEN) + r".*?" + re.escape(FENCE_CLOSE), "", src, flags=re.S)


def build_strip(names, imgs):
    figs = []
    for n in names:
        entry = imgs[n]
        label = n.replace(" also Lecture 8", "").replace(" also Lecture 3", "")
        look = LOOK[n]
        if entry is None:
            body = ('<div class="fg-nopic">No image of this in the deck</div>')
            cite = ""
        else:
            fn, c = entry
            body = ('<img src="cms-derm-chart-images/%s" decoding="async" alt="%s &mdash; %s">'
                    % (fn, H.escape(re.sub(r"<[^>]+>", "", label)),
                       H.escape(look.replace("&mdash;", "-"))))
            cite = '<span class="fg-cite">%s</span>' % c
        figs.append('<figure>%s<figcaption><span class="fg-name">%s</span>%s%s</figcaption></figure>'
                    % (body, label, look, cite))
    return ('%s\n  <p class="figgrid-h">What these look like</p>\n  <div class="figgrid">%s</div>\n  %s'
            % (FENCE_OPEN, "".join(figs), FENCE_CLOSE))


def main():
    imgs = chart_images()
    src = strip_old(open(GUIDE, encoding="utf-8").read())

    used, missing = [], []
    for _id, names in PLACEMENT:
        for n in names:
            if n not in imgs:
                missing.append(n)
            used.append(n)
    assert not missing, "condition not in the chart: %r" % missing
    assert len(used) == len(set(used)), "a condition is placed in two subsections"
    unplaced = [n for n in imgs if n not in set(used)]
    assert not unplaced, "chart condition never reaches the guide: %r" % unplaced

    n_ins = 0
    for anchor, names in PLACEMENT:
        i = src.find('id="%s"' % anchor)
        assert i > 0, "no subsection with id %r" % anchor
        # the subsection runs to the next h3/h2, whichever comes first
        nxt = min([x for x in (src.find("<h3", i + 1), src.find("<h2", i + 1)) if x > 0] or [len(src)])
        region = src[i:nxt]
        # after the first table if the subsection has one, otherwise at the end
        at = region.find("</table>")
        at = i + at + len("</table>") if at >= 0 else nxt
        strip = build_strip(names, imgs)
        src = src[:at] + "\n\n  " + strip + src[at:]
        n_ins += 1

    if ".figgrid{" not in src:
        src = src.replace("</style>", CSS + "</style>", 1)

    # Check the IMG TAGS, not the raw text: the CSS comment below explains the
    # rule and so contains the very string a naive substring test would find.
    assert not [t for t in re.findall(r"<img\b[^>]*>", src) if "lazy" in t], \
        "lazy images will not survive Download as PDF"
    assert src.count(FENCE_OPEN) == src.count(FENCE_CLOSE) == n_ins
    for fn in re.findall(r'src="cms-derm-chart-images/([^"]+)"', src):
        assert os.path.exists(os.path.join(IMGDIR, fn)), "missing image file %s" % fn

    open(GUIDE, "w", encoding="utf-8").write(src)
    n_img = len(re.findall(r'src="cms-derm-chart-images/', src))
    print("%d photograph strips inserted, %d images, %d conditions"
          % (n_ins, n_img, len(used)))
    print("no new bytes: images are the chart's, referenced in place")


if __name__ == "__main__":
    main()
