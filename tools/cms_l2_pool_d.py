# CMS I Lecture 2 (General Dermatology I) — SET 1 pool D.
#
# Built from the 2026-08-19 lecture recording, after the first three pools had
# already shipped. Every question here covers something Professor Jaquith spent
# time on out loud that pools A to C did not reach, or that she named as
# something she would write a question about.
#
# Facts are taken from "2. General Dermatology I.pptx", NOT from the transcript.
# Automatic speech recognition mis-heard betamethasone dipropionate 0.05% as
# "0.5%", which is exactly why the slide is the authority and the recording only
# tells you what to weight.
#
# Deliberately EXCLUDED, because she said so in as many words: the NAAT / RT-PCR
# / qPCR / multiplex taxonomy on slides 30 and 31 -- "this is not going to be on
# your exam" -- and any question that would require interpreting an image.
#
# Options drafted at matched lengths. Correct answer is ALWAYS written first.
SRC = "2. General Dermatology I.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOC = "Objective c — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of dermatological conditions"

POOL_D = [
 # ---- topical corticosteroid potency: she said outright she would ask this
 dict(topic="Pharmacology", io=IOC,
   q="Which topical corticosteroid is classified as mild?",
   opts=[
     ["Hydrocortisone, at all strengths",
      "Correct — 0.1%, 0.5%, 1% and 2.5% all sit in the mild tier."],
     ["Triamcinolone acetonide 0.1%",
      "That is in the medium to high tier."],
     ["Betamethasone valerate 0.1%",
      "That is in the medium to high tier."],
     ["Clobetasol propionate 0.05%",
      "That is the high potency agent."]],
   c=0, cite=c(42)),

 dict(topic="Pharmacology", io=IOC,
   q="Which topical corticosteroid is classified as moderate potency?",
   opts=[
     ["Betamethasone valerate 0.025%",
      "Correct — the same salt at 0.1% moves up to medium to high."],
     ["Betamethasone dipropionate 0.05%",
      "That is in the medium to high tier."],
     ["Hydrocortisone 2.5% applied twice daily",
      "Hydrocortisone is mild at every strength."],
     ["Clobetasol propionate 0.05% ointment",
      "That is the high potency agent."]],
   c=0, cite=c(42)),

 dict(topic="Pharmacology", io=IOC,
   q="Which three agents make up the medium to high potency tier?",
   opts=[
     ["Triamcinolone acetonide 0.1%, betamethasone valerate 0.1% and betamethasone dipropionate 0.05%",
      "Correct. Betamethasone appears twice here, in two different salts."],
     ["Hydrocortisone 2.5%, betamethasone valerate 0.025% and clobetasol propionate 0.05%",
      "Those are the mild, moderate and high agents respectively."],
     ["Triamcinolone acetonide 0.1%, hydrocortisone 1% and clobetasol propionate 0.05%",
      "Hydrocortisone is mild and clobetasol is high."],
     ["Betamethasone valerate 0.025%, tazarotene 0.1% and adapalene 0.1% preparations",
      "The last two are retinoids rather than corticosteroids."]],
   c=0, cite=c(42)),

 dict(topic="Pharmacology", io=IOC,
   q="Which topical corticosteroid should be chosen for a sensitive site such as the face or the genitals?",
   opts=[
     ["Hydrocortisone, or another low potency agent",
      "Correct — potency is selected according to site as well as severity."],
     ["Clobetasol propionate, for a shorter course",
      "A high potency agent on thin skin risks atrophy."],
     ["Betamethasone dipropionate, at half strength",
      "That agent sits in the medium to high tier."],
     ["Triamcinolone acetonide, applied once daily",
      "That agent sits in the medium to high tier."]],
   c=0, cite=c(42)),

 dict(topic="Pharmacology", io=IOC,
   q="Two betamethasone preparations appear on the potency table in different tiers. What distinguishes them?",
   opts=[
     ["The salt and the concentration together — valerate 0.025% is moderate, valerate 0.1% and dipropionate 0.05% are medium to high",
      "Correct. Concentration alone does not tell you which tier an agent belongs to."],
     ["The concentration alone — any preparation below 0.05% is moderate and anything at or above it is medium to high",
      "Dipropionate at 0.05% is medium to high while valerate at 0.025% is moderate."],
     ["The formulation alone — cream preparations are moderate and ointment preparations are medium to high",
      "The table is organised by agent and strength, not by vehicle."],
     ["The indication alone — eczema preparations are moderate and psoriasis preparations are medium to high",
      "Potency is a property of the agent rather than the indication."]],
   c=0, cite=c(42)),

 # ---- cultures, slide 29: not previously covered
 dict(topic="Diagnostic tools", io=IOC,
   q="What does a bacterial culture and sensitivity tell you that a plain culture does not?",
   opts=[
     ["Which antibiotic works best against the organism that was grown",
      "Correct — the culture identifies the organism and the sensitivity directs therapy."],
     ["Which fungal organism is present alongside the bacterial one",
      "That is the role of a separate fungal culture."],
     ["How much genetic material of the pathogen is present in the sample",
      "That is what a quantitative molecular test measures."],
     ["Whether the organism is part of the patient's normal skin flora",
      "Culture and sensitivity does not make that distinction."]],
   c=0, cite=c(29)),

 dict(topic="Diagnostic tools", io=IOC,
   q="What is a fungal culture used for?",
   opts=[
     ["Identifying the specific fungal organism",
      "Correct. A bacterial culture with sensitivity does the equivalent job for bacteria."],
     ["Distinguishing a dermatophyte from a yeast without any growth",
      "Culture requires growth to identify the organism."],
     ["Measuring how much fungal genetic material is in the sample",
      "That is what a quantitative molecular test measures."],
     ["Determining which antifungal agent will work best clinically",
      "Sensitivity testing is described for bacterial rather than fungal culture here."]],
   c=0, cite=c(29)),

 # ---- diagnostic tools she mentioned that pools A-C missed
 dict(topic="Diagnostic tools", io=IOC,
   q="What does transillumination distinguish?",
   opts=[
     ["Whether a nodule is fluid-filled or solid",
      "Correct — a fluid-filled lesion glows when a light is placed against it."],
     ["Whether a pigmented lesion is benign or malignant",
      "That is the role of dermoscopy and biopsy."],
     ["Whether a scaling lesion is fungal or bacterial",
      "That is the role of potassium hydroxide preparation and culture."],
     ["Whether a blister is subepidermal or intraepidermal",
      "That distinction is made on biopsy with immunofluorescence."]],
   c=0, cite=c(25)),

 dict(topic="Diagnostic tools", io=IOC,
   q="What is direct immunofluorescence used to diagnose in this lecture?",
   opts=[
     ["Autoimmune blistering disease, by showing where antibody is deposited in the skin",
      "Correct — it is what separates bullous pemphigoid from pemphigus on a biopsy."],
     ["Dermatophyte infection, by showing fungal elements within the stratum corneum",
      "That is the role of potassium hydroxide preparation."],
     ["Herpesvirus infection, by showing multinucleated giant cells in a smear",
      "That is the Tzanck smear."],
     ["Scabies infestation, by showing the mite, its eggs or its faecal pellets",
      "That is the mineral oil preparation."]],
   c=0, cite=c(34)),

 dict(topic="Diagnostic tools", io=IOC,
   q="What is a dermatoscope used for?",
   opts=[
     ["Magnified examination of a lesion's surface and pigment pattern",
      "Correct — it is the first-line tool for evaluating a pigmented lesion."],
     ["Rapid bedside identification of a mite and its eggs in oil",
      "That is the mineral oil preparation."],
     ["Detection of fungal elements after dissolving keratin in alkali",
      "That is the potassium hydroxide preparation."],
     ["Measurement of the amount of viral genetic material present",
      "That is what a quantitative molecular test measures."]],
   c=0, cite=c(24)),

 # ---- recognising disease across skin types: she spent 90 seconds on this
 dict(topic="Skin type recognition", io=IOC,
   q="How does erythema of stasis dermatitis appear in patients with darker skin tones?",
   opts=[
     ["Violaceous, grey or deep brown, so palpation is needed to find warmth and oedema",
      "Correct — colour becomes an unreliable signal and the examination has to change."],
     ["Brighter and more sharply red, making the affected area easier to delineate",
      "Erythema is harder rather than easier to appreciate on darker skin."],
     ["Completely absent, so the diagnosis cannot be made without a skin biopsy",
      "The changes are present but appear in different colours."],
     ["Silvery and scaling, which is what distinguishes it from venous ulceration",
      "That silvery appearance is described for atopic dermatitis."]],
   c=0, cite=c(114)),

 dict(topic="Skin type recognition", io=IOC,
   q="How can atopic dermatitis appear differently across skin tones?",
   opts=[
     ["Angry and inflamed on lighter skin, but almost silvery on darker skin",
      "Correct — the underlying disease is the same but the visual signal is not."],
     ["Silvery on lighter skin, but angry and inflamed on darker skin",
      "That reverses the two descriptions."],
     ["Identical on all skin tones, since the eruption is defined by its distribution",
      "Distribution helps, but the appearance genuinely differs."],
     ["Violaceous on lighter skin, but hypopigmented on darker skin in every case",
      "That is not how the difference is described."]],
   c=0, cite=c(53)),

 dict(topic="Skin type recognition", io=IOC,
   q="Which residual change is particularly common after pityriasis rosea in darker-skinned individuals?",
   opts=[
     ["Post-inflammatory hyperpigmentation lasting several months",
      "Correct — the eruption itself still resolves without scarring."],
     ["Permanent depigmentation of the affected areas of the trunk",
      "The change is hyperpigmentation and it is not permanent."],
     ["Atrophic scarring along the lines of the original lesions",
      "Pityriasis rosea resolves without scarring."],
     ["Persistent silvery scale over the site of the herald patch",
      "Scale resolves with the eruption."]],
   c=0, cite=c(169)),

 dict(topic="Skin type recognition", io=IOC,
   q="Which examination approach is most reliable when erythema is difficult to appreciate on darker skin?",
   opts=[
     ["Palpation for warmth and oedema, with attention to distribution and secondary change",
      "Correct — colour stops being the primary signal, so the other findings carry the diagnosis."],
     ["Wood's lamp examination of every affected area in a darkened room",
      "That is used for selected fungal and bacterial infections and for pigment change."],
     ["Immediate skin biopsy of the affected area, since clinical diagnosis is unreliable",
      "Most of these conditions remain clinical diagnoses."],
     ["Potassium hydroxide preparation from the affected area in every patient",
      "That test addresses fungal infection specifically."]],
   c=0, cite=c(114)),

 dict(topic="Skin type recognition", io=IOC,
   q="Which scale classifies skin type by its response to ultraviolet light?",
   opts=[
     ["The Fitzpatrick scale",
      "Correct — six types, from always burns and never tans through to never burns."],
     ["The SCORTEN score",
      "That estimates mortality in toxic epidermal necrolysis."],
     ["The Auspitz sign",
      "That is a physical finding in psoriasis, not a scale."],
     ["The Nikolsky sign",
      "That is a physical finding in blistering disease, not a scale."]],
   c=0, cite=c(53)),

 # ---- points she returned to
 dict(topic="Atopic dermatitis", io=IOC,
   q="What is the atopic triad?",
   opts=[
     ["Atopic dermatitis, asthma and allergic rhinitis",
      "Correct — a personal or family history of atopy is central to the diagnosis."],
     ["Atopic dermatitis, urticaria and food allergy",
      "Those are associated but are not the three named."],
     ["Asthma, allergic rhinitis and chronic sinusitis",
      "Atopic dermatitis is one of the three."],
     ["Atopic dermatitis, psoriasis and seborrhoeic dermatitis",
      "The last two are unrelated to atopy."]],
   c=0, cite=c(52)),

 dict(topic="Psoriasis", io=IOC,
   q="Which supplement must accompany methotrexate?",
   opts=[
     ["Folic acid",
      "Correct — supplementation is given with methotrexate in every case."],
     ["Vitamin B12",
      "That is not the supplement given with methotrexate."],
     ["Vitamin D",
      "That is not the supplement given with methotrexate."],
     ["Iron",
      "That is not the supplement given with methotrexate."]],
   c=0, cite=c(163)),

 dict(topic="Lichen planus", io=IOC,
   q="What does a biopsy show in lichen planus?",
   opts=[
     ["A band-like infiltration of lymphocytes in the dermis",
      "Correct — a classic descriptive phrase worth recognising on sight."],
     ["Full-thickness epidermal necrosis with junctional separation",
      "That is Stevens-Johnson syndrome and toxic epidermal necrolysis."],
     ["Granular immunoglobulin A deposits at the dermal papillae",
      "That is dermatitis herpetiformis."],
     ["Subepidermal separation with linear immunoglobulin G at the basement membrane",
      "That is bullous pemphigoid."]],
   c=0, cite=c(177)),

 dict(topic="Pharmacology", io=IOC,
   q="How should a topical retinoid be started, and which areas are avoided?",
   opts=[
     ["Begin at the lowest strength and build up toward nightly use, avoiding eyes, nose and mouth",
      "Correct — irritation, dryness and photosensitivity are the reasons to titrate."],
     ["Begin at the highest strength twice daily and reduce once the skin has settled",
      "Starting high causes the irritation that makes patients stop."],
     ["Begin nightly at full strength but restrict use to the face and neck only",
      "The titration is what matters, and the face is where care is needed."],
     ["Begin weekly and increase only if there has been no response after six months",
      "That is slower than the described approach."]],
   c=0, cite=c(44)),
]
