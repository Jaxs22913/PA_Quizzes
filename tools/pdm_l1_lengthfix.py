"""Length-bias remediation for Principles of Diagnostic Medicine I, Lecture 1.

The raw pool came out 50% gameable, which is unusually high and has an obvious
cause: this lecture's correct answers are enumerations ("bleeding, infection,
respiratory difficulties, perforation, and adverse effects of sedation") while
the natural distractor is a single clause. The fix is to give the distractors
the same structural register -- a multi-clause answer needs multi-clause wrong
choices -- rather than to truncate the correct one, which would lose content.

Only WRONG choices are rewritten; the applier excludes the correct option from
the candidate set by construction. Every replacement stays unambiguously false.

Keys are indices into the concatenated pool (A + B + C).
"""
FIXES = {
 # ---- pool A
 0:  (90,  "It replaces the history and physical examination once the results have been reported"),
 3:  (95,  "Compliance depends chiefly on the cost of the test and on how far the patient must travel"),
 4:  (89,  "Only the preparation instructions, since everything else is better discussed once results return"),
 5:  (88,  "It identifies which patients should be referred to another clinician before any testing begins"),
 13: (33,  "A postanalytical error of reporting"),
 15: (85,  "Assessing the patient's coping styles, fears and phobias before the procedure is scheduled"),
 16: (96,  "Arranging appropriate referrals, scheduling follow-up, and considering the patient's emotional well-being"),
 17: (105, "Only laboratory errors in the reported value, since the physical risks have passed once the test is complete"),
 18: (83,  "Repeat the test in the central laboratory before informing the patient of anything"),
 19: (72,  "Combining results from several laboratories into a single unified record"),
 21: (105, "Selecting the appropriate collection tube, observing the correct order of draw, and labeling each specimen"),
 24: (75,  "To reduce the total volume of blood that must be drawn from the patient"),
 29: (83,  "It is the tube used for trace metal studies where contamination must be avoided"),
 30: (74,  "Freeze the specimen if transport to the laboratory will be delayed beyond an hour"),
 31: (83,  "Because the laboratory requires a minimum total volume spread across three containers"),
 32: (56,  "Water from the toilet bowl, which dilutes the specimen"),
 35: (69,  "Fever with a suspicion of bloodstream infection or septicemia"),
 36: (83,  "A single large-volume sample drawn from either arm before antibiotics are started"),
 37: (85,  "They confirm the diagnosis without any need for further testing in essentially every case"),
 39: (111, "Direct antigen testing to establish the organism, followed by polymerase chain reaction for confirmation"),
 40: (94,  "Rinse the mouth with antiseptic mouthwash, then expectorate directly into the sterile container"),
 42: (77,  "Staphylococcus aureus, because of the risk of toxin-mediated illness"),
 43: (123, "Swab the soft palate and uvula only, deliberately avoiding the tonsils so that the gag reflex is not triggered"),
 44: (94,  "To collect the specimen directly from the surface of the tongue where organisms accumulate"),
 45: (67,  "Send the specimen only once the patient has become febrile"),
 46: (101, "Testing performed by a licensed clinician rather than by a laboratory technologist or technician"),
 51: (57,  "Rapid strep testing and rapid influenza antigen testing"),
 56: (56,  "It produces a numerical result without any reader device"),
 57: (180, "Handheld equipment requires a laboratory certificate and trained operators, whereas benchtop devices may be run by anyone on site without additional certification or documented competency"),
 58: (81,  "Greater precision than the equivalent central laboratory method in every case"),
 61: (76,  "Annual replacement of every device regardless of its measured performance"),
 62: (97,  "Voluntary best-practice recommendations that apply to hospital laboratories but not to other sites"),
 63: (119, "State regulation supersedes the federal standard in either direction, so a state may relax the requirement if it chooses"),
 65: (55,  "As provider-performed microscopy of a fresh specimen"),
 70: (118, "Screening is performed only after a diagnostic test has returned an abnormal result that requires further explanation"),
 71: (87,  "Typically performed in order to confirm a condition that is already strongly suspected"),
 77: (153, "A highly sensitive test costs less than a highly specific one in essentially every case, so it is the appropriate first step whenever budgets are constrained"),
 80: (25,  "Diagnostic specificity"),
 82: (101, "Neither location, because a detector with ninety-five percent specificity rarely produces a false positive"),
 83: (151, "The likelihood of the condition after the result is known, adjusted for the sensitivity and specificity of the assay that produced it"),
 84: (100, "Prevalence is how often something happens over time; incidence is how commonly it is found in a population"),
 85: (103, "Both the test characteristics and the predictive values belong to the test and travel with it between populations"),
 86: (121, "It allows the sensitivity and specificity of the test to be adjusted for that particular patient before it is ordered"),
 87: (73,  "The pre-test probability applying to the next patient who is tested"),
}

if __name__ == "__main__":
    import sys, os, difflib
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from pdm_l1_pool_a import POOL_A
    from pdm_l1_pool_b import POOL_B
    from pdm_l1_pool_c import POOL_C
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
                  % (i, L[q["c"]], max(l for j, l in enumerate(L) if j != q["c"]), q["q"][:58]))
        if len(set(o[0] for o in q["opts"])) != 4:
            print("  DUPLICATE OPTION at %d" % i)
