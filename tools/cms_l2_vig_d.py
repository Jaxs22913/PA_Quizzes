# CMS I Lecture 2 (General Dermatology I) — SET 2, vignette pool D.
#
# Added after the 2026-08-19 lecture recording. Professor Jaquith spent real time
# on recognising these conditions across skin types, and said plainly that the
# textbook descriptions students are tested on are written for Caucasian skin.
# Set 2 had no vignette where skin tone changes what the examiner sees, so these
# fill that gap. She also worked four practice vignettes in class and said "these
# are like how your PANCE-style questions will be" -- the shape here follows them.
#
# Facts come from "2. General Dermatology I.pptx". Correct answer written first.
SRC = "2. General Dermatology I.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOC = "c — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of dermatological conditions"

POOL_D = [
 dict(topic="Stasis dermatitis", io=IOC,
   q="A 68-year-old woman with deeply pigmented skin has months of itching and swelling of both lower legs. The gaiter regions show poorly demarcated violaceous-to-deep-brown patches, and on palpation both areas are warm and boggy. Which is the most likely diagnosis?",
   opts=[
     ["Stasis dermatitis",
      "Correct — on darker skin the erythema reads as violaceous, grey or brown, so palpation for warmth and oedema carries the diagnosis."],
     ["Bilateral cellulitis of the lower legs",
      "Cellulitis is essentially never bilateral, and it is acute and febrile."],
     ["Allergic contact dermatitis to a topical product",
      "That would be sharply marginated in the shape of the exposure."],
     ["Nummular eczema of both lower extremities",
      "That produces discrete coin-shaped plaques rather than confluent patches."]],
   c=0, cite=c(114)),

 dict(topic="Atopic dermatitis", io=IOC,
   q="A 9-year-old boy with darker skin has a chronic itchy eruption in both antecubital and popliteal fossae. The plaques look silvery rather than red, with excoriation and thickened skin markings. His mother has asthma. Which is the most likely diagnosis?",
   opts=[
     ["Atopic dermatitis",
      "Correct — flexural distribution with a family history of atopy; on darker skin the plaques can appear almost silvery instead of inflamed."],
     ["Plaque psoriasis of the flexures",
      "Psoriasis favours extensor surfaces and produces thick silvery scale on well-demarcated plaques."],
     ["Tinea corporis of both flexures",
      "That would have an advancing scaly border and be potassium hydroxide positive."],
     ["Lichen simplex chronicus at both sites",
      "That follows a sustained itch-scratch cycle at a site the patient can reach."]],
   c=0, cite=c(53)),

 dict(topic="Skin type recognition", io=IOC,
   q="A 34-year-old man with deeply pigmented skin has a warm, tender, swollen forearm. The examiner cannot appreciate any erythema. Which is the most appropriate approach?",
   opts=[
     ["Rely on palpation, distribution and secondary change, since erythema is an unreliable signal on darker skin",
      "Correct — the finding is present but the colour cue is not."],
     ["Conclude that inflammation is absent, since visible erythema is required in order to diagnose it",
      "Absence of visible erythema does not mean absence of inflammation."],
     ["Perform a Wood's lamp examination to bring out the erythema in a dark room",
      "A Wood's lamp evaluates pigment change and selected infections, not erythema."],
     ["Take a punch biopsy immediately, since clinical assessment cannot be relied on",
      "The clinical assessment is still valid; it just cannot lean on colour."]],
   c=0, cite=c(114)),

 dict(topic="Pityriasis rosea", io=IOC,
   q="A 24-year-old woman with darker skin had a single large oval patch on the trunk two weeks ago, followed by smaller oval lesions along the skin lines. The eruption is now fading but leaving brown marks. Which is the most appropriate counselling point?",
   opts=[
     ["Post-inflammatory hyperpigmentation is common here and can last several months, but it does resolve",
      "Correct — the eruption itself is self-limiting and leaves no scar."],
     ["The brown marks are permanent and will require long-term treatment with a depigmenting agent",
      "The hyperpigmentation is post-inflammatory and settles over months."],
     ["The brown marks mean the eruption was misdiagnosed and a biopsy is now needed",
      "Post-inflammatory pigment change is expected rather than a diagnostic problem."],
     ["The brown marks indicate secondary infection and need a topical antibiotic",
      "There is no described purulence, warmth or crusting."]],
   c=0, cite=c(169)),

 dict(topic="Pharmacology", io=IOC,
   q="A 29-year-old woman has a mildly inflamed eczematous patch on the eyelid and another on the vulva. Which topical corticosteroid is most appropriate?",
   opts=[
     ["Hydrocortisone, or another low potency agent",
      "Correct — potency is chosen by site, and these are the thinnest skin in the body."],
     ["Clobetasol propionate 0.05%, for a short course",
      "A high potency agent on eyelid and genital skin risks atrophy."],
     ["Betamethasone dipropionate 0.05% twice daily",
      "That agent sits in the medium to high tier."],
     ["Triamcinolone acetonide 0.1% twice daily",
      "That agent sits in the medium to high tier."]],
   c=0, cite=c(42)),

 dict(topic="Pharmacology", io=IOC,
   q="A 41-year-old man has thick psoriatic plaques on both elbows that have not responded to a moderate potency steroid. Which agent from the potency table is the highest available?",
   opts=[
     ["Clobetasol propionate 0.05%",
      "Correct — it is the only agent in the high potency tier on this table."],
     ["Betamethasone valerate 0.1%",
      "That sits in the medium to high tier."],
     ["Betamethasone dipropionate 0.05%",
      "That sits in the medium to high tier."],
     ["Triamcinolone acetonide 0.1%",
      "That sits in the medium to high tier."]],
   c=0, cite=c(42)),

 dict(topic="Diagnostic tools", io=IOC,
   q="A 52-year-old man has a purulent wound and the clinician wants to know both what is growing and what will treat it. Which test should be ordered?",
   opts=[
     ["Bacterial culture and sensitivity",
      "Correct — the culture names the organism and the sensitivity directs the antibiotic."],
     ["Fungal culture of the wound surface",
      "That identifies fungal organisms rather than bacteria."],
     ["Potassium hydroxide wet preparation",
      "That detects fungal elements in skin, hair or nail."],
     ["Tzanck smear of the wound base",
      "That is a rapid evaluation for herpesvirus changes."]],
   c=0, cite=c(29)),

 dict(topic="Diagnostic tools", io=IOC,
   q="A 47-year-old woman has a soft subcutaneous nodule on the forearm and the clinician wants to know whether it is fluid-filled. Which bedside technique addresses that?",
   opts=[
     ["Transillumination",
      "Correct — a fluid-filled lesion glows when a light is placed against it."],
     ["Dermoscopy",
      "That magnifies the surface and pigment pattern."],
     ["Diascopy with a Wood's lamp",
      "A Wood's lamp evaluates pigment change and selected infections."],
     ["Mineral oil preparation",
      "That identifies the scabies mite, its eggs or its faecal pellets."]],
   c=0, cite=c(25)),
]
