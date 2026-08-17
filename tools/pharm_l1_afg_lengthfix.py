"""Length-bias remediation for Pharmacology I Lecture 1, antifungals.

Same structural fix as the antibacterial pool: bring the runner-up wrong choice
up to the correct answer's clause structure rather than padding it to a
character count. Only WRONG choices are rewritten, and the applier excludes the
correct option from the candidate set by construction.
"""
FIXES = {
 0:  (1, "They are prokaryotic, with a peptidoglycan cell wall and a 70S ribosome that antibacterial agents cannot reach, and a nuclear region without a surrounding membrane"),
 2:  (2, "Recent travel, animal contact, contaminated water supply, insect bites, and crowded living conditions in institutional settings"),
 3:  (3, "A warm and moist local environment"),
 4:  (2, "Primary, opportunistic and reactivated, according to the host's immune status and whether the organism was previously encountered"),
 8:  (3, "It is converted to a fluorinated nucleotide by a fungal enzyme and then blocks thymidylate synthase, halting deoxyribonucleic acid synthesis"),
 10: (2, "They are caused by rapid fungal lysis releasing endotoxin into the circulation, and are prevented by slowing the rate of the infusion alone"),
 11: (1, "Hyperkalaemia and hypercalcaemia with a rising glomerular filtration rate, hypertension, and tubular hypertrophy that resolves without any need for hydration"),
 12: (1, "It is rapidly metabolized by hepatic cytochrome P450 enzymes before it can reach the systemic circulation"),
 13: (3, "It is actively pumped into fungal cells by a membrane transporter that is entirely absent from human cells and tissues"),
 15: (1, "Nephrotoxicity and electrolyte wasting requiring hydration with normal saline"),
 17: (2, "It inhibits squalene epoxidase in the parasite, progressively depleting the membrane of ergosterol until it loses integrity"),
 18: (1, "Squalene epoxidase, which acts early in the fungal ergosterol synthesis pathway"),
 20: (1, "It is available only intravenously and causes severe infusion reactions requiring routine premedication before every dose"),
 23: (3, "Itraconazole, with severe and often irreversible peripheral neuropathy"),
 26: (1, "Cryptococcal meningitis and prophylaxis against relapse in advanced acquired immunodeficiency syndrome"),
 28: (1, "Inhibition of lanosterol demethylase, progressively reducing ergosterol in the fungal membrane"),
 29: (1, "Cryptococcal meningitis, oral and vaginal candidiasis, and prophylaxis in advanced human immunodeficiency virus infection, together with urinary candidiasis"),
 30: (2, "Bone marrow suppression and hepatotoxicity as the principal dose-limiting effects"),
 32: (1, "Approximately one week for the scalp, one month for the fingernails, and three months for the toenails"),
 33: (1, "It must be taken on an empty stomach, since food chelates and inactivates the drug"),
 34: (1, "Inhibition of cytochrome P450 3A4, producing raised plasma levels of co-administered substrate drugs and a risk of toxicity"),
 37: (1, "It is effective against tinea unguium of the nails but against none of the other tineas"),
 38: (2, "Chromomycosis, Pseudallescheriasis and Sporotrichosis affecting the deeper skin layers"),
 41: (1, "Dermatophyte infections of the skin, hair and nails only, with no activity against any of the systemic fungal organisms"),
 42: (3, "The soil bacterium Amycolatopsis orientalis"),
 44: (2, "Terbinafine, by inhibiting squalene epoxidase early in the fungal ergosterol synthesis pathway"),
 48: (2, "Headache in about 15 percent of patients, with mental confusion and blurred vision"),
 49: (1, "They induce cytochrome P450 1A2 and 2C9, accelerating the clearance of co-administered drugs and lowering their levels"),
 56: (2, "Lanosterol demethylase, which the azole agents inhibit"),
 62: (1, "It contains peptidoglycan in a considerably thicker layer, so higher beta-lactam doses are required"),
 65: (1, "Griseofulvin targets nucleic acid synthesis; flucytosine targets cell division through microtubules"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pharm_l1_afg_pool_a import POOL_A
    from pharm_l1_afg_pool_b import POOL_B
    from pharm_l1_afg_pool_c import POOL_C
    from pharm_l1_afg_pool_d import POOL_D
    POOL = POOL_A + POOL_B + POOL_C + POOL_D
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
