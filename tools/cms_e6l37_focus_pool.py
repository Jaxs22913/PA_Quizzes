# -*- coding: utf-8 -*-
"""Lecture 37 STUDY-FOCUS pool, regular (non-vignette) items -- written 2026-10-31 for the focus points the
existing Lecture 37 pools left thin or missing (tools/cms_e6_focus_coverage.json): local antibiograms and
de-escalation in hospital-acquired and ventilator-associated pneumonia, Pneumocystis sampling and the limit of
a positive polymerase chain reaction, histoplasmosis by severity, pneumococcal sequencing after the 15-valent
conjugate vaccine, and outpatient regimens with versus without comorbidities.

NOT a topic-quiz pool: the file name does not match cms_e6l37_pool_*.py, so cms_e6_partition.py (the Lecture
37 topic quizzes) never reads it. Read by tools/cms_e6_focus_partition.py (the two Study Focus sets) and
tools/cms_e6_masters_partition.py (master candidates once cleanly reviewed), both through the Lecture 37
guards. Each question carries "focus": the study-focus point ids it practises (tools/cms_e6_focus_points.py).

WRITER.md v1 + EXPLAIN_DEEP.md: key authored first, misconception tag on every distractor, every claim on a
slide of the cited deck (the study-focus slide 127 counts as slide content).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l37_scope import *


def S(topic, io, q, opts, cite, slot, focus):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; d["focus"] = list(focus); return d


VAX = "Vaccines"
PNA = "Pneumonia antibiotics"
HAP = "Hospital and ventilator pneumonia"
PJP = "Pneumocystis"
FUN = "Histoplasmosis and cryptococcosis"

QUESTIONS = [

S(HAP, IO_B,
  "Which factors select the empiric antibiotic regimen for hospital-acquired pneumonia?",
  [["Local antibiogram and patient resistance risk",
    "Correct. For hospital-acquired and ventilator-associated pneumonia, empiric therapy follows the local antibiogram and the patient's own resistance risks, with prior cultures and recent antibiotics. A common backbone is an antipseudomonal beta-lactam such as cefepime or piperacillin-tazobactam, chosen by that local data."],
   ["Whether onset was early or late in the stay",
    "Onset timing matters for naming the pneumonia (hospital-acquired begins 48 hours or more after admission), but early versus late timing alone does not select the regimen. Tell: the regimen comes from local resistance data, prior cultures and recent antibiotics, not from the day count.", "adjacent fact"],
   ["Nursing-home residence before admission",
    "The health care-associated pneumonia category is retired, and therapy is not based on it: nursing-home residence or health care exposure alone does not mandate broad-spectrum therapy. Tell: hospital-acquired pneumonia is treated by the local antibiogram and the patient's resistance risk, not by where the patient lived.", "adjacent fact"],
   ["The color of the patient's sputum",
    "Sputum color does not establish a bacterial cause or choose an antibiotic; antibiotics treat a bacterial syndrome, not sputum color. Tell: for hospital-acquired pneumonia the empiric choice rests on the local antibiogram and the patient's resistance risks.", "common lay belief"]],
  CS(25, 39, 42, 46, 126), "agent/regimen", ["l37-antibiogram"]),

S(HAP, IO_B,
  "In hospital-acquired or ventilator-associated pneumonia, when is empiric antibiotic therapy narrowed or stopped?",
  [["As cultures and the course clarify it",
    "Correct. Respiratory specimens are collected before empiric therapy, then therapy is narrowed or stopped as culture results and the clinical course clarify the diagnosis. De-escalation is prompt, and the usual total course is 7 days when the response is adequate."],
   ["After the full 7-day course ends",
    "Seven days is the usual total duration with an adequate response, but de-escalation is not saved for the end. Tell: therapy is de-escalated promptly, as soon as cultures and the clinical course allow, within that course.", "adjacent fact"],
   ["Once the patient has been extubated",
    "Early extubation is a ventilator-associated pneumonia prevention measure, not the trigger for narrowing antibiotics. Tell: de-escalation follows the culture results and the clinical course, whether or not the patient is still ventilated.", "adjacent fact"],
   ["When a repeat chest film has cleared",
    "Narrowing is not tied to a clear chest film; the rule is to narrow or stop as culture results and the clinical course clarify the diagnosis. Tell: the decision rests on cultures and response, so waiting for imaging keeps broad coverage longer than needed.", "common lay belief"]],
  CS(42, 46, 49), "agent/regimen", ["l37-deescalate", "l37-hap-cultures"]),

S(PJP, IO_B,
  "What is the main limitation of a positive Pneumocystis polymerase chain reaction result?",
  [["It can detect colonization",
    "Correct. Polymerase chain reaction for Pneumocystis on induced sputum or bronchoalveolar lavage is highly sensitive but can detect colonization, so a positive result is interpreted with the symptoms, the imaging and the organism burden rather than read as proof of pneumonia."],
   ["It has low sensitivity",
    "This reverses the real problem: the polymerase chain reaction is highly sensitive. Its weakness is the opposite problem, a positive result from colonization. Tell: a sensitive test's risk is a positive that does not mean disease, so weigh symptoms, imaging and organism burden.", "reversed direction or value"],
   ["It cannot be run on induced sputum",
    "Induced sputum is one of the two recommended specimens: induced sputum or bronchoalveolar lavage is sent for microscopy and/or polymerase chain reaction. Tell: the specimen to avoid relying on is spontaneously expectorated sputum, which has poor sensitivity.", "adjacent fact"],
   ["It needs a lung biopsy specimen",
    "Lung biopsy is rarely needed and is kept for when less invasive studies are nondiagnostic; the test is run on induced sputum or lavage fluid. Tell: the limitation of the result is colonization, not the specimen it needs.", "adjacent fact"]],
  CS(65, 67, 69), "test finding", ["l37-pcr-limits"]),

S(PJP, IO_B,
  "For suspected Pneumocystis pneumonia, which respiratory specimen is obtained first when it is feasible?",
  [["Induced sputum",
    "Correct. Induced sputum is obtained for microscopy and/or polymerase chain reaction when feasible; if it is negative or unavailable and suspicion remains high, bronchoalveolar lavage follows. A negative induced specimen does not exclude Pneumocystis pneumonia."],
   ["Spontaneously expectorated sputum",
    "Spontaneously expectorated sputum has poor sensitivity and should not be used to exclude infection. Tell: the sputum sample for Pneumocystis is induced, and a negative one leads on to bronchoalveolar lavage when suspicion stays high.", "adjacent fact"],
   ["Lung biopsy tissue",
    "Lung biopsy is rarely needed and comes only when less invasive studies are nondiagnostic. Tell: start with induced sputum, then bronchoalveolar lavage; biopsy is not the first sample.", "wrong stage or severity"],
   ["Bronchoalveolar lavage fluid",
    "Bronchoalveolar lavage is the next specimen, considered when induced sputum is negative or unavailable and suspicion remains high, with its yield balanced against respiratory instability. Tell: when induced sputum is feasible it comes first, and lavage follows a negative result.", "wrong stage or severity"]],
  CS(65, 66, 67, 69), "initial test", ["l37-pjp-sampling"]),

S(FUN, IO_B,
  "How is severe pulmonary or disseminated histoplasmosis treated?",
  [["Amphotericin-based induction",
    "Correct. Treatment follows severity and host risk: severe pulmonary or disseminated histoplasmosis requires specialist-led amphotericin-based induction. Mild acute disease in an immunocompetent adult often needs only observation, and itraconazole is considered for prolonged or progressive illness or higher-risk hosts."],
   ["Observation without antifungals",
    "Observation is the usual plan for mild acute disease in an immunocompetent adult, the opposite end of the severity range. Tell: severe pulmonary or disseminated disease is the case for specialist-led amphotericin-based induction.", "wrong stage or severity"],
   ["Oral itraconazole as an outpatient",
    "Itraconazole is considered for prolonged or progressive illness or higher-risk hosts, with monitoring of interactions and drug levels, and chronic cavitary disease takes prolonged azole therapy. Tell: severe or disseminated disease starts with amphotericin-based induction, not an oral azole alone.", "wrong stage or severity"],
   ["Fluconazole for 6 to 12 months",
    "Fluconazole for 6 to 12 months is the treatment for mild, isolated pulmonary cryptococcosis, a different fungal pneumonia. Tell: for histoplasmosis, severe pulmonary or disseminated disease needs specialist-led amphotericin-based induction.", "competing diagnosis"]],
  CS(78, 123), "escalation", ["l37-histo-severity"]),

S(VAX, IO_VAX,
  "In an eligible adult, what usually follows a dose of the 15-valent pneumococcal conjugate vaccine?",
  [["A 23-valent polysaccharide dose",
    "Correct. The 15-valent conjugate vaccine usually requires the 23-valent polysaccharide vaccine afterward, usually 1 year or more later. A 20- or 21-valent conjugate vaccine, by contrast, completes the series for an adult who has never had a conjugate vaccine."],
   ["Nothing; the series is complete",
    "A single dose completes the series only when it is the 20- or 21-valent conjugate vaccine. Tell: the 15-valent conjugate vaccine is the one that usually needs the 23-valent polysaccharide vaccine afterward.", "adjacent fact"],
   ["A second 15-valent conjugate dose",
    "The 15-valent conjugate vaccine is not repeated to finish the adult series; it is followed by the 23-valent polysaccharide vaccine, usually 1 year or more later. Tell: the second product is a different vaccine type, the polysaccharide one.", "common lay belief"],
   ["A yearly pneumococcal booster",
    "Pneumococcal vaccination is not given every year; yearly vaccination is the influenza rule. Tell: after the 15-valent conjugate vaccine, one 23-valent polysaccharide dose usually follows, about 1 year or more later.", "adjacent fact"]],
  CS(8, 9, 124), "agent/regimen", ["l37-pneumo-seq"]),

S(PNA, IO_B,
  "Four adults have community-acquired pneumonia, are stable for outpatient treatment and have no risk for methicillin-resistant Staphylococcus aureus or Pseudomonas. Which one fits amoxicillin as a single drug?",
  [["The one with no chronic conditions",
    "Correct. Amoxicillin, or doxycycline, is the outpatient choice when there are no comorbidities and no methicillin-resistant Staphylococcus aureus or Pseudomonas risk. Each of the others has a listed comorbidity, which calls for a beta-lactam plus azithromycin or doxycycline, or a respiratory fluoroquinolone."],
   ["The one with diabetes mellitus",
    "Diabetes is on the comorbidity list, so this patient needs amoxicillin-clavulanate, cefpodoxime or cefuroxime plus azithromycin or doxycycline, or a respiratory fluoroquinolone. Tell: amoxicillin alone is reserved for the outpatient with no comorbidities.", "ruled out by a stated finding"],
   ["The one with chronic liver disease",
    "Chronic liver disease is a listed comorbidity, which moves this patient to the combination regimen (a beta-lactam such as amoxicillin-clavulanate plus azithromycin or doxycycline) or a respiratory fluoroquinolone. Tell: any listed comorbidity rules out amoxicillin alone.", "ruled out by a stated finding"],
   ["The one with asplenia",
    "Asplenia is a listed comorbidity, alongside chronic heart, lung, liver or renal disease, diabetes, alcoholism and malignancy, so this patient takes the comorbidity regimen. Tell: amoxicillin alone fits only the patient without comorbidities.", "ruled out by a stated finding"]],
  C(43), "first-line", ["l37-op-nocomorb", "l37-op-comorb"]),
]
