# -*- coding: utf-8 -*-
# PDM I Lecture 16 (Pericardial Disease, Electrolytes, Drug Effects, and Special ECG Patterns;
# Scott Mathis, EMS educator, First Response Training Group -- title slide) -- pool A: the STRIP and
# 12-LEAD questions. Each shows a picture from the deck (tools/pdm_e3_l15_l16_images.py; baked-in
# labels and machine readings cropped off the quiz copies), cites its slide, and asks the rhythm,
# the pattern, the finding or what it means. EKG rhythm and pattern naming is the one place this
# class asks for a diagnosis (her words, Lecture 1). Pool B is the text pool.
#
# Each picture is used by at most two questions with different asks; the partition puts at most one
# question per picture in each set.
#
# TRUTH NOTES, keyed to what is medically true (truth_wins_on_conflict), discrepancy noted in guide:
#   - Digoxin: slide 47 (and the recording) say Na+/K+-ATPase inhibition INCREASES intracellular
#     potassium. It does the reverse: the pump fails, so intracellular sodium (then calcium) rises
#     and potassium is left OUTSIDE the cell (hyperkalemia in acute toxicity). No key here depends on
#     the potassium direction; the mechanism is keyed only as "inhibits the sodium-potassium pump".
#   - Tricyclic overdose: slide 49 lists QT prolongation and tachycardia. True, but the hallmark
#     sodium-channel sign is a wide QRS (the slide's own tracing shows it). Nothing here keys QT
#     prolongation as "the hallmark". The slide's mechanism ("fast Na+ channel blockade leading to a
#     delay in outflow of K+, results in QT prolongation") conflates the two channels: sodium-channel
#     blockade widens the QRS, potassium-channel blockade prolongs the QT. No explanation repeats it
#     and no stem ties the QT to "the channel blockade" (2026-10-08 fact-check).
#   - Unknown accessory pathway (slide 31): the slide says pharmacological or electrical
#     cardioversion is used "to slow down the rate and look for delta waves". Cardioversion ENDS the
#     tachycardia, the delta wave is looked for on the sinus tracing afterwards, and an undiagnosed
#     wide regular tachycardia is treated as ventricular tachycardia until proven otherwise (nodal
#     blocking drugs can be harmful with an accessory pathway). Keyed: find delta waves in sinus
#     rhythm.
#   - Hypothermia: slide 16 says the changes are "not linked directly to the temperature" but to
#     acidosis. Osborn-wave size does track the degree of cooling, so that sentence is not keyed.
#   - Magnesium: slide 46 says clinical-range magnesium changes cause no ECG change; low magnesium
#     is in fact tied to QT prolongation and torsades (the lecturer said so too). Not keyed.
#
# KEYS ARE WRITTEN SHORT ON PURPOSE. Correct answer is ALWAYS written first (c=0).
SRC = "16. EKG Pericarditis Electrolytes and Other Abnormalities.pptx"
IMG = "pdm-exam-3-quiz-images/"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Recognize ECG findings associated with: Benign Early Repolarization (BER), acute pericarditis, long QT syndrome"
IOB = "Compare and contrast ECG findings associated with: BER, acute pericarditis, STEMI patterns"
IOC = "Recognize ECG changes associated with: hyperkalemia, hypokalemia, hypercalcemia, hypocalcemia"
IOD = "Compare and contrast ECG manifestations of electrolyte abnormalities."
IOE = "Recognize ECG findings associated with: COPD/COLD, pulmonary embolism, hypothermia"
IOF = "Recognize ECG changes associated with: digoxin toxicity, amiodarone toxicity, tricyclic antidepressant toxicity"
IOG = "Recognize common pacemaker rhythms and pacing artifacts."
# Deck content with no syllabus objective of its own (the lecture title's "Special ECG Patterns"):
TPX = "Topic — Preexcitation and accessory pathway tachycardias"
TTH = "Topic — Thyroid disorders"

ALT12 = "Twelve-lead electrocardiogram on grid paper, with each lead labeled"


# Which slide each quiz picture was taken from (tools/pdm_e3_l15_l16_images.py). The caption under
# a picture names THAT slide; when the fact the question tests sits on a different slide, the cite
# names both.
IMG_SLIDE = {
    "16-12-lead-case-a.jpg": 11,
    "16-12-lead-case-b.jpg": 12,
    "16-12-lead-case-c.jpg": 17,
    "16-12-lead-case-d.jpg": 50,
    "16-12-lead-case-e.jpg": 8,
    "16-12-lead-case-f.jpg": 15,
    "16-12-lead-case-g.jpg": 19,
    "16-12-lead-case-h.jpg": 41,
    "16-12-lead-case-i.jpg": 45,
    "16-12-lead-case-j.jpg": 32,
    "16-12-lead-case-k.jpg": 49,
    "16-12-lead-case-l.jpg": 35,
    "16-12-lead-case-m.jpg": 6,
    "16-12-lead-case-n.jpg": 29,
    "16-12-lead-case-o.jpg": 28,
    "16-12-lead-case-p.jpg": 43,
    "16-12-lead-case-q.jpg": 14,
    "16-12-lead-case-r.jpg": 36,
    "16-lead-v4-strip-a.jpg": 7,
    "16-lead-v6-strip-a.png": 9,
    "16-lead-v6-strip-b.png": 9,
    "16-leads-v4-v6-strip-a.jpg": 38,
    "16-rhythm-strip-a.jpg": 47,
    "16-rhythm-strip-b.jpg": 33,
    "16-single-complex-a.jpg": 16,
    "16-v1-v3-sketch-a.jpg": 11,
}


def Q(topic, io, slot, q, key, dists, cite, img=None, alt=None):
    opts = [list(key)] + [list(d) for d in dists]
    r = {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": cite}
    if img:
        n = IMG_SLIDE[img]
        r["img"] = IMG + img
        r["alt"] = alt or ALT12
        r["slide"] = "Slide %d" % n
        if not cite.endswith(", Slide %d" % n):
            r["cite"] = cite + "; tracing from Slide %d" % n
    return r


POOL_A = [

# ------------------------------------------------ case-m: pericarditis (slide 6)
Q("Pericarditis", IOA, "name",
  "A 34-year-old man has had chest pain for two days. His 12-lead is shown. Which diagnosis best fits the tracing?",
  ("Acute pericarditis",
   "Correct. Global concave ST elevation with PR-segment depression, PR elevation in aVR and no reciprocal ST depression outside aVR and V1 is acute pericarditis."),
  [("Inferior ST-elevation infarction",
    "An inferior infarction elevates II, III and aVF with reciprocal depression in I and aVL; this elevation is global and concave with no reciprocal changes."),
   ("Benign early repolarization",
    "Early repolarization also shows global concave elevation, but not the PR-segment depression seen here; it carries J-point notching instead."),
   ("Brugada syndrome",
    "Brugada changes are isolated to V1 to V3 (coved or saddleback elevation); this tracing's elevation is global.")],
  c(6), "16-12-lead-case-m.jpg"),

Q("Pericarditis", IOA, "finding",
  "A 29-year-old woman has the 12-lead shown, with global concave ST elevation. Which finding in lead aVR supports pericarditis?",
  ("PR-segment elevation",
   "Correct. Pericarditis inflames the atria too, so the PR segment is depressed in most leads and elevated in aVR, alongside global concave ST elevation."),
  [("ST-segment elevation",
    "aVR is one of the two leads where pericarditis may show ST depression; elevation in aVR is not its sign."),
   ("A pathologic Q wave",
    "Q waves anywhere on the tracing argue against pericarditis and mean an acute infarction must be considered."),
   ("A delta wave",
    "A delta wave is the slurred QRS upstroke of preexcitation; it has nothing to do with pericardial inflammation.")],
  c(6), "16-12-lead-case-m.jpg"),

# ------------------------------------------------ case-e: benign early repolarization (slide 8)
Q("Benign early repolarization", IOA, "name",
  "A healthy 22-year-old male athlete has a routine 12-lead, shown here. Which interpretation best fits?",
  ("Benign early repolarization",
   "Correct. Global concave ST elevation with terminal QRS notching (J waves), large T waves and no reciprocal depression outside aVR and V1 in a healthy young man is benign early repolarization."),
  [("Acute pericarditis",
    "Pericarditis shares the global concave elevation but adds PR-segment depression and PR elevation in aVR, which this tracing lacks."),
   ("Anterior ST-elevation infarction",
    "An infarction gives localized elevation in contiguous leads with reciprocal depression, not this diffuse concave pattern in a healthy athlete."),
   ("Brugada syndrome, type 1",
    "Type 1 Brugada is coved (convex) elevation isolated to V1 to V3; this elevation is concave and widespread.")],
  c(8), "16-12-lead-case-e.jpg"),

Q("Benign early repolarization", IOA, "significance",
  "A 24-year-old man's 12-lead is shown: concave ST elevation with notched J points and no reciprocal depression. What clinical significance does this pattern carry?",
  ("None; it is a normal variant",
   "Correct. Benign early repolarization, also called normal variant ST elevation, is seen mostly in young men and has no clinical significance."),
  [("It signals an evolving infarction",
    "An infarction shows localized elevation with reciprocal depression; diffuse concave elevation with J waves and no reciprocal change is the benign variant."),
   ("It predicts sudden cardiac death",
    "Arrhythmia risk belongs to Brugada syndrome, an inherited arrhythmogenic disease with V1 to V3 changes, not to benign early repolarization."),
   ("It indicates pericardial inflammation",
    "Pericardial inflammation adds PR-segment depression; benign early repolarization has no clinical significance.")],
  c(7), "16-12-lead-case-e.jpg"),

# ------------------------------------------------ V4 J-wave notch (slide 7)
Q("Benign early repolarization", IOA, "finding",
  "A healthy 25-year-old man's lead V4 is shown. What is the circled notch at the end of the QRS called?",
  ("A J wave",
   "Correct. Terminal QRS notching in benign early repolarization is known as the J wave (also the fishhook sign, or Osborn wave)."),
  [("A delta wave",
    "A delta wave is a slur at the start of the QRS from preexcitation; this notch sits at the end."),
   ("A U wave",
    "A U wave follows the T wave and is prominent in hypokalemia; this notch is at the junction of the QRS and ST segment."),
   ("A pathologic Q wave",
    "A Q wave is the first negative deflection of the QRS; this is a positive notch at its end.")],
  c(7), "16-lead-v4-strip-a.jpg", "Lead V4 rhythm strip with one area circled in red"),

# ------------------------------------------------ V6 ratio strips (slide 9)
Q("Pericarditis versus early repolarization", IOB, "ratio",
  "A 27-year-old man has global concave ST elevation. In lead V6, shown here, the blue box marks the ST elevation and the red box the T-wave height. Which diagnosis does this ratio favor?",
  ("Early repolarization",
   "Correct. In V6 the ST elevation is well under a quarter of the T-wave amplitude. An ST/T ratio under 25% suggests benign early repolarization: more T wave than ST elevation."),
  [("Acute pericarditis",
    "Pericarditis gives an ST/T ratio above 25% in V6, more ST elevation than T wave; here the T wave dwarfs the ST segment."),
   ("Anterior infarction",
    "The V6 ratio is used to separate the two benign-looking mimics, pericarditis and early repolarization; it does not diagnose an infarction."),
   ("Hyperkalemia",
    "Hyperkalemia's early sign is peaked, symmetric T waves without the diffuse concave ST elevation that the V6 ratio is used for.")],
  c(9), "16-lead-v6-strip-a.png", "Lead V6 rhythm strip with a blue box and a red box drawn over one beat"),

Q("Pericarditis versus early repolarization", IOB, "ratio",
  "A 31-year-old woman has global concave ST elevation. Her lead V6 is shown, with the ST elevation boxed in blue and the T-wave height in red. Which diagnosis does the ratio favor?",
  ("Acute pericarditis",
   "Correct. The ST elevation is about half the T-wave height. An ST/T ratio above 25% in V6 suggests pericarditis: more ST elevation than T wave (the V6 phenomenon)."),
  [("Benign early repolarization",
    "Early repolarization gives a V6 ST/T ratio under 25%, with much more T wave than ST elevation; this ratio is higher."),
   ("Brugada syndrome",
    "Brugada changes are isolated to V1 to V3; the V6 ratio separates pericarditis from early repolarization."),
   ("Hypercalcemia",
    "Hypercalcemia shortens the ST segment until the T wave sits against the QRS; it does not raise the ST/T ratio.")],
  c(9), "16-lead-v6-strip-b.png", "Lead V6 rhythm strip with a blue box and a red box drawn over one beat"),

# ------------------------------------------------ Brugada type 1 (slide 11)
Q("Brugada syndrome", IOB, "name",
  "A 30-year-old man of Southeast Asian descent fainted at rest. His 12-lead is shown. Which diagnosis fits the pattern in V1 and V2?",
  ("Type 1 Brugada pattern",
   "Correct. Coved (convex) ST elevation isolated to V1 to V3 in a young man of Southeast Asian descent is the type 1, coved-shaped Brugada pattern."),
  [("Type 2 Brugada pattern",
    "Type 2 is the saddleback shape, with the ST segment dipping before the T wave; these right precordial leads are coved."),
   ("Anteroseptal infarction",
    "An anteroseptal infarction elevates V1 to V4 in a patient with ischemic symptoms; the coved shape confined to V1 to V3 in a young man is Brugada."),
   ("Benign early repolarization",
    "Early repolarization is global and concave with J-point notching, not coved elevation confined to the right precordial leads.")],
  c(11), "16-12-lead-case-a.jpg"),

Q("Brugada syndrome", IOB, "mechanism",
  "A 26-year-old man's 12-lead is shown, with coved ST elevation in V1 and V2. Which structure does his inherited disease affect?",
  ("Right ventricular outflow sodium channels",
   "Correct. Brugada syndrome is an inherited arrhythmogenic disease that affects the sodium channels of the right ventricle's outflow tract."),
  [("Left ventricular potassium channels",
    "Brugada syndrome is a sodium channel disease of the right ventricular outflow tract."),
   ("An accessory atrioventricular pathway",
    "An accessory pathway (bundle of Kent) causes Wolff-Parkinson-White preexcitation, with a short PR and delta wave, not coved V1 to V3 elevation."),
   ("The pericardial sac",
    "Pericardial inflammation causes global concave ST elevation with PR depression, not right precordial coved elevation.")],
  c(10), "16-12-lead-case-a.jpg"),

# ------------------------------------------------ Brugada type 2 (slide 12)
Q("Brugada syndrome", IOB, "type",
  "A 28-year-old man's 12-lead is shown, with ST elevation in V2. Which pattern is this?",
  ("Type 2 Brugada (saddleback)",
   "Correct. Saddle-shaped (saddleback) ST elevation in V1 to V3 is type 2 Brugada; type 1 is the coved, convex shape."),
  [("Type 1 Brugada (coved)",
    "Type 1 is coved, convex elevation sloping straight down into the T wave; the saddle shape is type 2."),
   ("Acute pericarditis",
    "Pericarditis elevates the ST segment globally with PR depression, not in a saddle shape confined to V1 to V3."),
   ("Hyperkalemia",
    "Hyperkalemia shows peaked, symmetric T waves, then flattened P waves and a wide QRS; it has no saddle-shaped ST segment.")],
  c(12), "16-12-lead-case-b.jpg"),

# ------------------------------------------------ coved V1-V3 sketch (slide 11)
Q("Brugada syndrome", IOB, "shape",
  "A 32-year-old man's right precordial leads are shown. Which ST-segment shape do they show?",
  ("Coved",
   "Correct. The ST segment rises straight off the QRS and slopes down into an inverted T wave: the coved (convex) shape of type 1 Brugada, isolated to V1 to V3."),
  [("Saddleback",
    "A saddleback ST segment dips between the J point and the T wave (type 2 Brugada); these segments slope down without the dip."),
   ("Concave",
    "Concave (cupped) elevation is the shape of pericarditis and benign early repolarization, two ST-elevation infarction mimics; this is convex."),
   ("Flat",
    "These ST segments are clearly elevated off the baseline, not flat.")],
  c(11), "16-v1-v3-sketch-a.jpg", "Three right precordial leads, V1, V2 and V3, drawn on grid paper"),

# ------------------------------------------------ ventricular paced 12-lead (slide 14)
Q("Paced rhythms", IOG, "rhythm",
  "An 81-year-old woman has the 12-lead shown. Which rhythm is it?",
  ("Ventricular paced rhythm",
   "Correct. A sharp pacing spike before each wide QRS, with T waves pointing opposite the QRS (contralateral T waves) and global ST changes, is a ventricular paced rhythm."),
  [("Left bundle branch block",
    "A left bundle branch block also gives wide QRS complexes and global ST and T changes, but there is no pacing spike before each complex."),
   ("Ventricular tachycardia",
    "Ventricular tachycardia is a fast wide-complex rhythm without pacing spikes; this rate is not fast and every beat is preceded by a spike."),
   ("Wolff-Parkinson-White pattern",
    "Wolff-Parkinson-White shows a short PR interval and a slurred delta wave, not a pacing spike before each QRS.")],
  c(14), "16-12-lead-case-q.jpg"),

Q("Paced rhythms", IOG, "artifact",
  "A 78-year-old man has the 12-lead shown. What are the sharp, narrow vertical lines just before each wide QRS?",
  ("Pacing spikes",
   "Correct. Each sharp vertical line is the pacemaker's spike, the pacing artifact, followed by the wide QRS it produces in a ventricular paced rhythm."),
  [("Delta waves",
    "Delta waves are slurred, gradual upstrokes of the QRS in preexcitation; these are instantaneous vertical spikes."),
   ("P waves",
    "P waves are rounded atrial deflections; these are sharp, narrow lines that precede each paced QRS."),
   ("Osborn waves",
    "Osborn waves are notches at the end of the QRS, in hypothermia and early repolarization; these lines come before it.")],
  c(14), "16-12-lead-case-q.jpg"),

# ------------------------------------------------ LBBB global changes (slide 15)
Q("Left bundle branch block and pacing", IOB, "problem",
  "A 70-year-old man with chest pain has a left bundle branch block, shown here. Why is an ST-elevation infarction hard to locate on this tracing?",
  ("Wide QRS with global ST and T changes",
   "Correct. Left bundle branch blocks and ventricular paced rhythms cause wide QRS complexes with global ST elevation and T-wave changes, which make an ST-elevation infarction difficult to locate."),
  [("The block hides all ST segments",
    "The ST segments are still visible; the problem is that the block itself distorts them globally."),
   ("Bundle branch blocks prevent infarction",
    "A block does not protect the heart; it only makes an infarction harder to see."),
   ("The heart rate is always too fast",
    "The difficulty is the widened, distorted ventricular complex, not the rate.")],
  c(13), "16-12-lead-case-f.jpg"),

Q("Sgarbossa's criteria", IOB, "criteria",
  "A 66-year-old woman with chest pain has the left bundle branch block shown. Which criteria are used to identify an acute infarction on it?",
  ("Sgarbossa's criteria",
   "Correct. Sgarbossa's criteria are used to diagnose an acute myocardial infarction in the presence of a left bundle branch block or a ventricular paced rhythm."),
  [("The V6 ST-to-T ratio",
    "The V6 ratio separates pericarditis from benign early repolarization; it is not used for bundle branch block."),
   ("The S1Q3T3 pattern",
    "S1Q3T3 is a pattern associated with pulmonary embolism, not a set of criteria for infarction in a bundle branch block."),
   ("The 1 mm, two-lead rule alone",
    "One millimeter of elevation in contiguous leads can be a normal variant in a left bundle branch block, which is why Sgarbossa's criteria are needed.")],
  c(18), "16-12-lead-case-f.jpg"),

# ------------------------------------------------ LBBB meeting Sgarbossa (slide 19)
Q("Sgarbossa's criteria", IOB, "criteria",
  "A 58-year-old man with a known left bundle branch block has chest pain; his 12-lead is shown. Which ST change in V1 to V3 counts toward Sgarbossa's criteria?",
  ("Concordant depression of 1 mm or more",
   "Correct. Concordant ST depression of 1 mm or more in V1 to V3 is one of Sgarbossa's criteria; the others are concordant elevation of 1 mm or more and discordant elevation of 5 mm or more."),
  [("Discordant depression of any size",
    "Discordant change is expected in a left bundle branch block; in V1 to V3 the criterion is concordant depression of 1 mm or more."),
   ("Concordant elevation of half a millimeter",
    "Concordant elevation counts at 1 mm or more, in any lead with a positive QRS, not at half a millimeter."),
   ("Discordant elevation of 2 mm",
    "Discordant elevation counts only at 5 mm or more, in a lead with a negative QRS.")],
  c(18), "16-12-lead-case-g.jpg"),

Q("Sgarbossa's criteria", IOB, "criteria",
  "A 62-year-old woman with a left bundle branch block has chest pain; her 12-lead is shown. How much discordant ST elevation meets Sgarbossa's criteria?",
  ("5 mm or more",
   "Correct. Discordant ST elevation of 5 mm or more in any lead with a negative QRS complex is a Sgarbossa criterion; smaller discordant elevation can be expected in the block."),
  [("1 mm or more",
    "One millimeter is the threshold for concordant elevation; discordant elevation must reach 5 mm or more."),
   ("2 mm or more",
    "Two millimeters of discordant elevation is within what a left bundle branch block can produce; the criterion is 5 mm or more."),
   ("Any amount at all",
    "Some discordant elevation is normal for a left bundle branch block, so a threshold of 5 mm or more is used.")],
  c(18), "16-12-lead-case-g.jpg"),

# ------------------------------------------------ hypothermia (slides 16-17)
Q("Hypothermia", IOE, "finding",
  "A 75-year-old man was found outdoors on a winter night. His 12-lead is shown. What are the notches at the end of each QRS?",
  ("Osborn waves",
   "Correct. Below 32°C (90°F), Osborn (J) waves appear as notches at the end of the QRS, and they are frequently mistaken for an ST-elevation infarction."),
  [("Delta waves",
    "Delta waves are slurred upstrokes at the start of the QRS in preexcitation; these notches sit at its end."),
   ("Prominent U waves",
    "U waves follow the T wave and are a hypokalemia sign; these notches are at the junction of the QRS and ST segment."),
   ("Pacing artifacts",
    "Pacing artifacts are sharp spikes BEFORE a paced QRS, not rounded notches after it.")],
  c(16), "16-12-lead-case-c.jpg"),

Q("Hypothermia", IOE, "threshold",
  "An 80-year-old woman with hypothermia has the 12-lead shown. Below which core temperature do these notched waves typically appear?",
  ("32°C (90°F)",
   "Correct. As the temperature approaches 35°C (95°F) sinus bradycardia appears and the intervals then prolong; below 32°C (90°F) Osborn waves become apparent."),
  [("35°C (95°F)",
    "At about 35°C (95°F) the first change is sinus bradycardia; Osborn waves need cooling below 32°C (90°F)."),
   ("37°C (98.6°F)",
    "That is normal body temperature, at which no hypothermic changes occur."),
   ("39°C (102°F)",
    "That is a fever. Osborn waves are a hypothermia sign, below 32°C (90°F).")],
  c(16), "16-12-lead-case-c.jpg"),

Q("Hypothermia", IOE, "cause",
  "A 69-year-old man has a complex like the one shown in several leads, with a notch at the end of the QRS. Which condition most likely produced it?",
  ("Hypothermia",
   "Correct. The notch at the end of the QRS is an Osborn wave; it becomes apparent when the body temperature falls below 32°C (90°F)."),
  [("Hyperkalemia",
    "Hyperkalemia shows peaked, symmetric T waves, flattened P waves and a widening QRS, not a terminal notch."),
   ("Hypokalemia",
    "Hypokalemia shows T-wave flattening and prominent U waves after the T wave, not a notch at the end of the QRS."),
   ("Pulmonary embolism",
    "Pulmonary embolism shows tachycardia, a rightward axis and the S1Q3T3 pattern, not Osborn waves.")],
  c(16), "16-single-complex-a.jpg", "A single electrocardiogram complex on grid paper, with an arrow pointing to part of it"),

# ------------------------------------------------ WPW type A (slide 28)
Q("Wolff-Parkinson-White", TPX, "name",
  "A 19-year-old man has occasional palpitations. His 12-lead in sinus rhythm is shown. Which pattern does it show?",
  ("Wolff-Parkinson-White",
   "Correct. A short PR interval, a slurred upstroke of the QRS (delta wave) and a widened QRS, the diagnostic triad, is Wolff-Parkinson-White preexcitation."),
  [("Left bundle branch block",
    "A bundle branch block widens the QRS but leaves the PR interval normal and has no delta wave."),
   ("Ventricular paced rhythm",
    "A paced rhythm has a pacing spike before each wide QRS, not a short PR interval with a slurred delta wave."),
   ("Brugada syndrome",
    "Brugada changes are coved or saddleback ST elevation in V1 to V3, not a short PR with a delta wave.")],
  c(28), "16-12-lead-case-o.jpg"),

Q("Wolff-Parkinson-White", TPX, "type",
  "A 22-year-old woman's preexcitation tracing is shown, with a mostly positive QRS in V1. Where is her accessory pathway?",
  ("Between left atrium and left ventricle",
   "Correct. A left-sided Kent bundle, between the left atrium and the left ventricle, produces a QRS that is mostly positive in V1: type A Wolff-Parkinson-White."),
  [("Between right atrium and right ventricle",
    "A right-sided Kent bundle produces a mostly negative QRS in V1, type B."),
   ("Within the atrioventricular node",
    "The accessory pathway bypasses the atrioventricular node; it is a separate connection from atria to ventricles."),
   ("In the right ventricular outflow tract",
    "The right ventricular outflow tract is where Brugada syndrome's sodium channels are affected, not the site of a Kent bundle.")],
  c(26), "16-12-lead-case-o.jpg"),

# ------------------------------------------------ WPW type B (slide 29)
Q("Wolff-Parkinson-White", TPX, "type",
  "A 24-year-old man's preexcitation tracing is shown, with a mostly negative QRS in V1. Which type of Wolff-Parkinson-White is this?",
  ("Type B (right-sided pathway)",
   "Correct. A right-sided Kent bundle, between the right atrium and right ventricle, produces a QRS that is mostly negative in V1: type B."),
  [("Type A (left-sided pathway)",
    "Type A is a left-sided Kent bundle and gives a mostly positive QRS in V1."),
   ("Type 1 (coved)",
    "Type 1 and type 2 are Brugada patterns (coved and saddleback); Wolff-Parkinson-White is typed A or B."),
   ("Type 2 (saddleback)",
    "Saddleback is type 2 Brugada, an ST-segment shape in V1 to V3, not a Wolff-Parkinson-White type.")],
  c(29), "16-12-lead-case-n.jpg"),

Q("Wolff-Parkinson-White", TPX, "finding",
  "A 20-year-old woman's 12-lead is shown. What is the slurred upstroke at the start of each QRS called?",
  ("A delta wave",
   "Correct. The delta wave is a slurring of the QRS upstroke: impulses bypass the atrioventricular node through the accessory pathway and begin depolarizing the ventricles early."),
  [("A J wave",
    "A J (Osborn) wave is a notch at the end of the QRS, in hypothermia and early repolarization."),
   ("A U wave",
    "A U wave follows the T wave and is prominent in hypokalemia."),
   ("A pacing spike",
    "A pacing spike is a sharp vertical artifact before a paced QRS, not a gradual slur.")],
  c(27), "16-12-lead-case-n.jpg"),

# ------------------------------------------------ orthodromic AVRT (slide 32)
Q("Atrioventricular reentrant tachycardia", TPX, "rhythm",
  "A 23-year-old man with a known accessory pathway has sudden palpitations. His regular, narrow-complex tachycardia is shown. Which rhythm is this?",
  ("Orthodromic reentrant tachycardia",
   "Correct. Orthodromic atrioventricular reentrant tachycardia conducts down the normal pathway and back up the accessory pathway, producing a regular narrow-complex tachycardia."),
  [("Antidromic reentrant tachycardia",
    "Antidromic conduction runs down the accessory pathway first, so the ventricles depolarize abnormally and the tachycardia is wide."),
   ("Ventricular tachycardia",
    "Ventricular tachycardia is a wide-complex tachycardia; these complexes are narrow."),
   ("Ventricular paced rhythm",
    "A paced rhythm has a spike before each wide QRS and a set rate, not a narrow-complex tachycardia.")],
  c(32), "16-12-lead-case-j.jpg"),

Q("Atrioventricular reentrant tachycardia", TPX, "circuit",
  "A 27-year-old woman with an accessory pathway has the narrow-complex tachycardia shown. Which route does the circuit take?",
  ("Down the normal pathway, up the accessory",
   "Correct. In orthodromic reentry, conduction toward the ventricles (anterograde) goes through the normal pathway and returns up the accessory pathway, so the QRS stays narrow."),
  [("Down the accessory, up the normal pathway",
    "That is the antidromic circuit, which depolarizes the ventricles through the accessory pathway and produces a wide tachycardia."),
   ("Around the right ventricular outflow tract",
    "The right ventricular outflow tract is the site of Brugada syndrome's sodium-channel disease, not a reentry circuit."),
   ("Through the sinoatrial node alone",
    "Reentry needs a circuit: here the normal pathway and the accessory pathway together.")],
  c(30), "16-12-lead-case-j.jpg"),

# ------------------------------------------------ antidromic AVRT (slide 33)
Q("Atrioventricular reentrant tachycardia", TPX, "rhythm",
  "A 30-year-old man with a known accessory pathway has a regular, wide, monomorphic tachycardia, shown here. Which rhythm is most likely?",
  ("Antidromic reentrant tachycardia",
   "Correct. Antidromic atrioventricular reentrant tachycardia conducts down the accessory pathway and back up the normal pathway, producing a regular, monomorphic, wide tachycardia."),
  [("Orthodromic reentrant tachycardia",
    "Orthodromic reentry goes down the normal pathway, so its tachycardia is narrow."),
   ("Sinus tachycardia",
    "Sinus tachycardia has normal P waves before narrow QRS complexes; this is a wide-complex tachycardia."),
   ("Ventricular paced rhythm",
    "A paced rhythm shows a spike before each QRS at a programmed rate, not a wide tachycardia like this.")],
  c(33), "16-rhythm-strip-b.jpg", "Three-lead rhythm strip on grid paper at a fast rate"),

Q("Atrioventricular reentrant tachycardia", TPX, "next step",
  "A 35-year-old woman has the wide regular tachycardia shown and does not know whether she has an accessory pathway. How is the correct interpretation made?",
  ("Find delta waves in sinus rhythm",
   "Correct. The tracing alone may not separate antidromic reentry from ventricular tachycardia, which it is treated as until proven otherwise; once cardioversion restores sinus rhythm, a delta wave on that tracing reveals the pathway."),
  [("Measure the V6 ST-to-T ratio",
    "The V6 ratio separates pericarditis from early repolarization; it cannot tell antidromic reentry from ventricular tachycardia."),
   ("Apply Sgarbossa's criteria",
    "Sgarbossa's criteria find an infarction in a left bundle branch block or paced rhythm, not an accessory pathway."),
   ("Read the rate from the strip",
    "The rate alone cannot separate the two; at times the difference cannot be told from the tracing at all.")],
  c(31), "16-rhythm-strip-b.jpg", "Three-lead rhythm strip on grid paper at a fast rate"),

# ------------------------------------------------ hyperkalemia, peaked T (slide 35)
Q("Hyperkalemia", IOC, "name",
  "A 67-year-old man on dialysis feels weak. His 12-lead is shown, with tall, peaked T waves and a slow rate. Which electrolyte disturbance does it suggest?",
  ("Hyperkalemia",
   "Correct. Peaked, symmetric T waves (the early sign), flattened P waves and bradycardia are classic hyperkalemia changes on the tracing."),
  [("Hypokalemia",
    "Hypokalemia flattens the T wave and brings out prominent U waves, the opposite of tall peaked T waves."),
   ("Hypocalcemia",
    "Hypocalcemia prolongs the ST segment and QTc with a normally shaped T wave, not a peaked one."),
   ("Hypercalcemia",
    "Hypercalcemia shortens the ST segment and QTc so the T wave sits against the QRS; it does not peak the T wave.")],
  c(35), "16-12-lead-case-l.jpg"),

Q("Hyperkalemia", IOD, "early sign",
  "A 71-year-old woman with kidney failure has the 12-lead shown. Which finding on it is the early sign of her electrolyte disturbance?",
  ("Peaked T waves",
   "Correct. In hyperkalemia the peaked, symmetric T wave is the early sign; flattened P waves, a wide QRS and finally a sine wave follow as the potassium climbs."),
  [("Flattened P waves",
    "Flattened P waves are a hyperkalemia sign too, but they come later than the peaked T wave."),
   ("A wide QRS",
    "QRS widening is a later hyperkalemia change, after the peaked T waves and P-wave flattening."),
   ("A sine wave",
    "The sine wave is the last and most severe hyperkalemia pattern, not the early sign.")],
  c(34), "16-12-lead-case-l.jpg"),

# ------------------------------------------------ late hyperkalemia (slide 36)
Q("Hyperkalemia", IOD, "progression",
  "A 59-year-old man with untreated kidney failure has the 12-lead shown: very wide QRS complexes, no P waves and peaked T waves. Without treatment, which pattern comes next?",
  ("A sine wave",
   "Correct. Hyperkalemia progresses from peaked T waves to flattened P waves and a wide QRS, and finally to a sine wave, the end-stage pattern."),
  [("Prominent U waves",
    "Prominent U waves are a hypokalemia sign, the opposite disturbance."),
   ("A shortened QT interval",
    "A shortened QTc with the T wave against the QRS is the hypercalcemia pattern."),
   ("Osborn waves",
    "Osborn waves are terminal QRS notches of hypothermia, not the end stage of hyperkalemia.")],
  c(34), "16-12-lead-case-r.jpg"),

Q("Hyperkalemia", IOC, "name",
  "A 63-year-old woman on dialysis missed three sessions. Her 12-lead is shown, with very wide QRS complexes and no visible P waves. Which disturbance best explains it?",
  ("Severe hyperkalemia",
   "Correct. As potassium climbs, the P waves flatten away and the QRS widens toward a sine wave: late, severe hyperkalemia."),
  [("Hypokalemia",
    "Hypokalemia flattens T waves and brings out U waves; it does not erase the P waves and widen the QRS like this."),
   ("Hypercalcemia",
    "Hypercalcemia shortens the ST segment and QTc; it does not widen the QRS or remove the P waves."),
   ("Hypothyroidism",
    "Hypothyroidism gives low-voltage complexes with sinus bradycardia, not this very wide QRS.")],
  c(36), "16-12-lead-case-r.jpg"),

# ------------------------------------------------ hypokalemia U waves (slide 38)
Q("Hypokalemia", IOC, "finding",
  "A 45-year-old woman's leads V4 to V6 are shown. What are the arrowed waves that follow each T wave?",
  ("U waves",
   "Correct. A small wave after the T wave is a U wave. Prominent U waves, with T-wave flattening, are classic signs of hypokalemia, which prolongs repolarization."),
  [("Delta waves",
    "A delta wave slurs the start of the QRS in preexcitation; these waves come after the T wave."),
   ("Osborn waves",
    "Osborn waves are notches at the end of the QRS in hypothermia, not waves after the T wave."),
   ("Second P waves",
    "These waves follow the T wave closely in every beat; prominent waves in that position are U waves.")],
  c(38), "16-leads-v4-v6-strip-a.jpg", "Leads V4, V5 and V6 on grid paper, with red arrows pointing to part of each beat"),

Q("Hypokalemia", IOD, "name",
  "A 52-year-old man has the leads shown, with flattened T waves and the arrowed waves after them. Which electrolyte disturbance best explains this?",
  ("Hypokalemia",
   "Correct. Hypokalemia (serum potassium below 3.5 mEq/L) prolongs repolarization: T-wave flattening, prominent U waves and ST depression are its classic signs."),
  [("Hyperkalemia",
    "Hyperkalemia peaks the T wave; flattened T waves with prominent U waves are its opposite."),
   ("Hypercalcemia",
    "Hypercalcemia shortens the ST segment and QTc so the T wave hugs the QRS; it does not bring out U waves."),
   ("Hypocalcemia",
    "Hypocalcemia lengthens the ST segment but leaves the T wave normally shaped, without prominent U waves.")],
  c(37), "16-leads-v4-v6-strip-a.jpg", "Leads V4, V5 and V6 on grid paper, with red arrows pointing to part of each beat"),

# ------------------------------------------------ hypocalcemia (slide 41)
Q("Calcium disorders", IOC, "name",
  "A 48-year-old woman has the 12-lead shown: a long, flat ST segment before a normally shaped T wave. Which electrolyte disturbance does it suggest?",
  ("Hypocalcemia",
   "Correct. Hypocalcemia prolongs phase 2 of the action potential, so the ST segment lengthens while the T wave keeps a normal shape and duration, and the QTc is prolonged."),
  [("Hypercalcemia",
    "Hypercalcemia shortens the ST segment until the T wave sits against the QRS."),
   ("Hyperkalemia",
    "Hyperkalemia peaks the T wave rather than lengthening the ST segment before a normal one."),
   ("Hypokalemia",
    "Hypokalemia flattens the T wave and adds prominent U waves; the T wave here is normal.")],
  c(41), "16-12-lead-case-h.jpg"),

Q("Calcium disorders", IOD, "interval",
  "A 55-year-old man with a low serum calcium has the 12-lead shown. Which interval change accompanies his long ST segment?",
  ("A prolonged QTc",
   "Correct. Prolonging the ST segment also prolongs the QTc; with a normally shaped T wave, that is the classic hypocalcemia picture."),
  [("A shortened QTc",
    "A shortened QTc is the hypercalcemia finding, from a shortened ST segment."),
   ("A short PR interval",
    "A short PR interval belongs to preexcitation; calcium disorders act on the ST segment."),
   ("A narrowed QRS",
    "The QRS width is not what changes in hypocalcemia; the ST segment and QTc lengthen.")],
  c(40), "16-12-lead-case-h.jpg"),

# ------------------------------------------------ hypercalcemia (slide 43)
Q("Calcium disorders", IOC, "name",
  "A 64-year-old woman has the 12-lead shown, with almost no ST segment and the T wave pushed against the QRS. Which electrolyte disturbance does it suggest?",
  ("Hypercalcemia",
   "Correct. Hypercalcemia shortens phase 2 of the action potential and the ST segment, so the QTc shortens and the T wave can be pushed right against the QRS."),
  [("Hypocalcemia",
    "Hypocalcemia does the opposite, lengthening the ST segment and QTc."),
   ("Hypokalemia",
    "Hypokalemia flattens the T wave and brings out prominent U waves."),
   ("Hyperkalemia",
    "Hyperkalemia peaks the T wave and later widens the QRS; it does not erase the ST segment.")],
  c(43), "16-12-lead-case-p.jpg"),

Q("Calcium disorders", IOD, "mechanism",
  "A 60-year-old man with a high serum calcium has the 12-lead shown. Which phase of the cardiac action potential is shortened to produce it?",
  ("Phase 2",
   "Correct. Hypercalcemia shortens phase 2 (the plateau), which shortens the ST segment and the QTc; hypocalcemia prolongs the same phase."),
  [("Phase 0",
    "Phase 0 is the rapid sodium upstroke; calcium disorders act on the phase 2 plateau."),
   ("Phase 3",
    "Phase 3 is the repolarization slowed by amiodarone's potassium-channel block, which prolongs the QT; calcium acts on phase 2."),
   ("Phase 4",
    "Phase 4 is the resting phase between beats; the ST segment reflects phase 2.")],
  c(42), "16-12-lead-case-p.jpg"),

# ------------------------------------------------ hypothyroidism (slide 45)
Q("Thyroid disorders", TTH, "name",
  "A 61-year-old woman has a slow heart rate and the low-voltage 12-lead shown, with flattened T waves. Which endocrine disorder best fits it?",
  ("Hypothyroidism",
   "Correct. Hypothyroidism slows the metabolic rate and myocardial contractility: sinus bradycardia with global low-voltage QRS complexes, flattened or inverted T waves, a prolonged QTc and low P waves."),
  [("Hyperthyroidism",
    "Hyperthyroidism is a state of adrenergic hyperactivity; its commonest finding is sinus tachycardia, then atrial fibrillation."),
   ("Hypercalcemia",
    "Hypercalcemia shortens the ST segment and QTc; it does not cause global low voltage."),
   ("Hyperkalemia",
    "Hyperkalemia peaks the T wave; this tracing's T waves are flattened and its voltage is low.")],
  c(45), "16-12-lead-case-i.jpg"),

# ------------------------------------------------ digoxin bigeminy (slide 47)
Q("Digoxin toxicity", IOF, "rhythm",
  "An 82-year-old woman taking digoxin has nausea. Her rhythm strip is shown. Which rhythm is it?",
  ("Ventricular bigeminy",
   "Correct. A normal beat, then a wide premature ventricular complex, every other beat, is bigeminy; frequent premature ventricular complexes are the most common abnormality of digoxin toxicity."),
  [("Ventricular trigeminy",
    "Trigeminy places a premature beat after every two normal beats; here every other beat is premature."),
   ("Ventricular tachycardia",
    "Ventricular tachycardia is a run of consecutive wide beats; these wide beats alternate with normal ones."),
   ("Ventricular paced rhythm",
    "A paced rhythm has a pacing spike before each wide QRS and no alternating normal beats.")],
  c(47), "16-rhythm-strip-a.jpg", "A single-lead rhythm strip on grid paper"),

Q("Digoxin toxicity", IOF, "most common",
  "An 84-year-old man on digoxin has the rhythm strip shown. Which abnormality is the most common one in digoxin toxicity?",
  ("Frequent premature ventricular beats",
   "Correct. Digoxin toxicity inhibits the sodium-potassium pump and makes cells abnormally excitable; frequent premature ventricular complexes are its most common abnormality."),
  [("A delta wave with a short PR",
    "A delta wave with a short PR is Wolff-Parkinson-White preexcitation, not digoxin toxicity."),
   ("Coved ST elevation in V1 to V3",
    "Coved V1 to V3 elevation is type 1 Brugada, an inherited sodium-channel disease."),
   ("Osborn waves",
    "Osborn waves are terminal QRS notches of hypothermia and early repolarization.")],
  c(47), "16-rhythm-strip-a.jpg", "A single-lead rhythm strip on grid paper"),

# ------------------------------------------------ tricyclic overdose (slide 49)
Q("Tricyclic antidepressant toxicity", IOF, "mechanism",
  "A 23-year-old woman took an overdose of amitriptyline, a tricyclic antidepressant. Her 12-lead is shown. Which drug effect causes her fast heart rate?",
  ("Anticholinergic activity",
   "Correct. Tricyclic antidepressants' anticholinergic activity causes the tachycardia; their fast sodium-channel blockade widens the QRS (the wide complexes on this tracing), and the QT is prolonged."),
  [("Beta-receptor blockade",
    "Beta blockade slows the heart; it is one of amiodarone's actions, not the cause of tricyclic tachycardia."),
   ("Sodium-potassium pump inhibition",
    "Pump inhibition is digoxin's mechanism, with frequent premature ventricular complexes as its commonest result."),
   ("Raised serum calcium",
    "High calcium shortens the ST segment and QTc; it is not what speeds the heart in a tricyclic overdose.")],
  c(49), "16-12-lead-case-k.jpg"),

Q("Tricyclic antidepressant toxicity", IOF, "interval",
  "A 19-year-old man has the 12-lead shown after a tricyclic antidepressant overdose. Which interval change fits the overdose?",
  ("QT prolongation",
   "Correct. A tricyclic overdose prolongs the QT; its fast sodium-channel blockade also widens the QRS, as on this tracing, and its anticholinergic activity adds tachycardia."),
  [("A shortened QTc",
    "A shortened QTc is the hypercalcemia pattern; tricyclic overdose prolongs the QT."),
   ("A short PR interval",
    "A short PR interval with a delta wave is preexcitation through an accessory pathway."),
   ("A shortened ST segment",
    "A shortened ST segment is the hypercalcemia finding, from a shortened phase 2.")],
  c(49), "16-12-lead-case-k.jpg"),

# ------------------------------------------------ pulmonary embolism (slide 50)
Q("Pulmonary embolism", IOE, "pattern",
  "A 50-year-old woman has sudden severe shortness of breath with clear, equal lung sounds. Her 12-lead is shown. Which pattern on it is associated with pulmonary embolism?",
  ("S1Q3T3",
   "Correct. A deep S wave in lead I, a Q wave in lead III and an inverted T wave in lead III, the S1Q3T3 pattern, is the classic pulmonary embolism finding, with sinus tachycardia."),
  [("Coved elevation in V1 to V3",
    "Coved elevation confined to V1 to V3 is type 1 Brugada, not pulmonary embolism."),
   ("A delta wave",
    "A delta wave marks preexcitation through an accessory pathway."),
   ("Peaked T waves",
    "Peaked, symmetric T waves are the early sign of hyperkalemia.")],
  c(50), "16-12-lead-case-d.jpg"),

Q("Pulmonary embolism", IOE, "mechanism",
  "A 46-year-old man with a pulmonary embolism has the 12-lead shown, with a fast sinus rate. What causes the tachycardia?",
  ("Sympathetic activation from hypoxia",
   "Correct. Hypoxia activates the sympathetic nervous system, which leads to tachycardia; right ventricular dilation adds a rightward axis and the S1Q3T3 pattern."),
  [("Anticholinergic drug activity",
    "Anticholinergic activity explains the tachycardia of a tricyclic antidepressant overdose, not of pulmonary embolism."),
   ("An accessory pathway",
    "An accessory pathway causes reentrant tachycardias in preexcitation; this is sinus tachycardia from hypoxia."),
   ("Hyperthyroid adrenergic excess",
    "Hyperthyroidism also causes sinus tachycardia, but in pulmonary embolism the driver is hypoxia triggering sympathetic activation.")],
  c(50), "16-12-lead-case-d.jpg"),

]
