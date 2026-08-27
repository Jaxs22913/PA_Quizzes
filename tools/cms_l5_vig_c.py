# CMS I Lecture 5 (Dermatological Infestations) — SET 2, vignette pool C.
# Ticks (Lyme disease, Rocky Mountain spotted fever), cercarial dermatitis, and
# the primary-versus-secondary lesion objective.
#
# Options drafted at matched lengths. Correct answer is ALWAYS written first
# (c=0); the partition script rotates.
SRC = "CMS I Dermatological Infestations - Shahsv.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of dermatological infestations"
IOB = "b — Differentiate primary from secondary skin lesions"
IOC = "c — Medical care strategies across infant, child, adolescent, adult and elderly populations"

POOL_C = [
 dict(topic="Lyme disease", io=IOA,
   q="A 41-year-old woman in Connecticut removed a tick from her thigh eight days ago. She now has a 9 cm round red patch there with a paler centre and a darker dot in the middle, plus fever and aching. Which is the most likely diagnosis?",
   opts=[
     ["Stage 1 Lyme disease with erythema migrans",
      "Correct — a lesion over 5 cm with central clearing about a week after the bite, with constitutional symptoms."],
     ["Cellulitis at the site of the tick bite",
      "That produces uniform expanding erythema without central clearing."],
     ["A local hypersensitivity reaction to tick saliva",
      "That would be smaller and would not carry systemic symptoms."],
     ["Early Rocky Mountain spotted fever",
      "That produces a rash on ankles and wrists after several days of fever."]],
   c=0, cite=c(72)),

 dict(topic="Lyme disease", io=IOA,
   q="A 44-year-old man has a classic erythema migrans lesion after a tick bite in Vermont. Which is the most appropriate next step?",
   opts=[
     ["Diagnose and treat him on clinical grounds without waiting for serology",
      "Correct — a patient with the lesion is treated clinically, and testing is most useful outside endemic regions."],
     ["Send an enzyme-linked immunosorbent assay and withhold treatment until it returns",
      "Delaying treatment for serology is not appropriate with this lesion."],
     ["Send a Western blot and treat only if the immunoglobulin G band is positive",
      "The lesion itself is the indication to treat."],
     ["Reassure and review in two weeks, since most tick bites need no treatment",
      "Antibiotics are indicated in all stages of Lyme disease."]],
   c=0, cite=c(77)),

 dict(topic="Lyme disease", io=IOC,
   q="A 9-year-old girl has early Lyme disease with erythema migrans. Which is the most appropriate oral antibiotic?",
   opts=[
     ["Amoxicillin",
      "Correct — it is the alternative first line for early disease in children and pregnant patients."],
     ["Doxycycline",
      "It is first line generally, but amoxicillin is the alternative in children and pregnancy."],
     ["Azithromycin",
      "Macrolides are second line for those who cannot tolerate other agents."],
     ["Ceftriaxone",
      "That is intravenous, used for particular later manifestations."]],
   c=0, cite=c(79)),

 dict(topic="Lyme disease", io=IOA,
   q="A 52-year-old man untreated for a tick bite three weeks ago now has a facial droop on one side, headache and a stiff neck. Which stage of Lyme disease is this?",
   opts=[
     ["Stage 2, early disseminated infection",
      "Correct — days to weeks later, with cranial nerve palsies, meningitis and radiculopathies."],
     ["Stage 1, early localised infection",
      "That is the erythema migrans lesion about a week after the bite."],
     ["Stage 3, late persistent infection",
      "That occurs months to years later with arthritis and encephalopathy."],
     ["A post-treatment inflammatory reaction",
      "He has not been treated."]],
   c=0, cite=c(74)),

 dict(topic="Lyme disease", io=IOA,
   q="A 57-year-old woman has a swollen painful knee that has come and gone over two years, plus memory difficulty and low mood. She recalls a rash after a tick bite three years ago that was never treated. Which is the most likely diagnosis?",
   opts=[
     ["Stage 3 Lyme disease, late persistent infection",
      "Correct — monoarticular arthritis of a weight-bearing joint with subacute encephalopathy."],
     ["Stage 2 Lyme disease, early disseminated infection",
      "That occurs days to weeks after the bite rather than years."],
     ["Rheumatoid arthritis with an unrelated mood disorder",
      "The history of an untreated erythema migrans lesion points elsewhere."],
     ["Chronic Rocky Mountain spotted fever sequelae",
      "That illness is acute and does not present this way years later."]],
   c=0, cite=c(75)),

 dict(topic="Lyme disease", io=IOA,
   q="A 48-year-old man with Lyme arthritis of the knee has not responded to a full course of oral doxycycline. Which is the most appropriate next step?",
   opts=[
     ["Intravenous ceftriaxone, cefotaxime or penicillin G",
      "Correct — intravenous therapy is used for arthritis and acrodermatitis chronica atrophicans."],
     ["A second oral course of doxycycline for a further fortnight",
      "Repeating the same oral course is not the described escalation."],
     ["Oral azithromycin, since a macrolide covers resistant organisms",
      "Macrolides are second line where other agents cannot be tolerated."],
     ["Intra-articular corticosteroid injection into the affected knee",
      "That does not treat the underlying infection."]],
   c=0, cite=c(80)),

 dict(topic="Lyme disease", io=IOA,
   q="A 36-year-old woman who hikes in an endemic area asks how to protect herself. Which is the most appropriate advice?",
   opts=[
     ["Avoid tick habitat, use DEET, PMD or picaridin reapplied about every two hours, and treat clothing with pyrethrins",
      "Correct — there is no human vaccine, though one exists for dogs."],
     ["Request the human Lyme vaccine, which is recommended for anyone living in an endemic region",
      "There is no human vaccine available."],
     ["Take prophylactic doxycycline through the summer months while she continues to hike",
      "Continuous prophylaxis is not among the described measures."],
     ["Rely on showering promptly after each hike, since this removes ticks before they attach",
      "Tick checks and repellents are what the lecture names."]],
   c=0, cite=c(80)),

 dict(topic="Rocky Mountain spotted fever", io=IOA,
   q="A 47-year-old man in rural Tennessee has had fever to 39.8 degrees Celsius and severe headache for four days. Today a blanching macular rash appeared on his ankles and wrists, including the palms and soles, sparing his face. Which is the most likely diagnosis?",
   opts=[
     ["Rocky Mountain spotted fever",
      "Correct — the triad of fever, headache and rash, with centripetal spread involving palms and soles."],
     ["Early Lyme disease with erythema migrans",
      "That is a single expanding lesion at the bite site."],
     ["A drug eruption from a recently started medication",
      "That would not follow this geography, timing and distribution."],
     ["Meningococcaemia with an early petechial rash",
      "That is not the differential this lecture develops here."]],
   c=0, cite=c(82)),

 dict(topic="Rocky Mountain spotted fever", io=IOA,
   q="A 50-year-old woman with suspected Rocky Mountain spotted fever is on day 4 of illness. The indirect immunofluorescence assay has been sent. Which is the most appropriate next step?",
   opts=[
     ["Start doxycycline now, since treatment should begin by day 5 and the assay is rarely diagnostic before day 7",
      "Correct — treatment must not wait for the serology to return."],
     ["Wait for the assay result, since the gold standard test should guide the choice of antibiotic",
      "Waiting would push treatment past the point at which it should begin."],
     ["Start amoxicillin now, since doxycycline should be reserved for confirmed disease",
      "Doxycycline is the treatment for this illness in all groups."],
     ["Repeat the assay in three days and treat only if it has become positive by then",
      "Delay of that kind is what the lecture warns against."]],
   c=0, cite=c(85)),

 dict(topic="Rocky Mountain spotted fever", io=IOC,
   q="A 6-year-old boy has suspected Rocky Mountain spotted fever. Which is the most appropriate treatment?",
   opts=[
     ["Doxycycline at 2.2 mg per kilogram by mouth twice daily for five to ten days",
      "Correct — it is used in children and pregnancy here, with desensitisation where contraindicated."],
     ["Amoxicillin at a weight-based dose by mouth for a course of fourteen days",
      "That substitution belongs to Lyme disease in children."],
     ["Azithromycin at a weight-based dose by mouth for a course of five days",
      "Macrolides are not the treatment for this illness."],
     ["Intravenous ceftriaxone at a weight-based dose for a course of ten days",
      "That is used for particular Lyme manifestations."]],
   c=0, cite=c(86)),

 dict(topic="Rocky Mountain spotted fever", io=IOA,
   q="A 55-year-old man from a rural area has fever, severe headache, nausea and calf pain for five days but no rash. Which is the most appropriate consideration?",
   opts=[
     ["Rocky Mountain spotted fever can present without a rash in about 20% of patients",
      "Correct — the full triad is present in only about 60% and the rash follows the fever."],
     ["The absence of rash excludes the diagnosis, so an alternative should be sought",
      "About one in five patients has no rash."],
     ["The rash always appears within twenty-four hours of the fever beginning",
      "The rash follows two to four days after fever onset."],
     ["Treatment should be withheld until a rash confirms the clinical diagnosis",
      "Treatment should begin by day 5, before serology or rash confirm it."]],
   c=0, cite=c(85)),

 dict(topic="Rocky Mountain spotted fever", io=IOA,
   q="A 39-year-old woman removed a tick after hiking in South Carolina and asks whether she should take an antibiotic to prevent Rocky Mountain spotted fever. Which is the most appropriate response?",
   opts=[
     ["Prophylactic antibiotic therapy is not recommended; prevention rests on avoidance, clothing, tick checks and DEET",
      "Correct — she should return if fever or headache develop."],
     ["A single dose of doxycycline should be taken now to prevent the illness developing",
      "Prophylaxis is specifically not recommended."],
     ["A five-day course of doxycycline should be started because the area is endemic",
      "Prophylaxis is specifically not recommended."],
     ["Serology should be sent now and prophylaxis started if it returns positive",
      "Serology is rarely diagnostic before day 7 of an actual illness."]],
   c=0, cite=c(86)),

 dict(topic="Rocky Mountain spotted fever", io=IOA,
   q="A 44-year-old man admitted with Rocky Mountain spotted fever has blood tests sent. Which pattern is expected?",
   opts=[
     ["Thrombocytopenia, anaemia, mild hyponatraemia and mild transaminitis with a normal white count and increased bands",
      "Correct — cerebrospinal fluid shows leukocytosis with moderately raised protein and normal glucose."],
     ["Leukocytosis with a left shift, raised inflammatory markers and a normal platelet count throughout",
      "The platelet count is characteristically low in this illness."],
     ["Eosinophilia with a raised immunoglobulin E level and otherwise normal chemistry",
      "That pattern is not described for this illness."],
     ["Entirely normal blood tests, with the diagnosis made on clinical grounds alone",
      "A characteristic laboratory pattern is described."]],
   c=0, cite=c(85)),

 dict(topic="Cercarial dermatitis", io=IOA,
   q="A 14-year-old boy swam in a Michigan lake yesterday. He felt prickling on his legs for about half an hour afterwards, then severe itching by bedtime, and today has red papules turning into small blisters. Which is the most likely diagnosis?",
   opts=[
     ["Cercarial dermatitis, also called swimmer's itch",
      "Correct — prickling for about 30 minutes, itch at 10 to 12 hours, papules within 24 hours."],
     ["Contact dermatitis from something in the lake water",
      "That would not follow this characteristic time course."],
     ["Cutaneous larva migrans from the sand at the shore",
      "That produces a serpentine trail that advances daily."],
     ["Flea bites acquired at the lakeside from an animal",
      "Those are clustered urticarial papules without this time course."]],
   c=0, cite=c(90)),

 dict(topic="Cercarial dermatitis", io=IOA,
   q="A 16-year-old girl with cercarial dermatitis has pain and swelling with the itch, worst about two days after exposure. Which is the most appropriate treatment?",
   opts=[
     ["Antihistamines, oatmeal baths, antipruritic lotions, aspirin for pain and topical or oral glucocorticoids",
      "Correct — the pain and swelling peak at 48 to 72 hours before settling."],
     ["Albendazole 400 mg by mouth daily for three days to clear the parasite from the skin",
      "That is the treatment for cutaneous larva migrans."],
     ["Overnight topical permethrin to the whole skin surface with a repeat dose at one week",
      "That is the treatment for scabies."],
     ["Oral doxycycline for ten days to cover the organism carried in the fresh water",
      "The cause is a flatworm larva rather than a bacterium."]],
   c=0, cite=c(91)),

 dict(topic="Cercarial dermatitis", io=IOA,
   q="A 45-year-old rice farmer working in flooded paddies has recurrent itchy papular eruptions on his legs each season. Which is the most likely diagnosis?",
   opts=[
     ["Cercarial dermatitis from repeated exposure to infested water",
      "Correct — paddy workers and rice farmers of the Far East are specifically named."],
     ["Tungiasis from walking barefoot in contaminated soil",
      "That produces enlarging papules and nodules on the feet."],
     ["Cutaneous larva migrans from soil contaminated with faeces",
      "That produces a single advancing serpentine track."],
     ["Body louse infestation from prolonged wear of the same clothing",
      "That produces linear excoriations on the back and waist."]],
   c=0, cite=c(89)),

 dict(topic="Primary and secondary lesions", io=IOB,
   q="A 33-year-old woman presents with a rash that shows discrete circumscribed papules and, in the older areas, crusting and scaling. Which conclusion follows from the crusting?",
   opts=[
     ["The epidermis has been affected",
      "Correct — crust and scale indicate epidermal involvement, which narrows the reaction pattern."],
     ["The infection is bacterial in origin",
      "Crust does not by itself indicate an infectious cause."],
     ["The lesions are resolving spontaneously",
      "Crusting does not indicate resolution."],
     ["The subcutaneous tissue is involved",
      "Deeper involvement is not what crust signals."]],
   c=0, cite=c(3)),

 dict(topic="Primary and secondary lesions", io=IOB,
   q="A 40-year-old man has an eruption whose reaction pattern has been recognised. Which characteristics are used next to narrow the differential?",
   opts=[
     ["Colour, shape, configuration of the lesions relative to one another, and their distribution on the body",
      "Correct — those tune the differential the reaction pattern has already generated."],
     ["Duration of the eruption, the patient's age, and whether any treatment has been tried so far",
      "Those are clinically useful but are not the named characteristics."],
     ["Culture and sensitivity of the lesion together with a complete blood count and chemistry",
      "Laboratory testing is not what refines the morphological differential."],
     ["Presence of pruritus, presence of pain, and whether regional lymph nodes are enlarged",
      "Symptoms and nodes are helpful but are not the named characteristics."]],
   c=0, cite=c(3)),
]

# Five more, added because pools A to C totalled 57 against 60 slots and the
# partition needs headroom. Weighted to the topics carrying only one or two
# questions and to the "next step" and "which test" lead-ins.
POOL_C += [
 dict(topic="Scabies", io=IOC,
   q="A 4-month-old infant has irritability, poor sleep and crusted indurated nodules on the trunk and in the skin folds, with excoriations extending onto the scalp and neck. Which is the most likely diagnosis?",
   opts=[
     ["Scabies",
      "Correct \u2014 infants, the elderly and the immunocompromised can have head and neck involvement, and infants get these nodules."],
     ["Atopic dermatitis of infancy",
      "That favours the cheeks and extensor surfaces and does not produce these nodules."],
     ["Seborrhoeic dermatitis, or cradle cap",
      "That produces greasy scale on the scalp without trunk nodules."],
     ["Bullous impetigo of the trunk and folds",
      "That produces tense bullae leaving collarettes."]],
   c=0, cite=c(7)),

 dict(topic="Hymenoptera", io=IOA,
   q="A 29-year-old man stung on the forearm three days ago has swelling extending from wrist to elbow with firm induration, but no urticaria elsewhere and no breathing difficulty. Which best describes this reaction?",
   opts=[
     ["A severe local reaction, with extensive oedema and induration lasting up to one week",
      "Correct \u2014 a generalised systemic reaction would involve urticaria, angio-oedema and bronchospasm."],
     ["A generalised systemic reaction, occurring in 0.4% to 3% of stings overall",
      "That requires findings away from the sting site."],
     ["A typical reaction, with immediate burning followed by local erythema and swelling",
      "The typical reaction does not extend the length of a limb for a week."],
     ["A secondary bacterial infection developing at the site of the original sting",
      "There is no described fever, purulence or spreading erythema."]],
   c=0, cite=c(43)),

 dict(topic="Brown recluse spider", io=IOA,
   q="A 36-year-old man bitten by a brown recluse two days ago has a darkening area at the site plus nausea, headache and chills. Which is the most appropriate interpretation?",
   opts=[
     ["Systemic symptoms develop one to two days after the bite and necrosis at two to three days",
      "Correct \u2014 eschar forms between days five and seven, then deep ulcers."],
     ["Systemic symptoms indicate secondary bacterial infection and need immediate antibiotics",
      "The timing fits the natural course of the envenomation itself."],
     ["Systemic symptoms this early exclude a brown recluse and suggest a black widow bite",
      "A black widow bite produces spasm and abdominal pain within thirty minutes."],
     ["Systemic symptoms mean the wound requires wide surgical excision within the next day",
      "Surgery is delayed until the wound has become stable."]],
   c=0, cite=c(61)),

 dict(topic="Tarantula", io=IOA,
   q="A 25-year-old woman handling her pet tarantula developed a red painful eye an hour later and now has blurred vision. Which is the most appropriate next step?",
   opts=[
     ["Urgent ophthalmology referral, since embedded hairs can cause corneal granuloma",
      "Correct \u2014 topical corticosteroid addresses only the cutaneous reaction."],
     ["Topical corticosteroid to the eyelid skin with review in one week's time",
      "Skin therapy does not address hairs in the eye itself."],
     ["Oral antihistamine with artificial tears and reassessment in three days",
      "Blurred vision after this exposure needs urgent assessment."],
     ["Irrigation of the eye at home with saline and no further follow-up needed",
      "Self-irrigation would not exclude a corneal granuloma."]],
   c=0, cite=c(66)),

 dict(topic="Cutaneous larva migrans", io=IOA,
   q="A 34-year-old man has a suspected serpentine skin lesion but the diagnosis is uncertain and follicular pustules are also present. Which test is most appropriate?",
   opts=[
     ["Light microscopy with mineral oil, which shows live and dead larvae in folliculitis",
      "Correct \u2014 the serpentine rash alone is enough for a clinical diagnosis."],
     ["Serology for immunoglobulin M and immunoglobulin G against the responsible organism",
      "Serology belongs to tick-borne illness rather than this."],
     ["Dermoscopy of the lesion looking for the ovoid eggs within the affected skin",
      "That is the diagnostic approach in tungiasis."],
     ["Bacterial culture of an unroofed pustule sent for Gram stain and sensitivities",
      "The pustules here contain larvae rather than bacteria."]],
   c=0, cite=c(53)),
]
