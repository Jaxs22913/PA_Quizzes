# -*- coding: utf-8 -*-
"""Dermatological Infestations (Shah) -- pool for the Updated CMS derm master exams."""
DECK = "CMS I Dermatological Infestations - Shahsv.pptx"
IO = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, "
      "differential diagnosis, diagnostic testing, management, appropriate referrals, patient education, "
      "and prognosis of dermatological infestations")

def Q(topic, q, opts, c, slide):
    return {"topic": topic, "io": IO, "q": q, "opts": opts, "c": c, "cite": f"{DECK}, Slide {slide}"}

QUESTIONS = [

Q("Scabies",
  "A 24-year-old man reports six weeks of severe itching that is worst at night. Examination shows excoriations and "
  "eczematous change of the finger webs, the sides of the fingers, the volar wrists, the axillae, and the scrotum. "
  "The head and neck are spared. What is the pathognomonic lesion of this condition?",
  [["A thin, thread-like linear or J-shaped burrow 1 to 10 mm in length",
    "Correct. The pathognomonic lesion of scabies is a thin, thread-like linear or J-shaped burrow 1 to 10 mm long, "
    "a tunnel caused by movement of the mite in the stratum corneum. It is best seen in the interdigital webs and "
    "wrists, and is hard to see once excoriated."],
   ["Excoriated eczematous dermatitis of the finger webs",
    "This is present and typical, but excoriation and eczematous change are secondary consequences of scratching and "
    "occur in many pruritic dermatoses. Only the burrow is pathognomonic."],
   ["Intense nocturnal pruritus",
    "Nocturnal pruritus is almost always present and is severe, so it is a strong clue. But it is a symptom rather "
    "than a lesion, and it occurs in other conditions."],
   ["Thick flaking scale containing millions of mites",
    "Thick flaking scale describes hyperkeratotic or crusted scabies, a distinct presentation in which patients are "
    "highly infectious but pruritus is usually absent. That is a variant rather than the pathognomonic lesion of "
    "ordinary scabies."],
   ["Linear excoriations on the back, neck, shoulders, and waist",
    "That distribution of linear excoriation is the sign of pediculosis corporis, body lice, rather than scabies."]],
  0, 9),

Q("Scabies",
  "How is scabies typically transmitted, and how long after infestation does pruritus appear?",
  [["Close physical contact for 15 to 20 minutes, with pruritus appearing 4 to 6 weeks after initial infestation",
    "Correct. Scabies is transmitted by close physical contact for 15 to 20 minutes and may also be acquired from the "
    "bedding or underclothing of an infested individual. Pruritus appears 4 to 6 weeks after initial infestation, and "
    "many patients do not develop symptoms for up to 3 months."],
   ["Brief casual contact, with pruritus appearing within 24 hours",
    "Both halves fail. Transmission requires sustained contact, and the long sensitisation delay is why contacts are "
    "treated even when asymptomatic."],
   ["Airborne spread, with pruritus appearing after 1 week",
    "Scabies is not airborne. It requires direct skin contact or contact with contaminated bedding or clothing."],
   ["Contact with contaminated water, with pruritus appearing within hours",
    "Skin penetration from contaminated water within hours describes cercarial dermatitis, or swimmer's itch."],
   ["Direct head-to-head contact, with symptoms after 4 to 6 weeks",
    "Direct head-to-head contact is the primary mode of transmission for head lice. The incubation interval is "
    "similar, which is what makes this partially plausible, but the route is wrong."]],
  0, 5),

Q("Scabies",
  "What is the definitive method of diagnosing scabies, and what dermoscopic finding supports it?",
  [["Microscopic identification of the organism, ova, or feces, with the delta-wing jet sign on dermoscopy",
    "Correct. Definitive diagnosis is by microscopic identification of the organism, ova, or feces, obtained by skin "
    "scraping. The classic dermoscopic finding is the delta-wing jet sign, representing the dense scabies head, body, "
    "eggs, and burrow."],
   ["Microscopic identification of the organism, with a positive Nikolsky sign on examination",
    "Nikolsky sign is epidermal separation on rubbing, positive in pemphigus. It has no role in diagnosing an "
    "infestation."],
   ["A potassium hydroxide preparation showing spaghetti and meatballs",
    "Short hyphae with clusters of yeast described as spaghetti and meatballs is the potassium hydroxide finding in "
    "pityriasis versicolor, a fungal condition."],
   ["Serology for anti-mite antibodies",
    "No serological test is described. Diagnosis rests on visualising the organism or its products."],
   ["A burrow ink test alone, without microscopy",
    "The burrow ink test, in which blue or black ink is applied to a suspected lesion, is a useful supportive tool. "
    "But microscopic identification is what makes the diagnosis definitive."]],
  0, 14),

Q("Scabies",
  "A patient is prescribed topical permethrin for scabies. What counselling should be given about the response to "
  "treatment?",
  [["Apply overnight to the entire skin surface with attention to creases; relief usually comes in about 3 days, but "
    "rash and pruritus may persist for weeks",
    "Correct. Topical permethrin is applied overnight to the entire skin surface with special attention to creases. "
    "Most patients experience relief in about 3 days, but rash and pruritus may persist afterwards, which patients "
    "must be warned about or they will assume treatment failure."],
   ["Apply only to visibly affected areas; all symptoms resolve within 24 hours",
    "Both halves fail. Treatment must cover the entire skin surface because burrows are not all visible, and "
    "promising resolution in a day guarantees the patient concludes the drug did not work."],
   ["Apply overnight to the entire skin surface; any persistent itching means the treatment failed and must be "
    "repeated immediately",
    "The application is right but the interpretation is wrong, and it leads to unnecessary repeat treatment. "
    "Persistent post-scabietic pruritus is expected and is managed with mid to high potency corticosteroids or "
    "intralesional triamcinolone."],
   ["Apply for 20 minutes and rinse; no environmental measures are needed",
    "Overnight application is required, and bedding and clothing should be washed or set aside for 14 days in a "
    "plastic bag in a warm area, with high heat of 60 degrees Celsius needed to kill mites."],
   ["Apply weekly for three months to prevent recurrence",
    "Prolonged repeated application is not the described regimen and increases irritation without benefit."]],
  0, 19),

Q("Scabies",
  "An elderly nursing home resident has thick flaking scale over the hands and trunk but reports no itching. What is "
  "this presentation, and what is the infection control implication?",
  [["Crusted scabies, in which the scale contains millions of mites and the patient is highly infectious despite the "
    "absence of pruritus",
    "Correct. Hyperkeratotic or crusted scabies presents as thick flaking scale containing millions of mites. These "
    "patients are highly infectious, and pruritus is usually absent — which is exactly why the diagnosis is missed "
    "and outbreaks occur."],
   ["Crusted scabies, which is less infectious than ordinary scabies because the mites are trapped in scale",
    "The diagnosis is right but the inference is dangerously wrong. The scale contains millions of mites and these "
    "patients are the most infectious, not the least."],
   ["Post-scabietic dermatitis, which is not infectious",
    "Persistent pruritic post-scabietic papules follow successful treatment and are treated with corticosteroids. "
    "They are not associated with thick scale teeming with mites."],
   ["Xerosis of aging, requiring only emollients",
    "Dry scaly skin in an older adult is common, which is what makes this the natural assumption. But treating "
    "crusted scabies as simple xerosis leaves a highly infectious patient untreated in a congregate setting."],
   ["Psoriasis, requiring topical corticosteroids",
    "Psoriasis is on the scabies differential and produces well-demarcated plaques with silvery scale. Applying a "
    "corticosteroid to crusted scabies would suppress inflammation while the mite burden increases."]],
  0, 12),

Q("Scabies",
  "What complications of scabies should be anticipated?",
  [["Staphylococcal superinfection, which may lead to sepsis, and persistent pruritic post-scabietic papules",
    "Correct. Staphylococcal superinfection may lead to sepsis and requires antibiotics. Persistent pruritic "
    "post-scabietic papules are treated with mid to high potency corticosteroids or intralesional triamcinolone "
    "acetonide."],
   ["Progression to systemic parasitic infection of internal organs",
    "The mite remains within the stratum corneum. It does not disseminate to internal organs."],
   ["Permanent scarring alopecia of the scalp",
    "The head and neck are spared in adult scabies, so scalp complications are not expected."],
   ["Acute post-streptococcal glomerulonephritis in all patients",
    "That complication follows impetigo, especially in 3 to 7 year olds, rather than being a universal consequence of "
    "scabies — though a streptococcal superinfection could theoretically arise."],
   ["Malignant transformation of the burrow site",
    "Scabies is an infestation with no described malignant potential."]],
  0, 21),

Q("Pediculosis",
  "A 7-year-old girl has an itchy scalp, low-grade fever, occipital lymphadenopathy, and irritability. What is the "
  "best method of confirming an active infestation?",
  [["Finding live lice, best detected by combing and wet combing with water and conditioner",
    "Correct. Visualising live lice indicates active infestation and is best achieved by combing with a nit comb and "
    "by wet combing using water and conditioner. Nits are visible to the naked eye but indicate past or present "
    "infestation."],
   ["Finding nits alone, which confirms active infestation",
    "Nits are seen with the naked eye but indicate past or present infestation, so they cannot distinguish a treated "
    "case from an active one. This is the commonest reason children are treated unnecessarily."],
   ["A potassium hydroxide preparation of plucked hairs",
    "A potassium hydroxide preparation of a plucked hair is used to exclude dermatophyte infection such as tinea "
    "capitis, not to identify lice."],
   ["A skin scraping examined under mineral oil",
    "Mineral oil preparation of a skin scraping is used to identify the scabies mite, its eggs, or fecal pellets."],
   ["Wood's lamp examination of the scalp",
    "A Wood lamp may support Microsporum scalp infection but does not detect lice."]],
  0, 28),

Q("Pediculosis",
  "How does the presentation of pediculosis corporis differ from that of pediculosis capitis?",
  [["Pediculosis corporis produces linear excoriations primarily on the back, neck, shoulders, and waist, with "
    "post-inflammatory pigmentation in chronic cases",
    "Correct. Body lice produce pruritus with linear excoriations primarily on the back, neck, shoulders, and waist, "
    "and post-inflammatory pigmentation in chronic cases. Head lice affect the scalp with pruritus, low-grade fever, "
    "regional lymphadenopathy, and irritability."],
   ["Pediculosis corporis affects the scalp with regional lymphadenopathy",
    "Scalp involvement with regional lymphadenopathy is head lice. Body lice affect the trunk."],
   ["Pediculosis corporis is always asymptomatic",
    "Pubic lice are often asymptomatic or produce mild symptoms; body lice cause pruritus with excoriation."],
   ["Pediculosis corporis produces burrows in the interdigital webs",
    "Burrows in the finger webs are the pathognomonic lesion of scabies."],
   ["Pediculosis corporis is transmitted by direct head-to-head contact",
    "Direct head-to-head contact is the primary route for head lice."]],
  0, 26),

Q("Pediculosis",
  "Why is a multimodal approach recommended for treating head lice, and what does the World Health Organization "
  "recommend regarding pediculicide assessment?",
  [["Because resistance is increasing, and pediculicidal testing should be read 24 hours after application",
    "Correct. A multimodal approach is warranted because of increasing resistance, and the World Health Organization "
    "recommends that pediculicidal testing be read 24 hours after application. If treatment is not followed "
    "appropriately, patients tend to seek alternative care such as essential oils."],
   ["Because resistance is decreasing, and assessment should be made immediately after application",
    "Resistance is increasing rather than decreasing, and immediate assessment would not allow time for the "
    "pediculicide to act."],
   ["Because head lice are self-limiting and treatment is optional",
    "Head lice do not clear spontaneously in a useful timeframe and are readily transmitted among children aged 3 to "
    "12, in whom the infestation is common."],
   ["Because oral antibiotics are required alongside topical therapy in all cases",
    "Antibiotics treat secondary bacterial infection rather than the infestation itself, and they are not routinely "
    "required."],
   ["Because essential oils are the evidence-based first-line treatment",
    "Patients turn to essential oils and similar remedies when conventional treatment is not followed appropriately, "
    "which is presented as a consequence of poor adherence rather than a recommendation."]],
  0, 30),

Q("Bedbugs",
  "A 33-year-old man returns from a hotel stay with several itchy welts on exposed skin. Examination shows wheals and "
  "papules with a haemorrhagic punctum, arranged in rows of three. He did not feel the bites occur. What organism is "
  "responsible, and what is the classic descriptive term?",
  [["Cimex lectularius, with rows of three bites known as breakfast, lunch, and dinner",
    "Correct. Bedbugs are nocturnal feeders that hide in cracks and crevices of headboards, picture frames, and "
    "behind loose wallpaper. Bites are painless, multiple, and grouped in a linear fashion, and a row of three bites "
    "is known as breakfast, lunch, and dinner."],
   ["Sarcoptes scabiei, with the burrow known as the delta-wing jet",
    "The delta-wing jet is a dermoscopic sign of the scabies mite within its burrow, not a bite pattern. Scabies "
    "produces intense nocturnal itching in the finger webs and flexures rather than painless welts on exposed skin."],
   ["Pediculus humanus corporis, producing linear excoriations on the back and waist",
    "Body lice produce linear excoriations on the back, neck, shoulders, and waist and are associated with clothing "
    "rather than furniture."],
   ["Tunga penetrans, producing translucent nodules on the feet",
    "Tungiasis follows penetration of the adult female flea into human skin, producing enlarging papules and "
    "translucent nodules over the feet, and requires a travel history."],
   ["Cercariae, producing urticaria-like lesions after water exposure",
    "Cercarial dermatitis follows exposure to cercaria-infested water, with prickling within 30 minutes and severe "
    "pruritus 10 to 12 hours later."]],
  0, 33),

Q("Bedbugs",
  "What is essential in the management of a bedbug infestation beyond treating the patient's skin?",
  [["A professional exterminator is necessary to eradicate the infestation",
    "Correct. Management of the patient is symptomatic with local wound care, topical antiseptic or antibiotic cream "
    "for secondary infection, and topical corticosteroids or oral antihistamines for pruritus. A professional "
    "exterminator is necessary to eradicate the infestation itself."],
   ["Washing all bedding at 60 degrees Celsius is sufficient without any other measure",
    "High-heat laundering at 60 degrees Celsius is the environmental measure specified for scabies mites. Bedbugs "
    "live in cracks and crevices of furniture and walls, which laundering does not reach."],
   ["Treating all household contacts with topical permethrin",
    "Contact treatment applies to scabies, where household members are treated. Bedbugs are not carried on the "
    "person in the same way."],
   ["Applying a pediculicide to the affected skin",
    "Pediculicides treat lice living on the host. Bedbugs feed and then return to the environment."],
   ["No environmental action is needed since the infestation is self-limited",
    "Without eradication the bites simply continue, which is why professional extermination is described as "
    "necessary."]],
  0, 35),

Q("Fleas and tungiasis",
  "A traveller returns from a rural area having walked barefoot on sandy soil. He has several erythematous papules on "
  "the feet that have enlarged over weeks into firm, somewhat translucent yellow nodules 4 to 10 mm across, some "
  "painful. What is the diagnosis and how is it confirmed?",
  [["Tungiasis, confirmed by dermoscopy visualising ovoid eggs",
    "Correct. Tungiasis is infestation by penetration of the adult female flea into human skin to lay eggs. Solitary "
    "or multiple erythematous papules enlarge over weeks to 4 to 10 mm, sometimes forming a firm translucent nodule, "
    "and dermoscopy is used to visualise the ovoid eggs."],
   ["Cutaneous larva migrans, confirmed by the serpentine trail",
    "Cutaneous larva migrans also follows contact with contaminated soil, which makes it a genuine consideration. But "
    "it produces an erythematous, raised, serpentine trail advancing 2 to 3 cm per day rather than discrete enlarging "
    "nodules."],
   ["Scabies, confirmed by skin scraping",
    "Scabies favours the finger webs, wrists, axillae, and genitals with burrows and intense nocturnal itch rather "
    "than nodules on the feet after soil exposure."],
   ["Cercarial dermatitis, confirmed by history of freshwater exposure",
    "Cercarial dermatitis follows swimming in cercaria-infested water and produces urticaria-like lesions and papules "
    "rather than persistent translucent nodules."],
   ["Bedbug bites, confirmed by inspection of the sleeping area",
    "Bedbug bites are painless wheals and papules in linear groups on exposed skin, not enlarging nodules of the "
    "feet."]],
  0, 40),

Q("Fleas and tungiasis",
  "What management is appropriate for tungiasis?",
  [["Surgical excision or cryotherapy with topical agents, tetanus prophylaxis, and systemic antibiotics, with "
    "prevention by not walking barefoot",
    "Correct. Management includes surgical excision or cryotherapy and topical agents, tetanus prophylaxis, and "
    "systemic antibiotics. Prevention centres on avoiding walking barefoot in endemic areas."],
   ["Oral albendazole for 3 days",
    "Albendazole 400 mg daily for 3 days is the treatment for cutaneous larva migrans, a different soil-acquired "
    "parasitic condition."],
   ["Topical permethrin applied overnight to the whole body",
    "Whole-body overnight permethrin is the treatment for scabies."],
   ["Symptomatic treatment alone with antihistamines and oatmeal baths",
    "Symptomatic treatment with antihistamines and oatmeal baths is the approach to cercarial dermatitis, which is "
    "self-limited. Tungiasis requires removal of the embedded flea."],
   ["Professional extermination of the home",
    "Extermination is required for bedbugs, which live in the domestic environment. The flea in tungiasis is embedded "
    "in the patient's skin."]],
  0, 40),

Q("Hymenoptera",
  "A 28-year-old man is stung by a wasp and within minutes develops widespread urticaria, wheezing, and hypotension. "
  "What is the immediate treatment?",
  [["Epinephrine given intramuscularly or subcutaneously, with emergency transfer and supportive measures",
    "Correct. For an anaphylactic reaction to a hymenoptera sting the treatment is subcutaneous or intramuscular "
    "epinephrine with emergency department transfer and supportive measures."],
   ["Cleaning the site, ice, and possibly local anaesthetic injection for pain",
    "That is the management of a mild local cutaneous reaction. Applying it to anaphylaxis would leave a patient with "
    "airway and circulatory compromise untreated."],
   ["An oral antihistamine and observation at home",
    "Oral antihistamines address urticaria but do nothing for the airway and circulatory collapse of anaphylaxis."],
   ["A topical corticosteroid applied to the sting site",
    "Topical treatment cannot address a systemic reaction."],
   ["Extensive local wound debridement",
    "Debridement has no role. Extensive oedema at the sting site with induration describes a severe local reaction "
    "rather than a wound requiring surgery."]],
  0, 44),

Q("Cutaneous larva migrans",
  "A 19-year-old returns from a tropical beach holiday with an intensely itchy, raised, serpentine track on the foot "
  "that has advanced a few centimetres over the past two days. What is the diagnosis and treatment?",
  [["Cutaneous larva migrans, treated with oral albendazole or ivermectin",
    "Correct. Cutaneous larva migrans results from larvae of animal nematodes, mostly dog and cat hookworms, in which "
    "the human is a dead-end host. The classic lesion is an erythematous, raised, vesicular, linear or serpentine "
    "trail progressing 2 to 3 cm per day. Treatment is albendazole 400 mg daily for 3 days or ivermectin."],
   ["Cutaneous larva migrans, treated with surgical excision or cryotherapy",
    "The diagnosis is right but surgical excision and cryotherapy are specifically not recommended, because the "
    "advancing larva is ahead of the visible track."],
   ["Cutaneous larva migrans, treated with topical therapy alone",
    "Topical therapy is described as less effective. Oral treatment is what clears the infestation."],
   ["Tungiasis, treated with excision of the embedded flea",
    "Tungiasis produces discrete enlarging nodules on the feet rather than a migrating serpentine track."],
   ["Scabies, treated with whole-body permethrin",
    "Scabies burrows are 1 to 10 mm and static, whereas this track advances centimetres per day."]],
  0, 54),

Q("Brown recluse spider",
  "A patient in the American Southeast has a painful lesion on the thigh with a central violaceous area surrounded by "
  "a rim of blanched skin and then a large area of erythema. What is this sign, and what organism is responsible?",
  [["The red, white, and blue sign, from a brown recluse spider bite",
    "Correct. The hallmark of a brown recluse bite is the red, white, and blue sign — a central violaceous area "
    "surrounded by a rim of blanched skin surrounded by a large erythematous area. Loxosceles reclusa has a dark "
    "brown violin-shaped marking on the cephalothorax and is abundant in the American Midwest and Southeast."],
   ["The red, white, and blue sign, from a black widow spider bite",
    "The sign is correctly named but attributed to the wrong spider. The black widow has a red hourglass on the "
    "underside of the abdomen and produces crampy abdominal pain and muscle spasms rather than a necrotic lesion."],
   ["Hutchinson sign, from a hobo spider bite",
    "Hutchinson sign is lesions on the tip of the nose in herpes zoster ophthalmicus. Hobo spider bites are painless "
    "with induration and paraesthesia and are the predominant cause of necrotic arachnidism in the Pacific "
    "Northwest."],
   ["The delta-wing jet sign, from a mite infestation",
    "The delta-wing jet is a dermoscopic sign of scabies."],
   ["Crowe's sign, from a caterpillar reaction",
    "Crowe's sign is intertriginous freckling in neurofibromatosis type 1."]],
  0, 60),

Q("Brown recluse spider",
  "How does a brown recluse bite evolve in the small percentage of cases that progress, and what governs the timing "
  "of surgery?",
  [["Necrosis 2 to 3 days after the bite with eschar formation between days 5 and 7, followed by deep ulcers; "
    "surgery is delayed because necrotic wounds heal slowly",
    "Correct. In a small percentage of cases the initial wound progresses to necrosis 2 to 3 days after the bite, "
    "then eschar formation between days 5 and 7, then deep ulcers. Necrotic wounds heal very slowly and may need "
    "surgical intervention or reconstruction, with surgery delayed."],
   ["Immediate full-thickness necrosis within hours requiring emergency debridement",
    "Necrosis develops over days rather than hours, and early aggressive surgery is not the approach."],
   ["Resolution without any tissue loss in all cases",
    "Most bites cause mild local reactions, which makes this partly true, but a small percentage progress to "
    "ulcerative necrosis requiring prolonged management."],
   ["Systemic symptoms appearing within 30 minutes with crampy abdominal pain",
    "Localised erythema, piloerection, and sweating within 30 minutes followed by agonising crampy abdominal pain and "
    "muscle spasms describes black widow envenomation."],
   ["Painless induration and paraesthesia within 30 minutes with vesicles by 36 hours",
    "That course describes a hobo spider bite."]],
  0, 62),

Q("Black widow spider",
  "A patient bitten by a spider with a red hourglass on the underside of its abdomen develops localised erythema, "
  "piloerection, and sweating around the bite within 30 minutes, followed by severe crampy abdominal pain and muscle "
  "spasms. What treatments are used for envenomation?",
  [["Calcium gluconate 10 percent, narcotic analgesics, muscle relaxants, and antivenom in selected cases",
    "Correct. Latrodectus mactans, the southern black widow, has a characteristic red hourglass. Envenomation "
    "treatment includes calcium gluconate 10 percent, narcotic analgesics, and muscle relaxants, with hospitalisation "
    "depending on symptoms and increased risk in the very old, very young, and those with cardiovascular disease."],
   ["Albendazole and ivermectin",
    "Those are anthelmintics used for cutaneous larva migrans. They have no role in envenomation."],
   ["Topical permethrin applied overnight",
    "Permethrin treats scabies. A spider envenomation is a toxin exposure rather than an infestation."],
   ["Surgical debridement of the bite site",
    "Progressive necrosis requiring delayed surgical intervention characterises the brown recluse bite rather than "
    "the black widow, whose effects are largely neurotoxic and systemic."],
   ["Doxycycline for 5 to 10 days",
    "Doxycycline is the treatment for Rocky Mountain spotted fever and first-line for Lyme disease."]],
  0, 58),

Q("Hobo spider",
  "In which region of the United States is the hobo spider the predominant cause of necrotic arachnidism, and what is "
  "the early course of its bite?",
  [["The Pacific Northwest, with a painless bite followed by induration and paraesthesia within 30 minutes and "
    "vesicle formation in the first 36 hours",
    "Correct. The hobo spider, also called the aggressive house spider, is the predominant cause of necrotic "
    "arachnidism in the Pacific Northwest. The bite is painless, with induration and paraesthesia of the bite site "
    "within 30 minutes, a large erythematous area, and vesicle formation during the first 36 hours."],
   ["The American Midwest and Southeast, with a painful bite and the red, white, and blue sign",
    "The Midwest and Southeast is brown recluse territory, and the red, white, and blue sign is its hallmark. Hobo "
    "spiders are often mistaken for brown recluses, which is exactly the confusion this distinction addresses."],
   ["The Northeast, with erythema migrans developing at the bite site",
    "Erythema migrans is the stage 1 lesion of Lyme disease, a tick-borne spirochaetal infection."],
   ["The Southwest, with immediate crampy abdominal pain and muscle spasms",
    "Crampy abdominal pain and muscle spasms follow black widow envenomation."],
   ["The Pacific Northwest, with immediate severe pain at the bite site",
    "The region is right but the bite is specifically painless, which is part of why it is not recognised at the "
    "time."]],
  0, 64),

Q("Tarantula",
  "What cutaneous and ocular effects can tarantulas cause?",
  [["Embedded hairs producing pruritus or granulomatous reactions in skin, and conjunctivitis or corneal granuloma in "
    "the eye",
    "Correct. Tarantula hairs may land and embed on skin or eyes when the animal is threatened, producing cutaneous "
    "responses ranging from mild local pruritus to granulomatous reactions, and conjunctivitis or corneal granuloma "
    "in the eye."],
   ["Necrotic ulceration through cytotoxic venom",
    "Necrotic ulceration follows brown recluse and hobo spider bites. The tarantula problem is mechanical and "
    "inflammatory rather than a cytotoxic envenomation."],
   ["Systemic muscle spasm and abdominal pain from neurotoxin",
    "Neurotoxic muscle spasm and abdominal pain follow black widow envenomation."],
   ["A serpentine advancing track in the skin",
    "A serpentine advancing track is cutaneous larva migrans."],
   ["No cutaneous or ocular effects of any kind",
    "The hairs cause real effects at both sites, which is why eye protection matters when handling these animals."]],
  0, 66),

Q("Caterpillars",
  "A child develops multiple erythematous papules arranged in linear streaks after contact with a caterpillar. What "
  "is the term for the aggregate of medical effects caused by caterpillars, moths, and butterflies, and what is a "
  "specific step in management?",
  [["Lepidopterism, with removal of the hairs by stripping the affected area",
    "Correct. Lepidopterism is the aggregate of medical effects caused by caterpillars, moths, and butterflies. "
    "Gypsy moth caterpillar contact causes erucism, a pruritic dermatitis with erythematous papules in linear "
    "streaks. Management is symptomatic, and the hairs are removed by stripping."],
   ["Erucism, treated only with systemic corticosteroids",
    "Erucism is the specific caterpillar dermatitis rather than the umbrella term, and management extends beyond "
    "corticosteroids to antihistamines, topical menthol or camphor preparations, analgesia, and hair removal."],
   ["Arachnidism, treated with antivenom",
    "Necrotic arachnidism refers to spider bites. Antivenom is used in selected black widow envenomations."],
   ["Tungiasis, treated with excision",
    "Tungiasis is flea penetration of the skin producing nodules on the feet."],
   ["Cercarial dermatitis, treated with oatmeal baths",
    "Cercarial dermatitis follows exposure to cercaria-infested water and is managed symptomatically with "
    "antihistamines and oatmeal baths."]],
  0, 48),

Q("Lyme disease",
  "A 40-year-old man in Connecticut develops an expanding erythematous oval lesion 8 cm across with central clearing "
  "and a darker punctate centre at the site of a recent tick bite. What stage is this, what is the lesion called, and "
  "what should be done about testing?",
  [["Stage 1 early localised infection with erythema migrans; a patient with this lesion should be diagnosed and "
    "treated clinically rather than waiting for serology",
    "Correct. Stage 1 early localised infection is characterised by erythema migrans, a lesion greater than 5 cm that "
    "expands with central clearing and often a darker punctate centre, also called a bull's-eye. A patient with this "
    "lesion should be diagnosed and treated on that basis, and testing is most helpful in patients from non-endemic "
    "regions with non-diagnostic symptoms."],
   ["Stage 1 early localised infection; treatment should be withheld until two-tier serology returns positive",
    "The staging is right but withholding treatment is wrong and consequential. Serology may be negative early, and "
    "delay permits progression to disseminated disease."],
   ["Stage 2 early disseminated infection; intravenous ceftriaxone should be started",
    "Stage 2 occurs days to weeks later and involves the skin, central nervous system, cardiac, musculoskeletal, and "
    "ocular systems. A solitary erythema migrans lesion is stage 1."],
   ["Stage 3 late persistent infection; a monoarticular arthritis should be sought",
    "Stage 3 occurs months to years later, with monoarticular or oligoarticular arthritis of the knee or weight "
    "bearing joints as the classic manifestation."],
   ["Cellulitis at the bite site; cephalexin should be started",
    "Cellulitis produces warmth, tenderness, and indistinct spreading borders rather than an expanding annular lesion "
    "with central clearing."]],
  0, 72),

Q("Lyme disease",
  "What is first-line oral antibiotic therapy for Lyme disease, and what alternative applies to children and pregnant "
  "women with early disease?",
  [["Doxycycline first line, with amoxicillin as an alternative first-line agent for early disease in children and "
    "pregnant women",
    "Correct. Antibiotics are indicated in all stages. Doxycycline is first line, with amoxicillin as an alternative "
    "first-line agent for early disease including erythema migrans, particularly in children and pregnant women."],
   ["Amoxicillin first line for all patients, with doxycycline reserved for treatment failure",
    "The hierarchy is reversed. Doxycycline is the first-line agent generally, with amoxicillin as the alternative "
    "in specific populations."],
   ["Intravenous ceftriaxone for all stages",
    "Intravenous ceftriaxone, cefotaxime, or penicillin G is used for certain manifestations including acrodermatitis "
    "chronica atrophicans and arthritis, rather than for all patients."],
   ["No antibiotics for stage 1, since erythema migrans is self-limited",
    "Antibiotics are indicated in all stages, and treating early disease is what prevents dissemination."],
   ["Permethrin applied topically to the bite site",
    "Permethrin is a topical treatment for scabies, not an antibiotic for a spirochaetal infection."]],
  0, 79),

Q("Lyme disease",
  "What is the classic manifestation of stage 3 late persistent Lyme disease?",
  [["Monoarticular or oligoarticular arthritis affecting the knee or other weight-bearing joints",
    "Correct. Stage 3 occurs months to years later, affecting skin, central nervous system, and musculoskeletal "
    "systems, with monoarticular or oligoarticular arthritis of the knee or weight-bearing joints as the classic "
    "manifestation."],
   ["Erythema migrans at the site of the tick bite",
    "Erythema migrans is the stage 1 early localised finding."],
   ["Cranial nerve palsies and meningitis",
    "Cranial nerve palsies, meningitis, and radiculopathies belong to stage 2 early disseminated infection, occurring "
    "days to weeks after the bite."],
   ["A rash beginning on the ankles and wrists and spreading centrally",
    "A rash starting on the ankles and wrists is characteristic of Rocky Mountain spotted fever."],
   ["Symmetric polyarthritis of the small joints of the hands",
    "The arthritis of late Lyme disease is monoarticular or oligoarticular and favours large weight-bearing joints "
    "rather than a symmetric small-joint pattern."]],
  0, 75),

Q("Rocky Mountain spotted fever",
  "A 9-year-old presents with a fever above 39.5 degrees Celsius for three days, headache, and now a rash that began "
  "on the ankles and wrists and is spreading centrally. What is the treatment, and does his age change it?",
  [["Doxycycline 2.2 mg per kilogram by mouth every 12 hours for 5 to 10 days; doxycycline is used in children for "
    "this infection",
    "Correct. Rocky Mountain spotted fever is treated with doxycycline in adults at 100 mg every 12 hours for 5 to "
    "10 days, the same in pregnant women, and in children at 2.2 mg per kilogram every 12 hours. The illness is life "
    "threatening if untreated."],
   ["Amoxicillin, because doxycycline is contraindicated under the age of 8",
    "The usual paediatric caution about tetracyclines does not override treatment here — doxycycline dosing for "
    "children is specified, and delayed or inadequate treatment leads to severe and life-threatening complications."],
   ["Supportive care only, since the illness is self-limited",
    "The disease is life threatening if not treated, with severe cardiac, gastrointestinal, hepatic, neurological, "
    "ophthalmological, renal, and pulmonary manifestations following delayed or inadequate treatment."],
   ["Intravenous ceftriaxone for 14 days",
    "Ceftriaxone is used intravenously for certain manifestations of Lyme disease rather than for rickettsial "
    "infection."],
   ["Withhold antibiotics until the indirect immunofluorescence assay returns",
    "The indirect immunofluorescence assay is the gold standard test, but waiting for it costs the time in which "
    "treatment determines survival."]],
  0, 86),

Q("Rocky Mountain spotted fever",
  "What is the clinical triad of Rocky Mountain spotted fever, and how often is it present?",
  [["Fever above 39.5 degrees Celsius, headache, and rash, present in only about 60 percent of patients",
    "Correct. The clinical triad is fever above 39.5 degrees Celsius, headache, and rash, present in only about 60 "
    "percent of patients. Fever presents in the first 3 days with rash following 2 to 4 days after fever onset."],
   ["Fever, headache, and rash, present in essentially all patients",
    "Requiring the full triad would mean withholding treatment from roughly 40 percent of patients who do not have "
    "all three, which is precisely the error the 60 percent figure warns against."],
   ["Fever, arthritis, and erythema migrans, present in most patients",
    "Erythema migrans and arthritis belong to Lyme disease."],
   ["Fever, cough, and rash, present in about 60 percent",
    "The second element of the triad is headache rather than cough."],
   ["Rash, pruritus, and lymphadenopathy",
    "This omits fever, which presents first and is central to the illness."]],
  0, 82),

Q("Rocky Mountain spotted fever",
  "What laboratory abnormalities are characteristic of Rocky Mountain spotted fever, and what is the gold standard "
  "diagnostic test?",
  [["Thrombocytopenia, anaemia, mild hyponatraemia, mild transaminitis, and a normal white cell count with increased "
    "bands, with indirect immunofluorescence assay as the gold standard",
    "Correct. Those are the characteristic laboratory findings, and the indirect immunofluorescence assay is the gold "
    "standard. Cerebrospinal fluid may show leukocytosis, moderately elevated protein, and normal glucose."],
   ["Marked leukocytosis with neutrophilia and thrombocytosis",
    "The white cell count is characteristically normal with an increase in bands, and the platelet count falls rather "
    "than rises. Expecting a raised white count would argue against the diagnosis wrongly."],
   ["Hypernatraemia and marked hyperglycaemia",
    "The sodium abnormality is a mild hyponatraemia, and glucose is not a described feature."],
   ["Eosinophilia with raised immunoglobulin E",
    "Eosinophilia with raised immunoglobulin E suggests parasitic or atopic disease rather than a rickettsial "
    "infection."],
   ["A positive potassium hydroxide preparation",
    "A potassium hydroxide preparation detects fungal elements and has no role here."]],
  0, 85),

Q("Cercarial dermatitis",
  "A camper develops a prickling sensation lasting about 30 minutes after wading in a freshwater lake, followed 10 to "
  "12 hours later by severe itching and then erythematous papules. What is this condition, and what completes its "
  "life cycle?",
  [["Cercarial dermatitis, in which host animals pass eggs into water, snails become infected, and cercariae are "
    "released",
    "Correct. Cercarial dermatitis, also called swimmer's itch or clam digger's itch, results from penetration of the "
    "skin by cercarial forms of parasitic flatworms. Host animals such as waterfowl and muskrats pass eggs in feces "
    "into water, the eggs hatch and infect snails within 12 hours, and cercariae are released about 5 weeks later."],
   ["Cutaneous larva migrans, acquired from soil contaminated by dog and cat hookworm",
    "Cutaneous larva migrans is acquired from soil rather than water and produces an advancing serpentine track "
    "rather than an immediate prickling sensation and later papules."],
   ["Tungiasis, from a flea penetrating the skin of the feet",
    "Tungiasis produces enlarging nodules on the feet over weeks, following barefoot contact with sandy soil."],
   ["Scabies, from a mite burrowing into the stratum corneum",
    "Scabies produces intense nocturnal pruritus over weeks with burrows in the finger webs and flexures rather than "
    "an immediate reaction after a single water exposure."],
   ["Bedbug bites acquired from campsite bedding",
    "Bedbug bites are painless linear groups of wheals on exposed skin without the immediate prickling and delayed "
    "pruritus after water exposure."]],
  0, 89),

Q("Cercarial dermatitis",
  "What is the management of cercarial dermatitis?",
  [["Symptomatic treatment with antihistamines, oatmeal baths, antipruritic lotions, aspirin for pain, proper "
    "washing and hygiene, and topical or oral glucocorticoids",
    "Correct. Management is symptomatic: antihistamines, oatmeal baths, antipruritic lotions, aspirin for pain "
    "control, proper washing and hygiene, and topical or oral glucocorticoids."],
   ["Oral albendazole for 3 days",
    "Albendazole treats cutaneous larva migrans. In cercarial dermatitis the human is not a viable host and the "
    "organism dies in the skin, so the problem is the inflammatory reaction rather than an ongoing infestation."],
   ["Whole-body topical permethrin overnight",
    "Permethrin is used for scabies."],
   ["Doxycycline for 5 to 10 days",
    "Doxycycline treats rickettsial infection and Lyme disease."],
   ["Professional extermination of the water source",
    "Extermination is the environmental step for bedbugs. Avoidance of infested water is the relevant preventive "
    "measure here."]],
  0, 91),

Q("Ticks",
  "What single action is emphasised first in the management of a tick-borne illness such as Lyme disease?",
  [["Remove the tick immediately",
    "Correct. The management sequence begins with removing the tick immediately, followed by antibiotics, which are "
    "indicated in all stages."],
   ["Send the tick for species identification before any treatment",
    "Identification may be of interest but does not precede removal, and waiting delays both removal and treatment."],
   ["Apply a topical corticosteroid to the bite site",
    "A corticosteroid addresses local inflammation but leaves the attached vector in place."],
   ["Await the appearance of erythema migrans before acting",
    "Erythema migrans identifies stage 1 infection and prompts clinical diagnosis and treatment, but waiting for it "
    "before removing an attached tick prolongs exposure."],
   ["Administer prophylactic intravenous antibiotics to all patients",
    "Oral doxycycline is first line, and intravenous therapy is reserved for particular manifestations rather than "
    "given universally."]],
  0, 79),

Q("Scabies",
  "What environmental measure is specified for bedding and clothing in the management of scabies?",
  [["Wash them, or set them aside for 14 days in a plastic bag in a warm area, with high heat of 60 degrees Celsius "
    "needed to kill mites",
    "Correct. Bedding and clothing should be washed or set aside for 14 days in a plastic bag in a warm area, and "
    "high heat at 60 degrees Celsius is needed to kill mites."],
   ["Set them aside for 24 hours, after which the mites die",
    "A day is not long enough. The 14-day isolation period reflects how long mites can survive off the host."],
   ["Wash them in cold water, since detergent alone kills the mites",
    "High heat at 60 degrees Celsius is specified. Cold washing does not reliably kill mites."],
   ["Discard all bedding and clothing",
    "Laundering at high heat or bagging for 14 days is sufficient, so discarding possessions imposes cost without "
    "added benefit."],
   ["No environmental measures are needed because transmission requires prolonged skin contact",
    "Scabies may also be acquired from the bedding or underclothing of an infested person, which is why the "
    "environmental step exists."]],
  0, 18),
]
