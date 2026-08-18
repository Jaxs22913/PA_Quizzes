"""Length-bias remediation for Physical Diagnosis 2, Lecture 1.

Only wrong choices are rewritten; the applier excludes the correct option from
the candidate set by construction. Every replacement stays unambiguously false.
"""
FIXES = {
 6:  (3, "None — a focused encounter narrows the physical examination but never narrows the history at all"),
 7:  (1, "A diagnosis and a prescription, with the reasoning behind them left implicit rather than stated aloud"),
 13: (1, "Earlier work may contain clinical guidance that has since changed and would now be inaccurate"),
 14: (3, "Keep communication strictly to the presenting clinical question and nothing further"),
 15: (2, "Ask the course team for a single standardised rubric so that any disagreement between facilitators is settled"),
 16: (1, "A classmate's completed version of the very same assignment for comparison"),
 17: (1, "The physical examination is narrowed while the history is still taken in full"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pd2_l1_pool_a import POOL_A as POOL
    M, F = 8, 0.18
    def game(q):
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = L[0], L[1]
        return ti == q["c"] and (tl - rl) >= M and tl >= rl * (1 + F)
    before = sum(game(q) for q in POOL)
    for idx, (_stated, text) in FIXES.items():
        q = POOL[idx]
        ratio, oi = max((difflib.SequenceMatcher(None, text.lower(), o[0].lower()).ratio(), i)
                        for i, o in enumerate(q["opts"]) if i != q["c"])
        assert ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (idx, ratio)
        q["opts"][oi][0] = text
    after = sum(game(q) for q in POOL)
    print("gameable before: %d/%d (%.0f%%)" % (before, len(POOL), 100*before/len(POOL)))
    print("gameable after : %d/%d (%.0f%%)" % (after, len(POOL), 100*after/len(POOL)))
    for i, q in enumerate(POOL):
        if game(q):
            L = [len(o[0]) for o in q["opts"]]
            print("  still %d: correct=%d runner=%d" % (i, L[q["c"]], max(l for j,l in enumerate(L) if j!=q["c"])))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION at %d" % i)
