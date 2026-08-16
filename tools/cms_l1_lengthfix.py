#!/usr/bin/env python3
"""Length-bias remediation for the CMS Lecture 1 pool.

Only WRONG choices are rewritten, never the correct text and never the answer
index -- that is the whole safety property of this pass. Each replacement adds
real, plausible content from the lecture's own vocabulary rather than filler,
so a distractor stays a credible distractor.

Keyed by pool index; applied then re-measured.
"""
FIXES = {
 13: (2, "Cost, availability, and expected turnaround time of the test in the local laboratory setting"),
 18: (3, "Pretest probability applies to screening programmes only, while posttest probability applies to diagnostic testing"),
 19: (1, "The sensitivity and specificity of the test will differ between the two patients being evaluated"),
 22: (0, "Generate the hypotheses first, then organise and interpret the clinical information gathered from the patient"),
 23: (0, "What disease or underlying condition does this patient have?"),
 24: (1, "What information should be gathered from the patient at the outset"),
 27: (0, "Environmental exposure"),
 28: (3, "Endocrine — traumatic brain injury and traumatic subdural haematoma"),
 29: (2, "Central nervous system lupus and neurosarcoidosis"),
 34: (0, "Published guidelines, a literature review, and the cost data for each test"),
 37: (2, "Treating the patient empirically before any diagnosis has been formally considered"),
 38: (3, "A system that applies only to unstable patients presenting to emergency medicine"),
 40: (2, "It cannot be combined with clinical guidelines, and it disregards patient values entirely"),
 42: (1, "They should be used only once evidence-based medicine has failed to answer the question"),
 45: (3, "Rely on the first diagnosis that appears to fit the presenting clinical picture"),
 51: (0, "Screening whole populations for occult disease, lowering the overall cost of care, and replacing the physical examination"),
 53: (0, "Because false-positive results simply do not occur with tests that have high sensitivity for the condition"),
 55: (2, "The base rate of the disease and the availability of a published clinical guideline"),
 56: (0, "The benefit of screening the wider population against the financial cost of confirmatory testing for each positive result"),
 58: (2, "Treatment should be started immediately, because the worst-case scenario must always be ruled out before anything else"),
 62: (0, "Only the dosing schedule and administration route of any medication prescribed"),
 63: (0, "Apply the same standardised intervention regardless of where the patient sits on that continuum"),
 64: (3, "As a task that is best delegated to non-clinical support staff within the practice"),
 66: (0, "Excess follow-up appointments and over-explanation of the possible side effects of treatment"),
 68: (1, "Medication timing, appointment keeping, and the sharing of records between providers"),
 70: (2, "Musculoskeletal medicine, rheumatology, gastroenterology, urology, and reproductive endocrinology"),
 71: (3, "Cost, local availability, expected turnaround time, and laboratory reporting format of every diagnostic test ordered for a given patient"),
}

if __name__ == "__main__":
    import sys, os, json
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from cms_l1_pool_a import POOL_A
    from cms_l1_pool_b import POOL_B
    from cms_l1_pool_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C

    M_CH, M_FR = 8, 0.18
    def gameable(q):
        lens = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = lens[0], lens[1]
        return ti == q["c"] and (tl - rl) >= M_CH and tl >= rl * (1 + M_FR)

    before = sum(gameable(q) for q in POOL)
    still = []
    # Locate the option by matching the replacement against the existing text
    # rather than trusting a hand-typed index -- three of these were typed
    # pointing at the correct answer, which would have silently changed which
    # answer the question has.
    import difflib
    for idx, (_stated, text) in FIXES.items():
        q = POOL[idx]
        cands = [(difflib.SequenceMatcher(None, text.lower(), o[0].lower()).ratio(), i)
                 for i, o in enumerate(q["opts"])]
        ratio, opt_i = max(cands)
        assert opt_i != q["c"], (
            "index %d: best text match is the CORRECT option -- rewrite aimed wrong" % idx)
        assert ratio > 0.45, "index %d: replacement matches no existing option (%.2f)" % (idx, ratio)
        q["opts"][opt_i][0] = text
    for idx in FIXES:
        if gameable(POOL[idx]):
            lens = [len(o[0]) for o in POOL[idx]["opts"]]
            runner = max(l for j, l in enumerate(lens) if j != POOL[idx]["c"])
            still.append((idx, lens[POOL[idx]["c"]], runner))
    after = sum(gameable(q) for q in POOL)
    print("gameable before: %d/%d (%.0f%%)" % (before, len(POOL), 100*before/len(POOL)))
    print("gameable after : %d/%d (%.0f%%)" % (after, len(POOL), 100*after/len(POOL)))
    if still:
        print("\nstill gameable after fix (correct_len, runner_len):")
        for idx, cl, rl in still:
            print("  #%-3d correct=%d runner=%d  need runner >= %d" %
                  (idx, cl, rl, max(cl - M_CH + 1, int(cl / (1 + M_FR)) + 1)))
    # no option text may be duplicated within a question
    for i, q in enumerate(POOL):
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION TEXT at #%d" % i)
