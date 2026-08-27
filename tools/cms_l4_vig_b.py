# CMS I Lecture 4 (Cutaneous Bacterial Infections) — SET 2, vignette pool B.
# Hidradenitis suppurativa, erythrasma, impetigo, erysipelas.
#
# Options drafted at matched lengths. Lead-ins varied and tracked.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "4.  Cutaneous Bacterial Infections.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis for cutaneous bacterial infections"
IOB = "b — Unique considerations of methicillin-resistant Staphylococcus aureus skin infections"
IOC = "c — Differentiate primary from secondary bacterial infection of the skin"
IOD = "d — Medical care strategies across infant, adolescent, adult and elderly populations"

POOL_B = [
 dict(topic="Hidradenitis suppurativa", io=IOA,
   q="A 29-year-old woman who smokes has had painful nodules and draining sinuses in both axillae and the groin for two years, flaring five or six times a year, with meshlike scars between them. Which is the most likely diagnosis?",
   opts=[
     ["Hidradenitis suppurativa",
      "Correct — typical lesions, apocrine distribution and recurrence more than twice in six months."],
     ["Recurrent furunculosis of the axilla",
      "Furuncles do not produce sinus tracts or meshlike scarring."],
     ["Cutaneous Crohn's disease of the groin",
      "That is not among the differentials this lecture gives."],
     ["Erythrasma of the axilla and the groin",
      "Erythrasma is a superficial stratum corneum infection without nodules."]],
   c=0, cite=c(74)),

 dict(topic="Hidradenitis suppurativa", io=IOA,
   q="A 31-year-old man with hidradenitis suppurativa asks what he can do himself to reduce flares. Which is the most appropriate counselling point?",
   opts=[
     ["Stop smoking, lose weight, avoid heat and constrictive clothing, and cleanse with an antibacterial wash",
      "Correct — smoking cessation is described as essential, and laser hair removal is also offered."],
     ["Avoid all water contact with the affected areas and apply a barrier ointment twice each day",
      "Daily cleansing is recommended rather than avoiding water."],
     ["Isolate from close contacts until treatment has been underway for at least forty-eight hours",
      "That is the isolation advice for impetigo, which is contagious."],
     ["Shower promptly after any hot tub use and check the disinfectant level in the water",
      "Those are the preventive measures for Pseudomonas folliculitis."]],
   c=0, cite=c(75)),

 dict(topic="Hidradenitis suppurativa", io=IOA,
   q="A 35-year-old woman with hidradenitis suppurativa has draining sinuses that persist despite topical clindamycin and a mild steroid cream. Which is the most appropriate next treatment?",
   opts=[
     ["Intralesional triamcinolone acetonide to decrease the size of the draining sinuses",
      "Correct. Oral prednisone reduces inflammation and prevents future lesions."],
     ["A three-month course of oral doxycycline with topical benzoyl peroxide added",
      "That regimen belongs to acne vulgaris."],
     ["Dilute acetic acid compresses applied to the sinuses twice daily for a month",
      "That treats Pseudomonas folliculitis."],
     ["Topical mupirocin applied to the sinus openings three times daily for a week",
      "Mupirocin is used for impetigo and staphylococcal carriage."]],
   c=0, cite=c(77)),

 dict(topic="Hidradenitis suppurativa", io=IOA,
   q="A 40-year-old woman has extensive hidradenitis suppurativa in both axillae that has failed medical therapy for years. She asks whether anything can cure it. Which is the most appropriate response?",
   opts=[
     ["Wide excision of the affected areas gives the best chance of permanent cure",
      "Correct. Large fluctuant cysts are meanwhile incised and drained."],
     ["Long-term systemic antibiotic therapy gives the best chance of permanent cure",
      "Long-term outcomes with systemic antibiotics are often poor."],
     ["Laser hair removal of the axillae gives the best chance of permanent cure",
      "That is a preventive measure rather than a cure."],
     ["Spironolactone taken indefinitely gives the best chance of permanent cure",
      "It reduces androgen production but does not cure the disease."]],
   c=0, cite=c(79)),

 dict(topic="Erythrasma", io=IOA,
   q="A 55-year-old man with type 2 diabetes has asymptomatic red-brown patches on the inner thighs and between the fourth and fifth toes. Under a Wood's lamp they fluoresce coral-red. Which is the most likely diagnosis?",
   opts=[
     ["Erythrasma",
      "Correct — coral-red fluorescence in intertriginous skin, with diabetics at high risk."],
     ["Tinea cruris",
      "That would show hyphae on potassium hydroxide rather than this fluorescence."],
     ["Cutaneous candidiasis",
      "That produces satellite pustules and does not fluoresce coral-red."],
     ["Inverse psoriasis",
      "That produces well-demarcated plaques without fluorescence."]],
   c=0, cite=c(83)),

 dict(topic="Erythrasma", io=IOA,
   q="A 48-year-old woman has erythrasma confined to both inguinal folds. Which is the most appropriate first-line treatment?",
   opts=[
     ["Topical erythromycin or clindamycin",
      "Correct. Oral erythromycin or clarithromycin is used for widespread disease."],
     ["Oral erythromycin or clarithromycin",
      "Oral therapy is for widespread rather than localised disease."],
     ["Topical miconazole cream applied twice daily",
      "An antifungal is added only if yeast is also present."],
     ["Topical mupirocin ointment applied three times daily",
      "Mupirocin is the topical agent for impetigo."]],
   c=0, cite=c(84)),

 dict(topic="Erythrasma", io=IOA,
   q="A 60-year-old man treated for erythrasma asks how to stop it returning. Which is the most appropriate counselling point?",
   opts=[
     ["Keep the area clean and dry, avoid excessive heat and moisture, and maintain a healthy body weight",
      "Correct, alongside good general hygiene."],
     ["Avoid sharing towels, clothing, bath water and razors with anyone in the household",
      "That is the education for impetigo, which is contagious."],
     ["Stop smoking and avoid constrictive clothing over the affected skin at all times",
      "Those are the preventive measures for hidradenitis suppurativa."],
     ["Use a broad-spectrum sunscreen daily and cover the area with clothing outdoors",
      "Ultraviolet light is not a factor in erythrasma."]],
   c=0, cite=c(84)),

 dict(topic="Impetigo", io=IOD,
   q="A 5-year-old boy has honey-coloured crusted lesions around the nose and mouth that appeared four days after a scratch, and tender submandibular nodes. Which is the most likely diagnosis?",
   opts=[
     ["Non-bullous impetigo",
      "Correct — a honey-coloured adherent crust on the face with regional lymphadenopathy."],
     ["Bullous impetigo",
      "That produces tense bullae leaving collarettes, with lymphadenopathy uncommon."],
     ["Herpes simplex of the perioral skin",
      "That produces grouped vesicles rather than a honey-coloured crust."],
     ["Ecthyma of the face and perioral area",
      "Ecthyma ulcerates into the dermis and usually affects the lower legs."]],
   c=0, cite=c(87)),

 dict(topic="Impetigo", io=IOD,
   q="A 4-year-old girl has three crusted impetigo lesions on one forearm. She is systemically well. Which is the most appropriate treatment?",
   opts=[
     ["Mupirocin ointment after removing the crusts, since topical therapy suits limited lesions",
      "Correct — it is as effective as oral therapy with fewer side effects."],
     ["Oral cephalexin, since impetigo in children always requires systemic antibiotic treatment",
      "Topical therapy is adequate for a limited number of non-bullous lesions."],
     ["Oral doxycycline, since it covers both staphylococcal and streptococcal skin disease",
      "Doxycycline is limited to children over eight years old."],
     ["Warm compresses alone, since the condition is self-limiting and resolves without treatment",
      "The course is self-limiting but may last weeks to months untreated."]],
   c=0, cite=c(94)),

 dict(topic="Impetigo", io=IOD,
   q="The parent of a 6-year-old with impetigo asks when he can go back to school. Which is the most appropriate advice?",
   opts=[
     ["He may return once treatment has been underway for twenty-four to forty-eight hours",
      "Correct, and towels, clothing, bath water, washcloths and razors must not be shared."],
     ["He may return once every crusted lesion has completely healed and the skin is clear",
      "The stated interval is tied to starting treatment, not to healing."],
     ["He may return immediately, since impetigo does not spread from one person to another",
      "Impetigo is described as very contagious and autoinoculable."],
     ["He may return after ten full days from the appearance of the very first lesion",
      "That is longer than the interval the lecture gives."]],
   c=0, cite=c(96)),

 dict(topic="Impetigo", io=IOA,
   q="A 6-year-old boy had impetigo three weeks ago. He now has puffy eyelids, tea-coloured urine and a blood pressure of 138/88. Which is the most likely diagnosis?",
   opts=[
     ["Acute post-streptococcal glomerulonephritis",
      "Correct — sudden oedema, haematuria, proteinuria and hypertension, especially at three to seven years."],
     ["Acute rheumatic fever after streptococcal infection",
      "That produces carditis, arthritis and nodules rather than this renal picture."],
     ["Secondary bacterial infection of the healing lesions",
      "That would present with local rather than systemic renal findings."],
     ["Staphylococcal scalded skin syndrome in evolution",
      "That is a toxin-mediated blistering disease of the skin."]],
   c=0, cite=c(97)),

 dict(topic="Impetigo", io=IOA,
   q="A parent asks whether antibiotics given earlier would have prevented their child's post-streptococcal glomerulonephritis. Which is the most appropriate response?",
   opts=[
     ["Antibiotics do not prevent it, because the immune activation usually precedes treatment",
      "Correct — that is stated explicitly for this complication."],
     ["Antibiotics prevent it reliably if started within the first forty-eight hours of the rash",
      "Prevention is specifically stated not to occur."],
     ["Antibiotics prevent it only when the causative organism has been confirmed by culture",
      "Culture status does not change the lack of prevention."],
     ["Antibiotics worsen it, which is why topical therapy is preferred in young children",
      "Antibiotics do not worsen the complication."]],
   c=0, cite=c(97)),

 dict(topic="Impetigo", io=IOB,
   q="A 30-year-old primary school teacher has impetigo across one forearm. Which is the most appropriate next step?",
   opts=[
     ["Obtain a culture, because her occupation places her at high risk for resistant organisms",
      "Correct — a health-care worker or teacher is the stated example of that risk."],
     ["Treat empirically with mupirocin, because culture is never indicated in adult impetigo",
      "Culture is indicated in this risk group before deciding treatment."],
     ["Treat empirically with oral doxycycline, because adult impetigo is usually staphylococcal",
      "Empiric oral therapy without culture skips the stated step for this group."],
     ["Defer treatment until swabs of every household contact have been taken and reported",
      "Contact swabbing is not part of the impetigo workup."]],
   c=0, cite=c(93)),

 dict(topic="Impetigo", io=IOA,
   q="A 45-year-old man with poorly controlled diabetes has a punched-out ulcer on the shin with a thick grey-yellow crust that has been present for two weeks and is healing slowly. Which is the most likely diagnosis?",
   opts=[
     ["Ecthyma",
      "Correct — a deeper impetigo that ulcerates into the dermis, heals slowly and leaves a scar."],
     ["Non-bullous impetigo",
      "That stays superficial and does not ulcerate or scar."],
     ["Pyoderma gangrenosum",
      "That has an undermined violaceous border and worsens with debridement."],
     ["Venous ulceration of the shin",
      "That would not present with a thick grey-yellow crust of this kind."]],
   c=0, cite=c(91)),

 dict(topic="Erysipelas", io=IOA,
   q="A 68-year-old woman has a rapidly spreading, brightly erythematous, tender plaque on the left shin with an edge that is raised and sharply demarcated. She had a fever of 39.2 degrees Celsius and chills within a day of the rash. Which is the most likely diagnosis?",
   opts=[
     ["Erysipelas",
      "Correct — the raised, sharply demarcated edge with abrupt systemic symptoms is the defining picture."],
     ["Cellulitis",
      "Cellulitis has borders that are neither raised nor sharply demarcated."],
     ["Contact dermatitis",
      "That produces itching and vesicles without fever."],
     ["Deep vein thrombosis",
      "That produces swelling and pain without a demarcated erythematous plaque."]],
   c=0, cite=c(101)),

 dict(topic="Erysipelas", io=IOA,
   q="A 72-year-old woman with erysipelas of the leg has a clinically classic presentation. Which is the most appropriate diagnostic approach?",
   opts=[
     ["No routine testing, since blood and tissue cultures have extremely low yield",
      "Correct. Leukocytosis and raised inflammatory markers are common but not diagnostic."],
     ["Blood cultures in every case, since organism identification directs the antibiotic",
      "Their yield is described as extremely low and not cost effective."],
     ["Computed tomography of the limb to define the depth of tissue involvement",
      "Imaging is of low yield and not indicated in classic presentation."],
     ["Punch biopsy of the leading edge to separate this from contact dermatitis",
      "Biopsy is not part of the routine erysipelas workup."]],
   c=0, cite=c(103)),

 dict(topic="Erysipelas", io=IOA,
   q="A 65-year-old man with erysipelas of the face has no drug allergies. Which is the most appropriate treatment?",
   opts=[
     ["Penicillin V, with symptomatic care, hydration and elevation of the affected part",
      "Correct — prompt treatment matters because progression can be rapid."],
     ["Cephalexin, with trimethoprim-sulfamethoxazole added if purulence develops later",
      "That regimen belongs to cellulitis."],
     ["Mupirocin ointment, with oral dicloxacillin if the lesions become widespread",
      "That regimen belongs to impetigo."],
     ["Clindamycin, which is reserved for patients who report a penicillin allergy",
      "Clindamycin is the alternative for penicillin-allergic patients."]],
   c=0, cite=c(104)),

 dict(topic="Erysipelas", io=IOA,
   q="A 70-year-old woman who had a mastectomy with axillary node clearance has recurrent erysipelas of that arm. Which factor most explains the recurrence?",
   opts=[
     ["Impaired lymphatic drainage from the node clearance",
      "Correct — it is the first risk factor named for erysipelas."],
     ["Nasal carriage of Staphylococcus aureus after surgery",
      "That is a risk factor for folliculitis and furuncles."],
     ["Traumatic inoculation of bacteria into the dermis",
      "That mechanism describes abscess formation."],
     ["Obstruction of the apocrine ducts in the axilla",
      "That mechanism describes hidradenitis suppurativa."]],
   c=0, cite=c(99)),

 dict(topic="Erysipelas", io=IOC,
   q="A 58-year-old man with longstanding athlete's foot develops erysipelas of the same leg. Which is the most appropriate additional management step?",
   opts=[
     ["Treat the tinea pedis, since it is the portal of entry and predicts recurrence",
      "Correct — it is named among the risk factors for erysipelas."],
     ["Begin nasal mupirocin, since staphylococcal carriage drives recurrent disease",
      "Nasal decolonisation applies to recurrent folliculitis."],
     ["Begin oral fluconazole, since the causative organism here is a yeast",
      "The causative organism in erysipelas is Group A streptococcus."],
     ["Take no additional step, since the two conditions are entirely unrelated",
      "Tinea pedis is explicitly named as a risk factor."]],
   c=0, cite=c(99)),
]
