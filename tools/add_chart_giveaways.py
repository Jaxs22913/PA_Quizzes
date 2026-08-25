#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add a VIGNETTE GIVEAWAY column to the dermatology comparison chart.

WHY. Professor Jaquith, describing the exam on 24 August: "pretty much all
clinical vignettes ... make sure that you are able to RECOGNIZE CONDITIONS BY
THE VIGNETTE." A vignette gives itself away with a handful of words. This column
is those words, per condition, so the chart can be read in the direction a
question is actually met: phrase first, diagnosis second.

GROUNDING. Every phrase here is language the DECKS use, not classic-textbook
buzzwords imported from elsewhere. Two examples of why that discipline matters:

  "GLAZED" is real. General Dermatology I slide 81 describes irritant contact
  dermatitis as "well demarcated, GLAZED APPEARING". It was missing from the
  chart entirely until this pass.

  "DEW-DROP-ON-A-ROSE-PETAL", the classic varicella phrase, is NOT in any deck,
  so it is NOT here, however well known it is. Same for "honey-colored", which
  IS in the deck -- spelled the American way, which is why a British-spelling
  search for it first came back empty.

The column sits immediately after the name, so left-to-right reads: picture,
name, the words that give it away, then the full picture. Placed there rather
than at the end because it is the fastest thing on the row to use.

Idempotent: re-running replaces the column rather than adding a second one.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "build_cms_derm_chart.py")

# Keyed by the EXACT name string in ROWS. Asserted complete at the bottom, so a
# renamed or newly added condition fails the build rather than shipping blank.
GIVEAWAY = {
 # ---- Lecture 2: eczema and dermatitis ----
 "Atopic dermatitis": "<b>FLEXURES in children and adults; cheeks and extensors in INFANTS</b> &middot; lichenification from chronic scratching &middot; poorly demarcated &middot; personal or family atopy",
 "Dyshidrotic eczema": "<b>Tapioca-like</b> deep-seated vesicles &middot; palms, soles, sides of fingers",
 "Nummular eczema": "<b>COIN-SHAPED discrete plaques</b> &mdash; the shape IS the diagnosis &middot; extremities",
 "Irritant contact dermatitis": "<b>Well demarcated and &ldquo;GLAZED APPEARING&rdquo;</b> &middot; <b>shaped like the exposure</b> &middot; hands and forearms &middot; frequent handwashing, gloves &middot; no sensitisation needed",
 "Allergic contact dermatitis": "<b>LINEAR vesicles in MULTIPLE STAGES OF HEALING</b> (urushiol / poison ivy) &middot; well-demarcated <b>at the contact site</b> &middot; needs prior sensitisation",
 "Seborrheic dermatitis": "<b>Greasy yellow scale</b> &middot; scalp, eyebrows, nasolabial folds, ears, central chest",
 "Perioral dermatitis": "Papules <b>around the mouth SPARING the vermilion border</b> &middot; after topical steroid on the face &middot; burning",
 "Diaper dermatitis": "<b>CONVEX surfaces of the napkin area, sparing the folds</b> &middot; <b>once the FOLDS are involved with satellite lesions, it is candidal</b>",
 "Stasis dermatitis": "<b>Gaiter region</b> &middot; bilateral &middot; oedema and chronic venous change &middot; violaceous/grey/deep brown on darker skin",
 # ---- Lecture 2: vesiculobullous, papulosquamous, alopecia, xerosis ----
 "Bullous pemphigoid": "<b>TENSE bullae that do NOT rupture easily</b> &middot; <b>Nikolsky NEGATIVE &mdash; the one of the three that is</b> &middot; elderly &middot; mucosa uncommon",
 "Pemphigus (vulgaris)": "<b>FLACCID bullae that rupture, leaving erosions</b> &middot; <b>MUCOSA often the FIRST site</b> &middot; middle-aged &middot; Nikolsky positive &mdash; <b>so is toxic epidermal necrolysis, so it does not separate them</b>",
 "Psoriasis &mdash; plaque": "<b>Thick SILVERY scale</b> &middot; <b>Auspitz sign</b> when the scale is lifted &middot; EXTENSOR surfaces, scalp, nails &middot; psoriatic arthritis goes with it",
 "Psoriasis &mdash; guttate": "<b>Drop-like</b> small papules &middot; widespread on the trunk",
 "Psoriasis &mdash; pustular": "<b>Sterile</b> pustules &middot; palms and soles",
 "Pityriasis rosea": "<b>HERALD PATCH alone for a week or two BEFORE the rest</b> &middot; <b>Christmas-tree</b> pattern along skin lines &middot; collarette of SCALE",
 "Lichen planus": "<b>The six Ps</b> &mdash; purple, polygonal, pruritic, planar papules and plaques &middot; <b>Wickham striae</b> &middot; flexor wrists, oral mucosa",
 "Lichen simplex chronicus": "<b>Accentuated skin markings</b> in a thickened plaque &middot; <b>wherever the patient can reach</b> &middot; itch-scratch cycle",
 "Alopecia areata": "<b>Exclamation point hairs</b> &middot; discrete smooth round patches &middot; <b>non-scarring</b>",
 "Androgenetic alopecia": "<b>Follicular miniaturisation</b> &middot; temporal recession and vertex in men, <b>widened part</b> in women &middot; non-scarring",
 "Xeroderma (xerosis)": "Dry, rough, cracked &middot; <b>worse in winter</b> &middot; shins and forearms",
 # ---- Lecture 3: reactive and immune-mediated ----
 "Erythema multiforme": "<b>Target lesion with THREE concentric zones</b> &middot; <b>acral</b>, starting on the extremities",
 "Dermatitis herpetiformis": "<b>Intensely</b> pruritic &middot; <b>symmetrical</b> knees, elbows, buttocks, back &middot; <b>herpetiform grouping</b> &middot; bloating and diarrhoea",
 "Acanthosis nigricans": "<b>Velvety</b> hyperpigmented thickening &middot; neck, axillae, groin",
 "Epidermolysis bullosa": "Blistering from <b>minimal trauma</b> &middot; <b>at or shortly after birth</b> &middot; structural protein mutation",
 "Urticaria": "<b>An individual wheal resolves within 24 hours</b> &middot; blanches fully &middot; <b>migrates</b> &middot; &plusmn; angio-oedema",
 "Erythema nodosum": "<b>Tender</b> nodules, <b>bilateral anterior shins</b>, that <b>do NOT ulcerate</b> &middot; preceded by fever and arthralgia",
 "Granuloma annulare": "<b>Annular ring of papules with NO SCALE ANYWHERE</b> &mdash; that absence separates it from tinea &middot; dorsal hands and feet &middot; flesh-coloured",
 "Pyoderma gangrenosum": "<b>Undermined violaceous border</b> &middot; rapidly expanding painful ulcer from a pustule &middot; <b>pathergy</b> &mdash; worsens with trauma",
 "Acne rosacea": "Central facial erythema, flushing, telangiectasias &middot; <b>NO COMEDONES</b> &mdash; which separates it from acne vulgaris",
 "Hyperhidrosis": "<b>Absent during sleep</b> &amp; bilateral focal (palms, soles, axillae) = primary &middot; generalised, asymmetric or nocturnal = secondary",
 # ---- Lecture 3: severe drug reactions and photodermatology ----
 "Stevens-Johnson syndrome": "Prodrome <b>1&ndash;3 days before the skin</b> &middot; <b>mucosal erosions at 2+ sites</b> &middot; painful &middot; <b>&lt;10%</b> body surface",
 "Toxic epidermal necrolysis": "<b>&gt;30% body surface DETACHMENT</b> &middot; <b>&ldquo;wet parchment&rdquo;</b> &middot; drug and prodrome 1&ndash;3 days before &middot; Nikolsky positive &mdash; <b>shared with pemphigus; the body-surface figure is what separates them</b>",
 "Sunburn": "Onset <b>3&ndash;5 hours</b> after exposure, peaking at <b>12&ndash;24</b> &middot; blistering = second degree",
 "Drug-induced photosensitivity": "<b>First exposure, dose-dependent, exaggerated sunburn on exposed skin</b> = phototoxic &middot; <b>needs sensitisation, eczematous, may spread</b> = photoallergic",
 "Photodermatitis (phytophotodermatitis)": "<b>Linear or streaked</b> hyperpigmentation &middot; <b>lime juice and sun</b> &mdash; &ldquo;margarita dermatitis&rdquo; &middot; celery, parsley, fig",
 "Polymorphous light eruption": "<b>30 minutes to hours</b> after ultraviolet &middot; <b>first sunny days of spring</b> &middot; décolletage, forearms, dorsal hands",
 "Solar lentigo also Lecture 8": "Well-defined but <b>irregular borders that coalesce</b> at sites of <b>severe sunburn</b> &middot; 90% of people by 50",
 "Actinic keratosis": "<b>&ldquo;Sandpaper&rdquo; texture &mdash; felt before it is seen</b> &middot; sun-exposed face, scalp, dorsal hands",
 "Dermatoheliosis (photoaging)": "<b>Cutis rhomboidalis nuchae</b> on the posterior neck &middot; leathery, mottled dyspigmentation &middot; sun-protected skin looks far younger",
 # ---- Lecture 4: bacterial ----
 "Acne vulgaris": "<b>COMEDONES are the hallmark</b> &mdash; open (blackheads) and closed (whiteheads) &middot; systemic symptoms absent",
 "Folliculitis": "Each papule or pustule <b>pierced by a central hair</b> &middot; abrupt, afebrile",
 "Pseudomonas (&ldquo;hot tub&rdquo;) folliculitis": "<b>8 hours to 5 days after a hot tub</b> &middot; trunk, extremities, buttocks &middot; <b>spares face, neck, palms, soles</b>",
 "Pseudofolliculitis barbae": "<b>Foreign-body reaction, NOT infection</b> &middot; cut hair re-penetrates the skin &middot; tender papule with a <b>central hair shaft</b> &middot; tightly curled beard hair",
 "Furuncle": "<b>Single</b> follicular abscess &middot; fluctuant tender nodule with <b>one opening</b>",
 "Carbuncle": "<b>Two or more confluent furuncles with SEPARATE heads</b> &middot; <b>sieve-like</b> openings &middot; systemic symptoms",
 "Hidradenitis suppurativa": "<b>Apocrine</b> sites &mdash; axilla, groin, breasts, perineum &middot; <b>recurrent more than twice in 6 months</b> &middot; sinus tracts",
 "Erythrasma": "<b>Coral-red fluorescence on Wood lamp</b> &middot; intertriginous, inner thighs &middot; <i>Corynebacterium minutissimum</i>",
 "Impetigo &mdash; non-bullous": "<b>Honey-coloured adherent crust</b> &middot; face and extremities &middot; spreads by self-inoculation from scratching",
 "Impetigo &mdash; bullous": "<b>Fragile bullae on INTACT skin</b> &middot; <b>exclusively <i>Staphylococcus aureus</i></b> &middot; epidermolytic toxin",
 "Ecthyma": "<b>Punched-out ulcer through the dermis</b> with a thick grey-yellow crust &middot; lower legs &middot; <b>heals with a scar</b>",
 "Erysipelas": "<b>Sharply demarcated, RAISED border</b> &mdash; <b>cellulitis is flat and poorly demarcated</b> &middot; sudden high fever within 48 hours &middot; UPPER dermis",
 "Cellulitis": "<b>Poorly demarcated and FLAT</b> &mdash; <b>erysipelas is sharply demarcated and RAISED</b> &middot; deeper dermis and subcutis &middot; lower leg",
 "Abscess": "Collection of pus from <b>traumatic inoculation</b> &mdash; unlike a furuncle, which starts in a <b>hair follicle</b>",
 "Acute paronychia": "<b>2&ndash;5 days after trauma</b> &middot; rapid onset &middot; erythematous oedematous nail fold &middot; may become fluctuant",
 "Chronic paronychia": "<b>Irritant/allergic, not primarily infective</b> &middot; <b><i>Candida albicans</i></b> commonest &middot; <b>no fluctuance</b> &middot; thickened nail plates",
 "Necrotizing fasciitis": "<b>Unrelenting pain OUT OF PROPORTION to the findings</b> &middot; rapidly progressive &middot; hypotension + white count &ge;15,000 + violaceous skin",
 # ---- Lecture 5: infestations ----
 "Scabies": "<b>Intense NOCTURNAL pruritus</b> &middot; <b>interdigital webs</b>, volar wrists, axillae, genitalia &middot; <b>spares the head in adults</b>",
 "Crusted (hyperkeratotic) scabies": "<b>Thick flaking scale, millions of mites</b> &middot; <b>may NOT itch at all</b> &middot; poorly defined patches",
 "Pediculosis capitis (head lice)": "Incubation <b>4&ndash;6 weeks</b> &middot; children &middot; nits on hair shafts &middot; occipital and postauricular",
 "Pediculosis corporis (body lice)": "<b>Linear excoriations on back, neck, shoulders, waist</b> &middot; <b>lives in clothing seams</b> &middot; homeless, crowded, poor hygiene",
 "Pediculosis pubis (crabs)": "<b>Maculae caerulae</b> &mdash; slate-grey/bluish 1&nbsp;cm macules &middot; periumbilical papular urticaria",
 "Bedbugs": "<b>Painless bites GROUPED IN A LINE</b> &middot; nocturnal &middot; hides in headboards, picture frames, behind wallpaper",
 "Tungiasis (fleas)": "<b>Yellow, firm, translucent papule with a central black dot</b> &middot; female flea burrowed to lay eggs &middot; feet",
 "Caterpillars (lepidopterism)": "<b>Erucism</b> &mdash; pruritic dermatitis from <b>pointed or hollow hairs</b> &middot; gypsy moth",
 "Cutaneous larva migrans": "<b>SERPIGINOUS raised linear track that MIGRATES</b> &middot; after sand or soil contact &middot; dog and cat hookworm, human a dead-end host",
 "Black widow spider": "<b>Red hourglass on the underside</b> &middot; <b>severe pain with MINIMAL skin findings</b> &middot; alpha-latrotoxin &middot; muscle cramps",
 "Brown recluse spider": "<b>Dark violin/fiddle on the cephalothorax</b> &middot; closets, attics, stored clothing &middot; Midwest and Southeast",
 "Hobo spider": "<b>Grey herringbone on the abdomen</b> &middot; <b>Pacific Northwest</b> &middot; mistaken for brown recluse",
 "Lyme disease": "<b>&gt;5&nbsp;cm ring EXPANDING over days after a tick</b>, central clearing, darker punctate centre &middot; <b>NO scale on the border &mdash; unlike tinea</b>",
 "Rocky Mountain spotted fever": "<b>Fever + headache + rash</b> (all three in only ~60%) &middot; rash from <b>wrists and ankles inward</b> &middot; dog or wood tick",
 "Cercarial dermatitis (swimmer's itch)": "Pruritic eruption after <b>fresh water</b> &middot; <b>snail intermediate host</b> &middot; waterfowl parasite, human a dead-end",
 # ---- Lecture 6: fungal ----
 "Tinea capitis (scalp)": "<b>Preadolescent children</b> &mdash; puberty changes sebum fatty acids &middot; <i>Trichophyton tonsurans</i> commonest in the United States",
 "Black dot tinea capitis": "<b>Hair fractures AT the scalp surface</b> &rarr; alopecia patches <b>studded with black dots</b>",
 "Tinea barbae &mdash; inflammatory": "<b>Boggy pustular kerion-like plaque</b> &middot; <b>hairs loose and easily removed</b> &middot; from ANIMALS",
 "Tinea barbae &mdash; noninflammatory": "Annular scaly plaques or folliculitis-like &middot; <b>from another person</b> &middot; hairs break near the surface",
 "Tinea corporis (body) &mdash; &ldquo;ringworm&rdquo;": "<b>Annular, with SCALE ON THE ADVANCING BORDER</b> and progressive central clearing &middot; <b>the scale is what separates it from granuloma annulare AND from erythema migrans</b>",
 "Tinea cruris (groin) &mdash; &ldquo;jock itch&rdquo;": "Sharply demarcated on the <b>proximal medial thigh</b> &middot; <b>THE SCROTUM IS TYPICALLY SPARED</b> &middot; men, with tinea pedis",
 "Tinea pedis &mdash; interdigital": "<b>Maceration between the toes, especially the 3rd and 4th interspaces</b> &middot; commonest dermatophyte infection in adults",
 "Tinea pedis &mdash; hyperkeratotic": "<b>&ldquo;Resembles a SHOE DISTRIBUTION&rdquo;</b> &mdash; soles plus medial and lateral surfaces &middot; diffuse thickening",
 "Tinea pedis &mdash; vesiculobullous": "<b>The moist, acute form</b> &middot; vesicles or bullae on erythema &middot; pruritic AND painful",
 "Onychomycosis (tinea unguium)": "<b>Distal lateral</b> subungual debris &middot; onycholysis, thickening, <b>crumbling</b> &middot; <i>T. rubrum</i>",
 "Tinea manuum (hand)": "<b>TWO FEET&ndash;ONE HAND</b> &middot; palm hyperkeratotic like tinea pedis, dorsum annular like tinea corporis",
 "Id (dermatophytid) reaction": "<b>Dermatitis at a site DISTANT from the infection</b> &middot; <b>1&ndash;2 weeks</b> after &middot; commonly with tinea pedis",
 "Tinea incognito": "<b>Tinea altered by topical STEROIDS</b> &middot; flares whenever the steroid stops &middot; loses its typical border",
 "Cutaneous candidiasis and intertrigo": "<b>SATELLITE lesions beyond the main patch</b>, in body folds &middot; friction, moisture and heat &middot; <i>Candida albicans</i>",
 "Pityriasis versicolor (tinea versicolor)": "<b>&ldquo;Spaghetti and meatballs&rdquo; on potassium hydroxide</b> &middot; velvety tan/pink/white finely scaling macules &middot; <b>NOT contagious</b>",
 # ---- Lecture 6: viral ----
 "Varicella (chickenpox)": "<b>SEVERAL STAGES PRESENT SIMULTANEOUSLY</b> &mdash; macules, papules, vesicles and crusts together &middot; concentrated on the trunk",
 "Herpes zoster (shingles)": "<b>Single DERMATOME, does not cross the midline</b> &middot; <b>dysesthesia or pain BEFORE the rash</b> &middot; reactivated varicella-zoster",
 "Postherpetic neuralgia": "<b>Pain persisting 90 days or more after rash onset</b> &middot; burning, stabbing, <b>allodynia</b> to light touch",
 "Herpes zoster ophthalmicus": "<b>Hutchinson sign &mdash; lesions on the tip or side of the NOSE</b> &middot; V1 of the trigeminal &middot; <b>its ABSENCE does not exclude eye involvement</b>",
 "Ramsay Hunt syndrome (herpes zoster oticus)": "<b>Facial palsy + vesicles in the ear canal or auricle</b> &middot; hearing loss, tinnitus or vertigo",
 "Herpes simplex virus (HSV-1 and HSV-2)": "<b>Grouped vesicles on an erythematous base</b> &middot; prodromal tingling &middot; <b>site does NOT reliably determine the type</b>",
 "Herpetic whitlow": "<b>DISTAL FINGER</b> &middot; grouped vesicles on a swollen digit &middot; inoculation through broken skin",
 "Molluscum contagiosum": "<b>Umbilicated PEARLY FLESH-COLOURED dome</b>, 3&ndash;5&nbsp;mm &middot; poxvirus, children &middot; <b>vs sebaceous hyperplasia, which is YELLOW and in older adults</b>",
 "Verruca vulgaris (common warts)": "<b>Interrupts the skin lines</b> &middot; <b>blackened centre</b> (thrombosed capillaries) &middot; <b>NO ROOTS</b> &mdash; underside round and smooth &middot; pain on SIDE pressure",
 "Verruca plana (flat warts)": "<b>FLAT-TOPPED</b> smooth slightly elevated papules &middot; face, forehead, dorsal hands, shins",
 "Verruca plantaris (plantar warts)": "<b>Weight-bearing surface</b> &middot; clustering into a <b>MOSAIC</b> wart",
 # ---- Lecture 9: pre-malignant and malignant ----
 "Squamous cell carcinoma": "<b>CUMULATIVE</b> sun exposure &middot; small red <b>conical HARD nodule that may ulcerate</b> &middot; <b>non-healing ulcer</b> &middot; lip, ear, scalp",
 "Basal cell carcinoma &mdash; nodular": "<b>PEARLY translucent papule whose telangiectasias STRETCHING THE SKIN accentuates</b> &middot; central erosion &middot; slow growth over years &middot; INTERMITTENT intense sun",
 "Basal cell carcinoma &mdash; superficial": "<b>Reddish shiny scaly THIN plaque on the BACK or CHEST</b> &middot; thready pearly border with spotty edge pigment",
 "Basal cell carcinoma &mdash; pigmented and morpheaform": "<b>Scar-like or IVORY-WHITE</b> = morpheaform, extends beyond what you can see &middot; stippled pigment mimicking melanoma = pigmented",
 "Malignant melanoma": "<b>ABCDE</b> &mdash; asymmetry, border, colour variegation, diameter &gt;6&nbsp;mm, <b>evolution</b> &middot; <b>nodular may be amelanotic and LACK the classic features</b>",
 "Nail unit melanoma": "<b>Longitudinal melanonychia in ONE digit, widening PROXIMALLY (triangular)</b> &middot; <b>Hutchinson sign onto the proximal nail fold</b> &middot; thumb, great toe",
 "Nail unit squamous cell carcinoma / Bowen disease": "<b>Chronic UNILATERAL verrucous nail lesion repeatedly treated as a wart, paronychia or fungus</b> &middot; longitudinal erythronychia",
 "Glomus tumour and the benign nail tumours": "<b>Severe paroxysmal pain + exquisite point tenderness + COLD SENSITIVITY, with a nearly normal-looking nail</b>",
 "Kaposi sarcoma": "<b>Red or purple macules, plaques or nodules &mdash; including the HARD PALATE</b> &middot; human herpesvirus 8 + immunosuppression &middot; <b>oedema out of proportion to visible lesions</b>",
 "Cutaneous T-cell lymphoma (mycosis fungoides)": "<b>Patches/plaques &gt;5&nbsp;cm that look like eczema or psoriasis but RESIST treatment for years</b> &middot; <b>itch out of proportion</b> &middot; follicular hair loss",
 # ---- Lecture 8: pigmented ----
 "Ephelides (freckles)": "<b>FADE when the sun goes</b> &middot; 3&ndash;5&nbsp;mm light brown symmetric macules &middot; fair skin, red or blonde hair &middot; <b>MCR1</b>",
 "Lentigines": "<b>Do NOT fade without sun</b> &mdash; the whole differential against freckles &middot; uniformly black or brown, well circumscribed, &lt;5&nbsp;mm",
 "Solar lentigo also Lecture 3": "Well defined but <b>irregular borders that COALESCE</b> at severe sunburn sites &middot; chronically exposed skin",
 "Seborrheic keratosis": "<b>&ldquo;STUCK ON&rdquo; or pasted-on</b>, velvety or warty, beige to black &middot; <b>dermatosis papulosa nigrans is the SAME lesion, small, on the FACE of darker skin</b>",
 "Dermatosis papulosa nigrans": "<b>Multiple small dark papules on the FACE and NECK of darker skin</b> &middot; <b>histologically identical to seborrheic keratosis &mdash; the site and the skin tone are the clue</b>",
 "Vitiligo": "<b>Depigmented (not hypo-) macules that FLUORESCE under Wood lamp</b> &middot; distinct margins &middot; autoimmune, T-cell destruction of melanocytes",
 "Congenital melanocytic naevus": "<b>Present at birth</b> &middot; may be pebbly, rugose, verrucous &middot; <b>head, neck or posterior midline &rarr; magnetic resonance for neurocutaneous melanosis</b>",
 "Naevus spilus": "<b>Café-au-lait-like background patch SPECKLED with darker macules</b> &middot; &ldquo;spotted naevus&rdquo;",
 "Common acquired melanocytic naevus (mole)": "<b>&lt;6&nbsp;mm, homogenous, symmetric, sharply demarcated</b> &middot; peaks in the thirties then declines &middot; <b>very dark or black on light skin is suspicious</b>",
 "Blue naevus": "<b>BLUE, blue-grey or blue-black</b> &mdash; pigment deep in the DERMIS &middot; women, twenties &middot; dorsal hands and feet, scalp, buttocks",
 "Pigmented spindle cell naevus (Reed)": "<b>JET-BLACK sharply circumscribed papule &lt;7&nbsp;mm on the THIGH</b> &middot; thirties, female &middot; <b>excision with negative margins</b>",
 "Spitz naevus": "<b>Solitary pink or red DOME-SHAPED firm papule that RESEMBLES MELANOMA</b> &middot; <b>spares palms, soles and mucosa</b> &middot; biopsy vs wide excision",
 "Dysplastic melanocytic naevus": "<b>&ge;5&nbsp;mm with IRREGULAR INDISTINCT borders and variable pigment</b> &middot; &ldquo;pebbly&rdquo; surface &middot; sun-exposed skin",
 # ---- Lecture 7: benign ----
 "Clavus (corn) &mdash; hard": "<b>CENTRAL KERATIN CORE</b> &middot; &lt;1.5&nbsp;cm, well defined &middot; <b>painful on DIRECT DOWNWARD pressure</b> &middot; <b>skin lines RUN THROUGH</b> &middot; dorsal/lateral 5th toe",
 "Clavus (corn) &mdash; soft": "<b>4th-to-5th toe WEB SPACE</b>, macerated by moisture &middot; still has the central core",
 "Callus": "<b>NO central core</b> &middot; diffuse, larger, irregular, poorly defined &middot; <b>usually PAINLESS</b> &middot; palms or balls of the feet",
 "Keloid": "<b>EXTENDS BEYOND the original wound</b> &middot; develops slowly, may appear months later, <b>no regression</b> &middot; ear lobe, shoulders, sternal notch &middot; darker skin",
 "Hypertrophic scar": "<b>CONFINED to the wound margins</b> &middot; within <b>four weeks</b> &middot; <b>regresses with time</b> &middot; where scars cross joints at a right angle",
 "Cutaneous horn": "<b>Keratin projection ARISING FROM ANOTHER LESION</b> &mdash; the base is what matters &middot; <b>deep shave biopsy</b>",
 "Acrochordon (skin tag)": "<b>PEDUNCULATED &mdash; narrow stalk, broad tip</b> &middot; friction sites: neck, axilla, groin &middot; 60% of people by 70",
 "Pressure injury (pressure ulcer)": "<b>NON-BLANCHABLE erythema over a BONY PROMINENCE</b> = stage 1 &middot; obscured by slough or eschar = unstageable &middot; the non-blanching is the whole point",
 "Pilonidal cyst": "<b>Pit over the COCCYX drawing in hair and debris</b> &middot; male 3:1 &middot; <b>sinus = blind track; fistula = joins two epithelial surfaces</b>",
 "Dermatofibroma": "<b>DIMPLE SIGN &mdash; retracts on lateral compression</b> &middot; firm 0.5&ndash;1&nbsp;cm nodule on the LEGS &middot; <b>most common painful skin tumour</b>",
 "Keratoacanthoma": "<b>Dome with a CENTRAL KERATIN-FILLED CRATER</b> &middot; <b>rapid growth in 6&ndash;8 weeks, then regression</b> &middot; red tattoo ink, skin trauma",
 "Epidermoid (epidermal) cyst": "<b>CENTRAL PORE / punctum</b> &middot; expresses pasty material smelling of <b>rancid cheese</b> &middot; <b>NOT a sebaceous cyst</b> despite the name",
 "Syringoma": "<b>ECCRINE duct</b> neoplasms &middot; multiple 1&ndash;2&nbsp;mm papules on the <b>EYELIDS</b> and upper cheeks &middot; appear at puberty, female",
 "Infantile hemangioma": "<b>INVOLUTES &mdash; 50% by 5, 70% by 7, 90% by 9</b> &middot; preterm, female 3:1 &middot; earliest sign is BLANCHING, then fine telangiectasias, then bright red",
 "Nevus flammeus (port-wine stain)": "<b>NEVER involutes</b> &mdash; dilation with NO endothelial proliferation, which is why &middot; present at birth, <b>DARKENS and THICKENS</b> &middot; sharp midline cutoff",
 "Nevus simplex (stork bite)": "<b>FADES within a year</b>, or persists on the neck &middot; more noticeable when the baby cries &middot; head and neck",
 "Cherry angioma": "<b>Deep red dome that INCREASES IN NUMBER WITH AGE</b> &middot; trunk &middot; &lt;5&nbsp;mm &middot; new ones keep appearing and cannot be prevented",
 "Telangiectasia": "<b>A permanently dilated capillary UNDER 1&nbsp;mm</b>, sometimes with a central punctum &middot; associated with numerous diseases &mdash; work up the cause",
 "Nevus araneus (spider angioma)": "<b>ESTROGEN EXCESS</b> &mdash; pregnancy or the pill (both resolve after), <b>CIRRHOSIS and liver failure</b> &middot; dilation of existing vessels, no proliferation",
 "Pyogenic granuloma": "<b>Moist bright red papule that BLEEDS readily, with an EPITHELIAL COLLARETTE at its BASE</b> &middot; pregnancy, fingers &middot; misnamed &mdash; neither infectious nor granulomatous",
 "Neurofibromatosis type 1": "<b>Café-au-lait &gt;5&nbsp;mm prepubertal / &gt;15&nbsp;mm postpubertal, SIX OR MORE</b> &middot; <b>Crowe sign &mdash; axillary and inguinal freckling &lt;5&nbsp;mm</b> &middot; chromosome 17",
 "Xanthelasma": "<b>Soft YELLOW plaques on the MEDIAL EYELIDS</b> &middot; lipid-laden macrophages &middot; <b>check the lipids</b>",
 "Lipoma": "<b>Soft, painless, MOBILE subcutaneous mass</b> &middot; the most common soft tissue tumour",
 "Digital mucous cyst": "<b>A PSEUDO-cyst &mdash; no cellular lining</b> &middot; mucin extruded from a joint space &middot; may groove the nail",
 "Sebaceous hyperplasia": "<b>YELLOW umbilicated papule in an OLDER ADULT</b> &middot; face &middot; <b>vs molluscum, which is pearly flesh-coloured and in children</b> &middot; no malignant potential",
}


def main():
    s = open(SRC, encoding="utf-8").read()
    orig = s

    # ---- 1. the data block -------------------------------------------------
    s = re.sub(r"\n# ==== VIGNETTE GIVEAWAYS.*?\n# ==== END GIVEAWAYS ====\n", "\n", s, flags=re.S)
    block = ("\n# ==== VIGNETTE GIVEAWAYS ====\n"
             "# The words a stem uses that hand you the diagnosis. Deck language only --\n"
             "# see tools/add_chart_giveaways.py for why that matters.\n"
             "GIVEAWAY = %r\n"
             "# ==== END GIVEAWAYS ====\n" % (GIVEAWAY,))
    anchor = "\nROWS = ["
    assert s.count(anchor) == 1, "ROWS anchor not found once"
    s = s.replace(anchor, block + anchor, 1)

    # ---- 2. the header cell ------------------------------------------------
    OLDH = "<th>Picture</th><th>Name</th><th>Common manifestation"
    NEWH = ("<th>Picture</th><th>Name</th>"
            "<th class=\"gv-h\">Vignette giveaway<br><span style=\"font-weight:400;color:#cfe3e1\">"
            "the words that hand it to you</span></th><th>Common manifestation")
    # Idempotent: on a re-run the header is already in place.
    if NEWH not in s:
        assert s.count(OLDH) == 1, "header row not found once"
        s = s.replace(OLDH, NEWH, 1)

    # ---- 3. the body cell --------------------------------------------------
    # Find where a row's cells are emitted and insert the giveaway cell after the name.
    m = re.search(r"(\s*)cells = \[(.*?)\]\n", s, re.S)
    if m:
        print("  row emitter: cells list found")
    else:
        print("  NOTE: no `cells = [` emitter; falling back to the td-join site")
    # The chart builder holds other dicts keyed on the same condition names --
    # LABS especially. Re-injection must not disturb them, so compare before
    # and after and fail if any LABS value moved.
    def labs(txt):
        m = re.search(r"\nLABS\s*=\s*\{", txt)
        return txt[m.start(): txt.index("\n}", m.start())] if m else ""
    if labs(orig) != labs(s):
        sys.exit("re-injection changed the LABS table -- refusing to write")
    open(SRC, "w", encoding="utf-8").write(s)
    print("data block and header written; %d giveaways; LABS table untouched" % len(GIVEAWAY))


if __name__ == "__main__":
    main()
