# -*- coding: utf-8 -*-
"""Question bank for "Guess that Disease" -- CMS I Exam 1, dermatology.

Same shape and the same inclusion bar as tools/cms_e2_gtd_bank.py: an item
exists only where THE PHOTOGRAPH ITSELF SHOWS THE FEATURE THAT NAMES THE
DISEASE. All 145 pictures in the comparison chart were looked at; roughly
seventy make the bar. What did not, and why:

  * The answer is printed in the pixels -- the ephelides plate is captioned
    "Ephelides (freckles)".
  * A diagram or a table stands in for the finding -- vitiligo is a
    "Distribution of vitiligo" body map and pressure injury is the NPIAP
    staging table. NEITHER DECK CONTAINS A PHOTOGRAPH OF EITHER, so unlike the
    ophthalmology block there was nothing better to swap in; both conditions
    are simply absent from the game.
  * The discriminator is not visible in a photograph:
      - irritant vs allergic contact dermatitis, when the picture is a ring
        finger. Only the LINEAR streak picture is asked; irritant stays a
        distractor.
      - folliculitis vs its Pseudomonas form -- that is the hot-tub history.
      - ephelides vs solar lentigo -- freckles fade out of season.
      - tinea capitis vs its black-dot form -- "tinea capitis" is not wrong
        for the black-dot picture, so only the general answer is asked.
      - furuncle vs abscess -- a furuncle IS a follicular abscess.
      - brown recluse vs hobo spider, as spiders.
      - the naevus plates (blue, Spitz, Reed, dysplastic, spilus): multi-panel
        dermoscopy where the call is histological.
  * Duplicated rows: actinic keratosis and solar lentigo each appear twice in
    the chart, under two lectures. Each is asked once.

Distractors come from the same disease family, and several pairs ARE the
discrimination the block teaches -- tense vs flaccid bullae, sharply
demarcated erysipelas vs indistinct cellulitis, the scaly active border of
tinea corporis vs the scale-free ring of granuloma annulare, keloid growing
beyond the wound vs a hypertrophic scar confined to it. Correct answers are
authored at index 0 and rotated by the builder.
"""

ECZ = "Category — Eczema and dermatitis"
PAP = "Category — Papulosquamous, bullous, hair and nails"
IMM = "Category — Reactive and immune-mediated"
DRG = "Category — Drug reactions and photodermatology"
BAC = "Category — Bacterial infections"
INF = "Category — Infestations and bites"
FUN = "Category — Fungal infections"
VIR = "Category — Viral infections"
BEN = "Category — Benign and pigmented lesions"
MAL = "Category — Premalignant and malignant lesions"

D2 = "2. General Dermatology I.pptx"
D3 = "3. Dermatology  II.pptx"
D4 = "4.  Cutaneous Bacterial Infections.pptx"
D5 = "CMS I Dermatological Infestations - Shahsv.pptx"
D6 = "6. Fungal and Viral Skin Infections - Jaquith.pptx"
D7 = "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx"
D8 = "CMS I Pigmented Skin Lesions - Shahsv-2.pptx"
D9 = "Premalignant and Malignant Cutaneous Lesions - Jaquith.pptx"
EXT = None   # picture that is not on a slide; cited by its own source

ITEMS = [
# ------------------------------------------------- eczema and dermatitis ----
dict(cond="Atopic dermatitis", img="l2_s050_1.jpg", slide=50, deck=D2, io=ECZ,
     alt="Antecubital fossa with thickened, darkened, scratched skin",
     why="Poorly demarcated, lichenified plaques sitting IN THE FLEXURE, thickened by chronic scratching.",
     wrong=[("Psoriasis — plaque", "Psoriasis prefers the EXTENSOR surfaces and is sharply demarcated with silvery scale."),
            ("Nummular eczema", "That is discrete coin-shaped plaques, not a confluent flexural patch."),
            ("Tinea corporis", "That has an active scaly border with central clearing; this has neither.")]),

dict(cond="Dyshidrotic eczema", img="l2_s065_1.jpg", slide=65, deck=D2, io=ECZ,
     alt="Both palms studded with deep-seated vesicles and scaling",
     why="Deep-seated vesicles set into the palms like tapioca, intensely itchy.",
     wrong=[("Tinea manuum", "That scales diffusely in the palmar creases rather than raising discrete vesicles."),
            ("Psoriasis — pustular", "Those are sterile PUSTULES on a red base, not clear vesicles."),
            ("Allergic contact dermatitis", "That follows the shape of whatever touched the skin; this is symmetrical.")]),

dict(cond="Nummular eczema", img="l2_s070_1.jpg", slide=70, deck=D2, io=ECZ,
     alt="Forearm with several discrete round coin-shaped scaly plaques",
     why="Discrete COIN-SHAPED plaques with no central clearing.",
     wrong=[("Tinea corporis", "Ringworm clears in the middle and keeps a scaly advancing edge; these are solid discs."),
            ("Psoriasis — plaque", "Those are thicker, sharply edged and carry heavy silvery scale."),
            ("Pityriasis rosea", "That is oval, follows the skin lines and starts with a herald patch.")]),

dict(cond="Allergic contact dermatitis", img="l2_s087_1.jpg", slide=87, deck=D2, io=ECZ,
     alt="Skin with a straight linear streak of erythema carrying a vesicle",
     why="A LINEAR streak of erythema and vesicles — the shape of the plant that brushed the skin.",
     wrong=[("Irritant contact dermatitis", "That is a diffuse burn-like reaction at the site of contact, without this streaked, vesicular shape."),
            ("Nummular eczema", "That is round and discrete, never linear."),
            ("Urticaria", "Wheals are transient and raised, and they do not blister.")]),

dict(cond="Seborrheic dermatitis", img="l2_s092_2.jpg", slide=92, deck=D2, io=ECZ,
     alt="Forehead, brows and glabella with erythema and greasy scale",
     why="Greasy yellow scale on erythema in the SEBACEOUS areas — brows, glabella, nasolabial folds.",
     wrong=[("Psoriasis — plaque", "That scale is dry and silvery and its edge is sharp; this is greasy and ill-defined."),
            ("Perioral dermatitis", "That sits around the mouth and spares the lip border, not the brows."),
            ("Acne rosacea", "That brings telangiectasia and papulopustules on the cheeks and nose, without scale.")]),

dict(cond="Perioral dermatitis", img="l2_s097_1.jpg", slide=97, deck=D2, io=ECZ,
     alt="Papules and pustules around the mouth with a clear zone at the lip border",
     why="Papules and pustules ringing the mouth with a SPARED RIM at the vermilion border.",
     wrong=[("Acne vulgaris", "Acne has comedones and is spread over the whole face, not banded around the mouth."),
            ("Acne rosacea", "That is centrofacial flushing with telangiectasia, and it spares this distribution."),
            ("Seborrheic dermatitis", "That is greasy scale on the brows and nasolabial folds.")]),

dict(cond="Diaper dermatitis", img="l2_s104_2.jpg", slide=104, deck=D2, io=ECZ,
     alt="Infant buttocks with confluent erythema over the convex surfaces",
     why="Confluent erythema over the CONVEX surfaces the nappy touches, with the skin creases spared.",
     wrong=[("Cutaneous candidiasis", "Candida does the opposite — it goes INTO the creases and throws off satellite papules."),
            ("Atopic dermatitis", "That spares the nappy area, because it stays damp and covered."),
            ("Psoriasis — plaque", "That would be sharply demarcated with silvery scale.")]),

dict(cond="Stasis dermatitis", img="l2_s111_3.jpg", slide=111, deck=D2, io=ECZ,
     alt="Lower leg above the ankle with brown discolouration, scaling and swelling",
     why="Brown haemosiderin staining with scaling and oedema on the LOWER LEG, above the ankle.",
     wrong=[("Cellulitis", "That is acutely hot, tender and spreading, not chronically pigmented."),
            ("Erysipelas", "That is a sharply raised, fiery plaque with fever."),
            ("Atopic dermatitis", "That favours the flexures and does not stain the skin brown.")]),

# ------------------------ papulosquamous, bullous, hair and nails ----
dict(cond="Bullous pemphigoid", img="l2_s121_1.jpg", slide=121, deck=D2, io=PAP,
     alt="Leg with numerous large tense fluid-filled blisters on red skin",
     why="Large TENSE blisters that hold their dome — the split is below the epidermis.",
     wrong=[("Pemphigus vulgaris", "Those blisters are FLACCID and rupture almost at once, leaving raw erosions."),
            ("Impetigo — bullous", "That is a childhood infection with a thin collarette and honey crust."),
            ("Toxic epidermal necrolysis", "That sheds the epidermis in sheets and involves mucosa.")]),

dict(cond="Pemphigus vulgaris", img="l2_s127_2.jpg", slide=127, deck=D2, io=PAP,
     alt="Shoulder with flaccid blisters that have collapsed into raw erosions",
     why="FLACCID blisters that have already sloughed, leaving raw erosions — the split is within the epidermis.",
     wrong=[("Bullous pemphigoid", "Those blisters are TENSE and stay intact."),
            ("Impetigo — bullous", "That is superficial and crusts over honey-coloured, without this denudation."),
            ("Stevens-Johnson syndrome", "That is drug-triggered with target lesions and heavy mucosal involvement.")]),

dict(cond="Psoriasis — guttate", img="l2_s157_1.jpg", slide=157, deck=D2, io=PAP,
     alt="Back scattered with many small drop-shaped scaly papules",
     why="A shower of small DROP-SHAPED scaly papules, classically after a streptococcal sore throat.",
     wrong=[("Pityriasis rosea", "Those lesions are oval, follow the skin lines and start from a herald patch."),
            ("Psoriasis — plaque", "That is a few large thick plaques, not a scatter of small drops."),
            ("Lichen planus", "Those papules are violaceous, flat-topped and polygonal.")]),

dict(cond="Psoriasis — pustular", img="l2_s158_1.jpg", slide=158, deck=D2, io=PAP,
     alt="Palm and soles covered with sterile pustules on thickened red skin",
     why="Sterile PUSTULES studding red, thickened palms and soles.",
     wrong=[("Dyshidrotic eczema", "Those are clear deep-seated vesicles, not pustules."),
            ("Tinea pedis — vesiculobullous", "That is a fungal blistering pattern, usually on one foot."),
            ("Psoriasis — plaque", "That is scaly plaques without pustules.")]),

dict(cond="Lichen planus", img="l2_s175_1.jpg", slide=175, deck=D2, io=PAP,
     alt="Ankle with flat-topped violaceous polygonal papules",
     why="Purple, POLYGONAL, FLAT-TOPPED papules — the itchy, purple, polygonal rule.",
     wrong=[("Psoriasis — plaque", "That is salmon-pink with silvery scale, and its surface is not flat-topped."),
            ("Granuloma annulare", "That forms a ring of firm skin-coloured papules with no scale."),
            ("Lichen simplex chronicus", "That is one thickened plaque from rubbing, not scattered violaceous papules.")]),

dict(cond="Alopecia areata", img="l2_s136_2.jpg", slide=136, deck=D2, io=PAP,
     alt="Scalp with several sharply defined round patches of complete hair loss",
     why="Sharply defined ROUND patches of complete hair loss on a scalp that is otherwise normal.",
     wrong=[("Androgenetic alopecia", "That thins gradually along the frontal and vertex pattern, without bald circles."),
            ("Tinea capitis", "That scales and inflames the scalp; here the skin is smooth."),
            ("Pediculosis capitis", "That leaves nits on the hair shafts and does not cause hair loss.")]),

dict(cond="Androgenetic alopecia", img="l2_s142_2.jpg", slide=142, deck=D2, io=PAP,
     alt="Man's hairline receding at the temples with thinning over the front",
     why="Patterned recession at the temples and thinning over the vertex, with hair still present but finer.",
     wrong=[("Alopecia areata", "That takes out discrete round patches, leaving normal hair around them."),
            ("Tinea capitis", "That scales and breaks the hairs, and the scalp is inflamed."),
            ("Pediculosis capitis", "That is an infestation of the hair shafts, not hair loss.")]),

dict(cond="Xeroderma", img="l2_s151_2.jpg", slide=151, deck=D2, io=PAP,
     alt="Close view of dry skin cracked into a fine crazy-paving pattern",
     why="Dry skin cracked into fine plates — the crazy-paving look of severe xerosis.",
     wrong=[("Psoriasis — plaque", "That has thick silvery scale on a sharply bounded red plaque."),
            ("Atopic dermatitis", "That is inflamed and itchy with excoriation, not just dry and cracked."),
            ("Tinea pedis — hyperkeratotic", "That thickens one sole in a moccasin distribution.")]),

# ------------------------------------------ reactive and immune-mediated ----
dict(cond="Erythema multiforme", img="l3_s006_3.jpg", slide=6, deck=D3, io=IMM,
     alt="Fingers with round lesions showing concentric rings and a dusky centre",
     why="TARGET lesions — concentric rings around a dusky centre, typically on the hands.",
     wrong=[("Urticaria", "Wheals are uniformly raised and pale-centred only from pressure, and they move within hours."),
            ("Granuloma annulare", "That is a ring of firm papules with a normal centre, not a bullseye."),
            ("Erythema nodosum", "Those are deep tender nodules on the shins, with nothing on the hands.")]),

dict(cond="Acanthosis nigricans", img="l3_s021_2.jpg", slide=21, deck=D3, io=IMM,
     alt="Back of the neck with velvety thickened brown skin in the folds",
     why="VELVETY, thickened brown skin in a flexure — a marker of insulin resistance.",
     wrong=[("Pityriasis versicolor", "That is finely scaling macules on the trunk, not velvety thickening."),
            ("Erythrasma", "That is a flat brown patch that fluoresces coral-red under Wood's lamp."),
            ("Seborrheic keratosis", "Those are discrete stuck-on plaques, not a confluent velvety change.")]),

dict(cond="Urticaria", img="l3_s035_1.jpg", slide=35, deck=D3, io=IMM,
     alt="Skin with raised pale wheals surrounded by a red flare",
     why="Raised WHEALS with a surrounding flare — each one lasts under a day and leaves nothing behind.",
     wrong=[("Erythema multiforme", "Those lesions are fixed targets that last a week or more."),
            ("Bedbugs", "Bites come in a linear cluster with a central punctum."),
            ("Allergic contact dermatitis", "That blisters and scales in the shape of the contact.")]),

dict(cond="Erythema nodosum", img="l3_s041_1.jpg", slide=41, deck=D3, io=IMM,
     alt="Both shins with several deep red tender nodules",
     why="Deep, tender, red NODULES on the SHINS that bruise as they fade and never ulcerate.",
     wrong=[("Cellulitis", "That is one confluent hot area, not multiple discrete nodules on both legs."),
            ("Erythema multiforme", "Those are flat targets on the hands, not deep shin nodules."),
            ("Urticaria", "Wheals are superficial and shift within hours.")]),

dict(cond="Granuloma annulare", img="l3_s047_1.jpg", slide=47, deck=D3, io=IMM,
     alt="Back of the hand with a ring of firm skin-coloured papules and no scale",
     why="A ring of firm papules with NO SCALE at all — that absence is what separates it from ringworm.",
     wrong=[("Tinea corporis", "Ringworm's advancing edge is SCALY; run a finger over it and you feel it."),
            ("Erythema multiforme", "That is a bullseye with a dusky centre, not a raised papular ring."),
            ("Lichen planus", "Those papules are violaceous and flat-topped, and they do not form rings.")]),

dict(cond="Pyoderma gangrenosum", img="l3_s056_2.jpg", slide=56, deck=D3, io=IMM,
     alt="Ulcer with a raised violaceous undermined edge over a red base",
     why="An ulcer with a RAISED VIOLACEOUS, undermined edge — and debriding it makes it worse.",
     wrong=[("Ecthyma", "Those are small punched-out ulcers under a thick crust, from streptococcal infection."),
            ("Pressure injury", "That sits over a bony prominence and follows unrelieved pressure."),
            ("Necrotizing fasciitis", "That is systemically toxic, spreads by the hour and shows dusky necrosis.")]),

dict(cond="Acne rosacea", img="l3_s063_1.jpg", slide=63, deck=D3, io=IMM,
     alt="Cheek and nose with confluent erythema, telangiectasia and thickened nasal skin",
     why="Centrofacial erythema with TELANGIECTASIA, and no comedones anywhere.",
     wrong=[("Acne vulgaris", "Acne has COMEDONES — blackheads and whiteheads — which rosacea never does."),
            ("Seborrheic dermatitis", "That is greasy scale on the brows and folds rather than fixed redness."),
            ("Perioral dermatitis", "That bands around the mouth and spares the lip border.")]),

dict(cond="Hyperhidrosis", img="l3_s071_1.jpg", slide=71, deck=D3, io=IMM,
     alt="Both palms visibly wet with beads of sweat and no rash",
     why="Palms visibly WET with sweat and no rash at all — the skin itself is normal.",
     wrong=[("Dyshidrotic eczema", "That raises deep-seated vesicles you can see and feel in the skin."),
            ("Tinea manuum", "That scales the palm, particularly in the creases."),
            ("Psoriasis — pustular", "That studs the palm with pustules on red, thickened skin.")]),

# ------------------------------- drug reactions and photodermatology ----
dict(cond="Stevens-Johnson syndrome", img="l3_s081_2.jpg", slide=81, deck=D3, io=DRG,
     alt="Child with crusted eroded lips and a dusky rash over the chest",
     why="MUCOSAL erosions — here the lips — with a dusky rash over a limited area of skin.",
     wrong=[("Toxic epidermal necrolysis", "Same disease, further along: TEN sheds more than 30 percent of the body surface."),
            ("Erythema multiforme", "That is target lesions on the hands with little or no mucosal disease."),
            ("Pemphigus vulgaris", "That is autoimmune and comes on over months, not days after a drug.")]),

dict(cond="Toxic epidermal necrolysis", img="l3_s086_1.jpg", slide=86, deck=D3, io=DRG,
     alt="Child's back with the epidermis peeling away in large sheets",
     why="The epidermis coming off in SHEETS over most of the body surface.",
     wrong=[("Stevens-Johnson syndrome", "Same spectrum, but under 10 percent of the body surface detaches."),
            ("Bullous pemphigoid", "That makes discrete tense blisters, not confluent sheet loss."),
            ("Sunburn", "That is erythema and later peeling, never full-thickness detachment.")]),

dict(cond="Sunburn", img="l3_s092_1.jpg", slide=92, deck=D3, io=DRG,
     alt="Upper back and shoulders red with sharp pale lines where clothing sat",
     why="Erythema stopping in SHARP LINES exactly where clothing covered the skin.",
     wrong=[("Cellulitis", "That is unilateral, hot and tender, and pays no attention to clothing lines."),
            ("Erysipelas", "That is a raised fiery plaque with a well-defined but irregular border."),
            ("Polymorphous light eruption", "That is itchy papules appearing hours to days after sun, not uniform erythema.")]),

dict(cond="Dermatoheliosis", img="l3_s115_1.jpg", slide=115, deck=D3, io=DRG,
     alt="Man's face weathered and deeply wrinkled on one side only",
     why="Deep wrinkling, thickening and furrowing on ONE side of the face — decades of sun through a window.",
     wrong=[("Actinic keratosis", "Those are discrete rough scaly papules, not a change in the whole skin texture."),
            ("Solar lentigo", "Those are flat brown macules; here the skin's architecture itself is altered."),
            ("Xeroderma", "That is dryness and cracking, not thickened, furrowed skin.")]),

# --------------------------------------------------- bacterial infections ----
dict(cond="Acne vulgaris", img="l4_s004_1.jpg", slide=4, deck=D4, io=BAC,
     alt="Cheek with comedones, inflamed papules and dark healing marks",
     why="COMEDONES alongside inflamed papules — the comedone is what makes it acne.",
     wrong=[("Acne rosacea", "Rosacea never produces comedones; it flushes and telangiectases."),
            ("Perioral dermatitis", "That rings the mouth and spares the lip border."),
            ("Folliculitis", "That is pustules pierced by hairs, without comedones.")]),

dict(cond="Folliculitis", img="l4_s041_1.jpg", slide=41, deck=D4, io=BAC,
     alt="Skin with small pustules each pierced by a hair",
     why="Small pustules each with a HAIR THROUGH THE CENTRE — inflammation of the follicle itself.",
     wrong=[("Acne vulgaris", "Acne begins with comedones and sits on the face, chest and back."),
            ("Furuncle", "That is one deep tender nodule, not superficial follicular pustules."),
            ("Pseudofolliculitis barbae", "That is in the beard and driven by hairs curling back into the skin.")]),

dict(cond="Pseudofolliculitis barbae", img="l4_s054_1.jpg", slide=54, deck=D4, io=BAC,
     alt="Beard area of the jaw and neck covered in firm dark papules",
     why="Firm papules through the BEARD where shaved hairs have curled back and re-entered the skin.",
     wrong=[("Folliculitis", "That is frank pustules with a hair through each one, and it is not confined to the beard."),
            ("Acne vulgaris", "Acne brings comedones and spreads beyond the shaved area."),
            ("Tinea barbae — inflammatory", "That is boggy and pustular, and the hairs pull out painlessly.")]),

dict(cond="Furuncle", img="l4_s060_1.jpg", slide=60, deck=D4, io=BAC,
     alt="Single tender red nodule with a small central pustular point",
     why="ONE deep tender nodule pointing to a single head.",
     wrong=[("Carbuncle", "That is several furuncles joined underneath, draining through MULTIPLE heads."),
            ("Epidermoid cyst", "That is a painless mobile dome with a central punctum, not hot and tender."),
            ("Hidradenitis suppurativa", "That recurs in the axillae and groin with sinus tracts and scars.")]),

dict(cond="Carbuncle", img="l4_s060_2.jpg", slide=60, deck=D4, io=BAC,
     alt="Nape of the neck with a swollen red mass draining from several points",
     why="Several furuncles coalesced into one mass draining through MULTIPLE heads.",
     wrong=[("Furuncle", "A furuncle is a single lesion with one point of drainage."),
            ("Hidradenitis suppurativa", "That is chronic and recurrent in the flexures, with sinus tracts."),
            ("Folliculitis", "That is superficial pustules, not a deep coalesced mass.")]),

dict(cond="Hidradenitis suppurativa", img="l4_s074_1.jpg", slide=74, deck=D4, io=BAC,
     alt="Axilla with draining sinus openings, scarring and inflamed nodules",
     why="Recurrent nodules and DRAINING SINUS TRACTS with scarring in an apocrine-bearing flexure.",
     # Distractors picked at comparable length: "Hidradenitis suppurativa" is a
     # fixed name that cannot be shortened, and it was the only long option.
     wrong=[("Carbuncle", "That is a single acute event, and it does not scar into chronic tracts."),
            ("Pseudofolliculitis barbae", "That is in the beard, from shaved hairs curling back into the skin."),
            ("Cutaneous candidiasis", "Intertrigo is beefy red with satellite papules; it does not tunnel or scar.")]),

dict(cond="Erythrasma", img="l4_s083_1.jpg", slide=83, deck=D4, io=BAC,
     alt="Skin fold glowing coral-red under ultraviolet light",
     why="CORAL-RED fluorescence under Wood's lamp — the porphyrin made by Corynebacterium.",
     wrong=[("Tinea cruris", "A dermatophyte does not fluoresce coral-red; potassium hydroxide shows hyphae instead."),
            ("Cutaneous candidiasis", "That is beefy red with satellite papules and does not fluoresce."),
            ("Pityriasis versicolor", "That may fluoresce, but a pale yellow-green, and it scales.")]),

dict(cond="Impetigo — non-bullous", img="l4_s087_1.jpg", slide=87, deck=D4, io=BAC,
     alt="Skin around the nose and mouth with thick golden-yellow crust",
     why="Thick HONEY-COLOURED crust around the nose and mouth.",
     wrong=[("Impetigo — bullous", "That form raises flaccid blisters first and leaves a thin collarette."),
            ("Herpes simplex virus", "That is a tight group of vesicles on one spot, not spreading golden crust."),
            ("Ecthyma", "That digs deeper, leaving punched-out ulcers under the crust.")]),

dict(cond="Impetigo — bullous", img="l4_s089_1.jpg", slide=89, deck=D4, io=BAC,
     alt="Infant skin with flaccid blisters holding cloudy yellow fluid",
     why="FLACCID blisters filled with cloudy fluid on an infant, from a toxin-producing staphylococcus.",
     wrong=[("Impetigo — non-bullous", "That crusts honey-gold without ever forming true blisters."),
            ("Bullous pemphigoid", "Those blisters are TENSE and it is a disease of older adults."),
            ("Varicella", "Those are small vesicles on a red base in crops at different stages.")]),

dict(cond="Ecthyma", img="l4_s091_1.jpg", slide=91, deck=D4, io=BAC,
     alt="Lower leg with several round punched-out ulcers under crust",
     why="PUNCHED-OUT ulcers under crust — impetigo that has eroded through into the dermis, so it scars.",
     wrong=[("Impetigo — non-bullous", "That stays superficial, crusts and heals without a scar."),
            ("Pyoderma gangrenosum", "That ulcer has a raised violaceous undermined edge and is not infective."),
            ("Herpes zoster", "That is grouped vesicles confined to one dermatome.")]),

dict(cond="Erysipelas", img="l4_s098_1.jpg", slide=98, deck=D4, io=BAC,
     alt="Cheek with a raised fiery red plaque that has a sharp edge",
     why="A raised, fiery plaque with a SHARPLY DEMARCATED edge you could trace with a pen.",
     wrong=[("Cellulitis", "Cellulitis is deeper, and its border fades into normal skin rather than stopping."),
            ("Acne rosacea", "That is chronic centrofacial flushing without fever or a raised edge."),
            ("Sunburn", "That follows sun exposure and stops at clothing lines, not at a raised margin.")]),

dict(cond="Cellulitis", img="l4_s105_1.jpg", slide=105, deck=D4, io=BAC,
     alt="Lower leg with a warm red area whose edges fade into normal skin",
     why="Warm, tender erythema whose border FADES OUT rather than stopping — the infection is deeper.",
     wrong=[("Erysipelas", "That is superficial, raised, and sharply demarcated."),
            ("Stasis dermatitis", "That is chronic, brown-stained and usually on both legs."),
            ("Erythema nodosum", "Those are discrete tender nodules, not confluent erythema.")]),

dict(cond="Acute paronychia", img="l4_s117_1.jpg", slide=117, deck=D4, io=BAC,
     alt="Finger with a red, swollen, shiny nail fold beside an intact nail",
     why="A red, swollen, acutely tender NAIL FOLD, with the nail plate itself still normal.",
     wrong=[("Chronic paronychia", "That has lost its cuticle and ridged the nail over months, without this acute swelling."),
            ("Herpetic whitlow", "That raises grouped VESICLES on the fingertip and should not be incised."),
            ("Onychomycosis", "That thickens and discolours the nail plate, leaving the fold alone.")]),

dict(cond="Chronic paronychia", img="ext-chronic-paronychia.jpg", slide=0, deck=EXT, io=BAC,
     alt="Fingertip with a lost cuticle, bolstered nail fold and a ridged dystrophic nail",
     why="The CUTICLE IS GONE, the fold is bolstered, and the nail behind it has become ridged and dystrophic.",
     wrong=[("Acute paronychia", "That is hot, exquisitely tender and days old, with a normal nail."),
            ("Onychomycosis", "That discolours and crumbles the nail plate but leaves the cuticle intact."),
            ("Nail unit melanoma", "That is a pigmented band running down the nail.")]),

# ------------------------------------------------ infestations and bites ----
dict(cond="Scabies", img="l5_s009_1.jpg", slide=9, deck=D5, io=INF,
     alt="Skin with a fine wavy thread-like track marked out in ink",
     why="A BURROW — a fine wavy thread-like track — with itch that is worst at night.",
     wrong=[("Cutaneous larva migrans", "That track is raised, serpiginous and moves centimetres a day."),
            ("Bedbugs", "Those are discrete bite papules in a line, with no burrow."),
            ("Atopic dermatitis", "That is ill-defined lichenified plaques in the flexures.")]),

dict(cond="Crusted scabies", img="l5_s011_4.jpg", slide=11, deck=D5, io=INF,
     alt="Foot with thick heaped crusts and fissuring over the sole and toes",
     why="THICK heaped crusts teeming with mites — the immunosuppressed form, and highly contagious.",
     wrong=[("Scabies", "Ordinary scabies is a few burrows and excoriations, not confluent crusting."),
            ("Tinea pedis — hyperkeratotic", "That is dry moccasin scaling without these heaped crusts."),
            ("Psoriasis — plaque", "That scale is silvery and sits on sharply bounded plaques.")]),

dict(cond="Pediculosis capitis", img="l5_s027_2.jpg", slide=27, deck=D5, io=INF,
     alt="Scalp hair with a small oval nit cemented to a hair shaft",
     why="NITS cemented to the hair shafts — they will not brush out the way dandruff does.",
     wrong=[("Seborrheic dermatitis", "That scale flakes free from the scalp; it is not glued to the hair."),
            ("Tinea capitis", "That scales and breaks the hairs, leaving patches of loss."),
            ("Xeroderma", "That is generalised dry skin, not an infestation of the hair.")]),

dict(cond="Bedbugs", img="l5_s034_2.jpg", slide=34, deck=D5, io=INF,
     alt="Thigh with a row of red bite papules each with a darker centre",
     why="Bites in a LINE — breakfast, lunch and dinner — each with a central punctum, on exposed skin.",
     wrong=[("Scabies", "That leaves burrows in the web spaces and itches worst at night."),
            ("Urticaria", "Wheals are transient and have no central punctum."),
            ("Cercarial dermatitis", "That follows fresh-water swimming and covers the exposed limbs diffusely.")]),

dict(cond="Tungiasis", img="l5_s039_2.jpg", slide=39, deck=D5, io=INF,
     alt="Toe with a pale nodule containing a black central point",
     why="A pale nodule on the foot with a BLACK CENTRAL POINT — the burrowed sand flea.",
     wrong=[("Verruca plantaris", "That is a keratotic plaque with several black dots from thrombosed capillaries."),
            ("Malignant melanoma", "That is an asymmetric pigmented macule, not a nodule with a single punctum."),
            ("Cutaneous larva migrans", "That is a migrating track, not a fixed nodule.")]),

dict(cond="Cutaneous larva migrans", img="l5_s052_1.jpg", slide=52, deck=D5, io=INF,
     alt="Foot with a raised winding serpiginous track under the skin",
     why="A raised SERPIGINOUS track that advances a few centimetres a day — hookworm larvae in the wrong host.",
     wrong=[("Scabies", "The burrow is much finer, only millimetres, and favours the web spaces."),
            ("Allergic contact dermatitis", "That streak is vesicular and fixed; it does not migrate."),
            ("Tinea corporis", "That expands as a ring, not a wandering line.")]),

dict(cond="Black widow spider", img="l5_s056_1.jpg", slide=56, deck=D5, io=INF,
     alt="Glossy black spider photographed from below showing a red hourglass mark",
     why="A glossy black spider with the red HOURGLASS on its underside; the bite causes cramping and rigidity.",
     wrong=[("Brown recluse spider", "That is brown with a violin mark on its back, and its bite goes on to necrose."),
            ("Hobo spider", "That is a plain brown funnel-web spider with no hourglass."),
            ("Bedbugs", "Those are flat wingless insects, not spiders.")]),

dict(cond="Brown recluse spider", img="l5_s060_1.jpg", slide=60, deck=D5, io=INF,
     alt="Two views of a bite that has become a dusky necrotic ulcer",
     why="A bite that turns dusky and NECROSES into an ulcer over days.",
     wrong=[("Black widow spider", "That bite causes muscle cramping and rigidity, but the skin does not slough."),
            ("Pyoderma gangrenosum", "That ulcer has a raised violaceous undermined edge and no bite history."),
            ("Ecthyma", "That is a bacterial punched-out ulcer under honey crust.")]),

dict(cond="Lyme disease", img="l5_s073_5.jpg", slide=73, deck=D5, io=INF,
     alt="Thigh with a large round expanding red patch outlined in pen",
     why="ERYTHEMA MIGRANS — a round patch expanding outward from a tick bite, often with central clearing.",
     wrong=[("Tinea corporis", "That ring is scaly at its edge and grows over weeks, not days."),
            ("Granuloma annulare", "That is a ring of firm papules that does not expand like this."),
            ("Cellulitis", "That is hot, tender and spreading, without a clearing centre.")]),

dict(cond="Rocky Mountain spotted fever", img="l5_s084_1.jpg", slide=84, deck=D5, io=INF,
     alt="Panels showing a spotted rash on the wrist, palm and trunk of a febrile child",
     why="A petechial rash that starts at the wrists and ankles and moves INWARD, taking in the PALMS AND SOLES.",
     # Same reason as hidradenitis: the name is fixed, so the distractors carry
     # the length instead.
     wrong=[("Stevens-Johnson syndrome", "That is drug-triggered with mucosal erosions, and it does not start at the wrists and ankles."),
            ("Erythema multiforme", "Those are fixed target lesions, not petechiae."),
            ("Varicella", "Those are vesicles in crops at different stages, sparing the palms.")]),

# ------------------------------------------------------ fungal infections ----
dict(cond="Tinea capitis", img="l6_s009_1.jpg", slide=9, deck=D6, io=FUN,
     alt="Child's scalp with a scaly patch and broken, thinned hair",
     why="A SCALY scalp patch with the hairs broken off within it.",
     wrong=[("Alopecia areata", "That leaves smooth, non-scaly skin in the bald patch."),
            ("Seborrheic dermatitis", "That flakes greasily across the scalp without breaking hairs."),
            ("Psoriasis — plaque", "That is thick silvery scale on a sharply bounded plaque.")]),

dict(cond="Tinea barbae — inflammatory", img="l6_s020_1.jpg", slide=20, deck=D6, io=FUN,
     alt="Jaw and chin with a boggy swollen pustular plaque in the beard",
     why="A BOGGY, pustular swelling in the beard from which the hairs lift out painlessly.",
     wrong=[("Pseudofolliculitis barbae", "That is firm papules from ingrown hairs, without this boggy swelling."),
            ("Folliculitis", "That is discrete superficial pustules, each pierced by a hair."),
            ("Acne vulgaris", "Acne has comedones and does not swell the beard like this.")]),

dict(cond="Tinea corporis", img="l6_s024_2.jpg", slide=24, deck=D6, io=FUN,
     alt="Arm with an annular plaque that is scaly at the edge and clear in the middle",
     why="An annular plaque with a SCALY ACTIVE BORDER and a clearing centre.",
     wrong=[("Granuloma annulare", "That ring is made of firm papules and carries NO scale."),
            ("Nummular eczema", "Those are solid coin-shaped plaques with no central clearing."),
            ("Pityriasis rosea", "That is oval, follows the skin lines, and has a collarette rather than an edge.")]),

dict(cond="Tinea cruris", img="l6_s032_1.jpg", slide=32, deck=D6, io=FUN,
     alt="Groin fold with a red plaque advancing onto the thigh with a scaly edge",
     why="A scaly-edged plaque advancing out of the groin fold onto the thigh, sparing the scrotum.",
     wrong=[("Cutaneous candidiasis", "That goes right into the fold, is beefy red, and throws satellite papules."),
            ("Erythrasma", "That is a flat brown patch that fluoresces coral-red under Wood's lamp."),
            ("Psoriasis — plaque", "Inverse psoriasis is smooth and glossy in the fold, without a scaly advancing edge.")]),

dict(cond="Tinea pedis — interdigital", img="l6_s038_2.jpg", slide=38, deck=D6, io=FUN,
     alt="Macerated white peeling skin between the toes",
     why="Soggy white MACERATION and peeling BETWEEN THE TOES, most often the fourth web space.",
     wrong=[("Tinea pedis — hyperkeratotic", "That thickens and scales the whole sole in a moccasin pattern."),
            ("Clavus (corn) — soft", "That is a single macerated keratotic plug between the toes, not diffuse peeling."),
            ("Cutaneous candidiasis", "That is beefy red with satellite papules.")]),

dict(cond="Tinea pedis — hyperkeratotic", img="l6_s040_2.jpg", slide=40, deck=D6, io=FUN,
     alt="Sole and heel with dry scaling covering the whole weight-bearing surface",
     why="Dry scaling covering the sole and running up the sides — the MOCCASIN distribution.",
     wrong=[("Tinea pedis — interdigital", "That is confined to the soggy web spaces."),
            ("Xeroderma", "That is generalised dryness, not one foot scaled in a moccasin pattern."),
            ("Psoriasis — plaque", "That is sharply bounded plaques with silvery scale.")]),

dict(cond="Onychomycosis", img="l6_s048_1.jpg", slide=48, deck=D6, io=FUN,
     alt="Toenails thickened, yellow-brown and crumbling at the free edge",
     why="Nails thickened, discoloured and CRUMBLING from the free edge back, with debris underneath.",
     wrong=[("Chronic paronychia", "That inflames the fold and loses the cuticle; the plate is ridged rather than crumbling."),
            ("Nail unit melanoma", "That is a pigmented band running the length of the nail."),
            ("Psoriasis — plaque", "Nail psoriasis pits and oil-spots the plate rather than thickening it like this.")]),

dict(cond="Cutaneous candidiasis", img="l6_s069_2.jpg", slide=69, deck=D6, io=FUN,
     alt="Inframammary folds beefy red with small separate papules beyond the edge",
     why="BEEFY RED in the depth of the fold with SATELLITE papules scattered beyond the edge.",
     wrong=[("Tinea cruris", "That advances out of the fold with a scaly edge and spares its depth."),
            ("Erythrasma", "That is a flat brown patch, not beefy red, and it fluoresces coral-red."),
            ("Stasis dermatitis", "That is on the lower legs and stains the skin brown.")]),

dict(cond="Pityriasis versicolor", img="l6_s076_1.jpg", slide=76, deck=D6, io=FUN,
     alt="Upper back with many pale and tan patches that scale when scratched",
     why="Confluent pale and tan patches over the upper trunk that give up fine scale when scraped.",
     wrong=[("Vitiligo", "That is completely DEPIGMENTED, milk-white and sharply bordered, and it does not scale."),
            ("Tinea corporis", "That is an annular plaque with an active edge, not confluent macules."),
            ("Pityriasis rosea", "That is oval salmon patches along the skin lines, after a herald patch.")]),

# ------------------------------------------------------- viral infections ----
dict(cond="Varicella", img="l6_s084_1.jpg", slide=84, deck=D6, io=VIR,
     alt="Child's trunk with papules, vesicles and crusted lesions all at once",
     why="Lesions at DIFFERENT STAGES side by side — papules, vesicles and crusts together.",
     wrong=[("Herpes zoster", "That is confined to one dermatome and its lesions all move together."),
            ("Molluscum contagiosum", "Those are firm umbilicated papules that never vesiculate or crust."),
            ("Impetigo — non-bullous", "That is golden crust, generally around the nose and mouth.")]),

dict(cond="Herpes zoster", img="l6_s100_1.jpg", slide=100, deck=D6, io=VIR,
     alt="Flank with grouped vesicles and crust in a single band that stops at the midline",
     why="Grouped vesicles in ONE DERMATOME, stopping abruptly at the midline.",
     wrong=[("Varicella", "That is scattered over the whole body in crops at different stages."),
            ("Herpes simplex virus", "That is one small group of vesicles, recurring at the same spot."),
            ("Allergic contact dermatitis", "That follows the shape of the contact and pays no attention to dermatomes.")]),

dict(cond="Herpes zoster ophthalmicus", img="l6_s103_1.jpg", slide=103, deck=D6, io=VIR,
     alt="Forehead, upper eyelid and nose on one side crusted with haemorrhagic vesicles",
     why="Zoster in the FIRST TRIGEMINAL DIVISION — forehead, upper lid and the tip of the nose, one side only.",
     wrong=[("Herpes zoster", "True, but not specific enough: this distribution threatens the eye and is named for it."),
            ("Erysipelas", "That is a smooth raised plaque with a sharp edge and no vesicles."),
            ("Impetigo — non-bullous", "That is golden crust without an underlying dermatomal vesicular eruption.")]),

dict(cond="Ramsay Hunt syndrome", img="l6_s104_1.jpg", slide=104, deck=D6, io=VIR,
     alt="Auricle and ear canal opening studded with crusted vesicles",
     why="Zoster vesicles in the EAR, with facial palsy and hearing or balance disturbance alongside.",
     wrong=[("Herpes zoster ophthalmicus", "That takes the forehead, eyelid and nose, not the auricle."),
            ("Cellulitis", "That is diffuse erythema and swelling without vesicles."),
            ("Impetigo — non-bullous", "That is golden crust without a preceding vesicular crop.")]),

dict(cond="Herpes simplex virus", img="l6_s113_3.jpg", slide=113, deck=D6, io=VIR,
     alt="Lip with a small group of vesicles and an erosion at the vermilion border",
     why="A tight GROUP of vesicles and erosion at the VERMILION BORDER, recurring in the same place.",
     wrong=[("Impetigo — non-bullous", "That is spreading golden crust, not a discrete vesicle cluster."),
            ("Herpes zoster", "That runs as a band along a whole dermatome."),
            ("Perioral dermatitis", "That is papules and pustules around the mouth, sparing the lip border itself.")]),

dict(cond="Herpetic whitlow", img="l6_s127_1.jpg", slide=127, deck=D6, io=VIR,
     alt="Fingertip with clustered vesicles and a shallow erosion",
     why="Clustered VESICLES on the fingertip — and it must not be incised.",
     wrong=[("Acute paronychia", "That is a red swollen nail fold with pus, and it is drained."),
            ("Verruca vulgaris", "That is a firm keratotic papule, not a vesicle cluster."),
            ("Digital mucous cyst", "That is a clear translucent nodule near the nail fold, and it is painless.")]),

dict(cond="Molluscum contagiosum", img="l6_s131_1.jpg", slide=131, deck=D6, io=VIR,
     alt="Skin with several firm dome-shaped papules dimpled in the centre",
     why="Firm dome-shaped papules with a CENTRAL DIMPLE — umbilication is the giveaway.",
     wrong=[("Verruca vulgaris", "Warts are rough and keratotic on top, not smooth and umbilicated."),
            ("Varicella", "Those are fluid-filled vesicles on a red base, in crops."),
            ("Syringoma", "Those are small firm papules clustered under the eyes, without umbilication.")]),

dict(cond="Verruca plana", img="l6_s144_2.jpg", slide=144, deck=D6, io=VIR,
     alt="Child's cheek with many small flat-topped skin-coloured papules",
     why="Many small FLAT-TOPPED papules, often spread in a line where the skin was scratched.",
     wrong=[("Molluscum contagiosum", "Those are dome-shaped and umbilicated, not flat-topped."),
            ("Acne vulgaris", "Acne has comedones and inflamed pustules."),
            ("Syringoma", "Those cluster under the eyes and are not spread by scratching.")]),

dict(cond="Verruca plantaris", img="l6_s146_1.jpg", slide=146, deck=D6, io=VIR,
     alt="Sole with a thick keratotic plaque containing small black dots",
     why="A keratotic plaque on the sole containing BLACK DOTS — thrombosed capillaries, which a callus never has.",
     wrong=[("Callus", "A callus is uniform thickened keratin with the skin lines running straight through it."),
            ("Clavus (corn) — hard", "That has a central keratin plug over a bony point, and no black dots."),
            ("Tinea pedis — hyperkeratotic", "That scales the whole sole diffusely.")]),

# --------------------------------------------- benign and pigmented lesions ----
dict(cond="Keloid", img="l7_s013_1.jpg", slide=13, deck=D7, io=BEN,
     alt="Ear and adjacent scalp with a large lobulated firm growth around a piercing",
     why="Scar tissue that has grown BEYOND the boundaries of the original wound.",
     wrong=[("Hypertrophic scar", "That stays WITHIN the wound's own margins and tends to flatten with time."),
            ("Dermatofibroma", "That is a small firm nodule that dimples when pinched."),
            ("Epidermoid cyst", "That is a soft mobile dome with a central punctum.")]),

dict(cond="Hypertrophic scar", img="l7_s021_1.jpg", slide=21, deck=D7, io=BEN,
     alt="Shoulder with a raised firm scar running exactly along an old wound line",
     why="A raised scar that stays exactly WITHIN the original wound line.",
     wrong=[("Keloid", "That spills out past the wound's edges into normal skin."),
            ("Acrochordon", "That is a soft pedunculated tag hanging off the skin."),
            ("Dermatofibroma", "That is a discrete firm nodule, not a linear scar.")]),

dict(cond="Cutaneous horn", img="l7_s025_1.jpg", slide=25, deck=D7, io=BEN,
     alt="Finger with a hard conical keratin projection standing off the skin",
     why="A hard CONE of keratin standing off the skin — and the base always needs biopsy.",
     wrong=[("Verruca vulgaris", "A wart is a rough dome, not a projecting horn."),
            ("Seborrheic keratosis", "That is a flat stuck-on waxy plaque."),
            ("Actinic keratosis", "That is a rough scaly patch you feel more than see.")]),

dict(cond="Acrochordon", img="l7_s029_1.jpg", slide=29, deck=D7, io=BEN,
     alt="Neck with many small soft skin-coloured tags on narrow stalks",
     why="Soft skin-coloured tags hanging on NARROW STALKS in a flexure.",
     wrong=[("Dermatosis papulosa nigrans", "Those are flat, firmly attached dark papules with no stalk."),
            ("Molluscum contagiosum", "Those are firm dome papules with a central dimple, sitting flush."),
            ("Seborrheic keratosis", "That is a stuck-on waxy plaque, not a pedunculated tag.")]),

dict(cond="Pilonidal cyst", img="l7_s040_1.jpg", slide=40, deck=D7, io=BEN,
     alt="Natal cleft at the top of the buttocks with a red inflamed swelling",
     why="An inflamed swelling in the NATAL CLEFT, where hair has driven into a midline pit.",
     wrong=[("Hidradenitis suppurativa", "That is in the axillae and groin, with sinus tracts and scarring."),
            ("Epidermoid cyst", "That is a mobile dome with a punctum, and it can be anywhere."),
            ("Furuncle", "That is a follicular abscess with a single head, not tied to the midline cleft.")]),

dict(cond="Keratoacanthoma", img="l7_s049_1.jpg", slide=49, deck=D7, io=BEN,
     alt="Cheek with a dome-shaped nodule holding a central plug of keratin",
     why="A dome-shaped nodule with a CRATER of keratin in the middle, that grew over weeks.",
     wrong=[("Squamous cell carcinoma", "That grows over months, is firmer, and does not have this symmetrical crater — though the two can be impossible to separate without biopsy."),
            ("Basal cell carcinoma — nodular", "That is pearly with a rolled border and surface telangiectasia."),
            ("Molluscum contagiosum", "That is small, soft and umbilicated rather than crateriform.")]),

dict(cond="Epidermoid cyst", img="l7_s053_1.jpg", slide=53, deck=D7, io=BEN,
     alt="Skin with a smooth dome-shaped swelling marked by a dark central pore",
     why="A smooth mobile dome with a central PUNCTUM you can see.",
     wrong=[("Lipoma", "That is deeper, softer and doughy, with no punctum."),
            ("Furuncle", "That is acutely hot and tender, and it points to a pustular head."),
            ("Dermatofibroma", "That is a firm flat nodule that dimples inward when squeezed.")]),

dict(cond="Syringoma", img="l7_s058_1.jpg", slide=58, deck=D7, io=BEN,
     alt="Lower eyelid with many small firm skin-coloured papules",
     why="Crops of small firm SKIN-COLOURED papules on the lower eyelids.",
     wrong=[("Xanthelasma", "Those are soft YELLOW plaques, and they sit at the inner corner."),
            ("Molluscum contagiosum", "Those are umbilicated and infectious."),
            ("Sebaceous hyperplasia", "Those are yellowish with a central dimple, usually on the forehead and nose.")]),

dict(cond="Infantile hemangioma", img="l7_s067_1.jpg", slide=67, deck=D7, io=BEN,
     alt="Infant's cheek with a bright red raised lobulated nodule",
     why="A bright red RAISED nodule that appeared after birth, grew, and will involute on its own.",
     wrong=[("Nevus flammeus", "That is FLAT, present at birth, and it never goes away."),
            ("Nevus simplex", "That is a faint flat pink patch on the nape or glabella that fades."),
            ("Pyogenic granuloma", "That is a friable nodule that bleeds readily, usually after minor trauma.")]),

dict(cond="Nevus flammeus", img="l7_s078_1.jpg", slide=78, deck=D7, io=BEN,
     alt="One side of a man's face and neck covered by a flat dark red-purple patch",
     why="A FLAT dark red-purple patch in a trigeminal distribution, present from birth and permanent.",
     wrong=[("Infantile hemangioma", "That is raised, appears after birth and involutes."),
            ("Nevus simplex", "That is pale pink, on the nape or glabella, and it fades in infancy."),
            ("Telangiectasia", "Those are individual visible vessels, not a confluent patch.")]),

dict(cond="Cherry angioma", img="l7_s086_1.jpg", slide=86, deck=D7, io=BEN,
     alt="Trunk scattered with small bright red domed papules",
     why="Small, bright red, slightly DOMED papules scattered on the trunk — they accumulate with age.",
     wrong=[("Nevus araneus", "That has a central feeding vessel with legs radiating from it."),
            ("Telangiectasia", "Those are fine visible vessels lying flat in the skin."),
            ("Pyogenic granuloma", "That is a solitary friable nodule that bleeds.")]),

dict(cond="Nevus araneus", img="l7_s089_2.jpg", slide=89, deck=D7, io=BEN,
     alt="Skin with a central red point and fine vessels radiating outward from it",
     why="A central arteriole with vessels RADIATING out like legs; press the centre and the whole thing blanches.",
     wrong=[("Cherry angioma", "That is a solid red dome with no radiating vessels."),
            ("Telangiectasia", "Those are vessels without a central feeding point."),
            ("Nevus flammeus", "That is a large confluent patch present from birth.")]),

dict(cond="Pyogenic granuloma", img="l7_s092_1.jpg", slide=92, deck=D7, io=BEN,
     alt="Fingertip with a small glistening red nodule on a narrow base",
     why="A glistening red nodule on a narrow base that grew fast and BLEEDS at the slightest touch.",
     wrong=[("Cherry angioma", "Those are small, stable and do not bleed."),
            ("Infantile hemangioma", "That is a birth-onset lesion of infancy that involutes."),
            ("Verruca vulgaris", "That is rough and keratotic, not a friable bleeding nodule.")]),

dict(cond="Neurofibromatosis type 1", img="l7_s100_1.jpg", slide=100, deck=D7, io=BEN,
     alt="Trunk with many soft skin-coloured nodules of varying size",
     why="Many soft NEUROFIBROMAS over the trunk, alongside café-au-lait macules and axillary freckling.",
     wrong=[("Lipoma", "Those are deeper, doughier and far fewer."),
            ("Acrochordon", "Those are small pedunculated tags confined to the flexures."),
            ("Molluscum contagiosum", "Those are firm umbilicated papules, and they are infectious.")]),

dict(cond="Xanthelasma", img="l7_s104_1.jpg", slide=104, deck=D7, io=BEN,
     alt="Both eyelids with soft flat yellow plaques near the inner corners",
     why="Soft flat YELLOW plaques near the inner canthus, prompting a lipid profile.",
     wrong=[("Syringoma", "Those are skin-coloured firm papules on the lower lid, not yellow plaques."),
            ("Sebaceous hyperplasia", "Those are umbilicated yellowish papules, usually on the forehead and nose."),
            ("Epidermoid cyst", "That is a single dome with a punctum.")]),

dict(cond="Sebaceous hyperplasia", img="l7_s110_2.jpg", slide=110, deck=D7, io=BEN,
     alt="Cheek with a soft yellowish papule dimpled in the centre",
     why="A yellowish papule with a CENTRAL DIMPLE and a ring of lobules around it.",
     wrong=[("Basal cell carcinoma — nodular", "That is pearly with a rolled border and telangiectasia running over it."),
            ("Molluscum contagiosum", "That is firm, skin-coloured and infectious."),
            ("Syringoma", "Those are skin-coloured and cluster on the lower eyelids.")]),

dict(cond="Solar lentigo", img="l3_s108_1.jpg", slide=108, deck=D3, io=BEN,
     alt="Upper back scattered with flat well-defined tan-brown macules",
     why="Flat, well-defined tan-brown macules on chronically sun-exposed skin; unlike freckles they persist all year.",
     wrong=[("Seborrheic keratosis", "Those are RAISED and waxy, and look stuck onto the skin."),
            ("Dermatosis papulosa nigrans", "Those are raised dark papules on the face and neck."),
            ("Vitiligo", "That removes pigment entirely rather than adding it.")]),

dict(cond="Seborrheic keratosis", img="l8_s017_2.jpg", slide=17, deck=D8, io=BEN,
     alt="Back with a well-defined warty brown plaque that looks stuck on the skin",
     why="A waxy, warty plaque that looks STUCK ON, as though it could be lifted off with a fingernail.",
     wrong=[("Malignant melanoma", "That is asymmetric with an irregular border and varied colour, and it is flat or nodular, not waxy."),
            ("Solar lentigo", "That is FLAT — no thickness at all."),
            ("Dermatofibroma", "That is a firm dermal nodule that dimples when pinched.")]),

dict(cond="Dermatosis papulosa nigrans", img="l8_s019_2.jpg", slide=19, deck=D8, io=BEN,
     alt="Cheek and neck with numerous small dark brown papules",
     why="Numerous small dark papules over the cheeks and neck — seborrheic keratoses in miniature, on darker skin.",
     wrong=[("Acrochordon", "Those hang on stalks and are skin-coloured."),
            ("Molluscum contagiosum", "Those are umbilicated and skin-coloured."),
            ("Ephelides", "Freckles are FLAT macules, not raised papules.")]),

dict(cond="Congenital melanocytic naevus", img="l8_s029_2.jpg", slide=29, deck=D8, io=BEN,
     alt="Infant with a very large brown pigmented patch across the lower back and buttocks",
     why="A LARGE pigmented patch present from birth, often with coarse hair growing through it.",
     wrong=[("Malignant melanoma", "That is an acquired, asymmetric, changing lesion, not a birthmark of this size."),
            ("Nevus flammeus", "That is vascular and red-purple, not brown."),
            ("Common acquired melanocytic naevus", "Those appear in childhood and stay a few millimetres across.")]),

# --------------------------------------- premalignant and malignant lesions ----
dict(cond="Actinic keratosis", img="l9_s008_2.jpg", slide=8, deck=D9, io=MAL,
     alt="Back of a sun-damaged hand with multiple rough scaly red papules",
     why="Rough, scaly, gritty papules on sun-damaged skin — easier to FEEL than to see, and premalignant.",
     wrong=[("Seborrheic keratosis", "Those are waxy and stuck-on, and they are not gritty."),
            ("Squamous cell carcinoma", "That is a thicker, firmer nodule, often ulcerated — the next step along."),
            ("Solar lentigo", "That is a flat brown macule with no roughness at all.")]),

dict(cond="Squamous cell carcinoma", img="l9_s019_1.jpg", slide=19, deck=D9, io=MAL,
     alt="Skin with a firm raised nodule carrying a thick keratotic crust",
     why="A firm nodule with heaped KERATIN or ulceration, on chronically sun-damaged skin.",
     wrong=[("Basal cell carcinoma — nodular", "That is PEARLY with a rolled translucent border and surface telangiectasia."),
            ("Actinic keratosis", "That is a thin gritty scale, not a thick nodule."),
            ("Keratoacanthoma", "That is symmetrical with a clean central keratin crater and grows over weeks.")]),

dict(cond="Basal cell carcinoma — nodular", img="l9_s029_1.jpg", slide=29, deck=D9, io=MAL,
     alt="Skin with a translucent pearly nodule, a rolled border and fine surface vessels",
     why="A PEARLY, translucent nodule with a ROLLED border and telangiectasia running over the surface.",
     wrong=[("Squamous cell carcinoma", "That is keratotic or ulcerated, and it is opaque rather than pearly."),
            ("Sebaceous hyperplasia", "That is yellow and umbilicated, with a ring of lobules."),
            ("Epidermoid cyst", "That is a soft mobile dome with a punctum and normal overlying skin.")]),

dict(cond="Malignant melanoma", img="l9_s044_2.jpg", slide=44, deck=D9, io=MAL,
     alt="Sole of the foot with an asymmetric brown-black macule with ragged edges",
     why="Asymmetric, irregularly bordered and unevenly coloured — and on the sole, which demands more suspicion.",
     wrong=[("Common acquired melanocytic naevus", "That is small, round, evenly coloured and symmetrical."),
            ("Seborrheic keratosis", "That is waxy and stuck-on with a uniform surface."),
            ("Tungiasis", "That is a nodule with a single black punctum, from a burrowed flea.")]),

dict(cond="Nail unit melanoma", img="l9_s045_1.jpg", slide=45, deck=D9, io=MAL,
     alt="Thumb nail with a wide dark brown band running the length of the plate",
     why="A pigmented BAND running the length of the nail — widening, or spilling onto the fold, means biopsy.",
     wrong=[("Onychomycosis", "That thickens and crumbles the nail yellow-brown; it does not draw a longitudinal band."),
            ("Chronic paronychia", "That inflames the fold and ridges the nail without pigment."),
            ("Glomus tumour", "That is exquisitely painful with cold, and shows a small red-blue spot.")]),

dict(cond="Kaposi sarcoma", img="l9_s062_4.jpg", slide=62, deck=D9, io=MAL,
     alt="Roof of the mouth covered with confluent violaceous nodular plaques",
     why="Violaceous nodular plaques, here filling the PALATE — a vascular tumour tied to immunosuppression.",
     wrong=[("Malignant melanoma", "Oral melanoma is rare and would be a discrete pigmented lesion, not confluent purple plaques."),
            ("Pyogenic granuloma", "That is a solitary friable nodule that bleeds."),
            ("Cherry angioma", "Those are small bright red papules on the trunk, not the mouth.")]),
]
