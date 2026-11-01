#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the two CMS I Exam 6 "Lectures 37-38 Study Focus" sets, 30 questions each.

    python3 tools/cms_e6_focus_partition.py --draft    # review pass: every never-reviewed focus item is forced in
    python3 tools/cms_e6_focus_partition.py            # FINAL: only items with a clean blind + audit record
    python3 tools/cms_e6_focus_partition.py --dry-run  # build and report, write nothing

Then `python3 tools/render_cms_e6.py focus` renders cms-e6-l37-38-study-focus-set-1.html / -2.

WHY. Prof. Bobilin posted one study-focus slide per lecture on 2026-10-31 (L37 slide 127, L38 slide 41) and told
the class he wrote about 20 questions on Respiratory Infections and about 10 on the Mycobacterium lecture. Each set
follows that split: 20 Lecture 37 + 10 Lecture 38 questions, every one on a focus point
(tools/cms_e6_focus_points.py), aiming for EVERY focus point at least once per set.

WHERE THE QUESTIONS COME FROM. The Lecture 37/38 topic pools (cms_e6l3N_pool_*, cms_e6l3N_vig_*, loaded through
cms_e6_partition.load_guarded: patches and length fixes applied, the same guards) and the study-focus pools
(cms_e6l37_focus_pool/_vig, cms_e6l38_focus_vig) put through the same guards. Only questions that practise a
focus point are candidates.

REVIEW GATE, as the masters (cms_e6_masters_partition.review_state):
  --draft  every candidate not already flagged; every candidate with NO review record is forced in, so the
           draft pages carry all of them to tools/blind_review.py.
  final    only items whose blind pick equals the key AND whose audit is a current pass; asserted.

MIX: like the masters, 80% vignettes: per set L37 16 vignettes + 4 regular, L38 8 + 2 (soft in --draft).
NEAR-TWINS (same key text, three or more identical option texts, or stems at least 75% alike) never share a set.
POSITIONS: keys permuted onto an 8/8/7/7 A-D spread per set; numeric options stay ascending. Length-gameable
items: none (asserted in final; the brief's bar is under 10%).
"""
import sys, os, json, random, re, glob, importlib, math, copy, difflib
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
_argv = sys.argv; sys.argv = [_argv[0], "l37io"]
import cms_e6_partition as P
sys.argv = _argv
import cms_e6_masters_partition as M
import blind_review as BR
from cms_e6_focus_points import POINTS, POINT_IDS, focus_of

DRAFT = "--draft" in sys.argv
SEED = int(os.environ.get("CMS_E6_FOCUS_SEED", "20261031"))
OUT_JSON = os.path.join(HERE, "cms_e6_focus_sets.json")
REPORT = os.path.join(HERE, "cms_e6_focus_report.json")
QUOTA = {"l37": {"vig": 16, "reg": 4}, "l38": {"vig": 8, "reg": 2}}
PER_SET = 30
SKEW_CAP = 0.40
LEC_POINTS = {lec: [p[0] for p in POINTS if p[1] == lec] for lec in ("l37", "l38")}


def focus_modules(lec, vig):
    pat = "cms_e6%s_focus_%s.py" % (lec, "vig" if vig else "pool")
    return sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, pat)))


def review_state(rec, q):
    """As cms_e6_masters_partition.review_state, but independent of which sets file supplies `mis`: an audit
    record counts when its hash matches the question WITH its pool `mis` or WITHOUT any (a master-only question
    was audited with none). Sets q["_keep_mis"]: write the `mis` tags into tools/cms_e6_focus_sets.json only when
    the record was made with them (or there is no record yet, so the auditor sees them). This file sorts first
    among the tools/*_sets.json that blind_review.source_index reads, so what it says decides every page's join."""
    with_mis = BR.Q(M.FOLDER, "pool", 0, q)
    no_mis = BR.Q(M.FOLDER, "pool", 0, dict(q, opts=[o[:2] for o in q["opts"]]))
    q["_keep_mis"] = True
    b = BR.blind_of(rec, with_mis.h)
    if not b:
        return "none"
    if BR.norm(b.get("pick_text") or "") != BR.norm(with_mis.key_text):
        return "flagged"
    a = (rec.get(with_mis.h) or {}).get("passes", {}).get("audit")
    if not a:
        return "none"
    if a.get("ah") == with_mis.ah:
        return "clean" if a["verdict"] == "pass" else "flagged"
    if a.get("ah") == no_mis.ah:
        q["_keep_mis"] = False
        return "clean" if a["verdict"] == "pass" else "flagged"
    return "none"                                   # stale: the text changed since its audit


def load():
    rec = BR.load_records()
    out = []
    for lec in ("l37", "l38"):
        P.LEADS = M.BASE_LEADS + M.EXTRA_LEADS.get(lec, ())
        for vig in (False, True):
            scope, mods, pool, origin, _ = P.load_guarded(lec, vig)
            fpool, forig = [], []
            for m in focus_modules(lec, vig):
                for i, q in enumerate(importlib.import_module(m).QUESTIONS):
                    q = json.loads(json.dumps(q)); q.setdefault("c", 0)
                    fpool.append(q); forig.append((m, i))
            P.guard_all(scope, pool + fpool, origin + forig, vig)      # one guard run: duplicate stems span both
            for q, o in zip(pool + fpool, origin + forig):
                f = focus_of(q)
                if not f:
                    continue
                q = dict(q, _focus=f, _lec=lec, _kind="vig" if vig else "reg", _src="%s[%d]" % o,
                         _new="_focus_" in o[0])
                q["_state"] = review_state(rec, q)
                out.append(q)
    return out


def twin(a, b):
    if a["_lec"] != b["_lec"]:
        return False
    if BR.norm(a["opts"][0][0]).lower() == BR.norm(b["opts"][0][0]).lower():
        return True
    oa = {BR.norm(o[0]).lower() for o in a["opts"]}
    ob = {BR.norm(o[0]).lower() for o in b["opts"]}
    if len(oa & ob) >= 3:
        return True
    return difflib.SequenceMatcher(None, a["q"].lower(), b["q"].lower()).ratio() >= 0.75


def build(dry_run=False):
    rng = random.Random(SEED)
    POOL = load()
    POOL_ALL = list(POOL)
    print("focus candidates: %d  states %s" % (len(POOL), dict(Counter(q["_state"] for q in POOL))))
    if DRAFT:
        POOL = [q for q in POOL if q["_state"] != "flagged"]
    else:
        POOL = [q for q in POOL if q["_state"] == "clean"]
    FORCE = {i for i, q in enumerate(POOL) if DRAFT and q["_state"] == "none"}
    print("%s: %d candidates, %d forced (never reviewed)" % ("DRAFT" if DRAFT else "FINAL", len(POOL), len(FORCE)))
    G = [P.longest_is_correct(q) for q in POOL]
    N = len(POOL)
    TW = [[j for j in range(N) if j != i and twin(POOL[i], POOL[j])] for i in range(N)]
    groups = defaultdict(list)
    for i, q in enumerate(POOL):
        groups[(q["_lec"], q["_kind"])].append(i)
    for (lec, kind), idx in sorted(groups.items()):
        print("   %s %-3s %3d candidates (%d new, %d gameable)" % (lec, kind, len(idx),
              sum(POOL[i]["_new"] for i in idx), sum(G[i] for i in idx)))
    for lec in ("l37", "l38"):
        have = Counter(f for q in POOL if q["_lec"] == lec for f in q["_focus"])
        print("   %s points with fewer than 2 candidates: %s" % (lec, [p for p in LEC_POINTS[lec] if have[p] < 2]))

    def set_pen(sel):
        qs = [POOL[i] for i in sel]
        pen = 0.0
        for lec in ("l37", "l38"):
            got = Counter(f for q in qs if q["_lec"] == lec for f in q["_focus"])
            pen += 300 * sum(1 for p in LEC_POINTS[lec] if not got[p])
            pen += 6 * sum(max(0, c - 2) for c in got.values())
            for kind in ("vig", "reg"):
                n = sum(1 for q in qs if q["_lec"] == lec and q["_kind"] == kind)
                pen += (4 if DRAFT else 60) * abs(n - QUOTA[lec][kind])
            tops = Counter(q["topic"] for q in qs if q["_lec"] == lec)
            pen += 3 * sum(max(0, c - 3) for c in tops.values())
        pen += 400 * sum(G[i] for i in sel)
        s = set(sel)
        pen += 300 * sum(1 for i in sel for j in TW[i] if j in s) / 2
        leads = Counter(q["lead"] for q in qs if q["_kind"] == "vig")
        nv = sum(leads.values())
        pen += 200 * sum(max(0, c - nv * SKEW_CAP) for c in leads.values())
        return pen

    def total(sets):
        both = set(sets[0]) | set(sets[1])
        missing_forced = sum(1 for i in FORCE if i not in both)
        return set_pen(sets[0]) + set_pen(sets[1]) + 5000 * missing_forced      # forced: in one set or the other

    # initial deal: per (lec) fill each set to 30 lecture-proportionally, forced first
    sets = [[], []]
    for lec, n in (("l37", 20), ("l38", 10)):
        idx = [i for i in range(N) if POOL[i]["_lec"] == lec]
        rng.shuffle(idx)
        idx.sort(key=lambda i: (i not in FORCE, G[i]))
        take = idx[:2 * n]
        assert len(take) == 2 * n, "%s: only %d candidates for %d slots" % (lec, len(take), 2 * n)
        for k, i in enumerate(take):
            sets[k % 2].append(i)
    cur = total(sets)
    best = (cur, [list(s) for s in sets])
    STEPS, T0, T1 = 120000, 40.0, 0.05
    for step in range(STEPS):
        T = T0 * (T1 / T0) ** (step / STEPS)
        a = rng.randrange(2)
        k = rng.randrange(PER_SET)
        ia = sets[a][k]
        lec = POOL[ia]["_lec"]
        if rng.random() < 0.6:                         # swap in an unused candidate of the same lecture
            used = set(sets[0]) | set(sets[1])
            cands = [j for j in range(N) if POOL[j]["_lec"] == lec and j not in used]
            if not cands:
                continue
            ib = rng.choice(cands)
            sets[a][k] = ib
            t = total(sets)
            if t <= cur or rng.random() < math.exp((cur - t) / T):
                cur = t
            else:
                sets[a][k] = ia
        else:                                          # trade between the sets, same lecture
            b = 1 - a
            cand = [m for m, x in enumerate(sets[b]) if POOL[x]["_lec"] == lec]
            m = rng.choice(cand)
            sets[a][k], sets[b][m] = sets[b][m], sets[a][k]
            t = total(sets)
            if t <= cur or rng.random() < math.exp((cur - t) / T):
                cur = t
            else:
                sets[a][k], sets[b][m] = sets[b][m], sets[a][k]
        if cur < best[0]:
            best = (cur, [list(s) for s in sets])
    cur, sets = best
    print("local search settled at %.1f" % cur)

    # ---------------------------------------------------------------- asserts and report
    allsel = sets[0] + sets[1]
    assert len(allsel) == len(set(allsel)) == 2 * PER_SET
    assert not (FORCE - set(allsel)), "forced items left out: %r" % [POOL[i]["q"][:60] for i in FORCE - set(allsel)]
    report = {"mode": "draft" if DRAFT else "final", "seed": SEED, "sets": {}}
    out = {}
    for name, sel in zip(("set1", "set2"), sets):
        qs = [POOL[i] for i in sel]
        for lec, n in (("l37", 20), ("l38", 10)):
            assert sum(1 for q in qs if q["_lec"] == lec) == n, "%s: %s count" % (name, lec)
        s = set(sel)
        twins = [(POOL[i]["q"][:50], POOL[j]["q"][:50]) for i in sel for j in TW[i] if j in s and i < j]
        assert not twins, "%s near-twins: %r" % (name, twins)
        if not DRAFT:
            assert all(q["_state"] == "clean" for q in qs)
            assert sum(G[i] for i in sel) == 0, "%s has a length-gameable question" % name
        leads = Counter(q["lead"] for q in qs if q["_kind"] == "vig")
        assert max(leads.values()) <= sum(leads.values()) * SKEW_CAP, "%s lead skew %s" % (name, leads)
        cover = {lec: Counter(f for q in qs if q["_lec"] == lec for f in q["_focus"]) for lec in ("l37", "l38")}
        miss = [p for lec in ("l37", "l38") for p in LEC_POINTS[lec] if not cover[lec][p]]

        # order: shuffle, then keys onto an 8/8/7/7 spread, numeric options ascending
        qs = [copy.deepcopy(q) for q in qs]
        rng.shuffle(qs)
        fixed = {n: P.ascending(q).index(q["c"]) for n, q in enumerate(qs) if P.is_ordered(q)}
        want = [8, 8, 7, 7]
        rng.shuffle(want)
        for t in fixed.values():
            want[t] -= 1
        free = [k for k in range(4) for _ in range(max(0, want[k]))]
        assert len(free) == len(qs) - len(fixed), (len(free), len(qs), fixed)
        rng.shuffle(free)
        it = iter(free)
        for n, q in enumerate(qs):
            correct = q["opts"][q["c"]]
            if n in fixed:
                order = P.ascending(q)
                q["opts"] = [q["opts"][j] for j in order]
                q["c"] = order.index(q["c"])
                continue
            t = next(it)
            rest = [o for j, o in enumerate(q["opts"]) if j != q["c"]]
            rng.shuffle(rest)
            q["opts"] = rest[:t] + [correct] + rest[t:]
            q["c"] = t
            assert q["opts"][q["c"]] is correct
        for q in qs:
            assert re.match(r"correct\b", q["opts"][q["c"]][1], re.I)
        pos = Counter(q["c"] for q in qs)
        gam = sum(P.longest_is_correct(q) for q in qs)
        report["sets"][name] = {
            "positions": "/".join(str(pos.get(k, 0)) for k in range(4)),
            "gameable": gam, "gameable_pct": round(100.0 * gam / len(qs), 1),
            "vignettes": sum(q["_kind"] == "vig" for q in qs),
            "per_lecture": {lec: {kind: sum(1 for q in qs if q["_lec"] == lec and q["_kind"] == kind)
                                  for kind in ("vig", "reg")} for lec in ("l37", "l38")},
            "new_items": sum(q["_new"] for q in qs), "reused_items": sum(not q["_new"] for q in qs),
            "leads": dict(leads.most_common()),
            "points_missed": miss,
            "items": [{"lec": q["_lec"], "kind": q["_kind"], "src": q["_src"], "state": q["_state"],
                       "focus": q["_focus"], "c": "ABCD"[q["c"]], "q": q["q"]} for q in qs]}
        out[name] = []
        for q in qs:
            d = {k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite") if k in q}
            if not q["_keep_mis"]:
                d["opts"] = [o[:2] for o in q["opts"]]
            for k in ("slot", "lead"):
                if k in q:
                    d[k] = q[k]
            out[name].append(d)
        r = report["sets"][name]
        print("%s: positions %s  gameable %d (%.1f%%)  vignettes %d  new %d reused %d  per lecture %s  leads %s" % (
            name, r["positions"], gam, r["gameable_pct"], r["vignettes"], r["new_items"], r["reused_items"],
            r["per_lecture"], r["leads"]))
        print("   focus points missed: %s" % (miss or "none"))
    assert not (set(q["q"] for q in out["set1"]) & set(q["q"] for q in out["set2"]))
    report["mis_written"] = {name: sum(1 for q in out[name] if any(len(o) > 2 for o in q["opts"])) for name in ("set1", "set2")}
    if dry_run:
        print("--dry-run: nothing written")
        return out, report
    # Every study-focus pool question with its `mis`, so blind_review.source_index joins the misconception tags
    # wherever a new question ships (a master form too), not only in these two sets. Renderers read set1/set2.
    out["mis_source"] = [{k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite")} for q in POOL_ALL if q["_new"]]
    json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    json.dump(report, open(REPORT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote tools/%s and tools/%s (%s)" % (os.path.basename(OUT_JSON), os.path.basename(REPORT), report["mode"]))
    return out, report


if __name__ == "__main__":
    build(dry_run="--dry-run" in sys.argv)
