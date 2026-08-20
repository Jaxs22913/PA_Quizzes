#!/usr/bin/env python3
"""Build the Principles of Diagnostic Medicine I, Exam 1 cram sheet.

Condensed from the exam's own guide. Two rows are not condensations of the deck
but of Professor Reynolds' stated exam scope, because knowing what you do NOT
have to memorise is worth as much the night before as any fact.
"""
import sys, os
sys.path.insert(0, "/Users/jaxonluke/Developer/PA_Quizzes/tools/cram-sheet-template")
from render import render

OUT = "/Users/jaxonluke/Developer/PA_Quizzes/Principles of Diagnostic Medicine I Exam 1/pdm-exam-1-cram-sheet.html"

topics = [
 {"id": "scope", "label": "How This Exam Is Written", "color": "#69406c", "rows": [
   ["Reference ranges are GIVEN",
    "“I'm not going to just throw a random number at you” — normal ranges are always supplied, on this exam and in every class. Do not spend the night memorising cutoffs; spend it on what a value means."],
   ["Tests, not diagnoses",
    "“More related to the tests themselves rather than maybe the specific diagnosis.” What to order, why, its limits, how to read it. The instructional objectives are the blueprint."],
   ["No predictive-value math",
    "“We're not gonna do math, I'm not gonna make you do math.” Know which DIRECTION prevalence pushes positive predictive value and why — never the formula."],
   ["Question style",
    "Vignette and next-best-test: “which of the following laboratory tests would be best to evaluate…”, “what would be the next test that you would order?” Images (x-ray, CT, rhythm strip) may accompany the vignette."],
 ]},
 {"id": "phases", "label": "The Three Phases", "color": "#8f5f92", "rows": [
   ["Pretest = preanalytical", "Begins with patient preparation, extends until the test begins. History and risk, contraindications, coping styles and fears, universal precautions, documentation, cost, education, consent."],
   ["MOST ERRORS ARE PRETEST", "The single most testable fact here. Communication errors, medication administration, labeling; technical errors — inadequate tube fill, transport delay, wrong storage; inappropriate preparation — fasting."],
   ["Variables affecting results", "Patient preparation · current drug therapy · time of collection · physical activity · hydration · age · sex · body mass index."],
   ["Intratest = analytical", "Performing the test: collection, monitoring the environment, comfort, analgesics and sedatives, vital signs, universal precautions, minimising delays, watching for complications."],
   ["Posttest = postanalytical", "Aftercare. Complications: bleeding, infection, respiratory difficulty, perforation, sedation effects. Interpret, IDENTIFY AND TREAT CRITICAL VALUES, communicate clearly and sensitively."],
   ["Integration & follow-up", "Diagnosis, acceptance, healing, health-promoting behaviour. Education, follow-up labs and appointments, referrals, emotional well-being. “If it wasn't documented, it wasn't done.”"],
 ]},
 {"id": "tubes", "label": "Order of Draw & Tubes", "color": "#7a5a2e", "rows": [
   ["Stop Light Red Stay Put Green Light Go",
    "Yellow (sterile/blood culture) → Light blue (citrate/COAGS) → Red (non-additive) → Gold SST → Green PST → Green (heparin) → Lavender (EDTA/CBC) → Gray (glycolytic inhibitor). She wants THE ORDER and the broad category, not the full additive table."],
   ["The four pairings to know cold", "Light blue = coagulation. Lavender = complete blood count. Yellow = blood cultures. Gray = glucose."],
   ["Why the order exists", "To avoid cross-contamination of additives between tubes. Carry EDTA into a chemistry tube and the potassium reads wrong."],
   ["Clear tube", "Nonadditive discard tube — fills the collection set's dead space before the coagulation tube when no royal blue is drawn."],
 ]},
 {"id": "specimens", "label": "Stool, Blood, Sputum & Throat", "color": "#3f6b5a", "rows": [
   ["Get it BEFORE antibiotics", "Stated for blood, sputum and throat cultures alike. The single rule spanning them."],
   ["Ova & parasites", "DO NOT REFRIGERATE — warm stool is best. THREE separate random specimens, because of the parasite life cycle. Specimen free of urine or other secretions, dry clean container."],
   ["Guaiac", "Heme oxidises hydrogen peroxide in the guaiac → BLUE = POSITIVE. Use a SMALL sample; a large one obscures the result. Can be done off the gloved finger after digital rectal exam."],
   ["Blood cultures", "Acute febrile illness with suspected septicemia. Diagnostic AND therapeutic (pathogen + sensitivities). TWO samples from OPPOSITE ARMS, ideally pre-antibiotic. AEROBIC FIRST. Scrub, let dry, and do not palpate after disinfection unless sterile-gloved."],
   ["Sputum culture", "Two steps: GRAM STAIN first (positive vs negative), then culture for identification and sensitivities. Upright, rinse mouth with water, three deep breaths, deep cough. Aerosols may assist. Acid-fast bacilli from the same specimen."],
   ["Throat culture", "Streptococci, because of beta-hemolytic streptococcal pharyngitis; commonest ages 3–15. Tongue blade improves view, relaxes throat, reduces gag. Swab posterior throat, BOTH tonsils, any exudate — AVOID tongue and lips."],
 ]},
 {"id": "poct", "label": "Point-of-Care Testing & Regulation", "color": "#2f5b70", "rows": [
   ["Definition", "Testing completed OUTSIDE the centralized laboratory, at or close to the site of patient care. Near-patient, remote, satellite, rapid diagnostics."],
   ["Primary care menu", "Glucose · hemoglobin A1c · urinalysis · rapid influenza · rapid strep · fecal occult blood · pregnancy · cholesterol · PT/INR · drug screening. Rapidly increasing: fentanyl and HIV testing."],
   ["Acute care menu", "Venous blood gas · glucose · TROPONIN · brain natriuretic peptide · D-dimer · PT/INR · hemoglobin/hematocrit · rapid antigen · urine hCG · UA dipstick. Machines: portable x-ray, ECG, pulse oximetry, ultrasound."],
   ["Advantages vs limitations", "FOR: convenient, rapid, less manpower, fewer visits, fingerstick not needle stick, better care where resources are limited. AGAINST: expensive, quality assurance hard to control, operator and manufacturer variability, non-standard vocabulary, LESS PRECISE, supply needs."],
   ["Qualitative / semi-quant / quantitative", "Qualitative = rapid strep, flu, pregnancy (positive or negative). SEMI-QUANTITATIVE = urinalysis dipstick (matched to a chart). Quantitative = glucose (highest volume), chemistries, coags, cardiac markers — needs a reader."],
   ["CLIA complexity", "WAIVED = little harm from a false result; the Joint Commission calls all testing outside a traditional lab waived, i.e. POCT. MODERATELY COMPLEX = ~75% of the 12,000 tests, usually automated. HIGHLY COMPLEX = operator skill, e.g. cross match. PROVIDER-PERFORMED MICROSCOPY = provider reads a fresh slide."],
   ["Who does what", "CMS issues certificates, inspects, enforces. FDA categorizes tests by complexity. CDC provides standards, research, quality studies."],
   ["Regulation goes one way", "CLIA is the MINIMUM and cannot be downgraded, so state and city rules are always STRICTER. Every site licensed for ANY testing; licence matches complexity; reapply EVERY TWO YEARS."],
 ]},
 {"id": "stats", "label": "Sensitivity, Specificity & Predictive Value", "color": "#8a3f4a", "rows": [
   ["SnNout / SpPin", "High SENSITIVITY + Negative rules OUT (fewer false negatives; good at DETECTING; best for SCREENING). High SPECIFICITY + Positive rules IN (fewer false positives; good at EXCLUDING; best for CONFIRMING)."],
   ["One dial, two costs", "Move the threshold down to catch every case → false positives. Move it up to exclude cleanly → false negatives. You cannot maximise both, which is why HIV screening is sensitive first, confirmatory testing specific second."],
   ["Test-centered vs patient-centered", "Sensitivity and specificity belong to THE TEST. Positive and negative predictive value belong to THE POPULATION being tested."],
   ["The named trap", "“My patient's test is positive — do they have it?” feels like sensitivity. It is POSITIVE PREDICTIVE VALUE. Sensitivity = P(test+ | disease); PPV = P(disease | test+). That reversal is Bayes' theorem."],
   ["Frostbite — same test, two states", "95% sensitivity and specificity throughout. Michigan, prevalence 10% → PPV ~68%. Florida, prevalence 0.1% → PPV ~2%. Shark bite reverses the geography and the logic holds."],
   ["Pre-test vs post-test probability", "PRE-TEST = likelihood before the result, from signs, symptoms, history, risk factors, how common it is. POST-TEST = likelihood after, depending on sensitivity and specificity."],
   ["Prevalence vs incidence", "PREVALENCE = how COMMONLY something occurs (existing cases, usually a percentage). INCIDENCE = how OFTEN it happens."],
   ["Screening vs diagnostic", "SCREENING: asymptomatic, cheap, easy, indicates whether more testing is needed. DIAGNOSTIC: symptomatic, may be invasive, confirms. A screening test BECOMES diagnostic if an abnormality is found during it — e.g. colonoscopy."],
 ]},
 # ---------------- Lecture 2: Principles of Medical Imaging ----------------
 {"id": "modalities", "label": "The Modalities at a Glance", "color": "#3e5f8a", "rows": [
   ["Radiography", "Ionizing radiation, viewed in 2-D. Quick, cheap, available anywhere, portable — the most widely obtained study. Against: only FIVE densities, structures overlap, ionizing radiation (relatively low dose)."],
   ["Computed tomography", "Rotating fan beam, thousands of transmission points. EXPANDS THE GREY SCALE beyond five densities, reduces overlap, works with implanted devices, 3-D reconstruction. THE CORNERSTONE OF CROSS-SECTIONAL IMAGING. Against: not portable, a LOT of radiation, needs space and processing."],
   ["Ultrasound", "High-frequency sound from a transducer, bounced back. NO radiation — the SAFEST modality, and real time, so it is for MOVING structures: heart, vasculature, obstetrics. Colour Doppler adds flow DIRECTION and VELOCITY. Often first choice in the FEMALE PELVIS and in PAEDIATRICS. Against: cannot penetrate bone, gas disrupts it, deep structures are hard, OPERATOR-DEPENDENT."],
   ["Magnetic resonance", "Magnetic field aligns hydrogen; release emits radio waves — essentially a HYDROGEN MAP. Contrast is GADOLINIUM. Best for SOFT TISSUE, i.e. anything but bone; cornerstone of NEUROIMAGING and orthopaedic soft tissue. Calcium emits NO signal, so tissue inside bone is visible. Diffusion-weighted imaging for STROKE. Against: not widely available, expensive, slow, magnetic implants and ferromagnetic projectiles. Not recommended in pregnancy or infants despite no radiation."],
   ["PET vs SPECT", "PET = positrons, FDG-18 (radioactive glucose), 2-D, gamma camera — CANCER STAGING, brain disorders, cardiac blood flow; shows who is EATING GLUCOSE. SPECT = single photons, rotating gantry, 3-D, technetium-99 — heart disease, BONE SCANS, brain; shows WHERE BLOOD FLOWS."],
   ["Angiographic studies", "NOT one test — any modality can image vessels. X-ray → angiogram. Ultrasound → colour Doppler. CT angiography → iodine injected quickly. MR angiography → NO DYE NEEDED. Veins = venogram."],
   ["Fluoroscopy", "Ionizing radiation giving REAL-TIME video: motion, positioning, and barium or iodine moving through gut, urinary tract and vessels. Needs a specially fitted unit with a tilting table."],
 ]},
 {"id": "density", "label": "Density, Attenuation & Hounsfield", "color": "#7a5a2e", "rows": [
   ["Five densities, whitest → blackest", "METAL · CALCIUM (bone) · FLUID/SOFT TISSUE · FAT · AIR. Fluid and soft tissue have THE SAME DENSITY on a plain film — that is the pair you cannot separate."],
   ["Hounsfield numbers (SLIDE 13 — an IMAGE, not text)", "Air −1000 · Fat ~−40 to −120 · WATER = 0 BY CONVENTION · Soft tissue ~+20 to +100 · Bone ~+400 to +600 · Metal ~+1000 or higher. CT pulls WATER APART from soft tissue — the asterisk on the deck's “Five*”."],
   ["The vocabulary", "RADIOLUCENT = hypodense = DARKER, because MORE beam passed through (less absorbed). RADIOPAQUE = hyperdense = radiodense = WHITER, because LESS passed through (more absorbed)."],
   ["Attenuation", "INCREASED attenuation = high Hounsfield number = whiter (metal, calcium). DECREASED attenuation = low number = blacker (air, fat). Same substances read the same way on a plain film."],
   ["The WINDOW", "A pre-selected RANGE of Hounsfield numbers (e.g. −100 to +300) spread over the available grey scale. It is a DISPLAY choice, so POST-PROCESSING can re-window the same scan to show different pathology WITHOUT repeating the study or re-exposing the patient."],
   ["Units", "Radiation is measured in milliSieverts (mSv) and milliGrays (mGy). One gray = one joule per kilogram. For x-ray radiation, 1 mSv = 1 mGy."],
 ]},
 {"id": "mri-weights", "label": "T1 vs T2 — the always-asked one", "color": "#2f5b70", "rows": [
   ["T2: water is WHITE", "High water content is BRIGHT — fat, oedema, infection, blood (hyperemia), cerebrospinal fluid. Low water content is dark grey."],
   ["T1: water is DARK", "Exactly the inverse. High water content is DARK; low water content is BRIGHT (white). Same list of tissues, opposite appearance."],
   ["How to check yourself", "Look at the ventricles. Bright CSF = T2. Dark CSF = T1."],
 ]},
 {"id": "positioning", "label": "Positioning & Planes", "color": "#3f6b5a", "rows": [
   ["Projections are named for THE BEAM", "From what it strikes FIRST to the most distal portion. Posterior-anterior = beam enters the back, exits the front."],
   ["Why PA is preferred", "REDUCES MAGNIFICATION OF THE HEART, so cardiomegaly is not misread (the heart is anterior, so on PA it sits near the detector). Also: lower dose to radiation-sensitive organs, maximum lung visualisation, better apices, posterior ribs well seen."],
   ["Standard chest exam", "PA AND LATERAL, READ TOGETHER. PA is viewed as if the patient stood in front of you — THEIR RIGHT ON YOUR LEFT. On the lateral the patient faces LEFT. Comparison films are “old gold”: old PA beside new PA, old lateral beside new lateral."],
   ["Position → indication", "DECUBITUS = PLEURAL EFFUSION (gravity levels the fluid out). KUB = supine, AP, genitourinary tract. ABDOMINAL SERIES = STANDING, AP, gastrointestinal tract — air-fluid levels, free air, small bowel obstruction, perforation, volvulus."],
   ["Three planes", "AXIAL (transverse) = upper/lower, much the commonest. CORONAL = anterior/posterior. SAGITTAL = right/left; in the midline it is MIDSAGITTAL (median), off to either side PARASAGITTAL."],
   ["Cross-sectional viewing convention", "CT/MRI/nuclear: patient SUPINE, transverse sections viewed AS IF LOOKING AT THE PATIENT'S FEET — so the PATIENT'S LEFT IS ON THE READER'S RIGHT. Note this is the OPPOSITE of how a PA chest film is oriented."],
   ["Ultrasound indicator — “crucial”", "Cardiac imaging: indicator on the RIGHT of the screen. EVERY other ultrasound: on the LEFT. Get it wrong and left and right are mirrored."],
 ]},
 {"id": "radiation", "label": "Radiation Risk", "color": "#8a3f4a", "rows": [
   ["The highest emitters", "Marked IMPORTANT in the deck: CT, PET and SPECT are the HIGHEST-EMITTING medical imaging devices currently in existence. Ultrasound and MRI emit NONE."],
   ["Organ doses (SLIDE 21 — an IMAGE; the text extracts as EMPTY)", "Dental 0.005 · PA chest 0.01 · lateral chest 0.15 · screening mammography 3 · ADULT abdominal CT 10 · barium enema 15 · NEONATAL abdominal CT 20 (mGy or mSv). FOUR ORDERS OF MAGNITUDE across the table."],
   ["The neonatal point", "Neonatal abdominal CT doses TWICE the adult study. Smaller patient, larger organ dose for the same scan — which is exactly why the diagnostic approach asks whether something with less radiation would do."],
   ["Nuclear medicine is different in KIND", "The tracer is inside the patient, so for a while THE PATIENT IS THE SOURCE and can briefly expose other people. No other modality does this."],
 ]},
 {"id": "contrast", "label": "Contrast Media", "color": "#69406c", "rows": [
   ["CT intravenous — Omnipaque (iohexol)", "A radioactive form of IODINE. NEPHROTOXIC → CHECK BUN AND CREATININE, give 1 L NORMAL SALINE to protect the kidneys. For inflammation, cancer staging, tumour delineation, vasculopathy, emboli, thrombi, stenosis, aneurysm."],
   ["CT oral — barium or Gastrografin", "BARIUM IS CONTRAINDICATED IF PERFORATION IS SUSPECTED — it is toxic to extra-intestinal tissue and causes alkaline burns. USE GASTROGRAFIN instead. For the intraluminal space, upper oesophagus to rectum."],
   ["MRI — gadolinium", "Assess BUN and creatinine regardless, but it is NOT as harmful as CT contrast; renal function matters mainly for clearance. For CNS tumours (typically characterised WITHOUT biopsy), metastases, soft tissue masses, arthrograms. MRA and MRV are done WITHOUT contrast."],
   ["PET — fluorodeoxyglucose-18", "NO contraindications, NOT known to be nephrotoxic. May cause HYPERGLYCAEMIA. Renally cleared, so the genitourinary tract is ALWAYS contrast positive."],
   ["SPECT — technetium-99", "Travels to areas of higher blood flow and cellular activity. Bone scans, myocardial perfusion, functional brain imaging, immunoscintigraphy, sentinel node, white cell uptake. Allergic reactions RARE, NO organ damage documented."],
   ["SHELLFISH IS NOT IODINE", "There should be NO CROSS-REACTIVITY between shellfish allergy and iodinated radiocontrast. The real high-risk marker is a documented ANAPHYLACTIC REACTION TO ANY MEDICATION. Pre-treatment exists when contrast is necessary."],
   ["The stated takeaway", "ALWAYS ASK ABOUT ALLERGIES AND ASSESS KIDNEY FUNCTION. Also: all contrast is technically radioactive, so the deck names CANCER as a risk factor for all of it."],
   ["Other routes", "Joints = arthrogram. Central nervous system = intrathecal. Bladder = retrograde pyelogram."],
 ]},
 {"id": "radiology-team", "label": "The Radiology Relationship", "color": "#5a6b3a", "rows": [
   ["They have not seen the patient", "Whatever clinical information you give is what guides the read. A vague report is a CONVERSATION — contact the radiologist and discuss the patient."],
   ["Unsure which study?", "Tell them WHAT YOU ARE LOOKING FOR and they can guide the choice."],
   ["Multiple regions = multiple orders", "MRI brain, C-spine, T-spine and L-spine is FOUR requests, not one."],
 ]},
]

html = render(
    title="Cram Sheet — Principles of Diagnostic Medicine I Exam 1",
    kicker="Principles of Diagnostic Medicine I Exam 1 · Class of 2028",
    h1="Principles of Diagnostic Medicine I Exam 1 Cram Sheet",
    sub="Lectures 1 and 2. Laboratory diagnostics — the phases, the order of draw, the specimen studies, point-of-care testing and its regulation, and the statistics. Then medical imaging — the modalities, density and the Hounsfield scale, T1 against T2, positioning and the planes, radiation dose and contrast media. Opens with how Professor Reynolds said this exam is written.",
    topics=topics,
    guide_href="pdm-exam-1-study-guide.html",
    footer_note="Condensed from the Principles of Diagnostic Medicine I Exam 1 Study Guide (Class of 2028). Covers Lectures 1 and 2; Exam 1 spans Lectures 1–6 and Lab 1, and topics are added as each deck is posted. Exam-scope rows are quoted from the 2026-08-18 lecture recording. Two imaging rows are flagged as coming from slides that exist only as images — their content is in no text version of the deck.",
)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.basename(OUT), len(html)//1024,
      len(topics), sum(len(t["rows"]) for t in topics)))
