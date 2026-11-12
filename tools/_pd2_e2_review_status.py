#!/usr/bin/env python3
"""Which PD2 Exam 2 pool questions (Lectures 5-7) hold a current blind + audit PASS.

The Exam 2 master forms may only use passed items (brief 2026-11-12). Review records live in
tools/blind_review.json keyed to the item's stem + option texts, and the audit is current only
when the key, explanations and `mis` are unchanged -- the same tests `blind_review.py check` runs,
applied here to POOL items (shipped or held) rather than to pages.

    from _pd2_e2_review_status import passed     # passed(q) -> True / False
    python3 tools/_pd2_e2_review_status.py       # counts per lecture
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import blind_review as BR

_REC = BR.load_records()


def _mis_list(q):
    m = q.get("mis") or {}
    out = []
    for i, o in enumerate(q["opts"]):
        out.append("" if i == q["c"] else (m.get(o[0], "") if isinstance(m, dict) else ""))
    return out


def status(q):
    """Status as the item would have on a PAGE (no `mis` in the page; blind_review attaches it from
    the *_sets.json sources, exactly as for the master forms)."""
    page_q = {k: v for k, v in q.items() if k != "mis"}
    it = BR.attach_sources([BR.Q("Physical Diagnosis 2 Exam 2", "x.html", 0, page_q)])[0]
    h = it.h
    r = _REC.get(h) or {}
    p = r.get("passes", {})
    if not p.get("blind"):
        return "no blind"
    a = p.get("audit")
    if not a:
        return "no audit"
    if a.get("ah") != it.ah:
        return "stale audit"
    return "pass" if a.get("verdict") == "pass" else a.get("verdict")


def passed(q):
    return status(q) == "pass"


def pools():
    import pd2_l5_pool_a, pd2_l5_pool_b, pd2_l6_pool_a, pd2_l6_pool_b, pd2_l7_pool_a, pd2_l7_pool_b
    out = {}
    for lec, mods in (("L5", (pd2_l5_pool_a, pd2_l5_pool_b)), ("L6", (pd2_l6_pool_a, pd2_l6_pool_b)),
                      ("L7", (pd2_l7_pool_a, pd2_l7_pool_b))):
        qs = []
        for m in mods:
            for k, v in vars(m).items():
                if k.startswith("POOL") and isinstance(v, list) and v and isinstance(v[0], dict) and "opts" in v[0]:
                    qs += v
        out[lec] = qs
    return out


if __name__ == "__main__":
    from collections import Counter
    for lec, qs in pools().items():
        print(lec, len(qs), dict(Counter(status(q) for q in qs)))
