"""Length-bias remediation for CMS I Lecture 3 Set 1 (Dermatology II).

Only 18 fixes here against 69 on Lecture 2, because this pool was drafted with
MATCHED OPTION LENGTHS from the start rather than remediated afterwards. Raw
figure: 24% gameable against Lecture 2's 66%. Writing the distractors at the
correct length while the question is being written is the actual fix; this pass
is repair for the residue.

Keyed by (question index, OPTION index) so a fix lands on the option intended,
with an assert that it can never overwrite the correct answer.
"""
SLOT_FIXES = {
 (1, 2):  "A single uniform erythematous plaque with a raised advancing border and a clear centre, without any concentric zones",
 (5, 1): "Immunoglobulin G antibodies directed against the epithelial basement membrane zone of the skin",
 (10, 1): "A paraneoplastic process driven by an underlying gastric adenocarcinoma secreting growth factors that act on the epidermis",
 (13, 1): "It is a benign cosmetic change that carries no systemic implication and requires no further investigation",
 (30, 1): "Localised disease, which predominates at about 75% of cases and affects children and young adults",
 (35, 2): "Failure of the ulcer to culture any organism despite clear clinical signs of infection",
 (38, 1): "Papulopustular, with transient central facial papules and pustules on a background of erythema and no comedones",
 (41, 1): "It eradicates Demodex folliculorum from the follicles over the course of several weeks of therapy",
 (54, 1): "Granular immunoglobulin A deposited within the dermal papillae of the skin",
 (58, 1): "Phototoxicity is immunologic and requires prior sensitisation before any reaction; photoallergy is non-immunologic, dose-dependent and occurs on the very first exposure",
 (61, 1): "Bergapten in bergamot oil used in fragrances and cosmetics, producing drip-pattern hyperpigmentation of the neck",
 (62, 1): "Painful erythema developing within minutes of ultraviolet exposure and resolving within an hour of moving into the shade",
 (63, 1): "Thickening and hardening of the skin from repeated scratching of the eruption",
 (65, 2): "Solar lentigo appears in early childhood; lentigo maligna appears only after the age of seventy",
 (67, 3): "Lesions recur at exactly the same site after treatment, so repeat cryotherapy at regular intervals is the appropriate response",
 (70, 1): "Full-thickness epidermal necrosis with dermal-epidermal junction separation",
 (71, 2): "Vitamin C, which neutralises reactive oxygen species and stimulates new collagen",
 (73, 3): "They should use SPF 15 rather than SPF 30, on the basis that higher factors confer no additional benefit",
}

if __name__ == "__main__":
    import sys, os
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from cms_l3_pool_a import POOL_A
    from cms_l3_pool_b import POOL_B
    from cms_l3_pool_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C
    M, F = 8, 0.18
    def game(q):
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = L[0], L[1]
        return ti == q["c"] and (tl - rl) >= M and tl >= rl * (1 + F)
    before = sum(game(q) for q in POOL)
    for (qi, oi), t in SLOT_FIXES.items():
        assert oi != POOL[qi]["c"], "fix %d would overwrite the CORRECT option" % qi
        POOL[qi]["opts"][oi][0] = t
    after = sum(game(q) for q in POOL)
    print("gameable before: %d/%d (%.0f%%)" % (before, len(POOL), 100*before/len(POOL)))
    print("gameable after : %d/%d (%.0f%%)" % (after, len(POOL), 100*after/len(POOL)))
    for i, q in enumerate(POOL):
        if game(q):
            L = [len(o[0]) for o in q["opts"]]
            print("  still %d: correct=%d runner=%d" % (i, L[q["c"]], max(l for j,l in enumerate(L) if j!=q["c"])))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE at %d" % i)
