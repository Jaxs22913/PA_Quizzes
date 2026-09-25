# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 study guide -- section 4, Lecture 7 (Lipids).

Imported by build_pharm_e2_guide.py.

SOURCES
  Facts   Lipids.pptx (70 slides), mapped in
          ~/Developer/PA_Quizzes-handoff/2026-09-23/work/pharm-l6l7/lipids-map.md.
          Image-only slides used from the map's viewed transcriptions: the LDL
          receptor cycle (13), the niacin mechanism (52), the LDL algorithm (66)
          and the statin intensity table (68, whose cells are doses and are left
          out -- only the three definitions and the two high-intensity agents).
  Weight  .../audio-pharm-l6l7/l7-lipids-emphasis.md. Stars are its section 4.2
          list; the scope callout is its section 2.2. His quantifier inflation
          (section 3.1) is NOT carried: the statin liver line is starred WITH
          "exceedingly rare", statin + fibrate is "cautiously", resins are not
          called the weakest agent, rosuvastatin is "minimal CYP".

THE MEMORY AID. Jaxon asked (2026-09-23, memory_aid_systems) for the lipoprotein
"garbage system": HDL = garbage trucks, and every other player given a role in
the same story. The cast is the one drafted for the CMS Lecture 22 guide
(work/build-cms-e4/l22-garbage-system-analogy.md: liver = depot, intestine =
port, LDL = building-material delivery truck, VLDL = fuel tanker, LDL receptor =
receiving gate, PCSK9 = demolition crew, bile = sewer) so the two guides tell one
story. Here it is extended with the DRUGS, and every drug role maps to a
mechanism this deck states (slides in brackets in the box). It is labeled as a
memory aid, sits above the detail it explains, and says where it breaks.

Scope conflicts flagged, not resolved: slide 65's ">7.5%" against slide 66's
">10%" -- the guide lists the four groups from 65 and gives the algorithm's
branches as the algorithm's, without a question depending on either.
"""

TOC = '''  <a class="top-link" href="#lipid">4 &middot; Drugs that Lower Cholesterol and Triglyceride Levels</a>
  <a href="#lipid-transport">4.1 Objectives 1&ndash;2 &mdash; Lipid transport, and the memory aid</a>
  <a href="#lipid-statin">4.2 Objectives 1&ndash;8 &mdash; Statins</a>
  <a href="#lipid-ezetimibe">4.3 Objectives 1&ndash;8 &mdash; Ezetimibe</a>
  <a href="#lipid-resin">4.4 Objectives 1&ndash;8 &mdash; Bile acid sequestrants</a>
  <a href="#lipid-fibrate">4.5 Objectives 1&ndash;8 &mdash; Fibrates</a>
  <a href="#lipid-niacin">4.6 Objectives 1&ndash;8 &mdash; Niacin</a>
  <a href="#lipid-pcsk9">4.7 Objectives 1&ndash;6 &mdash; PCSK9 inhibitors</a>
  <a href="#lipid-compare">4.8 Objective 3 &mdash; Which class for which lipid</a>
  <a href="#lipid-guide">4.9 Objectives 9&ndash;10 &mdash; Guidelines, monitoring and patient education</a>'''

BODY = '''
<section class="deck" id="lipid">
  <h2 class="deck-title">4 &middot; Drugs that Lower Cholesterol and Triglyceride Levels</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify drug classes and commonly prescribed drugs that lower cholesterol and triglyceride levels.</li>
      <li>Describe the molecular mechanism of action of drugs that lower cholesterol and triglyceride levels.</li>
      <li>Identify indications for commonly used drugs that lower cholesterol and triglyceride levels.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of drugs that lower cholesterol and triglyceride levels.</li>
      <li>Summarize side effects and toxic manifestations of drugs that lower cholesterol and triglyceride levels.</li>
      <li>Describe adverse effects of drugs that lower cholesterol and triglyceride levels.</li>
      <li>Identify contraindications for drugs that lower cholesterol and triglyceride levels.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs that lower cholesterol and triglyceride levels.</li>
      <li>List commonly used protocols and patient monitoring for drugs that lower cholesterol and triglyceride levels.</li>
      <li>Outline appropriate patient education for drugs that lower cholesterol and triglyceride levels.</li>
    </ol>
  </div>

  <div class="callout"><strong>What he said is not examined, or not in depth.</strong>
  <ul>
    <li><strong>Choosing a statin intensity for a patient scenario</strong> &mdash; &ldquo;am I going
    to get so granular&hellip; probably not.&rdquo; What <em>is</em> asked: which statins can be
    high intensity.</li>
    <li><strong>Calculating 10-year risk</strong> &mdash; &ldquo;I wouldn&rsquo;t have you calculate
    the 10-year risk for a person.&rdquo; Recognizing the four statin benefit groups <em>is</em>
    asked.</li>
    <li><strong>The statin pharmacokinetics table, apart from its enzyme row</strong> &mdash;
    absorption, bioavailability, protein binding, half-lives, food effects and prodrug status step
    back; <em>&ldquo;the biggest things to focus on&rdquo;</em> are the CYP interactions.</li>
    <li><strong>IDL</strong> (intermediate-density lipoprotein) &mdash; &ldquo;not going to be a big
    player here for our purposes.&rdquo;</li>
    <li><strong>Ezetimibe with cyclosporine</strong> &mdash; rare in practice; the antacid
    interaction is the one that comes up.</li>
    <li>No doses: the dosing slides for ezetimibe, the resins, niacin and the lovastatin-niacin
    combination were skipped, and the intensity table is taught without its milligrams.</li>
  </ul>
  His question style here: <em>&ldquo;slight difference in the question, totally different
  answer&rdquo;</em> &mdash; the same drug property as the key to one lead-in and the trap in the
  next (a resin <em>lowers</em> LDL cholesterol, but is <em>contraindicated</em> when triglycerides
  are high).</div>

  <h3 class="sub" id="lipid-transport">4.1 &middot; Objectives 1&ndash;2 &mdash; Lipid transport, and the memory aid</h3>

  <div class="callout"><strong>Memory aid &mdash; the city&rsquo;s cholesterol logistics (the
  &ldquo;garbage system&rdquo;).</strong> <em>A story to hang the slide facts on, the same cast as the
  Clinical Medicine and Surgery I lipid memory aid. When a question asks for a fact, answer from the
  facts below it, not from the story.</em>
  <ul>
    <li>The <strong>liver is the depot</strong>: it ships lipoproteins out, takes them back in, and
    sends cholesterol down the <strong>bile, the sewer</strong> [slides 7, 8, 12]. The
    <strong>intestine is the port</strong> where dietary fat arrives [5, 7].</li>
    <li><strong>Chylomicrons are the port&rsquo;s fuel barges</strong> (dietary fat) and
    <strong>VLDL (very-low-density lipoprotein) is the depot&rsquo;s fuel tanker</strong>
    (triglyceride-rich). <strong>Lipoprotein lipase is the unloading crew</strong>: it empties the
    fuel into the tissues, and the emptied tanker becomes IDL, then LDL [7&ndash;10].</li>
    <li><strong>LDL (low-density lipoprotein) is the building-material delivery truck.</strong> Its
    one badge, <strong>ApoB-100</strong>, is what the gate scans [12].</li>
    <li><strong>The LDL receptor is the depot&rsquo;s receiving gate</strong>: it pulls about 75% of
    delivery trucks off the road, mostly in the liver, and is recycled back to the surface after each
    truck [12, 13]. Too few gates, and trucks pile up on the road &mdash; atherosclerosis [12].</li>
    <li><strong>HDL (high-density lipoprotein) trucks are the garbage trucks</strong>: made in the
    intestine and liver, they collect cholesterol and bring it back for the liver to take up [7, 10].</li>
    <li><strong>PCSK9 is the demolition crew</strong> that processes the receiving gates [60].</li>
  </ul>
  <strong>Now every drug in this lecture has a job in the city:</strong>
  <ul>
    <li><strong>Statins cut the depot&rsquo;s own output</strong> (block HMG-CoA reductase, its
    cholesterol synthesis line) &mdash; and the depot, short of material, <strong>opens more
    receiving gates</strong> to pull delivery trucks off the road [18].</li>
    <li><strong>Ezetimibe narrows the port&rsquo;s import gate</strong> (less intestinal cholesterol
    absorbed), so less material reaches the depot &mdash; and it too opens more gates [27, 28].</li>
    <li><strong>Bile acid sequestrants block the sewer&rsquo;s recycling loop</strong>: they trap bile
    acids in the gut so they cannot be reclaimed, the depot burns more cholesterol to make new bile
    acids and opens more gates &mdash; but it may also dispatch more fuel tankers, so triglycerides
    can rise [41, 42, 46].</li>
    <li><strong>Fibrates send out fewer fuel tankers</strong> (less VLDL secreted, so triglycerides
    fall) and <strong>build more garbage-truck chassis</strong> (more ApoA-1, so HDL rises) [34].</li>
    <li><strong>Niacin cuts the fuel line from the fat stores to the depot</strong>, so fewer tankers
    are built and fewer delivery trucks follow; HDL rises [52, 53].</li>
    <li><strong>PCSK9 inhibitors stop the demolition crew</strong>, so the gates stay open longer
    [60].</li>
  </ul>
  <strong>Where it breaks:</strong> trucks are concentrations, not vehicles with intent; how HDL
  collects and hands on cholesterol (LCAT, CETP, SR-BI) is shown only in a figure; the statins&rsquo;
  pleiotropic effects have no place in the story; and the story teaches no plaque mechanism.</div>

  <p><strong>Two sources of fat.</strong> Dietary (exogenous) fat is packed in the intestine into
  <strong>chylomicrons</strong>, carried by the lymph to the blood, stripped of triglyceride by
  <strong>lipoprotein lipase</strong> (releasing free fatty acids and glycerol), and the
  <strong>chylomicron remnant</strong> is removed by the liver through the LDL receptor-like protein.
  The liver makes its own (endogenous) triglyceride-rich <strong>VLDL</strong> from carbohydrate and
  fatty acids; lipoprotein lipase turns it into <strong>IDL</strong>, about half of which becomes
  <strong>LDL</strong> while half returns to the liver. In the enterocyte, dietary cholesterol is
  taken up through a cholesterol transporter (NPC1L1) and esterified before packaging.</p>

  <p><strong>LDL</strong> has one apolipoprotein, <strong>ApoB-100</strong>, the ligand for its
  receptor. About 75% of LDL is cleared by the <strong>LDL receptor</strong>, most of it in the liver;
  the receptor carries LDL into the cell, the lysosome breaks it down and releases its cholesterol,
  and the receptor returns to the surface. <strong>Less receptor activity means LDL accumulates, and
  atherosclerosis follows.</strong> Oxidized LDL enters macrophages through scavenger receptors (CD36
  and SR-A). <strong>HDL</strong> is made in the intestine and liver and is catabolized by handing
  cholesteryl ester to VLDL and LDL and by hepatic uptake.</p>

  <div class="pearl"><strong>The key point he returned to four times.</strong> Getting lipoproteins
  into the liver needs receptors, <em>&ldquo;and that&rsquo;s going to be a key point with some of
  our medications&rdquo;</em>. Statins, ezetimibe, the resins and the PCSK9 inhibitors all end in the
  same place: <strong>more working LDL receptors on the liver</strong>. What differs is how they get
  there.</div>

  <h3 class="sub" id="lipid-statin">4.2 &middot; Objectives 1&ndash;8 &mdash; Statins</h3>

  <p><strong>Class and agents:</strong> HMG-CoA (3-hydroxy-3-methylglutaryl coenzyme A) reductase
  inhibitors &mdash; lovastatin, simvastatin, pravastatin, fluvastatin, atorvastatin, rosuvastatin,
  pitavastatin. <strong>Mechanism:</strong> <mark class="prof-highlight">Reduce hepatic cholesterol
  synthesis, lowering intracellular cholesterol, which stimulates upregulation of LDL receptor and
  increases the uptake of non-HDL particles from the systemic circulation.</mark> LDL, VLDL remnants
  and IDL all fall. They also have <strong>pleiotropic effects</strong> beyond lipids: better
  endothelial function, plaque stabilization, inhibition of vascular smooth muscle growth, platelet
  inhibition, reduced leukocyte adhesiveness and inflammatory markers, among others.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><mark class="prof-highlight">Most efficacious and best tolerated of
    all agents</mark> &mdash; <mark class="prof-highlight">first line therapy when LDL-C lowering
    drugs are indicated</mark> (LDL-C = low-density lipoprotein cholesterol). <em>&ldquo;Statins 10
    times out of 10.&rdquo;</em></p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><strong>Metabolism (Objective 4) &mdash; the one row of the
    pharmacokinetics table to know:</strong> <mark class="prof-highlight">atorvastatin, lovastatin
    and simvastatin are metabolized by CYP3A4</mark> (cytochrome P450 3A4); fluvastatin by CYP2C9;
    pravastatin enzymatically and non-enzymatically, not by CYP; <mark class="prof-highlight">rosuvastatin
    minimal CYP</mark>; pitavastatin by glucuronidation. <em>&ldquo;Definitely know these&hellip; it
    may come up on a test.&rdquo;</em></p>
    <p><strong>Interactions:</strong> <mark class="prof-highlight">CYP-450 mediated interaction
    (especially CYP3A4 inhibitors and substrates) &mdash; verapamil, amiodarone, niacin, fibric acid
    derivatives, grapefruit juice</mark>. Grapefruit juice is the lecture&rsquo;s only drug-food
    interaction. Link it to section 3.4: the non-dihydropyridines that raise these three statins are
    CYP3A4 inhibitors.</p>
  </div>

  <table>
    <tr><th>Adverse effect</th><th>What the slide says</th></tr>
    <tr><td>Common</td><td>Headache, sleep disturbance, fatigue, gastrointestinal intolerance, flu-like symptoms</td></tr>
    <tr><td><strong>Liver enzymes</strong></td><td><mark class="prof-highlight">Increase in liver enzymes &mdash; occurs in 0.5 to 2.5% of cases, in a dose-dependent manner &mdash; serious liver problems are exceedingly rare</mark>. Manage by <strong>reducing the dose, or stopping until levels return to normal</strong></td></tr>
    <tr><td><strong>Muscle</strong></td><td><mark class="prof-highlight">Myalgia; myopathy; rare cases of rhabdomyolysis</mark>. Reduce the risk with caution in renal impairment, the lowest effective dose, <mark class="prof-highlight">cautiously combining statins with fibrates</mark>, avoiding other interactions, and monitoring symptoms and laboratory values. <mark class="prof-highlight">Presence of muscle toxicity requires the discontinuation of the statin</mark></td></tr>
  </table>

  <p><strong>Contraindications:</strong> <mark class="prof-highlight">hepatic disease; pregnancy</mark>.
  Relative: concomitant cyclosporine or other immunosuppressants, <strong>gemfibrozil</strong>,
  niacin and erythromycin. Pregnancy puts statins in the same group as ACE inhibitors and angiotensin
  receptor blockers from Lecture 6 &mdash; the three he called a &ldquo;no-go&rdquo;. The contrast
  that makes a good question: the <strong>bile acid sequestrants are approved in pregnancy</strong>
  (4.4).</p>

  <h3 class="sub" id="lipid-ezetimibe">4.3 &middot; Objectives 1&ndash;8 &mdash; Ezetimibe</h3>

  <p><strong>Ezetimibe (Zetia)</strong>, the cholesterol absorption inhibitor, <strong>selectively
  inhibits intestinal cholesterol absorption</strong> at the brush border, so less cholesterol
  reaches the liver, <strong>hepatic LDL receptors increase</strong>, and atherogenic particles carry
  less cholesterol. With a statin it gives &ldquo;dual inhibition&rdquo; of the two sources &mdash;
  the statin on synthesis, ezetimibe on absorption &mdash; and adds further LDL lowering.
  <strong>Absorption and metabolism:</strong> ezetimibe and its active glucuronide metabolite
  <strong>circulate enterohepatically</strong>, which returns the drug to its site of action and
  limits systemic exposure; it may be taken with or without meals.</p>

  <table>
    <tr><th>Adverse effects</th><th>Interactions</th></tr>
    <tr><td>Gastrointestinal effects; <strong>raised hepatic transaminases when combined with a statin</strong>. No contraindications are listed.</td><td><strong>Fibrates</strong> increase hepatobiliary side effects &mdash; <strong>cholelithiasis</strong> and myopathies; <strong>bile acid sequestrants lower its concentration</strong>; <strong>antacids lower its concentration</strong>; cyclosporine raises it</td></tr>
  </table>

  <h3 class="sub" id="lipid-resin">4.4 &middot; Objectives 1&ndash;8 &mdash; Bile acid sequestrants</h3>

  <p><strong>Agents:</strong> cholestyramine (Questran), colestipol (Colestid), colesevelam (Welchol).
  <strong>Mechanism:</strong> they bind bile acids in the gut and <strong>prevent their enterohepatic
  recirculation</strong> at the terminal ileum, so they are lost in the feces. The liver makes more
  bile acid from cholesterol (cholesterol 7-alpha-hydroxylase rises) and makes <strong>more LDL
  receptors</strong>, so LDL and VLDL are removed and LDL cholesterol falls.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><mark class="prof-highlight">Not absorbed in the GI tract</mark>
    (gastrointestinal) &mdash; so no systemic side effects &mdash; and therefore
    <mark class="prof-highlight">approved for children, adolescence and pregnancy</mark>. The
    &ldquo;safest drug because no systemic side effects&rdquo;, but <strong>poorly
    tolerated</strong>, and used mainly with a statin or when only a modest LDL reduction is
    needed.</p>
  </div>

  <p><strong>Adverse effects:</strong> gastrointestinal &mdash; bloating, flatulence, fullness,
  <strong>constipation</strong>, nausea; <strong>malabsorption of vitamins A, D, E and K and of folic
  acid</strong>; the resin&rsquo;s chloride raises calcium excretion; raising the dose may add side
  effects without more benefit; and one that turns into a contraindication:
  <mark class="prof-highlight">may increase VLDL production &rarr; &uarr; TG</mark> (triglycerides).</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><strong>Contraindications.</strong> <mark class="prof-highlight">Absolute:
    familial dysbetalipoproteinemia (increased TG); triglycerides &gt; 400 mg/dL. Relative:
    triglycerides &gt; 200 mg/dL.</mark></p>
    <p>His example stem: a patient with triglycerides of 600 &mdash; <em>which of these is
    contraindicated?</em> The resin. <em>&ldquo;Slight difference in the question, totally different
    answer.&rdquo;</em></p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><strong>Interactions and administration.</strong> Anion-exchange resins
    interfere with the absorption of <strong>digoxin, warfarin, thyroxine, beta blockers and thiazide
    diuretics</strong> &mdash; <mark class="prof-highlight">avoid the interaction by administering the
    drug 1 hour before or 4 hours after the bile acid sequestrant</mark>. They also lower ezetimibe
    levels and interact with fibrates and niacin. Patient education: powders are <strong>mixed with
    water or fruit juice</strong> (a pulpy drink masks the taste), taken <strong>within 1 hour of a
    meal</strong> &mdash; bile acids are released with a meal, so there is something to bind &mdash;
    and <mark class="prof-highlight">separate other medications</mark>.</p>
  </div>

  <h3 class="sub" id="lipid-fibrate">4.5 &middot; Objectives 1&ndash;8 &mdash; Fibrates</h3>

  <p><strong>Agents:</strong> gemfibrozil (Lopid), fenofibrate (Tricor), bezafibrate (Bezalip SR).
  <strong>Mechanism:</strong> <mark class="prof-highlight">activates PPAR-alpha</mark>
  (peroxisome proliferator-activated receptor alpha, a nuclear transcription factor) &rarr; more fatty
  acid oxidation &rarr; less secretion of triglyceride-rich VLDL &rarr;
  <mark class="prof-highlight">decrease in triglycerides</mark>; and
  <mark class="prof-highlight">increases expression of ApoA-1 &rarr; increase in HDL</mark>. The
  figure adds more lipoprotein lipase and less ApoC-III.</p>

  <table>
    <tr><th>Indication</th><td><mark class="prof-highlight">Primary indication TG &gt; 1000 mg/dL or low HDL</mark></td></tr>
    <tr><th>Adverse effects</th><td>Gastrointestinal (nausea, abdominal pain, diarrhea); <strong>cholelithiasis</strong>; <strong>myopathy</strong></td></tr>
    <tr><th>Contraindications</th><td><strong>Pregnancy; severe hepatic or renal dysfunction; existing gallbladder disease</strong></td></tr>
    <tr><th>Interactions</th><td><strong>Increase the anticoagulant effect of warfarin</strong>; statins (myopathy &mdash; gemfibrozil is a relative contraindication with a statin); ezetimibe (gallstones); bile acid sequestrants</td></tr>
  </table>

  <p>His example stem: a patient whose only problem is very high triglycerides &mdash; which drug is
  best at lowering them? <em>&ldquo;It&rsquo;s either the fibrates or&rdquo;</em> niacin.</p>

  <h3 class="sub" id="lipid-niacin">4.6 &middot; Objectives 1&ndash;8 &mdash; Niacin</h3>

  <p><strong>Niacin (nicotinic acid)</strong> is a B-complex vitamin; its amide,
  <strong>niacinamide (nicotinamide), is not an antilipemic</strong>. <strong>Mechanism:</strong> it
  reduces the mobilization of free fatty acids from adipose tissue, so the liver makes less
  triglyceride and <strong>less VLDL and apolipoprotein B</strong>, so less LDL is formed; and
  <strong>HDL rises</strong> &mdash; the largest HDL rise of any class. Products come as immediate
  release (a supplement, and Niacor), long-acting (supplement) and extended release (Niaspan).
  <strong>Indication:</strong> atherogenic dyslipidemia, including in combination when LDL is also
  high.</p>

  <table>
    <tr><th>Adverse effects</th><td><mark class="prof-highlight">Cutaneous flushing &mdash; prostaglandin mediated effect &mdash; minimized by premedication with ASA</mark> (aspirin), which blocks prostaglandin synthesis; nausea and abdominal discomfort; at larger doses <strong>raised liver enzymes, glucose and uric acid</strong>, and reduced glucose tolerance. The slide also lists immediate against extended release under adverse effects</td></tr>
    <tr><th>Contraindications</th><td><mark class="prof-highlight">Absolute: chronic liver disease. Relative: peptic ulcer disease, history of symptomatic gout, significant hyperuricemia, diabetes (glucose intolerance)</mark></td></tr>
    <tr><th>Interactions</th><td>Statins; bile acid sequestrants; <strong>alcohol</strong></td></tr>
  </table>

  <p>Each relative contraindication is one of niacin&rsquo;s own adverse effects meeting a patient who
  already has it: raised uric acid in gout, raised glucose in diabetes, the liver in liver disease.
  The <strong>lovastatin/niacin extended-release combination (Advicor)</strong> carries the adverse
  effects of both &mdash; hepatotoxicity, myopathy and flushing.</p>

  <h3 class="sub" id="lipid-pcsk9">4.7 &middot; Objectives 1&ndash;6 &mdash; PCSK9 inhibitors</h3>

  <p><strong>Alirocumab (Praluent) and evolocumab (Repatha)</strong> &mdash; the -mab tells you they
  are <strong>monoclonal antibodies</strong>, so they are <strong>injectable only</strong>, and they
  are expensive. PCSK9 (proprotein convertase subtilisin/kexin type 9) is <strong>responsible for
  processing hepatic LDL receptors</strong>; blocking it <strong>keeps LDL receptors active
  longer</strong>, and LDL falls by roughly half. <strong>The most serious adverse reaction is
  hypersensitivity.</strong> The slide gives no indications, contraindications or interactions.</p>

  <h3 class="sub" id="lipid-compare">4.8 &middot; Objective 3 &mdash; Which class for which lipid</h3>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <table>
      <tr><th>Class</th><th>LDL cholesterol</th><th>HDL cholesterol</th><th>Triglycerides</th></tr>
      <tr><td>Statins</td><td>&darr; 18&ndash;55%</td><td>&uarr; 5&ndash;15%</td><td>&darr; 7&ndash;30%</td></tr>
      <tr><td>Resins</td><td>&darr; 15&ndash;50%</td><td>&uarr; 3&ndash;5%</td><td><mark class="prof-highlight">No change / &uarr;</mark></td></tr>
      <tr><td>Nicotinic acid</td><td>&darr; 5&ndash;25%</td><td><mark class="prof-highlight">&uarr; 15&ndash;35%</mark></td><td><mark class="prof-highlight">&darr; 20&ndash;50%</mark></td></tr>
      <tr><td>Fibrates</td><td>&darr; 5&ndash;20%</td><td><mark class="prof-highlight">&uarr; 10&ndash;35%</mark></td><td><mark class="prof-highlight">&darr; 20&ndash;50%</mark></td></tr>
      <tr><td>Ezetimibe</td><td>&darr; 18%</td><td>Insignificant</td><td>&darr; 8%</td></tr>
    </table>
    <p>Three of his test-question cues aim at this table. Read it for <strong>direction and
    ranking</strong>, not the percentages: statins are the first-line LDL drug; <strong>niacin and the
    fibrates lower triglycerides and raise HDL</strong>; and the resins are <em>&ldquo;the only one
    that&rsquo;s bad for triglycerides&rdquo;</em>.</p>
  </div>

  <h3 class="sub" id="lipid-guide">4.9 &middot; Objectives 9&ndash;10 &mdash; Guidelines, monitoring and patient education</h3>

  <p>The older <strong>Adult Treatment Panel III (ATP III)</strong> goals were numbers: LDL under 100
  mg/dL optimal, HDL over 60 high and under 40 low, total cholesterol under 200, triglycerides under
  150. HDL rises with exercise. The <strong>American Heart Association and American College of
  Cardiology (AHA/ACC)</strong> guideline aims to reduce atherosclerotic cardiovascular disease
  (ASCVD) risk, the leading cause of death and disability in America, and changed the approach:</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <ul>
      <li>Start <strong>moderate- or high-intensity statin</strong> therapy for patients in the four
      groups.</li>
      <li><mark class="prof-highlight">Unlike ATP-III, do not titrate to a specific LDL cholesterol
      target.</mark></li>
      <li><mark class="prof-highlight">Measure lipids during follow-ups to assess adherence to
      treatment</mark>, not to reach a target.</li>
    </ul>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><strong>The four major statin benefit groups</strong> &mdash;
    <em>&ldquo;I would want you to be able to identify those four risk categories.&rdquo;</em></p>
    <ol>
      <li>Clinical ASCVD.</li>
      <li>LDL above 190 mg/dL.</li>
      <li>Diabetes, age 40 to 75, LDL 70 to 189 mg/dL, and no clinical ASCVD.</li>
      <li>No clinical ASCVD or diabetes, LDL 70 to 189 mg/dL, and an estimated 10-year ASCVD risk
      above 7.5%.</li>
    </ol>
  </div>

  <p><strong>Statin intensity</strong> is defined by the LDL reduction it produces: <strong>high,
  50% or more</strong>; <strong>moderate, 30 to 49%</strong>; <strong>low, under 30%</strong>.
  <mark class="prof-highlight">Only atorvastatin and rosuvastatin</mark> reach high intensity.
  <strong>Safety:</strong> choose the appropriate dose; keep side effects and drug interactions in
  mind; and <strong>if high- or moderate-intensity therapy is not tolerated, use the maximum tolerated
  dose</strong>.</p>

  <p>The algorithm on slide 66 (adults without cardiovascular disease) runs: measure LDL and counsel
  everyone on lifestyle; <strong>LDL 190 mg/dL or more</strong> &rarr; evaluate for familial
  hypercholesterolemia, and if absent start a <strong>high-intensity statin</strong>; otherwise
  calculate 10-year risk and branch &mdash; start a moderate-dose statin, discuss it with the patient,
  or repeat screening. After starting, <strong>repeat LDL in 6 weeks and expect a 30 to 50%
  fall</strong>; if it has not fallen, <strong>evaluate compliance</strong>. (The algorithm&rsquo;s
  risk cut-offs are not the same as the 7.5% on the benefit-group slide; no question should turn on
  the difference.)</p>

  <table>
    <tr><th>Drug</th><th>Patient education the slides support</th></tr>
    <tr><td>Statins</td><td>Report muscle pain or weakness; avoid grapefruit juice; not in pregnancy; lipids are rechecked to confirm the drug is being taken</td></tr>
    <tr><td>Ezetimibe</td><td>With or without meals</td></tr>
    <tr><td><strong>Bile acid sequestrants</strong></td><td>Mix the powder in water or a pulpy fruit juice; take within 1 hour of a meal; take other medicines 1 hour before or 4 hours after; constipation and bloating are common</td></tr>
    <tr><td>Niacin</td><td>Flushing is expected &mdash; take aspirin beforehand to reduce it; alcohol interacts</td></tr>
    <tr><td>PCSK9 inhibitors</td><td>An injection; watch for hypersensitivity</td></tr>
  </table>

</section>
'''
