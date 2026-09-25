# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 study guide -- section 2, Lecture 5 (ENT drugs).

Imported by build_pharm_e2_guide.py; holds only this lecture's table-of-contents
entries and body HTML.

SOURCE: "ENT Jax Pharmacology.pptx" (64 slides, Adam Wood). Every fact below is
on a slide. Two slides carry their content ONLY in embedded Word objects that a
plain text extraction misses entirely ([[image_only_slides]]): slide 28 (the
histamine receptor table) and slide 37 (the first- against second-generation
antihistamine table). Their text was pulled with textutil from the OLE blobs and
is used below. Slide 41 is two pictures (glucocorticoid actions on inflammatory
and structural cells; the receptor complex blocking NF-kappa-B), described in
prose rather than reproduced -- one is a Medscape figure and the repo is public.
Slide 53 is a packaging photograph of Sudafed PE; its one teachable fact is that
phenylephrine is the pseudoephedrine-free decongestant.

NO STARS in this section. The ENT recording has not been analyzed for emphasis,
so nothing here is marked as professor-emphasized; marks would be guesses.

Scope: no doses (Dr. Wood's standing rule). Indications and the adverse effects
of specific agents ARE examinable (Jaxon, 2026-09-18; see pharm_ent_pool_anti.py).
The aspirin dose-effect table is taught as a ladder of effects without grams.
"""

TOC = '''  <a class="top-link" href="#ent">2 &middot; Ear, Nose and Throat Drugs</a>
  <a href="#ent-abx">2.1 Objectives 1&ndash;3 &mdash; Antibiotics for ear, sinus and throat infections</a>
  <a href="#ent-otic">2.2 Objectives 1&ndash;7 &mdash; Otic antibiotics</a>
  <a href="#ent-antifungal">2.3 Objectives 1&ndash;8 &mdash; Antifungals</a>
  <a href="#ent-aspirin">2.4 Objectives 2&ndash;7 &mdash; Aspirin and Reye syndrome</a>
  <a href="#ent-nsaid">2.5 Objectives 1&ndash;8 &mdash; Ibuprofen, naproxen and acetaminophen</a>
  <a href="#ent-histamine">2.6 Objectives 1&ndash;6 &mdash; Histamine and the H1 antagonists</a>
  <a href="#ent-steroid">2.7 Objectives 1&ndash;8 &mdash; Corticosteroids</a>
  <a href="#ent-decongest">2.8 Objectives 1&ndash;8 &mdash; Decongestants</a>
  <a href="#ent-cough">2.9 Objectives 1&ndash;7 &mdash; Cough: antitussives, expectorants and mucolytics</a>
  <a href="#ent-edu">2.10 Objectives 9&ndash;10 &mdash; Protocols, monitoring and patient education</a>'''

BODY = '''
<section class="deck" id="ent">
  <h2 class="deck-title">2 &middot; Ear, Nose and Throat Drugs</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify ENT drug classes and commonly prescribed ENT drugs.</li>
      <li>Describe the molecular mechanism of action of ENT drugs.</li>
      <li>Identify indications for commonly used ENT drugs.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of ENT drugs.</li>
      <li>Summarize side effects and toxic manifestations of ENT drugs.</li>
      <li>Describe adverse effects of ENT drugs.</li>
      <li>Identify contraindications for ENT drugs.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with ENT drugs.</li>
      <li>List commonly used protocols and patient monitoring for ENT drugs.</li>
      <li>Outline appropriate patient education for ENT drugs.</li>
    </ol>
  </div>

  <div class="callout"><strong>How this lecture is examined.</strong> ENT (ear, nose and throat)
  drugs are taught agent by agent, most on a one-slide card: class, mechanism, indications, side
  effects, interactions, contraindications, patient education. <strong>Doses are not
  examined</strong>, so the milligram figures on those cards are left out of this guide.
  <strong>Indications and the adverse effects that belong to a specific agent are
  examined</strong> &mdash; which antibiotic replaces amoxicillin in penicillin allergy, which
  otic drop is unsafe through a perforated eardrum, which antihistamine sedates. Two slides
  (28 and 37) hold their tables inside embedded documents that do not show up in a text copy of
  the deck; both tables are reproduced below.</div>

  <h3 class="sub" id="ent-abx">2.1 &middot; Objectives 1&ndash;3 &mdash; Antibiotics for ear, sinus and throat infections</h3>

  <p>Three infections share one set of bacteria and one first-line drug. <strong>Acute otitis
  media</strong> is caused by viruses more often than bacteria; when bacteria are involved they are
  <strong><em>Streptococcus pneumoniae</em>, <em>Haemophilus influenzae</em> and <em>Moraxella
  catarrhalis</em></strong>, in that order of frequency, and the mix is shifting with
  vaccination. <strong>Acute bacterial rhinosinusitis</strong> has the same three, plus
  <em>Streptococcus pyogenes</em>, <em>Staphylococcus aureus</em> and gram-negative bacilli.
  <strong>Acute pharyngitis</strong> is mainly viral; <strong>group A beta-hemolytic
  <em>Streptococcus</em></strong> accounts for 15 to 30% of cases.</p>

  <table>
    <tr><th>Infection</th><th>First line</th><th>Step up / failure</th><th>Penicillin allergy</th></tr>
    <tr><td>Acute otitis media</td><td><strong>High-dose amoxicillin</strong> &mdash; the higher dose overcomes <em>S. pneumoniae</em> resistance</td><td>Amoxicillin-clavulanate for severe or resistant disease, or if antibiotics were taken in the previous month. <strong>No improvement in 3 days</strong> = failed therapy: amoxicillin-clavulanate or a third-generation cephalosporin (cefdinir) if no antibiotics in the past 3 months; <strong>ceftriaxone</strong> intramuscular or intravenous if that fails or oral drugs are not tolerated</td><td>Cefdinir or azithromycin &mdash; but up to 50% of <em>S. pneumoniae</em> is macrolide-resistant</td></tr>
    <tr><td>Acute bacterial rhinosinusitis</td><td><strong>Amoxicillin-clavulanate</strong> &mdash; because beta-lactamase-producing <em>H. influenzae</em> is common</td><td>Saline irrigation can help alongside</td><td><strong>Clindamycin plus cefixime</strong>, or <strong>levofloxacin</strong></td></tr>
    <tr><td>Acute pharyngitis (group A strep)</td><td><strong>Amoxicillin</strong> for 10 days, or <strong>benzathine penicillin G</strong> as a single intramuscular injection</td><td>&mdash;</td><td>Cephalexin, clindamycin or azithromycin</td></tr>
  </table>

  <div class="pearl"><strong>Two decisions that come before the drug.</strong> Sinusitis is only
  called bacterial when symptoms have lasted <strong>more than 10 days</strong> or are
  <strong>worsening</strong> &mdash; before that it is presumed viral and an antibiotic helps no
  one. In pharyngitis the goal of treatment is to <strong>prevent acute rheumatic fever and
  suppurative complications</strong>, and a <strong>rapid strep test</strong> is used to stop
  over-prescribing to the viral majority.</div>

  <p>Each amoxicillin substitution has a reason worth being able to say out loud. Clavulanate is
  added when a beta-lactamase producer is likely (sinusitis, recent antibiotics, treatment
  failure). The macrolide is an allergy option in otitis media, not an equal &mdash; half the
  pneumococci may resist it. Ceftriaxone is the escalation because it is parenteral.</p>

  <h3 class="sub" id="ent-otic">2.2 &middot; Objectives 1&ndash;7 &mdash; Otic antibiotics</h3>

  <p>Ear drops usually <strong>mix an anti-infective with a glucocorticoid</strong>: the antibiotic
  inhibits bacterial growth and the steroid decreases production of inflammatory cytokines. The
  agents on the slide are <strong>ciprofloxacin</strong>, <strong>ciprofloxacin/dexamethasone
  (Ciprodex)</strong>, <strong>neomycin, polymyxin B and hydrocortisone (Cortisporin)</strong>,
  and <strong>ofloxacin</strong>. Indications: otitis media and otitis externa.</p>

  <table>
    <tr><th>Agent</th><th>The fact that names it</th></tr>
    <tr><td>Neomycin</td><td>Chance of <strong>hypersensitivity</strong></td></tr>
    <tr><td>Polymyxin B</td><td><strong>Not for a ruptured tympanic membrane or tubes in place</strong> &mdash; cochlear damage and hearing loss</td></tr>
    <tr><td>Ciprofloxacin/dexamethasone</td><td><strong>Expensive</strong>; the alternative is <strong>ofloxacin plus dexamethasone ophthalmic</strong> drops</td></tr>
  </table>

  <div class="callout"><strong>The contraindication to hold.</strong> Before any drop goes in an
  ear, ask whether the eardrum is intact. Through a perforation or a tympanostomy tube the drug
  reaches the middle and inner ear, and polymyxin B is the one named as ototoxic there.</div>

  <h3 class="sub" id="ent-antifungal">2.3 &middot; Objectives 1&ndash;8 &mdash; Antifungals</h3>

  <p>The two antifungals are opposites in exposure. <strong>Nystatin</strong> oral suspension is a
  <strong>nonabsorbable</strong> antifungal: it binds sterols in the fungal cell membrane and
  increases its permeability, stays in the mouth and gut, and so causes nothing worse than
  diarrhea, nausea, stomach pain and vomiting. Its indication is <strong>oral candidiasis</strong>,
  and the slide names three settings that produce it: <strong>inhaled steroids, HIV/AIDS and
  chemotherapy</strong>.</p>

  <p><strong>Ketoconazole</strong> is systemic, for <strong>systemic fungal infections</strong>,
  and its mechanism is given as altering fungal cell wall permeability by inhibiting a
  cytochrome P450 enzyme. That same class of enzyme is why it is dangerous: it is a
  <strong>CYP3A4 (cytochrome P450 3A4) inhibitor</strong>, so it raises levels of other drugs.
  Its own adverse effects are <strong>QTc prolongation</strong>, hyperlipidemia, orthostatic
  hypotension, and the liver list &mdash; <strong>hepatitis, abnormal liver function tests,
  cirrhosis and hepatic failure</strong>.</p>

  <div class="pearl"><strong>Absorption decides the risk (Objective 4).</strong> Thrush after an
  inhaled steroid is treated with the drug that is <em>not</em> absorbed, because it only needs
  to reach the mucosa. Ketoconazole's hepatic and cardiac toxicity and its drug interactions all
  follow from the fact that it reaches the circulation.</div>

  <h3 class="sub" id="ent-aspirin">2.4 &middot; Objectives 2&ndash;7 &mdash; Aspirin and Reye syndrome</h3>

  <p><strong>Aspirin (acetylsalicylic acid)</strong> is absorbed orally, conjugated in the liver and
  excreted by the kidneys. It is an <strong>irreversible, noncompetitive inhibitor of
  platelets</strong> and is <strong>non-selective for cyclooxygenase-1 and
  cyclooxygenase-2</strong>. Irreversible is the word to hold: the platelet it touches stays
  inhibited, which is where both its antiplatelet use and its bleeding risk come from.</p>

  <p>Slide 16 is a dose-effect table. The doses themselves are not examined; the <strong>ladder
  of effects</strong> it describes is. As exposure rises, the same drug is first an
  <strong>antiplatelet</strong> (complication: bleeding), then an <strong>antipyretic and
  analgesic</strong> (bleeding, gastrointestinal upset, nausea, hypersensitivity), then an
  <strong>anti-inflammatory</strong> &mdash; where <strong>tinnitus</strong> appears &mdash; and
  finally toxic, as <strong>salicylism</strong>: hyperventilation and alkalosis, then fever,
  dehydration and metabolic acidosis, then shock, coma, respiratory and renal failure, and
  death.</p>

  <table>
    <tr><th>Contraindication</th><th>Why</th></tr>
    <tr><td>Bleeding disorders</td><td>Irreversible platelet inhibition</td></tr>
    <tr><td>Pregnancy</td><td>Contraindicated, although very low doses may benefit hypertensive disorders of pregnancy (pre-eclampsia)</td></tr>
    <tr><td><strong>Children with fever from a viral illness</strong> (chickenpox, influenza)</td><td><strong>Increased incidence of Reye syndrome</strong></td></tr>
  </table>

  <div class="callout"><strong>Reye syndrome (fatty liver encephalopathy).</strong> Children under
  15, with a <strong>mortality of 50%</strong>. It follows an upper respiratory infection,
  influenza or chickenpox, and presents with <strong>vomiting, progressive central nervous system
  damage, hepatic injury and hypoglycemia</strong>. The pathology is fatty change in the liver and
  renal tubules, cerebral edema, and mitochondrial dysfunction in brain, liver and muscle. It
  runs through five stages: (I) rash on hands and feet, vomiting, high fever, lethargy;
  (II) encephalitis, hyperventilation, fatty liver; (III) coma and cerebral edema; (IV) deeper
  coma, fixed dilated pupils, hepatic dysfunction; (V) seizures, multiple organ failure,
  death.</div>

  <h3 class="sub" id="ent-nsaid">2.5 &middot; Objectives 1&ndash;8 &mdash; Ibuprofen, naproxen and acetaminophen</h3>

  <p><strong>Ibuprofen (Motrin, Advil)</strong> is an NSAID (nonsteroidal anti-inflammatory drug):
  anti-inflammatory, analgesic and antipyretic. It <strong>reversibly</strong> inhibits
  cyclooxygenase-1 and -2, decreasing prostaglandin synthesis &mdash; the contrast with aspirin's
  irreversible block. Indication: relief of mild to moderate pain. Adverse effects fall in three
  places: the stomach (<strong>gastric or duodenal ulcers, perforation, bleeding</strong>), fluid
  (<strong>edema and fluid retention</strong>) and the kidney (<strong>acute renal failure,
  decreased creatinine clearance</strong>). <strong>Naproxen (Aleve)</strong> is the other
  over-the-counter NSAID: a longer half-life, so less frequent dosing.</p>

  <table>
    <tr><th>Ibuprofen interaction</th><th>Result</th></tr>
    <tr><td>ACE (angiotensin-converting enzyme) inhibitors</td><td>Decreases their effect</td></tr>
    <tr><td>Diuretics</td><td>Watch for renal failure</td></tr>
    <tr><td>Lithium</td><td>Decreases lithium secretion</td></tr>
    <tr><td>Methotrexate</td><td>Decreases its secretion, producing <strong>toxic levels</strong></td></tr>
    <tr><td>Anticoagulants</td><td>Prolongs prothrombin time, with <strong>serious gastrointestinal bleeds</strong></td></tr>
  </table>

  <p>Ibuprofen contraindications: allergy to the product; it <strong>may exacerbate
  asthma</strong>; <strong>avoid in children under 6 months</strong>; and a past history of stomach
  ulcer or perforation, or renal dysfunction.</p>

  <p><strong>Acetaminophen (Tylenol; acetyl-para-aminophenol)</strong> is an analgesic and
  antipyretic &mdash; <em>not</em> an anti-inflammatory &mdash; whose mechanism is <strong>not fully
  elucidated</strong>. Indications: pain, and fever above 100&nbsp;&deg;F. It is <strong>very well
  tolerated, with no notable side effects at therapeutic doses</strong>. The one interaction:
  <strong>chronic alcohol use with acetaminophen increases the risk of liver damage</strong>. Its
  only listed contraindication is allergy. Its antidote, N-acetylcysteine, reappears in 2.9 as a
  mucolytic.</p>

  <h3 class="sub" id="ent-histamine">2.6 &middot; Objectives 1&ndash;6 &mdash; Histamine and the H1 antagonists</h3>

  <p>Histamine is released from immune cells and produces the <strong>triple response</strong>:
  <strong>redness</strong> (direct vasodilation), <strong>wheal</strong> (edema from post-capillary
  permeability) and <strong>flare</strong> (redness around the primary insult, from reflex axonal
  vasodilation).</p>

  <table>
    <tr><th>Tissue</th><th>Receptor</th><th>Action</th></tr>
    <tr><td>Vascular</td><td>H1 and H2</td><td>&darr; total peripheral resistance</td></tr>
    <tr><td>Postcapillary venules</td><td>H1</td><td>&uarr; permeability</td></tr>
    <tr><td>Heart</td><td>H1 / H2</td><td>&uarr; heart rate / &uarr; force of contraction</td></tr>
    <tr><td>Bronchiolar smooth muscle</td><td>H1 / H2</td><td>Contraction / relaxation</td></tr>
    <tr><td>Gastrointestinal smooth muscle</td><td>H1</td><td>Constriction</td></tr>
    <tr><td>Gastrointestinal mucosa</td><td>H2</td><td>Gastric acid and pepsin secretion</td></tr>
    <tr><td>Cutaneous nerve endings</td><td>H1</td><td>Pain and itch</td></tr>
  </table>

  <p>The receptor mechanisms (Objective 2): <strong>H1</strong> activates phospholipase C (inositol
  trisphosphate and diacylglycerol raise calcium, contracting venules, so post-capillary
  permeability rises); causes rapid, short vasodilation through endothelial nitric oxide; raises
  nasal, bronchial and gastrointestinal mucus; raises smooth muscle tone; stimulates sensory nerve
  endings; and bronchoconstricts. <strong>H2</strong> activates adenylate cyclase (raising cyclic
  AMP), raises gastric acid, gives slow, long vasodilation, raises cardiac contractility, raises
  mucus and lowers smooth muscle tone.</p>

  <p><strong>H1 antagonists</strong> reverse the H1 list: they block gastrointestinal and bronchial
  smooth muscle contraction and rapid vasodilation, and decrease nasal and bronchial secretions,
  edema and vascular permeability, hives and itch. Indications: <strong>allergic reactions</strong>
  (allergic rhinitis, urticaria, insect bites, drug hypersensitivity); <strong>motion sickness,
  nausea and vestibular disturbances</strong>; <strong>over-the-counter sleep remedies</strong>;
  and an <strong>adjuvant role in anaphylaxis</strong> &mdash; adjuvant, not the treatment.</p>

  <div class="pearl"><strong>One distinction explains most of the class.</strong> <strong>First
  generation</strong> agents enter the central nervous system and act on other receptor systems
  too &mdash; <strong>antiemetic, antimuscarinic and antiserotonergic</strong>. So they sedate
  (the <strong>major side effect</strong>, additive with alcohol and other central depressants,
  and the reason doxylamine is sold as a sleep aid), they dry secretions, they treat motion
  sickness, and at higher doses &mdash; especially in children, and in overdose &mdash; they cause
  <strong>restlessness and excitation</strong>. <strong>Second generation</strong> agents do not
  enter the central nervous system, so they cause <strong>much less sedation</strong>.
  <strong>Promethazine</strong> has the strongest antimuscarinic action, especially for motion
  sickness.</div>

  <table>
    <tr><th>Agent</th><th>Sedation</th><th>Antiemetic</th><th>Anticholinergic</th></tr>
    <tr><td colspan="4"><strong>First generation</strong></td></tr>
    <tr><td>Chlorpheniramine (Chlor-Trimeton)</td><td>Medium</td><td>None</td><td>Medium</td></tr>
    <tr><td>Dimenhydrinate (Dramamine)</td><td>High</td><td>Medium</td><td>High</td></tr>
    <tr><td>Diphenhydramine (Benadryl)</td><td>High</td><td>Medium</td><td>High</td></tr>
    <tr><td>Hydroxyzine (Atarax)</td><td>High</td><td>High</td><td>Medium</td></tr>
    <tr><td>Meclizine (Antivert)</td><td>Medium</td><td>High</td><td>Medium</td></tr>
    <tr><td>Promethazine (Phenergan)</td><td>High</td><td>High</td><td>High</td></tr>
    <tr><td colspan="4"><strong>Second generation</strong></td></tr>
    <tr><td>Cetirizine (Zyrtec)</td><td>Low</td><td>None</td><td>Very low</td></tr>
    <tr><td>Fexofenadine (Allegra)</td><td>Very low</td><td>None</td><td>Very low</td></tr>
    <tr><td>Loratadine (Claritin)</td><td>Very low</td><td>None</td><td>Very low</td></tr>
    <tr><td colspan="4"><strong>Intranasal</strong></td></tr>
    <tr><td>Azelastine (Astelin)</td><td>Low</td><td>None</td><td>Very low</td></tr>
  </table>

  <p>Class adverse effects: <strong>sedation</strong>; gastrointestinal disturbance; the
  <strong>antimuscarinic set &mdash; dry mouth, urinary retention, blurred vision</strong>; and,
  with topical use, hypersensitivity (dermatitis, photosensitivity).
  <strong>Azelastine (Astelin)</strong> is the H1 antagonist given as a nasal spray, for
  <strong>allergic and vasomotor rhinitis</strong>; its side effects are a <strong>bitter
  taste</strong> and <strong>epistaxis</strong>.</p>

  <h3 class="sub" id="ent-steroid">2.7 &middot; Objectives 1&ndash;8 &mdash; Corticosteroids</h3>

  <p>Slide 41 shows what a glucocorticoid does, cell by cell. On <strong>inflammatory
  cells</strong> it reduces numbers of eosinophils (by apoptosis), mast cells and dendritic cells,
  and cuts cytokines from T lymphocytes and macrophages. On <strong>structural cells</strong> it
  reduces cytokine mediators from epithelium, reduces endothelial leak, reduces mucus secretion,
  and on smooth muscle <strong>increases beta-2 receptors</strong> while reducing cytokines. The
  molecular step beneath all of it: the steroid binds its receptor, the complex enters the
  nucleus and <strong>blocks the inflammatory transcription factor NF-kappa-B, so cytokine
  synthesis is inhibited</strong>.</p>

  <p><strong>Nasal corticosteroids</strong> &mdash; beclomethasone (Beconase AQ), budesonide
  (Rhinocort, over the counter), flunisolide (Nasalide), <strong>fluticasone (Flonase, over the
  counter &mdash; not Flovent)</strong>, mometasone (Nasonex), triamcinolone (Nasacort). Many have
  inhaled versions for asthma, so do not mix up the names. Indications: <strong>allergic and
  vasomotor rhinitis</strong>. Side effects are local: <strong>epistaxis, septal perforation,
  unpleasant taste</strong>. No interactions are listed.</p>

  <table>
    <tr><th></th><th>Dexamethasone (Decadron)</th><th>Prednisone (Deltasone) / prednisolone (Orapred, the liquid)</th></tr>
    <tr><td>Class</td><td>Synthetic adrenocortical steroid</td><td>Glucocorticoid</td></tr>
    <tr><td>Indications</td><td>Allergic rhinitis, drug hypersensitivity reactions</td><td>Allergic rhinitis, allergic conjunctivitis, drug hypersensitivity reactions</td></tr>
    <tr><td>Side effects</td><td colspan="2">Sodium and fluid retention, heart failure, hypertension, <strong>potassium loss</strong>; glucose intolerance; cushingoid features (and hirsutism with dexamethasone); <strong>tendon rupture</strong> (and pathologic fractures of long bones with prednisone); the eye &mdash; <strong>cataracts, raised intraocular pressure, glaucoma, exophthalmos</strong> (and papilledema with dexamethasone); raised liver enzymes with prednisone; <strong>a weakened immune system</strong></td></tr>
    <tr><td>Contraindications</td><td><strong>Systemic fungal infections</strong></td><td>Allergy; <strong>infections, especially fungal</strong></td></tr>
  </table>

  <p>Dexamethasone interactions all run through potassium, glucose or clearance: with a
  <strong>diuretic</strong>, hypokalemia; with <strong>digoxin</strong>, a higher risk of
  arrhythmia <em>because</em> of that hypokalemia; <strong>macrolides decrease its
  clearance</strong>; and it <strong>decreases the effect of antidiabetic drugs</strong>.</p>

  <h3 class="sub" id="ent-decongest">2.8 &middot; Objectives 1&ndash;8 &mdash; Decongestants</h3>

  <p>All three decongestants are <strong>alpha agonists that constrict blood vessels in the nasal
  mucosa</strong>. What separates them is the route and the price.</p>

  <table>
    <tr><th>Agent</th><th>Route and use</th><th>Adverse effects and interactions</th></tr>
    <tr><td><strong>Oxymetazoline (Afrin)</strong></td><td>Nasal spray, nasal congestion; <strong>3 to 5 days maximum</strong></td><td>Beyond 3 to 5 days, <strong>rebound rhinitis (rhinitis medicamentosa)</strong>; hypertension. Interacts with <strong>monoamine oxidase inhibitors and antidepressants</strong></td></tr>
    <tr><td><strong>Pseudoephedrine (Sudafed)</strong></td><td>Oral; nasal congestion from a cold, hay fever or allergy; sinus congestion; <strong>eustachian tube dysfunction from a viral infection</strong></td><td><strong>Tachycardia, hypertension, headache</strong>. <strong>Decreases the effect of antihypertensives</strong></td></tr>
    <tr><td>Phenylephrine (Sudafed PE)</td><td>Oral; the <strong>pseudoephedrine-free</strong> nasal decongestant</td><td>&mdash;</td></tr>
  </table>

  <div class="pearl"><strong>Rebound is a theme across Exam 2.</strong> The topical nasal
  decongestant has the same trap as the vasoconstrictor eye drops in section 1: used past its limit,
  it produces the congestion it was bought to treat, and the patient reaches for the bottle
  again.</div>

  <h3 class="sub" id="ent-cough">2.9 &middot; Objectives 1&ndash;7 &mdash; Cough: antitussives, expectorants and mucolytics</h3>

  <p>Cough receptors in the respiratory tract respond to chemical and mechanical irritants; the
  impulse travels a brainstem reflex pathway to the <strong>cough center in the medulla
  oblongata</strong>; then deep inspiration, glottis closure and contraction of chest wall,
  diaphragm and abdominal wall. Complications are insomnia, exhaustion, musculoskeletal pain and
  hoarseness, and less often dysrhythmias, syncope, stroke and rib fractures. Treatment goals:
  <strong>reduce the number and severity of episodes, and prevent complications</strong>.</p>

  <div class="pearl"><strong>The two antitussives work at opposite ends of the reflex.</strong>
  <strong>Benzonatate (Tessalon)</strong> anesthetizes the <strong>stretch receptors in the
  lungs</strong>, where the cough starts. <strong>Dextromethorphan (Robitussin, Delsym)</strong>,
  related to codeine, suppresses the <strong>medullary cough center through sigma receptor
  activation</strong>, where it is organized.</div>

  <table>
    <tr><th>Agent</th><th>Indication</th><th>Side effects</th><th>Contraindication / interaction</th></tr>
    <tr><td>Benzonatate</td><td>Symptomatic relief of <strong>non-productive</strong> cough</td><td><strong>Local anesthesia of the mouth if the capsule is chewed</strong></td><td>Allergy to it or related products (tetracaine)</td></tr>
    <tr><td>Dextromethorphan</td><td>Cough</td><td>Confusion, excitement, agitation</td><td><strong>Taking a monoamine oxidase inhibitor now or within 2 weeks</strong>; <strong>serotonin syndrome</strong> with other pro-serotonergic drugs</td></tr>
    <tr><td>Guaifenesin</td><td>Mucolytic, expectorant: <strong>loosens mucus and decreases its viscosity</strong></td><td>Nausea, vomiting</td><td>Allergy; no interactions listed</td></tr>
  </table>

  <p>Three more agents thin sputum in lung disease. <strong>Dornase alfa (Pulmozyme)</strong>,
  nebulized, is a DNA enzyme that <strong>selectively cleaves DNA from the nuclei of degenerating
  neutrophils</strong>, reducing the viscosity of cystic fibrosis sputum; it improves lung
  function and reduces exacerbations in mild to moderate disease, and helps severe disease less.
  <strong>Hypertonic saline</strong>, inhaled, is reported to improve the rheology and transport
  of mucus, airway surface hydration, mucociliary clearance and lung function.
  <strong>N-acetylcysteine (Mucomyst)</strong>, traditionally the treatment for acetaminophen
  toxicity, is mucolytic when nebulized: it <strong>splits the disulfide bonds linking
  mucoproteins</strong>. Inhaled, it smells of <strong>rotten eggs</strong> (its sulfur), causes
  nausea and vomiting, and can cause <strong>bronchospasm</strong>.</p>

  <h3 class="sub" id="ent-edu">2.10 &middot; Objectives 9&ndash;10 &mdash; Protocols, monitoring and patient education</h3>

  <p><strong>Protocols.</strong> Otitis media is judged to have failed treatment at <strong>3
  days without improvement</strong>. Sinusitis must meet the <strong>10-day or worsening</strong>
  test before it is treated as bacterial. Pharyngitis is confirmed with a <strong>rapid strep
  test</strong> before prescribing. Treatment durations on the slides: otitis media 5 to 7 days,
  possibly up to 10 (5 may be too short for severe disease); sinusitis 10 to 14 days in children
  and 5 to 7 in adults; strep pharyngitis 10 days of amoxicillin, or one benzathine penicillin
  injection.</p>

  <div class="callout"><strong>Nasal spray technique</strong> (azelastine and oxymetazoline share
  it): blow the nose and clear the nostrils; <strong>tilt the head down</strong> (toward the
  toes); <strong>angle the spray away from the septum</strong>; <strong>right hand sprays the left
  nostril, left hand the right</strong>; do not tilt the head back, which draws the drug into the
  throat; clean the tip with a tissue; do not use with other nasal sprays. <strong>If a nosebleed
  develops, stop and follow up immediately</strong>; if symptoms worsen, follow up immediately,
  and if they do not improve, follow up. Oxymetazoline adds one rule: <strong>no more than 3 to 5
  days</strong>.</div>

  <table>
    <tr><th>Drug</th><th>What to tell the patient</th></tr>
    <tr><td>Aspirin</td><td>Take for fever above 100&nbsp;&deg;F; if the fever is not held below 102&nbsp;&deg;F, or stays above 100&nbsp;&deg;F for more than 3 days, follow up immediately; drink plenty of fluids; follow up if pain worsens or lasts more than 10 days; <strong>do not combine with other NSAIDs</strong>; <strong>do not take with anticoagulants</strong>, because aspirin inhibits platelet function</td></tr>
    <tr><td>Dexamethasone</td><td><strong>Do not stop abruptly if taken for more than a week</strong>; it weakens the immune system</td></tr>
    <tr><td>Prednisone</td><td><strong>Do not stop abruptly</strong> (rebound symptoms); you are immunocompromised &mdash; <strong>avoid chickenpox, measles and live vaccines</strong></td></tr>
    <tr><td>Benzonatate</td><td><strong>Swallow whole</strong> &mdash; do not chew, cut or crush</td></tr>
    <tr><td>Guaifenesin</td><td>Drink plenty of fluid; <strong>expect more drainage</strong>; follow up if symptoms persist beyond 7 days or worsen</td></tr>
  </table>

</section>
'''
