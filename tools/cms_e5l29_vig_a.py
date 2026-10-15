# -*- coding: utf-8 -*-
"""Lecture 29 vignette pool A -- Arrhythmias I: sinus arrhythmia, sinus bradycardia, sinus
tachycardia and sick sinus syndrome, with the adult/elderly care strategies.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.

Patient vignettes with a varied lead-in (the lead-in decides the answer). Her stated exam shape is
"you see this EKG, what would you do? or what is a risk factor?", so the rhythm is described in
words and most lead-ins ask for management. Slides only; the recording set emphasis (atropine first
for unstable bradycardia; tachy-brady usually atrial fibrillation). Scope caps live in
cms_e5l29_scope.py.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e5l29_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


SAR = "Sinus arrhythmia"
SBR = "Sinus bradycardia"
STA = "Sinus tachycardia"
SSS = "Sick sinus syndrome"

QUESTIONS = [

# ---------------------------------------------------------------- sinus arrhythmia
V(SAR, IO_A,
  "A 19-year-old swimmer has an electrocardiogram before a sports physical. She has no symptoms. The rate is 72, with a normal P wave before every narrow QRS, but the beats come closer together as she breathes in and spread apart as she breathes out. Which is the most likely diagnosis?",
  [["Sinus arrhythmia",
    "Correct. A normal P wave before every narrow QRS at 60 to 100, with the rate rising on inspiration and falling on expiration, is sinus arrhythmia: a normal, physiologic rhythm that is irregular with a pattern."],
   ["Sick sinus syndrome",
    "Sick sinus syndrome produces pauses, sinus arrest or tachy-brady swings in a diseased node, usually with symptoms; a breathing-linked variation in a healthy swimmer is sinus arrhythmia.", "competing diagnosis"],
   ["Multifocal atrial tachycardia",
    "Multifocal atrial tachycardia is a fast, irregular rhythm with at least three P-wave shapes in acutely ill lung or heart patients; her single P-wave shape at 72 is sinus.", "competing diagnosis"],
   ["Atrial fibrillation",
    "Atrial fibrillation is irregularly irregular with no P waves; she has a normal P wave before every beat and a regular pattern tied to breathing.", "competing diagnosis"]],
  C(9), "differential", "diagnosis"),

V(SAR, IO_A,
  "A 24-year-old man is told his electrocardiogram shows a normal P wave before each narrow QRS at 68 beats per minute, with the rate rising as he breathes in and falling as he breathes out. He worries that he has heart disease. Which counseling is most accurate?",
  [["A normal variant; no treatment",
    "Correct. A sinus rate that speeds with inspiration and slows with expiration, with normal P waves and a narrow QRS, is sinus arrhythmia, a normal physiologic variant that needs no treatment."],
   ["He needs a pacemaker workup",
    "Pacemakers are for symptomatic bradycardia, sick sinus syndrome or high-grade block; a breathing-linked sinus variation is normal and needs nothing.", "wrong stage or severity"],
   ["He should stop exercising",
    "Exercise restriction has no place here; sinus arrhythmia is a normal physiologic response to breathing.", "common lay belief"],
   ["He needs an anticoagulant",
    "Anticoagulation prevents stroke in atrial fibrillation and flutter; sinus arrhythmia carries no clot risk and needs no treatment.", "confused mechanism or drug class"]],
  C(9), "education", "education"),

# ---------------------------------------------------------------- sinus bradycardia
V(SBR, IO_A,
  "A 26-year-old marathon runner has a resting heart rate of 48 at a preparticipation physical. He denies dizziness, fainting or chest pain. The electrocardiogram shows a regular rhythm with a normal P wave before every narrow QRS and a PR interval of 0.16 seconds. Which is the most appropriate next step?",
  [["Reassurance; no treatment",
    "Correct. Sinus bradycardia is seen in healthy people as an adaptive response, particularly well-conditioned athletes, and an asymptomatic sinus bradycardia is not treated."],
   ["Atropine",
    "Atropine is first line only for acute, symptomatic, hemodynamically unstable bradycardia; a well, conditioned runner needs no drug.", "wrong stage or severity"],
   ["Permanent pacemaker",
    "A permanent pacemaker is for chronic, symptomatic bradycardia; this athlete's adaptive bradycardia causes no symptoms.", "wrong stage or severity"],
   ["Stop running",
    "Training explains the slow rate and is not harmful here; asymptomatic sinus bradycardia in an athlete needs only reassurance.", "common lay belief"]],
  C(13), "first-line", "next step"),

V(SBR, IO_A,
  "A 68-year-old man is brought in confused, with a blood pressure of 76/40. The monitor shows a slow, regular rhythm at 36 with a normal P wave before every narrow QRS. Which is the first-line treatment?",
  [["Atropine",
    "Correct. Acute, symptomatic, hemodynamically unstable sinus bradycardia is treated first with atropine; if it fails, a temporary pacemaker follows, and chronic symptomatic disease gets a permanent one."],
   ["Adenosine",
    "Adenosine blocks the atrioventricular node to stop supraventricular tachycardia; in a slow, unstable rhythm it would deepen the bradycardia.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is a timed shock for an unstable tachycardia with a pulse; unstable bradycardia is treated with atropine first.", "confused mechanism or drug class"],
   ["Permanent pacemaker",
    "A permanent pacemaker is definitive care for chronic symptomatic bradycardia; the acutely unstable patient first gets atropine, then temporary pacing.", "wrong stage or severity"]],
  C(13), "first-line", "treatment"),

V(SBR, IO_A,
  "A 58-year-old woman has a slow sinus rhythm at 38 six hours after an inferior myocardial infarction. She feels faint and her blood pressure is 80/50. Each narrow QRS has a normal P wave before it. Which drug should be given first?",
  [["Atropine",
    "Correct. Acute, symptomatic, hemodynamically unstable sinus bradycardia, here from an infarction affecting the conduction tissue, is treated first with atropine, then a temporary pacemaker."],
   ["Metoprolol",
    "Metoprolol is a beta blocker, a listed cause of sinus bradycardia; it would slow her further.", "confused mechanism or drug class"],
   ["Diltiazem",
    "Diltiazem is a nondihydropyridine calcium channel blocker, another drug cause of bradycardia; it would worsen her hypotension and slow rate.", "confused mechanism or drug class"],
   ["Adenosine",
    "Adenosine stops supraventricular tachycardia by blocking the atrioventricular node; it has no place in an unstable bradycardia.", "confused mechanism or drug class"]],
  C(13), "agent/regimen", "treatment"),

V(SBR, IO_A,
  "A 71-year-old man with a slow sinus rhythm at 34 is hypotensive and drowsy. Two doses of atropine have not changed his rate or blood pressure. Which is the next step?",
  [["Temporary pacemaker",
    "Correct. When atropine fails in acute, symptomatic, unstable bradycardia, the next step is a temporary pacemaker; a permanent pacemaker follows if the cause will not resolve."],
   ["Adenosine",
    "Adenosine blocks the atrioventricular node and would slow him further; after failed atropine, a temporary pacemaker is used.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "A synchronized shock is for unstable fast rhythms; a slow rhythm unresponsive to atropine needs temporary pacing.", "confused mechanism or drug class"],
   ["Oral metoprolol",
    "A beta blocker is a cause of bradycardia, not a rescue for it; the next step after atropine is a temporary pacemaker.", "confused mechanism or drug class"]],
  C(13), "escalation", "next step"),

V(SBR, IO_POP,
  "A 74-year-old woman has months of fatigue and two near-faints. Repeated electrocardiograms show sinus bradycardia at 42, and her symptoms match the slow rate. She takes no rate-slowing drugs and her thyroid tests are normal. Which treatment is indicated?",
  [["Permanent pacemaker",
    "Correct. Chronic, symptomatic sinus bradycardia with no reversible cause, as here in an older adult, is managed with a permanent pacemaker."],
   ["Atropine as needed",
    "Atropine is a short-acting rescue for acute, unstable bradycardia, not long-term therapy for chronic symptomatic disease.", "wrong stage or severity"],
   ["Catheter ablation",
    "Ablation destroys tissue causing a tachycardia; it cannot speed a slow sinus node.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Cardioversion resets fast rhythms; chronic symptomatic sinus bradycardia needs a permanent pacemaker.", "confused mechanism or drug class"]],
  C(13), "escalation", "treatment"),

V(SBR, IO_A,
  "A 62-year-old man started a new blood pressure medication two weeks ago. He now feels tired, and his pulse is 46 and regular, with a normal P wave before every narrow QRS. Thyroid tests are normal. Which medication is the most likely cause?",
  [["Metoprolol",
    "Correct. Beta blockers such as metoprolol, nondihydropyridine calcium channel blockers and digoxin are the drug causes of sinus bradycardia; a new one two weeks ago is the likely culprit."],
   ["Amlodipine",
    "Amlodipine is a dihydropyridine calcium channel blocker; the calcium channel blockers that cause bradycardia are the nondihydropyridines, verapamil and diltiazem.", "confused mechanism or drug class"],
   ["Lisinopril",
    "Lisinopril, an angiotensin-converting enzyme inhibitor, is not among the drug causes of sinus bradycardia; beta blockers are.", "confused mechanism or drug class"],
   ["Hydrochlorothiazide",
    "A thiazide diuretic does not slow the sinus node; the listed bradycardic drugs are beta blockers, nondihydropyridine calcium channel blockers and digoxin.", "confused mechanism or drug class"]],
  C(13), "etiology", "diagnosis"),

V(SBR, IO_A,
  "A 58-year-old woman has new fatigue, weight gain, cold intolerance and constipation. Her pulse is 50 and regular, with a normal P wave before each narrow QRS. She takes no medications. Which test is most useful next?",
  [["Thyroid function tests",
    "Correct. Hypothyroidism is a listed cause of sinus bradycardia, and her weight gain, cold intolerance and constipation point to it, so thyroid testing comes next."],
   ["Serum digoxin level",
    "Digoxin causes bradycardia, but she takes no medications; her symptoms point to hypothyroidism instead.", "ruled out by a stated finding"],
   ["Electrophysiology study",
    "An invasive conduction study is not the first step when the history points to a reversible cause such as hypothyroidism.", "wrong stage or severity"],
   ["Ambulatory monitor for pauses",
    "Monitoring for pauses suits suspected sick sinus syndrome; her symptoms suggest hypothyroidism, checked first with thyroid tests.", "competing diagnosis"]],
  C(13), "initial test", "test"),

V(SBR, IO_POP,
  "A 72-year-old woman with symptomatic sinus bradycardia at 45 also has hypertension that needs a new medication. Which antihypertensive should be avoided?",
  [["Verapamil",
    "Correct. Verapamil is a nondihydropyridine calcium channel blocker, and these drugs, like beta blockers and digoxin, cause sinus bradycardia; it would slow her further."],
   ["Lisinopril",
    "Lisinopril does not slow the sinus node and is not among the listed causes of bradycardia, so it is not the drug to avoid.", "confused mechanism or drug class"],
   ["Chlorthalidone",
    "A thiazide-type diuretic does not cause sinus bradycardia; the drugs to avoid are beta blockers, nondihydropyridine calcium channel blockers and digoxin.", "confused mechanism or drug class"],
   ["Losartan",
    "Losartan, an angiotensin receptor blocker, does not slow the heart; verapamil does and should be avoided.", "confused mechanism or drug class"]],
  C(13), "avoid", "avoid"),

# ---------------------------------------------------------------- sinus tachycardia
V(STA, IO_A,
  "A 34-year-old woman is brought in after a car crash with a heart rate of 128 and a blood pressure of 88/56. The rhythm is regular with a normal P wave before every narrow QRS. Bedside ultrasound shows free fluid in the abdomen. Which is the most appropriate approach to her heart rate?",
  [["Treat the blood loss",
    "Correct. This is appropriate sinus tachycardia from hypovolemia, a pathologic cause; management of appropriate sinus tachycardia is treating the underlying cause."],
   ["Adenosine",
    "Adenosine is for reentrant supraventricular tachycardia; a sinus tachycardia compensating for blood loss settles when the cause is treated.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Cardioversion cannot fix a compensatory sinus rhythm and would not restore her volume; the cause must be treated.", "confused mechanism or drug class"],
   ["Intravenous metoprolol",
    "Slowing a compensatory tachycardia in a hypovolemic patient would remove her compensation; the bleeding is what needs treatment.", "confused mechanism or drug class"]],
  C(17), "first-line", "next step"),

V(STA, IO_A,
  "A 29-year-old woman has had a resting heart rate of 105 to 115 for a year. Thyroid tests, a blood count, a drug screen and an echocardiogram are normal, and she takes no medications or stimulants. Her electrocardiogram shows a normal P wave before every narrow QRS. Which is the most likely diagnosis?",
  [["Inappropriate sinus tachycardia",
    "Correct. A sinus tachycardia that remains unexplained after secondary causes are excluded is inappropriate sinus tachycardia, a diagnosis of exclusion."],
   ["Focal atrial tachycardia",
    "Focal atrial tachycardia has an abnormally shaped P wave from an ectopic focus and starts abruptly; her P waves are normal sinus P waves.", "competing diagnosis"],
   ["Atrioventricular nodal reentry",
    "Nodal reentry is a paroxysmal, regular narrow tachycardia with hidden P waves; hers is a persistent sinus rhythm with visible normal P waves.", "competing diagnosis"],
   ["Atrial flutter with 2:1 block",
    "Flutter shows sawtooth waves at an atrial rate of 250 or more; she has a normal P wave before each QRS at a rate near 110.", "competing diagnosis"]],
  C(16), "differential", "diagnosis"),

V(STA, IO_A,
  "A 31-year-old woman has inappropriate sinus tachycardia at about 110 after a full workup excluded other causes. Her only symptom is awareness of her heartbeat, and she asks whether she needs medication. Which response is most accurate?",
  [["Usually left untreated; benign",
    "Correct. Inappropriate sinus tachycardia is generally left untreated: patients tolerate the symptoms better than the treatment, beta blockers are poorly tolerated, and the prognosis is usually benign."],
   ["She needs a lifelong beta blocker",
    "Beta blockers are not well tolerated in inappropriate sinus tachycardia, which is why it is usually left untreated.", "common lay belief"],
   ["Cardioversion will cure it",
    "Cardioversion resets reentrant or fibrillatory rhythms; inappropriate sinus tachycardia is a sinus rhythm and is usually left untreated.", "confused mechanism or drug class"],
   ["She needs anticoagulation",
    "Anticoagulation prevents stroke in atrial fibrillation and flutter; a sinus tachycardia carries no such need.", "confused mechanism or drug class"]],
  C(17), "education", "education"),

V(STA, IO_A,
  "A 63-year-old man ran out of his metoprolol four days ago. He feels his heart racing, and his pulse is 118 and regular, with a normal P wave before every narrow QRS. He has no fever and is not bleeding. Which is the most likely cause of his tachycardia?",
  [["Beta blocker withdrawal",
    "Correct. Abrupt withdrawal of a beta blocker (or a nondihydropyridine calcium channel blocker) is a listed cause of sinus tachycardia, which fits stopping metoprolol four days ago."],
   ["Hypothyroidism",
    "Hypothyroidism slows the sinus node and causes bradycardia; it does not explain a racing heart after stopping a beta blocker.", "reversed direction or value"],
   ["Raised intracranial pressure",
    "Raised intracranial pressure is a listed cause of sinus bradycardia, not tachycardia; his fast rate follows beta blocker withdrawal.", "adjacent fact"],
   ["Increased vagal tone",
    "High vagal tone slows the heart, as in athletes with bradycardia; a fast sinus rate after stopping metoprolol is withdrawal.", "reversed direction or value"]],
  C(16), "etiology", "diagnosis"),

V(STA, IO_A,
  "A 45-year-old man has a heart rate of 122 with a normal P wave before every narrow QRS. His temperature is 39.2°C and he has a productive cough and crackles at the right base. He is alert with a blood pressure of 126/78. Which is the best treatment for his heart rate?",
  [["Treat the infection and fever",
    "Correct. A sinus tachycardia from fever and infection is an appropriate response to a pathologic process, and appropriate sinus tachycardia is managed by treating the underlying cause."],
   ["Adenosine",
    "Adenosine stops reentrant supraventricular tachycardia through the atrioventricular node; it has no role in a sinus tachycardia from fever.", "confused mechanism or drug class"],
   ["Vagal maneuver",
    "Vagal maneuvers are first line for reentrant supraventricular tachycardia; a fever-driven sinus tachycardia settles when the infection is treated.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Cardioversion is for unstable reentrant or fibrillatory rhythms; this stable sinus tachycardia needs its cause treated.", "confused mechanism or drug class"]],
  C(17), "first-line", "treatment"),

# ---------------------------------------------------------------- sick sinus syndrome
V(SSS, IO_A,
  "A 76-year-old woman has episodes of lightheadedness and one faint. A 24-hour ambulatory monitor shows runs of a fast, irregular rhythm that alternate with slow rates and long pauses. Which fast rhythm is most likely on her monitor?",
  [["Atrial fibrillation",
    "Correct. Fast rhythms alternating with bradycardia and offset pauses are tachy-brady syndrome, a form of sick sinus syndrome in which the tachyarrhythmia is most commonly atrial fibrillation."],
   ["Ventricular fibrillation",
    "Ventricular fibrillation is a pulseless arrest rhythm, not a recurring run she survives; the usual fast rhythm of tachy-brady syndrome is atrial fibrillation.", "competing diagnosis"],
   ["Sinus tachycardia",
    "In tachy-brady syndrome the fast rhythm comes from outside the failing sinus node, most commonly atrial fibrillation.", "competing diagnosis"],
   ["Atrioventricular nodal reentry",
    "Nodal reentry is a regular narrow tachycardia, usually in younger women without heart disease; it is not the fast phase of tachy-brady syndrome.", "competing diagnosis"]],
  C(18), "manifestation", "diagnosis"),

V(SSS, IO_A,
  "An 81-year-old man has known tachy-brady syndrome (a fast rhythm alternating with slow rates and pauses) and asks which fast rhythm is behind his palpitations. An ambulatory monitor is arranged. Which rhythm is it most likely to record during the fast episodes?",
  [["Atrial fibrillation",
    "Correct. In tachy-brady syndrome the tachyarrhythmia that alternates with bradycardia or pauses is most commonly atrial fibrillation."],
   ["Atrial flutter",
    "Flutter is an organized atrial circuit with sawtooth waves; it is not the usual fast rhythm of tachy-brady syndrome.", "competing diagnosis"],
   ["Ventricular tachycardia",
    "Ventricular tachycardia can occur in some patients, who then need a defibrillator with the pacemaker, but atrial fibrillation is the most common.", "adjacent fact"],
   ["Junctional rhythm",
    "A junctional rhythm is slow and regular, usually 40 to 60, not the fast phase of tachy-brady syndrome.", "competing diagnosis"]],
  C(18), "test finding", "test"),

V(SSS, IO_A,
  "A 79-year-old man has tachy-brady syndrome (a fast rhythm alternating with slow rates and pauses) on monitoring, and he faints during the pauses. Thyroid tests and electrolytes are normal and he takes no rate-slowing drugs. Which treatment is most appropriate?",
  [["Permanent pacemaker",
    "Correct. When symptoms correlate with bradycardia in sick sinus syndrome a permanent pacemaker is placed, and tachy-brady syndrome often needs one."],
   ["Atropine as needed",
    "Atropine is a short-acting rescue for acute unstable bradycardia, not long-term protection against pauses.", "wrong stage or severity"],
   ["Catheter ablation alone",
    "Ablation does nothing for the failing sinus node that causes his pauses; he needs a permanent pacemaker.", "confused mechanism or drug class"],
   ["Observation alone",
    "Observation is appropriate only when symptoms do not correlate with the bradycardia; his fainting during pauses needs a pacemaker.", "wrong stage or severity"]],
  C(22), "escalation", "treatment"),

V(SSS, IO_A,
  "A 72-year-old woman has sinus pauses of up to 2 seconds at night on an ambulatory monitor. Her occasional dizziness happens only when she stands up quickly and never during the pauses. Which is the most appropriate next step?",
  [["Observation",
    "Correct. In sick sinus syndrome, management confirms whether symptoms correlate with the bradycardia; when they do not, observation is appropriate."],
   ["Permanent pacemaker",
    "A permanent pacemaker is for symptomatic bradycardia; her dizziness does not match her pauses, so observation is appropriate.", "wrong stage or severity"],
   ["Atropine",
    "Atropine is for acute, symptomatic, unstable bradycardia; she is neither unstable nor symptomatic during the pauses.", "wrong stage or severity"],
   ["Catheter ablation",
    "Ablation treats tachycardias from a focus or pathway; it has no role in brief, asymptomatic sinus pauses.", "confused mechanism or drug class"]],
  C(22), "first-line", "next step"),

V(SSS, IO_A,
  "A 70-year-old man with sick sinus syndrome has pauses on monitoring that alternate with runs of ventricular tachycardia. Which device is indicated?",
  [["Pacemaker with a defibrillator",
    "Correct. Tachy-brady syndrome often needs a permanent pacemaker, and when the tachyarrhythmia is ventricular tachycardia the patient needs a pacemaker with an implantable cardioverter defibrillator."],
   ["Pacemaker alone",
    "A pacemaker alone protects against pauses but cannot shock ventricular tachycardia; a defibrillator must be added.", "wrong stage or severity"],
   ["No device; observe",
    "Observation suits pauses that cause no symptoms; ventricular tachycardia alternating with pauses needs a pacemaker with a defibrillator.", "wrong stage or severity"],
   ["Ablation alone",
    "Ablation does not fix the failing sinus node behind the pauses; the device answer is a pacemaker with a defibrillator.", "confused mechanism or drug class"]],
  C(22), "escalation", "treatment"),

V(SSS, IO_A,
  "A 77-year-old man had cardiac surgery last year. A rhythm strip shows normal sinus beats, then a sudden pause with no P wave, after which narrow beats at 45 appear with no visible P waves. Which is the most likely diagnosis?",
  [["Sinus arrest",
    "Correct. In sinus arrest the sinus node does not generate an impulse, leading to a junctional rhythm (narrow beats at 40 to 60 with no visible P waves); injury to the node from cardiac surgery is a listed cause."],
   ["Sinus bradycardia",
    "Sinus bradycardia is a regular rhythm under 60 with a P wave before every QRS, not a sudden pause followed by narrow beats with no P waves.", "competing diagnosis"],
   ["Sinus arrhythmia",
    "Sinus arrhythmia is a normal breathing-linked variation with a P wave before every beat, never a pause followed by junctional beats.", "competing diagnosis"],
   ["Atrial flutter",
    "Atrial flutter shows rapid sawtooth waves at 250 or more, not a pause followed by slow narrow beats without P waves.", "competing diagnosis"]],
  C(18), "differential", "diagnosis"),

V(SSS, IO_POP,
  "A 73-year-old man has new pauses and slow rates on an ambulatory monitor. He started verapamil and digoxin last month for palpitations. He feels mildly lightheaded but is otherwise well. Which is the most appropriate first step?",
  [["Stop the rate-slowing drugs",
    "Correct. Medications (beta blockers, nondihydropyridine calcium channel blockers and digoxin) are listed causes of sick sinus syndrome, and management starts by treating the underlying cause."],
   ["Permanent pacemaker now",
    "A pacemaker may be needed if symptomatic bradycardia persists, but a reversible drug cause is addressed first.", "wrong stage or severity"],
   ["Catheter ablation",
    "Ablation targets a tachycardia focus or pathway; his slow rates and pauses come from rate-slowing drugs.", "confused mechanism or drug class"],
   ["Atropine tablets",
    "Atropine is an acute intravenous rescue for unstable bradycardia, not a long-term oral therapy; stopping the culprit drugs comes first.", "confused mechanism or drug class"]],
  C(22), "first-line", "next step"),

]
