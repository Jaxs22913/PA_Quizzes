# -*- coding: utf-8 -*-
# PDM I Lecture 19 (Acid-Base Balance and Blood Gas Interpretation, Professor Finck) -- pool A.
# Objectives a (compare the laboratory studies: what the arterial blood gas order holds and what each
# value means: the carbon dioxide and oxygen pressures, pH, saturation, oxygen content, the
# dissociation curve, base excess, carboxyhemoglobin), b (arterial against venous: why arterial,
# the sample, its handling, the venous values) and c (indications for arterial blood gas testing).
# Pool B carries d (interpreting results), e (the four disorders' expected findings, potassium),
# f (calculating the anion gap) and g (an abnormal anion gap).
#
# LECTURER: Megan B. Finck, MMS, PA-C (title slide 1 and the 27 October recording, two segments,
# 90 minutes). The calendar and the syllabus both number it Lecture / Topic Outline 19. Exam 4's
# course director is Professor Reynolds; her rules hold.
#
# REYNOLDS' RULES, asserted in the partition: vignette and next-best-test style leaning to the tests;
# EVERY value in a stem carries its normal range "(normal ...)" (slide 54's table; venous values
# from slides 11, 14 and 18; the anion gap's 9 to 15 from slide 46; base excess plus or minus 2 from
# slide 41). Nothing calculated EXCEPT the anion gap: objective f is "Calculate the anion gap", and
# the lecturer said so aloud (1:18:52-1:19:23: "I do want you to memorize and understand this
# equation ... if I were to give you a list of lab values and ask you to calculate the anion gap");
# so an anion-gap item gives the sodium, chloride and bicarbonate with their ranges and asks for the
# gap (numeric options, ascending). The albumin correction is NOT calculated ("just know that it
# needs to be corrected if it's abnormal", 1:22:14). Winter's formula, the delta-delta and the
# osmolar gap are not in the deck and are never asked. Compensation is asked by DIRECTION only
# (slides 28, 50-53), never by an expected value.
#
# SLIDES ONLY. Every fact is on a visible slide (text or picture); speaker notes do not count (slide 9's
# asterisks are explained only in the notes, so "which electrolytes come from the metabolic panel" is
# not asked). The recording re-weights which items are selected and never adds a fact.
#
# NOT ASKED, by the lecturer's word or by the deck's own conflict:
#   - The saturation thresholds (slide 36: below 90% worrisome, below 75% critical): "I'm not going to
#     ask you ... my patient has an O2 saturation of 92%. Is this worrisome, or is this critical?"
#     (1:01:57-1:02:06).
#   - Memorized normal values: she named the first five rows of slide 54 to know by heart (1:28:28),
#     but "you're gonna have reference ranges when you're presented with clinical cases" and the course
#     rule supplies every range, so no item asks for a reference value.
#   - The arterial oxygen pressure's normal: slide 14 says greater than 88 mm Hg, slides 23 and 54 say
#     greater than 80 (both said aloud, 24:54 and 40:26). Stems give "(normal greater than 80 mm Hg)",
#     slide 54's table, and use values clear of 80 to 88.
#   - Anemia and polycythemia as causes of a low or high oxygen PRESSURE (slides 15 and 24): physiology
#     puts them on the oxygen CONTENT, so no item keys or refutes with them; the guide notes it.
#
# ABBREVIATIONS. None in options. In a stem or explanation an abbreviation appears only as
# ABBREV (full term), every time (the partition asserts it); values are written in words ("partial
# pressure of carbon dioxide"), never PaCO2.
#
# Correct answer is ALWAYS written first (c=0); the partition rotates (numeric option sets are sorted
# ascending instead and keep the key where its value falls).
SRC = "Acid Base Balance and Blood Gas Interpretation mbf2026sc.pptx"
IMG = "pdm-exam-4-quiz-images/"
def c(n): return f"{SRC}, Slide {n}" if isinstance(n, int) else f"{SRC}, {n}"   # "Slides 20 and 21": first = primary

IOA = "Compare and contrast laboratory studies used to diagnose acid-base disorders."
IOB = "Explain differences between arterial and venous blood gas measurements."
IOC = "Discuss indications for arterial blood gas testing."
IOD = "Interpret arterial blood gas results."
IOE = "Describe expected findings in: Metabolic acidosis, Metabolic alkalosis, Respiratory acidosis, Respiratory alkalosis."
IOF = "Calculate the anion gap."
IOG = "Discuss the clinical significance of an abnormal anion gap."

# The normal ranges every stem carries (slide 54 unless named).
PH = "(normal 7.35 to 7.45)"
PCO2 = "(normal 35 to 45 mm Hg)"
PO2 = "(normal greater than 80 mm Hg)"
HCO3 = "(normal 22 to 26 mEq/L)"
SAT = "(normal greater than 94%)"
NA = "(normal 135 to 148 mEq/L)"
CL = "(normal 98 to 106 mEq/L)"
K = "(normal 3.6 to 5.2 mEq/L)"
AG = "(normal 9 to 15)"                                   # slide 46
COHB = "(normal less than 2%)"
BE = "(normal plus or minus 2 mEq/L)"                     # slide 41


def Q(topic, io, slot, q, key, dists, cite, img=None, alt=None, slide=None, mis=None):
    """key/dists are (text, explanation)."""
    r = {"topic": topic, "io": io, "slot": slot, "q": q, "opts": [list(key)] + [list(d) for d in dists], "c": 0,
         "cite": c(cite)}
    if img:
        r["img"] = IMG + img
        r["alt"] = alt
        r["slide"] = "Slide %d" % (slide or cite)
    if mis:
        r["mis"] = mis
    return r


POOL_A = [

# =============================================================== objective a: what the order holds
Q("The blood gas order", IOA, "fact",
  "A 45-year-old firefighter is brought in after smoke inhalation. Which component of the arterial blood gas order indicates the amount of carbon monoxide poisoning?",
  ("Carboxyhemoglobin",
   "Correct. Carboxyhemoglobin forms when hemoglobin is exposed to carbon monoxide, and its result indicates the amount of carbon monoxide poisoning."),
  [("Base excess",
    "Base excess is the sum of the buffer anions in whole blood and separates respiratory from nonrespiratory change; carboxyhemoglobin measures carbon monoxide."),
   ("Partial pressure of oxygen",
    "The oxygen pressure measures oxygen dissolved in plasma and the lungs' ability to oxygenate; carboxyhemoglobin is what indicates carbon monoxide poisoning."),
   ("Bicarbonate",
    "Bicarbonate is the metabolic buffer, about half of the buffer anions in whole blood; the amount of carbon monoxide poisoning is read from carboxyhemoglobin.")],
  "Slides 42, 9 and 40", mis={"Base excess": "adjacent blood gas value", "Partial pressure of oxygen": "oxygen value, not carbon monoxide",
                              "Bicarbonate": "adjacent blood gas value"}),

Q("The blood gas order", IOA, "fact",
  "A 38-year-old is treated after a house fire and has a carboxyhemoglobin of 18% (normal less than 2%). Why does carbon monoxide take oxygen's place on hemoglobin?",
  ("Hemoglobin's affinity for it is 240 times that for oxygen",
   "Correct. Carboxyhemoglobin forms when hemoglobin is exposed to carbon monoxide, and hemoglobin's affinity for carbon monoxide is 240 times its affinity for oxygen."),
  [("It raises the fraction of inspired oxygen in the lungs",
    "The fraction of inspired oxygen is the oxygen in the air taken into the lungs; carbon monoxide wins because hemoglobin's affinity for it is 240 times oxygen's."),
   ("It shifts the dissociation curve to the right in acidosis",
    "A right shift comes with acidosis and makes hemoglobin release oxygen more easily; carbon monoxide displaces oxygen through a 240-fold affinity."),
   ("It dissolves in plasma, where 98% of the oxygen travels",
    "Only about 2% of oxygen is dissolved in plasma and 98% is bound to hemoglobin; carbon monoxide takes those binding sites with a 240-fold affinity.")],
  "Slides 42, 13 and 39", mis={"It raises the fraction of inspired oxygen in the lungs": "confused term (fraction of inspired oxygen)",
                               "It shifts the dissociation curve to the right in acidosis": "adjacent fact (curve shift)",
                               "It dissolves in plasma, where 98% of the oxygen travels": "reversed fact (98% is bound)"}),

Q("The blood gas order", IOA, "fact",
  "A 72-year-old woman in the intensive care unit has an arterial blood gas drawn. Which venous blood studies is it often used in combination with?",
  ("A blood count and a metabolic panel",
   "Correct. The blood gas is often used with other assessments: vital signs, the physical examination, venous blood analysis such as the complete blood count and comprehensive metabolic panel, fluid intake and urine output."),
  [("Blood cultures and a sputum culture",
    "Cultures are not among the assessments listed alongside the blood gas: vital signs, the examination, the complete blood count and metabolic panel, intake and urine output."),
   ("A lipid panel and cardiac troponin",
    "These are not among the studies listed with the blood gas; the venous analysis named alongside it is the complete blood count and comprehensive metabolic panel."),
   ("A coagulation panel and a D-dimer",
    "Clotting studies are not among the assessments listed with the blood gas; the venous blood analysis named is the complete blood count and comprehensive metabolic panel.")],
  4, mis={"Blood cultures and a sputum culture": "unrelated test pair", "A lipid panel and cardiac troponin": "unrelated test pair",
          "A coagulation panel and a D-dimer": "unrelated test pair"}),

# --------------------------------------------------------------- the carbon dioxide pressure
Q("Carbon dioxide pressure", IOA, "fact",
  "A 47-year-old is breathing slowly and shallowly after a sedative overdose, and an arterial blood gas is ordered to assess his ventilation. Which value answers that question?",
  ("Carbon dioxide pressure",
   "Correct. The blood gas assesses ventilation through the carbon dioxide: its partial pressure indicates the rate and depth of respirations and assesses alveolar ventilation."),
  [("Oxygen pressure",
    "The oxygen pressure assesses oxygenation (the ability to oxygenate) and is directly influenced by the fraction of inspired oxygen; ventilation is read from the carbon dioxide."),
   ("Oxygen saturation",
    "Saturation expresses the relationship between oxygen and hemoglobin; the rate and depth of breathing are reflected in the carbon dioxide pressure."),
   ("Carboxyhemoglobin",
    "Carboxyhemoglobin indicates the amount of carbon monoxide poisoning; ventilation is assessed through the partial pressure of carbon dioxide.")],
  "Slides 3, 21 and 23", mis={"Oxygen pressure": "oxygenation, not ventilation", "Oxygen saturation": "adjacent oxygen value",
                              "Carboxyhemoglobin": "adjacent blood gas value"}),

Q("Carbon dioxide pressure", IOA, "fact",
  "A 58-year-old man has a head injury. His carbon dioxide pressure rises from 46 to 58 mm Hg (normal 35 to 45 mm Hg), yet his breathing rate has not risen. Why is this a concern?",
  ("Rising carbon dioxide should drive ventilation up",
   "Correct. Carbon dioxide is the major chemical factor regulating ventilation: as it rises, ventilation increases. Head trauma impairs the respiratory center, so that response can fail."),
  [("Rising carbon dioxide should slow the breathing",
    "The direction is reversed: as carbon dioxide rises, ventilation increases. A rate that does not rise points to an impaired respiratory center, as after head trauma."),
   ("Only a falling oxygen pressure drives ventilation",
    "Carbon dioxide in the blood and cerebrospinal fluid is the major chemical factor regulating ventilation; its rise should have increased his breathing."),
   ("His kidneys should have corrected it in minutes",
    "Kidney compensation for a respiratory problem, by adjusting bicarbonate reabsorption, occurs over days; the expected fast response is increased ventilation.")],
  "Slides 10, 22 and 50", mis={"Rising carbon dioxide should slow the breathing": "reversed direction",
                               "Only a falling oxygen pressure drives ventilation": "confused regulator",
                               "His kidneys should have corrected it in minutes": "wrong system and timing"}),

# --------------------------------------------------------------- the oxygen pressure, saturation and content
Q("Oxygen pressure", IOA, "fact",
  "A 41-year-old's arterial blood gas reports a partial pressure of oxygen. What does this value measure?",
  ("Oxygen dissolved in the plasma",
   "Correct. The partial pressure of oxygen is the pressure exerted by oxygen dissolved in blood plasma (less than 2% of the oxygen carried); 98% is bound to hemoglobin."),
  [("Oxygen bound to hemoglobin",
    "Bound oxygen is the 98% carried on hemoglobin, described by the saturation; the partial pressure measures the dissolved oxygen in plasma."),
   ("All the oxygen in the blood",
    "The actual total amount of oxygen in the blood is the oxygen content; the partial pressure measures only the oxygen dissolved in plasma."),
   ("Hemoglobin's maximum oxygen load",
    "The maximum amount of oxygen that can combine with hemoglobin is the oxygen capacity; the partial pressure measures dissolved oxygen.")],
  "Slides 13, 35 and 37", mis={"Oxygen bound to hemoglobin": "adjacent value (saturation)", "All the oxygen in the blood": "adjacent value (oxygen content)",
                               "Hemoglobin's maximum oxygen load": "adjacent value (oxygen capacity)"}),

Q("Oxygen pressure", IOA, "fact",
  "A 55-year-old's clinician needs the actual amount of oxygen carried in his blood, bound and dissolved together. Which blood gas value reports it?",
  ("Oxygen content",
   "Correct. Oxygen content is the actual amount of oxygen in the blood: 98% transported with hemoglobin and the remainder dissolved."),
  [("Oxygen saturation",
    "Saturation is a ratio that indicates the relationship between oxygen and hemoglobin, not the oxygen content."),
   ("Partial pressure of oxygen",
    "The partial pressure reflects only the oxygen dissolved in plasma, less than 2% of the oxygen carried; the content is the actual total amount."),
   ("Oxygen capacity",
    "Oxygen capacity is the maximum amount of oxygen that can combine with hemoglobin, not the amount actually carried; that is the oxygen content.")],
  "Slides 37, 35 and 13", mis={"Oxygen saturation": "ratio, not content", "Partial pressure of oxygen": "dissolved fraction only",
                               "Oxygen capacity": "maximum, not actual"}),

Q("Oxygen pressure", IOA, "fact",
  "A 60-year-old's pulse oximeter reads 96% (normal greater than 94%). What does this saturation express?",
  ("Oxygen on hemoglobin as a share of its maximum",
   "Correct. Oxygen saturation is a ratio of the actual oxygen content of hemoglobin to hemoglobin's maximum oxygen-carrying capacity; it is also measured by pulse oximetry."),
  [("The total amount of oxygen in the blood",
    "Saturation indicates the relationship between oxygen and hemoglobin, not the oxygen content; the actual amount is the oxygen content."),
   ("The pressure of oxygen dissolved in plasma",
    "The pressure of dissolved oxygen is the partial pressure of oxygen on the blood gas; saturation is the hemoglobin ratio."),
   ("The share of oxygen in the air he breathes",
    "The oxygen in the air taken into the lungs is the fraction of inspired oxygen; saturation is a ratio on hemoglobin.")],
  "Slides 35, 13 and 37", mis={"The total amount of oxygen in the blood": "adjacent value (content)", "The pressure of oxygen dissolved in plasma": "adjacent value (partial pressure)",
                               "The share of oxygen in the air he breathes": "confused term (fraction of inspired oxygen)"}),

Q("Oxygen pressure", IOA, "fact",
  "A 49-year-old with asthma is seen in clinic, and the clinician wants only her oxygen saturation, not her pH or gas pressures. Besides the arterial blood gas, which test measures it?",
  ("Pulse oximetry",
   "Correct. Oxygen saturation, the ratio of hemoglobin's actual oxygen content to its maximum capacity, is also measured by pulse oximetry."),
  [("Carboxyhemoglobin level",
    "Carboxyhemoglobin indicates the amount of carbon monoxide poisoning; saturation is also measured by pulse oximetry."),
   ("Venous oxygen content",
    "Oxygen content is the actual amount of oxygen in the blood, not the saturation ratio; saturation is also measured by pulse oximetry."),
   ("Base excess",
    "Base excess is the sum of buffer anions in whole blood; it says nothing about saturation, which pulse oximetry also measures.")],
  "Slides 35, 37 and 42", mis={"Carboxyhemoglobin level": "adjacent blood gas value", "Venous oxygen content": "content, not saturation",
                               "Base excess": "adjacent blood gas value"}),

Q("Oxygen pressure", IOA, "fact",
  "A 70-year-old woman receiving supplemental oxygen has an arterial oxygen pressure of 145 mm Hg (normal greater than 80 mm Hg). Which factor most directly explains the high value?",
  ("An increased fraction of inspired oxygen",
   "Correct. The oxygen pressure is directly affected by the fraction of inspired oxygen, the amount of oxygen in the air taken into the lungs, and an increased fraction raises it."),
  [("Hypoventilation from neuromuscular disease",
    "Hypoventilation secondary to neuromuscular disease is a cause of a LOW oxygen pressure; her high value comes from the inspired oxygen."),
   ("An intracardiac shunt",
    "Intracardiac shunts lower the oxygen pressure; a high value on supplemental oxygen reflects the increased fraction of inspired oxygen."),
   ("Chronic obstructive pulmonary disease",
    "Chronic obstructive pulmonary disease lowers the oxygen pressure; supplemental oxygen raises it through the fraction of inspired oxygen.")],
  "Slides 13, 23 and 24", mis={"Hypoventilation from neuromuscular disease": "cause of the opposite change", "An intracardiac shunt": "cause of the opposite change",
                               "Chronic obstructive pulmonary disease": "cause of the opposite change"}),

# --------------------------------------------------------------- the oxygen-hemoglobin curve
Q("The dissociation curve", IOA, "fact",
  "A 52-year-old has an arterial pH of 7.22 (normal 7.35 to 7.45). How does this pH change the oxygen-hemoglobin dissociation curve?",
  ("Right shift: oxygen is released more easily",
   "Correct. A low pH (acidosis) shifts the curve to the right, and oxygen is released more easily from hemoglobin."),
  [("Left shift: oxygen is released more easily",
    "A left shift comes with a high pH (alkalosis) and makes oxygen bond more tightly; a low pH gives a right shift with easier release."),
   ("Right shift: oxygen bonds more tightly",
    "The right shift of acidosis loosens the hold: oxygen is released more easily; tighter bonding is the left shift of alkalosis."),
   ("Left shift: oxygen bonds more tightly",
    "This is the alkalosis pattern (high pH); a pH of 7.22 is an acidosis, which shifts the curve right and releases oxygen more easily.")],
  39, mis={"Left shift: oxygen is released more easily": "mixed-up pairing", "Right shift: oxygen bonds more tightly": "mixed-up pairing",
           "Left shift: oxygen bonds more tightly": "reversed (alkalosis)"}),

Q("The dissociation curve", IOA, "fact",
  "A 27-year-old has an arterial pH of 7.56 (normal 7.35 to 7.45) after a long bout of vomiting. How does this pH change hemoglobin's hold on oxygen?",
  ("Left shift: oxygen bonds more tightly",
   "Correct. A high pH (alkalosis) shifts the curve to the left, and oxygen bonds more tightly to hemoglobin."),
  [("Right shift: oxygen bonds more tightly",
    "The right shift belongs to a low pH and loosens the bond; alkalosis shifts the curve left, with tighter bonding."),
   ("Left shift: oxygen is released more easily",
    "A left shift means oxygen bonds more tightly, not that it is released more easily; easier release is the right shift of acidosis."),
   ("Right shift: oxygen is released more easily",
    "This is the acidosis pattern (low pH); a pH of 7.56 is an alkalosis, which shifts the curve left and holds oxygen more tightly.")],
  39, mis={"Right shift: oxygen bonds more tightly": "mixed-up pairing", "Left shift: oxygen is released more easily": "mixed-up pairing",
           "Right shift: oxygen is released more easily": "reversed (acidosis)"}),

Q("The dissociation curve", IOA, "image",
  "The curves shown are a 44-year-old's oxygen-hemoglobin dissociation curve at three pH values. Besides a fall in pH, which change shifts the curve to the right?",
  ("A rise in temperature",
   "Correct. The curve shifts to the right with increased hydrogen ions (a lower pH), increased carbon dioxide, increased temperature and increased BPG (2,3-bisphosphoglycerate)."),
  [("A fall in temperature",
    "It is INCREASED temperature that shifts the curve to the right, with increased hydrogen ions, carbon dioxide and BPG (2,3-bisphosphoglycerate)."),
   ("A fall in carbon dioxide",
    "Increased carbon dioxide is what shifts the curve right; a fall works the other way."),
   ("A rise in pH",
    "A high pH (alkalosis) shifts the curve to the LEFT, as the 7.6 curve lies; oxygen then bonds more tightly to hemoglobin.")],
  39, img="l19-fig-02.jpg", alt="Oxygen-hemoglobin dissociation curves labeled pH 7.6, 7.4 and 7.2", slide=39,
  mis={"A fall in temperature": "reversed direction", "A fall in carbon dioxide": "reversed direction", "A rise in pH": "reversed (left shift)"}),

Q("The dissociation curve", IOA, "image",
  "On a 36-year-old's oxygen-hemoglobin curve shown, two stretches are bracketed. Which description fits the blood in the lower, low-pressure bracket?",
  ("Tissue capillaries, where oxygen is released",
   "Correct. Where the oxygen pressure is low, in the tissue capillaries, oxygen is released from hemoglobin; where it is high, in the pulmonary capillaries, oxygen binds."),
  [("Pulmonary capillaries, where oxygen binds",
    "The pulmonary capillaries sit on the high-pressure, flat upper part of the curve (the upper bracket); the low-pressure stretch is the tissue capillaries, releasing oxygen."),
   ("Tissue capillaries, where oxygen binds",
    "The place is right but the action is reversed: in the tissue capillaries, at low oxygen pressure, oxygen is released from hemoglobin."),
   ("Pulmonary capillaries, where oxygen is released",
    "In the pulmonary capillaries the oxygen pressure is high and oxygen binds with hemoglobin; release happens at low pressure in the tissues.")],
  38, img="l19-fig-03.jpg", alt="Oxygen-hemoglobin dissociation curve with two unlabeled brackets, one high and one low on the curve", slide=38,
  mis={"Pulmonary capillaries, where oxygen binds": "wrong place", "Tissue capillaries, where oxygen binds": "reversed action",
       "Pulmonary capillaries, where oxygen is released": "wrong place and action"}),

# --------------------------------------------------------------- base excess
Q("Base excess", IOA, "fact",
  "A 64-year-old's blood gas reports a base deficit. Bicarbonate is half of his whole blood buffer base. Which anions make up the other half?",
  ("Proteins and phosphates",
   "Correct. Base excess (whole blood buffer base) is the sum of the buffer anions in whole blood: bicarbonate is half, and other anions such as plasma proteins and phosphates are the other half."),
  [("Lactate and ketoacids",
    "Lactate and ketoacids are acids whose excess produces a base deficit (and raise the anion gap); the other half of the buffer base is plasma proteins and phosphates."),
   ("Chloride and sulfate",
    "Chloride is the measured anion of the anion gap and sulfate an unmeasured one; the other half of the buffer base is plasma proteins and phosphates."),
   ("Sodium and potassium",
    "Sodium and potassium are cations, not anions; the buffer base is anions: bicarbonate plus plasma proteins and phosphates.")],
  "Slides 40, 41 and 45", mis={"Lactate and ketoacids": "adjacent fact (acids, anion gap)", "Chloride and sulfate": "adjacent fact (anion gap)",
                               "Sodium and potassium": "wrong charge"}),

Q("Base excess", IOA, "fact",
  "A 58-year-old's arterial blood gas includes the base excess or deficit. Why is that value reported?",
  ("To tell respiratory from nonrespiratory change",
   "Correct. Base excess or deficit, the sum of the buffer anions in whole blood, is critically important in determining respiratory against nonrespiratory changes in acid-base balance."),
  [("To measure the dissolved carbon dioxide",
    "Dissolved carbon dioxide is the partial pressure of carbon dioxide; base excess sums the buffer anions to separate respiratory from nonrespiratory change."),
   ("To measure the carbon monoxide exposure",
    "Carbon monoxide poisoning is indicated by carboxyhemoglobin; base excess separates respiratory from nonrespiratory change."),
   ("To measure the oxygen bound to hemoglobin",
    "Oxygen on hemoglobin is described by the saturation; base excess is the buffer-anion sum that separates respiratory from nonrespiratory change.")],
  "Slides 40, 10 and 42", mis={"To measure the dissolved carbon dioxide": "adjacent value", "To measure the carbon monoxide exposure": "adjacent value",
                               "To measure the oxygen bound to hemoglobin": "adjacent value"}),

# --------------------------------------------------------------- pH: where the acid comes from
Q("Blood pH", IOA, "fact",
  "A 33-year-old's blood pH reflects the hydrogen ions from both volatile and nonvolatile acids. Which acid is the volatile one?",
  ("Carbonic acid",
   "Correct. The sources of hydrogen ions are volatile acids, such as carbonic acid, and nonvolatile acids, such as dietary acids, lactic acids and ketoacids."),
  [("Lactic acid",
    "Lactic acid is a nonvolatile acid, like dietary acids and ketoacids; the volatile acid is carbonic acid."),
   ("Ketoacids",
    "Ketoacids, as in diabetic ketoacidosis, are nonvolatile acids; carbonic acid is the volatile acid."),
   ("Dietary acids",
    "Dietary acids are nonvolatile acids, with lactic acids and ketoacids; the volatile example is carbonic acid.")],
  16, mis={"Lactic acid": "adjacent fact (nonvolatile)", "Ketoacids": "adjacent fact (nonvolatile)", "Dietary acids": "adjacent fact (nonvolatile)"}),

# =============================================================== objective b: arterial against venous
Q("Why arterial blood", IOB, "fact",
  "A 57-year-old with acute dyspnea needs to know how well his lungs are oxygenating his blood. Why is the sample taken from an artery rather than a vein?",
  ("Arterial blood is a better mixture of blood",
   "Correct. Arterial blood provides a better mixture of blood and indicates how well the lungs oxygenate it; venous blood is more localized to the phlebotomy site."),
  [("Arterial blood shows how severe the illness is",
    "The blood gas does NOT indicate the degree of any abnormality; that needs a physical assessment of the patient. Arterial blood is chosen as the better mixture."),
   ("Venous blood has no measurable gas pressures",
    "Venous gases are measured and have their own normal values (carbon dioxide 41 to 57 mm Hg, oxygen 30 to 40); arterial blood is the better mixture."),
   ("Venous blood is free of local effects",
    "The reverse: venous blood is localized to the phlebotomy site and can be affected by temperature, perfusion, movement and local infection.")],
  "Slides 5, 11 and 14", mis={"Arterial blood shows how severe the illness is": "common belief (degree)", "Venous blood has no measurable gas pressures": "false premise",
                              "Venous blood is free of local effects": "reversed fact"}),

Q("Why arterial blood", IOB, "fact",
  "A 62-year-old's venous sample was drawn from an arm with an infection at the puncture site. Why might it mislead about her overall gases?",
  ("Venous blood reflects local conditions at its site",
   "Correct. Venous blood gives information localized to the phlebotomy site and can be affected by temperature, perfusion, movement and local infection; arterial blood is a better mixture."),
  [("Local infection affects only arterial samples",
    "It is venous blood that can be affected by local infection, temperature, perfusion and movement; arterial blood is the better mixture."),
   ("Venous blood is a better mixture than arterial",
    "The reverse: arterial blood provides the better mixture, while venous blood is localized to the phlebotomy site."),
   ("Venous carbon dioxide is lower than arterial",
    "Venous carbon dioxide pressure runs higher (41 to 57 mm Hg against 35 to 45); the concern here is local effects on the venous sample.")],
  "Slides 5 and 11", mis={"Local infection affects only arterial samples": "reversed fact", "Venous blood is a better mixture than arterial": "reversed fact",
                          "Venous carbon dioxide is lower than arterial": "reversed value"}),

Q("Venous against arterial values", IOB, "fact",
  "In a healthy 40-year-old, an arterial and a venous sample are drawn at the same moment. How does the venous sample compare?",
  ("Higher carbon dioxide pressure, lower pH",
   "Correct. Venous carbon dioxide pressure is 41 to 57 mm Hg against arterial 35 to 45, and venous pH is 7.31 to 7.41 against arterial 7.35 to 7.45."),
  [("Lower carbon dioxide pressure, higher pH",
    "Both are reversed: venous carbon dioxide pressure is higher (41 to 57 mm Hg) and venous pH lower (7.31 to 7.41) than arterial."),
   ("Higher carbon dioxide pressure, higher pH",
    "The carbon dioxide is right, but venous pH is LOWER than arterial: 7.31 to 7.41 against 7.35 to 7.45."),
   ("Lower carbon dioxide pressure, lower pH",
    "The pH is right, but venous carbon dioxide pressure is HIGHER than arterial: 41 to 57 mm Hg against 35 to 45.")],
  "Slides 11 and 18", mis={"Lower carbon dioxide pressure, higher pH": "reversed values", "Higher carbon dioxide pressure, higher pH": "half reversed",
                           "Lower carbon dioxide pressure, lower pH": "half reversed"}),

Q("Venous against arterial values", IOB, "fact",
  "A 50-year-old's venous blood gas shows a carbon dioxide pressure of 50 mm Hg (venous normal 41 to 57 mm Hg; arterial normal 35 to 45 mm Hg). How should the value be read?",
  ("Normal for a venous sample",
   "Correct. Venous carbon dioxide pressure normally runs higher than arterial, 41 to 57 mm Hg, so 50 is normal for this venous sample."),
  [("High, from carbon dioxide retention",
    "Fifty would be high for an ARTERIAL sample (35 to 45), but this is venous blood, whose normal is 41 to 57 mm Hg."),
   ("Low, from hyperventilation",
    "Fifty is not low for either sample; for venous blood it sits inside the normal 41 to 57 mm Hg."),
   ("Unreadable, as venous gases have no normal",
    "Venous gases have their own normal values: carbon dioxide 41 to 57 mm Hg, so 50 is normal for venous blood.")],
  11, mis={"High, from carbon dioxide retention": "used the arterial range", "Low, from hyperventilation": "misread value",
           "Unreadable, as venous gases have no normal": "false premise"}),

# --------------------------------------------------------------- the arterial sample
Q("The arterial sample", IOB, "image",
  "Before an arterial puncture at the wrist, a 59-year-old's clinician performs the maneuver shown. What does it check?",
  ("Collateral supply through the ulnar and radial arteries",
   "Correct. This is the Allen test: before a radial puncture, collateral blood supply via the ulnar and radial arteries must be checked."),
  [("The depth of the radial artery under the skin",
    "The maneuver tests collateral circulation (the Allen test); the site is then palpated to make sure the artery has been correctly identified."),
   ("Whether the venous return from the hand is normal",
    "The Allen test checks the ARTERIAL collateral supply through the ulnar and radial arteries, not venous return."),
   ("Whether the site shows signs of local infection",
    "The site is cleaned and checked for local infection as a separate step; this maneuver checks collateral circulation.")],
  6, img="l19-fig-01.jpg", alt="Three photographs of a clinician's hands pressing on a patient's wrist while the patient's hand closes and opens", slide=6,
  mis={"The depth of the radial artery under the skin": "adjacent procedure step", "Whether the venous return from the hand is normal": "arterial vs venous confusion",
       "Whether the site shows signs of local infection": "adjacent procedure step"}),

Q("The arterial sample", IOB, "next-test",
  "Before a radial arterial stick in a 61-year-old, the Allen test shows no collateral circulation to the hand. What is the next step?",
  ("Choose another site for the sample",
   "Correct. Collateral circulation must be present; if it is not, another location must be chosen, such as the femoral or brachial artery."),
  [("Proceed and hold pressure for longer",
    "Holding pressure follows any arterial stick; without collateral circulation the radial site must not be used and another location is chosen."),
   ("Draw from the same artery through a line",
    "An arterial line still needs collateral blood flow; when it is absent at that site, another location must be chosen."),
   ("Repeat the stick after warming the hand",
    "Without collateral circulation the site is not used at all; another location, such as the femoral or brachial artery, is chosen.")],
  "Slides 7 and 6", mis={"Proceed and hold pressure for longer": "right action at the wrong stage", "Draw from the same artery through a line": "ignores the stated finding",
                         "Repeat the stick after warming the hand": "ignores the stated finding"}),

Q("The arterial sample", IOB, "fact",
  "A 66-year-old in the intensive care unit needs a direct arterial stick for a blood gas. Which artery is usually the site of choice?",
  ("The radial artery",
   "Correct. The radial artery is usually the site of choice, after checking the collateral blood supply via the ulnar and radial arteries (the Allen test)."),
  [("The ulnar artery",
    "The ulnar artery is the collateral supply checked by the Allen test before a RADIAL puncture; the radial artery is the usual site."),
   ("The femoral artery",
    "The femoral artery can also be used, with the brachial, but the radial artery is usually the site of choice."),
   ("The carotid artery",
    "The carotid is not among the sampling sites; the radial artery is usual, and the femoral or brachial can also be used.")],
  6, mis={"The ulnar artery": "adjacent fact (collateral)", "The femoral artery": "alternative site, not first choice", "The carotid artery": "not a listed site"}),

Q("The arterial sample", IOB, "fact",
  "A 52-year-old needs an arterial sample, and his clinician is weighing possible puncture sites. Which feature makes an artery suitable?",
  ("It is superficial and easily accessible",
   "Correct. A sampling artery must have collateral blood flow, must be superficial and easily accessible, and its surrounding tissues must be relatively non-sensitive."),
  [("It lies deep beneath sensitive tissue",
    "The reverse on both counts: the artery must be superficial and easily accessible, with relatively non-sensitive surrounding tissue."),
   ("It is the only supply to the limb",
    "An artery with no collateral blood flow is unsuitable; collateral flow must be present, which is why the Allen test is done."),
   ("It is the largest artery near the site",
    "Size is not the criterion; the artery must be superficial and accessible, with collateral flow and non-sensitive surrounding tissue.")],
  6, mis={"It lies deep beneath sensitive tissue": "reversed criteria", "It is the only supply to the limb": "reversed criterion (collateral flow)",
          "It is the largest artery near the site": "irrelevant criterion"}),

Q("The arterial sample", IOB, "fact",
  "A 71-year-old's arterial sample has been collected in a pre-heparinized, self-filling syringe. What is done before it goes to the lab?",
  ("All air bubbles are removed and it is put on ice",
   "Correct. The sample is collected in a pre-heparinized self-filling syringe, all air bubbles are removed, and it is placed on ice and sent to the lab."),
  [("The air bubbles are kept and it is kept warm",
    "Both steps are reversed: all air bubbles are removed and the sample is placed on ice before it is sent."),
   ("It is left to clot, then sent at room temperature",
    "The syringe is pre-heparinized, so the sample is not left to clot; it is cleared of air bubbles and placed on ice."),
   ("It is held at the bedside for a repeat draw",
    "The sample is sent to the lab on ice, and it can be used for a blood gas only if it is less than 3 hours old.")],
  8, mis={"The air bubbles are kept and it is kept warm": "reversed steps", "It is left to clot, then sent at room temperature": "ignores the heparinized syringe",
          "It is held at the bedside for a repeat draw": "delays the sample"}),

Q("The arterial sample", IOB, "fact",
  "A 64-year-old's arterial sample sat unanalyzed for 4 hours after it was drawn. What does that mean for the blood gas?",
  ("The sample is too old to be used",
   "Correct. A sample can only be used for an arterial blood gas if it is less than 3 hours old, so a 4-hour-old sample cannot be used."),
  [("It can be used if it was kept on ice",
    "Ice is part of handling, but the time limit still applies: a sample can only be used if it is less than 3 hours old."),
   ("It is valid for the oxygen values only",
    "The limit applies to the blood gas as a whole: the sample can only be used if it is less than 3 hours old."),
   ("It is valid as long as it has no bubbles",
    "Removing air bubbles is required, but the sample must also be less than 3 hours old to be used.")],
  8, mis={"It can be used if it was kept on ice": "right step, wrong conclusion", "It is valid for the oxygen values only": "false partial validity",
          "It is valid as long as it has no bubbles": "right step, wrong conclusion"}),

Q("The arterial sample", IOB, "fact",
  "A 66-year-old's arterial blood gas sample is labeled for the lab. Which detail about him must be recorded with it?",
  ("Room air, or any supplemental oxygen he is on",
   "Correct. Indicate whether the patient was breathing room air or describe any supplemental oxygen, because the oxygen pressure is directly affected by the fraction of inspired oxygen."),
  [("The time of his last meal",
    "Mealtime is not the detail the sample requires; it requires room air or the supplemental oxygen, because inspired oxygen directly affects the oxygen pressure."),
   ("His blood pressure at the draw",
    "Blood pressure is not the detail the sample requires; whether he breathed room air or supplemental oxygen is, since it directly affects the oxygen pressure."),
   ("The arm his last venous sample came from",
    "That is not the detail the sample requires; record room air or the supplemental oxygen, which directly affects the oxygen pressure.")],
  "Slides 8, 13 and 36", mis={"The time of his last meal": "irrelevant detail", "His blood pressure at the draw": "irrelevant detail",
                              "The arm his last venous sample came from": "irrelevant detail"}),

Q("The arterial sample", IOB, "fact",
  "A 68-year-old has just had a direct arterial stick for a blood gas. How is the puncture site managed?",
  ("Pressure for at least 2 minutes, until bleeding stops",
   "Correct. Hold pressure for a minimum of 2 minutes or longer as needed until the bleeding stops; a pressure dressing may be needed."),
  [("A plain adhesive bandage, with no pressure held",
    "An arterial stick needs pressure held for at least 2 minutes, longer if needed, and sometimes a pressure dressing."),
   ("Pressure only for the time the needle is withdrawn",
    "Pressure is held for a minimum of 2 minutes, longer as needed until bleeding stops, not just at withdrawal."),
   ("Ice on the site, as for the sample itself",
    "Ice is for the SAMPLE on its way to the lab; the site needs pressure for at least 2 minutes until bleeding stops.")],
  8, mis={"A plain adhesive bandage, with no pressure held": "omits a required step", "Pressure only for the time the needle is withdrawn": "too short",
          "Ice on the site, as for the sample itself": "confused step (sample handling)"}),

# =============================================================== objective c: indications
Q("Indications", IOC, "fact",
  "A 61-year-old woman is well today and is scheduled for a lung resection next week. Why might an arterial blood gas be drawn now?",
  ("To establish baseline values before the operation",
   "Correct. Establishing baseline values pre- and post-operatively is one of the indications for an arterial blood gas."),
  [("To grade the severity of her lung disease",
    "A blood gas does NOT indicate the degree of any abnormality; severity needs a physical assessment. Here it sets a pre-operative baseline."),
   ("To monitor her as a critically ill patient",
    "Monitoring critically ill patients is an indication, but she is well today; the gas is drawn to establish a pre-operative baseline."),
   ("To monitor response to ongoing therapy",
    "She is not on an ongoing therapy to follow; the indication here is a baseline before the operation.")],
  "Slides 3 and 5", mis={"To grade the severity of her lung disease": "common belief (degree)", "To monitor her as a critically ill patient": "ruled out by a stated finding",
                         "To monitor response to ongoing therapy": "ruled out by a stated finding"}),

Q("Indications", IOC, "fact",
  "A 74-year-old's arterial blood gas comes back abnormal, and a student asks how sick he is from the numbers alone. What is the best reply?",
  ("The gas cannot show the degree; examine him",
   "Correct. The blood gas does NOT indicate the degree of any abnormality; a physical assessment is needed (treat the patient and not the labs)."),
  [("The further from normal, the sicker he is",
    "The blood gas does not indicate the degree of any abnormality; severity comes from a physical assessment of the patient."),
   ("The bicarbonate alone grades his severity",
    "No single value grades severity: the blood gas does not indicate the degree of an abnormality; examine the patient."),
   ("A normal pH would rule out serious illness",
    "The labs must be checked against the clinical presentation, and the gas does not show degree; the patient has to be assessed.")],
  "Slides 5 and 49", mis={"The further from normal, the sicker he is": "common belief", "The bicarbonate alone grades his severity": "common belief",
                          "A normal pH would rule out serious illness": "common belief"}),

Q("Indications", IOC, "fact",
  "A 36-year-old with vomiting and confusion has an arterial blood gas ordered to evaluate her acid-base status. Which values does that evaluation rest on?",
  ("pH, bicarbonate and carbon dioxide",
   "Correct. The blood gas evaluates acid-base status through the pH, the bicarbonate and the carbon dioxide; oxygenation (oxygen) and ventilation (carbon dioxide) are its other two assessments."),
  [("pH, sodium and potassium",
    "Sodium and potassium are electrolytes; acid-base status is evaluated from the pH, bicarbonate and carbon dioxide."),
   ("Oxygen, hemoglobin and hematocrit",
    "These describe oxygenation and oxygen carriage; acid-base status rests on the pH, bicarbonate and carbon dioxide."),
   ("Bicarbonate, chloride and albumin",
    "Chloride and albumin enter the anion gap; acid-base status itself is evaluated from the pH, bicarbonate and carbon dioxide.")],
  "Slides 3 and 45", mis={"pH, sodium and potassium": "adjacent values (electrolytes)", "Oxygen, hemoglobin and hematocrit": "oxygenation values",
                          "Bicarbonate, chloride and albumin": "adjacent values (anion gap)"}),

Q("Indications", IOC, "next-test",
  "A 77-year-old with pneumonia is started on oxygen by nasal cannula. The team wants to know whether the oxygen therapy is working. Which arterial value answers that?",
  ("Partial pressure of oxygen",
   "Correct. The partial pressure of oxygen is used to evaluate the ability of the lungs to oxygenate blood and to assess the efficacy of oxygen therapy."),
  [("Partial pressure of carbon dioxide",
    "The carbon dioxide pressure assesses ventilation; the efficacy of oxygen therapy is assessed with the partial pressure of oxygen."),
   ("Base excess",
    "Base excess separates respiratory from nonrespiratory acid-base change; oxygen therapy is judged by the oxygen pressure."),
   ("Carboxyhemoglobin",
    "Carboxyhemoglobin indicates carbon monoxide poisoning; the oxygen pressure assesses the efficacy of oxygen therapy.")],
  "Slides 13 and 3", mis={"Partial pressure of carbon dioxide": "ventilation, not oxygenation", "Base excess": "adjacent blood gas value",
                          "Carboxyhemoglobin": "adjacent blood gas value"}),

Q("Indications", IOC, "fact",
  "A 63-year-old in shock has an arterial blood gas drawn. Besides how well his lungs are oxygenating his blood, what else can it indicate?",
  ("Failure of the heart and circulation",
   "Correct. Arterial blood indicates how well the lungs are oxygenating blood and whether the heart and circulation are failing."),
  [("How severe each abnormality is",
    "The blood gas does NOT indicate the degree of any abnormality; it shows whether the lungs oxygenate and the heart and circulation are failing."),
   ("Whether his liver is failing",
    "Liver function is not what the arterial blood gas indicates; it indicates lung oxygenation and whether the heart and circulation are failing."),
   ("How much blood he has lost",
    "Blood loss is not read from the gas; it indicates oxygenation by the lungs and whether the heart and circulation are failing.")],
  5, mis={"How severe each abnormality is": "common belief (degree)", "Whether his liver is failing": "unrelated organ",
          "How much blood he has lost": "unrelated measure"}),
]
