#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 8 pool into 2 x 30.

Diagnosing Infections (Dr. Fair, per the calendar row for 2026-09-18; the deck
names no lecturer, and its PAJ5200.* filename is the pattern of Dr. Fair's decks.
An earlier version of this line named the other Micro lecturer). 62 questions.

OBJECTIVE COVERAGE IS NOT MEANINGFUL FOR THIS LECTURE, unlike Lectures 5 and 7.
The deck's instructional objective slide reproduces the COURSE-wide list --
common infectious agents, microbial physiology, mechanisms of disease,
epidemiology, antimicrobial action and resistance, treatment strategies,
prevention -- none of which is what the lecture actually teaches. The lecture is
a survey of DIAGNOSTIC METHODS, so 58 of the 62 questions tag to objective 1 by
default. The objective count is still printed, but the real organizing axis is
the phenotypic / genotypic / immunological split carried in each question's
topic field, and the selection is spread across that instead.

Four options and the class's existing shape. Length bias by selection; answer
position by ROTATION. Carries the house 60-character explanation guard.
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l8_pool_a import POOL_A

POOL = POOL_A
random.seed(20260920)
NOPT = 4


def longest_is_correct(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == q["c"] and (tl - rn) >= 8 and tl >= rn * 1.18


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_IOS = set(q["io"] for q in POOL)


def score(qs):
    ios = Counter(q["io"] for q in qs)
    missing = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - 7) for n in ios.values())
    return missing * 25 + lumpy * 3 + gameable_pct(qs) * 2.0


def rotate(qs):
    targets = [i % NOPT for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % NOPT
        q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
        q["c"] = t
    return qs


def validate(pool):
    bad = []
    for i, q in enumerate(pool):
        if len(q["opts"]) != NOPT: bad.append((i, "not four options"))
        if not (0 <= q["c"] < NOPT): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
        for o in q["opts"]:
            if len(o[1]) < 60:
                bad.append((i, "explanation under 60 chars: %r" % o[1][:40]))
        wrong = [o[1].strip() for j, o in enumerate(q["opts"]) if j != q["c"]]
        if len(set(wrong)) == 1:
            bad.append((i, "every wrong choice shares one explanation"))
        for o in q["opts"]:
            if not o[1].strip(): bad.append((i, "option unexplained"))
    return bad


if __name__ == "__main__":
    print("pool:", len(POOL))
    print("schema problems:", validate(POOL) or "none")
    print("objectives:", len(ALL_IOS))
    print("pool gameable: %.0f%%" % gameable_pct(POOL))
    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    best, idx = None, list(range(len(POOL)))
    for _ in range(40000):
        random.shuffle(idx)
        ch = idx[:60]
        total = score([POOL[i] for i in ch[:30]]) + score([POOL[i] for i in ch[30:]])
        if best is None or total < best[0]:
            best = (total, list(ch))

    ch = best[1]
    s1 = rotate([POOL[i] for i in ch[:30]])
    s2 = rotate([POOL[i] for i in ch[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions A/B/C/D %s  gameable %.0f%%  objectives %d/%d"
              % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)),
                 gameable_pct(s), len(set(q["io"] for q in s)), len(ALL_IOS)))

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "micro_l8_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote micro_l8_sets.json")
