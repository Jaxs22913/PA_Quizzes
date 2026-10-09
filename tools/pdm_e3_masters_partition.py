#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five PDM I Exam 3 Master Exams, 5 x 60 (copied in shape from pdm_e2_masters_partition.py).

    python3 tools/pdm_e3_masters_partition.py            # build, report, write the JSON
    python3 tools/pdm_e3_masters_partition.py --dry-run  # build and report, write nothing

Then tools/render_pdm_e3_masters.py renders the five pages from the JSON, and tools/add_stable_qids.py
gives the new pages their permanent ids.

BLOCK. Exam 3 (Wed 2026-10-14) covers Lectures 11-16 AND Lab 3 (calendar-data.js). All six lecture decks
are in and built (11 Rhythm Analysis and Sinus Rhythms, 12 Ectopy, Escape Rhythms and Supraventricular
Dysrhythmias, 13 Ventricular Dysrhythmias and Atrioventricular Blocks, 14 Axis, Bundle Branch Blocks and
Chamber Enlargement, 15 Ischemia, Injury and Infarction, 16 Pericardial Disease, Electrolytes, Drug Effects
and Special ECG Patterns), so the hold rule is met. LAB 3 IS NOT BUILT: Jaxon, 2026-10-08, "Lectures only".
These forms cover the six LECTURES and the page says so.

ALLOCATION: WEIGHTED BY SCHEDULED LECTURE HOURS, five questions per hour (timetable_weighted_exams).
calendar-data.js: L11 Mon 10/05 10-12, L12 Mon 10/05 1-3, L13 Tue 10/06 10-12, L14 Tue 10/06 1-3,
L15 Wed 10/07 10-12, L16 Wed 10/07 1-3 = six two-hour lectures = 12 hours. Five per hour predicts 60, which
IS the form size (master_exam_sizing), so there is no gap this time: 10 per lecture per form.
alloc_by_hours() re-derives it and the build asserts it.

WHERE THE QUESTIONS COME FROM: the lectures' SHIPPED topic-quiz questions (tools/pdm_l1N_sets.json, which
are the pools after the 2026-10-08 fact-check fixes), verbatim. 10 per lecture per form x 5 forms = 50
distinct per lecture, and the topic quizzes hold 60 per lecture, so no held-back pool question is needed
and none is used: every question here has been through the fact-check and keeps its exact shipped text, so
its guide link and audit record carry over. (Exam 2 had to dip into held-back questions because it needed
75 per lecture; Exam 3 needs 50.) Each question is matched back to its pool entry by stem (asserted) to
pick up the pool-only fields (twin labels) and the Lecture 15/16 CONFLICTS lists.

STRIPS HEAVY (Jaxon, 2026-10-08). About half of the shipped questions show a rhythm strip or a 12-lead
from the slides; the selector prefers to keep picture questions (the 10 left out per lecture lean to text),
and spreads each lecture's pictures evenly over the five forms. A TRACING appears at most once per form:
two questions on the same slide's picture in one form would let the first answer the second, so the
identity is (lecture, slide), which also folds two crops of one picture together. Every alt text is
re-checked against its key.

STRATIFICATION (cms_ophtho_masters): every (lecture, lead-in) cell and every (lecture, objective) cell is
spread across the five forms within one of even, so no lecture, lead-in type or objective drops out of a
form unevenly. Simulated annealing (seeded) over swaps INSIDE a lecture (form <-> form, form <-> unused)
also keeps out of one form: two questions where one's KEY appears in the other's stem (cross-lecture
too: an L12 "atrial flutter" key and an L16 stem that names atrial flutter), the Lecture 15/16 TWINS and
CONFLICTS, two questions with the same key, and repeats of one topic.

POSITIONS: permuted PER FORM onto an exact 15/15/15/15 A-D cycle. Ten per lecture cannot split evenly
four ways, so each lecture runs 3/3/2/2 and the two heavy letters per lecture come from the six pairs of
{A,B,C,D} (each letter heavy in exactly three lectures), rotated per form; inside a lecture the cycle runs
down the (picture, lead-in)-sorted order so picture and lead-in cells are balanced too. The key is moved
and the distractors keep their order. Question order is shuffled with no answer letter more than three in
a row. Never render straight from a pool.
"""
import sys, os, json, random, re, importlib, copy, math
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

FOLDER = "Principles of Diagnostic Medicine I Exam 3"
FORMS = ["A", "B", "C", "D", "E"]
LECS = ["l11", "l12", "l13", "l14", "l15", "l16"]
LEC_NAME = {"l11": "L11 Rhythm Analysis & Sinus Rhythms",
            "l12": "L12 Ectopy, Escape & Supraventricular",
            "l13": "L13 Ventricular Dysrhythmias & AV Blocks",
            "l14": "L14 Axis, Bundle Branch Blocks & Enlargement",
            "l15": "L15 Ischemia, Injury & Infarction",
            "l16": "L16 Pericardial, Electrolytes, Drugs & Special"}
HOURS = {l: 2 for l in LECS}         # calendar-data.js lines 179-184, two hours each
POOLS = {l: "AB" for l in LECS}
PARTITION_EXTRAS = {"l15": "pdm_l15_partition", "l16": "pdm_l16_partition"}   # TWINS + CONFLICTS live there
PER_FORM, SEED = 60, 20261008
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
# Heavy (3-question) answer letters per lecture: the six pairs of {0,1,2,3}, each letter in three pairs.
PAIRS = [(0, 1), (2, 3), (0, 2), (1, 3), (0, 3), (1, 2)]
# Shipped stems that must not go into a master form (none at the time of the build).
EXCLUDE = set()

CITES = re.compile(r"(?i)\b(lecture|slides?|deck|professor|this course|in class|syllabus|lecturer)\b")


def alloc_by_hours(total=PER_FORM):
    H = sum(HOURS.values())
    exact = {l: total * HOURS[l] / H for l in LECS}
    out = {l: int(exact[l]) for l in LECS}
    left = total - sum(out.values())
    for l in sorted(LECS, key=lambda l: (-round(exact[l] - out[l], 9), LECS.index(l)))[:left]:
        out[l] += 1
    return out


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def key_longest(opts, c):
    return len(opts[c][0]) > max(len(o[0]) for j, o in enumerate(opts) if j != c)


def lead_in(q):
    """Coarse lead-in type of the question's own asking sentence (stratification only)."""
    s = q["q"].strip()
    last = re.split(r"(?<=[.!?;])\s+", s)[-1].lower()
    if re.search(r"\b(next step|next test|next study|most appropriate|should be ordered|which (initial |next |best |first )?(test|study|studies|lead|leads|tracing|investigation)\b)", last):
        return "test"
    if re.search(r"\bwhat is the rhythm|which rhythm|what rhythm|rhythm is (it|this|shown)|what is it\b", last):
        return "rhythm"
    if re.search(r"\b(axis|abnormality|block|pacing|enlargement|hypertrophy|pattern|finding|show|shows|region|wall|artery|localize|territory|interpretation|condition|disorder|toxicity|fits?)\b", last):
        return "interpret"
    if re.match(r"(why|how|what happens|what causes|on what|by what|what mechanism|what separates|which feature|which finding)", last):
        return "mechanism"
    if re.search(r"\b(rate|interval|duration|regularity)\b", last):
        return "measure"
    return "identify"


def _norm(t):
    t = t.lower(); t = re.sub(r"\([^)]*\)", "", t); t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\b(a|an|the|of|in|and|or|to|is|are|it|its)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def tracing(q):
    """(lecture, slide): two questions on one slide's picture are one tracing."""
    return (q["_lec"], q.get("slide")) if q.get("img") else None


def check_rules(q):
    """The standing content rules, re-asserted on every master question."""
    w = q["q"][:60]
    assert len(q["opts"]) == 4, w
    assert 0 <= q["c"] < 4, w
    assert q["q"].rstrip().endswith("?") and q["q"].count("?") == 1, "%s: one ask per stem" % w
    assert not CITES.search(q["q"]), "%s: stem cites the course" % w
    assert len({o[0] for o in q["opts"]}) == 4, "%s: duplicate option" % w
    assert q["opts"][q["c"]][1].startswith("Correct"), "%s: key explanation" % w
    for j, (t, e) in enumerate(q["opts"]):
        assert len(e) >= 60, "%s: explanation under 60 characters" % w
        assert not CITES.search(t) and not CITES.search(e), "%s: option cites the course" % w
        if j != q["c"]:
            assert not e.startswith("Correct"), "%s: distractor opens Correct" % w
    assert q.get("cite"), w
    if q.get("img"):
        assert q.get("alt") and q.get("slide"), "%s: picture without alt or slide" % w
        assert os.path.exists(os.path.join(ROOT, FOLDER, q["img"])), "%s: missing %s" % (w, q["img"])
        assert q["opts"][q["c"]][0].lower() not in q["alt"].lower(), "%s: alt names the answer" % w


def load():
    """Return ({lecture: [shipped question, key-first, with _ fields]}, conflict stems per lecture)."""
    out, conflicts = {}, {}
    for l in LECS:
        if l in PARTITION_EXTRAS:          # sets q["twin"] on the shared pool dicts and exposes CONFLICTS
            m = importlib.import_module(PARTITION_EXTRAS[l])
            conflicts[l] = getattr(m, "CONFLICTS", [])
        sets = json.load(open(os.path.join(HERE, "pdm_%s_sets.json" % l), encoding="utf-8"))
        pool = []
        for n in POOLS[l]:
            m = importlib.import_module("pdm_%s_pool_%s" % (l, n.lower()))
            pool += getattr(m, "POOL_%s" % n)
        by_stem = {}
        for q in pool:
            assert q["q"] not in by_stem, "duplicate pool stem " + q["q"][:60]
            by_stem[q["q"]] = q
        qs = []
        for k in sorted(sets):
            for s in sets[k]:
                assert s["q"] in by_stem, "%s: shipped stem not in the pool: %s" % (l, s["q"][:60])
                p = by_stem[s["q"]]
                s = copy.deepcopy(s)
                check_rules(s)
                key = s["opts"][s["c"]]
                rest = [o for i, o in enumerate(s["opts"]) if i != s["c"]]
                assert [key] + rest == p["opts"], "%s: shipped options drifted from the pool: %s" % (l, s["q"][:60])
                if s["q"] in EXCLUDE:
                    continue
                s["opts"] = [key] + rest
                s["c"] = 0
                s["_lec"] = l
                s["_set"] = k
                s["_lead"] = lead_in(s)
                s["_twin"] = (l, p["twin"]) if p.get("twin") else None
                qs.append(s)
        assert len(qs) == 60 - len([x for x in EXCLUDE if x in by_stem]), "%s: %d shipped" % (l, len(qs))
        out[l] = qs
    return out, conflicts


def pair_weights(items, conflicts):
    """{i: {j: weight}} for pairs that must not share a form."""
    W = defaultdict(dict)

    def add(i, j, w):
        if i == j:
            return
        W[i][j] = W[j][i] = max(W[i].get(j, 0), w)
    keys = [_norm(q["opts"][0][0]) for q in items]
    stems = [_norm(q["q"]) for q in items]
    toks = [set(s.split()) for s in stems]
    for i, k in enumerate(keys):
        if len(k) < 6:
            continue
        pat = re.compile(r"(?<![a-z0-9])" + re.escape(k) + r"(?![a-z0-9])")
        for j, st in enumerate(stems):
            if i != j and pat.search(st):
                add(i, j, 6 if " " in k else 2)      # a named answer handed over vs a single common word
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            a, b = items[i], items[j]
            if keys[i] == keys[j]:
                add(i, j, 3)                         # same answer twice in a form
            if a["q"] == b["q"]:
                add(i, j, 50)                        # one stem on two strips (L11 and L12): the page keys by stem
            if a["_twin"] and a["_twin"] == b["_twin"]:
                add(i, j, 8)
            if not a.get("img") and not b.get("img") and a["_lec"] == b["_lec"]:
                jac = len(toks[i] & toks[j]) / max(1, len(toks[i] | toks[j]))
                if jac >= 0.7:
                    add(i, j, 3)
    for l, cl in conflicts.items():
        for A, B in cl:
            ia = [i for i, q in enumerate(items) if q["_lec"] == l and any(x in q["q"] for x in A)]
            ib = [i for i, q in enumerate(items) if q["_lec"] == l and any(x in q["q"] for x in B)]
            for i in ia:
                for j in ib:
                    add(i, j, 8)
    return W


def main():
    dry = "--dry-run" in sys.argv
    rng = random.Random(SEED)
    alloc = alloc_by_hours()
    assert alloc == {l: 10 for l in LECS}, alloc
    assert sum(HOURS.values()) * 5 == PER_FORM
    data, conflicts = load()
    items = [q for l in LECS for q in data[l]]
    W = pair_weights(items, conflicts)
    NF = len(FORMS)
    UNUSED = NF                                       # bucket index for the questions left out
    idx_by_lec = {l: [i for i, q in enumerate(items) if q["_lec"] == l] for l in LECS}
    n_io = {l: len({items[i]["io"] for i in idx_by_lec[l]}) for l in LECS}

    # initial deal: per lecture, picture questions first so they are kept and spread, then round-robin
    bucket = [None] * len(items)
    for l in LECS:
        ids = idx_by_lec[l][:]
        rng.shuffle(ids)
        ids.sort(key=lambda i: (0 if items[i].get("img") else 1, items[i]["_lead"]))
        keep = alloc[l] * NF
        for k, i in enumerate(ids[:keep]):
            bucket[i] = k % NF
        for i in ids[keep:]:
            bucket[i] = UNUSED

    def members(b, l=None):
        return [i for i in range(len(items)) if bucket[i] == b and (l is None or items[i]["_lec"] == l)]

    def form_cost(ids):
        c = 0.0
        tr = Counter(tracing(items[i]) for i in ids if items[i].get("img"))
        c += sum(v - 1 for v in tr.values()) * 50
        s = set(ids)
        c += sum(w for i in ids for j, w in W[i].items() if j in s) / 2
        top = Counter((items[i]["_lec"], items[i]["topic"]) for i in ids)
        c += sum(max(0, v - 2) for v in top.values()) * 1.5
        lg = sum(key_longest(items[i]["opts"], 0) for i in ids)
        c += max(0, lg - 18) * 1.0
        c += sum(gameable(items[i]["opts"], 0) for i in ids) * 10
        return c

    def lec_cost(l):
        per = [[i for i in idx_by_lec[l] if bucket[i] == b] for b in range(NF)]
        c = 0.0
        for field, wgt in (("_lead", 4), ("io", 2), ("topic", 0.5)):
            vals = {items[i][field] for i in idx_by_lec[l] if bucket[i] != UNUSED}
            for v in vals:
                cnt = [sum(1 for i in p if items[i][field] == v) for p in per]
                c += max(0, max(cnt) - min(cnt) - 1) * wgt
        img = [sum(1 for i in p if items[i].get("img")) for p in per]
        c += max(0, max(img) - min(img) - 1) * 6
        c += sum(1 for i in idx_by_lec[l] if bucket[i] == UNUSED and items[i].get("img")) * 0.6
        # each form should reach as many of the lecture's objectives as it can
        c += sum(max(0, min(n_io[l], 7) - len({items[i]["io"] for i in p})) for p in per) * 1.0
        return c

    forms_ids = [members(b) for b in range(NF)]
    fcost = [form_cost(f) for f in forms_ids]
    lcost = {l: lec_cost(l) for l in LECS}
    cur = sum(fcost) + sum(lcost.values())
    best = (cur, bucket[:])
    steps = 120000
    for it in range(steps):
        T = 3.0 * (1 - it / steps) + 0.02
        l = LECS[rng.randrange(len(LECS))]
        i, j = rng.sample(idx_by_lec[l], 2)
        bi, bj = bucket[i], bucket[j]
        if bi == bj or (bi == UNUSED and bj == UNUSED):
            continue
        touched = {b for b in (bi, bj) if b != UNUSED}
        old = sum(fcost[b] for b in touched) + lcost[l]
        bucket[i], bucket[j] = bj, bi
        newf = {}
        for b in touched:
            ids = [x for x in forms_ids[b] if x not in (i, j)] + [x for x in (i, j) if bucket[x] == b]
            newf[b] = (ids, form_cost(ids))
        nl = lec_cost(l)
        new = sum(v[1] for v in newf.values()) + nl
        d = new - old
        if d <= 0 or rng.random() < math.exp(-d / T):
            for b, (ids, cst) in newf.items():
                forms_ids[b] = ids; fcost[b] = cst
            lcost[l] = nl
            cur += d
            if cur < best[0] - 1e-9:
                best = (cur, bucket[:])
        else:
            bucket[i], bucket[j] = bi, bj
    cur, bucket = best
    forms_ids = [members(b) for b in range(NF)]
    print("search cost %.2f (0 = every soft target met): forms %s, lectures %s"
          % (cur, [round(form_cost(f), 1) for f in forms_ids], {l: round(lec_cost(l), 1) for l in LECS}))

    # ---- hard assertions on the selection
    for fi, ids in enumerate(forms_ids):
        assert len(ids) == PER_FORM, (fi, len(ids))
        lc = Counter(items[i]["_lec"] for i in ids)
        assert all(lc[l] == alloc[l] for l in LECS), (fi, lc)
        tr = Counter(tracing(items[i]) for i in ids if items[i].get("img"))
        assert all(v == 1 for v in tr.values()), "Form %s repeats a tracing: %r" % (FORMS[fi], [k for k, v in tr.items() if v > 1])
    for l in LECS:
        assert sum(1 for i in idx_by_lec[l] if bucket[i] != UNUSED) == alloc[l] * NF

    # ---- positions, per form
    result = {}
    for fi, name in enumerate(FORMS):
        out, assign = [], []
        for li, l in enumerate(LECS):
            mine = sorted([items[i] for i in forms_ids[fi] if items[i]["_lec"] == l],
                          key=lambda q: (0 if q.get("img") else 1, q["_lead"], q["topic"], q["q"]))
            h1, h2 = PAIRS[(li + fi) % 6]
            h1, h2 = (h1 + fi) % 4, (h2 + fi) % 4
            light = [x for x in range(4) if x not in (h1, h2)]
            if rng.random() < 0.5:
                light.reverse()
            cyc = [h1, light[0], h2, light[1]]
            seq = (cyc * 3)[:len(mine)]           # 10 -> h1,l0,h2,l1,h1,l0,h2,l1,h1,l0 ... rebalance below
            cnt = Counter(seq)
            # exact 3/3/2/2 with the heavy letters h1, h2
            while cnt[h2] < 3:
                k = max(range(len(seq)), key=lambda k: (seq[k] not in (h1, h2) and cnt[seq[k]] > 2, k))
                cnt[seq[k]] -= 1; seq[k] = h2; cnt[h2] += 1
            assert sorted(cnt.values()) == [2, 2, 3, 3] and cnt[h1] == cnt[h2] == 3, (name, l, cnt)
            assign += [[q, want] for q, want in zip(mine, seq)]
        # Swap letters between two questions of ONE lecture (keeps 3/3/2/2 and 15 each) to even the
        # letters inside the picture questions and inside each lead-in type across the whole form.
        def pcost():
            c = 0.0
            pic = Counter(w for q, w in assign if q.get("img"))
            npic = sum(pic.values())
            c += sum((pic[x] - npic / 4) ** 2 for x in range(4))
            txt = Counter(w for q, w in assign if not q.get("img"))
            c += sum((txt[x] - (60 - npic) / 4) ** 2 for x in range(4))
            for ld in {q["_lead"] for q, _ in assign}:
                cc = Counter(w for q, w in assign if q["_lead"] == ld)
                n = sum(cc.values())
                c += 0.5 * sum((cc[x] - n / 4) ** 2 for x in range(4))
            return c
        pc = pcost()
        bylec = defaultdict(list)
        for k, (q, w) in enumerate(assign):
            bylec[q["_lec"]].append(k)
        for _ in range(4000):
            l = LECS[rng.randrange(len(LECS))]
            a, b = rng.sample(bylec[l], 2)
            if assign[a][1] == assign[b][1]:
                continue
            assign[a][1], assign[b][1] = assign[b][1], assign[a][1]
            nc = pcost()
            if nc <= pc:
                pc = nc
            else:
                assign[a][1], assign[b][1] = assign[b][1], assign[a][1]
        for q, want in assign:
            o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
            r = {kk: vv for kk, vv in q.items() if not kk.startswith("_")}
            r["opts"] = o; r["c"] = want
            r["_lec"] = q["_lec"]; r["_lead"] = q["_lead"]
            out.append(r)
        for _ in range(5000):
            rng.shuffle(out)
            run = mx = 1; runl = mxl = 1
            for a, b in zip(out, out[1:]):
                run = run + 1 if a["c"] == b["c"] else 1
                runl = runl + 1 if a["_lec"] == b["_lec"] else 1
                mx = max(mx, run); mxl = max(mxl, runl)
            if mx <= 3 and mxl <= 3:
                break
        assert mx <= 3 and mxl <= 3, (name, mx, mxl)
        result[name] = out

    stems = [(q["q"], q.get("img")) for n in FORMS for q in result[n]]
    assert len(stems) == len(set(stems)) == PER_FORM * NF, "a question appears in more than one form"
    for n in FORMS:     # the page keys class picks, ids and guide links by stem: one stem per form
        assert len({q["q"] for q in result[n]}) == PER_FORM, "Form %s repeats a stem" % n
    for n in FORMS:
        for q in result[n]:
            check_rules(q)

    # ---- report
    print("ALLOCATION (hours x 5 = %d predicted = form size %d): %s"
          % (sum(HOURS.values()) * 5, PER_FORM, {LEC_NAME[l]: alloc[l] for l in LECS}))
    report = {"alloc": alloc, "hours": HOURS, "forms": {}}
    for fi, name in enumerate(FORMS):
        f = result[name]
        pos = Counter(q["c"] for q in f)
        assert [pos[i] for i in range(4)] == [15, 15, 15, 15], (name, pos)
        gm = sum(gameable(q["opts"], q["c"]) for q in f)
        lg = sum(key_longest(q["opts"], q["c"]) for q in f)
        lec = Counter(q["_lec"] for q in f)
        img = sum(1 for q in f if q.get("img"))
        imgpos = Counter(q["c"] for q in f if q.get("img"))
        s = set(forms_ids[fi])
        leaks = sum(1 for i in forms_ids[fi] for j in W[i] if j in s) // 2
        print("Form %s: 60 q | A/B/C/D %d/%d/%d/%d | gameable %d (%.1f%%) | key longest %d (%.0f%%) | pictures %d (A-D %s) | residual pair flags %d"
              % (name, pos[0], pos[1], pos[2], pos[3], gm, gm / 60 * 100, lg, lg / 60 * 100, img,
                 "/".join(str(imgpos[i]) for i in range(4)), leaks))
        spread = {l: "".join("ABCD"[c] * n for c, n in sorted(Counter(q["c"] for q in f if q["_lec"] == l).items())) for l in LECS}
        per = {l: "%d (%d pic)" % (lec[l], sum(1 for q in f if q["_lec"] == l and q.get("img"))) for l in LECS}
        print("        per lecture:", per)
        print("        positions per lecture:", {l: dict(Counter("ABCD"[q["c"]] for q in f if q["_lec"] == l)) for l in LECS})
        report["forms"][name] = dict(gameable=gm, key_longest=lg, positions={"ABCD"[k]: v for k, v in sorted(pos.items())},
                                     pictures=img, picture_positions={"ABCD"[k]: v for k, v in sorted(imgpos.items())},
                                     per_lecture={l: lec[l] for l in LECS},
                                     per_lecture_pictures={l: sum(1 for q in f if q["_lec"] == l and q.get("img")) for l in LECS},
                                     lecture_positions=spread, residual_pair_flags=leaks,
                                     leadins=dict(Counter(q["_lead"] for q in f)))
    for field in ("_lead", "io"):
        cell = defaultdict(lambda: [0] * NF)
        for fi, name in enumerate(FORMS):
            for q in result[name]:
                cell[(q["_lec"], q[field])][fi] += 1
        worst = max(max(v) - min(v) for v in cell.values())
        print("(lecture, %s) cells: %d, widest spread across forms = %d" % (field.strip("_"), len(cell), worst))
        report["widest_spread_" + field.strip("_")] = worst
    unused = {l: sum(1 for i in idx_by_lec[l] if bucket[i] == UNUSED) for l in LECS}
    unused_img = {l: sum(1 for i in idx_by_lec[l] if bucket[i] == UNUSED and items[i].get("img")) for l in LECS}
    print("shipped questions left out per lecture: %s (of which pictures %s)" % (unused, unused_img))
    report["left_out"] = unused
    report["left_out_pictures"] = unused_img
    report["left_out_stems"] = sorted(items[i]["q"] for i in range(len(items)) if bucket[i] == UNUSED)
    out = {n: [{k: v for k, v in q.items() if not k.startswith("_")} for q in result[n]] for n in FORMS}
    if dry:
        return
    path = os.path.join(ROOT, FOLDER, "master-exams.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    rep = os.path.join(HERE, "pdm_e3_masters_report.json")
    json.dump(report, open(rep, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(path, ROOT), "and", os.path.basename(rep))


if __name__ == "__main__":
    main()
