#!/usr/bin/env python3
"""Select the Physical Diagnosis 2 Lecture 1 quiz: ONE set of twelve.

Not the house two-by-thirty. The lecture is largely course orientation, and with
that excluded there are about eighteen genuinely clinical questions in the
source. Fifteen selected from eighteen is what the material honestly supports.

2026-09-22: three of those eighteen were course mechanics after all (handling
feedback that differs between facilitators, reviewing the grading rubric, and
reusing your own work for academic credit). Jaxon chose REMOVE ONLY, not
replace: they are gone from the pool, the shipped quiz went from 15 to 12, and
the asserts below make sure none of them can ever be selected again.

DO NOT RE-RUN THIS TO "REFRESH" THE QUIZ. The shipped set was chosen from the
18-question pool with the seed below; with 15 left in the pool the same seed
draws a different twelve, so a re-run would silently replace shipped questions
and desynchronize pd2_l1_sets.json from the page and the master forms (which
pair to it by stem). The committed pd2_l1_sets.json is the page's twelve with
the three removed, edited in place. The script therefore refuses to overwrite a
sets file whose selection would change; pass --force only when a NEW selection
is actually wanted (then re-render the page and tell the masters owner).

Explanations follow the site rule decided 2026-09-22: every option explanation
refutes (or confirms) AND states the replacing fact, at least 60 characters.
The old PD2 "names the distractor" allowance is retired; asserted below.

Same machinery as the other partitions: length-bias remediation first, then
selection against objective coverage, then rotation to spread the answer
position. Every question is authored with its correct answer first, because
choosing the index by hand while writing is how the "always A" bug happened.
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pd2_l1_pool_a import POOL_A as POOL

import difflib
from pd2_l1_lengthfix import FIXES
for _idx, (_stated, _text) in FIXES.items():
    _q = POOL[_idx]
    _ratio, _oi = max((difflib.SequenceMatcher(None, _text.lower(), _o[0].lower()).ratio(), _i)
                      for _i, _o in enumerate(_q["opts"]) if _i != _q["c"])
    assert _ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (_idx, _ratio)
    _q["opts"][_oi][0] = _text

# Jaxon's two rules for this lecture, asserted rather than trusted.
import re as _re
_CTX = _re.compile(r"according to the (powerpoint|slide|lecture)|in the (powerpoint|slide|example)|"
                   r"the sample (note|case)|as shown (on|in) the", _re.I)
assert not [q for q in POOL if _CTX.search(q["q"])], "question depends on having the deck open"
_MECH = _re.compile(r"percent of the (course|grade)|sequester|file nam|late assignment|dress code|"
                    r"how long does .* run|what may a student bring", _re.I)
assert not [q for q in POOL if _MECH.search(q["q"])], "course-mechanics question in the pool"
# The three removed 2026-09-22, by exact stem and by subject, so a rewording
# cannot slip one back in either.
_REMOVED = {
    "Why can reusing your own earlier written work create an academic integrity problem?",
    "How should a student handle feedback that differs between facilitators?",
    "What should be reviewed before submitting a written clinical assignment?",
}
_MECH2 = _re.compile(r"facilitator|rubric|academic (credit|integrity)|plagiar|reus(e|ing) (your|a) |"
                     r"grading|submitt(ed|ing) (for|a written)", _re.I)
assert not [q for q in POOL if q["q"] in _REMOVED], "a removed course-mechanics question is back"
assert not [q for q in POOL if _MECH2.search(q["q"]) or any(_MECH2.search(o[0]) for o in q["opts"][q["c"]:q["c"] + 1])], \
    "course-mechanics question (feedback / rubric / academic credit) in the pool"

# Site explanation rule (Jaxon 2026-09-22): refute + replacing fact, >= 60 chars.
_THIN = [(i, j) for i, q in enumerate(POOL) for j, o in enumerate(q["opts"]) if len(o[1].strip()) < 60]
assert not _THIN, "explanation under 60 characters at (question, option) %r" % _THIN[:8]

random.seed(20260818)
SET_SIZE = 12
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


def score(qs):
    ios = Counter(q["io"] for q in qs)
    missing = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - 6) for n in ios.values())
    return missing * 25 + lumpy * 3 + gameable_pct(qs) * 1.2


def rotate_for_balance(qs):
    targets = [i % 4 for i in range(len(qs))]
    random.shuffle(targets)
    for q, t in zip(qs, targets):
        k = (t - q["c"]) % 4
        if k:
            q["opts"] = q["opts"][-k:] + q["opts"][:-k]
        q["c"] = t
    return qs


if __name__ == "__main__":
    print("pool size:", len(POOL))
    print("objectives:", len(ALL_IOS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    bad = [i for i, q in enumerate(POOL)
           if len(q["opts"]) != 4 or len(set(o[0] for o in q["opts"])) != 4 or not q.get("cite")]
    print("schema problems:", bad or "none")
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best, idx = None, list(range(len(POOL)))
    for _ in range(20000):
        random.shuffle(idx)
        chosen = [POOL[i] for i in idx[:SET_SIZE]]
        s = score(chosen)
        if best is None or s < best[0]:
            best = (s, list(idx[:SET_SIZE]))

    qs = rotate_for_balance([POOL[i] for i in best[1]])
    for q in qs:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    pos = Counter(q["c"] for q in qs)
    ios = Counter(q["io"] for q in qs)
    print("SET  n=%d" % len(qs))
    print("   answer positions A/B/C/D: %d/%d/%d/%d" % tuple(pos.get(i, 0) for i in range(4)))
    print("   length-gameable: %.0f%%" % gameable_pct(qs))
    print("   objectives: %d of %d" % (len(ios), len(ALL_IOS)))
    out_path = os.path.join(HERE, "pd2_l1_sets.json")
    if os.path.exists(out_path) and "--force" not in sys.argv:
        shipped = [q["q"] for q in json.load(open(out_path, encoding="utf-8"))["set1"]]
        if shipped != [q["q"] for q in qs]:
            sys.exit("REFUSING to overwrite pd2_l1_sets.json: this run selects a different set "
                     "(%d of %d shipped stems kept, order may differ). See the docstring; "
                     "pass --force only to deliberately re-select." %
                     (len(set(shipped) & set(q["q"] for q in qs)), len(shipped)))
    json.dump({"set1": qs}, open(out_path, "w"),
              ensure_ascii=False, indent=1)
    print("\nwrote pd2_l1_sets.json")
