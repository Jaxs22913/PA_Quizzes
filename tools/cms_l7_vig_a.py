# CMS I Lecture 7 (Benign Skin Lesions) — SET 2, vignette pool A.
# Corns and calluses, keloid and hypertrophic scar, cutaneous horn, skin tags.
#
# LEAD-INS ARE EXPLICIT. Every question carries lead=, because a stem reading
# "which is the most appropriate response?" does not say on its face whether it
# is testing management, mechanism or counselling, and the skew guard has to be
# able to classify all of them. Lecture 5's build failed that guard at 15 of 30
# diagnosis lead-ins; a catalogue-of-lesions deck invites exactly that.
#
# Distractors are RIGHT-DISEASE-WRONG-PHASE or the neighbouring lesion in the
# same differential, so eliminating them takes knowledge rather than shape.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "7. Benign Skin Lesions Prof Griffenkranz 8-25-2025-2.pptx"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Objective a — Compare and contrast the etiologies, epidemiology, risk factors, clinical manifestations, differential diagnosis, diagnostic testing (including ordering and interpretation), management (including applicable rehabilitative and palliative care), appropriate referrals, patient education, and prognosis for benign skin lesions"
IOB = "Objective b — Identify medical strategies for common benign skin lesions in infants, adolescents, adults and the elderly"

VIG_A = [
 dict(topic="Clavus (corn)", io=IOA, lead="diagnosis",
   q="A 34-year-old woman who wears narrow dress shoes has a painful lesion on the dorsal aspect of her fifth toe. It is under a centimetre, sharply demarcated, and the skin lines run through it. Pressing straight down on it reproduces her pain. Which is the most likely diagnosis?",
   opts=[
     ["Hard corn",
      "Correct — a well-defined lesion, tender on direct pressure, with skin lines running through."],
     ["Verruca vulgaris",
      "A wart interrupts the skin lines and hurts on side pressure rather than direct."],
     ["Callus",
      "A callus is larger, irregular and usually painless."],
     ["Soft corn",
      "A soft corn sits in the fourth-to-fifth web space, macerated by moisture."]],
   c=0, cite=c(4)),

 dict(topic="Clavus (corn)", io=IOA, lead="diagnosis",
   q="A 41-year-old runner has a tender lesion in the web space between the fourth and fifth toes. It is whitish and boggy rather than hard. Which is the most likely diagnosis?",
   opts=[
     ["Soft corn",
      "Correct — clavus mollum, softened by moisture trapped between the toes."],
     ["Hard corn",
      "That sits on the dorsal and lateral fifth toe and is firm."],
     ["Callus",
      "A callus forms over the balls of the feet or the palms, and is diffuse."],
     ["Plantar wart",
      "A wart interrupts the skin lines and is not specific to a web space."]],
   c=0, cite=c(4)),

 dict(topic="Callus", io=IOA, lead="diagnosis",
   q="A 52-year-old carpenter has thickened, poorly demarcated, painless skin across both palms. The skin lines run through the thickened area. Which is the most likely diagnosis?",
   opts=[
     ["Callus",
      "Correct — broad-area pressure, diffuse thickening, no central core, painless."],
     ["Hard corn",
      "A corn is well defined, under one and a half centimetres, and painful on direct pressure."],
     ["Verruca vulgaris",
      "A wart interrupts the skin lines and has a blackened centre."],
     ["Keratoacanthoma",
      "That is a solitary dome-shaped nodule with a central keratin crater."]],
   c=0, cite=c(6)),

 dict(topic="Verruca vulgaris", io=IOA, lead="diagnosis",
   q="A 19-year-old has a rough lesion on the back of his hand with a cauliflower-like surface and small black dots at the centre. The skin lines stop at its edge. Squeezing it from the sides hurts more than pressing on it. Which is the most likely diagnosis?",
   opts=[
     ["Verruca vulgaris",
      "Correct — interrupted skin lines, blackened centre, and pain on side pressure."],
     ["Clavus",
      "A corn preserves the skin lines and hurts on direct downward pressure."],
     ["Callus",
      "A callus is diffuse, painless, and lets the skin lines run through."],
     ["Cutaneous horn",
      "A horn is a hard conical projection rather than a cauliflower-like plaque."]],
   c=0, cite=c(8)),

 dict(topic="Corns and calluses", io=IOA, lead="treatment",
   q="A 63-year-old man with type 2 diabetes mellitus has a painful corn on his fifth toe. Which is the most appropriate management?",
   opts=[
     ["Refer him to podiatry",
      "Correct — the deck flags the diabetic patient specifically for podiatry referral."],
     ["Start an over-the-counter salicylic acid product and review in a month",
      "Keratolytics are reasonable in general, but the diabetic foot is referred."],
     ["Pare the lesion down in clinic and advise wider footwear",
      "Padding and footwear help, but the diabetic patient needs specialist care."],
     ["Excise the lesion with a five-millimetre margin",
      "Those margins belong to keratoacanthoma."]],
   c=0, cite=c(9)),

 dict(topic="Corns and calluses", io=IOA, lead="education",
   q="A 29-year-old asks how to stop her calluses coming back. Which is the most appropriate advice?",
   opts=[
     ["Well-fitting shoes and socks, and pads inside the shoe",
      "Correct — remove the friction and the lesion stops re-forming. Tight shoes and high heels are named as causes, as is wearing shoes without socks."],
     ["Apply sunscreen daily and examine the skin periodically",
      "That is the general benign-lesion counselling point."],
     ["Avoid ear piercing and other cosmetic procedures",
      "That advice is for the keloid-prone patient."],
     ["Reposition every two hours and keep the skin clean and dry",
      "Those are pressure injury prevention measures."]],
   c=0, cite=c(10)),

 dict(topic="Keloid", io=IOA, lead="diagnosis",
   q="A 22-year-old woman of African descent had her ears pierced eight months ago. She now has a firm, bulbous nodule on the earlobe that has slowly enlarged and now extends well past the original piercing site. Which is the most likely diagnosis?",
   opts=[
     ["Keloid",
      "Correct — extension beyond the original wound margins is the defining feature."],
     ["Hypertrophic scar",
      "That stays within the wound margins and regresses with time."],
     ["Dermatofibroma",
      "That is a firm dermal nodule with a pigmented halo and a dimple sign."],
     ["Foreign-body granuloma",
      "That is in the differential, but it does not extend beyond the wound in this way."]],
   c=0, cite=c(13)),

 dict(topic="Hypertrophic scar", io=IOA, lead="diagnosis",
   q="A 30-year-old man had an appendicectomy five weeks ago. The scar is raised, firm and red but stops exactly at the edges of the original incision. Which is the most likely diagnosis?",
   opts=[
     ["Hypertrophic scar",
      "Correct — it developed within four weeks and is confined to the wound margins."],
     ["Keloid",
      "A keloid develops slowly and extends beyond the wound site."],
     ["Foreign-body granuloma",
      "That would suggest retained suture material rather than this pattern."],
     ["Dermatofibroma",
      "That is a discrete nodule, usually on a limb, rather than a linear scar."]],
   c=0, cite=c(21)),

 dict(topic="Hypertrophic scar", io=IOA, lead="education",
   q="The same patient asks what will happen to his scar over the next year. Which is the most appropriate answer?",
   opts=[
     ["It should stay stable and then flatten with time",
      "Correct — that natural history is the reason observation is reasonable."],
     ["It will keep enlarging for months to years and will not regress",
      "That is the keloid's course, not the hypertrophic scar's."],
     ["It will grow rapidly for two months and then regress over six",
      "That triphasic pattern belongs to keratoacanthoma."],
     ["It will remain unchanged and grow only in proportion to his body",
      "That is nevus flammeus."]],
   c=0, cite=c(21)),

 dict(topic="Keloid", io=IOA, lead="treatment",
   q="A 26-year-old with a keloid on the sternum wants it removed. Which is the most appropriate advice about surgical excision alone?",
   opts=[
     ["Recurrence is fifty to one hundred per cent, so steroid injection follows",
      "Correct — the recurrent lesion is often larger than the original, which is why excision is never done alone. Combination therapy has the best success rates."],
     ["Recurrence is under five per cent, so excision alone is usually curative",
      "That figure is far below what the deck reports."],
     ["Excision is contraindicated in keloids because it always causes bleeding",
      "Bleeding is not the reason excision alone is avoided."],
     ["Excision is preferred over all other options because it removes the fibrous tissue completely",
      "It removes the tissue, but the recurrence rate is the problem."]],
   c=0, cite=c(18)),

 dict(topic="Keloid", io=IOA, lead="treatment",
   q="A 35-year-old with a keloid asks about the silicone sheets a friend used. Which is the most appropriate description of how they are used?",
   opts=[
     ["Worn twelve to twenty-four hours a day for up to a year",
      "Correct — theorised to raise scar temperature and increase collagenase activity."],
     ["Applied for twenty minutes twice daily for six weeks",
      "The schedule is near-continuous and lasts far longer than this."],
     ["Worn only at night for the first month after surgery",
      "Overnight-only wear is not what is described."],
     ["Applied once weekly in clinic under an occlusive dressing",
      "This is a patient-applied therapy worn most of the day."]],
   c=0, cite=c(16)),

 dict(topic="Keloid", io=IOA, lead="treatment",
   q="A patient is offered compression therapy for a keloid. Which regimen matches the lecture?",
   opts=[
     ["Twenty-five millimetres of mercury, round the clock, six to twelve months",
      "Correct — the mechanism is not understood, but it possibly induces tissue hypoxia with fibroblast degeneration and subsequent collagen degradation."],
     ["Twenty-five millimetres of mercury, twelve hours a day, for six weeks",
      "The pressure is right but the schedule is far shorter than described."],
     ["Forty millimetres of mercury, overnight, for three months",
      "Neither the pressure nor the duration matches."],
     ["Fifteen millimetres of mercury, continuously, for one month",
      "Both the pressure and the duration are below what is specified."]],
   c=0, cite=c(17)),

 dict(topic="Keloid", io=IOA, lead="next step",
   q="A 40-year-old has a raised scar and you are not certain whether it is a keloid or something else. Which is the most appropriate next step?",
   opts=[
     ["Diagnose clinically; biopsy only if there is real doubt",
      "Correct — biopsy may itself induce new scarring, so the diagnostic act can provoke the disease it is investigating."],
     ["Biopsy every raised scar, because histology is the only way to be certain",
      "Routine biopsy is what the deck warns against here."],
     ["Excise it immediately and send the whole specimen",
      "Excision alone recurs at fifty to one hundred per cent."],
     ["Obtain magnetic resonance imaging of the lesion",
      "Imaging plays no part in diagnosing a scar."]],
   c=0, cite=c(14)),

 dict(topic="Keloid", io=IOB, lead="education",
   q="A 15-year-old with moderate acne has a family history of keloids. Which is the most appropriate counselling point?",
   opts=[
     ["Treat the acne early and appropriately",
      "Correct — acne is one of the named keloid triggers, and early appropriate treatment greatly increases the chance of scar-free healing."],
     ["Wait until the acne resolves on its own before starting any treatment",
      "Delay is the opposite of what is advised."],
     ["Begin silicone sheeting over the acne-prone areas now",
      "Silicone sheeting treats an existing scar rather than preventing acne."],
     ["Avoid all topical acne therapy, since it provokes fibrous overgrowth",
      "No such avoidance is described."]],
   c=0, cite=c(20)),

 dict(topic="Keloid", io=IOA, lead="education",
   q="A patient prone to keloids has just had a lesion excised. Which post-operative advice is most appropriate?",
   opts=[
     ["Do not stretch the immature scar, avoid hot baths, keep it clean",
      "Correct — stretching provokes scar inflammation and overgrowth, and hot baths can aggravate surgery-induced inflammation."],
     ["Massage the scar vigorously twice daily and expose it to sunlight",
      "Both of these run against the advice given."],
     ["Apply an over-the-counter keratolytic to thin the scar",
      "Keratolytics are for corns and calluses."],
     ["Take warm baths daily to soften the tissue",
      "Hot baths are specifically to be avoided."]],
   c=0, cite=c(20)),

 dict(topic="Cutaneous horn", io=IOA, lead="next step",
   q="A 71-year-old man has a firm, hard, conical projection on the helix of his ear that looks like a small animal horn. Which is the most appropriate next step?",
   opts=[
     ["Deep shave biopsy, to sample the tissue at the base",
      "Correct — there is often no clinical feature separating benign from malignant."],
     ["Reassure him, since a cutaneous horn is a benign keratin projection",
      "The horn is keratin, but what sits under it may be a carcinoma."],
     ["Cryotherapy to the projection, with review in three months",
      "Freezing the horn does not address the process at its base."],
     ["Dermoscopy alone, which will identify the underlying lesion",
      "Dermoscopy is not what the deck offers for this lesion."]],
   c=0, cite=c(27)),

 dict(topic="Cutaneous horn", io=IOA, lead="diagnosis",
   q="A biopsy at the base of a patient's cutaneous horn returns squamous cell carcinoma. Which statement best explains the significance of the horn itself?",
   opts=[
     ["The horn is only keratin; the process at its base is what matters",
      "Correct — horns arise from both benign and malignant lesions."],
     ["The horn indicates malignancy in every case in which it appears",
      "Horns also arise from warts, actinic and seborrheic keratoses."],
     ["The horn indicates a benign process, and the biopsy is a false positive",
      "That is not a conclusion the deck supports."],
     ["The horn's height predicts whether the base is malignant",
      "Height is not described as carrying diagnostic weight."]],
   c=0, cite=c(25)),

 dict(topic="Cutaneous horn", io=IOA, lead="test",
   q="Four patients each have a hard, hornlike keratotic projection. Which of them best matches the epidemiology the lecture gives for cutaneous horn?",
   opts=[
     ["A 62-year-old Caucasian with a lesion on the ear",
      "Correct — Caucasians over fifty, on head, neck and upper extremities."],
     ["A 14-year-old girl with lesions on the eyelids",
      "That is the syringoma profile."],
     ["A 3-month-old with a bright red lesion on the scalp",
      "That is the infantile hemangioma."],
     ["A 28-year-old pregnant woman with a bleeding finger lesion",
      "That is pyogenic granuloma."]],
   c=0, cite=c(26)),

 dict(topic="Acrochordon", io=IOA, lead="diagnosis",
   q="A 58-year-old woman with obesity has several soft, skin-coloured, pedunculated papules on a thin stalk in both axillae and on her neck. They are asymptomatic. Which is the most likely diagnosis?",
   opts=[
     ["Acrochordon",
      "Correct — friction sites, obesity, female, and a narrow stalk with a broad tip."],
     ["Cutaneous neurofibroma",
      "Those begin at puberty and are nerve sheath tumours, not friction-related."],
     ["Seborrheic keratosis",
      "Those are waxy stuck-on plaques rather than stalked papules."],
     ["Sebaceous hyperplasia",
      "Those are whitish-yellow papules with central umbilication, on the face."]],
   c=0, cite=c(29)),

 dict(topic="Acrochordon", io=IOA, lead="treatment",
   q="The same patient wants the lesions removed for cosmetic reasons. Which is the most appropriate approach?",
   opts=[
     ["Scissor excision, cryotherapy or electrodesiccation, without anesthesia",
      "Correct — anesthesia is stated not to be necessary."],
     ["Elliptical excision with five-millimetre margins under local anesthesia",
      "Those margins belong to keratoacanthoma."],
     ["Intralesional corticosteroid injection at monthly intervals",
      "That is a scar treatment."],
     ["Referral to a vascular anomalies specialist",
      "That referral belongs to infantile hemangioma."]],
   c=0, cite=c(30)),

 dict(topic="Acrochordon", io=IOA, lead="education",
   q="A patient asks whether she can remove a skin tag herself with nail scissors. Which is the most appropriate response?",
   opts=[
     ["She should not, because skin tags bleed when they come off",
      "Correct — and a new tag often forms in the same area anyway."],
     ["She may, provided she sterilises the scissors first",
      "The deck advises against home removal outright."],
     ["She should first apply a keratolytic for two weeks to soften it",
      "Keratolytics are for corns and calluses."],
     ["She should not, because skin tags are premalignant",
      "Skin tags are harmless growths of normal skin."]],
   c=0, cite=c(31)),

 dict(topic="Wound healing", io=IOA, lead="education",
   q="A patient asks why her surgical scar has become stronger over the past year. Which explanation is most appropriate?",
   opts=[
     ["Progressive cross-linking of collagen fibers as the scar matures",
      "Correct — the remodeling phase of wound healing."],
     ["Progressive proliferation of endothelial cells within the scar",
      "That process drives infantile hemangioma."],
     ["Progressive accumulation of keratin beneath the scar surface",
      "That describes an epidermoid cyst."],
     ["Progressive replacement of collagen by adipose tissue",
      "That is not part of normal wound healing."]],
   c=0, cite=c(11)),

 dict(topic="Keloid", io=IOA, lead="treatment",
   q="A patient's keloid has been treated with laser. Which addition does the lecture say gives the best result?",
   opts=[
     ["Combining the laser with intralesional steroids",
      "Correct — laser works by shrinking collagen or inducing microvascular thrombosis."],
     ["Combining the laser with over-the-counter keratolytics",
      "Keratolytics have no role in keloid treatment."],
     ["Combining the laser with oral antibiotics",
      "Antibiotics are used for an inflamed epidermoid cyst, not here."],
     ["Combining the laser with beta-blockade",
      "Beta-blockade is the infantile hemangioma treatment."]],
   c=0, cite=c(19)),

 dict(topic="Keloid", io=IOA, lead="test",
   q="A keloid is treated with cryotherapy. Which outcome should the patient be warned about?",
   opts=[
     ["Hypopigmentation at the treated site",
      "Correct — cryotherapy flattens lesions but can lighten the skin."],
     ["Tissue atrophy at the treated site",
      "That is the caution attached to intralesional steroid."],
     ["Permanent loss of sensation at the site",
      "Sensory loss is not a described effect."],
     ["Recurrence in one hundred per cent of cases",
      "That figure belongs to surgical excision performed alone."]],
   c=0, cite=c(19)),
]
