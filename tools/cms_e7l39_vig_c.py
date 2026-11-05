# -*- coding: utf-8 -*-
"""Lecture 39 vignette pool C -- Phases of Sleep: the four waveforms of a normal electroencephalogram (alpha,
beta, theta, delta: frequency, region, voltage, the people and states they occur in) and the tracing across
the stages of wakefulness and sleep (eyes open and closed, stages N1-N3, rapid eye movement sleep).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md (2026-10-29): the key names the stem's decisive
clue and the slide fact; each wrong choice says why it fails for THIS patient, the replacing fact, and a "Tell:".

Frequencies follow the waveform slides: alpha 8 to 13, beta more than 14, theta 4 to 7, delta less than 3.5
cycles per second (the "1 to 3 per second" figure is never used). Stage-to-wave follows the stage table:
eyes open beta, eyes closed alpha, N1 and N2 theta, N3 delta, rapid eye movement sleep beta-like. Theta is never
tied to stage N3, and sleep spindles and K complexes are never used (slide conflicts in the scope module).
Numeric frequency options are ascending (the partition sorts them).
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cmse3_q import Q
from cms_e7l39_scope import *


def S(topic, io, q, opts, cite, slot):
    d = Q(topic, io, q, opts, cite); d["slot"] = slot; return d


def V(topic, io, q, opts, cite, slot, lead):
    d = S(topic, io, q, opts, cite, slot); d["lead"] = lead; return d


def ORD(d, asc):
    d["ordered"] = True; d["asc"] = asc; return d


SVC = "Sleep versus coma"
CYC = "Sleep cycles"
REM = "Rapid eye movement sleep"
NRM = "Non-rapid eye movement sleep"
FUN = "Functions of sleep"
SWC = "The sleep-wake cycle"
BW = "Brain waves"
EAS = "Electroencephalogram across the stages"

QUESTIONS = [

# ---------------------------------------------------------------- brain waves
V(BW, IO_WAVES,
  "A 30-year-old woman sits quietly with her eyes closed, relaxed but awake, during an electroencephalogram. The tracing shows rhythmical waves at 10 cycles per second, strongest over the occipital region. Which waveform is this?",
  [["Alpha waves",
    "Correct. Rhythmical waves at 8 to 13 cycles per second, most intense over the occipital region, are alpha waves. They are found in almost all healthy adults who are awake in a quiet, resting state, such as sitting relaxed with the eyes closed, and they disappear during deep sleep."],
   ["Beta waves",
    "Beta waves run faster than 14 cycles per second, are asynchronous and low voltage, and come mainly from the parietal and frontal regions during alert, active thinking. Tell: a rhythmical 10 per second at quiet rest with the eyes closed is alpha.", "adjacent fact"],
   ["Theta waves",
    "Theta waves run at 4 to 7 cycles per second and appear in children's parietal and temporal regions, during emotional stress in some adults, and in brain disorders. Tell: 10 per second over the occipital region of a relaxed adult is alpha.", "adjacent fact"],
   ["Delta waves",
    "Delta waves run slower than 3.5 cycles per second with high voltage, in very deep sleep, infancy and serious organic brain disease. Tell: she is awake and her rhythm is 10 per second, far faster than delta and inside the alpha range.", "adjacent fact"]],
  CS(22, 23, 25, 26, 28), "test finding", "classify"),

V(BW, IO_WAVES,
  "A 25-year-old man is awake and alert, working through mental arithmetic during an electroencephalogram. Over his frontal and parietal regions the tracing shows asynchronous, low-voltage waves at 25 cycles per second. Which waveform is this?",
  [["Beta waves",
    "Correct. Beta waves occur at frequencies greater than 14 cycles per second (as high as 80), are asynchronous and low voltage, and are recorded mainly from the parietal and frontal regions while a person is awake, alert and actively processing information, as he is during mental arithmetic."],
   ["Alpha waves",
    "Alpha waves are rhythmical, 8 to 13 cycles per second, strongest over the occipital region in a quiet, resting state, and they stop when attention turns to a specific mental activity. Tell: 25 per second during arithmetic is beta.", "adjacent fact"],
   ["Theta waves",
    "Theta waves run at 4 to 7 cycles per second and appear in children, during emotional stress in some adults, and in brain disorders. Tell: 25 per second from the frontal and parietal regions of an alert adult is far above the theta range.", "adjacent fact"],
   ["Delta waves",
    "Delta waves are slower than 3.5 cycles per second and high voltage, seen in very deep sleep, infancy and serious organic brain disease. Tell: his waves are fast and low voltage while he is awake and thinking, the opposite of delta.", "reversed direction or value"]],
  CS(23, 24, 22, 25, 26), "test finding", "classify"),

V(BW, IO_WAVES,
  "A healthy 8-year-old boy has an electroencephalogram while awake. Waves at 5 cycles per second appear over his parietal and temporal regions. Which waveform is this?",
  [["Theta waves",
    "Correct. Theta waves have frequencies between 4 and 7 cycles per second and occur in the parietal and temporal regions in children. A 5-per-second rhythm over those regions in a healthy 8-year-old is theta, an expected finding at his age rather than a sign of disease."],
   ["Alpha waves",
    "Alpha waves run at 8 to 13 cycles per second and are most intense over the occipital region of an adult at quiet rest. Tell: 5 per second over the parietal and temporal regions of a child is theta, below the alpha range.", "adjacent fact"],
   ["Beta waves",
    "Beta waves run faster than 14 cycles per second, are asynchronous and low voltage, and come from the frontal and parietal regions during active thinking. Tell: 5 per second is far slower than beta and falls inside the theta range of 4 to 7.", "adjacent fact"],
   ["Delta waves",
    "Delta waves run below 3.5 cycles per second and are typical of infancy and very deep sleep. Tell: he is an awake 8-year-old with a 5-per-second rhythm, inside the theta range of 4 to 7 per second, not the slower delta range.", "wrong stage or severity"]],
  CS(25, 22, 23, 26), "epidemiology", "classify"),

ORD(V(BW, IO_WAVES,
  "A 2-month-old boy's electroencephalogram shows slow waves below 3.5 cycles per second. Compared with most other types of brain waves, how large is their voltage expected to be?",
  [["2 to 4 times greater",
    "Correct. Delta waves, which include all waves below 3.5 cycles per second and occur in infancy, often have voltages 2 to 4 times greater than most other types of brain waves. On a tracing they stand out as tall, slow waves, in contrast to the low-voltage beta waves of an alert adult."],
   ["Much smaller",
    "Low voltage describes beta waves, the asynchronous, fast waves of an alert, actively thinking person, not delta waves. Tell: slow delta waves are the tall ones, often 2 to 4 times the voltage of most other brain waves.", "reversed direction or value"],
   ["About the same",
    "Delta waves stand out by their size: their voltage is often 2 to 4 times greater than that of most other brain waves. Tell: on traces drawn to one voltage scale, the delta trace rises well above the alpha, beta and theta traces.", "common lay belief"],
   ["20 to 40 times greater",
    "This overstates the difference tenfold: delta waves are often 2 to 4 times greater in voltage than most other brain waves. Tell: the multiplier to remember is 2 to 4, not tens of times, for these slow waves of infancy and deep sleep.", "reversed direction or value"]],
  CS(26, 21, 23), "test finding", "test"), [1, 2, 0, 3]),

V(BW, IO_WAVES,
  "A 27-year-old woman sits relaxed with her eyes closed while her electroencephalogram shows alpha waves. She is then asked to multiply two numbers in her head. What change is expected on the tracing?",
  [["Alpha gives way to beta waves",
    "Correct. When an awake person's attention is directed to a specific type of mental activity, alpha waves stop and are replaced by beta waves: faster than 14 cycles per second, asynchronous and low voltage, recorded mainly from the frontal and parietal regions during active processing."],
   ["Alpha gives way to delta waves",
    "Delta waves, below 3.5 cycles per second, belong to very deep sleep, infancy and serious organic brain disease. Tell: she is awake and concentrating, which speeds the tracing up into beta rather than slowing it to delta.", "reversed direction or value"],
   ["Alpha waves grow larger",
    "Concentration does not enlarge alpha waves; it stops them, and beta waves take their place. Tell: alpha belongs to quiet rest, so turning attention to a mental task ends the alpha rhythm instead of strengthening it.", "common lay belief"],
   ["Alpha gives way to theta waves",
    "Theta waves, 4 to 7 cycles per second, appear in children, during emotional stress in some adults, and in brain disorders. Tell: a calm adult who turns her attention to arithmetic shows faster beta waves, not slower theta waves.", "adjacent fact"]],
  CS(24, 23, 22, 25, 26), "test finding", "test"),

V(BW, IO_WAVES,
  "A 23-year-old healthy man has a routine electroencephalogram while awake and resting quietly. How common is an alpha rhythm in healthy adults in this state?",
  [["Found in almost all of them",
    "Correct. Alpha waves are found in almost all healthy adults when they are awake and in a quiet, resting state, occurring most intensely over the occipital region and also from the parietal and frontal regions. An alpha rhythm in this healthy, resting 23-year-old is the expected finding."],
   ["Found in about half of them",
    "Alpha waves are not a coin toss in healthy adults; they are found in almost all of them when awake and resting quietly. Tell: alpha is the usual resting rhythm of a healthy adult, so it is expected in him rather than a matter of chance.", "reversed direction or value"],
   ["Found in a small minority",
    "Alpha waves are the usual resting rhythm of healthy adults, found in almost all of them, not in a minority. Tell: a quiet, resting, healthy adult such as this man is exactly the person in whom alpha waves are expected.", "reversed direction or value"],
   ["Found mainly in children",
    "The wave tied to children is theta, at 4 to 7 cycles per second over the parietal and temporal regions. Tell: alpha belongs to healthy adults at quiet rest, almost all of whom show it, so his age fits alpha.", "adjacent fact"]],
  CS(22, 25), "epidemiology", "test"),

V(BW, IO_WAVES,
  "A 45-year-old woman has an electroencephalogram while awake. She tells the technician she has felt deeply disappointed and frustrated since losing her job last week, and evaluation finds no brain disorder. The tracing shows waves at 4 to 7 cycles per second. Which explanation best fits these waves?",
  [["Her emotional stress",
    "Correct. Waves at 4 to 7 cycles per second are theta waves, which occur during emotional stress in some adults, especially during disappointment and frustration. With no brain disorder found and her disappointment and frustration since losing her job, emotional stress best explains them."],
   ["A normal resting adult rhythm",
    "The resting rhythm of a healthy, awake adult is alpha, at 8 to 13 cycles per second. Tell: 4 to 7 per second is theta, which in an adult points to emotional stress or a brain disorder rather than to a normal resting state.", "adjacent fact"],
   ["Very deep sleep",
    "Very deep sleep produces delta waves below 3.5 cycles per second, and she is awake and talking. Tell: her waves are theta, and in an awake adult with no brain disorder, theta follows emotional stress such as disappointment and frustration.", "ruled out by a stated finding"],
   ["Alert mental activity",
    "Directed mental activity brings beta waves, faster than 14 cycles per second, from the frontal and parietal regions. Tell: her waves are much slower, in the theta range, and her disappointment and frustration explain them.", "adjacent fact"]],
  CS(25, 22, 26, 23), "risk factors", "diagnosis"),

V(BW, IO_WAVES,
  "A 4-month-old boy who is feeding well and developing normally has an electroencephalogram showing high-voltage waves below 3.5 cycles per second. Which explanation best fits this finding?",
  [["A normal finding in infancy",
    "Correct. High-voltage waves below 3.5 cycles per second are delta waves, and infancy is one of the settings where delta waves occur, along with very deep sleep and serious organic brain disease. In a healthy infant who is feeding well and developing normally, infancy itself explains them."],
   ["Serious organic brain disease",
    "Delta waves do occur in persons with serious organic brain disease, but this infant is feeding well and developing normally. Tell: infancy is itself a setting for delta waves, so a healthy baby needs no disease to explain them.", "ruled out by a stated finding"],
   ["A comatose state",
    "Coma is unconsciousness from which a person cannot be aroused by stimuli, and an infant who is feeding well is plainly arousable. Tell: delta waves in a healthy, feeding infant reflect infancy, not coma.", "ruled out by a stated finding"],
   ["Emotional stress",
    "Emotional stress produces theta waves, 4 to 7 cycles per second, in some adults, not delta waves in an infant. Tell: waves below 3.5 per second are delta, and in a thriving 4-month-old, infancy explains them.", "adjacent fact"]],
  CS(26, 5, 25), "differential", "diagnosis"),

V(BW, IO_WAVES,
  "A 70-year-old man is awake and answering questions during an electroencephalogram. The tracing shows high-voltage waves below 3.5 cycles per second. Which explanation best fits this finding?",
  [["Serious organic brain disease",
    "Correct. High-voltage waves below 3.5 cycles per second are delta waves, which occur in very deep sleep, in infancy and in persons with serious organic brain disease. He is an awake adult answering questions, which rules out deep sleep and infancy, so serious organic brain disease is the setting that fits."],
   ["Very deep sleep",
    "Delta waves do occur in very deep sleep, but he is awake and answering questions. Tell: in an awake adult, delta waves point to serious organic brain disease rather than to sleep, since neither sleep nor infancy applies.", "ruled out by a stated finding"],
   ["Emotional stress",
    "Emotional stress, especially disappointment and frustration, brings theta waves at 4 to 7 cycles per second in some adults. Tell: his waves are slower than 3.5 per second and high voltage, which is delta, not theta.", "adjacent fact"],
   ["Quiet, relaxed wakefulness",
    "Quiet, relaxed wakefulness shows alpha waves at 8 to 13 cycles per second. Tell: an awake adult with waves below 3.5 per second does not have the normal resting rhythm; delta in this setting means serious organic brain disease.", "competing diagnosis"]],
  CS(26, 25, 22), "etiology", "diagnosis"),

V(BW, IO_WAVES,
  "A 63-year-old woman with a degenerative brain disorder has an electroencephalogram while awake and calm. It shows waves at 4 to 7 cycles per second. Which explanation best fits these waves?",
  [["Her brain disorder",
    "Correct. Waves at 4 to 7 cycles per second are theta waves, which occur in many brain disorders, especially degenerative brain states. In a calm, awake adult with a known degenerative brain disorder, that disorder best explains them."],
   ["Her emotional stress",
    "Theta waves do appear during emotional stress in some adults, especially with disappointment and frustration, but she is calm. Tell: in a calm adult with a degenerative brain disorder, the disorder explains the theta waves.", "ruled out by a stated finding"],
   ["Her calm, relaxed state",
    "A calm, relaxed adult at quiet rest shows alpha waves at 8 to 13 cycles per second, not theta. Tell: 4 to 7 per second is theta, which in an adult signals emotional stress or a brain disorder, not a normal resting rhythm.", "adjacent fact"],
   ["Very deep sleep",
    "Very deep sleep brings delta waves, below 3.5 cycles per second, and she is awake. Tell: her waves are theta, faster than delta, and her degenerative brain disorder is the setting that produces them.", "ruled out by a stated finding"]],
  CS(25, 22, 26), "differential", "diagnosis"),

V(BW, IO_WAVES,
  "A 58-year-old man with serious organic brain disease has delta waves on his electroencephalogram. Where in the brain do delta waves arise?",
  [["In the cortex, independent of lower regions",
    "Correct. Delta waves occur strictly in the cortex, independent of activities in lower regions of the brain. They even appear in the cortex of animals whose cerebral cortex has been separated from the thalamus by subcortical transection, so the cortex produces them without input from below."],
   ["In the thalamus, which drives the cortex",
    "Delta waves persist in the cortex of animals whose cortex has been separated from the thalamus, so the thalamus is not needed for them. Tell: delta waves arise in the cortex itself, independent of lower brain regions.", "reversed direction or value"],
   ["In the occipital region, as alpha does",
    "The occipital region is where alpha waves are most intense; delta waves are placed in the cortex, independent of lower brain regions, not tied to one lobe. Tell: the occipital link belongs to alpha.", "adjacent fact"],
   ["In the reticular activating nuclei",
    "The reticular activating nuclei are the proposed drivers of wakefulness, exciting the cerebral cortex. Tell: delta waves arise in the cortex independent of lower regions of the brain, such as these nuclei.", "adjacent fact"]],
  CS(26, 22, 18), "etiology", "test"),

V(BW, IO_WAVES,
  "A 33-year-old man with epilepsy asks why his electroencephalogram looks different from a healthy person's. What determines the intensity and patterns of the electrical activity it records?",
  [["How excited different brain regions are",
    "Correct. The intensity and patterns of electrical activity on an electroencephalogram are determined by the level of excitation of different parts of the brain, which changes with sleep, wakefulness and brain disorders such as epilepsy or psychosis. His epilepsy alters that excitation, and so his tracing."],
   ["Whether he is asleep or awake alone",
    "Sleep and wakefulness do shape the tracing, but brain disorders such as epilepsy or psychosis do too, through the level of excitation of brain regions. Tell: his disorder is itself one of the things that determines the pattern.", "adjacent fact"],
   ["The activity of his peripheral nerves",
    "The tracing reflects the level of excitation of different parts of the brain, not peripheral nerves; delta waves, for example, arise in the cortex. Tell: an electroencephalogram records the brain's own electrical activity.", "confused mechanism or drug class"],
   ["His heart rate and blood pressure",
    "Heart rate and blood pressure change across sleep, falling in non-rapid eye movement sleep, but they are body changes, not the source of the brain's electrical patterns. Tell: the excitation of brain regions determines the tracing.", "confused mechanism or drug class"]],
  CS(21, 26, 12), "education", "education"),

# ---------------------------------------------------------------- the electroencephalogram across the stages
V(EAS, IO_STAGES,
  "A 40-year-old man rests quietly with his eyes closed during an electroencephalogram. At what frequency should his dominant rhythm run?",
  [["8 to 13 cycles per second",
    "Correct. An awake adult in a quiet, resting state, such as resting with the eyes closed, shows alpha waves: rhythmical waves at 8 to 13 cycles per second, most intense over the occipital region. Alpha waves are found in almost all healthy adults in this state."],
   ["Less than 3.5 cycles per second",
    "This is the delta range, found in very deep sleep, infancy and serious organic brain disease. Tell: he is an awake adult at quiet rest, whose rhythm is alpha at 8 to 13 per second, not the slow waves of deep sleep.", "wrong stage or severity"],
   ["4 to 7 cycles per second",
    "This is the theta range, seen in children's parietal and temporal regions, during emotional stress in some adults, and in brain disorders. Tell: a calm adult resting with his eyes closed shows alpha at 8 to 13 per second.", "adjacent fact"],
   ["More than 14 cycles per second",
    "This is the beta range, which comes with alertness and active processing, as when the eyes are open or attention is focused on a task. Tell: resting with the eyes closed brings alpha at 8 to 13 per second instead.", "wrong stage or severity"]],
  CS(22, 28, 23, 25, 26), "test finding", "test"),

V(EAS, IO_STAGES,
  "A 26-year-old woman reaches stage N3, the deepest non-rapid eye movement stage, about 40 minutes into a sleep study. At what frequency are her dominant waves expected to run?",
  [["Less than 3.5 cycles per second",
    "Correct. Stage N3, the deepest non-rapid eye movement stage, shows delta waves, which include all waves with a frequency less than 3.5 cycles per second, often with voltages 2 to 4 times greater than other brain waves. Very deep sleep is one of the settings where delta waves occur."],
   ["4 to 7 cycles per second",
    "Theta waves at 4 to 7 per second belong to stages N1 and N2, the lighter non-rapid eye movement stages. Tell: the deepest stage, stage N3, slows further to delta waves, below 3.5 per second.", "wrong stage or severity"],
   ["8 to 13 cycles per second",
    "Alpha waves at 8 to 13 per second mark quiet wakefulness with the eyes closed, and they disappear during deep sleep. Tell: by stage N3 the tracing has slowed far below the alpha range, to delta.", "wrong stage or severity"],
   ["More than 14 cycles per second",
    "Beta waves above 14 per second mark alert wakefulness and the waking-like tracing of rapid eye movement sleep. Tell: stage N3 carries the slowest tracing of the night, delta, below 3.5 per second.", "wrong stage or severity"]],
  CS(26, 28, 22, 23), "test finding", "test"),

V(EAS, IO_STAGES,
  "A 32-year-old man has rhythmical alpha waves on his electroencephalogram while resting with his eyes closed. When he opens his eyes, the tracing flattens into faster, low-voltage activity. Which waveform has replaced the alpha waves?",
  [["Beta waves",
    "Correct. With the eyes closed and relaxed, an awake adult shows alpha waves; with the eyes open the person is alert and active, which brings beta waves, fast and low voltage. On the tracing, alpha flattens into this faster, low-voltage activity when the eyes open and returns when they close."],
   ["Theta waves",
    "Theta waves run at 4 to 7 cycles per second, slower than alpha, and appear with emotional stress in some adults or in brain disorders. Tell: opening the eyes made his tracing faster, which points to beta, not to a slower wave.", "reversed direction or value"],
   ["Delta waves",
    "Delta waves are slow and high voltage, often 2 to 4 times taller than other brain waves, and belong to very deep sleep, infancy and organic brain disease. Tell: his tracing became faster and lower in voltage, the opposite of delta.", "reversed direction or value"],
   ["Sawtooth waves",
    "Sawtooth waves appear in the mixed, low-voltage tracing of rapid eye movement sleep. Tell: he is awake with his eyes open, and the awake, eyes-open state is marked by beta waves, not by a feature of a sleep stage.", "wrong stage or severity"]],
  CS(24, 28, 23, 25, 26), "test finding", "classify"),

V(EAS, IO_STAGES,
  "A 35-year-old woman is having a routine electroencephalogram. She is alert, chatting with the technician and looking around the room, and the tracing shows fast, low-voltage waves. The technician wants to record her alpha rhythm. What should she be asked to do?",
  [["Close her eyes and rest quietly",
    "Correct. Alpha waves appear when an adult is awake in a quiet, resting state, and closing the eyes in relaxation brings them out, most intensely over the occipital region. Her fast, low-voltage waves are beta waves from alert activity, which give way to alpha once she rests quietly with her eyes closed."],
   ["Solve sums in her head",
    "Directing attention to a specific mental activity stops alpha waves and replaces them with beta waves, the opposite of what the technician wants. Tell: alpha needs quiet rest, while focused thinking keeps her in beta.", "reversed direction or value"],
   ["Fall into deep sleep",
    "Alpha waves disappear during deep sleep, where slow delta waves take over. Tell: the alpha rhythm belongs to quiet wakefulness, the relaxed state between alert activity and sleep, so she must stay awake.", "wrong stage or severity"],
   ["Recall a frustrating event",
    "Emotional stress, especially disappointment and frustration, brings theta waves (4 to 7 per second) in some adults, not alpha. Tell: relaxation, not upset, brings out the alpha rhythm of quiet wakefulness.", "adjacent fact"]],
  CS(22, 24, 28, 23, 25, 26), "initial test", "next step"),

V(EAS, IO_STAGES,
  "A 29-year-old man lies relaxed with his eyes closed while his electroencephalogram shows a steady alpha rhythm. The study next calls for a recording of his beta waves. What should he be asked to do?",
  [["Focus on a specific mental task",
    "Correct. When an awake person's attention is directed to a specific type of mental activity, alpha waves stop and are replaced by beta waves, faster than 14 cycles per second, asynchronous and low voltage, recorded mainly from the frontal and parietal regions."],
   ["Keep resting with his eyes closed",
    "Quiet rest with the eyes closed is what produces his alpha rhythm, so continuing it keeps alpha on the tracing. Tell: beta waves need alertness and active processing of information, not continued rest.", "wrong stage or severity"],
   ["Drift off into light sleep",
    "Drifting into sleep slows the tracing: the frequency becomes progressively slower as sleep deepens. Tell: beta waves come with alert, active processing, so he must be engaged with a task rather than drowsy.", "reversed direction or value"],
   ["Think about a past disappointment",
    "Emotional stress, especially disappointment and frustration, brings theta waves at 4 to 7 per second in some adults. Tell: beta comes from directed mental activity, not from upset, which would slow the tracing instead.", "adjacent fact"]],
  CS(24, 23, 22, 25, 27), "initial test", "next step"),

V(EAS, IO_STAGES,
  "A 25-year-old man in a sleep laboratory, about 90 minutes after falling asleep and still asleep, shows irregular, high-frequency, low-voltage waves resembling those of an awake person, with bursts of rapid eye movements. Which stage is he in?",
  [["Rapid eye movement sleep",
    "Correct. Rapid eye movement episodes recur about every 90 minutes, and their electroencephalogram is irregular, high frequency and low voltage, similar to wakefulness, with rapid eye movements. A man still asleep 90 minutes into the night with that tracing is in rapid eye movement sleep."],
   ["Non-rapid eye movement stage N3",
    "Stage N3 is the deepest non-rapid eye movement stage, with large, slow delta waves below 3.5 cycles per second. Tell: his tracing is fast and low voltage, resembling wakefulness, which is the opposite of delta sleep.", "wrong stage or severity"],
   ["Non-rapid eye movement stage N1",
    "Stage N1 is the drowsy transition from wakefulness into light sleep at the start of the night, with theta waves. Tell: 90 minutes in, a waking-like tracing with rapid eye movements marks rapid eye movement sleep instead.", "wrong stage or severity"],
   ["Alert, active wakefulness",
    "Alert wakefulness shares the fast, irregular tracing, and the two can be hard to tell apart on the electroencephalogram. Tell: he is still asleep, and a waking-like tracing in a sleeper, with rapid eye movements, is rapid eye movement sleep.", "ruled out by a stated finding"]],
  CS(9, 10, 29, 28), "test finding", "classify"),

V(EAS, IO_STAGES,
  "A 31-year-old woman in a sleep study has entered stage N2, the longest stage by total duration. Which waveform is her electroencephalogram expected to show?",
  [["Theta waves",
    "Correct. Stage N2, the less responsive, deeper sleep with falling heart rate and temperature and the longest stage by total duration, shows theta waves, 4 to 7 cycles per second. The faster alpha waves of quiet wakefulness are gone, and the slower delta waves belong to stage N3."],
   ["Alpha waves",
    "Alpha waves, 8 to 13 cycles per second, mark quiet wakefulness with the eyes closed, before sleep begins. Tell: once she is in stage N2, the tracing has slowed below the alpha range to theta waves.", "wrong stage or severity"],
   ["Beta waves",
    "Beta waves mark alert wakefulness and the waking-like tracing of rapid eye movement sleep. Tell: stage N2 is non-rapid eye movement sleep, whose tracing has slowed to theta waves rather than speeding up to beta.", "wrong stage or severity"],
   ["Delta waves",
    "Delta waves, below 3.5 cycles per second, mark stage N3, the deepest non-rapid eye movement stage. Tell: stage N2 is deeper than stage N1 but not the deepest, and its wave is theta, not delta.", "wrong stage or severity"]],
  CS(28, 25, 22, 26), "test finding", "test"),

V(EAS, IO_STAGES,
  "A 26-year-old man's sleep recording shows a period of rapid eye movements with atonia of his limb muscles. Which waveform is his electroencephalogram expected to show?",
  [["Beta waves",
    "Correct. Rapid eye movement sleep shows beta waves: a mixed, low-voltage, irregular, high-frequency pattern similar to the awake state, but with atonia of the voluntary muscles. His rapid eye movements and limb atonia place him in this stage, also called desynchronized sleep."],
   ["Alpha waves",
    "Alpha waves mark quiet wakefulness with the eyes closed. Tell: he is asleep with rapid eye movements and limb atonia, a stage whose tracing resembles alert wakefulness, with beta waves rather than the resting alpha rhythm.", "wrong stage or severity"],
   ["Theta waves",
    "Theta waves mark stages N1 and N2 of non-rapid eye movement sleep. Tell: rapid eye movements with limb atonia mean rapid eye movement sleep, whose tracing is beta-like and similar to the awake state.", "wrong stage or severity"],
   ["Delta waves",
    "Delta waves, slow and high voltage, mark stage N3, the deepest non-rapid eye movement stage. Tell: rapid eye movement sleep has the opposite tracing, fast, irregular and low voltage, with beta waves.", "wrong stage or severity"]],
  CS(28, 29, 10), "test finding", "test"),

V(EAS, IO_STAGES,
  "A 28-year-old woman lies relaxed with her eyes closed at lights-out and then sleeps on into her deepest non-rapid eye movement stage. Which sequence of dominant waves is her electroencephalogram expected to show?",
  [["Alpha, then theta, then delta",
    "Correct. Relaxed wakefulness with the eyes closed shows alpha waves; stages N1 and N2 show theta waves; and stage N3, the deepest non-rapid eye movement stage, shows delta waves. The frequency of the tracing becomes progressively slower as she passes from rest into deep sleep."],
   ["Beta, then alpha, then theta",
    "Beta belongs to alert wakefulness with the eyes open, yet she starts relaxed with her eyes closed, and this sequence stops before the deepest stage. Tell: the deepest non-rapid eye movement stage ends in delta waves.", "wrong stage or severity"],
   ["Delta, then theta, then alpha",
    "This runs the night backward: delta waves mark the deepest stage, which she reaches last, and alpha marks the relaxed wakefulness she starts in. Tell: the tracing slows progressively into sleep, from alpha to delta.", "reversed direction or value"],
   ["Alpha, then beta, then delta",
    "Beta waves come with alert, active processing and with rapid eye movement sleep, not on the way down from relaxation into deep sleep. Tell: frequency slows progressively into non-rapid eye movement sleep, so the middle step is theta.", "adjacent fact"]],
  CS(28, 27, 29), "test finding", "test"),

V(EAS, IO_STAGES,
  "A 30-year-old man's overnight recording shows a stretch of irregular, high-frequency, low-voltage waves, and the reviewer cannot tell from the electroencephalogram alone whether he is awake and active or in rapid eye movement sleep. Which additional finding best settles the question?",
  [["Muscle leads showing atonia",
    "Correct. Rapid eye movement sleep is often difficult to tell apart from being awake and active on the electroencephalogram, because both show irregular, high-frequency waves. The difference is in the muscles: rapid eye movement sleep pairs the waking-like tracing with atonia of the voluntary muscles, sparing the eyes and diaphragm."],
   ["Heart rate showing slowing",
    "A steady fall in heart rate marks non-rapid eye movement sleep, while in rapid eye movement sleep the heart rate becomes irregular. Tell: the question is awake versus rapid eye movement sleep, and the feature that separates them is atonia of the voluntary muscles.", "adjacent fact"],
   ["A search for delta waves",
    "Delta waves mark stage N3, the deepest non-rapid eye movement stage, and belong to neither of the two states in question. Tell: both candidates have fast tracings, so looking for slow waves cannot separate them, while muscle atonia can.", "adjacent fact"],
   ["Counting waves per second",
    "Alert wakefulness and rapid eye movement sleep both show fast, irregular, beta-like waves, so the frequency cannot separate them, as the reviewer has already found. Tell: the waves look alike; atonia on the muscle leads marks rapid eye movement sleep.", "ruled out by a stated finding"]],
  CS(29, 28, 10, 14), "differential", "next step"),

V(EAS, IO_STAGES,
  "A 34-year-old woman lies in bed at lights-out with her eyes closed. Her electroencephalogram shows rhythmical waves at 8 to 13 cycles per second, strongest over the occipital region. Which state does this tracing represent?",
  [["Quiet wakefulness",
    "Correct. Rhythmical waves at 8 to 13 cycles per second, strongest over the occipital region, are alpha waves, the mark of quiet wakefulness: an awake person with the eyes closed, relaxed, with a decreased level of alertness. She has not yet fallen asleep."],
   ["Alert wakefulness",
    "Alert wakefulness, with the eyes open and the person alert and active, shows beta waves faster than 14 cycles per second. Tell: a rhythmical 8 to 13 per second with the eyes closed is alpha, the relaxed waking state.", "adjacent fact"],
   ["Stage N1 sleep",
    "Stage N1 is the drowsy transition into light sleep, and its tracing has slowed to theta waves. Tell: a steady, rhythmical 8 to 13 per second over the occipital region is alpha, so she is still awake and resting.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep shows an irregular, mixed, low-voltage, beta-like tracing with sawtooth waves. Tell: rhythmical alpha at lights-out with closed eyes is quiet wakefulness, well before the first rapid eye movement period about 90 minutes in.", "wrong stage or severity"]],
  CS(22, 27, 28, 29, 9), "differential", "classify"),

V(EAS, IO_STAGES,
  "A 27-year-old man's electroencephalogram is compared between alert wakefulness in the evening and stage N3 later that night. Compared with his alert tracing, how does his stage N3 tracing differ?",
  [["Slower and higher in voltage",
    "Correct. Alert wakefulness shows beta waves: faster than 14 cycles per second, asynchronous and low voltage. Stage N3 shows delta waves: below 3.5 cycles per second, often with voltages 2 to 4 times greater than most other brain waves. The deep-sleep tracing is therefore slower and higher in voltage."],
   ["Faster and lower in voltage",
    "This reverses both features: faster and lower in voltage describes the beta waves of his alert evening tracing. Tell: stage N3 delta waves are slow, below 3.5 per second, and tall, often 2 to 4 times the voltage of other waves.", "reversed direction or value"],
   ["Slower and lower in voltage",
    "The slowing is right, but delta waves are not lower in voltage; they are often 2 to 4 times greater than most other brain waves. Tell: low voltage belongs to beta, the alert tracing, not to the deep-sleep tracing.", "reversed direction or value"],
   ["Faster and higher in voltage",
    "Delta waves are taller, but they are slower, not faster: below 3.5 cycles per second against beta's more than 14. Tell: deep sleep slows the tracing; the frequency becomes progressively slower as sleep deepens.", "reversed direction or value"]],
  CS(23, 26, 28, 27), "test finding", "test"),

V(EAS, IO_STAGES,
  "A 35-year-old woman lies relaxed with her eyes closed at the start of a sleep study, and her electroencephalogram shows alpha waves. What happens to these alpha waves once she reaches deep sleep?",
  [["They disappear",
    "Correct. Alpha waves belong to quiet, relaxed wakefulness, such as resting with the eyes closed, and they disappear during deep sleep. As she sinks into deep non-rapid eye movement sleep the tracing slows progressively, until delta waves below 3.5 cycles per second take over in stage N3."],
   ["They grow larger",
    "Tall, high-voltage waves in deep sleep are delta waves, often 2 to 4 times the voltage of other waves; the alpha waves themselves disappear. Tell: the big waves of deep sleep are a different, slower wave, not enlarged alpha.", "confused mechanism or drug class"],
   ["They speed up into beta",
    "Beta waves replace alpha when an awake person's attention turns to a specific mental activity. Tell: falling into deep sleep slows the tracing progressively; it does not speed it up into the beta range.", "reversed direction or value"],
   ["They persist unchanged",
    "Alpha waves mark quiet wakefulness and disappear during deep sleep. Tell: a persisting alpha rhythm would mean she is still awake and resting quietly, not deeply asleep, since the tracing slows as sleep deepens.", "common lay belief"]],
  CS(22, 26, 27, 24, 28), "test finding", "test"),

V(REM, IO_SWS,
  "A 22-year-old woman in a sleep study is in rapid eye movement sleep, with atonia of her voluntary muscles. Which muscles keep working during this atonia?",
  [["Eye muscles and diaphragm",
    "Correct. In rapid eye movement sleep the voluntary muscles are atonic, except the eye muscles and the diaphragm, because alpha motor neurons are inhibited. The spared eye muscles produce the irregular, sharply peaked rapid eye movements, and the spared diaphragm keeps her breathing going, though irregularly."],
   ["Arm and leg muscles",
    "The limbs are where the atonia shows: voluntary muscle tone is very depressed in rapid eye movement sleep from inhibition of spinal muscle control areas. Tell: the muscles spared from the atonia are the eye muscles and the diaphragm.", "reversed direction or value"],
   ["Diaphragm but not eye muscles",
    "The diaphragm is spared, but so are the eye muscles, which is why rapid eye movements can be recorded in this stage at all. Tell: the stage is named for movements of the spared eye muscles, so they cannot be atonic.", "adjacent fact"],
   ["Eye muscles but not diaphragm",
    "The eye muscles are spared, and so is the diaphragm, so breathing continues through rapid eye movement sleep, irregular rather than stopped. Tell: the two exceptions to the atonia are the eye muscles and the diaphragm together.", "adjacent fact"]],
  CS(28, 10), "manifestation", "physiology"),

]
