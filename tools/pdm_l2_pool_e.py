# Principles of Diagnostic Medicine I, Lecture 2 — pool E.
#
# WRITTEN FROM THE 2026-08-19 LECTURE RECORDING, not from the deck. Pools A to D
# were built before any audio existed and the guide said so. These questions
# capture the places where Professor Reynolds REFINED what the slide says, or
# named something out loud as a buzzword.
#
# Cross-examined: my own transcription and Notability's were both read. On the
# single de-emphasis in the lecture they agree exactly.
#
# Appended, never prepended -- pdm_l2_lengthfix keys index into A + B + C.
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "2. svPrinciples of Medical Imaging.pptx"
REC = "2026-08-19 lecture recording"
def c(n): return f"{SRC}, Slide {n}"
def r(t): return f"{REC}, {t}"

IOB = "b — Describe the function and clinical applications of radiography, ultrasonography, computed tomography, magnetic resonance imaging, magnetic resonance angiography, positron emission tomography, single photon emission computed tomography and angiographic studies"
IOC = "c — Discuss anatomical structures best visualized by each imaging modality"
IOE = "e — Discuss the importance of patient positioning in medical imaging"
IOG = "g — Compare and contrast the risks and benefits associated with contrast administration"
IOH = "h — Discuss contraindications and safety considerations of commonly used imaging modalities"

POOL_E = [
 dict(topic="Positioning", io=IOE, slot="test finding",
   q="Professor Reynolds said you need to know which view you are looking at. What clinical error does knowing it prevent?",
   opts=[
     ["Calling cardiomegaly that is not there",
      "Correct — the heart is magnified on an anterior-posterior film, so reading one as if it were posterior-anterior overcalls heart size."],
     ["Missing free air beneath the diaphragm",
      "Free air is found on an upright film; the view named here is about the heart."],
     ["Mistaking a pleural effusion for consolidation",
      "That is what the decubitus view helps with."],
     ["Reversing the patient's left and right sides",
      "Orientation matters, but the error she named was about heart size."]],
   c=0, cite=r("1:14:06")),

 dict(topic="Positioning", io=IOE, slot="manifestation",
   q="Which patient does Professor Reynolds say will get an anterior-posterior chest film rather than a posterior-anterior one?",
   opts=[
     ["A sick inpatient who cannot get out of bed",
      "Correct — they cannot stand against a wall, so they are filmed anterior-posterior in bed. Which is exactly why reading the view label matters in practice."],
     ["Any patient in whom cardiomegaly is suspected",
      "The anterior-posterior view magnifies the heart, so it is the worse view for that question."],
     ["Any paediatric patient, because of the lower dose",
      "The posterior-anterior view is the one credited with lower dose to sensitive organs."],
     ["Any patient having a follow-up rather than a first study",
      "Follow-up status is not what determines the projection."]],
   c=0, cite=r("1:14:21")),

 dict(topic="Abdominal series", io=IOC, slot="test finding",
   q="Which phrase did Professor Reynolds call out as a buzzword, and what does it mean?",
   opts=[
     ["Free air under the diaphragm — perforated bowel",
      "Correct — unless there has been recent laparoscopic surgery and the insufflated gas is not yet absorbed."],
     ["Air-fluid levels in dilated loops — small bowel obstruction",
      "Obstruction is a named indication for the series, but it is not the phrase she flagged."],
     ["Coral-red fluorescence — erythrasma",
      "That is a dermatology finding from a different course."],
     ["Increased attenuation — a metallic foreign body",
      "Attenuation is computed tomography vocabulary rather than the buzzword named."]],
   c=0, cite=r("1:22:50")),

 dict(topic="Abdominal series", io=IOC, slot="differential",
   q="A patient has free air under the diaphragm. Which history would make perforation NOT the explanation?",
   opts=[
     ["Recent laparoscopic surgery, with the gas not yet absorbed",
      "Correct — insufflation of the abdomen puts gas there deliberately. With belly pain, fever, nausea and vomiting and no recent surgery, it is perforation."],
     ["Recent upper gastrointestinal endoscopy without biopsy",
      "That is not the exception Professor Reynolds named."],
     ["A barium swallow performed the previous week",
      "Barium in the lumen is not free air, and this is not the named exception."],
     ["Chronic constipation with a heavy stool burden",
      "Stool burden does not produce free intraperitoneal air."]],
   c=0, cite=r("1:22:55")),

 dict(topic="Abdominal series", io=IOE, slot="first-line",
   q="Why is the abdominal film taken upright?",
   opts=[
     ["So air will float up and fluid will settle down",
      "Correct — which is what makes free air and air-fluid levels visible."],
     ["So the diaphragm is pushed down and the lung bases are cleared",
      "Diaphragm position is not the reason given."],
     ["So the bowel gas pattern is compressed into a single plane",
      "Compression is not what upright positioning achieves."],
     ["So the kidneys descend into the field of view",
      "The kidney-ureter-bladder film is taken supine, not upright."]],
   c=0, cite=r("1:23:22")),

 dict(topic="Contrast media", io=IOH, slot="initial test",
   q="Professor Reynolds said renal function must be checked before gadolinium, but for a different reason from iodinated contrast. What is that reason?",
   opts=[
     ["It is a clearance problem — poor function lets it build up in tissue",
      "Correct — gadolinium is not necessarily nephrotoxic itself, but if the kidney cannot clear it, it accumulates in tissue and that accumulation is toxic. With iodinated contrast the agent itself is nephrotoxic."],
     ["Gadolinium is far more nephrotoxic than iodinated contrast, so the threshold for withholding it is lower",
      "She said the opposite: gadolinium is not necessarily nephrotoxic."],
     ["Gadolinium is cleared hepatically, so renal function predicts the hepatic reserve",
      "The clearance route in question is renal."],
     ["Gadolinium interferes with the creatinine assay, so a baseline is needed for comparison",
      "No assay interference is described."]],
   c=0, cite=r("1:40:24")),

 dict(topic="Contrast media", io=IOH, slot="avoid",
   q="A patient says they cannot have iodinated contrast because they are allergic to shellfish. What did Professor Reynolds say to do?",
   opts=[
     ["Ask directly whether they have an IODINE allergy",
      "Correct — there should be no cross-reactivity from shellfish, but a genuine iodine allergy IS a concern, and when in doubt you pretreat."],
     ["Withhold the contrast, since shellfish allergy predicts iodinated contrast reaction",
      "The cross-reactivity is exactly what she rejects."],
     ["Give the contrast without further questions, since no allergy to contrast is possible",
      "A real iodine allergy is a genuine concern."],
     ["Switch to gadolinium, since it contains no iodine and carries no allergy risk",
      "Switching modality is not the response she described to this question."]],
   c=0, cite=r("1:39:11")),

 dict(topic="Contrast media", io=IOH, slot="escalation",
   q="What does pretreatment before contrast consist of, as Professor Reynolds described it?",
   opts=[
     ["Diphenhydramine and prednisone at intervals beforehand or at the time, plus fluids",
      "Correct — she noted there are formal protocols for this."],
     ["A single dose of intravenous adrenaline immediately before the injection",
      "Adrenaline treats anaphylaxis; it is not a pretreatment regimen."],
     ["One litre of normal saline alone, with no medication",
      "Saline protects the kidneys; the pretreatment she described also includes medication."],
     ["A test dose of contrast given twenty minutes beforehand",
      "No test-dose approach was described."]],
   c=0, cite=r("1:39:27")),

 dict(topic="Contrast media", io=IOG, slot="etiology",
   q="Why does a malignant mass enhance more than a benign one after intravenous contrast?",
   opts=[
     ["Neoplasms grow their own vessels and become more vascularized than the surrounding tissue",
      "Correct — the same logic explains why an abscess enhances: inflammation, oedema and increased blood flow."],
     ["Malignant cells take up iodine directly through a membrane transporter",
      "Uptake into the cell is not the mechanism; it is the blood supply."],
     ["Malignant tissue has a higher water content, which holds contrast longer",
      "Water content is a magnetic resonance consideration rather than this one."],
     ["Contrast is actively secreted into malignant tissue by surrounding macrophages",
      "No such secretory mechanism was described."]],
   c=0, cite=r("1:27:54")),

 dict(topic="Contrast media", io=IOG, slot="complication",
   q="What did Professor Reynolds say about the carcinogenicity of contrast media, and what does it justify?",
   opts=[
     ["It is all carcinogenic",
      "Correct — which is exactly why the diagnostic approach asks whether the study can be done without contrast. She tied the risk straight back to the four framing questions."],
     ["Only the iodinated agents are carcinogenic, which is why gadolinium is preferred",
      "She said the risk applies to contrast media generally."],
     ["None of them is carcinogenic, which is why contrast is used freely",
      "She stated the opposite."],
     ["Only the nuclear medicine tracers are carcinogenic, because they are radioactive",
      "She described the contrast media generally as technically radioactive."]],
   c=0, cite=r("27:38")),

 dict(topic="Contrast media", io=IOH, slot="referral",
   q="What did Professor Reynolds say about ordering contrast into a pregnant uterus in primary care?",
   opts=[
     ["Never order it in primary care",
      "Correct — if you have reached the point of needing it, the patient should already be with a specialist. She called it very dangerous."],
     ["It is acceptable in the third trimester with the patient's consent",
      "No trimester exception was described."],
     ["It is acceptable provided renal function is checked first",
      "Renal function is not what makes this decision."],
     ["It is acceptable if gadolinium is used instead of iodinated contrast",
      "Magnetic resonance is itself not recommended in pregnancy."]],
   c=0, cite=r("27:11")),

 dict(topic="Diagnostic approach", io=IOC, slot="first-line",
   q="What method did Professor Reynolds give for choosing a modality when you are not certain of the diagnosis?",
   opts=[
     ["Reason from the tissue rather than from a memorised protocol",
      "Correct — bone points to x-ray or computed tomography; soft tissue often starts with ultrasound. Memorised protocols are fine, but reasoning from the tissue is what generalises."],
     ["Always begin with the study carrying the least radiation and escalate only if negative",
      "Dose matters in the diagnostic approach, but this is not the method she described."],
     ["Always order both a plain film and a cross-sectional study at the same visit",
      "Ordering in parallel is not what she recommended."],
     ["Memorise a protocol for each presenting complaint and follow it exactly",
      "She allowed that this works, but named reasoning from the tissue as the fallback."]],
   c=0, cite=r("1:10:31")),

 dict(topic="Positioning", io=IOE, slot="first-line",
   q="How is the side chosen for a decubitus film?",
   opts=[
     ["By which direction you want the fluid to run",
      "Correct — decubitus positioning is used a great deal to layer out fluid."],
     ["Always left lateral, by convention",
      "Left lateral decubitus is used for particular purposes elsewhere, but the side here is chosen deliberately."],
     ["By which side the patient can lie on comfortably",
      "Comfort is not the criterion given."],
     ["By which lung field is the larger of the two",
      "Lung size is not what determines the side."]],
   c=0, cite=r("1:17:47")),

 dict(topic="Magnetic resonance imaging", io=IOB, slot="avoid",
   q="Which point did Professor Reynolds explicitly say would NOT be on the test?",
   opts=[
     ["Keeping a patient on the same scanner so serial studies match",
      "Correct — her example was repeating scans every six months in multiple sclerosis. She called it a life thing rather than exam material, and it is the only de-emphasis in the whole lecture."],
     ["The difference between T1 and T2 weighting",
      "That is core content and was taught at length."],
     ["The relationship between field strength in Tesla and image quality",
      "This was taught without any such disclaimer."],
     ["The need to screen for implanted magnetic devices",
      "That is a safety consideration and is examinable."]],
   c=0, cite=r("1:02:11")),
]
