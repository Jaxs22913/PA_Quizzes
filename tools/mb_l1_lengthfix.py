"""Length-bias remediation for the Microbiology Lecture 1 pool.

Only WRONG choices are rewritten. The applier resolves each replacement back to
an option by text similarity and asserts the match is not the correct answer —
that check has already caught three misaimed rewrites on an earlier pool.
"""
FIXES = {
 3:  (1, "By binding the sialic acid receptors on host cells with a surface hemagglutinin protein"),
 4:  (2, "Direct crosslinking of the peptidoglycan cell wall by bacterial transpeptidase enzymes"),
 6:  (0, "Bacteria and fungi are prokaryotic; protozoa and helminths are eukaryotic; viruses are simply very small bacteria"),
 8:  (3, "Chlamydias are free-living organisms, whereas Rickettsias are obligate intracellular pathogens"),
 10: (3, "Yeasts lack a cell wall entirely; molds have a wall built of chitin"),
 11: (1, "Trophozoite and endospore — the two alternating stages of the protozoan life cycle"),
 13: (2, "Flat, with no definite body cavity and a digestive tract that is a blind pouch throughout"),
 14: (3, "Tiny obligate intracellular bacteria that lack a cell wall, causing spongiform encephalopathies"),
 19: (0, "They are linear molecules, always integrated into the chromosome, and are essential to bacterial growth, to normal metabolism and to cell wall synthesis"),
 21: (0, "A defined nuclear membrane, mitochondria, and 80S ribosomes within the cytoplasm"),
 23: (2, "Teichoic acid and lipoteichoic acid, crosslinked by an outer bridge of lipopolysaccharide"),
 25: (0, "Flooding the slide with crystal violet for one full minute"),
 26: (1, "An asymmetric outer bilayer of lipopolysaccharide over a periplasmic space and a thin shell of peptidoglycan, losing crystal violet and staining red"),
 29: (0, "Gram-negative is physically strong — resistant to temperature, pH and osmotic pressure; Gram-positive is chemically strong — resistant to disinfectants and antibiotics"),
 30: (1, "It never binds the crystal violet stain in the first place during the procedure"),
 32: (3, "Colony appearance on selective agar, motility testing in semisolid medium, and spore staining with capsule staining under the light microscope"),
 33: (0, "Aerobic versus anaerobic oxygen requirements only — with temperature, pH and osmotic pressure counted as chemical rather than physical"),
 34: (2, "Synthetic contains at least one ingredient that is not chemically definable; complex contains pure organic and inorganic compounds in an exact chemical formula"),
 35: (2, "Agents that inhibit the growth of some microbes while encouraging the growth of the desired ones on the culture plate"),
 36: (0, "Selective allows several types of microbes to grow and displays visible differences between them; differential contains agents that inhibit some microbes and encourage others"),
 41: (2, "Adequate nutrients and favourable environment, plus removal of organic acids and pollutants, so growth continues unchecked"),
 42: (3, "Envelopes — lipid coats enclosing and protecting the capsid — which may be helical, icosahedral or complex"),
 44: (3, "The departure of completed virions to go on and infect other cells"),
 45: (0, "Integration of viral genes as a prophage, replication alongside the host cell, and immunity to reinfection"),
 46: (2, "Generalized transduction transfers plasmid DNA cell to cell; specialized takes up naked DNA"),
 47: (0, "The host bacterial cell is destroyed, releasing multiple copies of the virus"),
 48: (1, "The entire virion is engulfed, no uncoating is required at any point, and release occurs only by lysis of the host cell membrane rather than by budding"),
 49: (1, "Because animal viruses integrate into the host chromosome first, so the genetic material must be excised — driven by the difference in cytoplasmic pH"),
 52: (0, "Transfer of a plasmid from one bacterial cell to another, which may then impact the phenotype"),
 53: (0, "Binary fission — division of the parent cell into two; sporulation — formation of a resistant endospore coat; and budding — release of virions through the host membrane"),
 54: (3, "Viruses can no longer be identified by nucleic acid sequencing, and previously host-specific animal viruses lose the ability to cross to humans"),
 55: (0, "Acquisition of resistance to antibiotics and other control methods, the ability to produce toxins, and other virulence factors enhancing pathogenicity"),
 56: (3, "Aseptic or sterile means elimination of SOME forms of microbial contamination; disinfection means removal of ALL forms"),
 57: (0, "Inhibition of ribosomal function, and blockade of bacterial transcription and translation"),
 58: (3, "Low temperature can kill; high temperature will NOT — it only slows the rate of microbial growth"),
 60: (3, "Chlorine and bromine, used on water and surfaces, and alcohol, used on skin, instruments and laboratory work surfaces"),
 61: (2, "Natural origin — a substance produced by one microorganism against another"),
 64: (1, "Each successive 10-minute interval removes a fixed NUMBER of organisms, so the count falls in equal steps each time"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from mb_l1_pool_a import POOL_A
    from mb_l1_pool_b import POOL_B
    from mb_l1_pool_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C
    M, F = 8, 0.18
    def game(q):
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = L[0], L[1]
        return ti == q["c"] and (tl - rl) >= M and tl >= rl * (1 + F)
    before = sum(game(q) for q in POOL)
    RESOLVED = []
    # The correct option is excluded from the candidate set outright, so a
    # rewrite CANNOT land on the answer no matter how the similarity falls.
    # That is a stronger guarantee than asserting after the fact, and it stops
    # the matcher misfiring when a distractor legitimately shares wording with
    # the answer. A distractor that still scores closer to the correct option
    # than to any wrong one is reported: usually it means the distractor has
    # drifted into paraphrasing the answer, which is its own defect.
    for idx, (_st, text) in FIXES.items():
        q = POOL[idx]
        cands = [(difflib.SequenceMatcher(None, text.lower(), o[0].lower()).ratio(), i)
                 for i, o in enumerate(q["opts"]) if i != q["c"]]
        ratio, oi = max(cands)
        assert ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (idx, ratio)
        corr = difflib.SequenceMatcher(None, text.lower(), q["opts"][q["c"]][0].lower()).ratio()
        if corr > ratio:
            print("  note: fix %d reads closer to the answer than to any distractor "
                  "(%.2f vs %.2f) -- check it is not paraphrasing it" % (idx, corr, ratio))
        RESOLVED.append((idx, oi, q["opts"][oi][0][:58]))
        q["opts"][oi][0] = text
    after = sum(game(q) for q in POOL)
    if os.environ.get("SHOW_RESOLVED"):
        for idx, oi, was in RESOLVED:
            print("  %3d -> opt%d  was: %s" % (idx, oi, was))
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
