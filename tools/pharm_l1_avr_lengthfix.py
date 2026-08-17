"""Length-bias remediation for Pharmacology I Lecture 1, antivirals.

Only WRONG choices are rewritten; the applier excludes the correct option from
the candidate set by construction. Every replacement stays unambiguously false.
"""
FIXES = {
 0:  (2, "Disrupting the ergosterol membrane, inhibiting glucan synthesis in the cell wall, blocking mitotic spindle formation, and interfering with nucleic acid synthesis through a fluorinated nucleotide"),
 5:  (1, "It is concentrated by a membrane transporter that is expressed only on the surface of infected cells"),
 6:  (1, "It cross-links the two strands of viral DNA so that they can no longer separate"),
 12: (3, "They are viral protease inhibitors used chiefly in human immunodeficiency virus infection and hepatitis C"),
 14: (2, "Children with chickenpox presenting within the first 24 hours"),
 19: (3, "It inhibits a viral protease, preventing cleavage of polypeptide precursors into mature viral proteins"),
 21: (2, "Herpes simplex and varicella-zoster, circulating year-round"),
 30: (1, "Acyclovir is available only intravenously and cannot safely be given to a transplant recipient on immunosuppression"),
 34: (1, "Acyclovir targets viral neuraminidase directly; oseltamivir depends on thymidine kinase for activation"),
 36: (1, "Crystallisation within the renal tubule, requiring aggressive hydration throughout treatment"),
 37: (1, "They can no longer attach to the receptor on the next host cell"),
 42: (1, "The drug is only manufactured and distributed during those particular months"),
 43: (1, "Both rely on being concentrated inside infected cells by host transporters that healthy cells lack"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pharm_l1_avr_pool_a import POOL_A
    from pharm_l1_avr_pool_b import POOL_B
    POOL = POOL_A + POOL_B
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
            r = max(l for j, l in enumerate(L) if j != q["c"])
            print("  still %d: correct=%d runner=%d" % (i, L[q["c"]], r))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION at %d" % i)
