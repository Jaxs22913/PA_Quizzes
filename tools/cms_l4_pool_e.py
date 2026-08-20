# CMS I Lecture 4 (Cutaneous Bacterial Infections) — pool E.
#
# WRITTEN FROM THE 2026-08-19 LECTURE RECORDING, not from the deck. Pools A to D
# were built before the audio existed. These are the places where Professor
# Jaquith flagged a slide out loud, gave a prescribing detail that is on no
# slide, or handed out an exam heuristic.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "4.  Cutaneous Bacterial Infections.pptx"
REC = "2026-08-19 lecture recording"
def c(n): return f"{SRC}, Slide {n}"
def r(t): return f"{REC}, {t}"

IOA = "Objective a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing, management, referrals, patient education and prognosis of cutaneous bacterial infections"
IOB = "Objectives b, c & d — MRSA, primary versus secondary infection, and care across the age range"

POOL_E = [
 dict(topic="Acne vulgaris", io=IOA, slot="first-line",
   q="Which slides did Professor Jaquith name out loud as really important, and what are they?",
   opts=[
     ["The acne treatment ladder, slides 32 and 33",
      "Correct — she said 'make sure you know this', which is as direct a flag as the lecture gives."],
     ["The MRSA risk factor list, slides 44 and 45",
      "Not the slides she named."],
     ["The cellulitis versus erysipelas comparison",
      "Important content, but not the slides she flagged."],
     ["The necrotizing fasciitis red flags",
      "Not the slides she flagged."]],
   c=0, cite=r("15:40")),

 dict(topic="Acne vulgaris", io=IOA, slot="escalation",
   q="On the ladder she flagged, what is added for MODERATE acne with pustules?",
   opts=[
     ["A topical retinoid, an ORAL antibiotic, and benzoyl peroxide",
      "Correct — the severe tier is the same three, or oral isotretinoin instead."],
     ["A topical retinoid and benzoyl peroxide, with no oral agent",
      "That is the mild mixed tier; moderate adds an oral antibiotic."],
     ["Oral isotretinoin used as the sole agent from the outset",
      "Isotretinoin is the severe tier."],
     ["Azelaic acid used on its own as a single topical",
      "Azelaic acid is the alternative when a topical retinoid is not tolerated in mild disease."]],
   c=0, cite=r("15:25")),

 dict(topic="Acne vulgaris", io=IOA, slot="education",
   q="Why did Professor Jaquith say not to apply topical tretinoin and benzoyl peroxide together, and what should the patient do instead?",
   opts=[
     ["Because of irritation; use the retinoid at night and benzoyl peroxide during the day",
      "Correct — none of this timing advice is on a slide."],
     ["Because benzoyl peroxide inactivates the retinoid; use them on alternate days",
      "Irritation was the reason she gave, and the fix was time of day."],
     ["Because the combination bleaches fabric; apply both in the morning",
      "Bleaching is real but is not the reason she gave."],
     ["Because absorption is reduced; apply the retinoid an hour before",
      "Absorption was not the concern described."]],
   c=0, cite=r("16:30")),

 dict(topic="Acne vulgaris", io=IOA, slot="education",
   q="Which washing advice did Professor Jaquith give for acne?",
   opts=[
     ["Twice a day at most, gentle cleanser, warm not hot water",
      "Correct — hot water strips the barrier. She also said four to six weeks before improvement, avoid oil-based make-up, and do not pick, because picking is what scars."],
     ["At least three times a day with an antibacterial cleanser and hot water",
      "Over-washing and hot water are exactly what she advised against."],
     ["Once a week only, to avoid removing sebum",
      "Twice a day is the ceiling she gave, not the floor."],
     ["Whenever the skin feels oily, using an exfoliating scrub",
      "Frequent scrubbing is not what she recommended."]],
   c=0, cite=r("16:43")),

 dict(topic="MRSA", io=IOB, slot="agent/regimen",
   q="What is Professor Jaquith's simplified default when methicillin-resistant Staphylococcus aureus is suspected?",
   opts=[
     ["Cephalexin plus trimethoprim-sulfamethoxazole",
      "Correct — double strength, and the combination is broad enough to cover before susceptibilities return, which then confirm."],
     ["Cephalexin alone at a higher dose",
      "Cephalexin is the standard agent, but it does not cover the resistant organism."],
     ["Trimethoprim-sulfamethoxazole double strength alone",
      "She described adding it to cephalexin rather than replacing it."],
     ["Intravenous vancomycin as an outpatient",
      "That is not the oral outpatient default she described."]],
   c=0, cite=r("23:31")),

 dict(topic="Folliculitis", io=IOA, slot="agent/regimen",
   q="Professor Jaquith said to write Bactroban as the ointment rather than the cream. Why?",
   opts=[
     ["The cream costs far more and is never covered",
      "Correct — roughly a hundred times the price, and the ointment is covered. A prescribing detail that appears on no slide."],
     ["The cream is less effective against Staphylococcus aureus",
      "The reason she gave was cost and coverage, not potency."],
     ["The cream causes more contact irritation on inflamed skin",
      "Irritation was not the reason she gave."],
     ["The cream is not licensed for use on the face",
      "No licensing restriction was described."]],
   c=0, cite=r("22:12")),

 dict(topic="Folliculitis", io=IOA, slot="escalation",
   q="A patient has recurrent folliculitis. What did Professor Jaquith describe doing?",
   opts=[
     ["Check for carriage, then nasal mupirocin for five days",
      "Correct — checking whether they carry Staphylococcus aureus and decolonising the nares. She noted the pre-filled swabs were discontinued, so it is applied manually now."],
     ["Start a six-week course of oral doxycycline",
      "That is an acne regimen rather than a decolonisation one."],
     ["Refer for surgical excision of the affected follicles",
      "Excision is not what she described."],
     ["Switch from shaving to depilatory cream permanently",
      "Shaving is a trigger, but the decolonisation step is what she described."]],
   c=0, cite=r("22:56")),

 dict(topic="Cellulitis", io=IOA, slot="escalation",
   q="Professor Jaquith treats a small-surface-area non-purulent cellulitis as an outpatient. What follow-up does she insist on, and why?",
   opts=[
     ["Return in 24 to 48 hours, because it spreads so fast",
      "Correct — to confirm the antibiotic is working. That interval is the safety net on outpatient treatment."],
     ["Return in one week, once the course is complete",
      "A week is far longer than the interval she gave."],
     ["No routine follow-up unless the patient deteriorates",
      "She described a mandatory review rather than safety-netting alone."],
     ["Return in 72 hours for repeat blood cultures",
      "Blood cultures belong to the emergency department work-up she described separately."]],
   c=0, cite=r("1:01:43")),

 dict(topic="Necrotizing fasciitis", io=IOA, slot="etiology",
   q="What is the microbiology of necrotizing fasciitis, as Professor Jaquith described it?",
   opts=[
     ["Polymicrobial from mixed flora, or group A Streptococcus",
      "Correct — aerobic or anaerobic. She introduced it as the flesh-eating bacteria."],
     ["Always monomicrobial Staphylococcus aureus",
      "The infection is described as polymicrobial or group A streptococcal."],
     ["Always Pseudomonas aeruginosa from water exposure",
      "Pseudomonas is the hot tub folliculitis organism in this lecture."],
     ["Always methicillin-resistant Staphylococcus aureus",
      "Resistance is not what defines this infection."]],
   c=0, cite=r("1:10:15")),

 dict(topic="Bacterial infections overall", io=IOB, slot="etiology",
   q="What heuristic did Professor Jaquith give for a cutaneous bacterial infection question when you are not sure of the organism?",
   opts=[
     ["Guess Staphylococcus aureus, because it causes a lot of these conditions",
      "Correct — her words. Know the exceptions: erysipelas and ecthyma lean streptococcal, hot tub folliculitis is Pseudomonas."],
     ["Guess Streptococcus pyogenes, because it causes a lot of these conditions",
      "Streptococcus is the exception in a few conditions rather than the theme."],
     ["Guess Pseudomonas aeruginosa, because it causes a lot of these conditions",
      "Pseudomonas is specific to hot tub folliculitis here."],
     ["Guess a polymicrobial mixture, because most skin infections are mixed",
      "Polymicrobial is specific to necrotizing fasciitis in this lecture."]],
   c=0, cite=r("1:04:08")),

 dict(topic="Pseudofolliculitis barbae", io=IOB, slot="epidemiology",
   q="In whom did Professor Jaquith say pseudofolliculitis barbae most commonly occurs?",
   opts=[
     ["Black and brown males, or anyone with curlier facial or body hair",
      "Correct — hair curvature is the mechanism, not hygiene, and she called it very common."],
     ["Fair-skinned males who shave daily with a multi-blade razor",
      "Skin tone is not the driver; hair curvature is."],
     ["Females who wax rather than shave",
      "Not the group she named."],
     ["Adolescents of any background during puberty",
      "Age was not the factor she described."]],
   c=0, cite=r("26:14")),

 dict(topic="Folliculitis", io=IOA, slot="risk factors",
   q="Where and after what does Professor Jaquith say she sees folliculitis most often?",
   opts=[
     ["The groin, after shaving",
      "Correct — hot tubs come second, and hot tub folliculitis is the Pseudomonas one."],
     ["The scalp, after using hair oils",
      "Not the site or trigger she named."],
     ["The lower legs, after swimming in fresh water",
      "Fresh-water exposure is cercarial dermatitis in a different lecture."],
     ["The face, after using an occlusive moisturiser",
      "Not the site or trigger she named."]],
   c=0, cite=r("17:37")),
]
