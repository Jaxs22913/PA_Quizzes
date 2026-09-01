# -*- coding: utf-8 -*-
# PDM I Lecture 6 (Urinalysis, Prof. Stacie Gopal) -- pool C.
# Bilirubin, protein, and specific gravity. Syllabus objective a.
#
# SLIDE 30 IS A TABLE INSIDE A GRAPHIC FRAME, not body text. Extracting shape
# text alone returns two stray lines and loses the whole thing; it is really a
# four-mechanism breakdown of proteinuria. Read with a table-aware extractor.
# Its last cell carries the point she repeated at 39:52 -- reagent strips are
# insensitive to Bence Jones proteins, so a dipstick is not how myeloma is
# found, and urine protein electrophoresis is.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "6. Urinalysis Diagnostics SV Gopal Fall 2026.pptx"
def c(n):  return f"{SRC}, Slide {n}"
def ct(n): return f"{SRC}, Slide {n} (table)"
def au(t): return f"Lecture recording, 1 September 2026, {t}"

IOA = "a — Describe the following urinalysis parameters"

POOL_C = [
 dict(topic="Bilirubin", io=IOA, slot="mechanism",
   q="Which form of bilirubin appears in urine, and why?",
   opts=[
     ["Conjugated, because it is water soluble",
      "Correct — only the conjugated form dissolves in urine."],
     ["Unconjugated, because it is bound to albumin",
      "Albumin-bound bilirubin does not pass into the urine."],
     ["Both forms equally",
      "Only one of the two is water soluble."],
     ["Neither, since bilirubin is cleared entirely in bile",
      "Conjugated bilirubin does reach the urine in disease."]],
   c=0, cite=c(27)),

 dict(topic="Bilirubin", io=IOA, slot="interpretation",
   q="Bilirubin is found in the urine. Where does the problem lie?",
   opts=[
     ["After conjugation in the liver, or in the biliary tract",
      "Correct — bilirubinuria points downstream of conjugation."],
     ["Before conjugation, in the breakdown of red cells",
      "That raises the unconjugated form, which does not enter urine."],
     ["In the renal tubules' handling of protein",
      "Tubular protein handling is a separate question."],
     ["In the concentrating ability of the kidney",
      "That is what specific gravity reports."]],
   c=0, cite=c(27)),

 dict(topic="Bilirubin", io=IOA, slot="interpretation",
   q="Why is bilirubinuria valuable as a screening finding?",
   opts=[
     ["It can appear several days before the patient looks jaundiced",
      "Correct — it can precede visible jaundice."],
     ["It confirms the cause of the liver disease",
      "It flags the problem without naming the cause."],
     ["It distinguishes hepatitis from cirrhosis",
      "It does not separate one liver disease from another."],
     ["It rules out biliary obstruction",
      "Obstruction is one of the things that produces it."]],
   c=0, cite=c(27)),

 dict(topic="Bilirubin", io=IOA, slot="interpretation",
   q="Which conditions produce bilirubin in the urine?",
   opts=[
     ["Hepatitis, cirrhosis, cancer, or gallstones obstructing the biliary tract",
      "Correct — hepatic and biliary disease both do it."],
     ["Rhabdomyolysis and crush injury",
      "Those give a positive blood pad through myoglobin."],
     ["Urinary tract infection with Proteus",
      "Infection does not produce bilirubinuria."],
     ["Diabetes insipidus",
      "That produces dilute urine rather than bilirubinuria."]],
   c=0, cite=c(27)),

 dict(topic="Protein", io=IOA, slot="mechanism",
   q="Which protein does the dipstick mainly detect, and what does it report on?",
   opts=[
     ["Albumin, reporting on glomerular and tubular function",
      "Correct — albumin is the protein, and both are what it reflects."],
     ["Immunoglobulin, reporting on immune activity",
      "Immunoglobulin light chains are poorly detected by the pad."],
     ["Hemoglobin, reporting on red cell breakdown",
      "Hemoglobin registers on the blood pad."],
     ["Myoglobin, reporting on muscle injury",
      "Myoglobin also registers on the blood pad."]],
   c=0, cite=c(28)),

 dict(topic="Protein", io=IOA, slot="limitation",
   q="Which more accurate test follows a positive protein dipstick?",
   opts=[
     ["A twenty-four hour urine collection",
      "Correct — collecting over a day measures it far better than an estimate."],
     ["A repeat dipstick the following morning",
      "Repeating the same estimate does not improve on it."],
     ["A urine culture and sensitivity",
      "Culture answers a question about infection."],
     ["Renal ultrasound",
      "Imaging does not quantify protein loss."]],
   c=0, cite=c(28)),

 dict(topic="Protein", io=IOA, slot="interpretation",
   q="In which three situations can a trace of protein be normal?",
   opts=[
     ["Pregnancy, fever, and strenuous exercise",
      "Correct — functional proteinuria covers all three."],
     ["Dehydration, fasting, and sleep",
      "None of these three is the recognised functional cause."],
     ["Infection, inflammation, and malignancy",
      "Those are pathological causes rather than normal ones."],
     ["Contrast administration, diuresis, and overhydration",
      "Those change concentration rather than causing functional protein loss."]],
   c=0, cite=c(28)),

 dict(topic="Protein", io=IOA, slot="limitation",
   q="What causes a false positive on the protein pad?",
   opts=[
     ["Contamination with prostatic or vaginal secretions",
      "Correct — contamination is the recognised false positive."],
     ["Refrigeration of the specimen",
      "Refrigeration is how a specimen is properly held."],
     ["A high fluid intake before collection",
      "Dilution lowers rather than falsely raises the reading."],
     ["Reading the pad after ten minutes",
      "Late reading is an error but not the recognised false positive here."]],
   c=0, cite=c(28)),

 dict(topic="Protein", io=IOA, slot="mechanism",
   q="Protein is normally reabsorbed where?",
   opts=[
     ["In the renal tubules",
      "Correct — tubular disease therefore leaves protein in the urine."],
     ["In the glomerulus",
      "The glomerulus filters; the tubules reabsorb."],
     ["In the collecting duct only",
      "Reabsorption of protein is a tubular function more broadly."],
     ["In the bladder wall",
      "The bladder stores urine and does not reabsorb protein."]],
   c=0, cite=c(29)),

 dict(topic="Protein", io=IOA, slot="interpretation",
   q="Persistent proteinuria is best understood as what?",
   opts=[
     ["A significant sign of renal disease",
      "Correct — persistence is what makes it significant."],
     ["A normal variant in most adults",
      "Only a transient trace is normal, not persistent protein."],
     ["Proof of nephrotic syndrome",
      "Nephrotic syndrome sits at the massive end rather than being proven by any protein."],
     ["Evidence of urinary tract infection",
      "Infection shows on other pads."]],
   c=0, cite=c(29)),

 dict(topic="Protein", io=IOA, slot="interpretation",
   q="Which mechanism links multiple myeloma to protein in the urine?",
   opts=[
     ["Overflow from raised plasma protein levels",
      "Correct — the excess in plasma spills into the urine."],
     ["Glomerular damage from immune complex deposition",
      "The mechanism here is overflow rather than glomerular injury."],
     ["Diminished tubular reabsorption after infection",
      "That is a separate mechanism from overflow."],
     ["Transient protein loss after exercise",
      "That is the functional, benign category."]],
   c=0, cite=ct(30)),

 dict(topic="Protein", io=IOA, slot="limitation",
   q="Why should a reagent strip not be used to look for Bence Jones proteins?",
   opts=[
     ["Reagent strips are insensitive to them",
      "Correct — the pad does not pick them up."],
     ["Reagent strips over-report them, giving false positives",
      "The problem is failure to detect, not over-reporting."],
     ["They appear only in serum, never in urine",
      "They do reach the urine; the pad simply misses them."],
     ["They are detected only after the urine is refrigerated",
      "Refrigeration does not change what the pad can detect."]],
   c=0, cite=ct(30)),

 dict(topic="Protein", io=IOA, slot="next step",
   q="Bence Jones proteins are suspected. Which test identifies them?",
   opts=[
     ["Urine protein electrophoresis",
      "Correct — electrophoresis is what finds them."],
     ["A reagent strip read by an automated reader",
      "The pad is insensitive to them however it is read."],
     ["Urine culture and sensitivity",
      "Culture looks for organisms, not proteins."],
     ["Microscopic examination of the sediment",
      "Sediment microscopy does not identify light chains."]],
   c=0, cite=au("40:09")),

 dict(topic="Protein", io=IOA, slot="limitation",
   q="How specific is a finding of protein in the urine?",
   opts=[
     ["It is not specific to any one condition",
      "Correct — many conditions produce it."],
     ["It is specific for nephrotic syndrome",
      "Nephrotic syndrome is one of many causes."],
     ["It is specific for glomerular rather than tubular disease",
      "Both glomerular and tubular disease produce it."],
     ["It is specific for preeclampsia in a pregnant patient",
      "It is present in preeclampsia but is not diagnostic of it."]],
   c=0, cite=au("37:33")),

 dict(topic="Specific gravity", io=IOA, slot="mechanism",
   q="What does specific gravity measure?",
   opts=[
     ["The weight of solutes in urine against an equal volume of water",
      "Correct — it is a ratio of weights."],
     ["The number of particles per litre of urine",
      "It weighs the solutes rather than counting them."],
     ["The osmotic pressure the urine exerts",
      "That is osmolality, a related but different measure."],
     ["The volume of urine produced per hour",
      "Volume is not what specific gravity reports."]],
   c=0, cite=c(31)),

 dict(topic="Specific gravity", io=IOA, slot="mechanism",
   q="Which renal ability does specific gravity estimate?",
   opts=[
     ["The concentrating and excretory ability of the kidneys",
      "Correct — it reports how well urine can be concentrated."],
     ["The filtration rate across the glomerulus",
      "Filtration rate is estimated a different way."],
     ["The tubules' handling of hydrogen ions",
      "That is what the pH reports."],
     ["The integrity of the glomerular basement membrane",
      "Protein loss is the marker of that."]],
   c=0, cite=c(31)),

 dict(topic="Specific gravity", io=IOA, slot="limitation",
   q="Why does radiographic contrast material raise the specific gravity so sharply?",
   opts=[
     ["Its particles are large, and particle size affects the measurement",
      "Correct — bigger particles weigh more."],
     ["It binds water and reduces urine volume",
      "The effect is from particle size rather than volume."],
     ["It is excreted as protein",
      "Contrast is not protein."],
     ["It alters the urine pH, which the pad reads as density",
      "The pads are independent; pH does not drive specific gravity."]],
   c=0, cite=c(31)),

 dict(topic="Specific gravity", io=IOA, slot="interpretation",
   q="Which of these produces a LOW specific gravity?",
   opts=[
     ["Diabetes insipidus",
      "Correct — less antidiuretic hormone means more water in the urine."],
     ["Dehydration",
      "Dehydration concentrates the urine and raises it."],
     ["The syndrome of inappropriate antidiuretic hormone",
      "More antidiuretic hormone means less water and a higher reading."],
     ["Heart failure",
      "Reduced renal blood flow concentrates the urine."]],
   c=0, cite=c(32)),

 dict(topic="Specific gravity", io=IOA, slot="interpretation",
   q="Which of these produces a HIGH specific gravity?",
   opts=[
     ["The syndrome of inappropriate antidiuretic hormone",
      "Correct — more antidiuretic hormone leaves less water in the urine."],
     ["Overhydration",
      "That dilutes the urine."],
     ["Diuresis",
      "Diuresis dilutes the urine."],
     ["Chronic kidney disease with loss of concentrating ability",
      "That gives a low reading."]],
   c=0, cite=c(32)),

 dict(topic="Specific gravity", io=IOA, slot="interpretation",
   q="Which of these lowers the specific gravity through the kidney's own failure to concentrate?",
   opts=[
     ["Chronic kidney disease",
      "Correct — glomerulonephritis, tubular damage, and renal failure all cost concentrating ability."],
     ["Heart failure",
      "That reduces renal blood flow and concentrates the urine."],
     ["Hypotension",
      "Reduced perfusion concentrates the urine."],
     ["Renal artery stenosis",
      "Reduced flow concentrates the urine."]],
   c=0, cite=c(32)),

 dict(topic="Microscopic urinalysis", io=IOA, slot="next step",
   q="Which additional elements does a microscopic urinalysis report?",
   opts=[
     ["White cells, red cells, squamous epithelial cells, casts, and crystals",
      "Correct — those are the sediment findings."],
     ["Only bacteria and yeast",
      "Organisms are part of it, but the sediment carries more."],
     ["Only casts and crystals",
      "Cells are reported as well."],
     ["The same nine analytes as the dipstick, measured precisely",
      "Microscopy reports different elements rather than remeasuring the pads."]],
   c=0, cite=c(33)),

 dict(topic="Bacteria", io=IOA, slot="interpretation",
   q="Which finding makes bacteria in a specimen more likely to be significant?",
   opts=[
     ["Raised white cells with a positive leukocyte esterase",
      "Correct — bacteria alongside pyuria point to real infection."],
     ["More than twenty squamous epithelial cells per high power field",
      "Squamous cells suggest contamination instead."],
     ["Collection from a longstanding indwelling catheter",
      "That suggests colonisation rather than acute infection."],
     ["A specimen that has stood at room temperature overnight",
      "Standing allows overgrowth and makes the result less reliable."]],
   c=0, cite=c(34)),

 dict(topic="Bacteria", io=IOA, slot="limitation",
   q="More than twenty squamous epithelial cells per high power field are seen. How should the specimen be read?",
   opts=[
     ["It is likely contaminated",
      "Correct — that many squamous cells points to contamination."],
     ["It confirms pyelonephritis",
      "Squamous cells do not point to upper tract infection."],
     ["It confirms cystitis",
      "They suggest the specimen is contaminated rather than infected."],
     ["It indicates glomerular disease",
      "Glomerular disease is not marked by squamous cells."]],
   c=0, cite=c(34)),

 dict(topic="Bacteria", io=IOA, slot="next step",
   q="What is needed for a definitive diagnosis when bacteria are seen?",
   opts=[
     ["Gram stain and culture",
      "Correct — both are required to identify the organism definitively."],
     ["A repeat dipstick",
      "The dipstick does not identify organisms."],
     ["Renal ultrasound",
      "Imaging does not identify an organism."],
     ["A twenty-four hour urine collection",
      "That quantifies protein rather than identifying bacteria."]],
   c=0, cite=c(34)),
]
