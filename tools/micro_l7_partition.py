#!/usr/bin/env python3
"""Split and guard the Microbiology Lecture 7 pool into 2 x 30.

Disorders in Immunity (Dr. Webster). Pool A (67 questions) carries
objectives 1-4 -- the immunopathologies, the four hypersensitivities, allergy
diagnosis and management, and transfusion reactions. Pool B (added 2026-09-25)
carries objectives 5-9 -- transplantation and histocompatibility,
autoimmunity, primary against secondary immunodeficiency, carcinogenesis and
immunotherapy. Until pool B existed the two shipped sets covered only 4 of the
9 syllabus objectives.

The score now also punishes an objective with fewer than MIN_PER_IO questions
in a set, and the selector is swap-based local search rather than best-of-N
shuffles (the CMS I Exam 2 lesson): with nine objectives and a lopsided pool
(objective 2 alone has 40 questions) shuffling barely explores the space.

Four options and the class's existing shape, matching Lectures 1, 2 and 5.
Objective coverage and length bias by selection; answer position by ROTATION.

Adapted from the Lecture 5 driver, with the house 60-character explanation
guard added -- that driver predates it and checks only schema.
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from micro_l7_pool_a import POOL_A
from micro_l7_pool_b import POOL_B

POOL = POOL_A + POOL_B
MIN_PER_IO = 2
MAX_PER_IO = 5
# Objective 2 (the four hypersensitivities) spans slides 5-42, about half the
# deck, and its summary table (slide 9) is the one chart Dr. Webster told the
# class to "pay attention to". It is allowed more room than the others.
CAP = {"2": 7}
random.seed(20260920)
NOPT = 4


def longest_is_correct(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == q["c"] and (tl - rn) >= 8 and tl >= rn * 1.18


def uniquely_longest(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    return s[0][1] == q["c"] and s[0][0] > s[1][0]


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_IOS = set(q["io"] for q in POOL)
IO2_KEY = [io for io in ALL_IOS if io.startswith("2 ")][0]


def score(qs):
    ios = Counter(q["io"] for q in qs)
    missing = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - CAP.get(io.split(' ')[0], MAX_PER_IO)) for io, n in ios.items())
    thin = sum(max(0, MIN_PER_IO - ios.get(io, 0)) for io in ALL_IOS)
    thin += max(0, 6 - ios.get(IO2_KEY, 0))       # want objective 2 near its cap
    longest = 100.0 * sum(map(uniquely_longest, qs)) / len(qs)
    # keep the key the longest option in no more than ~30% of a set
    return (missing * 25 + thin * 10 + lumpy * 3 + gameable_pct(qs) * 2.0
            + max(0.0, longest - 30.0) * 1.0)


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
    probs = validate(POOL)
    print("schema problems:", probs or "none")
    assert not probs, "fix the pool before partitioning"
    print("objectives:", len(ALL_IOS))
    print("pool gameable: %.0f%%" % gameable_pct(POOL))
    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    def total(ch):
        return score([POOL[i] for i in ch[:30]]) + score([POOL[i] for i in ch[30:]])

    best, idx = None, list(range(len(POOL)))
    for _ in range(400):
        random.shuffle(idx)
        ch = idx[:60]
        t = total(ch)
        if best is None or t < best[0]:
            best = (t, list(ch))
    cur_t, cur = best
    for _ in range(60000):
        out = [i for i in range(len(POOL)) if i not in set(cur)]
        k = random.randrange(60)
        cand = list(cur)
        if random.random() < 0.5:
            cand[k] = random.choice(out)            # swap in an unused question
        else:
            j = random.randrange(60)                # move one across the sets
            cand[k], cand[j] = cand[j], cand[k]
        t = total(cand)
        if t <= cur_t:
            cur_t, cur = t, cand
    best = (cur_t, cur)
    print("selection score: %.1f" % cur_t)

    ch = best[1]
    s1 = rotate([POOL[i] for i in ch[:30]])
    s2 = rotate([POOL[i] for i in ch[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    assert not set(map(id, s1)) & set(map(id, s2)), "a question landed in both sets"
    for name, s in (("SET 1", s1), ("SET 2", s2)):
        per = Counter(q["io"].split(" ")[0] for q in s)
        assert set(q["io"] for q in s) == ALL_IOS, "%s misses an objective" % name
        print("   per objective:", " ".join("%s:%d" % (k, per[k]) for k in sorted(per)))
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions A/B/C/D %s  key uniquely longest %.0f%%  gameable %.0f%%  objectives %d/%d"
              % (name, len(s), "/".join(str(pos.get(i, 0)) for i in range(NOPT)),
                 100.0 * sum(map(uniquely_longest, s)) / len(s), gameable_pct(s), len(set(q["io"] for q in s)), len(ALL_IOS)))

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "micro_l7_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote micro_l7_sets.json")
