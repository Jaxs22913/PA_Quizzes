#!/usr/bin/env python3
"""Partition CMS I Lecture 9 Set 1 (Pre-malignant and Malignant Cutaneous Lesions) into two 30s.

CMS format per [[cms_exam_spec]]: Set 1 is 2 x 30 on the instructional
objectives, Set 2 is a separate 2 x 30 of vignettes. This builds Set 1.

THE SLIDE IS AUTHORITATIVE -- Jaquith's deck again, so every fact comes from the
PowerPoint rather than from any recording.

LENGTH BIAS. Raw rates fell across the five pools as the discipline improved:
A 71%, B 31%, C 15%, D 20%, E 56%. Pool A was written with enumerated-list
answers against one-clause distractors and needed 36 padding edits afterwards;
the later pools were written to the answer's shape from the start. Pool E rose
again because its content is four diseases compared side by side, which is the
compare-and-contrast shape that always inflates the rate. All five finish at 0%.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_l9_pool_a import POOL_A
from cms_l9_pool_b import POOL_B
from cms_l9_pool_c import POOL_C
from cms_l9_pool_d import POOL_D
from cms_l9_pool_e import POOL_E
from cms_l9_pool_f import POOL_F
from cms_l9_pool_g import POOL_G
from cms_l9_pool_h import POOL_H
from cms_l9_h_lengthfix import FIXES as H_FIXES
from cms_l9_g_lengthfix import FIXES as G_FIXES

# Pool G is APPENDED (never prepended) so the G length-fix indices, which are
# offsets into POOL_G itself, stay independent of everything before it.
for (_gi, _oi), _txt in G_FIXES.items():
    assert _oi != POOL_G[_gi]["c"], "pool G length fix %d/%d targets the CORRECT option" % (_gi, _oi)
    POOL_G[_gi]["opts"][_oi][0] = _txt

for (_hi, _oi), _txt in H_FIXES.items():
    assert _oi != POOL_H[_hi]["c"], "pool H length fix %d/%d targets the CORRECT option" % (_hi, _oi)
    POOL_H[_hi]["opts"][_oi][0] = _txt

POOL = POOL_A + POOL_B + POOL_C + POOL_D + POOL_E + POOL_F + POOL_G + POOL_H

# CMS scope guard: Set 1 is objective-style, NOT vignettes. A stem that opens
# with a patient age and presentation belongs in Set 2, and mixing them would
# make the two sets indistinguishable.
import re as _re
_VIG = _re.compile(r"^A[n]? \d+[- ]year[- ]old|^A \d+[- ]month[- ]old", _re.I)
_v = [q["q"] for q in POOL if _VIG.search(q["q"])]
assert not _v, "vignette-style stem in the Set 1 pool: %r" % _v[:2]

# every question carries an explicit fact slot
SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260820)
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


# The two forms should be comparable. Without this the optimiser is indifferent
# to which form a slot lands in, and the back-half slots -- the ones the
# corrective pool exists to supply -- can pile into one paper.
BALANCED_SLOTS = ("avoid", "education", "complication", "referral", "escalation",
                  "initial test", "gold standard")


def slot_imbalance(s1, s2):
    pen = 0
    for name in BALANCED_SLOTS:
        a = sum(1 for q in s1 if q["slot"] == name)
        b = sum(1 for q in s2 if q["slot"] == name)
        if a + b >= 2:
            pen += abs(a - b) * 6        # split them
            if min(a, b) == 0:
                pen += 25                # and never leave a form with none
    return pen


def score(setqs):
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    missing_io = len(ALL_IOS - set(ios))
    missing_topic = len(ALL_TOPICS - set(tops))
    lumpy = sum(max(0, n - 5) for n in ios.values())
    lumpy_t = sum(max(0, n - 4) for n in tops.values())
    slots = Counter(q["slot"] for q in setqs)
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
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    print("scope guard: no vignette stems in Set 1; every question carries a slot")
    print()

    # ---- slot floors, checked BEFORE partitioning -------------------------
    # The standing rule for this class, and the step that was skipped the first
    # time round: a slot that is empty in the POOL can never be filled by any
    # choice the partitioner makes.
    _FLOORS = {"avoid": 3, "education": 3, "complication": 2, "referral": 2,
               "prognosis": 2, "initial test": 3, "gold standard": 2}
    _have = Counter(q["slot"] for q in POOL)
    _under = {k: (_have.get(k, 0), v) for k, v in _FLOORS.items() if _have.get(k, 0) < v}
    assert not _under, ("pool is under the slot floor before partitioning -- write the "
                        "questions, do not hope the draw finds them: %r" % _under)
    print("slot floors met before partitioning:",
          {k: _have.get(k, 0) for k in sorted(_FLOORS)})

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    # POOL F IS GUARANTEED A PLACE. Its questions cover content that exists only
    # as pictures -- the Clark level diagram, the Stages of Melanoma diagram and
    # the TNM staging table, all on slides whose text extracts as empty. A
    # student cannot pick that up by re-reading the deck, which is precisely why
    # it must not be left to a random 60-of-84 draw. On the first run it was:
    # the Clark questions were written and then sampled straight back out again.
    # POOL G IS GUARANTEED TOO, for a different reason. check_slot_coverage.py
    # --floors found Lecture 9 under floor on nine slots, `avoid` at ZERO: pools
    # A to F had covered what a lesion is and how it is treated, and thinned out
    # across what to avoid, what to tell the patient, and what goes wrong. Pool
    # G is written to those slots, so leaving it to a random draw would reopen
    # the gap it exists to close.
    # POOL H IS GUARANTEED TOO. In the 24 August lecture she said repeatedly
    # that she was going to set "how do you diagnose this?" questions -- "you
    # guys know that question for everyone for this lecture at least". Measured
    # against the pools, Lecture 9 had the THINNEST diagnostic-test coverage of
    # any lecture on the exam, 2 questions in 108. Pool H is written to exactly
    # the question type she named, so it must not be left to a random draw.
    must = [i for i, q in enumerate(POOL) if q in POOL_F or q in POOL_G or q in POOL_H]
    rest = [i for i in range(len(POOL)) if i not in set(must)]
    assert len(must) <= 60, "more guaranteed questions than places"

    # THE GUARANTEED QUESTIONS MUST BE SHUFFLED INTO THE SPLIT, NOT PREPENDED
    # TO IT. `chosen = must + rest` followed by chosen[:30] / chosen[30:] puts
    # every guaranteed question in SET 1 whenever there are fewer than thirty of
    # them -- which is exactly what happened: set 1 came out with avoid=5,
    # education=5, complication=4 and set 2 with avoid=0, education=1,
    # complication=0. A student who only ever took Quiz 2 would have got none of
    # the coverage the corrective pool exists to provide.
    best, idx = None, list(rest)
    for _ in range(30000):
        random.shuffle(idx)
        chosen = must + idx[:60 - len(must)]
        random.shuffle(chosen)
        s1 = [POOL[i] for i in chosen[:30]]
        s2 = [POOL[i] for i in chosen[30:]]
        total = score(s1) + score(s2) + slot_imbalance(s1, s2)
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
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   objectives: %d of %d   topics: %d of %d   slots: %d"
              % (len(ios), len(ALL_IOS), len(set(q["topic"] for q in s)), len(ALL_TOPICS),
                 len(set(q["slot"] for q in s))))
        print()

    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "cms_l9_set1.json"), "w"), ensure_ascii=False, indent=1)
    print("wrote cms_l9_set1.json")
