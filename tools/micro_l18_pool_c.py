# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 18 — DNA Viruses of Medical Importance (Dr. Webster, 13 November 2026), pool C: the
# HERPESVIRUSES, deck slides 55-84 — the family (55-57: latency and recurrence, episome, few symptoms, worse with
# age / chemotherapy / immunocompromise, opportunists in acquired immunodeficiency syndrome, large enveloped
# icosahedral double-stranded DNA replicating in the nucleus), herpes simplex types 1 and 2 (58-63), herpes of the
# newborn (64-65), herpes simplex diagnosis (66-67), varicella zoster (68-70), cytomegalovirus (71-74), Epstein-Barr
# virus (75-80), human herpesviruses 6 and 7 (81-83) and human herpesvirus 8 (83-84); plus the herpesvirus rows of
# the summary chart pictured on slides 4-6 (cited as image on Slide 4/5/6).
#
# FROM THE SLIDES ALONE: every key and every explanation uses only the VISIBLE slides, text and pictures; speaker
# notes are not used. Picture-only content used: slide 4-6 chart rows (herpes simplex 1 "No, but candidate vaccines
# in trials"; herpes simplex 2 "No, research ongoing"; herpes simplex 1 and 2 row "No"; varicella zoster "Yes,
# vaccines for both chickenpox and shingles"; cytomegalovirus transmission list including tears and blood, "None
# currently available, but several in clinical trials", owl's eye picture; Epstein-Barr "No preventative vaccines
# but several therapeutic vaccines in clinical trials"; human herpesviruses 6 and 7 "Contact with saliva", "Acute
# febrile disease followed by rash", vaccine "None"; human herpesvirus 8 "Saliva, sexual contact, blood
# transfusion, organ transplant", vaccine "None", "May also be related to some forms of Castleman disease and
# primary effusion lymphoma"), slide 56 (virion diagram: glycoprotein spikes, envelope, capsid, DNA core,
# tegument), slide 67 (Pap smear: giant cell with multiple nuclei, inclusion, normal cells), slide 70 (zoster
# activated in the ganglion by stress; viruses migrate down the sensory nerve to the skin), slide 73 (owl's eye
# effect: infected lung cell, nucleus with large inclusion), slide 80 (normal lymphocyte against Epstein-Barr
# lymphocyte). Facts from other slides (poxviruses 32, 46, 53-54; persistent infections 26; hepatitis B 86-91;
# adenovirus 93-94; polyomaviruses 101-102; parvovirus 103-104; papillomavirus 96-99) appear only inside
# explanations, as the replacing fact for a distractor.
#
# Pictures used (8): l18-fig-06 (slide 62), l18-fig-07 (63), l18-fig-08 (65), l18-fig-09 (67), l18-fig-11 (70),
# l18-fig-12 (76), l18-fig-13 (80), l18-fig-14 (84). l18-fig-10 (child with chickenpox, slide 70) not used: the
# chickenpox transmission item reads better without it and the varicella topic already has the shingles picture.
#
# Four options throughout. KEYS SHORT and explanations FULL. Every key is authored at position 0 with the only
# "Correct." opener; one ordered numeric item (QO, the age group of herpes simplex type 2) keeps its ascending order.
#
# AVOIDING THE EXISTING WEBSTER-REVIEW ITEMS: whitlow picture, Burkitt picture, herpes simplex 1 trigeminal latency,
# cytomegalovirus retinitis in acquired immunodeficiency syndrome, roseola picture, herpes simplex 2 lumbosacral,
# shingles along a dermatome, mononucleosis from saliva in a college student, varicella most infectious 24-48 h
# before lesions, shingles giving chickenpox to an unvaccinated child, Kaposi picture -> human herpesvirus 8 and
# human herpesvirus 8 -> Kaposi: none of these stem/key pairs is asked here; the shingles picture asks where the
# virus was latent, the mononucleosis throat picture asks the blood count, the Kaposi picture asks where the tumor
# may spread, Burkitt is asked as its malaria coinfection.
#
# DELIBERATELY NOT ASKED (held), and why:
#   - WHICH DRUG treats what (acyclovir, famciclovir, valacyclovir, interferon, ganciclovir, foscarnet, gamma
#     globulin, monoclonal antibodies): not tested. Non-drug management IS asked (cesarean section if an outbreak
#     at birth; showering after practice; treatment reserved for the immunocompromised appears only in explanations).
#   - numbers: 1-1.5 million cases a year (58), newborn mortality 30% and 50-80% (64: "CNS worst" is asked without
#     numbers), 50% of women / 10% of newborns exposed (72), 90-95% infected by mid-life (75), 30-50 day incubation
#     (75), 95% of the population (81), over 70% of multiple sclerosis patients (81), Burkitt and nasopharyngeal age
#     ranges, 2-3 days to crust (60), "8 infect humans" (57). The only numeric key is herpes simplex 2's age group
#     14-29 (slide 58), as an ascending QO item where each distractor range is another slide's stated group.
#   - chronic fatigue syndrome (78): a "possible link" only; not asked this round.
#   - human herpesvirus 6 and multiple sclerosis (81 "signs of infection", chart "possible connection"): not asked.
#   - human herpesvirus 8 and multiple myeloma / Castleman disease: asked only as "may be involved" (primary
#     effusion lymphoma, on both slide 83 and the chart).
# CONFLICTS FOUND (not tested): Burkitt "African boys 5-7" (chart) against "central African children 5-7" (77) —
#   only "a child in central Africa" is used. Herpes simplex 2's chart cell "Association with Cervical and Penile
#   cancer" against slide 28 (papillomaviruses) — not asked, and papillomavirus is never offered where herpes
#   simplex is the key on a Pap smear. Human herpesviruses 6 and 7 transmission: chart "Contact with saliva",
#   slide 81 "close contact with saliva and other secretions" — consistent, used as saliva only. The chart's
#   herpetic whitlow row says "Pain and swelling on finger or thumb"; slide 60 "usually on one finger" — whitlow
#   not asked here (already in the review set).
# SPELLING: the deck's "leukopakia" is written leukoplakia; "sphenomegaly" splenomegaly; "Cytomegaloviirus"
#   cytomegalovirus; "preventatvie" preventive; "C-section" cesarean section; "Kaposi's" Kaposi.
from micro_l18_common import *

POOL_C = [

# ============================================================== HERPESVIRUS FAMILY (slides 55-57)
Q("Herpesvirus family", IO2,
  "Which feature do all members of the herpesvirus family share?",
  ("Latency with recurrent infection",
   "Correct. Every herpesvirus shows latency and causes recurrent infection: after a lytic cycle the viral "
   "deoxyribonucleic acid (DNA) persists as an episome in the nucleus, dormant and generally undetectable, and it "
   "can reactivate later to cause a new bout of disease."),
  [("A brief, acute lytic course",
    "A brief, rapid lytic course with no persistence describes acute viral agents such as colds and flu. "
    "Herpesviruses also begin with a lytic cycle, but they then stay for life as a latent infection that can "
    "recur, which is the family trait.",
    "acute agent confused with latent"),
   ("Slow, detectable chronic multiplication",
    "Slow multiplication that stays detectable in tissue for years is the persistent chronic infection of human "
    "immunodeficiency virus and hepatitis B virus. Herpesviruses are latent instead: dormant, generally not "
    "detectable, and able to reactivate.",
    "chronic and latent swapped"),
   ("Integration into the host chromosome",
    "Integration into the host chromosome describes a prophage in the lysogenic cycle, and some chronic "
    "infections. Herpesvirus deoxyribonucleic acid (DNA) sits in the nucleus as an episome that is not "
    "integrated, which is how it waits during latency.",
    "episome confused with integration")],
  c(26, 55)),

Q("Herpesvirus family", IO4,
  "Which description fits a herpesvirus virion and its deoxyribonucleic acid genome?",
  ("Enveloped, icosahedral, double-stranded",
   "Correct. Herpesviruses are large, enveloped, icosahedral viruses with double-stranded deoxyribonucleic acid "
   "(DNA). The virion has glycoprotein spikes on its envelope, a tegument layer beneath it, and a capsid holding "
   "the deoxyribonucleic acid core."),
  [("Nonenveloped, single-stranded",
    "A nonenveloped virus with single-stranded deoxyribonucleic acid (DNA) and a small diameter and genome is a "
    "parvovirus, such as B19. Herpesviruses are enveloped and carry double-stranded deoxyribonucleic acid inside an icosahedral "
    "capsid.",
    "parvovirus structure"),
   ("Nonenveloped, circular, double-stranded",
    "Small, nonenveloped viruses with circular double-stranded deoxyribonucleic acid (DNA) are the papilloma and "
    "polyoma viruses. A herpesvirus has an envelope with glycoprotein spikes around its icosahedral capsid; the "
    "envelope is the tell.",
    "papilloma and polyoma structure"),
   ("Enveloped, partly single-stranded",
    "An enveloped virus whose unusual genome holds both double- and single-stranded deoxyribonucleic acid (DNA) "
    "is a hepadnavirus, hepatitis B. Herpesvirus deoxyribonucleic acid is fully double-stranded, inside a large icosahedral capsid "
    "under its envelope.",
    "hepadnavirus genome")],
  c(55, 56, 86, 96, 103)),

Q("Herpesvirus family", IO2,
  "During latency, how does a herpesvirus infection differ from a persistent chronic infection?",
  ("The virus is generally not detectable",
   "Correct. In a latent infection, after a lytic cycle, the herpesvirus enters a dormant phase: it is generally "
   "not detectable and causes no symptoms, yet it can reactivate later. In a chronic infection the virus stays "
   "detectable in tissue samples, multiplying slowly."),
  [("The virus multiplies slowly in tissue",
    "Slow, ongoing multiplication that can be detected in tissue samples is the chronic infection, as with human "
    "immunodeficiency virus and hepatitis B virus. A latent herpesvirus is dormant and generally undetectable "
    "until it reactivates.",
    "chronic and latent swapped"),
   ("The host cell is destroyed quickly",
    "Rapid destruction of the host cell is a lytic cycle, the course of acute agents such as colds and flu. A "
    "latent herpesvirus leaves the cell alive, holding its deoxyribonucleic acid (DNA) as an episome until a "
    "trigger reactivates it.",
    "lytic course confused with latency"),
   ("Its genes replicate as a prophage",
    "A prophage is phage deoxyribonucleic acid (DNA) integrated into a bacterial chromosome and copied with it, "
    "the lysogenic cycle. A latent herpesvirus keeps its deoxyribonucleic acid as an episome in the nucleus, not integrated, and is "
    "generally not detectable.",
    "phage lysogeny borrowed")],
  c(15, 26, 55)),

Q("Herpesvirus family", IO1,
  "Where in the host cell do herpesviruses replicate?",
  ("Within the nucleus",
   "Correct. Herpesviruses replicate within the host cell nucleus, as most deoxyribonucleic acid (DNA) viruses "
   "do; most deoxyribonucleic acid viruses are budded off the nucleus. During latency their deoxyribonucleic acid also stays in the nucleus, as an "
   "episome."),
  [("In cytoplasmic factory areas",
    "Multiplying in cytoplasmic factory areas is the exception of the poxviruses, the largest and most complex "
    "animal viruses. Herpesviruses are deoxyribonucleic acid (DNA) viruses that follow the usual pattern and "
    "replicate within the nucleus.",
    "poxvirus site borrowed"),
   ("Free in the cytoplasm",
    "Most ribonucleic acid (RNA) viruses multiply in and are released from the cytoplasm. Herpesviruses carry "
    "double-stranded deoxyribonucleic acid (DNA), and like most deoxyribonucleic acid viruses they replicate within the nucleus.",
    "ribonucleic acid virus pattern borrowed"),
   ("At the cell membrane, while budding",
    "Budding through a cell membrane is how an enveloped animal virus is released and gets its envelope, after "
    "replication is finished. Herpesvirus replication itself happens within the nucleus.",
    "release step confused with replication")],
  c(9, 22, 24, 26, 32, 55)),

# ============================================================== HERPES SIMPLEX VIRUS TYPE 1 (slides 58-62, chart 4)
Q("Herpes simplex virus type 1", IO4,
  "Before the vesicles of herpes labialis (a cold sore) form, what does the patient usually notice?",
  ("Itching and tingling",
   "Correct. Herpes labialis, the fever blister or cold sore, is the most common recurrent herpes simplex virus "
   "type 1 infection. Itching and tingling come before vesicles form at the mucocutaneous junction of the lips or "
   "nearby skin; the lesion then crusts over and heals."),
  [("Bilateral tender groin swelling",
    "Bilateral swelling and tenderness in the groin, with malaise and fever, open genital herpes from herpes "
    "simplex virus type 2. A cold sore sits on the lip, and its warning is local itching and tingling.",
    "genital herpes onset borrowed"),
   ("A gritty feeling in the eye",
    "A gritty feeling in the eye, with conjunctivitis, sharp pain and sensitivity to light, is herpetic keratitis, "
    "ocular herpes. A cold sore is on the lips, and itching and tingling there come before its vesicles.",
    "keratitis borrowed"),
   ("Sore throat and swollen nodes",
    "Fever, sore throat and swollen lymph nodes describe herpetic gingivostomatitis, an infection of the "
    "oropharynx in young children. Herpes labialis is a recurrent lip lesion heralded by itching and tingling.",
    "gingivostomatitis borrowed")],
  ci(4, 58, 60)),

Q("Herpes simplex virus type 1", IO2,
  "Which stimulus can trigger a recurrence of a latent herpes simplex virus type 1 infection?",
  ("Ultraviolet radiation",
   "Correct. Recurrent herpes simplex infection is triggered by stimuli such as fever, ultraviolet radiation, "
   "stress and mechanical injury. Newly formed viruses then migrate from the ganglion to the body surface and "
   "produce a local skin or membrane lesion, such as a cold sore."),
  [("Eating salt-cured foods",
    "Eating salt-cured foods is a risk factor for nasopharyngeal carcinoma, a tumor linked to Epstein-Barr virus. "
    "Herpes simplex recurrences follow fever, ultraviolet radiation, stress or mechanical injury.",
    "carcinoma risk factor borrowed"),
   ("Handling sheep or goats",
    "Handling sheep or goats, by feeding, shearing or bites, passes orf virus, a parapoxvirus, to humans. It is a "
    "new infection, not a trigger for latent herpes simplex, which reactivates with fever, ultraviolet light, "
    "stress or injury.",
    "orf exposure borrowed"),
   ("Coinfection with malaria",
    "Chronic coinfection with malaria may be associated with Burkitt lymphoma, an Epstein-Barr virus tumor in "
    "central African children. The listed triggers for herpes simplex recurrence are fever, ultraviolet "
    "radiation, stress and mechanical injury.",
    "Burkitt cofactor borrowed")],
  c(54, 59, 77)),

Q("Herpes simplex virus type 1", IO4,
  "A young child has an oropharyngeal infection from herpes simplex virus type 1, with fever, sore throat and "
  "swollen lymph nodes. What is this infection called?",
  ("Herpetic gingivostomatitis",
   "Correct. Herpetic gingivostomatitis is herpes simplex virus type 1 infection of the oropharynx in young "
   "children, with fever, sore throat and swollen lymph nodes. Herpes simplex type 1 infection typically occurs "
   "in early childhood."),
  [("Herpes labialis",
    "Herpes labialis is the cold sore or fever blister: a recurrent lesion at the mucocutaneous junction of the "
    "lips, preceded by itching and tingling. An infection across the oropharynx of a young child with fever and "
    "sore throat is gingivostomatitis.",
    "recurrent lip lesion confused"),
   ("Herpetic keratitis",
    "Herpetic keratitis is ocular herpes: inflammation of the eye with a gritty feeling, conjunctivitis, sharp "
    "pain and sensitivity to light. This child's infection is in the oropharynx, which makes it "
    "gingivostomatitis.",
    "eye infection confused"),
   ("Herpes gladiatorum",
    "Herpes gladiatorum, mat herpes, is a skin infection common in athletes in wrestling, basketball or rugby. A "
    "young child's oropharyngeal infection with fever, sore throat and swollen nodes is herpetic "
    "gingivostomatitis.",
    "athlete skin infection confused")],
  ci(4, 58, 60, 62)),

Q("Herpes simplex virus type 1", IO4,
  "Which finding fits herpetic keratitis?",
  ("Sensitivity to light",
   "Correct. Herpetic keratitis, ocular herpes, is inflammation of the eye from herpes simplex virus: a gritty "
   "feeling in the eye, conjunctivitis, sharp pain and sensitivity to light."),
  [("Blind spots from retinitis",
    "Retinitis with blind spots is cytomegalovirus disease in patients with acquired immunodeficiency syndrome. "
    "Herpetic keratitis is an inflamed eye with a gritty feeling, conjunctivitis, sharp pain and light "
    "sensitivity.",
    "cytomegalovirus eye disease borrowed"),
   ("Vesicles at the lip margin",
    "Vesicles at the mucocutaneous junction of the lips are herpes labialis, the cold sore. Keratitis is the eye "
    "form of herpes simplex, with a gritty feeling, sharp pain and sensitivity to light.",
    "lip lesion confused"),
   ("Painless discolored lumps",
    "Small, painless, discolored lumps on the skin are Kaposi sarcoma, linked to human herpesvirus 8. Herpetic "
    "keratitis is painful: sharp eye pain with a gritty feeling and sensitivity to light.",
    "Kaposi lesion borrowed")],
  ci(4, 60, 83)),

Q("Herpes simplex virus type 1", IO5,
  "A high school wrestler develops the clustered skin lesions shown, a herpes simplex infection common in his "
  "sport. Which measure may help prevent it?",
  ("Showering right after practice",
   "Correct. These are herpes gladiatorum, mat herpes, a skin infection common in wrestling, basketball and rugby "
   "players. It may be prevented by showering immediately after practice or games and by not sharing razors, "
   "deodorants or towels."),
  [("A live attenuated vaccine",
    "A live attenuated vaccine exists for chickenpox and shingles, from varicella zoster virus. Mat herpes is"
    " prevented by showering promptly and not sharing razors, deodorants or towels.",
    "varicella vaccine borrowed"),
   ("Sharing towels only with teammates",
    "Sharing towels, razors or deodorants is exactly what should be avoided, since herpes simplex spreads by "
    "direct exposure to secretions from lesions. Showering right after practice and keeping personal items "
    "personal are the listed measures.",
    "reversed advice"),
   ("Screening by Papanicolaou smear",
    "A Papanicolaou (Pap) smear is a stained specimen used to diagnose herpes infection and to screen for "
    "abnormal cervical cells; it does not prevent mat herpes. Mat herpes is prevented by showering after "
    "practice and not sharing personal items.",
    "diagnostic test confused with prevention")],
  ci(62, 59, 69, 99),
  img=IMG + "/l18-fig-06.jpg",
  alt="Close-up photograph of skin on a limb or shoulder covered with a cluster of small raised, fluid-filled "
      "and crusting red bumps.",
  slide="Slide 62"),

# ============================================================== HERPES SIMPLEX VIRUS TYPE 2 (slides 58-59, 63, chart 5)
QO("Herpes simplex virus type 2", IO5,
   "Herpes simplex virus type 2 infection typically occurs in which age group?",
   [("Babies 2 to 12 months",
     "Babies 2 to 12 months old get roseola from human herpesvirus 6: fever followed by a faint rash. Herpes "
     "simplex virus type 2, the genital type, occurs in people aged 14 to 29.",
     "roseola age borrowed"),
    ("Children 5 to 7 years",
     "Children 5 to 7 years old in central Africa are the group for Burkitt lymphoma, an Epstein-Barr virus "
     "tumor. Herpes simplex virus type 2 infection occurs in ages 14 to 29.",
     "Burkitt age borrowed"),
    ("People 14 to 29 years",
     "Correct. Herpes simplex virus type 2, which usually causes genital lesions, occurs in ages 14 to 29. Type 1, "
     "the oropharyngeal type behind cold sores, occurs in early childhood instead.",
     None),
    ("Adults 30 to 60 years",
     "Adults 30 to 60 years old are the group for nasopharyngeal carcinoma, an Epstein-Barr virus tumor. Herpes "
     "simplex virus type 2 occurs in the younger group, ages 14 to 29.",
     "carcinoma age borrowed")],
   2, c(58, 77, 81)),

Q("Herpes simplex virus type 2", IO5,
  "Which statement about the transmission of genital herpes is accurate?",
  ("It can spread without visible lesions",
   "Correct. Herpes simplex spreads by direct exposure to secretions containing the virus. Active lesions are the "
   "most significant source, but genital herpes can be transmitted in the absence of lesions, so herpes simplex "
   "virus type 2 can spread without visible lesions."),
  [("It needs visible active lesions to spread",
    "Active lesions are the most significant source, but they are not required: genital herpes can be "
    "transmitted in the absence of lesions. That is why a partner with no visible sores can still pass herpes "
    "simplex virus type 2.",
    "lesions believed necessary"),
   ("It spreads mainly by respiratory droplets",
    "Respiratory droplets, with fluid from active skin lesions, spread varicella zoster virus, the cause of "
    "chickenpox. Herpes simplex virus type 2 spreads by direct contact with secretions, even without visible "
    "lesions.",
    "varicella route borrowed"),
   ("It spreads mainly through blood products",
    "Minute amounts of blood and blood products transmit hepatitis B virus. Genital herpes spreads by direct "
    "contact with secretions containing herpes simplex virus type 2, sometimes with no lesions visible.",
    "hepatitis B route borrowed")],
  ci(5, 58, 59, 68, 87)),

Q("Herpes simplex virus type 2", IO4,
  "A 22-year-old has malaise, fever and bilateral tender groin swelling, followed by clusters of sensitive "
  "vesicles on the genitalia like those shown, which later ulcerate. Which virus causes this?",
  ("Herpes simplex virus type 2",
   "Correct. This is genital herpes from herpes simplex virus type 2: it starts with malaise, anorexia, fever and "
   "bilateral swelling and tenderness in the groin, then clusters of sensitive vesicles on the genitalia, "
   "perineum and buttocks that ulcerate, with urethritis and painful urination."),
  [("Molluscum contagiosum virus",
    "Molluscum contagiosum, a poxvirus, gives small, smooth, waxy macules on the genitals and thighs and is "
    "normally self-limiting. It does not begin with fever and groin swelling, and its lesions are not clusters of "
    "sensitive vesicles that ulcerate.",
    "genital poxvirus lesion confused"),
   ("Human papillomavirus",
    "Human papillomavirus causes genital warts, ranging from tiny flat bumps to branching cauliflower-like "
    "masses. Clusters of sensitive vesicles that ulcerate, after fever and tender groin swelling, are genital "
    "herpes.",
    "genital wart confused"),
   ("Varicella zoster virus",
    "Varicella zoster virus gives chickenpox, with vesicles over the body, and shingles, with vesicles along a "
    "dermatome. Sensitive vesicles clustered on the genitalia after groin swelling and fever point to herpes "
    "simplex virus type 2.",
    "vesicular rash of another herpesvirus")],
  ci(63, 5, 46, 69, 97),
  img=IMG + "/l18-fig-07.jpg",
  alt="Close-up photograph of skin with a tight cluster of small, pale, fluid-filled blisters, one area beginning "
      "to crust.",
  slide="Slide 63"),

Q("Herpes simplex virus type 2", IO2,
  "Which trigger is described for recurrent bouts of genital herpes?",
  ("Menstruation",
   "Correct. Recurrent bouts of genital herpes are usually less severe than the first and are triggered by "
   "menstruation, stress and concurrent bacterial infection. The virus reactivates from its latent site and new "
   "virions travel back to the skin or membrane surface."),
  [("Eating salt-cured foods",
    "Eating salt-cured foods is a risk factor for nasopharyngeal carcinoma, linked to Epstein-Barr virus. Genital "
    "herpes recurrences are triggered by menstruation, stress and concurrent bacterial infection.",
    "carcinoma risk factor borrowed"),
   ("A recent blood transfusion",
    "A blood transfusion is a route of new infection for human herpesvirus 8 and hepatitis B virus, not a trigger "
    "for latent genital herpes. Recurrent bouts follow menstruation, stress or a concurrent bacterial infection.",
    "transmission route confused with trigger"),
   ("Contact with a shingles patient",
    "Contact with fluid from a shingles patient's lesions can give an unvaccinated person chickenpox, from "
    "varicella zoster virus. It does not reactivate genital herpes, whose recurrences follow menstruation, stress "
    "or concurrent bacterial infection.",
    "varicella exposure borrowed")],
  c(63, 69, 77, 83, 87)),

# ============================================================== HERPES OF THE NEWBORN (slides 64-65, chart 5)
Q("Herpes of the newborn", IO5,
  "A newborn has the herpes simplex lesions shown on the face and scalp. How was this infection most likely "
  "acquired?",
  ("From the mother, before or during birth",
   "Correct. In herpes of the newborn, from herpes simplex virus type 1 or type 2, the infant is contaminated by "
   "the mother before or during birth, or by hand transmission from mother to infant. It infects the mouth, skin, "
   "eyes and central nervous system and is potentially fatal."),
  [("From a shingles patient's lesion fluid",
    "Fluid from active shingles lesions passes varicella zoster virus, and an unvaccinated contact develops "
    "chickenpox. Neonatal herpes simplex comes from the mother, before or during birth or by her hands.",
    "varicella exposure borrowed"),
   ("From a contaminated organ transplant",
    "Organ transplants can carry cytomegalovirus and human herpesvirus 8 into a recipient. A newborn with herpes "
    "simplex lesions was contaminated by the mother before or during birth, or by hand transmission.",
    "transplant route borrowed"),
   ("From handling a pet that hunts rodents",
    "Handling a cat that has interacted with rodents passes cowpox, which gives pocks usually on the hands. "
    "Neonatal herpes simplex is passed from mother to infant before or during birth, or by hand afterward.",
    "cowpox route borrowed")],
  ci(65, 5, 53, 64, 69, 71, 83),
  img=IMG + "/l18-fig-08.jpg",
  alt="Photograph of a newborn in intensive care with a tube taped at the mouth and scattered red, crusted and "
      "blistered spots over the face and scalp.",
  slide="Slide 65"),

Q("Herpes of the newborn", IO4,
  "In herpes of the newborn, involvement of which site carries the worst outlook?",
  ("The central nervous system",
   "Correct. Neonatal herpes infects the mouth, skin, eyes and central nervous system, and it is potentially "
   "fatal. Its mortality rate is far higher when the central nervous system is involved than when the infection "
   "stays in the skin, eyes and mouth."),
  [("The skin",
    "Skin involvement is common in neonatal herpes, but infection confined to the skin, eyes and mouth has a much "
    "lower mortality rate than spread to the central nervous system, the most dangerous site.",
    "visible site assumed worst"),
   ("The eyes",
    "Eye involvement belongs to the lower-risk group of neonatal herpes, with the skin and mouth. Mortality rises "
    "sharply when the infection reaches the central nervous system.",
    "eye site overrated"),
   ("The mouth",
    "Mouth lesions in a newborn fall in the lower-mortality group, with skin and eye infection. The central "
    "nervous system is the site where neonatal herpes is deadliest.",
    "oral site overrated")],
  ci(5, 64)),

Q("Herpes of the newborn", IO4,
  "A pregnant woman with genital herpes has an active outbreak when labor begins. Which delivery is advised to "
  "protect the infant?",
  ("Delivery by cesarean section",
   "Correct. Herpes of the newborn is prevented by screening pregnant women and by delivery by cesarean section "
   "if there is an outbreak at the time of birth, because the infant is otherwise contaminated by the mother "
   "during birth."),
  [("Vaginal delivery after vaccination",
    "There is no herpes simplex vaccine: only candidate vaccines in trials and ongoing research. With an outbreak "
    "at the time of birth, the infant is protected by delivery by cesarean section.",
    "nonexistent vaccine assumed"),
   ("Vaginal delivery once lesions crust",
    "A cold sore crusts over in a few days and heals, but genital herpes can spread even without visible lesions, "
    "and labor will not wait. An outbreak at the time of birth calls for delivery by cesarean section.",
    "crusting assumed safe"),
   ("Vaginal delivery, then infant screening",
    "Screening is done on the pregnant woman, before birth, not as a substitute for a safe delivery. With an "
    "active outbreak at birth, the infant is protected by delivery by cesarean section.",
    "screening target confused")],
  ci(4, 5, 58, 59, 60, 64)),

# ============================================================== HERPES SIMPLEX DIAGNOSIS (slides 66-67)
Q("Herpes simplex diagnosis", IO4,
  "Scrapings from the base of a genital vesicle are stained, as shown. What is the large central "
  "cell?",
  ("A giant cell with multiple nuclei",
   "Correct. Scrapings from the base of herpes simplex lesions show giant multinucleated cells and inclusion "
   "bodies. In this stained Papanicolaou (Pap) specimen, the large central cell holds a long chain of many "
   "nuclei, surrounded by normal cells."),
  [("A large atypical lymphocyte",
    "A large atypical lymphocyte, with one big nucleus and abundant cytoplasm, is seen in the blood count in "
    "Epstein-Barr virus infection. The pictured cell came from a vesicle base and holds many nuclei: a giant "
    "multinucleated cell.",
    "Epstein-Barr blood cell confused"),
   ("A cell with one owl's-eye nucleus",
    "An enlarged cell with a single nucleus holding a large inclusion, the owl's eye effect, identifies "
    "cytomegalovirus. Count the nuclei: the pictured cell has many, the giant multinucleated cell of herpes "
    "simplex.",
    "cytomegalovirus inclusion confused"),
   ("A normal epithelial cell",
    "Normal cells sit around the edge of this specimen, each with one small nucleus. The central cell is far "
    "larger and holds many nuclei, the giant multinucleated cell typical of herpes simplex scrapings.",
    "normal cell confused")],
  ci(67, 66, 73, 79, 80),
  img=IMG + "/l18-fig-09.jpg",
  alt="Stained microscope specimen with a large pink cell in the center holding a long chain of many dark "
      "nuclei, surrounded by smaller blue-green cells and scattered small dark cells.",
  slide="Slide 67"),

Q("Herpes simplex diagnosis", IO4,
  "Which laboratory test is used in diagnosing herpes simplex infection?",
  ("Direct fluorescent antibody test",
   "Correct. Herpes simplex is diagnosed from its typical vesicles and exudate, scrapings from the base of lesions "
   "showing giant multinucleated cells and inclusion bodies, culture and specific tests for severe or "
   "disseminated infection, and direct fluorescent antibody tests."),
  [("Radioimmunoassay for surface antigen",
    "Radioimmunoassay and other tests for surface antigens diagnose hepatitis B virus infection. Herpes simplex is "
    "diagnosed from lesion scrapings showing giant multinucleated cells, culture and direct fluorescent antibody "
    "tests.",
    "hepatitis B test borrowed"),
   ("Count for atypical lymphocytes",
    "A differential blood count showing lymphocytosis, neutropenia and large atypical lymphocytes points to "
    "Epstein-Barr virus. Herpes simplex is diagnosed from the lesion itself: scrapings, culture and direct "
    "fluorescent antibody tests.",
    "Epstein-Barr test borrowed"),
   ("Culture in liver cancer cells",
    "Culture in human liver cancer cells, after isolating the viral deoxyribonucleic acid (DNA), is how "
    "hepatitis B virus must be grown in the lab. Herpes simplex is diagnosed with scrapings, culture and direct "
    "fluorescent antibody tests.",
    "hepadnavirus culture borrowed")],
  c(66, 79, 86, 90)),

# ============================================================== VARICELLA ZOSTER VIRUS (slides 68-70, chart 5)
Q("Varicella zoster virus", IO5,
  "What is the natural host range of varicella zoster virus?",
  ("Humans only",
   "Correct. Varicella zoster virus, the cause of chickenpox and shingles, has humans as its only natural host. It "
   "passes from person to person by respiratory droplets and by contact with fluid from active skin lesions."),
  [("Humans and rodents",
    "Rodents are the primary reservoirs of cowpox, which humans catch rarely, often by handling cats that "
    "interacted with rodents. Varicella zoster virus has humans as its only natural host.",
    "cowpox reservoir borrowed"),
   ("Humans and sheep",
    "Sheep and goats carry orf virus, a parapoxvirus that humans catch by feeding, shearing or bites. Varicella "
    "zoster virus has no animal host: humans are its only natural host.",
    "orf host borrowed"),
   ("Humans and cattle",
    "Cowpox is found in cows as well as rodents, cats and zoo animals. Varicella zoster virus infects only humans "
    "naturally, spreading by respiratory droplets and fluid from active lesions.",
    "cowpox host borrowed")],
  c(53, 54, 68)),

Q("Varicella zoster virus", IO5,
  "How does chickenpox spread from person to person?",
  ("Droplets and fluid from lesions",
   "Correct. Varicella zoster virus is transmitted by respiratory droplets and by contact with fluid from active "
   "skin lesions. The primary infection is chickenpox, with its characteristic vesicles."),
  [("Blood transfusion and transplants",
    "Blood transfusion and organ transplant are routes for human herpesvirus 8, the Kaposi sarcoma virus, and "
    "transplants also carry cytomegalovirus. Chickenpox spreads by respiratory droplets and fluid from active "
    "lesions.",
    "blood-borne route borrowed"),
   ("Contact with infected animals",
    "Contact with infected animals spreads mpox and cowpox, poxviruses with animal hosts. Varicella zoster virus "
    "has humans as its only natural host and spreads by respiratory droplets and lesion fluid.",
    "zoonotic route borrowed"),
   ("Sexual contact with a carrier",
    "Sexual contact spreads herpes simplex virus type 2 and human herpesvirus 8, among others. Chickenpox needs no "
    "sexual contact; it spreads through respiratory droplets and contact with fluid from active "
    "lesions.",
    "sexual route borrowed")],
  ci(4, 5, 6, 68)),

Q("Varicella zoster virus", IO2,
  "A man who had chickenpox as a child develops the painful rash shown. Where had the virus been latent?",
  ("In neurons of a nerve ganglion",
   "Correct. After primary chickenpox, varicella zoster virus enters neurons and remains latent. Activated in the "
   "ganglion, for example by stress, it migrates down the sensory nerve to the skin and causes shingles, with "
   "inflammation of the ganglion and pain down the nerve pathway."),
  [("In B lymphocytes",
    "B cells are where Epstein-Barr virus lies dormant before it is reactivated. Varicella zoster virus waits in "
    "neurons of a nerve ganglion, which is why shingles follows a nerve pathway.",
    "Epstein-Barr latency site borrowed"),
   ("In the salivary glands",
    "The salivary glands are infected by cytomegalovirus, the salivary gland virus, and by Epstein-Barr virus. "
    "Shingles comes from varicella zoster virus reactivating in neurons of a nerve ganglion.",
    "salivary gland virus confused"),
   ("In the kidney and bladder lining",
    "The kidney and the lining of the ureters and bladder are where BK polyomavirus lies dormant. Varicella "
    "zoster virus is latent in neurons of a ganglion and travels down the sensory nerve when it reactivates.",
    "BK latency site borrowed")],
  ci(70, 68, 69, 71, 75, 102),
  img=IMG + "/l18-fig-11.jpg",
  alt="Photograph of a person's back seen from behind, with a broad band of red, blotchy, raised rash running "
      "across one shoulder blade and down the arm on the same side.",
  slide="Slide 70"),

Q("Varicella zoster virus", IO4,
  "Why does shingles cause pain along a nerve pathway?",
  ("Inflammation of the ganglion",
   "Correct. In shingles, reactivated varicella zoster virus inflames the ganglion, giving pain down the nerve "
   "pathway, and vesicles appear on the skin area that nerve serves, the dermatome."),
  [("Destruction of myelin-making cells",
    "Destruction of the cells that produce myelin is progressive multifocal leukoencephalopathy, caused by JC "
    "polyomavirus in immunosuppressed patients. Shingles pain comes from inflammation of the ganglion where "
    "varicella zoster virus reactivates.",
    "polyomavirus damage borrowed"),
   ("Swelling of cervical lymph nodes",
    "Cervical lymphadenopathy, with sore throat, high fever and splenomegaly, is infectious mononucleosis from "
    "Epstein-Barr virus. Shingles pain follows a nerve because the ganglion of that nerve is inflamed.",
    "mononucleosis sign borrowed"),
   ("Ulceration of clustered vesicles",
    "Clusters of sensitive vesicles that ulcerate are genital herpes, from herpes simplex virus type 2. Shingles "
    "pain runs down a nerve pathway because varicella zoster virus inflames the ganglion of that nerve.",
    "genital herpes lesion borrowed")],
  c(63, 69, 70, 75, 102)),

Q("Varicella zoster virus", IO5,
  "Which vaccine is available against varicella zoster virus?",
  ("Live attenuated, for both diseases",
   "Correct. A live attenuated vaccine is available for chickenpox and for shingles, the two diseases of "
   "varicella zoster virus. Vaccination also matters because shingles patients can give chickenpox to "
   "unvaccinated people."),
  [("None yet, only candidates in trials",
    "Having no vaccine, only candidates in trials, describes herpes simplex virus type 1 and cytomegalovirus. "
    "Varicella zoster virus has a live attenuated vaccine for both chickenpox and shingles.",
    "herpes simplex and cytomegalovirus status borrowed"),
   ("Therapeutic, for related cancers",
    "Therapeutic vaccines for related cancers, with no preventive vaccine, describe Epstein-Barr virus. Varicella "
    "zoster virus has a preventive live attenuated vaccine for chickenpox and shingles.",
    "Epstein-Barr status borrowed"),
   ("Inactivated oral, for recruits",
    "An inactivated oral vaccine against types 4 and 7, given to some military personnel in training, is the "
    "adenovirus vaccine. Varicella zoster virus has a live attenuated vaccine for both chickenpox and shingles.",
    "adenovirus vaccine borrowed")],
  ci(4, 5, 69, 79, 94)),

# ============================================================== CYTOMEGALOVIRUS (slides 71-74, chart 5)
Q("Cytomegalovirus", IO4,
  "A lung specimen shows an enlarged infected cell whose nucleus holds a large inclusion, giving an owl's eye "
  "effect. Which virus is the cause?",
  ("Cytomegalovirus",
   "Correct. Cytomegaloviruses produce giant cells with nuclear and cytoplasmic inclusions. In an infected lung "
   "cell, the nucleus with its large inclusion gives the owl's eye effect, which identifies cytomegalovirus."),
  [("Epstein-Barr virus",
    "Epstein-Barr virus is recognized in the blood by large atypical lymphocytes, with lymphocytosis and "
    "neutropenia. An enlarged lung cell with a large nuclear inclusion and an owl's eye look is cytomegalovirus.",
    "Epstein-Barr cell change confused"),
   ("Human herpesvirus 8",
    "Human herpesvirus 8 is linked with Kaposi sarcoma, small painless discolored lumps on the skin. The owl's "
    "eye inclusion in an enlarged cell is the mark of cytomegalovirus.",
    "Kaposi virus confused"),
   ("Varicella zoster virus",
    "Varicella zoster virus is recognized clinically by chickenpox vesicles and dermatomal shingles. The owl's "
    "eye effect, a large nuclear inclusion in a giant cell, identifies cytomegalovirus.",
    "other herpesvirus confused")],
  ci(73, 5, 68, 69, 71, 79, 83)),

Q("Cytomegalovirus", IO5,
  "Which of these can transmit cytomegalovirus?",
  ("Breast milk",
   "Correct. Cytomegalovirus is transmitted in saliva, respiratory mucus, breast milk, urine, semen, "
   "cervical secretions, blood and tears, and in tissues such as transplants."),
  [("Handling sheep or goats",
    "Handling sheep or goats, by feeding, shearing or bites, transmits orf virus, a parapoxvirus. "
    "Cytomegalovirus is a human virus spread in body fluids such as saliva, breast milk, urine and semen, and in "
    "transplanted tissue.",
    "orf route borrowed"),
   ("Handling a rodent-hunting cat",
    "Handling cats that interacted with rodents passes cowpox to humans, usually on the hands. Cytomegalovirus "
    "spreads through body fluids, including breast milk, saliva and urine, and through transplants.",
    "cowpox route borrowed"),
   ("Contact with infected animals",
    "Contact with infected animals spreads mpox, a poxvirus. Cytomegalovirus passes from person to person in "
    "body fluids such as breast milk, saliva, urine, semen and cervical secretions, or in transplanted tissue.",
    "mpox route borrowed")],
  ci(5, 4, 53, 54, 71)),

Q("Cytomegalovirus", IO2,
  "How does cytomegalovirus establish its persistent infections?",
  ("Hindering antigen presentation to T cells",
   "Correct. Cytomegalovirus establishes persistent infections by interfering with antigen presentation to CD8 "
   "(cluster of differentiation 8) T cells. It also reduces cell-surface major histocompatibility complex class I, "
   "which leaves infected cells open to attack by natural killer cells."),
  [("Seeding the blood from the liver",
    "Multiplying exclusively in the liver and continuously seeding the blood is the chronic infection of "
    "hepatitis B virus. Cytomegalovirus persists by interfering with antigen presentation to T cells and is "
    "commonly latent in various tissues.",
    "hepatitis B chronicity borrowed"),
   ("Integrating as a prophage",
    "A prophage is phage deoxyribonucleic acid (DNA) integrated into a bacterial chromosome, the lysogenic cycle. "
    "Cytomegalovirus persists in human tissues by interfering with antigen presentation to CD8 (cluster of "
    "differentiation 8) T cells.",
    "phage lysogeny borrowed"),
   ("Multiplying in cytoplasmic factories",
    "Multiplying in cytoplasmic factory areas is how poxviruses replicate, not a way to persist. Cytomegalovirus "
    "persists by interfering with antigen presentation to T cells, staying latent in various tissues.",
    "poxvirus replication borrowed")],
  c(15, 32, 71, 87)),

Q("Cytomegalovirus", IO4,
  "Most cytomegalovirus infections are asymptomatic. Which group develops a more virulent form of the disease?",
  ("Immunodeficient adults",
   "Correct. Three groups develop a more virulent cytomegalovirus disease: fetuses, newborns and immunodeficient "
   "adults. In acquired immunodeficiency syndrome it causes retinitis and disseminated disease, and most "
   "transplant patients get pneumonitis or hepatitis; treatment is reserved for the immunocompromised."),
  [("College-age young adults",
    "The college-age population in industrialized countries is the group vulnerable to infectious mononucleosis "
    "from Epstein-Barr virus. The virulent cytomegalovirus groups are fetuses, newborns and immunodeficient "
    "adults.",
    "mononucleosis group borrowed"),
   ("Wrestlers and rugby players",
    "Athletes in wrestling, basketball or rugby are prone to herpes gladiatorum, a herpes simplex skin "
    "infection. Severe cytomegalovirus disease strikes fetuses, newborns and immunodeficient adults.",
    "mat herpes group borrowed"),
   ("Healthy older adults",
    "Older patients are more likely to get shingles from varicella zoster virus. Healthy age alone does not make "
    "cytomegalovirus virulent; the three groups are fetuses, newborns and immunodeficient adults.",
    "shingles group borrowed")],
  c(62, 69, 72, 74, 75)),

Q("Cytomegalovirus", IO3,
  "A newborn infected before birth has microcephaly, an enlarged liver and spleen, jaundice, capillary bleeding "
  "and ocular inflammation. Which herpesvirus crossed the placenta?",
  ("Cytomegalovirus",
   "Correct. Cytomegalovirus is teratogenic: it crosses the placenta and causes developmental disturbances. "
   "Affected newborns may have an enlarged liver and spleen, jaundice, capillary bleeding, microcephaly and "
   "ocular inflammation, and survivors develop neurological, hearing and visual sequelae."),
  [("Epstein-Barr virus",
    "Epstein-Barr virus infects lymphoid tissue and salivary glands and causes infectious mononucleosis, Burkitt "
    "lymphoma and nasopharyngeal carcinoma; it is oncogenic, not teratogenic. Microcephaly with jaundice and "
    "bleeding at birth points to cytomegalovirus.",
    "oncogenic virus confused with teratogenic"),
   ("Human herpesvirus 8",
    "Human herpesvirus 8 is oncogenic, linked with Kaposi sarcoma in patients with acquired immunodeficiency "
    "syndrome. The teratogenic herpesvirus that gives microcephaly, an enlarged liver and spleen, and jaundice is "
    "cytomegalovirus.",
    "oncogenic virus confused with teratogenic"),
   ("Human herpesvirus 6",
    "Human herpesvirus 6 causes roseola in babies 2 to 12 months old: fever followed by a faint rash, usually "
    "self-limited. Microcephaly and an enlarged liver and spleen from infection before birth are cytomegalovirus.",
    "infant rash virus confused")],
  ci(5, 28, 72, 75, 77, 81, 83)),

Q("Cytomegalovirus", IO5,
  "Many cytomegalovirus vaccines are in development, but none is available. What makes development difficult?",
  ("Lack of an animal model",
   "Correct. Many cytomegalovirus vaccines are at different stages of development, but progress is difficult "
   "because of the lack of an animal model. For now, no vaccine is available, though several are in clinical "
   "trials."),
  [("Difficulty culturing the virus",
    "Difficulty growing the virus in the lab, so that its deoxyribonucleic acid (DNA) must be put into liver "
    "cancer cells, describes hepatitis B virus, which does have vaccines. The cytomegalovirus obstacle is the "
    "lack of an animal model.",
    "hepadnavirus culture borrowed"),
   ("Its very large, complex genome",
    "The largest genome of all viruses belongs to the poxviruses, and a vaccinia vaccine still protects against "
    "smallpox. Genome size is not the stated obstacle; for cytomegalovirus it is the lack of an animal model.",
    "poxvirus genome borrowed"),
   ("Its single-stranded genome",
    "A single-stranded deoxyribonucleic acid (DNA) genome belongs to the parvoviruses. Cytomegalovirus carries "
    "double-stranded deoxyribonucleic acid like all herpesviruses, and its vaccines are held back by the lack of an animal model.",
    "parvovirus genome borrowed")],
  ci(5, 4, 32, 55, 74, 86, 103)),

# ============================================================== EPSTEIN-BARR VIRUS (slides 75-80, chart 6)
Q("Epstein-Barr virus", IO2,
  "Where does Epstein-Barr virus lie dormant after infection?",
  ("In B lymphocytes",
   "Correct. Epstein-Barr virus infects lymphoid tissue and the salivary glands, then lies dormant in B cells. It "
   "can be reactivated later, and reactivation may be asymptomatic."),
  [("In sensory nerve ganglia",
    "Sensory nerve ganglia hold latent herpes simplex virus and varicella zoster virus, which travel down nerves "
    "when they reactivate. Epstein-Barr virus stays dormant in B cells.",
    "neural latency borrowed"),
   ("In liver cells",
    "Liver cells are where hepatitis B virus multiplies exclusively, seeding the blood in a chronic infection. "
    "Epstein-Barr virus, which infects lymphoid tissue, lies dormant in B lymphocytes.",
    "hepatitis B site borrowed"),
   ("In the kidney and bladder lining",
    "The kidney and the lining of the ureters and bladder are the dormant site of BK polyomavirus. Epstein-Barr "
    "virus is dormant in B lymphocytes, the cells that also give rise to Burkitt lymphoma.",
    "BK latency site borrowed")],
  c(59, 68, 75, 77, 87, 102)),

Q("Epstein-Barr virus", IO4,
  "A college student has high fever, cervical lymphadenopathy, splenomegaly and the throat shown. Which "
  "differential blood count is expected?",
  ("Lymphocytosis and neutropenia",
   "Correct. This is infectious mononucleosis from Epstein-Barr virus, with tonsillar exudate, sore throat, high "
   "fever, cervical lymphadenopathy and splenomegaly. The differential blood count shows lymphocytosis, "
   "neutropenia and large atypical lymphocytes; serological assays detect antibodies and antigen."),
  [("Neutrophilia and lymphopenia",
    "This reverses the mononucleosis count: Epstein-Barr virus raises lymphocytes and lowers neutrophils, giving "
    "lymphocytosis, neutropenia and large atypical lymphocytes.",
    "reversed direction"),
   ("Low natural killer cell levels",
    "Low natural killer cell levels are listed among the features of chronic fatigue syndrome, which has only a "
    "possible link to Epstein-Barr virus. Acute mononucleosis shows lymphocytosis, neutropenia and atypical "
    "lymphocytes.",
    "chronic fatigue feature borrowed"),
   ("Halted red blood cell production",
    "Stopping red blood cell production is an effect of parvovirus B19 in adults. The mononucleosis blood count "
    "shows lymphocytosis, neutropenia and large atypical lymphocytes.",
    "parvovirus effect borrowed")],
  ci(76, 6, 75, 78, 79, 104),
  img=IMG + "/l18-fig-12.jpg",
  alt="Photograph looking into an open mouth at the back of the throat, labeled to show a rash on the palate, "
      "the tonsils and white exudate on the tonsils.",
  slide="Slide 76"),

Q("Epstein-Barr virus", IO4,
  "A blood smear from a patient with an Epstein-Barr virus infection shows the cell indicated by the arrows. "
  "What is it?",
  ("A large atypical lymphocyte",
   "Correct. Epstein-Barr virus infection gives lymphocytosis with large atypical lymphocytes. Compared with a "
   "normal small, round lymphocyte, the infected cell is much larger, with an irregular nucleus and abundant "
   "pale cytoplasm pressed between the red blood cells."),
  [("A normal small lymphocyte",
    "A normal lymphocyte is small and round, mostly nucleus, about the size of the nearby red blood cells. The "
    "pictured cell is far larger with abundant cytoplasm: the large atypical lymphocyte of Epstein-Barr virus.",
    "normal cell confused"),
   ("A giant multinucleated cell",
    "Giant multinucleated cells come from scrapings at the base of herpes simplex lesions and hold many nuclei. "
    "The pictured blood cell has one nucleus and is a large atypical lymphocyte.",
    "herpes simplex cell confused"),
   ("A cell with an owl's-eye inclusion",
    "An owl's eye inclusion, a large inclusion inside the nucleus of an enlarged cell, is the cytomegalovirus "
    "change. The pictured blood cell shows no such inclusion; it is a large atypical lymphocyte.",
    "cytomegalovirus inclusion confused")],
  ci(80, 66, 73, 79),
  img=IMG + "/l18-fig-13.jpg",
  alt="Stained blood smear showing a large cell with a dark purple irregular nucleus and wide pale blue "
      "cytoplasm, pointed at by two arrows and surrounded by round red blood cells.",
  slide="Slide 80"),

Q("Epstein-Barr virus", IO3,
  "Burkitt lymphoma, an Epstein-Barr virus B-cell malignancy in a child in central Africa, may be associated with "
  "which chronic coinfection?",
  ("Malaria",
   "Correct. Burkitt lymphoma is a B-cell malignancy that usually develops in the jaw and grossly swells the "
   "cheek. It affects children in central Africa and may be associated with chronic coinfections such as malaria. "
   "Epstein-Barr virus is oncogenic through such tumors."),
  [("Hepatitis D (delta agent)",
    "Coinfection with hepatitis D, the delta agent, can make hepatitis B disease more severe. Burkitt lymphoma "
    "is the Epstein-Barr virus tumor of central African children, which may be associated with chronic malaria.",
    "hepatitis B cofactor borrowed"),
   ("Adeno-associated virus",
    "Adeno-associated virus, a defective parvovirus, has been found with type 41 adenovirus in serious hepatitis "
    "in children. Burkitt lymphoma may be associated with chronic malaria coinfection.",
    "adenovirus hepatitis cofactor borrowed"),
   ("Human papillomavirus",
    "Human papillomavirus is linked to cervical and penile cancer. Burkitt lymphoma is a B-cell tumor of the jaw "
    "linked to Epstein-Barr virus, with chronic malaria as a possible coinfection.",
    "other oncogenic virus borrowed")],
  ci(6, 28, 77, 88, 94, 106)),

Q("Epstein-Barr virus", IO3,
  "Besides a family history, which risk factor is listed for nasopharyngeal carcinoma, an Epstein-Barr "
  "virus-associated tumor?",
  ("Eating salt-cured foods",
   "Correct. Nasopharyngeal carcinoma is a malignancy of epithelial cells occurring in adults, older Chinese and "
   "African men, those with a family history and those who eat salt-cured foods. It presents with a lump in the "
   "neck, hearing loss and a blocked nasal passage."),
  [("Playing contact sports",
    "Contact sports such as wrestling, basketball and rugby spread herpes gladiatorum, a herpes simplex skin "
    "infection. Nasopharyngeal carcinoma risk comes with family history and eating salt-cured foods.",
    "mat herpes risk borrowed"),
   ("Handling sheep or goats",
    "Handling sheep or goats transmits orf virus, a parapoxvirus that causes sores. The listed risk factors for "
    "nasopharyngeal carcinoma are older age in certain groups, family history and salt-cured foods.",
    "orf exposure borrowed"),
   ("Receiving a kidney transplant",
    "A renal transplant with immunosuppressive drugs is the setting for BK polyomavirus disease. Nasopharyngeal "
    "carcinoma, linked to Epstein-Barr virus, is tied to family history and eating salt-cured foods.",
    "BK setting borrowed")],
  ci(6, 54, 62, 77, 102)),

Q("Epstein-Barr virus", IO4,
  "A patient with acquired immunodeficiency syndrome develops hairy leukoplakia. Which herpesvirus is "
  "associated with it?",
  ("Epstein-Barr virus",
   "Correct. Anyone with an immune deficiency is highly susceptible to Epstein-Barr virus, and patients with "
   "acquired immunodeficiency syndrome develop hairy leukoplakia from it. Epstein-Barr virus infects lymphoid "
   "tissue and the salivary glands."),
  [("Human herpesvirus 8",
    "Human herpesvirus 8 gives patients with acquired immunodeficiency syndrome Kaposi sarcoma: small, painless "
    "discolored lumps, including in the mouth. Hairy leukoplakia in these patients is from Epstein-Barr virus.",
    "Kaposi virus confused"),
   ("Cytomegalovirus",
    "Cytomegalovirus gives patients with acquired immunodeficiency syndrome retinitis, mononucleosis and "
    "disseminated disease. Hairy leukoplakia belongs to Epstein-Barr virus.",
    "cytomegalovirus complication confused"),
   ("Herpes simplex virus type 1",
    "Herpes simplex virus type 1 gives oral cold sores and gingivostomatitis, and severe disseminated herpes in "
    "the immunodeficient. Hairy leukoplakia in acquired immunodeficiency syndrome is linked to Epstein-Barr "
    "virus.",
    "oral herpes confused")],
  c(60, 62, 74, 75, 77, 83)),

Q("Epstein-Barr virus", IO5,
  "What vaccine is available for Epstein-Barr virus?",
  ("Therapeutic, for related cancers",
   "Correct. There are no vaccines to prevent Epstein-Barr virus infection, but several therapeutic vaccines "
   "exist for Epstein-Barr virus-related cancers. Infectious mononucleosis itself is treated by relieving fever "
   "and sore throat."),
  [("Live attenuated, for prevention",
    "A live attenuated preventive vaccine exists for chickenpox and shingles, from varicella zoster virus. "
    "Epstein-Barr virus has no preventive vaccine, only therapeutic vaccines for its related cancers.",
    "varicella vaccine borrowed"),
   ("Inactivated oral, for recruits",
    "An inactivated oral vaccine against types 4 and 7, given to some military trainees, is the adenovirus "
    "vaccine. For Epstein-Barr virus there are only therapeutic vaccines for related cancers.",
    "adenovirus vaccine borrowed"),
   ("Yeast-derived, from surface antigen",
    "A vaccine made from surface antigen in cloned yeast prevents hepatitis B. Epstein-Barr virus has no "
    "preventive vaccine; several therapeutic vaccines target its related cancers.",
    "hepatitis B vaccine borrowed")],
  ci(6, 69, 79, 91, 94)),

# ============================================================== HUMAN HERPESVIRUSES 6 AND 7 (slides 81-83, chart 6)
Q("Human herpesviruses 6 and 7", IO4,
  "How does roseola from human herpesvirus 6 typically unfold in a baby?",
  ("Fever first, then a faint rash",
   "Correct. Roseola is an acute febrile disease of babies 2 to 12 months old: it begins with fever, followed by "
   "a faint maculopapular rash, and is usually self-limited. Adults infected with human herpesvirus 6 may instead "
   "get mono-like symptoms, lymphadenopathy and hepatitis."),
  [("A faint rash first, then fever",
    "This reverses the order. Roseola begins with fever, and the faint maculopapular rash follows: an acute febrile "
    "disease followed by rash.",
    "reversed sequence"),
   ("A cheek rash with low fever",
    "A low-grade fever with a rash on the cheeks, the slapped face, is fifth disease from parvovirus B19. Roseola "
    "starts with fever and is followed by a faint maculopapular rash.",
    "fifth disease borrowed"),
   ("Vesicles with malaise and fever",
    "Fluid-filled vesicles with malaise and fever are chickenpox, the primary varicella zoster infection. Roseola "
    "gives a faint maculopapular rash after the fever, not vesicles.",
    "chickenpox borrowed")],
  ci(6, 5, 81, 104)),

Q("Human herpesviruses 6 and 7", IO3,
  "Human herpesvirus 7 is closely related to human herpesvirus 6. How are these viruses tied to cancers such as "
  "Hodgkin lymphoma?",
  ("By association, not causation",
   "Correct. There is an association, not causation, between human herpesvirus 6 and Hodgkin lymphoma, oral "
   "carcinoma and certain T-cell leukemias. Human herpesvirus 7 is closely related, causes similar diseases such "
   "as roseola, and is also associated with cancers."),
  [("As their proven direct cause",
    "Causation is exactly what is not shown: the link between human herpesvirus 6 and these cancers is an "
    "association, not causation. Oncogenic links stated as such include Epstein-Barr virus with Burkitt "
    "lymphoma.",
    "association taken as cause"),
   ("By crossing the placenta",
    "Crossing the placenta to cause developmental defects is what teratogenic viruses, rubella and "
    "cytomegalovirus, do. Human herpesviruses 6 and 7 have only an association, not causation, with cancers.",
    "teratogenic confused with oncogenic"),
   ("They have no link to cancer",
    "A link is described: human herpesvirus 6 is associated with Hodgkin lymphoma, oral carcinoma and certain "
    "T-cell leukemias, and human herpesvirus 7 is also associated with cancers. The link is association, not "
    "causation.",
    "link denied")],
  ci(6, 28, 83)),

# ============================================================== HUMAN HERPESVIRUS 8 (slides 83-84, chart 6)
Q("Human herpesvirus 8", IO4,
  "The purple lesions shown are Kaposi sarcoma in the mouth of a patient with acquired immunodeficiency "
  "syndrome. Beyond the skin and mouth, where may this tumor spread?",
  ("To internal organs",
   "Correct. Kaposi sarcoma, linked with human herpesvirus 8, appears as small, painless, discolored lumps on "
   "the skin, but it may disseminate to internal organs. Human herpesvirus 8 spreads through saliva, sexual "
   "contact, blood transfusion and organ transplant."),
  [("Along a single dermatome",
    "A band of vesicles along one dermatome is shingles, reactivated varicella zoster virus following a sensory "
    "nerve. Kaposi sarcoma is not confined to a nerve path; it may disseminate to internal organs.",
    "shingles pattern borrowed"),
   ("To the retina, with blind spots",
    "Retinitis with blind spots is cytomegalovirus disease in acquired immunodeficiency syndrome. The spread "
    "described for Kaposi sarcoma is dissemination from the skin to internal organs.",
    "cytomegalovirus retinitis borrowed"),
   ("Into the jaw, swelling the cheek",
    "A tumor that develops in the jaw and grossly swells the cheek is Burkitt lymphoma, from Epstein-Barr virus, "
    "in central African children. Kaposi sarcoma may disseminate to internal organs.",
    "Burkitt site borrowed")],
  ci(84, 5, 6, 69, 77, 83),
  img=IMG + "/l18-fig-14.jpg",
  alt="Photograph of an open mouth showing dark purple patches on the inner cheek and gum beside the lower teeth.",
  slide="Slide 84"),

Q("Human herpesvirus 8", IO3,
  "Besides Kaposi sarcoma, human herpesvirus 8 may also be involved in which disorder?",
  ("Primary effusion lymphoma",
   "Correct. Human herpesvirus 8, the Kaposi sarcoma-associated virus, may also be involved in multiple myeloma, "
   "primary effusion lymphoma and some forms of Castleman disease."),
  [("Burkitt lymphoma",
    "Burkitt lymphoma, a B-cell tumor of the jaw in central African children, is the oncogenic link of "
    "Epstein-Barr virus. Human herpesvirus 8 may be involved in primary effusion lymphoma.",
    "Epstein-Barr tumor borrowed"),
   ("Nasopharyngeal carcinoma",
    "Nasopharyngeal carcinoma, a malignancy of epithelial cells tied to salt-cured foods and family history, is "
    "linked to Epstein-Barr virus. Human herpesvirus 8 may be involved in primary effusion lymphoma.",
    "Epstein-Barr tumor borrowed"),
   ("Hepatocellular carcinoma",
    "Hepatocellular carcinoma, liver cancer, is the oncogenic link of hepatitis B virus. Human herpesvirus 8 may "
    "be involved in primary effusion lymphoma, multiple myeloma and some forms of Castleman disease.",
    "hepatitis B tumor borrowed")],
  ci(6, 28, 77, 83, 87)),
]

CLUSTERS_C = [
    # Epstein-Barr blood findings: the smear picture's key (atypical lymphocyte) is restated in the count item
    (1, ["A college student has high fever, cervical", "A blood smear from a patient with an Epstein-Barr"]),
    # herpes simplex vs cytomegalovirus giant-cell pictures: each offers the other's cell as a distractor
    (1, ["Scrapings from the base of a genital vesicle", "A lung specimen shows an enlarged infected cell"]),
    # recurrence triggers: both items list the other's triggers in their explanations
    (1, ["Which stimulus can trigger a recurrence", "Which trigger is described for recurrent bouts"]),
    # latency vs chronic: the shared-feature and latency-contrast items key the same fact
    (1, ["Which feature do all members of the herpesvirus", "During latency, how does a herpesvirus"]),
    # vaccine status: each lists the other's vaccine as a distractor
    (1, ["Which vaccine is available against varicella", "What vaccine is available for Epstein-Barr"]),
]
