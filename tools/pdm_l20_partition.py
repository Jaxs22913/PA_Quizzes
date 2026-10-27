#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 20 (Pulmonary Function Testing and Oxygenation, Professor Fowler) pool into two 30s.

House format is 2x30 for the lecture. The remainder is held back for the cumulative Exam 4 master forms
(Lectures 17-21 and Labs 4-5), which wait until the block is complete.

RULES, asserted rather than trusted:
  1. A value in a STEM always carries its normal range or its reference value ("(normal 80% to 100%)",
     "of predicted", "reference"). Nothing is calculated (the ratio is always given, never asked for).
  2. No abbreviation in an option. In a stem or explanation an abbreviation appears only as
     ABBREV (full term), every time ("FEV1/FVC (forced expiratory volume in one second over forced vital
     capacity) ratio"); NOT is emphasis, not an abbreviation.
  3. Every stem names the patient's age, asks one thing, and never cites the course.
  4. Pictures: every set carries MIN_IMG to MAX_IMG, never the same picture twice in one set, and every
     picture exists on disk with alt text and a slide caption; the alt text never names the key.
  5. No option set is numeric (WRITER.md rule 8 would fix its order); asserted.

EMPHASIS (the 26 October recording, two segments, 62 minutes; minutes spoken per objective, measured on our
faster-whisper transcript and read against Notability's): objective a (the parameters: equipment,
plethysmography, the volumes and capacities with the class breathing them, spirometry, the forced values,
the curves and loops) about 27 minutes; objective c (the three physiologies, the disease lists, the
obstructive and restrictive curves and loops, the loop variations) about 16; objective d (normal values, the
result table, the algorithm, the basic interpretation) about 6; objective f (the pulse oximeter, exercise
oximetry, the walk test) about 4; objective b (indications) about 3; objective e (what the tests measure,
the standard tests' roles) about 3; the introduction about 3. The recording ENDS as the cases begin (1:02:09, "this represents three
different patients"): slides 46 to 57 (Cases 1 to 3) have no audio and are weighted by the slides alone.
Objective d is lifted above its spoken minutes (5 to 6 a set) because interpretation is the vignette core of
this class and twelve unspoken slides are cases; objective a is held to 10 to 11 so every objective is asked.
Spoken cues that point at slide facts: plethysmography ("this is important"; the residual volume "the key
thing"); the spirometry tracing ("I want you to see [it] in your sleep"); the three most important values
(the forced vital capacity, the one-second volume and their ratio, "the most important part of interpreting
PFTs"); "70% is your marker" ("Pay attention to this", Notability); "if there's a scoop in the loop, there's
obstruction"; the restrictive loop as a witch's hat, "volume is less ... the key thing to remember";
bronchiectasis ("remember this"). Each cue group is carried by EACH set where the pool has two or more items
for it, otherwise by one of the sets. De-emphasis: the incentive spirometer's piston ("Don't worry about
this"), the diffusing-capacity procedure ("we're not going to focus in on that today"), the normal-values
table ("I'm not going to be digging into this"): none is asked; normal ranges are always supplied.

Selection is swap-based local search, as on the Lecture 17 build. Target under 10% gameable per set.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
sys.path.insert(0, HERE)
from pdm_l20_pool_a import POOL_A, SRC, IOA, IOB, IOC, IOD, IOE, IOF
from pdm_l20_pool_b import POOL_B
from _option_order import ordered_kind

POOL = POOL_A + POOL_B
SEED, NOPT, BAR, TARGET, PER_SET = 20261026, 4, 0.35, 0.10, 30
MIN_IMG, MAX_IMG = 10, 13
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
IOS = [IOA, IOB, IOC, IOD, IOE, IOF]

CITES = re.compile(r"(?i)\b(lecture|lecturer|slides?|deck|professor|this course|in class|syllabus|fowler|reynolds)\b")
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"NOT", "WITHOUT", "MAXIMAL", "OUT", "TOTAL", "LOW", "NON", "AND"}            # capitals for emphasis, not abbreviations
_DEFINED = re.compile(r"(?:/[A-Z][A-Za-z0-9]*)* \(")                       # FEV1/FVC (... or COPD (...
_DURATION = re.compile(r"\b\d+ (?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)\b")
_ABBR_WITH_DIGIT = re.compile(r"\b[A-Z]{2,}\d\b")                          # FEV1 is a name, not a value
_HAS_RANGE = re.compile(r"\(normal |of predicted|predicted value|reference")


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert len(ids) == 1, "stem prefix matches %d items: %s" % (len(ids), p)
    return ids[0]


def stems(*ps):
    return [stem(p) for p in ps]


def _io(io): return lambda q: q["io"] == io
def _tp(*ts): return lambda q: q["topic"] in ts
GROUPS = [
    ("objective a", _io(IOA), 10, 11),
    ("objective b", _io(IOB), 2, 2),
    ("objective c", _io(IOC), 8, 9),
    ("objective d", _io(IOD), 5, 6),
    ("objective e", _io(IOE), 2, 3),
    ("objective f", _io(IOF), 2, 2),
    ("equipment", _tp("Equipment"), 1, 2),
    ("lung volumes", _tp("Lung volumes"), 1, 2),
    ("lung capacities", _tp("Lung capacities"), 1, 2),
    ("spirometry technique", _tp("Spirometry technique"), 1, 1),
    ("spirometry values", _tp("Spirometry values"), 2, 3),
    ("restrictive physiology", _tp("Restrictive physiology"), 1, 2),
    ("the two patients", _tp("The two patients"), 1, 1),
    ("volume-time curves", _tp("Volume-time curves"), 1, 2),
    ("flow-volume loops", _tp("Flow-volume loops"), 2, 4),
    ("result tables", _tp("Result tables"), 1, 1),
    ("stepwise read", _tp("Stepwise read"), 2, 2),
    ("basic interpretation", _tp("Basic interpretation"), 1, 2),
    ("reports", _tp("Reports"), 1, 2),
    ("standard tests", _tp("Standard tests"), 1, 1),
]

TRACINGS = stems("A 40-year-old has this tracing", "A 55-year-old has this tracing", "A 33-year-old has this tracing",
                 "A 62-year-old has this tracing")
# near-twins that give each other away (stem, key or explanation): at most N per set
CLUSTERS = [
    (1, TRACINGS),
    (1, stems("A 26-year-old woman breathing quietly", "A 33-year-old has this tracing")),
    (1, stems("A 52-year-old woman breathes out normally", "A 62-year-old has this tracing")),
    (1, stems("A 34-year-old man takes a maximal breath", "A 41-year-old woman's spirometry records")),
    (1, stems("A 41-year-old woman's spirometry records", "A 44-year-old's volume-time curve")),
    (1, stems("A 24-year-old woman with asthma", "A 31-year-old man with asthma")),
    (1, stems("A 58-year-old man with dyspnea needs", "A 47-year-old woman sits inside")),
    (1, stems("A 46-year-old woman has bronchiectasis", "A 19-year-old man with cystic fibrosis")),
    (1, stems("A 45-year-old man has sarcoidosis", "A 70-year-old man with COPD")),
    (2, stems("A 69-year-old woman's flow-volume loop", "A 61-year-old man's flow-volume loop", "A 35-year-old man's flow-volume loop")),
    (1, stems("A 69-year-old woman's flow-volume loop", "A 66-year-old man's flow-volume loop", "A 64-year-old woman's spirometry report")),
    (1, stems("A 61-year-old man's flow-volume loop", "A 60-year-old man's flow-volume loop")),
    (1, stems("A 54-year-old woman's volume-time curve", "A 49-year-old's volume-time curve")),
    (1, stems("A 74-year-old woman's flow-volume loop", "A 70-year-old's volume-time curve", "A 63-year-old man's volume-time curve")),
    (2, stems("A 57-year-old's volume-time curve", "A 70-year-old's volume-time curve", "A 49-year-old's volume-time curve")),
    (2, stems("A 48-year-old woman's FEV1", "A 71-year-old man's FEV1", "A 44-year-old woman's FEV1", "A 35-year-old man's FEV1")),
    (1, stems("A 57-year-old woman's total lung capacity", "A 69-year-old man's FEV1")),
    (1, stems("A 32-year-old woman who trains", "A 32-year-old woman with a restrictive")),
    (1, stems("A 32-year-old woman with a restrictive", "A 15-year-old boy")),
    (1, stems("A 59-year-old woman with pulmonary hypertension", "A 32-year-old woman with a restrictive")),
    (1, stems("A 59-year-old woman with pulmonary hypertension", "A 63-year-old man's spirometry suggests", "A 54-year-old smoker")),
    (1, stems("A 44-year-old woman's FEV1", "A 63-year-old man's spirometry suggests")),
    (1, stems("A 44-year-old woman's FEV1", "A 63-year-old man's forced vital capacity")),
    (1, stems("A 34-year-old woman has a chest wall", "A clinician asks whether")),
    (1, stems("A 64-year-old man has taken amiodarone", "A 38-year-old woman with an autoimmune")),
    (1, stems("A 79-year-old woman with lung disease", "A 58-year-old man's clinician")),
    (1, stems("A 65-year-old man with dyspnea has standard", "A 54-year-old smoker")),
]

# the lecturer's emphasis cues: each set carries one of the group (EACH), or the pair of sets does (ANY)
EACH = [
    ("the ratio, 70% the marker", stems("A 58-year-old man's forced breath", "A 66-year-old man with emphysema",
                                        "A 48-year-old woman's FEV1", "A 71-year-old man's FEV1", "A 56-year-old smoker")),
    ("scoop in the loop", stems("A 69-year-old woman's flow-volume loop", "A 66-year-old man's flow-volume loop",
                                "A 64-year-old woman's spirometry report", "A 74-year-old woman's flow-volume loop")),
    ("witch's hat", stems("A 61-year-old man's flow-volume loop", "A 60-year-old man's flow-volume loop")),
    ("restriction: the volume is less", stems("A 54-year-old woman's volume-time curve", "A 49-year-old's volume-time curve",
                                              "A 60-year-old man's flow-volume loop")),
    ("the spirometry tracing", TRACINGS),
    ("plethysmography", stems("A 58-year-old man with dyspnea needs", "A 47-year-old woman sits inside")),
    ("the forced values", stems("A 29-year-old student", "A 41-year-old woman's spirometry records", "A 44-year-old's volume-time curve",
                                "A 34-year-old man takes a maximal breath")),
]
ANY = [
    ("bronchiectasis", stems("A 46-year-old woman has bronchiectasis")),
]


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def _acronyms_ok(txt):
    bad = []
    for m in _ACRO.finditer(txt):
        a = m.group(0)
        if a in _ACRO_OK:
            continue
        if not _DEFINED.match(txt, m.end()):
            # inside a compound such as FEV1/FVC, the first part is defined by the bracket after the last part
            tail = txt[m.end():]
            if not re.match(r"(?:/[A-Z][A-Za-z0-9]*)+ \(", tail):
                bad.append(a)
    return bad


def check(pool):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d] %s" % (i, q["q"][:50])
        k = q["c"]
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert k == 0, "%s: key must be authored first" % w
        assert not ordered_kind([o[0] for o in q["opts"]]), "%s: numeric option set would be rotated" % w
        assert q["io"] in IOS, w
        assert q["q"].rstrip().endswith("?"), "%s: stem asks nothing" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert _AGE.search(q["q"]), "%s: stem names no patient" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not _CALC.search(q["q"]), "%s: stem asks for a calculation" % w
        bare = _ABBR_WITH_DIGIT.sub("", _DURATION.sub("", _AGE.sub("", q["q"])))
        if re.search(r"\d", bare):
            assert _HAS_RANGE.search(q["q"]), "%s: value without its normal range or reference" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        texts = [o[0].lower() for o in q["opts"]]
        for a in texts:
            for b in texts:
                assert a == b or a not in b, "%s: option %r contains option %r" % (w, b, a)
        assert q["opts"][k][1].startswith("Correct"), "%s: key explanation must open Correct" % w
        for j, (t, e) in enumerate(q["opts"]):
            assert len(t) <= 66, "%s: option over 66 characters: %r" % (w, t)
            assert not CITES.search(t), "%s: option cites the course" % w
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            assert not [a for a in _ACRO.findall(t) if a not in _ACRO_OK], "%s: abbreviation in option %r" % (w, t)
            if j != k:
                assert not e.startswith("Correct"), "%s: distractor explanation opens Correct" % w
                assert t in q.get("mis", {}), "%s: no mis label for %r" % (w, t)
        assert set(q.get("mis", {})) == {o[0] for j, o in enumerate(q["opts"]) if j != k}, "%s: mis labels do not match" % w
        assert re.match(re.escape(SRC) + r", Slides? \d", q.get("cite", "")), w
        for where, txt in [("stem", q["q"])] + [("explanation", o[1]) for o in q["opts"]]:
            bad = _acronyms_ok(txt)
            assert not bad, "%s: undefined abbreviation %r in %s" % (w, bad, where)
        if "img" in q:
            assert os.path.exists(os.path.join(FOLDER, q["img"])), "%s: missing %s" % (w, q["img"])
            assert re.match(r"pdm-exam-4-quiz-images/l20-fig-\d\d\.jpg$", q["img"]), "%s: picture name must be a number" % w
            assert q.get("alt") and q.get("slide", "").startswith("Slide "), w
            assert q["opts"][k][0].lower() not in q["alt"].lower(), "%s: alt text gives the answer away" % w


def score_set(sel):
    qs = [POOL[i] for i in sel]
    g = sum(gameable(q["opts"], q["c"]) for q in qs) / len(qs)
    s = max(0.0, g - TARGET) * 100
    for _, pred, lo, hi in GROUPS:
        k = sum(1 for q in qs if pred(q))
        s += 3 * (max(0, lo - k) + max(0, k - hi))
    imgs = [q["img"] for q in qs if "img" in q]
    s += 3 * (max(0, MIN_IMG - len(imgs)) + max(0, len(imgs) - MAX_IMG))
    s += 4 * (len(imgs) - len(set(imgs)))
    ss = set(sel)
    for mx, ids in CLUSTERS:
        s += 4 * max(0, len(ss & set(ids)) - mx)
    for _, ids in EACH:
        s += 4 * (not (ss & set(ids)))
    return s


def score(sel):
    v = score_set(sel[:PER_SET]) + score_set(sel[PER_SET:])
    both = set(sel)
    for _, ids in ANY:
        v += 4 * (not (both & set(ids)))
    return v


def rotate(qs, rng, k):
    """Balance key positions across A-D (no ordered items in this pool)."""
    want = [len(qs) // NOPT] * NOPT
    extra = list(range(NOPT)); rng.shuffle(extra)
    for p in extra[:len(qs) % NOPT]:
        want[p] += 1
    slots = [p for p in range(NOPT) for _ in range(want[p])]
    rng.shuffle(slots)
    out = []
    for q, want_p in zip(qs, slots):
        r = {kk: vv for kk, vv in q.items() if kk != "slot"}
        o = list(q["opts"]); key = o.pop(0); rng.shuffle(o); o.insert(want_p, key)
        r["opts"] = o; r["c"] = want_p
        out.append(r)
    pos = Counter(q["c"] for q in out)
    assert max(pos.values()) - min(pos.values()) <= 1, "set%d: uneven positions %r" % (k, pos)
    return out


def main():
    rng = random.Random(SEED)
    check(POOL)
    n = len(POOL)
    assert n >= PER_SET * 2, "pool of %d cannot fill two sets of %d" % (n, PER_SET)
    best = None
    for _ in range(400):
        idx = list(range(n)); rng.shuffle(idx)
        s = idx[:PER_SET * 2]
        v = score(s)
        if best is None or v < best[0]:
            best = (v, s)
    v, sel = best
    rest = [i for i in range(n) if i not in sel]
    for _ in range(150000):
        a = rng.randrange(PER_SET * 2)
        if rest and rng.random() < 0.5:
            b = rng.randrange(len(rest))
            new = sel[:]; new[a], nr = rest[b], sel[a]
            nv = score(new)
            if nv <= v:
                sel, v = new, nv; rest[b] = nr
        else:
            b = rng.randrange(PER_SET * 2)
            new = sel[:]; new[a], new[b] = new[b], new[a]
            nv = score(new)
            if nv <= v:
                sel, v = new, nv
    assert v < 1, "partition could not meet every constraint (score %.2f)" % v

    sets = {}
    for k, part in ((1, sel[:PER_SET]), (2, sel[PER_SET:])):
        qs = [POOL[i] for i in part]
        rot = rotate(qs, rng, k)
        pos = Counter(q["c"] for q in rot)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        assert frac <= BAR, "set%d: gameable %.0f%%" % (k, frac * 100)
        io = Counter("abcdef"[IOS.index(q["io"])] for q in rot)
        sets["set%d" % k] = rot
        print("set%d  %d questions  pictures=%d  positions=%s  gameable=%.1f%%  topics=%d  objectives=%s"
              % (k, len(rot), sum("img" in q for q in rot), {chr(65 + p): c for p, c in sorted(pos.items())},
                 frac * 100, len({q["topic"] for q in rot}), dict(sorted(io.items()))))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l20_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], q["c"]) for q in POOL) / n
    print("pool %d (%d pictures, raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, sum("img" in q for q in POOL), raw * 100, os.path.basename(out), len(held)))
    for q in held:
        print("  held: %s" % q["q"][:90])


if __name__ == "__main__":
    main()
