#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five CMS I Exam 4 (cardiology block I) Master Exams, 5 x 60.

    python3 tools/cms_e4_masters_partition.py            # build, report, write the JSON
    python3 tools/cms_e4_masters_partition.py --dry-run  # build and report, write nothing

Then tools/render_cms_e4_masters.py renders the five pages from the JSON.

Size: 5 x 60, Jaxon's choice on 2026-09-25 (Exam 1 shipped 60 and 65, Exam 2
65, Exam 3 50 -- see [[cms_exam_spec]]).

WHERE THE QUESTIONS COME FROM. Unlike Exams 2 and 3, whose masters were written
as separate master-only pools (cmsophtho_*, cmsent_*), Exam 4 has no master
pool. It draws from the six lectures' TOPIC POOLS (cms_e4l2N_pool_*.py and
cms_e4l2N_vig_*.py), the same way the Exam 1 originals reused the topic
quizzes (build_master_exams.py). Every question in those pools is a candidate,
including the ones the topic partition left out of the four topic quizzes;
the selector prefers those (a small bonus), so a student who has worked the
topic quizzes meets as much new material as the other rules allow.

  LECTURES 21-25 (Carter) load through cms_e4_partition.load_guarded and are
  put through cms_e4_partition.guard_all -- the SAME asserts the topic sets were
  built under: scope bans (SCOPE_BANNED, STEM_BANNED, TOPIC_BANNED, LINTS),
  excluded slides, dosing, brand names, mechanism-of-action stems, bare
  acronyms, US spelling, cross-question dependency, the vignette opening and the
  named-finding glosses. The guards run on the WHOLE pool, so nothing banned
  can be selected: a pool that fails any guard stops the build. The lecture's
  length fixes (cms_e4l2N_lengthfix.FIXES) are applied first, exactly as in the
  topic build.

  LECTURE 20 (Jaquith) was built on the legacy path, which has no guards and
  no lead-in labels. Here it gets the lecture-independent guards (dosing,
  brand names, bare acronyms, US spelling, dependency, stem ends on a
  question, vignette opens on a patient) after two MASTER-ONLY text repairs
  (L20_TEXT): "ACE inhibitor" is written out, per the no-abbreviations
  policy, and the British spelling of hyperkalemia is made US. The pool files are not
  touched, because re-running the legacy topic partition must keep
  reproducing the committed topic quizzes. Questions that still fail a guard
  are LEFT OUT and listed (DASH-style / STOP-BANG, the vignette-pool stems that
  do not open on a patient). Lead-ins for its 64 vignettes are labeled by hand
  in L20_LEAD, because regex classification is not enough ([[cms_exam_spec]]).

ALLOCATION: TEN PER LECTURE PER FORM. The Exam 3 precedent (the most recent
CMS master set) is an equal share per lecture, "ten from each"; neither CMS
precedent weights by scheduled hours. Six lectures into 60 is exactly 10, so
there is no rounding gap. The hours-weighted alternative (L25 is the only
three-hour lecture) is shown in MANIFEST.md for Jaxon to choose.

MIX: 8 VIGNETTE + 2 REGULAR per lecture per form (48 + 12 = 80% patient
stems). Exam 2's masters were 70% vignettes and Exam 3's were all patient
stems after its 2026-09-16 edit; 80% is the exam standard's floor for patient
stems (check_exam_standard.py) and Jaquith's "pretty much all clinical
vignettes" -- while keeping the recall questions the CMS spec's "mix" asks for.

STRATIFICATION, the Exam 2 lesson ([[cms_ophtho_masters]]): each (lecture,
kind, lead-in) cell is spread across the five forms at most one apart, so no
lecture and no lead-in type drops out of a form. Regular questions are
stratified by their fact slot's group (SLOT_GROUP).

WHAT THE LOCAL SEARCH HOLDS (hard = by construction or asserted)
  hard  exactly 8 vignettes + 2 regular per lecture per form; no question in two
        forms; every cell within one of even across forms
  hard  each lecture's REQUIRED content in every form (scope REQUIRED: L23
        mechanical valve -> warfarin, L24 troponin, L24 right-ventricular infarct
        -> no nitroglycerin, L25 Stage A diabetic -> sodium-glucose cotransporter 2
        inhibitor)
  hard  diagnosis lead-ins 10-13 of the 60 per form; no vignette lead-in above
        40% of a form's vignettes
  hard  length-gameable 0 per form (the selector has ~600 candidates and needs
        300; shorten-don't-pad is never needed if selection can reach zero)
  soft  topic spread inside each lecture's ten, no identical key twice in a
        form, prefer questions not already in the topic quizzes

POSITIONS: permuted PER FORM onto an exact 15/15/15/15 A-D cycle; the key is
authored first in every pool, so it is moved and the distractors shuffled.
"""
import sys, os, json, random, re, glob, importlib, copy
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

_argv = sys.argv
sys.argv = [_argv[0], "l21io"]            # cms_e4_partition reads argv[1] at import
import cms_e4_partition as P
sys.argv = _argv

FOLDER = "Clinical Medicine and Surgery I Exam 4"
FORMS = ["A", "B", "C", "D", "E"]
LECS = ["l20", "l21", "l22", "l23", "l24", "l25"]
LEC_NAME = {"l20": "L20 Hypertension", "l21": "L21 Hypotension",
            "l22": "L22 Atherosclerosis & Lipids", "l23": "L23 Valvular",
            "l24": "L24 Coronary Artery Disease", "l25": "L25 Heart Failure"}
PER_LEC = {"vig": 8, "reg": 2}           # per lecture per form
PER_FORM = 6 * sum(PER_LEC.values())     # 60
DX_RANGE = (10, 13)                      # diagnosis lead-ins per form of 60
SKEW_CAP = 0.40
SEED = 20260925

SLOT_GROUP = {
    "etiology": "cause/risk", "epidemiology": "cause/risk", "risk factors": "cause/risk",
    "manifestation": "presentation", "differential": "presentation",
    "initial test": "test", "gold standard": "test", "test finding": "test",
    "first-line": "treatment", "escalation": "treatment", "agent/regimen": "treatment",
    "avoid": "avoid", "education": "education", "referral": "referral",
    "complication": "complication", "prognosis": "complication",
}

# ---------------------------------------------------------------- Lecture 20
# Hand labels for the 64 Lecture 20 vignettes, (module suffix, index) -> lead.
# None = not a vignette (the stem does not open on a patient): left out.
L20_LEAD = {
 ("a", 0): "next step", ("a", 1): "test", ("a", 2): "diagnosis", ("a", 3): "test",
 ("a", 4): "diagnosis", ("a", 5): "diagnosis", ("a", 6): "referral", ("a", 7): "test",
 ("a", 8): "diagnosis", ("a", 9): "diagnosis", ("a", 10): "treatment", ("a", 11): "diagnosis",
 ("a", 12): "test", ("a", 13): None, ("a", 14): "next step", ("a", 15): "test",
 ("a", 16): "next step", ("a", 17): "diagnosis", ("a", 18): "diagnosis", ("a", 19): None,
 ("a", 20): "diagnosis", ("a", 21): "complication", ("a", 22): "education", ("a", 23): "test",
 ("a", 24): "next step", ("a", 25): "test", ("a", 26): None, ("a", 27): "diagnosis",
 ("a", 28): "treatment", ("a", 29): "treatment", ("a", 30): "next step", ("a", 31): "test",
 ("b", 0): "education", ("b", 1): "education", ("b", 2): "treatment", ("b", 3): "treatment",
 ("b", 4): "treatment", ("b", 5): "avoid", ("b", 6): "treatment", ("b", 7): "complication",
 ("b", 8): "complication", ("b", 9): "avoid", ("b", 10): "treatment", ("b", 11): "test",
 ("b", 12): "complication", ("b", 13): "next step", ("b", 14): "next step", ("b", 15): "treatment",
 ("b", 16): "treatment", ("b", 17): "complication", ("b", 18): "test", ("b", 19): "education",
 ("b", 20): None, ("b", 21): "education", ("b", 22): "treatment", ("b", 23): "complication",
 ("b", 24): "test", ("b", 25): None, ("b", 26): "education", ("b", 27): "treatment",
 ("b", 28): "complication", ("b", 29): "treatment", ("b", 30): "education", ("b", 31): "referral",
}

# Master-only text repairs for Lecture 20 (see the docstring).
L20_TEXT = [
    (re.compile(r"^ACE inhibitor cough$"), "Angiotensin-converting enzyme inhibitor cough"),
    (re.compile(r"\bACE inhibit"), "angiotensin-converting enzyme inhibit"),
    # bracketed so check_us_spelling.py --fix does not rewrite the pattern itself
    (re.compile(r"([Hh])yperkal[a]emia"), r"\1yperkalemia"),
]
# Words in capitals that are emphasis, not abbreviations.
_EMPH = re.compile(r"^(?:NOT|AND|NEW|NEVER|ABRUPT|SEVERE|CURRENT|INSTEAD|ARM|LEG|EXCEEDS|MARKED|"
                   r"SYSTOLIC|ORGAN|INJURY|DIHYDROPYRIDINE|ROUTINELY|ONLY|BOTH|ALL|NO|OR)$")


def _l20_fix(s):
    for rx, new in L20_TEXT:
        s = rx.sub(new, s)
    return s


def _l20_errors(q, vig):
    errs = []
    for label, t in P._texts(q):
        for rx, lab in ((P._DOSE, "dosing"), (P._BRAND, "brand"), (P._UK, "UK spelling")):
            m = rx.search(t)
            # "angioedema" contains "oedem"; it is the US word, not a British one.
            if m and not (lab == "UK spelling" and m.group(0).lower().startswith("angioedem")):
                errs.append("%s %r in %s" % (lab, m.group(0), label))
        for mm in P._ACRO.finditer(t):
            tok = mm.group(1)
            if P._ACRO_OK.match(tok) or _EMPH.match(tok):
                continue
            if not t[mm.end():].startswith(" ("):
                errs.append("bare acronym %r in %s" % (tok, label))
    if P._DEP.search(q["q"]):
        errs.append("refers to another question")
    if not q["q"].rstrip().endswith("?"):
        errs.append("stem does not end on a question")
    if vig and not P._VIG.match(q["q"].strip()):
        errs.append("vignette stem does not open on a patient")
    if len({o[0].strip().lower() for o in q["opts"]}) != 4:
        errs.append("duplicate option")
    if not re.match(r"correct\b", q["opts"][0][1].strip(), re.I):
        errs.append("keyed explanation does not open 'Correct'")
    return errs


def load_l20():
    out, dropped = [], []
    for kind, pat in (("reg", "cms_e4l20_pool_*.py"), ("vig", "cms_e4l20_vig_*.py")):
        for path in sorted(glob.glob(os.path.join(HERE, pat))):
            m = os.path.basename(path)[:-3]
            for i, q in enumerate(importlib.import_module(m).QUESTIONS):
                q = copy.deepcopy(q)
                q.setdefault("c", 0)
                assert q["c"] == 0, "%s[%d]: key not authored first" % (m, i)
                q["q"] = _l20_fix(q["q"])
                q["topic"] = _l20_fix(q["topic"])
                q["opts"] = [[_l20_fix(o[0]), _l20_fix(o[1])] for o in q["opts"]]
                if kind == "vig":
                    lead = L20_LEAD[(m[-1], i)]
                    if lead is None:
                        dropped.append((m, i, "vignette-pool stem does not open on a patient", q["q"]))
                        continue
                    q["lead"] = lead
                errs = _l20_errors(q, kind == "vig")
                if errs:
                    dropped.append((m, i, "; ".join(errs), q["q"]))
                    continue
                q["_src"] = (m, i)
                q["_kind"] = kind
                out.append(q)
    n_vig = sum(1 for k in L20_LEAD)
    assert n_vig == len(importlib.import_module("cms_e4l20_vig_a").QUESTIONS) + \
        len(importlib.import_module("cms_e4l20_vig_b").QUESTIONS), "L20_LEAD is stale"
    return out, dropped


def load_guarded_lecture(lec):
    out, required = [], []
    for kind, vig in (("reg", False), ("vig", True)):
        scope, mods, pool, origin, nfix = P.load_guarded(lec, vig)
        P.guard_all(scope, pool, origin, vig)           # asserts; a failure stops the build
        for q, o in zip(pool, origin):
            q["_src"] = o
            q["_kind"] = kind
            out.append(q)
        required = [(lab, re.compile(sr, re.I), re.compile(kr, re.I), n)
                    for lab, sr, kr, n in getattr(scope, "REQUIRED", ())]
        band = sorted(getattr(scope, "TOPIC_BAND", {}))
    return out, required, band


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
        for sj in ("cms_e4%s_sets.json" % lec, "cms_e4%s_vig_sets.json" % lec):
            S = json.load(open(os.path.join(HERE, sj), encoding="utf-8"))
            used |= {q["q"].strip() for k in S for q in S[k]}
    return used


def build(dry_run=False):
    rng = random.Random(SEED)
    POOL, REQ, dropped = [], [], []
    EVERY_FORM = {}
    l20, dropped = load_l20()
    for q in l20:
        q["_lec"] = "l20"
    POOL += l20
    for lec in LECS[1:]:
        qs, req, band = load_guarded_lecture(lec)
        # TOPIC_BAND's per-form minimum (2-4 per lesion in a set of 30) cannot
        # fit into ten questions; what carries over is its intent, every banded
        # topic in every form -- possible only when the band fits in the ten.
        if band and len(band) <= sum(PER_LEC.values()):
            EVERY_FORM[lec] = band
        elif band:
            print("   %s TOPIC_BAND has %d topics for %d slots: spread is scored, not required"
                  % (lec, len(band), sum(PER_LEC.values())))
        for q in qs:
            q["_lec"] = lec
        POOL += qs
        for lab, srx, krx, n in req:
            REQ.append((lec, lab, srx, krx, n))

    # the topic sets were built from the pools as they stand; a stem shipped in a
    # topic quiz must still be in its pool (a topic page edited after rendering
    # would mean the pool is no longer the source of truth)
    topic_used = used_in_topic_sets()
    for q in POOL:
        q["_fresh"] = q["q"].strip() not in topic_used

    stems = Counter(q["q"].strip().lower() for q in POOL)
    dup = [s for s, n in stems.items() if n > 1]
    assert not dup, "duplicate stem across pools: %r" % dup[:3]

    # REQUIRED hits (the key is authored at index 0 in every pool)
    req_hit = {}
    for lec, lab, srx, krx, n in REQ:
        hit = {i for i, q in enumerate(POOL) if q["_lec"] == lec
               and srx.search(q["q"]) and krx.search(q["opts"][0][0])}
        # Every form when the pool can supply it; otherwise as many forms as it
        # can (reported, never silently): L24's right-ventricular-infarct
        # nitroglycerin item has only four questions in the whole pool.
        target = min(len(FORMS), len(hit) // n)
        assert target >= 1, "%s %r: nothing in the pool" % (lec, lab)
        if target < len(FORMS):
            print("!! %s %r: the pool holds %d such questions, so it can reach %d of %d forms"
                  % (lec, lab, len(hit), target, len(FORMS)))
        req_hit[(lec, lab)] = (hit, n, target)

    G = [gameable(q) for q in POOL]
    groups = defaultdict(list)                  # (lec, kind) -> pool indices
    for i, q in enumerate(POOL):
        groups[(q["_lec"], q["_kind"])].append(i)

    print("candidates after guards: %d  (Lecture 20 left out: %d)" % (len(POOL), len(dropped)))
    for lec in LECS:
        for kind in ("reg", "vig"):
            idx = groups[(lec, kind)]
            print("   %-30s %-3s %3d candidates  %3d fresh  %2d gameable  cells=%s" % (
                LEC_NAME[lec], kind, len(idx), sum(POOL[i]["_fresh"] for i in idx),
                sum(G[i] for i in idx), dict(sorted(Counter(cell_lead(POOL[i]) for i in idx).items()))))
            assert len(idx) >= len(FORMS) * PER_LEC[kind]

    # ---------------------------------------------------------------- scoring
    def form_pen(sel):
        """sel: list of pool indices in one form."""
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
            pen += 8 * sum(max(0, c - 2) for c in tops.values())
            pen += 1.5 * (10 - len(tops))
            pen += 60 * sum(1 for t in EVERY_FORM.get(lec, ()) if t not in tops)
        keys = Counter(q["opts"][0][0].strip().lower() for q in qs)
        pen += 40 * sum(c - 1 for c in keys.values() if c > 1)
        pen += 1.0 * sum(1 for q in qs if not q["_fresh"])
        return pen

    def strat_pen(forms):
        cnt = defaultdict(lambda: [0] * len(FORMS))
        for f, sel in enumerate(forms):
            for i in sel:
                q = POOL[i]
                cnt[(q["_lec"], q["_kind"], cell_lead(q))][f] += 1
        pen = 200 * sum(max(0, max(v) - min(v) - 1) for v in cnt.values())
        for (lec, lab), (hit, n, target) in req_hit.items():
            covered = sum(1 for sel in forms if len(hit & set(sel)) >= n)
            pen += 500 * max(0, target - covered)
        return pen

    # ---------------------------------------------------------------- start: stratified deal
    # One continuous round-robin over (lecture, kind, lead) cells within each
    # (lecture, kind) group, dealing only as many as the group needs -- the
    # cmsent/cmsophtho deal, with the per-lecture quota enforced.
    forms = [[] for _ in FORMS]
    for (lec, kind), idx in sorted(groups.items()):
        need = PER_LEC[kind] * len(FORMS)
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
        for n, i in enumerate(order):
            forms[n % len(FORMS)].append(i)

    fp = [form_pen(s) for s in forms]

    def total(forms, changed=()):
        for f in changed:
            fp[f] = form_pen(forms[f])
        return sum(fp) + strat_pen(forms)

    cur = total(forms)
    print("\nstratified deal: score %.1f" % cur)
    chosen = {i for s in forms for i in s}
    # Simulated annealing over two moves that both preserve the per-lecture
    # quota: swap a chosen question for an unchosen one of the same (lecture,
    # kind), or swap two chosen ones of the same (lecture, kind) between forms.
    # (Plain hill-climbing stalled once the nine-lesion rule was added.) The
    # best state seen is what is kept; the asserts below decide if it is good.
    import math
    STEPS, T0, T1 = 250000, 60.0, 0.05
    best = (cur, [list(s) for s in forms])
    for step in range(STEPS):
        T = T0 * (T1 / T0) ** (step / STEPS)
        f = rng.randrange(len(FORMS))
        a = rng.randrange(len(forms[f]))
        ia = forms[f][a]
        key = (POOL[ia]["_lec"], POOL[ia]["_kind"])
        if rng.random() < 0.5:                   # swap with an unchosen question of the same group
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
        else:                                    # swap between two forms, same group
            g = rng.randrange(len(FORMS))
            if g == f:
                continue
            cand = [k for k, x in enumerate(forms[g]) if (POOL[x]["_lec"], POOL[x]["_kind"]) == key]
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
    chosen = {i for s in forms for i in s}
    fp[:] = [form_pen(s) for s in forms]
    print("local search settled at score %.1f" % cur)

    # ---------------------------------------------------------------- hard asserts
    allsel = [i for s in forms for i in s]
    assert len(allsel) == len(set(allsel)) == PER_FORM * len(FORMS), "a question landed in two forms"
    assert len({POOL[i]["q"].strip().lower() for i in allsel}) == len(allsel)
    assert strat_pen(forms) == 0, "a (lecture, kind, lead) cell is uneven, or REQUIRED coverage is short"
    req_cover = {}
    for (lec, lab), (hit, n, target) in req_hit.items():
        req_cover[(lec, lab)] = [name for name, sel in zip(FORMS, forms) if len(hit & set(sel)) >= n]
        assert len(req_cover[(lec, lab)]) >= target
        print("required %s %r: forms %s (target %d)" % (lec, lab, "".join(req_cover[(lec, lab)]), target))
    for name, sel in zip(FORMS, forms):
        assert len(sel) == PER_FORM
        for lec in LECS:
            for kind in ("reg", "vig"):
                n = sum(1 for i in sel if (POOL[i]["_lec"], POOL[i]["_kind"]) == (lec, kind))
                assert n == PER_LEC[kind], "Form %s %s %s has %d" % (name, lec, kind, n)
        leads = Counter(POOL[i]["lead"] for i in sel if POOL[i]["_kind"] == "vig")
        assert DX_RANGE[0] <= leads.get("diagnosis", 0) <= DX_RANGE[1], "Form %s diagnosis %d" % (
            name, leads.get("diagnosis", 0))
        assert max(leads.values()) <= sum(leads.values()) * SKEW_CAP, "Form %s lead skew" % name
        assert sum(G[i] for i in sel) == 0, "Form %s has a length-gameable question" % name
        for lec, band in EVERY_FORM.items():
            tops = {POOL[i]["topic"] for i in sel if POOL[i]["_lec"] == lec}
            assert all(t in tops for t in band), "Form %s %s misses %s" % (
                name, lec, [t for t in band if t not in tops])

    # ---------------------------------------------------------------- permute per form
    out = {}
    report = {"forms": {}, "dropped": dropped,
              "required": {"%s %s" % k: v for k, v in req_cover.items()}}
    for name, sel in zip(FORMS, forms):
        qs = [copy.deepcopy(POOL[i]) for i in sel]
        rng.shuffle(qs)
        targets = [k % 4 for k in range(len(qs))]
        rng.shuffle(targets)
        for q, t in zip(qs, targets):
            correct = q["opts"][q["c"]]
            rest = [o for j, o in enumerate(q["opts"]) if j != q["c"]]
            rng.shuffle(rest)
            q["opts"] = rest[:t] + [correct] + rest[t:]
            q["c"] = t
            assert q["opts"][q["c"]] is correct
            assert re.match(r"correct\b", q["opts"][q["c"]][1], re.I)
            assert sum(1 for o in q["opts"] if re.match(r"correct\b", o[1].strip(), re.I)) == 1
        pos = Counter(q["c"] for q in qs)
        assert all(pos[k] == 15 for k in range(4)), pos
        report["forms"][name] = [{
            "lec": q["_lec"], "kind": q["_kind"], "lead": cell_lead(q), "topic": q["topic"],
            "fresh": q["_fresh"], "src": "%s[%d]" % tuple(q["_src"]), "c": q["c"],
            "req": [lab for (lec, lab), (hit, n, target) in req_hit.items()
                    if lec == q["_lec"] and any(POOL[i]["q"] == q["q"] for i in hit)],
            "q": q["q"]} for q in qs]
        out[name] = [{k: q[k] for k in ("topic", "io", "q", "opts", "c", "cite")} for q in qs]

    for name in FORMS:
        r = report["forms"][name]
        print("  Form %s: %dq  vig %d  fresh %d  pos %s  leads(vig) %s" % (
            name, len(r), sum(x["kind"] == "vig" for x in r), sum(x["fresh"] for x in r),
            "/".join(str(sum(1 for x in r if x["c"] == k)) for k in range(4)),
            dict(Counter(x["lead"] for x in r if x["kind"] == "vig").most_common())))

    if dry_run:
        print("--dry-run: nothing written")
        return out, report
    path = os.path.join(ROOT, FOLDER, "master-exams.json")
    open(path, "w", encoding="utf-8").write(json.dumps(out, indent=1, ensure_ascii=False))
    json.dump(report, open(os.path.join(HERE, "cms_e4_masters_report.json"), "w", encoding="utf-8"),
              indent=1, ensure_ascii=False)
    print("wrote", os.path.relpath(path, ROOT), "and tools/cms_e4_masters_report.json")
    return out, report


if __name__ == "__main__":
    build(dry_run="--dry-run" in sys.argv)
