# -*- coding: utf-8 -*-
# PDM I Lecture 6 (Urinalysis, Prof. Stacie Gopal) -- pool A.
# What urinalysis is and when to order it; the physical examination of urine
# (colour, transparency, odour); reagent strip technique; the normal result.
# Syllabus objective a.
#
# GOPAL'S OWN TESTING RULE, from the 1 September recording at 15:08-15:43:
#   "for testing purposes, I would like you to know what a normal urinalysis
#    involves ... It's important to know that we should not find nitrites. We
#    should not find ketones. We should not find glucose. So I do want you to
#    know that. I'm not asking that you memorize ranges, okay? But I do want
#    you to know if there should just be none present at all. But for testing
#    purposes, if there's a range involved, it'll be provided for you."
# So: which analytes are normally NEGATIVE is fair to ask cold. A numeric range
# is not -- it must be supplied in the stem. Enforced in pdm_l6_partition.py.
#
# THIS DECK HAS NO SPEAKER NOTES. All 35 notes slides are empty placeholders,
# unlike Lectures 1-5. Anything not on a slide is cited to the recording.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "6. Urinalysis Diagnostics SV Gopal Fall 2026.pptx"
def c(n):  return f"{SRC}, Slide {n}"
def ci(n): return f"{SRC}, Slide {n} (image)"
def ct(n): return f"{SRC}, Slide {n} (table)"
def au(t): return f"Lecture recording, 1 September 2026, {t}"

IOA = "a — Describe the following urinalysis parameters"

POOL_A = [
 dict(topic="What urinalysis is", io=IOA, slot="initial test",
   q="What does a urinalysis examine?",
   opts=[
     ["The physical, chemical, and microscopic contents of urine",
      "Correct — all three together make up the test."],
     ["Only the chemical contents, read from a reagent strip",
      "The reagent strip is one part; inspection and microscopy are the others."],
     ["Only the microscopic sediment, after centrifugation",
      "Sediment microscopy is one component rather than the whole test."],
     ["The bacterial species present and their antibiotic sensitivities",
      "That is a urine culture and sensitivity, ordered separately."]],
   c=0, cite=c(4)),

 dict(topic="What urinalysis is", io=IOA, slot="initial test",
   q="Which two serum measurements should a urinalysis accompany when the kidneys are being evaluated?",
   opts=[
     ["Creatinine and blood urea nitrogen",
      "Correct — urinalysis complements both in a renal evaluation."],
     ["Sodium and potassium",
      "Electrolytes matter, but they are not the pair urinalysis complements here."],
     ["Alanine aminotransferase and aspartate aminotransferase",
      "Those are liver enzymes, not markers of renal function."],
     ["Calcium and phosphate",
      "Minerals shift in renal disease but are not the paired renal markers."]],
   c=0, cite=c(4)),

 dict(topic="When to order", io=IOA, slot="indication",
   q="A patient presents with abdominal, pelvic, or back pain. What does that indicate?",
   opts=[
     ["A urinalysis is indicated",
      "Correct — any of those three presentations calls for one."],
     ["A urinalysis is indicated only if there is also a fever",
      "Fever raises the concern but is not what makes the test indicated."],
     ["A urinalysis should wait until imaging returns",
      "It is inexpensive and non-invasive, so it comes early rather than last."],
     ["A urine culture should replace the urinalysis",
      "Culture follows the urinalysis rather than substituting for it."]],
   c=0, cite=c(4)),

 dict(topic="Colour", io=IOA, slot="interpretation",
   q="Urine appears pale yellow and almost colourless. What does that suggest?",
   opts=[
     ["Dilute urine",
      "Correct — the paler the urine, the more dilute it is."],
     ["Concentrated urine",
      "Concentrated urine is dark yellow or amber."],
     ["Bilirubin in the urine",
      "Bilirubin gives a yellow-brown or green colour."],
     ["Blood in the urine",
      "Blood gives a bright or dark red colour."]],
   c=0, cite=c(7)),

 dict(topic="Colour", io=IOA, slot="interpretation",
   q="Urine is yellow-brown with a green tinge. Which substance does that point to?",
   opts=[
     ["Bilirubin",
      "Correct — a yellow-brown or green colour points to bilirubin."],
     ["Hemoglobin",
      "Free hemoglobin gives a red to brown colour rather than green."],
     ["Myoglobin",
      "Myoglobin darkens the urine but does not give the green tinge."],
     ["Urea",
      "Urea is present in all urine and does not colour it this way."]],
   c=0, cite=c(7)),

 dict(topic="Colour", io=IOA, slot="patient education",
   q="A patient is prescribed a medication that will turn the urine a striking colour. What should be done?",
   opts=[
     ["Warn the patient in advance so the change does not alarm them",
      "Correct — telling them beforehand is the point of the counselling."],
     ["Stop the medication if the colour changes",
      "The colour change is an expected effect rather than a reason to stop."],
     ["Repeat the urinalysis once the colour appears",
      "Repeating adds nothing when the cause is already known."],
     ["Send the specimen for culture",
      "Culture answers a different question entirely."]],
   c=0, cite=au("3:05")),

 dict(topic="Transparency", io=IOA, slot="interpretation",
   q="How is urine transparency graded once it is no longer clear?",
   opts=[
     ["Hazy, then cloudy, then turbid",
      "Correct — that is the order of increasing opacity."],
     ["Turbid, then cloudy, then hazy",
      "That reverses the scale."],
     ["Trace, then one plus, then two plus",
      "Those grades belong to semi-quantitative reagent strip results."],
     ["Mild, then moderate, then severe",
      "Transparency is not graded on that scale."]],
   c=0, cite=c(8)),

 dict(topic="Transparency", io=IOA, slot="interpretation",
   q="Urine is noted to be foamy. Which finding does that suggest?",
   opts=[
     ["Proteinuria",
      "Correct — foam is associated with protein in the urine."],
     ["Glucosuria",
      "Glucose does not make urine foam."],
     ["Ketonuria",
      "Ketones give a sweet odour rather than foam."],
     ["Bilirubinuria",
      "Bilirubin colours the urine rather than making it foam."]],
   c=0, cite=c(8)),

 dict(topic="Transparency", io=IOA, slot="interpretation",
   q="Which of these makes urine turbid?",
   opts=[
     ["White cells, red cells, bacteria, yeast, crystals, mucus, or fat",
      "Correct — any of these will cloud the specimen."],
     ["A high urea concentration alone",
      "Urea is dissolved and does not cloud the specimen."],
     ["Dilution with a large water intake",
      "Dilute urine is paler, not more turbid."],
     ["Refrigeration before analysis",
      "Refrigeration preserves the specimen rather than clouding it."]],
   c=0, cite=c(8)),

 dict(topic="Odour", io=IOA, slot="interpretation",
   q="What is the normal odour of urine described as?",
   opts=[
     ["Aromatic",
      "Correct — that is the term used for the normal odour."],
     ["Odourless",
      "Normal urine has a faint odour rather than none."],
     ["Ammonia-like",
      "An ammonia odour means urea has been broken down by bacteria."],
     ["Sweet",
      "A sweet odour points to ketones."]],
   c=0, cite=c(9)),

 dict(topic="Odour", io=IOA, slot="specimen handling",
   q="A specimen collected two hours ago smells strongly of ammonia. What explains it?",
   opts=[
     ["Urea has been broken down by bacteria while the sample stood",
      "Correct — standing lets bacteria decompose the urea."],
     ["The patient is in ketoacidosis",
      "Ketoacidosis gives a fruity or sweet odour."],
     ["There is a connection between bowel and bladder",
      "That gives a faecal odour."],
     ["The sample has been refrigerated",
      "Refrigeration prevents this change rather than causing it."]],
   c=0, cite=c(9)),

 dict(topic="Odour", io=IOA, slot="specimen handling",
   q="A specimen cannot be examined within one to two hours. How should it be kept?",
   opts=[
     ["Refrigerated, with no preservative added",
      "Correct — refrigerate it and add nothing."],
     ["At room temperature with a preservative added",
      "No preservative is added to a urinalysis specimen."],
     ["Frozen until the following day",
      "Freezing is not how the specimen is held."],
     ["Kept warm to preserve any bacteria present",
      "Warmth accelerates the decomposition that refrigeration prevents."]],
   c=0, cite=c(9)),

 dict(topic="Odour", io=IOA, slot="interpretation",
   q="Urine has a fruity, sweet odour. What does that point to?",
   opts=[
     ["Ketones",
      "Correct — a sweet acetone odour means ketones."],
     ["Bilirubin",
      "Bilirubin changes the colour rather than the odour."],
     ["Protein",
      "Protein makes the urine foam rather than smell sweet."],
     ["Nitrites",
      "Nitrites carry no characteristic odour."]],
   c=0, cite=c(9)),

 dict(topic="Odour", io=IOA, slot="interpretation",
   q="Urine has a faecal odour. Which condition should be considered?",
   opts=[
     ["A fistula between bowel and bladder",
      "Correct — an enterovesical fistula lets bowel contents reach the bladder."],
     ["A simple lower urinary tract infection",
      "Infection gives a foul odour rather than a faecal one."],
     ["Diabetic ketoacidosis",
      "That gives a sweet odour."],
     ["Dehydration",
      "Dehydration concentrates the urine without adding a faecal odour."]],
   c=0, cite=c(9)),

 dict(topic="Reagent strip technique", io=IOA, slot="specimen handling",
   q="What kind of specimen does reagent strip testing require?",
   opts=[
     ["A fresh specimen in a sterile container",
      "Correct — both the freshness and the sterile container matter."],
     ["Any specimen collected within the past day",
      "A specimen brought in from the day before is no longer fresh."],
     ["A specimen collected after a preservative is added",
      "No preservative is added."],
     ["A first-morning specimen only",
      "A fresh specimen is required; it need not be the first of the day."]],
   c=0, cite=c(11)),

 dict(topic="Reagent strip technique", io=IOA, slot="limitation",
   q="Why must the timing of a reagent strip reading be watched closely?",
   opts=[
     ["Each analyte has its own reading time",
      "Correct — the times differ from one pad to the next."],
     ["All pads must be read at exactly sixty seconds",
      "The times differ by analyte rather than sharing one interval."],
     ["The strip must be read before it touches the urine",
      "The pads have to react with the urine first."],
     ["Reading time only matters for the pH pad",
      "It matters across the analytes, not for one alone."]],
   c=0, cite=ci(36)),

 dict(topic="Reagent strip technique", io=IOA, slot="limitation",
   q="Reagent strips from different manufacturers carry different analytes in different orders. What does that mean in practice?",
   opts=[
     ["Read each strip against the chart from its own manufacturer",
      "Correct — matching the strip to its own chart keeps the reading valid."],
     ["Any colour chart may be used, since the colours are standardised",
      "The colours and their order are not standardised across manufacturers."],
     ["Strips from different manufacturers may be combined on one specimen",
      "Mixing them does not solve the problem of reading against the wrong chart."],
     ["The order of the pads has no bearing on interpretation",
      "Reading a pad against the wrong row is exactly the error to avoid."]],
   c=0, cite=c(11)),

 dict(topic="Reagent strip technique", io=IOA, slot="limitation",
   q="How should reagent strips be stored?",
   opts=[
     ["Properly desiccated, to keep them accurate",
      "Correct — they must be kept dry."],
     ["Refrigerated in a sealed bag",
      "Cold storage is not what the strips require."],
     ["In the same container as the specimen cups",
      "Storage with specimen cups does nothing to keep them dry."],
     ["Immersed in buffer until use",
      "Wetting the pads before use destroys them."]],
   c=0, cite=c(11)),

 dict(topic="Reagent strip technique", io=IOA, slot="interpretation",
   q="A reagent strip reports a result as trace, one plus, two plus, or three plus. What kind of result is that?",
   opts=[
     ["Semi-quantitative",
      "Correct — a graded estimate rather than a measured value."],
     ["Qualitative",
      "A qualitative result is simply positive or negative."],
     ["Quantitative",
      "A measured value would come from a formal laboratory assay."],
     ["Confirmatory",
      "Grading estimates the amount; it does not confirm anything."]],
   c=0, cite=c(11)),

 dict(topic="Reagent strip technique", io=IOA, slot="initial test",
   q="What does an automated reagent strip reader add?",
   opts=[
     ["Improved diagnostic accuracy",
      "Correct — the reader improves the accuracy of the reading."],
     ["The ability to identify the infecting organism",
      "Identifying an organism needs a culture."],
     ["A microscopic examination of the sediment",
      "Microscopy is a separate step."],
     ["Elimination of the need for a fresh specimen",
      "The specimen must still be fresh."]],
   c=0, cite=c(13)),

 dict(topic="Normal urinalysis", io=IOA, slot="interpretation",
   q="Which set of dipstick analytes should read negative in a healthy person?",
   opts=[
     ["Leukocyte esterase, nitrites, ketones, glucose, blood, and bilirubin",
      "Correct — all six are normally absent."],
     ["Leukocyte esterase, nitrites, and specific gravity",
      "Specific gravity always has a value; it is never simply negative."],
     ["Ketones, glucose, and pH",
      "Urine always has a pH, so it is never reported as negative."],
     ["Blood, bilirubin, and specific gravity",
      "Specific gravity is a measured ratio rather than a positive or negative."]],
   c=0, cite=c(14)),

 dict(topic="Normal urinalysis", io=IOA, slot="interpretation",
   q="Which analyte on a urinalysis is reported as a value rather than as positive or negative?",
   opts=[
     ["Specific gravity",
      "Correct — it is a ratio, so it always carries a number."],
     ["Nitrites",
      "Nitrites are reported as positive or negative."],
     ["Leukocyte esterase",
      "Leukocyte esterase is reported as positive or negative."],
     ["Bilirubin",
      "Bilirubin is reported as positive or negative."]],
   c=0, cite=c(14)),

 dict(topic="Anatomy review", io=IOA, slot="mechanism",
   q="Which two structures make up a nephron?",
   opts=[
     ["A glomerulus and a tubule",
      "Correct — those two together form the nephron."],
     ["A calyx and a collecting duct",
      "Those carry urine away rather than forming the nephron."],
     ["A renal artery and a renal vein",
      "Those are the blood supply, not the functional unit."],
     ["A cortex and a medulla",
      "Those are regions of the kidney, not parts of a nephron."]],
   c=0, cite=c(15)),

 dict(topic="Anatomy review", io=IOA, slot="mechanism",
   q="What does the glomerular basement membrane do?",
   opts=[
     ["Acts as a selective barrier, filtering water, waste, and small molecules into the tubules",
      "Correct — it selects what passes into the tubule."],
     ["Reabsorbs water and nutrients back into the blood",
      "Reabsorption happens further along, in the tubules."],
     ["Concentrates the filtrate before it reaches the glomerulus",
      "Filtrate is produced at the glomerulus rather than arriving concentrated."],
     ["Secretes hydrogen ions to control the urine pH",
      "Hydrogen ion handling belongs to the tubules."]],
   c=0, cite=c(15)),

 dict(topic="Anatomy review", io=IOA, slot="mechanism",
   q="What happens to the fluid and waste that the tubules do not reabsorb?",
   opts=[
     ["It becomes urine",
      "Correct — whatever is not reabsorbed is excreted as urine."],
     ["It returns to the glomerulus to be filtered again",
      "Filtrate moves forward through the nephron rather than back."],
     ["It is stored in the renal cortex",
      "The cortex does not store filtrate."],
     ["It is broken down by tubular enzymes",
      "The tubules reabsorb rather than digest the filtrate."]],
   c=0, cite=c(15)),
]
