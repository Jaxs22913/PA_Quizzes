# -*- coding: utf-8 -*-
"""Rhythm strips and rhythm vignettes, pool A -- the STRIP questions (CMS I Exam 5, Lectures 29-30).

Every question here shows a real rhythm strip cropped from the two arrhythmia decks (see the strip
table in cms_e5rhy_scope.py), above a short patient case. Each strip is used once in the pool. The
stem gives the patient and what decides the action (stability, a pulse, symptoms); reading the
strip is the skill. Alt text says what is visible without naming the rhythm.

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation. Slides only.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e5rhy_scope import *


def V(topic, io, q, opts, cite, slot, lead, img=None, alt=None, slide=None):
    d = Q(topic, io, q, opts, cite)
    d["slot"] = slot
    d["lead"] = lead
    if img:
        d["img"] = "cms-e5-images/rhythm-strip-%02d.jpg" % img
        d["alt"] = alt
        d["slide"] = slide
    return d


SIN = "Sinus rhythms"
SSS = "Sick sinus syndrome"
ATR = "Atrial tachycardia"
SVT = "Nodal and reentrant tachycardia"
WPW = "Wolff-Parkinson-White syndrome"
FLU = "Atrial flutter"
AFB = "Atrial fibrillation"
JUN = "Junctional rhythm"
AVB = "First- and second-degree block"
CHB = "Third-degree block"
BBB = "Bundle branch blocks"
VTA = "Ventricular tachycardia"
TDP = "Torsades de pointes"
ARR = "Cardiac arrest rhythms"

QUESTIONS = [

# 01 -- sinus bradycardia, unstable -> atropine
V(SIN, IO_SV,
  "A 74-year-old man is brought in confused and pale, with a blood pressure of 74/40. The monitor reads a rate of 38, and his rhythm strip is shown. Which is the first-line treatment?",
  [["Atropine",
    "Correct. The strip shows a slow, regular rhythm with an upright P wave before every narrow QRS: sinus bradycardia. With confusion and hypotension it is acute, symptomatic and unstable, so atropine is first line, then a temporary pacemaker if it fails."],
   ["Adenosine",
    "Adenosine is the step after a vagal maneuver for stable supraventricular tachycardia, a fast rhythm; this slow, unstable sinus rhythm needs atropine first.", "confused mechanism or drug class"],
   ["Permanent pacemaker",
    "A permanent pacemaker is for chronic, symptomatic bradycardia; this acute, unstable episode is treated first with atropine and then a temporary pacemaker if needed.", "wrong stage or severity"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is a timed shock for an unstable tachycardia such as supraventricular tachycardia or atrial fibrillation; a slow sinus rhythm needs atropine.", "confused mechanism or drug class"]],
  C1(13), "first-line", "treatment",
  1, "Rhythm strip with four narrow complexes spaced widely apart, each preceded by an upright P wave", "Arrhythmias I, slide 12"),

# 02 -- sinus tachycardia -> a pathologic cause
V(SIN, IO_SV,
  "A 41-year-old woman has had palpitations for a month. The monitor reads a regular rate of 130, and her rhythm strip is shown. Which of the following would most likely account for this rhythm?",
  [["Hyperthyroidism",
    "Correct. A regular, narrow-complex rhythm at 130 with an upright P wave before every QRS is sinus tachycardia, which usually reflects a physiologic or pathologic process; hyperthyroidism is one of the listed pathologic causes."],
   ["Hypothyroidism",
    "Hypothyroidism is a listed cause of sinus bradycardia and sick sinus syndrome, slowing the rate below 60; this sinus rhythm is fast, which points the other way.", "reversed direction or value"],
   ["Digoxin therapy",
    "Digoxin is a listed cause of sinus bradycardia, along with beta blockers and nondihydropyridine calcium channel blockers; it slows the sinus rate rather than speeding it.", "reversed direction or value"],
   ["Raised intracranial pressure",
    "Increased intracranial pressure appears among the causes of sinus bradycardia, not tachycardia; a fast sinus rhythm comes from pain, anxiety, hypovolemia, anemia, hypoxia or hyperthyroidism.", "reversed direction or value"]],
  C1(16), "etiology", "etiology",
  2, "Rhythm strip with closely spaced, regular narrow complexes, each preceded by an upright P wave", "Arrhythmias I, slide 15"),

# 03 -- tachy-brady with symptomatic pauses -> permanent pacemaker
V(SSS, IO_SV_POP,
  "A 79-year-old woman has spells of a racing heartbeat followed by near-fainting. Her ambulatory monitor strip is shown, and her near-fainting spells match the long pauses. Which is the most appropriate management?",
  [["Permanent pacemaker",
    "Correct. Bursts of a rapid rhythm that stop into long pauses before slow beats return are tachy-brady syndrome, a form of sick sinus syndrome; when symptoms correlate with the bradycardia, a permanent pacemaker is the treatment."],
   ["Observation alone",
    "Observation is appropriate in sick sinus syndrome only when symptoms fail to correlate with the bradycardia; her near-fainting matches the pauses, so she needs a pacemaker.", "ruled out by a stated finding"],
   ["Atropine",
    "Atropine is the first-line drug for acute, unstable sinus bradycardia; chronic, recurrent symptomatic pauses from a sick sinus node are treated with a permanent pacemaker.", "wrong stage or severity"],
   ["Adenosine",
    "Adenosine is used for stable supraventricular tachycardia after a vagal maneuver; it does nothing for the pauses that are causing her near-fainting spells.", "confused mechanism or drug class"]],
  "%s, Slides 19, 22" % DECK1, "first-line", "treatment",
  3, "Three rows of a rhythm strip: bursts of rapid narrow complexes that stop abruptly, then long flat pauses before slower beats resume", "Arrhythmias I, slide 19"),

# 04 -- multifocal atrial tachycardia -> describe
V(ATR, IO_SV,
  "A 72-year-old man with severe chronic obstructive pulmonary disease is admitted in respiratory distress. His pulse is fast and irregular, and his rhythm strip is shown, with arrows marking P waves. Which description best fits this tracing?",
  [["Irregular, with several different P-wave shapes",
    "Correct. An irregular, narrow-complex tachycardia with a P wave before each QRS in at least three different shapes in the same lead is multifocal atrial tachycardia, typical of acutely ill patients with severe lung disease."],
   ["Irregularly irregular, with no visible P waves",
    "No P waves and an irregularly irregular rhythm describe atrial fibrillation; on this strip the arrows point to P waves, and their shape changes from beat to beat.", "competing diagnosis"],
   ["Regular, with one abnormal P-wave shape",
    "A regular rhythm with one consistently abnormal P wave is focal atrial tachycardia from a single ectopic focus; this rhythm is irregular, with P waves of changing shape.", "competing diagnosis"],
   ["Regular, with sawtooth waves between beats",
    "Regular sawtooth waves outnumbering the QRS complexes are atrial flutter; this strip shows separate P waves of varying shape, one before each QRS, at irregular intervals.", "competing diagnosis"]],
  "%s, Slides 28, 29" % DECK1, "test finding", "describe",
  4, "Rhythm strip of a fast, irregular narrow-complex rhythm; three arrows point to the small waves before several of the complexes", "Arrhythmias I, slide 29"),

# 05 -- pre-excitation in sinus rhythm -> describe
V(WPW, IO_SV,
  "A 17-year-old soccer player had an episode of racing heartbeat that stopped on its own. His resting tracing, taken in sinus rhythm, is shown. Which description best fits this tracing?",
  [["Short PR with a slurred QRS upstroke",
    "Correct. A short PR interval with a slurred upstroke of the QRS (the delta wave) in sinus rhythm is pre-excitation, consistent with an accessory pathway (bundle of Kent) and Wolff-Parkinson-White syndrome."],
   ["Long PR with every P wave conducted",
    "A PR interval over 0.20 seconds with every P wave conducted is first-degree atrioventricular block; on this tracing the P wave runs almost straight into the QRS, so the PR is short.", "reversed direction or value"],
   ["Progressively longer PR, then a dropped beat",
    "PR lengthening until a QRS drops is Mobitz type I block; here every P wave is followed by a QRS, and the striking feature is the slurred start of each QRS.", "competing diagnosis"],
   ["Irregular rhythm with no P waves",
    "No P waves and an irregular rhythm describe atrial fibrillation; this tracing is in sinus rhythm, with a P wave before every QRS.", "ruled out by a stated finding"]],
  C1(35), "test finding", "describe",
  5, "Close-up rhythm strip of three beats, each with a small P wave running into a QRS whose upstroke is gradual before the main spike", "Arrhythmias I, slide 35"),

# 06 -- stable narrow regular tachycardia -> vagal maneuver
V(SVT, IO_SV,
  "A 28-year-old woman has had a pounding heartbeat for 30 minutes that began suddenly. She is alert, with a blood pressure of 118/76. The monitor reads a regular rate of 170, and her rhythm strip is shown. Which is the most appropriate next step?",
  [["Vagal maneuver",
    "Correct. A regular, narrow-complex tachycardia with no visible P waves is supraventricular tachycardia (here typical nodal reentry); in a stable patient a vagal maneuver comes first, then adenosine if it fails."],
   ["Adenosine",
    "Adenosine is the right drug for stable supraventricular tachycardia, but it comes second: the first-line step in a stable patient is a vagal maneuver.", "wrong stage or severity"],
   ["Synchronized cardioversion",
    "Immediate synchronized cardioversion is for hemodynamically unstable supraventricular tachycardia; she is alert with a normal blood pressure.", "wrong stage or severity"],
   ["Intravenous procainamide",
    "Procainamide is used for atrial fibrillation conducting down an accessory pathway, an irregular wide rhythm; this strip is regular and narrow, so a vagal maneuver comes first.", "confused mechanism or drug class"]],
  "%s, Slides 26, 39" % DECK1, "first-line", "next step",
  6, "Lead II rhythm strip of a regular, rapid narrow-complex rhythm with no P wave visible before the complexes", "Arrhythmias I, slide 39"),

# 07 -- atrial flutter -> diagnosis
V(FLU, IO_SV,
  "A 66-year-old man who had cardiac surgery last year reports palpitations and fatigue. His blood pressure is normal, and his rhythm strip is shown. Which is the most likely diagnosis?",
  [["Atrial flutter",
    "Correct. Repeating sawtooth (flutter) waves outnumber the narrow QRS complexes because the atrioventricular node blocks some of them: atrial flutter, common after atrial scarring from cardiac surgery."],
   ["Atrial fibrillation",
    "Atrial fibrillation is irregularly irregular with no organized atrial waves; this strip shows regular, repeating sawtooth waves between the QRS complexes.", "competing diagnosis"],
   ["Multifocal atrial tachycardia",
    "Multifocal atrial tachycardia has one P wave per QRS in at least three shapes; here several identical sawtooth waves fall between each pair of QRS complexes.", "competing diagnosis"],
   ["Sinus tachycardia",
    "Sinus tachycardia has one upright P wave before each QRS at 100 to 160; this strip has several identical atrial waves for every QRS, the sawtooth of flutter.", "competing diagnosis"]],
  "%s, Slides 42, 43, 44" % DECK1, "test finding", "diagnosis",
  7, "Rhythm strip of narrow complexes with a continuous zigzag baseline of identical small waves between them, two to four per complex", "Arrhythmias I, slide 43"),

# 08 -- atrial fibrillation, stable -> rate control
V(AFB, IO_SV,
  "A 70-year-old woman with hypertension has had palpitations for a week. She is alert, with a blood pressure of 132/80, and her rhythm strip is shown. Which is the first goal of treatment?",
  [["Rate control",
    "Correct. Narrow complexes at irregularly irregular intervals with no P waves are atrial fibrillation; in a hemodynamically stable patient the first goal is rate control, with anticoagulation decided by the stroke-risk score."],
   ["Immediate synchronized shock",
    "Synchronized cardioversion now is for hemodynamically unstable atrial fibrillation; she is alert and normotensive, so rate control comes first.", "wrong stage or severity"],
   ["Adenosine",
    "Adenosine treats regular supraventricular tachycardia after a vagal maneuver; this rhythm is irregularly irregular with no P waves, and the goal is rate control.", "competing diagnosis"],
   ["Catheter ablation",
    "Mapping and ablation are a later option in atrial fibrillation; the first goal in a stable patient is rate control, then anticoagulation.", "wrong stage or severity"]],
  "%s, Slides 47, 49" % DECK1, "first-line", "treatment",
  8, "Rhythm strip of narrow complexes at visibly unequal intervals over a wavy baseline with no clear P waves", "Arrhythmias I, slide 47"),

# 09 -- pre-excited atrial fibrillation -> procainamide
V(WPW, IO_SV,
  "A 22-year-old man has sudden palpitations and lightheadedness. He is alert, with a blood pressure of 112/70. His 12-lead electrocardiogram is shown. Which drug is the most appropriate?",
  [["Intravenous procainamide",
    "Correct. A very fast, irregular rhythm with wide complexes of changing width is atrial fibrillation conducting down an accessory pathway (pre-excited atrial fibrillation); intravenous procainamide is used, never adenosine."],
   ["Adenosine",
    "When atrial fibrillation runs with Wolff-Parkinson-White, adenosine must not be used; the drug for pre-excited atrial fibrillation is intravenous procainamide.", "confused mechanism or drug class"],
   ["Intravenous beta blocker",
    "Intravenous rate control suits ordinary atrial fibrillation with a rapid rate; an irregular, wide rhythm through an accessory pathway is treated with procainamide.", "competing diagnosis"],
   ["Intravenous lidocaine",
    "Lidocaine is a choice for stable monomorphic ventricular tachycardia, which is regular at about 150 to 200; this wide rhythm is irregular and approaches 300.", "competing diagnosis"]],
  "%s, Slides 37, 52, 53" % DECK1, "agent/regimen", "treatment",
  9, "Twelve-lead electrocardiogram of a very rapid, irregular rhythm with wide complexes whose width and height vary from beat to beat", "Arrhythmias I, slide 52"),

# 10 -- junctional rhythm in an athlete -> diagnosis
V(JUN, IO_V,
  "A 30-year-old marathon runner has no symptoms. A lead II tracing taken at rest is shown; the rate is 48. Which is the most likely diagnosis?",
  [["Junctional rhythm",
    "Correct. A regular, narrow-complex rhythm at 40 to 60 with no P waves visible (hidden in the QRS) is a junctional rhythm, which can be seen in healthy, well-conditioned athletes with increased vagal tone."],
   ["Sinus bradycardia",
    "Sinus bradycardia, also common in athletes, has an upright P wave before every QRS; this tracing shows no P wave before any of the complexes.", "ruled out by a stated finding"],
   ["Third-degree block",
    "Third-degree block shows P waves marching at their own rate, unrelated to a slow escape rhythm; this tracing has no P waves to march.", "competing diagnosis"],
   ["Atrial fibrillation",
    "Atrial fibrillation is irregularly irregular; these complexes are evenly spaced, slow and regular, with no fibrillating baseline.", "competing diagnosis"]],
  "%s, Slides 62, 63, 64" % DECK1, "test finding", "diagnosis",
  10, "Lead II rhythm strip of five narrow complexes at a slow, regular rate, each followed by a T wave, with no P wave visible before any complex", "Arrhythmias I, slide 63"),

# 11 -- Mobitz type I -> diagnosis
V(AVB, IO_V,
  "A 58-year-old man who takes a beta blocker has an irregular pulse at a routine visit. He has no symptoms, and his rhythm strip is shown. Which is the most likely diagnosis?",
  [["Mobitz type I block",
    "Correct. The PR interval grows longer beat by beat until a P wave is not followed by a QRS, then the cycle restarts: second-degree Mobitz type I (Wenckebach) block, which medications such as beta blockers can cause."],
   ["Mobitz type II block",
    "Mobitz type II keeps a constant PR interval before randomly dropped QRS complexes; on this strip the PR lengthens progressively before each drop.", "competing diagnosis"],
   ["First-degree block",
    "First-degree block is a long but constant PR with every P wave conducted; this strip has a P wave that is not followed by a QRS.", "ruled out by a stated finding"],
   ["Third-degree block",
    "Third-degree block shows no relationship between P waves and QRS complexes; here the conducted beats keep a PR interval that lengthens in a repeating pattern.", "competing diagnosis"]],
  "%s, Slides 7, 8, 9" % DECK2, "test finding", "diagnosis",
  11, "Rhythm strip with small upright P waves and narrow complexes in groups, with a gap where one P wave stands alone", "Arrhythmias II, slide 8"),

# 12 -- Mobitz type II, symptomatic -> transcutaneous pacing
V(AVB, IO_V,
  "A 76-year-old woman is brought in after fainting twice today. She is pale, with a blood pressure of 84/50, and her lead II rhythm strip is shown. Which is the most appropriate emergent treatment?",
  [["Transcutaneous pacing",
    "Correct. P waves at a steady rate with a constant PR, then a P wave with no QRS, is Mobitz type II block; with fainting and hypotension the emergent treatment is transcutaneous pacing, followed by a permanent pacemaker."],
   ["Permanent pacemaker",
    "A permanent pacemaker is the definitive treatment for Mobitz type II block, but with fainting and hypotension right now she first needs emergent transcutaneous pacing.", "wrong stage or severity"],
   ["Adenosine",
    "Adenosine is used to slow or stop a regular supraventricular tachycardia, a fast rhythm; this slow rhythm with dropped QRS complexes needs pacing.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion shocks an unstable tachycardia with a pulse; this is a slow rhythm with dropped QRS complexes, which needs pacing.", "confused mechanism or drug class"]],
  "%s, Slides 11, 14" % DECK2, "first-line", "next step",
  12, "Lead II rhythm strip with regular small P waves and narrow complexes; at one point a P wave appears with no complex after it, leaving a long gap", "Arrhythmias II, slide 11"),

# 13 -- third-degree block -> describe
V(CHB, IO_V,
  "An 81-year-old man reports dizziness and two fainting spells. His pulse is 36, and his rhythm strip is shown, with arrows marking R waves and P waves. Which description best fits this tracing?",
  [["P waves and QRS complexes at unrelated rates",
    "Correct. The P waves march at their own regular rate and the slow QRS complexes at another, with no fixed relation: complete dissociation of the atria from the ventricles, third-degree (complete) block, ventricular rate usually under 40."],
   ["PR lengthens until a QRS is dropped",
    "Progressive PR lengthening before a dropped QRS is Mobitz type I block; here the P waves keep no consistent relation to the QRS at all.", "competing diagnosis"],
   ["Constant PR with an occasional dropped QRS",
    "A constant PR with occasional dropped beats is Mobitz type II block; on this strip the distance from P wave to QRS changes every beat.", "competing diagnosis"],
   ["Every P wave conducted with a long PR",
    "A long, constant PR with every P wave conducted is first-degree block; here most P waves are not followed by a QRS, and the two run at different rates.", "competing diagnosis"]],
  "%s, Slides 15, 16" % DECK2, "test finding", "describe",
  13, "Rhythm strip with regularly spaced P waves (upward arrows) and slower complexes (downward arrows) that fall at varying distances from the P waves", "Arrhythmias II, slide 16"),

# 14 -- left bundle branch block -> diagnosis
V(BBB, IO_V,
  "A 69-year-old woman with long-standing hypertension has a preoperative 12-lead electrocardiogram, which is shown. The QRS lasts 0.16 seconds. Which is the most likely diagnosis?",
  [["Left bundle branch block",
    "Correct. A QRS over 0.12 seconds with a deep, dominant S wave in V1 and broad, upright lateral complexes without Q waves in I, V5 and V6 is left bundle branch block; chronic hypertension is a common cause."],
   ["Right bundle branch block",
    "Right bundle branch block gives an rsR' pattern (a second upward deflection) in V1 to V3 and a slurred S wave in I and aVL; here V1 to V3 are deep and downward.", "competing diagnosis"],
   ["Ventricular tachycardia",
    "Ventricular tachycardia is a regular wide rhythm at 100 to 250; this tracing has wide complexes at a normal rate, from slowed conduction in one bundle.", "competing diagnosis"],
   ["Wolff-Parkinson-White syndrome",
    "Wolff-Parkinson-White shows a short PR and a slurred QRS upstroke (delta wave); this pattern of deep V1 complexes and broad lateral R waves is a bundle branch block.", "competing diagnosis"]],
  "%s, Slides 24, 25, 26" % DECK2, "test finding", "diagnosis",
  14, "Twelve-lead electrocardiogram with wide complexes, deep downward complexes in V1 to V3 and broad upright complexes in the lateral leads", "Arrhythmias II, slide 25"),

# 15 -- monomorphic VT, unstable with a pulse -> synchronized cardioversion
V(VTA, IO_V,
  "A 64-year-old man with a prior heart attack has chest pain and a blood pressure of 78/50, with a weak carotid pulse. His rhythm strip is shown. Which is the most appropriate next step?",
  [["Synchronized cardioversion",
    "Correct. A regular, wide-complex tachycardia of identical QRS shapes is monomorphic ventricular tachycardia; chest pain and hypotension make it unstable, and with a pulse present the treatment is synchronized cardioversion."],
   ["Defibrillation",
    "Defibrillation, an unsynchronized shock, is for pulseless ventricular tachycardia or fibrillation; this man still has a pulse, so the shock is synchronized.", "wrong stage or severity"],
   ["Intravenous amiodarone",
    "Intravenous amiodarone, lidocaine or procainamide is pharmacologic cardioversion for stable monomorphic ventricular tachycardia; chest pain and hypotension call for a shock.", "wrong stage or severity"],
   ["Adenosine",
    "Adenosine treats regular narrow-complex supraventricular tachycardia; this rhythm is wide and ventricular, and the patient is unstable.", "confused mechanism or drug class"]],
  "%s, Slides 41, 45" % DECK2, "first-line", "next step",
  15, "Rhythm strip of a rapid, regular series of broad complexes that all have the same shape, with no P waves seen", "Arrhythmias II, slide 41"),

# 16 -- polymorphic VT, "looks stable" -> defibrillate
V(VTA, IO_V,
  "A 59-year-old woman with crushing chest pain becomes lightheaded but stays awake, with a pulse and a blood pressure of 104/66. Her QT interval was normal on a tracing an hour ago, and her rhythm strip is shown. Which is the most appropriate next step?",
  [["Defibrillation",
    "Correct. Wide complexes that keep changing shape are polymorphic ventricular tachycardia; even when the patient looks well it is never truly stable, a short-lived transitional state that needs defibrillation."],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is used for unstable monomorphic ventricular tachycardia with a pulse; polymorphic ventricular tachycardia is defibrillated.", "competing diagnosis"],
   ["Intravenous amiodarone alone",
    "Amiodarone may be added after the shock, but drug therapy alone is for stable monomorphic ventricular tachycardia; polymorphic ventricular tachycardia is never truly stable.", "wrong stage or severity"],
   ["Intravenous magnesium",
    "Magnesium breaks torsades de pointes, the polymorphic tachycardia of a prolonged QT; her QT was normal, which points to ischemia and calls for defibrillation.", "ruled out by a stated finding"]],
  "%s, Slides 41, 46" % DECK2, "first-line", "next step",
  16, "Rhythm strip of a rapid, wide-complex rhythm whose complexes vary in height, width and shape from beat to beat", "Arrhythmias II, slide 41"),

# 17 -- torsades, conscious -> magnesium
V(TDP, IO_V,
  "A 48-year-old woman started a medication known to prolong the QT interval last week. She now has palpitations but is awake and talking, and her rhythm strip is shown. Which is the most appropriate treatment?",
  [["Intravenous magnesium",
    "Correct. A polymorphic ventricular tachycardia whose complexes twist around the baseline in a patient with a long QT is torsades de pointes; in a conscious patient intravenous magnesium breaks it, then more magnesium as an infusion."],
   ["Intravenous amiodarone",
    "Amiodarone (like procainamide) is avoided in torsades de pointes because it prolongs the QT further; magnesium is the treatment.", "confused mechanism or drug class"],
   ["Intravenous beta blocker",
    "Beta blockers are avoided in torsades de pointes: the bradycardia they cause lengthens the R-to-R interval and indirectly the QT.", "confused mechanism or drug class"],
   ["Adenosine",
    "Adenosine treats regular narrow-complex supraventricular tachycardia; this is a wide, polymorphic ventricular rhythm that needs magnesium.", "competing diagnosis"]],
  "%s, Slides 41, 47" % DECK2, "agent/regimen", "treatment",
  17, "Rhythm strip of a rapid, wide-complex rhythm whose complexes grow taller, shrink, then grow again, as if turning around the baseline", "Arrhythmias II, slide 41"),

# 18 -- coarse ventricular fibrillation -> defibrillation
V(ARR, IO_V,
  "A 62-year-old man collapses in a hospital hallway. He is unresponsive with no pulse, and cardiopulmonary resuscitation is started. His monitor strip is shown. Which is the most important next step?",
  [["Defibrillation",
    "Correct. Chaotic, uncoordinated activity with no organized QRS complexes and no pulse is ventricular fibrillation, treated as cardiac arrest with defibrillation (an unsynchronized shock) as soon as possible, then 2 minutes of compressions."],
   ["Synchronized cardioversion",
    "Synchronized cardioversion times the shock to a QRS complex, so it is for a tachycardia with a pulse; ventricular fibrillation has no QRS to time to and needs defibrillation.", "confused mechanism or drug class"],
   ["Intravenous amiodarone",
    "Amiodarone is added for ventricular fibrillation that persists after shocks and epinephrine; the first priority in this arrest is an immediate unsynchronized shock.", "wrong stage or severity"],
   ["Transcutaneous pacing",
    "Transcutaneous pacing is the emergent treatment for unstable bradycardia from high-grade block; this pulseless chaotic rhythm needs defibrillation.", "confused mechanism or drug class"]],
  "%s, Slides 48, 49, 50" % DECK2, "first-line", "next step",
  18, "Rhythm strip of continuous, irregular, low-to-medium waves with no recognizable P waves or complexes", "Arrhythmias II, slide 49"),

# 19 -- asystole -> compressions and epinephrine
V(ARR, IO_V,
  "A 77-year-old woman is found unresponsive and pulseless, and chest compressions are started. Her monitor strip is shown, and the same flat tracing appears in every lead. Which is the most appropriate next step?",
  [["Compressions and epinephrine",
    "Correct. A flat line with no P waves or QRS complexes is asystole, which is unshockable: continue high-quality chest compressions and give epinephrine every 3 to 5 minutes, the mainstays of treatment; the prognosis is poor."],
   ["Defibrillation",
    "Defibrillation treats ventricular fibrillation and pulseless ventricular tachycardia; asystole and pulseless electrical activity are unshockable.", "competing diagnosis"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion needs a QRS complex to time the shock to and a patient with a pulse; asystole has neither and is unshockable.", "confused mechanism or drug class"],
   ["Intravenous amiodarone",
    "Amiodarone is for ventricular fibrillation or pulseless ventricular tachycardia that persists after shocks; asystole is treated with compressions and epinephrine.", "confused mechanism or drug class"]],
  "%s, Slides 52, 53, 55" % DECK2, "first-line", "next step",
  19, "Rhythm strip with a nearly flat line across the whole page and no complexes", "Arrhythmias II, slide 53"),
]

check_strips(QUESTIONS)
