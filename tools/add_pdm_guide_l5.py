#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add PDM I section 5 (Chemistry Panels, Renal Function, Electrolytes).

Instructional Objectives are quoted VERBATIM from the PAJ 5600 syllabus,
including its a-i lettering and roman sub-items, per [[guide_verbatim_io_rule]].
The slide's own objective list happens to match here, but the syllabus is the
source.

FOLDS IN THE 26 AUGUST RECORDING (Prof. Reynolds, two 50-minute segments),
read from Notability's transcript. It settles three things the deck alone
leaves open:

  1. She expects the ANION GAP to be calculated, and gave 8 to 12 aloud.
  2. She does NOT want the filtration rate or the corrected sodium computed --
     "I don't need you to calculate that or know that just yet, but know OF it",
     and she reaches for MedCalc for the sodium.
  3. She never asks anyone to recall a reference range: "we ALWAYS give you
     reference ranges." That is why the three places this deck disagrees with
     its own fishbone are SHOWN side by side here rather than silently resolved.

Idempotent: fenced in <!--PDML5--> and stripped before reinsert.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
GUIDE = os.path.join(DIR, "pdm-exam-1-study-guide.html")
IMGDIR = os.path.join(DIR, "pdm-exam-1-l5-images")
ACC5 = "#69406c"


def fig(slug, caption, slide):
    path = os.path.join(IMGDIR, slug + ".png")
    assert os.path.exists(path), "missing figure %s -- run extract_pdm_l5_figures.py" % slug
    return ('<figure class="fig"><img src="pdm-exam-1-l5-images/%s.png" decoding="async" '
            'alt="Lecture 5 slide %d figure."><figcaption>%s '
            '<span class="cite">Lecture 5 &middot; Slide %d</span></figcaption></figure>'
            % (slug, slide, caption, slide))


SEC5 = """
<section class="deck" id="chemistry-panels">
  <h2 class="deck-title">5 &middot; Chemistry Panels, Renal Function and Electrolytes</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 5: Chemistry Panels, Renal Function, and Electrolytes</p>
    <ol type="a">
      <li>Explain the components of a chemistry panel.</li>
      <li>Discuss the physiological role of: i. Sodium &middot; ii. Potassium &middot; iii. Chloride &middot; iv. Bicarbonate &middot; v. Glucose &middot; vi. BUN &middot; vii. Creatinine</li>
      <li>Discuss basic liver function studies included in chemistry testing.</li>
      <li>Interpret abnormal chemistry values and their clinical significance.</li>
      <li>Compare and contrast laboratory patterns seen in: i. Renal disorders &middot; ii. Hepatic disorders &middot; iii. Metabolic disorders</li>
      <li>Explain the relationship between electrolyte abnormalities and acid-base disorders.</li>
      <li>Discuss indications for ordering chemistry panels.</li>
      <li>Correlate chemistry findings with other diagnostic modalities when appropriate.</li>
      <li>Explain laboratory evaluation of fluid and electrolyte homeostasis.</li>
    </ol>
  </div>

  <div class="callout prof">
    <p><strong>What she said about numbers, on 26 August.</strong>
    <em>&ldquo;The hard and fast memorize these numbers, we don&rsquo;t do that to you, because
    it&rsquo;s gonna depend on the lab, it&rsquo;s gonna depend on the person, and so we
    <strong>always give you reference ranges</strong>.&rdquo;</em> And again:
    <em>&ldquo;There&rsquo;s not anything I need you to memorize number-wise &hellip; but it is
    helpful for you to kind of have an idea &mdash; sodium should be around 140.&rdquo;</em></p>
    <p>So learn the <strong>direction</strong> of abnormality and the rough figure. This matters
    more than usual here, because <strong>this deck states three ranges two different ways</strong>
    &mdash; see the table below. You are not expected to adjudicate between them.</p>
    <p><strong>What she does want calculated: the anion gap.</strong>
    <em>&ldquo;You really quick and dirty, calculate your anion gap, and our normal range is
    8 to 12.&rdquo;</em> What she does <em>not</em> want calculated: the glomerular filtration
    rate &mdash; <em>&ldquo;I don&rsquo;t need you to calculate that or know that just yet, but
    know <strong>of</strong> it&rdquo;</em> &mdash; and the corrected sodium, which she does with
    UpToDate or MedCalc rather than by hand.</p>
  </div>

  <h3 class="sub" id="l5-panels">5.1 &middot; Objective a &mdash; What is on which panel</h3>
  <p>A chemistry panel is a blood test measuring <strong>metabolites, electrolytes and kidney
  markers</strong>, and in its expanded form <strong>liver and protein markers</strong> as well.
  It gives a snapshot of chemical balance, metabolism and organ function. Reynolds' framing: a
  panel is like a group of consultants &mdash; you can call on them individually, but you are
  meant to read them <em>as a whole</em>.</p>

  <table class="tbl">
    <tr><th>Panel</th><th>Tests</th><th>Components</th></tr>
    <tr><td><b>Basic metabolic panel</b><br><span class="muted">&ldquo;chem-7&rdquo;, &ldquo;chem-8&rdquo;</span></td><td>8</td>
        <td>Glucose, calcium, sodium, potassium, chloride, carbon dioxide (bicarbonate), blood urea nitrogen, creatinine</td></tr>
    <tr><td><b>Comprehensive metabolic panel</b><br><span class="muted">&ldquo;chem-14&rdquo;</span></td><td>14</td>
        <td>All eight of the above <b>plus</b> albumin, total protein, alkaline phosphatase, alanine transaminase, aspartate aminotransferase, bilirubin</td></tr>
  </table>
  <p><strong>Chem-7 versus chem-8 is calcium</strong> &mdash; the chem-8 includes it. The
  comprehensive panel's addition is <strong>the liver panel plus total protein and albumin</strong>.
  Order the comprehensive one when you need a fuller picture of liver and nutritional protein
  status; a basic panel is enough for electrolytes, glucose and renal screening.</p>

  <p>Grouped by what they tell you: <strong>metabolic fuel</strong> &mdash; glucose;
  <strong>electrolytes and acid-base</strong> &mdash; sodium, potassium, chloride, bicarbonate;
  <strong>kidney function and waste</strong> &mdash; blood urea nitrogen, creatinine;
  <strong>mineral</strong> &mdash; calcium; <strong>liver and protein</strong>, comprehensive panel
  only &mdash; albumin, total protein, alkaline phosphatase, alanine transaminase, aspartate
  aminotransferase, bilirubin.</p>

  @@FISHBONE@@

  <p>The fishbone is bedside shorthand: <strong>position on the diagram identifies the test</strong>,
  so no label is written. Reynolds flagged what it leaves out &mdash; <em>&ldquo;this fishbone also
  includes the general normal ranges, but what it doesn&rsquo;t have are the <strong>units</strong>
  &hellip; depending on where you practice will determine what the units are.&rdquo;</em></p>

  <div class="callout warn">
    <p><strong>Two abbreviation traps she called out.</strong> On a panel, <strong>Cr means
    creatinine, not chromium</strong>, and <strong>BUN is blood urea nitrogen</strong>, not boron,
    uranium and nitrogen. She also drew the line on where shorthand belongs: <em>&ldquo;Do we
    abbreviate in our electronic notes? Absolutely not. We write out sodium &hellip; you&rsquo;ll
    literally write out millimetres of mercury.&rdquo;</em> Shorthand is for handwritten bedside
    notes and older records.</p>
  </div>

  <h3 class="sub" id="l5-ranges">5.2 &middot; Where this deck disagrees with itself</h3>
  <p>Three reference ranges appear twice in the deck with different numbers &mdash; once on a
  teaching slide, once on the fishbone picture. Both are shown here rather than picking one,
  because she supplies ranges on the exam and no question can turn on the difference.</p>
  <table class="tbl">
    <tr><th>Analyte</th><th>Teaching slide</th><th>Fishbone image</th><th>Agree?</th></tr>
    <tr><td>Bicarbonate</td><td>~22&ndash;29</td><td>22&ndash;28 on the panel; 22&ndash;26 in the blood-gas column</td><td>no</td></tr>
    <tr><td>Glucose</td><td>~70&ndash;99 fasting</td><td>70&ndash;120</td><td>no</td></tr>
    <tr><td>Blood urea nitrogen</td><td>~7&ndash;20</td><td>7&ndash;18</td><td>no</td></tr>
    <tr><td>Creatinine</td><td>~0.6&ndash;1.2</td><td>0.6&ndash;1.2</td><td><b>yes</b></td></tr>
  </table>
  <p>Reason to keep in view generally: a normal range is <strong>the mean plus or minus two
  standard deviations</strong>, so about <strong>2.5 per cent of healthy people fall outside it by
  chance</strong> &mdash; and <strong>a normal value does not exclude disease</strong>. Confirm a
  borderline abnormality before an extensive workup, and read every value against history,
  medications and supplements, alcohol and examination.</p>

  <h3 class="sub" id="l5-electrolytes">5.3 &middot; Objective b(i&ndash;iv) &mdash; The electrolytes</h3>
  <p><strong>Sodium</strong> is the <strong>major extracellular cation</strong> and its salts are
  the major determinant of extracellular osmolality. The serum level is a balance between oral
  intake and renal excretion. The single most useful idea in this lecture:
  <strong>an abnormal sodium is a water problem first</strong> &mdash; ask whether there is too
  much or too little free water before asking about salt. As free body water rises the sodium is
  diluted; the kidneys compensate by <strong>conserving sodium and excreting water</strong>.
  Serum sodium reflects <em>water balance</em>, controlled by thirst and antidiuretic hormone;
  <em>total-body</em> sodium, via the renin&ndash;angiotensin&ndash;aldosterone system, governs
  extracellular volume.</p>

  <p><strong>Potassium</strong> is the <strong>major intracellular cation</strong> and the key
  determinant of membrane electrical potential, especially in neuromuscular tissue. Small serum
  fluctuations carry large consequences, and <strong>both hyperkalaemia and hypokalaemia can cause
  life-threatening arrhythmias</strong>. It is excreted by the kidneys <strong>with no
  reabsorption</strong>, so it must be replaced by diet or supplementation or the level drops
  rapidly. Regulation is by <strong>aldosterone</strong> at the distal tubule and collecting duct,
  plus <strong>transcellular shifts</strong> driven by insulin, acid-base status and
  catecholamines &mdash; which is why the potassium in diabetic ketoacidosis can mislead.</p>

  <p><strong>Chloride</strong> is the major extracellular anion and <strong>follows sodium to
  maintain electrical neutrality</strong>. Alone it says little; with the other electrolytes it
  reports acid-base balance and hydration. It is reciprocal with bicarbonate: when carbon dioxide
  and hydrogen ions rise, bicarbonate moves out of the cell and <strong>chloride shifts back
  in</strong>. A <strong>low chloride with a high bicarbonate suggests metabolic alkalosis</strong>,
  classically from vomiting; the opposite pairing gives hyperchloraemic non-gap acidosis.</p>

  <p><strong>Bicarbonate</strong> is the <strong>primary extracellular buffer</strong> and helps
  transport carbon dioxide. It is reported on the panel as <strong>&ldquo;CO<sub>2</sub>&rdquo;</strong>
  &mdash; total carbon dioxide, which is mostly serum bicarbonate. <strong>Low means metabolic
  acidosis</strong> and is the trigger to calculate the anion gap; <strong>high means metabolic
  alkalosis</strong>.</p>

  @@BUFFER@@

  <h3 class="sub" id="l5-kidney">5.4 &middot; Objective b(v&ndash;vii) &mdash; Glucose, urea nitrogen and creatinine</h3>
  <p><strong>Glucose</strong> is the body's main fuel, lowered by insulin and raised by glucagon
  and the counter-regulatory hormones, with a gluconeogenic contribution from the kidney. Always
  interpret it against the <strong>fasting or non-fasting state</strong>. Marked hyperglycaemia
  <strong>lowers the measured sodium by dilution</strong> and drives osmolality.</p>

  <p><strong>Blood urea nitrogen</strong> is a nitrogenous waste product of protein metabolism,
  <strong>produced by the liver and cleared by the kidneys</strong>. It rises with reduced
  clearance but is <strong>non-specific</strong> &mdash; dehydration, gastrointestinal bleeding,
  high protein intake and catabolic states all raise it. <strong>Creatinine</strong> is a waste
  product of muscle creatine metabolism, filtered by the kidneys, and <strong>more specific</strong>.
  It rises as filtration falls, but is influenced by <strong>muscle mass, age and sex</strong>, so
  a normal creatinine can mask a reduced filtration rate in an elderly or cachectic patient.</p>

  <p>Read the two together. A <strong>ratio above 20 to 1 suggests a prerenal cause</strong>;
  below that points to intrinsic renal disease. The estimated filtration rate is derived from
  creatinine &mdash; <strong>know of it, and do not calculate it</strong>.</p>

  <h3 class="sub" id="l5-liver">5.5 &middot; Objective c &mdash; The liver studies</h3>
  <div class="callout">
    <p><strong>The asterisk on her slide title is the point.</strong> Aspartate aminotransferase,
    alanine transaminase, alkaline phosphatase and bilirubin are markers of <strong>liver
    INJURY, not liver function</strong>. They are liver tests, or liver chemistries. The tests
    that actually measure <em>function</em> are <strong>albumin, prothrombin time and
    bilirubin</strong>.</p>
  </div>
  <table class="tbl">
    <tr><th>Test</th><th>What it marks</th><th>The catch</th></tr>
    <tr><td>Aspartate aminotransferase</td><td>Hepatocellular injury</td><td>Also in cardiac and skeletal muscle, kidney and brain &mdash; <b>less liver-specific</b></td></tr>
    <tr><td>Alanine transaminase</td><td>Hepatocellular injury</td><td>Primarily liver &mdash; <b>more specific</b></td></tr>
    <tr><td>Alkaline phosphatase</td><td>Cholestasis, bile duct obstruction</td><td>Also bone, placenta, intestine &mdash; confirm hepatic origin with <b>gamma-glutamyl transferase</b></td></tr>
    <tr><td>Albumin</td><td>Synthetic function</td><td>Half-life ~3 weeks, so a low value means <b>chronic</b> disease; may also drop in severe illness</td></tr>
    <tr><td>Prothrombin time and ratio</td><td>Synthetic function</td><td><b>Most sensitive functional marker</b> &mdash; can prolong within 24 hours. Factors II, VII, IX, X</td></tr>
    <tr><td>Total bilirubin</td><td>Conjugation and excretion</td><td>A breakdown product of red blood cells</td></tr>
  </table>

  <p><strong>Four patterns of hepatic abnormality:</strong></p>
  <table class="tbl">
    <tr><th>Pattern</th><th>Definition</th><th>Causes</th></tr>
    <tr><td>Hepatocellular</td><td>Transaminases raised out of proportion to alkaline phosphatase</td><td>Viral hepatitis, fatty liver disease, alcohol, drugs, ischaemia</td></tr>
    <tr><td>Cholestatic</td><td>Alkaline phosphatase raised out of proportion to the transaminases</td><td>Bile duct obstruction, gallstones, primary biliary cholangitis</td></tr>
    <tr><td>Mixed</td><td>Both raised</td><td>&mdash;</td></tr>
    <tr><td>Isolated hyperbilirubinaemia</td><td>Bilirubin up, enzymes normal</td><td>Gilbert syndrome, haemolysis</td></tr>
  </table>
  <p><strong>Three shortcuts worth having:</strong> a ratio of aspartate aminotransferase to
  alanine transaminase <strong>above 2 to 1 suggests alcoholic liver disease</strong>; a raised
  aspartate aminotransferase <strong>without</strong> a raised alanine transaminase points to
  cardiac or skeletal muscle rather than liver; and transaminases <strong>in the thousands</strong>
  narrow to just three causes &mdash; <strong>viral, ischaemia, toxins</strong>. Magnitude bands:
  mild under 5&times;, moderate 5&ndash;15&times;, severe over 15&times; the upper limit.</p>

  <h3 class="sub" id="l5-patterns">5.6 &middot; Objectives d &amp; e &mdash; Reading a panel, and the three patterns</h3>
  <p>Work through an abnormal comprehensive panel <strong>by organ system, in this order</strong>:
  electrolytes and acid-base (then calculate the anion gap) &rarr; renal, with the urea nitrogen to
  creatinine ratio &rarr; glucose &rarr; liver &rarr; minerals.</p>
  <table class="tbl">
    <tr><th>Disorder</th><th>Characteristic pattern</th></tr>
    <tr><td><b>Renal</b></td><td>&uarr; urea nitrogen, &uarr; creatinine, &darr; filtration rate; &plusmn; &uarr; potassium, &uarr; phosphate, &darr; calcium, metabolic acidosis; albuminuria</td></tr>
    <tr><td><b>Hepatic</b></td><td>&uarr; transaminases (hepatocellular) or &uarr; alkaline phosphatase and bilirubin (cholestatic); &darr; albumin and &uarr; prothrombin time in advanced disease</td></tr>
    <tr><td><b>Metabolic</b> (ketoacidosis)</td><td>&uarr; glucose, &darr; bicarbonate, &uarr; anion gap, low pH; &plusmn; &uarr; potassium <b>despite total-body depletion</b>; corrected sodium</td></tr>
  </table>
  <p>Two overlaps to know by name: <strong>hepatorenal syndrome</strong> shows liver and kidney
  failure together, and <strong>diabetic ketoacidosis</strong> produces electrolyte and renal
  derangements at once. <strong>Cardiorenal syndrome</strong> is the cardiac equivalent.</p>

  <h3 class="sub" id="l5-acidbase">5.7 &middot; Objective f &mdash; Electrolytes and acid-base, and the anion gap</h3>
  <p>These cannot be separated: they are <strong>regulated by the same renal transport
  mechanisms</strong> and <strong>physically coupled by electroneutrality</strong>.</p>
  <ul>
    <li><strong>Potassium and pH.</strong> Acidosis drives potassium <em>out</em> of cells, raising
    the serum level; alkalosis drives it <em>in</em>, lowering it. Running the other way,
    potassium depletion <strong>increases renal acid secretion</strong>.</li>
    <li><strong>Chloride.</strong> Losing it, as in vomiting, raises the strong ion difference and
    produces a <strong>metabolic alkalosis</strong>.</li>
  </ul>
  <div class="callout">
    <p><strong>The anion gap &mdash; she does want this one calculated.</strong></p>
    <p style="font-size:1.05em"><b>Anion gap = sodium &minus; (chloride + bicarbonate)</b>
    &nbsp; normal <b>8&ndash;12</b> mEq/L</p>
    <p>Extended form, adding potassium: <b>(sodium + potassium) &minus; (chloride + bicarbonate)</b>,
    normal <b>10&ndash;14</b>.</p>
    <p><b>Raised gap</b> &rarr; unmeasured acids: methanol, uraemia, diabetic ketoacidosis,
    paraldehyde and propylene glycol, isoniazid and iron, lactic acidosis, ethylene glycol,
    salicylates. <b>Normal gap</b> &rarr; bicarbonate loss from gut or kidney, i.e.
    hyperchloraemic acidosis.</p>
    <p><b>Correct the gap for a low albumin</b> &mdash; add about 2.5 for every 1 g/dL the
    albumin has fallen, because albumin is itself an unmeasured anion.</p>
  </div>

  <h3 class="sub" id="l5-fluid">5.8 &middot; Objectives g&ndash;i &mdash; Ordering, correlating, and fluid balance</h3>
  <p><strong>Order a panel for:</strong> screening metabolic, liver and renal status; monitoring
  diabetes, chronic kidney disease, hypertension and liver disease; drugs with renal or hepatic
  toxicity or electrolyte effects; symptoms of fatigue, weakness, oedema, jaundice, confusion,
  nausea and vomiting; acute illness with dehydration or a suspected acid-base disorder; and
  assessment of volume status.</p>
  <p><strong>Chemistry rarely stands alone.</strong> Abnormal liver tests &rarr; ultrasound first.
  A reduced filtration rate or albuminuria &rarr; urine studies and renal ultrasound; chronicity
  needs <strong>at least three months</strong>, and cystatin C confirms the rate when accuracy
  matters. Ketoacidosis &rarr; add ketones with beta-hydroxybutyrate, a venous blood gas,
  urinalysis, an electrocardiogram (for the potassium) and a complete blood count. Hyponatraemia
  &rarr; add serum osmolality with urine sodium and osmolality.</p>
  <table class="tbl">
    <tr><th>Test</th><th>What it tells you about fluid and electrolyte balance</th></tr>
    <tr><td>Serum sodium</td><td>The primary indicator of <b>water</b> balance, not salt content. Hyponatraemia usually means water excess</td></tr>
    <tr><td>Serum osmolality</td><td>Separates true hypotonic hyponatraemia from the pseudo- and hypertonic forms; normal tonicity ~275&ndash;285 mOsm/kg</td></tr>
    <tr><td>Urine sodium and osmolality</td><td>Localises it: <b>&lt;20</b> suggests hypovolaemia; <b>&gt;40</b> with concentrated urine suggests the syndrome of inappropriate antidiuretic hormone secretion</td></tr>
    <tr><td>Urea nitrogen : creatinine</td><td>Volume status and perfusion &mdash; a ratio <b>&gt;20</b> suggests prerenal hypovolaemia</td></tr>
    <tr><td>Potassium</td><td>Links to acid-base and adrenal function</td></tr>
  </table>
  <div class="callout warn">
    <p><strong>Three pitfalls.</strong> <b>Hyperglycaemia lowers the measured sodium</b> by about
    1.6&ndash;2 mEq/L per 100 mg/dL of glucose above normal &mdash; use a corrected sodium, from a
    calculator. <b>Pseudohyponatraemia</b> from severe hyperlipidaemia or hyperproteinaemia gives a
    falsely low sodium <em>with a normal osmolality</em>. And <b>the number alone never gives the
    diagnosis</b> &mdash; read sodium alongside volume status.</p>
  </div>

  <h3 class="sub" id="l5-case">5.9 &middot; The vomiting case &mdash; why the two cannot be separated</h3>
  <p>A 25-year-old woman, three days of intractable nausea and vomiting. The panel shows
  <strong>low sodium, low potassium, low chloride, a raised bicarbonate and alkalaemia</strong>.</p>
  <p><strong>Why it persists:</strong> volume, potassium and chloride depletion together force the
  kidney to reabsorb sodium and bicarbonate, which <em>maintains</em> the alkalosis after the
  vomiting has stopped. <strong>What fixes it:</strong> replacing sodium, chloride and potassium
  &mdash; saline with potassium chloride. Not bicarbonate, and not an antiemetic alone. Her
  speaker note calls this <em>&ldquo;the single best illustration that you cannot separate
  electrolytes from acid-base.&rdquo;</em></p>
</section>
"""

TOC = """  <a class="top-link" href="#chemistry-panels">5 &middot; Chemistry Panels &amp; Electrolytes</a>
  <a class="sub-link" href="#l5-panels">5.1 What is on which panel</a>
  <a class="sub-link" href="#l5-ranges">5.2 Where the deck disagrees</a>
  <a class="sub-link" href="#l5-electrolytes">5.3 The electrolytes</a>
  <a class="sub-link" href="#l5-kidney">5.4 Glucose, urea nitrogen, creatinine</a>
  <a class="sub-link" href="#l5-liver">5.5 The liver studies</a>
  <a class="sub-link" href="#l5-patterns">5.6 Reading a panel</a>
  <a class="sub-link" href="#l5-acidbase">5.7 Acid-base &amp; the anion gap</a>
  <a class="sub-link" href="#l5-fluid">5.8 Ordering &amp; fluid balance</a>
  <a class="sub-link" href="#l5-case">5.9 The vomiting case</a>
"""

TY = """    "chemistry-panels": [
      {q:"An abnormal sodium should raise which question first?",
       o:["Is there too much or too little free water?","Is there too much or too little salt?",
          "Is kidney function normal?","Was the sample haemolysed?"],a:0,
       why:"Serum sodium reflects water balance, not total-body sodium. Ask the water question first."},
      {q:"Sodium 140, chloride 100, bicarbonate 24. What is the anion gap, and how do you read it?",
       o:["16 &mdash; above the normal range","16 &mdash; within the normal range",
          "24 &mdash; above the normal range","40 &mdash; markedly raised"],a:0,
       why:"140 &minus; (100 + 24) = 16, and the normal range is 8 to 12, so this is a raised gap."},
      {q:"Which liver test is the most sensitive marker of FUNCTION?",
       o:["Prothrombin time and its ratio","Alanine transaminase","Alkaline phosphatase","Albumin"],a:0,
       why:"It can prolong within 24 hours of severe injury. Albumin's three-week half-life makes it a marker of chronic disease instead."},
      {q:"A low chloride with a high bicarbonate suggests what?",
       o:["Metabolic alkalosis, such as from vomiting","Raised-gap metabolic acidosis",
          "Respiratory acidosis","Normal-gap acidosis from bicarbonate loss"],a:0,
       why:"Chloride and bicarbonate move reciprocally to preserve electroneutrality."},
      {q:"A urea nitrogen to creatinine ratio above 20 to 1 points to which kind of cause?",
       o:["Prerenal","Intrinsic renal","Postrenal obstructive","Hepatic"],a:0,
       why:"Above 20 to 1 is the deck's separator for a prerenal cause."},
      {q:"Which does Professor Reynolds NOT want you to calculate?",
       o:["The glomerular filtration rate","The anion gap",
          "The extended anion gap with potassium","The urea nitrogen to creatinine ratio"],a:0,
       why:"Her words: &ldquo;I don't need you to calculate that or know that just yet, but know OF it.&rdquo; The anion gap she does want calculated."},
      {q:"Transaminases in the thousands narrow the cause to which three?",
       o:["Viral, ischaemia, toxins","Alcohol, gallstones, fatty liver",
          "Gilbert syndrome, haemolysis, obstruction","Sepsis, heart failure, pancreatitis"],a:0,
       why:"That magnitude is the discriminator; her speaker note names exactly these three."},
      {q:"What maintains the alkalosis after the vomiting has stopped?",
       o:["Volume, potassium and chloride depletion drive renal sodium and bicarbonate reabsorption",
          "The lungs retain carbon dioxide to compensate","The liver stops clearing bicarbonate",
          "Continued loss of gastric acid"],a:0,
       why:"The renal response is what keeps it going, which is why replacing all three corrects it."}
    ],
"""

FIGS = {
    "@@FISHBONE@@": [("fishbone",
                      "The fishbone shorthand. <b>Slide 4 extracts as completely blank text</b> "
                      "&mdash; this picture is the only copy of the reference set in the deck. "
                      "Note it carries ranges but no units.", 4)],
    "@@BUFFER@@": [("co2-buffer",
                    "The carbon dioxide and bicarbonate buffer system: lungs excreting carbon "
                    "dioxide on the left, kidney producing bicarbonate on the right, normal pH "
                    "7.35&ndash;7.45 between them.", 12)],
}


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for o, cl in (("<!--PDML5-->", "<!--/PDML5-->"),
                  ("<!--PDMTOC5-->", "<!--/PDMTOC5-->"),
                  ("<!--PDMTY5-->", "<!--/PDMTY5-->")):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(cl), "", src, flags=re.S)

    body = SEC5
    for token, items in FIGS.items():
        assert token in body, "figure token %s unused" % token
        body = body.replace(token, "\n".join(fig(s, cap, sl) for s, cap, sl in items))
    assert "@@" not in body, "unfilled figure token"

    end = src.index("</main>")
    src = src[:end] + "<!--PDML5-->" + body + "<!--/PDML5-->\n\n" + src[end:]

    navend = src.rindex("</nav>")
    src = src[:navend] + "<!--PDMTOC5-->\n" + TOC + "<!--/PDMTOC5-->\n" + src[navend:]

    tyanchor = "  var TEST_YOURSELF = {\n"
    assert src.count(tyanchor) == 1, "TEST_YOURSELF object not found once"
    src = src.replace(tyanchor, tyanchor + "<!--PDMTY5-->\n" + TY + "<!--/PDMTY5-->\n", 1)

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li",
                "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 5: %d subsections, %d figures, %d test-yourself questions"
          % (len(re.findall(r'<h3 class="sub" id="l5-', src)),
             len(re.findall(r'src="pdm-exam-1-l5-images/', src)),
             TY.count("{q:")))


if __name__ == "__main__":
    main()
