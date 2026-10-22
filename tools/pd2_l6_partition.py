#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Split and guard the Physical Diagnosis 2 Lecture 6 pool into 2 x 30.

Advanced Thorax and Lung Physical Examination (Emily Crowe, DMSc, PA-C, guest),
delivered 2026-10-22. 119 questions in two files: landmarks, history, clubbing and
hemoptysis and the dyspnea comparison in pool A; the examination, breath sounds,
adventitious sounds, transmitted voice tests and the five conditions in pool B.

Adapted from the Lecture 5 driver (tools/pd2_l5_partition.py). The house guards are
kept as asserts: nothing may depend on having the deck open, no course mechanics, no
straying into pathophysiology (Clin Path I) or management (CMS I). Added for the
WRITER.md (v1) rules: every explanation refutes AND supplies the replacing fact
(60 characters or more, the site rule PD2 adopted 2026-09-22), every distractor names
its misconception (`mis`), and numeric option sets sit in ascending order with the
key where its value falls (tools/_option_order.py).

WEIGHTING is by minutes of lecture, measured on both transcripts (see the guide's
signposting table), then intersected with the deck: the examination itself (survey,
inspection, palpation, percussion, breath sounds) took about 27 of 90 minutes, the
history about 21, the adventitious sounds about 11, the dyspnea comparison about 9,
the landmarks about 9, the transmitted voice tests and five conditions about 8, and
clubbing with hemoptysis about 6. Per objective across the two sets:
a 6, b 10, c 5, d 8, e 9, f 9, g 13.

CONFLICTS: pairs whose stems answer each other (the trachea "pulled toward the lesion"
vignette and the "which way does the trachea move" item, for example) are kept in
different sets.
"""
import sys, os, json, random, re
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from pd2_l6_pool_a import POOL_A, IO_A, IO_B, IO_C, IO_D, IO_E, IO_F, IO_G
from pd2_l6_pool_b import POOL_B
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

# ---- Guard 4: the WRITER.md item shape --------------------------------------
_MIS = ("competing diagnosis", "wrong stage or severity", "ruled out by a stated finding",
        "confused mechanism or drug class", "adjacent fact", "reversed direction or value",
        "common lay belief")
_ABBR = re.compile(r"\b(COPD|COLD|PE|PTX|MI|ACS|GERD|OSA|TB|VTE|ICS|SCM|RUL|RML|RLL|LUL|LLL|AP|PND|"
                   r"CF|ILD|HF|ET|CXR|ABI|IBD|SOB|DOE)\b")
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
        if not q.get("cite", "").startswith("6. Thorax - Dr. Crowe.pptx, Slide"):
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
TARGET = ({IO_A: 3, IO_B: 5, IO_C: 3, IO_D: 4, IO_E: 4, IO_F: 5, IO_G: 6},
          {IO_A: 3, IO_B: 5, IO_C: 2, IO_D: 4, IO_E: 4, IO_F: 5, IO_G: 7})

# Objective f names five conditions: every set carries each of them at least once.
FIVE = ("Asthma", "Atelectasis", "Pneumonia", "Pneumothorax", "Pleural effusion")
# What the recording stressed (both transcripts; see the guide's signposting box): at
# least one item on each across the two sets.
STRESSED = [
    ("tracheal shift: atelectasis pulls, tension pushes",
     ("In which condition does the trachea shift TOWARD", "Diminished chest wall motion, narrowed",
      "After chest trauma, a patient has hyperresonance")),
    ("pleural rub disappears with a breath hold", ("A grating, creaking sound over the lower lateral",)),
    ("silent chest of asthma", ("During a severe asthma attack",)),
    ("stridor needs immediate intervention", ("A high-pitched inspiratory whistling", "Where and when is stridor")),
    ("copious foul sputum: cystic fibrosis or bronchiectasis", ("A patient coughs up large amounts",)),
    ("aspiration goes right", ("Aspirated material most often enters",)),
    ("bronchial sounds in the periphery mean consolidation", ("Bronchial breath sounds are heard over the lung bases",)),
]
assert all(sum(t.values()) == 30 for t in TARGET)
_have = Counter(q["io"] for q in POOL)
for io in TARGET[0]:
    assert _have[io] >= TARGET[0][io] + TARGET[1][io] + 1, (
        "objective %r has %d questions for %d places" % (io[:40], _have[io], TARGET[0][io] + TARGET[1][io]))

# ---- stems that answer each other: never in the same set ---------------------
CONFLICTS = [
    ("In which condition does the trachea shift TOWARD", "Diminished chest wall motion, narrowed intercostal"),
    ("In which condition does the trachea shift TOWARD", "After chest trauma, a patient has hyperresonance"),
    ("Over the left lower chest there is dullness", "Where may tactile fremitus be INCREASED"),
    ("Which chest wall deformity may compress", "The cross-section and the front view show the same chest"),
    ("Which breath sound is loud and relatively high-pitched", "A silent gap between inspiration"),
    ("Which breath sound is soft and relatively low-pitched", "Where are bronchovesicular breath sounds"),
    ("After surgery and days of immobility", "Which history raises suspicion for pulmonary embolism"),
    ("A patient with sudden dyspnea has a history of emphysema", "After a recent procedure, a patient with emphysema"),
    ("A patient reports musical breathing sounds", "Which adventitious sound is continuous and musical"),
    ("A high-pitched inspiratory whistling", "Where and when is stridor best heard"),
    ("Hyperresonance on only ONE side", "Which percussion note over the affected side fits a pneumothorax"),
    ("Asymmetric INCREASED tactile fremitus", "Which palpation finding fits lobar pneumonia"),
    ("Over the right lower chest there is dullness", "Which palpation finding fits lobar pneumonia"),
    ("Over the right lower chest there is dullness", "Asymmetric INCREASED tactile fremitus"),
    ("Over the right lower chest there is dullness", "In a patient with fever and cough"),
    ("Sharp chest pain is worse with inspiration and cough", "Which diagnosis belongs to the sharp, pleuritic"),
    ("Which percussion finding fits asthma", "Hyperresonance on only ONE side"),
    ("What percussion note does healthy lung produce", "Dullness to percussion over the lung means"),
    ("Which cause of pleural effusion is exudative", "Over the left lower chest there is dullness"),
]


def _find(key):
    stem, _, img = key.partition("#")
    hits = [i for i, q in enumerate(POOL) if q["q"].startswith(stem)
            and (not img or img in q.get("img", ""))]
    assert len(hits) == 1, "conflict key %r matches %d questions" % (key, len(hits))
    return hits[0]


CONFLICT_IDX = [(_find(a), _find(b)) for a, b in CONFLICTS]

random.seed(20261022 + 6)
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
    five = sum(1 for t in FIVE if not tops[t])
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
        assert all(tops[t] for t in FIVE), "a set lacks one of the five conditions: %r" % tops
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
            for L, io in zip("abcdefg", (IO_A, IO_B, IO_C, IO_D, IO_E, IO_F, IO_G))))
    unused = [POOL[i]["q"][:70] for i in range(len(POOL)) if i not in set(cur)]
    print("\n%d pool questions not used this run" % len(unused))

    with open(os.path.join(HERE, "pd2_l6_sets.json"), "w", encoding="utf-8") as fh:
        json.dump({"set1": sets[0], "set2": sets[1]}, fh, ensure_ascii=False, indent=1)
    print("wrote pd2_l6_sets.json")
