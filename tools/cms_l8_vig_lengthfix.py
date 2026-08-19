#!/usr/bin/env python3
"""Length-bias remediation for the CMS I Lecture 8 SET 2 (vignette) pool.

Every fix LENGTHENS A DISTRACTOR. SLOT_FIXES is keyed by (index into
POOL_A + POOL_B + POOL_C, OPTION index); the partition asserts no fix can
overwrite the correct option.

Raw rate was 8 of 64, against the objective pool A's 57%. The difference is
that every distractor in these pools was written to the same compound shape as
the answer beside it, from the first draft.
"""

SLOT_FIXES = {
 (4, 1): "Excision with clear margins is needed on every single lesion, because of the risk of transformation",
 (7, 2): "The lesions indicate an underlying internal malignancy and warrant an urgent systemic screening of the whole body",
 (21, 2): "Observation with clinical photographs, repeating the whole assessment at twelve months of age",
 (26, 1): "Numbers continue to rise throughout life, and any patient with over twenty naevi needs them all excised early",
 (31, 3): "A dysplastic naevus of the lower extremity",
 (31, 1): "A blue naevus of the lower extremity or the thigh",
 (47, 1): "PUVA is preferred, because it produces faster repigmentation across a much larger body surface area",
 (55, 1): "The vascular anomaly is unrelated, since naevus spilus has no described systemic associations at all",
 (59, 1): "Birth control use is unrelated, since solar lentigines are caused by sun exposure and nothing else",
}

if __name__ == "__main__":
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HERE)
    from cms_l8_vig_a import POOL_A
    from cms_l8_vig_b import POOL_B
    from cms_l8_vig_c import POOL_C
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
