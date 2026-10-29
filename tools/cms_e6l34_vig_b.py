# -*- coding: utf-8 -*-
"""Lecture 34 vignette pool B -- Acid-Base Part I: finding the cause in a patient with several conditions,
calculating the anion gap, and choosing (or avoiding) a treatment (slides 8, 26-58).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

Exam 5 style (Jaxon, 2026-10-29): patients carry several conditions or medicines and the blood gas decides
which one explains it; each wrong choice says what that condition WOULD do to the gas. Every blood value
carries its range; urine chloride is described as low or high, never as a bare number, because it has no
fixed reference range. Explanations follow EXPLAIN_DEEP.md. No patient or value comes from the lecturer's
board cases.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l34_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


CAUSE = "Find the cause"
GAP = "Calculate the anion gap"
TREAT = "Treat the disorder"

ALB = "(normal 3.5 to 5.0 g/dL)"

QUESTIONS = [

# ---------------------------------------------------------------- which of several conditions explains it?
V(CAUSE, IO_D,
  "A 67-year-old man has hypertension treated with a thiazide diuretic, stable chronic obstructive pulmonary disease, and osteoarthritis for which he takes aspirin. He feels weak. Arterial blood gas: " + gas("7.48", "46", "33") + "; potassium 3.1 mEq/L " + K + "; urine chloride is low. Which part of his history best accounts for this blood gas?",
  [["His thiazide diuretic",
    "Correct. High pH with a high bicarbonate is metabolic alkalosis, and the low urine chloride marks the saline-responsive type. Diuretic therapy is a saline-responsive cause, and the low potassium and weakness fit; the carbon dioxide of 46 is the expected compensation."],
   ["His chronic lung disease",
    "His lung disease would cause respiratory acidosis: a high carbon dioxide driving a low pH. His pH is 7.48, alkalemic, and the carbon dioxide of 46 is only the small rise that compensates a metabolic alkalosis. Tell: his pH is alkalemic, so the primary disorder is not an acidosis.", "competing diagnosis"],
   ["His aspirin",
    "Salicylates (aspirin) are a listed toxic cause of respiratory alkalosis, a primary fall in carbon dioxide. His carbon dioxide is 46 and his bicarbonate 33, so the primary change is metabolic. Tell: a salicylate alkalosis has a low carbon dioxide, not a high bicarbonate.", "ruled out by a stated finding"],
   ["Primary aldosteronism",
    "Primary aldosteronism is a saline-unresponsive, hypertensive cause, and saline-unresponsive alkalosis has a high urine chloride, above 40 mEq/L. His urine chloride is low, which points to a saline-responsive cause such as his diuretic. Tell: low urine chloride means saline responsive.", "ruled out by a stated finding"]],
  Cs(33, 39, 41, 42, 43, 59), "etiology", "etiology"),

V(CAUSE, IO_D,
  "A 58-year-old woman has type 2 diabetes treated with metformin, hypertension treated with a thiazide diuretic, glaucoma treated with an oral carbonic anhydrase inhibitor, and heartburn for which she takes a calcium carbonate antacid. Her kidney function has worsened, and serum ketones are negative. Arterial blood gas: " + gas("7.26", "23", "10") + "; sodium 139 mEq/L " + NA + ", chloride 101 mEq/L " + CL + ". Which of her medicines best accounts for this blood gas?",
  [["Metformin",
    "Correct. Low pH with a low bicarbonate is metabolic acidosis, and the gap is 139 - (101 + 10) = 28, above 9 to 15: elevated. Metformin is one of the elevated-gap causes (the M of the mnemonic), and negative ketones argue against ketoacidosis."],
   ["Her thiazide diuretic",
    "Diuretic therapy causes saline-responsive metabolic alkalosis, with a high pH and a high bicarbonate. She has a pH of 7.26 and a bicarbonate of 10, the opposite. Tell: a diuretic raises the bicarbonate; hers has fallen.", "reversed direction or value"],
   ["Her calcium carbonate antacid",
    "Antacids are a cause of saline-responsive metabolic alkalosis, which would raise both her pH and her bicarbonate. Her values are both low. Tell: antacid alkalosis shows a bicarbonate above 26, not 10.", "reversed direction or value"],
   ["A carbonic anhydrase inhibitor",
    "A carbonic anhydrase inhibitor causes a normal-gap metabolic acidosis, with a gap within 9 to 15 and a high chloride. Her gap is 28 and her chloride normal, so an elevated-gap cause is needed. Tell: calculate the gap before choosing between the two lists.", "competing diagnosis"]],
  C(55), "etiology", "etiology"),

V(CAUSE, IO_D,
  "A 34-year-old woman has glaucoma treated with an oral carbonic anhydrase inhibitor, type 2 diabetes treated with metformin, and daily aspirin use for headaches. Arterial blood gas: " + gas("7.32", "30", "15") + "; sodium 140 mEq/L " + NA + ", chloride 115 mEq/L " + CL + ". Which of her medicines best accounts for this blood gas?",
  [["The carbonic anhydrase inhibitor",
    "Correct. Low pH and low bicarbonate make a metabolic acidosis; the gap is 140 - (115 + 15) = 10, within 9 to 15, with a high chloride: a normal-gap, hyperchloremic acidosis. Carbonic anhydrase inhibitors are on the normal-gap list (loss of bicarbonate)."],
   ["Metformin",
    "Metformin causes an elevated-gap acidosis, above 15. Her gap is 140 - (115 + 15) = 10, normal, and her chloride is high, the pattern of the normal-gap list. Tell: metformin sits in the mnemonic for an increased gap.", "competing diagnosis"],
   ["Aspirin",
    "Salicylates are on the elevated-gap list, and an elevated-gap acidosis is normochloremic with a gap above 15. Her gap is 10 with a high chloride. Tell: a normal gap with a high chloride points to the normal-gap list, not aspirin.", "competing diagnosis"],
   ["A respiratory cause, not a medicine",
    "A respiratory acidosis needs a high carbon dioxide; hers is 30, low, and her bicarbonate of 15 is what matches the pH. The low carbon dioxide is compensation, as the Winter formula (1.5 x 15 + 8 = 30.5) predicts.", "ruled out by a stated finding"]],
  Cs(47, 52, 55, 56, 58), "etiology", "etiology"),

V(CAUSE, IO_D,
  "A 52-year-old man has hypertension that is hard to control and muscle weakness. He takes no diuretics, has not vomited, and eats a bag of black licorice every day. Arterial blood gas: " + gas("7.47", "47", "33") + "; potassium 3.0 mEq/L " + K + "; urine chloride is high. Which part of his history best accounts for this blood gas?",
  [["His daily black licorice",
    "Correct. High pH with a high bicarbonate is metabolic alkalosis; the high urine chloride makes it saline unresponsive, and his high blood pressure puts it in the hypertensive group, which lists licorice. Low potassium with weakness fits."],
   ["Hidden vomiting",
    "Vomiting (loss of hydrochloric acid) causes a saline-responsive alkalosis with a low urine chloride, below 25 mEq/L, and volume contraction. His urine chloride is high and he is hypertensive. Tell: vomiting-type alkalosis has a low urine chloride.", "ruled out by a stated finding"],
   ["Antacid use",
    "Antacids cause a saline-responsive alkalosis, with a low urine chloride. His is high, and he is hypertensive rather than volume contracted. Tell: a high urine chloride steers you to the saline-unresponsive list.", "ruled out by a stated finding"],
   ["Anxiety with hyperventilation",
    "Hyperventilation causes respiratory alkalosis, with a carbon dioxide below 36. His is 47 and his bicarbonate 33, so the primary change is metabolic. Tell: respiratory alkalosis lowers the carbon dioxide; his is raised as compensation.", "ruled out by a stated finding"]],
  C(43), "etiology", "etiology"),

V(CAUSE, IO_D,
  "A 72-year-old man with severe chronic obstructive pulmonary disease was intubated with a carbon dioxide of 78 mm Hg " + PCO2 + ", and the ventilator brought it to 38 within a few hours. He has had no vomiting, nasogastric suction, diuretics or antacids. The next morning: " + gas("7.55", "38", "32") + ". What best explains his alkalemia?",
  [["Post-hypercapnic metabolic alkalosis",
    "Correct. His kidneys had retained bicarbonate for his chronic hypercapnia; when the carbon dioxide was lowered quickly, that bicarbonate of 32 was left unopposed, a post-hypercapnic metabolic alkalosis. This is why rapid, aggressive carbon dioxide reduction is avoided in chronic respiratory acidosis."],
   ["Acute respiratory alkalosis",
    "Respiratory alkalosis needs a low carbon dioxide, below 36. His is 38, within range; the high bicarbonate is what drives his pH up. Tell: in respiratory alkalosis the carbon dioxide, not the bicarbonate, is the abnormal value.", "ruled out by a stated finding"],
   ["Renal compensation that overshot",
    "Compensation never corrects the pH beyond normal, so an overshoot cannot explain a pH of 7.55. Here the compensating bicarbonate was stranded when the carbon dioxide it offset was removed. Tell: compensation alone stops short of 7.40.", "confused mechanism or drug class"],
   ["Worsening chronic respiratory acidosis",
    "Respiratory acidosis gives a low pH with a high carbon dioxide. His pH is 7.55 and his carbon dioxide 38, both pointing away from acidosis. Tell: acidosis lies below 7.35, and he is alkalemic.", "reversed direction or value"]],
  C(28), "complication", "complication"),

V(CAUSE, IO_D,
  "A 61-year-old man has had progressive limb weakness with muscle twitching for three years from amyotrophic lateral sclerosis; he also has hypertension and gout. He is drowsy in the mornings. Arterial blood gas: " + gas("7.34", "56", "30") + ". Which process best accounts for this blood gas?",
  [["Chronic hypoventilation from muscle weakness",
    "Correct. A high carbon dioxide of 56 matching a low pH is respiratory acidosis, and the bicarbonate of 30 (about 3.5 per 10 mm Hg) shows chronic renal compensation. Neuromuscular disease such as amyotrophic lateral sclerosis is a listed chronic cause, and morning drowsiness fits hypercapnia."],
   ["Acute airway obstruction",
    "Acute obstruction causes acute respiratory acidosis, where bicarbonate rises only about 1 per 10 mm Hg, to about 26. His 30 shows days of renal compensation, matching a three-year illness. Tell: an acute cause leaves the bicarbonate near normal.", "wrong stage or severity"],
   ["Hyperventilation from anxiety",
    "Hyperventilation lowers carbon dioxide below 36 and raises the pH. His carbon dioxide is 56, the opposite of hyperventilation. Tell: anxiety gives respiratory alkalosis, a low carbon dioxide.", "reversed direction or value"],
   ["Bicarbonate loss from diarrhea",
    "Diarrhea causes a normal-gap metabolic acidosis with a low bicarbonate. His bicarbonate is 30, high, and the high carbon dioxide drives the pH. Tell: in metabolic acidosis the bicarbonate falls below 22.", "reversed direction or value"]],
  C(27), "etiology", "etiology"),

V(CAUSE, IO_D,
  "A 74-year-old woman with osteoarthritis has been taking large amounts of aspirin; she also has hypertension treated with a thiazide diuretic and type 2 diabetes treated with metformin. She is breathing fast. Arterial blood gas: " + gas("7.52", "28", "22") + ". Which of her medicines best accounts for this blood gas?",
  [["Aspirin",
    "Correct. High pH with a low carbon dioxide of 28 is respiratory alkalosis, and her bicarbonate of 22 has barely fallen. Salicylates are a listed toxic cause of hyperventilation, and her fast breathing fits."],
   ["Her thiazide diuretic",
    "Diuretics cause a metabolic alkalosis, with a high bicarbonate above 26 and a mildly raised carbon dioxide. Her bicarbonate is 22 and her carbon dioxide 28. Tell: diuretic alkalosis shows up in the bicarbonate, not as a low carbon dioxide.", "ruled out by a stated finding"],
   ["Metformin",
    "Metformin causes an elevated-gap metabolic acidosis, a low pH with a low bicarbonate. Her pH is 7.52, alkalemic. Tell: metformin pushes the pH below 7.35.", "reversed direction or value"],
   ["The combination of diuretic and metformin",
    "One drug causes metabolic alkalosis and the other metabolic acidosis; neither changes carbon dioxide first. Her primary change is the low carbon dioxide, which only hyperventilation explains. Tell: match the value that moved with the pH.", "confused mechanism or drug class"]],
  C(33), "etiology", "etiology"),

V(CAUSE, IO_D,
  "A 48-year-old woman five days after hip replacement develops sudden pleuritic chest pain and fast breathing. Arterial blood gas: " + gas("7.51", "30", "23") + "; partial pressure of oxygen 68 mm Hg " + PO2 + ". Which process best accounts for this blood gas?",
  [["Hyperventilation from a pulmonary embolism",
    "Correct. High pH with a low carbon dioxide of 30 is respiratory alkalosis, and her bicarbonate of 23 has barely moved (acute). Pulmonary embolism is a listed pulmonary cause; after surgery, with sudden pleuritic pain and a low oxygen, it fits."],
   ["Hypoventilation from opioid pain medicine",
    "Opioids depress breathing and raise carbon dioxide, causing respiratory acidosis with a low pH. Her carbon dioxide is 30 and her pH 7.51. Tell: hypoventilation pushes carbon dioxide above 44.", "reversed direction or value"],
   ["Diuretic-induced metabolic alkalosis",
    "A diuretic alkalosis has a high bicarbonate above 26; hers is 23, and her primary change is the low carbon dioxide. Tell: in metabolic alkalosis the carbon dioxide rises slightly, it does not fall.", "ruled out by a stated finding"],
   ["Obesity hypoventilation syndrome",
    "Obesity hypoventilation syndrome is a triad ending in chronic hypercapnia, a high carbon dioxide. Hers is low and her illness began suddenly. Tell: that syndrome causes chronic respiratory acidosis, not an acute alkalosis.", "reversed direction or value"]],
  C(34), "etiology", "etiology"),

# ---------------------------------------------------------------- the anion gap
V(GAP, IO_F,
  "A 36-year-old man is confused after drinking antifreeze (ethylene glycol). Sodium 140 mEq/L " + NA + ", potassium 4.0 mEq/L " + K + ", chloride 102 mEq/L " + CL + ", bicarbonate 8 mEq/L " + HCO3 + ". What is his anion gap?",
  [["30",
    "Correct. Anion gap = sodium - (chloride + bicarbonate) = 140 - (102 + 8) = 140 - 110 = 30, above the normal 9 to 15: an elevated-gap metabolic acidosis, fitting ethylene glycol, the E of the mnemonic."],
   ["34",
    "34 adds the potassium of 4.0 to the sodium. The formula used here is sodium minus (chloride plus bicarbonate), with no potassium: 140 - 110 = 30. Tell: potassium is not part of this anion gap formula.", "confused mechanism or drug class"],
   ["38",
    "38 is 140 - 102, leaving out the bicarbonate. Both measured anions are subtracted: 140 - (102 + 8) = 30. Tell: the gap subtracts chloride and bicarbonate.", "adjacent fact"],
   ["46",
    "46 adds the bicarbonate instead of subtracting it (140 - 102 + 8). The bicarbonate sits inside the parentheses with chloride: 140 - (102 + 8) = 30. Tell: check the sign of the bicarbonate.", "reversed direction or value"]],
  C(47), "test finding", "test") | {"ordered": True, "asc": [0, 1, 2, 3]},

V(GAP, IO_F,
  "A 63-year-old woman with septic shock has a lactate elevation. Sodium 132 mEq/L " + NA + ", potassium 4.0 mEq/L " + K + ", chloride 96 mEq/L " + CL + ", bicarbonate 12 mEq/L " + HCO3 + ". What is her anion gap?",
  [["24",
    "Correct. Anion gap = 132 - (96 + 12) = 132 - 108 = 24, above 9 to 15: elevated. Lactic acidosis, the L of the mnemonic, raises the gap through unmeasured anions."],
   ["28",
    "28 adds the potassium of 4.0 to the sodium. This formula uses sodium minus (chloride plus bicarbonate) only: 132 - 108 = 24. Tell: leave potassium out.", "confused mechanism or drug class"],
   ["36",
    "36 is 132 - 96, leaving out the bicarbonate. Both chloride and bicarbonate are subtracted: 132 - 108 = 24. Tell: two anions go inside the parentheses.", "adjacent fact"],
   ["48",
    "48 adds the bicarbonate instead of subtracting it (132 - 96 + 12). The correct result is 132 - (96 + 12) = 24. Tell: the parentheses make the bicarbonate a subtraction.", "reversed direction or value"]],
  C(47), "test finding", "test") | {"ordered": True, "asc": [0, 1, 2, 3]},

V(GAP, IO_F,
  "A 70-year-old woman with cirrhosis and an albumin of 1.9 g/dL " + ALB + " has a metabolic acidosis, a chloride of 110 mEq/L " + CL + " and an anion gap of 11 " + AG + ". Which finding most limits how much the normal gap can reassure you?",
  [["Her low serum albumin",
    "Correct. Albumin accounts for most of the normal anion gap, so hypoalbuminemia lowers the gap and can hide added unmeasured anions. A normal gap does not exclude a high-gap acidosis and should not override clinical concern."],
   ["Her metabolic acidosis itself",
    "The acidosis is what the gap is meant to sort; it does not distort the number. Hypoalbuminemia does, by removing the anion that makes up most of the normal gap. Tell: look for the listed errors: low albumin, sodium extremes, antibiotics.", "confused mechanism or drug class"],
   ["Her high chloride",
    "A high chloride marks a true normal-gap (hyperchloremic) acidosis; it is a finding, not an error in the gap. Her low albumin is the listed source of error. Tell: hypoalbuminemia sits on the error list; chloride does not.", "adjacent fact"],
   ["A low unmeasured cation level",
    "Losing unmeasured cations (calcium, magnesium, potassium) raises the gap, so it would make a normal value less likely, not falsely reassuring. Her low albumin lowers it. Tell: fewer cations raise the gap; less albumin lowers it.", "reversed direction or value"]],
  C(49), "test finding", "test"),

# ---------------------------------------------------------------- treat, avoid, educate
V(TREAT, IO_D,
  "A 22-year-old college athlete with gastroenteritis has vomited for three days and is dizzy on standing. Arterial blood gas: " + gas("7.51", "48", "37") + "; potassium 3.1 mEq/L " + K + "; urine chloride is low. In addition to treating the cause, which therapy is indicated?",
  [["Isotonic saline",
    "Correct. Vomiting (loss of hydrochloric acid) with orthostatic dizziness and a low urine chloride is saline-responsive metabolic alkalosis, a sign of extracellular volume contraction. Isotonic saline corrects that volume deficit."],
   ["A sodium bicarbonate infusion",
    "Bicarbonate is alkali; exogenous alkali is itself a cause of metabolic alkalosis and would push his pH of 7.51 higher. Isotonic saline treats the volume loss behind his alkalosis. Tell: adding alkali to an alkalemia raises the pH further.", "confused mechanism or drug class"],
   ["Paper bag rebreathing",
    "Breathing into a paper bag is not necessary even for hyperventilation: it fails to correct carbon dioxide and may decrease oxygen. His carbon dioxide is already raised as compensation. Tell: this is metabolic, and the fix is volume.", "confused mechanism or drug class"],
   ["Starting a thiazide diuretic",
    "Diuretic therapy is a cause of saline-responsive alkalosis, and diuretics are stopped, not started, in this disorder. He needs volume, not more volume loss. Tell: discontinuing diuretics is part of the treatment.", "reversed direction or value"]],
  Cs(35, 39, 42, 43, 44), "first-line", "treatment"),

V(TREAT, IO_D,
  "A 70-year-old man with hypertension treated with a thiazide diuretic is light-headed on standing. Arterial blood gas: " + gas("7.49", "46", "34") + "; potassium 3.2 mEq/L " + K + "; urine chloride is low. Along with isotonic saline, which medication change is indicated?",
  [["Stop the thiazide diuretic",
    "Correct. Low urine chloride and orthostatic symptoms mark a saline-responsive metabolic alkalosis, and diuretic therapy is a listed cause. Treatment is isotonic saline for the volume deficit and discontinuing the diuretic."],
   ["Add a second diuretic",
    "A second diuretic would deepen the volume contraction and the alkalosis; diuretics are discontinued in saline-responsive alkalosis. Tell: the drug causing the alkalosis is stopped, not doubled.", "reversed direction or value"],
   ["Start a mineralocorticoid",
    "Mineralocorticoids cause a hypertensive, saline-unresponsive metabolic alkalosis, so adding one would worsen his. Tell: mineralocorticoids are on the cause list, not the treatment list.", "reversed direction or value"],
   ["Start a calcium carbonate antacid",
    "Antacids are a cause of saline-responsive metabolic alkalosis, so starting one adds alkali to an alkalemia. Tell: antacid, diuretic and vomiting sit together on the cause list.", "reversed direction or value"]],
  C(44), "first-line", "treatment"),

V(TREAT, IO_D,
  "A 68-year-old woman with severe chronic obstructive pulmonary disease and a baseline carbon dioxide of 60 mm Hg " + PCO2 + " is admitted with pneumonia and placed on a ventilator. Which step should be avoided?",
  [["Rapid, aggressive lowering of her carbon dioxide",
    "Correct. Her kidneys have retained bicarbonate to offset chronic hypercapnia. Rapid, aggressive carbon dioxide reduction leaves that bicarbonate unopposed and causes a post-hypercapnic metabolic alkalosis, so chronic respiratory acidosis is corrected carefully."],
   ["Careful titration of her oxygen",
    "Careful oxygen titration is the recommended approach in chronic respiratory acidosis, not something to avoid. Tell: careful oxygen and slow carbon dioxide reduction go together in chronic disease.", "adjacent fact"],
   ["Treating her pneumonia",
    "Treating the underlying cause is the first rule for every acid-base disorder, and pneumonia is a listed cause of acute respiratory acidosis. Tell: the underlying cause is always treated.", "adjacent fact"],
   ["Checking her arterial blood gas",
    "Repeating the blood gas is how the carbon dioxide is followed as ventilation is adjusted; it carries no harm. Tell: the danger is how fast the carbon dioxide falls, not measuring it.", "adjacent fact"]],
  C(28), "avoid", "avoid"),

V(TREAT, IO_D,
  "A 24-year-old man with a panic attack is breathing fast, with perioral numbness and tingling hands. His roommate hands him a paper bag to breathe into. What is accurate education about the bag?",
  [["It is unnecessary and may lower his oxygen",
    "Correct. Breathing into a paper bag is not necessary for hyperventilation: it fails to correct the carbon dioxide and may decrease oxygen, and any benefit is placebo. Hyperventilation is usually self-limited, and the cause is treated."],
   ["It safely corrects his carbon dioxide",
    "The bag fails to correct carbon dioxide, and it may lower oxygen. Its effect is placebo. Tell: the paper bag fails on both counts, carbon dioxide and safety.", "common lay belief"],
   ["It is needed to prevent tetany",
    "Tetany can occur in severe respiratory alkalosis from low ionized calcium, but the bag does not prevent it; hyperventilation is usually self-limited. Tell: treat the cause, not the carbon dioxide with a bag.", "common lay belief"],
   ["It works by raising his bicarbonate",
    "Rebreathing does not act on bicarbonate; bicarbonate changes come from the kidneys over hours to days. The bag's benefit is placebo. Tell: bicarbonate is renal and slow; no bag reaches it.", "confused mechanism or drug class"]],
  C(35), "education", "education"),

V(TREAT, IO_D,
  "A 45-year-old man with Guillain-Barré syndrome has worsening weakness and shallow breathing. Arterial blood gas: " + gas("7.26", "58", "26") + ". What is the priority treatment for his acid-base disorder?",
  [["Restore adequate ventilation",
    "Correct. A high carbon dioxide with a low pH and a barely raised bicarbonate is acute respiratory acidosis, and Guillain-Barré syndrome is a listed neuromuscular cause. Acute respiratory acidosis is treated by restoring ventilation while the cause is treated."],
   ["Give sodium bicarbonate to raise the pH",
    "His acidosis comes from retained carbon dioxide, so the fix is ventilation; therapy aimed at the pH itself is reserved for an unsustainable pH (below 6.7), alongside the cause. His pH is 7.26. Tell: respiratory acidosis is treated by breathing, not by bicarbonate.", "wrong stage or severity"],
   ["Wait for renal compensation",
    "Renal compensation begins only after 6 to 12 hours, takes days, and never returns the pH to normal. His breathing is failing now. Tell: compensation alone never restores the pH; the disorder must be corrected.", "wrong stage or severity"],
   ["Careful oxygen titration alone",
    "Careful oxygen titration is the approach for chronic respiratory acidosis. His is acute (bicarbonate 26), and the priority is restoring ventilation. Tell: acute equals restore ventilation; chronic equals careful oxygen.", "wrong stage or severity"]],
  C(28), "first-line", "treatment"),

V(TREAT, IO_D,
  "A 40-year-old man who drank methanol is obtunded. Arterial blood gas: " + gas("6.65", "18", "2") + ". Besides treating the poisoning, what does this pH warrant?",
  [["Therapy to raise the serum pH",
    "Correct. A pH below 6.7 is unsustainable: it may cause cardiac hypocontractility and irritability, seizures and cerebral edema, and may warrant therapy to normalize the serum pH along with treatment of the underlying cause. His pH is 6.65."],
   ["No pH-directed therapy",
    "Treating the cause is the rule, but a pH below 6.7 is unsustainable and may warrant therapy to normalize it as well. His 6.65 is past that threshold. Tell: extreme pH values earn their own therapy.", "wrong stage or severity"],
   ["Paper bag rebreathing",
    "Rebreathing would raise carbon dioxide and lower the pH further; it is a placebo for hyperventilation. His low carbon dioxide is life-saving compensation. Tell: never blunt the breathing that compensates a metabolic acidosis.", "reversed direction or value"],
   ["Waiting for respiratory compensation",
    "He is already hyperventilating to a carbon dioxide of 18, and compensation never returns the pH to normal. At 6.65 the pH is unsustainable. Tell: compensation cannot rescue a pH below 6.7.", "wrong stage or severity"]],
  C(8), "escalation", "treatment"),

V(TREAT, IO_D,
  "A 47-year-old woman has a metabolic alkalosis with normal blood pressure; she denies vomiting, diuretics and antacids. Arterial blood gas: " + gas("7.48", "46", "32") + ". Which test separates the saline-responsive from the saline-unresponsive type?",
  [["Urine chloride",
    "Correct. Urine chloride differentiates the two types: it is low (below 25 mEq/L) in saline-responsive alkalosis and high (above 40 mEq/L) in saline-unresponsive alkalosis. Her history gives no obvious cause, so the test sorts the list."],
   ["Anion gap",
    "The anion gap sorts metabolic acidosis into normal and elevated gap; it does not type an alkalosis. Tell: anion gap for acidosis, urine chloride for alkalosis.", "adjacent fact"],
   ["Winter formula",
    "The Winter formula predicts the carbon dioxide in metabolic acidosis; it does not type an alkalosis. Tell: Winter checks compensation in acidosis only.", "adjacent fact"],
   ["Serum albumin",
    "Albumin matters for interpreting the anion gap, since low albumin lowers it. It does not split saline-responsive from unresponsive alkalosis. Tell: albumin goes with the gap.", "adjacent fact"]],
  C(41), "initial test", "test"),

V(TREAT, IO_D,
  "A 50-year-old man has a metabolic alkalosis with a high urine chloride. He takes no diuretics and has not vomited. Arterial blood gas: " + gas("7.48", "47", "34") + ". Which finding should be checked next to narrow the cause?",
  [["His blood pressure",
    "Correct. A high urine chloride (above 40 mEq/L) means saline-unresponsive alkalosis, whose causes split by blood pressure: normotensive (severe potassium depletion, hypoparathyroidism and hypercalcemia) or hypertensive (primary aldosteronism, mineralocorticoids, licorice)."],
   ["His anion gap",
    "The anion gap types a metabolic acidosis; it does not sort the causes of an alkalosis. Saline-unresponsive causes split by blood pressure. Tell: the gap belongs to acidosis.", "adjacent fact"],
   ["His urine chloride again",
    "His urine chloride is already high, placing him in the saline-unresponsive group; repeating it adds nothing. The next split is by blood pressure. Tell: urine chloride first, then blood pressure.", "wrong stage or severity"],
   ["His expected carbon dioxide by Winter",
    "The Winter formula checks compensation in metabolic acidosis. His disorder is an alkalosis, and the cause list splits by blood pressure. Tell: Winter is for acidosis.", "adjacent fact"]],
  C(43), "differential", "next step"),

V(TREAT, IO_D,
  "A 23-year-old woman with type 1 diabetes has diabetic ketoacidosis with Kussmaul respirations (deep, rapid breathing). Arterial blood gas: " + gas("7.19", "21", "8") + ". Which approach corrects her acid-base disorder?",
  [["Treat the underlying disorder",
    "Correct. Elevated-gap metabolic acidosis is treated by treating the underlying disorder; her pH of 7.19 is acidemic but not in the unsustainable range below 6.7. Her deep breathing is compensation and is left alone."],
   ["Slow her breathing to retain carbon dioxide",
    "Her deep, rapid breathing is the compensation lowering carbon dioxide; slowing it would drop her pH further. Tell: compensatory hyperventilation is protective in metabolic acidosis.", "reversed direction or value"],
   ["Paper bag rebreathing",
    "Rebreathing would blunt her compensation, and a paper bag is not necessary even in hyperventilation, with only a placebo effect. Her acidosis is metabolic, and the cause is treated. Tell: a bag does not treat a metabolic acidosis.", "reversed direction or value"],
   ["Bicarbonate until her pH is normal",
    "Therapy to normalize the pH may be warranted at unsustainable values (below 6.7), along with treatment of the cause. At 7.19 she needs the ketoacidosis treated. Tell: treat the cause; pH-directed therapy belongs to unsustainable values.", "wrong stage or severity"]],
  Cs(8, 35, 57, 58), "first-line", "treatment"),
]
