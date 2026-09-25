# -*- coding: utf-8 -*-
"""Content for the Clinical Pathophysiology I Exam 2 study guide.

Data module for build_cp_e2_guide.py: TOC, the two lecture sections and the
TEST_YOURSELF banks. Kept apart from the builder so a content edit never has to
touch the page skeleton.

SCOPE -- mechanism only (clin_path_exam_spec). No treatment, no drug, no "next
step". The one place Lecture 7's recording strays into management (repair of a
large abdominal aortic aneurysm) is deliberately left out; the size figures stay
because rupture RISK by size is mechanism.

SOURCES
  Lecture 6: "6. Cardiac Pathophysiology  for posting.pptx" (72 slides). NO
    RECORDING exists for this lecture, so nothing in section 6 is marked as
    professor-emphasized; there is nothing to mark it from.
  Lecture 7: "SV Vascular Pathophys I Fall 2026.pptx" (39 slides) plus the
    51-minute recording of 2026-09-15, read in TWO transcriptions (ours and
    Notability's) and cross-examined. Slide wins on facts; the recording
    decides emphasis and supplies the explanations the slides only assert.

US spelling throughout (us_spelling); the io-box is the syllabus verbatim.
"""

L6 = "6. Cardiac Pathophysiology for posting.pptx"
L7 = "SV Vascular Pathophys I Fall 2026.pptx"


def fig(src, w, h, alt, cap, cite):
    return ('<figure class="fig"><img loading="lazy" decoding="async" width="%d" height="%d" '
            'src="%s" alt="%s"><figcaption>%s <span class="cite">%s</span></figcaption></figure>'
            % (w, h, src, alt, cap, cite))


TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#cardiac">6 &middot; Cardiac Pathophysiology</a>
  <a href="#l6-anatomy">6.1 Objectives a &amp; b &mdash; Anatomy and function</a>
  <a href="#l6-lipo">6.2 Objective c &mdash; Lipoproteins</a>
  <a href="#l6-molecular">6.3 Objective d &mdash; Molecular mechanisms</a>
  <a href="#l6-chd">6.4 Objective e &mdash; Coronary heart disease</a>
  <a href="#l6-plaque">6.5 Objective f &mdash; Atherosclerosis and plaque</a>
  <a href="#l6-ischemia">6.6 Objective g &mdash; Cardiac ischemia</a>
  <a href="#l6-syndromes">6.7 Objective h &mdash; Coronary syndromes</a>
  <a href="#l6-angina">6.8 Objective i &mdash; Angina pectoris</a>
  <a href="#l6-acs">6.9 Objective j &mdash; Acute coronary syndrome</a>
  <a href="#l6-valves">6.10 Objective k &mdash; Valve disease</a>
  <a href="#l6-infective">6.11 Objective l &mdash; Infective cardiopathies</a>
  <a href="#l6-bp">6.12 Objective m &mdash; Blood pressure regulation</a>
  <a href="#l6-conduction">6.13 Objective n &mdash; Conduction system</a>
  <a href="#l6-structural">6.14 Objective o &mdash; Structural pathologies</a>
  <a class="top-link" href="#vascular">7 &middot; Vascular Pathophysiology</a>
  <a href="#l7-recording">7.0 What the recording adds</a>
  <a href="#l7-anatomy">7.1 Objective a &mdash; Anatomy</a>
  <a href="#l7-function">7.2 Objective b &mdash; Functions</a>
  <a href="#l7-intima">7.3 Objective c &mdash; The wall and its injury response</a>
  <a href="#l7-size">7.4 Objective c &mdash; Two mechanisms, three sizes</a>
  <a href="#l7-bp">7.5 Objective c &mdash; Blood pressure and hypertension</a>
  <a href="#l7-arteriosclerosis">7.6 Objective c &mdash; Arteriosclerosis</a>
  <a href="#l7-athero">7.7 Objective c &mdash; Atherosclerosis</a>
  <a href="#l7-aneurysm">7.8 Objective c &mdash; Aneurysm and dissection</a>
  <a href="#l7-other">7.9 Objective c &mdash; Dysplasia, vasculitis, Raynaud, fistula</a>
  <a href="#l7-veins">7.10 Objective c &mdash; Veins and thrombosis</a>
</nav>'''

D6 = "cp-exam-2-l6-images/"
D7 = "cp-exam-2-l7-images/"

CARDIAC = '''
<section class="deck" id="cardiac">
  <h2 class="deck-title">6 &middot; Cardiac Pathophysiology</h2>
  <p class="lecturer">Lecture 6 &middot; 14 September 2026 &middot; deck title slide: &ldquo;Lecture
  Prepared by: Matthew Ward, DMSc, MBA, PA-C&rdquo;. The calendar lists Dr. Rappa for this session;
  who delivered it is not confirmed.</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol type="a">
      <li>Review the anatomy of the heart</li>
      <li>Review the function of cardiac structures</li>
      <li>Review the different lipoproteins</li>
      <li>Describe the molecular mechanisms of common cardiopathies</li>
      <li>Compare and contrast the various etiologies and risk factors for coronary heart disease</li>
      <li>Describe the pathological processes and risk factors for the formation of coronary atherosclerosis and plaques</li>
      <li>Explain the pathophysiology of cardiac ischemia</li>
      <li>Compare and contrast the etiologies and pathophysiological processes of coronary syndromes</li>
      <li>Describe the etiologies and pathophysiological processes for angina pectoris</li>
      <li>Compare and contrast the etiologies and pathophysiological processes of acute coronary syndrome</li>
      <li>Compare and contrast the etiologies and pathophysiological processes of valvular stenosis, regurgitation, and prolapse</li>
      <li>Compare and contrast the etiologies and pathophysiological processes of infective cardiopathies</li>
      <li>Compare and contrast the pathophysiology of blood pressure regulation</li>
      <li>Compare and contrast the pathophysiology of the cardiac conduction system</li>
      <li>Compare and contrast the pathophysiology of structural cardiac pathologies</li>
    </ol>
  </div>
  <div class="callout"><strong>No recording of this lecture exists</strong>, so nothing in this section
  is marked as professor-emphasized. Every fact here comes off the slides, and with no signposting to
  go on, the fair plan is to study all fifteen objectives evenly.</div>
  <div class="callout"><strong>The deck and the syllabus list different objectives.</strong> The deck&rsquo;s
  own objectives slide has thirteen (a&ndash;m), ending with <em>pericarditidies</em> and
  <em>myopathies</em>. The syllabus has fifteen (a&ndash;o), and the list above is the syllabus
  verbatim. Two of the syllabus objectives have little or nothing behind them in this deck:
  <b>(m) blood pressure regulation</b> is taught in Lecture 7, slides 19&ndash;21 (section 7.5), and
  <b>(n) the conduction system</b> has no slide at all (section 6.13 collects what the deck does say
  about rhythm).</div>

  <h3 class="sub" id="l6-anatomy">6.1 &middot; Objectives a &amp; b &mdash; Anatomy of the heart and function of cardiac structures</h3>
  <p>The anatomy in this deck is the <b>coronary circulation</b>, because every disease that follows
  is a problem of supply through it. Three slides (5&ndash;7) are pictures only:</p>
  <table>
    <tr><th>Vessel</th><th>Branches shown on the slides</th></tr>
    <tr><td>Left main coronary artery</td><td>Divides into the <b>left anterior descending artery</b>
    (the anterior interventricular branch, running in the anterior interventricular sulcus) and the
    <b>circumflex branch</b></td></tr>
    <tr><td>Right coronary artery</td><td>Runs in the coronary sulcus; gives the <b>marginal
    branch</b> and the <b>posterior interventricular branch</b></td></tr>
  </table>
  ''' + fig(D6 + "coronary-arteries.jpg", 566, 737,
            "Anterior view of the heart with the right and left coronary arteries and their branches labeled.",
            "The two coronary arteries and the branches you need by name: left coronary, circumflex, "
            "anterior interventricular; right coronary, marginal, posterior interventricular. Section 6.9 "
            "puts percentages on these: nearly every infarct is in the left ventricular wall, and the "
            "left anterior descending territory is the commonest.",
            "Lecture 6 &middot; Slide 6") + '''
  ''' + fig(D6 + "coronary-schematic.jpg", 352, 227,
            "Schematic of coronary anatomy labeled right coronary artery, left main, left anterior descending and left circumflex.",
            "The same tree reduced to four labels: right coronary artery, left main, left anterior "
            "descending, left circumflex.",
            "Lecture 6 &middot; Slide 7") + '''
  <h4 class="subsub">Function: what sets the heart&rsquo;s oxygen demand</h4>
  <p>Slide 31 names the four determinants of <b>workload</b>: <b>heart rate, preload, afterload and
  contractility</b>. An increase in any one of them increases the demand for oxygen. That list is the
  demand half of every ischemia question (section 6.6).</p>
  <h4 class="subsub">The Frank&ndash;Starling law (slide 62)</h4>
  <p>The more the ventricle fills during diastole, the greater the volume it ejects in the systole that
  follows; in a healthy heart the end-diastolic volume will equal the stroke volume. The force any
  single muscle fiber generates is <b>proportional to its initial sarcomere length</b> (preload), and
  that stretch is set by the end-diastolic volume. Maximal force comes at an initial sarcomere length of
  <b>2.6 micrometers</b>, a length rarely exceeded in the normal heart.</p>
  <div class="pearl">The slide sits just before the dilated cardiomyopathy slide for a reason: a
  ventricle that dilates keeps stretching its fibers, and the law describes the benefit of stretch only
  up to a point. Section 6.14 picks this up.</div>

  <h3 class="sub" id="l6-lipo">6.2 &middot; Objective c &mdash; The different lipoproteins</h3>
  <p>Plaques are made of lipid, and lipid travels in the blood bound to specific proteins. Which
  lipoprotein carries it changes the risk (slide 12):</p>
  <table>
    <tr><th>Lipoprotein</th><th>Rich in</th><th>Effect on atherosclerosis risk</th></tr>
    <tr><td>Low-density lipoprotein (LDL)</td><td>Cholesterol</td><td><b>Highest</b> risk</td></tr>
    <tr><td>Very-low-density lipoprotein (VLDL)</td><td>Triglycerides</td><td><b>Increases</b> risk</td></tr>
    <tr><td>High-density lipoprotein (HDL)</td><td>&mdash;</td><td><b>Decreases</b> risk: carries
    cholesterol <b>back to the liver</b>, clearing it away from plaque</td></tr>
  </table>
  <p><b>Familial hypercholesterolemia</b> (slide 13) is the most common form of genetic
  hyperlipidemia. The defect is in the <b>low-density lipoprotein receptor on liver cells</b>, so the
  liver cannot remove cholesterol from the bloodstream. <b>High-fat diets</b> are the acquired
  counterpart listed on the same slide.</p>
  <p>Lecture 7 adds a fourth name: <b>lipoprotein(a)</b>, an altered form of low-density lipoprotein
  linked to coronary and cerebrovascular disease, whose risk is independent of total cholesterol
  (section 7.7).</p>

  <h3 class="sub" id="l6-molecular">6.3 &middot; Objective d &mdash; Molecular mechanisms of common cardiopathies</h3>
  <p>The deck has no single slide for this objective; it is answered across the lecture. Every
  disease here reduces to one of four mechanisms:</p>
  <table>
    <tr><th>Where</th><th>Mechanism</th><th>Examples in this lecture</th></tr>
    <tr><td>Coronary arteries</td><td>Oxygen <b>supply falls below demand</b></td><td>Stable,
    variant and unstable angina; myocardial infarction</td></tr>
    <tr><td>Valves</td><td>Extra <b>pressure work</b> (stenosis) or extra <b>volume work</b>
    (regurgitation)</td><td>Mitral and aortic stenosis and regurgitation; prolapse</td></tr>
    <tr><td>Myocardium</td><td>Inflammation, dilation, hypertrophy or stiffening of the muscle
    itself</td><td>Myocarditis; dilated, hypertrophic, restrictive cardiomyopathy</td></tr>
    <tr><td>Pericardium</td><td>External <b>compression</b> or <b>encasement</b> that limits
    filling</td><td>Effusion and tamponade; constrictive pericarditis</td></tr>
  </table>
  <h4 class="subsub">Homocysteine (slide 11)</h4>
  <p>An intermediary amino acid formed in the conversion of <b>methionine to cysteine</b>, with
  primarily <b>atherogenic and prothrombotic</b> properties. The vascular injury it causes:
  intimal thickening, elastic lamina disruption, smooth muscle hypertrophy, marked platelet
  accumulation, and formation of a platelet-enriched occlusive thrombus.</p>
  <h4 class="subsub">The molecular picture of a plaque (slide 19)</h4>
  ''' + fig(D6 + "atherosclerosis-initiation.jpg", 400, 846,
            "Three-panel diagram: initiation of atherosclerosis, early lesion, and vulnerable plaque, with labeled cells and mediators.",
            "Read top to bottom. <b>(a) Initiation:</b> atherogenic factors (low-density lipoprotein "
            "cholesterol, diabetes, hypertension, smoking) cause endothelial dysfunction; adhesion "
            "molecules (MCP-1, monocyte chemoattractant protein 1; VCAM, vascular cell adhesion "
            "molecule) recruit monocytes, and vascular smooth muscle cells activate. <b>(b) Early "
            "lesion:</b> foam cells form the fatty streak, and growth factors such as PDGF "
            "(platelet-derived growth factor) drive smooth muscle migration and proliferation. <b>(c) "
            "Vulnerable plaque:</b> a thin fibrous cap (smooth muscle cells dying by apoptosis), a lipid "
            "core full of foam cells, intense inflammation at the shoulder, and collagenases, "
            "elastases and stromelysins degrading the cap until it ruptures.",
            "Lecture 6 &middot; Slide 19") + '''

  <h3 class="sub" id="l6-chd">6.4 &middot; Objective e &mdash; Etiologies and risk factors for coronary heart disease</h3>
  <p><b>Definition (slide 4).</b> Coronary heart disease, also called ischemic heart disease or
  coronary artery disease, is the <b>insufficient delivery of oxygenated blood to the myocardium
  because of atherosclerotic coronary arteries</b>. About <b>50%</b> of those who die of
  cardiovascular disease die of it. When the heart&rsquo;s metabolic demand for oxygen exceeds the
  supply, the myocardium becomes ischemic; ischemia causes abnormal heart function and abnormal
  cardiac rhythms, and if prolonged, irreversible damage.</p>
  <table>
    <tr><th>Etiology (slides 8&ndash;9)</th><th>How it causes ischemia</th></tr>
    <tr><td><b>Atherosclerosis</b> &mdash; behind almost all coronary heart disease</td><td>Progressive
    narrowing of the lumen, which predisposes to the processes that precipitate ischemia:
    <b>thrombosis, coronary vasospasm, endothelial cell dysfunction</b></td></tr>
    <tr><td>Abnormalities of the microcirculation</td><td>Abnormal regulation of the small cardiac
    vessels by their endothelial cells, so control of the cardiac blood supply is abnormal</td></tr>
    <tr><td>Uncommon: decreased oxygen content of blood</td><td>A respiratory cause; the arteries are
    open but the blood carries too little</td></tr>
    <tr><td>Uncommon: poor perfusion</td><td>Hypotension or hypovolemia; too little pressure to drive
    flow</td></tr>
  </table>
  <table>
    <tr><th>Major risk factors (slide 10)</th><th>Probable risk factors</th></tr>
    <tr><td>Age &middot; family history &middot; abnormal lipids &middot; cigarette smoking &middot;
    hypertension &middot; diabetes mellitus &middot; obesity</td><td>Male sex &middot; homocysteine
    &middot; high-sensitivity C-reactive protein</td></tr>
  </table>
  <div class="pearl">Lecture 7 lists the atherosclerosis risk factors again and adds that <b>family
  history is the most important</b> of them (slide 24), and that C-reactive protein is now used in
  cardiovascular risk stratification. See section 7.7.</div>

  <h3 class="sub" id="l6-plaque">6.5 &middot; Objective f &mdash; Formation of coronary atherosclerosis and plaques</h3>
  <p>The sequence on slides 14&ndash;16, in order:</p>
  <ol>
    <li><b>Injury to the endothelial cells</b> starts it &mdash; from chronic hemodynamic wall stress,
    toxins, inflammation or hyperlipidemia.</li>
    <li>The injured endothelium becomes <b>more permeable</b>, and <b>leukocytes are recruited</b>.</li>
    <li><b>Low-density lipoprotein leaks through</b> the endothelial wall, where cells and macrophages
    <b>oxidize</b> it.</li>
    <li><b>Oxidized lipid damages</b> both the wall and the smooth muscle cells; more macrophages
    arrive and keep engulfing lipid.</li>
    <li>Lipid-filled macrophages become <b>foam cells</b>. Both kinds of macrophage release
    inflammatory mediators and growth factor, attracting more leukocytes and <b>stimulating smooth
    muscle proliferation</b>.</li>
    <li>Excess lipid and debris pool inside the wall to form the <b>lipid core</b>.</li>
    <li>Plaques with <b>large lipid cores are fragile and rupture</b>, exposing subendothelial
    proteins, which starts platelet aggregation and thrombus formation; thrombotic material can be
    incorporated, enlarging the plaque.</li>
    <li>Over time <b>collagen and fibrin form a cap</b>, which makes the plaque more stable.</li>
    <li>Plaques grow over years until they begin to occlude the lumen. At <b>75% occlusion, blood
    flow is compromised</b>.</li>
  </ol>
  ''' + fig(D6 + "plaque-formation-steps.jpg", 1000, 412,
            "Diagram of a vessel wall with lettered steps a to f from activated platelet to plaque formation.",
            "The same sequence in six lettered steps: (a) an activated platelet, (b) deposition of "
            "chemokines on the endothelium, (c) adhesion of monocytes, (d) monocytes migrate into the "
            "wall and transform into macrophages, (e) macrophages ingest low-density lipoprotein, (f) "
            "plaque formation.",
            "Lecture 6 &middot; Slide 18") + '''
  <h4 class="subsub">What makes a plaque rupture</h4>
  <p>Slide 16 lists what makes a plaque vulnerable to erosion or rupture: <b>intra-plaque
  inflammation, a large core with a thin cap, superficial platelet aggregation, a ruptured cap, and
  severe stenosis</b>. Slides 26&ndash;28 give the reasons:</p>
  <ul>
    <li>Risk depends on the <b>composition</b> of the plaque and the <b>mechanical stresses</b> on it.
    A <b>vulnerable plaque has a large necrotic core under a thin fibrous cap</b>.</li>
    <li>A <b>triggering event</b> of enough magnitude and duration compromises it &mdash; for example
    the <b>shear force of blood flowing at high velocity through a severe stenosis</b>.</li>
    <li>The diseased wall may be rich in <b>vasa vasorum capillaries</b>. Their thin walls hemorrhage,
    depositing blood products and <b>building pressure inside the plaque</b>.</li>
  </ul>
  <p>The consequence (slide 29): <b>thrombosis</b>, and <b>emboli</b> carried downstream to block
  smaller vessels.</p>
  ''' + fig(D6 + "vulnerable-plaque-features.jpg", 600, 393,
            "Histologic cross-section of a coronary artery with a ruptured plaque and clot, beside a list of vulnerable plaque features.",
            "<b>This slide&rsquo;s list exists only in the picture</b>; the deck has no text version of "
            "it. The six features of the vulnerable plaque: <b>large lipid core, thin fibrous cap, rich "
            "in macrophages, increased MMPs (matrix metalloproteinases), poor in smooth muscle cells, "
            "low-grade stenosis</b>. Note the last one: the plaque that ruptures need not be the one "
            "narrowing the artery most.",
            "Lecture 6 &middot; Slide 24") + '''
  ''' + fig(D6 + "stable-vs-vulnerable.png", 1088, 768,
            "Two cross-sections of arteries: a stable plaque with a thick fibrous cap and a vulnerable plaque with a thin cap and a clot.",
            "A frame from the slide&rsquo;s animation. <b>Stable:</b> thick fibrous cap, small lipid "
            "core, plenty of smooth muscle cells. <b>Vulnerable:</b> thin fibrous cap, large lipid core, "
            "plenty of macrophages, and a thrombus in the lumen. Smooth muscle cells build the cap; "
            "macrophages digest it.",
            "Lecture 6 &middot; Slide 25") + '''
  <div class="callout">Lecture 7 covers atherosclerosis again, from the vessel wall&rsquo;s side
  (section 7.7). The Lecture 7 presenter said that where the two lectures disagree the textbook
  prevails, and that there would be no trick questions comparing them.</div>

  <h3 class="sub" id="l6-ischemia">6.6 &middot; Objective g &mdash; The pathophysiology of cardiac ischemia</h3>
  <p>Ischemia starts when <b>oxygen supply is insufficient for the demand of the cardiac cells</b>.
  With less oxygen, <b>less ATP (adenosine triphosphate) is formed</b> (slide 30). Every cause falls
  on one side of the balance:</p>
  <table>
    <tr><th>Supply falls: coronary perfusion impaired by</th><th>Demand rises: workload increased by</th></tr>
    <tr><td>Large atherosclerotic plaques &middot; acute platelet aggregation, then thrombosis
    &middot; vasospasm &middot; abnormal microcirculation &middot; poor perfusion pressures</td>
    <td>Heart rate &middot; preload &middot; afterload &middot; contractility</td></tr>
  </table>
  <ul>
    <li>When plaque builds over years, the heart develops <b>collateral circulation</b> to keep the
    muscle perfused (slide 31) &mdash; one reason a slow occlusion can be tolerated and a sudden one
    cannot.</li>
    <li>Myocardial oxygen consumption and myocardial blood flow correspond <b>nearly linearly</b>;
    <b>metabolic signals</b> are the principal determinants of oxygen delivery to the myocardium.</li>
  </ul>
  ''' + fig(D6 + "cardiac-ischemia.jpg", 355, 292,
            "Heart with a circled region of damaged muscle beside three coronary artery sections: normal, atherosclerosis, and atherosclerosis with blood clot.",
            "The progression in one image: a normal coronary artery, a narrowed atherosclerotic one, and "
            "one where a clot has formed on the plaque. The circled area on the heart is the muscle "
            "downstream that loses its supply.",
            "Lecture 6 &middot; Slide 32") + '''

  <h3 class="sub" id="l6-syndromes">6.7 &middot; Objective h &mdash; Coronary syndromes</h3>
  <p>Coronary syndromes are classified by the <b>severity and onset</b> of cardiac symptoms (slide 33):</p>
  <table>
    <tr><th>Chronic syndromes</th><th>Acute syndromes</th></tr>
    <tr><td>Stable angina &middot; ischemic cardiomyopathy</td><td>Unstable angina &middot;
    myocardial infarction</td></tr>
  </table>
  <p>The dividing line is mechanism: the chronic syndromes come from a fixed narrowing that fails only
  when demand rises; the acute ones come from <b>plaque rupture with acute thrombosis</b> (section 6.9).</p>

  <h3 class="sub" id="l6-angina">6.8 &middot; Objective i &mdash; Angina pectoris</h3>
  <p>Angina is <b>intermittent cardiac ischemia that is insufficient to kill cardiac cells</b>. It occurs
  under conditions that increase the heart&rsquo;s oxygen demand, and may cause insufficient pumping,
  leading to pulmonary congestion (slide 34).</p>
  <table>
    <tr><th>Type</th><th>Mechanism</th><th>Trigger</th></tr>
    <tr><td><b>Stable (typical)</b> &mdash; the most common</td><td>Stenotic atherosclerotic vessels
    reduce flow to a critical level</td><td>Increased cardiac workload: perfusion is adequate at rest
    and inadequate under load</td></tr>
    <tr><td><b>Prinzmetal (variant)</b></td><td><b>Vasospasm</b> is the probable mechanism; its cause
    is unknown</td><td>Unpredictable; <b>no relation to physical or emotional stress</b>, even though
    plaques are present</td></tr>
    <tr><td><b>Unstable (crescendo)</b></td><td>May progress to acute ischemia</td><td>Classed with the
    acute coronary syndromes for that reason</td></tr>
  </table>

  <h3 class="sub" id="l6-acs">6.9 &middot; Objective j &mdash; Acute coronary syndrome</h3>
  <p>Acute coronary syndrome includes <b>both unstable angina and myocardial infarction</b>, because
  they are hard to distinguish clinically. In both, pain lasts longer than typical angina, and
  <b>plaque rupture with acute thrombosis</b> is thought to occur (slide 37).</p>
  <p><b>Myocardial infarction</b> results from <b>prolonged or total disruption of blood flow</b>,
  causing cell death by <b>necrosis or apoptosis</b>. The initiating feature (slide 38):</p>
  <ol>
    <li>Thrombosis on top of an <b>ulcerated or cracked atherosclerotic plaque</b></li>
    <li>Platelets adhere to the ruptured plaque, forming a <b>platelet plug</b></li>
    <li>The <b>clotting cascade</b> is activated</li>
    <li>A growing thrombus <b>occludes the vessel</b></li>
  </ol>
  <p>What the occlusion does depends on <b>collateral circulation, workload, and length of time</b>. A
  typical infarct has several zones of cells in various stages of necrosis. <b>Complete occlusion</b>
  follows a pattern (slide 39):</p>
  <table>
    <tr><th>Time after complete occlusion</th><th>What happens</th></tr>
    <tr><td>Immediately</td><td>ATP is depleted</td></tr>
    <tr><td>A few minutes</td><td>The muscle can no longer contract</td></tr>
    <tr><td><b>After 30 minutes</b></td><td><b>Irreversible cell necrosis</b></td></tr>
  </table>
  <p><b>Where infarcts happen (slide 40).</b> Nearly all are in the <b>left ventricular walls</b>:</p>
  <table>
    <tr><th>Artery occluded</th><th>Share of infarcts</th></tr>
    <tr><td>Left anterior descending</td><td><b>40&ndash;50%</b></td></tr>
    <tr><td>Right coronary</td><td>30&ndash;40%</td></tr>
    <tr><td>Left circumflex</td><td>15&ndash;20%</td></tr>
  </table>
  <p><b>How the infarcted area changes (slide 40):</b></p>
  <table>
    <tr><th>Time</th><th>Gross change</th></tr>
    <tr><td>6 hours</td><td>Gross examination first becomes positive</td></tr>
    <tr><td>18&ndash;24 hours</td><td>Area becomes paler</td></tr>
    <tr><td>Then</td><td>Yellowish and soft, with a border of red vascular connective tissue</td></tr>
    <tr><td>1&ndash;2 weeks</td><td>Necrotic tissue is taken away</td></tr>
    <tr><td>By 6 weeks</td><td>Tough fibrous scar</td></tr>
  </table>

  <h3 class="sub" id="l6-valves">6.10 &middot; Objective k &mdash; Valvular stenosis, regurgitation and prolapse</h3>
  <p>Valves are damaged by <b>inflammation with scarring</b> (mitral or aortic), <b>calcification</b>
  (mitral or aortic), or <b>congenital</b> defects (any valve). The altered hemodynamics raise cardiac
  workload, and heart failure may result (slide 42).</p>
  <table>
    <tr><th></th><th>Stenosis</th><th>Regurgitation (insufficiency)</th></tr>
    <tr><td>Definition</td><td>Failure of the valve to <b>open</b> completely</td><td>Inability of
    the valve to <b>close</b> completely</td></tr>
    <tr><td>Extra work</td><td><b>Pressure work</b>: blood forced through a smaller opening; a
    pressure gradient forms across the valve</td><td><b>Volume work</b>: blood flows back across the
    valve and must be pumped again</td></tr>
    <tr><td>Threshold / tempo</td><td>Hemodynamics affected at <b>50% closure</b>; progresses slowly,
    so the heart compensates by <b>myocardial cell hypertrophy</b></td><td>Acute regurgitation comes
    from <b>infection or papillary muscle rupture</b></td></tr>
    <tr><td>Primary causes</td><td>Post-inflammatory scarring from <b>rheumatic fever</b>; aging
    valvular <b>calcification</b></td><td><b>Rheumatic heart disease</b>; <b>infective
    endocarditis</b></td></tr>
  </table>
  <table>
    <tr><th>Lesion</th><th>Mechanism</th><th>Consequences</th></tr>
    <tr><td><b>Mitral stenosis</b> (slides 45&ndash;46)</td><td>Abnormal left atrial to left ventricular
    gradient <b>during diastole</b>: atrial pressure stays higher than ventricular pressure, and the
    gradient grows as the stenosis worsens</td><td>Left atrial congestion, raised left atrial pressure,
    raised pulmonary pressures, <b>decreased left ventricular stroke volume</b>. Atrial enlargement and
    hypertrophy &rarr; pulmonary hypertension &rarr; right-sided hypertrophy and failure. With
    progression: <b>atrial fibrillation</b> (from increased atrial volume), atrial enlargement,
    <b>atrial clots</b></td></tr>
    <tr><td><b>Mitral regurgitation</b> (slide 48)</td><td>Backflow from ventricle to atrium <b>during
    systole</b>; a <b>high afterload increases the regurgitation</b></td><td>Raised left atrial volume
    and pressure; the left ventricle pumps a greater volume to keep an effective stroke volume, so
    <b>both atrium and ventricle dilate and hypertrophy</b>; if severe, left-sided heart failure</td></tr>
    <tr><td><b>Mitral valve prolapse</b> (slide 49)</td><td><b>Ballooning</b> of the mitral valve
    into the left atrium during systole</td><td>Usually no symptoms; in a few cases enough to cause
    some mitral regurgitation</td></tr>
    <tr><td><b>Aortic stenosis</b> (slides 50&ndash;51)</td><td>Most commonly <b>age-related
    calcification</b>, common with a <b>bicuspid aortic valve</b>; rheumatic disease is uncommon and
    affects children and young adults. Obstruction to outflow during systole creates a left ventricular
    to aortic gradient</td><td>The ventricle generates high systolic pressures and slowly
    <b>hypertrophies</b>; hypertrophy plus high pressure predispose to <b>ischemia and angina</b>; may
    lead to left heart failure</td></tr>
    <tr><td><b>Aortic regurgitation</b> (slide 53)</td><td>Incompetent valve leaks from aorta back into
    the left ventricle <b>during diastole</b>; causes similar to mitral regurgitation, with <b>aortic
    root dilation</b> (from aging or connective tissue disease) a common one</td><td>Left ventricle
    <b>hypertrophies and dilates</b>; <b>diastolic pressures fall</b>; high workload can lead to
    left-sided heart failure</td></tr>
  </table>
  <div class="pearl"><b>Timing is the whole trick.</b> Mitral stenosis and aortic regurgitation are
  problems <b>in diastole</b>; mitral regurgitation, prolapse and aortic stenosis are problems <b>in
  systole</b>. Ask which chamber is filling or emptying across the bad valve, and the consequence
  follows.</div>
  <div class="callout">Slide 50 prints aortic stenosis as clinically apparent in those <b>&ldquo;over 79
  years of age&rdquo;</b>. That is the figure as the slide gives it.</div>
  ''' + fig(D6 + "mitral-stenosis.jpg", 250, 253,
            "Gross specimen of a stenotic mitral valve seen from above, with an arrow pointing to nodular deposits on the leaflets.",
            "A stenotic mitral valve viewed from the atrium: thickened, fused leaflets leave a narrow "
            "opening, and the arrow marks the nodular deposits along the edge. This is the fixed "
            "orifice that sets up the diastolic gradient.",
            "Lecture 6 &middot; Slide 47") + '''
  ''' + fig(D6 + "aortic-stenosis.jpg", 350, 257,
            "Gross specimen of an aortic valve with three cusps filled with heaped-up nodular calcium.",
            "Calcific aortic stenosis: the three cusps are stiffened by heaped-up nodular deposits, so "
            "they cannot open fully in systole.",
            "Lecture 6 &middot; Slide 52") + '''

  <h3 class="sub" id="l6-infective">6.11 &middot; Objective l &mdash; Infective cardiopathies</h3>
  <table>
    <tr><th>Condition</th><th>Mechanism</th></tr>
    <tr><td><b>Rheumatic heart disease</b> (slides 54&ndash;55)</td><td>An uncommon but serious
    consequence of <b>rheumatic fever</b>, the acute inflammatory disease that follows infection with
    <b>group A beta-hemolytic streptococcus</b>. The damage is an <b>immune attack caused by
    cross-reactivity</b>, not the organism itself, with a genetic predisposition seen in certain HLA
    (human leukocyte antigen) types. The inflammation involves <b>all layers of the heart</b> (carditis).
    In the endocardium: valvular swelling, erosions, platelet aggregation and fibrin on the leaflets, and
    with progression <b>scarring and shortening</b> of the valve structures.</td></tr>
    <tr><td><b>Infective endocarditis</b> (slide 56)</td><td><b>Invasion and colonization</b> of
    endocardial structures by pathogens, causing inflammation. <b>Invasion of the bloodstream is a
    prerequisite.</b> <b>Vegetations</b> form &mdash; microorganisms enmeshed in fibrin &mdash; which
    grow large, interfere with valve function and predispose to <b>emboli</b>. Most common organisms:
    <i>Streptococcus</i> strains and <i>Staphylococcus aureus</i>.</td></tr>
    <tr><td><b>Subacute infective endocarditis</b> (slide 57)</td><td>Insidious onset in people with a
    <b>preexisting valve pathology</b>. The organisms are <b>less virulent</b> &mdash; the slide lists
    <i>S. aureus</i>, <i>Streptococcus</i> and <i>Candida</i> &mdash; and are <b>not virulent enough to
    attack a healthy endocardium</b>; the damaged valve is what lets them in.</td></tr>
    <tr><td><b>Myocarditis</b> (slide 59)</td><td>Etiologies include microbes, immune-related disease and
    physical agents; <b><i>Coxsackievirus</i> is the most common cause in North America</b>. Mechanism
    in section 6.14.</td></tr>
    <tr><td><b>Acute pericarditis</b> (slide 70)</td><td>Most cases are idiopathic, and most of those
    are <b>viral</b>; the inflammation damages the pericardium. Section 6.14.</td></tr>
  </table>
  <div class="callout"><strong>Check against the textbook.</strong> Slide 57 lists <i>Staphylococcus
  aureus</i> among the less virulent organisms of <em>subacute</em> endocarditis. The course text,
  Robbins, generally pairs highly virulent organisms such as <i>S. aureus</i> with the acute form.
  Answer from the slide if asked in the slide&rsquo;s terms, and know the general rule: the less
  virulent the organism, the more it depends on an already-damaged valve.</div>

  <h3 class="sub" id="l6-bp">6.12 &middot; Objective m &mdash; Blood pressure regulation</h3>
  <p>No slide in the Cardiac deck teaches this objective. <b>Lecture 7 does</b>, on slides
  19&ndash;21: blood pressure is set by <b>cardiac output and vascular resistance</b>, resistance is
  regulated at the arterioles, and a fall in pressure triggers the renin&ndash;angiotensin&ndash;aldosterone
  response. The full treatment is in <a href="#l7-bp">section 7.5</a>.</p>
  <p>Where pressure appears in this deck, it is as <b>load on the heart</b>: afterload is one of the
  four determinants of oxygen demand (slide 31); a <b>high afterload increases mitral
  regurgitation</b> (slide 48); in aortic regurgitation <b>diastolic pressures fall</b> (slide 53); and
  poor perfusion pressure is one cause of ischemia (slide 30).</p>

  <h3 class="sub" id="l6-conduction">6.13 &middot; Objective n &mdash; The cardiac conduction system</h3>
  <p><b>No slide in the deck covers the conduction system.</b> The deck mentions rhythm in only two
  places:</p>
  <ul>
    <li>Ischemia can lead to <b>abnormal cardiac rhythms</b> as well as abnormal heart function
    (slide 4).</li>
    <li>Mitral stenosis leads, with progression, to <b>atrial fibrillation due to the increased
    atrial volume</b> (slide 46).</li>
  </ul>
  <p>Nothing further is added here, so that nothing on this page goes beyond the deck. If the objective
  was covered aloud, those notes are the source.</p>

  <h3 class="sub" id="l6-structural">6.14 &middot; Objective o &mdash; Structural cardiac pathologies</h3>
  <h4 class="subsub">Myocarditis (slides 59&ndash;60)</h4>
  <p>Characterized by <b>inflammation, leukocyte infiltration and necrosis</b> of the myocardium. The
  picture: <b>left ventricular dysfunction</b>, general <b>dilation of all four chambers</b>, patchy or
  diffuse necrotic lesions, inflamed and edematous muscle with leukocyte infiltrates, and
  <b>endocardial structures that are usually normal</b>.</p>
  <h4 class="subsub">Cardiomyopathy (slides 61&ndash;65)</h4>
  <p>Some have known causes. Those of unknown cause are grouped by their <b>major pathophysiological
  feature</b>:</p>
  <table>
    <tr><th>Type</th><th>What the muscle does</th><th>Why the heart fails</th></tr>
    <tr><td><b>Dilated</b> (also called congested)</td><td>Dilation of one or both ventricles</td>
    <td>Cardiac failure with dilation. Factors: <b>alcohol, genetics, pregnancy, post-viral</b></td></tr>
    <tr><td><b>Hypertrophic</b></td><td>A thickened, <b>hyperkinetic</b> ventricular muscle mass</td>
    <td>Symptoms from <b>ventricular outflow obstruction</b> and <b>impaired diastolic filling</b></td></tr>
    <tr><td><b>Restrictive</b></td><td>A stiff, <b>fibrotic, rigid, noncompliant</b> ventricle; most
    related to a specific condition, for example <b>amyloidosis</b></td><td><b>Restricted diastolic
    filling</b> &rarr; low stroke volume &rarr; heart failure</td></tr>
  </table>
  <div class="pearl">Two of the three fail in <b>filling</b> (hypertrophic, restrictive); one fails in
  <b>emptying</b> (dilated). The Frank&ndash;Starling slide explains why dilation helps only so far.</div>
  <h4 class="subsub">Pericardial disease (slides 66&ndash;72)</h4>
  <p>Rarely primary; usually <b>secondary to another cause</b>. Whatever the cause, fluid accumulates
  in the pericardial sac and the pericardial structures become painfully inflamed.</p>
  <table>
    <tr><th>Pericardial effusion type</th><th>What it is and why</th></tr>
    <tr><td><b>Serous</b></td><td>A transudate, secondary to <b>heart failure</b> or
    <b>hypoproteinemia</b></td></tr>
    <tr><td><b>Serosanguinous</b></td><td>Serous fluid plus blood, after <b>blunt chest trauma, heart
    surgery or cardiopulmonary resuscitation</b></td></tr>
    <tr><td><b>Chylous</b></td><td>Lymph, from <b>obstruction to lymph drainage</b></td></tr>
    <tr><td><b>Blood</b> (hemopericardium)</td><td><b>Penetrating</b> cardiac trauma</td></tr>
  </table>
  <p>An effusion is by definition <b>non-inflammatory</b> fluid. <b>Cardiac tamponade</b> occurs when
  a large amount of pericardial fluid <b>compresses the heart chambers from outside</b> so that filling
  is impaired; it is life-threatening (slide 69).</p>
  <table>
    <tr><th>Pericarditis</th><th>Mechanism</th></tr>
    <tr><td><b>Acute</b></td><td>Mostly idiopathic, most of those viral; the inflammation damages the
    pericardium</td></tr>
    <tr><td><b>Chronic</b> (healed)</td><td>Healing of an acute form leaves chronic dysfunction; two
    principal types below</td></tr>
    <tr><td>Adhesive mediastinopericarditis</td><td>Follows suppurative or caseous pericarditis, or
    surgery. The sac is destroyed and the heart <b>adheres to the surrounding mediastinal
    structures</b>, so every beat pulls against them and <b>workload rises</b></td></tr>
    <tr><td><b>Constrictive pericarditis</b></td><td>Many causes unknown; can share the adhesive
    form&rsquo;s causes. The sac becomes dense, nonelastic, fibrous and scarred, and <b>encases the heart
    like a stiff cage, impairing diastolic filling</b></td></tr>
  </table>
  <div class="pearl"><b>Three ways to stop a heart filling, three different places:</b> fluid around it
  (tamponade), a scarred cage around it (constrictive pericarditis), or a stiff muscle within it
  (restrictive cardiomyopathy). The effect on filling is the same; the anatomy differs.</div>

  <button type="button" class="test-yourself-btn" style="--acc:#6e1f2f" onclick="window.openTestYourself('Test yourself — Cardiac Pathophysiology', TEST_YOURSELF.cardiac)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>6. Cardiac Pathophysiology for posting.pptx</em> (deck prepared
  by Matthew Ward, DMSc, MBA, PA-C). No lecture recording. Figures are reproduced from the lecture
  slides and each is cited to its slide.</footer>
</section>
'''

VASCULAR = '''
<section class="deck" id="vascular">
  <h2 class="deck-title">7 &middot; Vascular Pathophysiology</h2>
  <p class="lecturer">Lecture 7 &middot; 15 September 2026 &middot; deck title slide: &ldquo;Presented by
  Stacie Gopal, DMS, PA-C&rdquo;, &ldquo;Adapted from Lauren Reynolds, PA-C&rdquo;. The calendar row
  names Professor Reynolds; the deck&rsquo;s own wording is used here.</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <ol type="a">
      <li>Review the anatomy of the vascular system</li>
      <li>Review the functions of the components of the vascular system</li>
      <li>Describe the molecular mechanisms of common vascular pathologies</li>
    </ol>
  </div>
  <div class="callout">Objective (c) on the slide reads &ldquo;molecular mechanisms of vascular
  pathologies&rdquo;, without <em>common</em>. The syllabus wording is used above.</div>

  <h3 class="sub" id="l7-recording">7.0 &middot; What the recording adds</h3>
  <p>The 51-minute recording was read in two independent transcriptions and cross-examined. Both agree
  on everything below. Timestamps are minutes into the recording.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; stated in the lecture</span>
  <table>
    <tr><th>Said</th><th>What it means for the exam</th></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Do know that a consequence of atherosclerosis is
    peripheral arterial disease</mark>&hellip; an individual might experience claudication&hellip;
    because there&rsquo;s a lack of oxygenated blood supply to that musculature under increased
    demand.&rdquo;</em> [33:43]</td><td>The one explicit &ldquo;do know&rdquo; in the lecture. The
    mechanism: stenosis &rarr; ischemia that shows only when demand rises, exactly like stable angina in
    section 6.8.</td></tr>
    <tr><td><em>&ldquo;Notice the size of the arteries, because <mark class="prof-highlight">much of what
    we&rsquo;re going to be discussing today involves the large versus medium versus small</mark>.&rdquo;</em>
    [1:51]; <em>&ldquo;the take home point is that it affects different vessels based on their size and
    physiologic purpose.&rdquo;</em> [43:21]</td><td>The organizing principle of the whole lecture:
    <b>large elastic arteries &rarr; aneurysm; medium muscular arteries &rarr; atherosclerosis; small
    arteries and arterioles &rarr; hypertension</b> (section 7.4).</td></tr>
    <tr><td><em>&ldquo;Principal mechanisms of vascular disease, <mark class="prof-highlight">it&rsquo;s
    kind of easy, it&rsquo;s two things</mark>. It&rsquo;s either narrowing of the vessel&hellip; or
    weakening of the vessel, which would be dilation and rupture.&rdquo;</em> [22:08]</td><td>Sort every
    disease in this lecture into one of the two bins.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">An aneurysm means a weakening of the wall, it does
    not mean a rupture of the wall.</mark>&rdquo;</em> [38:55]</td><td>Answering a student&rsquo;s
    question: not all aneurysms rupture; the risk depends on size (section 7.8).</td></tr>
    <tr><td><em>&ldquo;You are held responsible for the textbook information too.&rdquo;</em> [21:59];
    <em>&ldquo;If there&rsquo;s any discrepancy&hellip; the textbook is going to be the rule to
    prevail&hellip; but <mark class="prof-highlight">I won&rsquo;t put any trick questions on the test
    trying to compare these two</mark>, I promise.&rdquo;</em> [33:27]</td><td>Said of the overlap with
    the Cardiac lecture on atherosclerosis. She pointed at the textbook&rsquo;s Figure 11.3 (the
    neointimal response) and its Key Concepts box (section 7.3).</td></tr>
  </table>
  </div>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Said to go light on</span>
  <ul>
    <li><b>Vasculitis:</b> <em>&ldquo;more than 20 forms&hellip; I just threw out a couple of examples
    there, but again this is not something we can dive into in tremendous detail today.&rdquo;</em>
    [43:15, 44:38]</li>
    <li><b>Mycotic aneurysm:</b> <em>&ldquo;These are very rare, but it&rsquo;s there for the sake of
    completeness.&rdquo;</em> [42:08]</li>
    <li><b>Atherosclerosis</b> was presented as a quick review, <em>&ldquo;because I know it was covered
    yesterday&rdquo;</em> [30:11]. Section 6.5 is the full version.</li>
  </ul>
  </div>
  <div class="callout"><strong>Two transcription slips, both corrected by the slide.</strong> Both
  transcriptions write the capillary&rsquo;s contractile cells as &ldquo;parasites&rdquo;; the slide 11
  figure labels them <b>pericytes</b>. And &ldquo;Mockingbird medial sclerosis&rdquo; is
  <b>M&ouml;nckeberg</b> medial sclerosis (slide 22).</div>

  <h3 class="sub" id="l7-anatomy">7.1 &middot; Objective a &mdash; Anatomy of the vascular system</h3>
  <p>The vascular system is a closed network of blood and lymph vessels. On the slide 3 overview, the
  numbered structures are 1 aorta, 2 pulmonary artery, 3 right heart, 4 left heart, 6 abdominal aorta
  (there is no 5). Slides 4 and 7 show the named arteries and veins, superficial and deep veins, and the
  <b>hepatic portal system</b>, where veins from the stomach and intestines enter the liver so that
  nutrients are processed and drugs metabolized on first pass.</p>
  <h4 class="subsub">From heart and back: the five components (slides 8&ndash;9)</h4>
  ''' + fig(D7 + "vessel-structure.jpg", 1100, 735,
            "Diagram of the circulation from aorta to large vein, with a cross-section of each vessel type and labels for high pressure, blood pressure control, gas and nutrient exchange and low pressure.",
            "Follow the loop clockwise from the heart: <b>elastic artery</b> (aorta; elastin fibers "
            "between smooth muscle), <b>muscular artery</b> (densely packed concentric smooth muscle), "
            "<b>arteriole</b> (labeled blood pressure control), <b>capillary</b> (endothelium and "
            "pericytes only; gas and nutrient exchange), then <b>post-capillary venule, medium vein, "
            "large vein</b>. Left side low pressure, right side high pressure: the walls thin as the "
            "pressure falls.",
            "Lecture 7 &middot; Slide 9") + '''
  <h4 class="subsub">The three layers (slide 10)</h4>
  <table>
    <tr><th>Layer</th><th>Structure</th></tr>
    <tr><td><b>Intima</b></td><td>A single layer of <b>endothelial cells on a basement membrane</b>, with
    a thin underlying layer of extracellular matrix</td></tr>
    <tr><td><b>Media</b></td><td>In elastic arteries such as the aorta, lamellar units of <b>elastin
    fibers and smooth muscle cells arranged like tree rings</b>, which <b>expand during systole and
    recoil during diastole</b></td></tr>
    <tr><td><b>Adventitia</b></td><td>Loose connective tissue for support; can carry nerve fibers; in
    large vessels it holds their own small arterioles (vasa vasorum) that perfuse the adventitia and
    part of the media</td></tr>
  </table>
  <p>All three layers are present in arteries and veins, though more clearly demarcated in the thicker
  arterial wall. The amount of smooth muscle and matrix in the media varies with the
  <b>hemodynamic demand</b> of the vessel&rsquo;s location. <b>Capillaries are the exception: they have
  no media.</b></p>
  <h4 class="subsub">Capillaries (slide 11)</h4>
  <p>A capillary is <b>equal to or slightly smaller than the diameter of a red blood cell</b> &mdash; in
  the lecture, roughly 5&ndash;10 micrometers against a red cell of 7&ndash;8. The lumen is lined with
  endothelium and has <b>no media</b>. Capillaries have a <b>large cross-sectional area and a low flow
  rate</b>; thin walls plus slow flow make exchange easy. Tissues with high metabolic rates,
  <b>myocardium and brain</b>, have the highest capillary density.</p>
  ''' + fig(D7 + "capillary-types.jpg", 343, 583,
            "Three capillary types drawn in section: continuous with pores, fenestrated with fenestrations, and sinusoidal with gaps and a discontinuous basement membrane.",
            "<b>Continuous</b> (least permeable; the blood&ndash;brain barrier), <b>fenestrated</b> "
            "(windows; kidney glomeruli, small intestine), <b>sinusoidal</b> (gaps, large fenestrations, "
            "discontinuous basement membrane; liver, bone marrow, spleen, endocrine glands). Note the "
            "<b>pericyte</b> wrapped around each one.",
            "Lecture 7 &middot; Slide 11") + '''

  <h3 class="sub" id="l7-function">7.2 &middot; Objective b &mdash; Functions of the components of the vascular system</h3>
  <table>
    <tr><th>Function of the vascular system (slide 5)</th><th></th></tr>
    <tr><td>Nutrients</td><td>Transported to tissues</td></tr>
    <tr><td>Waste products</td><td>Transported away from tissues</td></tr>
    <tr><td>Hormones</td><td>Transported from one part of the body to another</td></tr>
    <tr><td>Homeostasis</td><td>Balance in all tissue fluids, for the function of cells</td></tr>
  </table>
  <p><b>Two circulatory loops (slide 6).</b> <b>Pulmonary:</b> deoxygenated blood from the right heart
  to the lungs. <b>Systemic:</b> oxygenated blood from the left heart to the tissues, returning
  deoxygenated blood to the right heart. The naming rule she stopped on: an <b>artery carries blood away
  from the heart and a vein toward it</b>, which is why the pulmonary artery carries deoxygenated blood
  and the pulmonary vein oxygenated.</p>
  <table>
    <tr><th>Component (slide 8)</th><th>Function</th></tr>
    <tr><td>1 &middot; Arteries</td><td><b>High pressure</b>, strong walls, high-velocity flow</td></tr>
    <tr><td>2 &middot; Arterioles</td><td><b>Control conduits</b> for the release of blood into the
    capillaries &mdash; the principal points of resistance to flow (&ldquo;small but mighty&rdquo;)</td></tr>
    <tr><td>3 &middot; Capillaries</td><td><b>Exchange</b> of fluid, nutrients, electrolytes, hormones
    and wastes between blood and tissue</td></tr>
    <tr><td>4 &middot; Venules</td><td>Collect blood from capillaries and coalesce into larger veins</td></tr>
    <tr><td>5 &middot; Veins</td><td>Return blood to the heart; <b>major reservoir</b> of extra blood;
    <b>low pressure, thin walls</b></td></tr>
  </table>
  <p>Veins hold about <b>66% of the total blood volume</b> (slide 35), so maintaining that volume is a
  large part of maintaining blood pressure.</p>

  <h3 class="sub" id="l7-intima">7.3 &middot; Objective c &mdash; The healthy wall and its response to injury</h3>
  <table>
    <tr><th>Cell (slide 12)</th><th>What it does in health</th></tr>
    <tr><td><b>Endothelial cells</b> &mdash; specialized simple squamous epithelium lining the lumen</td>
    <td>Vessel homeostasis; a <b>nonthrombogenic surface</b> that keeps blood fluid; <b>modulates
    medial smooth muscle tone</b> and so vascular resistance; <b>metabolizes hormones such as
    angiotensin</b>; regulates inflammation; affects the growth of other cells, particularly smooth
    muscle</td></tr>
    <tr><td><b>Smooth muscle cells</b> &mdash; the predominant cell of the media</td><td>Normal vascular
    repair, and a large part in atherosclerosis: they <b>proliferate</b> when stimulated,
    <b>synthesize collagen, elastin, proteoglycans, growth factors and cytokines</b>, and are
    responsible for <b>vasoconstriction and vasodilation</b></td></tr>
  </table>
  <h4 class="subsub">Intimal thickening (slides 13&ndash;15)</h4>
  <p>Vascular injury with endothelial dysfunction or loss stimulates <b>smooth muscle cell recruitment
  and proliferation into the intima</b>:</p>
  <ul>
    <li><b>Endothelial cells</b> migrate in from uninjured areas or come from precursor cells in the
    blood &mdash; and <b>nitric oxide production falls</b>.</li>
    <li><b>Smooth muscle cells</b> (or circulating precursors) migrate into the intima, proliferate and
    synthesize extracellular matrix &mdash; <b>the primary pathology of neointimal hyperplasia</b>.</li>
    <li><b>Platelets activate</b> (a thrombus forms) and <b>leukocytes are recruited</b> (the
    inflammatory cascade begins).</li>
  </ul>
  <p>The result is a <b>thickened intima that narrows the lumen</b> and compromises flow. This
  neointimal response happens with <b>any form of vascular damage, regardless of cause</b>, and involves
  wall remodeling and loss of lumen patency.</p>
  <div class="pearl"><b>Why falling nitric oxide matters twice</b> (her question to the room, [18:48]):
  nitric oxide is a vasodilator. So the injured vessel is narrowed by the thickened intima <em>and</em>
  constricted by the loss of dilation &mdash; a &ldquo;twofold problem&rdquo;.</div>
  ''' + fig(D7 + "neointimal-response.jpg", 1100, 393,
            "Diagram of a vessel wall showing smooth muscle cells crossing the internal elastic lamina into the intima, dividing, and laying down extracellular matrix.",
            "The textbook&rsquo;s Figure 11.3, in three numbered steps: (1) recruitment of smooth muscle "
            "cells or their precursors into the intima, across the internal elastic lamina; (2) smooth "
            "muscle cell mitosis; (3) elaboration of extracellular matrix. The intima widens; the lumen "
            "narrows.",
            "Lecture 7 &middot; Slide 14") + '''
  <p><b>Key Concepts, response of vascular wall cells to injury</b> (slide 15, an image of the
  textbook&rsquo;s box; transcribed here because the deck has no text copy):</p>
  <ul>
    <li>All vessels are lined by endothelium; endothelial cells in specific vascular beds have special
    features for tissue-specific functions (for example, fenestrated endothelium in renal glomeruli).</li>
    <li>Endothelial function is tightly regulated. Stimuli can shift the phenotype: procoagulant versus
    anticoagulant, proinflammatory versus anti-inflammatory, adhesive versus nonadhesive.</li>
    <li><b>Injury of almost any type</b> to the wall produces a <b>stereotyped healing response</b>:
    smooth muscle proliferation, matrix deposition, and intimal expansion.</li>
    <li>Smooth muscle recruitment is signaled by endothelial cells, platelets and macrophages, and by
    mediators from the coagulation and complement cascades.</li>
    <li><b>Excessive intimal thickening</b> can cause luminal stenosis and vascular obstruction.</li>
  </ul>

  <h3 class="sub" id="l7-size">7.4 &middot; Objective c &mdash; Two mechanisms, three sizes of artery</h3>
  <p>The principal mechanisms of vascular disease (slide 16): <b>narrowing</b> &mdash; stenosis or
  obstruction of the lumen, either <b>progressive</b> (atherosclerosis) or <b>precipitous</b>
  (thrombosis, embolism) &mdash; and <b>weakening</b>, which leads to <b>dilation</b> or
  <b>rupture</b>. Each vessel type has its own structure for its own physiologic needs, so disease has
  <b>distinct anatomic distributions</b> (slide 17):</p>
  <table>
    <tr><th>Artery type (slide 18)</th><th>Examples</th><th>Typical disease and why</th></tr>
    <tr><td><b>Large (elastic)</b> &mdash; aorta about 2&ndash;3.5 cm</td><td>Aorta and its major
    branches, such as the iliac arteries</td><td><b>Aneurysm</b>: weakening from <b>loss of elastic
    tissue</b></td></tr>
    <tr><td><b>Medium (muscular)</b> &mdash; coronary arteries 3&ndash;4 mm</td><td>Smaller aortic
    branches: <b>coronary and renal</b> arteries</td><td><b>Atherosclerosis</b>: narrowing by intimal
    thickening, in arteries built with elastic and muscular components to withstand high pulsatile
    force and recoil</td></tr>
    <tr><td><b>Small arteries</b> (2 mm or less) and <b>arterioles</b> (20&ndash;100 micrometers)</td>
    <td>Within tissues and organs</td><td><b>Hypertension</b>: mechanical stress, endothelial
    dysfunction, less elasticity and weakening, while the lumen <b>stiffens and narrows</b></td></tr>
  </table>
  <div class="callout"><strong>A wording slip on slide 18.</strong> It says atherosclerosis narrows
  the vessel &ldquo;through intimal <em>neoplasia</em>&rdquo;. The deck&rsquo;s own slide 13, and the
  textbook figure it cites, describe the process as neointimal <b>hyperplasia</b>; a neoplasia would be
  a tumor. Read it as hyperplasia.</div>

  <h3 class="sub" id="l7-bp">7.5 &middot; Objective c &mdash; Blood pressure regulation and hypertension</h3>
  <p>Blood pressure is determined by <b>vascular resistance and cardiac output</b> (slide 19):</p>
  <ul>
    <li><b>Vascular resistance</b> is regulated at the <b>arterioles</b>, by neural and hormonal input,
    as a balance of vasoconstrictors (such as angiotensin) and vasodilators (such as nitric oxide).</li>
    <li><b>Cardiac output</b> is heart rate times stroke volume, and stroke volume depends on
    <b>blood volume</b>, which is regulated by <b>sodium excretion or resorption</b>. Water follows
    sodium: more sodium in the blood pulls in water, raising volume and so pressure &mdash; why chronic
    high sodium intake leads to hypertension.</li>
  </ul>
  ''' + fig(D7 + "blood-pressure-regulation.jpg", 1100, 409,
            "Diagram: blood pressure equals cardiac output times peripheral resistance, with the factors acting on each.",
            "<b>Blood pressure = cardiac output &times; peripheral resistance.</b> Cardiac output is fed "
            "by blood volume (sodium, mineralocorticoids, atrial natriuretic peptide) and cardiac factors "
            "(heart rate, contractility). Resistance is fed by humoral constrictors (angiotensin II, "
            "catecholamines, thromboxane, leukotrienes, endothelin) and dilators (prostaglandins, kinins, "
            "nitric oxide), neural factors (alpha-adrenergic constrict, beta-adrenergic dilate), and "
            "local factors (autoregulation, pH, hypoxia).",
            "Lecture 7 &middot; Slide 21") + '''
  <h4 class="subsub">When pressure falls: the renin&ndash;angiotensin&ndash;aldosterone response</h4>
  <ol>
    <li>The kidneys secrete <b>renin</b> in response to decreased pressure in the <b>afferent
    arterioles</b>.</li>
    <li>Renin cleaves <b>angiotensinogen to angiotensin I</b>.</li>
    <li><b>Endothelial catabolism</b> produces <b>angiotensin II</b>, a vasoconstrictor.</li>
    <li>Angiotensin II raises pressure by increasing <b>smooth muscle tone</b> and <b>adrenal
    aldosterone secretion</b>, which increases renal sodium resorption.</li>
  </ol>
  <h4 class="subsub">When pressure is high: hypertension (slide 20)</h4>
  <p>A common disorder and a risk factor for <b>atherosclerosis, congestive heart failure, renal failure,
  cerebral hemorrhage and aortic dissection</b>.</p>
  <table>
    <tr><th></th><th>Essential hypertension</th><th>Secondary hypertension</th></tr>
    <tr><td>Share</td><td><b>90&ndash;95%</b>, idiopathic</td><td>Much less common</td></tr>
    <tr><td>Mechanism</td><td>Genetic plus environmental factors; suspected small changes in <b>renal
    sodium homeostasis</b> and/or vessel wall tone and structure. <b>Insufficient renal sodium
    excretion</b> at normal arterial pressure &rarr; more fluid volume &rarr; more cardiac output
    &rarr; more vasoconstriction &rarr; raised pressure</td><td><b>Renovascular:</b> renal artery
    stenosis lowers glomerular flow and afferent arteriolar pressure, which <b>induces renin
    secretion</b> and raises volume and tone. <b>Primary hyperaldosteronism</b> is a common cause (in
    the lecture, for example from an adrenal adenoma)</td></tr>
  </table>

  <h3 class="sub" id="l7-arteriosclerosis">7.6 &middot; Objective c &mdash; Arteriosclerosis</h3>
  <p>Literally &ldquo;hardening of the arteries&rdquo;: the generic term for <b>arterial wall thickening
  and loss of elasticity</b>. Four patterns (slide 22):</p>
  <table>
    <tr><th>Pattern</th><th>Mechanism and features</th></tr>
    <tr><td><b>Arteriolosclerosis</b> of small arteries and arterioles</td><td>Can cause downstream
    ischemic injury. Two subtypes, both related to <b>hypertension</b>: <b>hyaline</b> and
    <b>hyperplastic</b></td></tr>
    <tr><td><b>Fibromuscular intimal hyperplasia</b></td><td>In muscular arteries larger than
    arterioles, driven by <b>inflammation or mechanical injury</b>; a healing response. Vessels can
    become very stenotic &mdash; for example <b>in-stent restenosis</b> &mdash; and it is a major
    long-term limitation of solid-organ transplants</td></tr>
    <tr><td><b>M&ouml;nckeberg medial sclerosis</b></td><td><b>Calcification of the media</b> of muscular
    arteries; usually not clinically significant (in the lecture, adults over 50)</td></tr>
    <tr><td><b>Atherosclerosis</b></td><td>Greek for &ldquo;gruel&rdquo; and &ldquo;hardening&rdquo;; the
    <b>most clinically relevant</b> form (section 7.7)</td></tr>
  </table>
  ''' + fig(D7 + "hyaline-hyperplastic.jpg", 1100, 390,
            "Two micrographs: A, an arteriole with a thick pink glassy wall and narrow lumen; B, an arteriole with concentric onion-skin layers.",
            "<b>A, hyaline:</b> the wall is thickened by protein deposition, glassy pink, and the lumen is "
            "markedly narrowed. <b>B, hyperplastic:</b> concentric layers of smooth muscle cells, the "
            "&ldquo;<b>onion skinning</b>&rdquo; she named, obliterating the lumen.",
            "Lecture 7 &middot; Slide 23") + '''

  <h3 class="sub" id="l7-athero">7.7 &middot; Objective c &mdash; Atherosclerosis, from the vessel wall</h3>
  <p>The major pathogenesis of <b>coronary, cerebral and peripheral vascular disease</b>, and the cause of
  more morbidity and mortality in the Western world than any other disorder &mdash; about half of all
  deaths (slide 24). Risk comes from acquired, inherited, sex- and age-related factors:</p>
  <table>
    <tr><th>Risk factor (slide 24)</th><th>What the lecture adds</th></tr>
    <tr><td>Hyperlipidemia</td><td>&mdash;</td></tr>
    <tr><td><b>Lipoprotein(a)</b></td><td>An altered form of low-density lipoprotein; risk independent of
    total cholesterol</td></tr>
    <tr><td>Smoking &middot; hypertension &middot; diabetes mellitus</td><td>&mdash;</td></tr>
    <tr><td><b>Metabolic syndrome</b></td><td>Central obesity, insulin resistance, hypertension,
    dyslipidemia; induces a <b>hypercoagulable and proinflammatory</b> state</td></tr>
    <tr><td><b>Inflammation</b> (C-reactive protein)</td><td>Now included in cardiovascular risk
    stratification</td></tr>
    <tr><td><b>Genetics</b></td><td><b>Family history is the most important risk factor</b> (on the
    slide)</td></tr>
    <tr><td>Increasing age</td><td>Progressive; manifests in the 40s to 60s and rises by decade</td></tr>
    <tr><td>Men and postmenopausal women</td><td>Likely a protective effect of estrogen</td></tr>
  </table>
  <p><b>The sequence (slide 25).</b> A chronic inflammatory and healing response of the arterial wall to
  endothelial injury:</p>
  <ol>
    <li>Healthy vessel is injured (think risk factors)</li>
    <li>Low-density lipoprotein accumulates in the wall</li>
    <li>Monocytes adhere to the endothelium</li>
    <li>Platelets adhere</li>
    <li>Smooth muscle cells are recruited, by factors released from activated platelets and macrophages</li>
    <li>Smooth muscle proliferates, extracellular matrix is produced, T cells are recruited</li>
    <li>Lipid accumulates</li>
    <li>Matrix and necrotic debris calcify</li>
  </ol>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
  <p><b>Peripheral arterial disease</b> is the consequence she told the class to know: the arteries become
  stenotic, which causes ischemia; with increased metabolic demand (walking) the patient has
  <mark class="prof-highlight">claudication, from lack of oxygenated blood to the working muscle</mark>
  (slide 25, [33:43]).</p>
  </div>
  ''' + fig(D7 + "atheroma.jpg", 1100, 337,
            "Diagram of an atheroma in the intima: a fibrous cap over a yellow necrotic center, above the media.",
            "The <b>atheroma</b>: an intimal lesion that projects into the lumen, with a <b>soft lipid core "
            "under a fibrous cap</b>. The labels: fibrous cap (smooth muscle cells, macrophages, foam "
            "cells, lymphocytes, collagen, elastin, proteoglycans, neovascularization); necrotic center "
            "(cell debris, cholesterol crystals, foam cells, calcium). Stable plaques cause ischemia; "
            "unstable ones rupture, thrombose and embolize.",
            "Lecture 7 &middot; Slide 26") + '''

  <h3 class="sub" id="l7-aneurysm">7.8 &middot; Objective c &mdash; Aneurysms and dissection</h3>
  <p>An <b>aneurysm</b> is a <b>localized abnormal dilation</b> of a vessel, congenital or acquired,
  classified by shape. A <b>dissection</b> is blood entering a defect in the arterial wall and
  <b>tunneling through the medial or medial-adventitial planes</b> (slide 27).</p>
  ''' + fig(D7 + "aneurysm-types.jpg", 1100, 323,
            "Five vessel outlines: normal, saccular true aneurysm, fusiform true aneurysm, false aneurysm with hematoma, and dissection with an intimal tear.",
            "<b>A</b> normal; <b>B</b> true aneurysm, saccular (a focal outward bulge; the berry "
            "shape); <b>C</b> true aneurysm, fusiform (circumferential dilation); <b>D</b> <b>false "
            "aneurysm</b> &mdash; the wall has ruptured and the hematoma is held in only by "
            "extravascular connective tissue; <b>E</b> <b>dissection</b> &mdash; a tear in the intima lets "
            "blood split the media.",
            "Lecture 7 &middot; Slide 27") + '''
  <p><b>Pathogenesis (slide 28).</b> Arterial walls constantly remodel; anything that compromises the
  connective tissue of the wall can produce aneurysm or dissection:</p>
  <table>
    <tr><th>Route to a weak wall</th><th>Examples</th></tr>
    <tr><td><b>Poor connective tissue quality</b></td><td>Defective collagen synthesis; abnormal
    transforming growth factor signaling (<b>Marfan syndrome</b>)</td></tr>
    <tr><td><b>Imbalance of collagen degradation and synthesis</b></td><td>Altered by inflammation and
    proteases; a genetic predisposition in the setting of inflammatory lesions</td></tr>
    <tr><td><b>Loss of smooth muscle cells</b> or inappropriate matrix synthesis</td><td><b>Ischemia,
    hypertension, tertiary syphilis</b></td></tr>
  </table>
  <p>Predisposing conditions for aortic aneurysm: <b>atherosclerosis, hypertension, smoking</b>.</p>
  <table>
    <tr><th>Aortic lesion (slide 29)</th><th>Mechanism and association</th></tr>
    <tr><td><b>Abdominal aortic aneurysm</b></td><td><b>Atherosclerotic</b> aneurysms occur most commonly
    in the abdominal aorta and common iliac arteries. Rupture risk rises with size: in the lecture,
    under <b>4 cm</b> they typically do not rupture and over <b>5.5 cm</b> the risk is very high</td></tr>
    <tr><td><b>Thoracic aortic aneurysm</b></td><td>Commonly associated with <b>hypertension</b>; also
    Marfan syndrome and inflammation (and, in the lecture, a bicuspid aortic valve, which raises local
    hemodynamic stress)</td></tr>
    <tr><td><b>Aortic dissection</b></td><td>The <b>laminar planes of the media split</b> to form a
    blood-filled channel in the wall. <b>Hypertension is the major risk factor.</b> In the lecture: two
    groups, ages 40&ndash;60 with hypertension, or younger patients with connective tissue disorders such
    as Marfan; also a sudden pressure spike (cocaine) or iatrogenic injury during catheterization</td></tr>
  </table>
  <table>
    <tr><th>Cerebral aneurysm (slide 30)</th><th>Features</th></tr>
    <tr><td><b>Saccular</b> (berry)</td><td>Thin-walled protrusions with <b>very thin or absent
    media</b> and <b>absent or fragmented internal elastic lamina</b>; typically acquired. Multifactorial:
    hemodynamic stress, turbulent flow causing structural fatigue, hypertension, smoking, connective tissue
    disease, possibly inflammation. <b>Lack of elastic lamina is the main feature.</b></td></tr>
    <tr><td><b>Fusiform</b></td><td>Dilation of the <b>entire circumference</b>; atherosclerosis may be
    a factor</td></tr>
    <tr><td><b>Mycotic</b></td><td>Usually from <b>infected emboli in infective endocarditis</b> (rare;
    see section 6.11)</td></tr>
  </table>

  <h3 class="sub" id="l7-other">7.9 &middot; Objective c &mdash; Fibromuscular dysplasia, vasculitis, Raynaud phenomenon, arteriovenous fistula</h3>
  <h4 class="subsub">Fibromuscular dysplasia (slide 31)</h4>
  <p>A <b>focal irregular thickening</b> of medium and large muscular arteries, exact cause unknown.
  Segments of wall are thickened by <b>hyperplasia and fibrosis of the media and intima</b>, causing
  luminal stenosis. Example: the <b>renal arteries</b> (in the lecture also carotid and vertebral; in the
  renal arteries it can cause renovascular hypertension). The angiographic sign is a <b>&ldquo;string of
  beads&rdquo;</b>, and it may lead to aneurysmal dilation that can rupture.</p>
  ''' + fig(D7 + "fibromuscular-dysplasia.jpg", 1100, 1184,
            "Six panels of computed tomography and catheter angiography images of renal arteries with beaded and focal narrowing.",
            "Renal arteries on computed tomography (left) and catheter angiography (right). Panels C and D "
            "show the classic <b>string of beads</b>: alternating narrowing and dilation along the "
            "vessel. The slide&rsquo;s note credits the American Heart Association source.",
            "Lecture 7 &middot; Slide 31") + '''
  <h4 class="subsub">Vasculitis (slide 32)</h4>
  <p>Vessel wall inflammation, with manifestations set by the vessel affected; any organ or vessel, but
  mostly small vessels. About 20 primary forms. <b>Two main pathogenic mechanisms: immune-mediated
  inflammation, and direct invasion of the wall by infectious pathogens.</b></p>
  <table>
    <tr><th>Vessel size</th><th>Examples on the slide</th></tr>
    <tr><td>Large</td><td>Giant cell arteritis (in the lecture: carotid, vertebral and temporal arteries;
    granulomatous inflammation)</td></tr>
    <tr><td>Medium</td><td>Polyarteritis nodosa; Kawasaki disease (in the lecture: an acute febrile
    illness of children under 5)</td></tr>
    <tr><td>Small</td><td>Two subgroups: <b>ANCA (anti-neutrophil cytoplasmic antibody)-associated</b>
    necrotizing vasculitis; <b>immune complex</b> vasculitis, as in systemic lupus erythematosus and
    rheumatoid arthritis</td></tr>
  </table>
  <h4 class="subsub">Raynaud phenomenon (slide 33)</h4>
  <p>An <b>exaggerated vasoconstrictive response to cold and emotional stress</b>, mostly in the arteries
  and arterioles of the extremities. <b>Vasoconstriction &rarr; tissue anoxia &rarr; return of
  oxygenated blood</b> produces the color sequence <b>white &rarr; blue &rarr; red</b>. In the lecture:
  white from constriction, blue from lack of oxygen, red when flow returns, which is painful because of
  rapid vessel dilation and a rush of inflammatory signals.</p>
  ''' + fig(D7 + "raynaud.jpg", 395, 506,
            "Illustration of a hand with a white finger and a blue finger, and insets of vasospastic and relaxed blood vessels.",
            "The white and blue phases in the fingers, with the vessel behind each: <b>vasospastic</b> "
            "(narrowed) against <b>relaxed</b>.",
            "Lecture 7 &middot; Slide 33") + '''
  <h4 class="subsub">Arteriovenous fistula (slide 34)</h4>
  <p>An irregular <b>direct connection between an artery and a vein, bypassing the capillaries</b>.
  Causes: developmental defects; <b>rupture of an arterial aneurysm into an adjacent vein</b>; penetrating
  injury that pierces artery and vein; inflammatory necrosis of adjacent vessels; or <b>surgical
  creation</b> for hemodialysis access, to carry high flow at a rapid rate. In the lecture: the vein then
  remodels until its wall can withstand arterial pressure.</p>

  <h3 class="sub" id="l7-veins">7.10 &middot; Objective c &mdash; Veins: varicosities and deep vein thrombosis</h3>
  <p>Veins have <b>larger diameters and lumens</b> than arteries and hold about <b>66% of total blood
  volume</b>. Their <b>thinner media</b> allows greater capacitance, and <b>venous valves prevent
  gravitational reverse flow</b>. As with arteries, location and structure predict the disease
  (slide 35):</p>
  <table>
    <tr><th>Veins</th><th>Examples</th><th>Typical disease</th></tr>
    <tr><td><b>Superficial</b></td><td>Great and small saphenous</td><td><b>Varicose veins</b>, from
    <b>insufficiency of the venous valves</b>; usually the lower extremities (flow against gravity), also
    pelvis and rectum (hemorrhoids)</td></tr>
    <tr><td><b>Deep</b></td><td>Femoral, popliteal, tibial</td><td><b>Stasis in a dilated vein &rarr;
    thrombosis</b> (deep vein thrombosis)</td></tr>
  </table>
  <p><b>Varicosities (slide 36).</b> Varicose veins are <b>dilated, tortuous veins</b> caused by
  <b>chronic high intraluminal pressure and weakened wall support</b>. <b>Esophageal varices</b> are
  dilated submucosal distal esophageal veins from <b>cirrhosis and portal venous hypertension</b>.
  <b>Hemorrhoids</b> are varicose dilations of the venous plexus at the anorectal junction. In the lecture,
  varicose veins and hemorrhoids were both linked to pregnancy.</p>
  ''' + fig(D7 + "varicose-veins.jpg", 800, 1007,
            "Illustration of a leg with varicose and spider veins, and insets comparing a normal vein and valve with a damaged valve and a varicose vein.",
            "Top inset: a <b>normal valve</b> closes and blood moves one way. Bottom inset: a <b>damaged "
            "valve</b> lets blood fall back, and the vein below it balloons into a varicosity.",
            "Lecture 7 &middot; Slide 36") + '''
  <h4 class="subsub">Deep vein thrombosis (slides 37&ndash;38)</h4>
  <p>A clot in a deep vein, typically of the legs; the <b>third most common cause of death from
  cardiovascular disease</b>.</p>
  <table>
    <tr><th>Risk factor (slide 37)</th><th>Examples</th></tr>
    <tr><td>Reduced blood flow</td><td><b>Immobility</b> (in the lecture: bed rest, general anesthesia,
    the postoperative state, stroke, a long flight)</td></tr>
    <tr><td>Increased venous pressure</td><td>Mechanical compression or functional impairment</td></tr>
    <tr><td>Mechanical injury</td><td>Trauma, surgery, intravenous drug use, iatrogenic</td></tr>
    <tr><td>Increased blood viscosity</td><td>Dehydration, thrombocytosis</td></tr>
    <tr><td>Anatomic variations</td><td>&mdash;</td></tr>
    <tr><td>Increased coagulation (genetic or acquired)</td><td>Cancer, sepsis, systemic lupus
    erythematosus, oral estrogen</td></tr>
  </table>
  <p><b>Virchow triad (slide 38):</b> (1) <b>damage to the vessel wall</b>, (2) <b>blood flow
  turbulence</b>, (3) <b>hypercoagulability</b>. Triggers are multifactorial, with the three involved in
  varying degrees.</p>
  <p><b>What happens to the clot.</b> Over weeks, <b>neutrophils and macrophages infiltrate the fibrin
  clot</b>, and <b>collagen gradually replaces the fibrin</b>; that remodeling and fibrosis
  <b>decrease blood flow</b>. If the thrombus dislodges it becomes an <b>embolus</b> that travels through
  the venous system to the <b>pulmonary artery</b>, occluding it: a <b>pulmonary embolus</b>.</p>
  ''' + fig(D7 + "deep-vein-thrombosis.jpg", 416, 480,
            "Illustration of a leg with a deep vein, and a sequence of panels: healthy vein with valve, pooling blood, blood clot, embolus.",
            "The sequence from stasis to embolus: healthy vein and valve &rarr; <b>pooling blood</b> "
            "&rarr; <b>blood clot</b> (thrombosis) &rarr; a fragment breaks free as an <b>embolus</b>.",
            "Lecture 7 &middot; Slide 38") + '''

  <button type="button" class="test-yourself-btn" style="--acc:#a23a4c" onclick="window.openTestYourself('Test yourself — Vascular Pathophysiology', TEST_YOURSELF.vascular)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>SV Vascular Pathophys I Fall 2026.pptx</em> (presented by Stacie
  Gopal, DMS, PA-C; adapted from Lauren Reynolds, PA-C) and the lecture recording of 15 September 2026.
  Figures are reproduced from the lecture slides and each is cited to its slide.</footer>
</section>
'''


def Q(q, choices, correct, explain):
    return {"q": q, "choices": choices, "correct": correct, "explain": explain}


TEST_YOURSELF = {
 "cardiac": [
  Q("What makes a coronary plaque vulnerable to rupture?",
    ["A large lipid core under a thin fibrous cap",
     "A small lipid core under a thick fibrous cap",
     "A heavily calcified cap rich in smooth muscle",
     "A cap made of collagen laid down over years"], 0,
    "A vulnerable plaque has a large necrotic core and a thin fibrous cap, rich in macrophages and poor in smooth muscle cells. A thick collagen cap is what makes a plaque more stable."),
  Q("After complete coronary occlusion, when does cell necrosis become irreversible?",
    ["Immediately, as ATP is depleted",
     "After about 30 minutes",
     "Within a few minutes, as contraction stops",
     "Only after 6 hours"], 1,
    "ATP is depleted immediately and contraction fails within a few minutes, but necrosis becomes irreversible after about 30 minutes. Six hours is when gross examination first turns positive."),
  Q("Which angina has no relation to physical or emotional stress?",
    ["Stable angina, from a fixed stenosis",
     "Unstable angina, from plaque rupture",
     "Prinzmetal angina, from vasospasm",
     "Crescendo angina, from rising demand"], 2,
    "Prinzmetal (variant) angina is unpredictable and probably caused by vasospasm. Stable angina appears when workload rises across a fixed stenosis; unstable (crescendo) angina is an acute coronary syndrome."),
  Q("In mitral stenosis, when is the abnormal left atrial to left ventricular pressure gradient present?",
    ["During systole, as the ventricle ejects",
     "During isovolumetric contraction only",
     "Only during atrial fibrillation",
     "During diastole, as the ventricle fills"], 3,
    "The stenotic mitral valve obstructs filling, so atrial pressure stays above ventricular pressure in diastole. Mitral regurgitation and aortic stenosis are the systolic lesions."),
  Q("Why does an infection that causes rheumatic heart disease damage the valves?",
    ["An immune attack caused by cross-reactivity",
     "Bacteria colonize the valve and form vegetations",
     "Toxins from the organism calcify the leaflets",
     "Ischemia of the papillary muscles tears them"], 0,
    "Rheumatic fever follows group A beta-hemolytic streptococcal infection, and the damage is immune-mediated through cross-reactivity. Vegetations of organisms in fibrin define infective endocarditis instead."),
  Q("Which lipoprotein lowers the risk of atherosclerosis, and how?",
    ["Very-low-density lipoprotein, by carrying triglyceride away",
     "High-density lipoprotein, by carrying cholesterol to the liver",
     "Low-density lipoprotein, by carrying cholesterol to tissue",
     "Lipoprotein(a), by stabilizing the fibrous cap"], 1,
    "High-density lipoprotein carries cholesterol back to the liver, clearing it from plaque. Low-density lipoprotein carries the highest risk, very-low-density lipoprotein increases it, and lipoprotein(a) adds risk."),
  Q("What defect causes familial hypercholesterolemia?",
    ["Overproduction of high-density lipoprotein",
     "Loss of lipoprotein lipase in muscle",
     "A defective low-density lipoprotein receptor on liver cells",
     "Excess conversion of methionine to cysteine"], 2,
    "A defective low-density lipoprotein receptor on hepatocytes leaves the liver unable to clear cholesterol from the blood. Methionine-to-cysteine conversion is where homocysteine comes from."),
  Q("What impairs diastolic filling in constrictive pericarditis?",
    ["Fluid compressing the chambers from outside",
     "A thickened, hyperkinetic ventricular wall",
     "Adhesion of the heart to mediastinal structures",
     "A dense, scarred sac encasing the heart like a cage"], 3,
    "In constrictive pericarditis the sac becomes dense, fibrous and nonelastic and encases the heart. Fluid compression is tamponade; adhesion to the mediastinum is adhesive mediastinopericarditis."),
 ],
 "vascular": [
  Q("Which size of artery is typically affected by atherosclerosis?",
    ["Medium muscular arteries, such as the coronaries",
     "Large elastic arteries, such as the aorta",
     "Small arteries and arterioles within organs",
     "Capillaries of the myocardium and brain"], 0,
    "Atherosclerosis narrows medium muscular arteries such as the coronary and renal arteries. Large elastic arteries typically develop aneurysms, and small arteries and arterioles are the target of hypertension."),
  Q("Why does endothelial injury narrow a vessel twice over?",
    ["Platelets dissolve the basement membrane",
     "Intimal thickening plus less nitric oxide",
     "Loss of elastin plus a thinner media",
     "Pericytes contract and occlude capillaries"], 1,
    "Smooth muscle migrates into the intima and lays down matrix, narrowing the lumen, while falling nitric oxide removes a vasodilator, so the vessel also constricts."),
  Q("In the renin-angiotensin response to low blood pressure, what does renin do?",
    ["Converts angiotensin I to angiotensin II",
     "Stimulates adrenal aldosterone release directly",
     "Cleaves angiotensinogen to angiotensin I",
     "Increases renal sodium excretion"], 2,
    "Renin, released from the kidney in response to low afferent arteriolar pressure, cleaves angiotensinogen to angiotensin I. Angiotensin II then raises smooth muscle tone and aldosterone secretion."),
  Q("What is the main feature of a saccular cerebral aneurysm?",
    ["Calcification of the media",
     "Circumferential dilation of the whole vessel",
     "Infected emboli lodged in the wall",
     "Lack of internal elastic lamina"], 3,
    "Saccular (berry) aneurysms have a thin or absent media and an absent or fragmented internal elastic lamina. Circumferential dilation is fusiform, and infected emboli produce mycotic aneurysms."),
  Q("What separates a dissection from a false aneurysm?",
    ["An intimal tear lets blood split the media",
     "A ruptured wall leaves a hematoma held by tissue",
     "The whole circumference of the vessel dilates",
     "A focal bulge of all three wall layers forms"], 0,
    "In dissection blood enters a defect and tunnels through the medial planes. In a false aneurysm the wall has ruptured and the hematoma is contained by extravascular connective tissue."),
  Q("Which is the major risk factor for aortic dissection?",
    ["Atherosclerosis",
     "Hypertension",
     "Tertiary syphilis",
     "Raynaud phenomenon"], 1,
    "Hypertension is the major risk factor for aortic dissection. Atherosclerotic aneurysms favor the abdominal aorta and common iliac arteries."),
  Q("Which triad underlies deep vein thrombosis?",
    ["Stasis, low sodium, and high renin",
     "Hypertension, smoking, and lipoprotein(a)",
     "Vessel wall damage, flow turbulence, hypercoagulability",
     "Valve insufficiency, dilation, and tortuosity"], 2,
    "Virchow triad: damage to the vessel wall, blood flow turbulence, and hypercoagulability. Valve insufficiency with dilated, tortuous veins describes varicose veins."),
  Q("What produces the red phase of Raynaud phenomenon?",
    ["Tissue anoxia during vasospasm",
     "Deoxygenated blood pooling in veins",
     "Calcification of digital arteries",
     "Return of oxygenated blood after the spasm"], 3,
    "The sequence is vasoconstriction (white), tissue anoxia (blue), then return of oxygenated blood (red). The return is painful because of rapid vessel dilation."),
 ],
}
