# -*- coding: utf-8 -*-
"""Pharmacology I Exam 2 study guide -- section 5, Lecture 8 (Myocardial Ischemia).

Imported by build_pharm_e2_guide.py.

SOURCES
  Facts   "Myocardial Ischemia Drugs.pptx" (69 slides; Adam Wood, Pharm.D.,
          DABAT). `python3 tools/pharm_e2_lib.py dump L8` prints the slide text;
          the picture-only slides (5, 15, 16, 20, 21, 25, 26, 34, 41-50, 67 and
          the picture captions on 27 and 31) were read by eye and live in
          tools/pharm_e2/ocr.json under "L8". Slide numbers in square brackets
          in the body are that deck's slide numbers.
  Weight  Dr. Wood's recording, 40 checked quotes in tools/pharm_e2/wood.json
          (lec "L8"): the scope callout near the top and the prof-flag stars in
          each subsection come from it. Stars only set weight; no fact was added.

NO DOSES. Left out on purpose (Dr. Wood: doses are not tested): the aspirin
milligram amount on slide 52, the nitroglycerin ointment amount per inch and
strength per inch on slide 31. Durations, routes, schedules and thresholds stay
(12 hours on and 12 off, 3 to 6 months after opening, heart rate below 60).

TRUTH WINS ON CONFLICT (standing rule). Every place the deck is wrong, old or
over-simple has a short "Deck versus truth" callout saying what the slide says
and what is true: slide 13 (antiplatelets "increase coronary flow"), slide 15
(grade I), slide 23 (atrioventricular block unqualified), slide 34 (two contested
cells), slide 55 (intravenous then oral), slide 58 (factor list), slides 61 and 64
(fibrin affinity of reteplase), slide 62 (urokinase), slide 63 (old numbers),
slide 65 (numbers). The contested cells and the wrong ones are NOT to be keyed.

SLIDES NOT COVERED: 1 (title), 2 (the deck's own objectives slide; the syllabus
wording is used instead), 3, 40 and 69 (section dividers and "Questions?"). Every
other slide carries teaching content and is represented below.
"""

TOC = '''  <a class="top-link" href="#mi">5 &middot; Myocardial Ischemia Drug Therapy</a>
  <a href="#mi-frame">5.1 Objectives 1&ndash;3 &mdash; Angina, and the oxygen supply-and-demand frame</a>
  <a href="#mi-bb">5.2 Objectives 1&ndash;7 &mdash; Beta blockers</a>
  <a href="#mi-ccb">5.3 Objectives 1&ndash;7 &mdash; Calcium channel blockers</a>
  <a href="#mi-nitrates">5.4 Objectives 1&ndash;7 &mdash; Nitrates</a>
  <a href="#mi-addon">5.5 Objectives 1&ndash;3 and 7 &mdash; Add-on therapy, comorbid conditions and variant angina</a>
  <a href="#mi-acs">5.6 Objectives 1&ndash;3 &mdash; Acute coronary syndrome and thrombus formation</a>
  <a href="#mi-acs-drugs">5.7 Objectives 1&ndash;7 &mdash; Acute coronary syndrome: aspirin, nitrates, beta blockers, morphine</a>
  <a href="#mi-lytics">5.8 Objectives 1&ndash;7 &mdash; Fibrinolytics and other antithrombotic drugs</a>
  <a href="#mi-monitor">5.9 Objectives 8&ndash;10 &mdash; Interactions, monitoring and patient education</a>'''

BODY = '''
<section class="deck" id="mi">
  <h2 class="deck-title">5 &middot; Myocardial Ischemia Drug Therapy</h2>
  <p class="lecturer">Adam Wood, Pharm.D., DABAT</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol>
      <li>Identify drug classes and commonly prescribed drugs used to treat myocardial ischemia.</li>
      <li>Describe the molecular mechanism of action of drugs used to treat myocardial ischemia.</li>
      <li>Identify indications for drugs used to treat myocardial ischemia.</li>
      <li>Describe absorption, distribution, metabolism, and excretion of drugs used to treat myocardial ischemia.</li>
      <li>Summarize side effects and toxic manifestations of drugs used to treat myocardial ischemia.</li>
      <li>Describe adverse effects of drugs used to treat myocardial ischemia.</li>
      <li>Identify contraindications for drugs used to treat myocardial ischemia.</li>
      <li>Discuss potential drug-drug, drug-food, and drug-herb interactions with drugs used to treat myocardial ischemia.</li>
      <li>List commonly used protocols and patient monitoring for myocardial ischemia drug therapy.</li>
      <li>Outline appropriate patient education for drugs used to treat myocardial ischemia.</li>
    </ol>
  </div>

  <div class="callout"><strong>What he said is not examined, or not in depth.</strong>
  <ul>
    <li><strong>Where the exam ends.</strong> &ldquo;The end of the testable material for the exam for Monday ends with this PowerPoint, and then we&rsquo;ll get started on the first PowerPoint for the third exam right after.&rdquo; (at 0:24). Myocardial ischemia is the last testable lecture of Exam 2; the diuretics and heart failure deck that follows in the same recording belongs to the next exam.</li>
    <li><strong>Which cell line makes which fibrinolytic</strong> &mdash; &ldquo;I don&rsquo;t care that you know the difference between which one&rsquo;s made with E. coli versus hamster cells.&rdquo; (at 1:02:02). The hamster ovary cells against <em>Escherichia coli</em> detail on slide 64 steps back.</li>
    <li><strong>Streptokinase the drug</strong> &mdash; &ldquo;Streptokinase, kind of an older one we&rsquo;ve used in the past, I don&rsquo;t want you to worry so much about that, but I do want to focus on this picture here&hellip; plasminogen coming in with streptokinase to form a complex&hellip; a tissue plasminogen activator, which is what we naturally produce, could do this as well.&rdquo; (at 58:27). What he does want known is the <strong>picture</strong> on slides 59 and 60: plasminogen is converted to plasmin, by a streptokinase complex or by tissue plasminogen activator.</li>
    <li><strong>Doses.</strong> This site leaves milligram amounts out (doses are not tested in this course, per the earlier lectures); he quoted the aspirin loading amount in this lecture without saying whether it is examined. The left-out box below lists what the deck gives and this guide omits.</li>
  </ul>
  What he does stress is a list of stem shapes, marked with a star in the sections below: <em>&ldquo;some things are for prophylaxis and some things for acute treatment&rdquo;</em> (prevention against quick relief), the order of use (what to add next, what to switch to), and the antianginal-by-comorbidity table, which he called <em>&ldquo;a cornucopia of test questions&rdquo;</em>.</div>

  <div class="callout"><strong>What is left out of this section, and why.</strong>
  <ul>
    <li><strong>Milligram doses.</strong> Doses are not tested in this course. The aspirin milligram
    amount on slide 52 and the nitroglycerin ointment amount per inch on slide 31 are not reproduced.
    Timings, durations, routes and schedules are kept, for example the 12 hours on and 12 hours off
    nitrate schedule.</li>
    <li><strong>Trial and registry percentages.</strong> Slide 52 says beta blockers cut the risk of
    myocardial infarction by 13 percent in unstable angina and cut deaths by 40 percent after a
    myocardial infarction. Slide 37 says aspirin cuts the risk of primary events by about 30 percent.
    Slide 65 gives bleeding of 0.5 to 7 percent and intracranial hemorrhage of 0.4 to 0.94 percent with
    fibrinolytics. These are stated here for completeness; learn the direction of each finding, not
    the number.</li>
    <li><strong>Older cut-offs.</strong> The numbers on the fibrinolytic contraindication slide (10 days,
    3 months, a diastolic pressure above 110) and on the fibrinolytic indication slide (under 75 years,
    within 12 hours) come from an older source; learn the categories they stand for.</li>
    <li><strong>Where the deck is wrong or out of date,</strong> the guide says so in a box headed
    &ldquo;Deck versus truth&rdquo; and follows the truth. Those points are not to be memorized as the
    slide words them.</li>
  </ul></div>

  <h3 class="sub" id="mi-frame">5.1 &middot; Objectives 1&ndash;3 &mdash; Angina, and the oxygen supply-and-demand frame</h3>

  <p><strong>Ischemic heart disease</strong> is an imbalance between the oxygen supply and the oxygen
  demand of the heart muscle [slide 4]. Less blood flow to the tissue means a lack of oxygen supply
  [slide 4]. <strong>Coronary heart disease</strong> is atherosclerotic narrowing of one or more
  coronary arteries [slide 4]. <strong>Angina pectoris</strong> is the clinical manifestation of
  myocardial ischemia: chest pain [slide 4]. <strong>Chronic stable angina</strong> is listed as the chronic
  counterpart of acute coronary syndrome [slide 4]. <strong>Acute coronary syndrome</strong> groups unstable angina, acute myocardial
  infarction and sudden cardiac death [slide 4].</p>

  <p>Angina is a late, symptomatic manifestation of ischemia that may occur with any degree of
  stenosis [slide 7]. (Slide 7 calls it &ldquo;latent&rdquo;; angina is the symptomatic phase, not a hidden one.) A narrowing of <strong>50 percent of the left main coronary artery, or 75 percent
  of another major coronary artery,</strong> is considered clinically significant [slide 7]. A stenosis
  above 90 percent severely limits flow (the slide says &ldquo;virtually no flow&rdquo;), so ischemia can occur
  even at low demand [slide 7].</p>

  <h4 class="subsub">The two sides of the balance [slides 5 and 6]</h4>
  <table>
    <tr><th>Side</th><th>What sets it</th></tr>
    <tr><td><strong>Oxygen supply (availability)</strong></td><td>Arterial partial pressure of oxygen and hemoglobin concentration; coronary flow and its distribution; oxygen extraction and the coronary microcirculation [slide 5]</td></tr>
    <tr><td><strong>Oxygen demand (requirement)</strong></td><td>Heart rate; contractility; and <strong>systolic (intramyocardial) wall tension</strong> [slides 5 and 6]</td></tr>
  </table>

  <p><strong>Wall tension</strong> is the tension in the heart wall [slide 6]. It is affected by ventricular
  volume and pressure and is a function of preload and afterload [slide 6]. <strong>Preload</strong> is the
  initial stretching of the cardiac muscle cells before contraction; it tracks ventricular and diastolic
  volume [slide 6]. <strong>Afterload</strong> is the pressure the heart must eject blood against; it tracks
  systemic vascular resistance [slide 6].</p>

  <div class="callout"><strong>Memory aid &mdash; the heart&rsquo;s oxygen budget.</strong> <em>A story to
  hang the slide facts on. When a question asks for a fact, answer from the facts in this section, not
  from the story.</em>
  <ul>
    <li><strong>Supply is the income</strong>: the oxygen that the coronary arteries deliver. A coronary
    stenosis caps the income, and a stenosis above 90 percent severely limits it [slide 7].</li>
    <li><strong>Demand is the spending</strong>: heart rate, contractility and wall tension [slide 6].
    Exercise raises the spending; angina is the overdraft warning, chest pain when spending outruns income.</li>
    <li><strong>Beta blockers cut spending only</strong>: they slow the rate and soften the contraction and
    have no effect on supply [slide 16].</li>
    <li><strong>Calcium channel blockers cut spending and raise income a little</strong>: mild dilation
    where the stenosis is fixed and relief of spasm [slide 20].</li>
    <li><strong>Nitrates cut spending and raise income</strong>: they lower wall tension, dilate the coronary
    arteries and relieve spasm [slide 25].</li>
    <li><strong>Aspirin, clopidogrel and statins protect the income source</strong> from being blocked by a
    clot or a ruptured plaque [slides 11, 12 and 37].</li>
  </ul>
  <strong>Where it breaks:</strong> it does not explain tachyphylaxis (loss of nitrate effect), it says nothing
  about acute coronary syndrome, and it makes antiplatelet drugs sound like direct blood flow raisers, which
  they are not (see the box below).</div>

  <h4 class="subsub">Risk factors, goals and strategy [slides 9 to 11]</h4>
  <table>
    <tr><th>Topic</th><th>What the slide lists</th></tr>
    <tr><td>Non-modifiable risk factors</td><td>Family history of a premature cardiovascular event; age above 45 years in males and above 55 years in females [slide 9]</td></tr>
    <tr><td>Modifiable risk factors</td><td>Sedentary lifestyle, diabetes, tobacco use, being overweight, hypertension and dyslipidemia [slide 9]</td></tr>
    <tr><td>Treatment goals</td><td>Increase quantity of life by preventing acute coronary syndromes; increase quality of life by relieving and preventing symptoms [slide 10]</td></tr>
    <tr><td>Lower oxygen demand</td><td>Decrease heart rate; decrease contractility; decrease intramyocardial wall tension by decreasing preload and afterload [slide 11]</td></tr>
    <tr><td>Raise oxygen supply</td><td>Improve coronary blood flow [slide 11]</td></tr>
    <tr><td>Other strategy</td><td>Stabilize atherosclerotic plaques to prevent acute coronary syndrome; modify reversible risk factors [slide 11]</td></tr>
  </table>

  <h4 class="subsub">The three treatment arms and the drug classes (Objective 1) [slides 12 to 14]</h4>
  <table>
    <tr><th>Arm</th><th>What it includes</th></tr>
    <tr><td>Revascularization</td><td>Percutaneous coronary intervention; coronary artery bypass grafting [slide 12]</td></tr>
    <tr><td>Drug therapy: antianginals</td><td><strong>Beta blockers, calcium channel blockers and nitrates</strong> [slides 12 and 14]</td></tr>
    <tr><td>Drug therapy: vasculoprotective</td><td>Antiplatelet drugs, statins and angiotensin-converting enzyme inhibitors [slide 12]. Aspirin is used in ischemic heart disease to prevent acute coronary syndromes [slide 37]</td></tr>
    <tr><td>Lifestyle</td><td>Change the modifiable risk factors [slide 12]</td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 9:15 of the recording: <em>&ldquo;I will reiterate and reiterate and reiterate that some things are for prophylaxis and some things for acute treatment&hellip; I may say a test question, which one of these is best suited for quick relief of symptoms, which would be one class of medications, and then if I were to say which one of these are good for prevention of symptoms, that&rsquo;s a totally different set of class events.&rdquo;</em></p>
    <p><strong>Prevention:</strong> beta blockers, calcium channel blockers and long-acting nitrates. <strong>Quick relief of an attack:</strong> short-acting (sublingual) nitroglycerin. Expect a stem that asks for one and offers the other [slides 12, 14, 27 and 29].</p>
  </div>

  <p><strong>Prevention of anginal attacks:</strong> metoprolol and other beta blockers, calcium channel blockers and long-acting nitrates are taken to prevent attacks; they are not rescue drugs. <strong>Rescue for an attack:</strong> sublingual nitroglycerin [slides 12, 14, 27 and 29].</p>

  <p>The <strong>antianginal</strong> drugs improve exercise capacity, reduce exercise-induced
  ST-segment changes and decrease the frequency of symptoms [slide 14]. Of the three antianginal classes, <strong>nitrates lower oxygen demand mainly by reducing left ventricular volume</strong>, which lowers wall tension [slides 6 and 25]. The calcium channel blockers
  come in two subclasses, <strong>dihydropyridine</strong> and <strong>non-dihydropyridine</strong>
  [slide 14]. The slide-13 overview groups the drugs by effect: <strong>calcium channel blockers, nitrates
  and beta blockers</strong> decrease heart rate, contractility and systolic wall tension; calcium channel
  blockers, nitrates, aspirin and clopidogrel are listed under increasing coronary blood flow [slide 13].</p>

  <div class="callout"><strong>Deck versus truth &mdash; antiplatelet drugs and blood flow.</strong> Slide 13
  lists aspirin and clopidogrel as drugs that increase coronary blood flow. They do not dilate the coronary
  arteries; they prevent a platelet clot from blocking the flow, so they protect supply rather than raise it.
  Learn them as vasculoprotective, as slide 12 has them. Slide 13 also lumps nitrates and calcium channel
  blockers with the drugs that lower heart rate. The hemodynamic table (slides 16, 20 and 25) is the accurate
  one: nitrates and the dihydropyridines raise the heart rate, and the fall in heart rate belongs to beta
  blockers and non-dihydropyridines.</div>

  <h4 class="subsub">Grades of angina [slide 15]</h4>
  <table>
    <tr><th>Class</th><th>Limitation of physical activity</th><th>When symptoms occur</th><th>At rest</th></tr>
    <tr><td><strong>I</strong></td><td>None</td><td>None with physical activity</td><td>Comfortable</td></tr>
    <tr><td><strong>II</strong></td><td>Slight</td><td>With greater than ordinary activities</td><td>Comfortable</td></tr>
    <tr><td><strong>III</strong></td><td>Marked</td><td>With ordinary activities</td><td>Comfortable</td></tr>
    <tr><td><strong>IV</strong></td><td>Any activity increases symptoms</td><td>At less than ordinary levels of activity</td><td>May or may not be symptomatic at rest</td></tr>
  </table>
  <p>The higher the class, the less activity it takes to bring on symptoms. Only class IV may cause symptoms at rest
  [slide 15]. (The usual grading describes class I as angina only with strenuous exertion; the slide&rsquo;s
  &ldquo;none&rdquo; means none with ordinary activity.)</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 14:48 of the recording: <em>&ldquo;How you grade angina is basically off of the degree of physical activity limitation&hellip; can you do more stuff before you start to have chest pain, that&rsquo;s how we&rsquo;re really going to determine how well our therapy is working.&rdquo;</em></p>
    <p>Angina is graded by <mark class="prof-highlight">how much activity the patient can do</mark> before symptoms [slide 15], and the same measure, exercise capacity, shows whether an antianginal is working [slide 14].</p>
  </div>

  <p><strong>Chronic stable angina</strong> is the chronic form of angina, and it is graded I to IV by how much activity brings on the symptoms; in classes I to III the patient is comfortable at rest [slides 4 and 15]. Read together with slide 41, unstable angina belongs to acute coronary syndrome, and a biochemical marker is what separates unstable angina from myocardial infarction, so a long-standing, unchanged exertional pattern with normal biomarkers is chronic stable angina rather than acute coronary syndrome.</p>

  <div class="pearl"><strong>Variant angina, stated once here and treated in 5.5.</strong> Vasospastic or variant
  (Prinzmetal) angina can occur at the site of a partly occluded lesion and causes a transient, abrupt
  reduction in vessel diameter [slide 8]. It may be due to autonomic control [slide 8]. It occurs in
  <strong>younger patients and those with fewer risk factors</strong> [slide 8]. The electrocardiogram may or may
  not show ST-segment elevation [slide 8]. It often occurs <strong>during the night or early morning hours</strong>
  [slide 8].</div>

  <h3 class="sub" id="mi-bb">5.2 &middot; Objectives 1&ndash;7 &mdash; Beta blockers</h3>

  <p><strong>Beta blockers are first line therapy for angina in the absence of contraindications</strong>
  [slide 17]. They are useful in patients with limited exercise capacity due to angina, and in patients who also
  have hypertension, anxiety, supraventricular arrhythmias, heart failure (stable, compensated; see below), or a prior myocardial infarction
  [slide 17].</p>

  <table>
    <tr><th>Group</th><th>Agents the slide names</th></tr>
    <tr><td>Beta-1 selective</td><td><strong>Metoprolol, atenolol</strong> [slide 17]</td></tr>
    <tr><td>Non-selective</td><td><strong>Propranolol, nadolol</strong> [slide 17]</td></tr>
    <tr><td>Third generation</td><td><strong>Carvedilol, labetalol</strong> [slide 17]</td></tr>
  </table>
  <p>Either beta-1 selective or non-selective agents may be used [slide 17]. <strong>Metoprolol and atenolol are the beta-1 selective beta blockers</strong> [slide 17]. Propranolol and nadolol are non-selective beta blockers [slide 17], and <strong>non-selective (non-cardioselective) beta blockers are avoided in asthma</strong>; cardioselective beta blockers and non-dihydropyridine calcium channel blockers remain options there [slide 34].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 17:44 of the recording: <em>&ldquo;Remember the rule we used was A through M &hellip; beta-1 selective. N through Z typically are considered the non-selective agents, and then we&rsquo;ll just need to know our exception with the third gen, that&rsquo;s carvedilol and labetalol.&rdquo;</em></p>
    <p>Selective: <mark class="prof-highlight">metoprolol, atenolol</mark> (A through M). Non-selective: <mark class="prof-highlight">propranolol, nadolol</mark> (N through Z). Third generation, the exception to the alphabet rule: <mark class="prof-highlight">carvedilol, labetalol</mark> [slide 17].</p>
  </div>

  <p><strong>Mechanism (Objective 2).</strong> Beta blockers act on the <strong>demand</strong> side only. They
  decrease heart rate and contractility and lower systolic blood pressure, and they have <strong>no effect on
  oxygen supply</strong> [slide 16]. Their effect on left ventricular volume is an <em>increase</em>
  [slide 16]. The receptor-level mechanism is taught with the antihypertensives (section 3.5); here only the
  hemodynamic result is on the slides.</p>

  <table>
    <tr><th>Drug class</th><th>Heart rate</th><th>Contractility</th><th>Systolic blood pressure</th><th>Left ventricular volume</th></tr>
    <tr><td><strong>Beta blockers</strong></td><td>Decreased (strongly)</td><td>Decreased</td><td>Decreased</td><td>Increased</td></tr>
    <tr><td><strong>Dihydropyridine calcium channel blockers</strong></td><td>Increased</td><td>Unchanged or decreased</td><td>Decreased (strongly)</td><td>Unchanged or decreased</td></tr>
    <tr><td><strong>Non-dihydropyridine calcium channel blockers</strong></td><td>Decreased</td><td>Decreased</td><td>Decreased</td><td>Unchanged or decreased</td></tr>
    <tr><td><strong>Nitrates</strong></td><td>Increased</td><td>No effect listed</td><td>Decreased</td><td>Decreased (strongly)</td></tr>
  </table>
  <p>This table is the deck&rsquo;s hemodynamic summary of all three antianginal classes [slides 16, 20 and 25].
  Read it across: beta blockers and non-dihydropyridines slow the heart, while the dihydropyridines as a class and
  nitrates raise the rate.</p>

  <table>
    <tr><th>Objective</th><th>What the slides give for beta blockers</th></tr>
    <tr><td><strong>3 &middot; Indications</strong></td><td>First line for angina; helpful when hypertension, anxiety, supraventricular arrhythmias, heart failure (stable, compensated; see below) or a prior myocardial infarction is also present [slide 17]. Give a beta blocker after a prior myocardial infarction unless contraindicated [slide 38]</td></tr>
    <tr><td><strong>7 &middot; Contraindications</strong></td><td><strong>Heart rate below 60 beats per minute; systolic blood pressure below 100 mmHg; atrioventricular block; acute decompensated heart failure</strong> [slide 18]</td></tr>
    <tr><td><strong>7 &middot; Precautions</strong></td><td><strong>Reactive airway disease; systolic heart failure; diabetes; peripheral vascular disease</strong> [slide 18]</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Side effects and adverse effects</strong></td><td>Hypotension, bradycardia, hyperglycemia and dyslipidemia; fatigue, sexual dysfunction, nightmares and worsened claudication [slide 19]</td></tr>
    <tr><td><strong>4 &middot; Absorption, distribution, metabolism, excretion</strong></td><td>The slides give none for beta blockers in this lecture</td></tr>
  </table>
  <p><strong>Beta blockers may worsen claudication</strong> (leg pain with walking); worsened claudication is a listed beta blocker adverse reaction, and peripheral vascular disease is a listed precaution [slides 18 and 19]; read together, they suggest that claudication is the reason for the precaution. Beta blockers as a class, including non-selective agents such as nadolol and propranolol, can cause fatigue, sexual dysfunction, nightmares and worsened claudication [slides 17 and 19].</p>
  <p><strong>Hypotension is listed for all three antianginal classes</strong>: beta blockers [slide 19], calcium channel blockers [slide 24] and nitrates, as postural hypotension [slide 31]. All three lower systolic blood pressure [slides 16, 20 and 25].</p>
  <p>Two entries that look alike are the ones to keep apart: <strong>systolic heart
  failure is a precaution, acute decompensated heart failure is a contraindication</strong> [slide 18]. Slide 17
  lists heart failure among the conditions a beta blocker helps. Read together, slides 17 and 18 imply that
  the line is between stable and acutely decompensated failure.</p>
  <p><strong>Monitoring</strong> is of heart rate, blood sugar and lipids [slide 19].
  <strong>Education:</strong> avoid rapid discontinuation; expect dizziness and fatigue [slide 19]. The reason to
  avoid stopping suddenly is given with the antihypertensive beta blockers (section 3.5): abrupt withdrawal can
  cause angina, myocardial infarction and high blood pressure. That reason is not on this lecture&rsquo;s slides.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 19:55 of the recording: <em>&ldquo;We recommend against immediate discontinuation, so don&rsquo;t quit cold turkey&hellip; even MIs have been induced because of the rapid discontinuation of beta blockers.&rdquo;</em></p>
    <p>Beta blocker education: <mark class="prof-highlight">avoid rapid discontinuation</mark> [slide 19]. He tied it to rebound angina and even myocardial infarction.</p>
  </div>

  <h3 class="sub" id="mi-ccb">5.3 &middot; Objectives 1&ndash;7 &mdash; Calcium channel blockers</h3>

  <p><strong>Mechanism (Objective 2).</strong> Calcium channel blockers lower oxygen demand and raise supply
  [slide 20]. On the <strong>supply</strong> side they give <strong>mild dilation in areas of fixed stenosis and
  relief of vasospasm</strong> [slide 20]. On the demand side the two subclasses differ, as the hemodynamic table
  in 5.2 shows: non-dihydropyridines slow the heart rate and weaken contraction; dihydropyridines lower systolic
  blood pressure strongly and raise the heart rate [slide 20].</p>

  <table>
    <tr><th>Subclass and agent</th><th>Vasodilation</th><th>Contractility</th><th>Heart rate</th><th>Atrioventricular conduction</th></tr>
    <tr><td><strong>Non-dihydropyridine: diltiazem</strong></td><td>++ (less)</td><td>Decreased (strongly)</td><td>Decreased</td><td>Decreased</td></tr>
    <tr><td><strong>Non-dihydropyridine: verapamil</strong></td><td>++ (less)</td><td>Decreased (strongly)</td><td>Decreased</td><td>Decreased (strongly)</td></tr>
    <tr><td><strong>Dihydropyridine: nifedipine</strong></td><td>++++ (most)</td><td>Decreased</td><td>Increased</td><td>Unchanged</td></tr>
    <tr><td><strong>Dihydropyridine: amlodipine</strong></td><td>++++ (most)</td><td>Unchanged or decreased</td><td>Unchanged</td><td>Unchanged</td></tr>
    <tr><td><strong>Dihydropyridine: felodipine</strong></td><td>++++ (most)</td><td>Unchanged or decreased</td><td>Increased</td><td>Unchanged</td></tr>
  </table>
  <p>This is the deck&rsquo;s calcium channel blocker table [slide 21]. The simple split: the
  <strong>non-dihydropyridines (diltiazem, verapamil) act on the heart</strong> &mdash; rate, contractility and
  atrioventricular conduction &mdash; while the <strong>dihydropyridines (nifedipine, amlodipine, felodipine)
  act on the vessels</strong>, with the most vasodilation and no change in atrioventricular conduction. On slide 21
  diltiazem and verapamil both decrease contractility strongly; verapamil has the larger effect on
  atrioventricular conduction. Among the dihydropyridines, nifedipine
  and felodipine raise the heart rate while amlodipine leaves it unchanged [slide 21].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 21:02 of the recording: <em>&ldquo;Here I want you to notice the major difference between the dihydropyridines and the non-dihydropyridine calcium channel blockers&hellip; if a patient could not get a beta blocker for one reason or another, you can basically sub that out for a non-DHP.&rdquo;</em></p>
    <p>The <mark class="prof-highlight">non-dihydropyridines (verapamil, diltiazem)</mark> act like a beta blocker on heart rate and contractility, so they are the substitute when a beta blocker cannot be used; the dihydropyridines (the -dipines) act on the vessels [slides 21 and 22].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 25:16 of the recording: <em>&ldquo;If I told you a patient was coming in, they were started on a beta blocker for anginal symptoms and they are complaining they just can&rsquo;t tolerate it, they complain about having horrible nightmares, what would you want to switch to? That could be a situation which you can switch out for a non-DHP calcium channel blocker.&rdquo;</em></p>
    <p>A patient started on a beta blocker for angina who cannot tolerate it because of nightmares (one of the listed adverse reactions [slide 19]) is switched to a <mark class="prof-highlight">non-dihydropyridine calcium channel blocker</mark> [slide 22].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 22:35 of the recording: <em>&ldquo;For your typical anginal cases you would not want to use a DHP med by itself because of that increase in heart rate, you&rsquo;re kind of fighting yourself&hellip; you wouldn&rsquo;t really want to do a beta blocker plus a non-DHP because they&rsquo;re just doing the same thing&hellip; bradycardia, heart block, it&rsquo;s just more likely to occur.&rdquo;</em></p>
    <p><mark class="prof-highlight">Nifedipine and felodipine alone raise the heart rate</mark> (amlodipine leaves it unchanged, slide 21), so a dihydropyridine is added to a beta blocker, which blunts that rise [slide 22]. <mark class="prof-highlight">A beta blocker plus verapamil or diltiazem is avoided</mark> in most cases because of added bradycardia and heart block [slide 23].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 27:01 of the recording: <em>&ldquo;Keep in mind the LV dysfunction is going to be suppressed or is worsened with the use of a non-DHP calcium channel blocker, so the way I highlight here is DHPs only for that.&rdquo;</em></p>
    <p>Reduced left ventricular function is a contraindication for the non-dihydropyridines; <mark class="prof-highlight">dihydropyridines only</mark> [slides 22 and 23], and amlodipine is the one named [slide 34].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 27:19 of the recording: <em>&ldquo;Typically we avoid short-acting agents, agents like nifedipine, so if you can stick with something long-acting like amlodipine&hellip; you&rsquo;re not going to get that yo-yo type of effect.&rdquo;</em></p>
    <p><mark class="prof-highlight">Avoid short-acting agents such as nifedipine</mark> [slide 22]; a long-acting dihydropyridine such as amlodipine is the pattern to know.</p>
  </div>

  <h4 class="subsub">Place in therapy and drug choice [slide 22]</h4>
  <table>
    <tr><th>Question</th><th>Answer</th></tr>
    <tr><td>First choice when beta blockers are contraindicated or not tolerated</td><td>A <strong>non-dihydropyridine</strong>, as initial therapy to reduce symptoms</td></tr>
    <tr><td>Added to a beta blocker when the beta blocker alone fails</td><td>A <strong>dihydropyridine</strong></td></tr>
    <tr><td>Other pairing</td><td>In combination with long-acting nitrates</td></tr>
    <tr><td>Populations where a calcium channel blocker suits</td><td>Contraindication or intolerance to beta blockers; vasospastic angina; severe peripheral vascular disease; asthma; uncontrolled diabetes; left ventricular dysfunction (dihydropyridines only)</td></tr>
    <tr><td>Agents to avoid</td><td><strong>Short-acting agents, for example short-acting nifedipine</strong></td></tr>
  </table>
  <p><strong>The switch when a beta blocker is not tolerated:</strong> a patient who cannot tolerate a beta blocker (for example because of nightmares and fatigue) and has no contraindication is switched to a non-dihydropyridine calcium channel blocker such as diltiazem or verapamil, the initial substitute [slides 19 and 22].</p>
  <p>The slide gives no reason for avoiding short-acting nifedipine, only the instruction to avoid short-acting agents.</p>

  <table>
    <tr><th>Objective</th><th>What the slides give for calcium channel blockers</th></tr>
    <tr><td><strong>7 &middot; Contraindications</strong></td><td><strong>Systolic blood pressure below 100 mmHg; heart rate below 60 beats per minute (non-dihydropyridines); acute heart failure (non-dihydropyridines); ejection fraction below 40 percent (non-dihydropyridines); atrioventricular block</strong> [slide 23]</td></tr>
    <tr><td><strong>7 &middot; Precautions</strong></td><td>Concurrent beta blocker use (non-dihydropyridines); CYP3A4 (cytochrome P450 3A4) interactions [slide 23]</td></tr>
    <tr><td><strong>5&ndash;6 &middot; Side effects and adverse effects</strong></td><td>Hypotension; with dihydropyridines, <strong>headache, flushing and peripheral edema</strong> [slide 24]</td></tr>
    <tr><td><strong>4 &middot; Metabolism</strong></td><td>The slide names CYP3A4 interactions as a precaution, no other pharmacokinetics are given [slide 23]</td></tr>
  </table>

  <p>Calcium channel blockers <strong>improve myocardial oxygen supply</strong> by <strong>relief of coronary vasospasm</strong> and by mild dilation in areas of fixed stenosis, and they also lower demand [slide 20]. <strong>Headache, flushing and peripheral edema (ankle swelling) are the typical effects of a dihydropyridine</strong> [slide 24]; <strong>nitrates share headache and flushing</strong> with the dihydropyridines [slide 31].</p>
  <p><strong>Verapamil and diltiazem lower heart rate and slow atrioventricular conduction</strong> [slide 21]; beta blockers also lower heart rate [slide 16]. Read together with slide 23, which lists concurrent beta blocker use as a precaution for non-dihydropyridines, combining verapamil or diltiazem with a beta blocker calls for caution because the effects are additive: <strong>additive bradycardia and conduction delay</strong>.</p>

  <p><strong>CYP3A4 (cytochrome P450 3A4).</strong> Verapamil and diltiazem, the non-dihydropyridines, <strong>inhibit CYP3A4 and are also substrates of it</strong>; the dihydropyridines such as amlodipine are only substrates (section 3.4). Slide 23 lists CYP3A4 interactions as a precaution. The worked example crosses to the lipid section: simvastatin is a CYP3A4 substrate (section 4.2), so a patient on verapamil who is then given simvastatin has higher simvastatin levels. In plain terms: adding simvastatin to a patient taking verapamil raises simvastatin levels because verapamil inhibits cytochrome P450 3A4, which clears simvastatin, so the main risk is statin muscle and liver toxicity (the statin adverse effects are in section 4.2).</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 28:02 of the recording: <em>&ldquo;If you don&rsquo;t know any other CYP enzyme, know CYP3A4, please, that&rsquo;s my only ask&hellip; the non-DHPs are both inhibitors of CYP3A4 and substrates&hellip; the DHPs like amlodipine are just substrates&hellip; a patient on verapamil and then you put them on simvastatin&hellip; now all of a sudden you&rsquo;re jacking your simvastatin levels up.&rdquo;</em></p>
    <p><mark class="prof-highlight">CYP3A4 is the one enzyme to know</mark>: non-dihydropyridines inhibit it and are substrates, dihydropyridines are only substrates, and verapamil with simvastatin raises the simvastatin level [slide 23; Antihypertensives slides 47, 48 and 54; sections 3.4 and 4.2].</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; atrioventricular block.</strong> Slide 23 lists
  atrioventricular block as a calcium channel blocker contraindication without saying which subclass. It is the
  <strong>non-dihydropyridines</strong> that slow atrioventricular conduction (slide 21 shows no effect for the
  dihydropyridines), and slide 34 names a dihydropyridine as first line when the patient has bradycardia or
  atrioventricular block. Read the contraindication as applying to diltiazem and verapamil.</div>

  <p><strong>Monitoring:</strong> relief of symptoms, and heart rate for the non-dihydropyridines [slide 24].
  <strong>Education:</strong> dizziness and constipation [slide 24]. The pairing caution is the one to remember:
  concurrent beta blocker use is a precaution for the non-dihydropyridines [slide 23], and the dihydropyridine
  is the calcium channel blocker named for combining with a beta blocker [slide 22]. The interacting agents of the
  non-dihydropyridines (statins, digoxin and others) are in section 3.4.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 29:48 of the recording: <em>&ldquo;Ask your patients about their bowel habits&hellip; what happens when they&rsquo;re sitting there straining on the toilet&hellip; let&rsquo;s put a little strain on the heart too.&rdquo;</em></p>
    <p>Education: <mark class="prof-highlight">dizziness and constipation</mark> [slide 24]. He added why constipation matters in a cardiac patient: straining puts a strain on the heart.</p>
  </div>

  <h3 class="sub" id="mi-nitrates">5.4 &middot; Objectives 1&ndash;7 &mdash; Nitrates</h3>

  <h4 class="subsub">Mechanism (Objective 2) [slide 26]</h4>
  <ol>
    <li>Nitrates supply <strong>nitric oxide</strong>.</li>
    <li>Nitric oxide stimulates the conversion of guanosine triphosphate to <strong>cyclic guanosine
    monophosphate</strong>.</li>
    <li>Cyclic guanosine monophosphate activates protein kinase G, which <strong>lowers cytosolic calcium</strong>.</li>
    <li>Lower calcium gives <strong>smooth muscle relaxation, vasodilation and lower blood pressure</strong>.</li>
    <li><strong>Phosphodiesterase type 5 breaks cyclic guanosine monophosphate down</strong> to inactive
    guanosine monophosphate.</li>
    <li><strong>Sildenafil, tadalafil and vardenafil inhibit phosphodiesterase type 5</strong>, so cyclic guanosine
    monophosphate builds up. Together with a nitrate this is the drug interaction the slide shows.</li>
  </ol>

  <p>On the <strong>demand</strong> side nitrates lower systolic blood pressure and, most strongly, left
  ventricular volume, while the heart rate rises [slide 25]. On the <strong>supply</strong> side they dilate the
  coronary arteries, relieve vasospasm and have antithrombotic and antiplatelet effects [slide 25].</p>

  <h4 class="subsub">Short-acting nitrates [slides 27 and 28]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides say</th></tr>
    <tr><td>Goals of therapy</td><td><strong>Relieve acute symptoms of myocardial ischemia and prevent effort-induced angina</strong> [slide 27]</td></tr>
    <tr><td>Forms pictured</td><td>Nitroglycerin sublingual tablets (Nitrostat) and a nitroglycerin lingual spray (Nitrolingual Pumpspray) [slide 27]</td></tr>
    <tr><td>Drug selection</td><td>Dosed every 5 minutes until relief or emergency medical services arrive (standard practice caps it at three doses in total; his words: keep dosing while waiting); <strong>call emergency medical services if there is no relief 5 minutes after the first dose</strong> [slide 27]</td></tr>
    <tr><td>Patient education</td><td>Warn about <strong>orthostatic hypotension</strong>; store in the original packaging in a cool, dry place; <strong>replace the tablets 3 to 6 months after opening</strong> (the slide&rsquo;s older rule; see the note below); apply or spray under the tongue [slide 28]</td></tr>
  </table>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 35:51 of the recording: <em>&ldquo;If I say a test question, which one of these is best for quick relief of myocardial&hellip; a quick relief of anginal symptoms, this is the answer. Okay, keep that in mind, highlight.&rdquo;</em></p>
    <p><mark class="prof-highlight">Short-acting nitroglycerin</mark> (sublingual tablet or spray) is the quick-relief answer [slide 27]; beta blockers and calcium channel blockers prevent attacks.</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 37:02 of the recording: <em>&ldquo;That&rsquo;s why I say after five minutes if you don&rsquo;t get the relief, call 911, okay, so you get one try and that&rsquo;s it, but while waiting you can continue taking the doses every five minutes.&rdquo;</em></p>
    <p>The patient takes the first dose; <mark class="prof-highlight">no relief after five minutes means call emergency services</mark>, and further doses can be taken while waiting [slide 27]. The action is the testable point.</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 37:12 of the recording: <em>&ldquo;Orthostatic hypotension makes sense&hellip; store them in the original packaging, a cool dry place, don&rsquo;t put them into your pill minder&hellip; and then we&rsquo;ll say after opening it replace every three to six months or so&hellip; I say go ahead, yes, do replace it.&rdquo;</em></p>
    <p>Warn about <mark class="prof-highlight">orthostatic hypotension</mark>; keep tablets in the original packaging in a cool, dry place; he teaches replacement every three to six months, which this guide notes is the course rule (current labeling ties expiry to the original bottle) [slide 28].</p>
  </div>

  <div class="callout"><strong>The five-minute rule is a safety protocol (Objective 9).</strong> The action is the
  point: <strong>if chest pain is not relieved five minutes after the first dose, call emergency medical services
  rather than keep dosing alone</strong> [slide 27]. The slide also says to dose every 5 minutes until relief or
  help arrives; the two lines agree once you read the second as &ldquo;while help is on the way&rdquo;. Standard practice caps it at three doses in total; his words: keep dosing while waiting.</div>

  <div class="callout"><strong>Deck versus truth &mdash; replacing the tablets.</strong> Slide 28 says to replace nitroglycerin tablets 3 to 6 months after opening. That is older advice; current labeling ties the expiry to the printed date when the tablets stay in the original tightly closed bottle. Learn it as the slide&rsquo;s rule and do not treat the number as the point.</div>

  <h4 class="subsub">Long-acting nitrates [slides 29 to 31]</h4>
  <table>
    <tr><th>Topic</th><th>What the slides say</th></tr>
    <tr><td>Place in therapy</td><td>Initial therapy to reduce symptoms <strong>when beta blockers and calcium channel blockers are contraindicated or not tolerated</strong>; or in combination with a beta blocker or calcium channel blocker when those are not successful [slide 29]</td></tr>
    <tr><td>Use</td><td><strong>Usually adjunctive therapy; not recommended as monotherapy</strong> [slide 29]. The two lines fit together this way: monotherapy is discouraged when a beta blocker or calcium channel blocker can be used, and a long-acting nitrate alone is accepted only when neither can be</td></tr>
    <tr><td>Isosorbide mononitrate (Imdur)</td><td><strong>Lasts 12 hours and is dosed daily</strong> [slide 30]</td></tr>
    <tr><td>Isosorbide dinitrate</td><td><strong>Duration 3 to 6 hours and dosed three times daily</strong> [slide 30]</td></tr>
    <tr><td>Nitroglycerin ointment (Nitro-Bid)</td><td>Squeeze onto the calibrated applicator paper; spread in a thin 2-inch by 2-inch layer on the chest; keep covered with the applicator paper; <strong>wipe off the previous dose before adding a new dose</strong>; 12 hours on, 12 hours off [slide 31]</td></tr>
    <tr><td>Transdermal patch</td><td><strong>12 hours on, 12 hours off</strong> [slide 31]</td></tr>
    <tr><td>Adverse reactions</td><td><strong>Headache, flushing, postural hypotension and reflex tachycardia</strong> (a reflex rise in heart rate, compensating for the fall in pressure) [slide 31]</td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 39:19 of the recording: <em>&ldquo;This is usually like the third add-on medication in that list&hellip; usually adjunctive therapy, very rarely or not recommended as monotherapy.&rdquo;</em></p>
    <p><mark class="prof-highlight">Long-acting nitrates are usually the third add-on</mark>, after a beta blocker and a calcium channel blocker, and rarely or not recommended as monotherapy [slide 29].</p>
  </div>

  <h4 class="subsub">Tachyphylaxis and the nitrate-free interval [slide 32]</h4>
  <p><strong>Tachyphylaxis</strong> is the loss of effect with continued dosing; the slide lists it as a
  consideration with nitrates. Its mechanism is <strong>not fully understood</strong>. Proposed contributors are
  depletion of cofactors, stimulation of counter-regulatory responses (the renin-angiotensin system and the
  sympathetic nervous system), plasma volume expansion, and decreased enzyme activity. The management is a
  <strong>nitrate-free interval, placed when the patient has the lowest symptom frequency</strong>. That is why the
  ointment and the patch are worn 12 hours on and 12 hours off.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 42:42 of the recording: <em>&ldquo;Regardless, all you need to know is do the nitrate-free interval for 12 hours when the patient is least likely to have symptom frequency, usually when they&rsquo;re asleep.&rdquo;</em></p>
    <p>Tachyphylaxis is handled by <mark class="prof-highlight">12 hours on and 12 hours off</mark>, timed so the off period is when the patient is least likely to have chest pain, usually asleep [slide 32].</p>
  </div>


  <h4 class="subsub">Absorption, distribution, metabolism and excretion (Objective 4)</h4>
  <p>The slides give routes and durations only. Short-acting nitroglycerin is taken under the tongue as a tablet or a
  spray [slides 27 and 28]. Long-acting nitrates come as isosorbide mononitrate (12 hours) and isosorbide
  dinitrate (3 to 6 hours), and as nitroglycerin ointment and a transdermal patch worn 12 hours on and 12 hours off
  [slides 30 and 31]. In acute coronary syndrome the sublingual route is followed by an intravenous infusion in
  the hospital [slide 54]. No metabolism or excretion is given.</p>

  <p><strong>Long-acting nitrates are usually used as add-on (adjunctive) therapy</strong>, added when a beta blocker or calcium channel blocker is not enough [slide 29]. <strong>Nitrates lower left ventricular volume the most of the three antianginal classes</strong>, which lowers wall tension, while the heart rate rises [slides 6 and 25]. <strong>Reflex tachycardia</strong> is a nitrate adverse reaction, a reflex rise in heart rate that follows the fall in blood pressure; it is listed with headache, flushing and postural hypotension [slide 31]. <strong>In acute coronary syndrome, nitroglycerin and the other nitrates relieve chest pain but show no mortality benefit</strong>; they start sublingually and move to an intravenous infusion in hospital [slides 52 and 54].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 33:39 of the recording: <em>&ldquo;The problem comes when you do both of these together&hellip; that can lead to profound hypotension&hellip; if the answer is yes, you cannot give them a nitrate, because it will synergize, it&rsquo;ll drop their blood pressure, they could die.&rdquo;</em></p>
    <p>Sildenafil, tadalafil and vardenafil with any nitrate: <mark class="prof-highlight">contraindicated</mark>, with hypotension, myocardial infarction and stroke as the risk [slide 33]. He said the patient should be asked, bluntly if needed.</p>
  </div>

  <h4 class="subsub">Contraindications (Objective 7) [slide 33]</h4>
  <p>A nitrate, including nitroglycerin, is contraindicated in <strong>obstructive cardiomyopathy</strong>, in <strong>aortic valve stenosis</strong>, and with <strong>phosphodiesterase type 5 inhibitors</strong>.</p>
  <ul>
    <li><strong>Aortic valve stenosis is a contraindication to nitrates.</strong></li>
    <li><strong>Obstructive cardiomyopathy is a contraindication to nitrates.</strong></li>
    <li><strong>Concurrent use of phosphodiesterase inhibitors: sildenafil (Viagra), tadalafil (Cialis) and
    vardenafil (Levitra).</strong> Concurrent use may lead to hypotension and myocardial infarction or stroke.</li>
  </ul>
  <div class="callout"><strong>Deck versus truth &mdash; nitrate contraindications.</strong> Slide 33 lists aortic valve stenosis and obstructive cardiomyopathy as contraindications. Current labeling treats severe aortic stenosis and obstructive cardiomyopathy as conditions to avoid or use with great caution, because nitrates can drop the blood pressure and worsen the outflow obstruction. The phosphodiesterase type 5 inhibitor combination is the absolute one.</div>

  <h3 class="sub" id="mi-addon">5.5 &middot; Objectives 1&ndash;3 and 7 &mdash; Add-on therapy, comorbid conditions and variant angina</h3>

  <h4 class="subsub">Combination therapy [slide 36]</h4>
  <p>Consider combination therapy <strong>if angina persists with monotherapy</strong> [slide 36]. A beta blocker
  and a calcium channel blocker may be combined if the patient can tolerate it, and there is some evidence that
  this increases exercise duration [slide 36]. If a <strong>third agent</strong> seems needed, the patient
  probably needs further workup, such as angiography [slide 36]. (In practice the calcium channel blocker paired
  with a beta blocker is a dihydropyridine, as slide 22 says.)</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 14:21 of the recording: <em>&ldquo;How do we sequence these medications, in what order do you use these&hellip; that was really easy for test questions where I can say, okay, well, patient&rsquo;s already on this and they&rsquo;re not really at goal, what do you want to do next? Or they&rsquo;re intolerant to this, what do you want to switch to?&rdquo;</em></p>
    <p>Two stem shapes: <mark class="prof-highlight">add-on</mark> (beta blocker, then a dihydropyridine calcium channel blocker, then a long-acting nitrate) and <mark class="prof-highlight">switch</mark> (beta blocker not tolerated, so a non-dihydropyridine calcium channel blocker) [slides 22, 29 and 36].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 46:55 of the recording: <em>&ldquo;If you see anyone who&rsquo;s on a beta blocker plus a non-DHP, you&rsquo;re just kind of begging for trouble with that kind of combination&hellip; if you need a third agent you probably need further workup.&rdquo;</em></p>
    <p>Dihydropyridine plus a beta blocker is the sensible pair; a beta blocker with a non-dihydropyridine is avoided; <mark class="prof-highlight">a third agent means further workup</mark> such as angiography [slide 36].</p>
  </div>

  <h4 class="subsub">Which drug for which comorbid condition [slide 34]</h4>
  <table>
    <tr><th>Comorbid condition</th><th>First line</th><th>Alternative</th><th>Avoid</th></tr>
    <tr><td><strong>Hypertension</strong></td><td>Beta blocker</td><td>Non-dihydropyridine calcium channel blocker</td><td>None listed</td></tr>
    <tr><td><strong>Prior myocardial infarction</strong></td><td>Beta blocker</td><td>None listed</td><td>Calcium channel blockers (slide wording; see the box below)</td></tr>
    <tr><td><strong>Decreased left ventricular function</strong></td><td>Beta blocker</td><td>Amlodipine</td><td>Other calcium channel blockers</td></tr>
    <tr><td><strong>Bradycardia or atrioventricular block</strong></td><td>Dihydropyridine calcium channel blocker</td><td>Long-acting nitrate</td><td>Non-dihydropyridines and beta blockers</td></tr>
    <tr><td><strong>Diabetes</strong></td><td>Non-dihydropyridine (slide wording; see the box below)</td><td>Long-acting nitrate; cardioselective beta blocker</td><td>Non-cardioselective beta blocker</td></tr>
    <tr><td><strong>Asthma</strong></td><td>Non-dihydropyridine and cardioselective beta blocker</td><td>None listed</td><td><strong>Non-cardioselective beta blocker</strong></td></tr>
  </table>
  <p>The firm, uncontested reading: a <strong>beta blocker is first line after a myocardial infarction, with
  hypertension, and with reduced left ventricular function</strong> (amlodipine is the calcium channel blocker
  alternative there and the other calcium channel blockers are avoided); a <strong>dihydropyridine is first
  line with bradycardia or atrioventricular block, and non-dihydropyridines and beta blockers are avoided</strong>;
  and a <strong>non-cardioselective beta blocker is avoided in asthma</strong> [slide 34]. Slide 18 lists reactive
  airway disease as a beta blocker precaution, which agrees. In asthma the cardioselective beta blockers the table
  lists are used with caution [slides 18 and 34]. In a patient with angina and asthma, <strong>non-selective beta blockers such as propranolol are avoided</strong>, while cardioselective beta blockers and non-dihydropyridine calcium channel blockers remain options [slide 34].</p>

  <div class="callout"><strong>Deck versus truth &mdash; two contested cells in the comorbidity table.</strong>
  <ul>
    <li><strong>Prior myocardial infarction &rarr; &ldquo;avoid calcium channel blockers.&rdquo;</strong> The slide
    says avoid them; that is over-simple. A beta blocker is first line after a myocardial infarction, but a
    non-dihydropyridine is a reasonable substitute when a beta blocker is contraindicated (slide 22) and there is no
    reduced left ventricular function. What is avoided is short-acting nifedipine and, with reduced function, the
    non-dihydropyridines.</li>
    <li><strong>Diabetes &rarr; &ldquo;non-dihydropyridine first line, avoid non-cardioselective beta
    blocker.&rdquo;</strong> This is an older simplification. A beta blocker remains a sound first choice in a patient
    with diabetes and angina; a cardioselective agent is preferred, and slide 18&rsquo;s caution about diabetes still
    applies. Diabetes is not a reason to put a non-dihydropyridine ahead of a beta blocker.</li>
  </ul>
  Do not memorize these two cells as the slide words them.</div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 43:30 of the recording: <em>&ldquo;This is a really good table for your anti-anginals&hellip; come back to this, because this is like a cornucopia of test questions could come from something like this.&rdquo;</em></p>
    <p>At 44:16 of the recording: <em>&ldquo;For things to avoid, for prior MI, calcium channel blockers kind of in general, we really prefer beta blockers just from the evidence that we have in terms of mortality&hellip; be very cautious.&rdquo;</em></p>
    <p><strong>He read these; current practice differs.</strong> He walked the table row by row and called it a cornucopia of test questions: hypertension, reduced left ventricular function and (after a myocardial infarction) a prior infarction all point to a beta blocker; bradycardia or block points to a dihydropyridine; asthma points to a cardioselective beta blocker or a non-dihydropyridine [slide 34]. He also read the prior-infarction and diabetes cells as the slide words them, but the boxed note above applies: do not learn those two cells as the slide has them.</p>
  </div>


  <h4 class="subsub">Angiotensin-converting enzyme inhibitors [slide 35]</h4>
  <p>These are used in patients with coronary artery disease who also have <strong>diabetes and/or left ventricular
  systolic dysfunction</strong> [slide 35]. They <strong>do not significantly affect myocardial oxygen
  consumption</strong> and <strong>do not relieve the symptoms of angina</strong> [slide 35]. They <strong>may
  help prevent progression of coronary artery disease</strong> [slide 35]. They should be used
  <strong>indefinitely</strong> after a myocardial infarction, with left ventricular dysfunction, or with diabetes
  [slide 35]. They should be considered in <strong>all patients with coronary artery disease or other vascular
  disease</strong> [slide 35]. They are vasculoprotective, not antianginal [slide 12].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 45:50 of the recording: <em>&ldquo;They do not relieve symptoms of angina, but they will help to prevent the progression of the coronary artery disease&hellip; these should be indefinitely in patients for post-MI, LV dysfunction, diabetes.&rdquo;</em></p>
    <p><mark class="prof-highlight">ACE inhibitors do not relieve angina</mark> [slide 35]; they are vasculoprotective and slow disease progression, and are continued indefinitely after infarction, with left ventricular dysfunction or with diabetes.</p>
  </div>

  <h4 class="subsub">Antiplatelet therapy [slide 37]</h4>
  <p><strong>Aspirin is given in the absence of contraindications</strong> [slide 37]. <strong>Aspirin is used in ischemic heart disease for preventing acute coronary syndromes</strong>: it is given to every patient with ischemic heart disease who has no contraindication, to prevent acute coronary syndrome rather than to relieve symptoms [slide 37]. Its place in therapy is to
  <strong>prevent acute coronary syndrome</strong>, in <strong>all patients with ischemic heart disease</strong>
  who have no contraindication [slide 37]. The slide gives about a 30 percent reduction in the risk of primary
  events with aspirin. <strong>Clopidogrel is as efficacious as aspirin in secondary prevention and is recommended
  for patients allergic to aspirin</strong> [slide 37].</p>

  <h4 class="subsub">The whole strategy on one slide [slide 38]</h4>
  <table>
    <tr><th>Group</th><th>Drugs</th></tr>
    <tr><td><strong>Give to everyone unless contraindicated</strong></td><td>Aspirin; a beta blocker if there was a prior myocardial infarction; an angiotensin-converting enzyme inhibitor in patients with diabetes or left ventricular dysfunction; lipid-lowering therapy; sublingual nitroglycerin for acute relief</td></tr>
    <tr><td><strong>For daily or more frequent symptoms</strong> (prophylactic therapy)</td><td>Beta blockers; calcium channel blockers; long-acting nitrates</td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 48:19 of the recording: <em>&ldquo;Unless contraindicated, patients with coronary artery disease or ischemic heart disease should be getting aspirin, if they&rsquo;ve had a previous MI beta blockers for sure, ACEs or ARBs in patients who have diabetes or LV dysfunction, lipid lowering therapy&hellip; they will have sublingual nitroglycerin for acute relief.&rdquo;</em></p>
    <p><mark class="prof-highlight">The standing list, unless contraindicated:</mark> aspirin; a beta blocker after infarction; an angiotensin-converting enzyme inhibitor (or receptor blocker) with diabetes or left ventricular dysfunction; lipid-lowering therapy; sublingual nitroglycerin for acute relief [slide 38].</p>
  </div>

  <h4 class="subsub">Variant angina [slides 8 and 39]</h4>
  <p><strong>Calcium channel blockers and nitrates can reduce symptoms</strong> of variant angina, because both
  relieve vasospasm [slides 20, 25 and 39]. <strong>Avoid beta blockers: they may lead to worsened symptoms</strong>
  [slide 39]. In variant angina the usual first line drug, the beta blocker, is the one to avoid [slide 39].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 26:25 of the recording: <em>&ldquo;If you were to say what&rsquo;s the treatment of choice for a variant angina or Prinzmetal angina, usually it&rsquo;s going to be a DHP&hellip; their problem is not necessarily contractility or heart rate, it&rsquo;s just that vessel is clamping down.&rdquo;</em></p>
    <p>At 49:11 of the recording: <em>&ldquo;For the variant angina, the Prinzmetal angina, that&rsquo;s where you get into utilizing your dihydropyridine calcium channel blockers most commonly, you typically avoid beta blockers, they tend to worsen symptoms for the patient.&rdquo;</em></p>
    <p><mark class="prof-highlight">Variant angina: calcium channel blockers (usually a dihydropyridine) and nitrates; avoid beta blockers.</mark> The problem is the vessel clamping down, a supply problem, not heart rate or contractility [slides 8 and 39].</p>
  </div>


  <h3 class="sub" id="mi-acs">5.6 &middot; Objectives 1&ndash;3 &mdash; Acute coronary syndrome and thrombus formation</h3>

  <h4 class="subsub">Classification [slide 41]</h4>
  <p>Acute coronary syndrome has two branches [slide 41]. <strong>ST-segment elevation myocardial infarction</strong> is one. <strong>Non-ST-segment elevation acute coronary syndrome</strong> is the other, and it
  contains <strong>unstable angina</strong> and <strong>non-ST-elevation myocardial infarction</strong> [slide 41].
  The figure on the slide runs as follows: ischemic discomfort leads to a working diagnosis of acute coronary
  syndrome; the electrocardiogram then splits it, with <strong>no ST elevation</strong> giving unstable angina or
  non-ST-elevation myocardial infarction (also called non-Q-wave myocardial infarction), and <strong>ST
  elevation</strong> giving ST-elevation myocardial infarction (drawn on the slide as Q-wave myocardial infarction); a <strong>biochemical marker separates unstable angina
  from myocardial infarction</strong>. The heart cross-sections at 1 hour, 4 hours and 8 hours show the infarct
  growing into the area of ischemia [slide 41]. Slide 4 lists sudden cardiac death under acute coronary
  syndrome; the working classification on slide 41 is ST-elevation myocardial infarction versus non-ST-elevation
  acute coronary syndrome.</p>

  <p><strong>ST-elevation myocardial infarction</strong> is the branch with ST elevation on the electrocardiogram in a patient with ischemic discomfort [slide 41]; it is the form for which fibrinolytics are indicated [slide 65]. <strong>If coronary blood flow is not restored, the infarct grows over hours into the area of ischemia</strong> [slide 41]; read together with slide 51, this is why reestablishing coronary blood flow is a goal of therapy.</p>

  <h4 class="subsub">How a thrombus forms, step by step [slides 42 to 50]</h4>
  <ol>
    <li><strong>The plaque.</strong> The vessel wall has endothelium, smooth muscle cells, and an atherosclerotic
    plaque under a fibrous cap [slide 42].</li>
    <li><strong>Injury.</strong> A procedural injury such as balloon deployment, or a spontaneous injury,
    leaves <strong>injured endothelium</strong> [slide 43].</li>
    <li><strong>Platelets respond.</strong> Platelet <strong>adhesion, activation and aggregation</strong> occur at
    the plaque [slide 44].</li>
    <li><strong>Fibrin forms.</strong> Fibrin strands form [slide 45].</li>
    <li><strong>The occlusive thrombus.</strong> The clot blocks the artery [slide 46].</li>
  </ol>
  <p><strong>Thrombin is the link</strong> between tissue injury, coagulation and the platelet response
  [slide 47]. Exposed collagen leads to release of <strong>adenosine diphosphate and thromboxane A2</strong>,
  which activate and aggregate platelets [slide 47]. <strong>Tissue factor</strong> starts the plasma clotting
  cascade; prothrombin becomes thrombin, and <strong>thrombin turns fibrinogen into fibrin</strong>, which forms the
  thrombus [slide 47]. Thrombin is a critical mediator in coagulation and elicits multiple responses in platelets
  [slide 47].</p>
  <table>
    <tr><th>Phase of clotting</th><th>What happens</th></tr>
    <tr><td><strong>Initiation</strong> [slide 48]</td><td>Tissue factor complexes with factor VIIa at the site of injury, activates factor X and factor IX, and generates a small amount of thrombin</td></tr>
    <tr><td><strong>Amplification</strong> [slide 49]</td><td>Thrombin activates platelets and stimulates its own production by activating factors V and VIII, and also factor XI (figure); the coagulation factors VIIIa, Va and IXa assemble on the surface of activated platelets</td></tr>
    <tr><td><strong>Propagation</strong> [slide 50]</td><td>The assembled complexes continue the cascade on the activated platelets: prothrombin is converted to thrombin, fibrinogen to fibrin, and the clot is stabilized</td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 51:33 of the recording: <em>&ldquo;If you only had to know two clotting factors, the two most important ones are 10 and 2&hellip; that&rsquo;s what&rsquo;s going to cause the activation of fibrin.&rdquo;</em></p>
    <p><mark class="prof-highlight">The two factors he said to know are factor X and factor II (thrombin).</mark> Factor X is activated in initiation [slide 48]; prothrombin (factor II) becomes thrombin, which activates platelets and turns fibrinogen into fibrin [slides 47 and 49].</p>
  </div>

  <h4 class="subsub">Goals of therapy [slide 51]</h4>
  <p>The five goals are to <strong>reestablish coronary blood flow, relieve chest pain, prevent progression to
  myocardial infarction, prevent the development of heart failure, and prevent death</strong> [slide 51].</p>

  <h3 class="sub" id="mi-acs-drugs">5.7 &middot; Objectives 1&ndash;7 &mdash; Acute coronary syndrome: aspirin, nitrates, beta blockers, morphine</h3>

  <p>Aspirin, nitrates and beta blockers are the <strong>common pharmacologic therapy for both ST-elevation
  myocardial infarction and non-ST-elevation acute coronary syndrome</strong> [slide 52].</p>

  <table>
    <tr><th>Drug</th><th>Use and timing</th><th>Benefit</th><th>Adverse effects</th><th>Contraindications and cautions</th></tr>
    <tr><td><strong>Aspirin</strong> [slides 52, 53]</td><td>Used at the <strong>first signs of chest pain</strong>; <strong>chewed and swallowed</strong></td><td>Reduces mortality and reinfarction; decreases recurrent ischemia, stroke and cardiac death</td><td>Not listed on these slides</td><td><strong>Allergy, recent gastrointestinal bleed, recent intracranial hemorrhage</strong></td></tr>
    <tr><td><strong>Nitrates</strong> [slides 52, 54]</td><td>Start with <strong>sublingual</strong> therapy, then an <strong>intravenous infusion</strong> once in the hospital</td><td><strong>No mortality benefit and no improvement in outcomes; relief of chest pain only</strong></td><td><strong>Hypotension, headache, reflex tachycardia</strong></td><td><strong>Hypotension; phosphodiesterase inhibitors</strong></td></tr>
    <tr><td><strong>Beta blockers</strong> [slides 52, 55]</td><td>Intravenous, followed by oral</td><td>Reduce early and late mortality, infarct size, heart failure and sudden cardiac death</td><td>Not listed on these slides</td><td>Caution with <strong>bradycardia or hypotension, heart block, and severe reactive airway disease</strong></td></tr>
    <tr><td><strong>Morphine</strong> [slide 56]</td><td>An opioid analgesic for <strong>chest pain that does not respond to nitrates</strong>; used in ST-elevation myocardial infarction</td><td>Analgesic for chest pain [slide 56]</td><td><strong>Hypotension, allergy</strong></td><td>May have <strong>increased mortality in unstable angina and non-ST-elevation myocardial infarction</strong>; its use is controversial</td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 54:21 of the recording: <em>&ldquo;Aspirin contraindications would just be different kind of like GI bleed or intracranial hemorrhage&hellip; should be one of the absolute got to use it, if you have an allergy and couldn&rsquo;t receive aspirin that&rsquo;s where those ADP blockers like clopidogrel come into play.&rdquo;</em></p>
    <p><mark class="prof-highlight">Aspirin first</mark>, chewed and swallowed at the first signs; contraindications are allergy, gastrointestinal bleeding and intracranial hemorrhage; clopidogrel is the alternative [slides 37, 52 and 53].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 53:58 of the recording: <em>&ldquo;Nitrates only help with symptom relief&hellip; they don&rsquo;t do anything for outcomes.&rdquo;</em></p>
    <p><mark class="prof-highlight">Nitrates give pain relief with no mortality benefit</mark> in acute coronary syndrome: sublingual first, then an intravenous infusion in hospital [slides 52 and 54].</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 55:17 of the recording: <em>&ldquo;Beta blockers will start IV initially till we get them under control and then we can switch over to PO, just know there&rsquo;s going to be contraindicated if they&rsquo;re already hypotensive or bradycardic or if they&rsquo;re having heart block&hellip; and then you know they have severe reactive airway disease, something like a cardioselective beta blocker would make sense.&rdquo;</em></p>
    <p>Cautions: <mark class="prof-highlight">hypotension, bradycardia, heart block, severe reactive airway disease</mark> (a cardioselective agent would make sense) [slide 55]. <strong>Flag:</strong> the intravenous-then-oral sequence is older teaching that he gave; see the deck-versus-truth box above, and do not learn the sequence.</p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 55:54 of the recording: <em>&ldquo;Morphine is not really shown to have any benefits on outcomes but it does help out with the pain&hellip; if they&rsquo;re having pain unresponsive to nitrates then you would initiate an opioid like morphine&hellip; some controversy in using it for unstable angina and [NSTEMI], but for the most part for STEMI is perfectly fine.&rdquo;</em></p>
    <p><mark class="prof-highlight">Morphine treats the pain only</mark>; it is reserved for pain that does not respond to nitrates, fine in ST-elevation myocardial infarction and controversial in unstable angina and non-ST-elevation myocardial infarction [slide 56].</p>
  </div>

  <p>Because the beta blocker cautions in acute coronary syndrome are bradycardia and hypotension [slide 55], <strong>heart rate and blood pressure are the findings to check before and after a beta blocker is given</strong> (read together with slide 55).</p>

  <p>The slides separate what each drug does for <strong>the patient&rsquo;s survival</strong> from what it does for
  <strong>the patient&rsquo;s pain</strong>: aspirin and beta blockers change outcomes; <strong>nitrates only relieve
  pain</strong> [slides 52 and 54]; morphine is held back for pain that nitrates do not relieve [slide 56]. Slide 52
  says beta blockers cut the risk of myocardial infarction among unstable angina patients by 13 percent and cut
  deaths in myocardial infarction patients by 40 percent.</p>

  <div class="callout"><strong>Deck versus truth &mdash; beta blockers in acute coronary syndrome.</strong> Slide 55
  says &ldquo;intravenous followed by oral.&rdquo; That reflects older practice. Current guidance favors an oral beta
  blocker within the first 24 hours and avoids early intravenous dosing in patients with signs of heart failure, low
  output or a risk of shock; intravenous use is kept for ongoing ischemia or high blood pressure without those
  contraindications. The mortality figures on slides 52 and 55 come from older trials; the benefit that holds today is mainly
  long-term use after a myocardial infarction. Early beta blockade can worsen heart failure and shock, so the
  heart failure benefit on the slide is also an older-trial claim. The caution list on the slide is the part to keep.</div>

  <h3 class="sub" id="mi-lytics">5.8 &middot; Objectives 1&ndash;7 &mdash; Fibrinolytics and other antithrombotic drugs</h3>

  <h4 class="subsub">The fibrinolytic system [slides 57 and 58]</h4>
  <p>The figure shows <strong>plasminogen</strong> being converted to <strong>plasmin</strong>, and plasmin breaking
  fibrin into fibrin products [slide 57]. <strong>Tissue plasminogen activator</strong> drives the first step
  [slide 57]. The brakes on the system are <strong>plasminogen activator inhibitor-1, plasminogen activator
  inhibitor-2, alpha-2 antiplasmin and thrombin-activatable fibrinolysis inhibitor</strong> [slide 57]. All the
  fibrinolytic drugs act <strong>directly or indirectly to activate the conversion of plasminogen to
  plasmin</strong> [slide 58]. Plasminogen is inactive in the circulation and is converted to plasmin by tissue
  plasminogen activator [slide 58]. Plasmin lyses fibrin and fibrinogen [slide 58].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 58:27 of the recording: <em>&ldquo;Streptokinase, kind of an older one we&rsquo;ve used in the past, I don&rsquo;t want you to worry so much about that, but I do want to focus on this picture here&hellip; plasminogen coming in with streptokinase to form a complex&hellip; a tissue plasminogen activator, which is what we naturally produce, could do this as well.&rdquo;</em></p>
    <p><strong>Learn the picture, not the drug:</strong> plasminogen is converted to plasmin, by a streptokinase complex or by tissue plasminogen activator, which the body also makes [slides 59 and 60].</p>
  </div>

  <h4 class="subsub">Mechanisms by agent [slides 59 to 61]</h4>
  <table>
    <tr><th>Agent</th><th>How it works</th></tr>
    <tr><td><strong>Streptokinase</strong></td><td>Forms a <strong>stable 1:1 complex with plasminogen</strong>; the complex exposes a catalytic site and converts other plasminogen to plasmin [slides 59 and 60]</td></tr>
    <tr><td><strong>Urokinase</strong></td><td>Converts plasminogen to plasmin directly [slide 60]</td></tr>
    <tr><td><strong>Tissue plasminogen activator (alteplase)</strong></td><td><strong>Binds plasminogen that is bound to fibrin</strong> and converts it to plasmin, which lyses the clot [slide 59]</td></tr>
    <tr><td><strong>Reteplase and tenecteplase</strong></td><td>Act like tissue plasminogen activator on fibrin-bound plasminogen; very similar responses and adverse effects [slide 61]</td></tr>
  </table>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 58:49 of the recording: <em>&ldquo;The three main ones you&rsquo;re going to run into include tPA, which is a recombinant tissue plasminogen activator, and then we also have reteplase and tenecteplase&hellip; working more specifically on plasminogen that&rsquo;s bound to fibrin&hellip; if it activated plasminogen all over the body you just bleed out and die.&rdquo;</em></p>
    <p><mark class="prof-highlight">Alteplase, reteplase and tenecteplase</mark> are recombinant and aimed at plasminogen bound to fibrin, so the clot is lysed with less activation of plasminogen elsewhere (selectivity is relative; bleeding is still the main risk) [slides 59 and 61]. <strong>Study note:</strong> he describes the fibrin selectivity at the class level; the deck-versus-truth box below applies to reteplase.</p>
  </div>

  <h4 class="subsub">The three agents and what sets them apart [slide 64]</h4>
  <table>
    <tr><th>Agent (brand)</th><th>Source and notes</th></tr>
    <tr><td><strong>Alteplase (Activase)</strong></td><td>Recombinant deoxyribonucleic acid technology in Chinese hamster ovary cells; directly activates fibrin-bound plasminogen; very expensive</td></tr>
    <tr><td><strong>Reteplase (Retavase)</strong></td><td>Made in <em>Escherichia coli</em> cells; recombinant</td></tr>
    <tr><td><strong>Tenecteplase (TNKase)</strong></td><td>Chinese hamster ovary cells; recombinant with substituted amino acids</td></tr>
  </table>
  <p><strong>Alteplase, reteplase and tenecteplase are the three recombinant fibrinolytic agents</strong> on slide 64; streptokinase is a bacterial protein, not recombinant [slides 59, 61 and 64]. Tenecteplase is a recombinant fibrinolytic, like alteplase and reteplase [slide 64].</p>
  <p>Reteplase and tenecteplase have a <strong>longer half-life than tissue plasminogen activator</strong> and are
  <strong>relatively resistant to plasminogen activator inhibitor-1</strong> [slide 64].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 1:02:06 of the recording: <em>&ldquo;They work very similar to one another, they&rsquo;re all going to be expensive, they can all cause allergy and they all cause bleeding&hellip; it&rsquo;s usually just based off provider preference and hospital formulary.&rdquo;</em></p>
    <p><mark class="prof-highlight">The three recombinant agents are very similar in response and adverse effects</mark>: all are expensive, all can cause allergy and all cause bleeding; the choice follows provider preference and hospital formulary [slides 61 and 62].</p>
  </div>

  <div class="callout"><strong>Deck versus truth &mdash; fibrin affinity, the factor list and urokinase.</strong>
  <ul>
    <li><strong>Fibrin affinity.</strong> Slide 64 says reteplase and tenecteplase have &ldquo;increased affinity for
    fibrin&rdquo;, and slide 61 says tissue plasminogen activator, reteplase and tenecteplase activate &ldquo;only&rdquo;
    fibrin-bound plasminogen. True for tenecteplase. <strong>False for reteplase, which binds fibrin less avidly than
    alteplase.</strong> All three favor clot-bound plasminogen, but not absolutely. Do not rely on the fibrin-affinity
    claim for reteplase.</li>
    <li><strong>Inhibitor resistance.</strong> Slide 64 says reteplase and tenecteplase are relatively resistant to
    plasminogen activator inhibitor-1. That is an established property of tenecteplase; do not rely on it for
    reteplase.</li>
    <li><strong>Factor list.</strong> Slide 58 says plasmin lyses factors II, V and VII as well as fibrin and
    fibrinogen. Sources differ on which clotting factors plasmin degrades; the firm point is fibrin and fibrinogen.
    Do not memorize the factor list.</li>
    <li><strong>Antigenic reactions.</strong> Slide 62 attributes fever, chills and rash &ldquo;mainly to streptokinase
    and urokinase&rdquo;. Only <strong>streptokinase</strong> is antigenic (it is a bacterial protein, so the body
    makes antibodies to it); urokinase is a human enzyme. Attribute these reactions to streptokinase only.</li>
  </ul></div>

  <h4 class="subsub">Absorption, distribution, metabolism and excretion (Objective 4)</h4>
  <p>The slides give no absorption or excretion data. What they give is how each agent is made and how long it lasts:
  alteplase and tenecteplase come from recombinant Chinese hamster ovary cells and reteplase from recombinant
  <em>Escherichia coli</em> cells [slide 64]; reteplase and tenecteplase have a longer half-life than tissue
  plasminogen activator [slide 64]; and streptokinase forms a stable 1:1 complex with plasminogen [slide 59].</p>

  <h4 class="subsub">Adverse effects, all agents (Objectives 5 and 6) [slide 62]</h4>
  <ul>
    <li><strong>Bleeding.</strong></li>
    <li><strong>Allergic reactions</strong>; fever, chills and skin rash, which belong to streptokinase (see the box
    above).</li>
    <li><strong>Anaphylactic reactions.</strong></li>
    <li><strong>Ventricular arrhythmias.</strong></li>
  </ul>
  <p><strong>Allergic reactions including anaphylaxis (anaphylactic reactions) are listed for all fibrinolytic agents</strong>; fever, chills and skin rash occur mainly with streptokinase [slide 62].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 59:41 of the recording: <em>&ldquo;Adverse effects, all these agents, bleeding is the big one&hellip; hemorrhagic stroke, GI bleeds, all kinds of bleeds are possible&hellip; allergic reactions because these are protein-based medications&hellip; and then you could also see ventricular arrhythmias.&rdquo;</em></p>
    <p><mark class="prof-highlight">Bleeding is the big one</mark>, including hemorrhagic stroke and gastrointestinal bleeds; allergic reactions; ventricular arrhythmias [slide 62].</p>
  </div>

  <h4 class="subsub">The nine contraindications (Objective 7) [slide 63]</h4>
  <p>Each of these nine findings contraindicates fibrinolytics, and they apply to every fibrinolytic agent, including tenecteplase, alteplase and reteplase, with one exception: prior exposure to streptokinase or an allergic reaction to it bars streptokinase only [slides 62 and 63]. The nine findings are: <strong>active bleeding</strong> or a hemorrhagic disorder; <strong>pregnancy</strong>; <strong>aortic dissection</strong>; <strong>serious head or facial trauma</strong> (listed with recent surgery); and the other five below. Fibrinolytics cause bleeding as their main adverse effect [slides 62 and 65].</p>
  <ol>
    <li><strong>Recent surgery</strong>, including organ biopsy, puncture of non-compressible vessels, serious head
    or facial trauma and cardiopulmonary resuscitation (the slide says within 10 days).</li>
    <li><strong>Serious gastrointestinal bleeding</strong> (the slide says within 3 months).</li>
    <li><strong>History of hypertension</strong> with a diastolic pressure above 110 mmHg.</li>
    <li><strong>Active bleeding or a hemorrhagic disorder contraindicates fibrinolytics.</strong></li>
    <li><strong>Previous cerebrovascular accident or an active intracranial process</strong> such as a tumor.</li>
    <li><strong>Aortic dissection.</strong></li>
    <li><strong>Acute pericarditis.</strong></li>
    <li><strong>Prior exposure to streptokinase or an allergic reaction to it.</strong></li>
    <li><strong>Pregnancy.</strong></li>
  </ol>
  <p>Most of the list is one idea: <strong>anything that could bleed, or that a bleed would make catastrophic.</strong>
  The exception is prior streptokinase exposure, which is about antigenicity, not bleeding. The numbers on this slide come from an older source; the current wording for item 3 is severe uncontrolled
  hypertension. Item 5 is firm for a prior hemorrhagic stroke or a recent ischemic stroke, not for any old
  stroke. Current guidelines treat recent major surgery, recent gastrointestinal bleeding and pregnancy as
  relative contraindications, and acute pericarditis is an older-list item; any prior intracranial hemorrhage,
  aortic dissection, active bleeding, an intracranial tumor and significant head or facial trauma are the firm
  ones. Learn the categories, not the numbers.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 1:00:30 of the recording: <em>&ldquo;This is important, whenever you&rsquo;re about to decide to give fibrinolytics&hellip; you have to go through your contraindications and if they meet any of these you don&rsquo;t give it&hellip; you have to go through this checklist&hellip; because once it&rsquo;s given you can&rsquo;t take it away.&rdquo;</em></p>
    <p><mark class="prof-highlight">Go through the contraindication checklist before every fibrinolytic</mark>: once it is given it cannot be taken back [slide 63]. <strong>Study note:</strong> the list above separates the firm items from the relative ones.</p>
  </div>

  <h4 class="subsub">Indications (Objective 3) [slide 65]</h4>
  <p>Fibrinolytics are indicated for <strong>ST-elevation myocardial infarction</strong>, the slide giving patients
  under 75 years within 12 hours of symptom onset. There is <strong>less benefit</strong> in patients over 75
  years, more than 6 hours after onset, or with <strong>non-ST-elevation</strong> myocardial infarction
  [slide 65]; slide 68 goes further, saying fibrinolytics are not recommended in non-ST-elevation acute coronary syndrome, and that is the point to learn. Age is a reason for less benefit, not a bar. <strong>Relatively few patients receive these agents</strong> [slide 65]. The main risk is bleeding,
  including intracranial hemorrhage [slide 65].</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 1:02:19 of the recording: <em>&ldquo;Patients less than 75 years of age, for example, if they&rsquo;re within 12 hours of symptom onset&hellip; outside of that window you tend to find patients have less benefit while still having that bleeding risk&hellip; relatively few patients end up getting these big full-blast doses.&rdquo;</em></p>
    <p><mark class="prof-highlight">Benefit is greatest early</mark> (within 12 hours of symptom onset), and relatively few patients receive systemic fibrinolytics, because the catheterization laboratory is preferred where available [slide 65].</p>
  </div>

  <h4 class="subsub">Other antithrombotic agents [slide 66]</h4>
  <table>
    <tr><th>Class</th><th>Place in therapy</th></tr>
    <tr><td><strong>Glycoprotein IIb/IIIa inhibitors</strong></td><td><strong>Not routinely recommended before percutaneous coronary intervention</strong></td></tr>
    <tr><td><strong>P2Y12 receptor antagonists</strong></td><td>Used <strong>before percutaneous coronary intervention</strong> and as <strong>clot prophylaxis with stent placement</strong></td></tr>
    <tr><td><strong>Heparins</strong></td><td>Used <strong>together with fibrinolysis or antiplatelet agents</strong></td></tr>
  </table>
  <p>Slide 67 pictures a coronary stent: a balloon catheter carries it into the narrowed artery and it is left
  expanded in place (percutaneous coronary intervention with stent placement).</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 1:03:43 of the recording: <em>&ldquo;Glycoprotein 2b3a inhibitors&hellip; another anti-platelet type of drug along with your ADP receptor blockers, [which] are also called P2Y12&hellip; whenever a stent gets placed that&rsquo;s foreign material&hellip; patients who go home on stents will need to be on some kind of anti-platelet therapy sometimes indefinitely.&rdquo;</em></p>
    <p><mark class="prof-highlight">Stent placement means antiplatelet therapy afterwards</mark>, sometimes indefinitely; P2Y12 receptor antagonists are used before intervention and with stents, and heparins accompany fibrinolysis or antiplatelet agents [slide 66].</p>
  </div>

  <h4 class="subsub">Non-ST-elevation acute coronary syndrome: how it differs [slide 68]</h4>
  <ul>
    <li>Early treatment is similar to treatment of ST-elevation myocardial infarction.</li>
    <li><strong>Fibrinolytics are not recommended</strong>, because the bleeding risk outweighs the benefit. This covers the fibrinolytic agents on slide 64: alteplase, reteplase and tenecteplase are not recommended in non-ST-elevation acute coronary syndrome.</li>
    <li><strong>Enoxaparin is preferred over heparin</strong>, based on studies. Enoxaparin is a low-molecular-weight heparin and the slide&rsquo;s &ldquo;heparin&rdquo; is unfractionated heparin; the preference comes from older studies, and current guidelines accept either.</li>
    <li><strong>Glycoprotein IIb/IIIa inhibitors are used more commonly</strong> than in ST-elevation myocardial infarction.</li>
  </ul>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p style="margin-top:2px">At 1:04:40 of the recording: <em>&ldquo;Treatment for NSTEMI is going to be similar to MI, it&rsquo;s just less use of fibrinolytics and then more use for things like your 2b3a inhibitors and enoxaparin.&rdquo;</em></p>
    <p><mark class="prof-highlight">Non-ST-elevation acute coronary syndrome: same early drugs, fewer fibrinolytics</mark> (not recommended), and more glycoprotein IIb/IIIa inhibitors and enoxaparin [slide 68].</p>
  </div>

  <h3 class="sub" id="mi-monitor">5.9 &middot; Objectives 8&ndash;10 &mdash; Interactions, monitoring and patient education</h3>

  <h4 class="subsub">Interactions (Objective 8)</h4>
  <table>
    <tr><th>Combination</th><th>What happens</th></tr>
    <tr><td><strong>Nitrates with sildenafil, tadalafil or vardenafil</strong></td><td><strong>Hypotension, and myocardial infarction or stroke</strong>; contraindicated [slides 26, 33 and 54]</td></tr>
    <tr><td><strong>Calcium channel blockers with CYP3A4 (cytochrome P450 3A4) substrates, inhibitors or inducers</strong></td><td>The slide lists CYP3A4 interactions as a precaution [slide 23]</td></tr>
    <tr><td><strong>Non-dihydropyridine with a beta blocker</strong></td><td>Listed as a precaution [slide 23]; the dihydropyridine is the usual partner for a beta blocker [slide 22]</td></tr>
    <tr><td><strong>Fibrinolytic with heparin or antiplatelet agents</strong></td><td>Used together on purpose [slide 66]; bleeding is the main risk of fibrinolytics [slide 65]</td></tr>
  </table>
  <p>The slides name <strong>no drug-food and no drug-herb interactions</strong> for these drugs.</p>

  <h4 class="subsub">Protocols and monitoring (Objective 9)</h4>
  <table>
    <tr><th>Topic</th><th>What the slides give</th></tr>
    <tr><td>Stable angina, stepwise</td><td>Aspirin, lipid-lowering therapy and sublingual nitroglycerin for everyone; a beta blocker after a myocardial infarction; an angiotensin-converting enzyme inhibitor with diabetes or left ventricular dysfunction; beta blocker, calcium channel blocker or long-acting nitrate for daily symptoms; combine if symptoms persist; a third agent calls for further workup [slides 36 and 38]</td></tr>
    <tr><td>Acute chest pain</td><td>Sublingual nitroglycerin; <strong>call emergency medical services if there is no relief five minutes after the first dose</strong> [slide 27]; aspirin at the first signs of chest pain [slide 52]</td></tr>
    <tr><td>Beta blockers</td><td>Monitor heart rate, blood sugar and lipids [slide 19]</td></tr>
    <tr><td>Calcium channel blockers</td><td>Monitor relief of symptoms, and heart rate for non-dihydropyridines [slide 24]</td></tr>
    <tr><td>Long-acting nitrates</td><td>A nitrate-free interval each day [slides 31 and 32]</td></tr>
  </table>

  <h4 class="subsub">Patient education (Objective 10)</h4>
  <table>
    <tr><th>Drug</th><th>What to tell the patient</th></tr>
    <tr><td><strong>Beta blockers</strong></td><td>Do not stop suddenly; expect dizziness and fatigue [slide 19]</td></tr>
    <tr><td><strong>Calcium channel blockers</strong></td><td>Expect dizziness and constipation [slide 24]</td></tr>
    <tr><td><strong>Short-acting nitrates</strong></td><td>Warn about orthostatic hypotension; store in the original packaging in a cool, dry place; replace tablets 3 to 6 months after opening (older rule, see 5.4); apply or spray under the tongue; call emergency medical services if there is no relief five minutes after the first dose [slides 27 and 28]</td></tr>
    <tr><td><strong>Long-acting nitrates</strong></td><td>12 hours on and 12 hours off for ointment and patch; wipe off the previous ointment dose before applying the next; keep the ointment covered with the applicator paper; expect headache, flushing and postural hypotension [slide 31]</td></tr>
    <tr><td><strong>Nitrates and erectile dysfunction drugs</strong></td><td>Counsel patients taking a nitrate, such as isosorbide mononitrate, to avoid combining it with sildenafil, tadalafil or vardenafil; the combination can cause hypotension, myocardial infarction or stroke [slide 33]</td></tr>
    <tr><td><strong>Aspirin in chest pain</strong></td><td>Chew and swallow at the first signs of chest pain [slide 52]</td></tr>
  </table>
</section>
'''
