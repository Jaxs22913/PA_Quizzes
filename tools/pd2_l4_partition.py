#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PD2 Lecture 4 (Advanced ENT History and Exam) pool into two 30s.

THE TUNING FORK BLOCK IS WEIGHTED AND BOTH SETS MUST CARRY IT. A video played
in class said it outright -- "the Weber and the Rinne tests are both high yield,
the difference between sensorineural hearing loss and conductive hearing loss is
also high yield ... it will be three points on test day" -- and the lecturer
added his own correction on top, because the video worked the sensorineural case
and left the conductive one implicit. Asserted below: at least four tuning fork
or hearing loss questions in each set.

CENTOR IS IN BOTH SETS BY ASSERTION. It has its own slide plus a modified
scoring slide behind it, and Jaxon flagged it independently out of the CMS
lecture the same week -- "I must know the centor criteria". Two courses asking
for the same four criteria is as strong a signal as this material gives.

BATES IS NOT A SOURCE HERE. Slide 94 declares tables 7-1, 7-2, 7-4 and 7-19
through 7-26 testable, and the reading assignments too. Those are a textbook I
do not have, so every question here comes from the deck or the recording. Where
the deck reproduces a Bates table on its own slide -- the vertigo comparison on
slide 12, the hearing loss summary on slide 45 -- that content IS covered,
because the slide carries it. The gap is flagged in the study guide rather than
papered over with invented content.

House rules for this course: no question may depend on having the deck open, and
none may be about course mechanics -- and this deck is full of the latter, from
"bring Bates to lab" to how the practical is graded.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pd2_l4_pool_a import POOL_A
from pd2_l4_pool_b import POOL_B
from pd2_l4_pool_c import POOL_C

POOL = POOL_A + POOL_B + POOL_C

try:
    from pd2_l4_lengthfix import FIXES
except ImportError:
    FIXES = {}
for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

# ---- Guard 1: nothing may depend on having the deck open -------------------
_CTX = re.compile(r"on (?:this|the) slide|the slide (?:shows|says)|as shown (?:above|below)|"
                  r"in the (?:image|picture|photograph) (?:above|below|shown)|"
                  r"pictured (?:above|below)|the deck", re.I)
_ctx = [q["q"][:70] for q in POOL if _CTX.search(q["q"])]
assert not _ctx, "question depends on having the deck open: %r" % _ctx[:3]

# ---- Guard 2: no course mechanics ------------------------------------------
# This deck carries an unusual amount of it -- what to bring to lab, which
# edition of Bates, how the practical is graded. None of it is content.
_MECH = re.compile(r"how many (?:points|questions) is|when is the exam|what should you bring|"
                   r"which edition|bates.{0,20}(?:chapter|table|edition)|reading assignment|"
                   r"lab session|how (?:are you|will you be) graded|earplugs", re.I)
_mech = [q["q"][:70] for q in POOL if _MECH.search(q["q"]) or
         any(_MECH.search(o[0]) for o in q["opts"])]
assert not _mech, "course-mechanics question in the pool: %r" % _mech[:3]

# ---- Guard 3: physical diagnosis, not pathophysiology or management --------
# Clin Path I Lecture 5 owns the mechanism side of this same organ system and
# CMS I Exam 3 owns the management side. This course asks what you find.
_SCOPE = re.compile(r"first[- ]line|drug of choice|what is the treatment|how (?:do|would) you treat|"
                    r"which antibiotic|molecular mechanism|pathogenesis of|cytokine|"
                    r"interleukin|apoptosis", re.I)
_sc = [q["q"][:70] for q in POOL if _SCOPE.search(q["q"])]
assert not _sc, "strays into pathophysiology or management: %r" % _sc[:3]

# ---- Guard 4: the weighted blocks are big enough to split ------------------
_FORK = [q for q in POOL if q["topic"] in ("Tuning fork tests", "Hearing loss", "Hearing screening")]
assert len(_FORK) >= 12, ("the tuning fork and hearing loss block was called out as three "
                          "points on test day -- %d questions is not enough to put four in "
                          "each set" % len(_FORK))
_CENTOR = [q for q in POOL if q["topic"] == "Centor criteria"]
assert len(_CENTOR) >= 2, "Centor needs at least one question per set"

# ---- Guard 5: every explanation refutes AND supplies the replacing fact ----
# RETIRED 2026-09-24: the old Guard 5 failed an explanation only if it opened
# with a bare negation AND ran under 52 characters, on the theory that "That is
# vertigo." teaches the discrimination. By 2026-09-22 65% of PD2 Exam 1's
# distractor explanations were under 60 characters. Jaxon decided 2026-09-22
# that PD2 uses the site rule (memory: pd2_exam_spec, option_explanation_length):
# every explanation, correct or wrong, is at least 60 characters, and a wrong
# option's explanation refutes it AND states the fact that replaces it. Length
# is the enforceable half; the refute-plus-fact half is authored by hand. Do not
# reintroduce the "names the distractor" guard.
MIN_EXPL = 60

# ---- Guard 6: one ask per stem, and no source citations --------------------
# 24 stems asked two things ("What is it, and does it matter?"), which forces a
# compound key and let a 2026-09-13 mechanical key-shortening cut half the
# answer away. A stem must ask exactly one thing.
_TWO_ASK = re.compile(r",? and (?:what|why|which|how|who|where|does|in whom)\b|"
                      r"— and what\b|\bwhat\b[^?]*\band what\b", re.I)
_two = [q["q"][:70] for q in POOL if _TWO_ASK.search(q["q"])]
assert not _two, "stem asks two things -- split or narrow it: %r" % _two[:3]
from _selfcontain_rx import RX as _CITES
_cit = [s[:70] for q in POOL for s in [q["q"]] + [x for o in q["opts"] for x in o]
        if _CITES.search(s)]
assert not _cit, "question cites its source (lecture/deck/lecturer): %r" % _cit[:3]

SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260903 + 44)
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (top_len, top_i), (runner, _) = lens[0], lens[1]
    if top_i != q["c"]:
        return False
    return (top_len - runner) >= MARGIN_CHARS and top_len >= runner * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


ALL_TOPICS = set(q["topic"] for q in POOL)
FORK_TOPICS = ("Tuning fork tests", "Hearing loss", "Hearing screening")


def score(setqs):
    tops = Counter(q["topic"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    nfork = sum(1 for q in setqs if q["topic"] in FORK_TOPICS)
    ncentor = sum(1 for q in setqs if q["topic"] == "Centor criteria")
    fork_pen = abs(6 - nfork) * 20          # want about six per set
    centor_pen = abs(1 - ncentor) * 40      # want exactly one per set
    lumpy_t = sum(max(0, n - 3) for n in tops.values())
    lumpy_s = sum(max(0, n - 6) for n in slots.values())
    thin_slots = max(0, 10 - len(slots))
    return (fork_pen + centor_pen + thin_slots * 15 + lumpy_t * 3 + lumpy_s * 2
            + gameable_pct(setqs) * 8.0)


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
            if len(o[1].strip()) < MIN_EXPL:
                bad.append((i, "explanation under %d characters: %r" % (MIN_EXPL, o[1][:44])))
        for j, o in enumerate(q["opts"]):
            if (j == q["c"]) != o[1].startswith("Correct"):
                bad.append((i, "only the key's explanation may open with 'Correct': option %d" % j))
    return bad


if __name__ == "__main__":
    print("pool size:", len(POOL), " topics:", len(ALL_TOPICS))
    problems = validate(POOL)
    print("schema problems:", problems or "none")
    assert not problems, problems[:6]
    print("tuning fork / hearing questions available:", len(_FORK))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("house rules: no deck-dependent question, no course mechanics, "
          "no pathophysiology or management")
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}

    def total(sel):
        return score([POOL[i] for i in sel[:30]]) + score([POOL[i] for i in sel[30:]])

    idx = list(range(len(POOL)))
    best = None
    for _ in range(400):
        random.shuffle(idx)
        cand = idx[:60]
        t = total(cand)
        if best is None or t < best[0]:
            best = (t, list(cand))
    cur_score, cur = best
    outside = [i for i in range(len(POOL)) if i not in set(cur)]
    for _ in range(60000):
        a = random.randrange(60)
        b = random.randrange(len(outside))
        cur[a], outside[b] = outside[b], cur[a]
        t = total(cur)
        if t < cur_score:
            cur_score = t
        else:
            cur[a], outside[b] = outside[b], cur[a]
    print("local search settled at score %.1f" % cur_score)

    s1 = rotate_for_balance([POOL[i] for i in cur[:30]])
    s2 = rotate_for_balance([POOL[i] for i in cur[30:]])
    for q in s1 + s2:
        assert q["opts"][q["c"]][0] == answer_text[id(q)], "rotation moved an answer!"
    print("rotation check: every correct answer still points at its own text")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        nf = sum(1 for q in s if q["topic"] in FORK_TOPICS)
        assert nf >= 4, ("%s has only %d tuning fork / hearing loss questions -- that block "
                         "was called out as three points on test day" % (name, nf))
        nc = sum(1 for q in s if q["topic"] == "Centor criteria")
        assert nc >= 1, "%s has no Centor question, and two courses asked for it" % name
        g = gameable_pct(s)
        assert g <= 35.0, "%s: key longest in %.0f%% -- shorten the keys" % (name, g)
    print("weighting check: both sets carry the tuning forks and Centor\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions %s  gameable %.1f%%  topics %d  slots %d  fork %d  centor %d"
              % (name, len(s), dict(sorted(pos.items())), gameable_pct(s),
                 len(set(q["topic"] for q in s)), len(set(q["slot"] for q in s)),
                 sum(1 for q in s if q["topic"] in FORK_TOPICS),
                 sum(1 for q in s if q["topic"] == "Centor criteria")))

    # ---- Selection guard (2026-09-24) -------------------------------------
    # The shipped topic pages are rendered from pd2_l4_sets.json, and the PD2
    # master forms were paired against them. A text-only pool edit reproduces
    # the committed selection exactly (the search is seeded and its random
    # stream does not depend on text), but an edit that flips a question's
    # length-gameable status changes the score and so the selection. Refuse to
    # overwrite a sets file whose selection (topic, slot, cite, key position,
    # per question, in order) would change, unless --force is given on purpose.
    _out = os.path.join(HERE, "pd2_l4_sets.json")
    def _sig(sets):
        return [(q["topic"], q["slot"], q["cite"], q["c"]) for k in ("set1", "set2") for q in sets[k]]
    if os.path.exists(_out) and "--force" not in sys.argv:
        _old = json.load(open(_out, encoding="utf-8"))
        _chg = sum(a != b for a, b in zip(_sig(_old), _sig({"set1": s1, "set2": s2})))
        assert _chg == 0, ("%d of 60 selected questions would change; the shipped pages and "
                           "master pairing assume the committed selection. Re-run with --force "
                           "only if a new selection is intended." % _chg)
        print("selection guard: identical selection to the committed sets file")
    with open(_out, "w", encoding="utf-8") as fh:
        json.dump({"set1": s1, "set2": s2}, fh, ensure_ascii=False, indent=1)
    print("\nwrote pd2_l4_sets.json")
