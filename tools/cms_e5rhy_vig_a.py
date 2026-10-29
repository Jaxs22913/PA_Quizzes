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
    "Correct. A regular rhythm at 130 with a P wave before every narrow QRS is sinus tachycardia, which is usually the result of a physiologic or pathologic process. Hyperthyroidism is one of the listed pathologic causes, alongside hypovolemia, anemia, hypoxia, pulmonary embolism and myocardial infarction, and it fits a month of palpitations."],
   ["Hypothyroidism",
    "Hypothyroidism is a listed cause of sinus bradycardia and of sick sinus syndrome, slowing the sinus rate below 60. Her sinus rhythm is fast at 130. Tell: the thyroid pair splits by direction; hyperthyroidism is on the list of pathologic causes of sinus tachycardia, hypothyroidism on the slow list.", "reversed direction or value"],
   ["Digoxin therapy",
    "Digoxin is listed with beta blockers and nondihydropyridine calcium channel blockers as a drug cause of sinus bradycardia; it slows the sinus rate. The drug causes of sinus tachycardia are stimulants, anticholinergics, or abrupt withdrawal of a beta blocker or nondihydropyridine calcium channel blocker. Tell: digoxin belongs on the slow list.", "reversed direction or value"],
   ["Raised intracranial pressure",
    "Increased intracranial pressure is listed among the causes of sinus bradycardia, so it would slow this rhythm below 60, not raise it to 130. A fast sinus rate instead points to causes such as pain, anxiety, hypovolemia, anemia, hypoxia or hyperthyroidism. Tell: raised intracranial pressure goes with a slow sinus rate.", "reversed direction or value"]],
  C1(16), "etiology", "etiology",
  2, "Rhythm strip with closely spaced, regular narrow complexes, each preceded by an upright P wave", "Arrhythmias I, slide 15"),

# 03 -- tachy-brady with symptomatic pauses -> permanent pacemaker
V(SSS, IO_SV_POP,
  "A 79-year-old woman has spells of a racing heartbeat followed by near-fainting. Her ambulatory monitor strip is shown, and her near-fainting spells match the long pauses. Which is the most appropriate management?",
  [["Permanent pacemaker",
    "Correct. Bursts of a racing rhythm that stop into long pauses are tachy-brady syndrome, a form of sick sinus syndrome, and her near-fainting matches the pauses. When symptoms correlate with the bradycardia, a permanent pacemaker is the treatment, and tachy-brady syndrome often needs one."],
   ["Observation alone",
    "Observation is appropriate in sick sinus syndrome only when symptoms do not correlate with episodes of bradycardia. Her near-fainting spells match the long pauses on her monitor. Tell: correlation between symptoms and pauses moves management from watching to a permanent pacemaker.", "ruled out by a stated finding"],
   ["Atropine",
    "Atropine is first line for acute, symptomatic, hemodynamically unstable bradycardia, a short-term rescue. Her problem is recurrent, documented pauses from a diseased sinus node, which needs a permanent pacemaker. Tell: acute and unstable means atropine; recurrent and symptomatic means a permanent pacemaker.", "wrong stage or severity"],
   ["Adenosine",
    "Adenosine is used for stable supraventricular tachycardia after a vagal maneuver, to convert the rhythm or slow it. Her near-fainting comes from the pauses, and slowing her heart would not help them. Tell: in tachy-brady syndrome, symptoms that match the pauses call for a permanent pacemaker.", "confused mechanism or drug class"]],
  "%s, Slides 19, 22" % DECK1, "first-line", "treatment",
  3, "Three rows of a rhythm strip: bursts of rapid narrow complexes that stop abruptly, then long flat pauses before slower beats resume", "Arrhythmias I, slide 19"),

# 04 -- multifocal atrial tachycardia -> describe
V(ATR, IO_SV,
  "A 72-year-old man with severe chronic obstructive pulmonary disease is admitted in respiratory distress. His pulse is fast and irregular, and his rhythm strip is shown, with arrows marking P waves. Which description best fits this tracing?",
  [["Irregular, with several different P-wave shapes",
    "Correct. The strip shows an irregular, narrow-complex tachycardia with a P wave before each QRS whose shape changes from beat to beat, at least three shapes in the same lead: multifocal atrial tachycardia. It is typical of acutely ill patients with severe chronic obstructive pulmonary disease, as in his respiratory distress."],
   ["Irregularly irregular, with no visible P waves",
    "No P waves with an irregularly irregular rhythm describes atrial fibrillation. On this strip the arrows point to P waves, and their shape changes from beat to beat. Tell: if you can mark a P wave before each QRS, the rhythm is not fibrillation.", "competing diagnosis"],
   ["Regular, with one abnormal P-wave shape",
    "A regular rhythm with one consistently abnormal P wave describes focal atrial tachycardia, from a single ectopic focus. This rhythm is irregular, with P waves of changing shape. Tell: one shape in a regular rhythm is focal; several shapes in an irregular rhythm is multifocal.", "competing diagnosis"],
   ["Regular, with sawtooth waves between beats",
    "Regular sawtooth waves outnumbering the QRS complexes describe atrial flutter, at an atrial rate of 250 or more. This strip shows separate P waves of varying shape, one before each QRS, at irregular intervals. Tell: one changing P wave per beat is multifocal; a repeating sawtooth is flutter.", "competing diagnosis"]],
  "%s, Slides 28, 29" % DECK1, "test finding", "describe",
  4, "Rhythm strip of a fast, irregular narrow-complex rhythm; three arrows point to the small waves before several of the complexes", "Arrhythmias I, slide 29"),

# 05 -- pre-excitation in sinus rhythm -> describe
V(WPW, IO_SV,
  "A 17-year-old soccer player had an episode of racing heartbeat that stopped on its own. His resting tracing, taken in sinus rhythm, is shown. Which description best fits this tracing?",
  [["Short PR with a slurred QRS upstroke",
    "Correct. On his resting tracing in sinus rhythm, the P wave runs almost straight into a QRS whose upstroke is slurred: a short PR interval with a delta wave. That is pre-excitation, consistent with an accessory pathway (bundle of Kent) and Wolff-Parkinson-White, which fits his self-terminating episode of racing heartbeat."],
   ["Long PR with every P wave conducted",
    "A long PR interval is not this tracing; the P wave runs almost straight into the QRS, so the PR is short, under 0.12 seconds. Combined with the slurred QRS upstroke (delta wave), that short PR marks pre-excitation through an accessory pathway. Tell: in Wolff-Parkinson-White the PR is short, never long.", "reversed direction or value"],
   ["Progressively longer PR, then a dropped beat",
    "A PR interval that lengthens until a beat drops is not what this tracing shows; every P wave here is followed by a QRS. The striking features are a short PR and a slurred start to each QRS (delta wave), which is pre-excitation. Tell: look at the start of the QRS; a slurred upstroke means an accessory pathway.", "competing diagnosis"],
   ["Irregular rhythm with no P waves",
    "An irregular rhythm with no P waves describes atrial fibrillation. This tracing was taken in sinus rhythm, with a P wave before every QRS. Tell: in sinus rhythm the clues to an accessory pathway are a short PR and a delta wave, not irregularity.", "ruled out by a stated finding"]],
  C1(35), "test finding", "describe",
  5, "Close-up rhythm strip of three beats, each with a small P wave running into a QRS whose upstroke is gradual before the main spike", "Arrhythmias I, slide 35"),

# 06 -- stable narrow regular tachycardia -> vagal maneuver
V(SVT, IO_SV,
  "A 28-year-old woman has had a pounding heartbeat for 30 minutes that began suddenly. She is alert, with a blood pressure of 118/76. The monitor reads a regular rate of 170, and her rhythm strip is shown. Which is the most appropriate next step?",
  [["Vagal maneuver",
    "Correct. A sudden, regular narrow-complex tachycardia at 170 with no visible P waves is supraventricular tachycardia, here typical slow-fast nodal reentry, and she is alert with a blood pressure of 118/76. In a stable patient a vagal maneuver is first line, followed by adenosine if it fails."],
   ["Adenosine",
    "Adenosine is the right drug for stable supraventricular tachycardia, but it comes second, after a vagal maneuver; it may convert the rhythm or slow it enough to show P waves. She is stable, so the drug-free step comes first. Tell: in a stable patient, try the vagal maneuver before any drug.", "wrong stage or severity"],
   ["Synchronized cardioversion",
    "Immediate synchronized cardioversion is for hemodynamically unstable supraventricular tachycardia. She is alert with a blood pressure of 118/76 after 30 minutes, so she is stable. Tell: stable means vagal maneuver, then adenosine; unstable means a timed shock.", "wrong stage or severity"],
   ["Intravenous procainamide",
    "Intravenous procainamide is used when Wolff-Parkinson-White is known or adenosine reveals atrial fibrillation with Wolff-Parkinson-White. Her strip is regular and narrow without pre-excitation. Tell: a regular narrow tachycardia in a stable patient starts with a vagal maneuver.", "confused mechanism or drug class"]],
  "%s, Slides 26, 39" % DECK1, "first-line", "next step",
  6, "Lead II rhythm strip of a regular, rapid narrow-complex rhythm with no P wave visible before the complexes", "Arrhythmias I, slide 39"),

# 07 -- atrial flutter -> diagnosis
V(FLU, IO_SV,
  "A 66-year-old man who had cardiac surgery last year reports palpitations and fatigue. His blood pressure is normal, and his rhythm strip is shown. Which is the most likely diagnosis?",
  [["Atrial flutter",
    "Correct. Repeating sawtooth flutter waves outnumber the narrow QRS complexes because the atrioventricular node blocks some of the impulses, which is atrial flutter. It is commonly seen with atrial scarring or damage from surgery, as after his cardiac operation, and causes palpitations and fatigue without usually causing collapse."],
   ["Atrial fibrillation",
    "Atrial fibrillation is irregularly irregular with absent P waves and no organized atrial activity. This strip shows repeating sawtooth waves between the QRS complexes. Tell: an organized sawtooth baseline is flutter; a chaotic baseline with no P waves is fibrillation.", "competing diagnosis"],
   ["Multifocal atrial tachycardia",
    "Multifocal atrial tachycardia has one P wave per QRS in at least three different shapes, usually in acutely ill patients with severe lung disease or heart failure. Here several sawtooth waves fall between each pair of QRS complexes. Tell: changing P shapes, one per beat, is multifocal; a repeating sawtooth outnumbering the QRS complexes is flutter.", "competing diagnosis"],
   ["Sinus tachycardia",
    "Sinus tachycardia has one uniform P wave before each QRS at over 100 to 160. This strip has several atrial waves for every QRS in a sawtooth pattern. Tell: one P wave per QRS is sinus; more atrial waves than QRS complexes is flutter.", "competing diagnosis"]],
  "%s, Slides 42, 43, 44" % DECK1, "test finding", "diagnosis",
  7, "Rhythm strip of narrow complexes with a continuous zigzag baseline of identical small waves between them, two to four per complex", "Arrhythmias I, slide 43"),

# 08 -- atrial fibrillation, stable -> rate control
V(AFB, IO_SV,
  "A 70-year-old woman with hypertension has had palpitations for a week. She is alert, with a blood pressure of 132/80, and her rhythm strip is shown. Which is the first goal of treatment?",
  [["Rate control",
    "Correct. The strip shows narrow complexes at irregularly irregular intervals with no P waves, which is atrial fibrillation, and with a blood pressure of 132/80 and a clear mind she is hemodynamically stable. Stable atrial fibrillation is managed with rate control, with anticoagulation decided by her stroke-risk score, to which her hypertension and age contribute."],
   ["Immediate synchronized shock",
    "Immediate synchronized cardioversion is for hemodynamically unstable atrial fibrillation. She is alert with a blood pressure of 132/80, so she is stable, and an elective cardioversion would need 21 days of anticoagulation first. Tell: a shock now needs instability, such as hypotension or pulmonary edema.", "wrong stage or severity"],
   ["Adenosine",
    "Adenosine is a step for stable, regular supraventricular tachycardia, after a vagal maneuver, to convert the rhythm or slow it enough to reveal P waves. Her rhythm is irregularly irregular with no P waves, already recognizable as atrial fibrillation. Tell: an irregularly irregular rhythm without P waves needs rate control, not a diagnostic drug.", "competing diagnosis"],
   ["Catheter ablation",
    "Mapping and ablation is one of the later options in managing atrial fibrillation, not the first goal of treatment. A stable patient like her starts with rate control, and anticoagulation is planned for all. Tell: stable atrial fibrillation begins with rate control; procedures come later.", "wrong stage or severity"]],
  "%s, Slides 47, 49" % DECK1, "first-line", "treatment",
  8, "Rhythm strip of narrow complexes at visibly unequal intervals over a wavy baseline with no clear P waves", "Arrhythmias I, slide 47"),

# 09 -- pre-excited atrial fibrillation -> procainamide
V(WPW, IO_SV,
  "A 22-year-old man has sudden palpitations and lightheadedness. He is alert, with a blood pressure of 112/70. His 12-lead electrocardiogram is shown. Which drug is the most appropriate?",
  [["Intravenous procainamide",
    "Correct. The tracing shows a very fast, irregular rhythm with wide complexes of changing width, which is atrial fibrillation conducting with Wolff-Parkinson-White (pre-excited atrial fibrillation). He is alert with a blood pressure of 112/70, and in this setting intravenous procainamide is used, never adenosine."],
   ["Adenosine",
    "Adenosine must never be used when atrial fibrillation runs with Wolff-Parkinson-White; it is first line only for ordinary orthodromic reentry. His irregular, wide-complex rhythm of changing width is pre-excited atrial fibrillation. Tell: irregular wide complexes in a young man with palpitations rule adenosine out and point to procainamide.", "confused mechanism or drug class"],
   ["Intravenous beta blocker",
    "Intravenous rate control is the step for ordinary, stable atrial fibrillation with rapid ventricular response, which has narrow complexes. His irregular, wide complexes of changing width show conduction down an accessory pathway, which is treated with intravenous procainamide. Tell: wide, irregular and very fast means pre-excited fibrillation, not routine rate control.", "competing diagnosis"],
   ["Intravenous lidocaine",
    "Lidocaine is not the listed drug for this rhythm. The look-alike wide rhythm, ventricular tachycardia, is regular at 150 to 200, whereas this one is irregular with rates approaching 300, which marks atrial fibrillation with Wolff-Parkinson-White, treated with intravenous procainamide. Tell: irregularity separates the two.", "competing diagnosis"]],
  "%s, Slides 37, 52, 53" % DECK1, "agent/regimen", "treatment",
  9, "Twelve-lead electrocardiogram of a very rapid, irregular rhythm with wide complexes whose width and height vary from beat to beat", "Arrhythmias I, slide 52"),

# 10 -- junctional rhythm in an athlete -> diagnosis
V(JUN, IO_V,
  "A 30-year-old marathon runner has no symptoms. A lead II tracing taken at rest is shown; the rate is 48. Which is the most likely diagnosis?",
  [["Junctional rhythm",
    "Correct. The lead II tracing shows evenly spaced, narrow QRS complexes at 48 with no P wave before any of them because the P waves are hidden in the QRS: a junctional rhythm, usually 40 to 60. It can be seen in healthy people with increased vagal tone, such as this well-conditioned runner, and needs no treatment when asymptomatic."],
   ["Sinus bradycardia",
    "Sinus bradycardia, which is also seen in conditioned athletes, keeps a uniform P wave before every QRS with a PR of 0.12 to 0.20 seconds. This tracing shows no P wave before any complex. Tell: same slow rate in the same kind of patient, so look for the P wave; hidden P waves mean junctional.", "ruled out by a stated finding"],
   ["Third-degree block",
    "Complete atrioventricular block is one cause of a junctional rhythm, and then a permanent pacemaker is needed, but nothing here suggests block: he is an asymptomatic runner with increased vagal tone. The tracing shows regular narrow complexes at 48 with hidden P waves. Tell: the question asks for the rhythm on the strip, and that is junctional.", "competing diagnosis"],
   ["Atrial fibrillation",
    "Atrial fibrillation is irregularly irregular with absent P waves, often at 110 to 160. These complexes are slow, at 48, and evenly spaced. Tell: both lack visible P waves, but a regular slow rhythm is junctional, while fibrillation is irregularly irregular.", "competing diagnosis"]],
  "%s, Slides 62, 63, 64" % DECK1, "test finding", "diagnosis",
  10, "Lead II rhythm strip of five narrow complexes at a slow, regular rate, each followed by a T wave, with no P wave visible before any complex", "Arrhythmias I, slide 63"),

# 11 -- Mobitz type I -> diagnosis
V(AVB, IO_V,
  "A 58-year-old man who takes a beta blocker has an irregular pulse at a routine visit. He has no symptoms, and his rhythm strip is shown. Which is the most likely diagnosis?",
  [["Mobitz type I block",
    "Correct. The PR grows longer beat by beat until a P wave is not followed by a QRS, then the cycle restarts, which explains the irregular pulse: second-degree Mobitz type I (Wenckebach) block. Beta blockers are a named cause, and since he has no symptoms, the block itself needs no treatment."],
   ["Mobitz type II block",
    "Mobitz type II keeps a constant PR before randomly dropped QRS complexes. On this strip the PR lengthens progressively before each drop. Tell: a lengthening PR before the drop is type I; a constant PR is type II.", "competing diagnosis"],
   ["First-degree block",
    "First-degree block is a long but constant PR with every P wave conducted. This strip has a P wave that is not followed by a QRS, after the PR has lengthened. Tell: any dropped beat moves the rhythm beyond first degree.", "ruled out by a stated finding"],
   ["Third-degree block",
    "Third-degree block shows no relationship between P waves and QRS complexes. On this strip the conducted beats keep a PR that lengthens in a repeating pattern, so the atria and ventricles are still linked. Tell: a predictable PR pattern rules out complete block.", "competing diagnosis"]],
  "%s, Slides 7, 8, 9" % DECK2, "test finding", "diagnosis",
  11, "Rhythm strip with small upright P waves and narrow complexes in groups, with a gap where one P wave stands alone", "Arrhythmias II, slide 8"),

# 12 -- Mobitz type II, symptomatic -> transcutaneous pacing
V(AVB, IO_V,
  "A 76-year-old woman is brought in after fainting twice today. She is pale, with a blood pressure of 84/50, and her lead II rhythm strip is shown. Which is the most appropriate emergent treatment?",
  [["Transcutaneous pacing",
    "Correct. P waves at a steady rate with a constant PR, then a P wave with no QRS, is Mobitz type II block. Fainting twice today with a blood pressure of 84/50 makes her unstable, so she needs emergent treatment: atropine, epinephrine or transcutaneous pacing, which bridges her to a permanent pacemaker."],
   ["Permanent pacemaker",
    "A permanent pacemaker is the definitive treatment for Mobitz type II, but with two faints today and a blood pressure of 84/50, she first needs emergent transcutaneous pacing to bridge her there. Tell: 'emergent' points to the temporary measure, 'definitive' to the permanent one.", "wrong stage or severity"],
   ["Adenosine",
    "Adenosine is not among the treatments for heart block, and it would not raise a slow rate. This slow rhythm with dropped QRS complexes is Mobitz type II, and an unstable patient needs transcutaneous pacing. Tell: a slow, blocked rhythm with hypotension needs pacing.", "confused mechanism or drug class"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion shocks an unstable tachycardia with a pulse. This is a slow rhythm with dropped QRS complexes from Mobitz type II, which needs pacing. Tell: pace the slow, shock the fast.", "confused mechanism or drug class"]],
  "%s, Slides 11, 14" % DECK2, "first-line", "next step",
  12, "Lead II rhythm strip with regular small P waves and narrow complexes; at one point a P wave appears with no complex after it, leaving a long gap", "Arrhythmias II, slide 11"),

# 13 -- third-degree block -> describe
V(CHB, IO_V,
  "An 81-year-old man reports dizziness and two fainting spells. His pulse is 36, and his rhythm strip is shown, with arrows marking R waves and P waves. Which description best fits this tracing?",
  [["P waves and QRS complexes at unrelated rates",
    "Correct. The P waves march at their own regular rate and the slow, wide QRS complexes at another, with no fixed relationship: complete dissociation of the atria from the ventricles, third-degree (complete) block, with a ventricular rate usually under 40. His syncope carries an increased risk of sudden death."],
   ["PR lengthens until a QRS is dropped",
    "Progressive PR lengthening before a dropped QRS is Mobitz type I. Here the P waves keep no consistent relationship to the QRS complexes at all. Tell: an orderly lengthening pattern is type I; no pattern at all is complete block.", "competing diagnosis"],
   ["Constant PR with an occasional dropped QRS",
    "A constant PR with an occasional dropped QRS is Mobitz type II. On this strip the distance from each P wave to the next QRS changes every beat, and most P waves are not followed by a QRS. Tell: if no PR repeats, it is not second-degree block.", "competing diagnosis"],
   ["Every P wave conducted with a long PR",
    "A long, constant PR with every P wave conducted is first-degree block. Here most P waves are not followed by a QRS, and P waves and QRS complexes run at different rates. Tell: far more P waves than QRS complexes rules out first degree.", "competing diagnosis"]],
  "%s, Slides 15, 16" % DECK2, "test finding", "describe",
  13, "Rhythm strip with regularly spaced P waves (upward arrows) and slower complexes (downward arrows) that fall at varying distances from the P waves", "Arrhythmias II, slide 16"),

# 14 -- left bundle branch block -> diagnosis
V(BBB, IO_V,
  "A 69-year-old woman with long-standing hypertension has a preoperative 12-lead electrocardiogram, which is shown. The QRS lasts 0.16 seconds. Which is the most likely diagnosis?",
  [["Left bundle branch block",
    "Correct. A QRS of 0.16 seconds with a deep, dominant S wave in V1 (rS pattern) and broad, upright, monophasic lateral complexes without Q waves in I, V5 and V6 is left bundle branch block. Chronic hypertension, her long-standing condition, is a named cause."],
   ["Right bundle branch block",
    "Right bundle branch block gives an rsR' pattern ('bunny ears') in V1 to V3 and a slurred S wave in I and aVL. Here V1 to V3 are deep and downward. Tell: bunny ears in V1 mean right; a deep S in V1 means left.", "competing diagnosis"],
   ["Ventricular tachycardia",
    "Ventricular tachycardia is a regular wide rhythm at 100 to 250 with no P waves. This preoperative tracing shows wide complexes at a normal rate with a deep S wave in V1, the pattern of a bundle branch block. Tell: wide at a normal rate means slowed conduction, not tachycardia.", "competing diagnosis"],
   ["Wolff-Parkinson-White syndrome",
    "This tracing does not show a pre-excitation pattern; its deep, dominant S waves in V1 and broad, upright lateral complexes are a bundle branch block. Tell: a QRS over 0.12 seconds with a deep S in V1 and no lateral Q waves is left bundle branch block.", "competing diagnosis"]],
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
    "Correct. Wide complexes that keep changing shape are polymorphic ventricular tachycardia, and with a normal QT and crushing chest pain, acute ischemia is the most common cause. Even though she is awake with a pulse, polymorphic tachycardia is never truly stable, so she is defibrillated, then sent for urgent coronary angiography."],
   ["Synchronized cardioversion",
    "Synchronized cardioversion is for unstable monomorphic ventricular tachycardia with a pulse. Her strip shows complexes that keep changing shape, so the rhythm is polymorphic and is defibrillated. Tell: a changing QRS shape means an unsynchronized shock.", "competing diagnosis"],
   ["Intravenous amiodarone alone",
    "Intravenous amiodarone may be added after the shock, but drug therapy alone is for stable monomorphic ventricular tachycardia. Polymorphic tachycardia is never truly stable, even in a patient who is awake. Tell: a polymorphic strip means defibrillation first.", "wrong stage or severity"],
   ["Intravenous magnesium",
    "Intravenous magnesium breaks torsades de pointes, the polymorphic tachycardia of a prolonged QT. Her QT was normal an hour ago, and polymorphic tachycardia without a long QT is most often from acute ischemia, so she is defibrillated. Tell: magnesium needs a long QT.", "ruled out by a stated finding"]],
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
    "Adenosine is not among the torsades de pointes treatments: intravenous magnesium for a conscious patient, defibrillation if unstable, and lidocaine as the one antiarrhythmic that can be used. Her twisting polymorphic rhythm on a QT-prolonging drug calls for magnesium.", "competing diagnosis"]],
  "%s, Slides 41, 47" % DECK2, "agent/regimen", "treatment",
  17, "Rhythm strip of a rapid, wide-complex rhythm whose complexes grow taller, shrink, then grow again, as if turning around the baseline", "Arrhythmias II, slide 41"),

# 18 -- coarse ventricular fibrillation -> defibrillation
V(ARR, IO_V,
  "A 62-year-old man collapses in a hospital hallway. He is unresponsive with no pulse, and cardiopulmonary resuscitation is started. His monitor strip is shown. Which is the most important next step?",
  [["Defibrillation",
    "Correct. Chaotic, uncoordinated activity with no organized QRS complexes and no pulse is ventricular fibrillation. It is treated as cardiac arrest: defibrillation (unsynchronized cardioversion) as soon as possible, then 2 minutes of cardiopulmonary resuscitation, with epinephrine every 3 to 5 minutes and amiodarone if it persists."],
   ["Synchronized cardioversion",
    "Synchronized cardioversion times the shock to a QRS complex, so it is for a tachycardia with a pulse. Ventricular fibrillation has no QRS to time to and no pulse, so it needs defibrillation. Tell: no QRS and no pulse mean an unsynchronized shock.", "confused mechanism or drug class"],
   ["Intravenous amiodarone",
    "Intravenous amiodarone is added when ventricular fibrillation persists after shocks and epinephrine. The first priority is defibrillation as soon as possible. Tell: shock first; antiarrhythmics come later.", "wrong stage or severity"],
   ["Transcutaneous pacing",
    "Transcutaneous pacing is the emergent treatment for unstable bradycardia from high-grade block. This pulseless, chaotic rhythm is ventricular fibrillation and needs defibrillation. Tell: a pulseless, chaotic strip is shocked, not paced.", "confused mechanism or drug class"]],
  "%s, Slides 48, 49, 50" % DECK2, "first-line", "next step",
  18, "Rhythm strip of continuous, irregular, low-to-medium waves with no recognizable P waves or complexes", "Arrhythmias II, slide 49"),

# 19 -- asystole -> compressions and epinephrine
V(ARR, IO_V,
  "A 77-year-old woman is found unresponsive and pulseless, and chest compressions are started. Her monitor strip is shown, and the same flat tracing appears in every lead. Which is the most appropriate next step?",
  [["Compressions and epinephrine",
    "Correct. A flat tracing in every lead, with no P waves or QRS complexes, is asystole, which is unshockable. High-quality chest compressions and epinephrine 1 mg (1:10,000) by intravenous or intraosseous push every 3 to 5 minutes are the mainstays, early intubation is considered, and the prognosis is poor."],
   ["Defibrillation",
    "Defibrillation treats ventricular fibrillation and pulseless ventricular tachycardia. A flat tracing in every lead is asystole, which is unshockable. Tell: a flat line is never shocked; compressions and epinephrine are the treatment.", "competing diagnosis"],
   ["Synchronized cardioversion",
    "Synchronized cardioversion needs a QRS complex to time the shock to and is for a patient with a pulse. Asystole has neither and is unshockable. Tell: with no QRS and no pulse, the answer is compressions and epinephrine.", "confused mechanism or drug class"],
   ["Intravenous amiodarone",
    "Amiodarone is for ventricular fibrillation or pulseless ventricular tachycardia that persists after shocks. Asystole is treated with high-quality compressions and epinephrine. Tell: antiarrhythmics belong to the shockable side of the arrest algorithm.", "confused mechanism or drug class"]],
  "%s, Slides 52, 53, 55" % DECK2, "first-line", "next step",
  19, "Rhythm strip with a nearly flat line across the whole page and no complexes", "Arrhythmias II, slide 53"),
]

check_strips(QUESTIONS)
