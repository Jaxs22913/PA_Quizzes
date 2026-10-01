#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add PDM I section 10 (Coagulation and Hemostasis Testing) to the Exam 2 study guide.

Lecture 10, Professor Lauren Reynolds, 30 September 2026. Deck: "Coagulation Studies 2026.pptx"
(37 slides). Instructional Objectives are VERBATIM from the syllabus (PDM.pdf, Topic Outline 10).

The Exam 2 guide is NOT regenerated for this lecture: since build_pdm_e2_guide.py ran, the guide has
taken two bulk passes (per-question "Also tested" lines written into sections, and the truth-audit
patches). Regenerating from the builder would lose them, so this script APPENDS, the way
add_pdm_guide_l6.py did for Exam 1. It is idempotent: every insertion is fenced in comment markers
and stripped before it is re-inserted.

Picture-only slides, all viewed at full size before being placed:
  4  the three phases of hemostasis (figure)            5  the coagulation pathway (figure)
  14 spurious thrombocytopenia smear                    15 thrombotic thrombocytopenic purpura smears
  17 bleeding time, the four-panel photograph           25 causes of acquired thrombocytopenia
  27 isolated prolonged aPTT algorithm                  28 inherited bleeding disorder algorithm
  29 a PHOTOGRAPH OF A TEXTBOOK PAGE carrying two tables (clotting/platelet tests; clotting studies)
  30 the disseminated intravascular coagulation table   37 a cartoon (not reproduced)
Slides 29 and 30 are tables that exist only as pictures; they are TYPED here as HTML tables. The two
algorithms (27, 28) are reproduced AND typed out step by step.

AFTER THIS SCRIPT, run tools/add_pdm_l10_memaid.py (section 10.0, the wall-building crew memory aid, Jaxon
2026-09-30), tools/apply_guide_additions.py, tools/build_guide_links.py and tools/build_guide_docx.py: this
script rebuilds the whole section and strips the memory aid.

Slide/figure disagreements flagged in the guide rather than resolved silently (truth wins): the
thrombocytopenia threshold on slide 13, the "fibrin monomers (fibrin split products)" heading on slide
22, the "international reference thromboplastin" wording on slide 20, hypersplenism filed under
"dilutional" in the slide 25 figure, and the DOAC wording on slides 23 versus 24.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
DIR = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 2")
GUIDE = os.path.join(DIR, "pdm-exam-2-study-guide.html")
IMG = "pdm-exam-2-study-guide-images"
DECK = "Coagulation Studies 2026.pptx"
RECORDING_NOTE_FILE = os.path.join(HERE, "pdm_l10_emphasis_block.html")   # written by the emphasis step


def fig(name, w, h, alt, cap, slide):
    assert "  " not in alt and "  " not in cap
    assert os.path.exists(os.path.join(DIR, IMG, name)), name
    return ('<figure class="fig"><img width="%d" height="%d" loading="lazy" src="%s/%s" alt="%s">'
            '<figcaption>%s <span class="tag">Source: %s, Slide %d.</span></figcaption></figure>'
            % (w, h, IMG, name, alt, cap, DECK, slide))


F = {}
F["three"] = fig("10-three-phases.png", 1000, 599,
    "Three panels. Panel A, platelets and vessel wall adhesion and aggregation: von Willebrand factor binds exposed collagen and the platelet receptor glycoprotein IIb/IIIa, and platelets aggregate. Panel B, blood coagulation from fibrinogen to fibrin: factor Xa converts prothrombin to thrombin, and thrombin turns fibrinogen into a fibrin network at the platelet aggregate. Panel C, fibrinolysis: tissue plasminogen activator converts plasminogen to plasmin on the fibrin surface, and plasmin degrades the clot to fragments including D-dimer; factor XIII cross-links the fibrin.",
    "<b>The three phases of hemostasis.</b> (A) Platelets stick to exposed collagen through von Willebrand factor and aggregate through glycoprotein IIb/IIIa. (B) Thrombin converts fibrinogen to a fibrin network. (C) Plasmin, made from plasminogen by tissue plasminogen activator, degrades cross-linked fibrin into pieces, and <b>D-dimer</b> is one of them. Each laboratory test in this lecture evaluates one of these three panels.", 4)
F["pathway"] = fig("10-coagulation-pathway.png", 1000, 1059,
    "Coagulation pathway diagram. The intrinsic pathway runs factor XII to XI to IX to VIII with calcium. The extrinsic pathway runs tissue factor and factor VII. Both converge on the common pathway: factor X, with factor V, converts prothrombin (II) to thrombin (IIa), which converts fibrinogen (I) to fibrin (Ia); thrombin also activates factor XIII, which stabilizes the clot. Red letters mark factors involved in hemophilia A (VIII), hemophilia B (IX), hemophilia C (XI), von Willebrand disease (VIII) and vitamin K deficiency (II, VII, IX, X).",
    "<b>The coagulation pathway (secondary hemostasis).</b> Intrinsic (XII, XI, IX, VIII) and extrinsic (tissue factor, VII) arms meet at factor X in the common pathway (X, V, II, I, XIII). The red letters on the figure mark the factors that fail in each disorder: <b>A</b> hemophilia A (VIII), <b>B</b> hemophilia B (IX), <b>C</b> hemophilia C (XI), <b>D</b> von Willebrand disease (VIII), <b>E</b> vitamin K deficiency (II, VII, IX and X).", 5)
F["spurious"] = fig("10-spurious-thrombocytopenia.jpg", 549, 388,
    "Peripheral blood smear showing clumps of platelets and neutrophils ringed by platelets, in a patient whose automated platelet count was reported as low.",
    "<b>Spurious thrombocytopenia.</b> Platelets clump, and platelets sit around neutrophils (satellitism), so the automated count reads falsely low (10,000 to 150,000 per microliter on different occasions in this patient). The smear exposes the artifact; a count confirmed in a citrated or heparinized tube avoids it.", 14)
F["ttp1"] = fig("10-ttp-smear.jpg", 511, 370,
    "Blood smear in thrombotic thrombocytopenic purpura showing fragmented red cells and basophilic cells with few platelets.",
    "<b>Thrombotic thrombocytopenic purpura.</b> The smear shows red blood cell fragments and basophilic cells, in addition to the thrombocytopenia.", 15)
F["ttp2"] = fig("10-ttp-schistocytes.jpg", 442, 357,
    "Blood smear in thrombotic thrombocytopenic purpura with several schistocytes, helmet-shaped and triangular red cell fragments.",
    "<b>Schistocytes</b> (fragmented red cells) in thrombotic thrombocytopenic purpura.", 15)
F["bt"] = fig("10-bleeding-time.jpg", 642, 475,
    "Four photographs of a bleeding time test on the forearm: a spring-loaded device makes small horizontal cuts, blood is blotted onto filter paper at intervals while a stopwatch runs, and the pattern of blotted spots fades as bleeding stops.",
    "<b>Bleeding time, done at the bedside.</b> A standardized device cuts the cleaned forearm skin, blood is blotted onto filter paper, and the time until bleeding stops is recorded.", 17)
F["causes"] = fig("10-thrombocytopenia-causes.png", 433, 362,
    "Flow chart of common causes of acquired thrombocytopenia: impaired production, increased destruction (immune mechanisms, microangiopathy, consumptive coagulopathy) and dilutional.",
    "<b>Common causes of acquired thrombocytopenia.</b> Impaired production (nutritional deficiency, marrow replacement, chemotherapy, alcohol); increased destruction by immune mechanisms (immune thrombocytopenia, drug-dependent), by microangiopathy (thrombotic thrombocytopenic purpura, hemolytic uremic syndrome) or by consumptive coagulopathy (disseminated intravascular coagulation, extracorporeal circuits, cardiopulmonary bypass); and dilutional.", 25)
F["ptt"] = fig("10-isolated-ptt-algorithm.png", 763, 466,
    "Algorithm for isolated prolongation of the partial thromboplastin time. Rule out heparin effect, then measure fibrinogen activity. If fibrinogen is high, do a 1:1 mixing study. If it corrects, evaluate factor deficiency with a factor VIII assay; a low factor VIII with abnormal von Willebrand factor means von Willebrand disease and with normal von Willebrand factor means hemophilia. If it fails to correct, look for an inhibitor; phospholipid dependence points to lupus anticoagulant and no dependence to a specific factor inhibitor. If fibrinogen is low, measure fibrinogen antigen to separate hypofibrinogenemia from dysfibrinogenemia.",
    "<b>Isolated prolongation of the partial thromboplastin time.</b> Typed out step by step in 10.8 below.", 27)
F["inh"] = fig("10-inherited-bleeding-algorithm.png", 952, 715,
    "Algorithm for a suspected inherited bleeding disorder. Start with the prothrombin time, partial thromboplastin time, thrombin time or fibrinogen activity assay. If all are normal: platelet disorders and mild von Willebrand disease, deficiency of inhibitors of the fibrinolytic system, or factor XIII deficiency. If prolonged: clotting factor deficiency, split by prolonged prothrombin time only (factor VII), partial thromboplastin time only (factors VIII, IX, XI or severe von Willebrand disease) or both (common pathway factors or a fibrinogen problem, separated by the thrombin time).",
    "<b>A suspected inherited bleeding disorder.</b> Typed out in 10.8 below.", 28)


SEC = """
<section class="deck" id="coagulation">
  <h2 class="deck-title">10 &middot; Coagulation and Hemostasis Testing</h2>
  <p class="lecturer">Lauren Reynolds, MSPA, PA-C &middot; 30 September 2026</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 10: Coagulation and Hemostasis Testing</p>
    <ol type="a">
      <li>Define: i. Hemostasis &middot; ii. Primary hemostasis &middot; iii. Secondary hemostasis &middot; iv. Thrombus &middot; v. Fibrinolysis &middot; vi. Fibrin degradation products &middot; vii. D-dimer</li>
      <li>Discuss diagnostic testing for: i. Primary hemostasis &middot; ii. Secondary hemostasis &middot; iii. Fibrinolysis</li>
      <li>Compare and contrast laboratory studies used to evaluate bleeding and thrombotic disorders.</li>
      <li>Describe laboratory findings associated with platelet abnormalities.</li>
      <li>Discuss indications for ordering coagulation studies.</li>
      <li>Interpret common coagulation studies including: i. PT &middot; ii. INR &middot; iii. aPTT &middot; iv. D-dimer</li>
    </ol>
  </div>

  <div class="callout"><p><strong>The one-line frame for the whole lecture.</strong> <em>Hemostasis is the balance between clot formation and clot breakdown, and each laboratory test evaluates one part of that balance.</em> Platelets make the plug (primary hemostasis), coagulation factors make the fibrin (secondary hemostasis), plasmin takes the clot apart (fibrinolysis). Decide which phase you are asking about, and the test follows.</p>
  <p><strong>Numbers:</strong> the values below are here so you can read a result, not to memorize &mdash; reference ranges vary by laboratory and are supplied on her exams (her standing rule from Lecture 1). Nothing in this lecture asks you to calculate.</p></div>

@@EMPH@@
  <h3 class="sub" id="co-define">10.1 &middot; Objective a &mdash; The seven terms</h3>
  <table>
    <tr><th>Term</th><th>Definition</th><th>Read it this way</th></tr>
    <tr><td><strong>Hemostasis</strong></td><td>The arrest of bleeding from an injured blood vessel</td><td>The finely tuned process that stops bleeding while <strong>preventing pathologic thrombosis</strong>. <mark class="prof-highlight">&#9733; Three overlapping stages: primary hemostasis, secondary hemostasis and fibrinolysis</mark>;  three classic components: vasoconstriction, platelet plug formation and coagulation.</td></tr>
    <tr><td><strong>Primary hemostasis</strong></td><td>Formation of a <strong>platelet plug</strong> at the site of vascular injury</td><td>von Willebrand factor tethers platelets to exposed subendothelial collagen through glycoprotein Ib; activated platelets release thromboxane A2 and granules, and aggregate through glycoprotein IIb/IIIa with fibrinogen bridging.</td></tr>
    <tr><td><strong>Secondary hemostasis</strong></td><td>Formation of <strong>insoluble, cross-linked fibrin</strong> by activated coagulation factors, specifically <strong>thrombin</strong></td><td>The coagulation cascade. In the cell-based model: <strong>initiation</strong> (tissue factor with factor VIIa activates IX and X, forming prothrombinase), <strong>amplification</strong> (thrombin activates platelets and cofactors V and VIII) and <strong>propagation</strong> (a burst of thrombin converts fibrinogen to fibrin).</td></tr>
    <tr><td><strong>Thrombus</strong></td><td>A blood clot formed <strong>in situ</strong> within the vascular system that impedes blood flow</td><td>Once it has done its job it must be dissolved to restore the vessel.</td></tr>
    <tr><td><strong>Fibrinolysis</strong></td><td>Enzymatic breakdown of fibrin in clots</td><td>Tissue plasminogen activator converts plasminogen to <strong>plasmin</strong>, which degrades fibrin.</td></tr>
    <tr><td><strong>Fibrin degradation products</strong></td><td>Fragments released after <strong>plasmin-mediated degradation of fibrinogen or fibrin</strong></td><td>Markedly elevated when fibrinolysis is activated, as in disseminated intravascular coagulation.</td></tr>
    <tr><td><strong>D-dimer</strong></td><td>A degradation product of fibrin clots, produced by the action of three enzymes: <strong>thrombin, activated factor XIII and plasmin</strong></td><td>A specific <strong>cross-linked</strong> fibrin degradation product. It exists only after fibrin has been formed, cross-linked and then broken down.</td></tr>
  </table>
  @@three@@
  @@pathway@@
  <div class="pearl"><strong>Reading the pathway figure.</strong> Thrombin does more than make fibrin: it activates factors <strong>VIII, V and XIII</strong>, which is why it appears three times on the diagram. The extrinsic arm is tissue factor and <strong>factor VII</strong>; the intrinsic arm is <strong>XII, XI, IX and VIII</strong>; both feed factor <strong>X</strong>, and everything downstream is the common pathway (X, V, II, I, XIII). The five red letters on the figure are the disorders to tie to a factor: hemophilia A is factor VIII, hemophilia B is factor IX, hemophilia C is factor XI, von Willebrand disease is tied to factor VIII, and <strong>vitamin K deficiency hits II, VII, IX and X</strong> (the reason the prothrombin time is sensitive to it; 10.3).</div>

  <h3 class="sub" id="co-primary">10.2 &middot; Objective b.i &mdash; Testing primary hemostasis (platelets)</h3>
  <p>Primary hemostasis is tested with three groups of studies: <strong>counts and smears</strong>, <strong>von Willebrand studies</strong> and <strong>platelet function testing</strong>.</p>
  <table>
    <tr><th>Test</th><th>What it tells you</th><th>Reference / key point</th></tr>
    <tr><td><strong>Platelet count</strong> (from the complete blood count)</td><td>How many platelets there are</td><td>Adults <strong>140,000&ndash;400,000 per microliter</strong> (1 cubic millimeter = 1 microliter); children 150,000&ndash;450,000. The deck defines <strong>thrombocytopenia</strong> as below 100,000 per microliter and <strong>thrombocytosis</strong> as above 350,000.</td></tr>
    <tr><td><strong>Mean platelet volume</strong></td><td>The <strong>uniformity of size</strong> of the platelet population</td><td>Used in the <strong>differential diagnosis of thrombocytopenia</strong>. Normal <strong>7.4&ndash;10.4 femtoliters</strong> in children and adults.</td></tr>
    <tr><td><strong>Peripheral blood smear</strong></td><td>Platelet <strong>morphology</strong>: macrothrombocytopenia, gray platelets, neutrophil inclusions, clumps</td><td>Also the way to catch a false low count (below).</td></tr>
    <tr><td><strong>von Willebrand studies</strong></td><td>von Willebrand factor <strong>antigen</strong> and <strong>activity</strong>, plus a <strong>factor VIII level</strong></td><td>von Willebrand disease is the <strong>most common inherited bleeding disorder</strong>.</td></tr>
    <tr><td><strong>Platelet function testing</strong></td><td>Whether platelets work</td><td>Light transmission aggregometry, lumiaggregometry, the PFA-100 (platelet function analyzer) and flow cytometry.</td></tr>
    <tr><td><strong>Bleeding time</strong></td><td>Minutes for a standardized, superficial skin puncture to stop bleeding, performed at the bedside</td><td>Normal for most laboratories <strong>3&ndash;10 minutes</strong>, varying with the method. <strong>Only useful if the platelet count is above 100,000 per microliter</strong>, because thrombocytopenia itself lengthens the time.</td></tr>
  </table>
  <p><mark class="prof-highlight">&#9733; <strong>von Willebrand disease is the most common inherited bleeding disorder</strong></mark>, and it is evaluated with von Willebrand factor antigen, activity and a factor VIII level.</p>
  @@bt@@
  <p>With a normal platelet count, <strong>a prolonged bleeding time means the platelets are not working well</strong>, a defect of primary hemostasis.</p>
  <div class="callout warn"><p><strong>The deck and current practice differ on bleeding time.</strong> Slide 9 lists it among the five initial screening tests, and slides 16 and 17 describe how it is done. It is nonetheless a poorly reproducible test that has largely given way to platelet function analyzer testing, so learn it as <em>what it measures and when it is meaningless</em> (platelet count of 100,000 or below), not as a modern first-line test.</p></div>
  <h4 class="subsub">Do not trust a low count until the smear agrees</h4>
  <p>Extreme <strong>thrombocytosis</strong> (above 1,000 &times; 10<sup>9</sup> per liter) and thrombocytopenia can <strong>both</strong> cause bleeding. A low count should be <strong>confirmed in a citrated or heparinized tube</strong> to exclude <strong>pseudothrombocytopenia induced by EDTA</strong> (ethylenediaminetetraacetic acid, the anticoagulant in the usual purple-top tube), in which platelets clump.</p>
  @@spurious@@

  <h3 class="sub" id="co-secondary">10.3 &middot; Objective b.ii &mdash; Testing secondary hemostasis (coagulation factors)</h3>
  <p><strong>Screening:</strong> PT (prothrombin time; the extrinsic or tissue factor pathway), aPTT (activated partial thromboplastin time; the intrinsic pathway), thrombin time and fibrinogen. <strong>Mixing studies</strong> follow when the PT or aPTT is prolonged; <strong>specific factor assays</strong> confirm.</p>
  <table>
    <tr><th>Test</th><th>What it measures</th><th>Pathway</th><th>Reference (varies by laboratory)</th><th>Prolonged or abnormal means</th></tr>
    <tr><td><strong>PT</strong> (prothrombin time)</td><td>Time for a fibrin clot to form in a lab tube when <strong>tissue factor</strong> is added to the patient&rsquo;s plasma. Prothrombin is made by the liver and depends on <strong>vitamin K</strong> intake and absorption.</td><td><strong>Extrinsic</strong> (plus common)</td><td>11&ndash;13 seconds</td><td>Deficiency of extrinsic (factor VII) or common pathway factors; <strong>liver disease, vitamin K deficiency, warfarin</strong></td></tr>
    <tr><td><strong>INR</strong> (international normalized ratio)</td><td>The PT expressed as a <strong>comparative rating</strong> (the observed PT ratio adjusted for the reagent used), so results can be <strong>standardized from lab to lab</strong></td><td>Same as PT</td><td><strong>0.8&ndash;1.2</strong>; on anticoagulation the target varies, typically <strong>2.0&ndash;3.0</strong></td><td><mark class="prof-highlight">&#9733; On warfarin: <strong>low = clot risk, high = bleeding risk</strong></mark>. Off warfarin: a bleeding disorder, a clotting disorder, liver disease or vitamin K deficiency.</td></tr>
    <tr><td><strong>aPTT</strong> (activated partial thromboplastin time)</td><td>Time for a fibrin clot to form when a special <strong>phospholipid activator</strong> is added to the patient&rsquo;s plasma</td><td><strong>Intrinsic</strong> (plus common)</td><td>21&ndash;35 seconds; above <strong>70 seconds</strong> signifies spontaneous bleeding</td><td>Deficiency of intrinsic factors (VIII, IX, XI); heparin; dabigatran; an inhibitor; lupus anticoagulant or factor XII deficiency</td></tr>
    <tr><td><strong>Thrombin time</strong></td><td>Listed by the deck as a screening test of secondary hemostasis (it gives no definition)</td><td>&mdash;</td><td>(no value given)</td><td>Raised by <strong>heparin and dabigatran</strong>, by low or abnormal fibrinogen and in disseminated intravascular coagulation; <strong>normal</strong> in a simple factor deficiency (Table 4-10 in 10.8)</td></tr>
    <tr><td><strong>Fibrinogen</strong></td><td>The substrate that thrombin converts to fibrin; the <strong>Clauss assay is preferred</strong> over a PT-derived value</td><td>&mdash;</td><td><strong>2.0&ndash;4.0 grams per liter</strong></td><td><strong>Low = bleed, high = clot.</strong> Below 0.5 g/L can cause hemorrhage after traumatic surgery; above 7.0 g/L is a significant risk for coronary and cerebrovascular disease. Elevated results indicate tissue damage or inflammation.</td></tr>
    <tr><td><strong>Mixing study</strong></td><td>Patient plasma mixed with normal plasma, then the prolonged test repeated</td><td>&mdash;</td><td>&mdash;</td><td><strong>Correction</strong> = a factor deficiency. <strong>No correction</strong> = an inhibitor.</td></tr>
    <tr><td><strong>Factor assays</strong></td><td>The level of one specific factor</td><td>&mdash;</td><td>&mdash;</td><td>Confirm the deficiency. Deficiencies may be inherited or acquired, and acquired disorders can <strong>raise or lower</strong> factor levels.</td></tr>
  </table>
  <div class="pearl"><strong>Which arm is which.</strong> The PT pairs with the <strong>extrinsic</strong> arm (tissue factor, factor VII); the aPTT pairs with the <strong>intrinsic</strong> arm (XII, XI, IX, VIII). A patient whose <em>only</em> abnormal screen is a prolonged PT points to factor VII, early vitamin K deficiency, liver disease or warfarin; a patient whose <em>only</em> abnormal screen is a prolonged aPTT points to the intrinsic factors, heparin or a circulating inhibitor. A prolongation of <em>both</em> means the common pathway or a combined problem.</div>
  <div class="callout warn"><p><strong>Three wording points where the slide is loose.</strong> (1) The INR adjusts for the <em>international sensitivity index</em> of the thromboplastin reagent; slide 20 calls it the &ldquo;International Reference Thromboplastin.&rdquo; Either way, the purpose is the same: make PT results comparable between laboratories. (2) Slide 22 titles its second entry &ldquo;fibrin monomers (fibrin split products),&rdquo; but the two are different things: <strong>fibrin degradation products come from plasmin</strong> (10.1), while the fibrin-monomer result described on that slide reflects <strong>thrombin</strong> activity (10.4). (3) The deck itself does not define thrombin time beyond listing it; it is treated here only by what the slides state about it.</p></div>
  <h4 class="subsub">Caveats to coagulation studies</h4>
  <ul>
    <li><strong>A normal PT/INR does not rule out a coagulopathy.</strong></li>
    <li><strong>Low-molecular-weight heparin and most direct oral anticoagulants</strong> may not derange the PT or aPTT yet still raise bleeding risk; <strong>routine monitoring of the direct oral anticoagulants is not required.</strong> (Slide 24 does list an oral factor Xa inhibitor among causes of a prolonged PT, so a normal result never proves the drug is absent.)</li>
    <li><strong>Pregnancy shifts reference ranges:</strong> by the third trimester the PT, aPTT and thrombin time <strong>shorten</strong>, and fibrinogen and D-dimer <strong>rise</strong>.</li>
    <li><strong>Mild or moderate PT/aPTT prolongation does not predict bleeding</strong> in a patient who is not bleeding (slide 8), so a mildly abnormal screen is not a forecast of bleeding.</li>
  </ul>

  <h3 class="sub" id="co-fibrinolysis">10.4 &middot; Objective b.iii &mdash; Testing fibrinolysis (the breakdown products)</h3>
  <table>
    <tr><th>Test</th><th>What a result means</th></tr>
    <tr><td><strong>D-dimer</strong> (normal below 250 micrograms per liter in the deck)</td><td><strong>Produced only by plasmin acting on cross-linked fibrin</strong>, so its presence confirms that <strong>both thrombin generation and plasmin generation</strong> have occurred. It is a <strong>nonspecific</strong> marker of fibrin breakdown: elevated in acute thrombosis, disseminated intravascular coagulation, pregnancy and many acute illnesses. <mark class="prof-highlight">&#9733; Its strength is a <strong>high negative predictive value</strong>: a normal result helps <strong>exclude</strong> thrombosis</mark>.</td></tr>
    <tr><td><strong>Fibrin monomers</strong></td><td>A <strong>positive</strong> test indicates thrombin activity and is consistent with <strong>intravascular coagulation</strong>. A <strong>negative</strong> test does <strong>not</strong> mean intravascular coagulation is absent. A positive result can also occur in some cases of severe liver disease and in inflammatory disorders.</td></tr>
  </table>
  <div class="pearl"><strong>Clot and breakdown in one sentence.</strong> Thrombin = clot generation; plasmin = clot breakdown. <strong>D-dimer tells you a clot is present</strong> &mdash; that clot factors <em>and</em> breakdown factors were both active &mdash; but not <em>where</em> it is or <em>why</em>. Use it to rule out, not to rule in.</div>
  <p>Other specific tests of fibrinolysis appear in the inherited-bleeding algorithm (10.8): <strong>euglobulin clot lysis time</strong> (screening) and assays for <strong>alpha-2 antiplasmin</strong> and <strong>plasminogen activator inhibitor 1</strong> when the fibrinolytic system&rsquo;s inhibitors are deficient.</p>

  <h3 class="sub" id="co-compare">10.5 &middot; Objective c &mdash; Bleeding versus thrombotic workups</h3>
  <p><strong>Five primary screening tests</strong> are done first when a coagulation disorder is suspected: <strong>platelet count, size and shape; bleeding time; aPTT; PT; fibrinogen level.</strong> Factor assays and tests for fibrinolysis follow if the screens call for them.</p>
  <table>
    <tr><th></th><th>Bleeding workup</th><th>Thrombotic (clotting) workup</th></tr>
    <tr><td><strong>Core tests</strong></td><td>Complete blood count with differential and <strong>peripheral smear</strong>; <strong>PT/INR</strong>; <strong>aPTT</strong>; <strong>fibrinogen</strong>. Interpret by the <strong>PT/aPTT pattern</strong> first.</td><td><strong>PT</strong>; <strong>aPTT</strong>; <strong>D-dimer</strong>. They differ significantly across thrombus types; most will be abnormal in disseminated intravascular coagulation.</td></tr>
    <tr><td><strong>What it screens</strong></td><td>The <strong>factor and platelet</strong> screens</td><td>Markers of <strong>thrombin generation</strong> and clot breakdown</td></tr>
    <tr><td><strong>Extra studies</strong></td><td>Factor assays; tests for fibrinolysis; platelet function and von Willebrand studies</td><td>Hypercoagulable testing (below)</td></tr>
  </table>
  <p><strong>The thrombotic workup is the PT, the aPTT and D-dimer</strong>; these differ significantly across thrombus types, and most are abnormal in disseminated intravascular coagulation. The <strong>prothrombin time and D-dimer are independent risk factors for arterial thrombosis</strong>.</p>
  <h4 class="subsub">Laboratory investigation of hypercoagulable states</h4>
  <p>Testing covers both primary and secondary causes.</p>
  <table>
    <tr><th>Causes</th><th>Examples</th></tr>
    <tr><td><strong>Primary</strong></td><td>Deficiencies of <strong>antithrombin III, protein C and protein S</strong>; abnormal fibrinolytic mechanisms. <em>The slide also lists factor XII here, but factor XII deficiency is not an established cause of thrombosis (slide 32 itself says it prolongs the aPTT without bleeding), so the established primary causes to know are the first three.</em></td></tr>
    <tr><td><strong>Secondary</strong></td><td>Acquired platelet disorders; acquired diseases of coagulation and fibrinolytic impairment</td></tr>
    <tr><td><strong>Tests</strong></td><td>PT, aPTT, fibrinogen level, thrombin time; antiplatelet factors (for example prostacyclin); anticoagulant factors (<strong>antithrombin III, protein C, protein S, lupus anticoagulant</strong>); fibrinolysis tests</td></tr>
  </table>

  <h3 class="sub" id="co-platelets">10.6 &middot; Objective d &mdash; Laboratory findings in platelet abnormalities</h3>
  <h4 class="subsub">Bleeding risk climbs as the count falls</h4>
  <table>
    <tr><th>Platelet count</th><th>What to expect</th></tr>
    <tr><td><strong>Below 50,000 per microliter</strong></td><td>May bleed excessively with mild or moderate trauma and with surgery involving mucous membranes; <strong>bruises easily</strong></td></tr>
    <tr><td><strong>Below 20,000</strong></td><td><strong>Spontaneous bleeding</strong>; <strong>petechiae</strong></td></tr>
    <tr><td><strong>Below 10,000</strong></td><td>Risk of <strong>spontaneous intracranial bleeding</strong> and serious hemorrhage</td></tr>
  </table>
  <p><mark class="prof-highlight">&#9733; In words:</mark> below 50,000 platelets per microliter a patient <strong>bruises easily and may bleed excessively</strong> with mild or moderate trauma or with surgery involving mucous membranes; below 20,000 there is <strong>spontaneous bleeding with petechiae</strong>; below 10,000 there is a risk of <strong>spontaneous intracranial bleeding</strong> and serious hemorrhage.</p>
  <h4 class="subsub">Three ways a platelet can be abnormal</h4>
  <table>
    <tr><th>Kind</th><th>Findings</th></tr>
    <tr><td><strong>Quantitative</strong></td><td><strong>Thrombocytopenia</strong> and <strong>extreme thrombocythemia</strong> (above 1,000 &times; 10<sup>9</sup> per liter) can both cause bleeding. Confirm a low count in a citrated or heparinized tube to exclude EDTA-induced pseudothrombocytopenia.</td></tr>
    <tr><td><strong>Morphology on the smear</strong></td><td><strong>Macrothrombocytopenia</strong> (gray platelet syndrome); <strong>neutrophil inclusions</strong> (May-Hegglin anomaly, a <em>MYH9</em> (myosin heavy chain 9) disorder); <strong>platelet clumps</strong>.</td></tr>
    <tr><td><strong>Qualitative</strong></td><td><mark class="prof-highlight">&#9733; <strong>Normal PT and aPTT with bleeding suggests platelet dysfunction.</strong></mark> Abnormal platelet function testing points to <strong>von Willebrand disease types 2 and 3, uremia or drugs</strong> (and some rarer things).</td></tr>
  </table>
  <p><strong>Macrothrombocytopenia with gray platelets on the smear is gray platelet syndrome</strong>, and neutrophil inclusions point to May-Hegglin anomaly.</p>
  @@causes@@
  <p><strong>Sequestration</strong> (hypersplenism) also lowers the circulating count (slide 25&rsquo;s heading and slide 36). The figure files hypersplenism beside massive transfusion under &ldquo;dilutional&rdquo;; the mechanism is pooling of platelets in an enlarged spleen, so learn it as sequestration.</p>
  <h4 class="subsub">Clotting and platelet tests by condition (slide 29, Table 4-9)</h4>
  <p>Slide 29 is a photograph of a textbook page; its tables are typed here. <em>PFA</em> is the platelet function analysis.</p>
  <table>
    <tr><th>Condition</th><th>PT</th><th>aPTT</th><th>PFA</th><th>Platelet count</th></tr>
    <tr><td>von Willebrand disease</td><td>Normal</td><td>Increased (factor VIII)</td><td>Abnormal</td><td>Normal</td></tr>
    <tr><td>Hemophilia A or B</td><td>Normal</td><td>Increased</td><td>Normal</td><td>Normal</td></tr>
    <tr><td>Disseminated intravascular coagulation</td><td>Increased</td><td>Increased</td><td>Abnormal</td><td>Low</td></tr>
    <tr><td>Uremia</td><td>Normal</td><td>Normal</td><td>Abnormal</td><td>Normal</td></tr>
    <tr><td>Aspirin or nonsteroidal anti-inflammatory drugs</td><td>Normal</td><td>Normal</td><td>Abnormal</td><td>Normal</td></tr>
    <tr><td>Liver failure, early</td><td>Increased</td><td>Normal</td><td>Normal</td><td>Normal</td></tr>
    <tr><td>Liver failure, late or severe</td><td>Increased</td><td>Increased</td><td>Abnormal</td><td>Low</td></tr>
    <tr><td>Immune thrombocytopenia, thrombotic thrombocytopenic purpura, hemolytic uremic syndrome, heparin-induced thrombocytopenia</td><td>Normal</td><td>Normal</td><td>Normal</td><td>Low</td></tr>
  </table>
  <p><mark class="prof-highlight">&#9733; <strong>Aspirin and other nonsteroidal anti-inflammatory drugs</strong> give a normal platelet count, PT and aPTT with an abnormal platelet function result</mark>. When platelet function is the only abnormal result, think medications and ask about over-the-counter products, because patients may not realize a product they take contains aspirin.</p>
  <p><strong>The pattern to hold:</strong> a <em>platelet</em> problem (count or function) gives a <strong>normal PT and aPTT</strong>; a low count with normal PT and aPTT fits immune thrombocytopenia, thrombotic thrombocytopenic purpura, hemolytic uremic syndrome or heparin-induced thrombocytopenia; add prolonged PT and aPTT with a low count and it is disseminated intravascular coagulation or severe liver failure.</p>
  @@ttp1@@
  @@ttp2@@

  <h3 class="sub" id="co-indications">10.7 &middot; Objective e &mdash; When to order coagulation studies</h3>
  <ul>
    <li><strong>Symptomatic bleeding or a suspicious bleeding history:</strong> the workup is a <strong>complete blood count, a peripheral smear and coagulation studies</strong>.</li>
    <li><strong>Preprocedural bleeding-risk assessment</strong> &mdash; but mild or moderate PT/aPTT prolongation does not predict bleeding in a nonbleeding patient.</li>
    <li><strong>Warfarin monitoring</strong> (the INR).</li>
    <li><strong>Suspected disseminated intravascular coagulation, liver disease or vitamin K deficiency.</strong></li>
    <li><strong>Suspected thrombosis:</strong> D-dimer, to help <strong>rule out</strong>.</li>
  </ul>
  <p>The slide&rsquo;s own summary: the patient is <strong>bleeding</strong>; the patient is <strong>clotting</strong>; the patient is <strong>bleeding and clotting at the same time</strong>; need for <strong>anticoagulation or thrombolytics</strong>; need for <strong>reversal of anticoagulation</strong>; <strong>monitoring medications</strong>; <strong>diagnosing disorders</strong> of hemostasis and thrombosis; and the <strong>perioperative</strong> setting.</p>
  <div class="pearl"><strong>Put the tests to the question.</strong> Easy bruising and bleeding gums &rarr; a bleeding workup (count, smear, PT/INR, aPTT, fibrinogen). A swollen, tender calf after surgery &rarr; a thrombotic question, but D-dimer is <em>nonspecific</em> (it also rises in pregnancy and with many acute illnesses), so a raised value after an operation tells you little and a normal value helps more than a high one. <mark class="prof-highlight">&#9733; D-dimer earns its place only when a normal result is plausible</mark>.</div>

  <h3 class="sub" id="co-interpret">10.8 &middot; Objective f &mdash; Interpreting PT, INR, aPTT and D-dimer</h3>
  <p><mark class="prof-highlight">&#9733; <strong>Where to begin.</strong> A prolonged PT or aPTT means the clotting factors, secondary hemostasis, and not the platelets. Normal PT and aPTT with bleeding means investigate the platelets next, with platelet function testing and von Willebrand studies</mark>. Bleeding and clotting are worked up with the same tests; read the pattern first.</p>
  <h4 class="subsub">Pattern-recognition table (slide 24)</h4>
  <table>
    <tr><th>PT/INR</th><th>aPTT</th><th>Fibrinogen</th><th>D-dimer</th><th>Platelets</th><th>Interpretation</th></tr>
    <tr><td>&uarr;</td><td>Normal</td><td>Normal</td><td>Normal</td><td>Normal</td><td>Liver disease, vitamin K antagonist, factor VII deficiency, oral factor Xa inhibitor</td></tr>
    <tr><td>Normal</td><td>&uarr;</td><td>Normal</td><td>Normal</td><td>Normal</td><td>Heparin or dabigatran (thrombin time also &uarr;); or factor VIII, IX or XI deficiency (<strong>with a bleeding history</strong>); or lupus anticoagulant or factor XII deficiency (<strong>no bleeding history</strong>)</td></tr>
    <tr><td>&uarr;</td><td>&uarr;</td><td>&darr;</td><td>&uarr;</td><td>&darr;</td><td><strong>Acute disseminated intravascular coagulation</strong></td></tr>
    <tr><td>Normal</td><td>Normal</td><td>Normal</td><td>&uarr;</td><td>Normal</td><td><strong>Acute thrombosis</strong> (nonspecific)</td></tr>
  </table>
  <h4 class="subsub">Patterns to watch for (slide 32)</h4>
  <table>
    <tr><th>Result</th><th>Think</th></tr>
    <tr><td><strong>Normal PT and normal aPTT, but bleeding</strong></td><td>A <strong>platelet disorder</strong>, mild von Willebrand disease, <strong>factor XIII</strong> or <strong>alpha-2 antiplasmin</strong> deficiency, or impaired fibrinolysis</td></tr>
    <tr><td><strong>Prolonged PT, normal aPTT</strong></td><td>Extrinsic pathway (<strong>factor VII</strong>), early <strong>vitamin K deficiency</strong>, liver disease, warfarin</td></tr>
    <tr><td><strong>Normal PT, prolonged aPTT</strong></td><td>Intrinsic pathway (factors VIII, IX, XI; von Willebrand disease; factor XII), inhibitors, <strong>heparin</strong>, or <strong>lupus anticoagulant</strong></td></tr>
    <tr><td><strong>Prolonged PT and prolonged aPTT</strong></td><td>Common pathway or combined deficiencies, <strong>disseminated intravascular coagulation</strong>, liver disease, severe vitamin K deficiency</td></tr>
    <tr><td><strong>Low fibrinogen and elevated D-dimer</strong></td><td>Disseminated intravascular coagulation, cirrhosis, hyperfibrinolysis</td></tr>
  </table>
  <p><strong>Factor XII deficiency prolongs the aPTT but does not cause bleeding</strong>, and lupus anticoagulant prolongs it <em>in the tube</em> without a bleeding history. A prolonged aPTT with <strong>no bleeding history</strong> therefore points to factor XII deficiency or lupus anticoagulant, while factor VIII, IX or XI deficiency comes with a bleeding history. The history decides.</p>
  <p><mark class="prof-highlight">&#9733; <strong>Acute disseminated intravascular coagulation</strong> is the pattern of a <strong>prolonged PT and aPTT, low fibrinogen, a raised D-dimer and a low platelet count</strong></mark> &mdash; nothing is normal.</p>
  <h4 class="subsub">Clotting studies by condition (slide 29, Table 4-10)</h4>
  <table>
    <tr><th>Condition</th><th>PT</th><th>aPTT</th><th>Mixing study</th><th>Thrombin time</th></tr>
    <tr><td>Inhibitor of factors VIII, IX, XI or XII; lupus antiphospholipid antibodies</td><td>Normal</td><td>Increased</td><td><strong>Abnormal</strong> (does not correct)</td><td>Normal</td></tr>
    <tr><td>Hemophilia A (factor VIII) or B (factor IX)</td><td>Normal</td><td>Increased</td><td>Normal (corrects)</td><td>Normal</td></tr>
    <tr><td>Disseminated intravascular coagulation</td><td>Increased</td><td>Increased</td><td>Normal</td><td>Increased</td></tr>
    <tr><td>Heparin</td><td>Normal</td><td>Increased</td><td>Abnormal</td><td>Increased (<strong>reptilase time normal</strong>)</td></tr>
    <tr><td>Low fibrinogen</td><td>Increased</td><td>Increased</td><td>Normal</td><td>Increased</td></tr>
    <tr><td>Factor VII deficiency</td><td>Increased</td><td>Normal</td><td>Normal</td><td>Normal</td></tr>
  </table>
  <p>Two test names from slide 27&rsquo;s notes: the <strong>reptilase time</strong> measures how quickly a clot forms with a snake-venom enzyme and mainly assesses <strong>fibrinogen function</strong> (it is normal with heparin, which is how heparin effect is separated from a fibrinogen problem); the <strong>dilute Russell viper venom time</strong> detects <strong>lupus anticoagulant</strong>.</p>
  <h4 class="subsub">Disseminated intravascular coagulation (slide 30)</h4>
  <table>
    <tr><th>Test</th><th>In disseminated intravascular coagulation</th><th>Other causes of the same result</th></tr>
    <tr><td>Platelet count</td><td>Decreased</td><td>Sepsis, impaired production, major blood loss, hypersplenism</td></tr>
    <tr><td>Prothrombin time</td><td>Prolonged</td><td>Vitamin K deficiency, liver failure, major blood loss</td></tr>
    <tr><td>aPTT</td><td>Prolonged</td><td>Liver failure, heparin treatment, major blood loss</td></tr>
    <tr><td>Fibrin degradation products</td><td>Elevated</td><td>Surgery, trauma, infection, hematoma</td></tr>
    <tr><td>Protease inhibitors (protein C, antithrombin, protein S)</td><td>Decreased</td><td>Liver failure, capillary leakage</td></tr>
  </table>
  <p>No single line of this table proves the diagnosis; <strong>every abnormality has another cause</strong>, which is why the picture (low platelets, long PT and aPTT, low fibrinogen, high D-dimer) matters rather than any one value.</p>
  <h4 class="subsub">An isolated prolonged aPTT, step by step (slide 27)</h4>
  @@ptt@@
  <ol>
    <li><strong>Rule out heparin effect</strong> first, then measure <strong>fibrinogen activity</strong>.</li>
    <li><strong>Fibrinogen low</strong> (below 100 mg/dL on the algorithm): measure fibrinogen antigen. Low antigen = <strong>hypofibrinogenemia</strong>; normal antigen = <strong>dysfibrinogenemia</strong>.</li>
    <li><strong>Fibrinogen high</strong>: do an <strong>immediate 1:1 mix</strong> (also incubated).</li>
    <li><strong>Corrects</strong> &rarr; factor deficiency &rarr; factor VIII assay. A <strong>low factor VIII</strong> &rarr; von Willebrand antigen and activity: <strong>abnormal = von Willebrand disease; normal = hemophilia</strong>. A normal factor VIII &rarr; assays for factors IX, XI and XII.</li>
    <li><strong>Fails to correct</strong> &rarr; an inhibitor &rarr; phospholipid neutralization (dilute Russell viper venom time): <strong>phospholipid-dependent = lupus anticoagulant</strong>; not dependent = a <strong>specific factor inhibitor</strong> (confirm with an inhibitor screen and the Bethesda assay).</li>
  </ol>
  <p>Take-away from the notes: if only the aPTT is abnormal, <strong>keep hemophilia in the back of your mind</strong>.</p>
  <h4 class="subsub">A suspected inherited bleeding disorder (slide 28)</h4>
  @@inh@@
  <p>Start with the PT, aPTT, thrombin time or fibrinogen activity assay.</p>
  <table>
    <tr><th>Screens</th><th>Think</th><th>Next</th></tr>
    <tr><td><strong>All normal</strong></td><td><strong>Platelet disorders and mild von Willebrand disease</strong>: skin bruising, petechiae, mucous membrane bleeding.</td><td>Platelet function analyzer closure time or bleeding time, platelet count and morphology, aggregation study, von Willebrand antigen and activity</td></tr>
    <tr><td><strong>All normal</strong></td><td><strong>Deficiency of inhibitors of the fibrinolytic system</strong>: severe bleeding, including hemarthroses and hematoma after trauma or surgery.</td><td>Euglobulin clot lysis time; alpha-2 antiplasmin and plasminogen activator inhibitor 1</td></tr>
    <tr><td><strong>All normal</strong></td><td><strong>Factor XIII deficiency</strong>: umbilical stump bleeding and lifelong severe bleeding of any tissue.</td><td>Clot stability test; factor XIII assay</td></tr>
    <tr><td><strong>Prolonged</strong></td><td><strong>Clotting factor deficiency</strong> (mild, moderate or severe): large, often palpable ecchymoses and bleeding into deep soft tissues (joints, muscles) with hematoma formation.</td><td>Split by the pattern below; then selective factor assays and/or fibrinogen activity and antigen</td></tr>
  </table>
  <table>
    <tr><th>Prolonged screen</th><th>Deficiency</th></tr>
    <tr><td><strong>PT only</strong></td><td><strong>Factor VII</strong></td></tr>
    <tr><td><strong>aPTT only</strong></td><td><strong>Factor VIII (hemophilia A), IX (hemophilia B) or XI</strong>; severe von Willebrand disease</td></tr>
    <tr><td><strong>PT and aPTT</strong></td><td><strong>Normal thrombin time:</strong> deficiency of factor X, V or II (or combined factor V and VIII deficiency). <strong>Prolonged thrombin time:</strong> hypofibrinogenemia or dysfibrinogenemia.</td></tr>
  </table>
  <p class="muted">The footnote on slide 28: the fibrinogen activity assay is now routinely available and has largely replaced the thrombin time for evaluating fibrinogen function.</p>

  <button type="button" class="test-yourself-btn" style="--acc:#a1363a" onclick="window.openTestYourself('Test yourself &mdash; Coagulation &amp; Hemostasis Testing', TEST_YOURSELF.coagulation)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>Coagulation Studies 2026.pptx</em> (Professor Lauren Reynolds). Slides 4, 5, 14, 15, 17 and 25 are pictures and are reproduced above; slides 27 and 28 (algorithms) and 29 and 30 (tables) are also pictures and are typed out. Slide 36 (disorders of hemostasis and thrombosis) is material for Clinical Medicine and Surgery I and is not restated; slide 37 is a cartoon. Where the deck and current practice differ, the guide says which it teaches.@@COVERAGE@@</footer>
</section>
"""

TOC = """  <a class="top-link" href="#coagulation">10 &middot; Coagulation &amp; Hemostasis Testing</a>
  <a href="#co-define">10.1 Objective a &mdash; The seven terms</a>
  <a href="#co-primary">10.2 Objective b.i &mdash; Primary hemostasis tests</a>
  <a href="#co-secondary">10.3 Objective b.ii &mdash; Secondary hemostasis tests</a>
  <a href="#co-fibrinolysis">10.4 Objective b.iii &mdash; Fibrinolysis tests</a>
  <a href="#co-compare">10.5 Objective c &mdash; Bleeding versus thrombotic</a>
  <a href="#co-platelets">10.6 Objective d &mdash; Platelet abnormalities</a>
  <a href="#co-indications">10.7 Objective e &mdash; When to order</a>
  <a href="#co-interpret">10.8 Objective f &mdash; Interpreting the results</a>
"""

TY = '''    "coagulation": [
      {q:"Which test is ordered to help exclude thrombosis because a normal result is reassuring?", choices:["D-dimer","Prothrombin time","Fibrinogen level","Bleeding time"], correct:0,
       explain:"D-dimer is nonspecific, so a high value proves little, but its high negative predictive value means a normal result helps exclude thrombosis."},
      {q:"A patient has a prolonged prothrombin time and a normal activated partial thromboplastin time. Which pathway is implicated?", choices:["Extrinsic pathway (factor VII)","Intrinsic pathway (factors VIII, IX, XI)","Platelet adhesion","Fibrinolysis"], correct:0,
       explain:"The prothrombin time tests the extrinsic (tissue factor, factor VII) and common pathways; the activated partial thromboplastin time tests the intrinsic and common pathways."},
      {q:"In a mixing study, what does failure to correct a prolonged activated partial thromboplastin time suggest?", choices:["An inhibitor","A factor deficiency","A platelet disorder","Fibrinolysis"], correct:0,
       explain:"Correction suggests a factor deficiency (normal plasma supplies the missing factor); no correction suggests an inhibitor, such as lupus anticoagulant or a specific factor inhibitor."},
      {q:"Which pattern fits acute disseminated intravascular coagulation?", choices:["Prolonged screening clotting times, low fibrinogen and platelets, high D-dimer","Normal clotting times with only a high D-dimer","Prolonged prothrombin time only","Prolonged partial thromboplastin time only"], correct:0,
       explain:"Consumption of platelets and factors with fibrinolysis gives prolonged screens, low fibrinogen and platelets and a raised D-dimer. A high D-dimer alone is acute thrombosis."},
      {q:"A patient on warfarin has an INR below the target range. What is the main concern?", choices:["Clot risk","Bleeding risk","Platelet failure","Vitamin K excess"], correct:0,
       explain:"On warfarin, a low INR means too little anticoagulation (clot risk) and a high INR means bleeding risk."}
    ],
'''


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for tag in ("PDML10", "PDMTOC10"):
        src = re.sub(r"<!--%s-->.*?<!--/%s-->\s*" % (tag, tag), "", src, flags=re.S)
    src = re.sub(r"\n<!--PDMTY10-->.*?<!--/PDMTY10-->", "", src, flags=re.S)

    body = SEC
    for k, v in F.items():
        token = "@@%s@@" % k
        assert token in body, "figure token %s unused" % k
        body = body.replace(token, v)
    emph = ""
    coverage = ""
    if os.path.exists(RECORDING_NOTE_FILE):
        blob = open(RECORDING_NOTE_FILE, encoding="utf-8").read()
        assert "<!--COVERAGE-->" in blob
        emph, coverage = blob.split("<!--COVERAGE-->", 1)
    body = body.replace("@@EMPH@@", emph.strip() + "\n").replace("@@COVERAGE@@", coverage.strip())
    assert "@@" not in body, "unfilled token"

    anchor = '<footer class="guide-foot">\n  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html"'
    assert src.count(anchor) == 1, "main-level footer anchor not found once"
    src = src.replace(anchor, "<!--PDML10-->" + body + "<!--/PDML10-->\n\n" + anchor, 1)

    navend = src.index("</nav>")
    src = src[:navend] + "<!--PDMTOC10-->\n" + TOC + "<!--/PDMTOC10-->\n" + src[navend:]

    tyend = src.index("\n  };\n</script>", src.index("var TEST_YOURSELF"))
    src = src[:tyend] + "\n<!--PDMTY10-->\n" + TY.rstrip() + "\n<!--/PDMTY10-->" + src[tyend:]
    assert TY.rstrip().endswith("],"), "TEST_YOURSELF entry must end with a comma (it is not the last key of the object in intent)"

    src = src.replace("<p>Covers Lectures 7, 8 and 9 &middot; Lecture 10 (Coagulation and Hemostasis Testing) is added when its deck is posted &middot; Instructional Objectives (IOs) taken verbatim from the syllabus</p>",
                      "<p>Covers Lectures 7, 8, 9 and 10 &middot; Instructional Objectives (IOs) taken verbatim from the syllabus</p>")

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li", "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for m in re.finditer(r'href="#([a-z0-9-]+)"', src):
        assert 'id="%s"' % m.group(1) in src, "dangling TOC link " + m.group(1)
    brit = re.findall(r"(?i)\b\w*(?:haem|oedem|tumour|colour|centre|anaem|oesoph|isation|oris[ei]|ognis[ei]|analyse)\w*\b", body)
    brit = [w for w in brit if w.lower() not in ("haemophilus",)]
    assert not brit, "British spelling: %r" % sorted(set(brit))
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 10: %d subsections, %d figures, %d test-yourself questions, emphasis block %s"
          % (len(re.findall(r'<h3 class="sub" id="co-', src)), body.count('<figure class="fig">'),
             TY.count("{q:"), "YES" if emph.strip() else "not yet"))


if __name__ == "__main__":
    main()
