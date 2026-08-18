"""Length-bias remediation for Clinical Pathophysiology I, Lecture 2 (Dermatology).

This pool started at 83% gameable, the worst of any built so far, and the reason
is structural rather than careless: a pathophysiology answer is inherently
multi-clause -- which cell, doing what, in which layer, with what result -- while
a plausible wrong answer can be stated in six words. So the distractors have to
be brought up to the same clause structure.

Only WRONG choices are rewritten. The applier excludes the correct option from
the candidate set by construction, and every replacement stays unambiguously
false.
"""
FIXES = {
 0:  (1, "Calcitriol is produced directly in the skin under ultraviolet B light and requires no further modification in either the liver or the kidneys at all"),
 3:  (2, "Every 6 to 12 months, and considerably more rapid in older patients"),
 4:  (2, "The granular layer, known as the stratum granulosum"),
 5:  (1, "Keratohyalin granules that give the cells a rough and irregular outline when viewed on microscopy"),
 6:  (1, "The stratum basale, a single layer of rapidly dividing columnar keratinocytes at the base"),
 8:  (3, "The papillary and the subcutaneous, being the superficial and the deepest layers"),
 10: (1, "Eccrine glands sit in the axilla and anogenital areas and secrete protein and fatty lipids; apocrine glands open onto the surface of the skin and secrete water and electrolytes for cooling the body"),
 11: (1, "Water, sodium and chloride electrolytes"),
 12: (1, "Vellus hair is regulated by androgens; terminal hair grows independently of them"),
 13: (3, "A primary lesion is the one that appears first in time, and a secondary lesion is any lesion that appears later at a different site elsewhere on the body"),
 14: (1, "Size — a macule is greater than 5 millimetres and a patch is up to 5 millimetres — and both of them are readily palpable on examination"),
 15: (1, "Increased melanin production within the epidermis, as against loss of melanocytes entirely"),
 16: (3, "Focal loss of the epidermis that does not penetrate below the dermal-epidermal junction beneath it"),
 17: (3, "Dilated superficial dermal capillaries with no inflammatory infiltration at all"),
 18: (1, "By separation of the epidermis from the dermis with accumulation of fluid between them"),
 19: (1, "A vesicle is greater than 5 millimetres and a bulla is up to 5 millimetres in diameter, and the two share an identical mechanism of fluid accumulation entirely within the epidermis rather than beneath it"),
 20: (1, "Increased melanin production and cumulative ultraviolet light exposure alone"),
 21: (1, "Neutrophils release proteases that digest the collagen of the dermis, producing a depression in the surface of the skin that persists after the trigger is removed and leaves a permanent mark"),
 22: (2, "Blood deposited into the dermis from ruptured capillaries, producing a non-blanchable discoloration of the overlying skin that fades over several days as the pigment breaks down"),
 24: (1, "Dermatofibroma is a benign enclosed capsule of adipocytes; lipoma is a fibrous tissue overgrowth within the dermis"),
 25: (3, "Any lesion that arises from malignant rather than from benign underlying disease processes"),
 26: (3, "Focal loss of epidermis and dermis with destruction of the collagen beneath"),
 27: (2, "Fluid containing inflammatory cells collecting beneath the epidermis itself"),
 28: (2, "Separation of the epidermis from the dermis with accumulation of fluid between the two layers, forming a large blister that lifts the surface away"),
 29: (1, "An erosion involves both the epidermis and the dermis beneath it; an ulcer is limited to the epidermis alone and spares the dermal-epidermal junction entirely, so it never destroys collagen at all"),
 30: (1, "A superficial loss of the epidermis that spares the dermal-epidermal junction and everything beneath it, so no collagen is ever destroyed in the process of healing"),
 31: (1, "Days 4 to 21: granulation tissue forms, comprised of macrophages, fibroblasts and endothelial cells that rebuild the wound bed from below over three weeks"),
 32: (2, "Type I collagen laid down in parallel bundles, over days 21 to one year of remodelling"),
 33: (1, "Type I collagen is replaced with weaker type III collagen oriented in a basket-weave pattern throughout the scar tissue that results"),
 34: (2, "The proliferative phase, days 4 to 21, in which granulation tissue first forms in the wound"),
 35: (2, "The inflammatory phase never resolves, so granulation tissue never forms at all and the wound remains open indefinitely without ever progressing to the proliferative or remodelling phases that normally follow"),
 37: (2, "Ulcer, arising from focal loss of both the epidermis and the dermis beneath it"),
 38: (3, "An ulcer involves a loss of melanocytes from the basal layer which cannot be reversed once it has occurred in the tissue at any point afterwards"),
 39: (1, "Permanent dilatation of the superficial dermal vessels, measuring 1 to 2 millimetres across the surface of the skin"),
 40: (1, "By mechanism — petechiae from capillary rupture, purpura from vessel dilatation, and ecchymoses from melanin deposition in the dermis rather than blood"),
 41: (3, "The skin alone, with no systemic involvement whatsoever, at any age at all"),
 42: (3, "Proliferation of new vessels driven by release of vascular endothelial growth factor into the surrounding dermis over a prolonged period"),
 44: (1, "Sensitization by mast cell degranulation, followed by elicitation through the release of histamine into the surrounding dermal tissue on every subsequent exposure to that same allergen thereafter"),
 45: (2, "Irritant contact dermatitis is immunoglobulin E-mediated through mast cells, while allergic contact dermatitis is mediated by memory T cells instead of by antibodies entirely"),
 48: (3, "Dysplastic keratinocyte change arising from cumulative sun exposure over many decades of outdoor life"),
 49: (1, "A single fungal pathogen acting alone, affecting mainly the palms of the hands and the soles of the feet rather than the sebaceous areas of the skin"),
 50: (2, "A dysplastic keratinocyte proliferation driven by cumulative ultraviolet light exposure over many years of sun damage to the skin surface"),
 51: (1, "Benign proliferation of immature keratinocytes, carrying a higher risk for basal cell carcinoma of the head and neck region in later life especially"),
 52: (2, "Langerhans cells present haptens to T cells, producing a delayed hypersensitivity reaction 48 to 72 hours after each exposure to the allergen in question every single time"),
 53: (2, "Separation of the epidermis from the dermis with fluid accumulating between the two layers of the skin itself"),
 54: (1, "It infects the melanocytes that lie along the dermal-epidermal junction within the epidermis"),
 55: (1, "They invade epidermal basal cells through microabrasions and drive proliferation of the epidermis above them over time"),
 57: (3, "Increased capillary density with release of vascular endothelial growth factor into the nail bed tissue itself"),
 58: (1, "A halt of keratin production producing horizontal transverse grooves across the surface of the nail plate itself"),
 59: (1, "Overgrowth of connective tissue within the nail bed, associated with chronic liver disease and with diabetes mellitus in particular"),
 60: (1, "Overgrowth of the connective tissue within the nail bed itself over a period of time"),
 61: (1, "Increased capillary density together with vascular endothelial growth factor release into the tissue locally over time"),
 62: (1, "The tp53 tumour suppressor pathway, acting in the differentiated keratinocytes of the epidermis"),
 63: (2, "Activating mutation of fibroblast growth factor receptor-3, with a stuck-on waxy and scaly appearance on the skin"),
 64: (1, "In the reticular layer of the dermis, transformed by dysregulation of the fibroblasts that reside within it over a long period of time"),
 65: (1, "Vertical growth down into the dermis first, then radial spread within the epidermis afterwards once the tumour has thickened sufficiently to invade"),
 67: (3, "Actinic keratosis, which is by far the most common malignancy occurring in human beings"),
 68: (1, "An immediate immunoglobulin E-mediated mast cell degranulation occurring upon the very first contact with the metal"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from cp_l2_pool_a import POOL_A
    from cp_l2_pool_b import POOL_B
    from cp_l2_pool_c import POOL_C
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
            r = max(l for j, l in enumerate(L) if j != q["c"])
            print("  still %d: correct=%d runner=%d need>=%d"
                  % (i, L[q["c"]], r, max(L[q["c"]]-M+1, int(L[q["c"]]/(1+F))+1)))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION at %d" % i)
