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
]

html = render(
    title="Cram Sheet — Principles of Diagnostic Medicine I Exam 1",
    kicker="Principles of Diagnostic Medicine I Exam 1 · Class of 2028",
    h1="Principles of Diagnostic Medicine I Exam 1 Cram Sheet",
    sub="Lecture 1, Principles of Laboratory Diagnostics — the phases, the order of draw, the specimen studies, point-of-care testing and its regulation, and the statistics. Opens with how Professor Reynolds said this exam is written.",
    topics=topics,
    guide_href="pdm-exam-1-study-guide.html",
    footer_note="Condensed from the Principles of Diagnostic Medicine I Exam 1 Study Guide (Class of 2028). Covers Lecture 1; Exam 1 spans Lectures 1–6 and Lab 1, and topics are added as each deck is posted. Exam-scope rows are quoted from the 2026-08-18 lecture recording.",
)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)" % (os.path.basename(OUT), len(html)//1024,
      len(topics), sum(len(t["rows"]) for t in topics)))
