#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Physical Diagnosis 2 Lecture 7 pool into 2 x 30.

The Advanced Hematological Physical Examination (Matthew Ward, DMSc, MBA, PA-C),
delivered 2026-11-12. The causes and thresholds, the history and the skin, nail,
mucosal and node examination in pool A; the other organ systems, the emergency and the
interpretation in pool B.

Adapted from the Lecture 6 driver (tools/pd2_l6_partition.py); the same house guards
as asserts (nothing deck-dependent, no course mechanics, no pathophysiology or
management, WRITER.md item shape, 60-character explanations, ordered numeric options).
Added for this lecture: no laboratory indices or smear findings (the same week's CMS I
Lecture 46 and Clinical Pathophysiology Lecture 10, both Ward, teach those; this deck does
not), enforced as Guard 3b.

WEIGHTING is by minutes of lecture on the transcript (see the guide's signposting table
and recordings/pd2-l7-anemia-2026-11-12.flags.md), intersected with the deck.

CONFLICTS: a definition item and the picture of the same finding (glossitis, Cullen,
Grey Turner, petechiae, Romberg) never share a set, nor do stems that answer each other.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pd2_l7_pool_a import POOL_A, IO_A, IO_B, IO_C, IO_D
from pd2_l7_pool_b import POOL_B
from _option_order import option_values

POOL = POOL_A + POOL_B
EXAM_DIR = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2")

# ---- Guard 1: nothing may depend on having the deck open -------------------
_CTX = re.compile(r"on (?:this|the) slide|the slide (?:shows|says)|as shown (?:above|below)|"
                  r"in the (?:image|picture|photograph) (?:above|below|shown)|"
                  r"pictured (?:above|below)|the deck|the lecture|the lecturer|professor|"
                  r"powerpoint|the case study", re.I)
_ctx = [q["q"][:70] for q in POOL
        if _CTX.search(q["q"]) or any(_CTX.search(o[0]) or _CTX.search(o[1]) for o in q["opts"])]
assert not _ctx, "question depends on having the deck open: %r" % _ctx[:3]

# ---- Guard 2: no course mechanics -------------------------------------------
_MECH = re.compile(r"how many (?:points|questions) is|when is the (?:exam|osce)|what should you bring|"
                   r"which edition|bates|reading assignment|lab session|"
                   r"how (?:are you|will you be) graded|small group", re.I)
_mech = [q["q"][:70] for q in POOL if _MECH.search(q["q"]) or
         any(_MECH.search(o[0]) or _MECH.search(o[1]) for o in q["opts"])]
assert not _mech, "course-mechanics question in the pool: %r" % _mech[:3]

# ---- Guard 3: physical diagnosis, not pathophysiology or management --------
_SCOPE = re.compile(r"first[- ]line|drug of choice|what is the treatment|how (?:do|would) you treat|"
                    r"which antibiotic|which medication|molecular mechanism|pathogenesis of|cytokine|"
                    r"interleukin|apoptosis|\bdose\b|\bmg\b", re.I)
_sc = [q["q"][:70] for q in POOL if _SCOPE.search(q["q"])]
assert not _sc, "strays into pathophysiology or management: %r" % _sc[:3]

# ---- Guard 3b: the same-week overlap trap (CMS I L46, Clin Path L10) -------
_LAB = re.compile(r"mean corpuscular|ferritin|reticulocyte|smear|schistocyte|target cell|"
                  r"haptoglobin|lactate dehydrogenase|bone marrow biopsy|transferrin|"
                  r"hypersegmented|microcytic|normocytic|intrinsic factor|methylmalonic", re.I)
_lab = [q["q"][:70] for q in POOL if _LAB.search(q["q"]) or
        any(_LAB.search(o[0]) or _LAB.search(o[1]) for o in q["opts"])]
assert not _lab, "laboratory or smear content this deck does not teach: %r" % _lab[:3]

# ---- Guard 4: the WRITER.md item shape --------------------------------------
_MIS = ("competing diagnosis", "wrong stage or severity", "ruled out by a stated finding",
        "confused mechanism or drug class", "adjacent fact", "reversed direction or value",
        "common lay belief")
_ABBR = re.compile(r"\b(GI|IBS|IBD|NSAIDs?|G6PD|PNH|DIC|TTP|RBCs?|CBC|CKD|DPD|IPD|DRE|FOBT|Hgb|Hb|Hct|"
                   r"MCV|HF|SOB|DOE|ER)\b")
assert _ABBR.search("NSAIDs")
SLOTS = ("etiology", "epidemiology", "risk factors", "manifestation", "differential",
         "initial test", "gold standard", "test finding", "first-line", "escalation",
         "agent/regimen", "avoid", "education", "referral", "complication", "prognosis")

# Ordinal-rib / intercostal-space sets the numeric detector does not read (2nd vs 4th
# differ in their suffix): sorted by the ordinal here.
_ORD = re.compile(r"^(\d+)(?:st|nd|rd|th) (?:rib|intercostal space)$")


def ordinal_values(q):
    m = [_ORD.match(o[0]) for o in q["opts"]]
    return [int(x.group(1)) for x in m] if all(m) else None


def is_ordered(q):
    return option_values([o[0] for o in q["opts"]]) is not None or ordinal_values(q) is not None


def ascending(q):
    """Option indices in ascending display order."""
    vals = option_values([o[0] for o in q["opts"]])
    if vals is None:
        vals = [(v, v) for v in ordinal_values(q)]
    return sorted(range(4), key=lambda i: vals[i])


def validate(pool):
    bad = []
    stems = Counter(q["q"] for q in pool)
    for i, q in enumerate(pool):
        tag = "%d %s" % (i, q["q"][:50])
        if stems[q["q"]] > 1: bad.append((tag, "duplicate stem"))
        if len(q["opts"]) != 4: bad.append((tag, "not 4 options"))
        if q["c"] != 0: bad.append((tag, "key must be written first"))
        if not q.get("cite", "").startswith("Anemia-PDII-Ward-STUDENT-COPY-Updated.pptx, Slide"):
            bad.append((tag, "missing citation"))
        if q.get("slot") not in SLOTS: bad.append((tag, "bad slot"))
        if not q["q"].rstrip().endswith("?"): bad.append((tag, "stem does not ask"))
        if len(set(o[0].lower() for o in q["opts"])) != 4: bad.append((tag, "duplicate option text"))
        if not re.match(r"Correct\b", q["opts"][0][1]): bad.append((tag, "key explanation"))
        for j, o in enumerate(q["opts"]):
            if len(o[1].strip()) < 60:
                bad.append((tag, "explanation under 60 characters: %r" % o[1][:40]))
            if j and q["mis"].get(o[0]) not in _MIS:
                bad.append((tag, "distractor without a valid mis: %r" % o[0]))
            for t in (o[0], o[1]):
                m = _ABBR.search(t)
                if m: bad.append((tag, "abbreviation %r" % m.group(0)))
        if _ABBR.search(q["q"]): bad.append((tag, "abbreviation in stem"))
        if q.get("img"):
            if not os.path.exists(os.path.join(EXAM_DIR, q["img"])):
                bad.append((tag, "image file missing: " + q["img"]))
            if not q.get("alt") or not q.get("slide"):
                bad.append((tag, "image without alt text or slide caption"))
    return bad


# ---- weighting ---------------------------------------------------------------
TARGET = ({IO_A: 9, IO_B: 8, IO_C: 8, IO_D: 5},
          {IO_A: 9, IO_B: 8, IO_C: 8, IO_D: 5})

# Each set must reach every system the objectives name (objective c): at least one item on each.
SYSTEMS = (("Cardiovascular findings",), ("Pulmonary findings",),
           ("Gastrointestinal examination", "Stool blood testing", "Internal bleeding signs"),
           ("B12 neurologic findings", "Neurologic examination"))
# What the recording stressed (see the flags file and the guide's signposting box): at
# least one item on each across the two sets.
STRESSED = [
    ("fatigue is the most common, early symptom (1:27)", ("What is the most common symptom of anemia",)),
    ("rest symptoms, chest pain and syncope mark severity (3:43)", ("Which symptom in an anemic patient most strongly",)),
    ("pulse oximetry is normal in anemia, 'the main thing' (33:45)", ("What pulse oximetry reading is typical",)),
    ("the conjunctiva is his favorite pallor site (17:23)", ("Which part of the eye is inspected", "What does the pulled-down lower eyelid")),
    ("a negative stool test does not exclude bleeding (36:30)", ("An anemic patient's stool blood test is negative",)),
    ("Cullen and Grey Turner: uncommon, may be late, take seriously (38:25)",
     ("A patient with suspected internal bleeding has no Cullen",)),
    ("B12 deficiency without anemia or macrocytosis (40:20)", ("Can the neurologic findings of B12",)),
    ("hemoglobin can lag after acute blood loss (43:01)", ("A patient with acute hemorrhage has a normal",)),
]
assert all(sum(t.values()) == 30 for t in TARGET)
_have = Counter(q["io"] for q in POOL)
for io in TARGET[0]:
    assert _have[io] >= TARGET[0][io] + TARGET[1][io] + 1, (
        "objective %r has %d questions for %d places" % (io[:40], _have[io], TARGET[0][io] + TARGET[1][io]))

# ---- stems that answer each other: never in the same set ---------------------
CONFLICTS = [
    ("What is glossitis?", "What does this tongue show?"),
    ("What is Cullen sign?", "Which sign is shown on this patient's abdomen?"),
    ("What is Grey Turner sign", "Which sign is shown on this patient's side?"),
    ("What are petechiae?", "Which lesions cover the leg in this picture?"),
    ("What precaution is required during Romberg", "Which test is being performed in this picture?"),
    ("During Romberg testing, a patient becomes", "Which test is being performed in this picture?"),
    ("Which group of clues points to B12", "A patient has difficulty walking in the dark"),
    ("Which group of clues points to B12", "A patient with a previous gastric bypass reports"),
    ("A patient has difficulty walking in the dark", "A patient with a previous gastric bypass reports"),
    ("Which group of clues points to IRON", "A patient admits to craving and chewing ice"),
    ("Which symptom in an anemic patient most strongly", "Which finding in an anemic patient calls for urgent"),
    ("Which two factors shape how severe", "Two patients reach the same hemoglobin"),
    ("How reliable is pallor", "A patient's skin, conjunctivae and nail beds look"),
    ("Jaundice and scleral icterus in an anemic patient", "In an anemic patient, which condition does the finding"),
    ("Which cardiovascular finding is expected", "Which murmur may be heard"),
    ("Which cardiovascular finding is expected", "Which pulse finding may accompany"),
    ("Which spinal cord structures are affected", "Damage to the posterior columns"),
    ("Which spinal cord structures are affected", "Which motor finding may result"),
    ("What is koilonychia?", "Which deficiency is associated with the nail shown?"),
    ("Where should pallor be looked for?", "Which part of the eye is inspected"),
    ("Which part of the eye is inspected", "What does the pulled-down lower eyelid"),
    ("Which bleeding finding is looked for inside the mouth?", "What does the roof of this patient's mouth show?"),
    ("Which three measures assess clubbing?", "When the backs of matching fingers"),
    ("Which three measures assess clubbing?", "Which nail-fold profile angle"),
    ("What is melena?", "A patient reports red or maroon blood"),
    ("What is Cullen sign?", "What is Grey Turner sign"),
    ("A patient with acute hemorrhage has a normal", "What is the immediate response to an anemic patient"),
    ("Below which hemoglobin is a woman", "Below which hematocrit is a man"),
    ("Which three mechanisms account for anemia?", "Which cause of anemia works by IMPAIRED"),
]


def _find(key):
    stem, _, img = key.partition("#")
    hits = [i for i, q in enumerate(POOL) if q["q"].startswith(stem)
            and (not img or img in q.get("img", ""))]
    assert len(hits) == 1, "conflict key %r matches %d questions" % (key, len(hits))
    return hits[0]


CONFLICT_IDX = [(_find(a), _find(b)) for a, b in CONFLICTS]

random.seed(20261112 + 7)
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18


def longest_is_correct(q):
    lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
    (top_len, top_i), (runner, _) = lens[0], lens[1]
    if top_i != q["c"]:
        return False
    return (top_len - runner) >= MARGIN_CHARS and top_len >= runner * (1 + MARGIN_FRAC)


def gameable_pct(qs):
    return 100.0 * sum(longest_is_correct(q) for q in qs) / len(qs)


def score(setqs, target):
    ios = Counter(q["io"] for q in setqs)
    tops = Counter(q["topic"] for q in setqs)
    slots = Counter(q["slot"] for q in setqs)
    quota = sum(abs(ios[io] - n) for io, n in target.items())
    lumpy_t = sum(max(0, n - 3) for n in tops.values())
    lumpy_s = sum(max(0, n - 9) for n in slots.values())
    imgs = sum(1 for q in setqs if q.get("img"))
    img_pen = max(0, imgs - 4) + max(0, 2 - imgs)
    ids = set(id(q) for q in setqs)
    clash = sum(1 for a, b in CONFLICT_IDX if id(POOL[a]) in ids and id(POOL[b]) in ids)
    five = sum(1 for grp in SYSTEMS if not any(tops[t] for t in grp))
    return (quota * 40 + clash * 100 + five * 60 + lumpy_t * 6 + lumpy_s * 2 + img_pen * 10
            + gameable_pct(setqs) * 8.0)


STRESSED_IDX = [(lab, set(i for i, q in enumerate(POOL) if q["q"].startswith(stems)))
                for lab, stems in STRESSED]
for _lab, _ix in STRESSED_IDX:
    assert _ix, "stressed item not found: %s" % _lab


def total(sel):
    chosen = set(sel)
    missing = sum(1 for _lab, ix in STRESSED_IDX if not (ix & chosen))
    return (score([POOL[i] for i in sel[:30]], TARGET[0])
            + score([POOL[i] for i in sel[30:]], TARGET[1]) + missing * 80)


def place(qs):
    """Ordered questions sit where their key's value falls; the rest fill the
    positions so the set stays as even as possible."""
    fixed = {n: ascending(q).index(q["c"]) for n, q in enumerate(qs) if is_ordered(q)}
    want = [len(qs) // 4 + (1 if k < len(qs) % 4 else 0) for k in range(4)]
    random.shuffle(want)
    for t in fixed.values():
        want[t] -= 1
    free = []
    for k in range(4):
        free += [k] * max(0, want[k])
    while len(free) < len(qs) - len(fixed):
        free.append(min(range(4), key=lambda k: want[k] - free.count(k)))
    random.shuffle(free)
    it = iter(free[:len(qs) - len(fixed)])
    out = []
    for n, q in enumerate(qs):
        q = json.loads(json.dumps(q))
        if n in fixed:
            order = ascending(q)
            q["opts"] = [q["opts"][j] for j in order]
            q["c"] = order.index(q["c"])
        else:
            t = next(it)
            k = (t - q["c"]) % 4
            q["opts"] = q["opts"][-k:] + q["opts"][:-k] if k else q["opts"]
            q["c"] = t
        out.append(q)
    return out


if __name__ == "__main__":
    print("pool size:", len(POOL), " topics:", len(set(q["topic"] for q in POOL)))
    problems = validate(POOL)
    print("schema problems:", problems or "none")
    assert not problems, problems[:8]
    print("per objective in the pool:", {k[:24]: v for k, v in _have.items()})
    print("pool length-gameable: %.1f%%" % gameable_pct(POOL))
    print("house rules: no deck-dependent question, no course mechanics, no pathophysiology "
          "or management, no abbreviations, every explanation >= 60 characters, every distractor has a mis")
    print()

    idx = list(range(len(POOL)))
    best = None
    for _ in range(600):
        random.shuffle(idx)
        cand = idx[:60]
        t = total(cand)
        if best is None or t < best[0]:
            best = (t, list(cand))
    cur_score, cur = best
    outside = [i for i in range(len(POOL)) if i not in set(cur)]
    for _ in range(120000):
        if random.random() < 0.5:
            a, b = random.randrange(60), random.randrange(len(outside))
            cur[a], outside[b] = outside[b], cur[a]
            t = total(cur)
            if t <= cur_score:
                cur_score = t
            else:
                cur[a], outside[b] = outside[b], cur[a]
        else:
            a, b = random.randrange(30), random.randrange(30, 60)
            cur[a], cur[b] = cur[b], cur[a]
            t = total(cur)
            if t <= cur_score:
                cur_score = t
            else:
                cur[a], cur[b] = cur[b], cur[a]
    print("local search settled at score %.1f" % cur_score)

    answer_text = {i: POOL[i]["opts"][0][0] for i in cur}
    sets = []
    for part, target in ((cur[:30], TARGET[0]), (cur[30:], TARGET[1])):
        qs = place([POOL[i] for i in part])
        for i, q in zip(part, qs):
            assert q["opts"][q["c"]][0] == answer_text[i], "rotation moved an answer!"
            assert re.match(r"Correct\b", q["opts"][q["c"]][1])
            if is_ordered(q):
                assert ascending(q) == [0, 1, 2, 3], "ordered options not ascending: " + q["q"][:60]
        ios = Counter(q["io"] for q in qs)
        assert all(ios[io] == n for io, n in target.items()), "objective quota missed: %r" % ios
        ids = set(q["q"] for q in qs)
        for a, b in CONFLICT_IDX:
            assert not (POOL[a]["q"] in ids and POOL[b]["q"] in ids), \
                "conflicting pair in one set: %s / %s" % (POOL[a]["q"][:40], POOL[b]["q"][:40])
        tops = Counter(q["topic"] for q in qs)
        assert all(any(tops[t] for t in grp) for grp in SYSTEMS), "a set misses an organ system: %r" % tops
        g = gameable_pct(qs)
        assert g <= 10.0, "key longest in %.0f%% -- shorten the keys" % g
        sets.append(qs)
    chosen = set(cur)
    for lab, ix in STRESSED_IDX:
        assert ix & chosen, "no item on a stressed point: " + lab
    print("stressed points covered: %d of %d" % (len(STRESSED_IDX), len(STRESSED_IDX)))
    print("rotation check: every correct answer still points at its own text")
    print("conflict check: no pair of mutually answering stems shares a set\n")

    for name, s in zip(("SET 1", "SET 2"), sets):
        pos = Counter(q["c"] for q in s)
        print("%s  n=%d  positions A/B/C/D %s  gameable %.1f%%  topics %d  images %d  ordered %d"
              % (name, len(s), "/".join(str(pos.get(k, 0)) for k in range(4)), gameable_pct(s),
                 len(set(q["topic"] for q in s)), sum(1 for q in s if q.get("img")),
                 sum(1 for q in s if is_ordered(q))))
        print("      per objective: %s" % " ".join(
            "%s%d" % (L, sum(1 for q in s if q["io"] == io))
            for L, io in zip("abcd", (IO_A, IO_B, IO_C, IO_D))))
    unused = [POOL[i]["q"][:70] for i in range(len(POOL)) if i not in set(cur)]
    print("\n%d pool questions not used this run" % len(unused))

    with open(os.path.join(HERE, "pd2_l7_sets.json"), "w", encoding="utf-8") as fh:
        json.dump({"set1": sets[0], "set2": sets[1]}, fh, ensure_ascii=False, indent=1)
    print("wrote pd2_l7_sets.json")
