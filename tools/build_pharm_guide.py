#!/usr/bin/env python3
"""Build the Pharmacology I Exam 1 study guide (Lecture 1).

Same skeleton-lift as the CMS, Clin Path and Microbiology builders: take the
donor's head and tail so the design system, chrome and read-aloud wiring come
for free, and splice in a fresh table of contents, body and Test Yourself.

The instructional objectives are reproduced VERBATIM from the syllabus,
including its numbering quirk -- objective 5 introduces the antivirals and the
three classes then appear as top-level items 6, 7 and 8 rather than 5a to 5c.
Nine printed numbers, six real objectives. Reproducing the printed numbering is
what the verbatim rule requires; the guide says so rather than silently
renumbering.

Deliberately NO data-audio-dir: the mp3s do not exist, and pointing at an empty
audio folder is what broke read-aloud on iPad once already.
"""
import os, re

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Microbiology Exam 1/micro-exam-1-study-guide.html")
OUT = os.path.join(ROOT, "Pharmacology I Exam 1/pharm-exam-1-study-guide.html")
I = "pharm-exam-1-study-guide-images"


def fig(n, w, h, alt, cap, src):
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="src">%s</span></figcaption></figure>\n  ') % (w, h, I, n, alt, cap, src)


FIG_TARGETS = fig("001.jpg", 500, 328,
  "Diagram of a bacterial cell with each antibiotic target labelled: cell wall synthesis, DNA gyrase, RNA elongation, DNA-directed RNA polymerase, protein synthesis at the 50S and 30S subunits, folic acid metabolism, and cytoplasmic membrane structure, each with its drug classes.",
  "The single most useful figure in the antibacterial half, because it answers objective 2 in one picture. Every class in this lecture is somewhere on this cell. Read it as a map: the cell wall agents sit on the outside, the two ribosomal groups sit in the middle with 50S and 30S separated, and folate metabolism sits below as a supply line rather than a structure. Holding this image is worth more than holding fifteen separate mechanisms, because it tells you what a drug does from where it acts.",
  "Figure 20-14, Brock Biology of Microorganisms 11th edition, &copy; 2006 Pearson Prentice Hall. Reproduced from the lecture slides (Slide 11).")

FIG_CELLWALL = fig("002.png", 595, 346,
  "Classification chart headed Agents Affecting the Cell Wall, branching into beta-lactam antibiotics and other antibiotics, with penicillins, cephalosporins by generation, carbapenems and monobactams listed, and a separate box for beta-lactamase inhibitors.",
  "Class before agent, drawn out. The top split is the one that matters: beta-lactams on one side, and bacitracin, vancomycin and daptomycin on the other as cell wall agents that are not beta-lactams. Notice that the beta-lactamase inhibitors sit in their own box off to the side, which is exactly right &mdash; they have no antibacterial activity of their own and only exist to protect a partner drug. The cephalosporin generations run left to right, and the agents beneath each are worth reading as examples of a generation rather than as a list to memorise.",
  "Reproduced from the lecture slides (Slide 12).")

FIG_PENICILLIN = fig("003.png", 380, 262,
  "Two bacterial cells side by side; penicillin molecules approach the first, and the second is shown later with the cell envelope ruptured.",
  "What the mechanism actually produces. Penicillin does not poison the cell directly &mdash; it inactivates the enzyme that cross-links peptidoglycan, so the wall keeps being built and never gets tied together. The cell then fails mechanically, which is why the effect is bactericidal and why it is strongest in organisms that are actively dividing.",
  "&copy; www.scienceaid.co.uk. Reproduced from the lecture slides (Slide 16).")

FIG_VANCOMYCIN = fig("004.png", 800, 274,
  "Four-stage comparison of vancomycin-sensitive and vancomycin-resistant cell wall synthesis, showing vancomycin binding the terminal D-alanine residues in the sensitive organism and failing to bind where D-alanine has been replaced by D-lactate in the resistant one.",
  "Mechanism and resistance in the same picture. In the top row vancomycin caps the two terminal D-alanine residues, so the cross-linking enzyme cannot reach its substrate. In the bottom row a single substitution &mdash; D-lactate in place of the terminal D-alanine &mdash; means vancomycin no longer binds, and cross-linking proceeds normally. That one change is the whole basis of vancomycin resistance, and it explains why the lecture says resistance is harder to develop here than against penicillin: the drug covers the substrate rather than disabling an enzyme, so the organism has to rebuild its own building block.",
  "Reproduced from the lecture slides (Slide 46).")

FIG_FUNGALWALL = fig("005.jpg", 688, 457,
  "Labelled cross-section of the fungal cell envelope showing mannoproteins, beta-1,3 and beta-1,6 glucans, beta-1,3 glucan synthase spanning the membrane, chitin, and ergosterol within the cell membrane.",
  "Both antifungal targets on one image, which is why this figure carries the whole of objective 9. The green mesh is glucan, and the orange enzyme spanning the membrane is beta-1,3 glucan synthase &mdash; the echinocandin target, and the only one here with no mammalian counterpart at all, since human cells have no cell wall. Below it, threaded through the membrane, is ergosterol: bound directly by the polyenes, and depleted upstream by the azoles and allylamines. Sort any antifungal by which of those two structures it attacks and the class list stops needing memorisation.",
  "Reproduced from the lecture slides (Slide 90).")

FIG_POLYENE = fig("006.png", 414, 276,
  "Two membrane diagrams: the first shows ergosterol embedded in a lipid bilayer, the second shows the same membrane after a polyene has been added, with a pore formed through the ergosterol.",
  "Why polyene toxicity is so predictable. The drug binds ergosterol already present and opens a channel through it, so potassium and magnesium leak out of the cell. That is a physical hole rather than an enzymatic block, which is why the effect is immediate and why the human toxicity is electrolyte disturbance &mdash; mammalian membranes contain the related sterol cholesterol, so the same trick works, just less well.",
  "Reproduced from the lecture slides (Slide 96).")

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#antimicrobials">1 &middot; Antibiotics, Antivirals and Antifungals</a>
  <a href="#am-categories">1.1 Objective 1 &mdash; Categorizations of antimicrobial drugs</a>
  <a href="#am-modes">1.2 Objective 2 &mdash; Common modes of action</a>
  <a href="#am-static-cidal">1.3 Objective 3 &mdash; Bacteriostatic versus bactericidal</a>
  <a href="#am-betalactams">1.4 Objective 4 &mdash; Beta-lactams</a>
  <a href="#am-glyco">1.5 Objective 4 &mdash; Glycopeptides &amp; lipopeptides</a>
  <a href="#am-protein">1.6 Objective 4 &mdash; Protein synthesis inhibitors</a>
  <a href="#am-dnafolate">1.7 Objective 4 &mdash; DNA, folate and membrane agents</a>
  <a href="#am-antivirals">1.8 Objectives 5&ndash;8 &mdash; Antivirals</a>
  <a href="#am-antifungals">1.9 Objective 9 &mdash; Antifungals</a>
  <a href="#am-outside">1.10 Taught but not in the objectives</a>
</nav>'''

BODY = '''<main>

<section class="deck" id="antimicrobials">
  <h2 class="deck-title">1 &middot; Antibiotics, Antivirals and Antifungals</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Discuss the basics of antimicrobial management, including the categorizations of drugs known as antiseptics, antimicrobials, anti-infectives, antibacterials (antibiotics), antivirals, and antifungals</li>
      <li>Compare and contrast the common modes of action of antimicrobial agents against microorganisms</li>
      <li>Explain the difference between a bacteriostatic drug and a bactericidal drug.</li>
      <li>Identify common drugs, indications, contraindications, molecular mechanisms of action, routes of administration, dosing protocols, potential interactions, precautions, common adverse effects, any needed laboratory monitoring, and appropriate patient education for the following classes of antibiotics: <em>a.</em> Penicillins <em>b.</em> Cephalosporins <em>c.</em> Monobactams <em>d.</em> Carbapenems <em>e.</em> Macrolides/ketolides <em>f.</em> Lincosamides <em>g.</em> Streptogramins <em>h.</em> Tetracyclines <em>i.</em> Aminoglycosides <em>j.</em> Glycopeptides &amp; lipopeptides <em>k.</em> Fluoroquinolones <em>l.</em> Oxazolidinones <em>m.</em> Polypeptides <em>n.</em> Folate synthesis inhibitors <em>o.</em> Nitroimidazoles</li>
      <li>Identify common drugs, indications, contraindications, mechanisms of action, routes of administration, dosing protocols, potential interactions, precautions, common adverse effects, any needed laboratory monitoring, and appropriate patient education for the following classes of antivirals:</li>
      <li>Anti-herpes agents</li>
      <li>Anti-cytomegalovirus agents</li>
      <li>Anti-influenza agents</li>
      <li>Identify common drugs, indications, contraindications, mechanisms of action, routes of administration, dosing protocols, potential interactions, precautions, common adverse effects, any needed laboratory monitoring, and appropriate patient education for the following classes of antifungals: <em>a.</em> Echinocandins <em>b.</em> Polyenes <em>c.</em> Azoles <em>d.</em> Allylamines <em>e.</em> Mitotic inhibitors</li>
    </ol>
  </div>

  <div class="callout"><strong>Two things about that list before you use it.</strong>
  The numbering above is reproduced exactly as the syllabus prints it. Objective 5 introduces
  the antivirals and then the three classes appear as top-level items <strong>6, 7 and 8</strong>
  rather than 5a to 5c &mdash; so nine printed numbers are really six objectives, and the
  antivirals are one objective with three parts, not four separate ones. Do not let the miscount
  make the antivirals look like half the lecture.
  <br><br>
  Second: <mark class="prof-highlight">Dr. Wood told the class there is no need to memorise or
  know drug dosages.</mark> The deck is full of regimens and this guide reproduces almost none of
  them. Where a number does appear it is because it is a monitoring target or a treatment
  duration you would counsel a patient about, not a dose.</div>

  <h3 class="sub" id="am-categories">1.1 &middot; Objective 1 &mdash; Categorizations of antimicrobial drugs</h3>
  <p>The lecture opens by separating terms that get used interchangeably in conversation and
  are not interchangeable at all.</p>
  <table>
    <tr><th>Term</th><th>What it means</th></tr>
    <tr><td>Antimicrobial</td><td>The broad category &mdash; any agent acting against a microbe</td></tr>
    <tr><td>Antibacterial (antibiotic)</td><td>Acting against bacteria. Strictly, an antibiotic is of microbial origin</td></tr>
    <tr><td>Antiviral</td><td>Acting against viruses</td></tr>
    <tr><td>Antifungal</td><td>Acting against fungi</td></tr>
    <tr><td>Antiseptic</td><td>Applied to living tissue to reduce microbial load</td></tr>
    <tr><td>Anti-infective</td><td>Umbrella term covering agents used to treat infection</td></tr>
  </table>
  <p>Choosing a regimen is then framed by <strong>drug factors</strong>: spectrum of activity;
  pharmacokinetics (absorption, distribution, penetration into body compartments, elimination);
  pharmacodynamics (bactericidal or bacteriostatic, time-dependent or concentration-dependent
  killing); and toxicities across six systems &mdash; gastrointestinal, integument, hematologic,
  central nervous system, hepatic and renal. Those six recur as the monitoring parameters for
  individual classes later, so they are worth reading as a checklist rather than a list.</p>
  <div class="pearl">The lecturer's own framing is worth keeping: this class is not the end of
  pharmacology, and the real-world answer is to use references &mdash; guidelines, textbooks,
  online references and a friendly pharmacist. Art versus science; things are rarely black and
  white.</div>

  <h3 class="sub" id="am-modes">1.2 &middot; Objective 2 &mdash; Common modes of action</h3>
  ''' + FIG_TARGETS + '''
  <table>
    <tr><th>Target</th><th>Classes</th></tr>
    <tr><td>Cell wall synthesis</td><td>Penicillins, cephalosporins, monobactams, carbapenems, vancomycin, bacitracin</td></tr>
    <tr><td>Protein synthesis &mdash; 50S subunit</td><td>Macrolides, clindamycin, chloramphenicol, streptogramins</td></tr>
    <tr><td>Protein synthesis &mdash; 30S subunit</td><td>Aminoglycosides, tetracyclines</td></tr>
    <tr><td>DNA gyrase / topoisomerase</td><td>Fluoroquinolones</td></tr>
    <tr><td>Folic acid metabolism</td><td>Sulfonamides, trimethoprim</td></tr>
    <tr><td>Cytoplasmic membrane</td><td>Polymyxins, daptomycin</td></tr>
    <tr><td>Nucleic acid, direct damage</td><td>Metronidazole</td></tr>
  </table>
  <div class="callout"><strong>Why the ribosome is a target at all.</strong> The bacterial
  ribosome is <strong>70S</strong>, made of a 50S and a 30S subunit; the mammalian one is
  <strong>80S</strong>, made of 60S and 40S. That difference is the entire basis of selectivity
  &mdash; and it is a difference of degree, not an absolute barrier, which is why high levels of
  these drugs can interact with mammalian ribosomes and produce dose-related toxicity.</div>

  <h3 class="sub" id="am-static-cidal">1.3 &middot; Objective 3 &mdash; Bacteriostatic versus bactericidal</h3>
  <p><strong>Bacteriostatic</strong> inhibits a vital pathway used in bacterial growth but does
  not directly cause death. <strong>Bactericidal</strong> disrupts function enough that death
  occurs. The lecture gives five and six agents respectively:</p>
  <table>
    <tr><th>Bacteriostatic</th><th>Bactericidal</th></tr>
    <tr><td>Erythromycin &middot; tetracyclines &middot; sulfonamides &middot; trimethoprim &middot; clindamycin</td>
        <td>Penicillins &middot; cephalosporins &middot; aminoglycosides &middot; vancomycin &middot; fluoroquinolones &middot; metronidazole</td></tr>
  </table>
  <p>Notice the bactericidal list spans the cell wall, the ribosome and DNA. Killing is not tied
  to one target, so you cannot infer static-versus-cidal from mechanism alone &mdash; it has to
  be learned.</p>
  <table>
    <tr><th></th><th>Concentration-dependent</th><th>Time-dependent</th></tr>
    <tr><td>What drives killing</td><td>Higher concentration, greater killing</td><td>Time above the minimal inhibitory concentration</td></tr>
    <tr><td>Post-antibiotic effect</td><td>Present</td><td>None</td></tr>
    <tr><td>Target</td><td>Peak level</td><td>40&ndash;70% of the dosing interval above the minimal inhibitory concentration</td></tr>
    <tr><td>Dosing that follows</td><td>Large, widely spaced doses</td><td>Continuous or frequent infusions</td></tr>
  </table>
  <div class="pearl">This is the reasoning behind two things you will see on the wards: the
  aminoglycosides moving from every 8 hours to once daily, and piperacillin/tazobactam being
  given as an extended infusion. One exploits a post-antibiotic effect; the other buys time above
  the minimal inhibitory concentration.</div>
  <button class="test-yourself-btn" style="--acc:#9c5230" onclick="window.openTestYourself('Test yourself &mdash; Principles', TEST_YOURSELF.principles)">Test yourself! &rarr;</button>

  <h3 class="sub" id="am-betalactams">1.4 &middot; Objective 4 &mdash; Beta-lactams</h3>
  ''' + FIG_CELLWALL + '''
  <h4 class="subsub">Penicillins (objective 4a)</h4>
  <p>The <strong>beta-lactam ring mimics two D-alanine residues</strong>. The cross-linking
  enzyme &mdash; a penicillin-binding protein &mdash; binds the drug by mistake and is covalently
  inactivated. Once enough penicillin-binding protein is inactive, peptidoglycan chains are still
  synthesized but <strong>no new cross-links can form</strong>.</p>
  ''' + FIG_PENICILLIN + '''
  <table>
    <tr><th>Subclass</th><th>Agents</th><th>What it is for</th></tr>
    <tr><td>Natural</td><td>Penicillin G, penicillin V potassium, penicillin G benzathine</td><td>Syphilis, gas gangrene, meningococcus. Good Gram-positive cocci, <strong>no Staphylococcus</strong>, no aerobic Gram-negatives</td></tr>
    <tr><td>Aminopenicillins</td><td>Ampicillin, amoxicillin</td><td>Enterococcus, Listeria, endocarditis prophylaxis, upper respiratory infection, community-acquired pneumonia at high dose</td></tr>
    <tr><td>With a beta-lactamase inhibitor</td><td>Augmentin, Unasyn, Zosyn</td><td>Adds Bacteroides and methicillin-susceptible <em>Staphylococcus aureus</em>. Skin and soft tissue, diabetic foot, animal and human bites</td></tr>
    <tr><td>Penicillinase-resistant</td><td>Nafcillin, oxacillin, dicloxacillin</td><td>Built solely for methicillin-susceptible <em>Staphylococcus aureus</em>; increasingly defeated by methicillin resistance</td></tr>
    <tr><td>Antipseudomonal</td><td>Piperacillin, piperacillin/tazobactam</td><td>Polymicrobial and nosocomial infection, intra-abdominal infection, <em>Pseudomonas</em></td></tr>
  </table>
  <p><strong>Dosage forms are worth separating from doses.</strong> Penicillin V potassium is the
  oral form because it is stable in stomach acid; penicillin G is intravenous; penicillin G
  benzathine is the long-acting intramuscular depot given as a one-time dose.</p>
  <p><strong>Resistance</strong> is beta-lactamase cleaving the beta-lactam ring. The inhibitors
  &mdash; sulbactam with ampicillin, tazobactam with piperacillin, clavulanate with amoxicillin
  &mdash; have <em>no antibacterial activity of their own</em> and irreversibly inactivate the
  enzyme.</p>
  <div class="callout"><strong>Adverse effects and interactions worth holding.</strong>
  Aminopenicillins: hepatic dysfunction, <em>Clostridium difficile</em>, Stevens-Johnson syndrome
  and toxic epidermal necrolysis, interstitial nephritis, anemia and thrombocytopenia.
  Interactions: prolongation of the prothrombin time with anticoagulants, and reduced oral
  contraceptive effectiveness &mdash; the lecture is candid that the evidence for the latter is
  not strong, the proposed mechanism being disrupted gut flora and reduced enterohepatic
  recycling of estrogens. Advise backup contraception anyway.</div>

  <h4 class="subsub">Cephalosporins (objective 4b)</h4>
  <p>Good cerebrospinal fluid penetration, mostly renal elimination, and penicillin
  cross-sensitivity of <strong>less than 1%</strong> &mdash; lower than the figure usually
  quoted, and clinically important because a reported penicillin allergy does not by itself rule
  a cephalosporin out.</p>
  <table>
    <tr><th>Generation</th><th>Agents</th><th>Coverage</th></tr>
    <tr><td>1st</td><td>Cefazolin, cephalexin</td><td>Great Gram-positive (no <em>Enterococcus</em>), some Gram-negative. Surgical prophylaxis, cellulitis, urinary tract infection</td></tr>
    <tr><td>2nd</td><td>Cefotetan, cefoxitin, cefuroxime, cefprozil</td><td>More Gram-negative &mdash; <em>Haemophilus</em>, <em>Neisseria</em>, <em>Proteus</em>, <em>Escherichia coli</em>, <em>Klebsiella</em></td></tr>
    <tr><td>3rd</td><td>Ceftriaxone, ceftazidime, cefotaxime, cefdinir, cefixime</td><td>Better Gram-negative, less Gram-positive. Ceftazidime adds <em>Pseudomonas</em></td></tr>
    <tr><td>4th</td><td>Cefepime</td><td>Gram-negative <em>and</em> retained Gram-positive, antipseudomonal. No methicillin-resistant <em>Staphylococcus aureus</em>, no <em>Enterococcus</em>, no anaerobes</td></tr>
    <tr><td>5th</td><td>Ceftaroline; ceftolozane/tazobactam</td><td>Ceftaroline is the one with methicillin-resistant coverage. Ceftolozane is the antipseudomonal one</td></tr>
  </table>
  <div class="pearl">The generation rule and its exception: moving up the generations buys
  Gram-negative activity and costs Gram-positive activity &mdash; <strong>except the 4th
  generation, which gains Gram-negative without sacrificing Gram-positive.</strong> That single
  exception is what makes cefepime broad rather than merely Gram-negative, and it is why cefepime
  is the drug of choice for neutropenic fever.</div>
  <p>Two agent-specific points that are easy to confuse and easy to test: <strong>ceftriaxone
  needs no dosage adjustment in renal insufficiency</strong> but cannot be used in the first 30
  days of life, and <strong>cefotaxime is the one preferred in neonatal fever or sepsis</strong>.</p>

  <h4 class="subsub">Monobactams (objective 4c) and carbapenems (objective 4d)</h4>
  <p><strong>Aztreonam</strong> covers Gram-negatives only &mdash; a spectrum the lecture
  describes as resembling the aminoglycosides, including <em>Pseudomonas aeruginosa</em> and
  Enterobacteriaceae, with no Gram-positive or anaerobic activity. Its defining property is that
  it has <strong>no cross-reactivity with other beta-lactams</strong>, so it can be used in truly
  penicillin-allergic patients.</p>
  <p><strong>Carbapenems</strong> &mdash; imipenem, meropenem, ertapenem, doripenem &mdash; are
  very broad: Gram-positive (not methicillin-resistant <em>Staphylococcus aureus</em>),
  Gram-negative, <em>Pseudomonas</em> (<strong>except ertapenem</strong>), and anaerobes. They
  resist hydrolysis by beta-lactamases, which is why they are the answer for extended-spectrum
  beta-lactamase producers, multidrug-resistant Gram-negatives, nosocomial infection and
  meningitis. Watch for <strong>seizures with imipenem</strong>.</p>

  <h3 class="sub" id="am-glyco">1.5 &middot; Objective 4 &mdash; Glycopeptides &amp; lipopeptides (objective 4j)</h3>
  ''' + FIG_VANCOMYCIN + '''
  <p><strong>Vancomycin</strong> is not a beta-lactam. It also targets the cell wall, but it
  <strong>binds the two D-alanine residues on the peptide</strong> to block cross-linking rather
  than inactivating the enzyme &mdash; and because it covers the substrate rather than disabling
  an enzyme, resistance is harder to develop.</p>
  <p>Coverage is <strong>Gram-positive only</strong>. Drug of choice for penicillin-allergy
  infections, methicillin-resistant <em>Staphylococcus aureus</em>, <em>Clostridium difficile</em>
  by mouth, endocarditis, osteomyelitis, and surgical prophylaxis in allergy.</p>
  <div class="callout"><strong>Monitoring is the examinable part.</strong> Vancomycin requires
  therapeutic drug monitoring. <mark class="prof-highlight">Troughs are drawn 15 to 30 minutes
  before the next scheduled dose, usually around the third or fourth dose</mark> &mdash; that
  timing is what makes the level reflect steady state. Random levels are used in unstable or
  severe renal impairment, and the time of the draw must be specified. Watch renal clearance,
  ototoxicity and nephrotoxicity, and the infusion-related reactions: <strong>red man
  syndrome</strong>, fever, chills and phlebitis.</div>
  <p>Where the minimal inhibitory concentration is 2&nbsp;mg/L or greater, the target ratio of
  area under the curve to minimal inhibitory concentration becomes difficult to achieve and
  <strong>alternative therapy such as linezolid</strong> may be needed &mdash; pushing the dose
  is not a reliable answer.</p>
  <p><strong>Daptomycin</strong> causes bacterial depolarization, inhibiting DNA, RNA and protein
  synthesis, and is bactericidal. Its one crucial limitation: <strong>it cannot be used in
  pneumonia.</strong> Monitor muscle pain and creatine phosphokinase.</p>
  <button class="test-yourself-btn" style="--acc:#6b3524" onclick="window.openTestYourself('Test yourself &mdash; Cell wall agents', TEST_YOURSELF.cellwall)">Test yourself! &rarr;</button>

  <h3 class="sub" id="am-protein">1.6 &middot; Objective 4 &mdash; Protein synthesis inhibitors</h3>
  <table>
    <tr><th>Class</th><th>Subunit &amp; mechanism</th><th>Key points</th></tr>
    <tr><td>Macrolides (4e)<br>erythromycin, clarithromycin, azithromycin</td><td>50S; blocks transpeptidation</td><td>Gram-positive aerobes and <strong>atypicals</strong> &mdash; <em>Legionella</em>, <em>Mycoplasma</em>, <em>Chlamydophila</em>, <em>Chlamydia</em>. QT prolongation and torsades de pointes. Cytochrome P450 3A inhibition, erythromycin &gt; clarithromycin &gt; azithromycin</td></tr>
    <tr><td>Lincosamides (4f)<br>clindamycin</td><td>50S</td><td>Gram-positive aerobes including methicillin-resistant <em>Staphylococcus aureus</em>, plus Gram-positive and Gram-negative anaerobes. <strong>No Gram-negative aerobic coverage.</strong> Toxin-mediated disease. <em>Clostridium difficile</em> and pseudomembranous colitis</td></tr>
    <tr><td>Tetracyclines (4h)<br>tetracycline, doxycycline, minocycline</td><td>30S; binds 16S ribosomal RNA, blocks transfer RNA at the A site. Bacteriostatic</td><td>Excellent for atypicals and animal-borne organisms. <strong>Chelate cations</strong> &mdash; iron and calcium. Photosensitivity, tooth discoloration, avoid under 8 years and in the 2nd and 3rd trimesters</td></tr>
    <tr><td>Aminoglycosides (4i)<br>gentamicin, tobramycin, amikacin</td><td>30S</td><td>Gram-negatives including <em>Pseudomonas</em>; <em>Enterococcus</em> at synergy dosing only. Post-antibiotic effect &rarr; once-daily dosing. <strong>Nephrotoxic and ototoxic</strong></td></tr>
    <tr><td>Oxazolidinones (4l)<br>linezolid</td><td>50S</td><td>Resistant Gram-positives &mdash; multidrug-resistant pneumococcus, methicillin-resistant <em>Staphylococcus aureus</em>, vancomycin-resistant <em>Enterococcus</em>. No Gram-negatives or anaerobes. Thrombocytopenia; <strong>serotonin syndrome</strong> with selective serotonin reuptake inhibitors, tyramine foods, pseudoephedrine</td></tr>
    <tr><td>Streptogramins (4g)</td><td>50S</td><td>Named in the syllabus and on the mechanism slide; the deck gives no dedicated agent slides</td></tr>
  </table>
  <div class="callout"><strong>QT prolongation &mdash; the one property that crosses classes.</strong>
  It turns up three times on this exam, in three unrelated groups: <strong>macrolides</strong> here,
  <strong>fluoroquinolones</strong> under Objective 4, and <strong>posaconazole</strong> among the
  antifungals. Worth understanding once rather than memorising three times.
  <br><br>
  The QT interval measures how long the ventricle takes to <strong>repolarise</strong>. Repolarisation
  depends on potassium leaving the cell, and these drugs block the potassium channel that lets it out
  &mdash; the <strong>hERG</strong> channel, named in the figure on the drug-induced QT slide. Block it,
  repolarisation takes longer, and the QT stretches. Stretch it far enough and the rhythm degenerates
  into <mark class="prof-highlight">torsades de pointes</mark> &mdash; French for &ldquo;twisting of the
  points&rdquo;, which is exactly what the tracing does, the amplitude waxing and waning around the
  baseline.
  <br><br>
  <strong>What raises the risk</strong> is stacking, not any single dose: a congenital long QT, several
  QT-prolonging drugs at once, or an electrolyte disturbance. This is why posaconazole is on the list at
  all &mdash; its own hypokalaemia and hypomagnesaemia are what push the QT out. A single course of
  azithromycin in a healthy patient is a different proposition from the same drug added to an
  antiarrhythmic in someone whose potassium is low. <strong>The treatment of choice for torsades is
  magnesium sulfate, two grams</strong> &mdash; described in lecture as the &ldquo;two gram slam&rdquo;
  and called out as worth remembering.</div>
  <p><strong>Tigecycline</strong>, a glycylcycline, binds the 30S subunit and is bacteriostatic.
  It is approved for complicated skin and complicated intra-abdominal infection, covering
  methicillin-resistant <em>Staphylococcus aureus</em> and <em>Enterococcus faecalis</em>
  <strong>but not vancomycin-resistant <em>Enterococcus</em></strong>.</p>

  <h3 class="sub" id="am-dnafolate">1.7 &middot; Objective 4 &mdash; DNA, folate and membrane agents</h3>
  <table>
    <tr><th>Class</th><th>Mechanism</th><th>Key points</th></tr>
    <tr><td>Fluoroquinolones (4k)<br>ciprofloxacin, levofloxacin, moxifloxacin</td><td><strong>Dual</strong> &mdash; inhibits DNA gyrase (topoisomerase II) forming a quinolone-DNA-gyrase complex with induced DNA cleavage, and inhibits topoisomerase IV</td><td>Levofloxacin has <em>Pseudomonas</em> coverage; moxifloxacin does not and <strong>must not be used for urinary tract infection</strong>. Chelated by iron, antacids, multivitamins, calcium and dairy. QT prolongation. <strong>Tendonitis and Achilles rupture, peripheral neuropathy, central nervous system toxicity</strong>; caution under 18. Overuse drives resistance, with <em>Clostridium difficile</em> as collateral damage</td></tr>
    <tr><td>Folate synthesis inhibitors (4n)<br>sulfamethoxazole/trimethoprim</td><td>Two sequential steps: sulfamethoxazole blocks para-aminobenzoic acid &rarr; dihydrofolic acid via tetrahydropteroic acid synthetase; trimethoprim blocks dihydrofolic acid &rarr; tetrahydrofolic acid via dihydrofolate reductase</td><td>Covers methicillin-resistant <em>Staphylococcus aureus</em>, <strong>not enterococci</strong>. <em>Pneumocystis jirovecii</em> treatment and prophylaxis, urinary tract infection, prostatitis. Stevens-Johnson syndrome and toxic epidermal necrolysis, blood dyscrasias. Raises the international normalised ratio significantly with warfarin via cytochrome P450 2C9 inhibition</td></tr>
    <tr><td>Nitroimidazoles (4o)<br>metronidazole</td><td>Interacts with bacterial DNA causing loss of helical structure and strand breakage</td><td>Gram-positive and Gram-negative anaerobes and parasites. Drug of choice for <em>Clostridium difficile</em>, intra-abdominal combination therapy, sexually transmitted infections. <strong>Disulfiram-like reaction with ethanol</strong></td></tr>
    <tr><td>Polypeptides (4m)<br>polymyxin B, polymyxin E</td><td>Detergent-like interaction with the lipopolysaccharide of the Gram-negative outer membrane, displacing magnesium and calcium</td><td>Broad Gram-negative coverage. Resistance uncommon because the class went largely unused for 50 years, and use is expected to rise with multidrug resistance</td></tr>
  </table>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Black box warnings</span>
  <p style="margin:0 0 4px;">The polymyxins carry the only warnings this deck labels explicitly as
  <strong>black box</strong>: <strong>nephrotoxicity, neurotoxicity and neuromuscular
  blockade</strong>. Black box warnings rank third in what to weight for this exam &mdash; above
  ordinary adverse effects &mdash; so they are worth holding separately rather than folding into a
  general side-effect list.</p></div>
  <button class="test-yourself-btn" style="--acc:#c9a227" onclick="window.openTestYourself('Test yourself &mdash; Protein, DNA and folate agents', TEST_YOURSELF.other)">Test yourself! &rarr;</button>

  <h3 class="sub" id="am-antivirals">1.8 &middot; Objectives 5&ndash;8 &mdash; Antivirals</h3>
  <p>Eight general approaches are listed: block attachment, block uncoating, inhibit DNA or RNA
  synthesis, inhibit viral protein synthesis, inhibit specific viral enzymes, inhibit assembly,
  inhibit release, and stimulate the host immune system. Every agent below is one of those.</p>
  <table>
    <tr><th>Virus</th><th>What it causes</th></tr>
    <tr><td>Herpes simplex type 1</td><td>Mouth, face, skin, esophagus or brain</td></tr>
    <tr><td>Herpes simplex type 2</td><td>Genitals, rectum, hands or meninges</td></tr>
    <tr><td>Varicella-zoster</td><td>Chickenpox and shingles</td></tr>
    <tr><td>Cytomegalovirus</td><td>Retinitis, esophagitis, colitis</td></tr>
  </table>
  <table>
    <tr><th>Agents</th><th>Mechanism</th><th>Used for</th></tr>
    <tr><td>Acyclovir, valacyclovir (obj. 6)</td><td>Guanine analog <strong>lacking the sugar moiety</strong>; selectively phosphorylated by <strong>viral thymidine kinase</strong>, incorporated into viral DNA, and the missing sugar prevents elongation</td><td>Herpes simplex, varicella-zoster. Valacyclovir is the prodrug with far better oral absorption</td></tr>
    <tr><td>Penciclovir, famciclovir (obj. 6)</td><td>Similar to acyclovir</td><td>Herpes simplex and varicella-zoster. Famciclovir is the oral prodrug; penciclovir is intravenous</td></tr>
    <tr><td>Ganciclovir, valganciclovir (obj. 7)</td><td>Guanine analog, inhibiting similarly to acyclovir</td><td><strong>Cytomegalovirus</strong> in transplant and immunocompromised patients. Valganciclovir is the better-absorbed oral prodrug</td></tr>
    <tr><td>Oseltamivir (obj. 8)</td><td>Prodrug converted to its carboxylate form; <strong>inhibits neuraminidase</strong> so budding progeny cannot be cleaved free of the host cell</td><td>Influenza A and B. Oral only, renally adjusted</td></tr>
  </table>
  <div class="callout"><strong>Selectivity, two different ways.</strong> Acyclovir is switched
  <em>on</em> by a viral enzyme &mdash; it is only phosphorylated where the virus is replicating.
  Oseltamivir switches a viral enzyme <em>off</em>. Both act on the virus and not the host, by
  opposite routes.</div>
  <p><strong>Timing matters and is examinable.</strong> Oseltamivir must be started as soon as
  possible, <mark class="prof-highlight">within 48 hours</mark>; because it blocks release of new
  virus rather than clearing virus already present, late treatment has little to act on. Acyclovir
  given in the first 24 hours of chickenpox <strong>shortens the acute illness but does not cure
  the infection</strong>.</p>
  <p><strong>Adverse effects.</strong> Acyclovir: nausea, vomiting, rash, bone marrow suppression,
  central nervous system effects (seizures, delirium, tremor), and <strong>crystallisation in the
  renal tubule</strong> &mdash; maintain hydration and renal function. Ganciclovir is the harder
  drug: neutropenia and thrombocytopenia, central nervous system effects including confusion,
  ataxia, seizures and coma, and <strong>about a third of patients must stop intravenous treatment
  because of side effects</strong>.</p>
  <div class="pearl">Four prodrugs appear in this short section &mdash; valacyclovir, famciclovir,
  valganciclovir and oseltamivir. Each exists to solve poor oral absorption of its parent. If a
  question asks why one agent is preferred orally, the prodrug design is usually the answer.</div>
  <button class="test-yourself-btn" style="--acc:#9c5230" onclick="window.openTestYourself('Test yourself &mdash; Antivirals', TEST_YOURSELF.antivirals)">Test yourself! &rarr;</button>

  <h3 class="sub" id="am-antifungals">1.9 &middot; Objective 9 &mdash; Antifungals</h3>
  <p>Fungi are <strong>eukaryotic</strong>, with a rigid cell wall containing chitin, a cell
  membrane built on <strong>ergosterol</strong>, different ribosomes and a distinct nuclear
  membrane. They are resistant to antibiotics, and every antifungal class exploits one of those
  differences.</p>
  ''' + FIG_FUNGALWALL + '''
  <p><strong>Predisposing factors:</strong> loss of barriers (burns, surgery, catheters);
  immunodeficiency (cancer, human immunodeficiency virus infection, transplant, chemotherapy);
  metabolic abnormality (diabetes); <strong>suppression of competing organisms</strong>
  (antibiotics); and a warm moist environment (diaper rash, athlete's foot). Note that treating a
  bacterial infection is itself a fungal risk factor.</p>
  <table>
    <tr><th>Depth</th><th>Organisms</th></tr>
    <tr><td>Systemic &mdash; internal organs</td><td><em>Aspergillus</em>, <em>Blastomyces</em>, <em>Candida</em>, <em>Coccidioides</em>, <em>Cryptococcus</em>, <em>Histoplasma</em>, Zygomycetes</td></tr>
    <tr><td>Subcutaneous &mdash; skin layers</td><td>Chromomycosis, Pseudallescheriasis, Sporotrichosis</td></tr>
    <tr><td>Superficial &mdash; hair, nails, mucous membranes</td><td><em>Epidermophyton</em>, <em>Microsporum</em>, <em>Trichophyton</em></td></tr>
  </table>
  <table>
    <tr><th>Class</th><th>Target &amp; mechanism</th><th>Agents and key points</th></tr>
    <tr><td>Polyenes (9b)</td><td><strong>Membrane</strong> &mdash; bind ergosterol already present, forming channels; oxidative damage</td><td>Amphotericin B, nystatin, natamycin. Lipid formulations cost 20&ndash;50&times; more with reduced toxicity. Fever and chills from interleukin-1 and tumour necrosis factor &mdash; pretreat. Hypokalaemia, hypomagnesaemia, hypotension, renal tubule damage &mdash; hydrate with normal saline. Nystatin is poorly absorbed, so topical and oral only</td></tr>
    <tr><td>Azoles (9c)</td><td><strong>Membrane</strong> &mdash; inhibit fungal cytochrome P450 14-alpha-demethylase, blocking lanosterol &rarr; ergosterol</td><td>Fluconazole: best oral absorption, penetrates the central nervous system, cryptococcal meningitis and candidiasis, <strong>teratogenic in animals</strong>. Voriconazole: systemic aspergillosis, <strong>vision effects in ~30%</strong>, cyclodextrin vehicle accumulates in renal failure, <strong>teratogenic in animals</strong>. Posaconazole: the <strong>only azole effective against the Zygomycetes</strong>, QT prolongation. Itraconazole: blastomycosis, histoplasmosis, onychomycosis, <strong>teratogenic</strong>. Ketoconazole: rarely used &mdash; no central nervous system entry, strong cytochrome P450 3A4 inhibition</td></tr>
    <tr><td>Echinocandins (9a)</td><td><strong>Cell wall</strong> &mdash; inhibit 1,3-beta-D-glucan synthase</td><td>Caspofungin, micafungin, anidulafungin. Oesophageal candidiasis, refractory aspergillosis, febrile neutropenia. Tachycardia, headache, insomnia, hypokalaemia, hypomagnesaemia</td></tr>
    <tr><td>Allylamines (9d)</td><td><strong>Membrane</strong> &mdash; inhibit squalene epoxidase</td><td>Naftifine (topical), terbinafine (oral and topical). Superficial dermatophytes. Fingernails 6&ndash;12 weeks, toenails up to 12 months</td></tr>
    <tr><td>Mitotic inhibitors (9e)</td><td><strong>Cell division</strong> &mdash; interrupts mitotic spindles</td><td>Griseofulvin, from <em>Penicillium griseofulvum</em>. Deposited in keratin precursor cells. Scalp ~1 month, fingernails 6&ndash;9 months, toenails up to 12 months. Absorption increased by a high-fat meal. Not effective against <em>Candida</em>; fungistatic. Induces cytochrome P450 1A2 and 2C9</td></tr>
  </table>
  ''' + FIG_POLYENE + '''
  <p><strong>Flucytosine</strong> sits outside that scheme: it is converted to 5-fluorouridine by
  <strong>cytosine deaminase, an enzyme human cells lack</strong>, and then inhibits thymidylate
  synthase. Used with amphotericin B in cryptococcal meningitis and with itraconazole in
  chromoblastomycosis. Bone marrow suppression, hepatotoxicity, gastrointestinal upset, rash.</p>
  <div class="pearl">Sorting the antifungals is a two-question exercise. First: wall or membrane?
  Echinocandins are the only wall agents. Second, for the membrane agents: bind ergosterol
  (polyenes) or block its synthesis (azoles at lanosterol demethylase, allylamines at squalene
  epoxidase)? Griseofulvin and flucytosine are the two that sit outside both questions.</div>
  <p>The tinea names are worth knowing outright: <strong>tinea pedis</strong> athlete's foot,
  <strong>tinea corporis</strong> ringworm, <strong>tinea cruris</strong> jock itch,
  <strong>tinea unguium</strong> onychomycosis of the nails.</p>
  <button class="test-yourself-btn" style="--acc:#6b3524" onclick="window.openTestYourself('Test yourself &mdash; Antifungals', TEST_YOURSELF.antifungals)">Test yourself! &rarr;</button>

  <h3 class="sub" id="am-outside">1.10 &middot; Taught but not in the objectives</h3>
  <div class="callout"><strong>Anthelmintics.</strong> Slides 114 to 116 cover the benzimidazoles
  &mdash; albendazole and mebendazole, which inhibit helminth microtubule formation and block
  glucose uptake, used for hookworm, roundworm, pinworm and whipworm &mdash; and
  <strong>pyrantel pamoate</strong>, which releases acetylcholine and inhibits cholinesterase,
  acting as a depolarizing neuromuscular blocker to paralyse the parasite, used for pinworm and
  hookworm.
  <br><br>
  They are included here and in the antifungal quizzes because he taught them, but they appear in
  <strong>no syllabus objective</strong> &mdash; objectives 4, 5 and 9 cover antibacterials,
  antivirals and antifungals only. Worth confirming their status before spending time on them.
  <strong>Tolnaftate</strong> is in a similar position: it distorts hyphae and stunts mycelial
  growth, treats tinea pedis, cruris and corporis but <em>not</em> tinea unguium, and is topical
  only.</div>
</section>

</main>'''

TEST_YOURSELF = '''  var TEST_YOURSELF = {
    principles: [
      {q:"Which of these is on the lecture's BACTERIOSTATIC list?",
       choices:["Clindamycin","Vancomycin","Metronidazole","Cephalosporins"],correct:0,
       explain:"Clindamycin sits with erythromycin, tetracyclines, sulfonamides and trimethoprim. The other three are on the bactericidal list."},
      {q:"An agent shows a post-antibiotic effect and concentration-dependent killing. What dosing follows?",
       choices:["Continuous infusion","Frequent small doses","Large, widely spaced doses","Alternate-day dosing"],correct:2,
       explain:"Killing rises with peak concentration and persists after the level falls, so one large dose beats several small ones. This is the reasoning behind once-daily aminoglycosides."},
      {q:"Selectivity of the protein synthesis inhibitors rests on which difference?",
       choices:["Bacteria lack ribosomes entirely","Bacteria use RNA where humans use DNA","Bacterial ribosomes sit outside the cell","Bacterial 70S versus mammalian 80S ribosomes"],correct:3,
       explain:"70S (50S plus 30S) against 80S (60S plus 40S). It is a difference of degree, which is why high levels can still reach mammalian ribosomes and cause dose-related toxicity."},
      {q:"Which six toxicity categories does the lecture list under drug factors?",
       choices:["Gastrointestinal, integument, hematologic, central nervous system, hepatic, renal","Cardiac, pulmonary, endocrine, ocular, dermatologic, renal","Renal, hepatic, endocrine, vascular, lymphatic, ocular","Neurologic, muscular, skeletal, vascular, renal, hepatic"],correct:0,
       explain:"These six recur as the monitoring parameters for individual classes later in the lecture, so they work as a checklist rather than a list to recite."},
      {q:"For a time-dependent agent with no post-antibiotic effect, what is the target?",
       choices:["Peak concentration ten times the minimal inhibitory concentration","A single daily peak","Time above the minimal inhibitory concentration for 40 to 70 percent of the interval","Trough above the minimal inhibitory concentration at all times"],correct:2,
       explain:"Without a post-antibiotic effect the organism resumes growing the moment the level falls, so what matters is how much of the interval sits above the threshold."}
    ],
    cellwall: [
      {q:"What does the beta-lactam ring mimic?",
       choices:["Two D-alanine residues","N-acetylglucosamine","Lanosterol","The pentaglycine bridge"],correct:0,
       explain:"The mimicry is the whole trick: the cross-linking enzyme cannot tell the drug from its substrate and is covalently inactivated."},
      {q:"Which cephalosporin generation gains Gram-negative activity WITHOUT sacrificing Gram-positive?",
       choices:["1st","2nd","3rd","4th"],correct:3,
       explain:"The 4th generation is the exception to the generation rule, which is what makes cefepime broad rather than merely Gram-negative."},
      {q:"How does vancomycin differ mechanistically from a penicillin?",
       choices:["It inactivates the cross-linking enzyme more strongly","It binds the D-alanine substrate rather than the enzyme","It inhibits the 50S ribosome","It disrupts the outer membrane"],correct:1,
       explain:"Covering the substrate rather than disabling an enzyme is why resistance is harder to develop, and why resistance when it comes involves swapping D-alanine for D-lactate."},
      {q:"Which carbapenem lacks Pseudomonas coverage?",
       choices:["Imipenem","Meropenem","Ertapenem","Doripenem"],correct:2,
       explain:"Ertapenem is the exception in an otherwise antipseudomonal class — and it is also the one dosed once daily. The convenience and the narrower spectrum travel together."},
      {q:"Why can aztreonam be used in a truly penicillin-allergic patient?",
       choices:["It is not a beta-lactam at all","It has no cross-reactivity with other beta-lactams","It is given only topically","It is always combined with an antihistamine"],correct:1,
       explain:"That single property is what makes a Gram-negative-only agent worth having."}
    ],
    other: [
      {q:"Which fluoroquinolone must NOT be used for urinary tract infection?",
       choices:["Ciprofloxacin","Levofloxacin","Moxifloxacin","All are suitable"],correct:2,
       explain:"Moxifloxacin also lacks Pseudomonas coverage, unlike levofloxacin, and needs no renal dose adjustment."},
      {q:"Which class carries the only explicit BLACK BOX warnings in this lecture?",
       choices:["Fluoroquinolones","Polymyxins","Macrolides","Aminoglycosides"],correct:1,
       explain:"Nephrotoxicity, neurotoxicity and neuromuscular blockade. Black box warnings rank third in what to weight for this exam, above ordinary adverse effects."},
      {q:"Clindamycin covers everything EXCEPT which group?",
       choices:["Gram-positive aerobes","Gram-positive anaerobes","Gram-negative anaerobes","Gram-negative aerobes"],correct:3,
       explain:"That gap is why it is combined with another agent for intra-abdominal infection."},
      {q:"Sulfamethoxazole and trimethoprim block which pathway, and at how many steps?",
       choices:["Folate synthesis, at two sequential steps","Cell wall cross-linking, at one step","Protein synthesis, at two subunits","DNA gyrase, at two sites"],correct:0,
       explain:"Sulfamethoxazole blocks para-aminobenzoic acid to dihydrofolic acid; trimethoprim blocks dihydrofolic acid to tetrahydrofolic acid. Two steps in one pathway is what makes the pair synergistic."},
      {q:"A patient on metronidazole must be counselled to avoid what?",
       choices:["Dairy products","Sun exposure","Ethanol","Tyramine-containing foods"],correct:2,
       explain:"A disulfiram-like reaction. Dairy chelates tetracyclines and fluoroquinolones; tyramine is the linezolid caution."}
    ],
    antivirals: [
      {q:"How does acyclovir achieve selectivity for infected cells?",
       choices:["It is activated by viral thymidine kinase","It is concentrated by a host transporter","It binds a viral capsid protein","It is activated at low pH"],correct:0,
       explain:"The virus supplies the enzyme that switches the drug on, so it is only activated where replication is happening."},
      {q:"Which agent treats cytomegalovirus?",
       choices:["Acyclovir","Famciclovir","Ganciclovir","Oseltamivir"],correct:2,
       explain:"All are guanine analogues except oseltamivir, but the indications split by virus: acyclovir and famciclovir cover herpes simplex and varicella-zoster, ganciclovir covers cytomegalovirus."},
      {q:"What does inhibiting neuraminidase actually prevent?",
       choices:["Viral attachment to the host cell","Uncoating after entry","Replication of viral nucleic acid","Budding progeny being cleaved free of the host cell"],correct:3,
       explain:"Oseltamivir blocks release, not entry or replication — which is exactly why it must be started within 48 hours, while there is still spread left to prevent."},
      {q:"Which renal problem is characteristic of acyclovir?",
       choices:["Direct tubular necrosis","Crystallisation in the renal tubule","Interstitial nephritis","Accumulation of its intravenous vehicle"],correct:1,
       explain:"A physical rather than a toxic mechanism, which is why hydration is the countermeasure. Direct tubular damage is amphotericin B, and vehicle accumulation is voriconazole."},
      {q:"Roughly what proportion of patients must stop intravenous ganciclovir for side effects?",
       choices:["About 1 in 20","About a third","Almost none","Essentially all"],correct:1,
       explain:"Neutropenia and thrombocytopenia dominate. It is the reason the better-absorbed oral prodrug valganciclovir matters clinically."}
    ],
    antifungals: [
      {q:"Which antifungal target has NO mammalian counterpart at all?",
       choices:["Ergosterol","1,3-beta-D-glucan in the cell wall","Lanosterol demethylase","Microtubules"],correct:1,
       explain:"Mammalian cells have no cell wall, so the echinocandins have the cleanest selective target. Ergosterol has the analogue cholesterol, and demethylase is a cytochrome P450 enzyme with human counterparts."},
      {q:"Azoles and allylamines both reduce ergosterol. Where does each act?",
       choices:["Azoles at squalene epoxidase, allylamines at lanosterol demethylase","Both at lanosterol demethylase","Both at squalene epoxidase","Azoles at lanosterol demethylase, allylamines at squalene epoxidase"],correct:3,
       explain:"Same pathway, different steps — which is why both end in decreased ergosterol by different routes."},
      {q:"Which azole is the only one effective against the Zygomycetes?",
       choices:["Fluconazole","Voriconazole","Posaconazole","Ketoconazole"],correct:2,
       explain:"Fluconazole's niche is central nervous system penetration; voriconazole's is systemic aspergillosis."},
      {q:"Why does amphotericin B cause electrolyte disturbance?",
       choices:["It forms channels in ergosterol membranes so potassium and magnesium leak out","It blocks renal tubular reabsorption directly","It inhibits aldosterone","It chelates magnesium in the gut"],correct:0,
       explain:"A physical hole rather than an enzymatic block, which is why the effect is immediate and why hydration with normal saline is the countermeasure for the renal injury."},
      {q:"Griseofulvin reaches a dermatophyte infection how?",
       choices:["Deposited in keratin precursor cells in skin, hair and nails","Concentrated in sebum","Applied topically to the nail plate","Carried by macrophages across the dermis"],correct:0,
       explain:"That is why treatment lasts as long as the keratin takes to grow out — about a month for scalp, up to twelve for toenails."}
    ],'''

donor = open(DONOR, encoding="utf-8").read()
head = donor[:donor.index('<div class="layout wrap"')]
tail = donor[donor.index("</main>") + len("</main>"):]
ts = tail.index("var TEST_YOURSELF = {")
te = tail.index("\n  };", ts)
tail = tail[:ts] + TEST_YOURSELF.lstrip() + tail[te:]

# micro's forest green -> pharmacology's rust and copper
for old, new in (("#1f4d2b", "#6b3524"), ("#c2903a", "#c9a227"), ("#3f8a55", "#9c5230"),
                 ("#123018", "#40200f"), ("#5aa872", "#c07a4e"),
                 ("#1b241d", "#241a14"), ("#a6d9b5", "#e8c9a8")):
    head = head.replace(old, new)

# the professor-emphasis convention, with the dark-mode variants
PROF_CSS = '''  .prof-flag{border:2px solid #d4a017;border-radius:10px;padding:16px 14px 6px;
    margin:22px 0 14px;position:relative;background:#fffdf5;}
  .prof-flag-label{position:absolute;top:-13px;left:14px;background:#fef3d4;color:#8a6205;
    font-size:.72rem;font-weight:700;padding:2px 10px;border-radius:8px;
    border:1px solid #d4a017;letter-spacing:.3px;}
  mark.prof-highlight{background:#fef3d4;color:#3a2c05;padding:0 3px;border-radius:3px;
    box-shadow:inset 0 0 0 1px #e8c766;}
  :root[data-theme="dark"] .prof-flag{background:#241f10;border-color:#a8801a;}
  :root[data-theme="dark"] .prof-flag-label{background:#3a2f12;color:#f0d98a;border-color:#a8801a;}
  :root[data-theme="dark"] mark.prof-highlight{background:#4a3a12;color:#f7ecc8;
    box-shadow:inset 0 0 0 1px #7a6220;}
</style>'''
head = head.replace("</style>", PROF_CSS, 1)

head = re.sub(r"<title>.*?</title>",
              "<title>Pharmacology I &middot; Exam 1 &mdash; Study Guide</title>", head, count=1, flags=re.S)
head = re.sub(r"<header class=\"top\">.*?</header>",
  '<header class="top">\n  <h1>Pharmacology I &middot; Exam 1 &mdash; Study Guide</h1>\n'
  '  <p>PAJ 5410 Pharmacology I &middot; Class of 2028</p>\n'
  '  <p>Covers Lecture 1, Antibiotics, Antivirals and Antifungals &middot; further sections are '
  'added as each Exam 1 lecture is posted &middot; Instructional Objectives (IOs) taken verbatim '
  'from the syllabus &middot; drug dosages are not tested</p>\n</header>',
  head, count=1, flags=re.S)

html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + BODY + tail
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
print("audio attr present (should be False):", "data-audio-dir" in html)
print("donor palette remaining:", [c for c in ("#1f4d2b", "#c2903a", "#3f8a55") if c in html] or "none")
print("figures:", html.count('class="fig"'), "| test-yourself buttons:", html.count("test-yourself-btn"))
