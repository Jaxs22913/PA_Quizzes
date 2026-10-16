#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five CMS I Exam 5 (Cardiology Block II) Master Exams, 5 x 60.

    python3 tools/cms_e5_masters_partition.py            # build, report, write the JSON
    python3 tools/cms_e5_masters_partition.py --dry-run  # build and report, write nothing

Then tools/render_cms_e5_masters.py renders the five pages from the JSON.

Size: 5 x 60, Jaxon's choice on 2026-10-15 ("CMS Exam 5 master exams = 5 forms x 60
questions, cumulative over Lectures 26-32"). Copied from cms_e4_masters_partition.py
(the Exam 4 build); what differs is listed here.

WHERE THE QUESTIONS COME FROM. The seven lectures' TOPIC POOLS (cms_e5l2N_pool_*.py,
cms_e5l2N_vig_*.py, cms_e5l3N_...), loaded through cms_e5_partition.load_guarded
(length fixes and reviewer patches applied, exactly as for the topic quizzes) and put
through cms_e5_partition.guard_all -- the SAME asserts the topic sets were built under.
The guards run on the WHOLE pool, so a pool that fails any guard stops the build.
Every question in those pools is a candidate, including the ones the topic partition
left out of the topic quizzes; the selector prefers those (a small bonus). All seven
lectures are on the guarded path (Exam 4's legacy Lecture 20 path is not carried over).

ALLOCATION: WEIGHTED BY SCHEDULED LECTURE HOURS, as Exam 4 was (Jaxon, 2026-09-27:
"Weight them by hours"). calendar-data.js gives every Exam 5 lecture two hours (26:
9/29; 27 and 28: 10/01; 29 and 30: 10/12; 31 and 32: 10/14), 14 hours in all, so each
lecture's exact share is 60 x 2 / 14 = 8.57 per form. Whole parts give 8 each (56);
the four slots left over in each form go to four lectures in a cycle over the seven
(EXTRA_ORDER), so across the five forms six lectures get 43 questions and one gets 42
-- the closest whole-number split of 300 x 2/14 = 42.86. Exam 4 broke ties by content;
here every lecture has the same hours and no lecture needs a fixed number of slots,
so the rotation is the fair choice.

MIX: 48 VIGNETTE + 12 REGULAR per form (80% patient stems), as Exam 4. Each lecture's
regular count is the largest remainder of 12 x its slots / 60 (a 9-slot lecture 1.8,
an 8-slot lecture 1.6): every 9-slot lecture takes 2, and the one regular slot left
goes to one 8-slot lecture in rotation (the others take 1).

STRATIFICATION: each (lecture, kind, lead-in) cell is spread across the five forms as
evenly as the per-form quotas allow (scored; at most two apart is asserted, because a
lecture's own quota differs by one between forms). Regular questions are stratified by
their fact slot's group (SLOT_GROUP).

WHAT THE LOCAL SEARCH HOLDS (hard = by construction or asserted)
  hard  the per-form (lecture, kind) quotas; no question in two forms
  hard  each lecture's REQUIRED content at least once in every form (the scope's own
        per-30 minimum is for a topic quiz; a lecture has 8-9 slots here); when a pool
        holds fewer than five such questions, each sits in a different form; at most one
        form may miss an item when the quotas make full coverage infeasible (Lecture 29)
  hard  diagnosis lead-ins 10-13 of the 60 per form; no vignette lead-in above 40% of a
        form's vignettes
  hard  length-gameable 0 per form
  soft  topic spread inside each lecture's share, no identical key twice in a form,
        prefer questions not already in the topic quizzes

POSITIONS: permuted PER FORM onto an exact 15/15/15/15 A-D cycle; the key is authored
first in every pool, so it is moved and the distractors shuffled.
"""
import sys, os, json, random, re, importlib, copy, math
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

_argv = sys.argv
sys.argv = [_argv[0], "l27io"]            # cms_e5_partition reads argv[1] at import
import cms_e5_partition as P
sys.argv = _argv

FOLDER = "Clinical Medicine and Surgery I Exam 5"
FORMS = ["A", "B", "C", "D", "E"]
LECS = ["l26", "l27", "l28", "l29", "l30", "l31", "l32"]
LEC_NAME = {"l26": "L26 Venous Disorders", "l27": "L27 Arterial Occlusive & Aneurysm",
            "l28": "L28 Cardiomyopathy", "l29": "L29 Arrhythmias I", "l30": "L30 Arrhythmias II",
            "l31": "L31 Pericardial Disease", "l32": "L32 Infective Endocarditis"}
HOURS = {l: 2 for l in LECS}                       # calendar-data.js, every lecture 2 hours
PER_FORM = 60
N_REG = 12
DX_RANGE = (10, 13)
SKEW_CAP = 0.40
SEED = int(os.environ.get("CMS_E5_MASTERS_SEED", "20261018"))   # best of 9 seeds after the L26-28 repair merge
EXTRA_ORDER = LECS                                 # the cycle the leftover slots follow
UNCHECKED_LECS = ("l26", "l27", "l28")             # pools whose never-shown questions need the master-only check

# Held out of the masters until repaired: questions a blind review flagged for revision or
# hold. Empty since the Lecture 26-28 repair merged (main a14caca4, 2026-10-15): the 15
# pilot-flagged stems are repaired or replaced, and every Lecture 26-28 topic-quiz question
# (360 of 360) carries a current PASS blind-review record (tools/blind_review.json).
# Matched on the stem's first 70 characters; each must match exactly one pool question.
HELD_FOR_REPAIR = []

# Held out after the master-only fact-check (2026-10-15): every Lecture 26-28 question these
# forms drew that no topic quiz shows was read against its deck by an independent checker;
# the first six were flagged (two defensible answers, a stem that names its answer, an
# explanation that is medically wrong, a key the guide corrects). The rest rest on a speaker
# note (Jaxon, 2026-10-15: notes do not count as slide content); live ones among them are the
# Lecture 26-28 repair's to fix, and are kept out of the masters until then. Left out here
# rather than rewritten, so this file never forks the Lecture 26-28 pools. Four stems the
# repair rewrote (main c1117deb/70f4bc6b) are no longer listed: their new versions are either
# on a topic quiz (blind-reviewed) or never shown and so not on the fact-checked list.
HELD_FACTCHECK = [
    "How much higher is the risk of recurrent deep vein thrombosis or pulmon",   # keys the slide's "30 times"; the guide teaches several-fold
    "A 68-year-old woman with chronic venous insufficiency has an itchy, re",   # rests on a speaker note (notes do not count, Jaxon 2026-10-15)
    "Which measure is used especially to prevent deep vein thrombosis in a ",   # rests on a speaker note (notes do not count, Jaxon 2026-10-15)
    "A 39-year-old man has a large proximal deep vein thrombosis together w",   # rests on a speaker note (notes do not count, Jaxon 2026-10-15)
    "A 68-year-old man with restrictive cardiomyopathy has worsening breath",   # rests on a speaker note (notes do not count, Jaxon 2026-10-15)
    "Which finding is most sensitive for a lower extremity deep vein thromb",   # rests on a speaker note
    "How reliable is the Homan sign (calf pain when the foot is flexed upwa",   # rests on a speaker note
    "Which study is the gold standard for diagnosing deep vein thrombosis?",   # rests on a speaker note
    "What is the mainstay of treatment for deep vein thrombosis?",   # rests on a speaker note
    "For which clot may thrombolysis be considered in deep vein thrombosis?",   # rests on a speaker note
    "A 68-year-old woman with active pancreatic cancer, which supplies the ",   # rests on a speaker note
    "A 66-year-old man who smokes and has hypertension had a transient isch",   # was the amaurosis fugax vignette (notes only); rewritten 2026-10-15 on slide 72, kept held so the seeded forms do not move
    "Which parasite causes dilated cardiomyopathy through Chagas disease?",   # rests on a speaker note
    "A 58-year-old woman with idiopathic dilated cardiomyopathy has taken a",   # rests on a speaker note
    "A 50-year-old man is newly diagnosed with dilated cardiomyopathy after",   # rests on a speaker note
    "A 41-year-old woman returns from a 14-hour flight and reports two days",
    "Which features separate a pseudoaneurysm from a true aneurysm?",
    "A 31-year-old tall man with Marfan syndrome develops sudden, severe, t",
    "Which is in the differential diagnosis of acute myocarditis?",
    "A 56-year-old man with dilated cardiomyopathy has an ejection fraction",
]


def allocation():
    """Per form: {lec: {"reg": n, "vig": n}}. See ALLOCATION and MIX in the docstring."""
    H = sum(HOURS.values())
    base = {l: int(PER_FORM * HOURS[l] / H) for l in LECS}
    left = PER_FORM - sum(base.values())
    out = []
    k = 0
    reg_turn = 0
    for f in range(len(FORMS)):
        alloc = dict(base)
        for _ in range(left):
            alloc[EXTRA_ORDER[k % len(EXTRA_ORDER)]] += 1
            k += 1
        exact = {l: N_REG * alloc[l] / PER_FORM for l in LECS}
        reg = {l: int(exact[l]) for l in LECS}
        spare = N_REG - sum(reg.values())
        # largest remainder; ties (the 8-slot lectures) rotate form by form
        order = sorted(LECS, key=lambda l: (-round(exact[l] - reg[l], 9),
                                            (LECS.index(l) - reg_turn) % len(LECS)))
        for l in order[:spare]:
            reg[l] += 1
        tied = [l for l in order[:spare] if round(exact[l] - int(exact[l]), 9) == min(
            round(exact[x] - int(exact[x]), 9) for x in order[:spare])]
        reg_turn += 1 if tied else 0
        out.append({l: {"reg": reg[l], "vig": alloc[l] - reg[l]} for l in LECS})
    return out


PER = allocation()
for f, a in enumerate(PER):
    assert sum(v["reg"] + v["vig"] for v in a.values()) == PER_FORM, a
    assert sum(v["reg"] for v in a.values()) == N_REG, a
TOTAL = {l: sum(PER[f][l]["reg"] + PER[f][l]["vig"] for f in range(len(FORMS))) for l in LECS}
assert sorted(TOTAL.values()) == [42] + [43] * 6, TOTAL

SLOT_GROUP = {
    "etiology": "cause/risk", "epidemiology": "cause/risk", "risk factors": "cause/risk",
    "manifestation": "presentation", "differential": "presentation",
    "initial test": "test", "gold standard": "test", "test finding": "test",
    "first-line": "treatment", "escalation": "treatment", "agent/regimen": "treatment",
    "avoid": "avoid", "education": "education", "referral": "referral",
    "complication": "complication", "prognosis": "complication",
}


def load_lecture(lec):
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
        for sj in ("cms_e5%s_sets.json" % lec, "cms_e5%s_vig_sets.json" % lec):
            S = json.load(open(os.path.join(HERE, sj), encoding="utf-8"))
            used |= {(q["q"].strip(), q["opts"][q["c"]][0].strip()) for k in S for q in S[k]}
    return used


def build(dry_run=False):
    rng = random.Random(SEED)
    POOL, REQ = [], []
    for lec in LECS:
        qs, req = load_lecture(lec)
        POOL += qs
        for lab, srx, krx in req:
            REQ.append((lec, lab, srx, krx))

    held = []
    for h in HELD_FOR_REPAIR + HELD_FACTCHECK:
        m = [i for i, q in enumerate(POOL) if q["q"].startswith(h)]
        assert len(m) == 1, "held stem %r matched %d pool questions" % (h, len(m))
        held += m
    POOL = [q for i, q in enumerate(POOL) if i not in set(held)]
    print("held out: %d (%d for repair, %d after the fact-check)" % (
        len(held), len(HELD_FOR_REPAIR), len(HELD_FACTCHECK)))

    topic_used = used_in_topic_sets()
    for q in POOL:
        q["_fresh"] = (q["q"].strip(), q["opts"][0][0].strip()) not in topic_used
    # A Lecture 26-28 question no topic quiz shows was never fact-checked with its quiz (the
    # Lecture 29-32 pools were checked whole), so it is drawn only if the master-only check
    # passed it (tools/cms_e5_masters_checked.json).
    checked = set(json.load(open(os.path.join(HERE, "cms_e5_masters_checked.json"), encoding="utf-8"))["stems"])
    unchecked = [i for i, q in enumerate(POOL) if q["_fresh"] and q["_lec"] in UNCHECKED_LECS
                 and q["q"][:70] not in checked]
    POOL = [q for i, q in enumerate(POOL) if i not in set(unchecked)]
    print("never-shown Lecture 26-28 questions not fact-checked, left out: %d" % len(unchecked))

    NTOPICS = {lec: len({q["topic"] for q in POOL if q["_lec"] == lec}) for lec in LECS}
    # The same stem in two lectures' pools (Lecture 28's and Lecture 31's "What is the
    # Kussmaul sign?"): keep the copy a topic quiz already uses, drop the other; any
    # other duplicate stops the build.
    stems = Counter(q["q"].strip().lower() for q in POOL)
    drop = set()
    for st in [s for s, n in stems.items() if n > 1]:
        same = [i for i, q in enumerate(POOL) if q["q"].strip().lower() == st]
        used = [i for i in same if not POOL[i]["_fresh"]]
        assert len(same) == 2 and len(used) == 1, "duplicate stem across pools: %r" % st
        drop |= set(same) - set(used)
        print("duplicate stem %r: kept the %s copy" % (st, POOL[used[0]]["_lec"]))
    POOL = [q for i, q in enumerate(POOL) if i not in drop]

    req_hit = {}
    for lec, lab, srx, krx in REQ:
        hit = {i for i, q in enumerate(POOL) if q["_lec"] == lec
               and srx.search(q["q"]) and krx.search(q["opts"][0][0])}
        # every form when the pool holds five such questions; otherwise each one in its own
        # form (Lecture 29's Wolff-Parkinson-White -> procainamide has four, so four forms)
        assert len(hit) >= 1, "%s %r: no such question" % (lec, lab)
        if len(hit) < len(FORMS):
            print("required %s %r: only %d such questions, so %d of %d forms" % (
                lec, lab, len(hit), len(hit), len(FORMS)))
        req_hit[(lec, lab)] = hit

    G = [gameable(q) for q in POOL]
    groups = defaultdict(list)
    for i, q in enumerate(POOL):
        groups[(q["_lec"], q["_kind"])].append(i)

    print("candidates after guards: %d" % len(POOL))
    print("per-form quotas (reg+vig): " + "  ".join(
        "%s %s" % (name, " ".join("%d+%d" % (PER[f][l]["reg"], PER[f][l]["vig"]) for l in LECS))
        for f, name in enumerate(FORMS)))
    for lec in LECS:
        for kind in ("reg", "vig"):
            idx = groups[(lec, kind)]
            need = sum(PER[f][lec][kind] for f in range(len(FORMS)))
            print("   %-34s %-3s %3d candidates  %3d fresh  %2d gameable  need %2d  cells=%s" % (
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

    # stratified deal: per (lecture, kind) group, round-robin over its lead cells, then
    # hand the dealt questions to the forms that still have room for that group
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
        """A required item short of every form costs 500 per missing form in form_pen; this
        adds 400 per form below a floor -- every one of a thin item's questions in its own
        form, and at most one miss for the rest -- so the misses Lecture 29's crowded quota
        forces spread one per item instead of piling onto one item."""
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
        # at most one form short of the target: Lecture 29 has five required items with 4-6
        # questions each, 2-3 of them regular, and only 9 regular L29 slots across the five
        # forms, so covering all five items in every form is infeasible (10 regular slots
        # would be forced); the search still tries for full coverage
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
    report = {"forms": {}, "allocation": {name: PER[f] for f, name in enumerate(FORMS)},
              "required": {"%s %s" % k: v for k, v in req_cover.items()}}
    for name, sel in zip(FORMS, forms):
        qs = [copy.deepcopy(POOL[i]) for i in sel]
        rng.shuffle(qs)
        # WRITER.md rule 8 (every lecture): an ordered question keeps its options
        # ascending, so its key sits where its value falls; the others fill the
        # remaining positions to exactly 15 each
        fixed = {n: P.ascending(q).index(q["c"]) for n, q in enumerate(qs) if P.is_ordered(q)}
        free = []
        for k in range(4):
            free += [k] * (len(qs) // 4 - sum(1 for t in fixed.values() if t == k))
        assert len(free) == len(qs) - len(fixed) and min(free.count(k) for k in range(4)) >= 0
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
    json.dump(report, open(os.path.join(HERE, "cms_e5_masters_report.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(path, ROOT), "and tools/cms_e5_masters_report.json")
    return out, report


if __name__ == "__main__":
    build(dry_run="--dry-run" in sys.argv)
