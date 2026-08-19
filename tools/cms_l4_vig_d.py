# CMS I Lecture 4 (Cutaneous Bacterial Infections) — SET 2, vignette pool D.
#
# A corrective pool. Pools A to C came out 19 diagnosis / 17 education /
# 13 treatment / 5 next step / 4 test across 62 questions, which is only 62 for
# 60 slots and leaves the partition almost no freedom -- a form could land at
# exactly 40% diagnosis and trip the skew guard. This pool is deliberately
# weighted to "next step" and "which test" lead-ins across the topics the
# earlier pools covered thinnest.
#
# Options drafted at matched lengths. Correct answer is ALWAYS written first.
SRC = "4.  Cutaneous Bacterial Infections.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis for cutaneous bacterial infections"
IOB = "Objective b — Unique considerations of methicillin-resistant Staphylococcus aureus skin infections"
IOC = "Objective c — Differentiate primary from secondary bacterial infection of the skin"
IOD = "Objective d — Medical care strategies across infant, adolescent, adult and elderly populations"

POOL_D = [
 dict(topic="Acne vulgaris", io=IOA,
   q="A 21-year-old woman with moderate acne has had no improvement on a topical retinoid, benzoyl peroxide and four months of doxycycline. She has regular periods and no hirsutism. Which is the most appropriate next step?",
   opts=[
     ["Consider a combined oral contraceptive pill, since the acne is unresponsive to both topical and oral therapy",
      "Correct — that is one of the two stated indications for hormonal therapy."],
     ["Extend the doxycycline course to twelve months to give the antibiotic time to work",
      "Oral courses are kept to three to four months to limit resistance."],
     ["Add a second topical antibiotic to the regimen without any benzoyl peroxide",
      "Adding an antibiotic without benzoyl peroxide increases resistance risk."],
     ["Reassure her that acne always resolves by the mid-twenties without treatment",
      "Post-adolescent acne is specifically more common in women over 25."]],
   c=0, cite=c(28)),

 dict(topic="Acne vulgaris", io=IOA,
   q="A 18-year-old man with severe nodular acne has failed a topical retinoid with an oral antibiotic and benzoyl peroxide. Which test is required before the next treatment is started?",
   opts=[
     ["A pregnancy test is not needed for him, but iPledge enrolment of the prescriber is required",
      "Correct — isotretinoin requires prescriber enrolment and a one-month supply at a time."],
     ["A bacterial culture of a nodule, to confirm that Cutibacterium acnes is still present",
      "Culture is considered when acne fails to respond, not before isotretinoin."],
     ["A fasting insulin and lipid panel, to identify the insulin resistance driving the acne",
      "Insulin resistance is a possible predisposing factor rather than a required test."],
     ["A skin biopsy of a nodular lesion, to exclude an alternative inflammatory disease",
      "Biopsy has no role in the routine diagnosis or treatment of acne."]],
   c=0, cite=c(30)),

 dict(topic="Folliculitis", io=IOA,
   q="A 36-year-old woman has folliculitis of the thighs that has not cleared after two weeks of topical clindamycin. Which is the most appropriate next step?",
   opts=[
     ["Unroof a pustule for Gram stain and culture, since this is now a resistant case",
      "Correct — culture, potassium hydroxide mount, nasal swab and biopsy are all available."],
     ["Switch to a different topical antibiotic and review again in a further two weeks",
      "Rotating topicals without identifying the organism delays the diagnosis."],
     ["Begin oral isotretinoin, since follicular disease unresponsive to topicals needs it",
      "Isotretinoin is a treatment for acne rather than folliculitis."],
     ["Reassure and stop treatment, since folliculitis resolves without any intervention",
      "Resistant cases are specifically worked up rather than left."]],
   c=0, cite=c(44)),

 dict(topic="Hidradenitis suppurativa", io=IOA,
   q="A 33-year-old woman has axillary nodules and sinuses. The diagnosis of hidradenitis suppurativa is being considered. Which test is required to confirm it?",
   opts=[
     ["None — it is a clinical diagnosis resting on lesions, distribution and recurrence",
      "Correct. Biopsy is not usually required, though it shows follicular occlusion and apocrine gland destruction."],
     ["Bacterial culture of the draining material, since the causative organism guides treatment",
      "Culture is not among the three diagnostic elements."],
     ["Punch biopsy of an active nodule, since the histology is what establishes the diagnosis",
      "Biopsy is not usually required to make the diagnosis."],
     ["Wood's lamp examination of the axilla, looking for the coral-red fluorescence",
      "That fluorescence identifies erythrasma."]],
   c=0, cite=c(74)),

 dict(topic="Impetigo", io=IOD,
   q="A 7-year-old boy has impetigo covering much of one arm and both cheeks, too extensive for topical therapy. He has no drug allergies. Which is the most appropriate treatment?",
   opts=[
     ["Oral cephalexin, the drug of choice in children",
      "Correct. Clindamycin is used where there is penicillin allergy."],
     ["Oral doxycycline, which covers both likely organisms",
      "Doxycycline is limited to children over eight years old."],
     ["Oral ciprofloxacin, which covers resistant organisms",
      "Ciprofloxacin is named for resistant Pseudomonas folliculitis."],
     ["Oral fluconazole, which covers candidal superinfection",
      "Impetigo is bacterial rather than fungal."]],
   c=0, cite=c(95)),

 dict(topic="Erysipelas", io=IOA,
   q="A 74-year-old man is being treated for erysipelas of the leg. Which is the most appropriate supportive management alongside the antibiotic?",
   opts=[
     ["Symptomatic treatment of aches and fever, hydration, cold compresses and elevation of the limb",
      "Correct — prompt treatment matters because progression can be rapid."],
     ["Warm soaks three times daily with incision if any purulent material has collected",
      "That is the management of acute paronychia."],
     ["Compression bandaging applied from the toes to the knee for the first week",
      "Elevation rather than compression is what the lecture names."],
     ["Dilute acetic acid compresses applied for twenty minutes several times daily",
      "That treats Pseudomonas folliculitis."]],
   c=0, cite=c(104)),

 dict(topic="Cellulitis", io=IOA,
   q="A 59-year-old woman with cellulitis of the leg still has a fever of 38.6 degrees Celsius after fifty-four hours of oral antibiotics. Which is the most appropriate next step?",
   opts=[
     ["Change the antimicrobial therapy, guided by the culture results",
      "Correct — fever beyond forty-eight hours is the stated trigger for a change."],
     ["Continue the same antibiotic, since inflammation resolves over two weeks",
      "Slow resolution of inflammation is expected but persistent fever is not."],
     ["Stop the antibiotic and observe, since the fever may be drug related",
      "Stopping treatment in active cellulitis is not appropriate."],
     ["Add a topical antibiotic to the affected area alongside the oral one",
      "Topical therapy does not address deeper dermal infection."]],
   c=0, cite=c(112)),

 dict(topic="Cellulitis", io=IOA,
   q="A 70-year-old immunocompromised man has extensive cellulitis of the leg with systemic signs. Which investigations are appropriate?",
   opts=[
     ["Blood cultures, punch biopsy, complete blood count and creatine phosphokinase",
      "Correct, with imaging considered for underlying fasciitis or osteomyelitis."],
     ["No investigations, since cellulitis is a clinical diagnosis in every patient",
      "That applies only to limited disease in a patient without risk factors."],
     ["Wood's lamp examination and a potassium hydroxide preparation of the skin",
      "Those tests belong to erythrasma and dermatophyte infection."],
     ["Nasal swab for staphylococcal carriage and a plucked hair for dermatophytes",
      "Those tests belong to the resistant folliculitis workup."]],
   c=0, cite=c(109)),

 dict(topic="Necrotizing fasciitis", io=IOA,
   q="A 52-year-old man with suspected necrotizing fasciitis is being prepared for theatre. Which laboratory studies should be sent?",
   opts=[
     ["Complete blood count with differential, chemistry, arterial blood gas, urinalysis, and blood and tissue cultures",
      "Correct — they are sent, but they must not delay the surgical intervention itself."],
     ["Complete blood count and inflammatory markers only, since the rest add nothing to management",
      "The listed panel is broader than that."],
     ["Antistreptolysin O titre and throat culture, since Group A streptococcus is a common cause",
      "That workup belongs to erythema nodosum in the previous lecture."],
     ["No laboratory studies at all, since none of them changes the operative decision here",
      "Studies are sent; they simply do not delay surgery."]],
   c=0, cite=c(128)),

 dict(topic="Primary vs secondary infection", io=IOC,
   q="A 15-year-old boy with untreated acne develops tender fluctuant nodules with purulent drainage over the same areas. Which best describes what has happened?",
   opts=[
     ["A secondary bacterial infection has developed within skin already affected by acne",
      "Correct — secondary infection arises in skin damaged by an existing condition."],
     ["A primary bacterial infection has arisen in previously normal and intact skin",
      "The acne-affected skin is the pre-existing lesion here."],
     ["The acne has progressed to its nodular form without any additional infection",
      "Purulent drainage from fluctuant nodules indicates infection."],
     ["A foreign body reaction to hair has developed within the affected follicles",
      "That describes pseudofolliculitis barbae."]],
   c=0, cite=c(56)),
]
