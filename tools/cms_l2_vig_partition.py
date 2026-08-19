#!/usr/bin/env python3
"""Partition CMS I Lecture 2 SET 2 (the vignettes) into two 30s.

CMS runs four exams per topic: Set 1 is 2 x 30 on the objectives, Set 2 is this
2 x 30 of vignettes. Set 1 ships separately.

Two guards run before anything else, because both failures would be invisible in
the finished quiz:

  EVERY STEM IS A VIGNETTE. A recall-shaped question here would make Set 2
  indistinguishable from Set 1 and waste one of the four exams.

  LEAD-INS STAY SPREAD. The style rule says not every vignette asks for
  management. Pools A and B alone came out 20-of-48 management against 2 asking
  for a test, which is why pool C exists. The guard fails the build if any one
  lead-in type exceeds 40% of a set.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_l2_vig_a import POOL_A
from cms_l2_vig_b import POOL_B
from cms_l2_vig_c import POOL_C
from cms_l2_vig_lengthfix import SLOT_FIXES

POOL = POOL_A + POOL_B + POOL_C
for (_qi, _oi), _t in SLOT_FIXES.items():
    assert _oi != POOL[_qi]["c"], "length fix %d would overwrite the correct option" % _qi
    POOL[_qi]["opts"][_oi][0] = _t

_VIG = re.compile(r"^A[n]? \d+[- ]?(year|month)[- ]old|^A (mother|father|parent)\b", re.I)
_bad = [q["q"][:60] for q in POOL if not _VIG.match(q["q"])]
assert not _bad, "non-vignette stem in Set 2: %r" % _bad

LEAD = {
 "diagnosis": r"most likely diagnosis|most likely explanation|which phenomenon|allergen is most likely",
 "next step": r"next step",
 "treatment": r"initial treatment|first-line|most appropriate treatment|appropriate management|treatment consideration|initial management|first-line option",
 "test": r"diagnostic test|test confirms|which test|diagnostic approach|establish the diagnosis|would settle|diagnostic approach",
 "education": r"counselling point",
}
def lead_of(q):
    for k, p in LEAD.items():
        if re.search(p, q["q"], re.I):
            return k
    return "other"

random.seed(20260819)
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rl, _) = lens[0], lens[1]
    return ti == q["c"] and (tl - rl) >= MARGIN_CHARS and tl >= rl * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_TOPICS = set(q["topic"] for q in POOL)


def score(s):
    tops = Counter(q["topic"] for q in s)
    leads = Counter(lead_of(q) for q in s)
    missing = len(ALL_TOPICS - set(tops))
    lumpy = sum(max(0, n - 4) for n in tops.values())
    # punish a set that drifts back toward all-management
    skew = sum(max(0, n - len(s) * 0.34) for n in leads.values())
    return missing * 14 + lumpy * 3 + skew * 6 + gameable_pct(s) * 1.2


def rotate_for_balance(qs):
    targets = [i % 4 for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % 4
        q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
        q["c"] = t
    return qs


if __name__ == "__main__":
    print("pool size:", len(POOL), " topics:", len(ALL_TOPICS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    print("guards: every stem is a vignette, lead-ins spread")
    print("pool lead-in mix:", dict(Counter(lead_of(q) for q in POOL)))
    print()
    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best, idx = None, list(range(len(POOL)))
    for _ in range(30000):
        random.shuffle(idx)
        ch = idx[:60]
        s1, s2 = [POOL[i] for i in ch[:30]], [POOL[i] for i in ch[30:]]
        t = score(s1) + score(s2)
        if best is None or t < best[0]:
            best = (t, list(ch))
    ch = best[1]
    s1 = rotate_for_balance([POOL[i] for i in ch[:30]])
    s2 = rotate_for_balance([POOL[i] for i in ch[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")
    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d" % (name, len(s)))
        print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
        print("   length-gameable: %.0f%%" % gameable_pct(s))
        print("   topics: %d of %d" % (len(set(q["topic"] for q in s)), len(ALL_TOPICS)))
        print("   lead-ins:", dict(Counter(lead_of(q) for q in s)))
        print()
    for name, s in (("SET 1", s1), ("SET 2", s2)):
        leads = Counter(lead_of(q) for q in s)
        top = max(leads.values())
        assert top <= len(s) * 0.40, "%s is %d/%d one lead-in type -- too skewed" % (name, top, len(s))
    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "cms_l2_set2.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote cms_l2_set2.json")
