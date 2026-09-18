#!/usr/bin/env python3
"""Partition a CMS I Exam 4 four-option pool into two 30s.

    python3 cms_e4_partition.py l20io    # Lecture 20 Hypertension, objective

Trimmed from cms_e3_partition.py. The Exam 3 driver carries three pieces of
machinery this one does not need: the lead-in attacher (Exam 4 pools are
authored with the lead-in in the stem), the length-fix tables, and the
five-to-four option drop remapping. Exam 4 is four-option from the start, so
none of that has anything to remap.

The scoring terms and the rotation are unchanged, including the deliberate
exclusion of the patient-stem term from objective sets -- Set 1 is recall by
design and carries no ages, so scoring it on patient stems is a flat penalty.
"""
import sys, os, json, random, re, statistics
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

WHICH = sys.argv[1] if len(sys.argv) > 1 else "l20io"
SPECS = {
 "l20io": (["cms_e4l20_pool_a:QUESTIONS", "cms_e4l20_pool_b:QUESTIONS"],
           "cms_e4l20_sets.json"),
 "l20vig": (["cms_e4l20_vig_a:QUESTIONS", "cms_e4l20_vig_b:QUESTIONS"],
            "cms_e4l20_vig_sets.json"),
}
if WHICH not in SPECS:
    sys.exit("unknown set %r -- use one of %s" % (WHICH, ", ".join(SPECS)))
mods, OUT_JSON = SPECS[WHICH]

POOL = []
for spec in mods:
    m, attr = spec.split(":")
    for q in getattr(__import__(m), attr):
        # Pools author the correct answer FIRST and leave the key implicit.
        # Rotation below moves it regardless, so a missing key means 0.
        if "c" not in q:
            q = dict(q, c=0)
        POOL.append(q)

random.seed(20260918)
PER_SET = 30
NOPT = len(POOL[0]["opts"]) if POOL else 4
assert all(len(q["opts"]) == NOPT for q in POOL), \
    "the pool mixes option counts: %s" % sorted({len(q["opts"]) for q in POOL})

PATIENT = re.compile(r"\b\d+-(year|month|week|day)-old\b|\bnewborn\b"
                     r"|\bin (his|her|their) (twenties|thirties|forties|fifties|sixties)\b", re.I)


def is_patient(q):
    return bool(PATIENT.search(q["q"]))


def is_pure_diagnosis(q):
    if q.get("lead") != "diagnosis":
        return False
    return all(len(o[0]) <= 46 and ";" not in o[0] and " and " not in o[0].lower()
               for o in q["opts"])


def longest_is_correct(q):
    s = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (tl, ti), (rn, _) = s[0], s[1]
    return ti == q["c"] and (tl - rn) >= 8 and tl >= rn * 1.18


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


# The slot floors are written for a whole lecture's pool, not for a 30. Splitting
# them in half and requiring both sets to clear them would be a different and much
# harsher bar. What matters here is that neither set collapses onto a handful of
# slots, so the term rewards SPREAD rather than any particular count.
def slot_spread(qs):
    c = Counter(q.get("slot") for q in qs if q.get("slot"))
    return len(c), sum(max(0, n - 6) for n in c.values())


def score(qs):
    """Lower is better -- penalties are in the units the standard is written in."""
    # Vignette sets only: the standard wants >= 80% patient stems. Set 1 is
    # recall by design and carries no ages, so on an objective pool this term
    # would be a flat penalty on every candidate set.
    pat = 100.0 * sum(is_patient(q) for q in qs) / len(qs)
    pat_term = max(0, 80 - pat) * 2.0 if WHICH.endswith("vig") else 0.0
    game = gameable_pct(qs)
    topics = Counter(q["topic"] for q in qs)
    lumpy = sum(max(0, n - 4) for n in topics.values())
    nslots, slot_lump = slot_spread(qs)
    return (pat_term                      # standard wants >= 80% patient stems
            + max(0, game - 13) * 1.5     # reference sits at 13%; the bar is 35%
            + lumpy * 2.0                 # do not stack one topic
            + max(0, 10 - nslots) * 3.0   # both sets should span the objective
            + slot_lump * 1.5)            # and not pile into one slot


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
        if len(q["opts"]) != NOPT:
            bad.append((i, "has %d options, set uses %d" % (len(q["opts"]), NOPT)))
        if not (0 <= q["c"] < NOPT): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
        for j, o in enumerate(q["opts"]):
            if not o[1].strip(): bad.append((i, "option %d unexplained" % j))
            if j != q["c"] and re.match(r"correct\b", o[1].strip(), re.I):
                bad.append((i, "wrong option opens with Correct"))
        if not re.match(r"correct\b", q["opts"][q["c"]][1].strip(), re.I):
            bad.append((i, "keyed option does not open with Correct"))
    return bad


if __name__ == "__main__":
    print("set: %s   pool: %d" % (WHICH, len(POOL)))
    print("schema problems:", validate(POOL) or "none")
    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    best, idx = None, list(range(len(POOL)))
    for _ in range(40000):
        random.shuffle(idx)
        ch = idx[:PER_SET * 2]
        total = score([POOL[i] for i in ch[:PER_SET]]) + score([POOL[i] for i in ch[PER_SET:]])
        if best is None or total < best[0]:
            best = (total, list(ch))

    ch = best[1]
    s1 = rotate([POOL[i] for i in ch[:PER_SET]])
    s2 = rotate([POOL[i] for i in ch[PER_SET:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        L = [len(o[0]) for q in s for o in q["opts"]]
        pos = Counter(q["c"] for q in s)
        nslots, _ = slot_spread(s)
        print("%s  n=%d" % (name, len(s)))
        print("   positions A-%s: %s" % ("ABCD"[NOPT - 1],
              "/".join(str(pos.get(i, 0)) for i in range(NOPT))))
        print("   gameable %d%%   slots covered %d   patient stems %d%%"
              % (gameable_pct(s), nslots,
                 100 * sum(map(is_patient, s)) // len(s)))
        print("   option length median %d, max %d (reference 19 / 66)"
              % (statistics.median(L), max(L)))
        print()

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, OUT_JSON), "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT_JSON)
