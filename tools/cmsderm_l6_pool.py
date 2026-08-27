# -*- coding: utf-8 -*-
"""Cutaneous Viral and Fungal Infections -- pool for the Updated CMS derm master exams."""
DECK = "6. Fungal and Viral Skin Infections - Jaquith.pptx"
IO_A = "a — Interpret a potassium hydroxide (KOH) preparation and recognize fungal elements"
IO_B = ("b — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
        "differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, "
        "and prognosis of cutaneous viral and fungal infections")
IO_C = ("c — Identify medical care strategies for cutaneous viral and fungal infections for infant, child, "
        "adolescent, adult and elderly populations")

def Q(topic, q, opts, c, slide, io=IO_B):
    return {"topic": topic, "io": io, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Antifungal classes",
  "A clinician wants an antifungal that works by destroying the fungal cell membrane rather than by blocking "
  "ergosterol synthesis. Which agent belongs to that class, and how is the class recognised by name?",
  [["Terbinafine, an allylamine, recognisable by the ending -fine",
    "Correct. The allylamine class works by destroying the cell membranes of fungi, preventing growth and ultimately "
    "killing them, and its members end in -fine: terbinafine and naftifine. Imidazoles instead block synthesis of "
    "ergosterol, a vital component of the fungal cell membrane."],
   ["Ketoconazole, an imidazole, recognisable by the ending -fine",
    "Ketoconazole is an imidazole, and imidazoles block ergosterol synthesis rather than destroying the membrane "
    "directly. The naming clue also belongs to the allylamines."],
   ["Terbinafine, an imidazole, recognisable by the ending -azole",
    "Terbinafine is correctly chosen but wrongly classified. It is an allylamine, and the -azole ending identifies "
    "the imidazoles instead."],
   ["Nystatin, a polyene that treats both Candida and dermatophytes",
    "Topical nystatin treats Candida only, which is precisely why topical azoles are preferred when a dermatophyte "
    "may also be present."],
   ["Griseofulvin, an allylamine favoured for Trichophyton infection",
    "Griseofulvin is often favoured for Microsporum infection in tinea capitis, whereas terbinafine is generally "
    "favoured for Trichophyton. Griseofulvin is not an allylamine."]],
  0, 5),

Q("Dermatophytes",
  "A student asks why dermatophyte infections never involve the mouth. What is the correct explanation?",
  [["Dermatophytes infect and survive only on dead keratin, so they cannot survive on mucous membranes",
    "Correct. Dermatophytes infect and survive only on dead keratin, involving the superficial portion of the skin at "
    "the stratum corneum, plus hair and nails. They cannot survive on mucous membranes."],
   ["Dermatophytes are killed by salivary enzymes but survive elsewhere",
    "The limitation is the absence of dead keratin rather than an antimicrobial property of saliva. Candida, which is "
    "not a dermatophyte, colonises mucosa freely."],
   ["Dermatophytes require sebum, which mucous membranes do not produce",
    "Sebum matters in tinea capitis, where post-pubertal changes in sebum fatty acid content are believed to inhibit "
    "dermatophyte growth. But the organisms depend on keratin rather than requiring sebum."],
   ["Dermatophytes are obligate intracellular organisms confined to keratinocyte nuclei",
    "Dermatophytes are not intracellular organisms. They live within keratinised tissue rather than inside cells."],
   ["Dermatophytes can involve mucous membranes when the patient is immunocompromised",
    "The constraint is structural rather than immunological. Immunosuppression extends the severity and extent of "
    "dermatophytosis but does not create keratin where there is none."]],
  0, 6),

Q("Tinea capitis",
  "A 7-year-old boy has scaly patches on the scalp with areas of hair loss and visible black dots where hairs have "
  "fractured. A potassium hydroxide preparation confirms fungal elements. His mother asks whether a medicated cream "
  "will be enough. What is the correct response?",
  [["Oral therapy is required, because topical agents alone do not penetrate the infected hair shaft",
    "Correct. Tinea capitis requires oral therapy; topical agents alone do not penetrate the infected hair shaft. "
    "Antifungal shampoo reduces viable spore shedding but does not replace oral treatment."],
   ["A topical antifungal cream applied to the lesion and 1 to 2 cm beyond will clear it",
    "That instruction belongs to localised tinea corporis. The scalp differs because the organism resides within the "
    "hair shaft, where topical agents cannot reach."],
   ["An antifungal shampoo used two to three times weekly is sufficient on its own",
    "Selenium sulfide or ketoconazole shampoo reduces viable spore shedding and is a useful adjunct during early "
    "systemic treatment, but it explicitly does not replace oral therapy."],
   ["A topical corticosteroid should be used first to settle the inflammation",
    "Topical steroids applied to a dermatophyte infection produce tinea incognito, in which the appearance is "
    "clinically altered and the lesion flares whenever the steroid is stopped."],
   ["No treatment is needed because tinea capitis resolves spontaneously after puberty",
    "Changes in sebum fatty acid content after puberty are believed to inhibit dermatophyte growth, but waiting years "
    "in an infected 7-year-old leaves an active, transmissible infection with a risk of scarring alopecia."]],
  0, 15),

Q("Tinea capitis",
  "In tinea capitis, which oral agent is generally favoured for Trichophyton infection, and which for Microsporum?",
  [["Terbinafine for Trichophyton and griseofulvin for Microsporum",
    "Correct. Terbinafine is generally favoured for Trichophyton infection and griseofulvin is often favoured for "
    "Microsporum infection, which is why identifying the organism by culture matters before prolonged systemic "
    "therapy."],
   ["Griseofulvin for Trichophyton and terbinafine for Microsporum",
    "The two are reversed. Because the pairing determines the drug choice, getting it backwards means selecting the "
    "less effective agent for the organism actually present."],
   ["Terbinafine for both organisms",
    "Terbinafine is favoured for Trichophyton but griseofulvin is often preferred for Microsporum, so a single agent "
    "for both discards the species-specific preference."],
   ["Fluconazole for both organisms",
    "Fluconazole and itraconazole appear as alternatives in other dermatophyte infections, but they are not the two "
    "agents paired with these organisms in tinea capitis."],
   ["Topical ketoconazole for both organisms",
    "Ketoconazole 2 percent shampoo is an adjunct that reduces spore shedding. Topical therapy of any kind does not "
    "penetrate the infected hair shaft."]],
  0, 15),

Q("Tinea capitis",
  "A Wood's lamp examination is performed on a child with suspected tinea capitis and shows no fluorescence. What is "
  "the correct interpretation?",
  [["A negative Wood's lamp does not exclude the diagnosis, because Trichophyton tonsurans usually does not "
    "fluoresce",
    "Correct. A Wood lamp may rapidly support Microsporum infection, but Trichophyton tonsurans — the most common "
    "species — usually does not fluoresce. Confirmation rests on potassium hydroxide microscopy and fungal culture."],
   ["A negative Wood's lamp excludes tinea capitis",
    "Relying on a negative Wood's lamp to exclude the diagnosis would miss most cases, since the commonest causative "
    "species does not fluoresce."],
   ["A negative Wood's lamp indicates a bacterial rather than fungal cause",
    "Coral-red fluorescence under a Wood's lamp identifies erythrasma, a bacterial infection. Absence of fluorescence "
    "says nothing about a bacterial cause on the scalp."],
   ["A negative Wood's lamp means oral therapy can be avoided",
    "The route of therapy is determined by the site rather than by fluorescence. Scalp infection requires oral "
    "therapy because topical agents do not reach the hair shaft."],
   ["A negative Wood's lamp confirms Microsporum infection",
    "Microsporum is the species a Wood lamp can support, so a negative result argues against it rather than "
    "confirming it."]],
  0, 14),

Q("Tinea corporis",
  "A 26-year-old woman has two round, sharply circumscribed, slightly erythematous scaly plaques on the forearm, each "
  "with an advancing scaly border and a clearer centre. Where should the specimen for potassium hydroxide microscopy "
  "be taken from?",
  [["The active advancing border of the lesion",
    "Correct. The potassium hydroxide specimen is taken from the active border, where the viable organism is "
    "concentrated. Culture is added for high clinical suspicion when the potassium hydroxide preparation is "
    "negative."],
   ["The centre of the lesion, where the change began",
    "The centre has cleared, which means the organism has moved outward. Sampling there yields the lowest density of "
    "fungal elements and produces false negatives."],
   ["Normal skin adjacent to the lesion",
    "Uninvolved skin contains no organism. Perilesional sampling belongs to direct immunofluorescence in autoimmune "
    "blistering disease, not to fungal microscopy."],
   ["A plucked hair from within the plaque",
    "A plucked hair is used for potassium hydroxide microscopy when dermatophyte folliculitis is suspected. This is a "
    "glabrous skin lesion with an advancing scaly edge."],
   ["A nail clipping from the same limb",
    "Nail clippings with periodic acid-Schiff stain evaluate onychomycosis. They do not sample a body lesion."]],
  0, 26),

Q("Tinea corporis",
  "A clinician is distinguishing tinea corporis from nummular eczema, both of which present as red, itchy, circular "
  "patches. What is the distinguishing feature?",
  [["Tinea corporis has an annular appearance with central clearing, whereas nummular eczema is coin-shaped without "
    "central clearing",
    "Correct. Both present as red or pink itchy circular patches. Tinea corporis is a fungal infection with an "
    "annular appearance, whereas nummular eczema is non-infectious and coin-shaped without central clearing."],
   ["Nummular eczema has an annular appearance with central clearing and tinea corporis does not",
    "The two are reversed. A clinician using this rule would treat a dermatophyte infection with a corticosteroid and "
    "produce tinea incognito."],
   ["Only tinea corporis is pruritic",
    "Nummular eczema is intensely pruritic and tinea corporis may be asymptomatic or pruritic. Itch does not separate "
    "them."],
   ["Only nummular eczema occurs on the extremities",
    "Nummular eczema favours the extremities but tinea corporis occurs there freely. Site does not decide."],
   ["Only tinea corporis is well demarcated",
    "Both are well demarcated — nummular eczema is described as well-demarcated and tinea corporis as sharply "
    "circumscribed."]],
  0, 27),

Q("Tinea cruris",
  "A 34-year-old man has an itchy, sharply demarcated plaque on the proximal medial thigh extending from the crural "
  "fold. The scrotum is not involved. He also has scaling between his toes. What does the scrotal sparing indicate?",
  [["It supports tinea cruris, since scrotal involvement would suggest candidal intertrigo instead",
    "Correct. In tinea cruris the scrotum is typically spared, and scrotal involvement suggests candidal intertrigo, "
    "which commonly involves the scrotum. His coexisting tinea pedis fits, since the two often occur together."],
   ["It argues against tinea cruris and toward a dermatophyte-negative process",
    "Sparing of the scrotum is characteristic of tinea cruris rather than evidence against it, so this inverts the "
    "finding's meaning."],
   ["It indicates erythrasma rather than a dermatophyte infection",
    "Erythrasma involves the inner thighs, crural region, and scrotum and fluoresces coral-red under a Wood's lamp. "
    "Scrotal involvement is typical of erythrasma rather than excluded by it."],
   ["It indicates inverse psoriasis",
    "Inverse psoriasis affects flexural sites but is not distinguished by scrotal sparing, and psoriasis is "
    "characterised by well-demarcated plaques with silver scale rather than an advancing fungal border."],
   ["It has no diagnostic significance",
    "The distribution is precisely what separates the two commonest groin diagnoses, so discarding it removes the "
    "most useful bedside discriminator."]],
  0, 33),

Q("Tinea pedis",
  "A 42-year-old man has maceration and erythematous erosions between the third and fourth toes with associated "
  "fissuring. What form of tinea pedis is this, and is it the commonest?",
  [["Interdigital tinea pedis, which is the most common form",
    "Correct. Interdigital tinea pedis is the most common form, caused by Trichophyton species, producing maceration "
    "and erythematous erosions or scales between the toes, especially in the third and fourth interspaces, with "
    "associated fissures."],
   ["Hyperkeratotic tinea pedis, which is the most common form",
    "Hyperkeratotic disease produces plantar erythema with scaling to diffuse thickening involving the soles and the "
    "medial and lateral surfaces in a shoe-like distribution. It is a different pattern and not the commonest."],
   ["Vesiculobullous tinea pedis, which is the most common form",
    "The vesiculobullous form is the moist acute variant with a vesicular or bullous eruption on underlying erythema. "
    "It is pruritic and painful rather than macerated and eroded."],
   ["Interdigital tinea pedis, which is the least common form",
    "The classification is right but the frequency is wrong. Naming it the least common would misdirect the index of "
    "suspicion for the presentation clinicians see most often."],
   ["Candidal intertrigo of the toe webs",
    "Candidiasis and mixed toe web infection are on the differential, and bacterial studies are added for marked "
    "maceration, malodour, or drainage. But the described pattern is the classic dermatophyte presentation."]],
  0, 39),

Q("Tinea pedis",
  "What patient education point for tinea pedis is described as essential?",
  [["Drying between the toes after bathing",
    "Correct. Drying between the toes after bathing is marked as essential, alongside antifungal foot powder for "
    "shoes, wearing open-toed sandals when possible, using sandals in community showers, and changing socks "
    "frequently."],
   ["Wearing occlusive footwear to protect the skin",
    "Occlusion traps the warmth and moisture dermatophytes need. Open-toed sandals are recommended where possible."],
   ["Soaking the feet daily in warm water",
    "Prolonged moisture is the predisposing condition rather than a treatment. Moisture control is a core part of "
    "management."],
   ["Sharing antifungal foot powder with household members",
    "Antifungal foot powder is used in the patient's own shoes. Sharing personal items is discouraged in dermatophyte "
    "infections generally."],
   ["Walking barefoot in community showers to allow air drying",
    "Sandals should be used in community showers, since the infection spreads by contact with infected desquamated "
    "skin."]],
  0, 45),

Q("Onychomycosis",
  "A 60-year-old man with diabetes has three thickened, discoloured, crumbling toenails with distal onycholysis. He "
  "asks for oral terbinafine. What must be done first?",
  [["Confirm fungal infection before oral therapy, because many dystrophic nails are not fungal",
    "Correct. Fungus must be confirmed before oral therapy, since many dystrophic nails are not fungal. Testing "
    "options include potassium hydroxide microscopy, periodic acid-Schiff stain of nail clippings, fungal culture, or "
    "polymerase chain reaction, sampling the most proximal accessible diseased nail bed."],
   ["Start terbinafine empirically, since dermatophytes cause most cases",
    "Dermatophytes, especially Trichophyton rubrum, do cause most cases, which makes empiric treatment tempting. But "
    "confirming first avoids months of hepatically monitored therapy for a nail that was never fungal."],
   ["Obtain a Wood's lamp examination of the nails",
    "A Wood lamp evaluates pigment change in selected fungal and bacterial infections and may support Microsporum "
    "scalp infection. It is not the confirmatory test for nail disease."],
   ["Begin topical antifungal therapy, which is adequate for most nail infections",
    "Topical therapy is inadequate for most nail infections, which is why the question of oral therapy arises at all."],
   ["Remove the affected nails surgically before medical therapy",
    "Nail avulsion is not the described first step. Confirming the diagnosis governs whether systemic therapy is "
    "justified."]],
  0, 51),

Q("Onychomycosis",
  "What is the usual duration of first-line oral terbinafine for fingernail and toenail onychomycosis, and what "
  "safety review is required?",
  [["Six weeks for fingernails and twelve weeks for toenails, with review of hepatic disease and interactions and "
    "baseline liver tests per labelling and patient risk",
    "Correct. Oral terbinafine is first-line for most dermatophyte nail disease, usually 6 weeks for fingernails and "
    "12 weeks for toenails, with hepatic disease and interactions reviewed and baseline liver tests obtained per "
    "labelling and patient risk."],
   ["Twelve weeks for fingernails and six weeks for toenails, with baseline liver tests",
    "The two durations are swapped. Toenails grow more slowly and require the longer course, so reversing them "
    "under-treats the site that needs more time."],
   ["Two weeks for both, with no laboratory monitoring",
    "A two-week course is far too short for nail disease, and omitting the hepatic review discards the principal "
    "safety consideration for terbinafine."],
   ["Six weeks for both, with baseline renal function testing",
    "The duration differs between fingernails and toenails, and the safety review for terbinafine is hepatic rather "
    "than renal."],
   ["Lifelong therapy, since onychomycosis cannot be cured",
    "Defined courses are given, and itraconazole is available as an alternative. Indefinite systemic antifungal "
    "therapy is not the approach."]],
  0, 52),

Q("Id reaction",
  "A 30-year-old man develops an extremely pruritic papulovesicular eruption on the fingers ten days after being "
  "diagnosed with tinea pedis. A potassium hydroxide preparation from the finger lesions is negative, while one from "
  "the toe webs is positive. What three criteria establish this diagnosis?",
  [["A dermatophyte infection elsewhere on the body, absence of fungal elements at the eruption site, and resolution "
    "after the primary infection is treated",
    "Correct. Those are the three criteria for establishing an id reaction. The primary site is potassium hydroxide "
    "positive and the distant id site is potassium hydroxide negative, and the eruption occurs 1 to 2 weeks after the "
    "primary infection."],
   ["A dermatophyte infection elsewhere, fungal elements present at the eruption site, and resolution after "
    "treatment",
    "The second criterion is inverted, and it is the decisive one: fungal elements must be absent from the id site. "
    "Their presence would mean the eruption is a second focus of infection rather than a reaction to a distant one."],
   ["A positive bacterial culture, absence of fungal elements, and response to antibiotics",
    "An id reaction is an inflammatory response to a dermatophyte rather than a bacterial process, and it resolves "
    "when the fungal infection is treated."],
   ["A positive Wood's lamp at the primary site, negative potassium hydroxide at the distant site, and biopsy "
    "confirmation",
    "Wood's lamp fluorescence and biopsy are not among the criteria, and the primary site is confirmed by potassium "
    "hydroxide microscopy."],
   ["Symmetric distribution, absence of pruritus, and spontaneous resolution without treatment",
    "The eruption is described as extremely pruritic, and resolution follows treatment of the primary dermatophyte "
    "infection."]],
  0, 62),

Q("Tinea incognito",
  "A patient has an expanding annular eruption whose appearance has become atypical and which flares every time a "
  "topical steroid is stopped. What has occurred, and what is the first management step?",
  [["Tinea incognito from inappropriate topical corticosteroid use; stop the corticosteroid",
    "Correct. Tinea incognito is tinea with a clinically altered appearance due to inappropriate treatment, usually "
    "topical steroids. Management begins by stopping the inappropriate corticosteroid or calcineurin inhibitor, then "
    "obtaining potassium hydroxide microscopy or culture from an active edge."],
   ["Tinea incognito; increase the potency of the topical corticosteroid",
    "This is the exact cycle described in the lecture — the lesion flares, more steroid is applied, and the "
    "appearance is further altered. Escalating potency deepens the problem."],
   ["Allergic contact dermatitis to the corticosteroid vehicle; patch test before any further treatment",
    "Contact allergy to a topical is possible in general, but the expanding annular morphology and the flare-on-"
    "withdrawal pattern point to a suppressed dermatophyte infection."],
   ["Steroid-induced atrophy; apply an emollient and observe",
    "Atrophy, striae, and telangiectasia follow prolonged steroid use, but they do not produce an expanding annular "
    "lesion that flares when treatment stops."],
   ["Psoriasis unmasked by steroid withdrawal; begin calcipotriene",
    "Systemic steroid withdrawal can precipitate pustular psoriasis, but that is an abrupt febrile eruption of "
    "pustules rather than a single altered annular plaque."]],
  0, 65),

Q("Cutaneous candidiasis",
  "A 61-year-old woman with obesity has a well-demarcated erythematous patch in the inframammary fold with several "
  "small papules and pustules on adjacent skin just beyond the main area of redness. What finding identifies the "
  "organism, and what topical choice covers both possibilities?",
  [["Satellite lesions identify Candida, and a topical azole covers both Candida and dermatophytes",
    "Correct. Satellite papules and pustules accompany the well-demarcated erythematous patches of candidal "
    "intertrigo. Topical nystatin treats Candida only, whereas topical azoles treat both Candida and dermatophytes."],
   ["Satellite lesions identify Candida, and topical nystatin covers both Candida and dermatophytes",
    "The finding is right but the drug choice is wrong in the way that matters. Nystatin treats Candida only, so if a "
    "dermatophyte is also present it will be left untreated."],
   ["Central clearing identifies Candida, and topical terbinafine covers both organisms",
    "Central clearing is the annular pattern of tinea rather than a candidal feature, and terbinafine is an "
    "allylamine aimed at dermatophytes."],
   ["Coral-red fluorescence identifies Candida, and topical erythromycin is used",
    "Coral-red fluorescence identifies erythrasma caused by Corynebacterium minutissimum, which is treated with "
    "topical erythromycin or clindamycin."],
   ["Honey-coloured crusting identifies Candida, and topical mupirocin is used",
    "Honey-coloured crust is impetigo, a bacterial infection treated with mupirocin."]],
  0, 72),

Q("Cutaneous candidiasis",
  "Beyond antifungal therapy, what environmental measure is central to treating candidal intertrigo?",
  [["Gently drying the folds, reducing friction and occlusion, using moisture-wicking or absorbent material, and "
    "addressing incontinence or hyperhidrosis",
    "Correct. Correcting the environment is central: gently dry the folds, reduce friction and occlusion, use "
    "moisture-wicking fabric or absorbent material, and address incontinence or hyperhidrosis. Intertrigo itself is "
    "caused by friction, moisture, and heat trapped in body folds."],
   ["Applying an occlusive ointment to the folds to protect the skin",
    "Occlusion traps the moisture and heat that produce intertrigo in the first place. Occlusive barriers are the "
    "approach to diaper dermatitis, where the exposure is urine and stool rather than trapped moisture."],
   ["Increasing the frequency of hot showers to keep the area clean",
    "Hot water and prolonged wetting worsen maceration in the folds. Gentle drying is what is required."],
   ["Applying a high-potency topical corticosteroid to the folds",
    "Potent steroids in occluded flexural skin cause atrophy and striae rapidly and can allow candidal overgrowth to "
    "extend."],
   ["Binding the folds tightly to prevent skin-on-skin contact",
    "Tight binding increases friction and occlusion, both of which are among the causes to be reduced."]],
  0, 72),

Q("Pityriasis versicolor",
  "A 19-year-old presents in summer with numerous well-defined hypopigmented macules over the upper back and "
  "shoulders that do not tan. Scraping the surface reveals fine scale. What does potassium hydroxide microscopy show?",
  [["Short hyphae with clusters of yeast, described as spaghetti and meatballs",
    "Correct. Potassium hydroxide microscopy in pityriasis versicolor shows short hyphae with clusters of yeast, "
    "classically described as spaghetti and meatballs. The condition is caused by overgrowth of lipid-dependent "
    "Malassezia species that normally inhabit the skin."],
   ["Long septate branching hyphae without yeast forms",
    "Long septate branching hyphae are the dermatophyte pattern seen in tinea corporis and other tinea infections. "
    "Pityriasis versicolor is caused by a yeast rather than a dermatophyte."],
   ["Budding yeast with pseudohyphae only",
    "Budding yeast and pseudohyphae support candidal infection, which is what a potassium hydroxide preparation looks "
    "for in candidal diaper dermatitis or intertrigo."],
   ["Mites, eggs, and fecal pellets",
    "Those are the findings of a mineral oil preparation in scabies, which is a mite infestation rather than a fungal "
    "one."],
   ["No organisms, since the diagnosis is made only by biopsy",
    "Biopsy is rarely needed. The diagnosis is usually clinical, supported by scraping or stretching the lesion to "
    "reveal fine scale and by the characteristic potassium hydroxide appearance."]],
  0, 80),

Q("Pityriasis versicolor",
  "A patient treated for pityriasis versicolor returns two months later frustrated that the pale patches persist "
  "despite completing therapy. What is the most accurate explanation?",
  [["Hypopigmentation reflects altered melanocyte function and reduced tanning, and recovery can lag months after the "
    "yeast has cleared",
    "Correct. Hypopigmentation reflects altered melanocyte function and reduced tanning, and recovery can lag months "
    "after yeast clearance. The persistence of pallor does not indicate treatment failure."],
   ["The persistence of pale patches indicates treatment failure requiring oral therapy",
    "Systemic therapy is reserved for extensive, recurrent, or topical-refractory disease. Treating persistent "
    "pigment change as failure exposes the patient to unnecessary systemic antifungal therapy."],
   ["The pale patches indicate vitiligo developing at the treated sites",
    "Vitiligo is on the differential and produces complete depigmentation without scale. Pityriasis versicolor "
    "produces partial pigment change that recovers over months."],
   ["The condition has become contagious and household members require treatment",
    "Pityriasis versicolor is not considered contagious, since it results from overgrowth of an organism that "
    "normally inhabits the skin."],
   ["The pale patches indicate a secondary bacterial infection",
    "There is no bacterial component. The pigment change is a consequence of altered melanocyte function from the "
    "yeast overgrowth."]],
  0, 77),

Q("Varicella",
  "A 6-year-old unvaccinated child has a generalised pruritic eruption concentrated on the trunk, scalp, and face. "
  "Macules, papules, vesicles, and crusts are all present at the same time. What feature is most characteristic?",
  [["Lesions in multiple stages of healing appearing simultaneously",
    "Correct. Primary varicella-zoster virus infection causes a generalised pruritic eruption in multiple stages of "
    "healing — macules progress to papules, vesicles, and crusts, with several stages appearing simultaneously."],
   ["Lesions all at the same stage of evolution",
    "Uniform staging is what distinguishes other vesicular eruptions from varicella. Simultaneous multiple stages is "
    "the defining feature here."],
   ["Lesions confined to a single dermatome",
    "Dermatomal confinement that abruptly stops at the midline describes herpes zoster, the reactivation of latent "
    "virus, rather than primary varicella."],
   ["Lesions limited to the palms and soles",
    "Varicella lesions concentrate on the trunk, scalp, and face. Palm and sole involvement points elsewhere."],
   ["Lesions with honey-coloured crusting around the nose and mouth",
    "Honey-coloured perioral crusting is impetigo, a superficial bacterial infection."]],
  0, 84),

Q("Varicella",
  "For how long is a child with varicella considered contagious?",
  [["From 1 to 2 days before the rash until all lesions have crusted",
    "Correct. Patients are contagious from 1 to 2 days before the rash appears until all lesions crust. In "
    "breakthrough disease without crusts, the period runs until no new lesions have appeared for 24 hours."],
   ["From the appearance of the rash until all lesions have crusted",
    "This omits the 1 to 2 days of contagiousness before the rash, which is exactly the window in which unrecognised "
    "transmission occurs."],
   ["Only while vesicles are present, ending once any crusting begins",
    "Contagion continues until all lesions have crusted rather than until crusting begins in some."],
   ["For 21 days from exposure regardless of the rash",
    "Twenty-one days describes the incubation window for monitoring an exposed contact rather than the infectious "
    "period of a case."],
   ["Until fever resolves, regardless of the state of the lesions",
    "The lesions rather than the temperature define the infectious period."]],
  0, 89),

Q("Herpes zoster",
  "A 68-year-old woman describes three days of burning pain in a band across her left flank, followed by an eruption. "
  "Examination shows grouped vesicles on an erythematous base confined to a single band that stops abruptly at the "
  "midline. What are the three clinical phases of this condition?",
  [["A pre-eruptive phase with dermatomal dysesthesia or pain, an acute eruptive phase, and a chronic phase of "
    "postherpetic neuralgia",
    "Correct. The pre-eruptive phase is characterised by dysesthesia or pain within the affected dermatome with "
    "lesion onset by 48 to 72 hours; the acute eruptive phase produces grouped herpetiform vesicles on an "
    "erythematous base with new lesions forming over 3 to 5 days; and postherpetic neuralgia is the chronic phase."],
   ["A prodromal fever, a generalised eruptive phase, and a desquamative phase",
    "Generalised eruption and desquamation describe other conditions. Herpes zoster is characteristically "
    "dermatomal, and its hallmark is that it does not cross the midline."],
   ["An incubation phase, a contagious phase, and a latency phase",
    "Latency is part of the pathophysiology — the virus remains latent in cranial nerve or dorsal root ganglia — but "
    "it is not one of the three clinical phases of the disease episode."],
   ["A pre-eruptive phase, an eruptive phase, and a scarring phase",
    "Vesicles may eventually scar if inflammation is intense, but scarring is a possible outcome rather than a named "
    "clinical phase. The recognised third phase is postherpetic neuralgia."],
   ["An erythematous phase, a bullous phase, and a necrotic phase",
    "Vesicles may coalesce to form bullae, but this sequence does not match the three phases described."]],
  0, 97),

Q("Herpes zoster",
  "What is the single most characteristic distributional feature of herpes zoster?",
  [["It is confined to one or two adjacent sensory nerve distributions and stops abruptly at the midline without "
    "crossing it",
    "Correct. Blisters are confined to the cutaneous distribution of one or two adjacent sensory nerves and abruptly "
    "stop at the midline. Thoracic dermatomes are most frequently involved at about 55 percent, followed by cranial "
    "at about 20 percent."],
   ["It crosses the midline symmetrically in a bilateral band",
    "This is the direct inversion of the defining feature. A bilateral symmetric eruption should prompt a different "
    "diagnosis entirely."],
   ["It is generalised over the trunk, scalp, and face",
    "That distribution describes primary varicella rather than reactivation, and varicella shows multiple stages "
    "simultaneously."],
   ["It follows the lines of skin cleavage in a Christmas tree pattern",
    "The Christmas tree pattern following cleavage lines describes pityriasis rosea, which follows a herald patch."],
   ["It is confined to intertriginous folds",
    "Flexural and intertriginous distribution suggests candidal intertrigo, erythrasma, or inverse psoriasis rather "
    "than a dermatomal viral reactivation."]],
  0, 100),

Q("Herpes zoster",
  "A 72-year-old man presents with vesicles in the right ophthalmic division distribution, including lesions on the "
  "tip of his nose. What does that finding signify, and what should be done?",
  [["Hutchinson sign, which increases ocular risk; start systemic antiviral therapy immediately, though its absence "
    "does not exclude eye involvement",
    "Correct. Herpes zoster ophthalmicus involves the ophthalmic division of the trigeminal nerve. Hutchinson sign — "
    "lesions on the tip or side of the nose — increases ocular risk, but its absence does not exclude eye "
    "involvement, and systemic antiviral therapy should be started immediately."],
   ["Hutchinson sign, whose absence would reliably exclude ocular involvement",
    "The sign's presence raises risk but its absence specifically does not exclude eye involvement. Relying on a "
    "negative sign to skip ophthalmological assessment is the error this caveat exists to prevent."],
   ["Ramsay Hunt syndrome, requiring antiviral therapy plus corticosteroid",
    "Ramsay Hunt syndrome is herpes zoster oticus — peripheral facial palsy with painful vesicles of the ear canal, "
    "auricle, or oropharynx, sometimes with hearing loss, tinnitus, or vertigo. The nose is not its territory."],
   ["Zoster sine herpete, requiring no antiviral therapy",
    "Zoster sine herpete is pain without a vesicular eruption. This patient has visible vesicles."],
   ["Disseminated zoster, requiring airborne isolation only",
    "Dissemination is defined by lesions beyond the affected and adjacent dermatomes. Antiviral therapy is required "
    "regardless, and isolation alone would leave the eye untreated."]],
  0, 103),

Q("Herpes zoster",
  "Within what window should antiviral therapy for herpes zoster ideally be started, and when should it still be "
  "given beyond that window?",
  [["Ideally within 72 hours of rash onset, and still given after 72 hours when new lesions are forming or the "
    "ophthalmic division is involved",
    "Correct. Antivirals should be started as soon as possible, ideally within 72 hours of rash onset, and treatment "
    "is still given after 72 hours when new lesions are forming or there is ophthalmic involvement."],
   ["Ideally within 72 hours, with no benefit and no indication beyond that point",
    "This is the closest wrong answer because the 72-hour target is correct. But refusing treatment beyond it would "
    "deny antivirals to patients with active new lesion formation or ophthalmic disease, who still benefit."],
   ["Within 7 days of rash onset, with no exceptions",
    "The stated target is 72 hours. Waiting a week loses the window in which antivirals most reduce acute severity."],
   ["Only after polymerase chain reaction confirmation, whenever that returns",
    "Typical unilateral dermatomal vesicles are diagnosed clinically, and polymerase chain reaction is reserved for "
    "atypical, disseminated, vaccine-modified, or immunocompromised presentations. Waiting for it forfeits the "
    "treatment window."],
   ["Only if postherpetic neuralgia has already developed",
    "Postherpetic neuralgia is the chronic complication defined as pain persisting at least 90 days after rash onset. "
    "Antivirals are an acute-phase treatment."]],
  0, 106),

Q("Postherpetic neuralgia",
  "How is postherpetic neuralgia defined, and what are the first-line treatments?",
  [["Pain persisting at least 90 days after rash onset, treated first with gabapentin or pregabalin, an appropriate "
    "tricyclic antidepressant, or topical lidocaine",
    "Correct. Pain persisting 90 days or more after rash onset is the commonly used definition. First-line treatment "
    "is gabapentin or pregabalin, an appropriate tricyclic antidepressant, or topical lidocaine, with a capsaicin "
    "patch as a further option."],
   ["Pain persisting at least 90 days after rash onset, treated first with long-term opioids",
    "The definition is right but routine long-term opioid therapy is specifically to be avoided, and it carries "
    "dependence and falls risk in the elderly patients most affected."],
   ["Pain persisting at least 7 days after rash onset, treated with antivirals",
    "Seven days is far too short a threshold, and antivirals are acute-phase therapy rather than treatment for "
    "established neuropathic pain."],
   ["Pain persisting at least 30 days after rash onset, treated with systemic corticosteroids",
    "The interval is wrong and corticosteroids are not among the first-line agents for this neuropathic pain."],
   ["Any pain during the acute eruptive phase, treated with acetaminophen",
    "Almost all patients have pain during the acute eruptive phase, and acetaminophen or a non-steroidal agent is "
    "used for mild acute pain. That is not postherpetic neuralgia, which is defined by persistence."]],
  0, 109),
]

QUESTIONS += [

Q("Shingrix",
  "Who should receive the recombinant zoster vaccine, and at what interval?",
  [["Two doses for immunocompetent adults aged 50 and over, and two doses for adults aged 19 and over who are or "
    "will be immunodeficient or immunosuppressed, at a standard interval of 2 to 6 months",
    "Correct. Two doses of recombinant zoster vaccine are given to immunocompetent adults aged 50 years and over, and "
    "two doses to adults aged 19 and over who are or will be immunodeficient or immunosuppressed, with a standard "
    "interval of 2 to 6 months."],
   ["A single dose for immunocompetent adults aged 50 and over",
    "The vaccine is a two-dose series. A single dose leaves the schedule incomplete and the patient inadequately "
    "protected."],
   ["Two doses for immunocompetent adults aged 65 and over only",
    "The age threshold for immunocompetent adults is 50 rather than 65, and restricting it to 65 would leave a "
    "fifteen-year band of eligible adults unvaccinated."],
   ["Two doses only for adults who have already had an episode of herpes zoster",
    "Prior zoster is not the eligibility criterion. Vaccination is recommended by age and by immune status."],
   ["Two doses for children as part of the routine childhood schedule",
    "The two-dose varicella vaccine is what is given in childhood to prevent primary infection. Recombinant zoster "
    "vaccine is for adults to prevent reactivation."]],
  0, 110, IO_C),

Q("Herpes zoster",
  "A patient with herpes zoster asks whether her grandson can catch shingles from her. What is the most accurate "
  "explanation?",
  [["A susceptible contact does not catch shingles, but exposure to vesicular fluid can transmit varicella-zoster "
    "virus and cause chickenpox",
    "Correct. A susceptible contact does not catch shingles. Herpes zoster is reactivation of latent virus in that "
    "individual, but exposure to vesicular fluid or, in disseminated disease, airborne virus can transmit "
    "varicella-zoster virus to a susceptible person and cause varicella."],
   ["A susceptible contact can catch shingles directly from the lesions",
    "Shingles arises from reactivation of virus already latent in the contact's own ganglia, so it cannot be acquired "
    "directly. What is transmitted is the virus that causes chickenpox."],
   ["There is no transmission risk of any kind from herpes zoster lesions",
    "Vesicular fluid contains virus. Dismissing the risk entirely would leave susceptible household contacts, "
    "including unvaccinated children and pregnant women, unprotected."],
   ["Transmission occurs only through respiratory droplets in all cases",
    "Localised zoster transmits through contact with vesicular fluid; airborne spread becomes a concern with "
    "disseminated disease."],
   ["The grandson can catch shingles only if he has never had chickenpox",
    "A child who has never had chickenpox and is unvaccinated is exactly the person at risk — but what he would "
    "develop is varicella, not shingles."]],
  0, 91),

Q("Herpes simplex virus",
  "A 24-year-old man has painful grouped vesicles on an erythematous base on the buttock that have broken down into "
  "shallow ulcers. He asks whether the location tells him which virus type he has. What is the correct response?",
  [["Either type can cause oral or genital infection, and lesion location does not reliably determine the type",
    "Correct. Either herpes simplex virus type can cause oral or genital infection, and lesion location does not "
    "reliably determine type. Infections can occur anywhere on the skin, and typing requires a type-specific test."],
   ["Genital or buttock lesions are always herpes simplex virus type 2",
    "This is the common assumption the lecture corrects. Type 1 causes a substantial share of genital infection, and "
    "acting on location alone gives false reassurance about transmission and recurrence patterns."],
   ["Oral lesions are always herpes simplex virus type 1 and genital lesions always type 2",
    "Both types produce similar genital and orofacial primary infections after exposure, so this mapping does not "
    "hold in either direction."],
   ["Type can be determined by the appearance of the vesicles",
    "Grouped vesicles on an erythematous base breaking down to shallow painful ulcers is the appearance of both "
    "types. Morphology does not distinguish them."],
   ["Type can be determined by whether a prodrome occurred",
    "Tenderness, pain, mild paraesthesia, or burning before the lesions appear is characteristic of herpes simplex "
    "virus generally rather than of one type."]],
  0, 112),

Q("Herpes simplex virus",
  "What is the preferred diagnostic test for a suspected herpes simplex virus lesion, and how should a negative "
  "result on an older lesion be interpreted?",
  [["A type-specific nucleic acid amplification test from a fresh vesicle, ulcer base, or crust; a negative result on "
    "an older lesion does not exclude infection because shedding is intermittent",
    "Correct. Swabbing a fresh vesicle, ulcer base, or crust for type-specific nucleic acid amplification testing is "
    "the preferred test. A negative swab from an older lesion does not exclude infection because shedding is "
    "intermittent, and culture is less sensitive in healing or recurrent lesions."],
   ["Viral culture, with a negative result reliably excluding infection",
    "Culture is less sensitive, especially in healing or recurrent lesions, and a negative result specifically does "
    "not exclude herpes simplex virus. Treating culture as definitive gives false reassurance."],
   ["Herpes simplex virus immunoglobulin M serology",
    "Herpes simplex virus immunoglobulin M should not be used. Low-positive type-2 serology should be confirmed with "
    "a second method where available."],
   ["A Tzanck smear, which distinguishes herpes simplex virus from varicella-zoster virus",
    "A Tzanck smear gives rapid evaluation for herpesvirus cytologic changes but cannot distinguish between the "
    "herpesviruses, and polymerase chain reaction is preferred for confirmation."],
   ["A potassium hydroxide preparation from the ulcer base",
    "A potassium hydroxide preparation detects fungal elements and has no role in diagnosing a viral vesicular "
    "eruption."]],
  0, 123),

Q("Herpes simplex virus",
  "A woman with recurrent genital herpes simplex virus type 2 infection is in a relationship with an uninfected "
  "partner. Which treatment approach also reduces transmission risk?",
  [["Daily suppressive valacyclovir",
    "Correct. Recurrent genital herpes may be managed with patient-initiated episodic therapy or daily suppressive "
    "therapy, and suppressive valacyclovir lowers herpes simplex virus type 2 transmission."],
   ["Patient-initiated episodic therapy at the first sign of a recurrence",
    "Episodic therapy is a legitimate option for managing recurrences and shortens individual episodes. But it treats "
    "outbreaks after they begin and does not carry the transmission-reduction benefit of daily suppression."],
   ["Topical acyclovir applied to lesions during outbreaks",
    "Oral agents are what is used for first episodes and recurrences. Topical therapy does not reduce transmission."],
   ["Treatment of the uninfected partner with prophylactic valacyclovir",
    "Suppression is given to the infected partner, in whom it reduces shedding. Treating an uninfected person has no "
    "target."],
   ["No antiviral therapy, since transmission occurs only during visible outbreaks",
    "Transmission can occur during asymptomatic shedding, which is precisely why suppressive therapy reduces risk "
    "beyond avoiding contact during outbreaks."]],
  0, 124),

Q("Herpetic whitlow",
  "A dental hygienist develops a painful, swollen index finger with grouped vesicles on an erythematous base, "
  "preceded by burning and tingling. A colleague suggests incision and drainage. What is the correct management?",
  [["Do not incise and drain; cover the lesions, use hand hygiene, and consider early oral antiviral therapy",
    "Correct. Incision and drainage does not treat herpes simplex virus and can delay healing. Lesions should be "
    "covered, hand hygiene used, contact with mucosa and broken skin avoided until healed, and early oral acyclovir, "
    "valacyclovir, or famciclovir may shorten the episode."],
   ["Incise and drain, then start oral antivirals",
    "This is the specific error the lecture warns against. The lesion is not an abscess, and incising it delays "
    "healing while creating a portal for secondary infection."],
   ["Incise and drain, then start oral antibiotics for presumed bacterial paronychia",
    "Herpetic whitlow mimics bacterial paronychia, which is exactly why it is on that differential and why a Tzanck "
    "smear is used to rule it out. Treating it surgically as a bacterial abscess compounds two errors."],
   ["Apply a topical antifungal and keep the hand dry",
    "That approach belongs to chronic paronychia, where Candida albicans is the most common pathogen and the cause is "
    "prolonged wet work."],
   ["Observe without treatment or precautions, since the lesion is self-limited",
    "The episode does resolve, but covering the lesions and avoiding contact with mucosa and broken skin are needed "
    "to prevent transmission, and early antivirals may shorten it."]],
  0, 128),

Q("Molluscum contagiosum",
  "A 6-year-old has fifteen discrete, smooth, firm, flesh-coloured dome-shaped papules averaging 4 mm on the trunk "
  "and arms, each with a central dimple. His parents ask about treatment. What is a reasonable approach?",
  [["Observation is appropriate for many patients, since procedures may blister, pigment, or scar",
    "Correct. Molluscum contagiosum is a benign poxvirus infection, and observation is appropriate for many patients "
    "because procedures may blister, pigment, or scar. Approved options such as berdazimer gel and cantharidin exist "
    "when treatment is chosen."],
   ["Aggressive curettage of every lesion at the first visit",
    "Destructive procedures carry risks of blistering, pigment change, and scarring, which is the specific reason "
    "observation is offered first in a child with asymptomatic lesions."],
   ["Oral acyclovir",
    "Acyclovir treats herpesvirus infections. Molluscum contagiosum is caused by a poxvirus and does not respond to "
    "it."],
   ["Topical mupirocin to each lesion",
    "Mupirocin is an antibacterial used for impetigo. There is no bacterial infection here."],
   ["Salicylic acid 40 percent to each lesion",
    "Salicylic acid 40 percent is a treatment for plantar warts. It is not among the options given for molluscum."]],
  0, 136, IO_C),

Q("Molluscum contagiosum",
  "What is the characteristic morphological feature of a molluscum contagiosum lesion?",
  [["Central umbilication of a smooth, firm, dome-shaped pearly papule",
    "Correct. Lesions are discrete, smooth-surfaced, firm, flesh-coloured, dome-shaped pearly papules averaging 3 to "
    "5 mm, and central umbilication is characteristic."],
   ["A rough greyish surface with tiny thrombosed capillaries visible",
    "A rough greyish surface with visible red or black dots representing thrombosed dilated capillaries describes "
    "verruca vulgaris. Trimming the surface makes those capillaries more prominent."],
   ["A stuck-on appearance with comedone-like openings",
    "A stuck-on appearance with comedone-like openings on dermoscopy describes seborrheic keratosis."],
   ["An annular plaque with an advancing scaly border and central clearing",
    "That describes tinea corporis, a dermatophyte infection."],
   ["Grouped vesicles on an erythematous base",
    "Grouped vesicles on an erythematous base are the hallmark of herpes simplex virus and herpes zoster."]],
  0, 134),

Q("Warts",
  "A 12-year-old has several elevated, round papules under 1 cm with a rough greyish surface on the fingers. Trimming "
  "one reveals tiny red-black dots. What do those dots represent, and what does their presence help exclude?",
  [["Thrombosed dilated capillaries, which help distinguish a wart from a callus",
    "Correct. Tiny red or black dots represent thrombosed dilated capillaries, and trimming the surface makes them "
    "more prominent. A callus lacks them, which is why paring the lesion is a useful bedside manoeuvre."],
   ["Retained keratin plugs, which help distinguish a wart from a seborrheic keratosis",
    "Comedone-like openings on dermoscopy characterise seborrheic keratosis, which is on the wart differential. But "
    "the dots in a wart are vascular rather than keratin-filled."],
   ["Melanocytic nests, which help exclude melanoma",
    "The dots are thrombosed capillaries rather than pigment. Melanoma is not what paring a verruca is designed to "
    "exclude."],
   ["Fungal elements, which help exclude tinea manuum",
    "Fungal elements are seen microscopically on a potassium hydroxide preparation, not as visible dots on a pared "
    "surface."],
   ["Deep roots extending into the dermis, confirming the need for excision",
    "Warts have no roots. A wart is confined to the epidermis, though it expands and displaces the dermis, giving the "
    "false impression that it extends deeper."]],
  0, 142),

Q("Warts",
  "A 28-year-old woman has multiple smooth, slightly elevated, flat-topped, light-brown papules across her forehead "
  "and dorsal hands. She reports they seemed to multiply along the line where she shaves her legs. What form is this, "
  "and what advice follows?",
  [["Flat warts, which spread by autoinoculation through shaving; observation is reasonable since spontaneous "
    "resolution occurs",
    "Correct. Flat warts are multiple smooth, slightly elevated, flat-topped, skin-coloured to light-brown papules "
    "common on the face, forehead, dorsal hands, and shins, and shaving can spread lesions through autoinoculation. "
    "Observation is reasonable because spontaneous resolution is likely."],
   ["Verruca vulgaris, which requires salicylic acid to every lesion",
    "Common warts are elevated round papules with a rough greyish surface, typically on the fingers and palms, rather "
    "than smooth flat-topped papules on the face and shins."],
   ["Molluscum contagiosum, which requires cantharidin",
    "Molluscum lesions are dome-shaped pearly papules with central umbilication rather than flat-topped papules, and "
    "they are caused by a poxvirus rather than human papillomavirus."],
   ["Plantar warts, which require salicylic acid 40 percent and cryotherapy",
    "Plantar warts occur on the weight-bearing surface of the foot and require therapy only if painful."],
   ["Seborrheic keratoses, which require no treatment",
    "Seborrheic keratoses have a stuck-on appearance with comedone-like openings and are not spread by shaving."]],
  0, 143),

Q("Warts",
  "A patient has plantar warts that are not painful. What is the appropriate management?",
  [["No therapy is required unless they are painful",
    "Correct. Plantar warts do not require therapy unless they are painful. They can cluster together to form a "
    "mosaic wart, and treatment when needed is salicylic acid 40 percent or cryotherapy."],
   ["Cryotherapy every 2 to 3 weeks regardless of symptoms",
    "Cryotherapy every 2 to 3 weeks is an option when treatment is indicated, but it may cause pain, blistering, and "
    "pigment change — all of which are unjustified for an asymptomatic lesion."],
   ["Surgical excision to remove the roots",
    "Warts have no roots, and excision on a weight-bearing surface risks a painful scar worse than the original "
    "lesion."],
   ["Oral antiviral therapy to eradicate human papillomavirus",
    "No therapy eradicates human papillomavirus with certainty, and oral antivirals are not among the treatments for "
    "cutaneous warts."],
   ["Daily salicylic acid 40 percent indefinitely to prevent recurrence",
    "Salicylic acid 40 percent is a treatment for symptomatic plantar warts rather than indefinite prophylaxis, and "
    "treatment choice should account for location, symptoms, and risk of scarring."]],
  0, 145),

Q("Tinea barbae",
  "A 38-year-old farmer has tender, boggy, pustular plaques in the beard area. Hairs in the affected area are easily "
  "removed. What does the ease of hair removal indicate, and what therapy is required?",
  [["It favours tinea barbae over bacterial folliculitis, and oral antifungal therapy is required",
    "Correct. Hair is easily removed in tinea barbae unlike in bacterial folliculitis, and a bacterial culture can be "
    "done to rule the latter out. Topical antifungals do not penetrate the hair follicle, so oral therapy with "
    "griseofulvin or terbinafine is required."],
   ["It favours bacterial folliculitis, and oral cephalexin is required",
    "The finding points the other way. Easy hair removal distinguishes tinea barbae from bacterial folliculitis, "
    "which is the comparison the differential draws."],
   ["It favours tinea barbae, and topical antifungal cream alone is sufficient",
    "The diagnosis is right but the treatment is not. Topical antifungals can be applied but do not penetrate the "
    "hair follicle, so oral therapy is required."],
   ["It indicates pseudofolliculitis barbae, and shaving technique should be modified",
    "Pseudofolliculitis barbae is a foreign body reaction to hair that has curved back into the skin, producing "
    "papules with a visible re-entrant hair shaft rather than boggy pustular plaques."],
   ["It indicates acne vulgaris, and a topical retinoid should be started",
    "Acne is on the differential but is identified by comedones, which are absent in an inflammatory boggy plaque "
    "acquired from animal contact."]],
  0, 22),

Q("Tinea manuum",
  "A 50-year-old labourer has a thickened, dry, scaly right palm that he has attributed to hard physical work. He "
  "also has scaling on both soles. What is the likely diagnosis, and how does it typically present?",
  [["Tinea manuum, often with one palm and both soles involved, and patients frequently unaware it is an infection",
    "Correct. Tinea manuum is associated with tinea pedis, and both palms and soles can be infected at the same time. "
    "Patients are often unaware of the infection, believing the changes are due to dry skin or hard physical labour, "
    "and the involved palm is thickened, dry, and scaly."],
   ["Irritant contact dermatitis from occupational exposure",
    "Occupational irritant dermatitis is a genuine consideration in a labourer, which is what makes his own "
    "explanation plausible. But the coexisting plantar scaling points to a dermatophyte infection spreading between "
    "sites."],
   ["Palmar psoriasis",
    "Psoriasis produces well-demarcated plaques with silvery scale and is typically bilateral on the palms. It would "
    "not be explained by concurrent tinea pedis."],
   ["Dyshidrotic eczema",
    "Dyshidrotic eczema produces crops of intensely pruritic deep-seated vesicles on the palms and lateral fingers "
    "that desquamate. There are no vesicles described here."],
   ["Chronic paronychia",
    "Chronic paronychia is inflammation of the proximal nail folds from prolonged wet work, producing swollen tender "
    "folds and thickened discoloured nail plates rather than a diffusely scaly palm."]],
  0, 56),

Q("Pityriasis versicolor",
  "What is first-line treatment for pityriasis versicolor, and when is systemic therapy appropriate?",
  [["Topical therapy first line, with oral fluconazole or itraconazole reserved for extensive, recurrent, or "
    "refractory disease",
    "Correct. Topical therapy is first line, including ketoconazole shampoo or cream, selenium sulfide, zinc "
    "pyrithione, ciclopirox, or topical terbinafine. Systemic therapy with oral fluconazole or itraconazole is "
    "reserved for extensive, recurrent, or topical-refractory disease."],
   ["Oral terbinafine as first-line therapy",
    "Oral terbinafine is specifically not effective for this organism, even though topical terbinafine is among the "
    "topical options. Malassezia is a yeast rather than a dermatophyte."],
   ["Topical nystatin as first-line therapy",
    "Nystatin treats Candida only. Pityriasis versicolor is caused by Malassezia species."],
   ["Oral fluconazole for all patients at diagnosis",
    "Systemic therapy is reserved rather than routine, and it requires review of hepatic risk, pregnancy status, and "
    "drug interactions that most patients do not need to undergo."],
   ["A high-potency topical corticosteroid",
    "Corticosteroid exposure is listed among the factors that make the condition more common, alongside heat, "
    "humidity, oily skin, sweating, and immunosuppression."]],
  0, 82),

Q("Varicella",
  "What analgesic caution applies to a child with varicella?",
  [["Avoid aspirin and use caution with non-steroidal anti-inflammatory drugs",
    "Correct. Management is supportive, avoiding aspirin in children and using caution with non-steroidal "
    "anti-inflammatory drugs. Early oral antivirals are considered for higher-risk patients and intravenous "
    "acyclovir for severe disease."],
   ["Avoid acetaminophen and use aspirin preferentially",
    "This inverts the caution and would expose a child with a viral illness to the risk aspirin carries in that "
    "setting."],
   ["Avoid all analgesics entirely",
    "Supportive care is the mainstay and symptom relief is appropriate; it is aspirin specifically that is avoided, "
    "with caution around non-steroidal agents."],
   ["Use oral antivirals in every child in place of analgesia",
    "Early oral antivirals are considered for higher-risk patients rather than all children, and they do not "
    "substitute for symptom relief."],
   ["Use systemic corticosteroids for the pruritus",
    "Systemic corticosteroids are not part of varicella management, and immunosuppression during an active viral "
    "infection carries clear risk."]],
  0, 87, IO_C),

Q("Herpes zoster",
  "A 66-year-old man has dermatomal pain but no vesicular eruption. What is this presentation called?",
  [["Zoster sine herpete",
    "Correct. Some patients have pain without a vesicular eruption, which is termed zoster sine herpete. Others have "
    "vesicular eruptions without pain, although almost all patients have pain during the acute eruptive phase."],
   ["Postherpetic neuralgia",
    "Postherpetic neuralgia is pain persisting at least 90 days after rash onset. It follows an eruption rather than "
    "occurring in its absence."],
   ["The pre-eruptive phase, which will always be followed by lesions within 72 hours",
    "The pre-eruptive phase does feature dermatomal dysesthesia or pain with lesion onset by 48 to 72 hours, which "
    "makes this the closest wrong answer. But there is a recognised presentation in which no lesions ever appear."],
   ["Ramsay Hunt syndrome",
    "Ramsay Hunt syndrome is peripheral facial palsy with painful vesicles of the ear canal, auricle, or oropharynx. "
    "It is defined in part by the presence of vesicles."],
   ["Disseminated zoster",
    "Disseminated disease involves lesions beyond the affected and adjacent dermatomes, which requires an eruption to "
    "be present."]],
  0, 99),

Q("Ramsay Hunt syndrome",
  "A 58-year-old woman presents with right-sided facial weakness, painful vesicles in the right ear canal, and "
  "vertigo. What is the diagnosis, and what treatment is added beyond antivirals?",
  [["Ramsay Hunt syndrome, treated with an antiviral plus a systemic corticosteroid started early when not "
    "contraindicated",
    "Correct. Ramsay Hunt syndrome, or herpes zoster oticus, is peripheral facial palsy with painful vesicles of the "
    "ear canal, auricle, or oropharynx, sometimes with hearing loss, tinnitus, or vertigo. Antiviral therapy plus a "
    "systemic corticosteroid is started early when not contraindicated."],
   ["Ramsay Hunt syndrome, treated with an antiviral alone",
    "The diagnosis is right but the regimen is incomplete, and the corticosteroid is the part specifically added in "
    "this syndrome rather than in uncomplicated zoster."],
   ["Herpes zoster ophthalmicus, treated with an antiviral and urgent ophthalmology referral",
    "Herpes zoster ophthalmicus involves the ophthalmic division of the trigeminal nerve, with Hutchinson sign on the "
    "nose raising ocular risk. The ear canal and facial nerve are a different territory."],
   ["Bell palsy, treated with a corticosteroid alone",
    "Idiopathic facial palsy does not produce painful vesicles in the ear canal. The vesicles identify a zoster "
    "reactivation and mandate antiviral therapy."],
   ["Otitis externa, treated with topical antibiotic drops",
    "Otitis externa does not cause facial palsy or grouped vesicles, and antibacterial drops would leave a viral "
    "reactivation untreated."]],
  0, 104),

Q("Herpes simplex virus",
  "A 21-year-old woman presents with painful genital ulcers. The clinician considers alternative causes. Which "
  "differential is characteristically painless?",
  [["Syphilis, whose lesions start as solitary raised papules that erode and are usually painless",
    "Correct. Syphilis lesions start as solitary raised papules that erode and are usually painless, which is what "
    "distinguishes them from the painful ulcers of herpes simplex virus and chancroid."],
   ["Chancroid, caused by Haemophilus ducreyi",
    "Chancroid is a bacterial sexually transmitted infection caused by Haemophilus ducreyi producing painful "
    "necrotizing ulcers with inguinal lymphadenopathy. It is painful rather than painless."],
   ["Trauma",
    "Trauma appears on the differential and is characteristically painful, so it does not provide the contrast the "
    "question asks for."],
   ["Candidiasis",
    "Candidiasis is on the differential and produces burning and pruritus with well-demarcated erythema and satellite "
    "lesions rather than a painless eroded papule."],
   ["Herpes simplex virus recurrence",
    "Herpes simplex virus produces grouped vesicles that break down into shallow painful ulcers, with localised pain "
    "and prodromal burning."]],
  0, 121),

Q("Molluscum contagiosum",
  "A 15-year-old presents with molluscum lesions confined to the genital area. What is the appropriate approach?",
  [["Assess for sexually transmitted infections as appropriate, since genital lesions in adolescents and adults may "
    "be sexually transmitted",
    "Correct. Genital lesions in adolescents and adults may be sexually transmitted and assessment for other "
    "infections is appropriate. In a child, genital lesions require context-sensitive assessment, and location alone "
    "does not prove abuse."],
   ["Assume sexual abuse on the basis of the genital location alone",
    "Location alone does not prove abuse, and the assessment is described as context-sensitive. Drawing that "
    "conclusion from site alone is both clinically and ethically wrong."],
   ["Reassure that genital molluscum is never sexually transmitted",
    "Sexual contact is common in adults with genital lesions, so this would miss an opportunity to screen for "
    "coexisting infections."],
   ["Treat with oral acyclovir and screen for herpes simplex virus only",
    "Molluscum contagiosum is a poxvirus infection and does not respond to acyclovir, and screening should not be "
    "limited to a single organism."],
   ["Refer immediately for surgical excision of all lesions",
    "Observation is appropriate for many patients, and procedures may blister, pigment, or scar. Excision is not the "
    "first response."]],
  0, 133, IO_C),

Q("Warts",
  "What treatment principle applies to all cutaneous warts?",
  [["No therapy eradicates human papillomavirus with certainty and recurrence can occur, so treatment is chosen "
    "according to location, symptoms, age, pregnancy and immune status, and scarring risk",
    "Correct. No therapy eradicates human papillomavirus with certainty and recurrence can occur. Treatment is chosen "
    "according to location, symptoms, age, pregnancy status, immune status, and the risk of scarring or "
    "dyspigmentation, avoiding excessive freezing or destruction."],
   ["Cryotherapy eradicates human papillomavirus and prevents recurrence",
    "Cryotherapy is a treatment option but does not eradicate the virus, and it may cause pain, blistering, and "
    "pigment change. Promising eradication sets up the patient for a recurrence they were told could not happen."],
   ["All warts should be treated at diagnosis regardless of symptoms",
    "Observation is reasonable because many warts resolve spontaneously, and plantar warts specifically do not "
    "require therapy unless painful."],
   ["Biopsy is required for every wart before treatment",
    "Biopsy is generally unnecessary and is reserved for atypical, bleeding, ulcerated, growing, or refractory "
    "lesions and for immunocompromised patients."],
   ["Warts must be excised deeply because they extend into the dermis",
    "A wart is confined to the epidermis. It expands and displaces the dermis, which gives a false impression of "
    "depth, and it has no roots."]],
  0, 149),

Q("Herpes zoster",
  "Which dermatomes are most frequently involved in herpes zoster?",
  [["Thoracic, involved in about 55 percent of cases, followed by cranial at about 20 percent",
    "Correct. Thoracic dermatomes are most frequently involved at about 55 percent, cranial at about 20 percent, "
    "with lumbar and sacral distributions following."],
   ["Cranial, involved in about 55 percent, followed by thoracic at about 20 percent",
    "The two are reversed. Thoracic involvement is by far the commonest, and inverting the figures would skew "
    "expectations toward cranial disease."],
   ["Sacral dermatomes in the majority of cases",
    "Sacral involvement occurs but is not the leading distribution."],
   ["Lumbar dermatomes in the majority of cases",
    "Lumbar involvement occurs but is less frequent than thoracic and cranial disease."],
   ["The distribution is random and no dermatome predominates",
    "There is a clear and clinically useful predominance, which is why the percentages are taught."]],
  0, 100),

Q("Tinea corporis",
  "When treating localised tinea corporis with a topical agent, how far should the medication be applied?",
  [["To the lesion and 1 to 2 cm beyond its border, continuing through the recommended course after visible "
    "improvement",
    "Correct. Topical terbinafine, butenafine, or an azole is applied to the lesion and 1 to 2 cm beyond its border, "
    "using the product-specific frequency and duration and continuing through the recommended course after visible "
    "improvement."],
   ["To the visible lesion only, stopping as soon as it clears",
    "Both halves fail. The advancing edge extends beyond what is visible, and stopping at visible clearance leaves "
    "viable organism behind, which is the commonest cause of apparent relapse."],
   ["To the whole limb, to prevent spread",
    "Treating an entire limb is unnecessary and increases irritation and cost without added benefit over margin "
    "coverage."],
   ["To the centre of the lesion only, where the infection began",
    "The centre has typically cleared as the organism advances outward. Treating there misses where the fungus "
    "actually is."],
   ["Application distance does not matter provided oral therapy is also given",
    "Oral therapy is reserved for extensive, follicular, immunocompromised, refractory, or recurrent disease rather "
    "than added routinely to localised disease."]],
  0, 28),

Q("Onychomycosis",
  "From where should a nail specimen be taken to confirm onychomycosis?",
  [["The most proximal accessible diseased nail bed or subungual debris",
    "Correct. Sampling should be from the most proximal accessible diseased nail bed and subungual debris, where "
    "viable organism is concentrated, using potassium hydroxide microscopy, periodic acid-Schiff stain of clippings, "
    "fungal culture, or polymerase chain reaction."],
   ["The distal free edge of the nail plate",
    "The distal edge contains the oldest, most degraded material with the lowest yield of viable organism. Distal "
    "lateral disease causes debris and crumbling there, but it is not the best sampling site."],
   ["The surrounding proximal nail fold",
    "The proximal nail fold is the site of paronychia rather than of nail plate infection, and sampling it would not "
    "demonstrate the organism within the nail."],
   ["A plucked hair from the affected limb",
    "A plucked hair is used for potassium hydroxide microscopy in dermatophyte folliculitis and tinea capitis."],
   ["Any nail on the affected foot, whether or not it appears diseased",
    "Sampling clinically normal nail risks a false negative and would not confirm the diagnosis for the affected "
    "nail."]],
  0, 51, IO_A),

Q("Tinea capitis",
  "A child is being treated for tinea capitis. What advice about school attendance and household measures is "
  "correct?",
  [["School exclusion is generally unnecessary once effective treatment has begun, and personal hair items should not "
    "be shared",
    "Correct. School exclusion is generally unnecessary once effective treatment has started. Patients should avoid "
    "sharing personal hair items and should clean clippers, combs, brushes, bedding, and hats, and household contacts "
    "may use a sporicidal shampoo."],
   ["The child must remain out of school until the scalp is completely clear",
    "Requiring complete clearance would keep a child out for weeks or months of oral therapy unnecessarily, since "
    "exclusion is generally not needed once effective treatment has begun."],
   ["No household measures are needed because transmission is only person to person",
    "Transmission occurs from infected persons, pets, fallen hairs, clothing, combs, hats, and furniture, and fungal "
    "particles remain viable for months. Fomites matter."],
   ["Treatment can be stopped as soon as itching and scaling improve",
    "Patients are specifically told to complete the prescribed oral course even when itching or scaling improves "
    "early."],
   ["Household contacts should all take oral antifungal therapy",
    "Household contacts may use a sporicidal shampoo rather than systemic therapy, which would expose asymptomatic "
    "people to a drug requiring hepatic consideration."]],
  0, 17, IO_C),
]

QUESTIONS += [
Q("Dermatophytes",
  "How are dermatophyte infections classified, and what does the naming convey?",
  [["By body location of the fungus, giving tinea capitis, barbae, corporis, manuum, cruris, and pedis",
    "Correct. Dermatophyte infections are classified by body location: tinea capitis for scalp, barbae for beard, "
    "corporis for body, manuum for hand, cruris for the inguinal creases, and pedis for feet."],
   ["By the causative species, giving Trichophyton, Microsporum, and Epidermophyton infection",
    "There are three genera of dermatophytes and species identification guides drug choice in tinea capitis. But the "
    "tinea naming system itself refers to body site rather than organism."],
   ["By the depth of invasion into the dermis",
    "Dermatophytes infect only dead keratin in the stratum corneum, hair, and nails, so they do not invade the dermis "
    "at all."],
   ["By whether the infection is contagious",
    "All dermatophyte infections are transmissible. Contagiousness is not the basis of the classification."],
   ["By the patient's age at presentation",
    "Age matters epidemiologically — tinea capitis is predominantly preadolescent and tinea pedis is the most common "
    "dermatophyte infection in adults — but it is not what the tinea names denote."]],
  0, 7),
]
