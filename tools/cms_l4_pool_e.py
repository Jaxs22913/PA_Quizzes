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

IOA = "a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing, management, referrals, patient education and prognosis of cutaneous bacterial infections"
IOB = "b, c & d — MRSA, primary versus secondary infection, and care across the age range"

POOL_E = [
 dict(topic="Acne vulgaris", io=IOA, slot="first-line",
   q="A patient's acne has papules and pustules that have not settled on a topical retinoid with benzoyl peroxide. What is added next?",
   opts=[
     ["An oral antibiotic",
      "Correct — an oral antibiotic joins the topical retinoid and benzoyl peroxide at this rung."],
     ["A six-week oral corticosteroid",
      "Oral corticosteroids are not part of the acne ladder; moderate papulopustular acne adds an oral antibiotic to the retinoid and benzoyl peroxide."],
     ["Oral isotretinoin straight away",
      "Oral isotretinoin monotherapy is an option for severe, nodular acne; persistent papulopustular acne first adds an oral antibiotic to the topical pair."],
     ["A stronger topical retinoid",
      "A stronger retinoid is not the next rung; moderate papulopustular acne adds an oral antibiotic to the topical retinoid and topical benzoyl peroxide."]],
   c=0, cite=c(33)),

 dict(topic="Acne vulgaris", io=IOA, slot="escalation",
   q="Which regimen treats MODERATE acne with pustules?",
   opts=[
     ["A topical retinoid, an ORAL antibiotic, and benzoyl peroxide",
      "Correct — moderate papulopustular and mixed acne is treated with a topical retinoid, an oral antibiotic and topical benzoyl peroxide together."],
     ["A topical retinoid and benzoyl peroxide, with no oral agent",
      "A topical retinoid with benzoyl peroxide treats mild papulopustular or mixed acne; the moderate tier adds an oral antibiotic to the pair."],
     ["Oral isotretinoin used as the sole agent from the outset",
      "Oral isotretinoin monotherapy is an option for severe, nodular acne, not the regimen for moderate acne with pustules."],
     ["Azelaic acid used on its own as a single topical",
      "Azelaic acid replaces a topical retinoid that is not tolerated in comedonal acne; moderate acne needs a retinoid, an oral antibiotic and benzoyl peroxide."]],
   c=0, cite=c(33)),

 dict(topic="Acne vulgaris", io=IOA, slot="education",
   q="What is the correct advice for a patient using both topical tretinoin and benzoyl peroxide?",
   opts=[
     ["Because of irritation; use the retinoid at night and benzoyl peroxide during the day",
      "Correct — applying them together risks skin irritation, so the two are separated in time, with at least three hours between them."],
     ["Because benzoyl peroxide inactivates the retinoid; use them on alternate days",
      "The reason for separating them is skin irritation, and the fix is spacing them at least three hours apart rather than alternating days."],
     ["Because the combination bleaches fabric; apply both in the morning",
      "Fabric bleaching is not why they are kept apart; applying them together irritates the skin, so they are spaced at least three hours apart."],
     ["Because absorption is reduced; apply the retinoid an hour before",
      "Absorption is not the problem; applying both together risks skin irritation, so the two are separated by at least three hours."]],
   c=0, cite=r("16:30")),

 dict(topic="Acne vulgaris", io=IOA, slot="education",
   q="Which washing advice is appropriate for a patient with acne?",
   opts=[
     ["Twice a day at most, gentle cleanser, warm not hot water",
      "Correct — wash no more than twice daily using a gentle cleanser with warm, not hot, water, and avoid vigorous washing or scrubbing."],
     ["At least three times a day with an antibacterial cleanser and hot water",
      "Washing is limited to twice daily with warm water; more frequent washing and hot water are advised against."],
     ["Once a week only, to avoid removing sebum",
      "Once a week is too little; the face is washed up to twice daily, with twice daily as the upper limit rather than a minimum."],
     ["Whenever the skin feels oily, using an exfoliating scrub",
      "Vigorous washing and scrubbing are specifically avoided; a gentle cleanser is used with warm water no more than twice daily."]],
   c=0, cite=r("16:43")),

 dict(topic="MRSA", io=IOB, slot="agent/regimen",
   q="An abscess drains spontaneously, and methicillin-resistant Staphylococcus aureus is possible. How are antibiotics chosen?",
   opts=[
     ["Broad-spectrum cover, then adjusted to culture",
      "Correct — a spontaneously draining abscess gets warm soaks and broad-spectrum antibiotics that consider methicillin-resistant Staphylococcus aureus, changed according to the culture result."],
     ["No antibiotics until the culture result is available",
      "Antibiotics are not withheld; the draining abscess gets warm soaks and broad-spectrum cover at once, and the culture result then guides any change."],
     ["Narrow-spectrum penicillin V with no culture taken",
      "Penicillin V is the erysipelas agent; a draining abscess needs broad-spectrum cover with methicillin-resistant organisms in mind, then culture-guided changes."],
     ["Incision and drainage before any antibiotic is started",
      "Incision and drainage is for an abscess that does not drain on its own; a spontaneously draining abscess is managed with warm soaks and antibiotics."]],
   c=0, cite=c(115)),

 dict(topic="Folliculitis", io=IOA, slot="agent/regimen",
   q="For a limited number of non-bullous impetigo lesions, how does mupirocin (Bactroban) ointment compare with oral antibiotics?",
   opts=[
     ["It is as effective, with fewer side effects",
      "Correct — for a single or limited number of non-bullous lesions, mupirocin ointment is adequate for most impetigo and as effective as oral antibiotics, with fewer side effects."],
     ["It is less effective but better tolerated",
      "Mupirocin ointment is not less effective; it is adequate for most impetigo and as effective as oral antibiotics, with fewer side effects."],
     ["It works best with the crusts left in place",
      "Crusts should be removed before the ointment is applied rather than left in place; the ointment is then as effective as oral antibiotics."],
     ["It is reserved for bullous or widespread disease",
      "Topical therapy is for a single or limited number of non-bullous lesions; widespread disease is treated with oral antibiotics instead."]],
   c=0, cite=c(94)),

 dict(topic="Folliculitis", io=IOA, slot="escalation",
   q="A patient has recurrent folliculitis. What is the most appropriate next step?",
   opts=[
     ["Check for carriage, then nasal mupirocin for five days",
      "Correct — a nasal swab checks for Staphylococcus aureus carriage, then mupirocin ointment is applied in the nasal vestibule twice daily for five days."],
     ["Start a six-week course of oral doxycycline",
      "Doxycycline courses belong to acne; recurrent folliculitis calls for nasal decolonization with mupirocin instead."],
     ["Refer for surgical excision of the affected follicles",
      "Surgical excision has no role here; recurrent folliculitis is managed by checking for nasal carriage and decolonizing with mupirocin."],
     ["Switch from shaving to depilatory cream permanently",
      "Avoiding shaving may help, but recurrence calls for checking for Staphylococcus aureus carriage and decolonizing the nares."]],
   c=0, cite=r("22:56")),

 dict(topic="Cellulitis", io=IOA, slot="escalation",
   q="A patient with non-purulent cellulitis is treated with oral antibiotics as an outpatient. Which finding should prompt a change in antimicrobial therapy?",
   opts=[
     ["Fever that persists beyond 48 hours",
      "Correct — with antibiotic therapy the fever usually resolves in 24 hours, so fever lasting more than 48 hours calls for a change guided by culture results."],
     ["Inflammation still settling after one week",
      "Inflammation resolves slowly over one to two weeks, so redness still settling at one week is the expected course rather than treatment failure."],
     ["Redness that looks worse on the first day",
      "Cellulitis may look and feel worse during the first day of treatment, because pathogens destroyed suddenly release enzymes that increase local inflammation."],
     ["Fever that resolves within 24 hours",
      "Fever usually resolves within 24 hours of antibiotic therapy; that is the expected response, and only fever beyond 48 hours prompts a change."]],
   c=0, cite=c(112)),

 dict(topic="Necrotizing fasciitis", io=IOA, slot="etiology",
   q="What is the microbiology of necrotizing fasciitis?",
   opts=[
     ["Polymicrobial from mixed flora, or group A Streptococcus",
      "Correct — necrotizing fasciitis is polymicrobial, with aerobic, anaerobic or mixed flora, and group A streptococci (Streptococcus pyogenes) are common."],
     ["Always monomicrobial Staphylococcus aureus",
      "A single staphylococcal organism is not typical; necrotizing fasciitis is polymicrobial, with aerobic, anaerobic or mixed flora."],
     ["Always Pseudomonas aeruginosa from water exposure",
      "Pseudomonas aeruginosa from contaminated water causes hot tub folliculitis; necrotizing fasciitis is polymicrobial or group A streptococcal."],
     ["Always methicillin-resistant Staphylococcus aureus",
      "Methicillin-resistant Staphylococcus aureus is not the defining organism; the infection is polymicrobial, with group A streptococci common."]],
   c=0, cite=c(124)),

 dict(topic="Bacterial infections overall", io=IOB, slot="etiology",
   q="When the organism behind a cutaneous bacterial infection is uncertain, which assumption is most often right?",
   opts=[
     ["Guess Staphylococcus aureus, because it causes a lot of these conditions",
      "Correct — Staphylococcus aureus causes most of these infections; erysipelas is mostly group A streptococcal and hot tub folliculitis is Pseudomonas."],
     ["Guess Streptococcus pyogenes, because it causes a lot of these conditions",
      "Streptococcus is the exception in a few conditions rather than the theme."],
     ["Guess Pseudomonas aeruginosa, because it causes a lot of these conditions",
      "Pseudomonas is specific to hot tub folliculitis here."],
     ["Guess a polymicrobial mixture, because most skin infections are mixed",
      "Polymicrobial infection is specific to type I necrotizing fasciitis; across skin infections generally, Staphylococcus aureus is the commonest single organism."]],
   c=0, cite=r("1:04:08")),

 dict(topic="Pseudofolliculitis barbae", io=IOB, slot="epidemiology",
   q="In whom does pseudofolliculitis barbae most commonly occur?",
   opts=[
     ["Black males, or anyone who shaves and has curlier hair",
      "Correct — this foreign-body reaction to hair in shaved areas is common in Black males with tightly curled hair and keratin gene variations, and in anyone curly-haired who shaves."],
     ["Fair-skinned males who shave daily with a multi-blade razor",
      "Fair skin is not the risk factor; the reaction follows cut hair curving back into the follicle wall, so tightly curled or curlier hair predisposes."],
     ["Females who wax rather than shave",
      "Waxing is not the classic setting; this is a foreign-body reaction to hair in shaved areas, commonest in Black men with tightly curled hair."],
     ["Adolescents of any background during puberty",
      "Puberty is not the driver; pseudofolliculitis barbae is a reaction to shaved hair curving back into the skin, so hair curvature decides who gets it."]],
   c=0, cite=c(54)),

 dict(topic="Folliculitis", io=IOA, slot="risk factors",
   q="Which sites does folliculitis commonly affect?",
   opts=[
     ["Scalp, thighs, trunk, axilla, groin",
      "Correct — folliculitis forms small papules or pustules pierced by a central hair, commonly on the scalp, thighs, trunk, axilla and inguinal area."],
     ["Face, neck, palms and soles",
      "The face, neck, palms and soles are usually spared by hot tub Pseudomonas folliculitis, which favors the trunk, extremities and buttocks."],
     ["Lower legs after fresh-water swimming",
      "Swimming in infested fresh water causes cercarial dermatitis, or swimmer's itch, from penetrating flatworm larvae rather than folliculitis."],
     ["Proximal nail folds of the fingers",
      "The proximal nail fold is the site of paronychia; folliculitis involves hair follicles, commonly on the scalp, thighs, trunk, axilla and groin."]],
   c=0, cite=c(41)),
]
