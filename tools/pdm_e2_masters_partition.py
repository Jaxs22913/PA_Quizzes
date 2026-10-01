#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Assemble the five PDM I Exam 2 Master Exams, 5 x 60.

    python3 tools/pdm_e2_masters_partition.py            # build, report, write the JSON
    python3 tools/pdm_e2_masters_partition.py --dry-run  # build and report, write nothing

Then tools/render_pdm_e2_masters.py renders the five pages from the JSON.

BLOCK. Exam 2 covers Lectures 7-10 AND Lab 2 (calendar-data.js). All four lecture decks are in and
built (7 Electrocardiography, 8 Cardiac Imaging and Vascular Studies, 9 Cardiac Biomarkers and Lipid
Testing, 10 Coagulation and Hemostasis Testing), so the hold rule is met. NO Lab 2 MATERIAL EXISTS
(the PDM inbox has no lab folder or file; Jaxon answered "no content for the labs" for Exam 1 on
2026-09-01 and that was Exam 1 only), so, exactly as the Exam 1 masters, these forms cover the four
LECTURES and the page says so.

ALLOCATION: WEIGHTED BY SCHEDULED LECTURE HOURS, five questions per hour (timetable_weighted_exams).
Verified from the printed calendar PDFs (September.pdf for L7 and L8, the 2026-09-25 Outlook export for
L9, October.pdf / the export for L10): L7 Tue 9/15 10-12, L8 Thu 9/17 1-3, L9 Mon 9/21 1-3, L10 Wed 9/30
10-12 = four two-hour lectures = 8 hours. At five per hour that predicts 40 questions, but the form
size is 60 (master_exam_sizing; the exam period is 10:00-12:00 on 10/09 and the real length is not
published), so the real 60 is APPORTIONED across the verified hours: 60 x 2/8 = 15 each. alloc_by_hours()
re-derives it and the build asserts it. THE GAP (40 predicted vs 60 built) IS FLAGGED, not papered over.

WHERE THE QUESTIONS COME FROM (as the Exam 1 masters, build_master_exams.py): verbatim from the
lectures' own pools, never re-authored for the masters. 15 per lecture per form x 5 forms = 75
DISTINCT questions per lecture, but the topic quizzes only hold 60 per lecture, so every shipped
topic question is used once and 15 UNSHIPPED pool questions per lecture fill the rest:
  L7  : 2 held back + 13 of the 16 master-only questions written for this build (pdm_l7_pool_m.py)
  L8  : 4 held back + 11 of the 14 master-only questions (pdm_l8_pool_m.py)
  L9  : 15 of the 26 held-back pool questions
  L10 : 15 of the 32 held-back pool questions
(The 15 unshipped per lecture are chosen by the selector, preferring keys that are not gameable by
length and topics the topic quizzes under-use.) Shipped questions keep their shipped text, so their
guide links and audit records carry over unchanged.

STRATIFICATION (the CMS Exam 2 lesson, cms_ophtho_masters): each (lecture, lead-in) cell is dealt across
the five forms by ONE continuous round-robin, so no lecture and no lead-in type drops out of a form and
each cell is within one of even. Then a seeded local search swaps within a lecture to even the
length-gameable questions across forms and to keep two questions with the same key out of one form.

POSITIONS: permuted PER FORM onto an exact 15/15/15/15 A-D cycle, stratified by lecture (4/4/4/3 with a
different short letter in each lecture) and by lead-in inside the lecture. The key is moved and the
distractors keep their order. Never render straight from a pool.

MASTER-ONLY TEXT FIXES (FIXES below) correct an UNSHIPPED pool question without touching the pool file,
because a pool edit can change a seeded topic partition. They are keyed by the pool stem.
"""
import sys, os, json, random, re, importlib, copy
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

FOLDER = "Principles of Diagnostic Medicine I Exam 2"
FORMS = ["A", "B", "C", "D", "E"]
LECS = ["l7", "l8", "l9", "l10"]
LEC_NAME = {"l7": "L7 Electrocardiography", "l8": "L8 Cardiac Imaging & Vascular Studies",
            "l9": "L9 Cardiac Biomarkers & Lipid Testing", "l10": "L10 Coagulation & Hemostasis Testing"}
HOURS = {"l7": 2, "l8": 2, "l9": 2, "l10": 2}      # calendar-data.js, checked against the calendar PDFs
POOLS = {"l7": "ABM", "l8": "ABM", "l9": "AB", "l10": "ABC"}
PER_FORM, SEED = 60, 20260930
MARGIN_CHARS, MARGIN_FRAC = 8, 0.18
SPEED = {"l7": "ecg"}

# Master-only repairs of UNSHIPPED questions, keyed by the pool stem. {stem: {"q": ..., "opts": [[t, e], ...]}}
# opts, when given, must be key-first (the key is opts[0]) exactly like a pool entry; "patch" edits single
# options in place: {index: (text-or-None, explanation-or-None)}. Fact-check verdicts of 2026-09-30.
FIXES = {
  # L9 held-back: independent fact-check (Q6, Q11, Q15 FIX; Q18 optional tightening)
  "An emergency department switches a 68-year-old's workup to high-sensitivity troponin. What is the main advantage?": {
    "patch": {1: ("Any measurable level confirms infarction",
                  "Sensitivity is so high that healthy people can have measurable levels, so a detectable value alone cannot confirm infarction; the whole clinical picture must be considered.")}},
  "A 78-year-old woman and a 40-year-old man have natriuretic peptide levels compared. Which factors push her concentration higher?": {
    "patch": {3: ("Statin use and a low-sodium diet",
                  "Neither is a recognized factor that raises natriuretic peptides; the factors listed are older age, female sex and renal impairment, while obesity lowers the level.")}},
  "A 55-year-old's high-sensitivity C-reactive protein falls after she starts a new medication. Which could explain the fall?": {
    "patch": {1: (None, "Oral estrogen-containing contraceptives tend to raise, not lower, C-reactive protein; a statin is the agent here that lowers it."),
              2: ("An oral antihistamine",
                  "Antihistamines are not among the agents that lower C-reactive protein; the list is anti-inflammatories, statins, biologics, GLP-1 (glucagon-like peptide-1) agonists and lifestyle.")}},
  "A 50-year-old has an elevated lipoprotein(a) and an LDL-C (low-density lipoprotein cholesterol) at goal on a statin. What does the elevated lipoprotein(a) prompt?": {
    "patch": {3: (None, "It is highly atherogenic, per particle more so than LDL (low-density lipoprotein), and its elevation is a risk enhancer.")}},
  # L10 held-back: independent fact-check (Q11, Q17, Q19, Q22, Q26, Q29, Q31 FIX; Q15 dropped, see DROP)
  "A 67-year-old man develops thrombocytopenia from consumption of platelets. Which condition is a consumptive coagulopathy?": {
    "q": "A 67-year-old man has acquired thrombocytopenia. Which listed condition is classified as a consumptive coagulopathy?",
    "patch": {3: (None, "Thrombotic thrombocytopenic purpura is classed with the microangiopathic causes of increased platelet destruction, a separate category from consumptive coagulopathy.")}},
  "A 58-year-old man has a normal prothrombin time, a prolonged partial thromboplastin time and a prolonged thrombin time. Which drug fits?": {
    "patch": {1: (None, "Warfarin, a vitamin K antagonist, chiefly prolongs the prothrombin time and does not prolong the thrombin time."),
              3: ("Rivaroxaban", "Rivaroxaban, an oral factor Xa inhibitor, can lengthen the prothrombin time but does not lengthen the thrombin time; a prolonged thrombin time points to heparin or dabigatran.")}},
  "A 53-year-old man has a fibrinogen above the reference range of 2.0 to 4.0 grams per liter. What does an elevated result indicate?": {
    "patch": {1: (None, "A clotting factor deficiency does not raise fibrinogen; a deficiency of fibrinogen itself lowers it. A raised level reflects tissue damage or inflammation.")}},
  "A 47-year-old woman has a prolonged partial thromboplastin time that does not correct, and the abnormality depends on phospholipid. Which inhibitor fits?": {
    "q": "A 47-year-old woman has a prolonged partial thromboplastin time that does not correct on mixing, and the abnormality depends on phospholipid. Which diagnosis fits?"},
  "A 29-year-old woman has normal clotting screens and bleeding with skin bruising, petechiae and mucous membrane bleeding. Which category fits?": {
    "patch": {3: (None, "Significant hypofibrinogenemia prolongs the prothrombin time and partial thromboplastin time and is a factor problem, so the screens would not be normal with bruising and mucosal bleeding.")}},
  "A 62-year-old man has suspected thrombosis. Which set of studies forms the initial laboratory evaluation?": {
    "q": "A 62-year-old man has suspected thrombosis. Which set of three studies makes up the laboratory workup of a thrombotic (clotting) disorder?",
    "patch": {1: ("Factor VIII assay, von Willebrand antigen and platelet function analysis",
                  "These are bleeding-disorder studies of factors and platelets, not the thrombotic workup, which uses the prothrombin time, the partial thromboplastin time and D-dimer.")}},
  "A 29-year-old woman with recurrent thrombosis is evaluated for a hypercoagulable state. Which deficiency is a primary cause tested?": {
    "patch": {0: (None, "Correct. Primary hypercoagulable causes include deficiencies of antithrombin III, protein C and protein S, along with abnormal fibrinolytic mechanisms.")}},
}
# Unshipped pool stems that must NOT be used (fact-check REMOVE verdicts).
DROP = {
    # L10 Q15: the deck's 'special phospholipid activator' is loose (the reagent is a contact activator plus phospholipid);
    # an accurate key is too long against its distractors, so the question is not used rather than padded or shortened wrongly
    "A 52-year-old woman has an activated partial thromboplastin time ordered. What is added to her plasma to start the clot?",
}


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


def lead_in(q):
    """Coarse lead-in type of the question's own asking sentence (stratification only)."""
    s = q["q"].strip()
    last = re.split(r"(?<=[.!?])\s+", s)[-1].lower()
    if re.search(r"\b(next step|next test|next study|most appropriate|should be ordered|which (initial |next |best |first )?(test|study|studies|biomarker|modality|imaging|investigation|exam)\b)", last):
        return "test"
    if re.search(r"\b(limitation|disadvantage|contraindicat|complication|pitfall|cannot|risk|avoid)\b", last):
        return "limit"
    if re.search(r"\b(indication|indicated|used for|purpose|when is|when should|use of|useful)\b", last):
        return "use"
    if re.match(r"(why|how|what happens|what causes|on what|by what|what mechanism|over which|during which)", last):
        return "mechanism"
    if re.search(r"\b(suggest|indicate|represent|diagnos|rhythm|term applies|category fits|cause fits|does this mean|pattern|abnormal|interpret|what does|rate)\b", last):
        return "interpret"
    if re.match(r"(what is|what are|which term|define|which structure|which statement|which of these|which set|which relationship|which property|which)", last):
        return "identify"
    return "other"


def load():
    """Return {lecture: [question dict, key-first, with _ship flag]}."""
    out = {}
    for l in LECS:
        num = l[1:]
        sets = json.load(open(os.path.join(HERE, "pdm_%s_sets.json" % l), encoding="utf-8"))
        shipped = {}
        for k in sets:
            for q in sets[k]:
                shipped[q["q"]] = q
        pool = []
        for n in POOLS[l]:
            m = importlib.import_module("pdm_%s_pool_%s" % (l, n.lower()))
            pool += getattr(m, "POOL_%s" % n)
        seen, qs = set(), []
        for q in pool:
            assert q["q"] not in seen, "duplicate pool stem " + q["q"][:60]
            seen.add(q["q"])
            if q["q"] in shipped:
                s = copy.deepcopy(shipped[q["q"]])
                key = s["opts"][s["c"]]
                rest = [o for i, o in enumerate(s["opts"]) if i != s["c"]]
                s["opts"] = [key] + rest
                s["c"] = 0
                s["_ship"] = True
            else:
                if q["q"] in DROP:
                    continue
                s = copy.deepcopy(q)
                s["_ship"] = False
                if q["q"] in FIXES:
                    f = FIXES[q["q"]]
                    s["_orig"] = q["q"]
                    s["q"] = f.get("q", s["q"])
                    if "opts" in f:
                        s["opts"] = copy.deepcopy(f["opts"])
                    for i, (t, e) in f.get("patch", {}).items():
                        # patch: {option index (key = 0): (text or None to keep, explanation or None to keep)}
                        s["opts"][i] = [t if t is not None else s["opts"][i][0], e if e is not None else s["opts"][i][1]]
            s.pop("slot", None)
            s["_lec"] = l
            s["_lead"] = lead_in(s)
            qs.append(s)
        assert all(q["c"] == 0 for q in qs)
        assert sum(q["_ship"] for q in qs) == 60, "%s: %d shipped found" % (l, sum(q["_ship"] for q in qs))
        out[l] = qs
    return out


def pick_unshipped(qs, need):
    """All shipped + `need` unshipped. Prefer non-gameable keys, then topics the shipped set under-uses."""
    ship = [q for q in qs if q["_ship"]]
    extra = [q for q in qs if not q["_ship"]]
    tcount = Counter(q["topic"] for q in ship)
    chosen = []
    rest = extra[:]
    ioc = Counter(q["io"] for q in ship)
    while len(chosen) < need:
        def score(q):
            g = 1 if gameable(q["opts"], 0) else 0
            return (g * 100 + tcount[q["topic"]] * 2 + ioc[q["io"]] * 0.05, qs.index(q))
        rest.sort(key=score)
        q = rest.pop(0)
        chosen.append(q)
        tcount[q["topic"]] += 1
        ioc[q["io"]] += 1
    # Each shipped question that is gameable by length is swapped for one more unshipped, non-gameable question
    # while any remain (Jaxon's target is under 10% gameable per form; a shipped key cannot be shortened here
    # without breaking its guide link, which is keyed to the exact text, so it is left out of the masters instead).
    def margin(q):
        L = [len(o[0]) for o in q["opts"]]
        return L[0] - max(L[1:])
    bad = sorted([q for q in ship if gameable(q["opts"], 0)], key=lambda q: -margin(q))
    good_rest = [q for q in rest if not gameable(q["opts"], 0)]
    swap = min(len(bad), len(good_rest))
    for q in bad[:swap]:
        ship.remove(q)
    for q in good_rest[:swap]:
        rest.remove(q)
        chosen.append(q)
    return ship + chosen, [q for q in rest]


def deal(lec_qs, rng, n_forms=5):
    """One continuous round-robin over (lead-in) cells: each cell lands within one of even."""
    cells = defaultdict(list)
    for q in lec_qs:
        cells[q["_lead"]].append(q)
    for c in cells.values():
        rng.shuffle(c)
    forms = [[] for _ in range(n_forms)]
    k = 0
    for name in sorted(cells, key=lambda n: (-len(cells[n]), n)):
        for q in cells[name]:
            forms[k % n_forms].append(q)
            k += 1
    return forms


def form_cost(f):
    g = sum(gameable(q["opts"], 0) for q in f)
    keys = Counter(q["opts"][0][0].strip().lower() for q in f)
    dup = sum(v - 1 for v in keys.values() if v > 1)
    topics = Counter((q["_lec"], q["topic"]) for q in f)
    rep = sum(max(0, v - 2) for v in topics.values())
    return g * 3 + dup * 4 + rep


def improve(allforms, rng, iters=40000):
    """Swap two questions of the SAME lecture AND lead-in cell between forms (keeps every cell even)."""
    def total():
        return sum(form_cost(f) for f in allforms)
    cur = total()
    cellmap = defaultdict(list)
    for fi, f in enumerate(allforms):
        for qi, q in enumerate(f):
            cellmap[(q["_lec"], q["_lead"])].append((fi, qi))
    keys = [k for k, v in cellmap.items() if len({fi for fi, _ in v}) > 1]
    for _ in range(iters):
        k = rng.choice(keys)
        (a_f, a_i), (b_f, b_i) = rng.sample(cellmap[k], 2)
        if a_f == b_f:
            continue
        before = form_cost(allforms[a_f]) + form_cost(allforms[b_f])
        allforms[a_f][a_i], allforms[b_f][b_i] = allforms[b_f][b_i], allforms[a_f][a_i]
        after = form_cost(allforms[a_f]) + form_cost(allforms[b_f])
        if after <= before:
            cur += after - before
        else:
            allforms[a_f][a_i], allforms[b_f][b_i] = allforms[b_f][b_i], allforms[a_f][a_i]
    return cur


def place_positions(form, fi, rng):
    """Exact 15/15/15/15 per form; per lecture 4/4/4/3 with a different short letter in each lecture;
    inside a lecture the cycle runs down the lead-in-sorted order so lead-in cells stay balanced."""
    out = []
    for li, l in enumerate(LECS):
        mine = sorted([q for q in form if q["_lec"] == l], key=lambda q: (q["_lead"], q["topic"], q["q"]))
        off = (li + fi) % 4
        # the short letter is (3 + off) % 4: distinct for the four lectures inside a form
        for k, q in enumerate(mine):
            want = (k + off) % 4
            o = list(q["opts"]); key = o.pop(0); o.insert(want, key)
            r = {kk: vv for kk, vv in q.items() if not kk.startswith("_")}
            r["opts"] = o; r["c"] = want
            r["_lec"] = l; r["_lead"] = q["_lead"]; r["_ship"] = q["_ship"]
            out.append(r)
    rng.shuffle(out)
    return out


def main():
    dry = "--dry-run" in sys.argv
    rng = random.Random(SEED)
    alloc = alloc_by_hours()
    assert alloc == {l: 15 for l in LECS}, alloc
    data = load()
    chosen, leftover, per_lec_forms = {}, {}, {}
    for l in LECS:
        need = alloc[l] * len(FORMS) - 60
        chosen[l], leftover[l] = pick_unshipped(data[l], need)
        assert len(chosen[l]) == alloc[l] * len(FORMS), (l, len(chosen[l]))
        print("%s: %d shipped + %d unshipped (%d gameable shipped swapped out)" % (
            l, sum(q["_ship"] for q in chosen[l]), sum(not q["_ship"] for q in chosen[l]), 60 - sum(q["_ship"] for q in chosen[l])))
        per_lec_forms[l] = deal(chosen[l], rng)
    allforms = [[q for l in LECS for q in per_lec_forms[l][fi]] for fi in range(len(FORMS))]
    for f in allforms:
        assert len(f) == PER_FORM
    improve(allforms, rng)

    result = {}
    stems = []
    for fi, name in enumerate(FORMS):
        f = place_positions(allforms[fi], fi, rng)
        result[name] = f
        stems += [q["q"] for q in f]
    assert len(stems) == len(set(stems)) == 300, "a question appears in more than one form"

    print("ALLOCATION (hours x 5 = %d predicted; real form size %d, apportioned): %s"
          % (sum(HOURS.values()) * 5, PER_FORM, {LEC_NAME[l]: alloc[l] for l in LECS}))
    report = {"alloc": alloc, "hours": HOURS, "forms": {}}
    for name in FORMS:
        f = result[name]
        pos = Counter(q["c"] for q in f)
        assert [pos[i] for i in range(4)] == [15, 15, 15, 15], (name, pos)
        gm = sum(gameable(q["opts"], q["c"]) for q in f)
        lec = Counter(q["_lec"] for q in f)
        assert all(lec[l] == 15 for l in LECS)
        lead = Counter(q["_lead"] for q in f)
        newq = sum(not q["_ship"] for q in f)
        print("Form %s: 60 q | A/B/C/D %d/%d/%d/%d | gameable %d (%.1f%%) | per lecture %s | unshipped %d | lead-ins %s"
              % (name, pos[0], pos[1], pos[2], pos[3], gm, gm / 60 * 100,
                 dict(lec), newq, dict(sorted(lead.items()))))
        # per-lecture position spread
        spread = {l: dict(sorted(Counter(q["c"] for q in f if q["_lec"] == l).items())) for l in LECS}
        report["forms"][name] = dict(gameable=gm, positions=dict(pos), lecture_positions=spread,
                                     leadins=dict(lead), unshipped=newq)
    cell = defaultdict(lambda: [0] * 5)
    for fi, name in enumerate(FORMS):
        for q in result[name]:
            cell[(q["_lec"], q["_lead"])][fi] += 1
    worst = max(max(v) - min(v) for v in cell.values())
    print("(lecture, lead-in) cells: %d, widest spread across forms = %d" % (len(cell), worst))
    assert worst <= 1
    used_new = {l: sum(not q["_ship"] for q in chosen[l]) for l in LECS}
    print("unshipped questions used per lecture:", used_new)
    out = {n: [{k: v for k, v in q.items() if not k.startswith("_")} for q in result[n]] for n in FORMS}
    if dry:
        return
    path = os.path.join(ROOT, FOLDER, "master-exams.json")
    json.dump(out, open(path, "w", encoding="utf-8"), ensure_ascii=False)
    rep = os.path.join(HERE, "pdm_e2_masters_report.json")
    report["unshipped_used"] = used_new
    report["unshipped_stems"] = sorted(q.get("_orig", q["q"]) for l in LECS for q in chosen[l] if not q["_ship"])
    json.dump(report, open(rep, "w", encoding="utf-8"), indent=1)
    print("wrote", os.path.relpath(path, ROOT), "and", os.path.basename(rep))


if __name__ == "__main__":
    main()
