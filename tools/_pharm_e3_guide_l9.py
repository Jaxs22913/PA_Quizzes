# -*- coding: utf-8 -*-
"""Pharmacology I Exam 3 study guide -- section 1, Lecture 9 (Diuretics and Heart Failure Drugs).

Imported by build_pharm_e3_guide.py.

SOURCES
  Facts   "Diuretics and Heart Failure Drugs.pptx" (83 slides; Adam Wood, Pharm.D., DABAT).
          `python3 tools/pharm_e3_lib.py dump L9` prints the slide text; the picture-only slides
          (6, 7, 12, 21, 30, 34, 41, 49, 61, 62, 70, 74) were read by eye and live in
          tools/pharm_e3/ocr.json under "L9". Slide numbers in square brackets in the body are that
          deck's slide numbers.
  Weight  Dr. Wood's live recording of 2026-09-30 (rebased times: 0:00 = start of this lecture). The star
          boxes quote it with their timestamps; stars only set weight, they add no fact. The recording
          has automatic-transcript slips (digoxin heard as "jox", eplerenone as "naporinone", and so on);
          the quotes are cleaned of them (tools/pharm_e3/wood.json checks the exact wording).

NO DOSES. Dr. Wood does not test dosages. No milligram amount appears anywhere below. Durations, routes,
thresholds (potassium, heart rate) and the percentages of sodium each nephron site handles stay, as
recognition-only facts. The digoxin target level is stated once and flagged: he said he would probably
not quiz it.

TRUTH WINS ON CONFLICT (standing rule). Every place the deck is wrong, loose or contradicts itself has a
short "Deck versus truth" callout: slide 9 (descending limb), slide 10 (aldosterone and water), slides 21
and 42 (carbonic anhydrase side facts), slide 23 (uric acid), slide 24 (thiazides and hypercalcemia), slide 25 (obese and first line), slide 28 (low clearance),
slide 30 (antiporters), slide 38 (spironolactone is an androgen receptor antagonist, not a partial agonist), slide 36 (calcium, lag), slide 37 versus 73 (class IV or III and IV), slide 46 (45 percent), slides 51, 52 and 58 (numbers), slide 62 (calcium exchanger), slide 67 (first line), slides 68 and 80 (the two kinds of halos),
slide 71 (hyperkalemia), slide 72 (antibody wording), slide 77 (dopamine and the kidney), slide 79 (ivabradine mortality), slides 81 and 82 (washout reason, fungal infection site), and the boxed warnings the slides omit. The wrong ones are NOT keyed.

SLIDES NOT COVERED: 1 (title), 2 (the deck's own objectives; the syllabus wording is used), 3, 44 and 78
(section dividers), 83 ("Questions?"). Every other slide is represented.
"""

TOC = '''  <a class="top-link" href="#diuretics-hf">1 &middot; Diuretics and Heart Failure Drugs</a>
  <a href="#dh-frame">1.1 Objectives 1&ndash;3 &mdash; Diuretics: the frame and the nephron (with a memory aid)</a>
  <a href="#dh-loop">1.2 Objectives 1&ndash;8 &mdash; Loop diuretics</a>
  <a href="#dh-thiazide">1.3 Objectives 1&ndash;8 &mdash; Thiazide diuretics</a>
  <a href="#dh-ksparing">1.4 Objectives 1&ndash;8 &mdash; Potassium-sparing diuretics</a>
  <a href="#dh-aldo">1.5 Objectives 1&ndash;7 &mdash; Aldosterone and aldosterone antagonists</a>
  <a href="#dh-cai">1.6 Objectives 1&ndash;7 &mdash; Carbonic anhydrase inhibitors</a>
  <a href="#dh-hf">1.7 Objectives 1&ndash;2 &mdash; Heart failure: causes, types and compensation</a>
  <a href="#dh-hfdiur">1.8 Objectives 1&ndash;7 &mdash; Heart failure: diuretics and angiotensin-converting enzyme inhibitors</a>
  <a href="#dh-hfbb">1.9 Objectives 1&ndash;7 &mdash; Heart failure: beta blockers</a>
  <a href="#dh-digoxin">1.10 Objectives 1&ndash;3 &mdash; Digoxin: action, benefit and place</a>
  <a href="#dh-digtox">1.11 Objectives 5&ndash;8 &mdash; Digoxin toxicity, contraindications and the antidote</a>
  <a href="#dh-hfother">1.12 Objectives 1&ndash;7 &mdash; Aldosterone antagonists in heart failure and the other inotropic agents</a>
  <a href="#dh-newer">1.13 Objectives 1&ndash;7 &mdash; Newer agents: ivabradine, sacubitril-valsartan, sodium-glucose cotransporter 2 inhibitors</a>
  <a href="#dh-summary">1.14 Objectives 4 and 8&ndash;10 &mdash; Absorption, interactions, monitoring and patient education</a>'''

BODY = '''
<section class="deck" id="diuretics-hf">
  <h2 class="deck-title">1 &middot; Diuretics and Heart Failure Drugs</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify diuretics and heart failure drug classes and commonly prescribed diuretics and heart failure drugs.</li>
      <li>Describe the molecular mechanism of action of diuretics and heart failure drugs.</li>
      <li>Identify indications for commonly used diuretics and heart failure drugs.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of diuretics and heart failure drugs.</li>
      <li>Summarize side effects and toxic manifestations of diuretics and heart failure drugs.</li>
      <li>Describe adverse effects of diuretics and heart failure drugs.</li>
      <li>Identify contraindications for diuretics and heart failure drugs.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with diuretics and heart failure drugs.</li>
      <li>List commonly used protocols and patient monitoring for diuretics and heart failure drugs.</li>
      <li>Outline appropriate patient education for diuretics and heart failure drugs.</li>
    </ol>
  </div>

  <div class="callout"><strong>This is the first of five lectures in Exam 3.</strong> The syllabus puts Lectures 9
  to 13 in Exam 3 (Thursday, December 3, 2026): (9) diuretics and heart failure drugs; (10) antiarrhythmic drugs; (11) drugs for
  pulmonary infections, asthma and chronic obstructive pulmonary disease (COPD); (12) hematological drugs; and (13) oncology drugs. Lecture 9 was delivered live on
  September 30, 2026 and is the only one built so far. The recording of that lecture ran through the whole deck.
  Dr. Wood said at 0:00 that he might need extra time on it at the next lecture, and at 36:53 that he might save
  leftovers; he got through every slide.</div>

  <div class="callout"><strong>What he stresses, and what is not examined or not in depth.</strong>
  <ul>
    <li><strong>The standing rule for the whole lecture.</strong> &ldquo;If I say something is good for mortality purposes&hellip; that means you want the patient on it no matter what. If it&rsquo;s just good for symptom management, then they may not need to be on it all the time&rdquo; (at 40:55). Diuretics are symptom drugs; angiotensin-converting enzyme (ACE) inhibitors, three named beta blockers and the aldosterone antagonists are survival drugs.</li>
    <li><strong>Potassium, drug by drug.</strong> &ldquo;You got to know what these medications are doing to your potassium&hellip; you can kill somebody very easily with potassium&rdquo; (at 6:11). Every class below states whether it lowers or raises potassium.</li>
    <li><strong>The digoxin target level is probably not examined.</strong> &ldquo;I&rsquo;m probably not going to quiz you specifically on the level on the test, but just know that this has a very tight therapeutic index&rdquo; (at 48:35).</li>
    <li><strong>Doses.</strong> This site leaves milligram amounts out (dosages are not tested in this course); this deck gives none.</li>
    <li><strong>Where the deck is wrong, loose or out of date,</strong> the guide says so in a box headed &ldquo;Deck versus truth&rdquo; and follows the truth. Those points are not to be memorized as the slide words them.</li>
  </ul></div>

  <h3 class="sub" id="dh-frame">1.1 &middot; Objectives 1&ndash;3 &mdash; Diuretics: the frame and the nephron</h3>

  <p><strong>Diuretics</strong> are drugs that increase urine flow and/or sodium and chloride excretion [slide 4].
  A sustained imbalance between sodium and chloride intake and loss is fatal [slide 4]. Too much sodium and
  water means <strong>volume overload and pulmonary edema</strong>; too little means <strong>volume depletion and
  cardiovascular collapse</strong> [slide 4]. The goal is the middle zone between the two.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 0:23 of the recording: <em>&ldquo;These are helping to block the reabsorption of sodium and chloride in the renal tubule, which will then cause water to flow with it. This is the general rule I&rsquo;ll use, that wherever salt goes, water wants to follow.&rdquo;</em></p>
    <p>A diuretic <mark class="prof-highlight">blocks sodium and chloride reabsorption, and water follows the salt into the urine</mark> [slide 4].</p>
  </div>

  <p><strong>The kidney fights back (&ldquo;diuretic braking&rdquo;).</strong> The kidneys receive about 22 percent of the cardiac output and
  7 percent of the oxygen, although they are only 0.5 percent of body weight [slide 5]. Renal compensatory
  mechanisms prevent volume depletion and cardiovascular collapse, and this is called <strong>diuretic
  braking</strong> [slide 5]. It consists of activation of the sympathetic nervous system and the
  renin-angiotensin-aldosterone system, a fall in blood pressure (less pressure natriuresis), a fall in atrial
  natriuretic peptide with a rise in antidiuretic hormone, and renal cell hypertrophy [slide 5].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 1:08 of the recording: <em>&ldquo;I always talk about the kidneys being kind of like divas&hellip; they need their blood flow&hellip; they have a lot of these compensatory mechanisms, they have this diuretic braking action, where you&rsquo;ll see activation of the renin-angiotensin system, you&rsquo;ll see things like increase in ADH release&hellip; The kidneys don&rsquo;t like losing all that salt and all that extra volume, so they&rsquo;re going to be fighting you. And again, that&rsquo;s why you see synergy between things like ACE inhibitors and diuretics and calcium channel blockers, because they can all help to block some of these compensatory mechanisms.&rdquo;</em></p>
    <p>Diuretics set off compensation (more renin, aldosterone and antidiuretic hormone, abbreviated ADH), which limits how well they work; <mark class="prof-highlight">angiotensin-converting enzyme (ACE) inhibitors and calcium channel blockers are synergistic partners</mark> because they block those compensations [slide 5].</p>
  </div>

  <h4 class="subsub">Walking down the nephron [slides 6 to 11]</h4>
  <p>The nephron is the functional unit of the kidney (slide 6 pictures the kidney: cortex, medulla, nephron, renal
  artery, renal vein, ureter). Slide 7 pictures the nephron, from Bowman&rsquo;s capsule and the glomerulus through
  the proximal tubule, loop of Henle, distal tubule and collecting tubule, with glucose and amino acids leaving at
  the proximal tubule and aldosterone and antidiuretic hormone acting at the collecting end.</p>
  <table>
    <tr><th>Site</th><th>What happens there</th><th>Diuretic that works there</th></tr>
    <tr><td><strong>Glomerulus (filtration)</strong> [slide 7]</td><td>16 to 20 percent of the fluid and its solutes is filtered: glucose; sodium, potassium, chloride and bicarbonate; amino acids. 150 to 180 liters are filtered per day and 1 to 2 liters are excreted; the plasma is filtered about 50 to 60 times a day</td><td>None</td></tr>
    <tr><td><strong>Proximal tubule</strong> [slide 8]</td><td>Reabsorption of glucose, amino acids and organic solutes; weak acids and bases are excreted into the lumen; <strong>60 to 70 percent of the filtrate is reabsorbed</strong></td><td><strong>Carbonic anhydrase inhibitors</strong> [slide 39]</td></tr>
    <tr><td><strong>Loop of Henle</strong> [slide 9]</td><td>Concentrates the urine and reabsorbs sodium. In the descending limb water leaves the lumen. In the ascending limb <strong>25 percent of the sodium is reabsorbed</strong> and the limb is impermeable to water</td><td><strong>Loop diuretics</strong> [slide 9]</td></tr>
    <tr><td><strong>Distal tubule</strong> [slide 10]</td><td>About <strong>5 percent</strong> of the sodium is reabsorbed (the slide adds that water movement here is controlled by aldosterone; that is loose, see the box below)</td><td><strong>Thiazide diuretics</strong> [slide 10]</td></tr>
    <tr><td><strong>Collecting duct</strong> [slide 11]</td><td><strong>2 to 3 percent</strong> of the sodium is reabsorbed. The slide says water movement is controlled by aldosterone and by antidiuretic hormone; in truth <strong>antidiuretic hormone controls the water channels</strong> and aldosterone controls sodium and potassium handling (see the box below)</td><td><strong>Potassium-sparing diuretics</strong> [slide 11] (the aldosterone antagonists also act at this end of the nephron [slides 34 to 36])</td></tr>
  </table>
  <p>Drugs are taught in descending order of potency. For the first three sites that follows how much sodium the site
  handles: loop (25 percent), thiazide (5 percent), potassium-sparing and aldosterone antagonist (2 to 3 percent). The carbonic anhydrase
  inhibitors act at the proximal tubule, where most of the filtrate is reabsorbed, but they are the weakest diuretics, because everything
  downstream of the proximal tubule makes up for them [slides 8 and 39].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 4:24 of the recording: <em>&ldquo;So we&rsquo;ll see that some drugs will work in the proximal tubule, some work in the loop, some in the distal tubule and some in the collecting duct&hellip; we&rsquo;re going to go in descending order of potency. We&rsquo;re going to start with the most potent, the most bang for our buck in terms of urine formation.&rdquo;</em></p>
    <p>Learn <mark class="prof-highlight">which class works at which site, and that loops are the most potent</mark> [slides 9 to 11].</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; two nephron statements.</strong> (1) Slide 9 says that in the
  descending limb water leaves the lumen, which is true: <strong>the descending limb is permeable to water</strong>
  and the thick ascending limb is the impermeable one. Dr. Wood said the opposite of the descending limb at 3:25
  (a slip); the slide is right. (2) Slide 10 says water movement at the distal tubule is controlled by
  aldosterone, and slide 11 repeats it for the collecting duct. Aldosterone drives sodium and potassium handling in the late distal tubule and collecting duct;
  <strong>water movement in the collecting duct is controlled by antidiuretic hormone</strong>, which opens the
  water channels (the collecting-tubule picture on slides 30 and 34 shows the water channels under the
  antidiuretic hormone receptor). The percentages on slides 7 to 11 are recognition-only; no question
  rests on a bare percentage.</div>

  <div class="callout"><strong>Memory aid &mdash; the nephron as a river with an intake screen, three stations and a customs office.</strong>
  <em>A story to hang the slide facts on. When a question asks for a fact, answer from the facts in this
  section, not from the story.</em>
  <ul>
    <li><strong>The river is the filtrate</strong>, and <strong>the glomerulus is the intake screen</strong>: it lets
    the small things through (water, salts, glucose, amino acids) and keeps the big things back (proteins, red blood
    cells), which is why protein or blood in the urine is a bad sign [the screen is slide 7; the protein and blood point is from the recording, 2:40].</li>
    <li><strong>The body is a thrifty water company that wants its water back.</strong> The river has to be mostly
    recycled: 150 to 180 liters enter, only 1 to 2 leave [slide 7]. &ldquo;Where salt goes, water follows,&rdquo; so salt left in
    the river holds water in the river with it (the one exception is the waterproof wall of the ascending limb, below).</li>
    <li><strong>The proximal tubule is the big recycling dock</strong> (60 to 70 percent back, all the glucose and
    amino acids) [slide 8]. A bicarbonate conveyor belt (carbonic anhydrase) runs through it. <strong>Carbonic
    anhydrase inhibitors jam that belt.</strong> Bicarbonate is stranded in the river and is passed in the urine, so
    the blood turns slightly acidic [slides 39, 41 and 43] and the urine alkaline [from the recording, 30:44]. They are the weakest diuretics
    because the three stations downstream (loop, distal tubule, collecting duct) simply take the extra water back [slide 39; the word &ldquo;weakest&rdquo; is from the recording, 31:25].</li>
    <li><strong>The loop of Henle is the powerhouse station</strong>: the ascending limb has a waterproof wall
    and a big sodium-potassium-chloride carrier taking back 25 percent of the sodium [slides 9 and 12].
    <strong>Loop diuretics jam the biggest carrier</strong>, so they give the biggest flood of urine. The same jam
    spills calcium and magnesium and potassium into the river [slide 13].</li>
    <li><strong>The distal tubule is a small fine-tuning station</strong> (5 percent) [slide 10]. <strong>Thiazides
    jam its sodium-chloride gate</strong> and give a moderate flow. Unlike the loop jam, this station pulls
    even more calcium back, so urinary calcium falls [slide 22].</li>
    <li><strong>The collecting duct is the customs office with two officers.</strong> The <strong>aldosterone officer</strong>
    orders more sodium doors to be installed in the wall and more sodium-potassium pumps (the sodium-potassium ATPase) to run, trading potassium out
    for sodium in [slide 34]. The <strong>antidiuretic hormone officer</strong> opens the water channels [slides 11, 30 and 34].
    <strong>Potassium-sparing drugs board up the sodium doors</strong> [slide 30]; <strong>aldosterone antagonists
    jam the officer&rsquo;s mailbox</strong> (they sit on the steroid receptor, so the message never reaches the
    nucleus) [slide 36]. Either way the sodium-for-potassium swap stops, so potassium is spared, and the flow is only
    modest [slides 30 and 36].</li>
    <li><strong>The kidney is a diva and runs a counter-offensive.</strong> When the river is drained, it sends out the
    renin-angiotensin messengers, aldosterone and antidiuretic hormone to hold water back [slide 5]. ACE inhibitors
    and calcium channel blockers help block these compensations, which is why they pair well with diuretics (the pairing is from the recording, 1:48).</li>
  </ul>
  <strong>Where it breaks:</strong> the story says nothing about uric acid, blood sugar, hearing, or the contraction
  alkalosis that comes from the volume loss; it does not explain why carbonic anhydrase inhibitors also waste potassium [slide 43];
  it does not say that thiazides and loops both waste potassium and magnesium; and the &ldquo;mailbox&rdquo; picture does not
  explain why aldosterone antagonists work best when aldosterone is high [slide 36]. The &ldquo;pump&rdquo; for the sodium-potassium
  ATPase is not the same thing as the loop&rsquo;s &ldquo;carrier&rdquo;. For each of those, use the facts below.</div>
'''

BODY += '''
  <h3 class="sub" id="dh-loop">1.2 &middot; Objectives 1&ndash;8 &mdash; Loop diuretics</h3>

  <p><strong>Mechanism (Objective 2).</strong> Loop diuretics <strong>inhibit the sodium-2 chloride-potassium carrier on the
  luminal membrane of the thick ascending limb of the loop of Henle</strong> [slide 12]. The carrier takes sodium,
  potassium and two chlorides in together; blocked, they stay in the lumen and leave in the urine, and water goes
  with them. The slide 12 picture also shows potassium leaking back into the lumen to make the lumen positive,
  which drives magnesium and calcium reabsorption; that is why loops waste calcium and magnesium.</p>
  <p><strong>The four loop diuretics (Objective 1):</strong> <strong>furosemide</strong> (Lasix),
  <strong>bumetanide</strong> (Bumex), <strong>torsemide</strong> (Demadex) and <strong>ethacrynic acid</strong>
  (Edecrin) [slide 12]. Ethacrynic acid is the one that does not follow the &ldquo;-ide&rdquo; naming pattern of the other three.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 5:14 of the recording: <em>&ldquo;Most bang for your buck, loop diuretics is going to cause the biggest increases in urine outflow. We have four in this category here we have furosemide, bumetanide, torsemide, and then, just to be difficult, ethacrynic acid.&rdquo;</em></p>
    <p><mark class="prof-highlight">Loops are the most potent diuretics</mark>; four agents [slide 12].</p>
  </div>

  <table>
    <tr><th>Topic</th><th>What the slides give for loop diuretics</th></tr>
    <tr><td><strong>Major actions</strong> [slide 13]</td><td>Inhibit sodium chloride reabsorption by <strong>20 to 25 percent</strong>; increase urine output by <strong>up to 4 liters a day</strong>; <strong>increase potassium excretion</strong>; <strong>increase calcium and magnesium excretion</strong></td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 17]</td><td><strong>Pulmonary edema</strong> (lowers pulmonary pressure); <strong>nephrotic syndrome</strong> (protein loss, so the plasma cannot hold its fluid); <strong>cirrhosis of the liver</strong> (ascites); <strong>hypercalcemia</strong> (an add-on to saline hydration, which is the main treatment); <strong>heart failure</strong>; <strong>renal failure or insufficiency</strong>; <strong>hypertension</strong></td></tr>
    <tr><td><strong>Kidney function</strong> [slide 16]</td><td><strong>Loops are effective in patients whose creatinine clearance is below 30 milliliters per minute</strong></td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 18]</td><td><strong>Volume depletion</strong> (reflex mechanisms); <strong>hypokalemia</strong> (cardiac arrhythmias); <strong>hyperglycemia</strong> (diabetogenic); <strong>contraction alkalosis</strong>; <strong>hyperuricemia</strong> (gout); <strong>ototoxicity</strong> (damages the cochlea, the hearing organ of the inner ear; classically described as hair-cell damage, though the effect is often reversible); <strong>hyponatremia</strong> (seizures); <strong>allergic reactions</strong> (rash, photosensitivity); <strong>azotemia</strong> (raised blood urea nitrogen)</td></tr>
    <tr><td><strong>8 &middot; Interactions</strong> [slide 19]</td><td><strong>Nonsteroidal anti-inflammatory drugs</strong> blunt the natriuretic and blood pressure response; <strong>aminoglycosides</strong> potentiate ototoxicity; <strong>warfarin</strong> competes for plasma protein binding; <strong>lithium</strong> clearance falls and toxicity rises; <strong>digitalis</strong>: the hypokalemia and hypomagnesemia of a loop diuretic bring arrhythmias</td></tr>
  </table>

  <p><strong>Why the adverse effects happen (Objectives 5 and 6) [slides 14 to 16].</strong></p>
  <ul>
    <li><strong>Hyperglycemia</strong> has three routes: hypokalemia impairs insulin release; reflex release of catecholamines acts through alpha-2 receptors to decrease insulin release and through beta-2 receptors to increase glycogenolysis; and peripheral glucose uptake is impaired (insulin resistance) [slide 14].</li>
    <li><strong>Vasodilation.</strong> Loops have systemic vasodilator actions: they stimulate prostaglandin E2, and <strong>nonsteroidal anti-inflammatory drugs block that effect</strong>; there is also a direct relaxant effect on muscle whose mechanism is not understood [slide 14].</li>
    <li><strong>Reflex activity from volume depletion</strong> raises the renin-angiotensin system, aldosterone and antidiuretic hormone [slide 15].</li>
    <li><strong>Uric acid:</strong> excretion falls and the plasma level rises, which can cause gout, because proximal tubule reabsorption rises, tubular excretion falls, and the shrunken plasma volume concentrates the uric acid [slide 15].</li>
    <li><strong>Mild metabolic alkalosis:</strong> volume depletion raises bicarbonate reabsorption (minor) and hydrogen ion secretion is enhanced (major) [slide 16].</li>
    <li><strong>Mild hyperlipidemia:</strong> increased sympathetic activity raises triglycerides [slide 16].</li>
    <li><strong>Glomerular feedback:</strong> loops block the transporter in the macula densa that sends the feedback signal regulating the glomerular filtration rate and angiotensin II [slide 16].</li>
  </ul>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 8:53 of the recording: <em>&ldquo;Notably, the loop diuretics, you&rsquo;re going to see these still retain efficacy even when patients have really, really poor kidney function&hellip; even though their GFR is less than 30, the loops will still work&hellip; just because the person&rsquo;s making urine does not mean their kidneys are functioning all that well.&rdquo;</em></p>
    <p><mark class="prof-highlight">Loops still work at a creatinine clearance below 30</mark> [slide 16]; the thiazide contrast is in 1.3.</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 10:46 of the recording: <em>&ldquo;Note that these are going to be very similar things to what you see with other diuretics. It&rsquo;s just they&rsquo;re going to be less pronounced because they&rsquo;re not going to be as potent at getting rid of salt and water. Loops are the biggest players here, they&rsquo;re going to be the most drastic, and so they&rsquo;re going to be having the most adverse effects associated with them.&rdquo;</em></p>
    <p>The diuretic adverse effects are shared across classes; <mark class="prof-highlight">the more potent the diuretic, the stronger the effect</mark>. The exception is potassium, where some classes lower it and some raise it [slides 18, 26 and 33].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 5:53 of the recording: <em>&ldquo;If I&rsquo;m increasing potassium excretion, well, I could see hypokalemia as a side effect&hellip; I could see hypocalcemia or hypomagnesemia as a result of this. So again, one of the big things I told you about with ACE inhibitors, you got to know what these medications are doing to your potassium&hellip; because you can kill somebody very easily with potassium. So this is a case here where these would actually lower your potassium levels.&rdquo;</em></p>
    <p><mark class="prof-highlight">Loop diuretics lower potassium</mark> (hypokalemia), with hypocalcemia and hypomagnesemia, because they increase potassium, calcium and magnesium excretion [slides 13 and 18].</p>
  </div>

  <p><strong>Contraindications (Objective 7).</strong> Apart from anuria (no urine output) and known allergy to the drug, the slides give no separate contraindication list for the loop diuretics; the
  adverse-effect list is the working guide: volume depletion, gout, uncontrolled diabetes (hyperglycemia), and
  hypokalemia with a digitalis drug (see 1.11) are the situations to avoid or monitor.</p>

  <div class="callout"><strong>Deck versus truth &mdash; what the slides leave out about loops.</strong> Not on the slides, and
  therefore not examined as slide facts: <strong>furosemide, bumetanide and ethacrynic acid carry a US Food and Drug Administration (FDA) boxed warning</strong>
  that these are potent diuretics which, in excessive amounts, can lead to a profound diuresis with water and
  electrolyte depletion (the guide flags this because the slides do not). Ethacrynic acid, the odd one in the name pattern,
  is also the loop diuretic that does not contain a sulfonamide group, which matters in a sulfonamide-allergic patient, and it is
  the most associated with ototoxicity. Dr. Wood said ototoxicity appears with high chronic dosing (at 10:11); in practice it is seen mainly with rapid high-dose intravenous use, kidney failure and aminoglycoside co-use (also not on the slides).</div>
'''

BODY += '''
  <h3 class="sub" id="dh-thiazide">1.3 &middot; Objectives 1&ndash;8 &mdash; Thiazide diuretics</h3>

  <p><strong>The thiazides and thiazide-like drugs (Objective 1)</strong> [slide 20]: <strong>chlorothiazide</strong> (Diuril),
  <strong>hydrochlorothiazide</strong> (Aquazide), <strong>chlorthalidone</strong> (Hygroton), <strong>metolazone</strong>
  (Mykrox) and <strong>indapamide</strong> (Lozol). <strong>Mechanism (Objective 2):</strong> they inhibit the
  <strong>sodium-chloride transporter on the luminal membrane of the distal convoluted tubule</strong> (the major
  action); the slide adds some carbonic anhydrase activity and, at high dose, phosphodiesterase inhibition [slide 21].
  Slide 21 pictures the distal convoluted tubule cell: sodium and chloride enter together on the lumen side, calcium
  enters through a channel, and the blood side has the sodium-potassium pump a sodium-calcium exchanger and a parathyroid hormone receptor.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 12:31 of the recording: <em>&ldquo;So these are actually working to block sodium and chloride transport in that distal tubule. The minor action has this carbonic anhydrase activity&hellip; don&rsquo;t worry so much about that.&rdquo;</em></p>
    <p>Thiazides act at the <mark class="prof-highlight">distal convoluted tubule</mark>; the carbonic anhydrase and phosphodiesterase side actions on slide 21 are not for the exam [slide 21].</p>
  </div>

  <table>
    <tr><th>Topic</th><th>What the slides give for thiazides</th></tr>
    <tr><td><strong>Major actions</strong> [slides 22 and 23]</td><td>Increased sodium chloride excretion, inhibiting <strong>up to 5 percent</strong> of the filtered load; urine output up by <strong>1 to 2 liters a day</strong>; <strong>increased potassium and magnesium excretion</strong>; <strong>decreased renal calcium excretion</strong>, because proximal tubule calcium reabsorption and distal tubule calcium reabsorption both rise; <strong>hyperglycemia</strong> (decreased glucose tolerance, decreased insulin secretion); the glomerular filtration rate falls acutely</td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 24]</td><td><strong>Hypertension</strong>; renal failure; cirrhosis of the liver; congestive heart failure; <strong>renal calcium stones</strong> (calcium oxalate). The slide also lists &ldquo;hypercalcemia&rdquo; here, but thiazides raise serum calcium and do not treat hypercalcemia (see the box below)</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slides 26 to 28]</td><td>Volume depletion (reflexes); increased sympathetic activity (decreased insulin); <strong>increased renin-angiotensin, aldosterone and antidiuretic hormone activity</strong>; <strong>hypokalemia</strong>; <strong>metabolic alkalosis</strong> (contracted extracellular fluid); <strong>hyperuricemia and gout</strong>; <strong>hyperglycemia</strong>; <strong>hypercalcemia</strong>; <strong>hyperlipidemia</strong> (5 to 15 percent rise in low-density lipoprotein cholesterol); <strong>allergic skin rashes</strong>; <strong>photosensitivity</strong>; dizziness, headache, weakness, restlessness; <strong>sexual dysfunction</strong>; <strong>constipation</strong></td></tr>
    <tr><td><strong>7 &middot; Limit of use</strong> [slide 28]</td><td>Thiazides are ineffective at low creatinine clearance, below 30 to 40 milliliters per minute; <strong>metolazone is effective at lower clearance rates</strong></td></tr>
    <tr><td><strong>8 &middot; Interactions</strong> [slide 29]</td><td><strong>Nonsteroidal anti-inflammatory drugs</strong> block prostaglandins and attenuate the natriuretic action; thiazides <strong>increase digitalis toxicity</strong>, so potassium should be kept above 4.0 milliequivalents (mEq) per liter</td></tr>
  </table>

  <h4 class="subsub">Thiazides in hypertension [slide 25]</h4>
  <p>Thiazides <strong>work best in elderly patients, African American patients and sodium-retentive states</strong>
  (the slide also lists obese patients; see the box below). The mechanism is time-dependent. In the <strong>short term</strong> they decrease blood
  volume and cardiac output. <strong>Chronically</strong> there are direct vasorelaxant effects, so total peripheral resistance falls;
  there is less sodium in the arteriolar walls and so less &ldquo;waterlogging&rdquo;; the wall is thinner and the
  diameter larger; and the vessel is less responsive to norepinephrine and shows more vasodepressor responses.
  <strong>Low-dose thiazides are preferred for hypertension because they cause few adverse effects.</strong></p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 14:46 of the recording: <em>&ldquo;Who does this work well in? If you have elderly patients, obese, African American patients, who they all tend to be more sodium retentive, so if you can get rid of that extra sodium you&rsquo;re going to be able to help to decrease some of this, what we call water logging&hellip; Thiazides have a more long lasting action than you would see with something like a loop diuretic, so for chronic hypertension you&rsquo;re going to see far more thiazides being used than ever you would loops. Doesn&rsquo;t mean they&rsquo;re first line anymore, they used to be, but they can be maybe as a useful maybe second or third line add-on&hellip; they&rsquo;re also well tolerated, they&rsquo;re cheap.&rdquo;</em></p>
    <p>Thiazides suit <mark class="prof-highlight">sodium-retentive patients</mark> and are used for chronic hypertension, while loops are not, because the thiazide effect is long lasting [slide 25].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 17:18 of the recording: <em>&ldquo;Big difference though is you can see this hypercalcemia, because you&rsquo;re causing the body to hold on to more calcium. But I just said, well, it reduces calcium stones&hellip; what it&rsquo;s going to do is&hellip; causing the patient to suck up more calcium out of the renal tubule, so there&rsquo;s less calcium there available to crystallize out. So yes, it could cause the patient&rsquo;s serum calcium levels to go up a little bit, but it&rsquo;s a pretty minor bump.&rdquo;</em></p>
    <p><mark class="prof-highlight">Thiazides lower urinary calcium and raise serum calcium a little</mark>, so they prevent calcium oxalate stones; loops do the opposite, wasting calcium [slides 22, 24 and 27]. The stone paradox is the one he said confuses students.</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 18:21 of the recording: <em>&ldquo;You can find the thiazides actually become ineffective when your GFR, your creatinine clearance, goes down too low. So once you get down below like 30 or 40&hellip; stop working, with the exception&hellip; metolazone&hellip; that one will still retain the efficacy even at very low creatinine clearances&hellip; I always think about that, metolazone could make a rock pee, and that&rsquo;s how I know it still retains efficacy.&rdquo;</em></p>
    <p><mark class="prof-highlight">Metolazone keeps working at a very low creatinine clearance</mark> (&ldquo;could make a rock pee&rdquo;); the other thiazides do not [slide 28]. He gave the case of a volume-overloaded heart failure patient already on a furosemide drip to whom the nephrologist added metolazone.</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; six thiazide statements.</strong> (1) <strong>Uric acid:</strong> slide 23 says
  thiazides increase uric acid excretion acutely and cause gout chronically. Learn what slide 26 says and what
  happens in practice: <strong>thiazides cause hyperuricemia and gout</strong>, because of volume contraction and less
  uric acid excretion. (2) <strong>Low clearance:</strong> slide 28 says thiazides are ineffective at a creatinine
  clearance below 30 to 40. That is the course teaching, and the useful exam fact is that <strong>metolazone retains
  efficacy</strong>; newer trial data show chlorthalidone also works in advanced kidney disease, so do not memorize
  &ldquo;thiazides never work in kidney disease&rdquo; as an absolute. (3) <strong>Who responds:</strong> slide 25
  lists obese patients, but the better-established responders are elderly patients, African American patients and sodium-retentive states. (4) The
  carbonic anhydrase and phosphodiesterase side actions (slide 21) are not for the exam, as Dr. Wood said.
  (5) <strong>Hypercalcemia:</strong> slide 24 lists &ldquo;hypercalcemia/renal calcium stones&rdquo; as an indication, yet slide 27 lists
  hypercalcemia as an adverse effect, and Dr. Wood said at 17:35 that patients are hypercalcemic to begin with. The truth: <strong>thiazides raise serum
  calcium and are not used to treat hypercalcemia</strong> (loops can be added to saline hydration, the main treatment, 1.2); the real use is calcium oxalate stones in patients who lose too much calcium in the urine.
  (6) <strong>First line:</strong> Dr. Wood said at 16:43 that thiazides are no longer first line but a second or third line add-on (his wording, not on a slide). Current US
  hypertension guidelines still list thiazide-type diuretics among the first-line drug classes, with ACE inhibitors, angiotensin receptor blockers and calcium channel blockers, so do not memorize &ldquo;second or third line&rdquo;.</div>

  <div class="pearl"><strong>Thiazide against loop, in one line each.</strong> Both lower potassium and magnesium and raise
  uric acid and glucose. The <strong>loop wastes calcium</strong> (and can be added to saline in hypercalcemia); the <strong>thiazide keeps
  calcium</strong> (and treats calcium stones). The loop works at a very low clearance; the thiazide does not, except
  <strong>metolazone</strong>. The thiazide is the chronic hypertension drug; the loop is the volume-removal drug.</div>
'''

BODY += '''
  <h3 class="sub" id="dh-ksparing">1.4 &middot; Objectives 1&ndash;8 &mdash; Potassium-sparing diuretics</h3>

  <p><strong>The drugs (Objective 1):</strong> <strong>amiloride</strong> (Midamor; the combination Moduretic) and
  <strong>triamterene</strong> (Dyrenium; the combinations Dyazide and Maxzide). The combinations are with
  hydrochlorothiazide [slide 31]. <strong>Mechanism (Objective 2):</strong> they <strong>block luminal sodium
  channels</strong> in the collecting duct [slide 30]. The collecting-tubule picture (slides 30 and 34) shows the principal cell: sodium
  enters and potassium leaves through luminal channels, the sodium-potassium pump works on the blood side, and the aldosterone and
  antidiuretic hormone receptors sit on the blood side.</p>
  <table>
    <tr><th>Topic</th><th>What the slides give for potassium-sparing diuretics</th></tr>
    <tr><td><strong>Actions</strong> [slide 30]</td><td>Inhibit <strong>2 to 3 percent</strong> of sodium chloride reabsorption; <strong>decrease the gradient for potassium secretion</strong> (so potassium is held); modest increase in urine flow; <strong>uric acid:</strong> a modest rise in excretion acutely in the collecting duct, a modest fall chronically (volume contraction and more reabsorption in the proximal tubule)</td></tr>
    <tr><td><strong>3 &middot; Indications</strong> [slide 32]</td><td>The same as the other diuretics, but with much <strong>less natriuretic and diuretic effect</strong>; <strong>most often used in combination</strong> with other diuretics or antihypertensive drugs</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 33]</td><td><strong>Hyperkalemia</strong>; caution with ACE inhibitors and angiotensin blockers; caution with potassium supplements; diabetes (glucose intolerance); <strong>megaloblastic anemia with triamterene</strong>; <strong>azotemia with amiloride</strong></td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 21:55 of the recording: <em>&ldquo;I&rsquo;m going to be holding on to more potassium, so I call it potassium sparing. That&rsquo;s going to be handy to offset the hypokalemia that stuff like loops can cause, so it would not be uncommon to see a mixture of both, a loop plus something like a potassium sparing diuretic to offset that potassium action to a degree. This is where things get complicated, because you can have multiple meds that can cause an increase in potassium, multiples that cause a decrease, and you need to know ultimately where is the patient going to fall, because if you don&rsquo;t, patient can have some major issues.&rdquo;</em></p>
    <p><mark class="prof-highlight">Potassium-sparing diuretics raise potassium</mark> and are paired with potassium-wasting loops or thiazides; the hyperkalemia risk is added to by <mark class="prof-highlight">ACE inhibitors, angiotensin receptor blockers and potassium supplements</mark> [slides 32 and 33].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 23:26 of the recording: <em>&ldquo;A little tip here, if you ever see someone on a salt substitute, so maybe they need to be on a low sodium diet, so they get a salt substitute for their food, that&rsquo;s usually potassium chloride. The tongue can&rsquo;t tell the difference between sodium and potassium, so it tastes salty but it cuts down the actual sodium intake they have. That can also contribute, though, to their potassium intake. They&rsquo;ve got to be cautious there.&rdquo;</em></p>
    <p>Patient education: <mark class="prof-highlight">salt substitutes are potassium chloride</mark>, so they add to the hyperkalemia risk with a potassium-sparing diuretic, an ACE inhibitor or an angiotensin receptor blocker [slide 33; the salt-substitute point itself comes from the recording, not the slide]. In truth, potassium chloride tastes salty enough, with a slightly bitter edge, to stand in for salt, so a salt substitute cuts the sodium a patient eats (the recording says the tongue cannot tell the difference).</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; mechanism and boxed warning.</strong> Slide 30 lists three mechanisms
  (luminal sodium channels, a sodium-calcium antiporter and a sodium-hydrogen antiporter). <strong>Learn the first:
  amiloride and triamterene block the luminal sodium channels</strong>; the antiporter lines are not examined. Not on the
  slides: <strong>amiloride and triamterene carry an FDA boxed warning for hyperkalemia</strong> (guide flag). Dr. Wood
  added that these drugs are not run across very often now because few patients are on them.</div>

  <h3 class="sub" id="dh-aldo">1.5 &middot; Objectives 1&ndash;7 &mdash; Aldosterone and aldosterone antagonists</h3>

  <p><strong>What aldosterone normally does (slide 34).</strong> Aldosterone binds to its receptor, which is translocated to the
  nucleus; in the nucleus it activates protein synthesis; this <strong>raises the number of sodium channels in the
  membrane</strong> and <strong>raises the activity of the sodium-potassium ATPase</strong>, and it stimulates energy production in
  the distal convoluted tubule. Aldosterone is the major mineralocorticoid (&ldquo;mineral&rdquo; means salt). More sodium channels
  mean sodium and water are reabsorbed while potassium is lost, which is why <strong>chronic excess aldosterone
  (hyperaldosteronism) produces hypokalemia</strong>. Two ways to interrupt this: block the sodium channels (1.4) or block aldosterone itself (here).</p>
  <p><strong>The drugs (Objective 1):</strong> <strong>spironolactone</strong> (Aldactone) and <strong>eplerenone</strong> (Inspra) [slide 35].</p>
  <table>
    <tr><th>Topic</th><th>What the slides give for aldosterone antagonists</th></tr>
    <tr><td><strong>2 &middot; Mechanism</strong> [slide 36]</td><td><strong>Bind the steroid receptor but do not translocate to the nucleus</strong>; <strong>most effective when aldosterone is high</strong>; block 2 to 3 percent of sodium chloride reabsorption, so potassium loss falls; modest effect on lipid, glucose and uric acid levels</td></tr>
    <tr><td><strong>3 &middot; Clinical uses</strong> [slide 37]</td><td><strong>Primary aldosteronism</strong>; <strong>hypertension</strong>; <strong>congestive heart failure</strong> (the slide says class IV, symptoms at rest); edematous conditions; <strong>cirrhosis</strong> (secondary hyperaldosteronism); <strong>nephrotic syndrome</strong></td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 38]</td><td><strong>Hyperkalemia and mild acidosis</strong>; nausea, vomiting and gastrointestinal upset; <strong>weak androgenic effects, a &ldquo;partial agonist at testosterone receptors&rdquo;</strong> (the slide&rsquo;s words; in truth spironolactone <strong>blocks</strong> the androgen receptor, see the box below); <strong>gynecomastia and testicular atrophy in men</strong>; <strong>menstrual irregularities</strong> and, as the slide words it, hirsutism in women (hirsutism is not a true adverse effect; spironolactone treats it); <strong>eplerenone has less effect on androgen receptors</strong></td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 25:39 of the recording: <em>&ldquo;Spironolactone in particular has these weak androgenic effects, and it&rsquo;s a partial agonist at testosterone receptors&hellip; it can both cause masculinizing effects in patients and feminizing effects in patients&hellip; with women you can see masculinizing issues, and men you could see breast development, feminizing sort of effect.&rdquo;</em> And at 29:31: <em>&ldquo;Spironolactone is an older drug, so it&rsquo;s pretty cheap, so we start with that first. But if this is an issue, if the patient is complaining about breast development, or if the patient is complaining about menstrual problems, then you could&hellip; utilize eplerenone instead. That&rsquo;s much less of the androgenic activity.&rdquo;</em></p>
    <p>His explanation (reported, not to be learned; see the box below): a partial agonist lifts the low androgen activity of a woman toward its own level and lowers the high activity of a man toward it, so he expected masculinizing effects in women and breast development in men. <mark class="prof-highlight">If a patient on spironolactone has breast development or menstrual problems, switch to eplerenone</mark> [slide 38]. He also named acne as a use of spironolactone (blocking testosterone&rsquo;s effect on sebum), which is not on the slide and is itself evidence that the drug blocks androgens rather than mimicking them.</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; aldosterone antagonists.</strong> (1) Slide 36 lists <em>increased
  calcium excretion</em> and a <em>30 to 60 minute lag time</em>. Neither is examined: the calcium line is not a reliable
  property of these drugs, and clinically their full diuretic effect builds over days, not minutes. (2) Slide 37 limits heart failure use to
  &ldquo;class IV&rdquo;, while slide 73 says &ldquo;grade III or IV&rdquo;; learn it as
  <strong>mortality reduction in advanced (class III or IV) heart failure</strong> (current guidelines extend it to milder reduced-ejection-fraction failure). Hyperkalemia is the danger to prevent (1.12 and 1.14).
  (3) <strong>Androgen receptor:</strong> slide 38 and Dr. Wood (25:39, and his drawing at 27:36 to 29:03) call spironolactone a
  &ldquo;partial agonist at testosterone receptors&rdquo; with &ldquo;weak androgenic effects&rdquo;. That is wrong. <strong>Spironolactone is an
  androgen receptor antagonist</strong> (it blocks the receptor, and it also modestly lowers androgen production), so it lowers androgen action in everyone. Breast
  enlargement (gynecomastia) in men and menstrual irregularity in women follow from that blockade. <strong>Hirsutism is not an adverse effect of spironolactone: it is a use</strong>,
  as acne is (his own acne point at 26:19 shows the same thing), and masculinizing effects are not expected from it. Learn gynecomastia and menstrual
  irregularity as the antiandrogen adverse effects; the slide&rsquo;s testicular atrophy is not an established hallmark. <strong>Eplerenone binds the androgen receptor much
  less</strong>, so the switch to eplerenone for breast development or menstrual problems is right. (4) Dr. Wood said at 20:40 that aldosterone is released by the kidneys; it is made by the
  adrenal cortex (the kidney&rsquo;s renin starts the chain that releases it).</div>

  <h3 class="sub" id="dh-cai">1.6 &middot; Objectives 1&ndash;7 &mdash; Carbonic anhydrase inhibitors</h3>

  <p><strong>The drugs (Objective 1):</strong> <strong>acetazolamide</strong> (Diamox), <strong>dichlorphenamide</strong>
  (Daramide) and <strong>methazolamide</strong> (Glauctabs) [slide 40]. <strong>Mechanism (Objective 2) [slide 39]:</strong>
  they inhibit carbonic anhydrase, so <strong>bicarbonate absorption in the proximal tubule falls by 80 to 90 percent</strong>, hydrogen
  ion production falls and the sodium-hydrogen exchange falls. The short-term effect is to increase sodium and
  potassium excretion by about 5 percent; <strong>after 3 to 5 days the effect is reduced to 1 to 3 percent</strong>,
  because the rest of the nephron makes up for it. Slide 41 pictures the proximal tubule cell with the two
  carbonic anhydrase sites (in the lumen and in the cell) and the carbonic anhydrase inhibitors blocking both.</p>
  <table>
    <tr><th>Topic</th><th>What the slides give for carbonic anhydrase inhibitors</th></tr>
    <tr><td><strong>3 &middot; Other uses</strong> [slide 42]</td><td><strong>Glaucoma</strong> (decreased bicarbonate in the ciliary body; the topical forms are dorzolamide, Trusopt, and brinzolamide, Azopt); <strong>epilepsy</strong> (metabolic acidosis, central nervous system effects); <strong>mountain sickness</strong>; head injury (decreased swelling)</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Adverse effects</strong> [slide 43]</td><td><strong>Metabolic acidosis</strong>; <strong>potassium depletion</strong>; <strong>drowsiness</strong></td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 30:44 of the recording: <em>&ldquo;By blocking this enzyme, you&rsquo;re gonna trap the bicarbonate in the tubule, and then you&rsquo;ll just pee it out&hellip; the urine pH may go up because there&rsquo;s more bicarbonate, and the actual serum pH may go down a little bit.&rdquo;</em> And at 36:15: <em>&ldquo;You could see a bit of a metabolic acidosis, that&rsquo;s different than your other diuretics, which typically cause more of a contraction alkalosis.&rdquo;</em></p>
    <p>Carbonic anhydrase inhibitors cause <mark class="prof-highlight">metabolic acidosis with alkaline urine</mark>, unlike the other diuretics, which cause contraction alkalosis [slides 18, 26 and 43].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 33:05 of the recording: <em>&ldquo;In the meantime we can utilize carbonic anhydrase inhibitors to cause your blood to acidify, and then how does your body respond to acidic blood? You breathe faster, you induce tachypnea to blow off more CO2 but to bring in more O2.&rdquo;</em> And at 34:35: <em>&ldquo;By acidifying a patient&rsquo;s blood you actually hyperpolarize their neurons, you make it harder for those neurons to fire off and cause a seizure.&rdquo;</em></p>
    <p>Mountain (altitude) sickness: the acidosis drives faster breathing until the body adapts. Epilepsy: the acidosis raises the seizure threshold. Glaucoma: less aqueous humor. He also noted that they can lessen cerebrospinal fluid production, and that the drowsiness comes from the neurons firing less readily (at 36:23) [slides 42 and 43].</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; carbonic anhydrase inhibitors.</strong> The &ldquo;head injury: decreased
  swelling&rdquo; line on slide 42 is not a settled use and is not examined. The deck lists only three adverse effects; the standard
  label also warns of kidney stones, tingling in the fingers and a sulfonamide allergy, which are not on the slides.</div>
'''

BODY += '''
  <h3 class="sub" id="dh-hf">1.7 &middot; Objectives 1&ndash;2 &mdash; Heart failure: causes, types and compensation</h3>

  <p><strong>Causes of heart failure [slide 45].</strong> <strong>Ischemic heart disease and myocardial infarction account for 50 to 60 percent of cases.</strong>
  The others are hypertension, idiopathic dilated cardiomyopathy, other cardiomyopathies (alcoholic, viral, hypertrophic) and drug-induced
  heart failure. Dr. Wood added that chronic high blood pressure, alcohol and heavy metals such as cobalt can all cause it (37:01).</p>
  <table>
    <tr><th>Type</th><th>What goes wrong</th><th>Causes</th><th>What the slides call it</th></tr>
    <tr><td><strong>Systolic dysfunction</strong> [slide 46]</td><td><strong>Decreased contractility</strong></td><td>Loss of myocardial muscle mass; left ventricular hypertrophy; dilated cardiomyopathies</td><td>Assessed as <strong>reduced ejection fraction</strong></td></tr>
    <tr><td><strong>Diastolic dysfunction</strong> [slide 47]</td><td><strong>Impaired relaxation</strong>: decreased ventricular filling, so decreased cardiac output</td><td>Left ventricular hypertrophy (thicker, stiffer ventricles relax less efficiently); ischemia, which impairs removal of calcium from the cytosol back into the sarcoplasmic reticulum</td><td>Heart failure symptoms with <strong>preserved ejection fraction</strong> (heart failure with preserved left ventricular function)</td></tr>
  </table>
  <p>Dr. Wood&rsquo;s way to hold the difference: in diastolic failure the ejection fraction percentage may be fine, but because the ventricle fills less the total blood pumped, the cardiac output, is still down (at 38:13).</p>

  <p><strong>Compensatory response [slide 48].</strong> The body compensates with <strong>increased preload</strong> (through sodium and water retention),
  <strong>vasoconstriction</strong>, <strong>tachycardia and increased contractility</strong> (through sympathetic activation) and
  <strong>left ventricular hypertrophy</strong>. Slide 49 pictures the cascade: heart failure lowers cardiac output; that leads
  to increased venous volume and pressure (congestion and edema, dyspnea and orthopnea), decreased tissue perfusion (weakness and
  fatigue), and neuroendocrine activation (sympathetic and renin-angiotensin-aldosterone activation) with a faster heart rate, vasoconstriction
  and increased afterload, and sodium and water retention. Each response worsens the failure, so it is a vicious circle. The drugs in this lecture break the circle at different points.</p>

  <p><strong>Common precipitants of decompensation [slide 50]:</strong> lack of compliance; uncontrolled hypertension; cardiac arrhythmias;
  inadequate therapy; inappropriate medications or fluid overload; and other causes: acute anginal chest pain, pulmonary infection and emotional stress.
  Dr. Wood&rsquo;s example was the holiday season, when people travel, forget their medications and eat sodium-heavy food (at 39:21).</p>

  <p><strong>Nonpharmacologic therapy [slide 51].</strong> <strong>Restrict dietary sodium and fluid</strong> (the slide gives 1 to 3 grams of sodium a day and fluids under 2 liters a day; learn the
  restriction, not the numbers). <strong>Physical activity may improve functional status.</strong> Exercise capacity is also how efficacy is judged: how much work the patient can do before getting winded
  (recording, 40:07).</p>

  <div class="callout"><strong>Deck versus truth &mdash; two numbers.</strong> Slide 46 defines reduced ejection fraction as
  below 45 percent; the current definition is 40 percent or less. Learn <strong>&ldquo;reduced ejection fraction&rdquo;</strong>,
  not the number. The sodium and fluid figures on slide 51 vary between guidelines and are not examined; the point is to restrict both.</div>

  <h3 class="sub" id="dh-hfdiur">1.8 &middot; Objectives 1&ndash;7 &mdash; Heart failure: diuretics and angiotensin-converting enzyme inhibitors</h3>

  <h4 class="subsub">Diuretics in heart failure [slides 52 and 53]</h4>
  <ul>
    <li><strong>Thiazide diuretics are not potent enough for most heart failure patients.</strong></li>
    <li><strong>Loop diuretics are the mainstay of heart failure therapy.</strong> They decrease sodium and water retention and so decrease preload, giving <strong>symptomatic benefit</strong>.</li>
    <li><strong>Monitor the patient&rsquo;s weight</strong> to detect worsening fluid overload: a gain of more than a pound a day over several days (the figure on the slide) is fluid, not tissue.</li>
    <li><strong>Diuretics are for symptomatic relief only.</strong> There is <strong>no evidence that they decrease progression or mortality</strong>, and they are <strong>not mandatory therapy</strong>.</li>
  </ul>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 40:42 of the recording: <em>&ldquo;Loops are&hellip; mainstay of therapy for heart failure&hellip; it doesn&rsquo;t do anything to help them live longer, it just helps with symptomatic management. This is another situation in which, if I say something is good for mortality purposes&hellip; if it&rsquo;s good for mortality reasons, that means you want the patient on it no matter what. If it&rsquo;s just good for symptom management, then they may not need to be on it all the time.&rdquo;</em> And at 41:46: <em>&ldquo;Diuretics are simply for symptomatic relief, they don&rsquo;t do anything for disease progression or mortality, so strictly not mandatory. You may have some people who are on this more as a PRN basis, so they notice their weight&rsquo;s gone up for several days in a row, they may be instructed to take the loops.&rdquo;</em></p>
    <p><mark class="prof-highlight">Diuretics relieve symptoms and do not prolong survival; they are not mandatory.</mark> Daily weights guide when to take them (PRN means as needed) [slides 52 and 53]. Expect a stem that sorts heart failure drugs into &ldquo;symptoms only&rdquo; and &ldquo;mortality benefit&rdquo;.</p>
  </div>

  <h4 class="subsub">Angiotensin-converting enzyme inhibitors in heart failure [slides 54 to 56]</h4>
  <p>ACE inhibitors <strong>decrease preload, decrease afterload, decrease sympathetic activation</strong> and <strong>decrease left ventricular hypertrophy, dilation and remodeling</strong>.
  They <strong>slow heart failure progression</strong> and <strong>decrease mortality</strong> [slide 54]. The benefits are
  hemodynamic improvements, improved exercise tolerance, decreased symptoms, fewer hospital admissions, slowed progression of disease and prolonged survival [slide 55].</p>
  <p><strong>ACE inhibitor problems (adverse effects) [slide 56]:</strong> <strong>impairment of renal function</strong>, <strong>hypotension</strong>, <strong>elevation of serum potassium</strong>,
  <strong>cough</strong> and <strong>angioedema</strong>. Dr. Wood&rsquo;s advice: if the cough or angioedema is the problem, switch to an angiotensin receptor blocker (43:15).</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 42:08 of the recording: <em>&ldquo;The ACEs and/or ARBs absolutely require. These work on all aspects to decrease preload and afterload, and they decrease that sympathetic activation. Biggest thing here too, they decrease left ventricular remodeling, dilation, hypertrophy&hellip; mandatory for these patients, because we know through these big huge heart studies that we see not only hemodynamic improvements, they&rsquo;re better exercise tolerance, fewer admissions, less progression of disease, and they live longer&hellip; so ACEs or ARBs have to be mandatory for these patients.&rdquo;</em> And at 42:58: <em>&ldquo;You may see some risk for hypotension depending what their other meds look like, and elevation&hellip; in potassium&hellip; potentially the decreased potassium, now we got ACEs which we&rsquo;re going to increase it, so we got&hellip; monitor for this.&rdquo;</em></p>
    <p><mark class="prof-highlight">An ACE inhibitor or an angiotensin receptor blocker is mandatory in heart failure with reduced ejection fraction (a weak pumping heart)</mark> because it prolongs survival [slides 54 and 55; the slides do not name the type of heart failure, and in preserved ejection fraction these drugs have not shown a survival benefit]; monitor kidney function and potassium [slide 56].</p>
  </div>

  <h3 class="sub" id="dh-hfbb">1.9 &middot; Objectives 1&ndash;7 &mdash; Heart failure: beta blockers</h3>

  <p>Beta blockers were <strong>classically considered contraindicated in heart failure</strong> [slide 57], because they lower heart rate and contractility
  (the recording, 44:03). The ones with a <strong>mortality benefit</strong> are only three: <strong>carvedilol</strong> (Coreg), <strong>metoprolol succinate</strong> (the extended-release form, marked XL; Toprol XL)
  and <strong>bisoprolol</strong> (Zebeta) [slide 57]. Dr. Wood: carvedilol is the third-generation beta blocker, metoprolol succinate is the long-acting formulation, and the other beta blockers have not been shown to reduce mortality in heart failure (43:28).</p>
  <table>
    <tr><th>Topic</th><th>What the slides give for beta blockers in heart failure</th></tr>
    <tr><td><strong>9 &middot; Keys to successful use</strong> [slide 58]</td><td>The patient should be <strong>stable before initiation</strong>; in hospital is preferred; <strong>start with very low doses</strong>; <strong>titrate up slowly</strong> over 6 to 8 weeks in total; <strong>monitor for worsening heart failure signs and symptoms</strong></td></tr>
    <tr><td><strong>Benefits</strong> [slide 59]</td><td>Improved exercise tolerance; hemodynamic improvements (increase in ejection fraction); slowed disease progression; decreased hospitalizations; <strong>decreased need for transplant</strong>; <strong>decreased mortality</strong></td></tr>
    <tr><td><strong>Place in therapy</strong> [slide 60]</td><td><strong>First-line therapy in class II to IV heart failure</strong>; patients should be on an ACE inhibitor and a beta blocker <strong>irrespective of symptoms</strong></td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 43:28 of the recording: <em>&ldquo;The next ones we need to look at are the beta blockers. These are also going to be mandatory, but note here it&rsquo;s only three specific beta blockers: carvedilol, which is that third gen type of beta blocker I talked about before, metoprolol succinate, which is the XL formulation&hellip; and then bisoprolol. These three in particular have been found to be associated with reducing mortality in these heart failure patients. All the other ones have not been found to do that.&rdquo;</em> At 44:20: <em>&ldquo;They probably need to be in the hospital when you start these, and you&rsquo;re going to just gradually work them up on very low doses&hellip; low and slow, that&rsquo;s the tempo, as the Beastie Boys famously said&hellip; we&rsquo;re gonna start low and gradually work them up. It may take like six to eight weeks to do so, but that&rsquo;s okay, this is a marathon.&rdquo;</em> At 45:04: <em>&ldquo;These should be first line therapy in class two to four heart failure. We&rsquo;re just going to say anyone with heart failure needs to be on these&hellip; irrespective of symptoms, ACEs and beta blockers are go-to. Remember the three: carvedilol, metoprolol succinate, and then bisoprolol.&rdquo;</em></p>
    <p><mark class="prof-highlight">The three heart failure beta blockers are carvedilol, metoprolol succinate and bisoprolol</mark>; they are mandatory because they prolong survival, and they are started <mark class="prof-highlight">low and slow</mark> because a decompensating patient can die from an abrupt fall in rate and contractility [slides 57 to 60].</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; beta blocker start-up.</strong> The 6 to 8 weeks and &ldquo;in hospital preferred&rdquo; are the
  slide&rsquo;s wording; the lesson is <strong>start at a very low dose in a stable patient and increase slowly</strong>, and beta blockers can be started
  in the outpatient clinic as well. Not on the slides: the heart failure beta blockers and ACE inhibitors share the class cautions
  described in the antihypertensive and antianginal sections: an FDA boxed warning against abrupt cessation of metoprolol (ischemic heart disease) and a boxed
  warning of fetal toxicity for ACE inhibitors and angiotensin receptor blockers.</div>
'''

BODY += '''
  <h3 class="sub" id="dh-digoxin">1.10 &middot; Objectives 1&ndash;3 &mdash; Digoxin: action, benefit and place</h3>

  <p><strong>The drug (Objective 1).</strong> Digoxin is a cardiac glycoside: a <strong>lactone ring and a steroid nucleus are essential for activity</strong>, and the
  sugar molecules (three, in the picture on slide 61) influence absorption, half-life and metabolism [slides 61 and 62]. Digoxin and digitalis-type compounds come from plants
  (foxglove, lily of the valley and oleander), as Dr. Wood noted (45:25).</p>
  <p><strong>Mechanism (Objective 2) [slides 62 to 65].</strong> There are two ways to describe it.</p>
  <table>
    <tr><th>View</th><th>What digoxin does</th></tr>
    <tr><td><strong>Inotropic action (the older mechanism)</strong> [slides 62 and 63]</td><td>It <strong>inhibits the sodium-potassium ATPase</strong> of the heart muscle cell, so intracellular sodium rises; the sodium-calcium exchanger then raises intracellular calcium, and <strong>fiber shortening (the force of contraction) increases</strong></td></tr>
    <tr><td><strong>Neurohormonal actions (the newer mechanism)</strong> [slides 63 to 65]</td><td><strong>Decreases sympathetic and increases parasympathetic activity</strong>; <strong>resensitizes the baroreflex</strong> (blocking the pump helps reset it, so the heart rate falls); more parasympathetic activity in the atrioventricular node and conduction system; less sympathetic activity, so lower blood pressure and heart rate; <strong>decreases renin-angiotensin-aldosterone activity</strong>, with less remodeling and structural change; better tissue perfusion; and <strong>increased cardiac output</strong> from better pumping</td></tr>
  </table>
  <p><em>Deck versus truth, a detail that is not examined:</em> slide 62 and Dr. Wood (46:31) say the sodium-calcium exchanger &ldquo;brings calcium in&rdquo;. More exactly, the rise in intracellular sodium
  weakens the exchanger&rsquo;s normal removal of calcium from the cell, so calcium builds up and more is released from the sarcoplasmic reticulum. The result, a stronger contraction, is the same.</p>
  <p><strong>Target level (monitoring):</strong> 0.5 to 1 nanogram per milliliter [slide 65]; higher concentrations may be associated with worse outcomes in heart failure patients. <strong>Digoxin is one of the few heart failure drugs for which a blood level is checked</strong> (Dr. Wood, 50:44). <em>Flag: Dr. Wood said the number itself is probably not tested (48:35); know that the level is monitored and the therapeutic index is narrow.</em></p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 48:19 of the recording: <em>&ldquo;Digoxin is what we call very narrow therapeutic index drug. It is a very narrow window in which it works&hellip; you do not need much of this drug to get very drastic effects&hellip; I&rsquo;m probably not going to quiz you specifically on the level on the test, but just know that this has a very tight therapeutic index. It is very easy to get too much and end up causing major problems for the patient.&rdquo;</em></p>
    <p>Digoxin has a <mark class="prof-highlight">narrow therapeutic index</mark>; the number itself is not the point [slide 65].</p>
  </div>

  <h4 class="subsub">Benefit and place in therapy (Objective 3) [slides 66 and 67]</h4>
  <ul>
    <li><strong>Clinical benefits:</strong> improvement in symptoms, improved exercise tolerance, improved quality of life and a decreased number of hospitalizations. <strong>No survival benefit.</strong></li>
    <li><strong>No evidence of slowed disease progression.</strong></li>
    <li><strong>Primary use:</strong> symptomatic patients who are already on optimal doses of ACE inhibitors, beta blockers and diuretics.</li>
    <li>It is also used for <strong>rate control in patients with atrial fibrillation and heart failure</strong> (see the box below) and is considered in patients with <strong>symptomatic heart failure and systolic dysfunction</strong>.</li>
  </ul>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 48:55 of the recording: <em>&ldquo;Clinical benefits you get with digoxin can include improvement of symptoms, better quality of life and exercise tolerance, but no survival benefits&hellip; It&rsquo;s not going to be one of those mandatory ones like beta blockers or ACEs, because they don&rsquo;t actually provide a survival benefit. If you&rsquo;re really topped up on your ACEs and beta blockers but you&rsquo;re still not really where you want to be, then maybe digoxin can be maybe a useful add-on.&rdquo;</em></p>
    <p><mark class="prof-highlight">Digoxin: symptoms yes, survival no, so an add-on, not mandatory</mark> [slides 66 and 67]. He added that he prefers not to use it because it is cleared by the kidneys and accumulates in patients with kidney problems (not on the slides).</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; digoxin and atrial fibrillation.</strong> Slide 67 calls digoxin &ldquo;first line&rdquo; for
  atrial fibrillation with heart failure because of its rate-control properties. That overstates it: beta blockers are the usual first
  choice for rate control, and digoxin is a reasonable add-on or alternative. Learn that digoxin <strong>can be used for rate control in atrial fibrillation with heart failure</strong>
  (Dr. Wood: &ldquo;if they would have afib plus heart failure, then you could utilize this&rdquo;, 49:44), not that it is first line.</div>

  <h3 class="sub" id="dh-digtox">1.11 &middot; Objectives 5&ndash;8 &mdash; Digoxin toxicity, contraindications and the antidote</h3>

  <table>
    <tr><th>Toxicity group</th><th>What the slides list</th></tr>
    <tr><td><strong>Gastrointestinal</strong> [slide 68]</td><td>Anorexia and nausea</td></tr>
    <tr><td><strong>Visual disturbances</strong> [slide 68]</td><td>Blurred vision, photophobia, <strong>xanthopsia</strong> (seeing yellow), <strong>shining lights around objects and yellow-green halos</strong></td></tr>
    <tr><td><strong>Central</strong> [slide 69]</td><td>Delirium, fatigue, confusion, dizziness and abnormal dreams</td></tr>
    <tr><td><strong>Cardiac</strong> [slide 70]</td><td><strong>Nodal slowing</strong> with a longer PR interval (slower conduction from the atria to the ventricles), a shorter QT interval (a shorter ventricular recovery time) and a depressed ST segment; <strong>bradycardia</strong>; digoxin-induced afterdepolarization (the electrocardiogram on slide 70 shows normal sinus beats alternating with premature ventricular beats, and ST depression)</td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 50:05 of the recording: <em>&ldquo;These can be clues&hellip; you can start to see things like xanthopsia&hellip; xanth as a prefix means yellow, so they get this kind of yellow greenish sort of color discoloration, and they start to see halos around lights&hellip; that clues me in, that&rsquo;s like pathognomonic for digoxin, like there&rsquo;s nothing else that does that, and so that should really clue you in&hellip; we need to check a level right away.&rdquo;</em> At 51:00 of the recording: <em>&ldquo;The other big toxicity will be cardiac in nature, so bradycardia is most common, but you can see just about any arrhythmia can be caused by too much digoxin&hellip; PVCs kind of give you a clue&hellip; ventricles are a little more sensitive, and they&rsquo;re more twitchy.&rdquo;</em></p>
    <p><mark class="prof-highlight">Yellow-green halos and xanthopsia point to digoxin toxicity</mark>; the next step is a digoxin level [slide 68]. Bradycardia is classically listed as the most common cardiac toxicity, and premature ventricular beats are also very common, but just about any arrhythmia can occur; the ventricles become more sensitive, which is why premature ventricular beats are a clue [slide 70].</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; &ldquo;pathognomonic&rdquo;, and the two kinds of halos.</strong> Dr. Wood called yellow-green halos with xanthopsia
  pathognomonic for digoxin (&ldquo;there&rsquo;s nothing else that does that&rdquo;). Treat it as a strong clue, not an absolute: slide 80 lists <strong>halos as a side effect of ivabradine</strong> (see 1.13), and halos around
  lights also occur in eye disease such as glaucoma and cataract (not on the slides). What separates them: <strong>digoxin</strong> gives a <strong>yellow-green tint to vision (xanthopsia)</strong> with halos, blurred vision, nausea,
  confusion and a slow or irregular pulse, in a patient with a high digoxin level; <strong>ivabradine</strong> gives <strong>transient brightness in a limited part of the visual field (phosphenes)</strong>, halos and multiple images, in a patient
  taking ivabradine, and it can resolve on its own. With the digoxin picture, the next step is a digoxin level.</div>

  <h4 class="subsub">Contraindications and risk factors (Objective 7) [slide 71]</h4>
  <p>The slide lists: <strong>advanced atrioventricular block</strong>; <strong>severe bradycardia or sick sinus syndrome</strong>; <strong>premature ventricular contractions and ventricular tachycardia</strong>;
  <strong>hypomagnesemia</strong>; <strong>hypercalcemia</strong>; <strong>Wolff-Parkinson-White syndrome</strong>; and electrolyte problems (the slide writes hyperkalemia; see the box, which adds the hypokalemia the slide omits).
  Electrolyte disturbances make toxicity more likely (Dr. Wood, 51:34).</p>

  <div class="callout"><strong>Deck versus truth &mdash; potassium and digoxin.</strong> Slide 71 lists <em>hyperkalemia</em>, and Dr. Wood said
  &ldquo;hyperkalemic&rdquo; at 51:39, but the deck contradicts itself: slide 19 says the <strong>hypokalemia and hypomagnesemia of a loop diuretic</strong>
  bring digitalis arrhythmias, and slide 29 says a thiazide increases digitalis toxicity, so <strong>potassium should be kept above 4.0 mEq per liter</strong>.
  The truth: <strong>low potassium (hypokalemia), low magnesium (hypomagnesemia) and high calcium (hypercalcemia) increase digoxin toxicity</strong>,
  because potassium competes with digoxin at the sodium-potassium pump, so a low level lets more digoxin bind. (In acute digoxin overdose a very high potassium
  marks severe poisoning, which is a different point.) The guide follows the truth, and a question never keys hyperkalemia as a digoxin risk factor.
  This is why a heart failure patient on a loop diuretic needs the potassium watched, and why the same patient on an ACE inhibitor and a potassium supplement complicates things:
  in his words, &ldquo;it gets complicated&rdquo; (52:01).</div>

  <h4 class="subsub">Digoxin immune Fab (the antidote) [slide 72]</h4>
  <p>Digoxin immune Fab (Fab means fragment antigen-binding, the part of an antibody that grips its target; the current brand is DigiFab, which the slide spells Digiband) is an <strong>antibody fragment</strong> that binds digoxin (the slide words this as binding the antigen-binding site of immunoglobulin, which is garbled: the fragment&rsquo;s own antigen-binding site is what grips the digoxin), made by <strong>immunizing healthy sheep
  with digoxin coupled to human serum albumin</strong>. Its <strong>affinity for digoxin is higher than the affinity of digoxin for the sodium-potassium ATPase</strong>, so it pulls the drug off the pump and <strong>rapidly reverses toxicity</strong>.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 52:09 of the recording: <em>&ldquo;If you had a patient who was in dire straits with digoxin and they needed to have it reversed, we do have an immune antibody&hellip; we basically hyper immunized sheep to digoxin and they produce these antibodies, and then we take that antibody and we give it to the patient, and so what this will do is bind to the digoxin and neutralize it&hellip; this will rapidly reverse the digoxin toxicity. Be careful though, because it can unmask whatever&hellip; digoxin was treating, so they may go back in afib or they may have a heart failure decompensation, but again it&rsquo;s better than being dead&hellip;&rdquo;</em></p>
    <p><mark class="prof-highlight">Digoxin toxicity is reversed with digoxin immune Fab</mark>, which can unmask the atrial fibrillation or heart failure the digoxin was treating [slide 72].</p>
  </div>

  <h3 class="sub" id="dh-hfother">1.12 &middot; Objectives 1&ndash;7 &mdash; Aldosterone antagonists in heart failure and the other inotropic agents</h3>

  <h4 class="subsub">Aldosterone antagonists in heart failure [slide 73]</h4>
  <ul>
    <li><strong>Spironolactone:</strong> <strong>mortality reduction in grade III or IV heart failure</strong> (slide 37 says class IV and slide 73 says grade III or IV for the same functional scale; learn it as advanced heart failure, see the box in 1.5); patients are <strong>not eligible if the potassium is above 5 or the serum creatinine above 2.5</strong>; gynecomastia in about 10 percent of men (it may respond to a lower dose).</li>
    <li><strong>Eplerenone:</strong> <strong>gynecomastia is rare</strong> (the slide says &ldquo;no gynecomastia&rdquo;; spironolactone causes it in about 10 percent of men).</li>
    <li><strong>Mechanism in heart failure:</strong> neurohormonal inhibition, slowed remodeling of the left ventricle, slowed progression of heart failure.</li>
  </ul>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 53:10 of the recording: <em>&ldquo;Remember we talked about spironolactone and eplerenone. Here we do see this does provide some mortality reduction in later stage heart failure, but they will be contraindicated if the potassium is too high or the serum creatinine is too elevated&hellip; with kidney dysfunction you&rsquo;re more likely to see a hyperkalemia and just more likelihood for arrhythmias&hellip; if you do see that kind of feminizing effects&hellip; switch to eplerenone, you&rsquo;ll see less of that androgen sort of activity.&rdquo;</em></p>
    <p>Aldosterone antagonists <mark class="prof-highlight">reduce mortality in advanced heart failure</mark> but are <mark class="prof-highlight">avoided with a high potassium or a high serum creatinine</mark>; eplerenone for the breast effects [slide 73].</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; why spironolactone causes the breast and menstrual effects.</strong> Slide 38 calls spironolactone a &ldquo;partial agonist at testosterone receptors&rdquo;, and Dr. Wood used that wording (25:39).
  In truth, spironolactone is an <strong>androgen receptor antagonist</strong>: it blocks testosterone&rsquo;s action (and has some progesterone-like activity), which gives gynecomastia in men and menstrual irregularity in women. The same antiandrogen action is why it is used for
  hirsutism and acne (not on the slides). Eplerenone binds the aldosterone receptor far more selectively, so it rarely has such an effect. What to learn is unchanged: <strong>breast enlargement or menstrual irregularity on spironolactone means switch to eplerenone</strong>; do not learn &ldquo;partial agonist&rdquo; as the mechanism (the full discussion is in the box in 1.5).</div>

  <h4 class="subsub">Milrinone and inamrinone [slides 74 to 76]</h4>
  <ul>
    <li><strong>Milrinone</strong> (Primacor) and <strong>inamrinone</strong> (Inocor, formerly amrinone) are <strong>cyclic adenosine monophosphate (cyclic AMP) phosphodiesterase (type III) inhibitors</strong> [slide 74; the structures are pictured]: by blocking the enzyme that breaks cyclic AMP down, they let it rise in the heart (the recording, 54:05).</li>
    <li>They are <strong>inotropic and vasodilator</strong>: direct stimulation of myocardial contraction, <strong>balanced arterial and venous dilation</strong>, <strong>decreased afterload</strong> and increased cardiac output [slide 75].</li>
    <li><strong>Approved for short-term intravenous use in acute decompensated heart failure</strong>; <strong>long-term use is associated with higher mortality and morbidity than placebo</strong> [slide 76].</li>
    <li>Adverse effects: <strong>thrombocytopenia</strong> (less with milrinone) and <strong>ventricular arrhythmias</strong> [slide 76].</li>
  </ul>
  <h4 class="subsub">Dobutamine and dopamine [slide 77]</h4>
  <ul>
    <li><strong>Dobutamine</strong> is a <strong>selective beta-1 agonist</strong>; intravenous infusion stimulates the force of contraction more than the rate; used <strong>short term to stabilize patients</strong>.</li>
    <li><strong>Dopamine</strong>: intravenous infusion; acts through dopamine and beta receptors (the slide adds that it maintains renal function; see the box).</li>
  </ul>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 55:32 of the recording: <em>&ldquo;Your main question will be, what&rsquo;s the patient hypo or hypertensive? If they&rsquo;re hypertensive, then milrinone works better. If they&rsquo;re going to be hypotensive, then something like&hellip; dobutamine or dopamine tends to make more sense from that standpoint.&rdquo;</em> And at 54:42: <em>&ldquo;You really just want to use it for short term, because if you leave them on it for too long you can see risk for arrhythmia start to go up.&rdquo;</em></p>
    <p><mark class="prof-highlight">Pick milrinone (vasodilator) for a decompensated patient with high blood pressure and dobutamine or dopamine for low blood pressure</mark>; all are short-term, started in hospital [slides 75 to 77]. Why: milrinone&rsquo;s balanced vasodilation lowers blood pressure (hypotension is a known adverse effect, not on the slide), so it suits the high-pressure patient, while dobutamine and dopamine raise the force of contraction with much less vasodilation than milrinone (the recording, 55:22; dobutamine can still lower systemic vascular resistance modestly, and dopamine at higher doses constricts vessels).</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; dopamine.</strong> Slide 77 says dopamine infusions &ldquo;maintain renal function&rdquo;. Low-dose
  dopamine has not been shown to protect the kidney, so this is not examined. Dr. Wood also said dopamine causes alpha constriction at higher doses; that is not on the slides.
  Not on the slides either: dopamine carries an FDA boxed warning about tissue injury if the infusion leaks out of the vein (extravasation).</div>

  <h3 class="sub" id="dh-newer">1.13 &middot; Objectives 1&ndash;7 &mdash; Newer agents: ivabradine, sacubitril-valsartan, sodium-glucose cotransporter 2 inhibitors</h3>

  <h4 class="subsub">Ivabradine (Procoralan) [slides 79 and 80]</h4>
  <ul>
    <li><strong>Mechanism:</strong> a <strong>hyperpolarization-activated cyclic nucleotide-gated channel blocker</strong> that <strong>inhibits the pacemaker current in the sinoatrial node</strong>. It <strong>reduces heart rate and does not affect contractility</strong> (unlike a beta blocker).</li>
    <li><strong>Use:</strong> heart failure patients <strong>who are maxed out on beta blockers</strong>, in <strong>normal sinus rhythm with a heart rate above 70 beats per minute</strong>. It has been shown to <strong>decrease hospitalization and heart-failure-related death</strong>.</li>
    <li><strong>Adverse reactions:</strong> <strong>increased risk of atrial fibrillation</strong>; <strong>symptomatic bradycardia</strong>; <strong>visual impairment (phosphenes)</strong>: it affects the retinal photoreceptors, with transient brightness in a limited area of the visual field, halos and multiple images (retinal persistency); it can resolve on its own.</li>
    <li><strong>Contraindications:</strong> similar to beta blockers: hypotension, heart block, a pacemaker, and so on.</li>
  </ul>
  <h4 class="subsub">Sacubitril (formulated with valsartan, Entresto) [slide 81]</h4>
  <ul>
    <li><strong>Mechanism:</strong> a <strong>neprilysin inhibitor</strong>. Neprilysin normally degrades vasoactive peptides (natriuretic peptide, bradykinin and others); inhibiting it causes <strong>vasodilation, natriuresis and diuresis</strong> and inhibits growth and fibrosis of myocardial tissue. The partner valsartan is an angiotensin receptor blocker.</li>
    <li><strong>Use:</strong> to <strong>reduce the risk of cardiovascular death and hospitalization</strong> in heart failure.</li>
    <li><strong>Never with an ACE inhibitor: allow a 36-hour washout period</strong> to avoid adverse effects.</li>
    <li><strong>Most common adverse effects:</strong> hypotension, hyperkalemia, cough and renal insufficiency.</li>
  </ul>
  <h4 class="subsub">Sodium-glucose cotransporter 2 (SGLT2) inhibitors [slide 82]</h4>
  <ul>
    <li><strong>Dapagliflozin</strong> (Farxiga) and <strong>empagliflozin</strong> (Jardiance), used for <strong>stable, chronic heart failure with reduced ejection fraction</strong>; they <strong>reduce mortality and hospitalizations</strong>.</li>
    <li>Originally for diabetes: they make the kidneys <strong>not reabsorb glucose</strong> (they block the sodium-glucose transporter in the proximal tubule).</li>
    <li><strong>Risks: hypotension and fungal urinary tract infections.</strong> Dr. Wood: hypotension because they cause the patient to lose fluid, and fungal infections because there is more sugar in the genitourinary tract.</li>
  </ul>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 56:22 of the recording: <em>&ldquo;This just reduces the heart rate, it doesn&rsquo;t affect the contractility. So who do you use this in? This is for patients who are maxed out on beta blockers but they still have a normal sinus rhythm and heart rate above 70.&rdquo;</em> At 58:01: <em>&ldquo;Keep in mind you would not want to use this with an ACE inhibitor&hellip; to avoid having that overlap, that overlap would include things like hypotension, hyperkalemia, cough, etc.&rdquo;</em> At 59:19: <em>&ldquo;So now this is another one of those necessary add-on medications to patients&hellip; these SGLT2 inhibitors&hellip; especially reduced ejection fraction, you see reduction mortality and hospitalizations.&rdquo;</em></p>
    <p><mark class="prof-highlight">Ivabradine: beta blocker maxed out, sinus rhythm, rate above 70. Sacubitril-valsartan: never with an ACE inhibitor, with a washout. SGLT2 inhibitors: a necessary add-on, with hypotension and fungal infections.</mark> [slides 79 to 82]</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; the newer agents.</strong>
  <ul>
    <li><strong>Ivabradine.</strong> Slide 79 says it decreases hospitalization and heart-failure-related death. The benefit that carries its approval is fewer hospitalizations for worsening heart failure; it has not been shown to lower overall mortality,
    so do not sort it with the mandatory survival drugs. The &ldquo;heart rate above 70&rdquo; is for patients taking the maximally tolerated beta blocker dose, and it works only in sinus rhythm, which is why atrial fibrillation matters. Its halos are not digoxin&rsquo;s (see 1.11).</li>
    <li><strong>Sacubitril-valsartan.</strong> Slide 81 gives the washout as &ldquo;to avoid adverse effects&rdquo;; Dr. Wood named hypotension, hyperkalemia and cough. Not on the slides: the main reason is <strong>angioedema</strong>, because both ACE inhibitors and neprilysin inhibition
    let bradykinin build up, so a history of angioedema is a contraindication. Sacubitril-valsartan also <strong>carries an FDA boxed warning for fetal toxicity</strong> (stop it when pregnancy is detected).</li>
    <li><strong>SGLT2 inhibitors.</strong> Slide 82 says fungal urinary tract infections; the typical infection is a genital yeast infection. Also not on the slides: they carry a risk of diabetic ketoacidosis that can occur with normal blood glucose, and they help heart failure with preserved ejection fraction too.</li>
  </ul></div>
'''

BODY += '''
  <h3 class="sub" id="dh-summary">1.14 &middot; Objectives 4 and 8&ndash;10 &mdash; Absorption, interactions, monitoring and patient education</h3>

  <h4 class="subsub">Absorption, distribution, metabolism and excretion (Objective 4)</h4>
  <p>The slides give very little for this objective. <strong>Digoxin:</strong> the sugar molecules attached to the steroid nucleus influence absorption, half-life and metabolism [slide 61].
  <strong>Nephron handling:</strong> the proximal tubule excretes weak acids and bases into the lumen [slide 8], and loop diuretics keep working when the creatinine clearance is below 30 milliliters per minute
  while the slide says thiazides lose effect (metolazone excepted; newer data show chlorthalidone still works, see 1.3) [slides 16 and 28]. <strong>Carbonic anhydrase inhibitors:</strong> their diuretic effect fades after 3 to 5 days [slide 39].
  <strong>Digoxin immune Fab</strong> has a higher affinity for digoxin than digoxin has for its pump [slide 72]. Dr. Wood added in passing that digoxin is cleared by the kidneys (not on a slide).</p>

  <h4 class="subsub">Interactions (Objective 8)</h4>
  <table>
    <tr><th>Combination</th><th>What happens</th></tr>
    <tr><td><strong>Loop or thiazide diuretic with a nonsteroidal anti-inflammatory drug</strong></td><td>Prostaglandin block blunts the natriuretic and blood pressure response [slides 14, 19 and 29]</td></tr>
    <tr><td><strong>Loop diuretic with an aminoglycoside</strong></td><td>Ototoxicity is potentiated [slide 19]</td></tr>
    <tr><td><strong>Loop diuretic with warfarin</strong></td><td>They compete for plasma protein binding [slide 19]</td></tr>
    <tr><td><strong>Loop diuretic with lithium</strong></td><td>Lithium clearance falls and toxicity rises [slide 19]</td></tr>
    <tr><td><strong>Loop or thiazide diuretic with digoxin (digitalis)</strong></td><td>Hypokalemia and hypomagnesemia bring arrhythmias and increase digitalis toxicity; keep potassium above 4.0 mEq per liter [slides 19 and 29]</td></tr>
    <tr><td><strong>Potassium-sparing diuretic with an ACE inhibitor, an angiotensin receptor blocker or a potassium supplement</strong></td><td>Hyperkalemia [slide 33]; the same added risk applies to aldosterone antagonists with a high potassium or creatinine [slide 73]</td></tr>
    <tr><td><strong>Diuretics with ACE inhibitors or calcium channel blockers</strong></td><td>Synergy, because these block the kidney&rsquo;s compensatory renin-angiotensin response (the recording, 1:48)</td></tr>
    <tr><td><strong>Sacubitril-valsartan with an ACE inhibitor</strong></td><td>Do not combine; allow a 36-hour washout to avoid overlapping adverse effects, which Dr. Wood named as hypotension, hyperkalemia and cough [slide 81; the recording, 58:01]; the main reason, angioedema, is not on the slide (see 1.13)</td></tr>
    <tr><td><strong>Loop plus potassium-sparing diuretic</strong></td><td>Used on purpose to offset potassium loss [recording, 21:54]</td></tr>
  </table>
  <p>The slides name <strong>no drug-herb interactions</strong> and no drug-food interaction, and none for digoxin. Not on the slides: amiodarone, verapamil, quinidine and macrolide antibiotics such as clarithromycin raise digoxin levels, and St. John&rsquo;s wort lowers them. The recording adds the salt-substitute point: salt substitutes are potassium chloride and add to hyperkalemia risk with potassium-sparing diuretics, ACE inhibitors and angiotensin receptor blockers.</p>

  <h4 class="subsub">Protocols and monitoring (Objective 9)</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give</th></tr>
    <tr><td><strong>Daily weight</strong></td><td>Worsening fluid overload shows up as weight gain over several days; heart failure patients on a loop diuretic are watched this way [slide 52]</td></tr>
    <tr><td><strong>Potassium and kidney function</strong></td><td>ACE inhibitors raise potassium and can impair kidney function [slide 56]; potassium above 4.0 mEq per liter with a thiazide and digitalis [slide 29]; spironolactone is not for a potassium above 5 or a serum creatinine above 2.5 [slide 73]</td></tr>
    <tr><td><strong>Beta blockers in heart failure</strong></td><td>Start low in a stable patient, titrate up slowly, monitor for worsening heart failure signs and symptoms [slide 58]</td></tr>
    <tr><td><strong>Digoxin level</strong></td><td>Target 0.5 to 1 nanogram per milliliter; higher levels may do worse [slide 65]; Dr. Wood said he is probably not going to quiz the number, so know that a level is checked, especially when toxicity is suspected</td></tr>
    <tr><td><strong>Short-term intravenous agents</strong></td><td>Milrinone, inamrinone, dobutamine and dopamine are started in hospital for acute decompensation and stopped as the patient stabilizes [slides 76 and 77]</td></tr>
    <tr><td><strong>Sodium and fluid restriction</strong></td><td>[slide 51]</td></tr>
    <tr><td><strong>Washout</strong></td><td>36 hours between an ACE inhibitor and sacubitril-valsartan [slide 81]</td></tr>
  </table>

  <h4 class="subsub">Patient education (Objective 10)</h4>
  <ul>
    <li><strong>All heart failure patients:</strong> restrict sodium and fluid; weigh yourself every day and report a gain over several days, which is fluid [slides 51 and 52].</li>
    <li><strong>Loop and thiazide diuretics:</strong> expect volume depletion and dizziness; photosensitivity and rash; report hearing problems with a loop diuretic; gout and high blood sugar are possible; potassium and magnesium need monitoring [slides 18, 26 and 27].</li>
    <li><strong>Potassium-sparing diuretics, aldosterone antagonists, ACE inhibitors, angiotensin receptor blockers and sacubitril-valsartan:</strong> be cautious with potassium supplements and salt substitutes (potassium chloride) [slides 33, 56 and 81; the salt-substitute point is from the recording].</li>
    <li><strong>Spironolactone:</strong> breast enlargement in men and menstrual irregularity in women are the reason to ask for eplerenone [slide 38].</li>
    <li><strong>Carbonic anhydrase inhibitors:</strong> drowsiness [slide 43].</li>
    <li><strong>Beta blockers in heart failure:</strong> they are started low and increased slowly, and the patient should report worsening heart failure symptoms [slide 58].</li>
    <li><strong>Digoxin:</strong> report nausea, loss of appetite, yellow-green halos or blurred vision, confusion and a slow pulse, which are signs of toxicity [slides 68 to 70].</li>
    <li><strong>Ivabradine:</strong> a transient brightness in part of the visual field, halos or multiple images can happen and may resolve on their own [slide 80].</li>
    <li><strong>SGLT2 inhibitors:</strong> dizziness from low blood pressure and fungal infections of the genitourinary tract [slide 82].</li>
  </ul>

  <div class="pearl"><strong>Symptoms versus survival, one table.</strong>
  <table>
    <tr><th>Relieves symptoms only</th><th>Prolongs survival (mandatory or necessary add-on)</th></tr>
    <tr><td>Loop diuretics (and thiazides, where strong enough) [slides 52 and 53]; digoxin [slide 66]</td><td>ACE inhibitors or angiotensin receptor blockers [slide 54]; carvedilol, metoprolol succinate and bisoprolol [slide 57]; spironolactone and eplerenone in advanced failure [slide 73]; sacubitril-valsartan [slide 81]; SGLT2 inhibitors [slide 82]</td></tr>
  </table>
  Milrinone is not on either list: it is short-term support for acute decompensation, and long-term use raises mortality [slide 76]. Ivabradine is not on either list either: it reduces hospitalization (the slide adds heart-failure-related death) but has not been shown to lower overall mortality [slide 79]. Not on the slides: the survival evidence for these drugs comes from heart failure with reduced ejection fraction (the slides say so only for the SGLT2 inhibitors).</div>

  <div class="callout"><strong>What is left out of this section, and why.</strong>
  <ul>
    <li><strong>Milligram doses.</strong> Doses are not tested in this course. The deck gives none.</li>
    <li><strong>The digoxin target level.</strong> It is stated in 1.10 because the slide gives it, but Dr. Wood said he is probably not going to quiz it.</li>
    <li><strong>Percentages and numbers.</strong> The sodium percentages by nephron site, the 20 to 25 percent and 4 liters of loops, the 1 to 2 liters of thiazides, the 80 to 90 percent bicarbonate figure, 50 to 60 percent of heart failure caused by ischemia, the 45 percent ejection fraction, the sodium and fluid limits, the weight-gain figure, 6 to 8 weeks of beta blocker titration and the 36-hour washout are stated for recognition. Learn the direction and the idea, not the figure.</li>
    <li><strong>Where the deck is wrong or loose,</strong> a &ldquo;Deck versus truth&rdquo; box says so: slides 9 and 10 (nephron), 21 and 42 (side actions), 23 (uric acid), 25 (obesity), 28 (clearance), 30 (antiporters), 36 (calcium, lag), 37 against 73 (class IV or III and IV), 38 (partial agonist), 46 (45 percent), 51, 52 and 58 (numbers), 62 (calcium exchanger), 67 (first line), 68 against 80 (the two kinds of halos), 71 (hyperkalemia), 72 (antibody wording), 77 (dopamine and the kidney), 79 (ivabradine mortality), 81 (washout reason) and 82 (fungal infection site). The boxed warnings that the slides omit (loop diuretics, amiloride, triamterene, sacubitril-valsartan, dopamine, ACE inhibitors, metoprolol) are flagged in the boxes above and are not on the slides.</li>
    <li><strong>Slides not represented:</strong> 1 (title), 2 (the deck&rsquo;s own objectives), 3, 44 and 78 (section dividers) and 83 (&ldquo;Questions?&rdquo;).</li>
  </ul></div>

</section>
'''
