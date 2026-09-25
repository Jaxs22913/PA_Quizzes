# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 study guide -- section 3, Lecture 6 (Antihypertensives).

Imported by build_pharm_e2_guide.py.

SOURCES
  Facts   Antihypertensives.pptx (109 slides), mapped in
          ~/Developer/PA_Quizzes-handoff/2026-09-23/work/pharm-l6l7/antihypertensives-map.md.
          Five slides are embedded Word objects (5, 24, 60, 88, 98) and the
          algorithm (108) is a picture; their content is used from the map's
          viewed transcriptions -- the first-generation beta-blocker table, the
          clonidine pathway, the vasodilator comparison, the algorithm.
  Weight  .../audio-pharm-l6l7/l6-antihypertensives-emphasis.md. The STARS
          (.prof-flag, mark.prof-highlight) are exactly its section 4.2 list;
          the "not examined" callout is its section 2.2. The slide wins every
          conflict in its section 3 (young patients, "mild" reflex tachycardia,
          lower doses of a beta blocker with verapamil, trimester wording), and
          no audio-only fact from its section 3.5 is stated as content.

Two deck problems handled on purpose:
  * Slide 7 prints the macula densa line without its down-arrow. The direction
    is given as he stated it in lecture and labeled so; it is not starred.
  * Slide 75 calls clonidine an "alpha-2 blocker"; slides 86 and 92 say agonist.
    The guide says agonist throughout and names the slip once.
Diuretics, heart-failure drugs, MRAs and ARNIs appear on slide 108 only; they
are Lecture 9 (Exam 3) and are named here as algorithm steps, nothing more.
"""

TOC = '''  <a class="top-link" href="#htn">3 &middot; Antihypertensive Drugs</a>
  <a href="#htn-raas">3.1 Objectives 1&ndash;2 &mdash; The renin-angiotensin system the drugs act on</a>
  <a href="#htn-acei">3.2 Objectives 1&ndash;10 &mdash; ACE inhibitors</a>
  <a href="#htn-arb">3.3 Objectives 1&ndash;8 &mdash; Angiotensin receptor blockers</a>
  <a href="#htn-ccb">3.4 Objectives 1&ndash;8 &mdash; Calcium channel blockers</a>
  <a href="#htn-bb">3.5 Objectives 1&ndash;8 &mdash; Beta blockers</a>
  <a href="#htn-alpha">3.6 Objectives 1&ndash;8 &mdash; Alpha-1 blockers</a>
  <a href="#htn-central">3.7 Objectives 1&ndash;8 &mdash; Central sympatholytics</a>
  <a href="#htn-vaso">3.8 Objectives 1&ndash;7 &mdash; Direct vasodilators</a>
  <a href="#htn-algo">3.9 Objectives 9&ndash;10 &mdash; The treatment algorithm, monitoring and patient education</a>'''

BODY = '''
<section class="deck" id="htn">
  <h2 class="deck-title">3 &middot; Antihypertensive Drugs</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify antihypertensive drug classes and commonly prescribed antihypertensive drugs.</li>
      <li>Describe the molecular mechanism of action of antihypertensive drugs.</li>
      <li>Identify indications for commonly used antihypertensive drugs.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of antihypertensive drugs.</li>
      <li>Summarize side effects and toxic manifestations of antihypertensive drugs.</li>
      <li>Describe adverse effects of antihypertensive drugs.</li>
      <li>Identify contraindications for antihypertensive drugs.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with antihypertensive drugs.</li>
      <li>List commonly used protocols and patient monitoring for antihypertensive drugs.</li>
      <li>Outline appropriate patient education for antihypertensive drugs.</li>
    </ol>
  </div>

  <div class="callout"><strong>What he said is not examined, or not in depth.</strong> Taking these
  at his word frees a lot of the 109 slides.
  <ul>
    <li><strong>Diuretics and heart-failure drugs</strong> &mdash; &ldquo;that&rsquo;s going to get
    broken up into the heart failure lecture&rdquo;, which is Lecture 9 and Exam 3. They appear here
    only as a step in the treatment algorithm.</li>
    <li><strong>Which ACE inhibitors are not prodrugs</strong> &mdash; &ldquo;I don&rsquo;t care
    necessarily that you know that.&rdquo;</li>
    <li><strong>Elimination routes</strong> &mdash; renal against biliary for ACE inhibitors and
    angiotensin receptor blockers, renal against hepatic for beta blockers.</li>
    <li><strong>The plus counts in the calcium channel blocker table</strong> &mdash; &ldquo;am I
    going to have you memorize which one has three pluses versus five pluses? No&rdquo; &mdash; but
    the <em>pattern</em> is examined.</li>
    <li><strong>Membrane stabilizing activity, intrinsic sympathomimetic activity and lipid
    solubility of beta blockers</strong> &mdash; with one exception he kept: propranolol&rsquo;s high
    lipid solubility and its central nervous system effects.</li>
    <li><strong>Carteolol and betaxolol</strong> (glaucoma agents) among the third-generation beta
    blockers; he focuses on carvedilol and labetalol. <strong>Terazosin and doxazosin</strong>
    beyond recognizing them as alpha-1 blockers. The AT2 receptor.</li>
    <li><strong>Depth on migraine, thyroid, diabetes and pregnancy hypertension</strong>, which are
    taught in later courses: know the indication as the slide states it.</li>
  </ul>
  And no doses, as in every lecture of his. His stated question style for this lecture:
  <em>&ldquo;the patient&rsquo;s on this, what do you want to go to next &mdash; or based off of this
  comorbidity, what should you start with.&rdquo;</em></div>

  <div class="pearl"><strong>Name the class from the suffix.</strong> &ldquo;Your job is to be able
  to identify these agents into which class they fit.&rdquo; <strong>-pril</strong> = ACE
  (angiotensin-converting enzyme) inhibitor; <strong>-sartan</strong> = angiotensin receptor
  blocker; <strong>-dipine</strong> = dihydropyridine calcium channel blocker;
  <strong>-olol</strong> = beta blocker; <strong>-zosin</strong> = alpha-1 blocker (not
  piperacillin-tazobactam, the antibiotic). His rule for beta blockers, which holds for every agent
  in the deck&rsquo;s first two tables: names starting <strong>N to Z are non-selective</strong>,
  <strong>A to M are beta-1 selective</strong> &mdash; with <strong>carvedilol and labetalol</strong>
  as the exceptions.</div>

  <h3 class="sub" id="htn-raas">3.1 &middot; Objectives 1&ndash;2 &mdash; The renin-angiotensin system the drugs act on</h3>

  <p>Renin release is controlled three ways: the <strong>renal baroreceptor</strong> (less renal
  perfusion, more renin), the <strong>macula densa</strong>, which senses sodium and chloride in the
  distal tubule, and the <strong>sympathetic nervous system</strong>, through beta-1 receptors on
  the juxtaglomerular cells. The slide prints the macula densa line without its arrow; in lecture
  he gave the direction as <em>a decrease</em> in sodium or chloride stimulating renin release.</p>

  <p>Renin makes angiotensin I; ACE turns it into <strong>angiotensin II</strong>; and the same
  enzyme <strong>breaks down bradykinin</strong>. Angiotensin II acts at the <strong>AT1
  receptor</strong> (heart, endothelium, vascular smooth muscle, kidney) to cause vasoconstriction
  and renal vasoconstriction, aldosterone secretion, sodium reabsorption, increased norepinephrine
  release and central sympathetic outflow, thirst and antidiuretic hormone, and cell hypertrophy
  with cardiac remodeling after a myocardial infarction. Overactivity of the system drives
  hypertension, heart failure, diabetic nephropathy and post-infarction remodeling &mdash; which is
  why those are the indications for the drugs that block it.</p>

  <div class="pearl"><strong>Two drugs, two points in the same chain.</strong> ACE inhibitors stop
  angiotensin II being <em>made</em> &mdash; and so also stop bradykinin being <em>broken
  down</em>. Angiotensin receptor blockers stop angiotensin II <em>acting</em> at AT1 and leave
  bradykinin alone. Almost every difference between the two classes in 3.2 and 3.3 comes from that
  one sentence.</div>

  <h3 class="sub" id="htn-acei">3.2 &middot; Objectives 1&ndash;10 &mdash; ACE inhibitors</h3>

  <p><strong>Agents (-pril):</strong> captopril, lisinopril, enalapril (whose active form,
  <strong>enalaprilat, is the intravenous one</strong>), benazepril, fosinopril, trandolapril,
  quinapril, ramipril, perindopril, moexipril. They share an identical mechanism and differ only in
  half-life and metabolism; most are dosed once daily, captopril more often because its half-life
  is short, and when the effect wears off before the next dose a twice-daily schedule is used.</p>

  <p><strong>Mechanism:</strong> blocking ACE lowers angiotensin II, so there is less vasoconstriction
  and renal vasoconstriction, less aldosterone and sodium reabsorption, and less angiotensin-driven
  norepinephrine release; bradykinin metabolism falls; and with the negative feedback gone,
  angiotensin I and renin rise.</p>

  <p><strong>Indications.</strong> Hypertension &mdash; lowering total peripheral resistance, systolic
  and diastolic pressure, and left ventricular hypertrophy &mdash; and
  <mark class="prof-highlight">preferred in diabetics (kidney protective effects)</mark>. Left
  ventricular dysfunction and heart failure, where they reduce remodeling, afterload and preload,
  raise cardiac output and cut infarctions and hospital admissions:
  <mark class="prof-highlight">ACE inhibitors should be given to all with LV dysfunction unless
  contraindicated</mark>. After a myocardial infarction, to reduce remodeling and overall mortality.
  And <strong>diabetic nephropathy</strong>, by lowering glomerular pressure.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><strong>Hyperkalemia &mdash; &uarr; K+ levels &mdash; most often seen
    with renal disease, and those taking potassium sparing diuretics, K+ supplements or salt
    substitutes.</strong></p>
    <p>His strongest cue of the whole lecture: <em>&ldquo;anytime you have a medication which
    affects your potassium levels you have to know that&hellip; it&rsquo;s a very easy test question
    to ask.&rdquo;</em> The same warning applies to angiotensin receptor blockers (3.3). The patient
    education that follows from it: no potassium supplements or salt substitutes without asking.</p>
  </div>

  <table>
    <tr><th>Adverse effect</th><th>What the slide says</th></tr>
    <tr><td><strong>Dry cough</strong></td><td>5 to 15%; <strong>bradykinin and substance P accumulate in the lungs</strong>; appears 1 week to 6 months into therapy; not dose- or agent-related; more frequent in women; may require stopping the drug</td></tr>
    <tr><td><strong>First-dose hypotension</strong></td><td>With the first dose or an increase; most common in <strong>sodium-depleted patients, heart failure, or those on multiple antihypertensives</strong></td></tr>
    <tr><td><strong>Renal impairment</strong></td><td>Where renal blood flow depends on angiotensin II, <mark class="prof-highlight">ACE inhibitors will dramatically decrease GFR &mdash; use cautiously, low doses move upward slowly</mark></td></tr>
    <tr><td><strong>Angioedema</strong></td><td>Rare (0.1 to 0.5%): rapid swelling of nose, throat, mouth, larynx, lips and tongue; usually in the <strong>first week</strong>; reversible on stopping; <strong>bradykinin</strong>-mediated</td></tr>
    <tr><td><strong>Fetal harm</strong></td><td><mark class="prof-highlight">Contraindicated in 2nd and 3rd trimesters. Birth defects and fetal death</mark></td></tr>
  </table>

  <div class="callout"><strong>Kidney protective, yet able to drop the GFR &mdash; both are true.</strong>
  His explanation: angiotensin II constricts the <em>efferent</em> arteriole. Take it away and
  glomerular pressure falls. In a kidney that depends on angiotensin II to keep filtering, that fall
  is an acute drop in glomerular filtration rate (GFR) &mdash; hence start low and titrate slowly.
  Over the long term the same lower pressure is what protects the diabetic kidney.</div>

  <p><strong>Interactions:</strong> <strong>NSAIDs (nonsteroidal anti-inflammatory drugs) decrease
  the ACE inhibitor effect</strong> &mdash; the slide&rsquo;s reason is that they block the
  prostaglandin-mediated relaxation bradykinin produces; potassium-sparing diuretics, potassium
  supplements and salt substitutes cause hyperkalemia; several antihypertensives together raise the
  risk of first-dose hypotension. No drug-food or drug-herb interaction is given for any class in
  this lecture.</p>

  <h3 class="sub" id="htn-arb">3.3 &middot; Objectives 1&ndash;8 &mdash; Angiotensin receptor blockers</h3>

  <p><strong>Agents (-sartan):</strong> candesartan, olmesartan, losartan, azilsartan, eprosartan,
  irbesartan, telmisartan, valsartan. <strong>Why they exist:</strong> ACE is not the only enzyme
  that makes angiotensin II &mdash; trypsin, cathepsin and chymase do too &mdash; so an ACE inhibitor
  never removes it completely. <strong>Mechanism:</strong> high-affinity, slowly dissociating,
  sustained blockade of the <strong>AT1 receptor</strong>, giving vasodilation, renal vasodilation,
  less aldosterone, less sodium reabsorption and less norepinephrine release.</p>

  <p><strong>Indications:</strong> hypertension; <strong>left ventricular dysfunction when an ACE
  inhibitor cannot be tolerated</strong>; diabetic nephropathy. AT1 receptors are saturated at
  starting doses, so raising the dose changes blood pressure little; <strong>adding a diuretic
  increases the effect</strong>, most come as combinations, and a diuretic helps in salt-sensitive
  hypertension, where they are less effective alone. In heart failure, start low and titrate up.</p>

  <p><strong>Adverse effects</strong> are the ACE inhibitor list minus bradykinin:
  <mark class="prof-highlight">hyperkalemia &mdash; renal disease or K+ sparing diuretics</mark>;
  first-dose hypotension; impaired renal function; and fetal morbidity and mortality &mdash; not
  given in the 2nd and 3rd trimesters.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <table>
      <tr><th></th><th>ACE inhibitor</th><th>Angiotensin receptor blocker</th></tr>
      <tr><td>Bradykinin</td><td>Not broken down &rarr; <strong>cough and angioedema</strong></td><td><mark class="prof-highlight">ARB&rsquo;s don&rsquo;t inhibit breakdown of bradykinin (disadvantage)</mark></td></tr>
      <tr><td>Cough</td><td>5 to 15%</td><td><mark class="prof-highlight">Do not cause cough &mdash; don&rsquo;t affect bradykinin metabolism</mark></td></tr>
      <tr><td>Angioedema</td><td>Rare but real</td><td><mark class="prof-highlight">Lower incidence of angioedema, may switch from ACE inhibitor</mark></td></tr>
      <tr><td>Angiotensin II at AT1</td><td>Reduced, not abolished</td><td>Better at reducing its effect at AT1</td></tr>
      <tr><td>Hyperkalemia, pregnancy</td><td colspan="2">Both &mdash; the same warnings</td></tr>
    </table>
    <p><em>&ldquo;Those are the key things and again great for test questions.&rdquo;</em> The
    classic stem: a patient on an ACE inhibitor develops a dry cough &mdash; switch to an
    angiotensin receptor blocker.</p>
  </div>

  <h3 class="sub" id="htn-ccb">3.4 &middot; Objectives 1&ndash;8 &mdash; Calcium channel blockers</h3>

  <p>All calcium channel blockers block the <strong>L-type calcium channel</strong>, found in
  vascular smooth muscle, cardiac myocytes and the sinoatrial and atrioventricular nodes. Two facts
  shape the whole class. At therapeutic doses they <strong>do not reduce venous tone</strong>, so
  they lower afterload without changing preload. And because arteries depend on calcium from
  outside the cell while myocytes also draw on the sarcoplasmic reticulum, <strong>arteries are 3
  to 10 times more sensitive</strong> to these drugs than the myocardium. Class uses: angina,
  hypertension, supraventricular arrhythmias, diastolic heart failure, cerebral ischemia and
  migraine prophylaxis.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px"><strong>Non-DHP reduce both slow inward current AND decrease rate of
    recovery &rarr; slow AV conduction. DHP reduce slow inward current without affecting recovery
    &rarr; no effect on AV conduction.</strong> (DHP = dihydropyridine; AV = atrioventricular.)</p>
    <table>
      <tr><th></th><th>Diltiazem</th><th>Verapamil</th><th>Dihydropyridines</th></tr>
      <tr><td>Vasodilation</td><td>Strong</td><td>Stronger</td><td><strong>Strongest</strong></td></tr>
      <tr><td>Suppresses contractility</td><td>Moderate</td><td><strong>Most</strong></td><td>None to minimal</td></tr>
      <tr><td>Suppresses sinoatrial automaticity</td><td><strong>Marked</strong></td><td><strong>Marked</strong></td><td>Minimal</td></tr>
      <tr><td>Slows atrioventricular conduction</td><td><strong>Marked</strong></td><td><strong>Marked</strong></td><td>None</td></tr>
    </table>
    <p>Learn the <strong>pattern</strong>, not the plus counts he waved away: <strong>the
    non-dihydropyridines work on the heart; the dihydropyridines work on the vessels.</strong>
    <em>&ldquo;Which one of these would you use to reduce heart rate &mdash; it&rsquo;s either
    diltiazem or verapamil.&rdquo;</em> Indications, side effects and contraindications all follow
    from this one table.</p>
  </div>

  <h4 class="subsub">Non-dihydropyridines: diltiazem (Cardizem) and verapamil (Calan)</h4>

  <p>Intravenous or oral. <strong>Indications:</strong> angina, hypertension, and
  <mark class="prof-highlight">supraventricular tachycardia &mdash; atrial fibrillation or flutter,
  paroxysmal supraventricular tachycardia</mark>. <strong>Adverse effects:</strong> peripheral
  vasodilation (flushing, headache, hypotension, peripheral edema, dizziness); the cardiac set
  &mdash; <mark class="prof-highlight">first-degree AV block, bradycardia, exacerbation of congestive
  heart failure</mark>; gastrointestinal effects, including <mark class="prof-highlight">constipation</mark>,
  which is worth asking the patient about; raised liver enzymes; central effects; gynecomastia or
  sexual dysfunction; <strong>gingival hyperplasia</strong>; skin reactions.
  <strong>Contraindications:</strong> advanced heart block and hypotension; relatively, heart
  failure, liver disease and gastroesophageal reflux disease.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">Non-dihydropyridines are <strong>CYP3A4 (cytochrome P450 3A4)
    inhibitors</strong> &mdash; raising <strong>statins (atorvastatin, lovastatin,
    simvastatin)</strong>, carbamazepine, propranolol, tacrolimus and cyclosporine &mdash; and
    <strong>P-glycoprotein inhibitors</strong>, raising tacrolimus, cyclosporine, carbamazepine and
    <strong>digoxin</strong>. <em>&ldquo;Note that down, start underlining.&rdquo;</em> The statins
    in that list are the same three that Lecture 7 names as CYP3A4 substrates (section 4.2).</p>
  </div>

  <p>Pharmacodynamic interactions: amiodarone (slower sinus rate, worse atrioventricular block),
  digoxin, and beta blockers &mdash; with a beta blocker the effects on blood pressure, heart rate
  and contractility are synergistic, so <strong>in combination use lower doses of each</strong>.
  CYP3A4 inhibitors lengthen the non-dihydropyridine&rsquo;s own half-life.</p>

  <h4 class="subsub">Dihydropyridines (-dipine)</h4>

  <p>Oral only, <strong>except nicardipine</strong>, which has an intravenous form. Amlodipine,
  nifedipine and nicardipine treat angina and hypertension; felodipine, isradipine and nisoldipine,
  hypertension; <strong>nimodipine, subarachnoid hemorrhage</strong>. <strong>Adverse
  effects:</strong> peripheral vasodilation &mdash; peripheral edema, dyspnea, wheezing and
  <mark class="prof-highlight">rebound tachycardia</mark>, the heart&rsquo;s reflex answer to an abrupt
  fall in resistance; gastrointestinal, central and skin effects; gynecomastia; gingival
  hyperplasia. <strong>Contraindications:</strong> <strong>severe aortic stenosis</strong>, and
  <strong>unstable angina or a recent myocardial infarction</strong> with the immediate-release
  form &mdash; avoid short-acting formulations. <strong>Interactions:</strong> amiodarone, digoxin
  and beta blockers pharmacodynamically; and CYP3A4 inhibitors lengthen their half-life.</p>

  <div class="pearl"><strong>The CYP3A4 asymmetry.</strong> Dihydropyridines are
  <em>substrates</em> of CYP3A4 but do not inhibit it; non-dihydropyridines are substrates
  <em>and</em> inhibitors. &ldquo;Another key difference.&rdquo; Only the non-dihydropyridine
  raises the statin.</div>

  <h3 class="sub" id="htn-bb">3.5 &middot; Objectives 1&ndash;8 &mdash; Beta blockers</h3>

  <p><strong>Mechanism:</strong> competitive block of cardiac beta-1 (lower cardiac output, an acute
  reflex rise in peripheral resistance, reduced exercise tolerance); of the beta-1 receptors that
  release renin (less angiotensin II); of presynaptic beta-2 (less norepinephrine release); and of
  pulmonary beta-2 (less bronchial relaxation, so bronchospasm in asthma); plus central reduction
  of sympathetic activity and an altered baroreflex. Blood pressure falls only
  <strong>chronically</strong>, once the baroreflex resets.</p>

  <table>
    <tr><th>Generation</th><th>Agents</th><th>What to know</th></tr>
    <tr><td>First &mdash; <strong>non-selective</strong></td><td>Nadolol, penbutolol, pindolol, <strong>propranolol</strong>, sotalol, timolol</td><td>Block beta-1 and beta-2. <mark class="prof-highlight">Propranolol: high lipid solubility</mark> &rarr; central effects</td></tr>
    <tr><td>Second &mdash; <strong>beta-1 selective</strong></td><td>Acebutolol, atenolol, bisoprolol, <strong>esmolol (intravenous)</strong>, metoprolol</td><td>Bronchospasm less likely</td></tr>
    <tr><td>Third &mdash; <strong>vasodilating</strong></td><td><strong>Carvedilol</strong>, <strong>labetalol</strong>; also carteolol and betaxolol (glaucoma)</td><td><mark class="prof-highlight">Carvedilol and labetalol: &alpha;1 blockade</mark> (labetalol also beta-2 agonism; carvedilol antioxidant and antiproliferative). Betaxolol is the beta-1 selective one</td></tr>
  </table>

  <p><strong>Indications.</strong> Hypertension &mdash; but <mark class="prof-highlight">not
  recommended for first line management of HTN</mark> (hypertension). The slide adds that they
  <strong>work best in young patients</strong> with resting tachycardia, high catecholamines and
  high renin, that fatigue and limited exercise are the common complaints, and that they are still
  useful in the elderly. Beyond hypertension: <strong>glaucoma</strong> (timolol, betaxolol,
  carteolol &mdash; less aqueous humor), <strong>migraine prophylaxis</strong> (propranolol,
  timolol), <strong>hyperthyroidism</strong> (less tachycardia, tremor and anxiety, and less
  peripheral conversion of T4 to T3), <strong>angina</strong> (longer exercise time),
  <strong>acute myocardial infarction</strong> (avoid agents with intrinsic sympathomimetic
  activity), <strong>supraventricular arrhythmias</strong> (atrioventricular nodal block),
  <strong>acute panic attacks</strong>, <strong>benign essential tremor</strong> (skeletal muscle
  beta-2), and <strong>heart failure</strong>.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">Heart failure: <strong>carvedilol, metoprolol succinate,
    bisoprolol</strong> &mdash; <em>&ldquo;just know these three.&rdquo;</em> Originally
    contraindicated; now they raise cardiac output and lower resistance and heart rate in a failing
    ventricle, but they <strong>initially worsen symptoms, so start with a very low dose and
    increase slowly</strong>.</p>
  </div>

  <table>
    <tr><th>Adverse effect</th><th>Detail</th></tr>
    <tr><td><strong>Bronchoconstriction</strong></td><td>Worsens asthma; bronchospasm in a third of patients with chronic obstructive pulmonary disease, where the class is contraindicated. <mark class="prof-highlight">Less likely with b1 selective agents</mark></td></tr>
    <tr><td>Cardiodepression</td><td>Negative inotropy (fatigue, heart failure); negative chronotropy (bradycardia under 60); first-, second- and third-degree heart block</td></tr>
    <tr><td><strong>Glucose</strong></td><td><mark class="prof-highlight">b-blockers inhibit glycogenolysis, prolong hypoglycemia, mask symptoms</mark> in type 1 diabetes; in type 2, less insulin, higher and harder-to-control glucose, and the same masked hypoglycemia</td></tr>
    <tr><td>Peripheral circulation</td><td>Vascular beta-2 block: cold extremities and Raynaud phenomenon, muscle fatigue, intermittent claudication in peripheral artery disease</td></tr>
    <tr><td><strong>Sudden withdrawal</strong></td><td><mark class="prof-highlight">Sudden withdrawal syndrome &mdash; acute angina, MI, marked &uarr;BP &mdash; slowly withdraw</mark>; the receptors have upregulated</td></tr>
    <tr><td>Central effects</td><td><mark class="prof-highlight">Highly lipid soluble agents &mdash; depression; nightmares, vivid dreams, hallucinations</mark>; fatigue</td></tr>
    <tr><td>Lipids</td><td>Elevated triglycerides</td></tr>
  </table>

  <p><strong>Interactions.</strong> Verapamil and diltiazem: synergistic falls in blood pressure,
  heart rate and contractility &mdash; use lower doses of each. <strong>Clonidine</strong>: the
  combination lowers blood pressure further, and <strong>abrupt clonidine withdrawal causes a
  severe rise in blood pressure</strong> (the slide&rsquo;s label of clonidine as an alpha-2
  &ldquo;blocker&rdquo; is a slip; it is an agonist, 3.7). Beta blockers also enhance
  prazosin&rsquo;s postural hypotension.</p>

  <h3 class="sub" id="htn-alpha">3.6 &middot; Objectives 1&ndash;8 &mdash; Alpha-1 blockers</h3>

  <p><strong>Mechanism:</strong> reversible block of vascular alpha-1 receptors, dilating
  precapillary arterioles and lowering peripheral resistance, with a reflex rise in heart rate.
  <strong>Prazosin (Minipress)</strong> is the prototype, used for hypertension with beta blockers
  and diuretics; it slightly lowers LDL (low-density lipoprotein) cholesterol and triglycerides and
  raises HDL (high-density lipoprotein). Its adverse effects: <strong>orthostatic hypotension</strong>
  and postural dizziness, headache, drowsiness, lack of energy; a <strong>mild</strong> reflex
  tachycardia; raised renin with sodium and water retention; impotence. Use with caution in cardiac
  and renal failure. <strong>NSAIDs attenuate its response; beta blockers may enhance the postural
  hypotension.</strong></p>

  <p><strong>Terazosin (Hytrin) and doxazosin (Cardura)</strong> have longer half-lives, so once
  daily, and treat hypertension and <strong>benign prostatic hyperplasia</strong>.
  <strong>Tamsulosin (Flomax)</strong> is <strong>alpha-1A selective</strong>: it treats benign
  prostatic hyperplasia with <strong>limited vascular effect</strong>, because vascular receptors
  are alpha-1B. Its adverse effects are hypotension, dizziness and diarrhea.</p>

  <h3 class="sub" id="htn-central">3.7 &middot; Objectives 1&ndash;8 &mdash; Central sympatholytics</h3>

  <p><strong>Mechanism:</strong> stimulation of postsynaptic <strong>alpha-2 (alpha-2A)
  receptors</strong>, and possibly imidazoline receptors, in the nucleus of the solitary tract and
  ventrolateral medulla, which lowers sympathetic outflow through the spinal cord and ganglia to the
  vessels and raises vagal output to the heart &mdash; so resistance, heart rate and cardiac output
  all fall. <strong>Advantages:</strong> efficacy independent of age, race and gender; suitable for
  monotherapy; work well in the elderly; <strong>no negative effects on lipids</strong>.
  <strong>Class side effects:</strong> drowsiness and sedation, dry mouth, sexual dysfunction, a
  <strong>narrow therapeutic range</strong>, and <mark class="prof-highlight">abrupt withdrawal
  hypertension</mark>.</p>

  <p><strong>Clonidine (Catapres)</strong> is an <strong>alpha-2 agonist and imidazoline
  agonist</strong>. It <strong>raises blood glucose by inhibiting insulin secretion</strong> and
  lowers antidiuretic hormone secretion. It causes <strong>sodium retention, so it is often given
  with a diuretic</strong>, plus dry mouth, sedation, orthostatic hypotension, impotence, bradycardia
  and <mark class="prof-highlight">withdrawal reactions (may be severe)</mark>. Beyond blood pressure
  it has <strong>analgesic activity and blunts opiate withdrawal reactions</strong>.
  <strong>Guanfacine (Tenex)</strong> is less potent, the <strong>most selective</strong> for alpha-2
  over alpha-1, <strong>less sedating</strong>, and only occasionally causes a withdrawal
  syndrome.</p>

  <div class="pearl"><strong>The &ldquo;do not stop abruptly&rdquo; pair.</strong> Beta blockers and
  clonidine are the two antihypertensives whose sudden withdrawal is dangerous &mdash; and they are
  often prescribed together, which is why their interaction is on the slide.</div>

  <h3 class="sub" id="htn-vaso">3.8 &middot; Objectives 1&ndash;7 &mdash; Direct vasodilators</h3>

  <p>They dilate arterioles directly and lower resistance, and the body fights back: reflex
  sympathetic activation brings tachycardia, higher cardiac output, fluid retention and more renin,
  which in turn produces <strong>tachyphylaxis</strong>. For chronic hypertension they are given with
  a diuretic and a beta blocker: <strong>hydralazine</strong>, and <strong>minoxidil as triple therapy
  for severe or refractory hypertension</strong>. <strong>Nitroprusside</strong>, by intravenous
  infusion, is for <strong>hypertensive crisis</strong>.</p>

  <table>
    <tr><th></th><th>Hydralazine</th><th>Minoxidil</th><th>Nitroprusside</th></tr>
    <tr><td>Veins</td><td>No</td><td>No</td><td><strong>Yes</strong> (veins and arterioles)</td></tr>
    <tr><td>Arterioles</td><td>Yes</td><td><strong>Most</strong></td><td>Yes</td></tr>
    <tr><td>Reflex tachycardia, sodium retention</td><td>Some</td><td><strong>Most</strong></td><td>Tachycardia some; sodium retention none</td></tr>
    <tr><td>Mechanism</td><td>Not clear &mdash; raised cyclic GMP (nitric oxide), renal prostaglandins, interference with calcium</td><td><strong>Opens ATP-modulated potassium channels</strong> &rarr; potassium efflux &rarr; hyperpolarization &rarr; relaxation</td><td>Releases <strong>nitric oxide</strong> (one nitric oxide and five cyanide groups on iron) &rarr; cyclic GMP &rarr; less intracellular calcium</td></tr>
  </table>

  <p><strong>Hydralazine (Apresoline)</strong> is <mark class="prof-highlight">N-acetylated in liver
  &mdash; fast and slow acetylators</mark>. Adverse effects: reflex rise in cardiac output and fluid
  volume; headache, dizziness, flushing; and a <mark class="prof-highlight">drug-induced &ldquo;lupus
  syndrome&rdquo; &mdash; high dose, long term, women, slow acetylators, Caucasians</mark>.
  <strong>Contraindicated in coronary artery disease, the elderly, and ischemia</strong>, because it
  adds sympathetic workload. Patient education: <mark class="prof-highlight">stools may turn
  black</mark> &mdash; warn ahead of time about any drug that changes stool or urine color.</p>

  <p><strong>Minoxidil (Loniten)</strong> has the harshest reflexes (cardiac output two to three
  times, renin stimulated), so <strong>myocardial ischemia</strong>; <strong>arrhythmias</strong>
  from its potassium channel action; and <strong>hypertrichosis</strong> of the face, back, arms and
  legs. Rogaine is the topical form for hair growth, and <strong>may have cardiovascular
  effects</strong>.</p>

  <p><strong>Nitroprusside (Nitropress)</strong> toxicity comes from its cyanide groups.
  <strong>Cyanide toxicity</strong> (trembling, vomiting, convulsions) is limited by giving
  <strong>sodium thiosulfate</strong>. <strong>Thiocyanate toxicity</strong> (weakness, anoxia,
  tinnitus, muscle spasms, toxic psychosis) follows <strong>long infusions or renal
  failure</strong>.</p>

  <h3 class="sub" id="htn-algo">3.9 &middot; Objectives 9&ndash;10 &mdash; The treatment algorithm, monitoring and patient education</h3>

  <p>Slide 108 is a picture of the management algorithm, and it is the deck&rsquo;s only protocol
  content. <strong>Every motivated patient gets lifestyle counseling first.</strong> Then:</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <ol>
      <li><strong>Systolic more than 20 mmHg, or diastolic more than 10 mmHg, above goal?</strong>
      &rarr; <mark class="prof-highlight">Initiate an ACE inhibitor (or ARB) plus a dihydropyridine
      calcium channel blocker</mark> (ARB = angiotensin receptor blocker). Uncontrolled &rarr;
      <mark class="prof-highlight">add a thiazide-like diuretic</mark>.</li>
      <li>Not that far above goal, with <strong>urine albumin-to-creatinine ratio 300 mg/g or
      more</strong> &rarr; <mark class="prof-highlight">initiate an ACE inhibitor (or ARB)</mark>.</li>
      <li>Otherwise &rarr; an ACE inhibitor (or angiotensin receptor blocker) <strong>or</strong> a
      dihydropyridine calcium channel blocker.</li>
      <li>Still uncontrolled &rarr; combine an ACE inhibitor (or angiotensin receptor blocker)
      <strong>with</strong> a dihydropyridine &rarr; then add a thiazide-like diuretic &rarr; then
      &ldquo;apparent resistant hypertension&rdquo;.</li>
    </ol>
    <p>Note the <strong>or</strong>: an ACE inhibitor <em>or</em> an angiotensin receptor blocker,
    never both together. He caught himself saying &ldquo;ACEs and ARBs&rdquo; and corrected it.</p>
  </div>

  <p><strong>Reasons to reach for another class earlier</strong> (inset 1): a <strong>beta
  blocker</strong> should generally be used first after a <strong>myocardial infarction</strong>,
  and beta blockers are among the first drugs in heart failure with reduced ejection fraction. (The
  diuretic, mineralocorticoid-antagonist and heart-failure indications on the same inset belong to
  Lecture 9.) Beta blockers, non-dihydropyridines and alpha blockers are otherwise for these
  compelling indications, not first line.</p>

  <div class="pearl"><strong>Monitoring</strong> (inset 2): <strong>reassess blood pressure about
  4 weeks</strong> after starting or titrating; one or two titration steps before changing or adding
  a drug, because pushing a drug to its maximum adds adverse effects for diminishing benefit. When
  therapy seems to fail, the commonest causes are <strong>(1) medication nonadherence, (2) the white
  coat effect, (3) improper blood pressure measurement</strong>.</div>

  <table>
    <tr><th>Class or drug</th><th>Patient education the slides support</th></tr>
    <tr><td>ACE inhibitors</td><td>A dry cough may appear weeks to months in &mdash; report it; report swelling of the lips, tongue or throat at once (angioedema, usually in the first week); no potassium supplements or salt substitutes; not in pregnancy (2nd and 3rd trimesters)</td></tr>
    <tr><td>Angiotensin receptor blockers</td><td>Same potassium and pregnancy warnings; no cough</td></tr>
    <tr><td>Calcium channel blockers</td><td>Peripheral edema, flushing, headache; constipation; gum overgrowth (gingival hyperplasia)</td></tr>
    <tr><td>Beta blockers</td><td><strong>Never stop suddenly</strong>; in diabetes the warning signs of low blood sugar may be hidden; fatigue and reduced exercise tolerance</td></tr>
    <tr><td>Alpha-1 blockers</td><td>Dizziness on standing</td></tr>
    <tr><td>Clonidine</td><td><strong>Never stop suddenly</strong>; drowsiness and dry mouth</td></tr>
    <tr><td>Hydralazine</td><td>Stools may turn black</td></tr>
    <tr><td>Minoxidil</td><td>Unwanted hair growth</td></tr>
  </table>

</section>
'''
