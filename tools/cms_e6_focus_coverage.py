#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Coverage audit: every Lecture 37/38 STUDY-FOCUS point against the questions that practise it.

    python3 tools/cms_e6_focus_coverage.py          # writes tools/cms_e6_focus_coverage.json

Reads the points and the existing-question map from tools/cms_e6_focus_points.py, every L37/L38 topic pool
(through cms_e6_partition.load_guarded, patches and length fixes applied) and the new study-focus pools
(tools/cms_e6l37_focus_*.py, tools/cms_e6l38_focus_*.py), and each question's review state in
tools/blind_review.json ("clean" = blind pick equals the key AND a current audit pass, as the masters use).

STATUS (of the EXISTING topic-pool questions, i.e. before the study-focus items were written):
  covered  at least 2 cleanly reviewed questions practise the point (one per Study Focus set)
  thin     exactly 1, or the clean questions miss the part of the point the slide stresses (OVERRIDE below)
  missing  none
`new` lists the study-focus questions written for the point and their review state.
"""
import os, sys, json, glob, importlib
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
_argv = sys.argv; sys.argv = [_argv[0], "l37io"]
import cms_e6_partition as P
sys.argv = _argv
import cms_e6_masters_partition as M
import blind_review as BR
from cms_e6_focus_points import POINTS, POINT_IDS, EXISTING, focus_of

OUT = os.path.join(HERE, "cms_e6_focus_coverage.json")
SLIDE = {"l37": "37. Respiratory Infections - Bobilin - 10-29-2026 SV.pptx, Slide 127 (Slide 128 repeats it)",
         "l38": "38. Mycobacterial Infections including Tuberculosis - Bobilin - 10-29-2025 SV.pptx, Slide 41"}

# clean questions exist, but none practises the part of the point the slide singles out
OVERRIDE = {
 "l37-pneumo-seq": "clean items cover only 'PCV20 or PCV21 completes the series'; none asks when PCV15 needs PPSV23 afterward",
 "l37-antibiogram": "the clean HAP/VAP regimen items imply local data (MRSA common in the unit) but none asks what selects the empiric regimen",
 "l37-deescalate": "narrowing is practised only for community-acquired pneumonia (blood culture) and VAP duration; none de-escalates HAP/VAP",
 "l37-histo-severity": "clean items cover mild acute disease (observation) and chronic cavitary duration; none covers itraconazole or severe disease (amphotericin-based induction)",
 "l38-tst5": "the clean 5 mm items are a recall item and transplant/old-film vignettes; the HIV and recent-contact vignettes were flagged in review",
}


def focus_pool_modules(lec, vig):
    pat = "cms_e6%s_focus_%s.py" % (lec, "vig" if vig else "pool")
    return sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, pat)))


def load_all():
    rec = BR.load_records()
    rows = []
    for lec in ("l37", "l38"):
        P.LEADS = M.BASE_LEADS + M.EXTRA_LEADS.get(lec, ())
        for vig in (False, True):
            scope, mods, pool, origin, _ = P.load_guarded(lec, vig)
            for q, o in zip(pool, origin):
                rows.append(dict(lec=lec, kind="vig" if vig else "reg", src="%s[%d]" % o, new=False, q=q,
                                 state=M.review_state(rec, q)))
            for m in focus_pool_modules(lec, vig):
                for i, q in enumerate(importlib.import_module(m).QUESTIONS):
                    q = json.loads(json.dumps(q)); q.setdefault("c", 0)
                    rows.append(dict(lec=lec, kind="vig" if vig else "reg", src="%s[%d]" % (m, i), new=True, q=q,
                                     state=M.review_state(rec, q)))
    return rows


def main():
    rows = load_all()
    used_keys = Counter()
    for r in rows:
        if not r["new"]:
            for k in EXISTING:
                if r["q"]["q"].startswith(k):
                    used_keys[k] += 1
    unmatched = [k for k in EXISTING if used_keys[k] == 0]
    dup = [k for k, n in used_keys.items() if n > 1]
    assert not unmatched, "EXISTING keys that match no pool question: %r" % unmatched[:5]
    assert not dup, "EXISTING keys that match two pool questions: %r" % dup[:5]
    for r in rows:
        r["focus"] = focus_of(r["q"])
        bad = [f for f in r["focus"] if f not in POINT_IDS]
        assert not bad, "unknown focus id %r on %s" % (bad, r["src"])
        assert not r["new"] or r["focus"], "new item without a focus list: %s" % r["src"]

    out = {"built_by": "tools/cms_e6_focus_coverage.py", "slides": SLIDE,
           "status_rule": "covered = 2+ cleanly reviewed existing questions; thin = 1, or the clean ones miss the stressed part (note); missing = 0",
           "points": []}
    for pid, lec, group, label, slide in POINTS:
        ex = [r for r in rows if not r["new"] and pid in r["focus"]]
        clean = [r for r in ex if r["state"] == "clean"]
        status = "missing" if not clean else ("thin" if len(clean) == 1 or pid in OVERRIDE else "covered")
        item = lambda r: {"src": r["src"], "kind": r["kind"], "state": r["state"], "stem": r["q"]["q"][:160],
                          "key": r["q"]["opts"][0][0]}
        out["points"].append({
            "id": pid, "lecture": lec, "group": group, "point": label, "slide_words": slide,
            "status": status, "note": OVERRIDE.get(pid),
            "existing_clean": [item(r) for r in clean],
            "existing_not_clean": [item(r) for r in ex if r["state"] != "clean"],
            "new": [item(r) for r in rows if r["new"] and pid in r["focus"]],
        })
    for lec in ("l37", "l38"):
        pts = [p for p in out["points"] if p["lecture"] == lec]
        out.setdefault("summary", {})[lec] = dict(Counter(p["status"] for p in pts), points=len(pts),
            missing=[p["id"] for p in pts if p["status"] == "missing"],
            thin=[p["id"] for p in pts if p["status"] == "thin"],
            new_items=sum(1 for r in rows if r["new"] and r["lec"] == lec),
            new_clean=sum(1 for r in rows if r["new"] and r["lec"] == lec and r["state"] == "clean"),
            points_without_a_clean_item=[p["id"] for p in pts if not p["existing_clean"]
                                         and not any(n["state"] == "clean" for n in p["new"])])
    json.dump(out, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    for lec, s in out["summary"].items():
        print(lec, {k: v for k, v in s.items()})
    print("wrote", os.path.relpath(OUT, os.path.dirname(HERE)))


if __name__ == "__main__":
    main()
