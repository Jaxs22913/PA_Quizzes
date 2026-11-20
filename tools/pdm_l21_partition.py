#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Partition the PDM I Lecture 21 (Transfusion Medicine and Blood Banking Fundamentals, Professor Reynolds)
pool into two 30s.

House format is 2x30 for the lecture. The remainder is held back for the cumulative Exam 4 master forms
(Lectures 17-21), which wait until the block is complete.

RULES, asserted rather than trusted:
  1. Numbers in a STEM. A lab value always carries its normal range ("(normal ...)"). Without a range a stem
     may carry only the slide's own clinical criteria and setting, which are not lab values: an age, a
     duration, a body temperature in degrees, an infused volume in mL, and a count of units. Antigen and
     reagent names that contain a digit (A1 cells, C3d, IgG1) are names. Nothing is calculated.
  2. Abbreviations: none in an option. In a stem or explanation an abbreviation appears only as
     ABBREV (full term). Names that are not abbreviations are whitelisted: the ABO system and the group AB
     (A, B, O are single letters), plus capitals used for emphasis (NOT, ALREADY, FREE, ...). Rh, RhD,
     IgM/IgG/IgA/IgE, Kell, Kidd, Duffy, Jka are mixed case and pass by construction.
  3. Every stem names the patient's age, asks one thing, and never cites the course.
  4. No option set is numeric (WRITER.md rule 8 would fix its order); asserted. No dose is asked.
  5. Slides only; slide 23 (Cases) is empty and nothing cites it.

EMPHASIS: see EMPHASIS_NOTE below (the 19 November recording).

Selection is swap-based local search, as on the Lecture 18 and 17 builds. Target under 10% gameable per set.
"""
import json, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from pdm_l21_pool_a import POOL_A, SRC, IOA, IOB, IOC, IOD, IOE
from pdm_l21_pool_b import POOL_B
from _option_order import ordered_kind

POOL = POOL_A + POOL_B
SEED, NOPT, BAR, TARGET, PER_SET = 20261119, 4, 0.35, 0.10, 30
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
IOS = [IOA, IOB, IOC, IOD, IOE]

EMPHASIS_NOTE = """The 19 November recording (51:19, one segment; our faster-whisper transcript read against Notability's,
which agree). The recording starts as slide 4 ends ("... second sample rule. It's that important"), so slides 1-4
have almost no audio. Minutes spoken per objective (distinct minutes): a about 2 (the second-sample rule, human
error recalled at 34:00 and 49:13); b about 18 (the compatibility table "a very important table", 2:05 to 11:32,
then O-negative against O-positive, 12:35 to 14:09; about 4 of the 18 are asides on donating blood and plasma);
c about 4 (18:26 to 22:29: sensitization, Rh immune globulin, IgG crosses the placenta and IgM is too big); d about
10 (22:29 to 32:41: forward and reverse as mirrors, the antibody screen and its time cost, direct against indirect,
type and screen against type and crossmatch, the 3-day rule); e about 18 (32:44 to 51:11, including about 6 minutes
of four cases worked aloud for the empty Cases slide). No "on the exam" statement in this lecture; her cues are
listed in EACH and ANY. Objective b is weighted up and c down to match; d and e stay the largest because she framed
the lecture as "not pathophys, this is diagnostics" (0:17). De-emphasis: the sickle cell mimicry "is pathophys ...
beyond labs" (36:52), platelet compatibility rules "don't necessarily apply the same way" (6:29), pediatric rules
(14:20): the sickle cell items are not forced in."""

CITES = re.compile(r"(?i)\b(lecture|lecturer|slides?|deck|professor|this course|in class|syllabus|reynolds)\b")
_AGE = re.compile(r"\b\d+-(?:year|month|week|day)-old\b")
_CALC = re.compile(r"(?i)\bcalculat|\bcompute\b|\bwork out\b")
_DOSE = re.compile(r"(?i)\b\d+(?:\.\d+)?\s*(?:mg|mcg|g)\b(?!/dL)|\bdose\b")
_ACRO = re.compile(r"\b[A-Z]{2,}[A-Za-z0-9]*\b")
_ACRO_OK = {"ABO", "AB", "NOT", "ALREADY", "FREE", "ZERO", "MUST", "WITH", "RESERVES", "RESERVED", "SAME",
            "SLOWER", "WITHIN", "BOTH", "NO", "UNEXPECTED", "NEGATIVE", "POSITIVE", "PLASMA", "RED", "CELL",
            "CELLS", "SENSITIZED", "MAINTAINED", "NON", "DIRECT", "INDIRECT", "AND", "NEW", "RECIPIENT", "DONOR", "PLASMA", "OUT", "HALT", "SAMPLE"}
_DEFINED = re.compile(r" \(")
_ALLOWED_NUM = re.compile(
    r"\b\d+-(?:year|month|week|day)-old\b"
    r"|\b\d+(?:\.\d+)?\s*(?:to\s+\d+\s*)?(?:seconds?|minutes?|hours?|days?|weeks?|months?|years?)\b"
    r"|\b\d+(?:\.\d+)?\s*°\s*[CF]\b"
    r"|\b\d+\s*(?:to\s+\d+\s*)?mL\b"
    r"|\b\d+\s*units?\b"
    r"|\b[A-Z][A-Za-z]*\d+[a-z]?\b")
_HAS_RANGE = re.compile(r"\(normal ")
_KEEP_IDS = set()


def stem(p):
    ids = [i for i, q in enumerate(POOL) if q["q"].startswith(p)]
    assert len(ids) == 1, "stem prefix matches %d items: %s" % (len(ids), p)
    return ids[0]


def stems(*ps):
    return [stem(p) for p in ps]


def _io(io): return lambda q: q["io"] == io
def _tp(*ts): return lambda q: q["topic"] in ts
GROUPS = [
    ("objective a", _io(IOA), 3, 4),
    ("objective b", _io(IOB), 6, 7),
    ("objective c", _io(IOC), 3, 4),
    ("objective d", _io(IOD), 8, 9),
    ("objective e", _io(IOE), 9, 10),
    ("ABO antigens and antibodies", _tp("ABO antigens and antibodies"), 1, 2),
    ("compatibility", _tp("Compatibility"), 2, 3),
    ("emergency release", _tp("Emergency release"), 1, 2),
    ("Rh factor", _tp("Rh factor"), 1, 2),
    ("hemolytic disease of the newborn", _tp("Hemolytic disease of the newborn"), 1, 2),
    ("ABO typing", _tp("ABO typing"), 2, 3),
    ("antibody screen", _tp("Antibody screen"), 1, 2),
    ("crossmatch", _tp("Crossmatch"), 2, 2),
    ("antiglobulin tests", _tp("Antiglobulin tests"), 1, 2),
    ("ordering and specimens", _tp("Ordering and specimens"), 1, 2),
    ("reaction protocol", _tp("Reaction protocol"), 1, 2),
    ("acute hemolytic", _tp("Acute hemolytic"), 1, 2),
    ("delayed hemolytic", _tp("Delayed hemolytic"), 1, 2),
    ("febrile non-hemolytic", _tp("Febrile non-hemolytic"), 1, 2),
    ("allergic", _tp("Allergic"), 1, 2),
    ("anaphylactic", _tp("Anaphylactic"), 1, 2),
]

# near-twins that give each other away (stem, key or explanation): at most N per set
CLUSTERS = [
    (1, stems("A 34-year-old man in one trauma bay", "A 56-year-old woman dies")),
    (1, stems("A 27-year-old woman types as group A", "A 37-year-old woman's plasma agglutinates")),
    (2, stems("A 37-year-old woman's plasma agglutinates", "A 58-year-old man's plasma agglutinates",
              "A 49-year-old woman's plasma agglutinates")),
    (1, stems("A 58-year-old man's plasma agglutinates", "A 35-year-old man's washed red cells")),
    (1, stems("A 49-year-old woman's plasma agglutinates", "A 63-year-old man who types as group AB")),
    (1, stems("A 42-year-old man's washed red cells", "A 35-year-old man's washed red cells", "A 53-year-old woman needs")),
    (1, stems("A 33-year-old man types as group O", "A 52-year-old man's type is unknown", "A 35-year-old man's washed red cells")),
    (1, stems("A 63-year-old man who types as group AB", "A 36-year-old woman who types as group B")),
    (1, stems("A 38-year-old woman who types as group O", "A 45-year-old man of unknown type")),
    (1, stems("A 45-year-old man of unknown type", "A 52-year-old man's type is unknown")),
    (1, stems("A 24-year-old woman of unknown blood type", "A 26-year-old woman with trauma")),
    (1, stems("A 68-year-old man of unknown blood type", "A 70-year-old man who is RhD-negative")),
    (1, stems("A 40-year-old man receives ABO-incompatible", "A 38-year-old woman has an acute ABO", "A 35-year-old RhD-negative woman")),
    (1, stems("A 44-year-old man becomes hypotensive", "A 50-year-old woman develops kidney injury")),
    (1, stems("A 50-year-old woman develops kidney injury", "A 62-year-old woman's acute hemolytic")),
    (1, stems("A 22-year-old RhD-negative woman", "A 39-year-old woman's chart compares")),
    (1, stems("A 35-year-old RhD-negative woman", "A 46-year-old man with anti-D")),
    (1, stems("A 28-year-old RhD-negative woman made anti-D", "A 39-year-old woman's chart compares", "A 34-year-old woman's fetus")),
    (1, stems("A 25-year-old RhD-negative woman", "A 31-year-old RhD-negative woman")),
    (1, stems("A 30-year-old RhD-negative woman", "A 27-year-old RhD-negative woman")),
    (1, stems("A 60-year-old man who was transfused", "A 32-year-old woman with three")),
    (1, stems("A 67-year-old man's antibody screen", "A 59-year-old man's identification panel")),
    (1, stems("A 59-year-old man's identification panel", "A 66-year-old woman with a known")),
    (1, stems("A 71-year-old man has a positive", "A 62-year-old man with a known anti-Kell")),
    (1, stems("A 44-year-old woman has a negative", "A 57-year-old woman with a negative")),
    (1, stems("A 48-year-old woman becomes febrile", "A 55-year-old man's transfusion is stopped", "A 52-year-old man's hemolysis")),
    (1, stems("A 25-year-old pregnant woman", "A 32-year-old woman with three")),
    (1, stems("A 70-year-old man transfused 6 weeks", "A 30-year-old woman who was pregnant")),
    (1, stems("A 54-year-old man with a stable", "A 61-year-old man's type and crossmatch")),
    (1, stems("A 58-year-old woman develops chills", "A 47-year-old man's transfusion has just")),
    (1, stems("A 40-year-old man gets high fever", "A 45-year-old man's plasma and urine", "A 43-year-old woman shows")),
    (1, stems("A 39-year-old woman has a mild fever", "A 41-year-old man's peripheral smear")),
    (1, stems("A 19-year-old man with sickle cell", "A 23-year-old woman with sickle cell")),
    (1, stems("A 66-year-old man's temperature rises", "A 59-year-old man has a transfusion reaction")),
    (1, stems("A 74-year-old man has had febrile", "A 45-year-old man has a febrile")),
    (1, stems("A 33-year-old woman develops itching", "A 48-year-old man gets hives")),
    (1, stems("A 37-year-old woman has hives", "A 42-year-old woman is about to be transfused")),
    (1, stems("A 28-year-old woman develops stridor", "A 54-year-old man becomes severely", "A 47-year-old woman reacts within")),
    (1, stems("A 31-year-old woman with severe IgA", "A 74-year-old man has had febrile")),
    (1, stems("A 61-year-old woman's reaction workup", "A 50-year-old man has hives during")),
]

# the lecturer's emphasis cues: each set carries one of the group (EACH), or the pair of sets does (ANY)
EACH = [
    ("the inverse compatibility rule ('a very important table', 2:05; 10:50-11:25)",
     stems("A 63-year-old man who types as group AB", "A 38-year-old woman who types as group O",
           "A 45-year-old man of unknown type", "A 36-year-old woman who types as group B", "A 52-year-old man's type is unknown")),
    ("always stop the blood (32:44; 50:53-51:11)",
     stems("A 58-year-old woman develops chills", "A 47-year-old man's transfusion has just")),
    ("the allergic restart, the only one (39:49-40:43)",
     stems("A 33-year-old woman develops itching", "A 48-year-old man gets hives")),
    ("the direct antiglobulin test separates hemolytic from non-hemolytic (42:25-42:47; 50:09-50:40)",
     stems("A 61-year-old woman's reaction workup", "A 48-year-old woman becomes febrile", "A 55-year-old man's transfusion is stopped",
           "A 50-year-old man has hives during", "A 59-year-old man has a transfusion reaction")),
    ("human error drives mortality (49:13-49:24)",
     stems("A 34-year-old man in one trauma bay", "A 56-year-old woman dies")),
    ("the delayed hemolytic reaction, diagnosed in primary care (47:07-49:07)",
     stems("A 39-year-old woman has a mild fever", "A 57-year-old man had a negative", "A 64-year-old woman develops a delayed",
           "A 41-year-old man's peripheral smear")),
    ("forward and reverse typing as mirrors (24:09-25:23)",
     stems("A 42-year-old man's washed red cells", "A 37-year-old woman's plasma agglutinates", "A 58-year-old man's plasma agglutinates",
           "A 49-year-old woman's plasma agglutinates", "A 35-year-old man's washed red cells")),
    ("O-negative against O-positive (13:20-14:09)",
     stems("A 24-year-old woman of unknown blood type", "A 68-year-old man of unknown blood type", "A 26-year-old woman with trauma")),
]
ANY = [
    ("the second-sample rule ('It's that important', 0:04)", stems("A 29-year-old man has no verified")),
    ("the 3-day specimen rule (31:00-32:37)", stems("A 70-year-old man transfused 6 weeks", "A 30-year-old woman who was pregnant")),
    ("IgG crosses the placenta, IgM is too big (20:28-21:26)", stems("A 28-year-old RhD-negative woman made anti-D", "A 39-year-old woman's chart compares")),
]

# The first selection (before the recording arrived) was blind-reviewed and audited item by item. When the
# recording's emphasis was folded in, the search starts from that selection and pays 2 points for every reviewed
# item it drops, so only the swaps the emphasis needs are made (each new item then goes through review).
KEEP = [
[
"A 27-year-old RhD-negative woman without anti-D has abdomina",
"A 44-year-old man becomes hypotensive and shocked minutes in",
"A 74-year-old man has had febrile non-hemolytic reactions be",
"A 66-year-old woman's transfusion is stopped for a suspected",
"A 46-year-old woman's polyspecific direct antiglobulin test ",
"A 24-year-old woman of unknown blood type is bleeding heavil",
"A 41-year-old man's peripheral smear is reviewed 10 days aft",
"A 39-year-old woman's chart compares the ABO and RhD systems",
"A 37-year-old woman's plasma agglutinates reagent A1 cells b",
"A 52-year-old woman needs a blood sample drawn for pre-trans",
"A 50-year-old man has hives during a transfusion. What do hi",
"A 30-year-old woman who was pregnant 2 months ago has a pre-",
"A 63-year-old man who types as group AB needs red cells. Fro",
"A 38-year-old woman who types as group O needs plasma. From ",
"A 61-year-old man's type and crossmatch has tagged and reser",
"A 47-year-old woman reacts within seconds after only 2 mL of",
"A 60-year-old man who was transfused 2 years ago is typed be",
"A 61-year-old woman is starting her first unit of red cells.",
"A 57-year-old woman with a negative screen gets an immediate",
"A 31-year-old RhD-negative woman without anti-D has just del",
"A 34-year-old man in one trauma bay is given a red cell unit",
"A 40-year-old man receives ABO-incompatible red cells and hi",
"A 60-year-old woman's temperature rises 2.3 °C during a plat",
"A 59-year-old man's identification panel shows anti-Jka. Wha",
"A 37-year-old woman has hives and itching during a plasma tr",
"A 64-year-old man's forward type reads group A, but his reve",
"A 45-year-old man's plasma and urine are inspected after a s",
"A 23-year-old woman with sickle cell disease has a delayed r",
"A 62-year-old man with a known anti-Kell needs 2 units. Whic",
"A 46-year-old man with anti-D receives RhD-positive cells. W"
],
[
"A 28-year-old RhD-negative woman made anti-D after deliverin",
"A 25-year-old pregnant woman has her routine prenatal antibo",
"A 45-year-old man has a febrile non-hemolytic reaction durin",
"A 66-year-old woman with a known red cell alloantibody is sc",
"A 42-year-old woman is about to be transfused. With which ki",
"A 1-year-old girl who has never been transfused types as gro",
"A 35-year-old RhD-negative woman with anti-D is transfused R",
"A 36-year-old woman who types as group B needs red cells. Fr",
"A 42-year-old man's washed red cells agglutinate with anti-A",
"A 55-year-old man's transfusion is stopped for a suspected r",
"A 29-year-old man has no verified blood type on record and n",
"A 25-year-old RhD-negative woman with no anti-D is pregnant.",
"A 62-year-old woman's acute hemolytic reaction is followed b",
"A 49-year-old woman's plasma agglutinates neither reagent A1",
"A 47-year-old man is about to receive a red cell unit. The n",
"A 59-year-old man has a transfusion reaction with fever, sta",
"A 57-year-old man had a negative antibody screen before his ",
"A 67-year-old man's antibody screen is positive. What is the",
"A 31-year-old woman types as group B. Which enzyme gives her",
"A 40-year-old man gets high fever, rigors, flank pain and re",
"A 71-year-old man has a positive antibody screen. Which cros",
"A 56-year-old woman dies after a hemolytic transfusion react",
"A 52-year-old man's type is unknown and he needs red cells b",
"A 70-year-old man transfused 6 weeks ago has a type and scre",
"A 58-year-old man's plasma agglutinates both reagent A1 cell",
"A 41-year-old woman's antibody screen is negative. Outside t",
"A 61-year-old woman's reaction workup shows a newly positive",
"A 31-year-old woman with severe IgA deficiency and anti-IgA ",
"A 44-year-old woman has a negative antibody screen, no histo",
"A 70-year-old man who is RhD-negative receives O-positive re"
]
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
        assert not _DOSE.search(q["q"] + " " + q["opts"][k][0]), "%s: a dose is asked" % w
        if re.search(r"\d", _ALLOWED_NUM.sub("", q["q"])):
            assert _HAS_RANGE.search(q["q"]), "%s: value without its normal range" % w
        assert q["q"] not in seen, "%s: duplicate stem" % w
        seen.add(q["q"])
        assert len({o[0] for o in q["opts"]}) == NOPT, "%s: duplicate option text" % w
        texts = [o[0].lower() for o in q["opts"]]
        for a in texts:          # whole words: "group a" is not inside "group ab"
            for b in texts:
                assert a == b or not re.search(r"(?<![\w-])" + re.escape(a) + r"(?![\w-])", b), \
                    "%s: option %r contains option %r" % (w, b, a)
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
        assert not re.search(r"\b23\b", q["cite"]), "%s: cites the empty Cases slide" % w
        for where, txt in [("stem", q["q"])] + [("explanation", o[1]) for o in q["opts"]]:
            bad = _acronyms_ok(txt)
            assert not bad, "%s: undefined abbreviation %r in %s" % (w, bad, where)
        assert "img" not in q, "%s: the deck has no pictures" % w


def score_set(sel):
    qs = [POOL[i] for i in sel]
    g = sum(gameable(q["opts"], q["c"]) for q in qs) / len(qs)
    s = max(0.0, g - TARGET) * 100
    for _, pred, lo, hi in GROUPS:
        k = sum(1 for q in qs if pred(q))
        s += 3 * (max(0, lo - k) + max(0, k - hi))
    ss = set(sel)
    for mx, ids in CLUSTERS:
        s += 4 * max(0, len(ss & set(ids)) - mx)
    for _, ids in EACH:
        s += 4 * (not (ss & set(ids)))
    return s


def score(sel):
    v = score_set(sel[:PER_SET]) + score_set(sel[PER_SET:])
    v += 2 * len(_KEEP_IDS - set(sel))
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
    global _KEEP_IDS
    keep = [stem(p) for p in KEEP[0]] + [stem(p) for p in KEEP[1]]
    _KEEP_IDS = set(keep)
    best = (score(keep), keep)
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
    print("search score %.1f (2 per reviewed item dropped)" % v)
    assert v - 2 * len(_KEEP_IDS - set(sel)) < 1, "partition could not meet every constraint (score %.2f)" % v

    sets = {}
    for k, part in ((1, sel[:PER_SET]), (2, sel[PER_SET:])):
        qs = [POOL[i] for i in part]
        rot = rotate(qs, rng, k)
        pos = Counter(q["c"] for q in rot)
        frac = sum(gameable(q["opts"], q["c"]) for q in rot) / len(rot)
        assert frac <= BAR, "set%d: gameable %.0f%%" % (k, frac * 100)
        io = Counter("abcde"[IOS.index(q["io"])] for q in rot)
        sets["set%d" % k] = rot
        print("set%d  %d questions  positions=%s  gameable=%.1f%%  topics=%d  objectives=%s"
              % (k, len(rot), {chr(65 + p): c for p, c in sorted(pos.items())},
                 frac * 100, len({q["topic"] for q in rot}), dict(sorted(io.items()))))
    held = [POOL[i] for i in range(n) if i not in sel]
    out = os.path.join(HERE, "pdm_l21_sets.json")
    json.dump(sets, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    raw = sum(gameable(q["opts"], q["c"]) for q in POOL) / n
    print("pool %d (raw gameable %.1f%%)  wrote %s  (%d held back for the master exams)"
          % (n, raw * 100, os.path.basename(out), len(held)))
    for q in held:
        print("  held: %s" % q["q"][:90])


if __name__ == "__main__":
    main()
