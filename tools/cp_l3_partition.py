#!/usr/bin/env python3
"""Partition the Clinical Pathophysiology I Lecture 3 pool into two 30s.

Abnormal Cell Growth and Differentiation. House format for this class is 2x30
per topic and NO vignettes -- Clin Path asks what is happening in the tissue,
which is not a bedside question.

Objectives come from the SYLLABUS, verbatim (a-l), not from the slides.

LENGTH BIAS. Raw rates: pool A 19%, pool B 38%, pool C 66%. Pool C is the worst
because it is nothing but mechanism explanations, and a mechanism stated
correctly is long by nature. All three were repaired by TRIMMING THE CORRECT
ANSWER and moving the mechanism into its own explanation, which the student
reads immediately after answering -- 25 single edits took pool C from 66% to 0%.
All three pools finish at 0%.

POOL D IS FROM THE 2026-08-20 RECORDING. This lecture SIGNPOSTS NOTHING -- 84
minutes across two independent transcriptions with no statement about what is or
is not on the exam. So pool D is not a re-weighting; it is the teaching that
never reaches a slide. Professor Rappa explains almost every term through a
clinical example (Barrett's oesophagus for metaplasia, cervical dysplasia for
dysplasia, weight training for hypertrophy) and states one link the deck does
not make at all: falling differentiation means a MORE AGGRESSIVE tumour.

SLIDE 43 IS AN IMAGE and is deliberately not asked from. It is a lung-cancer-
specific 7th-edition TNM table, and the deck's own point on slide 42 is that TNM
definitions are CANCER-SPECIFIC. Asking its lung cut-offs would be inventing
scope out of an illustration. Asserted below.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.

2026-09-24 -- RECORDING-ONLY QUESTIONS ARE NO LONGER DRAWN, AND THIS SCRIPT NO
LONGER OVERWRITES THE SHIPPED SELECTION BY DEFAULT. Site rule (CLAUDE.md sec. 7,
slides-only grounding): a lecturer's aside does not add content the deck lacks,
and no question is built on a lecture's worked example. Six shipped pool-D items
rested on the recording alone (Barrett's oesophagus as THE metaplasia example,
columnar cells meaning "secondary to reflux", the pathologist as sole
diagnostician, lung-to-brain via the carotids, the plural "carcinomata", the
leio-/rhabdo- prefixes). cp_l3_sets.json and both pages now carry unshipped
deck-grounded pool items in those six positions instead (same objective or
slide, same answer position), chosen by hand -- not by this script. Pool-D
items that the deck does support are re-cited to their slide and still ship.
So:
  * POOL excludes any item whose cite is the recording (EXCLUDED_REC below).
  * Re-running therefore selects DIFFERENTLY from the shipped sets. The script
    compares its selection (option texts, order and keys per position) with the
    existing cp_l3_sets.json and REFUSES to write when they differ, unless run
    with --force. A text-only change (stems, explanations) still writes.
  * Run with --force only when you mean to reselect both quizzes; then re-render,
    re-check, and tell the Clin Path masters, which sample from these pages.
"""
import sys, os, json, random
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cp_l3_pool_a import POOL_A
from cp_l3_pool_b import POOL_B
from cp_l3_pool_c import POOL_C
from cp_l3_pool_d import POOL_D

_REC = "2026-08-20 lecture recording"
EXCLUDED_REC = [q for q in POOL_A + POOL_B + POOL_C + POOL_D if q["cite"].startswith(_REC)]
POOL = [q for q in POOL_A + POOL_B + POOL_C + POOL_D if not q["cite"].startswith(_REC)]

# SCOPE GUARD: Clinical Pathophysiology is mechanism, never management. The
# same oncology material is taught elsewhere in the curriculum, so the line has
# to be enforced rather than trusted. "Eradication" is allowed through because
# the deck's own point about Helicobacter pylori is what eradication does to
# RISK -- that is the mechanism, not a treatment recommendation.
import re as _re
_MGMT = _re.compile(r"first[- ]line|drug of choice|treatment of choice|next step|"
                    r"prescrib|manage(d|ment) with|how (is|would) .* treated", _re.I)
assert not [q for q in POOL if _MGMT.search(q["q"]) or _MGMT.search(q["opts"][q["c"]][0])], \
    "management-scope question in a pathophysiology pool"

# Slide 43's table is an illustration of "TNM is cancer-specific", not a
# memorisation target.
_s43 = [q["q"] for q in POOL if q["cite"].strip().endswith("Slide 43")]
assert not _s43, "cites slide 43, a cancer-specific TNM table used only as an illustration: %r" % _s43[:2]

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


def score(setqs):
    """Lower is better. Position is not scored -- rotation guarantees it."""
    ios = Counter(q["io"] for q in setqs)
    missing = len(ALL_IOS - set(ios))
    # a set that piles six questions onto one objective is worse than one that
    # spreads them, even when both cover everything
    lumpy = sum(max(0, n - 4) for n in ios.values())
    return missing * 25 + lumpy * 3 + gameable_pct(setqs) * 1.2


def rotate_for_balance(qs):
    """Give each question a target answer position, evenly spread, then rotate."""
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
    print("objectives:", len(ALL_IOS))
    print("pool length-gameable: %.0f%%" % gameable_pct(POOL))
    print()

    # the correct TEXT of each question, captured before rotation, so the
    # rotation can be proven not to have moved any answer onto a wrong option
    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    best, idx = None, list(range(len(POOL)))
    for _ in range(30000):
        random.shuffle(idx)
        chosen = idx[:60]
        s1 = [POOL[i] for i in chosen[:30]]
        s2 = [POOL[i] for i in chosen[30:]]
        total = score(s1) + score(s2)
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
        print("   objectives: %d of %d" % (len(ios), len(ALL_IOS)))
        print()

    # GUARD (2026-09-24): never silently replace the shipped selection.
    _out = os.path.join(HERE, "cp_l3_sets.json")
    if os.path.exists(_out) and "--force" not in sys.argv:
        _old = json.load(open(_out, encoding="utf-8"))
        _fp = lambda qs: [([o[0] for o in q["opts"]], q["c"]) for q in qs]
        if _fp(_old["set1"]) != _fp(s1) or _fp(_old["set2"]) != _fp(s2):
            print("REFUSING to overwrite cp_l3_sets.json: this run selects different questions, "
                  "options or keys than the shipped sets (see the 2026-09-24 note in the docstring). "
                  "Re-run with --force only if you intend to reselect both quizzes.")
            sys.exit(2)
    json.dump({"set1": s1, "set2": s2},
              open(os.path.join(HERE, "cp_l3_sets.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote cp_l3_sets.json")
