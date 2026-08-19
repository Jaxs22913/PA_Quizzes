# CMS I Lecture 2 (General Dermatology I) — SET 2, vignette pool C.
#
# Written to correct two measured gaps in pools A and B rather than to add
# volume for its own sake:
#
#   1. LEAD-IN MIX. A and B came out management-heavy — 20 of 48 asked for
#      treatment or next step, against only 2 asking for a test. The standing
#      style says spread the lead-ins across every beat the stem contains, so
#      this pool is weighted to INITIAL TEST, CONFIRMATORY TEST and DIAGNOSIS.
#   2. COUNT. 48 is short of the 60 a 2 x 30 set needs without repeating a
#      question between the two forms.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "2. General Dermatology I.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOC = "Objective c — Etiologies, manifestations, diagnosis and management of dermatological conditions"

POOL_C = [
 dict(topic="Nummular eczema", io=IOC,
   q="A 55-year-old man has several round scaly plaques on his forearms. The lesions are uniform throughout without central clearing, and he has been applying an over-the-counter antifungal for three weeks without improvement. Which is the best initial diagnostic test?",
   opts=[
     ["Potassium hydroxide preparation",
      "Correct. Tinea corporis is the main differential, and it must be excluded before committing to a diagnosis of nummular eczema."],
     ["Punch biopsy for direct immunofluorescence",
      "Immunofluorescence is used for vesiculobullous disease."],
     ["Serum immunoglobulin E level",
      "This supports atopic dermatitis but is not routinely tested and does not address this differential."],
     ["Bacterial culture and sensitivity",
      "Culture is reserved for lesions that appear secondarily infected."]],
   c=0, cite=c(74)),

 dict(topic="Atopic dermatitis", io=IOC,
   q="A 32-year-old woman has adult-onset eczema that has not responded to appropriate topical therapy over several months. Her rash involves the eyelids and hands. Which is the most appropriate diagnostic test?",
   opts=[
     ["Patch testing",
      "Correct — patch testing is indicated for atypical, adult-onset or treatment-resistant disease, and eyelid and hand involvement raises contact allergy."],
     ["Potassium hydroxide preparation",
      "This detects fungal elements, which the distribution and history do not suggest."],
     ["Skin-prick testing",
      "This evaluates immediate immunoglobulin E-mediated reactions rather than contact allergy."],
     ["Tzanck smear",
      "This evaluates vesicular lesions for herpesvirus changes."]],
   c=0, cite=c(56)),

 dict(topic="Atopic dermatitis", io=IOC,
   q="A 5-year-old with atopic dermatitis has an area of weeping, thickly crusted plaques with pustules over a previously flaring elbow. She is afebrile. Which is the most appropriate diagnostic test?",
   opts=[
     ["Bacterial culture of the crusted lesions",
      "Correct — culture is indicated for purulent, pustular or significantly crusted lesions to rule out infection."],
     ["Herpes simplex virus polymerase chain reaction",
      "That is triggered by painful monomorphic erosions or systemic illness rather than crusting with pustules."],
     ["Patch testing",
      "This is for atypical, adult-onset or treatment-resistant disease."],
     ["Potassium hydroxide preparation",
      "This addresses fungal infection, which the description does not suggest."]],
   c=0, cite=c(56)),

 dict(topic="Pemphigus", io=IOC,
   q="A 58-year-old woman has painful oral erosions and flaccid skin bullae. A biopsy has been taken. Which finding on that biopsy would establish the diagnosis?",
   opts=[
     ["Acantholysis",
      "Correct — loss of keratinocyte-to-keratinocyte adhesion is the defining histological feature, with immunofluorescence and serum ELISA confirmatory."],
     ["Neutrophils aligned in a straight narrow row at the dermal-epidermal junction",
      "That is bullous pemphigoid."],
     ["Band-like lymphocytic infiltration of the dermis",
      "That is lichen planus."],
     ["Hyperkeratosis without parakeratosis and Civatte bodies",
      "Those are also lichen planus findings."]],
   c=0, cite=c(132)),

 dict(topic="Diaper dermatitis", io=IOC,
   q="A 10-month-old has a diaper rash involving the inguinal folds with satellite papules beyond the main area. Which is the most appropriate diagnostic test?",
   opts=[
     ["Potassium hydroxide preparation",
      "Correct — fold involvement and satellite lesions suggest Candida, and identification of budding yeast or pseudohyphae supports it."],
     ["Bacterial culture",
      "Culture is obtained when purulence, bullae, crusting or perianal bacterial disease is suspected."],
     ["Patch testing",
      "This identifies contact allergens and is not appropriate at this age or presentation."],
     ["Skin biopsy",
      "Biopsy is not required for a clinical diagnosis of this pattern."]],
   c=0, cite=c(108)),

 dict(topic="Seborrhoeic dermatitis", io=IOC,
   q="A 3-month-old infant has thick, greasy yellow scale adherent to the scalp, with mild erythema and no distress. Which is the most likely diagnosis?",
   opts=[
     ["Seborrhoeic dermatitis",
      "Correct — the scalp form is dandruff in adults and this presentation in infants, driven by Malassezia in sebum-rich areas."],
     ["Atopic dermatitis",
      "The infantile pattern favours weeping patches on cheeks and extensor surfaces rather than greasy adherent scalp scale."],
     ["Tinea capitis",
      "This produces round scaling patches of alopecia with hairs broken close to the scalp."],
     ["Psoriasis",
      "Scalp psoriasis produces well-demarcated plaques with silvery rather than greasy yellow scale."]],
   c=0, cite=c(93)),

 dict(topic="Psoriasis", io=IOC,
   q="A 41-year-old man has plaques on both elbows that have been present for two years. The clinical picture is not clear-cut and treatment has failed. Which test would settle the diagnosis?",
   opts=[
     ["Skin biopsy",
      "Correct — psoriasis is generally a clinical diagnosis, though biopsy may be needed for definitive diagnosis."],
     ["Potassium hydroxide preparation",
      "This excludes fungal infection but does not confirm psoriasis."],
     ["Serum HLA-B27",
      "This associates with psoriatic arthritis rather than establishing cutaneous psoriasis."],
     ["Direct immunofluorescence",
      "This is used for vesiculobullous disease."]],
   c=0, cite=c(162)),

 dict(topic="Alopecia areata", io=IOC,
   q="A 30-year-old woman has patchy hair loss. Dermoscopy shows yellow dots, black dots, broken hairs, tapered hairs and short regrowth. Which is the most likely diagnosis?",
   opts=[
     ["Alopecia areata",
      "Correct — the diagnosis is usually clinical and is strengthened by exactly this dermoscopic pattern."],
     ["Androgenetic alopecia",
      "This produces patterned recession or diffuse thinning without these dermoscopic features."],
     ["Trichotillomania",
      "This results from hair pulling and does not produce tapered hairs."],
     ["Tinea capitis",
      "This produces scaling patches with hairs broken close to the scalp."]],
   c=0, cite=c(139)),

 dict(topic="Alopecia areata", io=IOC,
   q="A 35-year-old man has patchy hair loss with an unusual scarred appearance in one area and diffuse atypical loss elsewhere, and the picture remains unclear after dermoscopy. Which is the most appropriate next step?",
   opts=[
     ["Scalp biopsy",
      "Correct — biopsy is performed when scarring alopecia, diffuse atypical loss or persistent diagnostic uncertainty remains after clinical and dermoscopic assessment."],
     ["Begin intralesional corticosteroids empirically",
      "Treating before establishing the diagnosis risks missing a scarring alopecia."],
     ["Begin topical minoxidil",
      "This treats androgenetic alopecia and would not clarify the diagnosis."],
     ["Repeat dermoscopy in six months",
      "Delay is not appropriate when scarring alopecia is a possibility."]],
   c=0, cite=c(139)),

 dict(topic="Irritant contact dermatitis", io=IOC,
   q="A 38-year-old woman has a glazed, well-demarcated dermatitis over both eyelids that began after she started using a new cosmetic. Which is the most likely diagnosis?",
   opts=[
     ["Irritant contact dermatitis",
      "Correct — the eyelids and face are among the commonest sites, from makeup and masks, and the glazed well-demarcated appearance fits."],
     ["Atopic dermatitis",
      "Adult atopic dermatitis can involve the eyelids but would not be sharply demarcated to the exposure area with this onset."],
     ["Seborrhoeic dermatitis",
      "This produces greasy yellow scale in sebum-rich areas."],
     ["Perioral dermatitis",
      "This produces monomorphic papules around the mouth with sparing of the vermilion border."]],
   c=0, cite=c(81)),

 dict(topic="Pityriasis rosea", io=IOC,
   q="A 23-year-old man has an oval scaly plaque on his chest that appeared ten days ago, and now smaller oval lesions are spreading down his trunk. Which is the most appropriate initial diagnostic approach?",
   opts=[
     ["Clinical diagnosis based on the herald patch and the typical pattern",
      "Correct — the herald patch and cleavage-line distribution are enough."],
     ["Skin biopsy of the herald patch",
      "Biopsy is not required when the pattern is typical."],
     ["Potassium hydroxide preparation of the herald patch",
      "This excludes tinea but the herald patch and subsequent pattern are diagnostic."],
     ["Serum rapid plasma reagin",
      "Syphilis is not among the differentials this lecture raises."]],
   c=0, cite=c(171)),

 dict(topic="Bullous pemphigoid", io=IOC,
   q="An 82-year-old woman has had several weeks of intense itching with urticarial plaques but no blisters. She is otherwise well. Which is the most likely explanation?",
   opts=[
     ["The prodromal phase of bullous pemphigoid, which may precede bullae by weeks to months",
      "Correct — the prodrome presents as pruritic urticarial or oedematous lesions before the blistering phase."],
     ["Chronic urticaria unrelated to blistering disease",
      "Possible in isolation, but the age and the described prodrome point to pemphigoid."],
     ["Early pemphigus vulgaris",
      "Pemphigus usually begins with oral lesions rather than an urticarial prodrome."],
     ["Lichen simplex chronicus",
      "This produces a localised lichenified plaque from scratching."]],
   c=0, cite=c(123)),

 dict(topic="Allergic contact dermatitis", io=IOC,
   q="A 35-year-old woman develops an itchy eruption under a new necklace and beneath the button of her jeans. Which allergen is most likely?",
   opts=[
     ["Nickel",
      "Correct — nickel is the most common metal allergen, and eruptions reproduce the shape of the item worn."],
     ["Urushiol",
      "Urushiol causes linear vesicles from plant contact rather than jewellery-shaped eruptions."],
     ["Neomycin",
      "This is a common topical antibiotic allergen rather than a metal one."],
     ["Bacitracin",
      "This is also a topical antibiotic allergen."]],
   c=0, cite=c(85)),

 dict(topic="Psoriasis", io=IOC,
   q="A 29-year-old man with plaque psoriasis develops new plaques along a surgical scar several weeks after an operation. Which phenomenon does this represent?",
   opts=[
     ["Koebner's phenomenon",
      "Correct — the development of lesions at sites of trauma, seen in psoriasis and also in lichen planus."],
     ["The Auspitz sign",
      "That is pinpoint bleeding on removal of scale."],
     ["A positive Nikolsky sign",
      "That is sloughing of the top skin layers on rubbing, seen in pemphigus."],
     ["Wickham's striae",
      "Those are fine white lines on the surface of lichen planus plaques."]],
   c=0, cite=c(159)),

 dict(topic="Dyshidrotic eczema", io=IOC,
   q="A 31-year-old woman with recurrent palmar vesicles asks how to reduce flares. Which is the most appropriate counselling point?",
   opts=[
     ["Avoid irritants such as detergents, solvents and hair dyes, wash with lukewarm water and soap-free cleanser, dry hands thoroughly, and apply emollients immediately afterwards",
      "Correct — trigger avoidance and barrier care are the named education points."],
     ["Wash hands frequently with antibacterial soap to prevent secondary infection",
      "Frequent washing with detergents is itself an irritant exposure."],
     ["Use hot water to relieve the itching",
      "Lukewarm water is advised."],
     ["Apply emollients only when the skin feels dry",
      "Emollients are applied immediately after drying and as often as possible."]],
   c=0, cite=c(66)),

 dict(topic="Lichen planus", io=IOC,
   q="A 58-year-old man develops an itchy violaceous papular eruption on his wrists two months after starting a new antihypertensive. Which is the most appropriate next step?",
   opts=[
     ["Review the medication list, since several drugs produce lichenoid reactions",
      "Correct — nonsteroidal anti-inflammatory drugs, sulfonamides, tetracyclines, hydrochlorothiazide, quinidine and some beta blockers are named."],
     ["Begin superpotent topical steroids without further history",
      "Treating without identifying a drug trigger risks missing the cause."],
     ["Test for hepatitis C and treat it to clear the rash",
      "Incidence may be increased in hepatitis C, but a causal relationship has never been established."],
     ["Reassure that the eruption is self-limited and needs no action",
      "Lichen planus is a chronic inflammatory condition rather than self-limited."]],
   c=0, cite=c(173)),
]
