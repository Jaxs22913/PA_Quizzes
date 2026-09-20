# -*- coding: utf-8 -*-
# PDM I Lecture 8 (Cardiac Imaging and Vascular Studies, Ayelet Elwaya) -- pool A.
# Chest radiography for cardiac evaluation, vascular ultrasound, and
# echocardiography. Pool B carries stress testing through the invasive studies.
#
# NUMBERS. The course rule is that a number never appears in a stem without the
# scale that reads it, and that nothing is calculated. This deck has two numbers
# that matter -- the cardiothoracic ratio threshold and the 85 per cent of
# predicted maximum heart rate that makes a stress test valid -- and both are
# handled the same way here: the figure is SUPPLIED in the stem and the question
# asks what it means. That is the more useful question in any case, since a
# ratio a student can recall but not interpret is worth nothing on a film.
#
# The transcript for this lecture is queued but not yet written, so every
# question comes off the slides. Emphasis can be layered in afterwards.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "Cardiac Imaging and Vascular Studies - Elwaya.pptx"
def c(n):  return f"{SRC}, Slide {n}"

IOA = "Identify common abnormal cardiovascular imaging findings"
IOB = "Measure the cardiothoracic ratio to evaluate cardiac enlargement"
IOC = "Compare and contrast cardiovascular imaging modalities"
IOD = "Discuss indications, advantages, and limitations of echocardiography"

POOL_A = [

{"topic": "Chest radiography", "io": IOC, "slot": "modality choice",
 "q": "What is the standing of chest radiography in cardiac evaluation?",
 "opts": [
  ["It is not the primary modality, but it gives useful clues when obtained",
   "Correct. It is rarely the study you order to answer a cardiac question, and frequently the study you already have, which is why reading it well matters."],
  ["It is the primary modality for assessing cardiac function",
   "Function and detailed cardiac anatomy are exactly what it does not assess."],
  ["It has no role in cardiac assessment",
   "It visualises the cardiac silhouette, the great vessels and the pulmonary vasculature, all of which carry cardiac information."],
  ["It replaces echocardiography when the patient cannot lie flat",
   "It does not substitute for echocardiography; the two answer different questions."]],
 "c": 0, "cite": c(4)},

{"topic": "Chest radiography", "io": IOA, "slot": "anatomy",
 "q": "Which structures can be at least partly seen on a chest radiograph for cardiac purposes?",
 "opts": [
  ["Cardiac silhouette, great vessels, lungs and pleura",
   "Correct, along with the pulmonary vasculature. Note what is absent: the chambers, the valves and the coronary arteries are not among them."],
  ["The coronary arteries and the cardiac valves",
   "Neither is visualised on a plain radiograph; calcification of a valve may be seen, but not the valve's structure."],
  ["The cardiac conduction system",
   "Conduction is assessed electrically rather than radiographically."],
  ["The pericardial fluid volume",
   "Pericardial calcification may be visible, but fluid volume is not measured on a plain film."]],
 "c": 0, "cite": c(4)},

{"topic": "Chest radiography", "io": IOA, "slot": "finding",
 "q": "Which chest radiograph findings are given as indicators of cardiac pathology?",
 "opts": [
  ["Oedema, effusion, cardiomegaly, cephalisation and calcification",
   "Correct, with tension physiology completing the list. Several are about the lungs rather than the heart, which is the point: the heart announces itself through what it does to everything around it. The calcification may be of the great vessels, the valves or the pericardium, and tension physiology completes the list."],
  ["Coronary artery stenosis and the distribution of plaque",
   "These require computed tomography angiography or catheter angiography."],
  ["Ejection fraction and regional wall motion abnormality",
   "Both are functional measures requiring echocardiography or magnetic resonance."],
  ["Valve pressure gradients and regurgitant volume",
   "These are Doppler measurements made on echocardiography rather than findings visible on a plain film."]],
 "c": 0, "cite": c(6)},

{"topic": "Cardiothoracic ratio", "io": IOB, "slot": "interpretation",
 "q": "A properly performed posteroanterior chest radiograph shows the cardiac silhouette occupying 58 per cent of the internal thoracic diameter. What does that suggest?",
 "opts": [
  ["Cardiomegaly",
   "Correct. The silhouette should normally occupy no more than about half the internal thoracic diameter, so this exceeds it."],
  ["A normal heart size",
   "A normal ratio sits below about one half of the internal thoracic diameter, and this measurement is above it."],
  ["Pulmonary hypertension without cardiac enlargement",
   "The ratio measures the cardiac silhouette rather than the pulmonary circulation."],
  ["A pericardial effusion specifically",
   "An effusion can enlarge the silhouette, but the ratio identifies enlargement rather than its cause."]],
 "c": 0, "cite": c(8)},

{"topic": "Cardiothoracic ratio", "io": IOB, "slot": "interpretation",
 "q": "Why does the cardiothoracic ratio require a properly performed posteroanterior film?",
 "opts": [
  ["Projection alters the apparent size of the cardiac silhouette",
   "Correct. A ratio measured off the wrong projection is a measurement of the technique rather than of the heart."],
  ["Only a posteroanterior film shows the pulmonary vasculature",
   "Vasculature is visible on other projections; it is the silhouette measurement that depends on projection."],
  ["Contrast is required and is only given for posteroanterior films",
   "No contrast is involved in measuring the ratio; it is the projection that alters the apparent silhouette size."],
  ["The ratio can only be calculated with electrocardiographic gating",
   "Gating belongs to cardiac computed tomography rather than to plain radiography."]],
 "c": 0, "cite": c(8)},

{"topic": "Cephalisation", "io": IOA, "slot": "finding",
 "q": "What is cephalisation on a chest radiograph?",
 "opts": [
  ["Upper zone vessels becoming larger",
   "Correct. Flow redistributes upward, which is why the sign sits in the lungs while the problem is in the heart."],
  ["Fluid tracking into the interlobar fissures",
   "That would be described as effusion or fissural fluid rather than cephalisation."],
  ["The trachea deviating toward the apex",
   "Tracheal deviation is a different sign entirely. Cephalisation is enlargement of the upper zone vessels."],
  ["Calcification of the aortic arch",
   "Great vessel calcification is listed separately from cephalisation."]],
 "c": 0, "cite": c(9)},

{"topic": "Cephalisation", "io": IOA, "slot": "finding",
 "q": "In which patients is cephalisation seen?",
 "opts": [
  ["Heart failure and pulmonary hypertension",
   "Correct. Both raise pressure in the pulmonary circulation, and the redistribution upward is the radiographic consequence."],
  ["Pneumothorax and pleural effusion",
   "Neither is given as a cause. Cephalisation is seen in heart failure and pulmonary hypertension."],
  ["Coronary artery disease without failure",
   "Coronary disease alone does not produce it; the sign follows raised pulmonary pressure in failure or pulmonary hypertension."],
  ["Pericardial calcification",
   "Calcification is listed as a separate radiographic finding rather than as a form of cephalisation."]],
 "c": 0, "cite": c(9)},

{"topic": "Vascular ultrasound", "io": IOC, "slot": "mechanism",
 "q": "How does a vascular ultrasound image form?",
 "opts": [
  ["Quartz crystals emit pulses that reflect off tissue",
   "Correct. The returning echoes are what the machine turns into a picture, so anything that stops sound returning leaves a gap in it. The pulses are high frequency, and what returns depends on the density of what they meet."],
  ["Ionising radiation is absorbed differently by tissues of differing density",
   "That describes radiography; ultrasound uses no ionising radiation."],
  ["A magnetic field aligns protons which then emit radiofrequency signal",
   "That describes magnetic resonance. Ultrasound works by emitting sound pulses and reading the returning echoes."],
  ["An injected tracer is taken up and emits gamma rays",
   "That describes nuclear imaging. Ultrasound forms its image from reflected high-frequency sound."]],
 "c": 0, "cite": c(14)},

{"topic": "Vascular ultrasound", "io": IOC, "slot": "interpretation",
 "q": "On a vascular ultrasound, how does tissue density relate to the image?",
 "opts": [
  ["The denser the structure the lighter it appears",
   "Correct, and superficial structures sit nearer the top of the screen, which together let you orient any image without being told what it is. So air is black and bone is near white."],
  ["The denser the structure the darker it appears",
   "The relationship runs the other way: dense structures return more signal and appear lighter."],
  ["Density does not affect the image, only depth does",
   "Both matter: depth sets position on the screen and density sets brightness."],
  ["Only flowing blood produces any signal",
   "Tissue of all kinds reflects sound; Doppler is what adds flow information."]],
 "c": 0, "cite": c(14)},

{"topic": "Vascular ultrasound", "io": IOA, "slot": "interpretation",
 "q": "How are veins and arteries told apart on a vascular ultrasound?",
 "opts": [
  ["Veins collapse when compressed and arteries pulsate",
   "Correct. Compression is the manoeuvre the whole deep vein thrombosis study rests on, because a vein that will not collapse has something in it."],
  ["Veins pulsate and arteries collapse when compressed",
   "The behaviours are the other way round: veins collapse under compression and arteries pulsate."],
  ["Veins appear bright and arteries appear dark",
   "Both appear as well circumscribed hypoechoic or anechoic structures."],
  ["Only Doppler can distinguish them",
   "Compression and pulsatility distinguish them on grey scale alone."]],
 "c": 0, "cite": c(15)},

{"topic": "Vascular ultrasound", "io": IOC, "slot": "indication",
 "q": "Which of these is NOT among the listed indications for vascular ultrasound?",
 "opts": [
  ["Assessment of coronary artery stenosis",
   "Correct -- this is not one. The coronary arteries are not accessible to surface vascular ultrasound; they are assessed by computed tomography angiography or catheter angiography."],
  ["Deep vein thrombosis study and vascular access",
   "Both are listed indications, alongside carotid evaluation, aneurysm assessment and venous insufficiency."],
  ["Carotid evaluation after stroke, transient ischaemic attack or myocardial infarction",
   "This is a listed indication, alongside deep vein thrombosis studies, vascular access and aneurysm evaluation."],
  ["Abdominal aortic aneurysm evaluation and varicose veins",
   "Both are listed indications, alongside vascular access, deep vein thrombosis studies and carotid assessment."]],
 "c": 0, "cite": c(16)},

{"topic": "Vascular ultrasound", "io": IOC, "slot": "advantage",
 "q": "Which combination of advantages does vascular ultrasound offer?",
 "opts": [
  ["Fast, portable, repeatable, no ionising radiation",
   "Correct. The combination of no radiation and easy repetition is what makes it the study you can do again tomorrow without cost to the patient. It shows both anatomy and flow."],
  ["Superior resolution to computed tomography with no operator dependence",
   "Resolution is not its strength and it is highly operator dependent."],
  ["Reliable assessment of deep vessels regardless of body habitus",
   "Deep vessels are harder to assess and body habitus is an explicit limitation."],
  ["Independence from the angle at which the probe is held",
   "Probe angle can affect measurements, which is one of its limitations."]],
 "c": 0, "cite": c(17)},

{"topic": "Vascular ultrasound", "io": IOC, "slot": "limitation",
 "q": "Which limitations are described for vascular ultrasound?",
 "opts": [
  ["Highly operator dependent, limited by body habitus",
   "Correct. Calcification causes acoustic shadowing, which matters because the vessels most worth imaging are often the ones most calcified. Degraded by bone, air and calcification."],
  ["Ionising radiation dose and contrast nephrotoxicity",
   "Neither applies: ultrasound uses no ionising radiation and no iodinated contrast."],
  ["Dependence on heart rate and rhythm",
   "Rate and rhythm dependence belongs to cardiac computed tomography."],
  ["Inability to show blood flow",
   "Showing both anatomy and flow is one of its advantages rather than a limitation, with Doppler supplying the flow."]],
 "c": 0, "cite": c(18)},

{"topic": "Vascular ultrasound", "io": IOC, "slot": "limitation",
 "q": "Why does calcification degrade a vascular ultrasound image?",
 "opts": [
  ["It causes acoustic shadowing",
   "Correct. Sound does not pass through, so everything behind the calcium is unassessable rather than merely indistinct."],
  ["It absorbs the ionising radiation before it reaches the vessel",
   "No ionising radiation is involved in ultrasound. Calcification blocks sound, casting an acoustic shadow behind it."],
  ["It produces a blooming artefact that exaggerates the lesion",
   "Blooming from calcification is a computed tomography artefact."],
  ["It prevents the vein from collapsing under compression",
   "Failure to collapse indicates thrombus rather than calcification."]],
 "c": 0, "cite": c(18)},

{"topic": "Echocardiography", "io": IOD, "slot": "indication",
 "q": "What does echocardiography evaluate?",
 "opts": [
  ["Chamber size, ventricular function, valves, shunts and pressures",
   "Correct. It is the functional study of the heart, which is what separates it from computed tomography, and Doppler is what adds flow and velocity to it. Wall thickness and ejection fraction come with the ventricular assessment, and Doppler adds flow and velocity."],
  ["The coronary artery calcium score",
   "Calcium scoring is done by non-contrast cardiac computed tomography."],
  ["The distribution of coronary atherosclerotic plaque",
   "Plaque distribution requires computed tomography angiography or catheter angiography."],
  ["The electrical conduction pathways of the heart",
   "Conduction is assessed by electrocardiography and electrophysiological testing."]],
 "c": 0, "cite": c(20)},

{"topic": "Echocardiography", "io": IOD, "slot": "modality choice",
 "q": "What distinguishes a transthoracic from a transoesophageal echocardiogram?",
 "opts": [
  ["The transducer is outside the body in one, inside in the other",
   "Correct, and everything else about the two -- invasiveness, sedation, contraindications, and how much posterior detail you get -- follows from that single difference."],
  ["One uses Doppler and the other does not",
   "Both can use Doppler. What separates them is whether the transducer sits outside the body or inside it."],
  ["One uses ionising radiation while the other does not",
   "Neither uses ionising radiation. The difference is the position of the transducer, outside the body or within it."],
  ["One assesses valves and the other assesses chambers",
   "Both assess valves and chambers; the difference is the transducer position."]],
 "c": 0, "cite": c(20)},

{"topic": "Echocardiography", "io": IOD, "slot": "modality choice",
 "q": "Why is transthoracic echocardiography the most common echo procedure?",
 "opts": [
  ["It can be performed at the bedside and is noninvasive",
   "Correct. Availability rather than image quality is what makes it the default, and the trade is detail at the back of the heart."],
  ["It gives better detail of the posterior structures",
   "Posterior and inferior detail is exactly where it is weaker than the transoesophageal study."],
  ["It requires no operator training",
   "Operator dependence applies to ultrasound generally. Its advantage is being noninvasive and available at the bedside."],
  ["It is the only echo that can use Doppler",
   "Doppler is available in both studies. The transthoracic study leads because it is noninvasive and bedside-capable."]],
 "c": 0, "cite": c(22)},

{"topic": "Echocardiography", "io": IOD, "slot": "modality choice",
 "q": "Which structures does a transoesophageal study show in more detail than a transthoracic one?",
 "opts": [
  ["Left atrium, mitral valve, aorta and coronaries",
   "Correct, with the pulmonary artery too. The probe sits directly behind the heart, so the structures that gain are the posterior ones."],
  ["The right ventricle and the tricuspid valve",
   "The gain is on the posterior and inferior side of the heart rather than on the right-sided structures."],
  ["The pericardium alone",
   "The improvement is not confined to the pericardium; it covers the left atrium, mitral valve, pulmonary artery, aorta and coronary arteries."],
  ["The coronary calcium burden",
   "Calcium scoring is a non-contrast computed tomography measurement rather than an echocardiographic one."]],
 "c": 0, "cite": c(22)},

{"topic": "Echocardiography", "io": IOD, "slot": "indication",
 "q": "For which of these is a transoesophageal study specifically useful?",
 "opts": [
  ["Valve vegetations",
   "Correct. All are small, posterior, or both, which is precisely where the transthoracic view falls short. Prosthetic valve function, cardiac tumours and left atrial appendage thrombus."],
  ["Coronary artery calcium scoring",
   "That is a non-contrast computed tomography study. The transoesophageal study excels at posterior structures."],
  ["Assessing exercise capacity",
   "Exercise capacity is assessed by stress testing rather than by an echocardiogram at rest."],
  ["Measuring the cardiothoracic ratio",
   "That is measured on a chest radiograph rather than by echocardiography."]],
 "c": 0, "cite": c(23)},

{"topic": "Echocardiography", "io": IOD, "slot": "indication",
 "q": "Why is a transoesophageal study used in a patient presenting with cerebral ischaemia?",
 "opts": [
  ["It can find thrombus in the left atrial appendage",
   "Correct. It looks for the source rather than the consequence, and the appendage is the site the transthoracic study sees worst."],
  ["It measures cerebral blood flow directly and noninvasively",
   "Echocardiography images the heart rather than the cerebral circulation."],
  ["It assesses the carotid arteries",
   "The carotids are assessed by vascular ultrasound. The transoesophageal study looks for a cardiac source of embolus."],
  ["It excludes coronary stenosis",
   "Coronary stenosis is not assessed by echocardiography; it needs computed tomography angiography or catheter angiography."]],
 "c": 0, "cite": c(23)},

{"topic": "Echocardiography", "io": IOD, "slot": "procedure",
 "q": "In which position does a patient lie initially for transthoracic echocardiography?",
 "opts": [
  ["Left lateral decubitus",
   "Correct. It brings the heart toward the chest wall, and the patient is moved through other positions to obtain the different views."],
  ["Supine and flat throughout",
   "The patient starts in the left lateral decubitus position and is repositioned."],
  ["Prone",
   "The prone position is not used. The patient starts in left lateral decubitus and is repositioned for other views."],
  ["Standing",
   "The study is performed lying, starting in the left lateral decubitus position."]],
 "c": 0, "cite": c(24)},

{"topic": "Echocardiography", "io": IOD, "slot": "procedure",
 "q": "What does a transoesophageal study require that a transthoracic one does not?",
 "opts": [
  ["Throat anaesthesia, sedation and monitoring",
   "Correct. It is a procedure rather than a scan, which is why it carries a contraindication list and the transthoracic study does not."],
  ["Iodinated contrast given intravenously",
   "No iodinated contrast is used in echocardiography; the transoesophageal study needs anaesthesia, sedation and monitoring."],
  ["Electrocardiographic gating of the images",
   "Gating belongs to cardiac computed tomography. The transoesophageal study requires sedation and airway monitoring."],
  ["A period of fasting from fluids only",
   "The requirements described are anaesthesia, sedation and monitoring."]],
 "c": 0, "cite": c(25)},

{"topic": "Echocardiography", "io": IOD, "slot": "contraindication",
 "q": "Which oesophageal conditions contraindicate a transoesophageal echocardiogram?",
 "opts": [
  ["Stricture, malignancy or bleeding varices",
   "Correct. All three mean passing a probe risks perforation or haemorrhage, which is the hazard the contraindication list exists to avoid."],
  ["Gastro-oesophageal reflux disease",
   "Reflux alone is not listed. Stricture, malignancy and bleeding varices are the oesophageal contraindications."],
  ["A history of oesophageal candidiasis",
   "Not among the listed contraindications, which are stricture, malignancy and varices with recent or active bleeding."],
  ["Recent barium swallow",
   "Not among the listed contraindications; stricture, malignancy and bleeding varices are the oesophageal ones."]],
 "c": 0, "cite": c(26)},

{"topic": "Echocardiography", "io": IOD, "slot": "contraindication",
 "q": "Why must a Zenker's diverticulum be identified before a transoesophageal study?",
 "opts": [
  ["The probe risks entering and perforating the pouch",
   "Correct, and because it is a pouch rather than a narrowing, the operator may feel nothing wrong until the damage is done."],
  ["It prevents adequate sedation",
   "Sedation is not the issue; the hazard is that the probe may enter and perforate the pouch."],
  ["It causes a false positive for vegetations",
   "It is a procedural hazard rather than an imaging artefact: the probe risks entering and perforating the pouch."],
  ["It makes the patient unable to swallow the local anaesthetic",
   "The concern is perforation rather than anaesthetic administration."]],
 "c": 0, "cite": c(26)},

{"topic": "Echocardiography", "io": IOD, "slot": "contraindication",
 "q": "Which patient factors, other than oesophageal disease, contraindicate a transoesophageal study?",
 "opts": [
  ["An uncooperative patient, restricted neck movement, airway risk",
   "Correct. Two are about whether the patient can be positioned and kept still, and one is about whether the airway can be protected under sedation. In full: altered mental status or an uncooperative patient, cervical spine arthritis with reduced range of motion, and obstructive sleep apnoea or other risk of airway compromise."],
  ["Significant renal impairment",
   "Renal impairment matters for iodinated contrast rather than for this study."],
  ["An implanted cardiac pacemaker",
   "A pacemaker is not among the listed contraindications for this study."],
  ["Atrial fibrillation",
   "Atrial fibrillation is a reason to look for appendage thrombus rather than a contraindication."]],
 "c": 0, "cite": c(26)},
]
