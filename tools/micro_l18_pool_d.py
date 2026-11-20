# -*- coding: utf-8 -*-
# Microbiology Exam 3, Lecture 18 — DNA Viruses of Medical Importance (Dr. Webster, 13 November 2026), pool D:
# deck slides 85-106 — the viral agents of hepatitis and the hepadnaviruses (hepatitis B virus: genome, culture,
# transmission, pathogenesis, the clinical-features picture on slide 89, diagnosis, screening, passive
# immunization and the two vaccines), the nonenveloped DNA viruses (adenoviruses with type 41 hepatitis and the
# military vaccine, papillomaviruses, polyomaviruses JC and BK, parvovirus B19, adeno-associated virus); plus the
# chart rows on slides 6-7 (Hepatitis B, Adenovirus, Human Papilloma Virus, Polyoma Viruses, Parvovirus B19).
#
# FROM THE VISIBLE SLIDES ONLY (text and pictures; speaker notes not used). Facts from other slides of the deck
# (24 most DNA viruses bud off the nucleus, 26 persistent chronic vs latent, 28 oncogenic/teratogenic list, 32
# poxviruses in cytoplasmic factory areas, 43-44 vaccinia/ACAM2000/JYNNEOS, 46 molluscum, 59 trigeminal latency,
# 64 C-section, 66 giant multinucleated cells, 81 roseola) appear only inside explanations or as distractors.
# Keys short and authored at index 0 with the only "Correct." opener; `mis` per distractor.
#
# Picture-only facts used: slide 6 and 7 chart rows (hepatitis B "contact with blood or serum, sexual contact",
# "Yes" vaccine, "may lead to cirrhosis and hepatic cancer"; adenovirus "droplet infection from respiratory and
# ocular secretions"; HPV "direct contact including sexual contact or contact with fomites", "vaccines available for
# genital warts", nine strains raise reproductive system cancer risk; polyoma "JC in early childhood, BK in
# adolescence", "None for humans"; parvovirus B19 "droplet infection", hydrops fetalis, polyarthropathy, cessation
# of red blood cell production); slide 89 (fever, rash, arthritis, jaundice, enlarged liver, low white cell count,
# pain and tenderness); slide 95 (viral inclusions inside the nuclear membrane, mass of virions); slide 98 (common
# warts on a hand = quiz picture l18-fig-15); slide 100 (koilocyte vs normal cervical cell = l18-fig-16, labels
# removed, pointer lines kept).
#
# HELD (never a key or decisive fact), and why:
#   - drugs: interferon for chronic hepatitis B (90) and for severe adenovirus (93), podophyllin (99; chemical
#     application mentioned only beside the physical methods).
#   - numbers: 10^7 virions/mL (87), 7-week incubation (88), 3 doses (91), 100 strains, nine types and "2 account
#     for 70%" (97, 99; "nine types raise the risk" is used only as words in explanations), HPV incubation 2 weeks
#     to over a year (97), over 50 adenovirus types (93), vaccine ages 17-50 (94), children aged 1-6 (94, "young
#     children" used), 80% and 91% seroprevalence (101).
#   - "most common STD in U.S." for genital warts (97): held per brief.
#   - adenovirus vaccine "inactivated" (94): not keyed (live in current practice); its oral route and types 4/7 are
#     not asked here (types 4 and 7 asked elsewhere).
#   - JC/BK patient names (101) and "link to systemic lupus" for BK (102): not asked.
#   - AAV clinical-trial list (106): not asked; AAV-adenovirus hepatitis asked only as an association.
#   - which hepatitis viruses are named on other slides beyond A, B, C and D: none used.
# CONFLICTS / CAUTIONS found (not tested):
#   - acute hemorrhagic cystitis is given to adenoviruses (93) AND hemorrhagic cystitis to BK virus (102): no item
#     offers both as options for cystitis.
#   - adenovirus transmission: slide 93 "respiratory and ocular secretions"; chart slide 7 adds "Ingestion". The
#     key uses the secretions; ingestion/food is never a distractor in the adenovirus item.
#   - slide 104 "Most common in immunocompromised" has no clear referent (B19 adult disease?): not asked.
#   - polyoma transmission: chart "body fluids, ingestion of contaminated food or water" vs slide 102 "initial
#     infection via tonsils or GI tract": consistent, used only in explanations.
# SPELLING: "Hepa dnaviruses" written hepadnaviruses; "polyarthopathy" polyarthropathy; "remarkedly" markedly;
# "occular" ocular; "preventatvie" not used.
from micro_l18_common import *

POOL_D = [
# ============================================================== HEPATITIS B VIRUS (slides 6, 85-91)
Q("Hepatitis B virus", IO4,
  "Of the three principal viruses that cause hepatitis, which one is a deoxyribonucleic acid (DNA) virus?",
  ("Hepatitis B virus",
   "Correct. Hepatitis B virus is the deoxyribonucleic acid (DNA) virus among the three principal hepatitis "
   "viruses; hepatitis A and hepatitis C viruses are ribonucleic acid (RNA) viruses. It belongs to the "
   "hepadnaviruses, enveloped deoxyribonucleic acid viruses with a tropism for the liver."),
  [("Hepatitis A virus",
    "Hepatitis A virus is one of the three principal hepatitis viruses, but it is a ribonucleic acid (RNA) "
    "virus. The deoxyribonucleic acid virus of the three is hepatitis B virus, an enveloped hepadnavirus.",
    "RNA hepatitis virus"),
   ("Hepatitis C virus",
    "Hepatitis C virus is the third principal hepatitis virus and, like hepatitis A, a ribonucleic acid (RNA) "
    "virus. Only hepatitis B virus carries deoxyribonucleic acid (DNA), with its unusual partly double-stranded, "
    "partly single-stranded genome.",
    "RNA hepatitis virus"),
   ("Hepatitis D virus",
    "Hepatitis D, the delta agent, is a circular ribonucleic acid (RNA) virus and not one of the three principal "
    "hepatitis viruses; it is known for co-infecting with hepatitis B virus and making severe disease worse. "
    "The deoxyribonucleic acid virus is hepatitis B.",
    "delta agent confused with hepatitis B")],
  c(85, 86, 88)),

Q("Hepatitis B virus", IO4,
  "In viral hepatitis, which failure of liver function leads to jaundice?",
  ("Failure to excrete bile pigments",
   "Correct. Hepatitis is inflammation of liver cells: hepatocytes die and a mononuclear response disrupts liver "
   "structure. That interferes with the liver's excretion of bile pigments, so bilirubin builds up in blood and "
   "tissues and gives the yellow tinge of skin and eyes called jaundice."),
  [("Failure to make red blood cells",
    "Stopping red blood cell production is what parvovirus B19 can do in adults, giving anemia, not a yellow "
    "tinge. Jaundice in hepatitis comes from the inflamed liver failing to excrete bile pigments, so bilirubin "
    "accumulates in blood and tissues.",
    "parvovirus red cell cessation borrowed"),
   ("Failure to make white blood cells",
    "A low white cell count is one of the pictured features of hepatitis B, but it is not why the skin turns "
    "yellow. Jaundice follows the liver's failure to excrete bile pigments, letting bilirubin accumulate in "
    "blood and tissues.",
    "associated finding mistaken for mechanism"),
   ("Failure to clear virions from blood",
    "The infected liver does the reverse of clearing virus: hepatitis B virus multiplies there and continuously "
    "seeds the blood. The yellow tinge of jaundice is bilirubin, which builds up because the liver cannot "
    "excrete bile pigments.",
    "viremia confused with jaundice")],
  c(85, 87)),

Q("Hepatitis B virus", IO4,
  "What is unusual about the genome of hepatitis B virus?",
  ("Both double- and single-stranded",
   "Correct. Hepatitis B virus, a hepadnavirus, has an unusual genome containing both double-stranded and "
   "single-stranded deoxyribonucleic acid (DNA). It is also enveloped and has a tropism for the liver, unlike the "
   "small nonenveloped deoxyribonucleic acid viruses."),
  [("Single-stranded throughout",
    "A wholly single-stranded deoxyribonucleic acid (DNA) genome belongs to the parvoviruses, small nonenveloped "
    "viruses such as parvovirus B19. Hepatitis B virus has the unusual mix: part double-stranded, part "
    "single-stranded.",
    "parvovirus genome borrowed"),
   ("Circular and fully double-stranded",
    "Circular, double-stranded deoxyribonucleic acid (DNA) is the genome of the papilloma and polyoma viruses, "
    "small nonenveloped viruses that cause persistent infections and tumors. Hepatitis B virus is enveloped with "
    "a partly double-, partly single-stranded genome.",
    "papilloma/polyoma genome borrowed"),
   ("Circular ribonucleic acid",
    "Circular ribonucleic acid (RNA) is the genome of hepatitis D, the delta agent that can co-infect and worsen "
    "hepatitis B. Hepatitis B virus itself carries deoxyribonucleic acid (DNA) that is partly double- and partly "
    "single-stranded.",
    "delta agent genome borrowed")],
  c(86, 88)),

Q("Hepatitis B virus", IO4,
  "Hepatitis B virus is difficult to culture in the laboratory. How is it grown?",
  ("Its isolated genome is put into liver cancer cells",
   "Correct. Hepatitis B virus is hard to culture, so its deoxyribonucleic acid (DNA) is isolated and injected "
   "into human liver cancer cells. That fits its tropism for the liver, where it multiplies exclusively in the "
   "body."),
  [("Whole virions are grown in normal liver cells",
    "Normal liver cells are where the virus multiplies in the body, but the laboratory method is different: the "
    "deoxyribonucleic acid (DNA) is isolated from hepatitis B virus and injected into human liver CANCER cells, "
    "not whole virions into normal cells.",
    "in-body tropism mistaken for lab method"),
   ("Whole virions are grown in kidney tubular cells",
    "Kidney tubular epithelial cells are where JC polyomavirus lies latent, shedding virus in urine. Hepatitis B "
    "virus is grown by isolating its deoxyribonucleic acid (DNA) and injecting it into human liver cancer "
    "cells.",
    "JC latency site borrowed"),
   ("Whole virions are grown in experimental animals",
    "Experimental animals are where polyomaviruses induce tumors. Hepatitis B virus is difficult to culture at "
    "all; the method is to isolate its deoxyribonucleic acid (DNA) and inject it into human liver cancer cells.",
    "polyoma animal tumors borrowed")],
  c(86, 101, 102)),

Q("Hepatitis B virus", IO5,
  "Besides blood and blood products, by which other route is hepatitis B virus transmitted?",
  ("Sexual contact",
   "Correct. Minute amounts of blood or blood products transmit hepatitis B virus, and it is also sexually "
   "transmitted, which is why it has a high incidence in the same population as human immunodeficiency virus. "
   "It enters through a break in the skin or mucous membrane or by injection."),
  [("Respiratory droplets",
    "Droplet infection is how adenoviruses and parvovirus B19 spread, through respiratory secretions. Hepatitis "
    "B virus is carried in blood and serum and is also sexually transmitted, entering through skin or mucous "
    "membrane breaks.",
    "droplet route borrowed"),
   ("Contaminated food or water",
    "Ingestion of contaminated food or water is a listed route for the polyomaviruses, alongside exposure to "
    "body fluids. Hepatitis B virus needs blood or serum contact, or sexual contact, to reach the bloodstream "
    "and liver.",
    "polyoma ingestion route borrowed"),
   ("Contact with saliva",
    "Contact with saliva spreads human herpesviruses 6 and 7 (roseola) and Epstein-Barr virus. Hepatitis B "
    "virus is a blood-borne virus that is also sexually transmitted, which is why it is a risk for health care "
    "workers.",
    "herpesvirus saliva route borrowed")],
  ci(6, 87, 88)),

Q("Hepatitis B virus", IO2,
  "Hepatitis B virus multiplies in the liver and continuously seeds the blood with virus. Which type of infection "
  "can it establish?",
  ("Persistent chronic infection",
   "Correct. Hepatitis B virus can become a chronic infection: virus keeps multiplying in the liver and seeding "
   "the blood, stays detectable, and symptoms may be mild or absent. Chronic persistent infections are the type "
   "given for human immunodeficiency virus and hepatitis B virus."),
  [("Persistent latent infection",
    "In a latent infection the virus goes dormant after a lytic cycle, is generally not detectable and later "
    "reactivates, as herpesviruses do. Hepatitis B virus keeps multiplying and seeding the blood, which is the "
    "chronic, not latent, pattern.",
    "latent vs chronic confused"),
   ("Acute, self-ending infection",
    "An acute infection is the pattern of the adenoviruses, which run their course and end. Hepatitis B virus "
    "can instead persist, continuously seeding the blood from the liver, which defines a persistent chronic "
    "infection.",
    "acute course assumed"),
   ("Lysogenic infection",
    "Lysogeny is a bacteriophage cycle in which viral deoxyribonucleic acid (DNA) is copied with the bacterial "
    "chromosome. Hepatitis B virus infects human liver cells and causes a persistent chronic infection, "
    "detectable in blood.",
    "phage cycle borrowed")],
  c(15, 26, 87, 93)),

Q("Hepatitis B virus", IO4,
  "Co-infection with which agent can make severe hepatitis B worse?",
  ("Hepatitis D (the delta agent)",
   "Correct. In more severe hepatitis B, fever, jaundice, rash and arthritis may be exacerbated by co-infection "
   "with hepatitis D, the delta agent, a circular ribonucleic acid (RNA) virus. The clue is co-infection with "
   "hepatitis B specifically."),
  [("Adeno-associated virus",
    "Adeno-associated virus is linked with more severe ADENOVIRUS hepatitis in young children (type 41), and "
    "that link is only an association. The co-infection that worsens hepatitis B is hepatitis D, the delta "
    "agent.",
    "adenovirus co-infection borrowed"),
   ("Hepatitis A virus",
    "Hepatitis A virus is another principal hepatitis virus (a ribonucleic acid virus), but it is not the agent "
    "described as worsening hepatitis B. That role belongs to hepatitis D, the circular ribonucleic acid delta "
    "agent.",
    "wrong hepatitis letter"),
   ("BK polyomavirus",
    "BK polyomavirus lies dormant in the kidney and urinary tract and causes problems after renal transplant, "
    "not liver disease. The agent that exacerbates severe hepatitis B by co-infection is hepatitis D, the delta "
    "agent.",
    "unrelated deoxyribonucleic acid virus")],
  c(88, 94, 102, 106)),

Q("Hepatitis B virus", IO4,
  "A patient with a more severe case of hepatitis B has an enlarged, tender liver and a low white cell count. "
  "Which other set of findings fits?",
  ("Fever, jaundice, rash and arthritis",
   "Correct. In more severe hepatitis B, fever, jaundice, rash and arthritis appear, with an enlarged liver, pain "
   "and tenderness and a low white cell count shown among its clinical features. Hepatitis D co-infection can "
   "make these worse."),
  [("Fever, cheek rash and hydrops",
    "A cheek rash with low-grade fever is fifth disease from parvovirus B19, and hydrops fetalis is that virus "
    "passed from mother to fetus. Severe hepatitis B brings fever, jaundice, rash and arthritis with an enlarged "
    "liver.",
    "parvovirus B19 picture"),
   ("Hematuria, cystitis and nephritis",
    "Hematuria, hemorrhagic cystitis and interstitial nephritis are the urinary complications of BK polyomavirus "
    "after renal transplant. Hepatitis B targets the liver, with fever, jaundice, rash and arthritis in severe "
    "cases.",
    "BK urinary picture"),
   ("Cough, congestion and conjunctivitis",
    "Cough, congestion and conjunctivitis are adenovirus illnesses spread by respiratory and ocular secretions. "
    "The liver findings here point to hepatitis B, whose severe cases show fever, jaundice, rash and arthritis.",
    "adenovirus picture")],
  ci(89, 7, 88)),

Q("Hepatitis B virus", IO4,
  "Which laboratory tests detect hepatitis B surface antigen?",
  ("Radioimmunoassay and enzyme-linked immunosorbent assay (ELISA)",
   "Correct. Hepatitis B is diagnosed from risk factors and serological tests for viral antibodies or antigen; "
   "radioimmunoassay and enzyme-linked immunosorbent assay (ELISA) tests detect its surface antigens. Screening "
   "covers blood for transfusion, semen, organs for transplant and all pregnant women."),
  [("Pap smear and genital inspection for abnormal cells",
    "Pap smear and inspection of the genitals are the early-detection tools for human papillomavirus, which "
    "shows abnormal cervical cells such as koilocytes. Hepatitis B surface antigen is found by radioimmunoassay "
    "and enzyme-linked immunosorbent assay.",
    "papillomavirus screening borrowed"),
   ("Urine testing for virus shed from the kidney tubules",
    "Virus shed in urine comes from JC polyomavirus lying latent in the tubular epithelial cells of the kidney. "
    "Hepatitis B is diagnosed by serology, with radioimmunoassay and enzyme-linked immunosorbent assay for its "
    "surface antigen.",
    "JC urine shedding borrowed"),
   ("Scrapings showing giant multinucleated cells in lesions",
    "Scrapings from the base of vesicles showing giant multinucleated cells diagnose herpes simplex virus "
    "infection. Hepatitis B causes no such vesicles; its surface antigen is detected by radioimmunoassay and "
    "enzyme-linked immunosorbent assay.",
    "herpes simplex diagnosis borrowed")],
  c(66, 90, 99, 102)),

Q("Hepatitis B virus", IO5,
  "From what is the main hepatitis B vaccine derived?",
  ("Surface antigen cloned in yeast",
   "Correct. Hepatitis B vaccines are derived from surface antigen from cloned yeast, given with boosters. "
   "Vaccination is the primary prevention for high-risk people and is encouraged for all newborns and infants. "
   "A second vaccine, made from antigen purified from carrier blood, is mainly for people with yeast allergies."),
  [("Live vaccinia virus",
    "Live vaccinia virus is the smallpox vaccine (ACAM2000 is one), also made available to prevent mpox. "
    "Hepatitis B vaccination uses no live virus: the main vaccine is surface antigen produced from cloned yeast.",
    "poxvirus vaccine borrowed"),
   ("Adenovirus types 4 and 7",
    "A vaccine against adenovirus types 4 and 7 is given to some military personnel in training. Hepatitis B "
    "vaccine is a single antigen, the surface antigen, cloned in yeast, not a mix of virus types.",
    "adenovirus vaccine borrowed"),
   ("An adeno-associated virus vector",
    "Adeno-associated virus is used as a vector for human gene therapy, approved to treat lipoprotein lipase "
    "deficiency, not as a hepatitis vaccine. The hepatitis B vaccine is built from surface antigen cloned in "
    "yeast.",
    "gene therapy vector borrowed")],
  c(43, 44, 91, 94, 106)),

Q("Hepatitis B virus", IO5,
  "Who mainly receives the hepatitis B vaccine made from purified antigen extracted from carrier blood?",
  ("People with yeast allergies",
   "Correct. The usual hepatitis B vaccine is surface antigen cloned in yeast, so the vaccine made from purified "
   "sterile antigen extracted from carrier blood is mainly for people with yeast allergies. The clue is the "
   "alternative source of the antigen."),
  [("Newborns of infected mothers",
    "Newborns of infected mothers are protected passively with hepatitis B immune globulin (HBIG), and "
    "vaccination is encouraged for all newborns. The blood-derived vaccine exists mainly for people who cannot "
    "take the yeast-derived one.",
    "passive immunization group"),
   ("Health care workers after exposure",
    "Exposed or possibly exposed health care workers receive passive immunization with hepatitis B immune "
    "globulin (HBIG). The vaccine extracted from carrier blood is reserved mainly for people allergic to yeast.",
    "post-exposure passive group"),
   ("Military personnel in training",
    "Military personnel in training are the group given the adenovirus types 4 and 7 vaccine. The hepatitis B "
    "vaccine made from carrier-blood antigen is mainly for people with yeast allergies.",
    "adenovirus vaccine group")],
  c(91, 94)),

Q("Hepatitis B virus", IO5,
  "A newborn's mother is infected with hepatitis B virus. What gives the newborn passive immunization?",
  ("Hepatitis B immune globulin (HBIG)",
   "Correct. Passive immunization with hepatitis B immune globulin (HBIG) is given to people exposed or possibly "
   "exposed, including neonates born to infected mothers and health care workers. Vaccination, the primary "
   "prevention, is active immunity and is encouraged for all newborns."),
  [("The yeast-derived surface antigen vaccine",
    "The vaccine from surface antigen cloned in yeast gives ACTIVE immunity and is encouraged for all newborns, "
    "but the question asks for passive protection. That is hepatitis B immune globulin (HBIG), given to "
    "neonates of infected mothers.",
    "active vs passive confused"),
   ("Delivery by cesarean section",
    "Delivery by cesarean section is the step taken when a mother has a herpes simplex outbreak at the time of "
    "birth. For hepatitis B the newborn is passively immunized with hepatitis B immune globulin (HBIG).",
    "herpes birth measure borrowed"),
   ("An adeno-associated virus vector",
    "Adeno-associated virus is a gene therapy vector, approved for lipoprotein lipase deficiency; it gives no "
    "immunity to hepatitis B. Passive immunization of the newborn uses hepatitis B immune globulin (HBIG).",
    "gene therapy vector borrowed")],
  c(64, 91, 106)),

# ============================================================== ADENOVIRUS (slides 7, 93-95)
Q("Adenovirus", IO4,
  "Which description fits the adenovirus virion and genome?",
  ("Nonenveloped; double-stranded",
   "Correct. Adenoviruses are nonenveloped, double-stranded deoxyribonucleic acid (DNA) viruses that cause acute "
   "infections. They infect lymphoid tissue, respiratory and intestinal epithelia and the conjunctiva, and spread "
   "by respiratory and ocular secretions."),
  [("Enveloped; partly single-stranded",
    "An envelope with a partly double-, partly single-stranded genome describes hepatitis B virus, a "
    "hepadnavirus. Adenoviruses have no envelope and carry fully double-stranded deoxyribonucleic acid (DNA).",
    "hepadnavirus structure borrowed"),
   ("Nonenveloped; single-stranded",
    "Nonenveloped with single-stranded deoxyribonucleic acid (DNA) is the parvovirus pattern, small viruses such "
    "as parvovirus B19. Adenoviruses share the lack of an envelope but their genome is double-stranded.",
    "parvovirus structure borrowed"),
   ("Enveloped; double-stranded",
    "Adenoviruses are listed among the nonenveloped deoxyribonucleic acid viruses, alongside the polyoma, papilloma and parvo "
    "viruses. Their genome is double-stranded deoxyribonucleic acid (DNA) inside a bare capsid, with no "
    "envelope.",
    "envelope assumed")],
  c(86, 92, 93, 103)),

Q("Adenovirus", IO3,
  "In which hosts are adenoviruses oncogenic?",
  ("In animals, not in humans",
   "Correct. Adenoviruses are oncogenic in animals but not in humans. In people they cause acute infections such "
   "as colds, pharyngitis, conjunctivitis, keratoconjunctivitis, acute hemorrhagic cystitis and infantile "
   "gastroenteritis, not tumors."),
  [("In humans, not in animals",
    "This reverses the fact: adenoviruses are oncogenic in animals, not in humans. Human oncogenic deoxyribonucleic acid viruses "
    "include hepatitis B virus (hepatic carcinoma) and the papillomaviruses (cervical and penile cancer).",
    "direction reversed"),
   ("In both humans and animals",
    "Adenoviruses cause tumors in animals only; in humans their infections are acute, such as colds and "
    "conjunctivitis. Viruses oncogenic in humans are a separate list, for example Epstein-Barr virus and "
    "hepatitis B virus.",
    "overextended oncogenicity"),
   ("In children, not in adults",
    "Age does not decide adenovirus oncogenicity; the line is drawn between species: animals yes, humans no. In "
    "children adenoviruses cause acute illness such as infantile gastroenteritis and, with type 41, hepatitis.",
    "pediatric disease mistaken for tumor")],
  c(28, 93, 94)),

Q("Adenovirus", IO5,
  "How do adenoviruses mainly spread from person to person?",
  ("Respiratory and ocular secretions",
   "Correct. Adenoviruses spread by respiratory and ocular secretions (droplet infection), which fits where they "
   "infect: respiratory epithelium and the conjunctiva, causing colds, pharyngitis and conjunctivitis."),
  [("Blood and sexual contact",
    "Blood, serum and sexual contact transmit hepatitis B virus, a risk for health care workers. Adenoviruses "
    "spread by respiratory and ocular secretions, matching their colds and conjunctivitis.",
    "hepatitis B route borrowed"),
   ("Direct skin contact and fomites",
    "Direct contact or contaminated fomites is how human papillomavirus spreads its warts. Adenoviruses travel in "
    "respiratory and ocular secretions, infecting respiratory epithelium and the conjunctiva.",
    "papillomavirus route borrowed"),
   ("Contact with saliva alone",
    "Contact with saliva is the route for human herpesviruses 6 and 7 (roseola). Adenoviruses spread through "
    "respiratory and ocular secretions as droplets, which explains their eye infections.",
    "herpesvirus saliva route borrowed")],
  ci(7, 6, 93)),

Q("Adenovirus", IO4,
  "Which of these diseases is caused by adenoviruses?",
  ("Infantile gastroenteritis",
   "Correct. Adenoviruses infect intestinal epithelia as well as respiratory epithelia, lymphoid tissue and the "
   "conjunctiva, causing colds, pharyngitis, conjunctivitis, keratoconjunctivitis, acute hemorrhagic cystitis and "
   "infantile gastroenteritis."),
  [("Erythema infectiosum",
    "Erythema infectiosum, fifth disease, is the slapped-cheek rash of childhood caused by parvovirus B19. "
    "Adenoviruses cause respiratory, eye, bladder and intestinal illness, including infantile gastroenteritis.",
    "parvovirus disease"),
   ("Progressive multifocal leukoencephalopathy",
    "Progressive multifocal leukoencephalopathy is JC polyomavirus destroying myelin-producing cells in "
    "immunosuppressed patients. Adenoviruses cause acute illnesses such as colds, conjunctivitis and infantile "
    "gastroenteritis.",
    "JC disease"),
   ("Hepatocellular carcinoma",
    "Hepatocellular carcinoma is the liver cancer whose risk rises with chronic hepatitis B virus infection. "
    "Adenoviruses are not oncogenic in humans; their diseases are acute, such as infantile gastroenteritis.",
    "hepatitis B cancer")],
  ci(7, 87, 93, 102, 104)),

Q("Adenovirus", IO4,
  "Some of the most serious cases of adenovirus type 41 hepatitis in young children also show co-infection with "
  "which virus, so far only as an association?",
  ("Adeno-associated virus",
   "Correct. Type 41 adenovirus is associated with hepatitis in young children, with markedly raised liver "
   "enzymes, vomiting, diarrhea, jaundice and abdominal pain. Some of the most serious cases show co-infection "
   "with adeno-associated virus, a parvovirus; this is only an association, and more data are needed for "
   "causation."),
  [("Hepatitis D virus",
    "Hepatitis D, the delta agent, is the co-infection that can exacerbate severe HEPATITIS B, not adenovirus "
    "hepatitis. The virus found alongside severe type 41 adenovirus hepatitis is adeno-associated virus.",
    "delta agent borrowed"),
   ("Hepatitis B virus",
    "Hepatitis B virus causes its own hepatitis, multiplying in the liver and seeding the blood. The co-infection "
    "noted in the most serious type 41 adenovirus hepatitis cases is adeno-associated virus, a parvovirus.",
    "other hepatitis virus"),
   ("BK polyomavirus",
    "BK polyomavirus lies dormant in the kidney and urinary tract and causes hematuria and nephritis after renal "
    "transplant. Severe type 41 adenovirus hepatitis has been associated with adeno-associated virus co-infection.",
    "unrelated deoxyribonucleic acid virus")],
  c(87, 88, 94, 102, 106)),

Q("Adenovirus", IO1,
  "In electron micrographs of adenovirus-infected cells, viral inclusions and a packed mass of virions are seen in "
  "which part of the cell?",
  ("The nucleus",
   "Correct. The distinctive adenovirus structures are viral inclusions lying inside the nuclear membrane and a "
   "dense mass of virions. That fits the rule that most deoxyribonucleic acid (DNA) viruses are assembled and "
   "budded off the nucleus."),
  [("Cytoplasmic factory areas",
    "Cytoplasmic factory areas are where poxviruses multiply, unlike most deoxyribonucleic acid viruses. Adenovirus inclusions sit "
    "inside the nuclear membrane, in keeping with most deoxyribonucleic acid (DNA) viruses budding off the "
    "nucleus.",
    "poxvirus site borrowed"),
   ("The nucleolus",
    "The nucleolus is labeled separately in the micrograph as a dark round body; the viral inclusions are "
    "scattered elsewhere inside the nuclear membrane. Adenovirus assembly happens in the nucleus, not in the "
    "nucleolus.",
    "neighboring structure in the picture"),
   ("The cell membrane",
    "The cell membrane is where enveloped viruses pick up an envelope as they bud. Adenoviruses are nonenveloped, "
    "and their inclusions and virion masses are seen inside the nucleus.",
    "envelope budding confused")],
  ci(95, 24, 32, 93)),

# ============================================================== HUMAN PAPILLOMAVIRUS (slides 7, 96-100)
Q("Human papillomavirus", IO4,
  "What is a papilloma?",
  ("A squamous epithelial growth",
   "Correct. A papilloma is a squamous epithelial growth: a wart or verruca. Human papillomaviruses cause common "
   "seed warts, deep plantar warts and genital warts, all growths of the skin or mucosa."),
  [("A cancer of liver cells",
    "A cancer of liver cells is hepatocellular carcinoma, a risk of chronic hepatitis B infection. A papilloma "
    "is a benign squamous epithelial growth, the wart caused by human papillomavirus.",
    "hepatocellular carcinoma confused"),
   ("A mass of virions in a nucleus",
    "A mass of virions inside the nucleus is the distinctive adenovirus structure seen by electron microscopy. "
    "A papilloma is a whole tissue growth, a squamous epithelial wart or verruca.",
    "adenovirus inclusion confused"),
   ("A loss of myelin-making cells",
    "Destruction of the cells that produce myelin is progressive multifocal leukoencephalopathy from JC "
    "polyomavirus. A papilloma is a squamous epithelial growth, a wart, from human papillomavirus.",
    "polyoma disease confused")],
  c(87, 95, 97, 102)),

Q("Human papillomavirus", IO4,
  "The painless, elevated, rough growths shown are on an adult's fingers. What are they?",
  ("Common seed warts",
   "Correct. Common seed warts are painless, elevated, rough growths on the fingers and similar sites, as on the "
   "hand shown. They are papillomas caused by human papillomavirus, spread by direct contact or fomites; most "
   "regress over time."),
  [("Plantar warts",
    "Plantar warts are deep and painful and sit on the soles of the feet. These growths are on the fingers, "
    "painless and raised: common seed warts from human papillomavirus.",
    "wrong wart type by site"),
   ("Genital warts",
    "Genital warts range from tiny flat bumps to branching cauliflower-like masses on the genitals. Raised, "
    "rough, painless growths on the fingers are common seed warts.",
    "wrong wart type by site"),
   ("Molluscum contagiosum lesions",
    "Molluscum contagiosum gives small, smooth, waxy lesions, often in the genital area and on the thighs. The "
    "growths shown are rough and elevated on the fingers, the picture of common seed warts.",
    "smooth poxvirus lesion confused")],
  ci(98, 46, 97),
  img=IMG + "/l18-fig-15.jpg",
  alt="Photograph of the back of an adult's hand and fingers with several small, raised, rough, grayish-brown "
      "growths on the skin of the fingers and knuckles.",
  slide="Slide 98"),

Q("Human papillomavirus", IO5,
  "How is human papillomavirus transmitted?",
  ("Direct contact or fomites",
   "Correct. Human papillomavirus is transmissible through direct contact, including sexual contact, or through "
   "contaminated fomites. That is how common, plantar and genital warts pass from person to person."),
  [("Respiratory droplets",
    "Droplet infection from respiratory secretions spreads adenoviruses and parvovirus B19. Human papillomavirus "
    "warts spread by direct contact, including sexual contact, or contaminated fomites.",
    "droplet route borrowed"),
   ("Contaminated food or water",
    "Ingestion of contaminated food or water is a route listed for the polyomaviruses. Human papillomavirus "
    "needs direct contact with the skin or mucosa, including sexual contact, or contact with fomites.",
    "polyoma ingestion route borrowed"),
   ("Blood transfusion",
    "Blood transfusion and blood products transmit hepatitis B virus and human herpesvirus 8. Human "
    "papillomavirus spreads by direct contact, including sexual contact, or fomites.",
    "blood-borne route borrowed")],
  ci(7, 6, 97)),

Q("Human papillomavirus", IO4,
  "Which test is used to screen women for abnormal cervical cells caused by human papillomavirus?",
  ("Pap smear",
   "Correct. Early detection of human papillomavirus disease is by inspection of the genitals and, in women, a "
   "Pap smear to screen for abnormal cervical cells, such as koilocytes. Nine types raise the risk of "
   "reproductive cancer, so screening matters."),
  [("Surface antigen assay",
    "A surface antigen assay, by radioimmunoassay or enzyme-linked immunosorbent assay, diagnoses hepatitis B "
    "virus. Abnormal cervical cells from human papillomavirus are found on a Pap smear.",
    "hepatitis B test borrowed"),
   ("Urine viral shedding",
    "Shedding of virus in urine is a feature of JC polyomavirus latent in the kidney tubules. Cervical cell "
    "changes from human papillomavirus are screened by Pap smear.",
    "JC urine shedding borrowed"),
   ("Liver enzyme levels",
    "Markedly raised liver enzymes mark type 41 adenovirus hepatitis in young children. Human papillomavirus "
    "affects squamous epithelium, and cervical changes are screened by Pap smear.",
    "adenovirus hepatitis test borrowed")],
  c(90, 94, 99, 102)),

Q("Human papillomavirus", IO4,
  "In this Pap smear from a patient with human papillomavirus infection, what is the cell marked by the bracket "
  "on the left pointer?",
  ("A koilocyte",
   "Correct. The bracketed cell is a koilocyte, the abnormal cervical cell seen on a Pap smear in human "
   "papillomavirus infection, set beside a normal cervical cell (the right pointer). The Pap smear is how women "
   "are screened for these abnormal cells."),
  [("A normal cervical cell",
    "The normal cervical cell is the one at the right pointer: a large flat cell with a small nucleus. The "
    "bracketed cell in the cluster on the left is the abnormal one, a koilocyte from human papillomavirus.",
    "other labeled cell in the picture"),
   ("A giant multinucleated cell",
    "Giant multinucleated cells come from scrapings at the base of herpes simplex vesicles. The bracketed cell on "
    "this cervical Pap smear is a koilocyte, the human papillomavirus change.",
    "herpes simplex cell borrowed"),
   ("A liver cancer cell",
    "Human liver cancer cells are used in the laboratory to grow hepatitis B virus from its isolated genome. A "
    "cervical Pap smear in papillomavirus infection shows koilocytes, like the bracketed cell.",
    "hepatitis B culture cell borrowed")],
  ci(100, 66, 86, 99),
  img=IMG + "/l18-fig-16.jpg",
  alt="Stained cervical smear under a microscope: a cluster of blue-staining cells on the left, one of them "
      "marked by a bracket, and a single large flat blue cell with a small nucleus on the right marked by a "
      "pointer line.",
  slide="Slide 100"),

Q("Human papillomavirus", IO4,
  "What happens to most common warts over time?",
  ("They regress",
   "Correct. Most common warts regress over time. They can also be removed physically by cauterization, "
   "freezing or laser surgery, but warts can recur. Common seed warts are painless, raised, rough growths."),
  [("They become malignant",
    "Cancer risk is stated for nine human papillomavirus types and for reproductive cancers, not as the course "
    "of common skin warts. What most common warts do over time is regress, though they can recur.",
    "cancer-risk types generalized"),
   ("They become latent in ganglia",
    "Latency in ganglia is the herpesvirus pattern, such as herpes simplex virus type 1 in the trigeminal "
    "ganglion. Most common warts regress over time, though warts can recur.",
    "herpes latency borrowed"),
   ("They spread to the liver",
    "Spread to the liver fits hepatitis B virus, with its tropism for liver cells. Human papillomavirus causes "
    "local squamous epithelial growths, and most common warts regress over time.",
    "hepatotropic virus borrowed")],
  c(59, 86, 97, 99)),

Q("Human papillomavirus", IO3,
  "Nine human papillomavirus types increase the risk of cancer in which body system?",
  ("Reproductive system",
   "Correct. Nine human papillomavirus types increase the risk of developing reproductive system cancer; "
   "papillomaviruses are linked to cervical and penile cancer. Women are screened by Pap smear for abnormal "
   "cervical cells."),
  [("Hepatic system",
    "Liver cancer, hepatocellular carcinoma, is the cancer risk of chronic hepatitis B virus infection. The "
    "human papillomavirus types raise the risk of reproductive cancers, cervical and penile.",
    "hepatitis B cancer borrowed"),
   ("Lymphatic system",
    "Lymphatic cancer such as Burkitt lymphoma is tied to Epstein-Barr virus. Human papillomavirus types raise "
    "the risk of reproductive system cancers, such as cervical and penile cancer.",
    "Epstein-Barr cancer borrowed"),
   ("Nervous system",
    "The nervous system disease among these deoxyribonucleic acid viruses is progressive multifocal leukoencephalopathy from JC "
    "polyomavirus, a demyelinating infection, not a cancer. Human papillomavirus raises reproductive cancer "
    "risk.",
    "JC disease borrowed")],
  ci(7, 28, 87, 99, 102)),

Q("Human papillomavirus", IO5,
  "Which effective vaccines are available against human papillomavirus?",
  ("Gardasil and Cervarix",
   "Correct. There are two effective human papillomavirus vaccines, Gardasil and Cervarix; vaccines are "
   "available for genital warts. That sets papillomavirus apart from the polyomaviruses, which have no vaccine "
   "for humans."),
  [("JYNNEOS and ACAM2000",
    "JYNNEOS and ACAM2000 are the poxvirus vaccines, used against smallpox and made available to prevent mpox. "
    "The human papillomavirus vaccines are Gardasil and Cervarix.",
    "poxvirus vaccines borrowed"),
   ("A yeast-cloned antigen vaccine",
    "A vaccine from surface antigen cloned in yeast is the hepatitis B vaccine. Human papillomavirus has its own "
    "two named vaccines, Gardasil and Cervarix.",
    "hepatitis B vaccine borrowed"),
   ("An oral types 4 and 7 vaccine",
    "An oral vaccine against types 4 and 7 is the adenovirus vaccine given to some military personnel in "
    "training. Human papillomavirus is prevented with Gardasil or Cervarix.",
    "adenovirus vaccine borrowed")],
  ci(7, 44, 52, 91, 94, 99)),

# ============================================================== POLYOMAVIRUSES (slides 7, 96, 101-102)
Q("Polyomaviruses", IO3,
  "In which hosts do polyomaviruses induce tumors?",
  ("Experimental animals",
   "Correct. Polyomaviruses induce tumors in experimental animals. In humans, JC and BK viruses, the most "
   "important human polyomas, mostly cause asymptomatic or mild infections, with serious disease in "
   "immunosuppressed patients."),
  [("Immunosuppressed humans",
    "Immunosuppressed humans are where JC and BK cause serious disease, progressive multifocal "
    "leukoencephalopathy and renal complications, not tumors. The tumor-inducing property is shown in "
    "experimental animals.",
    "immunosuppressed disease confused with tumors"),
   ("Young children",
    "Young children are when JC virus exposure typically happens, mostly without symptoms. Polyomaviruses are "
    "described as inducing tumors in experimental animals, not in children.",
    "exposure age confused"),
   ("Developing fetuses",
    "Crossing the placenta to cause permanent defects is teratogenic, the property of viruses such as rubella and "
    "cytomegalovirus. Polyomaviruses are noted for inducing tumors in experimental animals.",
    "teratogenic confused")],
  c(28, 96, 101, 102)),

Q("Polyomaviruses", IO5,
  "When are people typically first exposed to BK polyomavirus?",
  ("Early adolescence",
   "Correct. People are typically exposed to BK polyomavirus in early adolescence, whereas JC virus exposure is "
   "possibly in childhood. After an initial cold-like illness, BK lies dormant in the kidney and the lining of "
   "the ureters and bladder."),
  [("Early childhood",
    "Early childhood is the typical exposure for JC polyomavirus. BK polyomavirus is typically picked up in "
    "early adolescence, then lies dormant in the kidney and urinary tract.",
    "JC timing borrowed"),
   ("Before birth",
    "Infection before birth, from mother to fetus, is the route of parvovirus B19 causing hydrops fetalis. BK "
    "polyomavirus exposure is typically in early adolescence.",
    "parvovirus fetal route borrowed"),
   ("At renal transplant",
    "Renal transplant with immunosuppressive drugs is when dormant BK virus causes complications such as "
    "hematuria and nephritis; the first exposure came years earlier, typically in early adolescence.",
    "reactivation mistaken for exposure")],
  ci(7, 101, 102, 104)),

Q("Polyomaviruses", IO2,
  "After initial infection through the tonsils or gastrointestinal tract, where does JC polyomavirus remain "
  "latent?",
  ("Gut and kidney tubular cells",
   "Correct. After initial infection via the tonsils or gastrointestinal tract, JC virus is latent in the "
   "gastrointestinal tract and the tubular epithelial cells of the kidneys, shedding virus in urine. It can cross "
   "the blood-brain barrier in immunosuppressed patients."),
  [("The trigeminal ganglion",
    "The trigeminal ganglion is where herpes simplex virus type 1 stays latent after entering the fifth cranial "
    "nerve. JC polyomavirus stays latent in the gastrointestinal tract and kidney tubular cells.",
    "herpes latency site borrowed"),
   ("Liver cells",
    "Liver cells are where hepatitis B virus multiplies exclusively, seeding the blood in a chronic infection. "
    "JC polyomavirus is latent in the gastrointestinal tract and the tubular epithelium of the kidneys.",
    "hepatitis B site borrowed"),
   ("Lymphoid tissue",
    "Lymphoid tissue, along with respiratory and intestinal epithelia and conjunctiva, is what adenoviruses "
    "infect. JC polyomavirus lies latent in the gastrointestinal tract and kidney tubular cells.",
    "adenovirus tissues borrowed")],
  c(59, 87, 93, 102)),

Q("Polyomaviruses", IO4,
  "Which property lets JC polyomavirus cause progressive multifocal leukoencephalopathy in immunosuppressed "
  "patients?",
  ("It can cross the blood-brain barrier",
   "Correct. JC virus can cross the blood-brain barrier, and in immunosuppressed patients it destroys the "
   "cells that produce myelin, causing progressive multifocal leukoencephalopathy, an uncommon, often fatal "
   "infection."),
  [("It enters the fifth cranial nerve",
    "Entering the fifth cranial nerve is how herpes simplex virus type 1 reaches the trigeminal ganglion. JC "
    "virus reaches the brain by crossing the blood-brain barrier.",
    "herpes neural route borrowed"),
   ("It is a defective helper virus",
    "A defective virus that cannot replicate without a helper is adeno-associated virus, which needs adenovirus. "
    "JC virus replicates on its own and causes brain disease by crossing the blood-brain barrier.",
    "adeno-associated virus trait borrowed"),
   ("It multiplies only in the liver",
    "Multiplying exclusively in the liver is hepatitis B virus. JC virus is latent in the gut and kidney tubules "
    "and, by crossing the blood-brain barrier, destroys myelin-producing cells.",
    "hepatitis B trait borrowed")],
  c(86, 87, 102, 106)),

Q("Polyomaviruses", IO5,
  "Which vaccine is available against the human polyomaviruses JC and BK?",
  ("None for humans",
   "Correct. There is no vaccine for humans against the polyomaviruses, JC and BK. They are most prevalent as "
   "disease in immunosuppressed populations: JC causing progressive multifocal leukoencephalopathy and BK renal "
   "complications."),
  [("Gardasil or Cervarix",
    "Gardasil and Cervarix are the two effective human papillomavirus vaccines. The papilloma and polyoma viruses "
    "share their small circular genome, but no vaccine is available for humans against polyomaviruses.",
    "papillomavirus vaccine borrowed"),
   ("A yeast-cloned antigen",
    "Surface antigen cloned in yeast is the hepatitis B vaccine. For the human polyomaviruses, JC and BK, no "
    "vaccine is available for humans; they are most prevalent as disease in immunosuppressed populations.",
    "hepatitis B vaccine borrowed"),
   ("An oral polyvalent one",
    "An oral polyvalent vaccine against types 4 and 7 is the adenovirus vaccine for some military personnel in "
    "training. The polyomaviruses have no vaccine for humans.",
    "adenovirus vaccine borrowed")],
  ci(7, 91, 94, 99)),

# ============================================================== PARVOVIRUS B19 (slides 7, 103-105)
Q("Parvovirus B19", IO4,
  "Which description fits the parvoviruses?",
  ("Small, nonenveloped, single-stranded",
   "Correct. Parvoviruses are nonenveloped, single-stranded deoxyribonucleic acid (DNA) viruses with a small "
   "diameter and genome size. In animals they cause distemper in cats, enteric disease in dogs and fatal cardiac "
   "infection in puppies; in humans B19 causes fifth disease."),
  [("Small, nonenveloped, circular double-stranded",
    "Small, nonenveloped viruses with circular double-stranded deoxyribonucleic acid (DNA) are the papilloma and "
    "polyoma viruses. Parvoviruses are also small and bare but carry single-stranded deoxyribonucleic acid.",
    "papilloma/polyoma structure borrowed"),
   ("Enveloped, partly single-stranded",
    "An envelope and a partly single-, partly double-stranded genome describe hepatitis B virus, a "
    "hepadnavirus. Parvoviruses have no envelope and a fully single-stranded genome.",
    "hepadnavirus structure borrowed"),
   ("Nonenveloped, double-stranded, acute",
    "Nonenveloped, double-stranded viruses causing acute infection are the adenoviruses. Parvoviruses are "
    "smaller still and single-stranded, the clue that separates them.",
    "adenovirus structure borrowed")],
  c(86, 93, 96, 103)),

Q("Parvovirus B19", IO5,
  "A pregnant woman transmits parvovirus B19 to her fetus. Which outcome can follow?",
  ("Hydrops fetalis",
   "Correct. If a pregnant woman transmits parvovirus B19 to her fetus, severe, fatal anemia can result, leading "
   "to hydrops fetalis. In children the same virus causes fifth disease, and in adults polyarthropathy or "
   "cessation of red cell production."),
  [("Erythema infectiosum",
    "Erythema infectiosum, fifth disease, is the childhood illness from parvovirus B19, with fever and a rash on "
    "the cheeks. Passed from mother to fetus, the virus causes fatal anemia and hydrops fetalis.",
    "childhood form confused with fetal"),
   ("Polyarthropathy",
    "Polyarthropathy with massive joint swelling is how parvovirus B19 can affect adults. Transmission to the "
    "fetus instead causes severe anemia and hydrops fetalis.",
    "adult form confused with fetal"),
   ("Hemorrhagic cystitis",
    "Hemorrhagic cystitis comes from BK polyomavirus after renal transplant and from adenoviruses. Parvovirus B19 "
    "passed to a fetus gives severe anemia and hydrops fetalis.",
    "urinary disease borrowed")],
  ci(7, 93, 102, 104)),

Q("Parvovirus B19", IO4,
  "Besides polyarthropathy with massive joint swelling, which problem can parvovirus B19 cause in adults?",
  ("Cessation of red cell production",
   "Correct. In adults, parvovirus B19 can cause a polyarthropathy syndrome with massive swelling of joints or "
   "can stop red blood cell production, causing anemia. In children it causes fifth disease, and in the fetus "
   "hydrops fetalis."),
  [("Hydrops fetalis",
    "Hydrops fetalis is the fetal outcome when a pregnant woman passes parvovirus B19 to her fetus, from severe "
    "anemia. In the adult the virus causes polyarthropathy or cessation of red cell production.",
    "fetal form confused with adult"),
   ("Loss of myelin-making cells",
    "Destruction of myelin-producing cells is progressive multifocal leukoencephalopathy from JC polyomavirus. "
    "Parvovirus B19 in adults causes joint swelling or stops red blood cell production.",
    "JC disease borrowed"),
   ("Hepatocellular carcinoma",
    "Hepatocellular carcinoma is the liver cancer risk of chronic hepatitis B virus infection. Parvovirus B19 in "
    "adults causes polyarthropathy or cessation of red blood cell production.",
    "hepatitis B cancer borrowed")],
  ci(7, 87, 102, 104)),

Q("Parvovirus B19", IO5,
  "Erythema infectiosum is the fifth rash disease of childhood. Which is one of the other four?",
  ("Roseola",
   "Correct. Erythema infectiosum (fifth disease, from parvovirus B19) is the fifth rash disease of childhood; the "
   "other four are chickenpox, measles, rubella and roseola. Roseola, from human herpesviruses 6 and 7, is an "
   "acute febrile disease followed by rash."),
  [("Molluscum contagiosum",
    "Molluscum contagiosum is a poxvirus skin infection with small, smooth, waxy lesions, often in the genital "
    "area and on the thighs, not one of the childhood rash diseases. Those are chickenpox, measles, rubella and "
    "roseola.",
    "poxvirus skin lesion confused"),
   ("Infectious mononucleosis",
    "Infectious mononucleosis is Epstein-Barr virus disease with sore throat, high fever, cervical "
    "lymphadenopathy and splenomegaly. The rash diseases of childhood listed with fifth disease are chickenpox, "
    "measles, rubella and roseola.",
    "Epstein-Barr disease confused"),
   ("Infantile gastroenteritis",
    "Infantile gastroenteritis is an adenovirus disease of the intestinal epithelium, without a defining rash. "
    "The other four childhood rash diseases are chickenpox, measles, rubella and roseola.",
    "adenovirus disease confused")],
  ci(6, 46, 81, 93, 104)),

Q("Parvovirus B19", IO5,
  "How is parvovirus B19 transmitted?",
  ("Droplet infection",
   "Correct. Parvovirus B19 spreads by droplet infection. It causes fifth disease in children, with a slapped-face "
   "rash and low-grade fever, hydrops fetalis when passed to a fetus, and polyarthropathy in adults."),
  [("Blood or serum contact",
    "Contact with blood or serum, plus sexual contact, is the route of hepatitis B virus. Parvovirus B19, the "
    "cause of the slapped-face rash of fifth disease, spreads by droplet infection.",
    "hepatitis B route borrowed"),
   ("Direct skin contact",
    "Direct contact, including sexual contact, or fomites spreads human papillomavirus warts on the skin. "
    "Parvovirus B19 instead spreads by droplet infection, the same route as the adenoviruses.",
    "papillomavirus route borrowed"),
   ("Contaminated food",
    "Ingestion of contaminated food or water is a route listed for the polyomaviruses. Parvovirus B19 spreads "
    "by droplet infection, a route it shares with the adenoviruses and their respiratory secretions.",
    "polyoma ingestion route borrowed")],
  ci(7, 6)),

# ============================================================== ADENO-ASSOCIATED VIRUS (slide 106)
Q("Adeno-associated virus", IO1,
  "Adeno-associated virus is a defective parvovirus. What does it need to replicate in a host cell?",
  ("Co-infection with adenovirus",
   "Correct. Adeno-associated virus is a defective parvovirus: it cannot replicate in the host cell without "
   "adenovirus. By itself it is not known to cause disease, although co-infection with an adenovirus that causes "
   "hepatitis may make that infection more severe."),
  [("Co-infection with hepatitis B virus",
    "Hepatitis B virus is the partner of hepatitis D, the delta agent, whose co-infection worsens severe "
    "hepatitis B. Adeno-associated virus depends on adenovirus to replicate.",
    "delta agent pairing borrowed"),
   ("Co-infection with BK polyomavirus",
    "BK polyomavirus lies dormant in the kidney and the lining of the ureters and bladder. Adeno-associated "
    "virus, a defective parvovirus, cannot replicate without adenovirus.",
    "unrelated deoxyribonucleic acid virus"),
   ("A bacterial host cell",
    "Bacterial host cells are what bacteriophages infect. As a defective parvovirus, adeno-associated virus "
    "needs adenovirus present to replicate.",
    "phage host borrowed")],
  c(13, 88, 102, 106)),

Q("Adeno-associated virus", IO4,
  "For what is adeno-associated virus now used in medicine?",
  ("A vector for gene therapy",
   "Correct. Adeno-associated virus is now used as a viral vector for human gene therapy and is currently "
   "approved to treat lipoprotein lipase deficiency, with trials in cystic fibrosis, eye diseases, hemophilia and "
   "neurodegenerative diseases. Alone it is not known to cause disease."),
  [("A smallpox vaccine",
    "The smallpox vaccines use live vaccinia virus, such as ACAM2000. Adeno-associated virus, a defective "
    "parvovirus, serves instead as a vector to deliver genes in human gene therapy.",
    "vaccinia role borrowed"),
   ("A host for viral culture",
    "Human liver cancer cells serve as the culture host for hepatitis B virus, which is hard to grow. "
    "Adeno-associated virus is a gene therapy vector, approved for lipoprotein lipase deficiency.",
    "culture host confused"),
   ("A military vaccine",
    "The vaccine given to some military personnel in training is against adenovirus types 4 and 7. "
    "Adeno-associated virus is a different agent, used as a vector for human gene therapy.",
    "adenovirus vaccine borrowed")],
  c(44, 86, 94, 106)),
]

CLUSTERS_D = [
    # genome/structure items: each lists the other viruses' genomes as replacing facts
    (1, ["What is unusual about the genome of hepatitis B", "Which description fits the adenovirus virion",
         "Which description fits the parvoviruses"]),
    # oncogenic-host items: adenovirus (animals not humans) vs polyoma (experimental animals)
    (1, ["In which hosts are adenoviruses oncogenic", "In which hosts do polyomaviruses induce tumors"]),
    # adeno-associated virus with adenovirus: one stem names the pairing the other asks
    (1, ["Some of the most serious cases of adenovirus type 41", "Adeno-associated virus is a defective"]),
    # hepatitis D: the delta-agent co-infection is keyed in one and a distractor in the other
    (1, ["Co-infection with which agent can make severe", "Of the three principal viruses that cause"]),
    # passive immunization vs blood-derived vaccine: same recipients named across both
    (1, ["Who mainly receives the hepatitis B vaccine", "A newborn's mother is infected with hepatitis B"]),
    # Pap smear screening vs koilocyte picture (stem names Pap smear)
    (1, ["Which test is used to screen women", "In this Pap smear from a patient"]),
    # parvovirus B19 fetal vs adult outcomes
    (1, ["A pregnant woman transmits parvovirus B19", "Besides polyarthropathy with massive joint"]),
]
