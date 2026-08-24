# -*- coding: utf-8 -*-
# CMS I Lecture 8 — SET 2, vignette pool D. NON-DIAGNOSIS LEAD-INS ONLY.
#
# WHY THIS EXISTS. Professor Jaquith's 24 August description of the exam: "there
# might be SOME question, what's the most likely diagnosis, but A LOT OF THEM
# are -- what's the next management plan? What's your first line treatment
# plan? ... what's the proper patient education?"
#
# The vignette partitions now cap diagnosis lead-ins at 6 of 30. Lecture 8's
# pool was the worst placed of the eight to meet that: 64 vignettes of which 26
# were diagnosis, leaving 38 non-diagnosis where two sets need 48. The cap
# failed the build with that arithmetic in the message rather than shipping a
# 37%-diagnosis paper. This pool supplies the ten it was short.
#
# EVERY LEAD-IN HERE IS next step, treatment, test or education. Asserted below.
#
# Content note: this lecture's management is unusually repetitive by design --
# she teaches it to one pattern (observe, biopsy if it changes) with two
# exceptions. Several vignettes below therefore turn on the EXCEPTIONS or on the
# specific counselling point, since a stem whose answer is "observe" for the
# fifth time tests nothing.
SRC = "CMS I Pigmented Skin Lesions - Shahsv-2.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = "Objective 1 — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (acute and chronic), appropriate referrals, patient education, and prognosis of pigmented skin lesions"
IOB = "Objective 11 — Identify medical care strategies for pigmented skin lesions for adult and elderly populations"

VIG_D = [
 dict(topic="Ephelides", io=IOA, lead="treatment",
   q="A 24-year-old with red hair and widespread freckling across her nose and cheeks asks what can be done about them. Which management does the deck support, and which must be avoided?",
   opts=[
     ["Sun protection, patient education and topical depigmenting agents; cryotherapy is NOT used",
      "Correct — cryotherapy is difficult because of the size of the lesions, so intense pulsed light or lasers are preferred."],
     ["Cryotherapy to each individual lesion, with sun protection counselling afterwards",
      "The deck states no cryotherapy for these, because of the lesion size."],
     ["Surgical excision of the most prominent lesions",
      "Excision is not offered for freckles."],
     ["No treatment of any kind is available or appropriate",
      "Depigmenting agents, intense pulsed light and lasers are all described."]],
   c=0, cite=c(7)),

 dict(topic="Ephelides", io=IOA, lead="education",
   q="A 26-year-old woman is booked for intense pulsed light treatment of her freckles. What must she be told to expect?",
   opts=[
     ["The lesions can relapse, so this is not necessarily permanent",
      "Correct — the deck says explicitly that lesions can relapse after light or laser treatment."],
     ["The result is permanent once a full course has been completed",
      "The deck warns of relapse."],
     ["Her freckles will darken before they fade, over about six weeks",
      "No such course is described."],
     ["She will need lifelong monthly maintenance treatments",
      "No maintenance schedule is given."]],
   c=0, cite=c(7)),

 dict(topic="Solar lentigo", io=IOA, lead="treatment",
   q="A 63-year-old asks about the flat brown patches on the backs of her hands. They are asymptomatic and unchanged. What is the most appropriate management?",
   opts=[
     ["No treatment is necessary; cosmetic removal by cryotherapy or quality-switched laser only if she wishes",
      "Correct — treatment is elective, not indicated."],
     ["Cryotherapy to all of the lesions, since solar lentigines are considered to be premalignant",
      "The deck does not treat them as premalignant, and treatment is not necessary."],
     ["Topical fluorouracil as field therapy across both hands",
      "Field therapy belongs to actinic keratosis in Lecture 9."],
     ["Excisional biopsy of the largest lesion to exclude melanoma",
      "Nothing in the stem raises that concern."]],
   c=0, cite=c(12)),

 dict(topic="Seborrheic keratosis", io=IOA, lead="treatment",
   q="A 70-year-old man wants several waxy stuck-on lesions on his trunk removed because they catch on his clothing. Which options does the deck give?",
   opts=[
     ["Retinoids, cryotherapy or quality-switched laser, since removal here is elective",
      "Correct — treatment is not necessary; removal is for cosmetic or symptomatic reasons."],
     ["Excision with a two-millimetre margin, because they are premalignant",
      "They are benign and excision with margins is not described."],
     ["Topical imiquimod five nights weekly for six weeks",
      "That regimen belongs to superficial basal cell carcinoma."],
     ["No intervention is available for symptomatic lesions",
      "Cosmetic removal is offered when the patient prefers it."]],
   c=0, cite=c(15)),

 dict(topic="Seborrheic keratosis", io=IOA, lead="education",
   q="A 69-year-old woman is about to have an irritated seborrhoeic keratosis frozen. What should she be told beforehand, and why does it matter?",
   opts=[
     ["That the lesion can come back after freezing, so she is not surprised or disappointed later",
      "Correct — she framed this as protecting the relationship as much as informing the patient."],
     ["That freezing is curative and the lesion will not return",
      "Recurrence after cryotherapy is exactly what the patient is warned about."],
     ["That the site will remain permanently depigmented",
      "That is not the counselling point given here."],
     ["That she will need a confirmatory biopsy afterwards to establish the diagnosis",
      "The diagnosis is clinical."]],
   c=0, cite=c(15)),

 dict(topic="Vitiligo", io=IOA, lead="treatment",
   q="A 29-year-old has depigmented patches over roughly three per cent of her body surface, mostly on her hands and around the mouth. Which first-line approach fits?",
   opts=[
     ["Topical therapy, with calcineurin inhibitors useful where steroids cannot be applied such as face and neck",
      "Correct — topical therapy suits under five per cent involvement, ideally combined with phototherapy."],
     ["Narrow-band ultraviolet B phototherapy as first line",
      "Phototherapy is first line above five per cent body surface area."],
     ["Tissue or cellular grafting as the definitive treatment",
      "Surgical grafting is only for highly stable disease."],
     ["Psoralen plus ultraviolet A therapy in preference to narrow-band ultraviolet B phototherapy",
      "Narrow-band ultraviolet B is preferred; psoralen therapy raises skin cancer risk."]],
   c=0, cite=c(24)),

 dict(topic="Vitiligo", io=IOA, lead="next step",
   q="A 35-year-old man has vitiligo affecting about fifteen per cent of his body surface. He has used topical steroids without benefit. What is the most appropriate next step?",
   opts=[
     ["Narrow-band ultraviolet B phototherapy, ideally combined with topical therapy",
      "Correct — phototherapy is first line above five per cent, and combination therapy is described as ideal."],
     ["Psoralen plus ultraviolet A, since it is more effective than narrow-band ultraviolet B",
      "Psoralen therapy carries increased skin cancer risk and narrow-band ultraviolet B is preferred."],
     ["Tissue grafting to the affected areas",
      "Surgery is reserved for highly stable disease."],
     ["Continue the same topical steroid for a further six months",
      "Topical therapy alone suits limited disease and has already failed here."]],
   c=0, cite=c(25)),

 dict(topic="Vitiligo", io=IOA, lead="education",
   q="A 31-year-old man with extensive vitiligo says the condition troubles him socially far more than physically. Which aspect of care does the deck single out alongside repigmentation?",
   opts=[
     ["Psychological intervention, alongside cosmetic and non-traditional therapies",
      "Correct — it is listed as part of management rather than as an afterthought."],
     ["Screening the whole family for autoimmune thyroid disease at diagnosis",
      "Not a step the deck lists here."],
     ["Annual skin cancer surveillance for every patient",
      "Skin cancer risk is raised in connection with psoralen therapy, not as routine surveillance."],
     ["Immediate referral for surgical grafting in all patients",
      "Grafting is reserved for highly stable disease."]],
   c=0, cite=c(25)),

 dict(topic="Congenital melanocytic naevus", io=IOA, lead="next step",
   q="A newborn has a large pigmented patch across the posterior midline of the neck and upper back. What does the deck require next?",
   opts=[
     ["Magnetic resonance imaging of the brain, with or without total spine, matched to where the naevus sits",
      "Correct — head, neck or posterior midline lesions raise neurocutaneous melanosis."],
     ["Immediate excision of the whole lesion before the child reaches six months of age or walks",
      "Management balances melanoma risk, cosmesis and function; it is not automatic early excision."],
     ["Observation alone, with review when the child starts school",
      "The midline site specifically triggers imaging."],
     ["Skin biopsy of the darkest area to exclude melanoma at birth",
      "Biopsy is sometimes needed, but the midline site is what drives imaging."]],
   c=0, cite=c(30)),

 dict(topic="Congenital melanocytic naevus", io=IOA, lead="education",
   q="The parents of a child with a very large congenital naevus ask what support exists. What does the deck point them towards, and what shapes the plan?",
   opts=[
     ["Counselling and support groups, with management balancing melanoma risk, cosmetic outcome and preserved function",
      "Correct — the goal is removing as much as possible while preserving function and improving appearance."],
     ["Counselling alone, since surgery is contraindicated in large naevi",
      "Surgery is ideal where there is enough skin for grafting."],
     ["Immediate referral for total surgical excision, regardless of whether a graft site is available",
      "If there is little skin for a graft site, observation may be the better option."],
     ["No specific support is described beyond routine dermatology follow-up",
      "Counselling and support groups are named explicitly."]],
   c=0, cite=c(31)),
]

_bad = [q["q"][:60] for q in VIG_D if q.get("lead") == "diagnosis" or not q.get("lead")]
assert not _bad, ("this pool exists to supply NON-diagnosis vignettes: %r" % _bad)
