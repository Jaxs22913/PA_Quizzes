# -*- coding: utf-8 -*-
# Microbiology Exam 3 — "Webster Review" master exams, forms A and B, Lecture 18 (DNA Viruses of Medical
# Importance, Dr. Webster). Her review of this lecture: part 3 of the 13 Nov 2026 recording [29:00-32:12]. Her
# words only WEIGHT what is asked; every fact is from the visible slides (text + pictures), never speaker notes.
#
# COUNTS: 20 per form (40 total). Per form: 3.1 x2, 3.2 x1, 3.3 x2, 3.4 x1, 3.5 x1, 3.6 x4, 3.7 x1, 3.8 x1, 3.9 x1,
# 3.10 x1, 3.11 x1, 3.12 x4. Forms A and B ask different facts for each item.
#   3.6 herpesviruses: A = herpes simplex (whitlow picture), Epstein-Barr (Burkitt picture), herpes simplex type 1
#       (trigeminal latency), cytomegalovirus (retinitis in AIDS); B = human herpesvirus 6 (roseola picture),
#       herpes simplex type 2 (lumbosacral latency), varicella zoster (dermatome reactivation), Epstein-Barr
#       (infectious mononucleosis). Human herpesvirus 8 is covered by 3.11 in both forms (a 3.6 item on it in the
#       same form would have cued or duplicated the 3.11 key).
#   3.12 chart viruses: A = hepatitis B (low infective dose), adenovirus (types 4 and 7 military vaccine), JC
#       polyomavirus (progressive multifocal leukoencephalopathy), molluscum contagiosum; B = parvovirus B19
#       (slapped-cheek picture), human papillomavirus (plantar warts), BK polyomavirus (after renal transplant),
#       cowpox (hands, from cats that met rodents).
# PICTURES (each used once): A = wr3-fig-16 (whitlow, 3.6), wr3-fig-19 (Burkitt jaw, 3.6), wr3-fig-17 (Kaposi
#   lumps, 3.11); B = wr3-fig-20 (roseola rash, 3.6), wr3-fig-18 (slapped cheek, 3.12). All five viewed.
# CHART slides 4-7 (pictures of a table) all viewed; their rows are cited as "image on Slide N".
#
# HER WORDS VERSUS THE SLIDES / SLIDE CONFLICTS (held, never keyed):
#   - Spoken "the first VIRUS to be eliminated by vaccination" vs chart (slide 4) "First DISEASE to be eliminated by
#     vaccine": neither wording is keyed; no "first eliminated" item at all (also a history/date area).
#   - Chart (slide 5) HSV-2 row "Association with Cervical and Penile cancer" vs slide 28 "Papilloma viruses—Cervical
#     and penile cancer": B 3.4 (repaired) keys papillomavirus from slide 28 and never offers herpes simplex (any
#     type) as an option, so the chart's HSV-2 association cannot make a second answer.
#   - Chart (slide 4) JYNNEOS "became available April 2024" vs slide 44 "approved September 24, 2019": no date items;
#     JYNNEOS is keyed only as a vaccine against mpox (slides 4, 44, 52). Slide 44 calls it "live virus"; not used.
#   - Chart (slide 4) "Vaccinia" row lists the disease as Cowpox, while slide 43 makes vaccinia the smallpox vaccine
#     and slide 53 is "Cowpox in humans": the cowpox item keys "Cowpox virus" and never offers vaccinia as an option.
#   - Chart (slide 6) Burkitt lymphoma "primarily affects African boys 5-7" vs slide 77 "central African children 5-7
#     years old": the stem says only "a child in central Africa".
#   - Chart (slide 7) HPV "Vaccines available for Genital Warts" vs slide 99 "Two effective HPV vaccines": vaccine
#     wording not keyed.
# HELD: dates, years, historical people (slides 34-38, 44-45), dosing (JYNNEOS 2 doses, hepatitis B 3 doses),
#   case counts and outbreak tallies (47, 49-51), prevalence percentages, incubation numbers as keys, the treatment
#   drugs (not on her list), "most common STD" (slides 46 and 97 both claim a "most common" sexually transmitted
#   role, for molluscum and genital warts).
# SPELLING: chart "sphenomegaly" = splenomegaly; "Hairy leukopakia" (77) = hairy leukoplakia; "occular" = ocular;
#   "Cytomegaloiivrus" = cytomegalovirus. Abbreviations written out (AIDS, HIV, HSV, VZV, CMV, EBV, HHV, HPV, PML).
# KEYS AUTHORED AT INDEX 0 (c=0); positions are permuted by the renderer.

SRC = "Lecture 18  Dr. Webster -  DNA viruses of medical importance.pptx"
LEC = 18
IMG = "micro-exam-3-quiz-images"


def cl(*n):
    return f"{SRC}, Slide {n[0]}" if len(n) == 1 else f"{SRC}, Slides " + ", ".join(map(str, n[:-1])) + " and " + str(n[-1])


def ci(img, *n):
    return (cl(*n) + f" and image on Slide {img}") if n else f"{SRC}, image on Slide {img}"


IO = {
    1: "1 — Recall the steps of DNA virus replication.",
    2: ("2 — Compare and contrast the characteristics of a lytic viral infection versus a persistent chronic or "
        "persistent latent infection."),
    3: "3 — Differentiate between oncogenic and teratogenic viruses.",
    4: ("4 — Compare and contrast the morphology, medium, laboratory tests, biochemical reactions, diseases, clinical "
        "manifestations, methods of treatment, and prevention of DNA viruses of medical importance."),
    5: ("5 — Compare and contrast the mode of transmission, clinical manifestations, and availability of a vaccine "
        "for DNA viruses of medical importance."),
}


def Q(item, tier, form, topic, io, q, key, wrongs, cite, **extra):
    """key = (text, explanation); wrongs = [(text, explanation, misconception) x3]"""
    d = dict(lecture=LEC, item=item, tier=tier, form=form, topic=topic, io=IO[io], q=q,
             opts=[[key[0], key[1]]] + [[w[0], w[1]] for w in wrongs],
             mis={w[0]: w[2] for w in wrongs}, c=0, cite=cite)
    d.update(extra)
    return d


POOL = [

# ============================================================ 3.1 (cold) animal virus versus phage replication
Q("3.1", "cold", "A", "Animal virus entry versus phage penetration", 1,
  "How does an animal virus get its genetic material into a host cell, unlike a bacteriophage?",
  ("The whole virion is engulfed",
   "Correct: animal viruses differ from phages in that the entire virion is engulfed (taken into a vesicle by "
   "endocytosis) and must then be uncoated to free its genetic material. A phage instead breaches the bacterial "
   "wall and injects only its DNA."),
  [("Its tail injects only the DNA",
    "Injection is the phage method: in the lytic cycle a phage uses viral lysozyme and a tail pin mechanism to breach "
    "the wall and inject its DNA into the bacterium. An animal virus is engulfed whole and then uncoated.",
    "gives the animal virus the phage's tail-injection penetration"),
   ("Its DNA integrates as a prophage",
    "Integration as a prophage is what happens after entry in the lysogenic phage cycle, when the viral DNA joins the "
    "bacterial chromosome. It is not a way of entering a cell; an animal virus enters by being engulfed whole.",
    "confuses the lysogenic integration step with entry"),
   ("It binds pili without lysozyme",
    "Attaching to pili or walls without lysozyme, through capsid-receptor protein compatibility, is how filamentous "
    "phages of the chronic cycle enter bacteria. An animal virus is instead engulfed whole into the host cell.",
    "gives the animal virus the filamentous (chronic-cycle) phage entry")],
  cl(14, 16, 22, 23)),

Q("3.1", "cold", "A", "Phage cycles: lysogenic prophage", 1,
  ("In one bacteriophage cycle, the viral DNA joins the bacterial chromosome and is copied along with it for many "
   "generations until a shock releases it. Which cycle is this?"),
  ("Lysogenic cycle",
   "Correct: in the lysogenic cycle the viral DNA integrates into the bacterial host chromosome as a prophage instead "
   "of shutting down the bacterium's metabolism; prophage bacteria persist for generations until a shock induces a "
   "lytic cycle."),
  [("Lytic cycle",
    "The lytic cycle is a rapid takeover: the phage turns off the bacterium's metabolism, makes many copies and bursts "
    "the cell wall with viral lysozyme. Integration into the chromosome for many generations is the lysogenic cycle.",
    "confuses rapid takeover and lysis with integration"),
   ("Chronic cycle",
    "The chronic cycle belongs to filamentous phages, whose virions are extruded continuously without lysing the "
    "host, only slowing its growth. DNA that integrates into the chromosome as a prophage marks the lysogenic cycle.",
    "confuses continuous extrusion with integration"),
   ("Latent cycle",
    "Latency describes animal herpesviruses, whose DNA sits in the nucleus as an episome that is not integrated. A "
    "phage whose DNA integrates into the bacterial chromosome as a prophage is in the lysogenic cycle.",
    "borrows the animal-virus latency term for a phage cycle")],
  cl(13, 15, 18, 26)),

Q("3.1", "cold", "B", "Uncoating: the step animal viruses need", 1,
  "Which step must an animal virus carry out, that a bacteriophage does not, to free its genetic material inside the host cell?",
  ("Uncoating",
   "Correct: because the entire animal virion is engulfed, it requires uncoating to release its genetic material, "
   "driven by the pH difference between the cytoplasm and the extracellular fluid. A phage injects bare DNA, so it "
   "has nothing to uncoat."),
  [("Adsorption",
    "Adsorption, attaching to the host's surface, is shared: phages adsorb to the bacterium and animal viruses attach "
    "by binding spikes to cell receptors. The step only the animal virus needs is uncoating after it is engulfed.",
    "picks a step both kinds of virus perform"),
   ("Maturation",
    "Maturation, completing the new virions, happens in phage and animal virus cycles alike. The step that frees an "
    "engulfed animal virus's genetic material, and that phages lack, is uncoating.",
    "picks a late step both kinds of virus perform"),
   ("Assembly",
    "Assembly, putting new virions together from replicated nucleic acid and capsid parts, occurs in both phage and "
    "animal virus cycles. The animal-only step that releases the genetic material is uncoating.",
    "picks a late step both kinds of virus perform")],
  cl(14, 22, 23)),

Q("3.1", "cold", "B", "Phage cycles: chronic cycle", 1,
  ("A filamentous bacteriophage releases new virions from its bacterial host continuously without lysing it; the "
   "host simply grows more slowly. Which cycle is this?"),
  ("Chronic cycle",
   "Correct: in the chronic cycle filamentous phages, flexible rods with single-stranded DNA, replicate and assemble "
   "virions that are extruded from the host without lysing it, only slowing its growth. Host and phage form a "
   "cooperative arrangement (toxins, biofilms)."),
  [("Lytic cycle",
    "The lytic cycle ends in destruction of the host: viral lysozyme causes the cell wall to burst and release the "
    "new virions. Virions extruded without lysis, with only slowed growth, mark the chronic cycle.",
    "misses that the host survives here"),
   ("Lysogenic cycle",
    "In the lysogenic cycle the DNA integrates as a prophage and no virions are made until a shock induces a lytic "
    "cycle. Continuous release of virions without lysis is the chronic cycle of filamentous phages.",
    "confuses dormant integration with continuous release"),
   ("Budding cycle",
    "Release by budding is how animal viruses leave the cell, picking up an envelope from the membrane. Filamentous "
    "phages releasing virions from bacteria without lysis are in the chronic cycle.",
    "borrows animal-virus budding for a phage")],
  cl(13, 14, 16, 18, 22)),

# ============================================================ 3.2 (cold) animal virus structure, envelope
Q("3.2", "cold", "A", "Origin of the viral envelope", 4,
  "Where does an enveloped animal virus get its envelope?",
  ("From a host membrane as it buds",
   "Correct: the envelope is obtained during budding of the virus through a cell membrane; enveloped viruses bud off "
   "the membrane carrying away an envelope with the spikes. The envelope helps the virus evade the immune system."),
  [("From capsid proteins it makes",
    "Capsid proteins build the capsid, the protein coat that encloses and protects the nucleic acid in every virus. "
    "The envelope is a separate outer layer taken from a host cell membrane during budding.",
    "confuses the capsid with the envelope"),
   ("From the bacterial cell wall",
    "Bacterial cell walls are what phages breach with lysozyme or burst at release; they do not supply animal virus "
    "envelopes. An animal virus takes its envelope from a host cell membrane as it buds out.",
    "mixes in the phage-bacterium relationship"),
   ("From the viral matrix layer",
    "The matrix is a layer of the virion itself, drawn beneath the envelope and present even in naked nucleocapsid "
    "viruses. The envelope is a separate outer layer obtained from a host cell membrane as the virus buds out.",
    "confuses the matrix layer with the envelope")],
  ci(10, 9, 22)),

Q("3.2", "cold", "B", "Structure common to all viruses", 4,
  "Which structure do all viruses have?",
  ("A protein capsid",
   "Correct: all viruses have a capsid, a protein coat (helical, icosahedral or complex) that encloses and protects "
   "the nucleic acid. A naked nucleocapsid virus is just capsid plus nucleic acid, with no envelope at all."),
  [("A lipid envelope",
    "An envelope is optional: animal viruses may have one, obtained by budding through a cell membrane, and naked "
    "nucleocapsid viruses such as adenoviruses lack it. The structure every virus has is the protein capsid.",
    "treats an optional envelope as universal"),
   ("Surface spikes",
    "Spikes are optional too: animal viruses may have an envelope or spikes, and a naked nucleocapsid virus shows "
    "neither. What every virus has is a capsid, the protein coat around its nucleic acid.",
    "treats optional spikes as universal"),
   ("Both DNA and RNA",
    "A virus contains genetic material that is DNA or RNA, not both; animal viruses are even classified by their "
    "nucleic acid. The structure common to all viruses is the protein capsid that encloses it.",
    "thinks viruses carry both nucleic acids")],
  ci(10, 8, 9, 93)),

# ============================================================ 3.3 (cold) acute, chronic, latent infections
Q("3.3", "cold", "A", "Example of a persistent chronic infection", 2,
  "Which virus is an example of a persistent chronic infection, detectable in tissue and multiplying slowly for years?",
  ("Human immunodeficiency virus",
   "Correct: in a chronic infection the virus is detectable in tissue samples and multiplies at a slow rate with mild "
   "or absent symptoms; human immunodeficiency virus and hepatitis B virus are the examples, and this may involve "
   "integration into the host chromosome."),
  [("Influenza virus",
    "Influenza (flu), like colds, is an acute viral infection: a rapid course with a lytic cycle. A persistent "
    "chronic infection, slowly multiplying and detectable for years, is the pattern of human immunodeficiency virus.",
    "files an acute infection as chronic"),
   ("Herpes simplex virus type 1",
    "Herpesviruses cause persistent latent infections: after a lytic cycle the virus is dormant and generally not "
    "detectable, then can reactivate. Detectable, slowly multiplying virus marks a chronic infection such as human "
    "immunodeficiency virus.",
    "confuses latent with chronic persistence"),
   ("Epstein-Barr virus",
    "Epstein-Barr virus is a herpesvirus, so it shows latency: dormancy in B cells with reactivation, its DNA an "
    "episome. A virus detectable in tissue and slowly multiplying is chronic, as human immunodeficiency virus is.",
    "confuses latent with chronic persistence")],
  cl(26, 55, 75)),

Q("3.3", "cold", "A", "Latent infection: dormancy and reactivation", 2,
  ("After an initial lytic cycle, a virus becomes dormant, is generally not detectable and causes no symptoms, but "
   "later reactivates to cause recurrent infection. Which type of infection is this?"),
  ("Persistent latent infection",
   "Correct: a latent infection follows a lytic cycle with a dormant phase in which the virus is generally not "
   "detectable and causes no symptoms; it can reactivate and cause recurrent infections, as herpesviruses do."),
  [("Persistent chronic infection",
    "In a chronic infection the virus stays detectable in tissue samples, multiplying at a slow rate, as with human "
    "immunodeficiency virus and hepatitis B. A dormant, undetectable virus that later reactivates is latent.",
    "misses that chronic virus remains detectable and active"),
   ("Acute infection",
    "An acute infection has a rapid course with a lytic cycle, such as a cold or flu, and does not go dormant. "
    "Dormancy with later reactivation and recurrence is a persistent latent infection.",
    "misses the dormant phase"),
   ("Lysogenic infection",
    "Lysogeny is a bacteriophage cycle in which DNA integrates into a bacterial chromosome as a prophage. In human "
    "viral disease, a dormant, undetectable virus that later reactivates causes a persistent latent infection.",
    "borrows the phage term for an animal-virus infection")],
  cl(15, 26, 55)),

Q("3.3", "cold", "B", "Example of an acute viral infection", 2,
  "Which of these is an acute viral infection, with a rapid lytic course?",
  ("Influenza",
   "Correct: many viral infections have a rapid course with a lytic cycle and are termed acute; colds and flu "
   "(influenza) are the examples. Persistent infections, by contrast, last many years or a lifetime."),
  [("Hepatitis B",
    "Hepatitis B virus causes a persistent chronic infection: the liver continuously seeds the blood with virus, and "
    "it can stay detectable for years. Influenza, a rapid lytic infection, is the acute example.",
    "files a chronic infection as acute"),
   ("Herpes simplex",
    "Herpes simplex virus causes a persistent latent infection: it lies dormant in sensory ganglia and reactivates to "
    "cause recurrent lesions. Influenza, with a rapid lytic course, is the acute example.",
    "files a latent infection as acute"),
   ("Human immunodeficiency virus infection",
    "Human immunodeficiency virus causes a persistent chronic infection, with virus detectable and slowly multiplying "
    "for years. A rapid lytic course belongs to acute infections such as influenza and colds.",
    "files a chronic infection as acute")],
  cl(26, 59, 87)),

Q("3.3", "cold", "B", "Latency: herpesvirus DNA as an episome", 2,
  "During latency, in what form does herpesvirus DNA persist in the host cell?",
  ("As an episome in the nucleus",
   "Correct: in a latent herpesvirus infection the viral DNA is an episome, in the nucleus but not integrated into "
   "the host chromosome; it is generally not detectable and can reactivate to cause recurrent infection."),
  [("Integrated into a chromosome",
    "Integration into the host chromosome is noted for chronic infections such as human immunodeficiency virus and "
    "hepatitis B, and for phage prophages. Latent herpesvirus DNA is an episome: in the nucleus but not integrated.",
    "confuses latent episomes with chronic or prophage integration"),
   ("As free virus in the blood",
    "Continuously seeding the blood with virus is hepatitis B virus's chronic pattern from the liver. Latent "
    "herpesvirus is generally not detectable; its DNA sits as an episome in the nucleus.",
    "confuses latency with chronic viremia"),
   ("In cytoplasmic factory areas",
    "Cytoplasmic factory areas are where poxviruses multiply. Herpesviruses replicate within the nucleus, and in "
    "latency their DNA stays there as an episome, not integrated into the chromosome.",
    "confuses herpesvirus latency with poxvirus replication")],
  cl(26, 32, 55, 87)),

# ============================================================ 3.4 (cold) oncogenic
Q("3.4", "cold", "A", "Oncogenic virus example: hepatitis B", 3,
  "Which persistent virus is oncogenic, linked to hepatic carcinoma?",
  ("Hepatitis B virus",
   "Correct: some persistent viruses are oncogenic, and hepatitis B is paired with hepatic carcinoma. Hepatitis B "
   "can become chronic, increases the risk of hepatocellular carcinoma and may lead to cirrhosis."),
  [("Adenovirus",
    "Adenoviruses are oncogenic in animals, not in humans; they cause acute infections such as colds, pharyngitis "
    "and conjunctivitis. The persistent virus linked to hepatic carcinoma is hepatitis B virus.",
    "assumes animal oncogenicity applies to humans"),
   ("JC polyomavirus",
    "Polyomaviruses induce tumors in experimental animals; in people, JC virus causes progressive multifocal "
    "leukoencephalopathy in the immunosuppressed. The persistent virus linked to hepatic carcinoma is hepatitis B.",
    "assumes animal tumor induction means human liver cancer"),
   ("Cytomegalovirus",
    "Cytomegalovirus is a teratogenic virus that crosses the placenta, and it causes severe disease in transplant "
    "and immunocompromised patients; it is not the hepatic carcinoma virus. That pairing is hepatitis B.",
    "swaps a teratogenic virus for an oncogenic one")],
  ci(6, 28, 72, 87, 93, 101)),

Q("3.4", "cold", "B", "Oncogenic viruses: cervical and penile cancer", 3,
  "Some persistent viruses are oncogenic. Which of these is linked to cervical and penile cancer?",
  ("Human papillomavirus",
   "Correct: papilloma viruses are on the list of persistent oncogenic viruses, linked to cervical and penile cancer. "
   "Nine types increase the risk of reproductive cancer, and a Pap smear screens women for abnormal cervical cells."),
  [("JC polyomavirus",
    "Polyomaviruses induce tumors in experimental animals; in people, JC virus causes progressive multifocal "
    "leukoencephalopathy, an often fatal brain infection. The cervical and penile cancer link is papillomavirus.",
    "assumes animal tumor induction means a human cancer"),
   ("Cytomegalovirus",
    "Cytomegalovirus is a teratogenic virus: it crosses the placenta and causes developmental defects such as "
    "microcephaly. The persistent virus linked to cervical and penile cancer is human papillomavirus.",
    "swaps a teratogenic virus for an oncogenic one"),
   ("Adenovirus",
    "Adenoviruses are oncogenic in animals, not in humans, and cause acute colds, pharyngitis and conjunctivitis. "
    "The virus linked to cervical and penile cancer is human papillomavirus.",
    "assumes animal oncogenicity carries over to people")],
  cl(28, 72, 93, 96, 99, 101, 102)),

# ============================================================ 3.5 (cold) teratogenic
Q("3.5", "cold", "A", "Teratogenic: what the term means", 3,
  ("A virus that crosses the placenta and causes developmental disturbances and permanent defects in the fetus is "
   "described by which term?"),
  ("Teratogenic",
   "Correct: several viruses can cross the placenta causing developmental disturbances and permanent defects; these "
   "are teratogenic, and rubella and cytomegalovirus are the examples. Newborns with cytomegalovirus may show "
   "microcephaly."),
  [("Oncogenic",
    "Oncogenic viruses are persistent viruses linked to cancer, such as hepatitis B with hepatic carcinoma. A virus "
    "that crosses the placenta and causes permanent developmental defects is teratogenic.",
    "confuses teratogenic with oncogenic"),
   ("Latent",
    "Latent describes a virus that goes dormant after a lytic cycle and later reactivates, as herpesviruses do. "
    "Crossing the placenta to cause developmental defects is what makes a virus teratogenic.",
    "confuses teratogenic with latent"),
   ("Zoonotic",
    "Zoonoses are infections humans get from animals, often through vectors, such as West Nile fever and hantavirus. "
    "Crossing the placenta to cause permanent defects in development is teratogenic.",
    "confuses teratogenic with zoonotic")],
  cl(24, 26, 28, 72)),

Q("3.5", "cold", "B", "Teratogenic virus example: rubella", 3,
  "Which virus is teratogenic, able to cross the placenta and cause permanent developmental defects?",
  ("Rubella virus",
   "Correct: rubella and cytomegalovirus are the teratogenic viruses, able to cross the placenta and cause "
   "developmental disturbances and permanent defects in the fetus. Rubella is also one of the rash diseases of "
   "childhood."),
  [("Epstein-Barr virus",
    "Epstein-Barr virus is an oncogenic virus, linked to Burkitt lymphoma, and causes infectious mononucleosis; it is "
    "not one of the teratogenic viruses. Rubella crosses the placenta to cause permanent defects.",
    "swaps an oncogenic virus for a teratogenic one"),
   ("Adenovirus",
    "Adenoviruses cause acute infections spread by respiratory and ocular secretions, such as colds, conjunctivitis "
    "and infantile gastroenteritis. The teratogenic viruses are rubella and cytomegalovirus.",
    "picks an acute respiratory virus"),
   ("Molluscum contagiosum virus",
    "Molluscum contagiosum is a poxvirus spread by direct contact and fomites, causing small, smooth, waxy lesions "
    "that are normally self-limiting. The teratogenic viruses are rubella and cytomegalovirus.",
    "picks a skin poxvirus")],
  cl(28, 46, 75, 77, 93, 104)),

# ============================================================ 3.6 (cold) herpesviruses 1-8 — form A
Q("3.6", "cold", "A", "Herpetic whitlow (picture)", 5,
  ("An adult has the extremely painful, itchy lesion shown on one finger, which began at a break in the skin. "
   "Which virus causes it?"),
  ("Herpes simplex virus",
   "Correct: this is herpetic whitlow. Herpes simplex type 1 or type 2 can penetrate a break in the skin and cause a "
   "localized infection, usually on one finger, that is extremely painful and itchy."),
  [("Human papillomavirus",
    "Human papillomavirus causes common seed warts on the fingers, but these are painless, elevated, rough growths. "
    "An extremely painful, itchy lesion on one finger after a break in the skin is herpetic whitlow from herpes simplex.",
    "confuses a painless finger wart with a painful whitlow"),
   ("Cowpox virus",
    "Cowpox in humans is rare, usually pocks confined to the hands, caught from cats that interacted with rodents or "
    "after traumatic injury, and is not described as extremely painful and itchy. That pain and itch at a skin break "
    "on one finger is the herpetic whitlow picture.",
    "fixes on hand lesions and picks the poxvirus"),
   ("Molluscum contagiosum virus",
    "Molluscum contagiosum causes small, smooth, waxy lesions, usually in the genital area and thighs, normally "
    "self-limiting. An extremely painful, itchy lesion on one finger is herpetic whitlow from herpes simplex.",
    "picks another skin virus")],
  ci(61, 5, 46, 53, 60, 97),
  img=IMG + "/wr3-fig-16.jpg",
  alt=("Close-up of a single finger on a green cloth: the fingertip and the skin around the nail are swollen, with "
       "dark red-purple discoloration and grouped, partly broken, fluid-filled areas")),

Q("3.6", "cold", "A", "Epstein-Barr virus and Burkitt lymphoma (picture)", 4,
  ("A child in central Africa has the jaw swelling shown, caused by a B-cell malignancy. Which virus is associated "
   "with this tumor?"),
  ("Epstein-Barr virus",
   "Correct: this is Burkitt lymphoma, a B-cell malignancy that usually develops in the jaw and grossly swells the "
   "cheek in central African children aged 5 to 7; it is associated with Epstein-Barr virus, an oncogenic herpesvirus."),
  [("Human herpesvirus 8",
    "Human herpesvirus 8 is linked with Kaposi sarcoma, small painless discolored lumps on the skin, common in patients "
    "with acquired immunodeficiency syndrome. A B-cell tumor swelling a child's jaw is Burkitt lymphoma from "
    "Epstein-Barr virus.",
    "swaps one oncogenic herpesvirus for another"),
   ("Hepatitis B virus",
    "Hepatitis B virus is oncogenic for the liver, linked to hepatic (hepatocellular) carcinoma. A B-cell malignancy "
    "grossly swelling a child's jaw is Burkitt lymphoma, associated with Epstein-Barr virus.",
    "picks the liver-cancer virus"),
   ("Adenovirus",
    "Adenoviruses are oncogenic in animals but not in humans; they cause colds, pharyngitis and conjunctivitis. The "
    "jaw-swelling B-cell tumor of central African children is Burkitt lymphoma from Epstein-Barr virus.",
    "assumes animal oncogenicity applies to humans")],
  ci(76, 6, 28, 77, 87, 93),
  img=IMG + "/wr3-fig-19.jpg",
  alt="Photograph of a young child's face with a large, firm swelling of one side of the lower face and jaw"),

Q("3.6", "cold", "A", "Herpes simplex type 1 latency site", 4,
  "After a first infection, where does herpes simplex virus type 1 remain latent?",
  ("Trigeminal ganglion",
   "Correct: herpes simplex multiplies in sensory neurons and moves to the ganglia; type 1 enters the fifth cranial "
   "nerve and is latent in the trigeminal ganglion. Fever, ultraviolet radiation, stress or injury can trigger "
   "recurrence."),
  [("Lumbosacral ganglia",
    "The lumbosacral spinal nerve trunk ganglia are where herpes simplex type 2 goes, fitting its genital lesions. "
    "Type 1, with its oral and facial lesions, enters the fifth cranial nerve and is latent in the trigeminal ganglion.",
    "swaps type 2's latency site for type 1's"),
   ("B lymphocytes",
    "Dormancy in B cells, with later reactivation, belongs to Epstein-Barr virus. Herpes simplex type 1 stays latent "
    "in a sensory ganglion, the trigeminal ganglion of the fifth cranial nerve.",
    "swaps Epstein-Barr's dormancy site in"),
   ("Kidney and bladder lining",
    "Lying dormant in the kidney and the lining of the ureters and bladder describes BK polyomavirus, which flares "
    "after renal transplant. Herpes simplex type 1 is latent in the trigeminal ganglion.",
    "swaps BK virus's dormancy site in")],
  cl(59, 75, 102)),

Q("3.6", "cold", "A", "Cytomegalovirus retinitis in acquired immunodeficiency syndrome", 4,
  ("A patient with acquired immunodeficiency syndrome develops retinitis and blind spots. Which herpesvirus "
   "most likely causes it?"),
  ("Cytomegalovirus",
   "Correct: in patients with acquired immunodeficiency syndrome, cytomegalovirus causes cytomegalovirus "
   "mononucleosis, disseminated disease and retinitis, and blind spots are among its manifestations; severe "
   "complications occur in immunocompromised hosts."),
  [("Herpes simplex virus type 1",
    "Herpes simplex type 1 affects the eye as herpetic keratitis, an inflammation with a gritty feeling, "
    "conjunctivitis, sharp pain and light sensitivity, not retinitis. Retinitis in a patient with acquired immunodeficiency syndrome is "
    "cytomegalovirus.",
    "confuses herpetic keratitis with retinitis"),
   ("Epstein-Barr virus",
    "In patients with acquired immunodeficiency syndrome, Epstein-Barr virus is linked to hairy leukoplakia, and it "
    "also causes infectious mononucleosis and Burkitt lymphoma. Retinitis in acquired immunodeficiency syndrome is cytomegalovirus.",
    "picks another acquired immunodeficiency syndrome-associated herpesvirus"),
   ("Human herpesvirus 8",
    "Human herpesvirus 8 is linked with Kaposi sarcoma, the small painless discolored skin lumps common in patients "
    "with acquired immunodeficiency syndrome. Retinitis with blind spots in a patient with acquired immunodeficiency syndrome is cytomegalovirus.",
    "picks another acquired immunodeficiency syndrome-associated herpesvirus")],
  ci(5, 60, 74, 77, 83)),

# ============================================================ 3.6 (cold) herpesviruses — form B
Q("3.6", "cold", "B", "Roseola: human herpesvirus 6 (picture)", 4,
  ("A 12-month-old had an acute febrile illness, followed by the faint rash shown. Which virus causes this "
   "disease?"),
  ("Human herpesvirus 6",
   "Correct: this is roseola, an acute febrile disease of babies 2 to 12 months old that begins with fever followed "
   "by a faint maculopapular rash and is usually self-limited. Human herpesvirus 6 causes it, spread by close "
   "contact with saliva; the closely related herpesvirus 7 causes similar diseases."),
  [("Varicella zoster virus",
    "Varicella zoster causes chickenpox, with characteristic filled vesicles, malaise and fever, and later shingles. "
    "A faint rash following fever in a 12-month-old is roseola, from human herpesvirus 6.",
    "confuses a vesicular rash with a faint one"),
   ("Parvovirus B19",
    "Parvovirus B19 causes fifth disease, a slapped-face rash on the cheeks with low-grade fever. A faint rash on the "
    "trunk after a febrile illness in a baby is roseola, from human herpesvirus 6.",
    "confuses two childhood rash diseases"),
   ("Cytomegalovirus",
    "Cytomegalovirus is mostly asymptomatic, but in newborns it can bring an enlarged liver and spleen, jaundice, "
    "capillary bleeding and microcephaly. A faint rash after fever in a baby is roseola, from human herpesvirus 6.",
    "picks another herpesvirus of infancy")],
  ci(82, 6, 7, 57, 68, 72, 81, 83, 104),
  img=IMG + "/wr3-fig-20.jpg",
  alt="Photograph of a baby's chest and abdomen covered by a faint, blotchy pink rash of small flat spots"),

Q("3.6", "cold", "B", "Herpes simplex type 2 latency site", 4,
  "After a first genital infection, where does herpes simplex virus type 2 remain latent?",
  ("Lumbosacral ganglia",
   "Correct: herpes simplex multiplies in sensory neurons and moves to the ganglia; type 2 enters the lumbosacral "
   "spinal nerve trunk ganglia. Recurrent genital bouts are triggered by menstruation, stress and concurrent "
   "bacterial infection."),
  [("Trigeminal ganglion",
    "The trigeminal ganglion, reached through the fifth cranial nerve, is where herpes simplex type 1 lies latent, "
    "fitting its cold sores. Type 2, with genital lesions, is latent in the lumbosacral spinal nerve trunk ganglia.",
    "swaps type 1's latency site for type 2's"),
   ("B lymphocytes",
    "Dormancy in B cells, with later reactivation, is the latency of Epstein-Barr virus. Herpes simplex type 2 stays "
    "latent in sensory ganglia of the lumbosacral spinal nerve trunk.",
    "swaps Epstein-Barr's dormancy site in"),
   ("Liver cells",
    "Hepatitis B virus multiplies exclusively in the liver, continuously seeding the blood in a chronic infection. "
    "Herpes simplex type 2 is latent in the lumbosacral spinal nerve trunk ganglia.",
    "swaps hepatitis B's site in")],
  cl(59, 63, 75, 87)),

Q("3.6", "cold", "B", "Varicella zoster reactivation: shingles", 4,
  "When latent varicella zoster virus reactivates as shingles, where do the painful vesicles appear?",
  ("Along a dermatome",
   "Correct: reactivation of varicella zoster results in shingles, with painful vesicles localized to distinctive "
   "areas of skin along specific nerve pathways (dermatomes); inflammation of the ganglia sends pain down the "
   "nerve pathways. It is more common in older patients."),
  [("At the lip margin",
    "Vesicles at the mucocutaneous junction of the lips are herpes labialis, the most common recurrent herpes "
    "simplex type 1 infection. Reactivated varicella zoster appears along a dermatome as shingles.",
    "confuses cold sores with shingles"),
   ("Over the whole body",
    "Total body coverage in 24 hours, starting on the face, is the smallpox rash. Shingles from reactivated "
    "varicella zoster is localized to a dermatome, a band of skin along one nerve pathway.",
    "confuses the generalized smallpox rash with shingles"),
   ("On the genitals and thighs",
    "Small, smooth, waxy lesions in the genital area and thighs are molluscum contagiosum. Reactivated varicella "
    "zoster produces shingles, with painful vesicles along a dermatome.",
    "confuses molluscum's distribution with shingles")],
  ci(5, 41, 46, 60, 68, 69)),

Q("3.6", "cold", "B", "Epstein-Barr virus: infectious mononucleosis", 5,
  ("A college student has sore throat, high fever, cervical lymphadenopathy and splenomegaly, caught through "
   "contact with saliva. Which herpesvirus causes this?"),
  ("Epstein-Barr virus",
   "Correct: Epstein-Barr virus spreads by direct oral contact and saliva, and in industrialized countries the "
   "college-age population is vulnerable to infectious mononucleosis: sore throat, high fever, cervical "
   "lymphadenopathy and splenomegaly."),
  [("Varicella zoster virus",
    "Varicella zoster spreads by respiratory droplets and fluid from skin lesions and causes chickenpox, with "
    "characteristic vesicles. Sore throat, fever, cervical nodes and splenomegaly in a college student is infectious "
    "mononucleosis from Epstein-Barr virus.",
    "misses the absence of a vesicular rash"),
   ("Herpes simplex virus type 2",
    "Herpes simplex type 2 causes genital herpes, with groin swelling and clusters of sensitive genital vesicles. "
    "Sore throat, fever, cervical lymphadenopathy and splenomegaly spread by saliva is infectious mononucleosis from "
    "Epstein-Barr virus.",
    "picks a sexually spread herpesvirus"),
   ("Human herpesvirus 8",
    "Human herpesvirus 8 is linked with Kaposi sarcoma, small painless discolored skin lumps in patients with "
    "acquired immunodeficiency syndrome. A college student with sore throat, fever and splenomegaly has infectious "
    "mononucleosis from Epstein-Barr virus.",
    "picks a tumor-linked herpesvirus")],
  ci(6, 63, 68, 75, 83)),

# ============================================================ 3.7 (cold) poxvirus reproduction
Q("3.7", "cold", "A", "Poxviruses multiply in the cytoplasm", 1,
  "Unlike most DNA viruses, where in the host cell do poxviruses multiply?",
  ("In cytoplasmic factory areas",
   "Correct: poxviruses, the largest and most complex animal viruses, multiply in the cytoplasm in factory areas, "
   "with specificity for the cytoplasm of epidermal cells. Most DNA viruses, by contrast, are budded off the nucleus."),
  [("Within the host cell nucleus",
    "Most DNA viruses replicate in and are budded off the nucleus, and herpesviruses replicate within the nucleus. "
    "Poxviruses are the exception: they multiply in factory areas of the cytoplasm.",
    "applies the usual DNA-virus rule to poxviruses"),
   ("Integrated in a chromosome",
    "Integration into a host chromosome is noted for chronic infections such as hepatitis B and for phage prophages; "
    "it is not where poxviruses multiply. Poxviruses replicate in cytoplasmic factory areas.",
    "confuses integration with replication site"),
   ("As an episome in the nucleus",
    "An episome in the nucleus is the latent form of herpesvirus DNA, not a site of multiplication. Poxviruses "
    "multiply outside the nucleus, in factory areas of the cytoplasm.",
    "confuses herpes latency with poxvirus replication")],
  cl(24, 26, 32, 55)),

Q("3.7", "cold", "B", "Poxviruses: largest and most complex", 4,
  "Which group contains the largest and most complex animal viruses, with the largest genome of all viruses?",
  ("Poxviruses",
   "Correct: poxviruses are the largest and most complex animal viruses and have the largest genome of all viruses; "
   "they are double-stranded DNA viruses that, unusually, multiply in the cytoplasm in factory areas."),
  [("Herpesviruses",
    "Herpesviruses are large, enveloped, icosahedral double-stranded DNA viruses that replicate within the nucleus, "
    "but the largest and most complex animal viruses, with the largest genome, are the poxviruses.",
    "takes 'large herpesviruses' as the largest"),
   ("Parvoviruses",
    "Parvoviruses are at the other extreme: nonenveloped single-stranded DNA viruses of small diameter and genome "
    "size. The largest and most complex animal viruses are the poxviruses.",
    "reverses the size extreme"),
   ("Adenoviruses",
    "Adenoviruses are nonenveloped double-stranded DNA viruses causing acute infections such as colds and "
    "conjunctivitis; they are not the largest. That distinction belongs to the poxviruses.",
    "picks a common double-stranded DNA virus")],
  cl(32, 33, 55, 93, 103)),

# ============================================================ 3.8 (it) variola / smallpox
Q("3.8", "it", "A", "Smallpox: stage of greatest contagion", 5,
  "During smallpox, which stage is the stage of greatest contagion?",
  ("The early rash in the mouth",
   "Correct: the early rash, small red spots on the tongue and mouth that break open and release large amounts of "
   "virus into the mouth and throat, is the stage of greatest contagion; smallpox spreads by inhaling airborne saliva."),
  [("The incubation period",
    "During the incubation period, before the high fever, aches and vomiting begin, there is no rash releasing virus. "
    "The greatest contagion comes with the early rash in the mouth, when sores break open into the throat.",
    "places peak contagion before symptoms"),
   ("The scab stage",
    "During scabbing the patient remains contagious and stops being contagious only once all scabs fall off, but this "
    "is not the peak. The greatest contagion is the early mouth rash that releases large amounts of virus.",
    "confuses lasting contagion with peak contagion"),
   ("The fluid-filled sore stage",
    "By the fourth day the skin sores fill with fluid and fever may rise again; the patient is still contagious. The "
    "stage of greatest contagion, though, is the earlier rash on the tongue and mouth.",
    "picks the most visible skin stage as the most contagious")],
  ci(40, 41)),

Q("3.8", "it", "B", "Smallpox: when contagion ends", 5,
  "When is a patient with smallpox no longer contagious?",
  ("Once all scabs have fallen off",
   "Correct: the patient remains contagious through the sores and the scabs that form over them; only once all "
   "scabs have fallen off (which may leave scars) is the patient no longer contagious. Scabs can also spread "
   "disease by contact or fomites."),
  [("Once the fever declines",
    "The fever declines once the rash has covered the body, but the patient is still contagious and the fever may "
    "rise again by the fourth day. Contagion ends only after all scabs have fallen off.",
    "takes the first fever drop as the end of contagion"),
   ("Once scabs begin to form",
    "Scab formation does not end contagion: the patient remains contagious, and material from scabs can spread the "
    "disease by contact and fomites. Contagion ends only once all scabs have fallen off.",
    "ends contagion too early"),
   ("Once the rash covers the body",
    "Total body coverage within 24 hours is early in the illness, soon after the most contagious mouth-rash stage. "
    "The patient stays contagious until every scab has fallen off.",
    "confuses rash spread with recovery")],
  cl(40, 41)),

# ============================================================ 3.9 (it) mpox and its vaccine
Q("3.9", "it", "A", "Mpox vaccine: JYNNEOS", 5,
  "Which vaccine is available to prevent mpox?",
  ("JYNNEOS",
   "Correct: JYNNEOS, held in the Strategic National Stockpile, is a smallpox and monkeypox vaccine, and it is "
   "offered to prevent mpox; the smallpox vaccine ACAM2000 has also been made available against it."),
  [("Gardasil",
    "Gardasil is one of the two effective human papillomavirus vaccines (with Cervarix), used against warts and "
    "papillomavirus infection, not mpox. Mpox is prevented with JYNNEOS, a smallpox and monkeypox vaccine.",
    "picks another viral vaccine"),
   ("Hepatitis B vaccine",
    "The hepatitis B vaccine is derived from surface antigen from cloned yeast and protects against hepatitis B, a "
    "blood-borne liver infection. Mpox is prevented with JYNNEOS, a smallpox and monkeypox vaccine.",
    "picks another DNA-virus vaccine"),
   ("Adenovirus vaccine",
    "The adenovirus vaccine, against types 4 and 7, is given to some military personnel in training environments. "
    "Mpox, a poxvirus, is prevented with JYNNEOS, a smallpox and monkeypox vaccine.",
    "picks another DNA-virus vaccine")],
  ci(4, 44, 52, 91, 94, 99)),

Q("3.9", "it", "B", "Mpox vaccine origin: smallpox vaccine", 5,
  "ACAM2000, a live vaccinia vaccine made available to prevent mpox, was approved to protect against which disease?",
  ("Smallpox",
   "Correct: ACAM2000, a live vaccinia virus vaccine in the Strategic National Stockpile, was approved to protect "
   "against smallpox and made available to prevent monkeypox; smallpox prevention is vaccination with vaccinia virus."),
  [("Orf",
    "Orf is a parapoxvirus of sheep and goats caught by people through feeding, shearing or bites, and is more "
    "serious in the immunocompromised. ACAM2000, a live vaccinia vaccine, was approved to protect against smallpox.",
    "picks an animal poxvirus disease"),
   ("Chickenpox",
    "Chickenpox is caused by varicella zoster, a herpesvirus, and has its own live attenuated vaccine. ACAM2000 is a "
    "vaccinia vaccine approved against smallpox, a poxvirus disease.",
    "confuses 'pox' names across virus families"),
   ("Molluscum contagiosum",
    "Molluscum contagiosum, a poxvirus causing small waxy lesions, has no vaccine; it is treated by removing lesions. "
    "ACAM2000 was approved against smallpox and later made available to prevent mpox.",
    "picks another poxvirus disease")],
  ci(4, 43, 44, 46, 52, 54, 69)),

# ============================================================ 3.10 (cold) varicella zoster contagion
Q("3.10", "cold", "A", "Chickenpox: most infectious period", 5,
  "When is a person with a primary varicella zoster infection (chickenpox) most infectious?",
  ("In the 24 to 48 hours before lesions",
   "Correct: varicella zoster is most infectious 24 to 48 hours prior to the development of lesions; it spreads by "
   "respiratory droplets and contact with fluid from active skin lesions, so a person can spread it before any rash "
   "is seen."),
  [("Only after all lesions crust over",
    "Crusted lesions are the end of the eruption, not the peak; the virus spreads by droplets and fluid from active "
    "lesions. Varicella zoster is most infectious 24 to 48 hours before lesions develop.",
    "places peak contagion after the eruption"),
   ("Only once vesicles have erupted",
    "Fluid from active lesions does transmit the virus, but the most infectious time comes earlier, 24 to 48 hours "
    "prior to lesion development, when no rash is yet visible.",
    "assumes contagion starts with the visible rash"),
   ("When pain follows a dermatome",
    "Pain along a nerve pathway with vesicles in a dermatome is shingles, the later reactivation of the latent virus. "
    "Primary chickenpox is most infectious 24 to 48 hours before lesions appear.",
    "confuses shingles with primary chickenpox")],
  ci(5, 68, 69)),

Q("3.10", "cold", "B", "Shingles exposure in an unvaccinated child", 5,
  ("An unvaccinated child has close contact with fluid from a grandparent's active shingles lesions and becomes "
   "infected. What illness will the child develop?"),
  ("Chickenpox",
   "Correct: shingles patients can infect unvaccinated individuals, particularly children, and they develop "
   "chickenpox, not shingles. Chickenpox is the primary infection; shingles comes only from later reactivation of "
   "latent virus."),
  [("Shingles",
    "Shingles is reactivation of varicella zoster that has been latent in neurons after an earlier primary "
    "infection. A child with no prior infection or vaccine catches chickenpox, the primary infection, from shingles.",
    "thinks the contact catches the same form"),
   ("No illness at all",
    "Shingles is infectious to those who have never been immunized; the virus spreads through contact with fluid "
    "from active skin lesions. An unvaccinated child who is infected develops chickenpox.",
    "thinks shingles cannot spread"),
   ("Roseola",
    "Roseola, a febrile illness with a faint rash in babies, is caused by human herpesviruses 6 and 7, spread by "
    "saliva. Varicella zoster from shingles lesions gives an unvaccinated child chickenpox.",
    "swaps in another childhood herpesvirus rash")],
  ci(5, 6, 68, 69, 81)),

# ============================================================ 3.11 (cold) Kaposi sarcoma
Q("3.11", "cold", "A", "Kaposi sarcoma virus (picture)", 4,
  ("A patient with acquired immunodeficiency syndrome has many small, painless, discolored skin lumps like "
   "those shown. Which herpesvirus is linked to this tumor?"),
  ("Human herpesvirus 8",
   "Correct: these are Kaposi sarcoma lesions, small painless discolored lumps on the skin that may disseminate to "
   "internal organs. Kaposi sarcoma-associated virus, human herpesvirus 8, is linked with this common tumor of acquired immunodeficiency syndrome "
   "patients."),
  [("Epstein-Barr virus",
    "Epstein-Barr virus is the oncogenic herpesvirus of Burkitt lymphoma and nasopharyngeal carcinoma, and of hairy "
    "leukoplakia in acquired immunodeficiency syndrome. Small painless discolored skin lumps in acquired immunodeficiency syndrome are Kaposi sarcoma, from human herpesvirus 8.",
    "swaps one oncogenic herpesvirus for another"),
   ("Cytomegalovirus",
    "In patients with acquired immunodeficiency syndrome, cytomegalovirus causes retinitis, mononucleosis and disseminated disease, not skin "
    "tumors. Small painless discolored skin lumps are Kaposi sarcoma, linked with human herpesvirus 8.",
    "picks another acquired immunodeficiency syndrome-associated herpesvirus"),
   ("Human herpesvirus 6",
    "Human herpesvirus 6 causes roseola in babies and has an association (not causation) with Hodgkin lymphoma and "
    "some leukemias. Kaposi sarcoma, the common skin tumor of acquired immunodeficiency syndrome, is linked with human herpesvirus 8.",
    "confuses the numbered herpesviruses")],
  ci(84, 6, 28, 74, 77, 81, 83),
  img=IMG + "/wr3-fig-17.jpg",
  alt=("Photograph of a patient lying in a hospital bed with a breathing tube taped at the mouth; the bare chest "
       "and abdomen show many scattered small dark raised spots")),

Q("3.11", "cold", "B", "Human herpesvirus 8: the tumor it is linked to", 4,
  "Human herpesvirus 8 is linked with which tumor, common in patients with acquired immunodeficiency syndrome?",
  ("Kaposi sarcoma",
   "Correct: human herpesvirus 8 is the Kaposi sarcoma-associated virus, linked with this common tumor of acquired immunodeficiency syndrome "
   "patients; Kaposi sarcoma forms small, painless, discolored lumps on the skin and may spread to internal organs."),
  [("Burkitt lymphoma",
    "Burkitt lymphoma, a B-cell malignancy that swells the jaw in central African children, is associated with "
    "Epstein-Barr virus. Human herpesvirus 8 is linked with Kaposi sarcoma.",
    "swaps Epstein-Barr's tumor in"),
   ("Hepatocellular carcinoma",
    "Hepatocellular (hepatic) carcinoma is linked with hepatitis B virus, which multiplies in the liver and can become "
    "chronic. Human herpesvirus 8 is linked with Kaposi sarcoma, the skin tumor of acquired immunodeficiency syndrome.",
    "swaps hepatitis B's tumor in"),
   ("Hodgkin lymphoma",
    "Hodgkin lymphoma has an association, not causation, with human herpesvirus 6. Human herpesvirus 8 is linked "
    "with Kaposi sarcoma, the small painless discolored skin lumps common in acquired immunodeficiency syndrome.",
    "confuses the numbered herpesviruses")],
  ci(6, 28, 77, 83, 87)),

# ============================================================ 3.12 (cold) the other chart viruses — form A
Q("3.12", "cold", "A", "Hepatitis B: risk to health care workers", 5,
  "Why is hepatitis B virus a great risk to health care workers?",
  ("Minute amounts of blood transmit it",
   "Correct: hepatitis B multiplies in the liver, which continuously seeds the blood with virus, so minute amounts "
   "of blood or blood products can transmit it; the very low infective dose makes it a great risk to health care "
   "workers."),
  [("It spreads by respiratory droplets",
    "Droplet spread fits adenovirus and parvovirus B19, not hepatitis B. Hepatitis B passes through blood or serum "
    "and sexual contact, and minute amounts of blood are enough to transmit it.",
    "assigns a respiratory route to a blood-borne virus"),
   ("It spreads in contaminated food",
    "Ingesting contaminated food or water is a route for polyomaviruses, and ingestion for adenovirus. Hepatitis B "
    "enters through broken skin, mucous membranes or injection, and minute amounts of blood transmit it.",
    "assigns a food route to a blood-borne virus"),
   ("No vaccine exists against it",
    "A hepatitis B vaccine does exist, made from surface antigen from cloned yeast, and it is the primary prevention. "
    "The risk to health care workers comes from the very low infective dose: minute amounts of blood transmit it.",
    "thinks hepatitis B has no vaccine")],
  ci(6, 7, 87, 88, 91)),

Q("3.12", "cold", "A", "Adenovirus: military vaccine", 5,
  "Which DNA virus has a vaccine against types 4 and 7 that is given to some military personnel in training?",
  ("Adenovirus",
   "Correct: an inactivated polyvalent vaccine against adenovirus types 4 and 7 is given to some military personnel "
   "in training environments. Adenoviruses spread by respiratory and ocular secretions and cause colds and "
   "conjunctivitis."),
  [("JC polyomavirus",
    "Polyomaviruses, JC virus included, have no vaccine for humans; JC causes progressive multifocal "
    "leukoencephalopathy in the immunosuppressed. The types 4 and 7 military vaccine is against adenovirus.",
    "assigns a vaccine to a virus that has none"),
   ("Epstein-Barr virus",
    "Epstein-Barr virus has no preventive vaccine, only therapeutic vaccines in trials for its related cancers. The "
    "vaccine against types 4 and 7 for military trainees is the adenovirus vaccine.",
    "assigns a vaccine to a virus that has none"),
   ("Cytomegalovirus",
    "No cytomegalovirus vaccine is currently available; several are in clinical trials, slowed by the lack of an "
    "animal model. The types 4 and 7 vaccine for military trainees is against adenovirus.",
    "assigns a vaccine to a virus that has none")],
  ci(7, 5, 6, 74, 79, 93, 94)),

Q("3.12", "cold", "A", "JC virus: progressive multifocal leukoencephalopathy", 4,
  ("An immunosuppressed patient develops progressive multifocal leukoencephalopathy, with destruction of the cells "
   "that make myelin and progressive neurological symptoms. Which virus causes it?"),
  ("JC polyomavirus",
   "Correct: progressive multifocal leukoencephalopathy is an uncommon, often fatal infection caused by JC virus, "
   "seen in immunosuppressed patients; the virus can cross the blood-brain barrier and destroys myelin-producing "
   "cells."),
  [("BK polyomavirus",
    "BK virus, the other important human polyomavirus, lies dormant in the kidney, ureter and bladder lining and "
    "causes hematuria and nephritis after renal transplant. Demyelinating leukoencephalopathy is JC virus.",
    "confuses the two human polyomaviruses"),
   ("Cytomegalovirus",
    "Cytomegalovirus can cause encephalitis with brain swelling and confusion, and severe disease in transplant and "
    "acquired immunodeficiency syndrome patients, but progressive multifocal leukoencephalopathy, destroying myelin-making cells, is JC virus.",
    "picks another opportunistic brain infection"),
   ("Herpes simplex virus",
    "Herpes simplex can cause herpetic meningoencephalitis, at first infection or on reactivation, which may be fatal "
    "untreated. Progressive multifocal leukoencephalopathy with myelin loss is caused by JC virus.",
    "confuses herpetic meningoencephalitis with demyelination")],
  ci(7, 5, 62, 101, 102)),

Q("3.12", "cold", "A", "Molluscum contagiosum", 4,
  ("A patient has small, smooth, waxy lesions in the genital area and on the thighs, spread by direct contact and "
   "fomites and normally self-limiting. Which virus causes them?"),
  ("Molluscum contagiosum virus",
   "Correct: molluscum contagiosum, a poxvirus spread by direct contact and fomites, produces small, smooth, waxy "
   "lesions in the genital area and thighs that are normally self-limiting; treatment, when used, removes the "
   "individual lesions."),
  [("Human papillomavirus",
    "Human papillomavirus causes genital warts, ranging from tiny flat bumps to extensive, branching, cauliflower-like "
    "masses, not smooth waxy lesions. Smooth, waxy, self-limiting lesions on the genitals and thighs are molluscum.",
    "confuses genital warts with molluscum"),
   ("Herpes simplex virus type 2",
    "Herpes simplex type 2 causes clusters of sensitive vesicles on the genitalia, perineum and buttocks that "
    "ulcerate, with groin swelling and painful urination. Smooth, waxy, self-limiting lesions are molluscum.",
    "confuses genital herpes with molluscum"),
   ("Mpox virus",
    "Mpox begins with fever, aches and swollen lymph nodes, then a rash often starting on the face that goes from "
    "macules to pustules to scabs. Small smooth waxy genital lesions without that course are molluscum contagiosum.",
    "picks the other human poxvirus")],
  ci(4, 5, 46, 48, 63, 97)),

# ============================================================ 3.12 (cold) the other chart viruses — form B
Q("3.12", "cold", "B", "Parvovirus B19: fifth disease (picture)", 4,
  "A child with a low-grade fever has the rash shown on the cheek. Which virus causes it?",
  ("Parvovirus B19",
   "Correct: this is the slapped-face rash of fifth disease (erythema infectiosum), caused by parvovirus B19, a "
   "nonenveloped single-stranded DNA virus spread by droplet infection; children may have fever and a rash on the "
   "cheeks."),
  [("Human herpesvirus 6",
    "Human herpesvirus 6 causes roseola, an acute febrile disease of babies with a faint maculopapular rash after the "
    "fever. A slapped-face rash on the cheeks of a child with low-grade fever is fifth disease, from parvovirus B19.",
    "confuses two childhood rash diseases"),
   ("Rubella virus",
    "Rubella is one of the other childhood rash diseases and is teratogenic, crossing the placenta. Fifth disease, "
    "the slapped-face rash on the cheeks, is caused by parvovirus B19.",
    "confuses two childhood rash diseases"),
   ("Varicella zoster virus",
    "Varicella zoster causes chickenpox, with characteristic filled vesicles, another of the childhood rash "
    "diseases. A flat red slapped-face rash on the cheeks is fifth disease from parvovirus B19.",
    "confuses a vesicular rash with a slapped-cheek rash")],
  ci(105, 5, 7, 28, 81, 103, 104),
  img=IMG + "/wr3-fig-18.jpg",
  alt="Side view of a young child's face showing a bright red flush over the cheek, with the surrounding skin normal"),

Q("3.12", "cold", "B", "Human papillomavirus: plantar warts", 4,
  "Which virus causes deep, painful warts on the soles of the feet?",
  ("Human papillomavirus",
   "Correct: papillomas are squamous epithelial growths (warts) caused by about 100 strains of human papillomavirus; "
   "plantar warts are deep and painful on the soles of the feet, and the virus spreads by direct contact or "
   "contaminated fomites."),
  [("Molluscum contagiosum virus",
    "Molluscum contagiosum, a poxvirus, causes small, smooth, waxy lesions in the genital area and thighs that are "
    "normally self-limiting. Deep, painful warts on the soles are plantar warts from human papillomavirus.",
    "confuses waxy molluscum lesions with warts"),
   ("Cowpox virus",
    "Cowpox causes rare pocks usually confined to the hands, caught from cats that met rodents or after injury. "
    "Deep, painful warts on the soles of the feet are plantar warts from human papillomavirus.",
    "picks a poxvirus for a wart"),
   ("Herpes simplex virus",
    "Herpes simplex causes vesicles that crust over, such as cold sores, and herpetic whitlow on a finger. Deep, "
    "painful growths on the soles of the feet are plantar warts from human papillomavirus.",
    "confuses vesicles with warts")],
  cl(46, 53, 60, 97, 98)),

Q("3.12", "cold", "B", "BK virus after renal transplant", 4,
  ("Months after a renal transplant, a patient on immunosuppressive drugs develops hematuria, hemorrhagic cystitis "
   "and interstitial nephritis. Which virus, dormant in the kidney and the lining of the ureters and bladder, is the "
   "cause?"),
  ("BK polyomavirus",
   "Correct: after a cold-like first infection, BK virus lies dormant in the kidney and the lining of the ureters and "
   "bladder; after renal transplant and immunosuppressive drugs it causes hematuria, hemorrhagic cystitis and "
   "interstitial nephritis."),
  [("JC polyomavirus",
    "JC virus also sheds in urine, but its disease is progressive multifocal leukoencephalopathy, destroying "
    "myelin-making cells in immunosuppressed patients. Urinary bleeding and nephritis after renal transplant is BK virus.",
    "confuses the two human polyomaviruses"),
   ("Hepatitis B virus",
    "Hepatitis B virus multiplies exclusively in the liver and is screened for in organs for transplant; its disease "
    "is hepatitis, with jaundice, cirrhosis or cancer. Hematuria and nephritis after renal transplant is BK virus.",
    "picks a transplant-screened virus"),
   ("Parvovirus B19",
    "In adults parvovirus B19 can cause polyarthropathy with massive joint swelling or stop red blood cell "
    "production, most often in the immunocompromised. Hematuria and nephritis after renal transplant is BK virus.",
    "picks another virus of the immunocompromised")],
  ci(7, 87, 90, 102, 104)),

Q("3.12", "cold", "B", "Cowpox in humans", 5,
  ("A person develops pocks on one hand after handling a pet cat that hunts rodents. Which virus most likely "
   "causes this?"),
  ("Cowpox virus",
   "Correct: human cowpox is rare and usually confined to the hands; rodents are the primary reservoir, and people "
   "can catch it from handling cats that interacted with rodents. Its vaccine is only for animals."),
  [("Orf virus",
    "Orf is a parapoxvirus of sheep and goats (sore mouth, contagious ecthyma), caught by people through feeding, "
    "shearing or bites. Hand pocks after handling a cat that hunts rodents point to cowpox.",
    "picks the poxvirus of sheep and goats"),
   ("Variola virus",
    "Variola, the smallpox virus, requires a human host and spreads by inhaled saliva, scab material and fomites, "
    "with a rash covering the whole body. A single-hand lesion after handling a cat points to cowpox.",
    "picks the human-only poxvirus"),
   ("Molluscum contagiosum virus",
    "Molluscum contagiosum spreads person to person by direct contact and fomites, with small waxy lesions on the "
    "genitals and thighs. Pocks on the hand after handling a rodent-hunting cat are cowpox.",
    "picks the poxvirus spread between people")],
  ci(4, 34, 40, 41, 46, 53, 54)),
]
