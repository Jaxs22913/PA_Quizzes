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
      "Correct — the deck's definition of the hepatocellular pattern."],
     ["Alkaline phosphatase is raised out of proportion to the transaminases",
      "That is the cholestatic pattern."],
     ["Bilirubin is raised while the enzymes stay normal",
      "That is isolated hyperbilirubinaemia."],
     ["Both the transaminases and alkaline phosphatase are raised together",
      "That is the mixed pattern."]],
   c=0, cite=c(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="test finding",
   q="Which pattern defines cholestatic liver injury?",
   opts=[
     ["Alkaline phosphatase is raised out of proportion to the transaminases",
      "Correct — the deck's definition of the cholestatic pattern."],
     ["The transaminases are raised out of proportion to alkaline phosphatase",
      "That is the hepatocellular pattern."],
     ["Albumin is low with a prolonged prothrombin time",
      "Those indicate advanced disease rather than defining cholestasis."],
     ["Bilirubin is raised while the enzymes stay normal",
      "That is isolated hyperbilirubinaemia."]],
   c=0, cite=c(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="Which causes do the speaker notes give for a cholestatic pattern?",
   opts=[
     ["Bile duct obstruction, gallstones, and primary biliary cholangitis",
      "Correct — the three the notes list."],
     ["Viral hepatitis, alcohol, and ischaemia",
      "Those are given for the hepatocellular pattern."],
     ["Gilbert syndrome and haemolysis",
      "Those are given for isolated hyperbilirubinaemia."],
     ["Heart failure and sepsis",
      "Neither is on the notes' cholestatic list."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="Which two causes do the speaker notes give for isolated hyperbilirubinaemia?",
   opts=[
     ["Gilbert syndrome and haemolysis",
      "Correct — the two the notes name for a raised bilirubin with normal enzymes."],
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
      "Correct — the ratio the speaker notes give for alcohol."],
     ["Viral hepatitis",
      "Viral hepatitis does not characteristically produce this ratio."],
     ["Biliary obstruction",
      "That raises alkaline phosphatase preferentially."],
     ["Ischaemic hepatitis",
      "Ischaemia is one of the causes of transaminases in the thousands."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="Transaminases in the thousands narrow the cause to which three possibilities?",
   opts=[
     ["Viral hepatitis, ischaemia, and toxins",
      "Correct — the three the speaker notes name at that magnitude."],
     ["Alcohol, fatty liver disease, and gallstones",
      "None of these characteristically reaches the thousands."],
     ["Gilbert syndrome, haemolysis, and biliary obstruction",
      "These raise bilirubin or alkaline phosphatase rather than the transaminases."],
     ["Heart failure, sepsis, and pancreatitis",
      "Not the three the notes list."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOE, slot="differential",
   q="A raised aspartate aminotransferase with a normal alanine transaminase points away from the liver and towards what?",
   opts=[
     ["Cardiac or skeletal muscle",
      "Correct — the notes send you to muscle when only the less specific enzyme is up."],
     ["The biliary tree",
      "That would raise alkaline phosphatase."],
     ["The kidney",
      "Kidney disease is read from creatinine and the filtration rate."],
     ["Red blood cell breakdown",
      "That raises bilirubin."]],
   c=0, cite=cn(17)),

 dict(topic="Hepatic patterns", io=IOD, slot="test finding",
   q="How do the speaker notes band the magnitude of a transaminase rise?",
   opts=[
     ["Mild under five times, moderate five to fifteen times, and severe over fifteen times the upper limit",
      "Correct — the three bands the notes give."],
     ["Mild under two times, moderate two to ten times, and severe over ten times the upper limit",
      "Not the bands the notes use."],
     ["Mild under ten times, moderate ten to fifty times, and severe over fifty times the upper limit",
      "These thresholds are higher than the notes state."],
     ["Mild under three times, moderate three to twenty times, and severe over twenty times the upper limit",
      "Not the deck's banding."]],
   c=0, cite=cn(17)),

 # ---- renal and metabolic patterns ----
 dict(topic="Renal pattern", io=IOE, slot="test finding",
   q="Which laboratory pattern does the deck give for a renal disorder?",
   opts=[
     ["Raised urea nitrogen and creatinine with a fallen filtration rate, and possibly a raised potassium and a metabolic acidosis",
      "Correct — the deck's renal row."],
     ["Raised transaminases with a low albumin and a prolonged prothrombin time",
      "That is the hepatic row."],
     ["A raised glucose with a low bicarbonate and a raised anion gap",
      "That is the metabolic row, and describes ketoacidosis."],
     ["A low sodium with a high bicarbonate and a low chloride",
      "That is the vomiting case rather than the renal pattern."]],
   c=0, cite=c(19)),

 dict(topic="Renal pattern", io=IOE, slot="test finding",
   q="Besides urea nitrogen and creatinine, which findings does the deck list in the renal pattern?",
   opts=[
     ["A raised phosphate, a lowered calcium, and albuminuria",
      "Correct — the deck lists these alongside the potassium and acidosis."],
     ["A raised calcium, a lowered phosphate, and glycosuria",
      "The calcium and phosphate directions are reversed and glycosuria is not listed."],
     ["A raised albumin with a lowered total protein",
      "Albuminuria is protein in the urine, not a raised serum albumin."],
     ["A raised bilirubin with a lowered alkaline phosphatase",
      "Those belong to the hepatic row."]],
   c=0, cite=c(19)),

 dict(topic="Metabolic pattern", io=IOE, slot="test finding",
   q="Which laboratory pattern does the deck give for diabetic ketoacidosis?",
   opts=[
     ["A raised glucose, a lowered bicarbonate, a raised anion gap, and a low pH",
      "Correct — the deck's metabolic row."],
     ["A lowered glucose, a raised bicarbonate, and a normal anion gap",
      "Every direction here is reversed."],
     ["A raised glucose with a raised bicarbonate and a high pH",
      "Ketoacidosis is an acidosis, so bicarbonate falls and pH drops."],
     ["A normal glucose with a lowered bicarbonate and a normal gap",
      "The glucose is raised in this disorder."]],
   c=0, cite=c(19)),

 dict(topic="Metabolic pattern", io=IOE, slot="test finding",
   q="In diabetic ketoacidosis the serum potassium may be raised. What does the deck say about total-body potassium?",
   opts=[
     ["Total-body potassium is depleted despite the raised serum level",
      "Correct — the deck flags the discrepancy explicitly."],
     ["Total-body potassium is also raised, matching the serum level",
      "The deck's point is that the two disagree."],
     ["Total-body potassium is normal and only the serum is affected",
      "The deck describes depletion, not a normal total."],
     ["Total-body potassium cannot be inferred from any measurement",
      "The deck states the direction rather than declining to."]],
   c=0, cite=c(19)),

 dict(topic="Overlap syndromes", io=IOE, slot="differential",
   q="Which syndrome does the deck give as showing both liver and kidney failure at once?",
   opts=[
     ["Hepatorenal syndrome",
      "Correct — the deck names this as the overlap of the two patterns."],
     ["Cardiorenal syndrome",
      "That is also named, but as a cardiac and renal overlap."],
     ["Diabetic ketoacidosis",
      "That produces electrolyte and renal derangements, not liver failure."],
     ["Nephrotic syndrome",
      "The deck does not name this among its overlap examples."]],
   c=0, cite=c(19)),

 dict(topic="Reading a panel", io=IOD, slot="initial test",
   q="In the deck's stepwise approach to an abnormal comprehensive metabolic panel, which step comes first?",
   opts=[
     ["The electrolytes and acid-base group, then calculate the anion gap",
      "Correct — the deck's first step, ending in the gap calculation."],
     ["The liver group — the transaminases, alkaline phosphatase, and bilirubin",
      "Liver comes fourth in the deck's order."],
     ["The kidney group — urea nitrogen, creatinine, and the filtration rate",
      "That is the second step."],
     ["The minerals — calcium",
      "Calcium is the last step in the deck's sequence."]],
   c=0, cite=c(20)),

 dict(topic="Reading a panel", io=IOD, slot="education",
   q="What does the deck say usually follows any single or combined abnormality on a panel?",
   opts=[
     ["Confirmatory testing",
      "Correct — the deck says an abnormality usually warrants confirmation."],
     ["Immediate treatment of the abnormal value",
      "The deck's next step is diagnostic."],
     ["Referral to the relevant specialist",
      "Referral is not the deck's stated next step."],
     ["Repeating the whole panel every day",
      "The deck asks for confirmation, not daily repetition."]],
   c=0, cite=c(20)),

 # ---- electrolytes and acid-base ----
 dict(topic="Potassium and pH", io=IOF, slot="etiology",
   q="What happens to serum potassium in acidosis?",
   opts=[
     ["Potassium shifts out of cells, so the serum level rises",
      "Correct — the shift the deck describes for acidosis."],
     ["Potassium shifts into cells, so the serum level falls",
      "That is what happens in alkalosis."],
     ["Potassium is excreted faster, so the serum level falls",
      "The deck describes a transcellular shift rather than a change in excretion."],
     ["Potassium is unchanged, because pH does not affect it",
      "The deck's point is that the two are coupled."]],
   c=0, cite=c(21)),

 dict(topic="Potassium and pH", io=IOF, slot="etiology",
   q="What happens to serum potassium in alkalosis?",
   opts=[
     ["Potassium shifts into cells, so the serum level falls",
      "Correct — the shift the deck describes for alkalosis."],
     ["Potassium shifts out of cells, so the serum level rises",
      "That is the acidosis direction."],
     ["Potassium is retained by the kidney, so the serum level rises",
      "The deck describes a shift across the cell membrane."],
     ["Potassium is unaffected by alkalosis",
      "The deck describes a definite direction of movement."]],
   c=0, cite=c(21)),

 dict(topic="Potassium and pH", io=IOF, slot="etiology",
   q="The deck describes the potassium and pH relationship as working in both directions. What does potassium depletion do?",
   opts=[
     ["It increases renal acid secretion",
      "Correct — the reverse arm of the relationship as the deck states it."],
     ["It decreases renal acid secretion",
      "The deck gives the opposite direction."],
     ["It has no effect on renal acid handling",
      "The deck's point is that the effect runs both ways."],
     ["It causes the kidney to retain bicarbonate only",
      "The deck describes acid secretion rather than bicarbonate retention."]],
   c=0, cite=c(21)),

 dict(topic="Chloride and acid-base", io=IOF, slot="etiology",
   q="How does loss of chloride, as in vomiting, produce a metabolic alkalosis?",
   opts=[
     ["It raises the strong ion difference",
      "Correct — the deck's stated mechanism."],
     ["It lowers the strong ion difference",
      "The deck gives the opposite direction."],
     ["It directly removes hydrogen ions from the blood",
      "Vomiting removes acid from the stomach, but the deck's stated mechanism here is the ion difference."],
     ["It stimulates the lungs to retain carbon dioxide",
      "That would be a respiratory rather than a metabolic mechanism."]],
   c=0, cite=c(21)),

 dict(topic="Electrolytes and acid-base", io=IOF, slot="education",
   q="The deck states that acid-base and electrolyte balance cannot be separated. Why?",
   opts=[
     ["They are regulated by the same renal transport mechanisms and are physically coupled by electroneutrality",
      "Correct — the two reasons the deck gives."],
     ["They are measured on the same laboratory analyser",
      "The deck's argument is physiological, not analytic."],
     ["They are both reported on the comprehensive panel only",
      "Both are on the basic panel, and that is not the deck's reason."],
     ["They both depend on the liver's synthetic function",
      "The deck attributes the coupling to renal handling and electroneutrality."]],
   c=0, cite=c(21)),

 # ---- the anion gap: CALCULATION IS EXPECTED ----
 dict(topic="Anion gap", io=IOF, slot="initial test",
   q="What is the standard formula for the anion gap?",
   opts=[
     ["Sodium minus the sum of chloride and bicarbonate",
      "Correct — the standard formula as the deck prints it."],
     ["Sodium minus chloride, without subtracting bicarbonate",
      "Bicarbonate is part of the subtraction."],
     ["The sum of sodium and potassium minus chloride",
      "This omits bicarbonate and adds potassium, which is the extended formula's change."],
     ["Chloride plus bicarbonate minus sodium",
      "This inverts the calculation and would give a negative value."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="A patient's sodium is 140, chloride 100 and bicarbonate 24 milliequivalents per litre. What is the anion gap?",
   opts=[
     ["16", "Correct — 140 minus the sum of 100 and 24 gives 16, which is above the normal range."],
     ["24", "This subtracts only the chloride and leaves the bicarbonate out."],
     ["40", "This subtracts only the bicarbonate."],
     ["8", "This is within the normal range but does not follow from these numbers."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="A patient's sodium is 138, chloride 104 and bicarbonate 24 milliequivalents per litre. How should the anion gap be read?",
   opts=[
     ["It is 10, which sits within the normal range",
      "Correct — 138 minus 128 is 10, inside the 8 to 12 range Reynolds gave."],
     ["It is 10, which is above the normal range",
      "The arithmetic is right but 10 sits inside the normal range."],
     ["It is 14, which is above the normal range",
      "The subtraction does not give 14."],
     ["It is 34, which is markedly raised",
      "This leaves the bicarbonate out of the subtraction."]],
   c=0, cite=c(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="Using the standard formula, what is the normal range for the anion gap?",
   opts=[
     ["8 to 12 milliequivalents per litre",
      "Correct — the range the deck prints and Reynolds repeated in the lecture."],
     ["10 to 14 milliequivalents per litre",
      "That is the range for the extended formula that includes potassium."],
     ["4 to 8 milliequivalents per litre",
      "Below the deck's stated range."],
     ["12 to 20 milliequivalents per litre",
      "Above the deck's stated range."]],
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
      "Correct — the speaker notes' interpretation of a wide gap."],
     ["A loss of bicarbonate from the gut or kidney",
      "That produces a normal-gap, hyperchloraemic acidosis."],
     ["An excess of measured cations",
      "The gap widens because of unmeasured anions."],
     ["A respiratory rather than a metabolic problem",
      "The gap is used within the assessment of metabolic acidosis."]],
   c=0, cite=cn(22)),

 dict(topic="Anion gap", io=IOF, slot="differential",
   q="A normal anion gap acidosis is most often caused by what?",
   opts=[
     ["Gastrointestinal or renal bicarbonate loss",
      "Correct — the cause the speaker notes give for the hyperchloraemic form."],
     ["Accumulation of ketoacids",
      "Ketoacids are unmeasured anions and widen the gap."],
     ["Lactic acid accumulation",
      "Lactate also widens the gap."],
     ["Methanol or ethylene glycol ingestion",
      "Both are among the causes of a widened gap."]],
   c=0, cite=cn(22)),

 dict(topic="Anion gap", io=IOF, slot="differential",
   q="The mnemonic in the speaker notes for a raised anion gap includes which of these?",
   opts=[
     ["Methanol, uraemia, diabetic ketoacidosis, lactic acidosis, ethylene glycol, and salicylates",
      "Correct — the causes the notes list under the mnemonic."],
     ["Vomiting, diuretics, and excess antacid use",
      "Those produce alkalosis or a normal-gap picture."],
     ["Diarrhoea, renal tubular acidosis, and saline infusion",
      "Those are normal-gap, hyperchloraemic causes."],
     ["Sepsis, heart failure, and dehydration alone",
      "Not the list the notes give."]],
   c=0, cite=cn(22)),

 dict(topic="Anion gap", io=IOF, slot="test finding",
   q="How does the deck say the anion gap should be adjusted when albumin is low?",
   opts=[
     ["Correct it upward by about 2.5 for every one gram per decilitre the albumin has fallen",
      "Correct — the correction the deck prints."],
     ["Correct it downward by about 2.5 for every one gram per decilitre the albumin has fallen",
      "The correction raises the gap, because albumin is itself an unmeasured anion."],
     ["No correction is needed, because albumin is not charged",
      "Albumin carries negative charge and does affect the gap."],
     ["Correct it by 1.6 for every one gram per decilitre",
      "That figure belongs to the sodium correction for glucose."]],
   c=0, cite=c(21)),

 # ---- fluid and electrolyte homeostasis ----
 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="Serum sodium is the primary indicator of what?",
   opts=[
     ["Water balance", "Correct — the deck is explicit that it indicates water balance, not salt content."],
     ["Total body salt content", "The deck states directly that this is what it does NOT indicate."],
     ["Extracellular fluid volume", "Total-body sodium governs that, per the speaker notes."],
     ["Kidney filtration rate", "That is estimated from creatinine."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="Hyponatraemia usually means what, according to the deck?",
   opts=[
     ["Water excess", "Correct — the deck's shorthand reading of a low sodium."],
     ["Salt deficiency", "The deck reads the low value as a water problem first."],
     ["Kidney failure", "Not the deck's default reading."],
     ["Dehydration", "Dehydration would tend to concentrate rather than dilute the sodium."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="initial test",
   q="What does serum osmolality allow you to distinguish?",
   opts=[
     ["True hypotonic hyponatraemia from the pseudo- and hypertonic forms",
      "Correct — the separation the deck assigns to osmolality."],
     ["Prerenal from intrinsic renal failure",
      "That separation comes from the urea nitrogen to creatinine ratio."],
     ["Raised-gap from normal-gap acidosis",
      "That comes from the anion gap."],
     ["Acute from chronic kidney disease",
      "Chronicity is judged over at least three months."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="A urine sodium below 20 milliequivalents per litre suggests what?",
   opts=[
     ["Hypovolaemia", "Correct — the deck reads a low urine sodium as hypovolaemia."],
     ["The syndrome of inappropriate antidiuretic hormone secretion",
      "That is suggested by a urine sodium above 40 with concentrated urine."],
     ["Intrinsic renal failure", "Not the reading the deck gives for this value."],
     ["Diabetes insipidus", "The deck does not use urine sodium for this."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="A urine sodium above 40 milliequivalents per litre with concentrated urine suggests what?",
   opts=[
     ["The syndrome of inappropriate antidiuretic hormone secretion",
      "Correct — the deck's reading of this combination."],
     ["Hypovolaemia", "That is suggested by a urine sodium below 20."],
     ["Diabetic ketoacidosis", "That is read from glucose, bicarbonate, and the gap."],
     ["Hepatorenal syndrome", "Not what the deck assigns to this pattern."]],
   c=0, cite=c(25)),

 dict(topic="Fluid balance", io=IOI, slot="test finding",
   q="Which four core tests does the deck list for evaluating water and electrolyte balance?",
   opts=[
     ["Serum sodium, serum osmolality, urine sodium and osmolality, and the urea nitrogen to creatinine ratio",
      "Correct — the deck's core set, with potassium noted alongside."],
     ["Serum sodium, serum potassium, serum calcium, and serum magnesium",
      "Magnesium was not covered and the deck's list is not four cations."],
     ["Serum glucose, bicarbonate, the anion gap, and ketones",
      "That is the diabetic ketoacidosis workup."],
     ["Albumin, total protein, prothrombin time, and bilirubin",
      "Those assess liver function."]],
   c=0, cite=c(25)),

 # ---- pitfalls and corrections ----
 dict(topic="Pitfalls", io=IOD, slot="test finding",
   q="Hyperglycaemia lowers the measured sodium. What should be done about it?",
   opts=[
     ["Use a corrected sodium, which Reynolds obtains from a clinical calculator rather than by hand",
      "Correct — she named UpToDate, MedCalc and eCalc and did not ask for the arithmetic."],
     ["Ignore the sodium entirely until the glucose is normal",
      "The value is usable once corrected."],
     ["Repeat the sample from an artery instead of a vein",
      "Sampling site is not the issue."],
     ["Subtract the glucose from the sodium",
      "That is not how the correction works."]],
   c=0, cite=au()),

 dict(topic="Pitfalls", io=IOD, slot="test finding",
   q="In which direction does hyperglycaemia move the measured sodium, and why?",
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
   q="What distinguishes pseudohyponatraemia from a true hypotonic hyponatraemia?",
   opts=[
     ["The osmolality is normal in pseudohyponatraemia",
      "Correct — a falsely low sodium with a normal osmolality is the deck's definition."],
     ["The osmolality is low in pseudohyponatraemia",
      "A low osmolality indicates the true hypotonic form."],
     ["The potassium is also low in pseudohyponatraemia",
      "Potassium is not what separates the two."],
     ["The urine sodium is above 40 in pseudohyponatraemia",
      "Urine sodium separates hypovolaemia from the syndrome of inappropriate secretion."]],
   c=0, cite=c(26)),

 dict(topic="Pitfalls", io=IOD, slot="etiology",
   q="Which two states cause pseudohyponatraemia?",
   opts=[
     ["Severe hyperlipidaemia and hyperproteinaemia",
      "Correct — the two the deck names."],
     ["Severe dehydration and blood loss",
      "Those affect the true sodium rather than producing a false reading."],
     ["Heart failure and cirrhosis",
      "Those cause a genuine dilutional hyponatraemia."],
     ["Adrenal insufficiency and hypothyroidism",
      "The deck does not list these as causes of a false reading."]],
   c=0, cite=c(26)),

 dict(topic="Pitfalls", io=IOD, slot="education",
   q="What does the deck say about interpreting a sodium value on its own?",
   opts=[
     ["The number alone does not give the diagnosis; interpret it alongside volume status",
      "Correct — the deck's closing caution on sodium."],
     ["The number alone is diagnostic if it is outside the reference range",
      "The deck says the opposite."],
     ["The number should be interpreted alongside the potassium only",
      "The deck asks for volume status from history, examination, and the kidney markers."],
     ["The number is only meaningful on a comprehensive panel",
      "Sodium is on the basic panel and is meaningful there."]],
   c=0, cite=c(26)),

 # ---- correlating with other tests ----
 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Abnormal liver tests should be followed by which imaging first?",
   opts=[
     ["Ultrasound", "Correct — the deck names ultrasound first, for steatosis and biliary dilation."],
     ["Computed tomography with contrast", "The deck lists this after ultrasound."],
     ["Magnetic resonance cholangiopancreatography", "Not the deck's first step."],
     ["Plain abdominal radiography", "The deck does not give this for abnormal liver tests."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="test finding",
   q="Over what period must a reduced filtration rate persist to be called chronic?",
   opts=[
     ["At least three months", "Correct — the deck's threshold for chronicity."],
     ["At least one month", "Shorter than the deck's stated threshold."],
     ["At least six months", "Longer than the deck states."],
     ["At least one year", "Well beyond the deck's threshold."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Which test does the deck name for confirming an estimated filtration rate when accuracy matters?",
   opts=[
     ["Cystatin C", "Correct — the deck's named confirmatory measure."],
     ["A twenty-four hour urine protein", "That measures protein loss rather than confirming the rate."],
     ["Serum urea nitrogen", "Too non-specific to confirm the rate."],
     ["A renal biopsy", "The deck does not name biopsy for this purpose."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Which tests does the deck add to the panel in a diabetic ketoacidosis workup?",
   opts=[
     ["Ketones with beta-hydroxybutyrate, a venous blood gas, urinalysis, an electrocardiogram, and a complete blood count",
      "Correct — the deck's full ketoacidosis add-on list."],
     ["Liver ultrasound, cystatin C, and a urine protein",
      "Those belong to the liver and kidney correlation lines."],
     ["Serum osmolality with urine sodium and osmolality",
      "That is the hyponatraemia workup."],
     ["Blood cultures and a chest radiograph",
      "Not the deck's list for this presentation."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Why does the deck include an electrocardiogram in the ketoacidosis workup?",
   opts=[
     ["To look for the cardiac effects of a raised potassium",
      "Correct — the deck ties the tracing to potassium."],
     ["To exclude a myocardial infarction as the precipitant",
      "A reasonable clinical thought, but not the deck's stated reason."],
     ["To measure the degree of dehydration",
      "The tracing does not measure volume status."],
     ["To confirm the diagnosis of ketoacidosis",
      "Diagnosis comes from the glucose, gap, and ketones."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="initial test",
   q="Which tests does the deck pair with the panel to work out the cause of hyponatraemia?",
   opts=[
     ["Serum osmolality with urine sodium and osmolality",
      "Correct — the deck's hyponatraemia pairing."],
     ["Ketones and a venous blood gas",
      "Those belong to the ketoacidosis workup."],
     ["Liver ultrasound and cystatin C",
      "Those belong to the liver and kidney lines."],
     ["A complete blood count and inflammatory markers",
      "Not what the deck pairs for this problem."]],
   c=0, cite=c(24)),

 dict(topic="Correlation", io=IOH, slot="education",
   q="What general lesson do the speaker notes draw about chemistry results?",
   opts=[
     ["A lab value narrows the differential and directs the next test rather than being diagnostic by itself",
      "Correct — the notes' point-of-care lesson."],
     ["A lab value is diagnostic once it falls outside the reference range",
      "The notes argue the opposite."],
     ["A lab value should always be confirmed by imaging before acting",
      "Imaging follows only where the notes indicate it."],
     ["A lab value is only useful when the whole panel is abnormal",
      "The notes make no such claim."]],
   c=0, cite=cn(24)),

 # ---- the vomiting case ----
 dict(topic="Vomiting case", io=IOF, slot="test finding",
   q="In the deck's case of three days of intractable vomiting, what does the panel show?",
   opts=[
     ["Low sodium, low potassium, low chloride, and a raised bicarbonate with alkalaemia",
      "Correct — the pattern the deck prints for the case."],
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
      "Correct — the deck's explanation for why the alkalosis is maintained."],
     ["The lungs retain carbon dioxide to compensate",
      "That would be a respiratory response, not the deck's mechanism."],
     ["The liver stops clearing bicarbonate from the blood",
      "The liver has no such role here."],
     ["Ongoing loss of gastric acid is the only factor",
      "The deck's point is that renal handling maintains it after the loss."]],
   c=0, cite=c(27)),

 dict(topic="Vomiting case", io=IOF, slot="first-line",
   q="What corrects the alkalosis in the vomiting case?",
   opts=[
     ["Replacing sodium, chloride, and potassium with saline and potassium chloride",
      "Correct — the deck states that only replacing all three corrects it."],
     ["Giving intravenous bicarbonate",
      "The bicarbonate is already high; adding more would worsen the alkalosis."],
     ["Giving an antiemetic alone",
      "Stopping the vomiting does not itself reverse the depletion driving the alkalosis."],
     ["Restricting fluid intake",
      "Volume depletion is part of what maintains the alkalosis."]],
   c=0, cite=c(27)),

 dict(topic="Vomiting case", io=IOF, slot="education",
   q="What do the speaker notes say the vomiting case illustrates?",
   opts=[
     ["That electrolytes and acid-base cannot be separated",
      "Correct — the notes call it the single best illustration of that point."],
     ["That a single electrolyte can be interpreted on its own",
      "The notes argue the opposite."],
     ["That vomiting is the commonest cause of alkalosis",
      "Frequency is not the point the notes draw."],
     ["That imaging is required before treating an electrolyte disorder",
      "The notes do not raise imaging here."]],
   c=0, cite=cn(27)),
]
