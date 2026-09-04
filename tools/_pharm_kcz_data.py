# -*- coding: utf-8 -*-
"""Killers, commons and zebras -- Pharmacology I Exam 1.

The framework is Dr. Wood's, given at the exam review on 3 September:

    "I typically break them up into three categories. There's the killers,
     the commons and the zebras."

  KILLERS  dangerous; require immediate discontinuation and evaluation. Not
           necessarily common -- these are the ones the patient is warned about
           in advance so they do not mistake them for normal.
  COMMONS  what actually happens often. HE SAID THESE BELONG TO THE GROUP, NOT
           THE DRUG -- asked whether the common effects of penicillins,
           cephalosporins and carbapenems need learning separately, he said
           "no, they're all the same". So the commons here are listed by group.
  ZEBRAS   uncommon, but UNIQUE TO ONE DRUG. His steer: "any time you see those
           killers or the zebras, those are always things you should look at."

`his=True` marks the entries HE named himself at the review. Everything else is
the deck's own adverse-effect list sorted by his stated criteria -- the sorting
is an application of his framework, not a claim that he assigned that bucket.
Every entry cites the slide it comes from.
"""
L1 = "Antibiotics, Antivirals, and Antifungals"
L2 = "Dermatology Medications"
L3 = "ANS Pharmacology"

# effect, drug(s), what it means / what to do, deck, slide, his
KILLERS = [
 ("Anaphylaxis", "Penicillins &mdash; the whole class, and the carbapenems and monobactam",
  "The deck asks for monitoring for signs and symptoms of anaphylaxis on the natural "
  "penicillins, the penicillinase-resistant penicillins, the antipseudomonal penicillins, "
  "aztreonam and the carbapenems &mdash; five separate slides. <b>Stop the drug and evaluate.</b>",
  L1, 17, True),
 ("Stevens-Johnson syndrome and toxic epidermal necrolysis",
  "aminopenicillins; sulfamethoxazole/trimethoprim",
  "<b>His own example of a killer.</b> Skin sloughing is not a side effect to tolerate &mdash; "
  "he made the point that patients must be told in advance so they do not assume it is normal.",
  L1, 21, True),
 ("Suicidal ideation and worsening depression", "isotretinoin",
  "<b>His own example of a killer.</b> The deck instructs monitoring for signs of developing "
  "depression, and the drug is also contraindicated in pregnancy and breastfeeding with the "
  "iPledge programme attached.",
  L2, 27, True),
 ("Clostridioides difficile infection and pseudomembranous colitis",
  "clindamycin; aminopenicillins; fluoroquinolones",
  "Clindamycin is the one classically named for it. <b>Stop the antibiotic and treat.</b>",
  L1, 81, False),
 ("Torsades de pointes from QT prolongation", "macrolides; fluoroquinolones; azoles",
  "The deck gives QT prolongation its own slide. On the fluoroquinolones it is listed with "
  "torsades by name. <b>An arrhythmia, not an inconvenience.</b>",
  L1, 58, False),
 ("Serotonin syndrome", "linezolid",
  "Listed on the linezolid slide with its triggers: <b>selective serotonin reuptake inhibitors, "
  "tyramine-containing foods and pseudoephedrine</b>. Linezolid is a monoamine oxidase "
  "inhibitor, which is why an antibiotic is on this list at all.",
  L1, 71, False),
 ("Seizures", "carbapenems; acyclovir and ganciclovir at high levels",
  "On the carbapenem slide directly. It is the reason the class is not simply the safe "
  "broad-spectrum default.",
  L1, 44, False),
]

# group, the effect, note, deck, slide, his
COMMONS = [
 ("Every antibiotic", "Gastrointestinal upset &mdash; nausea, vomiting, diarrhoea",
  "<b>His own example, and the whole point of the bucket.</b> Almost every antibiotic causes "
  "this in somebody. Tell the patient it is expected; it may or may not warrant changing "
  "therapy.", L1, 22, True),
 ("All beta-lactams &mdash; penicillins, cephalosporins, carbapenems",
  "Hypersensitivity reaction, rash, diarrhoea",
  "<b>Do not learn these three classes' common effects separately.</b> Asked exactly that, he "
  "said: <i>&ldquo;no, they're all the same&rdquo;</i>. Learn the shared set once and spend the "
  "effort where a class breaks the pattern.", L1, 22, True),
 ("Penicillins", "Renal and hepatic monitoring, platelets",
  "Dosing frequency falls with renal impairment.", L1, 22, False),
 ("Vancomycin", "Renal clearance monitoring", "Trough levels are checked to confirm efficacy.",
  L1, 51, False),
 ("Aminoglycosides", "Ototoxicity and nephrotoxicity",
  "Common enough in this class to be the reason troughs are checked at all &mdash; the target "
  "is an <b>undetectable</b> trough, because it is accumulation that harms.", L1, 68, False),
 ("Topical retinoids", "Retinoid dermatitis &mdash; erythema, pruritus, scaling",
  "Expected with the class rather than a reason to stop.", L2, 24, False),
]

# effect, the one drug, why it is a zebra, deck, slide, his
ZEBRAS = [
 ("Disulfiram-like reaction with alcohol", "metronidazole",
  "<b>His own example of a zebra.</b> Uncommon in practice &mdash; a patient taking it for an "
  "infection is often not drinking &mdash; but unique to this drug, and it costs nothing to "
  "warn them.", L1, 86, True),
 ("Red Man syndrome", "vancomycin",
  "<b>His own example.</b> An infusion-related reaction, not an allergy, which is why the answer "
  "is to <b>slow the infusion</b> rather than to stop the drug. He specified two hours.",
  L1, 51, True),
 ("Tooth discolouration and depression of skeletal growth", "tetracyclines",
  "<b>He pointed at the tetracyclines by name</b> as where a class breaks the common pattern. "
  "Doxycycline discolours more than the others; avoid under <b>8 years old</b> and in the "
  "<b>second and third trimesters</b>.", L1, 63, True),
 ("Chelation with calcium and iron", "tetracyclines; fluoroquinolones",
  "The interaction he illustrated with a patient on a <b>prenatal vitamin</b> whose calcium and "
  "iron bind up the doxycycline. Both classes complex with cations.", L1, 63, True),
 ("Achilles tendonitis and tendon rupture", "fluoroquinolones",
  "Unique to this class, and paired on the slide with a caution in the <b>under-18s</b> and with "
  "peripheral neuropathy.", L1, 79, False),
 ("Photosensitivity", "tetracyclines; fluoroquinolones; topical retinoids",
  "Not dangerous, but it is the one that actually changes what you tell the patient &mdash; "
  "sunscreen and covering up, because they will be outdoors regardless.", L1, 63, False),
 ("Teratogenicity", "azoles; isotretinoin; tetracyclines",
  "The azole slides carry it three times over. Isotretinoin is contraindicated in pregnancy and "
  "breastfeeding outright.", L1, 104, False),
 ("Bone marrow suppression", "flucytosine; ganciclovir",
  "Confined to these agents rather than shared across the antifungals or antivirals.",
  L1, 101, False),
 ("Raised serum lipids", "isotretinoin",
  "Sits alongside photophobia, arthralgia, headaches, alopecia and brittle nails on the same "
  "slide &mdash; the price of the most effective acne drug.", L2, 27, False),
]
