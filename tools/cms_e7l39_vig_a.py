# -*- coding: utf-8 -*-
"""Lecture 39 vignette pool A -- Phases of Sleep: sleep versus coma (arousability decides), the night's sleep
cycles (count, length, rapid eye movement share and timing, what extreme sleepiness does), and rapid eye
movement sleep (body changes, recording signature, names, dreaming).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md (2026-10-29): the key names the stem's decisive
clue and the slide fact; each wrong choice says why it fails for THIS patient, the replacing fact, and a "Tell:".

Slide conflicts (scope module) are never keyed: stages are named N1-N3 only, sleep spindles and K complexes are
never used, "slow-wave sleep" appears only where both readings give the same answer, delta is "less than 3.5
cycles per second", theta is never tied to stage N3, and no item compares how hard rapid eye movement sleep and
stage N3 are to wake from. Speaker notes are never used.
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

# ---------------------------------------------------------------- sleep versus coma
V(SVC, IO_COMA,
  "A 68-year-old man on a medical ward is found late at night lying still with his eyes closed, not answering when the nurse enters the room. When she calls his name loudly and squeezes his shoulder, he opens his eyes and answers her questions. Which state best explains his earlier unresponsiveness?",
  [["Sleep",
    "Correct. He was unconscious, yet a loud voice and a squeeze of the shoulder roused him and he answered questions. Sleep is unconsciousness from which a person can be aroused by sensory or other stimuli, which is exactly what happened at his bedside."],
   ["Coma",
    "Coma is unconsciousness from which a person cannot be aroused by stimuli. Tell: he opened his eyes and answered once he heard his name and felt the squeeze, so he was arousable, and arousable unconsciousness is sleep, not coma.", "competing diagnosis"],
   ["Quiet wakefulness",
    "Quiet wakefulness is a relaxed, awake state with a decreased level of alertness and alpha waves on the electroencephalogram, not unconsciousness. Tell: he did not answer until he was stimulated, so he was unconscious first, then roused, which is sleep.", "ruled out by a stated finding"],
   ["Alert wakefulness",
    "Alert wakefulness describes a person who is alert, active and processing information, with fast beta waves on the electroencephalogram. Tell: a man lying still who ignores the nurse until he is called loudly and touched is not alert; he was asleep.", "ruled out by a stated finding"]],
  CS(5, 27, 28), "differential", "diagnosis"),

V(SVC, IO_COMA,
  "A 59-year-old woman is brought to the emergency department unresponsive. She does not open her eyes or move when her name is shouted, when she is shaken, or when firm pressure is applied to her nail bed. Which state best describes her?",
  [["Coma",
    "Correct. She is unconscious and cannot be aroused by any of the stimuli tried: a shouted name, shaking and painful pressure. Coma is unconsciousness from which a person cannot be aroused by stimuli, whereas sleep, however deep, is unconsciousness from which a person can be aroused."],
   ["Stage N3 sleep",
    "Stage N3 is the deepest non-rapid eye movement stage and is more difficult to arouse from, but it is still sleep, from which stimuli can arouse a person. Tell: nothing roused her at all, and failure to arouse defines coma rather than any depth of sleep.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep is a stage of sleep, and people even awaken from it spontaneously in the morning. Tell: she could not be roused by shouting, shaking or pain, so she is not in any stage of sleep; unarousable unconsciousness is coma.", "competing diagnosis"],
   ["Quiet wakefulness",
    "Quiet wakefulness is an awake, relaxed state with alpha waves, the state of someone resting with the eyes closed. Tell: she is unconscious and unresponsive to every stimulus, which rules out any form of wakefulness and fits coma.", "ruled out by a stated finding"]],
  CS(5, 10, 28), "differential", "diagnosis"),

V(SVC, IO_COMA,
  "A 20-year-old college student is slumped over a library desk with his eyes closed. A friend says his name quietly and he does not respond, but when the friend shakes his arm he wakes and starts talking. Which finding shows he was asleep rather than in a coma?",
  [["He woke when his arm was shaken",
    "Correct. Sleep is unconsciousness from which a person can be aroused by sensory or other stimuli; coma is unconsciousness from which a person cannot be aroused. Waking when his arm was shaken shows he was arousable, so he was asleep, even though a quieter stimulus had failed first."],
   ["He ignored a quiet voice",
    "Not answering a quiet voice shows that he was unconscious, which is true of sleep and coma alike, so it cannot separate them. Tell: the deciding finding is that a stronger stimulus, the shake, did rouse him, which is what makes it sleep.", "common lay belief"],
   ["His eyes were closed",
    "Closed eyes say nothing about arousability, and arousability is the feature the definitions of sleep and coma turn on. Tell: both states are unconsciousness; what separates them is whether a stimulus can rouse the person, and the shake did.", "adjacent fact"],
   ["He lay slumped and motionless",
    "Lying still describes his unconscious state, not which kind it was, since both sleep and coma are unconsciousness. Tell: his posture cannot decide it; being roused by the shake of his arm places him in sleep rather than coma.", "adjacent fact"]],
  CS(5), "differential", "diagnosis"),

V(SVC, IO_COMA,
  "A 66-year-old man in the intensive care unit has been unresponsive for 2 days. His electroencephalogram shows high-voltage waves slower than 3.5 cycles per second, and he cannot be aroused by voice, touch or painful pressure. Which state best describes him?",
  [["Coma",
    "Correct. The deciding finding is that no stimulus arouses him, which defines coma. His slow, high-voltage delta waves do not decide it on their own, because delta waves occur in very deep sleep as well as in serious organic brain disease; arousability is what separates sleep from coma."],
   ["Very deep sleep",
    "Delta waves do occur in very deep sleep, so his tracing alone could fit it. Tell: a sleeper, however deep, can be aroused by stimuli; he cannot be roused by voice, touch or pain, which makes this coma rather than sleep.", "ruled out by a stated finding"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep has an electroencephalogram resembling wakefulness, with irregular, high-frequency, low-voltage waves, not tall, slow delta waves. Tell: his tracing is slow and high-voltage, and no stimulus rouses him, so neither the waves nor the arousal test fit.", "ruled out by a stated finding"],
   ["Alert wakefulness",
    "Alert wakefulness shows fast, low-voltage beta waves in a person who is awake and actively processing information. Tell: he is unresponsive and his waves are slower than 3.5 per second, the opposite of an alert tracing; unarousable unconsciousness is coma.", "ruled out by a stated finding"]],
  CS(5, 26, 23, 28), "differential", "diagnosis"),

V(SVC, IO_COMA,
  "A 30-year-old woman in a sleep laboratory, about 40 minutes after falling asleep, shows large, slow waves below 3.5 cycles per second on her electroencephalogram. When the technician calls her name loudly, she wakes and answers. Which state was she in before she woke?",
  [["Stage N3 sleep",
    "Correct. Waves below 3.5 cycles per second are delta waves, the wave of stage N3, the deepest non-rapid eye movement stage. That a loud voice woke her confirms sleep rather than coma, because sleep is unconsciousness from which a person can be aroused by stimuli."],
   ["Coma",
    "Delta waves also occur with serious organic brain disease, but coma is unconsciousness from which a person cannot be aroused. Tell: she woke to a loud voice and answered, so her slow waves came from deep sleep, not from coma.", "competing diagnosis"],
   ["Stage N1 sleep",
    "Stage N1 is the drowsy transition from wakefulness into light sleep, with theta waves of 4 to 7 cycles per second. Tell: waves below 3.5 per second are delta waves, which mark the deepest non-rapid eye movement stage, not the lightest one.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep shows a mixed, low-voltage tracing with beta waves, similar to the awake state. Tell: large, slow delta waves are the opposite of the fast, desynchronized tracing of rapid eye movement sleep; they mark stage N3.", "wrong stage or severity"]],
  CS(5, 26, 28, 25), "test finding", "classify"),

V(SVC, IO_COMA,
  "A 78-year-old woman in a nursing home is found in bed with her eyes closed and does not answer when an aide walks into the room. Which step best distinguishes sleep from coma in her?",
  [["Apply a stimulus and watch for arousal",
    "Correct. Sleep and coma are both unconsciousness; what separates them is whether stimuli can arouse the person. Calling her loudly or touching her and watching whether she wakes answers the question directly: arousal means sleep, and no arousal to stimuli means coma."],
   ["Look for delta waves on an electroencephalogram",
    "Delta waves occur in very deep sleep as well as in persons with serious organic brain disease, so finding them would not separate sleep from coma. Tell: the definitions differ by arousability, and a stimulus tests that directly at the bedside.", "adjacent fact"],
   ["Watch her eyes for rapid movements",
    "Rapid eye movements mark rapid eye movement sleep, but a sleeper in non-rapid eye movement sleep does not show them, so their absence would not mean coma. Tell: the test that defines the difference is whether a stimulus wakes her.", "adjacent fact"],
   ["Count her breathing rate",
    "Breathing slows in non-rapid eye movement sleep and turns irregular in rapid eye movement sleep, so a rate describes the stage of sleep rather than separating sleep from coma. Tell: arousal to a stimulus is the deciding test.", "adjacent fact"]],
  CS(5, 10, 14, 26), "initial test", "next step"),

V(SVC, IO_COMA,
  "A 45-year-old man's father has been in a coma for a week. The son asks how coma differs from very deep sleep. Which explanation is accurate?",
  [["A sleeper can be roused; a person in coma cannot",
    "Correct. Both sleep and coma are states of unconsciousness. The difference is arousal: sleep is unconsciousness from which a person can be aroused by sensory or other stimuli, and coma is unconsciousness from which a person cannot be aroused by stimuli, however deep the sleep is."],
   ["Coma is the deepest stage of sleep",
    "The deepest non-rapid eye movement stage, stage N3, is still sleep: more difficult to arouse, yet arousable by stimuli. Tell: coma is not a sleep stage at all; it is defined by the inability to be aroused, whatever the depth.", "common lay belief"],
   ["A sleeper is conscious; a person in coma is not",
    "Sleep is unconsciousness too; a sleeper is not conscious. Tell: both states are unconsciousness, and what separates them is whether stimuli can arouse the person, which is possible in sleep and not in coma.", "common lay belief"],
   ["Coma shows slower brain waves than sleep",
    "Slow, high-voltage delta waves occur in very deep sleep as well as in serious organic brain disease, so slow waves do not mark the boundary between sleep and coma. Tell: the definitions turn on arousal, not on wave speed.", "adjacent fact"]],
  CS(5, 26, 28), "education", "education"),

# ---------------------------------------------------------------- sleep cycles
V(CYC, IO_SWS,
  "A 25-year-old man spends a full 8-hour night in a sleep laboratory. How many separate sleep cycles is his recording expected to show?",
  [["4 to 5 cycles",
    "Correct. An average night is about 8 hours of sleep, and during those 8 hours there are 4 to 5 separate sleep cycles, each lasting 90 to 120 minutes. His full 8-hour recording should show 4 to 5 cycles, each closing with a rapid eye movement period."],
   ["1 to 2 cycles",
    "Each cycle lasts 90 to 120 minutes, so 1 to 2 cycles would cover only about 2 to 4 hours, half of his night or less. Tell: 8 hours divided into 90- to 120-minute cycles gives 4 to 5, not 1 to 2.", "reversed direction or value"],
   ["8 to 10 cycles",
    "Eight to 10 cycles would need cycles of under an hour, but each cycle runs 90 to 120 minutes. Tell: this answer mistakes the 8 hours of an average night for the number of cycles; the count over 8 hours is 4 to 5.", "adjacent fact"],
   ["12 to 15 cycles",
    "This would mean cycles of about half an hour, yet rapid eye movement episodes recur only about every 90 minutes and a cycle lasts 90 to 120 minutes. Tell: one cycle per 90 to 120 minutes over 8 hours gives 4 to 5.", "reversed direction or value"]],
  CS(6, 7, 9), "test finding", "test"),

V(CYC, IO_SWS,
  "A 22-year-old student asks how long one complete sleep cycle lasts. Which answer is accurate?",
  [["90 to 120 minutes",
    "Correct. Each sleep cycle lasts 90 to 120 minutes, and an average 8 hours of sleep holds 4 to 5 of them. Within each cycle non-rapid eye movement sleep is followed by a rapid eye movement episode, and those episodes recur about every 90 minutes."],
   ["20 to 30 minutes",
    "This is closer to the length of a single rapid eye movement episode, which lasts 5 to 30 minutes, than to a whole cycle. Tell: a cycle holds non-rapid eye movement sleep as well as the rapid eye movement episode and runs 90 to 120 minutes.", "adjacent fact"],
   ["45 to 60 minutes",
    "Cycles this short would fit 8 to 10 into an 8-hour night, but an average night holds 4 to 5. Tell: rapid eye movement episodes recur about every 90 minutes, which marks the length of a cycle at 90 to 120 minutes.", "reversed direction or value"],
   ["180 to 240 minutes",
    "At 3 to 4 hours per cycle, an 8-hour night would hold only 2 to 3 cycles rather than 4 to 5. Tell: each cycle runs 90 to 120 minutes, about the interval between one rapid eye movement episode and the next.", "reversed direction or value"]],
  CS(6, 9), "education", "education"),

V(CYC, IO_SWS,
  "A 25-year-old man falls asleep at the start of an overnight sleep study. About how long after he falls asleep is his first rapid eye movement period expected?",
  [["About 90 minutes",
    "Correct. Sleep begins in non-rapid eye movement sleep, and in a typical night the first rapid eye movement period closes the first cycle, between 1 and 2 hours in. Rapid eye movement episodes recur about every 90 minutes, and each cycle lasts 90 to 120 minutes."],
   ["About 10 minutes",
    "Ten minutes in, the sleeper is still descending through the non-rapid eye movement stages; in a typical night the first rapid eye movement period comes at the end of the first cycle. Tell: rapid eye movement sleep closes a 90- to 120-minute cycle; it does not open the night.", "wrong stage or severity"],
   ["About 30 minutes",
    "At about 30 minutes a typical night shows deepening non-rapid eye movement sleep, not rapid eye movement sleep. Tell: 30 minutes is the upper end of one rapid eye movement episode's length (5 to 30 minutes), not the wait before the first one.", "adjacent fact"],
   ["About 240 minutes",
    "Four hours in, a typical night has already held two rapid eye movement periods, so waiting that long would skip the first two cycles. Tell: rapid eye movement episodes recur about every 90 minutes, so the first comes about 90 minutes in.", "reversed direction or value"]],
  CS(6, 7, 9), "test finding", "test"),

V(CYC, IO_SWS,
  "A 24-year-old woman's overnight recording is scored stage by stage. About what share of her total sleep time is rapid eye movement sleep expected to fill?",
  [["About 25%",
    "Correct. Rapid eye movement sleep occurs in episodes and occupies about 25% of a young adult's sleep time, and at 24 she is a young adult. The rest of her night is non-rapid eye movement sleep, of which stage N2 is the largest part."],
   ["About 5%",
    "Far too small: rapid eye movement sleep fills about a quarter of a young adult's sleep, with episodes of 5 to 30 minutes recurring about every 90 minutes. Tell: 5 is the shortest episode length in minutes, not the share of the night.", "adjacent fact"],
   ["About 50%",
    "Half would make rapid eye movement sleep as large as all non-rapid eye movement sleep, yet stage N2 alone is the longest stage by total duration. Tell: rapid eye movement sleep is about one quarter of a young adult's sleep.", "reversed direction or value"],
   ["About 75%",
    "Three quarters reverses the proportions: most of the night is non-rapid eye movement sleep, with stage N2 the longest stage, and rapid eye movement sleep is about one quarter. Tell: the figure for a young adult is 25%, not 75%.", "reversed direction or value"]],
  CS(9, 13, 28), "epidemiology", "test"),

V(CYC, IO_SWS,
  "A 21-year-old student stayed awake for more than 24 hours to study and then falls asleep. Which kind of sleep is expected to fill his first hour of sleep?",
  [["Deep non-rapid eye movement sleep",
    "Correct. After being up for more than 24 hours, the sleep of the first hour is deep and extremely restful, the non-rapid eye movement kind. Extreme sleepiness also makes rapid eye movement episodes short or even absent, so deep non-rapid eye movement sleep fills his first hour."],
   ["Long rapid eye movement episodes",
    "Extreme sleepiness does the opposite: each rapid eye movement episode is short or even absent, and the episodes lengthen only as the person becomes more rested. Tell: after a sleepless night, deep non-rapid eye movement sleep comes first.", "reversed direction or value"],
   ["Light, drowsy stage N1 sleep",
    "Stage N1 is the brief, drowsy transition from wakefulness into light sleep. Tell: the sleep that follows more than 24 hours awake is deep and extremely restful, which is deep non-rapid eye movement sleep, not light sleep.", "wrong stage or severity"],
   ["Quiet wakefulness with alpha waves",
    "Quiet wakefulness is a relaxed, awake state with alpha waves, and alpha waves disappear during deep sleep. Tell: he has fallen asleep, and the first hour after a sleepless night is deep sleep, so the resting awake rhythm is gone.", "ruled out by a stated finding"]],
  CS(12, 9, 22, 28), "manifestation", "classify"),

V(CYC, IO_SWS,
  "A 30-year-old resident falls asleep after a 30-hour shift without any sleep. What is expected of the rapid eye movement episodes on her recording tonight?",
  [["Short or even absent",
    "Correct. When a person is extremely sleepy, each rapid eye movement episode is short or even absent; as the person becomes more rested, the episodes lengthen. After 30 hours awake she is extremely sleepy, so tonight her rapid eye movement episodes should be brief or missing."],
   ["Longer than on rested nights",
    "This reverses the pattern: rapid eye movement episodes lengthen as a person becomes more rested and shorten when the person is extremely sleepy. Tell: sleep debt shortens or removes the episodes, and rest lengthens them.", "reversed direction or value"],
   ["The same as on rested nights",
    "Episode length is not fixed; it depends on how sleepy the person is. Tell: extreme sleepiness makes each rapid eye movement episode short or even absent, so her recording should look different from a rested night's.", "common lay belief"],
   ["More frequent than usual",
    "Rapid eye movement episodes recur about every 90 minutes within 90- to 120-minute cycles, and extreme sleepiness changes their length, making each one short or even absent. Tell: what sleepiness changes is how long each episode lasts.", "confused mechanism or drug class"]],
  CS(9, 6), "risk factors", "complication"),

V(CYC, IO_SWS,
  "A 27-year-old man has had several short nights, and his first recovery night showed short rapid eye movement episodes. He asks what will happen to those episodes as he catches up on sleep. Which answer is accurate?",
  [["They will get longer",
    "Correct. Rapid eye movement episode length follows sleepiness: when a person is extremely sleepy each episode is short or even absent, and as the person becomes more rested (less sleepy), the duration of the episodes increases. Catching up on sleep should lengthen his episodes."],
   ["They will get shorter",
    "Shortening goes with greater sleepiness, not with recovery. Tell: as he becomes less sleepy, the duration of each rapid eye movement episode increases, so recovery moves his episodes in the other direction, toward longer ones.", "reversed direction or value"],
   ["They will stay the same",
    "Episode length is not fixed; it rises as sleepiness falls. Tell: his short episodes reflect how sleepy he still is, and they should lengthen as he becomes more rested over the coming nights.", "common lay belief"],
   ["They will stop occurring",
    "Episodes can be absent when a person is extremely sleepy, which is the state he is leaving behind. Tell: recovery moves him toward longer rapid eye movement episodes, not toward losing them altogether.", "wrong stage or severity"]],
  C(9), "prognosis", "education"),

V(CYC, IO_SWS,
  "A 25-year-old woman has an overnight sleep recording. Compared with her first sleep cycle, what does her last cycle before morning show?",
  [["A longer rapid eye movement period",
    "Correct. Across a typical night, rapid eye movement periods grow longer in the later cycles, while the deepest non-rapid eye movement sleep falls in the first cycles. This fits rapid eye movement episodes lengthening as the sleeper becomes more rested."],
   ["Deeper non-rapid eye movement sleep",
    "A typical night shows the reverse: the deepest non-rapid eye movement sleep comes in the first cycles, and the later cycles stay lighter. Tell: deep sleep is concentrated early in the night, while rapid eye movement periods lengthen toward morning.", "reversed direction or value"],
   ["No rapid eye movement period",
    "Each cycle of a typical night ends in a rapid eye movement period, and the last one leads into waking; people can awaken spontaneously in the morning during rapid eye movement sleep. Tell: late cycles hold longer rapid eye movement periods, not none.", "reversed direction or value"],
   ["A cycle under 30 minutes long",
    "Each cycle lasts 90 to 120 minutes through the night. Tell: 30 minutes is the upper length of one rapid eye movement episode (5 to 30 minutes), not of a whole cycle, and the late cycles are not shortened to that.", "adjacent fact"]],
  CS(7, 9, 10, 6), "prognosis", "test"),

V(CYC, IO_SWS,
  "A 28-year-old woman wakes on her own at the end of a full night's sleep, recalling a vivid dream. From which sleep stage did she probably wake?",
  [["Rapid eye movement sleep",
    "Correct. Rapid eye movement sleep is associated with vivid dreaming, and people can awaken spontaneously in the morning during rapid eye movement sleep; in a typical night the last rapid eye movement period leads into waking. Her spontaneous morning waking and vivid dream both point here."],
   ["Non-rapid eye movement stage N3",
    "Stage N3 is the deepest, most restful non-rapid eye movement stage, and non-rapid eye movement sleep has less vivid dreams that are often not remembered. Tell: a vivid, recalled dream on spontaneous morning waking points to rapid eye movement sleep.", "wrong stage or severity"],
   ["Non-rapid eye movement stage N2",
    "Stage N2 is the longest stage by total duration, but its dreams, like other non-rapid eye movement dreams, are less vivid and often not remembered. Tell: vivid dreaming at a spontaneous morning waking fits rapid eye movement sleep.", "adjacent fact"],
   ["Non-rapid eye movement stage N1",
    "Stage N1 is the drowsy transition from wakefulness into light sleep, the stage at the start of sleep rather than the end of the night. Tell: her vivid, remembered dream on waking points to rapid eye movement sleep, the dream state.", "wrong stage or severity"]],
  CS(9, 10, 13, 14, 7, 28), "manifestation", "classify"),

# ---------------------------------------------------------------- rapid eye movement sleep
V(REM, IO_SWS,
  "A 26-year-old man in a sleep laboratory enters a period with rapid eye movements and an electroencephalogram resembling wakefulness. Which change in his heart rate and breathing is expected during this period?",
  [["They become irregular",
    "Correct. His rapid eye movements and waking-like tracing place him in rapid eye movement sleep, in which heart rate and respiratory rate become irregular, a pattern characteristic of the dream state. Steady slowing belongs to non-rapid eye movement sleep instead."],
   ["They slow steadily",
    "Steady slowing of heart rate and breathing, with low blood pressure from increased parasympathetic tone, describes non-rapid eye movement sleep. Tell: his rapid eye movements and waking-like tracing mark rapid eye movement sleep, where both rates turn irregular.", "wrong stage or severity"],
   ["They rise steadily",
    "Neither sleep type brings a steady climb: non-rapid eye movement sleep lowers heart rate and breathing by 10 to 30%, and rapid eye movement sleep makes them irregular. Tell: the dream state is marked by irregularity, not a steady rise.", "reversed direction or value"],
   ["Breathing stops from atonia",
    "The atonia of rapid eye movement sleep affects the voluntary muscles except the eye muscles and the diaphragm, so breathing goes on. Tell: the diaphragm is spared; what changes in this stage is that breathing becomes irregular.", "confused mechanism or drug class"]],
  CS(10, 12, 14, 28), "manifestation", "physiology"),

V(REM, IO_SWS,
  "A 23-year-old woman in a sleep study has an electroencephalogram resembling wakefulness with irregular, sharply peaked eye movements. What is expected of her limb muscle tone during this period?",
  [["Markedly depressed",
    "Correct. Her waking-like tracing and irregular, sharply peaked eye movements place her in rapid eye movement sleep, in which muscle tone is very depressed: the voluntary muscles show atonia, sparing the eye muscles and diaphragm, from inhibition of spinal muscle control areas and alpha motor neurons."],
   ["Higher than when awake",
    "Muscle tone in rapid eye movement sleep is very depressed, not raised; the voluntary muscles are atonic because spinal muscle control areas are inhibited. Tell: the tracing looks awake, but the limbs are limp, the opposite of increased tone.", "reversed direction or value"],
   ["The same as when awake",
    "The electroencephalogram resembles wakefulness, but muscle tone does not: rapid eye movement sleep pairs a waking-like tracing with atonia of the voluntary muscles. Tell: the brain looks awake while the limbs are atonic.", "common lay belief"],
   ["Kept in limbs, lost in eyes",
    "This reverses the pattern: the eye muscles and diaphragm are the muscles spared from atonia, which is why rapid eye movements can be recorded, while the limb muscles lose their tone. Tell: the eyes move because they are spared.", "reversed direction or value"]],
  CS(10, 28), "manifestation", "physiology"),

V(REM, IO_SWS,
  "A 31-year-old man's sleep study shows a mixed, low-voltage electroencephalogram with sawtooth waves, rapid eye movements and atonia of his limb muscles. What explains the atonia?",
  [["Inhibited spinal motor neurons",
    "Correct. His tracing, rapid eye movements and atonia place him in rapid eye movement sleep. Muscle tone is very depressed because spinal muscle control areas are inhibited; the inactivity is due to inhibited alpha motor neurons, sparing the eye muscles and the diaphragm."],
   ["Increased parasympathetic tone",
    "Increased parasympathetic tone is the autonomic change of non-rapid eye movement sleep, lowering blood pressure, heart rate and breathing. Tell: limb atonia in rapid eye movement sleep comes from inhibited alpha motor neurons, not from autonomic tone.", "confused mechanism or drug class"],
   ["Fatigued activating-system neurons",
    "Fatigue of neurons in the activating system is the proposed reason a person passes from wakefulness into sleep after many hours awake. Tell: it explains falling asleep, whereas atonia within rapid eye movement sleep comes from inhibited spinal motor neurons.", "adjacent fact"],
   ["Exhausted muscle energy stores",
    "The atonia is not a problem in the muscle itself; it reflects inhibition of the spinal muscle control areas and alpha motor neurons that drive the muscles. Tell: the eye muscles and diaphragm keep working, which exhausted muscles would not explain.", "common lay belief"]],
  CS(10, 28, 14, 19), "etiology", "physiology"),

V(REM, IO_SWS,
  "A 29-year-old woman's sleep recording shows rapid eye movements, irregular breathing and an electroencephalogram resembling wakefulness. How is her overall brain metabolism expected to change during this period?",
  [["Rises by up to 20%",
    "Correct. Rapid eye movement sleep is an active form of sleep in which the brain is very active, and overall brain metabolism can increase by as much as 20% because of that increased brain activity. Her rapid eye movements, irregular breathing and waking-like tracing place her in this stage."],
   ["Falls by 10 to 30%",
    "A 10 to 30% fall in metabolic rate, along with blood pressure, heart rate and breathing, belongs to non-rapid eye movement sleep. Tell: her rapid eye movements and waking-like tracing mark rapid eye movement sleep, when brain metabolism rises instead.", "wrong stage or severity"],
   ["Falls along with muscle tone",
    "Muscle tone is very depressed in rapid eye movement sleep, but that comes from inhibited spinal muscle control areas while the brain itself is very active. Tell: limp limbs and a busy brain go together here, with brain metabolism up by as much as 20%.", "confused mechanism or drug class"],
   ["Rises 2 to 4 times over",
    "The rise is up to 20%, not a doubling or more; 2 to 4 times is the figure for delta wave voltage compared with most other brain waves. Tell: brain metabolism in rapid eye movement sleep climbs by as much as one fifth.", "adjacent fact"]],
  CS(10, 12, 26), "manifestation", "physiology"),

V(REM, IO_SWS,
  "A 27-year-old man's recording, about 90 minutes after he falls asleep, shows irregular, high-frequency waves like those of an awake, active person, while he lies asleep with atonic limbs. Which term names this stage?",
  [["Paradoxical sleep",
    "Correct. In rapid eye movement sleep the electroencephalogram shows brain wave patterns similar to those during wakefulness, so this stage is also called paradoxical sleep: he is asleep with atonic limbs while his tracing looks awake. Rapid eye movement episodes recur about every 90 minutes."],
   ["Slow-wave sleep",
    "Slow-wave sleep is the deep, restful non-rapid eye movement sleep, with slow waves rather than the fast, irregular waves of wakefulness. Tell: a sleeper whose tracing looks awake and active is in paradoxical, rapid eye movement sleep.", "competing diagnosis"],
   ["Quiet wakefulness",
    "Quiet wakefulness is an awake, relaxed state marked by rhythmical alpha waves. Tell: he is asleep, and his waves are irregular and high frequency like those of alert wakefulness, not the steady alpha rhythm of a person resting awake.", "ruled out by a stated finding"],
   ["Light stage N1 sleep",
    "Stage N1 is the drowsy transition from wakefulness into light sleep, with theta waves. Tell: irregular, high-frequency waves resembling an awake, active person, together with limb atonia 90 minutes into the night, describe rapid eye movement sleep.", "wrong stage or severity"]],
  CS(10, 9, 29, 28, 6), "test finding", "classify"),

V(REM, IO_SWS,
  "A 32-year-old woman's recording during a period of rapid eye movements shows irregular, high-frequency waves, and the technician labels it desynchronized sleep. What does that label describe?",
  [["Neurons firing without synchrony",
    "Correct. Rapid eye movement sleep is also called desynchronized sleep because there is a lack of synchrony in neuron firing when there is brain activity. The tracing is irregular and high frequency, much like an awake, active person's, which fits her period of rapid eye movements."],
   ["Neurons firing in tight unison",
    "This is the reverse of the label: desynchronized means a lack of synchrony in neuron firing. Tell: her irregular, high-frequency tracing reflects neurons firing out of step with each other, not together.", "reversed direction or value"],
   ["Rhythmic waves of quiet rest",
    "Rhythmical waves at 8 to 13 per second in a relaxed, awake person are alpha waves of quiet wakefulness. Tell: her waves are irregular and high frequency during sleep with rapid eye movements, which is the desynchronized pattern, not a rhythm.", "adjacent fact"],
   ["Fatigue of the activating system",
    "Fatigue of neurons in the activating system is the proposed trigger for falling asleep after many hours awake, not a description of a tracing. Tell: desynchronized describes how neurons fire during rapid eye movement sleep, without synchrony.", "adjacent fact"]],
  CS(29, 22, 19), "test finding", "test"),

V(REM, IO_SWS,
  "A 24-year-old man's overnight recording shows a mixed, low-voltage electroencephalogram with sawtooth waves, irregular and sharply peaked eye movements, and atonia on the limb muscle leads. Which stage is he in?",
  [["Rapid eye movement sleep",
    "Correct. A mixed, low-voltage tracing with sawtooth waves, irregular and sharply peaked eye movements, and atonia of the voluntary muscles (sparing the eye muscles and diaphragm) is the recorded signature of rapid eye movement sleep, the dream state."],
   ["Alert, active wakefulness",
    "Alert wakefulness also shows fast, low-voltage beta waves, and the two can be hard to tell apart on the electroencephalogram alone. Tell: the atonia on his limb leads separates them, since rapid eye movement sleep has the waking-like tracing but with atonia.", "competing diagnosis"],
   ["Non-rapid eye movement stage N3",
    "Stage N3 is the deepest non-rapid eye movement stage, with large, slow delta waves below 3.5 cycles per second. Tell: a low-voltage, mixed tracing with sawtooth waves and rapid eye movements is the opposite of high-voltage delta sleep.", "wrong stage or severity"],
   ["Non-rapid eye movement stage N1",
    "Stage N1 is the drowsy transition from wakefulness into light sleep, with theta waves. Tell: sawtooth waves, sharply peaked rapid eye movements and atonia of the limb muscles mark rapid eye movement sleep, not light sleep.", "wrong stage or severity"]],
  CS(28, 29), "test finding", "classify"),

V(REM, IO_SWS,
  "A 33-year-old woman's partner notices that late in the night her eyes dart rapidly under closed lids, her breathing becomes irregular and her fingers twitch. When woken, she describes a vivid dream. Which stage was she in?",
  [["Rapid eye movement sleep",
    "Correct. Rapid eye movement sleep is the active form of sleep associated with vivid dreaming, rapid eye movements, irregular muscle movements, and irregular heart rate and breathing. Late-night timing fits too, since rapid eye movement periods lengthen in the later cycles."],
   ["Non-rapid eye movement stage N3",
    "Stage N3 is deep, restful non-rapid eye movement sleep, with slow heart rate, decreased breathing and less vivid dreams. Tell: darting eyes, irregular breathing and a vivid dream mark rapid eye movement sleep, not the deepest non-rapid stage.", "wrong stage or severity"],
   ["Non-rapid eye movement stage N2",
    "Stage N2 is deeper non-rapid eye movement sleep with heart rate and temperature falling, and non-rapid eye movement dreams are less vivid and often not remembered. Tell: irregular breathing and darting eyes are rapid eye movement features.", "competing diagnosis"],
   ["Quiet, relaxed wakefulness",
    "Quiet wakefulness is a relaxed, awake state with alpha waves, but she had to be woken and was dreaming. Tell: she was asleep, and a vivid dream with rapid eye movements and irregular breathing is the dream state of rapid eye movement sleep.", "ruled out by a stated finding"]],
  CS(9, 10, 13, 14, 7, 28), "manifestation", "classify"),

V(REM, IO_SWS,
  "A 38-year-old man has read that the dreaming stage is the most restful part of the night. Which statement corrects him?",
  [["Dreaming sleep is not restful or deep",
    "Correct. Rapid eye movement sleep, the stage associated with vivid dreaming, is not the most restful type of sleep: it is not restful or deep, and the brain is very active. The deep, restful sleep is non-rapid eye movement sleep, and stage N3 is its deepest, most restful stage."],
   ["Dreaming sleep is restful but light",
    "Rapid eye movement sleep is neither restful nor deep, so calling it restful repeats his error. Tell: the restful sleep is non-rapid eye movement sleep, deepest and most restful in stage N3.", "wrong stage or severity"],
   ["The brain rests most while dreaming",
    "During rapid eye movement sleep the brain is very active, and overall brain metabolism can rise by as much as 20%. Tell: the dreaming brain is busy, which is part of why rapid eye movement sleep is not the restful kind.", "reversed direction or value"],
   ["Restfulness is equal across stages",
    "The stages differ: non-rapid eye movement sleep is deep and restful, with stage N3 the most restful, while rapid eye movement sleep is not restful or deep. Tell: the two types of sleep are told apart partly by how restful they are.", "common lay belief"]],
  CS(6, 9, 10, 28), "education", "education"),

]
