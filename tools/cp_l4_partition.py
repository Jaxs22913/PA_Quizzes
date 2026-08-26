#!/usr/bin/env python3
"""Partition the Clinical Pathophysiology I Lecture 4 pool into two 30s.

House format for this course is 2x30 per topic, NO VIGNETTES, plus 5x60
cumulative masters per exam. MASTERS WAIT until the whole Exam 1 block is in.

WEBSTER'S STATED EXAM SCOPE, from the last two minutes of the 26 August
recording. He opened with "This is for the test" and named:

    cataracts | macular degeneration | the visual pathway (what change causes
    what deficit) | refraction errors | retinal detachment causes | glaucoma
    (the PATHOPHYSIOLOGICAL EXPLANATION for the vision loss)

then, after saying "that's it", went back to add PRESBYOPIA -- the lens hardens
so accommodation fails, tied to the A in PERRLA.

RECOVERING THAT LIST REQUIRED BOTH TRANSCRIPTS. Notability's ASR heard
cataracts as "catalysts" but caught it, and DROPPED GLAUCOMA ENTIRELY.
faster-whisper caught glaucoma and MISSED CATARACTS ENTIRELY. Each lost a
different topic; either alone would have shipped a guide missing a condition he
named aloud as testable. See [[lecture_transcript_cross_examine]].

Guard 4 asserts every one of the seven appears in BOTH sets.

HE ALSO CUT SCOPE, TWICE, ON THE SAME POINT. Slide 34 lists visual-field lesion
sites A-E:
    "these I wouldn't worry about that much ... this is getting more into
     neurology, which we'll see later ... KNOW THESE BETTER: optic nerve
     damage, optic chiasm damage, optic tract damage"
    "So D and E are, you know, you can know that if you want, but know A, B
     and C."
So A/B/C carry the weight and D/E are deferred. Guard 5 keeps the D/E questions
to a token presence rather than letting the partitioner load up on them.

AND HE DE-EMPHASISED LENS CORRECTION: "not that important, concave and convex
for my purposes; MORE IMPORTANT is knowing the difference between myopia,
hyperopia, and the globe shape." He also contradicted himself while saying it,
correcting mid-sentence -- both transcripts catch the "sorry, other way around".
The slide is right and the slide always wins, but no question asks which lens
corrects which. Guard 3.

THE DECK CONTRADICTS ITSELF ON NORMAL INTRAOCULAR PRESSURE -- slide 24 says
10-21 mmHg, slide 25 says "about 6-19 mmHg". Prof. Beck's PD2 deck independently
says 10-21, so 6-19 looks like the slip, but this script does not adjudicate: no
question turns on the normal value. Guard 2.

Every question is authored with its correct answer first, because choosing the
index by hand while writing is how the "always A" bug was introduced.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from cp_l4_pool_a import POOL_A
from cp_l4_pool_b import POOL_B
from cp_l4_pool_c import POOL_C
from cp_l4_pool_d import POOL_D

POOL = POOL_A + POOL_B + POOL_C + POOL_D

try:
    from cp_l4_lengthfix import FIXES
except ImportError:
    FIXES = {}
for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

# ---- Guard 1: mechanism, never management --------------------------------
# The line against CMS I, and it matters more here than in any previous Clin
# Path lecture: CMS I Exam 2 Lecture 1 covers a nearly identical condition list
# from the management side. This deck DOES put treatments on its slides -- the
# lecturer's own subtitle says "and (some) clinical concepts" -- so the rule is
# that a treatment may be stated as a fact ABOUT the disease but never asked as
# a decision.
_MGMT = re.compile(r"first[- ]line|drug of choice|treatment of choice|next step|"
                   r"most appropriate (?:treatment|management|therapy)|"
                   r"how (?:would|should) you (?:treat|manage)|what would you do|"
                   r"initial management|best (?:treatment|management)", re.I)
_mg = [q["q"][:60] for q in POOL if _MGMT.search(q["q"]) or _MGMT.search(q["opts"][q["c"]][0])]
assert not _mg, ("management-scope question in a pathophysiology pool -- that is CMS I's "
                 "half of this content: %r" % _mg[:3])

# ---- Guard 2: no question turns on the disputed pressure ------------------
_IOP = re.compile(r"\b10\s*(?:to|-|–)\s*21\b|\b6\s*(?:to|-|–)\s*19\b|"
                  r"ten to twenty-one|six to nineteen")
_bad = [q["q"][:60] for q in POOL
        if _IOP.search(q["q"]) or _IOP.search(q["opts"][q["c"]][0])]
assert not _bad, ("turns on the normal intraocular pressure, which this deck states as "
                  "10-21 on slide 24 and 6-19 on slide 25 -- no single right answer: %r" % _bad[:3])

# ---- Guard 3: no lens-choice question -------------------------------------
_LENS = re.compile(r"which lens|concave or convex|convex or concave|"
                   r"corrected with (?:a )?(?:concave|convex)", re.I)
_lens = [q["q"][:60] for q in POOL if _LENS.search(q["q"])]
assert not _lens, ("asks which lens corrects which error -- he de-emphasised it AND "
                   "contradicted himself saying it: %r" % _lens[:3])

# ---- Guard 4: his seven stated exam topics, in BOTH sets ------------------
KFE_TOPICS = {
    "cataracts":            {"Cataract"},
    "macular degeneration": {"Dry macular degeneration", "Wet macular degeneration",
                             "Macular degeneration"},
    "visual pathway":       {"Visual pathway", "Visual field defects",
                             "Optic neuropathy"},
    "refraction errors":    {"Myopia", "Hyperopia", "Astigmatism"},
    "retinal detachment":   {"Retinal detachment", "Vitreous ageing"},
    "glaucoma":             {"Glaucoma mechanism", "Open-angle glaucoma",
                             "Angle-closure glaucoma"},
    "presbyopia":           {"Presbyopia"},
}
for _name, _tops in KFE_TOPICS.items():
    _have = [q for q in POOL if q["topic"] in _tops and q.get("kfe")]
    assert len(_have) >= 4, ("he named %r for the exam but the pool has only %d "
                             "kfe-flagged questions on it -- the guide and cram sheet "
                             "build their \"Know for Exam - stated\" markers off that "
                             "flag" % (_name, len(_have)))

# The converse: nothing may be flagged kfe unless it sits under one of the seven.
# Otherwise the marker spreads and stops meaning "he said this out loud".
_KFE_ALL = set().union(*KFE_TOPICS.values())
_stray = [q["q"][:60] for q in POOL if q.get("kfe") and q["topic"] not in _KFE_ALL]
assert not _stray, ("flagged \"Know for Exam - stated\" but not on a topic he named: "
                    "%r" % _stray[:3])

# ---- Guard 5: D and E stay a token presence -------------------------------
_DE = [q for q in POOL if q["topic"] == "Visual field defects" and not q.get("kfe")]
assert len(_DE) <= 3, ("too many questions on the two lesion sites he deferred to "
                       "neurology: %d" % len(_DE))

SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260826 + 4)
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
ALL_TOPICS = set(q["topic"] for q in POOL)


def kfe_missing(setqs):
    """How many of his seven named topics are absent from this set."""
    have = set(q["topic"] for q in setqs)
    return sum(1 for tops in KFE_TOPICS.values() if not (tops & have))


def score(setqs):
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    missing_io = len(ALL_IOS - set(ios))
    lumpy = sum(max(0, n - 6) for n in ios.values())
    lumpy_t = sum(max(0, n - 3) for n in tops.values())
    lumpy_s = sum(max(0, n - 9) for n in slots.values())
    # a missing exam-list topic is the most expensive thing that can happen
    return (kfe_missing(setqs) * 120 + missing_io * 30 + lumpy * 3 + lumpy_t * 2
            + lumpy_s * 2 + gameable_pct(setqs) * 1.2)


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
    return bad


if __name__ == "__main__":
    print("pool size:", len(POOL), " kfe-flagged:", sum(1 for q in POOL if q.get("kfe")))
    print("schema problems:", validate(POOL) or "none")
    print("objectives:", len(ALL_IOS), " topics:", len(ALL_TOPICS))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("Webster checks: mechanism-only OK, disputed pressure unused OK, "
          "no lens-choice question OK, all 7 stated exam topics present, "
          "D/E deferred (%d questions)" % len(_DE))
    print()

    answer_text = {id(q): q["opts"][q["c"]][0] for q in POOL}
    best = None
    idx = list(range(len(POOL)))
    for _ in range(40000):
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
    print("rotation check: every correct answer still points at its own text")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        assert kfe_missing(s) == 0, ("%s is missing one of the topics he named for the "
                                     "exam" % name)
    print("exam-list check: both sets cover all seven topics he named aloud\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions %s  gameable %.1f%%  objectives %d  topics %d  kfe %d"
              % (name, len(s), dict(sorted(pos.items())), gameable_pct(s),
                 len(set(q["io"] for q in s)), len(set(q["topic"] for q in s)),
                 sum(1 for q in s if q.get("kfe"))))

    with open(os.path.join(HERE, "cp_l4_sets.json"), "w", encoding="utf-8") as fh:
        json.dump({"set1": s1, "set2": s2}, fh, ensure_ascii=False, indent=1)
    print("\nwrote cp_l4_sets.json")
