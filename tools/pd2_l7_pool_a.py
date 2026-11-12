# -*- coding: utf-8 -*-
# Physical Diagnosis 2, Lecture 7 -- The Advanced Hematological Physical Examination
# (Matthew Ward, DMSc, MBA, PA-C; title slide), delivered 2026-11-12 -- pool A.
#
# The causes of anemia and its thresholds, the whole history (slides 3-14), and the
# skin, nail, mucosal and lymph node examination (slides 15-35). Pool B carries the other
# organ systems: cardiovascular, clubbing, pulmonary, gastrointestinal, internal bleeding,
# the B12 neurologic examination, the emergency and the interpretation (slides 36-56).
#
# Written by tools/question_writing/WRITER.md (v1) with explanations to EXPLAIN_DEEP.md.
# Every fact is on a VISIBLE slide (text or picture); speaker notes are not used, and the
# lecturer said so himself: "on my tests [you] only get tested on things on the slide"
# (recording 4:16). Correct answer written first (c=0); the partition permutes positions.
# `mis` names the misconception each distractor stands for; it is stripped at render.
#
# SCOPE (the same-week overlap trap): CMS I Lecture 46 and Clinical Pathophysiology
# Lecture 10, both Ward, cover the same diseases. Nothing here is imported from them: no
# laboratory indices, no smear findings, no treatment. Only the history, the examination
# and the work-up this deck presents.
SRC = "Anemia-PDII-Ward-STUDENT-COPY-Updated.pptx"


def c(*n):
    return "%s, Slide%s %s" % (SRC, "s" if len(n) > 1 else "", ", ".join(str(x) for x in n))


IO_A = ("Define the elements of the medical history that aid in identifying disorders of the "
        "hematological system.")
IO_B = ("Define the elements and physical examination findings that aid in identifying disorders "
        "of the hematological system.")
IO_C = ("List presenting signs and symptoms from other organ systems associated with disorders of "
        "the hematological system.")
IO_D = ("Characterize the signs and symptoms of anemia with regard to severity of anemia and "
        "specificity.")

IMG = "pd2-exam-2-quiz-images/"
# picture -> the slide it was cut from (tools/extract_pd2_e2_l7_figures.py)
IMG_SLIDE = {
    "l7-fig-01.jpg": 24, "l7-fig-02.jpg": 32, "l7-fig-03.jpg": 34, "l7-fig-04.jpg": 35,
    "l7-fig-05.jpg": 48, "l7-fig-06.jpg": 49, "l7-fig-07.jpg": 19, "l7-fig-08.jpg": 30,
    "l7-fig-09.jpg": 27, "l7-fig-10.jpg": 53, "l7-fig-11.jpg": 17,
}


def Q(topic, io, slot, q, key, dists, cite, img=None, alt=None):
    assert len(dists) == 3, q
    opts = [[key[0], key[1]]] + [[t, e] for t, e, _m in dists]
    r = {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": cite,
         "mis": {t: m for t, _e, m in dists}}
    if img:
        n = IMG_SLIDE[img]
        r["img"] = IMG + img
        r["alt"] = alt
        r["slide"] = "Slide %d" % n
    return r


POOL_A = [

# ======================================================== causes and thresholds (slides 3-6)
Q("Causes of anemia", IO_A, "etiology",
  "Which three mechanisms account for anemia?",
  ("Blood loss, destruction and impaired production",
   "Correct. Anemia comes from red cells being lost (bleeding), destroyed (hemolysis) or not made "
   "(impaired production). Sorting a patient into one of these three is what the history and "
   "examination are for."),
  [("Blood loss, dilution and splenic sequestration",
    "Blood loss is one of the three, but dilution and sequestration are not the other two. The "
    "remaining mechanisms are destruction (hemolysis) and impaired red cell production.",
    "adjacent fact"),
   ("Destruction, iron overload and dehydration",
    "Destruction (hemolysis) is one mechanism, but iron overload and dehydration are not causes of "
    "anemia in this framework. The other two are blood loss and impaired production.",
    "confused mechanism or drug class"),
   ("Impaired production, fever and infection alone",
    "Impaired production is one mechanism; fever and infection are history clues, not mechanisms. "
    "The full set is blood loss, destruction and impaired production.",
    "adjacent fact")],
  c(3)),

Q("Causes of anemia", IO_A, "etiology",
  "Which three sources of blood loss are named as causes of anemia?",
  ("Trauma, menstrual and gastrointestinal",
   "Correct. Blood loss anemia is traced to trauma, menstrual loss or the gastrointestinal tract, "
   "which is why the bleeding and menstrual history and the stool questions matter."),
  [("Trauma, hemolysis and renal failure",
    "Trauma is a blood loss source, but hemolysis is destruction and renal failure is impaired "
    "production. The other two blood loss sources are menstrual and gastrointestinal.",
    "confused mechanism or drug class"),
   ("Menstrual, malaria and chronic disease",
    "Menstrual loss belongs here, but malaria causes hemolysis and chronic disease impairs production. "
    "Blood loss is trauma, menstrual or gastrointestinal.",
    "confused mechanism or drug class"),
   ("Gastrointestinal, lupus and transfusion",
    "Gastrointestinal loss belongs here, but lupus and transfusion reactions are extrinsic causes of "
    "hemolysis. The blood loss trio is trauma, menstrual and gastrointestinal.",
    "confused mechanism or drug class")],
  c(4)),

Q("Anemia thresholds", IO_D, "test finding",
  "Below which hemoglobin is a woman considered anemic?",
  ("11.9 g/dL",
   "Correct. In females anemia is a hemoglobin below 11.9 g/dL (119 g/L) or a hematocrit below 35 "
   "percent. The male cut-off is higher, 13.6 g/dL."),
  [("10.0 g/dL",
    "10.0 g/dL is well under the cut-off; a woman at 11 g/dL is already anemic. The female threshold "
    "is a hemoglobin below 11.9 g/dL or a hematocrit below 35 percent.",
    "reversed direction or value"),
   ("13.6 g/dL",
    "13.6 g/dL is the MALE threshold (hematocrit below 40 percent). For females the hemoglobin "
    "threshold is lower, below 11.9 g/dL.",
    "adjacent fact"),
   ("15.0 g/dL",
    "15.0 g/dL is above both thresholds and would be normal. Females are anemic below 11.9 g/dL, "
    "males below 13.6 g/dL.",
    "reversed direction or value")],
  c(4)),

Q("Anemia thresholds", IO_D, "test finding",
  "Below which hematocrit is a man considered anemic?",
  ("40 percent",
   "Correct. In males anemia is a hemoglobin below 13.6 g/dL (136 g/L) or a hematocrit below 40 "
   "percent. Females have the lower thresholds, 11.9 g/dL and 35 percent."),
  [("30 percent",
    "30 percent is below both sexes' thresholds; a man at 35 percent is already anemic. The male "
    "hematocrit threshold is 40 percent.",
    "reversed direction or value"),
   ("35 percent",
    "35 percent is the FEMALE hematocrit threshold. Men are held to a higher one: a hematocrit below "
    "40 percent (or hemoglobin below 13.6 g/dL).",
    "adjacent fact"),
   ("45 percent",
    "45 percent sits above the cut-off and would not define anemia. A man is anemic with a hematocrit "
    "below 40 percent.",
    "reversed direction or value")],
  c(4)),

Q("Causes of anemia", IO_A, "etiology",
  "Which is an example of an INTRINSIC (intracorpuscular) cause of hemolytic anemia?",
  ("Sickle cell disease",
   "Correct. Intrinsic, intracorpuscular causes lie in the red cell itself: sickle cell disease, the "
   "thalassemia syndromes, glucose-6-phosphate dehydrogenase deficiency and other hemoglobinopathies."),
  [("Transfusion reaction",
    "A transfusion reaction destroys red cells from outside them, an extrinsic (extracorpuscular) "
    "cause. Intrinsic examples are defects of the cell itself, such as sickle cell disease.",
    "reversed direction or value"),
   ("Malaria",
    "Malaria is an extrinsic cause of hemolysis, along with lupus and transfusion reactions. An "
    "intrinsic cause is a defect within the red cell, such as sickle cell disease.",
    "reversed direction or value"),
   ("Renal failure",
    "Renal failure causes anemia by impaired red cell production, not hemolysis. Intrinsic hemolytic "
    "causes include sickle cell disease and the thalassemias.",
    "confused mechanism or drug class")],
  c(5)),

Q("Causes of anemia", IO_A, "etiology",
  "Which is an example of a microangiopathic hemolytic anemia?",
  ("Thrombotic thrombocytopenic purpura",
   "Correct. Microangiopathic hemolytic anemia is extrinsic red cell destruction, and the examples "
   "given are disseminated intravascular coagulation and thrombotic thrombocytopenic purpura."),
  [("Glucose-6-phosphate dehydrogenase deficiency",
    "This enzyme deficiency is an intrinsic (intracorpuscular) cause of hemolysis, a defect of the red "
    "cell itself. Microangiopathic examples are disseminated intravascular coagulation and thrombotic "
    "thrombocytopenic purpura.",
    "reversed direction or value"),
   ("Thalassemia syndromes",
    "Thalassemias are intrinsic hemoglobin defects, not microangiopathic destruction. The "
    "microangiopathic examples are disseminated intravascular coagulation and thrombotic "
    "thrombocytopenic purpura.",
    "reversed direction or value"),
   ("Folic acid deficiency",
    "Folic acid deficiency impairs red cell production; it does not destroy red cells. Microangiopathic "
    "hemolysis is seen in thrombotic thrombocytopenic purpura and disseminated intravascular coagulation.",
    "confused mechanism or drug class")],
  c(5)),

Q("Causes of anemia", IO_A, "etiology",
  "Which cause of anemia works by IMPAIRED red cell production?",
  ("Renal failure",
   "Correct. Impaired production covers iron, B12 and folic acid deficiency, renal failure, chronic "
   "disease and hematologic neoplasm or metastatic disease."),
  [("Sickle cell disease",
    "Sickle cell disease causes anemia by destruction: it is an intrinsic hemolytic anemia. Impaired "
    "production includes renal failure, chronic disease and nutrient deficiency.",
    "confused mechanism or drug class"),
   ("Heavy menstrual bleeding",
    "Menstrual bleeding is a blood loss cause, alongside trauma and gastrointestinal loss. Impaired "
    "production includes renal failure, chronic disease and iron, B12 or folate deficiency.",
    "confused mechanism or drug class"),
   ("Transfusion reaction",
    "A transfusion reaction is extrinsic hemolysis, destruction of red cells. Impaired production "
    "instead includes renal failure, chronic disease and marrow neoplasm or metastasis.",
    "confused mechanism or drug class")],
  c(6)),

# ======================================================== the history: symptoms and severity (slide 8)
Q("Symptoms and severity", IO_D, "manifestation",
  "What is the most common symptom of anemia?",
  ("Fatigue",
   "Correct. Fatigue is the most common symptom of anemia; weakness and reduced exercise tolerance "
   "are listed beside it. Being common, it is also present with mild anemia and is nonspecific."),
  [("Syncope",
    "Syncope signals severity: symptoms at rest, chest pain and syncope point to "
    "severe anemia or another problem. Fatigue is the most common symptom.",
    "wrong stage or severity"),
   ("Chest pain",
    "Chest pain is a severity marker, grouped with syncope and symptoms at rest, not the usual "
    "complaint. The most common symptom is fatigue.",
    "wrong stage or severity"),
   ("Pica",
    "Pica is a clue to iron deficiency specifically, not the commonest symptom of anemia in general. "
    "That is fatigue.",
    "adjacent fact")],
  c(8)),

Q("Symptoms and severity", IO_D, "manifestation",
  "Which symptom in an anemic patient most strongly suggests SEVERE anemia?",
  ("Syncope",
   "Correct. Symptoms at rest, chest pain and syncope are the severity markers; patients with them "
   "need urgent assessment. Fatigue and weakness are common even in mild anemia."),
  [("Fatigue",
    "Fatigue is the most common symptom and appears even with mild anemia, so it does not mark "
    "severity. Syncope, chest pain and symptoms at rest do.",
    "wrong stage or severity"),
   ("Weakness",
    "Weakness and reduced exercise tolerance are common symptoms, listed with fatigue. The ones that mark severe "
    "anemia are syncope, chest pain and symptoms at rest.",
    "wrong stage or severity"),
   ("Hair shedding",
    "Hair shedding is a possible iron deficiency clue with many other causes; it says nothing about "
    "severity. Syncope, chest pain and rest symptoms do.",
    "adjacent fact")],
  c(8, 54)),

Q("Symptoms and severity", IO_D, "prognosis",
  "Which two factors shape how severe a patient's anemia symptoms are?",
  ("Rate of onset and cardiopulmonary disease",
   "Correct. Severity depends on how fast the anemia developed and on any cardiopulmonary disease. "
   "A rapid fall gives the body no time to adapt, and a weak heart or lungs tolerate anemia poorly."),
  [("Age at diagnosis and family history",
    "Family history helps find inherited hemoglobinopathies but does not set symptom severity. "
    "Severity tracks the rate of onset and cardiopulmonary disease.",
    "adjacent fact"),
   ("Diet and recent travel",
    "Diet and travel are clues to the CAUSE (deficiency, infection), not to how severe the symptoms "
    "are. Severity tracks the rate of onset and cardiopulmonary disease.",
    "adjacent fact"),
   ("Skin color and nail shape",
    "Pallor and nail changes are signs, and pallor is an unreliable estimate of hemoglobin. Symptom "
    "severity depends on the rate of onset and cardiopulmonary disease.",
    "confused mechanism or drug class")],
  c(8)),

Q("Symptoms and severity", IO_A, "manifestation",
  "Besides fatigue and weakness, which symptom belongs to the general symptoms of anemia?",
  ("Exertional dyspnea",
   "Correct. The general symptoms are fatigue, weakness, exertional dyspnea, palpitations and "
   "lightheadedness. They establish anemia's effect but do not point to its cause."),
  [("Melena",
    "Melena, black tarry stool, is part of the bleeding history: a clue to a gastrointestinal "
    "source, not a general symptom. Exertional dyspnea is a general symptom.",
    "adjacent fact"),
   ("Paresthesias",
    "Paresthesias are a clue to B12 deficiency, a specific cause. The general symptoms are fatigue, "
    "weakness, exertional dyspnea, palpitations and lightheadedness.",
    "adjacent fact"),
   ("Pica",
    "Pica, especially chewing ice, points to iron deficiency, a specific cause. The general symptoms "
    "include exertional dyspnea and palpitations.",
    "adjacent fact")],
  c(8, 55)),

Q("Symptoms and severity", IO_A, "manifestation",
  "When taking an anemia history, what should be compared with the patient's current symptoms?",
  ("Their baseline function",
   "Correct. The history covers onset, progression and change from baseline function: what the "
   "patient could do before and what they can no longer do as easily."),
  [("Their family's symptoms",
    "Family history is asked for hemoglobinopathy, bleeding and jaundice, but symptoms are measured "
    "against the patient's own baseline function.",
    "adjacent fact"),
   ("A standard hemoglobin chart",
    "Hemoglobin thresholds define anemia; the history compares symptoms with the patient's own "
    "baseline function, their onset and progression.",
    "confused mechanism or drug class"),
   ("Their oxygen saturation",
    "Oxygen saturation is not what the history compares with the symptoms; they are compared with "
    "the patient's own baseline function, onset and progression.",
    "confused mechanism or drug class")],
  c(8)),

# ======================================================== bleeding history (slide 9)
Q("Bleeding history", IO_A, "manifestation",
  "What is melena?",
  ("Black, tarry stool",
   "Correct. Melena is black, tarry stool. Hematochezia is red or maroon blood per rectum, and "
   "hematemesis is blood or coffee-ground emesis."),
  [("Red or maroon blood per rectum",
    "Red or maroon blood per rectum is hematochezia, not melena. Melena is black, tarry stool.",
    "adjacent fact"),
   ("Blood or coffee-ground emesis",
    "Vomiting blood or coffee-ground material is hematemesis. Melena refers to the stool: black and "
    "tarry.",
    "adjacent fact"),
   ("Blood in the urine",
    "Blood in the urine is hematuria, part of the same bleeding history. Melena is black, tarry "
    "stool.",
    "adjacent fact")],
  c(9)),

Q("Bleeding history", IO_A, "manifestation",
  "A patient reports red or maroon blood passed per rectum. What is this called?",
  ("Hematochezia",
   "Correct. Hematochezia is red or maroon blood per rectum. Black, tarry stool is melena, and blood "
   "or coffee-ground emesis is hematemesis."),
  [("Melena",
    "Melena is black, tarry stool, not red or maroon blood. Red or maroon blood per rectum is "
    "hematochezia.",
    "adjacent fact"),
   ("Hematemesis",
    "Hematemesis is blood or coffee-ground emesis, from the mouth. Blood per rectum that is red or "
    "maroon is hematochezia.",
    "adjacent fact"),
   ("Epistaxis",
    "Epistaxis is a nosebleed, part of the easy-bleeding questions. Red or maroon blood per rectum is "
    "hematochezia.",
    "adjacent fact")],
  c(9)),

Q("Bleeding history", IO_A, "manifestation",
  "A patient vomits material that looks like coffee grounds. What is this called?",
  ("Hematemesis",
   "Correct. Hematemesis is blood or coffee-ground emesis. It sits in the bleeding history with "
   "melena and hematochezia."),
  [("Hematochezia",
    "Hematochezia is red or maroon blood per rectum, not vomited. Coffee-ground emesis is hematemesis.",
    "adjacent fact"),
   ("Melena",
    "Melena is black, tarry STOOL. Blood or coffee-ground material that is vomited is hematemesis.",
    "adjacent fact"),
   ("Hematuria",
    "Hematuria is blood in the urine. Vomited blood or coffee-ground material is hematemesis.",
    "adjacent fact")],
  c(9)),

Q("Bleeding history", IO_A, "manifestation",
  "Which question about bleeding belongs in the history of an anemic patient?",
  ("Gum bleeding or nosebleeds",
   "Correct. The bleeding history asks about easy bruising, epistaxis, gum bleeding and prolonged "
   "procedural bleeding, then the gastrointestinal, urinary and uterine sources."),
  [("Whether the patient has ever donated blood",
    "Blood donation is not on the bleeding history. It asks about easy bruising, nosebleeds, gum "
    "bleeding and prolonged bleeding after procedures.",
    "adjacent fact"),
   ("The patient's blood type",
    "Blood type does not identify a bleeding source. The history asks about bruising, nosebleeds, gum "
    "bleeding and prolonged procedural bleeding.",
    "common lay belief"),
   ("Whether bleeding stops with ice",
    "No such question is part of the history. It covers bruising, nosebleeds, gum bleeding, prolonged "
    "procedural bleeding and each source's onset, frequency, amount and duration.",
    "common lay belief")],
  c(9)),

Q("Bleeding history", IO_A, "manifestation",
  "Once a patient reports bleeding, which four features of it should be defined?",
  ("Onset, frequency, amount and duration",
   "Correct. For any bleeding, define its onset, frequency, amount and duration; for menstrual "
   "bleeding also flooding, protection changes and daily impact."),
  [("Color, smell, temperature and texture",
    "Appearance helps name the bleeding (melena against hematochezia), but the history defines onset, "
    "frequency, amount and duration.",
    "common lay belief"),
   ("Location, radiation, timing and relief",
    "Those are pain descriptors. Bleeding is characterized by onset, frequency, amount and duration.",
    "confused mechanism or drug class"),
   ("Triggers, family pattern, cost and treatment",
    "Family patterns belong to the family history, not the description of one bleed. Define onset, "
    "frequency, amount and duration.",
    "adjacent fact")],
  c(9)),

# ======================================================== associated symptoms and risk factors (slide 10)
Q("Associated symptoms", IO_A, "risk factors",
  "Which group of clues points to IRON deficiency?",
  ("Pica, spoon-shaped nails and hair shedding",
   "Correct. Iron deficiency clues are pica, brittle or spoon-shaped nails and possible hair "
   "shedding."),
  [("Paresthesias, poor balance and lost vibration",
    "These are the B12 deficiency clues: paresthesias, impaired balance, reduced vibration or "
    "position sense. Iron deficiency gives pica, spoon nails and hair shedding.",
    "competing diagnosis"),
   ("Jaundice, dark urine and splenomegaly",
    "Jaundice and splenomegaly point toward hemolysis. Iron deficiency clues are pica, spoon-shaped "
    "nails and hair shedding.",
    "competing diagnosis"),
   ("Fever, night sweats and weight loss",
    "Those raise concern for infection or malignancy. Iron deficiency's clues are pica, brittle or "
    "spoon-shaped nails and hair shedding.",
    "competing diagnosis")],
  c(10)),

Q("Associated symptoms", IO_A, "risk factors",
  "Which group of clues points to B12 deficiency?",
  ("Paresthesias, poor balance, lost vibration",
   "Correct. The B12 clues are paresthesias, impaired balance and reduced vibration or position "
   "sense."),
  [("Pica, brittle nails and hair shedding",
    "Pica, brittle or spoon-shaped nails and hair shedding are the IRON deficiency clues. B12 "
    "deficiency is neurologic: paresthesias, balance, vibration and position sense.",
    "competing diagnosis"),
   ("Easy bruising, nosebleeds and gum bleeding",
    "These belong to the bleeding history. B12 deficiency shows instead as paresthesias, impaired "
    "balance and reduced vibration or position sense.",
    "adjacent fact"),
   ("Bloating, chronic diarrhea and weight loss",
    "These suggest possible malabsorption, a risk factor rather than the deficiency's own signs. B12 "
    "deficiency gives paresthesias, poor balance and lost vibration sense.",
    "adjacent fact")],
  c(10)),

Q("Associated symptoms", IO_A, "risk factors",
  "Which surgical history is a risk factor for iron or B12 deficiency?",
  ("Gastric bypass",
   "Correct. Gastric bypass, gastrectomy and intestinal resection are listed risks: they impair "
   "absorption, so a patient can be deficient despite a good diet."),
  [("Appendectomy",
    "An appendectomy does not appear among the risks. The surgeries that matter are gastric bypass, "
    "gastrectomy and intestinal resection, which impair absorption.",
    "adjacent fact"),
   ("Cholecystectomy",
    "Gallbladder removal is not among the listed risks. Gastric bypass, gastrectomy and intestinal "
    "resection are, because they impair absorption.",
    "adjacent fact"),
   ("Knee replacement",
    "Orthopedic surgery does not impair nutrient absorption. Gastric bypass, gastrectomy and "
    "intestinal resection do, and belong in the history.",
    "adjacent fact")],
  c(10)),

Q("Associated symptoms", IO_A, "risk factors",
  "Which symptoms raise the possibility of malabsorption as the cause of an anemia?",
  ("Chronic diarrhea, bloating and weight loss",
   "Correct. Chronic diarrhea, bloating and weight loss suggest possible malabsorption, and celiac "
   "disease, inflammatory bowel disease and gastrointestinal surgery are on the exposure history."),
  [("Fever, night sweats and travel",
    "Fever, night sweats and travel prompt questions about infection or malignancy. Malabsorption is "
    "suggested by chronic diarrhea, bloating and weight loss.",
    "competing diagnosis"),
   ("Flooding and intermenstrual bleeding",
    "Those are menstrual bleeding questions, a blood loss source. Malabsorption shows as chronic "
    "diarrhea, bloating and weight loss.",
    "adjacent fact"),
   ("Gum bleeding and easy bruising",
    "Those are bleeding-history questions. Malabsorption is suggested by chronic diarrhea, bloating "
    "and weight loss.",
    "adjacent fact")],
  c(10)),

# ======================================================== diet, travel, recent illness (slide 11)
Q("Diet and travel", IO_A, "risk factors",
  "Which diet puts a patient at risk of B12 deficiency?",
  ("Vegan, without supplements",
   "Correct. A vegan diet without B12 supplements or fortified foods is a B12 deficiency risk, "
   "since the diet history asks about animal products, fortified foods and supplements."),
  [("Vegetarian with daily fortified cereal",
    "Fortified foods are a B12 source, so this diet is covered. The risk is a vegan diet WITHOUT "
    "supplements or fortified foods.",
    "ruled out by a stated finding"),
   ("High-protein with daily red meat",
    "Animal products supply B12; this diet is not the listed risk. A vegan diet without supplements "
    "or fortified foods is.",
    "reversed direction or value"),
   ("Mediterranean with fish twice a week",
    "Fish is an animal product and supplies B12. The listed risk is a vegan diet without B12 "
    "supplements or fortified foods.",
    "reversed direction or value")],
  c(11)),

Q("Diet and travel", IO_A, "risk factors",
  "A patient admits to craving and chewing ice. Which deficiency does this suggest?",
  ("Iron deficiency",
   "Correct. Pica, particularly craving or chewing ice, is an iron deficiency clue, listed with "
   "brittle or spoon-shaped nails and hair shedding."),
  [("B12 deficiency",
    "B12 deficiency shows as paresthesias, impaired balance and reduced vibration or position sense, "
    "not pica. Ice chewing points to iron deficiency.",
    "competing diagnosis"),
   ("Folate deficiency",
    "Folate deficiency shares glossitis and angular cheilitis with iron and B12, but pica is the iron "
    "clue specifically.",
    "competing diagnosis"),
   ("Lead poisoning",
    "Lead exposure is asked about as an occupational or renovation history, not through ice cravings. "
    "Pica for ice points to iron deficiency.",
    "competing diagnosis")],
  c(10, 11)),

Q("Diet and travel", IO_A, "risk factors",
  "Which question about diet is part of the anemia history?",
  ("Iron-rich foods and supplements",
   "Correct. The diet history covers iron-containing foods, animal products, fortified foods, "
   "supplements and restrictive eating patterns."),
  [("Total daily calories",
    "Calorie count is not the point. The diet history asks about iron-containing foods, animal "
    "products, fortified foods, supplements and restrictive eating.",
    "common lay belief"),
   ("Caffeine intake after noon",
    "Caffeine timing is a sleep question. The diet history asks about iron-containing foods, animal "
    "products, fortified foods and supplements.",
    "adjacent fact"),
   ("Salt intake",
    "Salt intake belongs to a cardiovascular history. The anemia diet history asks about iron sources, "
    "animal products, fortified foods and supplements.",
    "adjacent fact")],
  c(11)),

Q("Diet and travel", IO_A, "risk factors",
  "In an anemic patient, which travel detail should be asked about?",
  ("Febrile illness or infections",
   "Correct. The travel history asks destination, timing, febrile illness and infectious exposures; "
   "malaria, for example, is an extrinsic cause of hemolysis."),
  [("Airline and seat class",
    "Travel logistics do not matter. The questions are destination, timing, febrile illness and "
    "infectious exposures.",
    "common lay belief"),
   ("Jet lag and sleep loss",
    "Fatigue from jet lag is not the concern. Ask about destination, timing, febrile illness and "
    "infectious exposures.",
    "common lay belief"),
   ("Altitude of the destination",
    "Altitude is not on the travel history. It asks destination, timing, febrile illness and "
    "infectious exposures.",
    "adjacent fact")],
  c(11)),

Q("Medication history", IO_A, "risk factors",
  "Which exposure is linked with possible B12 deficiency?",
  ("Nitrous oxide",
   "Correct. Nitrous oxide exposure is listed with possible B12 deficiency in the medication history, "
   "beside metformin and acid-suppressing medications."),
  [("Lead from pre-1978 buildings",
    "Lead exposure (occupational, renovation, pre-1978 buildings) is a separate exposure question. "
    "Nitrous oxide is the one tied to B12 deficiency.",
    "adjacent fact"),
   ("Benzene",
    "Benzene is a marrow-toxic chemical, asked about for marrow damage. Nitrous oxide is the exposure "
    "tied to B12 deficiency.",
    "adjacent fact"),
   ("Aspirin",
    "Aspirin is asked about in the medication history beside anti-inflammatories and anticoagulants, "
    "but nitrous oxide is the exposure listed with possible B12 deficiency.",
    "confused mechanism or drug class")],
  c(12)),

Q("Menstrual history", IO_A, "risk factors",
  "Which menstrual history detail helps judge how heavy a patient's bleeding is?",
  ("Flooding and protection changes",
   "Correct. The menstrual history asks duration, flooding, protection changes and daily impact, "
   "and any intermenstrual or postmenopausal bleeding."),
  [("Age at the first period",
    "Age at menarche does not measure loss. The menstrual history asks duration, flooding, protection "
    "changes and daily impact.",
    "adjacent fact"),
   ("The brand of protection used",
    "The brand does not matter; how often protection is changed does. Ask also about duration, "
    "flooding and daily impact.",
    "common lay belief"),
   ("Whether cramps are present",
    "Cramping is not on the list. Heaviness is judged by duration, flooding, protection changes and "
    "daily impact.",
    "common lay belief")],
  c(12)),

Q("Menstrual history", IO_A, "risk factors",
  "Which bleeding history in a 62-year-old woman must be asked about specifically?",
  ("Postmenopausal bleeding",
   "Correct. The menstrual history includes intermenstrual and postmenopausal bleeding; in an older "
   "woman, any postmenopausal bleeding is a blood loss source to identify."),
  [("Cycle length in her twenties",
    "Past cycle length does not identify a present source. Ask about postmenopausal and intermenstrual "
    "bleeding.",
    "adjacent fact"),
   ("Pregnancy and recent delivery",
    "Pregnancy and recent delivery are on the history, but are unlikely at 62. Postmenopausal bleeding "
    "is the question to ask.",
    "ruled out by a stated finding"),
   ("Age at her first period",
    "Age at menarche identifies no source of present blood loss. Postmenopausal bleeding does.",
    "adjacent fact")],
  c(12)),

# ======================================================== family and social history (slide 13)
Q("Family and social history", IO_A, "risk factors",
  "Which family history finding raises suspicion for an inherited hemolytic disorder?",
  ("Relatives who needed a splenectomy",
   "Correct. The family history asks about anemia, hemoglobinopathy, abnormal bleeding and "
   "unexplained jaundice, and relatives requiring transfusions or splenectomy."),
  [("Relatives with high blood pressure",
    "Hypertension is not a hemolysis clue. Relatives requiring transfusions or splenectomy, and "
    "unexplained jaundice, are.",
    "adjacent fact"),
   ("Relatives with seasonal allergies",
    "Allergies are not on the hematologic family history. Ask about transfusions, splenectomy, "
    "jaundice and hemoglobinopathy.",
    "adjacent fact"),
   ("Relatives with early cataracts",
    "Cataracts do not point to hemolysis. Relatives requiring splenectomy or transfusions, or with "
    "unexplained jaundice, do.",
    "adjacent fact")],
  c(13)),

Q("Family and social history", IO_A, "risk factors",
  "How should ancestry be used when taking a hemoglobinopathy history?",
  ("As risk information; hemoglobinopathies occur in any ancestry",
   "Correct. Ancestry is risk information only: hemoglobinopathies are possible in any ancestry, "
   "so a patient's background never rules one out."),
  [("To rule out hemoglobinopathy when ancestry is low risk",
    "Ancestry cannot exclude a hemoglobinopathy; they are possible in any ancestry. It is risk "
    "information, nothing more.",
    "reversed direction or value"),
   ("To replace previous genetic testing results",
    "Known diagnoses and previous genetic or hemoglobinopathy testing are asked for in their own "
    "right. Ancestry is only risk information.",
    "adjacent fact"),
   ("It is left out of the history",
    "Ancestry is asked, as risk information. It just never rules a hemoglobinopathy in or out, since "
    "they occur in any ancestry.",
    "reversed direction or value")],
  c(13)),

Q("Family and social history", IO_A, "risk factors",
  "Which social history item belongs in the hematologic history?",
  ("Alcohol intake",
   "Correct. The social history covers alcohol intake, nutritional adequacy and occupational "
   "exposures."),
  [("Number of siblings",
    "Siblings matter only through the family history of anemia or bleeding. The social history asks "
    "alcohol intake, nutrition and occupational exposures.",
    "adjacent fact"),
   ("Preferred exercise",
    "Exercise tolerance is a symptom question, compared with baseline. The social history asks about "
    "alcohol, nutrition and occupational exposures.",
    "adjacent fact"),
   ("Highest level of education",
    "Education is not on the list. Alcohol intake, nutritional adequacy and occupational exposures "
    "are.",
    "common lay belief")],
  c(13)),

Q("Family and social history", IO_A, "risk factors",
  "Besides known diagnoses, which family-history element should be asked about?",
  ("Previous hemoglobinopathy testing",
   "Correct. The family history covers anemia, hemoglobinopathy, abnormal bleeding, unexplained "
   "jaundice, relatives requiring transfusions or splenectomy, and known diagnoses with previous "
   "genetic or hemoglobinopathy testing."),
  [("Relatives' blood types",
    "Blood type is not on the family history. It asks about known diagnoses and previous genetic or "
    "hemoglobinopathy testing, with anemia, bleeding and jaundice in relatives.",
    "common lay belief"),
   ("Relatives' cholesterol levels",
    "Cholesterol is a cardiovascular question. The hematologic family history asks about previous "
    "genetic or hemoglobinopathy testing and relatives' transfusions or splenectomy.",
    "adjacent fact"),
   ("Relatives' eye color",
    "Eye color carries no hematologic information. Ask about previous genetic or hemoglobinopathy "
    "testing, anemia, bleeding and unexplained jaundice in relatives.",
    "common lay belief")],
  c(13)),

# ======================================================== medical and exposure history (slide 14)
Q("Exposure history", IO_A, "risk factors",
  "A painter who strips old paint in houses built before 1978 is anemic. Which exposure should be asked about?",
  ("Lead",
   "Correct. Lead exposure comes from occupational or renovation work and pre-1978 buildings, and "
   "belongs in the medical and exposure history."),
  [("Nitrous oxide",
    "Nitrous oxide is the exposure tied to B12 deficiency, not paint work. Renovation in pre-1978 "
    "buildings points to lead.",
    "adjacent fact"),
   ("Asbestos",
    "Asbestos is not on the hematologic exposure history. Lead (renovation, pre-1978 buildings) and "
    "benzene are.",
    "competing diagnosis"),
   ("Silica dust",
    "Silica is a lung exposure, not a hematologic one here. Old-paint renovation points to lead.",
    "competing diagnosis")],
  c(14)),

Q("Exposure history", IO_A, "risk factors",
  "Which chemical is asked about as a marrow-toxic exposure?",
  ("Benzene",
   "Correct. Benzene and other marrow-toxic chemicals are on the exposure history, beside lead from "
   "renovation work and pre-1978 buildings."),
  [("Lead",
    "Lead is asked about too, but as its own exposure (renovation, pre-1978 buildings). The listed "
    "marrow-toxic chemical is benzene.",
    "adjacent fact"),
   ("Nitrous oxide",
    "Nitrous oxide is linked to B12 deficiency, not named as marrow-toxic. Benzene is the marrow-toxic "
    "chemical.",
    "adjacent fact"),
   ("Chlorine",
    "Chlorine is not on the exposure history. Benzene and other marrow-toxic chemicals are.",
    "competing diagnosis")],
  c(14)),

Q("Exposure history", IO_A, "differential",
  "A patient with a diagnosis of irritable bowel syndrome is found to be anemic. What does this call for?",
  ("Evaluation for another explanation",
   "Correct. Anemia with irritable bowel syndrome calls for evaluation for another explanation, "
   "such as celiac disease, inflammatory bowel disease or a bleeding source."),
  [("Reassurance that the bowel disorder explains it",
    "That reverses the point: irritable bowel syndrome is not taken as the explanation. Anemia with it "
    "prompts a search for another cause.",
    "reversed direction or value"),
   ("Stopping the history at that diagnosis",
    "The rest of the history still matters: celiac disease, inflammatory bowel disease, chronic "
    "diarrhea and gastrointestinal surgery are asked about.",
    "common lay belief"),
   ("A diet higher in fiber",
    "Treating bowel symptoms is not the step here. Anemia with irritable bowel syndrome calls for "
    "evaluation for another explanation.",
    "wrong stage or severity")],
  c(14)),

Q("Exposure history", IO_A, "risk factors",
  "Which chronic condition belongs in the medical history of an anemic patient?",
  ("Chronic kidney disease",
   "Correct. The medical history covers chronic kidney disease, inflammatory disease, liver disease "
   "and malignancy; renal failure and chronic disease impair red cell production."),
  [("Migraine",
    "Migraine is not on the hematologic medical history. Chronic kidney, inflammatory and liver "
    "disease and malignancy are.",
    "adjacent fact"),
   ("Myopia",
    "Myopia has no bearing on red cell production. The list is chronic kidney disease, inflammatory "
    "disease, liver disease and malignancy.",
    "adjacent fact"),
   ("Seasonal allergies",
    "Allergies are not part of it. Ask about chronic kidney disease, inflammatory disease, liver "
    "disease and malignancy.",
    "adjacent fact")],
  c(14, 6)),

Q("Exposure history", IO_A, "risk factors",
  "Which gastrointestinal history is asked about because it can cause anemia through malabsorption?",
  ("Celiac disease",
   "Correct. Celiac disease, inflammatory bowel disease, chronic diarrhea and gastrointestinal "
   "surgery are on the history because they impair absorption of iron or B12."),
  [("Hemorrhoids treated years ago",
    "Old, treated hemorrhoids are not a malabsorption cause. Celiac disease and inflammatory bowel "
    "disease are.",
    "adjacent fact"),
   ("Lactose intolerance alone",
    "Lactose intolerance is not on the list. The malabsorption history names celiac disease, "
    "inflammatory bowel disease and gastrointestinal surgery.",
    "adjacent fact"),
   ("Childhood appendicitis",
    "A remote appendicitis does not cause malabsorption. Celiac disease, inflammatory bowel disease "
    "and intestinal resection can.",
    "adjacent fact")],
  c(14, 10)),

# ======================================================== focused exam, pallor, jaundice, hair (slides 15-20)
Q("Focused examination", IO_B, "manifestation",
  "Which belongs to the focused physical examination of an anemic patient?",
  ("Abdomen, liver and spleen",
   "Correct. The focused examination covers general appearance and vital signs, skin, conjunctivae, "
   "mouth and nails, lymph nodes, heart and lungs, the abdomen with liver and spleen, and a targeted "
   "neurologic examination."),
  [("Visual acuity and visual fields",
    "Eye charts are not part of it; the eye examination looks at the conjunctivae for pallor and the "
    "sclerae for icterus. The abdomen with liver and spleen is included.",
    "adjacent fact"),
   ("Otoscopy of both ears",
    "The ears are not on the focused list. It covers skin, conjunctivae, mouth, nails, nodes, heart, "
    "lungs, abdomen and a targeted neurologic examination.",
    "adjacent fact"),
   ("Range of motion of the joints",
    "A joint survey is not part of it. The abdomen, including liver and spleen, is.",
    "adjacent fact")],
  c(15)),

Q("Pallor", IO_B, "manifestation",
  "Where should pallor be looked for?",
  ("Conjunctivae, mouth, palms, nails",
   "Correct. Pallor is looked for in the conjunctivae, oral mucosa, palms and nail beds; the palpebral "
   "conjunctiva is checked by pulling down the lower lid."),
  [("Forehead, cheeks, ears and chin",
    "Facial skin is not where pallor is judged. Look at the conjunctivae, oral mucosa, palms and nail "
    "beds.",
    "common lay belief"),
   ("Sclerae, soles, scalp and tongue",
    "The sclerae are checked for icterus, not pallor. Pallor is sought in the conjunctivae, oral "
    "mucosa, palms and nail beds.",
    "adjacent fact"),
   ("Lips, eyelashes, knees and elbows",
    "These are not the listed sites. Pallor is looked for in the conjunctivae, oral mucosa, palms "
    "and nail beds.",
    "common lay belief")],
  c(16, 29)),

Q("Pallor", IO_D, "test finding",
  "How reliable is pallor as an estimate of a patient's hemoglobin?",
  ("Unreliable, though it suggests possible anemia",
   "Correct. Pallor suggests possible anemia but is an unreliable estimate of the hemoglobin, and a "
   "normal appearance does not exclude anemia."),
  [("Reliable enough to replace a blood count",
    "Pallor cannot stand in for a hemoglobin; it is an unreliable estimate. It only suggests possible "
    "anemia.",
    "reversed direction or value"),
   ("Reliable when the palms are pale",
    "No site makes pallor a reliable estimate. Conjunctivae, oral mucosa, palms and nail beds are all "
    "checked, and pallor stays unreliable.",
    "adjacent fact"),
   ("Its absence rules out anemia",
    "A normal appearance does not exclude anemia: anemia is still possible. Pallor is only a "
    "suggestion and an unreliable estimate.",
    "reversed direction or value")],
  c(16)),

Q("Pallor", IO_D, "test finding",
  "A patient's skin, conjunctivae and nail beds look entirely normal. What does this mean for anemia?",
  ("Anemia is still possible",
   "Correct. A normal appearance does not exclude anemia: anemia is still possible. Pallor itself is "
   "an unreliable estimate of the hemoglobin."),
  [("Anemia is excluded",
    "A normal look cannot exclude anemia. Pallor is unreliable both ways, so anemia is still possible.",
    "reversed direction or value"),
   ("Severe anemia is excluded",
    "Even severe anemia is not ruled out by appearance; severity is judged from symptoms and vital "
    "signs. Anemia is still possible.",
    "wrong stage or severity"),
   ("The anemia must be from hemolysis",
    "A normal appearance does not point to any one mechanism. It simply leaves anemia possible.",
    "confused mechanism or drug class")],
  c(16)),

Q("Pallor", IO_B, "manifestation",
  "What does this examination show?",
  ("Palmar pallor",
   "Correct. The left palm is distinctly pale beside the pink one on the right: palmar pallor. It "
   "suggests anemia but is an unreliable estimate of the hemoglobin."),
  [("Jaundice of the palms",
    "Jaundice turns the skin yellow, as on the forearm and face in jaundiced patients. This palm is "
    "pale, not yellow: pallor.",
    "competing diagnosis"),
   ("Palmar petechiae",
    "Petechiae are pinpoint, nonblanching red spots. The palm here is uniformly pale: pallor.",
    "competing diagnosis"),
   ("Digital clubbing",
    "Clubbing changes the fingertips and nail angle. The difference here is color: the left palm is "
    "pale.",
    "competing diagnosis")],
  c(17), img="l7-fig-11.jpg",
  alt="Two open palms side by side; the hand on the left is much paler than the pink hand on the right."),

Q("Jaundice", IO_B, "differential",
  "Jaundice and scleral icterus in an anemic patient point most toward which mechanism?",
  ("Hemolysis",
   "Correct. Jaundice and scleral icterus point to hemolytic anemia, including sickle cell disease. "
   "Disorders of bilirubin metabolism are another cause of jaundice."),
  [("Iron deficiency",
    "Iron deficiency's clues are pica, spoon-shaped nails and hair shedding, not jaundice. Icterus "
    "points to hemolysis.",
    "competing diagnosis"),
   ("Gastrointestinal blood loss",
    "Blood loss shows in the bleeding history and stool questions. Jaundice with anemia points to "
    "hemolysis.",
    "confused mechanism or drug class"),
   ("Renal failure",
    "Renal failure impairs red cell production; it is not the jaundice cause listed. Jaundice points "
    "to hemolysis, such as sickle cell disease.",
    "confused mechanism or drug class")],
  c(16)),

Q("Jaundice", IO_B, "differential",
  "Besides hemolytic anemia, what else causes jaundice?",
  ("Bilirubin disorders",
   "Correct. Jaundice and scleral icterus suggest hemolytic anemia, but other causes include "
   "disorders of bilirubin metabolism, so the sign is not specific for hemolysis."),
  [("Iron deficiency",
    "Iron deficiency is not a jaundice cause; its clues are pica and spoon nails. The other jaundice "
    "cause listed is disorders of bilirubin metabolism.",
    "competing diagnosis"),
   ("B12 deficiency",
    "B12 deficiency is known here for its neurologic findings, not jaundice. Disorders of bilirubin "
    "metabolism are the other cause.",
    "competing diagnosis"),
   ("Heavy menstrual bleeding",
    "Menstrual blood loss does not cause jaundice. Apart from hemolysis, jaundice comes from "
    "disorders of bilirubin metabolism.",
    "confused mechanism or drug class")],
  c(16)),

Q("Jaundice", IO_B, "manifestation",
  "In an anemic patient, which condition does the finding in this picture suggest?",
  ("Hemolytic anemia",
   "Correct. The sclerae are yellow: scleral icterus. With anemia it points to hemolytic anemia, "
   "including sickle cell disease (disorders of bilirubin metabolism are the other cause)."),
  [("Iron deficiency anemia",
    "Iron deficiency is linked to spoon nails and hair shedding, not yellow sclerae. Scleral icterus "
    "points to hemolysis.",
    "competing diagnosis"),
   ("Vitamin B12 deficiency anemia",
    "B12 deficiency is recognized by its neurologic findings. Yellow sclerae point to hemolysis.",
    "competing diagnosis"),
   ("Anemia of renal failure",
    "Renal failure impairs production and is not the cause of icterus listed. Yellow sclerae suggest "
    "hemolytic anemia.",
    "competing diagnosis")],
  c(19, 16), img="l7-fig-07.jpg",
  alt="Close view of a woman's eyes; the whites of the eyes are yellow."),

Q("Hair shedding", IO_D, "differential",
  "How specific is hair shedding as a sign of iron deficiency?",
  ("Nonspecific; it has multiple other causes",
   "Correct. Hair shedding is a possible sign of iron deficiency, but it has multiple other causes, "
   "so it supports rather than establishes the diagnosis."),
  [("Diagnostic of iron deficiency",
    "Hair shedding cannot establish iron deficiency; it has multiple other causes. It is a possible "
    "clue only.",
    "reversed direction or value"),
   ("Specific for B12 deficiency instead",
    "Hair shedding is listed with iron, not B12. B12 deficiency is recognized by paresthesias and lost "
    "vibration sense.",
    "competing diagnosis"),
   ("A sign of hemolysis",
    "Hemolysis is suggested by jaundice and icterus, not hair loss. Hair shedding is a nonspecific "
    "iron clue.",
    "competing diagnosis")],
  c(16, 20)),

# ======================================================== nails (slides 21-24)
Q("Nail changes", IO_B, "manifestation",
  "What is koilonychia?",
  ("Thin, concave, spoon-shaped nails",
   "Correct. Koilonychia is thin, concave, spoon-shaped nails, associated with iron deficiency. Like "
   "other nail findings it is a supporting clue only."),
  [("Bulbous fingertips with a lost nail angle",
    "That is digital clubbing, judged by Schamroth's window and the nail-fold angle, and atypical for "
    "uncomplicated anemia. Koilonychia is a spoon-shaped nail.",
    "competing diagnosis"),
   ("Fine lengthwise ridges in the nail",
    "Longitudinal ridging is a nonspecific nail change. Koilonychia is thin, concave and "
    "spoon-shaped.",
    "adjacent fact"),
   ("Pinpoint hemorrhages under the nail",
    "Pinpoint, nonblanching hemorrhages are petechiae, a skin finding. Koilonychia is the spoon-shaped "
    "nail.",
    "adjacent fact")],
  c(21)),

Q("Nail changes", IO_B, "manifestation",
  "Which deficiency is associated with the nail shown?",
  ("Iron deficiency",
   "Correct. This is koilonychia, the thin, concave, spoon-shaped nail, associated with iron "
   "deficiency. It supports, but cannot establish, the cause or severity."),
  [("Vitamin B12 deficiency",
    "B12 deficiency is recognized by paresthesias, balance problems and lost vibration sense, not "
    "spoon nails. Koilonychia points to iron.",
    "competing diagnosis"),
   ("Folate deficiency",
    "Folate shares glossitis and angular cheilitis with iron and B12, not koilonychia. The spoon nail "
    "is the iron clue.",
    "competing diagnosis"),
   ("Vitamin C deficiency",
    "Vitamin C is not discussed among the nail findings. Spoon-shaped nails are associated with iron "
    "deficiency.",
    "competing diagnosis")],
  c(24, 21), img="l7-fig-01.jpg",
  alt="A thumb seen from the side; the nail is thin and dished upward like a spoon."),

Q("Nail changes", IO_D, "differential",
  "How should brittle nails, flattening and longitudinal ridging be interpreted in an anemia work-up?",
  ("As nonspecific supporting clues",
   "Correct. Brittle nails, flattening and longitudinal ridging are nonspecific. Nail findings are "
   "supporting clues and cannot reliably tell the cause or severity."),
  [("As proof of iron deficiency",
    "Only koilonychia carries the iron association, and even it is a supporting clue. Brittleness, "
    "flattening and ridging are nonspecific.",
    "reversed direction or value"),
   ("As a measure of anemia severity",
    "Nail findings cannot assess severity. Severity comes from the symptoms, vital signs and "
    "cardiopulmonary reserve.",
    "wrong stage or severity"),
   ("As a sign of hemolysis",
    "Hemolysis shows as jaundice and icterus. Ridged, brittle or flattened nails are nonspecific.",
    "competing diagnosis")],
  c(21)),

Q("Nail changes", IO_D, "differential",
  "What can nail findings tell you in a patient with anemia?",
  ("Supporting clues, not cause or severity",
   "Correct. Nail findings are supporting clues; they are unreliable for assessing the cause or the "
   "severity of the anemia."),
  [("They establish the cause reliably",
    "Even koilonychia only supports iron deficiency. Nail findings cannot reliably establish the cause.",
    "reversed direction or value"),
   ("They grade how severe the anemia is",
    "Nails are unreliable for assessing severity as well as cause; they are supporting clues only, "
    "never a grade of the anemia.",
    "wrong stage or severity"),
   ("Little, so the nails are skipped",
    "The nails ARE examined, with the skin, conjunctivae and mouth. They give supporting clues.",
    "reversed direction or value")],
  c(21, 15)),

# ======================================================== petechiae, purpura, ecchymoses (slides 25-28)
Q("Petechiae and purpura", IO_B, "manifestation",
  "What are petechiae?",
  ("Pinpoint, nonblanching skin hemorrhages",
   "Correct. Petechiae are pinpoint, nonblanching skin hemorrhages. Purpura are larger nonblanching "
   "lesions, and ecchymoses are larger areas of bruising."),
  [("Larger nonblanching hemorrhagic lesions",
    "Larger nonblanching hemorrhagic lesions are purpura. Petechiae are the pinpoint ones.",
    "adjacent fact"),
   ("Larger areas of bruising",
    "Larger areas of bruising are ecchymoses. Petechiae are pinpoint, nonblanching hemorrhages.",
    "adjacent fact"),
   ("Small red spots that blanch with pressure",
    "Petechiae are NONblanching; that is what marks them as hemorrhage into the skin.",
    "reversed direction or value")],
  c(25)),

Q("Petechiae and purpura", IO_B, "manifestation",
  "Which term describes nonblanching hemorrhagic lesions LARGER than pinpoint spots but smaller than bruises?",
  ("Purpura",
   "Correct. Purpura are larger nonblanching hemorrhagic lesions, between pinpoint petechiae and "
   "ecchymoses, the larger areas of bruising."),
  [("Petechiae",
    "Petechiae are the PINPOINT nonblanching hemorrhages. The larger lesions are purpura.",
    "adjacent fact"),
   ("Ecchymoses",
    "Ecchymoses are the largest, areas of bruising. Purpura sit between them and petechiae.",
    "adjacent fact"),
   ("Telangiectasias",
    "Telangiectasias are not among the three bleeding lesions. The middle size is purpura.",
    "competing diagnosis")],
  c(25)),

Q("Petechiae and purpura", IO_B, "manifestation",
  "Which lesions cover the leg in this picture?",
  ("Petechiae",
   "Correct. The leg is scattered with small, pinpoint red spots: petechiae, nonblanching skin "
   "hemorrhages. Purpura would be larger lesions."),
  [("Ecchymoses",
    "Ecchymoses are larger areas of bruising. These spots are pinpoint: petechiae.",
    "adjacent fact"),
   ("Koilonychia",
    "Koilonychia is a spoon-shaped nail, not a skin lesion. These are pinpoint hemorrhages: petechiae.",
    "adjacent fact"),
   ("Cullen sign",
    "Cullen sign is periumbilical ecchymosis. These are pinpoint spots on a leg: petechiae.",
    "adjacent fact")],
  c(27, 25), img="l7-fig-09.jpg",
  alt="The side of a lower leg scattered with many small red pinpoint spots."),

Q("Petechiae and purpura", IO_B, "differential",
  "Which accompanying finding raises concern most in a patient with new petechiae?",
  ("Mucosal bleeding",
   "Correct. Concern increases with mucosal bleeding or systemic illness. Petechiae and purpura have "
   "possible causes in platelet or vascular disorders, medications and other conditions."),
  [("Lesions on the lower legs",
    "Distribution is recorded, but leg lesions alone are not the named concern. Mucosal bleeding or "
    "systemic illness is.",
    "adjacent fact"),
   ("A history of recent sun exposure",
    "Sun exposure is not on the list. Concern rises with mucosal bleeding or systemic illness.",
    "common lay belief"),
   ("Lesions that do not itch",
    "Itch is not a criterion. Mucosal bleeding or systemic illness raises the concern.",
    "common lay belief")],
  c(25)),

Q("Petechiae and purpura", IO_B, "manifestation",
  "Which features of petechiae or purpura should be described on examination?",
  ("Distribution, extent and palpability",
   "Correct. Record the distribution, extent and palpability of the lesions; possible causes include "
   "platelet or vascular disorders and medications."),
  [("Color, odor and temperature",
    "Odor and temperature are not features of these lesions. Describe distribution, extent and "
    "palpability.",
    "common lay belief"),
   ("Blanching, itch and pain",
    "They are nonblanching by definition. Describe distribution, extent and palpability.",
    "reversed direction or value"),
   ("Size of the nearby lymph nodes",
    "Nodes are examined separately. The lesions are described by distribution, extent and "
    "palpability.",
    "adjacent fact")],
  c(25)),

Q("Petechiae and purpura", IO_B, "etiology",
  "Which is a listed possible cause of petechiae and purpura?",
  ("A platelet disorder",
   "Correct. Possible causes are platelet or vascular disorders, medications and other conditions; "
   "mucosal bleeding or systemic illness raises concern."),
  [("Iron deficiency",
    "Iron deficiency's skin clues are pallor, hair shedding and spoon nails. Petechiae and purpura "
    "come from platelet or vascular disorders and medications.",
    "competing diagnosis"),
   ("Vitamin B12 deficiency",
    "B12 deficiency shows in the nervous system. Petechiae point to platelet or vascular disorders "
    "or medications.",
    "competing diagnosis"),
   ("Hair shedding",
    "Hair shedding is an unrelated iron clue. Platelet or vascular disorders cause petechiae and "
    "purpura.",
    "adjacent fact")],
  c(25)),

# ======================================================== HEENT and lymph nodes (slides 29-32)
Q("HEENT", IO_B, "manifestation",
  "Which part of the eye is inspected for the pallor of anemia?",
  ("The conjunctiva",
   "Correct. Pallor is looked for in the palpebral conjunctiva (pull the lower lid down), with the "
   "oral mucosa; the sclera is inspected separately for icterus."),
  [("The sclera",
    "The sclera is inspected for icterus (yellowing), not pallor. Pallor is judged on the palpebral "
    "conjunctiva.",
    "adjacent fact"),
   ("The iris",
    "Iris color says nothing about anemia. Pallor is sought in the palpebral conjunctiva.",
    "common lay belief"),
   ("The retina",
    "The retina is not where pallor is looked for. Pull the lower lid down and look at the palpebral "
    "conjunctiva.",
    "adjacent fact")],
  c(29, 30)),

Q("HEENT", IO_B, "manifestation",
  "What does the pulled-down lower eyelid in this picture show?",
  ("Conjunctival pallor",
   "Correct. The inner lining of the lower lid, the palpebral conjunctiva, is pale: "
   "conjunctival pallor, one of the sites where the pallor of anemia is looked for."),
  [("Scleral icterus",
    "Icterus is yellowing of the sclera, the white of the eye. Here the lid's lining is pale: pallor.",
    "competing diagnosis"),
   ("Palatal petechiae",
    "Palatal petechiae are red dots on the roof of the mouth. This is a pale eyelid lining.",
    "adjacent fact"),
   ("Normal conjunctiva",
    "This lining is not a normal finding here: it is pale, which is conjunctival pallor, one of the "
    "listed sites for the pallor of anemia.",
    "reversed direction or value")],
  c(30, 29), img="l7-fig-08.jpg",
  alt="A lower eyelid pulled down to show a pale, almost white inner lining."),

Q("HEENT", IO_B, "manifestation",
  "Which bleeding finding is looked for inside the mouth?",
  ("Palatal petechiae",
   "Correct. The oral examination looks for palatal petechiae and other mucosal bleeding, beside "
   "pallor of the oral mucosa."),
  [("Koilonychia",
    "Koilonychia is a nail finding. In the mouth, look for palatal petechiae and other mucosal "
    "bleeding.",
    "adjacent fact"),
   ("Scleral icterus",
    "Icterus is an eye finding. Inside the mouth the bleeding sign is palatal petechiae.",
    "adjacent fact"),
   ("Cullen sign",
    "Cullen sign is periumbilical ecchymosis on the abdomen. In the mouth, look for palatal petechiae.",
    "adjacent fact")],
  c(29)),

Q("HEENT", IO_B, "manifestation",
  "What does the roof of this patient's mouth show?",
  ("Palatal petechiae",
   "Correct. Clustered pinpoint red spots on the palate are palatal petechiae, a form of mucosal "
   "bleeding, which raises concern when seen with skin petechiae."),
  [("Glossitis",
    "Glossitis is a smooth, sore, beefy-red tongue. The finding here is pinpoint red dots on the "
    "palate.",
    "competing diagnosis"),
   ("Angular cheilitis",
    "Angular cheilitis is fissuring at the mouth corners. These are pinpoint red dots on the palate.",
    "competing diagnosis"),
   ("Oral mucosal pallor",
    "Pallor would make the mucosa pale. These are red pinpoint hemorrhages: palatal petechiae.",
    "reversed direction or value")],
  c(32, 29), img="l7-fig-02.jpg",
  alt="An open mouth showing the roof of the mouth, with a cluster of small red dots on the soft palate."),

Q("Lymph nodes", IO_B, "manifestation",
  "Which lymph node groups are examined routinely in the hematologic examination?",
  ("Cervical and supraclavicular",
   "Correct. The cervical and supraclavicular nodes are examined, and the axillary and inguinal "
   "regions when indicated."),
  [("Popliteal and epitrochlear",
    "These are not on the list. Cervical and supraclavicular nodes are examined, axillary and "
    "inguinal when indicated.",
    "adjacent fact"),
   ("Inguinal and femoral",
    "The inguinal region is examined when indicated, not routinely, and femoral nodes are not named. "
    "Cervical and supraclavicular are the routine groups.",
    "wrong stage or severity"),
   ("Mesenteric",
    "Mesenteric nodes cannot be examined at the bedside. Cervical and supraclavicular nodes are.",
    "common lay belief")],
  c(29)),

Q("Lymph nodes", IO_B, "manifestation",
  "Besides location and size, which features of an enlarged lymph node should be recorded?",
  ("Tenderness, consistency and mobility",
   "Correct. An enlarged node is described by location, size, tenderness, consistency and mobility, "
   "the five features to record for any enlarged node."),
  [("Color, temperature and odor",
    "These are not lymph node descriptors. After location and size, record tenderness, consistency "
    "and mobility.",
    "common lay belief"),
   ("Blanching, distribution and palpability",
    "Distribution and palpability describe petechiae and purpura, which are nonblanching. Nodes are "
    "described by tenderness, consistency and mobility.",
    "adjacent fact"),
   ("Pulsation, warmth and itch",
    "None of these is on the node checklist. After location and size come tenderness, consistency "
    "and mobility.",
    "common lay belief")],
  c(29)),

# ======================================================== glossitis and angular cheilitis (slides 33-35)
Q("Glossitis and cheilitis", IO_B, "manifestation",
  "What is glossitis?",
  ("A smooth, sore, beefy-red tongue",
   "Correct. Glossitis is inflammation of the tongue: smooth, sore and beefy red. It suggests "
   "possible iron, B12 or folate deficiency."),
  [("Fissures at the corners of the mouth",
    "Inflammation and fissures at the corners of the mouth are angular cheilitis. Glossitis is a "
    "smooth, sore, beefy-red tongue.",
    "adjacent fact"),
   ("Red pinpoint dots on the palate",
    "Those are palatal petechiae, mucosal bleeding. Glossitis is a smooth, sore, beefy-red tongue.",
    "adjacent fact"),
   ("A pale, dry oral mucosa",
    "A pale mucosa is pallor. Glossitis is a red, inflamed, smooth tongue.",
    "reversed direction or value")],
  c(33)),

Q("Glossitis and cheilitis", IO_D, "differential",
  "A patient has glossitis. Which deficiency does this identify?",
  ("None in particular",
   "Correct. Glossitis suggests possible iron, B12 or folate deficiency, and it is nonspecific for a "
   "particular deficiency; angular cheilitis is the same."),
  [("Iron deficiency specifically",
    "Iron is possible, but so are B12 and folate. Glossitis is nonspecific for a particular deficiency.",
    "competing diagnosis"),
   ("B12 deficiency specifically",
    "B12 is one of three possibilities. Glossitis does not point to one deficiency in particular.",
    "competing diagnosis"),
   ("Folate deficiency specifically",
    "Folate is one possibility, with iron and B12. Glossitis is nonspecific among them.",
    "competing diagnosis")],
  c(33, 10)),

Q("Glossitis and cheilitis", IO_B, "manifestation",
  "What does this tongue show?",
  ("Glossitis",
   "Correct. A smooth, glossy, beefy-red tongue is glossitis, inflammation of the tongue, which "
   "suggests possible iron, B12 or folate deficiency."),
  [("Palatal petechiae",
    "Palatal petechiae are pinpoint red dots on the roof of the mouth. This is a diffusely red, smooth "
    "tongue.",
    "competing diagnosis"),
   ("Oral mucosal pallor",
    "Pallor makes the mucosa pale. This tongue is beefy red: glossitis.",
    "reversed direction or value"),
   ("Angular cheilitis",
    "Angular cheilitis is at the mouth corners. The finding is the smooth, red tongue itself.",
    "competing diagnosis")],
  c(34, 33), img="l7-fig-03.jpg",
  alt="A protruded tongue that is smooth, glossy and beefy red."),

Q("Glossitis and cheilitis", IO_B, "manifestation",
  "What does this picture show at the corners of the mouth?",
  ("Angular cheilitis",
   "Correct. Inflammation and fissures at the corners of the mouth are angular cheilitis. Causes "
   "include nutritional deficiency, Candida, bacteria and local irritation."),
  [("Glossitis",
    "Glossitis is a smooth, sore, beefy-red tongue. The cracks here are at the mouth corners.",
    "competing diagnosis"),
   ("Oral mucosal pallor",
    "Pallor is a pale mucosa. This shows fissures at the corners of the mouth.",
    "competing diagnosis"),
   ("Palatal petechiae",
    "Palatal petechiae are on the roof of the mouth. The finding is at the corners: angular cheilitis.",
    "competing diagnosis")],
  c(35, 33), img="l7-fig-04.jpg",
  alt="Close view of a woman's closed lips with pale, cracked fissures at both corners of the mouth."),

Q("Glossitis and cheilitis", IO_D, "differential",
  "Besides nutritional deficiency, what else can cause angular cheilitis?",
  ("Candida infection",
   "Correct. Angular cheilitis can come from nutritional deficiency, Candida, bacteria or local "
   "irritation, which is why it is nonspecific."),
  [("Hemolysis",
    "Hemolysis gives jaundice and icterus. Angular cheilitis can come from Candida, bacteria or local "
    "irritation as well as deficiency.",
    "competing diagnosis"),
   ("Nitrous oxide exposure",
    "Nitrous oxide is not among the listed causes of angular cheilitis: nutritional deficiency, "
    "Candida, bacteria and local irritation.",
    "adjacent fact"),
   ("Lead exposure",
    "Lead is not among the listed causes of angular cheilitis. Those are nutritional deficiency, "
    "Candida, bacteria and local irritation.",
    "adjacent fact")],
  c(33)),
]

# blind_review.py reads `mis` from a pool module through QUESTIONS, so a held item carries its
# misconception notes on every page (a sets-only lookup made audits go stale on each repartition).
QUESTIONS = POOL_A
