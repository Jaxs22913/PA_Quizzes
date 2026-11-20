# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 18 — DNA Viruses of Medical Importance (Dr. Webster, 13 November 2026), pool B: the
# POXVIRUSES, deck slides 31-54 — classification and structure (31-33), variola and smallpox (34-42, 45),
# smallpox prevention and the Strategic National Stockpile (42-44), molluscum contagiosum (46), mpox (47-49, 52),
# cowpox (53) and orf virus (54); plus the chart rows on slide 4 (Variola, Molluscum contagiosum, Monkeypox,
# Vaccinia | Cowpox).
#
# PHASE 1, FROM THE SLIDES ALONE. Every key and every explanation is from the VISIBLE slides, text and pictures;
# speaker notes are not used. Facts from other slides of the same deck (rubella and cytomegalovirus teratogenic
# and the oncogenic list on 28, the survey of enveloped and nonenveloped groups on 30-31, herpes simplex virus
# type 1 in the trigeminal ganglion and cold sores on 58-60, shingles along a dermatome on 69, hepatitis B
# blood transmission on 87, adenovirus, papillomavirus and parvovirus morphology on 93, 96-97 and 103, Kaposi
# sarcoma on 83) appear only inside explanations, as the replacing fact for a distractor.
#
# Picture-only content used: slide 4 (chart rows: variola transmission "Inhalation, Direct Contact, Fomites",
# "possible toxemia, shock", "No more routine vaccination except for front line"; molluscum "Treatment typically
# by removal of individual lesions", vaccine "No"; monkeypox "Skin pocks, Fever, Swollen lymph nodes"; cowpox
# "Yes-- used in Europe for animals"); slide 33 (the poxvirus virion drawing: envelope, outer membrane, core);
# quiz pictures l18-fig-01 (slide 45, smallpox pustules on a child's arm and hand), l18-fig-02 (slide 46,
# tumor-like facial growths of atypical molluscum), l18-fig-03 (slide 47, mpox pustules over a child's body,
# hands and feet), l18-fig-04 (slide 53, cowpox lesions on an arm and trunk), l18-fig-05 (slide 54, orf ulcer on
# the back of a hand).
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the only
# "Correct." opener; the partition rotates positions per set. `mis` names the misconception each distractor stands
# for (review metadata; the renderer strips it).
#
# DELIBERATELY NOT ASKED (held), and why:
#   - WHICH DRUG treats smallpox (slide 42: tecovirimat, cidofovir, brincidofovir): she does not test specific
#     treatments. The Strategic National Stockpile is asked only as "holds vaccines and treatments".
#   - dates, years and historical persons (slides 34-38, 43-45, 47, 49-51): variolation is asked only as the
#     concept, and why vaccination replaced it; the vaccine's ending and reintroduction years are never used.
#   - numbers: incubation 7-10 days (40), "good for about 3 years" (43), the mpox 2-4 week illness (48), the
#     JYNNEOS 28-day interval and dose count (52), every case and death count (47, 50-51), the 24-hour body
#     coverage (41). None is a key.
#   - molluscum "In U.S., most commonly an STD" (46) and genital warts "most common STD" (97): never keyed.
#   - mpox spread "within the defined subpopulation" of men who have sex with men (52): not asked.
#   - JYNNEOS date conflict (chart slide 4 "became available April 2024" against slide 44 "approved Septembe 24,
#     2019"): no dates asked; JYNNEOS is already covered by another quiz and is used only as a distractor.
# CONFLICTS FOUND (not tested):
#   - chart slide 4 puts "Vaccinia" in the Virus column of the Cowpox row, while slides 43-44 make vaccinia the
#     smallpox vaccine virus and slide 53 names the virus cowpox. Vaccinia is keyed only as the smallpox vaccine,
#     and cowpox never appears as an option beside a vaccinia key (or the reverse).
#   - slide 46 calls molluscum lesions "macules" though the pictures show raised bumps; the word is used only as
#     the deck's own phrase "small, smooth, waxy" lesions.
# SPELLING: the chart's "contagiousum" is written contagiosum; "Septembe" September; "Jynneos" JYNNEOS; "M pox"
# mpox (the deck also says monkeypox; mpox is used in stems, the virus is "monkeypox virus" only where the deck
# names the virus).
from micro_l18_common import *

POX = "Poxviruses"
VAR = "Variola and smallpox"
PREV = "Smallpox prevention"
MOL = "Molluscum contagiosum"
MPX = "Mpox"
COW = "Cowpox"
ORF = "Orf virus"

POOL_B = [

# ============================================================== POXVIRUSES (slides 31-33)
Q(POX, IO4,
  "How are poxviruses classified by their envelope and their genome?",
  ("With envelope; double-stranded genome",
   "Correct. Poxviruses are listed among the enveloped deoxyribonucleic acid viruses, with the herpesviruses and hepadnaviruses, and "
   "their genome is double-stranded deoxyribonucleic acid. The drawing of the virion shows the envelope around an "
   "outer membrane and a core that holds the genome."),
  [("Without envelope; double-stranded genome",
    "Nonenveloped double-stranded viruses are the adenoviruses and the papilloma and polyoma viruses, not the "
    "poxviruses. Poxviruses carry an envelope over their outer membrane, so they sit with the herpesviruses and "
    "hepadnaviruses in the enveloped group.",
    "adenovirus and papillomavirus morphology"),
   ("Without envelope; single-stranded genome",
    "Nonenveloped single-stranded deoxyribonucleic acid is the parvovirus pattern, small in diameter and genome "
    "size. Poxviruses are the opposite on both counts: enveloped, and the largest genome of all viruses, made of "
    "double-stranded deoxyribonucleic acid.",
    "parvovirus morphology"),
   ("With envelope; partly single-stranded genome",
    "A genome that is partly double- and partly single-stranded is the unusual genome of hepatitis B virus, a "
    "hepadnavirus. Poxviruses share the envelope with it, but their genome is fully double-stranded "
    "deoxyribonucleic acid, the largest of all viruses.",
    "hepadnavirus genome borrowed")],
  ci(33, 30, 31, 32, 86, 93, 96, 103)),

Q(POX, IO4,
  "Poxviruses show specificity for the cytoplasm of which cells, which leads to their pustules?",
  ("Epidermal cells",
   "Correct. Poxviruses have a specificity for the cytoplasm of epidermal cells and subcutaneous connective "
   "tissue. That is what produces their eruptive skin pustules, the pocks or pox that leave scars, and it can also "
   "stimulate tumor formation."),
  [("Trigeminal ganglion cells",
    "The trigeminal ganglion is where herpes simplex virus type 1 lies latent after entering the fifth cranial "
    "nerve, not a target of poxviruses. Poxviruses home to the cytoplasm of epidermal cells and subcutaneous "
    "connective tissue, which is why they make skin pustules.",
    "herpes simplex latency site"),
   ("B lymphocytes",
    "B cells are where Epstein-Barr virus stays dormant, and Burkitt lymphoma is a B-cell malignancy linked to it. "
    "Poxviruses instead have specificity for the cytoplasm of epidermal cells and subcutaneous connective tissue, "
    "giving pocks on the skin.",
    "Epstein-Barr virus target"),
   ("Liver cells",
    "Liver cells are the target of hepatitis B virus, which raises the risk of hepatocellular carcinoma. "
    "Poxviruses are skin viruses: their specificity for the cytoplasm of epidermal cells and subcutaneous "
    "connective tissue produces the eruptive pustules called pocks.",
    "hepatitis B target")],
  c(32, 75, 77, 59, 87)),

Q(POX, IO3,
  "Besides eruptive skin pustules, what else can the poxviruses' specificity for epidermal cells and "
  "subcutaneous connective tissue stimulate?",
  ("Tumor formation",
   "Correct. The specificity of poxviruses for the cytoplasm of epidermal cells and subcutaneous connective "
   "tissue leads to the pustules, or it can stimulate tumor formation. The atypical molluscum contagiosum seen in "
   "acquired immunodeficiency syndrome, with tumor-like growths on the face, is an example."),
  [("Fetal birth defects",
    "Crossing the placenta to cause developmental disturbances and permanent defects is what teratogenic viruses "
    "do, such as rubella and cytomegalovirus. The poxviruses' specificity for epidermal cells and subcutaneous "
    "connective tissue instead gives pustules or tumor formation.",
    "teratogenic effect"),
   ("Myelin destruction",
    "Destruction of the cells that make myelin is the hallmark of progressive multifocal leukoencephalopathy from "
    "JC polyomavirus. Poxviruses act on the skin: their tissue specificity gives pustules or can stimulate tumor "
    "formation.",
    "JC polyomavirus effect"),
   ("Dermatomal vesicles",
    "Vesicles along a dermatome are shingles, the reactivation of latent varicella zoster virus along a nerve "
    "pathway. Poxviruses cause scarring pustules, the pocks, and their specificity for epidermal cells and "
    "subcutaneous connective tissue can also stimulate tumor formation.",
    "shingles pattern")],
  c(32, 46, 28, 69, 102)),

# ============================================================== VARIOLA AND SMALLPOX (slides 4, 34-42, 45)
Q(VAR, IO5,
  "Why did smallpox tend to be present in densely populated areas?",
  ("It requires a human host",
   "Correct. Variola virus requires a human host, so smallpox persisted where people were crowded together, in "
   "densely populated areas, with epidemics recurring at regular intervals. It spreads from person to person by "
   "inhaled airborne saliva, direct contact and fomites."),
  [("Rodents are its main reservoir",
    "Rodents seem to be the primary reservoir of cowpox, which reaches people through cats that interact with "
    "rodents. Variola has no animal reservoir: it requires a human host, which is why smallpox clustered in "
    "densely populated areas.",
    "cowpox reservoir borrowed"),
   ("It spreads by handling sheep",
    "Handling sheep and goats, by feeding, shearing or bites, is how people catch orf virus, a parapox virus of "
    "ruminant animals. Smallpox needs a human host and spreads from person to person, so crowded populations "
    "sustained it.",
    "orf transmission borrowed"),
   ("Pet prairie dogs carry it",
    "Pet prairie dogs carried mpox in a United States outbreak, after picking it up from rodents imported from "
    "Africa. Variola has no animal host at all; it requires humans, so it lingered in densely populated areas.",
    "mpox outbreak borrowed")],
  c(34, 40, 49, 53, 54)),

Q(VAR, IO4,
  "Before a cure existed, which method of preventing smallpox did most medical traditions rely on?",
  ("Quarantine",
   "Correct. Most medical traditions focused on prevention rather than a cure for smallpox, and quarantine was a "
   "prevalent method. Because variola needs a human host and spreads person to person, separating the sick from "
   "others cut its spread."),
  [("Lesion removal",
    "Removing individual lesions, by freezing, electric cautery or chemical agents, is the typical treatment of "
    "molluscum contagiosum, not a way to prevent smallpox. For smallpox, traditions focused on prevention, with "
    "quarantine a prevalent method.",
    "molluscum treatment borrowed"),
   ("Electric cautery",
    "Electric cautery is one way to remove molluscum contagiosum lesions, along with freezing and chemical "
    "agents. It treats existing lesions and does not prevent a person-to-person disease; smallpox prevention "
    "relied on quarantine.",
    "molluscum treatment borrowed"),
   ("Animal vaccination",
    "A vaccine for animals only, used in Europe for circus and zoo animals, belongs to cowpox. Smallpox has no "
    "animal host, so vaccinating animals could not prevent it; most traditions relied on quarantine of the sick.",
    "cowpox animal vaccine borrowed")],
  c(34, 46, 53) + " and image on Slide 4"),

Q(VAR, IO4,
  "What was variolation?",
  ("Deliberate infection with smallpox",
   "Correct. Variolation was the deliberate introduction of smallpox material as a preventive measure, for "
   "example by blowing powdered smallpox material up the nose (nasal insufflation). It did not always protect, "
   "and the smallpox cases it seeded led to its replacement by vaccination."),
  [("Vaccination with vaccinia virus",
    "Vaccination with vaccinia virus is the method that replaced variolation, being less harmful; vaccinia is a "
    "live virus vaccine. Variolation used smallpox material itself, deliberately introduced as a preventive "
    "measure.",
    "vaccination confused with variolation"),
   ("Isolation of smallpox patients",
    "Isolating the sick is quarantine, the prevalent preventive method in most medical traditions. Variolation was "
    "different: it deliberately introduced smallpox material into a healthy person, for example by nasal "
    "insufflation.",
    "quarantine confused with variolation"),
   ("Stockpiling of smallpox vaccine",
    "Keeping smallpox vaccines and treatments in reserve is the job of the Strategic National Stockpile, prepared "
    "for a public health emergency such as bioterrorism. Variolation was the deliberate introduction of smallpox "
    "material to prevent the disease.",
    "stockpile confused with variolation")],
  c(35, 34, 38, 43, 42)),

Q(VAR, IO4,
  "Why was variolation replaced by vaccination?",
  ("It seeded new smallpox cases",
   "Correct. Variolation did not always work and sometimes failed to protect during an epidemic, and the "
   "collateral smallpox cases spread by variolated people began to outweigh its benefits. Vaccination was less "
   "harmful, and variolation was made illegal in some countries."),
  [("It caused facial tumor growths",
    "Tumor-like growths on the face are the atypical form of molluscum contagiosum in acquired immunodeficiency "
    "syndrome. The problem with variolation was that variolated people spread collateral cases of smallpox.",
    "molluscum complication borrowed"),
   ("It infected pet prairie dogs",
    "Prairie dogs were infected with mpox from African rodents housed in the same animal vendor facility, not by "
    "variolation. Variolation was abandoned because the smallpox cases spread by variolated people outweighed the "
    "benefits.",
    "mpox outbreak borrowed"),
   ("It ended herd immunity to pox",
    "Loss of herd immunity is linked to the end of smallpox vaccination and is thought to explain re-emerging "
    "cowpox cases. Variolation gave way to vaccination because variolated people spread collateral smallpox "
    "cases.",
    "cowpox re-emergence borrowed")],
  c(38, 46, 49, 53)),

Q(VAR, IO5,
  "Which is a route by which smallpox spreads?",
  ("Inhaled airborne saliva",
   "Correct. Smallpox spreads from person to person by inhalation of airborne saliva, by contact with material "
   "from pustules or scabs, and by fomites contaminated with that material. Variola requires a human host, so "
   "animals play no part."),
  [("Shearing infected sheep",
    "Shearing, feeding and bites from sheep and goats pass orf virus, a parapox virus, to people who handle the "
    "animals. Variola has no animal host; smallpox passes from person to person, by inhaled saliva, contact with "
    "pustule material, or fomites.",
    "orf transmission borrowed"),
   ("A rodent-hunting pet cat",
    "Handling a cat that interacted with rodents is how people catch cowpox, usually on the hands. Smallpox needs "
    "a human host and spreads person to person through airborne saliva, contact with pustules or scabs, and "
    "fomites.",
    "cowpox transmission borrowed"),
   ("Contact with prairie dogs",
    "Contact with infected pet prairie dogs spread mpox in a United States outbreak. Smallpox has no animal source: "
    "it requires a human host and spreads by inhaled airborne saliva and contact with pustule material or "
    "fomites.",
    "mpox transmission borrowed")],
  c(40, 34, 49, 53, 54) + " and image on Slide 4"),

Q(VAR, IO5,
  "In smallpox, the skin rash starts on the face. Where does it spread next?",
  ("To the arms and legs",
   "Correct. The smallpox rash starts on the face, spreads to the arms and legs, and then to the hands and feet, "
   "covering the whole body quickly. After full coverage the fever declines, and by the fourth day the sores "
   "fill with fluid."),
  [("To the hands and feet",
    "The hands and feet are the last stop, reached after the arms and legs. The order is face, then arms and "
    "legs, then hands and feet; the rash does not skip from the face straight to the extremities.",
    "order of spread skipped"),
   ("To the genitals and thighs",
    "The genital area and thighs are where molluscum contagiosum places its small, smooth, waxy lesions. The "
    "smallpox rash moves from the face to the arms and legs, then the hands and feet.",
    "molluscum distribution borrowed"),
   ("Along a single dermatome",
    "A band of vesicles along one dermatome is shingles, the reactivation of varicella zoster virus along a "
    "nerve pathway. Smallpox covers the whole body, spreading from the face to the arms and legs, then the hands "
    "and feet.",
    "shingles distribution borrowed")],
  c(41, 46, 69)),

Q(VAR, IO5,
  "In smallpox, once the skin sores fill with fluid around the fourth day, what may the fever do?",
  ("Rise again until scabs form",
   "Correct. The fever declines once the rash has covered the body, but by the fourth day, as the sores fill with "
   "fluid, it may rise again and remain high until scabs form over the bumps. The patient stays contagious until "
   "all scabs have fallen off."),
  [("Decline for good",
    "The fever declines earlier, once the rash has covered the whole body. By the fourth day, as the sores fill "
    "with fluid, it may rise again and remain high until scabs form, so a falling fever is not the end.",
    "first decline taken as final"),
   ("Begin for the first time",
    "Fever is not new at this stage: high fever is among the first symptoms, with head and body aches and "
    "vomiting, before any rash. Around the fourth day it may rise a second time and stay high until scabs form.",
    "fever onset misplaced"),
   ("Stay high until scabs fall off",
    "The fever stays high only until scabs FORM over the bumps. Scabs falling off marks something else: the point "
    "when the patient is no longer contagious. The fever rises again around the fourth day.",
    "scab formation and scab loss confused")],
  c(40, 41)),

Q(VAR, IO4,
  "Which form of smallpox was highly virulent, causing toxemia, shock and intravascular coagulation?",
  ("Variola major",
   "Correct. Variola major was the highly virulent form of smallpox, causing toxemia, shock and intravascular "
   "coagulation. Variola minor was the less virulent form of the same disease."),
  [("Variola minor",
    "Variola minor was the less virulent form of smallpox. Toxemia, shock and intravascular coagulation mark "
    "variola major, the highly virulent form.",
    "major and minor reversed"),
   ("Monkeypox",
    "Mpox brings fever, aches, chills, swollen lymph nodes, exhaustion and a rash that moves from macules to "
    "scabs over a 2-4 week illness. Toxemia, shock and intravascular coagulation define variola major, the "
    "virulent smallpox.",
    "mpox confused with severe smallpox"),
   ("Cowpox",
    "Cowpox in humans is rare and usually confined to the hands. Toxemia, shock and intravascular coagulation are "
    "the marks of variola major, the highly virulent form of smallpox.",
    "cowpox confused with severe smallpox")],
  c(42, 48, 53) + " and image on Slide 4"),

Q(VAR, IO5,
  "A child has the raised, fluid-filled pustules shown on the arm and hand. The rash followed a high fever and "
  "spread out from the face, and the virus has no host other than humans. Which disease is this?",
  ("Smallpox",
   "Correct. A virus that requires a human host and a pustular rash that starts on the face and spreads to the "
   "arms and legs, then the hands and feet, after a high fever, is smallpox from variola virus. The pustules "
   "shown on the arm and hand fit the stage when sores fill with fluid."),
  [("Mpox",
    "Mpox also gives fever and a pustular rash beginning on the face, but it is not limited to humans: it comes "
    "from rodents and spread to people through infected prairie dogs. A virus with only a human host is variola.",
    "mpox look-alike"),
   ("Cowpox",
    "Cowpox has rodents as its primary reservoir and is also found in cats, cows and zoo animals; human infections "
    "are rare and usually confined to the hands. A whole-body rash from a human-only virus is smallpox.",
    "cowpox look-alike"),
   ("Molluscum contagiosum",
    "Molluscum contagiosum gives small, smooth, waxy lesions in the genital area and thighs, normally "
    "self-limiting and without the high fever first. Fluid-filled pustules spreading from the face after a high "
    "fever are smallpox.",
    "molluscum look-alike")],
  ci(45, 34, 40, 41, 46, 48, 49, 53),
  img=IMG + "/l18-fig-01.jpg",
  alt="Photograph of a child's forearm and hand covered with many raised, round, fluid-filled pustules, including "
      "on the fingers and palm.",
  slide="Slide 45"),

# ============================================================== SMALLPOX PREVENTION (slides 4, 42-44)
Q(PREV, IO5,
  "What kind of vaccine is used to prevent smallpox?",
  ("Live vaccinia virus",
   "Correct. Smallpox is prevented by vaccination with vaccinia virus, a live virus vaccine. ACAM2000, one of the "
   "vaccines in the Strategic National Stockpile, is a live vaccinia virus vaccine."),
  [("Live variola virus",
    "Deliberately introducing live smallpox material was variolation, which was replaced because variolated "
    "people spread collateral smallpox cases. The smallpox vaccine uses a different live virus, vaccinia.",
    "variolation confused with vaccination"),
   ("Killed variola virus",
    "A killed variola vaccine is not among the smallpox vaccines held in the Strategic National Stockpile, which "
    "include ACAM2000, a live vaccinia virus, and JYNNEOS, a live virus. Smallpox is prevented with live vaccinia.",
    "inactivated vaccine assumed"),
   ("Live orf virus",
    "Orf virus is a parapox virus of sheep and goats that people catch by feeding, shearing or being bitten by "
    "the animals; it is not a vaccine. The smallpox vaccine is live vaccinia virus.",
    "orf virus confused with vaccine")],
  c(43, 44, 38, 54)),

Q(PREV, IO5,
  "Smallpox vaccination is no longer routine. Who still receives it?",
  ("Military and medical personnel",
   "Correct. Smallpox vaccination is no longer routinely given, except for the front line: the vaccine was "
   "reintroduced for military and medical personnel. Everyone else is unvaccinated, which is why smallpox is a "
   "potential bioterrorism weapon."),
  [("All children entering school",
    "Children are not routinely vaccinated against smallpox; routine vaccination ended, leaving the general "
    "population unvaccinated. Only front-line groups, military and medical personnel, receive the vaccine.",
    "routine vaccination assumed"),
   ("Travelers to the Pacific islands",
    "The Pacific islands are an endemic area for molluscum contagiosum, where it is mainly an infection of "
    "children, and molluscum has no vaccine. Smallpox vaccine now goes only to military and medical personnel.",
    "molluscum geography borrowed"),
   ("People who shear sheep and goats",
    "Shearing sheep and goats is a way to catch orf virus, a parapox virus of ruminants. Smallpox vaccination is "
    "no longer routine and is kept for front-line military and medical personnel.",
    "orf exposure borrowed")],
  c(43, 46, 54) + " and image on Slide 4"),

Q(PREV, IO4,
  "Why is smallpox considered a potential weapon for bioterrorism?",
  ("Routine vaccination has ended",
   "Correct. Smallpox is a potential weapon because people are no longer routinely vaccinated, leaving most of the "
   "population unprotected. For that reason vaccines and treatments are kept in the Strategic National Stockpile "
   "for a public health emergency."),
  [("Rodents carry it worldwide",
    "Rodents are the primary reservoir of cowpox, not of smallpox. Variola requires a human host; its danger as a "
    "weapon comes from the end of routine vaccination, which leaves people unprotected.",
    "cowpox reservoir borrowed"),
   ("No vaccine against it exists",
    "Molluscum contagiosum is the poxvirus with no vaccine. Smallpox has vaccines, including live vaccinia "
    "vaccines held in the Strategic National Stockpile; the risk is that people are no longer routinely "
    "vaccinated.",
    "molluscum vaccine status borrowed"),
   ("It spreads after scabs fall off",
    "This reverses the contagious period: once all scabs have fallen off, a smallpox patient is no longer "
    "contagious. Smallpox is a bioterrorism risk because routine vaccination ended.",
    "contagious period reversed")],
  c(43, 41, 44, 53) + " and image on Slide 4"),

Q(PREV, IO4,
  "Where are smallpox vaccines and treatments kept in case of a public health emergency?",
  ("The Strategic National Stockpile",
   "Correct. Smallpox vaccines and treatments are kept in the Strategic National Stockpile, a store of medical "
   "supplies for a public health emergency. It holds three smallpox vaccines, including ACAM2000 and JYNNEOS, "
   "because smallpox is a potential bioterrorism weapon."),
  [("The two smallpox research labs",
    "Only two laboratories work with smallpox itself, one in Atlanta and one in Russia. The vaccines and "
    "treatments kept ready for an emergency sit in the Strategic National Stockpile, not in those labs.",
    "research labs confused with stockpile"),
   ("Animal vendor facilities",
    "An animal vendor facility was where prairie dogs caught mpox from African rodents. Smallpox vaccines and "
    "treatments for a public health emergency are kept in the Strategic National Stockpile.",
    "mpox outbreak borrowed"),
   ("Routine childhood clinics",
    "Smallpox vaccine is no longer routinely given, so childhood clinics do not hold it. Vaccines and treatments "
    "for an emergency are kept in the Strategic National Stockpile.",
    "routine vaccination assumed")],
  c(42, 43, 44, 49)),

# ============================================================== MOLLUSCUM CONTAGIOSUM (slides 4, 46)
Q(MOL, IO5,
  "In endemic areas such as the Pacific islands, molluscum contagiosum is primarily an infection of which group?",
  ("Children",
   "Correct. In endemic areas such as the Pacific islands, molluscum contagiosum is primarily an infection of "
   "children. It spreads by direct contact and fomites and gives small, smooth, waxy lesions that are normally "
   "self-limiting."),
  [("Older adults",
    "Older adults are not the group named for endemic molluscum contagiosum. In endemic areas such as the Pacific "
    "islands it is primarily an infection of children, spread by direct contact and fomites.",
    "wrong age group"),
   ("Military recruits",
    "Military personnel are the group still given smallpox vaccine now that routine vaccination has ended. "
    "Endemic molluscum contagiosum, in places such as the Pacific islands, is primarily an infection of children.",
    "smallpox vaccine group borrowed"),
   ("Sheep farmers",
    "People who feed, shear or are bitten by sheep and goats catch orf virus, a parapox virus. Molluscum "
    "contagiosum in endemic areas such as the Pacific islands is primarily an infection of children.",
    "orf exposure borrowed")],
  c(46, 43, 54)),

Q(MOL, IO4,
  "Which skin condition may be a risk factor for molluscum contagiosum, through breaks in the skin?",
  ("Atopic dermatitis",
   "Correct. Atopic dermatitis may be a risk factor for molluscum contagiosum because of the breaks it leaves in "
   "the skin. The virus spreads by direct contact and fomites and causes small, smooth, waxy lesions in the "
   "genital area and on the thighs."),
  [("Plantar warts",
    "Plantar warts are deep, painful warts on the soles of the feet caused by human papillomavirus; they are a "
    "disease of their own, not a risk factor named for molluscum. The risk factor is atopic dermatitis, through "
    "breaks in the skin.",
    "papillomavirus disease confused"),
   ("Cold sores",
    "Cold sores, or fever blisters, are lesions of herpes simplex virus type 1 near the lips, not a risk factor "
    "for molluscum contagiosum. The condition that may raise the risk, through breaks in the skin, is atopic "
    "dermatitis.",
    "herpes simplex disease confused"),
   ("Shingles",
    "Shingles is reactivated varicella zoster virus with vesicles along a dermatome; it is a disease, not a risk "
    "factor named for molluscum contagiosum. Atopic dermatitis, by breaking the skin, may be the risk factor.",
    "varicella zoster disease confused")],
  c(46, 58, 69, 97)),

Q(MOL, IO4,
  "The tumor-like facial growths shown are an atypical form of molluscum contagiosum. In which patients does "
  "this form occur?",
  ("Patients with acquired immunodeficiency syndrome",
   "Correct. Patients with acquired immunodeficiency syndrome suffer an atypical form of molluscum contagiosum "
   "that attacks the skin of the face and forms tumor-like growths, as the many raised growths over the jaw and "
   "cheek in the picture show. In others the lesions are small, waxy and self-limiting."),
  [("Children in endemic areas such as the Pacific islands",
    "Children in endemic areas such as the Pacific islands are the main group infected there, but they have the "
    "usual small, smooth, waxy, self-limiting lesions. The tumor-like facial form occurs in acquired "
    "immunodeficiency syndrome.",
    "endemic group confused with atypical form"),
   ("Patients whose atopic dermatitis breaks the skin",
    "Atopic dermatitis may be a risk factor for catching molluscum contagiosum, through breaks in the skin, but "
    "it is not tied to the atypical form. Tumor-like facial growths are the form seen in acquired "
    "immunodeficiency syndrome.",
    "risk factor confused with atypical form"),
   ("People who feed and shear sheep and goats",
    "Handling sheep and goats spreads orf virus, which is more serious in the immunocompromised. The atypical "
    "molluscum contagiosum with tumor-like facial growths is the form seen in acquired immunodeficiency syndrome.",
    "orf exposure borrowed")],
  ci(46, 54),
  img=IMG + "/l18-fig-02.jpg",
  alt="Close photograph of the lower face and jaw of an adult, covered with many clustered, raised, rounded "
      "skin-colored growths of varying size.",
  slide="Slide 46"),

Q(MOL, IO4,
  "How is molluscum contagiosum typically treated?",
  ("Removal of individual lesions",
   "Correct. Molluscum contagiosum is typically treated by removing individual lesions, by freezing, electric "
   "cautery or chemical agents. No vaccine is available, and the lesions are normally self-limiting."),
  [("A two-dose vaccine series",
    "A two-dose vaccine series is JYNNEOS, used to prevent mpox. Molluscum contagiosum has no vaccine; it is "
    "treated by removing individual lesions with freezing, electric cautery or chemical agents.",
    "mpox vaccine borrowed"),
   ("Quarantine until scabs fall",
    "Staying contagious until all scabs have fallen off describes smallpox, and quarantine was the old way to "
    "prevent it. Molluscum contagiosum is treated by removing individual lesions.",
    "smallpox measure borrowed"),
   ("Live vaccinia vaccination",
    "Live vaccinia virus is the smallpox vaccine, kept for military and medical personnel. No vaccine is available "
    "for molluscum contagiosum; its lesions are removed one by one with freezing, cautery or chemicals.",
    "smallpox vaccine borrowed")],
  c(46, 41, 43, 52) + " and image on Slide 4"),

# ============================================================== MPOX (slides 4, 47-49, 52)
Q(MPX, IO5,
  "A United States mpox outbreak was traced to an animal vendor facility that also housed rodents from Africa. "
  "Which pet animals carried the virus to people?",
  ("Prairie dogs",
   "Correct. The outbreak was traced to prairie dogs housed in an animal vendor facility with rodents from "
   "Africa (African giant pouched rats, dormice and rope squirrels), which passed the virus to them. The virus was "
   "recovered from a patient and the patient's pet prairie dog, and African rodents may no longer be imported."),
  [("House cats",
    "Cats that interact with rodents pass cowpox, not mpox, to the people who handle them. In the mpox outbreak "
    "the pets were prairie dogs infected by African rodents in a vendor facility.",
    "cowpox carrier borrowed"),
   ("Pet rabbits",
    "Rabbits host their own poxvirus, rabbitpox, but humans are named as susceptible only to cowpox and "
    "monkeypox. The pets that spread mpox in the outbreak were prairie dogs.",
    "rabbitpox confused"),
   ("Pet goats",
    "Goats and sheep spread orf virus, a parapox virus, to people who feed, shear or are bitten by them. The pets "
    "behind the mpox outbreak were prairie dogs infected by African rodents.",
    "orf carrier borrowed")],
  c(49, 47, 53, 54)),

Q(MPX, IO5,
  "Mpox virus enters the body through broken skin, mucous membranes, or which other route?",
  ("The respiratory tract",
   "Correct. Mpox virus enters through broken skin, the respiratory tract or mucous membranes, by contact with "
   "infected animals or humans, their body fluids, or fomites. Fever, aches, chills, swollen lymph nodes and "
   "exhaustion follow, then the rash."),
  [("Intact skin",
    "The skin route needs a break: mpox virus enters through BROKEN skin, along with the respiratory tract and "
    "mucous membranes. Intact skin is not listed as a way in.",
    "broken skin requirement missed"),
   ("The placenta",
    "Crossing the placenta to cause developmental defects is the route of teratogenic viruses such as rubella "
    "and cytomegalovirus. Mpox virus enters through broken skin, mucous membranes and the respiratory tract.",
    "teratogenic route borrowed"),
   ("The fifth cranial nerve",
    "Herpes simplex virus type 1 enters the fifth cranial nerve and lies latent in the trigeminal ganglion. Mpox "
    "virus gets into the body through broken skin, mucous membranes and the respiratory tract.",
    "herpes simplex path borrowed")],
  c(48, 28, 59) + " and image on Slide 4"),

Q(MPX, IO5,
  "Through which sequence of stages does the mpox rash pass?",
  ("Macules, papules, vesicles, pustules, scabs",
   "Correct. The mpox rash, often beginning on the face and spreading, goes through macules, then papules, then "
   "vesicles, then pustules, then scabs. It appears 1-3 days after the fever, in an illness lasting a few weeks."),
  [("Papules, macules, vesicles, pustules, scabs",
    "This swaps the first two stages. The mpox rash starts flat, as macules, and only then rises into papules, "
    "before vesicles, pustules and scabs.",
    "first stages swapped"),
   ("Macules, papules, pustules, vesicles, scabs",
    "This puts pustules before vesicles. In the mpox rash the clear vesicles come first and then become pustules, "
    "which finally scab: macules, papules, vesicles, pustules, scabs.",
    "vesicle and pustule swapped"),
   ("Vesicles, macules, papules, pustules, scabs",
    "Vesicles are not the starting point. The mpox rash begins as macules, rises to papules, then forms vesicles, "
    "then pustules, and ends as scabs.",
    "vesicles placed first")],
  c(48)),

Q(MPX, IO5,
  "A child has the pustular rash shown over the trunk, back, hands and feet, after fever, chills and swollen lymph "
  "nodes. The infection came from contact with an infected animal. Which virus is the cause?",
  ("Monkeypox virus",
   "Correct. Fever, chills and swollen lymph nodes, then a pustular rash spreading over the body, after contact "
   "with an infected animal, point to monkeypox virus (mpox). Humans are susceptible to it and to cowpox among the "
   "animal poxviruses, and mpox gives skin pocks, fever and swollen lymph nodes."),
  [("Variola virus",
    "Variola gives a similar pustular rash, but it requires a human host and has no animal source. An infection "
    "caught from an infected animal, with swollen lymph nodes, is mpox.",
    "smallpox look-alike"),
   ("Cowpox virus",
    "Cowpox also comes from animals, but human infections are rare and usually confined to the hands. A rash over "
    "the trunk, back, hands and feet with swollen lymph nodes fits mpox.",
    "cowpox look-alike"),
   ("Molluscum contagiosum virus",
    "Molluscum contagiosum spreads from person to person by direct contact and fomites and gives small, "
    "smooth, waxy lesions in the genital area and thighs. A febrile pustular rash from an animal is mpox.",
    "molluscum look-alike")],
  ci(47, 34, 46, 48, 53) + " and image on Slide 4",
  img=IMG + "/l18-fig-03.jpg",
  alt="Four photographs of a child: the front of the trunk and arms, the back, the legs and feet, and the palms, "
      "all covered with many small raised pustules.",
  slide="Slide 47"),

# ============================================================== COWPOX (slides 4, 53)
Q(COW, IO5,
  "What seems to be the primary reservoir of cowpox infection?",
  ("Rodents",
   "Correct. Despite its name, cowpox is found not only in cows but in rodents, cats and zoo animals, and rodents "
   "seem to be its primary reservoir. Humans can catch it from rodents by handling cats that interacted with "
   "them."),
  [("Cows",
    "Cows gave the disease its name, but cowpox is found in rodents, cats and zoo animals too, and rodents seem to "
    "be the primary reservoir. The name is a trap, not the reservoir.",
    "name taken as reservoir"),
   ("Humans",
    "Humans are the only host of variola, the smallpox virus. Human cowpox infections are rare and come from "
    "animals; the primary reservoir appears to be rodents.",
    "smallpox host borrowed"),
   ("Sheep and goats",
    "Sheep and goats are the ruminant hosts of orf virus, a parapox virus that causes sore mouth. Cowpox's primary "
    "reservoir appears to be rodents.",
    "orf host borrowed")],
  c(53, 34, 54)),

Q(COW, IO4,
  "Why are human cowpox cases thought to be re-emerging worldwide?",
  ("Loss of herd immunity from smallpox vaccination",
   "Correct. Cowpox cases are re-emerging worldwide, thought perhaps to be related to the loss of herd immunity "
   "that smallpox vaccination once gave. With routine smallpox vaccination over, fewer people are protected "
   "against this related poxvirus."),
  [("Importation of rodents from Africa",
    "Rodents imported from Africa infected prairie dogs in a United States mpox outbreak, and their import is no "
    "longer permitted. Re-emerging cowpox is linked to the loss of herd immunity from smallpox vaccination.",
    "mpox outbreak borrowed"),
   ("Spread from person to person by airborne saliva",
    "Spread by inhaled airborne saliva describes smallpox. Cowpox is caught from animals, rarely from humans, and "
    "its re-emergence is thought to reflect lost herd immunity from smallpox vaccination.",
    "smallpox transmission borrowed"),
   ("Failure of the human cowpox vaccine",
    "There is no human cowpox vaccine: the only one is for animals, used in Europe for circus and zoo animals. "
    "The re-emergence is put down to the loss of herd immunity from smallpox vaccination.",
    "animal vaccine misread")],
  c(53, 40, 43, 49) + " and image on Slide 4"),

Q(COW, IO5,
  "Lesions like those shown come from a poxvirus whose human infections are rare and usually confined to the "
  "hands, with rodents as its primary reservoir. What vaccine is available against it?",
  ("A vaccine for animals only",
   "Correct. Rare human infections usually confined to the hands, with rodents as the primary reservoir, describe "
   "cowpox, seen here as red, inflamed lesions with dark crusted centers. Its only vaccine is for animals, used in "
   "Europe for circus and zoo animals."),
  [("JYNNEOS, for humans",
    "JYNNEOS is the vaccine available to prevent mpox and smallpox. The poxvirus described, usually on the hands "
    "with a rodent reservoir, is cowpox, whose only vaccine is for animals.",
    "mpox vaccine borrowed"),
   ("No vaccine of any kind",
    "Having no vaccine at all is molluscum contagiosum's status. Cowpox does have a vaccine, but only for "
    "animals, used in Europe for circus and zoo animals.",
    "molluscum vaccine status borrowed"),
   ("A routine childhood vaccine",
    "Smallpox vaccination is no longer routinely given; it ended in 1972. For cowpox, the only vaccine is for"
    " animals, used in Europe for circus and zoo animals.",
    "routine vaccination assumed")],
  ci(53, 43, 46, 52) + " and image on Slide 4",
  img=IMG + "/l18-fig-04.jpg",
  alt="Two photographs labeled A and B: A, an arm with a reddened, inflamed area around a small dark crusted "
      "spot; B, a trunk with several scattered pink-purple marks and a small dark crusted spot.",
  slide="Slide 53"),

# ============================================================== ORF VIRUS (slide 54)
Q(ORF, IO5,
  "How do humans usually catch orf virus?",
  ("Handling sheep and goats",
   "Correct. Orf virus is a parapox virus mainly of ruminant animals, sheep and goats, in which it causes sores on "
   "the mouth. People catch it by handling the animals: feeding, shearing and bites. It is more serious in the "
   "immunocompromised."),
  [("Handling rodent-hunting cats",
    "Handling cats that interacted with rodents is how people catch cowpox. Orf virus comes from ruminants, "
    "sheep and goats, through feeding, shearing and bites.",
    "cowpox transmission borrowed"),
   ("Inhaling airborne saliva",
    "Inhaled airborne saliva spreads smallpox from person to person. Orf virus is caught from sheep and goats by "
    "people who feed, shear or are bitten by them.",
    "smallpox transmission borrowed"),
   ("Keeping pet prairie dogs",
    "Pet prairie dogs carried mpox to people in a United States outbreak. Orf virus is a parapox virus of sheep "
    "and goats, passed to people who feed, shear or are bitten by the animals.",
    "mpox transmission borrowed")],
  c(54, 40, 49, 53)),

Q(ORF, IO4,
  "A farmer has the ulcerated lesion shown on the back of the hand after feeding and shearing his sheep. In the "
  "animals, what is this virus's disease called?",
  ("Contagious ecthyma",
   "Correct. A hand lesion after feeding and shearing sheep is orf, a parapox virus of sheep and goats. In the "
   "animals it causes sores on the mouth, called sore mouth, scabby mouth or contagious ecthyma. It is more "
   "serious in the immunocompromised."),
  [("Molluscum contagiosum",
    "Molluscum contagiosum is a human poxvirus disease spread by direct contact and fomites, with small, smooth, "
    "waxy lesions; it is not a disease of sheep. Orf virus in sheep and goats causes contagious ecthyma, also "
    "called sore mouth or scabby mouth.",
    "human poxvirus disease confused with orf"),
   ("Variola minor",
    "Variola minor is the less virulent form of smallpox, a virus that requires a human host and has no animal "
    "form. The sheep and goat disease spread by feeding and shearing is orf, called contagious ecthyma in the "
    "animals.",
    "smallpox form confused with orf"),
   ("Rabbitpox",
    "Rabbitpox is the poxvirus of rabbits, one of many mammalian poxviruses. The sheep and goat disease spread by "
    "feeding and shearing is orf, called sore mouth, scabby mouth or contagious ecthyma in the animals.",
    "rabbitpox confused with orf")],
  ci(54, 34, 42, 46, 47),
  img=IMG + "/l18-fig-05.jpg",
  alt="Photograph of the back of an adult's hand near a wristwatch, with a large, raised, ulcerated, yellow-crusted "
      "sore on reddened, swollen skin.",
  slide="Slide 54"),
]

CLUSTERS_B = [
    # the human-only host: the reason for crowding, the transmission item and the picture item share the fact
    (1, ["Why did smallpox tend to be present", "A child has the raised, fluid-filled pustules"]),
    # variolation defined and why it was replaced: the definition item's explanation gives the other's key
    (1, ["What was variolation?", "Why was variolation replaced"]),
    # routine vaccination ended: the bioterrorism key states the fact behind the who-still-gets-it item
    (1, ["Why is smallpox considered a potential weapon", "Smallpox vaccination is no longer routine"]),
    # orf from sheep and goats: the picture stem states the route the other item asks
    (1, ["How do humans usually catch orf virus?", "A farmer has the ulcerated lesion"]),
    # the mpox animal source: prairie dogs and the picture item's "from an infected animal"
    (1, ["A United States mpox outbreak", "A child has the pustular rash shown"]),
    # cowpox rodent reservoir stated in the picture stem
    (1, ["What seems to be the primary reservoir of cowpox", "Lesions like those shown come from a poxvirus"]),
]
