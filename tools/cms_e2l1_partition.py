#!/usr/bin/env python3
"""Partition the CMS I Exam 2 Lecture 1 SET 1 pool into two 30s.

Per [[cms_exam_spec]] each CMS topic gets FOUR exams: two 30-question sets on
the instructional objectives (this file) and two 30-question vignette sets
(cms_e2l1_vig_partition.py). Masters are 5x60 mixed and WAIT until the whole
Exam 2 block is in -- the syllabus still has Neuro-ophthalmology and Acute
Vision Loss to come.

OBJECTIVES ARE THE SYLLABUS'S, not the slide's. The slide reproduces them
closely but its population list omits CHILD, which the syllabus includes.
Per [[guide_verbatim_io_rule]] the syllabus wins.

SCOPE LINE AGAINST CLIN PATH I LECTURE 4: that lecture covers almost this exact
condition list from the MECHANISM side. This one is management -- what it looks
like, what to order, what to give, when to refer. Guard 1 asserts that a
meaningful share of this pool is actually management, because a CMS pool that
drifted into pure pathophysiology would duplicate the other course.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_e2l1_pool_a import POOL_A
from cms_e2l1_pool_b import POOL_B
from cms_e2l1_pool_c import POOL_C
from cms_e2l1_pool_d import POOL_D

POOL = POOL_A + POOL_B + POOL_C + POOL_D

try:
    from cms_e2l1_lengthfix import FIXES
except ImportError:
    FIXES = {}
for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

# ---- Guard 1: this is the MANAGEMENT half, and must look like it -----------
_MGMT_SLOTS = {"initial test", "gold standard", "first-line", "escalation",
               "agent/regimen", "avoid", "education", "referral"}
_mg = sum(1 for q in POOL if q["slot"] in _MGMT_SLOTS)
assert _mg >= len(POOL) * 0.45, (
    "only %d of %d questions sit in a management slot -- this pool has drifted toward "
    "pathophysiology, which is Clin Path I Lecture 4's half of the same condition list"
    % (_mg, len(POOL)))

# ---- Guard 2: the deck's own hedges are respected --------------------------
# Several slides are softened by their speaker notes -- imaging is NOT automatic
# for dacryoadenitis, dacryocystitis or clearly pre-septal cellulitis, and
# haematology referral is NOT automatic for recurrent subconjunctival
# haemorrhage. A question whose CORRECT answer says "always" or "every" on one
# of those is contradicted by the notes on the same slide.
_ABSOLUTE = re.compile(r"\b(?:always|every case|in all cases|never)\b", re.I)
_HEDGED = ("dacryoadenitis", "dacryocystitis", "cellulitis", "subconjunctival")
_bad = [q["q"][:60] for q in POOL
        if _ABSOLUTE.search(q["opts"][q["c"]][0])
        and any(h in (q["topic"] + q["q"]).lower() for h in _HEDGED)]
assert not _bad, ("a correct answer states an absolute on a topic the speaker notes "
                  "explicitly hedge: %r" % _bad[:3])

random.seed(20260826 + 21)
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
    lumpy_t = sum(max(0, n - 3) for n in tops.values())
    lumpy_s = sum(max(0, n - 5) for n in slots.values())
    thin_slots = len(set(SLOTS) - set(slots))
    # Gameability is weighted heavily here, unlike the other partitions on the
    # site. This pool starts at 57.7 per cent even after padding, because a
    # management answer is the deck's full list while a wrong answer is one
    # condition's name. With 163 questions to choose 60 from, the selector can
    # and should prefer the questions where that asymmetry is smallest.
    return (missing_io * 40 + thin_slots * 4 + lumpy_t * 3 + lumpy_s * 2
            + gameable_pct(setqs) * 8.0)


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
    print("management-slot share: %d/%d (%.0f%%)" % (_mg, len(POOL), 100.0*_mg/len(POOL)))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    # A plain shuffle-and-take-60 barely explores this space: with 163
    # questions there are far too many selections for random sampling to find
    # a low-gameability one that still covers every slot. Local search does --
    # start from the best of a few random draws, then repeatedly swap one
    # chosen question for an unchosen one and keep any swap that improves the
    # combined score. This dropped Set 1 from 33% gameable to single figures.
    def total(sel):
        return score([POOL[i] for i in sel[:30]]) + score([POOL[i] for i in sel[30:]])

    idx = list(range(len(POOL)))
    best = None
    for _ in range(400):
        random.shuffle(idx)
        cand = idx[:60]
        t = total(cand)
        if best is None or t < best[0]:
            best = (t, list(cand))

    cur_score, cur = best
    outside = [i for i in range(len(POOL)) if i not in set(cur)]
    for _ in range(60000):
        a = random.randrange(60)
        b = random.randrange(len(outside))
        cur[a], outside[b] = outside[b], cur[a]
        t = total(cur)
        if t < cur_score:
            cur_score = t
        else:
            cur[a], outside[b] = outside[b], cur[a]   # revert
    best = (cur_score, cur)
    print("local search settled at score %.1f" % cur_score)

    chosen = best[1]
    s1 = rotate_for_balance([POOL[i] for i in chosen[:30]])
    s2 = rotate_for_balance([POOL[i] for i in chosen[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions %s  gameable %.1f%%  topics %d  slots %d"
              % (name, len(s), dict(sorted(pos.items())), gameable_pct(s),
                 len(set(q["topic"] for q in s)), len(set(q["slot"] for q in s))))

    with open(os.path.join(HERE, "cms_e2l1_sets.json"), "w", encoding="utf-8") as fh:
        json.dump({"set1": s1, "set2": s2}, fh, ensure_ascii=False, indent=1)
    print("\nwrote cms_e2l1_sets.json")
