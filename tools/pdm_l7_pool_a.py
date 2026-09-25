# -*- coding: utf-8 -*-
# PDM I Lecture 7 (Principles of Electrocardiography, Ayelet Elwaya) -- pool A.
# Cardiac cell properties, the action potential and its five phases, the
# refractory periods, the conduction system, and the cardiac vector.
# Pool B carries leads, paper, the waves and intervals, and rate determination.
#
# THE NUMBER RULE DOES NOT APPLY TO THIS LECTURE THE WAY IT APPLIES TO THE REST
# OF THE COURSE, and that is deliberate rather than an oversight. Elsewhere in
# Principles of Diagnostic Medicine a figure never appears without the scale
# that reads it and nothing is calculated. Here the objectives say "Determine
# heart rate using an electrocardiogram" and "Measure and interpret" the PR
# interval and the rest, so intervals, thresholds and the two rate methods are
# the material rather than a violation of it. Questions still supply what a
# clinician would have in front of them -- the strip, the counts -- rather than
# asking for recall of a figure with no context.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "Principles of Electrocardiography.pptx"
def c(n):  return f"{SRC}, Slide {n}"

IOA = "Describe action potentials and impulse conduction through the cardiac conduction system"
IOB = "Define depolarization and repolarization"
IOC = "Define absolute and relative refractory periods"
IOD = "Describe the fundamental principles of electrocardiography"

POOL_A = [

{"topic": "Cardiac cell properties", "io": IOA, "slot": "definition",
 "q": "Which property refers to a cardiac cell's ability to produce its own impulse?",
 "opts": [
  ["Automaticity",
   "Correct. It is why the heart beats without instruction from anywhere else, and why several parts of it can take over pacemaking if the one above fails."],
  ["Excitability",
   "Excitability is the ability to respond to an impulse or stimulus rather than to generate one."],
  ["Conductivity",
   "Conductivity is the ability to pass an impulse from one myocyte to the next."],
  ["Contractility",
   "Contractility is the ability of the cell to shorten, which is the mechanical consequence rather than the electrical origin."]],
 "c": 0, "cite": c(3)},

{"topic": "Cardiac cell properties", "io": IOA, "slot": "definition",
 "q": "Which property allows an impulse to spread from one myocyte to the next?",
 "opts": [
  ["Conductivity",
   "Correct. It is what turns a single cell's discharge into a coordinated wave across the whole muscle."],
  ["Automaticity",
   "Automaticity is the ability to generate an impulse rather than to pass one along."],
  ["Excitability",
   "Excitability is the ability to respond to a stimulus, which is a property of the receiving cell rather than of the spread itself."],
  ["Contractility",
   "Contractility is the mechanical response to the impulse rather than its propagation."]],
 "c": 0, "cite": c(3)},

{"topic": "Depolarisation", "io": IOB, "slot": "definition",
 "q": "What does depolarization represent, and what is its relationship to contraction?",
 "opts": [
  ["Activation of cardiac tissue, and it precedes contraction",
   "Correct, and the order matters: the electrical event comes first, so an electrocardiogram showing depolarization does not prove the muscle actually contracted."],
  ["Recovery of cardiac tissue, and it follows contraction",
   "Recovery is repolarization; depolarization is activation and it comes before contraction."],
  ["Activation of cardiac tissue, occurring simultaneously with contraction",
   "The activation precedes the contraction rather than coinciding with it."],
  ["The resting state of the cell between beats",
   "The resting state is phase four, which is neither depolarization nor repolarization."]],
 "c": 0, "cite": c(4)},

{"topic": "Depolarisation", "io": IOB, "slot": "mechanism",
 "q": "What happens to the membrane during depolarization?",
 "opts": [
  ["It becomes less negative",
   "Correct. The cell moves away from its resting negativity, which is what the word depolarization describes."],
  ["It becomes more negative",
   "Becoming more negative is the direction of repolarization, returning toward rest."],
  ["It holds steady at its resting voltage",
   "Holding steady describes the resting state rather than depolarization."],
  ["It loses all charge separation entirely",
   "The membrane becomes less negative rather than losing charge separation completely."]],
 "c": 0, "cite": c(4)},

{"topic": "Action potential phases", "io": IOA, "slot": "sequence",
 "q": "In what order do the five phases of the cardiac action potential occur?",
 "opts": [
  ["Phase 4, then 0, 1, 2 and 3",
   "Correct. The numbering does not run in order, which is exactly why it is worth learning as a sequence rather than as a list: rest is phase four, and the upstroke that follows it is phase zero."],
  ["Phase 0, then 1, 2, 3 and 4",
   "This reads the numbers in order, but the cycle begins at the resting state, which is phase four."],
  ["Phase 1, then 2, 3, 4 and 0",
   "Neither the starting point nor the order matches the described sequence."],
  ["Phase 4, then 3, 2, 1 and 0",
   "The sequence runs from phase four into phase zero and then upward, not downward."]],
 "c": 0, "cite": c(5)},

{"topic": "Phase 4", "io": IOA, "slot": "mechanism",
 "q": "What is the ionic arrangement during phase 4, the resting state?",
 "opts": [
  ["More potassium inside the cell",
   "Correct. That separation is the stored charge the cell spends when it fires, and restoring it is what the later phases achieve. With sodium and calcium outside."],
  ["More sodium inside the cell, with potassium outside",
   "The arrangement is the other way round: potassium is the ion held inside at rest."],
  ["Equal concentrations of all ions across the membrane",
   "An equal distribution would leave no voltage across the membrane, and the resting cell holds a substantial one."],
  ["Calcium inside the cell with potassium outside",
   "Calcium sits outside at rest and enters later, during the plateau."]],
 "c": 0, "cite": c(6)},

{"topic": "Phase 4", "io": IOA, "slot": "interpretation",
 "q": "A cardiac cell is at minus ninety millivolts and able to respond to an impulse. Which phase is it in?",
 "opts": [
  ["Phase 4, the resting state",
   "Correct, and this is the phase in which the cell is ready and can respond, which is what distinguishes it from the refractory portion of the cycle."],
  ["Phase 0, the upstroke",
   "The upstroke is a rapid change away from the resting voltage rather than a steady state at it."],
  ["Phase 2, the plateau",
   "The plateau sits at a balanced voltage well above the resting level."],
  ["Phase 3, rapid repolarization",
   "Phase three is the return toward minus ninety rather than the steady state there."]],
 "c": 0, "cite": c(6)},

{"topic": "Phase 0", "io": IOA, "slot": "mechanism",
 "q": "What happens during phase 0, the upstroke?",
 "opts": [
  ["Fast sodium channels open and sodium rushes into the cell",
   "Correct. It is the fastest event in the cycle, and the rapid inward sodium current is what drives the voltage positive."],
  ["Calcium channels open and calcium enters the cell",
   "Calcium entry belongs to phase two, the plateau, and it is what triggers contraction."],
  ["Potassium channels open and potassium leaves the cell",
   "Potassium movement dominates the repolarizing phases rather than the upstroke."],
  ["Sodium is actively pumped out of the cell",
   "Active extrusion restores the gradient over time; the upstroke is a passive rapid influx."]],
 "c": 0, "cite": c(7)},

{"topic": "Phase 1", "io": IOA, "slot": "mechanism",
 "q": "What characterizes phase 1, early repolarization?",
 "opts": [
  ["Sodium channels close and potassium channels reopen",
   "Correct. The inward current stops and an outward one resumes, which begins bringing the membrane back down."],
  ["Calcium channels open, producing contraction",
   "Calcium entry and contraction belong to phase two, the plateau, rather than to early repolarization."],
  ["Fast sodium channels open",
   "Sodium channel opening is phase zero; in phase one they close."],
  ["The membrane returns fully to minus ninety millivolts",
   "The full return to resting voltage is completed in phase three rather than phase one."]],
 "c": 0, "cite": c(8)},

{"topic": "Phase 2", "io": IOA, "slot": "mechanism",
 "q": "Why is phase 2 called the plateau?",
 "opts": [
  ["Calcium entering the cell is matched by potassium moving the other way",
   "Correct, and the calcium entering during this balance is what actually produces contraction, so the flat part of the trace is the working part of the beat. So the voltage holds."],
  ["All ion movement stops entirely",
   "Ions continue to move; it is the balance between two currents that holds the voltage steady."],
  ["Sodium continues to enter at a constant rate",
   "Sodium channels have closed by this point; the inward current here is calcium."],
  ["The cell has returned to its resting voltage and remains there",
   "The plateau sits well above the resting voltage, which is reached again at the end of phase three."]],
 "c": 0, "cite": c(9)},

{"topic": "Phase 2", "io": IOA, "slot": "mechanism",
 "q": "Which ion entering the cell during the plateau causes contraction?",
 "opts": [
  ["Calcium",
   "Correct. It is the link between the electrical event and the mechanical one, which is why the plateau is where excitation becomes contraction."],
  ["Sodium",
   "Sodium drives the upstroke in phase zero rather than the contraction, which calcium triggers."],
  ["Potassium",
   "Potassium movement repolarizes the cell rather than triggering contraction."],
  ["Chloride",
   "Chloride is not among the ions described in these phases; sodium, potassium and calcium are."]],
 "c": 0, "cite": c(9)},

{"topic": "Phase 3", "io": IOA, "slot": "mechanism",
 "q": "What happens during phase 3, rapid repolarization?",
 "opts": [
  ["Calcium channels close while potassium channels remain open, returning the cell to minus ninety millivolts",
   "Correct. The inward current stops and the outward one continues unopposed, which is why this phase is the rapid one."],
  ["Calcium channels open and the voltage rises",
   "Calcium entry belongs to the plateau; in phase three the calcium channels close."],
  ["Fast sodium channels reopen",
   "Sodium channel reopening does not occur here; the cell is returning toward rest."],
  ["The membrane holds at a steady plateau voltage",
   "The steady plateau is phase two; phase three is the fall away from it."]],
 "c": 0, "cite": c(10)},

{"topic": "Refractory periods", "io": IOC, "slot": "definition",
 "q": "Over which part of the action potential does the ABSOLUTE refractory period run?",
 "opts": [
  ["From phase 0 to the middle of phase 3",
   "Correct, and it lasts about a hundred and eighty milliseconds, during which no stimulus of any strength will produce another action potential."],
  ["From the middle of phase 3 to the end of phase 3",
   "That span is the RELATIVE refractory period, in which a strong enough stimulus can succeed."],
  ["Throughout phase 4",
   "Phase four is the resting state, in which the cell is ready to respond rather than refractory."],
  ["From phase 1 to phase 2 only",
   "The absolute period begins at the upstroke and extends well past the plateau."]],
 "c": 0, "cite": c(11)},

{"topic": "Refractory periods", "io": IOC, "slot": "definition",
 "q": "What distinguishes the relative from the absolute refractory period?",
 "opts": [
  ["In the relative period a sufficiently strong stimulus can produce a response",
   "Correct. It is the dangerous window: the cell is excitable again but not yet fully recovered, so a stimulus arriving there can start something abnormal."],
  ["In the relative period no stimulus of any strength will produce a response",
   "That describes the absolute period; the relative one can be overcome."],
  ["The relative period occurs before the absolute period",
   "It runs from the middle to the end of phase three, after the absolute period."],
  ["The relative period occupies the whole of phase 4",
   "Phase four is the resting state, in which the cell responds normally."]],
 "c": 0, "cite": c(11)},

{"topic": "SA node", "io": IOA, "slot": "anatomy",
 "q": "Where does the sinoatrial node sit?",
 "opts": [
  ["In the upper wall of the right atrium",
   "Correct, and being the highest pacemaker in the chain is what makes it the one that normally sets the rate. Just below the opening of the vena cava."],
  ["At the junction of the atria and the ventricles",
   "That is where the atrioventricular node sits, near the coronary sinus, rather than the sinoatrial node."],
  ["Within the interventricular septum",
   "The septum carries the bundle of His and its branches rather than the sinoatrial node."],
  ["In the wall of the left atrium",
   "It sits in the upper wall of the RIGHT atrium, just below the opening of the vena cava."]],
 "c": 0, "cite": c(13)},

{"topic": "Pacemaker rates", "io": IOA, "slot": "interpretation",
 "q": "A heart is being paced at a rate in the forties, with no sinoatrial activity. Which pacemaker is most likely responsible?",
 "opts": [
  ["The atrioventricular node",
   "Correct. Its intrinsic rate is forty to sixty, and it takes over as the backup when the sinoatrial node fails."],
  ["The sinoatrial node",
   "The sinoatrial node paces at sixty to a hundred, and the question states it is not firing."],
  ["The Purkinje network",
   "The Purkinje network paces more slowly still, at twenty to forty."],
  ["The bundle of His alone",
   "The bundle of His conducts rather than being described as an independent pacemaker with its own rate."]],
 "c": 0, "cite": c(14)},

{"topic": "Pacemaker rates", "io": IOA, "slot": "interpretation",
 "q": "Which structure is described as the third pacemaker, taking over if both the sinoatrial and atrioventricular nodes fail?",
 "opts": [
  ["The Purkinje network",
   "Correct, at an intrinsic rate of twenty to forty -- slow enough to be a last resort rather than a comfortable substitute."],
  ["The bundle of His",
   "The bundle of His is the connection between the atrioventricular node and the bundle branches rather than the third pacemaker."],
  ["The left anterior fascicle",
   "The fascicles are branches of the conducting pathway rather than a named pacemaker."],
  ["The internodal tracts",
   "These connect the sinoatrial node to the atrioventricular node rather than pacing the heart."]],
 "c": 0, "cite": c(17)},

{"topic": "Internodal pathways", "io": IOA, "slot": "anatomy",
 "q": "Which internodal tract does the majority of the population use?",
 "opts": [
  ["The superior anterior, or fast, tract",
   "Correct. The other two usually terminate before reaching the atrioventricular node, so the fast tract does most of the work."],
  ["The middle tract",
   "The middle tract is one of the three but is not the one most people use."],
  ["The inferior posterior, or slow, tract",
   "The slow tract is one of the three but is not the predominant route."],
  ["All three equally",
   "The superior anterior tract predominates rather than the three sharing the load."]],
 "c": 0, "cite": c(13)},

{"topic": "AV node", "io": IOA, "slot": "mechanism",
 "q": "What two things does the atrioventricular node do to the impulse passing through it?",
 "opts": [
  ["It introduces a short pause and amplifies the signal",
   "Correct. The pause is what lets the atria finish emptying before the ventricles contract, so a delay in the conduction system is doing useful mechanical work."],
  ["It speeds the impulse up and attenuates it",
   "It delays rather than accelerates, and it amplifies rather than attenuates."],
  ["It blocks every second impulse by design",
   "Blocking alternate impulses is a pathological pattern rather than normal nodal behavior."],
  ["It reverses the direction of the impulse",
   "The impulse continues onward toward the ventricles; the node delays and amplifies it rather than reversing it."]],
 "c": 0, "cite": c(14)},

{"topic": "Bundle of His", "io": IOA, "slot": "anatomy",
 "q": "What is distinctive about the bundle of His in a normal heart?",
 "opts": [
  ["It is the only electrical pathway crossing from the atria to the ventricles",
   "Correct. Everything above and below has to go through it, which is why a block there separates the two halves of the heart electrically."],
  ["It is one of several pathways crossing the atrioventricular junction",
   "In a normal heart it is the only one; additional pathways are abnormal."],
  ["It paces the heart at sixty to a hundred beats per minute",
   "That intrinsic rate belongs to the sinoatrial node; the bundle of His is a conducting pathway rather than a pacemaker."],
  ["It lies within the atrial wall",
   "It connects the atrioventricular node to the bundle branches across the nonconductive wall between the chambers."]],
 "c": 0, "cite": c(14)},

{"topic": "Bundle branches", "io": IOA, "slot": "anatomy",
 "q": "Into how many fascicles does the left bundle branch divide, and what are they?",
 "opts": [
  ["Three: left anterior, left posterior and septal",
   "Correct. The septal fascicle is the one most often forgotten, which matters because the three-fascicle arrangement is what makes bifascicular block possible. The left anterior."],
  ["Two: the left anterior and the left posterior",
   "A third, the interventricular septal fascicle, is described alongside these two."],
  ["Four, one to each wall of the ventricle",
   "Three fascicles are described: the left posterior, the interventricular septal and the left anterior."],
  ["It does not divide; it terminates directly in Purkinje fibers",
   "It divides into fascicles before becoming the Purkinje network."]],
 "c": 0, "cite": c(15)},

{"topic": "Bundle branches", "io": IOA, "slot": "anatomy",
 "q": "What is noted about the length of the right bundle branch?",
 "opts": [
  ["It is much longer than the left, despite the left ventricle being the larger chamber",
   "Correct, and the counterintuitiveness is the point: the anatomy does not follow chamber size."],
  ["It is much shorter than the left, in proportion to the smaller right ventricle",
   "It is described as the longer of the two despite serving the smaller chamber."],
  ["The two are of equal length",
   "They are explicitly contrasted: the right bundle branch is much longer despite serving the smaller ventricle."],
  ["It does not reach the Purkinje network",
   "It terminates in the Purkinje network, as the left bundle branch does through its fascicles."]],
 "c": 0, "cite": c(16)},

{"topic": "Cardiac vector", "io": IOD, "slot": "definition",
 "q": "What does a cardiac vector represent?",
 "opts": [
  ["The direction and strength of the electrical impulse",
   "Correct. Both quantities at once, which is why it is drawn as an arrow rather than described as a line."],
  ["The direction of blood flow through the chambers",
   "It describes electrical activity rather than mechanical flow."],
  ["The strength of contraction alone",
   "It carries direction as well as magnitude, and it is electrical rather than mechanical."],
  ["The position of the heart within the chest",
   "It describes the electrical impulse rather than anatomical position."]],
 "c": 0, "cite": c(18)},

{"topic": "Cardiac vector", "io": IOD, "slot": "mechanism",
 "q": "In which direction does conduction truly travel through the heart?",
 "opts": [
  ["Left and down, toward the anterior chest",
   "Correct, and this is why lead II sees the beat so well: it looks along that axis."],
  ["Right and up, toward the shoulder",
   "The described pathway runs leftward and downward rather than to the right and upward."],
  ["Straight downward, in the coronal plane only",
   "The described direction has a leftward and anterior component as well as a downward one."],
  ["Posteriorly, away from the chest wall",
   "It runs left and down toward the anterior chest rather than posteriorly away from it."]],
 "c": 0, "cite": c(18)},
]
