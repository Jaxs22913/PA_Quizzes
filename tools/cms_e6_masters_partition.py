#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five CMS I Exam 6 (Respiratory Block Exam I) Master Exams, 5 x 60.

    python3 tools/cms_e6_masters_partition.py --draft     # every guarded candidate (for the review of new items)
    python3 tools/cms_e6_masters_partition.py             # FINAL: only items with a clean blind + audit record
    python3 tools/cms_e6_masters_partition.py --dry-run   # build and report, write nothing

Then tools/render_cms_e6_masters.py renders the five pages from the JSON.

Size: 5 x 60, the CMS default (memory master_exam_sizing; Exam 5 was 5 x 60 too). Copied from
cms_e5_masters_partition.py; what differs is listed here.

WHERE THE QUESTIONS COME FROM. The six lectures' topic pools (cms_e6l3N_pool_*.py, cms_e6l3N_vig_*.py),
loaded through cms_e6_partition.load_guarded (length fixes and reviewer patches applied, exactly as for the
topic quizzes) and put through cms_e6_partition.guard_all -- the SAME asserts the topic sets were built under.

REVIEW GATE (2026-10-30, the coordinator's brief: "only items with clean blind+audit records"). Two passes:
  --draft  draws from every guarded candidate except the ones a review has already flagged (blind pick
           differs from the key, ambiguous or insufficient, or an audit verdict other than pass). The draft
           forms are rendered and the never-reviewed items on them go through tools/blind_review.py.
  final    (no flag) draws ONLY from items whose record in tools/blind_review.json has a blind pick equal to
           the key AND a CURRENT audit PASS (the audit hash covers the key and every explanation and `mis`).
           Every chosen item is asserted clean before anything is written.
A master question whose text matches a topic-quiz question is the same review item (the hash ignores option
order), so topic-quiz records carry over.

ALLOCATION: WEIGHTED BY SCHEDULED LECTURE HOURS (calendar-data.js): L33 1, L34 2, L35 2, L36 2, L37 3,
L38 1 -- 11 hours. Exact share per form 60 x h / 11: 5.45, 10.91, 10.91, 10.91, 16.36, 5.45. Whole parts
give 5/10/10/10/16/5 (56); largest remainders give Lectures 34-36 one more each (59); the last slot is a
tie between Lectures 33 and 38 (both .45, above Lecture 37's .36), so it ROTATES: Forms A, C, E give it to
Lecture 38, Forms B and D to Lecture 33. Totals over the five forms: L33 27, L34 55, L35 55, L36 55,
L37 80, L38 28 (exact 27.3/54.5/54.5/54.5/81.8/27.3).

MIX: 48 VIGNETTE + 12 REGULAR per form (80% patient stems), as Exams 4 and 5. Each lecture's regular count
is the largest remainder of 12 x its slots / 60; ties rotate form by form.

DIAGNOSIS LEAD-INS: Exam 5's hard 10-13 range does not carry over -- these pools hold few diagnosis
vignettes (acid-base naming is most of them). The range is set from the candidates: the diagnosis share of
the eligible vignettes x 48, plus or minus 2 (printed). No vignette lead-in above 40% of a form's vignettes.

STRATIFICATION, REQUIRED CONTENT, GAMEABLE, POSITIONS: as Exam 5 (each scope's REQUIRED content in every
form, at most one form short; length-gameable 0 per form; keys permuted PER FORM onto an exact 15/15/15/15
A-D cycle, ordered numeric options kept ascending).
"""
import sys, os, json, random, re, importlib, copy, math
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

_argv = sys.argv
sys.argv = [_argv[0], "l33io"]            # cms_e6_partition reads argv[1] at import
import cms_e6_partition as P
sys.argv = _argv
import blind_review as BR

FOLDER = "Clinical Medicine and Surgery I Exam 6"
FORMS = ["A", "B", "C", "D", "E"]
LECS = ["l33", "l34", "l35", "l36", "l37", "l38"]
LEC_NAME = {"l33": "L33 Oxygen Delivery", "l34": "L34 Acid-Base", "l35": "L35 Asthma",
            "l36": "L36 COPD", "l37": "L37 Respiratory Infections", "l38": "L38 Mycobacterial Infections"}
HOURS = {"l33": 1, "l34": 2, "l35": 2, "l36": 2, "l37": 3, "l38": 1}     # calendar-data.js
TIE_ROTATION = ["l38", "l33"]              # the L33/L38 tie slot: Forms A, C, E -> L38; B, D -> L33
PER_FORM = 60
N_REG = 12
SKEW_CAP = 0.40
SEED = int(os.environ.get("CMS_E6_MASTERS_SEED", "20261030"))
DRAFT = "--draft" in sys.argv


def allocation():
    H = sum(HOURS.values())
    out = []
    for f in range(len(FORMS)):
        exact = {l: PER_FORM * HOURS[l] / H for l in LECS}
        alloc = {l: int(exact[l]) for l in LECS}
        left = PER_FORM - sum(alloc.values())
        rem = sorted(LECS, key=lambda l: -round(exact[l] - alloc[l], 9))
        top = [l for l in rem if round(exact[l] - int(exact[l]), 9) > 0.5]      # Lectures 34-36 (.91)
        for l in top[:left]:
            alloc[l] += 1
        left = PER_FORM - sum(alloc.values())
        if left:
            assert left == 1, left
            alloc[TIE_ROTATION[f % 2]] += 1
        ex = {l: N_REG * alloc[l] / PER_FORM for l in LECS}
        reg = {l: int(ex[l]) for l in LECS}
        spare = N_REG - sum(reg.values())
        order = sorted(LECS, key=lambda l: (-round(ex[l] - reg[l], 9), (LECS.index(l) - f) % len(LECS)))
        for l in order[:spare]:
            reg[l] += 1
        out.append({l: {"reg": reg[l], "vig": alloc[l] - reg[l]} for l in LECS})
    return out


PER = allocation()
for f, a in enumerate(PER):
    assert sum(v["reg"] + v["vig"] for v in a.values()) == PER_FORM, a
    assert sum(v["reg"] for v in a.values()) == N_REG, a
TOTAL = {l: sum(PER[f][l]["reg"] + PER[f][l]["vig"] for f in range(len(FORMS))) for l in LECS}
assert TOTAL == {"l33": 27, "l34": 55, "l35": 55, "l36": 55, "l37": 80, "l38": 28}, TOTAL

SLOT_GROUP = {
    "etiology": "cause/risk", "epidemiology": "cause/risk", "risk factors": "cause/risk",
    "manifestation": "presentation", "differential": "presentation",
    "initial test": "test", "gold standard": "test", "test finding": "test",
    "first-line": "treatment", "escalation": "treatment", "agent/regimen": "treatment",
    "avoid": "avoid", "education": "education", "referral": "referral",
    "complication": "complication", "prognosis": "complication",
}


def review_state(rec, q):
    """'clean' (blind pick = key and a current audit pass), 'flagged' (any review says otherwise) or 'none'."""
    bq = BR.Q(FOLDER, "pool", 0, q)
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


BASE_LEADS = P.LEADS                       # imported as l33, which has no extra lead-ins
EXTRA_LEADS = {"l34": ("etiology", "compensation"), "l35": ("classify",), "l36": ("classify",),
               "l37": ("classify",), "l38": ("classify",)}       # as cms_e6_partition.py sets per lecture


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
            out.append(q)
        required = [(lab, re.compile(sr, re.I), re.compile(kr, re.I))
                    for lab, sr, kr, n in getattr(scope, "REQUIRED", ())]
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
        for sj in ("cms_e6%s_sets.json" % lec, "cms_e6%s_vig_sets.json" % lec):
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
            floor = len(hit) if len(hit) < len(FORMS) else len(FORMS) - 1
            pen += 400 * max(0, floor - cover)
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
        assert len(req_cover[(lec, lab)]) >= (len(hit) if len(hit) < len(FORMS) else len(FORMS) - 1), "%s %r only in forms %s" % (
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
            "fresh": q["_fresh"], "src": "%s[%d]" % tuple(q["_src"]), "c": q["c"],
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
    json.dump(report, open(os.path.join(HERE, "cms_e6_masters_report.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(path, ROOT), "and tools/cms_e6_masters_report.json (%s)" % report["mode"])
    return out, report


if __name__ == "__main__":
    build(dry_run="--dry-run" in sys.argv)
