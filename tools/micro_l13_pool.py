# -*- coding: utf-8 -*-
# Microbiology Exam 2, Lecture 13 — Miscellaneous Bacterial Agents of Disease (Dr. Fair, 16 October 2026).
# 70 slides: the spirochetes (Treponema, Leptospira, Borrelia), the curviform Gram-negatives (Vibrio,
# Campylobacter, Helicobacter), the bacteria of unique morphology (rickettsias, Coxiella, Bartonella,
# chlamydias, mycoplasmas) and bacteria in dental disease.
#
# ATTRIBUTION: the PAJ5200.* deck names no lecturer (her decks never do); the calendar row for 16 October
# 2026, 3-5 pm, names Dr. Fair. The recording is still to come; this pool is drafted from the deck alone
# and its weights are slide counts until the recording can re-weight them.
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the
# only "Correct:" opener; the partition rotates positions per set. `mis` names the misconception each
# distractor stands for (review metadata for tools/blind_review.py; the renderer strips it).
#
# GROUNDING: only what is VISIBLE on a slide counts (text and pictures); speaker notes do not ("prostitute's
# pupil", "CJT = Campylobacter jejuni toxin", the Lyme state incidences, "un-Gramstainable" are notes-only and
# are not used). Picture-only content used: slide 4 (endoflagella in the periplasmic space), slide 11 (the
# syphilis stage table), slide 25 (the relapsing-fever antigen and fever graph), slide 28 (the two-year Lyme
# tick cycle), slide 33 (the cholera water and electrolyte diagram), slide 41 (the biopsy urease gel), slide 47
# (the rickettsia table), slide 57 (the chlamydia life cycle), slide 66 (the dental disease flow chart).
#
# OBJECTIVES (syllabus, "Misc. Bacterial Agents of Human Diseases", two numbered objectives, verbatim in
# IO1/IO2). Objective 1 carries most of the deck, so the real coverage axis is the organism group in the
# topic field; objective 2 is tagged on every item that asks how the organism is acquired, its vector or
# its reservoir.
#
# DELIBERATELY NOT ASKED (held), and why:
#   - percentages and case counts (30% entering the tertiary stage, 50-70% with the bull's-eye rash, 90% of
#     ulcers, type O blood 1.5-2x, 50-60 leptospirosis cases a year, the infectious-dose numbers): trivia, and
#     her own scope is not yet known. "Why so large a dose" (it must first pass through the stomach) is asked.
#   - Helicobacter as a "spirochete": slide 31 calls it one, but slide 39 calls it "motile curved cells" and
#     slide 3 defines spirochetes by endoflagella inside the cell; the deck contradicts itself, so the point is
#     not tested (its several polar flagella, urease, ulcers and the biopsy gel are).
#   - "Rickettsioses ... only identified in the last 20-30 years" (slide 43): contradicted by the deck's own
#     1942-1945 typhus story on slide 45.
#   - spirochetes as "human pathogens" yet "not considered primary pathogens" (slide 3): self-contradictory.
#   - WHY the human Lyme vaccine was withdrawn: slide 26 says adverse effects, slide 27 says researchers found
#     no connection. That a dog vaccine exists and that the human vaccine was withdrawn IS asked.
#   - human GRANULOCYTIC ehrlichiosis as a key (slide 46/47; it is now called anaplasmosis): monocytic
#     ehrlichiosis and tick transmission are asked instead.
#   - "Typhinia"; secondary syphilis "may be fatal at this point"; the Weil-Felix wartime story's towns and
#     dates; the Komodo dragon slide; marriage-license states; the "?" demographic line of slide 48; map shading.
#   - drug doses (slide 11's penicillin units). Drugs the slides NAME are asked; no dose ever is.
# SPELLING: the slides' "rapid plasma reagent" is the rapid plasma reagin test (its expansion is not tested);
# "Coxiella burnetti" is written Coxiella burnetii; "Ureplasma" Ureaplasma; "angiomatosus" angiomatosis.
SRC = "PAJ5200.Misc inf agents-2.pptx"


def c(*n):
    return f"{SRC}, Slide " + (str(n[0]) if len(n) == 1 else ", ".join(map(str, n[:-1])) + " and " + str(n[-1]))


def ci(img, *n):
    """cite with a picture slide: c(n...) + ' and image on Slide img'"""
    return (c(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO1 = ("1 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, "
       "clinical manifestations, methods of treatment, and prevention of miscellaneous bacterial agents of human "
       "diseases")
IO2 = ("2 — Describe the modes of transmission by which humans acquire miscellaneous bacterial agents of human "
       "diseases")
IMG = "micro-exam-2-quiz-images"


def Q(topic, io, q, key, wrong, cite, **kw):
    """key = (text, explanation); wrong = [(text, explanation, misconception), x3]. Key authored at 0."""
    assert len(wrong) == 3, q
    d = dict(topic=topic, io=io, q=q,
             opts=[[key[0], key[1]]] + [[t, e] for t, e, _ in wrong],
             mis={t: m for t, _, m in wrong}, c=0, cite=cite)
    d.update(kw)
    return d


POOL = [

# ============================================================== SPIROCHETE FEATURES (slides 3-4)
Q("Spirochete features", IO1,
  "How do spirochetes such as Treponema, Leptospira and Borrelia move?",
  ("By endoflagella inside the cell",
   "Correct: spirochetes are motile by means of endoflagella, which are found inside the cell, in the periplasmic "
   "space beneath the outer membrane."),
  [("By one polar flagellum outside",
    "A single polar flagellum belongs to the curviform bacteria such as Vibrio and Campylobacter; spirochetes move by "
    "endoflagella that lie inside the cell.", "adjacent fact from the same lecture (curviform flagella)"),
   ("By pili that pull the cell",
    "Pili are not how spirochetes move; their motility comes from endoflagella, found inside the cell beneath the "
    "outer membrane.", "confused structure"),
   ("They are nonmotile",
    "Spirochetes are motile; it is the rickettsias that are nonmotile rods or coccobacilli. Spirochetes move by "
    "endoflagella inside the cell.", "adjacent fact from the same lecture (rickettsias are nonmotile)")],
  c(3), ),

Q("Spirochete features", IO1,
  "In a spirochete, where do the endoflagella lie?",
  ("In the periplasmic space",
   "Correct: the endoflagella run in the periplasmic space, under the outer membrane and along the cell body, which "
   "is why they are called endoflagella."),
  [("Outside the outer membrane",
    "Flagella outside the cell are what the curviform bacteria have; a spirochete's endoflagella sit in the "
    "periplasmic space beneath the outer membrane.", "reversed location"),
   ("Within a thick capsule",
    "No capsule is shown housing them; the endoflagella lie in the periplasmic space between the outer membrane and "
    "the cell body.", "confused structure"),
   ("Inside the cytoplasm",
    "They do not sit in the cytoplasm; the drawing places the endoflagella in the periplasmic space, under the "
    "outer membrane.", "confused location")],
  ci(4, 3)),

Q("Spirochete features", IO1,
  "Which Gram reaction and shape do the spirochetes share?",
  ("Gram-negative and spiral",
   "Correct: spirochetes are Gram-negative and spiral shaped, and they move by endoflagella inside the cell."),
  [("Gram-positive and spiral",
    "Spirochetes are spiral but Gram-negative, not Gram-positive; the whole group shares a Gram-negative wall and a "
    "spiral shape.", "reversed Gram reaction"),
   ("Gram-negative and comma-shaped",
    "Comma-shaped Gram-negative rods are Vibrio, a curviform bacterium; spirochetes are Gram-negative and spiral.",
    "adjacent fact from the same lecture (Vibrio shape)"),
   ("Gram-negative coccobacilli",
    "Gram-negative coccobacilli describes the rickettsias and chlamydias; spirochetes are Gram-negative and spiral "
    "shaped.", "adjacent fact from the same lecture (rickettsia shape)")],
  c(3)),

Q("Spirochete features", IO1,
  "Which spirochete genus is especially noted for linear double-stranded deoxyribonucleic acid and plasmids?",
  ("Borrelia",
   "Correct: most bacteria have circular chromosomes, but these narrow cells may carry linear double-stranded "
   "deoxyribonucleic acid and plasmids, especially Borrelia."),
  [("Treponema",
    "Treponema is a spirochete with thin, regular coils, but the genus singled out for linear deoxyribonucleic acid "
    "and plasmids is Borrelia.", "competing organism in the same group"),
   ("Leptospira",
    "Leptospira has tight coils with hooked ends; the genus singled out for linear deoxyribonucleic acid and "
    "plasmids is Borrelia.", "competing organism in the same group"),
   ("Vibrio",
    "Vibrio is a comma-shaped curviform rod, not a spirochete; among the spirochetes, Borrelia is noted for linear "
    "deoxyribonucleic acid and plasmids.", "wrong group")],
  c(4)),

Q("Spirochete features", IO1,
  "Which three genera make up the spirochetes?",
  ("Treponema, Leptospira, Borrelia",
   "Correct: Treponema (syphilis and the nonsyphilitic treponematoses), Leptospira (leptospirosis) and Borrelia "
   "(relapsing fever and Lyme disease) are the spirochetes."),
  [("Treponema, Vibrio, Borrelia",
    "Vibrio is a comma-shaped curviform rod with one polar flagellum, not a spirochete; the third genus is "
    "Leptospira.", "wrong group (curviform)"),
   ("Leptospira, Rickettsia, Borrelia",
    "Rickettsia is a tiny obligate intracellular coccobacillus, not a spirochete; the third genus is Treponema.",
    "wrong group (unique morphology)"),
   ("Treponema, Campylobacter, Borrelia",
    "Campylobacter is a curved or spiral rod with one polar flagellum among the curviform bacteria; the third "
    "spirochete genus is Leptospira.", "wrong group (curviform)")],
  c(3)),

# ============================================================== SYPHILIS (slides 5-18)
Q("Syphilis", IO1,
  "Which stage of syphilis begins with a hard chancre at the site of inoculation?",
  ("Primary",
   "Correct: primary syphilis is the appearance of a hard chancre where the organism entered; the chancre often "
   "heals on its own."),
  [("Secondary",
    "Secondary syphilis brings fever, headache, sore throat and a red or brown rash, including the palms and soles, "
    "after the chancre has gone.", "adjacent stage"),
   ("Tertiary",
    "Tertiary syphilis is the late stage of gummas and neurological and cardiovascular disease, years after the "
    "chancre.", "adjacent stage"),
   ("Congenital",
    "Congenital syphilis is the fetal infection acquired across the placenta, shown by snuffles, skin eruptions "
    "and bone deformation, not a chancre.", "competing presentation")],
  c(9)),

Q("Syphilis", IO1,
  "Why may primary syphilis go undiagnosed?",
  ("The chancre often heals on its own",
   "Correct: the hard chancre at the inoculation site often heals spontaneously, so the illness may be missed "
   "while the organism spreads."),
  [("No lesion forms at the entry site",
    "A lesion does form: a hard chancre appears at the site of inoculation; it is missed because it often heals on "
    "its own.", "reversed fact"),
   ("Its rash stays hidden on the soles",
    "The palm and sole rash belongs to secondary syphilis; primary syphilis is a chancre that may heal "
    "spontaneously and be missed.", "adjacent stage"),
   ("Its organisms stay out of the blood",
    "In the first two stages spirochetes are in the lesions and in the blood; primary syphilis is missed because "
    "the chancre heals by itself.", "reversed fact")],
  c(8, 9)),

Q("Syphilis", IO1,
  "Weeks after a genital sore healed, a patient has fever, sore throat and a red-brown rash on the palms "
  "and soles. Which stage of syphilis is this?",
  ("Secondary",
   "Correct: secondary syphilis brings an upper respiratory-like illness (fever, headache, sore throat) and a red "
   "or brown rash on the skin, palms and soles, after the chancre has healed."),
  [("Primary",
    "Primary syphilis is the hard chancre itself; this patient's chancre has already healed and a palm and sole "
    "rash has followed.", "adjacent stage"),
   ("Tertiary",
    "Tertiary syphilis comes years later, with gummas and neurological and cardiovascular disease, not a febrile "
    "palm and sole rash weeks after the chancre.", "adjacent stage"),
   ("Latent",
    "Latency is the quiet period with few if any symptoms between stages; a rash with fever and sore throat is "
    "secondary syphilis.", "wrong phase of the stage table")],
  ci(11, 9)),

Q("Syphilis", IO1,
  "Which lesions develop in tertiary syphilis?",
  ("Gummas",
   "Correct: tertiary syphilis can last 20 years or longer; neurological and cardiovascular symptoms develop and "
   "gummas form in organs."),
  [("Hard chancres",
    "A hard chancre is the lesion of primary syphilis at the site of inoculation, not of the tertiary stage.",
    "adjacent stage"),
   ("Palm and sole rashes",
    "A red or brown rash on the palms and soles is secondary syphilis; the tertiary stage brings gummas.",
    "adjacent stage"),
   ("Hutchinson's teeth",
    "Hutchinson's teeth are a sign of congenital syphilis, acquired across the placenta, not of the tertiary stage.",
    "competing presentation")],
  c(10, 14)),

Q("Syphilis", IO1,
  "Which eye sign of tertiary syphilis eventually ends in loss of the light reflex?",
  ("Argyll Robertson pupil",
   "Correct: the Argyll Robertson pupil of tertiary syphilis is irregular in shape and eventually loses its "
   "light reflex."),
  [("Ocular trachoma",
    "Ocular trachoma is a severe chlamydial infection that deforms the eyelid and cornea; the tertiary syphilis "
    "eye sign is the Argyll Robertson pupil.", "competing organism (Chlamydia trachomatis)"),
   ("Inclusion conjunctivitis",
    "Inclusion conjunctivitis is a chlamydial infection a baby acquires in the birth canal; tertiary syphilis "
    "gives the Argyll Robertson pupil.", "competing organism (Chlamydia trachomatis)"),
   ("Leptospiral conjunctivitis",
    "Conjunctivitis is a sign of leptospirosis with sudden high fever; the tertiary syphilis eye sign is the "
    "Argyll Robertson pupil.", "competing organism (Leptospira)")],
  ci(14, 14)),

Q("Syphilis", IO1,
  "Which pair of signs is classic for congenital syphilis?",
  ("Snuffles and Hutchinson's teeth",
   "Correct: congenital syphilis shows post-natal nasal discharge (\"snuffles\") and Hutchinson's teeth, with skin "
   "eruptions, bone deformation and nervous system abnormalities."),
  [("Gummas and abnormal pupils",
    "Gummas and the Argyll Robertson pupil are tertiary syphilis in an adult infected years before; congenital "
    "syphilis gives snuffles and Hutchinson's teeth.", "adjacent stage"),
   ("Chancre and hair loss",
    "A chancre is primary syphilis and hair loss is listed for secondary syphilis; congenital syphilis gives "
    "snuffles and Hutchinson's teeth.", "adjacent stage"),
   ("Bull's-eye rash and arthritis",
    "A bull's-eye rash and polyarthritis are Lyme disease; congenital syphilis gives snuffles and Hutchinson's "
    "teeth.", "competing organism (Borrelia burgdorferi)")],
  c(10, 15)),

Q("Syphilis", IO2,
  "How does a fetus acquire syphilis?",
  ("Across the placenta",
   "Correct: congenital syphilis is a trans-placental infection of the fetus, causing nasal discharge, skin "
   "eruptions, bone deformation and nervous system abnormalities after birth."),
  [("Through the birth canal",
    "Infection in the birth canal is how newborns get chlamydial inclusion conjunctivitis; syphilis reaches the "
    "fetus across the placenta.", "competing organism (Chlamydia trachomatis)"),
   ("From a tick bite in infancy",
    "Ticks carry Borrelia and the rickettsias of spotted fever; Treponema pallidum reaches the fetus across the "
    "placenta.", "wrong vector"),
   ("From the mother's urine",
    "Urine spreads Leptospira, which is shed by mammals; Treponema pallidum is passed sexually and across the "
    "placenta.", "competing organism (Leptospira)")],
  c(6, 10)),

Q("Syphilis", IO2,
  "By which routes is Treponema pallidum transmitted?",
  ("Sexually and across the placenta",
   "Correct: humans are the natural hosts of Treponema pallidum, which spreads by sexual and trans-placental "
   "transmission and cannot survive long outside the human host."),
  [("By ticks from mouse reservoirs",
    "Ticks feeding on mice spread Borrelia burgdorferi, the cause of Lyme disease; Treponema pallidum passes "
    "sexually and across the placenta.", "competing organism (Borrelia burgdorferi)"),
   ("Through mammal urine in water",
    "Contact with urine-contaminated water spreads Leptospira interrogans; Treponema pallidum passes sexually and "
    "across the placenta.", "competing organism (Leptospira)"),
   ("By inhaling contaminated dust",
    "Inhaled infectious particles spread Coxiella burnetii, the cause of Q fever; Treponema pallidum passes sexually "
    "and across the placenta.", "competing organism (Coxiella)")],
  c(6)),

Q("Syphilis", IO1,
  "In which stages of untreated syphilis is the patient communicable?",
  ("Primary and secondary",
   "Correct: spirochetes appear in the lesions and in the blood during the first two stages, primary and "
   "secondary, and syphilis is communicable at these stages."),
  [("Secondary and tertiary",
    "Tertiary syphilis is a late stage of gummas and organ damage; the communicable stages are the first two, "
    "primary and secondary.", "adjacent stage"),
   ("Primary and tertiary",
    "Primary is one of the communicable stages, but the other is secondary, when spirochetes are in the lesions and "
    "blood, not tertiary.", "adjacent stage"),
   ("Latent and tertiary",
    "Latency and the tertiary stage come after the two communicable stages; spirochetes are in lesions and blood "
    "in primary and secondary syphilis.", "reversed sequence")],
  c(8)),

Q("Syphilis", IO1,
  "Why is Treponema pallidum hard to culture in the laboratory?",
  ("It needs live host cells",
   "Correct: Treponema species are strict parasites with complex growth requirements; they need live host cells to "
   "be cultivated in the lab."),
  [("It needs host-membrane lipids",
    "Needing special lipids from host membranes is the Mycoplasma requirement; Treponema needs live host cells to "
    "be cultivated.", "adjacent fact from the same lecture (Mycoplasma)"),
   ("It forms a resistant endospore",
    "An unusually resistant endospore is made by Coxiella burnetii; Treponema is hard to grow because it needs live "
    "host cells.", "adjacent fact from the same lecture (Coxiella)"),
   ("It needs a salt-rich marine medium",
    "Salt tolerance belongs to the seafood vibrios of coastal waters; Treponema needs live host cells to be "
    "cultivated.", "adjacent fact from the same lecture (seafood vibrios)")],
  c(5)),

Q("Syphilis", IO1,
  "Where does Treponema pallidum survive poorly?",
  ("Outside the human host",
   "Correct: Treponema pallidum is extremely fastidious and sensitive to environmental conditions, and it cannot "
   "survive long outside the human host, its natural host."),
  [("In the bloodstream",
    "It does survive in blood: spirochetes are in the blood during the first two stages. What it cannot do is "
    "survive long outside the human host.", "reversed fact"),
   ("On mucous membranes",
    "Mucous membranes are where it binds and multiplies before penetrating capillaries; it survives poorly outside "
    "the human host.", "reversed fact"),
   ("Inside human tissues",
    "Human tissues are its home (humans are its natural hosts, and gummas form in organs); it fails outside the "
    "human host.", "reversed fact")],
  c(6, 8)),

Q("Syphilis", IO1,
  "After Treponema pallidum binds to a mucous membrane or abraded skin, what does it do next?",
  ("Multiplies, then enters capillaries",
   "Correct: the spirochete binds to epithelial tissue, multiplies, then penetrates capillaries, moves into the "
   "circulation and multiplies further."),
  [("Invades endothelial cells first",
    "Entering endothelial cells and causing vasculitis is the rickettsia mechanism; Treponema multiplies at the "
    "site and then penetrates capillaries.", "competing organism (Rickettsia)"),
   ("Stays confined to the skin",
    "It does not stay local: after multiplying it penetrates capillaries and spreads in the circulation.",
    "reversed fact"),
   ("Forms spores in the epidermis",
    "Treponema forms no spores (an endospore is the Coxiella feature); it multiplies and then penetrates "
    "capillaries.", "adjacent fact from the same lecture (Coxiella)")],
  c(8)),

Q("Syphilis", IO1,
  "Which drug is named with doxycycline as the treatment for syphilis, not as a less effective fallback?",
  ("Penicillin G",
   "Correct: syphilis is treated with penicillin G or doxycycline; erythromycin and tetracycline are less effective "
   "and used when penicillin is contraindicated, for example by allergy."),
  [("Erythromycin",
    "Erythromycin is the less effective fallback when penicillin is contraindicated; the drug named with doxycycline "
    "is penicillin G.", "right drug at the wrong priority"),
   ("Rifampin",
    "Rifampin is listed among the treatments for Bartonella infections, not syphilis; syphilis is treated with "
    "penicillin G or doxycycline.", "adjacent fact from the same lecture (Bartonella)"),
   ("Amoxicillin",
    "Amoxicillin is named with tetracycline for Lyme disease; syphilis is treated with penicillin G or "
    "doxycycline.", "adjacent fact from the same lecture (Lyme)")],
  c(16, 53, 26)),

Q("Syphilis", IO1,
  "Why might erythromycin or tetracycline be used to treat syphilis?",
  ("Penicillin is contraindicated",
   "Correct: erythromycin and tetracycline are less effective than penicillin G or doxycycline but can be used "
   "when penicillin is contraindicated, for example by patient allergy."),
  [("They work better than penicillin",
    "They are LESS effective than penicillin; they are the fallback when penicillin is contraindicated, as in a "
    "patient with an allergy.", "reversed fact"),
   ("The disease is tertiary",
    "The stage is not what calls for them; erythromycin and tetracycline are used when penicillin is "
    "contraindicated, for example by allergy.", "wrong deciding factor"),
   ("The patient is pregnant",
    "Pregnancy is not the reason given; erythromycin and tetracycline are the fallback when penicillin is "
    "contraindicated, for example by allergy.", "wrong deciding factor")],
  c(16)),

Q("Syphilis", IO1,
  "Which test is the older version of the rapid plasma reagin test for syphilis?",
  ("Venereal Disease Research Laboratory test",
   "Correct: the Venereal Disease Research Laboratory test is the older version of the rapid plasma reagin "
   "test, which tests for syphilis antibodies."),
  [("Fluorescent treponemal antibody test",
    "The fluorescent treponemal antibody-absorption test is a separate serological test; the older version of the "
    "rapid plasma reagin test is the Venereal Disease Research Laboratory test.", "competing test"),
   ("Dark-field microscopy of a lesion",
    "Dark-field microscopy looks at the organism in a lesion and is not a blood antibody test; the older version of "
    "the rapid plasma reagin test is the Venereal Disease Research Laboratory test.", "confused test category"),
   ("Weil-Felix agglutination test",
    "The Weil-Felix test detects rickettsial infection by cross-reaction with Proteus; the older version of the "
    "rapid plasma reagin test is the Venereal Disease Research Laboratory test.",
    "adjacent fact from the same lecture (rickettsias)")],
  c(17)),

Q("Syphilis", IO1,
  "A false-positive rapid plasma reagin result for syphilis can occur in a patient with which condition?",
  ("Lyme disease",
   "Correct: syphilis tests can give false positives with human immunodeficiency virus infection, Lyme disease, "
   "some pneumonias, malaria and lupus."),
  [("Cholera",
    "Cholera is not among the conditions that give a false-positive rapid plasma reagin; those listed are human "
    "immunodeficiency virus, Lyme disease, some pneumonias, malaria and lupus.", "unlisted condition"),
   ("Dental caries",
    "Dental caries is not among the causes of a false-positive rapid plasma reagin; those listed include Lyme "
    "disease, malaria and lupus.", "unlisted condition"),
   ("Trench fever",
    "Trench fever is not among the causes of a false-positive rapid plasma reagin; those listed include Lyme "
    "disease, malaria and lupus.", "unlisted condition")],
  c(16)),

Q("Syphilis", IO1,
  "Why must clinicians weigh symptoms, history, microscopy and serology together when diagnosing syphilis?",
  ("Its stages can mimic other diseases",
   "Correct: the stages of syphilis can mimic other diseases, and serological tests can give false positives, so "
   "symptoms, history, microscopic and serological testing are considered together."),
  [("It cannot be seen by microscopy",
    "It can be seen: dark-field microscopy of a lesion is one of the listed diagnostic tests. The reason is that its "
    "stages mimic other diseases.", "reversed fact"),
   ("No blood test exists for it",
    "Blood tests do exist (the rapid plasma reagin test and the fluorescent treponemal antibody test among them); "
    "evidence is combined because the stages mimic other diseases.", "reversed fact"),
   ("It grows quickly on blood agar",
    "Treponema needs live host cells and is difficult to culture; the evidence is combined because syphilis can "
    "mimic other diseases.", "reversed fact")],
  c(5, 16)),

Q("Syphilis", IO1,
  "Which complications mark tertiary syphilis?",
  ("Neurological and cardiovascular disease",
   "Correct: tertiary syphilis can last 20 years or longer, with neurological and cardiovascular symptoms and "
   "gummas in susceptible tissues and organs."),
  [("Fever, sore throat and a rash",
    "Fever, sore throat and a red or brown rash are secondary syphilis; the tertiary stage is neurological and "
    "cardiovascular disease with gummas.", "adjacent stage"),
   ("Nasal discharge and bone deformity",
    "Nasal discharge and bone deformation are congenital syphilis in the newborn; the tertiary stage is "
    "neurological and cardiovascular disease.", "competing presentation"),
   ("Pneumonitis and liver inflammation",
    "Pneumonitis, fever and inflammation of the liver are Q fever; tertiary syphilis is neurological and "
    "cardiovascular disease with gummas.", "competing organism (Coxiella)")],
  c(10)),

Q("Syphilis", IO1,
  "What was the Tuskegee Study (1932-1972)?",
  ("A study of untreated syphilis",
   "Correct: the Tuskegee Study was a study of untreated syphilis that ran from 1932 to 1972."),
  [("A study of untreated yaws",
    "Yaws is a nonsyphilitic treponematosis of skin lesions; the Tuskegee Study followed untreated syphilis.",
    "competing disease in the same genus"),
   ("A trial of a syphilis vaccine",
    "It was not a vaccine trial; the Tuskegee Study was a study of untreated syphilis from 1932 to 1972.",
    "confused study type"),
   ("A trial of Lyme disease treatment",
    "Lyme disease is a tick-borne Borrelia infection; the Tuskegee Study was a study of untreated syphilis.",
    "competing disease")],
  c(7)),

Q("Syphilis", IO1,
  "Which feature belongs to secondary syphilis?",
  ("Hair loss",
   "Correct: the secondary stage brings skin and mucous membrane lesions, hair loss, fever and lymphadenopathy, "
   "and the patient is highly infectious."),
  [("A hard chancre",
    "The hard chancre at the inoculation site is the primary stage; hair loss is listed for the secondary stage.",
    "adjacent stage"),
   ("Gummas in organs",
    "Gummas develop in organs in tertiary syphilis; hair loss is the secondary-stage feature.", "adjacent stage"),
   ("Snuffles at birth",
    "Snuffles (post-natal nasal discharge) are congenital syphilis; hair loss is the secondary-stage feature.",
    "competing presentation")],
  ci(11, 9)),

# picture items (Set 2 only)
Q("Syphilis", IO1,
  "A patient has this rash on both palms, with fever and a sore throat, a few weeks after a genital sore healed "
  "by itself. Which organism is the cause?",
  ("Treponema pallidum",
   "Correct: a red or brown rash on the palms and soles with an upper respiratory-like illness, after a chancre "
   "that healed on its own, is secondary syphilis, caused by Treponema pallidum."),
  [("Rickettsia rickettsii",
    "Rocky Mountain spotted fever gives a spotted rash after a tick bite, with no preceding sore that healed; this "
    "history is secondary syphilis.", "competing diagnosis (spotted rash)"),
   ("Borrelia burgdorferi",
    "Lyme disease gives a bull's-eye rash at the tick-bite site, not a palm rash after a healed genital sore.",
    "competing diagnosis (rash)"),
   ("Chlamydia trachomatis",
    "Chlamydia trachomatis causes urethritis, cervicitis and lymphogranuloma venereum, not a palm and sole rash "
    "with fever.", "competing sexually transmitted organism")],
  ci(13, 9), img=IMG + "/l13-s13-palm-rash.jpg",
  alt="Both palms covered in scattered red-brown spots.", slide="Slide 13"),

Q("Syphilis", IO1,
  "This lesion appeared on the face of a patient infected with Treponema pallidum many years earlier. What is it?",
  ("A gumma",
   "Correct: gummas develop in tertiary syphilis, the late stage that can last 20 years or longer, along with "
   "neurological and cardiovascular symptoms."),
  [("A hard chancre",
    "A hard chancre is the first lesion, at the inoculation site, in primary syphilis; a lesion years after "
    "infection is a gumma.", "adjacent stage"),
   ("Erythema migrans",
    "Erythema migrans is the expanding bull's-eye rash at a tick bite in Lyme disease, not a raised late "
    "syphilitic lesion.", "competing diagnosis"),
   ("A cat-scratch papule",
    "Cat-scratch disease follows a clawing injury by a cat and is caused by Bartonella; a late lesion of syphilis is "
    "a gumma.", "competing diagnosis")],
  ci(14, 10), img=IMG + "/l13-s14-gumma.jpg",
  alt="A raised, red, granular lesion on the cheek below the eye.", slide="Slide 14"),

Q("Syphilis", IO1,
  "Teeth like these in a child are a sign of which infection?",
  ("Congenital syphilis",
   "Correct: these are Hutchinson's teeth, a sign of congenital syphilis, the trans-placental infection that also "
   "causes snuffles, skin eruptions and bone deformation."),
  [("Dental caries",
    "Caries is acid damage to the enamel from plaque bacteria such as Streptococcus mutans; these teeth are "
    "Hutchinson's teeth of congenital syphilis.", "competing diagnosis (dental)"),
   ("Periodontitis",
    "Periodontitis is infection of the tooth socket behind calculus and gingival pockets; these teeth are a sign of "
    "congenital syphilis.", "competing diagnosis (dental)"),
   ("Yaws",
    "Yaws is a nonsyphilitic treponematosis that enters a skin cut and causes skin lesions; Hutchinson's teeth are "
    "congenital syphilis.", "competing disease in the same genus")],
  ci(15, 10), img=IMG + "/l13-s15-hutchinson-teeth.jpg",
  alt="A child's front teeth, the upper central incisors notched and narrowed with a gap between them.",
  slide="Slide 15"),

# ============================================================== NONSYPHILITIC TREPONEMATOSES (slides 19-20)
Q("Nonsyphilitic treponematoses", IO1,
  "Which nonsyphilitic treponematosis is a superficial skin lesion that depigments and scars the skin?",
  ("Pinta",
   "Correct: pinta, caused by Treponema carateum, is a superficial skin lesion that depigments and scars the skin."),
  [("Yaws",
    "Yaws enters a skin cut, causing a primary ulcer that seeds a second crop of lesions; the depigmenting, "
    "scarring lesion is pinta.", "competing disease in the same group"),
   ("Bejel",
    "Bejel is a deforming childhood infection of the mouth, nasal cavity, body and hands; the depigmenting, "
    "scarring lesion is pinta.", "competing disease in the same group"),
   ("Relapsing fever",
    "Relapsing fever is a tick-borne Borrelia infection with febrile cycles, not a skin lesion; the depigmenting "
    "lesion is pinta.", "wrong genus")],
  c(19)),

Q("Nonsyphilitic treponematoses", IO1,
  "Which treponematosis starts as a primary ulcer in a skin cut that seeds a second crop of lesions?",
  ("Yaws",
   "Correct: yaws, caused by Treponema pallidum subspecies pertenue, invades a skin cut and causes a primary ulcer "
   "that seeds a second crop of lesions."),
  [("Pinta",
    "Pinta is a superficial skin lesion that depigments and scars the skin, not an ulcer that seeds a second crop.",
    "competing disease in the same group"),
   ("Bejel",
    "Bejel is a deforming childhood infection of the mouth, nasal cavity, body and hands, not a skin-cut ulcer.",
    "competing disease in the same group"),
   ("Primary syphilis",
    "Primary syphilis is a hard chancre at the site of sexual inoculation; the skin-cut ulcer that seeds a second "
    "crop is yaws.", "competing disease in the same genus")],
  c(19)),

Q("Nonsyphilitic treponematoses", IO1,
  "Which organism causes bejel?",
  ("Treponema pallidum endemicum",
   "Correct: bejel is caused by Treponema pallidum subspecies endemicum, a deforming childhood infection of the "
   "mouth, nasal cavity, body and hands."),
  [("Treponema pallidum pertenue",
    "Treponema pallidum subspecies pertenue causes yaws, the skin-cut ulcer that seeds a second crop of lesions.",
    "competing subspecies"),
   ("Treponema carateum",
    "Treponema carateum causes pinta, the superficial skin lesion that depigments and scars the skin.",
    "competing species"),
   ("Leptospira interrogans",
    "Leptospira interrogans causes leptospirosis, spread by mammal urine; bejel is caused by Treponema pallidum "
    "subspecies endemicum.", "wrong genus")],
  c(19)),

Q("Nonsyphilitic treponematoses", IO2,
  "How does the transmission of the nonsyphilitic treponematoses differ from that of syphilis?",
  ("Mostly by nonsexual routes",
   "Correct: the nonsyphilitic (non-venereal) treponematoses resemble syphilis but are rarely transmitted "
   "sexually or congenitally; they are cutaneous and bone diseases endemic to particular regions."),
  [("Mostly by tick bites",
    "Ticks carry Borrelia and the spotted-fever rickettsias; the nonsyphilitic treponematoses are non-venereal, "
    "rarely transmitted sexually or congenitally.", "wrong vector"),
   ("Mostly through animal urine",
    "Spread through animal urine belongs to Leptospira; the nonsyphilitic treponematoses differ from syphilis by "
    "being rarely transmitted sexually or congenitally.", "competing organism (Leptospira)"),
   ("Mostly by inhalation",
    "Inhalation is how Q fever is usually acquired; the nonsyphilitic treponematoses are rarely transmitted sexually "
    "or congenitally.", "competing organism (Coxiella)")],
  c(19, 22, 52)),

Q("Nonsyphilitic treponematoses", IO1,
  "Where are the nonsyphilitic treponematoses endemic?",
  ("Arid regions and the Global South",
   "Correct: they are cutaneous and bone diseases endemic to specific regions, usually arid climates and/or Global "
   "South countries; yaws, for example, is found in South America, Africa, Asia and Oceania."),
  [("Coastal shellfish waters",
    "Coastal waters harbor the salt-tolerant seafood vibrios; the treponematoses are endemic to arid regions and "
    "Global South countries.", "competing organism (seafood vibrios)"),
   ("The northeastern United States",
    "A tick-borne disease such as Lyme disease is not the pattern here; these treponematoses are endemic to arid "
    "climates and Global South countries.", "competing disease (Lyme)"),
   ("Worldwide, wherever lice are",
    "Lice spread epidemic typhus and trench fever; the nonsyphilitic treponematoses are endemic to arid climates and "
    "the Global South.", "competing vector-borne disease")],
  c(19, 20)),

# ============================================================== LEPTOSPIRA (slides 21-22)
Q("Leptospira", IO1,
  "Which shape identifies Leptospira?",
  ("Tight coils with hooked ends",
   "Correct: Leptospira has tight, regular individual coils with a bend or hook at one or both ends."),
  [("Large, loose, irregular coils",
    "Large cells with 3-10 irregularly spaced coils are Borrelia; Leptospira has tight, regular coils with hooked "
    "ends.", "competing spirochete (Borrelia)"),
   ("Comma-shaped rods",
    "Comma-shaped rods with one polar flagellum are Vibrio; Leptospira has tight coils with a bend or hook at the "
    "ends.", "adjacent fact from the same lecture (Vibrio)"),
   ("Gull-winged curved pairs",
    "Curved rods in S-shaped or gull-winged pairs are Campylobacter; Leptospira has tight coils with hooked ends.",
    "adjacent fact from the same lecture (Campylobacter)")],
  c(21)),

Q("Leptospira", IO2,
  "How is leptospirosis mainly acquired?",
  ("Contact with mammal urine",
   "Correct: leptospirosis is a zoonosis transmitted mainly via mammal urine; the bacteria are shed in urine and "
   "infection primarily occurs by contact with it, so moisture is required."),
  [("Bites of infected ticks",
    "Tick bites transmit Borrelia and the spotted-fever rickettsias; Leptospira interrogans is acquired by contact "
    "with contaminated urine.", "wrong vector"),
   ("Eating raw shellfish",
    "Raw seafood and oysters transmit Vibrio parahaemolyticus and Vibrio vulnificus; leptospirosis comes from "
    "contact with mammal urine.", "competing organism (seafood vibrios)"),
   ("Sexual contact",
    "Sexual contact transmits Treponema pallidum and Chlamydia trachomatis; leptospirosis comes from contact with "
    "mammal urine.", "competing organism")],
  c(21, 22)),

Q("Leptospira", IO2,
  "Which worker is at higher risk of leptospirosis?",
  ("A slaughterhouse worker",
   "Correct: Leptospira is shed in mammalian urine and needs moisture; surfers, water-skiers, veterinarians, farmers "
   "and slaughterhouse workers are among those likely to be infected."),
  [("A cat groomer",
    "Cat handlers face cat-scratch disease from Bartonella; leptospirosis risk follows contact with mammal urine and "
    "moisture, as in slaughterhouse work.", "competing organism (Bartonella)"),
   ("A pet-bird breeder",
    "Birds transmit Chlamydophila psittaci, the cause of ornithosis; leptospirosis risk follows contact with "
    "mammal urine, as in slaughterhouse work.", "competing organism (Chlamydophila psittaci)"),
   ("A dental hygienist",
    "Dental work involves the plaque bacteria of caries and periodontal disease; leptospirosis risk follows "
    "contact with mammal urine.", "competing setting (dental)")],
  c(22)),

Q("Leptospira", IO1,
  "Which Leptospira species is a harmless, free-living saprobe?",
  ("Leptospira biflexa",
   "Correct: Leptospira biflexa is a harmless free-living saprobe, while Leptospira interrogans causes "
   "leptospirosis."),
  [("Leptospira interrogans",
    "Leptospira interrogans is the pathogen, causing leptospirosis, a zoonosis spread mainly by mammal urine.",
    "reversed pair"),
   ("Borrelia hermsii",
    "Borrelia hermsii is the tick-borne cause of relapsing fever, not a harmless Leptospira.",
    "wrong genus"),
   ("Treponema carateum",
    "Treponema carateum causes pinta, a depigmenting skin lesion; the harmless Leptospira is Leptospira biflexa.",
    "wrong genus")],
  c(21)),

Q("Leptospira", IO1,
  "Which organs does Leptospira interrogans target?",
  ("Kidneys, liver, brain and eyes",
   "Correct: leptospirosis targets the kidneys, liver, brain and eyes, and long-term infections may affect the "
   "kidneys and liver."),
  [("Stomach and duodenum",
    "The stomach and duodenum are the targets of Helicobacter pylori, which causes ulcers; Leptospira targets the "
    "kidneys, liver, brain and eyes.", "competing organism (Helicobacter)"),
   ("Lining of small blood vessels",
    "Entering endothelial cells of the vascular lining is the rickettsia pattern; Leptospira targets the kidneys, "
    "liver, brain and eyes.", "competing organism (Rickettsia)"),
   ("Gums and tooth sockets",
    "The gums and tooth sockets are attacked in periodontal disease; Leptospira targets the kidneys, liver, brain "
    "and eyes.", "competing setting (dental)")],
  c(21)),

Q("Leptospira", IO1,
  "Which set of findings fits acute leptospirosis?",
  ("Fever, aches, conjunctivitis",
   "Correct: leptospirosis brings a sudden high fever, chills, headache, muscle aches, conjunctivitis and vomiting; "
   "long-term infection may affect the kidneys and liver."),
  [("Fever, sore throat, palm rash",
    "Fever, sore throat and a palm and sole rash are secondary syphilis; leptospirosis gives sudden fever, muscle "
    "aches and conjunctivitis.", "competing spirochete (Treponema)"),
   ("Rice water stool, dehydration",
    "Rice water stool and dehydration are cholera; leptospirosis gives sudden high fever, muscle aches and "
    "conjunctivitis.", "competing disease (cholera)"),
   ("Fever, chest pain, sore throat",
    "Fever, chest pain and sore throat are Mycoplasma pneumoniae's primary atypical pneumonia; leptospirosis adds "
    "conjunctivitis to fever and aches.", "competing disease (Mycoplasma)")],
  c(21)),

# ============================================================== RELAPSING FEVER / BORRELIA (slides 23-25)
Q("Relapsing fever", IO1,
  "How do Borrelia cells differ from the other spirochetes in their coils?",
  ("Large, with irregular coils",
   "Correct: Borrelia cells are large, with 3-10 irregularly spaced coils, unlike the thin regular coils of "
   "Treponema or the tight hooked coils of Leptospira."),
  [("Thin, with regular coils",
    "Thin, regular, coiled cells describe Treponema; Borrelia is large, with 3-10 irregularly spaced coils.",
    "competing spirochete (Treponema)"),
   ("Tight coils with hooked ends",
    "Tight, regular coils with a hook at one or both ends describe Leptospira; Borrelia is large with irregular "
    "coils.", "competing spirochete (Leptospira)"),
   ("No coils, a comma shape",
    "A comma shape belongs to Vibrio, a curviform bacterium; Borrelia is a spirochete with large, irregular "
    "coils.", "wrong group")],
  c(5, 21, 23)),

Q("Relapsing fever", IO2,
  "How are the borrelioses transmitted to humans?",
  ("By arthropods such as ticks",
   "Correct: borrelioses are transmitted by arthropod vectors such as ticks: Borrelia hermsii causes relapsing "
   "fever and Borrelia burgdorferi Lyme disease."),
  [("By contaminated drinking water",
    "Contaminated water carries Vibrio cholerae and Campylobacter; Borrelia reaches humans through arthropod "
    "vectors such as ticks.", "competing organism (enteric)"),
   ("Through mammal urine",
    "Mammal urine spreads Leptospira; Borrelia is carried by arthropod vectors such as ticks.",
    "competing spirochete (Leptospira)"),
   ("By sexual contact",
    "Sexual contact spreads Treponema pallidum; the borrelioses are transmitted by arthropod vectors such as "
    "ticks.", "competing spirochete (Treponema)")],
  c(23)),

Q("Relapsing fever", IO1,
  "Which organism causes relapsing fever?",
  ("Borrelia hermsii",
   "Correct: Borrelia hermsii causes relapsing fever, with recurrent febrile and afebrile cycles; Borrelia "
   "burgdorferi causes Lyme disease."),
  [("Borrelia burgdorferi",
    "Borrelia burgdorferi causes Lyme disease, carried by the white-footed mouse and Ixodes ticks; relapsing fever "
    "is Borrelia hermsii.", "competing species"),
   ("Rickettsia typhi",
    "Rickettsia typhi causes endemic (murine) typhus, spread by fleas; relapsing fever is caused by Borrelia "
    "hermsii.", "competing organism"),
   ("Leptospira interrogans",
    "Leptospira interrogans causes leptospirosis, spread in mammal urine; relapsing fever is caused by Borrelia "
    "hermsii.", "competing spirochete")],
  c(23, 24)),

Q("Relapsing fever", IO1,
  "What drives the repeated cycles of fever and no fever in relapsing fever?",
  ("New antigenic forms of Borrelia",
   "Correct: the organism changes in the patient's body while the immune system tries to control it; each new "
   "antigenic form escapes the last antibody response and causes another relapse."),
  [("Repeated new tick bites",
    "The relapses do not need new bites; they come from mutant Borrelia with new antigens that escape each antibody "
    "response.", "plausible but unsupported cause"),
   ("A heat-labile enterotoxin",
    "A heat-labile enterotoxin is how Campylobacter jejuni causes secretory diarrhea; relapses come from new "
    "antigenic forms of Borrelia.", "adjacent fact from the same lecture (Campylobacter)"),
   ("Switching between two cell forms",
    "Alternating elementary and reticulate bodies is the chlamydial life cycle; relapses come from new antigenic "
    "forms of Borrelia.", "adjacent fact from the same lecture (Chlamydia)")],
  ci(25, 24)),

Q("Relapsing fever", IO2,
  "Which animals are the reservoirs of Borrelia hermsii?",
  ("Squirrels and chipmunks",
   "Correct: the mammalian reservoirs of Borrelia hermsii, the cause of relapsing fever, are squirrels, chipmunks "
   "and wild rodents, and it is spread by ticks."),
  [("Domestic cats",
    "Cats are linked to cat-scratch disease from Bartonella; relapsing fever's reservoirs are squirrels, chipmunks "
    "and wild rodents.", "competing organism (Bartonella)"),
   ("Cattle and sheep",
    "Cattle, sheep and goats pass Campylobacter fetus between themselves; relapsing fever's reservoirs are "
    "squirrels, chipmunks and wild rodents.", "competing organism (Campylobacter fetus)"),
   ("Pet birds",
    "Birds transmit Chlamydophila psittaci, the cause of ornithosis; relapsing fever's reservoirs are squirrels, "
    "chipmunks and wild rodents.", "competing organism (Chlamydophila psittaci)")],
  c(24)),

Q("Relapsing fever", IO1,
  "In relapsing fever, what brings each bout of high fever back down?",
  ("An antibody response",
   "Correct: the initial antibody response at first reduces the fever, until a mutant Borrelia with a new antigen "
   "causes a relapse, and each new antibody response again reduces the symptoms."),
  [("Tetracycline taken by mouth",
    "Tetracycline is the usual treatment, but the fall in fever between relapses comes from each new antibody "
    "response to the organism.", "right treatment, wrong mechanism"),
   ("The tick detaching",
    "The tick's departure does not end each bout; the fever falls when an antibody response controls the current "
    "antigenic form.", "plausible but unsupported cause"),
   ("Loss of the endoflagella",
    "Borrelia does not shed its endoflagella between bouts; the fever falls with each antibody response to the "
    "current antigen.", "confused structure")],
  ci(25, 24)),

Q("Relapsing fever", IO1,
  "What is the most common treatment for relapsing fever?",
  ("Tetracycline",
   "Correct: tetracycline is the most common treatment option for relapsing fever, and it recurs as a treatment "
   "throughout these organisms."),
  [("Penicillin G",
    "Penicillin G is named with doxycycline for syphilis; relapsing fever is most commonly treated with "
    "tetracycline.", "adjacent fact from the same lecture (syphilis)"),
   ("Oral rehydration",
    "Oral rehydration replaces the water and electrolytes lost in cholera; relapsing fever is treated with "
    "tetracycline.", "adjacent fact from the same lecture (cholera)"),
   ("Rifampin",
    "Rifampin is one of the options for Bartonella; relapsing fever is most commonly treated with tetracycline.",
    "adjacent fact from the same lecture (Bartonella)")],
  c(24)),

# ============================================================== LYME DISEASE (slides 26-30)
Q("Lyme disease", IO2,
  "Which ticks transmit Lyme disease?",
  ("Ixodes ticks",
   "Correct: Borrelia burgdorferi is carried by the white-footed mouse and transmitted by Ixodes ticks."),
  [("Dog and wood ticks",
    "Dog and wood ticks carry Rickettsia rickettsii, the cause of Rocky Mountain spotted fever; Lyme disease is "
    "transmitted by Ixodes ticks.", "competing tick-borne disease"),
   ("Body lice",
    "Body lice carry Rickettsia prowazekii (epidemic typhus) and trench fever; Lyme disease is transmitted by "
    "Ixodes ticks.", "wrong vector"),
   ("Rat fleas",
    "Fleas spread endemic typhus from rodents; Lyme disease is transmitted by Ixodes ticks.", "wrong vector")],
  c(26)),

Q("Lyme disease", IO2,
  "Which animal carries Borrelia burgdorferi?",
  ("The white-footed mouse",
   "Correct: Borrelia burgdorferi is carried by the white-footed mouse and transmitted by Ixodes ticks in a "
   "two-year cycle involving mice and deer."),
  [("The domestic cat",
    "The cat is linked to cat-scratch disease from Bartonella; Borrelia burgdorferi is carried by the white-footed "
    "mouse.", "competing organism (Bartonella)"),
   ("The pet parrot",
    "Birds transmit Chlamydophila psittaci (ornithosis); Borrelia burgdorferi is carried by the white-footed mouse.",
    "competing organism (Chlamydophila psittaci)"),
   ("The dairy cow",
    "Contaminated milking barns are linked to Q fever from Coxiella; Borrelia burgdorferi is carried by the "
    "white-footed mouse.", "competing organism (Coxiella)")],
  c(26)),

Q("Lyme disease", IO2,
  "In the Lyme disease tick cycle, on which animal do nymphs mature into adult ticks that mate?",
  ("Deer",
   "Correct: in the second year nymphs feed on several hosts, including deer and humans; on deer they mature into "
   "adult male and female ticks, which mate, and the female lays eggs in plant litter."),
  [("White-footed mice",
    "Mice are where newly hatched larvae become infected in the first year; nymphs mature into mating adults on "
    "deer.", "right host, wrong stage"),
   ("Humans",
    "Humans are accidental hosts that nymphs may feed on; the adults mature and mate on deer.",
    "accidental host mistaken for a maintenance host"),
   ("Wild birds",
    "Birds are not part of this cycle (they carry Chlamydophila psittaci); adult ticks mature and mate on deer.",
    "competing organism (Chlamydophila psittaci)")],
  ci(28, 26)),

Q("Lyme disease", IO2,
  "How do newly hatched tick larvae become infected with Borrelia burgdorferi?",
  ("By feeding on infected mice",
   "Correct: newly hatched larvae become infected when they feed on small animals such as mice, which harbor the "
   "spirochete, and continue development through the first year."),
  [("By hatching from infected eggs",
    "The larvae hatch uninfected and pick up the spirochete when they feed on mice; the eggs are laid in plant "
    "litter by adults from deer.", "reversed sequence"),
   ("By feeding on deer",
    "Deer are where nymphs mature into adults in the second year; larvae are infected by feeding on mice.",
    "right host, wrong stage"),
   ("By biting infected humans",
    "Humans are accidental hosts, not the source of the larvae's infection; larvae are infected by feeding on mice.",
    "accidental host mistaken for a reservoir")],
  ci(28, 26)),

Q("Lyme disease", IO2,
  "What role do humans play in the Lyme disease cycle?",
  ("Accidental hosts",
   "Correct: humans are accidental hosts: the nymph takes blood from a number of hosts, including deer and humans, "
   "but the cycle is kept going by mice and deer."),
  [("The main reservoir",
    "The reservoir is the white-footed mouse, which harbors the spirochete; humans are accidental hosts.",
    "reversed role"),
   ("Hosts where adults mate",
    "Adult ticks mature and mate on deer; humans are only accidental hosts of the nymphs.", "right cycle, wrong host"),
   ("Hosts where larvae hatch",
    "Larvae hatch from eggs laid in plant litter; humans are accidental hosts.", "right cycle, wrong host")],
  ci(28, 26)),

Q("Lyme disease", IO1,
  "What is the bull's-eye rash at the site of the tick bite in Lyme disease called?",
  ("Erythema migrans",
   "Correct: erythema migrans is the bull's-eye rash at the initial tick-bite location in Lyme disease."),
  [("A gumma",
    "A gumma is a lesion of tertiary syphilis that forms in organs years after infection, not a rash at a tick "
    "bite.", "competing diagnosis"),
   ("A hard chancre",
    "A hard chancre is the lesion of primary syphilis at the site of inoculation, not the Lyme tick-bite rash.",
    "competing diagnosis"),
   ("Bacillary angiomatosis",
    "Bacillary angiomatosis is a Bartonella infection in patients with acquired immunodeficiency syndrome, not the "
    "Lyme tick-bite rash.", "competing diagnosis")],
  c(26, 30)),

Q("Lyme disease", IO1,
  "Because it mimics neuromuscular and rheumatoid conditions, Lyme disease can be mistaken for what?",
  ("An autoimmune disorder",
   "Correct: Lyme disease is a nonfatal, slowly progressive syndrome that mimics neuromuscular and rheumatoid "
   "conditions and could be mistaken for an autoimmune disorder."),
  [("A secretory diarrhea",
    "Secretory diarrhea is the effect of cholera toxin or the Campylobacter enterotoxin, not what Lyme disease "
    "mimics.", "competing disease (enteric)"),
   ("An atypical pneumonia",
    "Atypical pneumonia is caused by Mycoplasma pneumoniae or Chlamydophila pneumoniae; Lyme disease mimics "
    "autoimmune disorders.", "competing disease"),
   ("A peptic ulcer",
    "Peptic ulcers are caused by Helicobacter pylori; Lyme disease mimics neuromuscular, rheumatoid and autoimmune "
    "conditions.", "competing disease")],
  c(26)),

Q("Lyme disease", IO1,
  "Untreated Lyme disease can progress to which problems?",
  ("Heart, nerve and joint disease",
   "Correct: if untreated, Lyme disease can progress to cardiac and neurological symptoms and polyarthritis."),
  [("Gummas and pupil changes",
    "Gummas and the Argyll Robertson pupil are tertiary syphilis; untreated Lyme disease brings cardiac, "
    "neurological and joint disease.", "competing spirochete (Treponema)"),
   ("Rice water stool",
    "Rice water stool and dehydration are cholera; untreated Lyme disease brings cardiac and neurological symptoms "
    "and polyarthritis.", "competing disease (cholera)"),
   ("Ulcers and gastric cancer",
    "Ulcers and gastric cancer are linked to Helicobacter pylori; untreated Lyme disease brings cardiac, "
    "neurological and joint disease.", "competing disease (Helicobacter)")],
  c(26)),

Q("Lyme disease", IO1,
  "Which drugs are most commonly used for Lyme disease?",
  ("Tetracycline or amoxicillin",
   "Correct: tetracycline or amoxicillin is most commonly used for Lyme disease."),
  [("Rifampin or erythromycin",
    "Rifampin and erythromycin are named for Bartonella infections; Lyme disease is most commonly treated with "
    "tetracycline or amoxicillin.", "adjacent fact from the same lecture (Bartonella)"),
   ("Oral rehydration alone",
    "Oral rehydration replaces cholera's water and electrolyte losses; Lyme disease needs an antibiotic, "
    "tetracycline or amoxicillin.", "adjacent fact from the same lecture (cholera)"),
   ("Tick removal, no antibiotic",
    "Checking for and removing ticks is prevention; once Lyme disease is established it is treated with "
    "tetracycline or amoxicillin.", "prevention confused with treatment")],
  c(26)),

Q("Lyme disease", IO1,
  "What is the best prevention of Lyme disease?",
  ("Repellent and tick checks",
   "Correct: insect repellent containing DEET (N,N-diethyl-meta-toluamide) is the best prevention, along with "
   "checking for ticks; the human vaccine was discontinued."),
  [("The human Lyme vaccine",
    "The human vaccine was withdrawn from the market; a vaccine exists only for dogs. Prevention is repellent and "
    "tick checks.", "outdated belief"),
   ("Avoiding raw shellfish",
    "Raw seafood is the risk for the seafood vibrios; Lyme disease is prevented with insect repellent and tick "
    "checks.", "competing disease (seafood vibrios)"),
   ("Boiling drinking water",
    "Water treatment prevents waterborne disease such as cholera; Lyme disease is tick-borne, so repellent and tick "
    "checks prevent it.", "competing disease (cholera)")],
  c(26)),

Q("Lyme disease", IO1,
  "Which statement about Lyme disease vaccines is accurate?",
  ("Dogs have one; the human one was withdrawn",
   "Correct: a vaccine for dogs is available, but the human vaccine (approved in 1998) was withdrawn from the United "
   "States market in 2002."),
  [("Humans receive one as routine care",
    "No human vaccine is in use: the one approved in 1998 was withdrawn in 2002; a vaccine is available for dogs.",
    "outdated belief"),
   ("None has ever been licensed",
    "Vaccines have been licensed: one is available for dogs, and a human vaccine was approved in 1998 before being "
    "withdrawn.", "reversed fact"),
   ("Deer are vaccinated to break the cycle",
    "Deer are not vaccinated; a vaccine is available for dogs, and the human vaccine was withdrawn.",
    "plausible but unsupported claim")],
  c(26, 27)),

Q("Lyme disease", IO1,
  "This rash appeared around the site of a tick bite after a hike. Which organism causes it?",
  ("Borrelia burgdorferi",
   "Correct: the bull's-eye rash at the tick-bite site, erythema migrans, is the sign of Lyme disease, caused by "
   "Borrelia burgdorferi."),
  [("Rickettsia rickettsii",
    "Rocky Mountain spotted fever is also tick-borne, but it gives a distinct spotted rash, not one expanding patch "
    "at the bite site.", "competing tick-borne disease"),
   ("Borrelia hermsii",
    "Borrelia hermsii is tick-borne too, but relapsing fever is a pattern of febrile cycles, not an expanding "
    "bite-site rash.", "competing species"),
   ("Treponema pallidum",
    "Treponema pallidum is spread sexually, not by tick bite; its rashes are on the palms and soles in secondary "
    "syphilis.", "competing spirochete")],
  ci(30, 26), img=IMG + "/l13-s30-erythema-migrans.jpg",
  alt="A large, round, evenly red patch on the skin of the upper arm.", slide="Slide 30"),

# ============================================================== VIBRIO CHOLERAE and the curviform group (slides 31-33)
Q("Vibrio cholerae", IO1,
  "Which curviform genus is comma-shaped with a single polar flagellum?",
  ("Vibrio",
   "Correct: Vibrio is a comma-shaped rod with a single polar flagellum."),
  [("Campylobacter",
    "Campylobacter also has one flagellum, but its cells are short spirals or curved rods, often S-shaped or "
    "gull-winged pairs, not commas.", "competing curviform genus"),
   ("Helicobacter",
    "Helicobacter has several polar flagella, not a single one; the comma-shaped rod with one polar flagellum is "
    "Vibrio.", "competing curviform genus"),
   ("Leptospira",
    "Leptospira is a spirochete with tight coils and hooked ends, moving by endoflagella; the comma-shaped rod is "
    "Vibrio.", "wrong group")],
  c(31, 32)),

Q("Vibrio cholerae", IO1,
  "How does Vibrio cholerae infect the small intestine?",
  ("Without invading its lining",
   "Correct: Vibrio cholerae infects the mucous barrier of the small intestine and is noninvasive; its toxin causes "
   "the secretory diarrhea."),
  [("By invading the intestinal wall",
    "Vibrio cholerae does not invade; it sits on the mucous barrier of the small intestine and acts through cholera "
    "toxin.", "reversed fact"),
   ("By raising its pH with urease",
    "Raising the local pH with urease is how Helicobacter pylori survives in the stomach; Vibrio cholerae infects "
    "the small intestine noninvasively.", "competing organism (Helicobacter)"),
   ("By entering endothelial cells",
    "Entering endothelial cells is the rickettsia mechanism; Vibrio cholerae infects the small intestine's mucous "
    "barrier without invading.", "competing organism (Rickettsia)")],
  c(32)),

Q("Vibrio cholerae", IO1,
  "What does cholera toxin cause?",
  ("Secretory, rice water diarrhea",
   "Correct: cholera toxin causes electrolyte and water loss through secretory diarrhea, \"rice water stool\", and "
   "the dehydration leads to muscle, circulatory and neurological symptoms."),
  [("Bloody diarrhea from invasion",
    "Vibrio cholerae is noninvasive; its toxin drives water and electrolytes out as secretory rice water diarrhea.",
    "reversed mechanism"),
   ("Ulcers of the stomach lining",
    "Stomach and duodenal ulcers are Helicobacter pylori; cholera toxin causes secretory rice water diarrhea.",
    "competing organism (Helicobacter)"),
   ("Necrosis of vessel linings",
    "Necrosis of the vascular lining is the rickettsial vasculitis; cholera toxin causes secretory rice water "
    "diarrhea.", "competing organism (Rickettsia)")],
  c(32)),

Q("Vibrio cholerae", IO1,
  "In cholera, which way do water and electrolytes move across the intestinal cell?",
  ("Out of the cell into the lumen",
   "Correct: normally water and electrolytes are absorbed from the lumen into the blood; cholera toxin reverses "
   "this, so water and electrolytes (chloride and potassium among them) are lost into the lumen."),
  [("From the lumen into the blood",
    "Lumen-to-blood movement is normal intestinal absorption; cholera toxin causes loss of water and electrolytes "
    "into the lumen.", "reversed direction"),
   ("Into the cell, which then swells",
    "The water does not stay in the cell; under cholera toxin water and electrolytes leave into the intestinal "
    "lumen.", "confused mechanism"),
   ("Out of the gut into the lymph",
    "Cholera's losses are not into the lymph; water and electrolytes are lost into the intestinal lumen, producing "
    "secretory diarrhea.", "confused mechanism")],
  ci(33, 32)),

Q("Vibrio cholerae", IO1,
  "Why can Vibrio cholerae need a very large infectious dose?",
  ("It must first pass the stomach",
   "Correct: the infectious dose can run very high because the vibrios must first pass through the stomach to "
   "infect the intestines."),
  [("It must first enter the blood",
    "Vibrio cholerae never needs the blood; it is noninvasive and acts in the small intestine once it has passed "
    "the stomach.", "confused mechanism"),
   ("It must first multiply in urine",
    "Shedding in urine is how Leptospira spreads; the cholera dose is high because the vibrios must pass through "
    "the stomach.", "competing organism (Leptospira)"),
   ("It must first form a spore",
    "Vibrio cholerae forms no spore (an endospore is the Coxiella feature); the dose is high because the vibrios "
    "must pass the stomach.", "adjacent fact from the same lecture (Coxiella)")],
  c(32)),

Q("Vibrio cholerae", IO1,
  "What sets the El Tor biotype of Vibrio cholerae apart from other strains?",
  ("It survives longer and spreads more",
   "Correct: the El Tor biotype survives longer and is more infectious than other strains."),
  [("It invades the intestinal wall",
    "No Vibrio cholerae strain is described as invasive; El Tor stands out because it survives longer and is more "
    "infectious.", "reversed fact"),
   ("It is milder and rarely infectious",
    "El Tor is the opposite: it survives longer and is more infectious than other strains.", "reversed fact"),
   ("It lacks the O and H antigens",
    "Vibrio cholerae possesses unique O and H antigens; El Tor is set apart by surviving longer and being more "
    "infectious.", "reversed fact")],
  c(32)),

Q("Vibrio cholerae", IO1,
  "Which part of cholera treatment replaces what the toxin removes?",
  ("Oral rehydration",
   "Correct: cholera toxin drains water and electrolytes, and oral rehydration replaces them; tetracycline is "
   "also used, and a vaccine is available."),
  [("Tetracycline",
    "Tetracycline is part of cholera treatment, but it acts on the bacterium; the water and electrolyte losses are "
    "replaced by oral rehydration.", "right treatment, wrong role"),
   ("The cholera vaccine",
    "The vaccine is for prevention; the water and electrolytes the toxin removes are replaced by oral rehydration.",
    "prevention confused with treatment"),
   ("Penicillin G",
    "Penicillin G is named for syphilis, not cholera; cholera's water and electrolyte losses are replaced by oral "
    "rehydration.", "adjacent fact from the same lecture (syphilis)")],
  c(32)),

# ============================================================== SEAFOOD VIBRIOS (slides 34-35)
Q("Seafood vibrios", IO1,
  "Which vibrio causes gastroenteritis from raw oysters, with serious complications in people with diabetes or "
  "liver disease?",
  ("Vibrio vulnificus",
   "Correct: Vibrio vulnificus causes gastroenteritis from raw oysters, with serious complications in persons "
   "with diabetes or liver disease; it is one of the \"flesh-eating\" bacteria."),
  [("Vibrio parahaemolyticus",
    "Vibrio parahaemolyticus causes gastroenteritis from raw seafood with symptoms similar to cholera; the oyster "
    "vibrio dangerous in diabetes or liver disease is Vibrio vulnificus.", "competing species"),
   ("Vibrio cholerae",
    "Vibrio cholerae causes cholera from contaminated water; the oyster-borne vibrio dangerous in diabetes or liver "
    "disease is Vibrio vulnificus.", "competing species"),
   ("Campylobacter jejuni",
    "Campylobacter jejuni comes from water, milk, meat and chicken; the oyster-borne vibrio is Vibrio vulnificus.",
    "competing curviform organism")],
  c(34)),

Q("Seafood vibrios", IO1,
  "Which vibrio causes gastroenteritis from raw seafood with symptoms similar to cholera?",
  ("Vibrio parahaemolyticus",
   "Correct: Vibrio parahaemolyticus causes gastroenteritis from raw seafood, with symptoms similar to cholera."),
  [("Vibrio vulnificus",
    "Vibrio vulnificus is the raw-oyster vibrio that is dangerous in diabetes or liver disease; the cholera-like "
    "seafood gastroenteritis is Vibrio parahaemolyticus.", "competing species"),
   ("Vibrio cholerae El Tor",
    "El Tor is a longer-surviving biotype of Vibrio cholerae itself; the cholera-like seafood vibrio is Vibrio "
    "parahaemolyticus.", "competing strain"),
   ("Campylobacter fetus",
    "Campylobacter fetus is an opportunist of debilitated persons and late pregnancy; the seafood vibrio is Vibrio "
    "parahaemolyticus.", "competing curviform organism")],
  c(34)),

Q("Seafood vibrios", IO1,
  "What is the best treatment option for seafood vibrio gastroenteritis?",
  ("Fluid and electrolyte replacement",
   "Correct: for the seafood vibrios, fluid and electrolyte replacement is the best option; antimicrobial drugs "
   "are used only occasionally."),
  [("Penicillin G or doxycycline",
    "Penicillin G or doxycycline is the syphilis treatment; seafood vibrio gastroenteritis is best treated with "
    "fluid and electrolyte replacement.", "adjacent fact from the same lecture (syphilis)"),
   ("Tetracycline or amoxicillin",
    "Tetracycline or amoxicillin is the Lyme disease treatment; seafood vibrios are best treated with fluid and "
    "electrolyte replacement.", "adjacent fact from the same lecture (Lyme)"),
   ("Rifampin or erythromycin",
    "Rifampin and erythromycin are Bartonella options; the best option for seafood vibrios is fluid and "
    "electrolyte replacement.", "adjacent fact from the same lecture (Bartonella)")],
  c(34)),

Q("Seafood vibrios", IO1,
  "Which property lets the seafood vibrios live in coastal waters?",
  ("Salt tolerance",
   "Correct: the seafood vibrios are salt-tolerant inhabitants of coastal waters that associate with marine "
   "invertebrates."),
  [("Endospore formation",
    "An unusually resistant endospore is made by Coxiella burnetii, not the vibrios; they live in coastal waters "
    "because they tolerate salt.", "adjacent fact from the same lecture (Coxiella)"),
   ("Lack of a cell wall",
    "Lacking a cell wall is the Mycoplasma feature; the seafood vibrios live in coastal waters because they are "
    "salt-tolerant.", "adjacent fact from the same lecture (Mycoplasma)"),
   ("Urease production",
    "Urease lets Helicobacter pylori raise its local pH in the stomach; the seafood vibrios are salt-tolerant.",
    "adjacent fact from the same lecture (Helicobacter)")],
  c(34)),

# ============================================================== CAMPYLOBACTER (slides 36-38)
Q("Campylobacter", IO1,
  "Which description fits Campylobacter?",
  ("Curved rods in gull-winged pairs",
   "Correct: campylobacters are Gram-negative slender, curved or spiral rods, often S-shaped or gull-winged pairs, "
   "with a single polar flagellum."),
  [("Comma-shaped single rods",
    "Comma-shaped rods are Vibrio; Campylobacter is curved or spiral, often in S-shaped or gull-winged pairs.",
    "competing curviform genus"),
   ("Tight coils with hooked ends",
    "Tight coils with hooked ends are Leptospira, a spirochete; Campylobacter forms curved rods in gull-winged "
    "pairs.", "wrong group"),
   ("Wall-less, highly variable cells",
    "Lacking a wall and highly pleomorphic describes Mycoplasma; Campylobacter is a curved rod in gull-winged "
    "pairs.", "wrong group")],
  c(36, 21, 62)),

Q("Campylobacter", IO2,
  "How is Campylobacter jejuni enteritis transmitted?",
  ("Contaminated food and drink",
   "Correct: Campylobacter jejuni is transmitted by beverages and food; water, milk, meat and chicken are common "
   "sources."),
  [("The bite of an infected tick",
    "Ticks spread Borrelia and the spotted-fever rickettsias; Campylobacter jejuni comes from food and drinks such "
    "as chicken and milk.", "wrong vector"),
   ("The scratch of a pet cat",
    "A cat's scratch transmits Bartonella; Campylobacter jejuni comes from food and drinks such as water, milk, meat "
    "and chicken.", "competing organism (Bartonella)"),
   ("Inhaled dust from barns",
    "Inhaled particles spread Coxiella burnetii (Q fever); Campylobacter jejuni comes from food and drinks.",
    "competing organism (Coxiella)")],
  c(37)),

Q("Campylobacter", IO1,
  "Where in the gut does Campylobacter jejuni reach the mucosa?",
  ("The last part of the small intestine",
   "Correct: Campylobacter jejuni reaches the mucosa at the last segment of the small intestine near the colon, "
   "adheres to and burrows through the mucus, then multiplies."),
  [("The lining of the stomach",
    "The stomach lining is the home of Helicobacter pylori; Campylobacter jejuni reaches the mucosa at the last "
    "segment of the small intestine.", "competing organism (Helicobacter)"),
   ("The mouth and the gums",
    "The mouth and gums host the plaque bacteria of dental disease; Campylobacter jejuni targets the last segment "
    "of the small intestine.", "competing setting (dental)"),
   ("The lining of the blood vessels",
    "The vessel lining is where rickettsias cause vasculitis; Campylobacter jejuni targets the last segment of the "
    "small intestine.", "competing organism (Rickettsia)")],
  c(37)),

Q("Campylobacter", IO1,
  "How does Campylobacter jejuni produce a secretory diarrhea like that of cholera?",
  ("A heat-labile enterotoxin",
   "Correct: a heat-labile enterotoxin stimulates a secretory diarrhea like that of cholera, with headache, fever, "
   "abdominal pain and bloody or watery diarrhea."),
  [("Urease that raises the pH",
    "Urease raising the local pH is how Helicobacter pylori survives in the stomach; Campylobacter jejuni acts "
    "through a heat-labile enterotoxin.", "competing organism (Helicobacter)"),
   ("Invasion of the endothelium",
    "Invading endothelial cells is the rickettsial mechanism; Campylobacter jejuni causes secretory diarrhea with a "
    "heat-labile enterotoxin.", "competing organism (Rickettsia)"),
   ("Acid that dissolves the lining",
    "Acid dissolving a surface is how plaque bacteria damage tooth enamel; Campylobacter jejuni acts through a "
    "heat-labile enterotoxin.", "competing mechanism (dental)")],
  c(37)),

Q("Campylobacter", IO1,
  "What is the usual treatment for Campylobacter jejuni enteritis?",
  ("Rehydration and electrolytes",
   "Correct: Campylobacter jejuni enteritis is treated with rehydration and electrolyte balance therapy, rarely "
   "with antibiotics."),
  [("Penicillin G",
    "Penicillin G is a syphilis treatment; Campylobacter jejuni enteritis is treated with rehydration and "
    "electrolyte balance, rarely antibiotics.", "adjacent fact from the same lecture (syphilis)"),
   ("Tetracycline or amoxicillin",
    "Tetracycline or amoxicillin is the Lyme disease treatment; Campylobacter jejuni is treated with rehydration "
    "and electrolytes.", "adjacent fact from the same lecture (Lyme)"),
   ("Rifampin or erythromycin",
    "Rifampin and erythromycin are Bartonella options; Campylobacter jejuni enteritis is treated with rehydration "
    "and electrolytes.", "adjacent fact from the same lecture (Bartonella)")],
  c(37)),

Q("Campylobacter", IO1,
  "Who is most at risk of infection with Campylobacter fetus?",
  ("Women late in pregnancy",
   "Correct: Campylobacter fetus is an opportunistic pathogen that infects debilitated persons or women late in "
   "pregnancy, with meningitis, pneumonia, arthritis and newborn septicemia."),
  [("Surfers and water-skiers",
    "Surfers and water-skiers are at risk of leptospirosis from urine-contaminated water; Campylobacter fetus "
    "strikes debilitated persons and late pregnancy.", "competing organism (Leptospira)"),
   ("People with liver disease",
    "Diabetes or liver disease makes Vibrio vulnificus serious; Campylobacter fetus strikes debilitated persons "
    "and women late in pregnancy.", "competing organism (Vibrio vulnificus)"),
   ("People with asthma",
    "Asthma makes Chlamydophila pneumoniae's atypical pneumonia serious; Campylobacter fetus strikes debilitated "
    "persons and late pregnancy.", "competing organism (Chlamydophila pneumoniae)")],
  c(38)),

Q("Campylobacter", IO2,
  "In veterinary medicine, how is Campylobacter fetus spread among domestic herd animals?",
  ("As a sexually transmitted disease",
   "Correct: Campylobacter fetus is a significant veterinary pathogen as a sexually transmitted disease of domestic "
   "herd animals, passed animal to animal in cattle, sheep and goats; how humans acquire it remains uncertain."),
  [("By tick bites in pastures",
    "Ticks carry Borrelia and the spotted-fever rickettsias; Campylobacter fetus passes between herd animals as a "
    "sexually transmitted disease.", "wrong vector"),
   ("By fleas from rodents",
    "Fleas from rodents spread endemic typhus; Campylobacter fetus passes between cattle, sheep and goats as a "
    "sexually transmitted disease.", "wrong vector"),
   ("By airborne barn particles",
    "Airborne particles from barns spread Q fever (Coxiella); Campylobacter fetus passes between herd animals "
    "sexually.", "competing organism (Coxiella)")],
  c(38)),

Q("Campylobacter", IO1,
  "Which infections can Campylobacter fetus cause in a newborn?",
  ("Meningitis and septicemia",
   "Correct: Campylobacter fetus can cause meningitis, pneumonia, arthritis and septicemia in the newborn."),
  [("Inclusion conjunctivitis",
    "Inclusion conjunctivitis is the chlamydial eye infection acquired in the birth canal; Campylobacter fetus "
    "causes newborn meningitis and septicemia.", "competing organism (Chlamydia trachomatis)"),
   ("Snuffles and bone deformity",
    "Snuffles and bone deformation are congenital syphilis; Campylobacter fetus causes newborn meningitis and "
    "septicemia.", "competing organism (Treponema pallidum)"),
   ("Hutchinson's teeth",
    "Hutchinson's teeth are a sign of congenital syphilis; Campylobacter fetus causes newborn meningitis and "
    "septicemia.", "competing organism (Treponema pallidum)")],
  c(38)),

# ============================================================== HELICOBACTER (slides 31, 39-41)
Q("Helicobacter", IO1,
  "How does Helicobacter differ from Vibrio and Campylobacter in its flagella?",
  ("It has several polar flagella",
   "Correct: Vibrio and Campylobacter each have a single polar flagellum; Helicobacter has several polar flagella."),
  [("It has a single polar flagellum",
    "A single polar flagellum is what Vibrio and Campylobacter have; Helicobacter has several polar flagella.",
    "reversed pair"),
   ("It has no flagella",
    "Helicobacter is motile, with several polar flagella; it is the rickettsias that are nonmotile.",
    "adjacent fact from the same lecture (rickettsias)"),
   ("It uses pili, not flagella",
    "Helicobacter is a motile curved cell that moves by several polar flagella, not by pili.",
    "confused structure")],
  c(31, 39)),

Q("Helicobacter", IO1,
  "How does Helicobacter pylori survive in the stomach?",
  ("Urease raises its local pH",
   "Correct: Helicobacter pylori produces urease, which converts urea into ammonium and bicarbonate, raising its "
   "local pH so the bacterium can survive."),
  [("It forms acid-proof spores",
    "Helicobacter forms no spores (an endospore is the Coxiella feature); it survives the stomach by making urease, "
    "which raises its local pH.", "adjacent fact from the same lecture (Coxiella)"),
   ("It hides inside host cells",
    "Living inside host cells is the obligate intracellular habit of rickettsias and chlamydias; Helicobacter "
    "survives by raising its local pH with urease.", "adjacent fact from the same lecture (obligate parasites)"),
   ("It lacks a cell wall",
    "Lacking a cell wall is the Mycoplasma feature; Helicobacter survives in the stomach by raising its local pH "
    "with urease.", "adjacent fact from the same lecture (Mycoplasma)")],
  c(39)),

Q("Helicobacter", IO1,
  "Helicobacter pylori's urease converts urea into which products?",
  ("Ammonium and bicarbonate",
   "Correct: urease converts urea into ammonium and bicarbonate, which raises the local pH and lets the bacterium "
   "survive in the stomach."),
  [("Lactic acid and water",
    "Acid production is what plaque bacteria do to dissolve tooth enamel; urease converts urea into ammonium and "
    "bicarbonate, which raise the pH.", "reversed effect (acid instead of base)"),
   ("Hydrochloric acid",
    "Making acid would lower the pH; urease converts urea into ammonium and bicarbonate, raising the local pH.",
    "reversed effect (acid instead of base)"),
   ("Glucose and nitrogen",
    "Urease does not make glucose; it converts urea into ammonium and bicarbonate, raising the local pH.",
    "confused chemistry")],
  c(39)),

Q("Helicobacter", IO1,
  "Which diseases is Helicobacter pylori linked to?",
  ("Ulcers and gastric cancer",
   "Correct: Helicobacter pylori causes most stomach and duodenal ulcers and is an apparent cofactor in gastric "
   "cancer."),
  [("Secretory diarrhea",
    "Secretory diarrhea is the effect of cholera toxin and the Campylobacter enterotoxin; Helicobacter pylori causes "
    "ulcers and is a cofactor in gastric cancer.", "competing curviform organism"),
   ("Atypical pneumonia",
    "Atypical pneumonia is caused by Mycoplasma pneumoniae and Chlamydophila pneumoniae; Helicobacter pylori causes "
    "ulcers.", "competing organism"),
   ("Dental caries",
    "Dental caries is acid damage to enamel by plaque bacteria; Helicobacter pylori causes stomach and duodenal "
    "ulcers.", "competing disease (dental)")],
  c(39)),

Q("Helicobacter", IO1,
  "In which specimens was Helicobacter pylori first discovered?",
  ("Stomach biopsies from ulcer patients",
   "Correct: Helicobacter pylori was discovered in stomach biopsies from ulcer patients by Warren and Marshall, who "
   "won the Nobel Prize in Medicine."),
  [("Stool from cholera patients",
    "Cholera stool is rice water diarrhea from Vibrio cholerae; Helicobacter pylori was found in stomach biopsies "
    "from ulcer patients.", "competing curviform organism"),
   ("Dental plaque from cavities",
    "Plaque harbors Streptococcus mutans and other caries bacteria; Helicobacter pylori was found in stomach "
    "biopsies from ulcer patients.", "competing setting (dental)"),
   ("Blood from patients with fever",
    "Blood holds spirochetes in early syphilis; Helicobacter pylori was found in stomach biopsies from ulcer "
    "patients.", "competing organism")],
  c(39)),

Q("Helicobacter", IO1,
  "Why does a gastric biopsy containing Helicobacter pylori turn a urease test gel positive?",
  ("Its urease raises the gel's pH",
   "Correct: the bacterium's urease converts urea into ammonium and bicarbonate, raising the pH; the gel reads "
   "negative at pH 5.2-5.8 and positive from pH 6.5 upward."),
  [("Its acid lowers the gel's pH",
    "The reaction goes the other way: urease raises the pH, and the gel reads positive from pH 6.5 upward.",
    "reversed direction"),
   ("It ferments sugar in the gel",
    "Sugar fermentation is not the test; urease converting urea raises the pH and turns the gel positive.",
    "confused test"),
   ("It lyses red cells in the gel",
    "Red cell lysis is not the reaction read; urease raises the pH of the gel, which is read against a pH scale.",
    "confused test")],
  ci(41, 39)),

Q("Helicobacter", IO1,
  "For discovering which organism did Warren and Marshall receive the Nobel Prize in Medicine?",
  ("Helicobacter pylori",
   "Correct: Warren and Marshall, Australian doctors, discovered Helicobacter pylori in stomach biopsies from ulcer "
   "patients and received the Nobel Prize in Medicine in 2005."),
  [("Treponema pallidum",
    "Treponema pallidum, the spirochete of syphilis, is not their discovery; Warren and Marshall discovered "
    "Helicobacter pylori.", "competing organism"),
   ("Vibrio cholerae",
    "Vibrio cholerae causes cholera; Warren and Marshall's Nobel discovery was Helicobacter pylori in ulcer "
    "patients' stomachs.", "competing curviform organism"),
   ("Coxiella burnetii",
    "Coxiella burnetii causes Q fever; Warren and Marshall discovered Helicobacter pylori in stomach biopsies.",
    "competing organism")],
  c(39)),

# ============================================================== RICKETTSIAS incl. Ehrlichia (slides 42-50)
Q("Rickettsias", IO1,
  "Which description fits Rickettsia?",
  ("Tiny, nonmotile Gram-negative rods",
   "Correct: rickettsias are obligate intracellular parasites with a Gram-negative wall, among the smallest "
   "bacteria, nonmotile pleomorphic rods or coccobacilli."),
  [("Large spirals with endoflagella",
    "Large spiral cells moving by endoflagella describe Borrelia, a spirochete; rickettsias are tiny, nonmotile "
    "Gram-negative rods or coccobacilli.", "wrong group (spirochetes)"),
   ("Wall-less, highly variable cells",
    "Lacking a cell wall describes Mycoplasma; rickettsias have a Gram-negative cell wall.",
    "adjacent fact from the same lecture (Mycoplasma)"),
   ("Comma rods with one flagellum",
    "Comma-shaped rods with one polar flagellum are Vibrio; rickettsias are tiny, nonmotile coccobacilli.",
    "wrong group (curviform)")],
  c(42, 44)),

Q("Rickettsias", IO1,
  "What do rickettsias need in order to be cultivated?",
  ("Live host cells",
   "Correct: rickettsias are very small intracellular parasites that require live cells for cultivation."),
  [("Blood agar alone",
    "Being cultured on blood agar is said of Bartonella, a fastidious relative; rickettsias require live cells.",
    "adjacent fact from the same lecture (Bartonella)"),
   ("Host-membrane lipids",
    "Special lipids from host membranes are what Mycoplasma requires; rickettsias require live host cells.",
    "adjacent fact from the same lecture (Mycoplasma)"),
   ("A salt-rich medium",
    "Salt tolerance belongs to the seafood vibrios; rickettsias need live cells to be cultivated.",
    "adjacent fact from the same lecture (seafood vibrios)")],
  c(43)),

Q("Rickettsias", IO1,
  "How do rickettsias damage blood vessels?",
  ("By invading endothelial cells",
   "Correct: rickettsias enter endothelial cells and cause necrosis of the vascular lining, giving vasculitis, "
   "vascular leakage and thrombosis."),
  [("By a heat-labile enterotoxin",
    "A heat-labile enterotoxin is the Campylobacter jejuni mechanism of diarrhea; rickettsias invade endothelial "
    "cells.", "competing organism (Campylobacter)"),
   ("By raising pH with urease",
    "Urease raising local pH is Helicobacter pylori's survival trick in the stomach; rickettsias invade the "
    "endothelium.", "competing organism (Helicobacter)"),
   ("By acid that dissolves tissue",
    "Acid dissolving a surface is how plaque bacteria damage enamel; rickettsias damage vessels by invading "
    "endothelial cells.", "competing mechanism (dental)")],
  c(44)),

Q("Rickettsias", IO2,
  "Which vector carries Rickettsia prowazekii, the cause of epidemic typhus?",
  ("Body lice",
   "Correct: epidemic typhus is caused by Rickettsia prowazekii, carried by lice; louse feces are rubbed into the "
   "bite, and humans are the primary reservoir."),
  [("Fleas",
    "Fleas carry Rickettsia typhi, the cause of endemic (murine) typhus; epidemic typhus is carried by body lice.",
    "competing species (Rickettsia typhi)"),
   ("Ticks",
    "Ticks carry Rickettsia rickettsii (Rocky Mountain spotted fever) and Ehrlichia; epidemic typhus is carried by "
    "body lice.", "competing species (Rickettsia rickettsii)"),
   ("Mites",
    "Mites carry rickettsialpox and scrub typhus; epidemic typhus is carried by body lice.",
    "competing rickettsial disease")],
  ci(47, 45)),

Q("Rickettsias", IO1,
  "Which organism causes endemic (murine) typhus?",
  ("Rickettsia typhi",
   "Correct: endemic typhus is caused by Rickettsia typhi, harbored by mice and rats; it occurs sporadically where "
   "fleas are heavy and has milder symptoms."),
  [("Rickettsia prowazekii",
    "Rickettsia prowazekii causes epidemic typhus, carried by lice; endemic typhus is Rickettsia typhi.",
    "competing species"),
   ("Rickettsia rickettsii",
    "Rickettsia rickettsii causes Rocky Mountain spotted fever, carried by ticks; endemic typhus is Rickettsia "
    "typhi.", "competing species"),
   ("Coxiella burnetii",
    "Coxiella burnetii causes Q fever, usually inhaled; endemic typhus is Rickettsia typhi.",
    "related organism")],
  c(45)),

Q("Rickettsias", IO2,
  "How is endemic typhus spread to people?",
  ("Flea feces rubbed into the skin",
   "Correct: Rickettsia typhi is harbored by mice and rats and spread by fleas; flea feces are rubbed into the skin "
   "(or inhaled), so it occurs where fleas are heavy."),
  [("Louse feces rubbed into bites",
    "Louse feces rubbed into the bite spread epidemic typhus (Rickettsia prowazekii); endemic typhus is spread by "
    "fleas.", "competing species (epidemic typhus)"),
   ("The bite of a dog tick",
    "Dog and wood ticks carry Rocky Mountain spotted fever; endemic typhus is spread by flea feces rubbed into the "
    "skin.", "competing species (Rocky Mountain spotted fever)"),
   ("The bite of an immature mite",
    "Immature mites spread scrub typhus (Orientia tsutsugamushi); endemic typhus is spread by fleas.",
    "competing rickettsial disease")],
  ci(47, 45)),

Q("Rickettsias", IO1,
  "What is Brill-Zinsser disease?",
  ("Recurrent epidemic typhus",
   "Correct: Brill-Zinsser disease is the chronic, recurrent form of epidemic typhus, caused by Rickettsia "
   "prowazekii."),
  [("Milder flea-borne typhus",
    "The milder flea-borne typhus is endemic typhus (Rickettsia typhi); Brill-Zinsser is the chronic recurrent "
    "form of epidemic typhus.", "competing disease"),
   ("Tick-borne spotted fever",
    "The tick-borne spotted fever is Rocky Mountain spotted fever; Brill-Zinsser is recurrent epidemic typhus.",
    "competing disease"),
   ("Relapsing Borrelia fever",
    "Relapsing fever is Borrelia hermsii, a spirochete; Brill-Zinsser is the recurrent form of epidemic typhus.",
    "competing recurrent fever")],
  c(45)),

Q("Rickettsias", IO1,
  "The Weil-Felix test detects rickettsial infection by cross-reaction with which bacterium?",
  ("Proteus",
   "Correct: the Weil-Felix test rests on a cross reaction between Proteus bacteria and Rickettsia prowazekii."),
  [("Vibrio",
    "Vibrio is a curviform enteric organism with no part in the Weil-Felix test; the test uses cross reaction with "
    "Proteus.", "unrelated organism"),
   ("Bartonella",
    "Bartonella is related to the rickettsioses but is not the test organism; Weil-Felix uses cross reaction with "
    "Proteus.", "related organism"),
   ("Treponema",
    "Treponema infection is tested with serological tests such as the rapid plasma reagin test; the Weil-Felix test "
    "uses Proteus.",
    "competing test")],
  c(45)),

Q("Rickettsias", IO1,
  "Which organism causes Rocky Mountain spotted fever?",
  ("Rickettsia rickettsii",
   "Correct: Rocky Mountain spotted fever is a Rickettsia rickettsii zoonosis carried by dog and wood ticks, with a "
   "distinct spotted rash."),
  [("Rickettsia typhi",
    "Rickettsia typhi causes endemic (murine) typhus, spread by fleas; Rocky Mountain spotted fever is Rickettsia "
    "rickettsii.", "competing species"),
   ("Rickettsia akari",
    "Rickettsia akari causes rickettsialpox, spread by mite bite; Rocky Mountain spotted fever is Rickettsia "
    "rickettsii.", "competing species"),
   ("Borrelia burgdorferi",
    "Borrelia burgdorferi causes Lyme disease, another tick-borne illness; Rocky Mountain spotted fever is "
    "Rickettsia rickettsii.", "competing tick-borne disease")],
  ci(47, 46)),

Q("Rickettsias", IO2,
  "Which vectors carry Rocky Mountain spotted fever?",
  ("Dog and wood ticks",
   "Correct: Rocky Mountain spotted fever is a Rickettsia rickettsii zoonosis carried by dog and wood ticks; the "
   "cycle runs between ticks and dogs, with humans infected by tick bite."),
  [("Ixodes ticks",
    "Ixodes ticks transmit Lyme disease; Rocky Mountain spotted fever is carried by dog and wood ticks.",
    "competing tick-borne disease"),
   ("Body lice",
    "Body lice carry epidemic typhus and trench fever; Rocky Mountain spotted fever is carried by dog and wood "
    "ticks.", "wrong vector"),
   ("Rat fleas",
    "Fleas carry endemic typhus from rodents; Rocky Mountain spotted fever is carried by dog and wood ticks.",
    "wrong vector")],
  ci(49, 46)),

Q("Rickettsias", IO1,
  "Where in the United States do most cases of Rocky Mountain spotted fever occur?",
  ("The Southeast and East Coast",
   "Correct: despite its name, most Rocky Mountain spotted fever cases occur in the Southeast United States and on "
   "the eastern seaboard."),
  [("The Rocky Mountain states",
    "The name misleads: most cases are in the Southeast and along the eastern seaboard, not the Rocky Mountains.",
    "common belief from the disease's name"),
   ("The Pacific Northwest",
    "The Pacific Northwest is not where most cases are; they are in the Southeast and along the eastern seaboard.",
    "unsupported region"),
   ("The desert Southwest",
    "The desert Southwest is not where most cases are; they are in the Southeast and along the eastern seaboard.",
    "unsupported region")],
  c(46)),

Q("Rickettsias", IO1,
  "The early rash of Rocky Mountain spotted fever may be misdiagnosed as which viral disease?",
  ("Measles",
   "Correct: the early rash may be misdiagnosed as measles, a viral disease with significantly different treatment "
   "options."),
  [("Chickenpox",
    "Chickenpox is not the disease named; the early Rocky Mountain spotted fever rash is mistaken for measles, which "
    "is treated very differently.", "unlisted viral rash"),
   ("Rubella",
    "Rubella is not the disease named; the early Rocky Mountain spotted fever rash is mistaken for measles.",
    "unlisted viral rash"),
   ("Influenza",
    "Influenza is not a rash illness here; the early Rocky Mountain spotted fever rash is mistaken for measles.",
    "unlisted viral illness")],
  c(50)),

Q("Rickettsias", IO1,
  "A camper who was bitten by a tick develops fever and the spotted rash shown. Which organism is most likely?",
  ("Rickettsia rickettsii",
   "Correct: a tick bite followed by fever and a distinct spotted rash is Rocky Mountain spotted fever, caused by "
   "Rickettsia rickettsii; its early rash may be mistaken for measles."),
  [("Borrelia burgdorferi",
    "Lyme disease is tick-borne too, but its rash is one expanding bull's-eye patch at the bite, not a spotted "
    "rash.", "competing tick-borne disease"),
   ("Rickettsia prowazekii",
    "Rickettsia prowazekii causes epidemic typhus, carried by body lice rather than ticks.", "wrong vector"),
   ("Treponema pallidum",
    "Treponema pallidum is spread sexually, not by tick bite; its rash is secondary syphilis on the palms and soles.",
    "competing rash")],
  ci(50, 46), img=IMG + "/l13-s50-spotted-rash.jpg",
  alt="A wrist and hand covered in many small, flat, red spots.", slide="Slide 50"),

Q("Rickettsias", IO1,
  "Which disease does Ehrlichia chaffeensis cause?",
  ("Human monocytic ehrlichiosis",
   "Correct: Ehrlichia chaffeensis causes human monocytic ehrlichiosis, a tick-borne infection whose distribution "
   "is similar to that of Rocky Mountain spotted fever."),
  [("Rocky Mountain spotted fever",
    "Rocky Mountain spotted fever is caused by Rickettsia rickettsii; Ehrlichia chaffeensis causes human monocytic "
    "ehrlichiosis, also tick-borne and found in similar places.", "competing tick-borne disease"),
   ("Epidemic louse-borne typhus",
    "Epidemic typhus is caused by Rickettsia prowazekii and carried by body lice; Ehrlichia chaffeensis causes human "
    "monocytic ehrlichiosis.", "competing rickettsial disease"),
   ("Mite-borne rickettsialpox",
    "Rickettsialpox is caused by Rickettsia akari, spread by mite bite from mice; Ehrlichia chaffeensis causes human "
    "monocytic ehrlichiosis.", "competing rickettsial disease")],
  ci(47, 46)),

Q("Rickettsias", IO2,
  "How is human ehrlichiosis transmitted?",
  ("By tick bite",
   "Correct: Ehrlichia are tick-borne bacteria; human ehrlichiosis is acquired by tick bite."),
  [("By louse feces",
    "Louse feces rubbed into a bite spread epidemic typhus; human ehrlichiosis is acquired by tick bite.",
    "competing rickettsial disease"),
   ("By mite bite",
    "Mite bites spread rickettsialpox and scrub typhus; human ehrlichiosis is acquired by tick bite.",
    "competing rickettsial disease"),
   ("By inhaled dust",
    "Inhaled particles spread Q fever; human ehrlichiosis is acquired by tick bite.",
    "related organism (Coxiella)")],
  ci(47, 46)),

Q("Rickettsias", IO2,
  "Which vector transmits scrub typhus?",
  ("Immature mites",
   "Correct: scrub typhus, caused by Orientia tsutsugamushi, is spread by the bite of immature mites, with rodents "
   "as the reservoir, in Asia, Australia and the Pacific Islands."),
  [("Body lice",
    "Body lice transmit epidemic typhus; scrub typhus is spread by immature mites.", "competing rickettsial disease"),
   ("Fleas",
    "Fleas transmit endemic (murine) typhus; scrub typhus is spread by immature mites.",
    "competing rickettsial disease"),
   ("Ticks",
    "Ticks transmit Rocky Mountain spotted fever and ehrlichiosis; scrub typhus is spread by immature mites.",
    "competing rickettsial disease")],
  ci(47)),

# ============================================================== COXIELLA and BARTONELLA (slides 51-54)
Q("Coxiella & Bartonella", IO1,
  "Which organism causes Q fever?",
  ("Coxiella burnetii",
   "Correct: Coxiella burnetii, an intracellular parasite related to the rickettsias, causes Q fever (Q for "
   "\"query\", or unknown)."),
  [("Chlamydophila psittaci",
    "Chlamydophila psittaci causes ornithosis, a bird-borne pneumonia; Q fever is caused by Coxiella burnetii.",
    "competing pneumonia"),
   ("Rickettsia rickettsii",
    "Rickettsia rickettsii causes Rocky Mountain spotted fever, carried by ticks; Q fever is Coxiella burnetii.",
    "related organism"),
   ("Leptospira interrogans",
    "Leptospira interrogans causes leptospirosis from mammal urine; Q fever is caused by Coxiella burnetii.",
    "competing zoonosis")],
  c(51, 52)),

Q("Coxiella & Bartonella", IO2,
  "How is Q fever usually acquired?",
  ("By inhalation",
   "Correct: Coxiella's infectious material includes urine, feces, milk and airborne particles, and it is usually "
   "inhaled, causing pneumonitis, fever and inflammation of the liver."),
  [("By raw oysters",
    "Raw oysters transmit Vibrio vulnificus; Q fever is usually acquired by inhaling infectious particles.",
    "competing organism (seafood vibrios)"),
   ("By louse feces",
    "Louse feces rubbed into a bite spread epidemic typhus; Q fever is usually acquired by inhaling infectious "
    "particles.",
    "competing rickettsial disease"),
   ("By sexual contact",
    "Sexual contact spreads syphilis and Chlamydia trachomatis; Q fever is usually acquired by inhalation.",
    "competing organism")],
  c(52)),

Q("Coxiella & Bartonella", IO1,
  "Which unusual structure does Coxiella burnetii produce?",
  ("A resistant endospore",
   "Correct: Coxiella burnetii produces an unusually resistant endospore."),
  [("An elementary body",
    "The elementary body is the infectious form of the chlamydias; Coxiella burnetii produces an unusually "
    "resistant endospore.", "adjacent fact from the same lecture (Chlamydia)"),
   ("An endoflagellum",
    "Endoflagella are the motility organs of the spirochetes; Coxiella burnetii produces a resistant endospore.",
    "adjacent fact from the same lecture (spirochetes)"),
   ("A urease enzyme",
    "Urease is Helicobacter pylori's means of raising its local pH; Coxiella burnetii produces a resistant "
    "endospore.", "adjacent fact from the same lecture (Helicobacter)")],
  c(52)),

Q("Coxiella & Bartonella", IO2,
  "Which group is at highest risk of Q fever?",
  ("Farmers and veterinarians",
   "Correct: a Q fever vaccine is available, and veterinarians, farmers and lab technicians are at highest risk; "
   "historic cases most likely arose from contaminated milking barns."),
  [("Surfers and water-skiers",
    "Surfers and water-skiers are named as at risk of leptospirosis from urine-contaminated water, not Q fever.",
    "competing organism (Leptospira)"),
   ("Owners of pet cats",
    "Cat owners risk cat-scratch disease from Bartonella; Q fever risk is highest for farmers, veterinarians and lab "
    "technicians.", "competing organism (Bartonella)"),
   ("Hikers in tick country",
    "Hikers risk tick-borne disease such as Lyme disease; Q fever risk is highest for farmers, veterinarians and lab "
    "technicians.", "competing tick-borne disease")],
  c(52)),

Q("Coxiella & Bartonella", IO1,
  "What does Q fever usually cause once inhaled?",
  ("Pneumonitis, fever and hepatitis",
   "Correct: Q fever is usually inhaled, causing pneumonitis, fever and inflammation of the liver; it is treated "
   "with tetracycline."),
  [("A bull's-eye rash and arthritis",
    "A bull's-eye rash and polyarthritis are Lyme disease; inhaled Q fever causes pneumonitis, fever and liver "
    "inflammation.", "competing disease (Lyme)"),
   ("Rice water stool",
    "Rice water stool is cholera's secretory diarrhea; Q fever causes pneumonitis, fever and liver inflammation.",
    "competing disease (cholera)"),
   ("Gummas in organs",
    "Gummas are tertiary syphilis; Q fever causes pneumonitis, fever and inflammation of the liver.",
    "competing disease (syphilis)")],
  c(52)),

Q("Coxiella & Bartonella", IO1,
  "Which genus causes cat-scratch disease?",
  ("Bartonella",
   "Correct: Bartonella species cause cat-scratch disease, a lymphatic infection after a clawing injury by a cat, "
   "as well as trench fever and bacillary angiomatosis."),
  [("Coxiella",
    "Coxiella causes Q fever, usually inhaled; cat-scratch disease is caused by Bartonella.", "related organism"),
   ("Chlamydophila",
    "Chlamydophila causes atypical pneumonia and bird-borne ornithosis; cat-scratch disease is caused by "
    "Bartonella.", "competing organism"),
   ("Leptospira",
    "Leptospira causes leptospirosis from mammal urine; cat-scratch disease is caused by Bartonella.",
    "competing zoonosis")],
  c(53, 54)),

Q("Coxiella & Bartonella", IO2,
  "How is trench fever spread?",
  ("By lice",
   "Correct: trench fever, caused by Bartonella, is spread by lice."),
  [("By cat scratches",
    "A cat's clawing injury transmits cat-scratch disease, another Bartonella infection; trench fever is spread by "
    "lice.", "right genus, wrong disease"),
   ("By tick bites",
    "Ticks spread Lyme disease and Rocky Mountain spotted fever; trench fever is spread by lice.", "wrong vector"),
   ("By inhaled dust",
    "Inhaled particles spread Q fever; trench fever is spread by lice.", "related organism (Coxiella)")],
  c(53)),

Q("Coxiella & Bartonella", IO1,
  "Which Bartonella disease occurs in patients with acquired immunodeficiency syndrome?",
  ("Bacillary angiomatosis",
   "Correct: Bartonella causes bacillary angiomatosis in patients with acquired immunodeficiency syndrome, besides "
   "trench fever and cat-scratch disease."),
  [("Trench fever",
    "Trench fever is the louse-borne Bartonella infection; the one in acquired immunodeficiency syndrome is "
    "bacillary angiomatosis.", "competing disease, same genus"),
   ("Cat-scratch disease",
    "Cat-scratch disease follows a clawing injury by a cat; the Bartonella infection of acquired immunodeficiency "
    "syndrome is bacillary angiomatosis.", "competing disease, same genus"),
   ("Q fever",
    "Q fever is caused by Coxiella, not Bartonella; the Bartonella infection of acquired immunodeficiency syndrome "
    "is bacillary angiomatosis.", "related organism")],
  c(53)),

Q("Coxiella & Bartonella", IO1,
  "Why is tetracycline a treatment for so many different bacteria, from Borrelia to Mycoplasma?",
  ("Broad spectrum, 30S ribosome target",
   "Correct: tetracycline is a very broad-spectrum antibiotic that targets prokaryotic ribosomes, at the 30S "
   "subunit; it is named for relapsing fever, Lyme disease, cholera, Q fever, Bartonella and Mycoplasma."),
  [("Peptidoglycan synthesis blockade",
    "Acting on peptidoglycan is why penicillin fails against Mycoplasma, which has none; tetracycline targets the "
    "prokaryotic 30S ribosomal subunit.", "confused drug mechanism (penicillin)"),
   ("Selective Gram-negative wall attack",
    "Tetracycline acts on ribosomes, not on cell walls; it is very broad-spectrum, targeting the prokaryotic 30S "
    "subunit.", "confused drug mechanism"),
   ("Replacement of lost electrolytes",
    "Electrolyte replacement is rehydration therapy, as in cholera; tetracycline is an antibiotic targeting the "
    "prokaryotic 30S ribosomal subunit.", "treatment category confused")],
  c(53, 24, 26, 32, 52, 62)),

# ============================================================== CHLAMYDIAS incl. Chlamydophila (slides 56-61)
Q("Chlamydias", IO1,
  "Which chlamydial form is the infectious one released by the infected host cell?",
  ("The elementary body",
   "Correct: the elementary body is small, metabolically inactive, extracellular and infectious, released by the "
   "infected host cell; the reticulate body is the noninfectious dividing form."),
  [("The reticulate body",
    "The reticulate body is the noninfectious, actively dividing form inside host cell vacuoles; the infectious form "
    "is the elementary body.", "reversed pair"),
   ("The endospore",
    "Chlamydias make no endospore (the resistant endospore is Coxiella's); their infectious form is the elementary "
    "body.", "adjacent fact from the same lecture (Coxiella)"),
   ("The inclusion body",
    "The inclusion body is the mass of chlamydias seen inside an infected cell; the infectious form released is "
    "the elementary body.", "confused structure")],
  ci(57, 56)),

Q("Chlamydias", IO1,
  "What does the chlamydial reticulate body do?",
  ("Divides inside host cell vacuoles",
   "Correct: the reticulate body is the noninfectious, actively dividing form that grows within host cell "
   "vacuoles, though it cannot make its own adenosine triphosphate."),
  [("Survives outside cells to infect",
    "Surviving outside cells and infecting is the job of the elementary body; the reticulate body divides inside "
    "host cell vacuoles.", "reversed pair"),
   ("Makes its own energy supply",
    "It cannot make its own adenosine triphosphate; the reticulate body divides inside host cell vacuoles using the "
    "host's.", "reversed fact"),
   ("Forms a resistant spore",
    "Chlamydias do not form spores; the reticulate body is the dividing form inside host cell vacuoles.",
    "adjacent fact from the same lecture (Coxiella)")],
  ci(57, 56)),

Q("Chlamydias", IO2,
  "How does a newborn acquire chlamydial inclusion conjunctivitis?",
  ("Via the birth canal",
   "Correct: inclusion conjunctivitis occurs as the baby passes through the birth canal, and it is prevented by "
   "prophylaxis."),
  [("Across the placenta",
    "Trans-placental infection is how congenital syphilis is acquired; inclusion conjunctivitis is acquired in the "
    "birth canal.", "competing organism (Treponema pallidum)"),
   ("From flies after birth",
    "Flying insects belong to the setting of ocular trachoma in poor sanitation; inclusion conjunctivitis is "
    "acquired in the birth canal.", "competing chlamydial disease"),
   ("From a pet bird at home",
    "Birds transmit Chlamydophila psittaci (ornithosis); inclusion conjunctivitis is acquired in the birth canal.",
    "competing chlamydial species")],
  ci(59, 58)),

Q("Chlamydias", IO1,
  "Which chlamydial disease deforms the eyelid and cornea and may cause blindness?",
  ("Ocular trachoma",
   "Correct: ocular trachoma is a severe infection that deforms the eyelid and cornea and may cause blindness."),
  [("Inclusion conjunctivitis",
    "Inclusion conjunctivitis is the newborn's eye infection from the birth canal, prevented by prophylaxis; the "
    "blinding eyelid and corneal disease is ocular trachoma.", "competing chlamydial disease"),
   ("Lymphogranuloma venereum",
    "Lymphogranuloma venereum disfigures the external genitalia and pelvic lymphatics; the blinding eye disease is "
    "ocular trachoma.", "competing chlamydial disease"),
   ("Ornithosis",
    "Ornithosis is a bird-borne pneumonia from Chlamydophila psittaci; the blinding eye disease is ocular trachoma.",
    "competing chlamydial species")],
  c(58)),

Q("Chlamydias", IO1,
  "Which Chlamydia trachomatis disease disfigures the external genitalia and pelvic lymphatic system?",
  ("Lymphogranuloma venereum",
   "Correct: lymphogranuloma venereum is a disfiguring disease of the external genitalia and the pelvic lymphatic "
   "system, one of the two strains of Chlamydia trachomatis."),
  [("Ocular trachoma",
    "Ocular trachoma deforms the eyelid and cornea; the genital and pelvic lymphatic disease is lymphogranuloma "
    "venereum.", "competing chlamydial disease"),
   ("Bacillary angiomatosis",
    "Bacillary angiomatosis is a Bartonella infection in acquired immunodeficiency syndrome; the chlamydial "
    "lymphatic disease is lymphogranuloma venereum.", "competing organism (Bartonella)"),
   ("Pinta",
    "Pinta is a depigmenting skin lesion from Treponema carateum; the chlamydial genital lymphatic disease is "
    "lymphogranuloma venereum.", "competing organism (Treponema)")],
  c(58)),

Q("Chlamydias", IO1,
  "Which complications can genital Chlamydia trachomatis infection cause?",
  ("Salpingitis and infertility",
   "Correct: as a sexually transmitted disease, Chlamydia trachomatis causes urethritis, cervicitis, salpingitis "
   "(pelvic inflammatory disease), infertility and scarring."),
  [("Gummas and heart disease",
    "Gummas and cardiovascular disease are tertiary syphilis; genital Chlamydia trachomatis causes pelvic "
    "inflammatory disease and infertility.", "competing sexually transmitted organism"),
   ("Bacillary angiomatosis",
    "Bacillary angiomatosis is a Bartonella infection in acquired immunodeficiency syndrome, not a chlamydial "
    "genital complication.", "competing organism (Bartonella)"),
   ("Hutchinson's teeth",
    "Hutchinson's teeth are a sign of congenital syphilis; genital Chlamydia trachomatis leads to pelvic "
    "inflammatory disease and infertility.", "competing sexually transmitted organism")],
  c(58)),

Q("Chlamydias", IO2,
  "What is the reservoir of Chlamydia trachomatis?",
  ("Humans",
   "Correct: Chlamydia trachomatis has a human reservoir; its two strains cause trachoma and lymphogranuloma "
   "venereum."),
  [("Birds",
    "Birds are the source of Chlamydophila psittaci, the cause of ornithosis; Chlamydia trachomatis has a human "
    "reservoir.", "competing chlamydial species"),
   ("Rodents",
    "Rodents are reservoirs of Rickettsia typhi and Borrelia hermsii; Chlamydia trachomatis has a human reservoir.",
    "competing organism"),
   ("Cattle",
    "Cattle pass Campylobacter fetus between themselves; Chlamydia trachomatis has a human reservoir.",
    "competing organism")],
  c(58)),

Q("Chlamydias", IO1,
  "Which organism causes ornithosis?",
  ("Chlamydophila psittaci",
   "Correct: Chlamydophila psittaci causes ornithosis, a zoonosis transmitted to humans from birds (\"ornith\" = "
   "bird), with pneumonia or a flulike infection."),
  [("Chlamydophila pneumoniae",
    "Chlamydophila pneumoniae causes an atypical pneumonia that is serious in asthma patients; ornithosis is "
    "Chlamydophila psittaci.", "competing species"),
   ("Chlamydia trachomatis",
    "Chlamydia trachomatis causes trachoma and lymphogranuloma venereum, with a human reservoir; ornithosis is "
    "Chlamydophila psittaci.", "competing species"),
   ("Coxiella burnetii",
    "Coxiella burnetii causes Q fever, usually inhaled from farm animals; ornithosis is Chlamydophila psittaci.",
    "competing pneumonia")],
  c(61)),

Q("Chlamydias", IO2,
  "How is ornithosis transmitted to humans?",
  ("From birds",
   "Correct: ornithosis (Chlamydophila psittaci) is a zoonosis transmitted to humans from birds and is highly "
   "communicable among all birds."),
  [("From ticks",
    "Ticks transmit Lyme disease and Rocky Mountain spotted fever; ornithosis comes from birds.", "wrong vector"),
   ("From cats",
    "Cats transmit cat-scratch disease (Bartonella); ornithosis comes from birds.", "competing organism"),
   ("From lice",
    "Lice transmit epidemic typhus and trench fever; ornithosis comes from birds.", "wrong vector")],
  c(61)),

Q("Chlamydias", IO1,
  "Chlamydophila pneumoniae causes an atypical pneumonia that is serious in which patients?",
  ("Patients with asthma",
   "Correct: Chlamydophila pneumoniae causes an atypical pneumonia that is serious in asthma patients."),
  [("Patients with diabetes",
    "Diabetes or liver disease makes Vibrio vulnificus serious; Chlamydophila pneumoniae pneumonia is serious in "
    "asthma patients.", "competing organism (Vibrio vulnificus)"),
   ("Women late in pregnancy",
    "Late pregnancy is the risk for Campylobacter fetus; Chlamydophila pneumoniae pneumonia is serious in asthma "
    "patients.", "competing organism (Campylobacter fetus)"),
   ("Patients with immunodeficiency",
    "Acquired immunodeficiency syndrome is the setting of Bartonella's bacillary angiomatosis; Chlamydophila "
    "pneumoniae pneumonia is serious in asthma.", "competing organism (Bartonella)")],
  c(61)),

# ============================================================== MYCOPLASMA (slides 62-63)
Q("Mycoplasma", IO1,
  "Why is penicillin not used against Mycoplasma?",
  ("They have no peptidoglycan",
   "Correct: mycoplasmas naturally lack cell walls, so no peptidoglycan is present; they are treated with "
   "tetracycline or erythromycin instead."),
  [("They live inside host cells",
    "Obligate intracellular life is the rickettsia and chlamydia habit; penicillin fails against Mycoplasma because "
    "it has no peptidoglycan.", "adjacent fact from the same lecture (obligate parasites)"),
   ("They form resistant endospores",
    "A resistant endospore is the Coxiella feature; penicillin fails against Mycoplasma because it lacks "
    "peptidoglycan.", "adjacent fact from the same lecture (Coxiella)"),
   ("Their outer membrane blocks it",
    "Mycoplasma has no cell wall at all; penicillin fails because no peptidoglycan is present.",
    "confused structure")],
  c(42, 62)),

Q("Mycoplasma", IO1,
  "Which disease does Mycoplasma pneumoniae cause?",
  ("Primary atypical pneumonia",
   "Correct: Mycoplasma pneumoniae causes primary atypical pneumonia, slowly spreading over the interior "
   "respiratory surfaces with fever, chest pain and sore throat."),
  [("Lymphogranuloma venereum",
    "Lymphogranuloma venereum is a Chlamydia trachomatis disease of the genitalia and pelvic lymphatics; Mycoplasma "
    "pneumoniae causes primary atypical pneumonia.", "competing organism"),
   ("Trench fever",
    "Trench fever is a louse-borne Bartonella infection; Mycoplasma pneumoniae causes primary atypical pneumonia.",
    "competing organism"),
   ("Inclusion conjunctivitis",
    "Inclusion conjunctivitis is the newborn's chlamydial eye infection; Mycoplasma pneumoniae causes primary "
    "atypical pneumonia.", "competing organism")],
  c(62)),

Q("Mycoplasma", IO1,
  "What do mycoplasmas require from host cell membranes?",
  ("Special lipids",
   "Correct: mycoplasmas naturally lack cell walls, are highly pleomorphic and require special lipids from host "
   "membranes."),
  [("Adenosine triphosphate",
    "Needing the host's adenosine triphosphate describes the chlamydial reticulate body; mycoplasmas require "
    "special lipids from host membranes.", "adjacent fact from the same lecture (Chlamydia)"),
   ("Urea for urease",
    "Urea is what Helicobacter pylori's urease converts to raise its local pH; mycoplasmas need special host "
    "lipids.", "adjacent fact from the same lecture (Helicobacter)"),
   ("Peptidoglycan",
    "Mycoplasmas have no peptidoglycan and take none from the host; what they require is special lipids from host "
    "membranes.", "confused structure")],
  c(62)),

Q("Mycoplasma", IO1,
  "Which description fits the shape of mycoplasmas?",
  ("Highly variable (pleomorphic)",
   "Correct: mycoplasmas naturally lack cell walls and are highly pleomorphic; their cell shapes can be highly "
   "variable."),
  [("Rigid, regular spirals",
    "Regular spirals belong to spirochetes such as Treponema; mycoplasmas lack a wall, so their shape is highly "
    "variable.", "competing group"),
   ("Comma-shaped rods",
    "Comma-shaped rods are Vibrio; mycoplasmas are highly pleomorphic because they lack a cell wall.",
    "competing group"),
   ("Gull-winged pairs",
    "Gull-winged pairs are Campylobacter; mycoplasmas are highly pleomorphic because they lack a cell wall.",
    "competing group")],
  ci(63, 62)),

# ============================================================== DENTAL DISEASE (slides 64-70)
Q("Dental disease", IO1,
  "Which is the most commonly diagnosed of all diseases in humans?",
  ("Dental caries",
   "Correct: dental caries, a slow progressive infection of irregular areas of the enamel surface, is the most "
   "commonly diagnosed of all diseases in humans."),
  [("Periodontitis",
    "Periodontitis is infection that reaches the tooth socket and can lose the tooth; the most commonly diagnosed "
    "disease is dental caries.", "competing dental disease"),
   ("Chlamydia infection",
    "Chlamydia is the first or second most prevalent sexually transmitted disease, not the most commonly diagnosed "
    "of all diseases; that is dental caries.", "adjacent fact from the same lecture (Chlamydia)"),
   ("Gingivitis",
    "Gingivitis is inflammation of the gums from calculus; the most commonly diagnosed of all diseases is dental "
    "caries.", "competing dental disease")],
  c(64)),

Q("Dental disease", IO1,
  "Which bacterium is commonly found as dental plaque begins to form?",
  ("Streptococcus mutans",
   "Correct: caries begins with colonization by slime-forming species of Streptococcus, with cross adherence with "
   "Actinomyces in the biofilm; Streptococcus mutans is commonly found."),
  [("Lactobacillus",
    "Lactobacillus is a secondary invader that appears if plaque is left on the teeth; the early colonizer commonly "
    "found is Streptococcus mutans.", "right setting, wrong stage"),
   ("Fusobacterium",
    "Fusobacterium is a secondary invader of plaque left on the teeth; the early colonizer commonly found is "
    "Streptococcus mutans.", "right setting, wrong stage"),
   ("Helicobacter pylori",
    "Helicobacter pylori lives in the stomach and causes ulcers; the plaque-forming streptococcus is Streptococcus "
    "mutans.", "competing organism (Helicobacter)")],
  c(64)),

Q("Dental disease", IO1,
  "How does dental plaque damage tooth enamel?",
  ("Its bacteria make acid",
   "Correct: plaque harbors masses of bacteria that produce acid, which dissolves the enamel, leading to dental "
   "caries."),
  [("Its bacteria make urease",
    "Urease raises pH and belongs to Helicobacter pylori; plaque bacteria damage enamel by producing acid.",
    "reversed effect (base instead of acid)"),
   ("It hardens into the gums",
    "Hardened plaque is calculus, which irritates the gums and causes gingivitis; enamel is dissolved by the "
    "plaque bacteria's acid.", "right structure, wrong effect"),
   ("It blocks the tooth's blood",
    "Plaque sits on the enamel surface; it damages enamel through the acid its bacteria produce.",
    "confused mechanism")],
  c(64)),

Q("Dental disease", IO1,
  "What is dental calculus?",
  ("Mineralized plaque",
   "Correct: calculus is mineralized (calcified) plaque, which forms above and below the gingiva and irritates it, "
   "causing gingivitis."),
  [("A cavity in the enamel",
    "A cavity in the enamel is dental caries from acid damage; calculus is mineralized plaque.",
    "competing dental lesion"),
   ("Inflamed gum tissue",
    "Inflamed gingiva is gingivitis, which calculus causes; calculus itself is mineralized plaque.",
    "effect confused with cause"),
   ("An infected tooth socket",
    "Infection of the tooth socket is periodontitis; calculus is mineralized plaque.", "competing dental lesion")],
  c(67, 68)),

Q("Dental disease", IO1,
  "In periodontal disease, which bacteria invade the pockets between the tooth and gingiva?",
  ("Spirochetes and Gram-negative bacilli",
   "Correct: the pockets between tooth and gingiva are invaded by bacteria, spirochetes and Gram-negative bacilli; "
   "the tooth socket may become involved (periodontitis) and the tooth may be lost."),
  [("Mycoplasmas and chlamydias",
    "Mycoplasmas and chlamydias are respiratory, genital and eye pathogens; the gingival pockets are invaded by "
    "spirochetes and Gram-negative bacilli.", "wrong organism group"),
   ("Vibrios and campylobacters",
    "Vibrios and campylobacters are enteric curviform bacteria; the gingival pockets are invaded by spirochetes and "
    "Gram-negative bacilli.", "wrong organism group"),
   ("Rickettsias and Coxiella",
    "Rickettsias and Coxiella are intracellular, arthropod- or inhalation-acquired agents; the gingival pockets are "
    "invaded by spirochetes and Gram-negative bacilli.", "wrong organism group")],
  c(67)),

Q("Dental disease", IO1,
  "In the progression of dental disease, which step leads toward gingivitis rather than toward caries?",
  ("Calculus formation",
   "Correct: after plaque forms, one branch is acidification and cavitation leading to caries; the other is "
   "calculus (tartar) formation, leading to gingivitis, periodontal disease and bone resorption."),
  [("Acidification and cavitation",
    "Acidification and cavitation lead to dental caries and tooth destruction; the gingivitis branch begins with "
    "calculus formation.", "competing branch"),
   ("Pellicle formation",
    "Pellicle formation comes before plaque and leads to both branches; the gingivitis branch begins with calculus "
    "formation.", "earlier shared step"),
   ("Damage to the enamel",
    "Enamel damage is dental caries on the acid branch; the gingivitis branch begins with calculus formation.",
    "competing branch")],
  ci(66, 67)),

Q("Dental disease", IO1,
  "What is periodontitis?",
  ("Infection reaching the tooth socket",
   "Correct: when bacteria invade the pockets between tooth and gingiva, the tooth socket may become involved "
   "(periodontitis) and the tooth may be lost."),
  [("Gum inflammation from calculus",
    "Inflamed gingiva from calculus is gingivitis, the earlier stage; periodontitis is when the tooth socket is "
    "involved.", "earlier stage"),
   ("Acid damage to the enamel",
    "Acid damage to enamel is dental caries; periodontitis is infection that involves the tooth socket.",
    "competing dental disease"),
   ("Mineralized plaque on teeth",
    "Mineralized plaque is calculus; periodontitis is infection that involves the tooth socket.",
    "competing dental lesion")],
  c(67)),
]

# Arcade cards come from tools/micro_e2/l13_cards.json (atomic facts from the keys above).
if __name__ == "__main__":
    from collections import Counter
    print(len(POOL), Counter(q["topic"] for q in POOL))
    print(Counter(q["io"][0] for q in POOL))
