#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 20 (Point-of-Care Ultrasound and Diagnostic Integration, Jordan Stores, PA-C) pool
into two 30s.

House format is 2x30 for the lecture. The remainder is held back for the cumulative Exam 4 master forms
(Lectures 17-21), which wait until the block is complete.

RULES, asserted rather than trusted:
  1. No number in a STEM except an age or a duration, unless it carries its normal or reference range (vital
     signs are given in words). Nothing is calculated.
  2. No abbreviation in an option. In a stem or explanation an abbreviation appears only as ABBREV (full term),
     every time; capitals for emphasis and the slide's word-mnemonic BART are allowed.
  3. Every stem names the patient's age, asks one thing, and never cites the course.
  4. Pictures: every set carries MIN_IMG to MAX_IMG, never the same picture twice in one set, every picture exists
     on disk under a neutral number with alt text and a slide caption; the alt text never names the key.
  5. No option set is numeric (WRITER.md rule 8 would fix its order); asserted.

EMPHASIS (17 November recording, both parts read; see the .flags.md beside the recordings): EACH set carries one item on lung sliding and the lung point, compressibility for a deep vein thrombosis, B lines for pulmonary edema, subxiphoid for pericardial effusion, color Doppler direction, and mirror image/spine sign; the PAIR of sets carries the indicator, Morison's pouch, cobblestoning, the inferior vena cava collapse, the lung probes and the frequency trade-off. Played down aloud (probe movements, ring-down, side lobe): AVOID, a soft cost.

Selection is swap-based local search, as on the Lecture 18 (pulmonary function) build. Target under 10% gameable
per set.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
sys.path.insert(0, HERE)
from pdm_pocus_pool_a import POOL_A, SRC, IOA, IOB, IOC, IOD, IOE1, IOE2, IOE3, IOE4, IOF
from pdm_pocus_pool_b import POOL_B
from _option_order import ordered_kind

POOL = POOL_A + POOL_B
SEED, NOPT, BAR, TARGET, PER_SET = 20261117, 4, 0.35, 0.10, 30
MIN_IMG, MAX_IMG = 10, 13
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
IOS = [IOA, IOB, IOC, IOD, IOE1, IOE2, IOE3, IOE4, IOF]
IO_TAG = ["a", "b", "c", "d", "e.i", "e.ii", "e.iii", "e.iv", "f"]

CITES = re.compile(r"(?i)\b(lecture|lecturer|deck|professor|this course|in class|syllabus|stores|reynolds)\b|\b(?:the|this|that|each|on) slides?\b|slide's")   # "slide" alone is a probe movement
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"NOT", "WITHOUT", "RIGHT", "LEFT", "BOTH", "ABOLISHED", "BRIGHTER", "BEHIND", "VERTICAL", "LUNG", "OPPOSITE", "LESS", "BARRIER",
            "FLUID", "DARK", "BRIGHT", "ABOVE", "NORMAL",
            "BART"}   # capitals for emphasis; BART is the slide's own word-mnemonic (blue away, red towards)            # capitals for emphasis, not abbreviations
_DEFINED = re.compile(r"(?:/[A-Z][A-Za-z0-9]*)* \(")                       # FEV1/FVC (... or COPD (...
_DURATION = re.compile(r"\b\d+ (?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)\b")
_ABBR_WITH_DIGIT = re.compile(r"\b[A-Z]{2,}\d\b")                          # FEV1 is a name, not a value
_HAS_RANGE = re.compile(r"\(normal |reference range")


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert len(ids) == 1, "stem prefix matches %d items: %s" % (len(ids), p)
    return ids[0]


def stems(*ps):
    return [stem(p) for p in ps]


def _io(io): return lambda q: q["io"] == io
def _tp(*ts): return lambda q: q["topic"] in ts
GROUPS = [
    ("objective a", _io(IOA), 2, 3),
    ("objective b", _io(IOB), 2, 3),
    ("objective c", _io(IOC), 6, 8),
    ("objective d", _io(IOD), 9, 11),
    ("objective e.i cardiac", _io(IOE1), 3, 5),
    ("objective e.ii pulmonary", _io(IOE2), 2, 3),
    ("objective e.iii abdominal", _io(IOE3), 2, 3),
    ("objective e.iv soft tissue", _io(IOE4), 1, 2),
    ("objective f", _io(IOF), 2, 2),
    ("echogenicity", _tp("Echogenicity"), 2, 3),
    ("artifacts", _tp("Artifacts"), 4, 6),
    ("cardiac windows", _tp("Cardiac windows"), 3, 5),
    ("lung findings", _tp("Lung findings"), 2, 4),
    ("gallbladder", _tp("Gallbladder"), 1, 2),
    ("vessels", _tp("Vessels"), 1, 2),
    ("protocols", _tp("Protocols"), 1, 2),
]

# near-twins that give each other away (stem, key or explanation): at most N per set
CLUSTERS = [
    (1, stems("A 34-year-old man has this right upper quadrant", "A 24-year-old woman is hypotensive")),
    (1, stems("A 42-year-old woman has this lung ultrasound", "A 25-year-old man has this chest wall")),
    (2, stems("A 66-year-old woman with dyspnea has this lung", "A 77-year-old woman with orthopnea", "A 78-year-old man in acute",
              "A 68-year-old man with long-untreated hypertension")),
    (1, stems("A 31-year-old woman has chest pain after a fall", "A 22-year-old man has sudden chest pain")),
    (1, stems("A 67-year-old woman has this right upper quadrant", "A 71-year-old man's right upper quadrant")),
    (1, stems("A 59-year-old woman has gallstones", "A 64-year-old man has this right upper quadrant")),
    (1, stems("A 64-year-old man has this right upper quadrant", "A 49-year-old woman has right upper quadrant pain")),
    (2, stems("A 45-year-old woman's bedside scan shows gallstones", "A 49-year-old woman has right upper quadrant pain",
              "A 56-year-old man has right upper quadrant pain", "A 60-year-old woman has right upper quadrant pain")),
    (1, stems("A 53-year-old man's gallbladder wall", "A 55-year-old man has this transverse")),
    (1, stems("A 76-year-old man's liver ultrasound", "A 76-year-old man has this liver")),
    (1, stems("A 41-year-old man needs a superficial", "A 68-year-old woman with a large")),
    (1, stems("A 79-year-old woman with vomiting", "A 74-year-old man is hypotensive after days")),
    (2, stems("A 32-year-old man is hypotensive after a motorcycle", "A 28-year-old woman is scanned after blunt",
              "A 41-year-old man is scanned in the right upper", "A 30-year-old man is hypotensive after a fall")),
    (1, stems("A 30-year-old man is hypotensive after a fall", "A 24-year-old woman is hypotensive")),
    (1, stems("A 55-year-old man with sudden dyspnea needs his right", "A 61-year-old man has this focused")),
    (1, stems("A 47-year-old woman's clinician obtains", "A 66-year-old man has a cardiac scan", "A 70-year-old man has this focused")),
    (1, stems("A 51-year-old woman's clinician starts", "A 64-year-old woman has this focused")),
    (1, stems("A 73-year-old woman is hypotensive and a pericardial", "A 52-year-old woman has this focused")),
    (1, stems("A 26-year-old man is checked for a pneumothorax", "A 69-year-old woman with dyspnea is scanned")),
    (1, stems("A 33-year-old woman has a tender", "A 29-year-old man's soft tissue")),
    (2, stems("A 63-year-old woman has a swollen leg", "A 59-year-old man's leg scan", "A 66-year-old woman's leg vein")),
    (1, stems("A 44-year-old woman has had one swollen", "A 59-year-old man on a surgical ward")),
    (1, stems("A 47-year-old woman's color Doppler", "A 58-year-old man's color Doppler")),
    (1, stems("A 44-year-old woman is scanned for a general", "A 52-year-old man has a cardiac point-of-care")),
    (1, stems("A 36-year-old man's ultrasound image looks", "A 49-year-old woman is being scanned")),
    (1, stems("A 30-year-old pregnant woman", "A 63-year-old man's standard bedside")),
    (1, stems("A 63-year-old man with fever and cough", "A 58-year-old woman with pneumonia")),
    (2, stems("A 47-year-old man in the emergency department", "A 62-year-old woman has a comprehensive",
              "A 38-year-old woman's bedside ultrasound")),
    (1, stems("A 26-year-old student asks", "A 31-year-old woman asks why")),
    (1, stems("A 29-year-old man has blunt trauma", "A 45-year-old man arrives in cardiac arrest")),
    (3, stems("A 46-year-old man's bladder appears", "A 58-year-old woman's ultrasound shows a gallstone",
              "A 35-year-old man's liver and spleen", "A 61-year-old woman's mass", "A 34-year-old man has this right upper quadrant")),
]

# the lecturer's emphasis cues: each set carries one of the group (EACH), or the pair of sets does (ANY)
EACH = [
    ("lung sliding; the lung point rules a pneumothorax in", stems("A 31-year-old woman has chest pain after a fall",
        "A 22-year-old man has sudden chest pain", "A 28-year-old man with sudden dyspnea")),
    ("compressibility is the deep vein thrombosis test", stems("A 63-year-old woman has a swollen leg",
        "A 59-year-old man's leg scan", "A 54-year-old woman needs ultrasound-guided")),
    ("B lines mean pulmonary edema", stems("A 66-year-old woman with dyspnea has this lung", "A 77-year-old woman with orthopnea",
        "A 78-year-old man in acute", "A 68-year-old man with long-untreated hypertension")),
    ("subxiphoid is the pericardial effusion view", stems("A 73-year-old woman is hypotensive and a pericardial",
        "A 32-year-old man is hypotensive after a motorcycle", "A 52-year-old woman has this focused")),
    ("color Doppler: red toward, blue away, not artery and vein", stems("A 47-year-old woman's color Doppler",
        "A 58-year-old man's color Doppler")),
    ("mirror image, and its absence with the spine sign", stems("A 48-year-old man has this right upper quadrant",
        "A 67-year-old woman has this right upper quadrant", "A 71-year-old man's right upper quadrant")),
]
ANY = [
    ("indicator on the left, the patient's right", stems("A 44-year-old woman is scanned for a general")),
    ("Morison's pouch", stems("A 24-year-old woman is hypotensive")),
    ("cobblestoning", stems("A 40-year-old man has a red, warm")),
    ("inferior vena cava collapse over 50%", stems("A 79-year-old woman with vomiting", "A 74-year-old man is hypotensive after days")),
    ("linear up high, curvilinear low", stems("A 26-year-old man is checked for a pneumothorax", "A 69-year-old woman with dyspnea is scanned")),
    ("frequency trade-off", stems("A 41-year-old man needs a superficial", "A 68-year-old woman with a large")),
]
# failed audit twice (judges reject the picture-title grounding): never in the lecture sets
HOLD = stems("A 25-year-old man has this chest wall",
             # still failing audit after their one repair (WRITER.md: hold, replace)
             "A 26-year-old man is checked for a pneumothorax", "A 67-year-old woman has this right upper quadrant")
# played down aloud ("read on your own", "won't spend a lot of time"): a soft cost, never banned
AVOID = stems("A 57-year-old man is scanned while", "A 76-year-old man's liver ultrasound", "A 76-year-old man has this liver",
              "A 72-year-old woman has this gallbladder")



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
            assert re.match(r"pdm-exam-4-quiz-images/pocus-fig-\d\d\.jpg$", q["img"]), "%s: picture name must be a number" % w
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
    s += 1 * len(ss & set(AVOID))
    s += 100 * len(ss & set(HOLD))
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
        io = Counter(IO_TAG[IOS.index(q["io"])] for q in rot)
        sets["set%d" % k] = rot
        print("set%d  %d questions  pictures=%d  positions=%s  gameable=%.1f%%  topics=%d  objectives=%s"
              % (k, len(rot), sum("img" in q for q in rot), {chr(65 + p): c for p, c in sorted(pos.items())},
                 frac * 100, len({q["topic"] for q in rot}), dict(sorted(io.items()))))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_pocus_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], q["c"]) for q in POOL) / n
    print("pool %d (%d pictures, raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, sum("img" in q for q in POOL), raw * 100, os.path.basename(out), len(held)))
    for q in held:
        print("  held: %s" % q["q"][:90])


if __name__ == "__main__":
    main()
