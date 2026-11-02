# -*- coding: utf-8 -*-
"""Lecture 39 scope -- Phases of Sleep (Sleep Physiology) (Shah), CMS I Exam 7 (Respiratory Block Exam II,
Monday 2026-11-16, Lectures 39-45).

Read by cms_e7_partition.py (guards) and imported by every Lecture 39 pool.
Not a question bank: check_pool_cites does not glob it.

LECTURER: Chand Shah, MPAS, PA-C, Assistant Professor -- title slide. calendar-data.js lists "CMS I - LECTURE
#39 - Phases of Sleep (Sleep Physiology) - Professor Shah", Monday 2026-11-02, 10-11 AM (1 hour). No conflict.
Deck file "CMS 1 Phases of Sleep - Shah Fallsv.pptx", 31 slides.

PHASE 1 (2026-11-02) = SLIDES ONLY. The live recording (Notability) is not in yet; when it arrives it sets emphasis
and scope only (slides-only grounding; time spoken never adds off-deck content).

IOS are the SYLLABUS objectives, verbatim (CMS syllabus.pdf p. 19, "Phases of Sleep (Sleep Physiology)"), the
leading letters dropped. Objective a prints without a final period; quoted as printed. The deck's own objectives
slide (s2) words objective a differently ("Define sleep and distinguish sleep from coma"): the syllabus wins.

SLIDE CONFLICTS (never keyed one way or the other; the guide notes each):
  NREM stage count: s13, s15 and the s28 table divide NREM into THREE stages (N1, N2, N3); the s7 hypnogram, the
      s27 list and the s29 picture use FOUR (stages 1-4, delta waves in stage 4). Items name stages N1-N3 only and
      never ask how many NREM stages there are.
  Sleep spindles: s27 places them in the FIRST stage ("short spindle-shaped bursts of alpha waves") and the s29
      picture labels "Stage 1 sleep (low voltage and spindles)"; the s28 table places spindles and K complexes in
      STAGE N2 ("bursts of monomorphic 12- to 14-Hz waves"). Spindles and K complexes are never keyed to a stage.
  "Slow-wave sleep": s6 uses it for ALL non-REM sleep ("Slow-Wave Sleep (aka non-REM sleep - NREM)"); the s28
      table uses it for stage N3 only ("Stage N3 (deep sleep, or slow-wave sleep)"). Items say "non-rapid eye
      movement sleep" or "stage N3", and use "slow-wave sleep" only where both readings give the same answer.
  Delta frequency: s26 "less than 3.5 cycles/second"; s27 "1-3 waves per second in stage 4". Delta is keyed as
      "below 3.5 cycles per second"; the 1-3 figure is never an option.
  Theta: the s28 table gives theta for N1 and N2; the s29 picture gives theta for stages 2 and 3. Theta is keyed
      to N1 and N2 only through the s28 table, never to "stage 3".
  Arousal: s10 says REM is "more difficult to arouse by sensory stimuli than during NREM"; s28 calls N3 the stage
      that is "More difficult to arouse" (within NREM). Never ask whether REM or N3 is harder to wake from.

SPEAKER NOTES ARE NOT SLIDE CONTENT (Jaxon, 2026-10-15): e.g. the s21 note "flat line ... brain death", the s22
note "eyes closed", the s9 note "memory consolidation" are never used. (Eyes closed -> alpha IS on slide s28 and
the s24 picture, so it may be keyed from those.)

EXCLUDED_SLIDES (never cited):
  1, 2            title, objectives
  4               five cartoon images ("What is Sleep?"), no content
  8, 11, 20       section title slides
  30, 31          resources, questions
"""

DECK = "CMS 1 Phases of Sleep - Shah Fallsv.pptx"
C = lambda n: "%s, Slide %d" % (DECK, n)
CS = lambda *ns: "%s, Slides %s" % (DECK, ", ".join(str(n) for n in ns))

IO_COMA = "Compare and contrast sleep and coma"
IO_SWS = "Compare and contrast slow-wave sleep and rapid eye movement sleep."
IO_FUNC = "Discuss the physiological functions of sleep."
IO_WAVES = "Differentiate between the waveforms of a normal EEG: alpha waves, beta waves, theta waves, delta waves."
IO_STAGES = "Compare and contrast characteristic changes in the EEG at different stages of wakefulness and sleep."
IOS = [IO_COMA, IO_SWS, IO_FUNC, IO_WAVES, IO_STAGES]

EXCLUDED_SLIDES = {1, 2, 4, 8, 11, 20, 30, 31}

SCOPE_BANNED = [
    r"\bstage 4\b|\bstage four\b|\bfourth stage\b|four (?:non-rapid|NREM|slow-wave) stages",
    r"\b1-3 (?:waves|cycles)|\b1 to 3 (?:waves|cycles)",
    r"brain death|flat ?line",
    r"memory consolidation",
    r"Lecturio|Guyton",
]

# Named findings in vignette stems carry their description in parentheses, taken from the deck.
NAMED = {
    "sleep spindle": "bursts",          # s27/s28: short spindle-shaped bursts / bursts of 12- to 14-Hz waves
    "k complex": "sharp",               # s28: negative sharp waves, followed by positive component
    "paradoxical sleep": "wakefulness", # s10: EEG patterns similar to those during wakefulness
}

REQUIRED = []
