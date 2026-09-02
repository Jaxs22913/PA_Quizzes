#!/usr/bin/env python3
"""Partition a CMS I Exam 2 five-option pool into two 30s.

    python3 cms_e2_partition.py l2vig     # Lecture 11 Neuro-Ophthalmology, vignettes
    python3 cms_e2_partition.py l2io      # Lecture 11, objective set
    python3 cms_e2_partition.py l3vig     # Lecture 12 Acute Vision Loss, vignettes
    python3 cms_e2_partition.py l3io      # Lecture 12, objective set

Unlike the pharmacology partitions this is FIVE-option, because CMS follows the
exam standard Jaxon set from his own reference items on 2026-08-26/27. The
scoring optimises the things that standard actually measures -- patient stems,
share of pure-diagnosis items, length gameability -- rather than only objective
coverage, so a set does not have to be repaired after the fact.

Answer position is set by ROTATION across A-E, never chosen while authoring.
"""
import sys, os, json, random, re, statistics
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

WHICH = sys.argv[1] if len(sys.argv) > 1 else "l2vig"
SPECS = {
 "l2vig": (["cms_e2l2_vig_a:POOL_A", "cms_e2l2_vig_b:POOL_B", "cms_e2l2_vig_c:POOL_C",
           "cms_e2l2_vig_d:POOL_D"],
           "cms_e2l2_vig_sets.json"),
 "l2io":  (["cms_e2l2_vig_a:POOL_A", "cms_e2l2_vig_b:POOL_B", "cms_e2l2_vig_c:POOL_C",
            "cms_e2l2_pool_a:POOL_A", "cms_e2l2_pool_b:POOL_B"], "cms_e2l2_sets.json"),
 "l3vig": (["cms_e2l3_vig_a:POOL_A", "cms_e2l3_vig_b:POOL_B"], "cms_e2l3_vig_sets.json"),
 "l3io":  (["cms_e2l3_pool_a:POOL_A", "cms_e2l3_pool_b:POOL_B"], "cms_e2l3_sets.json"),
 # Lecture 13, Chronic Vision Loss & Tumors. Its pools export QUESTIONS rather
 # than POOL_A, which the loader below handles.
 "l4vig": (["cms_e2l13_vig_a:QUESTIONS", "cms_e2l13_vig_b:QUESTIONS"],
           "cms_e2l13_vig_sets.json"),
 "l4io":  (["cms_e2l13_pool_a:QUESTIONS", "cms_e2l13_pool_b:QUESTIONS"],
           "cms_e2l13_sets.json"),
 # Lecture 14, Ocular Trauma. Same QUESTIONS export as Lecture 13.
 "l5vig": (["cms_e2l14_vig_a:QUESTIONS", "cms_e2l14_vig_b:QUESTIONS",
            "cms_e2l14_vig_c:QUESTIONS", "cms_e2l14_vig_d:QUESTIONS"],
           "cms_e2l14_vig_sets.json"),
 "l5io":  (["cms_e2l14_pool_a:QUESTIONS", "cms_e2l14_pool_b:QUESTIONS",
            "cms_e2l14_pool_c:QUESTIONS"], "cms_e2l14_sets.json"),
}
if WHICH not in SPECS:
    sys.exit("unknown set %r -- use one of %s" % (WHICH, ", ".join(SPECS)))
mods, OUT_JSON = SPECS[WHICH]

# Length-bias fixes, if the set has any. Keyed by (module, question index) so a
# fix survives the pools being combined in a different order, and applied BEFORE
# anything is measured. Shorten the KEY; only pad a distractor where the key's
# own detail is the content (Jaxon, 2026-08-30).
try:
    from cms_e2l14_lengthfix import KEYS as _LKEYS, SPECIFIC as _LSPEC
except ImportError:
    _LKEYS, _LSPEC = {}, {}

POOL = []
for spec in mods:
    m, attr = spec.split(":")
    for _qi, q in enumerate(getattr(__import__(m), attr)):
        if (m, _qi) in _LKEYS:
            _new = _LKEYS[(m, _qi)]
            assert len(_new) < len(q["opts"][0][0]), \
                "length fix %s[%d] is not shorter" % (m, _qi)
            q["opts"][0][0] = _new
        for (_fm, _fq, _fo), _txt in _LSPEC.items():
            if _fm == m and _fq == _qi:
                assert _fo != 0, "SPECIFIC fix targets the CORRECT option"
                q["opts"][_fo][0] = _txt
        # Pools may author the correct answer FIRST and leave the key implicit --
        # that is the convention that stops an author drifting toward a favourite
        # position. Rotation below moves it regardless, so a missing key means 0.
        if "c" not in q:
            q = dict(q, c=0)
        POOL.append(q)

# Lecture 11 authored one pool; the pathway-and-anatomy items are routed to the
# objective set and kept out of the vignettes, which the standard judges on
# whether its stems carry an age.
if WHICH in ("l2vig", "l2io"):
    from cms_e2l2_split import RECALL
    if WHICH == "l2vig":
        POOL = [q for i, q in enumerate(POOL) if i not in RECALL]
    else:
        # RECALL indexes the three vignette modules, which are listed first here;
        # everything past them is purpose-written objective material and is kept.
        from cms_e2l2_vig_a import POOL_A as _va
        from cms_e2l2_vig_b import POOL_B as _vb
        from cms_e2l2_vig_c import POOL_C as _vc
        n_vig = len(_va) + len(_vb) + len(_vc)
        POOL = [q for i, q in enumerate(POOL) if i >= n_vig or i in RECALL]

random.seed(20260829)
PER_SET, NOPT = 30, 5
# taken verbatim from check_exam_standard.py: a stem "names a patient" only if
# it carries an explicit age. Scoring against a looser proxy (counting the word
# "patient") optimised for the wrong thing and shipped a set at 67%.
PATIENT = re.compile(r"\b\d+-(year|month|week|day)-old\b|\bnewborn\b"
                     r"|\bin (his|her|their) (twenties|thirties|forties|fifties|sixties)\b", re.I)


def is_patient(q):
    return bool(PATIENT.search(q["q"]))


def is_pure_diagnosis(q):
    """Every option is a bare condition name and the stem asks which it is."""
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


def score(qs):
    """Lower is better -- penalties are in the units the standard is written in."""
    pat = 100.0 * sum(is_patient(q) for q in qs) / len(qs)
    dx = 100.0 * sum(is_pure_diagnosis(q) for q in qs) / len(qs)
    game = gameable_pct(qs)
    topics = Counter(q["topic"] for q in qs)
    lumpy = sum(max(0, n - 4) for n in topics.values())
    leads = len(set(q.get("lead") for q in qs))
    return (max(0, 80 - pat) * 2.0          # standard wants >= 80% patient stems
            + abs(dx - 30) * 0.8            # about a quarter to a third pure diagnosis
            + max(0, game - 13) * 1.5       # reference sits at 13%; the bar is 35%
            + lumpy * 2.0                   # do not stack one topic
            + max(0, 5 - leads) * 4)        # keep the lead-ins varied


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
        if len(q["opts"]) != NOPT: bad.append((i, "not five options"))
        if not (0 <= q["c"] < NOPT): bad.append((i, "answer index out of range"))
        if not q.get("cite"): bad.append((i, "missing citation"))
        if len(set(o[0] for o in q["opts"])) != NOPT: bad.append((i, "duplicate option"))
        for j, o in enumerate(q["opts"]):
            if not o[1].strip(): bad.append((i, "option %d unexplained" % j))
            # word boundary matters: a distractor reading "Corrective treatment
            # is considered only after six months" is not opening with "Correct"
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
        print("%s  n=%d" % (name, len(s)))
        print("   positions A-E: %s" % "/".join(str(pos.get(i, 0)) for i in range(NOPT)))
        print("   patient stems %d%%   pure diagnosis %d%%   gameable %d%%"
              % (100 * sum(map(is_patient, s)) // len(s),
                 100 * sum(map(is_pure_diagnosis, s)) // len(s), gameable_pct(s)))
        print("   option length median %d, max %d (reference 19 / 66)"
              % (statistics.median(L), max(L)))
        print()

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, OUT_JSON), "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT_JSON)
