#!/usr/bin/env python3
"""Partition the PDM I Lecture 5 (Chemistry Panels) pool into two 30s.

House format is 2x30 per topic plus 5x60 masters per exam. MASTERS STILL WAIT:
Exam 1 covers Lectures 1-6 and Lab 1, and Lecture 6 (Urinalysis) has not been
delivered.

REYNOLDS' RULES, AS THE 26 AUGUST RECORDING ACTUALLY STATES THEM
---------------------------------------------------------------
Her Lecture 1 rule was recorded as a flat "we're not gonna do math." Lecture 5
shows that was too blunt, and this script encodes the real shape of it.

  SHE EXPECTS THE ANION GAP TO BE CALCULATED.
      "you really quick and dirty, calculate your anion gap, and our normal
       range is 8 to 12"
  So this file asserts the worked gap questions EXIST. Deleting them would stop
  the build covering objective (f) the way she teaches it.

  SHE EXPLICITLY DOES NOT WANT THESE CALCULATED.
      glomerular filtration rate -- "I don't need you to calculate that or know
                                     that just yet, but know OF it"
      corrected sodium           -- done with "UpToDate, MedCalc, eCalc"
  Guard 2 below fires if a question asks for either.

  SHE NEVER MAKES THEM RECALL A REFERENCE RANGE.
      "the hard and fast memorize these numbers, we don't do that to you
       because it's gonna depend on the lab ... we ALWAYS give you reference
       ranges"
  This is why guard 3 exists and why the deck's internal disagreements do not
  need resolving.

THE DECK DISAGREES WITH ITS OWN FISHBONE IN THREE PLACES
--------------------------------------------------------
    bicarbonate   text slide 12  ~22-29     fishbone image  22-28 (and 22-26 in
                                                            the blood-gas column)
    glucose       text slide 13  ~70-99     fishbone image  70-120
                                 fasting
    blood urea    text slide 14  ~7-20      fishbone image  7-18
      nitrogen
Creatinine, 0.6-1.2, is the one that agrees.

Because she supplies ranges on the exam, NO QUESTION MAY TURN ON WHICH FIGURE
IS RIGHT -- there would be no single right answer to grade. Guard 3 enforces it.
The anion gap's 8-12 is NOT in this category: it appears once, she said it
aloud, and it is a calculated threshold rather than a laboratory reference
range.

THE FISHBONE IS AN IMAGE-ONLY SLIDE. Slide 4 extracts as completely empty and
carries the whole reference set; slide 3 is a decorative periodic table. Found
with tools/ocr_deck_images.py. Anything sourced from a picture says so in its
citation.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l5_pool_a import POOL_A
from pdm_l5_pool_b import POOL_B
from pdm_l5_pool_c import POOL_C
from pdm_l5_pool_d import POOL_D

POOL = POOL_A + POOL_B + POOL_C + POOL_D

try:
    from pdm_l5_lengthfix import FIXES
except ImportError:
    FIXES = {}

if FIXES:
    for (_qi, _oi), _txt in FIXES.items():
        _q = POOL[_qi]
        assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
        _q["opts"][_oi][0] = _txt

# ---- Guard 1: a number never appears without the scale that reads it --------
# Her stated rule: "I'm not going to just throw a random number at you and not
# give you context of whether that's high or low." A stem quoting a value must
# either say which direction it is, or supply the range, or ask for a
# calculation whose scale is in the options.
_NUM_STEM = re.compile(r"\b\d[\d,\.]*\s*(?:milli|mg|mEq|mmol|g/|per cent|%)", re.I)
_SCALE = re.compile(r"\bnormal\b|\brange\b|\braised\b|\brises\b|\bhigh\b|\blow\b|\bfall\b|"
                    r"\bfallen\b|\babove\b|\bbelow\b|\bover\b|\bunder\b|anion gap|ratio", re.I)
_ctx = [q["q"][:70] for q in POOL
        if _NUM_STEM.search(q["q"]) and not _SCALE.search(q["q"] + " " + q["opts"][q["c"]][0])]
assert not _ctx, ("a value appears with no scale to read it against -- her rule 1: %r" % _ctx[:3])

# ---- Guard 2: the two calculations she ruled out are never asked for --------
_NO_CALC = [
    ("glomerular filtration rate",
     r"calculat\w*[^.?]{0,60}(?:filtration rate|\bGFR\b)|"
     r"(?:filtration rate|\bGFR\b)[^.?]{0,40}\bcalculat"),
    ("corrected sodium",
     r"calculat\w*[^.?]{0,60}corrected sodium|corrected sodium[^.?]{0,40}\bcalculat|"
     r"what is the corrected sodium"),
]
_asked = []
for _q in POOL:
    for _label, _rx in _NO_CALC:
        if re.search(_rx, _q["q"], re.I):
            _asked.append((_label, _q["q"][:60]))
assert not _asked, ("asks the student to compute something she said she would not "
                    "make them compute: %r" % _asked[:3])

# ---- Guard 3: no question turns on a range the deck states two ways ---------
# Each is (label, regex). A stem or a CORRECT answer carrying one of these is a
# question whose right answer depends on which slide the examiner read.
_DISPUTED = [
    ("bicarbonate range", r"\b22\s*(?:to|-|–)\s*(?:26|28|29)\b|"
                          r"twenty-two to (?:twenty-six|twenty-eight|twenty-nine)"),
    ("glucose range",     r"\b70\s*(?:to|-|–)\s*(?:99|120)\b|"
                          r"seventy to (?:ninety-nine|one hundred and twenty)"),
    ("urea nitrogen range", r"\b7\s*(?:to|-|–)\s*(?:18|20)\b|seven to (?:eighteen|twenty)"),
]
_bad = []
for _q in POOL:
    _texts = [_q["q"], _q["opts"][_q["c"]][0]]
    for _label, _rx in _DISPUTED:
        if any(re.search(_rx, _t, re.I) for _t in _texts):
            _bad.append((_label, _q["q"][:60]))
assert not _bad, ("turns on a range the deck states two different ways, so there is no "
                  "single right answer to grade: %r" % _bad[:3])

# ---- Guard 4: the anion gap arithmetic she DOES want is actually present ----
# The inverse guard. If these ever vanish the build has stopped teaching the
# objective the way she teaches it.
_GAP_CALC = [q for q in POOL
             if re.search(r"what is the anion gap|how should the anion gap be read", q["q"], re.I)]
assert len(_GAP_CALC) >= 2, ("she expects the anion gap to be calculated -- worked "
                             "examples must exist, found %d" % len(_GAP_CALC))

# ---- every question carries an explicit fact slot ---------------------------
SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260826 + 5)
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (top_len, top_i), (runner, _) = lens[0], lens[1]
    if top_i != q["c"]:
        return False
    return (top_len - runner) >= MARGIN_CHARS and top_len >= runner * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_IOS = set(q["io"] for q in POOL)
ALL_TOPICS = set(q["topic"] for q in POOL)


def score(setqs):
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    missing_io = len(ALL_IOS - set(ios))
    missing_topic = len(ALL_TOPICS - set(tops))
    lumpy = sum(max(0, n - 5) for n in ios.values())
    lumpy_t = sum(max(0, n - 4) for n in tops.values())
    lumpy_s = sum(max(0, n - 8) for n in slots.values())
    return (missing_io * 30 + missing_topic * 6 + lumpy * 3 + lumpy_t * 2
            + lumpy_s * 2 + gameable_pct(setqs) * 1.2)


def rotate_for_balance(qs):
    targets = [i % 4 for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % 4
        q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
        q["c"] = t
    return qs


def validate(pool):
    bad = []
    for i, q in enumerate(pool):
        if len(q["opts"]) != 4: bad.append((i, "not 4 options"))
        if not (0 <= q["c"] <= 3): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != 4: bad.append((i, "duplicate option text"))
        for o in q["opts"]:
            if not o[1].strip(): bad.append((i, "option missing explanation"))
    return bad


if __name__ == "__main__":
    print("pool size:", len(POOL))
    print("schema problems:", validate(POOL) or "none")
    print("objectives:", len(ALL_IOS), " topics:", len(ALL_TOPICS),
          " slots:", len(set(q["slot"] for q in POOL)))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("Reynolds checks: number-context OK, no-GFR/corrected-sodium-math OK, "
          "disputed ranges unused OK, %d anion-gap calculations present" % len(_GAP_CALC))
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best = None
    idx = list(range(len(POOL)))
    for _ in range(40000):
        random.shuffle(idx)
        chosen = idx[:60]
        s1 = [POOL[i] for i in chosen[:30]]
        s2 = [POOL[i] for i in chosen[30:]]
        total = score(s1) + score(s2)
        if best is None or total < best[0]:
            best = (total, list(chosen))

    chosen = best[1]
    s1 = rotate_for_balance([POOL[i] for i in chosen[:30]])
    s2 = rotate_for_balance([POOL[i] for i in chosen[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  answer positions %s  gameable %.1f%%  objectives %d  topics %d"
              % (name, len(s), dict(sorted(pos.items())), gameable_pct(s),
                 len(set(q["io"] for q in s)), len(set(q["topic"] for q in s))))

    out = {"set1": s1, "set2": s2}
    with open(os.path.join(HERE, "pdm_l5_sets.json"), "w", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    print("\nwrote pdm_l5_sets.json")
