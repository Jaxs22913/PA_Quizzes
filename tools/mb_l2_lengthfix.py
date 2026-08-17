"""Length-bias remediation for Microbiology Lecture 2.

This deck is enumerative — most correct answers are lists — so the fix is
STRUCTURAL: a three-part answer gets three-part distractors. Padding a short
phrase cannot catch a list, which is what stalled the Lecture 1 pass at 40%.

Only wrong choices are rewritten. The applier excludes the correct option from
the candidate set by construction, so a rewrite cannot land on the answer.
"""
FIXES = {
 0:  (2, "Any synthetic compound that kills harmful bacteria without damaging the host tissue"),
 2:  (0, "Penicillin, from mouldy bread stored alongside the remains in the burial chambers"),
 3:  (1, "That Streptomyces species produce antibiotics, work which yielded streptomycin and over twenty further agents isolated from common soil organisms"),
 4:  (3, "That Streptomyces produced over twenty antibiotics; Selman Waksman commercialised them, coined the term antibiotic, and won the Nobel prize in 1952"),
 7:  (0, "Bactericidal inhibits growth, measured by the minimal bactericidal concentration (the level inhibiting 99.9% of test organisms); bacteriostatic kills organisms directly, measured by the minimal inhibitory concentration"),
 9:  (0, "Killing every microbe present in the sample; normally achieved by raising the dose above the upper limit of the therapeutic window until no organism survives"),
 11: (2, "The number of distinct resistance mechanisms a drug is able to overcome in practice"),
 12: (0, "Because eukaryotic pathogens replicate considerably faster than bacteria do, so they outpace the drug before an effective concentration is reached"),
 14: (1, "Minimal inhibitory concentration divided by minimal bactericidal concentration, equivalently the trough over the peak plasma level"),
 15: (3, "Drug A is less likely to select for resistant organisms over the course of a full therapeutic regimen"),
 16: (2, "The proportion of an administered dose that reaches the systemic circulation intact"),
 17: (0, "Doses should be spaced as widely apart as the patient will tolerate, since the drug persists in tissue long after the plasma level falls"),
 18: (0, "The zone diameter in millimetres, corrected for the molecular weight and diffusion rate of the agent tested"),
 19: (1, "Renal clearance, hepatic clearance, and clearance from all other tissues"),
 21: (0, "It prevents peptidoglycan monomers from being transported across the cell membrane"),
 22: (0, "Carbapenems have a single ring; monobactams substitute a carbon for a sulphur and add a double bond"),
 23: (0, "Streptomyces griseus; first generation broad spectrum and Gram-negative, second narrowed to Gram-positive, third oral, fourth injected against pseudomonads"),
 24: (1, "Amycolatopsis orientalis; a polyene that binds ergosterol in the fungal membrane and forms pores through it, causing leakage of cell contents, which is why it is too toxic for routine systemic use"),
 25: (2, "Paenibacillus polymyxa; a polypeptide that disrupts the outer membrane by attaching directly to its lipid components"),
 26: (1, "Isoniazid inhibits DNA gyrase; ethambutol inhibits bacterial RNA polymerase"),
 29: (0, "Chloramphenicol changes the shape of the 30S ribosomal subunit; erythromycin blocks the attachment of transfer RNA to the ribosome entirely"),
 30: (3, "Inhibit folic acid synthesis because their structure closely resembles that of para-aminobenzoic acid"),
 31: (0, "Inhibiting bacterial RNA polymerase and so preventing transcription; used chiefly against tuberculosis and other mycobacterial infections, always in combination with a second agent to limit resistance"),
 32: (3, "Binding the penicillin-binding proteins on the cell membrane; used mainly against Gram-positive organisms and some anaerobes"),
 33: (3, "They prevent peptidoglycan monomer transport across the cell membrane; naturally produced antibiotics, isolated from Bacillus subtilis in 1945"),
 34: (0, "Blocking the synthesis of beta-glucan, an essential structural component of the fungal cell wall, and so weakening it until the cell lyses"),
 35: (2, "Echinocandins are reserved for azole-resistant infections; azoles are the agents typically given by the intravenous route in serious systemic disease"),
 36: (1, "Griseofulvin binds ergosterol within the fungal membrane and forms pores; tolnaftate blocks the synthesis of beta-glucan in the fungal cell wall"),
 37: (0, "Damaging the parasite's DNA through the formation of cytotoxic free radicals inside the cell"),
 38: (0, "Praziquantel prevents ATP generation (tapeworms); niclosamide alters membrane permeability (flatworms)"),
 39: (1, "An integrase inhibitor preventing viral genes from entering the host chromosome after reverse transcription"),
 40: (1, "They block the proteolytic cleavage of viral polypeptide precursors into mature proteins"),
 42: (3, "It inhibits neuraminidase and so stops viral escape from the host cell; adding polyethylene glycol prolongs the half-life with no accompanying disadvantage"),
 43: (1, "The failure of a drug to reach the target site at an effective concentration, whether through poor absorption, rapid clearance or barriers to distribution"),
 44: (0, "Antibiotics actively mutate bacterial DNA on contact, and the mutations that result then spread through the population by conjugation and transduction"),
 45: (3, "Spontaneous loss of the resistance plasmid during binary fission"),
 46: (1, "A plasmid carrying the resistance gene is passed directly between two cells during conjugation"),
 48: (3, "Modification of the target site"),
 49: (3, "The drug is inherently bacteriostatic rather than bactericidal, so it slows the organism without ever clearing it from the host"),
 50: (0, "By raising the metabolic rate of the organisms inside them so they divide faster than the drug can act, by physically excluding immune cells from the surface, and by preventing any transfer of resistance genes between the organisms held within"),
 51: (1, "The six antibiotic classes most often rendered useless by beta-lactamase enzymes — penicillins, cephalosporins, monobactams, carbapenems, glycopeptides and macrolides — which together account for most treatment failure in hospital-acquired infection worldwide"),
 52: (2, "Using a narrow spectrum agent once the causative organism is known"),
 53: (1, "Combining two antibiotics that act antagonistically, so that the effect of the pair is less than either agent alone would have achieved against the organism"),
 54: (0, "Only hospital-acquired infections, through the Centers for Disease Control and Prevention alone, with data drawn from inpatient isolates and reported annually to state health departments for regional comparison"),
 55: (2, "Soil acidification, heavy metal contamination of groundwater, and progressive loss of environmental microbial diversity"),
 57: (0, "An infection with two organisms simultaneously, triggered by mixed exposure during a single episode of care within a healthcare facility"),
 58: (0, "Streptococcus pyogenes, Neisseria meningitidis, Haemophilus influenzae, Streptococcus pneumoniae and Moraxella catarrhalis"),
 61: (1, "Oesophageal ulcerations following oral dosing without water"),
 62: (2, "Tetracyclines and aminoglycosides; reactions may be immediate or delayed, ranging from photosensitivity through to permanent tooth discoloration"),
 63: (1, "Additive effects, in which the two simply sum; multiplicative effects, in which each amplifies the other; and subtractive effects between the agents"),
 65: (3, "They sequester the iron that a pathogen requires for its metabolism; example, diiodohydroxyquinoline used in amoebic disease"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from mb_l2_pool_a import POOL_A
    from mb_l2_pool_b import POOL_B
    from mb_l2_pool_c import POOL_C
    POOL = POOL_A + POOL_B + POOL_C
    M, F = 8, 0.18
    def game(q):
        L = sorted(((len(o[0]), i) for i, o in enumerate(q["opts"])), reverse=True)
        (tl, ti), (rl, _) = L[0], L[1]
        return ti == q["c"] and (tl - rl) >= M and tl >= rl * (1 + F)
    before = sum(game(q) for q in POOL)
    for idx, (_st, text) in FIXES.items():
        q = POOL[idx]
        ratio, oi = max((difflib.SequenceMatcher(None, text.lower(), o[0].lower()).ratio(), i)
                        for i, o in enumerate(q["opts"]) if i != q["c"])
        assert ratio > 0.22, "fix %d matches no wrong option (%.2f)" % (idx, ratio)
        corr = difflib.SequenceMatcher(None, text.lower(), q["opts"][q["c"]][0].lower()).ratio()
        if corr > ratio:
            print("  note: fix %d reads closer to the answer than to any distractor (%.2f vs %.2f)"
                  % (idx, corr, ratio))
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
