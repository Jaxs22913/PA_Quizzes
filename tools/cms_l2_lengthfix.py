"""Length-bias remediation for CMS I Lecture 2 Set 1 (General Dermatology I).

The raw pool came out 66% gameable, the highest of any build on this site, and
the cause is structural rather than careless. This lecture's correct answers are
enumerations -- "erythema, oedema, papules, vesicles, oozing and crusting" --
because that is how the material is actually taught, while the natural wrong
answer is a single clause. Truncating the correct options would throw away the
content the question exists to test, so instead every distractor is given the
same register: a multi-clause answer gets multi-clause distractors.

Each replacement stays unambiguously WRONG, and most are wrong by describing a
real condition from elsewhere in the lecture -- which makes them better
distractors than padding would, because a student who confuses the two
conditions is exactly who should miss the question.

Only wrong choices are rewritten; the applier excludes the correct option by
construction. Keys index the concatenated pool (A + B + C).
"""
FIXES = {
 # ---- pool A: terminology, tools, pharmacology
 1:   (71,  "A flat elevated plateau lesion measuring greater than one centimetre across"),
 2:   (72,  "A plaque is always poorly demarcated while a patch is always well demarcated"),
 4:   (74,  "A deposit of blood in the skin measuring one to two millimetres across"),
 7:   (70,  "Petechiae are 4 mm or greater and purpura are 1 to 2 mm, the reverse of the usual"),
 9:  (107, "An ulceration involves only the epidermis and always heals without scarring, while an erosion reaches the dermis or deeper"),
 11:  (95, "A scratch or abrasion in which the top layer of the skin is worn away by repeated rubbing or friction"),
 12:  (64,  "Smaller than one centimetre in every dimension measured"),
 15:  (104, "Short-wave ultraviolet light, used to sterilise the skin surface before a procedure is performed"),
 17:  (130, "Rapid detection of fungal elements in skin, hair or nail, with fungal culture preferred for confirmation of the species"),
 21:  (90,  "A magnified imaging method for viewing the scalp and hair follicles without touching them"),
 23:  (52,  "Photosensitivity, dryness and marked irritation"),
 25:  (122, "They are effective for scalp and nail infections without any need for systemic therapy, and are the mainstay of treatment for allergic contact dermatitis"),
 27:  (153, "Creams, because they spread most easily over large areas and are the foundation of treatment for xerosis, eczema, irritant dermatitis and diaper dermatitis"),
 28:  (81, "A rash that improves steadily with over-the-counter emollients used alone twice daily"),
 29:  (81,  "Because most drug eruptions occur only after six months of continuous therapy"),
 # ---- pool B: eczemas and dermatitides
 30:  (155, "Eczema is the broad category for inflammatory skin disorders and dermatitis is one pruritic subtype within it, so the two should never be used interchangeably"),
 31:  (142, "Acute disease shows lichenification and pigment alteration; chronic disease shows erythema, oedema, vesicles, oozing and crusting"),
 34:  (156, "Infants: flexures and popliteal fossae. Children: extensor surfaces and scalp. Adults: cheeks, scalp and the extensor surfaces of the limbs"),
 36:  (152, "By serum immunoglobulin E level, which is measured routinely in every patient and establishes the diagnosis on its own without any clinical assessment"),
 37:  (61, "High-potency topical corticosteroids applied to the face"),
 39:  (114, "On the flexural surfaces of the elbows and knees, with vesicles described as herald patches preceding the wider eruption"),
 42:  (77,  "Adolescents in the weeks following a streptococcal throat infection"),
 43:  (115, "Well-demarcated salmon-pink plaques with prominent silvery scale on the extensor surfaces of the elbows and knees"),
 44:  (120, "An immunoglobulin E-mediated immediate hypersensitivity reaction, and it is the most common form of contact dermatitis"),
 45:  (141, "All irritants produce symptoms 48 to 72 hours after exposure regardless of whether the agent is a mild soap or a concentrated acid"),
 46:  (72,  "An immunoglobulin E-mediated type I immediate hypersensitivity reaction"),
 47:  (65, "Perfumes and fragrance mixes — approximately 60% of people"),
 48:  (120, "Well-demarcated plaques shaped like the object contacted, erupting within minutes of exposure and clearing within a day"),
 49:  (95,  "No, and the resin cannot be transferred once it has dried onto clothing or bedding"),
 50:  (122, "High-potency topical steroids alone regardless of how extensive the eruption is across the body surface area"),
 52:  (132, "Well-demarcated salmon plaques with prominent silvery scale on the extensor elbows, knees, trunk, scalp, umbilicus and sacrum"),
 53:  (89,  "High-potency topical corticosteroids alone, continued long term as monotherapy"),
 54:  (31, "Overgrowth of Malassezia yeast"),
 55:  (120, "Prominent greasy yellow scale involving the scalp, eyebrows, glabella and the nasolabial folds bilaterally"),
 56:  (65, "A higher-potency topical corticosteroid applied twice daily"),
 57:  (142, "Irritant disease produces satellite papules and pustules within the inguinal folds while candidal disease spares them entirely"),
 59:  (185, "A topical antifungal applied at every diaper change regardless of cause, together with a course of oral antibiotics to prevent secondary bacterial infection of the damaged barrier"),
 60:  (76, "Arterial insufficiency arising from established peripheral arterial disease"),
 62:  (97,  "Identifying the causative organism by culture and selecting an appropriate antibiotic"),
 64:  (76,  "Compression therapy, applied immediately in all patients on presentation"),
 # ---- pool C: vesiculobullous, psoriasis, lichen, alopecia
 65:  (120, "Subepithelial, from a delayed type IV hypersensitivity reaction, most often in children and young adults"),
 66:  (87,  "A herald patch followed one to two weeks later by a Christmas tree pattern"),
 67:  (77, "Band-like infiltration of neutrophils throughout the papillary dermis"),
 68:  (145, "Autoimmune damage to the epithelial basement membrane producing subepithelial blistering that resolves without any scarring"),
 69:  (150, "Subepithelial rather than intraepithelial, flaccid rather than tense blisters, a positive Nikolsky sign, and no acantholysis on biopsy"),
 70:  (80, "Fine white lacy lines appearing across the surface of the plaques"),
 71:  (93, "On the lower legs in the gaiter region, and it is far more common in older men than women"),
 72:  (131, "With watchful observation alone, since the disease usually remits spontaneously within five to six years without treatment"),
 75:  (80, "Chronic kidney disease, hepatic cirrhosis and early osteoporosis"),
 76:  (166, "Coin-shaped, intensely pruritic light pink scaly plaques scattered over the extremities and trunk without any degree of central clearing"),
 78:  (147, "Erythematous patches with margins studded with subcorneal pustules, appearing typically in the third trimester of pregnancy"),
 79:  (200, "A slowly progressive eruption of silvery plaques developing over months on the extensor surfaces of the elbows and knees, without fever, malaise or any systemic upset"),
 81:  (72, "Green nail discoloration and chronic paronychia of the nail folds"),
 82:  (65, "Salicylic acid — caution with systemic absorption in children"),
 83:  (80,  "Phototherapy is contraindicated in pregnancy; acitretin is used instead"),
 84:  (134, "A single tense bulla on the trunk, occurring in about a third of cases before the wider eruption appears elsewhere"),
 85:  (125, "It appears on the extensor surfaces and persists indefinitely unless it is treated with phototherapy"),
 86:  (120, "A tapering course of oral prednisone given over two to three weeks from the outset of the eruption"),
 87:  (47, "Purple, painless, peripheral pustules"),
 88:  (64, "Atrophic stretch marks from prolonged topical steroid use"),
 91:  (120, "Penicillins, cephalosporins and the macrolide antibiotics, taken either as a class or individually"),
 92:  (102, "An autoimmune attack that destroys both the hair follicle and its stem cell compartment"),
 93:  (97, "Systemic antibiotics given long term in order to prevent recurrent secondary infection"),
 94:  (128, "Autoantibodies destroy the follicle and its entire stem cell compartment, so that regrowth is never possible"),
 97:  (97, "Oral finasteride in adults and topical minoxidil in children under the age of ten years"),
 99:  (199, "Male pattern produces diffuse thinning of the central and parietal scalp while female pattern recedes at the frontotemporal hairline in a triangular shape then the vertex"),
 100:  (194, "A topical 5-alpha-reductase inhibitor applied to the crown, whose effects on libido and erectile function are permanent and do not reverse at all when the drug is stopped"),
 102:  (172, "An autoimmune process affecting the epithelial basement membrane, occurring most often in the elderly and remitting spontaneously after five or six years"),
 103:  (136, "Long hot showers followed by a light lotion applied only once the skin has completely dried"),
}

# A second pass, keyed by (question index, OPTION index).
#
# The dict above finds its target by text similarity, which is right when a
# replacement is a rewrite of one specific wrong answer. For the last few it
# picked a different option than the longest one, so the longest wrong choice
# stayed short and the question stayed gameable. These name the slot directly.
SLOT_FIXES = {
 (70, 3): "Fine white lacy lines appearing across the surface of the affected plaques",
 (75, 1): "Chronic kidney disease, hepatic cirrhosis and early-onset osteoporosis",
 (76, 2): "Coin-shaped, intensely pruritic light pink scaly plaques scattered over the extremities and the trunk, uniform in appearance and without any degree of central clearing",
 (78, 3): "Erythematous patches with margins studded with subcorneal pustules, appearing typically during the third trimester of pregnancy",
 (79, 1): "A slowly progressive eruption of silvery scaling plaques developing over many months on the extensor surfaces of the elbows and knees, without fever, chills, malaise or any systemic upset at all",
 (85, 3): "It appears on the extensor surfaces of the limbs and persists indefinitely unless it is treated with phototherapy",
 (86, 1): "A tapering course of oral prednisone given over a period of two to three weeks from the outset of the eruption",
 (87, 3): "Purple, painless, peripheral pustular lesions",
 (91, 1): "Penicillins, cephalosporins and the macrolide antibiotics, taken either together as a class or individually",
 (94, 1): "Autoantibodies destroy the hair follicle and its entire stem cell compartment, so that any regrowth is never possible",
 (103, 1): "Long hot showers taken twice daily, followed by a light fragrance-free lotion applied only once the skin has completely dried",
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from cms_l2_pool_a import POOL_A
    from cms_l2_pool_b import POOL_B
    from cms_l2_pool_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C
    M, F = 8, 0.18
    def game(q):
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = L[0], L[1]
        return ti == q["c"] and (tl - rl) >= M and tl >= rl * (1 + F)
    before = sum(game(q) for q in POOL)
    for idx, (_stated, text) in FIXES.items():
        q = POOL[idx]
        ratio, oi = max((difflib.SequenceMatcher(None, text.lower(), o[0].lower()).ratio(), i)
                        for i, o in enumerate(q["opts"]) if i != q["c"])
        assert ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (idx, ratio)
        q["opts"][oi][0] = text
    for (qi, oi2), text in SLOT_FIXES.items():
        assert oi2 != POOL[qi]["c"], "slot fix %d would overwrite the CORRECT option" % qi
        POOL[qi]["opts"][oi2][0] = text
    after = sum(game(q) for q in POOL)
    print("gameable before: %d/%d (%.0f%%)" % (before, len(POOL), 100*before/len(POOL)))
    print("gameable after : %d/%d (%.0f%%)" % (after, len(POOL), 100*after/len(POOL)))
    for i, q in enumerate(POOL):
        if game(q):
            L = [len(o[0]) for o in q["opts"]]
            print("  still %d: correct=%d runner=%d :: %s"
                  % (i, L[q["c"]], max(l for j, l in enumerate(L) if j != q["c"]), q["q"][:56]))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION at %d" % i)
