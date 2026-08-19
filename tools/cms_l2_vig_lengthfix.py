"""Length-bias remediation for CMS I Lecture 2 Set 2 (the vignettes).

Keyed by (question index, OPTION index) rather than by text similarity. The
similarity-matched approach used elsewhere kept landing on a different option
than the longest one, which meant three rounds of chasing on the Set 1 pool.
Naming the slot directly gets it in one, and an assert makes it impossible for a
fix to overwrite the correct answer.

Every replacement stays a genuine wrong answer of the kind the vignette style
calls for: right disease at the wrong phase, right drug for the wrong severity,
or a real lookalike condition from this lecture. Nothing here is padding.
"""
SLOT_FIXES = {
 (0, 3):  "Systemic prednisone for four weeks with a slow taper",
 (3, 3):  "Advise that the condition resolves permanently by school age, so consistent daily treatment is optional and can be stopped whenever the skin looks clear",
 (7, 3): "Ketoconazole shampoo applied to all the affected areas",
 (9, 1):  "Begin a high-potency topical corticosteroid indefinitely, continuing it daily even once the hands have healed, without addressing the exposure",
 (10, 1): "Irritant contact dermatitis of the hands",
 (11, 2): "A five-day course of oral prednisone without any taper",
 (12, 3): "Future exposure to the same adhesive will not provoke a reaction once this episode has settled",
 (14, 1): "A single two-week course of antifungal shampoo is usually curative and needs no repeating",
 (15, 3): "Apply an occlusive moisturiser several times each day instead",
 (16, 3): "The condition will not recur once the corticosteroid has been stopped once",
 (19, 3): "A high-potency topical corticosteroid applied at every change until the rash has completely cleared",
 (21, 2): "High-potency topical corticosteroids as the sole long-term therapy",
 (23, 1): "Take long hot showers each morning to hydrate the skin thoroughly, then apply a light lotion once the skin has completely dried",
 (25, 1): "Potassium hydroxide preparation of the blister roof",
 (31, 3): "Begin a biologic agent such as etanercept, adalimumab, infliximab or ixekizumab",
 (32, 2): "Restart the oral prednisone at the previous dose and then continue it indefinitely thereafter",
 (34, 2): "Salicylic acid — caution with systemic absorption in children",
 (36, 3): "It is highly contagious by direct skin contact, so he should avoid close contact with others until every last lesion has faded",
 (39, 3): "Hepatitis C is the established cause of this condition, so treating the infection will reliably clear the rash",
 (40, 1): "Topical tacrolimus ointment",
 (41, 3): "Begin an oral antifungal such as terbinafine, on the basis that the thickened scaly plaque is most likely a fungal infection of long standing",
 (44, 1): "The hair loss is permanent, because the follicle and its stem cells have been destroyed",
 (45, 3): "Trichotillomania from chronic hair pulling",
 (46, 3): "It can safely be shared with a female partner who is also experiencing hair thinning at the crown",
 (47, 1): "Oral finasteride prescribed as first-line therapy for female-pattern hair loss at any age after puberty",
 (52, 1): "Bacterial culture and sensitivity",
 (58, 2): "Potassium hydroxide preparation taken from the herald patch",
 (59, 1): "Chronic idiopathic urticaria entirely unrelated to any blistering disease",
 (62, 1): "Wash the hands frequently with an antibacterial soap through the course of the day, in order to prevent secondary bacterial infection of the ruptured vesicles",
 (63, 3): "Reassure that the eruption is self-limited and requires no action",
}

if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from cms_l2_vig_a import POOL_A
    from cms_l2_vig_b import POOL_B
    from cms_l2_vig_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C
    M, F = 8, 0.18
    def game(q):
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = L[0], L[1]
        return ti == q["c"] and (tl - rl) >= M and tl >= rl * (1 + F)
    before = sum(game(q) for q in POOL)
    for (qi, oi), text in SLOT_FIXES.items():
        assert oi != POOL[qi]["c"], "fix %d would overwrite the CORRECT option" % qi
        POOL[qi]["opts"][oi][0] = text
    after = sum(game(q) for q in POOL)
    print("gameable before: %d/%d (%.0f%%)" % (before, len(POOL), 100*before/len(POOL)))
    print("gameable after : %d/%d (%.0f%%)" % (after, len(POOL), 100*after/len(POOL)))
    for i, q in enumerate(POOL):
        if game(q):
            L = [len(o[0]) for o in q["opts"]]
            print("  still %d: correct=%d runner=%d" % (i, L[q["c"]],
                  max(l for j, l in enumerate(L) if j != q["c"])))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION at %d" % i)
