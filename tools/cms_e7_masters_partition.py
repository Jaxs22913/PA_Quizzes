#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five CMS I Exam 7 (Respiratory Block Exam II, Lectures 39-45) Master Exams, 5 x 60.

    python3 tools/cms_e7_masters_partition.py --draft     # every guarded candidate not already flagged
    python3 tools/cms_e7_masters_partition.py             # FINAL: only items with a clean blind + audit record
    python3 tools/cms_e7_masters_partition.py --dry-run   # build and report, write nothing

Then tools/render_cms_e7_masters.py renders the five pages from the JSON.

Size: 5 x 60 (Jaxon 2026-11-02, "5 x 60"; memory cms_exam_spec). Copied from cms_e6_masters_partition.py
(2026-11-12); what differs is listed here.

WHERE THE QUESTIONS COME FROM. The seven lectures' topic pools (cms_e7l3N/l4N_pool_*.py, _vig_*.py), loaded
through cms_e7_partition.load_guarded (length fixes and reviewer patches applied, as for the topic quizzes) and
put through cms_e7_partition.guard_all -- the SAME asserts the topic sets were built under, with each lecture's
own lead-in vocabulary (l39 classify + physiology; l40-l44 classify; l45 etiology, compensation, classify).

REVIEW GATE: as Exam 6. --draft draws from every guarded candidate that no review has flagged; the
never-reviewed items on the draft forms go through tools/blind_review.py. FINAL (no flag) draws ONLY from
items whose record in tools/blind_review.json has a blind pick equal to the key AND a CURRENT audit PASS; every
chosen item is asserted clean before anything is written.

ALLOCATION: WEIGHTED BY SCHEDULED LECTURE HOURS (calendar-data.js): L39 1, L40 1, L41 2, L42 2, L43 2, L44 2,
L45 2 -- 12 hours, so exactly 5 questions per hour: per form L39 5, L40 5, L41-L45 10 each. No remainders, no
rotation. Totals over the five forms: L39 25, L40 25, L41-L45 50 each.

MIX: 48 VIGNETTE + 12 REGULAR per form (80% patient stems), as Exams 4-6. Regular per form: L39 1, L40 1,
L41-L45 2 each.

REQUIRED: each scope's REQUIRED / REQUIRED_IO / REQUIRED_VIG rows (content the lecturer said is on the test)
are preferred in every form, matched against both kinds. With up to 20 rows for a lecture holding 10 slots a
form, every row cannot reach every form: the assert is that each row reaches at least min(3, its question count)
forms; the coverage is printed.

DIAGNOSIS LEAD-INS: the range is set from the candidates (share of the eligible vignettes x 48, +-2), as Exam 6.
STRATIFICATION, GAMEABLE, POSITIONS: as Exam 6 (round-robin over (lecture, kind, lead) cells, length-gameable 0
per form; keys permuted PER FORM onto an exact 15/15/15/15 A-D cycle, ordered numeric options kept ascending).
"""
import sys, os, json, random, re, importlib, copy, math
from collections import Counter, defaultdict
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

_argv = sys.argv
sys.argv = [_argv[0], "l39io"]            # cms_e7_partition reads argv[1] at import
import cms_e7_partition as P
sys.argv = _argv
import blind_review as BR

FOLDER = "Clinical Medicine and Surgery I Exam 7"
FORMS = ["A", "B", "C", "D", "E"]
LECS = ["l39", "l40", "l41", "l42", "l43", "l44", "l45"]
LEC_NAME = {"l39": "L39 Phases of Sleep", "l40": "L40 Sleep Apnea and Hypoventilation",
            "l41": "L41 Inflammatory Lung Diseases", "l42": "L42 Pulmonary Vascular Disease",
            "l43": "L43 Nodules and Neoplasms", "l44": "L44 Pleural Disorders", "l45": "L45 Acid-Base II"}
HOURS = {"l39": 1, "l40": 1, "l41": 2, "l42": 2, "l43": 2, "l44": 2, "l45": 2}     # calendar-data.js
PER_FORM = 60
N_REG = 12
SKEW_CAP = 0.40
SEED = int(os.environ.get("CMS_E7_MASTERS_SEED", "20261112"))
DRAFT = "--draft" in sys.argv


def allocation():
    H = sum(HOURS.values())
    out = []
    for f in range(len(FORMS)):
        alloc = {l: PER_FORM * HOURS[l] // H for l in LECS}
        assert sum(alloc.values()) == PER_FORM and all(PER_FORM * HOURS[l] % H == 0 for l in LECS), alloc
        reg = {l: N_REG * alloc[l] // PER_FORM for l in LECS}
        assert sum(reg.values()) == N_REG, reg
        out.append({l: {"reg": reg[l], "vig": alloc[l] - reg[l]} for l in LECS})
    return out


PER = allocation()
for f, a in enumerate(PER):
    assert sum(v["reg"] + v["vig"] for v in a.values()) == PER_FORM, a
    assert sum(v["reg"] for v in a.values()) == N_REG, a
TOTAL = {l: sum(PER[f][l]["reg"] + PER[f][l]["vig"] for f in range(len(FORMS))) for l in LECS}
assert TOTAL == {"l39": 25, "l40": 25, "l41": 50, "l42": 50, "l43": 50, "l44": 50, "l45": 50}, TOTAL

SLOT_GROUP = {
    "etiology": "cause/risk", "epidemiology": "cause/risk", "risk factors": "cause/risk",
    "manifestation": "presentation", "differential": "presentation",
    "initial test": "test", "gold standard": "test", "test finding": "test",
    "first-line": "treatment", "escalation": "treatment", "agent/regimen": "treatment",
    "avoid": "avoid", "education": "education", "referral": "referral",
    "complication": "complication", "prognosis": "complication",
}


def review_state(rec, q):
    """'clean' (blind pick = key and a current audit pass), 'flagged' (any review says otherwise) or 'none'.
    The hashes are taken from the question AS ITS MASTER PAGE WILL READ IT: options without `mis`, then joined
    to their sources exactly as `blind_review.py check` joins a page (a question no sets file holds gets no
    `mis`), so a record counts here only if the final page will pass the check too."""
    bq = BR.attach_sources([BR.Q(FOLDER, "pool", 0, dict(q, opts=[o[:2] for o in q["opts"]]))])[0]
    b = BR.blind_of(rec, bq.h)
    if not b:
        return "none"
    if BR.norm(b.get("pick_text") or "") != BR.norm(bq.key_text):
        return "flagged"
    a = BR.audit_current(rec, bq)
    if not a:
        old = (rec.get(bq.h) or {}).get("passes", {}).get("audit")
        return "flagged" if old and old.get("verdict") != "pass" and old.get("ah") == bq.ah else "none"
    return "clean" if a["verdict"] == "pass" else "flagged"


BASE_LEADS = ("diagnosis", "next step", "treatment", "test", "education", "avoid", "complication", "referral")
EXTRA_LEADS = {"l39": ("classify", "physiology"), "l40": ("classify",), "l41": ("classify",),
               "l42": ("classify",), "l43": ("classify",), "l44": ("classify",),
               "l45": ("etiology", "compensation", "classify")}       # as cms_e7_partition.py sets per lecture


def load_lecture(lec):
    P.LEADS = BASE_LEADS + EXTRA_LEADS.get(lec, ())     # guard_all reads the module-level vocabulary
    out, required = [], []
    for kind, vig in (("reg", False), ("vig", True)):
        scope, mods, pool, origin, nfix = P.load_guarded(lec, vig)
        P.guard_all(scope, pool, origin, vig)           # asserts; a failure stops the build
        for q, o in zip(pool, origin):
            q["_src"] = o
            q["_kind"] = kind
            q["_lec"] = lec
            q["_focus"] = False
            out.append(q)
        for row in (list(getattr(scope, "REQUIRED", ())) + list(getattr(scope, "REQUIRED_IO", ()))
                    + list(getattr(scope, "REQUIRED_VIG", ()))):
            lab, sr, kr = row[:3]
            if lab not in {r[0] for r in required}:
                required.append((lab, re.compile(sr, re.I), re.compile(kr, re.I)))
    return out, required


def gameable(q):
    L = [len(o[0]) for o in q["opts"]]
    c = q["c"]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= P.MARGIN_CHARS and L[c] >= runner * (1 + P.MARGIN_FRAC)


def cell_lead(q):
    return q["lead"] if q["_kind"] == "vig" else SLOT_GROUP[q["slot"]]


def used_in_topic_sets():
    used = set()
    for lec in LECS:
        for sj in ("cms_e7%s_sets.json" % lec, "cms_e7%s_vig_sets.json" % lec):
            p = os.path.join(HERE, sj)
            S = json.load(open(p, encoding="utf-8"))
            used |= {(q["q"].strip(), q["opts"][q["c"]][0].strip()) for k in S for q in S[k]}
    return used


def build(dry_run=False):
    rng = random.Random(SEED)
    rec = BR.load_records()
    POOL, REQ = [], []
    for lec in LECS:
        qs, req = load_lecture(lec)
        POOL += qs
        for lab, srx, krx in req:
            REQ.append((lec, lab, srx, krx))

    states = [review_state(rec, q) for q in POOL]
    print("review records over %d guarded candidates: %s" % (len(POOL), dict(Counter(states))))
    keep = [i for i, s in enumerate(states) if (s == "clean" if not DRAFT else s != "flagged")]
    print("%s: %d candidates kept (%s)" % ("DRAFT" if DRAFT else "FINAL", len(keep),
          "every item not already flagged" if DRAFT else "clean blind + audit records only"))
    POOL = [POOL[i] for i in keep]
    STATE = [states[i] for i in keep]

    topic_used = used_in_topic_sets()
    for q in POOL:
        q["_fresh"] = (q["q"].strip(), q["opts"][0][0].strip()) not in topic_used

    NTOPICS = {lec: len({q["topic"] for q in POOL if q["_lec"] == lec}) for lec in LECS}
    stems = Counter(q["q"].strip().lower() for q in POOL)
    drop = set()
    for st in [s for s, n in stems.items() if n > 1]:
        same = [i for i, q in enumerate(POOL) if q["q"].strip().lower() == st]
        used = [i for i in same if not POOL[i]["_fresh"]]
        assert len(same) == 2 and len(used) <= 1, "duplicate stem across pools: %r" % st
        drop |= set(same[1:]) if not used else set(same) - set(used)
        print("duplicate stem %r: one copy kept" % st)
    POOL = [q for i, q in enumerate(POOL) if i not in drop]
    STATE = [s for i, s in enumerate(STATE) if i not in drop]

    req_hit = {}
    for lec, lab, srx, krx in REQ:
        hit = {i for i, q in enumerate(POOL) if q["_lec"] == lec
               and srx.search(q["q"]) and krx.search(q["opts"][0][0])}
        assert len(hit) >= 1, "%s %r: no such question" % (lec, lab)
        if len(hit) < len(FORMS):
            print("required %s %r: only %d such questions, so %d of %d forms" % (
                lec, lab, len(hit), len(hit), len(FORMS)))
        req_hit[(lec, lab)] = hit

    G = [gameable(q) for q in POOL]
    groups = defaultdict(list)
    for i, q in enumerate(POOL):
        groups[(q["_lec"], q["_kind"])].append(i)

    vig_all = [q for q in POOL if q["_kind"] == "vig"]
    share = sum(1 for q in vig_all if q["lead"] == "diagnosis") / max(1, len(vig_all))
    mid = 48 * share
    DX_RANGE = (max(0, int(math.floor(mid)) - 2), int(math.ceil(mid)) + 2)
    print("diagnosis share of eligible vignettes %.1f%% -> %.1f of 48; range per form %d-%d" % (
        100 * share, mid, DX_RANGE[0], DX_RANGE[1]))

    print("candidates after guards: %d" % len(POOL))
    print("per-form quotas (reg+vig): " + "  ".join(
        "%s %s" % (name, " ".join("%d+%d" % (PER[f][l]["reg"], PER[f][l]["vig"]) for l in LECS))
        for f, name in enumerate(FORMS)))
    for lec in LECS:
        for kind in ("reg", "vig"):
            idx = groups[(lec, kind)]
            need = sum(PER[f][lec][kind] for f in range(len(FORMS)))
            print("   %-30s %-3s %3d candidates  %3d fresh  %2d gameable  need %2d  cells=%s" % (
                LEC_NAME[lec], kind, len(idx), sum(POOL[i]["_fresh"] for i in idx),
                sum(G[i] for i in idx), need,
                dict(sorted(Counter(cell_lead(POOL[i]) for i in idx).items()))))
            assert len(idx) - sum(G[i] for i in idx) >= need, "%s %s: too few non-gameable candidates" % (lec, kind)

    def form_pen(f, sel):
        qs = [POOL[i] for i in sel]
        pen = 0.0
        pen += 400 * sum(G[i] for i in sel)
        leads = Counter(q["lead"] for q in qs if q["_kind"] == "vig")
        nv = sum(leads.values())
        pen += 300 * sum(max(0, c - nv * SKEW_CAP) for c in leads.values())
        dx = leads.get("diagnosis", 0)
        pen += 300 * (max(0, DX_RANGE[0] - dx) + max(0, dx - DX_RANGE[1]))
        for lec in LECS:
            lq = [q for q in qs if q["_lec"] == lec]
            tops = Counter(q["topic"] for q in lq)
            n = PER[f][lec]["reg"] + PER[f][lec]["vig"]
            pen += 8 * sum(max(0, c - 2) for c in tops.values())
            pen += 1.5 * (min(n, NTOPICS[lec]) - len(tops))
        keys = Counter(q["opts"][0][0].strip().lower() for q in qs)
        pen += 40 * sum(c - 1 for c in keys.values() if c > 1)
        pen += 1.0 * sum(1 for q in qs if not q["_fresh"])
        for (lec, lab), hit in req_hit.items():
            if not (hit & set(sel)):
                pen += 500
        return pen

    def strat_pen(forms):
        cnt = defaultdict(lambda: [0] * len(FORMS))
        for f, sel in enumerate(forms):
            for i in sel:
                q = POOL[i]
                cnt[(q["_lec"], q["_kind"], cell_lead(q))][f] += 1
        return 30 * sum(max(0, max(v) - min(v) - 1) for v in cnt.values())

    forms = [[] for _ in FORMS]
    for (lec, kind), idx in sorted(groups.items()):
        quota = [PER[f][lec][kind] for f in range(len(FORMS))]
        need = sum(quota)
        cells = defaultdict(list)
        for i in idx:
            cells[cell_lead(POOL[i])].append(i)
        for v in cells.values():
            rng.shuffle(v)
            v.sort(key=lambda i: (G[i], not POOL[i]["_fresh"]))
        order, k = [], 0
        while len(order) < need:
            progressed = False
            for c in sorted(cells):
                if k < len(cells[c]):
                    order.append(cells[c][k]); progressed = True
                    if len(order) == need:
                        break
            k += 1
            assert progressed
        f = 0
        for i in order:
            while sum(1 for x in forms[f] if (POOL[x]["_lec"], POOL[x]["_kind"]) == (lec, kind)) >= quota[f]:
                f = (f + 1) % len(FORMS)
            forms[f].append(i)
            f = (f + 1) % len(FORMS)

    fp = [form_pen(f, s) for f, s in enumerate(forms)]

    def req_pen(forms):
        sets = [set(sel) for sel in forms]
        pen = 0
        for hit in req_hit.values():
            cover = sum(1 for st in sets if hit & st)
            pen += 400 * max(0, min(3, len(hit)) - cover) + 40 * max(0, len(FORMS) - cover)
        return pen

    def total(forms, changed=()):
        for f in changed:
            fp[f] = form_pen(f, forms[f])
        return sum(fp) + strat_pen(forms) + req_pen(forms)

    cur = total(forms)
    print("\nstratified deal: score %.1f" % cur)
    chosen = {i for s in forms for i in s}
    STEPS, T0, T1 = 250000, 60.0, 0.05
    best = (cur, [list(s) for s in forms])
    for step in range(STEPS):
        T = T0 * (T1 / T0) ** (step / STEPS)
        f = rng.randrange(len(FORMS))
        a = rng.randrange(len(forms[f]))
        ia = forms[f][a]
        key = (POOL[ia]["_lec"], POOL[ia]["_kind"])
        if rng.random() < 0.5:
            ib = rng.choice(groups[key])
            if ib in chosen:
                continue
            forms[f][a] = ib
            t = total(forms, (f,))
            if t <= cur or rng.random() < math.exp((cur - t) / T):
                cur = t; chosen.discard(ia); chosen.add(ib)
            else:
                forms[f][a] = ia
                total(forms, (f,))
        else:
            g = rng.randrange(len(FORMS))
            if g == f:
                continue
            cand = [k for k, x in enumerate(forms[g]) if (POOL[x]["_lec"], POOL[x]["_kind"]) == key]
            if not cand:
                continue
            b = rng.choice(cand)
            forms[f][a], forms[g][b] = forms[g][b], forms[f][a]
            t = total(forms, (f, g))
            if t <= cur or rng.random() < math.exp((cur - t) / T):
                cur = t
            else:
                forms[f][a], forms[g][b] = forms[g][b], forms[f][a]
                total(forms, (f, g))
        if cur < best[0]:
            best = (cur, [list(s) for s in forms])
    cur, forms = best[0], best[1]
    print("local search settled at score %.1f (stratification part %.1f)" % (cur, strat_pen(forms)))

    # ---------------------------------------------------------------- hard asserts
    allsel = [i for s in forms for i in s]
    assert len(allsel) == len(set(allsel)) == PER_FORM * len(FORMS), "a question landed in two forms"
    assert len({POOL[i]["q"].strip().lower() for i in allsel}) == len(allsel)
    if not DRAFT:
        bad = [POOL[i]["q"][:70] for i in allsel if STATE[i] != "clean"]
        assert not bad, "FINAL forms hold items without a clean record: %r" % bad[:5]
    cnt = defaultdict(lambda: [0] * len(FORMS))
    for f, sel in enumerate(forms):
        for i in sel:
            cnt[(POOL[i]["_lec"], POOL[i]["_kind"], cell_lead(POOL[i]))][f] += 1
    spread = {k: max(v) - min(v) for k, v in cnt.items()}
    assert max(spread.values()) <= 2, "a (lecture, kind, lead) cell is uneven: %r" % {
        k: v for k, v in cnt.items() if max(v) - min(v) > 2}
    req_cover = {}
    for (lec, lab), hit in req_hit.items():
        req_cover[(lec, lab)] = [name for name, sel in zip(FORMS, forms) if hit & set(sel)]
        assert len(req_cover[(lec, lab)]) >= min(3, len(hit)), "%s %r only in forms %s" % (
            lec, lab, req_cover[(lec, lab)])
        print("required %s %r: forms %s" % (lec, lab, "".join(req_cover[(lec, lab)])))
    for f, (name, sel) in enumerate(zip(FORMS, forms)):
        assert len(sel) == PER_FORM
        for lec in LECS:
            for kind in ("reg", "vig"):
                n = sum(1 for i in sel if (POOL[i]["_lec"], POOL[i]["_kind"]) == (lec, kind))
                assert n == PER[f][lec][kind], "Form %s %s %s has %d" % (name, lec, kind, n)
        leads = Counter(POOL[i]["lead"] for i in sel if POOL[i]["_kind"] == "vig")
        assert DX_RANGE[0] <= leads.get("diagnosis", 0) <= DX_RANGE[1], "Form %s diagnosis %d" % (
            name, leads.get("diagnosis", 0))
        assert max(leads.values()) <= sum(leads.values()) * SKEW_CAP, "Form %s lead skew" % name
        assert sum(G[i] for i in sel) == 0, "Form %s has a length-gameable question" % name
    print("cells more than one apart across forms: %d of %d" % (sum(1 for v in spread.values() if v > 1), len(spread)))

    # ---------------------------------------------------------------- permute per form
    out = {}
    report = {"mode": "draft" if DRAFT else "final", "forms": {},
              "allocation": {name: PER[f] for f, name in enumerate(FORMS)},
              "required": {"%s %s" % k: v for k, v in req_cover.items()}}
    for name, sel in zip(FORMS, forms):
        qs = [copy.deepcopy(POOL[i]) for i in sel]
        rng.shuffle(qs)
        fixed = {n: P.ascending(q).index(q["c"]) for n, q in enumerate(qs) if P.is_ordered(q)}
        free = []
        for k in range(4):
            free += [k] * (len(qs) // 4 - sum(1 for t in fixed.values() if t == k))
        assert len(free) == len(qs) - len(fixed)
        rng.shuffle(free)
        it = iter(free)
        targets = [fixed[n] if n in fixed else next(it) for n in range(len(qs))]
        for q, t in zip(qs, targets):
            correct = q["opts"][q["c"]]
            if P.is_ordered(q):
                order = P.ascending(q)
                q["opts"] = [q["opts"][j] for j in order]
                q["c"] = order.index(q["c"])
                assert q["c"] == t
                continue
            rest = [o for j, o in enumerate(q["opts"]) if j != q["c"]]
            rng.shuffle(rest)
            q["opts"] = rest[:t] + [correct] + rest[t:]
            q["c"] = t
        for q in qs:
            assert re.match(r"correct\b", q["opts"][q["c"]][1], re.I)
            assert sum(1 for o in q["opts"] if re.match(r"correct\b", o[1].strip(), re.I)) == 1
        pos = Counter(q["c"] for q in qs)
        assert all(pos[k] == 15 for k in range(4)), pos
        assert not any(gameable(q) for q in qs)
        report["forms"][name] = [{
            "lec": q["_lec"], "kind": q["_kind"], "lead": cell_lead(q), "topic": q["topic"],
            "fresh": q["_fresh"], "focus": q["_focus"], "src": "%s[%d]" % tuple(q["_src"]), "c": q["c"],
            "q": q["q"]} for q in qs]
        out[name] = [{k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite")} for q in qs]

    for name in FORMS:
        r = report["forms"][name]
        print("  Form %s: %dq  vig %d  fresh %d  pos %s  per lecture %s  leads(vig) %s" % (
            name, len(r), sum(x["kind"] == "vig" for x in r), sum(x["fresh"] for x in r),
            "/".join(str(sum(1 for x in r if x["c"] == k)) for k in range(4)),
            "/".join(str(sum(1 for x in r if x["lec"] == l)) for l in LECS),
            dict(Counter(x["lead"] for x in r if x["kind"] == "vig").most_common())))

    if dry_run:
        print("--dry-run: nothing written")
        return out, report
    path = os.path.join(ROOT, FOLDER, "master-exams.json")
    open(path, "w", encoding="utf-8").write(json.dumps(out, indent=1, ensure_ascii=False))
    json.dump(report, open(os.path.join(HERE, "cms_e7_masters_report.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(path, ROOT), "and tools/cms_e7_masters_report.json (%s)" % report["mode"])
    return out, report


if __name__ == "__main__":
    build(dry_run="--dry-run" in sys.argv)
