"""Length-bias remediation for Physical Diagnosis 2, Lecture 2 (Dermatology).

Only WRONG choices are rewritten; the applier excludes the correct option from
the candidate set by construction, so a fix can never land on the answer. Each
replacement is a structural match for the correct option — a multi-clause answer
gets multi-clause distractors — and stays unambiguously false.

Keys are indices into the concatenated pool (A + B + C).
"""
FIXES = {
 # pool A
 1:   (32, "The apocrine (scent) gland"),
 4:   (132, "The patient's age, occupation, marital status and insurance carrier, recorded in full before the skin complaint is discussed"),
 5:   (151, "Recent insect bites, any recorded allergy to an antibiotic, and whether the patient wears gloves at work or handles chemicals at home"),
 12:  (79, "Nutritional status, measured through serum albumin and prealbumin levels"),
 13:  (81, "It may be recorded as the diagnosis in its own right whenever no rash is visible"),
 14:  (93, "Contact dermatitis, scabies and other infestations, to the exclusion of systemic disease"),
 16:  (75, "A dermatoscope, a Wood's lamp, and sterile swabs for any open lesion"),
 18:  (134, "It prevents contamination of the patient's clothing and keeps the examination table clean between successive patients"),
 # pool B
 30:  (129, "A primary lesion is larger than one centimetre in diameter, while a secondary lesion is anything smaller than that"),
 39:  (24, "Annular (a single ring)"),
 50:  (68, "A nodule is filled with fluid, whereas a papule is a solid elevation"),
 57:  (27, "A macule, patch or freckle"),
 58:  (123, "An erosion is always linear in shape, whereas an ulcer is round or oval and has a clearly defined raised margin"),
 63:  (94, "A keloid is thin and white in appearance, while a hypertrophic scar is thick and pink"),
 67:  (141, "A corn is the larger of the two lesions and lies over the ball or the heel of the foot, where the body's weight is chiefly borne"),
 # pool C
 80:  (57, "Partial loss of the epidermis, leaving a moist base"),
 92:  (68, "E for erythema, F for friability, and G for a granular surface"),
 94:  (59, "Confined to the sun-exposed areas of the face and neck"),
 95:  (146, "Terminal hair is the short, fine hair that covers the body, while vellus hair is the coarse hair of the scalp, axillae and beard"),
 96:  (69, "Texture by inspection; colour, distribution and quantity by palpation"),
 100: (71, "Diffuse thinning of the scalp hair in women following the menopause"),
 109: (121, "A splinter hemorrhage is painful to the touch, whereas a subungual hematoma causes the patient no discomfort"),
 113: (86, "Capillary refill time, nail bed temperature and the presence of peripheral cyanosis"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pd2_l2_pool_a import POOL_A
    from pd2_l2_pool_b import POOL_B
    from pd2_l2_pool_c import POOL_C
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
    after = sum(game(q) for q in POOL)
    print("gameable before: %d/%d (%.0f%%)" % (before, len(POOL), 100*before/len(POOL)))
    print("gameable after : %d/%d (%.0f%%)" % (after, len(POOL), 100*after/len(POOL)))
    for i, q in enumerate(POOL):
        if game(q):
            L = [len(o[0]) for o in q["opts"]]
            print("  still %d: correct=%d runner=%d :: %s"
                  % (i, L[q["c"]], max(l for j, l in enumerate(L) if j != q["c"]), q["q"][:60]))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION at %d" % i)
