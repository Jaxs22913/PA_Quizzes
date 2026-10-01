# -*- coding: utf-8 -*-
# PDM I Lecture 8 (Cardiac Imaging and Vascular Studies, Ayelet Elwaya) -- pool M.
# Fourteen extra questions for the cumulative master exams. They target facts the
# 64 questions in pools A and B under-use or skip: the silhouette borders (slide 5),
# the exercise-test endpoint chart (slide 36), the pharmacological stress agents
# (slide 38), the prognostic use of nuclear perfusion imaging (slide 50), the signal
# source and limitations of magnetic resonance (slides 54 and 58), electrophysiology
# technique (slide 64), the angiography treatment indication (slides 71-72),
# claudication (slide 16), the Doppler addition (slide 20), the history that bars a
# transesophageal study (slide 26), sedation for it (slide 25) and gating (slide 41).
#
# No figure appears in any stem here, so the number-with-scale rule is met by having
# no numbers at all, and nothing asks for a calculation.
#
# Correct answer is ALWAYS written first (c=0); the master builder rotates.
SRC = "Cardiac Imaging and Vascular Studies - Elwaya.pptx"
def c(n):  return f"{SRC}, Slide {n}"

IOA = "Identify common abnormal cardiovascular imaging findings"
IOS = "Identify structures comprising the cardiac silhouette"
IOC = "Compare and contrast cardiovascular imaging modalities"
IOD = "Discuss indications, advantages, and limitations of echocardiography"
IOE = "Discuss indications, advantages, and limitations of stress testing"
IOF = "Discuss indications, advantages, and limitations of nuclear cardiology studies"
IOG = "Discuss indications, advantages, and limitations of cardiac CT"
IOH = "Discuss indications, advantages, and limitations of cardiac MRI"
IOI = "Discuss indications, advantages, and limitations of coronary angiography"

POOL_M = [

{"topic": "Chest radiography", "io": IOS, "slot": "anatomy",
 "q": "Which structure forms the upper part of the right heart border on a posteroanterior chest radiograph?",
 "opts": [
  ["Superior vena cava",
   "Correct. It sits above the right atrium along the right border, whereas the aortic knuckle, pulmonary artery segment, left atrial appendage and left ventricle all lie along the left."],
  ["Aortic knuckle",
   "The aortic knuckle forms the top of the left heart border, not the right; the superior vena cava occupies the upper right border."],
  ["Main pulmonary artery segment",
   "The pulmonary artery segment lies on the left border beneath the aortic knuckle; the right border above the atrium is the superior vena cava."],
  ["Left atrial appendage",
   "The left atrial appendage is part of the left border, between the pulmonary artery segment and the left ventricle, not the right border."]],
 "c": 0, "cite": c(5)},

{"topic": "Exercise stress test", "io": IOE, "slot": "interpretation",
 "q": "Which of these is a provider-determined reason to end an exercise stress test?",
 "opts": [
  ["Exertional hypotension",
   "Correct. A fall in systolic pressure below the resting standing value is a provider-determined endpoint, alongside extreme pressures, a patient who looks unwell and dangerous rhythms."],
  ["The patient wanting to stop",
   "That is a patient-determined endpoint, in the same group as chest discomfort, severe dyspnea and fatigue, rather than a provider-determined one."],
  ["Leg cramps or joint discomfort",
   "Cramps and joint discomfort are other limiting symptoms reported by the patient, so they are patient-determined rather than provider-determined endpoints."],
  ["A workload target set in advance",
   "A predetermined workload or heart rate is a protocol-determined endpoint used in submaximal tests, not one the provider decides during the test."]],
 "c": 0, "cite": c(36)},

{"topic": "Pharmacological stress test", "io": IOE, "slot": "mechanism",
 "q": "A pharmacological stress test is planned using a drug that increases the workload of the heart rather than dilating the coronary arteries. Which drug is it?",
 "opts": [
  ["Dobutamine",
   "Correct. It raises the work the heart performs, which is how it provokes ischemia, whereas adenosine and dipyridamole act by dilating the coronary arteries."],
  ["Adenosine",
   "Adenosine is used to vasodilate the coronary arteries rather than to increase the workload of the heart, which is the role of dobutamine."],
  ["Dipyridamole",
   "Dipyridamole, like adenosine, vasodilates the coronary arteries; the agent that increases cardiac workload instead is dobutamine."],
  ["Metoprolol",
   "Metoprolol slows the heart, as it is used to do before cardiac computed tomography, which is the opposite of increasing the workload of the heart."]],
 "c": 0, "cite": c(38)},

{"topic": "Nuclear cardiology", "io": IOF, "slot": "indication",
 "q": "Besides diagnosing coronary artery disease, which use is described for radionuclide myocardial perfusion imaging?",
 "opts": [
  ["Predicting future cardiac events",
   "Correct. Prognosis is a stated indication, since the study identifies patients at increased risk of myocardial infarction and those who may need angiography or surgery."],
  ["Measuring pulmonary artery occlusion pressure",
   "Occlusion pressure is measured during right heart catheterization; perfusion imaging shows tracer uptake and blood flow, not intracardiac pressures."],
  ["Identifying cardiac tumors such as myxoma",
   "Tumor identification is a use of transesophageal echocardiography; perfusion imaging assesses blood flow to the heart muscle rather than masses."],
  ["Locating the origin of an arrhythmia",
   "Locating an arrhythmia is done by electrophysiological testing; perfusion imaging compares stress and rest blood flow to the heart muscle."]],
 "c": 0, "cite": c(50)},

{"topic": "Cardiovascular magnetic resonance", "io": IOH, "slot": "mechanism",
 "q": "What does cardiovascular magnetic resonance map to build its three-dimensional images?",
 "opts": [
  ["Hydrogen atoms",
   "Correct. Strong magnetic fields and radiofrequency pulses are used to map hydrogen atoms, giving very detailed anatomy of the heart and great vessels."],
  ["Iodinated contrast pooling in vessels",
   "Magnetic resonance needs no iodinated contrast, which is one of its advantages; the image comes from hydrogen atoms in the tissue itself."],
  ["Reflected high-frequency sound pulses",
   "Reflected sound forms an ultrasound or echocardiographic image; magnetic resonance maps hydrogen atoms using magnetic fields and radiofrequency."],
  ["Gamma rays emitted by an injected tracer",
   "Gamma emission from a radioactive tracer forms a nuclear perfusion image; magnetic resonance uses no radioactive tracer and no ionizing radiation, only hydrogen atoms in the tissue."]],
 "c": 0, "cite": c(54)},

{"topic": "Cardiovascular magnetic resonance", "io": IOH, "slot": "limitation",
 "q": "Which is a recognized limitation of cardiovascular magnetic resonance?",
 "opts": [
  ["Lengthy acquisition time",
   "Correct. Along with claustrophobia, a distorted electrocardiogram and the need for electrocardiographic and respiratory gating, the long scan is one of its recognized drawbacks."],
  ["Interference from lung and bone",
   "Magnetic resonance has no interference from lung or bone; that is an advantage over ultrasound, which air and bone degrade."],
  ["Exposure to ionizing radiation",
   "Magnetic resonance uses no ionizing radiation, which is an advantage; radiation is a disadvantage of computed tomography and nuclear studies."],
  ["Dependence on iodinated contrast",
   "Magnetic resonance has intrinsic high contrast and needs no iodinated contrast; contrast dependence is a disadvantage of computed tomography."]],
 "c": 0, "cite": c(58)},

{"topic": "Electrophysiological testing", "io": IOI, "slot": "procedure",
 "q": "How are the catheters for electrophysiological testing introduced?",
 "opts": [
  ["Through veins into the right heart",
   "Correct. Three or four catheters pass from the internal jugular, subclavian or common femoral vein into the right atrium or right ventricle."],
  ["Through arteries into the left ventricle",
   "Electrophysiological catheters are placed through veins into the right heart; arterial access to the left side is used for left heart catheterization."],
  ["Down the esophagus on an endoscope",
   "The esophageal route belongs to transesophageal echocardiography; electrophysiological catheters are passed through veins into the right atrium or ventricle."],
  ["Into each coronary artery through the aorta",
   "Entering each coronary artery is how angiography is done; electrophysiological catheters go through veins into the right atrium or right ventricle."]],
 "c": 0, "cite": c(64)},

{"topic": "Electrophysiological testing", "io": IOI, "slot": "procedure",
 "q": "How does electrophysiological testing identify a reproducible arrhythmia?",
 "opts": [
  ["Electrical stimulation of different heart areas",
   "Correct. The rhythm is recorded while different areas are stimulated with electrical impulses, revealing reproducible arrhythmias and their exact origin."],
  ["Injection of contrast into each coronary artery",
   "Contrast injection is how coronary angiography shows blockages; it does not reveal the origin of an arrhythmia, which stimulation and recording do."],
  ["Comparison of tracer uptake at stress and rest",
   "Stress and rest tracer comparison is nuclear perfusion imaging, which assesses blood flow; arrhythmia origin is found by stimulation and recording."],
  ["Timing blood pressure during treadmill stages",
   "Blood pressure at exercise stages belongs to the exercise stress test; arrhythmias are provoked and located by electrical stimulation and recording."]],
 "c": 0, "cite": c(64)},

{"topic": "Coronary angiography", "io": IOI, "slot": "advantage",
 "q": "A patient with an acute myocardial infarction needs the coronary arteries imaged and treated in the same procedure. Which study is appropriate?",
 "opts": [
  ["Coronary angiography",
   "Correct. Acute infarction is a listed indication, and balloon angioplasty or stent placement can be done during the same catheter procedure."],
  ["Coronary computed tomography angiography",
   "It assesses the coronary arteries noninvasively but cannot treat a blockage, so it cannot image and treat the vessel in one procedure."],
  ["Radionuclide perfusion imaging",
   "It shows tracer uptake and viability but is purely diagnostic; only a catheter study can open a blocked artery during the same sitting."],
  ["Cardiovascular magnetic resonance",
   "It shows anatomy, function and viability without radiation but offers no treatment; stent or balloon therapy needs a catheter in the coronary artery."]],
 "c": 0, "cite": c(72)},

{"topic": "Vascular ultrasound", "io": IOC, "slot": "indication",
 "q": "Which study is used to evaluate a patient with claudication and suspected peripheral arterial disease?",
 "opts": [
  ["Arterial vascular ultrasound",
   "Correct. Evaluation of claudication and peripheral arterial disease is a listed indication, and it is fast, portable and free of ionizing radiation."],
  ["Transthoracic echocardiography",
   "It evaluates chamber size, ventricular function and valves in the heart, not the arteries of the legs affected in claudication."],
  ["Non-contrast cardiac computed tomography",
   "It is used for coronary artery calcium scoring in the heart rather than for evaluating leg arteries in claudication or peripheral arterial disease."],
  ["Electrophysiological testing",
   "It investigates and treats cardiac rhythm disorders and says nothing about the arteries supplying the legs, which vascular ultrasound assesses."]],
 "c": 0, "cite": c(16)},

{"topic": "Echocardiography", "io": IOD, "slot": "contraindication",
 "q": "Which history contraindicates a transesophageal echocardiogram?",
 "opts": [
  ["Odynophagia or dysphagia",
   "Correct. A history of painful or difficult swallowing is a contraindication, since a probe must be passed down the esophagus and swallowed to advance."],
  ["Cerebral ischemia",
   "Cerebral ischemia is an indication, because the study can find left atrial appendage thrombus as the source, rather than a contraindication."],
  ["A prosthetic heart valve",
   "Assessing a prosthetic valve and its current function is an indication for the transesophageal study, not a reason to avoid it."],
  ["Aortic dilation",
   "Aortic dilation, dissection and arteritis are indications for the transesophageal study, which shows the aorta in more detail than a chest wall view."]],
 "c": 0, "cite": c(26)},

{"topic": "Echocardiography", "io": IOD, "slot": "mechanism",
 "q": "What does Doppler add to an echocardiogram?",
 "opts": [
  ["Blood flow and velocity",
   "Correct. Doppler shows flow and velocity through the heart chambers and great vessels, which the grayscale picture of structure alone does not provide."],
  ["Myocardial tracer uptake",
   "Tracer uptake is what nuclear perfusion imaging measures with a gamma camera; Doppler uses sound to measure flow and velocity, not a tracer."],
  ["The coronary calcium burden",
   "Calcium scoring is a non-contrast cardiac computed tomography measurement; Doppler adds blood flow and velocity to the echocardiogram instead."],
  ["Electrical conduction pathways",
   "Conduction is investigated by electrophysiological testing; Doppler adds information about blood flow and its velocity through the heart."]],
 "c": 0, "cite": c(20)},

{"topic": "Cardiac computed tomography", "io": IOG, "slot": "procedure",
 "q": "Why is cardiac computed tomography synchronized with an electrocardiogram?",
 "opts": [
  ["To view different stages of the cardiac cycle",
   "Correct. Because the heart is constantly moving, tying the scan to the tracing lets the heart be evaluated at chosen points in the cycle."],
  ["To slow the heart during the scan",
   "Slowing the heart is done with medication such as metoprolol; the electrocardiogram synchronizes the scan to the cardiac cycle but does not slow the rate."],
  ["To provoke ischemia while images are taken",
   "Provoking ischemia is the purpose of stress testing; the scan is synchronized to the tracing so the heart is imaged at set points of its cycle."],
  ["To locate the origin of an arrhythmia",
   "Locating an arrhythmia is the work of electrophysiological testing; here the tracing only times the scan to the stages of the cardiac cycle."]],
 "c": 0, "cite": c(41)},

{"topic": "Echocardiography", "io": IOD, "slot": "procedure",
 "q": "Why is an intravenous sedative given before a transesophageal echocardiogram?",
 "opts": [
  ["To relax the patient and prevent vomiting",
   "Correct. The sedative helps the patient relax and prevents vomiting while the probe is passed through the mouth and down the esophagus."],
  ["To slow the heart for clearer images",
   "Slowing the heart for images is the role of medication before cardiac computed tomography; the sedative here relaxes the patient and prevents vomiting."],
  ["To numb the back of the throat",
   "A local anesthetic applied to the back of the throat does the numbing; the intravenous sedative relaxes the patient and prevents vomiting."],
  ["To prevent a reaction to contrast",
   "The sedative is given to relax the patient and prevent vomiting while the probe is passed, not to prevent a reaction to contrast; transesophageal echocardiography does not use iodinated contrast."]],
 "c": 0, "cite": c(25)},
]
