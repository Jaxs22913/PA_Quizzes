# -*- coding: utf-8 -*-
# PDM I Lecture 15 (Ischemia, Injury, and Infarction; Scott Mathis, EMS educator, First Response
# Training Group -- title slide) -- pool A: the STRIP and 12-LEAD questions. Every question here
# shows a picture taken from the deck (tools/pdm_e3_l15_l16_images.py makes the crops; machine
# interpretations and baked-in labels are cropped off the quiz copies), cites its slide, and asks
# the finding, the territory, the artery or the next lead to record. Pool B is the text pool.
#
# Each picture is used by at most two questions with DIFFERENT asks, and the partition puts at most
# one question per picture in each set, so the two quizzes never show the same tracing twice.
#
# KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
# NUMBERS: no stem carries a measured value without the scale that reads it; most stems carry none.
# Abbreviations: lead names (V1, aVL, V4R) and wave names (QRS, ST, PR, TP, QS) are nomenclature,
# not abbreviations; everything else is spelled out (no "ECG", "STEMI", artery initials).
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "15. EKG Ischemia and Infarction.pptx"
IMG = "pdm-exam-3-quiz-images/"
def c(n): return f"{SRC}, Slide {n}"

IOA = "Review coronary artery anatomy and myocardial blood supply."
IOB = "Recognize ECG findings associated with: myocardial ischemia, myocardial injury, myocardial infarction"
IOC = "Differentiate ECG findings associated with ischemia, injury, and infarction: ST-segment elevation, ST-segment depression, T-wave inversion, pathologic Q waves"
IOD = "Compare and contrast ECG findings associated with ischemia, injury, and infarction."
IOE = "Correlate ECG lead changes with anatomic regions of the heart."
IOF = "Recognize common ECG patterns associated with acute coronary syndromes."
IOG = "Discuss the related anatomy and physiology of myocardial ischemia and infarction."

ALT12 = "Twelve-lead electrocardiogram on grid paper, with each lead labeled"


# Which slide each quiz picture was taken from (tools/pdm_e3_l15_l16_images.py). The caption under
# a picture names THAT slide; when the fact the question tests sits on a different slide, the cite
# names both.
IMG_SLIDE = {
    "15-12-lead-case-a.jpg": 9,
    "15-12-lead-case-b.jpg": 11,
    "15-12-lead-case-d.jpg": 16,
    "15-12-lead-case-e.jpg": 17,
    "15-12-lead-case-f.jpg": 18,
    "15-12-lead-case-g.jpg": 20,
    "15-12-lead-case-h.jpg": 21,
    "15-12-lead-case-i.jpg": 23,
    "15-12-lead-case-j.jpg": 24,
    "15-fast-rate-strip.jpg": 6,
    "15-limb-leads-case-c.jpg": 13,
    "15-precordial-leads-a.jpg": 7,
    "15-single-complex-a.png": 12,
    "15-single-complex-b.jpg": 12,
    "15-t-wave-strip-a.jpg": 7,
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

# ------------------------------------------------ case-a: global ST depression (slide 9)
Q("ST depression", IOC, "finding",
  "A 66-year-old woman has chest pressure at rest. Her 12-lead is shown. Which finding is present across most leads?",
  ("ST-segment depression",
   "Correct. The J point and ST segment sit below the baseline in most leads of this tracing. Widespread ST-segment depression, most obvious in the lateral chest leads and often with ST elevation in aVR, is the picture of subendocardial ischemia."),
  [("ST-segment elevation",
    "ST elevation would put the J point above the baseline in contiguous leads; here it sits below it in most leads, which is depression."),
   ("Pathologic Q waves",
    "Pathologic Q waves are deep, wide initial negative deflections that mark dead tissue. These complexes begin with normal upstrokes; the change is in the ST segment."),
   ("Hyperacute T waves",
    "Hyperacute T waves are broad, tall and symmetrical. The abnormality on this tracing is the ST segment dropping below baseline, not an enlarged T wave.")],
  c(9), "15-12-lead-case-a.jpg"),

Q("Subendocardial ischemia", IOG, "physiology",
  "A 71-year-old man with exertional chest pain has the 12-lead shown. Which layer of the heart does this pattern indicate is ischemic?",
  ("The subendocardium",
   "Correct. Widespread ST-segment depression represents subendocardial ischemia: the innermost layer, farthest from the epicardial coronary arteries, is starved first."),
  [("The full wall thickness",
    "Ischemia through the full wall thickness is transmural ischemia, also called injury, and it produces ST-segment elevation rather than depression."),
   ("The epicardium alone",
    "The epicardium lies next to the coronary arteries and is the best perfused layer. Subendocardial ischemia, shown as ST depression, affects the innermost layer."),
   ("The pericardium",
    "Inflammation of the pericardium (pericarditis) gives global concave ST elevation with PR depression, not the diffuse ST depression shown here.")],
  c(8), "15-12-lead-case-a.jpg"),

# ------------------------------------------------ case-b: V1-V4 ST elevation with hyperacute T (slide 11)
Q("Artery and territory", IOE, "artery",
  "A 52-year-old man has crushing chest pain. His 12-lead is shown. Occlusion of which artery best explains the pattern in V1 to V4?",
  ("Left anterior descending",
   "Correct. ST elevation in V1 to V4 involves the septal and anterior walls, which the left anterior descending artery supplies (front of the left ventricle and front of the septum)."),
  [("Right coronary artery",
    "The right coronary artery supplies the right atrium, right ventricle and bottom of the left ventricle; its occlusion shows up in II, III and aVF, not V1 to V4."),
   ("Left circumflex artery",
    "The circumflex supplies the side and back of the left ventricle; its territory shows in the lateral leads (I, aVL, V5, V6) or as posterior changes."),
   ("A coronary vein",
    "The coronary veins carry used, deoxygenated blood from the heart muscle back to the right atrium; an arterial occlusion causes this pattern.")],
  c(11), "15-12-lead-case-b.jpg"),

Q("Hyperacute T waves", IOB, "finding",
  "A 49-year-old woman has chest pain and the 12-lead shown. Besides ST elevation, which early ischemic finding is visible in V1 to V4?",
  ("Hyperacute T waves",
   "Correct. The T waves are broad, increased in amplitude and symmetrical, large enough to hold the QRS inside them: hyperacute T waves alongside the ST elevation."),
  [("Pathologic Q waves",
    "Pathologic Q waves mark tissue death and are deep and wide initial negative deflections; the striking change in these leads is the size of the T waves."),
   ("Inverted T waves",
    "These T waves point upward and are enlarged. T-wave inversion is a different, later sign of ischemia."),
   ("Prominent U waves",
    "Prominent U waves are a hypokalemia finding that follows the T wave; here the T wave itself is broad, tall and symmetrical.")],
  c(11), "15-12-lead-case-b.jpg"),

# ------------------------------------------------ case-c: Q waves + ST elevation III, aVF (slide 13)
Q("Pathologic Q waves", IOC, "finding",
  "A 63-year-old man has the limb-lead tracing shown. Which finding in leads III and aVF indicates death of myocardial tissue?",
  ("Pathologic Q waves",
   "Correct. The deep, wide negative deflections that open the QRS in III and aVF are pathologic Q waves, which represent infarction: actual death of cardiac tissue."),
  [("ST-segment elevation",
    "The ST elevation in these leads represents injury (transmural ischemia). It is the Q wave, not the ST segment, that marks dead tissue."),
   ("Hyperacute T waves",
    "Hyperacute T waves are the very first sign of ischemia, before any tissue has died; they mark the start of an event, not infarction."),
   ("ST-segment depression",
    "ST depression in these leads would point to subendocardial ischemia; the inferior leads here show elevation and Q waves.")],
  c(13), "15-limb-leads-case-c.jpg", "Limb-lead electrocardiogram (leads I, II, III, aVR, aVL, aVF) on grid paper"),

Q("Artery and territory", IOA, "artery",
  "A 69-year-old woman's limb leads are shown, with Q waves and ST elevation in III and aVF. Which artery most likely supplies the affected wall?",
  ("Right coronary artery",
   "Correct. III and aVF view the inferior wall, and the right coronary artery supplies the bottom (inferior) portion of the left ventricle along with the right atrium and right ventricle."),
  [("Left anterior descending",
    "The left anterior descending artery supplies the front of the left ventricle and the front of the septum, which the V leads (V1 to V4) view."),
   ("Left circumflex artery",
    "The circumflex supplies the side and back of the left ventricle; its occlusion shows in the lateral leads or as a posterior infarction."),
   ("Left main coronary artery",
    "The left main divides into the circumflex and the left anterior descending; it does not supply the inferior wall that III and aVF view.")],
  c(4), "15-limb-leads-case-c.jpg", "Limb-lead electrocardiogram (leads I, II, III, aVR, aVL, aVF) on grid paper"),

# ------------------------------------------------ case-d: inferior STEMI with reciprocal I, aVL (slide 16)
Q("Localization", IOE, "region",
  "A 42-year-old man has chest pain and the 12-lead shown. Which region of the heart does the ST elevation localize to?",
  ("Inferior wall",
   "Correct. The ST elevation is in II, III and aVF, contiguous leads that look at the inferior region, so this is documented as an inferior ST-elevation myocardial infarction."),
  [("High lateral wall",
    "The high lateral wall is viewed by I and aVL. On this tracing those leads show ST depression, the reciprocal of the inferior elevation."),
   ("Anteroseptal wall",
    "The anteroseptal wall is viewed by V1 to V4. Elevation there would sit in the chest leads, not in II, III and aVF."),
   ("Posterior wall",
    "No standard lead faces the posterior wall; it shows as isolated ST depression in V1 to V4 and is confirmed with V7 to V9.")],
  c(16), "15-12-lead-case-d.jpg"),

Q("Reciprocal changes", IOF, "reciprocal",
  "A 58-year-old man's 12-lead is shown, with ST elevation in II, III and aVF. How should the ST depression in leads I and aVL be read?",
  ("As a reciprocal change",
   "Correct. ST depression should be considered a reciprocal change until proven otherwise when ST elevation exists in the same tracing. I and aVL mirror the inferior leads, so the depression supports the inferior event."),
  [("As a second infarction",
    "Reciprocal depression is the mirror image of one event seen from the opposite side, not evidence of a separate infarction."),
   ("As lateral subendocardial ischemia",
    "With ST elevation on the same tracing, depression is read as reciprocal first. Global depression without elevation is what points to subendocardial ischemia."),
   ("As a lead placement error",
    "Mirror-image depression in the leads opposite an infarct is expected physiology, and it supports an acute event rather than a technical fault.")],
  c(14), "15-12-lead-case-d.jpg"),

# ------------------------------------------------ case-e: high lateral (slide 17)
Q("Localization", IOE, "region",
  "A 64-year-old woman has chest pain and the 12-lead shown. Which region does the ST elevation localize to?",
  ("High lateral wall",
   "Correct. ST elevation in I and aVL, contiguous leads looking at the high lateral wall of the left ventricle, with reciprocal ST depression in III and aVF."),
  [("Inferior wall",
    "The inferior leads (II, III, aVF) show depression on this tracing; that is the reciprocal of the high lateral elevation, not the infarct itself."),
   ("Anteroseptal wall",
    "Anteroseptal infarction elevates V1 to V4; the elevation that localizes this infarct is in I and aVL, with reciprocal depression in III and aVF."),
   ("Right ventricle",
    "Right ventricular involvement is confirmed by ST elevation in V4R on a right-sided tracing; it is not what I and aVL show.")],
  c(17), "15-12-lead-case-e.jpg"),

Q("Artery and territory", IOA, "artery",
  "A 61-year-old man's 12-lead is shown, with ST elevation in I and aVL and reciprocal depression in III and aVF. Occlusion of which artery best explains it?",
  ("Left circumflex artery",
   "Correct. The circumflex wraps around to supply the left atrium and the side and back of the left ventricle, so of these arteries it best explains a lateral infarction (a diagonal branch of the left anterior descending can also cause one)."),
  [("Right coronary artery",
    "The right coronary artery supplies the right heart and the bottom of the left ventricle; its occlusion elevates II, III and aVF, which are depressed here."),
   ("A coronary vein",
    "The coronary veins return used blood to the right atrium; an infarction pattern comes from an arterial occlusion."),
   ("Left main coronary artery",
    "A left main occlusion starves both of its branches, so the anterior and septal leads would be elevated too, not the high lateral leads alone.")],
  c(4), "15-12-lead-case-e.jpg"),

# ------------------------------------------------ case-f: anteroseptal (slide 18)
Q("Localization", IOE, "region",
  "A 55-year-old man has chest pain and the 12-lead shown. Which region does the ST elevation in V1 to V3 localize to?",
  ("Anteroseptal wall",
   "Correct. V1, V2 and V3 are contiguous leads looking at the anterior and septal walls, so this is an anteroseptal ST-elevation infarction."),
  [("Inferior wall",
    "The inferior wall is viewed by II, III and aVF; elevation there would be in the limb leads, not V1 to V3."),
   ("High lateral wall",
    "The high lateral wall is viewed by I and aVL; the leads named here, V1 to V3, face the anterior and septal walls instead."),
   ("Posterior wall",
    "A posterior infarction shows as ST DEPRESSION in V1 to V4 on the standard tracing; elevation in V1 to V3 faces the anteroseptal wall directly.")],
  c(18), "15-12-lead-case-f.jpg"),

# The slide 18 tracing's elevation is not confined to V1 to V3 (I, aVL and V4 to V6 are up too, and
# II, III and aVF are depressed), so no question here says the other leads are flat; the reciprocal
# question that used this picture was moved to pool B as a bare table item (2026-10-08 fact-check),
# and this artery question took its place. An extensive anterior pattern points to the same artery.
Q("Artery and territory", IOA, "artery",
  "A 57-year-old man has chest pain and the 12-lead shown, with ST elevation in V1 to V3. Occlusion of which artery best explains it?",
  ("Left anterior descending",
   "Correct. The left anterior descending artery supplies the front of the left ventricle and the front of the septum, the anterior and septal walls that V1 to V3 face."),
  [("Right coronary artery",
    "The right coronary artery supplies the right heart and the bottom of the left ventricle; its occlusion elevates II, III and aVF, which are depressed here."),
   ("Left circumflex artery",
    "The circumflex supplies the left atrium and the side and back of the left ventricle; it does not explain elevation in V1 to V3."),
   ("A coronary vein",
    "The coronary veins return used blood to the right atrium; an infarction pattern comes from an arterial occlusion.")],
  c(4), "15-12-lead-case-f.jpg"),

# ------------------------------------------------ case-g: isolated ST depression V1-V3 (slide 20)
Q("Posterior infarction", IOF, "next test",
  "A 62-year-old woman has chest pain. Her 12-lead is shown, with ST depression in V1 to V3 and no ST elevation anywhere. Which is the next best step?",
  ("Record posterior leads V7 to V9",
   "Correct. Isolated ST depression in V1 to V4 with no elevation anywhere is a reciprocal change for a posterior infarction until proven otherwise, so a posterior (15-lead) tracing is obtained."),
  [("Record right-sided lead V4R",
    "V4R checks for right ventricular involvement in an inferior infarction. The pattern here (isolated anterior depression) calls for the posterior leads."),
   ("Repeat the standard 12 leads only",
    "The standard leads have no camera on the back of the heart; repeating them cannot show the posterior wall that this depression may be mirroring."),
   ("Treat as anterior ischemia only",
    "Isolated V1 to V4 depression must be presumed reciprocal to a posterior infarction until proven otherwise; settling for anterior ischemia risks missing it.")],
  c(19), "15-12-lead-case-g.jpg"),

Q("Posterior infarction", IOF, "interpret",
  "A 57-year-old man's 12-lead is shown: ST depression in V1 to V3 and no ST elevation in any lead. Until proven otherwise, what should this be considered?",
  ("Reciprocal to a posterior infarction",
   "Correct. Isolated ST depression in V1 to V4 with no elevation anywhere should always be considered a reciprocal change for a posterior ST-elevation infarction until proven otherwise."),
  [("Anterior subendocardial ischemia",
    "That reading misses the rule: isolated anterior depression with no elevation anywhere is presumed to mirror a posterior infarction until posterior leads say otherwise."),
   ("Right ventricular infarction",
    "Right ventricular involvement accompanies an inferior infarction and is confirmed by elevation in V4R, not by isolated depression in V1 to V3."),
   ("A normal variant",
    "Depression in V1 to V3 in a patient with chest pain is not dismissed as normal; it is the classic mirror of a posterior wall infarction.")],
  c(19), "15-12-lead-case-g.jpg"),

# ------------------------------------------------ case-h: posterior leads (slide 21)
Q("Posterior infarction", IOA, "artery",
  "A 62-year-old woman's repeat tracing is shown, with V4 to V6 moved to the back as V7 to V9; V8 and V9 show ST elevation. Which artery is typically occluded?",
  ("Left circumflex artery",
   "Correct. Posterior wall infarctions typically result from occlusion or stenosis of the left circumflex artery, which supplies the back of the left ventricle."),
  [("Left anterior descending",
    "The left anterior descending artery supplies the front of the left ventricle and septum; the posterior wall belongs to the circumflex."),
   ("Left main coronary artery",
    "A left main occlusion would starve both the circumflex and the left anterior descending territories, not the posterior wall alone."),
   ("Pulmonary artery",
    "The pulmonary artery carries blood to the lungs and does not perfuse the myocardium; the coronary arteries do.")],
  c(19), "15-12-lead-case-h.jpg", "Electrocardiogram with three chest-lead labels crossed out and handwritten replacements (V7, V8, V9)"),

Q("Posterior infarction", IOF, "name",
  "A 62-year-old woman had V4, V5 and V6 moved to her back and the tracing repeated, as shown. What is this recording often called?",
  ("A 15-lead electrocardiogram",
   "Correct. Moving V4 to V6 to the back as V7, V8 and V9 and repeating the tracing gives what is at times called a 15-lead electrocardiogram, the posterior tracing."),
  [("A right-sided electrocardiogram",
    "A right-sided tracing moves V4 to the right fifth intercostal space at the midclavicular line (V4R) to look at the right ventricle, not to the back."),
   ("A 3-lead rhythm strip",
    "A rhythm strip monitors rate and rhythm in a few leads. The posterior tracing is a full 12-lead with three chest electrodes relocated."),
   ("A reversed limb-lead tracing",
    "No limb electrode is moved here; the three lateral chest electrodes are relocated to the back to view the posterior wall.")],
  c(19), "15-12-lead-case-h.jpg", "Electrocardiogram with three chest-lead labels crossed out and handwritten replacements (V7, V8, V9)"),

# ------------------------------------------------ case-i: inferior STEMI, RV suspicion (slide 23)
Q("Right ventricular involvement", IOF, "next test",
  "A 70-year-old man has chest pain, hypotension, clear lungs and distended neck veins. His 12-lead is shown. Which is the next best step?",
  ("Record right-sided lead V4R",
   "Correct. This is an inferior ST-elevation infarction, and hypotension with clear lungs and jugular vein distension raises suspicion of right ventricular involvement. Moving V4 to the right (V4R) rules it in or out."),
  [("Record posterior leads V7 to V9",
    "Posterior leads answer isolated ST depression in V1 to V4. Hypotension, clear lungs and distended neck veins with an inferior infarct point to the right ventricle."),
   ("Repeat the standard 12 leads only",
    "The standard 12-lead does not look at the right ventricle in its entirety; only a right-sided lead such as V4R can confirm its involvement."),
   ("No more leads; it is inferior only",
    "Hypotension, clear lungs and jugular vein distension in an inferior infarction are the cue to suspect right ventricular involvement, so it cannot be assumed inferior only.")],
  c(22), "15-12-lead-case-i.jpg"),

Q("Reciprocal changes", IOF, "reciprocal",
  "A 67-year-old woman's 12-lead is shown, with ST elevation in II, III and aVF. Which leads carry the reciprocal ST depression?",
  ("Leads I and aVL",
   "Correct. I and aVL are the reciprocal leads of the inferior wall, and here they show the mirror-image ST depression that confirms the inferior infarction."),
  [("Leads V1 to V3",
    "Isolated depression in V1 to V3 is the mirror of a POSTERIOR infarction. The inferior wall's reciprocal leads are I and aVL."),
   ("Leads V5 and V6",
    "V5 and V6 face the lateral wall; on the localization table the inferior wall's reciprocal leads are I and aVL only."),
   ("Leads II, III and aVF",
    "II, III and aVF are the leads facing the infarct and carry the elevation; reciprocal leads are the opposite ones.")],
  c(23), "15-12-lead-case-i.jpg"),

# ------------------------------------------------ case-j: V4R tracing (slide 24)
Q("Right ventricular involvement", IOF, "interpret",
  "A 72-year-old man with an inferior infarction had V4 moved to the right fifth intercostal space, midclavicular line. The tracing is shown, with ST elevation in that lead. What does this confirm?",
  ("Right ventricular involvement",
   "Correct. ST elevation in V4R (V4 moved to the right fifth intercostal space, midclavicular line) confirms right ventricular involvement in an inferior infarction."),
  [("A posterior wall infarction",
    "A posterior infarction is confirmed by ST elevation in V7 to V9 on the back, not by elevation in a right-chest lead."),
   ("Lead misplacement",
    "The lead was moved on purpose to look at the right ventricle; elevation there is a finding, not an artifact."),
   ("Acute pericarditis",
    "Pericarditis gives global concave ST elevation with PR depression; a single right-sided lead elevating in an inferior infarct means right ventricular involvement.")],
  c(24), "15-12-lead-case-j.jpg", "Electrocardiogram with the V4 label circled and relabeled by hand"),

Q("Right ventricular involvement", IOA, "artery",
  "A 74-year-old woman's right-sided tracing is shown, with ST elevation in V4R during an inferior infarction. Occlusion of which artery explains this?",
  ("Right coronary artery",
   "Correct. Inferior infarctions involving the right coronary artery can include the right ventricle, which the right coronary artery supplies along with the right atrium."),
  [("Left circumflex artery",
    "The circumflex supplies the side and back of the left ventricle. It does not supply the right ventricle that V4R views."),
   ("Left anterior descending",
    "The left anterior descending artery supplies the front of the left ventricle and septum, not the right ventricle."),
   ("Left main coronary artery",
    "The left main feeds the circumflex and left anterior descending arteries; the right ventricle is perfused by the right coronary artery.")],
  c(22), "15-12-lead-case-j.jpg", "Electrocardiogram with the V4 label circled and relabeled by hand"),

# ------------------------------------------------ single complexes (slide 12)
Q("Pathologic Q waves", IOC, "finding",
  "A 59-year-old man who had an infarction last year has this complex in lead III. What is the deep first deflection?",
  ("A pathologic Q wave",
   "Correct. The first negative deflection before the R wave is a Q wave; one deeper than 2 mm, or than a quarter of the R wave's height as this one is, is pathologic, a sign of infarction."),
  [("A delta wave",
    "A delta wave is a slurred UPSTROKE of the QRS from preexcitation; this is a deep negative deflection before the R wave."),
   ("An S wave",
    "An S wave is a negative deflection that comes AFTER the R wave. The first negative deflection, before the R, is the Q wave."),
   ("An Osborn wave",
    "An Osborn (J) wave is a notch at the END of the QRS, seen in hypothermia and early repolarization, not a deep initial deflection.")],
  c(12), "15-single-complex-a.png", "A single electrocardiogram complex on grid paper"),

Q("Pathologic Q waves", IOG, "physiology",
  "A 64-year-old man with no known heart history has a complex like this in leads II, III and aVF. What does the deep first deflection represent?",
  ("Death of myocardial tissue",
   "Correct. Pathological Q waves usually represent infarction, the actual death of cardiac tissue, from either a previous or an acute cardiac event."),
  [("Reversible ischemia",
    "Reversible ischemia shows as hyperacute T waves or ST depression. A pathologic Q wave usually means tissue has already died."),
   ("Transmural injury in progress",
    "Injury (transmural ischemia) is shown by ST elevation. The Q wave marks infarction, the stage after injury."),
   ("Normal septal activation",
    "A normal septal Q wave is small and shallow; one this deep, past 2 mm and a quarter of the R wave's height, meets the pathologic criteria.")],
  c(12), "15-single-complex-a.png", "A single electrocardiogram complex on grid paper"),

Q("Pathologic Q waves", IOC, "name",
  "A 70-year-old woman with a recent infarction has this complex in V2: a single deep negative deflection with no R wave. In this setting, what is it called?",
  ("A pathologic Q wave",
   "Correct. With no R wave the deflection is technically a QS complex, and in the setting of an infarction it is read as a pathological Q wave with no R wave."),
  [("A delta wave",
    "A delta wave is a slurred upstroke at the start of a QRS in preexcitation; it is followed by the rest of a positive QRS."),
   ("An inverted U wave",
    "A U wave follows the T wave and is small; this is the whole ventricular complex, a single deep negative deflection."),
   ("A hyperacute T wave",
    "A hyperacute T wave is a broad, tall, upright T wave. This deflection is the QRS itself, deep and negative.")],
  c(12), "15-single-complex-b.jpg", "A single electrocardiogram complex on grid paper"),

# ------------------------------------------------ hyperacute T waves V1-V6 (slide 7)
Q("Hyperacute T waves", IOB, "finding",
  "A 48-year-old man has had 20 minutes of chest pressure. His precordial leads are shown, with no ST elevation. What are these T waves?",
  ("Hyperacute T waves",
   "Correct. Tall, increased in amplitude and symmetrical, with no ST elevation yet: hyperacute T waves, often the very first sign of cardiac ischemia."),
  [("Normal T waves",
    "Normal T waves are asymmetrical, with a slow initial upstroke and a sharper terminal downstroke, and their amplitude is modest. These are tall and symmetrical."),
   ("Inverted T waves",
    "These T waves point upward. T-wave inversion is a later ischemic sign than hyperacute T waves."),
   ("Flattened T waves",
    "Flattened T waves (a hypokalemia and hypothyroidism finding) are low and shallow; these are tall and upright.")],
  c(7), "15-precordial-leads-a.jpg", "Six precordial leads, V1 to V6, on grid paper"),

Q("Hyperacute T waves", IOF, "significance",
  "A 53-year-old woman with chest pain has these precordial T waves but no ST elevation or depression. Why does this finding matter?",
  ("It is often the first sign of ischemia",
   "Correct. Hyperacute T waves are often the very first sign of cardiac ischemia. Because there is no ST change to call yet, they are easily missed."),
  [("It is a normal variant",
    "Tall, symmetrical T waves in a patient with chest pain are hyperacute, not a variant; normal T waves are asymmetrical and modest."),
   ("It proves an old infarction",
    "An old infarction is shown by pathologic Q waves. Hyperacute T waves come at the very start of an ischemic event."),
   ("It shows dead myocardial tissue",
    "Tissue death is marked by pathologic Q waves. Hyperacute T waves appear before injury or infarction has developed.")],
  c(7), "15-precordial-leads-a.jpg", "Six precordial leads, V1 to V6, on grid paper"),

# ------------------------------------------------ normal T waves strip (slide 7)
Q("Hyperacute T waves", IOD, "normal",
  "A healthy 30-year-old woman has the rhythm strip shown. Which description fits her T waves?",
  ("Asymmetrical, slow upstroke",
   "Correct. Normal T waves are asymmetrical, with a slow initial upstroke and a sharper negative terminal deflection, and a modest amplitude."),
  [("Broad, tall and symmetrical",
    "Broad, tall, symmetrical T waves are hyperacute T waves, the earliest sign of ischemia; normal T waves are asymmetrical."),
   ("Inverted below the baseline",
    "These T waves are upright. T-wave inversion is an ischemic sign, not the normal shape."),
   ("Peaked and narrow",
    "Peaked, symmetric T waves are the early sign of hyperkalemia. A normal T wave rises slowly and falls more sharply.")],
  c(7), "15-t-wave-strip-a.jpg", "A single-lead rhythm strip on grid paper"),

# ------------------------------------------------ fast rate, no TP (slide 6)
Q("J point and baseline", IOC, "measure",
  "A 55-year-old woman has chest pain and the fast rhythm strip shown, with no visible TP segment. To judge ST elevation, what should the J point be compared with?",
  ("The onset of the QRS",
   "Correct. The J point is normally compared to the TP segment, but at fast rates the TP segment can be hard to find, and it is then appropriate to compare the J point to the beginning of the QRS complex."),
  [("The TP segment",
    "The TP segment is the usual baseline, but at this rate it has disappeared, which is exactly when the onset of the QRS is used instead."),
   ("The peak of the T wave",
    "The peak of the T wave is not a baseline at all; ST deviation is measured against the resting baseline."),
   ("The top of the R wave",
    "The R-wave peak measures QRS amplitude, not ST deviation. A baseline is needed, and here that is the start of the QRS.")],
  c(6), "15-fast-rate-strip.jpg", "A single-lead rhythm strip on grid paper at a fast rate"),

Q("Pathologic Q waves", IOG, "physiology",
  "A 66-year-old woman with a recent infarction has this QS complex in V2. What has happened to the tissue under that lead?",
  ("It has died (infarction)",
   "Correct. A pathological Q wave, here a QS complex with no R wave, usually represents infarction: the cells beneath that lead have died and can no longer depolarize."),
  [("It is reversibly ischemic",
    "Reversible ischemia shows as hyperacute T waves or ST depression. Loss of the R wave into a QS complex usually means the tissue has died."),
   ("It is injured but alive",
    "Injury (transmural ischemia) is shown by ST elevation. A pathologic Q wave usually marks the stage after injury, tissue death."),
   ("It is normal septal tissue",
    "Normal septal activation produces a small, narrow initial deflection with an R wave following; a deep QS complex after infarction is pathologic.")],
  c(12), "15-single-complex-b.jpg", "A single electrocardiogram complex on grid paper"),

Q("Hyperacute T waves", IOB, "first sign",
  "A healthy 30-year-old woman's T waves are shown. If ischemia began, which change in these T waves is often the very first sign?",
  ("They become hyperacute",
   "Correct. Hyperacute T waves, broad, increased in amplitude and symmetrical, are often the very first sign of cardiac ischemia; the normal T wave shown is asymmetrical."),
  [("They become inverted",
    "T-wave inversion is a sign of ischemia, but it comes later than hyperacute T waves."),
   ("They become flattened",
    "Flattened T waves belong to hypokalemia and hypothyroidism, not to the first minutes of ischemia."),
   ("They disappear entirely",
    "The T wave does not vanish with ischemia; the earliest change is that it grows broad, tall and symmetrical.")],
  c(7), "15-t-wave-strip-a.jpg", "A single-lead rhythm strip on grid paper"),

Q("J point and baseline", IOC, "measure",
  "A 60-year-old man's rhythm strip is shown at a fast rate. Which usual baseline has disappeared, making ST deviation harder to judge?",
  ("The TP segment",
   "Correct. The TP segment is the usual baseline for judging the J point, but at fast heart rates it can be hard to locate, and the onset of the QRS is used instead."),
  [("The PR interval",
    "The PR interval runs from the start of the P wave to the QRS; it is not the reference baseline for the J point, which is the TP segment."),
   ("The QRS complex",
    "The QRS is still present on every beat; it is the flat TP segment between beats that has disappeared at this rate."),
   ("The ST segment",
    "The ST segment is what is being judged, not the baseline it is compared against; that baseline is the TP segment.")],
  c(6), "15-fast-rate-strip.jpg", "A single-lead rhythm strip on grid paper at a fast rate"),

]

