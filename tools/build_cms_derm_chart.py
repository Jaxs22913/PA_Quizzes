#!/usr/bin/env python3
"""Build the CMS I Dermatology Comparison Chart.

Jaxon's format, 2026-08-19: one row per condition, columns left to right --
Picture, Name, Common manifestation (including how a patient may describe it),
First test and gold standard, First line then second line treatment, Patient
education. He asked to try it on dermatology first and then extend the same
shape to the other CMS blocks.

EVERY CELL COMES FROM THE DECKS. Where a deck does not state something, the
cell says so rather than being filled in from general knowledge -- an invented
gold standard in a revision chart is worse than an empty box.

Images are extracted from the five Exam 1 dermatology PowerPoints. Slide images
are cleared for use provided the slide is cited (Jaxon, 2026-08-18: the decks
come from the school and the class may use them on that condition), so every
row carries its deck and slide number. Third-party marks baked into the images
-- Fitzpatrick's, DermNet, VisualDx, Current Medical Diagnosis & Treatment,
Mayo -- are left visible rather than cropped out.

Every image was viewed on a contact sheet before being assigned to a row.
Conditions with no suitable slide image get a labelled placeholder rather than
a picture of something else.
"""
import os, re, html as H
from PIL import Image, PngImagePlugin
PngImagePlugin.MAX_TEXT_CHUNK = 100 * 1024 * 1024

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SRC = "/private/tmp/claude-501/-Users-jaxonluke/8623a091-045a-42b8-8052-ca7d2eb04188/scratchpad/cms_derm_imgs"
OUT_DIR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1", "cms-derm-chart-images")
OUT_HTML = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1", "cms-derm-comparison-chart.html")
MAXW = 420

DECK = {
 "l2": "2. General Dermatology I.pptx",
 "l3": "3. Dermatology  II.pptx",
 "l4": "4.  Cutaneous Bacterial Infections.pptx",
 "l5": "CMS I Dermatological Infestations - Shahsv.pptx",
 "l6": "6. Fungal and Viral Skin Infections - Jaquith.pptx",
 "l9": "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx",
 "l7": "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx",
 "l8": "CMS I Pigmented Skin Lesions - Shahsv-2.pptx",
}
LECTURE = {"l2": "Lecture 2", "l3": "Lecture 3", "l4": "Lecture 4",
           "l5": "Lecture 5", "l6": "Lecture 6", "l7": "Lecture 7", "l8": "Lecture 8",
           "l9": "Lecture 9"}

# (img, name, manifestation, tests, treatment, education)
# img is "tag_sNNN_K.ext" or None
_re_tags = re.compile(r"<[^>]+>")


# ==== VIGNETTE GIVEAWAYS ====
# The words a stem uses that hand you the diagnosis. Deck language only --
# see tools/add_chart_giveaways.py for why that matters.
GIVEAWAY = {'Atopic dermatitis': '<b>FLEXURES in children and adults; cheeks and extensors in INFANTS</b> &middot; lichenification from chronic scratching &middot; poorly demarcated &middot; personal or family atopy', 'Dyshidrotic eczema': '<b>Tapioca-like</b> deep-seated vesicles &middot; palms, soles, sides of fingers', 'Nummular eczema': '<b>COIN-SHAPED discrete plaques</b> &mdash; the shape IS the diagnosis &middot; extremities', 'Irritant contact dermatitis': '<b>Well demarcated and &ldquo;GLAZED APPEARING&rdquo;</b> &middot; <b>shaped like the exposure</b> &middot; hands and forearms &middot; frequent handwashing, gloves &middot; no sensitisation needed', 'Allergic contact dermatitis': '<b>LINEAR vesicles in MULTIPLE STAGES OF HEALING</b> (urushiol / poison ivy) &middot; well-demarcated <b>at the contact site</b> &middot; needs prior sensitisation', 'Seborrheic dermatitis': '<b>Greasy yellow scale</b> &middot; scalp, eyebrows, nasolabial folds, ears, central chest', 'Perioral dermatitis': 'Papules <b>around the mouth SPARING the vermilion border</b> &middot; after topical steroid on the face &middot; burning', 'Diaper dermatitis': '<b>CONVEX surfaces of the napkin area, sparing the folds</b> &middot; <b>once the FOLDS are involved with satellite lesions, it is candidal</b>', 'Stasis dermatitis': '<b>Gaiter region</b> &middot; bilateral &middot; oedema and chronic venous change &middot; violaceous/grey/deep brown on darker skin', 'Bullous pemphigoid': '<b>TENSE bullae that do NOT rupture easily</b> &middot; <b>Nikolsky NEGATIVE &mdash; the one of the three that is</b> &middot; elderly &middot; mucosa uncommon', 'Pemphigus (vulgaris)': '<b>FLACCID bullae that rupture, leaving erosions</b> &middot; <b>MUCOSA often the FIRST site</b> &middot; middle-aged &middot; Nikolsky positive &mdash; <b>so is toxic epidermal necrolysis, so it does not separate them</b>', 'Psoriasis &mdash; plaque': '<b>Thick SILVERY scale</b> &middot; <b>Auspitz sign</b> when the scale is lifted &middot; EXTENSOR surfaces, scalp, nails &middot; psoriatic arthritis goes with it', 'Psoriasis &mdash; guttate': '<b>Drop-like</b> small papules &middot; widespread on the trunk', 'Psoriasis &mdash; pustular': '<b>Sterile</b> pustules &middot; palms and soles', 'Pityriasis rosea': '<b>HERALD PATCH alone for a week or two BEFORE the rest</b> &middot; <b>Christmas-tree</b> pattern along skin lines &middot; collarette of SCALE', 'Lichen planus': '<b>The six Ps</b> &mdash; purple, polygonal, pruritic, planar papules and plaques &middot; <b>Wickham striae</b> &middot; flexor wrists, oral mucosa', 'Lichen simplex chronicus': '<b>Accentuated skin markings</b> in a thickened plaque &middot; <b>wherever the patient can reach</b> &middot; itch-scratch cycle', 'Alopecia areata': '<b>Exclamation point hairs</b> &middot; discrete smooth round patches &middot; <b>non-scarring</b>', 'Androgenetic alopecia': '<b>Follicular miniaturisation</b> &middot; temporal recession and vertex in men, <b>widened part</b> in women &middot; non-scarring', 'Xeroderma (xerosis)': 'Dry, rough, cracked &middot; <b>worse in winter</b> &middot; shins and forearms', 'Erythema multiforme': '<b>Target lesion with THREE concentric zones</b> &middot; <b>acral</b>, starting on the extremities', 'Dermatitis herpetiformis': '<b>Intensely</b> pruritic &middot; <b>symmetrical</b> knees, elbows, buttocks, back &middot; <b>herpetiform grouping</b> &middot; bloating and diarrhoea', 'Acanthosis nigricans': '<b>Velvety</b> hyperpigmented thickening &middot; neck, axillae, groin', 'Epidermolysis bullosa': 'Blistering from <b>minimal trauma</b> &middot; <b>at or shortly after birth</b> &middot; structural protein mutation', 'Urticaria': '<b>An individual wheal resolves within 24 hours</b> &middot; blanches fully &middot; <b>migrates</b> &middot; &plusmn; angio-oedema', 'Erythema nodosum': '<b>Tender</b> nodules, <b>bilateral anterior shins</b>, that <b>do NOT ulcerate</b> &middot; preceded by fever and arthralgia', 'Granuloma annulare': '<b>Annular ring of papules with NO SCALE ANYWHERE</b> &mdash; that absence separates it from tinea &middot; dorsal hands and feet &middot; flesh-coloured', 'Pyoderma gangrenosum': '<b>Undermined violaceous border</b> &middot; rapidly expanding painful ulcer from a pustule &middot; <b>pathergy</b> &mdash; worsens with trauma', 'Acne rosacea': 'Central facial erythema, flushing, telangiectasias &middot; <b>NO COMEDONES</b> &mdash; which separates it from acne vulgaris', 'Hyperhidrosis': '<b>Absent during sleep</b> &amp; bilateral focal (palms, soles, axillae) = primary &middot; generalised, asymmetric or nocturnal = secondary', 'Stevens-Johnson syndrome': 'Prodrome <b>1&ndash;3 days before the skin</b> &middot; <b>mucosal erosions at 2+ sites</b> &middot; painful &middot; <b>&lt;10%</b> body surface', 'Toxic epidermal necrolysis': '<b>&gt;30% body surface DETACHMENT</b> &middot; <b>&ldquo;wet parchment&rdquo;</b> &middot; drug and prodrome 1&ndash;3 days before &middot; Nikolsky positive &mdash; <b>shared with pemphigus; the body-surface figure is what separates them</b>', 'Sunburn': 'Onset <b>3&ndash;5 hours</b> after exposure, peaking at <b>12&ndash;24</b> &middot; blistering = second degree', 'Drug-induced photosensitivity': '<b>First exposure, dose-dependent, exaggerated sunburn on exposed skin</b> = phototoxic &middot; <b>needs sensitisation, eczematous, may spread</b> = photoallergic', 'Photodermatitis (phytophotodermatitis)': '<b>Linear or streaked</b> hyperpigmentation &middot; <b>lime juice and sun</b> &mdash; &ldquo;margarita dermatitis&rdquo; &middot; celery, parsley, fig', 'Polymorphous light eruption': '<b>30 minutes to hours</b> after ultraviolet &middot; <b>first sunny days of spring</b> &middot; décolletage, forearms, dorsal hands', 'Solar lentigo also Lecture 8': 'Well-defined but <b>irregular borders that coalesce</b> at sites of <b>severe sunburn</b> &middot; 90% of people by 50', 'Actinic keratosis': '<b>&ldquo;Sandpaper&rdquo; texture &mdash; felt before it is seen</b> &middot; sun-exposed face, scalp, dorsal hands', 'Dermatoheliosis (photoaging)': '<b>Cutis rhomboidalis nuchae</b> on the posterior neck &middot; leathery, mottled dyspigmentation &middot; sun-protected skin looks far younger', 'Acne vulgaris': '<b>COMEDONES are the hallmark</b> &mdash; open (blackheads) and closed (whiteheads) &middot; systemic symptoms absent', 'Folliculitis': 'Each papule or pustule <b>pierced by a central hair</b> &middot; abrupt, afebrile', 'Pseudomonas (&ldquo;hot tub&rdquo;) folliculitis': '<b>8 hours to 5 days after a hot tub</b> &middot; trunk, extremities, buttocks &middot; <b>spares face, neck, palms, soles</b>', 'Pseudofolliculitis barbae': '<b>Foreign-body reaction, NOT infection</b> &middot; cut hair re-penetrates the skin &middot; tender papule with a <b>central hair shaft</b> &middot; tightly curled beard hair', 'Furuncle': '<b>Single</b> follicular abscess &middot; fluctuant tender nodule with <b>one opening</b>', 'Carbuncle': '<b>Two or more confluent furuncles with SEPARATE heads</b> &middot; <b>sieve-like</b> openings &middot; systemic symptoms', 'Hidradenitis suppurativa': '<b>Apocrine</b> sites &mdash; axilla, groin, breasts, perineum &middot; <b>recurrent more than twice in 6 months</b> &middot; sinus tracts', 'Erythrasma': '<b>Coral-red fluorescence on Wood lamp</b> &middot; intertriginous, inner thighs &middot; <i>Corynebacterium minutissimum</i>', 'Impetigo &mdash; non-bullous': '<b>Honey-coloured adherent crust</b> &middot; face and extremities &middot; spreads by self-inoculation from scratching', 'Impetigo &mdash; bullous': '<b>Fragile bullae on INTACT skin</b> &middot; <b>exclusively <i>Staphylococcus aureus</i></b> &middot; epidermolytic toxin', 'Ecthyma': '<b>Punched-out ulcer through the dermis</b> with a thick grey-yellow crust &middot; lower legs &middot; <b>heals with a scar</b>', 'Erysipelas': '<b>Sharply demarcated, RAISED border</b> &mdash; <b>cellulitis is flat and poorly demarcated</b> &middot; sudden high fever within 48 hours &middot; UPPER dermis', 'Cellulitis': '<b>Poorly demarcated and FLAT</b> &mdash; <b>erysipelas is sharply demarcated and RAISED</b> &middot; deeper dermis and subcutis &middot; lower leg', 'Abscess': 'Collection of pus from <b>traumatic inoculation</b> &mdash; unlike a furuncle, which starts in a <b>hair follicle</b>', 'Acute paronychia': '<b>2&ndash;5 days after trauma</b> &middot; rapid onset &middot; erythematous oedematous nail fold &middot; may become fluctuant', 'Chronic paronychia': '<b>Irritant/allergic, not primarily infective</b> &middot; <b><i>Candida albicans</i></b> commonest &middot; <b>no fluctuance</b> &middot; thickened nail plates', 'Necrotizing fasciitis': '<b>Unrelenting pain OUT OF PROPORTION to the findings</b> &middot; rapidly progressive &middot; hypotension + white count &ge;15,000 + violaceous skin', 'Scabies': '<b>Intense NOCTURNAL pruritus</b> &middot; <b>interdigital webs</b>, volar wrists, axillae, genitalia &middot; <b>spares the head in adults</b>', 'Crusted (hyperkeratotic) scabies': '<b>Thick flaking scale, millions of mites</b> &middot; <b>may NOT itch at all</b> &middot; poorly defined patches', 'Pediculosis capitis (head lice)': 'Incubation <b>4&ndash;6 weeks</b> &middot; children &middot; nits on hair shafts &middot; occipital and postauricular', 'Pediculosis corporis (body lice)': '<b>Linear excoriations on back, neck, shoulders, waist</b> &middot; <b>lives in clothing seams</b> &middot; homeless, crowded, poor hygiene', 'Pediculosis pubis (crabs)': '<b>Maculae caerulae</b> &mdash; slate-grey/bluish 1&nbsp;cm macules &middot; periumbilical papular urticaria', 'Bedbugs': '<b>Painless bites GROUPED IN A LINE</b> &middot; nocturnal &middot; hides in headboards, picture frames, behind wallpaper', 'Tungiasis (fleas)': '<b>Yellow, firm, translucent papule with a central black dot</b> &middot; female flea burrowed to lay eggs &middot; feet', 'Caterpillars (lepidopterism)': '<b>Erucism</b> &mdash; pruritic dermatitis from <b>pointed or hollow hairs</b> &middot; gypsy moth', 'Cutaneous larva migrans': '<b>SERPIGINOUS raised linear track that MIGRATES</b> &middot; after sand or soil contact &middot; dog and cat hookworm, human a dead-end host', 'Black widow spider': '<b>Red hourglass on the underside</b> &middot; <b>severe pain with MINIMAL skin findings</b> &middot; alpha-latrotoxin &middot; muscle cramps', 'Brown recluse spider': '<b>Dark violin/fiddle on the cephalothorax</b> &middot; closets, attics, stored clothing &middot; Midwest and Southeast', 'Hobo spider': '<b>Grey herringbone on the abdomen</b> &middot; <b>Pacific Northwest</b> &middot; mistaken for brown recluse', 'Lyme disease': '<b>&gt;5&nbsp;cm ring EXPANDING over days after a tick</b>, central clearing, darker punctate centre &middot; <b>NO scale on the border &mdash; unlike tinea</b>', 'Rocky Mountain spotted fever': '<b>Fever + headache + rash</b> (all three in only ~60%) &middot; rash from <b>wrists and ankles inward</b> &middot; dog or wood tick', "Cercarial dermatitis (swimmer's itch)": 'Pruritic eruption after <b>fresh water</b> &middot; <b>snail intermediate host</b> &middot; waterfowl parasite, human a dead-end', 'Tinea capitis (scalp)': '<b>Preadolescent children</b> &mdash; puberty changes sebum fatty acids &middot; <i>Trichophyton tonsurans</i> commonest in the United States', 'Black dot tinea capitis': '<b>Hair fractures AT the scalp surface</b> &rarr; alopecia patches <b>studded with black dots</b>', 'Tinea barbae &mdash; inflammatory': '<b>Boggy pustular kerion-like plaque</b> &middot; <b>hairs loose and easily removed</b> &middot; from ANIMALS', 'Tinea barbae &mdash; noninflammatory': 'Annular scaly plaques or folliculitis-like &middot; <b>from another person</b> &middot; hairs break near the surface', 'Tinea corporis (body) &mdash; &ldquo;ringworm&rdquo;': '<b>Annular, with SCALE ON THE ADVANCING BORDER</b> and progressive central clearing &middot; <b>the scale is what separates it from granuloma annulare AND from erythema migrans</b>', 'Tinea cruris (groin) &mdash; &ldquo;jock itch&rdquo;': 'Sharply demarcated on the <b>proximal medial thigh</b> &middot; <b>THE SCROTUM IS TYPICALLY SPARED</b> &middot; men, with tinea pedis', 'Tinea pedis &mdash; interdigital': '<b>Maceration between the toes, especially the 3rd and 4th interspaces</b> &middot; commonest dermatophyte infection in adults', 'Tinea pedis &mdash; hyperkeratotic': '<b>&ldquo;Resembles a SHOE DISTRIBUTION&rdquo;</b> &mdash; soles plus medial and lateral surfaces &middot; diffuse thickening', 'Tinea pedis &mdash; vesiculobullous': '<b>The moist, acute form</b> &middot; vesicles or bullae on erythema &middot; pruritic AND painful', 'Onychomycosis (tinea unguium)': '<b>Distal lateral</b> subungual debris &middot; onycholysis, thickening, <b>crumbling</b> &middot; <i>T. rubrum</i>', 'Tinea manuum (hand)': '<b>TWO FEET&ndash;ONE HAND</b> &middot; palm hyperkeratotic like tinea pedis, dorsum annular like tinea corporis', 'Id (dermatophytid) reaction': '<b>Dermatitis at a site DISTANT from the infection</b> &middot; <b>1&ndash;2 weeks</b> after &middot; commonly with tinea pedis', 'Tinea incognito': '<b>Tinea altered by topical STEROIDS</b> &middot; flares whenever the steroid stops &middot; loses its typical border', 'Cutaneous candidiasis and intertrigo': '<b>SATELLITE lesions beyond the main patch</b>, in body folds &middot; friction, moisture and heat &middot; <i>Candida albicans</i>', 'Pityriasis versicolor (tinea versicolor)': '<b>&ldquo;Spaghetti and meatballs&rdquo; on potassium hydroxide</b> &middot; velvety tan/pink/white finely scaling macules &middot; <b>NOT contagious</b>', 'Varicella (chickenpox)': '<b>SEVERAL STAGES PRESENT SIMULTANEOUSLY</b> &mdash; macules, papules, vesicles and crusts together &middot; concentrated on the trunk', 'Herpes zoster (shingles)': '<b>Single DERMATOME, does not cross the midline</b> &middot; <b>dysesthesia or pain BEFORE the rash</b> &middot; reactivated varicella-zoster', 'Postherpetic neuralgia': '<b>Pain persisting 90 days or more after rash onset</b> &middot; burning, stabbing, <b>allodynia</b> to light touch', 'Herpes zoster ophthalmicus': '<b>Hutchinson sign &mdash; lesions on the tip or side of the NOSE</b> &middot; V1 of the trigeminal &middot; <b>its ABSENCE does not exclude eye involvement</b>', 'Ramsay Hunt syndrome (herpes zoster oticus)': '<b>Facial palsy + vesicles in the ear canal or auricle</b> &middot; hearing loss, tinnitus or vertigo', 'Herpes simplex virus (HSV-1 and HSV-2)': '<b>Grouped vesicles on an erythematous base</b> &middot; prodromal tingling &middot; <b>site does NOT reliably determine the type</b>', 'Herpetic whitlow': '<b>DISTAL FINGER</b> &middot; grouped vesicles on a swollen digit &middot; inoculation through broken skin', 'Molluscum contagiosum': '<b>Umbilicated PEARLY FLESH-COLOURED dome</b>, 3&ndash;5&nbsp;mm &middot; poxvirus, children &middot; <b>vs sebaceous hyperplasia, which is YELLOW and in older adults</b>', 'Verruca vulgaris (common warts)': '<b>Interrupts the skin lines</b> &middot; <b>blackened centre</b> (thrombosed capillaries) &middot; <b>NO ROOTS</b> &mdash; underside round and smooth &middot; pain on SIDE pressure', 'Verruca plana (flat warts)': '<b>FLAT-TOPPED</b> smooth slightly elevated papules &middot; face, forehead, dorsal hands, shins', 'Verruca plantaris (plantar warts)': '<b>Weight-bearing surface</b> &middot; clustering into a <b>MOSAIC</b> wart', 'Squamous cell carcinoma': '<b>CUMULATIVE</b> sun exposure &middot; small red <b>conical HARD nodule that may ulcerate</b> &middot; <b>non-healing ulcer</b> &middot; lip, ear, scalp', 'Basal cell carcinoma &mdash; nodular': '<b>PEARLY translucent papule whose telangiectasias STRETCHING THE SKIN accentuates</b> &middot; central erosion &middot; slow growth over years &middot; INTERMITTENT intense sun', 'Basal cell carcinoma &mdash; superficial': '<b>Reddish shiny scaly THIN plaque on the BACK or CHEST</b> &middot; thready pearly border with spotty edge pigment', 'Basal cell carcinoma &mdash; pigmented and morpheaform': '<b>Scar-like or IVORY-WHITE</b> = morpheaform, extends beyond what you can see &middot; stippled pigment mimicking melanoma = pigmented', 'Malignant melanoma': '<b>ABCDE</b> &mdash; asymmetry, border, colour variegation, diameter &gt;6&nbsp;mm, <b>evolution</b> &middot; <b>nodular may be amelanotic and LACK the classic features</b>', 'Nail unit melanoma': '<b>Longitudinal melanonychia in ONE digit, widening PROXIMALLY (triangular)</b> &middot; <b>Hutchinson sign onto the proximal nail fold</b> &middot; thumb, great toe', 'Nail unit squamous cell carcinoma / Bowen disease': '<b>Chronic UNILATERAL verrucous nail lesion repeatedly treated as a wart, paronychia or fungus</b> &middot; longitudinal erythronychia', 'Glomus tumour and the benign nail tumours': '<b>Severe paroxysmal pain + exquisite point tenderness + COLD SENSITIVITY, with a nearly normal-looking nail</b>', 'Kaposi sarcoma': '<b>Red or purple macules, plaques or nodules &mdash; including the HARD PALATE</b> &middot; human herpesvirus 8 + immunosuppression &middot; <b>oedema out of proportion to visible lesions</b>', 'Cutaneous T-cell lymphoma (mycosis fungoides)': '<b>Patches/plaques &gt;5&nbsp;cm that look like eczema or psoriasis but RESIST treatment for years</b> &middot; <b>itch out of proportion</b> &middot; follicular hair loss', 'Ephelides (freckles)': '<b>FADE when the sun goes</b> &middot; 3&ndash;5&nbsp;mm light brown symmetric macules &middot; fair skin, red or blonde hair &middot; <b>MCR1</b>', 'Lentigines': '<b>Do NOT fade without sun</b> &mdash; the whole differential against freckles &middot; uniformly black or brown, well circumscribed, &lt;5&nbsp;mm', 'Solar lentigo also Lecture 3': 'Well defined but <b>irregular borders that COALESCE</b> at severe sunburn sites &middot; chronically exposed skin', 'Seborrheic keratosis': '<b>&ldquo;STUCK ON&rdquo; or pasted-on</b>, velvety or warty, beige to black &middot; <b>dermatosis papulosa nigrans is the SAME lesion, small, on the FACE of darker skin</b>', 'Dermatosis papulosa nigrans': '<b>Multiple small dark papules on the FACE and NECK of darker skin</b> &middot; <b>histologically identical to seborrheic keratosis &mdash; the site and the skin tone are the clue</b>', 'Vitiligo': '<b>Depigmented (not hypo-) macules that FLUORESCE under Wood lamp</b> &middot; distinct margins &middot; autoimmune, T-cell destruction of melanocytes', 'Congenital melanocytic naevus': '<b>Present at birth</b> &middot; may be pebbly, rugose, verrucous &middot; <b>head, neck or posterior midline &rarr; magnetic resonance for neurocutaneous melanosis</b>', 'Naevus spilus': '<b>Café-au-lait-like background patch SPECKLED with darker macules</b> &middot; &ldquo;spotted naevus&rdquo;', 'Common acquired melanocytic naevus (mole)': '<b>&lt;6&nbsp;mm, homogenous, symmetric, sharply demarcated</b> &middot; peaks in the thirties then declines &middot; <b>very dark or black on light skin is suspicious</b>', 'Blue naevus': '<b>BLUE, blue-grey or blue-black</b> &mdash; pigment deep in the DERMIS &middot; women, twenties &middot; dorsal hands and feet, scalp, buttocks', 'Pigmented spindle cell naevus (Reed)': '<b>JET-BLACK sharply circumscribed papule &lt;7&nbsp;mm on the THIGH</b> &middot; thirties, female &middot; <b>excision with negative margins</b>', 'Spitz naevus': '<b>Solitary pink or red DOME-SHAPED firm papule that RESEMBLES MELANOMA</b> &middot; <b>spares palms, soles and mucosa</b> &middot; biopsy vs wide excision', 'Dysplastic melanocytic naevus': '<b>&ge;5&nbsp;mm with IRREGULAR INDISTINCT borders and variable pigment</b> &middot; &ldquo;pebbly&rdquo; surface &middot; sun-exposed skin', 'Clavus (corn) &mdash; hard': '<b>CENTRAL KERATIN CORE</b> &middot; &lt;1.5&nbsp;cm, well defined &middot; <b>painful on DIRECT DOWNWARD pressure</b> &middot; <b>skin lines RUN THROUGH</b> &middot; dorsal/lateral 5th toe', 'Clavus (corn) &mdash; soft': '<b>4th-to-5th toe WEB SPACE</b>, macerated by moisture &middot; still has the central core', 'Callus': '<b>NO central core</b> &middot; diffuse, larger, irregular, poorly defined &middot; <b>usually PAINLESS</b> &middot; palms or balls of the feet', 'Keloid': '<b>EXTENDS BEYOND the original wound</b> &middot; develops slowly, may appear months later, <b>no regression</b> &middot; ear lobe, shoulders, sternal notch &middot; darker skin', 'Hypertrophic scar': '<b>CONFINED to the wound margins</b> &middot; within <b>four weeks</b> &middot; <b>regresses with time</b> &middot; where scars cross joints at a right angle', 'Cutaneous horn': '<b>Keratin projection ARISING FROM ANOTHER LESION</b> &mdash; the base is what matters &middot; <b>deep shave biopsy</b>', 'Acrochordon (skin tag)': '<b>PEDUNCULATED &mdash; narrow stalk, broad tip</b> &middot; friction sites: neck, axilla, groin &middot; 60% of people by 70', 'Pressure injury (pressure ulcer)': '<b>NON-BLANCHABLE erythema over a BONY PROMINENCE</b> = stage 1 &middot; obscured by slough or eschar = unstageable &middot; the non-blanching is the whole point', 'Pilonidal cyst': '<b>Pit over the COCCYX drawing in hair and debris</b> &middot; male 3:1 &middot; <b>sinus = blind track; fistula = joins two epithelial surfaces</b>', 'Dermatofibroma': '<b>DIMPLE SIGN &mdash; retracts on lateral compression</b> &middot; firm 0.5&ndash;1&nbsp;cm nodule on the LEGS &middot; <b>most common painful skin tumour</b>', 'Keratoacanthoma': '<b>Dome with a CENTRAL KERATIN-FILLED CRATER</b> &middot; <b>rapid growth in 6&ndash;8 weeks, then regression</b> &middot; red tattoo ink, skin trauma', 'Epidermoid (epidermal) cyst': '<b>CENTRAL PORE / punctum</b> &middot; expresses pasty material smelling of <b>rancid cheese</b> &middot; <b>NOT a sebaceous cyst</b> despite the name', 'Syringoma': '<b>ECCRINE duct</b> neoplasms &middot; multiple 1&ndash;2&nbsp;mm papules on the <b>EYELIDS</b> and upper cheeks &middot; appear at puberty, female', 'Infantile hemangioma': '<b>INVOLUTES &mdash; 50% by 5, 70% by 7, 90% by 9</b> &middot; preterm, female 3:1 &middot; earliest sign is BLANCHING, then fine telangiectasias, then bright red', 'Nevus flammeus (port-wine stain)': '<b>NEVER involutes</b> &mdash; dilation with NO endothelial proliferation, which is why &middot; present at birth, <b>DARKENS and THICKENS</b> &middot; sharp midline cutoff', 'Nevus simplex (stork bite)': '<b>FADES within a year</b>, or persists on the neck &middot; more noticeable when the baby cries &middot; head and neck', 'Cherry angioma': '<b>Deep red dome that INCREASES IN NUMBER WITH AGE</b> &middot; trunk &middot; &lt;5&nbsp;mm &middot; new ones keep appearing and cannot be prevented', 'Telangiectasia': '<b>A permanently dilated capillary UNDER 1&nbsp;mm</b>, sometimes with a central punctum &middot; associated with numerous diseases &mdash; work up the cause', 'Nevus araneus (spider angioma)': '<b>ESTROGEN EXCESS</b> &mdash; pregnancy or the pill (both resolve after), <b>CIRRHOSIS and liver failure</b> &middot; dilation of existing vessels, no proliferation', 'Pyogenic granuloma': '<b>Moist bright red papule that BLEEDS readily, with an EPITHELIAL COLLARETTE at its BASE</b> &middot; pregnancy, fingers &middot; misnamed &mdash; neither infectious nor granulomatous', 'Neurofibromatosis type 1': '<b>Café-au-lait &gt;5&nbsp;mm prepubertal / &gt;15&nbsp;mm postpubertal, SIX OR MORE</b> &middot; <b>Crowe sign &mdash; axillary and inguinal freckling &lt;5&nbsp;mm</b> &middot; chromosome 17', 'Xanthelasma': '<b>Soft YELLOW plaques on the MEDIAL EYELIDS</b> &middot; lipid-laden macrophages &middot; <b>check the lipids</b>', 'Lipoma': '<b>Soft, painless, MOBILE subcutaneous mass</b> &middot; the most common soft tissue tumour', 'Digital mucous cyst': '<b>A PSEUDO-cyst &mdash; no cellular lining</b> &middot; mucin extruded from a joint space &middot; may groove the nail', 'Sebaceous hyperplasia': '<b>YELLOW umbilicated papule in an OLDER ADULT</b> &middot; face &middot; <b>vs molluscum, which is pearly flesh-coloured and in children</b> &middot; no malignant potential'}
# ==== END GIVEAWAYS ====

ROWS = [
 # ================= LECTURE 2 =================
 ("SECTION", "Lecture 2 &middot; General Dermatology I &mdash; eczema and dermatitis"),

 ("l2_s050_1.jpg", "Atopic dermatitis",
  "Chronic relapsing itchy eruption. <b>Infants</b> cheeks and extensors; <b>children and adults</b> the flexures. Poorly demarcated erythematous plaques with excoriation and lichenification.<br><span class=pt>&ldquo;It itches all the time and it keeps coming back &mdash; especially in the creases of my elbows and knees.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> Supported by family history, personal atopy, recurrent rash and raised immunoglobulin E (not routinely tested). No routine labs.<br><b>Patch test</b> if atypical, adult-onset or treatment-resistant. <b>Biopsy</b> if atypical or refractory. <b>Culture</b> purulent or crusted lesions; <b>herpes simplex polymerase chain reaction</b> for painful monomorphic erosions.",
  "<b>1st:</b> site-appropriate topical corticosteroid &mdash; low potency or non-steroid on the face, low to medium on the body, applied sparingly. Emollients throughout.<br><b>2nd:</b> tacrolimus or pimecrolimus for sensitive areas; crisaborole; emollient wet wraps for severe flares; hydroxyzine or another antihistamine for itch.<br><b>Severe:</b> refer &mdash; phototherapy, systemic treatment.",
  "Emollient after rinsing. Avoid irritants; fragrance-free skin care. Demonstrate quantity and correct application. Address steroid concerns directly. Written flare and infection action plan. <b>Refer</b> for uncertain diagnosis, moderate-to-severe disease or recurrent infection. Chronic and relapsing, but many improve with age."),

 ("l2_s065_1.jpg", "Dyshidrotic eczema",
  "Deep-seated tapioca-like vesicles on the palms, soles and sides of the fingers.<br><span class=pt>&ldquo;I get these tiny deep blisters on my hands and they itch like mad.&rdquo;</span>",
  "<b>Clinical diagnosis.</b>",
  "<b>1st:</b> high-potency topical corticosteroid.<br><b>2nd:</b> systemic corticosteroid in severe cases.",
  "Avoid triggers and irritants &mdash; detergents, solvents, hair lotions or dyes, acidic foods. Lukewarm water and soap-free cleansers. Dry hands thoroughly. Emollient immediately after drying and as often as possible."),

 ("l2_s070_1.jpg", "Nummular eczema",
  "Discrete coin-shaped plaques, often on the extremities and often in older adults.<br><span class=pt>&ldquo;I have round itchy patches, almost like coins, on my arms and legs.&rdquo;</span>",
  "<b>Clinical.</b> <b>Potassium hydroxide preparation</b> if tinea corporis cannot be ruled out. <b>Bacterial culture</b> if lesions look secondarily infected. <b>Patch testing</b> if chronic or recurrent.",
  "<b>1st:</b> medium to high potency topical corticosteroid for active lesions.<br><b>2nd:</b> antihistamines for itch (hydroxyzine, diphenhydramine); treat secondary bacterial infection if present.",
  "Emollients restore the barrier and prevent recurrence."),

 ("l2_s080_1.jpg", "Irritant contact dermatitis",
  "The commonest form of contact dermatitis. Sharply demarcated in the shape and distribution of the exposure.<br><span class=pt>&ldquo;My hands are raw and cracked &mdash; I wash them all day at work.&rdquo;</span>",
  "<b>Clinical</b>, from known irritant exposure with obvious demarcation and distribution. In insidious cases it becomes a diagnosis of exclusion.",
  "<b>1st:</b> avoid the exposure and repair the barrier with emollients.<br><b>2nd:</b> antihistamines for itch (hydroxyzine, diphenhydramine).",
  "Sleep in cotton gloves after applying a heavy emollient such as petroleum jelly."),

 ("l2_s087_1.jpg", "Allergic contact dermatitis",
  "Well-demarcated rash at the site of contact. With urushiol sap (poison ivy) &mdash; <b>linear vesicular lesions in multiple stages of healing</b> with excoriation.<br><span class=pt>&ldquo;I got these streaks of blisters after I was clearing the yard.&rdquo;</span>",
  "<b>Clinical diagnosis</b> from the history and the typical appearance. <b>Patch testing</b> identifies the allergen.",
  "<b>1st (limited):</b> soothing measures &mdash; oatmeal baths, cool wet compresses, topical astringents &mdash; plus a high-potency topical steroid.<br><b>2nd (extensive):</b> high-dose oral corticosteroid.",
  "Identify and avoid the allergen. Expect lesions in multiple stages of healing at once."),

 ("l2_s092_2.jpg", "Seborrheic dermatitis",
  "Greasy yellow scale on erythema in sebum-rich sites &mdash; scalp, eyebrows, nasolabial folds, ears, central chest.<br><span class=pt>&ldquo;My scalp and the sides of my nose are flaky and greasy and it never fully goes away.&rdquo;</span>",
  "<b>Clinical diagnosis.</b>",
  "<b>1st:</b> topical antifungal &mdash; ketoconazole is the mainstay. Scalp: ketoconazole or selenium sulfide shampoo. Face: ketoconazole cream or lotion.<br><b>2nd:</b> steroids early on to reduce the inflammatory response.",
  "Chronic and relapsing, so repeated and long-term use of medication is often required."),

 ("l2_s097_1.jpg", "Perioral dermatitis",
  "Burning with small erythematous papules around the mouth, <b>sparing the vermilion border</b>. Often follows topical corticosteroid use on the face.<br><span class=pt>&ldquo;I have a burning rash around my mouth &mdash; it started after I used a cream on my face.&rdquo;</span>",
  "<b>Clinical.</b> <b>Potassium hydroxide</b> if tinea or Candida suspected. <b>Bacterial culture</b> if pustules, crusting or drainage. <b>Patch testing</b> if allergic contact dermatitis suspected. <b>Biopsy</b> if persistent, granulomatous or atypical.",
  "<b>1st:</b> <span class=warn>stop facial topical corticosteroids</span> &mdash; continued exposure perpetuates it. Stop non-essential cosmetics and occlusive moisturisers; simplify the routine. Mild disease: topical metronidazole, erythromycin, pimecrolimus or azelaic acid.<br><b>2nd:</b> oral tetracycline or doxycycline for extensive or persistent disease.",
  "<span class=warn>Warn that the eruption may temporarily worsen after corticosteroid withdrawal</span> &mdash; otherwise the patient restarts the steroid and the cycle continues."),

 ("l2_s104_2.jpg", "Diaper dermatitis",
  "Erythema on the <b>convex surfaces</b> of the napkin area. Fold involvement with satellite lesions suggests candidal overgrowth.<br><span class=pt>&ldquo;His bottom is red and sore where the nappy sits.&rdquo;</span>",
  "<b>Clinical.</b> <b>Potassium hydroxide</b> if Candida suspected &mdash; budding yeast or pseudohyphae confirm it. <b>Bacterial culture</b> if purulence, bullae, crusting or perianal disease.",
  "<b>1st:</b> reduce moisture and irritant exposure &mdash; frequent changes, gentle cleansing, air exposure, superabsorbent nappies. Thick zinc oxide or petrolatum barrier at every change.<br><b>2nd:</b> brief low-potency topical corticosteroid for significant inflammation; topical antifungal if candidal.",
  "The whole previous barrier layer does not need scrubbing away if it is still clean."),

 ("l2_s111_3.jpg", "Stasis dermatitis",
  "Pruritic erythematous, violaceous or hyperpigmented patches in the <b>gaiter region</b>, with oedema and signs of chronic venous disease. Usually <b>bilateral</b>.<br><span class=pt>&ldquo;Both my ankles are swollen, itchy and discoloured, and it has been going on for months.&rdquo;</span><br><span class=warn>On darker skin the erythema reads violaceous, grey or deep brown &mdash; palpate for warmth and oedema.</span>",
  "<b>Clinical</b> &mdash; lower-leg dermatitis with oedema and chronic venous disease.<br><b>Ankle-brachial index or toe pressure</b> before substantial compression, to clarify arterial status. <b>Venous duplex ultrasound</b> if reflux, obstruction or deep vein thrombosis suspected.",
  "<b>1st:</b> <b>compression therapy</b> is the cornerstone once arterial circulation is established. Leg elevation, walking, calf exercises, weight management, treat the underlying venous disease. Fragrance-free emollients.<br><b>2nd:</b> short course of an appropriate topical corticosteroid for active inflammation.",
  "<span class=warn>Not cellulitis</span> &mdash; bilateral, chronic, itchy and afebrile. Refer to dermatology, vascular surgery or wound care for refractory disease, venous reflux or ulceration."),

 ("SECTION", "Lecture 2 &middot; Vesiculobullous, papulosquamous, alopecia and xerosis"),

 ("l2_s121_1.jpg", "Bullous pemphigoid",
  "<b>Elderly.</b> Subepidermal split, so <b>tense</b> bullae that do not rupture easily. <b>Nikolsky negative.</b> Mucosal involvement uncommon. May begin with urticarial or oedematous lesions before blistering.<br><span class=pt>&ldquo;I came up in big tight blisters that don't burst easily.&rdquo;</span>",
  "<b>Light microscopy</b> &mdash; neutrophils aligned in a straight narrow row at the dermal-epidermal junction.<br><b>Gold standard:</b> biopsy lesional tissue for histopathology <b>and perilesional tissue for direct immunofluorescence</b>. Serum indirect immunofluorescence or ELISA identifies anti-basement membrane zone antibodies.",
  "<b>1st (mild):</b> ultrapotent topical steroids.<br><b>1st (moderate-severe):</b> oral prednisone or doxycycline. Dapsone is particularly effective with mucous membrane involvement. Low-dose methotrexate is safe and effective in the elderly &mdash; <b>with folic acid</b>.<br><b>2nd (refractory):</b> methotrexate, azathioprine, biologics, intravenous immunoglobulin.",
  "Better prognosis than pemphigus."),

 ("l2_s127_2.jpg", "Pemphigus (vulgaris)",
  "<b>Middle-aged.</b> Intraepidermal split, so <b>flaccid</b> bullae that rupture easily leaving erosions. <b>Nikolsky positive.</b> Mucosal involvement common and often the first site.<br><span class=pt>&ldquo;My mouth is full of sores and the blisters on my skin burst as soon as they form.&rdquo;</span>",
  "<b>Gold standard:</b> biopsy demonstrating <b>acantholysis</b>. Immunofluorescence studies and serum ELISA for pathogenic antibodies are confirmatory.",
  "<b>Urgent treatment needed.</b><br><b>1st:</b> rituximab, or high-dose oral prednisone.<br><b>2nd:</b> steroid given with azathioprine or mycophenolate so the patient can be transitioned off. Antibiotics as needed.<br><b>Supportive:</b> cleansing baths, wet dressings, topical or intralesional glucocorticoids, correction of fluid and electrolyte imbalance.",
  "Worse prognosis than bullous pemphigoid; frequently fatal before corticosteroids."),

 ("l2_s156_1.jpg", "Psoriasis &mdash; plaque",
  "Well-demarcated plaques with thick <b>silvery scale</b>; Auspitz sign on removing scale. Extensor surfaces, scalp, nails. Psoriatic arthritis goes hand in hand with it.<br><span class=pt>&ldquo;Thick scaly patches on my elbows and knees that flake off.&rdquo;</span>",
  "<b>Generally clinical</b>, though biopsy may be needed for definitive diagnosis.",
  "<b>1st (mild):</b> emollients, topical steroids, <b>calcipotriene</b> (vitamin D analogue &mdash; quickest action, caution with nephrotoxicity), ultraviolet B phototherapy for smaller stubborn areas.<br><b>2nd:</b> salicylic acid, coal tar.<br><b>Moderate-severe or after failure:</b> methotrexate (with folic acid), acitretin, apremilast, or a biologic &mdash; etanercept, infliximab, adalimumab, ixekizumab.",
  "Chronic. Methotrexate always needs folic acid supplementation."),

 ("l2_s157_1.jpg", "Psoriasis &mdash; guttate",
  "Numerous small drop-like papules, widespread over the trunk.<br><span class=pt>&ldquo;Hundreds of little scaly spots came up all over my back.&rdquo;</span>",
  "<b>Clinical</b>, as above.",
  "<b>No treatment needed</b>, though phototherapy and topical steroids may be used.",
  "Distinct from plaque psoriasis in its management &mdash; the default is observation."),

 ("l2_s158_1.jpg", "Psoriasis &mdash; pustular",
  "Sterile pustules, often on palms and soles.<br><span class=pt>&ldquo;My palms and soles have come up in little pus-filled spots.&rdquo;</span>",
  "<b>Clinical</b>, as above.",
  "<b>1st:</b> acitretin (<span class=warn>contraindicated in pregnancy</span>) or methotrexate.<br><b>If pregnant:</b> high-potency topical steroids.",
  "Pregnancy changes the treatment entirely &mdash; ask before prescribing."),

 ("l2_s167_1.jpg", "Pityriasis rosea",
  "<b>Herald patch</b> first &mdash; one large salmon-coloured oval, present a week or two alone &mdash; then smaller ovals with a collarette of scale in a <b>Christmas-tree pattern</b> along the skin lines.<br><span class=pt>&ldquo;I had one big patch, then a week later my whole trunk broke out.&rdquo;</span><br><span class=warn>Darker skin: post-inflammatory hyperpigmentation for several months.</span>",
  "<b>Clinical</b>, on the herald patch and the typical pattern.",
  "<b>1st:</b> self-limited &mdash; reassurance. Oral antihistamines and/or cautious topical steroids for itch.<br><b>2nd:</b> ultraviolet B phototherapy or natural sunlight if begun in the first week. Aciclovir for severe cases.",
  "Resolves over about six weeks. The herald patch is what separates it from hives, which appear all at once."),

 ("l2_s175_1.jpg", "Lichen planus",
  "The <b>six Ps</b> &mdash; purple, polygonal, pruritic, planar papules and plaques, shiny, with <b>Wickham striae</b>. Flexor wrists, ankles, oral mucosa. Genital involvement in both sexes.<br><span class=pt>&ldquo;Itchy purple flat-topped bumps on my wrists, and my mouth feels raw.&rdquo;</span>",
  "<b>Biopsy</b> &mdash; <b>band-like infiltration of lymphocytes in the dermis</b>. Also hyperkeratosis without parakeratosis, basal vacuolisation, Civatte bodies, saw-tooth rete ridges.",
  "<b>1st:</b> superpotent topical steroids.<br><b>2nd:</b> topical tacrolimus for oral and vaginal disease; oral steroids in severe cases; PUVA or phototherapy in refractory cases.",
  "Certain medications produce lichenoid reactions &mdash; take a drug history."),

 ("l2_s181_1.jpg", "Lichen simplex chronicus",
  "Thickened lichenified plaque with accentuated skin markings, wherever the patient can reach to scratch. Sustained by the itch-scratch cycle.<br><span class=pt>&ldquo;I scratch it without thinking, especially at night, and now the skin has gone thick and leathery.&rdquo;</span>",
  "<b>Clinical.</b> <b>Biopsy</b> atypical, unilateral, nodular, ulcerated or treatment-resistant plaques to exclude neoplasia.<br><span class=warn>Generalised or unexplained pruritus &rarr; targeted systemic evaluation.</span>",
  "<b>1st:</b> break the itch-scratch cycle &mdash; education, treat the trigger, emollients, behavioural substitution, nail care, safe physical occlusion. Appropriate potent topical corticosteroid for a limited course.<br><b>2nd:</b> calcineurin inhibitor for sensitive sites or maintenance.",
  "Address sleep, anxiety, neuropathic symptoms and the primary dermatosis. <b>Recurrence is common unless the initiating itch is controlled.</b>"),

 ("l2_s136_2.jpg", "Alopecia areata",
  "Discrete smooth round patches of complete hair loss, with <b>exclamation point hairs</b> at the edge. Non-scarring.<br><span class=pt>&ldquo;A round bald patch appeared out of nowhere.&rdquo;</span>",
  "<b>Clinical</b>, strengthened by <b>dermoscopy</b> &mdash; yellow dots, black dots, broken hairs, tapered hairs, short regrowth.<br><b>Scalp biopsy</b> for scarring alopecia, diffuse atypical loss, or persisting uncertainty.",
  "<b>1st (adolescents and adults):</b> intralesional steroids.<br><b>1st (children 10 and under):</b> topical steroids.",
  "<b>Psychological support is one of the most important factors.</b> Support groups may be offered."),

 ("l2_s142_2.jpg", "Androgenetic alopecia",
  "Gradual thinning from follicular miniaturisation &mdash; temporal recession and vertex in men, widened part in women. Non-scarring.<br><span class=pt>&ldquo;My hair has been thinning slowly for years.&rdquo;</span>",
  "<b>Clinical</b>, from history and examination, though additional testing can exclude other causes of alopecia.",
  "<b>Male-pattern:</b> topical minoxidil (mainly effective at the crown); oral finasteride, a 5-alpha-reductase type 2 inhibitor. <b>Works best in combination.</b><br><b>Female-pattern:</b> treatments are limited; oral antiandrogens.",
  "About 2% of men on finasteride report reduced libido and erectile function &mdash; <b>reversible on stopping</b>. <span class=warn>Finasteride is not indicated in women and is contraindicated in pregnancy.</span>"),

 ("l2_s151_2.jpg", "Xeroderma (xerosis)",
  "Dry, rough, cracked skin, worse in winter, typically shins and forearms.<br><span class=pt>&ldquo;My skin is so dry it cracks and stings.&rdquo;</span>",
  "<b>Clinical.</b>",
  "<b>1st:</b> short lukewarm showers, gentle fragrance-free cleanser only where needed, thick ointment or cream within minutes of bathing.<br><b>2nd:</b> petrolatum, ceramide-containing products, humectants such as urea or lactic acid.",
  "<span class=warn>Keratolytics may sting fissured skin.</span> Most improve with consistent barrier care, but <b>recurrence is expected while environmental exposure, ageing or systemic risk persists</b>."),
]

ROWS += [
 # ================= LECTURE 3 =================
 ("SECTION", "Lecture 3 &middot; Dermatology II &mdash; reactive and immune-mediated"),

 ("l3_s006_3.jpg", "Erythema multiforme",
  "<b>Target lesions</b> with three concentric zones &mdash; central dusky or necrotic area, pale oedematous ring, outer erythematous rim. Acral distribution, beginning on the extremities.<br><span class=pt>&ldquo;I have these bullseye-looking spots on my hands and arms.&rdquo;</span>",
  "<b>Clinical diagnosis</b>; biopsy if uncertain.<br>Herpes simplex polymerase chain reaction, Mycoplasma serology. If erythema multiforme major or systemic concern: <b>complete blood count, comprehensive metabolic panel, liver function tests</b>.",
  "<b>1st:</b> supportive &mdash; analgesia, antihistamines, wound care. <b>Discontinue the offending drug immediately.</b> Topical corticosteroids for localised lesions. Oral aciclovir or valaciclovir if herpes-triggered.<br><b>2nd (recurrent):</b> suppressive antiviral therapy, aciclovir 400&nbsp;mg twice daily.",
  "<b>Herpes simplex virus triggers over 50% of cases.</b> Hospitalise if erythema multiforme major with poor oral intake or extensive mucosal disease."),

 ("l3_s014_1.jpg", "Dermatitis herpetiformis",
  "Intensely pruritic papules, vesicles and urticarial plaques, <b>symmetrically</b> on knees, elbows, buttocks and back, grouped in a herpetiform pattern. Often bloating and diarrhoea.<br><span class=pt>&ldquo;Unbelievably itchy blisters on my elbows and knees, both sides, and my stomach has been off.&rdquo;</span>",
  "<b>Gold standard: perilesional direct immunofluorescence &mdash; granular immunoglobulin A at the dermal papillae.</b><br>Also immunoglobulin A anti-tissue transglutaminase, anti-endomysial antibody, small bowel biopsy.<br><span class=warn>She flagged this in class: most of this block is clinical diagnosis, so a disease with a distinctive test is high-yield.</span>",
  "<b>1st:</b> dapsone for rapid symptom control.<br><b>Cornerstone:</b> a strict lifelong gluten-free diet, which is what allows dapsone to be reduced or stopped over one to two years.",
  "<b>Screen every patient for coeliac disease.</b> Also autoimmune thyroid disease and T-cell lymphoma. Rare &mdash; 11 to 75 per 100,000, northern European descent, ages 30 to 40."),

 ("l3_s021_2.jpg", "Acanthosis nigricans",
  "Velvety hyperpigmented thickening of flexural skin &mdash; neck, axillae, groin.<br><span class=pt>&ldquo;The skin on my neck has gone dark and velvety and it won't wash off.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> Then <b>haemoglobin A1c, fasting insulin, lipid panel</b>, polycystic ovarian syndrome workup.",
  "<b>1st:</b> treat the underlying cause &mdash; insulin resistance. 5 to 10% weight loss improves it. Metformin.<br><b>2nd:</b> topical retinoids for cosmetic improvement.",
  "<b>A metabolic warning sign, not a hygiene problem.</b> <span class=warn>Sudden onset in an adult &rarr; urgent evaluation for gastrointestinal malignancy, especially gastric adenocarcinoma.</span>"),

 ("l3_s027_2.jpg", "Epidermolysis bullosa",
  "Blistering and skin fragility from minimal trauma, evident at or shortly after birth. Caused by a <b>mutation in structural proteins</b>.<br><span class=pt>&ldquo;His skin blisters and tears wherever he is handled.&rdquo;</span>",
  "<b>Gold standard: transmission electron microscopy with immunofluorescence antigen mapping.</b> Supported by a genetic panel and nutritional labs.",
  "<b>Supportive.</b> Wound care, nutrition, infection control, pain management.",
  "<b>Referral to essentially every specialty</b> given the multisystem burden. Early palliative care integration, genetics counselling and family support in severe forms such as Herlitz junctional disease."),

 ("l3_s035_1.jpg", "Urticaria",
  "Transient pruritic wheals, with or without angio-oedema. <b>An individual wheal resolves within 24 hours</b>, blanches fully and migrates.<br><span class=pt>&ldquo;Itchy welts come up and move around, and each one is gone by the next day.&rdquo;</span>",
  "<b>Clinical.</b> <span class=warn>Biopsy if lesions persist beyond 24 hours &mdash; that suggests urticarial vasculitis.</span><br>Thyroid-stimulating hormone, complement C4, tryptase, specific immunoglobulin E.",
  "<b>1st:</b> second-generation antihistamine &mdash; cetirizine, loratadine, fexofenadine. Short oral prednisone 40&ndash;60&nbsp;mg for 5 days in severe acute disease. <span class=warn>Intramuscular epinephrine 0.3&nbsp;mg immediately for anaphylaxis.</span><br><b>2nd (chronic):</b> scheduled non-sedating antihistamine up to <b>4&times; standard dose</b>; add an H2 blocker; then omalizumab 300&nbsp;mg every 4 weeks; ciclosporin.",
  "Acute versus chronic is defined at <b>six weeks</b>. About half of chronic urticaria resolves within a year, and over half of cases have no identifiable trigger."),

 ("l3_s041_1.jpg", "Erythema nodosum",
  "Tender erythematous nodules, <b>bilateral on the anterior shins</b>, that <b>do not ulcerate</b>. The commonest panniculitis. Often preceded by fever and arthralgia.<br><span class=pt>&ldquo;Painful red lumps came up on both my shins and I ached all over first.&rdquo;</span>",
  "<b>Clinical</b>; deep incisional biopsy if atypical (septal panniculitis without vasculitis).<br><b>Antistreptolysin O titre, chest radiograph, tuberculin or interferon gamma test, inflammatory markers</b>, colonoscopy, pregnancy test where relevant.",
  "<b>1st:</b> rest, leg elevation, compression stockings, a nonsteroidal anti-inflammatory drug.<br><b>2nd:</b> potassium iodide for idiopathic and recurrent disease; short corticosteroid course once infection is excluded.",
  "<b>It is a reaction pattern, not an isolated disease</b> &mdash; identifying and treating the trigger is the point. Löfgren syndrome (with ankle arthritis and hilar nodes) has the best sarcoid prognosis, over 90% remitting."),

 ("l3_s047_1.jpg", "Granuloma annulare",
  "Annular ring of flesh-coloured or erythematous papules, commonly dorsal hands and feet. <b>No scale on the border</b> &mdash; which is what separates it from tinea.<br><span class=pt>&ldquo;A ring of little bumps on the back of my hand. It doesn't itch.&rdquo;</span>",
  "<b>Clinical</b>; biopsy for confirmation shows palisading granulomas with central necrobiosis and mucin.",
  "<b>Localised:</b> benign and self-limiting &mdash; treat for cosmesis or discomfort. Intralesional or topical corticosteroid.<br><b>Generalised:</b> phototherapy or systemic therapy via dermatology.",
  "Localised disease is benign and about <b>half resolve within two years</b>; no malignant potential. <span class=warn>Generalised disease in an adult over fifty &rarr; screen for diabetes, thyroid disease, dyslipidaemia and lymphoma.</span>"),

 ("l3_s056_2.jpg", "Pyoderma gangrenosum",
  "Rapidly expanding painful ulcer with an <b>undermined violaceous border</b>, beginning as a pustule or nodule. Lower extremities most common. <b>Pathergy</b> &mdash; it worsens with trauma.<br><span class=pt>&ldquo;A small spot turned into a big painful ulcer within days, and it got worse after they cleaned it out.&rdquo;</span>",
  "<b>A diagnosis of exclusion &mdash; no gold standard test.</b> Biopsy the ulcer EDGE and take wound cultures to exclude malignancy and infection. Serum protein electrophoresis, antineutrophil cytoplasmic and antinuclear antibodies, colonoscopy.",
  "<b>Wound care (critical):</b> <span class=warn>avoid debridement &mdash; pathergy worsens the ulcer.</span> Moist dressings, non-adherent contact layers. Topical tacrolimus or clobetasol to the wound edges for pain.<br><b>1st systemic:</b> prednisone 0.5&ndash;1&nbsp;mg/kg/day for acute rapid progression, or ciclosporin 3&ndash;5&nbsp;mg/kg/day.<br><b>2nd:</b> infliximab 5&nbsp;mg/kg &mdash; approved with inflammatory bowel disease.",
  "<span class=warn>Do not debride.</span> Screen for inflammatory bowel disease (25&ndash;50%), haematologic malignancy, monoclonal gammopathy, rheumatoid arthritis. The bullous variant associates with acute myeloid leukaemia."),

 ("l3_s063_1.jpg", "Acne rosacea",
  "Persistent central facial erythema with flushing and telangiectasias, and <b>no comedones</b> &mdash; which is what separates it from acne vulgaris. Four subtypes: erythematotelangiectatic (commonest), papulopustular, phymatous, ocular.<br><span class=pt>&ldquo;My face goes red and burns, especially with wine or hot drinks.&rdquo;</span>",
  "<b>Clinical.</b> <b>Antinuclear antibody</b> if lupus is a consideration &mdash; it helps <b>rule out</b> autoimmune disease; a positive result only means more testing is needed.",
  "<b>1st: topical metronidazole.</b><br><b>Alternative:</b> azelaic acid &mdash; effective but <span class=warn>more drying, and these patients already have an impaired barrier</span>. Ivermectin 1% cream is superior where there is a Demodex burden. Brimonidine for erythema. Sub-antimicrobial doxycycline; isotretinoin for refractory disease.",
  "Chronic &mdash; therapy controls rather than cures. Trigger diary, gentle non-irritating skincare, daily sun protection. <span class=warn>Ocular rosacea with visual symptoms &rarr; urgent ophthalmology.</span>"),

 ("l3_s071_1.jpg", "Hyperhidrosis",
  "<b>Primary focal:</b> bilateral, focal (palms, soles, axillae), adolescent onset, <b>absent during sleep</b>.<br><b>Secondary:</b> generalised, may be asymmetric, can occur at night.<br><span class=pt>&ldquo;My hands drip so much I smudge everything I write.&rdquo;</span>",
  "<b>Clinical + Hyperhidrosis Disease Severity Score.</b> Minor's starch-iodine test maps the distribution; gravimetric measurement quantifies it.<br><span class=warn>Generalised or nocturnal &rarr; secondary workup: 24-hour urine metanephrines and catecholamines, thyroid-stimulating hormone.</span>",
  "<b>1st:</b> aluminium chloride topically at night.<br><b>2nd:</b> glycopyrronium 2.4% cloth once daily (axillary), or an oral anticholinergic.<br><b>3rd:</b> botulinum toxin A; microwave thermolysis.<br><b>Last resort:</b> endoscopic thoracic sympathectomy for refractory palmar disease.",
  "<b>It is a medical condition, not poor hygiene or anxiety.</b> Quality-of-life impairment is comparable to severe psoriasis. Botulinum toxin lasts 3&ndash;6 months and needs repeating; it can be cost-prohibitive. Moisture-wicking clothing; set realistic expectations."),

 ("SECTION", "Lecture 3 &middot; Severe drug reactions and photodermatology"),

 ("l3_s081_2.jpg", "Stevens-Johnson syndrome",
  "Prodrome of fever, malaise and upper respiratory symptoms <b>1&ndash;3 days before</b> the skin findings. Painful erythematous macules and target lesions starting on the trunk. <b>Mucosal erosions &mdash; oral, ocular, genital &mdash; in over 90%.</b> Nikolsky positive. <b>Epidermal detachment under 10% body surface.</b><br><span class=pt>&ldquo;I had flu symptoms, then my mouth and eyes became raw and my skin started peeling.&rdquo;</span>",
  "<b>Pathognomonic: punch biopsy showing full-thickness epidermal necrosis with dermal-epidermal junction separation.</b><br>Complete blood count, metabolic panel, liver function, urea and creatinine. Blood cultures if secondary infection suspected. Chest radiograph. <b>Ophthalmology with slit-lamp.</b> SCORTEN scoring.",
  "<b>1st and most important: withdraw the causative drug immediately</b> &mdash; earlier withdrawal is strongly associated with improved survival.<br>Burn unit or intensive care. Aggressive fluids, temperature control, non-adhesive dressings, nasogastric nutrition, infection surveillance. <span class=warn>Avoid silver sulfadiazine (sulfonamide cross-reaction). Antibiotic prophylaxis is NOT recommended.</span><br><b>2nd:</b> intravenous immunoglobulin 1&nbsp;g/kg/day &times;3 or ciclosporin 3&ndash;5&nbsp;mg/kg/day; etanercept emerging.",
  "1&ndash;7 per million per year &mdash; <b>uncommon but deadly, so it has to be known.</b> Culprits: aromatic anticonvulsants, sulfonamides, allopurinol, oxicam nonsteroidals, nevirapine. <b>Lifelong avoidance of the drug class, medical alert bracelet, counsel first-degree relatives on shared genetic risk</b> (HLA-B*15:02 with carbamazepine, HLA-B*58:01 with allopurinol)."),

 ("l3_s086_1.jpg", "Toxic epidermal necrolysis",
  "The same spectrum, at its severe end. High fever, stinging eyes, painful swallowing 1&ndash;3 days before. Painful erythema &rarr; flaccid bullae &rarr; confluent detachment <b>over 30% body surface</b>, Nikolsky positive, &ldquo;wet parchment&rdquo;. Mucosal erosions nearly universal.<br><span class=pt>&ldquo;My skin is coming off in sheets.&rdquo;</span>",
  "As for Stevens-Johnson syndrome. <b>SCORTEN within 24 hours of admission and repeated on day 3</b> &mdash; age over 40, malignancy, heart rate over 120, detachment over 10%, urea over 28&nbsp;mg/dL, bicarbonate under 20&nbsp;mEq/L, glucose over 252&nbsp;mg/dL. Score 5+ &rarr; 90% predicted mortality.",
  "<b>Burn unit or intensive care admission is mandatory.</b> Immediate withdrawal of all suspect drugs. Fluid resuscitation as for major burns. Non-adhesive biological dressings. Early enteral feeding.<br><b>1st drug: ciclosporin 3&ndash;5&nbsp;mg/kg/day &mdash; strongest current evidence</b>, early initiation preferred.<br><b>2nd:</b> intravenous immunoglobulin, etanercept. Opioids and gabapentin for pain.",
  "Mortality 30&ndash;35%. <span class=warn>Antibiotic prophylaxis is NOT recommended</span> &mdash; treat infections when confirmed. Palliative care involvement at SCORTEN 5 or more. Survivors face sicca syndrome, lung disease and psychological trauma."),

 ("l3_s092_1.jpg", "Sunburn",
  "<b>First degree:</b> erythema, warmth, tenderness, no blistering, resolving in 3&ndash;5 days with desquamation.<br><b>Second degree:</b> blistering, intense pain, oedema, 1&ndash;2 weeks.<br>Onset 3&ndash;5 hours after exposure, peaking at 12&ndash;24 hours. &ldquo;Sun poisoning&rdquo; &mdash; fever, chills, nausea, dehydration &mdash; with large body surface involvement.",
  "<b>Clinical.</b>",
  "<b>1st:</b> cool compresses and cool (not cold) water immersion. <b>Nonsteroidal anti-inflammatory drugs started early</b> reduce prostaglandin-mediated pain. Oral hydration; intravenous fluids if severe.<br><b>2nd:</b> topical moisturisers &mdash; aloe vera, soy &mdash; soothing but do not alter healing. Topical steroid has limited evidence, possibly if within 6 hours.",
  "<span class=warn>Do not pop blisters &mdash; intact blisters are protective.</span> Hospitalise for severe blistering over 20% body surface, systemic toxicity, or extremes of age. Broad-spectrum SPF 30+, reapply every 2 hours; avoid 10&nbsp;AM&ndash;4&nbsp;PM; <b>tanning beds are Group 1 carcinogens</b>."),

 ("l3_s097_1.jpg", "Drug-induced photosensitivity",
  "<b>Phototoxicity:</b> non-immunologic, dose-dependent, occurs on <b>first</b> exposure, within hours, looks like an exaggerated sunburn confined to exposed skin.<br><b>Photoallergy:</b> immunologic type IV, dose-independent, needs sensitisation, eczematous and pruritic, <b>extends beyond sun-exposed skin</b>, can persist after the drug stops.<br><span class=pt>&ldquo;I burned badly after barely any sun since starting that antibiotic.&rdquo;</span>",
  "Thorough drug history including over-the-counter and topical products.<br><b>Phototesting</b> &mdash; minimal erythema dose to ultraviolet A and B before and after drug withdrawal.<br><b>Gold standard for photoallergy: photopatch testing</b> &mdash; duplicate sets, one irradiated with ultraviolet A at 5&nbsp;J/cm². Reaction on the irradiated patch <b>only</b> = photoallergy; <b>both</b> = contact allergy.",
  "<b>1st:</b> identify and discontinue or substitute the offending agent where feasible. Strict photoprotection &mdash; SPF 50+ broad-spectrum, physical blockers (zinc oxide, titanium dioxide).<br><b>2nd:</b> phototoxicity &mdash; supportive care. Photoallergy &mdash; topical or short systemic corticosteroid, antihistamine. Persistent light reaction &mdash; narrowband ultraviolet B desensitisation.",
  "Phototoxic drugs: tetracyclines (especially doxycycline), fluoroquinolones, amiodarone, thiazides, furosemide, voriconazole, nonsteroidals, psoralens, St John's Wort. Photoallergic: sunscreen chemicals (oxybenzone), sulfonamides, topical antihistamines, phenothiazines. Avoid medication during peak sun hours."),

 (None, "Photodermatitis (phytophotodermatitis)",
  "Furanocoumarins from limes, celery, parsley, wild parsnip or fig plus ultraviolet A. <b>Linear or streaked hyperpigmentation</b> after lime juice and sun &mdash; &ldquo;margarita dermatitis&rdquo;. Painful blistering in the acute phase.<br>Berloque dermatitis: drip-pattern hyperpigmentation on the neck from bergamot oil.<br>Chronic actinic dermatitis: persistent eczematous eruption in chronically exposed skin in older males.",
  "Detailed exposure history &mdash; plants, topicals, fragrances, medications. <b>Photopatch testing</b> for photocontact allergy. Antinuclear antibody panel if lupus suspected. Biopsy if uncertain.<br><span class=warn>Photodermatitis spares the nasolabial folds; seborrhoeic dermatitis involves them.</span>",
  "<b>1st:</b> avoid the contactant and ultraviolet exposure concurrently. Acute blistering &mdash; cool compresses, wound care, mid-potency topical corticosteroid.<br><b>2nd:</b> hyperpigmentation &mdash; reassurance, it fades over months; hydroquinone or azelaic acid if persistent. Chronic actinic dermatitis &mdash; potent steroids, tacrolimus, hydroxychloroquine, narrowband ultraviolet B or PUVA, azathioprine.",
  "Recognise photosensitising plants, especially in landscaping, gardening and food preparation. <b>Wash skin immediately after plant contact before sun exposure.</b> Year-round sun protection prevents the pigment darkening further."),

 ("l3_s103_1.jpg", "Polymorphous light eruption",
  "The commonest idiopathic photodermatosis (10&ndash;20% of the population). 2&ndash;5&nbsp;mm erythematous papules on décolletage, forearms and dorsal hands, appearing 30 minutes to hours after ultraviolet exposure, <b>in the first sunny days of spring</b>. <b>Spares chronically exposed areas.</b> Resolves in 7&ndash;10 days without scarring; &ldquo;hardening&rdquo; by late summer.<br><span class=pt>&ldquo;Every spring the first proper sun brings out an itchy rash, and it settles by July.&rdquo;</span>",
  "<b>Largely clinical</b> &mdash; history and morphology.<br><b>Antinuclear antibody panel is MANDATORY to exclude lupus</b>, especially anti-Ro/SSA and anti-La/SSB. Phototesting reproduces the eruption in 50&ndash;60%. Biopsy shows a perivascular lymphocytic infiltrate with dermal oedema &mdash; supportive, not pathognomonic.",
  "<b>1st (acute):</b> avoid further ultraviolet exposure, cool compresses, moderate-potency topical corticosteroid, oral antihistamine. Short prednisolone 0.5&nbsp;mg/kg/day &times;4&ndash;5 days for severe episodes.<br><b>1st (preventive): prophylactic narrowband ultraviolet B, 3&times;/week for 5 weeks in spring &mdash; induces tolerance and is the most effective preventive strategy.</b><br><b>2nd:</b> hydroxychloroquine 200&nbsp;mg twice daily for refractory cases.",
  "Broad-spectrum SPF 50+ including ultraviolet A blockers. Recurs each spring and often improves with summer hardening. Strong hereditary component &mdash; up to 50% family concordance."),

 ("l3_s108_1.jpg", "Solar lentigo <span class=\"dup\">also Lecture 8</span>",
  "Well-defined light-to-dark brown macules with <b>irregular borders that coalesce at sites of severe sunburn</b>, from under 1&nbsp;mm to several centimetres, on chronically exposed skin. <b>90% of people by age 50.</b><br><span class=pt>&ldquo;Age spots on the backs of my hands and my shoulders.&rdquo;</span>",
  "<b>Dermoscopy</b> &mdash; finger-like projections and a &ldquo;moth-eaten&rdquo; border.<br><span class=warn>Biopsy if atypical or uncertain on dermoscopy, to exclude lentigo maligna</span> (asymmetric, irregular border and colour, structureless pigment). Reflectance confocal microscopy where biopsy is deferred.",
  "<b>Treatment is not necessary.</b> Cosmetic removal by preference:<br><b>1st:</b> cryotherapy (5&ndash;10 second freeze), or quality-switched Nd:YAG, intense pulsed light or fractional laser.<br><b>2nd:</b> topical hydroquinone 2&ndash;4%, azelaic acid, kojic acid, retinoids, tranexamic acid &mdash; slower but less post-procedure pigmentation risk. Chemical peels.",
  "Benign, <b>but monitor for change</b>. Daily SPF 30+ prevents new lesions. Annual full-body skin examination. Associated with actinic keratosis, squamous and basal cell carcinoma, and melanoma &mdash; it marks cumulative sun damage. Over time may progress into lichenoid keratoses."),

 ("l3_s117_3.jpg", "Actinic keratosis",
  "Rough, scaly, erythematous papules and plaques on sun-exposed skin &mdash; face, scalp, dorsal hands, forearms. Skin-coloured to red-brown, <b>&ldquo;sandpaper&rdquo; texture on palpation</b>, typically 2&ndash;10&nbsp;mm.<br><span class=pt>&ldquo;Rough scaly spots I can feel better than I can see.&rdquo;</span>",
  "<b>Clinical.</b> <span class=warn>Biopsy if indurated, ulcerated, tender or bleeding &mdash; concerning for invasive squamous cell carcinoma.</span>",
  "<b>1st (lesion-directed):</b> cryotherapy, 2&ndash;3 freeze-thaw cycles &mdash; standard of care for isolated lesions. Shave excision or curettage with electrodessication.<br><b>1st (field-directed, for multiple or confluent):</b> 5-fluorouracil 5% for 2&ndash;4 weeks; imiquimod 3.75% or 5% twice weekly &times;16 weeks; photodynamic therapy; tirbanibulin 1%; diclofenac 3% gel for mild disease.",
  "<b>Field cancerization</b> &mdash; the clinically normal skin around a lesion already carries mutations, which is why confluent disease gets field therapy. 0.025&ndash;16% annual transformation risk per lesion. Organ transplant recipients carry 65&times; the risk. Hypertrophic lesions have higher malignant potential."),

 ("l3_s115_1.jpg", "Dermatoheliosis (photoaging)",
  "Coarse deep wrinkles, leathery rough texture, mottled dyspigmentation, telangiectasias, persistent erythema. <b>Cutis rhomboidalis nuchae</b> on the posterior neck is the classic marker of severe photoaging. Sun-protected skin looks far younger.<br><span class=pt>&ldquo;One side of my face looks a decade older &mdash; the side that was by the car window.&rdquo;</span>",
  "<b>Clinical</b> &mdash; chronic sun exposure with the characteristic distribution.<br>Biopsy confirms <b>solar elastosis</b>, the hallmark. Dermoscopy for individual lesions. Ultraviolet photography quantifies subclinical damage. Genetic testing if xeroderma pigmentosum suspected. <b>Annual full-body skin examination.</b>",
  "<b>1st: tretinoin 0.025&ndash;0.1% &mdash; the only agent approved by the Food and Drug Administration for photoaging.</b> Start low, titrate; expect initial retinoid dermatitis; minimum 6&ndash;12 months for visible results.<br><b>2nd:</b> vitamin C 10&ndash;20%, niacinamide, hydroquinone 2&ndash;4%, azelaic/kojic/tranexamic acid. Chemical peels, ablative or non-ablative laser resurfacing, intense pulsed light, radiofrequency, microneedling.",
  "<b>Broad-spectrum SPF 30+ daily is the single most evidence-supported intervention.</b> Apply as the last skincare step before makeup, 2&nbsp;mg/cm² (about a teaspoon for face and neck), reapply every 2 hours. Largely preventable; established change can still be meaningfully improved. <b>Tanning is not healthy &mdash; a tan is a UV injury response.</b>"),
]

ROWS += [
 # ================= LECTURE 4 =================
 ("SECTION", "Lecture 4 &middot; Cutaneous Bacterial Infections"),

 ("l4_s004_1.jpg", "Acne vulgaris",
  "Polymorphic. <b>Comedones are the hallmark</b> &mdash; open (blackheads) and closed (whiteheads), non-inflammatory &mdash; plus inflammatory papules, pustules and nodules. Face, neck, chest, upper back, upper arms. Systemic symptoms absent.<br><span class=pt>&ldquo;Spots that keep coming, and they flare before my period.&rdquo;</span>",
  "<b>Clinical.</b> Culture only if there is no response to treatment.<br>Pre-treatment assessment: type and severity, skin type, scarring, menstrual and hyperandrogenism history, current regimen, psychological impact.",
  "<b>Comedonal:</b> topical retinoid (adapalene, tazarotene, tretinoin); azelaic or salicylic acid if not tolerated.<br><b>Mild papulopustular:</b> topical antimicrobial + retinoid, <i>or</i> benzoyl peroxide + topical antibiotic.<br><b>Moderate:</b> topical retinoid + <b>oral antibiotic</b> (doxycycline, minocycline; sarecycline; erythromycin if tetracycline contraindicated) + benzoyl peroxide.<br><b>Severe nodular:</b> the same triple, <i>or</i> <b>oral isotretinoin monotherapy</b>, 16&ndash;20 weeks.<br><b>Hormonal:</b> combined oral contraceptive for hyperandrogenism or unresponsive disease.",
  "<b>Benzoyl peroxide with every antibiotic</b> to cut resistance; oral courses 3&ndash;4 months only. Separate tretinoin and benzoyl peroxide by <b>3+ hours</b>. Wash no more than twice daily, gentle cleanser, warm not hot water. Non-comedogenic products. Improvement takes <b>4&ndash;6 weeks</b>; back and chest 3&ndash;4 months. <span class=warn>Isotretinoin: pregnancy tests before, monthly, and 5 weeks after; iPledge; one month dispensed at a time; two forms of contraception; no blood donation.</span>"),

 ("l4_s041_1.jpg", "Folliculitis",
  "Small papules or pustules on an erythematous base, each <b>pierced by a central hair</b>. Scalp, thighs, trunk, axilla, inguinal area. Abrupt eruption, afebrile, no systemic involvement.<br><span class=pt>&ldquo;Little pimples with a hair coming out of the middle.&rdquo;</span>",
  "<b>History and clinical manifestations.</b><br><b>Resistant cases:</b> culture and Gram stain from an unroofed pustule; potassium hydroxide wet mount using a <b>plucked hair</b> to exclude dermatophyte folliculitis; nasal swab of patient and family for Staphylococcus aureus colonisation; biopsy.",
  "<b>1st:</b> moist heat, antibacterial soaps, good glycaemic control, good skin hygiene, loose clean clothing. Mild infection &mdash; topical mupirocin, clindamycin or erythromycin.<br><b>Recurrent (carrier state):</b> mupirocin ointment in the nasal vestibule twice daily &times;5 days.<br><b>Extensive:</b> oral cephalexin or dicloxacillin. <b>If MRSA:</b> trimethoprim-sulfamethoxazole, ciprofloxacin or linezolid.",
  "Instruct the patient <b>not to squeeze pustules</b>. Superficial pustules rupture and drain spontaneously; deep lesions may be incised and drained. Risk factors: obesity, poor hygiene, occlusive clothing, heat and humidity, immunocompromise, corticosteroids, diabetes, nasal carriage."),

 ("l4_s050_1.jpg", "Pseudomonas (&ldquo;hot tub&rdquo;) folliculitis",
  "Follicular papules, vesicles and pustules that can crust, primarily on <b>trunk, extremities and buttocks</b>, <b>sparing face, neck, soles and palms</b>. Onset <b>8 hours to 5 days</b> after exposure. Pruritic or tender.<br><span class=pt>&ldquo;A day after the hot tub I broke out in an itchy rash everywhere my swimsuit covered.&rdquo;</span>",
  "<b>Usually clinical.</b> Bacterial culture from a pustule or a sample of the contaminated water if unclear or treatment-resistant.",
  "<b>1st:</b> most cases resolve without specific treatment, clearing in <b>2&ndash;10 days</b>. Dilute acetic acid 5% wet dressing &mdash; 3 tablespoons in a pint of water, 20 minutes, 2&ndash;4&times; daily.<br><b>2nd:</b> ciprofloxacin for widespread or resistant cases.",
  "<span class=warn>Showering after contact does NOT prevent infection.</span> Continuous water filtration to remove dead skin, frequent monitoring of chlorine levels, frequent changing of the water. Caused by <b>Pseudomonas aeruginosa</b>, a Gram-negative organism, from inadequate chlorination."),

 ("l4_s054_1.jpg", "Pseudofolliculitis barbae",
  "<b>Foreign body reaction, not an infection.</b> The cut hair curves into the follicular wall and re-penetrates the skin, forming a tender red papule with a <b>central hair shaft</b>. Commonly in Black males with tightly curled facial hair, or anyone who shaves curlier hair.<br><span class=pt>&ldquo;I get sore ingrown bumps every time I shave.&rdquo;</span>",
  "<b>Clinical diagnosis.</b>",
  "<b>1st:</b> stop shaving if possible; clean razors; <span class=warn>avoid &ldquo;lift-and-cut&rdquo; razor systems</span>; mild razor angles, single or at most double blades.<br><b>Alternatives:</b> chemical depilatories; laser-assisted permanent hair removal.<br><b>2nd (topical):</b> tretinoin relieves hyperkeratosis; mild corticosteroid for inflammation; eflornithine cream reduces facial hair; topical clindamycin, benzoyl peroxide or erythromycin to reduce colonisation. Oral tetracycline.",
  "The shaving technique itself has to change &mdash; treating the papules alone will not resolve it. Secondary infection can produce pustules and abscess."),

 ("l4_s060_1.jpg", "Furuncle",
  "A painful, fluctuant, erythematous nodule &mdash; a deep abscess of a hair follicle and adjacent subcutaneous tissue. Firm tender nodule with a <b>single opening</b> and a surrounding zone of erythema; often fluctuant, may drain spontaneously. Back of neck, face, axillae, buttocks.<br><span class=pt>&ldquo;A painful boil on the back of my neck.&rdquo;</span>",
  "<b>Clinical appearance.</b> Organism identified by <b>aspiration or incision and drainage</b>.",
  "<b>1st:</b> warm compresses are usually sufficient for small furuncles. <b>No antibiotics if afebrile with a single lesion under 5&nbsp;mm.</b><br><b>Oral antibiotics if:</b> a lesion under 5&nbsp;mm fails drainage, a single lesion is over 5&nbsp;mm, expanding cellulitis, immunocompromise, or endocarditis risk. Empiric: dicloxacillin or cephalexin. <b>If MRSA:</b> trimethoprim-sulfamethoxazole, clindamycin or doxycycline.<br>Incise and drain large furuncles and <b>culture the material</b>.",
  "Endocarditis prophylaxis for at-risk patients. Recurrent furunculosis &mdash; address <b>obesity, diabetes and nasal Staphylococcus aureus carriage</b>."),

 ("l4_s060_2.jpg", "Carbuncle",
  "<b>Two or more confluent furuncles with separate heads.</b> Extremely painful. Several loculated abscesses, superficial pustules, necrotic plugs and <b>sieve-like openings</b> draining purulent material. <b>Systemic symptoms &mdash; malaise, chills, fever &mdash; are more common than with a furuncle.</b><br><span class=pt>&ldquo;A cluster of boils that have joined together, and I feel unwell with it.&rdquo;</span>",
  "<b>Clinical appearance</b>; organism via aspiration or incision and drainage.",
  "<b>1st: incision and drainage is the mainstay of therapy.</b> Endocarditis prophylaxis for at-risk patients.<br><b>Oral antibiotics:</b> dicloxacillin or cephalexin. <b>If MRSA:</b> trimethoprim-sulfamethoxazole, doxycycline or clindamycin.",
  "Differential: cystic acne, folliculitis, hidradenitis suppurativa."),

 ("l4_s074_1.jpg", "Hidradenitis suppurativa",
  "Also called <b>acne inversa</b>. Inflammation of cutaneous <b>apocrine</b> glands &mdash; axilla (most common), groin, breasts, perineum. Recurrent painful or suppurative lesions <b>more than twice in 6 months</b>. Nodules, sinus tracts, abscesses, atrophic or meshlike scarring, and the <b>double comedone</b> (a blackhead with two or more openings).<br><span class=pt>&ldquo;Painful lumps under my arms that keep coming back and now they leak.&rdquo;</span>",
  "<b>Primarily clinical.</b> <b>Three key elements: typical lesions + characteristic distribution (axilla and groin) + recurrence more than twice in 6 months.</b><br>Biopsy is not usually required; it shows follicular occlusion by keratinous material, folliculitis and apocrine gland destruction.",
  "<b>Prevention:</b> avoid heat, daily antibacterial soap / chlorhexidine / benzoyl peroxide wash, weight loss, avoid constrictive clothing and friction, <b>smoking cessation is essential</b>, laser hair removal.<br><b>1st:</b> mild topical steroid with topical antibiotic (clindamycin, erythromycin).<br><b>2nd:</b> intralesional triamcinolone for draining sinuses; oral prednisone; oral retinoid; spironolactone; combined oral contraceptive.<br><b>3rd:</b> infliximab for disease unresponsive to corticosteroids. Analgesia: codeine, then fentanyl patch for resistant pain.<br><b>Definitive:</b> incise and drain large fluctuant cysts; <b>wide excision gives the best chance of permanent cure</b>.",
  "Long-term systemic antibiotics have often poor outcomes. Predisposing: hot weather, perspiration, obesity, apocrine duct obstruction, secondary infection, smoking."),

 ("l4_s083_1.jpg", "Erythrasma",
  "Chronic superficial infection of intertriginous skin by <b>Corynebacterium minutissimum</b>, invading the upper third of the stratum corneum under heat and humidity. Usually asymptomatic, may be pruritic. Inner thighs, crural region, scrotum, and <b>between the 4th and 5th toes</b>. <b>Diabetics are high risk.</b><br><span class=pt>&ldquo;A brownish patch in my groin that doesn't itch much.&rdquo;</span>",
  "<b>Gold standard: &ldquo;coral-red&rdquo; fluorescence under a Wood's lamp (ultraviolet light).</b>",
  "<b>1st (localised):</b> topical erythromycin or clindamycin.<br><b>Widespread:</b> oral erythromycin or clarithromycin.<br><b>If yeast also present:</b> add an antifungal cream (miconazole).",
  "Keep the area clean and dry. Avoid excessive heat or moisture. Maintain a healthy body weight and good hygiene. Differential: cutaneous candidiasis, contact dermatitis, psoriasis, tinea."),

 ("l4_s087_1.jpg", "Impetigo &mdash; non-bullous",
  "The more common form. A macule rapidly becomes a vesicle or pustule and ruptures; serous contents dry to a <b>honey-coloured adherent crust</b> over an erosion. Face and extremities. Spreads by extension and self-inoculation from scratching. <b>Regional lymphadenopathy common.</b> <b>VERY contagious.</b><br><span class=pt>&ldquo;Golden crusty sores around his nose and mouth that keep spreading.&rdquo;</span>",
  "<b>Clinical appearance.</b><br><b>Culture if:</b> high risk for MRSA (health-care worker, teacher), or acute post-streptococcal glomerulonephritis is present.",
  "<b>1st (topical, limited non-bullous):</b> <b>mupirocin ointment</b> &mdash; adequate for most cases, as effective as oral with fewer side effects. <b>Remove crusts before applying.</b> Retapamulin is licensed but far more expensive.<br><b>1st (oral):</b> dicloxacillin, amoxicillin-clavulanate, <b>cephalexin &mdash; drug of choice in children</b>, clindamycin if penicillin allergic.<br><b>If MRSA:</b> clindamycin, trimethoprim-sulfamethoxazole, doxycycline (over 8 years old).",
  "Self-limiting but may last weeks or months. <b>Isolate children until treatment has been underway 24&ndash;48 hours.</b> Do not share towels, clothing, bath water, washcloths or razors. Gentle cleansing with antibacterial soap. <span class=warn>Acute post-streptococcal glomerulonephritis may follow &mdash; especially ages 3&ndash;7 &mdash; and antibiotics do NOT prevent it.</span>"),

 ("l4_s089_1.jpg", "Impetigo &mdash; bullous",
  "<b>Exclusively Staphylococcus aureus</b>, releasing epidermolytic toxins that split the epidermis. Small or large superficial <b>fragile bullae</b>, tense clear or cloudy, on intact skin or invading pre-existing lesions such as eczema. Rupture leaves shallow moist erosions with remnant <b>collarettes</b>. <b>Lymphadenopathy uncommon.</b>",
  "<b>Clinical appearance</b>, as above.<br>Differential: thermal burn, allergic contact dermatitis, herpes simplex or zoster.",
  "As for non-bullous impetigo. Coverage must include staphylococci and streptococci.",
  "The bullous form is the one that <b>secondarily invades existing skin disease</b> such as eczema &mdash; that is a secondary bacterial infection rather than a primary one."),

 ("l4_s091_1.jpg", "Ecthyma",
  "Not common. Begins as a vesicle or pustule over inflamed skin and <b>deepens into dermal ulceration with a thicker grey-yellow crust</b>. Usually the lower extremities. Regional lymphadenopathy common; <b>heals slowly and leaves a scar</b>.<br><span class=pt>&ldquo;A punched-out sore on my shin with a thick crust that isn't healing.&rdquo;</span>",
  "<b>Clinical appearance</b>, as for impetigo.",
  "As for impetigo, covering staphylococci and streptococci.",
  "Predisposed by pre-existing tissue damage (bites) and immunocompromise such as diabetes; crowding and poor hygiene increase risk. <b>The depth is what separates it &mdash; it scars, ordinary impetigo does not.</b>"),

 ("l4_s098_1.jpg", "Erysipelas",
  "Infection of the <b>upper dermis extending to superficial cutaneous lymphatics</b> &mdash; a superficial cellulitis. <b>Group A streptococcus.</b> Sudden onset with malaise, myalgia, chills and high fever (38&ndash;40&deg;C) within 48 hours. <b>A plaque raised above the surrounding skin with a CLEAR LINE OF DEMARCATION.</b> Lower extremities in 80%; face is the other common site. &ldquo;Red streaks&rdquo; toward lymph nodes.<br><span class=pt>&ldquo;My face went bright red with a sharp edge to it and I spiked a fever.&rdquo;</span>",
  "<b>Clinical diagnosis in classic presentation.</b> Leukocytosis, raised erythrocyte sedimentation rate and C-reactive protein are common but not diagnostic.<br><span class=warn>Blood and tissue cultures are not cost effective &mdash; extremely low yield. Imaging is low yield and not indicated.</span>",
  "<b>Prompt treatment matters &mdash; progression can be rapid.</b><br><b>1st: penicillin V.</b><br><b>If penicillin allergic:</b> clindamycin.<br><b>Supportive:</b> symptomatic treatment of aches and fever, hydration, cold compresses, elevation of the affected limb.",
  "Risk factors: <b>impaired lymphatic drainage (mastectomy)</b>, immunocompromise, <b>athlete's foot</b>, obesity, trauma, pre-existing impetigo. Treat the tinea pedis &mdash; it is the portal of entry and predicts recurrence. The inciting event is often not recalled."),

 ("l4_s105_1.jpg", "Cellulitis",
  "Acute inflammation of the <b>deeper dermis and subcutaneous tissue</b>. Group A beta-haemolytic streptococci or Staphylococcus aureus. <b>All four cardinal signs</b> &mdash; erythema, warmth, oedema, tenderness. Most common site the lower leg, <b>almost never bilateral</b>. <b>Borders are NOT elevated or demarcated</b> &mdash; which rules out erysipelas. May be purulent or non-purulent.<br><span class=pt>&ldquo;My leg is hot, red, swollen and sore, and the edge just fades out.&rdquo;</span>",
  "<b>Usually clinical. No workup if</b> limited involvement, minimal pain, no systemic signs and no risk factor for serious illness.<br><b>Serious infection:</b> blood cultures and skin punch biopsy; complete blood count (leukocytosis); <b>creatine phosphokinase</b> if muscle damage. Plain films, computed tomography or magnetic resonance imaging to evaluate for underlying fasciitis or osteomyelitis.",
  "<b>Non-purulent:</b> dicloxacillin or cephalexin; clindamycin if penicillin allergic.<br><b>Purulent &mdash; consider MRSA:</b> trimethoprim-sulfamethoxazole, doxycycline, clindamycin or linezolid.<br>Oral versus intravenous depends on presentation.<br><span class=warn>Devitalised tissue &mdash; tense, cyanotic, necrotic, bronzed or blanched &mdash; is not perfused, so antibiotics never reach it. It needs surgical debridement.</span>",
  "<b>May look and feel worse during the first day</b> &mdash; sudden destruction of pathogens releases enzymes that increase local inflammation. Fever usually resolves in 24 hours. <b>Fever beyond 48 hours &rarr; change the antimicrobial, guided by culture.</b> Inflammation settles over 1&ndash;2 weeks. Complications: gangrene and sepsis in the immunocompromised."),

 ("l4_s114_1.jpg", "Abscess",
  "A collection of purulent material within the dermis and deeper tissues, usually from <b>traumatic inoculation</b> of bacteria &mdash; unlike a furuncle, which arises from an infected hair follicle. Early: erythematous tender nodule. Later: purulent material collects centrally and may drain spontaneously. Axilla, vulva, perianal, head, neck, buttocks, extremities, perineum. Often polymicrobial; Staphylococcus aureus commonest.<br><span class=pt>&ldquo;A painful lump that came up where I injured myself, and now it's got a head on it.&rdquo;</span>",
  "<b>Clinical.</b> Culture the drained material, with consideration of MRSA.",
  "<b>If it drains spontaneously:</b> warm soaks; broad-spectrum antibiotics considering MRSA, then narrow to the culture result.<br><b>If it does not drain:</b> <b>surgical incision and drainage.</b>",
  "The aim is to eradicate infection and prevent recurrence."),

 ("l4_s117_1.jpg", "Acute paronychia",
  "Infection of the soft tissue around the fingernail (perionychium), starting as cellulitis and progressing to abscess. <b>Usually 2&ndash;5 days after trauma.</b> Rapid onset of an erythematous oedematous area; advanced cases collect purulent fluid under the nail folds. Staphylococcus aureus, Streptococcus pyogenes.<br><span class=pt>&ldquo;My finger went red and throbbing a couple of days after a manicure.&rdquo;</span>",
  "<b>Usually clinical.</b><br><b>Gram stain and culture</b> to identify the bacterial cause; <b>potassium hydroxide</b> to rule out candida; <b>Tzanck smear</b> to rule out herpetic whitlow.",
  "<b>1st (mild):</b> warm water compresses or soaks, 20 minutes 3&times; daily.<br><b>Severe:</b> incise and drain; obtain cultures to rule out MRSA. Oral antibiotics &mdash; amoxicillin-clavulanate, cephalexin, or <b>clindamycin if exposed to oral flora from nail biting</b>.",
  "Predisposing: manicure, ingrown nail, hangnail, nail biting. Differential: onychomycosis, felon, herpetic whitlow, pseudomonal nail infection, squamous cell cancer of the nail."),

 (None, "Chronic paronychia",
  "An <b>inflammatory reaction of the proximal nail fold to irritants and allergens</b>, possibly eczematous. <b>Candida albicans</b> is the commonest organism. Oedematous, erythematous, tender nail folds <b>without fluctuance</b>; nail plates thicken and discolour; cuticles separate from the plate. <b>Present at least 6 weeks.</b><br><span class=pt>&ldquo;My nail folds have been puffy and sore for months and my nails look ruined.&rdquo;</span>",
  "<b>Clinical</b>, with a history of continuous hand immersion in water or chemical contact.",
  "<b>1st:</b> treat the underlying inflammation and infection; <b>keep the hands as dry as possible</b>; broad-spectrum topical antifungal (miconazole).<br><b>2nd:</b> oral antifungal in severe cases (fluconazole).",
  "Predisposing: diabetes, laundry workers, cleaners, cooks, bartenders, dishwashers, swimming. <b>The timescale is what separates it from acute paronychia</b> &mdash; days versus six weeks."),

 ("l4_s124_2.jpg", "Necrotizing fasciitis",
  "Bacterial infection of the tissue surrounding muscle, nerve, fat and vessels, leading to necrosis. Polymicrobial; Group A streptococcus common. <b>Difficult to recognise early but rapidly progressive.</b><br><span class=warn>The clue: unrelenting pain OUT OF PROPORTION to the physical examination.</span> Later: skin changes red-purple to blue-grey, bullae with thick pink or purple fluid, cutaneous gangrene, and <b>the area stops being tender because the superficial nerves have been destroyed</b>. Fever 38.9&ndash;40.5&deg;C, tachycardia, hypotension, septic shock.<br><span class=pt>&ldquo;The pain is far worse than it looks &mdash; and now it's gone numb.&rdquo;</span>",
  "<b>A surgical emergency with high mortality.</b> <span class=warn>Laboratory tests and imaging must NOT delay surgical intervention.</span><br>Complete blood count with differential, chemistry, arterial blood gas, urinalysis, blood and tissue cultures.<br>Ultrasound demonstrates air bubbles in soft tissue; magnetic resonance or computed tomography localises site and depth. <b>Gas may be present with Clostridium perfringens; it is NOT present with Group A streptococcus.</b>",
  "<b>1st: aggressive surgical debridement of necrotic tissue.</b> Admit to a surgical intensive care unit (burn or trauma centre). Team approach with consultations.<br><b>Antibiotics:</b> broad-based, covering aerobic Gram-positive and Gram-negative organisms and anaerobes.",
  "<b>Commonly misdiagnosed as cellulitis, sent home, and returns worse.</b> Consider it if there is no response to antibiotics within 48 hours. Risk factors: trauma, burns, surgery, immunosuppression, renal failure, alcoholism, dental infection, injection drug use. Male &gt; female."),
]

ROWS += [
 # ================= LECTURE 5 =================
 ("SECTION", "Lecture 5 &middot; Dermatological Infestations"),

 ("l5_s009_1.jpg", "Scabies",
  "<b>Itching almost always, and severe</b>, with intense <b>nocturnal</b> pruritus. Insidious onset. Excoriations and eczematous dermatitis in interdigital webs, sides of fingers, volar wrists, elbows, axillae, scrotum, penis, labia, areolae. <b>Head and neck spared in healthy adults</b> &mdash; but involved in infants, the elderly and the immunocompromised, who also get indurated crusted nodules on the trunk.<br><b>Pathognomonic: a thin, thread-like linear or J-shaped BURROW, 1&ndash;10&nbsp;mm.</b><br><span class=pt>&ldquo;The itch is unbearable at night and it's driving me mad.&rdquo;</span>",
  "<b>Definitive: microscopic identification of the organism, ova or faeces.</b><br><b>Skin scraping</b> &mdash; number 15 blade, unexcoriated burrow or papule, swab with alcohol, apply mineral oil, scrape firmly onto a slide.<br><b>Dermoscopy</b> &mdash; the <b>&ldquo;delta-wing jet&rdquo;</b> sign.<br><b>Burrow ink test</b> &mdash; blue/black ink applied; a zigzag line running away from the lesion is positive.",
  "<b>1st: topical permethrin overnight to the ENTIRE skin surface with attention to creases, and a SECOND APPLICATION ONE WEEK LATER.</b><br><b>Non-pharmacologic:</b> wash bedding and clothing at <b>60&deg;C</b> or bag for 14 days in a warm area; <b>treat all infected persons in the family or group</b>.<br><b>Hyperkeratotic or immunosuppressed:</b> ivermectin every 2 weeks for 2&ndash;3 doses + topical permethrin every 3 days to weekly.<br><b>Pregnancy:</b> treat only if documented.",
  "Relief in about 3 days, but <b>rash and itch may last up to 4 weeks</b> (triamcinolone if needed). <span class=warn>Excessive washing with harsh soap worsens irritation.</span> Pruritus appears 4&ndash;6 weeks after a first infestation but <b>2&ndash;3 days after reinfestation</b>. Complications: staphylococcal superinfection (may lead to sepsis), persistent post-scabietic papules, psychological effects."),

 ("l5_s011_4.jpg", "Crusted (hyperkeratotic) scabies",
  "<b>Thick flaking scale containing millions of mites.</b> Nails thickened or discoloured, patches poorly defined, and patients <b>may be asymptomatic &mdash; not itchy at all</b>.<br><span class=pt>&ldquo;My skin has gone thick and scaly, but honestly it doesn't itch.&rdquo;</span>",
  "As for scabies &mdash; but the mite burden is massive, so scrapings are strongly positive.",
  "<b>Ivermectin every 2 weeks for 2&ndash;3 doses plus topical permethrin every 3 days to weekly.</b>",
  "<span class=warn>These patients are HIGHLY INFECTIOUS.</span> Facility-associated scabies is common in long-term care where residents are elderly and immunosuppressed; a hospital epidemic can follow their admission, and it is difficult to eradicate once healthcare workers are infested."),

 ("l5_s027_2.jpg", "Pediculosis capitis (head lice)",
  "Incubation 4&ndash;6 weeks. Pruritus, low-grade fever, regional lymphadenopathy, irritability. 2&nbsp;mm erythematous macules or papules; excoriations, erythema, scaling. Some patients are asymptomatic carriers. Commonest in <b>children 3&ndash;12 years</b>; direct head-to-head contact.<br><span class=pt>&ldquo;Her head is so itchy and the school sent a note home.&rdquo;</span>",
  "<b>Visualising nits or live lice.</b> Live lice mean active infestation &mdash; best found by <b>wet combing</b> with water and conditioner using a nit comb. Nits are visible to the naked eye and indicate past or present infestation.<br><b>Nits cannot be removed from the hair shaft</b> &mdash; that is what separates them from dandruff. Viable eggs are tan to brown; hatched remnants are clear, white or light.",
  "<b>A multimodal approach is warranted because of increasing resistance.</b> Pediculicidal effect read <b>24 hours</b> after application (World Health Organization).<br><b>Physical methods:</b> shaving the head; combing nits after 2 minutes of hair moisturiser, then drying &mdash; repeated every few days. These work but are time-consuming, painful and difficult, and <b>need adjuvant therapy</b>.",
  "Wear clean clothing after treatment; dry or bag clothing, bedding and towels from the prior week for 2 weeks; <b>wash combs</b>; vacuum floors, carpets, upholstery, play areas and furniture. <span class=warn>Fumigation is NOT recommended.</span> Nits may remain in the hair for months, and a <b>&ldquo;no nit&rdquo; policy is NOT recommended</b> by the American Academy of Pediatrics because of school absence. If treatment is not done properly patients turn to essential oils, mayonnaise or mineral oil, which may not be lethal."),

 ("l5_s027_1.jpg", "Pediculosis corporis (body lice)",
  "Pruritus, with <b>linear excoriations primarily on the back, neck, shoulders and waist</b>; post-inflammatory pigmentation in chronic cases. Found in the homeless, refugees, victims of war and disaster, and crowded living with poor hygiene.<br><span class=pt>&ldquo;I itch all over my back and I can't get on top of it.&rdquo;</span>",
  "<b>Close examination of the SEAMS OF CLOTHING for nits.</b> Shaking clothing over white paper &mdash; the lice move onto the paper.",
  "As for head lice &mdash; multimodal, with attention to clothing.",
  "Transmission is via contaminated clothing and bedding; the inability to wash or change clothes is what allows the infestation to persist. Addressing that is the intervention."),

 ("l5_s027_4.jpg", "Pediculosis pubis (crabs)",
  "Often asymptomatic or mild to moderate pruritus for months. <b>Maculae caerulae</b> &mdash; slate-grey to bluish irregular macules about 1&nbsp;cm, representing haemorrhage. Papular urticaria at feeding sites, commonly periumbilical. <b>Phthiriasis palpebrarum</b> is infestation of the eyelashes.<br><span class=pt>&ldquo;I've been itching down there for weeks and there are odd bluish marks.&rdquo;</span>",
  "<b>Locating nits at the base of hairs</b>; confirmed by <b>microscopic examination of a plucked hair</b>.",
  "As for the other forms.",
  "<span class=warn>Patients often have a concurrent sexually transmitted disease &mdash; screen for it.</span> Transmission is sexual, but also via contaminated clothing, towels and bedding. Found across all levels of society and all ethnic groups."),

 ("l5_s034_2.jpg", "Bedbugs",
  "Nocturnal feeders hiding by day in cracks and crevices of headboards, picture frames, behind loose wallpaper. Attracted to warmth and carbon dioxide. <b>Bites are painless, multiple, and grouped in a LINEAR fashion &mdash; a row of three is &ldquo;breakfast, lunch and dinner&rdquo;.</b> Wheals and papules with a <b>haemorrhagic punctum</b>; bullous reactions in sensitised patients. <b>Blood flecks on the bed linen.</b><br><span class=pt>&ldquo;I wake up with itchy welts in a line, and there are little blood spots on the sheets.&rdquo;</span>",
  "<b>Physical examination.</b>",
  "<b>Symptomatic treatment</b> and local wound care.<br><b>Secondary infection:</b> topical antiseptic lotion or antibiotic cream.<br><b>Pruritus:</b> topical corticosteroids or oral antihistamines.<br><b>Eradication: a professional exterminator is necessary.</b>",
  "Bedbugs need a blood meal every 5&ndash;10 days but <b>can survive up to a year</b> without one &mdash; leaving a room empty does not clear them. Spread in clothing and baggage of travellers and visitors, second-hand mattresses, and laundry. <b>Not a marker of poor hygiene.</b>"),

 ("l5_s039_2.jpg", "Tungiasis (fleas)",
  "Infestation by penetration of an adult female flea into human skin to lay eggs (family Tungidae). Solitary or multiple erythematous papules enlarging over weeks to <b>4&ndash;10&nbsp;mm</b>; a fully developed <b>yellow, firm, somewhat translucent nodule</b> that may be painful. Over the feet (especially plantar), subungual and periungual skin, web spaces and legs. Pain, pruritus, <b>autoamputation of toes</b>.<br><span class=pt>&ldquo;I got these sore lumps on my feet after walking barefoot on the beach abroad.&rdquo;</span>",
  "<b>Dermoscopy to visualise the ovoid eggs.</b>",
  "<b>1st: surgical excision, or cryotherapy / topical agents.</b><br><b>Plus: tetanus prophylaxis and systemic antibiotics.</b>",
  "Travel or residence in endemic areas &mdash; West Indies, Central America, Africa, India, Pakistan, South America. <b>Prevention: avoid walking barefoot or in sandals along beaches, and do not sit in the sand</b> in Nigeria, the Caribbean, India or Brazil.<br>Pulicidae fleas instead cause linear or clustered urticarial papules on the lower legs; rat fleas transmit bubonic plague, cat fleas plague and endemic typhus."),

 ("l5_s047_1.jpg", "Caterpillars (lepidopterism)",
  "About 100&ndash;150 species. Mechanisms: mechanical irritation by pointed hairs, toxin injection through hollow hairs, cell-mediated hypersensitivity to hairs.<br><b>Gypsy moth:</b> erucism &mdash; pruritic dermatitis with multiple erythematous papules in <b>linear streaks</b>.<br><b>Processionary:</b> urticaria, angio-oedema, anaphylaxis.<br><b>Asp or puss caterpillar (most poisonous):</b> intense painful sting with a <b>train-track pattern of purpura</b>.",
  "<b>Clinical</b>, from the exposure history and the pattern.",
  "<b>Symptomatic:</b> systemic antihistamines; topical menthol or camphor; moderate to high potency topical corticosteroids; systemic corticosteroids; oral or parenteral narcotic analgesics for severe pain.<br><b>Specific:</b> <b>remove the hairs by &ldquo;stripping&rdquo; with adhesive tape.</b> Antivenom for certain categories.",
  "The physical removal of hairs with tape is the step that is easy to forget and makes the difference."),

 ("l5_s052_1.jpg", "Cutaneous larva migrans",
  "Larvae of animal hookworms &mdash; mostly dog and cat &mdash; in which the human is a <b>dead-end host</b>. Requires contact with sand or soil contaminated with animal faeces.<br><b>Classic: an erythematous, raised, vesicular, linear or SERPENTINE cutaneous trail that progresses 2&ndash;3&nbsp;cm PER DAY.</b> Intensely pruritic and painful; lasts 2&ndash;8 weeks. Systemic signs rare.<br><b>Hookworm folliculitis:</b> follicular papules and pustules confined to one location, usually the buttock.<br><span class=pt>&ldquo;There's a winding red track on my foot and it moves every day.&rdquo;</span>",
  "<b>Clinical diagnosis if the serpiginous rash is present.</b><br>Pathology: larvae trapped within the follicular canal, stratum corneum or dermis with an eosinophilic infiltrate. <b>Light microscopy with mineral oil</b> shows live and dead larvae in the folliculitic form.",
  "<b>1st: albendazole 400&nbsp;mg by mouth daily for 3 days, or ivermectin 200&nbsp;micrograms/kg daily for 1&ndash;2 days.</b><br>Hookworm folliculitis may need repeated treatments.<br><span class=warn>Topical therapy is less effective. Surgical excision and cryotherapy are NOT recommended.</span>",
  "Commonly found in tropical and subtropical areas &mdash; southeastern United States, Caribbean, Africa, Central and South America, India, Southeast Asia."),

 ("l5_s056_1.jpg", "Black widow spider",
  "<i>Latrodectus mactans</i> &mdash; characteristic <b>red hourglass on the underside of the abdomen</b>. Venom contains the neurotoxin <b>alpha-latrotoxin</b>.<br>Painful bite with mild dermatologic findings. <b>Within 30 minutes:</b> localised erythema, piloerection and sweating around the bite. Then <b>agonising crampy abdominal pain and muscle spasms</b>; headache, paraesthesia, nausea, vomiting, hypertension, lacrimation, salivation, seizures, tremors, acute renal failure, paralysis.<br><span class=pt>&ldquo;It bit me and within half an hour my stomach was cramping so badly I thought something had ruptured.&rdquo;</span>",
  "<b>Clinical</b>, from the exposure and the systemic picture.",
  "<b>Local wound care versus hospitalisation depending on symptoms.</b><br><b>Envenomation:</b> calcium gluconate 10%; narcotic analgesics; muscle relaxants; benzodiazepines.<br><b>Ensure tetanus vaccination is up to date.</b>",
  "<span class=warn>Increased risk of complications in the very old, the very young, and those with cardiovascular disease.</span> Death is uncommon. Webs in corners of doors and windows, under woodpiles, garages, sheds, around outdoor toilet seats."),

 ("l5_s060_1.jpg", "Brown recluse spider",
  "<i>Loxosceles reclusa</i> &mdash; non-aggressive, with a dark brown <b>fiddle or violin marking on the cephalothorax</b>. Abundant in the American Midwest and Southeast; shelters in closets, attics and storage areas for bedding and clothing.<br>Ranges from mild local reaction to <b>severe ulcerative necrosis</b>. <b>Hallmark: the RED, WHITE AND BLUE sign</b> &mdash; a central violaceous area surrounded by a rim of blanched skin, surrounded by a large asymmetric area.<br><b>Necrosis 2&ndash;3 days</b> after the bite, <b>eschar between days 5 and 7</b>, then deep ulcers. Systemic symptoms 1&ndash;2 days after: nausea, vomiting, headache, fever, chills.",
  "<b>Clinical</b>, from the appearance and the exposure history.",
  "<b>1st:</b> pain control, warm compresses, avoid strenuous exercise.<br><b>Antibiotics</b> for secondary bacterial infection.<br><b>Necrotic wounds heal very slowly and may need surgical intervention or reconstruction to close the defect &mdash; <span class=warn>surgery is DELAYED until the wound is stable.</span></b>",
  "Bites occur when the spider feels threatened or provoked. The staged timeline &mdash; necrosis at 2&ndash;3 days, eschar at 5&ndash;7 &mdash; is what lets you place a presenting lesion in its course."),

 ("l5_s063_1.jpg", "Hobo spider",
  "<i>Tegenaria agrestis</i>, the aggressive house spider &mdash; brown with a <b>grey herringbone pattern on the abdomen</b>. <b>Often mistaken for the brown recluse.</b> The predominant cause of necrotic arachnidism in the Pacific Northwest. Bites <b>July to September</b> during mating season; webs in basements, wood piles, bushes.<br><b>Painless bite</b>; induration and paraesthesia within 30 minutes; a large erythematous area; <b>vesicle formation during the first 36 hours</b>; sometimes eschar. Systemic: headaches, fatigue, nausea, vomiting, diarrhoea, paraesthesia, <b>memory impairment</b>.",
  "<b>Clinical</b>, from geography, season and the appearance.",
  "<b>Supportive measures.</b>",
  "Wounds heal within several weeks; headaches may last up to a week. <span class=warn>Rare: death from severe systemic effects, including aplastic anaemia.</span>"),

 ("l5_s073_5.jpg", "Lyme disease",
  "<i>Borrelia burgdorferi</i>, a spirochete.<br><b>Stage 1 &mdash; early localised:</b> <b>erythema migrans</b> &mdash; a large (&gt;5&nbsp;cm) expanding erythematous round or oval lesion with <b>central clearing</b> and often a darker punctate centre at the bite site &mdash; the &ldquo;bull's eye&rdquo;. Occurs <b>1 week</b> after the bite, with fever, myalgia, arthralgia, fatigue, lymphadenopathy.<br><b>Stage 2 &mdash; early disseminated (days to weeks):</b> skin, central nervous system, cardiac, musculoskeletal, eyes &mdash; cranial nerve palsies, meningitis, radiculopathies, arthralgias, headache, stiff neck.<br><b>Stage 3 &mdash; late persistent (months to years):</b> <b>monoarticular or oligoarticular arthritis</b> of the knee or weight-bearing joints; subacute encephalopathy with memory loss, mood change and sleep disturbance; <b>acrodermatitis chronica atrophicans</b>.",
  "<b>If the patient has an erythema migrans lesion, diagnose and treat on CLINICAL signs.</b><br>Testing is most helpful in patients who do <b>not</b> live in an endemic region and present with possibly consistent signs.<br><b>ELISA</b> for immunoglobulin M and G; the immunoglobulin G assay (<b>C6 peptide test</b>) has greater specificity; <b>Western blot</b> is more specific still.",
  "<b>Remove the tick immediately.</b> Antibiotics are indicated at all stages.<br><b>1st oral: doxycycline.</b><br><b>Children and pregnant women: amoxicillin</b> (alternative first line for early erythema migrans).<br><b>2nd:</b> macrolides &mdash; azithromycin &mdash; for those who cannot tolerate other agents.<br><b>Duration: 10&ndash;14 days.</b><br><b>Intravenous:</b> ceftriaxone, cefotaxime or penicillin G for some cutaneous manifestations, acrodermatitis chronica atrophicans and arthritis.",
  "Endemic in Connecticut, Delaware, Maine, Maryland, Massachusetts, Minnesota, New Hampshire, New Jersey, New York, Pennsylvania, Rhode Island, Vermont, Wisconsin.<br><b>Prevention:</b> avoid tick habitat; <b>no human vaccine (one exists for dogs)</b>; repellents DEET, PMD, picaridin reapplied about every 2 hours; pyrethrins."),

 ("l5_s084_1.jpg", "Rocky Mountain spotted fever",
  "<i>Rickettsia rickettsii</i>. <b>Life-threatening if not treated.</b> Incubation 3&ndash;12 days. Vectors: dog tick, wood tick, rodents.<br><b>Clinical triad: fever (&gt;39.5&deg;C), headache and rash &mdash; but present in only about 60%.</b> Fever comes first for 3 days; <b>rash 2&ndash;4 days after fever onset</b>. <b>Rash starts on the ankles and wrists and spreads CENTRIPETALLY over 6&ndash;18 hours; palms and soles ARE affected; the FACE is spared.</b> Erythematous blanching macules and papules that may evolve to petechiae and purpura.<br>Also chills, malaise, myalgia, nausea, vomiting, anorexia, periorbital oedema, abdominal pain (mimics appendicitis, more in children), conjunctival injection, palatal petechiae, dorsal hand oedema, calf pain.",
  "<b>Labs:</b> thrombocytopenia, anaemia, mild hyponatraemia, mild transaminitis, normal white count with increased bands. <b>Cerebrospinal fluid:</b> leukocytosis, moderately elevated protein, normal glucose.<br><b>Gold standard: indirect immunofluorescence assay</b> &mdash; but it is <b>rarely diagnostic before day 7</b>, and <span class=warn>treatment should be started by day 5. Start treatment while waiting for results.</span><br>About 20% present <b>without</b> a rash.",
  "<b>Adults: doxycycline 100&nbsp;mg by mouth every 12 hours for 5&ndash;10 days &mdash; the same in pregnancy.</b><br><b>Children: doxycycline 2.2&nbsp;mg/kg by mouth every 12 hours for 5&ndash;10 days.</b><br><b>Second line (allergy or contraindication):</b> doxycycline via <b>desensitisation</b> &mdash; small initial doses increased every 15&ndash;60 minutes until the therapeutic dose is reached &mdash; including in pregnancy and children under 8, where teeth staining and hepatotoxicity are the usual contraindications.",
  "<span class=warn>Prophylactic antibiotic therapy is NOT recommended.</span> Prevention: avoid tick exposure, protective clothing, tick checks, DEET. Risk factors: male, adults 40&ndash;64, children under 10, rural dwelling; southeastern and south central states in spring and early summer. Delayed or inadequate treatment &rarr; severe cardiac, gastrointestinal, hepatic, neurologic, ophthalmologic, renal and pulmonary manifestations, with long-term sequelae in survivors."),

 ("l5_s090_1.jpg", "Cercarial dermatitis (swimmer's itch)",
  "Acute pruritic eruption from penetration of the skin by the <b>cercarial</b> forms of parasitic flatworms. Host (waterfowl, marsh bird, finch, muskrat, mouse, deer) passes eggs in faeces into water; eggs hatch and infect a snail within 12 hours; in 5 weeks cercariae are released and carried to the shore.<br><b>Urticaria-like lesions and a prickling sensation lasting about 30 minutes</b> after exposure &rarr; <b>severe pruritus at 10&ndash;12 hours</b> &rarr; <b>erythematous papules within 24 hours</b> &rarr; vesicles &rarr; pustules. Pain and swelling with pruritus <b>peaking at 48&ndash;72 hours</b>. Sometimes headaches, fever, lymphangitis.<br><span class=pt>&ldquo;After the lake my legs prickled, then that night they itched like fire and came up in spots.&rdquo;</span>",
  "<b>Clinical</b>, from the freshwater exposure and the characteristic time course.",
  "<b>Symptomatic:</b> antihistamines, oatmeal baths, antipruritic lotions.<br><b>Aspirin</b> for pain control.<br><b>Topical or oral glucocorticoids.</b>",
  "Proper washing and hygiene after leaving the water. Affects the Great Lakes region, and paddy workers and rice farmers of the Far East."),
]

ROWS += [
 # ================= LECTURE 6 =================
 # Every image below was audited at full size first. See METAPHOR_IMAGES,
 # WRONG_DISEASE_IMAGES and MICROGRAPH_IMAGES for what that audit rejected.
 ("SECTION", "Lecture 6 &middot; Cutaneous Fungal Infections"),

 ("l6_s009_1.jpg", "Tinea capitis (scalp)",
  "<b>Predominantly preadolescent children</b> &mdash; after puberty, changes in the fatty acid content of sebum are believed to inhibit growth. The commonest fungal infection in children; <i>Trichophyton tonsurans</i> is commonest in the United States. Red papules progressing to <b>greyish ring-formed patches with perifollicular papules</b>, scaly patches, and <b>lymphadenopathy is often present</b>.<br><span class=pt>&ldquo;He has a scaly bald patch on his head and he keeps scratching it.&rdquo;</span>",
  "<b>Potassium hydroxide microscopy and fungal culture</b> where feasible &mdash; especially <b>before prolonged systemic therapy</b>. <b>Wood lamp</b> may rapidly support <i>Microsporum</i>, but <b><i>T. tonsurans</i> usually does not fluoresce</b>, so a negative lamp excludes nothing. Bacterial culture if a kerion has purulent drainage.",
  "<b>Oral therapy is required</b> &mdash; topical agents do not penetrate the infected hair shaft.<br><b>Terbinafine</b> generally favored for <i>Trichophyton</i>; <b>griseofulvin</b> often favored for <i>Microsporum</i>.<br>Review interactions and hepatic disease; baseline liver tests when indicated by the agent and patient risk.<br><b>Adjunct:</b> selenium sulfide 1&ndash;2.5% or ketoconazole 2% shampoo, 2&ndash;3 times weekly &mdash; reduces spore shedding but <b>does not replace oral therapy</b>.",
  "Complete the whole oral course even when itching settles early. Do not share combs, brushes, hats, towels or hair accessories; clean tools and washable fomites. <b>Fungal particles stay viable for months.</b> Evaluate symptomatic contacts and consider pets where a zoophilic source is suspected. <b>School exclusion is generally unnecessary once effective therapy has begun</b>; follow local policy. Treat inflammatory disease promptly to reduce scarring alopecia."),

 ("l6_s011_1.jpg", "Black dot tinea capitis",
  "The pattern in which the <b>hair fractures at the scalp surface</b>, leaving patches of alopecia studded with visible black dots.<br><span class=pt>&ldquo;There are little black specks where the hair broke off.&rdquo;</span>",
  "As for tinea capitis &mdash; <b>potassium hydroxide microscopy and culture</b>.",
  "As for tinea capitis: <b>oral</b> antifungal therapy.",
  "Distinguish from <b>alopecia areata</b>, where the skin is smooth and shiny without inflammation, and from <b>seborrheic dermatitis</b>, where hair may be lost but is <b>not broken</b>."),

 ("l6_s020_1.jpg", "Tinea barbae &mdash; inflammatory",
  "<i>Trichophyton</i> species. <b>Usually acquired from animals.</b> Tender, boggy, pustular <b>kerion-like plaques</b>; <b>infected hairs are loose and easily removed</b>. <b>Scarring alopecia may occur.</b><br><span class=pt>&ldquo;My beard is swollen and sore, and the hairs just pull straight out.&rdquo;</span>",
  "<b>Potassium hydroxide and culture.</b> <b>Bacterial culture</b> to rule out bacterial folliculitis &mdash; in tinea barbae the hair is easily removed, unlike folliculitis. Biopsy for refractory cases.",
  "<b>Oral antifungal therapy is required</b> &mdash; topicals do not penetrate the hair follicle.<br><b>Griseofulvin</b> or <b>terbinafine</b>.<br>Shave or remove hair; warm compresses to remove crusts and debris.",
  "Differential also includes <b>acne, rosacea and seborrheic dermatitis</b>. The animal source is worth tracing."),

 ("l6_s019_1.jpg", "Tinea barbae &mdash; noninflammatory",
  "<b>Usually acquired from another person.</b> Annular scaly plaques, or a folliculitis-like eruption; <b>hairs may break near the skin surface</b>. Asymptomatic or mildly pruritic.",
  "<b>Potassium hydroxide and culture</b>; bacterial culture to exclude folliculitis.",
  "As for the inflammatory form &mdash; <b>oral</b> antifungal therapy.",
  "Person-to-person acquisition, so shared razors and clippers matter."),

 ("l6_s024_2.jpg", "Tinea corporis (body) &mdash; &ldquo;ringworm&rdquo;",
  "<i>Trichophyton rubrum</i> is the common pathogen. One or more <b>circular, sharply circumscribed, slightly erythematous, dry scaly patches or plaques</b> with <b>progressive central clearing</b> producing the annular outline.<br><span class=pt>&ldquo;It started as a small ring and it's been growing outwards, clearing in the middle.&rdquo;</span>",
  "<b>Potassium hydroxide from the ACTIVE BORDER</b> &mdash; not the cleared centre. <b>Culture</b> where clinical suspicion is high and the preparation is negative, and for refractory cases.",
  "<b>Localized:</b> topical terbinafine, butenafine or an azole, applied to the lesion <b>and 1&ndash;2&nbsp;cm beyond its border</b>, for the product-specific duration and continued past visible improvement.<br><b>Systemic:</b> consider oral therapy for extensive, follicular, immunocompromised, refractory or recurrent disease &mdash; terbinafine commonly, or itraconazole or fluconazole by organism and interactions.",
  "<b>Avoid corticosteroid&ndash;antifungal combination products</b>: steroids mask and worsen dermatophytosis (tinea incognito). Differential is psoriasis, <b>nummular eczema</b> (commonly confused with it), discoid lupus and fixed drug eruption. <b>Suspect resistance</b> when disease is widespread, intensely inflammatory, epidemiologically linked, or fails an adequate terbinafine course &mdash; then get species identification and susceptibility testing."),

 ("l6_s032_1.jpg", "Tinea cruris (groin) &mdash; &ldquo;jock itch&rdquo;",
  "Involves the <b>crural fold</b>. <b>More common in men</b>; often coexists with tinea pedis. <i>T. rubrum</i> and <i>Epidermophyton floccosum</i>. Pruritic, <b>sharply demarcated plaque on the proximal medial thigh &mdash; the SCROTUM IS TYPICALLY SPARED</b>.<br><span class=pt>&ldquo;The itch is in the crease of my groin, and it's spreading down my inner thigh.&rdquo;</span>",
  "<b>Potassium hydroxide from the active border</b> for uncertain cases.",
  "<b>Localized:</b> topical allylamine (terbinafine) or azole (ketoconazole).<br>Reserve <b>oral</b> therapy for extensive or refractory disease.",
  "Predisposing: <b>warm moist environment, obesity, diabetes, tight clothing worn for long periods, sharing clothes</b>. <b>Scrotal involvement points elsewhere</b> &mdash; candidal intertrigo commonly involves the scrotum and throws satellite papules or pustules; erythrasma may fluoresce coral-red."),

 ("l6_s038_2.jpg", "Tinea pedis &mdash; interdigital",
  "<b>The most common form</b>, and tinea pedis is <b>the most common dermatophyte infection in adults</b> (men more than women). Pruritic. <b>Maceration, erythematous erosions or scaling between the toes</b>, especially the <b>third and fourth interspaces</b>, with associated fissures.<br><span class=pt>&ldquo;It's raw and peeling between my toes and it itches.&rdquo;</span>",
  "<b>Clinical.</b> Confirm uncertain cases with <b>potassium hydroxide from the advancing scale</b>. Culture for atypical, recurrent, severe or refractory disease. <b>Add bacterial studies for marked maceration, malodor, erosion, drainage, ulceration or cellulitis.</b>",
  "<b>Topical terbinafine or butenafine, or an azole.</b><br>Consider <b>oral</b> therapy for extensive, recurrent, refractory or immunocompromised disease. <b>Treat coexisting onychomycosis</b> and reinforce moisture control.",
  "<b>Drying between the toes after bathing is essential.</b> Antifungal foot powder in shoes; open-toed sandals where possible; sandals in communal showers; change socks frequently. Spread is by contact with infected desquamated skin &mdash; shoes, locker room floors, sweating."),

 ("l6_s040_2.jpg", "Tinea pedis &mdash; hyperkeratotic",
  "<i>Trichophyton</i> species. Asymptomatic or pruritic. <b>Plantar erythema with slight scaling through to diffuse thickening</b>, involving the soles and the medial and lateral surfaces &mdash; <b>resembling a shoe distribution</b>.<br><span class=pt>&ldquo;The bottoms of my feet are thick and dry all over.&rdquo;</span>",
  "As for interdigital disease &mdash; <b>potassium hydroxide</b>, culture if atypical or refractory.",
  "<b>Antifungal plus a KERATOLYTIC</b> for the thickening.<br>Oral therapy for extensive, recurrent, refractory or immunocompromised disease.",
  "Often bilateral and long-standing; patients frequently put it down to dry skin."),

 ("l6_s041_1.png", "Tinea pedis &mdash; vesiculobullous",
  "<i>Trichophyton</i> species. The <b>moist, acute form</b> &mdash; pruritic <b>and painful</b>. Vesicular or bullous eruption on underlying erythema.<br><span class=pt>&ldquo;Blisters came up on my foot and they hurt.&rdquo;</span>",
  "<b>Potassium hydroxide</b>; bacterial studies if macerated, malodorous or draining.",
  "Topical antifungal; <b>oral</b> therapy for extensive or refractory disease.",
  "Distinguish from contact dermatitis and psoriasis, both of which sit in the tinea pedis differential."),

 ("l6_s048_1.jpg", "Onychomycosis (tinea unguium)",
  "<b>Dermatophytes &mdash; especially <i>T. rubrum</i> &mdash; cause most cases</b>; yeast and molds also occur. Distal lateral disease produces <b>debris, onycholysis, thickening, discoloration and crumbling</b>.<br><span class=pt>&ldquo;My toenails are thick, yellow and crumbling.&rdquo;</span>",
  "<b>Confirm fungus BEFORE oral therapy &mdash; many dystrophic nails are not fungal.</b><br>Potassium hydroxide microscopy, <b>periodic acid&ndash;Schiff stain of nail clippings</b>, fungal culture, or polymerase chain reaction where available.<br><b>Sample the most PROXIMAL accessible diseased nail bed or subungual debris</b>, after trimming the onycholytic nail.",
  "<b>Oral terbinafine is first-line</b> for most dermatophyte disease: usually <b>6 weeks for fingernails, 12 weeks for toenails</b>. Review hepatic disease and interactions; baseline liver tests per labeling and risk.<br><b>Itraconazole</b> is an alternative; <b>fluconazole is off label in the United States</b>.<br><b>Limited disease:</b> topical efinaconazole, tavaborole or ciclopirox &mdash; <b>lower cure rates</b>.",
  "<b>Improvement requires nail growth</b>, so appearance lags well behind treatment. Manage concomitant tinea pedis or it will recur. Risks: <b>tinea pedis, age, diabetes, trauma, occlusive footwear, psoriasis and vascular disease</b>."),

 ("l6_s054_1.jpg", "Tinea manuum (hand)",
  "Associated with tinea pedis, with <b>high recurrence</b>. <b>Dorsal hand</b> looks like tinea corporis (annular plaque); <b>palm</b> looks like tinea pedis (hyperkeratotic, thickened, dry, scaly). <b>Two feet&ndash;one hand syndrome</b>: the hand used to scratch the foot is the one affected.<br><span class=pt>&ldquo;My palm has been dry and thick for months &mdash; I assumed it was from work.&rdquo;</span>",
  "<b>Potassium hydroxide</b> and culture, as for the corresponding body site.",
  "<b>Same as tinea pedis</b> &mdash; topical for localized disease; oral for extensive, recurrent, refractory or immunocompromised disease. Treat coexisting onychomycosis; reinforce moisture control.",
  "<b>Patients are often unaware they have an infection</b>, believing the change is dry skin or hard physical labour. Check both feet and both palms."),

 ("l6_s060_1.jpg", "Id (dermatophytid) reaction",
  "An inflammatory dermatitis <b>at a site DISTANT from the primary dermatophytosis</b> &mdash; occurs with any dermatophyte infection, tinea pedis commonly. Mechanism <b>unknown</b>; possibly delayed-type hypersensitivity. Appears <b>1&ndash;2 weeks after the primary infection</b>, <b>extremely pruritic</b>, papules or papulovesicular eruptions, <b>commonly on the fingers</b>.<br><span class=pt>&ldquo;My hands broke out in itchy little blisters after my foot was treated.&rdquo;</span>",
  "<b>Potassium hydroxide POSITIVE at the primary site, NEGATIVE at the id site.</b><br>Three criteria: (1) dermatophyte infection elsewhere on the body, (2) <b>absence of fungal elements at the reaction site</b>, (3) resolution when the primary infection is treated.",
  "<b>Treat the primary dermatophyte infection</b> &mdash; the id reaction resolves with it.",
  "Examine carefully for an <b>asymptomatic fissure or maceration in the toe webs</b>; the patient may not know the foot is infected."),

 ("l6_s064_1.jpg", "Tinea incognito",
  "Tinea with a <b>clinically altered appearance due to inappropriate treatment, usually topical steroids</b>. Steroids get used on anything that looks inflammatory; when they are stopped the lesion flares, and more steroid follows.<br><span class=pt>&ldquo;It settles while I use the cream and comes back worse every time I stop.&rdquo;</span>",
  "<b>Stop the corticosteroid or calcineurin inhibitor</b>, then <b>potassium hydroxide and culture from an active edge</b>. Warn that <b>inflammation may rebound after withdrawal</b>.",
  "<b>Topical</b> antifungal for localized disease; <b>systemic</b> for extensive, follicular or refractory infection.",
  "The reason combination steroid&ndash;antifungal products are to be avoided in the first place."),

 ("l6_s069_2.jpg", "Cutaneous candidiasis and intertrigo",
  "<b>Intertrigo</b> is an inflammatory rash from <b>friction, moisture and heat trapped in body folds</b>; <b>Candida may secondarily infect it</b>. <i>Candida albicans</i> is the commonest species, an opportunistic <b>yeast</b> (unicellular fungi reproducing by budding); males equal females. <b>Well-demarcated erythematous patches with SATELLITE papules or pustules.</b> Pruritus and burning pain.<br><span class=pt>&ldquo;Under my breasts is raw, red and burning.&rdquo;</span>",
  "<b>Clinical</b>, supported by <b>potassium hydroxide preparation</b> and culture. <b>Satellite papules or pustules support Candida</b>; <b>malodor, erosions or drainage raise concern for bacterial coinfection</b>.",
  "<b>Correct the environment first:</b> gently dry the folds, reduce friction and occlusion, use moisture-wicking or absorbent material, address incontinence or hyperhidrosis.<br><b>Topical nystatin treats Candida ONLY; topical azoles treat Candida AND many dermatophytes.</b><br>Consider a <b>low-potency corticosteroid briefly</b> for marked inflammation, and <b>only</b> alongside adequate antifungal treatment.",
  "Common sites: <b>inframammary, axillary, abdominal, inguinal, perineal and interdigital folds</b>. Risks: obesity, diabetes, incontinence, occlusion, immobility, recent antibiotics, immunosuppression. <b>Recurrent or extensive disease warrants evaluation for diabetes and immunosuppression.</b>"),

 ("l6_s076_1.jpg", "Pityriasis versicolor (tinea versicolor)",
  "<b>Overgrowth of lipid-dependent <i>Malassezia</i></b> species that normally inhabit the skin &mdash; <b>NOT considered contagious</b>. Velvety tan, pink or white <b>finely scaling macules 4&ndash;5&nbsp;mm to large confluent areas</b> on the <b>neck, upper arms, trunk and groin</b>. Usually asymptomatic or mildly pruritic.<br><span class=pt>&ldquo;I get these pale patches every summer and they won't tan.&rdquo;</span>",
  "<b>Usually clinical</b> &mdash; scrape or stretch the lesion to reveal fine scale.<br><b>Potassium hydroxide shows short hyphae with clusters of yeast &mdash; &ldquo;spaghetti and meatballs&rdquo;.</b><br>Wood lamp may show <b>yellow-gold fluorescence, but sensitivity is limited</b>. Biopsy rarely needed.",
  "<b>Topical therapy is first-line:</b> ketoconazole shampoo or cream, selenium sulfide, zinc pyrithione, ciclopirox, or topical terbinafine. One common selenium sulfide approach is <b>daily for 7 days with a 10-minute contact time</b>.<br><b>Systemic</b> for extensive, recurrent or refractory disease: oral fluconazole or itraconazole.<br><b>Oral terbinafine is INEFFECTIVE</b> &mdash; adequate levels are not achieved in sweat (topical terbinafine does work).<br><b>Do NOT use oral ketoconazole</b> &mdash; hepatic and adrenal toxicity outweigh benefit in a superficial infection.",
  "<b>Scale resolves before pigment normalises</b>, and recovery can lag months. <b>Colour change alone does not prove treatment failure</b> &mdash; look for scale or confirm with microscopy. Recurrence is common in warm climates; intermittent prophylactic topical therapy may help. Differential: seborrheic dermatitis (yellowish tint, soft greasy scale), pityriasis rosea (herald patch, Christmas-tree distribution), <b>vitiligo (completely depigmented)</b>."),

 ("SECTION", "Lecture 6 &middot; Cutaneous Viral Infections"),

 ("l6_s084_1.jpg", "Varicella (chickenpox)",
  "Primary varicella-zoster infection. Generalized pruritic eruption <b>in multiple stages of healing</b>: macules &rarr; papules &rarr; vesicles &rarr; crusts, with <b>several stages present SIMULTANEOUSLY</b>. Lesions concentrate on the <b>trunk, scalp and face</b>.<br><span class=pt>&ldquo;He has spots everywhere &mdash; some are blisters and some have already scabbed.&rdquo;</span>",
  "<b>Usually clinical</b>; <b>lesion polymerase chain reaction</b> is preferred when confirmation is needed.",
  "<b>Supportive care; AVOID ASPIRIN in children</b> and use caution with non-steroidal anti-inflammatories.<br>Consider <b>early oral antivirals for higher-risk patients</b>; <b>intravenous acyclovir for severe or disseminated disease</b>.",
  "<b>Adults, pregnancy, newborn age and immunocompromise increase complication risk.</b> Promptly consult for pregnancy, neonatal exposure, immunocompromise or severe complications. <b>Contagious from 1&ndash;2 days before the rash until all lesions crust</b>; in breakthrough disease without crusts, until no new lesions for 24 hours. In healthcare settings use <b>standard, airborne AND contact precautions</b>. <b>Two-dose varicella vaccination</b> is primary prevention."),

 ("l6_s100_1.jpg", "Herpes zoster (shingles)",
  "<b>Reactivation of latent varicella-zoster virus</b>; risk rises with <b>age and impaired cell-mediated immunity</b>. Latent in <b>cranial-nerve or dorsal-root ganglia</b>, travelling along a sensory nerve to the skin.<br><b>Pre-eruptive:</b> dysesthesia or pain in the dermatome, lesions by <b>48&ndash;72 hours</b>.<br><b>Acute eruptive:</b> erythematous macules and papules, then <b>grouped herpetiform vesicles on an erythematous base</b> (classic); new lesions over 3&ndash;5 days.<br><b>Blisters confined to one or two adjacent dermatomes and STOP ABRUPTLY AT THE MIDLINE.</b> Thoracic 55%, cranial 20%, lumbar 15%, sacral 5%.<br><span class=pt>&ldquo;A burning band of blisters across one side of my chest.&rdquo;</span>",
  "<b>Typical unilateral dermatomal vesicles are diagnosed clinically.</b><br><b>Polymerase chain reaction from vesicle fluid, scab, or cells from the lesion base</b> is preferred for <b>atypical, disseminated, vaccine-modified or immunocompromised</b> presentations.<br>Differential: herpes simplex, contact dermatitis, impetigo, folliculitis, insect bites, dermatitis herpetiformis, varicella.",
  "<b>Preferred oral agents: valacyclovir, famciclovir or acyclovir</b>; adjust for renal function.<br><b>Start as soon as possible &mdash; ideally within 72 hours of rash onset.</b><br><b>Treat AFTER 72 hours when new lesions are forming</b>, or there is ophthalmic, neurologic, disseminated, severe or immunocompromised disease.<br><b>Intravenous acyclovir</b> and specialist or hospital management for severe disseminated, visceral, central nervous system or sight-threatening disease.<br>Acetaminophen or a non-steroidal for mild pain; cool compresses, calamine, loose clothing, lesion coverage.",
  "<b>A susceptible contact does not &ldquo;catch shingles&rdquo;</b> &mdash; exposure to vesicular fluid, or airborne virus from disseminated disease, can cause <b>varicella</b>. Cover lesions, do not scratch, hand hygiene, and <b>avoid susceptible pregnant people, premature infants and immunocompromised people until crusted</b>. <b>Infectious until lesions have dried.</b> Some have pain without eruption (<b>zoster sine herpete</b>). Resolves over 10&ndash;15 days; complete healing may take a month, <b>typically without visible sequelae</b> &mdash; it scars only when deeper layers are compromised by excoriation or secondary infection.<br><b>Prevention: two doses of recombinant zoster vaccine (Shingrix)</b> for immunocompetent adults 50 and over, and for adults 19 and over who are or will be immunodeficient or immunosuppressed. Standard interval <b>2&ndash;6 months</b>; for immunocompromised patients the second dose may be given <b>1&ndash;2 months</b> after the first."),

 (None, "Postherpetic neuralgia",
  "<b>The most common complication of herpes zoster</b>, and very debilitating. <b>Pain persisting 90 days or more after rash onset</b> is the commonly used definition. Burning, aching, stabbing, electric shock-like, or <b>evoked by light touch (allodynia)</b> &mdash; neuropathic pain from injury of peripheral nerves. <b>May last months to years</b> and impairs sleep, mood and function.<br><span class=pt>&ldquo;The rash cleared months ago but I still can't bear my shirt touching it.&rdquo;</span>",
  "<b>Clinical</b>, from the history of a preceding zoster eruption.",
  "<b>First line: gabapentin or pregabalin, an appropriate tricyclic antidepressant, or topical lidocaine.</b> A <b>capsaicin patch</b> may help.<br>Individualize for kidney function, falls, anticholinergic burden and interactions.<br><b>Avoid routine long-term opioids</b>; refer severe, persistent or disabling pain.",
  "Risk rises with <b>age, severe acute pain, severe rash, ophthalmic involvement and immunocompromise</b>. <b>Topical and systemic corticosteroids do NOT prevent it and must never replace antiviral therapy.</b>"),

 ("l6_s103_1.jpg", "Herpes zoster ophthalmicus",
  "Zoster involving the <b>ophthalmic division (V1) of the trigeminal nerve</b>. <b>Hutchinson sign</b> &mdash; lesions on the <b>tip or side of the nose</b> &mdash; increases ocular risk, <b>but its ABSENCE does NOT exclude eye involvement</b>.<br><span class=pt>&ldquo;The rash is over my forehead and eyelid, and my eye hurts.&rdquo;</span>",
  "<b>Clinical.</b> Evaluate urgently for ophthalmic, otic, neurologic, disseminated or visceral disease.",
  "<b>Start systemic antiviral therapy IMMEDIATELY.</b><br><b>Same-day ophthalmology evaluation</b> for eye pain, visual symptoms, red eye, photophobia, Hutchinson sign, or eyelid or ocular involvement.",
  "Do not wait for the ophthalmology review before starting the antiviral. A negative Hutchinson sign is not reassurance."),

 ("l6_s104_1.jpg", "Ramsay Hunt syndrome (herpes zoster oticus)",
  "<b>Peripheral facial palsy with painful vesicles of the ear canal, auricle or oropharynx</b>; <b>hearing loss, tinnitus or vertigo may occur</b>.<br><span class=pt>&ldquo;My face has dropped on one side and there are painful blisters in my ear.&rdquo;</span>",
  "<b>Clinical.</b>",
  "<b>Antiviral therapy PLUS a systemic corticosteroid, started early when not contraindicated</b> &mdash; one of the few places a steroid is added.<br><b>Urgent ear, nose and throat or neurology evaluation.</b>",
  "<b>Protect the cornea if eyelid closure is impaired.</b>"),

 # s113_1 is severe primary gingivostomatitis -- correct for HSV, but the
 # hemorrhagic lip crusting reads like Stevens-Johnson syndrome, which is
 # taught in Lecture 3 of this same exam. s113_3 is unambiguous herpes labialis.
 ("l6_s113_3.jpg", "Herpes simplex virus (HSV-1 and HSV-2)",
  "<b>Either type can cause oral or genital infection &mdash; lesion location does NOT reliably determine type.</b> Double-stranded DNA <b>Herpesviridae</b>; <b>neurovirulent</b>, producing <b>latent but lifelong infection</b> with episodic reactivation.<br><b>First episode</b> is more prominent and longer; <b>recurrences</b> are milder and shorter. Prodrome of tenderness, pain, paresthesias or burning &mdash; with <b>localized pain, tender lymphadenopathy, headache, generalized aching and fever</b> characteristic; some have no prodrome.<br><b>Grouped vesicles on an erythematous base breaking down to a shallow painful ulcer</b>; dysuria in women with genital lesions; last about two weeks, <b>heal without scarring</b>.<br><span class=pt>&ldquo;It tingled for a day, then painful blisters came up and burst.&rdquo;</span>",
  "<b>Swab a FRESH vesicle, ulcer base or crust for type-specific nucleic acid amplification &mdash; the preferred test.</b><br><b>Culture is less sensitive</b>, especially in healing or recurrent lesions; a negative result does not exclude HSV. A <b>negative older-lesion swab does not exclude infection because shedding is intermittent</b>.<br><b>Do NOT use HSV immunoglobulin M.</b> Confirm low-positive HSV-2 serology with a second method. <b>Routine serologic screening of asymptomatic adults is not recommended.</b> Evaluate genital ulcers for other causes including syphilis, by risk.",
  "<b>Treat EVERY first clinical episode</b> with oral acyclovir, valacyclovir or famciclovir.<br><b>Recurrent genital HSV:</b> patient-initiated episodic <b>or</b> daily suppressive therapy.<br><b>Topical antivirals provide minimal benefit</b> for genital herpes.",
  "<b>Suppressive valacyclovir lowers HSV-2 transmission; condoms reduce but do not eliminate risk.</b> <b>Avoid sexual or direct lesion contact during the prodrome or while lesions are active.</b> Reactivation triggers: <b>stress, illness, menstruation, ultraviolet light</b>. Differential: chancroid (painful necrotizing ulcers, <i>Haemophilus ducreyi</i>, inguinal nodes), syphilis (solitary raised papules that erode, <b>usually painless</b>), trauma, candidiasis."),

 ("l6_s127_1.jpg", "Herpetic whitlow",
  "<b>Painful herpes simplex infection of the DISTAL FINGER</b>, often after inoculation through broken skin. Prodromal burning or tingling, then <b>grouped vesicles on an erythematous, swollen digit</b>; fever or lymphangitis may occur.<br><span class=pt>&ldquo;My fingertip is swollen and throbbing, with little blisters on it.&rdquo;</span>",
  "<b>Confirm atypical cases with HSV amplification testing from a fresh vesicle or the lesion base.</b><br>Mimics <b>bacterial felon or paronychia, contact dermatitis, and blistering dactylitis</b>.",
  "<b>DO NOT INCISE AND DRAIN</b> &mdash; it does not treat HSV and can delay healing.<br><b>Early oral acyclovir, valacyclovir or famciclovir</b> may shorten symptoms; consider suppression for frequent recurrence.<br><b>Treat bacterial superinfection only when it is present.</b>",
  "<b>Cover the lesions, use hand hygiene, and avoid contact with mucosa or broken skin until healed.</b> An occupational risk for anyone whose hands are near other people's mouths."),

 ("l6_s131_1.jpg", "Molluscum contagiosum",
  "<b>Benign POXVIRUS infection.</b> <b>Discrete, smooth-surfaced, firm, flesh-coloured, dome-shaped pearly papules averaging 3&ndash;5&nbsp;mm</b>; <b>CENTRAL UMBILICATION is characteristic</b>. Asymptomatic, or tender or pruritic.<br><span class=pt>&ldquo;He's got little pearly bumps with a dimple in the middle.&rdquo;</span>",
  "<b>Clinical diagnosis</b>; <b>biopsy if uncertain</b>.<br>Differential: <b>basal cell carcinoma, sebaceous hyperplasia, condyloma acuminatum</b>.",
  "<b>Observation is appropriate for many patients</b> &mdash; procedures may blister, pigment or scar.<br><b>Berdazimer 10.3% gel (Zelsuvmi)</b>, once daily at home, <b>age 1 and over</b>.<br><b>Cantharidin 0.7% (Ycanth)</b>, applied by a clinician, <b>age 2 and over</b>.<br>Others: curettage or cryotherapy; <b>topical retinoids are off label</b>. Treat associated dermatitis.",
  "Spread by <b>direct skin contact, shared contaminated objects, and autoinoculation</b>; sexual contact is common in adults with genital lesions. <b>Most immunocompetent patients clear spontaneously, though it may take months to several years</b>; lesions are more numerous, larger or atypical with immunosuppression.<br><b>Genital lesions in a child require context-sensitive assessment &mdash; location alone does NOT prove abuse.</b> Genital lesions in adolescents or adults may be sexually transmitted; assess for other infections as appropriate. <b>Extensive or giant facial lesions warrant evaluation for immunosuppression, including HIV where appropriate.</b>"),

 ("l6_s142_1.jpg", "Verruca vulgaris (common warts)",
  "<b>Human papillomavirus</b> infecting keratinocytes; <b>confined to the epidermis</b>, though it expands and displaces the dermis, giving a false impression of depth. The underside is <b>round and smooth with NO ROOTS</b>.<br>Frequently <b>ages 5&ndash;20</b>; usually on the hands, favouring fingers and palms. Usually under 1&nbsp;cm, <b>elevated round papules with a rough greyish surface</b>. <b>Tiny red or black dots are thrombosed dilated capillaries &mdash; trimming the surface makes them more prominent.</b> <b>Periungual, lip and tongue warts are more common in nail biters.</b><br><span class=pt>&ldquo;Rough bumps on my fingers with little black dots in them.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> <b>Biopsy is generally unnecessary</b> but may suit <b>immunocompromised patients</b> or <b>lesions of uncertain etiology (ruling out squamous cell carcinoma)</b>.<br>Differential: <b>squamous cell carcinoma, molluscum contagiosum, seborrheic keratosis</b>.",
  "<b>Observation is reasonable &mdash; many resolve spontaneously.</b><br><b>Salicylic acid.</b><br><b>Cryotherapy every 2&ndash;3 weeks</b> &mdash; may cause pain, blistering and pigment change.<br><b>Biopsy or refer atypical, bleeding, ulcerated, growing or refractory lesions.</b>",
  "Transmitted by <b>skin-to-skin contact, autoinoculation and contaminated surfaces</b>. <b>No therapy eradicates the virus with certainty, and recurrence can occur.</b> Choose treatment by <b>location, symptoms, age, pregnancy status, immune status, and risk of scarring or dyspigmentation</b>. <b>Avoid excessive freezing or destructive therapy for benign lesions likely to resolve.</b> <b>Refer periungual, facial, extensive, recalcitrant, diagnostically uncertain or immunocompromised cases.</b>"),

 ("l6_s144_2.jpg", "Verruca plana (flat warts)",
  "<b>Multiple smooth, slightly elevated, FLAT-TOPPED, skin-coloured to light-brown papules.</b> Common on the <b>face, forehead, dorsal hands and shins</b>.<br><span class=pt>&ldquo;Lots of small flat bumps across my forehead and shins.&rdquo;</span>",
  "<b>Clinical diagnosis.</b>",
  "<b>Observation is reasonable because spontaneous resolution is common.</b><br>Options include carefully selected <b>salicylic acid, topical retinoids, or cryotherapy</b>.",
  "<b>Shaving can spread lesions through autoinoculation.</b> <b>Balance treatment against the risk of dyspigmentation and scarring</b> &mdash; particularly on the face."),

 ("l6_s146_1.jpg", "Verruca plantaris (plantar warts)",
  "On the <b>weight-bearing surface</b> of the foot. May <b>cluster together to form a MOSAIC wart</b>.<br><span class=pt>&ldquo;It feels like I'm walking on a stone.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> Distinguish from a <b>callus</b>, which does not interrupt the skin lines and has no capillary dots.",
  "<b>Plantar warts do not require therapy unless they are PAINFUL.</b><br><b>Salicylic acid 40%</b><br><b>Cryotherapy</b>",
  "Acquired from contaminated surfaces &mdash; communal floors and showers. Recurrence is common, and no treatment guarantees eradication."),
]

ROWS += [
 # ================= LECTURE 9 =================
 # All 81 embedded images were audited at full size. NOTE: 39 of this deck's 120
 # pictures are LINKED rather than embedded and do not exist inside the file, so
 # some conditions are illustrated from a neighbouring slide of the same module.
 ("SECTION", "Lecture 9 &middot; Pre-Malignant and Malignant Cutaneous Lesions"),

 ("l9_s008_2.jpg", "Actinic keratosis",
  "<b>Premalignant</b>, on a biologic continuum with keratinocyte carcinoma &mdash; not a separate entity. Small <b>0.2&ndash;0.6&nbsp;cm</b> flesh-coloured, pink or slightly hyperpigmented papules with a <b>sandpaper texture</b>; <b>more apparent by touch than by sight</b>. Sun-exposed face, scalp, ears, forearms, dorsal hands.<br><span class=pt>&ldquo;Rough patches that keep coming back, and I feel them more than I see them.&rdquo;</span>",
  "<b>Usually clinical</b>; dermoscopy supports it when the clinician is trained.<br><b>Shave or punch biopsy</b> when morphology or behaviour raises concern for squamous cell carcinoma, or the lesion persists or recurs after therapy. Interpretation must separate <b>actinic keratosis vs carcinoma in situ vs invasive carcinoma</b>.<br><b>Not features of a typical lesion</b> &mdash; bleeding, induration, ulceration or rapid enlargement.",
  "<b>Lesion-directed</b> (isolated, clear borders): liquid nitrogen cryotherapy &mdash; crusts and disappears over <b>10&ndash;14 days</b>.<br><b>Field-directed</b> (multiple lesions in one region &mdash; field cancerization): topical <b>fluorouracil</b>, <b>imiquimod</b>, <b>photodynamic therapy</b>; fluorouracil plus calcipotriene possibly.",
  "Daily broad-spectrum sun protection and protective clothing. Expect erythema and crusting from field therapy and complete the course. <b>About 1 in 1,000 lesions per year progresses to squamous cell carcinoma</b>, and cumulative FIELD risk matters more than any single lesion. Treatment reduces lesion burden but the field stays at risk &mdash; surveillance continues."),

 ("l9_s019_1.jpg", "Squamous cell carcinoma",
  "<b>The second most common skin cancer.</b> Prolonged CUMULATIVE sun exposure; may arise from an actinic keratosis. Small <b>red, conical, hard nodule that may ulcerate</b>; also a <b>non-healing ulcer</b>, warty nodule, or irregular pink plaque with haemorrhagic crust.<br><span class=pt>&ldquo;A sore on my lip that just won&rsquo;t heal.&rdquo;</span>",
  "<b>Biopsy.</b> Use <b>time course, firmness or induration, ulceration, site, immune status and pathology</b> &mdash; not morphology alone.<br><b>Red flags:</b> rapid growth, pain, bleeding, ulceration, induration, fixation, palpable regional nodes.<br><b>Differential:</b> actinic keratosis, carcinoma in situ (Bowen), keratoacanthoma, verruca, inflamed seborrheic keratosis, basal cell carcinoma, amelanotic melanoma, chronic ulcer.",
  "<b>In situ</b> (no high-risk features): imiquimod, topical fluorouracil, or curettage and electrodesiccation.<br><b>Invasive:</b> surgical excision or <b>Mohs</b>.<br><b>Advanced/metastatic:</b> programmed death 1 blockade; cetuximab.<br><b>Mohs indications:</b> lips, temples, ears, nose, genitalia; recurrent; perineural or perivascular invasion; <b>&gt;1&nbsp;cm on face or &gt;2&nbsp;cm on trunk/extremities</b>; immunosuppression; tumours in scars; genetic disease.",
  "<b>High-risk sites:</b> mucosal surfaces, lip, ear, scalp, temple, nose, genitalia. <b>&gt;10 tumours</b> means higher local recurrence and nodal metastasis. Common and often aggressive after transplant, with multiple tumours typically at <b>~5 years</b>. <b>Nicotinamide 500&nbsp;mg twice daily cuts new tumours by ~30%.</b> At least <b>annual skin AND node examination</b>. Metastatic rate <b>3&ndash;7%</b>."),

 ("l9_s029_1.jpg", "Basal cell carcinoma &mdash; nodular",
  "<b>The most common form of cancer.</b> INTERMITTENT intense ultraviolet exposure in fair skin. Papule or nodule with <b>central erosion</b>, slow growth over years to 1&ndash;2&nbsp;cm; <b>pearly or translucent</b> with <b>telangiectasias accentuated by STRETCHING the skin</b>.<br><span class=pt>&ldquo;A shiny bump by my nose that scabs and comes back.&rdquo;</span>",
  "<b>Shave or punch biopsy.</b> The <b>HISTOLOGIC</b> subtype determines behaviour and dictates treatment.<br>Clinical subtypes: superficial, nodular, pigmented, morpheaform. Histologic: superficial, nodular, micronodular, infiltrative.<br><b>Differential:</b> intradermal naevus, sebaceous hyperplasia, squamous cell carcinoma, actinic keratosis, scar/morphea, pigmented melanoma or seborrheic keratosis.",
  "<b>Superficial, selected:</b> imiquimod 5 nights weekly for 6&ndash;10 weeks, or fluorouracil twice daily up to 12 weeks &mdash; <b>confirm clearance afterwards</b>.<br><b>Surgery:</b> curettage and electrodesiccation, excision, or Mohs by size, site and histologic risk. <b>Excision recurrence &le;5%; Mohs cure ~98%.</b><br><b>Advanced/metastatic:</b> hedgehog inhibitors &mdash; vismodegib or sonidegib.",
  "<b>A second basal cell carcinoma develops in up to 50%</b> &mdash; at least annual full-skin examination is mandatory. <b>Nicotinamide 500&nbsp;mg twice daily cuts new tumours by ~20%</b> (the squamous figure is 30%). Slow-growing and highly curable early; morbidity comes from <b>local destruction</b>, recurrence and delayed diagnosis. <b>Mohs</b> for eyelids, nasolabial folds, canthi, external ear, temple; recurrence; tissue-sparing need; aggressive histology."),

 ("l9_s034_2.jpg", "Basal cell carcinoma &mdash; superficial",
  "Reddish, shiny, <b>scaly thin papules or plaques on back or chest</b>, sometimes with a <b>thready pearly border</b> and spotty edge pigmentation.<br><span class=pt>&ldquo;A dry red patch on my back that never quite clears.&rdquo;</span>",
  "<b>Shave or punch biopsy</b>, as for any basal cell carcinoma.<br>Distinguish from a <b>superficial inflammatory dermatosis</b> &mdash; which is why a &ldquo;patch of eczema&rdquo; that fails treatment gets sampled.",
  "The subtype most often suitable for <b>topical</b> therapy: imiquimod or fluorouracil, with clearance confirmed. Curettage and electrodesiccation also used.",
  "Warning patterns for basal cell carcinoma generally: <b>a pearly papule, an erythematous patch &gt;6&nbsp;mm, or a non-healing ulcer</b> &mdash; commonly face, trunk or lower legs."),

 ("l9_s030_2.jpg", "Basal cell carcinoma &mdash; pigmented and morpheaform",
  "<b>Pigmented:</b> stippled or focal pigmentation that <b>may mimic melanocytic disease</b>; the <b>pearly border and slow growth</b> discriminate.<br><b>Morpheaform/sclerosing:</b> a <b>scar-like or ivory-white</b> lesion whose extension beyond the visible pink segment is <b>clinically subtle</b>.<br><span class=pt>&ldquo;A scar on my cheek, but I never cut myself there.&rdquo;</span>",
  "<b>Biopsy.</b> Morpheaform disease carries a <b>higher risk of subclinical spread</b>, which is what makes margin control matter.",
  "<b>Mohs</b> for aggressive histology &mdash; morpheaform, micronodular or infiltrative &mdash; and for recurrent tumours or where tissue sparing matters.",
  "A scar with no history of injury deserves a second look. Pigmented disease is the one that gets mistaken for a melanocytic lesion."),

 ("l9_s044_2.jpg", "Malignant melanoma",
  "<b>4th most common cancer in the United States</b> and the <b>leading cause of death due to skin disease</b>; incidence doubled over 30 years. 2023: ~97,610 new invasive melanomas, ~7,990 deaths, <b>two-thirds of deaths in men</b>. Lifetime risk <b>~2% in white individuals; 0.1&ndash;0.5% in persons of colour</b>.<br><b>Subtypes:</b> superficial spreading (~2/3, radial then vertical growth); lentigo maligna (chronically sun-exposed skin, older adults); <b>nodular &mdash; rapid, often amelanotic, may LACK the classic features</b>; acral lentiginous.<br><span class=pt>&ldquo;This mole has changed shape and colour this year.&rdquo;</span>",
  "<b>ABCDE:</b> Asymmetry &middot; Border irregular, notched or poorly defined &middot; Colour variegation &middot; Diameter &gt;6&nbsp;mm &mdash; <b>though smaller lesions can be melanoma</b> &middot; Evolution.<br><b>Initial test: biopsy or excision.</b><br><b>Sentinel node biopsy</b> offered/discussed at <b>&ge;1.0&nbsp;mm</b> Breslow, or <b>&ge;0.8&nbsp;mm</b> with ulceration, high mitotic rate or lymphovascular invasion. It is a <b>STAGING</b> procedure and <b>may not itself improve overall survival</b>.<br><b>Level of invasion</b> is the anatomic layer reached (I epidermis &rarr; V subcutis) &mdash; the deck labels these only &ldquo;Level I&rdquo; to &ldquo;Level V&rdquo; and never says <i>Clark</i>, which is the conventional name for the same system; <b>Breslow thickness is the dominant prognostic variable</b>.",
  "<b>Re-excision margins:</b> in situ <b>0.5&ndash;1&nbsp;cm</b>; <b>&lt;1&nbsp;mm &rarr; 1&nbsp;cm</b>; <b>&gt;1&nbsp;mm &rarr; 1&ndash;2&nbsp;cm</b>.<br><b>Refer to an expert centre</b> for melanoma deeper than 1&nbsp;mm or with nodal/other-site spread.",
  "<b>Monthly self-examination</b> using ABCDE and ugly-duckling principles &mdash; <b>including scalp, back, palms, soles and nails</b>. Consistent ultraviolet protection; adhere to the specialist surveillance schedule. Breslow thickness must be measured accurately at the initial biopsy; ulceration and mitotic activity further modify stage-based prognosis."),

 ("l9_s045_1.jpg", "Nail unit melanoma",
  "Rare acral melanoma arising most often in the <b>MATRIX</b>. <b>Not clearly ultraviolet-driven; may occur in any skin tone.</b> <b>Thumb and great toe</b> are high-yield sites.<br><b>Signs:</b> new or evolving <b>longitudinal melanonychia in ONE digit</b>; increasing width; irregular colour, thickness or spacing of lines; <b>proximal widening or triangular shape</b>; blurred borders; nail splitting or dystrophy; ulceration or a subungual mass.<br><span class=pt>&ldquo;A dark stripe in one nail that&rsquo;s getting wider.&rdquo;</span>",
  "<b>Hutchinson sign</b> &mdash; periungual pigment extending onto the <b>proximal nail fold</b> &mdash; is highly concerning and should prompt <b>urgent expert evaluation regardless of other features</b>.<br><b>Amelanotic nail melanoma</b> may be red, pink, eroded or mass-like <b>with no dark band; absence of pigment does NOT exclude melanoma</b>.<br>Remove polish and inspect <b>every</b> nail, periungual skin, palms, soles and regional nodes. Onychoscopy.",
  "Coordinate dermatology, nail surgery and surgical oncology.<br><b>Digit-sparing wide excision or Mohs with immunostaining</b> for in situ and selected invasive tumours when margins can be reliably assessed.<br><b>Amputation is NOT automatic</b> &mdash; reserved for deep, extensive or bone-involving disease. Sentinel node discussion and systemic therapy follow melanoma stage and Breslow principles.",
  "<b>Delayed recognition contributes to advanced-stage presentation.</b> Check nails during self-examination. <b>Urgent referral:</b> new or changing single-digit melanonychia, proximal widening, Hutchinson sign, nail dystrophy with pigment; unexplained subungual mass or persistent ulceration/bleeding; a chronic &ldquo;wart&rdquo; or &ldquo;infection&rdquo; failing appropriate therapy."),

 ("l9_s082_1.jpg", "Nail unit squamous cell carcinoma / Bowen disease",
  "<b>The most common malignant nail tumour.</b> Chronic <b>unilateral verrucous periungual papule or plaque</b>, subungual hyperkeratosis, onycholysis, oozing, bleeding, ulceration, nail-plate destruction, longitudinal erythronychia, or pain &mdash; often <b>repeatedly labelled a wart, paronychia or fungal infection</b>.<br><span class=pt>&ldquo;They&rsquo;ve treated this as a wart three times and it&rsquo;s still there.&rdquo;</span>",
  "Associations: <b>high-risk human papillomavirus</b>, immunosuppression, chronic inflammation or trauma, prior radiation, older age. Periungual disease may be <b>multifocal</b>.<br>Biopsy any chronic lesion that fails appropriate therapy.",
  "<b>Complete margin-controlled surgery preferred</b> &mdash; Mohs or wide surgical excision. <b>Partial or limited destructive treatment carries a higher recurrence risk.</b><br>Distal phalanx or digital amputation reserved for bone invasion or disease that cannot otherwise be cleared.",
  "The recurring theme of this module is <b>diagnostic delay as a preventable harm</b>. A nail lesion that has been treated as something benign more than once is the one to biopsy."),

 ("l9_s087_1.jpg", "Glomus tumour and the benign nail tumours",
  "<b>Glomus tumour:</b> small <b>red-blue subungual focus</b> with <b>severe paroxysmal pain, exquisite point tenderness and cold sensitivity</b> &mdash; the nail may look nearly normal.<br><b>Onychopapilloma / onychomatricoma:</b> a single nail with <b>longitudinal erythronychia or leukonychia</b>, distal subungual hyperkeratosis, splinter haemorrhages or localised plate abnormality.<br><span class=pt>&ldquo;It&rsquo;s agony in cold water and I can point to the exact spot.&rdquo;</span>",
  "The glomus <b>triad strongly suggests</b> the diagnosis but <b>does not replace imaging or specialist evaluation</b>.<br>Other benign tumours that mimic malignancy: acquired digital fibrokeratoma, melanocytic naevus or lentigo, pyogenic granuloma, digital myxoid cyst, subungual exostosis.",
  "<b>Diagnosis-specific surgical removal</b> when symptoms, growth or diagnostic uncertainty warrant it.",
  "These matter <b>because they mimic malignancy</b> &mdash; and because a painful nail with a normal-looking plate is easy to dismiss."),

 ("l9_s062_4.jpg", "Kaposi sarcoma",
  "Caused by <b>human herpesvirus 8 combined with a weakened immune system</b>, arising in the cells lining <b>blood and lymph vessels</b>. <b>Red or purple macules, plaques or nodules</b> on skin or mucous membranes.<br><b>Four forms:</b> <b>classic</b> (older men, chronic, rarely fatal); <b>endemic</b> (young Black men in equatorial Africa, often aggressive); <b>iatrogenic</b> (immunosuppressive therapy); <b>epidemic</b> (acquired immunodeficiency).<br><span class=pt>&ldquo;Purple patches on my legs, and my mouth is sore.&rdquo;</span>",
  "<b>ORAL EXAMINATION IS ESSENTIAL</b> when Kaposi sarcoma is suspected &mdash; <b>hard palate lesions are common and may be the presenting site</b>.<br><b>Marked oedema may occur with few or no visible skin lesions &mdash; do not use oedema severity to gauge disease burden.</b><br><b>Differential:</b> bacillary angiomatosis, angioma/haemangioma, purpura, venous stasis, pyogenic granuloma, lymphoma, metastatic disease.",
  "<b>Epidemic (AIDS-associated) &mdash; FIRST PRIORITY: begin or optimise antiretroviral therapy.</b> Immune restoration is the cornerstone.<br><b>Classic/older adult:</b> palliative local therapy &mdash; intralesional vincristine, vinblastine or bleomycin, or radiation.<br><b>Iatrogenic:</b> reduce immunosuppressive doses where feasible &mdash; <b>coordinate with the transplant team first</b>.<br><b>Systemic first-line:</b> liposomal doxorubicin and paclitaxel. <b>Antiretroviral therapy plus chemotherapy beats antiretroviral therapy alone in advanced disease.</b>",
  "Report respiratory or gastrointestinal symptoms &mdash; visceral disease. Referral spans dermatology for biopsy, human immunodeficiency virus care, medical oncology, pulmonology or gastroenterology, the transplant team before any dose change, and palliative care."),

 ("l9_s072_1.jpg", "Cutaneous T-cell lymphoma (mycosis fungoides)",
  "A cutaneous T-cell lymphoma that <b>begins in the skin and may remain confined there for years or decades</b>. Early: localised or generalised <b>erythematous patches or scaly plaques, usually on the trunk</b>, <b>frequently &gt;5&nbsp;cm</b>. <b>May resemble psoriasis, eczema or tinea</b>, which is why diagnosis is often delayed.<br><span class=pt>&ldquo;They&rsquo;ve called it eczema for four years and nothing works.&rdquo;</span>",
  "<b>Two clues:</b> <b>itch out of proportion</b> to the apparent inflammatory activity, and <b>follicular involvement with hair loss</b> &mdash; folliculotropism discriminates from routine eczema or psoriasis.<br><b>Discriminators:</b> chronicity, treatment resistance, large or oddly distributed plaques, severe pruritus, tumours or erythroderma, nodes, and histology.<br>Enlarged nodes <b>may be benign dermatopathic change OR lymphoma</b> &mdash; directed biopsy or imaging is required.",
  "<b>Stage-directed, skin-first.</b> <b>Early aggressive treatment has NOT been proven to cure or prevent progression, and may cause complications and premature death.</b><br><b>Initial skin-directed:</b> topical corticosteroids, topical mechlorethamine, bexarotene gel, ultraviolet phototherapy.<br><b>Progressive:</b> PUVA &plusmn; retinoids or interferon; methotrexate; extracorporeal photopheresis; systemic bexarotene; romidepsin or vorinostat; brentuximab or mogamulizumab; total-skin electron-beam treatment.",
  "Diagnosis may take repeated biopsies over time. Referral: dermatology/dermatopathology early for persistent suspicious disease; a cutaneous lymphoma centre once blood, node, tumour or erythrodermic involvement is suspected."),
]

ROWS += [
 # ================= LECTURE 8 =================
 ("SECTION", "Lecture 8 &middot; Pigmented Skin Lesions"),

 ("l8_s006_1.jpg", "Ephelides (freckles)",
  "Asymptomatic small <b>light brown symmetric macules, 3&ndash;5&nbsp;mm</b>, on sun-exposed skin of fair-skinned people, often with blonde or red hair and possibly Celtic ancestry. Autosomal dominant. <b>More pronounced in spring and summer, fading in winter</b>; first appear in young children and <b>regress later in life</b>.<br><span class=pt>&ldquo;I've had freckles since I was small &mdash; they come out every summer.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> Histopathology (not needed) shows a normal to reduced number of hypertrophic melanocytes with increased melanin in the basal epidermal layer.<br><b>Main differential: lentigines.</b>",
  "<b>1st: sun protection, with proper patient education and counselling &mdash; this is the key.</b><br><b>2nd:</b> topical depigmenting agents &mdash; hydroquinone, retinoids, alpha-hydroxy acids, botanicals.<br><b>Preferred procedure:</b> intense pulsed light or laser, though lesions can relapse.<br><span class=warn>NO CRYOTHERAPY &mdash; difficult because of the size of the lesions.</span>",
  "Related to a mutation in the <b>MCR-1</b> gene &mdash; the receptor for alpha-melanocyte-stimulating hormone, which activates melanogenesis via cyclic adenosine monophosphate. Decreased pathway activity promotes <b>pheomelanin</b>, the yellow-red sulfur-containing pigment. <b>The distinction from lentigines: freckles fade when the sun goes; lentigines do not.</b>"),

 ("l8_s011_3.jpg", "Lentigines",
  "Common melanocytic lesion, &ldquo;age spots&rdquo;. <b>Benign, well-circumscribed, round to oval, uniformly black or brown macules under 5&nbsp;mm.</b> On skin, conjunctiva and mucocutaneous surfaces, and on <b>both sun-exposed and sun-protected</b> areas. <b>Bimodal age distribution</b> &mdash; early childhood or later life. <b>Do NOT fade with cessation of sun exposure.</b><br>Types: lentigo simplex, acral, agminated (a grouping of small light brown macules), generalised.",
  "<b>Clinical diagnosis.</b>",
  "<b>Treatment is not necessary.</b><br><b>Cosmetic removal if the patient prefers:</b> cryotherapy or quality-switched laser.",
  "Can be associated with isolated or inherited disorders. <span class=warn>An inherited disorder should be considered if a partial or generalised lentigo is present</span> &mdash; for example LAMB or myxoma syndrome. Lentigo simplex does not carry the mutations found in solar lentigo, PUVA lentigines or common acquired naevi."),

 ("l8_s014_1.jpg", "Solar lentigo <span class=\"dup\">also Lecture 3</span>",
  "Arises from proliferation of basal melanocytes with increased melanin production. <b>Well-defined but with irregular borders, tending to coalesce at sites of severe sunburn</b>; from under 1&nbsp;mm to several centimetres; light to dark brown. Over time they enlarge, darken, stay stable, regress, or <b>progress into lichenoid keratoses</b>.<br><b>PUVA lentigines</b> appear on sun-protected sites (buttocks, genitalia) as well as exposed, with brown/black irregular pigmentation.",
  "<b>Dermoscopy</b> &mdash; finger-like projections, &ldquo;moth-eaten&rdquo; border.<br><span class=warn>Biopsy if atypical or uncertain, especially to exclude lentigo maligna</span> (asymmetric, irregular border and colour, darker areas; structureless irregular pigment on dermoscopy). Reflectance confocal microscopy as an adjunct.",
  "<b>Treatment is not necessary.</b><br><b>Cosmetic removal:</b> retinoids, cryotherapy, or quality-switched laser.",
  "<b>Strongly associated with older age (90% at 50), sun damage, ephelides, tanning, and birth control use.</b> Also associated with actinic keratosis, squamous cell carcinoma, basal cell carcinoma and melanoma. PUVA lentigines relate to total number of treatments, male sex, fair skin and older age."),

 ("l8_s017_2.jpg", "Seborrheic keratosis",
  "<b>Benign papules and plaques, beige to brown to black, 2&ndash;20&nbsp;mm</b>, feeling <b>velvety or warty</b> and appearing <b>stuck or pasted onto the skin</b>. Common in older adults.<br><span class=pt>&ldquo;A dark warty growth that looks like it's been stuck on.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> Dermoscopy shows comedone-like openings.",
  "<b>Management is supportive.</b><br><b>If itchy or inflamed:</b> cryotherapy may help &mdash; <b>however they do recur after treatment.</b>",
  "<span class=warn>Easily mistaken for neoplasms</span> &mdash; which is exactly why they matter in an older adult presenting with a new dark growth."),

 ("l8_s019_2.jpg", "Dermatosis papulosa nigrans",
  "<b>Multiple small (1&ndash;5&nbsp;mm), smooth, firm, black or dark brown papules on the face and neck.</b> <b>Identical to small seborrheic keratoses.</b> Common in African Americans, dark-skinned Asians and Polynesians; <b>females more than males</b>.<br><span class=pt>&ldquo;These little dark bumps on my cheeks &mdash; my mother has them too.&rdquo;</span>",
  "<b>Clinical diagnosis</b> (biopsy if uncertain).",
  "<b>Best left untreated.</b><br><b>If treatment is wanted:</b> excision, curettage or laser.<br><span class=warn>AVOID CRYOTHERAPY &mdash; post-inflammatory hyperpigmentation.</span>",
  "Likely genetic, and believed to be a <b>developmental defect of the hair follicle</b>. Benign."),

 ("l8_s022_1.jpg", "Vitiligo",
  "Common autoimmune disease causing depigmentation through <b>T-cell mediated destruction of melanocytes</b>. Can begin at any age but usually starts before the thirties &mdash; half before 20, a third before 12. Males and females equally affected.<br><b>Asymptomatic white, non-scaly macules and patches with distinct margins that FLUORESCE under a Wood's lamp.</b> Usually symmetrical; face, acral and genital areas are often the initial sites.<br><b>Segmental variant:</b> unilateral, does not cross the midline, block-like patterns, with unpredictable cycles of flare and stabilisation.<br><span class=pt>&ldquo;White patches are spreading and people stare &mdash; I've stopped going out.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> <b>Wood's lamp examination in a DARK ROOM.</b><br><b>Labs</b> to correlate with associated autoimmune disease: complete blood count and antinuclear antibody.<br><span class=warn>Distinguishing segmental from non-segmental matters &mdash; they differ in diagnostic tools and treatment.</span>",
  "<b>Under 5% body surface (with phototherapy):</b> topical steroids (good efficacy, easy, cheap &mdash; watch skin atrophy and intraocular pressure) <i>or</i> topical calcineurin inhibitors &mdash; tacrolimus, pimecrolimus &mdash; safe and good for face, neck, intertriginous areas and children, but with <span class=warn>increased cancer risk</span>.<br><b>Over 5% body surface: PHOTOTHERAPY is first line &mdash; narrowband ultraviolet B, preferred over PUVA</b> (PUVA raises skin cancer risk). <b>Combination of topical + phototherapy is ideal.</b><br><b>Surgical (tissue and cellular grafting): only for highly stable disease.</b>",
  "<span class=warn>Do not dismiss it as &ldquo;cosmetic&rdquo;.</span> It affects patients psychologically and socially through low self-esteem and poor body image. <b>Psychological intervention is part of management</b>, alongside cosmetic and non-traditional therapies. Management is multifactorial &mdash; take a thorough medical, social and family history."),

 ("l8_s029_2.jpg", "Congenital melanocytic naevus",
  "Pigmented neoplasms of melanocytes evident <b>at birth or shortly after</b>, from somatic mutations. Flat brown patches or plaques with smooth or slightly uneven borders; may be pebbly, rugose, verrucous or lobular. Small, medium or large. Most commonly trunk and extremities, though scalp and face are affected.<br><b>The larger the lesion, the higher the risk for melanoma.</b>",
  "<b>Clinical diagnosis</b>; sometimes biopsy.<br><span class=warn>If on the cranium or axial midline, consider NEUROCUTANEOUS MELANOSIS &mdash; get MRI brain with or without total spine, concordant with the anatomic location of the naevus.</span>",
  "<b>Depends on melanoma risk plus cosmetic and functional considerations.</b> The goal is to remove as much as possible while preserving function and improving appearance. <b>Observation versus surgical &mdash; ideally surgical, but if there is little skin for a graft site, observation may be the better option.</b> Symptoms are another indication.",
  "<b>Risk: neurofibromatosis type I.</b> Neurocutaneous melanosis affects patients with naevi on head, neck or posterior midline &mdash; seizures, hydrocephalus, neurological deficits and vomiting within the first few years of life, and <b>the prognosis is poor once neurological symptoms appear</b>. <b>Counselling and support groups</b> assist families and patients with large naevi."),

 ("l8_s033_1.jpg", "Naevus spilus",
  "&ldquo;Spotted naevus&rdquo; &mdash; a variant of congenital naevus, present at birth or in the first years of life. <b>Background pigmentation is circumscribed and similar to a café-au-lait spot in hue, with even light pigmentation</b>, carrying <b>scattered superimposed more darkly pigmented macules or papules</b>. The tan macular background ranges from under 1&nbsp;cm to over 10&nbsp;cm. Most commonly trunk and extremities.",
  "<b>Clinical.</b>",
  "<b>Observation with periodic clinical evaluation.</b>",
  "<b>Rarely progresses to melanoma.</b> Sun protection counselling. Associated with other anomalies of <b>vascular, central nervous system or connective tissue</b> origin."),

 ("l8_s036_1.jpg", "Common acquired melanocytic naevus (mole)",
  "Develops slowly after birth, enlarges symmetrically, stabilises and regresses. <b>Numbers peak in the thirties and decline afterwards.</b> Usually <b>under 6&nbsp;mm</b>, homogenous surface and colour (skin coloured, brown, pink), round to oval with sharp demarcation. Can be anywhere.<br><span class=warn>Very dark brown or black on a light-skinned individual is suspicious.</span>",
  "<b>Clinical diagnosis.</b>",
  "<b>Observation.</b><br><b>Remove for cosmetic reasons or symptomatic relief.</b>",
  "<b>Proper counselling on sun protection.</b> Melanoma risk increases with the number of naevi. Increased numbers in patients with light skin tone and those who tend to sunburn. Risk factors: ultraviolet exposure, male sex, and a genetic component."),

 ("l8_s039_1.jpg", "Blue naevus",
  "A group of lesions composed of <b>deeply pigmented spindle or epithelioid melanocytes in the DERMIS</b>. Affects women more than men, most commonly in their <b>twenties</b>. Blue, blue-grey or blue-black. On the <b>dorsal hands and feet, scalp, buttocks or sacral region</b>.<br><b>Common blue:</b> deeply pigmented, under 1&nbsp;cm, arising in adolescence.<br><b>Cellular blue:</b> larger plaques or nodules over 1&nbsp;cm, arising before age 40.",
  "<b>Clinical for small lesions.</b><br><b>Biopsy for larger lesions.</b>",
  "<b>Observation.</b><br><b>Biopsy or excision if changes are noted.</b>",
  "Includes common blue, cellular blue, combined blue and atypical cellular blue lesions."),

 ("l8_s041_1.jpg", "Pigmented spindle cell naevus (Reed)",
  "Commonly in the <b>thirties</b>; <b>females more than males</b>. Found on the extremities, <b>mainly the lower extremities and especially the thigh</b>. A <b>sharply circumscribed darkly pigmented papule, usually under 7&nbsp;mm, JET-BLACK</b> but may have shades of blue, grey or brown. <b>Benign.</b>",
  "<b>Confirm with biopsy.</b>",
  "<b>Excision with negative margins.</b>",
  "Benign despite the alarming jet-black appearance &mdash; but it is one of the lesions in this lecture that gets a knife rather than a follow-up appointment."),

 ("l8_s042_1.jpg", "Spitz naevus",
  "Usually benign, with a <b>phase of growth (fast or slow) followed by a stable period</b>. <b>Solitary, asymptomatic, pink or red, hairless, firm and dome-shaped.</b> Several millimetres to centimetres. Located on face, neck, trunk and extremities; <b>SPARES palms, soles and mucous membranes</b>.<br><span class=warn>Sometimes resembles melanoma.</span>",
  "<b>Biopsy versus wide excision.</b>",
  "<b>Excision.</b>",
  "<b>Multiple lesions can be associated with a familial cancer syndrome.</b>"),

 ("l8_s043_1.jpg", "Dysplastic melanocytic naevus",
  "Common in Caucasians. <b>At least 5&nbsp;mm in diameter with irregular, indistinct borders</b>, variable pigmentation (tan to brown) with a smooth or <b>&ldquo;pebbly&rdquo;</b> surface. Common on sun-exposed skin.<br>In <b>dysplastic naevus syndrome</b> there can be <b>over 100 naevi by adolescence</b>.<br><span class=warn>May progress to melanoma &mdash; the higher the number of naevi, the higher the risk.</span>",
  "<b>Diagnosis is by biopsy.</b>",
  "<b>Observation.</b><br><b>Biopsy on ALL changing or developing lesions.</b><br><b>Excision where there is concern for melanoma.</b><br><b>Sun protection.</b>",
  "<b>Risk factor: family history.</b> The relationship between naevus count and melanoma risk is the point to carry away."),
]



# Labs to send, per condition, taken from the decks. "None" is a real answer
# here and is stated rather than left blank -- most of dermatology is a clinical
# diagnosis, and knowing which conditions genuinely need bloods is the point of
# the column. Keyed by the row's name with any badge markup stripped.
LABS = {
 # ---- Lecture 9 (Jaquith). Skin cancer is a TISSUE diagnosis, not a blood one:
 # every entry here turns on biopsy and histology. The blood work that does
 # appear is about the HOST -- immune status -- rather than the tumour.
 "Actinic keratosis": "<b>None.</b> Usually a clinical diagnosis; <b>shave or punch biopsy</b> when behaviour or morphology raises concern for squamous cell carcinoma, or when a lesion persists or recurs after therapy.",
 "Squamous cell carcinoma": "<b>No routine bloods.</b> Diagnosis is by <b>biopsy</b>. Investigate the HOST where relevant &mdash; transplant, chronic lymphocytic leukaemia, or human immunodeficiency virus status all raise risk and aggressiveness, and coordinate transplant, haematology or HIV care.",
 "Basal cell carcinoma &mdash; nodular": "<b>None.</b> <b>Shave or punch biopsy</b>; the histologic subtype determines behaviour and dictates treatment.",
 "Basal cell carcinoma &mdash; superficial": "<b>None</b> &mdash; biopsy as for any basal cell carcinoma.",
 "Basal cell carcinoma &mdash; pigmented and morpheaform": "<b>None</b> &mdash; biopsy, with margin control the issue rather than any laboratory test.",
 "Malignant melanoma": "<b>No blood test makes the diagnosis</b> &mdash; it is <b>biopsy or excision</b>, and <b>Breslow thickness</b> from that specimen is the dominant prognostic variable. <b>Sentinel lymph node biopsy</b> is a staging procedure offered at &ge;1.0&nbsp;mm, or &ge;0.8&nbsp;mm with ulceration, high mitotic rate or lymphovascular invasion.",
 "Nail unit melanoma": "<b>None.</b> Diagnosis is by <b>nail unit biopsy</b> after onychoscopy; staging follows melanoma principles.",
 "Nail unit squamous cell carcinoma / Bowen disease": "<b>No routine bloods.</b> Biopsy any chronic lesion failing appropriate therapy. Associations worth noting in the history: <b>high-risk human papillomavirus</b> and <b>immunosuppression</b>.",
 "Glomus tumour and the benign nail tumours": "<b>None.</b> The clinical triad suggests it; <b>imaging and specialist evaluation</b> are still required, and the triad does not replace them.",
 "Kaposi sarcoma": "<b>Human immunodeficiency virus testing and staging matter here</b> &mdash; immune status defines the clinical form and drives treatment. Diagnosis itself is by <b>biopsy</b>. In epidemic disease the first priority is starting or optimising <b>antiretroviral therapy</b>.",
 "Cutaneous T-cell lymphoma (mycosis fungoides)": "<b>Histology</b> is the diagnosis, and it often takes <b>repeated biopsies over time</b>. Blood involvement is assessed when S&eacute;zary syndrome or erythroderma is suspected; enlarged nodes need <b>directed biopsy or imaging</b> rather than assumption.",

 # ---- Lecture 6 (Jaquith). Almost nothing here needs blood work; the two
 # places it does are both about the DRUG rather than the disease, which is the
 # distinction worth carrying into the exam.
 "Tinea capitis (scalp)": "<b>No bloods for the diagnosis.</b> But <b>baseline liver tests when indicated by the selected systemic agent, its labeling and patient risk</b> &mdash; oral therapy is mandatory here, so this is where it comes up. Review drug interactions and hepatic disease.",
 "Black dot tinea capitis": "<b>None</b> &mdash; the same scalp workup; potassium hydroxide and culture.",
 "Tinea barbae &mdash; inflammatory": "<b>No bloods.</b> <b>Bacterial culture</b> to exclude bacterial folliculitis; biopsy for refractory cases.",
 "Tinea barbae &mdash; noninflammatory": "<b>No bloods.</b> Potassium hydroxide and culture; bacterial culture to exclude folliculitis.",
 "Tinea corporis (body) &mdash; &ldquo;ringworm&rdquo;": "<b>None.</b> Potassium hydroxide from the active border; culture when suspicion is high and the preparation is negative. <b>Species identification and susceptibility testing</b> where resistance is suspected.",
 "Tinea cruris (groin) &mdash; &ldquo;jock itch&rdquo;": "<b>None</b> &mdash; potassium hydroxide from the active border for uncertain cases.",
 "Tinea pedis &mdash; interdigital": "<b>No bloods.</b> <b>Add bacterial studies</b> for marked maceration, malodor, erosion, drainage, ulceration or cellulitis.",
 "Tinea pedis &mdash; hyperkeratotic": "<b>None</b> &mdash; potassium hydroxide from the advancing scale; culture if atypical or refractory.",
 "Tinea pedis &mdash; vesiculobullous": "<b>None</b> &mdash; potassium hydroxide; bacterial studies if macerated or draining.",
 "Onychomycosis (tinea unguium)": "<b>No bloods for the diagnosis</b> &mdash; but <b>baseline liver tests per labeling and patient risk before oral terbinafine</b>, with a review of hepatic disease and interactions. Confirm fungus first: potassium hydroxide, periodic acid&ndash;Schiff of clippings, culture, or polymerase chain reaction.",
 "Tinea manuum (hand)": "<b>None</b> &mdash; potassium hydroxide and culture, as for the corresponding site.",
 "Id (dermatophytid) reaction": "<b>None.</b> The diagnosis is made by the <b>pattern of potassium hydroxide results</b> &mdash; positive at the primary site, <b>negative at the reaction site</b>.",
 "Tinea incognito": "<b>None</b> &mdash; potassium hydroxide and culture from an active edge, after stopping the corticosteroid.",
 "Cutaneous candidiasis and intertrigo": "<b>No bloods routinely.</b> But <b>recurrent or extensive disease warrants evaluation for diabetes and immunosuppression</b>.",
 "Pityriasis versicolor (tinea versicolor)": "<b>None.</b> Potassium hydroxide shows short hyphae with clusters of yeast. <b>Review hepatic risk, pregnancy status and drug interactions before oral fluconazole or itraconazole.</b>",
 "Varicella (chickenpox)": "<b>None routinely</b> &mdash; usually clinical; <b>lesion polymerase chain reaction</b> when confirmation is needed.",
 "Herpes zoster (shingles)": "<b>None routinely</b> &mdash; typical dermatomal disease is clinical. <b>Polymerase chain reaction from vesicle fluid, scab or lesion base</b> for atypical, disseminated, vaccine-modified or immunocompromised presentations. Adjust antiviral dosing for <b>renal function</b>.",
 "Postherpetic neuralgia": "<b>None</b> &mdash; clinical. Individualize treatment for <b>kidney function</b>, falls risk, anticholinergic burden and interactions.",
 "Herpes zoster ophthalmicus": "<b>None</b> &mdash; clinical; the urgency is the <b>same-day ophthalmology evaluation</b>, not a test.",
 "Ramsay Hunt syndrome (herpes zoster oticus)": "<b>None</b> &mdash; clinical; urgent ear, nose and throat or neurology evaluation.",
 "Herpes simplex virus (HSV-1 and HSV-2)": "<b>Type-specific serology has selected uses</b>, but <b>low-positive results may be false positive</b> &mdash; confirm with a second method. <b>Do NOT use immunoglobulin M.</b> <b>Routine serologic screening of asymptomatic adults is not recommended.</b> The diagnosis is made by <b>lesion amplification testing</b>, not by blood.",
 "Herpetic whitlow": "<b>None</b> &mdash; confirm atypical cases with amplification testing from a fresh vesicle or the lesion base.",
 "Molluscum contagiosum": "<b>No bloods routinely.</b> <b>Extensive or giant facial lesions warrant evaluation for immunosuppression, including HIV testing where appropriate.</b>",
 "Verruca vulgaris (common warts)": "<b>None</b> &mdash; clinical. Biopsy is generally unnecessary but may suit immunocompromised patients or lesions of uncertain etiology.",
 "Verruca plana (flat warts)": "<b>None</b> &mdash; clinical diagnosis.",
 "Verruca plantaris (plantar warts)": "<b>None</b> &mdash; clinical diagnosis.",

 # ---- Lecture 2
 "Atopic dermatitis": "<b>None routinely.</b> Raised immunoglobulin E supports it but is not routinely tested. Culture purulent, pustular or crusted lesions; herpes simplex polymerase chain reaction for painful monomorphic erosions.",
 "Dyshidrotic eczema": "<b>None</b> &mdash; clinical diagnosis.",
 "Nummular eczema": "<b>No bloods.</b> Potassium hydroxide preparation if tinea cannot be ruled out; bacterial culture if secondarily infected; patch testing if chronic or recurrent.",
 "Irritant contact dermatitis": "<b>None</b> &mdash; clinical diagnosis from the exposure.",
 "Allergic contact dermatitis": "<b>No bloods.</b> Patch testing identifies the allergen.",
 "Seborrheic dermatitis": "<b>None</b> &mdash; clinical diagnosis.",
 "Perioral dermatitis": "<b>No bloods.</b> Potassium hydroxide if tinea or Candida suspected; bacterial culture if pustules, crusting or drainage; patch testing; biopsy if persistent or atypical.",
 "Diaper dermatitis": "<b>No bloods.</b> Potassium hydroxide if Candida suspected; bacterial culture if purulence, bullae, crusting or perianal disease.",
 "Stasis dermatitis": "<b>No bloods.</b> Ankle-brachial index or toe pressure before compression; venous duplex ultrasound if reflux, obstruction or thrombosis suspected.",
 "Bullous pemphigoid": "<b>Serum indirect immunofluorescence or ELISA</b> for anti-basement membrane zone antibodies, alongside the biopsy and direct immunofluorescence.",
 "Pemphigus (vulgaris)": "<b>Serum ELISA</b> for pathogenic antibodies, plus immunofluorescence studies &mdash; both confirmatory after the biopsy.",
 "Psoriasis &mdash; plaque": "<b>None for diagnosis.</b> Systemic agents carry their own monitoring &mdash; methotrexate always with folic acid.",
 "Psoriasis &mdash; guttate": "<b>None</b> &mdash; clinical diagnosis.",
 "Psoriasis &mdash; pustular": "<b>None for diagnosis.</b> Acitretin is contraindicated in pregnancy, so establish pregnancy status before prescribing.",
 "Pityriasis rosea": "<b>None</b> &mdash; clinical, on the herald patch and the pattern.",
 "Lichen planus": "<b>No bloods.</b> Biopsy is the test.",
 "Lichen simplex chronicus": "<b>None for the plaque itself.</b> <span class=warn>Generalised or unexplained pruritus triggers a targeted systemic evaluation</span> guided by history, medications and review of systems.",
 "Alopecia areata": "<b>None</b> &mdash; clinical with dermoscopy; scalp biopsy only if scarring, diffuse atypical loss or persisting uncertainty.",
 "Androgenetic alopecia": "<b>None routinely.</b> Additional testing can be done to exclude other causes of alopecia.",
 "Xeroderma (xerosis)": "<b>None</b> &mdash; clinical diagnosis.",
 # ---- Lecture 3
 "Erythema multiforme": "<b>Complete blood count, comprehensive metabolic panel and liver function tests</b> if erythema multiforme major or systemic involvement is a concern. Herpes simplex polymerase chain reaction; <b>Mycoplasma serology / immunoglobulin M</b>.",
 "Dermatitis herpetiformis": "<b>Immunoglobulin A anti-tissue transglutaminase and anti-endomysial antibody</b>, plus small bowel biopsy. Screen thyroid function given the association.",
 "Acanthosis nigricans": "<b>Haemoglobin A1c, fasting insulin and a lipid panel</b>, plus a polycystic ovarian syndrome workup.",
 "Epidermolysis bullosa": "<b>Genetic panel and nutritional labs</b>, alongside the electron microscopy and antigen mapping.",
 "Urticaria": "<b>Thyroid-stimulating hormone, complement C4, serum tryptase and specific immunoglobulin E.</b>",
 "Erythema nodosum": "<b>Antistreptolysin O titre, inflammatory markers, chest radiograph, tuberculin or interferon gamma release assay</b>; colonoscopy; <b>pregnancy test</b> where relevant.",
 "Granuloma annulare": "<b>Screen for diabetes (haemoglobin A1c), thyroid disease and dyslipidaemia</b> &mdash; and in generalised disease in an adult over fifty, workup for lymphoma.",
 "Pyoderma gangrenosum": "<b>Serum protein electrophoresis, antineutrophil cytoplasmic and antinuclear antibodies</b>, inflammatory markers; colonoscopy. Wound cultures to exclude infection.",
 "Acne rosacea": "<b>Antinuclear antibody</b> only if lupus is a consideration &mdash; it helps rule autoimmune disease OUT; a positive result means more testing, not a diagnosis.",
 "Hyperhidrosis": "<b>Only in suspected SECONDARY disease</b> &mdash; generalised or nocturnal sweating: <b>24-hour urine metanephrines and catecholamines, thyroid-stimulating hormone</b>, glucose.",
 "Stevens-Johnson syndrome": "<b>Complete blood count, comprehensive metabolic panel, liver function tests, urea and creatinine.</b> Blood cultures if secondary infection suspected. Chest radiograph.",
 "Toxic epidermal necrolysis": "The same, plus the <b>SCORTEN variables: urea, bicarbonate and glucose</b>, with heart rate and detachment area, within 24 hours and repeated day 3.",
 "Sunburn": "<b>None</b> &mdash; clinical diagnosis.",
 "Drug-induced photosensitivity": "<b>No bloods.</b> Phototesting (minimal erythema dose) and photopatch testing are the investigations.",
 "Photodermatitis (phytophotodermatitis)": "<b>Antinuclear antibody panel</b> if lupus is suspected. Otherwise exposure history and photopatch testing.",
 "Polymorphous light eruption": "<b>Antinuclear antibody panel is MANDATORY</b> to exclude lupus, especially anti-Ro/SSA and anti-La/SSB. <b>Porphyrin screen</b> (urine, stool, red cell) if erythropoietic protoporphyria is suspected.",
 "Actinic keratosis": "<b>None</b> &mdash; clinical, with biopsy for concerning features.",
 "Dermatoheliosis (photoaging)": "<b>None routinely.</b> Genetic testing and a DNA repair assay only if xeroderma pigmentosum is suspected.",
 # ---- Lecture 4
 "Acne vulgaris": "<b>None</b> &mdash; clinical. Culture only if there is no response to treatment. Isotretinoin requires <b>pregnancy tests before, monthly during, and 5 weeks after</b>.",
 "Folliculitis": "<b>No bloods.</b> Culture and Gram stain of unroofed pustule material; potassium hydroxide on a plucked hair; nasal swab for staphylococcal carriage.",
 "Pseudomonas (&ldquo;hot tub&rdquo;) folliculitis": "<b>None usually.</b> Bacterial culture from a pustule or the contaminated water if unclear or resistant.",
 "Pseudofolliculitis barbae": "<b>None</b> &mdash; clinical diagnosis.",
 "Furuncle": "<b>No bloods.</b> Culture the material obtained at aspiration or incision and drainage, to identify the organism and check for resistance.",
 "Carbuncle": "<b>No bloods.</b> Culture from aspiration or incision and drainage.",
 "Hidradenitis suppurativa": "<b>None</b> &mdash; clinical, on lesions plus distribution plus recurrence. Biopsy is not usually required.",
 "Erythrasma": "<b>None</b> &mdash; Wood's lamp coral-red fluorescence is the test.",
 "Impetigo &mdash; non-bullous": "<b>Culture</b> if high risk for methicillin-resistant Staphylococcus aureus (health-care worker, teacher) or if post-streptococcal glomerulonephritis is present. Otherwise none.",
 "Impetigo &mdash; bullous": "As for non-bullous &mdash; <b>culture only on the stated indications</b>.",
 "Ecthyma": "As for impetigo &mdash; <b>culture on the stated indications</b>.",
 "Erysipelas": "<b>Leukocytosis, raised erythrocyte sedimentation rate and C-reactive protein are common but not diagnostic.</b> <span class=warn>Blood and tissue cultures are NOT cost effective &mdash; extremely low yield.</span>",
 "Cellulitis": "<b>No workup at all</b> in limited disease with no systemic signs and no risk factor. <b>Serious infection: blood cultures, skin punch biopsy, complete blood count (leukocytosis) and creatine phosphokinase</b> for muscle damage.",
 "Abscess": "<b>No bloods.</b> Culture the drained material, considering methicillin-resistant Staphylococcus aureus, then narrow to the result.",
 "Acute paronychia": "<b>No bloods.</b> Gram stain and culture for the bacterial cause; potassium hydroxide to rule out Candida; Tzanck smear to rule out herpetic whitlow.",
 "Chronic paronychia": "<b>None</b> &mdash; clinical, on the immersion or chemical exposure history.",
 "Necrotizing fasciitis": "<b>Complete blood count with differential, chemistry, arterial blood gas, urinalysis, and blood and tissue cultures.</b> <span class=warn>They must NOT delay surgery.</span>",
 # ---- Lecture 5
 "Scabies": "<b>None</b> &mdash; microscopic identification of the organism, ova or faeces is the diagnosis.",
 "Crusted (hyperkeratotic) scabies": "<b>None</b> &mdash; as for scabies, but scrapings are strongly positive given the mite burden.",
 "Pediculosis capitis (head lice)": "<b>None</b> &mdash; visualising nits or live lice.",
 "Pediculosis corporis (body lice)": "<b>None</b> &mdash; examine clothing seams; shake clothing over white paper.",
 "Pediculosis pubis (crabs)": "<b>None for the infestation.</b> <span class=warn>Screen for concurrent sexually transmitted infection</span> &mdash; patients often have one.",
 "Bedbugs": "<b>None</b> &mdash; physical examination.",
 "Tungiasis (fleas)": "<b>None</b> &mdash; dermoscopy visualises the ovoid eggs.",
 "Caterpillars (lepidopterism)": "<b>None</b> &mdash; clinical, from the exposure and the pattern.",
 "Cutaneous larva migrans": "<b>None</b> &mdash; clinical if the serpiginous rash is present. Light microscopy with mineral oil shows larvae in the folliculitic form.",
 "Black widow spider": "<b>None diagnostic.</b> Clinical, from the exposure and the systemic picture.",
 "Brown recluse spider": "<b>None diagnostic.</b> Clinical, from the appearance and the exposure history.",
 "Hobo spider": "<b>None diagnostic.</b> Clinical, from geography, season and appearance.",
 "Lyme disease": "<b>Enzyme-linked immunosorbent assay for immunoglobulin M and G; the C6 peptide test (immunoglobulin G) is more specific; Western blot more specific still.</b> <span class=warn>If erythema migrans is present, diagnose and treat CLINICALLY &mdash; do not wait.</span>",
 "Rocky Mountain spotted fever": "<b>Complete blood count (thrombocytopenia, anaemia, normal white count with increased bands), chemistry (mild hyponatraemia), liver function (mild transaminitis).</b> Cerebrospinal fluid: leukocytosis, moderately raised protein, normal glucose. <b>Gold standard: indirect immunofluorescence assay</b> &mdash; rarely diagnostic before day 7, so <span class=warn>treat by day 5 while waiting.</span>",
 "Cercarial dermatitis (swimmer's itch)": "<b>None</b> &mdash; clinical, from the freshwater exposure and the time course.",
 # ---- Lecture 7
 "Clavus (corn) &mdash; hard": "<b>None.</b> Purely clinical. In a diabetic patient the relevant work-up is a foot risk assessment &mdash; sensation, pulses, glycaemic control &mdash; not blood tests for the lesion.",
 "Clavus (corn) &mdash; soft": "<b>None.</b> Clinical. Potassium hydroxide preparation only if an interdigital fungal infection is the real question.",
 "Callus": "<b>None</b> &mdash; clinical diagnosis.",
 "Keloid": "<b>None.</b> Clinical diagnosis. <b>Biopsy is actively discouraged unless there is real doubt, because it may induce new scarring.</b>",
 "Hypertrophic scar": "<b>None.</b> Clinical diagnosis, with the same biopsy caution as keloid.",
 "Cutaneous horn": "<b>No bloods, but tissue is essential.</b> <b>Deep shave biopsy</b> to sample the base &mdash; the only way to know whether the underlying lesion is benign or malignant.",
 "Acrochordon (skin tag)": "<b>None.</b> Clinical.",
 "Pressure injury (pressure ulcer)": "<b>No test diagnoses or stages it &mdash; staging is visual.</b> Bloods support management rather than diagnosis: <b>nutritional markers (albumin, prealbumin)</b> because nutrition assessment is part of prevention, and inflammatory markers plus culture <b>only if infection is suspected</b>. Deep or non-healing wounds over bone may warrant imaging for osteomyelitis.",
 "Pilonidal cyst": "<b>None usually needed.</b> Clinical diagnosis. Culture of drainage is not routine.",
 "Dermatofibroma": "<b>No bloods.</b> Dermoscopy supports it; shave or punch biopsy is both diagnostic and therapeutic in a small lesion.",
 "Keratoacanthoma": "<b>No bloods, but BIOPSY IS MANDATORY</b> &mdash; it is the only reliable method of diagnosis, because the lesion cannot be separated from squamous cell carcinoma clinically.",
 "Epidermoid (epidermal) cyst": "<b>Lab tests usually unnecessary.</b> Culture only if an inflamed cyst is thought to be secondarily infected.",
 "Syringoma": "<b>None.</b> Usually clinical; biopsy only if malignancy is a concern.",
 "Infantile hemangioma": "<b>None for a typical lesion</b> &mdash; most are diagnosed clinically. Referral to a vascular anomalies specialist replaces testing when the diagnosis is in question; imaging is that specialist's decision, not a screening test.",
 "Nevus flammeus (port-wine stain)": "<b>None</b> &mdash; clinical diagnosis.",
 "Nevus simplex (stork bite)": "<b>None</b> &mdash; clinical diagnosis.",
 "Cherry angioma": "<b>None</b> &mdash; clinical diagnosis.",
 "Telangiectasia": "<b>None for the lesion itself.</b> Because telangiectasias are associated with numerous diseases, any testing follows the <b>suspected underlying condition</b> rather than the skin finding.",
 "Nevus araneus (spider angioma)": "<b>The history is the test</b> &mdash; pregnancy, hormone use, alcohol, hepatotoxic drugs. Where liver disease is suspected on that history, <b>liver function tests</b> are the reasonable follow-on. The lesion itself needs none.",
 "Pyogenic granuloma": "<b>None.</b> Usually a clinical diagnosis &mdash; though surgical excision has the advantage of providing histopathologic analysis, which matters because melanoma and squamous cell carcinoma are in the differential.",
 "Neurofibromatosis type 1": "<b>No routine bloods.</b> Diagnosis is clinical on the recognised criteria. Genetic testing exists but is not what this lecture asks for; surveillance is by cutaneous examination at every visit.",
 "Xanthelasma": "<b>YES &mdash; SCREEN FOR HYPERLIPIDEMIA.</b> A fasting lipid panel. This is the one lesion in the lecture whose blood work is the whole point: it may signify increased risk of cardiac disease.",
 "Lipoma": "<b>None</b> &mdash; typically a clinical diagnosis.",
 "Digital mucous cyst": "<b>None.</b> Clinical. The association is with osteoarthritis of the distal interphalangeal joint.",
 "Sebaceous hyperplasia": "<b>No bloods.</b> <b>Dermoscopy</b> distinguishes it from basal cell carcinoma; biopsy only if that concern remains.",

 # ---- Lecture 8
 "Ephelides (freckles)": "<b>None</b> &mdash; clinical diagnosis.",
 "Lentigines": "<b>None</b> &mdash; clinical diagnosis.",
 "Solar lentigo": "<b>None</b> &mdash; dermoscopy, with biopsy only if atypical.",
 "Seborrheic keratosis": "<b>None</b> &mdash; clinical diagnosis.",
 "Dermatosis papulosa nigrans": "<b>None</b> &mdash; clinical, with biopsy only if uncertain.",
 "Vitiligo": "<b>Complete blood count and antinuclear antibody</b>, to correlate with the other autoimmune diseases associated with it.",
 "Congenital melanocytic naevus": "<b>No bloods.</b> Magnetic resonance imaging of brain, with or without total spine, if cranial or axial &mdash; for neurocutaneous melanosis.",
 "Naevus spilus": "<b>None</b> &mdash; clinical, with periodic evaluation.",
 "Common acquired melanocytic naevus (mole)": "<b>None</b> &mdash; clinical diagnosis.",
 "Blue naevus": "<b>None</b> &mdash; clinical for small lesions, biopsy for larger ones.",
 "Pigmented spindle cell naevus (Reed)": "<b>None</b> &mdash; biopsy confirms it.",
 "Spitz naevus": "<b>None</b> &mdash; biopsy or wide excision.",
 "Dysplastic melanocytic naevus": "<b>None</b> &mdash; diagnosis is by biopsy.",
}

ROWS += [
 # ================= LECTURE 7 =================
 ("SECTION", "Lecture 7 &middot; Benign Skin Lesions"),

 ("l7_s005_1.png", "Clavus (corn) &mdash; hard",
  "<b>Focal</b> mechanical trauma (ill-fitting shoes) &rarr; hyperkeratosis with a <b>cone-shaped central core of hard keratin pointing into the skin</b>. Well defined, <b>&lt;1.5&nbsp;cm</b>, <b>painful on direct downward pressure</b>. Skin lines <b>run through</b> it. Clavus durum favours the <b>dorsal and lateral fifth toe</b>.<br><span class=pt>&ldquo;It's like walking on a pebble &mdash; right on this one spot.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> No testing needed.<br><b>Differential: callus</b> (larger, irregular, painless, no core) and <b>verruca vulgaris</b> (interrupts skin lines, blackened centre, hurts on <em>side</em> pressure, not confined to pressure areas).",
  "<b>1st: remove the pressure</b> &mdash; padding, and stop wearing poorly fitting footwear.<br><b>2nd:</b> over-the-counter keratolytic products. Every one in the deck's table is <b>salicylic acid</b>, 12.6&ndash;40%, as a disk, liquid or plaster.<br><b>Diabetic patient &rarr; refer to podiatry.</b>",
  "Caused by shoes too tight or too loose, shoes without socks, going barefoot, and tools or sports equipment rubbing the skin. To heal and prevent: properly fitting shoes and socks, avoid high heels, avoid barefoot, use pads inside the shoe."),

 ("l7_s005_2.png", "Clavus (corn) &mdash; soft",
  "Same pressure mechanism, but sited in the <b>fourth-to-fifth toe web space</b>, where trapped moisture <b>macerates</b> it &mdash; hence clavus mollum, &ldquo;soft&rdquo;. Still has the central core.<br><span class=pt>&ldquo;There's a sore white patch between my little toes.&rdquo;</span>",
  "<b>Clinical diagnosis.</b><br>Distinguish from an interdigital fungal infection, which is scaly and itchy rather than cored and tender.",
  "<b>1st:</b> as for hard corn &mdash; padding and footwear change, plus <b>keeping the web space dry</b>.<br><b>2nd:</b> salicylic acid keratolytics.<br><b>Diabetic &rarr; podiatry.</b>",
  "Dry carefully between the toes after washing. Wear socks that wick moisture. The same footwear advice as for any corn."),

 ("l7_s006_1.png", "Callus",
  "<b>Broad-area</b> pressure and friction &rarr; <b>diffuse</b> hyperkeratosis with <b>no central core</b>. Larger than a corn, <b>irregular and poorly defined</b>, and <b>usually painless</b>. Typically the <b>palms</b> or the <b>balls of the feet</b>. If the process is acute and severe, a <b>blister</b> forms instead.<br><span class=pt>&ldquo;The skin on my hands has gone thick and yellow, but it doesn't hurt.&rdquo;</span>",
  "<b>Clinical diagnosis.</b><br>The three-way differential is corn (cored, tender, small), callus (diffuse, painless, large) and wart (skin lines interrupted, blackened centre).",
  "<b>1st:</b> padding and better-fitting footwear or gloves.<br><b>2nd:</b> over-the-counter salicylic acid keratolytics.<br><b>Diabetic &rarr; podiatry.</b>",
  "Same prevention as corns. A callus is protective as well as symptomatic &mdash; the aim is to reduce it, not to remove the protection entirely."),

 ("l7_s013_1.png", "Keloid",
  "A <b>fibroproliferative</b> disorder; pathophysiology remains unclear. Overgrowth of dense fibrous tissue that <b>extends beyond the margins of the original wound</b>, develops <b>slowly</b> and <b>keeps enlarging for months to years</b>, with <b>no regression</b> and a tendency to recur. Firm bulbous nodules or markedly elevated plaques. Predominantly <b>ear lobe, shoulders, sternal notch</b>; rarely across joints. <b>Rare</b> incidence but <b>associated with dark skin colour</b> &mdash; African American, Hispanic and Asian patients. Triggers: surgical incisions, traumatic wounds, vaccination sites, burns, chickenpox, acne, even minor scratches.<br><span class=pt>&ldquo;I got my ears pierced and this lump keeps growing &mdash; it's way bigger than the hole was.&rdquo;</span>",
  "<b>Clinical diagnosis.</b><br><b>Biopsy only if there is genuine clinical doubt, because it may induce new scarring.</b><br>Differential: hypertrophic scar, dermatofibroma, foreign-body granuloma.",
  "<b>Most important treatment is PREVENTION</b> &mdash; advise high-risk patients to avoid cosmetic procedures such as ear piercing. No single modality is best; <b>combination therapy has the best success rates</b>.<br><b>Occlusive silicone gel sheets</b> 12&ndash;24&nbsp;h/day for up to a year. <b>Compression</b> at 25&nbsp;mmHg, 24&nbsp;h/day, 6&ndash;12 months. <b>Intralesional steroid</b> (flattens; may cause tissue atrophy). <b>Surgical removal</b> &mdash; but <b>50&ndash;100% recurrence, often larger</b>, so always follow with intralesional steroid. <b>Radiation</b> in the first two weeks after excision. <b>Cryotherapy</b> (flattens; causes hypopigmentation). <b>Laser</b>, best combined with intralesional steroid. <b>Intralesional fluorouracil</b> &mdash; inhibits fibroblast proliferation.",
  "Post-surgery: <b>avoid stretching the immature scar</b>, avoid hot baths (they aggravate surgery-induced inflammation), keep the wound clean. <b>Avoid body piercings.</b> Adolescents with acne should seek early, appropriate acne treatment &mdash; it greatly increases the chance of scar-free healing."),

 ("l7_s021_1.jpg", "Hypertrophic scar",
  "The <b>active proliferative phase</b> of wound healing overshooting. Develops <b>rapidly, within four weeks</b> of the event, and stays <b>confined to the wound margins</b>. Remains stable and then <b>regresses (flattens) with time</b>. Asymptomatic. Occurs where scars <b>cross joints or skin creases at a right angle</b>. <b>Frequent</b> incidence, and <b>no association with skin colour</b>.<br><span class=pt>&ldquo;My scar went thick and red about a month after the operation, but it stops right at the edges.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> Biopsy only if there is clinical doubt, as it may induce new scarring.<br>Differential: keloid, dermatofibroma, foreign-body granuloma.",
  "<b>Intralesional injection</b> &mdash; corticosteroid or fluorouracil.<br><b>Compression therapy and silicone sheeting.</b><br><b>Surgical excision</b> &mdash; unlike keloid, hypertrophic scars <b>improve with appropriate surgery</b>.<br><b>Pulsed dye laser</b> &mdash; reduces erythema by reducing neovascularization.",
  "Reassure: this is the scar that gets better. It should flatten on its own over months. Distinguish it plainly from keloid, which does not."),

 ("l7_s025_1.png", "Cutaneous horn",
  "A hard <b>conical exophytic projection composed of keratin</b>, with the appearance of an animal horn. <b>It arises from the surface of another lesion &mdash; benign or malignant</b>: actinic keratosis, wart, seborrheic keratosis, keratoacanthoma, or basal or squamous cell carcinoma. <b>The process at the base of the lesion is what matters.</b> Caucasians <b>over 50</b>, males = females, on <b>head, neck and upper extremities</b>, commonly sun-exposed face, ears and hands. May bleed or hurt from trauma.<br><span class=pt>&ldquo;There's a hard little horn growing out of my ear.&rdquo;</span>",
  "<b>Often NO clinical feature distinguishes benign from malignant.</b><br><b>Gold standard: deep shave biopsy to sample the underlying tissue.</b><br>Differential: wart, actinic keratosis, squamous cell carcinoma.",
  "<b>Depends entirely on the underlying etiology.</b> An underlying malignancy frequently requires <b>excision to the standard practice for that tumour type and location</b>. Removing the horn alone treats nothing.",
  "Explain that the horn itself is only keratin, and the reason for biopsy is what lies beneath it. Counsel on sun protection and periodic skin examination."),

 ("l7_s029_1.png", "Acrochordon (skin tag)",
  "A <b>fibroepithelial pedunculated papilloma</b> &mdash; a <b>narrow stalk with a broad tip</b>. Soft, skin-coloured papules from about <b>1&nbsp;mm to 10&nbsp;mm</b>. Asymptomatic. Increased in <b>females and obese patients</b>, in <b>areas of friction</b> &mdash; neck, axilla, groin. Very common: present in <b>60% of people by age 70</b>.<br><span class=pt>&ldquo;I've got these little flaps of skin under my arms and they catch on my clothes.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> No testing needed.",
  "<b>Usually for cosmesis only.</b><br><b>Scissor excision, cryotherapy, or electrodesiccation.</b><br><b>Anesthesia is not necessary.</b>",
  "Harmless growths of normal skin. They form where skin rubs together &mdash; armpit, neck, under the breasts, groin &mdash; and become more likely with age and with excess weight. <b>Never cut or pull one off yourself: they bleed.</b> A new tag often forms in the same area after removal."),

 ("l7_s033_1.png", "Pressure injury (pressure ulcer)",
  "<b>Unrelieved pressure</b> damaging underlying tissue, generally soft tissue compressed <b>between a bony prominence and an external surface</b> for a prolonged time. Extent ranges from non-blanchable intact skin to deep ulcers reaching bone.<br><b>STAGING (from the slide's images):</b><br><b>1</b> &mdash; localised <b>non-blanchable erythema of intact skin</b>.<br><b>2</b> &mdash; <b>partial-thickness</b> loss with <b>exposed dermis</b>; bed viable, pink/red, moist, shiny or dry.<br><b>3</b> &mdash; <b>full thickness</b>; <b>adipose tissue visible</b>.<br><b>4</b> &mdash; full thickness skin AND tissue loss; <b>fascia, muscle, tendon, ligament, cartilage or bone exposed</b>.<br><b>Unstageable</b> &mdash; obscured by <b>slough or eschar</b>, extent cannot be determined.<br><b>Deep tissue</b> &mdash; persistent <b>non-blanchable deep red/purple discolouration</b>; skin intact or not.",
  "<b>Clinical diagnosis and staging.</b> The staging tables illustrate every stage in <b>both lightly and darkly pigmented skin</b> &mdash; non-blanchable erythema is harder to see and easier to miss on darker skin.",
  "<b>Best measure is PREVENTION:</b> frequent skin assessment, nutrition assessment, moisture control and skin care (keep clean and dry, manage incontinence, barrier creams), <b>reposition every two hours</b>, manage pain, improve mobility, specialty mattresses.<br><b>Management depends on stage.</b> <b>Refer to a wound care specialist.</b> Control infection risk. Silicone and hydrocolloid dressings. <b>Surgical referral for debridement</b> &mdash; removes necrotic tissue, eschar and slough, which promote infection, delay granulation and impede healing &mdash; and for wound closure.",
  "For carers: reposition two-hourly, keep skin clean and dry, manage incontinence promptly, and check the skin over every bony prominence at every opportunity. Report any non-blanching red area at once."),

 ("l7_s040_1.png", "Pilonidal cyst",
  "Disruption of the skin over the <b>coccyx</b> leaves a <b>dimple (pit)</b> that draws in hair and debris &rarr; <b>follicular plugging</b>; ingrown hairs prevent drainage and promote <b>abscess</b> formation. <b>Male to female 3:1.</b> Originally thought congenital, now believed <b>acquired</b>. <b>Recurrence is common.</b><br><b>Risk factors:</b> obesity, local trauma or irritation, sedentary lifestyle, <b>increased hair density in the natal cleft</b>, family history.<br><b>Acute abscess:</b> sudden pain and swelling in the gluteal cleft; warm, tender, erythematous, purulent or bloody drainage, may be <b>fluctuant</b>. <b>Chronic:</b> recurrent drainage and pain from one or more <b>sinus tracts</b>; a hair may be seen protruding from a sinus opening.<br><span class=pt>&ldquo;I get a painful swelling at the top of my bum crack, and sometimes it bursts and drains.&rdquo;</span>",
  "<b>No diagnostic testing usually needed.</b><br><b>Sinus vs fistula</b> (from the slide's diagram): a <b>sinus is a BLIND track</b>; a <b>fistula connects TWO epithelium-lined surfaces</b>. Both usually arise from a preceding abscess.",
  "<b>1st:</b> keep the area <b>clean and free of debris</b>; shaving or laser hair therapy may help.<br><b>Acute abscess &rarr; incision and drainage.</b><br><b>Chronic disease &rarr; refer to a surgeon for excision.</b>",
  "Maintain good hygiene of the natal cleft, and seek care if an abscess occurs. Recurrence is common, so hair control and hygiene are ongoing rather than one-off."),

 ("l7_s045_1.png", "Dermatofibroma",
  "<b>Fibroblasts in the dermis</b> forming small dense clusters &rarr; a firm <b>0.5&ndash;1&nbsp;cm nodule</b>. <b>Legs are the commonest site</b>, then arms. Male to female <b>1:2</b>, all races. Etiology uncertain &mdash; may follow <b>trauma, viral infection or insect bites</b>. Usually asymptomatic; if symptomatic, slight pruritus or pain &mdash; it is the <b>most common painful skin tumour</b>. Firm nodule with a <b>hyperpigmented brown halo</b>, pink hue, raised centre, scaly surface.<br><b>DIMPLE SIGN: the lesion retracts beneath the skin surface with lateral compression.</b><br><span class=pt>&ldquo;There's a hard little brown bump on my shin &mdash; I think it started after a bug bite.&rdquo;</span>",
  "<b>Clinical diagnosis, supported by dermoscopy</b> &mdash; often shows a <b>peripheral pigment network with a central white mass</b>.<br>Differential: basal cell carcinoma, hypertrophic scar, <b>cutaneous melanoma</b>, keratoacanthoma.",
  "<b>Often no treatment</b> unless the diagnosis is questioned or symptoms warrant it.<br><b>Small lesions: shave or punch biopsy &mdash; both diagnostic AND therapeutic.</b><br><b>Larger lesions:</b> may require surgical excision.",
  "Benign. The dimple sign is what distinguishes it from the pigmented lesions it can resemble. Return if it changes in size, colour or shape."),

 ("l7_s049_1.png", "Keratoacanthoma",
  "Believed to arise from the <b>pilosebaceous unit</b>. <b>Rapid, abundant growth then spontaneous resolution</b> &mdash; but it may keep growing or rarely metastasize. <b>Histopathologically similar to squamous cell carcinoma; strong arguments support classifying it as a VARIANT of invasive squamous cell carcinoma.</b> Classic in middle-aged, light-skinned people in hair-bearing sun-exposed areas. Males &gt; females.<br><b>Risk factors:</b> age &gt;40, sun exposure, very fair skin that always burns and never tans, male sex, <b>tattoos (red ink)</b>, <b>skin trauma such as lasers, surgery or cryotherapy</b>, human papillomavirus infection.<br><b>Triphasic:</b> rapid growth in <b>6&ndash;8 weeks</b>, stabilization, regression after <b>3&ndash;6 months</b>.<br>Solitary, smooth, shiny, <b>dome-shaped red papule or nodule with a central keratin-filled crater &mdash; resembles a volcano</b>.<br><span class=pt>&ldquo;This came up out of nowhere in about six weeks and it's got a crusty plug in the middle.&rdquo;</span>",
  "<b>Biopsy is the ONLY reliable method to make the diagnosis.</b><br>Differential: <b>squamous cell carcinoma</b>, basal cell carcinoma, amelanotic melanoma, molluscum contagiosum.",
  "<b>Surgical &mdash; standard of care is to excise or destroy the tumour, preferred because of possible malignancy.</b><br><b>Elliptical excision with 5&nbsp;mm margins.</b><br><b>Mohs surgery</b> for large or recurrent lesions, or lesions in areas with cosmetic or functional considerations.<br><b>Intralesional methotrexate</b> may be given before excision to reduce the size &mdash; it inhibits deoxyribonucleic acid synthesis in actively dividing cells.",
  "Do not wait for it to regress. Even though many do, it cannot be told from a squamous cell carcinoma without histology, so it is treated as one. Counsel on sun protection."),

 ("l7_s053_1.png", "Epidermoid (epidermal) cyst",
  "<b>Cystic enclosure of epithelium within the dermis</b>, filling with <b>KERATIN</b>. Often called a &ldquo;sebaceous cyst&rdquo; because the contents look like sebum &mdash; <b>it is not one</b>. Males &gt; females <b>2:1</b>; very common, on <b>face, scalp, neck and trunk</b>. Usually asymptomatic; may drain foul-smelling material. Single firm papule or nodule, <b>movable, round, protruding</b>, with a <b>central pore or punctum communicating with the skin surface</b>. Expresses <b>cream-coloured pasty material with the odour of rancid cheese</b>.<br><span class=pt>&ldquo;There's a lump on my back with a little hole in the middle, and if I squeeze it something white and awful comes out.&rdquo;</span>",
  "<b>Clinical diagnosis. Lab tests usually unnecessary.</b><br>Differential: cystic acne, lipoma, neurofibroma, keratoacanthoma, basal cell carcinoma.",
  "<b>Asymptomatic: no treatment necessary.</b><br><b>If inflamed: POSTPONE excision for a few weeks</b>, reduce inflammation with <b>intralesional triamcinolone</b>, add antibiotics if needed.<br><b>Standard of care is surgical removal of the ENTIRE capsule, performed when the cyst is not inflamed.</b> A small cyst (1&ndash;3&nbsp;cm) can be treated with a punch incision and removal of the cystic contents.",
  "The lump is keratin, not oil, and it is benign. Squeezing it risks rupture and inflammation. If it becomes red and painful, come in &mdash; that is the point at which surgery is delayed rather than brought forward."),

 ("l7_s058_1.png", "Syringoma",
  "<b>Benign neoplasms of ECCRINE ducts</b> (sweat glands). Appear at <b>puberty</b>; females &gt; males. Usually asymptomatic. <b>Multiple 1&ndash;2&nbsp;mm skin-coloured, pink or brown papules</b>, most frequently on the <b>eyelids (periorbital region) and upper cheeks</b>.<br><span class=pt>&ldquo;I've got these tiny bumps under my eyes &mdash; they came up in my teens.&rdquo;</span>",
  "<b>Usually clinical; biopsy if there is concern about malignancy.</b><br>Differential: <b>milia</b>, <b>xanthelasma</b>, basal cell carcinoma.",
  "<b>For cosmesis only, and every option has a trade-off.</b><br><b>Drugs</b> (e.g. oral isotretinoin) &mdash; <b>increased risk of recurrence</b>.<br><b>Removal procedures</b> (curettage and electrodesiccation, laser therapy, cryotherapy, surgical excision) &mdash; <b>possible poor cosmetic results</b>.",
  "Benign and harmless. Any treatment is elective, and the periorbital skin makes cosmetic outcome the main consideration. Recurrence is common with medical treatment."),

 ("l7_s067_1.png", "Infantile hemangioma",
  "<b>Congenital vascular lesion; the most common tumour of infancy</b>, and most are medically insignificant. A <b>benign neoplasm</b> from <b>rapid proliferation of endothelial cells</b>, from mutations in the genes regulating it. Usually noticed in the first days to weeks; usually single; typical maximum size <b>0.5&ndash;5&nbsp;cm</b>. More common in <b>preterm infants, females 3:1, Caucasians</b>. <b>Head and neck 60%</b>, trunk 25%, extremities 15%.<br><b>Earliest sign: blanching of the involved skin, then fine telangiectasias, then a red/crimson macule.</b> 50% present at birth.<br><b>Growth:</b> rapid birth&ndash;4 weeks, most growth in the first <b>4&ndash;6 months</b>, slowing 6&ndash;12 months. <b>Involution: 50% by age 5, 70% by 7, 90% by 9.</b><br><b>Superficial</b> (most common) &mdash; dilated vessels in dermis, bright red papule/plaque/nodule, once called &ldquo;strawberry&rdquo;. <b>Deep</b> (least common) &mdash; deep dermis and subcutis, pale/skin-coloured/red/blue nodule.",
  "<b>Most are diagnosed clinically.</b> If the diagnosis is in question, <b>refer to an appropriate and experienced vascular anomalies specialist</b>.<br>Differential: <b>nevus flammeus</b> (present at birth, present for life) and <b>pyogenic granuloma</b> (due to minor trauma).",
  "<b>No treatment may be needed &mdash; serial observation</b>, since most involute.<br><b>Indications to treat: cosmetic, functional involvement, deep ulceration, infection.</b><br><b>First line: BETA-BLOCKERS</b> &mdash; oral propranolol or topical timolol (mechanism not well understood).<br><b>Also first line: corticosteroids</b> &mdash; topical, intralesional or oral; slow growth and decrease size.<br><b>Pulsed dye laser</b> for superficial lesions (depth ~1.2&nbsp;mm). <b>Surgical excision.</b>",
  "Most disappear on their own over years, and the natural history is the reassurance. Watch for anything that blocks vision, interferes with feeding or breathing, obstructs the ear canal, ulcerates or bleeds &mdash; those are the reasons to treat rather than wait."),

 ("l7_s078_1.png", "Nevus flammeus (port-wine stain)",
  "<b>Congenital vascular lesion.</b> <b>Dilated superficial dermal capillaries through the entire depth of the dermis, with NO proliferation of endothelial cells</b> &mdash; which is why it never involutes. More common in Caucasians, male = female. <b>Present at birth, grows in proportion with the child, NO involution, becomes darker and thicker.</b> Painless expanding lesion.<br><b>Early:</b> flat (macular) well-circumscribed <b>blanchable</b> patches, pink to red to purple; <b>colour darkens with crying, fever or overheating</b>; usually <b>unilateral with fairly sharp midline cutoffs</b>. <b>Later:</b> vasculature dilates and it may evolve into a raised, thickened plaque of deep red to purple.<br>Psychosocial disability from facial disfigurement can be overwhelming.<br><span class=pt>&ldquo;He's had this red mark on one side of his face since the day he was born, and it's got darker as he's grown.&rdquo;</span>",
  "<b>Clinical diagnosis.</b><br>The critical contrast is with <b>infantile hemangioma</b>: hemangioma proliferates then involutes; nevus flammeus does neither.",
  "<b>No treatment</b> is required.<br><b>Cosmetics</b> &mdash; tinted waterproof makeup.<br><b>Pulsed dye laser therapy</b> &mdash; causes selective destruction of superficial target blood vessels, inducing intravascular coagulation; the vessel is later absorbed and replaced by collagen.",
  "This is permanent and will darken and thicken with time, unlike a hemangioma. Discuss the psychosocial impact openly. Camouflage cosmetics and laser are both legitimate options and neither is compulsory."),

 ("l7_s083_2.png", "Nevus simplex (stork bite)",
  "<b>Congenital vascular lesion</b>, a <b>more superficial variant of nevus flammeus</b> involving dermal capillaries. Present at birth; <b>becomes more noticeable when the baby cries</b>. Most common on the <b>head and neck</b>. Pink to erythematous, irregular, <b>blanchable</b> macules and/or patches, single or multiple.<br><span class=pt>&ldquo;There's a pink patch on the back of her neck that goes bright red when she cries.&rdquo;</span>",
  "<b>Clinical diagnosis.</b><br>Distinguish from nevus flammeus, which is usually unilateral with a sharp midline cutoff and does <em>not</em> fade.",
  "<b>No treatment.</b> <b>Fades within one year</b>, or may persist for life on the neck.",
  "Reassure: this is the common birthmark that usually goes away in the first year. The one on the nape may stay, which is why it is nicknamed a stork bite."),

 ("l7_s086_1.jpg", "Cherry angioma",
  "<b>Acquired vascular lesion</b>, formed by <b>capillary (venule) proliferation</b>. Very common, and <b>increases with age</b> &mdash; previously known as senile angioma. <b>Cause unknown.</b> Most common on the <b>trunk</b>; may bleed after trauma. <b>&lt;5&nbsp;mm</b>, smooth, firm, deep red papules that <b>blanch with pressure</b> (a fibrotic one may not blanch completely).<br><span class=pt>&ldquo;I keep getting these little bright red spots on my chest and back as I get older.&rdquo;</span>",
  "<b>Clinical diagnosis.</b><br>Differential includes petechiae (do not blanch, not papular) and pyogenic granuloma (moist, exophytic, grows fast).",
  "<b>Not necessary unless it bothers the patient.</b><br><b>Laser therapy</b> for superficial lesions.<br><b>Shave excision and electrocauterization</b> for large lesions.",
  "Benign, and strongly age-related. <b>New lesions will likely develop and there is no way to prevent them</b> &mdash; removing existing ones does not stop new ones forming."),

 ("l7_s088_1.png", "Telangiectasia",
  "<b>Acquired vascular lesion.</b> A <b>permanently dilated capillary, &lt;1&nbsp;mm</b>. <b>Blanchable.</b> Occurs singly, in groups, or with a <b>central punctum</b>. May be <b>primary or secondary</b>, and is <b>associated with numerous diseases</b>.<br><span class=pt>&ldquo;I've got tiny red lines on my cheeks that don't go away.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> Because telangiectasias are secondary to many conditions, the work-up follows the suspected cause rather than the lesion.",
  "Treat the <b>underlying cause</b> where there is one. Cosmetic treatment where wanted follows the same options as other superficial vascular lesions &mdash; laser being the mainstay.",
  "Explain that these are dilated existing vessels, not new growths. Their significance is as a possible sign of something else, which is why the history matters more than the lesion."),

 ("l7_s089_2.png", "Nevus araneus (spider angioma)",
  "<b>Acquired vascular lesion.</b> <b>NO vascular proliferation &mdash; dilation of preexisting vessels.</b> <b>Estrogen excess states may be the cause:</b> pregnancy or oral contraceptive use (<b>resolve after delivery or after stopping the pill</b>), and <b>cirrhosis or liver failure</b>. Location: <b>hands and fingers in children</b>; <b>face, neck, upper trunk and arms in adults</b>. Asymptomatic. Central arteriole with radiating capillaries; <b>lesion blanches</b>; <b>&lt;10&nbsp;mm</b>.<br><span class=pt>&ldquo;There's a little red spot with legs coming off it, like a spider.&rdquo;</span>",
  "<b>Clinical diagnosis &mdash; but the HISTORY is the test.</b> Ask about <b>pregnancies, hormone use, alcohol history, and medications carrying a risk of liver damage</b>.",
  "<b>No treatment may be needed</b> &mdash; pregnancy- and pill-related lesions resolve on their own.<br><b>Pulsed dye laser resolves most lesions.</b>",
  "The lesion itself is harmless; its value is as a clue. Several spider angiomas in a non-pregnant adult warrant a conversation about alcohol and liver health."),

 ("l7_s092_1.png", "Pyogenic granuloma",
  "<b>Acquired vascular lesion &mdash; MISNAMED: neither infectious nor granulomatous.</b> Exact cause unknown; a response to <b>injury or hormonal factors</b>. Common in <b>children, young adults and pregnancy</b>. A benign vascular tumour of skin and mucous membrane appearing as a <b>rapidly growing vascular papule or nodule</b>, from overgrowth of blood vessels in response to <b>irritation, trauma or hormonal change</b>. Most common on <b>head, neck and fingers</b>. <b>Bright red exophytic papule or nodule with a MOIST surface and an EPITHELIAL COLLARETTE at the base.</b> Bleeding, erosion, ulceration, purulence and crusting all possible. Average <b>6.5&nbsp;mm</b>; may reach several centimetres.<br><span class=pt>&ldquo;It came up really fast after I cut my finger, and it bleeds every time I knock it.&rdquo;</span>",
  "<b>Usually a clinical diagnosis.</b><br>Differential: cherry angioma, <b>malignant melanoma</b>, <b>squamous cell carcinoma</b> &mdash; two malignancies, which is why many are excised.",
  "<b>Spontaneous resolution may occur</b>, but patients often opt for treatment for cosmesis or because of bleeding.<br><b>Surgical excision</b> &mdash; provides histopathologic analysis, <b>lowest recurrence rate</b>, <b>highest rate of scarring</b>.<br><b>Other modalities:</b> shave excision followed by curettage and electrodesiccation, laser, cryotherapy.",
  "These lesions are benign and often resolve spontaneously over months to years. Effective treatments exist if wanted for appearance or to stop bleeding. <b>If it recurs, come back early &mdash; small lesions are easier to treat than large ones.</b>"),

 ("l7_s100_1.jpg", "Neurofibromatosis type 1",
  "Also <b>von Recklinghausen disease</b>. A common <b>neurocutaneous genetic disorder</b> causing tumours to form on nerve tissue. <b>NF1: NF1 gene, chromosome 17. NF2: NF2 gene, chromosome 22. Schwannomatosis (NF3): SMARCB1 and LZTR1, chromosome 22.</b><br><b>NF1 skin manifestations, all four:</b><br><b>Caf&eacute; au lait spots</b> &mdash; light tan to brown macules, <b>&gt;5&nbsp;mm prepubertal, &gt;15&nbsp;mm postpubertal</b>; often the first manifestation; usually present at birth or in the first year; grow in proportion with the child. <b>Six or more are diagnostic &mdash; but the macules alone do not establish the diagnosis.</b><br><b>Cutaneous neurofibromas</b> &mdash; benign nerve sheath tumours from peripheral nerves; well-circumscribed, sessile or pedunculated; protrude just above the skin or lie just under it with a violaceous hue; <b>begin at puberty and increase in number and size with age</b>; a few to hundreds.<br><b>Plexiform neurofibromas</b> &mdash; tumour in the tissue covering nerves; anywhere except brain and spinal cord; large and extensive; may be locally invasive.<br><b>Intertriginous freckling (Crowe's sign)</b> &mdash; freckles <b>&lt;5&nbsp;mm</b>, smaller than caf&eacute; au lait spots, grouped, more prominent with sun exposure; <b>axillary and inguinal</b> (may be seen under the breasts, but that site is not a diagnostic criterion).",
  "<b>Clinical diagnosis</b> on the recognised criteria. Six or more caf&eacute; au lait macules of the size threshold, plus the other features.",
  "<b>Surveillance.</b> A <b>cutaneous examination at every visit</b>, assessing for new neurofibromas or progression of existing lesions.<br><b>Plexiform neurofibromas</b> may be locally invasive; clinical evaluation should be directed at determining the extent of involvement.",
  "Point patients to <b>national and regional support groups</b> &mdash; for continuous updates on treatment advances and for emotional support. This is the education point the lecture names."),

 ("l7_s104_1.jpg", "Xanthelasma",
  "<b>Soft, yellow cholesterol plaques</b> &mdash; a collection of <b>lipid-laden macrophages</b>. <b>Associated with lipid disorders.</b> Asymptomatic. Most common location: the <b>medial eyelids</b>.<br><span class=pt>&ldquo;I've got soft yellow patches on my eyelids near my nose.&rdquo;</span>",
  "<b>Clinical diagnosis.</b><br><b>SCREEN FOR HYPERLIPIDEMIA</b> &mdash; it may signify an increased risk of cardiac disease.<br>Differential includes syringoma and milia, which share the periorbital site.",
  "<b>Laser or surgical excision.</b><br><b>Recurrence is common.</b><br>Treating the lipid disorder is the part that matters medically; removing the plaque is cosmetic.",
  "The plaque itself is harmless, but it can be a marker of a lipid disorder and of cardiac risk &mdash; which is why a cholesterol check is part of the visit. Recurrence after removal is common."),

 ("l7_s105_1.png", "Lipoma",
  "<b>The most common soft tissue tumour.</b> A benign <b>localised overgrowth of fat cells in the subcutaneous tissue</b>; single or multiple. Asymptomatic unless adjoining structures are invaded; can occur anywhere on the body. <b>Soft, painless subcutaneous nodules of rubbery consistency, usually &lt;5&nbsp;cm.</b><br><span class=pt>&ldquo;There's a soft squishy lump under my skin &mdash; it moves when I push it and doesn't hurt.&rdquo;</span>",
  "<b>Typically a clinical diagnosis.</b><br>Differential: epidermal cyst, dermatofibroma, abscess.",
  "<b>Asymptomatic tumours can be observed.</b><br><b>Cosmetically deforming enlarged masses, and uncertain diagnosis, can be treated surgically with excision.</b>",
  "Benign and very common. Excision is for appearance, for symptoms from pressure on nearby structures, or to settle a diagnosis &mdash; not because the lump is dangerous."),

 ("l7_s108_1.png", "Digital mucous cyst",
  "A <b>PSEUDO-cyst &mdash; it does not have a cellular lining (a true capsule)</b>. Represents an <b>extrusion of mucinous contents from a local joint space into the surrounding dermis</b>; as the mucin collects it compacts the cells at the margin, <b>mimicking</b> a capsule. Females &gt; males. Asymptomatic unless large. <b>Associated with osteoarthritis.</b> Typically located over the <b>distal interphalangeal (DIP) joint</b> &mdash; a translucent skin-coloured cyst papule on the distal digit, over the proximal nail matrix or the nail bed. <b>May cause a longitudinal groove in the nail</b> from pressure on the matrix.<br><span class=pt>&ldquo;There's a clear little blister by my fingernail and the nail has a line down it now.&rdquo;</span>",
  "<b>Clinical diagnosis.</b> The association with osteoarthritis of the distal interphalangeal joint is part of the picture.",
  "<b>Asymptomatic lesions may be observed.</b><br><b>Symptomatic cysts, or those causing nail dystrophy, can be excised.</b>",
  "The nail groove is caused by the cyst pressing on the nail matrix and usually resolves once the cyst is dealt with. Otherwise no treatment is needed."),

 ("l7_s110_2.png", "Sebaceous hyperplasia",
  "A common benign condition of the <b>sebaceous glands</b>, with <b>NO known potential for malignant transformation</b>. With age, <b>turnover of sebocytes slows</b>, crowding them and <b>enlarging the gland</b>. <b>Immunosuppression is high risk.</b> Asymptomatic; the patient usually presents about appearance or about cancer. Single or multiple <b>whitish-yellow or skin-coloured papules, soft, 2&ndash;9&nbsp;mm</b>, with <b>CENTRAL UMBILICATION</b> &mdash; a very small globule of sebum can sometimes be expressed. Common on the <b>face</b>.<br><span class=pt>&ldquo;I've got small yellowish bumps on my forehead with a dip in the middle &mdash; is it skin cancer?&rdquo;</span>",
  "<b>Dermoscopy can distinguish between basal cell carcinoma and sebaceous hyperplasia.</b><br><b>Biopsy if concern about malignancy (basal cell carcinoma) remains.</b><br>Differential: <b>basal cell skin cancer</b> &mdash; and that is exactly what the patient is worried about.",
  "<b>Does not require treatment.</b> Lesions <b>tend to recur</b> and treatment carries a <b>risk of scarring</b>.<br><b>Light electrocautery</b> can be used if treatment is wanted.",
  "Benign, with no potential to become cancerous. The main reason to see a clinician is to have it distinguished from a basal cell carcinoma, which dermoscopy can usually do without a biopsy."),
]

SECTION_LABELS = {

 "Lecture 2 &middot; General Dermatology I &mdash; eczema and dermatitis": "L2 eczema",
 "Lecture 2 &middot; Vesiculobullous, papulosquamous, alopecia and xerosis": "L2 bullous + papulosquamous",
 "Lecture 3 &middot; Dermatology II &mdash; reactive and immune-mediated": "L3 reactive",
 "Lecture 3 &middot; Severe drug reactions and photodermatology": "L3 drug + photo",
 "Lecture 4 &middot; Cutaneous Bacterial Infections": "L4 bacterial",
 "Lecture 5 &middot; Dermatological Infestations": "L5 infestations",
 "Lecture 6 &middot; Cutaneous Fungal Infections": "L6 fungal",
 "Lecture 6 &middot; Cutaneous Viral Infections": "L6 viral",
 "Lecture 7 &middot; Benign Skin Lesions": "L7 benign",
 "Lecture 8 &middot; Pigmented Skin Lesions": "L8 pigmented",
 "Lecture 9 &middot; Pre-Malignant and Malignant Cutaneous Lesions": "L9 malignant",
}


# Slides whose title marks them as non-content -- section dividers, the closing
# "Questions?" slide, references, case studies. An image was taken from Lecture
# 8 slide 47 ("Questions?") and shipped as congenital melanocytic naevus; it was
# a photograph of a dog. This makes that class of error fail the build.
# Slides whose image is a VISUAL METAPHOR rather than a clinical photograph.
# The non-content guard cannot catch these -- their slide titles are ordinary
# ("Clavi or Clavus (Corns)", "Keratoacanthoma: Clinical Presentation",
# "Sebaceous Hyperplasia: Clinical Presentation") and only the picture gives it
# away. Lecture 7 alone contains a photograph of corn on the cob, a photograph
# of an erupting volcano, and a photograph of a doughnut. Any of the three would
# have shipped looking exactly as authoritative as the dog did.
METAPHOR_IMAGES = {
    "l7_s004_1", "l7_s004_2",   # corn on the cob, for "corns"
    "l7_s050_1",                # a volcano, for the keratin-filled crater
    "l7_s110_1",                # a doughnut, for the central umbilication

    # Lecture 6 (Jaquith) audited 2026-08-20. This deck is not metaphorical but
    # it is full of pictures that are not of a patient, and every one of them
    # sits on a slide with a perfectly ordinary clinical title. Four distinct
    # classes turned up; all would have shipped looking as authoritative as the
    # Lecture 8 dog did.
    #
    # 1. PRODUCT PACKAGING -- a photograph of the box, not the disease.
    "l6_s005_1", "l6_s005_2", "l6_s005_3", "l6_s005_4",   # terbinafine, clotrimazole, ketoconazole
    "l6_s044_1", "l6_s057_1",                             # a tub of CeraVe
    "l6_s045_1",                                          # Zeasorb AF powder
    "l6_s148_2",                                          # Compound W wart remover
    # 2. THE SOURCE, NOT THE LESION -- the tinea capitis transmission slide is
    #    four photographs of household PETS, and the tinea pedis epidemiology
    #    slide is a photograph of an empty communal shower room.
    "l6_s010_1", "l6_s010_2", "l6_s010_3", "l6_s010_4",
    "l6_s035_1",
    # 3. STOCK ART AND DIAGRAMS -- a stock photograph of a woman holding her
    #    head (for the zoster prodrome), a cartoon of a cryotherapy gun, and a
    #    line drawing of pseudohyphae. None is a clinical photograph.
    "l6_s097_1", "l6_s148_1", "l6_s067_1",
    # 4. BROKEN OR SELF-ANSWERING -- s064_2 extracts as a solid black rectangle;
    #    s055_3 has "TINEA MANUUM" burned into the picture, which hands the
    #    student the answer before they have looked at it.
    "l6_s064_2", "l6_s055_3",

    # Lecture 9 (Jaquith) audited 2026-08-24. Same four classes again, plus a
    # new one: this deck leans on SCHEMATIC DIAGRAMS and DATA TABLES to teach
    # staging, and those are content -- pool F asks about them -- but they are
    # not what a lesion looks like.
    "l9_s005_1",                        # skin-cancer cross-section schematic
    "l9_s025_1", "l9_s025_2",           # Mohs surgery diagrams
    "l9_s050_1", "l9_s053_1",           # Clark level and Stages of Melanoma diagrams
    "l9_s054_1", "l9_s055_1",           # TNM staging table; survival bar chart
    "l9_s047_1", "l9_s048_1",           # captioned ABCDE and early-detection figures
    "l9_s058_1",                        # line drawing of legs
    "l9_s035_5", "l9_s046_6", "l9_s074_1",   # stray icons, not photographs
    # BAKED-IN ANSWER TEXT -- the label hands the student the diagnosis.
    "l9_s020_1",                        # "SCC on the leg" burned into the image
    "l9_s031_1",                        # side-by-side captioned BASAL / SQUAMOUS
    "l9_s091_1",                        # nail figure with its findings labelled
}

# Images that ARE clinical photographs but are photographs of a DIFFERENT
# disease -- they sit on differential-diagnosis slides, or on a slide whose
# whole point is that the thing shown is NOT the condition being taught. Filing
# one of these under the lecture's own condition would be a factual error in the
# chart, not merely an ugly picture.
WRONG_DISEASE_IMAGES = {
    "l6_s027_1", "l6_s027_2", "l6_s027_3",   # "Clinical Pearl": nummular eczema, the tinea corporis mimic
    "l6_s042_1", "l6_s042_2", "l6_s042_3",   # tinea pedis differential: candidiasis, contact dermatitis, psoriasis
    "l6_s050_1", "l6_s050_2",                # slide title is literally "Dystrophic nails: NOT Onychomycosis"
    "l6_s121_1", "l6_s121_2",                # herpes simplex differential: chancroid and syphilis
}

# Micrographs. Legitimate teaching images, and the potassium hydroxide ones
# answer Objective a directly -- but they are not what the DISEASE looks like,
# so they must never fill a "what this looks like" cell.
MICROGRAPH_IMAGES = {
    "l6_s043_1", "l6_s071_1", "l6_s080_1",
}

NON_CONTENT = re.compile(r"^\s*(questions\??|resources?|case stud(y|ies)|references?|"
                         r"thank you|acknowledg\w*)\s*$", re.I)


def non_content_slides():
    import os as _os
    SCRATCH = "/private/tmp/claude-501/-Users-jaxonluke/8623a091-045a-42b8-8052-ca7d2eb04188/scratchpad"
    files = {"l2": "cms_l2.txt", "l3": "cms_l3.txt", "l4": "cms_l4.txt",
             "l5": "cms_l5.txt", "l6": "cms_l6.txt",
             "l7": "cms_l7.txt", "l8": "cms_l8.txt", "l9": "cms_l9.txt"}
    out = {}
    for tag, fn in files.items():
        path = _os.path.join(SCRATCH, fn)
        if not _os.path.exists(path):
            continue                      # extraction not present; skip the guard
        txt = open(path, encoding="utf-8").read()
        parts = re.split(r"=== SLIDE (\d+) ===", txt)
        bad = set()
        for i in range(1, len(parts), 2):
            head = parts[i + 1].strip().split("\n")[0] if parts[i + 1].strip() else ""
            if NON_CONTENT.match(head):
                bad.add(int(parts[i]))
        out[tag] = bad
    return out


# Vertical bands removed from an extracted image, as (start, end) fractions of
# its height. The rest of the image is rejoined, so the source citation printed
# at the foot of a textbook figure is KEPT -- that strip is the attribution and
# must survive any crop.
#
# l5_s027_4 (pubic lice) is the only entry. The slide is a male lower abdomen
# and every diagnostic feature -- the scattered bite macules and the coarse
# terminal hair the louse lives in -- sits above the band that is dropped. This
# repo is a public website, so the genitalia below it is exposure with no
# teaching value attached. Removing it costs the image nothing.
DROP_BAND = {
    "l5_s027_4.jpg": (0.75, 0.885),
}


def apply_crop(im, stem):
    band = DROP_BAND.get(stem)
    if not band:
        return im
    a, b = (int(im.height * f) for f in band)
    assert 0 < a < b < im.height, "crop band outside the image"
    keep = Image.new(im.mode, (im.width, im.height - (b - a)))
    keep.paste(im.crop((0, 0, im.width, a)), (0, 0))
    keep.paste(im.crop((0, b, im.width, im.height)), (0, a))
    return keep


def prep_images():
    os.makedirs(OUT_DIR, exist_ok=True)
    mapping, missing = {}, []
    for row in ROWS:
        if row[0] == "SECTION":
            continue
        src = row[0]
        if not src:
            continue
        # rows name images by stem; the extractor kept each blob's native
        # extension, so resolve it rather than assuming .jpg
        stem_in = src.rsplit(".", 1)[0]
        cand = [f for f in os.listdir(SRC) if f.rsplit(".", 1)[0] == stem_in
                and not f.lower().endswith((".wmf", ".emf"))]   # vector metafiles will not load
        if not cand:
            missing.append(src)
            continue
        p = os.path.join(SRC, cand[0])
        stem = src.rsplit(".", 1)[0] + ".jpg"
        out = os.path.join(OUT_DIR, stem)
        im = Image.open(p)
        if im.mode in ("RGBA", "P", "LA"):
            im = im.convert("RGB")
        im = apply_crop(im, stem)
        if im.width > MAXW:
            im = im.resize((MAXW, round(im.height * MAXW / im.width)), Image.LANCZOS)
        im.save(out, "JPEG", quality=82, optimize=True)
        mapping[src] = stem
    assert not missing, "images not found: %r" % missing
    unused = set(DROP_BAND) - set(mapping.values())
    assert not unused, "DROP_BAND names an image no row uses: %r" % unused
    return mapping


def slide_of(src):
    tag, s, _ = src.split("_", 2)
    return tag, int(s[1:])


# ---- the giveaways must DISCRIMINATE -------------------------------------
# A phrase shared by two conditions is not a giveaway. The first version of the
# column had three bold fragments doing double duty -- "well-demarcated" across
# allergic contact dermatitis and plaque psoriasis, "Nikolsky positive" across
# pemphigus and toxic epidermal necrolysis, "poorly demarcated" across atopic
# dermatitis and cellulitis. Each is now either led by something unique, or says
# outright that the feature is shared and names what separates the two.
#
# The ONLY permitted collision is one condition appearing in two lecture
# sections, which the chart does deliberately for solar lentigo.
def _gv_lead(html):
    m = re.search(r"<b>(.*?)</b>", html)
    if not m:
        return ""
    t = re.sub(r"<[^>]+>", "", m.group(1))
    t = re.sub(r"&[a-z]+;", " ", t)
    return re.sub(r"\s+", " ", t).strip(" .,;()").lower()


_leads = {}
for _n, _g in GIVEAWAY.items():
    _leads.setdefault(_gv_lead(_g), []).append(_n)
_clash = {k: v for k, v in _leads.items()
          if k and len(v) > 1
          and len({re.sub(r"\s*also Lecture \d+\s*", "", x).strip() for x in v}) > 1}
assert not _clash, ("two DIFFERENT conditions lead with the same giveaway, so it gives "
                    "nothing away: %r" % _clash)


def render(mapping):
    body, n_rows, n_imgs = [], 0, 0
    for row in ROWS:
        if row[0] == "SECTION":
            label = SECTION_LABELS[row[1]]
            body.append('<tr class="sec" data-label="%s"><td colspan="7">%s</td></tr>'
                        % (H.escape(label), row[1]))
            continue
        src, name, manif, tests, tx, edu = row
        # strip the "also Lecture N" badge as well as the tags around it, so
        # the two solar lentigo rows share one labs entry
        key = re.sub(r"<span class=\"dup\">.*?</span>", "", name)
        key = re.sub(r"<[^>]+>", "", key).strip()
        assert key in LABS, "no labs entry for %r" % key
        tests = tests + ('<div class="labs"><span class="labs-h">Labs to order</span>%s</div>'
                         % LABS[key])
        if src:
            tag, sl = slide_of(src)
            cite = "%s &middot; Slide %d" % (LECTURE[tag], sl)
            deck = H.escape(DECK[tag])
            # NOT loading="lazy". A lazy image that never entered the viewport
            # is absent from the print output -- a test export carried 10 of 84
            # photographs. This page exists to be downloaded, so the images load
            # eagerly and `decoding="async"` keeps scrolling smooth instead.
            pic = ('<figure><img src="cms-derm-chart-images/%s" alt="%s, from the lecture slides" '
                   'decoding="async"><figcaption>%s<span class="deck">%s</span></figcaption></figure>'
                   % (mapping[src], H.escape(name.replace("&mdash;", "-")), cite, deck))
            n_imgs += 1
        else:
            pic = '<div class="nopic">No suitable slide image in the deck</div>'
        # A condition with no giveaway fails the build rather than shipping a
        # blank cell: the column is only useful if it is complete.
        # Look up on the PLAIN name: several rows carry markup in the name cell
        # (the "also Lecture 8" duplicate tag), and Actinic keratosis appears in
        # both Lecture 3 and Lecture 9, sharing one giveaway on purpose.
        _plain = _re_tags.sub("", name).strip()
        gv = GIVEAWAY.get(_plain)
        assert gv, ("no vignette giveaway for %r -- add one to "
                    "tools/add_chart_giveaways.py rather than leaving the cell empty" % _plain)
        body.append(
            '<tr>'
            '<td class="pic">%s</td>'
            '<td class="name">%s</td>'
            '<td class="gv">%s</td>'
            '<td>%s</td>'
            '<td>%s</td>'
            '<td>%s</td>'
            '<td>%s</td>'
            '</tr>' % (pic, name, gv, manif, tests, tx, edu))
        n_rows += 1
    return "\n".join(body), n_rows, n_imgs


HTML = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dermatology Comparison Chart &mdash; CMS I Exam 1</title>
<link rel="stylesheet" href="../theme.css">
<style>
  /* LIGHT PALETTE ONLY, deliberately.
     theme.css gives every non-index page dark mode by inverting the content
     wrapper -- `:root[data-theme="dark"] body > .wrap { filter: invert(1)
     hue-rotate(180deg) }` -- and re-inverting img/video so photographs are not
     rendered as negatives. A page that ALSO ships its own dark palette gets
     both, and the two cancel: an earlier draft here darkened the table and
     theme.css then inverted it back to light while the rest of the site went
     dark, leaving the "How to use this" panel as dark text on a dark ground.
     So there is one mechanism, not two, and it is the site's. */
  :root{
    --acc:#17494b; --acc2:#3f7d7a; --gold:#c08a2e;
    --c-line:#cfdcdb; --c-tbl:#fff; --c-zebra:#f7fbfa; --c-fg:#1b2b2a;
    --c-name:#17494b; --c-b:#123c3d; --c-pt:#4a5f5e; --c-warn:#8c3b12;
    --c-panel:#eef5f4; --c-panel-fg:#1b2b2a; --c-labs-h:#8a6508;
    --c-btn-bg:#fff; --c-dup:#8a6508; --c-mute:#4c5f5e; --c-mute2:#5f7170;
    --c-gv-bg:#fdf6e7; --c-gv-b:#7a4d05; --c-gv-h:#8a6508;
  }
  body{margin:0;}
  .wrap{max-width:1700px;margin:0 auto;padding:18px 14px 90px;}
  header.top{text-align:center;padding:26px 12px 6px;}
  header.top h1{margin:0 0 6px;font-size:clamp(1.4rem,3.4vw,2.1rem);color:var(--acc);}
  header.top p{margin:3px 0;color:var(--c-mute);font-size:.95rem;}
  .howto{max-width:900px;margin:14px auto 22px;padding:12px 14px;border-left:4px solid var(--gold);
    background:var(--c-panel);color:var(--c-panel-fg);border-radius:0 8px 8px 0;
    font-size:.92rem;line-height:1.55;}
  .filterbar{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin:0 0 16px;}
  /* Print / Download-as-PDF. theme.css only un-clips `.table-scroll`; this page
     is a wide table in its own scroll box, so without these it exports as a
     clipped strip. Landscape, repeating header, no row split across a break. */
  @media print{
    .filterbar, .savehint{display:none !important;}
    .wrap{max-width:none !important;padding:0 !important;}
    .scroll{overflow:visible !important;border:0 !important;}
    table{min-width:0 !important;width:100% !important;font-size:7.4pt !important;
      table-layout:fixed;}
    td,th{padding:4px 5px !important;}
    thead th{position:static !important;background:#17494b !important;color:#fff !important;
      -webkit-print-color-adjust:exact;print-color-adjust:exact;}
    tr.sec td{position:static !important;background:#3f7d7a !important;color:#fff !important;
      -webkit-print-color-adjust:exact;print-color-adjust:exact;}
    td.pic{width:150px !important;min-width:150px !important;}
    td.pic img{max-height:96px !important;width:auto !important;}
    td.pic figcaption{font-size:5.6pt !important;}
    .pt{font-size:7pt !important;}
    .labs{background:#f2f6f5 !important;padding:3px 5px !important;
      -webkit-print-color-adjust:exact;print-color-adjust:exact;}
    td.name{width:110px !important;min-width:110px !important;}
    tr,figure{break-inside:avoid;page-break-inside:avoid;}
    .howto{break-inside:avoid;}
    @page{size:A4 landscape;margin:10mm 8mm;}
  }
  .filterbar button{font:inherit;font-size:.85rem;font-weight:600;padding:6px 13px;border-radius:999px;
    border:1.5px solid var(--acc2);background:var(--c-btn-bg);color:var(--c-name);cursor:pointer;}
  .filterbar button[aria-pressed="true"]{background:var(--acc);color:#fff;border-color:var(--acc);}
  .scroll{overflow-x:auto;-webkit-overflow-scrolling:touch;border:1px solid var(--c-line);border-radius:12px;}
  table{border-collapse:collapse;width:100%;min-width:1180px;background:var(--c-tbl);}
  thead th{position:sticky;top:0;z-index:3;background:var(--acc);color:#fff;font-size:.86rem;
    letter-spacing:.02em;text-align:left;padding:10px 11px;border-right:1px solid rgba(255,255,255,.18);}
  thead th:last-child{border-right:0;}
  td{vertical-align:top;padding:11px;border-top:1px solid var(--c-line);color:var(--c-fg);
    font-size:.87rem;line-height:1.5;}
  tr.sec td{background:var(--acc2);color:#fff;font-weight:700;font-size:.95rem;padding:8px 12px;
    position:sticky;left:0;}
  tbody tr:not(.sec):nth-child(even) td{background:var(--c-zebra);}
  td.pic{width:230px;min-width:230px;}
  td.pic img{width:100%;height:auto;border-radius:7px;display:block;border:1px solid var(--c-line);}
  td.pic figcaption{font-size:.68rem;color:var(--c-mute2);margin-top:4px;line-height:1.35;}
  td.pic figcaption .deck{display:block;font-style:italic;color:var(--c-mute2);}
  td.pic figure{margin:0;}
  .nopic{font-size:.72rem;color:var(--c-mute2);font-style:italic;padding:14px 6px;border:1px dashed var(--c-line);
    border-radius:7px;text-align:center;}
  td.name{width:150px;min-width:150px;font-weight:700;color:var(--c-name);font-size:.95rem;}
  .pt{display:block;margin-top:6px;font-style:italic;color:var(--c-pt);}
  .warn{color:var(--c-warn);font-weight:600;}
  .labs{margin-top:9px;padding:7px 9px;border-radius:7px;background:var(--c-panel);
    color:var(--c-panel-fg);border-left:3px solid var(--gold);font-size:.83rem;line-height:1.45;}
  .labs-h{display:block;font-size:.66rem;font-weight:800;letter-spacing:.07em;
    text-transform:uppercase;color:var(--c-labs-h);margin-bottom:3px;}
  .dup{display:block;font-weight:600;font-size:.68rem;color:var(--c-dup);
    text-transform:uppercase;letter-spacing:.04em;margin-top:3px;}
  /* The vignette-giveaway column. Deliberately the loudest cell on the row:
     it is the one you scan when a stem is in front of you. */
  td.gv{background:var(--c-gv-bg);border-left:3px solid var(--gold);
    font-size:.82rem;line-height:1.5;}
  td.gv b{color:var(--c-gv-b);font-weight:800;}
  th.gv-h{background:var(--c-gv-h);}
  b{color:var(--c-b);}
</style>
</head><body>
<!-- theme.js gates its corner "Download as PDF" button on .guide-back-bar. -->
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">
<header class="top">
  <h1>Dermatology Comparison Chart</h1>
  <p>Clinical Medicine and Surgery I &middot; Exam 1 &middot; Class of 2028</p>
  <p>__NROWS__ conditions across Lectures __LECTURES__ &middot; __NIMGS__ images from the lecture slides</p>
  <p style="margin-top:10px;font-size:.82rem;color:var(--c-mute)">Use the <b>Download as PDF</b> button, top
  right, to keep this offline &mdash; it prints landscape with every row and every photograph intact.</p>
</header>

<div class="howto"><b>How to use this.</b> Read it left to right for one condition: what it looks like,
what it is called, <b>the words a question will use to hand it to you</b>, how it presents and how a patient
will actually describe it, what you order first and what confirms it, what you give first and what comes
next, and what you tell them. Read it top to bottom down one column to compare across conditions.<br><br>
<b>The gold &ldquo;Vignette giveaway&rdquo; column</b> is the one to scan when a stem is in front of you.
Professor Jaquith described this exam as <i>&ldquo;pretty much all clinical vignettes &hellip; make sure that
you are able to recognize conditions by the vignette&rdquo;</i>, and a vignette gives itself away with a
handful of words &mdash; <i>coin-shaped</i>, <i>glazed appearing</i>, <i>tapioca-like</i>, <i>herald
patch</i>, <i>spares the scrotum</i>. Those words are in that column, per condition, so you can read the
chart in the direction the question actually arrives: <b>phrase first, diagnosis second</b>. Every phrase
there is language the lecture decks themselves use &mdash; classic buzzwords that are NOT in your decks are
deliberately left out. <b>Everything here comes from the lecture PowerPoints</b>, and every
picture cites its deck and slide. Where a deck does not state something, the cell says so rather than
being filled in from elsewhere.<br><br><b>The gold &ldquo;Labs to order&rdquo; block</b> in the testing
column tells you what blood work to send &mdash; and, just as often, that there is none to send.
<b>__NNOLABS__ of the __NROWS__ conditions here need no blood work at all</b>; dermatology is mostly a
clinical diagnosis, and knowing which ones are the exception is the point of reading down that column.</div>

<div class="filterbar" id="fb"></div>

<div class="scroll">
<table>
<thead><tr>
  <th>Picture</th><th>Name</th><th class="gv-h">Vignette giveaway<br><span style="font-weight:400;color:#cfe3e1">the words that hand it to you</span></th><th>Common manifestation<br><span style="font-weight:400;color:#cfe3e1">and how a patient may describe it</span></th>
  <th>First test &amp; gold standard</th><th>First line &rarr; second line treatment</th><th>Patient education</th>
</tr></thead>
<tbody>
__BODY__
</tbody>
</table>
</div>

<p style="text-align:center;margin-top:26px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
<p style="text-align:center;font-size:13px;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</div>
<script src="../theme.js"></script>
<script>
(function(){
  var secs=[].slice.call(document.querySelectorAll('tr.sec'));
  var fb=document.getElementById('fb');
  function mk(label,idx){
    var b=document.createElement('button');
    b.textContent=label; b.setAttribute('aria-pressed', idx===-1?'true':'false');
    b.onclick=function(){
      [].forEach.call(fb.children,function(x){x.setAttribute('aria-pressed','false');});
      b.setAttribute('aria-pressed','true');
      var show=(idx===-1), i=-1;
      [].slice.call(document.querySelectorAll('tbody tr')).forEach(function(tr){
        if(tr.classList.contains('sec')){ i++; show=(idx===-1)||(i===idx); }
        tr.style.display = show ? '' : 'none';
      });
    };
    fb.appendChild(b);
  }
  mk('All',-1);
  secs.forEach(function(tr,i){
    mk(tr.getAttribute('data-label') || ('Section '+(i+1)), i);
  });
})();
</script>
</body></html>
"""


def main():
    mapping = prep_images()
    body, n_rows, n_imgs = render(mapping)
    import re as _re
    nolabs = sum(1 for b in _re.findall(r'<div class="labs">.*?</div>', body, _re.S)
                 if _re.search(r"<b>(None|No bloods|No workup)", b))
    # Lecture list DERIVED from the rows, never hardcoded. It used to read
    # "Lectures 2, 3, 4, 5 and 8" and had already gone stale before Lecture 6
    # was added -- Lecture 7 was in the chart but missing from that sentence.
    lec_nums = sorted({int(r[0].split("_")[0][1:]) for r in ROWS
                       if r[0] and r[0] != "SECTION"})
    lec_str = (", ".join(str(x) for x in lec_nums[:-1]) + " and " + str(lec_nums[-1])
               if len(lec_nums) > 1 else str(lec_nums[0]))
    html = (HTML.replace("__BODY__", body)
                .replace("__LECTURES__", lec_str)
                .replace("__NROWS__", str(n_rows))
                .replace("__NNOLABS__", str(nolabs))
                .replace("__NIMGS__", str(n_imgs)))
    open(OUT_HTML, "w", encoding="utf-8").write(html)
    kb = sum(os.path.getsize(os.path.join(OUT_DIR, f)) for f in os.listdir(OUT_DIR)) // 1024
    print("wrote %s" % os.path.basename(OUT_HTML))
    print("  %d conditions, %d images (%d KB total), %d KB of HTML"
          % (n_rows, n_imgs, kb, len(html) // 1024))
    # every cell must be populated
    for row in ROWS:
        if row[0] == "SECTION":
            continue
        for i, cell in enumerate(row[1:], 1):
            assert cell and cell.strip(), "empty cell %d in %r" % (i, row[1])
    print("  every cell populated; %d of %d need no blood work" % (nolabs, n_rows))
    # A lazy-loaded image that never entered the viewport is missing from the
    # print output. An export before this check carried 10 of 84 photographs.
    assert 'loading="lazy"' not in html, "lazy images will not survive Download as PDF"
    assert html.count("<img ") == n_imgs, "image count mismatch"
    assert 'class="guide-back-bar"' in html, "no back bar, so theme.js adds no PDF button"
    assert "@media print" in html, "no print rules"
    used_stems = {r[0].rsplit(".", 1)[0] for r in ROWS if r[0] and r[0] != "SECTION"}
    used_metaphor = sorted(METAPHOR_IMAGES & used_stems)
    assert not used_metaphor, ("a row takes its image from a visual metaphor rather than a "
                               "clinical photograph: %r" % used_metaphor)
    used_wrong = sorted(WRONG_DISEASE_IMAGES & used_stems)
    assert not used_wrong, ("a row takes its image from a differential-diagnosis slide, so the "
                            "picture is of a DIFFERENT disease: %r" % used_wrong)
    used_micro = sorted(MICROGRAPH_IMAGES & used_stems)
    assert not used_micro, ("a row illustrates a disease with a micrograph rather than a "
                            "clinical photograph: %r" % used_micro)
    bad_slides = non_content_slides()
    for row in ROWS:
        if row[0] == "SECTION" or not row[0]:
            continue
        tag, sl = slide_of(row[0])
        assert sl not in bad_slides.get(tag, ()), (
            "%s takes its image from %s slide %d, which is a non-content slide"
            % (row[1], tag, sl))
    print("  no image taken from a title / questions / resources slide")
    # theme.css dark mode is filter:invert on body > .wrap, and text dimmed
    # with `opacity` under that filter rendered near-black on near-black.
    # Dim with an explicit colour instead.
    import re as _o
    bad = _o.findall(r"opacity:\.?\d", html)
    assert not bad, "opacity-dimmed text will misbehave under the wrap invert: %r" % bad
    # See the palette comment in the stylesheet: theme.css already does dark
    # mode for this page by inverting body > .wrap. A page-level dark palette
    # fights it and the two cancel out.
    assert "prefers-color-scheme" not in html, (
        "page-level dark palette fights theme.css's wrap inversion")
    import re as _r
    assert not _r.search(r':root\[data-theme=[^\]]*\]\s*\{', html), (
        "page-level data-theme palette fights theme.css's wrap inversion")
    assert html.count('class="labs"') == n_rows, "every row needs a labs block"
    print("  images eager, back bar present, print rules present")


if __name__ == "__main__":
    main()
