# -*- coding: utf-8 -*-
"""Lecture 19 objective-style pool A -- Oral Cavity, Salivary Glands and Neck."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q

IO = ("Disorders of the oral cavity, salivary glands, and neck: etiologies, epidemiology, risk "
      "factors, clinical manifestations, differential diagnosis, diagnostic testing, management, "
      "referrals, patient education, and prognosis")
C = lambda n: "CMS I Disorders of the Oral Cavity, Salivary Glands, Slide %d" % n

QUESTIONS = [

Q("Oral mucosa variants", IO, "What distinguishes leukoedema from leukoplakia at the bedside?",
  [["Leukoedema disappears when the mucosa is stretched",
    "Correct. Leukoedema is a normal variant caused by fluid accumulating within epithelial cells, "
    "so stretching the mucosa disperses it and the greyish-white change vanishes. Leukoplakia is a "
    "premalignant lesion that cannot be scraped off or stretched away, which is why this single "
    "manoeuvre separates a reassurance from a biopsy."],
   ["Leukoedema can be scraped off with a tongue depressor",
    "Scraping off is the test for CANDIDIASIS, which forms a removable pseudomembrane. Leukoedema is "
    "a change within the epithelium itself and does not wipe away."],
   ["Leukoedema is painful and leukoplakia is not",
    "Both are painless. Pain is not a discriminator between them, and expecting it would delay "
    "recognising a premalignant lesion."],
   ["Leukoedema occurs only on the tongue",
    "Leukoedema is characteristically a diffuse change of the BUCCAL mucosa. Site is not the "
    "distinguishing feature in any case."]], C(9)),

Q("Oral mucosa variants", IO, "What are Fordyce granules?",
  [["Ectopic sebaceous glands",
    "Correct. Fordyce granules are normal variants: sebaceous glands appearing where sebaceous "
    "glands are not usually expected, on the vermilion of the lip and the buccal mucosa. They "
    "present as small yellow-white papules and need nothing but recognition and reassurance."],
   ["Premalignant squamous lesions",
    "Premalignant white lesions are leukoplakia, defined as unable to be scraped off, with 5 to 20 "
    "per cent progressing to squamous cell carcinoma. Fordyce granules carry no such risk."],
   ["Deposits of melanin",
    "Melanin deposition gives physiologic oral pigmentation, another normal variant, but it appears "
    "as brown-grey colouration rather than yellow-white papules."],
   ["Fungal colonies within the epithelium",
    "Fungal disease gives creamy white curd-like patches that wipe off, revealing an erythematous "
    "base. Fordyce granules are fixed anatomical structures."]], C(10)),

Q("Stomatitis", IO, "Which of these is a listed cause of stomatitis?",
  [["Chemotherapy or radiation",
    "Correct. The causes listed include trauma from ill-fitting dentures or braces, cheek and tongue "
    "biting, surgery, chemotherapy and radiation, viral infection with herpes or coxsackievirus, "
    "candidiasis, xerostomia, tobacco, nutritional deficiency of zinc or iron, allergy, and "
    "idiopathic aphthous ulceration."],
   ["Excessive fluoride intake",
    "Fluorosis mottles enamel and is a disorder of the teeth rather than a cause of mucosal "
    "inflammation. It does not appear on the stomatitis list."],
   ["Hypercalcaemia",
    "Hypercalcaemia produces thirst, constipation, confusion and renal stones. It has no place among "
    "the causes of oral mucosal inflammation."],
   ["Chronic sinusitis",
    "Chronic sinusitis causes postnasal drip and can irritate the pharynx, contributing to chronic "
    "pharyngitis, but it does not inflame the oral mucosa."]], C(13)),

Q("Aphthous stomatitis", IO,
  "On which type of mucosa do aphthous ulcers characteristically occur?",
  [["Freely moving, non-keratinised mucosa",
    "Correct. Aphthae are found on buccal and labial mucosa, non-attached gingiva and palate, all of "
    "which are freely moving and non-keratinised. That location rule is the practical way to "
    "separate them from herpetic lesions, which favour keratinised surfaces."],
   ["Keratinised, attached mucosa",
    "Keratinised attached surfaces such as the hard palate and attached gingiva are where primary "
    "HERPETIC lesions appear. Reversing the rule swaps two diagnoses with different treatments."],
   ["The dorsum of the tongue only",
    "The dorsal tongue is keratinised and is not the characteristic site. Aphthae can involve the "
    "tongue but the rule concerns mucosal type rather than a single location."],
   ["The tonsillar fossae",
    "Ulcerative vesicles over the tonsils describe herpangina, a feature of viral pharyngitis, "
    "rather than aphthous ulceration."]], C(15)),

Q("Aphthous stomatitis", IO, "How are minor aphthous ulcers characterised?",
  [["Under 1 centimetre, commonest, healing in 7 to 10 days",
    "Correct. Minor aphthae are the commonest form, under a centimetre, preceded by burning and "
    "tingling, painful, and healing within 7 to 10 days without scarring. Major ulcers exceed a "
    "centimetre, are more painful, may scar and last over a month; herpetiform ulcers are numerous "
    "1 to 3 millimetre lesions that also scar and persist."],
   ["Over 1 centimetre with a risk of scarring",
    "Those are MAJOR aphthae, which are more painful, often multiple, and last over a month. Size is "
    "the dividing line."],
   ["Numerous 1 to 3 millimetre ulcers",
    "That describes the HERPETIFORM variant, which carries a scarring risk and lasts over a month "
    "despite the name having nothing to do with herpes."],
   ["Painless lesions healing within 24 hours",
    "Aphthae are notably painful, and none of the three forms resolves within a day &mdash; the "
    "shortest is 7 to 10 days."]], C(16)),

Q("Aphthous stomatitis", IO, "What is recurrent aphthous stomatitis also called?",
  [["Sutton disease",
    "Correct. Recurrent aphthous stomatitis carries the eponym Sutton disease. The condition is "
    "self-limiting and managed with observation, with anti-inflammatories, corticosteroids, silver "
    "nitrate cauterisation and dilute rinses as options for symptom control."],
   ["Behcet syndrome",
    "Behcet is a multisystem inflammatory disorder in which oral ulcers are the commonest feature, "
    "affecting up to 100 per cent, with genital ulcers in about 75 per cent. Recurrent oral ulcers "
    "alone do not make that diagnosis."],
   ["Ludwig angina",
    "Ludwig angina is a severe infection of the floor of the mouth and the submental, sublingual and "
    "submandibular spaces, threatening the airway."],
   ["Sjogren syndrome",
    "Sjogren syndrome causes dry mouth and eyes from autoimmune destruction of exocrine glands, and "
    "appears among the non-infectious inflammatory causes of neck masses."]], C(17)),

Q("Behcet syndrome", IO,
  "What proportion of patients with Behcet syndrome have oral ulcers?",
  [["Up to 100 per cent",
    "Correct. Oral ulcers are the commonest feature of Behcet, affecting up to 100 per cent of "
    "patients, with genital ulcers in about 75 per cent that look identical to oral aphthae. "
    "Diagnosis is clinical: recurrent aphthous ulceration in the context of the characteristic "
    "systemic manifestations."],
   ["About 10 per cent",
    "If oral ulcers were uncommon they could not serve as the entry point to the diagnosis, which is "
    "how they are actually used."],
   ["About 40 per cent",
    "Forty per cent is the figure for mucous membrane involvement in systemic LUPUS, which is a "
    "different disorder with different oral findings."],
   ["About 75 per cent",
    "Seventy-five per cent is the figure for GENITAL ulcers in Behcet. The two proportions are easy "
    "to swap."]], C(19)),

Q("Oral lichen planus", IO, "What are Wickham striae?",
  [["Lacy white lines on the buccal mucosa",
    "Correct. The reticular form of oral lichen planus produces lacy white lines called Wickham "
    "striae, most often on the buccal mucosa but also on palate, lips and tongue. They are part of "
    "the mucosa and cannot be wiped away, which distinguishes them from candidiasis."],
   ["Creamy patches that wipe off",
    "Removable creamy patches on an erythematous base are oral candidiasis, treated with topical "
    "antifungals rather than with the steroids used for lichen planus."],
   ["Yellow-grey ulcer centres with a red halo",
    "That describes aphthous ulceration, which occurs on freely moving non-keratinised mucosa and "
    "heals within 7 to 10 days in its minor form."],
   ["Ectopic sebaceous glands on the lip",
    "Those are Fordyce granules, a normal variant appearing as small yellow-white papules."]],
  C(21)),

Q("Oral lichen planus", IO,
  "What proportion of oral lichen planus progresses to squamous cell carcinoma?",
  [["1 to 4 per cent, higher with ulcerative lesions",
    "Correct. The malignant potential is modest but real, and it is higher in ulcerative forms. That "
    "is the reason close follow-up is the point of making the diagnosis, alongside pain relief and "
    "removing reversible contributors such as medications, dental restorations, tobacco and "
    "alcohol."],
   ["None; it is entirely benign",
    "Treating it as entirely benign removes the follow-up, which is the main clinical consequence of "
    "recognising the condition."],
   ["Around 90 per cent",
    "Ninety per cent dysplastic or malignant is the figure for ERYTHROPLAKIA, a far more dangerous "
    "red lesion."],
   ["5 to 20 per cent",
    "That is the transformation range quoted for LEUKOPLAKIA. Lichen planus carries a lower risk, "
    "which is why the two figures are worth keeping apart."]], C(22)),

Q("Systemic lupus erythematosus", IO,
  "What proportion of patients with systemic lupus have mucous membrane involvement?",
  [["About 40 per cent",
    "Correct. Around 40 per cent of lupus patients have mucous membrane involvement, and oral "
    "lesions may be the FIRST sign of the disease. There is no correlation between the oral ulcers "
    "and systemic activity, so they cannot be used to judge control."],
   ["About 5 per cent",
    "Five per cent would make oral involvement a rarity, when in fact it is common enough that an "
    "oral lesion can be the presenting feature."],
   ["About 90 per cent",
    "Near-universal involvement would make oral examination almost diagnostic on its own, which is "
    "not the case."],
   ["About 75 per cent",
    "Seventy-five per cent is the proportion of Behcet patients with genital ulcers, a different "
    "disease and a different figure."]], C(23)),

Q("Herpes simplex", IO,
  "What is the commonest clinical manifestation of primary herpes simplex infection?",
  [["Herpetic gingivostomatitis",
    "Correct. Primary infection presents as herpetic gingivostomatitis, most often in seronegative "
    "children and young adults, with fever, malaise and cervical lymphadenopathy alongside the oral "
    "lesions. Secondary disease is reactivation of virus dormant in the trigeminal ganglion."],
   ["A single cold sore at the lip margin",
    "A solitary perioral lesion is the pattern of SECONDARY, recurrent disease, arising from "
    "reactivation and preceded by a burning prodrome."],
   ["Herpangina",
    "Herpangina is ulcerative vesicles over the tonsils and is a feature of viral pharyngitis, "
    "usually coxsackievirus."],
   ["Hairy leukoplakia",
    "Hairy leukoplakia is associated with Epstein-Barr virus and strongly with HIV, appearing as "
    "painless lateral tongue lesions."]], C(25)),

Q("Herpes simplex", IO, "Where does herpes simplex virus lie dormant between recurrences?",
  [["The trigeminal ganglion",
    "Correct. After primary infection the virus travels along the axon to the trigeminal ganglion "
    "and persists there. Reactivation is triggered by stress, trauma, immunosuppression or "
    "ultraviolet light, and the virus migrates back along the axonal sheath, which is why a burning "
    "prodrome precedes the visible lesion by about 24 hours."],
   ["The salivary glands",
    "Cytomegalovirus and mumps involve salivary tissue, but herpes simplex latency is neuronal. The "
    "prodrome of burning and tingling is the clinical evidence of that."],
   ["The regional lymph nodes",
    "Nodes enlarge during primary infection but do not harbour latent virus. Latency is established "
    "in sensory neurons."],
   ["The oral epithelium itself",
    "If the virus persisted in the epithelium the lesions would not follow a dermatomal or neural "
    "distribution and there would be no neurological prodrome."]], C(25)),

Q("Herpes simplex", IO, "Which test is most sensitive and specific for herpes simplex?",
  [["Polymerase chain reaction for HSV DNA",
    "Correct. Diagnosis is often clinical when characteristic lesions are present, but confirmation "
    "is by polymerase chain reaction for viral DNA, which is the most sensitive and specific option. "
    "Serology with IgG and IgM helps distinguish HSV 1 from HSV 2."],
   ["Tzanck smear",
    "A Tzanck smear shows multinucleated giant cells, but those also appear in varicella zoster "
    "infection, so it cannot distinguish the two and is not the best test."],
   ["Viral culture",
    "Culture is described as the definitive test but is slower and less sensitive than polymerase "
    "chain reaction, particularly once lesions have begun to crust."],
   ["Potassium hydroxide preparation",
    "A potassium hydroxide preparation reveals spores and pseudohyphae and is the test for oral "
    "CANDIDIASIS, not for a virus."]], C(27)),

Q("Salivary anatomy", IO, "Which duct drains the parotid gland?",
  [["Stensen duct",
    "Correct. The parotid glands lie on the sides of the face and drain through Stensen duct, which "
    "crosses the masseter and opens opposite the upper second molar. That is where pus is expressed "
    "from in acute suppurative sialadenitis, which is characteristically a parotid disease."],
   ["Wharton duct",
    "Wharton duct drains the SUBMANDIBULAR gland, and its long upward course carrying alkaline "
    "mucin-rich saliva is why 80 to 90 per cent of stones form there."],
   ["The sublingual ducts",
    "The sublingual gland drains through multiple small ducts into the floor of the mouth, and it is "
    "the source of a ranula."],
   ["The nasolacrimal duct",
    "The nasolacrimal duct drains tears from the eye into the nose. It has nothing to do with "
    "salivary glands."]], C(29)),

Q("Salivary anatomy", IO,
  "Why do 80 to 90 per cent of salivary stones form in the submandibular gland?",
  [["Its duct is long and uphill, and its saliva is alkaline and mucin-rich",
    "Correct. Wharton duct runs a longer course and against gravity, and submandibular saliva has "
    "higher mucin and alkaline content with high concentrations of calcium and phosphate. Those "
    "conditions favour precipitation of calcium phosphate and carbonate, which is what a stone is."],
   ["It is the largest salivary gland",
    "The parotid is the largest of the major salivary glands, and size is not what determines stone "
    "formation in any case."],
   ["It produces the most saliva overall",
    "Salivary volume is not the driver. The composition and the duct anatomy are what matter."],
   ["It is the most exposed to oral bacteria",
    "Bacterial ascent explains suppurative sialadenitis, which is chiefly a PAROTID disease. Stones "
    "are a physicochemical problem rather than an infective one."]], C(40)),

Q("Acute suppurative sialadenitis", IO,
  "Which organism most commonly causes acute suppurative sialadenitis?",
  [["Staphylococcus aureus",
    "Correct. Staphylococcus aureus is the commonest pathogen, followed by Streptococcus viridans, "
    "Haemophilus influenzae, Streptococcus pyogenes and gram-negatives, with Candida in chronically "
    "ill hospitalised patients. That is why treatment uses penicillinase-resistant gram-positive "
    "cover such as nafcillin or cefazolin."],
   ["Pseudomonas aeruginosa",
    "Pseudomonas is the organism of malignant otitis externa and of swimmer's ear, favoured by a "
    "moist alkaline canal rather than by salivary stasis."],
   ["Streptococcus pneumoniae",
    "Pneumococcus is a middle ear and sinus pathogen rather than the leading salivary one, though "
    "streptococci do feature further down the list."],
   ["Candida albicans",
    "Candida appears in chronically ill hospitalised patients, so it is on the list, but it is not "
    "the usual organism in an otherwise typical case."]], C(35)),

Q("Acute suppurative sialadenitis", IO,
  "Which gland is most commonly affected by acute suppurative sialadenitis?",
  [["The parotid",
    "Correct. Infection ascends the parotid duct and then spreads haematogenously, and salivary "
    "stasis is the initiating event. The gland becomes firm and diffusely tender with overlying "
    "erythema, trismus, purulent ductal discharge, induration, fever and chills, typically "
    "unilaterally in acute disease."],
   ["The submandibular",
    "The submandibular gland is the commonest site of STONES rather than of suppurative infection, "
    "though submandibular sialadenitis exists and can mimic Ludwig angina if treatment fails."],
   ["The sublingual",
    "The sublingual gland is the source of a ranula and accounts for a very small share of salivary "
    "pathology overall."],
   ["The minor salivary glands",
    "Minor glands are relevant chiefly for neoplasia, where only about 35 per cent of tumours are "
    "benign, rather than for suppurative infection."]], C(36)),

Q("Acute suppurative sialadenitis", IO,
  "What should be presumed if there is no improvement after 48 hours of conservative treatment?",
  [["An abscess has formed",
    "Correct. Failure to improve within 48 hours of rehydration, antibiotics, warm compresses, "
    "massage and sialogogues means an abscess should be presumed. The gland becomes indurated with a "
    "dough-like consistency, and ultrasound or computed tomography locates the loculation for "
    "drainage or guided aspiration."],
   ["The diagnosis was wrong and it is a tumour",
    "A neoplasm presents as a slow-growing painless mass rather than an acutely tender infected "
    "gland, so a tumour would not explain the original picture."],
   ["The organism is fungal",
    "Candida features in chronically ill hospitalised patients, so it is worth considering in that "
    "group, but the stated presumption after 48 hours is a collection rather than a change of "
    "organism."],
   ["Treatment should simply be continued for another week",
    "Continuing without reassessment allows an abscess to enlarge, and the 48-hour mark exists "
    "precisely as a decision point."]], C(38)),

Q("Sialolithiasis", IO,
  "What is the characteristic symptom pattern of sialolithiasis?",
  [["Recurrent swelling and pain that worsens with eating",
    "Correct. Eating stimulates salivary flow, and an obstructing stone traps that saliva behind it, "
    "distending the gland until pressure equalises. That is salivary colic, and it is why the "
    "history alone often makes the diagnosis before any imaging."],
   ["Constant swelling with fever and pus from the duct",
    "That describes acute suppurative sialadenitis, typically in a dehydrated post-operative or "
    "elderly patient, and it does not fluctuate with meals."],
   ["Painless progressive enlargement over months",
    "Painless slow growth suggests a neoplasm, most often at the tail of the parotid, where 75 to 80 "
    "per cent are benign."],
   ["Bilateral swelling with systemic viral symptoms",
    "Bilateral parotid swelling with systemic symptoms suggests mumps, caused by a paramyxovirus."]],
  C(42)),

Q("Sialolithiasis", IO, "Which imaging method is most sensitive for detecting salivary stones?",
  [["Computed tomography",
    "Correct. Computed tomography is the most sensitive method for detecting stones because it "
    "resolves small calcifications anywhere in the gland or duct. Digital subtraction sialography is "
    "described separately as the most ACCURATE method, and the two claims are deliberately "
    "distinguished."],
   ["Plain radiography",
    "Submandibular stones are calcium phosphate and hydroxyapatite and are therefore radiopaque and "
    "visible on plain films, but films miss radiolucent and small stones."],
   ["Ultrasound",
    "Ultrasound shows an echogenic structure with an acoustic shadow and is a reasonable first test, "
    "being cheap and radiation-free, but it is less sensitive and operator-dependent."],
   ["Magnetic resonance imaging",
    "Magnetic resonance shows soft tissue well but is comparatively poor at demonstrating "
    "calcification, which is exactly what a stone is."]], C(42)),
]
