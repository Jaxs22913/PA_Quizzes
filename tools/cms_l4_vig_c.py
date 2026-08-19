# CMS I Lecture 4 (Cutaneous Bacterial Infections) — SET 2, vignette pool C.
# Cellulitis, abscess, acute and chronic paronychia, necrotizing fasciitis,
# and the cross-cutting objectives.
#
# Options drafted at matched lengths. Lead-ins varied and tracked; this pool
# carries the extra "which test", "which referral" and "patient education"
# lead-ins so no single type exceeds 40% of either finished form.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "4.  Cutaneous Bacterial Infections.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Etiologies, epidemiology, risk factors, manifestations, differential diagnosis, testing, management, referrals, education and prognosis for cutaneous bacterial infections"
IOB = "Objective b — Unique considerations of methicillin-resistant Staphylococcus aureus skin infections"
IOC = "Objective c — Differentiate primary from secondary bacterial infection of the skin"
IOD = "Objective d — Medical care strategies across infant, adolescent, adult and elderly populations"

POOL_C = [
 dict(topic="Cellulitis", io=IOA,
   q="A 54-year-old man with diabetes has a warm, tender, swollen, erythematous area over the right lower leg. The border blends gradually into normal skin. The left leg is unaffected. Which is the most likely diagnosis?",
   opts=[
     ["Cellulitis",
      "Correct — all four cardinal signs on one lower leg with borders neither raised nor demarcated."],
     ["Erysipelas",
      "Erysipelas has a raised plaque with a clear line of demarcation."],
     ["Stasis dermatitis",
      "That is usually bilateral and lacks the warmth and tenderness."],
     ["Contact dermatitis",
      "That causes itching and vesicles with no fever."]],
   c=0, cite=c(107)),

 dict(topic="Cellulitis", io=IOA,
   q="A 47-year-old healthy woman has a small area of cellulitis on the forearm with minimal pain, no fever and no risk factors for serious illness. Which is the most appropriate diagnostic approach?",
   opts=[
     ["No workup, since the diagnosis is clinical in limited disease without systemic signs",
      "Correct. Serious infection warrants blood cultures, punch biopsy, blood count and creatine phosphokinase."],
     ["Blood cultures and a punch biopsy, since organism identification guides therapy",
      "Those belong to serious infection rather than limited disease."],
     ["Plain films of the forearm, since underlying osteomyelitis must be excluded",
      "Imaging is considered when fasciitis or osteomyelitis is suspected."],
     ["Venous duplex ultrasound, since deep vein thrombosis must be excluded first",
      "Thrombosis is a differential but not a mandatory first test here."]],
   c=0, cite=c(109)),

 dict(topic="Cellulitis", io=IOB,
   q="A 50-year-old man has cellulitis of the thigh with a central area of purulence. Which antibiotic choice is most appropriate?",
   opts=[
     ["Trimethoprim-sulfamethoxazole, doxycycline, clindamycin or linezolid",
      "Correct — purulent cellulitis prompts cover for methicillin-resistant Staphylococcus aureus."],
     ["Dicloxacillin or cephalexin, with clindamycin if penicillin allergic",
      "That regimen is for non-purulent cellulitis."],
     ["Penicillin V, with clindamycin if the patient is penicillin allergic",
      "That regimen is for erysipelas."],
     ["Topical mupirocin, with oral cephalexin if lesions become widespread",
      "That regimen is for impetigo."]],
   c=0, cite=c(110)),

 dict(topic="Cellulitis", io=IOA,
   q="A 61-year-old woman started on antibiotics for cellulitis yesterday reports the leg looks worse today, though she feels no more unwell. Which is the most appropriate response?",
   opts=[
     ["Reassure her, because sudden destruction of pathogens releases enzymes that increase local inflammation",
      "Correct. Fever usually resolves in twenty-four hours and inflammation over one to two weeks."],
     ["Change the antibiotic immediately, because worsening on day one indicates the wrong organism",
      "A change is considered if fever persists beyond forty-eight hours."],
     ["Admit her for intravenous therapy, because worsening at any point signals systemic spread",
      "Worsening appearance on the first day alone is expected."],
     ["Arrange urgent surgical review, because worsening at any point suggests necrotizing fasciitis",
      "The clue for that is no response at forty-eight hours, or pain out of proportion."]],
   c=0, cite=c(112)),

 dict(topic="Cellulitis", io=IOA,
   q="A 66-year-old man with cellulitis of the calf has an area that is tense, cyanotic and bronzed, and has not improved on antibiotics. Which is the most appropriate next step?",
   opts=[
     ["Surgical debridement, because devitalised tissue is not perfused so antibiotics cannot reach it",
      "Correct — that is the pitfall the lecture names explicitly."],
     ["Escalation to intravenous vancomycin, because the organism is likely to be resistant",
      "The problem is drug delivery to dead tissue rather than resistance."],
     ["Continued oral antibiotics for a further week, because resolution can take two weeks",
      "Necrotic tissue will not respond to any antibiotic regimen."],
     ["Compression bandaging and elevation, because venous congestion explains the colour",
      "The described appearance is of devitalised tissue."]],
   c=0, cite=c(111)),

 dict(topic="Abscess", io=IOC,
   q="A 33-year-old man who injects drugs has a tender fluctuant swelling of the forearm that developed at an injection site. Which best describes how this lesion arose?",
   opts=[
     ["Traumatic inoculation of bacteria into the skin, which is how an abscess differs from a furuncle",
      "Correct — a furuncle arises from an infected hair follicle instead."],
     ["Infection of a hair follicle spreading into the adjacent subcutaneous tissue of the arm",
      "That describes a furuncle rather than an abscess."],
     ["Obstruction of an apocrine duct followed by rupture into the surrounding dermal tissue",
      "That describes hidradenitis suppurativa."],
     ["Spread of streptococci along the superficial lymphatics of the upper dermal layer",
      "That describes erysipelas."]],
   c=0, cite=c(113)),

 dict(topic="Abscess", io=IOA,
   q="A 40-year-old woman has an axillary abscess that has not drained spontaneously. Which is the most appropriate treatment?",
   opts=[
     ["Surgical incision and drainage",
      "Correct. If a lesion drains on its own, warm soaks with broad-spectrum antibiotics are used."],
     ["Warm soaks and observation",
      "That applies where the lesion has already drained spontaneously."],
     ["Oral antibiotics on their own",
      "Antibiotics alone will not evacuate an undrained collection."],
     ["Wide excision of the axilla",
      "Wide excision belongs to hidradenitis suppurativa."]],
   c=0, cite=c(115)),

 dict(topic="Acute paronychia", io=IOA,
   q="A 26-year-old woman has redness, swelling and tenderness around the right index fingernail three days after a manicure, with a small collection of pus visible under the nail fold. Which is the most likely diagnosis?",
   opts=[
     ["Acute paronychia",
      "Correct — onset two to five days after trauma, starting as cellulitis and progressing to abscess."],
     ["Chronic paronychia",
      "That develops over at least six weeks and is not fluctuant."],
     ["Herpetic whitlow",
      "That produces grouped vesicles and is excluded with a Tzanck smear."],
     ["Felon of the fingertip",
      "That involves the pulp space rather than the nail fold."]],
   c=0, cite=c(117)),

 dict(topic="Acute paronychia", io=IOA,
   q="A 35-year-old man has early acute paronychia with erythema and tenderness but no fluctuance. Which is the most appropriate initial treatment?",
   opts=[
     ["Warm water soaks for twenty minutes three times daily",
      "Correct. Incision and drainage is reserved for severe cases with purulent collection."],
     ["Incision and drainage under digital block anaesthesia",
      "That is for severe cases where pus has collected."],
     ["A broad-spectrum topical antifungal applied twice daily",
      "That is the treatment of chronic paronychia."],
     ["Immediate removal of the nail plate under local block",
      "Nail removal is not the described treatment."]],
   c=0, cite=c(119)),

 dict(topic="Acute paronychia", io=IOA,
   q="A 22-year-old man who bites his nails has acute paronychia requiring an oral antibiotic. Which agent is specifically suggested for his exposure?",
   opts=[
     ["Clindamycin, because of exposure to oral flora",
      "Correct. Amoxicillin-clavulanate and cephalexin are the other named options."],
     ["Ciprofloxacin, because of exposure to oral flora",
      "Ciprofloxacin is named for resistant Pseudomonas folliculitis."],
     ["Doxycycline, because of exposure to oral flora",
      "Doxycycline is not the agent named for this exposure."],
     ["Penicillin V, because of exposure to oral flora",
      "Penicillin V is the erysipelas treatment."]],
   c=0, cite=c(119)),

 dict(topic="Acute paronychia", io=IOA,
   q="A 30-year-old woman has a painful swollen fingertip with grouped small vesicles at the lateral nail fold. Which test would settle the diagnosis?",
   opts=[
     ["Tzanck smear, to rule out herpetic whitlow",
      "Correct. Potassium hydroxide rules out candida and Gram stain identifies bacteria."],
     ["Potassium hydroxide preparation, to rule out candida",
      "That addresses a different differential than the vesicles suggest."],
     ["Wood's lamp examination, to rule out erythrasma",
      "That fluorescence test applies to intertriginous skin."],
     ["Gram stain and culture, to identify the bacterial cause",
      "That would not identify the viral cause the vesicles suggest."]],
   c=0, cite=c(118)),

 dict(topic="Chronic paronychia", io=IOA,
   q="A 44-year-old bartender has had swollen, tender nail folds on several fingers for four months, with thickened discoloured nails and cuticles that have separated from the nail plate. Which is the most likely diagnosis?",
   opts=[
     ["Chronic paronychia",
      "Correct — an inflammatory reaction to irritants over at least six weeks, with Candida albicans commonest."],
     ["Acute paronychia",
      "That comes on within days of trauma and is often fluctuant."],
     ["Onychomycosis",
      "That thickens the nail plate without inflaming the nail folds."],
     ["Nail psoriasis",
      "That produces pitting and onycholysis rather than nail fold inflammation."]],
   c=0, cite=c(122)),

 dict(topic="Chronic paronychia", io=IOA,
   q="A 39-year-old dishwasher is diagnosed with chronic paronychia. Which is the most appropriate treatment?",
   opts=[
     ["Keep the hands as dry as possible and use a broad-spectrum topical antifungal",
      "Correct, with oral fluconazole reserved for severe cases."],
     ["Warm soaks three times daily and incision if any purulent material collects",
      "That is the treatment of acute paronychia."],
     ["A ten-day course of oral cephalexin covering staphylococci and streptococci",
      "Antibacterial therapy does not address the usual candidal cause."],
     ["Topical mupirocin to the nail folds until the swelling has fully resolved",
      "Mupirocin is an antibacterial used for impetigo and carriage."]],
   c=0, cite=c(123)),

 dict(topic="Necrotizing fasciitis", io=IOA,
   q="A 58-year-old man with alcohol use disorder has severe pain in the thigh that is far worse than the modest erythema on examination. He was diagnosed with cellulitis two days ago and is no better on oral antibiotics. Which is the most likely diagnosis?",
   opts=[
     ["Necrotizing fasciitis",
      "Correct — pain out of proportion to examination, and no response to antibiotics at forty-eight hours."],
     ["Progressing cellulitis needing intravenous therapy",
      "That would not explain pain out of proportion to the findings."],
     ["Deep vein thrombosis of the femoral vein",
      "That produces swelling and pain without this pattern."],
     ["Compartment syndrome from an unnoticed injury",
      "That can complicate the condition but is not the diagnosis here."]],
   c=0, cite=c(126)),

 dict(topic="Necrotizing fasciitis", io=IOA,
   q="A 63-year-old woman with suspected necrotizing fasciitis is febrile and hypotensive. The surgical team is available now. Which is the most appropriate next step?",
   opts=[
     ["Proceed to surgical debridement, since tests and imaging must not delay intervention",
      "Correct — it is a surgical emergency with high mortality."],
     ["Complete computed tomography of the limb before any operative decision is taken",
      "Imaging must not delay surgery."],
     ["Await blood culture results before committing the patient to an operation",
      "Cultures are sent but do not gate the operation."],
     ["Trial forty-eight hours of broad intravenous antibiotics and then reassess",
      "Antibiotics alone are inadequate for this condition."]],
   c=0, cite=c(128)),

 dict(topic="Necrotizing fasciitis", io=IOA,
   q="A 55-year-old man with necrotizing fasciitis of the leg reports that the area, previously exquisitely tender, is now numb. Which explains this change?",
   opts=[
     ["The superficial nerves have been destroyed as the infection advanced",
      "Correct, alongside skin colour changing to blue-grey, bullae and cutaneous gangrene."],
     ["The inflammatory response has begun to resolve with antibiotic therapy",
      "Loss of tenderness here signals progression rather than recovery."],
     ["The infection has been walled off by the fascial plane it is spreading in",
      "The fascial planes are the route of spread, not a barrier."],
     ["The analgesia given on admission has reached its full therapeutic effect",
      "The change is a physical sign rather than an analgesic effect."]],
   c=0, cite=c(127)),

 dict(topic="Necrotizing fasciitis", io=IOA,
   q="A 61-year-old man with suspected necrotizing fasciitis of the thigh has a computed tomography scan showing gas in the soft tissue fascial planes. Which organism does this suggest?",
   opts=[
     ["Clostridium perfringens, since gas is not present with Group A streptococcus",
      "Correct. Ultrasound also demonstrates air bubbles in soft tissue."],
     ["Group A streptococcus, since gas is not present with Clostridium perfringens",
      "That reverses the two organisms."],
     ["Staphylococcus aureus, which produces gas through epidermolytic toxins",
      "Those toxins split the epidermis in bullous impetigo instead."],
     ["Pseudomonas aeruginosa, which produces gas in inadequately perfused tissue",
      "That organism is associated with hot tub folliculitis here."]],
   c=0, cite=c(129)),

 dict(topic="Necrotizing fasciitis", io=IOA,
   q="A 60-year-old man has confirmed necrotizing fasciitis. Which combination of care is required?",
   opts=[
     ["Aggressive surgical debridement, broad antibiotic cover and surgical intensive care admission",
      "Correct — cover aerobic Gram-positive and Gram-negative organisms and anaerobes, with a team approach."],
     ["Broad intravenous antibiotics with observation on a general ward for forty-eight hours",
      "Antibiotics alone are inadequate; debridement is required."],
     ["Bedside incision and drainage followed by discharge on oral antibiotic therapy",
      "That approach belongs to a simple abscess."],
     ["Elevation with warm compresses and a narrow-spectrum oral antibiotic course",
      "That is far below the level of care required."]],
   c=0, cite=c(131)),

 dict(topic="Necrotizing fasciitis", io=IOA,
   q="A 48-year-old man is admitted with necrotizing fasciitis after dental sepsis. Which referrals should be arranged?",
   opts=[
     ["A team approach with surgical intensive care, ideally at a burn or trauma centre",
      "Correct — consultations are described as necessary rather than optional."],
     ["Dermatology alone, since the presenting problem is a skin infection",
      "The disease is deeper than skin and needs surgical management."],
     ["Infectious diseases alone, since antibiotic selection determines outcome",
      "Antibiotics matter but debridement is the definitive treatment."],
     ["Wound care nursing alone, with review by the general team each day",
      "That level of care is far below what this condition requires."]],
   c=0, cite=c(131)),

 dict(topic="MRSA considerations", io=IOB,
   q="A 36-year-old man has a drained furuncle growing methicillin-resistant Staphylococcus aureus. He asks why the first antibiotic did not work. Which is the most appropriate explanation?",
   opts=[
     ["The empiric agents cephalexin and dicloxacillin do not cover this resistant organism",
      "Correct — the culture is what redirects therapy to trimethoprim-sulfamethoxazole, clindamycin or doxycycline."],
     ["The organism was not reached because the lesion had not yet been drained at all",
      "The lesion was drained, and the culture identifies the resistance."],
     ["The antibiotic was taken for too short a period to eradicate any skin infection",
      "Duration is not what the culture result indicates here."],
     ["The organism produces epidermolytic toxins that inactivate oral antibiotics",
      "Those toxins split the epidermis in bullous impetigo."]],
   c=0, cite=c(66)),

 dict(topic="Primary vs secondary infection", io=IOC,
   q="A 9-year-old girl with atopic dermatitis of the flexures develops weeping honey-coloured crusting over the affected eczema. Which best describes the infection?",
   opts=[
     ["A secondary bacterial infection of skin already damaged by another condition",
      "Correct — bullous impetigo can secondarily invade pre-existing lesions such as eczema."],
     ["A primary bacterial infection arising in previously normal intact skin",
      "The eczema is the pre-existing lesion that has been invaded."],
     ["A primary fungal infection of skin already damaged by another condition",
      "The honey-coloured crusting describes a bacterial infection."],
     ["A foreign body reaction within skin already damaged by another condition",
      "That describes pseudofolliculitis barbae."]],
   c=0, cite=c(89)),
]
