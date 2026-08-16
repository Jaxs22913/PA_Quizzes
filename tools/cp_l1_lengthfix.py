"""Length-bias remediation for the Clin Path Lecture 1 pool.

Only WRONG choices are rewritten — never the correct text, never the answer
index. The applier resolves each replacement back to an option by text
similarity rather than trusting a hand-typed index, and asserts the match is
not the correct answer; on the CMS pool that check caught three rewrites aimed
at the right answer, which would have silently changed what the question tests.

Replacements add real content from the lecture's own vocabulary, so a
distractor stays a credible distractor rather than becoming padded filler.
"""
FIXES = {
 2:  (3, "Endothelial contraction, then vasodilation of the arterioles, then leukocyte transmigration into the tissue"),
 7:  (2, "Over minutes to hours only, beginning after a full 24 hours have elapsed since the injury"),
 8:  (3, "Serous exudate with low protein content, no cellular infiltrate, and no proliferation of blood vessels"),
 9:  (1, "Opsonisation of foreign material, phagocytosis by neutrophils, and enzymatic degradation"),
 12: (3, "Mucus hypersecretion accompanying inflammation of a mucous membrane surface"),
 16: (1, "Formation of a membrane-like covering over intact and otherwise viable mucosa"),
 17: (2, "Dry gangrene occurs on mucosal surfaces; wet gangrene occurs on serosal surfaces"),
 18: (1, "Granulation tissue, proliferating fibroblasts and newly formed capillary networks throughout"),
 19: (1, "Fibrinogen deposition, and preceding every other exudate pattern"),
 20: (1, "Inflammation that resolves completely versus inflammation that becomes chronic"),
 21: (0, "Neutrophils and eosinophils predominantly, without mononuclear infiltrate"),
 22: (0, "Lymphocytes phagocytose the cellular debris at the site, while macrophages produce and secrete the antibody"),
 23: (1, "A kidney-shaped nucleus that permits the cell to transmigrate between two adjacent endothelial cells nearby"),
 26: (1, "Erythrocytes, platelets and circulating plasma cells"),
 27: (1, "It lacks the enzymes needed to digest the bacterial cell wall it engulfs"),
 28: (0, "They are the predominant inflammatory cell in allergic reactions and in parasitic infection"),
 29: (1, "Kidney-shaped nucleus with abundant cytoplasm that is usually agranulated when it is viewed on light microscopy"),
 32: (3, "Fungal infection; predominating in chronic granulomatous inflammatory processes"),
 34: (1, "Returning immune function to its normal operation after infection, and preventing autoimmunity"),
 37: (0, "T helper cells and regulatory suppressor T cells"),
 38: (0, "Producing antibody directed against antigens the host has encountered previously"),
 39: (1, "A plasma cell that secretes antibody directly into the interstitium"),
 41: (3, "Restoring the immune system to its normal function once the infection has resolved"),
 46: (0, "Vasoconstriction of the arterioles"),
 47: (3, "Haemoconcentration occurring within the capillary bed"),
 48: (0, "It marks the point at which acute inflammation gives way to chronic inflammation in the tissue"),
 52: (0, "Long term, lasting at least several days, with proliferation of both blood vessels and connective tissue"),
 54: (0, "The final mediator released during the whole response, causing fibrosis and the formation of dense scar tissue at the site"),
 56: (0, "Vasoconstriction, reduced capillary permeability, and analgesia at the site"),
 57: (3, "25%; responsible for the formation of a clot at the site of the injury or lesion"),
 58: (0, "It increases capillary permeability so that circulating leukocytes are able to transmigrate into the injured tissue"),
 59: (3, "A receptor on the surface of the phagocyte that binds directly to the bacterial cell wall"),
 60: (0, "Through the complement receptors that bind to the C3b fragment"),
 61: (1, "When fibrin is degraded during healing; it then acts to prevent any further clot formation at that site"),
 62: (0, "Because sterilisation leaves residual endotoxin behind, and that endotoxin then acts as a chemotactic agent"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from cp_l1_pool_a import POOL_A
    from cp_l1_pool_b import POOL_B
    from cp_l1_pool_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C
    M_CH, M_FR = 8, 0.18
    def game(q):
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = L[0], L[1]
        return ti == q["c"] and (tl - rl) >= M_CH and tl >= rl * (1 + M_FR)
    before = sum(game(q) for q in POOL)
    for idx, (_stated, text) in FIXES.items():
        q = POOL[idx]
        ratio, oi = max((difflib.SequenceMatcher(None, text.lower(), o[0].lower()).ratio(), i)
                        for i, o in enumerate(q["opts"]))
        assert oi != q["c"], "fix %d resolves to the CORRECT option" % idx
        assert ratio > 0.45, "fix %d matches no option (%.2f)" % (idx, ratio)
        q["opts"][oi][0] = text
    after = sum(game(q) for q in POOL)
    print("gameable before: %d/%d (%.0f%%)" % (before, len(POOL), 100 * before / len(POOL)))
    print("gameable after : %d/%d (%.0f%%)" % (after, len(POOL), 100 * after / len(POOL)))
    for i, q in enumerate(POOL):
        if game(q):
            L = [len(o[0]) for o in q["opts"]]
            r = max(l for j, l in enumerate(L) if j != q["c"])
            print("  still #%d: correct=%d runner=%d need>=%d"
                  % (i, L[q["c"]], r, max(L[q["c"]] - M_CH + 1, int(L[q["c"]] / (1 + M_FR)) + 1)))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION TEXT at #%d" % i)
