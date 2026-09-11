#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Pharmacology I Exam 2 cram sheet (Lecture 4, Ophthalmic Drugs).

Opens with what Dr. Wood excludes, because on this lecture that is the single
most useful thing to read first -- a 79-slide drug deck of which dosing,
formulations, the indications table and per-agent adverse effects are all off
the table.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "cram-sheet-template"))
from render import render

OUT = os.path.join(os.path.dirname(HERE),
                   "Pharmacology I Exam 2/pharm-exam-2-cram-sheet.html")

T = [
{"id":"rules","label":"What is NOT on it","color":"#8c1d12","rows":[
 ["Dosing","&ldquo;Not for memorization sake necessarily, because you can always look up the dosing for a medication <b>if you know which drug you actually want to use in the first place</b>.&rdquo; The deck is full of regimens. Learn none of them."],
 ["Formulations","&ldquo;I don&rsquo;t care that you memorize that necessarily, with some exceptions.&rdquo; Percent strengths, solution against ointment: not the question."],
 ["The indications table","&ldquo;Don&rsquo;t worry so much about indications for use&hellip; a lot of them have a lot of crossover.&rdquo; Slide 14 lists ten antibiotics against overlapping indications; it is orientation, not content."],
 ["Which agent irritates","&ldquo;Don&rsquo;t memorize which ones cause eye irritation or hypersensitivity. <b>Any of these can do that.</b>&rdquo; Only two adverse effects name a drug &mdash; see the antibiotics block."],
 ["Combination products","&ldquo;The specific combinations, I don&rsquo;t care that you memorize, <b>BUT</b> just know if I was to say, hey, patient&rsquo;s on this drug right now, what would be a helpful second line agent to add on?&rdquo; Products out, reasoning in."],
 ["&#9733; What IS promised","&ldquo;<b>I will tell you, I will ask this question</b>&hellip; there&rsquo;s rebound hyperaemia.&rdquo; It is in the allergy block below."],
]},
{"id":"kinetics","label":"Delivery &amp; kinetics","color":"#2f4f6b","rows":[
 ["ONE variable","<b>Time in contact with the eye.</b> Gels, ointments and solid inserts exist to prolong contact in the cul-de-sac. So does blocking the tear ducts with silicone plugs or cautery."],
 ["Two routes, two effects","<b>TRANSCORNEAL &rarr; local effect.</b> Has a lag time; rate depends on the CONCENTRATION GRADIENT, governed by <b>Fick&rsquo;s law</b>. <b>NASOLACRIMAL &rarr; systemic effect</b>, and it <b>AVOIDS FIRST-PASS METABOLISM</b> &mdash; which is why a topical beta blocker can drop a heart rate."],
 ["Four absorption determinants","Time in cul-de-sac and tear film &middot; nasolacrimal drainage &middot; protein binding &middot; diffusion across cornea and conjunctiva."],
 ["Prodrugs activated IN the eye","<b>Dipivefrin &rarr; epinephrine. Latanoprost &rarr; prostaglandin F2-alpha.</b> Some drugs instead ACCUMULATE &mdash; chloroquine&rsquo;s <b>bull&rsquo;s eye lesion</b>."],
 ["Route trade-offs","TOPICAL: convenient, economical, safe; costs compliance, surface toxicity, systemic absorption. PERIOCULAR (subconjunctival, sub-Tenon&rsquo;s, retrobulbar): reaches posterior uveitis and cystoid macular oedema; risks <b>globe perforation, optic nerve trauma, retinal vessel occlusion</b>. INTRACAMERAL: prompt, anterior segment, short-lived."],
]},
{"id":"abx","label":"Ocular antibiotics","color":"#1f6f5c","rows":[
 ["★ THE MECHANISM PAIR","<b>Macrolides &rarr; 50S</b> (block transpeptidation). <b>Aminoglycosides &rarr; 30S.</b> Same endpoint, different subunit."],
 ["The other mechanisms","<b>Fluoroquinolones</b> &rarr; DNA gyrase + topoisomerase IV, double-stranded breakage. <b>Bacitracin</b> &rarr; blocks mucopeptide transfer into the CELL WALL. <b>Polymyxin B</b> &rarr; binds membrane phospholipids, contents leak. <b>Sulfacetamide</b> &rarr; antagonises PABA. <b>Trimethoprim</b> &rarr; blocks reduction to tetrahydrofolate. (The last two are the same pathway, one step apart.)"],
 ["★ DRUG CHOICE","<b>Erythromycin</b> = commonest, SOOTHING, usable before a bacterial cause is confirmed; also ophthalmia neonatorum prophylaxis. <b>Fluoroquinolone</b> = corneal ulcers, suspected <b>Pseudomonas</b>, and therefore CONTACT LENS wearers once keratitis is excluded. <b>Azithromycin</b> = twice daily instead of 4+, but expensive and used less."],
 ["The only two adverse effects that name a drug","<b>Ciprofloxacin &rarr; white precipitate in ~17%.</b> <b>Aminoglycoside over several days &rarr; corneal ulceration and reactive keratoconjunctivitis.</b> Everything else irritates."],
 ["The only hard contraindication","<b>Sulfacetamide in sulfonamide allergy.</b>"],
 ["Conjunctivitis context","Most is NOT bacterial: viruses, allergy, irritants, contact lenses. Bacteria: <b>Neisseria, Haemophilus, Strep pneumoniae, Staph aureus, Moraxella</b>. Treat empirically, broad spectrum, <b>no cultures unless an unusual organism is expected</b>."],
]},
{"id":"viral","label":"Antivirals &amp; antifungals","color":"#7a4a9c","rows":[
 ["★ NO antiviral for adenoviral conjunctivitis","Self-limited; symptomatic relief only. Antivirals exist for <b>keratitis, herpes zoster ophthalmicus, retinitis</b>."],
 ["Topical antivirals","<b>Trifluridine</b> &rarr; inhibits thymidylate synthetase AND substitutes for thymidine in viral DNA. <b>Ganciclovir</b> &rarr; competitively inhibits dGTP binding to DNA polymerase; intravitreal for CMV retinitis."],
 ["Systemic antivirals","<b>Acyclovir, valacyclovir, famciclovir</b> oral &mdash; zoster ophthalmicus, simplex keratitis. <b>Foscarnet</b> intravenous &mdash; CMV retinitis."],
 ["★ Natamycin","<b>The ONLY commercially available ophthalmic antifungal.</b> Polyene &mdash; binds sterol, increases membrane permeability. Covers Aspergillus, Candida, Cephalosporium, <b>Fusarium</b>, Penicillium. <b>Amphotericin B</b> is the one with every route (topical, subconjunctival, intravitreal, intravenous)."],
 ["★ Fungal risk factors","Trauma &middot; chronic ocular surface disease &middot; contact lens wear &middot; immunosuppression &mdash; <b>including topical steroid use</b>. The only one a prescription creates."],
]},
{"id":"allergy","label":"Allergy","color":"#a8562f","rows":[
 ["★★ REBOUND HYPERAEMIA","The promised question. OTC redness drops are <b>alpha-1 agonists</b> &rarr; vasoconstriction. Constant activation <b>DOWNREGULATES the receptors</b> &rarr; on stopping, fewer receptors for endogenous catecholamines &rarr; <b>vessels blow open</b>. Use <b>&lt;2 weeks</b>; no improvement in <b>72 hours</b> &rarr; stop and be seen."],
 ["★ Imidazoline ingestion","<b>LOCALLY alpha-1. SYSTEMICALLY alpha-2.</b> That is why a toddler who swallows the bottle gets CNS depression and apnoea, not hypertension. Same receptor logic as the brimonidine age limit."],
 ["H1 agents","<b>Not antagonists &mdash; INVERSE AGONISTS</b> that inactivate the receptor, still competitive with histamine. Onset <b>minutes</b>; allow <b>2 weeks</b> for full efficacy. Typically preferred over mast cell stabilisers. Can worsen dryness."],
 ["Mast cell stabilisers","Cromolyn, lodoxamide, nedocromil. Inhibit degranulation (histamine, tryptase, PGD2). <b>5&ndash;14 days</b> to full effect &mdash; <b>NOT for acute symptoms</b>. Often 4&times; daily. For predictable seasonal allergy in someone intolerant of alternatives."],
 ["The cascade","IgE binds Fc receptors on <b>mast cells and basophils</b>; tyrosine kinases in <b>5&ndash;15 seconds</b>; histamine, PAF, leukotrienes &rarr; vasodilation, swelling, redness, itch."],
]},
{"id":"inflam","label":"Anti-inflammatories &amp; dry eye","color":"#b8862f","rows":[
 ["★ One step apart","<b>STEROIDS inhibit phospholipase A2</b> &mdash; arachidonic acid never liberated, whole cascade fails. <b>NSAIDs block cyclooxygenase</b> &mdash; only the prostaglandin/thromboxane arm."],
 ["NSAIDs","Bromfenac, diclofenac, flurbiprofen, ketorolac, nepafenac. For <b>postoperative inflammation and pain</b> and allergic conjunctivitis; <b>NOT routinely for conjunctivitis</b>. Adverse: lacrimation, keratitis, <b>raised IOP</b>."],
 ["★ Steroid risks &rarr; &lt;2 week pulse","Cataract &middot; raised IOP and glaucoma (<b>more with family history</b>) &middot; infection &middot; delayed wound healing &middot; corneal ulcers. Also inhibit fibrin/collagen deposition &rarr; less scarring."],
 ["★ &ldquo;Soft steroids&rdquo;","<b>Fluorometholone, loteprednol, rimexolone</b> &mdash; lower IOP risk. Triamcinolone = intravitreal."],
 ["Dry eye order","<b>TREAT THE DISEASE FIRST</b> (Sjogren, rheumatoid, vitamin A deficiency, Stevens-Johnson). Then punctal plugs or surgical occlusion, then tear substitutes (electrolytes + surfactants + <b>thickeners to prolong cul-de-sac time</b>)."],
 ["Cyclosporine","Inhibits <b>interleukin-2</b> &rarr; less T cell activation &rarr; less lacrimal gland inflammation &rarr; more tears. For <b>chronic dry eye WITH inflammation</b>. Warn: <b>burning in ~17%</b>."],
]},
{"id":"glaucoma","label":"Glaucoma","color":"#4a4f8c","rows":[
 ["★ Sort every drug by side","<b>INCREASE OUTFLOW:</b> prostaglandins, alpha agonists, cholinergics. <b>DECREASE PRODUCTION:</b> alpha agonists, beta blockers, carbonic anhydrase inhibitors. <b>Alpha agonists are on BOTH</b> &mdash; that is where the errors come from."],
 ["The three definitions","<b>Ocular hypertension</b> = high pressure, NO nerve damage, NO field loss. <b>Open angle</b> = increased production or decreased drainage; may have damage. <b>Angle closure</b> = blocked canal, often normal nerve, usually acute PAIN. Normal IOP <b>10&ndash;21 mmHg</b>. Drugs target OPEN angle."],
 ["★ Prostaglandins","<b>FIRST LINE, most commonly used.</b> Increase outflow. <b>ONCE DAILY &mdash; exceeding it INHIBITS the effect.</b> Warn: <b>eyelash length and IRIS COLOUR change</b>, hyperaemia. Latanoprost, travoprost, bimatoprost, tafluprost."],
 ["★ Beta blockers","Block beta receptors in ciliary epithelium &rarr; less cAMP &rarr; less production. <b>Betaxolol = beta-1 SELECTIVE</b> (safer in asthma). Carteolol, timolol, levobunolol = non-selective, more efficacious, more risk. Systemic: <b>heart failure, bradycardia, heart block, airway resistance</b>."],
 ["★ Alpha-2 agonists","Apraclonidine, brimonidine. Reduce production AND increase outflow. <b>CONTRAINDICATED UNDER 2 YEARS &mdash; CNS depression and apnoea.</b> Apraclonidine ionised &rarr; less blood-brain penetration; brimonidine lipophilic but less allergic conjunctivitis."],
 ["Carbonic anhydrase inhibitors","Dorzolamide, brinzolamide. Less bicarbonate &rarr; less fluid. Tolerability is the issue: <b>bitter taste ~25%, stinging ~33%</b>."],
 ["Cholinergics","Pilocarpine, carbachol, acetylcholine. Muscarinic &rarr; ciliary muscle contracts &rarr; outflow opens. <b>Fixed small pupils, myopia, blurring</b> &mdash; <b>young patients cannot tolerate it</b>."],
 ["★ Treat / target","Treat those <b>with risk factors</b>; monitor those without. Start with a <b>prostaglandin or beta blocker</b>, optionally <b>one eye</b> as its own control. Goal: <b>20&ndash;30% reduction</b>. Combinations are synergistic across DIFFERENT routes."],
]},
{"id":"diag","label":"Diagnostic agents &amp; administration","color":"#3d6b52","rows":[
 ["★ Anaesthetics","Tetracaine, proparacaine. Inhibit <b>sodium influx</b>. For tonometry, foreign body removal, superficial corneal surgery. <b>Numb 10&ndash;20 min with NO BLINK REFLEX.</b> <b>DO NOT PRESCRIBE</b> &mdash; repeated use is epithelial-toxic and delays healing."],
 ["Cycloplegics &mdash; two routes","<b>ANTIMUSCARINICS</b> (atropine, cyclopentolate, tropicamide) block muscarinic receptors &rarr; mydriasis. <b>SYMPATHOMIMETIC</b> (phenylephrine) stimulates the dilator &rarr; pupil stays <b>more light-reactive</b>. Uses: fundoscopy; uveitis to prevent synechiae and relieve ciliary spasm."],
 ["Fluorescein","Reveals <b>epithelial defects of cornea and conjunctiva</b>. Anterior segment staining; discloses corneal injury."],
 ["★ BEFORE any drop","<b>MEASURE VISUAL ACUITY.</b> Document allergies and last eye exam. Repeat acuity every visit &mdash; <b>if it worsens, immediate ophthalmology consult</b>."],
 ["Instillation","<b>Wash hands (most important)</b> &rarr; dropper touches nothing &rarr; head back, lower lid pocket &rarr; one drop &rarr; close eyes, tilt forward, <b>finger over lacrimal duct</b> &rarr; hold <b>2&ndash;3 minutes</b> &rarr; wipe, wash again."],
 ["Ointments &amp; lenses","Ointment suits <b>children and poor compliers</b> (works even from the lashes); ribbon into the pocket, <b>no duct occlusion needed</b>; <b>blurs vision ~20 min</b>. Contact lenses: stop; resume after <b>24 h free of inflammation and discharge</b>; discard or disinfect the lens; bin the eye makeup."],
]},
]

html = render(
    title="Pharmacology I Exam 2 Cram Sheet &mdash; Ophthalmic Drugs",
    kicker="Pharmacology I &middot; Exam 2 &middot; Class of 2028",
    h1="Ophthalmic Drugs Cram Sheet",
    sub="Lecture 4, Adam Wood Pharm.D. DABAT. Opens with what he says is NOT on the exam, "
        "because on this lecture that is the most useful thing to read first.",
    topics=T,
    guide_href="pharm-exam-2-study-guide.html",
    footer_note="Lecture 4 of five in Exam 2 &mdash; lectures 5 to 8 are not delivered yet. "
                "The <a href=\"pharm-exam-2-study-guide.html\">study guide</a> has the full "
                "treatment.")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d topics, %d rows)"
      % (os.path.basename(OUT), len(html)//1024, len(T), sum(len(t["rows"]) for t in T)))
