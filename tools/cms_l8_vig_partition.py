#!/usr/bin/env python3
"""Partition CMS I Lecture 8 SET 2 (the vignettes) into two 30s.

CMS runs four exams per topic: Set 1 is 2 x 30 on the objectives, Set 2 is this
2 x 30 of vignettes. Set 1 shipped separately.

Three guards run before anything else, because all three failures would be
invisible in the finished quiz:

  EVERY STEM IS A VIGNETTE. A recall-shaped question here would make Set 2
  indistinguishable from Set 1 and waste one of the four exams.

  LEAD-INS STAY SPREAD. The style rule says not every vignette asks for
  management. Pools A to C came out 19 diagnosis against 4 asking for a test
  across 62 questions -- only two spare for 60 slots -- which is why pool D
  exists. The guard fails the build if any one lead-in type exceeds 40% of a
  set.

  NOTHING DEPENDS ON THE OTHER FORM. No stem may refer to a previous question.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cms_l8_vig_a import POOL_A
from cms_l8_vig_b import POOL_B
from cms_l8_vig_c import POOL_C
# STRAY IMPORTS REMOVED. This file used to carry
#     from cms_l4_vig_d import POOL_D
#     from cms_l5_vig_d import POOL_D
# neither of which was used, the second shadowing the first. Leftover from
# copy-paste. Harmless only by accident: had anyone later written "+ POOL_D"
# they would have silently shipped LECTURE 5's vignettes inside the Lecture 8
# paper, and nothing here would have complained.
from cms_l8_vig_d import VIG_D
from cms_l8_vig_lengthfix import SLOT_FIXES

# Pool D is APPENDED, so the SLOT_FIXES indices into A + B + C stay valid.
POOL = POOL_A + POOL_B + POOL_C
for (_qi, _oi), _t in SLOT_FIXES.items():
    assert _oi != POOL[_qi]["c"], "length fix %d would overwrite the correct option" % _qi
    POOL[_qi]["opts"][_oi][0] = _t
POOL = POOL + VIG_D

_VIG = re.compile(r"^A[n]? \d+[- ]?(year|month|week|day)[- ]old|^(A|The) (mother|father|parent|parents)\b|^An? (neonate|infant|newborn|patient)\b", re.I)
_bad = [q["q"][:60] for q in POOL if not _VIG.match(q["q"])]
assert not _bad, "non-vignette stem in Set 2: %r" % _bad

# A stem must stand alone: the partitioner shuffles, so there is no "previous
# question". The original version of this pattern listed only the phrasings I
# imagined -- "previous question", "question above" -- and missed the one I had
# actually written thirteen times, "The same patient". A student found it before
# the guard did. It now matches back-references anywhere in the stem, and it is
# present in EVERY vignette partition; Lecture 2's had no dependency guard at all.
_DEP = re.compile(r"previous question|question above|as in the last|earlier question"
                  r"|\b(?:that|the same|this same) (?:patient|man|woman|girl|boy|mother|"
                  r"father|child|infant|lesion|nodule|plaque|rash|scar)\b"
                  r"|\bthe patient (?:above|described above)\b", re.I)
assert not [q for q in POOL if _DEP.search(q["q"])], (
    "a stem leans on another question; the draw shuffles, so it must stand alone: %r"
    % [q["q"][:70] for q in POOL if _DEP.search(q["q"])][:3])

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

random.seed(20260824)
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
    # HER DESCRIPTION OF THE EXAM, 24 August 2026: "there's gonna be like
    # clinical vignettes or pretty much all clinical vignettes. There might be
    # SOME question, what's the most likely diagnosis, but A LOT OF THEM are --
    # what's the next management plan? What's your first line treatment plan?
    # ... what's the proper patient education?"
    #
    # The old guard capped every lead-in at 34% symmetrically, which let
    # diagnosis sit level with management. She puts diagnosis in the minority,
    # so it now carries a tighter cap of its own while the rest keep 34%.
    skew = sum(max(0, n - len(s) * 0.34) for k, n in leads.items() if k != "diagnosis")
    skew += max(0, leads.get("diagnosis", 0) - len(s) * 0.20) * 2.5
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
    # THE DIAGNOSIS CAP IS ENFORCED BY CONSTRUCTION, not hoped for.
    #
    # Adding a diagnosis penalty to score() was not enough. score() also pays 14
    # per uncovered topic, and with 60-odd vignettes across 20-odd topics that
    # term dominates, so the optimiser kept buying topic coverage with
    # diagnosis-heavy sets -- Lecture 8 still shipped at 37% and Lecture 9 at
    # 40%, the old cap exactly. Several POOLS are themselves diagnosis-heavy
    # (Lecture 8 is 41%), and no amount of scoring fixes a pool.
    #
    # So the draw now takes at most DX_CAP diagnosis vignettes per set. If the
    # pool cannot supply enough non-diagnosis stems to fill both sets, this
    # FAILS rather than quietly shipping a skewed paper -- the honest signal
    # that more management, treatment and education vignettes need writing.
    DX_CAP = int(30 * 0.20)          # 6 of 30, matching "there might be SOME"
    dx_idx = [i for i, q in enumerate(POOL) if lead_of(q) == "diagnosis"]
    other_idx = [i for i in range(len(POOL)) if i not in set(dx_idx)]
    need_other = 60 - 2 * DX_CAP
    assert len(other_idx) >= need_other, (
        "pool has only %d non-diagnosis vignettes but two sets need %d at the %d%% cap -- "
        "write more management/treatment/education stems rather than relaxing the cap"
        % (len(other_idx), need_other, 20))

    best = None
    for _ in range(30000):
        random.shuffle(dx_idx)
        random.shuffle(other_idx)
        take_dx = dx_idx[:2 * DX_CAP]
        take_ot = other_idx[:60 - len(take_dx)]
        ch = take_dx[:DX_CAP] + take_ot[:30 - DX_CAP] + \
             take_dx[DX_CAP:] + take_ot[30 - DX_CAP:]
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
        # And diagnosis specifically stays a minority, per her 24 August
        # description of the exam: "there might be SOME question, what's the
        # most likely diagnosis, but A LOT OF THEM are ... next management
        # plan ... first line treatment ... patient education".
        dx = leads.get("diagnosis", 0)
        assert dx <= DX_CAP, ("%s carries %d diagnosis lead-ins of %d; she puts diagnosis in "
                              "the minority, cap is %d" % (name, dx, len(s), DX_CAP))
    json.dump({"set1": s1, "set2": s2}, open(os.path.join(HERE, "cms_l8_set2.json"), "w"),
              ensure_ascii=False, indent=1)
    print("wrote cms_l8_set2.json")
