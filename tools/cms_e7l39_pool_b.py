# -*- coding: utf-8 -*-
"""Lecture 39 objective pool B -- Phases of Sleep: rapid eye movement sleep (episodes, paradoxical sleep, atonia,
recordings, dreaming) and non-rapid eye movement sleep (autonomic changes, stages N1-N3, age, dreams)
(slides 5-7, 9, 10, 12-14, 19, 27-28).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md (Jaxon, 2026-10-29).

Held back on purpose (cms_e7l39_scope.py SLIDE CONFLICTS): no item asks whether rapid eye movement sleep or N3
is harder to wake from, how many non-rapid eye movement stages there are, or which stage holds sleep spindles
or K complexes. The slide line "dreams during REM are associated with more bodily muscle activity" (s13) sits
against "muscle tone is very depressed" (s10) and "atonia" (s28), so no item keys muscle ACTIVITY in rapid eye
movement sleep; muscle TONE items key "very depressed"/atonia, which s10 and s28 agree on.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l39_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


COMA = "Sleep versus coma"
CYC = "Sleep cycles"
REM = "Rapid eye movement sleep"
NREM = "Non-rapid eye movement sleep"
FUN = "Functions of sleep"
SWC = "The sleep-wake cycle"
WAV = "Brain waves"
EEG = "Electroencephalogram across the stages"

QUESTIONS = [

# ---------------------------------------------------------------- rapid eye movement sleep
S(REM, IO_SWS,
  "How long does each rapid eye movement episode last?",
  [["5 to 30 minutes",
    "Correct. Each rapid eye movement episode lasts 5 to 30 minutes and recurs about every 90 minutes. Episodes are short, or even absent, when a person is extremely sleepy, and they lengthen as the person becomes more rested."],
   ["45 to 60 minutes",
    "Forty-five to 60 minutes is longer than any rapid eye movement episode, which lasts 5 to 30 minutes even when episodes lengthen late in the night. Tell: an episode lasts under half an hour.", "reversed direction or value"],
   ["90 to 120 minutes",
    "Ninety to 120 minutes is the length of a whole sleep cycle, which holds non-rapid eye movement stages as well as one rapid eye movement episode. Tell: the cycle is 90 to 120 minutes; the episode within it is 5 to 30.", "adjacent fact"],
   ["150 to 180 minutes",
    "Two and a half to three hours exceeds even a full 90 to 120 minute sleep cycle, so no single rapid eye movement episode could last that long. Tell: an episode fits inside one cycle, at 5 to 30 minutes.", "reversed direction or value"]],
  CS(6, 9), "manifestation"),

S(REM, IO_SWS,
  "During rapid eye movement sleep, by up to how much can overall brain metabolism rise?",
  [["Up to 20%",
    "Correct. Overall brain metabolism can increase by as much as 20% during rapid eye movement sleep because brain activity rises; the brain is very active, and the electroencephalogram shows patterns similar to wakefulness."],
   ["Up to 10%",
    "Ten percent understates the rise: overall brain metabolism can increase by as much as 20% in this active, dreaming state, when the electroencephalogram resembles wakefulness. Tell: the rise reaches a fifth, not a tenth.", "reversed direction or value"],
   ["Up to 30%",
    "Thirty percent is the upper end of the 10 to 30% fall in blood pressure, heart rate, breathing rate and metabolic rate during non-rapid eye movement sleep. Tell: 10 to 30% is a non-rapid eye movement decrease; 20% is the rapid eye movement rise.", "adjacent fact"],
   ["Up to 50%",
    "Half again would overstate it: the rise in overall brain metabolism during rapid eye movement sleep reaches as much as 20%, enough to reflect a brain as active as an awake one. Tell: the ceiling is 20%.", "reversed direction or value"]],
  CS(10, 12), "manifestation"),

S(REM, IO_SWS,
  "Why is rapid eye movement sleep also called paradoxical sleep?",
  [["Its brain waves resemble wakefulness",
    "Correct. During rapid eye movement sleep the electroencephalogram shows brain wave patterns similar to those during wakefulness, beta waves, even though the person is asleep. That contrast between an awake-looking brain and a sleeping person is why it is also called paradoxical sleep."],
   ["Its muscle tone exceeds waking tone",
    "Muscle tone is very depressed in rapid eye movement sleep, with atonia of voluntary muscles except the eyes and diaphragm. Tell: the paradox is awake-like brain waves in a sleeping body without muscle tone, not extra tone.", "reversed direction or value"],
   ["It is the most restful sleep",
    "Rapid eye movement sleep is not restful or deep; the deep, restful sleep is non-rapid eye movement sleep, deepest in stage N3. Tell: restfulness belongs to non-rapid eye movement sleep, not to the paradoxical state.", "reversed direction or value"],
   ["It lowers heart rate by 10 to 30%",
    "A 10 to 30% fall in heart rate, blood pressure, breathing rate and metabolic rate belongs to non-rapid eye movement sleep. In rapid eye movement sleep heart and breathing rates become irregular. Tell: steady slowing is non-rapid eye movement sleep.", "competing diagnosis"]],
  CS(6, 10, 12, 28), "test finding"),

S(REM, IO_SWS,
  "What happens to muscle tone during rapid eye movement sleep?",
  [["It is very depressed",
    "Correct. Muscle tone is very depressed during rapid eye movement sleep, which indicates inhibition of the spinal muscle control areas. The muscle recording shows atonia of voluntary muscles, sparing the eye muscles and the diaphragm."],
   ["It rises above waking tone",
    "Tone falls, not rises: rapid eye movement sleep brings atonia of voluntary muscles, inactivity due to inhibited alpha motor neurons. Tell: the brain is active, but the body is atonic.", "reversed direction or value"],
   ["It matches the awake state",
    "The brain waves of rapid eye movement sleep resemble the awake state, but the muscles do not: the beta waves come paired with atonia of voluntary muscles. Tell: an awake-looking brain sits in an atonic body.", "adjacent fact"],
   ["It is lost mainly in the diaphragm",
    "The diaphragm is one of the muscles spared, along with the eye muscles, so breathing continues while other voluntary muscles are atonic. Tell: the eye muscles and diaphragm keep working; the rest of the voluntary muscles go slack.", "reversed direction or value"]],
  CS(10, 28), "manifestation"),

S(REM, IO_SWS,
  "Which muscles are spared from the atonia of rapid eye movement sleep?",
  [["Eye muscles and diaphragm",
    "Correct. Rapid eye movement sleep brings atonia of voluntary muscles except the eye muscles and the diaphragm. The eyes still make irregular, sharply peaked movements, and the diaphragm keeps breathing going."],
   ["Limb muscles and diaphragm",
    "The diaphragm is spared, but limb muscles are voluntary muscles and share the atonia. The eye muscles, not the limbs, are the other exception. Tell: the two exceptions are the eye muscles and the diaphragm.", "adjacent fact"],
   ["Eye and limb muscles",
    "The eye muscles are spared, but limb muscles are not: the atonia of voluntary muscles includes the limbs. The diaphragm is the second exception. Tell: pair the eye muscles with the diaphragm.", "adjacent fact"],
   ["Trunk and neck muscles",
    "Trunk and neck muscles are voluntary muscles and become atonic in rapid eye movement sleep, because alpha motor neurons are inhibited. Tell: the exceptions are the eye muscles and diaphragm, which keep the eyes moving and the breathing going.", "reversed direction or value"]],
  CS(10, 28), "manifestation"),

S(REM, IO_SWS,
  "What causes the muscle inactivity of rapid eye movement sleep?",
  [["Inhibited alpha motor neurons",
    "Correct. The atonia of rapid eye movement sleep is inactivity due to inhibited alpha motor neurons, which matches the very depressed muscle tone that indicates inhibition of the spinal muscle control areas. The eye muscles and diaphragm are spared."],
   ["Fatigued reticular activating neurons",
    "Fatigue of reticular activating neurons, after many hours awake, explains the transition from wakefulness to sleep, not muscle atonia within rapid eye movement sleep. Tell: atonia comes from inhibition of motor neurons, not from fatigue of the activating system.", "adjacent fact"],
   ["Increased parasympathetic tone",
    "Increased parasympathetic tone is a physiologic change of non-rapid eye movement sleep, with low blood pressure and a slow heart rate. It does not explain the atonia of rapid eye movement sleep. Tell: parasympathetic tone is a non-rapid eye movement change.", "confused mechanism or drug class"],
   ["Decreased peripheral vascular tone",
    "Decreased peripheral vascular tone accompanies non-rapid eye movement sleep along with falling blood pressure and heart rate; it concerns blood vessels, not voluntary muscle activity. Tell: vascular tone is not skeletal muscle tone.", "confused mechanism or drug class"]],
  CS(10, 12, 14, 19, 28), "etiology"),

S(REM, IO_SWS,
  "How do heart rate and breathing rate behave during rapid eye movement sleep?",
  [["They become irregular",
    "Correct. In rapid eye movement sleep heart rate and breathing rate become irregular, which is characteristic of the dream state, alongside rapid eye movements and an active brain. Non-rapid eye movement sleep instead brings a slow heart rate and a decreased breathing rate."],
   ["They fall by 10 to 30%",
    "A 10 to 30% fall in heart rate, breathing rate, blood pressure and metabolic rate describes non-rapid eye movement sleep. Tell: a steady fall is non-rapid eye movement sleep; irregularity is rapid eye movement sleep.", "competing diagnosis"],
   ["They slow with parasympathetic tone",
    "Increased parasympathetic tone with a slow heart rate and decreased breathing rate is the physiology of non-rapid eye movement sleep, not of the dream state. Tell: parasympathetic slowing marks non-rapid eye movement sleep.", "competing diagnosis"],
   ["They rise steadily with metabolism",
    "Overall brain metabolism can rise by up to 20% in rapid eye movement sleep, but heart and breathing rates do not climb steadily; they become irregular. Tell: the rhythm turns irregular rather than steadily faster.", "confused mechanism or drug class"]],
  CS(10, 12, 14), "manifestation"),

S(REM, IO_SWS,
  "Which state combines vivid dreaming, irregular heart and breathing rates, and very depressed muscle tone?",
  [["Rapid eye movement sleep",
    "Correct. Rapid eye movement sleep is the active, dreaming form of sleep: dreams are vivid, heart and breathing rates become irregular, and muscle tone is very depressed, with atonia of voluntary muscles except the eyes and diaphragm."],
   ["Non-rapid eye movement sleep",
    "Non-rapid eye movement sleep has less vivid dreams and increased parasympathetic tone with a slow heart rate and decreased breathing rate, so irregular vital signs and vivid dreaming do not fit. Tell: steady slowing and dimmer dreams mean non-rapid eye movement sleep.", "competing diagnosis"],
   ["Quiet wakefulness",
    "Quiet wakefulness is a relaxed, awake state with the eyes closed and alpha waves; the person is not dreaming and has no sleep atonia. Tell: dreaming requires sleep, so no waking state fits.", "ruled out by a stated finding"],
   ["Alert wakefulness",
    "Alert wakefulness shares beta waves with rapid eye movement sleep, but the person is awake and processing information, not dreaming with very depressed muscle tone. Tell: beta waves plus atonia and dreams means rapid eye movement sleep.", "competing diagnosis"]],
  CS(9, 10, 14, 27, 28), "differential"),

S(REM, IO_SWS,
  "Despite brain waves that resemble wakefulness, what is the state of a person in rapid eye movement sleep?",
  [["Asleep, not fully aware of surroundings",
    "Correct. In rapid eye movement sleep the brain is very active and its waves resemble wakefulness, yet the person is asleep and not fully aware of the surroundings. That mismatch is why the state is also called paradoxical sleep."],
   ["Awake but unable to move the limbs",
    "The limbs are atonic in rapid eye movement sleep, but the person is asleep, not awake; the awake-like brain waves are the paradox, not evidence of waking. Tell: atonia with dreaming is sleep.", "common lay belief"],
   ["Unarousable by stimuli, as in coma",
    "Rapid eye movement sleep is sleep, and sleep is unconsciousness from which stimuli can arouse a person; people can even awaken spontaneously from it in the morning. Tell: arousable means sleep, not coma.", "competing diagnosis"],
   ["Awake and relaxed with eyes closed",
    "Awake relaxation with the eyes closed is quiet wakefulness, marked by alpha waves rather than the beta waves of rapid eye movement sleep. Tell: alpha means a resting, awake person; beta during sleep means rapid eye movement sleep.", "competing diagnosis"]],
  CS(5, 9, 10, 28), "differential"),

S(REM, IO_SWS,
  "How do dreams of rapid eye movement sleep compare with dreams of non-rapid eye movement sleep?",
  [["More vivid",
    "Correct. Rapid eye movement sleep is associated with vivid dreaming in a very active brain, whereas non-rapid eye movement sleep brings less vivid dreams. Dreams and nightmares still occur in non-rapid eye movement sleep, but they are dimmer and often not remembered."],
   ["Less vivid",
    "That reverses the contrast: non-rapid eye movement sleep has the less vivid dreams, and rapid eye movement sleep the vivid ones. Tell: the active, high-metabolism brain of rapid eye movement sleep dreams vividly.", "reversed direction or value"],
   ["Equally vivid",
    "The two types differ: rapid eye movement dreaming is vivid, and non-rapid eye movement dreams are less vivid. Tell: vividness is one of the clearest contrasts between the two types of sleep, so they are not equal.", "adjacent fact"],
   ["Less often remembered",
    "Poor recall is the feature of non-rapid eye movement dreams, which are often not remembered because they are not consolidated in memory. Tell: forgotten dreams point to non-rapid eye movement sleep, not to the vivid dreams of rapid eye movement sleep.", "reversed direction or value"]],
  CS(9, 13, 14), "differential"),

S(REM, IO_SWS,
  "Which recording shows the atonia of voluntary muscles during rapid eye movement sleep?",
  [["Electromyogram",
    "Correct. The electromyogram, the muscle recording, shows atonia of voluntary muscles in rapid eye movement sleep, sparing the eye muscles and diaphragm, as inactivity due to inhibited alpha motor neurons."],
   ["Electrooculogram",
    "The electrooculogram records the eyes, and in rapid eye movement sleep it shows irregular, sharply peaked eye movements, not voluntary muscle atonia. Tell: the eye recording shows eye movements; the muscle recording shows atonia.", "adjacent fact"],
   ["Electroencephalogram",
    "The electroencephalogram records brain waves: in rapid eye movement sleep a mixed, low-voltage pattern with sawtooth waves and beta waves like wakefulness. It does not measure muscle tone. Tell: brain waves are not muscle tone.", "adjacent fact"],
   ["Blood pressure recording",
    "Blood pressure tracks vascular changes, falling by 10 to 30% in non-rapid eye movement sleep along with decreased peripheral vascular tone; it does not show voluntary muscle activity. Tell: atonia is read from the muscle recording.", "adjacent fact"]],
  CS(12, 28), "initial test"),

S(REM, IO_SWS,
  "Which recording shows the irregular, sharply peaked eye movements of rapid eye movement sleep?",
  [["Electrooculogram",
    "Correct. The electrooculogram, the eye-movement recording, shows the irregular, sharply peaked eye movements of rapid eye movement sleep. The eye muscles are spared from the atonia that affects other voluntary muscles, so the eyes keep moving."],
   ["Electromyogram",
    "The electromyogram records muscle activity and in rapid eye movement sleep shows atonia of voluntary muscles; the eye movements themselves are read from the eye-movement recording. Tell: atonia on the muscle recording, eye movements on the eye recording.", "adjacent fact"],
   ["Electroencephalogram",
    "The electroencephalogram shows brain waves, a mixed, low-voltage pattern with sawtooth waves in rapid eye movement sleep, not the movements of the eyes. Tell: sawtooth waves are brain activity, not eye movement.", "adjacent fact"],
   ["Blood pressure recording",
    "Blood pressure falls with non-rapid eye movement sleep and says nothing about eye movement. Heart and breathing rates turn irregular in rapid eye movement sleep, but eye movements need their own recording. Tell: the eyes are read from the electrooculogram.", "adjacent fact"]],
  CS(10, 12, 28), "initial test"),

S(REM, IO_SWS,
  "Which circumstance makes rapid eye movement episodes short or even absent?",
  [["Extreme sleepiness",
    "Correct. When a person is extremely sleepy, each rapid eye movement episode is short or even absent. As the person becomes more restful and less sleepy, the duration of rapid eye movement episodes increases, so the later periods of a night are longer."],
   ["Being well rested",
    "Being rested has the opposite effect: as a person becomes more restful and less sleepy, rapid eye movement episodes lengthen, which is why the later periods of a night are longer. Tell: sleepiness shortens the episodes; rest lengthens them.", "reversed direction or value"],
   ["Young adulthood",
    "Young adulthood is the age at which rapid eye movement sleep is given as about 25% of sleep time, a normal share; it is not a cause of short or absent episodes. Tell: 25% is a young adult's ordinary share of rapid eye movement sleep.", "adjacent fact"],
   ["The late cycles of the night",
    "The late cycles carry the longest rapid eye movement periods, as the sleeper has become more rested and the deepest sleep is over. Tell: rapid eye movement periods grow, rather than shrink, toward morning.", "reversed direction or value"]],
  CS(7, 9), "risk factors"),

# ---------------------------------------------------------------- non-rapid eye movement sleep
S(NREM, IO_SWS,
  "Which autonomic change marks non-rapid eye movement sleep?",
  [["Increased parasympathetic tone",
    "Correct. Non-rapid eye movement sleep brings increased parasympathetic tone, with low blood pressure, a slow heart rate and a decreased breathing rate. Blood pressure, heart rate, breathing rate and metabolic rate fall by 10 to 30%."],
   ["Increased peripheral vascular tone",
    "Peripheral vascular tone decreases, not increases, during non-rapid eye movement sleep, along with other vegetative bodily functions. Tell: vascular tone falls as blood pressure falls, so an increase points the wrong way.", "reversed direction or value"],
   ["Irregular heart and breathing rates",
    "Irregular heart and breathing rates belong to rapid eye movement sleep, characteristic of the dream state. Non-rapid eye movement sleep slows them instead. Tell: irregular vital signs mean rapid eye movement sleep.", "competing diagnosis"],
   ["Rising blood pressure",
    "Blood pressure falls by 10 to 30% in non-rapid eye movement sleep under increased parasympathetic tone. Tell: low blood pressure, a slow heart rate and a decreased breathing rate go together in this sleep.", "reversed direction or value"]],
  CS(10, 12, 14), "manifestation"),

S(NREM, IO_SWS,
  "During non-rapid eye movement sleep, by about how much do blood pressure, heart rate, breathing rate and metabolic rate fall?",
  [["10 to 30%",
    "Correct. Non-rapid eye movement sleep is associated with decreased peripheral vascular tone and other vegetative bodily functions, with blood pressure, heart rate, breathing rate and metabolic rate falling by 10 to 30%."],
   ["1 to 5%",
    "A fall of 1 to 5% understates the change; the decrease in blood pressure, heart rate, breathing rate and metabolic rate is 10 to 30%. Tell: the fall is tens of percent, not a few.", "reversed direction or value"],
   ["40 to 60%",
    "A fall of 40 to 60% overstates it; the decrease is 10 to 30%. For scale, the rise in brain metabolism during rapid eye movement sleep is up to 20%. Tell: the non-rapid eye movement changes stay within 10 to 30%.", "reversed direction or value"],
   ["70 to 90%",
    "A fall of 70 to 90% is far beyond the 10 to 30% decrease of normal non-rapid eye movement sleep, which is deep and restful rather than a collapse of bodily function. Tell: 10 to 30%.", "reversed direction or value"]],
  CS(6, 10, 12), "manifestation"),

S(NREM, IO_SWS,
  "Which stage is the deepest sleep of the night?",
  [["Stage N3",
    "Correct. Stage N3, also called deep sleep, is restful sleep and the deepest non-rapid eye movement stage, marked by delta waves. Body and tissue growth and repair occur in it, and it decreases with age."],
   ["Stage N1",
    "Stage N1 is the drowsy, somnolent transition from wakefulness, the lightest sleep stage, when the electroencephalogram voltage becomes low. Tell: N1 is light sleep; depth increases through N2 to N3.", "wrong stage or severity"],
   ["Stage N2",
    "Stage N2 is less responsive and deeper than N1, and it is the longest stage by total duration, but it is not the deepest. Tell: deeper is N2, deepest is N3, the delta-wave stage.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep is described as not restful or deep; the brain is very active, with waves like wakefulness. Tell: deep, restful sleep is non-rapid eye movement sleep, deepest in stage N3.", "common lay belief"]],
  CS(6, 9, 28), "manifestation"),

S(NREM, IO_SWS,
  "Which stage is the drowsy transition from wakefulness into light sleep?",
  [["Stage N1",
    "Correct. Stage N1 is the transition from wakefulness: the person is somnolent or drowsy and in light sleep. It is the first, lightest non-rapid eye movement stage, and the electroencephalogram voltage becomes low."],
   ["Stage N2",
    "Stage N2 follows N1 and is less responsive, deeper sleep, with falling heart rate and temperature; it is the longest stage by total duration. Tell: the drowsy transition is N1; deeper and longest is N2.", "wrong stage or severity"],
   ["Stage N3",
    "Stage N3 is the deepest non-rapid eye movement stage, deep restful sleep with delta waves, far from the drowsy edge of wakefulness. Tell: deepest is N3; lightest and transitional is N1.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep is the active dream state with atonia and awake-like brain waves, and in a typical night it follows the non-rapid eye movement stages rather than opening sleep. Tell: the doorway into sleep is N1.", "adjacent fact"]],
  CS(7, 27, 28), "manifestation"),

S(NREM, IO_SWS,
  "Which stage of sleep decreases with age?",
  [["Stage N3",
    "Correct. Stage N3, the deepest, restful non-rapid eye movement stage, marked by delta waves and the time of body and tissue growth and repair, decreases with age. Stage N2 remains the longest stage by total duration, and rapid eye movement sleep is about 25% of a young adult's sleep."],
   ["Stage N1",
    "Stage N1 is the drowsy transition into light sleep. The stage that decreases with age is the deepest one, N3, the delta-wave stage. Tell: think of deep sleep for the age-linked decrease.", "wrong stage or severity"],
   ["Stage N2",
    "Stage N2 is the longest stage by total duration and makes up the majority of the sleep cycle. The decrease with age is noted for N3. Tell: N2 is the bulk of sleep; N3 is the stage that shrinks with age.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep is given as about 25% of a young adult's sleep time; the stage named as decreasing with age is N3. Tell: deep, delta-wave sleep is the stage tied to the decrease with age.", "adjacent fact"]],
  CS(9, 13, 28), "epidemiology"),

S(NREM, IO_SWS,
  "Why are dreams during non-rapid eye movement sleep often not remembered?",
  [["They are not consolidated in memory",
    "Correct. Dreams during non-rapid eye movement sleep are often not remembered because the dreams are not consolidated in memory. Dreams and nightmares do occur in this sleep, which is why calling it the dreamless state is not accurate; they are simply less vivid and usually lost."],
   ["No dreams occur in this sleep",
    "Non-rapid eye movement sleep is often called a dreamless state, but that is not accurate: dreams and nightmares do occur during it. Tell: the issue is recall, not an absence of dreams.", "common lay belief"],
   ["They are too vivid to store",
    "Non-rapid eye movement dreams are less vivid, not more; vivid dreaming belongs to rapid eye movement sleep. Tell: these are dimmer dreams that are not consolidated in memory.", "reversed direction or value"],
   ["The brain is in a coma-like state",
    "Non-rapid eye movement sleep is sleep, unconsciousness from which a person can be aroused by stimuli; coma is the state without arousal. Tell: forgetting dreams reflects missing consolidation in memory, not coma.", "competing diagnosis"]],
  CS(5, 9, 13, 14), "education"),

S(NREM, IO_SWS,
  "Which stage shows a falling heart rate and temperature and is the longest stage by total duration?",
  [["Stage N2",
    "Correct. Stage N2 is less responsive, deeper sleep in which heart rate and temperature decrease, and it is the longest stage by total duration, making up the majority of the sleep cycle. Its electroencephalogram shows theta waves."],
   ["Stage N1",
    "Stage N1 is the drowsy, somnolent transition from wakefulness into light sleep, not the stage that fills most of the night; the falling heart rate and temperature belong to N2. Tell: the longest stage by total duration is N2.", "wrong stage or severity"],
   ["Stage N3",
    "Stage N3 is the deepest, restful stage with delta waves and tissue repair, concentrated early in the night and decreasing with age; it is not the longest stage. Tell: deepest is N3, longest is N2.", "adjacent fact"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep has irregular, rather than falling, heart and breathing rates, and it fills about 25% of a young adult's sleep. Tell: irregular vital signs and a quarter of the night point away from it.", "ruled out by a stated finding"]],
  CS(7, 9, 10, 13, 28), "differential"),

S(NREM, IO_SWS,
  "Which combination fits non-rapid eye movement sleep rather than rapid eye movement sleep?",
  [["Low blood pressure, slow heart rate",
    "Correct. Non-rapid eye movement sleep brings increased parasympathetic tone with low blood pressure, a slow heart rate and a decreased breathing rate, part of a 10 to 30% fall in vegetative functions. In rapid eye movement sleep, heart and breathing rates become irregular instead."],
   ["Irregular heart and breathing rates",
    "Irregular heart and breathing rates are characteristic of the dream state of rapid eye movement sleep. Tell: irregular vital signs point to rapid eye movement sleep; steady slowing points to non-rapid eye movement sleep.", "competing diagnosis"],
   ["Brain metabolism up to 20% higher",
    "Overall brain metabolism rises by up to 20% in rapid eye movement sleep because the brain is very active, whereas metabolic rate falls in non-rapid eye movement sleep. Tell: rising metabolism means rapid eye movement sleep.", "reversed direction or value"],
   ["Waves that resemble wakefulness",
    "Brain waves resembling wakefulness are the reason rapid eye movement sleep is called paradoxical sleep. Non-rapid eye movement sleep slows toward theta and delta waves. Tell: awake-like waves during sleep mean rapid eye movement sleep.", "competing diagnosis"]],
  CS(10, 12, 14, 28), "differential"),

S(NREM, IO_FUNC,
  "After someone stays awake for more than 24 hours, what is sleep like in the first hour after falling asleep?",
  [["Deep and extremely restful",
    "Correct. After more than 24 hours awake, the sleep in the first hour after going to sleep is deep, extremely restful non-rapid eye movement sleep, with blood pressure, heart rate, breathing rate and metabolic rate falling by 10 to 30%."],
   ["Rapid eye movement with vivid dreams",
    "When a person is extremely sleepy, rapid eye movement episodes are short or even absent, so vivid-dream sleep does not fill that first hour. Tell: sleepiness shortens rapid eye movement sleep, and early sleep after a long time awake is deep.", "reversed direction or value"],
   ["Light and drowsy throughout",
    "Light, drowsy sleep describes stage N1, the transition from wakefulness. After a long period awake, the first hour is described as deep sleep, not light. Tell: a long time awake brings deep sleep early.", "wrong stage or severity"],
   ["Restless, with irregular breathing",
    "Irregular heart and breathing rates mark rapid eye movement sleep, the dream state, which is not restful. The deep sleep after long wakefulness is extremely restful, with a decreased breathing rate. Tell: restful and steadily slowed is non-rapid eye movement sleep.", "competing diagnosis"]],
  CS(9, 10, 12, 28), "complication"),

]
