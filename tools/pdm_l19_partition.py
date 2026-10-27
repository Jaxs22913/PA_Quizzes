#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 19 (Acid-Base Balance and Blood Gas Interpretation, Professor Finck) pool into two 30s.

House format is 2x30 for the lecture. The remainder is held back for the cumulative Exam 4 master forms
(Lectures 17-21 and Labs 4-5), which wait until the block is complete (Lecture 21, 19 November).

RULES, asserted rather than trusted:
  1. EVERY number in a stem that is not an age, a duration or inside a "(normal ...)" bracket is followed by its
     unit and "(normal ...)": a value never appears without its normal range (Reynolds, Lecture 1).
  2. Nothing is calculated except the anion gap (objective f; the lecturer at 1:18:52 said she will ask for it).
     The calculation items are the only numeric option sets; they are sorted ascending and keep the key where
     its value falls (WRITER.md rule 8); every other item is rotated to balance the key positions.
  3. No abbreviation in an option. In a stem or explanation an abbreviation appears only as ABBREV (full term).
     Capitals used for emphasis (NOT, LOW, ...) are listed.
  4. Every stem names the patient's age, asks one thing, and never cites the course.
  5. Pictures: every set carries MIN_IMG to MAX_IMG, never the same picture twice, every picture exists, is
     numbered (l19-fig-NN.jpg) and its alt text never names the key.

EMPHASIS (the 27 October recording, two segments, 90 minutes; minutes spoken per objective, measured on our
faster-whisper transcript; Notability's second opinion has text for segment 1 only, 0:00-47:13, and agrees on
content there): objective a (the order and each value: the carbon dioxide and oxygen pressures, saturation,
content, the dissociation curve, base excess, carboxyhemoglobin) about 29 minutes; objective d (pH and its
definitions, the steps, what moves each pressure, compensation and the pearls) about 25; objective e (the four
disorders and their causes, potassium) about 18; objective b (why arterial, the sample, the venous values) about
8; objective g (the abnormal gap) about 5; objective c (indications) about 2; objective f (the formula) about 2;
opening and close about 2. Objective f is lifted to 2 a set (the syllabus objective and the lecturer's own
"I do want you to memorize and understand this equation"); objective c is held to 2.
Spoken cues that point at slide facts, each carried by EACH set: the step-wise read ("step one, pH; step two,
CO2", 37:42); potassium and pH ("Put a star on this slide", 1:16:20; "a very clinically important concept");
the anion gap equation (1:18:58); the "classic" anxious hyperventilating patient (20:59) and the "classic"
ketoacids (31:07); the fraction of inspired oxygen ("remember this", 40:15; "you have to know this", 1:00:40);
oxygen carried on hemoglobin, 98% (13:07 "we need to know", 1:02:21 "remember"); whether the labs fit the
patient (36:13 "ingrain in your head"). De-emphasis: the saturation thresholds of slide 36 ("I'm not going to
ask you", 1:01:57: none asked); the normal values to memorize (all supplied instead); the arterial stick in
detail ("more detail really is coming during CPSS": at most two sample-handling items a set).

Selection is swap-based local search, as on the Lecture 20 build. Target under 10% gameable per set.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
sys.path.insert(0, HERE)
from pdm_l19_pool_a import POOL_A, SRC, IOA, IOB, IOC, IOD, IOE, IOF, IOG
from pdm_l19_pool_b import POOL_B
from _option_order import ordered_kind, order_options, is_monotonic

POOL = POOL_A + POOL_B
SEED, NOPT, BAR, TARGET, PER_SET = 20261027, 4, 0.35, 0.10, 30
MIN_IMG, MAX_IMG = 1, 2
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
IOS = [IOA, IOB, IOC, IOD, IOE, IOF, IOG]

CITES = re.compile(r"(?i)\b(lecture|lecturer|slides?|deck|professor|this course|in class|syllabus|finck|reynolds)\b")
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"NOT", "LOW", "HIGH", "RIGHT", "LEFT", "ARTERIAL", "SAMPLE", "INCREASED", "DECREASED", "MORE", "LOSS",
            "EXCESS", "ACIDOSIS", "ALKALOSIS", "MILD", "RAISES", "RAISE", "METABOLIC", "RESPIRATORY", "POSITIVE",
            "NEGATIVE", "ADDS", "SUM", "ACID", "HYPOKALEMIA", "DECREASE", "RADIAL", "RISEN", "CHRONIC", "OTHER"}       # capitals for emphasis, not abbreviations
_DEFINED = re.compile(r"(?:/[A-Z][A-Za-z0-9]*)* \(")
_DURATION = re.compile(r"\b\d+ (?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)\b")
_NUM = re.compile(r"\d+(?:\.\d+)?")
_UNIT_THEN_RANGE = re.compile(r"\s*(?:mm Hg|mEq/L|g/dL|%)?\s*\((?:venous |arterial )?normal ")


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert len(ids) == 1, "stem prefix matches %d items: %s" % (len(ids), p)
    return ids[0]


def stems(*ps):
    return [stem(p) for p in ps]


def values_without_range(s):
    """Numbers in a stem that are not an age, a duration or inside brackets, and are not followed by their
    unit and "(normal ...)"."""
    skip = set()
    for rx in (_AGE, _DURATION):
        for m in rx.finditer(s):
            skip |= set(range(m.start(), m.end()))
    depth, inside = 0, set()
    for i, ch in enumerate(s):
        if ch == "(":
            depth += 1
        if depth:
            inside.add(i)
        if ch == ")":
            depth -= 1
    bad = []
    for m in _NUM.finditer(s):
        if m.start() in skip or m.start() in inside:
            continue
        if not _UNIT_THEN_RANGE.match(s, m.end()):
            bad.append(m.group(0))
    return bad


def _io(io): return lambda q: q["io"] == io
def _tp(*ts): return lambda q: q["topic"] in ts
GROUPS = [
    ("objective a", _io(IOA), 7, 8),
    ("objective b", _io(IOB), 3, 4),
    ("objective c", _io(IOC), 2, 2),
    ("objective d", _io(IOD), 7, 8),
    ("objective e", _io(IOE), 6, 7),
    ("objective f", _io(IOF), 2, 2),
    ("objective g", _io(IOG), 2, 3),
    ("the order", _tp("The blood gas order"), 1, 2),
    ("carbon dioxide", _tp("Carbon dioxide pressure", "What moves the carbon dioxide"), 2, 3),
    ("oxygen", _tp("Oxygen pressure", "What moves the oxygen"), 3, 4),
    ("the curve", _tp("The dissociation curve"), 1, 2),
    ("base excess", _tp("Base excess"), 1, 2),
    ("blood pH and buffers", _tp("Blood pH", "Buffers"), 0, 1),
    ("why arterial", _tp("Why arterial blood"), 1, 1),
    ("venous values", _tp("Venous against arterial values"), 1, 1),
    ("the arterial sample", _tp("The arterial sample"), 1, 2),
    ("stepwise read", _tp("The stepwise read"), 1, 2),
    ("compensation", _tp("Compensation"), 2, 3),
    ("respiratory acidosis", _tp("Respiratory acidosis"), 1, 2),
    ("respiratory alkalosis", _tp("Respiratory alkalosis"), 1, 2),
    ("metabolic acidosis", _tp("Metabolic acidosis"), 1, 2),
    ("metabolic alkalosis", _tp("Metabolic alkalosis"), 1, 2),
    ("plain four-way reads", _tp("The four disorders"), 0, 1),
    ("mixed pictures", _tp("Mixed pictures"), 0, 1),
    ("potassium", _tp("Potassium"), 1, 1),
]

# near-twins that give each other away (stem, key or explanation): at most N per set
CLUSTERS = [
    (1, stems("A 52-year-old has an arterial pH of 7.22", "A 27-year-old has an arterial pH of 7.56")),
    (1, stems("A 41-year-old's arterial blood gas reports", "A 55-year-old's clinician needs", "A 60-year-old's pulse oximeter")),
    (1, stems("A 60-year-old's pulse oximeter", "A 49-year-old with asthma is seen")),
    (1, stems("A 45-year-old firefighter", "A 38-year-old is treated after a house fire")),
    (1, stems("A 47-year-old is breathing slowly", "A 36-year-old with vomiting and confusion")),
    (1, stems("A 70-year-old woman receiving supplemental", "A 66-year-old's arterial blood gas sample is labeled")),
    (1, stems("Before an arterial puncture at the wrist", "Before a radial arterial stick")),
    (1, stems("A 66-year-old in the intensive care unit needs", "Before a radial arterial stick")),
    (1, stems("A 57-year-old with acute dyspnea", "A 62-year-old's venous sample")),
    (1, stems("A 74-year-old's arterial blood gas comes back", "A 57-year-old with acute dyspnea")),
    (1, stems("A 74-year-old's arterial blood gas comes back", "A 61-year-old woman is well today")),
    (1, stems("A 74-year-old's arterial blood gas comes back", "A 63-year-old in shock")),
    (1, stems("A 59-year-old's arterial blood gas has just", "A 66-year-old's blood gas has been read")),
    (1, stems("A 29-year-old is having a panic attack", "A 32-year-old in her third trimester")),
    (1, stems("A 45-year-old in septic shock", "A 50-year-old was given excessive bicarbonate")),
    (1, stems("A 64-year-old's blood gas reports a base deficit", "A 58-year-old's arterial blood gas includes the base")),
    (1, stems("A 63-year-old with severe kyphoscoliosis", "A 57-year-old has a respiratory acidosis from")),
    (1, stems("A 45-year-old has had 5 days of profuse diarrhea", "A 38-year-old has pH")),
    (1, stems("A 35-year-old has been on nasogastric", "A 68-year-old with heart failure received")),
    (2, stems("A 42-year-old is oversedated", "A 50-year-old with renal failure", "A 47-year-old has had several days of vomiting")),
    (2, stems("A 24-year-old is brought in after an opioid", "A 26-year-old is anxious and breathing fast",
              "A 44-year-old has pH", "A 53-year-old has pH")),
    (1, stems("A 60-year-old in severe acidosis", "A 50-year-old with metabolic alkalosis from vomiting")),
    (1, stems("A 40-year-old took far too much", "A 78-year-old has severe congestive")),
    (1, stems("A 25-year-old with diabetic ketoacidosis has an anion gap", "A 31-year-old trauma patient")),
    (1, stems("A 44-year-old taking lithium", "A 59-year-old has an elevated anion gap")),
    (1, stems("A 58-year-old with cirrhosis", "A healthy 30-year-old has a normal anion gap")),
    (1, stems("A 60-year-old has developed a respiratory acidosis", "A 31-year-old woman has had a respiratory alkalosis")),
    (1, stems("A 40-year-old has been vomiting for 3 days", "A 47-year-old has had several days of vomiting")),
]

# the lecturer's emphasis cues: each set carries at least one of the group
EACH = [
    ("the step-wise read", stems("A 59-year-old's arterial blood gas has just", "A 52-year-old has an arterial pH of 7.30",
                                 "A 66-year-old's blood gas has been read")),
    ("potassium (put a star on this slide)", stems("A 60-year-old in severe acidosis", "A 50-year-old with metabolic alkalosis from vomiting")),
    ("the classic anxious hyperventilating patient", stems("A 29-year-old is having a panic attack", "A 26-year-old is anxious and breathing fast")),
    ("the classic ketoacids", stems("A 23-year-old with diabetic ketoacidosis", "A 22-year-old with diabetic ketoacidosis",
                                    "A 25-year-old with diabetic ketoacidosis", "A 38-year-old has pH")),
    ("the fraction of inspired oxygen", stems("A 70-year-old woman receiving supplemental", "A 66-year-old's arterial blood gas sample is labeled",
                                              "A 77-year-old with pneumonia")),
    ("98% carried on hemoglobin", stems("A 41-year-old's arterial blood gas reports", "A 55-year-old's clinician needs")),
    ("do the labs fit the patient", stems("A 66-year-old's blood gas has been read", "A 74-year-old's arterial blood gas comes back")),
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
            tail = txt[m.end():]
            if not re.match(r"(?:/[A-Z][A-Za-z0-9]*)+ \(", tail):
                bad.append(a)
    return bad


def numeric(q):
    return bool(ordered_kind([o[0] for o in q["opts"]]))


def check(pool):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d] %s" % (i, q["q"][:50])
        k = q["c"]
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert k == 0, "%s: key must be authored first" % w
        assert q["io"] in IOS, w
        assert numeric(q) == (q["io"] == IOF), "%s: numeric options only on the anion gap calculation" % w
        assert q["q"].rstrip().endswith("?"), "%s: stem asks nothing" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert _AGE.search(q["q"]), "%s: stem names no patient" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not _CALC.search(q["q"]), "%s: stem says calculate" % w
        bad = values_without_range(q["q"])
        assert not bad, "%s: value(s) %r without their normal range" % (w, bad)
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        texts = [o[0].lower() for o in q["opts"]]
        for a in texts:
            for b in texts:
                assert a == b or not re.search(r"(?<![\w.])%s(?![\w.])" % re.escape(a), b), "%s: option %r contains option %r" % (w, b, a)
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
            assert re.match(r"pdm-exam-4-quiz-images/l19-fig-\d\d\.jpg$", q["img"]), "%s: picture name must be a number" % w
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
    return score_set(sel[:PER_SET]) + score_set(sel[PER_SET:])


def rotate(qs, rng, k):
    """Numeric option sets are sorted ascending and keep their key where its value falls; every other item is
    rotated so the set's key positions come out balanced across A-D."""
    out, fixed = [None] * len(qs), Counter()
    free = []
    for i, q in enumerate(qs):
        r = {kk: vv for kk, vv in q.items() if kk != "slot"}
        if numeric(q):
            r = order_options(r)
            assert is_monotonic([o[0] for o in r["opts"]])
            out[i] = r
            fixed[r["c"]] += 1
        else:
            free.append((i, r))
    total = len(qs)
    want = [total // NOPT] * NOPT
    extra = list(range(NOPT)); rng.shuffle(extra)
    for p in extra[:total % NOPT]:
        want[p] += 1
    need = [max(0, want[p] - fixed[p]) for p in range(NOPT)]
    while sum(need) < len(free):                       # a fixed position overfilled: spread the rest evenly
        need[min(range(NOPT), key=lambda p: need[p] + fixed[p])] += 1
    slots = [p for p in range(NOPT) for _ in range(need[p])][:len(free)]
    rng.shuffle(slots)
    for (i, r), want_p in zip(free, slots):
        o = list(r["opts"]); key = o.pop(0); rng.shuffle(o); o.insert(want_p, key)
        r["opts"] = o; r["c"] = want_p
        out[i] = r
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
        io = Counter("abcdefg"[IOS.index(q["io"])] for q in rot)
        sets["set%d" % k] = rot
        print("set%d  %d questions  pictures=%d  positions=%s  gameable=%.1f%%  topics=%d  objectives=%s"
              % (k, len(rot), sum("img" in q for q in rot), {chr(65 + p): c for p, c in sorted(pos.items())},
                 frac * 100, len({q["topic"] for q in rot}), dict(sorted(io.items()))))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l19_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], q["c"]) for q in POOL) / n
    print("pool %d (%d pictures, raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, sum("img" in q for q in POOL), raw * 100, os.path.basename(out), len(held)))
    for q in held:
        print("  held: %s" % q["q"][:90])


if __name__ == "__main__":
    main()
