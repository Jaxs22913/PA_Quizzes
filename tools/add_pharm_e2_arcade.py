#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Pharmacology I Exam 2 (Ophthalmic Drugs) Arcade decks.

Three decks matching the three quiz topics, so a student can drill the same
split they revise. ATOMIC FACTS ONLY per [[arcade_content_policy]] -- one
question, one short answer.

NOTHING HERE IS A DOSE OR A FORMULATION. Dr. Wood excludes both, and a
flashcard deck is exactly where that material would creep back in because it
looks so drillable. The assertion at the bottom enforces it.

Idempotent: fenced between markers, re-runnable. Carries the two guards the CMS
adder earned the hard way -- decks must land INSIDE DEMO_DECKS, and the exam
registry edit is scoped to the Pharmacology group so it cannot rewrite another
class's deck list.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCADE = os.path.join(ROOT, "arcade.js")
OPEN, CLOSE = "  // <!--PHARME2-DECKS-->", "  // <!--/PHARME2-DECKS-->"

EYE_ICON = ('<path d="M2 12s4-7 10-7 10 7 10 7-4 7-10 7-10-7-10-7z"/><circle cx="12" cy="12" r="3"/>')
DROP_ICON = ('<path d="M12 3s5 6 5 9a5 5 0 0 1-10 0c0-3 5-9 5-9z"/>')
PRESS_ICON = ('<circle cx="12" cy="12" r="8"/><path d="M12 8v4l3 2"/><path d="M12 2v2M12 20v2"/>')

DECKS = [
 ("pharm-oph-antiinfective", "Ocular Anti-infectives", "accent1", DROP_ICON, [
  ("Macrolides inhibit protein synthesis at which ribosomal subunit?", "The 50S."),
  ("Aminoglycosides inhibit protein synthesis at which subunit?", "The 30S."),
  ("Which enzymes do the ophthalmic fluoroquinolones inhibit?", "DNA gyrase and topoisomerase IV."),
  ("What does bacitracin block?", "Transfer of mucopeptides into the cell wall."),
  ("How does polymyxin B work?", "It binds membrane phospholipids and lets the contents leak out."),
  ("Sulfacetamide blocks folate synthesis by antagonising what?", "p-aminobenzoic acid."),
  ("Trimethoprim blocks which step?", "Reduction of folic acid to tetrahydrofolate."),
  ("Which ophthalmic antibiotic is contraindicated in sulfonamide allergy?", "Sulfacetamide."),
  ("Which class is preferred for corneal ulcers?", "The fluoroquinolones."),
  ("Which organism makes fluoroquinolones the choice in contact lens wearers?", "Pseudomonas aeruginosa."),
  ("Which is the commonest ophthalmic antibiotic?", "Erythromycin ointment."),
  ("Why can erythromycin be used before a bacterial cause is confirmed?", "It is soothing on the inflamed eye."),
  ("Which antibiotic is used for ophthalmia neonatorum prophylaxis?", "Erythromycin ointment."),
  ("Which fluoroquinolone causes a white precipitate in about 17 percent?", "Ciprofloxacin."),
  ("What can several days of an ophthalmic aminoglycoside cause?", "Corneal ulceration and reactive keratoconjunctivitis."),
  ("Why is azithromycin used less often than erythromycin?", "It is considerably more expensive."),
  ("Name the bacterial causes of conjunctivitis.", "Neisseria, Haemophilus, Streptococcus pneumoniae, Staphylococcus aureus, Moraxella catarrhalis."),
  ("Are cultures routinely taken before treating ocular infection?", "No, unless an unusual organism is expected."),
  ("Which vaccine changed the ocular microbiological spectrum?", "The Haemophilus influenzae vaccine."),
  ("Is there an antiviral for adenoviral conjunctivitis?", "No. It is self-limited and treated symptomatically."),
  ("How does trifluridine work?", "It inhibits thymidylate synthetase and substitutes for thymidine in viral DNA."),
  ("How does ganciclovir work?", "It competitively inhibits deoxyguanosine triphosphate binding to DNA polymerase."),
  ("Which antiviral is given intravitreally for cytomegalovirus retinitis?", "Ganciclovir."),
  ("Which antiviral is intravenous for cytomegalovirus retinitis?", "Foscarnet."),
  ("Which oral antivirals treat herpes zoster ophthalmicus?", "Acyclovir, valacyclovir and famciclovir."),
  ("Which is the only commercially available ophthalmic antifungal?", "Natamycin."),
  ("How does natamycin work?", "It binds sterol and increases fungal membrane permeability."),
  ("Which antifungal is given by every route including intravitreal?", "Amphotericin B."),
  ("Name the risk factors for ophthalmic fungal infection.", "Trauma, chronic ocular surface disease, contact lens wear and immunosuppression."),
  ("Which fungal risk factor can a prescription create?", "Topical corticosteroid use."),
  ("What must be measured before instilling any ophthalmic medication?", "Visual acuity."),
  ("If visual acuity worsens at follow-up, what happens?", "Immediate ophthalmology consult."),
  ("Which absorption route avoids first-pass metabolism?", "Nasolacrimal drainage."),
  ("Which absorption route gives the local ocular effect?", "Transcorneal absorption."),
  ("Which law governs the rate of transcorneal absorption?", "Fick's law, by the concentration gradient."),
  ("Dipivefrin is a prodrug for what?", "Epinephrine."),
  ("Latanoprost is a prodrug for what?", "Prostaglandin F2-alpha."),
  ("Which drug causes a bull's eye lesion by accumulating in the eye?", "Chloroquine."),
  ("Why do gels and ointments increase absorption?", "They prolong contact time in the cul-de-sac."),
  ("Which injection route risks globe perforation and optic nerve trauma?", "Periocular injection, including retrobulbar."),
 ]),
 ("pharm-oph-allergy", "Ocular Allergy &amp; Inflammation", "accent2", EYE_ICON, [
  ("What is rebound hyperaemia?", "Worsening redness after stopping a vasoconstrictor, from alpha-1 receptor downregulation."),
  ("How long may an over-the-counter ocular vasoconstrictor be used?", "Less than two weeks."),
  ("No improvement on a redness drop after how long means stop and be seen?", "Seventy-two hours."),
  ("Which receptor do imidazolines act on locally?", "Alpha-1."),
  ("Which receptor do imidazolines act on systemically?", "Alpha-2."),
  ("Why is imidazoline ingestion dangerous in a toddler?", "Central alpha-2 agonism causes depression, bradycardia and apnoea."),
  ("Ocular H1 agents are not antagonists. What are they?", "Inverse agonists."),
  ("How quickly do ocular antihistamines work?", "Within minutes."),
  ("How long before an ocular antihistamine's full efficacy can be judged?", "Two weeks."),
  ("Which ocular antihistamine is available over the counter?", "Ketotifen."),
  ("Name the three mast cell stabilisers.", "Cromolyn, lodoxamide and nedocromil."),
  ("How long do mast cell stabilisers take for full effect?", "Five to fourteen days."),
  ("Are mast cell stabilisers useful for acute symptoms?", "No."),
  ("What do mast cell stabilisers inhibit?", "Mast cell degranulation."),
  ("Which cells are the principal targets in ocular hypersensitivity?", "Mast cells and basophils."),
  ("How quickly do tyrosine kinases activate after IgE binds?", "Five to fifteen seconds."),
  ("Which mediators are released in the ocular allergic response?", "Histamine, platelet-activating factor and leukotrienes."),
  ("What do ocular NSAIDs inhibit?", "Cyclooxygenase."),
  ("What do ocular glucocorticoids inhibit?", "Phospholipase A2."),
  ("Which ocular NSAID adverse effect matters most in glaucoma?", "Raised intraocular pressure."),
  ("Are NSAIDs routinely recommended for conjunctivitis?", "No."),
  ("Name the ocular glucocorticoid adverse effects.", "Cataract, raised pressure and glaucoma, infection, delayed healing, corneal ulcers."),
  ("How long is an ocular steroid course generally limited to?", "Under two weeks."),
  ("Name the three soft steroids.", "Fluorometholone, loteprednol and rimexolone."),
  ("What makes a steroid a soft steroid?", "Lower risk of raising intraocular pressure."),
  ("Which glucocorticoid is given intravitreally?", "Triamcinolone."),
  ("Besides inflammation, what else do glucocorticoids reduce in the eye?", "Scar formation, by inhibiting fibrin and collagen deposition."),
  ("What is the first step in treating dry eye?", "Treat the underlying disease."),
  ("Name the physical interventions for dry eye.", "Punctal plugs and surgical occlusion of lacrimal drainage."),
  ("How does cyclosporine help dry eye?", "It inhibits interleukin-2, reducing T cell activation and lacrimal gland inflammation."),
  ("What proportion get ocular burning on cyclosporine?", "About seventeen per cent."),
  ("What is the most important step when instilling an eye drop?", "Washing the hands thoroughly."),
  ("Why hold a finger over the lacrimal duct after a drop?", "To keep drug on the eye and limit systemic absorption."),
  ("How long are the eyes held closed after a drop?", "Two to three minutes."),
  ("Who are ointments preferred for?", "Children and those with poor compliance."),
  ("How long does an ophthalmic ointment blur vision?", "About twenty minutes."),
  ("When may contact lens wear resume after conjunctivitis?", "After 24 hours free of inflammation and discharge."),
 ]),
 ("pharm-oph-glaucoma", "Glaucoma &amp; Diagnostics", "accent3", PRESS_ICON, [
  ("What is the normal range of intraocular pressure?", "Ten to twenty-one millimetres of mercury."),
  ("What is ocular hypertension?", "Raised pressure with no optic nerve damage and no visual field loss."),
  ("What defines angle-closure glaucoma?", "Blockage of the drainage canal, usually with acute pain."),
  ("Which type of glaucoma do the drugs target?", "Open angle."),
  ("What are the two drug strategies in glaucoma?", "Decrease aqueous production or increase outflow."),
  ("Which classes increase outflow?", "Prostaglandins, alpha adrenergic agonists and cholinergic agonists."),
  ("Which classes decrease production?", "Alpha adrenergic agonists, beta blockers and carbonic anhydrase inhibitors."),
  ("Which class appears on both the production and outflow lists?", "The alpha adrenergic agonists."),
  ("Which class is first line for glaucoma?", "The prostaglandin analogues."),
  ("How often are prostaglandin analogues given?", "Once daily."),
  ("What happens if prostaglandin dosing is exceeded?", "The pressure-lowering effect is inhibited."),
  ("Name the cosmetic adverse effects of prostaglandin analogues.", "Eyelash lengthening and iris colour change."),
  ("How do ophthalmic beta blockers lower pressure?", "They block beta receptors in the ciliary epithelium, reducing cyclic AMP and aqueous production."),
  ("Which ophthalmic beta blocker is beta-1 selective?", "Betaxolol."),
  ("Why are non-selective beta blockers risky in asthma?", "Beta-2 blockade increases airway resistance."),
  ("Name the systemic adverse effects of ophthalmic beta blockers.", "Worsening heart failure, bradycardia, heart block and increased airway resistance."),
  ("Name the two ophthalmic alpha-2 agonists.", "Apraclonidine and brimonidine."),
  ("In whom are ophthalmic alpha-2 agonists contraindicated?", "Children under two years."),
  ("Why are alpha-2 agonists contraindicated in young children?", "Central nervous system depression and apnoea."),
  ("Why does apraclonidine have limited systemic effects?", "It is highly ionised, so it penetrates the blood-brain barrier poorly."),
  ("How do carbonic anhydrase inhibitors lower pressure?", "They reduce bicarbonate production in the ciliary epithelium, so less fluid is transported."),
  ("Name the two topical carbonic anhydrase inhibitors.", "Dorzolamide and brinzolamide."),
  ("What proportion get bitter taste from a carbonic anhydrase inhibitor?", "About twenty-five per cent."),
  ("How do cholinergic agonists lower pressure?", "They activate muscarinic receptors, contracting the ciliary muscle and opening outflow."),
  ("Name the adverse effects of ocular cholinergic agonists.", "Fixed small pupils, myopia, visual disturbance and headache."),
  ("Why do younger patients tolerate miotics poorly?", "Visual blurring, because they still accommodate strongly."),
  ("Which patients with raised pressure are treated?", "Those with risk factors."),
  ("Which two classes are reasonable places to start therapy?", "A prostaglandin analogue or a beta blocker."),
  ("Why might therapy start in one eye only?", "To judge efficacy and tolerability against the untreated eye."),
  ("What is the general target for pressure reduction?", "Twenty to thirty per cent."),
  ("Why are combination products synergistic?", "They target different routes, production and outflow."),
  ("How do ocular anaesthetics work?", "They inhibit sodium influx into the neuron."),
  ("Name the two topical ocular anaesthetics.", "Tetracaine and proparacaine."),
  ("How long does an ocular anaesthetic last, and what is lost?", "Ten to twenty minutes, with no blink reflex."),
  ("Should ocular anaesthetics be prescribed for home use?", "No."),
  ("How do antimuscarinic cycloplegics dilate the pupil?", "They competitively block muscarinic acetylcholine receptors."),
  ("Name the antimuscarinic cycloplegics.", "Atropine, cyclopentolate and tropicamide."),
  ("Which sympathomimetic is used for mydriasis?", "Phenylephrine."),
  ("How does phenylephrine differ from the antimuscarinics?", "The pupil remains more reactive to light."),
  ("Besides fundoscopy, what are cycloplegics used for?", "Uveitis, to prevent synechiae and relieve ciliary spasm."),
  ("What does fluorescein reveal?", "Epithelial defects of the cornea and conjunctiva."),
 ]),
]


def js(decks):
    out = []
    for did, name, color, icon, cards in decks:
        rows = "\n".join('      [%s, %s],' % (jstr(q), jstr(a)) for q, a in cards)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ] }," % (did, name, color, icon, rows))
    return "\n".join(out) + "\n"


def jstr(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    # Nothing in this deck may be a dose or a strength.
    bad = re.compile(r"(?i)\b\d+\s*(mg|milligram|microgram|unit|per cent solution)\b"
                     r"|\b\d+\s*%\s*(solution|ointment|suspension)")
    for did, _n, _c, _i, cards in DECKS:
        for q, a in cards:
            assert not bad.search(q + " " + a), "%s: dose or strength in a card: %r" % (did, q)

    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(DECKS) + CLOSE

    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src, flags=re.S)
    else:
        decl = src.index("var DEMO_DECKS = [")
        end = src.index("\n];", decl)
        src = src[:end] + "\n\n" + block + src[end:]

    ids = ", ".join('"%s"' % d[0] for d in DECKS)
    exam2 = '    { id: "exam2", name: "Exam 2", deckIds: [\n      %s\n    ] }' % ids

    g_start = src.index('  { id: "pharm-1", name: "Pharmacology I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 1"') == 1, "Pharmacology group not isolated cleanly"

    if 'name: "Exam 2"' in group:
        group = re.sub(r'    \{ id: "exam2", name: "Exam 2", deckIds: \[.*?\] \}',
                       lambda _m: exam2, group, flags=re.S)
    else:
        e1 = group.rindex("] }")
        group = group[:e1 + len("] }")] + ",\n" + exam2 + group[e1 + len("] }"):]
    src = src[:g_start] + group + src[g_end:]

    d0 = src.index("var DEMO_DECKS = [")
    d1 = src.index("\n];", d0)
    for did, *_ in DECKS:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s was placed OUTSIDE the DEMO_DECKS array" % did

    open(ARCADE, "w", encoding="utf-8").write(src)
    n = sum(len(d[4]) for d in DECKS)
    print("wrote %d decks, %d cards into arcade.js" % (len(DECKS), n))
    for did, name, _c, _i, cards in DECKS:
        print("   %-26s %-32s %d cards" % (did, re.sub("&[a-z]+;", "&", name), len(cards)))


if __name__ == "__main__":
    main()
