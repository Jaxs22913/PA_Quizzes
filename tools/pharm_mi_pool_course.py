# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 -- Myocardial Ischemia Drugs (Lecture 8): the items KEYED AS THE COURSE TEACHES THEM.

WHY THIS FILE EXISTS. Dr. Wood taught three things that are older than, or simpler than, current labeling and
guidelines. The Lecture 8 build (0a8c3801) deliberately did not key them (truth wins on conflict). Jaxon
then decided (2026-09-30): "key the contested items as 'the course says'". So for THESE THREE GROUPS ONLY
the key follows what was taught, the explanation says plainly where current practice differs, and every other
question on the site stays truth-wins:

  (a) the slide 34 comorbidity table: prior myocardial infarction -> AVOID calcium channel blockers, and
      diabetes -> a NON-DIHYDROPYRIDINE calcium channel blocker first line (alternatives long-acting nitrate
      and cardioselective beta blocker; avoid non-cardioselective beta blockers);
  (b) nitroglycerin tablets are REPLACED about every 3 to 6 months after opening (slide 28, said aloud at
      37:49 in the recording and again as "yes, do replace it");
  (c) beta blockers in acute coronary syndrome are given INTRAVENOUSLY FIRST, THEN ORALLY, and are taught to
      reduce early and late mortality (slides 52 and 55; recording 55:17).

HOW THEY ARE USED. This module is NOT split by pharm_mi_partition.py and does not disturb its seeded
selection. pharm_mi_course_extend.py appends these questions to the sets that pharm_mi_partition.py and
pharm_mi_vignette_partition.py already wrote, so every question already shipped keeps its place and its key.

  QUESTIONS      topic-quiz style (appended to the anginal sets and the acs sets by the `set` field)
  VIGNETTES      patient style, appended to the two myocardial ischemia vignette sets

WORDING RULES THAT APPLY HERE. The stems never cite a lecture, slide, professor or course; where the keyed
answer is the older teaching the stem says "traditional", which is honest framing rather than a citation.
Each key's explanation says what current labeling or guidelines add. No doses. Keys are written short on
purpose, with the detail in the explanation. The correct answer is authored FIRST and rotated by the extender.
"""
D = "Myocardial Ischemia Drugs.pptx"
IO_IND = "Identify indications for drugs used to treat myocardial ischemia"
IO_CONTRA = "Identify contraindications for drugs used to treat myocardial ischemia"
IO_EDU = "Outline appropriate patient education for drugs used to treat myocardial ischemia"
IO_PROT = "List commonly used protocols and patient monitoring for myocardial ischemia drug therapy"

# `set` names the group the question joins: "anginal" or "acs" (topic quizzes).
QUESTIONS = [

# ---- (a) comorbidity table: prior myocardial infarction, diabetes --------------------------------
{"set": "anginal", "topic": "Comorbid conditions", "io": IO_CONTRA, "slot": "contraindication",
 "q": "In the traditional comorbidity-based approach to angina therapy, which drug class is best avoided after a myocardial infarction?",
 "opts": [
  ["Calcium channel blockers", "Correct. The traditional comorbidity table lists calcium channel blockers as the class to avoid after an infarction, because a beta blocker is preferred on the mortality evidence. Current practice is less absolute: a non-dihydropyridine may substitute when a beta blocker cannot be used and ventricular function is normal."],
  ["Beta blockers", "Beta blockers are the first-line antianginal after an infarction and are the class preferred in this setting, so they are not the ones to avoid."],
  ["Long-acting nitrates", "Long-acting nitrates are not listed as a class to avoid after an infarction; they serve as adjuncts, and calcium channel blockers are the class traditionally avoided."],
  ["Angiotensin-converting enzyme inhibitors", "These are continued indefinitely after an infarction to slow disease progression, so they are not avoided; calcium channel blockers are the class traditionally avoided."]],
 "c": 0, "cite": D + ", Slide 34"},

{"set": "anginal", "topic": "Comorbid conditions", "io": IO_IND, "slot": "drug choice",
 "q": "In the traditional comorbidity-based approach, which class is first line for angina in a patient with diabetes who has no other reason to need a beta blocker?",
 "opts": [
  ["Non-dihydropyridine calcium channel blockers", "Correct. The traditional comorbidity table gives a non-dihydropyridine calcium channel blocker as first line in diabetes, with a long-acting nitrate or a cardioselective beta blocker as alternatives. Current practice is more flexible: a cardioselective beta blocker remains a sound first choice."],
  ["Beta blockers", "The traditional table makes a beta blocker an alternative in diabetes, and only a cardioselective one, because the class can raise blood sugar and mask hypoglycemia. Current practice still accepts it as a first choice."],
  ["Dihydropyridine calcium channel blockers", "A dihydropyridine is first line with bradycardia or atrioventricular block, not with diabetes; in diabetes the traditional first line is a non-dihydropyridine."],
  ["Long-acting nitrates", "Long-acting nitrates are the listed alternative in diabetes, not the first-line choice, and they are adjuncts rather than monotherapy."]],
 "c": 0, "cite": D + ", Slide 34"},

{"set": "anginal", "topic": "Comorbid conditions", "io": IO_CONTRA, "slot": "contraindication",
 "q": "In the traditional comorbidity-based approach, which drug type is avoided for angina in a patient with diabetes?",
 "opts": [
  ["Non-cardioselective beta blockers", "Correct. Non-cardioselective beta blockers are the type avoided in diabetes, because beta blockers can raise blood sugar and mask the warning signs of hypoglycemia; a cardioselective one is the listed alternative. Current practice is less absolute: beta blockers are not contraindicated in diabetes, but a cardioselective one is preferred and the patient is taught about masked hypoglycemia."],
  ["Cardioselective beta blockers", "A cardioselective beta blocker is a listed alternative in diabetes; it is the non-cardioselective type that is avoided."],
  ["Long-acting nitrates", "A long-acting nitrate is a listed alternative in diabetes, so it is not the type to avoid; the type avoided is the non-cardioselective beta blocker."],
  ["Non-dihydropyridine calcium channel blockers", "A non-dihydropyridine is the first-line class in diabetes under the traditional table, so it is not the one avoided; non-cardioselective beta blockers are."]],
 "c": 0, "cite": D + ", Slide 34"},

# ---- (b) nitroglycerin tablet replacement -----------------------------------------------------------
{"set": "anginal", "topic": "Nitrate education", "io": IO_EDU, "slot": "education",
 "q": "Traditionally, when should a patient replace sublingual nitroglycerin tablets after opening the bottle?",
 "opts": [
  ["Every 3 to 6 months", "Correct. The traditional counseling is to replace opened tablets every 3 to 6 months, so that a fresh supply is on hand in an emergency. Current labeling instead ties expiry to the printed date when the tablets stay in the tightly closed original glass bottle."],
  ["Every 1 to 2 weeks", "That is far more often than the traditional advice; opened tablets are replaced about every 3 to 6 months, not every week or two."],
  ["Every 12 to 18 months", "That is too long for the traditional advice, which replaces opened tablets every 3 to 6 months because nitroglycerin degrades."],
  ["Only when the bottle is empty", "Waiting for the bottle to empty risks a degraded tablet in an emergency; the traditional advice is to replace opened tablets every 3 to 6 months."]],
 "c": 0, "cite": D + ", Slide 28"},

{"set": "anginal", "topic": "Nitrate education", "io": IO_EDU, "slot": "education",
 "q": "Why, in the traditional advice, are opened nitroglycerin tablets replaced on a schedule?",
 "opts": [
  ["Light and moisture degrade the drug", "Correct. Nitroglycerin is unstable, and exposure to light or moisture breaks it down so it may not work when needed; that is the reason for the traditional 3 to 6 month replacement and for keeping the tablets in the original container."],
  ["Aged tablets become toxic", "Aged tablets are not toxic; they lose potency, which is why they are replaced and why the original container, cool and dry, protects them."],
  ["Repeated use causes tolerance", "Tolerance develops with continuous exposure to long-acting nitrates and is handled with a nitrate-free interval; replacing tablets addresses degradation instead."],
  ["The tablets harden and cannot dissolve", "Hardening is not the concern; nitroglycerin degrades chemically with light and moisture, which is why opened tablets are replaced."]],
 "c": 0, "cite": D + ", Slide 28"},

# ---- (c) beta blockers in acute coronary syndrome -------------------------------------------------
{"set": "acs", "topic": "Beta blockers in ACS", "io": IO_PROT, "slot": "protocol",
 "q": "In the traditional approach to acute coronary syndrome, how is a beta blocker given?",
 "opts": [
  ["Intravenously first, then orally", "Correct. The traditional sequence is an intravenous beta blocker followed by an oral one. Current guidelines favor oral therapy within the first day and avoid the intravenous route when there is heart failure, low output or a risk of shock."],
  ["Orally only, after discharge", "Waiting until discharge is not the traditional teaching; the beta blocker is started early, intravenously and then switched to oral."],
  ["Orally first, then intravenously", "The sequence is the reverse here; the traditional approach starts with an intravenous dose and then moves to oral therapy."],
  ["Sublingually, then by patch", "Sublingual and patch forms describe nitrates, not beta blockers; the beta blocker goes intravenous first, then oral."]],
 "c": 0, "cite": D + ", Slide 55"},

{"set": "acs", "topic": "Beta blockers in ACS", "io": IO_IND, "slot": "indication",
 "q": "Which outcome benefit is traditionally credited to beta blockers in acute coronary syndrome?",
 "opts": [
  ["Lower early and late mortality", "Correct. Beta blockers are taught to reduce early and late mortality, along with infarct size, heart failure and sudden cardiac death. Current evidence supports the long-term benefit most clearly when ventricular function is reduced, and early intravenous use can raise the risk of shock."],
  ["Chest pain relief with no mortality change", "That describes nitrates, which relieve pain without improving outcomes; beta blockers are credited with lowering mortality."],
  ["Possibly higher mortality in unstable angina", "That is the concern raised about morphine, not beta blockers, which are credited with lower early and late mortality."],
  ["Dissolving the coronary clot", "Clot dissolution is the work of fibrinolytics; beta blockers lower oxygen demand and are credited with lower mortality."]],
 "c": 0, "cite": D + ", Slide 55"},
]

# Patient-style items (the lead-in decides the answer). `lead` is bookkeeping for the distribution report.
VIGNETTES = [

# ---- (a) comorbidity table ----------------------------------------------------------------------
dict(topic="Add-on therapy and variant angina", io=IO_CONTRA, slot="contraindication", lead="avoid",
 q="A 63-year-old man with stable exertional angina had a myocardial infarction three years ago. Heart rate is 70 beats per minute and blood pressure is 128/78 mmHg. He has no asthma and no conduction disease. In the traditional comorbidity-based approach, which class is best avoided?",
 opts=[["Calcium channel blockers",
        "Correct. The traditional comorbidity table says to avoid calcium channel blockers after an infarction and to prefer a beta blocker. Current practice is less absolute and allows a non-dihydropyridine when a beta blocker cannot be used and ventricular function is normal."],
       ["Beta blockers",
        "A beta blocker is first line after an infarction and is the class preferred here, so it is not the one to avoid."],
       ["Long-acting nitrates",
        "These are adjuncts that can be added when symptoms persist; they are not the class avoided after an infarction."],
       ["Angiotensin-converting enzyme inhibitors",
        "These are continued indefinitely after an infarction to slow disease progression, so they are not avoided here."]],
 c=0, cite=D + ", Slide 34"),

dict(topic="Add-on therapy and variant angina", io=IO_IND, slot="drug choice", lead="drug choice",
 q="A 59-year-old woman with type 2 diabetes mellitus has exertional angina. She has no history of myocardial infarction, heart failure or hypertension, and no asthma. Heart rate is 76 beats per minute and blood pressure is 124/76 mmHg. In the traditional comorbidity-based approach, which class is first line?",
 opts=[["A non-dihydropyridine calcium channel blocker",
        "Correct. With diabetes and no other reason for a beta blocker, the traditional table gives a non-dihydropyridine as first line; a long-acting nitrate or a cardioselective beta blocker is the alternative. Current practice is more flexible and still accepts a cardioselective beta blocker first."],
       ["A non-cardioselective beta blocker",
        "This is the type the traditional table avoids in diabetes, because beta blockers can raise blood sugar and mask hypoglycemia."],
       ["A dihydropyridine calcium channel blocker",
        "A dihydropyridine is first line with bradycardia or atrioventricular block, which she does not have; in diabetes the traditional first line is a non-dihydropyridine."],
       ["A short-acting nitrate",
        "Short-acting nitroglycerin is for relief of an attack and is not a daily preventive; the traditional first line for prevention in diabetes is a non-dihydropyridine."]],
 c=0, cite=D + ", Slide 34"),

# ---- (b) nitroglycerin tablet replacement --------------------------------------------------------
dict(topic="Nitrates", io=IO_EDU, slot="education", lead="education",
 q="A 70-year-old man with stable angina opened his bottle of sublingual nitroglycerin tablets eight months ago. He keeps it in the original container in a bedroom drawer and has used it twice. In the traditional counseling, what should he be told about the tablets?",
 opts=[["Replace them with a fresh supply",
        "Correct. The traditional counseling is to replace opened tablets about every 3 to 6 months so that a potent tablet is ready in an emergency. Current labeling ties expiry to the printed date when the tablets stay in the tightly closed original glass bottle."],
       ["Keep using them until the bottle is empty",
        "Nitroglycerin is unstable, and waiting for the bottle to empty risks a degraded tablet in an emergency; the traditional advice is to replace opened tablets every 3 to 6 months."],
       ["Move them to a weekly pill organizer",
        "The tablets belong in the original packaging in a cool, dry place, because light and moisture degrade them; a pill organizer is the wrong storage."],
       ["Refrigerate them to extend their life",
        "Refrigeration is not the instruction; the tablets are kept cool and dry in the original packaging and replaced about every 3 to 6 months."]],
 c=0, cite=D + ", Slide 28"),

# ---- (c) beta blockers in acute coronary syndrome ----------------------------------------------------
dict(topic="Acute coronary syndrome", io=IO_IND, slot="drug choice", lead="drug choice",
 q="A 61-year-old man with ST-elevation myocardial infarction has received chewed aspirin and sublingual nitroglycerin. Heart rate is 88 beats per minute, blood pressure is 134/82 mmHg, the lungs are clear, and there is no heart block or asthma. In the traditional approach, which added class is given to lower early mortality?",
 opts=[["A beta blocker",
        "Correct. A beta blocker is traditionally added, intravenous first and then oral, and is credited with lower early and late mortality when heart rate and pressure allow. Current guidelines favor oral therapy in the first day."],
       ["A non-dihydropyridine calcium channel blocker",
        "Calcium channel blockers are not credited with a mortality benefit after an infarction, and the traditional table lists them as a class to avoid after one."],
       ["An opioid analgesic",
        "Morphine treats pain that nitrates do not relieve and is not credited with improving outcomes, so it is not the class that lowers mortality."],
       ["A long-acting nitrate",
        "Nitrates relieve chest pain with no mortality benefit, so adding another does not lower early mortality."]],
 c=0, cite=D + ", Slide 55"),

dict(topic="Acute coronary syndrome", io=IO_PROT, slot="protocol", lead="next step",
 q="A 57-year-old woman with an acute coronary syndrome received intravenous metoprolol in the emergency department. Heart rate is now 64 beats per minute, blood pressure is 126/74 mmHg, and she has no heart block or wheezing. In the traditional sequence, what is the next step in her beta blocker therapy?",
 opts=[["Switch to an oral beta blocker",
        "Correct. The traditional sequence is an intravenous beta blocker followed by an oral one once she is stable. Current guidelines favor starting oral therapy within the first day."],
       ["Stop the beta blocker now",
        "The intravenous dose is the start of therapy, not the whole of it; the traditional sequence continues with an oral beta blocker."],
       ["Add a non-dihydropyridine calcium channel blocker",
        "A beta blocker with a non-dihydropyridine risks excess bradycardia and block, and calcium channel blockers are not the next step; the sequence continues with an oral beta blocker."],
       ["Repeat intravenous doses for several days",
        "The traditional sequence is intravenous followed by oral, not prolonged intravenous dosing; she moves to an oral beta blocker once stable."]],
 c=0, cite=D + ", Slide 55"),
]
