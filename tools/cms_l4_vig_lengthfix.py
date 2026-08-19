#!/usr/bin/env python3
"""Length-bias remediation for the CMS I Lecture 4 SET 2 (vignette) pool.

Every fix LENGTHENS A DISTRACTOR. SLOT_FIXES is keyed by (index into
POOL_A + POOL_B + POOL_C + POOL_D, OPTION index); the partition asserts no fix
can overwrite the correct option.

Raw rate was 4 of 72.
"""

SLOT_FIXES = {
 (3, 1): "Pregnancy testing is required only before starting, after which monthly liver function tests replace it entirely",
 (28, 1): "Avoid sharing towels, clothing, bath water, washcloths and razors with anyone else in the household",
 (62, 1): "Extend the doxycycline course to twelve months, to give the oral antibiotic more time to take effect",
 (70, 1): "Complete blood count and inflammatory markers only, since the remaining studies add nothing to management",
}

if __name__ == "__main__":
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HERE)
    from cms_l4_vig_a import POOL_A
    from cms_l4_vig_b import POOL_B
    from cms_l4_vig_c import POOL_C
    from cms_l4_vig_d import POOL_D
    POOL = POOL_A + POOL_B + POOL_C + POOL_D

    MARGIN_CHARS, MARGIN_FRAC = 8, 0.18

    def gameable(q):
        lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = lens[0], lens[1]
        return ti == q["c"] and (tl - rl) >= MARGIN_CHARS and tl >= rl * (1 + MARGIN_FRAC)

    before = sum(gameable(q) for q in POOL)
    for (qi, oi), text in SLOT_FIXES.items():
        assert oi != POOL[qi]["c"], "fix %d would overwrite the correct option" % qi
        POOL[qi]["opts"][oi][0] = text
    after = [i for i, q in enumerate(POOL) if gameable(q)]
    print("%d questions: %d gameable before (%d%%), %d after (%d%%)"
          % (len(POOL), before, round(100 * before / len(POOL)),
             len(after), round(100 * len(after) / len(POOL))))
    for i in after:
        print("  still gameable:", i, [len(o[0]) for o in POOL[i]["opts"]], POOL[i]["q"][:55])
