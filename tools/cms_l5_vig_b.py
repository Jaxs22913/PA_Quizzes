# CMS I Lecture 5 (Dermatological Infestations) — SET 2, vignette pool B.
# Hymenoptera, caterpillars, cutaneous larva migrans, spider bites.
#
# Options drafted at matched lengths. Correct answer is ALWAYS written first
# (c=0); the partition script rotates.
SRC = "CMS I Dermatological Infestations - Shahsv.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis of dermatological infestations"
IOB = "b — Differentiate primary from secondary skin lesions"
IOC = "c — Medical care strategies across infant, child, adolescent, adult and elderly populations"

POOL_B = [
 dict(topic="Hymenoptera", io=IOA,
   q="A 10-year-old boy is stung by a honeybee and the stinger is still visible in the skin. Which is the most appropriate immediate action?",
   opts=[
     ["Scrape it off with a card edge held parallel to the skin, as quickly as possible",
      "Correct — the barbed ovipositor keeps pumping venom while it remains impaled."],
     ["Grasp it with fine forceps and withdraw it with steady traction along its axis",
      "Scraping parallel to the surface is the described technique."],
     ["Apply ice for twenty minutes and remove it once the swelling has settled down",
      "Delay allows more venom to be pumped into the skin."],
     ["Leave it in place, since removal releases the remaining venom into the tissue",
      "It should be removed as fast as possible."]],
   c=0, cite=c(42)),

 dict(topic="Hymenoptera", io=IOA,
   q="A 44-year-old woman stung by a wasp develops generalised urticaria, lip swelling and wheeze within ten minutes. Which is the most appropriate immediate treatment?",
   opts=[
     ["Epinephrine, given intramuscularly or subcutaneously, with emergency transfer and supportive measures",
      "Correct — this is an anaphylactic reaction rather than a severe local one."],
     ["An oral antihistamine with a short course of prednisolone and review the following day",
      "Those do not substitute for epinephrine in anaphylaxis."],
     ["Ice to the sting site with injection of a local anaesthetic for control of the pain",
      "That addresses a mild local cutaneous reaction."],
     ["Calcium gluconate with a muscle relaxant and a benzodiazepine given intravenously",
      "That is envenomation treatment for a black widow spider bite."]],
   c=0, cite=c(44)),

 dict(topic="Hymenoptera", io=IOA,
   q="A 39-year-old man had anaphylaxis after a wasp sting last summer and has a positive skin test. Which is the most appropriate long-term management?",
   opts=[
     ["Carry an epinephrine auto-injector and be referred for desensitisation therapy",
      "Correct — immunotherapy is specified for fire ant hypersensitivity as well."],
     ["Carry an oral antihistamine and take it at the first sign of any sting reaction",
      "Antihistamines do not prevent or treat anaphylaxis."],
     ["Take a daily leukotriene antagonist through the summer months of each year",
      "That is not among the described measures."],
     ["Avoid all outdoor activity between the months of July and September each year",
      "Avoidance alone does not replace the named measures."]],
   c=0, cite=c(44)),

 dict(topic="Hymenoptera", io=IOA,
   q="A 27-year-old man stepped on a fire ant mound and has flushing, widespread hives, abdominal pain and vomiting. Which mechanism explains these features?",
   opts=[
     ["The venom induces mast cell degranulation",
      "Correct — fire ants usually attack in groups, which increases the venom load."],
     ["The venom contains the neurotoxin alpha-latrotoxin",
      "That is the venom of the black widow spider."],
     ["The venom is cytotoxic and causes local necrosis",
      "That describes the brown recluse spider bite."],
     ["The hairs cause mechanical irritation of the skin",
      "That describes caterpillar exposure."]],
   c=0, cite=c(42)),

 dict(topic="Caterpillars", io=IOA,
   q="An 8-year-old boy brushed against a caterpillar in the garden and now has multiple itchy erythematous papules arranged in linear streaks on his forearm. Which is the most likely diagnosis?",
   opts=[
     ["Erucism, or caterpillar dermatitis, from a gypsy moth caterpillar",
      "Correct — a pruritic dermatitis with papules in linear streaks."],
     ["An asp or puss caterpillar sting, the most poisonous of the group",
      "That produces an intensely painful sting with train-track purpura."],
     ["A processionary caterpillar reaction with urticaria and angio-oedema",
      "That species produces urticaria, angio-oedema and anaphylaxis."],
     ["Cutaneous larva migrans acquired from soil in the same garden",
      "That produces a single serpentine trail that advances daily."]],
   c=0, cite=c(47)),

 dict(topic="Caterpillars", io=IOA,
   q="A 12-year-old girl has an intensely painful sting on the arm with two parallel rows of purpura at the site after handling a caterpillar. Which caterpillar is responsible?",
   opts=[
     ["The asp or puss caterpillar, described as the most poisonous",
      "Correct — the train-track pattern of purpura is characteristic."],
     ["The gypsy moth caterpillar, which causes caterpillar dermatitis",
      "That produces pruritic papules in linear streaks rather than purpura."],
     ["The processionary caterpillar, which causes systemic reactions",
      "That species causes urticaria, angio-oedema and anaphylaxis."],
     ["The tarantula, whose shed hairs embed in skin and in the eyes",
      "A tarantula is a spider rather than a caterpillar."]],
   c=0, cite=c(47)),

 dict(topic="Caterpillars", io=IOA,
   q="A 9-year-old boy has caterpillar dermatitis with visible fine hairs still on the skin. Which physical measure is most appropriate?",
   opts=[
     ["Strip the hairs off with adhesive tape",
      "Correct, alongside antihistamines, menthol or camphor, and topical corticosteroid."],
     ["Scrape the area with a card edge held flat",
      "That is the technique for removing a honeybee stinger."],
     ["Comb the area after applying hair moisturiser",
      "That is a physical method used for head lice."],
     ["Apply blue ink and look for a zigzag line",
      "That is the burrow ink test for scabies."]],
   c=0, cite=c(48)),

 dict(topic="Cutaneous larva migrans", io=IOA,
   q="A 24-year-old woman returned from the Caribbean where she lay on the sand. She has an intensely itchy, raised, winding red track on her foot that has moved about 2 cm since yesterday. Which is the most likely diagnosis?",
   opts=[
     ["Cutaneous larva migrans",
      "Correct — a serpentine trail advancing 2 to 3 cm daily, from animal hookworm larvae in contaminated sand."],
     ["Tungiasis of the plantar surface",
      "That produces enlarging papules and a firm translucent nodule rather than a moving track."],
     ["A scabies burrow of the foot",
      "That is 1 to 10 mm long and does not advance centimetres a day."],
     ["Cercarial dermatitis after swimming",
      "That produces papules and vesicles hours after freshwater exposure."]],
   c=0, cite=c(51)),

 dict(topic="Cutaneous larva migrans", io=IOA,
   q="A 30-year-old man with cutaneous larva migrans of the foot asks about treatment. Which is the most appropriate answer?",
   opts=[
     ["Albendazole 400 mg by mouth daily for three days, or ivermectin for one to two days",
      "Correct — topical therapy is less effective and surgery or cryotherapy is not recommended."],
     ["Cryotherapy applied to the advancing end of the track where the larva is located",
      "Cryotherapy is specifically not recommended for this condition."],
     ["Surgical excision of the leading edge of the lesion under local anaesthetic",
      "Excision is specifically not recommended for this condition."],
     ["Topical permethrin to the affected area with a second application at one week",
      "That is the treatment for scabies."]],
   c=0, cite=c(54)),

 dict(topic="Cutaneous larva migrans", io=IOA,
   q="A 26-year-old man who sat on a beach in Southeast Asia has follicular papules and pustules confined to one buttock, with no visible track. Which is the most likely diagnosis?",
   opts=[
     ["Hookworm folliculitis, a form of cutaneous larva migrans",
      "Correct — it may need repeated courses of treatment."],
     ["Pseudomonas folliculitis from a contaminated hot tub",
      "That affects the trunk, extremities and buttocks after water exposure."],
     ["Bacterial folliculitis from occlusive swimwear and heat",
      "That produces pustules pierced by a central hair."],
     ["Tungiasis with multiple lesions at the site of contact",
      "That favours the feet, web spaces and periungual skin."]],
   c=0, cite=c(51)),

 dict(topic="Black widow spider", io=IOA,
   q="A 46-year-old man reached into a woodpile and felt a sharp bite. Within thirty minutes he has sweating and gooseflesh around the bite, and now has severe cramping abdominal pain and muscle spasms. Which spider is most likely responsible?",
   opts=[
     ["The black widow spider",
      "Correct — alpha-latrotoxin produces this neurotoxic picture within thirty minutes."],
     ["The brown recluse spider",
      "That produces a local necrotic lesion with systemic symptoms at one to two days."],
     ["The hobo spider",
      "That produces a painless bite with induration and paraesthesia."],
     ["A tarantula",
      "That produces mild local reactions from shed hairs."]],
   c=0, cite=c(57)),

 dict(topic="Black widow spider", io=IOA,
   q="A 71-year-old man with coronary artery disease has a confirmed black widow bite with severe abdominal pain. Which is the most appropriate management?",
   opts=[
     ["Hospitalise him, since the very old, the very young and those with cardiovascular disease are at increased risk",
      "Correct — treat with calcium gluconate, narcotic analgesia, muscle relaxants and benzodiazepines."],
     ["Discharge him with oral analgesia, since death from this bite is uncommon in any age group",
      "His age and cardiac disease both raise the risk of complications."],
     ["Refer him urgently for surgical debridement before necrosis develops at the bite site",
      "Necrosis is the concern in brown recluse bites, not this one."],
     ["Observe him for six hours, since all symptoms of this envenomation resolve within that time",
      "Symptoms are not limited to a six-hour window."]],
   c=0, cite=c(58)),

 dict(topic="Brown recluse spider", io=IOA,
   q="A 38-year-old woman in Missouri was bitten while cleaning an attic. The site now shows a dark purple centre surrounded by a pale blanched ring, and beyond that a large irregular area of redness. Which is the most likely diagnosis?",
   opts=[
     ["A brown recluse spider bite",
      "Correct — the red, white and blue sign is the hallmark of this envenomation."],
     ["A black widow spider bite",
      "That produces local sweating and piloerection with systemic muscle spasm."],
     ["A hobo spider bite",
      "That is found in the Pacific Northwest and begins painlessly with induration."],
     ["Early cellulitis at the site",
      "That produces uniform expanding erythema without a blanched ring."]],
   c=0, cite=c(60)),

 dict(topic="Brown recluse spider", io=IOA,
   q="A 41-year-old man bitten by a brown recluse six days ago now has a black eschar over the site with a deep ulcer forming beneath it. Which is the most appropriate management?",
   opts=[
     ["Pain control, warm compresses and avoiding strenuous exercise, deferring surgery until the wound is stable",
      "Correct — necrotic wounds heal very slowly and may later need reconstruction."],
     ["Immediate wide excision of the necrotic area with primary closure of the resulting defect",
      "Surgery is delayed until the wound has stabilised."],
     ["Intravenous calcium gluconate with muscle relaxants and benzodiazepines for the pain",
      "That is envenomation treatment for a black widow bite."],
     ["Oral doxycycline for ten days to prevent the wound becoming secondarily infected",
      "Antibiotics are used for established secondary infection rather than prophylaxis."]],
   c=0, cite=c(62)),

 dict(topic="Hobo spider", io=IOA,
   q="A 35-year-old man in Oregon was bitten in his basement in August. He felt nothing at the time, then noticed hardness and tingling within half an hour, and a blister formed the next day. Which spider is most likely responsible?",
   opts=[
     ["The hobo spider",
      "Correct — the Pacific Northwest, a painless bite, induration and paraesthesia within thirty minutes, vesicles by thirty-six hours."],
     ["The brown recluse spider",
      "That is abundant in the Midwest and Southeast and produces the red, white and blue sign."],
     ["The black widow spider",
      "That bite is painful and produces muscle spasm within thirty minutes."],
     ["A tarantula that had been kept as a pet",
      "That causes local reactions from shed hairs rather than a bite of this kind."]],
   c=0, cite=c(64)),

 dict(topic="Hobo spider", io=IOA,
   q="A 33-year-old woman with a hobo spider bite asks what to expect. Which is the most appropriate counselling point?",
   opts=[
     ["The wound heals within several weeks and headaches may last a week; treatment is supportive",
      "Correct — death from severe systemic effects, including aplastic anaemia, is rare."],
     ["The wound will need surgical reconstruction and healing will take several months",
      "That is the course of a severe brown recluse bite."],
     ["The symptoms will resolve within six hours with intravenous calcium gluconate",
      "That is envenomation treatment for a black widow bite."],
     ["The lesion will continue to advance daily until antiparasitic treatment is given",
      "That describes cutaneous larva migrans."]],
   c=0, cite=c(65)),

 dict(topic="Tarantula", io=IOA,
   q="A 22-year-old man who keeps a pet tarantula has an itchy papular rash on his forearms and a red, gritty eye. Which is the most appropriate management?",
   opts=[
     ["Topical corticosteroid for the skin, with ophthalmology referral for the eye",
      "Correct — shed hairs embed in skin and eyes, causing conjunctivitis and corneal granuloma."],
     ["Oral antihistamine for the skin, with artificial tears and review in two weeks",
      "Ocular involvement here needs specialist assessment."],
     ["Oral ivermectin for the skin, with topical antibiotic drops for the affected eye",
      "Antiparasitic therapy has no role in this reaction."],
     ["Surgical removal of each embedded hair from the skin and from the eye surface",
      "That is not the described management."]],
   c=0, cite=c(66)),
]
