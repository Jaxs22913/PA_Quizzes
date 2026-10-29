# -*- coding: utf-8 -*-
"""CMS I Exam 5 EXAM-STYLE II, pool A -- Lectures 29-32 (Arrhythmias I and II, Pericardial Disease,
Infective Endocarditis). Writer B's pool_b covers Lectures 26-28.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

WHY (Jaxon, 2026-10-29, after the real Exam 5): the paper had (1) vignettes of patients with SEVERAL
comorbidities where similar drugs or diagnoses had to be told apart by CONTRAINDICATION, and the student
had to pick what to use instead, and (2) guideline-score questions: a vignette, then "what is the score?".
This pool is written in those two shapes for two new 70-question forms.

Every item: tools/question_writing/WRITER.md (stem, options, key) and EXPLAIN_DEEP.md (explanations:
the key says why it fits THIS patient and names the clues; each distractor says why it fails here, the
replacing fact, and how to tell it apart; score keys show the arithmetic item by item). Slides only;
the contested-slide rules in cms_e5l29..32_scope.py hold (no HAS-BLED withholding threshold, no
"anticoagulation for all", no atropine in Lecture 30 items, no Lecture 30 QT drug list, no doses).

Fields per item (beyond the usual Q fields): slot, lead (the cms_e5_partition vocabulary), lec
(l29..l32) and kind: "comorbid" (multi-comorbidity / contraindication / what-instead), "score"
(compute a guideline score or count criteria) or "classify" (place the case in a slide-defined
category). Options are [text, explanation] for the key (authored FIRST) and [text, explanation, mis]
for each distractor.

FLAG FOR JAXON: the CHA2DS2-VASc and HAS-BLED point tables are on Arrhythmias I slide 51, which the
lecturer told the class not to memorize (the Lecture 29 scope excludes that slide). The score items that
use them are here because the real exam asked score-from-vignette questions; drop them if he prefers.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
import cms_e5l29_scope as S29
import cms_e5l30_scope as S30
import cms_e5l31_scope as S31
import cms_e5l32_scope as S32

DECKS = {"l29": S29.DECK, "l30": S30.DECK, "l31": S31.DECK, "l32": S32.DECK}


def cite(lec, *ns):
    d = DECKS[lec]
    if len(ns) == 1:
        return "%s, Slide %d" % (d, ns[0])
    return "%s, Slides %s" % (d, ", ".join(str(n) for n in ns))


def X(lec, kind, topic, io, q, opts, slides, slot, lead):
    d = Q(topic, io, q, opts, cite(lec, *slides))
    d.update(slot=slot, lead=lead, lec=lec, kind=kind)
    return d


QUESTIONS = []

# =====================================================================================================
# LECTURE 29 -- Arrhythmias I (supraventricular)
# =====================================================================================================
L = "l29"
A, POP = S29.IO_A, S29.IO_POP
SBR, STA, SSS, SVT = "Sinus bradycardia", "Sinus tachycardia", "Sick sinus syndrome", "Supraventricular tachycardia"
MAT, PAC, AFL, AFI = "Multifocal atrial tachycardia", "Atrial premature beats", "Atrial flutter", "Atrial fibrillation"
FAT, WPW, JR = "Atrial tachycardia", "Wolff-Parkinson-White", "Junctional rhythm"

QUESTIONS += [

X(L, "comorbid", SBR, POP,
  "A 76-year-old woman with paroxysmal atrial fibrillation, hypertension and heart failure takes metoprolol, "
  "diltiazem and digoxin. She has had a week of fatigue but is alert and afebrile, with a blood pressure of "
  "118/70 mm Hg and a normal neurologic examination. Her electrocardiogram shows a regular rhythm at 46 beats "
  "per minute with a normal P wave before every narrow QRS. Thyroid-stimulating hormone is 2.1 mIU/L (normal "
  "0.4-4.0). Which is the most likely cause of her slow rhythm?",
  [["Her rate-slowing medications",
    "Correct. A regular rate of 46 with a normal P wave before every narrow QRS is sinus bradycardia, and beta blockers (metoprolol), nondihydropyridine calcium channel blockers (diltiazem) and digoxin are each a listed cause; she takes all three. Her normal thyroid result, normal neurologic examination and absent fever remove the thyroid, intracranial pressure and infection causes."],
   ["Hypothyroidism",
    "Hypothyroidism is a listed cause of sinus bradycardia, but her thyroid-stimulating hormone of 2.1 sits inside "
    "the normal range, so it is not the cause here. Her three rate-slowing drugs explain the slow sinus rate; a "
    "thyroid cause would show an abnormal thyroid result.", "ruled out by a stated finding"],
   ["Raised intracranial pressure",
    "Increased intracranial pressure can slow the sinus node, but she is alert with a normal neurologic examination, "
    "so nothing points to it. The cause that fits her is the drug list: a beta blocker, a nondihydropyridine calcium "
    "channel blocker and digoxin together.", "ruled out by a stated finding"],
   ["Late-stage infection",
    "Late-stage infection is on the list of sinus bradycardia causes, but she is afebrile and her only complaint is "
    "fatigue. Her three rate-slowing medications are the documented cause; an infectious cause would come with "
    "fever and a source.", "ruled out by a stated finding"]],
  (13,), "etiology", "diagnosis"),

X(L, "comorbid", SBR, POP,
  "A 69-year-old man with type 2 diabetes and chronic kidney disease is brought in confused and pale. His blood "
  "pressure is 74/40 mm Hg. The monitor shows a regular rhythm at 34 beats per minute with a normal P wave before "
  "every narrow QRS. Which is the first-line treatment?",
  [["Intravenous atropine",
    "Correct. This is sinus bradycardia (normal P before each narrow QRS, rate under 60) that is acute, symptomatic "
    "and hemodynamically unstable: he is confused with a pressure of 74/40. For that situation atropine is first "
    "line, then a temporary pacemaker, with a permanent pacemaker kept for chronic symptomatic disease."],
   ["Temporary pacemaker first",
    "A temporary pacemaker is the SECOND step for unstable symptomatic sinus bradycardia, used when atropine does not "
    "work. With confusion and a pressure of 74/40, he gets atropine first, then temporary pacing if needed.",
    "wrong stage or severity"],
   ["Permanent pacemaker now",
    "A permanent pacemaker is for chronic, symptomatic bradycardia, not the first move in an acute unstable "
    "presentation like his. The acute sequence is atropine first, then a temporary pacemaker.",
    "wrong stage or severity"],
   ["Observation on the monitor",
    "No treatment is needed only when sinus bradycardia is asymptomatic. He is confused and hypotensive, which makes "
    "it acute, symptomatic and unstable, so atropine is given first rather than watching.",
    "ruled out by a stated finding"]],
  (13,), "first-line", "treatment"),

X(L, "comorbid", SSS, POP,
  "A 74-year-old man with ischemic heart disease and sick sinus syndrome has spells of near-fainting. Ambulatory "
  "monitoring shows tachy-brady syndrome (fast rhythms alternating with slow rhythms and pauses), and the fast "
  "episodes are runs of ventricular tachycardia that match his symptoms. Which device does he need?",
  [["Pacemaker with a defibrillator",
    "Correct. Tachy-brady syndrome often needs a permanent pacemaker for the slow phase, and when the fast rhythm is "
    "ventricular tachycardia he needs a permanent pacemaker WITH an automatic implantable cardioverter defibrillator. "
    "His symptoms match the episodes, so this is not an observe-only case."],
   ["A pacemaker by itself",
    "A permanent pacemaker alone treats the slow, symptomatic phase of tachy-brady syndrome. His fast episodes are ventricular tachycardia, so the pacemaker must also carry a defibrillator.", "wrong stage or severity"],
   ["Observation without a device",
    "Observation fits sick sinus syndrome only when symptoms do NOT correlate with the slow episodes. His near-fainting "
    "matches the recorded runs, so he needs a device: a pacemaker with a defibrillator because the fast rhythm is "
    "ventricular tachycardia.", "ruled out by a stated finding"],
   ["Ablation of the fast rhythm",
    "Catheter ablation is the curative step for reentrant rhythms such as atrioventricular nodal reentry, not part of the listed sick sinus syndrome management. Tachy-brady with ventricular tachycardia is treated with a pacemaker that includes a defibrillator.", "confused mechanism or drug class"]],
  (18, 22), "agent/regimen", "treatment"),

X(L, "comorbid", MAT, POP,
  "A 71-year-old woman with severe chronic obstructive pulmonary disease and heart failure is admitted in respiratory "
  "failure from an exacerbation. The monitor shows an irregular rhythm at 128 beats per minute with at least three "
  "different P-wave shapes in the same lead and one P wave for every narrow QRS. She is alert, with a blood "
  "pressure of 132/78 mm Hg. Which is the priority in managing this rhythm?",
  [["Treat the underlying illness",
    "Correct. At least three P-wave shapes in one lead with an irregular rhythm is multifocal atrial tachycardia, "
    "which usually comes from severe chronic obstructive pulmonary disease or heart failure when the patient is "
    "acutely ill. Its management is treating the underlying condition; she is stable, so no shock is needed."],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is the step for an UNSTABLE tachycardia; she is alert with a pressure of 132/78. "
    "Multifocal atrial tachycardia is driven by her acute lung and heart illness, so treating that illness is the "
    "priority.", "ruled out by a stated finding"],
   ["Catheter ablation of foci",
    "Catheter ablation is usually curative for FOCAL atrial tachycardia, which has a single, consistent abnormal "
    "P-wave shape. Her three or more P-wave shapes mark the multifocal form, which is managed by treating the "
    "underlying condition.", "competing diagnosis"],
   ["Adenosine to stop the rhythm",
    "Adenosine terminates tachycardias that depend on the atrioventricular node (nodal and atrioventricular reentry) "
    "and is less effective even for focal atrial tachycardia. Multifocal atrial tachycardia in an acutely ill lung "
    "patient is managed by treating the cause.", "confused mechanism or drug class"]],
  (28, 31, 32), "first-line", "treatment"),

X(L, "comorbid", PAC, A,
  "A 58-year-old man with chronic obstructive pulmonary disease and paroxysmal atrial fibrillation has daily "
  "palpitations. Monitoring shows frequent premature atrial contractions (early, abnormally shaped P waves), and his "
  "atrial fibrillation episodes start right after runs of them. An echocardiogram shows no structural heart disease. "
  "He has cut out caffeine and alcohol, and three months of metoprolol has not helped. Which treatment fits best?",
  [["Catheter ablation",
    "Correct. Premature atrial contractions that persist with symptoms are treated with a beta blocker if not "
    "contraindicated, or with catheter ablation when they are frequent or are triggering atrial fibrillation. His are "
    "frequent, trigger his atrial fibrillation and did not respond to metoprolol, so ablation is the fit."],
   ["Reassurance alone",
    "Reassurance about the benign nature of premature atrial contractions fits patients without symptoms. His are "
    "frequent, symptomatic and set off atrial fibrillation, which is the indication for catheter ablation.",
    "wrong stage or severity"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion treats an unstable tachycardia, not isolated early beats. Frequent premature atrial "
    "contractions that trigger atrial fibrillation are treated with catheter ablation once a beta blocker has failed.",
    "confused mechanism or drug class"],
   ["Look for structural disease",
    "Frequent premature atrial contractions do call for a search for structural heart disease, but his echocardiogram "
    "has already shown none. The next step for persistent, triggering beats after failed metoprolol is catheter "
    "ablation.", "ruled out by a stated finding"]],
  (54, 58), "escalation", "treatment"),

X(L, "comorbid", SVT, POP,
  "A 66-year-old man with coronary artery disease and type 2 diabetes has a regular, narrow-complex tachycardia at "
  "210 beats per minute with no visible P waves. He has chest pain and is confused, with a blood pressure of 76/44 "
  "mm Hg. Which is the next step?",
  [["Synchronized cardioversion",
    "Correct. A regular narrow-complex tachycardia over 160 with hidden P waves is supraventricular tachycardia, and "
    "chest pain, confusion and a pressure of 76/44 make it hemodynamically unstable. Unstable supraventricular "
    "tachycardia gets immediate synchronized cardioversion, a timed shock with decreased voltage."],
   ["Vagal maneuver first",
    "A vagal maneuver is first line for STABLE supraventricular tachycardia. He is confused and hypotensive, so the "
    "rhythm is unstable and needs immediate synchronized cardioversion instead of a trial of vagal maneuvers.",
    "wrong stage or severity"],
   ["Intravenous adenosine",
    "Adenosine (which may be repeated once) follows a vagal maneuver in STABLE supraventricular tachycardia. With a "
    "pressure of 76/44 and confusion he is unstable, which calls for immediate synchronized cardioversion.",
    "wrong stage or severity"],
   ["Unsynchronized shock",
    "An unsynchronized shock is not timed to the QRS. Unstable supraventricular tachycardia with a pulse is treated "
    "with SYNCHRONIZED cardioversion, a timed shock delivered with decreased voltage.",
    "confused mechanism or drug class"]],
  (23, 25, 26), "escalation", "next step"),

X(L, "comorbid", WPW, A,
  "A 34-year-old woman with hypertension controlled on lisinopril has a prior electrocardiogram showing "
  "pre-excitation (a short PR interval with a delta wave, a slurred upstroke of the QRS). She now has palpitations. "
  "She is alert with a blood pressure of 124/76 mm Hg, and the monitor shows a fast, irregularly irregular rhythm "
  "with wide, varying QRS complexes: atrial fibrillation with Wolff-Parkinson-White. Which drug is the right choice?",
  [["Intravenous procainamide",
    "Correct. Her old tracing shows pre-excitation (short PR, delta wave), so this irregular wide rhythm is atrial "
    "fibrillation over an accessory pathway. Atrial fibrillation with Wolff-Parkinson-White is treated with "
    "intravenous procainamide, never adenosine; she is stable, so no shock is needed, and ablation of the pathway "
    "is the later definitive step."],
   ["Intravenous adenosine",
    "Adenosine is first line for ORTHODROMIC atrioventricular reentry, but it is never used for atrial fibrillation "
    "with Wolff-Parkinson-White, which is what her irregular, wide, varying complexes show. The drug here is "
    "intravenous procainamide.", "adjacent fact"],
   ["Intravenous diltiazem",
    "Intravenous rate control fits stable atrial fibrillation with a rapid rate when there is NO accessory pathway. "
    "Her known pre-excitation makes this atrial fibrillation with Wolff-Parkinson-White, which is treated with "
    "intravenous procainamide.", "competing diagnosis"],
   ["Catheter ablation today",
    "Ablation of the accessory pathway is the first-line CHRONIC management of Wolff-Parkinson-White, not the drug "
    "for the acute episode. Right now the irregular pre-excited rhythm is treated with intravenous procainamide.",
    "wrong stage or severity"]],
  (33, 35, 37, 52), "agent/regimen", "treatment"),

X(L, "score", AFI, A,
  "A 70-year-old woman with hypertension and type 2 diabetes is found to have non-valvular atrial fibrillation. She "
  "has no heart failure, stroke, transient ischemic attack, myocardial infarction, peripheral artery disease or "
  "aortic plaque. What is her CHA2DS2-VASc (stroke risk) score?",
  [["Score of 4",
    "Correct. Age 70 falls in the 65-74 band for 1 point, female sex adds 1, hypertension 1 and diabetes 1: "
    "1 + 1 + 1 + 1 = 4. She has no heart failure, no prior stroke or transient ischemic attack (2 points) and no "
    "vascular disease, so nothing else is added. A score this high means she typically needs anticoagulation."],
   ["Score of 2",
    "Two points counts only her hypertension and diabetes. The score also gives 1 point for age 65-74 and 1 point for "
    "female sex, so her total is 4, well above the low-risk line of 1 for a woman.", "adjacent fact"],
   ["Score of 3",
    "Three points drops one item, most often female sex, which adds 1 point. Age 70 (1), female sex (1), hypertension "
    "(1) and diabetes (1) add up to 4.", "adjacent fact"],
   ["Score of 5",
    "Five points scores her age as 2, but 2 points start at age 75. At 70 she is in the 65-74 band for 1 point, which "
    "with sex, hypertension and diabetes gives 4.", "reversed direction or value"]],
  (50, 51), "test finding", "test"),

X(L, "score", AFI, POP,
  "A 78-year-old man with chronic heart failure had a transient ischemic attack last year and now has atrial "
  "fibrillation. He has no hypertension, diabetes, myocardial infarction or peripheral artery disease. What is his "
  "CHA2DS2-VASc (stroke risk) score?",
  [["Score of 5",
    "Correct. Age 75 or older scores 2, heart failure 1, and a prior transient ischemic attack 2 (stroke, transient "
    "ischemic attack or thromboembolism count double): 2 + 1 + 2 = 5. Male sex adds nothing, and he has no "
    "hypertension, diabetes or vascular disease."],
   ["Score of 3",
    "Three points scores the transient ischemic attack as 1 and the age as 1. Both are double items here: age 75 or "
    "older is 2 and prior stroke or transient ischemic attack is 2, so with heart failure the total is 5.",
    "reversed direction or value"],
   ["Score of 4",
    "Four points counts one of his double items as a single point. Age 75 or older (2), heart failure (1) and a prior "
    "transient ischemic attack (2) give 5.", "adjacent fact"],
   ["Score of 6",
    "Six points adds a sex point he does not get: female sex scores 1, male sex 0. His total is age 2 + heart failure "
    "1 + transient ischemic attack 2 = 5.", "adjacent fact"]],
  (50, 51), "test finding", "test"),

X(L, "score", AFI, A,
  "A 66-year-old man had a myocardial infarction treated with a stent four years ago and has hypertension. He now has "
  "atrial fibrillation. He has no heart failure, diabetes, stroke or transient ischemic attack. What is his "
  "CHA2DS2-VASc (stroke risk) score?",
  [["Score of 3",
    "Correct. Age 66 is in the 65-74 band for 1 point, the prior myocardial infarction counts as vascular disease for "
    "1, and hypertension adds 1: 1 + 1 + 1 = 3. Male sex scores 0, and he has no heart failure, diabetes or prior "
    "stroke. He is above the low-risk line of 0 for a man."],
   ["Score of 1",
    "One point counts only his hypertension. A prior myocardial infarction is scored as vascular disease (1 point) and "
    "age 65-74 adds 1, so his total is 3.", "adjacent fact"],
   ["Score of 2",
    "Two points misses one item, usually the vascular disease point: a prior myocardial infarction counts there. Age "
    "(1), vascular disease (1) and hypertension (1) make 3.", "adjacent fact"],
   ["Score of 4",
    "Four points scores the myocardial infarction as 2, but among the history items only stroke, transient ischemic attack or thromboembolism count double; vascular disease is 1. His total is 3.", "reversed direction or value"]],
  (50, 51), "test finding", "test"),

X(L, "score", AFI, A,
  "A 63-year-old woman with hypertension is found to have atrial fibrillation. She has no heart failure, diabetes, "
  "stroke, transient ischemic attack or vascular disease. What is her CHA2DS2-VASc (stroke risk) score?",
  [["Score of 2",
    "Correct. Age 63 is under 65 and scores 0, female sex adds 1 and hypertension 1: 0 + 1 + 1 = 2. The age points "
    "start at 65, which is the usual trap in a patient in her early sixties. Two points for a woman is above the "
    "low-risk line of 1."],
   ["Score of 1",
    "One point counts her hypertension but leaves out female sex, which adds 1 point. With age under 65 scoring 0, "
    "sex 1 and hypertension 1, her total is 2.", "adjacent fact"],
   ["Score of 3",
    "Three points gives her an age point she has not reached: age points start at 65, and she is 63. Her total is "
    "female sex 1 + hypertension 1 = 2.", "reversed direction or value"],
   ["Score of 4",
    "Four points scores her age as 2 and adds sex and hypertension. Age under 65 scores 0, so her total is only "
    "female sex 1 + hypertension 1 = 2.", "reversed direction or value"]],
  (50, 51), "test finding", "test"),

X(L, "score", AFI, POP,
  "An 81-year-old woman with type 2 diabetes and peripheral artery disease had an ischemic stroke two years ago. She "
  "now has atrial fibrillation. She has no heart failure or hypertension. What is her CHA2DS2-VASc (stroke risk) "
  "score?",
  [["Score of 7",
    "Correct. Age 75 or older scores 2, female sex 1, diabetes 1, peripheral artery disease (vascular disease) 1 and "
    "prior stroke 2: 2 + 1 + 1 + 1 + 2 = 7. She has no heart failure or hypertension to add. A score this high means "
    "she typically needs anticoagulation unless her bleeding risk is high."],
   ["Score of 5",
    "Five points scores both double items (age 75 or older and prior stroke) as single points. Each is worth 2, so "
    "with sex, diabetes and peripheral artery disease her total is 7.", "reversed direction or value"],
   ["Score of 6",
    "Six points misses one single-point item, usually peripheral artery disease, which counts as vascular disease. "
    "Age 2 + sex 1 + diabetes 1 + vascular disease 1 + stroke 2 = 7.", "adjacent fact"],
   ["Score of 8",
    "Eight points adds a hypertension or heart failure point she does not have. Her items are age 2, female sex 1, "
    "diabetes 1, vascular disease 1 and prior stroke 2, for 7.", "adjacent fact"]],
  (50, 51), "test finding", "test"),

X(L, "score", AFI, A,
  "A 61-year-old woman has new atrial fibrillation found at a routine visit. She has no hypertension, diabetes, heart "
  "failure, stroke, transient ischemic attack or vascular disease, so her CHA2DS2-VASc (stroke risk) score is 1, "
  "from female sex. Her rate is controlled. What does this score mean for her?",
  [["Low stroke risk; may not need anticoagulation",
    "Correct. The score estimates stroke risk, and 0 for a man or 1 for a woman is low risk: such a patient may not "
    "require anticoagulation. Her single point comes only from female sex, so she sits on that low-risk line."],
   ["Raised stroke risk; needs anticoagulation",
    "One point would place a MAN above the low-risk line, but for a woman the low-risk line is 1, because female sex "
    "alone adds a point. She is low risk and may not require anticoagulation.", "reversed direction or value"],
   ["Low bleeding risk; anticoagulation is safe",
    "This score measures STROKE risk, not bleeding risk; bleeding risk is estimated with the HAS-BLED (bleeding risk) "
    "score. Her stroke-risk score of 1 as a woman is low, so she may not need anticoagulation at all.",
    "confused mechanism or drug class"],
   ["Rate control is no longer needed",
    "Rate control is the first goal in atrial fibrillation whatever the stroke-risk score; the score decides "
    "anticoagulation, not rate control. Her score of 1 as a woman is low risk for stroke.", "adjacent fact"]],
  (49, 50), "prognosis", "test"),

X(L, "score", AFI, POP,
  "A 72-year-old man with atrial fibrillation is on hemodialysis for end-stage kidney disease, takes daily aspirin "
  "for a coronary stent and had a major gastrointestinal bleed last year. His blood pressure is 148/84 mm Hg. He has "
  "no liver disease, prior stroke or unstable international normalized ratio, and he drinks no alcohol. What is his "
  "HAS-BLED (bleeding risk) score?",
  [["Score of 4",
    "Correct. Age over 65 scores 1, renal disease on dialysis 1, prior major bleeding 1 and aspirin (medication "
    "predisposing to bleeding) 1: 1 + 1 + 1 + 1 = 4. His systolic pressure of 148 does not reach the uncontrolled "
    "line of above 160, so hypertension adds nothing. This score estimates his risk of major bleeding."],
   ["Score of 2",
    "Two points counts only the dialysis and the prior bleed. Age over 65 and daily aspirin each add 1 point as "
    "well, so his total is 4.", "adjacent fact"],
   ["Score of 3",
    "Three points leaves out one of his four items, usually the aspirin, which counts as a medication predisposing to "
    "bleeding. Age, renal disease, prior bleeding and aspirin add up to 4.", "adjacent fact"],
   ["Score of 5",
    "Five points adds a hypertension point, but that item needs uncontrolled pressure above 160 systolic; his is 148. "
    "Without it, age 1 + renal 1 + bleeding 1 + aspirin 1 = 4.", "ruled out by a stated finding"]],
  (50, 51), "test finding", "test"),

X(L, "score", AFI, POP,
  "A 67-year-old woman with atrial fibrillation takes clopidogrel after a coronary stent. Her blood pressure is "
  "150/86 mm Hg, creatinine 1.0 mg/dL (normal 0.6-1.2), liver tests are normal, she has had no stroke or bleeding, "
  "she is not on warfarin and she drinks two glasses of wine a week. What is her HAS-BLED (bleeding risk) score?",
  [["Score of 2",
    "Correct. Age over 65 scores 1 and clopidogrel (a medication predisposing to bleeding) scores 1: 1 + 1 = 2. Her "
    "pressure of 150 is below the uncontrolled line of above 160, her kidneys and liver are normal, and two drinks "
    "a week is far under the 8 or more drinks a week that would score."],
   ["Score of 1",
    "One point counts her age but not the clopidogrel. Antiplatelet drugs such as clopidogrel and aspirin, and "
    "nonsteroidal anti-inflammatory drugs, each count as a medication predisposing to bleeding, so her total is 2.",
    "adjacent fact"],
   ["Score of 3",
    "Three points scores her blood pressure, but the hypertension item needs uncontrolled pressure above 160 systolic; "
    "hers is 150. Age 1 + clopidogrel 1 = 2.", "ruled out by a stated finding"],
   ["Score of 4",
    "Four points also scores her pressure and her wine, but neither reaches its line: hypertension needs a systolic "
    "above 160 and alcohol needs 8 or more drinks a week. Her total is 2.", "ruled out by a stated finding"]],
  (50, 51), "test finding", "test"),

X(L, "classify", AFI, A,
  "A 64-year-old man with obesity and obstructive sleep apnea has had continuous atrial fibrillation for 5 weeks. It "
  "has not stopped on its own, and he and his clinician still plan to restore sinus rhythm. Which category describes "
  "his atrial fibrillation?",
  [["Persistent",
    "Correct. Atrial fibrillation that is continuous for more than 7 days but less than 1 year is persistent and needs "
    "treatment. Five weeks of continuous rhythm fits that window, and since rhythm control is still planned it has "
    "not been declared permanent."],
   ["Paroxysmal",
    "Paroxysmal atrial fibrillation lasts less than 1 week and usually stops without treatment. His has run "
    "continuously for 5 weeks, which makes it persistent.", "reversed direction or value"],
   ["Long-standing persistent",
    "Long-standing persistent atrial fibrillation has been continuous for more than 1 year. At 5 weeks he is in the "
    "persistent window of more than 7 days but less than 1 year.", "reversed direction or value"],
   ["Permanent",
    "Permanent atrial fibrillation is a joint decision by patient and clinician to stop trying to restore or keep "
    "sinus rhythm. They still plan to restore it, so his 5-week episode is persistent.",
    "ruled out by a stated finding"]],
  (46, 48), "manifestation", "diagnosis"),

X(L, "classify", AFI, POP,
  "A 79-year-old woman with hypertension has had continuous atrial fibrillation for 2 years. Two cardioversions "
  "failed, and she and her cardiologist have agreed to stop trying to restore sinus rhythm and to focus on rate "
  "control. Which category describes her atrial fibrillation now?",
  [["Permanent",
    "Correct. Atrial fibrillation becomes permanent when the patient and clinician make a joint decision to stop "
    "further attempts to restore or maintain sinus rhythm. That decision, not the 2-year duration alone, is what "
    "places her in this category."],
   ["Long-standing persistent",
    "Long-standing persistent describes atrial fibrillation continuous for more than 1 year while rhythm control is "
    "still being pursued. She and her cardiologist have stopped trying to restore sinus rhythm, which makes it "
    "permanent.", "adjacent fact"],
   ["Persistent",
    "Persistent atrial fibrillation is continuous for more than 7 days but less than 1 year. Hers has lasted 2 years "
    "and rhythm control has been abandoned by joint decision, so it is permanent.", "reversed direction or value"],
   ["Paroxysmal",
    "Paroxysmal atrial fibrillation lasts under 1 week and usually ends on its own. Hers has been continuous for 2 "
    "years with failed cardioversions, and the joint decision to stop rhythm control makes it permanent.",
    "reversed direction or value"]],
  (46,), "manifestation", "diagnosis"),

X(L, "comorbid", AFI, POP,
  "A 67-year-old woman with hypertension and obesity has had stable atrial fibrillation for 3 months. Her rate is "
  "controlled on metoprolol and she is not anticoagulated. She asks to have an outpatient cardioversion to get back "
  "into sinus rhythm. Which must come first?",
  [["21 days of anticoagulation",
    "Correct. Outpatient cardioversion of atrial fibrillation is done only after 21 days of anticoagulation. She is "
    "stable and rate controlled, so there is no reason for an urgent shock, and she has had no anticoagulation yet."],
   ["Immediate cardioversion",
    "Immediate synchronized cardioversion is for hemodynamically UNSTABLE atrial fibrillation. She is stable and rate "
    "controlled, so an elective outpatient cardioversion waits until she has had 21 days of anticoagulation.",
    "wrong stage or severity"],
   ["Catheter ablation",
    "Mapping and ablation are part of longer-term atrial fibrillation management, not a required step before "
    "cardioversion. What must come before an outpatient cardioversion is 21 days of anticoagulation.",
    "adjacent fact"],
   ["Stopping her metoprolol",
    "Rate control is the first goal in atrial fibrillation, and stopping it before cardioversion has no basis. The "
    "step that must precede an outpatient cardioversion is 21 days of anticoagulation.", "common lay belief"]],
  (49,), "escalation", "next step"),

X(L, "comorbid", AFI, POP,
  "An 80-year-old man with heart failure and type 2 diabetes has atrial fibrillation at 150 beats per minute. He has "
  "crackles to both lung apices from pulmonary edema, and his blood pressure is 78/46 mm Hg. Which is the next step?",
  [["Synchronized cardioversion",
    "Correct. Atrial fibrillation with severe heart failure (pulmonary edema) and hypotension is a medical emergency "
    "and hemodynamically unstable. Unstable atrial fibrillation gets synchronized cardioversion, not a trial of "
    "rate-control drugs."],
   ["Intravenous rate control",
    "Intravenous rate control fits atrial fibrillation with a rapid rate that is hemodynamically STABLE. His pulmonary "
    "edema and pressure of 78/46 make him unstable, which calls for synchronized cardioversion.",
    "wrong stage or severity"],
   ["Oral rate control",
    "Oral rate control fits stable atrial fibrillation WITHOUT a rapid rate. He has a rate of 150, pulmonary edema and "
    "hypotension, which make this an emergency treated with synchronized cardioversion.", "wrong stage or severity"],
   ["Cardioversion after 21 days",
    "Waiting 21 days on anticoagulation applies to an ELECTIVE outpatient cardioversion in a stable patient. His "
    "pulmonary edema and hypotension make him unstable, so synchronized cardioversion is done now.",
    "wrong stage or severity"]],
  (48, 49), "escalation", "next step"),

X(L, "comorbid", AFI, POP,
  "A 72-year-old man with non-valvular atrial fibrillation, hypertension and type 2 diabetes has a stroke-risk score "
  "that calls for anticoagulation and a low bleeding-risk score. Which anticoagulant choice is preferred?",
  [["A direct oral anticoagulant",
    "Correct. With a stroke-risk score that calls for anticoagulation and a low bleeding risk he should be "
    "anticoagulated, and in non-valvular atrial fibrillation the direct oral anticoagulants (dabigatran, apixaban, "
    "edoxaban or rivaroxaban) are preferred. Warfarin, if used, targets an international normalized ratio of 2 to 3."],
   ["Warfarin, ratio goal 3 to 4",
    "Warfarin is an option, but its target international normalized ratio in atrial fibrillation is 2 to 3, not 3 to "
    "4, and in NON-valvular atrial fibrillation the direct oral anticoagulants such as apixaban are preferred.",
    "reversed direction or value"],
   ["Aspirin as the sole agent",
    "Aspirin is not one of the anticoagulants for atrial fibrillation; the choices are the direct oral anticoagulants "
    "(dabigatran, apixaban, edoxaban, rivaroxaban) or warfarin. With his risk score and low bleeding risk, a direct "
    "oral anticoagulant is preferred.", "common lay belief"],
   ["No anticoagulant needed",
    "With his low bleeding risk, no anticoagulation is reasonable only at low stroke risk: 0 for a man or 1 for a woman. His hypertension, diabetes and age put him above that line, so he needs one, preferably a direct oral anticoagulant.",
    "ruled out by a stated finding"]],
  (50,), "agent/regimen", "treatment"),

X(L, "comorbid", JR, S29.IO_L30,
  "A 79-year-old woman with paroxysmal atrial fibrillation and worsening chronic kidney disease takes digoxin. She has "
  "nausea and fatigue. Her electrocardiogram shows a regular rhythm at 48 beats per minute with narrow QRS complexes "
  "and retrograde P waves (inverted, after the QRS). Her digoxin level is 3.4 ng/mL (therapeutic 0.5-2.0). Which "
  "treatment fits?",
  [["Digoxin immune Fab",
    "Correct. A regular narrow rhythm at 48 with inverted P waves after the QRS is a junctional rhythm, and digoxin "
    "toxicity is a listed cause; her level of 3.4 is above the therapeutic range. Junctional rhythm from digitalis "
    "toxicity is treated with atropine and/or digoxin immune Fab (Digibind)."],
   ["Permanent pacemaker",
    "A permanent pacemaker treats a junctional rhythm caused by complete or high-grade atrioventricular block or sick "
    "sinus syndrome. Hers comes from digoxin toxicity (level 3.4), which is reversed with digoxin immune Fab.",
    "competing diagnosis"],
   ["No treatment needed",
    "No treatment fits a junctional rhythm only in an asymptomatic, otherwise healthy patient such as a "
    "well-conditioned athlete. She is symptomatic with a toxic digoxin level, so she needs digoxin immune Fab.",
    "ruled out by a stated finding"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion treats unstable tachycardias, not a slow junctional rhythm. Her rhythm is driven by "
    "digoxin toxicity, and the treatment is digoxin immune Fab.", "confused mechanism or drug class"]],
  (62, 64), "agent/regimen", "treatment"),

X(L, "comorbid", JR, S29.IO_L30,
  "A 22-year-old competitive rower with well-controlled seasonal allergies has a preparticipation electrocardiogram "
  "showing a regular rhythm at 46 beats per minute with narrow QRS complexes and inverted P waves buried in or just "
  "after the QRS. He has no symptoms, takes no medications and his examination is normal. Which is the next step?",
  [["Reassure; no treatment",
    "Correct. This is a junctional rhythm (rate 40-60, narrow QRS, inverted P waves around the QRS). It can be seen in "
    "healthy patients with increased vagal tone such as well-conditioned athletes, is generally well tolerated, and "
    "needs no treatment when the patient is asymptomatic and otherwise healthy."],
   ["Permanent pacemaker",
    "A pacemaker is for a junctional rhythm caused by complete or high-grade atrioventricular block or sick sinus "
    "syndrome. His comes from an athlete's increased vagal tone without symptoms, so no treatment is needed.",
    "wrong stage or severity"],
   ["Digoxin immune Fab",
    "Digoxin immune Fab treats a junctional rhythm caused by digoxin toxicity. He takes no medications; his rhythm "
    "reflects the increased vagal tone of a well-conditioned athlete and needs no treatment.",
    "ruled out by a stated finding"],
   ["Daily metoprolol",
    "A beta blocker is used for frequent or persistently symptomatic premature JUNCTIONAL contractions, and it would "
    "slow his rate further. An asymptomatic athlete's junctional rhythm needs reassurance, not a drug.",
    "adjacent fact"]],
  (62, 64), "first-line", "next step"),

X(L, "comorbid", STA, A,
  "A 27-year-old woman who works rotating night shifts has a resting heart rate of 118 beats per minute with a "
  "normal P wave before every narrow QRS. Hemoglobin is 13.6 g/dL (normal 12-16), thyroid-stimulating hormone 1.8 "
  "mIU/L (normal 0.4-4.0), oxygen saturation 99%, and a drug screen is negative. She is mildly bothered by palpitations. "
  "Which is the first step in management?",
  [["Remove influencing factors",
    "Correct. With anemia, thyroid disease, hypoxia and drugs excluded, this is inappropriate sinus tachycardia, a "
    "diagnosis of exclusion. Management starts by eliminating influencing factors, including lifestyle changes such as "
    "night shifts, medications and illicit drugs, plus behavioral therapy; it is generally left untreated."],
   ["Long-term beta blocker",
    "Beta blockers are poorly tolerated in inappropriate sinus tachycardia, and patients usually tolerate the symptoms "
    "better than the treatment. The first step is removing influencing factors such as her night shifts.",
    "wrong stage or severity"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion treats unstable supraventricular tachycardia. Hers is sinus tachycardia (normal P "
    "before each QRS) in a stable patient, managed first by eliminating influencing factors.",
    "competing diagnosis"],
   ["Treat for hyperthyroidism",
    "Hyperthyroidism is a pathologic cause of sinus tachycardia, but her thyroid-stimulating hormone of 1.8 is normal. "
    "With secondary causes excluded, the first step is addressing triggers such as night shifts.",
    "ruled out by a stated finding"]],
  (16, 17), "first-line", "treatment"),

X(L, "comorbid", STA, A,
  "A 62-year-old man with hypertension and stable angina ran out of his metoprolol 2 days ago. He feels his heart "
  "racing. His heart rate is 124 beats per minute with a normal P wave before every narrow QRS. He is afebrile, "
  "hemoglobin is 14.8 g/dL (normal 13.5-17.5), thyroid-stimulating hormone 2.0 mIU/L (normal 0.4-4.0) and oxygen "
  "saturation 98%. Which is the most likely cause of his tachycardia?",
  [["Metoprolol withdrawal",
    "Correct. A normal P before every narrow QRS at 124 is sinus tachycardia, and abrupt withdrawal of medications "
    "such as beta blockers or nondihydropyridine calcium channel blockers is a listed cause. He stopped metoprolol "
    "2 days ago, and his normal hemoglobin, thyroid test and oxygen saturation exclude anemia, hyperthyroidism and "
    "hypoxia."],
   ["Hyperthyroidism",
    "Hyperthyroidism is a pathologic cause of sinus tachycardia, but his thyroid-stimulating hormone of 2.0 is normal. "
    "The trigger here is stopping metoprolol 2 days ago, which causes sinus tachycardia on abrupt withdrawal.",
    "ruled out by a stated finding"],
   ["Underlying anemia",
    "Anemia can drive sinus tachycardia, but his hemoglobin of 14.8 is normal. Abrupt withdrawal of his beta blocker "
    "2 days ago is the cause that fits.", "ruled out by a stated finding"],
   ["Underlying hypoxia",
    "Hypoxia is a pathologic cause of sinus tachycardia, but his oxygen saturation is 98%. The sudden stop of his "
    "metoprolol is what explains the fast sinus rate.", "ruled out by a stated finding"]],
  (16,), "etiology", "diagnosis"),

X(L, "comorbid", AFL, A,
  "A 70-year-old man who had mitral valve surgery 6 months ago and has right-sided heart failure has palpitations. "
  "His electrocardiogram shows flutter waves (a sawtooth pattern) with 2:1 block and a ventricular rate of 150. He is "
  "alert with a blood pressure of 128/80 mm Hg. This is his third episode despite rate control. Which offers "
  "definitive management?",
  [["Catheter ablation",
    "Correct. Sawtooth flutter waves with 2:1 block are atrial flutter, common after atrial scarring from surgery and "
    "in right-sided heart failure. He is stable, rate control is harder in flutter and recurrence is substantial, as "
    "his third episode shows; ablation is the definitive management, with anticoagulation alongside."],
   ["Rate control by itself",
    "A beta blocker or calcium channel blocker is the stable-patient step, but rate control is harder to achieve in "
    "flutter and recurrence is substantial; this is already his third episode. Ablation is the definitive management.",
    "wrong stage or severity"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is for HEMODYNAMICALLY UNSTABLE atrial flutter. He is alert with a pressure of "
    "128/80, and the question is definitive management of recurrent flutter, which is ablation.",
    "wrong stage or severity"],
   ["Pacemaker with defibrillator",
    "A pacemaker with a defibrillator is for tachy-brady syndrome whose fast rhythm is ventricular tachycardia. His "
    "problem is recurrent atrial flutter, which is treated definitively with ablation.", "competing diagnosis"]],
  (42, 44, 45), "escalation", "treatment"),

X(L, "comorbid", FAT, A,
  "A 35-year-old woman whose hyperthyroidism is now controlled has recurrent episodes of abrupt palpitations. During "
  "one, the rhythm is regular at 170 beats per minute with one consistently abnormal P wave before every narrow QRS. "
  "Adenosine slowed it only briefly without ending it. She stays stable, and the episodes keep returning. Which is "
  "the initial chronic therapy?",
  [["Oral beta blocker",
    "Correct. A regular tachycardia with one consistent abnormal P wave before each QRS that adenosine does not end is "
    "focal atrial tachycardia; adenosine is a useful diagnostic tool because it is less effective here than in "
    "nodal or atrioventricular reentry. Initial chronic therapy is an oral beta blocker or nondihydropyridine calcium "
    "channel blocker, with ablation usually curative."],
   ["Intravenous procainamide",
    "Intravenous procainamide is the drug for atrial fibrillation with Wolff-Parkinson-White, an irregular rhythm with "
    "wide pre-excited complexes. Her regular narrow rhythm with one abnormal P-wave shape is focal atrial tachycardia, "
    "started on an oral beta blocker.", "competing diagnosis"],
   ["Permanent pacemaker",
    "A permanent pacemaker treats symptomatic bradycardia, not a recurrent tachycardia. Focal atrial tachycardia is "
    "managed long term with an oral beta blocker or nondihydropyridine calcium channel blocker, or ablation.",
    "confused mechanism or drug class"],
   ["Repeat adenosine daily",
    "Adenosine is an intravenous diagnostic tool and is less effective for terminating focal atrial tachycardia, as it "
    "was for her. Chronic control starts with an oral beta blocker or nondihydropyridine calcium channel blocker.",
    "confused mechanism or drug class"]],
  (28, 30, 31), "agent/regimen", "treatment"),
]

# =====================================================================================================
# LECTURE 30 -- Arrhythmias II (blocks and ventriculars). Never "atropine", never the QT drug list.
# =====================================================================================================
L = "l30"
A, POP = S30.IO_A, S30.IO_POP
TDP, VTA, AVB, PVC = "Torsades de Pointes", "Ventricular tachycardia", "Atrioventricular block", "Ventricular premature beats"
VFI, BBB = "Ventricular fibrillation", "Bundle branch blocks"

QUESTIONS += [

X(L, "comorbid", TDP, A,
  "A 58-year-old woman with depression and chronic diarrhea was recently started on a medication known to prolong the "
  "QT interval. Her corrected QT is 560 ms, potassium 3.0 mEq/L (normal 3.5-5.0) and magnesium 1.4 mg/dL (normal "
  "1.7-2.2). The monitor shows polymorphic ventricular tachycardia whose QRS complexes twist around the baseline "
  "(torsades de pointes). She is awake with a blood pressure of 112/70 mm Hg. Which drug is given first?",
  [["Intravenous magnesium",
    "Correct. Polymorphic ventricular tachycardia twisting around the baseline with a long QT is torsades de pointes, "
    "and most torsades is acquired, from drugs, low potassium or low calcium. In a conscious patient intravenous "
    "magnesium breaks it, followed by more magnesium as an infusion."],
   ["Intravenous amiodarone",
    "Amiodarone prolongs the QT interval, so it is not used in torsades, where her QT of 560 ms is the problem. In a "
    "conscious patient intravenous magnesium is given to break the rhythm.", "confused mechanism or drug class"],
   ["Intravenous procainamide",
    "Procainamide prolongs the QT interval and is avoided in torsades de pointes. Her long QT, low potassium and low "
    "magnesium call for intravenous magnesium first.", "confused mechanism or drug class"],
   ["Intravenous metoprolol",
    "Beta blockers are avoided in torsades because the bradycardia they cause lengthens the interval between beats and "
    "indirectly prolongs the QT. A conscious patient with torsades gets intravenous magnesium.",
    "confused mechanism or drug class"]],
  (40, 42, 47), "first-line", "treatment"),

X(L, "comorbid", TDP, A,
  "A 64-year-old man with heart failure and alcohol use disorder has recurrent runs of polymorphic ventricular "
  "tachycardia whose QRS complexes twist around the baseline (torsades de pointes), with a corrected QT of 540 ms. He "
  "stays conscious with a blood pressure of 104/66 mm Hg and is already on a magnesium infusion. An antiarrhythmic is "
  "to be added. Which one can be used?",
  [["Intravenous lidocaine",
    "Correct. In torsades de pointes amiodarone and procainamide are avoided because they prolong the QT, and beta "
    "blockers are avoided because their bradycardia indirectly prolongs it. Intravenous lidocaine is the antiarrhythmic "
    "that CAN be used, although the evidence for it is limited; magnesium remains the core treatment."],
   ["Intravenous amiodarone",
    "Amiodarone is a choice for STABLE MONOMORPHIC ventricular tachycardia, but it prolongs the QT and is not used in "
    "torsades. With his QT of 540 ms the antiarrhythmic that can be added is lidocaine.", "adjacent fact"],
   ["Intravenous procainamide",
    "Procainamide is listed for stable monomorphic ventricular tachycardia, but it prolongs the QT and is avoided in "
    "torsades; it is also avoided in heart failure, which he has. Lidocaine is the one that can be used.",
    "adjacent fact"],
   ["Carvedilol by mouth",
    "Beta blockers such as carvedilol treat symptomatic non-sustained ventricular tachycardia, but in torsades they "
    "slow the rate and indirectly lengthen the QT. Lidocaine is the antiarrhythmic that can be added.",
    "confused mechanism or drug class"]],
  (43, 44, 47), "agent/regimen", "treatment"),

X(L, "comorbid", VTA, A,
  "A 70-year-old man with ischemic cardiomyopathy and chronic heart failure has a regular wide-complex tachycardia at "
  "170 beats per minute with identical QRS complexes: monomorphic ventricular tachycardia. He is alert with a blood "
  "pressure of 118/74 mm Hg and has no chest pain or shortness of breath. Which should be avoided in his initial "
  "management?",
  [["Intravenous procainamide",
    "Correct. He is stable (no chest pain, altered mental status, shortness of breath or hypotension), so "
    "pharmacologic cardioversion with lidocaine, amiodarone or procainamide is the route, but procainamide is avoided "
    "in a patient with a prolonged QT or congestive heart failure, and he has heart failure."],
   ["Intravenous amiodarone",
    "Amiodarone is one of the three drugs for stable monomorphic ventricular tachycardia and carries no "
    "heart-failure warning in this setting. Procainamide is the one to avoid because of his heart failure.",
    "adjacent fact"],
   ["Intravenous lidocaine",
    "Lidocaine is listed for pharmacologic cardioversion of stable monomorphic ventricular tachycardia and is "
    "reasonable for him. The drug avoided with congestive heart failure is procainamide.", "adjacent fact"],
   ["Supplemental oxygen",
    "Supplemental oxygen is part of the initial management of every patient with sustained ventricular tachycardia, "
    "along with a monitor, intravenous access, a 12-lead electrocardiogram and labs. The drug to avoid is "
    "procainamide.", "adjacent fact"]],
  (44, 45), "avoid", "avoid"),

X(L, "comorbid", VTA, A,
  "A 66-year-old woman with chronic kidney disease has a baseline corrected QT of 520 ms. She develops a regular "
  "wide-complex tachycardia at 160 beats per minute with identical QRS complexes. She is alert with a blood pressure "
  "of 126/78 mm Hg and has no chest pain, confusion or shortness of breath. Which antiarrhythmic avoids adding to her "
  "QT prolongation?",
  [["Intravenous lidocaine",
    "Correct. She has stable monomorphic ventricular tachycardia, treated with lidocaine, amiodarone or procainamide. "
    "Procainamide is avoided with a prolonged QT, and amiodarone and procainamide both prolong the QT; lidocaine is "
    "the antiarrhythmic that CAN be used when the QT is the problem, as it is in torsades."],
   ["Intravenous procainamide",
    "Procainamide treats stable monomorphic ventricular tachycardia, but it is avoided when the QT is prolonged, as "
    "hers is at 520 ms, because it lengthens the QT further. Lidocaine does not.", "ruled out by a stated finding"],
   ["Intravenous amiodarone",
    "Amiodarone is listed for stable monomorphic ventricular tachycardia, but it prolongs the QT, which is why it is "
    "avoided in torsades. With her already long QT, lidocaine is the choice that adds no QT prolongation.",
    "confused mechanism or drug class"],
   ["Intravenous metoprolol",
    "A beta blocker is not one of the listed drugs for converting stable sustained ventricular tachycardia, and the "
    "bradycardia it causes indirectly prolongs the QT. Lidocaine is the antiarrhythmic that avoids it.",
    "confused mechanism or drug class"]],
  (44, 47), "agent/regimen", "treatment"),

X(L, "comorbid", VTA, A,
  "A 67-year-old woman with a prior myocardial infarction and type 2 diabetes has a regular wide-complex tachycardia at "
  "190 beats per minute with identical QRS complexes. She has chest pain and a blood pressure of 82/50 mm Hg, and a "
  "carotid pulse is present. Which is the next step?",
  [["Synchronized cardioversion",
    "Correct. Identical wide complexes at 190 are monomorphic ventricular tachycardia, and chest pain with hypotension "
    "makes it unstable. For unstable monomorphic ventricular tachycardia the next move is to check for a pulse: with a "
    "pulse present, synchronized cardioversion; without one, defibrillation."],
   ["Unsynchronized defibrillation",
    "Defibrillation (unsynchronized cardioversion) is for PULSELESS ventricular tachycardia, and for polymorphic "
    "ventricular tachycardia. She has a carotid pulse and identical complexes, so she gets synchronized cardioversion.",
    "ruled out by a stated finding"],
   ["Intravenous lidocaine",
    "Lidocaine is pharmacologic cardioversion for STABLE monomorphic ventricular tachycardia. Her chest pain and "
    "pressure of 82/50 make her unstable, and with a pulse present she needs synchronized cardioversion.",
    "wrong stage or severity"],
   ["Intravenous magnesium",
    "Magnesium breaks torsades de pointes, a polymorphic ventricular tachycardia with a long QT. Her complexes are "
    "identical (monomorphic) and she is unstable with a pulse, so synchronized cardioversion is next.",
    "competing diagnosis"]],
  (39, 45), "escalation", "next step"),

X(L, "comorbid", VTA, A,
  "A 61-year-old man with diabetes and hyperlipidemia has crushing chest pain. His corrected QT was 420 ms on arrival. "
  "The monitor now shows a fast wide-complex rhythm whose QRS shapes vary from beat to beat: polymorphic ventricular "
  "tachycardia. He is awake with a pulse and a blood pressure of 108/70 mm Hg. Which is the next step?",
  [["Defibrillation",
    "Correct. Polymorphic ventricular tachycardia without a prolonged QT is most commonly due to acute myocardial "
    "ischemia, as with his crushing chest pain. Even if the patient looks well, polymorphic ventricular tachycardia is "
    "never truly stable: defibrillate, then urgent coronary angiography with possible revascularization."],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is for unstable MONOMORPHIC ventricular tachycardia with a pulse. His QRS shapes vary, "
    "and polymorphic ventricular tachycardia is never truly stable, so he is defibrillated even with a pulse.",
    "competing diagnosis"],
   ["Intravenous magnesium",
    "Magnesium treats polymorphic ventricular tachycardia WITH a prolonged QT (torsades). His QT was normal at 420 ms "
    "and he has ischemic chest pain, so he is defibrillated and sent for urgent coronary angiography.",
    "ruled out by a stated finding"],
   ["Intravenous procainamide",
    "Procainamide is a pharmacologic option for STABLE MONOMORPHIC ventricular tachycardia. Polymorphic ventricular "
    "tachycardia is never truly stable and is treated with defibrillation.", "wrong stage or severity"]],
  (42, 46), "first-line", "next step"),

X(L, "comorbid", AVB, POP,
  "A 77-year-old man with type 2 diabetes and long-standing hypertension has a routine electrocardiogram. It shows a "
  "constant PR interval of 0.18 s with occasional P waves that are suddenly not followed by a QRS complex. He has no "
  "dizziness, fatigue or syncope. Which is the definitive management?",
  [["Permanent pacemaker",
    "Correct. A constant PR interval with randomly dropped QRS complexes is second-degree Mobitz type II block, common "
    "with degenerative conduction disease of old age, hypertension and diabetes. It is considered dangerous even "
    "without symptoms because it can progress to complete block and sudden cardiac death; definitive treatment is a "
    "permanent pacemaker."],
   ["Observation; he has no symptoms",
    "Observation suits blocks that are usually benign without symptoms, such as first-degree or Mobitz type I. Mobitz "
    "type II is considered dangerous even in the absence of symptoms, so he needs a permanent pacemaker.",
    "wrong stage or severity"],
   ["Transcutaneous pacing",
    "Transcutaneous pacing is the EMERGENT treatment for an unstable Mobitz type II or complete block. He is stable, "
    "and the question is definitive management, which is a permanent pacemaker.", "wrong stage or severity"],
   ["Repeat tracing in a year",
    "Waiting a year ignores the unpredictable progression of Mobitz type II to complete heart block and sudden cardiac "
    "death. The definitive treatment, even without symptoms, is a permanent pacemaker.", "wrong stage or severity"]],
  (10, 13, 14), "first-line", "treatment"),

X(L, "comorbid", AVB, A,
  "A 45-year-old man who injects drugs is being treated for aortic valve infective endocarditis. On day 6 he becomes "
  "dizzy. His electrocardiogram shows regular P waves at 80 per minute and a separate regular ventricular rhythm at "
  "36, with no relationship between the P waves and the QRS complexes. He takes no rate-slowing drugs and reports no "
  "tick bites. Which is the most likely cause of the block?",
  [["Endocarditis with an abscess",
    "Correct. Two unrelated regular rates with a ventricular rate under 40 is third-degree (complete) block, and "
    "bacterial endocarditis with an associated abscess is a listed cause. In a man on day 6 of treatment for aortic "
    "valve endocarditis, the infection extending into the conduction tissue is the cause that fits."],
   ["Lyme carditis infection",
    "Lyme carditis (a tick-borne infection of the heart) is a listed cause of complete block, but he reports no tick "
    "bites and has active aortic valve endocarditis. Bacterial endocarditis with an abscess explains the new block.",
    "ruled out by a stated finding"],
   ["Age-related degeneration",
    "Degenerative disease of the conduction system is the most common cause of complete block overall, mostly in old "
    "age. He is 45 with active endocarditis, so endocarditis with an associated abscess is the likely cause.",
    "adjacent fact"],
   ["A rate-slowing medication",
    "Rate-slowing drugs such as beta blockers, nondihydropyridine calcium channel blockers and digoxin cause "
    "atrioventricular block, but he takes none. His active aortic valve endocarditis with an abscess is the cause.",
    "ruled out by a stated finding"]],
  (15, 17, 18), "etiology", "diagnosis"),

X(L, "comorbid", AVB, POP,
  "A 74-year-old woman with hypertension and stable angina takes metoprolol and diltiazem. Her electrocardiogram shows "
  "a regular rhythm at 64 beats per minute, one P wave before every narrow QRS and a constant PR interval of 0.26 s. "
  "She has no fatigue, shortness of breath, palpitations or heart failure symptoms. Which is the appropriate "
  "management?",
  [["No treatment needed",
    "Correct. A constant PR interval over 0.20 s with every P wave conducted is first-degree atrioventricular block; "
    "her beta blocker and nondihydropyridine calcium channel blocker, and her age, are listed causes. The vast "
    "majority are asymptomatic, and no treatment is needed unless there are debilitating or heart-failure symptoms."],
   ["Permanent pacemaker",
    "A permanent pacemaker is considered for first-degree block in symptomatic patients or when the PR interval is over 0.3 seconds. Hers is 0.26 seconds and she has no symptoms, so no treatment is needed.", "wrong stage or severity"],
   ["Transcutaneous pacing",
    "Transcutaneous pacing is the emergent treatment for unstable Mobitz type II or complete block. First-degree "
    "block in an asymptomatic patient needs no treatment.", "wrong stage or severity"],
   ["Catheter ablation",
    "Catheter ablation is itself a listed cause of conduction block, not a treatment for it; it is used for "
    "tachycardias such as reentry. Her asymptomatic first-degree block needs no treatment.",
    "confused mechanism or drug class"]],
  (4, 6), "first-line", "treatment"),

X(L, "comorbid", AVB, A,
  "A 32-year-old man with asthma went hiking 3 weeks ago, had a tick bite and then an expanding red rash. He now feels "
  "lightheaded. His electrocardiogram shows Wenckebach block (the PR interval grows longer with each beat until a QRS "
  "is dropped). He takes no medications and has no history of heart disease. Which is the most likely cause?",
  [["Lyme carditis",
    "Correct. A PR interval that lengthens until a QRS drops is second-degree Mobitz type I (Wenckebach) block, and Lyme "
    "disease (Lyme carditis) is a listed cause. A tick bite and expanding rash 3 weeks before, in a young man on no "
    "medications, point to it rather than age-related or ischemic causes."],
   ["Age-related degeneration",
    "Degenerative conduction disease is a cause of block in old age; he is 32. His recent tick bite and expanding rash "
    "make Lyme carditis the cause that fits.", "ruled out by a stated finding"],
   ["A medication effect",
    "Beta blockers, nondihydropyridine calcium channel blockers and digoxin cause Mobitz type I block, but he takes no "
    "medications. The tick bite and rash point to Lyme carditis.", "ruled out by a stated finding"],
   ["Ischemia after infarction",
    "Atrioventricular node ischemia after a myocardial infarction is a listed cause, but he is 32 with no heart "
    "disease or chest pain. A recent tick bite with an expanding rash points to Lyme carditis.",
    "ruled out by a stated finding"]],
  (7, 9), "etiology", "diagnosis"),

X(L, "comorbid", PVC, A,
  "A 68-year-old woman with chronic obstructive pulmonary disease and heart failure on a loop diuretic is admitted with "
  "an exacerbation. The monitor shows frequent premature ventricular contractions (early, wide, bizarre QRS complexes "
  "with no P wave). Oxygen saturation is 86%, potassium 2.9 mEq/L (normal 3.5-5.0) and magnesium 1.3 mg/dL (normal "
  "1.7-2.2). Which is the next step?",
  [["Fix oxygen and electrolytes",
    "Correct. Early, wide, bizarre beats without a P wave are premature ventricular contractions, and the main causes "
    "are hypoxemia and electrolyte imbalance such as low potassium and low magnesium. She has all three, so fixing the "
    "oxygenation and replacing potassium and magnesium comes first."],
   ["Start a beta blocker now",
    "A beta blocker is first line for symptomatic LOW-RISK premature ventricular contractions without a reversible "
    "cause. Hers come with a saturation of 86% and low potassium and magnesium, which are corrected first.",
    "wrong stage or severity"],
   ["Catheter ablation of foci",
    "Catheter ablation is for premature ventricular contraction-induced cardiomyopathy with heart failure, or for "
    "low-risk patients refractory to or intolerant of drugs. Her beats have reversible causes (hypoxemia, low "
    "potassium and magnesium) to correct first.", "wrong stage or severity"],
   ["Implantable defibrillator",
    "An implantable defibrillator prevents sudden death after life-threatening ventricular tachycardia or fibrillation. "
    "Isolated early beats driven by hypoxemia and electrolyte loss are treated by correcting those causes.",
    "wrong stage or severity"]],
  (33, 35, 36), "first-line", "next step"),

X(L, "comorbid", PVC, A,
  "A 55-year-old man with hypertension has worsening exertional dyspnea and leg swelling. A 24-hour monitor shows "
  "premature ventricular contractions making up 22% of his beats (about 24,000 per day), and echocardiography shows a "
  "new cardiomyopathy with no other cause found, attributed to the premature beats. Which treatment fits?",
  [["Catheter ablation",
    "Correct. A burden over 15% (or 15,000 a day) with premature ventricular contraction-induced cardiomyopathy makes "
    "him high risk, and he has heart-failure symptoms. For isolated premature ventricular contraction-induced "
    "cardiomyopathy with heart-failure signs, catheter ablation is the treatment."],
   ["Beta blocker first",
    "A beta blocker is first line for symptomatic LOW-RISK patients, and the first step for high-risk patients "
    "OTHERWISE. His beats have caused an isolated cardiomyopathy with heart-failure symptoms, which goes straight to "
    "catheter ablation.", "wrong stage or severity"],
   ["Reassurance and triggers",
    "Reassurance and removing triggers fit low-risk patients with a burden under 1% (or 1,000 a day), no structural "
    "disease and no symptoms. His 22% burden with cardiomyopathy and heart-failure symptoms calls for catheter "
    "ablation.", "wrong stage or severity"],
   ["Implantable defibrillator",
    "An implantable defibrillator prevents sudden death: secondary prevention after life-threatening ventricular tachycardia or fibrillation, and primary prevention in selected patients. It does not stop premature beats. Premature beats that have caused a cardiomyopathy are treated with catheter ablation.",
    "confused mechanism or drug class"]],
  (36,), "escalation", "treatment"),

X(L, "classify", PVC, A,
  "A 40-year-old woman with generalized anxiety drinks six cups of coffee a day. A 24-hour monitor done for an "
  "insurance physical shows premature ventricular contractions making up 0.5% of beats (about 700 per day). Her "
  "echocardiogram is normal, she has never fainted and she has no symptoms. Which management fits her risk group?",
  [["Reassure; remove triggers",
    "Correct. A burden under 1% (or 1,000 a day), no structural heart disease and no symptoms puts her in the low-risk, "
    "asymptomatic group, managed with reassurance and eliminating triggers. Caffeine is a listed trigger, so cutting "
    "her coffee fits."],
   ["Beta blocker first line",
    "A beta blocker is first line for low-risk patients WITH symptoms. She has none, a burden of 0.5% and a normal "
    "heart, so reassurance and removing triggers such as caffeine are the plan.", "wrong stage or severity"],
   ["Catheter ablation",
    "Ablation is for premature ventricular contraction-induced cardiomyopathy or for symptomatic low-risk patients who "
    "fail or cannot take drugs. Her low burden without symptoms needs reassurance and trigger removal.",
    "wrong stage or severity"],
   ["Implantable defibrillator",
    "An implantable defibrillator prevents sudden death after life-threatening ventricular rhythms. A 0.5% burden of "
    "early beats in a normal heart is low risk and managed with reassurance.", "wrong stage or severity"]],
  (36,), "first-line", "treatment"),

X(L, "comorbid", VTA, A,
  "A 63-year-old man with ischemic heart disease and hypertension has palpitations. A monitor shows runs of three or "
  "more wide, identical beats lasting 6 to 10 seconds that stop on their own, without fainting or low blood pressure. "
  "His heart disease treatment is already optimized. Which is the first drug therapy?",
  [["Metoprolol or carvedilol",
    "Correct. Three or more consecutive premature ventricular beats lasting under 30 seconds is non-sustained "
    "ventricular tachycardia, and symptomatic non-sustained ventricular tachycardia is treated first with a beta blocker "
    "such as metoprolol or carvedilol; ablation or an antiarrhythmic follows if that fails."],
   ["Implantable defibrillator now",
    "Non-sustained ventricular tachycardia in and of itself is not an indication for an implantable defibrillator. His "
    "symptomatic runs are treated first with a beta blocker.", "wrong stage or severity"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is for unstable monomorphic ventricular tachycardia with a pulse. His runs stop on their "
    "own in under 30 seconds without instability, so a beta blocker is the first therapy.", "wrong stage or severity"],
   ["Intravenous magnesium",
    "Magnesium breaks torsades de pointes, a polymorphic rhythm with a long QT. His runs are identical, short and "
    "self-terminating, which is symptomatic non-sustained ventricular tachycardia treated with a beta blocker.",
    "competing diagnosis"]],
  (40, 43), "first-line", "treatment"),

X(L, "comorbid", VFI, POP,
  "A 59-year-old man with a prior myocardial infarction and type 2 diabetes collapsed from ventricular fibrillation "
  "and was resuscitated with defibrillation. He is now stable, and no reversible cause was found. Before discharge, "
  "which is recommended?",
  [["Implantable defibrillator",
    "Correct. Once stabilized after life-threatening ventricular tachycardia or fibrillation, most patients need an "
    "implantable cardioverter defibrillator for secondary prevention of sudden cardiac death. Coronary artery disease, "
    "as in his prior infarction, is the most common predisposing condition for sudden death."],
   ["Permanent pacemaker alone",
    "A permanent pacemaker treats symptomatic bradycardia and high-grade block; it cannot shock a fatal rhythm. After "
    "surviving ventricular fibrillation he needs an implantable defibrillator, which senses fatal rhythms and shocks.",
    "confused mechanism or drug class"],
   ["Beta blocker without a device",
    "A beta blocker treats symptomatic premature beats and non-sustained ventricular tachycardia. A survivor of "
    "ventricular fibrillation needs an implantable defibrillator for secondary prevention of sudden death.",
    "wrong stage or severity"],
   ["Ablation of early beats",
    "Catheter ablation treats premature ventricular contraction-induced cardiomyopathy or refractory symptomatic beats. "
    "After a ventricular fibrillation arrest, secondary prevention is an implantable defibrillator.",
    "wrong stage or severity"]],
  (37, 38, 45), "complication", "next step"),

X(L, "comorbid", VFI, POP,
  "A 70-year-old woman with sepsis and ongoing gastrointestinal bleeding becomes unresponsive. The monitor shows an "
  "organized narrow-complex rhythm at 90 per minute, but no pulse can be felt. Which is the next step?",
  [["Compressions and epinephrine",
    "Correct. An organized rhythm that should produce a pulse but does not is pulseless electrical activity, and its "
    "two leading causes in adults are hypovolemia and hypoxia; bleeding makes hypovolemia likely here. It is "
    "unshockable: start chest compressions immediately, with epinephrine every 3 to 5 minutes."],
   ["Immediate defibrillation",
    "Defibrillation treats ventricular fibrillation and pulseless ventricular tachycardia. Pulseless electrical "
    "activity, an organized rhythm without a pulse, is unshockable and needs chest compressions and epinephrine.",
    "competing diagnosis"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is for unstable tachycardias WITH a pulse. She has no pulse with an organized rhythm, "
    "which is pulseless electrical activity, treated with chest compressions and epinephrine.",
    "wrong stage or severity"],
   ["Transcutaneous pacing",
    "Transcutaneous pacing treats unstable Mobitz type II or complete block in a patient who has a pulse. Pulseless "
    "electrical activity is a cardiac arrest rhythm treated with compressions and epinephrine.",
    "wrong stage or severity"]],
  (52, 55), "first-line", "next step"),

X(L, "comorbid", BBB, A,
  "A 72-year-old man with dilated non-ischemic cardiomyopathy (ejection fraction 25%) and chronic hypertension has "
  "worsening dyspnea on exertion despite medical therapy. His electrocardiogram shows a long-standing left bundle "
  "branch block (QRS 0.16 s, dominant S wave in V1, monophasic R waves in I, V5 and V6). Which treatment targets the "
  "block?",
  [["Biventricular pacemaker",
    "Correct. Left bundle branch block is usually left untreated, except when it is symptomatic with heart failure with "
    "reduced ejection fraction, which calls for a biventricular pacer. His ejection fraction of 25% with exertional "
    "dyspnea fits that exception; dilated cardiomyopathy and hypertension are listed causes of the block."],
   ["No treatment for the block",
    "Leaving the block untreated is right for an ASYMPTOMATIC left bundle branch block. He has symptoms with heart "
    "failure with reduced ejection fraction, the exception that calls for a biventricular pacer.",
    "ruled out by a stated finding"],
   ["Transcutaneous pacing",
    "Transcutaneous pacing is the emergent treatment for unstable Mobitz type II or complete block. His chronic, "
    "symptomatic left bundle branch block with a low ejection fraction calls for a biventricular pacer.",
    "wrong stage or severity"],
   ["Catheter ablation",
    "Catheter ablation treats tachycardias and premature beats, and ablation can itself cause conduction block. "
    "Symptomatic left bundle branch block with heart failure with reduced ejection fraction is treated with a "
    "biventricular pacer.", "confused mechanism or drug class"]],
  (24, 26, 27), "agent/regimen", "treatment"),

X(L, "comorbid", BBB, A,
  "A 50-year-old woman with migraine and hypothyroidism has just flown overseas. She has sudden shortness of breath, "
  "pleuritic chest pain and a swollen, tender left calf. Her electrocardiogram, normal last year, now shows a new "
  "right bundle branch block: QRS 0.14 s with an rsR' pattern in V1 to V3 (bunny ears, a second upward deflection) "
  "and a slurred S wave in I and aVL. Which is the most likely cause of the new block?",
  [["Pulmonary embolism",
    "Correct. A wide QRS with an rsR' (bunny ears) in V1 to V3 is right bundle branch block, and a sudden rise in right "
    "ventricular pressure from pulmonary embolism is a listed cause. Sudden dyspnea and pleuritic pain after a long "
    "flight point to it, and the block was absent a year ago."],
   ["Age-related degeneration",
    "Degenerative change of the conduction system causes right bundle branch block that develops slowly with age. Hers "
    "appeared suddenly with dyspnea and pleuritic pain after a flight, which points to pulmonary embolism.",
    "competing diagnosis"],
   ["Lenègre-Lev disease",
    "Lenègre-Lev disease (degenerative fibrotic conduction disease) is a listed cause of LEFT bundle branch block. Her "
    "new right bundle branch block with sudden dyspnea after a flight fits a pulmonary embolism.",
    "adjacent fact"],
   ["Hypertrophic cardiomyopathy",
    "Hypertrophic cardiomyopathy is a listed cause of right bundle branch block, but it would not appear suddenly with "
    "pleuritic chest pain after a flight. A sudden right ventricular pressure rise from pulmonary embolism fits.",
    "competing diagnosis"]],
  (28, 29, 31), "etiology", "diagnosis"),

X(L, "classify", VTA, A,
  "A 66-year-old man with ischemic cardiomyopathy has a run of regular wide-complex tachycardia at 160 beats per "
  "minute on telemetry. Every QRS complex has the same shape. The run lasts 45 seconds and then stops; he stays alert "
  "with a normal blood pressure throughout. Which describes this rhythm?",
  [["Sustained monomorphic",
    "Correct. Three or more consecutive ventricular beats is ventricular tachycardia; a run lasting 30 seconds or more "
    "is sustained, and identical QRS shapes make it monomorphic. His 45-second run with the same shape every beat is "
    "sustained monomorphic ventricular tachycardia, typical with cardiomyopathy."],
   ["Non-sustained tachycardia",
    "Non-sustained ventricular tachycardia lasts under 30 seconds. His run lasted 45 seconds, which makes it sustained "
    "even though it stopped on its own and he stayed stable.", "reversed direction or value"],
   ["Polymorphic tachycardia",
    "Polymorphic ventricular tachycardia has QRS shapes that vary from beat to beat. Every complex in his run had the "
    "same shape, which makes it monomorphic.", "ruled out by a stated finding"],
   ["Ventricular fibrillation",
    "Ventricular fibrillation has no organized complexes, no pulse and no perfusion. He had regular identical wide "
    "complexes and stayed alert, which is sustained monomorphic ventricular tachycardia.",
    "ruled out by a stated finding"]],
  (39, 40, 42), "manifestation", "diagnosis"),

X(L, "classify", VTA, A,
  "A 64-year-old woman with a prior myocardial infarction has monomorphic ventricular tachycardia at 180 beats per "
  "minute. Her blood pressure is 128/78 mm Hg, she is alert and oriented and has no chest pain, but she is short of "
  "breath. A pulse is present. Which is the next step?",
  [["Synchronized cardioversion",
    "Correct. Instability in ventricular tachycardia is defined as ANY one of chest pain, altered mental status, "
    "shortness of breath or hypotension. Her shortness of breath alone makes her unstable despite a normal pressure, "
    "and with a pulse present unstable monomorphic ventricular tachycardia gets synchronized cardioversion."],
   ["Intravenous amiodarone",
    "Amiodarone is pharmacologic cardioversion for STABLE monomorphic ventricular tachycardia. Shortness of breath is "
    "one of the four instability criteria, so she is unstable and needs synchronized cardioversion.",
    "ruled out by a stated finding"],
   ["Unsynchronized defibrillation",
    "Defibrillation (unsynchronized) is for pulseless ventricular tachycardia. She has a pulse, so her unstable "
    "monomorphic ventricular tachycardia is treated with synchronized cardioversion.", "ruled out by a stated finding"],
   ["Monitor; she is stable",
    "A normal blood pressure does not make her stable: shortness of breath is one of the four instability criteria, "
    "with chest pain, altered mental status and hypotension. She needs synchronized cardioversion.",
    "common lay belief"]],
  (45,), "escalation", "next step"),
]

# =====================================================================================================
# LECTURE 31 -- Pericardial Disease. No doses, no pressor names, no stage durations, no "gold standard".
# =====================================================================================================
L = "l31"
A, POP = S31.IO_A, S31.IO_POP
ACP, RCP, CON, EFF, TAM = ("Acute pericarditis", "Recurrent pericarditis", "Constrictive pericarditis",
                           "Pericardial effusion", "Cardiac tamponade")

QUESTIONS += [

X(L, "comorbid", ACP, POP,
  "A 64-year-old man with type 2 diabetes had a myocardial infarction treated with a coronary stent 3 days ago and "
  "takes aspirin and clopidogrel. He now has sharp chest pain that is worse lying flat and eases when he leans "
  "forward, and a pericardial friction rub (a superficial scratchy or squeaking sound) is heard. Troponin is falling "
  "from its peak. Which anti-inflammatory drug is appropriate?",
  [["Aspirin",
    "Correct. Positional pain with a friction rub days after an infarction is post-infarction pericarditis. Nonsteroidal anti-inflammatory drugs such as ibuprofen and indomethacin are not given for post-infarction pericarditis, and glucocorticoids are also avoided, so aspirin is the anti-inflammatory; he is already in the aspirin-as-antiplatelet group in whom the others are avoided."],
   ["Ibuprofen",
    "Ibuprofen is a first-line nonsteroidal anti-inflammatory drug for most acute idiopathic or viral pericarditis, but nonsteroidal anti-inflammatory drugs are not given for "
    "post-infarction pericarditis. Three days after his infarction, aspirin is the anti-inflammatory to use.",
    "adjacent fact"],
   ["Indomethacin",
    "Indomethacin is listed with ibuprofen as a first-line nonsteroidal anti-inflammatory drug for most patients, but nonsteroidal anti-inflammatory drugs are avoided after a "
    "myocardial infarction. His pericarditis follows an infarction 3 days ago, so aspirin is used.",
    "adjacent fact"],
   ["Prednisone",
    "Prednisone is second-line therapy when nonsteroidal anti-inflammatory drugs are contraindicated, but glucocorticoid therapy is also avoided in "
    "peri-infarction pericarditis. Aspirin is the anti-inflammatory for pericarditis after an infarction.",
    "adjacent fact"]],
  (28, 29), "first-line", "treatment"),

X(L, "comorbid", ACP, POP,
  "A 71-year-old woman with hypertension had a myocardial infarction 3 weeks ago and takes aspirin. She now has fever, "
  "sharp pleuritic chest pain (worse with each breath in) that eases leaning forward, and widespread concave ST "
  "elevation: Dressler syndrome. A colchicine-based regimen with gastrointestinal protection is planned. Which drug "
  "should be avoided?",
  [["Indomethacin",
    "Correct. Pericarditis weeks after an infarction (Dressler syndrome) is post-infarction pericarditis, and nonsteroidal anti-inflammatory drugs "
    "such as indomethacin and ibuprofen are not given for it; aspirin is the anti-inflammatory used instead, with "
    "colchicine and gastrointestinal protection."],
   ["Aspirin",
    "Aspirin is the anti-inflammatory that IS used for post-infarction pericarditis, and she already takes it as an "
    "antiplatelet. The drug to avoid is a nonsteroidal anti-inflammatory drug such as indomethacin.", "reversed direction or value"],
   ["Colchicine",
    "Colchicine is paired with aspirin or a nonsteroidal anti-inflammatory drug as first-line therapy for most patients and is not one of the drugs "
    "avoided after an infarction. The drug to avoid here is the nonsteroidal anti-inflammatory drug indomethacin.", "adjacent fact"],
   ["A proton pump inhibitor",
    "Gastrointestinal protection with a proton pump inhibitor such as omeprazole is recommended with anti-inflammatory "
    "therapy, not avoided. The drug to avoid after an infarction is a nonsteroidal anti-inflammatory drug such as indomethacin.",
    "reversed direction or value"]],
  (28, 29, 34), "avoid", "avoid"),

X(L, "comorbid", ACP, A,
  "A 45-year-old woman with a recent viral illness has acute pericarditis: sharp substernal chest pain relieved by "
  "leaning forward, a pericardial friction rub (a superficial scratchy sound) and widespread ST elevation. She has a "
  "documented contraindication to nonsteroidal anti-inflammatory drugs. She is afebrile without an effusion. Which "
  "regimen fits?",
  [["Prednisone plus colchicine",
    "Correct. Nonsteroidal anti-inflammatory drugs plus colchicine are the initial therapy for most acute idiopathic or viral pericarditis, but prednisone is used if nonsteroidal anti-inflammatory drugs cannot be taken: second-line therapy, for refractory cases or a contraindication to nonsteroidal anti-inflammatory drugs, is prednisone plus colchicine. Her documented nonsteroidal anti-inflammatory drug contraindication puts her there."],
   ["Ibuprofen plus colchicine",
    "Ibuprofen plus colchicine is first-line for most acute viral pericarditis, but she has a documented "
    "contraindication to nonsteroidal anti-inflammatory drugs. When nonsteroidal anti-inflammatory drugs cannot be taken, prednisone replaces them, still with colchicine.",
    "ruled out by a stated finding"],
   ["Anakinra by itself",
    "Anti-interleukin-1 therapy (anakinra or rilonacept) is preferred for RECURRENT, colchicine-resistant or "
    "steroid-dependent disease, or earlier with an inflammatory phenotype. A first episode with a nonsteroidal anti-inflammatory drug "
    "contraindication gets prednisone plus colchicine.", "wrong stage or severity"],
   ["Pericardiectomy now",
    "Pericardiectomy is not among the listed regimens for acute pericarditis, which are drug therapy: nonsteroidal anti-inflammatory drugs or prednisone, each with colchicine. A first uncomplicated episode with a nonsteroidal anti-inflammatory drug contraindication gets prednisone plus colchicine.",
    "wrong stage or severity"]],
  (28, 29), "first-line", "treatment"),

X(L, "comorbid", ACP, POP,
  "An 82-year-old woman with osteoporosis and a hip fracture last year has acute idiopathic pericarditis. Her "
  "clinician reviews the drugs used for pericarditis with her age and bones in mind. Which drug most raises her "
  "osteoporosis risk?",
  [["Prednisone",
    "Correct. In elderly patients with pericarditis, corticosteroids increase osteoporosis risk, which matters for an "
    "82-year-old with osteoporosis and a prior fracture. Older adults also need caution with nonsteroidal anti-inflammatory drugs and colchicine, "
    "with dose reduction considered, but the bone risk belongs to the corticosteroid."],
   ["Colchicine",
    "Colchicine calls for caution in older adults, with a dose reduction considered (Beers list), but it is not the "
    "drug tied to osteoporosis. Corticosteroids such as prednisone raise osteoporosis risk.", "adjacent fact"],
   ["Ibuprofen",
    "Nonsteroidal anti-inflammatory drugs such as ibuprofen need caution in older adults (Beers list), but the listed bone risk in the elderly comes from corticosteroids. Prednisone is the drug that raises her osteoporosis risk.", "adjacent fact"],
   ["Aspirin",
    "Aspirin is a first-line anti-inflammatory for pericarditis and calls for the same nonsteroidal anti-inflammatory drug caution in older adults, "
    "but it is not the drug linked to osteoporosis; corticosteroids are.", "adjacent fact"]],
  (29, 36), "avoid", "avoid"),

X(L, "comorbid", ACP, POP,
  "A 70-year-old man with atrial fibrillation on warfarin and hypertension has had 1 day of sharp chest pain that is "
  "worse lying flat and better leaning forward. His electrocardiogram shows widespread concave ST elevation with PR "
  "depression. He is afebrile with stable vital signs, troponin is normal, and echocardiography shows a small "
  "effusion without tamponade. Which is the most appropriate next step?",
  [["Hospital admission",
    "Correct. Patients on oral anticoagulants are among the features of higher risk and possible need for "
    "hospitalization in acute pericarditis, and anticoagulation is also linked to the poorest prognosis. His warfarin "
    "therefore moves him from outpatient care to admission even though he is otherwise stable."],
   ["Outpatient anti-inflammatories",
    "Outpatient nonsteroidal anti-inflammatory drugs and colchicine fit low-risk acute pericarditis. Being on an oral anticoagulant is a listed "
    "high-risk feature that points to hospitalization, so he is admitted.", "ruled out by a stated finding"],
   ["Urgent pericardiocentesis",
    "Pericardiocentesis is for tamponade, moderate to large refractory effusions with severe symptoms, or suspected "
    "bacterial or neoplastic disease. His effusion is small without tamponade; his anticoagulation calls for admission.",
    "wrong stage or severity"],
   ["Discharge, recheck in a month",
    "Discharge ignores a listed high-risk feature: patients on oral anticoagulants may need hospitalization and have a "
    "poorer prognosis. He should be admitted.", "ruled out by a stated finding"]],
  (27, 32), "referral", "next step"),

X(L, "score", ACP, A,
  "A 58-year-old woman with rheumatoid arthritis on immunosuppressive therapy has had 1 day of sharp chest pain that "
  "eases leaning forward. Her temperature is 38.7 °C (101.7 °F), troponin is 0.12 ng/mL (normal under 0.04), and "
  "echocardiography shows a small effusion without tamponade. She takes no anticoagulant and has had no trauma. How "
  "many of the listed higher-risk features for acute pericarditis does she have?",
  [["Three",
    "Correct. Fever above 38 °C (1), immunosuppression (1) and an elevated troponin suggesting myopericarditis (1) are "
    "listed higher-risk features: 1 + 1 + 1 = 3. Her effusion is small (the feature is a MODERATE to large one), her "
    "onset was acute, and she has no anticoagulant or trauma. Any of these features points to possible hospitalization."],
   ["One",
    "One counts only the fever. Immunosuppressive therapy and an elevated troponin are listed higher-risk features "
    "too, so she has three.", "adjacent fact"],
   ["Two",
    "Two misses one item, usually the troponin: an elevated cardiac troponin suggests myopericarditis and is a listed "
    "higher-risk feature. Fever, immunosuppression and troponin make three.", "adjacent fact"],
   ["Four",
    "Four counts her small effusion, but the listed feature is a MODERATE to large effusion. Fever, immunosuppression "
    "and an elevated troponin make three.", "ruled out by a stated finding"]],
  (26, 27), "prognosis", "test"),

X(L, "score", ACP, A,
  "A 31-year-old man had an upper respiratory infection last week. He has sharp substernal chest pain that is worse "
  "lying back and eases leaning forward. No pericardial friction rub (a superficial scratchy sound) is heard on repeated examination. His electrocardiogram shows "
  "widespread concave ST elevation with PR depression and reciprocal ST depression in aVR. Echocardiography shows no "
  "pericardial effusion. How many of the four diagnostic criteria for acute pericarditis does he meet?",
  [["Criteria met: 2",
    "Correct. The four criteria are sharp substernal chest pain, a pericardial friction rub, suggestive "
    "electrocardiogram changes (widespread ST elevation) and a new or worsening effusion. He has the chest pain (1) and "
    "the electrocardiogram changes (1): 1 + 1 = 2, which meets the two-of-four rule for a clinical diagnosis."],
   ["Criteria met: 1",
    "One criterion counts only his chest pain. Widespread concave ST elevation with PR depression is the suggestive "
    "electrocardiogram criterion, so he meets two of four.", "adjacent fact"],
   ["Criteria met: 3",
    "Three would need a friction rub or an effusion as well, and he has neither: no rub on repeated examination and no "
    "effusion on echocardiography. He meets two: the pain and the electrocardiogram.", "ruled out by a stated finding"],
   ["Criteria met: 4",
    "Four would need all of pain, rub, electrocardiogram changes and a new effusion. He has no rub and no effusion, so "
    "he meets two, which is still enough for the diagnosis.", "ruled out by a stated finding"]],
  (14, 19), "manifestation", "test"),

X(L, "comorbid", ACP, A,
  "A 66-year-old man with end-stage kidney disease and diabetes has missed a week of dialysis. He has pleuritic chest "
  "pain (sharp, worse with each breath in) and a pericardial friction rub (a superficial scratchy sound). Blood urea "
  "nitrogen is 96 mg/dL (normal 7-20). Echocardiography shows a small effusion without tamponade. Which treatment "
  "addresses the cause?",
  [["Resume dialysis",
    "Correct. A blood urea nitrogen above 60 mg/dL marks uremic pericarditis, and his 96 after a missed week of "
    "dialysis fits. Treatment targets the underlying disorder, and for uremia that is dialysis."],
   ["Pericardiectomy",
    "Pericardiectomy is considered for constrictive pericarditis, large refractory effusions or frequent symptomatic "
    "recurrences. His uremic pericarditis with a small effusion is treated by dialysis.", "wrong stage or severity"],
   ["Tuberculosis therapy",
    "Treating tuberculosis addresses tuberculous pericarditis, mainly in developing countries, and can slow "
    "constriction. His blood urea nitrogen of 96 after missed dialysis points to uremia, treated with dialysis.",
    "competing diagnosis"],
   ["Prednisone",
    "Steroids treat the underlying disorder in AUTOIMMUNE pericarditis. His pericarditis is uremic (blood urea "
    "nitrogen 96 after missed dialysis), and the underlying-cause treatment for uremia is dialysis.",
    "competing diagnosis"]],
  (11, 34), "first-line", "treatment"),

X(L, "comorbid", ACP, A,
  "A 54-year-old woman with resistant hypertension has taken hydralazine for a year. She now has joint pains, "
  "pleuritic chest pain (sharp, worse with each breath in) and a pericardial friction rub (a superficial scratchy "
  "sound). Antinuclear antibody is positive, blood urea nitrogen is 14 mg/dL (normal 7-20), and she has had no "
  "tuberculosis exposure or recent viral illness. Which is the most likely cause of her pericarditis?",
  [["Drug-induced lupus",
    "Correct. Drug-induced lupus from procainamide or hydralazine is a listed iatrogenic cause of pericarditis. A year "
    "of hydralazine, joint pains and a positive antinuclear antibody fit it, and her normal urea nitrogen and lack of "
    "tuberculosis exposure or viral illness make the other causes unlikely."],
   ["Uremic pericarditis",
    "Uremic pericarditis needs a blood urea nitrogen above 60 mg/dL; hers is 14. Hydralazine with joint pains and a "
    "positive antinuclear antibody points to drug-induced lupus.", "ruled out by a stated finding"],
   ["Tuberculous pericarditis",
    "Tuberculosis is a cause of pericarditis especially in developing countries, but she has no exposure. A year of "
    "hydralazine with a positive antinuclear antibody fits drug-induced lupus.", "ruled out by a stated finding"],
   ["Viral pericarditis",
    "Most idiopathic pericarditis is likely viral, but she had no recent viral illness, and hydralazine with joint "
    "pains and a positive antinuclear antibody gives a specific cause: drug-induced lupus.", "competing diagnosis"]],
  (8, 11, 58), "etiology", "diagnosis"),

X(L, "comorbid", ACP, A,
  "A 20-year-old college soccer player with mild asthma was diagnosed with viral pericarditis 2 weeks ago. His pain "
  "has been gone for 5 days, but his C-reactive protein is still 18 mg/L (normal under 10). He asks when he can "
  "return to full training. Which answer is accurate?",
  [["Once 1 month out and markers normal",
    "Correct. Strenuous activity is avoided until symptoms resolve and biomarkers such as C-reactive protein normalize, "
    "and for at least 1 month after diagnosis with a maximal heart rate under 100. At 2 weeks with a C-reactive "
    "protein of 18 he meets neither the time nor the marker condition."],
   ["Now, because his pain has resolved",
    "Pain resolution alone is not enough: strenuous activity waits for normal biomarkers and at least 1 month from "
    "diagnosis. His C-reactive protein is still 18 at 2 weeks.", "common lay belief"],
   ["After 24 hours free of symptoms",
    "Twenty-four symptom-free hours is the point at which drug TAPERING can begin, not the return to strenuous "
    "activity, which needs at least 1 month and normal biomarkers.", "adjacent fact"],
   ["After a week of colchicine therapy",
    "One week is the point by which a failure to respond to nonsteroidal anti-inflammatory drug plus colchicine suggests another cause; it is not a "
    "return-to-play rule. Strenuous activity waits at least 1 month and for normal biomarkers.", "adjacent fact"]],
  (28, 30), "education", "education"),

X(L, "comorbid", RCP, A,
  "A 47-year-old woman with hypothyroidism has her third episode of pericarditis. She has stayed on colchicine, but "
  "every attempt to taper prednisone has brought a flare (steroid-dependent disease). She has a temperature of 38.4 "
  "°C and a C-reactive protein of 42 mg/L (normal under 10). Which therapy is preferred now?",
  [["Anakinra or rilonacept",
    "Correct. Current guidance supports anti-interleukin-1 therapy (anakinra or rilonacept) earlier for an inflammatory "
    "phenotype (C-reactive protein over 10 mg/L, fever, pericardial inflammation), and it is preferred for recurrent, "
    "colchicine-resistant or steroid-dependent disease. She is recurrent, steroid-dependent and inflamed."],
   ["Higher-dose prednisone",
    "Escalating prednisone ignores that she is already steroid-dependent, one of the situations in which "
    "anti-interleukin-1 therapy (anakinra or rilonacept) is preferred. Corticosteroids also carry osteoporosis risk.",
    "wrong stage or severity"],
   ["Ibuprofen by itself",
    "A nonsteroidal anti-inflammatory drug is part of first-line therapy for a FIRST episode, and dropping colchicine and steroid support at her "
    "third flare would undertreat her. Recurrent, steroid-dependent disease calls for anakinra or rilonacept.",
    "wrong stage or severity"],
   ["Stopping colchicine",
    "Colchicine is continued for months in recurrent disease (6 months or more), not stopped. Her steroid dependence "
    "with fever and a high C-reactive protein calls for anti-interleukin-1 therapy.", "reversed direction or value"]],
  (29, 35), "escalation", "treatment"),

X(L, "comorbid", TAM, A,
  "A 25-year-old man with asthma is brought in after a stab wound to the left chest. His blood pressure is 78/50 mm "
  "Hg, his neck veins are distended and his heart sounds are muffled (Beck triad). Bedside ultrasound shows "
  "pericardial fluid compressing the heart. Intravenous fluids are running. Which treatment does this "
  "traumatic tamponade need next?",
  [["Emergent surgical repair",
    "Correct. Hypotension, distended neck veins and muffled heart sounds after penetrating trauma are cardiac "
    "tamponade from bleeding. Aggressive intravenous fluids support him, but HEMORRHAGIC tamponade secondary to trauma "
    "needs emergent surgery to repair the injury; pericardiocentesis is for nonhemorrhagic tamponade."],
   ["Needle pericardiocentesis",
    "Pericardiocentesis is the definitive treatment for cardiac tamponade in general, and the choice when the "
    "tamponade is nonhemorrhagic. His comes from a stab wound: hemorrhagic tamponade secondary to trauma needs "
    "emergent surgery to repair the injury, not just drainage.",
    "competing diagnosis"],
   ["Fluids, then observation",
    "Intravenous fluids increase preload and are a temporizing measure only; observation would leave a bleeding "
    "injury compressing the heart. Traumatic hemorrhagic tamponade needs emergent surgical repair.",
    "wrong stage or severity"],
   ["Ibuprofen and colchicine",
    "Nonsteroidal anti-inflammatory drugs and colchicine treat acute pericarditis, an inflammatory process. Blood compressing the heart after a stab wound is hemorrhagic tamponade, treated with emergent surgery.", "confused mechanism or drug class"]],
  (54, 68, 71), "first-line", "treatment"),

X(L, "comorbid", TAM, POP,
  "A 61-year-old woman with metastatic lung cancer has worsening dyspnea. Her blood pressure is 84/52 mm Hg with "
  "pulsus paradoxus (a 10 mm Hg drop in blood pressure with inspiration), and her jugular venous pressure is "
  "elevated. Echocardiography shows a large effusion with right ventricular diastolic collapse. While "
  "pericardiocentesis is being arranged, which measure helps stabilize her?",
  [["Intravenous fluid bolus",
    "Correct. Pulsus paradoxus, hypotension, raised jugular pressure and right ventricular diastolic collapse are "
    "cardiac tamponade, for which expedient pericardiocentesis is definitive. Intravenous fluids are given meanwhile to "
    "increase preload and prevent collapse of the right ventricle, a temporizing measure."],
   ["Intravenous furosemide",
    "Furosemide removes fluid, the opposite of what tamponade needs: intravenous fluids are given to increase preload "
    "and keep the compressed right ventricle from collapsing until the fluid is drained.",
    "reversed direction or value"],
   ["Ibuprofen plus colchicine",
    "Nonsteroidal anti-inflammatory drugs and colchicine treat acute pericarditis but do nothing to relieve a large effusion compressing the heart. She needs intravenous fluids to support preload until pericardiocentesis.", "confused mechanism or drug class"],
   ["Repeat echo tomorrow",
    "Waiting a day ignores tamponade, an emergency with hypotension and right ventricular collapse. She needs "
    "intravenous fluids now as a bridge to expedient pericardiocentesis.", "wrong stage or severity"]],
  (59, 63, 68, 71), "first-line", "next step"),

X(L, "comorbid", EFF, POP,
  "A 58-year-old woman with metastatic breast cancer had a large pericardial effusion drained for tamponade. Cytology "
  "of the fluid shows malignant cells. She is stable and asks what to expect next. Which step is recommended?",
  [["Palliative care consultation",
    "Correct. A symptomatic malignant pericardial effusion carries a limited life expectancy (median 2 to 4 months), "
    "and the effusion often recurs in that time. A palliative care consult is recommended to improve outcomes and "
    "quality of life, alongside close oncology and cardiology follow-up."],
   ["Pericardiectomy as a cure",
    "A pericardial window or pericardiectomy can manage RECURRENT effusions, but it does not cure a malignant "
    "effusion, whose prognosis follows the cancer. A palliative care consult is recommended.",
    "wrong stage or severity"],
   ["Colchicine for 3 months",
    "Colchicine for 3 months treats acute pericarditis. A malignant effusion is managed by treating the underlying "
    "cancer, with a palliative care consult given the limited life expectancy.", "confused mechanism or drug class"],
   ["No further follow-up needed",
    "Large effusions are followed with serial transthoracic echocardiograms, and malignant effusions often recur "
    "within months. She needs close follow-up and a palliative care consult.", "reversed direction or value"]],
  (69, 70), "prognosis", "referral"),

X(L, "comorbid", CON, POP,
  "A 63-year-old man treated with chest radiation for lymphoma 15 years ago has anasarca (generalized swelling) and "
  "an elevated jugular venous pressure that rises during inspiration (Kussmaul sign). Echocardiography shows a "
  "thickened pericardium with septal bounce: constrictive pericarditis. Pericardiectomy is scheduled for next week. "
  "How should his diuretics be handled before surgery?",
  [["Use them sparingly",
    "Correct. Constrictive pericarditis is often a surgical disease, and if surgery is planned, diuretics should be "
    "used sparingly in the preoperative period. Diuretics treat fluid overload in early, stable constriction on a "
    "medical trial, but heavy preoperative diuresis is avoided."],
   ["Increase them aggressively",
    "Aggressive diuresis is what the preoperative rule warns against: if surgery is planned, diuretics are used "
    "sparingly. His fluid overload is ultimately relieved by the pericardiectomy.", "reversed direction or value"],
   ["Swap them for fluid boluses",
    "Fluid boluses are the temporizing measure for cardiac TAMPONADE, to raise preload. He has constriction with "
    "anasarca; before surgery his diuretics are continued sparingly, not replaced with fluid.",
    "competing diagnosis"],
   ["Add a second diuretic",
    "Adding a second diuretic intensifies diuresis, the opposite of the preoperative rule. When pericardiectomy is "
    "planned, diuretics are used sparingly.", "reversed direction or value"]],
  (39, 41, 49), "avoid", "treatment"),

X(L, "comorbid", CON, POP,
  "A 61-year-old man with hypertension has constrictive pericarditis caused by chest radiation he received for "
  "lymphoma years ago. He has an elevated jugular venous pressure that rises during inspiration (Kussmaul sign) and "
  "is scheduled for pericardiectomy. He asks what in his case most affects survival. Which feature is linked to the "
  "worst survival?",
  [["Prior chest radiation",
    "Correct. Etiology is an important determinant of survival in constrictive pericarditis, and prior ionizing "
    "radiation is associated with the worst survival rates. Pericardiectomy still improves survival (5-year about 80%, "
    "10-year about 60%), and earlier surgery has better outcomes."],
   ["Pericardial calcification",
    "Pericardial calcification is a highly specific but uncommon DIAGNOSTIC finding of constriction, not the "
    "survival marker. The cause linked to the worst survival is prior ionizing radiation.", "adjacent fact"],
   ["Choosing earlier surgery",
    "Earlier intervention is associated with IMPROVED outcomes in those who need surgery, not worse ones. His "
    "radiation-related cause is the feature tied to the worst survival.", "reversed direction or value"],
   ["An idiopathic or viral cause",
    "More than half of constrictive pericarditis is idiopathic or viral, but those are not the causes with the worst "
    "survival. Prior ionizing radiation carries the worst survival rates.", "competing diagnosis"]],
  (39, 40, 47, 50), "prognosis", "complication"),

X(L, "classify", ACP, A,
  "A 39-year-old woman with rheumatoid arthritis developed pericarditis 9 weeks ago. Despite treatment her sharp chest "
  "pain has never fully gone away; she has had no symptom-free stretch. Which term describes her pericarditis now?",
  [["Incessant",
    "Correct. Incessant pericarditis is when symptoms persist for more than 4 to 6 weeks, up to 3 months, without a "
    "sustained remission. At 9 weeks with no symptom-free stretch she fits; past 3 months it would be chronic."],
   ["Acute",
    "Acute pericarditis is inflammation lasting under 4 to 6 weeks. Hers has persisted 9 weeks without remission, which "
    "makes it incessant.", "reversed direction or value"],
   ["Recurrent",
    "Recurrent pericarditis is a RETURN of symptoms after a symptom-free interval of 4 to 6 weeks or longer. She has "
    "never had a symptom-free stretch, so hers is incessant.", "ruled out by a stated finding"],
   ["Chronic",
    "Chronic pericarditis is symptoms persisting for more than 3 months. At 9 weeks without remission she is in the "
    "incessant window of more than 4 to 6 weeks up to 3 months.", "reversed direction or value"]],
  (5,), "manifestation", "diagnosis"),
]

# =====================================================================================================
# LECTURE 32 -- Infective Endocarditis. Duke criteria as on slides 22-23 (definite: 2 major, 1 major +
# 3 minor, or 5 minor; possible: 1 major + 1 minor, or 3 minor). No doses.
# =====================================================================================================
L = "l32"
DUKE, PROPH, REG, A = S32.IO_DUKE, S32.IO_PROPH, S32.IO_REGIMEN, S32.IO_A
IE = "Infective endocarditis"
D2M, D13, D5m = "Definite: two major criteria", "Definite: one major, three minor", "Definite: five minor criteria"
P11, P3m = "Possible: one major, one minor", "Possible: three minor criteria"

QUESTIONS += [

X(L, "score", IE, DUKE,
  "A 63-year-old man with a prosthetic aortic valve and type 2 diabetes has 10 days of malaise and fever to 38.8 °C "
  "(101.8 °F). Two separate blood cultures grow Staphylococcus aureus. Transesophageal echocardiography shows an "
  "oscillating mass on the prosthetic valve. Which modified Duke classification fits?",
  [[D2M,
    "Correct. Staphylococcus aureus, a typical organism, from two separate blood cultures is one major criterion, and an "
    "oscillating intracardiac mass on the valve is the second (evidence of endocardial involvement). Two major criteria "
    "define definite endocarditis; his prosthetic valve and fever are minor criteria that are not needed."],
   [D13,
    "One major plus three minor is another route to definite endocarditis, but it miscounts him: both the cultures and "
    "the echocardiogram are MAJOR criteria, and he has only two minor ones (prosthetic valve, fever).",
    "adjacent fact"],
   [P11,
    "One major plus one minor criterion gives possible endocarditis. He has TWO major criteria, a typical organism in "
    "two separate cultures and an oscillating mass on echocardiography, which makes it definite.",
    "wrong stage or severity"],
   [P3m,
    "Three minor criteria alone give possible endocarditis, but his cultures and echocardiogram are major criteria, not "
    "minor ones. With two major criteria he is definite.", "wrong stage or severity"]],
  (22, 23, 25), "test finding", "test"),

X(L, "score", IE, DUKE,
  "A 52-year-old woman with type 1 diabetes has 2 weeks of fatigue and a temperature of 38.4 °C (101.1 °F). She has no "
  "known heart disease, does not inject drugs and has no skin, eye or nail findings. Three sets of blood cultures show "
  "no growth. Transesophageal echocardiography shows an oscillating mass on the mitral valve. Which modified Duke "
  "classification fits?",
  [[P11,
    "Correct. The oscillating mass on the valve is a major criterion (1), and a fever of 38.0 °C or higher is a minor "
    "criterion (1). Her cultures are negative and diabetes is not a listed predisposing heart condition, so she has "
    "one major plus one minor: possible endocarditis."],
   [D2M,
    "Two major criteria would need positive blood cultures as well as the echocardiogram finding. Her three culture "
    "sets show no growth, so she has one major criterion (the mass) and one minor (fever): possible.",
    "ruled out by a stated finding"],
   [D13,
    "One major plus three minor needs three minor criteria; she has only fever. Diabetes is not a predisposing heart "
    "condition, and she has no vascular or immunologic findings, so she is possible, not definite.",
    "adjacent fact"],
   [P3m,
    "Three minor criteria would need predisposition, vascular or immunologic findings besides fever, and she has none. "
    "Her valve mass is a MAJOR criterion, giving one major plus one minor: possible.", "adjacent fact"]],
  (22, 23, 25), "test finding", "test"),

X(L, "score", IE, DUKE,
  "A 34-year-old man who injects heroin has a temperature of 39.2 °C (102.6 °F) and painless flat red spots on his "
  "soles (Janeway lesions). Two separate blood cultures grow Staphylococcus aureus. Transthoracic echocardiography shows "
  "no vegetation, and a transesophageal study is pending. Which modified Duke classification fits now?",
  [[D13,
    "Correct. Staphylococcus aureus from two separate blood cultures is one major criterion. Injection drug use "
    "(predisposition), fever of 38.0 °C or higher, and Janeway lesions (vascular phenomena) are three minor criteria: "
    "1 major + 3 minor = definite endocarditis, even before the transesophageal study."],
   [D2M,
    "Two major criteria would need echocardiographic evidence of endocardial involvement as well; his transthoracic "
    "study showed no vegetation. His one major (cultures) plus three minor criteria still make it definite.",
    "ruled out by a stated finding"],
   [P11,
    "One major plus one minor undercounts him: injection drug use, fever and Janeway lesions are three separate minor "
    "criteria. One major with three minor is definite.", "adjacent fact"],
   [P3m,
    "Three minor criteria alone give possible endocarditis, but his cultures are a MAJOR criterion (a typical organism "
    "in two separate cultures). One major plus three minor is definite.", "adjacent fact"]],
  (13, 22, 23), "test finding", "test"),

X(L, "score", IE, DUKE,
  "A 70-year-old woman with a prosthetic mitral valve has a temperature of 38.6 °C (101.5 °F) and painful red nodules "
  "on her finger pads (Osler nodes). Three sets of blood cultures show no growth, and transesophageal echocardiography "
  "shows no vegetation, abscess or new regurgitation. Which modified Duke classification fits?",
  [[P3m,
    "Correct. Her prosthetic valve (predisposition), fever of 38.0 °C or higher, and Osler nodes (immunologic "
    "phenomena) are three minor criteria, and she has no major criterion. Three minor criteria make possible "
    "endocarditis, and a normal transesophageal study does not necessarily rule it out."],
   [D5m,
    "Five minor criteria would need two more: microbiologic evidence and a vascular phenomenon, for example. She has "
    "three minor criteria (prosthetic valve, fever, Osler nodes) and no major, which is possible.",
    "adjacent fact"],
   [P11,
    "One major plus one minor needs a major criterion, but her cultures are negative and the transesophageal study shows "
    "no vegetation, abscess or new regurgitation. Her three minor criteria make it possible.",
    "ruled out by a stated finding"],
   [D13,
    "Definite by one major plus three minor needs a major criterion, and she has none: negative cultures and a "
    "transesophageal study without endocardial involvement. Three minor criteria alone make it possible.",
    "ruled out by a stated finding"]],
  (13, 22, 23, 25), "test finding", "test"),

X(L, "score", IE, DUKE,
  "A 58-year-old man treated for infective endocarditis 3 years ago now has a temperature of 38.9 °C (102.0 °F), "
  "conjunctival hemorrhages and Roth spots (white-centered retinal hemorrhages). One of three blood cultures grows "
  "viridans streptococci; the other two show no growth. Transesophageal echocardiography is normal. Which modified "
  "Duke classification fits?",
  [[D5m,
    "Correct. Prior endocarditis (predisposition), fever, conjunctival hemorrhages (vascular), Roth spots (immunologic) "
    "and one positive culture that does not meet the major rule (microbiologic) are five minor criteria: "
    "1 + 1 + 1 + 1 + 1 = 5, which defines definite endocarditis without any major criterion."],
   [P3m,
    "Three minor criteria undercount him. Prior endocarditis, fever, conjunctival hemorrhages, Roth spots and the single "
    "positive culture are five minor criteria, and five minor make it definite.", "adjacent fact"],
   [D13,
    "One major plus three minor treats his single positive culture as major, but the major culture criterion needs a "
    "typical organism from TWO separate cultures (or persistently positive cultures). One of three is a minor criterion.",
    "reversed direction or value"],
   [P11,
    "One major plus one minor would need a major criterion; his single positive culture is minor and his "
    "transesophageal study is normal. His five minor criteria make it definite.", "adjacent fact"]],
  (12, 22, 23), "test finding", "test"),

X(L, "score", IE, DUKE,
  "A 41-year-old woman had a ventricular septal defect repaired in childhood, with no residual defect. She now has a "
  "temperature of 38.3 °C (100.9 °F), and her long-known murmur sounds louder. One of three blood cultures grows "
  "coagulase-negative staphylococci. Transthoracic echocardiography shows no vegetation. How many modified Duke "
  "criteria does she meet?",
  [["No major, one minor",
    "Correct. Only her fever (38.0 °C or higher) counts, as one minor criterion. A repaired ventricular septal defect is "
    "excluded from predisposing conditions, an increase in a preexisting murmur is not sufficient for the major "
    "regurgitation criterion, and a single culture of coagulase-negative staphylococci is excluded as a common "
    "contaminant."],
   ["No major, three minor",
    "Three minor criteria would count her repaired septal defect and the single culture, but both are excluded: a "
    "repaired ventricular septal defect is not a predisposition, and one coagulase-negative staphylococcal culture is a "
    "likely contaminant. Only the fever counts.", "ruled out by a stated finding"],
   ["One major, one minor",
    "This treats her louder murmur as new valvular regurgitation, a major criterion, but an increase or change in a "
    "preexisting murmur is not sufficient. With no major criterion, she has one minor: the fever.",
    "ruled out by a stated finding"],
   ["One major, two minor",
    "No major criterion is met: the louder old murmur does not count, the echocardiogram shows no vegetation and a "
    "single coagulase-negative staphylococcal culture is excluded. She has one minor criterion, the fever.",
    "ruled out by a stated finding"]],
  (22,), "test finding", "test"),

X(L, "score", IE, DUKE,
  "A 67-year-old man with hypertension has 3 weeks of low fevers to 38.2 °C (100.8 °F), fatigue and weight loss. He "
  "now has a holosystolic murmur; he had no murmur before, and echocardiography confirms new mitral regurgitation "
  "without a vegetation. Two blood cultures drawn more than "
  "12 hours apart both grow Enterococcus faecalis, and no other source of infection is found. Which modified Duke "
  "classification fits?",
  [[D2M,
    "Correct. Community-acquired enterococci in two separate cultures without a primary focus meet the major culture "
    "criterion (1), and NEW valvular regurgitation is evidence of endocardial involvement, the second major criterion "
    "(2). Two major criteria make definite endocarditis; the weeks-long low fever and weight loss fit a subacute "
    "course."],
   [D13,
    "One major plus three minor undercounts his major criteria: new valvular regurgitation, confirmed here on "
    "echocardiography, is itself a major criterion alongside the cultures. He has only one minor criterion (fever), "
    "and two major criteria already make it definite.",
    "adjacent fact"],
   [P11,
    "One major plus one minor treats the new mitral regurgitation as minor or ignores it. New valvular regurgitation is "
    "a major criterion, so with his cultures he has two major: definite.", "adjacent fact"],
   [P3m,
    "Three minor criteria would need predisposition and vascular or immunologic findings; he has only fever as a minor. "
    "His cultures and new regurgitation are two major criteria: definite.", "adjacent fact"]],
  (10, 16, 22), "test finding", "test"),

X(L, "classify", IE, DUKE,
  "A 50-year-old man being evaluated for endocarditis has painful red nodules on his finger pads, painless flat red "
  "spots on his soles, conjunctival hemorrhages, and septic pulmonary infarcts on chest imaging. Which finding counts "
  "as an immunologic minor criterion?",
  [["Painful finger-pad nodules",
    "Correct. Painful finger-pad nodules are Osler nodes, and the immunologic minor criterion covers glomerulonephritis, "
    "Osler nodes, Roth spots and rheumatoid factor. His other three findings belong to the VASCULAR minor criterion, "
    "so together he has two separate minor criteria from these signs."],
   ["Painless spots on the soles",
    "Painless flat spots on the soles are Janeway lesions, which sit under the VASCULAR phenomena criterion with "
    "emboli, infarcts and conjunctival hemorrhages. The immunologic one is the painful finger-pad nodule (Osler node).",
    "adjacent fact"],
   ["Conjunctival hemorrhages",
    "Conjunctival hemorrhages are listed under vascular phenomena, not immunologic phenomena. The immunologic finding "
    "here is the painful finger-pad nodules (Osler nodes); Roth spots would also qualify.", "adjacent fact"],
   ["Septic pulmonary infarcts",
    "Septic pulmonary infarcts are vascular phenomena, listed with major arterial emboli and mycotic aneurysm. The "
    "immunologic minor criterion here is the painful finger-pad nodules (Osler nodes).", "adjacent fact"]],
  (13, 22), "manifestation", "test"),

X(L, "comorbid", IE, REG,
  "A 66-year-old woman with a transcatheter aortic valve replacement and chronic kidney disease had anaphylaxis to "
  "penicillin as a child. She needs a tooth extraction and can swallow pills. Which prophylaxis regimen fits?",
  [["Oral azithromycin",
    "Correct. A transcatheter prosthetic valve qualifies for prophylaxis before an extraction. A patient allergic to "
    "penicillin who can take pills gets azithromycin or clarithromycin (or doxycycline), and because her allergy was "
    "anaphylaxis, cephalexin is not an option for her."],
   ["Oral cephalexin",
    "Cephalexin is on the oral penicillin-allergy list, but cephalosporins should not be used in anyone with a history "
    "of anaphylaxis, angioedema or urticaria to penicillin or ampicillin. Her childhood anaphylaxis rules it out.",
    "ruled out by a stated finding"],
   ["Oral clindamycin",
    "Clindamycin is no longer recommended for dental prophylaxis because of the risk of Clostridioides difficile "
    "infection. For a penicillin-allergic patient taking pills, azithromycin, clarithromycin or doxycycline is used.",
    "common lay belief"],
   ["Oral amoxicillin",
    "Oral amoxicillin is the standard regimen only for patients WITHOUT a penicillin allergy. She had anaphylaxis to "
    "penicillin, so she gets azithromycin, clarithromycin or doxycycline instead.", "ruled out by a stated finding"]],
  (35, 36), "agent/regimen", "treatment"),

X(L, "comorbid", IE, REG,
  "A 59-year-old man with a mitral annuloplasty ring is recovering from a stroke with severe dysphagia and cannot take "
  "anything by mouth. He has no drug allergies and needs a dental extraction. Which prophylaxis regimen fits?",
  [["Intravenous ampicillin",
    "Correct. Prosthetic material used for valve repair, such as an annuloplasty ring, qualifies for prophylaxis before "
    "an extraction. Without a penicillin allergy but unable to take oral medication, he gets ampicillin "
    "(intramuscular or intravenous), or cefazolin or ceftriaxone, 30 to 60 minutes before the procedure."],
   ["Amoxicillin by mouth",
    "Oral amoxicillin is the standard choice for a patient without a penicillin allergy who CAN take pills. He cannot "
    "take anything by mouth, so the parenteral option, ampicillin, is used.", "ruled out by a stated finding"],
   ["Intravenous clindamycin",
    "Clindamycin is no longer recommended for endocarditis prophylaxis because of the risk of Clostridioides difficile "
    "infection. A patient without allergies who cannot take pills gets ampicillin.", "common lay belief"],
   ["Doxycycline by mouth",
    "Doxycycline is an oral option for a PENICILLIN-ALLERGIC patient. He has no allergy and cannot swallow, so he gets "
    "parenteral ampicillin.", "ruled out by a stated finding"]],
  (35, 36), "agent/regimen", "treatment"),

X(L, "comorbid", IE, REG,
  "A 64-year-old man with a bioprosthetic aortic valve is receiving chemotherapy and cannot keep any pills down. His "
  "penicillin allergy was a mild, delayed rash years ago, with no hives, swelling or breathing trouble. He needs a "
  "dental extraction. Which prophylaxis regimen fits?",
  [["Intravenous cefazolin",
    "Correct. A prosthetic valve qualifies for prophylaxis before an extraction. A penicillin-allergic patient who "
    "cannot take oral medication gets cefazolin or ceftriaxone, and since his reaction was a mild rash without "
    "anaphylaxis, angioedema or urticaria, a cephalosporin is allowed."],
   ["Intravenous ampicillin",
    "Ampicillin is the parenteral choice for a patient who cannot take pills and has NO penicillin allergy. He is "
    "penicillin-allergic, so the parenteral option is cefazolin or ceftriaxone.", "ruled out by a stated finding"],
   ["Azithromycin by mouth",
    "Azithromycin fits a penicillin-allergic patient who CAN take oral medication. He cannot keep pills down, so he "
    "gets cefazolin or ceftriaxone by injection.", "ruled out by a stated finding"],
   ["Intravenous clindamycin",
    "Clindamycin is no longer recommended for prophylaxis because of the risk of Clostridioides difficile infection. "
    "For a penicillin allergy without a severe reaction and no oral route, cefazolin or ceftriaxone is used.",
    "common lay belief"]],
  (35, 36), "agent/regimen", "treatment"),

X(L, "comorbid", IE, PROPH,
  "A 71-year-old man who had infective endocarditis 2 years ago and has chronic kidney disease is scheduled for a "
  "screening colonoscopy. He has no active infection. Which is correct about endocarditis prophylaxis?",
  [["Not recommended for this",
    "Correct. Prior endocarditis puts him in a high-risk group, but prophylaxis is recommended only before dental "
    "procedures that manipulate the gums or tooth roots or perforate the oral mucosa, and invasive respiratory "
    "procedures. Gastrointestinal procedures such as colonoscopy do not need it in the absence of active infection."],
   ["Amoxicillin beforehand",
    "Oral amoxicillin is the standard regimen when prophylaxis IS indicated, as before a dental extraction. Colonoscopy "
    "is a gastrointestinal procedure that does not require prophylaxis, even after prior endocarditis.",
    "wrong stage or severity"],
   ["Ampicillin beforehand",
    "Parenteral ampicillin is for an indicated procedure when the patient cannot take pills. A screening colonoscopy "
    "is not an indication: gastrointestinal procedures do not require endocarditis prophylaxis.",
    "wrong stage or severity"],
   ["Azithromycin beforehand",
    "Azithromycin is the oral choice for a penicillin-allergic patient having an indicated dental procedure. Colonoscopy "
    "does not require prophylaxis at all, whatever his allergy status.", "wrong stage or severity"]],
  (34, 36), "agent/regimen", "education"),

X(L, "comorbid", IE, PROPH,
  "A 62-year-old man with hypertension and diabetes had his mitral valve repaired with an annuloplasty ring 5 years "
  "ago. He is scheduled for a dental cleaning that will manipulate his gums. He has no allergies and can take pills. "
  "Which is correct about endocarditis prophylaxis?",
  [["Give oral amoxicillin before",
    "Correct. Prosthetic material used for valve repair, such as annuloplasty rings, is a listed indication, and dental "
    "cleaning that manipulates the gums is a listed procedure. With no allergy and an oral route, a single dose of "
    "amoxicillin 30 to 60 minutes before is the standard regimen."],
   ["Not needed: the repair is old",
    "The listed adult conditions have no time limit; the 6-month window applies to CHILDREN after congenital heart "
    "repair with prosthetic material. His annuloplasty ring still qualifies.", "adjacent fact"],
   ["Not needed: cleaning is minor",
    "Dental cleaning is named among the procedures that need prophylaxis because it manipulates the gums. With his "
    "annuloplasty ring, he should get amoxicillin beforehand.", "common lay belief"],
   ["Give it after, if he bleeds",
    "Prophylaxis is a single dose 30 to 60 minutes BEFORE the procedure, decided by his condition and the procedure, "
    "not by bleeding afterward. He gets oral amoxicillin beforehand.", "reversed direction or value"]],
  (34, 35, 36, 42), "agent/regimen", "education"),

X(L, "comorbid", IE, A,
  "A 68-year-old woman with chronic kidney disease (creatinine 2.4 mg/dL, normal 0.6-1.2) has uncomplicated native "
  "mitral valve endocarditis from viridans streptococci and is responding quickly to therapy. A short combination "
  "course is being discussed. Which drug should be left out because of her kidney disease?",
  [["Gentamicin",
    "Correct. For viridans streptococci, penicillin G or ceftriaxone can be given with gentamicin as a 2-week regimen, "
    "but only for uncomplicated endocarditis with a rapid response and NO chronic kidney disease. Her kidney disease "
    "rules out the gentamicin-containing short course."],
   ["Ceftriaxone",
    "Ceftriaxone is a listed backbone for viridans streptococcal endocarditis and is not the drug her kidney disease "
    "rules out. The 2-week regimen's gentamicin is what requires the absence of chronic kidney disease.",
    "adjacent fact"],
   ["Penicillin G",
    "Penicillin G is a listed agent for viridans streptococci and is not the one excluded by kidney disease. Gentamicin "
    "is: its 2-week combination is reserved for patients without chronic kidney disease.", "adjacent fact"],
   ["Vancomycin",
    "Vancomycin is a listed alternative for viridans streptococci, not the drug named in the kidney-disease condition. "
    "The 2-week gentamicin regimen is the one limited to patients without chronic kidney disease.",
    "adjacent fact"]],
  (27,), "avoid", "avoid"),

X(L, "comorbid", IE, A,
  "A 72-year-old man with type 2 diabetes had a mechanical aortic valve placed 8 months ago. He has 5 days of fever to "
  "38.9 °C (102.0 °F) and a new regurgitant murmur. Three sets of blood cultures have just been drawn, and results are "
  "pending. Which empiric regimen fits?",
  [["Vancomycin, gentamicin, cefepime",
    "Correct. Empiric therapy, started only after blood cultures are drawn, covers staphylococci, streptococci and "
    "enterococci. For prosthetic valve endocarditis when the valve has been in place for 1 year or less, it is "
    "vancomycin plus gentamicin plus cefepime; his valve is 8 months old."],
   ["Vancomycin plus ceftriaxone",
    "Vancomycin plus ceftriaxone is the empiric regimen for native valve endocarditis, a subacute presentation, or a "
    "prosthetic valve in place MORE than 1 year. His valve is 8 months old, so he gets vancomycin, gentamicin and "
    "cefepime.", "ruled out by a stated finding"],
   ["Penicillin G plus gentamicin",
    "Penicillin G with gentamicin is a directed regimen for VIRIDANS STREPTOCOCCI once cultures identify them. Before "
    "results, an early prosthetic valve infection gets vancomycin, gentamicin and cefepime.",
    "wrong stage or severity"],
   ["Nafcillin plus gentamicin",
    "Nafcillin is directed therapy for methicillin-susceptible Staphylococcus aureus once it is identified, and it "
    "would miss resistant staphylococci. Empiric therapy for a valve under 1 year old is vancomycin, gentamicin and "
    "cefepime.", "wrong stage or severity"]],
  (17, 26, 27), "agent/regimen", "treatment"),

X(L, "comorbid", IE, A,
  "A 29-year-old woman who injects heroin and has hepatitis C has tricuspid valve endocarditis. Blood cultures grow "
  "methicillin-resistant Staphylococcus aureus. Which antibiotic fits?",
  [["Vancomycin",
    "Correct. Staphylococcus aureus causes most endocarditis in people who inject drugs, and 80 to 90% when the "
    "tricuspid valve is infected. For the methicillin-RESISTANT strain, the listed agents are vancomycin or "
    "daptomycin."],
   ["Nafcillin",
    "Nafcillin (or oxacillin) treats METHICILLIN-SUSCEPTIBLE Staphylococcus aureus. Her organism is "
    "methicillin-resistant, so vancomycin or daptomycin is used.", "ruled out by a stated finding"],
   ["Cefazolin",
    "Cefazolin is an option for methicillin-SUSCEPTIBLE Staphylococcus aureus. For her methicillin-resistant strain "
    "the agents are vancomycin or daptomycin.", "ruled out by a stated finding"],
   ["Penicillin G",
    "Penicillin G (with or without gentamicin) treats viridans streptococci, the classic subacute oral-flora organism. "
    "Her tricuspid infection grows methicillin-resistant Staphylococcus aureus, treated with vancomycin or daptomycin.",
    "competing diagnosis"]],
  (18, 27), "agent/regimen", "treatment"),

X(L, "comorbid", IE, A,
  "A 40-year-old woman who receives long-term intravenous nutrition through a central line has fever and a large "
  "vegetation on her native tricuspid valve. Blood cultures grow Candida, and antifungal therapy has been started. "
  "Which additional step is indicated?",
  [["Cardiothoracic surgery referral",
    "Correct. Fungal infection is a listed indication for surgery because it is difficult to cure with medications "
    "alone, and cardiothoracic surgery is consulted to evaluate surgery. Fungal endocarditis also carries a high risk of "
    "embolism to large peripheral arteries."],
   ["Heparin anticoagulation",
    "Anticoagulation is not beneficial in native valve infection, and her tricuspid valve is native. The added step "
    "for Candida endocarditis is a cardiothoracic surgery referral, since fungal infection rarely clears with drugs.",
    "common lay belief"],
   ["Adding gentamicin for synergy",
    "Gentamicin appears in the listed antibacterial regimens for viridans streptococci and prosthetic valve staphylococci, not in an antifungal one. Fungal endocarditis needs a surgical evaluation.", "confused mechanism or drug class"],
   ["Two weeks of oral antifungal",
    "Endocarditis therapy is prolonged and parenteral, and fungal infection is difficult to cure with medications "
    "alone. She needs a cardiothoracic surgery referral, not a short oral course.", "wrong stage or severity"]],
  (16, 26, 32, 33, 37), "referral", "referral"),
]
