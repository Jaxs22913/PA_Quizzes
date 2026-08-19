#!/usr/bin/env python3
"""Length-bias remediation for the CMS I Lecture 8 SET 1 (objective) pool.

Every fix LENGTHENS A DISTRACTOR. SLOT_FIXES is keyed by (index into
POOL_A + POOL_B + POOL_C, OPTION index); the partition asserts no fix can
overwrite the correct option.

Pool A came out at 57% raw -- the highest of any pool built for this exam, and
higher even than Lecture 5's 48%. Same cause, more concentrated: this entire
deck is compare-and-contrast across a catalogue of pigmented lesions, so the
correct answer is a full compound description and every distractor names a
different lesion in fewer words. Those seventeen were repaired at source in
cms_l8_pool_a.py, and pools B and C were written with the distractors given the
same compound shape from the outset. What remains here is the residue.
"""

SLOT_FIXES = {
 (35, 1): "Lesion size alone, with every lesion over 5 mm excised regardless of its site or of graft availability at all",
 (39, 1): "They are present at birth, enlarge in proportion to the child's own growth, and never regress at any stage of life",
 (50, 3): "Beige to black papules and plaques 2 to 20 mm across that feel velvety and appear stuck onto the surface of the skin",
 (52, 1): "Diagnosis is made clinically; management is observation alone with sun protection counselling, since these lesions never progress to melanoma at all",
}

if __name__ == "__main__":
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HERE)
    from cms_l8_pool_a import POOL_A
    from cms_l8_pool_b import POOL_B
    from cms_l8_pool_c import POOL_C
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
