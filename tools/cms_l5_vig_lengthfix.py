#!/usr/bin/env python3
"""Length-bias remediation for the CMS I Lecture 5 SET 2 (vignette) pool.

Every fix LENGTHENS A DISTRACTOR. SLOT_FIXES is keyed by (index into
POOL_A + POOL_B + POOL_C + POOL_D, OPTION index); the partition asserts no fix can
overwrite the correct option.
"""

SLOT_FIXES = {
 (11, 1): "She must stay home until every single nit has been combed out of her hair completely",
 (33, 3): "Observe him for six hours, since all the symptoms of this envenomation resolve within that time",
 (35, 1): "Immediate wide excision of the necrotic area with primary closure of the resulting skin defect",
 (45, 1): "Request the human Lyme vaccine, which is recommended for anyone living in or visiting an endemic region",
 (50, 1): "A single dose of doxycycline should be taken now to prevent the illness from developing at all over the coming days",
 (53, 2): "Overnight topical permethrin applied to the whole skin surface with a repeat dose at one week",
 (65, 1): "Have the home professionally fumigated and then discard all the pillows and the soft furnishings",
 (66, 1): "Applying mayonnaise or mineral oil weekly to smother the live lice and their attached eggs on the hair",
 (75, 1): "Testing is not indicated at all, since Lyme disease occurs only in the northeastern states of the country",
 (78, 1): "Doxycycline must be avoided under eight years of age, so azithromycin is substituted instead",
}

if __name__ == "__main__":
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HERE)
    from cms_l5_vig_a import POOL_A
    from cms_l5_vig_b import POOL_B
    from cms_l5_vig_c import POOL_C
    from cms_l5_vig_d import POOL_D
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
