#!/usr/bin/env python3
"""Partition the PDM I Lecture 6 (Urinalysis) pool into two 30s.

House format is 2x30 per topic. Lecture 6 is the LAST lecture of Exam 1, which
covers Lectures 1-6 and Lab 1; the 5x60 master forms wait on a decision about
how Lab 1 is folded in.

GOPAL'S OWN TESTING RULE, 1 September recording, 15:08-15:43
------------------------------------------------------------
    "for testing purposes, I would like you to know what a normal urinalysis
     involves ... It's important to know that we should not find nitrites. We
     should not find ketones. We should not find glucose. So I do want you to
     know that. I'm not asking that you memorize ranges, okay? But I do want
     you to know if there should just be none present at all. But for testing
     purposes, if there's a range involved, it'll be provided for you."

So the split is:
  FAIR COLD  -- which analytes are normally negative, and which is reported as
                a value rather than as positive/negative.
  NOT FAIR   -- recalling a laboratory reference range. No question here asks
                for the normal pH range, the normal specific gravity range, or
                the normal protein figures, even though all three are printed
                on slide 14. Guard 2 enforces it.

This sits on top of Reynolds' rule for the whole course (a number never appears
without the scale that reads it, and nothing is calculated), which Gopal's
wording restates rather than contradicts.

TWO DOCUMENTED EXCEPTIONS, both definitional thresholds rather than laboratory
reference ranges -- the same category as Lecture 5's anion gap:
  * three red cells, which is what the term microscopic hematuria MEANS
  * four hours between voids, a procedural interval for the nitrite conversion
Guard 2 allows exactly these two and nothing else.

DECK QUIRKS THIS BUILD HAD TO WORK AROUND
-----------------------------------------
  * NO SPEAKER NOTES AT ALL. 35 notes slides, every one an empty placeholder.
    Lectures 1-5 leaned on notes heavily; here the recording is the only
    source of spoken emphasis.
  * SLIDE 30 IS A TABLE in a graphic frame. Shape-text extraction returns two
    stray lines and silently loses a four-mechanism breakdown of proteinuria.
  * SLIDE 23's picture carries the three-red-cell threshold; the shape text on
    that slide breaks off before it.
  * SLIDE 36 IS AN UNFINISHED ANSWER SLIDE -- a dipstick chart with three
    unlabelled "x" shapes. Which analytes they mark was resolved from their
    coordinates, and agrees with what she read out at 49:12.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l6_pool_a import POOL_A
from pdm_l6_pool_b import POOL_B
from pdm_l6_pool_c import POOL_C
from pdm_l6_pool_d import POOL_D
from pdm_l6_pool_e import POOL_E
from _selfcontain_rx import RX as CITES_SOURCE

POOL = POOL_A + POOL_B + POOL_C + POOL_D + POOL_E

# ---- length-bias fixes, applied before anything is measured ----------------
# Shorten the KEY, never pad the distractors (Jaxon, 2026-08-30). The handful
# of SPECIFIC entries are the documented exception: where the key is a list and
# the list is the content, one distractor is made more specific instead.
try:
    from pdm_l6_lengthfix import KEYS as _LKEYS, SPECIFIC as _LSPEC
except ImportError:
    _LKEYS, _LSPEC = {}, {}
for _i, _txt in _LKEYS.items():
    _q = POOL[_i]
    assert len(_txt) < len(_q["opts"][_q["c"]][0]), "length fix %d is not shorter" % _i
    _q["opts"][_q["c"]][0] = _txt
for (_qi, _oi), _txt in _LSPEC.items():
    assert _oi != POOL[_qi]["c"], "SPECIFIC fix %d/%d targets the CORRECT option" % (_qi, _oi)
    POOL[_qi]["opts"][_oi][0] = _txt

ALL_IOS = set(q["io"] for q in POOL)
ALL_TOPICS = set(q["topic"] for q in POOL)

# ---- Guard 1: correct answer authored first, before any rotation -----------
assert all(q["c"] == 0 for q in POOL), "a question was authored with c != 0"

# ---- Guard 2: no question requires a laboratory reference range from memory -
# A stem may quote a value if it also supplies the scale; and the two
# definitional thresholds above are allowed by name.
_ALLOWED = re.compile(r"microscopic h[ae]maturia|between voids|four hours", re.I)
_NUM = re.compile(r"\b\d[\d,\.]*\s*(?:mg|milligram|mEq|mmol|g/|per cent|%|hours?)", re.I)
_SCALE = re.compile(r"\bnormal\b|\brange\b|\braised\b|\bhigh\b|\blow\b|\babove\b|"
                    r"\bbelow\b|\bover\b|\bunder\b|\bmore than\b|\bnegative\b", re.I)
_bare = [q["q"][:70] for q in POOL
         if _NUM.search(q["q"]) and not _SCALE.search(q["q"]) and not _ALLOWED.search(q["q"])]
assert not _bare, ("a value appears with no scale to read it against: %r" % _bare[:3])

_RANGE_RECALL = re.compile(r"what is the normal (range|value|pH|specific gravity)"
                           r"|normal range (for|of)", re.I)
_recall = [q["q"][:70] for q in POOL if _RANGE_RECALL.search(q["q"])]
assert not _recall, ("a question asks a reference range to be recalled: %r" % _recall)

# ---- Guard 3: nothing asks the student to calculate ------------------------
_CALC = re.compile(r"\bcalculat|\bcompute(?!d tomography)|\bwork out\b|\bwhat is the sum\b", re.I)
_calc = [q["q"][:70] for q in POOL if _CALC.search(q["q"])]
assert not _calc, ("a question asks for a calculation, against the course rule: %r" % _calc)

# ---- Guard 4: every question stands on its own -----------------------------
# No stem, option or explanation may send the reader back to the lecture, the
# deck or the professor. Same detector as tools/check_self_contained.py.
_cited = []
for q in POOL:
    for t in [q["q"]] + [o[0] for o in q["opts"]] + [o[1] for o in q["opts"]]:
        if CITES_SOURCE.search(t):
            _cited.append(t[:80])
assert not _cited, ("text cites its own source: %r" % _cited[:3])

# ---- Guard 5: the three objectives are all really covered ------------------
assert len(ALL_IOS) == 3, "expected objectives a, b and c, got %d" % len(ALL_IOS)
_bio = [q for q in POOL if q["io"].startswith("b ")]
assert len(_bio) >= 12, "objective b is thin: %d questions" % len(_bio)


def longest_is_correct(q):
    L = [len(o[0]) for o in q["opts"]]
    c = L[q["c"]]
    others = [x for i, x in enumerate(L) if i != q["c"]]
    return c > max(others) and c - max(others) >= 8 and c >= max(others) * 1.18


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


def score(setqs):
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    missing_io = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - 14) for n in ios.values())
    lumpy_t = sum(max(0, n - 4) for n in tops.values())
    lumpy_s = sum(max(0, n - 8) for n in slots.values())
    return (missing_io * 40 + lumpy * 3 + lumpy_t * 2 + lumpy_s * 2
            + gameable_pct(setqs) * 1.2)


def rotate_for_balance(qs):
    """Spread the correct answers across A-D. Authoring put them all at 0."""
    targets = [0, 1, 2, 3] * ((len(qs) // 4) + 1)
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        opts, cur = q["opts"], q["c"]
        opts[cur], opts[t] = opts[t], opts[cur]
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
    random.seed(20260901)
    print("pool size:", len(POOL))
    print("schema problems:", validate(POOL) or "none")
    print("objectives:", len(ALL_IOS), " topics:", len(ALL_TOPICS),
          " slots:", len(set(q["slot"] for q in POOL)))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("guards: range-recall OK, no-calculation OK, self-contained OK, "
          "objective b has %d questions" % len(_bio))
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

    with open(os.path.join(HERE, "pdm_l6_sets.json"), "w", encoding="utf-8") as fh:
        json.dump({"set1": s1, "set2": s2}, fh, ensure_ascii=False, indent=1)
    print("\nwrote pdm_l6_sets.json")
