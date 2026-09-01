# -*- coding: utf-8 -*-
# PDM I Lecture 6 (Urinalysis, Prof. Stacie Gopal) -- pool E.
# Objective c: correlating urinalysis findings with clinical presentations.
# Written in Reynolds' stated house style for this course -- a short vignette
# ending in "what is the next test" or "how do you read this" rather than
# "name the disease".
#
# THE CASE SHE WORKED THROUGH IS NOT ON THE SLIDE. Slide 35 poses a 28-year-old
# with dysuria, frequency and urgency; slide 36 is meant to hold the answer and
# is a picture of a dipstick chart with three floating "x" shapes and no text
# beyond them. The x's have no labels, so which analytes they mark was resolved
# from their coordinates against the picture's own extent -- rows 1, 2 and 6 of
# ten, i.e. LEUKOCYTES, NITRITE and BLOOD. That agrees with what she read out
# at 49:12 ("leukocytes and blood") plus the third mark, and with the negatives
# she listed at 49:21 (glucose, bilirubin, ketones, protein).
#
# THE RECORDING STOPS MID-SENTENCE at 49:41, part-way through her explanation
# of why the picture fits a urinary tract infection. Nothing here depends on
# what came after the cut.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "6. Urinalysis Diagnostics SV Gopal Fall 2026.pptx"
def c(n):  return f"{SRC}, Slide {n}"
def cg(n): return f"{SRC}, Slide {n} (marks resolved by position)"
def au(t): return f"Lecture recording, 1 September 2026, {t}"

IOC = "c — Correlate urinalysis findings with common clinical presentations"

POOL_E = [
 dict(topic="Suspected urinary tract infection", io=IOC, slot="next step",
   q="A 28-year-old woman has two days of dysuria, frequency, and urgency with mild suprapubic tenderness. She is afebrile with no flank pain. What is the next step?",
   opts=[
     ["Urinalysis",
      "Correct — it is quick, non-invasive, and answers the question in front of you."],
     ["Renal ultrasound",
      "Imaging is not the first move in an uncomplicated lower tract presentation."],
     ["Computed tomography of the abdomen and pelvis",
      "Far beyond what this presentation calls for."],
     ["Serum creatinine and blood urea nitrogen alone",
      "Those assess renal function rather than answering the infection question."]],
   c=0, cite=c(35)),

 dict(topic="Suspected urinary tract infection", io=IOC, slot="interpretation",
   q="A woman with dysuria and frequency has a dipstick positive for leukocyte esterase, nitrites, and blood, with glucose, bilirubin, ketones, and protein all negative. How is this read?",
   opts=[
     ["It fits a urinary tract infection",
      "Correct — pyuria with nitrites and blood, and nothing pointing elsewhere."],
     ["It fits diabetic ketoacidosis",
      "Glucose and ketones would be positive."],
     ["It fits nephrotic syndrome",
      "Protein would be heavily positive."],
     ["It fits biliary obstruction",
      "Bilirubin would be positive."]],
   c=0, cite=cg(36)),

 dict(topic="Suspected urinary tract infection", io=IOC, slot="interpretation",
   q="In a patient with cystitis, which negative dipstick results help to rule other things out?",
   opts=[
     ["Glucose, ketones, bilirubin, and protein",
      "Correct — their absence points away from metabolic, hepatic, and glomerular causes."],
     ["Specific gravity and pH",
      "Both always carry a value rather than being negative."],
     ["Leukocyte esterase and nitrites",
      "Those are the positives that support the diagnosis."],
     ["Blood and leukocyte esterase",
      "Both are positive in this picture."]],
   c=0, cite=au("49:21")),

 dict(topic="Suspected urinary tract infection", io=IOC, slot="next step",
   q="A dipstick supports a urinary tract infection. What identifies the organism and what will treat it?",
   opts=[
     ["Urine culture and sensitivity",
      "Correct — culture names the organism and sensitivity picks the agent."],
     ["Gram stain of the urine alone",
      "A stain narrows the field but does not give sensitivities."],
     ["A repeat dipstick after treatment",
      "That does not identify anything."],
     ["Blood cultures",
      "Those are for suspected bloodstream infection."]],
   c=0, cite=c(34)),

 dict(topic="Suspected urinary tract infection", io=IOC, slot="interpretation",
   q="A patient has clear symptoms of cystitis, positive leukocyte esterase, and negative nitrites. How should the negative nitrite be treated?",
   opts=[
     ["As unhelpful for excluding infection, since Escherichia coli rarely turns it positive",
      "Correct — the commonest organism does not produce nitrites."],
     ["As excluding infection, so no culture is needed",
      "It does not exclude infection."],
     ["As indicating a fungal rather than bacterial cause",
      "A negative nitrite says nothing about fungal infection."],
     ["As indicating the specimen was contaminated",
      "Contamination is not what a negative nitrite shows."]],
   c=0, cite=au("24:21")),

 dict(topic="Suspected urinary tract infection", io=IOC, slot="limitation",
   q="A toddler is being assessed for a urinary tract infection and the nitrite pad is negative. What limits that result here?",
   opts=[
     ["Young children void too frequently for nitrates to convert",
      "Correct — the conversion needs urine to sit in the bladder."],
     ["The pad cannot be used under the age of five",
      "It can be used; the interval between voids is the limitation."],
     ["Children produce no urinary nitrates",
      "Nitrates are present; the time to convert them is what is short."],
     ["Paediatric specimens must be refrigerated first",
      "Refrigeration is not the issue here."]],
   c=0, cite=c(20)),

 dict(topic="Uncontrolled diabetes", io=IOC, slot="interpretation",
   q="A patient with sweet-smelling urine has ketones and glucose on the dipstick. Which picture does that fit?",
   opts=[
     ["Uncontrolled diabetes mellitus",
      "Correct — glucose spilling with ketones from fatty acid metabolism."],
     ["A simple urinary tract infection",
      "That gives pyuria and nitrites rather than glucose and ketones."],
     ["Rhabdomyolysis",
      "That gives a positive blood pad with a raised creatine phosphokinase."],
     ["Biliary obstruction",
      "That gives bilirubin in the urine."]],
   c=0, cite=c(9)),

 dict(topic="Uncontrolled diabetes", io=IOC, slot="interpretation",
   q="A patient with ketonuria has a normal blood glucose and reports not eating for two days. What explains the ketones?",
   opts=[
     ["Starvation",
      "Correct — fasting drives fatty acid metabolism just as insulin deficiency does."],
     ["Uncontrolled diabetes mellitus",
      "The blood glucose is normal, which does not fit."],
     ["A urinary tract infection",
      "Infection does not produce ketones."],
     ["Overhydration",
      "That dilutes the urine without producing ketones."]],
   c=0, cite=c(21)),

 dict(topic="Liver and biliary disease", io=IOC, slot="interpretation",
   q="A patient has dark yellow-brown urine and bilirubin on the dipstick but is not yet jaundiced. How should that be read?",
   opts=[
     ["It may be an early sign of liver disease, before jaundice appears",
      "Correct — bilirubinuria can precede visible jaundice by days."],
     ["It rules out liver disease, since the patient is not jaundiced",
      "The absence of jaundice does not exclude it."],
     ["It indicates dehydration",
      "Dehydration darkens the urine without adding bilirubin."],
     ["It indicates a urinary tract infection",
      "Infection does not put bilirubin in the urine."]],
   c=0, cite=c(27)),

 dict(topic="Rhabdomyolysis", io=IOC, slot="next step",
   q="A patient is found after several hours trapped under a fallen beam. The dipstick is positive for blood but no red cells are seen. Which test confirms the source?",
   opts=[
     ["Serum creatine phosphokinase",
      "Correct — a raised level points to muscle as the source."],
     ["Serum unconjugated bilirubin",
      "That would point to red cell destruction instead."],
     ["Urine culture and sensitivity",
      "Culture does not address the source of heme."],
     ["A twenty-four hour urine protein collection",
      "Quantifying protein does not identify the source of heme."]],
   c=0, cite=c(26)),

 dict(topic="Nephrotic syndrome", io=IOC, slot="interpretation",
   q="A patient has heavy protein on the dipstick and foamy urine. Which finding on inspection matched the pad?",
   opts=[
     ["The foam",
      "Correct — foaming is associated with protein."],
     ["The colour",
      "Colour points to concentration, bilirubin, or blood."],
     ["The odour",
      "Odour points to infection or ketones."],
     ["The transparency",
      "Turbidity points to cells, organisms, or crystals."]],
   c=0, cite=c(8)),

 dict(topic="Nephrotic syndrome", io=IOC, slot="next step",
   q="A dipstick shows heavy proteinuria. Which test quantifies it properly?",
   opts=[
     ["A twenty-four hour urine collection",
      "Correct — it measures the loss far more accurately than an estimate."],
     ["A repeat dipstick with an automated reader",
      "The reader improves accuracy but still gives an estimate."],
     ["Urine culture and sensitivity",
      "Culture answers a question about infection."],
     ["Serum creatinine alone",
      "That assesses function rather than quantifying the protein lost."]],
   c=0, cite=c(28)),

 dict(topic="Multiple myeloma", io=IOC, slot="next step",
   q="An older patient has bone pain, anemia, and a raised total protein, but the urine dipstick protein is negative. What should be done?",
   opts=[
     ["Send urine protein electrophoresis, since the pad misses Bence Jones proteins",
      "Correct — a negative pad does not exclude light chains."],
     ["Accept the negative pad as excluding urinary protein loss",
      "The pad is insensitive to the protein in question."],
     ["Repeat the dipstick on a first-morning specimen",
      "Timing does not change what the pad can detect."],
     ["Send a urine culture and sensitivity",
      "Culture answers an infection question."]],
   c=0, cite=au("40:09")),

 dict(topic="Diabetes insipidus", io=IOC, slot="interpretation",
   q="A patient passes large volumes of very dilute urine with a low specific gravity. Which condition fits?",
   opts=[
     ["Diabetes insipidus",
      "Correct — reduced antidiuretic hormone leaves more water in the urine."],
     ["The syndrome of inappropriate antidiuretic hormone",
      "That concentrates the urine instead."],
     ["Dehydration",
      "Dehydration concentrates the urine."],
     ["Heart failure",
      "Reduced renal blood flow concentrates the urine."]],
   c=0, cite=c(32)),

 dict(topic="Contrast administration", io=IOC, slot="interpretation",
   q="A patient's urine is turbid with a specific gravity above 1.040 shortly after an imaging study. What explains it?",
   opts=[
     ["Radiographic contrast material, whose particles are large",
      "Correct — large particles drive the reading up sharply."],
     ["Severe dehydration alone",
      "Dehydration raises it, but not to that degree."],
     ["Heavy proteinuria",
      "Protein does not raise it that far."],
     ["A urinary tract infection",
      "Infection clouds the urine without that specific gravity."]],
   c=0, cite=c(32)),

 dict(topic="Stone disease", io=IOC, slot="interpretation",
   q="A patient with recurrent stones has persistently alkaline urine and repeated infections. Which stone type does that combination suggest?",
   opts=[
     ["Struvite",
      "Correct — alkaline urine with urease-producing organisms."],
     ["Uric acid",
      "Those form in acidic urine."],
     ["Calcium oxalate",
      "Those are associated with acidic urine."],
     ["Cystine",
      "Not the type this combination points to."]],
   c=0, cite=c(18)),

 dict(topic="Specimen quality", io=IOC, slot="limitation",
   q="A specimen shows bacteria and many squamous epithelial cells but the patient has no symptoms. How should it be handled?",
   opts=[
     ["Treat it as likely contaminated rather than as infection",
      "Correct — squamous cells and no symptoms point to contamination."],
     ["Treat empirically for cystitis",
      "Treating a contaminated specimen in an asymptomatic patient is not indicated."],
     ["Send blood cultures",
      "There is nothing here to suggest bloodstream infection."],
     ["Repeat with the same collection method",
      "Repeating the same way invites the same contamination."]],
   c=0, cite=c(34)),

 dict(topic="Specimen quality", io=IOC, slot="limitation",
   q="A patient with a longstanding indwelling catheter has bacteria in the urine but no symptoms. What does that most likely represent?",
   opts=[
     ["Colonisation of the catheter rather than acute infection",
      "Correct — long-term catheters are colonised."],
     ["Acute pyelonephritis",
      "There is nothing here to suggest upper tract infection."],
     ["Contamination from the vagina",
      "The catheter is the more likely source."],
     ["Interstitial cystitis",
      "That is a chronic inflammatory condition, not bacteriuria."]],
   c=0, cite=c(34)),
]
