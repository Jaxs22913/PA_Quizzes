#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Pharmacology I Exam 2 study guide (Lecture 4, Ophthalmic Drugs).

Same skeleton-lift as build_pharm_guide.py: take the Exam 1 guide's head and
tail so the chrome, design system and read-aloud wiring come for free, and
splice in a fresh table of contents and body.

BUILT INCREMENTALLY, AND THE PAGE SAYS SO. The syllabus puts LECTURES 4 TO 8 in
Exam 2; only Lecture 4 has been delivered. The remaining four drop in as further
sections without touching this file's structure, exactly as the CMS Exam 3
chart was grown.

Objectives are VERBATIM from the syllabus, not from the deck. The two differ on
objective 2 -- the syllabus says "molecular mechanism of action", the slide
drops "molecular" -- and [[guide_verbatim_io_rule]] says the syllabus wins.

Deliberately NO data-audio-dir: the mp3s do not exist, and pointing at an empty
audio folder broke read-aloud on iPad once already.
"""
import os, re

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Pharmacology I Exam 1/pharm-exam-1-study-guide.html")
OUT = os.path.join(ROOT, "Pharmacology I Exam 2/pharm-exam-2-study-guide.html")

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#ophthalmic">1 &middot; Ophthalmic Drugs</a>
  <a href="#oph-delivery">1.1 Objective 4 &mdash; Getting a drug into the eye, and out again</a>
  <a href="#oph-antibiotics">1.2 Objectives 1&ndash;3 &mdash; Ocular antibiotics</a>
  <a href="#oph-antivirals">1.3 Objectives 1&ndash;3 &mdash; Antivirals and antifungals</a>
  <a href="#oph-allergy">1.4 Objectives 1&ndash;3 &mdash; Allergy and the red eye</a>
  <a href="#oph-inflam">1.5 Objectives 5&ndash;7 &mdash; Anti-inflammatories and dry eye</a>
  <a href="#oph-glaucoma">1.6 Objectives 1&ndash;7 &mdash; Glaucoma</a>
  <a href="#oph-diagnostic">1.7 Objectives 1&ndash;3 &mdash; Diagnostic and procedural agents</a>
  <a href="#oph-admin">1.8 Objectives 9&ndash;10 &mdash; Administration, monitoring and patient education</a>
</nav>'''

BODY = '''<main>

<section class="deck" id="ophthalmic">
  <h2 class="deck-title">1 &middot; Ophthalmic Drugs</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify ophthalmic drug classes and commonly prescribed ophthalmic drugs.</li>
      <li>Describe the molecular mechanism of action of ophthalmic drugs.</li>
      <li>Identify indications for commonly used ophthalmic drugs.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of ophthalmic drugs.</li>
      <li>Summarize side effects and toxic manifestations of ophthalmic drugs.</li>
      <li>Describe adverse effects of ophthalmic drugs.</li>
      <li>Identify contraindications for ophthalmic drugs.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with ophthalmic drugs.</li>
      <li>List commonly used protocols and patient monitoring for ophthalmic drugs.</li>
      <li>Outline appropriate patient education for ophthalmic drugs.</li>
    </ol>
  </div>

  <div class="callout"><strong>This is one of five lectures in Exam 2.</strong> The syllabus puts
  <strong>Lectures 4 to 8</strong> in this exam &mdash; ophthalmic drugs, then ear, nose and
  throat, and then the cardiovascular block. Only Lecture 4 has been delivered, so this guide has
  one section and will grow. It says so rather than implying the exam is covered.</div>

  <div class="prof-flag">
    <span class="prof-flag-label">&#9733; HE PROMISED TO ASK THIS</span>
    <p style="margin-top:2px">At 50:27 of the recording: <em>&ldquo;Most of you will probably
    forget this and we&rsquo;ll get it wrong on the test. But I will tell you, <strong>I will ask
    this question</strong>, it&rsquo;ll come up in ENT as well &mdash; there&rsquo;s <strong>rebound
    hyperaemia</strong>.&rdquo;</em></p>
    <p>The mechanism in his own words: over-the-counter redness drops are <strong>alpha-1
    agonists</strong> that vasoconstrict to reduce swelling and oedema. Constant activation
    <strong>downregulates the receptors</strong>, so when the drug stops there are fewer left for
    naturally occurring noradrenaline and adrenaline to bind &mdash; and the vessels
    <em>&ldquo;just blow open&rdquo;</em>. Hence the counselling point on slide 48: use for
    <strong>under two weeks</strong>, and if there is no improvement in <strong>72 hours</strong>,
    stop and be seen, because it may be something more serious.</p>
  </div>

  <div class="callout"><strong>What he told you not to learn.</strong> This lecture is unusual for
  how much of its own deck it excludes, and taking him at his word is the difference between a
  sensible evening and a wasted one.
  <ul>
    <li><mark class="prof-highlight">Dosing</mark> &mdash; <em>&ldquo;not for memorization sake
    necessarily, because you can always look up the dosing for a medication if you know which drug
    you actually want to use in the first place.&rdquo;</em></li>
    <li><mark class="prof-highlight">Formulations</mark> &mdash; <em>&ldquo;I don&rsquo;t care that
    you memorize that necessarily, with some exceptions.&rdquo;</em></li>
    <li><mark class="prof-highlight">The indications table</mark> &mdash; <em>&ldquo;Don&rsquo;t
    worry so much about indications for use&hellip; a lot of them have a lot of
    crossover.&rdquo;</em></li>
    <li><mark class="prof-highlight">Which agent causes which adverse effect</mark> &mdash;
    <em>&ldquo;don&rsquo;t memorize which ones cause eye irritation or hypersensitivity. Any of
    these can do that.&rdquo;</em></li>
    <li><mark class="prof-highlight">Specific combination products</mark> &mdash; <em>&ldquo;the
    specific combinations, I don&rsquo;t care that you memorize, <strong>but</strong> just know if
    I was to say, hey, patient&rsquo;s on this drug right now, what would be a helpful second line
    agent to add on?&rdquo;</em> The products are out; the reasoning is in.</li>
  </ul>
  What is left is <strong>mechanism</strong>, <strong>drug choice</strong>, and the handful of
  facts he stops to make. This guide is written to that.</div>

  <h3 class="sub" id="oph-delivery">1.1 &middot; Objective 4 &mdash; Getting a drug into the eye, and out again</h3>

  <p>Every formulation decision in this lecture comes back to one variable: <strong>how long the
  drug stays in contact with the eye</strong>. Most drugs are given as solutions; suspensions are
  used where solubility is limited; and <strong>gels, ointments and solid inserts exist to prolong
  contact in the cul-de-sac</strong>. More time in the cul-de-sac means more absorption, and
  inserts and implants extend that into sustained release.</p>

  <p>Four things determine how much gets absorbed: <strong>time in the cul-de-sac and the
  precorneal tear film</strong>, <strong>nasolacrimal drainage</strong>, <strong>drug binding to
  tear and tissue proteins</strong>, and <strong>diffusion across the cornea and
  conjunctiva</strong>. Two of those can be manipulated &mdash; change the formulation, or block
  the tear ducts with silicone plugs or cautery so the drug cannot drain away.</p>

  <div class="pearl"><strong>The two routes out, and why it matters.</strong>
  <strong>Transcorneal</strong> absorption is what produces the <em>local</em> ocular effect: it
  has a lag time, and its rate depends most on the <strong>concentration gradient</strong>,
  governed by <strong>Fick&rsquo;s law</strong>. <strong>Nasolacrimal</strong> drainage is what
  produces the <em>systemic</em> effect &mdash; and because it bypasses the portal circulation it
  <strong>avoids first-pass metabolism</strong>. That single fact explains why a topical beta
  blocker can cause bradycardia, and why pressing on the punctum after a drop is worth doing.</div>

  <p>Distribution into the eye happens normally after systemic absorption, and some drugs
  <strong>accumulate</strong> there &mdash; the named example is the <strong>bull&rsquo;s eye
  lesion after chloroquine</strong>. Some drugs are also <strong>metabolised within the eye</strong>,
  which is exploited deliberately: <strong>dipivefrin becomes epinephrine</strong> and
  <strong>latanoprost becomes prostaglandin F2-alpha</strong> once inside. Elimination is otherwise
  ordinary hepatic and renal clearance.</p>

  <p>The route table is worth holding by its trade-offs rather than its rows. <strong>Topical</strong>
  is convenient, economical and relatively safe, at the price of compliance, surface toxicity and
  systemic absorption. <strong>Periocular injection</strong> &mdash; subconjunctival, sub-Tenon&rsquo;s,
  retrobulbar &mdash; reaches posterior uveitis and cystoid macular oedema, at the price of
  <strong>globe perforation, optic nerve trauma and retinal artery or vein occlusion</strong>.
  <strong>Intracameral</strong> injection is prompt and used in anterior segment surgery and
  infection, but short-lived.</p>

  <h3 class="sub" id="oph-antibiotics">1.2 &middot; Objectives 1&ndash;3 &mdash; Ocular antibiotics</h3>

  <p>Most conjunctivitis is <strong>not</strong> bacterial. The common causes given are
  <strong>viruses, allergies, environmental irritants and contact lenses</strong>, with immune-mediated
  reactions, systemic disease and tumours less common. The bacterial pathogens worth naming are
  <strong>Neisseria, Haemophilus, Streptococcus pneumoniae, Staphylococcus aureus</strong> and
  <strong>Moraxella catarrhalis</strong>. The spectrum shifts over time &mdash; the example is the
  fall in <em>Haemophilus influenzae</em> after the vaccine.</p>

  <p>Small, mild, peripheral infections are treated <strong>topically and empirically</strong>,
  with broad-spectrum agents and <strong>no cultures unless an unusual organism is expected</strong>
  &mdash; the immunocompromised patient being the example. Topical therapy buys very high local
  concentrations at the cost of poor systemic bioavailability and frequent dosing. Whether a
  patient needs oral or parenteral treatment instead turns on <strong>clinical setting, age,
  immune status and how much is involved</strong>.</p>

  <div class="pearl"><strong>The mechanism pairing to hold.</strong> Two classes stop bacterial
  protein synthesis and differ only in where: <strong>macrolides at the 50S</strong> subunit
  (blocking transpeptidation) and <strong>aminoglycosides at the 30S</strong>. Everything else has
  its own target &mdash; <strong>fluoroquinolones</strong> inhibit DNA gyrase and topoisomerase IV
  so supercoiled DNA cannot relax and the strands break; <strong>bacitracin</strong> blocks
  mucopeptide transfer into the cell wall; <strong>polymyxin B</strong> binds membrane
  phospholipids and lets the contents leak out; and <strong>sulfacetamide</strong> and
  <strong>trimethoprim</strong> hit folate at successive steps &mdash; sulfacetamide antagonising
  p-aminobenzoic acid, trimethoprim blocking reduction to tetrahydrofolate.</div>

  <p><strong>Drug choice is the testable part.</strong> <strong>Erythromycin</strong> ointment is
  the commonest ophthalmic antibiotic and is <strong>soothing on an inflamed eye</strong>, so it
  may reasonably be used before a bacterial cause is confirmed; it is also the agent for
  <strong>ophthalmia neonatorum prophylaxis</strong>. <strong>Azithromycin</strong> is dosed twice
  daily rather than four or more times, but is considerably more expensive and used less often.
  <strong>Fluoroquinolones</strong> are preferred for <strong>corneal ulcers</strong> and for
  suspected <strong>Pseudomonas aeruginosa</strong>, which is why they are also the choice for
  conjunctivitis in a <strong>contact lens wearer</strong> once keratitis has been excluded &mdash;
  set against cost and emerging resistance.</p>

  <div class="callout"><strong>Two adverse effects that actually distinguish something.</strong>
  Ocular irritation and hypersensitivity are shared by essentially every agent here, so they name
  no drug. The two that do: <strong>ciprofloxacin produces a white precipitate in about 17%</strong>,
  worth recognising so it is not mistaken for a worsening infiltrate; and
  <strong>aminoglycosides used for several days can cause corneal ulceration and a reactive
  keratoconjunctivitis</strong>, which changes how long you continue them. The one genuine
  contraindication in the list is <strong>sulfacetamide in sulfonamide allergy</strong>.</div>

  <h3 class="sub" id="oph-antivirals">1.3 &middot; Objectives 1&ndash;3 &mdash; Antivirals and antifungals</h3>

  <p>Ocular antivirals exist for <strong>viral keratitis, herpes zoster ophthalmicus and
  retinitis</strong>. They do <strong>not</strong> exist for adenoviral conjunctivitis, which is
  self-limited and treated with symptomatic relief &mdash; a common exam trap because the patient
  in front of you looks like they need something.</p>

  <p>Topically, <strong>trifluridine</strong> inhibits thymidylate synthetase and is incorporated
  into viral DNA in place of thymidine, for herpes simplex keratoconjunctivitis.
  <strong>Ganciclovir</strong> competitively inhibits deoxyguanosine triphosphate binding to DNA
  polymerase, for herpetic keratitis and &mdash; by intravitreal injection &mdash; cytomegalovirus
  retinitis. Systemically, <strong>acyclovir, valacyclovir and famciclovir</strong> are the oral
  agents for zoster ophthalmicus and simplex keratitis, and <strong>foscarnet</strong> is
  intravenous for cytomegalovirus retinitis.</p>

  <p><strong>Natamycin is the only commercially available ophthalmic antifungal</strong> &mdash;
  that is the fact to hold, because everything else on the table is given by another route or
  compounded. It is a <strong>polyene</strong>: it binds sterol and increases fungal membrane
  permeability, covering <em>Aspergillus, Candida, Cephalosporium, Fusarium</em> and
  <em>Penicillium</em>. <strong>Amphotericin B</strong> is the agent with every route &mdash;
  topical, subconjunctival, intravitreal and intravenous &mdash; which is what makes it usable for
  endophthalmitis.</p>

  <div class="pearl"><strong>The risk factor you can create.</strong> Fungal ocular infection is
  rising as more patients are immunocompromised. The risk list is <strong>trauma, chronic ocular
  surface disease, contact lens wear and immunosuppression</strong> &mdash; and
  <mark class="prof-highlight">topical steroid use is named explicitly as immunosuppression</mark>.
  It is the only item on that list a prescription can introduce.</div>

  <h3 class="sub" id="oph-allergy">1.4 &middot; Objectives 1&ndash;3 &mdash; Allergy and the red eye</h3>

  <p>Mast cells and basophils are the principal target cells. <strong>Immunoglobulin E binds Fc
  receptors</strong>, tyrosine kinases activate within <strong>5 to 15 seconds</strong>, and
  <strong>histamine, platelet-activating factor and leukotrienes</strong> are released &mdash;
  producing vasodilation, swelling, redness and itch. Every drug below is aimed at one point in
  that sequence.</p>

  <p><strong>H1 agents are not really antagonists.</strong> They are <strong>inverse
  agonists</strong> &mdash; they drive the receptor into an inactive state rather than merely
  occupying it &mdash; while remaining competitive with histamine. They decrease capillary
  dilation, itch and swelling. Onset is <strong>within minutes</strong>, but allow
  <strong>two weeks</strong> to judge full efficacy. They are typically preferred over mast cell
  stabilisers, and can worsen ocular dryness.</p>

  <p><strong>Mast cell stabilisers</strong> &mdash; cromolyn, lodoxamide, nedocromil &mdash;
  inhibit degranulation, limiting release of histamine, tryptase and prostaglandin D2, and dampen
  basophils, eosinophils and neutrophils. They take <strong>5 to 14 days</strong> for full effect
  and are <strong>not useful for acute symptoms</strong>, which is the whole distinction from the
  antihistamines. Often four times daily. Their place is <strong>predictable seasonal allergy in
  someone who does not tolerate the alternatives</strong>.</p>

  <div class="pearl"><strong>The imidazoline question.</strong> The vasoconstrictors activate
  <strong>postjunctional alpha-adrenergic receptors</strong> on conjunctival vessels, reducing
  oedema and redness. But their receptor behaviour splits by route:
  <mark class="prof-highlight">locally they act on alpha-1; systemically they target
  alpha-2</mark>. That is why an accidental ingestion in a toddler causes central nervous system
  depression, bradycardia and apnoea rather than the hypertension you might expect &mdash; and it
  is the same central alpha-2 effect that contraindicates brimonidine under two years.</div>

  <h3 class="sub" id="oph-inflam">1.5 &middot; Objectives 5&ndash;7 &mdash; Anti-inflammatories and dry eye</h3>

  <p>The two anti-inflammatory classes sit one step apart in the same cascade.
  <strong>Glucocorticoids inhibit phospholipase A2</strong>, so arachidonic acid is never
  liberated and the whole downstream family of mediators fails. <strong>Nonsteroidals block
  cyclooxygenase</strong>, so arachidonic acid that has already been liberated cannot become
  prostaglandin or thromboxane. The steroids therefore cut off more, and cost more to use.</p>

  <p><strong>Nonsteroidals</strong> &mdash; bromfenac, diclofenac, flurbiprofen, ketorolac,
  nepafenac &mdash; are indicated for <strong>postoperative inflammation and pain</strong> and
  <strong>allergic conjunctivitis</strong>, and are <strong>not routinely recommended for
  conjunctivitis</strong> generally. Adverse effects: lacrimation, keratitis,
  <strong>raised intraocular pressure</strong> and irritation.</p>

  <p><strong>Glucocorticoids</strong> also inhibit fibrin and collagen deposition, so they reduce
  scarring &mdash; useful where a scar costs vision. They are used for severe ocular allergy,
  anterior uveitis, external eye inflammatory disease and post-surgical inflammation, generally
  for <strong>refractory</strong> symptoms.</p>

  <div class="callout"><strong>Why steroid courses are short.</strong> Cataract formation; raised
  intraocular pressure and glaucoma, <strong>more with a family history</strong>; infection,
  through reduced local immune function; delayed wound healing; corneal ulcers. Hence
  <mark class="prof-highlight">limited to under a two-week pulse</mark>. Three agents are marked as
  <strong>&ldquo;soft steroids&rdquo; with lower pressure risk &mdash; fluorometholone,
  loteprednol and rimexolone</strong>. Triamcinolone is the intravitreal one.</div>

  <p><strong>Dry eye</strong> is often a manifestation of something else &mdash; Sjogren syndrome,
  rheumatoid arthritis, vitamin A deficiency, Stevens-Johnson syndrome &mdash; so the first
  instruction is <strong>treat the disease</strong>. Then physical measures (<strong>punctal plugs,
  surgical occlusion</strong>) and tear substitutes: hypotonic or isotonic solutions with
  electrolytes, surfactants and <strong>thickeners to increase time in the cul-de-sac</strong>.</p>

  <p><strong>Cyclosporine</strong> inhibits <strong>interleukin-2</strong> production and so T cell
  activation, reducing inflammatory markers in the lacrimal gland and increasing tear production.
  Indication: <strong>chronic dry eye associated with inflammation</strong> (keratoconjunctivitis
  sicca). Warn about <strong>ocular burning in about 17%</strong>, foreign body sensation and
  blurred vision &mdash; a drug that takes time to work needs its side effects flagged up front.</p>

  <h3 class="sub" id="oph-glaucoma">1.6 &middot; Objectives 1&ndash;7 &mdash; Glaucoma</h3>

  <p>Raised pressure causes <strong>optic neuropathy &rarr; loss of retinal ganglion cell axons
  &rarr; visual field loss &rarr; irreversible blindness</strong>. Irreversible is the operative
  word: therapy prevents progression, it does not recover vision. Normal pressure is
  <strong>10 to 21 mmHg</strong>.</p>

  <div class="pearl"><strong>Three definitions that are examined against each other.</strong>
  <strong>Ocular hypertension</strong> &mdash; pressure above normal, <em>no</em> optic nerve
  damage, <em>no</em> field loss. A risk factor, not a disease. <strong>Open-angle glaucoma</strong>
  &mdash; increased production or decreased drainage; the patient may have nerve damage or reduced
  field. <strong>Angle-closure glaucoma</strong> &mdash; blockage of the drainage canal; the optic
  nerve may be normal but the patient is usually in acute pain. <strong>Drug therapy targets open
  angle disease.</strong></div>

  <p><strong>Sort every agent by which side it works on.</strong> Increasing outflow:
  <strong>prostaglandins</strong>, <strong>alpha adrenergic agonists</strong>,
  <strong>cholinergic agonists</strong>. Decreasing production: <strong>alpha adrenergic
  agonists</strong>, <strong>beta blockers</strong>, <strong>carbonic anhydrase inhibitors</strong>.
  The alpha agonists appear on <em>both</em> lists, which is where most errors come from.</p>

  <p><strong>Prostaglandins</strong> (latanoprost, travoprost, bimatoprost, tafluprost) analogue
  prostaglandin F2-alpha and increase outflow. They are <strong>first line and the most commonly
  used</strong>, dosed <strong>once daily &mdash; and exceeding that inhibits the pressure-lowering
  effect</strong>. Warn about <strong>eyelash lengthening and iris colour change</strong>, plus
  conjunctival hyperaemia. Limited systemic effects.</p>

  <p><strong>Beta blockers</strong> block beta receptors in the ciliary epithelium, reducing
  catecholamine activation and cyclic AMP, and so aqueous production. <strong>Betaxolol is
  beta-1 selective</strong>; carteolol, timolol and levobunolol are non-selective. Non-selective is
  more efficacious but riskier, because <strong>beta-2 receptors mediate bronchodilation</strong>.
  Systemic effects reach through nasolacrimal absorption: <strong>worsening heart failure,
  bradycardia, heart block, increased airway resistance</strong>.</p>

  <p><strong>Alpha-2 agonists</strong> (apraclonidine, brimonidine) reduce catecholamine release
  presynaptically and aqueous production postsynaptically, and increase outflow.
  <strong>Contraindicated under two years &mdash; central nervous system depression and
  apnoea.</strong> Apraclonidine is highly ionised at physiological pH, which limits blood-brain
  barrier penetration; brimonidine is more lipophilic but causes less allergic conjunctivitis.</p>

  <p><strong>Carbonic anhydrase inhibitors</strong> (dorzolamide, brinzolamide) reduce bicarbonate
  production in the ciliary epithelium, so less fluid is transported. Their problem is
  tolerability: <strong>bitter taste in about 25%</strong> and <strong>burning or stinging in about
  33%</strong>. <strong>Cholinergic agonists</strong> (pilocarpine, carbachol, acetylcholine)
  activate muscarinic receptors, contracting the ciliary muscle and opening outflow &mdash; but
  give <strong>fixed small pupils, induced myopia and visual disturbance</strong>, and
  <strong>younger patients are usually intolerant</strong> because they still accommodate.</p>

  <div class="callout"><strong>The question he said he would ask.</strong> Combination products
  &mdash; brimonidine with timolol, brinzolamide with brimonidine, dorzolamide with timolol &mdash;
  are synergistic because they target <em>different</em> routes, and fewer drops improves
  compliance. He does not want the products memorised; he wants
  <mark class="prof-highlight">&ldquo;patient&rsquo;s on this drug right now, what would be a
  helpful second line agent to add on?&rdquo;</mark> Answer it by asking which side of the
  production/outflow divide the current drug is on, and adding from the other.
  <br><br>
  <strong>Who to treat:</strong> those with risk factors. Those without are monitored until
  glaucomatous change occurs. Start with a <strong>prostaglandin or a beta blocker</strong>,
  optionally <strong>in one eye</strong> to judge efficacy and tolerability against the other.
  General goal: a <strong>20 to 30% reduction</strong>.</div>

  <h3 class="sub" id="oph-diagnostic">1.7 &middot; Objectives 1&ndash;3 &mdash; Diagnostic and procedural agents</h3>

  <p><strong>Anaesthetics</strong> (tetracaine, proparacaine) inhibit sodium influx into the neuron
  so the signal cannot propagate. Indications: <strong>tonometry, foreign body removal, superficial
  corneal surgery</strong>. Two warnings that matter more than the mechanism: the eye stays numb
  for <strong>10 to 20 minutes with no blink reflex</strong>, so it is unprotected; and
  <mark class="prof-highlight">do not write prescriptions for these</mark> &mdash; repeated use is
  toxic to the epithelium and delays healing.</p>

  <p><strong>Cycloplegics</strong> come in two flavours with the same endpoint.
  <strong>Antimuscarinics</strong> (atropine, cyclopentolate, tropicamide) competitively block
  muscarinic receptors &mdash; the exact opposite of pilocarpine &mdash; giving mydriasis.
  <strong>Sympathomimetics</strong> (phenylephrine) stimulate the dilator instead, and leave the
  pupil <strong>more reactive to light</strong>. Used diagnostically for fundoscopy, and
  therapeutically in <strong>uveitis to prevent synechiae and relieve ciliary spasm</strong>. Both
  cause photosensitivity and blurred vision.</p>

  <p><strong>Fluorescein</strong> reveals <strong>epithelial defects of the cornea and
  conjunctiva</strong>, for anterior segment staining and disclosing corneal injury. Adverse
  effects are hypersensitivity and burning.</p>

  <h3 class="sub" id="oph-admin">1.8 &middot; Objectives 9&ndash;10 &mdash; Administration, monitoring and patient education</h3>

  <div class="pearl"><strong>Before any medication goes in the eye: measure visual acuity.</strong>
  Document allergies and the date and result of the last eye exam. Repeat the acuity at
  <em>every</em> follow-up &mdash; and <mark class="prof-highlight">if it gets worse, that is an
  immediate ophthalmology consult</mark>. The baseline exists so that sentence can be acted on.</div>

  <p>The instillation sequence, with the step he marks as most important first:
  <strong>wash hands thoroughly</strong>; do not let the dropper touch anything; tilt the head back
  and pull down the lower lid to form a pocket; hold the dropper close without contact; one drop
  into the pocket; <strong>close the eyes, tilt forward and hold a finger over the lacrimal
  duct</strong>; keep the eyes closed <strong>two to three minutes</strong>; wipe and wash again.
  The finger on the punctum is the same trick as the silicone plug &mdash; keep the drug on the eye
  and out of the circulation.</p>

  <p><strong>Ointments</strong> suit <strong>children and poor compliers</strong>, because they work
  even if the drug only reaches the lashes. Squeeze a ribbon into the pocket; there is
  <strong>no need to cover the duct</strong>. Warn that <strong>vision blurs for about 20
  minutes</strong> &mdash; no driving until it clears.</p>

  <p><strong>Contact lenses</strong> come out. With conjunctivitis, discontinue wear; resume once
  the eye is uninflamed and <strong>free of discharge for 24 hours</strong>; and the lens itself is
  <strong>discarded or disinfected</strong> first. The eye makeup goes too.</p>

</section>
</main>'''


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap"')]
    tail = donor[donor.index("</main>") + len("</main>"):]

    # The donor's Test Yourself bank is Exam 1's -- acne, dermatology, the
    # autonomic drills -- and would sit in an ophthalmology guide answering
    # nothing. Located by the variable rather than by a guessed opening line,
    # which is what let it survive the first build.
    i = tail.find("TEST_YOURSELF")
    assert i != -1, "donor has no Test Yourself block; check the donor guide"
    ts = tail.rfind("<script", 0, i)
    te = tail.index("</script>", i) + len("</script>")
    assert ts != -1 and ts < i < te, "could not bound the Test Yourself script"
    tail = tail[:ts] + tail[te:]
    assert "TEST_YOURSELF" not in tail, "Test Yourself survived removal"

    # And the Word-copy link points at Exam 1's docx, which does not exist for
    # this guide at all.
    tail_and_head_fix = re.compile(r'\s*<link rel="alternate"[^>]*pharm-exam-1[^>]*>')

    head = re.sub(r"<title>.*?</title>",
                  "<title>Pharmacology I Exam 2 Study Guide &mdash; Ophthalmic Drugs</title>",
                  head, count=1, flags=re.S)
    head = re.sub(r'<header class="top">.*?</header>',
                  '<header class="top">\n  <h1>Pharmacology I Exam 2 Study Guide</h1>\n'
                  '  <p>Lecture 4 &middot; Ophthalmic Drugs &middot; Class of 2028</p>\n'
                  '  <p>Adam Wood, Pharm.D., DABAT</p>\n</header>',
                  head, count=1, flags=re.S)
    # No audio exists for this lecture; an empty audio dir breaks read-aloud.
    head = re.sub(r'\s*data-audio-dir="[^"]*"', "", head)
    head = tail_and_head_fix.sub("", head)

    html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + BODY + tail

    for tag in ("div", "section", "p", "h2", "h3", "ol", "ul", "li", "nav", "main", "strong", "em"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert "data-audio-dir" not in html, "audio dir survived"
    assert "TEST_YOURSELF" not in html, "Exam 1 question bank survived"
    assert "pharm-exam-1" not in html, "a link to Exam 1 survived"
    assert html.count("<li>") >= 10, "objectives missing"

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d subsections)"
          % (os.path.basename(OUT), len(html) // 1024, len(re.findall(r'<h3 class="sub"', html))))


if __name__ == "__main__":
    main()
