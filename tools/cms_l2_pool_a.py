# Clinical Medicine and Surgery I, Lecture 2 (General Dermatology I) — pool A
# SET 1 (instructional-objective style, not vignette).
# Terminology, description, diagnostic tools, and dermatologic pharmacology.
#
# CMS format per [[cms_exam_spec]]: Set 1 is 2 x 30 on the INSTRUCTIONAL
# OBJECTIVES, taken from the syllabus rather than the slides. Set 2 is a
# separate 2 x 30 of vignettes.
#
# Objectives (a) and (b) — anatomy and physiology of the integument — are named
# in the syllabus but the deck covers them only in passing before moving to
# terminology, so this pool draws them from what the lecture actually taught:
# the descriptive vocabulary and the tools. The morphology definitions here are
# JAQUITH'S: macule < 1 cm, patch > 1 cm. Clinical Pathophysiology teaches 5 mm
# for the same lesions; each course examines its own.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "2. General Dermatology I.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Anatomy of the integumentary system"
IOC = "c — Etiologies, manifestations, diagnosis and management of dermatological conditions"

POOL_A = [
 dict(topic="Describing a rash", io=IOA,
   q="Which six features are used to translate a dermatological finding into words?",
   opts=[
     ["Primary morphology, secondary morphology, demarcation, colour, size and distribution",
      "Correct. Getting all six into a description is what lets another provider picture the lesion without seeing it."],
     ["Primary morphology, colour and distribution only, since the rest are subjective",
      "Demarcation, secondary morphology and size are all part of the description."],
     ["Onset, duration, severity, triggers, treatments tried and response",
      "Those come from the history rather than the description of the lesion."],
     ["Location, laterality, symmetry, tenderness, temperature and texture",
      "These are not the six features named."]],
   c=0, cite=c(9)),

 dict(topic="Primary morphology", io=IOA,
   q="How is a macule defined in this lecture?",
   opts=[
     ["A flat lesion less than one centimetre, without elevation or depression",
      "Correct. A patch is the same lesion larger than one centimetre."],
     ["A flat lesion less than five millimetres",
      "Five millimetres is the Clinical Pathophysiology convention; this course uses one centimetre."],
     ["An elevated solid lesion less than one centimetre",
      "That is a papule."],
     ["A flat elevated plateau lesion greater than one centimetre",
      "That is a plaque."]],
   c=0, cite=c(10)),

 dict(topic="Primary morphology", io=IOA,
   q="What distinguishes a plaque from a patch?",
   opts=[
     ["A plaque is elevated and plateau-like; a patch is flat with no elevation",
      "Correct — both exceed one centimetre, so elevation is the discriminator."],
     ["A plaque is larger than a patch",
      "Both are greater than one centimetre; size does not separate them."],
     ["A plaque is fluid-filled and a patch is solid",
      "Neither is fluid-filled."],
     ["A plaque is poorly demarcated and a patch is well demarcated",
      "Demarcation is described separately and varies for both."]],
   c=0, cite=c(10)),

 dict(topic="Primary morphology", io=IOA,
   q="A solid elevated lesion measuring more than one centimetre is called what?",
   opts=[
     ["A nodule",
      "Correct. A papule is the same solid elevated lesion under one centimetre."],
     ["A papule",
      "A papule is under one centimetre."],
     ["A wheal",
      "A wheal is a firm oedematous plaque from fluid infiltrating the dermis."],
     ["A bulla",
      "A bulla is fluid-filled."]],
   c=0, cite=c(12)),

 dict(topic="Primary morphology", io=IOA,
   q="What defines a wheal?",
   opts=[
     ["A firm oedematous plaque produced by infiltration of fluid into the dermis",
      "Correct — the fluid is in the tissue rather than in a cavity, which is what separates it from a vesicle."],
     ["A fluid-filled lesion containing leukocytes",
      "That is a pustule."],
     ["A fluid-filled lesion under one centimetre",
      "That is a vesicle."],
     ["A deposit of blood measuring one to two millimetres",
      "That is a petechia."]],
   c=0, cite=c(13)),

 dict(topic="Primary morphology", io=IOA,
   q="What distinguishes a pustule from a vesicle?",
   opts=[
     ["A pustule contains leukocytes; a vesicle contains clear fluid",
      "Correct — the contents, not the size, separate them."],
     ["A pustule is larger than one centimetre and a vesicle is smaller",
      "That is the vesicle-to-bulla distinction."],
     ["A pustule is solid and a vesicle is fluid-filled",
      "Both contain fluid."],
     ["A pustule sits in the dermis and a vesicle in the epidermis",
      "Depth is not what distinguishes them here."]],
   c=0, cite=c(13)),

 dict(topic="Primary morphology", io=IOA,
   q="A fluid-filled lesion greater than one centimetre is called what?",
   opts=[
     ["A bulla",
      "Correct — a vesicle is the same lesion up to one centimetre."],
     ["A vesicle",
      "A vesicle is up to one centimetre."],
     ["A pustule",
      "A pustule is defined by its leukocyte content."],
     ["A nodule",
      "A nodule is solid rather than fluid-filled."]],
   c=0, cite=c(14)),

 dict(topic="Blood deposits", io=IOA,
   q="How are petechiae and purpura distinguished by size in this lecture?",
   opts=[
     ["Petechiae are deposits of blood 1 to 2 mm; purpura are 4 mm or greater",
      "Correct, and purpura is flagged as a medical emergency until proven otherwise."],
     ["Petechiae are under 3 mm and purpura are 3 mm to 1 cm",
      "That is the Clinical Pathophysiology convention rather than this lecture's."],
     ["Petechiae are 4 mm or greater and purpura are 1 to 2 mm",
      "The sizes are reversed."],
     ["Both are defined as deposits of blood greater than 1 cm",
      "Neither is defined that way; over 1 cm would be an ecchymosis."]],
   c=0, cite=c(15)),

 dict(topic="Blood deposits", io=IOA,
   q="What does this lecture say about a patient presenting with purpura?",
   opts=[
     ["It is a medical emergency until proven otherwise",
      "Correct — the lecture flags it explicitly rather than treating it as one finding among many."],
     ["It is a benign finding common in the elderly",
      "The lecture treats it as an emergency until disproven."],
     ["It requires only outpatient dermatology follow-up",
      "That understates the urgency stated."],
     ["It is diagnostic of thrombocytopenia",
      "It raises concern but is not diagnostic of any single cause."]],
   c=0, cite=c(15)),

 dict(topic="Secondary morphology", io=IOA,
   q="What distinguishes an ulceration from an erosion?",
   opts=[
     ["An ulceration is full-thickness loss extending to the dermis or deeper; an erosion loses only the epidermis",
      "Correct — depth is the discriminator, and it determines whether the lesion can scar."],
     ["An ulceration is linear and an erosion is round",
      "Shape does not distinguish them."],
     ["An ulceration is painful and an erosion is painless",
      "Neither is defined by pain."],
     ["An ulceration involves only the epidermis and an erosion reaches the dermis",
      "The definitions are reversed."]],
   c=0, cite=c(17)),

 dict(topic="Secondary morphology", io=IOA,
   q="What is lichenification?",
   opts=[
     ["Thickening and hardening of the skin",
      "Correct — it develops from chronic rubbing or scratching."],
     ["Accumulation of loose cornified fragments of the epidermis",
      "That is scaling."],
     ["A break in the skin",
      "That is a fissure."],
     ["Abnormal formation of connective tissue",
      "That is a scar."]],
   c=0, cite=c(18)),

 dict(topic="Secondary morphology", io=IOA,
   q="How is scaling described?",
   opts=[
     ["Accumulation of loose or adherent cornified fragments of the epidermis, typically grey or white",
      "Correct."],
     ["A dried crust of serum",
      "That is serum crusting."],
     ["A scratch or abrasion where the top layer of skin wears off",
      "That is an excoriation."],
     ["Thickening and hardening of the skin",
      "That is lichenification."]],
   c=0, cite=c(18)),

 dict(topic="Demarcation", io=IOA,
   q="How is a poorly demarcated lesion described?",
   opts=[
     ["Irregular or blotchy in appearance, without well-defined borders",
      "Correct — as against a well demarcated lesion, which has clearly defined borders."],
     ["Smaller than one centimetre in every dimension",
      "Demarcation is about border definition rather than size."],
     ["Present in more than one body region",
      "That is distribution."],
     ["Raised above the surrounding skin surface",
      "That is elevation, part of primary morphology."]],
   c=0, cite=c(20)),

 dict(topic="Diagnostic tools", io=IOC,
   q="Which biopsy technique cuts deep into the fat layers and is preferred for rashes or deeper bumps?",
   opts=[
     ["Punch biopsy",
      "Correct — it often needs one or two stitches."],
     ["Shave biopsy",
      "A shave biopsy takes surface skin only and needs no stitches; it suits moles and growths on top."],
     ["Excisional biopsy",
      "An excisional biopsy removes the whole lesion with deep and wide margins and always needs stitches."],
     ["Curettage",
      "This technique is not among the three described."]],
   c=0, cite=c(26)),

 dict(topic="Diagnostic tools", io=IOC,
   q="Which biopsy takes the whole lesion with deep and wide margins?",
   opts=[
     ["Excisional biopsy",
      "Correct, and it always needs stitches to close."],
     ["Punch biopsy",
      "A punch biopsy samples deeply but does not take the whole lesion with margins."],
     ["Shave biopsy",
      "A shave biopsy removes only surface skin."],
     ["Incisional biopsy",
      "This is not one of the three described in the lecture."]],
   c=0, cite=c(26)),

 dict(topic="Diagnostic tools", io=IOC,
   q="What does a Wood's lamp emit, and what is it used to evaluate?",
   opts=[
     ["Long-wave ultraviolet light, used to evaluate pigment changes in selected fungal or bacterial infections",
      "Correct — a handheld device highlighting subtle changes in skin, scalp and hair."],
     ["Polarised white light, used to magnify pigmented lesions",
      "That describes a dermoscope."],
     ["Infrared light, used to assess perfusion",
      "This is not what a Wood's lamp does."],
     ["Short-wave ultraviolet light, used to sterilise the skin surface",
      "It is a diagnostic device, not a sterilising one."]],
   c=0, cite=c(27)),

 dict(topic="Diagnostic tools", io=IOC,
   q="What does a potassium hydroxide wet preparation detect?",
   opts=[
     ["Fungal elements in skin, hair or nail samples",
      "Correct."],
     ["Herpesvirus cytologic changes in vesicular lesions",
      "That is a Tzanck smear."],
     ["The scabies mite, its eggs or its faecal pellets",
      "That is a mineral oil preparation."],
     ["Immune deposits within skin tissue",
      "That is direct immunofluorescence."]],
   c=0, cite=c(28)),

 dict(topic="Diagnostic tools", io=IOC,
   q="What is a Tzanck smear used for, and what is preferred for confirmation?",
   opts=[
     ["Rapid evaluation of vesicular lesions for herpesvirus cytologic changes, with polymerase chain reaction preferred for confirmation",
      "Correct — the smear is fast, the polymerase chain reaction is definitive."],
     ["Rapid detection of fungal elements, with culture preferred for confirmation",
      "That describes potassium hydroxide preparation and fungal culture."],
     ["Detection of the scabies mite, with dermoscopy preferred for confirmation",
      "That describes mineral oil testing."],
     ["Detection of immune deposits, with serum ELISA preferred for confirmation",
      "That describes direct immunofluorescence."]],
   c=0, cite=c(32)),

 dict(topic="Diagnostic tools", io=IOC,
   q="A mineral oil preparation is used to confirm which diagnosis?",
   opts=[
     ["Scabies infestation, by identifying the mite, its eggs or its faecal pellets",
      "Correct — a rapid bedside test."],
     ["Onychomycosis, by identifying fungal elements in the nail",
      "That uses nail clipping with periodic acid-Schiff stain."],
     ["Bullous pemphigoid, by identifying basement membrane antibodies",
      "That uses direct immunofluorescence or serum studies."],
     ["Allergic contact dermatitis, by identifying the causative allergen",
      "That uses patch testing."]],
   c=0, cite=c(33)),

 dict(topic="Diagnostic tools", io=IOC,
   q="Which allergy test diagnoses allergic contact dermatitis?",
   opts=[
     ["Patch testing",
      "Correct. Skin-prick testing evaluates immediate, immunoglobulin E-mediated reactions instead."],
     ["Skin-prick testing",
      "That evaluates immediate immunoglobulin E-mediated allergic reactions."],
     ["Serum immunoglobulin E allergy testing",
      "That evaluates immunoglobulin E allergies in the blood."],
     ["Direct immunofluorescence",
      "That detects immune deposits in tissue, used in vesiculobullous disease."]],
   c=0, cite=c(35)),

 dict(topic="Diagnostic tools", io=IOC,
   q="Nail clipping with periodic acid-Schiff stain evaluates which suspected condition?",
   opts=[
     ["Onychomycosis",
      "Correct."],
     ["Psoriatic nail disease",
      "Nail changes occur in psoriasis but this stain targets fungal infection."],
     ["Subungual melanoma",
      "That would require biopsy of the nail matrix."],
     ["Alopecia areata",
      "Nail pitting occurs in alopecia areata, but this test is not how it is assessed."]],
   c=0, cite=c(36)),

 dict(topic="Diagnostic tools", io=IOC,
   q="What is the hair-pull test?",
   opts=[
     ["An office exam in which a small group of hairs is gently tugged to measure active shedding",
      "Correct. Trichoscopy is the separate imaging method using a magnified scope."],
     ["A magnified imaging method for viewing the scalp and follicles",
      "That is trichoscopy."],
     ["A biopsy of the scalp taken to exclude scarring alopecia",
      "That is a scalp biopsy."],
     ["A test measuring the tensile strength of the hair shaft",
      "It measures shedding rather than strength."]],
   c=0, cite=c(37)),

 dict(topic="Pharmacology", io=IOC,
   q="What is the usual application schedule for topical corticosteroids given in this lecture?",
   opts=[
     ["Twice a day for two weeks",
      "Correct, with potency selected according to site and severity."],
     ["Once a day for six weeks",
      "That is not the schedule given."],
     ["Three times a day until the rash resolves",
      "That is not the schedule given."],
     ["Twice a day indefinitely for chronic conditions",
      "Prolonged use risks atrophy, striae, telangiectasia and hypopigmentation."]],
   c=0, cite=c(41)),

 dict(topic="Pharmacology", io=IOC,
   q="Which adverse effects follow prolonged topical corticosteroid use?",
   opts=[
     ["Atrophy, striae, telangiectasia and hypopigmentation",
      "Correct — which is why potency is matched to site and severity."],
     ["Photosensitivity, dryness and irritation",
      "Those are the topical retinoid effects."],
     ["Nephrotoxicity and hepatotoxicity",
      "Nephrotoxicity is a caution with calcipotriene rather than topical steroids."],
     ["Hyperpigmentation and hypertrichosis",
      "Hypopigmentation, not hyperpigmentation, is the listed effect."]],
   c=0, cite=c(41)),

 dict(topic="Pharmacology", io=IOC,
   q="Which topical corticosteroid is classified as high potency in this lecture?",
   opts=[
     ["Clobetasol propionate 0.05%",
      "Correct. Hydrocortisone at any strength is mild."],
     ["Hydrocortisone 2.5%",
      "Hydrocortisone at all strengths is classified mild."],
     ["Betamethasone valerate 0.025%",
      "That is moderate."],
     ["Triamcinolone acetonide 0.1%",
      "That is medium to high."]],
   c=0, cite=c(42)),

 dict(topic="Pharmacology", io=IOC,
   q="Which statement about topical antifungals is correct?",
   opts=[
     ["They are particularly effective against dermatophytes, but topical therapy is inadequate for most scalp or nail infections",
      "Correct — terbinafine, clotrimazole and ketoconazole are the agents named."],
     ["They are effective for scalp and nail infections without systemic therapy",
      "Topical therapy is explicitly inadequate for most of those."],
     ["They are ineffective against dermatophytes",
      "They are particularly effective against them."],
     ["They are first-line for allergic contact dermatitis",
      "That condition is not fungal."]],
   c=0, cite=c(43)),

 dict(topic="Pharmacology", io=IOC,
   q="Which topical retinoid also treats psoriasis?",
   opts=[
     ["Tazarotene",
      "Correct — the other named retinoids are adapalene, tretinoin and trifarotene."],
     ["Adapalene",
      "Adapalene is used for acne and photoaging."],
     ["Tretinoin",
      "Tretinoin is used for acne and photoaging."],
     ["Trifarotene",
      "Trifarotene is not the one named for psoriasis."]],
   c=0, cite=c(44)),

 dict(topic="Pharmacology", io=IOC,
   q="Which formulation is generally most occlusive, and what is it the foundation of treatment for?",
   opts=[
     ["Ointments, and they are the foundation of treatment for many inflammatory conditions including xerosis, eczema, irritant dermatitis and diaper dermatitis",
      "Correct — ointments are more occlusive than creams or lotions."],
     ["Lotions, used chiefly for scalp conditions",
      "Lotions are the least occlusive of the three."],
     ["Creams, because they spread most easily over large areas",
      "Creams sit between ointments and lotions in occlusiveness."],
     ["Gels, because they dry quickly and do not trap heat",
      "Gels are not among the formulations compared."]],
   c=0, cite=c(40)),

 dict(topic="History taking", io=IOC,
   q="Which finding is listed as an urgent warning sign in a patient with a rash?",
   opts=[
     ["Fever with a rapidly spreading, painful, blistering, purple or non-blanching rash",
      "Correct, alongside airway swelling, skin peeling involving eyes, mouth or genitals, severe pain with pus or red streaking, and a new rash after starting a medication."],
     ["Pruritus that disturbs sleep",
      "This affects quality of life but is not on the urgent list."],
     ["A rash that has been present for more than six weeks",
      "Chronicity alone is not an urgent warning sign."],
     ["A rash that improves with over-the-counter emollients",
      "Improvement is reassuring rather than alarming."]],
   c=0, cite=c(8)),

 dict(topic="History taking", io=IOC,
   q="Why does the medication history ask when each drug was started in relation to the rash?",
   opts=[
     ["Because the timing between starting a drug and the eruption is what implicates it",
      "Correct — a new rash after starting a medication, especially with fever or mucosal sores, is an urgent warning sign."],
     ["Because most drug eruptions occur only after six months of therapy",
      "No such interval is given."],
     ["Because only prescription medications can cause eruptions",
      "Antibiotics, pain relievers, supplements, vitamins and herbal products are all asked about."],
     ["Because the dose determines whether a reaction is possible",
      "Timing rather than dose is what the history targets."]],
   c=0, cite=c(7)),
]
