# -*- coding: utf-8 -*-
"""Propose a lead-in question for a stem that has none.

A stem that states a scenario and stops is not a question -- the student has to
reverse-engineer what is being asked from the options. 364 stems written on
2026-09-08 shipped that way (the ENT masters and the L18/L19 vignettes); the
L15-L17 pools and the L18/L19 objective pools were fine, so the regression is
specific to how the vignettes were authored, not to the pipeline.

THIS ONLY PROPOSES. The lead-in decides which option is correct
([[vignette_question_style]]), so a wrong one silently breaks the item. Every
proposal is reviewed against its own options before it is applied, and anything
this cannot classify with confidence is left for hand-authoring rather than
given a vague catch-all.
"""
import re

def _txt(s):
    return re.sub(r"<[^>]+>", "", s).strip()

DRUG = re.compile(r"(?i)\b(cillin|micin|mycin|oxacin|azole|cycline|sone|olol|"
                  r"steroid|antibiotic|antifungal|antiviral|drops?|ointment)\b")
TESTW = re.compile(r"(?i)\b(computed tomograph|magnetic resonance|ultrasound|"
                   r"radiograph|x-ray|audiometr|tympanometr|biopsy|aspiration|"
                   r"culture|serolog|swab|endoscop|laryngoscop|titre|titer|"
                   r"assay|panel|screen|scan|imaging|polymerase)\b")
ACTION = re.compile(r"(?i)^(refer|admit|start|give|prescribe|observe|reassure|"
                    r"arrange|order|perform|obtain|remove|drain|incise|irrigate|"
                    r"discharge|treat|begin|continue|stop|withhold|schedule|"
                    r"apply|advise|counsel|educate|explain|tell|instruct|avoid|"
                    r"keep|repeat|consult|transfer|secure|call|place|insert)\b")
FINDING = re.compile(r"(?i)\b(weber|rinne|lateralis|lateraliz|air conduction|"
                     r"bone conduction|nystagmus|type [abc] tympanogram|"
                     r"decibel|hertz|notch|audiogram)\b")
ORGANISM = re.compile(r"(?i)\b(pseudomonas|staphylococc|streptococc|haemophilus|"
                      r"moraxella|candida|aspergillus|corynebacter|bartonella|"
                      r"mycobacter|epstein|virus|bacteri|fungal|treponema|"
                      r"toxoplasma|brucell|francisella|actinomyc)\b")

LEADINS = {
  "diagnosis":  "What is the most likely diagnosis?",
  "treatment":  "Which of the following is the most appropriate treatment?",
  "next_step":  "What is the most appropriate next step in management?",
  "test":       "Which investigation is most appropriate?",
  "finding":    "Which finding would be expected?",
  "organism":   "Which organism is most likely responsible?",
}

def classify(q):
    """Return (key, confidence) -- confidence 'high' is safe to apply after a
    read-through, 'low' means hand-author it."""
    opts = [_txt(o[0]) for o in q["opts"]]
    key  = opts[q["c"]]
    n    = len(opts)

    # A majority test decides: the option SET has to look like one kind of
    # answer, not just the key, or the distractors would not be parallel.
    def frac(rx):  return sum(bool(rx.search(o)) for o in opts) / n

    if frac(FINDING) >= 0.75:                       return "finding", "high"
    if frac(ORGANISM) >= 0.75:                      return "organism", "high"
    if frac(ACTION) >= 0.75:
        # "refer / admit / observe" is a management decision; a bare drug list
        # is a treatment choice. Both are actions, so split on the wording.
        if frac(DRUG) >= 0.5:                       return "treatment", "high"
        return "next_step", "high"
    if frac(TESTW) >= 0.75:                         return "test", "high"
    if frac(DRUG) >= 0.75:                          return "treatment", "high"
    # Short bare noun phrases with no verb read as disease names.
    noverb = sum(1 for o in opts if not ACTION.match(o) and len(o.split()) <= 8) / n
    if noverb >= 0.75:                              return "diagnosis", "low"
    return None, "low"
