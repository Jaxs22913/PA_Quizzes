# -*- coding: utf-8 -*-
# PDM I Lecture 14 (Axis, Bundle Branch Blocks, and Chamber Enlargement, Scott Mathis) -- pool A.
# The electrical axis (definitions, the lead I and aVF method, causes), the fascicular blocks,
# and the right and left bundle branch blocks. Pool B carries atrial enlargement, ventricular
# hypertrophy, the systematic 12-lead read and the hypertrophy STEMI mimic.
#
# LECTURER: Scott Mathis, EMS educator, First Response Training Group (title slide 1, and the
# 6 October recording, three parts). The calendar names a different lecturer; the slide wins.
#
# STRIPS HEAVY. "img" questions show a 12-lead or lead tracing from the deck (extracted by
# tools/extract_pdm_l14_figures.py, every picture viewed before use, labels masked). Values in
# a stem tied to a picture are only the ones the slide itself states.
#
# SOURCE CONFLICTS, keyed to what is true and noted in the guide:
#   slide 22  the quadrant drawing's right-axis panel is drawn reversed (lead I up, aVF down).
#             The lecturer corrected it aloud twice (part 2, 42:28 and 44:31) and slide 25's
#             text is right. Keyed: right axis deviation = lead I negative, aVF positive.
#   slide 21  the causes wheel lists left ventricular hypertrophy under RIGHT axis deviation;
#             slide 36 says it causes LEFT axis deviation. Nothing here is keyed to that entry.
#   slide 21  draws the normal sector to +110 degrees; slide 20 and the recording ("negative 30
#             to 90 degrees", part 2, 31:06) give -30 to +90. Keyed: -30 to +90.
#   slides 12 and 16 say the bundle branch block QRS "is best measured in lead V1". QRS duration
#             is measured in the lead where it is widest; V1 is the lead that decides right versus
#             left. Nothing is keyed to "measured in V1" (2026-10-08 fact-check).
#   slide 6   calls left anterior fascicular block the most common intraventricular conduction
#             abnormality in acute infarction (standard sources agree); right bundle branch block
#             also occurs there, and the distractor says so.
#   slides 12 and 16 say "longer than 0.12 seconds"; the recording says ".12 seconds in duration
#             or greater" (part 2, 0:02), which is the accepted criterion. Keyed: 0.12 or longer.
#
# INCOMPLETE BUNDLE BRANCH BLOCK (objective d) is NOT in the deck or the recording, so no
# question is built on it; the guide says so.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "14. EKG Axis, BBB.pptx"
IMG = "pdm-exam-3-quiz-images/"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Define: normal axis, left axis deviation, right axis deviation"
IOB = "Determine the electrical axis of an electrocardiogram"
IOC = "Recognize ECG findings associated with bundle branch blocks: right bundle branch block, left bundle branch block"
IOD = "Compare and contrast ECG findings associated with bundle branch blocks: incomplete and complete right bundle branch block, incomplete and complete left bundle branch block"
IOE = "Recognize ECG findings associated with atrial enlargement: left atrial enlargement, right atrial enlargement"
IOF = "Compare and contrast ECG findings associated with atrial enlargement"
IOG = "Recognize ECG findings associated with: left ventricular hypertrophy, right ventricular hypertrophy"
IOH = "Compare and contrast ECG findings associated with ventricular hypertrophy"
IOI = "Discuss related anatomy and physiology of ventricular conduction abnormalities and chamber enlargement"

TWELVE = "Twelve-lead electrocardiogram"
LIMB = "Limb-lead tracings from an electrocardiogram"

AX_N, AX_L, AX_R, AX_X = "Normal axis", "Left axis deviation", "Right axis deviation", "Extreme axis deviation"
EXPL_AX = {
 AX_N: "A normal axis has a mostly positive QRS in both lead I and aVF; the normal range is -30 to +90 degrees.",
 AX_L: "Left axis deviation has lead I mostly positive and aVF mostly negative, an axis beyond -30 degrees.",
 AX_R: "Right axis deviation has lead I mostly negative and aVF mostly positive, an axis beyond +90 degrees.",
 AX_X: "Extreme axis deviation, no man's land, has both lead I and aVF mostly negative.",
}


import glob as _glob, os as _os
_QDIR = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),
                      "Principles of Diagnostic Medicine I Exam 3", "pdm-exam-3-quiz-images")


def _file(stem):
    """The extractor picks .png or .jpg by size, so pools name a strip by its stem."""
    stem = _os.path.splitext(stem)[0]
    hits = sorted(_glob.glob(_os.path.join(_QDIR, stem + ".*")))
    assert len(hits) == 1, "strip %s: %d files" % (stem, len(hits))
    return _os.path.basename(hits[0])


def Q(topic, io, slot, q, key, dists, cite, img=None, alt=TWELVE, slide=None):
    opts = [list(key)] + [list(d) for d in dists]
    r = {"topic": topic, "io": io, "slot": slot, "q": q, "opts": opts, "c": 0, "cite": c(cite)}
    if img:
        r["img"] = IMG + _file(img)
        r["alt"] = alt
        r["slide"] = "Slide %d" % (slide or cite)
    return r


def AXQ(q, key, why, cite, img, slide=None, io=IOB, topic="Determining the axis"):
    """Axis-naming question on a tracing: the four axis categories, each refuted by its own rule."""
    others = [a for a in (AX_N, AX_L, AX_R, AX_X) if a != key]
    return Q(topic, io, "axis", q, (key, "Correct. " + why),
             [(a, EXPL_AX[a] + " That is not the pattern in leads I and aVF here.") for a in others],
             cite, img=img, slide=slide)


POOL_A = [

# ---------------------------------------------------------------- axis on a tracing
AXQ("A 45-year-old woman has a routine electrocardiogram. What is her electrical axis?",
    AX_N, "The QRS is mostly positive in both lead I and aVF, so the axis falls in the normal range of -30 to +90 degrees.",
    23, "l14-axis-normal.jpg"),
AXQ("A 63-year-old man has this electrocardiogram. What is his electrical axis?",
    AX_L, "Lead I is mostly positive and aVF is mostly negative: left axis deviation.",
    24, "l14-axis-left.jpg"),
AXQ("A 58-year-old woman with lung disease has this electrocardiogram. What is her electrical axis?",
    AX_R, "Lead I is mostly negative and aVF is mostly positive: right axis deviation.",
    25, "l14-axis-right.jpg"),
AXQ("A 70-year-old man has this electrocardiogram. What is his electrical axis?",
    AX_X, "Both lead I and aVF are mostly negative: extreme axis deviation, the region called no man's land.",
    26, "l14-axis-extreme.jpg"),
AXQ("A 36-year-old woman has a screening electrocardiogram. What is her electrical axis?",
    AX_N, "Lead I and aVF are both mostly positive, a normal axis; this tracing reads as normal throughout.",
    42, "l14-normal-12-lead.jpg", slide=41),
AXQ("A 61-year-old man with chest pain has this electrocardiogram. What is his electrical axis?",
    AX_L, "Lead I is mostly positive while aVF is mostly negative: left axis deviation.",
    46, "l14-axis-left-b.jpg", slide=45),
AXQ("A 57-year-old woman has this electrocardiogram. What is her electrical axis?",
    AX_L, "Lead I is mostly positive (up) and aVF is mostly negative (down): left axis deviation.",
    50, "l14-axis-left-c.jpg", slide=49),
AXQ("A 52-year-old woman has this electrocardiogram. What is her electrical axis?",
    AX_R, "Lead I is mostly negative and aVF mostly positive: right axis deviation, here alongside peaked P waves.",
    56, "l14-rae-right-axis.png", slide=55),
AXQ("A 74-year-old man with a wide QRS has this electrocardiogram. What is his electrical axis?",
    AX_X, "Both lead I and aVF are mostly negative, which is extreme axis deviation.",
    48, "l14-rbbb-12-lead-b.jpg", slide=18),
AXQ("A 68-year-old woman with a wide QRS has this electrocardiogram. What is her electrical axis?",
    AX_L, "Lead I is mostly positive and aVF mostly negative: left axis deviation.",
    52, "l14-lbbb-12-lead-c.jpg", slide=51),
AXQ("A 66-year-old man has this electrocardiogram with a narrow QRS. What is his electrical axis?",
    AX_L, "Lead I is mostly positive and aVF mostly negative: left axis deviation, here from a left anterior fascicular block.",
    54, "l14-lafb-12-lead.jpg", slide=7),

# ---------------------------------------------------------------- axis definitions
Q("Defining the axis", IOA, "define",
  "A 40-year-old man's electrocardiogram is reviewed for axis. Which range is the normal electrical axis?",
  ("-30 to +90 degrees",
   "Correct. The normal electrical axis ranges between -30 and +90 degrees; both lead I and aVF are mostly positive."),
  [("0 to +180 degrees",
    "That range would take in most of right axis deviation. The normal axis runs from -30 to +90 degrees."),
   ("+90 to +180 degrees",
    "That is right axis deviation, where lead I turns negative and aVF stays positive."),
   ("-30 to -90 degrees",
    "That is left axis deviation, where lead I is positive and aVF negative.")],
  20),

Q("Defining the axis", IOB, "method",
  "A 55-year-old woman's electrocardiogram needs a quick axis determination. Which two leads are used?",
  ("Lead I and aVF",
   "Correct. Leads I and aVF are used to quickly determine the axis: they sit at either end of the normal sector."),
  [("Leads II and III",
    "Leads II and III add detail, but the quick method uses lead I and aVF."),
   ("Leads V1 and V6",
    "V1 and V6 are precordial leads used for bundle branch block morphology, not for the frontal axis."),
   ("Leads aVR and aVL",
    "The quick method uses lead I and aVF. aVR and aVL are not the pair it relies on.")],
  22),

Q("Defining the axis", IOA, "define",
  "A 62-year-old man's lead I QRS is mostly positive and his aVF QRS is mostly negative. Which axis is this?",
  (AX_L, "Correct. Lead I mostly positive with aVF mostly negative is left axis deviation."),
  [(AX_N, EXPL_AX[AX_N] + " Here aVF is negative."),
   (AX_R, EXPL_AX[AX_R] + " Here lead I is positive."),
   (AX_X, EXPL_AX[AX_X] + " Here lead I is positive.")],
  24),

Q("Defining the axis", IOA, "define",
  "A 48-year-old woman's lead I QRS is mostly negative and her aVF QRS is mostly positive. Which axis is this?",
  (AX_R, "Correct. Lead I mostly negative with aVF mostly positive is right axis deviation."),
  [(AX_N, EXPL_AX[AX_N] + " Here lead I is negative."),
   (AX_L, EXPL_AX[AX_L] + " Here the pattern is reversed."),
   (AX_X, EXPL_AX[AX_X] + " Here aVF is positive.")],
  25),

Q("Defining the axis", IOA, "define",
  "A 71-year-old man's QRS is mostly negative in both lead I and aVF. Which axis is this?",
  (AX_X, "Correct. Both lead I and aVF mostly negative is extreme axis deviation, the region called no man's land."),
  [(AX_N, EXPL_AX[AX_N] + " Here both are negative."),
   (AX_L, EXPL_AX[AX_L] + " Here lead I is negative too."),
   (AX_R, EXPL_AX[AX_R] + " Here aVF is negative too.")],
  26),

Q("Defining the axis", IOA, "define",
  "A 59-year-old woman's axis lies beyond -30 degrees (normal -30 to +90). Which category is this?",
  (AX_L, "Correct. Beyond -30 degrees, toward -90, is left axis deviation; the normal range ends at -30 degrees."),
  [(AX_N, "The normal axis stops at -30 degrees. An axis beyond -30 has deviated to the left."),
   (AX_R, "Right axis deviation lies beyond +90 degrees, on the opposite side of the circle."),
   (AX_X, "Extreme axis deviation lies between -90 and 180 degrees, where both lead I and aVF are negative.")],
  20),

Q("Causes of axis deviation", IOI, "cause",
  "A 64-year-old man has a new wide-complex tachycardia with extreme axis deviation. Which rhythm does that axis raise suspicion for?",
  ("Ventricular tachycardia",
   "Correct. A ventricular arrhythmia is one of the causes of extreme axis deviation; a wide-complex tachycardia in no man's land points toward ventricular tachycardia."),
  [("Sinus tachycardia",
    "Sinus tachycardia uses the normal pathway and leaves the axis normal. Extreme deviation suggests a ventricular origin."),
   ("Left anterior fascicular block",
    "Left anterior fascicular block causes left axis deviation with a narrow QRS, not a wide tachycardia in no man's land."),
   ("Right atrial enlargement",
    "Right atrial enlargement changes the P wave, not the QRS axis of a tachycardia.")],
  21),

Q("Causes of axis deviation", IOI, "cause",
  "A 69-year-old woman has new left axis deviation. Which is a listed cause of left axis deviation?",
  ("Left anterior fascicular block",
   "Correct. Left anterior fascicular block is a cause of left axis deviation, along with past inferior infarction and ventricular pacing."),
  [("Left posterior fascicular block",
    "Left posterior fascicular block causes right axis deviation: lead I negative, aVF positive."),
   ("Pulmonary embolism",
    "Pulmonary embolism strains the right heart and is listed among the causes of right axis deviation."),
   ("Dextrocardia",
    "Dextrocardia, a right-sided heart, is listed among the causes of right axis deviation.")],
  21),

Q("Causes of axis deviation", IOI, "cause",
  "A 72-year-old man with long-standing lung disease has right axis deviation. Which is a listed cause?",
  ("Chronic obstructive pulmonary disease",
   "Correct. Chronic obstructive pulmonary disease is a cause of right axis deviation; lung disease makes the right heart work harder."),
  [("Left anterior fascicular block",
    "Left anterior fascicular block produces left axis deviation, lead I up and aVF down."),
   ("Past inferior infarction",
    "A past inferior infarction is a cause of left axis deviation."),
   ("Tricuspid atresia",
    "Tricuspid atresia is listed among the causes of left axis deviation, not right.")],
  21),

Q("Causes of axis deviation", IOA, "normal-variant",
  "A 6-year-old boy has right axis deviation on a preoperative electrocardiogram. How should it be read?",
  ("It can be normal in children",
   "Correct. Right axis deviation is listed as normal in children."),
  [("It always signals heart disease",
    "Right axis deviation is listed as a normal finding in children, so in a child it does not by itself signal disease."),
   ("It means a left fascicle is blocked",
    "A left posterior fascicular block can cause right axis deviation, but in a child the axis can simply be normal."),
   ("It is caused by lead misplacement",
    "Reversed arm leads can cause it, but right axis deviation is also a normal finding in children.")],
  21),

Q("Defining the axis", IOA, "framing",
  "A 50-year-old woman asks why her axis is assessed on every 12-lead. Which factors can shift the cardiac axis?",
  ("Age, history and disease",
   "Correct. A patient's age, medical history and disease processes, chronic or acute, can affect the axis of the heart."),
  [("Paper speed and calibration",
    "Paper speed and calibration change how a tracing is drawn, not the direction of the mean electrical vector."),
   ("The P wave height and shape",
    "The axis is the direction of the QRS vector. P waves are atrial and do not set it."),
   ("The PR interval duration",
    "The PR interval reflects conduction through the atrioventricular node, not the direction of the QRS axis.")],
  20),

# ---------------------------------------------------------------- fascicular blocks
Q("Fascicular blocks", IOB, "name",
  "A 66-year-old man has this electrocardiogram with a narrow QRS. Which conduction abnormality does it show?",
  ("Left anterior fascicular block",
   "Correct. Left axis deviation (lead I up, aVF down), a q wave in lead I with an r wave in lead III, and mostly negative leads II and III with a narrow QRS: left anterior fascicular block."),
  [("Left posterior fascicular block",
    "Left posterior fascicular block gives right axis deviation, lead I negative and aVF positive. Here lead I is positive."),
   ("Left bundle branch block",
    "Left bundle branch block needs a QRS of 0.12 seconds or longer. This QRS is narrow."),
   ("Right bundle branch block",
    "Right bundle branch block needs a wide QRS with an rSR pattern in V1. This QRS is narrow.")],
  7, img="l14-lafb-12-lead.jpg"),

Q("Fascicular blocks", IOB, "name",
  "A 70-year-old woman has these limb leads with a narrow QRS. Which conduction abnormality do they show?",
  ("Left posterior fascicular block",
   "Correct. Right axis deviation (lead I mostly negative, aVF positive), an r wave in lead I with a q wave in lead III, and a positive lead III: left posterior fascicular block."),
  [("Left anterior fascicular block",
    "Left anterior fascicular block gives left axis deviation, lead I positive and aVF negative. Here lead I is negative."),
   ("Left bundle branch block",
    "Left bundle branch block is a wide-QRS block. These complexes are narrow."),
   ("Right bundle branch block",
    "Right bundle branch block is wide, with an rSR pattern in V1. These complexes are narrow.")],
  9, img="l14-lpfb-limb-leads.jpg", alt=LIMB),

Q("Fascicular blocks", IOI, "clinical",
  "A 62-year-old man develops a new intraventricular conduction abnormality. Which one is most common during an acute myocardial infarction?",
  ("Left anterior fascicular block",
   "Correct. Left anterior fascicular block, the left anterior hemiblock, is the most common intraventricular conduction abnormality during an acute myocardial infarction."),
  [("Left posterior fascicular block",
    "Left posterior fascicular block is far less common than the anterior one."),
   ("Left bundle branch block",
    "Left bundle branch block blocks all three fascicles at once. The single most common abnormality in acute infarction is the anterior fascicular block."),
   ("Right bundle branch block",
    "Right bundle branch block can also appear during an acute infarction, but the most common intraventricular conduction abnormality there is left anterior fascicular block.")],
  6),

Q("Fascicular blocks", IOB, "criteria",
  "A 67-year-old woman is suspected to have left anterior fascicular block. Which lead pattern fits?",
  ("q wave in lead I, r wave in lead III",
   "Correct. Left anterior fascicular block shows a q wave in lead I and an r wave in lead III (q1r3), with left axis deviation and negative leads II and III."),
  [("r wave in lead I, q wave in lead III",
    "An r wave in lead I with a q wave in lead III (r1q3) is left posterior fascicular block, with right axis deviation."),
   ("rSR pattern in lead V1",
    "An rSR pattern in V1 with a wide QRS is right bundle branch block, not a fascicular block."),
   ("Notched QRS in lead V6",
    "Notching in the lateral leads with a wide QRS is left bundle branch block, not a fascicular block.")],
  7),

Q("Fascicular blocks", IOI, "compare",
  "A 73-year-old man has left posterior fascicular block. How common is it compared with the anterior one?",
  ("Far less common",
   "Correct. Left posterior fascicular block, the left posterior hemiblock, is far less common than left anterior fascicular block."),
  [("Far more common",
    "It is the anterior fascicular block that is common, especially in acute infarction. The posterior one is far less common."),
   ("Equally common",
    "The two are not equally common: the posterior block is far less common than the anterior one."),
   ("Seen only in children",
    "Left posterior fascicular block is not confined to children; it is simply far less common than the anterior block.")],
  8),

Q("Fascicular blocks", IOB, "criteria",
  "A 64-year-old woman's limb leads are being read for a posterior fascicular block. Which lead has no significance in identifying it?",
  ("Lead II",
   "Correct. Lead II has no significance in identifying left posterior fascicular block; it is usually positive or biphasic."),
  [("Lead I",
    "Lead I matters: it is mostly negative in left posterior fascicular block, with an r wave."),
   ("Lead III",
    "Lead III matters: it is mostly positive, with a q wave, in left posterior fascicular block."),
   ("Lead aVF",
    "aVF matters: it is mostly positive, which with a negative lead I gives right axis deviation.")],
  9),

Q("Fascicular blocks", IOI, "anatomy",
  "A 58-year-old man is learning his conduction system. Into which three fascicles does the left bundle branch split?",
  ("Anterior, posterior and septal",
   "Correct. The left bundle arises from the His bundle and quickly splits into the posterior, anterior and interventricular septal fascicles."),
  [("Anterior, posterior and right",
    "The right bundle branch is a separate branch, not a fascicle of the left bundle. The third left fascicle is the septal one."),
   ("Superior, inferior and lateral",
    "The left bundle's fascicles are named anterior, posterior and septal."),
   ("Septal, apical and basal",
    "There are no apical or basal fascicles. The left bundle splits into anterior, posterior and septal fascicles.")],
  10),

# ---------------------------------------------------------------- bundle branch blocks on a tracing
Q("Left bundle branch block", IOC, "name",
  "A 71-year-old man has this electrocardiogram. Which conduction abnormality does it show?",
  ("Left bundle branch block",
   "Correct. A wide QRS, a negative first deflection back from the J point in V1, notched lateral QRS complexes and no lateral Q waves: left bundle branch block."),
  [("Right bundle branch block",
    "Right bundle branch block shows a positive deflection before the J point in V1 (rSR) and slurred lateral S waves. V1 here is negative."),
   ("Left anterior fascicular block",
    "Left anterior fascicular block has a narrow QRS with left axis deviation. These complexes are wide."),
   ("Left ventricular hypertrophy",
    "Hypertrophy raises voltage with a normal QRS duration. These complexes are wide, with lateral notching.")],
  13, img="l14-lbbb-12-lead-a.jpg"),

Q("Left bundle branch block", IOC, "name",
  "A 76-year-old woman has this electrocardiogram. Which conduction abnormality does it show?",
  ("Left bundle branch block",
   "Correct. Wide QRS complexes, an rS pattern in V1 whose first deflection back from the J point is negative, and notched lateral complexes without Q waves: left bundle branch block."),
  [("Right bundle branch block",
    "Right bundle branch block puts a terminal R wave in V1 and a slurred S in the lateral leads. V1 here ends negative."),
   ("Left posterior fascicular block",
    "Left posterior fascicular block has a narrow QRS with right axis deviation. These complexes are wide."),
   ("Right ventricular hypertrophy",
    "Right ventricular hypertrophy shows more R wave than S wave in V1. V1 here is a deep negative complex.")],
  14, img="l14-lbbb-12-lead-b.jpg"),

Q("Left bundle branch block", IOC, "name",
  "A 68-year-old woman has this electrocardiogram. Which conduction abnormality does it show?",
  ("Left bundle branch block",
   "Correct. The QRS is wide, V1 is an rS pattern ending negative, and the lateral leads are notched with no Q waves: left bundle branch block, here with left axis deviation."),
  [("Right bundle branch block",
    "Right bundle branch block ends V1 with a positive R wave. Here the last deflection before the J point in V1 is negative."),
   ("Left anterior fascicular block",
    "Left anterior fascicular block shares the left axis but keeps a narrow QRS. These complexes are wide."),
   ("Left atrial enlargement",
    "Left atrial enlargement changes the P wave, not the width and shape of the QRS.")],
  52, img="l14-lbbb-12-lead-c.jpg", slide=51),

Q("Right bundle branch block", IOC, "name",
  "A 59-year-old man has this electrocardiogram. Which conduction abnormality does it show?",
  ("Right bundle branch block",
   "Correct. A wide QRS with an rSR pattern in V1, a positive first deflection back from the J point, and slurred S waves in the lateral leads: right bundle branch block."),
  [("Left bundle branch block",
    "Left bundle branch block ends V1 with a negative deflection and notches the lateral leads. V1 here ends positive."),
   ("Left posterior fascicular block",
    "Left posterior fascicular block keeps a narrow QRS. These complexes are wide with an rSR in V1."),
   ("Right ventricular hypertrophy",
    "Right bundle branch block is an exclusion for the voltage diagnosis of right ventricular hypertrophy; the wide rSR in V1 is the block.")],
  19, img="l14-rbbb-12-lead-a.jpg"),

Q("Right bundle branch block", IOC, "name",
  "A 74-year-old man has this electrocardiogram. Which conduction abnormality does it show?",
  ("Right bundle branch block",
   "Correct. The QRS is wide, V1 shows an rSR pattern ending in a positive deflection, and the lateral leads carry slurred S waves: right bundle branch block."),
  [("Left bundle branch block",
    "Left bundle branch block makes V1 end negative and notches the lateral leads without slurred S waves."),
   ("Left anterior fascicular block",
    "Left anterior fascicular block is a narrow-QRS block with left axis deviation. These complexes are wide."),
   ("Left ventricular hypertrophy",
    "Left ventricular hypertrophy raises voltage with a normal duration. These complexes are wide with an rSR in V1.")],
  48, img="l14-rbbb-12-lead-b.jpg", slide=18),

Q("Left bundle branch block", IOC, "name",
  "A 72-year-old woman's QRS is 0.12 seconds or longer (normal under 0.12). Her V1 and V6 complexes are shown. Which block is this?",
  ("Left bundle branch block",
   "Correct. V1 is an rS pattern whose first deflection back from the J point is negative, and V6 is a notched R wave: left bundle branch block."),
  [("Right bundle branch block",
    "Right bundle branch block makes V1 an rSR pattern ending positive, with a slurred S wave in V6."),
   ("Left anterior fascicular block",
    "A fascicular block keeps the QRS narrow. This QRS is 0.12 seconds or longer."),
   ("Right ventricular hypertrophy",
    "Right ventricular hypertrophy puts more R wave than S wave in V1. This V1 is mostly a deep S wave.")],
  12, img="l14-lbbb-v1-v6.png", alt="Two drawn complexes, leads V1 and V6"),

Q("Right bundle branch block", IOC, "name",
  "A 67-year-old man's QRS is 0.12 seconds or longer (normal under 0.12). His V1 and V6 complexes are shown. Which block is this?",
  ("Right bundle branch block",
   "Correct. V1 is an rSR pattern whose first deflection back from the J point is positive, and V6 has a slurred S wave: right bundle branch block."),
  [("Left bundle branch block",
    "Left bundle branch block makes V1 an rS pattern ending negative, with a notched R in V6."),
   ("Left posterior fascicular block",
    "A fascicular block keeps the QRS narrow. This QRS is 0.12 seconds or longer."),
   ("Left ventricular hypertrophy",
    "Left ventricular hypertrophy gives deep S waves in V1 and tall lateral R waves at a normal duration.")],
  16, img="l14-rbbb-v1-v6.png", alt="Two drawn complexes, leads V1 and V6"),

Q("Left bundle branch block", IOC, "feature",
  "A 73-year-old woman has this electrocardiogram. Tracing back from the J point in V1, what is the first deflection you reach?",
  ("A negative deflection",
   "Correct. In left bundle branch block, the first deflection you come to traveling back from the J point in V1 is negative (an rS pattern)."),
  [("A positive deflection",
    "A positive first deflection back from the J point in V1 is the rule for right bundle branch block. This V1 ends negative."),
   ("A flat, isoelectric segment",
    "The QRS in V1 here is a deep negative complex; tracing back from the J point lands on it, not on a flat segment."),
   ("A pacer spike",
    "There are no pacer spikes on this tracing. The first deflection back from the J point in V1 is negative.")],
  13, img="l14-lbbb-12-lead-a.jpg"),

Q("Right bundle branch block", IOC, "feature",
  "A 60-year-old man has this electrocardiogram. Tracing back from the J point in V1, what is the first deflection you reach?",
  ("A positive deflection",
   "Correct. In right bundle branch block, traveling back from the J point in V1 the very first deflection is positive, the terminal R of the rSR pattern."),
  [("A negative deflection",
    "A negative first deflection back from the J point in V1 is the rule for left bundle branch block."),
   ("A flat, isoelectric segment",
    "Tracing back from the J point lands on the QRS itself, and here its last wave is a positive R."),
   ("A pacer spike",
    "There are no pacer spikes on this tracing. The first deflection back from the J point in V1 is positive.")],
  19, img="l14-rbbb-12-lead-a.jpg"),

Q("Left bundle branch block", IOC, "feature",
  "A 78-year-old man has this electrocardiogram. What do its lateral leads (I, aVL, V5, V6) lack?",
  ("Q waves",
   "Correct. In left bundle branch block the septal fascicle is blocked, so the septum's normal Q wave is lost from the lateral leads."),
  [("R waves",
    "The lateral leads in left bundle branch block have tall, often notched R waves. It is the Q wave that is missing."),
   ("T waves",
    "T waves are present after each complex. The missing wave is the septal Q wave."),
   ("P waves",
    "P waves are atrial and appear across the leads in sinus rhythm. The lateral leads lack Q waves.")],
  14, img="l14-lbbb-12-lead-b.jpg"),

Q("Right bundle branch block", IOC, "feature",
  "A 74-year-old woman has this electrocardiogram. Which lateral-lead finding supports the diagnosis?",
  ("Slurred S waves",
   "Correct. Right bundle branch block puts slurred S waves in the lateral leads (I, aVL, V5, V6), the double QRS phenomenon, best seen in V6."),
  [("Notched R waves",
    "Notched lateral R waves without Q waves are the left bundle branch block pattern."),
   ("Absent Q waves",
    "Loss of lateral Q waves belongs to left bundle branch block, where the septal fascicle is blocked."),
   ("Tall peaked P waves",
    "Tall peaked P waves in the limb leads are right atrial enlargement, not a bundle branch block finding.")],
  18, img="l14-rbbb-12-lead-b.jpg"),

# ---------------------------------------------------------------- bundle branch block criteria
Q("Bundle branch block criteria", IOC, "criteria",
  "A 65-year-old man's QRS looks wide. Which QRS duration is required to call a bundle branch block?",
  ("0.12 seconds or longer",
   "Correct. A bundle branch block needs a QRS of 0.12 seconds or longer, three small boxes; a normal QRS is under 0.12."),
  [("0.20 seconds or longer",
    "That is far wider than the threshold. A QRS of 0.12 seconds, three small boxes, is enough."),
   ("Under 0.12 seconds",
    "Under 0.12 seconds is a normal QRS. A bundle branch block widens it to 0.12 or more."),
   ("0.04 seconds or longer",
    "That is a single small box, a normal width. The bundle branch block threshold is 0.12 seconds.")],
  12),

Q("Bundle branch block criteria", IOC, "criteria",
  "A 70-year-old woman has a bundle branch block. Which lead decides whether the block is right or left?",
  ("V1",
   "Correct. Find the J point in V1 and travel backward: if the first deflection you reach is positive the block is right-sided, and if it is negative the block is left-sided."),
  [("Lead II",
    "Lead II is the rhythm lead; the side of a bundle branch block is read in V1, by the first deflection before the J point."),
   ("aVR",
    "aVR does not decide the side of the block; V1 does, through the direction of the deflection just before the J point."),
   ("V4",
    "V4 does not decide the side; V1 decides it, and V6 is where the double QRS phenomenon is best seen.")],
  16),

Q("Bundle branch block criteria", IOD, "compare",
  "A 69-year-old man has a QRS of 0.14 seconds (normal under 0.12). Which V1 finding separates a right from a left bundle branch block?",
  ("The wave just before the J point",
   "Correct. Find the J point in V1 and travel backwards: a positive first deflection is right bundle branch block, a negative one is left."),
  [("The duration of the QRS complex",
    "Both blocks need a QRS of 0.12 seconds or longer, so duration says only that a bundle branch block is present."),
   ("The height of the R wave in V1",
    "R wave height in V1 is a hypertrophy question. The side of a bundle branch block is read from the deflection before the J point."),
   ("The shape of the P wave in V1",
    "The P wave reflects the atria. The side of a bundle branch block is read from the QRS in V1.")],
  17),

Q("Bundle branch block criteria", IOD, "compare",
  "A 77-year-old woman has a wide QRS with slurred S waves in leads I, aVL, V5 and V6. Which block is this?",
  ("Right bundle branch block",
   "Correct. Slurred S waves in the lateral leads are a right bundle branch block criterion, the double QRS phenomenon best seen in V6."),
  [("Left bundle branch block",
    "Left bundle branch block notches the lateral QRS complexes and removes their Q waves; it does not give slurred S waves."),
   ("Left anterior fascicular block",
    "A fascicular block keeps the QRS narrow and is diagnosed by axis and limb-lead patterns."),
   ("Left ventricular hypertrophy",
    "Left ventricular hypertrophy gives tall lateral R waves with a normal duration, not slurred S waves.")],
  16),

Q("Bundle branch block criteria", IOD, "compare",
  "A 75-year-old man has a wide QRS with notched lateral complexes and no Q waves in I, aVL, V5 and V6. Which block is this?",
  ("Left bundle branch block",
   "Correct. Notching of the lateral QRS complexes, the double QRS phenomenon best seen in V6, with no lateral Q waves is left bundle branch block."),
  [("Right bundle branch block",
    "Right bundle branch block gives slurred lateral S waves and an rSR in V1, not notching with absent Q waves."),
   ("Left posterior fascicular block",
    "A fascicular block keeps the QRS narrow and does not notch the lateral complexes."),
   ("Right ventricular hypertrophy",
    "Right ventricular hypertrophy changes V1 and V2 (more R than S wave), not the lateral leads in this way.")],
  12),

Q("Bundle branch block criteria", IOC, "criteria",
  "A 66-year-old woman's QRS is 0.13 seconds (normal under 0.12). Which V1 pattern fits left bundle branch block?",
  ("rS pattern",
   "Correct. Left bundle branch block shows an rS pattern in V1: a small r wave, then a deep S, so the first deflection back from the J point is negative."),
  [("rSR pattern",
    "An rSR pattern in V1, ending positive, is right bundle branch block."),
   ("qR pattern",
    "A qR in V1 ends with a positive R wave, which points to the right side, not to a left bundle branch block."),
   ("Tall R pattern",
    "A dominant R wave in V1 ends positive. Left bundle branch block ends V1 with a deep S wave.")],
  12),

Q("Bundle branch block criteria", IOC, "criteria",
  "A 64-year-old man's QRS is 0.13 seconds (normal under 0.12). Which V1 pattern fits right bundle branch block?",
  ("rSR pattern",
   "Correct. Right bundle branch block shows an rSR pattern in V1, so the first deflection back from the J point is positive."),
  [("rS pattern",
    "An rS pattern in V1, ending negative, is left bundle branch block."),
   ("QS pattern",
    "A wholly negative complex in V1 ends negative, the left bundle branch block side."),
   ("Notched R in V6 only",
    "A notched R in V6 is the left bundle branch block double QRS phenomenon, not a V1 pattern of the right side.")],
  16),

Q("Bundle branch block criteria", IOD, "compare",
  "A 61-year-old woman is told her electrocardiogram shows bunny ears in V1. Why should that pattern not be relied on?",
  ("Right bundle block has many V1 shapes",
   "Correct. Right bundle branch block can have many morphologies in V1; the constant is that the first deflection back from the J point is positive."),
  [("Bunny ears mean left bundle block",
    "Bunny ears are taught for the right side, and even there they are not reliable. The J point rule decides."),
   ("Bunny ears are a normal variant",
    "The problem is not that bunny ears are normal; it is that right bundle branch block takes many V1 shapes besides them."),
   ("Bunny ears need a narrow QRS",
    "Every bundle branch block has a wide QRS. The issue is that V1 morphology varies, while the J point rule does not.")],
  17),

Q("Where the ventricles depolarize", IOI, "physiology",
  "A 70-year-old man has a bundle branch block. Why is his QRS wide?",
  ("Slow myocyte-to-myocyte conduction",
   "Correct. The blocked side must wait for myocyte-to-myocyte transmission across the heart, much slower than the conduction pathway, so the QRS widens."),
  [("Faster conduction down both bundles",
    "Faster conduction would narrow the QRS. A blocked bundle forces slow cell-to-cell spread instead."),
   ("A block in the atrioventricular node",
    "A nodal block lengthens the PR interval, not the QRS. A bundle branch block widens the QRS."),
   ("Chaotic ventricular foci",
    "Chaotic foci are ventricular fibrillation. A bundle branch block is organized conduction delayed on one side.")],
  11),

Q("Where the ventricles depolarize", IOI, "physiology",
  "A 75-year-old woman has left bundle branch block. Which ventricle depolarizes first?",
  ("The right ventricle",
   "Correct. Impulses travel down the right bundle normally, so the right ventricle contracts first; the left must wait for myocyte-to-myocyte spread."),
  [("The left ventricle",
    "The left bundle is the blocked one, so the left ventricle depolarizes late, after the impulse crosses from the right."),
   ("Both at the same time",
    "Simultaneous depolarization is normal conduction. In a bundle branch block the ventricles contract in sequence."),
   ("The septum, left to right",
    "Normal septal depolarization runs left to right, but in left bundle branch block the septal fascicle is blocked too.")],
  11),

Q("Where the ventricles depolarize", IOI, "physiology",
  "A 69-year-old man has left bundle branch block. Why are the Q waves missing from his lateral leads?",
  ("The septal fascicle is blocked",
   "Correct. Q waves represent depolarization of the interventricular septum; with the septal fascicle blocked, the lateral leads lose them."),
  [("The right bundle is blocked",
    "In left bundle branch block the right bundle conducts normally. It is the septal fascicle of the left bundle that is lost."),
   ("The atria are enlarged",
    "Atrial enlargement changes the P wave. The missing Q waves come from the blocked septal fascicle."),
   ("The QRS is too narrow",
    "The QRS in left bundle branch block is wide, 0.12 seconds or longer. The Q waves vanish because the septum is not activated first.")],
  11),

Q("Where the ventricles depolarize", IOI, "physiology",
  "A 72-year-old woman has a bundle branch block with a double-humped QRS. What produces this two-QRS-complex phenomenon?",
  ("Ventricles depolarizing in sequence",
   "Correct. Because the ventricles are contracted in sequence rather than at the same time, the QRS shows two humps: the two QRS complex phenomenon."),
  [("Two separate pacemakers firing",
    "Two independent pacemakers describe third-degree block. In a bundle branch block one impulse reaches the ventricles at different times."),
   ("Atrial and ventricular overlap",
    "The P wave is not fused into the QRS here. The two humps come from the two ventricles depolarizing one after the other."),
   ("A pacer spike before each QRS",
    "A pacer spike is a device artifact. The double QRS comes from sequential ventricular depolarization.")],
  15),

Q("Where the ventricles depolarize", IOI, "physiology",
  "A 63-year-old man has right bundle branch block. Which part of the heart is depolarized normally?",
  ("The left ventricle",
   "Correct. In right bundle branch block, impulses travel down the left bundle normally, so the left ventricle contracts normally; the right waits."),
  [("The right ventricle",
    "The right bundle is the blocked one, so the right ventricle depolarizes late, by myocyte-to-myocyte spread."),
   ("Neither ventricle",
    "Only one side is blocked. The left bundle still carries the impulse to the left ventricle."),
   ("Only the atria",
    "The atria and the left ventricle both depolarize normally. Only the right ventricle is delayed.")],
  15),
]
