# -*- coding: utf-8 -*-
"""Lecture 39 (Phases of Sleep, Shah) cram topics, condensed from guide section 1.

CRITERIA: one table per classification, cut-off or staging table on the slides (Jaxon's standing rule, memory
cram_criteria_tables), each with a labeled memory aid. Cells are the slide wording; slide conflicts are note rows.
Phase 1 (2026-11-02): slides only; the recording will add the emphasis card's spoken items.
"""
L39C = "#5e4123"

CRITERIA = [
{"id": "crit-l39-waves", "label": "The Four EEG Waveforms", "color": L39C,
 "tag": "Classification &middot; Lecture 39 &middot; slides 21&ndash;26",
 "cols": ["Wave", "Frequency (cycles/second)", "Where and when"], "widths": ["14%", "24%", "62%"], "rows": [
  ("<b>Beta</b>", "<b>Greater than 14</b> (as high as 80)", "Parietal and frontal regions; <b>asynchronous, low voltage</b>; <b>awake, alert, actively processing</b> information"),
  ("<b>Alpha</b>", "<b>8&ndash;13</b>, rhythmical", "Healthy adults <b>awake, quiet and resting</b>; most intense <b>occipital</b>; <b>disappear in deep sleep</b>; replaced by beta when attention is directed to a task"),
  ("<b>Theta</b>", "<b>4&ndash;7</b>", "Parietal and temporal regions <b>in children</b>; <b>emotional stress</b> in some adults (disappointment, frustration); <b>degenerative brain disorders</b>"),
  ("<b>Delta</b>", "<b>Less than 3.5</b>", "Voltage <b>2&ndash;4 times</b> other waves; strictly cortical; <b>very deep sleep, infancy, serious organic brain disease</b>, cortex cut off from the thalamus"),
 ], "mnemonic": {"hook": "Fastest to slowest the waves spell BAT-D: Busy, At rest, Tired, Deep.",
  "key": [["B", "Beta: busy, alert, actively processing (&gt;14)"], ["A", "Alpha: awake but at rest, quiet (8&ndash;13)"],
          ["T", "Theta: tired (light sleep), children, stress, brain disorders (4&ndash;7)"], ["D", "Delta: deep sleep, infancy, organic brain disease (&lt;3.5)"]],
  "breaks": "&ldquo;Tired&rdquo; covers only theta&rsquo;s sleep use; its children, stress and brain-disorder settings must be learned separately."}},

{"id": "crit-l39-stages", "label": "EEG by Stage of Wakefulness and Sleep", "color": L39C,
 "tag": "Staging &middot; Lecture 39 &middot; slide 28 (with 27, 29)",
 "cols": ["Stage", "What happens", "EEG"], "widths": ["20%", "52%", "28%"], "rows": [
  ("Awake, eyes open", "Alert and active", "<b>Beta</b>"),
  ("Awake, eyes closed", "Decreased alertness, relaxation", "<b>Alpha</b>"),
  ("<b>N1</b>", "Transition from wakefulness; drowsy; light sleep", "<b>Theta</b>"),
  ("<b>N2</b>", "Deeper sleep; heart rate and temperature fall; <b>longest stage by total duration</b>", "Theta; <b>sleep spindles</b> (12&ndash;14 Hz bursts); <b>K complexes</b> (negative sharp wave then positive component)"),
  ("<b>N3</b> (deep, slow-wave)", "Deepest non-REM stage; harder to arouse; <b>growth and repair</b>; <b>decreases with age</b>", "<b>Delta</b>"),
  ("<b>REM</b> (stage R)", "Dream state; rapid, irregular eye movements; <b>atonia except eyes and diaphragm</b>; sawtooth waves", "<b>Beta</b> (like awake, with atonia)"),
  {"note": "Slide 27 and the slide 29 picture use FOUR non-REM stages and put spindles in stage 1; the slide 28 table (above) uses three and puts spindles in N2."},
 ], "mnemonic": {"hook": "BATTeD, then Back: down the night the waves go Beta, Alpha, Theta, Theta, Delta, and REM goes Back to beta.",
  "key": [["B", "Eyes open: beta"], ["A", "Eyes closed: alpha"], ["T", "N1: theta"], ["T", "N2: theta (+ spindles, K complexes)"],
          ["D", "N3: delta"], ["Back", "REM: back to beta, with atonia"]],
  "breaks": "The vowel &ldquo;e&rdquo; in BATTeD stands for nothing."}},

{"id": "crit-l39-numbers", "label": "Sleep by the Numbers", "color": L39C,
 "tag": "Cut-offs &middot; Lecture 39 &middot; slides 6, 9, 10, 12",
 "cols": ["Measure", "Value"], "widths": ["58%", "42%"], "rows": [
  ("Average sleep", "<b>8 hours</b>"),
  ("Cycles per night", "<b>4&ndash;5</b>"),
  ("Length of one cycle", "<b>90&ndash;120 minutes</b>"),
  ("REM share of a young adult&rsquo;s sleep", "<b>About 25%</b>"),
  ("REM episodes", "Recur about <b>every 90 minutes</b>; each lasts <b>5&ndash;30 minutes</b>"),
  ("Non-REM fall in blood pressure, heart rate, breathing, metabolic rate", "<b>10&ndash;30%</b>"),
  ("REM rise in brain metabolism", "Up to <b>20%</b>"),
 ], "mnemonic": {"hook": "8 hours, 4&ndash;5 laps of 90: a quarter of it dreaming.",
  "key": [["8", "hours of sleep on average"], ["4&ndash;5", "cycles"], ["90", "minutes: cycle length starts at 90 (to 120) and REM recurs every 90"],
          ["A quarter", "REM is about 25% of a young adult&rsquo;s sleep"]],
  "breaks": "Leaves out the 5&ndash;30 minute REM episode, the 10&ndash;30% non-REM fall and the 20% REM rise: learn those from the table."}},
]

TOPICS = [
{"id": "l39-emph", "label": "★ Emphasized: Sleep Physiology", "color": "#b8860b", "rows": [
  ["★ CAN vs CANNOT", "Capitals on the slide: sleep = unconsciousness from which a person <b>CAN</b> be aroused; coma = one from which a person <b>CANNOT</b>."],
  ["Recording", "Not in yet (Monday 2 November): her spoken emphasis is added when it arrives."],
]},
{"id": "l39-rem-nrem", "label": "REM vs Non-REM Sleep", "color": L39C, "rows": [
  ["Non-REM (slow-wave)", "Deep, <b>extremely restful</b>; <b>increased parasympathetic tone</b>; blood pressure, heart rate, breathing and metabolic rate <b>10&ndash;30% lower</b>; dreams less vivid and <b>often not remembered</b> (not consolidated). Stages N1, <b>N2 (the majority)</b>, N3."],
  ["REM", "Not restful; <b>vivid dreams</b> with muscle activity; <b>muscle tone very depressed</b> (atonia except eyes and diaphragm); heart rate and breathing <b>irregular</b>; brain metabolism up to <b>20%</b> higher; <b>harder to arouse than non-REM</b>, yet spontaneous morning waking happens in REM."],
  ["Paradoxical / desynchronized", "REM&rsquo;s EEG looks like wakefulness (<b>paradoxical sleep</b>); neurons fire without synchrony (<b>desynchronized sleep</b>)."],
  ["Very sleepy", "REM episodes are <b>short or absent</b>; they lengthen as the person becomes rested."],
]},
{"id": "l39-functions", "label": "Why We Sleep &amp; the Sleep-Wake Cycle", "color": "#2f5d6b", "rows": [
  ["Sleep restriction", "Over a few days: worse <b>cognitive and physical performance</b>, productivity and health."],
  ["Two effect types", "On the <b>nervous system</b> and on <b>other body systems</b>; the exact functions remain a mystery."],
  ["Functions", "Neural maturation; learning and memory; <b>targeted erasure of synapses</b>; cognition; <b>clearing metabolic waste</b> of the awake brain; <b>conserving metabolic energy</b>."],
  ["Waking up", "Sleep centers off &rarr; <b>mesencephalic and upper pontile reticular activating nuclei</b> released &rarr; cortex excited &rarr; <b>positive feedback</b> keeps wakefulness going."],
  ["Falling asleep", "Hours later the activating neurons <b>fatigue</b>, the feedback loop fades and <b>sleep-promoting centers take over</b>. No definitive explanation exists."],
]},
]
