#!/usr/bin/env python3
"""Extract the Dermatology lecture's figures for the Physical Diagnosis 2 guide.

Slide images are cleared for use provided the slide is cited (Jaxon, 2026-08-18:
the decks come from the school and the class may use them on that condition).
Every figure that ships therefore carries its deck and slide number in the
caption, and the third-party marks baked into some of these images -- Fitzpatrick's
Color Atlas, Current Medical Diagnosis & Treatment, Mayo Foundation, Galderma,
Medscape, the National Pressure Ulcer Advisory Panel, University of Wisconsin --
are left visible rather than cropped out.

Each figure in FIGURES was viewed before being captioned; nothing here is
described from the surrounding slide text. Where a slide offered more than one
image of the same finding the clearest was taken, with one deliberate exception:
Kaposi's sarcoma, where slide 74 has a full-face photograph of an identifiable
patient and a skin-only one. The skin-only image ships. That is a patient
privacy judgement, not a licensing one, and it stands independently.

Images are capped at 900 px wide and re-encoded as JPEG, which takes the set
from 8.0 MB to something a study guide can actually load.
"""
import os, shutil
from PIL import Image

SRC = "/private/tmp/claude-501/-Users-jaxonluke/8623a091-045a-42b8-8052-ca7d2eb04188/scratchpad/derm_imgs"
OUT = "/Users/jaxonluke/Developer/PA_Quizzes/Physical Diagnosis 2 Exam 1/pd2-exam-1-study-guide-images"
MAXW = 900

# (source file, output stem, slide, alt text, caption)
FIGURES = [
 ("s003_1.png", "skin-layers", 3,
  "Cutaway block diagram of skin showing three labelled layers from the surface downward: epidermis, dermis containing hair follicles and a network of red and blue vessels, and hypodermis composed of yellow fat lobules.",
  "The three layers, and why the morphology definitions care about them. A lesion confined to the <b>epidermis</b> is superficial &mdash; that is an erosion, which stays moist and does not bleed. Reach the <b>dermis</b>, where the vessels run, and it can bleed and scar &mdash; that is an ulcer. A nodule sits deeper in the dermis than a papule, and a cyst may sit deeper still, in the subcutaneous layer."),

 ("s032_1.jpg", "macule-freckles", 32,
  "Face of a young child with numerous small light-brown flat spots scattered across both cheeks and the bridge of the nose.",
  "<b>Macules</b> &mdash; freckles. Circumscribed, flat discoloration under one centimetre. Run a finger across them and you feel nothing; that is what makes them macules rather than papules."),

 ("s033_1.jpg", "patch-cafe-au-lait", 33,
  "Back of a young child with two flat light-brown areas of uniform colour, one on the left mid-back and a smaller one to the right of the spine.",
  "<b>Patches</b> &mdash; caf&eacute; au lait spots. The same flat discoloration as a macule, but larger than one centimetre. A patch may also be several macules that have coalesced."),

 ("s034_1.png", "papule-nevi", 34,
  "Close view of pale skin with four raised brown lesions of varying size, the largest oval and darkly pigmented, each standing above the surrounding surface.",
  "<b>Papules</b> &mdash; nevi. Palpable, elevated, solid, under one centimetre. Elevation is the whole distinction from a macule, and it is found by touch rather than by looking."),

 ("s035_1.png", "plaque-psoriasis", 35,
  "Elbow and forearm with several sharply demarcated raised red areas, the largest flat-topped and covered in thick silvery scale.",
  "<b>Plaques</b> &mdash; psoriasis. Elevated, flat-topped, firm and rough, larger than one centimetre, and occupying a large area compared with how far they rise. Note the extensor location: distribution and morphology are pointing at the same diagnosis."),

 ("s036_1.jpg", "nodule-measured", 36,
  "A smooth dome-shaped pink lesion on skin with black measurement bars marking it as eighteen millimetres across and twelve millimetres high.",
  "A <b>nodule</b>, measured. Elevated, firm, circumscribed, round or ellipsoid, and sitting deeper in the dermis than a papule. This is why a ruler is on the equipment list &mdash; at eighteen millimetres this is a nodule, and at over twenty it would be a tumor."),

 ("s037_1.png", "wheal-urticaria", 37,
  "Forearm with several raised pale pink irregular swellings that run together, surrounded by a broader area of redness.",
  "<b>Wheals</b> &mdash; an allergic reaction. Elevated, irregular areas of cutaneous edema: solid, of variable diameter, and the only primary lesion that is <b>transient</b>. If it has gone by the next visit, that is the finding rather than a missed examination."),

 ("s039_1.jpg", "vesicle-herpes-simplex", 39,
  "Lower lip and adjacent skin with a cluster of small clear fluid-filled blisters, some crusting, on a red base.",
  "<b>Vesicles</b> &mdash; herpes simplex. Superficial elevations filled with fluid, under one centimetre. The grouping is worth naming too: papules or vesicles clustered like this are described as <b>herpetiform</b>."),

 ("s040_1.jpg", "bulla", 40,
  "Child's arm covered in numerous raised round fluid-filled blisters of varying size on reddened skin.",
  "<b>Bullae</b>. The same superficial fluid-filled elevation as a vesicle, over one centimetre. Size is the only thing separating the two terms."),

 ("s041_1.png", "pustule-acne", 41,
  "Chin and lower face with multiple small raised lesions, several topped with visible yellow-white material, on reddened skin.",
  "<b>Pustules</b> &mdash; acne. Superficial elevations filled with <b>purulent</b> material, usually under one centimetre. Contents are what separate a pustule from a vesicle, not size."),

 ("s042_1.png", "cyst-diagram", 42,
  "Labelled cutaway diagram of a sebaceous cyst showing a large yellow sac of sebum sitting within the dermis and pushing the epidermis upward into a swelling.",
  "A <b>cyst</b> &mdash; elevated, circumscribed and <b>encapsulated</b>, sitting in the dermis or subcutaneous layer and filled with liquid or semisolid material. The capsule is the distinguishing feature; a nodule at the same depth has none."),

 ("s043_1.png", "crust-impetigo", 43,
  "Skin around the nose and upper lip covered with thick golden-yellow adherent crusts over reddened skin.",
  "<b>Crust</b> &mdash; the honey-coloured adherent crusting of impetigo. Cellular debris, dried serum and blood: a scab. Work backwards from it, because the antecedent primary lesion is usually a vesicle, bulla or pustule."),

 ("s044_1.png", "erosion", 44,
  "Lower leg with a bright red moist shallow denuded area alongside intact blistered skin and surrounding redness.",
  "<b>Erosion</b> &mdash; the moist area left after a bulla or vesicle ruptures. Loss of superficial epidermis only: the surface is moist but <b>does not bleed</b>, because the dermis has not been breached."),

 ("s045_1.png", "ulcer-stasis", 45,
  "Two photographs of the same lower leg side by side, each showing a deep open wound with a red base and irregular margins, the right panel smaller and healing.",
  "<b>Ulcer</b> &mdash; a stasis ulcer of venous insufficiency, shown before and after healing. Deeper loss of epidermis and dermis, so it may bleed and it may scar. Depth decides all three consequences at once."),

 ("s046_1.png", "fissure-tinea-pedis", 46,
  "Toes held apart to reveal a narrow linear split in the macerated pale skin of the interdigital space.",
  "<b>Fissure</b> &mdash; a linear crack in the skin, here between the toes in athlete's foot. Same site as tinea pedis on the infection slide, which is not a coincidence."),

 ("s047_1.png", "scale-scalp", 47,
  "Parted hair revealing scalp scattered with numerous small yellowish-white flakes adherent to the hair shafts and skin.",
  "<b>Scale</b> &mdash; thin flakes of exfoliated epidermis. Distinguish it from crust by what it is made of: scale is shed epidermis, crust is dried serum, blood and debris."),

 ("s048_1.png", "excoriation", 48,
  "Upper back with multiple linear and rounded red scratch marks, several with small dark scabs, scattered over otherwise pale skin.",
  "<b>Excoriations</b> &mdash; abrasions or scratch marks, which may be linear or rounded. This is the secondary lesion caused by <b>manipulation</b> rather than by the disease, and it tells you the eruption itches."),

 ("s049_2.jpg", "scar-linear", 49,
  "A thin pink linear scar running diagonally across pale skin, flat and confined to a narrow track.",
  "A <b>scar</b> &mdash; fibrous tissue replacing destroyed tissue. Thin and pale is atrophic, thick and pink is hypertrophic, and either way a scar <b>does not extend beyond the injured area</b>. That last clause is what separates it from a keloid."),

 ("s052_2.jpg", "lichenification", 52,
  "Backs of both knees showing thickened reddened skin with deep exaggerated skin creases and scattered small dark excoriated spots.",
  "<b>Lichenification</b> &mdash; thickening with <b>skin line accentuation</b>, from chronic irritation in atopic dermatitis. The exaggerated creases are the finding. Note the flexural distribution, and the excoriations that explain the mechanism."),

 ("s053_1.png", "collarette-scale", 53,
  "Pale skin with two ring-shaped lesions, each edged by a fine rim of scale that is attached at the outer margin and lifting free toward the centre.",
  "<b>Collarette scale</b> &mdash; pityriasis rosea. Fine scale attached at the <b>periphery</b> and detached at the <b>centre</b>, sitting on the edge of an inflammatory lesion. Which end is attached is the entire definition."),

 ("s055_1.jpg", "diascopy", 55,
  "A clear glass slide pressed against skin by a thumb and finger; small red spots remain visible through the glass in the compressed area and continue outside it.",
  "<b>Diascopy.</b> Press clear glass or plastic against the lesion and look at it under pressure. Here the spots persist under the glass &mdash; <b>no blanching, so this is hemorrhage in the skin</b>. Had the colour faded, it would be vascular engorgement instead. One manoeuvre, and it splits the whole vascular differential."),

 ("s056_1.png", "petechiae-purpura", 56,
  "Lower leg scattered with small red spots, with two labelled circles marking a cluster of pinpoint spots as petechiae and a single larger spot as purpura.",
  "<b>Petechiae and purpura</b> on one leg, labelled. Same finding at two sizes: petechiae under three millimetres, purpura from three millimetres to one centimetre. Neither blanches. Over a centimetre and it becomes an ecchymosis."),

 ("s057_1.png", "ecchymosis", 57,
  "Forearm with a large irregular purple-blue discoloured area above the wrist, flat and blending into surrounding skin.",
  "<b>Ecchymosis</b> &mdash; over one centimetre, purple to purplish-blue, non-blanching, and it <b>fades over time</b> as the extravasated blood breaks down. That evolution is what the other two do not do."),

 ("s058_1.jpg", "cherry-angioma", 58,
  "Close view of pale skin with two small bright red dome-shaped raised lesions, the larger one lobulated.",
  "<b>Cherry angiomas</b>, also called Campbell De Morgan spots. Dome shaped, bright red to violet or black, and they may or may not blanch &mdash; which is why they sit awkwardly between the blanching and non-blanching groups and are best learned by their shape."),

 ("s059_1.png", "pressure-ulcer-stage-1", 59,
  "Heel of a foot with a large well-defined pink-red area over the pressure point, the skin unbroken, with a paper measuring tape laid beside it.",
  "<b>Stage I</b> pressure ulcer. The skin is <b>intact</b> &mdash; the finding is erythema that fails to blanch under pressure, together with change in temperature, consistency, sensation and colour. Everything after this stage involves broken skin."),

 ("s060_1.png", "pressure-ulcer-stage-2", 60,
  "Reddened skin over a bony prominence with a shallow open wound at its centre exposing a moist pink-red base.",
  "<b>Stage II</b>. Partial thickness skin loss involving epidermis, dermis or both. Shallow and open, with no necrosis of the tissue beneath."),

 ("s061_1.png", "pressure-ulcer-stage-3", 61,
  "A deep crater-like open wound labelled Stage 3, with a dark red base, thickened yellow-tan margins and surrounding reddened skin.",
  "<b>Stage III</b>. Full thickness skin loss with necrosis of subcutaneous tissue. It may extend down to underlying muscle but <b>not through</b> it &mdash; reaching muscle without destroying it is still stage III."),

 ("s062_1.png", "pressure-ulcer-stage-4", 62,
  "A large deep wound on darkly pigmented skin with an open red cavity, extensive yellow-grey necrotic tissue and undermined blackened edges.",
  "<b>Stage IV</b>. Full thickness loss with destruction of tissue, muscle and/or bone. Involvement of muscle and bone is the line between this and stage III."),

 ("s064_1.jpg", "tinea-capitis", 64,
  "Scalp with a well-defined round area of hair loss covered in fine grey scale, the remaining hairs within it short and broken.",
  "<b>Tinea capitis</b> &mdash; a round <b>scaling</b> patch of alopecia with hairs broken off close to the scalp. Both features matter: alopecia areata gives smooth patches with no scale, and trichotillomania gives neither."),

 ("s064_2.jpg", "tinea-pedis", 64,
  "Two toes held apart showing white sodden macerated skin in the web space with fine scaling at the margins.",
  "<b>Tinea pedis</b> &mdash; macerated fissuring of the interdigital spaces. It also presents dry and scaling; the web spaces are the constant."),

 ("s064_3.jpg", "tinea-corporis", 64,
  "Upper back with several round scaly plaques of varying size, each with a raised active border and a paler clearer centre.",
  "<b>Tinea corporis</b> &mdash; scaling, sharply demarcated round plaques with <b>central clearing</b>. The active advancing edge with a quiet middle is what earns it the name ringworm, and the configuration term for it is <b>annular</b>."),

 ("s067_1.jpg", "basal-cell-carcinoma", 67,
  "Small round lesion on pale skin with a translucent raised rolled border and a depressed crusted red centre.",
  "<b>Basal cell carcinoma</b> &mdash; a translucent, pearly nodule with a <b>depressed centre and raised borders</b>. The face is the common site. A non-healing ulcer there should raise the same suspicion even without the pearly rim."),

 ("s069_1.jpg", "squamous-cell-carcinoma", 69,
  "Raised red-brown plaque on sun-damaged skin with an irregular scaling crusted surface and a small central erosion.",
  "<b>Squamous cell carcinoma</b> &mdash; a red scaling, crusting nodule or plaque that can ulcerate and bleed. Face and other sun-exposed areas. Compare the surface with basal cell carcinoma: scaling and crusted here, translucent and pearly there."),

 ("s071_1.png", "melanoma-diameter", 71,
  "Diagram of a brown oval lesion above a ruler segment marked six millimetres, with a pencil eraser drawn beneath it for comparison.",
  "The <b>D</b> in the melanoma warning signs: diameter larger than <b>six millimetres</b>, which is about the width of a pencil eraser. The full list runs A asymmetry, B border irregularity, C colour variation, D diameter, E evolving or elevation, F family history, G growing."),

 ("s072_1.jpg", "melanoma", 72,
  "A large irregular lesion on skin with a raised glossy near-black nodular portion, a ragged notched dark red-brown area beside it, and a centimetre ruler below showing it spans over two centimetres.",
  "<b>Malignant melanoma</b>, with a ruler for scale. Every letter is visible at once: asymmetric, notched irregular border, marked variation in pigment, and well beyond six millimetres. Compare it against the <b>changing nevus</b> the history should have flagged."),

 ("s074_2.png", "kaposi-sarcoma", 74,
  "Two adjacent raised firm plaques of deep purple-red colour on otherwise normal skin.",
  "<b>Kaposi's sarcoma</b> &mdash; dark blue-purple macules, papules, nodules and plaques. Lesions start light coloured and coalesce into darker ones, and they are widely disseminated across legs, trunk, arms, neck and head. The most frequent neoplasm in patients with acquired immunodeficiency syndrome."),

 ("s079_1.png", "alopecia-areata", 79,
  "Scalp with dark hair parted to show two smooth well-circumscribed round bald patches with no scaling or redness.",
  "<b>Alopecia areata</b> &mdash; hair loss in multiple round patches. The scalp is <b>smooth</b>, with no scale, which separates it immediately from tinea capitis. Look at the margins for the tapered &ldquo;exclamation point&rdquo; hairs. It is a chronic inflammatory disease of the hair follicles and is associated with autoimmune disorders."),

 ("s085_1.jpg", "koilonychia", 85,
  "Fingertip with a nail whose plate is thinned and curves upward at the edges into a concave spoon shape.",
  "<b>Koilonychia</b> &mdash; spoon-shaped concave nails. The nail plate thins and becomes inverted; the concavity can be deep enough to hold a drop of water."),

 ("s086_1.png", "onycholysis", 86,
  "Four fingernails with the outer portions separated from the nail bed, appearing opaque yellow-white against the pink attached proximal nail.",
  "<b>Onycholysis</b> &mdash; <b>painless</b> separation of the nail plate from the bed, beginning <b>distally</b> and enlarging the free edge. Several or all nails are usually affected. Causes span local irritation, fungal infection, psoriasis, tetracycline and trauma."),

 ("s087_1.png", "nail-pitting", 87,
  "A single fingernail whose surface is dotted with numerous small shallow depressions scattered irregularly across the plate.",
  "<b>Nail pitting</b> &mdash; dystrophy of the nail plate producing small depressions. Worth pairing in your head with onycholysis, since psoriasis produces both."),

 ("s090_1.jpg", "nail-transverse-line", 90,
  "A fingernail crossed by a single pale line running side to side across the plate, parallel to the nail base.",
  "A <b>transverse</b> nail change. Beau's lines are transverse <b>depressions</b> you can feel; Mee's lines are transverse <b>lines</b> of colour. Beau's lines date the insult &mdash; halfway up the nail corresponds to an illness about three months before the visit."),

 ("s091_1.jpg", "clubbing", 91,
  "Back of a hand with all four fingertips broadened and rounded, the nails curving over bulbous ends.",
  "<b>Clubbing</b> &mdash; the angle between nail base and finger exceeds <b>one hundred and eighty degrees</b>, and the end of the finger becomes rounded and bulbous. Sight the finger from the side; the angle is the measurable part rather than the impression of bulbousness."),

 ("s092_1.png", "paronychia", 92,
  "Thumb with the skin of the nail fold swollen, shiny and deep red, with a small streak of blood at the nail margin.",
  "<b>Acute paronychia</b> &mdash; soft tissue infection around the cuticle or nail fold, painful and purulent. There is a chronic form too; pain and pus are what mark this one as acute."),
]


def main():
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    before = after = 0
    for i, (src, stem, slide, alt, cap) in enumerate(FIGURES, 1):
        sp = os.path.join(SRC, src)
        before += os.path.getsize(sp)
        im = Image.open(sp)
        if im.mode in ("RGBA", "P", "LA"):
            bg = Image.new("RGB", im.size, (255, 255, 255))
            im = im.convert("RGBA")
            bg.paste(im, mask=im.split()[-1])
            im = bg
        else:
            im = im.convert("RGB")
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        dst = os.path.join(OUT, "%02d-%s.jpg" % (i, stem))
        im.save(dst, "JPEG", quality=85, optimize=True, progressive=True)
        after += os.path.getsize(dst)
    print("figures: %d   %.1f MB -> %.1f MB" % (len(FIGURES), before / 1e6, after / 1e6))
    return len(FIGURES)


def figure_html(dirname):
    """Emit the <figure> blocks, keyed by output stem, for the guide builder."""
    out = {}
    for i, (src, stem, slide, alt, cap) in enumerate(FIGURES, 1):
        fn = "%02d-%s.jpg" % (i, stem)
        path = os.path.join(OUT, fn)
        w = h = None
        if os.path.exists(path):
            with Image.open(path) as im:
                w, h = im.size
        dims = ' width="%d" height="%d"' % (w, h) if w else ""
        out[stem] = (
          '<figure class="fig"><img%s loading="lazy" src="%s/%s" alt="%s">'
          '<figcaption>%s <span class="tag">Source: PD II Derm - Beck.pptx, Slide %d.</span>'
          '</figcaption></figure>' % (dims, dirname, fn, alt, cap, slide))
    return out


if __name__ == "__main__":
    main()
