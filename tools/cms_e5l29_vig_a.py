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
    "Correct. A rate of 72 with a normal P wave before every narrow QRS, beats closer together on inspiration and farther apart on expiration, is sinus arrhythmia. It is a normal, physiologic rhythm at 60 to 100 that is irregular with a pattern, which fits a healthy swimmer with no symptoms."],
   ["Sick sinus syndrome",
    "Sick sinus syndrome is an irregular rhythm with variable P waves, from sinus exit block, sinus arrest or tachy-brady swings with pauses. She has a uniform P wave before every beat and a variation tied to breathing, with no pauses. Tell: a breathing-linked pattern is physiologic; pauses and fast-slow swings suggest a diseased node.", "competing diagnosis"],
   ["Multifocal atrial tachycardia",
    "Multifocal atrial tachycardia is a fast rhythm, over 100, with at least three different P-wave shapes in one lead, usually in acutely ill patients. She has one normal P-wave shape at 72. Tell: multifocal needs both tachycardia and changing P waves, and she has neither.", "competing diagnosis"],
   ["Atrial fibrillation",
    "Atrial fibrillation is irregularly irregular with absent P waves. She has a normal P wave before every QRS, and her irregularity follows her breathing. Tell: patterned irregularity with P waves is sinus arrhythmia; patternless irregularity without P waves is fibrillation.", "competing diagnosis"]],
  C(9), "differential", "diagnosis"),

V(SAR, IO_A,
  "A 24-year-old man is told his electrocardiogram shows a normal P wave before each narrow QRS at 68 beats per minute, with the rate rising as he breathes in and falling as he breathes out. He worries that he has heart disease. Which counseling is most accurate?",
  [["A normal variant; no treatment",
    "Correct. A normal P wave before each narrow QRS at 68, with the rate rising on inspiration and falling on expiration, is sinus arrhythmia. It is a normal, physiologic rhythm, irregular with a pattern at 60 to 100, so he can be reassured that it is not heart disease and needs no treatment."],
   ["He needs a pacemaker workup",
    "A permanent pacemaker is for chronic symptomatic bradycardia or sick sinus syndrome with correlated symptoms. His rate is 68 with a breathing-linked variation and normal P waves, a normal finding. Tell: a patterned variation at 60 to 100 is physiologic, not a pacemaker problem.", "wrong stage or severity"],
   ["He should stop exercising",
    "Stopping exercise has no basis here; sinus arrhythmia is a normal, physiologic rhythm tied to breathing. Tell: the rate rising on inspiration and falling on expiration is expected, so reassurance, not restriction, is the counseling for this healthy young man.", "common lay belief"],
   ["He needs an anticoagulant",
    "Anticoagulation is part of managing atrial fibrillation and atrial flutter, guided by stroke risk. Sinus arrhythmia is a normal, physiologic rhythm with a P wave before every beat. Tell: a normal sinus P wave before each QRS means no atrial fibrillation and no anticoagulation question.", "confused mechanism or drug class"]],
  C(9), "education", "education"),

# ---------------------------------------------------------------- sinus bradycardia
V(SBR, IO_A,
  "A 26-year-old marathon runner has a resting heart rate of 48 at a preparticipation physical. He denies dizziness, fainting or chest pain. The electrocardiogram shows a regular rhythm with a normal P wave before every narrow QRS and a PR interval of 0.16 seconds. Which is the most appropriate next step?",
  [["Reassurance; no treatment",
    "Correct. A regular rhythm at 48 with a normal P wave before every narrow QRS and a PR of 0.16 seconds is sinus bradycardia. In a well-conditioned marathon runner with no dizziness, fainting or chest pain it is an adaptive response, and asymptomatic sinus bradycardia is not treated."],
   ["Atropine",
    "Atropine is first line for acute, symptomatic, hemodynamically unstable bradycardia. This runner is well, with no dizziness, fainting or chest pain. Tell: atropine needs symptoms and instability; an asymptomatic athlete with sinus bradycardia needs neither a drug nor a device.", "wrong stage or severity"],
   ["Permanent pacemaker",
    "A permanent pacemaker is for chronic, symptomatic bradycardia. This runner denies dizziness, fainting and chest pain, and his slow rate is an adaptive response to conditioning. Tell: a pacemaker needs symptoms that track the slow rate, and none are present here.", "wrong stage or severity"],
   ["Stop running",
    "Sinus bradycardia is seen in healthy people as an adaptive response, particularly in well-conditioned athletes. His training is the reason for the slow rate, and with no symptoms nothing needs treating or stopping. Tell: an athlete's asymptomatic sinus bradycardia gets reassurance only, not activity limits.", "common lay belief"]],
  C(13), "first-line", "next step"),

V(SBR, IO_A,
  "A 68-year-old man is brought in confused, with a blood pressure of 76/40. The monitor shows a slow, regular rhythm at 36 with a normal P wave before every narrow QRS. Which is the first-line treatment?",
  [["Atropine",
    "Correct. A slow, regular rhythm at 36 with a normal P wave before every narrow QRS is sinus bradycardia, and confusion with a blood pressure of 76/40 make it acute, symptomatic and hemodynamically unstable. Atropine is first line; if it fails, a temporary pacemaker follows."],
   ["Adenosine",
    "Adenosine is used in stable supraventricular tachycardia after a vagal maneuver, to convert the rhythm or slow it enough to reveal P waves. Slowing a rhythm already at 36 in a confused, hypotensive man is the opposite of the goal. Tell: adenosine is for fast narrow rhythms; atropine is for unstable slow ones.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion, a timed shock at decreased voltage, treats hemodynamically unstable tachycardias such as supraventricular tachycardia or atrial fibrillation. His rhythm is slow at 36, the opposite problem. Tell: unstable and fast means a synchronized shock; unstable and slow means atropine.", "confused mechanism or drug class"],
   ["Permanent pacemaker",
    "A permanent pacemaker is for chronic, symptomatic bradycardia, not the first step in an acute, unstable episode. The acute sequence is atropine, then a temporary pacemaker if atropine fails. Tell: acute and unstable means atropine first; a permanent device comes later if the problem is chronic.", "wrong stage or severity"]],
  C(13), "first-line", "treatment"),

V(SBR, IO_A,
  "A 58-year-old woman has a slow sinus rhythm at 38 six hours after an inferior myocardial infarction. She feels faint and her blood pressure is 80/50. Each narrow QRS has a normal P wave before it. Which drug should be given first?",
  [["Atropine",
    "Correct. A sinus rhythm at 38 with a normal P wave before each narrow QRS, faintness and a blood pressure of 80/50 is acute, symptomatic, hemodynamically unstable sinus bradycardia; sinus node ischemia is a listed cause, fitting the infarction. Atropine is first line, followed by a temporary pacemaker if it fails."],
   ["Metoprolol",
    "Metoprolol is a beta blocker, and beta blockers are a listed cause of sinus bradycardia, so it would slow her further at a rate of 38. Beta blockers are used for fast rhythms, such as rate control in stable atrial flutter. Tell: a hypotensive, faint patient with a slow sinus rate needs atropine, not a rate-slowing drug.", "confused mechanism or drug class"],
   ["Diltiazem",
    "Diltiazem is a nondihydropyridine calcium channel blocker, a class listed with beta blockers and digoxin as a drug cause of sinus bradycardia. Giving it at a rate of 38 with a blood pressure of 80/50 would deepen the problem. Tell: drugs that cause bradycardia never rescue it; atropine does.", "confused mechanism or drug class"],
   ["Adenosine",
    "Adenosine is used in stable supraventricular tachycardia after a vagal maneuver, to convert the rhythm or slow it enough to reveal P waves. Slowing a sinus rhythm already at 38 is the opposite of what she needs. Tell: adenosine is for a fast narrow rhythm; unstable sinus bradycardia gets atropine.", "confused mechanism or drug class"]],
  C(13), "agent/regimen", "treatment"),

V(SBR, IO_A,
  "A 71-year-old man with a slow sinus rhythm at 34 is hypotensive and drowsy. Two doses of atropine have not changed his rate or blood pressure. Which is the next step?",
  [["Temporary pacemaker",
    "Correct. A sinus rhythm at 34 with hypotension and drowsiness is acute, symptomatic, hemodynamically unstable bradycardia, and atropine, the first-line drug, has failed after two doses. The next step is a temporary pacemaker; a permanent pacemaker is for chronic symptomatic bradycardia."],
   ["Adenosine",
    "Adenosine is used in stable supraventricular tachycardia after a vagal maneuver, to convert the rhythm or slow it enough to reveal P waves. Slowing a heart already at 34 is the opposite of the goal. Tell: after failed atropine in unstable bradycardia, use a temporary pacemaker.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion, a timed shock at decreased voltage, treats unstable tachycardias such as supraventricular tachycardia or atrial fibrillation. His rhythm is slow at 34, the opposite problem. Tell: unstable and slow after atropine means a temporary pacemaker.", "confused mechanism or drug class"],
   ["Oral metoprolol",
    "Metoprolol is a beta blocker, and beta blockers are a listed cause of sinus bradycardia, so it would slow him further. Tell: a drug that causes bradycardia is never the rescue; the sequence for unstable bradycardia is atropine, then a temporary pacemaker.", "confused mechanism or drug class"]],
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
    "Correct. A regular rate of 46 with a normal P wave before every narrow QRS is sinus bradycardia, and with normal thyroid tests the likely cause is a drug. Beta blockers such as metoprolol, nondihydropyridine calcium channel blockers and digoxin are its listed drug causes, and metoprolol is the new blood pressure medication on that list."],
   ["Amlodipine",
    "Only the nondihydropyridine calcium channel blockers are on the slow list for sinus bradycardia, with beta blockers and digoxin, and amlodipine is a dihydropyridine. A new slow sinus rhythm after a blood pressure drug therefore points to metoprolol. Tell: the calcium channel blocker qualifier matters, and dihydropyridines are not listed.", "confused mechanism or drug class"],
   ["Lisinopril",
    "Lisinopril is not among the listed drug causes of sinus bradycardia, which are beta blockers, nondihydropyridine calcium channel blockers and digoxin. A new slow sinus rhythm after starting a blood pressure drug points to the beta blocker. Tell: match the drug to the slow list, and metoprolol is on it.", "confused mechanism or drug class"],
   ["Hydrochlorothiazide",
    "Hydrochlorothiazide is not among the listed drug causes of sinus bradycardia. Those are beta blockers, nondihydropyridine calcium channel blockers and digoxin. Tell: of the blood pressure drugs offered, only the beta blocker belongs to that group.", "confused mechanism or drug class"]],
  C(13), "etiology", "diagnosis"),

V(SBR, IO_A,
  "A 58-year-old woman has new fatigue, weight gain, cold intolerance and constipation. Her pulse is 50 and regular, with a normal P wave before each narrow QRS. She takes no medications. Which test is most useful next?",
  [["Thyroid function tests",
    "Correct. A regular rate of 50 with a normal P wave before each narrow QRS is sinus bradycardia, and with no medications the drug causes are excluded. Hypothyroidism is a listed cause, and her fatigue, weight gain, cold intolerance and constipation point to it, so thyroid testing comes next."],
   ["Serum digoxin level",
    "Digoxin is a listed drug cause of sinus bradycardia, but she takes no medications, so a level would not help. Her fatigue, weight gain, cold intolerance and constipation point instead to hypothyroidism, another listed cause. Tell: no drug exposure rules out the drug causes.", "ruled out by a stated finding"],
   ["Electrophysiology study",
    "An electrophysiology study is not among the listed steps for sinus bradycardia. Her symptoms point to a listed, treatable cause, hypothyroidism, which is checked with thyroid tests. Tell: look for the underlying cause first when the history already suggests one.", "wrong stage or severity"],
   ["Ambulatory monitor for pauses",
    "Ambulatory monitoring is used in suspected sick sinus syndrome to see whether symptoms correlate with episodes of bradycardia. Her rhythm is a steady sinus bradycardia, and her symptoms suggest hypothyroidism, a listed cause checked with thyroid tests. Tell: weight gain and cold intolerance point to the thyroid, not to pauses.", "competing diagnosis"]],
  C(13), "initial test", "test"),

V(SBR, IO_POP,
  "A 72-year-old woman with symptomatic sinus bradycardia at 45 also has hypertension that needs a new medication. Which antihypertensive should be avoided?",
  [["Verapamil",
    "Correct. She already has symptomatic sinus bradycardia at 45, and nondihydropyridine calcium channel blockers such as verapamil are listed, with beta blockers and digoxin, as drug causes of sinus bradycardia. Adding verapamil would slow her further, so it should be avoided."],
   ["Lisinopril",
    "Lisinopril is not among the listed drug causes of sinus bradycardia, which are beta blockers, nondihydropyridine calcium channel blockers and digoxin. It is not the antihypertensive to avoid here. Tell: in a patient with sinus bradycardia, avoid the drugs on the slow list.", "confused mechanism or drug class"],
   ["Chlorthalidone",
    "Chlorthalidone is not among the listed drug causes of sinus bradycardia. The drugs to avoid in symptomatic sinus bradycardia are beta blockers, nondihydropyridine calcium channel blockers and digoxin. Tell: only the drug on the slow list needs avoiding, and that is verapamil.", "confused mechanism or drug class"],
   ["Losartan",
    "Losartan is not among the listed drug causes of sinus bradycardia. Verapamil, a nondihydropyridine calcium channel blocker, is on that list with beta blockers and digoxin. Tell: the one option here that slows the sinus node is verapamil.", "confused mechanism or drug class"]],
  C(13), "avoid", "avoid"),

# ---------------------------------------------------------------- sinus tachycardia
V(STA, IO_A,
  "A 34-year-old woman is brought in after a car crash with a heart rate of 128 and a blood pressure of 88/56. The rhythm is regular with a normal P wave before every narrow QRS. Bedside ultrasound shows free fluid in the abdomen. Which is the most appropriate approach to her heart rate?",
  [["Treat the blood loss",
    "Correct. This is appropriate sinus tachycardia from hypovolemia, a pathologic cause; management of appropriate sinus tachycardia is treating the underlying cause."],
   ["Adenosine",
    "Adenosine is used in stable supraventricular tachycardia after a vagal maneuver, to convert the rhythm or slow it enough to see P waves. Her P waves are already visible before every QRS, and her sinus rate is a response to blood loss. Tell: a normal P wave before each QRS plus an obvious cause means sinus tachycardia, so treat the cause.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is for hemodynamically unstable tachyarrhythmias such as supraventricular tachycardia, atrial flutter or atrial fibrillation. Her rhythm is sinus, driven by bleeding, so a shock would leave the cause untouched. Tell: a sinus P wave before every QRS rules out cardioversion; appropriate sinus tachycardia is managed by treating the cause.", "confused mechanism or drug class"],
   ["Intravenous metoprolol",
    "Within sinus tachycardia, beta blockers come up only for the inappropriate form, a diagnosis of exclusion with no secondary cause, and even there they are not well tolerated. Her tachycardia has an obvious cause, hypovolemia from bleeding, which makes it appropriate. Tell: an identified cause means treat the cause, not the rate.", "confused mechanism or drug class"]],
  C(17), "first-line", "next step"),

V(STA, IO_A,
  "A 29-year-old woman has had a resting heart rate of 105 to 115 for a year. Thyroid tests, a blood count, a drug screen and an echocardiogram are normal, and she takes no medications or stimulants. Her electrocardiogram shows a normal P wave before every narrow QRS. Which is the most likely diagnosis?",
  [["Inappropriate sinus tachycardia",
    "Correct. A resting rate of 105 to 115 for a year with a normal P wave before every narrow QRS is sinus tachycardia, and normal thyroid tests, blood count, drug screen and echocardiogram with no medications or stimulants exclude the secondary causes. A sinus tachycardia that stays unexplained after that is inappropriate sinus tachycardia, a diagnosis of exclusion."],
   ["Focal atrial tachycardia",
    "Focal atrial tachycardia comes from a single ectopic focus outside the sinus node, with a consistently abnormal P wave, usually at 150 to 250, and abrupt-onset palpitations. Her P waves are normal and her rate is a steady 105 to 115. Tell: a normal P-wave shape points to the sinus node; an abnormal one points to an ectopic focus.", "competing diagnosis"],
   ["Atrioventricular nodal reentry",
    "Nodal reentrant tachycardia is a paroxysmal, regular narrow tachycardia, usually 140 to 180, with hidden P waves. Hers is a persistent rate of 105 to 115 for a year with normal P waves visible before every QRS. Tell: sudden episodes with hidden P waves mean nodal reentry; a steady sinus rate with visible P waves does not.", "competing diagnosis"],
   ["Atrial flutter with 2:1 block",
    "Atrial flutter with 2:1 block shows two sawtooth waves for every QRS, at an atrial rate of 250 or more. She has one normal P wave before each QRS at about 110. Tell: one normal P wave per QRS is sinus; two sawtooth waves per QRS is flutter.", "competing diagnosis"]],
  C(16), "differential", "diagnosis"),

V(STA, IO_A,
  "A 31-year-old woman has inappropriate sinus tachycardia at about 110 after a full workup excluded other causes. Her only symptom is awareness of her heartbeat, and she asks whether she needs medication. Which response is most accurate?",
  [["Usually left untreated; benign",
    "Correct. Inappropriate sinus tachycardia is generally left untreated because patients tolerate the symptoms better than the treatment and the prognosis is usually benign. Management centers on removing influencing factors, such as night-shift work, illicit drugs and medications, rather than on beta blockers, which are poorly tolerated."],
   ["She needs a lifelong beta blocker",
    "Beta blockers are not well tolerated in inappropriate sinus tachycardia, which is why it is generally left untreated. Her only symptom is awareness of her heartbeat. Tell: patients tolerate the symptoms better than the treatment, so a lifelong drug is not the usual plan.", "common lay belief"],
   ["Cardioversion will cure it",
    "Synchronized cardioversion is for hemodynamically unstable tachyarrhythmias such as supraventricular tachycardia, atrial flutter or atrial fibrillation. Inappropriate sinus tachycardia is a sinus rhythm in a stable patient and is generally left untreated. Tell: a sinus rhythm is not shocked; management is removing influencing factors.", "confused mechanism or drug class"],
   ["She needs anticoagulation",
    "Anticoagulation belongs to atrial fibrillation and atrial flutter, guided by stroke risk. Inappropriate sinus tachycardia is a sinus rhythm with a usually benign prognosis, and anticoagulation is not part of its management. Tell: a sinus rhythm, even a fast one, does not bring an anticoagulation decision.", "confused mechanism or drug class"]],
  C(17), "education", "education"),

V(STA, IO_A,
  "A 63-year-old man ran out of his metoprolol four days ago. He feels his heart racing, and his pulse is 118 and regular, with a normal P wave before every narrow QRS. He has no fever and is not bleeding. Which is the most likely cause of his tachycardia?",
  [["Beta blocker withdrawal",
    "Correct. A regular rate of 118 with a normal P wave before every narrow QRS is sinus tachycardia, and abrupt withdrawal of a beta blocker or nondihydropyridine calcium channel blocker is a listed drug cause. Running out of metoprolol four days ago, with no fever or bleeding to explain the rate, fits that cause."],
   ["Hypothyroidism",
    "Hypothyroidism is a listed cause of sinus bradycardia and sick sinus syndrome, so it slows the sinus rate. His rate is fast at 118 and began after he ran out of metoprolol. Tell: hyperthyroidism, not hypothyroidism, sits on the sinus tachycardia list.", "reversed direction or value"],
   ["Raised intracranial pressure",
    "Increased intracranial pressure is a listed cause of sinus bradycardia, not sinus tachycardia. His fast sinus rate began after he stopped metoprolol, a listed drug-withdrawal cause. Tell: raised intracranial pressure slows the sinus node; beta blocker withdrawal speeds it.", "adjacent fact"],
   ["Increased vagal tone",
    "Increased vagal tone is not among the listed causes of sinus tachycardia, which are physiologic, pathologic or drug-related, including abrupt beta blocker withdrawal. A slow sinus rate, sinus bradycardia, is the adaptive response seen in well-conditioned athletes. Tell: a fast sinus rate four days after stopping metoprolol is withdrawal.", "reversed direction or value"]],
  C(16), "etiology", "diagnosis"),

V(STA, IO_A,
  "A 45-year-old man has a heart rate of 122 with a normal P wave before every narrow QRS. His temperature is 39.2°C and he has a productive cough and crackles at the right base. He is alert with a blood pressure of 126/78. Which is the best treatment for his heart rate?",
  [["Treat the infection and fever",
    "Correct. A rate of 122 with a normal P wave before every narrow QRS is sinus tachycardia, and with a temperature of 39.2°C, a productive cough and crackles it is an appropriate response to an underlying pathologic process, infection. Appropriate sinus tachycardia is managed by treating that cause, here the infection and fever."],
   ["Adenosine",
    "Adenosine follows a vagal maneuver in stable supraventricular tachycardia, converting the rhythm or slowing it to reveal P waves. His P waves are already visible and normal, and the rate is a response to fever and pneumonia. Tell: when the P waves are normal and a cause is obvious, treating the cause is the answer.", "confused mechanism or drug class"],
   ["Vagal maneuver",
    "A vagal maneuver is first line for stable reentrant tachycardias such as nodal reentry. His rhythm is sinus, with a normal P wave before every QRS, responding to fever and pneumonia. Tell: an obvious cause with visible normal P waves means appropriate sinus tachycardia, so treat the cause.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is for hemodynamically unstable tachyarrhythmias such as supraventricular tachycardia, atrial flutter or atrial fibrillation. He is alert with a blood pressure of 126/78, and his rhythm is sinus, driven by infection. Tell: a sinus rhythm with an obvious cause is not shocked; the cause is treated.", "confused mechanism or drug class"]],
  C(17), "first-line", "treatment"),

# ---------------------------------------------------------------- sick sinus syndrome
V(SSS, IO_A,
  "A 76-year-old woman has episodes of lightheadedness and one faint. A 24-hour ambulatory monitor shows runs of a fast, irregular rhythm that alternate with slow rates and long pauses. Which fast rhythm is most likely on her monitor?",
  [["Atrial fibrillation",
    "Correct. Runs of a fast, irregular rhythm alternating with slow rates and long pauses, with lightheadedness and a faint, are tachy-brady syndrome, a form of sick sinus syndrome. The tachyarrhythmia in tachy-brady syndrome is most commonly atrial fibrillation, which fits an irregular fast run."],
   ["Ventricular fibrillation",
    "Ventricular fibrillation is not the listed fast rhythm of tachy-brady syndrome, and she has recurring runs she lives through between slow spells. The tachyarrhythmia there is most commonly atrial fibrillation; ventricular tachycardia occurs in some patients and calls for a pacemaker with a defibrillator. Tell: recurring irregular fast runs with pauses are atrial fibrillation.", "competing diagnosis"],
   ["Sinus tachycardia",
    "Sinus tachycardia is regular with a uniform P wave before every QRS. Her fast runs are irregular, and in tachy-brady syndrome the fast rhythm is most commonly atrial fibrillation. Tell: an irregular fast phase alternating with pauses is not sinus; it is atrial fibrillation until proven otherwise.", "competing diagnosis"],
   ["Atrioventricular nodal reentry",
    "Nodal reentrant tachycardia is a regular narrow tachycardia, usually 140 to 180, typically in women without heart disease. Her fast runs are irregular and alternate with slow rates and pauses, the pattern of tachy-brady syndrome. Tell: irregular fast runs plus pauses in an older patient point to atrial fibrillation.", "competing diagnosis"]],
  C(18), "manifestation", "diagnosis"),

V(SSS, IO_A,
  "An 81-year-old man has known tachy-brady syndrome (a fast rhythm alternating with slow rates and pauses) and asks which fast rhythm is behind his palpitations. An ambulatory monitor is arranged. Which rhythm is it most likely to record during the fast episodes?",
  [["Atrial fibrillation",
    "Correct. In tachy-brady syndrome, the form of sick sinus syndrome in which a fast rhythm alternates with slow rates or pauses, the tachyarrhythmia is most commonly atrial fibrillation. During his fast episodes the monitor would most likely show an irregularly irregular rhythm without P waves."],
   ["Atrial flutter",
    "Atrial flutter is an organized atrial rhythm with sawtooth waves at an atrial rate of 250 or more, but it is not the named most-common fast rhythm of tachy-brady syndrome. That is atrial fibrillation. Tell: in tachy-brady syndrome, expect an irregularly irregular fast phase, not a regular sawtooth.", "competing diagnosis"],
   ["Ventricular tachycardia",
    "Ventricular tachycardia can be the fast rhythm in some patients with tachy-brady syndrome, who then need a permanent pacemaker with an implantable defibrillator. It is not the most common one; atrial fibrillation is. Tell: ventricular tachycardia changes the device, not the most likely rhythm.", "adjacent fact"],
   ["Junctional rhythm",
    "A junctional rhythm is a slow, regular rhythm usually at 40 to 60 with inverted or hidden P waves, and it can follow sinus arrest. It could appear in his slow phases, not his fast ones. Tell: junctional rhythm belongs to the brady side; atrial fibrillation is the usual tachy side.", "competing diagnosis"]],
  C(18), "test finding", "test"),

V(SSS, IO_A,
  "A 79-year-old man has tachy-brady syndrome (a fast rhythm alternating with slow rates and pauses) on monitoring, and he faints during the pauses. Thyroid tests and electrolytes are normal and he takes no rate-slowing drugs. Which treatment is most appropriate?",
  [["Permanent pacemaker",
    "Correct. He faints during the pauses of tachy-brady syndrome, so his symptoms correlate with the bradycardia, and the reversible causes (thyroid disease, electrolyte abnormalities, rate-slowing drugs) have been excluded. Symptomatic bradycardia in sick sinus syndrome is treated with a permanent pacemaker, and tachy-brady syndrome often needs one."],
   ["Atropine as needed",
    "Atropine is first line for acute, symptomatic, hemodynamically unstable bradycardia, a short-term rescue. His fainting comes from recurrent pauses that correlate with his symptoms, which calls for a permanent pacemaker. Tell: recurrent symptomatic pauses need a device, not an as-needed drug.", "wrong stage or severity"],
   ["Catheter ablation alone",
    "Ablation alone does not address the pauses that make him faint. When symptoms correlate with bradycardia in sick sinus syndrome, a permanent pacemaker is placed, and tachy-brady syndrome often needs one. Tell: fainting during pauses means pacing.", "confused mechanism or drug class"],
   ["Observation alone",
    "Observation is appropriate in sick sinus syndrome only when symptoms do not correlate with episodes of bradycardia. He faints during the pauses, so they clearly correlate. Tell: correlated symptoms move management to a permanent pacemaker.", "wrong stage or severity"]],
  C(22), "escalation", "treatment"),

V(SSS, IO_A,
  "A 72-year-old woman has sinus pauses of up to 2 seconds at night on an ambulatory monitor. Her occasional dizziness happens only when she stands up quickly and never during the pauses. Which is the most appropriate next step?",
  [["Observation",
    "Correct. In sick sinus syndrome the key step is to confirm whether symptoms correlate with episodes of bradycardia. Her night-time pauses cause no symptoms, and her dizziness occurs only on standing quickly, never during the pauses, so with no correlation observation is appropriate."],
   ["Permanent pacemaker",
    "A permanent pacemaker is placed in sick sinus syndrome when symptomatic bradycardia is confirmed, meaning symptoms correlate with the slow episodes. Her dizziness comes on standing, never during the pauses. Tell: no correlation, no pacemaker; observe instead.", "wrong stage or severity"],
   ["Atropine",
    "Atropine is first line for acute, symptomatic, hemodynamically unstable bradycardia. She is stable, and her pauses cause no symptoms. Tell: atropine needs an unstable patient; uncorrelated night-time pauses need observation.", "wrong stage or severity"],
   ["Catheter ablation",
    "Catheter ablation is used for tachycardias, such as focal atrial tachycardia or an accessory pathway. Her finding is brief night-time sinus pauses that do not match her symptoms. Tell: ablation removes fast circuits; uncorrelated pauses call for observation.", "confused mechanism or drug class"]],
  C(22), "first-line", "next step"),

V(SSS, IO_A,
  "A 70-year-old man with sick sinus syndrome has pauses on monitoring that alternate with runs of ventricular tachycardia. Which device is indicated?",
  [["Pacemaker with a defibrillator",
    "Correct. Tachy-brady syndrome often needs a permanent pacemaker, and when the tachyarrhythmia is ventricular tachycardia the patient needs a pacemaker with an implantable cardioverter defibrillator."],
   ["Pacemaker alone",
    "A permanent pacemaker alone covers the pauses of tachy-brady syndrome, but when the tachyarrhythmia is ventricular tachycardia the listed device is a pacemaker with an automatic implantable cardioverter-defibrillator. Tell: ventricular tachycardia is the trigger to add the defibrillator.", "wrong stage or severity"],
   ["No device; observe",
    "Observation is appropriate in sick sinus syndrome only when symptoms do not correlate with episodes of bradycardia. Tachy-brady syndrome with ventricular tachycardia needs a permanent pacemaker with an automatic implantable cardioverter-defibrillator. Tell: ventricular tachycardia as the fast phase means adding a defibrillator.", "wrong stage or severity"],
   ["Ablation alone",
    "Ablation alone is not the listed device answer for tachy-brady syndrome. The pauses need a permanent pacemaker, and because the tachyarrhythmia is ventricular tachycardia, the pacemaker comes with an automatic implantable cardioverter-defibrillator. Tell: pauses need pacing; ventricular tachycardia adds a defibrillator.", "confused mechanism or drug class"]],
  C(22), "escalation", "treatment"),

V(SSS, IO_A,
  "A 77-year-old man had cardiac surgery last year. A rhythm strip shows normal sinus beats, then a sudden pause with no P wave, after which narrow beats at 45 appear with no visible P waves. Which is the most likely diagnosis?",
  [["Sinus arrest",
    "Correct. Normal sinus beats followed by a sudden pause with no P wave mean the sinus node stopped generating impulses: sinus arrest, a form of sick sinus syndrome. The escape rhythm is junctional, narrow beats at 45 with no visible P waves. Injury to the sinus node from cardiac surgery is a listed cause, matching his history."],
   ["Sinus bradycardia",
    "Sinus bradycardia is a regular rhythm under 60 with a uniform P wave before every QRS. This strip shows a sudden pause and then narrow beats with no P waves, so the sinus node is not driving the slow beats at all. Tell: in sinus bradycardia every beat still has its P wave.", "competing diagnosis"],
   ["Sinus arrhythmia",
    "Sinus arrhythmia is a normal, physiologic rhythm at 60 to 100 that varies with breathing, with a uniform P wave before every QRS. A sudden pause followed by slow beats with no P waves in a man after cardiac surgery is pathologic. Tell: sinus arrhythmia never loses its P waves or stops abruptly.", "competing diagnosis"],
   ["Atrial flutter",
    "Atrial flutter shows sawtooth waves at an atrial rate of 250 or more, outnumbering the QRS complexes. This strip shows a flat pause followed by slow narrow beats with no atrial waves at all. Tell: flutter fills the baseline with waves; sinus arrest leaves it empty and then hands over to a junctional rhythm.", "competing diagnosis"]],
  C(18), "differential", "diagnosis"),

V(SSS, IO_POP,
  "A 73-year-old man has new pauses and slow rates on an ambulatory monitor. He started verapamil and digoxin last month for palpitations. He feels mildly lightheaded but is otherwise well. Which is the most appropriate first step?",
  [["Stop the rate-slowing drugs",
    "Correct. New pauses and slow rates a month after starting verapamil, a nondihydropyridine calcium channel blocker, and digoxin fit drug-induced sick sinus syndrome, since those medications are listed causes. Management starts with treating the underlying cause, and he is stable and only mildly lightheaded, so stopping the rate-slowing drugs comes first."],
   ["Permanent pacemaker now",
    "A permanent pacemaker is for symptomatic bradycardia in sick sinus syndrome once symptoms are shown to correlate with the slow rates, after the underlying cause is treated. His slow rates began with verapamil and digoxin, so treating that cause comes first. Tell: remove the reversible cause before committing to a device.", "wrong stage or severity"],
   ["Catheter ablation",
    "Catheter ablation is used for tachycardias, such as curing focal atrial tachycardia or an accessory pathway. His problem is pauses and slow rates caused by rate-slowing drugs. Tell: ablation removes a fast focus or circuit; it does not fix a slow sinus node.", "confused mechanism or drug class"],
   ["Intravenous atropine now",
    "Atropine is first line for acute, symptomatic, hemodynamically unstable bradycardia. He is stable and only mildly lightheaded, and his slow rates have a reversible drug cause. Tell: a stable patient with a drug-induced slow rhythm needs the culprit stopped, not a rescue drug.", "wrong stage or severity"]],
  DECK + ", Slides 13, 22", "first-line", "next step"),

]
