# -*- coding: utf-8 -*-
"""Lecture 45 vignette pool B -- simple disorders outside mixed-disorder reasoning: potassium and oxygen (s5), the
anion gap and its albumin correction (s7-8), compensation rules (s23-25), respiratory acidosis (s31-37), respiratory
alkalosis (s38-40), metabolic acidosis causes (s41-48), metabolic alkalosis (s51-55) and the stepwise method (s56-59).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md. Every blood value carries its range (scope gas()/lytes()).

Held for the scope (cms_e7l45_scope.py):
  values   every gas is internally consistent (pH from the bicarbonate / carbon dioxide ratio, within about 0.02);
           metabolic acidosis carbon dioxide sits inside the Winter range, so no item hides a mixed disorder;
           every raised-gap item has a gap rise equal to (or within 2 of) the bicarbonate fall, so no hidden second
           metabolic disorder either. Gap = sodium - (chloride + bicarbonate), checked by script.
  ratios   the respiratory acidosis 1 and 3.5 per 10 ratios and the metabolic alkalosis 0.75 per 1 ratio are GIVEN in
           the stem with baselines 40 mm Hg and 25 mEq/L. The respiratory alkalosis ratios are never used.
  albumin  the correction rule (2.5 per 1 g/dL below 4.5) is NOT given; corrected gaps are asked as numbers or sit
           well clear of 12.
  urine chloride  one item quotes a number (60 mEq/L, against the over-40 saline-unresponsive cut); the others say low.
  contested never keyed: alkali ingestion group, hypoparathyroidism group, pulmonary embolism direction, the category
           label of the neuromuscular diseases; diabetic ketoacidosis is always named by phase (active).
  recording-only content (shortcuts, paper bag, the board cases) is not used.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l45_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ABG(ph, pco2, hco3):
    return "Arterial blood gas: " + gas(ph, pco2, hco3) + "."


def CHEM(na, cl, hco3, k=None):
    return " Serum " + lytes(na, cl, hco3, k) + "."


RA_RATIO = (" For respiratory acidosis, bicarbonate is expected to rise 1 mEq/L per 10 mm Hg rise in carbon dioxide "
            "when acute and 3.5 mEq/L per 10 mm Hg when chronic, from baselines of 40 mm Hg and 25 mEq/L.")
MA_RATIO = (" For metabolic alkalosis, carbon dioxide is expected to rise 0.75 mm Hg per 1 mEq/L rise in bicarbonate, "
            "from baselines of 40 mm Hg and 25 mEq/L.")

QUESTIONS = [

# ================================================================ potassium and oxygen (s5)
V(T_DEF, IO_B,
  "A 47-year-old man is admitted after a crush injury with prolonged poor tissue perfusion. " + ABG("7.31", "29", "14")
  + " Which change should be expected from his acid-base disturbance itself?",
  [["Potassium moves out of cells, raising serum potassium",
    "Correct. A pH of 7.31 with a bicarbonate of 14 is a metabolic acidosis (poor perfusion and trauma cause lactic acidosis). In acidosis, hydrogen ions shift into cells and potassium shifts out of cells into the extracellular fluid, resulting in hyperkalemia."],
   ["Potassium moves into cells, lowering serum potassium",
    "Potassium moving into cells, with hypokalemia, is the shift of alkalosis. His pH is 7.31, an acidemia, so potassium leaves the cells instead. Tell: acidosis raises the serum potassium; alkalosis lowers it.", "reversed direction or value"],
   ["Hydrogen ions move out of cells into the blood",
    "Hydrogen ions leave cells in alkalosis, the body's way of adding acid back to the blood. In his acidosis the excess hydrogen ions move from the blood into cells. Tell: in acidosis hydrogen goes in and potassium comes out.", "reversed direction or value"],
   ["Hemoglobin holds oxygen more tightly, cutting delivery",
    "Increased hemoglobin affinity for oxygen, with less oxygen delivered to tissues, is the alkalosis effect. Acidosis lowers the affinity, so more oxygen is released to tissues. Tell: acid loosens hemoglobin's grip on oxygen.", "reversed direction or value"]],
  CS(5, 45), "complication", "complication"),

V(T_DEF, IO_B,
  "A 29-year-old woman has vomited repeatedly for 3 days. " + ABG("7.48", "47", "34")
  + " Which effect on oxygen delivery does her acid-base disorder produce?",
  [["Higher hemoglobin affinity; less oxygen delivered",
    "Correct. A pH of 7.48 with a bicarbonate of 34 is a metabolic alkalosis (vomiting loses gastric acid), and the carbon dioxide of 47 is respiratory compensation. Alkalosis increases hemoglobin's affinity for oxygen, so less oxygen is delivered to the tissues."],
   ["Lower hemoglobin affinity; more oxygen delivered",
    "Lower affinity with more oxygen released to tissues is the effect of acidosis. Her pH is 7.48, alkalemic, which does the opposite. Tell: match the oxygen effect to the side of 7.40 the pH is on.", "reversed direction or value"],
   ["Higher hemoglobin affinity; more oxygen delivered",
    "This pairs the right affinity change with the wrong consequence. When hemoglobin binds oxygen more tightly it releases less to the tissues, so delivery falls in her alkalosis. Tell: higher affinity and lower delivery travel together.", "confused mechanism or drug class"],
   ["Lower hemoglobin affinity; less oxygen delivered",
    "Lower affinity means hemoglobin gives oxygen up more easily, so delivery would rise, and lower affinity belongs to acidosis anyway. Her alkalosis raises affinity. Tell: affinity and delivery move in opposite directions.", "confused mechanism or drug class"]],
  C(5), "complication", "complication"),

V(T_DEF, IO_B,
  "A 31-year-old woman has been breathing rapidly for 30 minutes during a panic attack. She has not vomited, has no diarrhea and takes no medicines. "
  + ABG("7.54", "28", "23") + " Her potassium is 3.3 mEq/L " + K + ". Which process best accounts for her potassium level?",
  [["Potassium shifted into cells as hydrogen ions left them",
    "Correct. A pH of 7.54 with a carbon dioxide of 28 is a respiratory alkalosis from anxiety. In alkalosis hydrogen ions shift out of cells and potassium shifts into cells, resulting in hypokalemia, with no potassium actually lost from the body."],
   ["Potassium shifted out of cells as hydrogen ions entered",
    "That is the shift of acidosis, and it raises the serum potassium. Her pH is 7.54, alkalemic, so potassium moves the other way. Tell: a low potassium with a high pH is the alkalosis shift into cells.", "reversed direction or value"],
   ["Potassium lost through the gut from vomiting",
    "Vomiting causes a saline-responsive metabolic alkalosis with a high bicarbonate. She has not vomited, and her bicarbonate is 23 with a low carbon dioxide, a respiratory picture. Tell: the stem rules out vomiting.", "ruled out by a stated finding"],
   ["Severe depletion of total body potassium",
    "Severe potassium depletion is a saline-unresponsive cause of metabolic alkalosis, with a high bicarbonate. Her bicarbonate is 23 and her low carbon dioxide drives the pH, and nothing in her history removes potassium from the body. Tell: her potassium has moved, not been lost.", "adjacent fact"]],
  CS(5, 39), "etiology", "etiology"),

# ================================================================ anion gap and albumin correction (s7-8)
V(T_AG, IO_F,
  "A 54-year-old man with chronic kidney failure has fatigue. " + ABG("7.29", "30", "14")
  + CHEM("138", "103", "14", "4.0") + " What is his anion gap?",
  [["21",
    "Correct. Anion gap = sodium - (bicarbonate + chloride) = 138 - (14 + 103) = 138 - 117 = 21, above the normal 6 to 12. A raised gap with a low pH and low bicarbonate is a raised-gap metabolic acidosis, and renal failure is on that list."],
   ["11",
    "This uses a normal bicarbonate of 24 in place of his measured 14: 138 - (24 + 103) = 11. The formula takes the measured value, which is 14. Tell: plug in the patient's own bicarbonate, not the normal one.", "confused mechanism or drug class"],
   ["25",
    "This adds his potassium of 4.0 to the sodium: (138 + 4) - (14 + 103) = 25. The anion gap formula used here is sodium minus chloride and bicarbonate, with no potassium. Tell: potassium is not part of the calculation.", "confused mechanism or drug class"],
   ["35",
    "This subtracts only the chloride: 138 - 103 = 35, leaving out the bicarbonate. The gap subtracts both measured anions, chloride and bicarbonate. Tell: two anions come off the sodium, not one.", "confused mechanism or drug class"]],
  CS(7, 26, 45), "test finding", "classify"),

V(T_AG, IO_F,
  "A 63-year-old woman with months of poor oral intake is admitted with a new infection. " + ABG("7.33", "35", "18")
  + CHEM("136", "106", "18") + " Her albumin is 2.5 g/dL " + ALB + ". What is her anion gap after correction for her albumin?",
  [["17",
    "Correct. The measured gap is 136 - (18 + 106) = 12. The correction adds 2.5 for each 1 g/dL that albumin sits below 4.5: 4.5 - 2.5 = 2, and 2 x 2.5 = 5, so the corrected gap is 12 + 5 = 17, above the normal 6 to 12."],
   ["12",
    "This is her uncorrected gap, 136 - (18 + 106) = 12. With an albumin of 2.5 g/dL the gap must be corrected, and the correction adds 5. Tell: a low albumin hides unmeasured anions, so correct before calling the gap normal.", "wrong stage or severity"],
   ["14.5",
    "This counts the albumin drop from 3.5, the bottom of the normal range: (3.5 - 2.5) x 2.5 = 2.5, giving 14.5. The correction counts from 4.5 g/dL, a 2 g/dL drop worth 5. Tell: the reference point for the correction is 4.5.", "reversed direction or value"],
   ["19.5",
    "This counts the albumin drop from 5.5, the top of the normal range: (5.5 - 2.5) x 2.5 = 7.5, giving 19.5. The correction counts from 4.5 g/dL, a 2 g/dL drop worth 5. Tell: the reference point for the correction is 4.5.", "reversed direction or value"]],
  CS(8, 57), "test finding", "classify"),

V(T_AG, IO_F,
  "A 58-year-old man with cirrhosis and a low albumin has had watery diarrhea for 6 days. " + ABG("7.34", "36", "19")
  + CHEM("136", "112", "19") + " His albumin is 2.5 g/dL " + ALB + ". His anion gap calculates to 5. Which step comes next in interpreting the gap?",
  [["Correct the gap for his low albumin",
    "Correct. A low gap is most often a low albumin, and the gap must be corrected when albumin is abnormal. Adding 2.5 for each 1 g/dL below 4.5 gives 5 + 5 = 10, a normal gap, which fits a normal-gap metabolic acidosis from his diarrhea."],
   ["Screen for a plasma cell dyscrasia",
    "Plasma cell dyscrasias lower the gap through cationic paraproteins, but they are considered only when the gap stays low after correction. His corrected gap is 10, normal. Tell: rule out the low albumin first.", "wrong stage or severity"],
   ["Check for bromide intoxication",
    "Bromide intoxication is another rare cause of a low gap, kept for a gap that remains low once albumin is accounted for. His albumin is 2.5 g/dL and explains the low value. Tell: the common reason for a low gap is the albumin.", "wrong stage or severity"],
   ["Search the raised-gap causes",
    "The raised-gap list is used when the gap is above 12. His measured gap is 5 and his corrected gap 10, both at or below normal, so the normal-gap list applies, and diarrhea is on it. Tell: correct first, then pick the list.", "reversed direction or value"]],
  CS(8, 46, 48, 57), "initial test", "next step"),

V(T_AG, IO_D,
  "A 41-year-old woman has bipolar disorder treated with lithium and type 2 diabetes treated with metformin. Routine testing shows "
  + lytes("136", "106", "26") + ", albumin 4.4 g/dL " + ALB + ", and no monoclonal protein. Which part of her history best accounts for her anion gap?",
  [["Lithium",
    "Correct. Her gap is 136 - (26 + 106) = 4, below the normal 6 to 12. A decreased gap comes from added abnormal cations such as lithium, which are not counted in the formula. Her normal albumin and absent monoclonal protein remove the other low-gap causes."],
   ["Metformin",
    "Metformin is a cause of raised-gap metabolic acidosis, which would push the gap above 12 and lower the bicarbonate. Her gap is 4 and her bicarbonate 26. Tell: metformin raises the gap; hers is low.", "reversed direction or value"],
   ["A low serum albumin",
    "A low albumin is the usual reason for a low gap, but her albumin is 4.4 g/dL, normal, so there is nothing to correct for. Tell: check the albumin first; when it is normal, look for an added cation.", "ruled out by a stated finding"],
   ["A plasma cell dyscrasia",
    "A plasma cell dyscrasia lowers the gap through a cationic monoclonal protein. Her testing shows no monoclonal protein. Tell: the stem removes this cause and leaves her lithium.", "ruled out by a stated finding"]],
  CS(7, 48), "etiology", "etiology"),

V(T_AG, IO_F,
  "A 70-year-old man with heart failure, poor tissue perfusion and a low albumin is admitted. " + ABG("7.32", "32", "16")
  + CHEM("140", "108", "16") + " His albumin is 2.9 g/dL " + ALB + ". What is his anion gap after correction for his albumin?",
  [["20",
    "Correct. The measured gap is 140 - (16 + 108) = 16. His albumin is 4.5 - 2.9 = 1.6 g/dL below 4.5, and 1.6 x 2.5 = 4, so the corrected gap is 16 + 4 = 20, a raised gap that fits lactic acidosis from poor perfusion."],
   ["16",
    "This is the uncorrected gap, 140 - (16 + 108) = 16. With an albumin of 2.9 g/dL the gap must be corrected upward by 4. Tell: a low albumin makes the measured gap read too low.", "wrong stage or severity"],
   ["17.5",
    "This counts the albumin drop from 3.5, the bottom of the normal range: (3.5 - 2.9) x 2.5 = 1.5. The correction counts from 4.5 g/dL, a 1.6 g/dL drop worth 4. Tell: start the correction at 4.5.", "reversed direction or value"],
   ["22.5",
    "This counts the albumin drop from 5.5, the top of the normal range: (5.5 - 2.9) x 2.5 = 6.5. The correction counts from 4.5 g/dL, a 1.6 g/dL drop worth 4. Tell: start the correction at 4.5.", "reversed direction or value"]],
  CS(8, 45, 57), "test finding", "classify"),

V(T_AG, IO_F,
  "A 76-year-old woman with long-standing poor nutrition becomes confused with a low blood pressure and cool extremities. "
  + ABG("7.34", "36", "19") + CHEM("137", "106", "19") + " Her albumin is 2.1 g/dL " + ALB
  + ". Which acid-base disorder do her results show?",
  [["Raised anion gap metabolic acidosis",
    "Correct. Low pH and low bicarbonate make a metabolic acidosis. The measured gap is 137 - (19 + 106) = 12, but her albumin is 2.4 g/dL below 4.5, adding 2.4 x 2.5 = 6, so the corrected gap is 18, above 12. Poor perfusion causes lactic acidosis, a raised-gap cause."],
   ["Normal anion gap metabolic acidosis",
    "This reads the uncorrected gap of 12 as normal. With an albumin of 2.1 g/dL the gap must be corrected, and it rises to 18. Tell: a low albumin can hide a raised gap inside the normal range.", "wrong stage or severity"],
   ["Respiratory acidosis with renal compensation",
    "Respiratory acidosis needs a carbon dioxide above 45 with a raised bicarbonate. Hers is 36 with a bicarbonate of 19. Tell: the low bicarbonate, not the carbon dioxide, explains her low pH.", "ruled out by a stated finding"],
   ["Respiratory alkalosis with renal compensation",
    "Respiratory alkalosis has a pH above 7.45 with a low carbon dioxide. Her pH is 7.34, acidemic. Tell: compensation never pushes the pH past normal, so an acidemic pH rules out a primary alkalosis.", "ruled out by a stated finding"]],
  CS(8, 11, 45, 57), "test finding", "diagnosis"),

# ================================================================ compensation rules (s23-25)
V(T_COMP, IO_C,
  "A 68-year-old man has had obesity hypoventilation syndrome for many years. " + ABG("7.33", "66", "34") + RA_RATIO
  + " Which process accounts for his bicarbonate of 34?",
  [["The kidneys retaining bicarbonate over days",
    "Correct. A primary respiratory acidosis is compensated by the kidneys, which retain bicarbonate over hours to days. A chronic rise of 26 mm Hg predicts 25 + 3.5 x 2.6 = about 34, exactly his value, so this is the expected renal compensation."],
   ["The lungs retaining carbon dioxide to compensate",
    "Lungs adjusting carbon dioxide is the compensation for a metabolic disorder. His carbon dioxide of 66 is the primary problem, so the compensation must come from the other system. Tell: respiratory cause, renal compensation.", "confused mechanism or drug class"],
   ["A second, primary metabolic alkalosis",
    "An added metabolic alkalosis would push the bicarbonate above the predicted value. The chronic rule predicts about 34, and his is 34. Tell: a bicarbonate that matches the expected compensation needs no second disorder.", "competing diagnosis"],
   ["The kidneys excreting acid within minutes",
    "Renal control of bicarbonate occurs over hours to days, not minutes; the lungs are the fast system. His history spans years, which is why the larger chronic rise is seen. Tell: kidneys are slow, lungs are quick.", "wrong stage or severity"]],
  CS(19, 23, 24, 34), "test finding", "compensation"),

V(T_COMP, IO_E,
  "A 44-year-old man has had nasogastric suction for 4 days after bowel surgery. His arterial pH is 7.49 " + PH
  + " and his bicarbonate 33 mEq/L " + HCO3 + "." + MA_RATIO + " What carbon dioxide is expected from appropriate compensation?",
  [["46 mm Hg",
    "Correct. Bicarbonate has risen 33 - 25 = 8 mEq/L. At 0.75 mm Hg per 1 mEq/L, carbon dioxide should rise 8 x 0.75 = 6, so the expected value is 40 + 6 = 46 mm Hg. In metabolic alkalosis the lungs compensate by retaining carbon dioxide."],
   ["34 mm Hg",
    "This subtracts the 6 mm Hg instead of adding it. The lungs compensate an alkalosis by retaining carbon dioxide, which raises it. Tell: in metabolic alkalosis the carbon dioxide goes up, in the same direction as the bicarbonate.", "reversed direction or value"],
   ["40 mm Hg",
    "This assumes no compensation. The lungs respond to a metabolic alkalosis by hypoventilating, so carbon dioxide rises to about 46. Tell: an unchanged carbon dioxide would mean the compensation is missing.", "wrong stage or severity"],
   ["48 mm Hg",
    "This uses 1 mm Hg per 1 mEq/L: 40 + 8 = 48. The given ratio is 0.75, so the rise is 6, not 8. Tell: multiply the bicarbonate rise by 0.75.", "confused mechanism or drug class"]],
  CS(24, 53), "test finding", "classify"),

V(T_COMP, IO_E,
  "A 72-year-old woman has chronic respiratory acidosis from long-standing chronic obstructive pulmonary disease. "
  + ABG("7.33", "68", "35") + " A student predicts her kidneys will bring her pH back to 7.40 with time. Which statement about her compensation is accurate?",
  [["It moves pH toward normal without fully correcting it",
    "Correct. Compensation will not fully correct the pH disturbance; the underlying condition must be corrected to restore balance. Her kidneys have raised the bicarbonate to 35, which pulls the pH up toward normal, but it remains 7.33."],
   ["It fully restores pH once 48 hours have passed",
    "The chronic renal response is in place after 24 to 48 hours, but it still falls short of a normal pH; her pH is 7.33 despite years of disease. Tell: compensation narrows the gap to normal but does not close it.", "reversed direction or value"],
   ["It works through the lungs blowing off carbon dioxide",
    "Lungs blowing off carbon dioxide compensate a metabolic acidosis. Her primary problem is respiratory, so the kidneys compensate by retaining bicarbonate. Tell: the compensating system is the other one.", "confused mechanism or drug class"],
   ["It overshoots, leaving her slightly alkalemic",
    "Compensation does not overshoot into the opposite state; an alkalemic pH in a retainer would point to an added disorder. Her pH is 7.33. Tell: a simple disorder keeps the pH on the side of its primary problem.", "reversed direction or value"]],
  CS(23, 34), "prognosis", "compensation"),

V(T_COMP, IO_E,
  "A 66-year-old woman taking a diuretic has a metabolic alkalosis. " + ABG("7.49", "48", "35") + MA_RATIO
  + " How should her respiratory compensation be judged?",
  [["Appropriate; a simple metabolic alkalosis",
    "Correct. Bicarbonate has risen 35 - 25 = 10, so carbon dioxide should rise 10 x 0.75 = 7.5, to about 47.5. Her carbon dioxide of 48 matches, so the compensation is appropriate and no second disorder is needed. Diuretics are a saline-responsive cause."],
   ["Excessive; an added respiratory acidosis",
    "Excess compensation would show a carbon dioxide well above the predicted 47.5. Hers is 48, on target. Tell: a value that matches the calculation is appropriate compensation, not excess.", "wrong stage or severity"],
   ["Inadequate; an added respiratory alkalosis",
    "Inadequate compensation would leave the carbon dioxide well below the predicted 47.5. Hers is 48. Tell: the carbon dioxide has risen by the expected amount.", "wrong stage or severity"],
   ["Primary respiratory acidosis, renally compensated",
    "A primary respiratory acidosis has a pH below 7.35. Her pH is 7.49, alkalemic, so the high carbon dioxide is a response, not the cause. Tell: the pH names the primary side; the raised bicarbonate fits it.", "competing diagnosis"]],
  CS(23, 24, 26, 53), "test finding", "compensation"),

V(T_COMP, IO_C,
  "A 37-year-old man has had profuse watery diarrhea for 4 days and is breathing deeply. " + ABG("7.32", "30", "15")
  + " What does his carbon dioxide of 30 represent?",
  [["Respiratory compensation for metabolic acidosis",
    "Correct. A low pH with a low bicarbonate is a metabolic acidosis, and diarrhea is a common cause. When the cause is metabolic, compensation is respiratory: increased breathing lowers carbon dioxide, which pulls the pH toward normal without fully correcting it."],
   ["A primary respiratory alkalosis",
    "A primary respiratory alkalosis would raise the pH above 7.45. His pH is 7.32, acidemic, so the low carbon dioxide cannot be the primary problem. Tell: the pH points to the low bicarbonate as the primary change.", "ruled out by a stated finding"],
   ["Renal compensation for respiratory alkalosis",
    "Renal compensation changes bicarbonate, not carbon dioxide, and it would follow a primary respiratory alkalosis with a high pH. His pH is 7.32. Tell: carbon dioxide changes are the lungs' work.", "confused mechanism or drug class"],
   ["Carbon dioxide retention from hypoventilation",
    "Hypoventilation raises carbon dioxide above 45. His is 30, low, from breathing more. Tell: a low carbon dioxide means more ventilation, not less.", "reversed direction or value"]],
  CS(23, 41, 46), "manifestation", "compensation"),

# ================================================================ respiratory acidosis (s31-37)
V(T_RACID, IO_E,
  "A 61-year-old man is brought in drowsy, and no history is available. " + ABG("7.32", "70", "35") + RA_RATIO
  + " Which form of disorder do these values fit?",
  [["Chronic respiratory acidosis",
    "Correct. Low pH with a high carbon dioxide is a respiratory acidosis. Carbon dioxide has risen 30 mm Hg: acute compensation predicts 25 + 3 = 28, chronic predicts 25 + 3.5 x 3 = 35.5. His bicarbonate of 35 sits at the chronic value, so the kidneys have had days to respond."],
   ["Acute respiratory acidosis",
    "An acute rise of 30 mm Hg predicts a bicarbonate of only 25 + 3 = 28. His is 35, far above that. Tell: a bicarbonate near the 3.5-per-10 value means the kidneys have had at least 24 to 48 hours.", "wrong stage or severity"],
   ["Metabolic alkalosis with compensation",
    "A primary metabolic alkalosis has a pH above 7.45. His pH is 7.32, acidemic, so the high bicarbonate is the response, not the cause. Tell: the pH tells you which change is primary.", "competing diagnosis"],
   ["Respiratory alkalosis with compensation",
    "Respiratory alkalosis has a low carbon dioxide and a high pH. His carbon dioxide is 70 and his pH 7.32. Tell: a high carbon dioxide with acidemia is respiratory acidosis.", "reversed direction or value"]],
  CS(33, 34, 35), "test finding", "compensation"),

V(T_RACID, IO_E,
  "A 23-year-old man is found unresponsive about an hour after an opioid overdose. His arterial pH is 7.28 " + PH
  + " and his carbon dioxide 60 mm Hg " + PCO2 + "." + RA_RATIO + " What bicarbonate is expected for this disorder?",
  [["27 mEq/L",
    "Correct. A rise in carbon dioxide over an hour is acute. Carbon dioxide has risen 60 - 40 = 20 mm Hg, and the acute rule adds 1 mEq/L per 10 mm Hg, so bicarbonate should be 25 + 2 = 27 mEq/L."],
   ["25 mEq/L",
    "This assumes no change at all. Even an acute respiratory acidosis raises plasma bicarbonate a little through cell buffering, 1 mEq/L per 10 mm Hg. Tell: acute compensation is small, not absent.", "wrong stage or severity"],
   ["29 mEq/L",
    "This uses 2 mEq/L per 10 mm Hg, which is not the given acute ratio. A 20 mm Hg rise at 1 per 10 adds 2, giving 27. Tell: use the ratio for acute respiratory acidosis, 1 per 10.", "confused mechanism or drug class"],
   ["32 mEq/L",
    "This applies the chronic rule: 25 + 3.5 x 2 = 32. His overdose was an hour ago, too soon for the kidneys, which need 24 to 48 hours of sustained hypercapnia. Tell: an hour-old event takes the acute ratio.", "wrong stage or severity"]],
  CS(33, 34, 35), "test finding", "classify"),

V(T_RACID, IO_E,
  "A 47-year-old woman with asthma for 20 years has had severe bronchospasm for the last 2 hours. " + ABG("7.29", "58", "27") + RA_RATIO
  + " How should her bicarbonate be interpreted?",
  [["Acute; the rise fits 1 per 10",
    "Correct. Carbon dioxide has risen 18 mm Hg. The acute rule predicts 25 + 1.8 = about 27, and the chronic rule 25 + 6.3 = about 31. Her bicarbonate of 27 matches the acute value, fitting a 2-hour episode of acute airway obstruction."],
   ["Chronic; the rise fits 3.5 per 10",
    "The chronic rule predicts about 31 for an 18 mm Hg rise. Her bicarbonate is 27, well short of it. Tell: the kidneys add the larger rise only after 24 to 48 hours of sustained hypercapnia.", "wrong stage or severity"],
   ["Chronic, as her asthma is long-standing",
    "Chronicity is judged from how long the carbon dioxide has been raised, not how long the disease has existed. Her hypercapnia began 2 hours ago, and the bicarbonate matches the acute value. Tell: date the high carbon dioxide, not the diagnosis.", "common lay belief"],
   ["Excessive; a separate metabolic alkalosis",
    "A separate metabolic alkalosis would push the bicarbonate above the predicted value. The acute rule predicts about 27, and hers is 27. Tell: a bicarbonate on target needs no second disorder.", "competing diagnosis"]],
  CS(32, 33, 34, 35), "test finding", "compensation"),

V(T_RACID, IO_D,
  "A 74-year-old woman is drowsy 2 days after hip surgery. She takes an opioid for pain, a benzodiazepine at night for anxiety, a thiazide for hypertension and an inhaled bronchodilator for asthma. "
  + ABG("7.26", "62", "27") + " Which of her medicines should be stopped?",
  [["The opioid and the benzodiazepine",
    "Correct. Low pH with a high carbon dioxide and a bicarbonate only slightly raised is an acute respiratory acidosis. Treatment starts with the cause and a medicine review: stop respiratory depressants, narcotics and benzodiazepines, which reduce ventilation."],
   ["The thiazide and the bronchodilator",
    "A thiazide causes metabolic alkalosis, not a respiratory acidosis, and a bronchodilator opens the airways rather than depressing breathing. Tell: the drugs to stop in respiratory acidosis are the respiratory depressants.", "adjacent fact"],
   ["The inhaled bronchodilator alone",
    "Her bronchodilator treats bronchospasm, itself a cause of respiratory acidosis, so stopping it could worsen ventilation. Tell: the sedating drugs, not the airway drug, explain a drowsy patient with a high carbon dioxide.", "reversed direction or value"],
   ["The thiazide diuretic alone",
    "Diuretics cause a saline-responsive metabolic alkalosis with a raised bicarbonate. Her problem is a high carbon dioxide from reduced breathing. Tell: look for respiratory depressants on the list, not diuretics.", "adjacent fact"]],
  CS(32, 36), "avoid", "avoid"),

V(T_RACID, IO_D,
  "A 67-year-old man with severe pneumonia is increasingly somnolent. " + ABG("7.16", "88", "30")
  + " His partial pressure of oxygen is 36 mm Hg " + PO2 + ". Which is the most appropriate next step?",
  [["Secure the airway and ventilate mechanically",
    "Correct. A carbon dioxide above 80 mm Hg with life-threatening hypoxia (partial pressure of oxygen below 40) is an acute, severe failure of carbon dioxide excretion. He needs adequate ventilation, which may mean an emergency airway and a mechanical ventilator, plus oxygen."],
   ["Withhold oxygen to protect his breathing drive",
    "Oxygen is part of treatment, and his partial pressure of oxygen of 36 is life-threatening. Careful oxygen applies to chronic retainers, and even then it is given, not withheld. Tell: severe hypoxia is treated, not tolerated.", "reversed direction or value"],
   ["Coach him in slow, mindful breathing",
    "Mindful breathing helps control the hyperventilation of respiratory alkalosis. He is under-ventilating with a carbon dioxide of 88 and is somnolent. Tell: breathing coaching is for too much breathing, not too little.", "adjacent fact"],
   ["Repeat the blood gas in 24 hours",
    "Waiting suits a stable patient, not one whose carbon dioxide is above 80 with an oxygen below 40. These values mark an acute, severe impairment that needs ventilation now. Tell: the thresholds call for action, not observation.", "wrong stage or severity"]],
  CS(32, 36), "escalation", "next step"),

V(T_RACID, IO_D,
  "A 70-year-old man with long-standing chronic obstructive pulmonary disease and chronic carbon dioxide retention has an exacerbation. "
  + ABG("7.32", "74", "37") + " His partial pressure of oxygen is 52 mm Hg " + PO2 + ". Which approach should be avoided?",
  [["Driving his carbon dioxide down rapidly",
    "Correct. His bicarbonate of 37 shows chronic renal compensation. Treatment is similar to acute disease but with careful oxygen, because a rapidly falling carbon dioxide in chronic respiratory acidosis may trigger the complications of alkalosis: cardiac arrhythmias, reduced cerebral perfusion and seizures."],
   ["Treating the cause of the exacerbation",
    "Treating the underlying condition is the first step of respiratory acidosis treatment, acute or chronic. Tell: the risk in a chronic retainer comes from correcting carbon dioxide too fast, not from treating its cause.", "reversed direction or value"],
   ["Giving oxygen in carefully titrated amounts",
    "Careful oxygen administration is exactly what chronic respiratory acidosis calls for, and his partial pressure of oxygen of 52 is low. Tell: oxygen is given with care, not avoided.", "reversed direction or value"],
   ["Reviewing his medicines for sedatives",
    "Looking at the medication list and stopping respiratory depressants is part of treatment in both acute and chronic respiratory acidosis. Tell: a medicine review helps; a rapid fall in carbon dioxide harms.", "reversed direction or value"]],
  CS(34, 36, 37), "avoid", "avoid"),

V(T_RACID, IO_D,
  "A 66-year-old woman with chronic respiratory acidosis from kyphoscoliosis is intubated, and the ventilator lowers her carbon dioxide from 70 to 40 mm Hg within an hour. Her bicarbonate is 35 mEq/L " + HCO3
  + ". Which complication is she now at risk for?",
  [["Cardiac arrhythmias and seizures",
    "Correct. In chronic respiratory acidosis the kidneys have raised bicarbonate over days, and it falls slowly. Lowering carbon dioxide rapidly leaves that bicarbonate unopposed, and the alkalosis may cause cardiac arrhythmias, reduced cerebral perfusion and seizures."],
   ["Hyperkalemia from potassium leaving cells",
    "Potassium leaves cells in acidosis. A rapid fall in her carbon dioxide with a bicarbonate of 35 creates an alkalosis, which moves potassium into cells and lowers it. Tell: the risk after over-correction is alkalosis, so think low potassium.", "reversed direction or value"],
   ["Improved oxygen delivery to tissues",
    "Alkalosis increases hemoglobin's affinity for oxygen and decreases delivery to tissues. Her sudden alkalosis worsens delivery. Tell: alkalosis holds oxygen on hemoglobin.", "reversed direction or value"],
   ["A worsening metabolic acidosis",
    "Her retained bicarbonate of 35 is unopposed once the carbon dioxide falls, which produces alkalosis, not acidosis; a high bicarbonate after high carbon dioxide is the post-hypercapnia pattern. Tell: the leftover bicarbonate makes her alkalotic.", "reversed direction or value"]],
  CS(34, 37, 5), "complication", "complication"),

V(T_RACID, IO_D,
  "A 38-year-old man with generalized anxiety disorder and interstitial pulmonary fibrosis is brought in after a car crash with a flail chest (a rib segment moving inward on inspiration). "
  + ABG("7.31", "56", "27") + " Which part of his history explains this blood gas?",
  [["The flail chest",
    "Correct. Low pH with a high carbon dioxide is a respiratory acidosis, and the bicarbonate of 27 fits an acute rise. Respiratory acidosis comes from decreased ventilation, and thoracic cage injury such as a flail chest is a listed cause."],
   ["His anxiety disorder",
    "Anxiety causes respiratory alkalosis, with hyperventilation, a low carbon dioxide and a high pH. His carbon dioxide is 56 and his pH 7.31. Tell: anxiety lowers carbon dioxide; his is high.", "reversed direction or value"],
   ["His interstitial fibrosis",
    "Interstitial fibrosis decreases lung compliance and is listed as a cause of respiratory alkalosis, a low carbon dioxide state. His carbon dioxide is 56. Tell: fibrosis drives breathing up; his ventilation has fallen.", "reversed direction or value"],
   ["Pain from his injuries",
    "Pain drives hyperventilation, and treating pain is part of managing respiratory alkalosis. His carbon dioxide is raised, not lowered. Tell: pain would push the carbon dioxide below 35, not above 45.", "reversed direction or value"]],
  CS(31, 32, 39, 40), "etiology", "etiology"),

# ================================================================ respiratory alkalosis (s38-40)
V(T_RALK, IO_D,
  "A 52-year-old man is sedated on a mechanical ventilator after abdominal surgery. " + ABG("7.55", "26", "22")
  + " Which ventilator change is most appropriate?",
  [["Lower the set rate or tidal volume",
    "Correct. A pH of 7.55 with a carbon dioxide of 26 is a respiratory alkalosis, and on a ventilator the fix is to decrease minute volume by lowering the number of breaths per minute or the tidal volume, so less carbon dioxide is blown off."],
   ["Raise the set rate or tidal volume",
    "Raising rate or tidal volume increases minute volume and blows off more carbon dioxide, deepening the alkalosis. His carbon dioxide is already 26. Tell: too much ventilation is the problem, so turn it down.", "reversed direction or value"],
   ["Give saline with potassium replacement",
    "Fluid and potassium replacement treat a saline-responsive metabolic alkalosis with a high bicarbonate. His bicarbonate is 22 and the low carbon dioxide drives the pH. Tell: a respiratory alkalosis is fixed at the ventilator.", "competing diagnosis"],
   ["Leave the settings; mild alkalosis needs nothing",
    "Treatment is usually not required only for a mild change, a pH below 7.50. His pH is 7.55. Tell: above 7.50 on a ventilator, decrease minute volume.", "wrong stage or severity"]],
  CS(38, 40), "first-line", "treatment"),

V(T_RALK, IO_D,
  "A 26-year-old woman has episodes of rapid breathing and palpitations when she is anxious; her examination is otherwise normal. "
  + ABG("7.48", "32", "23") + " Which counseling point is most appropriate?",
  [["Slow, mindful breathing can ease the episodes",
    "Correct. A pH of 7.48 with a low carbon dioxide is a mild respiratory alkalosis from anxiety. With a pH below 7.50 treatment is usually not required; treating the anxiety and mindful breathing to control the hyperventilation are the measures."],
   ["Faster breathing will help clear the episodes",
    "Faster breathing blows off more carbon dioxide and raises the pH further. Her carbon dioxide is already 32 from hyperventilation. Tell: the fix for over-breathing is slower breathing.", "reversed direction or value"],
   ["Daily potassium supplements prevent the episodes",
    "Alkalosis can lower potassium by shifting it into cells, but supplements do not stop hyperventilation, and her episodes come from anxiety. Tell: treat the cause of the breathing, not a shifted electrolyte.", "adjacent fact"],
   ["She will need mechanical ventilation if they recur",
    "Mechanical ventilation is for failing ventilation, as in severe respiratory acidosis. Her pH of 7.48 is a mild alkalosis that usually needs no treatment. Tell: mild anxiety hyperventilation is managed with breathing, not a ventilator.", "wrong stage or severity"]],
  CS(39, 40), "education", "education"),

# ================================================================ metabolic acidosis (s41-48)
V(T_MACID, IO_F,
  "A 19-year-old man with type 1 diabetes has 2 days of abdominal pain and increased urination, and Kussmaul breathing (deep, regular, sighing breaths). Serum ketones are positive. "
  + ABG("7.26", "23", "10") + CHEM("135", "100", "10") + " Which acid-base disorder is present?",
  [["Raised anion gap metabolic acidosis",
    "Correct. Low pH with a bicarbonate of 10 is a metabolic acidosis, and the gap is 135 - (10 + 100) = 25, above 12. Active diabetic ketoacidosis is one of the raised-gap causes, and Kussmaul breathing is seen with severe acidosis; the low carbon dioxide is compensation."],
   ["Normal anion gap metabolic acidosis",
    "A normal-gap acidosis has a gap of 6 to 12 with a raised chloride. His gap is 25 and his chloride 100. Tell: ketoacids are unmeasured anions that raise the gap; the normal-gap list is for bicarbonate loss.", "ruled out by a stated finding"],
   ["Respiratory alkalosis with renal compensation",
    "His carbon dioxide is low, but a primary respiratory alkalosis would make the pH high. His pH is 7.26. Tell: a low carbon dioxide with acidemia is compensation for a metabolic acidosis.", "ruled out by a stated finding"],
   ["Respiratory acidosis with renal compensation",
    "Respiratory acidosis needs a carbon dioxide above 45. His is 23, and his deep breathing is lowering it. Tell: Kussmaul breathing blows carbon dioxide off; it does not retain it.", "reversed direction or value"]],
  CS(42, 44, 45), "test finding", "diagnosis"),

V(T_MACID, IO_D,
  "A 45-year-old man has renal tubular acidosis, irritable bowel syndrome with intermittent diarrhea, and glaucoma treated with an oral carbonic anhydrase inhibitor. His roommate found him confused beside an open container of antifreeze. "
  + ABG("7.23", "22", "9") + CHEM("140", "105", "9") + " Which part of his history best accounts for this blood gas?",
  [["Ethylene glycol in the antifreeze",
    "Correct. Low pH with a bicarbonate of 9 is a metabolic acidosis, and the gap is 140 - (9 + 105) = 26, well above 12. Ethylene glycol is a toxic alcohol on the raised-gap list. His other conditions all cause a normal-gap acidosis."],
   ["Renal tubular acidosis",
    "Renal tubular acidosis causes a normal-gap acidosis through chloride retention, with a gap of 6 to 12 and a high chloride. His gap is 26 and his chloride 105. Tell: calculate the gap before choosing a list.", "competing diagnosis"],
   ["Intermittent diarrhea",
    "Diarrhea causes a normal-gap acidosis by gastrointestinal bicarbonate loss, with a high chloride. His gap is 26. Tell: bicarbonate loss leaves the gap normal; a toxin adds unmeasured anions.", "competing diagnosis"],
   ["The carbonic anhydrase inhibitor",
    "Carbonic anhydrase inhibitors cause a normal-gap acidosis by loss of bicarbonate. His gap of 26 needs a raised-gap cause. Tell: this drug is on the normal-gap list, not the toxin list.", "competing diagnosis"]],
  CS(44, 45, 46, 47), "etiology", "etiology"),

V(T_MACID, IO_D,
  "A 59-year-old woman has type 2 diabetes treated with metformin, takes aspirin daily, takes isoniazid for latent tuberculosis, and has had profuse watery diarrhea for 5 days. "
  + ABG("7.32", "30", "15") + CHEM("138", "114", "15") + " Which part of her history best accounts for this blood gas?",
  [["Her diarrhea",
    "Correct. Low pH and bicarbonate make a metabolic acidosis, and the gap is 138 - (15 + 114) = 9, normal, with a high chloride. Diarrhea, gastrointestinal bicarbonate loss, is one of the most common normal-gap causes. Metformin, aspirin and isoniazid all raise the gap."],
   ["Metformin",
    "Metformin causes a raised-gap acidosis, with a gap above 12. Her gap is 9 with a high chloride. Tell: metformin sits on the raised-gap list.", "competing diagnosis"],
   ["Aspirin",
    "Salicylates are a toxin on the raised-gap list. Her gap is 9, normal, and her chloride is high. Tell: a normal gap with a high chloride points to bicarbonate loss, not aspirin.", "competing diagnosis"],
   ["Isoniazid",
    "Isoniazid is a cause of raised-gap acidosis, which would push the gap above 12. Her gap is 9. Tell: with a normal gap, pick from the bicarbonate-loss causes.", "competing diagnosis"]],
  CS(44, 46, 47), "etiology", "etiology"),

V(T_MACID, IO_D,
  "A 66-year-old man has type 2 diabetes treated with metformin, hypertension treated with a thiazide, asthma treated with an inhaled bronchodilator, and kidney function that has worsened over a month. Serum ketones are negative. "
  + ABG("7.27", "25", "11") + CHEM("139", "104", "11") + " Which of his medicines should be stopped because it adds to this acidosis?",
  [["Metformin",
    "Correct. Low pH with a bicarbonate of 11 is a metabolic acidosis, and the gap is 139 - (11 + 104) = 24, well above 12. Metformin is on the raised-gap list, and stopping possible contributors is part of treating the underlying cause."],
   ["The thiazide",
    "Diuretics cause a saline-responsive metabolic alkalosis, with a raised bicarbonate. His bicarbonate is 11. Tell: a thiazide pushes the pH up; it does not explain an acidosis.", "reversed direction or value"],
   ["The bronchodilator",
    "An inhaled bronchodilator is not on any metabolic acidosis list, and it keeps his airways open. His gap of 24 points to a raised-gap cause. Tell: of his medicines, only metformin is a raised-gap cause.", "adjacent fact"],
   ["No change to his medicines",
    "Metformin is a listed raised-gap cause, and his gap is 24 with negative ketones. Leaving it in place keeps adding to the acidosis. Tell: when a raised-gap drug is on the list, stop it.", "wrong stage or severity"]],
  CS(44, 45), "avoid", "avoid"),

V(T_MACID, IO_D,
  "A 64-year-old man has an ileal loop bladder (a ureteral diversion) after bladder cancer surgery, takes isoniazid for latent tuberculosis, and has type 2 diabetes treated with metformin. Serum ketones are negative. "
  + ABG("7.34", "31", "16") + CHEM("139", "113", "16") + " Which part of his history best accounts for this blood gas?",
  [["The ileal loop bladder",
    "Correct. Low pH and bicarbonate make a metabolic acidosis, and the gap is 139 - (16 + 113) = 10, normal, with a high chloride. Ureteral diversion and the ileal loop bladder are on the normal-gap list. Isoniazid and metformin raise the gap."],
   ["Isoniazid",
    "Isoniazid is on the raised-gap list, with a gap above 12. His gap is 10. Tell: a normal gap with a high chloride rules out the raised-gap drugs.", "competing diagnosis"],
   ["Metformin",
    "Metformin causes a raised-gap acidosis. His gap is 10 and his chloride 113. Tell: metformin raises the gap; his is normal.", "competing diagnosis"],
   ["Diabetic ketoacidosis, active",
    "Active diabetic ketoacidosis is a raised-gap cause, and his ketones are negative with a gap of 10. Tell: ketoacids add unmeasured anions; his gap has not risen.", "ruled out by a stated finding"]],
  CS(44, 46, 47), "etiology", "etiology"),

V(T_MACID, IO_F,
  "A 50-year-old woman is confused. " + ABG("7.27", "25", "11")
  + " Serum electrolytes were drawn with the gas. Which step narrows the list of causes next?",
  [["Calculate the anion gap",
    "Correct. Her low pH and bicarbonate make a metabolic acidosis, and her carbon dioxide is lowered by compensation. The next step is to calculate the anion gap, which splits the causes into the raised-gap list and the normal-gap list."],
   ["Measure the urine chloride",
    "Urine chloride separates saline-responsive from saline-unresponsive metabolic alkalosis. Her pH is 7.27, an acidosis. Tell: urine chloride is the sorting test for alkalosis; the gap sorts acidosis.", "adjacent fact"],
   ["Apply the 3.5-per-10 bicarbonate rule",
    "That ratio estimates compensation in chronic respiratory acidosis, a high carbon dioxide state. Her carbon dioxide is 25 and her bicarbonate 11. Tell: her primary change is metabolic, so the respiratory acidosis rules do not apply.", "adjacent fact"],
   ["Repeat the blood gas in 24 hours",
    "Repeating the gas later delays the cause, and treatment of acidosis begins with finding the underlying condition. Tell: the electrolytes are already in hand, so the gap can be calculated now.", "wrong stage or severity"]],
  CS(26, 43, 57), "initial test", "next step"),

V(T_MACID, IO_D,
  "A 72-year-old man has chronic kidney failure that has worsened over months, adrenal insufficiency on hormone replacement, glaucoma treated with an oral carbonic anhydrase inhibitor, and leg edema treated with a loop diuretic. "
  + ABG("7.32", "30", "15") + CHEM("138", "103", "15") + " Which part of his history best accounts for this blood gas?",
  [["His kidney failure",
    "Correct. Low pH and bicarbonate make a metabolic acidosis, and the gap is 138 - (15 + 103) = 20, above 12. Renal failure, acute or chronic, is one of the big four raised-gap causes. His other conditions do not raise the gap."],
   ["His adrenal insufficiency",
    "Adrenal insufficiency causes a normal-gap acidosis, with a gap of 6 to 12 and a high chloride. His gap is 20 and his chloride 103. Tell: adrenal insufficiency is on the normal-gap list.", "competing diagnosis"],
   ["The carbonic anhydrase inhibitor",
    "Carbonic anhydrase inhibitors cause a normal-gap acidosis by bicarbonate loss. His gap is 20. Tell: a raised gap needs unmeasured anions, which failing kidneys retain.", "competing diagnosis"],
   ["The loop diuretic",
    "Diuretics cause a saline-responsive metabolic alkalosis with a high bicarbonate. His bicarbonate is 15 and his pH 7.32. Tell: a diuretic pushes the pH the other way.", "reversed direction or value"]],
  CS(44, 45, 46), "etiology", "etiology"),

V(T_MACID, IO_D,
  "A 55-year-old woman has received large volumes of normal saline for 3 days after abdominal surgery. She also takes acetaminophen for pain, has nasogastric suction, and takes a loop diuretic for edema. "
  + ABG("7.32", "30", "15") + CHEM("140", "115", "15") + " Which part of her care should be limited?",
  [["Further large-volume normal saline",
    "Correct. Low pH and bicarbonate make a metabolic acidosis, and the gap is 140 - (15 + 115) = 10, normal, with a high chloride. Saline infusion is a normal-gap cause, so the infusion feeding the acidosis is the part to limit."],
   ["Her acetaminophen for pain",
    "Acetaminophen toxicity causes a raised-gap acidosis through 5-oxoproline. Her gap is 10, normal. Tell: a normal gap with a high chloride fits saline, not acetaminophen.", "competing diagnosis"],
   ["Her nasogastric suction",
    "Gastric suction removes acid and causes a saline-responsive metabolic alkalosis. Her pH is 7.32 with a low bicarbonate. Tell: suction pushes the pH up, so it is not feeding this acidosis.", "reversed direction or value"],
   ["Her loop diuretic for edema",
    "Diuretics cause a saline-responsive metabolic alkalosis with a high bicarbonate. Her bicarbonate is 15. Tell: a diuretic raises the bicarbonate; hers has fallen.", "reversed direction or value"]],
  CS(45, 46, 53), "avoid", "avoid"),

# ================================================================ metabolic alkalosis (s51-55)
V(T_MALK, IO_D,
  "A 46-year-old woman has weakness. Her blood pressure is normal, and she reports no vomiting and no medicines. " + ABG("7.48", "47", "34")
  + " The cause of her disorder is unclear. Which test best narrows the list of causes?",
  [["Urine chloride",
    "Correct. A pH of 7.48 with a bicarbonate of 34 is a metabolic alkalosis. When its cause is unclear, measuring urine chloride separates the saline-responsive causes (low urine chloride) from the saline-unresponsive causes (high urine chloride)."],
   ["Serum anion gap",
    "The anion gap sorts the causes of metabolic acidosis into raised-gap and normal-gap lists. Her pH is 7.48, an alkalosis. Tell: alkalosis is sorted by urine chloride.", "adjacent fact"],
   ["Serum albumin",
    "Albumin is used to correct the anion gap in acidosis. It does not separate the causes of metabolic alkalosis. Tell: albumin adjusts the gap; urine chloride sorts alkalosis.", "adjacent fact"],
   ["Urine bicarbonate",
    "Metabolic alkalosis is sorted by urine chloride, not urine bicarbonate, so urine bicarbonate is not the test that splits the causes of alkalosis. Tell: the sorting test is urine chloride, which is low or high.", "confused mechanism or drug class"]],
  CS(51, 54), "initial test", "test"),

V(T_MALK, IO_F,
  "A 52-year-old man has weakness and a blood pressure of 168/102 mm Hg. " + ABG("7.49", "48", "35")
  + " His potassium is 2.9 mEq/L " + K + ", and his urine chloride is 60 mEq/L. How should these results be interpreted?",
  [["Saline-unresponsive, hypertensive alkalosis",
    "Correct. A pH of 7.49 with a bicarbonate of 35 is a metabolic alkalosis. Urine chloride is higher in saline-unresponsive types (above 40), and his is 60. With hypertension, the group includes primary aldosteronism and mineralocorticoids."],
   ["Saline-responsive, volume-contracted alkalosis",
    "Saline-responsive alkalosis, as with vomiting or diuretics, has a low urine chloride, below 25. His is 60. Tell: a high urine chloride rules out the saline-responsive group.", "ruled out by a stated finding"],
   ["Saline-unresponsive, normotensive alkalosis",
    "The normotensive saline-unresponsive group includes severe potassium depletion, but his blood pressure is 168/102. Tell: once the urine chloride is high, the blood pressure splits the group, and his is high.", "ruled out by a stated finding"],
   ["Respiratory acidosis, renally compensated",
    "Respiratory acidosis has a pH below 7.35. His pH is 7.49, so the carbon dioxide of 48 is compensation for the alkalosis. Tell: the pH names the primary disorder.", "competing diagnosis"]],
  CS(51, 52, 53), "test finding", "test"),

V(T_MALK, IO_D,
  "A 39-year-old man has had nasogastric suction for 4 days after bowel surgery and has dry mucous membranes. " + ABG("7.50", "48", "36")
  + " His potassium is 3.0 mEq/L " + K + ", and his urine chloride is low. Along with stopping the suction, which treatment is most appropriate?",
  [["Saline with potassium replacement",
    "Correct. Gastric suction causes a saline-responsive metabolic alkalosis, confirmed by the low urine chloride, and he is volume depleted. Treatment is to stop contributors such as suction and treat the fluid and potassium deficits."],
   ["Fluid restriction with a diuretic",
    "He is already volume depleted, and diuretics are themselves a cause of saline-responsive alkalosis. Tell: a low urine chloride with dry mucous membranes calls for fluid, not fluid removal.", "reversed direction or value"],
   ["A hydrocortisone infusion",
    "Corticosteroids are a contributor to metabolic alkalosis and are among the drugs to stop, and hydrocortisone has more mineralocorticoid activity than prednisone. Tell: steroids worsen this alkalosis.", "reversed direction or value"],
   ["Ventilation to lower his carbon dioxide",
    "His carbon dioxide of 48 is compensation for the alkalosis. Lowering it would raise the pH further. Tell: treat the metabolic cause, not the compensation.", "wrong stage or severity"]],
  CS(53, 54), "first-line", "treatment"),

V(T_MALK, IO_D,
  "A 61-year-old woman takes hydrocortisone for a chronic inflammatory condition and must stay on a corticosteroid. She has a metabolic alkalosis. "
  + ABG("7.49", "47", "34") + " Which change to her corticosteroid is most appropriate?",
  [["Switch to prednisone",
    "Correct. If a patient with metabolic alkalosis requires corticosteroids, lower the dose or change to one with less mineralocorticoid activity: prednisone or methylprednisolone rather than cortisone or hydrocortisone."],
   ["Keep hydrocortisone at the same dose",
    "Hydrocortisone has more mineralocorticoid activity, which drives the alkalosis, so leaving it unchanged keeps the contributor in place. Tell: change the steroid or lower the dose.", "wrong stage or severity"],
   ["Switch to cortisone",
    "Cortisone sits with hydrocortisone on the side to move away from, with more mineralocorticoid activity. Tell: the preferred agents are prednisone and methylprednisolone.", "adjacent fact"],
   ["Raise the hydrocortisone dose",
    "A higher dose adds mineralocorticoid effect and worsens the alkalosis; the advice is to decrease the dose if possible. Tell: dose goes down, not up.", "reversed direction or value"]],
  CS(53, 54, 55), "agent/regimen", "treatment"),

V(T_MALK, IO_D,
  "A 33-year-old woman with self-induced vomiting has a metabolic alkalosis. " + ABG("7.51", "47", "36")
  + " Her potassium is 2.9 mEq/L " + K + ". Her vomiting has stopped and saline has been started. Which approach to her potassium should be avoided?",
  [["Replacing well beyond the measured deficit",
    "Correct. Much of the low potassium in alkalosis is a shift into cells. Potassium deficits are treated if needed, but overcorrection is to be avoided, because as the alkalosis corrects potassium shifts back out of the cells."],
   ["Replacing potassium alongside her fluids",
    "Treating fluid and potassium deficits is part of treating saline-responsive metabolic alkalosis, and her potassium of 2.9 is low. Tell: replacement is right; overshooting is the danger.", "reversed direction or value"],
   ["Rechecking potassium as the alkalosis corrects",
    "Rechecking is how overcorrection is avoided, since potassium moves back out of cells as the pH falls. Tell: monitoring is the safe practice, not the one to avoid.", "reversed direction or value"],
   ["Treating the cause of her vomiting",
    "Treating the underlying condition is the first step for metabolic alkalosis. Tell: the item to avoid is excess potassium, not care of the cause.", "reversed direction or value"]],
  CS(5, 54), "avoid", "avoid"),

V(T_MALK, IO_D,
  "A 77-year-old woman takes a thiazide for hypertension and has had 3 days of weakness. Her blood pressure is 126/74 mm Hg. " + ABG("7.47", "47", "33")
  + " Her potassium is 3.1 mEq/L " + K + ", and her urine chloride is low. Which is the most appropriate next step?",
  [["Stop the thiazide; give fluid and potassium",
    "Correct. A pH of 7.47 with a bicarbonate of 33 and a low urine chloride is a saline-responsive metabolic alkalosis, and diuretics are a cause. Treatment stops the contributor and treats the fluid and potassium deficits, without overcorrecting."],
   ["Add a loop diuretic to the thiazide therapy",
    "Diuretics cause saline-responsive alkalosis, so adding a second one worsens both the alkalosis and the volume loss. Tell: discontinue the diuretic; do not add another.", "reversed direction or value"],
   ["Start hydrocortisone and continue the thiazide",
    "Corticosteroids, particularly hydrocortisone, add mineralocorticoid effect and are among the contributors to stop, and the thiazide is the cause. Tell: both choices push the bicarbonate higher.", "reversed direction or value"],
   ["Restrict her salt and fluid intake for now",
    "A low urine chloride marks the saline-responsive group, which is volume contracted. Restricting salt and fluid deepens that. Tell: saline-responsive means give fluid.", "reversed direction or value"]],
  CS(51, 53, 54), "first-line", "next step"),

V(T_MALK, IO_F,
  "A 71-year-old man with weeks of vomiting from a gastric outlet obstruction has muscle weakness and hyporeflexia (diminished reflexes). "
  + ABG("7.50", "48", "36") + " His potassium is 2.8 mEq/L " + K + ". Which acid-base disorder is present?",
  [["Metabolic alkalosis with hypokalemia",
    "Correct. A pH of 7.50 with a bicarbonate of 36 is a metabolic alkalosis; vomiting causes it by loss of gastric acid. The carbon dioxide of 48 is compensation. Hypokalemia, partly a shift into cells, causes the weakness and hyporeflexia."],
   ["Respiratory acidosis from muscle weakness",
    "Respiratory acidosis has a pH below 7.35. His pH is 7.50, so the carbon dioxide of 48 is compensation, not a failure of breathing. Tell: always read the pH first.", "ruled out by a stated finding"],
   ["Metabolic acidosis with hyperkalemia",
    "Metabolic acidosis has a low pH and low bicarbonate, and it shifts potassium out of cells. His pH is 7.50, his bicarbonate 36 and his potassium 2.8. Tell: every value points the other way.", "reversed direction or value"],
   ["Respiratory alkalosis with low potassium",
    "Respiratory alkalosis has a low carbon dioxide. His is 48, and his bicarbonate of 36 drives the pH. Tell: in an alkalemic patient, a high bicarbonate means the problem is metabolic.", "ruled out by a stated finding"]],
  CS(51, 52, 53, 58), "manifestation", "diagnosis"),

# ================================================================ step by step (s56-59)
V(T_STEPS, IO_F,
  "A 58-year-old man is brought in confused with a low blood pressure, and the cause of his critical illness is not yet clear. Which initial testing best characterizes his acid-base status?",
  [["Arterial gas and electrolytes drawn together",
    "Correct. The first step is to obtain an arterial blood gas and electrolytes simultaneously, so the bicarbonate on each can be compared to verify accuracy and the anion gap can be calculated. In a critically ill patient the acid-base type can assist the diagnosis."],
   ["Arterial gas now, electrolytes the next day",
    "Drawing them a day apart loses the comparison of the two bicarbonate values and makes the anion gap unreliable. Tell: the gas and electrolytes are drawn at the same time.", "wrong stage or severity"],
   ["Electrolytes alone, adding a gas if abnormal",
    "The anion gap can be abnormal even when sodium, chloride and bicarbonate are normal, and electrolytes alone give no pH or carbon dioxide. Tell: the disorder cannot be named without the gas.", "wrong stage or severity"],
   ["Urine chloride before any blood testing",
    "Urine chloride is used when a metabolic alkalosis has an unclear cause, after the blood gas has named the disorder. Tell: the blood gas and electrolytes come first.", "wrong stage or severity"]],
  CS(9, 26, 56), "initial test", "test"),

V(T_STEPS, IO_F,
  "A 49-year-old woman is evaluated for fatigue. Her arterial blood gas shows " + gas("7.40", "40", "24")
  + ". A serum panel drawn at the same moment shows a bicarbonate of 14 mEq/L " + HCO3 + ". Which is the most appropriate next step?",
  [["Recheck both, as the bicarbonates disagree",
    "Correct. The bicarbonate on the blood gas and on the electrolytes is compared to verify accuracy before any further step. A difference of 10 mEq/L between samples drawn together means one result is unreliable, so neither can carry the analysis yet."],
   ["Use the gas bicarbonate and proceed",
    "Choosing one value skips the accuracy check, and the analysis could rest on the wrong number. Tell: two simultaneous bicarbonates that disagree are a warning to verify, not a choice to make.", "wrong stage or severity"],
   ["Use the panel bicarbonate and proceed",
    "A bicarbonate of 14 with a pH of 7.40 and a carbon dioxide of 40 does not fit, and taking it on trust skips the accuracy check. Tell: verify first when the two values disagree.", "wrong stage or severity"],
   ["Average the two values and proceed",
    "An average of an accurate and an inaccurate value is still inaccurate. The comparison exists to catch a bad result. Tell: disagreeing values are rechecked, not blended.", "common lay belief"]],
  CS(56, 57), "initial test", "next step"),

V(T_STEPS, IO_F,
  "A 57-year-old man with type 2 diabetes and an anxiety disorder is drowsy after taking extra doses of a sedating medicine. "
  + ABG("7.30", "55", "26") + " Which primary disorder do these values show?",
  [["Respiratory acidosis",
    "Correct. A pH below 7.35 is an acidosis. The carbon dioxide of 55 is above 45, matching the low pH, so the primary disorder is respiratory acidosis; the bicarbonate of 26 shows the small acute renal response. Sedatives depress ventilation."],
   ["Metabolic acidosis",
    "Metabolic acidosis needs a low bicarbonate, below 22. His bicarbonate is 26. Tell: in an acidosis, a high carbon dioxide points to the respiratory side.", "ruled out by a stated finding"],
   ["Respiratory alkalosis",
    "Respiratory alkalosis has a pH above 7.45 and a low carbon dioxide, as with anxiety. His pH is 7.30 and his carbon dioxide 55. Tell: his anxiety disorder is a distractor; the gas shows the opposite.", "reversed direction or value"],
   ["Metabolic alkalosis",
    "Metabolic alkalosis has a pH above 7.45 with a high bicarbonate. His pH is 7.30. Tell: start with the pH; an acidemic pH rules out both alkaloses.", "reversed direction or value"]],
  CS(11, 32, 58, 59), "test finding", "diagnosis"),
]
