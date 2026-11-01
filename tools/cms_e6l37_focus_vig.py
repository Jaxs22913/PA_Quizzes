# -*- coding: utf-8 -*-
"""Lecture 37 STUDY-FOCUS pool, vignettes -- written 2026-10-31 for the focus points the existing Lecture 37
pools left thin or missing (tools/cms_e6_focus_coverage.json): cultures, local antibiograms and de-escalation
in hospital-acquired and ventilator-associated pneumonia, anaerobic coverage only for abscess or empyema,
aspiration pneumonia versus pneumonitis, the limit of a positive Pneumocystis polymerase chain reaction,
histoplasmosis by severity, pneumococcal sequencing, respiratory syncytial virus vaccine eligibility,
psittacosis and doxycycline, and a negative rapid influenza test in a high-risk patient past 48 hours.

NOT a topic-quiz pool (the name does not match cms_e6l37_vig_*.py). Read by tools/cms_e6_focus_partition.py
and tools/cms_e6_masters_partition.py through the Lecture 37 vignette guards. "focus" = the study-focus point
ids each question practises (tools/cms_e6_focus_points.py).

WRITER.md v1 + EXPLAIN_DEEP.md; every claim on a slide of the cited deck (the study-focus slide 127 counts).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e6l37_scope import *


def V(topic, io, q, opts, cite, slot, lead, focus):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; d["lead"] = lead; d["focus"] = list(focus); return d


VAX = "Vaccines"
HAP = "Hospital and ventilator pneumonia"
ASP = "Aspiration and lung abscess"
PJP = "Pneumocystis"
FUN = "Histoplasmosis and cryptococcosis"
ATY = "Psittacosis and Mycoplasma"
FLU = "Influenza"

QUESTIONS = [

# ---------------------------------------------------------------- bronchitis or pneumonia; severity and site of care
V("Acute bronchitis", IO_B,
  "A 48-year-old man has had a cough for 6 days with yellow sputum. His temperature is 101.8°F and his respiratory rate 24/min, and there are crackles with dullness to percussion over the left lower lobe. He asks for an antibiotic because his sputum is yellow. Which is the most appropriate next step?",
  [["A chest radiograph to confirm pneumonia",
    "Correct. Fever, a raised respiratory rate and focal crackles with dullness are the findings that raise concern for pneumonia rather than uncomplicated bronchitis, and suspected pneumonia is confirmed with a chest radiograph. The yellow sputum is not what changes the plan: the fever and focal findings are."],
   ["An antibiotic for the yellow sputum",
    "Purulent or colored sputum does not establish a bacterial infection and does not justify antibiotics. Tell: his fever and focal findings should prompt evaluation for pneumonia rather than empiric bronchitis antibiotics, and that evaluation starts with a chest radiograph, not with an antibiotic chosen for sputum color.", "common lay belief"],
   ["Supportive care for bronchitis",
    "Supportive care fits uncomplicated acute bronchitis, where consolidation should not be detected. Tell: focal crackles and dullness with fever are the cue to think pneumonia and image, not to treat as bronchitis.", "competing diagnosis"],
   ["A sputum culture before deciding",
    "Routine sputum culture is unnecessary in uncomplicated cases, and in pneumonia cultures are obtained selectively for severe disease, resistant-pathogen risk or treatment failure. Tell: the test that answers his question, is this pneumonia, is the chest radiograph.", "wrong stage or severity"]],
  CS(15, 16, 18, 29), "initial test", "next step", ["l37-bronch-vs-pna", "l37-sputum-color", "l37-cap-confirm"]),

V("Pneumonia workup and severity", IO_B,
  "A 47-year-old woman with community-acquired pneumonia has a Pneumonia Severity Index total of 82 points. After intravenous fluids she remains hypotensive and needs a vasopressor infusion to maintain her blood pressure. She is breathing on her own. Where should she be treated?",
  [["Intensive care unit-level care",
    "Correct. Vasopressor-dependent shock is one of the severity signals of severe community-acquired pneumonia, with mechanical ventilation or at least three minor criteria, and severe pneumonia needs urgent intensive care-level assessment and circulatory support. The Pneumonia Severity Index guides the outpatient-or-ward choice only in nonsevere pneumonia."],
   ["A general ward, by her score",
    "The Pneumonia Severity Index with clinical judgment chooses between outpatient care and a general ward for nonsevere pneumonia. Tell: her need for a vasopressor makes the pneumonia severe whatever her point total, which moves her to intensive care-level care.", "wrong stage or severity"],
   ["Outpatient care with close follow-up",
    "Outpatient care is an option only for nonsevere pneumonia chosen with the Pneumonia Severity Index and clinical judgment. Tell: a patient who needs a vasopressor to keep her blood pressure up has severe community-acquired pneumonia.", "wrong stage or severity"],
   ["An observation unit for a repeat score",
    "Waiting to repeat a score delays care: severity changes the site of care, and vasopressor-dependent shock already defines severe pneumonia. Tell: severe community-acquired pneumonia calls for urgent intensive care-level assessment, not another total.", "wrong stage or severity"]],
  CS(30, 45), "referral", "referral", ["l37-psi", "l37-severe-cap"]),

# ---------------------------------------------------------------- hospital and ventilator pneumonia
V(HAP, IO_B,
  "A 64-year-old man has been intubated in the intensive care unit for 4 days after a stroke. He develops a new fever, purulent endotracheal secretions and a new infiltrate, and his blood pressure is falling. Which is the most appropriate next step?",
  [["Cultures, then empiric antibiotics",
    "Correct. A new infiltrate with fever and purulent secretions more than 48 hours after intubation is ventilator-associated pneumonia. Respiratory specimens are collected, then appropriate empiric antibiotics start without delay, because he is becoming unstable; therapy is later narrowed to the culture results."],
   ["Hold antibiotics until cultures return",
    "Cultures come first, but waiting for their results is wrong in an unstable patient: empiric antibiotics start right after the specimens are collected, without delaying care. Tell: his falling blood pressure makes him unstable, and necessary empiric therapy is not delayed for a result.", "wrong stage or severity"],
   ["Ceftriaxone plus azithromycin",
    "Ceftriaxone plus azithromycin is a community-acquired pneumonia regimen. Pneumonia that develops more than 48 hours after intubation is ventilator-associated, treated by the local antibiogram, commonly with an antipseudomonal beta-lactam after cultures. Tell: the 4 days on the ventilator make this a hospital pathway.", "competing diagnosis"],
   ["Chest computed tomography first",
    "Follow-up computed tomography is for a questionable diagnosis, a nonhomogeneous pattern, lower lobes hidden by atelectasis, severe inflammation or a cavitary lesion; it does not come before treating an unstable patient. Tell: the next step here is respiratory cultures, then empiric antibiotics.", "wrong stage or severity"]],
  CS(25, 37, 42, 49), "initial test", "next step", ["l37-hap-cultures", "l37-hap-timing"]),

V(HAP, IO_B,
  "A 67-year-old woman with ventilator-associated pneumonia was started on cefepime plus vancomycin because methicillin-resistant Staphylococcus aureus is common in her unit. On day 3 her respiratory culture grows Pseudomonas susceptible to cefepime, and no Staphylococcus aureus grows. She is improving. What is the most appropriate change?",
  [["Stop vancomycin, continue cefepime",
    "Correct. Her culture shows cefepime-susceptible Pseudomonas and no Staphylococcus aureus, and she is improving, so therapy is de-escalated to the culture and susceptibility results: the vancomycin added for methicillin-resistant Staphylococcus aureus is stopped and cefepime continues, usually for 7 days in total."],
   ["Continue both drugs for 14 days",
    "Keeping both drugs ignores the culture, which grew no Staphylococcus aureus, and 14 days is longer than the usual 7-day course with an adequate response. Tell: once cultures clarify the cause, therapy is narrowed promptly, not continued unchanged.", "wrong stage or severity"],
   ["Add a second antipseudomonal class",
    "Two antipseudomonal classes are for selected patients with resistance risk or high mortality risk at the start of therapy. Tell: her organism is susceptible to cefepime and she is improving, so the move is to narrow, not to broaden.", "wrong stage or severity"],
   ["Switch to moxifloxacin",
    "Moxifloxacin does not provide reliable Pseudomonas coverage, so it would not treat the organism that grew. Tell: narrow within an active antipseudomonal agent, here the cefepime her isolate is susceptible to.", "confused mechanism or drug class"]],
  CS(40, 42, 46), "agent/regimen", "treatment", ["l37-deescalate", "l37-hap-cultures"]),

V(HAP, IO_B,
  "A 71-year-old woman admitted 5 days ago for a hip fracture develops fever, purulent sputum and a new infiltrate. She is not intubated and has no risk for methicillin-resistant Staphylococcus aureus, no resistance risk and no high mortality risk. The hospital antibiogram shows most local Pseudomonas isolates are resistant to piperacillin-tazobactam but susceptible to cefepime. Which empiric agent is most appropriate?",
  [["Cefepime",
    "Correct. Pneumonia that begins 48 hours or more after admission is hospital-acquired. With no major resistance or high mortality risk, one antipseudomonal agent with methicillin-susceptible Staphylococcus aureus coverage is chosen using the local antibiogram, and hers favors cefepime over piperacillin-tazobactam."],
   ["Piperacillin-tazobactam",
    "Piperacillin-tazobactam is one of the usual single agents for hospital-acquired pneumonia without major risks, but the choice between it and cefepime is made with the local antibiogram. Tell: her hospital's Pseudomonas isolates are mostly resistant to it and susceptible to cefepime.", "ruled out by a stated finding"],
   ["Ceftriaxone plus azithromycin",
    "Ceftriaxone plus azithromycin is a regimen for nonsevere community-acquired pneumonia. Her pneumonia began on hospital day 5, which makes it hospital-acquired, treated with an antipseudomonal agent chosen by the antibiogram. Tell: onset 48 hours or more after admission moves her off the community pathway.", "competing diagnosis"],
   ["Cefepime plus vancomycin",
    "Vancomycin or linezolid is added only when methicillin-resistant Staphylococcus aureus risk or local prevalence supports it, and she has no such risk. Tell: without that risk, one antipseudomonal agent with methicillin-susceptible Staphylococcus aureus coverage is enough.", "ruled out by a stated finding"]],
  CS(25, 42, 44, 46), "first-line", "treatment", ["l37-antibiogram", "l37-hap-timing"]),

# ---------------------------------------------------------------- aspiration: anaerobes only for abscess or empyema
V(ASP, IO_B,
  "A 78-year-old man with dysphagia after a stroke is admitted to a general ward with nonsevere aspiration pneumonia and started on ceftriaxone plus azithromycin. He has never had methicillin-resistant Staphylococcus aureus or Pseudomonas isolated. On day 2, imaging newly shows a pleural empyema. Which change to his antibiotics is appropriate?",
  [["Add anaerobic coverage",
    "Correct. Aspiration pneumonia is treated with the community or hospital regimen for its setting and severity, and anaerobic coverage is added only when abscess or empyema is suspected, not routinely. The new empyema is that trigger; drainage is also considered when indicated."],
   ["Add vancomycin",
    "Vancomycin is the methicillin-resistant Staphylococcus aureus agent, given only when that coverage is indicated, and he has never had the organism isolated. Tell: an empyema after aspiration calls for anaerobic coverage, not resistant-organism coverage.", "ruled out by a stated finding"],
   ["No change to the regimen",
    "Leaving the regimen unchanged would be right for uncomplicated aspiration pneumonia, but an empyema changes it. Tell: anaerobic coverage is reserved for abscess or empyema, and he now has one.", "wrong stage or severity"],
   ["Stop antibiotics; this is pneumonitis",
    "Aspiration pneumonitis is a sterile chemical injury managed with support and no prophylactic antibiotics. He has an infectious syndrome with an infiltrate and now an empyema, which is established infection that needs antibiotics. Tell: chemical injury needs support; infection needs antibiotics.", "competing diagnosis"]],
  CS(38, 40, 50, 51, 126), "escalation", "treatment", ["l37-anaerobes"]),

V(ASP, IO_B,
  "An 80-year-old woman with dysphagia after a stroke lives at home. She has 3 days of fever, a productive cough and a new right lower lobe infiltrate, and imaging shows no abscess or empyema. She is admitted to a general ward with nonsevere pneumonia. She has never had methicillin-resistant Staphylococcus aureus or Pseudomonas isolated and has had no recent intravenous antibiotics. Which treatment is most appropriate?",
  [["Ceftriaxone plus azithromycin",
    "Correct. Fever, productive cough and an infiltrate in a patient at risk of aspiration is aspiration pneumonia, an infection treated with the regimen for its setting and severity: here nonsevere pneumonia from home on a ward, a beta-lactam plus a macrolide. With no abscess or empyema, anaerobic coverage is not added."],
   ["Weeks of ampicillin-sulbactam",
    "Weeks of a beta-lactam/beta-lactamase inhibitor is the lung abscess plan, and anaerobic coverage is added only when abscess or empyema is suspected. Tell: her imaging shows neither, so she takes the ordinary nonsevere ward regimen.", "competing diagnosis"],
   ["Supportive care, no antibiotic",
    "Support without antibiotics is the plan for chemical aspiration pneumonitis, a sterile injury after a witnessed aspiration. She has 3 days of an infectious syndrome with a compatible infiltrate, which is aspiration pneumonia and needs antibiotics. Tell: established infection needs antibiotics.", "competing diagnosis"],
   ["Cefepime plus vancomycin",
    "Methicillin-resistant Staphylococcus aureus or Pseudomonas coverage is added only for validated risks, such as prior respiratory isolation or recent hospitalization with intravenous antibiotics, and she has none. Tell: without those risks, nonsevere ward pneumonia takes a beta-lactam plus a macrolide.", "ruled out by a stated finding"]],
  CS(25, 44, 50, 51, 56), "first-line", "treatment", ["l37-anaerobes", "l37-pneumonitis"]),

# ---------------------------------------------------------------- Pneumocystis: what a positive polymerase chain reaction means
V(PJP, IO_B,
  "A 62-year-old woman who takes long-term prednisone has bronchoscopy to evaluate a lung nodule. A Pneumocystis polymerase chain reaction test on the lavage fluid is positive at a low level. She has no dyspnea, fever or cough, her oxygen saturation is normal on room air, and her imaging shows no infiltrates. How should this result be interpreted?",
  [["It may reflect colonization, not infection",
    "Correct. The Pneumocystis polymerase chain reaction is highly sensitive but can detect colonization, so it is interpreted with the symptoms, the imaging and the organism burden. A low-level positive in a woman with no symptoms, a normal oxygen saturation and no infiltrates does not establish pneumonia."],
   ["It confirms Pneumocystis pneumonia",
    "A positive polymerase chain reaction alone does not confirm pneumonia, because the test can detect colonization. Tell: she has none of the usual symptoms (progressive exertional dyspnea, fever, nonproductive cough), so the result is weighed against the clinical findings.", "common lay belief"],
   ["It must be repeated on expectorated sputum",
    "Spontaneously expectorated sputum has poor sensitivity and is not a useful specimen for Pneumocystis. Tell: induced sputum or lavage is the right sample, and she already has a lavage result; the question is what it means, not where to resample.", "adjacent fact"],
   ["It calls for adjunctive corticosteroids",
    "Adjunctive corticosteroids are for Pneumocystis pneumonia with a room-air arterial oxygen below 70 mm Hg, a threshold set in human immunodeficiency virus infection. Tell: she has a normal oxygen saturation and no pneumonia, so there is nothing for a steroid to treat.", "adjacent fact"]],
  CS(62, 65, 67, 72), "test finding", "test", ["l37-pcr-limits"]),

# ---------------------------------------------------------------- histoplasmosis by severity
V(FUN, IO_B,
  "A 44-year-old man with untreated human immunodeficiency virus infection cleaned out a barn full of bird droppings 3 weeks ago. He is admitted to the intensive care unit with high fever, hypoxemia, hypotension and diffuse infiltrates, and his urine Histoplasma antigen is positive. Which treatment is most appropriate?",
  [["Amphotericin-based induction",
    "Correct. Histoplasmosis treatment follows severity and host risk. An intensive care admission with hypoxemia, hypotension and diffuse infiltrates in an immunocompromised host is severe disease, and severe pulmonary or disseminated histoplasmosis requires specialist-led amphotericin-based induction."],
   ["Observation without an antifungal",
    "Observation is for mild acute disease in an immunocompetent adult. Tell: he is immunocompromised and critically ill, the opposite end of the severity range, so he needs amphotericin-based induction.", "wrong stage or severity"],
   ["Oral itraconazole as an outpatient",
    "Itraconazole is considered for prolonged or progressive illness or higher-risk hosts who are not severely ill. Tell: an intensive care admission with hypoxemia and hypotension is severe disease, which starts with amphotericin-based induction under a specialist.", "wrong stage or severity"],
   ["Fluconazole for 6 to 12 months",
    "Fluconazole for 6 to 12 months treats mild, isolated pulmonary cryptococcosis. Tell: his exposure to bird droppings and positive urine Histoplasma antigen point to histoplasmosis, and his severity calls for amphotericin-based induction.", "competing diagnosis"]],
  CS(75, 77, 78, 123), "escalation", "treatment", ["l37-histo-severity"]),

V(FUN, IO_B,
  "A 52-year-old woman with no immune problems developed fever, chills, a nonproductive cough and chest pain after clearing soil under a bird roost, and her urine Histoplasma antigen is positive. Five weeks later she is no better: her cough and fatigue are worsening, but she is not hypoxemic and is managing at home. Which treatment is most appropriate?",
  [["Oral itraconazole",
    "Correct. Histoplasmosis is treated by severity and host risk. Her illness is prolonged and progressive but not severe, so itraconazole is considered, with monitoring of interactions and drug levels; observation fits mild acute disease in an immunocompetent adult, and amphotericin is for severe disease."],
   ["Continued observation",
    "Observation is the usual plan for mild acute disease in an immunocompetent adult. Tell: her illness is prolonged and worsening rather than mild, which is the case for considering itraconazole.", "wrong stage or severity"],
   ["Amphotericin-based induction",
    "Amphotericin-based induction is for severe pulmonary or disseminated disease. Tell: she is not hypoxemic and is managing at home, so her disease is prolonged and progressive but not severe, and an oral azole is considered first.", "wrong stage or severity"],
   ["Fluconazole for 6 to 12 months",
    "Fluconazole for 6 to 12 months treats mild, isolated pulmonary cryptococcosis, a different fungal infection. Tell: her bird-roost soil exposure and positive urine Histoplasma antigen make this histoplasmosis, for which the azole named is itraconazole.", "competing diagnosis"]],
  CS(76, 77, 78, 123), "escalation", "treatment", ["l37-histo-severity"]),

# ---------------------------------------------------------------- vaccines: sequencing and eligibility
V(VAX, IO_VAX,
  "A 58-year-old woman with no chronic conditions received the 15-valent pneumococcal conjugate vaccine 14 months ago at a pharmacy and has had no pneumococcal vaccine since. Which plan completes her pneumococcal vaccination?",
  [["A 23-valent polysaccharide dose now",
    "Correct. Every adult aged 50 or older is eligible, and a series started with the 15-valent conjugate vaccine usually needs the 23-valent polysaccharide vaccine afterward, usually 1 year or more later. Fourteen months have passed, so she gets it now."],
   ["Nothing; her series is complete",
    "One dose completes the series only when it is the 20- or 21-valent conjugate vaccine. Tell: she had the 15-valent conjugate vaccine, which usually needs the 23-valent polysaccharide vaccine afterward.", "adjacent fact"],
   ["A second 15-valent conjugate dose",
    "The 15-valent conjugate vaccine is not repeated; the second product in this series is the 23-valent polysaccharide vaccine. Tell: the sequence is 15-valent conjugate, then polysaccharide usually 1 year or more later.", "common lay belief"],
   ["A 23-valent dose when she turns 65",
    "Pneumococcal vaccination is recommended for all adults aged 50 or older, so there is no reason to wait for 65. Tell: she is 58 and more than a year past her conjugate dose, so the polysaccharide vaccine is due now.", "reversed direction or value"]],
  CS(8, 9, 124), "agent/regimen", "next step", ["l37-pneumo-seq"]),

V(VAX, IO_VAX,
  "A 66-year-old man with no condition that increases his risk of severe respiratory syncytial virus disease asks whether he should get the respiratory syncytial virus vaccine this fall. Which counseling statement is accurate?",
  [["Not yet; one dose is due at 75",
    "Correct. One respiratory syncytial virus vaccine dose is recommended for all adults 75 or older and for adults 50 to 74 who are at increased risk of severe disease. At 66 with no such risk he is not yet eligible; when he turns 75, one dose is recommended, not a yearly one."],
   ["Yes, one dose now",
    "One dose now fits an adult aged 50 to 74 only when he is at increased risk of severe respiratory syncytial virus disease. Tell: he has no risk condition, so at 66 he waits until 75.", "ruled out by a stated finding"],
   ["Yes, one dose every year",
    "Repeat annual dosing is not currently recommended for the respiratory syncytial virus vaccine; it is not an annual adult vaccine. Tell: yearly vaccination is the influenza rule, and he is not yet eligible anyway.", "adjacent fact"],
   ["Yes, two doses 4 weeks apart",
    "Two doses at least 4 weeks apart is the influenza schedule some children aged 6 months to 8 years may need. Tell: the respiratory syncytial virus vaccine is a single adult dose, given at 75, or from 50 with increased risk.", "adjacent fact"]],
  CS(7, 124), "education", "education", ["l37-rsv"]),

# ---------------------------------------------------------------- psittacosis
V(ATY, IO_B,
  "A 47-year-old man who races pigeons has 6 days of fever, severe headache and a dry cough, with a lower-lobe infiltrate. A respiratory nucleic acid test detects Chlamydia psittaci. He has no drug allergies. Which treatment is preferred?",
  [["Doxycycline",
    "Correct. Bird exposure, severe headache, a dry cough and a lower-lobe infiltrate with Chlamydia psittaci on a respiratory nucleic acid test is psittacosis. Doxycycline is preferred in adults, started promptly and continued about 10 to 14 days after the fever resolves to prevent relapse."],
   ["Azithromycin",
    "A macrolide is the alternative only when tetracyclines are unsuitable, discussed with infectious disease, and macrolide treatment failures have occurred. Tell: he has no allergy, so the preferred adult drug, doxycycline, is used.", "wrong stage or severity"],
   ["Amoxicillin",
    "Amoxicillin is the outpatient choice for community-acquired pneumonia without comorbidities, aimed at the usual pneumonia pathogens such as pneumococcus. Tell: a bird keeper with Chlamydia psittaci on testing has psittacosis, for which doxycycline is preferred.", "confused mechanism or drug class"],
   ["Trimethoprim-sulfamethoxazole",
    "Trimethoprim-sulfamethoxazole is the preferred treatment for Pneumocystis pneumonia, an opportunistic infection of immunocompromised hosts. Tell: bird exposure and Chlamydia psittaci point to psittacosis, treated with doxycycline.", "competing diagnosis"]],
  CS(43, 71, 81, 85, 88), "first-line", "treatment", ["l37-psittacosis"]),

# ---------------------------------------------------------------- influenza: a negative rapid test in a high-risk patient past 48 hours
V(FLU, IO_B,
  "A 70-year-old woman with chronic obstructive pulmonary disease has had fever, myalgias and cough for 4 days during a week of high influenza activity. She is not hypoxemic and will be treated at home. A rapid influenza antigen test is negative. Which is the most appropriate plan?",
  [["Start oseltamivir now",
    "Correct. Age 65 or older and chronic pulmonary disease make her high-risk, and risk status supports prompt antiviral treatment even after 48 hours. A negative rapid antigen test does not exclude influenza during high activity, and indicated antivirals are not withheld while awaiting confirmation."],
   ["No antiviral; influenza is excluded",
    "Rapid antigen tests have limited sensitivity, so a negative result does not exclude influenza, especially during high community activity. Tell: her picture and the season keep influenza likely, and as a high-risk patient she is treated.", "common lay belief"],
   ["No antiviral after 48 hours",
    "The 48-hour window limits single-dose baloxavir for uncomplicated influenza, not oseltamivir for a high-risk patient. Tell: for high-risk patients, treatment starts promptly even when symptoms began more than 48 hours ago.", "wrong stage or severity"],
   ["Await a molecular test result first",
    "Molecular testing can confirm when the result affects management, but indicated antivirals are not withheld while awaiting confirmation, and treatment does not wait for a test in high-risk patients. Tell: she is high-risk, so treat now and test alongside if needed.", "wrong stage or severity"]],
  CS(95, 97, 105, 108), "first-line", "treatment", ["l37-rapid-flu", "l37-flu-48h"]),
]
