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

IOA = "Objective a — Explain the components of a chemistry panel"
IOG = "Objective g — Discuss indications for ordering chemistry panels"

POOL_A = [
 dict(topic="What a chemistry panel is", io=IOA, slot="initial test",
   q="What does a chemistry panel measure?",
   opts=[
     ["Metabolites, electrolytes, kidney markers, and in the expanded version liver and protein markers",
      "Correct — the deck's own one-line definition of the panel."],
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
      "Correct — the three words the deck uses for what the panel shows."],
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
     ["Eight", "Correct — the deck's table gives the basic metabolic panel as eight tests."],
     ["Seven", "Seven is the older chem-7, which leaves calcium off."],
     ["Twelve", "Twelve is a chem-12, an intermediate panel."],
     ["Fourteen", "Fourteen is the comprehensive metabolic panel."]],
   c=0, cite=c(7)),

 dict(topic="Basic metabolic panel", io=IOA, slot="initial test",
   q="Which eight tests make up the basic metabolic panel?",
   opts=[
     ["Glucose, calcium, sodium, potassium, chloride, carbon dioxide, blood urea nitrogen, and creatinine",
      "Correct — the eight the deck's panel table lists."],
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
      "Correct — the six the deck's table adds to reach fourteen."],
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
     ["Chem-14", "Correct — the deck gives chem-14 as the alternative name."],
     ["Chem-8", "Chem-8 is the basic panel including calcium."],
     ["Chem-20", "The deck does not use this name for any panel."],
     ["Chem-10", "The deck names chem-7, chem-8, chem-12 and chem-14 only."]],
   c=0, cite=c(7)),

 dict(topic="Choosing a panel", io=IOG, slot="initial test",
   q="A clinician wants a fuller picture of a patient's liver and nutritional protein status. Which panel is indicated?",
   opts=[
     ["A comprehensive metabolic panel",
      "Correct — the speaker notes name exactly this as the reason to step up from a basic panel."],
     ["A basic metabolic panel",
      "The basic panel carries no liver or protein markers at all."],
     ["A chem-7", "A chem-7 is a basic panel without even calcium."],
     ["A complete blood count",
      "That reports cell lines, not liver or protein markers."]],
   c=0, cite=cn(7)),

 dict(topic="Choosing a panel", io=IOG, slot="initial test",
   q="For which purpose do the speaker notes say a basic metabolic panel suffices?",
   opts=[
     ["Electrolytes, glucose, and renal screening",
      "Correct — the notes give these three as the basic panel's remit."],
     ["Liver injury and synthetic function",
      "Neither is measurable without the six comprehensive-panel additions."],
     ["Nutritional protein status",
      "Albumin and total protein are on the comprehensive panel only."],
     ["Cholestasis and biliary obstruction",
      "Alkaline phosphatase and bilirubin are comprehensive-panel tests."]],
   c=0, cite=cn(7)),

 dict(topic="Panel groupings", io=IOA, slot="initial test",
   q="Under the deck's functional grouping of panel components, which group do blood urea nitrogen and creatinine belong to?",
   opts=[
     ["Kidney function and waste",
      "Correct — the deck groups both as kidney function and waste markers."],
     ["Electrolytes and acid-base",
      "That group holds sodium, potassium, chloride, and bicarbonate."],
     ["Metabolic and fuel",
      "That group holds glucose alone."],
     ["Liver and protein",
      "That group is the six the comprehensive panel adds."]],
   c=0, cite=c(7)),

 dict(topic="Panel groupings", io=IOA, slot="initial test",
   q="Which four panel components make up the deck's electrolytes and acid-base group?",
   opts=[
     ["Sodium, potassium, chloride, and bicarbonate",
      "Correct — the four the deck groups together for electrolytes and acid-base."],
     ["Sodium, potassium, calcium, and chloride",
      "Calcium is grouped separately as the mineral."],
     ["Sodium, chloride, bicarbonate, and glucose",
      "Glucose is the metabolic and fuel group on its own."],
     ["Potassium, chloride, bicarbonate, and creatinine",
      "Creatinine belongs to the kidney function group."]],
   c=0, cite=c(7)),

 dict(topic="Panel groupings", io=IOA, slot="initial test",
   q="Where does calcium sit in the deck's grouping of panel components?",
   opts=[
     ["On its own, as the mineral",
      "Correct — the deck lists calcium separately under mineral."],
     ["With sodium and potassium as an electrolyte",
      "The deck's electrolyte group is sodium, potassium, chloride, and bicarbonate."],
     ["With the liver and protein markers",
      "Calcium is on the basic panel; the liver and protein group is the comprehensive addition."],
     ["With blood urea nitrogen as a kidney marker",
      "Calcium is not grouped as a measure of kidney function."]],
   c=0, cite=c(7)),

 dict(topic="Indications", io=IOG, slot="initial test",
   q="Which of these is given as a medication-related indication for ordering a chemistry panel?",
   opts=[
     ["Drugs with kidney or liver toxicity, or with electrolyte effects",
      "Correct — the deck's medication indication, worded as toxicity or electrolyte effect."],
     ["Any newly started prescription medication",
      "The indication is specific to drugs with those effects, not to all new prescriptions."],
     ["Drugs that require a loading dose",
      "Loading is not one of the deck's stated reasons."],
     ["Medications taken more than once daily",
      "Dosing frequency is not an indication the deck gives."]],
   c=0, cite=c(23)),

 dict(topic="Indications", io=IOG, slot="manifestation",
   q="Which cluster of symptoms does the deck give as an indication for a chemistry panel?",
   opts=[
     ["Fatigue, weakness, oedema, jaundice, confusion, nausea and vomiting",
      "Correct — the symptom list the deck prints under its indications."],
     ["Fever, night sweats, weight loss, and lymph node swelling",
      "That pattern points to infection or malignancy workups instead."],
     ["Chest pain, breathlessness, and palpitations",
      "Cardiac symptoms would drive different first tests."],
     ["Joint pain, rash, and morning stiffness",
      "Those suggest a rheumatologic rather than a chemistry workup."]],
   c=0, cite=c(23)),

 dict(topic="Indications", io=IOG, slot="initial test",
   q="Which chronic conditions does the deck name as monitoring indications for a chemistry panel?",
   opts=[
     ["Diabetes, chronic kidney disease, hypertension, and liver disease",
      "Correct — the four conditions the deck lists under monitoring."],
     ["Asthma, chronic obstructive pulmonary disease, and heart failure",
      "None is on the deck's monitoring list for this panel."],
     ["Rheumatoid arthritis, lupus, and psoriasis",
      "The deck does not give autoimmune disease as a monitoring indication."],
     ["Depression, anxiety, and insomnia",
      "These are not indications the deck gives."]],
   c=0, cite=c(23)),

 dict(topic="Indications", io=IOG, slot="initial test",
   q="Under the deck's acute illness indication, which two situations call for a chemistry panel?",
   opts=[
     ["Dehydration and a suspected acid-base disorder",
      "Correct — the two the deck pairs under acute illness."],
     ["Fever and a suspected bloodstream infection",
      "Those would prompt cultures and a complete blood count."],
     ["Chest trauma and a suspected rib fracture",
      "Imaging rather than chemistry is the first step there."],
     ["Headache and a suspected migraine",
      "The deck does not give this as an indication."]],
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
   q="Why does the deck say roughly 2.5 per cent of healthy people fall outside a normal range?",
   opts=[
     ["A normal range is defined as the mean plus or minus two standard deviations",
      "Correct — the tail beyond two standard deviations is where those healthy people sit."],
     ["Laboratory equipment has a known error rate of about 2.5 per cent",
      "The figure comes from how the range is defined, not from instrument error."],
     ["About 2.5 per cent of samples are mishandled before analysis",
      "Pre-analytic error is a real problem but is not the deck's explanation."],
     ["Roughly 2.5 per cent of people have undiagnosed disease",
      "The point is the opposite — these people are healthy."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="education",
   q="Following from how a normal range is defined, what does the deck conclude about a normal result?",
   opts=[
     ["A normal value does not exclude disease",
      "Correct — the deck states this directly."],
     ["A normal value effectively excludes disease",
      "The deck says the opposite."],
     ["A normal value should always be repeated",
      "It is the borderline abnormal value the deck says to confirm."],
     ["A normal value means the sample was handled correctly",
      "Sample handling is a separate concern."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="education",
   q="What does the deck advise before launching an extensive workup on a borderline abnormal result?",
   opts=[
     ["Repeat or confirm the abnormality",
      "Correct — the deck's instruction, with confirming a raised alkaline phosphatase as its example."],
     ["Proceed straight to imaging",
      "Imaging follows a confirmed abnormality rather than replacing confirmation."],
     ["Treat empirically and recheck afterwards",
      "The deck does not suggest treating before confirming."],
     ["Refer to the relevant specialist",
      "Referral is not the deck's next step for a borderline value."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="test finding",
   q="The deck gives one worked example of confirming a borderline abnormality. Which is it?",
   opts=[
     ["Using gamma-glutamyl transferase to confirm that a raised alkaline phosphatase is hepatic",
      "Correct — the deck's own example of a confirmatory step."],
     ["Using a repeat potassium to confirm a raised potassium is not haemolysed",
      "A sensible step clinically, but not the example the deck prints."],
     ["Using cystatin C to confirm a reduced estimated filtration rate",
      "Cystatin C does appear in the deck, but on the correlation slide rather than here."],
     ["Using a fasting glucose to confirm a raised random glucose",
      "Fasting state matters for glucose, but this is not the deck's confirmation example."]],
   c=0, cite=c(18)),

 dict(topic="Reference ranges", io=IOA, slot="education",
   q="What third thing does the deck say every value must be interpreted against?",
   opts=[
     ["Clinical context — history, medications and supplements, alcohol, and examination",
      "Correct — the deck's list of what surrounds the number."],
     ["The patient's previous result from the same laboratory only",
      "A prior value helps, but the deck's point is broader than that."],
     ["The reference range printed by the laboratory alone",
      "Interpreting against the range alone is what the deck warns against."],
     ["The severity of the presenting complaint",
      "The deck asks for the fuller clinical picture, not the complaint alone."]],
   c=0, cite=c(18)),
]
