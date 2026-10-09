#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write the PDM I Exam 3 Arcade card fragments for Lectures 11 and 12.

    tools/pdm_e3/l11_cards.json  {"pdm-rhythm-analysis-sinus": [[front, back], ...]}
    tools/pdm_e3/l12_cards.json  {"pdm-ectopy-supraventricular": [[front, back], ...]}

Same shape as tools/pdm_e2_cards.json, consumed by the assembler's Arcade step. ATOMIC FACTS ONLY
(arcade_content_policy): one fact per card, short backs, every back unique within its deck so
Match and the Learn/Sprint distractor picker never show two identical answers. Every fact is in
the lecture's guide fragment (tools/pdm_e3/l1N_guide.html) and its deck; truth-over-slide items
are carried as the truth (potassium efflux in phase 3; no "six in a row" card; no "agonal" card).
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

L11 = [
 ["Which structure is the main pacemaker of the heart?", "The sinoatrial node"],
 ["Where does the sinoatrial node sit?", "In the upper right atrial wall, just below the superior vena cava"],
 ["What is the sinoatrial node's intrinsic rate?", "60 to 100 beats per minute"],
 ["Which structure is the backup pacemaker if the sinoatrial node fails?", "The atrioventricular node"],
 ["What is the atrioventricular node's intrinsic rate?", "40 to 60 beats per minute"],
 ["Which structure paces the heart when both nodes fail?", "The Purkinje network"],
 ["What is the Purkinje network's intrinsic rate?", "20 to 40 beats per minute"],
 ["Which cells conduct action potentials fastest of all?", "The Purkinje fibers"],
 ["Which bundle carries the impulse from the right to the left atrium?", "Bachmann's bundle"],
 ["In most people, which internodal tract truly attaches to the atrioventricular node?", "The superior anterior, or fast, tract"],
 ["In a normal heart, what is the only path from atria to ventricles?", "The bundle of His"],
 ["What separates the atria from the ventricles electrically?", "The nonconductive atrioventricular septum"],
 ["How many fascicles does the left bundle branch split into?", "Three: posterior, septal and anterior"],
 ["Which fascicle depolarizes the septum and makes the Q wave?", "The interventricular septal fascicle"],
 ["How does the right bundle branch compare with the left?", "It is a much longer piece of tissue"],
 ["What share of ventricular filling is passive?", "70 to 80 percent"],
 ["Which cell property is producing its own impulse?", "Automaticity"],
 ["Which cell property is responding to a stimulus?", "Excitability"],
 ["What keeps the lower pacemaker cells from firing on their own?", "The natural hierarchy of pacemaker function"],
 ["In what order do the action potential phases run from rest?", "4, 0, 1, 2, 3"],
 ["What is the resting voltage inside a cardiac cell?", "About minus 90 millivolts"],
 ["Which ion rushes in during phase 0?", "Sodium, through fast sodium channels"],
 ["What is phase 1 of the action potential called?", "Early repolarization, the notch"],
 ["Which ion enters in phase 2 and causes contraction?", "Calcium"],
 ["Which ion movement repolarizes the cell in phase 3?", "Potassium flowing out of the cell"],
 ["How does a cell respond during the absolute refractory period?", "It does not respond to any stimulus"],
 ["How does a cell respond during the relative refractory period?", "It responds, but the cells are very fragile"],
 ["Which landmark divides the absolute from the relative refractory period?", "The peak of the T wave"],
 ["What is the normal direction of the heart's vector?", "Left and down, toward the front of the body"],
 ["Why is lead II used for rhythm interpretation?", "It has a perfect view of the heart's vector"],
 ["How long is one small box at standard speed?", "0.04 seconds"],
 ["How long is one large box at standard speed?", "0.2 seconds, five small boxes"],
 ["What does the vertical axis of the paper measure?", "Voltage"],
 ["How tall is a standard calibration mark?", "10 millimeters, two large boxes"],
 ["What does the P wave represent?", "Atrial depolarization"],
 ["What is the normal PR interval?", "0.12 to 0.20 seconds, three to five small boxes"],
 ["What is the upper limit of a normal QRS duration?", "Under 0.12 seconds"],
 ["What does a QRS of 0.12 seconds or more mean?", "Abnormal conduction through the ventricles"],
 ["What duration keeps a Q wave normal?", "Under 0.04 seconds"],
 ["Why is the R wave upright in lead II?", "Ventricular depolarization moves toward lead II"],
 ["Why is the S wave negative in lead II?", "Its depolarization moves away from lead II"],
 ["What is a terminal deflection that never crosses baseline called?", "An S wave pattern"],
 ["Where is the J point?", "Where the QRS ends and the ST segment begins"],
 ["What does the QT interval represent?", "All ventricular activity in one cardiac cycle"],
 ["Which segment is the best reference for the isoelectric line?", "The TP segment"],
 ["What are the five steps of the systematic approach, in order?", "Rate, regularity, P waves, PR interval, QRS"],
 ["What does a P wave before every QRS tell you about origin?", "The rhythm starts in the atria"],
 ["What does it mean that P waves are married to the QRS?", "Each P wave is causing its QRS"],
 ["How is the ventricular rate found with the six-second method?", "QRS complexes in six seconds times ten"],
 ["Which rate method is the most accurate?", "The 1500 method, using small boxes"],
 ["Below what rate is the count-down method unreliable?", "Below 50 per minute"],
 ["What should be used when regularity is uncertain?", "Calipers on consecutive R to R intervals"],
 ["Where is the positive electrode of lead II?", "On the left foot"],
 ["What is the negative pole of the augmented leads?", "A theoretical central terminal in the heart"],
 ["Where is V1 placed?", "Fourth intercostal space, right of the sternum"],
 ["Where is V4 placed?", "Fifth intercostal space, midclavicular line"],
 ["Which leads look at the inferior wall?", "II, III and aVF (augmented vector foot)"],
 ["Which leads look at the septal wall?", "V1 and V2"],
 ["What view do the precordial leads give?", "A horizontal view of the heart"],
 ["What separates sinus bradycardia and tachycardia from normal sinus rhythm?", "The rate alone"],
 ["What rate defines sinus bradycardia?", "Under 60 per minute"],
 ["What rate defines sinus tachycardia?", "Over 100 per minute"],
 ["What separates sinus arrhythmia from normal sinus rhythm?", "Irregular R to R intervals"],
 ["In whom is sinus arrhythmia most commonly seen?", "Children; it is benign"],
 ["What happens to the heart rate on inspiration in sinus arrhythmia?", "It rises, because vagal tone is suppressed"],
 ["In sinus exit block, what is the sinus node doing?", "Firing normally, but its impulse is blocked"],
 ["After a sinus exit block, what do the P to P intervals do?", "They still march out on schedule"],
 ["Why do beats fail to march out after a sinus pause?", "The sinus node stops and resets"],
 ["What separates sinus arrest from a sinus pause?", "At least three missed cardiac cycles"],
 ["What is sick sinus syndrome?", "Exit block, pause and arrest in the same patient"],
]

L12 = [
 ["Where does a premature atrial complex originate?", "In the atria, outside the sinoatrial node"],
 ["What usually causes premature atrial complexes?", "Increased automaticity"],
 ["Which P wave marks a premature atrial complex?", "An early P wave of different shape"],
 ["Which P wave findings fit a premature junctional complex?", "None, inverted, or after the QRS"],
 ["What is the significance of an isolated premature junctional complex?", "None clinically"],
 ["How wide is a ventricular beat typically?", "Over 0.12 seconds"],
 ["Which way does a ventricular beat's T wave point?", "Opposite the QRS"],
 ["What is a premature beat every other beat called?", "Bigeminy"],
 ["What is a premature beat every third beat called?", "Trigeminy"],
 ["What is a premature beat every fourth beat called?", "Quadrigeminy"],
 ["Which premature beats can form bigeminy or trigeminy?", "Atrial, junctional and ventricular alike"],
 ["What are two premature ventricular complexes in a row called?", "A couplet"],
 ["What does an identical shape on every premature ventricular complex mean?", "Unifocal: one ectopic focus"],
 ["What do differently shaped premature ventricular complexes mean?", "Multifocal: several ventricular foci"],
 ["Why is R on T dangerous?", "It can trigger ventricular tachycardia or fibrillation"],
 ["What can frequent grouped premature ventricular complexes do to output?", "Reduce cardiac output"],
 ["When does an escape beat arrive?", "Late, past the next expected R wave"],
 ["What causes a junctional escape beat?", "The sinus node failing or firing too slowly"],
 ["What causes a ventricular escape complex?", "Both the sinus and atrioventricular nodes failing"],
 ["What happens in a junctional escape rhythm?", "The atrioventricular node takes over and suppresses the sinus node"],
 ["What is the rate of a junctional escape rhythm?", "40 to 60 per minute"],
 ["What is the rate of an accelerated junctional rhythm?", "60 to 100 per minute"],
 ["What is the rate of junctional tachycardia?", "Over 100 per minute"],
 ["What regularity do junctional rhythms have?", "Regular, by definition"],
 ["Why is a junctional P wave inverted in lead II?", "The atria depolarize from the bottom up"],
 ["When does a junctional rhythm show no P wave?", "When atria and ventricles depolarize together"],
 ["Where does a junctional impulse start if its P falls after the QRS?", "In the trigger zone"],
 ["What PR interval goes with a junctional P wave before the QRS?", "Under 0.12 seconds"],
 ["Which atrioventricular node zone causes most premature junctional complexes?", "The transition zone"],
 ["Which atrioventricular node zone slows conduction and backs up the sinus node?", "The compact zone"],
 ["Which structure paces an idioventricular rhythm?", "The Purkinje network takes over"],
 ["What is the rate of idioventricular rhythm?", "20 to 40 per minute"],
 ["What is the rate of accelerated idioventricular rhythm?", "40 to 100 per minute"],
 ["What does idioventricular rhythm look like?", "Regular, wide, with no P waves"],
 ["What QRS width usually separates junctional from idioventricular rhythm?", "Narrow for junctional, wide for idioventricular"],
 ["How many P wave shapes define a wandering atrial pacemaker?", "At least three"],
 ["What separates multifocal atrial tachycardia from a wandering atrial pacemaker?", "A rate over 100 rather than under 100"],
 ["What causes atrial flutter?", "A reentry circuit in the atria"],
 ["Where does the flutter circuit most often run?", "The right atrium"],
 ["Which tissue changes set up atrial flutter?", "Enlarged, scarred or ischemic atrial tissue"],
 ["Which pattern is pathognomonic of atrial flutter?", "The sawtooth baseline"],
 ["What atrial rate do flutter waves usually represent?", "About 300 per minute"],
 ["How is a flutter strip with a changing ratio documented?", "Atrial flutter with variable conduction"],
 ["How are flutter waves counted for the ratio?", "Count troughs to the next QRS"],
 ["What happens in the atria in atrial fibrillation?", "Many sites fire chaotically and suppress the sinus node"],
 ["What mechanical function is lost in atrial fibrillation?", "The atrial kick"],
 ["What replaces P waves in atrial fibrillation?", "Fibrillatory waves"],
 ["What regularity defines atrial fibrillation?", "Irregularly irregular"],
 ["What is the atrial rate in atrial fibrillation?", "Indeterminate"],
 ["What is atrioventricular nodal reentrant tachycardia commonly called?", "Supraventricular tachycardia"],
 ["What is the rate range of supraventricular tachycardia?", "150 to 300 per minute"],
 ["Which P waves does supraventricular tachycardia show?", "None visible, or retrograde"],
 ["What usually triggers atrioventricular nodal reentrant tachycardia?", "An ectopic beat, typically a premature atrial complex"],
 ["How does the typical reentry circuit travel?", "Down the slow tract and up the fast tract"],
 ["What marks the atypical form of the reentry tachycardia?", "Clearly visible retrograde P waves"],
 ["What are pseudo S waves?", "Retrograde P waves buried at the end of the QRS"],
 ["A sinus P wave precedes every QRS at 190 per minute. What is the rhythm?", "Sinus tachycardia"],
 ["If one wave between rapid QRS complexes could be P or T, call it what?", "A T wave"],
]

DECKS = (("l11_cards.json", "pdm-rhythm-analysis-sinus", L11), ("l12_cards.json", "pdm-ectopy-supraventricular", L12))

if __name__ == "__main__":
    for fn, key, cards in DECKS:
        backs = [b for _, b in cards]
        assert len(backs) == len(set(backs)), sorted({b for b in backs if backs.count(b) > 1})
        assert len({f for f, _ in cards}) == len(cards)
        for f, b in cards:
            assert f.endswith("?") and len(b.split()) <= 14, (f, b)
        json.dump({key: cards}, open(os.path.join(HERE, "pdm_e3", fn), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print("wrote tools/pdm_e3/%s  %s: %d cards" % (fn, key, len(cards)))
