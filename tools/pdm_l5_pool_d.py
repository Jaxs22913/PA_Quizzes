# -*- coding: utf-8 -*-
# PDM I Lecture 5 -- pool D. Interpreting abnormal values (objective d), the
# renal/hepatic/metabolic lab patterns (e), electrolytes against acid-base (f),
# correlating chemistry with other tests (h), and fluid and electrolyte
# homeostasis (i).
#
# THE ANION GAP IS CALCULATED HERE, ON PURPOSE. Reynolds, 26 August: "you
# really quick and dirty, calculate your anion gap, and our normal range is
# 8 to 12", with the extended potassium formula and her own mnemonic. Her
# no-math rule does NOT cover this, and pdm_l5_partition.py asserts that these
# worked questions EXIST rather than that they are absent.
#
# CORRECTED SODIUM IS NOT CALCULATED. She does it with a calculator -- "UpToDate,
# MedCalc, eCalc". Questions ask what the correction is FOR and which direction
# it moves, never for the arithmetic.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "5. Chemistry Panels, Renal Fxn, Elytes.pptx"
def c(n): return f"{SRC}, Slide {n}"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"
def au(): return "Lecture recording, 26 August 2026"

IOD = "d — Interpret abnormal chemistry values and their clinical significance"
IOE = "e — Compare and contrast laboratory patterns seen in renal, hepatic and metabolic disorders"
IOF = "f — Explain the relationship between electrolyte abnormalities and acid-base disorders"
IOH = "h — Correlate chemistry findings with other diagnostic modalities when appropriate"
IOI = "i — Explain laboratory evaluation of fluid and electrolyte homeostasis"

POOL_D = [
 # ---- hepatic patterns (objective d/e) ----
 dict(topic="Hepatic patterns", io=IOE, slot="test finding",
   q="Which pattern defines hepatocellular liver injury?",
   opts=[
     ["The transaminases are raised out of proportion to alkaline phosphatase",
      "Correct — hepatocellular injury damages the liver cells themselves, releasing the transaminases out of proportion to alkaline phosphatase, which is the enzyme of the biliary epithelium."],
     ["Alkaline phosphatase is raised out of proportion to the transaminases",
      "That is the cholestatic pattern."],
     ["Bilirubin is raised while the enzymes stay normal",
      "That is isolated hyperbilirubinemia."],
     ["Both the transaminases and alkaline phosphatase are raised together",
      "That is the mixed pattern."]],
   c=0, cite=c(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="test finding",
   q="Which pattern defines cholestatic liver injury?",
   opts=[
     ["Alkaline phosphatase is raised out of proportion to the transaminases",
      "Correct — cholestatic injury obstructs bile flow, so the biliary enzyme alkaline phosphatase rises out of proportion to the transaminases released from hepatocytes."],
     ["The transaminases are raised out of proportion to alkaline phosphatase",
      "That is the hepatocellular pattern."],
     ["Albumin is low with a prolonged prothrombin time",
      "Those indicate advanced disease rather than defining cholestasis."],
     ["Bilirubin is raised while the enzymes stay normal",
      "That is isolated hyperbilirubinemia."]],
   c=0, cite=c(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="What causes a cholestatic pattern?",
   opts=[
     ["Bile duct obstruction, gallstones, and primary biliary cholangitis",
      "Correct — bile duct obstruction, gallstones and primary biliary cholangitis raise alkaline phosphatase out of proportion to the transaminases."],
     ["Viral hepatitis, alcohol, and ischemia",
      "Those are given for the hepatocellular pattern."],
     ["Gilbert syndrome and hemolysis",
      "Those are given for isolated hyperbilirubinemia."],
     ["Heart failure and sepsis",
      "Heart failure and sepsis are not the cholestatic causes, which are bile duct obstruction, gallstones and primary biliary cholangitis."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="What are the two causes of isolated hyperbilirubinemia?",
   opts=[
     ["Gilbert syndrome and hemolysis",
      "Correct — Gilbert syndrome and hemolysis raise the bilirubin while the enzymes stay normal, which is the isolated hyperbilirubinemia pattern."],
     ["Gallstones and primary biliary cholangitis",
      "Those produce a cholestatic pattern."],
     ["Viral hepatitis and drug injury",
      "Those produce a hepatocellular pattern."],
     ["Alcohol and fatty liver disease",
      "Those also sit under the hepatocellular heading."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="test finding",
   q="A ratio of aspartate aminotransferase to alanine transaminase above two to one suggests which cause?",
   opts=[
     ["Alcoholic liver disease",
      "Correct — a ratio above two to one is characteristic of alcoholic liver disease, where pyridoxine deficiency limits alanine transaminase production more than aspartate aminotransferase."],
     ["Viral hepatitis",
      "Viral hepatitis does not characteristically produce this ratio."],
     ["Biliary obstruction",
      "That raises alkaline phosphatase preferentially."],
     ["Ischemic hepatitis",
      "Ischemia is one of the causes of transaminases in the thousands."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="Transaminases in the thousands narrow the cause to which three possibilities?",
   opts=[
     ["Viral hepatitis, ischemia, and toxins",
      "Correct — transaminases in the thousands require massive hepatocyte necrosis, which in practice means viral hepatitis, ischemia, or a toxin such as paracetamol."],
     ["Alcohol, fatty liver disease, and gallstones",
      "None of these characteristically reaches the thousands."],
     ["Gilbert syndrome, hemolysis, and biliary obstruction",
      "These raise bilirubin or alkaline phosphatase rather than the transaminases."],
     ["Heart failure, sepsis, and pancreatitis",
      "Heart failure, sepsis and pancreatitis raise the transaminases modestly at most; none characteristically reaches the thousands."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="A raised aspartate aminotransferase with a normal alanine transaminase points away from the liver and towards what?",
   opts=[
     ["Cardiac or skeletal muscle",
      "Correct — aspartate aminotransferase is present in cardiac and skeletal muscle as well as liver, so a rise with a normal alanine transaminase, which is liver-specific, points to a muscle source."],
     ["The biliary tree",
      "That would raise alkaline phosphatase."],
     ["The kidney",
      "Kidney disease is read from creatinine and the filtration rate."],
     ["Red blood cell breakdown",
      "That raises bilirubin."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOD, slot="test finding",
   q="How is the magnitude of a transaminase rise banded?",
   opts=[
     ["Mild under five times, moderate five to fifteen times, and severe over fifteen times the upper limit",
      "Correct — a rise under five times the upper limit is mild, five to fifteen times is moderate, and over fifteen times is severe."],
     ["Mild under two times, moderate two to ten times, and severe over ten times the upper limit",
      "Two and ten times are not the thresholds; the bands fall at five and fifteen times the upper limit of normal."],
     ["Mild under ten times, moderate ten to fifty times, and severe over fifty times the upper limit",
      "Ten and fifty times are far too high; severe disease begins at fifteen times the upper limit, not fifty."],
     ["Mild under three times, moderate three to twenty times, and severe over twenty times the upper limit",
      "Three and twenty times are close but wrong; the bands fall at five and fifteen times the upper limit of normal."]],
   c=0, cite=cn(17)),

 # ---- renal and metabolic patterns ----
 dict(topic="Renal pattern", io=IOE, slot="test finding",
   q="Which laboratory pattern is given for a renal disorder?",
   opts=[
     ["Raised urea nitrogen and creatinine with a fallen filtration rate, and possibly a raised potassium and a metabolic acidosis",
      "Correct — failing glomerular filtration retains urea nitrogen and creatinine, and the same failure impairs potassium excretion and acid handling, giving a raised potassium and a metabolic acidosis."],
     ["Raised transaminases with a low albumin and a prolonged prothrombin time",
      "That is the hepatic row."],
     ["A raised glucose with a low bicarbonate and a raised anion gap",
      "That is the metabolic row, and describes ketoacidosis."],
     ["A low sodium with a high bicarbonate and a low chloride",
      "That is the vomiting case rather than the renal pattern."]],
   c=0, cite=c(19)),

 dict(topic="Renal pattern", io=IOE, slot="test finding",
   q="Besides urea nitrogen and creatinine, what else appears in the renal pattern?",
   opts=[
     ["A raised phosphate, a lowered calcium, and albuminuria",
      "Correct — the renal pattern adds a raised potassium and phosphate, a lowered calcium, metabolic acidosis and albuminuria to the rising urea nitrogen and creatinine."],
     ["A raised calcium, a lowered phosphate, and glycosuria",
      "The calcium and phosphate directions are reversed and glycosuria is not listed."],
     ["A raised albumin with a lowered total protein",
      "Albuminuria is protein in the urine, not a raised serum albumin."],
     ["A raised bilirubin with a lowered alkaline phosphatase",
      "Those belong to the hepatic row."]],
   c=0, cite=c(19)),

 dict(topic="Metabolic pattern", io=IOE, slot="test finding",
   q="Which laboratory pattern is given for diabetic ketoacidosis?",
   opts=[
     ["A raised glucose, a lowered bicarbonate, a raised anion gap, and a low pH",
      "Correct — insulin deficiency raises glucose and drives ketone production; the ketoacids consume bicarbonate and are unmeasured anions, so the gap widens and the pH falls."],
     ["A lowered glucose, a raised bicarbonate, and a normal anion gap",
      "Every direction here is reversed."],
     ["A raised glucose with a raised bicarbonate and a high pH",
      "Ketoacidosis is an acidosis, so bicarbonate falls and pH drops."],
     ["A normal glucose with a lowered bicarbonate and a normal gap",
      "The glucose is raised in this disorder."]],
   c=0, cite=c(19)),

 dict(topic="Metabolic pattern", io=IOE, slot="test finding",
   q="In diabetic ketoacidosis the serum potassium may be raised. What is true of total-body potassium?",
   opts=[
     ["Total-body potassium is depleted despite the raised serum level",
      "Correct — acidosis and insulin deficiency drive potassium out of cells into the serum while osmotic diuresis excretes it, so the measured level looks normal or high over a large total-body deficit."],
     ["Total-body potassium is also raised, matching the serum level",
      "Serum and total body disagree here; the serum level is propped up by a transcellular shift while the total store is being lost in the urine."],
     ["Total-body potassium is normal and only the serum is affected",
      "Total-body potassium is not normal; osmotic diuresis has depleted it, which is why replacement is needed once insulin is started."],
     ["Total-body potassium cannot be inferred from any measurement",
      "It can be inferred; the osmotic diuresis of ketoacidosis reliably depletes total-body potassium whatever the serum value shows."]],
   c=0, cite=c(19)),

 dict(topic="Overlap syndromes", io=IOE, slot="differential",
   q="Which syndrome shows liver and kidney failure at once?",
   opts=[
     ["Hepatorenal syndrome",
      "Correct — hepatorenal syndrome shows both liver and kidney failure, much as ketoacidosis produces electrolyte and renal derangements at the same time."],
     ["Cardiorenal syndrome",
      "That is also named, but as a cardiac and renal overlap."],
     ["Diabetic ketoacidosis",
      "That produces electrolyte and renal derangements, not liver failure."],
     ["Nephrotic syndrome",
      "Nephrotic syndrome is not the overlap; hepatorenal syndrome shows liver and kidney failure together, and cardiorenal syndrome is the other overlap pattern."]],
   c=0, cite=c(19)),

 dict(topic="Reading a panel", io=IOD, slot="initial test",
   q="In the stepwise approach to an abnormal comprehensive metabolic panel, which step comes first?",
   opts=[
     ["The electrolytes and acid-base group, then calculate the anion gap",
      "Correct — the stepwise read starts with sodium, potassium, chloride, bicarbonate and the anion gap, then renal, glucose, liver and finally calcium."],
     ["The liver group — the transaminases, alkaline phosphatase, and bilirubin",
      "The liver group is read fourth; the electrolytes and the anion gap come first."],
     ["The kidney group — urea nitrogen, creatinine, and the filtration rate",
      "That is the second step."],
     ["The minerals — calcium",
      "Calcium is read last; the electrolytes and acid-base group come first."]],
   c=0, cite=c(20)),

 dict(topic="Reading a panel", io=IOD, slot="education",
   q="What usually follows any single or combined abnormality on a panel?",
   opts=[
     ["Confirmatory testing",
      "Correct — a single abnormal value is a screening signal rather than a diagnosis, so it is confirmed before it is acted on."],
     ["Immediate treatment of the abnormal value",
      "Treating the value is not the next step; any single or combined abnormality usually warrants confirmatory testing before it is acted on."],
     ["Referral to the relevant specialist",
      "Referral may follow eventually, but the immediate next step is to confirm the abnormality."],
     ["Repeating the whole panel every day",
      "Repeating the whole panel daily is neither targeted nor necessary; it is the specific abnormality that gets confirmed."]],
   c=0, cite=c(20)),

 # ---- electrolytes and acid-base ----
 dict(topic="Potassium and pH", io=IOF, slot="etiology",
   q="What happens to serum potassium in acidosis?",
   opts=[
     ["Potassium shifts out of cells, so the serum level rises",
      "Correct — in acidosis hydrogen ions move into cells and potassium moves out to maintain electroneutrality, so the serum potassium rises."],
     ["Potassium shifts into cells, so the serum level falls",
      "That is what happens in alkalosis."],
     ["Potassium is excreted faster, so the serum level falls",
      "The rise is a transcellular shift rather than reduced excretion; potassium moves out of cells as hydrogen ions move in."],
     ["Potassium is unchanged, because pH does not affect it",
      "pH and potassium are tightly coupled; acidosis reliably shifts potassium out of cells and raises the serum level."]],
   c=0, cite=c(21)),

 dict(topic="Potassium and pH", io=IOF, slot="etiology",
   q="What happens to serum potassium in alkalosis?",
   opts=[
     ["Potassium shifts into cells, so the serum level falls",
      "Correct — alkalosis shifts potassium into cells and lowers the serum level, while acidosis shifts it out of cells and raises the serum level."],
     ["Potassium shifts out of cells, so the serum level rises",
      "That is the acidosis direction."],
     ["Potassium is retained by the kidney, so the serum level rises",
      "The fall is a shift into cells rather than renal retention; retention would raise the serum level, not lower it."],
     ["Potassium is unaffected by alkalosis",
      "Alkalosis has a definite effect; it drives potassium into cells and lowers the serum level."]],
   c=0, cite=c(21)),

 dict(topic="Potassium and pH", io=IOF, slot="etiology",
   q="The potassium and pH relationship works in both directions. What does potassium depletion do?",
   opts=[
     ["It increases renal acid secretion",
      "Correct — potassium depletion makes the kidney secrete more acid, which is why hypokalemia sustains a metabolic alkalosis."],
     ["It decreases renal acid secretion",
      "Acid secretion increases rather than decreases, which is why potassium depletion maintains an alkalosis."],
     ["It has no effect on renal acid handling",
      "There is a clear effect; potassium depletion increases renal acid secretion, and the relationship runs in both directions."],
     ["It causes the kidney to retain bicarbonate only",
      "The kidney does retain bicarbonate as a consequence, but the primary change is increased acid secretion."]],
   c=0, cite=c(21)),

 dict(topic="Chloride and acid-base", io=IOF, slot="etiology",
   q="How does loss of chloride, as in vomiting, produce a metabolic alkalosis?",
   opts=[
     ["It raises the strong ion difference",
      "Correct — chloride is a strong anion, so losing it in gastric fluid widens the strong ion difference, and electroneutrality is restored by a rise in bicarbonate."],
     ["It lowers the strong ion difference",
      "The strong ion difference rises rather than falls; losing chloride, a strong anion, widens the gap between the strong cations and anions."],
     ["It directly removes hydrogen ions from the blood",
      "Direct hydrogen removal is not the mechanism given; loss of chloride, as in vomiting, raises the strong ion difference and produces a metabolic alkalosis."],
     ["It stimulates the lungs to retain carbon dioxide",
      "That would be a respiratory rather than a metabolic mechanism."]],
   c=0, cite=c(21)),

 dict(topic="Electrolytes and acid-base", io=IOF, slot="education",
   q="Acid-base and electrolyte balance cannot be separated. Why?",
   opts=[
     ["They are regulated by the same renal transport mechanisms and are physically coupled by electroneutrality",
      "Correct — the same renal transporters move hydrogen, bicarbonate, sodium, potassium and chloride, and electroneutrality means a shift in one must be matched by another."],
     ["They are measured on the same laboratory analyzer",
      "The coupling is physiological rather than analytic; the same renal transporters handle both, and electroneutrality links them."],
     ["They are both reported on the comprehensive panel only",
      "Both appear on the basic panel, and the coupling is physiological rather than a matter of which panel reports them."],
     ["They both depend on the liver's synthetic function",
      "The coupling is renal rather than hepatic; shared tubular transport and electroneutrality are what bind the two."]],
   c=0, cite=c(21)),

 # ---- the anion gap: CALCULATION IS EXPECTED ----
 dict(topic="Anion gap", io=IOF, slot="initial test",
   q="What is the standard formula for the anion gap?",
   opts=[
     ["Sodium minus the sum of chloride and bicarbonate",
      "Correct — the gap is sodium minus the sum of chloride and bicarbonate, and what remains represents the unmeasured anions."],
     ["Sodium minus chloride, without subtracting bicarbonate",
      "Bicarbonate is part of the subtraction."],
     ["The sum of sodium and potassium minus chloride",
      "This omits bicarbonate and adds potassium, which is the extended formula's change."],
     ["Chloride plus bicarbonate minus sodium",
      "This inverts the calculation and would give a negative value."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="A patient's sodium is 140, chloride 100 and bicarbonate 24 milliequivalents per liter. What is the anion gap?",
   opts=[
     ["16", "Correct — 140 minus the sum of 100 and 24 gives 16, which is above the normal range."],
     ["24", "This subtracts only the chloride and leaves the bicarbonate out."],
     ["40", "This subtracts only the bicarbonate."],
     ["8", "This is within the normal range but does not follow from these numbers."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="A patient's sodium is 138, chloride 104 and bicarbonate 24 milliequivalents per liter. How should the anion gap be read?",
   opts=[
     ["It is 10, which sits within the normal range",
      "Correct — 138 minus the sum of 104 and 24 is 10, which sits inside the standard normal range of 8 to 12 milliequivalents per liter."],
     ["It is 10, which is above the normal range",
      "The arithmetic is right, but a gap of 10 sits inside the standard 8 to 12 range, so it is not raised."],
     ["It is 14, which is above the normal range",
      "Sodium minus the sum of chloride and bicarbonate is 138 minus 128, which gives 10, not 14."],
     ["It is 34, which is markedly raised",
      "A gap of 34 comes from leaving bicarbonate out; the standard formula subtracts chloride plus bicarbonate from sodium."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="Using the standard formula, what is the normal range for the anion gap?",
   opts=[
     ["8 to 12 milliequivalents per liter",
      "Correct — 8 to 12 milliequivalents per liter is the normal range when potassium is left out of the calculation."],
     ["10 to 14 milliequivalents per liter",
      "That is the range for the extended formula that includes potassium."],
     ["4 to 8 milliequivalents per liter",
      "4 to 8 sits below normal; the standard range begins at 8 milliequivalents per liter."],
     ["12 to 20 milliequivalents per liter",
      "12 to 20 overlaps the raised range; normal tops out at 12 milliequivalents per liter."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="initial test",
   q="How does the extended anion gap formula differ from the standard one?",
   opts=[
     ["Potassium is added to sodium before the subtraction, and the normal range rises to 10 to 14",
      "Correct — both the change and its effect on the range."],
     ["Potassium is subtracted along with chloride and bicarbonate, and the range falls",
      "Potassium is added to the cations, not the anions."],
     ["Albumin is added to the calculation, and the range is unchanged",
      "Albumin features in a separate correction, not in the extended formula."],
     ["Calcium is added to sodium, and the normal range rises to 10 to 14",
      "The extended formula adds potassium, not calcium."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="differential",
   q="A raised anion gap suggests what?",
   opts=[
     ["An increase in unmeasured acids",
      "Correct — a wide gap means unmeasured anions have accumulated, as with lactate, ketoacids or an ingested toxin."],
     ["A loss of bicarbonate from the gut or kidney",
      "That produces a normal-gap, hyperchloremic acidosis."],
     ["An excess of measured cations",
      "The gap widens because of unmeasured anions."],
     ["A respiratory rather than a metabolic problem",
      "The gap is used within the assessment of metabolic acidosis."]],
   c=0, cite=cn(22)),

 dict(topic="Anion gap", io=IOF, slot="differential",
   q="A normal anion gap acidosis is most often caused by what?",
   opts=[
     ["Gastrointestinal or renal bicarbonate loss",
      "Correct — bicarbonate lost through the gut or kidney is replaced by chloride, so the gap stays normal and the chloride rises."],
     ["Accumulation of ketoacids",
      "Ketoacids are unmeasured anions and widen the gap."],
     ["Lactic acid accumulation",
      "Lactate also widens the gap."],
     ["Methanol or ethylene glycol ingestion",
      "Both are among the causes of a widened gap."]],
   c=0, cite=cn(22)),

 dict(topic="Anion gap", io=IOF, slot="differential",
   q="The mnemonic for a raised anion gap includes which of these?",
   opts=[
     ["Methanol, uremia, diabetic ketoacidosis, lactic acidosis, ethylene glycol, and salicylates",
      "Correct — methanol, uremia, diabetic ketoacidosis, lactic acidosis, ethylene glycol and salicylates all add unmeasured anions to the plasma."],
     ["Vomiting, diuretics, and excess antacid use",
      "Those produce alkalosis or a normal-gap picture."],
     ["Diarrhea, renal tubular acidosis, and saline infusion",
      "Those are normal-gap, hyperchloremic causes."],
     ["Sepsis, heart failure, and dehydration alone",
      "Sepsis, heart failure and dehydration widen the gap only when they generate lactate; on their own they are not gap-widening causes."]],
   c=0, cite=cn(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="How is the anion gap adjusted when albumin is low?",
   opts=[
     ["Correct it upward by about 2.5 for every one gram per deciliter the albumin has fallen",
      "Correct — a low albumin calls for correcting the anion gap by about 2.5 for every one gram per deciliter drop in albumin."],
     ["Correct it downward by about 2.5 for every one gram per deciliter the albumin has fallen",
      "The correction raises the gap, because albumin is itself an unmeasured anion."],
     ["No correction is needed, because albumin is not charged",
      "Albumin carries negative charge and does affect the gap."],
     ["Correct it by 1.6 for every one gram per deciliter",
      "That figure belongs to the sodium correction for glucose."]],
   c=0, cite=c(21)),

 # ---- fluid and electrolyte homeostasis ----
 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="Serum sodium is the primary indicator of what?",
   opts=[
     ["Water balance", "Correct — the sodium concentration reflects how much water the sodium is dissolved in, so it tracks water balance rather than total salt."],
     ["Total body salt content", "Total body salt is not what a concentration shows; a patient can be salt-depleted with a normal sodium if water is lost in proportion."],
     ["Extracellular fluid volume", "Extracellular volume is governed by total-body sodium, not by its serum concentration."],
     ["Kidney filtration rate", "That is estimated from creatinine."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="Hyponatremia usually means what?",
   opts=[
     ["Water excess", "Correct — a low sodium usually means the sodium has been diluted by excess water rather than that sodium itself has been lost."],
     ["Salt deficiency", "Salt deficiency is possible but less common; a low sodium is read first as a water excess."],
     ["Kidney failure", "Kidney failure can contribute, but the first reading of a low sodium is dilution by excess water."],
     ["Dehydration", "Dehydration would tend to concentrate rather than dilute the sodium."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="initial test",
   q="What does serum osmolality allow you to distinguish?",
   opts=[
     ["True hypotonic hyponatremia from the pseudo- and hypertonic forms",
      "Correct — osmolality is normal in pseudohyponatremia and raised in the hypertonic form, so it isolates the true hypotonic case."],
     ["Prerenal from intrinsic renal failure",
      "That separation comes from the urea nitrogen to creatinine ratio."],
     ["Raised-gap from normal-gap acidosis",
      "That comes from the anion gap."],
     ["Acute from chronic kidney disease",
      "Chronicity is judged over at least three months."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="A urine sodium below 20 milliequivalents per liter suggests what?",
   opts=[
     ["Hypovolaemia", "Correct — a hypovolemic kidney reabsorbs sodium avidly, driving the urine sodium below 20 milliequivalents per liter."],
     ["The syndrome of inappropriate antidiuretic hormone secretion",
      "That is suggested by a urine sodium above 40 with concentrated urine."],
     ["Intrinsic renal failure", "Intrinsic renal failure impairs sodium reabsorption, so the urine sodium is typically raised rather than low."],
     ["Diabetes insipidus", "Diabetes insipidus is a water-handling disorder judged from urine osmolality and the water deprivation test, not from urine sodium."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="A urine sodium above 40 milliequivalents per liter with concentrated urine suggests what?",
   opts=[
     ["The syndrome of inappropriate antidiuretic hormone secretion",
      "Correct — inappropriate antidiuretic hormone retains water while sodium continues to be excreted, giving concentrated urine with a high sodium."],
     ["Hypovolaemia", "That is suggested by a urine sodium below 20."],
     ["Diabetic ketoacidosis", "That is read from glucose, bicarbonate, and the gap."],
     ["Hepatorenal syndrome", "Hepatorenal syndrome behaves like hypovolemia, with avid sodium retention and a LOW urine sodium."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="Which four core tests evaluate water and electrolyte balance?",
   opts=[
     ["Serum sodium, serum osmolality, urine sodium and osmolality, and the urea nitrogen to creatinine ratio",
      "Correct — serum sodium and osmolality, urine sodium and osmolality, and the urea nitrogen to creatinine ratio together locate the problem."],
     ["Serum sodium, serum potassium, serum calcium, and serum magnesium",
      "The evaluation is not simply four cations; it pairs serum measurements with urine measurements, and magnesium is not part of the set."],
     ["Serum glucose, bicarbonate, the anion gap, and ketones",
      "That is the diabetic ketoacidosis workup."],
     ["Albumin, total protein, prothrombin time, and bilirubin",
      "Those assess liver function."]],
   c=0, cite=c(25)),

 # ---- pitfalls and corrections ----
 dict(topic="Pitfalls", io=IOD, slot="test finding",
   q="Hyperglycemia lowers the measured sodium. What should be done about it?",
   opts=[
     ["Use a corrected sodium, obtained from a clinical calculator rather than by hand",
      "Correct — hyperglycemia lowers measured sodium by about 1.6 to 2 milliequivalents per liter per 100 milligrams per deciliter of glucose, so a corrected sodium is used."],
     ["Ignore the sodium entirely until the glucose is normal",
      "The value is usable once corrected."],
     ["Repeat the sample from an artery instead of a vein",
      "Sampling site is not the issue."],
     ["Subtract the glucose from the sodium",
      "That is not how the correction works."]],
   c=0, cite=c(26)),

 dict(topic="Pitfalls", io=IOD, slot="test finding",
   q="In which direction does hyperglycemia move the measured sodium, and why?",
   opts=[
     ["Downward, because glucose draws water out of the cells and dilutes it",
      "Correct — a dilutional effect, so the true sodium is higher than measured."],
     ["Upward, because glucose draws water into the cells and concentrates it",
      "The water shift is out of the cells, which dilutes rather than concentrates."],
     ["Downward, because glucose interferes chemically with the sodium assay",
      "The effect is physiological rather than analytic."],
     ["Upward, because the kidney retains sodium in response to glucose",
      "The measured value falls."]],
   c=0, cite=c(26)),

 dict(topic="Pitfalls", io=IOD, slot="differential",
   q="What distinguishes pseudohyponatremia from a true hypotonic hyponatremia?",
   opts=[
     ["The osmolality is normal in pseudohyponatremia",
      "Correct — in pseudohyponatremia severe hyperlipidemia or hyperproteinemia gives a falsely low sodium while the osmolality stays normal."],
     ["The osmolality is low in pseudohyponatremia",
      "A low osmolality indicates the true hypotonic form."],
     ["The potassium is also low in pseudohyponatremia",
      "Potassium is not what separates the two."],
     ["The urine sodium is above 40 in pseudohyponatremia",
      "Urine sodium separates hypovolemia from the syndrome of inappropriate secretion."]],
   c=0, cite=c(26)),

 dict(topic="Pitfalls", io=IOD, slot="etiology",
   q="Which two states cause pseudohyponatremia?",
   opts=[
     ["Severe hyperlipidemia and hyperproteinemia",
      "Correct — severe hyperlipidemia and hyperproteinemia displace plasma water, so the measured sodium reads low while osmolality is normal."],
     ["Severe dehydration and blood loss",
      "Those affect the true sodium rather than producing a false reading."],
     ["Heart failure and cirrhosis",
      "Those cause a genuine dilutional hyponatremia."],
     ["Adrenal insufficiency and hypothyroidism",
      "Adrenal insufficiency and hypothyroidism cause a genuine hyponatremia rather than a laboratory artifact."]],
   c=0, cite=c(26)),

 dict(topic="Pitfalls", io=IOD, slot="education",
   q="What is true of interpreting a sodium value on its own?",
   opts=[
     ["The number alone does not give the diagnosis; interpret it alongside volume status",
      "Correct — the same sodium value means different things in a hypovolemic and a fluid-overloaded patient, so volume status must be assessed alongside it."],
     ["The number alone is diagnostic if it is outside the reference range",
      "A value outside the range is a starting point rather than a diagnosis; volume status determines what it means."],
     ["The number should be interpreted alongside the potassium only",
      "Potassium alone is not enough; volume status from history, examination and the kidney markers is what interprets the sodium."],
     ["The number is only meaningful on a comprehensive panel",
      "Sodium is on the basic panel and is meaningful there."]],
   c=0, cite=c(26)),

 # ---- correlating with other tests ----
 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Abnormal liver tests should be followed by which imaging first?",
   opts=[
     ["Ultrasound", "Correct — abnormal liver tests lead to imaging that starts with ultrasound for steatosis and biliary dilation, then computed tomography or magnetic resonance."],
     ["Computed tomography with contrast", "Contrast computed tomography follows ultrasound rather than preceding it."],
     ["Magnetic resonance cholangiopancreatography", "Magnetic resonance cholangiopancreatography is not the first step; abnormal liver tests go to ultrasound first, then computed tomography or magnetic resonance."],
     ["Plain abdominal radiography", "Plain radiography is not in the pathway; abnormal liver tests go to ultrasound for steatosis and biliary dilation, then computed tomography or magnetic resonance."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="test finding",
   q="Over what period must a reduced filtration rate persist to be called chronic?",
   opts=[
     ["At least three months", "Correct — a reduced filtration rate must persist at least three months to be called chronic rather than acute."],
     ["At least one month", "One month is too short; three months is the threshold separating chronic from acute."],
     ["At least six months", "Six months exceeds the threshold; chronicity is established at three months."],
     ["At least one year", "A year is far beyond the threshold; three months is enough to call the reduction chronic."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Which test is named for confirming an estimated filtration rate when accuracy matters?",
   opts=[
     ["Cystatin C", "Correct — cystatin C is produced at a steadier rate than creatinine and is unaffected by muscle mass, so it confirms the estimate."],
     ["A twenty-four hour urine protein", "That measures protein loss rather than confirming the rate."],
     ["Serum urea nitrogen", "Too non-specific to confirm the rate."],
     ["A renal biopsy", "Biopsy characterizes the cause of kidney disease rather than confirming the filtration rate."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Which tests are added to the panel in a diabetic ketoacidosis workup?",
   opts=[
     ["Ketones with beta-hydroxybutyrate, a venous blood gas, urinalysis, an electrocardiogram, and a complete blood count",
      "Correct — ketones with beta-hydroxybutyrate, a venous blood gas, urinalysis, an electrocardiogram and a complete blood count round out the panel."],
     ["Liver ultrasound, cystatin C, and a urine protein",
      "Those belong to the liver and kidney correlation lines."],
     ["Serum osmolality with urine sodium and osmolality",
      "That is the hyponatremia workup."],
     ["Blood cultures and a chest radiograph",
      "Blood cultures and a chest radiograph are added only where infection is suspected as the precipitant, not routinely."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Why is an electrocardiogram part of the ketoacidosis workup?",
   opts=[
     ["To look for the cardiac effects of a raised potassium",
      "Correct — the ketoacidosis workup includes an electrocardiogram for potassium effects, because both high and low potassium can cause life-threatening arrhythmias."],
     ["To exclude a myocardial infarction as the precipitant",
      "Infarction is not the stated reason; the electrocardiogram in the ketoacidosis workup is there to show the cardiac effects of potassium."],
     ["To measure the degree of dehydration",
      "The tracing does not measure volume status."],
     ["To confirm the diagnosis of ketoacidosis",
      "Diagnosis comes from the glucose, gap, and ketones."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Which tests are paired with the panel to work out the cause of hyponatremia?",
   opts=[
     ["Serum osmolality with urine sodium and osmolality",
      "Correct — serum osmolality separates true hypotonic hyponatremia from the pseudo- and hypertonic forms, and the urine studies then separate hypovolemia from inappropriate antidiuretic hormone secretion."],
     ["Ketones and a venous blood gas",
      "Those belong to the ketoacidosis workup."],
     ["Liver ultrasound and cystatin C",
      "Those belong to the liver and kidney lines."],
     ["A complete blood count and inflammatory markers",
      "A blood count and inflammatory markers say nothing about water handling; the cause of a low sodium is found from serum and urine osmolality with urine sodium."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="education",
   q="What general lesson applies to chemistry results?",
   opts=[
     ["A lab value narrows the differential and directs the next test rather than being diagnostic by itself",
      "Correct — a chemistry result shifts the probability of the diagnoses under consideration and tells you what to order next, rather than settling the question on its own."],
     ["A lab value is diagnostic once it falls outside the reference range",
      "Falling outside the range is not diagnostic; about 2.5 percent of healthy people fall outside a normal range by chance, so values are read in context."],
     ["A lab value should always be confirmed by imaging before acting",
      "Imaging is not a routine confirmation; a lab value directs the next test, which may be imaging, urine studies or a blood gas, depending on the result."],
     ["A lab value is only useful when the whole panel is abnormal",
      "A single abnormal value is informative on its own; an isolated result still narrows the differential and points to the next test."]],
   c=0, cite=cn(24)),

 # ---- the vomiting case ----
 dict(topic="Vomiting case", io=IOF, slot="test finding",
   q="After three days of intractable vomiting, what does the panel show?",
   opts=[
     ["Low sodium, low potassium, low chloride, and a raised bicarbonate with alkalemia",
      "Correct — the case shows low sodium, potassium and chloride with a raised bicarbonate and alkalemia, maintained by volume, potassium and chloride depletion."],
     ["Low sodium, raised potassium, raised chloride, and a low bicarbonate",
      "That would be an acidosis, not the alkalosis vomiting produces."],
     ["Raised sodium, raised potassium, and a normal bicarbonate",
      "Vomiting depletes rather than raises these."],
     ["Normal electrolytes with an isolated raised anion gap",
      "The case turns on the electrolyte losses."]],
   c=0, cite=c(27)),

 dict(topic="Vomiting case", io=IOF, slot="etiology",
   q="What keeps the alkalosis going in the vomiting case?",
   opts=[
     ["Volume, potassium, and chloride depletion force the kidney to reabsorb sodium and bicarbonate",
      "Correct — a volume-depleted kidney reabsorbs sodium avidly, and with chloride unavailable it must reabsorb bicarbonate alongside it, so the alkalosis is sustained long after the vomiting stops."],
     ["The lungs retain carbon dioxide to compensate",
      "Carbon dioxide retention is the respiratory compensation for an alkalosis, not what maintains it; the maintenance is renal."],
     ["The liver stops clearing bicarbonate from the blood",
      "The liver has no such role here."],
     ["Ongoing loss of gastric acid is the only factor",
      "Gastric acid loss starts the alkalosis but does not maintain it; renal bicarbonate reabsorption driven by volume, chloride and potassium depletion keeps it going."]],
   c=0, cite=c(27)),

 dict(topic="Vomiting case", io=IOF, slot="first-line",
   q="What corrects the alkalosis in the vomiting case?",
   opts=[
     ["Replacing sodium, chloride, and potassium with saline and potassium chloride",
      "Correct — the alkalosis is maintained by volume, chloride and potassium depletion together, so saline with potassium chloride is needed to replace all three before the kidney will excrete the excess bicarbonate."],
     ["Giving intravenous bicarbonate",
      "The bicarbonate is already high; adding more would worsen the alkalosis."],
     ["Giving an antiemetic alone",
      "Stopping the vomiting does not itself reverse the depletion driving the alkalosis."],
     ["Restricting fluid intake",
      "Volume depletion is part of what maintains the alkalosis."]],
   c=0, cite=c(27)),

 dict(topic="Vomiting case", io=IOF, slot="education",
   q="What does the vomiting case illustrate?",
   opts=[
     ["That electrolytes and acid-base cannot be separated",
      "Correct — one insult produces both an electrolyte disturbance and an acid-base disturbance, and neither can be corrected without addressing the other."],
     ["That a single electrolyte can be interpreted on its own",
      "The case shows the reverse: the low chloride, low potassium and raised bicarbonate only make sense read together."],
     ["That vomiting is the commonest cause of alkalosis",
      "Frequency is not the lesson; the case is used because one insult produces coupled electrolyte and acid-base changes."],
     ["That imaging is required before treating an electrolyte disorder",
      "No imaging is involved; the case is resolved entirely from the electrolyte and acid-base pattern and the history."]],
   c=0, cite=cn(27)),
]
