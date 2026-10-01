#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the five cumulative Master Exams (Forms A-E, 60 questions each) for Pharmacology I Exam 2.

Written 2026-09-30, after Lecture 8 completed the block (Lectures 4-8), per [[master_exam_sizing]]: five
SEPARATE 60-question forms, all five lectures in every form, no question in two forms.

WHERE THE QUESTIONS COME FROM. The questions already shipped in the Exam 2 topic quizzes and the two
clinical-vignette pairs (ophthalmic and myocardial ischemia), read from the same sets files the quiz pages
are rendered from (pharm_oph / pharm_ent / pharm_htn / pharm_lipid / pharm_mi _sets.json,
pharm_e2_vignette_sets.json, pharm_mi_vignette_sets.json): 150 / 145 / 129 / 88 / 164 questions for
Lectures 4 to 8. Reused VERBATIM, as the Exam 1 and CMS masters are, so a master cannot drift from the quiz
it summarizes. The rapid drills are NOT used: they are a different format (one drug per choice).

WEIGHTED BY THE TIMETABLE ([[timetable_weighted_exams]], five questions per scheduled lecture hour), with
the hours read from calendar-data.js and checked against the printed Outlook export:

    Lecture 4 Ophthalmic Drugs                  2 h  (Fri 2026-09-04, 10:00-12:00)
    Lecture 5 ENT Drugs                         2 h  (Wed 2026-09-09, 15:00-17:00)
    Lecture 6 Antihypertensive Drugs            2 h  (Tue 2026-09-22,  8:00-10:00)
    Lecture 7 Cholesterol and Triglycerides     2 h  (Tue 2026-09-22, 10:00-12:00)
    Lecture 8 Myocardial Ischemia Drug Therapy  1 h  (Wed 2026-09-30, 15:00-16:00)

NINE hours x 5 = 45, but a master exam is 60 questions, so the arithmetic does not close (the same kind of
gap as Micro Exam 1's 70-versus-65). The real 60 is APPORTIONED across the verified hours by largest
remainder (13.33 / 13.33 / 13.33 / 13.33 / 6.67 -> 13 / 13 / 13 / 13 / 6, leaving two spare questions that
go to the two largest remainders: Lecture 8 (.67) and then, the four others tying at .33, the lecture with
the largest shipped pool, Lecture 4). Result: 14 / 13 / 13 / 13 / 7. The extra questions are an
apportionment, not a published fact, and the report says so.

STRATIFIED. Inside each lecture the questions are grouped into five lead-in cells (mechanism and physiology,
indication and drug choice, safety, education and monitoring, clinical judgment) and sampled in proportion;
the selected questions are then dealt to the five forms along one continuous pointer, so every form gets the
same cell mix and the leftovers rotate (the CMS ophthalmology lesson in [[cms_ophtho_masters]]: a per-lecture
quota draw can starve the smallest lecture in a form).

EXCLUDED FROM THE DRAW (they stay in the topic quizzes):
  * dosage questions (Dr. Wood does not test doses): any question whose KEY states a dose, a dosing
    frequency or a regimen;
  * any question the length-bias definition marks as gameable (key the longest by 8+ characters and 18%+),
    so every form is 0 percent gameable by construction;
Mechanism and physiology are capped at 20 percent of each lecture's draw (the pools run 12 to 32 percent), and never outnumber indications, drug choice, safety and education combined
(Dr. McInnis, [[pharmacology_exam_spec]]) in any form.

ANSWER POSITIONS are assigned PER FORM, after the draw: the form's questions are ordered by (lecture, cell)
and given a continuing A, B, C, D cycle (starting offset seeded per form), so each form holds exactly
15 / 15 / 15 / 15 and each lecture's block is within one of even; the key moves with its explanation.

    python3 tools/build_pharm_e2_masters.py          # writes Pharmacology I Exam 2/master-exams.json
                                                     # and tools/pharm_e2_masters_report.json
"""
import json, os, random, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "Pharmacology I Exam 2", "master-exams.json")
REPORT = os.path.join(HERE, "pharm_e2_masters_report.json")

SEED = 20261005
FORMS = "ABCDE"
PER_FORM = 60
NOPT = 4

SOURCES = {
    "L4": ["pharm_oph_sets.json", "pharm_e2_vignette_sets.json"],
    "L5": ["pharm_ent_sets.json"],
    "L6": ["pharm_htn_sets.json"],
    "L7": ["pharm_lipid_sets.json"],
    "L8": ["pharm_mi_sets.json", "pharm_mi_vignette_sets.json"],
}
NAMES = {"L4": "Ophthalmic drugs", "L5": "ENT drugs", "L6": "Antihypertensives",
         "L7": "Lipid-lowering drugs", "L8": "Myocardial ischemia"}
HOURS = {"L4": 2, "L5": 2, "L6": 2, "L7": 2, "L8": 1}     # calendar-data.js, verified against the Outlook export

CELL_OF = {}
for s in ("mechanism", "physiology"):
    CELL_OF[s] = "mechanism"
for s in ("indication", "drug choice", "first-line", "agent/regimen", "class"):
    CELL_OF[s] = "indication"
for s in ("adverse effect", "contraindication", "avoid", "interaction", "complication"):
    CELL_OF[s] = "safety"
for s in ("education", "monitoring", "protocol"):
    CELL_OF[s] = "education"
for s in ("diagnosis", "next step", "initial test", "test finding", "risk factor", "risk factors",
          "referral", "escalation"):
    CELL_OF[s] = "clinical"
BACKGROUND = {"mechanism"}
MECH_CAP = 0.20      # share of one lecture's draw that may be mechanism (the pools run 12 to 32 percent)

DOSE_KEY = re.compile(r"(?i)\bdos(e|es|ing|age)\b|\bonce daily\b|\btwice\b|\b\d+(\.\d+)?\s*(mg|mcg|microgram|units?)\b|\bregimen")


def gameable(opts, c):
    L = [len(re.sub(r"<[^>]+>", "", o[0])) for o in opts]
    runner = max(L[:c] + L[c + 1:])
    return L[c] > runner and (L[c] - runner) >= 8 and L[c] >= runner * 1.18


def load():
    pools, dropped = {}, defaultdict(list)
    for lec, files in SOURCES.items():
        qs, seen = [], set()
        for f in files:
            d = json.load(open(os.path.join(HERE, f), encoding="utf-8"))
            for key in sorted(d):
                for q in d[key]:
                    assert len(q["opts"]) == NOPT and q["opts"][q["c"]][1].startswith("Correct"), q["q"]
                    assert q["q"] not in seen, "duplicate stem inside %s: %s" % (lec, q["q"])
                    seen.add(q["q"])
                    qs.append(q)
        keep = []
        for q in qs:
            keytext = q["opts"][q["c"]][0]
            if DOSE_KEY.search(keytext):
                dropped["dose"].append((lec, q["q"]))
            elif gameable(q["opts"], q["c"]):
                dropped["gameable"].append((lec, q["q"]))
            else:
                assert q["slot"] in CELL_OF, "unmapped slot %r" % q["slot"]
                keep.append(q)
        pools[lec] = (qs, keep)
    return pools, dropped


def apportion(hours, pool_size, total):
    """Largest remainder over the scheduled hours; ties go to the larger pool."""
    H = sum(hours.values())
    exact = {k: total * v / H for k, v in hours.items()}
    quota = {k: int(e) for k, e in exact.items()}
    left = total - sum(quota.values())
    for k in sorted(exact, key=lambda k: (-(exact[k] - quota[k]), -pool_size[k]))[:left]:
        quota[k] += 1
    return quota, exact


def systematic(cells, n, rng):
    """n questions from the cells in proportion to cell size (largest remainder, capped by cell size)."""
    size = {c: len(v) for c, v in cells.items()}
    total = sum(size.values())
    exact = {c: n * size[c] / total for c in cells}
    # Dr. McInnis: mechanism is over-weighted, so it is held to MECH_CAP of a lecture's draw; the rest of the
    # draw is shared out over the other cells in proportion to their size.
    cap = MECH_CAP * n
    if "mechanism" in exact and exact["mechanism"] > cap:
        spare = exact["mechanism"] - cap
        exact["mechanism"] = cap
        others = {c: size[c] for c in cells if c != "mechanism"}
        room = {c: size[c] - exact[c] for c in others}
        for c in sorted(others, key=lambda c: -room[c]):
            add = min(room[c], spare * size[c] / sum(others.values()))
            exact[c] += add
        # whatever the proportional share could not place (small cells) goes to the roomiest cell
        short = n - sum(exact.values())
        for c in sorted(others, key=lambda c: -(size[c] - exact[c])):
            add = min(size[c] - exact[c], short)
            exact[c] += add; short -= add
    take = {c: min(size[c], int(exact[c])) for c in cells}
    order = sorted(cells, key=lambda c: (-(exact[c] - int(exact[c])), c))
    while sum(take.values()) < n:
        moved = False
        for c in order:
            if sum(take.values()) >= n:
                break
            if take[c] < size[c]:
                take[c] += 1
                moved = True
        assert moved, "cannot reach %d" % n
    picked = []
    for c in sorted(cells):
        shuffled = cells[c][:]
        rng.shuffle(shuffled)
        picked.append((c, shuffled[:take[c]]))
    return picked, take


def main():
    pools, dropped = load()
    size = {l: len(p[1]) for l, p in pools.items()}
    quota, exact = apportion(HOURS, {l: len(p[0]) for l, p in pools.items()}, PER_FORM)
    assert sum(quota.values()) == PER_FORM
    print("hours %s -> x5 = %d (not %d: apportioned)" % (HOURS, 5 * sum(HOURS.values()), PER_FORM))
    print("exact shares %s" % {k: round(v, 2) for k, v in exact.items()})
    print("per-form quota %s" % quota)
    for l in pools:
        need = quota[l] * len(FORMS)
        print("  %s  shipped %3d  eligible %3d  need %3d (dropped: dose/gameable)" % (l, len(pools[l][0]), size[l], need))
        assert size[l] >= need, "%s: %d eligible, %d needed" % (l, size[l], need)

    rng = random.Random(SEED)
    forms = {f: [] for f in FORMS}
    pointer = 0
    for lec in sorted(pools):
        cells = defaultdict(list)
        for q in pools[lec][1]:
            cells[CELL_OF[q["slot"]]].append(q)
        picked, take = systematic(cells, quota[lec] * len(FORMS), rng)
        print("  %s cells %s" % (lec, dict(sorted(take.items()))))
        for cell, qs in picked:                     # one continuous pointer: leftovers rotate between forms
            for q in qs:
                forms[FORMS[pointer % len(FORMS)]].append((lec, cell, q))
                pointer += 1

    # ---- answer positions, per form, stratified by (lecture, cell) ----------------------------------
    out, report = {}, {"hours": HOURS, "exact_share": exact, "quota": quota, "forms": {}}
    for fi, f in enumerate(FORMS):
        items = sorted(forms[f], key=lambda t: (t[0], t[1], t[2]["q"]))
        start = random.Random(SEED + fi).randrange(NOPT)
        built = []
        for i, (lec, cell, q) in enumerate(items):
            want = (start + i) % NOPT
            o = list(q["opts"]); key = o.pop(q["c"]); o.insert(want, key)
            r = {k: q[k] for k in ("topic", "io", "q", "cite")}
            r["opts"] = o; r["c"] = want
            built.append((lec, cell, r))
        random.Random(SEED * 3 + fi).shuffle(built)
        out[f] = [b[2] for b in built]
        pos = Counter(r["c"] for r in out[f])
        assert len(out[f]) == PER_FORM and set(pos.values()) == {PER_FORM // NOPT}, (f, pos)
        lec_n = Counter(b[0] for b in built)
        assert dict(lec_n) == quota, (f, lec_n)
        cell_n = Counter(b[1] for b in built)
        back = sum(cell_n[c] for c in BACKGROUND)
        assert back <= PER_FORM - back, (f, "mechanism outweighs breadth", cell_n)
        runs, cur, mx = 1, 1, 1
        for a, b in zip(out[f], out[f][1:]):
            cur = cur + 1 if a["c"] == b["c"] else 1
            mx = max(mx, cur)
        assert mx <= 4, (f, "answer-position run of %d" % mx)
        by_lec_pos = {l: dict(sorted(Counter(b[2]["c"] for b in built if b[0] == l).items())) for l in sorted(quota)}
        game = sum(gameable(r["opts"], r["c"]) for r in out[f])
        report["forms"][f] = {"lectures": dict(sorted(lec_n.items())), "cells": dict(sorted(cell_n.items())),
                              "positions": {chr(65 + k): v for k, v in sorted(pos.items())},
                              "positions_by_lecture": by_lec_pos, "gameable": game, "max_run": mx}
        print("form %s  %d q  positions %s  lectures %s  cells %s  gameable %d  max run %d"
              % (f, len(out[f]), report["forms"][f]["positions"], dict(sorted(lec_n.items())),
                 dict(sorted(cell_n.items())), game, mx))

    # ---- no question twice, and no two forms sharing a key text on the same slide -------------------
    allq = [r["q"] for f in FORMS for r in out[f]]
    assert len(allq) == len(set(allq)) == PER_FORM * len(FORMS), "a question landed in two forms"
    for f in FORMS:
        same = defaultdict(list)
        for r in out[f]:
            same[(r["cite"], r["opts"][r["c"]][0])].append(r["q"])
        for k, v in same.items():
            if len(v) > 1:
                print("  NOTE form %s: same slide and same key twice: %s" % (f, k))
    print("%d distinct questions across the five forms" % len(allq))
    json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    report["dropped"] = {k: len(v) for k, v in dropped.items()}
    report["dropped_detail"] = {k: v for k, v in dropped.items()}
    json.dump(report, open(REPORT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", os.path.relpath(OUT, ROOT), "and", os.path.basename(REPORT))


if __name__ == "__main__":
    main()
