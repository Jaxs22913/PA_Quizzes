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
   q="Knowing whether a chest film is anterior-posterior or posterior-anterior prevents which clinical error?",
   opts=[
     ["Calling cardiomegaly that is not there",
      "Correct — the posterior-anterior view reduces magnification of the heart, so reading an anterior-posterior film as if it were one overcalls cardiomegaly."],
     ["Missing free air beneath the diaphragm",
      "Free air is sought on the upright abdominal series; the projection question on a chest film is about magnification of the heart."],
     ["Mistaking a pleural effusion for consolidation",
      "Pleural effusion is evaluated with the decubitus position, where fluid layers out with gravity, not by knowing the chest projection."],
     ["Reversing the patient's left and right sides",
      "Side orientation is a separate convention; knowing the chest projection matters because the anterior-posterior view magnifies the heart."]],
   c=0, cite=c(40)),

 dict(topic="Positioning", io=IOE, slot="manifestation",
   q="Which patient gets an anterior-posterior chest film rather than a posterior-anterior one?",
   opts=[
     ["A sick inpatient who cannot get out of bed",
      "Correct — a patient who cannot stand is filmed anterior-posterior, and because that view magnifies the heart it must not be read for cardiomegaly like a posterior-anterior film."],
     ["Any patient in whom cardiomegaly is suspected",
      "The anterior-posterior view magnifies the heart, so it is the worse view for that question."],
     ["Any pediatric patient, because of the lower dose",
      "The posterior-anterior view is the one credited with lower dose to sensitive organs."],
     ["Any patient having a follow-up rather than a first study",
      "Follow-up status does not decide the projection; posterior-anterior is preferred because it reduces heart magnification and dose to sensitive organs."]],
   c=0, cite=c(40)),

 dict(topic="Abdominal series", io=IOC, slot="test finding",
   q="Which radiographic buzzword means a perforated bowel?",
   opts=[
     ["Free air under the diaphragm — perforated bowel",
      "Correct — the abdominal series is shot standing to assess air-fluid levels or free air in the abdomen, and free air is the sign of a perforated bowel."],
     ["Air-fluid levels in dilated loops — small bowel obstruction",
      "Air-fluid levels are how the series shows obstruction, but a perforated bowel shows as free air in the abdomen, not as air-fluid levels."],
     ["Coral-red fluorescence — erythrasma",
      "Coral-red fluorescence is not a radiographic finding at all; on the upright abdominal series, perforation shows as free air in the abdomen."],
     ["Increased attenuation — a metallic foreign body",
      "Increased attenuation is computed tomography vocabulary for dense material that appears whiter; it does not mean perforation, which shows as free air."]],
   c=0, cite=c(43)),

 dict(topic="Abdominal series", io=IOC, slot="differential",
   q="A patient has free air under the diaphragm. Which history would make perforation NOT the explanation?",
   opts=[
     ["Recent laparoscopic surgery, with the gas not yet absorbed",
      "Correct — gas left from recent laparoscopic surgery that has not yet been absorbed can explain free air; without that history, free air means perforation."],
     ["Recent upper gastrointestinal endoscopy without biopsy",
      "Endoscopy without biopsy is not the exception; only unabsorbed gas from recent laparoscopic surgery explains free air without a perforation."],
     ["A barium swallow performed the previous week",
      "Barium in the bowel lumen is not free air, and barium is contraindicated when perforation is suspected; the exception is recent laparoscopy."],
     ["Chronic constipation with a heavy stool burden",
      "A heavy stool burden does not put free air under the diaphragm; that finding means perforation unless gas remains from recent laparoscopic surgery."]],
   c=0, cite=c(43)),

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
   q="Renal function must be checked before gadolinium, but for a different reason from iodinated contrast. What is that reason?",
   opts=[
     ["It is a clearance problem — poor function lets it build up in tissue",
      "Correct — for gadolinium, renal function matters primarily for clearance; it can cause kidney damage, but not as much as computed tomography contrast, which is nephrotoxic."],
     ["Gadolinium is far more nephrotoxic than iodinated contrast, so the threshold for withholding it is lower",
      "The reverse holds: gadolinium can cause kidney damage but is not as harmful as computed tomography contrast, which is the nephrotoxic agent."],
     ["Gadolinium is cleared hepatically, so renal function predicts the hepatic reserve",
      "Gadolinium clearance is renal, not hepatic, which is why urea nitrogen and creatinine are assessed before magnetic resonance with contrast."],
     ["Gadolinium interferes with the creatinine assay, so a baseline is needed for comparison",
      "Assay interference is not the reason; renal function matters primarily for clearance, so urea nitrogen and creatinine are checked regardless."]],
   c=0, cite=c(54)),

 dict(topic="Contrast media", io=IOH, slot="avoid",
   q="A patient says they cannot have iodinated contrast because they are allergic to shellfish. What is the appropriate response?",
   opts=[
     ["Ask directly whether they have an IODINE allergy",
      "Correct — there should be no cross-reactivity between shellfish and iodinated contrast, but allergies are always asked about, and pretreatment is available."],
     ["Withhold the contrast, since shellfish allergy predicts iodinated contrast reaction",
      "Shellfish allergy does not predict a contrast reaction; there should be no cross-reactivity between shellfish and iodinated radiocontrast."],
     ["Give the contrast without further questions, since no allergy to contrast is possible",
      "Allergies are always asked about before contrast, and a documented anaphylactic reaction to any medication marks a high-risk patient."],
     ["Switch to gadolinium, since it contains no iodine and carries no allergy risk",
      "Switching modality is not the response; contrast is sometimes absolutely necessary, and pretreatment is available for high-risk patients."]],
   c=0, cite=c(53)),

 dict(topic="Contrast media", io=IOH, slot="escalation",
   q="What does pretreatment before contrast consist of?",
   opts=[
     ["Diphenhydramine and prednisone at intervals beforehand or at the time, plus fluids",
      "Correct — pretreatment combines diphenhydramine and prednisone, given at intervals beforehand or at the time, with fluids, for patients who need contrast."],
     ["A single dose of intravenous adrenaline immediately before the injection",
      "Adrenaline treats anaphylaxis; it is not a pretreatment regimen."],
     ["One liter of normal saline alone, with no medication",
      "One liter of normal saline protects the kidneys from iodinated contrast; pretreatment for allergy also includes medication."],
     ["A test dose of contrast given twenty minutes beforehand",
      "A test dose is not part of pretreatment; the regimen is medication given beforehand, with fluids, when contrast is necessary."]],
   c=0, cite=c(53)),

 dict(topic="Contrast media", io=IOG, slot="etiology",
   q="Why does a malignant mass enhance more than a benign one after intravenous contrast?",
   opts=[
     ["Neoplasms grow their own vessels and become more vascularized than the surrounding tissue",
      "Correct — the same logic explains why an abscess enhances: inflammation, edema and increased blood flow."],
     ["Malignant cells take up iodine directly through a membrane transporter",
      "Uptake into the cell is not the mechanism; it is the blood supply."],
     ["Malignant tissue has a higher water content, which holds contrast longer",
      "Water content is a magnetic resonance consideration rather than this one."],
     ["Contrast is actively secreted into malignant tissue by surrounding macrophages",
      "No such secretory mechanism was described."]],
   c=0, cite=r("1:27:54")),

 dict(topic="Contrast media", io=IOG, slot="complication",
   q="Which statement about the carcinogenicity of contrast media is correct?",
   opts=[
     ["It is all carcinogenic",
      "Correct — dyes and contrast materials are technically radioactive, so cancer is a risk factor for all contrast material, which is why each study asks whether it can be done without contrast. Note that iodinated and gadolinium agents are not themselves radioactive; only nuclear medicine tracers such as technetium-99 are."],
     ["Only the iodinated agents are carcinogenic, which is why gadolinium is preferred",
      "Cancer risk applies to all contrast material, not only iodinated agents, and gadolinium is the magnetic resonance agent rather than a safer substitute."],
     ["None of them is carcinogenic, which is why contrast is used freely",
      "Contrast is not used freely: cancer is a risk factor for all contrast material, so every study asks whether it could be done without contrast."],
     ["Only oral barium is carcinogenic, because it is toxic outside the bowel",
      "Barium's stated toxicity is to extra-intestinal tissue, with alkaline burns; cancer is a risk factor for all contrast material, not barium alone."]],
   c=0, cite=c(50)),

 dict(topic="Contrast media", io=IOH, slot="referral",
   q="What is the rule on ordering contrast into a pregnant uterus in primary care?",
   opts=[
     ["Never order it in primary care",
      "Correct — it is not ordered from primary care; by the time it is needed, the patient should already be with a specialist."],
     ["It is acceptable in the third trimester with the patient's consent",
      "No trimester makes it acceptable from primary care; pregnancy is one of the patient-specific risks weighed before any study."],
     ["It is acceptable provided renal function is checked first",
      "Checking renal function does not make it acceptable; pregnancy is the patient-specific risk that decides it, not kidney function."],
     ["It is acceptable if gadolinium is used instead of iodinated contrast",
      "Switching to gadolinium does not help: magnetic resonance, although safe, is still not recommended in pregnant patients."]],
   c=0, cite=c(3)),

 dict(topic="Diagnostic approach", io=IOC, slot="first-line",
   q="How should a modality be chosen when the diagnosis is not certain?",
   opts=[
     ["Reason from the tissue rather than from a memorized protocol",
      "Correct — computed tomography suits bone, magnetic resonance is the best modality for soft tissue, and ultrasound cannot penetrate bone or gas-filled structures."],
     ["Always begin with the study carrying the least radiation and escalate only if negative",
      "A lower-radiation alternative is one framing question, but a least-dose-first rule ignores which modality can rule the diagnosis in or out."],
     ["Always order both a plain film and a cross-sectional study at the same visit",
      "Parallel ordering adds radiation without adding benefit; the framing questions ask which modality best rules the diagnosis in or out."],
     ["Memorize a protocol for each presenting complaint and follow it exactly",
      "A fixed protocol does not cover the uncertain case; when unsure, reason from the tissue or tell the radiologist what you are looking for."]],
   c=0, cite=c(58)),

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
   q="Although magnetic resonance emits no radiation, in which patients is it still not recommended?",
   opts=[
     ["Pregnant patients and infants",
      "Correct — magnetic resonance emits no radiation and is considered safe, but it is still not recommended in pregnant patients or infants."],
     ["Patients with an acute stroke",
      "Stroke is a use, not a contraindication: magnetic resonance can be programmed for diffusion-weighted imaging, which is useful in stroke."],
     ["Patients with soft tissue masses",
      "Soft tissue masses are an indication, not a contraindication; magnetic resonance is the best imaging modality for soft tissue."],
     ["Patients needing neuro-imaging",
      "Neuro-imaging is where magnetic resonance is widely used, so it is an indication rather than a group in whom it is avoided."]],
   c=0, cite=c(27)),
]
