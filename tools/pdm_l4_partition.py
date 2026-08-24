#!/usr/bin/env python3
"""Partition the PDM I Lecture 4 (Complete Blood Count) pool into two 30s.

House format is 2x30 per topic plus 5x60 masters per exam. MASTERS WAIT: Exam 1
covers Lectures 1-6 and Lab 1, and only Lectures 1-4 exist.

PROFESSOR REYNOLDS' NO-MATH RULE DOES NOT APPLY HERE, and that is the point of
writing this file separately rather than reusing hers. This is Professor Shah's
lecture and his objective (d) is literally "Calculate absolute white blood cell
counts". Pool B therefore contains worked arithmetic, and this script asserts
that the calculation questions EXIST rather than that they are absent.

THE DECK CONTRADICTS ITSELF ON THREE REFERENCE RANGES. The full reference table
appears twice, as a picture on slides 7 and 31, and disagrees with the
individual teaching slides:

    lymphocytes           table 25-33%          teaching slide 24-44%
    platelets             table 150,000-400,000 teaching slide 150,000-450,000
    red cell distribution table 11-15%          teaching slide 12-15%

A fourth set of numbers appears on the labelled smear on slide 15 (neutrophil
60-70%, lymphocyte 20-25%, monocyte 3-8%, eosinophil 2-4%, basophil 0.5-1%),
which is a borrowed textbook graphic and matches neither.

THE RULE: no question may hinge on a disputed value. Where the table and the
teaching slide agree -- white cells, hemoglobin, hematocrit, mean corpuscular
volume, mean corpuscular hemoglobin and its concentration, mean platelet volume,
neutrophils, eosinophils, monocytes -- the value is quizzed normally. Where they
disagree, the fact is not quizzed as a bare number. The guard below enforces it,
and the study guide carries a table of all four sets so the disagreement is
visible rather than hidden.

THE WORKED EXAMPLE ON SLIDE 21 IS MIS-PARENTHESISED. It prints
"ANC = 6,000 x (40 + 5/100) = 2,700"; that bracketing evaluates to 240,300. The
printed ANSWER of 2,700 is right and agrees with the formula image on slide 20,
so the slip is typographical. Questions use the formula that the printed answer
and the formula image agree on.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l4_pool_a import POOL_A
from pdm_l4_pool_b import POOL_B
from pdm_l4_pool_c import POOL_C
from pdm_l4_pool_d import POOL_D
from pdm_l4_lengthfix import FIXES

# D is APPENDED, never prepended: the length-fix keys are indices into A + B + C
# and prepending would silently retarget every one of them.
POOL = POOL_A + POOL_B + POOL_C + POOL_D

import pdm_l4_lengthfix as _LF
assert _LF.B == len(POOL_A), "lengthfix pool B offset is stale"
assert _LF.C == len(POOL_A) + len(POOL_B), "lengthfix pool C offset is stale"
assert _LF.D == len(POOL_A) + len(POOL_B) + len(POOL_C), "lengthfix pool D offset is stale"

for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

# ---- Rule 1: no question hinges on a value the deck disputes with itself ----
# Each entry is (label, regex of the disputed numbers). A question stem or a
# CORRECT answer carrying one of these is a question whose "right" answer
# depends on which slide the examiner was looking at.
_DISPUTED = [
    ("lymphocyte percentage",       r"\b(?:25\s*(?:to|-)\s*33|24\s*(?:to|-)\s*44)\s*(?:per cent|%)|"
                                    r"twenty-four to forty-four per cent|twenty-five to thirty-three per cent"),
    ("platelet upper limit",        r"\b4[05]0,000\b|four hundred (?:and fifty )?thousand"),
    ("red cell distribution width", r"\b1[12]\s*(?:to|-)\s*15\s*(?:per cent|%)|"
                                    r"(?:eleven|twelve) to fifteen per cent"),
]
_bad = []
for _q in POOL:
    _texts = [_q["q"], _q["opts"][_q["c"]][0]]
    for _label, _rx in _DISPUTED:
        if any(re.search(_rx, _t, re.I) for _t in _texts):
            _bad.append((_label, _q["q"][:60]))
assert not _bad, ("a question turns on a value the deck states two different ways -- "
                  "there is no single right answer to grade: %r" % _bad[:3])

# ---- Rule 2: the arithmetic objective is actually covered --------------------
# The inverse of Reynolds' guard. Objective (d) is "Calculate absolute white
# blood cell counts", so if the calculation questions ever disappear from the
# pool this build has stopped covering a syllabus objective.
_CALC = [q for q in POOL if re.search(r"what is the absolute neutrophil count", q["q"], re.I)]
assert len(_CALC) >= 3, ("objective (d) is a CALCULATION objective and needs worked "
                         "examples -- found %d" % len(_CALC))

# ---- Rule 3: picture-only facts are labelled as such ------------------------
# Slides 7, 10, 14, 16, 17, 20, 21, 31, 39, 47, 52, 54, 55, 57, 63, 69, 71 and
# 72 carry content that is in a picture and not in the extracted text. Anything
# sourced from one must say "(image only)" or "(speaker notes)" in its citation,
# so a reader can tell why the fact is not in their copy of the slide text.
# NOTE slide 21 is deliberately NOT in this set. It carries BOTH -- its text has
# the worked absolute-neutrophil-count example, while its neutropenia severity
# table is a picture. A blanket rule on 21 fired on the worked example, which is
# genuinely in the slide text. The table's questions cite it as image-only.
_PICTURE_ONLY = {39, 63, 71, 72}
_unlabelled = [q["q"] for q in POOL
               if any(q["cite"].strip().endswith("Slide %d" % n) for n in _PICTURE_ONLY)]
assert not _unlabelled, ("cites a picture-only slide without saying so -- the reader "
                         "will not find this in the slide text: %r" % _unlabelled[:2])

# ---- every question carries an explicit fact slot ---------------------------
SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260824 + 4)
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
    lumpy = sum(max(0, n - 6) for n in ios.values())
    lumpy_t = sum(max(0, n - 5) for n in tops.values())
    lumpy_s = sum(max(0, n - 8) for n in slots.values())
    return (missing_io * 30 + missing_topic * 8 + lumpy * 3 + lumpy_t * 2
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
    print("Shah rule checks: no disputed-value questions OK, %d calculation questions, picture-only slides labelled OK" % len(_CALC))
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best, idx = None, list(range(len(POOL)))
    for _ in range(30000):
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
        ios = Counter(q["io"] for q in s)
        print("%s  n=%d" % (name, len(s)))
        print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
        print("   length-gameable: %.1f%%" % gameable_pct(s))
        print("   objectives: %d of %d   topics: %d of %d   slots: %d"
              % (len(ios), len(ALL_IOS), len(set(q["topic"] for q in s)), len(ALL_TOPICS),
                 len(set(q["slot"] for q in s))))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "pdm_l4_sets.json"), "w"), ensure_ascii=False, indent=1)
    print("wrote pdm_l4_sets.json")
