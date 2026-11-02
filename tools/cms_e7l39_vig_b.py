# -*- coding: utf-8 -*-
"""Lecture 39 vignette pool B -- Phases of Sleep: non-rapid eye movement sleep (body changes, stages N1-N3,
age, tissue repair, dreaming), the functions of sleep and the effects of sleep restriction, and the proposed
sleep-wake cycle (reticular activating nuclei, positive feedback, fatigue of the activating system).

KEYS ARE WRITTEN SHORT ON PURPOSE -- detail lives in the explanation.
EXPLANATIONS follow tools/question_writing/EXPLAIN_DEEP.md (2026-10-29): the key names the stem's decisive
clue and the slide fact; each wrong choice says why it fails for THIS patient, the replacing fact, and a "Tell:".

Slide conflicts (scope module) are never keyed: stages are named N1-N3 only, sleep spindles and K complexes are
never used, theta is tied to stage N2 only where the stem also gives N2's own features, and no item compares how
hard rapid eye movement sleep and stage N3 are to wake from. Speaker notes are never used (the "memory" note on
the rapid eye movement slide included).
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

# ---------------------------------------------------------------- non-rapid eye movement sleep
V(NRM, IO_SWS,
  "A 35-year-old man's 8-hour sleep recording is scored stage by stage. Which stage takes up the largest share of his total sleep time?",
  [["Stage N2",
    "Correct. Stage N2 makes up the majority of the sleep cycle and is the longest stage by total duration. Rapid eye movement sleep fills about 25% of a young adult's sleep, and stage N2 outlasts both the brief drowsy stage N1 and the deep stage N3, so it holds the largest share of his night."],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep occupies about 25% of a young adult's sleep time, roughly a quarter of the night. Tell: the stage that makes up the majority of the sleep cycle and the longest by total duration is stage N2, not the dream state.", "adjacent fact"],
   ["Stage N3",
    "Stage N3 is the deepest, most restful non-rapid eye movement stage, and it decreases with age. Tell: depth is not duration; the stage that is the longest by total duration and fills the majority of the cycle is stage N2.", "competing diagnosis"],
   ["Stage N1",
    "Stage N1 is the brief, drowsy transition from wakefulness into light sleep. Tell: a transition stage does not make up the bulk of the night; stage N2 is the majority of the sleep cycle and the longest stage by total duration.", "wrong stage or severity"]],
  CS(13, 28, 9), "epidemiology", "test"),

V(NRM, IO_SWS,
  "A 40-year-old man in a sleep laboratory has been in deep, restful non-rapid eye movement sleep for 30 minutes. Which change in his vital signs is expected?",
  [["Lower blood pressure and heart rate",
    "Correct. Non-rapid eye movement sleep brings increased parasympathetic tone with low blood pressure, slow heart rate and decreased respiratory rate. Blood pressure, heart rate, respiratory rate and metabolic rate fall by about 10 to 30%, along with decreased peripheral vascular tone."],
   ["Irregular heart rate and breathing",
    "Irregular heart rate and respiratory rate, characteristic of the dream state, belong to rapid eye movement sleep. Tell: he is in deep, restful non-rapid eye movement sleep, where both rates slow steadily instead of becoming irregular.", "wrong stage or severity"],
   ["Higher blood pressure and heart rate",
    "This reverses the change: non-rapid eye movement sleep lowers blood pressure and heart rate by about 10 to 30% through increased parasympathetic tone. Tell: deep, restful sleep is a slowing, vegetative state, not a stimulated one.", "reversed direction or value"],
   ["Unchanged from wakefulness",
    "Deep non-rapid eye movement sleep does change the vital signs: blood pressure, heart rate, respiratory rate and metabolic rate fall by about 10 to 30%. Tell: increased parasympathetic tone in this sleep lowers them rather than leaving them at waking levels.", "common lay belief"]],
  CS(12, 14, 10), "manifestation", "physiology"),

V(NRM, IO_SWS,
  "A 45-year-old woman's heart rate and blood pressure fall steadily after she enters non-rapid eye movement sleep. Which autonomic change explains this?",
  [["Increased parasympathetic tone",
    "Correct. Non-rapid eye movement sleep brings increased parasympathetic tone, with low blood pressure, slow heart rate and decreased respiratory rate, together with decreased peripheral vascular tone. Her steady fall in heart rate and blood pressure is that parasympathetic shift."],
   ["Increased sympathetic tone",
    "The autonomic change of non-rapid eye movement sleep is increased parasympathetic tone, with low blood pressure and slow heart rate. Tell: her values fall steadily, which matches the parasympathetic change, not a sympathetic one.", "reversed direction or value"],
   ["Decreased parasympathetic tone",
    "This reverses the direction: parasympathetic tone rises in non-rapid eye movement sleep, producing low blood pressure, slow heart rate and decreased respiratory rate. Tell: a falling heart rate and blood pressure go with increased parasympathetic tone.", "reversed direction or value"],
   ["Inhibited spinal motor neurons",
    "Inhibited spinal muscle control areas and alpha motor neurons explain the atonia of rapid eye movement sleep, a muscle change. Tell: a falling heart rate and blood pressure in non-rapid eye movement sleep are autonomic, from increased parasympathetic tone.", "confused mechanism or drug class"]],
  CS(14, 12, 10, 28), "etiology", "physiology"),

V(NRM, IO_SWS,
  "A 36-year-old man's blood pressure, heart rate, breathing rate and metabolic rate are tracked as he passes into deep, restful non-rapid eye movement sleep. By about how much are these values expected to fall?",
  [["10 to 30 percent",
    "Correct. Deep, restful non-rapid eye movement sleep is associated with decreased peripheral vascular tone and other vegetative bodily functions: blood pressure, heart rate, respiratory rate and metabolic rate fall by about 10 to 30%, alongside increased parasympathetic tone."],
   ["1 to 5 percent",
    "A change this small would barely register, but the fall in vegetative functions during deep non-rapid eye movement sleep is 10 to 30%. Tell: the slowing in this sleep is substantial, enough to describe as low blood pressure and slow heart rate.", "reversed direction or value"],
   ["40 to 60 percent",
    "This overstates the change: blood pressure, heart rate, respiratory rate and metabolic rate fall by about 10 to 30% in deep non-rapid eye movement sleep. Tell: the fall tops out at 30%, well short of halving these values.", "reversed direction or value"],
   ["70 to 90 percent",
    "A fall this large would nearly stop circulation and breathing; the fall in deep non-rapid eye movement sleep is 10 to 30%. Tell: the number to remember is 10 to 30%, set against the rise of up to 20% in brain metabolism during rapid eye movement sleep.", "reversed direction or value"]],
  CS(12, 14, 10), "manifestation", "physiology"),

V(NRM, IO_SWS,
  "A 34-year-old woman in a sleep study has moved into stage N2, the less responsive, deeper sleep that follows the drowsy transition. Which change in her body temperature and heart rate is expected?",
  [["They decrease",
    "Correct. Stage N2 is less responsive, deeper sleep in which heart rate and temperature decrease, fitting the slow heart rate and increased parasympathetic tone of non-rapid eye movement sleep. Stage N2 is also the longest stage by total duration."],
   ["They increase",
    "This reverses the change: in stage N2 heart rate and temperature decrease, as part of the slowing of non-rapid eye movement sleep. Tell: deeper non-rapid eye movement sleep lowers these values, with increased parasympathetic tone.", "reversed direction or value"],
   ["They become irregular",
    "Irregular heart rate and breathing mark rapid eye movement sleep, the dream state. Tell: in stage N2, a non-rapid eye movement stage, heart rate and temperature both fall steadily rather than fluctuating, with increased parasympathetic tone.", "wrong stage or severity"],
   ["Temperature rises, heart rate falls",
    "Heart rate does fall in stage N2, but temperature falls with it rather than rising, as part of the general slowing of non-rapid eye movement sleep. Tell: both values decrease in stage N2, so an answer that sends one of them up is wrong.", "reversed direction or value"]],
  CS(28, 14), "manifestation", "physiology"),

V(NRM, IO_SWS,
  "A 29-year-old man settles into bed in a sleep laboratory, and a few minutes later he is drowsy and drifting off into light sleep. Which stage is he in?",
  [["Stage N1",
    "Correct. Stage N1 is the transition from wakefulness: the person is somnolent or drowsy and in light sleep. Minutes after settling into bed and drifting off, he fits this first non-rapid eye movement stage, before the deeper stages N2 and N3."],
   ["Stage N2",
    "Stage N2 is less responsive, deeper sleep, with heart rate and temperature falling, and it is the longest stage by total duration. Tell: drowsiness at the edge of wakefulness, minutes after lying down, is stage N1.", "wrong stage or severity"],
   ["Stage N3",
    "Stage N3 is the deepest, most restful non-rapid eye movement stage, with delta waves and tissue growth and repair. Tell: he is only drowsy and drifting off, which is the light transition stage, stage N1, not the deepest one.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "The first rapid eye movement period comes at the end of the first 90- to 120-minute cycle, after the non-rapid eye movement stages. Tell: a few minutes after lying down he is still in the drowsy transition, stage N1.", "wrong stage or severity"]],
  CS(28, 27, 6, 7), "manifestation", "classify"),

V(NRM, IO_STAGES,
  "A 28-year-old woman in a sleep laboratory has passed beyond drowsy, light sleep. She is now less responsive, her heart rate and temperature are falling, and her electroencephalogram shows theta waves. Which stage is she in?",
  [["Stage N2",
    "Correct. Stage N2 is less responsive, deeper sleep in which heart rate and temperature decrease, and its electroencephalogram shows theta waves. She has moved past the drowsy, light sleep of stage N1 but does not show the delta waves of stage N3."],
   ["Stage N1",
    "Stage N1 also shows theta waves, but it is the drowsy transition from wakefulness into light sleep. Tell: she has passed beyond drowsy, light sleep and her heart rate and temperature are falling, which marks stage N2.", "ruled out by a stated finding"],
   ["Stage N3",
    "Stage N3, the deepest non-rapid eye movement stage, shows delta waves, below 3.5 cycles per second. Tell: her tracing shows theta waves together with falling heart rate and temperature, which fits stage N2 rather than stage N3.", "wrong stage or severity"],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep shows a mixed, low-voltage, beta-like tracing with sawtooth waves, and its heart rate is irregular. Tell: theta waves with a steady fall in heart rate and temperature point to stage N2.", "wrong stage or severity"]],
  CS(28, 14), "test finding", "classify"),

V(NRM, IO_SWS,
  "A 74-year-old woman says she no longer sleeps as deeply as she did in her twenties. Which sleep stage can she be told decreases with age?",
  [["Stage N3",
    "Correct. Stage N3, the deep, restful, deepest non-rapid eye movement stage with delta waves, decreases with age. Her sense that her sleep is less deep than it was in her twenties fits a smaller share of stage N3 sleep."],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep is not restful or deep, so it cannot account for a loss of deep sleep. Tell: the deep, restful stage that decreases with age is stage N3, the deepest non-rapid eye movement stage.", "competing diagnosis"],
   ["Stage N2",
    "Stage N2 is the longest stage by total duration, a less responsive, deeper sleep but not the deepest. Tell: losing the deepest sleep with age is a loss of stage N3, the stage that decreases with age.", "wrong stage or severity"],
   ["Stage N1",
    "Stage N1 is the drowsy, light transition from wakefulness. Tell: a light stage cannot explain losing deep sleep; the deepest stage, stage N3, is the one that decreases with age.", "wrong stage or severity"]],
  CS(28, 6), "epidemiology", "education"),

V(NRM, IO_SWS,
  "A 16-year-old athlete asks during which stage of sleep body tissue growth and repair take place. Which stage should he be told?",
  [["Stage N3",
    "Correct. Stage N3, the deep, restful, deepest non-rapid eye movement stage, is when body and tissue growth and repair occur. Its electroencephalogram shows delta waves, and it is the stage that decreases with age."],
   ["Rapid eye movement sleep",
    "Rapid eye movement sleep is the active dream state, with brain metabolism raised by as much as 20%, and it is not restful or deep. Tell: tissue growth and repair belong to the deep, restful stage N3.", "adjacent fact"],
   ["Stage N2",
    "Stage N2 is the longest stage by total duration, with heart rate and temperature falling, but it is not the stage where growth and repair are placed. Tell: body and tissue growth and repair occur in stage N3, the deepest stage.", "adjacent fact"],
   ["Stage N1",
    "Stage N1 is the brief, drowsy transition from wakefulness into light sleep. Tell: growth and repair are placed in the deepest, most restful stage, stage N3, not in the lightest one.", "wrong stage or severity"]],
  CS(28, 6, 10), "education", "education"),

V(NRM, IO_SWS,
  "A 29-year-old man insists that he never dreams outside the dreaming stage because non-rapid eye movement sleep is dreamless. Which statement about non-rapid eye movement sleep is accurate?",
  [["Dreams occur but are often forgotten",
    "Correct. Non-rapid eye movement sleep is often called a dreamless state, but that is not accurate: dreams and nightmares do occur. They are often not remembered because the dreams are not consolidated in memory, and they are less vivid than rapid eye movement dreams."],
   ["It is truly a dreamless state",
    "This is the common label, and it is not accurate: dreams and nightmares do occur in non-rapid eye movement sleep. Tell: they happen but are often not remembered, which is why this sleep only seems dreamless.", "common lay belief"],
   ["Its dreams carry more muscle activity",
    "The reverse is true: dreams during rapid eye movement sleep are the ones associated with more bodily muscle activity. Tell: muscle activity with dreaming points to rapid eye movement sleep, not to non-rapid eye movement sleep.", "reversed direction or value"],
   ["Its dreams are the most vivid ones",
    "Non-rapid eye movement sleep has less vivid dreams; vivid dreaming is associated with rapid eye movement sleep. Tell: non-rapid eye movement dreams are fainter and often forgotten, while the vivid ones belong to rapid eye movement sleep.", "reversed direction or value"]],
  CS(13, 14, 9), "education", "education"),

# ---------------------------------------------------------------- functions of sleep
V(FUN, IO_FUNC,
  "A 29-year-old surgical resident has slept about 4 hours a night for the past 5 nights. Which effect of this sleep restriction is expected?",
  [["Lower cognitive and physical performance",
    "Correct. Sleep restriction over a few days can cause decreased cognitive and physical performance, lower overall productivity and poorer health. Five nights of about 4 hours is restriction over a few days, so both his thinking and his physical work are expected to suffer."],
   ["Sharper focus from adapting to less sleep",
    "Restriction does not sharpen the mind; over a few days it decreases cognitive and physical performance. Tell: the expected direction is downward, in cognition, physical performance, productivity and health, not an adaptive gain.", "common lay belief"],
   ["Effects limited to daytime mood",
    "The effects of sleep restriction are broader: decreased cognitive and physical performance, overall productivity and health. Tell: his surgical work itself is expected to suffer, not just how he feels during the day.", "common lay belief"],
   ["No effect until weeks of restriction",
    "Harm does not wait for weeks: sleep restriction over a few days can already decrease performance, productivity and health. Tell: 5 nights of short sleep falls within the few days that are enough to expect effects.", "reversed direction or value"]],
  C(16), "complication", "complication"),

V(FUN, IO_FUNC,
  "A 34-year-old new mother has been sleeping about 4 hours a night for a week and has gone back to her office job. Which change is expected from this sleep restriction?",
  [["Reduced productivity at work",
    "Correct. Sleep restriction over a few days can decrease cognitive and physical performance, overall productivity and the health of a person. A week of about 4 hours a night is restriction over more than a few days, so lower productivity at work is expected."],
   ["More output from longer waking days",
    "Extra waking hours do not translate into more output: restriction over a few days decreases overall productivity. Tell: her productivity is expected to fall, along with cognitive and physical performance and health.", "common lay belief"],
   ["Better physical performance",
    "This reverses the effect: sleep restriction over a few days decreases physical as well as cognitive performance. Tell: each effect of restriction is a decrease, in performance, productivity and health.", "reversed direction or value"],
   ["No change for at least a month",
    "Effects appear within days, not after a month: restriction over a few days can decrease performance, productivity and health. Tell: a week of short nights is already longer than the few days that are enough.", "reversed direction or value"]],
  C(16), "complication", "complication"),

V(FUN, IO_FUNC,
  "A 24-year-old competitive cyclist has cut her sleep to 5 hours a night for the 4 nights before a race. Which effect on her race performance is expected?",
  [["Lower physical performance",
    "Correct. Sleep restriction over a few days can decrease physical as well as cognitive performance, along with productivity and health. Four nights of 5 hours before her race is restriction over a few days, so her physical performance is expected to fall."],
   ["Higher endurance from training more",
    "Trading sleep for training time does not raise endurance; restriction over a few days decreases physical performance. Tell: the effects of restriction run downward, in physical and cognitive performance alike.", "common lay belief"],
   ["No change after so few nights",
    "A few nights are enough: sleep restriction over a few days can already decrease physical and cognitive performance. Tell: 4 short nights is within that window, so an effect on her race is expected.", "reversed direction or value"],
   ["Faster times from a lower heart rate",
    "The slow heart rate of non-rapid eye movement sleep is a change during sleep itself, not a racing benefit of sleeping less. Tell: cutting sleep lowers physical performance; it does not borrow the slowing of deep sleep.", "confused mechanism or drug class"]],
  CS(16, 14), "complication", "complication"),

V(FUN, IO_FUNC,
  "A 20-year-old student plans to sleep 3 hours a night for the 4 nights before an exam, reasoning that nobody knows what sleep is for anyway. What should he be told?",
  [["Short nights can impair his thinking",
    "Correct. Sleep restriction over a few days can decrease cognitive and physical performance, productivity and health, and the functions of sleep include cognition and the facilitation of learning or memory. Four nights of 3 hours is restriction over a few days, so his studying could backfire."],
   ["Sleep's role is unknown, so cutting it is safe",
    "Researchers have limited understanding of why sleep is essential, but its importance is not in doubt: restriction over a few days already decreases performance. Tell: unknown mechanisms do not mean no effect.", "common lay belief"],
   ["Harm needs months of short sleep",
    "Restriction over a few days is enough to decrease cognitive and physical performance, productivity and health. Tell: 4 short nights fall within that window, so harm is expected well before months have passed.", "reversed direction or value"],
   ["Short sleep mainly costs physical strength",
    "Restriction lowers physical performance, but it lowers cognitive performance too, and sleep supports cognition and learning or memory. Tell: for exam preparation, the cognitive cost is the one that matters, and it is part of the expected effect.", "adjacent fact"]],
  CS(16, 17), "complication", "education"),

V(FUN, IO_FUNC,
  "A 19-year-old student learning anatomy asks which function of sleep helps her retain what she studies. Which function is it?",
  [["Facilitating learning or memory",
    "Correct. Facilitation of learning or memory is one of the functions of sleep, alongside cognition, and it is the function tied to retaining what she studies. Restricting sleep over a few days lowers cognitive performance, which works against her."],
   ["Targeted erasure of synapses",
    "This function works the other way: sleep targets synapses for erasure so that unimportant information that might clutter the synaptic network is forgotten. Tell: erasure helps forget the unimportant, while facilitation of learning or memory helps retain.", "adjacent fact"],
   ["Conserving metabolic energy",
    "Conservation of metabolic energy is a function of sleep, but it concerns the body's energy use, not learning. Tell: holding on to what she studies is the job of the learning or memory function, not of energy conservation.", "adjacent fact"],
   ["Clearing metabolic waste",
    "Sleep clears metabolic waste products generated by neural activity in the awake brain, a housekeeping function rather than one for retaining information. Tell: the function aimed at what she studies is facilitation of learning or memory.", "adjacent fact"]],
  CS(17, 16), "education", "education"),

V(FUN, IO_FUNC,
  "A 23-year-old man asks why trivial details of his day seem to fade after a night's sleep while what mattered stays. Which function of sleep explains this?",
  [["Targeted erasure of synapses",
    "Correct. One function of sleep is targeted erasure of synapses to forget unimportant information that might otherwise clutter the synaptic network. Losing trivial details while keeping what matters fits that function, which works alongside sleep's facilitation of learning or memory."],
   ["Facilitating learning or memory",
    "That function helps him keep information, the opposite of losing it. Tell: the fading of unimportant details is the work of targeted erasure of synapses, which keeps the synaptic network uncluttered.", "reversed direction or value"],
   ["Clearing metabolic waste",
    "Sleep clears metabolic waste products generated by neural activity in the awake brain; that removes chemical by-products, not information. Tell: forgetting trivia on purpose is targeted erasure of synapses, not waste clearance.", "confused mechanism or drug class"],
   ["Neural maturation",
    "Neural maturation is a function of sleep that concerns the maturing of the nervous system, not the pruning of a day's trivia. Tell: forgetting unimportant information that might clutter the network is targeted erasure of synapses.", "adjacent fact"]],
  C(17), "education", "education"),

V(FUN, IO_FUNC,
  "A 46-year-old woman asks what sleep does about the by-products her brain makes while she is awake and thinking. Which function answers her?",
  [["Clearing metabolic waste",
    "Correct. One function of sleep is clearance of metabolic waste products generated by neural activity in the awake brain. Her question about the by-products of her brain's waking activity is answered by that clearance function."],
   ["Conserving metabolic energy",
    "Energy conservation is a separate function of sleep, and it concerns saving energy rather than removing anything. Tell: removing the by-products of waking neural activity is clearance of metabolic waste, not conservation of energy.", "adjacent fact"],
   ["Targeted erasure of synapses",
    "Synaptic erasure removes unimportant information that might clutter the synaptic network, not chemical by-products. Tell: the by-products of neural activity in the awake brain are cleared as metabolic waste.", "confused mechanism or drug class"],
   ["Raising brain metabolism",
    "Overall brain metabolism can rise by as much as 20% in rapid eye movement sleep, which is a feature of that stage, not a function that removes by-products. Tell: removal is clearance of metabolic waste.", "adjacent fact"]],
  CS(17, 10), "education", "education"),

V(FUN, IO_FUNC,
  "A 2-month-old boy's parents ask what sleep does for his developing nervous system. Which function of sleep answers them?",
  [["Neural maturation",
    "Correct. Neural maturation is one of the functions of sleep, and it is the one that speaks to a developing nervous system. Sleep's physiological effects fall into two groups, effects on the nervous system and effects on the body's other functional systems, and maturation belongs with the first."],
   ["Conserving metabolic energy",
    "Conservation of metabolic energy is a function of sleep, but it concerns energy use rather than development of the nervous system. Tell: the parents ask about a developing nervous system, which is neural maturation.", "adjacent fact"],
   ["Targeted erasure of synapses",
    "This function trims synapses holding unimportant information that might clutter the synaptic network; it is about forgetting, not about maturing. Tell: maturation of a developing nervous system is neural maturation.", "adjacent fact"],
   ["Clearing metabolic waste",
    "Sleep clears metabolic waste generated by neural activity in the awake brain, a cleanup role rather than a developmental one. Tell: the parents ask how sleep helps a nervous system develop, which is neural maturation.", "adjacent fact"]],
  C(17), "education", "education"),

V(FUN, IO_FUNC,
  "A 50-year-old man asks whether scientists fully understand why sleep is essential. Which reply is accurate?",
  [["No; its functions are still under study",
    "Correct. Sleep has important physiological functions, but researchers have limited understanding of why it is an essential part of life; its specific physiological functions remain a mystery and continue to be researched. Its functions include neural maturation, learning or memory, cognition, waste clearance and energy conservation."],
   ["Yes; it exists to save energy",
    "Conservation of metabolic energy is one function among several, and the specific functions of sleep are not settled. Tell: a single settled purpose contradicts the limited understanding researchers describe.", "adjacent fact"],
   ["Yes; it mainly rests the muscles",
    "Resting the muscles is not among the functions of sleep; the effects of sleep fall on the nervous system and on the other functional systems, and the specifics remain under research. Tell: the answer to whether it is fully understood is no.", "common lay belief"],
   ["No; it seems to have no real function",
    "Uncertainty about why sleep is essential is not doubt that it matters: sleep has important physiological functions, and restriction over a few days decreases performance and health. Tell: the functions are real; their specifics are still being researched.", "reversed direction or value"]],
  CS(16, 17), "education", "education"),

V(FUN, IO_FUNC,
  "A 37-year-old woman believes that sleep matters for the brain and nothing else. Which statement about the physiological effects of sleep is accurate?",
  [["It affects brain and body systems",
    "Correct. Sleep has two major types of physiological effects: effects on the nervous system and effects on the other functional systems of the body. Its functions span both, from neural maturation and cognition to conservation of metabolic energy, so its importance is not limited to the brain."],
   ["It affects the brain alone",
    "That leaves out half of the picture: sleep also has effects on other functional systems of the body, such as the fall in blood pressure, heart rate and metabolic rate in non-rapid eye movement sleep. Tell: there are two types of effects, nervous system and body.", "common lay belief"],
   ["It affects the muscles alone",
    "Muscle tone does change in sleep, being very depressed in rapid eye movement sleep, but the two major types of effects are on the nervous system and on the other functional systems. Tell: the brain is one of the two targets, not left out.", "adjacent fact"],
   ["Its effects are purely psychological",
    "The effects of sleep are physiological, on the nervous system and on other body systems, including blood pressure, heart rate, breathing and metabolic rate. Tell: a measurable 10 to 30% fall in these values during non-rapid eye movement sleep is not psychological.", "common lay belief"]],
  CS(17, 12, 10), "education", "education"),

# ---------------------------------------------------------------- the sleep-wake cycle
V(SWC, IO_FUNC,
  "A 24-year-old student has been awake and studying for 20 hours and finally dozes off at his desk. Which proposed mechanism explains his transition from wakefulness to sleep?",
  [["Fatigue of activating-system neurons",
    "Correct. After the brain has remained active for many hours, neurons in the activating system become fatigued, the positive feedback cycle between the mesencephalic reticular nuclei and the cerebral cortex fades, and the sleep-promoting centers take over. Twenty hours of studying fits that fatigue."],
   ["Stronger reticular-cortex positive feedback",
    "Positive feedback between the reticular nuclei and the cortex sustains wakefulness, and it fades rather than strengthens as sleep approaches. Tell: strengthening that loop would keep him awake; its fading lets the sleep-promoting centers take over.", "reversed direction or value"],
   ["Release of reticular nuclei from inhibition",
    "Release of the mesencephalic and upper pontile reticular activating nuclei from inhibition is the proposed start of wakefulness, when the sleep centers are not activated. Tell: release from inhibition wakes the brain; fatigue of those neurons lets sleep in.", "reversed direction or value"],
   ["Increased parasympathetic tone",
    "Increased parasympathetic tone describes the body during non-rapid eye movement sleep, with low blood pressure and slow heart rate. Tell: it is a feature of sleep once it has begun, while the proposed trigger for the transition is fatigue of the activating system.", "confused mechanism or drug class"]],
  CS(19, 18, 14), "etiology", "physiology"),

V(SWC, IO_FUNC,
  "A 30-year-old woman wakes in the morning and stays awake through the day without effort. According to the proposed sleep-wake theory, what keeps her wakefulness going once it begins?",
  [["Reticular-cortex positive feedback",
    "Correct. Once wakefulness begins, it can sustain itself naturally because of a positive feedback mechanism: the reticular activating nuclei excite the cerebral cortex and peripheral nervous system, which send positive feedback signals back to the same nuclei and keep them active."],
   ["Continuous activation of sleep centers",
    "Wakefulness begins when the sleep centers are not activated, which releases the reticular activating nuclei from inhibition. Tell: active sleep centers would favor sleep, not sustain her waking day; the positive feedback loop does that.", "reversed direction or value"],
   ["Fatigue of activating-system neurons",
    "Fatigue after many hours awake is what ends wakefulness: the feedback cycle fades and the sleep-promoting centers take over. Tell: fatigue closes the waking day; positive feedback between the reticular nuclei and the cortex carries it.", "reversed direction or value"],
   ["Rising parasympathetic tone",
    "Increased parasympathetic tone, with low blood pressure and slow heart rate, belongs to non-rapid eye movement sleep. Tell: it is a feature of sleep, not the loop that sustains wakefulness, which is reticular-cortex positive feedback.", "confused mechanism or drug class"]],
  CS(18, 19, 14), "etiology", "physiology"),

V(SWC, IO_FUNC,
  "A 26-year-old man is waking up as his sleep centers stop being activated. Which structures are proposed to be released from inhibition and to activate spontaneously?",
  [["Mesencephalic and upper pontile reticular nuclei",
    "Correct. The proposed theory holds that when the sleep centers are not activated, the mesencephalic and upper pontile reticular activating nuclei are released from inhibition and activate spontaneously, exciting the cerebral cortex and peripheral nervous system, which feed back positively to keep them active."],
   ["Sleep-promoting centers within the sleep centers",
    "These take over at the other end of the day, when activating-system neurons fatigue and the feedback cycle fades. Tell: waking begins with the reticular activating nuclei released from inhibition, not with the sleep-promoting centers.", "reversed direction or value"],
   ["Spinal muscle control areas and motor neurons",
    "Spinal muscle control areas and alpha motor neurons are inhibited in rapid eye movement sleep, producing atonia; they are not the activating system. Tell: waking is driven by the mesencephalic and upper pontile reticular activating nuclei.", "adjacent fact"],
   ["Occipital and parietal regions of the cortex",
    "The occipital region is where alpha waves are most intense, and the cortex is the target the reticular nuclei excite, not the source released from inhibition. Tell: release from inhibition happens in the reticular activating nuclei.", "adjacent fact"]],
  CS(18, 10, 28, 22), "etiology", "physiology"),

V(SWC, IO_FUNC,
  "A 25-year-old woman has been awake and active for many hours, and the feedback loop between her reticular nuclei and her cerebral cortex is fading. Which centers are proposed to take over at this point?",
  [["Sleep-promoting centers",
    "Correct. After the brain has remained active for many hours, neurons in the activating system fatigue, the positive feedback cycle between the mesencephalic reticular nuclei and the cerebral cortex fades, and the sleep-promoting centers of the sleep centers take over, bringing the transition from wakefulness to sleep."],
   ["Reticular activating nuclei",
    "These nuclei drive wakefulness, and it is their fatigue that lets the feedback loop fade. Tell: the centers that take over as the loop weakens are the sleep-promoting centers, which bring the transition into sleep.", "reversed direction or value"],
   ["Cerebral cortex",
    "The cortex is the partner the reticular nuclei excite in the positive feedback loop that sustains wakefulness. Tell: as that loop fades, control passes to the sleep-promoting centers, not to the cortex.", "adjacent fact"],
   ["Spinal muscle control areas",
    "These areas are inhibited during rapid eye movement sleep to produce atonia; they do not start sleep. Tell: the transition from wakefulness into sleep is handed to the sleep-promoting centers once the activating system fatigues.", "adjacent fact"]],
  CS(19, 18, 10), "etiology", "physiology"),

V(SWC, IO_FUNC,
  "A 33-year-old woman asks whether the cause of the daily cycle between sleep and wakefulness is fully understood. Which reply is accurate?",
  [["No; there are proposed theories",
    "Correct. There is no definitive explanation of the sleep-wakefulness cycle, but there are proposed theories: release of the reticular activating nuclei from inhibition starts wakefulness, positive feedback sustains it, and fatigue of the activating system ends it."],
   ["Yes; the sleep centers alone control it",
    "The cycle is not settled, and the proposed theory involves the reticular activating nuclei and their positive feedback with the cortex as well as the sleep centers. Tell: there is no definitive explanation, and the theories involve several players.", "common lay belief"],
   ["No; the brain plays no part in it",
    "The proposed theories place the cycle in the brain: the reticular activating nuclei, the cerebral cortex and the sleep centers, and states of brain activity arise from forces generated within the brain. Tell: uncertain does not mean outside the brain.", "reversed direction or value"],
   ["Yes; it simply follows muscle fatigue",
    "The cycle is not settled, and the fatigue in the proposed theory is of neurons in the activating system, not of muscles. Tell: there is no definitive explanation, and the fatigue that ends wakefulness is neural.", "confused mechanism or drug class"]],
  CS(18, 19, 3), "education", "education"),

V(SWC, IO_FUNC,
  "A 31-year-old woman notices that her day moves between focused work, a moment of fear, an evening of exhilaration and then sleep. She asks what generates these different states. Which answer is accurate?",
  [["Activating or inhibiting brain forces",
    "Correct. The brain has many states of activity, including sleep, wakefulness, extreme excitement and different levels of mood such as exhilaration, depression and fear, and they arise, for the most part, from different activating or inhibiting forces generated within the brain."],
   ["Outside stimuli acting on a passive brain",
    "The states of brain activity arise, for the most part, from forces generated within the brain itself. Tell: the brain is not passive here; its own activating or inhibiting forces produce sleep, wakefulness and mood.", "common lay belief"],
   ["Fatigued muscles signaling the brain",
    "The fatigue in the proposed sleep-wake theory is of neurons in the activating system, not of muscles, and moods such as fear are not explained by muscle signals. Tell: the states come from activating or inhibiting forces within the brain.", "confused mechanism or drug class"],
   ["Sleep centers that stay switched on",
    "Sleep centers that stay activated would favor sleep, yet she moves through waking states too; wakefulness begins when the sleep centers are not activated. Tell: shifting states come from changing activating or inhibiting forces in the brain.", "reversed direction or value"]],
  CS(3, 18, 19), "etiology", "education"),

]
