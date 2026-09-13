#!/usr/bin/env python3
"""Partition a CMS I Exam 3 five-option pool into two 30s.

    python3 cms_e3_partition.py l15io    # Lecture 15 External and Middle Ear, objective
    python3 cms_e3_partition.py l15vig   # Lecture 15, vignettes
    python3 cms_e3_partition.py l16io    # Lecture 16 Inner Ear and Hearing Loss, objective
    python3 cms_e3_partition.py l16vig   # Lecture 16, vignettes

Same machinery as cms_e2_partition.py -- five options, rotation across A-E,
scoring in the units the exam standard is written in.

ONE DELIBERATE CHANGE FROM THE EXAM 2 DRIVER. The patient-stem term is applied
only to VIGNETTE sets. Set 1 is recall by design and carries no ages, so on an
objective pool that term was a flat penalty on every candidate set -- and where
a pool held a handful of incidental ages it actively pulled the optimiser
toward them for no reason. The shipped Exam 2 objective quizzes sit at 7%
patient stems and that is the accepted state for Set 1; see [[cms_exam_spec]],
"the recall quizzes do not match the exam's FORM".
"""
import sys, os, json, random, re, statistics
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import apply_leadins as _leadins
_DROPS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                     "cms_four_option_drops.json"), encoding="utf-8"))
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

WHICH = sys.argv[1] if len(sys.argv) > 1 else "l15io"
SPECS = {
 "l15io":  (["cms_e3l15_pool_a:QUESTIONS", "cms_e3l15_pool_b:QUESTIONS"],
            "cms_e3l15_sets.json"),
 "l15vig": (["cms_e3l15_vig_a:QUESTIONS", "cms_e3l15_vig_b:QUESTIONS"],
            "cms_e3l15_vig_sets.json"),
 "l16io":  (["cms_e3l16_pool_a:QUESTIONS", "cms_e3l16_pool_b:QUESTIONS"],
            "cms_e3l16_sets.json"),
 "l16vig": (["cms_e3l16_vig_a:QUESTIONS", "cms_e3l16_vig_b:QUESTIONS"],
            "cms_e3l16_vig_sets.json"),
 "l17io":  (["cms_e3l17_pool_a:QUESTIONS", "cms_e3l17_pool_b:QUESTIONS"],
            "cms_e3l17_sets.json"),
 "l17vig": (["cms_e3l17_vig_a:QUESTIONS", "cms_e3l17_vig_b:QUESTIONS",
            "cms_e3l17_vig_c:QUESTIONS"], "cms_e3l17_vig_sets.json"),
 # Lectures 18 and 19 are FOUR-option, unlike 15-17 -- Jaxon, 2026-09-08.
 # NOPT is read off the pool, so nothing here needs to say so.
 "l18io":  (["cms_e3l18_pool_a:QUESTIONS", "cms_e3l18_pool_b:QUESTIONS",
            "cms_e3l18_pool_c:QUESTIONS"], "cms_e3l18_sets.json"),
 "l18vig": (["cms_e3l18_vig_a:QUESTIONS", "cms_e3l18_vig_b:QUESTIONS",
            "cms_e3l18_vig_c:QUESTIONS",
            "cms_e3l18_vig_d:QUESTIONS"], "cms_e3l18_vig_sets.json"),
 "l19io":  (["cms_e3l19_pool_a:QUESTIONS", "cms_e3l19_pool_b:QUESTIONS",
            "cms_e3l19_pool_c:QUESTIONS"], "cms_e3l19_sets.json"),
 "l19vig": (["cms_e3l19_vig_a:QUESTIONS", "cms_e3l19_vig_b:QUESTIONS",
            "cms_e3l19_vig_c:QUESTIONS"], "cms_e3l19_vig_sets.json"),
}
if WHICH not in SPECS:
    sys.exit("unknown set %r -- use one of %s" % (WHICH, ", ".join(SPECS)))
mods, OUT_JSON = SPECS[WHICH]

# Length-bias fixes, if the set has any. Keyed by (module, question index) so a
# fix survives the pools being combined in a different order, and applied BEFORE
# anything is measured. Shorten the KEY; only pad a distractor where the key's
# own detail is the content (Jaxon, 2026-08-30).
try:
    _lf = __import__("cms_e3%s_lengthfix" % WHICH.replace("io", "").replace("vig", ""))
    _LKEYS, _LSPEC = _lf.KEYS, _lf.SPECIFIC
except ImportError:
    _LKEYS, _LSPEC = {}, {}

POOL = []
for spec in mods:
    m, attr = spec.split(":")
    for _qi, q in enumerate(getattr(__import__(m), attr)):
        # Lead-in first: the L18/L19 vignette pools were authored as
        # scenario-only stems. Everything below measures option text, not the
        # stem, so order does not matter -- but doing it here keeps every
        # post-load fix in one loop.
        q = _leadins.attach(m, _qi, q)
        if (m, _qi) in _LKEYS:
            _new = _LKEYS[(m, _qi)]
            assert len(_new) < len(q["opts"][0][0]), \
                "length fix %s[%d] is not shorter" % (m, _qi)
            q["opts"][0][0] = _new
        for (_fm, _fq, _fo), _txt in _LSPEC.items():
            if _fm == m and _fq == _qi:
                assert _fo != 0, "SPECIFIC fix targets the CORRECT option"
                # These length fixes address options BY INDEX into the original
                # five. CMS moved to four on 13 September 2026, so the index has
                # to be remapped through the record of what was removed --
                # cms_four_option_drops.json, regenerated from git by
                # _four_option_drop_manifest.py.
                _di = _DROPS.get(m + ".py", [None] * (_qi + 1))[_qi] \
                    if _qi < len(_DROPS.get(m + ".py", [])) else None
                if _di is not None:
                    if _fo == _di:
                        continue                 # that option no longer exists
                    _fo -= 1 if _fo > _di else 0
                q["opts"][_fo][0] = _txt
        # Pools may author the correct answer FIRST and leave the key implicit --
        # that is the convention that stops an author drifting toward a favourite
        # position. Rotation below moves it regardless, so a missing key means 0.
        if "c" not in q:
            q = dict(q, c=0)
        POOL.append(q)

random.seed(20260903)
PER_SET = 30
# Derived from the pool rather than fixed at five. Lectures 15-17 are
# five-option; Lectures 18 and 19 are four, because Jaxon asked for four on
# 2026-09-08. A hardcoded 5 would have rejected the new pools as malformed
# rather than adapting, so the count is read off the questions and then
# enforced for consistency within the set.
NOPT = len(POOL[0]["opts"]) if POOL else 5
assert all(len(q["opts"]) == NOPT for q in POOL), \
    "the pool mixes option counts: %s" % sorted({len(q["opts"]) for q in POOL})
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
    # Vignette sets only: Set 1 is recall by design and has no ages to find.
    pat_term = max(0, 80 - pat) * 2.0 if WHICH.endswith("vig") else 0.0
    return (pat_term                        # standard wants >= 80% patient stems
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
        if len(q["opts"]) != NOPT:
            bad.append((i, "has %d options, set uses %d" % (len(q["opts"]), NOPT)))
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
        print("   positions A-%s: %s" % ("ABCDE"[NOPT - 1],
              "/".join(str(pos.get(i, 0)) for i in range(NOPT))))
        print("   patient stems %d%%   pure diagnosis %d%%   gameable %d%%"
              % (100 * sum(map(is_patient, s)) // len(s),
                 100 * sum(map(is_pure_diagnosis, s)) // len(s), gameable_pct(s)))
        print("   option length median %d, max %d (reference 19 / 66)"
              % (statistics.median(L), max(L)))
        print()

    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, OUT_JSON), "w"),
              ensure_ascii=False, indent=1)
    print("wrote", OUT_JSON)
