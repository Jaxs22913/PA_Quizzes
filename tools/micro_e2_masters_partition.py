#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five Microbiology Exam 2 Master Exams, 5 x 60 (shape from pdm_e3_masters_partition.py).

    python3 tools/micro_e2_masters_partition.py            # build, report, write the JSON
    python3 tools/micro_e2_masters_partition.py --dry-run  # build and report, write nothing

Then tools/render_micro_e2_masters.py renders the five pages, and tools/add_stable_qids.py gives them ids.

BLOCK. Exam 2 (Friday 2026-10-23, calendar-data.js "EXAM #2 (7-13)") covers Lectures 7-13, all built:
7 Disorders in Immunity (Webster), 8 Diagnosing Infections (Fair), 9 Cocci of Medical Importance (Fair),
10 Gram-Positive Bacilli (Webster; deck file "Lecture 9"), 11 Novel Antimicrobial Therapy (Fair),
12 Epidemiology (Webster), 13 Miscellaneous Bacterial Agents (Fair).

ALLOCATION: by scheduled hours (timetable_weighted_exams). Every lecture is a two-hour slot (calendar-data.js
lines 143-144, 176-177, 188, 202-203), 14 hours; five per hour predicts 70, the form is 60 (master_exam_sizing),
so 60 x 2/14 = 8.57 per lecture: four lectures get 9 and three get 8 in each form, the four 9s rotating
form by form so each lecture totals 42-44 across the five forms.

WHERE THE QUESTIONS COME FROM: the FULL pools (tools/micro_l{7..13}_pool*.py, read through
micro_e2_sync_sets.pool_records), so a form is not only the topic quizzes again. Questions the topic quizzes
ship were blind-reviewed; a pool-only question costs a little in the search (POOL_ONLY_COST) so it is used
where it adds coverage, and every pool-only question chosen is listed in the report (master_only) for the
blind review export. Every question keeps its pool text verbatim.

PROFESSOR WEBSTER'S EXAM 2 REVIEW (16 October 2026, Lecture 12 recording part 4; page
micro-exam-2-webster-review.html) WEIGHTS HER THREE LECTURES. Every form carries at least one question for
each item she put at "Know cold":
  Lecture 7  objectives 2 (the four hypersensitivities), 3 (allergy diagnosis and treatment), 4 (ABO, Rh),
             7 (primary vs secondary immunodeficiency), 9 (immunotherapy)
  Lecture 10 Bacillus anthracis, spore position (central Bacillus / terminal Clostridium), C. perfringens,
             C. botulinum, C. difficile, Listeria, Corynebacterium diphtheriae, Mycobacterium leprae
  Lecture 12 objectives 1 (descriptive vs analytic), 3 (history, genomic epidemiology), 7 (incidence vs
             prevalence, mortality), 8 (association vs causation, Hill), 9 (endemic ... herd immunity, curves)
Her "Know it" items fill the remaining slots. Light-touch material contributes nothing: the Lecture 12 slides
13/23/25 questions are already out of the pool, and the Lecture 7 not-to-memorize charts (slides 6, 50,
58-60, 67) were never pooled. Dr. Fair's lectures (8, 9, 11, 13) stay purely hours-weighted: the review is
silent on them, which is not a skip. Lecture 10's own exclusions (Erysipelothrix, nontuberculous
mycobacteria: "don't worry about being tested") are kept out.

STRATIFICATION (cms_ophtho_masters): every (lecture, lead-in) and (lecture, objective) cell is spread
across the five forms within one of even. Simulated annealing (seeded) over swaps INSIDE a lecture keeps
out of one form: a question whose key appears in another's stem, two questions with one key, the topic
quizzes' near-twin CLUSTERS, near-identical stems, and one slide's picture twice.

POSITIONS: permuted PER FORM onto exactly 15/15/15/15, each lecture's letters as even as its 8 or 9 allow,
picture and lead-in letters balanced; no letter and no lecture more than three in a row.
"""
import sys, os, json, random, re, importlib, math
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import micro_e2_sync_sets as SS
import _option_order as OO

FOLDER = "Microbiology Exam 2"
FORMS = ["A", "B", "C", "D", "E"]
LECS = [7, 8, 9, 10, 11, 12, 13]
LEC_NAME = {7: "L7 Disorders in Immunity", 8: "L8 Diagnosing Infections", 9: "L9 Cocci",
            10: "L10 Gram-Positive Bacilli", 11: "L11 Novel Antimicrobial Therapy", 12: "L12 Epidemiology",
            13: "L13 Misc. Bacterial Agents"}
HOURS = {l: 2 for l in LECS}
PER_FORM, SEED = 60, 20261017
POOL_ONLY_COST = 2.0
RESTARTS = 4
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
# "slide" alone is a glass slide in Lecture 8/9 options; a course citation names a slide number or "the slides".
CITES = re.compile(r"(?i)\b(lecture|deck|professor|this course|in class|syllabus|lecturer)\b|\bslides? \d|"
                   r"\b(?:the|these|this) slides\b|\bon (?:the|this) slide\b")
EXCLUDE_RE = re.compile(r"(?i)erysipelothrix|nontuberculous|non-tuberculous|atypical mycobacteri")
# Pool-only questions kept out of the masters, with the reason (they were never shipped in a topic quiz).
SKIP_STEMS = {
    # Explanations give the current United States program (about 12 months tuberculoid); the slide says 6
    # months, and since 2026-10-15 the slide wins. Not worth a repair: the topic quizzes cover leprosy.
    "How does treatment of lepromatous leprosy compare with tuberculoid leprosy?",
}


def ion(q):
    return q["io"].split(" ")[0]


def l10_spore(q):
    """Spore POSITION (central Bacillus anthracis, terminal Clostridium): five questions, one per form
    (pools A/B hold three; pool M, written for the masters, adds two)."""
    t = (q["q"] + " " + q["opts"][0][0]).lower()
    return "spore" in t and any(w in t for w in ("central", "terminal", "where the spores sit"))


# (lecture, label, predicate) -- every form carries at least one of each
COLD = [(7, "obj 2 hypersensitivities", lambda q: ion(q) == "2"),
        (7, "obj 3 allergy", lambda q: ion(q) == "3"),
        (7, "obj 4 ABO / Rh", lambda q: ion(q) == "4"),
        (7, "obj 7 immunodeficiency", lambda q: ion(q) == "7"),
        (7, "obj 9 immunotherapy", lambda q: ion(q) == "9"),
        (10, "Bacillus anthracis", lambda q: q["topic"] == "Bacillus anthracis"),
        (10, "spore position", l10_spore),
        (10, "C. perfringens", lambda q: q["topic"] == "Clostridium perfringens"),
        (10, "C. botulinum", lambda q: q["topic"] == "Clostridium botulinum"),
        (10, "C. difficile", lambda q: q["topic"] == "Clostridioides difficile"),
        (10, "Listeria", lambda q: q["topic"] == "Listeria"),
        (10, "C. diphtheriae", lambda q: q["topic"] == "Corynebacterium"),
        (10, "M. leprae", lambda q: q["topic"] == "Leprosy"),
        (12, "obj 1 descriptive vs analytic", lambda q: ion(q) == "1"),
        (12, "obj 3 history / genomic", lambda q: ion(q) == "3"),
        (12, "obj 7 morbidity and mortality", lambda q: ion(q) == "7"),
        (12, "obj 8 association vs causation", lambda q: ion(q) == "8"),
        (12, "obj 9 endemic ... herd immunity", lambda q: ion(q) == "9")]


SPORE = [k for k, (_, lab, _) in enumerate(COLD) if lab == "spore position"][0]


def alloc_for(fi):
    """Four lectures get 9, three get 8; the four 9s rotate with the form."""
    nine = {LECS[(fi * 4 + k) % 7] for k in range(4)}
    return {l: 9 if l in nine else 8 for l in LECS}


def gameable(opts, c):
    L = [len(o[0]) for o in opts]
    r = max(L[:c] + L[c + 1:])
    return L[c] > r and (L[c] - r) >= MARGIN_CHARS and L[c] >= r * (1 + MARGIN_FRAC)


def key_longest(opts, c):
    return len(opts[c][0]) > max(len(o[0]) for j, o in enumerate(opts) if j != c)


def lead_in(q):
    if q.get("img"):
        return "picture"
    last = re.split(r"(?<=[.!?;])\s+", q["q"].strip())[-1].lower()
    if re.search(r"\b(transmit|transmitted|spread|vector|carrie[sd]|acquire|acquired|reservoir|route)\b", last):
        return "transmission"
    if re.search(r"\b(treat|treatment|therapy|drug|antibiotic|prevent|prevention|vaccine|vaccination)\b", last):
        return "treat"
    if re.search(r"\b(test|diagnos\w*|stain\w*|culture\w*|medium|media|agar|identify|detect\w*)\b", last):
        return "lab"
    if re.match(r"(why|how|what happens|what causes|by what|what makes|what does .* do)", last):
        return "mechanism"
    if re.search(r"\bwhich (organism|bacterium|bacteria|genus|species|pathogen|vibrio|disease|condition|type|"
                 r"term|stage|form|criterion|of hill)", last):
        return "identify"
    return "define"


def _norm(t):
    t = t.lower(); t = re.sub(r"\([^)]*\)", "", t); t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\b(a|an|the|of|in|and|or|to|is|are|it|its|by|for|with|on)\b", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def check_rules(q, where):
    w = "%s: %s" % (where, q["q"][:60])
    assert len(q["opts"]) == 4, w
    assert 0 <= q["c"] < 4, w
    assert q["q"].rstrip().endswith("?") and q["q"].count("?") == 1, "%s: one ask per stem" % w
    assert not CITES.search(q["q"]), "%s: stem cites the course" % w
    assert len({o[0] for o in q["opts"]}) == 4, "%s: duplicate option" % w
    assert q["opts"][q["c"]][1].startswith("Correct"), "%s: key explanation" % w
    for j, o in enumerate(q["opts"]):
        assert len(o[1]) >= 60, "%s: explanation under 60 characters" % w
        assert not CITES.search(o[0]) and not CITES.search(o[1]), "%s: option cites the course" % w
        if j != q["c"]:
            assert not o[1].startswith("Correct"), "%s: distractor opens Correct" % w
    assert q.get("cite"), w
    if q.get("img"):
        assert q.get("alt") and q.get("slide"), "%s: picture without alt or slide" % w
        assert os.path.exists(os.path.join(ROOT, FOLDER, q["img"])), "%s: missing %s" % (w, q["img"])


def clusters_for(l, pool_by_stem):
    """The topic quiz's near-twin clusters, as sets of stems (L10-L13 partitions define them)."""
    try:
        m = importlib.import_module("micro_l%d_partition" % l)
    except Exception:
        return []
    P = getattr(m, "POOL", None)
    out = []
    for n, cl in getattr(m, "CLUSTERS", []):
        stems = {P[i]["q"] for i in cl if P[i]["q"] in pool_by_stem}
        if len(stems) > 1:
            out.append((n, stems))
    return out


def load():
    items, clusters, dropped = [], [], Counter()
    for l in LECS:
        pool = SS.pool_records(l)
        sets = json.load(open(os.path.join(HERE, "micro_l%d_sets.json" % l), encoding="utf-8"))
        shipped = {q["q"] for qs in sets.values() for q in qs}
        assert shipped <= set(pool), "L%d: a shipped stem is not in the pool (run micro_e2_sync_sets.py)" % l
        for st, r in pool.items():
            assert r["c"] == 0, "L%d pool key not at position 0: %s" % (l, st[:60])
            text = " ".join([r["q"]] + [o[0] for o in r["opts"]])
            if EXCLUDE_RE.search(text) or st in SKIP_STEMS:
                dropped[l] += 1
                continue
            try:
                check_rules(r, "L%d" % l)
            except AssertionError as e:
                print("  skip (fails a house rule):", e)
                dropped[l] += 1
                continue
            q = {k: v for k, v in r.items() if k != "mis"}
            q = json.loads(json.dumps(q))
            q["_lec"] = l
            q["_shipped"] = st in shipped
            q["_lead"] = lead_in(q)
            q["_cold"] = [k for k, (cl, _, f) in enumerate(COLD) if cl == l and f(q)]
            items.append(q)
        for n, stems in clusters_for(l, pool):
            clusters.append((n, stems))
    return items, clusters, dropped


def pair_weights(items, clusters):
    W = defaultdict(dict)

    def add(i, j, w):
        if i != j:
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
                add(i, j, 6 if " " in k else 2)
    by_stem = {q["q"]: i for i, q in enumerate(items)}
    for n, stset in clusters:
        ids = [by_stem[s] for s in stset if s in by_stem]
        for a in ids:
            for b in ids:
                if a < b:
                    add(a, b, 8)
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if keys[i] == keys[j]:
                add(i, j, 3)
            if items[i]["_lec"] == items[j]["_lec"]:
                jac = len(toks[i] & toks[j]) / max(1, len(toks[i] | toks[j]))
                if jac >= 0.6:
                    add(i, j, 4)
    return W


def picture_id(q):
    return (q["_lec"], q.get("img")) if q.get("img") else None


def main():
    dry = "--dry-run" in sys.argv
    rng = random.Random(SEED)
    items, clusters, dropped = load()
    print("candidates per lecture:", {LEC_NAME[l]: sum(1 for q in items if q["_lec"] == l) for l in LECS},
          "| excluded:", dict(dropped))
    W = pair_weights(items, clusters)
    NF, UNUSED = len(FORMS), len(FORMS)
    allocs = [alloc_for(fi) for fi in range(NF)]
    for fi in range(NF):
        assert sum(allocs[fi].values()) == PER_FORM
    tot = {l: sum(a[l] for a in allocs) for l in LECS}
    print("per-lecture totals over five forms:", tot)
    idx_by_lec = {l: [i for i, q in enumerate(items) if q["_lec"] == l] for l in LECS}

    def form_cost(ids):
        c = 0.0
        pic = Counter(picture_id(items[i]) for i in ids if items[i].get("img"))
        c += sum(v - 1 for v in pic.values()) * 50
        s = set(ids)
        c += sum(w for i in ids for j, w in W[i].items() if j in s) / 2
        top = Counter((items[i]["_lec"], items[i]["topic"]) for i in ids)
        c += sum(max(0, v - 3) for v in top.values()) * 1.5
        c += sum(gameable(items[i]["opts"], 0) for i in ids) * 10
        lg = sum(key_longest(items[i]["opts"], 0) for i in ids)
        c += max(0, lg - 18) * 1.0
        have = Counter(k for i in ids for k in items[i]["_cold"])
        c += sum(25 for k in range(len(COLD)) if not have[k])
        c += max(0, have[SPORE] - 1) * 8          # one spore-position question per form
        c += sum(POOL_ONLY_COST for i in ids if not items[i]["_shipped"])
        return c

    def lec_cost(l, bucket):
        per = [[i for i in idx_by_lec[l] if bucket[i] == b] for b in range(NF)]
        c = 0.0
        for field, wgt in (("_lead", 3), ("io", 2), ("topic", 0.6)):
            vals = {items[i][field] for i in idx_by_lec[l] if bucket[i] != UNUSED}
            for v in sorted(vals):          # sorted: float sums in a fixed order keep the seeded run reproducible
                cnt = [sum(1 for i in p if items[i][field] == v) for p in per]
                c += max(0, max(cnt) - min(cnt) - 1) * wgt
        img = [sum(1 for i in p if items[i].get("img")) for p in per]
        c += max(0, max(img) - min(img) - 1) * 4
        n_io = len({items[i]["io"] for i in idx_by_lec[l]})
        c += sum(max(0, min(n_io, 7) - len({items[i]["io"] for i in p})) for p in per) * 1.5
        return c

    def search(rng):
        # initial deal: shipped first, then cold coverage, round-robin by need
        bucket = [UNUSED] * len(items)
        for l in LECS:
            ids = idx_by_lec[l][:]
            rng.shuffle(ids)
            ids.sort(key=lambda i: (0 if items[i]["_shipped"] else 1, 0 if items[i]["_cold"] else 1))
            need = [allocs[fi][l] for fi in range(NF)]
            f = 0
            for i in ids:
                if not any(need):
                    break
                while need[f % NF] == 0:
                    f += 1
                bucket[i] = f % NF
                need[f % NF] -= 1
                f += 1
            assert all(n == 0 for n in need), (l, need)

        forms_ids = [[i for i in range(len(items)) if bucket[i] == b] for b in range(NF)]
        fcost = [form_cost(f) for f in forms_ids]
        lcost = {l: lec_cost(l, bucket) for l in LECS}
        cur = sum(fcost) + sum(lcost.values())
        best = (cur, bucket[:])
        steps = 300000
        for it in range(steps):
            T = 3.0 * (1 - it / steps) + 0.02
            l = LECS[rng.randrange(len(LECS))]
            i, j = rng.sample(idx_by_lec[l], 2)
            bi, bj = bucket[i], bucket[j]
            if bi == bj:
                continue
            touched = {b for b in (bi, bj) if b != UNUSED}
            old = sum(fcost[b] for b in touched) + lcost[l]
            bucket[i], bucket[j] = bj, bi
            newf = {}
            for b in touched:
                ids = [x for x in forms_ids[b] if x not in (i, j)] + [x for x in (i, j) if bucket[x] == b]
                newf[b] = (ids, form_cost(ids))
            nl = lec_cost(l, bucket)
            d = sum(v[1] for v in newf.values()) + nl - old
            if d <= 0 or rng.random() < math.exp(-d / T):
                for b, (ids, cst) in newf.items():
                    forms_ids[b] = ids; fcost[b] = cst
                lcost[l] = nl
                cur += d
                if cur < best[0] - 1e-9:
                    best = (cur, bucket[:])
            else:
                bucket[i], bucket[j] = bi, bj
        return best

    # several seeded restarts of the annealing; the cheapest wins (ties: the earliest)
    runs = [search(random.Random(SEED + r)) for r in range(RESTARTS)]
    print("restart costs:", [round(r[0], 2) for r in runs])
    cur, bucket = min(runs, key=lambda r: r[0])
    forms_ids = [[i for i in range(len(items)) if bucket[i] == b] for b in range(NF)]
    print("search cost %.2f: forms %s | lectures %s" % (cur, [round(form_cost(f), 1) for f in forms_ids],
                                                       {l: round(lec_cost(l, bucket), 1) for l in LECS}))

    # ---- hard assertions
    for fi, ids in enumerate(forms_ids):
        lc = Counter(items[i]["_lec"] for i in ids)
        assert all(lc[l] == allocs[fi][l] for l in LECS), (fi, lc)
        pic = Counter(picture_id(items[i]) for i in ids if items[i].get("img"))
        assert all(v == 1 for v in pic.values()), "Form %s repeats a picture" % FORMS[fi]
        have = Counter(k for i in ids for k in items[i]["_cold"])
        missing = [COLD[k][1] for k in range(len(COLD)) if not have[k]]
        assert not missing, "Form %s misses Know-cold items: %s" % (FORMS[fi], missing)

    # ---- positions per form: exactly 15 each, each lecture as even as it can be
    result = {}
    for fi, name in enumerate(FORMS):
        qs = [items[i] for i in forms_ids[fi]]
        letters = [k % 4 for k in range(PER_FORM)]
        rng.shuffle(letters)
        want = letters[:]
        # numeric option sets keep ascending order, so their key letter is fixed (WRITER.md rule 8)
        fixed = {}
        for k, q in enumerate(qs):
            if OO.ordered_kind([o[0] for o in q["opts"]]):
                fixed[k] = OO.order_options(dict(opts=q["opts"], c=0))["c"]
        for k, f in fixed.items():
            if want[k] != f:
                m = next(m for m in range(PER_FORM) if m not in fixed and want[m] == f)
                want[k], want[m] = want[m], want[k]

        def pcost(w):
            c = 0.0
            for l in LECS:
                cc = Counter(w[k] for k, q in enumerate(qs) if q["_lec"] == l)
                c += 3 * (max(cc[x] for x in range(4)) - min(cc[x] for x in range(4)))
            for grp in sorted({q["_lead"] for q in qs}):
                cc = Counter(w[k] for k, q in enumerate(qs) if q["_lead"] == grp)
                n = sum(cc.values())
                c += 0.5 * sum((cc[x] - n / 4) ** 2 for x in range(4))
            pc = Counter(w[k] for k, q in enumerate(qs) if q.get("img"))
            n = sum(pc.values())
            c += sum((pc[x] - n / 4) ** 2 for x in range(4))
            return c
        pc = pcost(want)
        for _ in range(20000):
            a, b = rng.sample(range(PER_FORM), 2)
            if want[a] == want[b] or a in fixed or b in fixed:
                continue
            want[a], want[b] = want[b], want[a]
            nc = pcost(want)
            if nc <= pc:
                pc = nc
            else:
                want[a], want[b] = want[b], want[a]
        out = []
        for k, (q, w) in enumerate(zip(qs, want)):
            if k in fixed:
                srt = OO.order_options(dict(opts=q["opts"], c=0))
                o = srt["opts"]
                assert srt["c"] == w
            else:
                o = list(q["opts"]); key = o.pop(0); o.insert(w, key)
            r = {k: v for k, v in q.items() if not k.startswith("_")}
            r["opts"] = o; r["c"] = w
            r["_lec"] = q["_lec"]; r["_lead"] = q["_lead"]; r["_shipped"] = q["_shipped"]
            out.append(r)
        for _ in range(20000):
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

    stems = [q["q"] for n in FORMS for q in result[n]]
    assert len(stems) == len(set(stems)) == PER_FORM * NF, "a question appears twice"
    for n in FORMS:
        for q in result[n]:
            check_rules(q, "Form " + n)
            assert q["opts"][q["c"]][1].startswith("Correct")

    # ---- report
    report = {"allocations": {FORMS[fi]: {LEC_NAME[l]: allocs[fi][l] for l in LECS} for fi in range(NF)},
              "forms": {}}
    for fi, name in enumerate(FORMS):
        f = result[name]
        pos = Counter(q["c"] for q in f)
        assert [pos[i] for i in range(4)] == [15, 15, 15, 15], (name, pos)
        gm = sum(gameable(q["opts"], q["c"]) for q in f)
        lg = sum(key_longest(q["opts"], q["c"]) for q in f)
        lec = Counter(q["_lec"] for q in f)
        img = sum(1 for q in f if q.get("img"))
        po = sum(1 for q in f if not q["_shipped"])
        cold = Counter(COLD[k][1] for q in f for k in [kk for kk, (cl, _, fn) in enumerate(COLD) if cl == q["_lec"] and fn(q)])
        print("Form %s: A/B/C/D %d/%d/%d/%d | gameable %d (%.1f%%) | key longest %d (%.0f%%) | pictures %d | pool-only %d"
              % (name, pos[0], pos[1], pos[2], pos[3], gm, gm / 60 * 100, lg, lg / 60 * 100, img, po))
        print("        per lecture:", {l: lec[l] for l in LECS},
              "| letters per lecture:", {l: "".join(str(Counter(q["c"] for q in f if q["_lec"] == l)[x]) for x in range(4)) for l in LECS})
        report["forms"][name] = dict(positions={"ABCD"[k]: pos[k] for k in range(4)}, gameable=gm,
                                     gameable_pct=round(gm / 60 * 100, 1), key_longest=lg, pictures=img,
                                     pool_only=po, per_lecture={LEC_NAME[l]: lec[l] for l in LECS},
                                     know_cold={c[1]: cold[c[1]] for c in COLD},
                                     leadins=dict(Counter(q["_lead"] for q in f)))
    for field in ("_lead", "io"):
        cell = defaultdict(lambda: [0] * NF)
        for fi, name in enumerate(FORMS):
            for q in result[name]:
                cell[(q["_lec"], q[field])][fi] += 1
        worst = max(max(v) - min(v) for v in cell.values())
        print("(lecture, %s) cells: %d, widest spread across forms = %d" % (field.strip("_"), len(cell), worst))
        report["widest_spread_" + field.strip("_")] = worst
    mo = [dict(form=n, lecture=q["_lec"], q=q["q"]) for n in FORMS for q in result[n] if not q["_shipped"]]
    report["master_only"] = mo
    print("master-only (pool questions not in any topic quiz): %d -> %s"
          % (len(mo), dict(Counter(LEC_NAME[m["lecture"]] for m in mo))))
    out = {n: [{k: v for k, v in q.items() if not k.startswith("_")} for q in result[n]] for n in FORMS}
    if dry:
        return
    path = os.path.join(ROOT, FOLDER, "master-exams.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    rep = os.path.join(HERE, "micro_e2_masters_report.json")
    json.dump(report, open(rep, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(path, ROOT), "and", os.path.basename(rep))


if __name__ == "__main__":
    main()
