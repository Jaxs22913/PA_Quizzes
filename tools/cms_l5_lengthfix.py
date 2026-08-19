#!/usr/bin/env python3
"""Length-bias remediation for the CMS I Lecture 5 SET 1 (objective) pool.

Every fix LENGTHENS A DISTRACTOR. SLOT_FIXES is keyed by (index into
POOL_A + POOL_B + POOL_C, OPTION index); the partition asserts no fix can
overwrite the correct option.

Pool C of this lecture is the counterexample to the run of low rates. It came
out at 48% raw -- 15 of 31 -- because the lecture's spider and tick sections are
compare-and-contrast material, so the correct answer is naturally a compound
clause ("organism, vector, and risk factors") while every wrong-disease
distractor is a single one. Length matching is not automatic just because you
intend it; it has to be checked per question against the structure the CONTENT
imposes. Those fifteen were repaired at source in cms_l5_pool_c.py by giving the
distractors the same compound shape, which is the right fix. What remains here
is the residue across all three pools.
"""

SLOT_FIXES = {
 (18, 1): "Post-streptococcal glomerulonephritis, treated with supportive care while the kidney function recovers on its own",
 (24, 3): "Skin scraping of an unexcoriated papule with mineral oil, examined under a microscope",
 (25, 2): "Children must remain out of school for two weeks after the treatment has been completed",
 (29, 3): "Weekly application of an occlusive agent such as mayonnaise or mineral oil to smother the live lice and eggs",
 (44, 1): "Direct penetration of the skin by larvae that then migrate through the epidermal layer of the skin",
}

if __name__ == "__main__":
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HERE)
    from cms_l5_pool_a import POOL_A
    from cms_l5_pool_b import POOL_B
    from cms_l5_pool_c import POOL_C
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
