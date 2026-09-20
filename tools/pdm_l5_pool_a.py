# -*- coding: utf-8 -*-
# PDM I Lecture 5 (Chemistry Panels, Renal Function, Electrolytes, Prof. Reynolds)
# -- pool A. What a chemistry panel is, what is on which panel, and when to order.
# Syllabus objectives a and g.
#
# REYNOLDS' RULES, as refined by the 26 August recording (see pdm_l5_partition.py):
#   1. A number never appears without the scale that reads it. She goes further
#      than that here -- "we ALWAYS give you reference ranges" -- so no question
#      may require a range to be recalled cold.
#   2. The no-math rule is NOT a blanket ban. She expects the anion gap to be
#      calculated. She explicitly does not want glomerular filtration rate
#      calculated ("know OF it"), and does corrected sodium with a calculator.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "5. Chemistry Panels, Renal Fxn, Elytes.pptx"
def c(n): return f"{SRC}, Slide {n}"
def ci(n): return f"{SRC}, Slide {n} (image only)"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"
def au(): return "Lecture recording, 26 August 2026"

IOA = "a — Explain the components of a chemistry panel"
IOG = "g — Discuss indications for ordering chemistry panels"

POOL_A = [
 dict(topic="What a chemistry panel is", io=IOA, slot="initial test",
   q="What does a chemistry panel measure?",
   opts=[
     ["Metabolites, electrolytes, kidney markers, and in the expanded version liver and protein markers",
      "Correct — the panel samples the plasma chemistry that the kidneys and liver regulate, so it reports on fuel, electrolyte balance and waste handling in a single draw."],
     ["Red cells, white cells, and platelets with their indices",
      "That is the complete blood count, a separate panel from Lecture 4."],
     ["Clotting factor activity and the time taken for a clot to form",
      "Prothrombin time and its ratio are coagulation studies, ordered separately."],
     ["Hormone levels from the thyroid, adrenal, and pituitary glands",
      "Endocrine assays are not part of a routine chemistry panel."]],
   c=0, cite=c(5)),

 dict(topic="What a chemistry panel is", io=IOA, slot="initial test",
   q="A chemistry panel is best described as a snapshot of which three things?",
   opts=[
     ["Chemical balance, metabolism, and organ function",
      "Correct — the panel captures a single moment, showing whether the internal chemical environment is balanced, whether fuel is being handled normally, and whether the organs that maintain both are working."],
     ["Infection, inflammation, and immune response",
      "None of the three is assessed by a chemistry panel."],
     ["Oxygen delivery, oxygen consumption, and tissue perfusion",
      "Those come from blood gases and haemodynamic measures."],
     ["Nutrition, hydration, and body composition",
      "Only hydration is touched, and only indirectly."]],
   c=0, cite=c(5)),

 dict(topic="Basic metabolic panel", io=IOA, slot="initial test",
   q="How many tests are on a basic metabolic panel?",
   opts=[
     ["Eight", "Correct — the basic panel is eight tests: glucose, calcium, the four electrolytes, and the two kidney markers."],
     ["Seven", "Seven is the older chem-7, which leaves calcium off."],
     ["Twelve", "Twelve is a chem-12, an intermediate panel."],
     ["Fourteen", "Fourteen is the comprehensive metabolic panel."]],
   c=0, cite=c(7)),

 dict(topic="Basic metabolic panel", io=IOA, slot="initial test",
   q="Which eight tests make up the basic metabolic panel?",
   opts=[
     ["Glucose, calcium, sodium, potassium, chloride, carbon dioxide, blood urea nitrogen, and creatinine",
      "Correct — one fuel marker, one mineral, four electrolytes with acid-base, and two waste products, giving a survey of metabolism, balance and renal clearance."],
     ["Glucose, calcium, sodium, potassium, chloride, albumin, blood urea nitrogen, and creatinine",
      "Albumin is one of the six the comprehensive panel adds."],
     ["Glucose, magnesium, sodium, potassium, chloride, carbon dioxide, blood urea nitrogen, and creatinine",
      "Magnesium is not on the panel; Reynolds said outright it would not be covered."],
     ["Glucose, calcium, sodium, potassium, phosphate, carbon dioxide, blood urea nitrogen, and creatinine",
      "Phosphate is not one of the eight; chloride is the anion measured."]],
   c=0, cite=c(7)),

 dict(topic="Basic metabolic panel", io=IOA, slot="initial test",
   q="What distinguishes a chem-7 from a chem-8?",
   opts=[
     ["A chem-8 includes calcium and a chem-7 does not",
      "Correct — calcium is the difference between the two older names."],
     ["A chem-8 includes albumin and a chem-7 does not",
      "Albumin belongs to the comprehensive panel, not to either chem-7 or chem-8."],
     ["A chem-8 includes magnesium and a chem-7 does not",
      "Magnesium is not on either panel."],
     ["A chem-8 includes bicarbonate and a chem-7 does not",
      "Bicarbonate, reported as carbon dioxide, is on both."]],
   c=0, cite=c(6)),

 dict(topic="Comprehensive metabolic panel", io=IOA, slot="initial test",
   q="What does a comprehensive metabolic panel add to a basic metabolic panel?",
   opts=[
     ["Six markers of liver function and protein status",
      "Correct — the comprehensive panel is the basic panel plus six liver and protein tests."],
     ["Six markers of kidney function and acid-base status",
      "Kidney and acid-base markers are already on the basic panel."],
     ["Four markers of bone turnover and mineral balance",
      "Only calcium is a mineral measure, and it is on the basic panel."],
     ["Three markers of muscle injury and two of cardiac strain",
      "Those are separate assays and are on neither panel."]],
   c=0, cite=c(6)),

 dict(topic="Comprehensive metabolic panel", io=IOA, slot="initial test",
   q="Which six tests does the comprehensive metabolic panel add?",
   opts=[
     ["Albumin, total protein, alkaline phosphatase, alanine transaminase, aspartate aminotransferase, and bilirubin",
      "Correct — two synthetic products, two markers of hepatocyte injury, one of cholestasis, and one of conjugation and excretion, which together cover both what the liver makes and whether it is damaged."],
     ["Albumin, total protein, alkaline phosphatase, lactate dehydrogenase, ammonia, and bilirubin",
      "Lactate dehydrogenase and ammonia are separate orders, not part of the panel."],
     ["Albumin, prealbumin, gamma-glutamyl transferase, alanine transaminase, aspartate aminotransferase, and bilirubin",
      "Prealbumin and gamma-glutamyl transferase are add-on tests rather than panel components."],
     ["Globulin, total protein, alkaline phosphatase, alanine transaminase, aspartate aminotransferase, and ammonia",
      "Globulin is calculated rather than measured, and ammonia is not on the panel."]],
   c=0, cite=c(7)),

 dict(topic="Comprehensive metabolic panel", io=IOA, slot="initial test",
   q="What is the other common name for the comprehensive metabolic panel?",
   opts=[
     ["Chem-14", "Correct — the panels are commonly named for the number of tests they carry, and the comprehensive panel holds fourteen."],
     ["Chem-8", "Chem-8 is the basic panel including calcium."],
     ["Chem-20", "Chem-20 is not one of the panel names in use here; the comprehensive panel is the chem-14."],
     ["Chem-10", "The panels in use are the chem-7, chem-8, chem-12 and chem-14; the comprehensive panel is the last of these."]],
   c=0, cite=c(7)),

 dict(topic="Choosing a panel", io=IOG, slot="initial test",
   q="A clinician wants a fuller picture of a patient's liver and nutritional protein status. Which panel is indicated?",
   opts=[
     ["A comprehensive metabolic panel",
      "Correct — albumin and total protein report nutritional and synthetic status, and the transaminases, alkaline phosphatase and bilirubin report liver injury, and none of the six is on the basic panel."],
     ["A basic metabolic panel",
      "The basic panel carries no liver or protein markers at all."],
     ["A chem-7", "A chem-7 is a basic panel without even calcium."],
     ["A complete blood count",
      "That reports cell lines, not liver or protein markers."]],
   c=0, cite=cn(7)),

 dict(topic="Choosing a panel", io=IOG, slot="initial test",
   q="For which purpose does a basic metabolic panel suffice?",
   opts=[
     ["Electrolytes, glucose, and renal screening",
      "Correct — the eight tests cover fuel, the four electrolytes with acid-base, and the two waste markers, which is enough to answer questions about balance, glucose and renal clearance."],
     ["Liver injury and synthetic function",
      "Neither is measurable without the six comprehensive-panel additions."],
     ["Nutritional protein status",
      "Albumin and total protein are on the comprehensive panel only."],
     ["Cholestasis and biliary obstruction",
      "Alkaline phosphatase and bilirubin are comprehensive-panel tests."]],
   c=0, cite=cn(7)),

 dict(topic="Panel groupings", io=IOA, slot="initial test",
   q="Under the functional grouping of panel components, which group do blood urea nitrogen and creatinine belong to?",
   opts=[
     ["Kidney function and waste",
      "Correct — both are nitrogenous waste products cleared by glomerular filtration, so their accumulation reports directly on how well the kidney is clearing."],
     ["Electrolytes and acid-base",
      "That group holds sodium, potassium, chloride, and bicarbonate."],
     ["Metabolic and fuel",
      "That group holds glucose alone."],
     ["Liver and protein",
      "That group is the six the comprehensive panel adds."]],
   c=0, cite=c(7)),

 dict(topic="Panel groupings", io=IOA, slot="initial test",
   q="Which four panel components make up the electrolytes and acid-base group?",
   opts=[
     ["Sodium, potassium, chloride, and bicarbonate",
      "Correct — these four carry almost all the charge in extracellular fluid, and because charge must balance, a shift in any one is reflected in the others."],
     ["Sodium, potassium, calcium, and chloride",
      "Calcium is grouped separately as the mineral."],
     ["Sodium, chloride, bicarbonate, and glucose",
      "Glucose is the metabolic and fuel group on its own."],
     ["Potassium, chloride, bicarbonate, and creatinine",
      "Creatinine belongs to the kidney function group."]],
   c=0, cite=c(7)),

 dict(topic="Panel groupings", io=IOA, slot="initial test",
   q="Where does calcium sit in the grouping of panel components?",
   opts=[
     ["On its own, as the mineral",
      "Correct — calcium is grouped by itself as the mineral, because it is regulated by parathyroid hormone and vitamin D rather than by the renal handling that governs the other cations."],
     ["With sodium and potassium as an electrolyte",
      "The electrolyte and acid-base group is sodium, potassium, chloride and bicarbonate; calcium is regulated differently and stands alone as the mineral."],
     ["With the liver and protein markers",
      "Calcium is on the basic panel; the liver and protein group is the comprehensive addition."],
     ["With blood urea nitrogen as a kidney marker",
      "Calcium is not grouped as a measure of kidney function."]],
   c=0, cite=c(7)),

 dict(topic="Indications", io=IOG, slot="initial test",
   q="Which of these is given as a medication-related indication for ordering a chemistry panel?",
   opts=[
     ["Drugs with kidney or liver toxicity, or with electrolyte effects",
      "Correct — the panel detects exactly the harms these drugs cause: a rising creatinine, rising transaminases, or a shifted potassium."],
     ["Any newly started prescription medication",
      "The indication is specific to drugs with those effects, not to all new prescriptions."],
     ["Drugs that require a loading dose",
      "A loading dose affects how quickly a level is reached rather than whether the drug harms kidney, liver or electrolytes."],
     ["Medications taken more than once daily",
      "Dosing frequency does not determine toxicity; the indication is the drug's effect on kidney, liver or electrolytes."]],
   c=0, cite=c(23)),

 dict(topic="Indications", io=IOG, slot="manifestation",
   q="Which cluster of symptoms is given as an indication for a chemistry panel?",
   opts=[
     ["Fatigue, weakness, oedema, jaundice, confusion, nausea and vomiting",
      "Correct — each can arise from a chemical derangement the panel detects: uraemia, electrolyte disturbance, hypoalbuminaemia, hyperbilirubinaemia or acidosis."],
     ["Fever, night sweats, weight loss, and lymph node swelling",
      "That pattern points to infection or malignancy workups instead."],
     ["Chest pain, breathlessness, and palpitations",
      "Cardiac symptoms would drive different first tests."],
     ["Joint pain, rash, and morning stiffness",
      "Those suggest a rheumatologic rather than a chemistry workup."]],
   c=0, cite=c(23)),

 dict(topic="Indications", io=IOG, slot="initial test",
   q="Which chronic conditions are named as monitoring indications for a chemistry panel?",
   opts=[
     ["Diabetes, chronic kidney disease, hypertension, and liver disease",
      "Correct — each either damages the organs the panel measures or is treated with drugs that do, so the panel tracks both the disease and its therapy."],
     ["Asthma, chronic obstructive pulmonary disease, and heart failure",
      "These are monitored by lung function and cardiac assessment; the panel tracks conditions affecting glucose, kidney and liver."],
     ["Rheumatoid arthritis, lupus, and psoriasis",
      "Autoimmune disease is monitored by inflammatory markers and antibodies, though a panel may be added for drug toxicity rather than for the disease itself."],
     ["Depression, anxiety, and insomnia",
      "These are assessed clinically; the panel is used to monitor diabetes, kidney disease, hypertension and liver disease."]],
   c=0, cite=c(23)),

 dict(topic="Indications", io=IOG, slot="initial test",
   q="Under the acute illness indication, which two situations call for a chemistry panel?",
   opts=[
     ["Dehydration and a suspected acid-base disorder",
      "Correct — dehydration shows as a rising urea nitrogen to creatinine ratio with concentrated electrolytes, and a bicarbonate with the anion gap identifies an acid-base disorder."],
     ["Fever and a suspected bloodstream infection",
      "Those would prompt cultures and a complete blood count."],
     ["Chest trauma and a suspected rib fracture",
      "Imaging rather than chemistry is the first step there."],
     ["Headache and a suspected migraine",
      "A suspected migraine is diagnosed clinically; the acute indications are dehydration and a suspected acid-base disorder."]],
   c=0, cite=c(23)),

 dict(topic="Abbreviations", io=IOA, slot="education",
   q="On a chemistry panel, what does the abbreviation Cr stand for?",
   opts=[
     ["Creatinine", "Correct — Reynolds singled this out as the one abbreviation that is not the element symbol it looks like."],
     ["Chromium", "This is the element whose symbol Cr normally is, and she warned specifically against reading it that way."],
     ["Creatine kinase", "That is a separate enzyme assay, abbreviated differently."],
     ["C-reactive protein", "That is an inflammatory marker and is not on the panel."]],
   c=0, cite=au()),

 dict(topic="Abbreviations", io=IOA, slot="education",
   q="Reynolds contrasted panel shorthand with what is written in an electronic medical record. What did she say about abbreviating there?",
   opts=[
     ["Do not abbreviate — write the term out in full",
      "Correct — her rule was that shorthand belongs to handwritten bedside notes, not the record."],
     ["Abbreviate wherever a standard abbreviation exists",
      "She said the opposite, and gave writing out sodium as her example."],
     ["Abbreviate only the electrolytes",
      "She drew no such distinction; the rule was to write everything out."],
     ["Follow whatever the ordering laboratory uses",
      "The laboratory's shorthand was not her standard for the note."]],
   c=0, cite=au()),

 dict(topic="Fishbone diagram", io=IOA, slot="education",
   q="The fishbone shorthand diagram carries reference ranges. What does Reynolds say it does NOT carry?",
   opts=[
     ["The units", "Correct — she pointed out the fishbone gives ranges but omits units."],
     ["The reference ranges themselves", "It does carry those; the omission is the units."],
     ["The patient's name and date", "The diagram is a shorthand for values, and she did not raise this."],
     ["The abnormal flags", "Flagging was not what she said the diagram leaves out."]],
   c=0, cite=au()),

 dict(topic="Fishbone diagram", io=IOA, slot="education",
   q="In fishbone shorthand, why is no label written next to each number?",
   opts=[
     ["Position on the diagram already identifies which test the number belongs to",
      "Correct — the layout itself carries the labelling, which is the point of the shorthand."],
     ["The labels are added later by the laboratory",
      "The diagram is written at the bedside by the clinician."],
     ["Only abnormal values are labelled",
      "Labelling does not depend on whether a value is abnormal."],
     ["The units serve as the labels",
      "The units are the part the diagram omits."]],
   c=0, cite=au()),

 dict(topic="Reference ranges", io=IOA, slot="education",
   q="Why do roughly 2.5 per cent of healthy people fall outside a normal range?",
   opts=[
     ["A normal range is defined as the mean plus or minus two standard deviations",
      "Correct — the tail beyond two standard deviations is where those healthy people sit."],
     ["Laboratory equipment has a known error rate of about 2.5 per cent",
      "The figure comes from how the range is defined, not from instrument error."],
     ["About 2.5 per cent of samples are mishandled before analysis",
      "Mishandling does produce spurious results, but the 2.5 per cent figure follows arithmetically from defining the range as two standard deviations about the mean."],
     ["Roughly 2.5 per cent of people have undiagnosed disease",
      "The point is the opposite — these people are healthy."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="education",
   q="Following from how a normal range is defined, what is concluded about a normal result?",
   opts=[
     ["A normal value does not exclude disease",
      "Correct — the range is set to capture most healthy people, not to separate sick from well, so a patient with disease can sit inside it just as a healthy person can sit outside."],
     ["A normal value effectively excludes disease",
      "A normal value lowers the probability of disease without excluding it, because the range is built from a healthy distribution rather than to discriminate disease."],
     ["A normal value should always be repeated",
      "It is the borderline abnormal result that warrants repeating; a normal one is interpreted against the clinical picture."],
     ["A normal value means the sample was handled correctly",
      "Sample handling is a separate concern."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="education",
   q="What is advised before launching an extensive workup on a borderline abnormal result?",
   opts=[
     ["Repeat or confirm the abnormality",
      "Correct — a value just outside the range may be biological variation or a pre-analytic artefact, so confirming it first avoids an expensive workup chasing a number that was never real."],
     ["Proceed straight to imaging",
      "Imaging follows a confirmed abnormality rather than replacing confirmation."],
     ["Treat empirically and recheck afterwards",
      "Treating before confirming risks committing a patient to therapy for an abnormality that a repeat would not reproduce."],
     ["Refer to the relevant specialist",
      "Referral on an unconfirmed borderline value passes on a question that a repeat test might answer immediately."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="test finding",
   q="There is one worked example of confirming a borderline abnormality. Which is it?",
   opts=[
     ["Using gamma-glutamyl transferase to confirm that a raised alkaline phosphatase is hepatic",
      "Correct — alkaline phosphatase also comes from bone, placenta and intestine, so gamma-glutamyl transferase, which does not, establishes that a raised value is biliary before any liver workup begins."],
     ["Using a repeat potassium to confirm a raised potassium is not haemolysed",
      "Repeating a potassium to exclude haemolysis is sound practice, but the worked confirmation example pairs alkaline phosphatase with gamma-glutamyl transferase."],
     ["Using cystatin C to confirm a reduced estimated filtration rate",
      "Cystatin C confirms an estimated filtration rate rather than illustrating the confirmation principle, which is shown with alkaline phosphatase and gamma-glutamyl transferase."],
     ["Using a fasting glucose to confirm a raised random glucose",
      "A fasting glucose reinterprets a value in the right context rather than confirming the same analyte through a second, more specific test."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="education",
   q="What third thing must every value be interpreted against?",
   opts=[
     ["Clinical context — history, medications and supplements, alcohol, and examination",
      "Correct — a result only acquires meaning alongside what the patient reports, what they are taking, and what the examination shows, since any of these can produce or explain the abnormality."],
     ["The patient's previous result from the same laboratory only",
      "A prior result establishes a trend, which helps, but the clinical context is broader: history, medications, supplements, alcohol and examination."],
     ["The reference range printed by the laboratory alone",
      "Reading a value against the printed range alone is exactly the trap; the clinical context determines what the number means."],
     ["The severity of the presenting complaint",
      "The presenting complaint is one part of it; the full context includes medications, supplements, alcohol and the examination findings."]],
   c=0, cite=c(18)),
]
