#!/usr/bin/env python3
"""Length-bias remediation for the CMS I Lecture 4 SET 1 (objective) pool.

A question is length-gameable when the correct option is the longest AND is at
least 8 characters and 18% longer than the next longest.

Every fix LENGTHENS A DISTRACTOR. Nothing shortens the correct answer.

SLOT_FIXES is keyed by (index into POOL_A + POOL_B + POOL_C, OPTION index) so a
fix lands on exactly the slot it was written for. The partition script asserts
no fix can ever overwrite the correct option.

Raw rate for this pool was 5 of 100 -- the lowest of any Set 1 pool so far, and
the fourth confirmation that matching option lengths while drafting beats
repairing afterwards.
"""

SLOT_FIXES = {
 (23, 3): "A foreign body reaction to a cut hair that curves back into the wall of the follicle",
 (41, 1): "A single firm tender nodule with one opening and a surrounding zone of erythema and swelling",
 (42, 2): "Only after culture has confirmed methicillin-resistant Staphylococcus aureus in the material that was drained",
 (61, 1): "In every case at first presentation, since staphylococcal and streptococcal disease are treated differently from one another",
 (90, 3): "The muscle compartment itself; almost always Clostridium perfringens acquired through an open wound",
}

if __name__ == "__main__":
    import sys, os
    HERE = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, HERE)
    from cms_l4_pool_a import POOL_A
    from cms_l4_pool_b import POOL_B
    from cms_l4_pool_c import POOL_C
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
