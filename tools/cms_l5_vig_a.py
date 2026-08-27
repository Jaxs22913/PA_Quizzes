# CMS I Lecture 5 (Dermatological Infestations) — SET 2, vignette pool A.
# Scabies, pediculosis, bedbugs, fleas and tungiasis.
#
# Options drafted at matched lengths, checked per question against the shape the
# content imposes -- Lecture 5's objective pool C came out 48% raw because the
# compare-and-contrast material makes correct answers compound and distractors
# single-clause by default.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "CMS I Dermatological Infestations - Shahsv.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of dermatological infestations"
IOB = "b — Differentiate primary from secondary skin lesions"
IOC = "c — Medical care strategies across infant, child, adolescent, adult and elderly populations"

POOL_A = [
 dict(topic="Scabies", io=IOA,
   q="A 32-year-old man has six weeks of severe itching that is worst at night. Examination shows excoriations in the finger webs, on the volar wrists and in the axillae, with fine thread-like lines a few millimetres long between two fingers. His head and neck are clear. Which is the most likely diagnosis?",
   opts=[
     ["Scabies",
      "Correct — nocturnal itch at six weeks with burrows in the interdigital webs and head and neck spared."],
     ["Atopic dermatitis",
      "That is a listed differential but does not produce linear burrows."],
     ["Dermatitis herpetiformis",
      "That produces grouped vesicles on extensor surfaces and is gluten-driven."],
     ["Body louse infestation",
      "That produces linear excoriations on the back, neck, shoulders and waist."]],
   c=0, cite=c(9)),

 dict(topic="Scabies", io=IOA,
   q="A 34-year-old woman treated for scabies two months ago has itching again, and this time it began three days after her partner was diagnosed. Which best explains the timing?",
   opts=[
     ["Reinfestation, in which symptoms develop within two to three days rather than weeks",
      "Correct — the first infestation takes four to six weeks because sensitisation must occur."],
     ["Treatment failure, in which symptoms never resolved from the original infestation",
      "The symptoms had resolved and returned after a new exposure."],
     ["Post-scabietic pruritus, which persists for up to four weeks after successful therapy",
      "That would have been continuous rather than beginning after a new exposure."],
     ["Delusional parasitosis, in which the patient feels mites that are no longer present",
      "That is a psychological complication rather than an explanation of this timing."]],
   c=0, cite=c(6)),

 dict(topic="Scabies", io=IOC,
   q="A 78-year-old nursing home resident has widespread thick flaking scale on the hands, feet and trunk with thickened discoloured nails. He does not complain of itch. Which is the most likely diagnosis?",
   opts=[
     ["Crusted scabies",
      "Correct — a massive mite burden, poorly defined patches, often no pruritus, and highly infectious."],
     ["Ordinary scabies",
      "That produces intense itch with discrete burrows rather than thick scale."],
     ["Chronic plaque psoriasis",
      "That is a listed differential but does not carry the infectious risk here."],
     ["Asteatotic eczema of age",
      "That produces dry cracked skin without the mite burden."]],
   c=0, cite=c(12)),

 dict(topic="Scabies", io=IOC,
   q="An 81-year-old nursing home resident is confirmed to have crusted scabies. Which is the most important consequence to act on?",
   opts=[
     ["The scale contains millions of mites, so the resident is highly infectious to staff and other residents",
      "Correct — a hospital epidemic can follow admission, and infested healthcare workers make it hard to eradicate."],
     ["The absence of itch means the diagnosis is unlikely, so an alternative should be sought first",
      "Absent pruritus is characteristic of crusted scabies rather than evidence against it."],
     ["The thickened nails indicate a fungal infection, so a potassium hydroxide test is needed",
      "Nail change is part of the crusted scabies picture."],
     ["The condition resolves on its own, so isolation and contact tracing are not required",
      "This form is the one that most requires containment."]],
   c=0, cite=c(5)),

 dict(topic="Scabies", io=IOA,
   q="A 29-year-old woman has suspected scabies with several unexcoriated papules on the wrist. Which is the most appropriate next step?",
   opts=[
     ["Skin scraping of an unexcoriated burrow with mineral oil on a number 15 blade",
      "Correct — microscopic identification of the organism, ova or faeces is the definitive diagnosis."],
     ["Serological testing for immunoglobulin M and immunoglobulin G against the mite",
      "Serology belongs to Lyme disease rather than scabies."],
     ["Punch biopsy of an active lesion sent for direct immunofluorescence studies",
      "Immunofluorescence addresses autoimmune blistering disease."],
     ["Potassium hydroxide preparation of a plucked hair examined under a microscope",
      "That test identifies dermatophyte infection."]],
   c=0, cite=c(13)),

 dict(topic="Scabies", io=IOA,
   q="A 40-year-old man has been prescribed permethrin for scabies. Which is the most appropriate counselling point?",
   opts=[
     ["Apply it overnight to the entire skin surface with attention to creases, and repeat the application one week later",
      "Correct — the second application is the point most often missed."],
     ["Apply it overnight to the affected areas only, and no repeat application will be needed afterwards",
      "The whole skin surface is treated and a second application is required."],
     ["Wash the skin vigorously with a strong soap before each application to remove the mites",
      "Excessive washing with harsh soap may worsen the irritation."],
     ["Expect all itching to have stopped within three days, and return if any remains after that",
      "Rash and itch may last up to four weeks after successful treatment."]],
   c=0, cite=c(19)),

 dict(topic="Scabies", io=IOA,
   q="A 35-year-old woman treated for scabies three weeks ago still has itchy papules, though no new burrows are seen and her household has been treated. Which is the most appropriate treatment?",
   opts=[
     ["A mid to high potency topical corticosteroid, or intralesional triamcinolone acetonide",
      "Correct — persistent post-scabietic papules are a recognised complication."],
     ["A second full course of permethrin applied overnight to the whole skin surface",
      "There is no evidence of ongoing infestation to re-treat."],
     ["Oral ivermectin every two weeks for two to three doses alongside topical therapy",
      "That regimen is for hyperkeratotic or immunosuppressed cases."],
     ["Oral antibiotics directed at staphylococcal superinfection of the excoriations",
      "There is no described evidence of superinfection here."]],
   c=0, cite=c(21)),

 dict(topic="Scabies", io=IOA,
   q="A 42-year-old man with treated scabies develops spreading erythema, warmth and purulent crusting over several excoriated areas, with fever. Which is the most likely complication?",
   opts=[
     ["Staphylococcal superinfection",
      "Correct — it may lead to sepsis and requires antibiotic treatment."],
     ["Post-scabietic pruritic papules",
      "Those are itchy papules without fever or purulence."],
     ["Delusions of ongoing parasitosis",
      "That is a psychological complication without physical signs."],
     ["A reaction to topical permethrin",
      "Irritation from permethrin does not produce fever and purulence."]],
   c=0, cite=c(21)),

 dict(topic="Scabies", io=IOA,
   q="A 36-year-old woman and the three other members of her household are being treated for scabies. Which household measure is required?",
   opts=[
     ["Wash bedding and clothing at 60 degrees Celsius, or bag it in a warm place for fourteen days",
      "Correct — high heat is needed to kill both mites and ova, and all infested persons are treated."],
     ["Engage a professional exterminator, since the mite survives in cracks and crevices",
      "That is the requirement for bedbugs."],
     ["Vacuum floors, carpets, upholstery and play areas, but avoid any fumigation of the home",
      "That advice belongs to head lice."],
     ["Discard all bedding and soft furnishings used in the week before treatment was started",
      "Discarding is not required; washing or bagging is sufficient."]],
   c=0, cite=c(18)),

 dict(topic="Pediculosis", io=IOC,
   q="A 7-year-old girl has an itchy scalp, and the school nurse found tiny pale specks firmly attached to the hair shafts that will not brush off. Which is the most likely diagnosis?",
   opts=[
     ["Head louse infestation",
      "Correct — nits cannot be removed from the hair shaft, which separates them from dandruff."],
     ["Seborrhoeic dermatitis of the scalp",
      "That produces greasy scale that brushes off the hair."],
     ["Tinea capitis with scaling and breakage",
      "That produces broken hairs and scaly patches rather than attached nits."],
     ["Scabies affecting the scalp and hairline",
      "Head and neck are spared in healthy older children and adults."]],
   c=0, cite=c(28)),

 dict(topic="Pediculosis", io=IOA,
   q="A 9-year-old boy has had head lice treated twice without success. Which is the most appropriate explanation to give the parents?",
   opts=[
     ["Resistance is increasing, so a multimodal approach combining physical and chemical methods is warranted",
      "Correct — pediculicidal effect is read twenty-four hours after application."],
     ["Failure means the diagnosis is wrong, so the itching is more likely to be seborrhoeic dermatitis",
      "Live lice on wet combing would settle that question directly."],
     ["Occlusive home remedies such as mayonnaise or mineral oil are the recommended next step",
      "Those alternatives may not be lethal to lice."],
     ["Nits remaining in the hair after treatment prove the infestation is still active",
      "Nits may remain in the hair for months after successful treatment."]],
   c=0, cite=c(30)),

 dict(topic="Pediculosis", io=IOC,
   q="The parent of an 8-year-old treated for head lice asks when she can return to school. Which is the most appropriate response?",
   opts=[
     ["She can return now — a no-nit policy is not recommended because of the school absence it causes",
      "Correct — that position comes from the American Academy of Pediatrics."],
     ["She must stay home until every nit has been combed out of her hair completely",
      "That is the no-nit policy that is specifically not recommended."],
     ["She must stay home for two full weeks after the treatment has been completed",
      "No such exclusion period is recommended."],
     ["She must stay home until a repeat wet comb finds no nits and no live lice",
      "Nits may persist for months after cure."]],
   c=0, cite=c(30)),

 dict(topic="Pediculosis", io=IOA,
   q="A 52-year-old man living in a shelter has intense itching with linear excoriations across his back, neck, shoulders and waist, and patches of darker pigmentation where older lesions have healed. Which is the most likely diagnosis?",
   opts=[
     ["Body louse infestation",
      "Correct — that distribution with post-inflammatory pigmentation in chronic cases is characteristic."],
     ["Head louse infestation",
      "That is confined to the scalp and affects children between three and twelve."],
     ["Pubic louse infestation",
      "That produces maculae caerulae and periumbilical papular urticaria."],
     ["Scabies of the trunk and back",
      "Scabies favours the finger webs, wrists, axillae and genitalia."]],
   c=0, cite=c(26)),

 dict(topic="Pediculosis", io=IOA,
   q="A 54-year-old man with suspected body lice has no visible organisms on skin examination. Which is the most appropriate next step?",
   opts=[
     ["Examine the seams of his clothing for nits and shake the clothing over white paper",
      "Correct — the lice will move onto the paper where they can be seen."],
     ["Wet comb the scalp with water and conditioner using a fine-toothed nit comb",
      "That is the method for head lice."],
     ["Pluck a hair from the affected area and examine it under the microscope for nits",
      "That is the confirmatory method for pubic lice."],
     ["Scrape an unexcoriated papule with mineral oil and examine the smear microscopically",
      "That is the method for scabies."]],
   c=0, cite=c(28)),

 dict(topic="Pediculosis", io=IOA,
   q="A 26-year-old man has mild pubic itching, slate-grey to bluish irregular macules about 1 cm across on the lower abdomen, and papules around the umbilicus. Which additional step is most appropriate?",
   opts=[
     ["Screen for concurrent sexually transmitted infection, since pubic lice often coexist with one",
      "Correct — the macules are maculae caerulae, representing haemorrhage at feeding sites."],
     ["Screen for diabetes, since the intertriginous distribution suggests an underlying metabolic cause",
      "That association belongs to erythrasma in the previous lecture."],
     ["Screen for immunosuppression, since the massive mite burden indicates impaired immunity",
      "That reasoning applies to crusted scabies."],
     ["Screen for coeliac disease, since the eruption is associated with gluten sensitivity",
      "That association belongs to dermatitis herpetiformis."]],
   c=0, cite=c(24)),

 dict(topic="Pediculosis", io=IOA,
   q="A 30-year-old woman has itching and irritation of both eyelids, with small organisms visible at the base of her eyelashes. Which is the most likely diagnosis?",
   opts=[
     ["Phthiriasis palpebrarum, infestation of the eyelashes with pubic lice",
      "Correct — pubic lice can infest the eyelashes as well as pubic skin."],
     ["Anterior blepharitis from staphylococcal colonisation of the lid margin",
      "That would not show visible organisms at the lash base."],
     ["Demodex infestation contributing to a papulopustular facial eruption",
      "That association belongs to rosacea in the previous lecture."],
     ["Head louse infestation that has spread from the scalp to the lashes",
      "The organism named for eyelash infestation is the crab louse."]],
   c=0, cite=c(26)),

 dict(topic="Bedbugs", io=IOA,
   q="A 34-year-old woman returned from a hotel stay and has itchy wheals in rows of three across her forearms and shoulders. She did not feel any bites, and there are small blood flecks on her sheets. Which is the most likely diagnosis?",
   opts=[
     ["Bedbug bites",
      "Correct — painless bites grouped in a linear row of three, the breakfast, lunch and dinner sign."],
     ["Flea bites from the family Pulicidae",
      "Those are linear or clustered urticarial papules usually on the lower legs."],
     ["Scabies acquired from hotel bedding",
      "That produces burrows and severe nocturnal itch after weeks."],
     ["Papular urticaria from a caterpillar",
      "That follows contact with the caterpillar's hairs."]],
   c=0, cite=c(33)),

 dict(topic="Bedbugs", io=IOA,
   q="A 45-year-old man has confirmed bedbug bites and asks what will get rid of them. Which is the most appropriate advice?",
   opts=[
     ["A professional exterminator is necessary; treatment of the bites themselves is symptomatic",
      "Correct — topical antiseptic or antibiotic for secondary infection, steroids or antihistamines for itch."],
     ["Washing all bedding at 60 degrees Celsius and bagging clothing for fourteen days will clear it",
      "That is the household measure for scabies."],
     ["Leaving the room unoccupied for a month will starve the insects out of the property",
      "Bedbugs can survive up to a year without a blood meal."],
     ["Vacuuming floors, carpets and upholstery thoroughly is sufficient without any chemical treatment",
      "That advice belongs to head lice."]],
   c=0, cite=c(35)),

 dict(topic="Bedbugs", io=IOA,
   q="A 38-year-old man asks how bedbugs got into his flat when he keeps it clean. Which is the most appropriate explanation?",
   opts=[
     ["They spread in the clothing and baggage of travellers and visitors, and in second-hand mattresses and laundry",
      "Correct — the infestation is not a marker of poor hygiene."],
     ["They spread by direct skin-to-skin contact lasting fifteen to twenty minutes with an infested person",
      "That is how scabies is transmitted."],
     ["They spread through contaminated clothing that cannot be washed or changed regularly",
      "That is how body lice persist."],
     ["They spread from soil or sand contaminated with the faeces of dogs and cats",
      "That is how cutaneous larva migrans is acquired."]],
   c=0, cite=c(32)),

 dict(topic="Fleas and tungiasis", io=IOA,
   q="A 28-year-old man returned from a month in Brazil, where he walked barefoot on beaches. He has several painful papules on the plantar surface of one foot, one of which is a firm yellow translucent nodule about 8 mm across. Which is the most likely diagnosis?",
   opts=[
     ["Tungiasis",
      "Correct — the female flea burrows into the skin to lay eggs, favouring feet, web spaces and periungual skin."],
     ["Cutaneous larva migrans",
      "That produces a serpentine trail advancing two to three centimetres a day."],
     ["A plantar wart with surrounding inflammation",
      "That would not follow this travel history or enlarge over weeks."],
     ["Cercarial dermatitis after sea bathing",
      "That produces urticarial lesions within hours of freshwater exposure."]],
   c=0, cite=c(38)),

 dict(topic="Fleas and tungiasis", io=IOA,
   q="A 31-year-old woman with confirmed tungiasis of the foot asks how it will be treated. Which is the most appropriate answer?",
   opts=[
     ["Surgical excision or cryotherapy with tetanus prophylaxis and systemic antibiotics",
      "Correct — dermoscopy showing ovoid eggs is what makes the diagnosis."],
     ["Albendazole 400 mg by mouth daily for three days with no procedural treatment needed",
      "That is the treatment for cutaneous larva migrans."],
     ["Overnight topical permethrin to the whole skin surface with a repeat dose at one week",
      "That is the treatment for scabies."],
     ["Symptomatic care with antihistamines and oatmeal baths until the lesions resolve",
      "That is the treatment for cercarial dermatitis."]],
   c=0, cite=c(40)),

 dict(topic="Fleas and tungiasis", io=IOA,
   q="A 44-year-old woman with a new kitten has clustered itchy urticarial papules on both lower legs. Which is the most likely diagnosis?",
   opts=[
     ["Flea bites from the family Pulicidae",
      "Correct — linear or clustered urticarial papules, usually on the lower legs."],
     ["Tungiasis from the family Tungidae",
      "That produces enlarging papules and nodules on the feet after travel to endemic areas."],
     ["Bedbug bites acquired from furniture",
      "Those come in linear rows of three with a haemorrhagic punctum."],
     ["Scabies acquired from the new animal",
      "Human scabies is caused by the human variety of the mite."]],
   c=0, cite=c(38)),
]
