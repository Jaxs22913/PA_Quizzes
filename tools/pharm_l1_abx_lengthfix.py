"""Length-bias remediation for Pharmacology I Lecture 1, antibacterials.

This deck is enumerative in the same way Microbiology Lecture 2 was -- correct
answers are lists of indications or two-part mechanisms, while the distractors
came out as single short phrases. The fix is STRUCTURAL: a three-part answer
needs three-part distractors. Padding a short phrase to a character count does
not work and stalls the rate around 40%.

Only WRONG choices are rewritten. The applier excludes the correct option from
the candidate set by construction, so a rewrite cannot land on the answer.
Every replacement must stay unambiguously false.
"""
FIXES = {
 3:  (1, "In concentration-dependent killing the drug must be given by continuous infusion to hold a steady level; in time-dependent killing a single large daily dose is preferred because the post-antibiotic effect carries the interval"),
 4:  (2, "A loading dose followed by widely spaced maintenance doses, with the interval guided by trough levels alone rather than by time above the minimal inhibitory concentration"),
 5:  (1, "Cardiac, pulmonary, endocrine, musculoskeletal, ocular, and dermatologic systems"),
 6:  (1, "The beta-lactam ring chelates the magnesium ion required by the cross-linking enzyme, reversibly inhibiting it until the metal is replaced"),
 11: (2, "Pseudomonas aeruginosa pneumonia, nosocomial intra-abdominal infection, and polymicrobial infection in the critically ill patient"),
 12: (1, "Induction of hepatic cytochrome P450 enzymes accelerates estrogen metabolism, lowering circulating hormone levels below the contraceptive threshold"),
 19: (2, "Clostridium difficile colitis, intra-abdominal abscess, and pseudomembranous colitis"),
 23: (1, "Community-acquired pneumonia managed in the outpatient setting, uncomplicated sinusitis, and acute otitis media in a child"),
 27: (3, "Activity is unchanged across the generations; the generations differ only in half-life and dosing interval, so the choice between them is a matter of convenience"),
 30: (1, "Excellent Gram-negative activity including Pseudomonas aeruginosa, with limited Gram-positive coverage and reliable activity against Enterococcus"),
 31:  (3, "Complicated intra-abdominal infection with Bacteroides fragilis, anaerobic abscess and biliary sepsis"),
 35: (1, "Community-acquired pneumonia and skin and soft tissue infection in the outpatient setting, together with uncomplicated urinary tract infection"),
 41:  (1, "Methicillin-resistant Staphylococcus aureus bacteraemia, infective endocarditis, vertebral osteomyelitis, and prosthetic joint infection"),
 44: (1, "It inactivates the penicillin-binding protein by forming a covalent bond at its active site, exactly as a penicillin does"),
 45: (1, "Pseudomonal pneumonia, multidrug-resistant Gram-negative infection, extended-spectrum beta-lactamase producing organisms, and nosocomial intra-abdominal sepsis"),
 46: (1, "Oral vancomycin is absorbed too rapidly from the small bowel and produces toxic serum concentrations before reaching the colon"),
 48: (3, "At any point within the dosing interval, provided the exact time of the draw is recorded"),
 50: (2, "Switch to the oral route to raise gut concentrations, since the failure reflects poor luminal delivery rather than reduced susceptibility"),
 51: (1, "It inhibits protein synthesis at the 50S ribosomal subunit, and it cannot be used in renal failure"),
 54: (3, "Mammalian mitochondria use a 90S ribosome that binds these drugs preferentially at therapeutic levels"),
 56:  (1, "Pseudomonas aeruginosa, Acinetobacter species, Burkholderia cepacia and Stenotrophomonas maltophilia"),
 57:  (2, "Hypertensive crisis and hyperpyrexia, increased by tyramine-containing foods, sympathomimetics and serotonergic agents"),
 58: (1, "They induce CYP3A subclass enzymes, lowering levels of substrates such as carbamazepine, cyclosporine, digoxin, midazolam and theophylline, with azithromycin greater than clarithromycin greater than erythromycin"),
 60: (3, "Forming channels within the cell membrane that allow potassium and magnesium to leak out of the cell"),
 61:  (1, "Pseudomonas aeruginosa, Clostridium difficile, Enterococcus faecium and Acinetobacter baumannii"),
 63:  (2, "Kernicterus from bilirubin displacement — avoid in the first 30 days of life and throughout the third trimester of pregnancy"),
 64:  (1, "Uncomplicated urinary tract infection, outpatient sinusitis, acute uncomplicated cystitis in a non-pregnant adult, and community-acquired pneumonia managed in the outpatient setting"),
 66: (1, "They show time-dependent killing, so a longer interval keeps the level above the minimal inhibitory concentration for a greater share of the dosing period"),
 68: (3, "Serotonin syndrome, hypertensive crisis, and thrombocytopenia"),
 69: (1, "Pseudomonal and multidrug-resistant Gram-negative infection; it covers no Gram-positive organisms and no atypicals"),
 70: (3, "Ethanol, which produces a disulfiram-like reaction with flushing and vomiting"),
 71: (2, "Sulfamethoxazole inhibits dihydrofolate reductase and blocks conversion of dihydrofolic acid to tetrahydrofolic acid; trimethoprim inhibits tetrahydropteroic acid synthetase upstream of it"),
 74:  (1, "Ototoxicity and nephrotoxicity, requiring trough monitoring, renal dose adjustment, and baseline audiometry before each course of therapy"),
 75: (2, "Permanent loss of Gram-positive coverage across the entire class"),
 76:  (1, "Gram-negative aerobes including Pseudomonas aeruginosa, plus Gram-negative anaerobes, with no Gram-positive aerobic or anaerobic activity of any kind at all"),
 77:  (3, "A disulfiram-like reaction on exposure to ethanol, with flushing, vomiting and tachycardia"),
 78:  (3, "Bacterial meningitis, cerebral abscess and ventriculitis requiring reliable central nervous system penetration, together with neurosurgical prophylaxis after craniotomy"),
 79: (2, "Sulfamethoxazole inhibits the conversion of dihydrofolic acid to tetrahydrofolic acid via dihydrofolate reductase; trimethoprim inhibits the conversion of para-aminobenzoic acid to dihydrofolic acid via tetrahydropteroic acid synthetase"),
 82: (2, "It binds the 50S ribosomal subunit and blocks the transpeptidation step of protein synthesis"),
 85:  (2, "Binding the 30S ribosomal subunit and preventing transfer RNA from occupying the A site of the bacterial ribosome during chain elongation and protein assembly"),
 86: (1, "The mechanism is impossible for bacteria to circumvent, and newer formulations have removed the nephrotoxicity and neurotoxicity entirely"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pharm_l1_abx_pool_a import POOL_A
    from pharm_l1_abx_pool_b import POOL_B
    from pharm_l1_abx_pool_c import POOL_C
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
