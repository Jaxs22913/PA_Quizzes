# Sections 2 and 3 for the Pharmacology I Exam 1 study guide.
# Kept in their own module so build_pharm_guide.py stays readable; it imports
# TOC_ADD, BODY_ADD and TY_ADD and splices them in.
#
# Instructional objectives are VERBATIM from the syllabus, including the ANS
# numbering quirk -- objective 7 introduces the drug categories and they then
# appear as top-level items 8 to 11 rather than 7a to 7d, exactly as the
# antivirals do in Lecture 1. Eleven printed numbers, seven real objectives.

TOC_ADD = '''  <a class="top-link" href="#dermmeds">2 &middot; Dermatology Medications</a>
  <a href="#dm-vehicles">2.1 Objectives 1 &amp; 4 &mdash; Vehicles, penetration and the depot effect</a>
  <a href="#dm-acne-why">2.2 Objectives 1&ndash;3 &mdash; Acne: four factors, one target</a>
  <a href="#dm-acne-drugs">2.3 Objectives 2&ndash;7 &mdash; The acne drugs</a>
  <a href="#dm-eczema">2.4 Objectives 3, 9 &amp; 10 &mdash; Atopic dermatitis and the steroid ladder</a>
  <a href="#dm-anti">2.5 Objectives 1&ndash;3 &mdash; Topical antibiotics, antifungals, antivirals</a>
  <a class="top-link" href="#ans">3 &middot; Autonomic Nervous System Pharmacology</a>
  <a href="#ans-wiring">3.1 Objectives 1&ndash;2 &mdash; How the system is wired</a>
  <a href="#ans-receptors">3.2 Objectives 3, 5 &amp; 6 &mdash; Transmitters and receptors</a>
  <a href="#ans-predict">3.3 Objective 4 &mdash; Predicting effects: the two pictures</a>
  <a href="#ans-cholag">3.4 Objectives 7&ndash;8 &mdash; Cholinergic agonists</a>
  <a href="#ans-cholant">3.5 Objectives 7 &amp; 9 &mdash; Cholinergic antagonists</a>
  <a href="#ans-adrag">3.6 Objectives 7 &amp; 10 &mdash; Adrenergic agonists</a>
  <a href="#ans-adrant">3.7 Objectives 7 &amp; 11 &mdash; Adrenergic antagonists</a>
'''

BODY_ADD = '''
<section class="deck" id="dermmeds">
  <h2 class="deck-title">2 &middot; Dermatology Medications</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify dermatologic drug classes and commonly prescribed dermatologic drugs.</li>
      <li>Describe the molecular mechanism of action of dermatologic drugs.</li>
      <li>Identify indications for commonly used dermatologic drugs.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of dermatologic drugs.</li>
      <li>Summarize side effects and toxic manifestations of dermatologic drugs.</li>
      <li>Describe adverse effects of dermatologic drugs.</li>
      <li>Identify contraindications for dermatologic drugs.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with dermatologic drugs.</li>
      <li>List commonly used protocols and patient monitoring for dermatologic drugs.</li>
      <li>Outline appropriate patient education for dermatologic drugs.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the course director</span>
  <mark class="prof-highlight">Dr. McInnis emailed the class before this exam: in past years students
  spent a lot of study time on mechanisms of action. That is important, <em>however</em> &mdash; study
  the drug more comprehensively.</mark> She named four things: <strong>indications discussed in
  lecture, patient education, side effects, and contraindications</strong>.
  <br><br>
  Four of the ten objectives above are exactly those four &mdash; 3, 5 and 6, 7, and 10 &mdash; while
  mechanism is a single objective. The syllabus was already weighted the way she is telling you to
  study. This guide and the quizzes follow that weighting: mechanism is covered, but it is not what
  most questions turn on.
  <br><br>
  Note the scope limit hiding in her wording: the indication that counts is the one
  <strong>discussed in lecture</strong>, not everything the drug is licensed for.</div>

  <h3 class="sub" id="dm-vehicles">2.1 &middot; Objectives 1 &amp; 4 &mdash; Vehicles, penetration and the depot effect</h3>
  <p>Topical dermatology is the one place where the vehicle is part of the prescription. Four
  variables change how much drug actually arrives.</p>
  <table>
    <tr><th>Variable</th><th>What it means</th></tr>
    <tr><td><strong>Regional variation</strong></td><td><strong>Scrotum, face, axilla and scalp</strong> are more permeable. The same tube does very different things in different places.</td></tr>
    <tr><td><strong>Concentration gradient</strong></td><td>More concentration means more transfer. The worked example is <strong>corticosteroid resistance overcome by raising the concentration</strong>.</td></tr>
    <tr><td><strong>Dosing schedule</strong></td><td>Skin acts as a <strong>reservoir</strong> &mdash; the depot effect &mdash; which may permit once daily dosing of a short acting drug.</td></tr>
    <tr><td><strong>Vehicle and occlusion</strong></td><td>The vehicle can dramatically alter permeability, may be therapeutic in itself, and <strong>occlusion increases efficacy</strong> &mdash; with the lecture raising toxicity in the same breath.</td></tr>
  </table>
  <div class="pearl"><strong>Match the vehicle to the lesion, not to the diagnosis.</strong>
  The range runs <strong>tinctures (most drying) &rarr; wet dressings &rarr; lotions &rarr; gels &rarr;
  aerosols &rarr; powders &rarr; pastes &rarr; creams &rarr; foams &rarr; ointments (least drying)</strong>.
  Oozing, vesiculation and crusting go to the drying end; scaling, lichenification and xerosis to the
  other. Two site rules follow: <strong>avoid ointment in intertriginous areas</strong>, and use a
  <strong>gel or foam on the scalp</strong>, where it foams well and leaves low residue.</div>

  <h3 class="sub" id="dm-acne-why">2.2 &middot; Objectives 1&ndash;3 &mdash; Acne: four factors, one target</h3>
  <p>Acne is multifactorial, and the lecture gives four major factors: <strong>increased sebum
  production</strong>, <strong>altered keratinization with hyperproliferation of the ductal
  epidermis</strong>, <strong>bacterial colonization with <em>Propionibacterium acnes</em></strong>,
  and <strong>release of inflammatory mediators</strong>. Every drug in the section attacks one of them.</p>
  <p>The cascade runs: pooled sebum creates anaerobic conditions &rarr; <em>P. acnes</em> proliferates
  &rarr; a T cell response drives inflammation; bacterial <strong>lipase hydrolyses triglycerides into
  free fatty acids</strong>, keratinization increases, microcomedones form, and cytokines generate pus.</p>
  <div class="pearl"><strong>The critical target is the microcomedone.</strong> Eliminating follicular
  occlusion arrests the cascade &mdash; which is why a comedolytic sits at the base of almost every
  regimen. Lesions divide into <strong>noninflammatory</strong> (open and closed comedones) and
  <strong>inflammatory</strong> (papulopustular and nodular); mild to moderate disease is topical,
  moderate to severe is systemic.</div>
  <div class="callout"><strong>Drug-induced acne.</strong> Systemic corticosteroids give pustular
  inflammation on the trunk two to six weeks in &mdash; <strong>not with hydrocortisone</strong> &mdash;
  and <strong>removal causes an initial worsening</strong> because inflammation increases. Warn the
  patient of that before they stop, or they will conclude the plan failed. Antiepileptics,
  tuberculostatics and lithium are also on the list.</div>

  <h3 class="sub" id="dm-acne-drugs">2.3 &middot; Objectives 2&ndash;7 &mdash; The acne drugs</h3>
  <table>
    <tr><th>Drug</th><th>Mechanism</th><th>What to tell the patient</th></tr>
    <tr><td><strong>Benzoyl peroxide</strong></td><td>Crosses the stratum corneum unchanged, then converts to <strong>benzoic acid</strong>, active against <em>P. acnes</em>; peeling and comedolytic</td><td><strong>It bleaches hair, clothing and bedding.</strong> Start low, once daily, and build up</td></tr>
    <tr><td><strong>Azelaic acid</strong></td><td>Not fully understood &mdash; antimicrobial, plus inhibiting testosterone to dihydrotestosterone conversion</td><td>Give it <strong>six to eight weeks</strong> of continuous use. Can cause <strong>hypopigmentation</strong></td></tr>
    <tr><td><strong>Topical retinoids</strong></td><td>Correct abnormal follicular keratinization, reduce <em>P. acnes</em>, reduce inflammation. <strong>First line for comedonal acne</strong></td><td><strong>Avoid in pregnancy.</strong> Photosensitivity and severe sunburn; tretinoin is <strong>photolabile</strong> so apply at night</td></tr>
    <tr><td><strong>Topical antibiotics</strong></td><td><strong>Clindamycin preferred</strong>; erythromycin losing efficacy to resistance</td><td>No systemic side effects</td></tr>
    <tr><td><strong>Isotretinoin</strong></td><td>Systemic retinoid, effective in one to three months</td><td><strong>Contraindicated in pregnancy and breastfeeding</strong>, iPledge; raised serum lipids; <strong>monitor for depression</strong></td></tr>
    <tr><td><strong>Tetracyclines</strong></td><td>Chelate calcium ions, preventing neutrophil and monocyte chemotaxis &mdash; an anti-inflammatory action separate from killing</td><td><strong>Contraindicated under 8 years and in pregnancy</strong></td></tr>
  </table>
  <div class="pearl"><strong>Two interactions worth holding onto.</strong>
  <strong>Benzoyl peroxide inactivates tretinoin</strong> &mdash; which is exactly why
  <strong>adapalene</strong>, stable in sunlight and stable with benzoyl peroxide, is singled out.
  And the retinoid family branches: <strong>tazarotene</strong> for acne and psoriasis,
  <strong>alitretinoin</strong> for Kaposi sarcoma, <strong>bexarotene</strong> for T-cell lymphoma.</div>
  <p><strong>Also in the section:</strong> salicylic acid (keratinolytic, few supporting studies);
  antiandrogens &mdash; spironolactone, and oral contraceptives in some women; intralesional steroids
  for individual nodules, with <strong>adrenal suppression from systemic absorption</strong> and
  <strong>local tissue atrophy</strong> as the costs.</p>
  <button class="test-yourself-btn" style="--acc:#9c5230" onclick="window.openTestYourself('Test yourself &mdash; Acne', TEST_YOURSELF.acne)">Test yourself! &rarr;</button>

  <h3 class="sub" id="dm-eczema">2.4 &middot; Objectives 3, 9 &amp; 10 &mdash; Atopic dermatitis and the steroid ladder</h3>
  <p>Atopic dermatitis is chronic inflammation with pruritus, part of the atopic triad with
  <strong>asthma and allergic rhino-conjunctivitis</strong>, and <strong>skin barrier dysfunction</strong>
  plays the major role. The major indicators are <strong>pruritus, rash in typical areas, chronic or
  repeated symptoms, and family history</strong>; raised immunoglobulin E and positive skin tests are
  minor ones.</p>
  <div class="pearl"><strong>Topical corticosteroids are the gold standard, and potency is chosen by
  site.</strong> <strong>Low potency</strong> for face, intertriginous areas and infants, and better for
  long-term use; <strong>medium</strong> for the body; for an exacerbation, <strong>medium to high for
  one to two weeks, then step down</strong>. Adverse effects track <strong>potency, duration, area
  covered and occlusiveness</strong> &mdash; ointment &gt; cream &gt; lotion.</div>
  <p>Local effects are skin atrophy, acne, rosacea and allergic dermatitis to the vehicle. Systemic
  effects &mdash; from a topical drug &mdash; are <strong>adrenal suppression, infections,
  hyperglycaemia, glaucoma, cataracts and growth retardation in children</strong>.</p>
  <p><strong>Topical immunomodulators</strong> (tacrolimus, pimecrolimus) inhibit activation of T cells,
  mast cells and keratinocytes. They are <strong>second line after topical steroids</strong>, carry a
  possible cancer risk, should be avoided in the immunosuppressed, and need counselling on
  <strong>burning</strong> and <strong>high SPF sunscreen</strong>.</p>

  <h3 class="sub" id="dm-anti">2.5 &middot; Objectives 1&ndash;3 &mdash; Topical antibiotics, antifungals, antivirals</h3>
  <table>
    <tr><th>Agent</th><th>Mechanism</th><th>Coverage / use</th></tr>
    <tr><td><strong>Bacitracin</strong></td><td>Peptide; prevents cell wall synthesis</td><td>Gram positives; <strong>no systemic toxicity</strong></td></tr>
    <tr><td><strong>Mupirocin</strong></td><td>Binds bacterial transfer RNA, stopping protein synthesis</td><td>Gram positive aerobes esp. MRSA; <strong>eliminates nasal carriage of <em>S. aureus</em></strong></td></tr>
    <tr><td><strong>Polymyxin B</strong></td><td>Interrupts the cytoplasmic membrane</td><td>Gram negatives; <strong>avoid on open or denuded skin in high doses &mdash; neuro- and nephrotoxicity</strong></td></tr>
    <tr><td><strong>Aminoglycosides</strong></td><td>Inhibit protein synthesis</td><td>Gram negatives; <strong>neomycin frequently sensitises</strong></td></tr>
    <tr><td><strong>Azoles</strong></td><td>Inhibit fungal cytochrome P450, preventing cell wall formation</td><td>Topical and vaginal; treatment is <strong>prolonged, two to three weeks</strong></td></tr>
    <tr><td><strong>Ciclopirox</strong></td><td>Blocks uptake of precursors at the fungal cell wall</td><td>Nail lacquer for onychomycosis &mdash; <strong>less than 12% effective</strong></td></tr>
    <tr><td><strong>Allylamines</strong></td><td>Inhibit ergosterol production</td><td>Naftifine, terbinafine</td></tr>
    <tr><td><strong>Tolnaftate / nystatin</strong></td><td>&mdash;</td><td>Tolnaftate has <strong>no Candida activity</strong>; nystatin is the candidal agent, <strong>no oral absorption</strong></td></tr>
    <tr><td><strong>Acyclovir, penciclovir</strong></td><td>Synthetic guanine analogues</td><td>Recurrent orolabial herpes simplex</td></tr>
    <tr><td><strong>Imiquimod</strong></td><td>Immunomodulator &mdash; interferon alpha, tumour necrosis factor alpha, interleukins</td><td>Warts, actinic keratoses, basal cell carcinoma</td></tr>
  </table>
  <div class="pearl"><strong>Imiquimod's adverse effect is the point, not a complication.</strong>
  Skin irritation occurs in virtually all patients, and <strong>the degree of inflammation parallels
  efficacy</strong>. A patient who reports redness, swelling and erosions is not failing therapy.</div>
  <button class="test-yourself-btn" style="--acc:#6b3524" onclick="window.openTestYourself('Test yourself &mdash; Topical anti-infectives', TEST_YOURSELF.topicals)">Test yourself! &rarr;</button>
</section>

<section class="deck" id="ans">
  <h2 class="deck-title">3 &middot; Principles of Autonomic Nervous System Pharmacology</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Recall the gross organization of the nervous system with particular attention to the sympathetic and parasympathetic divisions of the autonomic nervous system (ANS)</li>
      <li>Explain the mechanism whereby nerve impulses are carried from the brain to effector organs of the ANS and contrast this with the efferent mechanism of the somatic system</li>
      <li>Classify the neurotransmitters released and the types of receptors found within the ANS</li>
      <li>Predict the effects of adrenergic stimulation, adrenergic inhibition, cholinergic stimulation and cholinergic inhibition on effector organs of the ANS (i.e., &ldquo;fight or flight&rdquo; and &ldquo;rest and digest&rdquo;)</li>
      <li>Identify the location and effects of alpha-one, alpha-two, beta-one, and beta-two stimulation and inhibition on associated organs with regard to the sympathetic division of the ANS</li>
      <li>Summarize the synthesis, release, and subsequent destiny of neurotransmitters involved in ANS physiology</li>
      <li>Outline the mechanism of action, pharmacokinetics, indications, contraindications, and major adverse effects for the following drug categories:</li>
      <li>Cholinergic agonists</li>
      <li>Cholinergic antagonists</li>
      <li>Adrenergic agonists</li>
      <li>Adrenergic antagonists</li>
    </ol>
  </div>

  <div class="callout"><strong>The same numbering quirk as the antivirals.</strong> Objective 7
  introduces the drug categories and they then appear as top-level items <strong>8, 9, 10 and
  11</strong> rather than 7a to 7d. <strong>Eleven printed numbers are really seven objectives</strong>,
  and the four drug categories are one objective with four parts. The numbering is reproduced above
  exactly as the syllabus prints it.
  <br><br>
  Worth seeing the shape this gives the lecture: <strong>objectives 1 to 6 are physiology and receptor
  anatomy</strong>, and only objective 7 is drug-shaped. This is a physiology lecture with a drug
  section attached, not a drug lecture &mdash; which is why the receptor map below is worth more than
  any single agent.</div>

  <h3 class="sub" id="ans-wiring">3.1 &middot; Objectives 1&ndash;2 &mdash; How the system is wired</h3>
  <p>Nervous system &rarr; <strong>central</strong> (brain, spinal cord) and <strong>peripheral</strong>.
  Peripheral &rarr; <strong>afferent</strong> (to the centre; the example is sensing pressure in the
  carotid sinus and aortic arch) and <strong>efferent</strong> (away). Efferent &rarr;
  <strong>somatic</strong> (voluntary, muscle) and <strong>autonomic</strong> (involuntary). Autonomic
  &rarr; <strong>enteric, parasympathetic, sympathetic</strong>.</p>
  <div class="pearl"><strong>The contrast objective 2 asks for.</strong> An autonomic efferent pathway
  is <strong>two neurons</strong>: a <strong>preganglionic neuron within the central nervous
  system</strong> and a <strong>postganglionic neuron</strong> arising in a ganglion, generally
  nonmyelinated, ending on the effector organ. The somatic route does not relay that way. The
  <strong>enteric</strong> system is the third division &mdash; the &ldquo;brain of the gut&rdquo;,
  innervating gut, pancreas and gallbladder, <strong>functioning independently</strong> of the central
  nervous system while being modulated by the other two.</div>

  <h3 class="sub" id="ans-receptors">3.2 &middot; Objectives 3, 5 &amp; 6 &mdash; Transmitters and receptors</h3>
  <table>
    <tr><th>Receptor</th><th>Where</th><th>Note</th></tr>
    <tr><td><strong>M1</strong></td><td>Neurons, gastric parietal cells</td><td rowspan="3">Five subclasses; <strong>only M1, M2 and M3 are functionally characterised</strong></td></tr>
    <tr><td><strong>M2</strong></td><td>Neurons, cardiac cells, smooth muscle</td></tr>
    <tr><td><strong>M3</strong></td><td>Neurons, bladder, exocrine glands, smooth muscle</td></tr>
    <tr><td><strong>Nicotinic</strong></td><td>CNS, adrenal medulla, autonomic ganglia, neuromuscular junction</td><td>Five subunits, <strong>ligand-gated ion channel</strong>; two acetylcholine molecules open it to sodium</td></tr>
    <tr><td><strong>Alpha-one</strong></td><td><strong>Postsynaptic</strong>, on the effector organ</td><td rowspan="2">Alpha potency: <strong>epinephrine &ge; norepinephrine &gt;&gt; isoproterenol</strong></td></tr>
    <tr><td><strong>Alpha-two</strong></td><td><strong>Presynaptic</strong> nerve endings</td></tr>
    <tr><td><strong>Beta</strong></td><td>Cardiac (beta-one), airway and vessels (beta-two)</td><td>Beta potency: <strong>isoproterenol &gt; epinephrine &gt; norepinephrine</strong></td></tr>
  </table>
  <div class="pearl"><strong>Transmitter fate is where several drug classes act.</strong>
  Acetylcholine runs <strong>six steps</strong> &mdash; synthesis, storage, release, receptor binding,
  <strong>degradation by acetylcholinesterase</strong>, recycling of choline. Catecholamines are
  inactivated by <strong>catechol-O-methyltransferase postsynaptically and monoamine oxidase within
  the neuron</strong>; the noncatecholamines escape both, which is why they last longer and reach the
  brain. Nicotine is the oddity: it <strong>stimulates at low concentration and blocks at high</strong>.</div>

  <h3 class="sub" id="ans-predict">3.3 &middot; Objective 4 &mdash; Predicting effects: the two pictures</h3>
  <table>
    <tr><th>Muscarinic (DUMBBELS)</th><th>Nicotinic (MTWHF)</th><th>Anticholinergic</th></tr>
    <tr><td>Defecation, urination, miosis, bradycardia, bronchorrhoea, bronchospasm, emesis, lacrimation, salivation</td><td>Mydriasis, tachycardia, weakness, hypertension, fasciculations</td><td>Mad as a hatter, blind as a bat, red as a beet, dry as a bone, hot as Hades &mdash; plus constipation, urinary retention, tachycardia</td></tr>
  </table>
  <div class="pearl"><strong>Read the pupil and the heart first.</strong> Muscarinic stimulation gives
  <strong>small pupils and a slow heart</strong>; nicotinic and anticholinergic both give
  <strong>large pupils and a fast heart</strong>. Wet versus dry then separates the last two:
  muscarinic is wet, anticholinergic is bone dry.</div>

  <h3 class="sub" id="ans-cholag">3.4 &middot; Objectives 7&ndash;8 &mdash; Cholinergic agonists</h3>
  <p><strong>Direct-acting</strong> bind the receptor: choline esters (acetylcholine, carbachol,
  <strong>bethanechol</strong>) and the alkaloid <strong>pilocarpine</strong>.
  <strong>Indirect-acting</strong> raise acetylcholine by <strong>inhibiting acetylcholinesterase</strong>
  &mdash; the anticholinesterases.</p>
  <table>
    <tr><th>Agent</th><th>Use</th></tr>
    <tr><td><strong>Bethanechol</strong></td><td>Resists acetylcholinesterase, muscarinic only. Stimulates detrusor, relaxes trigone and sphincter &rarr; <strong>urinary retention</strong></td></tr>
    <tr><td><strong>Carbachol</strong></td><td>Muscarinic and nicotinic; <strong>glaucoma</strong>; releases epinephrine from the adrenal medulla</td></tr>
    <tr><td><strong>Pilocarpine</strong></td><td>Miosis and ciliary contraction &rarr; glaucoma; also <strong>xerostomia</strong></td></tr>
    <tr><td><strong>Edrophonium</strong></td><td>Short acting &mdash; <strong>diagnosing</strong> myasthenia gravis, reversing nondepolarizing blockade</td></tr>
    <tr><td><strong>Physostigmine</strong></td><td>Enters the brain &mdash; <strong>antidote for anticholinergic overdose</strong></td></tr>
    <tr><td><strong>Neostigmine, pyridostigmine</strong></td><td>Do not enter the brain; bladder and gut, blockade reversal, <strong>myasthenia gravis</strong> (pyridostigmine for chronic management)</td></tr>
    <tr><td><strong>Donepezil, rivastigmine, galantamine</strong></td><td>Alzheimer disease &mdash; a <strong>deficiency of central cholinergic neurons</strong></td></tr>
  </table>
  <div class="callout"><strong>Poisoning, both directions.</strong> Anticholinesterase insecticides are
  treated with atropine plus <strong>pralidoxime</strong>, which reactivates the inhibited enzyme but
  <strong>does not enter the brain</strong> and <strong>cannot overcome reversible inhibitors such as
  physostigmine</strong>. Anticholinergic overdose runs the other way and is treated with
  physostigmine. Getting the direction wrong doubles the poisoning.</div>
  <button class="test-yourself-btn" style="--acc:#c9a227" onclick="window.openTestYourself('Test yourself &mdash; Cholinergic drugs', TEST_YOURSELF.cholinergic)">Test yourself! &rarr;</button>

  <h3 class="sub" id="ans-cholant">3.5 &middot; Objectives 7 &amp; 9 &mdash; Cholinergic antagonists</h3>
  <p>Three classes: <strong>antimuscarinics</strong>, <strong>ganglionic blockers</strong> and
  <strong>neuromuscular blocking agents</strong>. Antimuscarinics do <strong>not</strong> block
  nicotinic receptors and have little action at ganglia or the neuromuscular junction.</p>
  <p><strong>Atropine</strong> &mdash; persistent <strong>mydriasis and cycloplegia</strong>; antispasmodic;
  <strong>bradycardia at low dose, tachycardia at higher dose</strong>, given in a code for bradycardia;
  greatest inhibitory effect on bronchial tissue, sweat and saliva; antidote for cholinesterase inhibitor
  insecticides and some mushrooms. <strong>Scopolamine</strong> has greater central action &mdash; motion
  sickness, short-term memory blocking &mdash; and the patch carries a real instruction: <strong>wash
  hands afterwards or blur your vision</strong>. Synthetics: <strong>ipratropium and tiotropium</strong>
  (inhaled, COPD), <strong>glycopyrrolate</strong> (secretions, drooling), the <strong>bladder
  agents</strong> (lower pressure, raise capacity), and <strong>glycopyrronium</strong> for axillary
  hyperhidrosis.</p>
  <div class="pearl"><strong>Neuromuscular blockade, two mechanisms.</strong>
  <strong>Nondepolarizing</strong> agents compete with acetylcholine, so <strong>more acetylcholine
  reverses them</strong> &mdash; neostigmine, pyridostigmine, edrophonium. Face and eye go first,
  <strong>diaphragm last</strong>, recovery in reverse. <strong>Succinylcholine</strong> is the only
  depolarizing agent: it acts <em>like</em> acetylcholine and is not destroyed, so it holds the receptor
  open &mdash; an anticholinesterase would make it worse. Rapid on, rapid off, used for rapid sequence
  intubation; the risk to know is <strong>malignant hyperthermia</strong> with halothane, treated by
  <strong>cooling and dantrolene</strong>.</div>

  <h3 class="sub" id="ans-adrag">3.6 &middot; Objectives 7 &amp; 10 &mdash; Adrenergic agonists</h3>
  <table>
    <tr><th>Agent</th><th>Receptors</th><th>Use / note</th></tr>
    <tr><td><strong>Epinephrine</strong></td><td>Alpha and beta &mdash; <strong>beta at low dose, alpha at high</strong></td><td>Anaphylaxis, cardiac arrest, acute bronchospasm; raises systolic, lowers diastolic; in local anaesthetic to <strong>prolong the block</strong></td></tr>
    <tr><td><strong>Norepinephrine</strong></td><td>Mostly alpha</td><td>Shock. <strong>Reflex bradycardia</strong> via baroreceptor; extravasation treated with <strong>phentolamine</strong></td></tr>
    <tr><td><strong>Isoproterenol</strong></td><td>Beta-one and beta-two</td><td>Stimulate the heart in an emergency</td></tr>
    <tr><td><strong>Dopamine</strong></td><td>Beta-one; alpha-one at very high dose; dopaminergic</td><td>Cardiogenic and septic shock; <strong>dilates renal and splanchnic arteries</strong></td></tr>
    <tr><td><strong>Dobutamine</strong></td><td>Beta-one</td><td>Acute heart failure; <strong>barely raises myocardial oxygen demand</strong>; caution in atrial fibrillation</td></tr>
    <tr><td><strong>Phenylephrine</strong></td><td>Alpha-one</td><td>Decongestant, septic shock; <strong>reflex bradycardia</strong></td></tr>
    <tr><td><strong>Oxymetazoline</strong></td><td>Alpha-one and two</td><td>Decongestant &mdash; <strong>rebound congestion beyond three days</strong></td></tr>
    <tr><td><strong>Clonidine</strong></td><td>Alpha-two</td><td>Hypertension, withdrawal syndromes; <strong>rebound hypertension if stopped abruptly</strong></td></tr>
    <tr><td><strong>Albuterol</strong></td><td>Beta-two</td><td>Asthma and COPD; tremor and anxiety</td></tr>
  </table>
  <div class="callout"><strong>Indirect and mixed.</strong> <strong>Amphetamine</strong> and
  <strong>cocaine</strong> raise norepinephrine by release or blocked reuptake; <strong>tyramine</strong>
  does the same and is normally destroyed by monoamine oxidase in the gut &mdash; which is why it is
  dangerous on a monoamine oxidase inhibitor, and why fermented cheese and wine matter.
  <strong>Ephedrine and pseudoephedrine</strong> are mixed: they release stored transmitter <em>and</em>
  act directly.</div>

  <h3 class="sub" id="ans-adrant">3.7 &middot; Objectives 7 &amp; 11 &mdash; Adrenergic antagonists</h3>
  <p><strong>Alpha blockers.</strong> <strong>Phenoxybenzamine</strong> is irreversible and
  noncompetitive &mdash; recovery needs new receptors, at least a day &mdash; and produces
  <strong>epinephrine reversal</strong>: vasoconstriction blocked, vasodilation left, so the net effect
  flips. <strong>Phentolamine</strong> is competitive and shorter. Both treat
  <strong>pheochromocytoma</strong>. The selective alpha-one blockers split by use:
  <strong>prazosin, terazosin, doxazosin</strong> for hypertension, <strong>tamsulosin, alfuzosin</strong>
  for benign prostatic hyperplasia &mdash; with <strong>first-dose syncope</strong> as the signature.</p>
  <div class="pearl"><strong>Propranolol is the one to know in detail.</strong> Nonselective, so
  beta-two blockade brings <strong>bronchoconstriction &mdash; contraindicated in asthma and chronic
  obstructive pulmonary disease</strong>. It <strong>masks the response to hypoglycaemia</strong>.
  Stopping it abruptly risks arrhythmia because <strong>beta receptors up-regulate</strong>. Uses run
  well beyond blood pressure: <strong>migraine prevention, hyperthyroidism, angina, and after
  myocardial infarction</strong>.</div>
  <p><strong>The rest of the class by property:</strong> <strong>timolol</strong> reduces aqueous humour
  for glaucoma; the <strong>selective beta-one</strong> agents suit impaired lungs but
  <strong>lose selectivity at higher doses</strong>; <strong>acebutolol and pindolol</strong> have
  intrinsic sympathomimetic activity; <strong>labetalol and carvedilol</strong> add alpha-one blockade,
  labetalol intravenously for hypertensive emergency and carvedilol for mortality in heart failure.
  <strong>Reserpine</strong> blocks transmitter uptake into vesicles; <strong>guanethidine</strong>
  blocks release from them.</p>
  <button class="test-yourself-btn" style="--acc:#9c5230" onclick="window.openTestYourself('Test yourself &mdash; Adrenergic drugs', TEST_YOURSELF.adrenergic)">Test yourself! &rarr;</button>
</section>
'''

TY_ADD = '''    acne: [
      {q:"Which is FIRST LINE for noninflammatory, comedonal acne?",
       choices:["Topical retinoid","Oral isotretinoin","Topical clindamycin","Oral doxycycline"],correct:0,
       explain:"The retinoid corrects the follicular keratinization that forms the microcomedone, which is the critical target."},
      {q:"A patient is prescribed benzoyl peroxide. What must you warn them about?",
       choices:["It bleaches hair, clothing and bedding","It stains the skin orange","It causes permanent hypopigmentation","It must never touch the face"],correct:0,
       explain:"A practical warning that prevents ruined clothes and an abandoned prescription."},
      {q:"Why is adapalene singled out from the other retinoids?",
       choices:["It is stable in sunlight and stable with benzoyl peroxide","It is safe in pregnancy","It works within one week","It has no irritant effect at all"],correct:0,
       explain:"Tretinoin is photolabile and is inactivated by benzoyl peroxide; adapalene is not, and tends to be less irritating."},
      {q:"Tetracyclines are contraindicated in which two groups?",
       choices:["Children under 8 and pregnant women","The elderly and diabetics","Asthmatics and smokers","Adolescents and athletes"],correct:0,
       explain:"Those two are named explicitly. Their acne role is partly anti-inflammatory, by chelating calcium and blocking chemotaxis."},
      {q:"Stopping a systemic corticosteroid that caused acne does what first?",
       choices:["Causes an initial worsening","Clears the eruption immediately","Converts pustules to comedones","Has no effect"],correct:0,
       explain:"Inflammation increases on withdrawal. Warn the patient in advance or they will think the plan failed."}
    ],
    topicals: [
      {q:"Which topical antibiotic eliminates nasal carriage of Staphylococcus aureus?",
       choices:["Mupirocin","Bacitracin","Polymyxin B","Neomycin"],correct:0,
       explain:"It binds bacterial transfer RNA and covers gram positive aerobes, especially MRSA."},
      {q:"Why avoid high-dose polymyxin B on denuded skin?",
       choices:["Risk of neurotoxicity and nephrotoxicity","It bleaches the skin","It causes photosensitivity","It inactivates other topicals"],correct:0,
       explain:"Losing the barrier turns a topical exposure into a systemic one."},
      {q:"A patient reports redness, swelling and erosions on imiquimod. What does that mean?",
       choices:["Expected — the degree of inflammation parallels efficacy","An allergy; stop the drug","Secondary infection","The dose is too low"],correct:0,
       explain:"Irritation occurs in virtually all patients and is intrinsic to how the drug works."},
      {q:"Which antifungal has NO Candida activity?",
       choices:["Tolnaftate","Nystatin","Clotrimazole","Ciclopirox"],correct:0,
       explain:"Nystatin is the candidal agent; tolnaftate's gap is explicitly flagged."},
      {q:"How effective is the ciclopirox nail lacquer for onychomycosis?",
       choices:["Less than 12%","About half","Around 80%","Curative in most"],correct:0,
       explain:"Worth saying up front before committing a patient to months of treatment."}
    ],
    cholinergic: [
      {q:"A patient has diarrhoea, urination, miosis, bradycardia, bronchorrhoea and salivation. Which picture?",
       choices:["Muscarinic stimulation","Nicotinic stimulation","Anticholinergic toxicity","Ganglionic blockade"],correct:0,
       explain:"DUMBBELS. Small pupils and a slow heart, and wet throughout."},
      {q:"Which agent is used to DIAGNOSE myasthenia gravis?",
       choices:["Edrophonium","Pyridostigmine","Physostigmine","Neostigmine"],correct:0,
       explain:"Short acting, so it suits a diagnostic test. Pyridostigmine handles chronic management."},
      {q:"Physostigmine is the antidote for what?",
       choices:["Anticholinergic overdose","Organophosphate insecticide","Beta blocker overdose","Malignant hyperthermia"],correct:0,
       explain:"It crosses into the brain. Giving it for an anticholinesterase poisoning would deepen the poisoning."},
      {q:"What limits pralidoxime?",
       choices:["It does not enter the brain and cannot overcome reversible inhibitors","It works only in children","It must be given orally","It reverses only nicotinic signs"],correct:0,
       explain:"It reactivates inhibited acetylcholinesterase within those two limits."},
      {q:"Why can neostigmine reverse a nondepolarizing blockade but not succinylcholine?",
       choices:["The nondepolarizing block is competitive, so more acetylcholine outcompetes it","Succinylcholine is not a receptor drug","Neostigmine only works at muscarinic sites","Succinylcholine is given intravenously"],correct:0,
       explain:"Succinylcholine acts like acetylcholine, so adding more would prolong the block rather than break it."}
    ],
    adrenergic: [
      {q:"Epinephrine given to a patient on a beta blocker does what?",
       choices:["Leaves alpha effects unopposed, raising blood pressure","Abolishes all effects","Lowers blood pressure sharply","Nothing clinically important"],correct:0,
       explain:"Blocking the vasodilating beta side leaves only vasoconstriction."},
      {q:"Norepinephrine extravasates and the skin blanches. What is given?",
       choices:["Phentolamine","Atropine","Dantrolene","Pralidoxime"],correct:0,
       explain:"An alpha blocker reverses the intense local vasoconstriction before the skin sloughs."},
      {q:"Which receptor does clonidine act on, and where?",
       choices:["Alpha-two, presynaptic and central, reducing sympathetic outflow","Alpha-one on vessels","Beta-one in the heart","Beta-two in the airway"],correct:0,
       explain:"An agonist that lowers blood pressure, by damping sympathetic drive rather than blocking the vessel."},
      {q:"Why is propranolol contraindicated in asthma?",
       choices:["Beta-two blockade causes bronchoconstriction","It raises pulmonary pressure","It thickens secretions","It blocks alpha receptors in the airway"],correct:0,
       explain:"Nonselective blockade removes the beta-two bronchodilation the airway depends on."},
      {q:"Why is tyramine dangerous on a monoamine oxidase inhibitor?",
       choices:["That enzyme normally destroys it in the gut","It becomes a direct alpha agonist","It is converted to amphetamine","It blocks reuptake"],correct:0,
       explain:"Blocking the enzyme lets it reach the terminal and displace stored norepinephrine, with serious vasopressor effects."}
    ],'''
