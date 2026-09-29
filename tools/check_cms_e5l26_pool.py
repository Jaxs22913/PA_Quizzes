#!/usr/bin/env python3
"""Run the guarded-partition checks on ONE Lecture 26 pool module (or all present) without partitioning.

    python3 tools/check_cms_e5l26_pool.py cms_e5l26_pool_b [more modules ...]
    python3 tools/check_cms_e5l26_pool.py            # every cms_e5l26_pool_* / cms_e5l26_vig_* present
"""
import glob, importlib, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
mods = sys.argv[1:] or sorted(os.path.basename(p)[:-3] for p in glob.glob(os.path.join(HERE, "cms_e5l26_*_*.py"))
                              if os.path.basename(p)[:-3].rsplit("_", 2)[-2] in ("pool", "vig"))
sys.argv = [sys.argv[0], "l26io"]                       # the partition module reads argv at import
import cms_e5_partition as P
scope = importlib.import_module("cms_e5l26_scope")
rc = 0
for m in mods:
    vig = "_vig_" in m
    qs = importlib.import_module(m).QUESTIONS
    pool, origin = [], []
    for i, q in enumerate(qs):
        q = json.loads(json.dumps(q)); q.setdefault("c", 0); pool.append(q); origin.append((m, i))
    try:
        P.guard_all(scope, pool, origin, vig)
        from collections import Counter
        extra = ""
        if vig:
            extra = "  leads=%s" % dict(Counter(q["lead"] for q in pool))
        req = {lab: sum(1 for q in pool if __import__("re").search(sr, q["q"], 2)) for lab, sr, kr, n in scope.REQUIRED}
        print("%-26s OK   %3d questions  slots=%d  required-stems=%s%s" % (m, len(pool), len({q['slot'] for q in pool}), req, extra))
    except AssertionError as e:
        rc = 1
        print("%-26s FAILED\n%s" % (m, e))
sys.exit(rc)
