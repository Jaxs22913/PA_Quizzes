#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 2 and Lecture 3 topics to the Pharmacology I Exam 1 cram sheet.

Same colour-coded topic/table structure as the Lecture 1 sections: the guide
carries the explanation, this carries only what has to be recallable cold.

WEIGHTED TO WHAT THE COURSE ASKED FOR. Dr. McInnis told the class on 28 August
that mechanism is over-studied and to work on indications, patient education,
side effects and contraindications. So the rows here lean that way, and the
mechanism rows that survive are the ones that DISCRIMINATE between two agents
rather than the ones that merely describe one.

NO DOSES, per Dr. Wood. Concentrations and milligram figures are left out
entirely; where a number appears it is a duration, a threshold or a counselling
point ("no longer than three days"), never a dose to recall.

Idempotent -- existing sections with these ids are stripped before re-adding.
"""
import os, re, sys, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Pharmacology I Exam 1",
                    "pharm-exam-1-cram-sheet.html")

RUST, COPPER, GOLD = "#6b3524", "#9c5230", "#c9a227"

TOPICS = [
 ("l2-vehicles", "L2 · Vehicles & Penetration", COPPER, "#efe6e0", "#f8f3ef", "#5e3320", [
   ("More permeable sites", "SCROTUM · FACE · AXILLA · SCALP. The same tube does different things in different places."),
   ("Drying range", "TINCTURES most drying → wet dressings → lotions → gels → aerosols → powders → pastes → creams → foams → OINTMENTS least drying."),
   ("Match vehicle to lesion", "OOZING, VESICULATION, CRUSTING → drying end. SCALING, LICHENIFICATION, XEROSIS → least drying end."),
   ("Two site rules", "AVOID OINTMENT in intertriginous areas. GEL or FOAM for scalp and hairy locations — foams well, low residue."),
   ("Depot effect", "Skin acts as a RESERVOIR, which may permit ONCE DAILY dosing of a short acting drug."),
   ("Occlusion", "Increases efficacy — and the lecture raises TOXICITY in the same breath."),
   ("Concentration gradient", "More concentration means more transfer. Worked example: CORTICOSTEROID RESISTANCE overcome by raising concentration."),
 ]),
 ("l2-acne", "L2 · Acne — Factors and Drugs", RUST, "#eae3e0", "#f5f1f0", "#53291c", [
   ("Four major factors", "INCREASED SEBUM · ALTERED KERATINIZATION with ductal hyperproliferation · BACTERIAL COLONIZATION (P. acnes) · INFLAMMATORY MEDIATORS."),
   ("Critical target", "The MICROCOMEDONE. Eliminating follicular occlusion arrests the cascade."),
   ("Lesion split", "NONINFLAMMATORY = open and closed comedones. INFLAMMATORY = papulopustular and nodular."),
   ("Route by severity", "MILD–MODERATE topical. MODERATE–SEVERE systemic."),
   ("Benzoyl peroxide", "Crosses stratum corneum UNCHANGED, converts to BENZOIC ACID. Counsel: BLEACHES hair, clothing, bedding."),
   ("Topical retinoid", "FIRST LINE for comedonal acne. AVOID IN PREGNANCY. Tretinoin is PHOTOLABILE — apply at night."),
   ("The interaction", "BENZOYL PEROXIDE INACTIVATES TRETINOIN. Adapalene is the one stable in sunlight AND with benzoyl peroxide."),
   ("Retinoid branches", "TAZAROTENE acne + psoriasis · ALITRETINOIN Kaposi sarcoma · BEXAROTENE T-cell lymphoma."),
   ("Topical antibiotic", "CLINDAMYCIN preferred. Erythromycin losing efficacy to P. acnes RESISTANCE."),
   ("Isotretinoin", "CONTRAINDICATED in pregnancy and breastfeeding; iPledge. Raised SERUM LIPIDS. MONITOR FOR DEPRESSION."),
   ("Tetracyclines", "Chelate CALCIUM, blocking neutrophil and monocyte CHEMOTAXIS. CONTRAINDICATED under 8 years and in pregnancy."),
   ("Azelaic acid", "Give it SIX TO EIGHT WEEKS. Can cause HYPOPIGMENTATION."),
   ("Drug-induced acne", "SYSTEMIC CORTICOSTEROIDS (not hydrocortisone) · antiepileptics · tuberculostatics · lithium. Withdrawal causes an INITIAL WORSENING."),
 ]),
 ("l2-eczema", "L2 · Atopic Dermatitis & Steroids", GOLD, "#f2ecd9", "#faf7ec", "#6b5410", [
   ("Atopic triad", "Atopic dermatitis + ASTHMA + ALLERGIC RHINO-CONJUNCTIVITIS. SKIN BARRIER DYSFUNCTION plays the major role."),
   ("Major indicators", "PRURITUS · rash in TYPICAL AREAS · CHRONIC or repeated · FAMILY HISTORY. (Raised IgE and skin tests are MINOR.)"),
   ("Gold standard", "TOPICAL CORTICOSTEROIDS, chosen by severity and SITE."),
   ("Potency by site", "LOW for face, intertriginous areas, infants — and better long term. MEDIUM for body. Exacerbation: MEDIUM–HIGH for one to two weeks then STEP DOWN."),
   ("What drives adverse effects", "POTENCY · DURATION · AREA COVERED · OCCLUSIVENESS (ointment > cream > lotion)."),
   ("Local vs systemic", "LOCAL: skin atrophy, acne, rosacea, allergic dermatitis to the vehicle. SYSTEMIC: adrenal suppression, infections, hyperglycaemia, GLAUCOMA, CATARACTS, growth retardation in children."),
   ("Immunomodulators", "TACROLIMUS, PIMECROLIMUS inhibit T cell, mast cell and keratinocyte activation. SECOND LINE. Possible cancer risk; avoid if immunosuppressed. Counsel BURNING and HIGH SPF."),
   ("Oral steroid course", "Needs a TAPER to prevent a flare-up."),
 ]),
 ("l2-topicals", "L2 · Topical Anti-infectives", COPPER, "#efe6e0", "#f8f3ef", "#5e3320", [
   ("Bacitracin", "Prevents CELL WALL synthesis. Gram positives. NO SYSTEMIC TOXICITY."),
   ("Mupirocin", "Binds bacterial TRANSFER RNA. MRSA. Eliminates NASAL CARRIAGE of S. aureus."),
   ("Polymyxin B", "Interrupts CYTOPLASMIC MEMBRANE. Gram negatives. AVOID high dose on OPEN or DENUDED skin — neuro- and nephrotoxicity."),
   ("Neomycin", "Frequently causes SENSITISATION. Class can accumulate systemically."),
   ("Azoles", "Inhibit FUNGAL P450, preventing cell wall formation. Treatment is PROLONGED, two to three weeks."),
   ("Ciclopirox nail lacquer", "LESS THAN 12% EFFECTIVE for onychomycosis. Say so before starting."),
   ("Allylamines", "NAFTIFINE, TERBINAFINE — inhibit ERGOSTEROL production."),
   ("Coverage gaps", "TOLNAFTATE has NO CANDIDA activity. NYSTATIN is the candidal agent, NO ORAL ABSORPTION."),
   ("Topical antivirals", "ACYCLOVIR, PENCICLOVIR — guanine analogues, recurrent OROLABIAL herpes simplex."),
   ("Imiquimod", "Immunomodulator — warts, ACTINIC KERATOSES, BASAL CELL CARCINOMA. Irritation in VIRTUALLY ALL patients, and the DEGREE OF INFLAMMATION PARALLELS EFFICACY."),
 ]),
 ("l3-wiring", "L3 · ANS Wiring & Receptors", RUST, "#eae3e0", "#f5f1f0", "#53291c", [
   ("The tree", "Nervous system → CENTRAL / PERIPHERAL. Peripheral → AFFERENT / EFFERENT. Efferent → SOMATIC / AUTONOMIC. Autonomic → ENTERIC, PARASYMPATHETIC, SYMPATHETIC."),
   ("Autonomic vs somatic", "Autonomic is TWO NEURONS — PREGANGLIONIC within the CNS, POSTGANGLIONIC from a ganglion, generally NONMYELINATED. The somatic route does not relay that way."),
   ("Enteric", "The BRAIN OF THE GUT — gut, pancreas, gallbladder. FUNCTIONS INDEPENDENTLY of the CNS, modulated by the other two."),
   ("Cholinergic steps", "SIX: synthesis · storage · release · receptor binding · DEGRADATION by acetylcholinesterase · RECYCLING of choline. (Adrenergic has FIVE.)"),
   ("Muscarinic subtypes", "Five subclasses, ONLY M1, M2, M3 functionally characterised. M1 neurons + gastric parietal · M2 neurons + CARDIAC + smooth muscle · M3 neurons + BLADDER + exocrine glands."),
   ("Nicotinic receptor", "FIVE SUBUNITS, LIGAND-GATED ION CHANNEL. TWO acetylcholine molecules open it to sodium. CNS, adrenal medulla, ganglia, neuromuscular junction."),
   ("Nicotine's twist", "STIMULATES at low concentration, BLOCKS at high."),
   ("Alpha vs beta location", "ALPHA-1 POSTSYNAPTIC on the effector organ. ALPHA-2 PRESYNAPTIC on nerve endings."),
   ("Potency orders", "ALPHA: epinephrine ≥ norepinephrine >> isoproterenol. BETA: isoproterenol > epinephrine > norepinephrine."),
   ("Catecholamine breakdown", "COMT postsynaptically, MAO within the neuron. Noncatecholamines escape both — longer acting, more CNS penetration."),
 ]),
 ("l3-effects", "L3 · Predicting Effects", GOLD, "#f2ecd9", "#faf7ec", "#6b5410", [
   ("Muscarinic — DUMBBELS", "Defecation · Urination · Miosis · Bradycardia · Bronchorrhoea · Bronchospasm · Emesis · Lacrimation · Salivation."),
   ("Nicotinic — MTWHF", "Mydriasis · Tachycardia · Weakness · Hypertension · Fasciculations."),
   ("Anticholinergic", "Mad as a hatter · Blind as a bat · Red as a beet · Dry as a bone · Hot as Hades. Plus constipation, urinary retention, TACHYCARDIA."),
   ("How to tell them apart", "PUPIL AND HEART FIRST: muscarinic is SMALL pupil, SLOW heart. Nicotinic and anticholinergic are both BIG pupil, FAST heart. Then WET vs DRY separates those two."),
   ("Ganglionic blockade", "Blocks the ENTIRE autonomic output at nicotinic receptors. Vasodilation, plus atony of bladder and gut, cycloplegia, xerostomia, tachycardia."),
 ]),
 ("l3-chol", "L3 · Cholinergic Drugs", COPPER, "#efe6e0", "#f8f3ef", "#5e3320", [
   ("Direct vs indirect", "DIRECT bind the receptor (choline esters, pilocarpine). INDIRECT = ANTICHOLINESTERASES, raising acetylcholine."),
   ("Bethanechol", "Resists acetylcholinesterase, MUSCARINIC ONLY. Stimulates DETRUSOR, relaxes trigone and sphincter → urinary retention."),
   ("Pilocarpine", "Miosis + ciliary contraction → GLAUCOMA. Also XEROSTOMIA."),
   ("Edrophonium vs pyridostigmine", "EDROPHONIUM short acting — DIAGNOSING myasthenia gravis. PYRIDOSTIGMINE — CHRONIC MANAGEMENT."),
   ("Physostigmine", "ENTERS THE BRAIN. Antidote for ANTICHOLINERGIC OVERDOSE."),
   ("Neostigmine", "Does NOT enter the brain. Bladder and gut, reversing blockade, myasthenia gravis."),
   ("Alzheimer agents", "DONEPEZIL · RIVASTIGMINE · GALANTAMINE. Deficiency of CENTRAL cholinergic neurons."),
   ("Poisoning, both ways", "INSECTICIDE (anticholinesterase) → ATROPINE + PRALIDOXIME. ANTICHOLINERGIC overdose → PHYSOSTIGMINE. Getting the direction wrong doubles the poisoning."),
   ("Pralidoxime limits", "Does NOT enter the brain. CANNOT overcome reversible inhibitors such as physostigmine."),
   ("Atropine", "Persistent MYDRIASIS + CYCLOPLEGIA. BRADYCARDIA at low dose, TACHYCARDIA at higher. Greatest inhibition on bronchial tissue, sweat, saliva."),
   ("Scopolamine", "Greater CENTRAL action — MOTION SICKNESS, blocks SHORT-TERM MEMORY. Patch: WASH HANDS or you blur your vision."),
   ("Synthetic antimuscarinics", "IPRATROPIUM, TIOTROPIUM inhaled for COPD · GLYCOPYRROLATE secretions and drooling · bladder agents lower pressure and raise capacity."),
   ("Neuromuscular blockade", "NONDEPOLARIZING is COMPETITIVE — MORE ACETYLCHOLINE REVERSES IT. Face and eye first, DIAPHRAGM LAST, recovery in reverse."),
   ("Succinylcholine", "The ONLY depolarizing agent. Acts LIKE acetylcholine and is not destroyed — an anticholinesterase makes it WORSE. Risk: MALIGNANT HYPERTHERMIA with halothane → COOLING + DANTROLENE."),
 ]),
 ("l3-adren", "L3 · Adrenergic Drugs", RUST, "#eae3e0", "#f5f1f0", "#53291c", [
   ("Epinephrine by dose", "BETA effects at LOW dose, ALPHA at HIGH. Raises SYSTOLIC, lowers DIASTOLIC."),
   ("Epinephrine uses", "ANAPHYLAXIS · CARDIAC ARREST · acute bronchospasm. In local anaesthetic to PROLONG the block by vasoconstriction."),
   ("Epinephrine + beta blocker", "ALPHA EFFECTS LEFT UNOPPOSED → peripheral resistance and blood pressure RISE."),
   ("Norepinephrine", "Mostly ALPHA. REFLEX BRADYCARDIA via baroreceptor. EXTRAVASATION → PHENTOLAMINE."),
   ("Dopamine", "Beta-1 cardiac · dopaminergic dilates RENAL and SPLANCHNIC · alpha-1 vasoconstriction only at VERY HIGH dose. Cardiogenic and septic shock."),
   ("Dobutamine", "Selective BETA-1. Acute heart failure. BARELY RAISES MYOCARDIAL OXYGEN DEMAND. Caution in ATRIAL FIBRILLATION."),
   ("Alpha-1 vs alpha-2 agonist", "PHENYLEPHRINE alpha-1 → vasoconstriction, REFLEX BRADYCARDIA. CLONIDINE alpha-2 → reduces CENTRAL SYMPATHETIC OUTFLOW."),
   ("Two rebound warnings", "OXYMETAZOLINE longer than THREE DAYS → rebound congestion. CLONIDINE stopped abruptly → REBOUND HYPERTENSION."),
   ("Indirect agonists", "AMPHETAMINE · COCAINE · TYRAMINE — release norepinephrine or block reuptake. EPHEDRINE and PSEUDOEPHEDRINE are MIXED."),
   ("Tyramine trap", "Normally destroyed by MAO IN THE GUT. On an MAO INHIBITOR it reaches the terminal — serious vasopressor effect. Fermented cheese and wine."),
   ("Phenoxybenzamine", "IRREVERSIBLE, noncompetitive — needs NEW RECEPTORS, at least a day. EPINEPHRINE REVERSAL: vasoconstriction blocked, vasodilation left."),
   ("Alpha-1 blockers split", "PRAZOSIN, TERAZOSIN, DOXAZOSIN for hypertension. TAMSULOSIN, ALFUZOSIN for BPH. Signature: FIRST-DOSE SYNCOPE."),
   ("Propranolol", "Nonselective → BRONCHOCONSTRICTION, CONTRAINDICATED in asthma and COPD. MASKS HYPOGLYCAEMIA. Abrupt stop → arrhythmia from RECEPTOR UP-REGULATION."),
   ("Propranolol beyond BP", "MIGRAINE PREVENTION · HYPERTHYROIDISM · ANGINA · after MYOCARDIAL INFARCTION."),
   ("The rest by property", "TIMOLOL glaucoma · SELECTIVE BETA-1 lose selectivity at higher doses · ACEBUTOLOL and PINDOLOL have ISA · LABETALOL IV for hypertensive emergency · CARVEDILOL mortality in heart failure."),
   ("Storage agents", "RESERPINE blocks uptake INTO vesicles. GUANETHIDINE blocks release FROM them."),
 ]),
]


def section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
        for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def main():
    s = open(CRAM, encoding="utf-8").read()
    for tid in [t[0] for t in TOPICS]:
        s = re.sub(r'\n  <section class="topic" id="%s".*?\n  </section>\n' % re.escape(tid),
                   "", s, flags=re.S)
        s = re.sub(r'      <a href="#%s"[^\n]*\n' % re.escape(tid), "", s)

    last = s.rindex('<section class="topic"')
    end = s.index("\n  </section>", last) + len("\n  </section>\n")
    # the jump links live in <div class="toc">, not a <nav> as they do on the
    # PDM sheet this pattern came from
    toc_start = s.index('<div class="toc">')
    toc_end = s.index("</div>", toc_start)
    links_anchor = s.rindex("</a>\n", toc_start, toc_end) + len("</a>\n")

    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], H.escape(t[1])) for t in TOPICS)
    s = s[:end] + "".join(section(t) for t in TOPICS) + s[end:]
    s = s[:links_anchor] + links + s[links_anchor:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th", "div"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling
    assert "**" not in s, "markdown emphasis left in a cram row"

    order = re.findall(r'<section class="topic" id="([^"]+)"', s)
    assert order.index("principles") < order.index("l2-vehicles") < order.index("l3-wiring"), \
        "lectures must stay in syllabus order"

    # Dr. Wood: no dosages. A row whose content is essentially a milligram figure
    # or a percentage strength should never have been written.
    for t in TOPICS:
        for label, text in t[6]:
            assert not re.search(r"\b\d+(\.\d+)?\s*(mg|g|mcg|units)\b", text, re.I), \
                "dose in a cram row: %r" % label
            # A percentage is only a problem when it is a drug STRENGTH. An
            # efficacy figure ("less than 12% effective") is a counselling point
            # and is exactly what Dr. McInnis asked to be emphasised -- the same
            # line Lecture 1 drew when it kept the monitoring numbers and dropped
            # the doses.
            for m in re.finditer(r"\b\d+(\.\d+)?\s*%", text):
                window = text[max(0, m.start() - 60):m.end() + 60].lower()
                if not re.search(r"effective|of patients|of cases|mortality|risk|survival", window):
                    raise AssertionError("strength in a cram row: %r" % label)

    # the subtitle still describes a one-lecture sheet
    s = re.sub(r'<p class="sub">Lecture 1:.*?</p>',
               '<p class="sub">All three Exam 1 lectures &mdash; antimicrobials, dermatology '
               'medications and autonomic pharmacology. Class identity first, then indications, '
               'patient education, side effects and contraindications. Drug dosages are not '
               'tested.</p>', s, count=1, flags=re.S)

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lectures 2 and 3 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance, jump links, syllabus order and the no-dose guard all verified")


if __name__ == "__main__":
    main()
