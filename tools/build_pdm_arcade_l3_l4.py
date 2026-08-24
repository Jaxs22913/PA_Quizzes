#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PDM I Lecture 3 and Lecture 4 Arcade decks to arcade.js.

One deck per topic, joining the existing PDM Exam 1 group in syllabus order.

Cards are single atomic facts for Sprint's eight-second clock. matchCards are
recognition pairs with compressed identity tags.

NO CARD IS BUILT ON ONE OF LECTURE 4'S DISPUTED REFERENCE RANGES -- lymphocytes,
platelets and red cell distribution width each appear twice in that deck with
different numbers, so there is no single right answer to grade. Asserted below.

Arcade has no image support. Lecture 4 is the most image-dependent topic in the
course, so the recognition work -- what an acanthocyte actually looks like --
lives in the guide's 22 photographs. What is here is the verbal half: the name,
the discriminating feature, and the disease.
"""
import json, os, re, sys

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a microscope over a slide
ICON3 = ('<path d="M9 3h4v6H9z"/><path d="M11 9v5"/><circle cx="11" cy="16" r="3"/>'
         '<path d="M5 21h14"/><path d="M14 21a6 6 0 0 0-6-9"/>')
# a droplet with cells in it
ICON4 = ('<path d="M12 3s6 6.5 6 10a6 6 0 0 1-12 0c0-3.5 6-10 6-10z"/>'
         '<circle cx="10.5" cy="13" r="1.6"/><circle cx="14" cy="15.5" r="1.6"/>')

DECKS = [
 dict(id="pdm-derm-ent-ophtho", name="Derm, Ophtho &amp; ENT Testing", color="accent4",
      icon=ICON3, cards=[
  ["How is most skin disease diagnosed?", "By history and visual inspection, with office testing added only for uncertain diagnoses."],
  ["What should every diagnostic test you order do?", "Answer a specific clinical question."],
  ["Which four factors govern test selection?", "Cost, availability, invasiveness and diagnostic yield."],
  ["What is the closing rule of this lecture?", "Always choose the least invasive test that answers the clinical question."],
  ["Which test answers abscess versus cellulitis?", "Point-of-care ultrasound."],
  ["Which three tests does the deck group as bedside testing?", "Potassium hydroxide preparation, Tzanck smear and Gram stain."],
  ["What are the two limitations of bedside testing?", "Operator skill and sampling technique."],
  ["What does a potassium hydroxide preparation showing branching, septate hyphae indicate?", "A dermatophyte."],
  ["Which potassium hydroxide finding indicates Candida?", "Pseudohyphae together with budding yeast."],
  ["Which organism gives the spaghetti and meatballs appearance?", "Tinea versicolor."],
  ["What concentration of potassium hydroxide does the procedure use?", "Twenty per cent, one drop."],
  ["Which two objectives does the potassium hydroxide procedure use?", "Ten times to survey, then forty times for anything suspicious."],
  ["How are epithelial cells made visible on a potassium hydroxide slide?", "Reduce the illumination by lowering the condenser."],
  ["What does the sensitivity of a potassium hydroxide preparation depend on?", "Adequate scraping technique."],
  ["Which biopsy suits raised epidermal lesions and superficial rashes?", "The shave biopsy."],
  ["Which biopsy gives a full-thickness sample?", "The punch biopsy, used for inflammatory rashes and small lesions."],
  ["Which biopsy is preferred when melanoma is suspected?", "Excisional biopsy, removing the entire lesion."],
  ["What margin does the melanoma rule specify for the diagnostic biopsy?", "One to three millimetres, a narrow excisional biopsy."],
  ["To what depth must a melanoma biopsy go, and why?", "Below the lesion without transecting the base, so Breslow depth can be measured."],
  ["When is a partial shave acceptable for a pigmented lesion?", "Only when suspicion is low, and it may underestimate Breslow depth."],
  ["What does the T category measure in melanoma?", "How deeply the primary tumour has grown, in millimetres."],
  ["Which Breslow depth is T2?", "More than one millimetre and up to two millimetres."],
  ["What are the ultrasound findings of cellulitis?", "Dermal thickening, increased echogenicity and cobblestoning."],
  ["What are the ultrasound findings of an abscess?", "A hypoechoic collection with possible septations and posterior acoustic enhancement."],
  ["Why is cobblestoning non-specific?", "It is also seen in venous stasis."],
  ["Which triad must be screened for necrotizing infection?", "Hypotension, a white cell count of fifteen thousand or more, and violaceous skin."],
  ["Which study best defines the extent of tissue damage?", "Contrast magnetic resonance imaging."],
  ["What is the indication for a skin or wound culture?", "Purulent lesions, sampling pus from abscesses, carbuncles and furuncles."],
  ["Which lesion does the deck say not to culture?", "An inflamed epidermoid cyst."],
  ["With what is a wound cleaned before the Levine method?", "Sterile water or saline, never an antimicrobial solution."],
  ["How is the swab used in the Levine method?", "Rotated for five seconds over one to two centimetres of clean tissue, with enough pressure to express fluid."],
  ["Which material must a Levine specimen avoid?", "Exudate, eschar or necrotic material."],
  ["What gives higher yield in a diabetic foot ulcer than a swab?", "A deeper tissue biopsy or aspirate."],
  ["What does VVEEPP stand for?", "Visual acuity, visual fields, external exam, extraocular movements, pupils, pressure."],
  ["What is the indication for visual acuity testing?", "Every eye complaint."],
  ["Which chart is used for distance, and which for near?", "Snellen for distance, Rosenbaum for near."],
  ["How does a pinhole work?", "It blocks peripheral light and focuses central rays onto the retina."],
  ["Acuity corrects with a pinhole. What does that mean?", "The cause is a refractive error."],
  ["Acuity does not correct with a pinhole. What does that mean?", "Eye pathology is likely present."],
  ["Unilateral visual loss localises where?", "To the optic nerve or the eye itself."],
  ["Bilateral visual loss suggests what?", "A systemic or intracranial cause."],
  ["A central scotoma localises where?", "To the macula or the optic nerve."],
  ["Which field pattern goes with glaucoma?", "Peripheral loss."],
  ["Bitemporal hemianopia localises where?", "To the chiasm, classically a pituitary lesion."],
  ["Homonymous hemianopia localises where?", "Retrochiasmal, and the deck queries a stroke."],
  ["Under what light is fluorescein read, and after what?", "Cobalt-blue light, after a topical anesthetic."],
  ["Fluorescein shows linear staining. What is it?", "A corneal abrasion."],
  ["Fluorescein shows branching, dendritic staining. What is it?", "Herpetic keratitis."],
  ["Which fluorescein finding needs urgent referral?", "Fixed dense staining or an opacity, meaning an ulcer."],
  ["What is the normal intraocular pressure?", "Ten to twenty-one millimetres of mercury."],
  ["Why is intraocular pressure alone insufficient?", "Most open-angle glaucoma has normal pressure, and readings vary with corneal thickness."],
  ["Which glaucoma is an ophthalmologic emergency?", "Acute angle-closure glaucoma."],
  ["What is the normal cup-to-disc ratio, and the glaucomatous one?", "About zero point three normally, greater than zero point seven in glaucoma."],
  ["What distinguishes glaucomatous optic damage from other atrophies?", "It is excavated rather than merely pale."],
  ["What is the sensitivity of the rapid streptococcal antigen test?", "About seventy to ninety per cent, so false negatives occur."],
  ["A rapid strep test is negative in a child. What next?", "Confirm with a throat culture."],
  ["Is confirmatory culture routinely needed in adults?", "No, not routinely for adult patients."],
  ["Why is throat culture the gold standard?", "It has the highest sensitivity, though results take twenty-four to forty-eight hours."],
  ["Which test must not be used to diagnose acute pharyngitis?", "Antistreptococcal antibody titres."],
  ["What does audiometry distinguish?", "Conductive from sensorineural hearing loss."],
  ["What does an air-bone gap of ten decibels or more indicate?", "Middle-ear fluid."],
  ["What counts as a fail on primary-care audiometry?", "More than twenty decibels hearing level at one or more frequencies."],
  ["At what levels does screening audiometry present tones?", "Twenty-five to thirty decibels for adults, fifteen to twenty for children."],
  ["What does a threshold search find?", "The softest sound heard at each frequency half of the time."],
  ["How are right and left thresholds marked on an audiogram?", "Right is a red circle, left is a blue cross."],
  ["Which frequencies are lost first in presbycusis?", "The high frequencies."],
  ["What does tympanometry vary, and what does it measure?", "It varies air pressure in the external canal and measures reflected energy."],
  ["How does compliance relate to the reflected tone?", "The less compliant the system, the greater the intensity reflected back."],
  ["Where does a normal tympanogram peak?", "At fifty millimetres of water."],
  ["What does a type A tympanogram mean?", "Normal middle ear function."],
  ["What does a type B tympanogram mean?", "Restricted tympanic membrane mobility."],
  ["A flat tympanogram with high canal volume suggests what?", "Perforation or a patent tube."],
  ["A flat tympanogram with normal canal volume suggests what?", "Middle-ear effusion."],
  ["What does a type C tympanogram mean?", "Significant negative middle-ear pressure, from eustachian tube dysfunction."],
  ["Below what pressure is negative middle-ear pressure significant for treatment?", "More negative than minus two hundred millimetres of water."],
  ["What does a type AS tympanogram show?", "Normal pressure with reduced mobility, from ossicular fixation or tympanosclerosis."],
  ["What does a type AD tympanogram show?", "Normal pressure with hypermobility, a flaccid membrane from disarticulation."],
  ["Which modality is first-line for acute head and neck infection?", "Contrast-enhanced computed tomography."],
  ["What is the clinical pearl for computed tomography?", "Think computed tomography for bone, trauma and speed."],
  ["What is the clinical pearl for magnetic resonance?", "Think magnetic resonance for soft tissue, nerves, and tumour or intracranial extension."],
  ["Which three presentations need no imaging?", "Uncomplicated acute rhinosinusitis, otitis, and simple soft-tissue infections."],
  ["Which findings make orbital imaging an emergency?", "Facial swelling, proptosis, eye signs or neurologic signs."],
  ["What is first-line for a deep neck infection?", "Contrast computed tomography of the neck; ultrasound is not helpful."],
  ["What is first-line for a neck mass?", "Ultrasound, for cystic versus solid, size and vascularity."],
  ["Which study is used for suspected acoustic neuroma?", "Magnetic resonance imaging with contrast."],
  ["What does contrast computed tomography of the neck evaluate?", "A drainable abscess, airway compromise, and spread towards the mediastinum."],
  ["Which syndrome is the deck's example of vascular thrombosis in the neck?", "Lemierre syndrome."],
  ["Which findings describe a blow-out fracture?", "Orbital emphysema, an orbital floor fracture, and soft tissue in the top of the maxillary sinus."],
  ["Which suture separates in a tripod fracture?", "The frontozygomatic suture."],
 ],
      matchCards=[
  ["Branching, septate hyphae", "Dermatophyte"],
  ["Pseudohyphae with budding yeast", "Candida"],
  ["Spaghetti and meatballs", "Tinea versicolor"],
  ["Linear corneal staining", "Abrasion"],
  ["Branching dendritic staining", "Herpetic keratitis"],
  ["Bitemporal hemianopia", "Chiasmal or pituitary lesion"],
  ["Peripheral visual field loss", "Glaucoma"],
  ["Flat tympanogram, high canal volume", "Perforation or patent tube"],
  ["Flat tympanogram, normal volume", "Middle-ear effusion"],
  ["Negative middle-ear pressure", "Type C tympanogram"],
  ["Hypotension, high count, purple skin", "Necrotizing fasciitis screen"],
  ["Bone, trauma and speed", "Computed tomography"],
  ["Soft tissue, nerves and tumour", "Magnetic resonance imaging"],
  ["Frontozygomatic suture diastasis", "Tripod fracture"],
 ]),

 dict(id="pdm-cbc-hematology", name="Complete Blood Count &amp; Hematology", color="accent",
      icon=ICON4, cards=[
  ["What does a complete blood count report on?", "The hematologic system and other organ systems."],
  ["Which four red cell indices are reported?", "Mean corpuscular volume, mean corpuscular hemoglobin, its concentration, and red cell distribution width."],
  ["Which five lines make up the differential?", "Neutrophils, lymphocytes, monocytes, eosinophils and basophils."],
  ["What does a count WITHOUT differential add up to?", "Red cell count, red cell indices, a total white cell count, and platelets."],
  ["When do you order a count without differential?", "To screen or monitor for anemia, leukocytosis or leukopenia, or thrombocytopenia."],
  ["Which line do you check for bacterial infection?", "Neutrophils."],
  ["Which line do you check for viral infection?", "Lymphocytes."],
  ["Which line do you check for allergies and parasites?", "Eosinophils."],
  ["What is the normal white blood cell count?", "Four thousand five hundred to eleven thousand cells per microlitre."],
  ["What are the terms for a low and a high white cell count?", "Leukopenia below four thousand five hundred, leukocytosis above eleven thousand."],
  ["Which cells are granulocytes?", "Neutrophils, eosinophils and basophils, which have distinctive cytoplasmic granules."],
  ["Which cells are agranulocytes?", "Monocytes and lymphocytes, with no granules and a non-lobular nucleus."],
  ["What is the normal neutrophil percentage?", "Fifty-four to sixty-two per cent, the most abundant white cell."],
  ["How is the neutrophil nucleus described?", "Three to four lobes, with granular cytoplasm."],
  ["What are bands, and what is their normal proportion?", "Immature neutrophils, normally five per cent or less."],
  ["What does a band look like?", "One or two nuclear lobes separated by a thick chromatin band."],
  ["Which combination indicates bacterial infection?", "Neutrophils plus bands."],
  ["What is a left shift?", "An increase in immature cells, meaning bands."],
  ["Why does a left shift happen in bacterial infection?", "Neutrophils are consumed faster than the marrow can mature replacements."],
  ["By what mechanism do steroids raise the neutrophil count?", "Demargination, detaching neutrophils from the vessel wall into the bloodstream."],
  ["Why do folate and vitamin B12 deficiency lower neutrophils?", "Both are needed for the bone marrow to function."],
  ["Which toxic chemical does the deck name for neutropenia?", "Benzene."],
  ["Which three viruses suppress bone marrow function?", "Mononucleosis, human immunodeficiency virus and hepatitis."],
  ["What is the normal eosinophil percentage, and what do its granules hold?", "One to three per cent, with granules containing histamines."],
  ["What raises the eosinophil count?", "Parasitic infection, allergic reactions and cancer."],
  ["What do basophil granules contain?", "Heparin, histamine and other mediators of inflammation."],
  ["Why is a normal eosinophil or basophil range hard to define?", "Because a normal count can sometimes be zero."],
  ["What is the monocyte's rank and normal percentage?", "The largest white blood cell, three to seven per cent."],
  ["What do monocytes differentiate into?", "Macrophages or dendritic cells."],
  ["What do monocytes become in the liver, and in the skin?", "Kupffer cells in the liver, Langerhans cells in the skin."],
  ["What is the primary role of a dendritic cell?", "Antigen presentation, capturing antigens and presenting them to T cells."],
  ["What raises monocytes?", "Chronic inflammation, stress and viral infection."],
  ["Which three lymphocyte types exist?", "T cells, B cells and natural killer cells."],
  ["Does the complete blood count separate the lymphocyte types?", "No, it does not differentiate between them."],
  ["How long does a neutrophil survive in blood?", "Seven hours."],
  ["How long does an eosinophil survive in blood?", "Eight to twelve days."],
  ["How long does a monocyte survive in blood?", "Three days."],
  ["How long do lymphocyte memory cells live?", "They may live for years."],
  ["What is the absolute neutrophil count formula?", "White cell count multiplied by the percentage of neutrophils plus bands, divided by one hundred."],
  ["Which cells are counted with the neutrophils in the absolute count?", "Bands."],
  ["A count of six thousand with forty per cent neutrophils and five per cent bands gives what?", "Two thousand seven hundred per microlitre."],
  ["How is mild neutropenia defined?", "One thousand to under one thousand five hundred cells per microlitre."],
  ["How is moderate neutropenia defined?", "Five hundred to under one thousand cells per microlitre."],
  ["How is severe neutropenia defined?", "Under five hundred cells per microlitre."],
  ["Where do platelets come from?", "Megakaryocytes in the bone marrow, which break into fragments."],
  ["Why does the deck say platelets are not really cells?", "They are fragments of megakaryocytes rather than whole cells."],
  ["What is the platelet's primary role?", "Hemostasis, stopping the bleeding and repairing damaged vessels."],
  ["How long do platelets live?", "Seven to ten days."],
  ["Below what platelet count does hemorrhage risk increase?", "Twenty thousand."],
  ["What raises the platelet count?", "Trauma, acute hemorrhage, iron deficiency and polycythemia vera."],
  ["What lowers the platelet count?", "Marrow suppression from chemotherapy, alcohol, radiation, aplastic anemia or drugs."],
  ["What does mean platelet volume measure?", "The average size of platelets, as a marker of function and activation."],
  ["What does a raised mean platelet volume represent?", "An increase in immature platelets, as after recent blood loss."],
  ["What is the difference between hemoglobin and hematocrit?", "Hemoglobin is the amount per volume of blood; hematocrit is the percentage of blood that is red cells."],
  ["What is the rule of thumb relating them?", "Hemoglobin multiplied by three equals the hematocrit."],
  ["Which three causes raise red cell count, hemoglobin and hematocrit alike?", "Polycythemia vera, chronic hypoxia and dehydration."],
  ["Which three conditions are the deck's examples of chronic hypoxia?", "Chronic obstructive pulmonary disease, sleep apnea and high altitude."],
  ["Can the red cell count be used to diagnose anemia?", "Not directly, and it does not accurately measure oxygen carrying capacity."],
  ["What is the normal mean corpuscular volume?", "Eighty to one hundred femtolitres."],
  ["What is the formula for mean corpuscular volume?", "Hematocrit as a percentage times ten, divided by the red cell count in millions."],
  ["What does mean corpuscular hemoglobin measure?", "The average amount of hemoglobin in a single red cell, twenty-seven to thirty-three picograms."],
  ["What does mean corpuscular hemoglobin concentration measure?", "The average hemoglobin concentration in packed red cells, thirty-two to thirty-six grams per decilitre."],
  ["What separates the two mean corpuscular hemoglobin measures?", "The denominator: the red cell count for one, the hematocrit for the other."],
  ["Which condition does mean corpuscular hemoglobin concentration flag?", "Hereditary spherocytosis and other hyperchromic red cell states."],
  ["What does red cell distribution width indicate?", "The degree of anisocytosis, the variation in red cell size."],
  ["What defines a hypochromic cell?", "Central pallor greater than one third of the cell diameter."],
  ["How much of a normal red cell is central pallor?", "One third of the diameter."],
  ["What does poikilocytosis mean?", "Abnormally shaped red blood cells."],
  ["What does an acanthocyte look like, and what causes it?", "Irregular thorn-like spikes with no central pallor, in liver disease."],
  ["What does an echinocyte look like, and what causes it?", "Regularly spaced blunt projections with central pallor kept, in renal disease."],
  ["What separates an acanthocyte from an echinocyte?", "Spike regularity, and whether central pallor is preserved."],
  ["What is a schistocyte?", "A fragmented red cell, also called a helmet or horn cell."],
  ["Which four schistocyte types does the deck's figure name?", "Triangular cell, horn cell, helmet cell and microspherocyte."],
  ["What laboratory error do schistocytes cause?", "Automated counters may count them as platelets."],
  ["Under what condition do sickled cells form?", "Low oxygen tension, when sickle hemoglobin becomes long and rigid."],
  ["What is a spherocyte, and what causes it?", "A perfectly round cell with no central pallor, often small, in hereditary spherocytosis."],
  ["What is a target cell, and why does it form?", "A bullseye cell with a dark circle in the central pallor, from redundant membrane."],
  ["What is a target cell associated with?", "Post splenectomy and liver disease."],
  ["What is a teardrop cell associated with?", "Bone marrow disease, from marrow infiltrated by scar tissue or tumour."],
  ["What is basophilic stippling, and what causes it?", "Blue-black ribosomal RNA dots spread evenly through the cytoplasm, in lead poisoning."],
  ["What is a Howell-Jolly body?", "A single dark purple residual nuclear fragment, seen post splenectomy."],
  ["Why does a Howell-Jolly body appear in the blood?", "The spleen normally removes them, so their presence signals splenic dysfunction or asplenia."],
  ["What are Heinz bodies, and where do they sit?", "Denatured hemoglobin attached to the periphery of the red cell, in G6PD deficiency."],
  ["Which stain is needed to see Heinz bodies?", "A supravital stain such as new methylene blue."],
  ["Why will nobody report Heinz bodies unless asked?", "They are invisible on the routine Wright stain used for the differential."],
  ["What is rouleaux formation, and why does it happen?", "Red cells stacked like rows of coins, because raised serum proteins neutralise their negative charge."],
  ["What is rouleaux associated with?", "Multiple myeloma and liver disease."],
  ["What is agglutination, and what causes it?", "Disorderly clumping, because antibodies coat and bridge the cells."],
  ["What is agglutination associated with?", "Blood transfusion reactions."],
  ["Which value do you evaluate after finding a low hemoglobin?", "The mean corpuscular volume."],
  ["What are the three mean corpuscular volume bands?", "Microcytic under eighty, normocytic eighty to one hundred, macrocytic over one hundred femtolitres."],
  ["What does the reticulocyte count tell you?", "Whether the bone marrow is functioning appropriately."],
  ["What does a decreased reticulocyte count suggest?", "Underproduction of red cells."],
  ["What does an increased reticulocyte count suggest?", "Hemolysis or blood loss."],
  ["What is the most common cause of anemia?", "Iron deficiency anemia."],
  ["What must be evaluated for when iron deficiency is found?", "Occult blood loss, often the first sign of gastrointestinal bleeding."],
  ["Which iron studies indicate iron deficiency?", "Ferritin low, serum iron low, total iron binding capacity high."],
  ["Which iron studies indicate anemia of chronic disease?", "Ferritin high, serum iron low, total iron binding capacity low."],
  ["Why does ferritin rise in anemia of chronic disease?", "It is an acute phase reactant, so it rises even while the iron is unavailable."],
  ["Iron studies are all normal in a microcytic anemia. What next?", "Look for basophilic stippling; if present, obtain a serum lead level."],
  ["Iron studies are normal with no stippling. What is it?", "Thalassemia trait."],
  ["Which condition has a low cell size with all other iron studies normal?", "Thalassaemia minor."],
  ["What does the bus represent in the iron transport analogy?", "Transferrin, the binding protein that transports iron."],
  ["What does the bus stop represent?", "Ferritin, which stores iron and can be measured."],
  ["Which causes of macrocytic anemia are megaloblastic?", "Vitamin B12, folate and copper deficiency, and drugs impairing DNA synthesis."],
  ["Which three drugs impair DNA synthesis?", "Methotrexate, antiretrovirals and hydroxyurea."],
  ["Which smear findings mark a megaloblastic anemia?", "Macroovalocytes and hypersegmented neutrophils."],
  ["A macrocytic anemia with no megaloblastic changes suggests what?", "Chronic liver disease or acute hematologic malignancy."],
  ["How is normocytic anemia divided?", "Into hypo-proliferative causes, and hemolysis or hemorrhage."],
  ["How soon does hemoglobin fall after acute blood loss?", "Within two to three days."],
  ["What is intrinsic hemolytic anemia?", "A defect in the red cell causing premature splenic removal."],
  ["What is extrinsic hemolytic anemia?", "Mechanical stress, immunologic destruction or inflammatory injury from outside the cell."],
  ["A normocytic anemia with high reticulocytes suggests what?", "Hemolysis, sickle cell anemia or acute hemorrhage."],
  ["Low reticulocytes with low white cells or platelets suggests what?", "Leukemia, metastatic malignancy or aplastic anemia."],
  ["Low reticulocytes with normal white cells and platelets suggests what?", "Chronic infection or inflammation, malignancy, chronic renal disease or endocrine dysfunction."],
  ["Which cause appears in both the microcytic and normocytic branches?", "Iron deficiency."],
  ["Why obtain iron studies in everyone with a microcytic anemia?", "A concomitant iron deficiency can affect hemoglobin analysis and hide a thalassemia."],
  ["How is a complete blood count written as a fishbone?", "White cells left, hemoglobin above the line, hematocrit below it, platelets right."],
 ],
      matchCards=[
  ["Irregular spikes, no central pallor", "Acanthocyte, liver disease"],
  ["Regular blunt spikes, pallor kept", "Echinocyte, renal disease"],
  ["Fragments counted as platelets", "Schistocyte"],
  ["Round, pallor gone, often small", "Spherocyte"],
  ["Bullseye from redundant membrane", "Target cell"],
  ["Evenly spread blue-black dots", "Basophilic stippling, lead"],
  ["A single dark nuclear remnant", "Howell-Jolly body, asplenia"],
  ["Needs a supravital stain", "Heinz bodies, G6PD"],
  ["Stacked like rows of coins", "Rouleaux, myeloma"],
  ["Disorderly antibody clumping", "Agglutination, transfusion"],
  ["Low ferritin, high binding capacity", "Iron deficiency"],
  ["High ferritin, low binding capacity", "Anemia of chronic disease"],
  ["Absolute count under five hundred", "Severe neutropenia"],
  ["Immature neutrophils above five per cent", "Left shift"],
 ]),
]

# Lecture 4's three self-contradicting reference ranges. A card built on one of
# these has no single right answer, because the deck states it two ways.
DISPUTED = [
    ("lymphocyte percentage", r"twenty-four to forty-four per cent|twenty-five to thirty-three per cent|\b(?:24-44|25-33)\b"),
    ("platelet upper limit",  r"four hundred (?:and fifty )?thousand|\b4[05]0,000\b"),
    ("red cell distribution", r"(?:eleven|twelve) to fifteen per cent|\b1[12]-15\b"),
]


def js_deck(d):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False)) for a, b in rows)
    return ('  { id: %s, name: %s, color: %s,\n    icon: \'%s\',\n'
            '    cards: [\n%s\n    ],\n    matchCards: [\n%s\n    ] },\n') % (
        json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
        d["icon"], pairs(d["cards"]), pairs(d["matchCards"]))


s = open(ARCADE, encoding="utf-8").read()
if "pdm-derm-ent-ophtho" in s:
    sys.exit("decks already present -- nothing to do")

for d in DECKS:
    assert 8 <= len(d["cards"])
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "card back too long -> %s" % back
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "match definition too long -> %s" % definition
    for coll, i in (("cards", 0), ("cards", 1), ("matchCards", 0), ("matchCards", 1)):
        vals = [x[i] for x in d[coll]]
        assert len(vals) == len(set(vals)), "duplicate in %s[%d] of %s" % (coll, i, d["id"])
    backs = [b for _, b in d["matchCards"]]
    assert len(backs) == len(set(backs)), "two match prompts share an answer in %s" % d["id"]
    if d["id"] == "pdm-cbc-hematology":
        bad = [(lab, txt[:60]) for lab, rx in DISPUTED
               for txt in [c[0] + " " + c[1] for c in d["cards"]] if re.search(rx, txt, re.I)]
        assert not bad, ("a card is built on a reference range the deck states two "
                         "different ways: %r" % bad[:3])

m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

OLD = '"pdm-lab-diagnostics", "pdm-medical-imaging"'
NEW = '"pdm-lab-diagnostics", "pdm-medical-imaging", "pdm-derm-ent-ophtho", "pdm-cbc-hematology"'
assert s.count(OLD) == 1, "PDM exam group not found exactly once"
s = s.replace(OLD, NEW)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d deck(s): %d cards, %d match pairs"
      % (len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
