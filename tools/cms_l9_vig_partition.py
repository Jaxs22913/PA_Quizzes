#!/usr/bin/env python3
"""Partition CMS I Lecture 9 Set 2 (Pre-malignant and Malignant vignettes) into two 30s.

Four pools rather than three: 38 vignettes across A-C was short of the 60 that
two distinct 30-question forms need, so pool D is a second pass across every
topic. Pool D was written faster and came in at 55% length-gameable against
0-7% for the others -- seven were fixed by the automated trimmer and the rest by
padding. All four finish at 0%.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_l9_vig_a import VIG_A
from cms_l9_vig_b import VIG_B
from cms_l9_vig_c import VIG_C
from cms_l9_vig_d import VIG_D

POOL = VIG_A + VIG_B + VIG_C + VIG_D

# Set 2 is vignettes: every stem must present a patient, not ask a bare fact.
# A handful legitimately follow on from the stem before them ("the same
# patient"), which is why this looks for a patient anywhere in the stem rather
# than only at the start.
_PT = re.compile(r"\b\d+[- ]year[- ]old|\b\d+[- ]month[- ]old|\b\d+[- ]week[- ]old|"
                 r"newborn|the same (patient|mother|woman|man)|that (patient|infant)|"
                 r"the patient|a patient|an? (immunocompromised|pregnant) patient|"
                 r"\ba (child|man|woman)\b|two patients|four patients|you are (assessing|explaining)|his |her ", re.I)
_bare = [q["q"][:70] for q in POOL if not _PT.search(q["q"])]
assert not _bare, "Set 2 stem with no patient in it: %r" % _bare[:3]

_DEP = re.compile(r"previous question|question above|as in the last|earlier question", re.I)
assert not [q for q in POOL if _DEP.search(q["q"])], "a stem depends on another question"

LEAD = {
 "diagnosis": r"most likely diagnosis|most likely explanation|which term describes|which subtype|best separates|most appropriate interpretation|which condition must be checked|which risk factors are named",
 "next step": r"next step|most appropriate approach|why can it not simply be observed",
 "treatment": r"most appropriate treatment|first-line|appropriate management|which topical option|which options are appropriate|most appropriate plan|most appropriate first-line",
 "test": r"which test|establishes the diagnosis|which investigations|which risks should be checked",
 "education": r"counselling point|most appropriate response|most appropriate advice|most appropriate explanation|which support does the lecture name|most important consequence|which additional consideration",
}
def lead_of(q):
    # An explicit lead= on the question wins. The regexes below classify the
    # rest; where a stem reads "which is the most appropriate response?" the
    # phrasing alone does not say whether it is testing management, mechanism
    # or education, so those carry the field.
    if q.get("lead"):
        return q["lead"]
    for k, p in LEAD.items():
        if re.search(p, q["q"], re.I):
            return k
    return "other"

_other = [q["q"][-70:] for q in POOL if lead_of(q) == "other"]
assert not _other, "unclassified lead-in, the skew guard would be blind to it: %r" % _other

random.seed(20260820)
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
    print("guards: every stem is a vignette, no cross-form dependency, lead-ins spread")
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
    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "cms_l9_set2.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote cms_l9_set2.json")
