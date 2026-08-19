#!/usr/bin/env python3
"""Length-bias remediation for the CMS I Lecture 3 SET 2 (vignette) pool.

A question is length-gameable when the correct option is the longest AND is at
least 8 characters and 18% longer than the next longest. A student who reads
nothing but option lengths would score above chance on those.

Every fix here LENGTHENS A DISTRACTOR. Nothing shortens the correct answer,
because the explanation of why an answer is right is the part worth reading.

SLOT_FIXES is keyed by (index into POOL_A + POOL_B + POOL_C, OPTION index) so a
fix lands on exactly the slot it was written for. The partition script asserts
no fix can ever overwrite the correct option.

Pool C came out at 3% raw — 1 of 29 — which is the lowest of any pool built so
far, and confirms the Lecture 3 finding that matching option lengths while
drafting is far cheaper than repairing afterwards.
"""

SLOT_FIXES = {
 (7, 1): "Dapsone alone controls the condition completely, so a change in diet is optional provided the rash stays quiet",
 (9, 3): "Reassure her that the change is cosmetic and arrange routine follow-up with lifestyle advice in six months",
 (10, 1): "The change is caused by friction from clothing against the neck and will settle with softer, looser fabrics",
 (14, 1): "Gene therapy will cure the condition entirely once the child is old enough to be enrolled for treatment",
 (16, 1): "Increase the second-generation antihistamine to four times the standard licensed daily dose",
 (20, 1): "A specific environmental or dietary trigger can be identified in almost every case if enough testing is done",
 (24, 1): "A prolonged course of oral antibiotics directed at streptococcal infection",
 (26, 3): "Begin oral terbinafine on the assumption of a widespread dermatophyte infection of the trunk and limbs",
 (27, 3): "It will persist unchanged for life unless systemic immunosuppressive therapy is started early in the course",
 (29, 1): "Take a punch biopsy from the centre of the ulcer for direct immunofluorescence",
 (35, 1): "A twelve-week course of oral antibiotics usually produces a permanent remission with no need for any further treatment",
 (44, 1): "Avoid the causative drug for six months, after which a cautious supervised rechallenge in hospital is reasonable to consider",
}

if __name__ == "__main__":
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HERE)
    from cms_l3_vig_a import POOL_A
    from cms_l3_vig_b import POOL_B
    from cms_l3_vig_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C

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
