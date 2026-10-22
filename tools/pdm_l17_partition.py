#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 17 (Pulmonary Imaging, Professor Fowler, guest) pool into two 30s.

House format is 2x30 for the lecture. The remainder is held back for the cumulative Exam 4 master
forms (Lectures 17-21 and Labs 4-5), which wait until the block is complete.

RULES, asserted rather than trusted:
  1. A value in a STEM always carries its normal range ("(normal 0.6 to 1.2)"). Nothing is calculated.
  2. No acronym in a stem, option or explanation (NOT is emphasis, not an acronym).
  3. Every stem names the patient's age, asks one thing, and never cites the course.
  4. Pictures: every set carries MIN_IMG to MAX_IMG, never the same picture twice in one set, and every
     picture exists on disk with alt text and a slide caption; the alt text never names the key.
  5. Numeric option sets keep their authored ascending order ("ordered" items, WRITER.md rule 8): their key
     position is fixed and the other items are rotated around them to keep A-D balanced.

EMPHASIS (the 20 October recording, two segments, about 97 minutes; distinct minutes spoken per objective,
measured on the Notability transcript and re-checked on our faster-whisper transcript): objective a
(normal structures: surface anatomy, the upper airway films, the views, the one-third/two-thirds rule, the
systematic read, the hila) about 31 minutes; objective b (bony landmarks) about 9; objective c (abnormal
findings and technique) about 8; objective d (the modalities: indications, cautions, ultrasound, computed
tomography and attenuation, positron emission tomography, contrast, the angiogram, ventilation/perfusion,
magnetic resonance) about 36; objective e (the five patterns) about 10. Objective e is lifted to one item
per condition per set because the syllabus lists all five by name.
Spoken cues that point at slide facts ("this is important", "very important", "gotta know", "remember
that"): the sternal angle and the nipple line; the lateral neck film; the anteroposterior against the
posteroanterior view; the one-third/two-thirds rule; the costophrenic angles; the aortic knob; rotation
(never the tracheal shadow); the trachea in the midline; the left hilum higher; the pregnancy test
("always, always, always"); very few true contraindications; shellfish; the ventilation/perfusion scan
inferior to the angiogram; Kerley B lines; recognizing interstitial lung disease. Each cue group is
carried by EACH set where the pool has two or more items for it, otherwise by one of the sets.
De-emphasis: reading a ventilation/perfusion scan ("Are you going to be reading that? No.") -> the
mismatch-reading item was removed; the order a scan is read in ("Are you gonna get that deep into this? No.")
and the kinds of pneumonia ("I don't want you to get into the minutia") were never written.

Selection is swap-based local search, as on the Exam 3 builds. Target under 10% gameable per set.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
FOLDER = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 4")
sys.path.insert(0, HERE)
from pdm_l17_pool_a import POOL_A, SRC, IOA, IOB, IOC, IOD, IOE
from pdm_l17_pool_b import POOL_B
from _option_order import ordered_kind

BAN_STEMS = []   # the ventilation/perfusion mismatch-reading item was removed from pool B instead
POOL = [q for q in POOL_A + POOL_B if not any(q["q"].startswith(b) for b in BAN_STEMS)]
assert len(POOL) == len(POOL_A) + len(POOL_B) - len(BAN_STEMS), "a banned stem was not found"
SEED, NOPT, BAR, TARGET, PER_SET = 20261020, 4, 0.35, 0.10, 30
MIN_IMG, MAX_IMG = 10, 13
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

CITES = re.compile(r"(?i)\b(lecture|lecturer|slides?|deck|professor|this course|in class|syllabus|fowler|reynolds)\b")
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_NOTVAL = re.compile(r"\b\d+ degrees\b|\b[CT]\d\b|\bT[12]\b")     # a film angle or a vertebral level is not a patient value
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"NOT"}


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert len(ids) == 1, "stem prefix matches %d items: %s" % (len(ids), p)
    return ids[0]


def stems(*ps):
    return [stem(p) for p in ps]


# per-set bounds: (label, predicate, lo, hi)
def _io(io): return lambda q: q["io"] == io
def _tp(*ts): return lambda q: q["topic"] in ts
GROUPS = [
    ("objective a", _io(IOA), 8, 9),
    ("objective b", _io(IOB), 3, 4),
    ("objective c", _io(IOC), 3, 4),
    ("objective d", _io(IOD), 10, 11),
    ("objective e", _io(IOE), 5, 6),
    ("upper airway film", _tp("The upper airway film"), 1, 2),
    ("film quality", _tp("Film quality"), 2, 3),
    ("computed tomography anatomy", _tp("Computed tomography anatomy"), 1, 2),
    ("hila and heart", _tp("Hila and heart"), 1, 2),
    ("normal chest film", _tp("The normal chest film"), 1, 2),
    ("choosing the first study", _tp("Choosing the first study"), 2, 3),
    ("radiation and safety", _tp("Radiation and safety"), 1, 2),
    ("ultrasound", _tp("Ultrasound"), 1, 1),
    ("computed tomography basics", _tp("Computed tomography basics"), 1, 2),
    ("contrast", _tp("Contrast"), 1, 2),
    ("nuclear scans", _tp("Positron emission and single-photon scans"), 1, 1),
    ("ventilation/perfusion", _tp("Ventilation/perfusion scan"), 1, 2),
    ("angiogram", _tp("Computed tomography angiogram"), 1, 2),
    ("magnetic resonance", _tp("Magnetic resonance imaging"), 1, 2),
    ("pneumonia", _tp("Pneumonia"), 1, 1),
    ("pleural effusion", _tp("Pleural effusion"), 1, 1),
    ("pulmonary edema", _tp("Pulmonary edema"), 1, 1),
    ("pneumothorax", _tp("Pneumothorax"), 1, 1),
    ("interstitial lung disease", _tp("Interstitial lung disease"), 1, 2),
]

# near-twins that give each other away (stem, key or explanation): at most N per set
CLUSTERS = [
    (1, stems("A 74-year-old with shortness of breath has this", "A 77-year-old woman has this posteroanterior",
              "A 69-year-old with heart failure has a chest")),
    (1, stems("A 79-year-old with heart failure", "An 80-year-old with left heart failure",
              "A 73-year-old man with left heart failure")),
    (1, stems("A 41-year-old has this computed tomography reconstruction", "A 57-year-old has this computed",
              "A 49-year-old has this computed tomography image")),
    (1, stems("A 63-year-old man's lung mass", "A 72-year-old woman with chest pain may have an intramural",
              "A 44-year-old man may have vasculitis")),
    (1, stems("A 52-year-old with suspected pulmonary embolism had anaphylaxis",
              "A 49-year-old man asks how a ventilation/perfusion")),
    (1, stems("A 48-year-old woman has sudden pleuritic", "A 49-year-old man asks how a ventilation/perfusion")),
    (1, stems("A 66-year-old man asks about the risks", "A 58-year-old woman needs a procedure guided")),
    (1, stems("A 57-year-old woman is having a ventilation/perfusion", "A 54-year-old woman is having the ventilation half")),
    (1, stems("A 66-year-old man asks about the risks", "A 26-year-old woman needs a chest radiograph")),
    (1, stems("A 51-year-old's chest computed tomography report uses", "A 60-year-old's transverse computed",
              "A 30-year-old has chest trauma")),
    (1, stems("A 67-year-old woman has newly diagnosed lung cancer", "A 62-year-old woman with cancer has the study",
              "A 70-year-old man's staging scan")),
    (1, stems("A 46-year-old woman with scleroderma", "A 50-year-old man is referred for a pulmonary")),
    (1, stems("A 61-year-old has this transverse computed tomography angiogram", "A 70-year-old's chest computed")),
    (2, stems("A 40-year-old woman has this posteroanterior chest film", "A 44-year-old man has this posteroanterior",
              "A 66-year-old man's nasogastric tube", "A 57-year-old woman's chest film is being checked")),
    (1, stems("The posterior ribs above the diaphragm", "A 39-year-old takes a deep breath")),
    (1, stems("A 78-year-old in the intensive care unit", "A 40-year-old outpatient walks into radiology")),
    (1, stems("A 61-year-old man's posteroanterior film is checked", "A 58-year-old woman's heart size")),
    (1, stems("A clinician palpates the sternal angle", "A 36-year-old man is examined for landmarks")),
    (1, stems("A 40-year-old woman's lateral soft-tissue neck film", "A 29-year-old man's lateral soft-tissue")),
    (1, stems("A 25-year-old with suspected sinusitis", "A 35-year-old woman probably has a sinus")),
    (1, stems("A 66-year-old with worsening shortness of breath", "A 61-year-old woman may have interstitial")),
    (1, stems("A 58-year-old woman needs a procedure guided", "A 55-year-old man is screened before chest magnetic")),
    (1, stems("A 47-year-old had anaphylaxis to shellfish", "A 55-year-old man is screened before chest magnetic")),
    (1, stems("A 52-year-old woman is scheduled for contrast", "A 55-year-old man is screened before chest magnetic")),
    (1, stems("A 26-year-old woman needs a chest radiograph", "A 30-year-old pregnant woman")),
]

# the lecturer's emphasis cues: each set carries one of the group (EACH), or the pair of sets does (ANY)
EACH = [
    ("sternal angle / nipple line", stems("A clinician palpates the sternal angle", "A 36-year-old man is examined for landmarks")),
    ("anteroposterior against posteroanterior", stems("A 78-year-old in the intensive care unit", "A 40-year-old outpatient walks into radiology")),
    ("heart size, one third / two thirds", stems("A 61-year-old man's posteroanterior film is checked", "A 58-year-old woman's heart size")),
    ("costophrenic angles", stems("A 52-year-old woman has this routine", "A 74-year-old with shortness of breath has this",
                                  "A 77-year-old woman has this posteroanterior", "A 69-year-old with heart failure has a chest")),
    ("lateral neck film", stems("A 6-year-old has noisy breathing", "A 40-year-old woman's lateral soft-tissue neck film",
                                "A 29-year-old man's lateral soft-tissue")),
    ("pregnancy test", stems("A 26-year-old woman needs a chest radiograph", "A 30-year-old pregnant woman")),
    ("few true contraindications", stems("A 66-year-old man asks about the risks", "A 58-year-old woman needs a procedure guided")),
    ("ventilation/perfusion inferior to the angiogram", stems("A 52-year-old with suspected pulmonary embolism had anaphylaxis",
                                                         "A 49-year-old man asks how a ventilation/perfusion")),
    ("Kerley B lines", stems("A 79-year-old with heart failure", "A 76-year-old woman's chest radiograph shows Kerley")),
    ("computed tomography slices", stems("A 41-year-old has this computed tomography reconstruction", "A 57-year-old has this computed",
                                         "A 49-year-old has this computed tomography image")),
]
ANY = [
    ("aortic knob", stems("A 34-year-old man has this standing")),
    ("rotation, never the tracheal shadow", stems("A 76-year-old woman's posteroanterior film is checked for rotation")),
    ("trachea midline", stems("A 45-year-old's posteroanterior film shows the trachea")),
    ("left hilum higher", stems("A 45-year-old woman's posteroanterior film shows the left hilum")),
    ("shellfish", stems("A 47-year-old had anaphylaxis to shellfish")),
]


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def check(pool):
    seen = set()
    for i, q in enumerate(pool):
        w = "pool[%d] %s" % (i, q["q"][:50])
        k = q["c"]
        assert len(q["opts"]) == NOPT, "%s: %d options" % (w, len(q["opts"]))
        assert k == 0 or q.get("ordered"), "%s: key must be authored first" % w
        if not q.get("ordered"):
            assert not ordered_kind([o[0] for o in q["opts"]]), "%s: numeric option set would be rotated" % w
        assert q["q"].rstrip().endswith("?"), "%s: stem asks nothing" % w
        assert q["q"].count("?") == 1, "%s: stem asks more than one thing" % w
        assert _AGE.search(q["q"]), "%s: stem names no patient" % w
        assert not CITES.search(q["q"]), "%s: stem cites the course" % w
        assert not _CALC.search(q["q"]), "%s: stem asks for a calculation" % w
        if re.search(r"\d", _NOTVAL.sub("", _AGE.sub("", q["q"]))):
            assert "(normal " in q["q"], "%s: value without its normal range" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        assert q["opts"][k][1].startswith("Correct"), "%s: key explanation must open Correct" % w
        for j, (t, e) in enumerate(q["opts"]):
            assert len(t) <= 66, "%s: option over 66 characters: %r" % (w, t)
            assert not CITES.search(t), "%s: option cites the course" % w
            assert not CITES.search(e), "%s: explanation cites the course: %r" % (w, e[:70])
            assert len(e) >= 60, "%s: explanation too thin: %r" % (w, e[:60])
            if j != k:
                assert not e.startswith("Correct"), "%s: distractor explanation opens Correct" % w
                assert t in q.get("mis", {}), "%s: no mis label for %r" % (w, t)
        assert q.get("cite", "").startswith(SRC + ", Slide "), w
        for where, txt in [("stem", q["q"])] + [("option", o[0]) for o in q["opts"]] + [("explanation", o[1]) for o in q["opts"]]:
            bad = [a for a in _ACRO.findall(txt) if a not in _ACRO_OK]
            assert not bad, "%s: acronym %r in %s" % (w, bad, where)
        if "img" in q:
            assert os.path.exists(os.path.join(FOLDER, q["img"])), "%s: missing %s" % (w, q["img"])
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
    """Balance key positions: ordered items keep theirs, the rest fill what keeps A-D level."""
    fixed = Counter(q["c"] for q in qs if q.get("ordered"))
    free = [q for q in qs if not q.get("ordered")]
    want = Counter({p: len(qs) // NOPT for p in range(NOPT)})
    extra = list(range(NOPT)); rng.shuffle(extra)
    for p in extra[:len(qs) % NOPT]:
        want[p] += 1
    slots = []
    for p in range(NOPT):
        slots += [p] * max(0, want[p] - fixed[p])
    while len(slots) < len(free):
        slots.append(min(range(NOPT), key=lambda p: fixed[p] + slots.count(p)))
    slots = slots[:len(free)]
    rng.shuffle(slots)
    it = iter(slots)
    out = []
    for q in qs:
        r = {kk: vv for kk, vv in q.items() if kk not in ("slot", "ordered")}
        if not q.get("ordered"):
            o = list(q["opts"]); key = o.pop(0); want_p = next(it); o.insert(want_p, key)
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
    for _ in range(120000):
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
        io = Counter("abcde"[[IOA, IOB, IOC, IOD, IOE].index(q["io"])] for q in rot)
        sets["set%d" % k] = rot
        print("set%d  %d questions  pictures=%d  positions=%s  gameable=%.1f%%  topics=%d  objectives=%s"
              % (k, len(rot), sum("img" in q for q in rot), {chr(65 + p): c for p, c in sorted(pos.items())},
                 frac * 100, len({q["topic"] for q in rot}), dict(sorted(io.items()))))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l17_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], q["c"]) for q in POOL) / n
    print("pool %d (%d pictures, raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, sum("img" in q for q in POOL), raw * 100, os.path.basename(out), len(held)))


if __name__ == "__main__":
    main()
