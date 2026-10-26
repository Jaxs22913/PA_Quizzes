# -*- coding: utf-8 -*-
"""Rhythm Strips and Rhythm Vignettes scope -- CMS I Exam 5, Lectures 29 and 30 together.

Read by cms_e5_partition.py (key "rhyvig") and imported by the three cms_e5rhy_vig_* pools.
Not a question bank.

WHY THIS SET EXISTS (2026-10-25): the course emailed the class that Exam 5 is 70 questions
"including a couple of EKG tracings. A significantly greater number of questions will describe
cardiac rhythms within clinical vignettes", asking for the diagnosis or underlying etiology, the
diagnostic test, or the next step in management. So this set mixes real rhythm strips from the two
arrhythmia decks with cases whose stems DESCRIBE the rhythm in words (rate, regularity, P waves and
their relation to the QRS, PR interval, QRS width).

GROUNDING: the two arrhythmia decks only, slides as visible (speaker notes never count). Every cap,
exclusion and contested-slide decision already made in cms_e5l29_scope.py and cms_e5l30_scope.py is
inherited here unchanged: this module imports both and merges them.

  IOS      the union of the two lectures' verbatim syllabus objectives (the Lecture 29 module already
           carries the Lecture 30 objective for junctional rhythm, so the union has four strings).
  DECKS    both deck file names; a question cites ONE deck, "<deck>, Slide N".
  EXCLUDED_BY_DECK   each deck's own excluded slides (the numbers differ between decks).
  SCOPE_BANNED       both lists, EXCEPT Lecture 30's blanket atropine ban: atropine IS keyed for
           symptomatic sinus bradycardia (Lecture 29, slide 13). It stays banned next to Mobitz II
           or complete block, which is what Lecture 30 capped.
  NAMED    both glossaries.

STRIPS: pictures cropped from the decks' slide images, saved as cms-e5-images/rhythm-strip-NN.jpg
(names never state the rhythm). Every caption, title or label naming the rhythm was cropped off; a
strip whose labels could not be removed cleanly (the flutter strip with "F" marks, the junctional
caption diagrams, the watermarked first-degree block and atrial premature beat pictures) was not
used. The atrial premature beat strip on Arrhythmias I slide 57 (unlabeled) was dropped because its
early beat is not clearly visible (a pause after a P wave hidden in a T wave), so its answer would
not be defensible.

  01 Arrhythmias I s12   sinus bradycardia            11 Arrhythmias II s8   Mobitz type I
  02 Arrhythmias I s15   sinus tachycardia            12 Arrhythmias II s11  Mobitz type II
  03 Arrhythmias I s19   tachy-brady (sick sinus)     13 Arrhythmias II s16  third-degree block
  04 Arrhythmias I s29   multifocal atrial tachy      14 Arrhythmias II s25  left bundle branch block
  05 Arrhythmias I s35   pre-excitation (delta wave)  15 Arrhythmias II s41  monomorphic VT
  06 Arrhythmias I s39   nodal reentry (narrow, reg)  16 Arrhythmias II s41  polymorphic VT
  07 Arrhythmias I s43   atrial flutter               17 Arrhythmias II s41  torsades de pointes
  08 Arrhythmias I s47   atrial fibrillation          18 Arrhythmias II s49  coarse VF
  09 Arrhythmias I s52   pre-excited atrial fib       19 Arrhythmias II s53  asystole
  10 Arrhythmias I s63   junctional rhythm

Each strip is used by ONE question in the pool, so a strip can never appear twice in a form.
REQUIRED below puts at least 8 strip questions in each form, and each of the stressed decision points.
"""
import os, re
import cms_e5l29_scope as L29
import cms_e5l30_scope as L30

DECK1 = L29.DECK                 # "arrhythmias I - Elwaya-2.pptx"
DECK2 = L30.DECK                 # "Arrhythmias II - Elwaya  (1).pptx" (two spaces)
DECKS = (DECK1, DECK2)
DECK = DECK1                     # the partition's single-deck fallback; DECKS is what it checks
C1 = lambda n: "%s, Slide %d" % (DECK1, n)
C2 = lambda n: "%s, Slide %d" % (DECK2, n)

IOS = []
for _io in list(L29.IOS) + list(L30.IOS):
    if _io not in IOS:
        IOS.append(_io)
IO_SV = L29.IO_A                 # supraventricular rhythms
IO_SV_POP = L29.IO_POP
IO_V = L30.IO_A                  # blocks, ventricular rhythms, junctional rhythm
IO_V_POP = L30.IO_POP
assert L29.IO_L30 == L30.IO_A and len(IOS) == 4

EXCLUDED_BY_DECK = {DECK1: set(L29.EXCLUDED_SLIDES), DECK2: set(L30.EXCLUDED_SLIDES)}
EXCLUDED_SLIDES = set()          # per deck instead (EXCLUDED_BY_DECK)

SCOPE_BANNED = list(L29.SCOPE_BANNED) + [p for p in L30.SCOPE_BANNED if p != r"\batropine\b"] + [
    r"atropine[^?]{0,120}(?:mobitz type ii|third-degree|complete (?:heart |atrioventricular )?block)",
    r"(?:mobitz type ii|third-degree|complete (?:heart |atrioventricular )?block)[^?]{0,120}atropine",
]

NAMED = dict(L29.NAMED)
NAMED.update(L30.NAMED)

STRIP = r"\bis shown\b"     # every picture stem says its strip or tracing "is shown"
# (label, stem regex, key regex, minimum per form): at least 8 strips per form, plus the decision
# points the lecturer stressed (stable narrow tachycardia -> vagal maneuver then adenosine; pacing
# for symptomatic bradycardia and high-grade block; defibrillation; torsades; the accessory pathway).
REQUIRED = [
    ("rhythm strip shown", STRIP, r".", 8),
    ("stable narrow tachycardia: vagal maneuver, then adenosine", r"narrow", r"^(?:Vagal maneuver|Adenosine)$", 1),
    ("bradycardia or block: pacing", r".", r"pac(?:ing|emaker)", 1),
    ("defibrillation", r".", r"^Defibrillation$", 1),
    ("torsades: magnesium, or lidocaine as the usable antiarrhythmic", r"twist|QT", r"^(?:Intravenous magnesium|Lidocaine)$", 1),
    ("accessory pathway: procainamide or ablation", r".", r"procainamide|ablation of the pathway", 1),
]

IMG_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                       "Clinical Medicine and Surgery I Exam 5")


def check_strips(qs):
    """Every strip question shows a real file, says so in the stem, and never names its rhythm in
    the file name or the alt text; no strip is used twice in the pool module."""
    seen = set()
    for q in qs:
        shows = bool(re.search(STRIP, q["q"], re.I))
        assert shows == ("img" in q), "strip wording and img disagree: %r" % q["q"][:70]
        if "img" not in q:
            continue
        assert re.fullmatch(r"cms-e5-images/rhythm-strip-\d\d\.jpg", q["img"]), q["img"]
        assert os.path.exists(os.path.join(IMG_DIR, q["img"])), q["img"]
        assert q["img"] not in seen, "strip used twice: %s" % q["img"]
        seen.add(q["img"])
        assert q.get("alt") and re.fullmatch(r"Arrhythmias I{1,2}, slide \d+", q.get("slide", "")), q["img"]
        key = q["opts"][0][0].lower()
        assert key not in q["alt"].lower(), "alt text names the answer: %s" % q["img"]
    return seen
