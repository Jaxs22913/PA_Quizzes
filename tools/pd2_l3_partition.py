#!/usr/bin/env python3
"""Partition the PD2 Lecture 3 (Advanced Ocular Examination) pool into two 30s.

BECK'S SKIP INSTRUCTIONS ARE BINDING. Jaxon, 2026-08-26: "if she says don't
worry about a slide then she won't test on it so no need to include it." That
is stronger than ordinary de-emphasis -- it removes the slide from scope -- and
it is why this lecture was NOT built from the deck alone. The deck cannot say
which slides she cut, so a deck-only build would have quizzed material she has
excluded, which is the one error that wastes a student's time outright.

SIX THINGS ARE OUT, each with her words:

  1. THE NAMED VIRUS in viral conjunctivitis. "I'm not gonna test you on it, but
     adenovirus..." -- she uses it for the great-mimicker story only.
     NOTE: CMS I Exam 2 DOES test adenovirus. Different course, different scope,
     and this guard must not be copied there.
  2. THE EXOPHTHALMOMETER, technique and its 20-22 mm figure. "I am not going to
     test you on the minutia of how to do that test ... don't sit there and
     [think] I have so much to memorize, it was 20 to 22 millimetres -- don't
     worry about it." Recognising exophthalmos, and the stand-behind-and-look-
     down technique, are still IN.
  3. THE STRABISMUS DIAGRAM. "This is just a visual ... that you don't have to
     memorize." Eso/exo/hypertropia as concepts remain in.
  4. THE CORNEAL REFLECTION TEST. "We've already done this, so I'm not gonna
     test you on it ... we already did that in PD1."
  5. THE ADIE'S PUPIL ASSOCIATIONS SLIDE -- dysautonomia, Shy-Drager, diabetes,
     amyloidosis. "It's not on my test this time ... I'm not gonna nitpick you
     on that." ADIE'S PUPIL ITSELF IS IN: "you should know Adie's pupil, that
     could be on my test."
  6. THE LATIN EXPANSIONS of OD/OS/OU. "I don't care if you remember Oculus
     Sinister or Dexter." THE ABBREVIATIONS ARE IN: "those are terms that you
     must remember."

AND ONE THING IS IN BOTH SETS BY ASSERTION: the RED-EYE COMPARISON CHART on
slide 48. It extracts as completely blank -- it is a picture of the Bates table
-- and was recovered with tools/ocr_deck_images.py. Beck then said "I genuinely
think it's important that you are very familiar with that chart." A build that
dropped it would miss the slide she emphasised most.

House rules for this course also apply: no question may depend on having the
deck open, and none may be about course mechanics.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pd2_l3_pool_a import POOL_A
from pd2_l3_pool_b import POOL_B
from pd2_l3_pool_c import POOL_C

POOL = POOL_A + POOL_B + POOL_C

try:
    from pd2_l3_lengthfix import FIXES
except ImportError:
    FIXES = {}
for (_qi, _oi), _txt in FIXES.items():
    _q = POOL[_qi]
    assert _oi != _q["c"], "length fix %d/%d targets the CORRECT option" % (_qi, _oi)
    _q["opts"][_oi][0] = _txt

# ---- Guard 1: the six things Beck took out of scope ------------------------
# Each entry is (label, regex). A stem or a CORRECT answer matching one is
# testing something she said she would not test.
_EXCLUDED = [
    ("the named virus (adenovirus)", r"\badenovirus\b"),
    ("the exophthalmometer and its 20-22 mm figure",
     r"exophthalmomet|\b20\s*(?:to|-|–)\s*22\s*(?:mm|millimet)"),
    ("the corneal reflection test", r"corneal reflection"),
    ("the Adie's pupil ASSOCIATIONS slide",
     r"shy[- ]drager|multiple system atrophy|dysautonomia|amyloidosis"),
    ("the Latin expansions of OD/OS/OU", r"oculus (?:dexter|sinister|uterque)"),
]
_bad = []
for _q in POOL:
    _hay = _q["q"] + " " + _q["opts"][_q["c"]][0]
    for _label, _rx in _EXCLUDED:
        if re.search(_rx, _hay, re.I):
            _bad.append((_label, _q["q"][:55]))
assert not _bad, ("tests something Beck said she would NOT test -- her skip "
                  "instructions are binding: %r" % _bad[:3])

# The strabismus DIAGRAM is out, but the concepts are in. Catch only a question
# that asks about the picture itself.
_diag = [q["q"][:55] for q in POOL
         if re.search(r"which (?:image|picture|figure|diagram)|on the diagram|"
                      r"in the illustration", q["q"], re.I)]
assert not _diag, ("asks about a diagram rather than a concept -- she said the "
                   "strabismus visual does not have to be memorised: %r" % _diag[:3])

# ---- Guard 2: PD2 house rules ---------------------------------------------
_CTX = re.compile(r"on (?:this|the) slide|the slide (?:shows|says)|as shown (?:above|below)|"
                  r"in the (?:image|photo|figure) (?:above|below)|the deck's own", re.I)
assert not [q for q in POOL if _CTX.search(q["q"])], "question depends on having the deck open"
_MECH = re.compile(r"how many (?:points|questions) is|when is the exam|"
                   r"office hours|grading|syllabus says|attendance", re.I)
assert not [q for q in POOL if _MECH.search(q["q"])], "course-mechanics question in the pool"

# ---- Guard 3: the chart she emphasised must survive into both sets ---------
_CHART = [i for i, q in enumerate(POOL) if q.get("chart")]
assert len(_CHART) >= 8, ("Beck singled out the red-eye chart -- the pool needs enough "
                          "chart questions to put some in both sets, found %d" % len(_CHART))

SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")
for _q in POOL:
    assert _q.get("slot") in SLOTS, "bad or missing slot on: %s" % _q["q"][:70]

random.seed(20260826 + 33)
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


def score(setqs):
    tops = Counter(q["topic"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    nchart = sum(1 for q in setqs if q.get("chart"))
    # she emphasised the chart: want 3-5 of its questions in each set
    chart_pen = abs(4 - nchart) * 25
    lumpy_t = sum(max(0, n - 2) for n in tops.values())
    lumpy_s = sum(max(0, n - 6) for n in slots.values())
    thin_slots = max(0, 10 - len(slots))
    return (chart_pen + thin_slots * 15 + lumpy_t * 3 + lumpy_s * 2
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
    return bad


if __name__ == "__main__":
    print("pool size:", len(POOL), " topics:", len(ALL_TOPICS))
    print("schema problems:", validate(POOL) or "none")
    print("red-eye chart questions available:", len(_CHART))
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("Beck checks: none of her six excluded items appears; no deck-dependent or "
          "course-mechanics question")
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
        nc = sum(1 for q in s if q.get("chart"))
        assert nc >= 2, "%s has only %d red-eye chart questions -- she emphasised it" % (name, nc)
    print("chart check: both sets carry the red-eye comparison chart\n")

    for name, s in (("SET 1", s1), ("SET 2", s2)):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions %s  gameable %.1f%%  topics %d  slots %d  chart %d"
              % (name, len(s), dict(sorted(pos.items())), gameable_pct(s),
                 len(set(q["topic"] for q in s)), len(set(q["slot"] for q in s)),
                 sum(1 for q in s if q.get("chart"))))

    with open(os.path.join(HERE, "pd2_l3_sets.json"), "w", encoding="utf-8") as fh:
        json.dump({"set1": s1, "set2": s2}, fh, ensure_ascii=False, indent=1)
    print("\nwrote pd2_l3_sets.json")
