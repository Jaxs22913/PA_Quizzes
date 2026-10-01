# -*- coding: utf-8 -*-
# PDM I Lecture 7 (Principles of Electrocardiography, Ayelet Elwaya) -- pool M
# (16 extra questions for the cumulative master exams).
# Written to sit beside pools A and B without duplicating them: it targets facts
# those pools skip or under-use -- the sinoatrial node's intrinsic rate, the
# absolute refractory duration, the left anterior fascicle, the atrioventricular
# node's location, Einthoven's triangle, the fourth limb electrode, the
# contiguous lateral group, standard voltage calibration, the thirty-large-box
# six-second strip, atrial versus ventricular rate, regularity without calipers,
# QTc banding, sex-specific QT limits, Q wave width, the J point's allowed
# variance and the three-hundred method (slide 53 carries it as a picture only).
# The bifascicular-block aside and Bazett's formula are deliberately NOT used.
#
# The lecture's number rule is relaxed (see pool A): intervals, thresholds and
# the two rate methods are the material. Stems still hand over the strip counts
# or measured boxes and a word that reads them.
#
# Correct answer is ALWAYS written first (c=0); the builder rotates positions.
SRC = "Principles of Electrocardiography.pptx"
def c(n):  return f"{SRC}, Slide {n}"

IOA = "Describe action potentials and impulse conduction through the cardiac conduction system"
IOB = "Define depolarization and repolarization"
IOC = "Define absolute and relative refractory periods"
IOD = "Describe the fundamental principles of electrocardiography"

POOL_M = [

{"topic": "Sinoatrial node", "io": IOA, "slot": "intrinsic rate",
 "q": "What is the intrinsic firing rate of the sinoatrial node, the main pacemaker of the heart?",
 "opts": [
  ["60 to 100 beats per minute",
   "Correct. This is the fastest intrinsic rate in the conduction system, which is why the sinoatrial node normally sets the pace and the slower pacemakers stay in reserve."],
  ["40 to 60 beats per minute",
   "That is the intrinsic rate of the atrioventricular node, the back-up pacemaker; the sinoatrial node fires faster, at 60 to 100 beats per minute."],
  ["20 to 40 beats per minute",
   "That is the intrinsic rate of the Purkinje network, the third pacemaker; the sinoatrial node fires much faster, at 60 to 100 beats per minute."],
  ["100 to 150 beats per minute",
   "That is faster than any structure in the conduction system fires on its own; the sinoatrial node's intrinsic rate is 60 to 100 beats per minute."]],
 "c": 0, "cite": c(13)},

{"topic": "Refractory periods", "io": IOC, "slot": "duration",
 "q": "How long does the absolute refractory period typically last?",
 "opts": [
  ["About 180 milliseconds",
   "Correct. It runs from phase 0 to the middle of phase 3, and throughout that time the cell will not respond to another stimulus."],
  ["About 18 milliseconds",
   "That is far too short; the absolute refractory period typically lasts about 180 milliseconds, covering phase 0 through the middle of phase 3."],
  ["About 80 milliseconds",
   "That is too short to span phase 0 to mid phase 3; the absolute refractory period typically lasts about 180 milliseconds."],
  ["About 360 milliseconds",
   "That is double the typical length; the absolute refractory period lasts about 180 milliseconds, ending in the middle of phase 3."]],
 "c": 0, "cite": c(11)},

{"topic": "Left bundle branch", "io": IOA, "slot": "anatomy",
 "q": "Which fascicle of the left bundle branch extends across the anterior wall of the left ventricle?",
 "opts": [
  ["The left anterior fascicle",
   "Correct. Of the left fascicles it is the one that extends across the anterior wall of the left ventricle."],
  ["The left posterior fascicle",
   "The left posterior fascicle extends across the posterior aspect of the left ventricle rather than the anterior wall."],
  ["The intraventricular septal fascicle",
   "The septal fascicle extends across the interventricular septum; it is the left anterior fascicle that crosses the anterior wall."],
  ["The right bundle branch",
   "The right bundle branch is not a fascicle of the left bundle branch; it supplies the right ventricle."]],
 "c": 0, "cite": c(15)},

{"topic": "Atrioventricular node", "io": IOA, "slot": "location",
 "q": "Where is the atrioventricular node located?",
 "opts": [
  ["At the junction of atria and ventricles, near the coronary sinus",
   "Correct. This position lets it sit between the atrial and ventricular halves of the system, where it adds a short pause in conduction before the ventricles are activated."],
  ["In the upper wall of the right atrium, below the vena cava opening",
   "That describes the sinoatrial node, the main pacemaker; the atrioventricular node lies lower, at the junction of the atria and ventricles."],
  ["Across the posterior aspect of the left ventricle, near its wall",
   "That describes the path of the left posterior fascicle; the atrioventricular node sits at the junction of the atria and ventricles."],
  ["Inside the right ventricle, at the end of the right bundle branch",
   "That is where the right bundle branch ends in the Purkinje network; the atrioventricular node sits at the junction of atria and ventricles."]],
 "c": 0, "cite": c(14)},

{"topic": "Bipolar leads", "io": IOD, "slot": "lead anatomy",
 "q": "Which body points form Einthoven's triangle, the imaginary triangle created by leads I, II and III?",
 "opts": [
  ["Both shoulders and the left lower extremity",
   "Correct. Each side of the triangle compares two of these points, which is why these three leads are bipolar."],
  ["Both shoulders and the right lower extremity",
   "The lower corner is the left lower extremity; the right leg electrode is the fourth limb lead added to the original three, not a corner of the triangle."],
  ["Both hips and the left shoulder",
   "The triangle is anchored at both shoulders with a single lower corner on the left lower extremity, not on the hips."],
  ["Both shoulders and the center of the chest",
   "The chest electrodes make up the precordial leads, which are unipolar; the bipolar triangle uses both shoulders and the left lower extremity."]],
 "c": 0, "cite": c(21)},

{"topic": "Limb leads", "io": IOD, "slot": "lead placement",
 "q": "Which physical limb electrode was added to the original three to give four limb electrodes?",
 "opts": [
  ["Right leg",
   "Correct. The right leg electrode was added to the original three (right arm, left arm, left leg). It serves as a ground, and the four physical limb electrodes give the six hexaxial leads."],
  ["Right arm",
   "The right arm electrode was one of the original three; the one added later is the right leg electrode."],
  ["Left arm",
   "The left arm electrode was one of the original three limb electrodes; the one added later is the right leg electrode."],
  ["Left leg",
   "The left leg electrode was already one of the original three limb electrodes; the one added later is the right leg electrode."]],
 "c": 0, "cite": c(22)},

{"topic": "Contiguous leads", "io": IOD, "slot": "lead groups",
 "q": "Lead I and lead aVL form a contiguous group with which other leads?",
 "opts": [
  ["V5 and V6",
   "Correct. Leads I, aVL, V5 and V6 look at the same area of the heart, so a change across all four means more than one isolated lead."],
  ["V1 and V2",
   "V1 and V2 sit in the group with V3 and V4, which looks at a different area; leads I and aVL group with V5 and V6."],
  ["II and III",
   "Leads II and III group with aVF; leads I and aVL group with V5 and V6."],
  ["V3 and V4",
   "V3 and V4 belong to the V1 to V4 group rather than the lead I group; leads I and aVL group with V5 and V6."]],
 "c": 0, "cite": c(25)},

{"topic": "Voltage", "io": IOD, "slot": "calibration",
 "q": "On standard calibration, a deflection rises ten millimeters, which is two large boxes. What voltage does it represent?",
 "opts": [
  ["1 millivolt",
   "Correct. Standard calibration sets two large boxes, a 10 millimeter deflection, equal to 1 millivolt, so each small box is 0.1 millivolt."],
  ["10 millivolts",
   "That is ten times too large; on standard calibration a 10 millimeter deflection equals 1 millivolt, because each small box is 0.1 millivolt."],
  ["0.1 millivolt",
   "That is the value of a single small box, one millimeter tall; two large boxes equal 10 millimeters, which is 1 millivolt."],
  ["0.5 millivolt",
   "That would be half the standard deflection; a rise of two large boxes, 10 millimeters, equals 1 millivolt."]],
 "c": 0, "cite": c(28)},

{"topic": "Time", "io": IOD, "slot": "paper timing",
 "q": "A strip has no three-second markers. How many large boxes make up a six-second strip?",
 "opts": [
  ["Thirty large boxes",
   "Correct. Each large box is 0.2 seconds, so fifteen large boxes make 3 seconds and thirty make 6 seconds."],
  ["Fifteen large boxes",
   "Fifteen large boxes at 0.2 seconds each is only 3 seconds; a six-second strip needs thirty large boxes."],
  ["Five large boxes",
   "Five large boxes is just one second, since each is 0.2 seconds; a six-second strip needs thirty large boxes."],
  ["Sixty large boxes",
   "Sixty large boxes at 0.2 seconds each would be 12 seconds; a six-second strip needs thirty large boxes."]],
 "c": 0, "cite": c(51)},

{"topic": "Heart rate", "io": IOD, "slot": "six-second method",
 "q": "A six-second rhythm strip shows twelve P waves and eleven QRS complexes. What is the atrial rate?",
 "opts": [
  ["120 beats per minute",
   "Correct. The atrial rate comes from counting P waves in six seconds and multiplying by ten, so twelve P waves give 120."],
  ["110 beats per minute",
   "That multiplies the QRS count by ten, which gives the ventricular rate; the atrial rate uses the twelve P waves and is 120."],
  ["23 beats per minute",
   "That adds the two counts together, which has no meaning; the atrial rate is the P wave count multiplied by ten, or 120."],
  ["12 beats per minute",
   "That is the raw P wave count without the multiplication; six seconds is a tenth of a minute, so the atrial rate is 120."]],
 "c": 0, "cite": c(51)},

{"topic": "Rhythm regularity", "io": IOD, "slot": "technique",
 "q": "No calipers are available and a rhythm may be irregular. What is the most appropriate way to compare consecutive R to R intervals?",
 "opts": [
  ["A marked sheet of paper",
   "Correct. Marking two R waves on a paper edge and sliding it along the strip does the job of calipers for comparing consecutive R to R intervals."],
  ["A count of complexes in three seconds",
   "A raw count gives a rate, not a comparison of consecutive R to R intervals; without calipers, a marked sheet of paper is used for regularity."],
  ["The three hundred method on one interval",
   "That method gives a rate and only works if the rhythm is already regular, so it cannot test regularity; a marked sheet of paper can."],
  ["The QT interval between two beats",
   "The QT interval measures ventricular activity within one beat and says nothing about spacing between beats; a marked sheet of paper compares R to R intervals."]],
 "c": 0, "cite": c(47)},

{"topic": "Corrected QT", "io": IOD, "slot": "interpretation",
 "q": "A man has a corrected QT interval of 480 milliseconds. How should that be read?",
 "opts": [
  ["Borderline or prolonged",
   "Correct. Above 450 milliseconds in a man, or 460 in a woman, up to 500 milliseconds is borderline or prolonged, and only above 500 is it high risk."],
  ["Normal for a man",
   "The normal corrected QT in a man is 350 to 450 milliseconds; 480 is above that and falls in the borderline or prolonged band."],
  ["High risk prolongation",
   "High risk prolongation begins above 500 milliseconds; 480 is in the borderline or prolonged band between 450 and 500."],
  ["Prolonged only in women",
   "The female limit is 460 milliseconds, so 480 is above it too; the borderline or prolonged band applies to both sexes."]],
 "c": 0, "cite": c(42)},

{"topic": "QT interval", "io": IOD, "slot": "normal values",
 "q": "What is the normal corrected QT interval range in a man?",
 "opts": [
  ["350 to 450 milliseconds",
   "Correct. The corrected QT interval, which adjusts for heart rate, is normally 350 to 450 milliseconds in men; the female range is slightly higher, at 360 to 460 milliseconds."],
  ["360 to 460 milliseconds",
   "That is the normal corrected QT range for a woman; in a man it is 350 to 450 milliseconds."],
  ["450 to 500 milliseconds",
   "That band is borderline or prolonged for a corrected QT, not normal; the normal QT interval in a man is 350 to 450 milliseconds."],
  ["400 to 500 milliseconds",
   "That reaches into the prolonged range, up to the 500 millisecond threshold; the normal QT interval in a man is 350 to 450 milliseconds."]],
 "c": 0, "cite": c(41)},

{"topic": "Q wave", "io": IOD, "slot": "measure and interpret",
 "q": "A Q wave measures 0.08 seconds, which is two small boxes. How should that be read?",
 "opts": [
  ["Too wide; normal is under 0.04 seconds",
   "Correct. A normal Q wave is under 0.04 seconds (one small box) and low in amplitude, so two small boxes is too wide."],
  ["Normal; a Q wave may last to 0.12 seconds",
   "That is the limit for the P wave and the QRS complex; a Q wave must be under 0.04 seconds, so 0.08 is too wide."],
  ["Normal; a Q wave lasts 0.12 to 0.20 seconds",
   "That is the normal PR interval; a Q wave must be under 0.04 seconds, so 0.08 seconds is too wide."],
  ["Too narrow; it should reach 0.12 seconds",
   "A Q wave is meant to be brief, under 0.04 seconds, and low in amplitude; 0.08 seconds is too wide, not too narrow."]],
 "c": 0, "cite": c(35)},

{"topic": "J point", "io": IOD, "slot": "normal values",
 "q": "In most leads, how far from the baseline may a normal J point sit?",
 "opts": [
  ["Within 1 millimeter",
   "Correct. The J point, where the QRS complex ends and the ST segment begins, should be at the baseline, with one millimeter of variance allowed."],
  ["Within 3 millimeters",
   "That allows far too much variance for most leads; the J point should be at the baseline with only 1 millimeter of variance."],
  ["Within 5 millimeters, one large box",
   "That is a whole large box of displacement; the J point should sit at the baseline with only 1 millimeter of variance."],
  ["Exactly on the baseline, with no allowance",
   "That is stricter than the rule; the J point should be at the baseline but 1 millimeter of variance is allowed."]],
 "c": 0, "cite": c(38)},

{"topic": "Heart rate", "io": IOD, "slot": "three hundred method",
 "q": "In a regular rhythm, one R wave sits on a heavy line and the next R wave lands on the fourth heavy line after it. What is the heart rate?",
 "opts": [
  ["75 beats per minute",
   "Correct. Counting down the heavy lines from the first R wave gives 300, 150, 100 and then 75 for the fourth line."],
  ["100 beats per minute",
   "That is the rate when the next R wave lands on the third heavy line; the fourth heavy line gives 75."],
  ["60 beats per minute",
   "That is the rate when the next R wave lands on the fifth heavy line; the fourth heavy line gives 75."],
  ["150 beats per minute",
   "That is the rate when the next R wave lands on the second heavy line; the fourth heavy line gives 75."]],
 "c": 0, "cite": c(53)},

]
