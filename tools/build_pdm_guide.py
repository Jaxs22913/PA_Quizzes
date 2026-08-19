#!/usr/bin/env python3
"""Build the Principles of Diagnostic Medicine I, Exam 1 study guide.

Skeleton lifted from the PD1 Exam 3 guide, which carries the site's guide design
system; retheme is the plum identity established for this exam by its quizzes.

Exam 1 covers Lectures 1-6 and Lab 1. Only Lecture 1 exists so far, so this is
one section and grows as each deck is posted. Lab content is deliberately absent
- Jaxon wants lecture content only for now, and how the labs get folded in is a
decision we make together when that material arrives.

Instructional Objectives are VERBATIM from the syllabus (a-o) and each is
answered in order.

Throughout, the guide reflects how Professor Reynolds said this course is
examined, taken from the 2026-08-18 recording and confirmed against Notability's
independent transcript: reference ranges are always supplied, predictive values
are never calculated, and the tube objective means the order of draw and the
common colour-to-test pairings rather than the deck's exhaustive additive table.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from extract_pdm_figures import figure_html

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Physical Diagnosis 1 Exam 3/pd1-exam3-study-guide.html")
OUT = os.path.join(ROOT, "Principles of Diagnostic Medicine I Exam 1/pdm-exam-1-study-guide.html")
IMGDIR = "pdm-exam-1-study-guide-images"
F = figure_html(IMGDIR)

TOC = '''<nav class="toc">
  <h2>Contents</h2>
  <a class="top-link" href="#lab-diagnostics">1 &middot; Principles of Laboratory Diagnostics</a>
  <a href="#ld-role">1.1 Objectives a &amp; b &mdash; Role of testing &amp; patient counseling</a>
  <a href="#ld-phases">1.2 Objectives c &amp; d &mdash; The three phases</a>
  <a href="#ld-tubes">1.3 Objective e &mdash; Collection tubes &amp; order of draw</a>
  <a href="#ld-cultures">1.4 Objective f &mdash; Stool, blood, sputum &amp; throat studies</a>
  <a href="#ld-poct">1.5 Objectives g, h &amp; j &mdash; Point-of-care testing</a>
  <a href="#ld-qualquant">1.6 Objective i &mdash; Qualitative versus quantitative</a>
  <a href="#ld-quality">1.7 Objectives k &amp; l &mdash; Quality assurance &amp; regulation</a>
  <a href="#ld-screening">1.8 Objective n &mdash; Screening versus diagnostic</a>
  <a href="#ld-stats">1.9 Objectives m &amp; o &mdash; Sensitivity, specificity &amp; predictive value</a>
</nav>'''

BODY = '''<main>

<section class="deck" id="lab-diagnostics">
  <h2 class="deck-title">1 &middot; Principles of Laboratory Diagnostics</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 1: Principles of Laboratory Diagnostics</p>
    <ol type="a">
      <li>Define the importance and role of laboratory testing in the evaluation of a patient.</li>
      <li>Discuss the importance of patient counseling for diagnostic testing to reduce medical errors.</li>
      <li>Describe the phases of the diagnostic testing process: pretest phase, intratest phase, posttest phase.</li>
      <li>Explain the components of the: pretest phase, intratest phase, posttest phase.</li>
      <li>Identify which colored laboratory collection tubes correspond to common laboratory tests.</li>
      <li>Define the purpose and appropriate use of: stool studies, throat cultures, sputum cultures, blood cultures.</li>
      <li>Define point-of-care (POC) testing.</li>
      <li>Discuss common point-of-care tests performed in primary care and acute care settings.</li>
      <li>Compare and contrast qualitative and quantitative diagnostic tests.</li>
      <li>Discuss the availability, advantages, and limitations of point-of-care testing.</li>
      <li>Describe quality assurance measures necessary for point-of-care testing.</li>
      <li>Discuss accreditation and regulatory considerations related to point-of-care testing.</li>
      <li>Define sensitivity, specificity, positive predictive value, and negative predictive value.</li>
      <li>Differentiate between screening tests and diagnostic tests.</li>
      <li>Explain the concepts of pretest probability and posttest probability.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; How this course is examined</span>
  <p>Professor Reynolds answered &ldquo;what are the exams going to be like?&rdquo; in the first three
  minutes of Lecture 1. Four things follow from it, and they shape this whole guide:</p>
  <table>
    <tr><th>She said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;We always also give you the normal ranges &hellip; I&rsquo;m not going to just throw a random number at you and not give you context of whether that&rsquo;s high or low.&rdquo;</em></td><td><strong>Do not memorise reference values.</strong> If a lab value appears in a stem, its range appears with it &mdash; on this exam and, she said, in every class. Spend the effort on what the value <em>means</em>.</td></tr>
    <tr><td><em>&ldquo;It will be based on the instructional objectives &hellip; more related to the tests themselves rather than maybe the specific diagnosis.&rdquo;</em></td><td>Study <strong>the test</strong>: what to order, why, its limits, how to read it. The objectives above are the blueprint.</td></tr>
    <tr><td><em>&ldquo;Although a heart rhythm can be a diagnosis, you also need to be able to interpret an EKG by naming the rhythm.&rdquo;</em></td><td>The one stated exception. It lands on Lectures 7 and 11&ndash;16, so Exams 2 and 3.</td></tr>
    <tr><td><em>&ldquo;There could be pictures &hellip; images of x-rays or CT scans &hellip; in addition to the vignette.&rdquo;</em></td><td>Expect image-based vignettes, not only text.</td></tr>
  </table>
  <p>Her question style, in her own words: <em>&ldquo;which of the following laboratory tests would be
  best to evaluate a patient with microscopic anemia?&rdquo;</em> &middot; <em>&ldquo;what would be the next
  test that you would order?&rdquo;</em></p></div>

  <h3 class="sub" id="ld-role">1.1 &middot; Objectives a &amp; b &mdash; The role of testing, and counseling the patient</h3>
  <p>Diagnostics are <strong>tools to gain additional information</strong>, used <em>in conjunction with</em>
  a thorough history and physical examination &mdash; not in place of them. They are not necessarily
  therapeutic, though a blood culture that returns sensitivities certainly can be.</p>
  <table>
    <tr><th>What testing does</th></tr>
    <tr><td>Confirms a diagnosis &middot; informs health status &middot; evaluates disease severity &middot; directs treatment &middot; monitors response to therapy &middot; guides ongoing care through regular screening</td></tr>
  </table>
  <div class="pearl"><strong>Two questions before you order anything:</strong> will it support or guide
  management, and is it cost effective? Appropriateness for <em>this</em> patient comes before
  availability or turnaround.</div>
  <p><strong>Counseling is framed as error reduction, not courtesy.</strong> Patients who are informed and
  understand the plan are more likely to be compliant, and compliance is what makes the result
  meaningful. Education covers the testing process, their questions, and the anticipated timeline
  for results.</p>
  <table>
    <tr><th>Effective diagnostic testing</th></tr>
    <tr><td>Communicate clearly &middot; consider ethnicity, culture, gender and age &middot; prepare the patient properly &middot; follow standards &middot; measure and evaluate outcomes &middot; manage services with a team approach &middot; interpret, treat, monitor and counsel on abnormal outcomes &middot; maintain proper records</td></tr>
  </table>

  <h3 class="sub" id="ld-phases">1.2 &middot; Objectives c &amp; d &mdash; The three phases</h3>
  <p>Each phase has its own guidelines and standards, and each has its own characteristic failures.</p>
  <table>
    <tr><th>Phase</th><th>Also called</th><th>Span</th></tr>
    <tr><td><strong>Pretest</strong></td><td>Preanalytical</td><td>Begins with patient preparation, extends until the test begins</td></tr>
    <tr><td><strong>Intratest</strong></td><td>Analytical</td><td>Performing the test and everything it encompasses</td></tr>
    <tr><td><strong>Posttest</strong></td><td>Postanalytical</td><td>Begins once the test is complete; focuses on aftercare</td></tr>
  </table>
  <div class="pearl"><strong>Most errors occur in the pretest phase.</strong> That is the single most
  testable fact in this section, and it is why so much of the objective is about preparation,
  labeling and communication rather than about the assay.</div>
  <table>
    <tr><th>Pretest &mdash; what to consider</th><th>Pretest &mdash; how it fails</th></tr>
    <tr><td>Review history and risk assessment &middot; identify contraindications &middot; assess coping styles, fears and phobias &middot; observe universal precautions &middot; document relevant data &middot; cost and reimbursement &middot; patient and family education &middot; documentation &middot; ethical and legal considerations, including consent</td><td><strong>Communication errors</strong> &middot; medication administration as directed &middot; proper labeling &middot; <strong>technical errors</strong> &mdash; inadequate blood in the vacuum tube, delay in transport, inappropriate preparation and storage &middot; <strong>inappropriate patient preparation</strong> &mdash; fasting</td></tr>
  </table>
  <p><strong>Variables that can affect results:</strong> patient preparation &middot; current drug therapy
  &middot; time of specimen collection &middot; physical activity &middot; hydration status &middot; age
  &middot; sex &middot; body mass index.</p>
  <table>
    <tr><th>Intratest</th><th>Posttest</th></tr>
    <tr><td>Specimen or tissue collection &middot; monitoring the testing environment &middot; performing or assisting the procedure &middot; providing emotional and physical comfort &middot; administering analgesics and sedatives &middot; monitoring vital signs &middot; universal precautions &middot; proper collection &middot; minimizing delays &middot; monitoring for side effects or complications</td><td>Monitor for complications &mdash; <strong>bleeding, infection, respiratory difficulties, perforation, adverse effects of sedation or anesthesia</strong> &middot; interpret results and the patient's response &middot; <strong>identify and treat critical values</strong> &middot; communicate results clearly and sensitively</td></tr>
  </table>
  <div class="callout"><strong>Integration and follow-up</strong> is the second half of the posttest phase:
  diagnosis, acceptance, healing and health-promoting behavior. It includes patient education,
  ordering appropriate follow-up labs, scheduling follow-up, making referrals, and considering
  emotional well-being. Behavioural responses to a significant diagnosis <em>may last several weeks
  or longer</em>. And on documentation: <em>&ldquo;if it wasn&rsquo;t documented, it wasn&rsquo;t
  done&rdquo;</em>.</div>

  <h3 class="sub" id="ld-tubes">1.3 &middot; Objective e &mdash; Collection tubes and the order of draw</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor narrowed this objective</span>
  <p>The deck carries a two-dozen-row table pairing every additive to every stopper colour. She does
  not want it memorised. <em>&ldquo;The thing I want you to know better, have a better handle on, is
  kind of the <strong>order</strong> and sort of the <strong>broad category</strong> &mdash; so light
  blue, think coags; lavender, we&rsquo;re gonna be using this for like our CBC.&rdquo;</em> Then:
  <em>&ldquo;the order is important. I kind of want you to have an idea of the order.&rdquo;</em></p>
  <p>Her test of whether you know it: if you ordered coagulation studies and someone walks in with a
  lavender tube, you should immediately know that is the wrong tube.</p></div>
  ''' + F["order-of-draw"] + '''
  <table>
    <tr><th>Order</th><th>Tube</th><th>Contents</th><th>Think</th></tr>
    <tr><td>1</td><td>Yellow</td><td>Sterile media</td><td><strong>Blood cultures</strong></td></tr>
    <tr><td>2</td><td>Light blue</td><td>Sodium citrate</td><td><strong>Coagulation studies</strong></td></tr>
    <tr><td>3</td><td>Red</td><td>Non-additive serum tube</td><td>Serum chemistry</td></tr>
    <tr><td>4</td><td>Gold / tiger</td><td>Serum separator</td><td>Serum chemistry</td></tr>
    <tr><td>5</td><td>Green</td><td>Heparin</td><td>Plasma chemistry</td></tr>
    <tr><td>6</td><td>Lavender</td><td>Ethylenediaminetetraacetic acid</td><td><strong>Complete blood count</strong></td></tr>
    <tr><td>7</td><td>Gray</td><td>Glycolytic inhibitor</td><td>Glucose</td></tr>
  </table>
  <div class="pearl"><strong>Why the order exists:</strong> to avoid cross-contamination of additives
  between tubes. Carry over a little ethylenediaminetetraacetic acid into a chemistry tube and the
  potassium comes back wrong &mdash; the sequence is a contamination control, not a convention. The
  <strong>clear</strong> tube is a discard tube, used to fill the collection set's dead space before
  the coagulation tube when no royal blue is drawn.</div>

  <h3 class="sub" id="ld-cultures">1.4 &middot; Objective f &mdash; Stool, blood, sputum and throat studies</h3>
  <div class="pearl"><strong>One rule spans three of the four:</strong> get the specimen <em>before</em>
  starting antibiotics. Stated for blood, sputum and throat cultures alike.</div>
  <table>
    <tr><th>Study</th><th>Purpose and use</th><th>The detail that gets tested</th></tr>
    <tr><td><strong>Stool studies</strong></td><td>Non-invasive; diagnostic or screening. Indications: diarrhea, excessive flatus, abdominal discomfort, change in stool colour, recent travel, well water, prolonged antibiotics. Identifies overgrowth of normal flora, toxins, acquired bacteria, parasites</td><td>Specimen must be <strong>uncontaminated with urine or other secretions</strong>, in a dry clean container</td></tr>
    <tr><td><strong>Ova &amp; parasites</strong></td><td>Part of stool studies</td><td><strong>Do NOT refrigerate</strong> &mdash; warm stool is best. <strong>Three separate random specimens</strong>, because of the parasite life cycle</td></tr>
    <tr><td><strong>Guaiac</strong></td><td>Detects fecal occult blood; from a specimen or from the gloved finger after digital rectal examination</td><td>Heme oxidises the hydrogen peroxide in the guaiac &rarr; <strong>blue = positive</strong>. Use a <strong>small</strong> sample; a large one obscures the result</td></tr>
    <tr><td><strong>Blood cultures</strong></td><td>Acute febrile illness with suspicion of septicemia. <strong>Both diagnostic and therapeutic</strong> &mdash; identifies the pathogen <em>and</em> gives sensitivities</td><td><strong>Two separate samples from opposite arms</strong>, ideally before antibiotics. <strong>Aerobic first.</strong> Scrub and let dry; <strong>do not palpate after disinfection</strong> unless wearing sterile gloves</td></tr>
    <tr><td><strong>Sputum culture</strong></td><td>Identifies respiratory pathogens and directs treatment</td><td>Two steps: <strong>Gram stain first</strong> (positive versus negative), then culture for identification and sensitivities. Sit upright, rinse mouth with water, three deep breaths, deep cough. Aerosols may assist. Acid-fast bacilli can be done from the same specimen</td></tr>
    <tr><td><strong>Throat culture</strong></td><td>Isolates the pathogen, often streptococci, because of beta-hemolytic streptococcal pharyngitis. Most common ages <strong>3&ndash;15</strong>; in adults, severe or recurrent sore throat, fever, palpable lymphadenopathy</td><td>Tongue blade improves visualization, relaxes the throat and reduces gag. Rotate the swab over the <strong>posterior throat, both tonsils</strong>, and any inflammation, exudate or ulceration. <strong>Avoid the tongue and lips.</strong> Rapid immunologic tests are highly accurate</td></tr>
  </table>

  <h3 class="sub" id="ld-poct">1.5 &middot; Objectives g, h &amp; j &mdash; Point-of-care testing</h3>
  <p><strong>Definition:</strong> medical testing completed <em>outside the centralized laboratory</em>,
  at or close to the site of patient care. Also called near-patient, remote, satellite laboratory
  testing, or rapid diagnostics. Traditional testing is multi-step and delays treatment; this brings
  the laboratory to the patient.</p>
  <table>
    <tr><th>Universal features</th></tr>
    <tr><td>Simple to use &middot; reagents durable in storage and use &middot; <strong>results align with established laboratory methods</strong> &middot; safe during testing &middot; performable by medical assistants, first responders, physicians, physician assistants, nurses and others &mdash; some by non-medical individuals at home</td></tr>
  </table>
  <table>
    <tr><th>Common in primary care</th><th>Common in acute care</th></tr>
    <tr><td>Blood glucose &middot; hemoglobin A1c &middot; urinalysis &middot; rapid influenza &middot; rapid strep &middot; fecal occult blood &middot; pregnancy testing &middot; cholesterol &middot; prothrombin time with international normalized ratio &middot; drug screening<br><em>Rapidly increasing: fentanyl and human immunodeficiency virus testing</em></td><td>Venous blood gas &middot; point-of-care glucose &middot; <strong>troponin</strong> &middot; brain natriuretic peptide &middot; D-dimer &middot; prothrombin time with international normalized ratio &middot; hemoglobin and hematocrit &middot; rapid antigen tests &middot; urine human chorionic gonadotropin &middot; urinalysis dipsticks<br><em>Machines: portable x-ray, electrocardiography, pulse oximetry, ultrasound</em></td></tr>
  </table>
  <table>
    <tr><th>Advantages</th><th>Limitations</th></tr>
    <tr><td>Convenience &middot; rapid, less manpower &middot; reduced visits &middot; fingerstick rather than needle stick &middot; <strong>better care where resources are limited</strong> &mdash; rural, disaster zone</td><td>Expensive &middot; quality assurance difficult to control &middot; <strong>operator and manufacturer variability</strong> &middot; vocabulary not always standardised &middot; <strong>results may be less precise</strong> &middot; supply needs</td></tr>
  </table>
  <div class="pearl">The advantage and the limitation are the same coin. It is fast and close to the
  patient <em>because</em> it is not the central laboratory &mdash; which is also why it is less
  precise and harder to quality-control.</div>

  <h3 class="sub" id="ld-qualquant">1.6 &middot; Objective i &mdash; Qualitative versus quantitative</h3>
  <table>
    <tr><th></th><th>Qualitative</th><th>Quantitative</th></tr>
    <tr><td>Answers</td><td>&ldquo;Why&rdquo; questions</td><td>&ldquo;How many / how much&rdquo; questions</td></tr>
    <tr><td>Data</td><td>Observation, description</td><td>Numbers, statistical results</td></tr>
    <tr><td>Approach</td><td>Observe and interpret</td><td>Measure and test</td></tr>
    <tr><td>Analysis</td><td>Grouping of common data; non-statistical</td><td>Statistical analysis</td></tr>
  </table>
  ''' + F["urinalysis-dipstick"] + '''
  <table>
    <tr><th>Analyser type</th><th>Examples</th></tr>
    <tr><td>Qualitative or semi-quantitative cartridge</td><td>Rapid strep (qualitative), influenza (qualitative), <strong>urinalysis dipstick (semi-quantitative)</strong>, pregnancy (qualitative)</td></tr>
    <tr><td>Single-use quantitative cartridge or strip with a reader</td><td><strong>Glucose &mdash; the highest-volume point-of-care test</strong>, blood chemistries, coagulation, cardiac markers, C-reactive protein, hemoglobin A1c, arterial blood gases, electrolytes</td></tr>
    <tr><td>Multiple-use quantitative cartridge / benchtop</td><td>Hemoglobin species with arterial blood gas, bilirubin, electrolytes, cardiac markers, drugs</td></tr>
  </table>
  <p><strong>Non-instrumental</strong> point-of-care testing does not rely on instrumentation to
  interpret the result &mdash; urine pregnancy, coronavirus tests, fecal occult blood. <strong>Handheld</strong>
  equipment is easy to carry, one to two steps, few data points. <strong>Benchtop</strong> devices are
  stationary, multi-step, multiple data points. Both usually need reagents and consumables.</p>

  <h3 class="sub" id="ld-quality">1.7 &middot; Objectives k &amp; l &mdash; Quality assurance and regulation</h3>
  <table>
    <tr><th>Quality measures for point-of-care testing</th></tr>
    <tr><td>Supervising testing and delivery of results &middot; operators trained and competent &middot; collection per the device instructions &middot; <strong>accurate patient identification</strong> throughout testing and reporting &middot; quality control &middot; <strong>active enrollment in an External Quality Assurance program</strong> &middot; devices connected to electronic information systems to minimise post-testing errors &middot; a safe, secure working environment</td></tr>
  </table>
  <p><strong>Clinical Laboratory Improvement Amendments (CLIA)</strong> &mdash; federal guidelines setting
  <em>minimum</em> quality standards for testing human samples at all types of sites. It began in the
  late 1960s after problems in the cytology laboratories reading Papanicolaou smears.</p>
  <table>
    <tr><th>Complexity category</th><th>What it means</th></tr>
    <tr><td>Waived</td><td>Little chance of a negative outcome from a false result. <strong>The Joint Commission classifies all testing outside a traditional laboratory as waived &mdash; that is, point-of-care testing</strong></td></tr>
    <tr><td>Moderately complex</td><td><strong>The majority &mdash; roughly 75% of the 12,000 available tests.</strong> Usually automated</td></tr>
    <tr><td>Highly complex</td><td>Requires operator skill and decision making; not fully automated; complex instrumentation, such as cross match testing</td></tr>
    <tr><td>Provider-performed microscopy</td><td>Slide examination of a freshly collected specimen by a provider &mdash; Gram stain, manual cell count</td></tr>
  </table>
  <table>
    <tr><th>Agency</th><th>Role</th></tr>
    <tr><td>Centers for Medicare &amp; Medicaid Services</td><td>Issues certificates &middot; collects user fees &middot; <strong>inspects and enforces</strong> &middot; approves accreditation organizations &middot; monitors proficiency testing &middot; publishes the rules</td></tr>
    <tr><td>Food and Drug Administration</td><td><strong>Categorizes tests by complexity</strong> &middot; reviews waiver applications &middot; develops categorization guidance</td></tr>
    <tr><td>Centers for Disease Control and Prevention</td><td>Analysis, research and technical assistance &middot; technical standards and practice guidelines &middot; quality improvement studies &middot; manages the advisory committee</td></tr>
  </table>
  <div class="pearl"><strong>The direction of regulation only goes one way.</strong> Every testing site must
  be licensed to perform <em>any</em> test, the licence must match the complexity performed, and sites
  reapply <strong>every two years</strong>. States and cities may add requirements but may never
  downgrade them &mdash; so local regulation is always <em>stricter</em> than the federal floor, never
  looser.</div>

  <h3 class="sub" id="ld-screening">1.8 &middot; Objective n &mdash; Screening versus diagnostic</h3>
  <table>
    <tr><th></th><th>Screening</th><th>Diagnostic</th></tr>
    <tr><td>Who</td><td><strong>Asymptomatic</strong> person &mdash; looking for evidence of disease</td><td>Person <strong>with symptoms</strong> &mdash; looking for the reason</td></tr>
    <tr><td>Character</td><td>Typically inexpensive, easy to perform</td><td>May be more invasive, with risk of complications</td></tr>
    <tr><td>Output</td><td>Indicates whether more testing is needed; not necessarily a diagnosis</td><td>Confirmation &mdash; the &ldquo;definitive&rdquo; diagnosis</td></tr>
    <tr><td>Sequence</td><td>Do this first, before the expensive or time-consuming test</td><td>Follows an abnormal screen, or investigates symptoms directly</td></tr>
  </table>
  <div class="pearl">The two are not fixed labels on a test &mdash; they are roles. <strong>A screening
  test becomes diagnostic if an abnormality is found during it</strong>: a screening colonoscopy that
  finds and biopsies a lesion has changed role mid-procedure.</div>

  <h3 class="sub" id="ld-stats">1.9 &middot; Objectives m &amp; o &mdash; Sensitivity, specificity and predictive value</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; No arithmetic on this exam</span>
  <p>Walking the shark-bite example, she stopped before the numbers: <em>&ldquo;What do we think the
  percentage &mdash; we don&rsquo;t, we&rsquo;re not gonna do math, <strong>I&rsquo;m not gonna make you
  do math</strong>&rdquo;</em> &mdash; and then asked only which scenario has the higher positive
  predictive value.</p>
  <p>So learn the <em>direction</em> and the <em>reason</em>, not the formula. The worked figures below
  are here to make the reasoning concrete, not to be recomputed.</p></div>
  <table>
    <tr><th></th><th>Sensitivity</th><th>Specificity</th></tr>
    <tr><td>Measures</td><td>Test is positive when the person <strong>does</strong> have the condition</td><td>Test is negative when the person <strong>does not</strong> have the condition</td></tr>
    <tr><td>Good at</td><td><strong>Detecting</strong> disease</td><td><strong>Excluding</strong> disease</td></tr>
    <tr><td>Fewer</td><td>False negatives <span class="tag">does not address false positives</span></td><td>False positives <span class="tag">does not address false negatives</span></td></tr>
    <tr><td>Mnemonic</td><td><strong>SnNout</strong> &mdash; high Sensitivity + Negative rules <em>out</em></td><td><strong>SpPin</strong> &mdash; high Specificity + Positive rules <em>in</em></td></tr>
    <tr><td>Best for</td><td><strong>Screening</strong></td><td><strong>Confirming</strong></td></tr>
    <tr><td>Example</td><td>Human immunodeficiency virus screening &mdash; very few infected individuals are missed</td><td>Human immunodeficiency virus confirmatory testing &mdash; minimises false-positive diagnoses</td></tr>
  </table>
  ''' + F["threshold-sensitivity"] + F["threshold-specificity"] + '''
  <div class="pearl"><strong>The two figures above are one dataset and one dial.</strong> Move the
  threshold down and you catch every case but collect false positives; move it up and you exclude
  cleanly but miss cases. That trade-off is why a sensitive test screens and a specific test confirms
  &mdash; and why the human immunodeficiency virus pathway runs sensitive first, specific second.</div>
  <table>
    <tr><th>Measure</th><th>Question it answers</th><th>Belongs to</th></tr>
    <tr><td>Sensitivity</td><td>If the disease is present, will the test be positive?</td><td rowspan="2"><strong>The test</strong> &mdash; test-centered</td></tr>
    <tr><td>Specificity</td><td>If the disease is absent, will the test be negative?</td></tr>
    <tr><td><strong>Positive predictive value</strong></td><td><strong>My patient&rsquo;s test is positive &mdash; do they actually have it?</strong></td><td rowspan="2"><strong>The population</strong> &mdash; patient-centered</td></tr>
    <tr><td>Negative predictive value</td><td>My patient&rsquo;s test is negative &mdash; are they actually clear?</td></tr>
  </table>
  <div class="callout"><strong>The trap, named in the lecture.</strong> A clinician asks &ldquo;my
  patient&rsquo;s test is positive, what is the probability they have the disease?&rdquo; and reaches for
  SnNout and SpPin &mdash; that is, for sensitivity. <em>But it is not sensitivity, it is the positive
  predictive value.</em> Sensitivity is the probability the test is positive <em>given</em> disease;
  predictive value is the probability of disease <em>given</em> the test. <strong>That reversal of
  conditioning is the foundation of Bayes&rsquo; theorem</strong>, and prevalence &mdash; the pre-test
  probability &mdash; is what carries you across it.</div>
  <table>
    <tr><th>Frostbite in January, same test, 95% sensitivity and 95% specificity</th></tr>
    <tr><td><strong>Michigan</strong> &mdash; prevalence about 10%. Of 1000 tested: 95 true positives against 45 false positives &rarr; <strong>positive predictive value about 68%</strong></td></tr>
    <tr><td><strong>Florida</strong> &mdash; prevalence about 0.1%. Of 1000 tested: about 1 true positive against 50 false positives &rarr; <strong>positive predictive value about 2%</strong></td></tr>
  </table>
  <p>Then she reversed it. A shark-bite detector, same 95% and 95%: in Florida a positive has a
  reasonable chance of being real; in Michigan, where shark bites are vanishingly rare, most positives
  are false. <strong>The tests are identical. The pre-test probability is what changed.</strong></p>
  <table>
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td>Pre-test probability</td><td>Likelihood of the condition <em>before</em> the result &mdash; from signs, symptoms, history, risk factors and how common it is in the population</td></tr>
    <tr><td>Post-test probability</td><td>Likelihood <em>after</em> the result &mdash; depends on sensitivity and specificity</td></tr>
    <tr><td>Prevalence</td><td>How <strong>commonly</strong> something occurs; existing cases, usually a percentage</td></tr>
    <tr><td>Incidence</td><td>How <strong>often</strong> something happens &mdash; not how commonly</td></tr>
  </table>
  <div class="pearl"><strong>The one sentence to carry out of this lecture:</strong> sensitivity and
  specificity belong to the <em>test</em>; predictive value belongs to the <em>population being
  tested</em>. The test stays the same &mdash; prevalence changes the meaning of the result. Which is
  also why knowing the pre-test probability helps you decide whether to order the test at all.</div>
  <button type="button" class="test-yourself-btn" style="--acc:#69406c" onclick="window.openTestYourself('Test yourself — Laboratory Diagnostics', TEST_YOURSELF.labdiagnostics)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>1. Principles of Laboratory Diagnostics sv.pptx</em>
  (Professor Lauren M. Reynolds, MSPA, PA-C, Course Director), Slides 1&ndash;53, and the PAJ 5600
  syllabus instructional objectives. Exam-format notes are quoted from the 2026-08-18 lecture
  recording. Figures are reproduced from the lecture slides and each is cited to its slide. Course
  references: Laposata, <em>Laboratory Medicine: Diagnosis of Disease in the Clinical Laboratory</em>,
  4th edition, chapters 1&ndash;2.</footer>
</section>

</main>'''

TEST_YOURSELF = '''  var TEST_YOURSELF = {
    labdiagnostics: [
      {q:"During which phase of diagnostic testing do MOST errors occur?",
       choices:["Pretest","Intratest","Posttest","Errors are spread evenly"],correct:0,
       explain:"The pretest phase. That is why preparation, labeling, transport and communication carry so much of the objective — the assay itself is rarely the weak link."},
      {q:"You order coagulation studies. Which tube must the specimen arrive in?",
       choices:["Lavender","Gray","Light blue","Gold"],correct:2,
       explain:"Light blue, containing sodium citrate. Lavender is the complete blood count tube. Professor Reynolds' own test of whether you know this: if someone walks in with a lavender tube for your coags, you should catch it immediately."},
      {q:"A patient will collect a stool specimen at home for ova and parasites. What must you tell them?",
       choices:["Refrigerate it right away","Do NOT refrigerate it","Freeze it if delayed","Add the preservative provided"],correct:1,
       explain:"Do not refrigerate — warm stool is best for detecting ova and parasites. Patients refrigerate by instinct, so say it explicitly. Three separate random specimens are recommended because of the parasite life cycle."},
      {q:"Which is TRUE of a highly sensitive test with a negative result?",
       choices:["It rules the disease IN","It rules the disease OUT","It confirms the diagnosis","It tells you nothing without prevalence"],correct:1,
       explain:"SnNout — high Sensitivity plus a Negative result rules out. That is why sensitive tests screen. SpPin is the mirror: high Specificity plus a Positive rules in, which is why specific tests confirm."},
      {q:"The same test, 95% sensitivity and 95% specificity, is used where the disease is rare. What happens to the positive predictive value?",
       choices:["It rises, because specificity is high","It is unchanged, because the test is unchanged","It falls, because most positives will be false","It cannot be assessed without recalculating sensitivity"],correct:2,
       explain:"It falls. Sensitivity and specificity belong to the test; predictive value belongs to the population. In the frostbite example the same test gives about 68% in Michigan and about 2% in Florida."},
      {q:"A screening colonoscopy finds a lesion, which is biopsied. What does this illustrate?",
       choices:["A diagnostic test being downgraded to screening","A screening test becoming diagnostic","That the two terms are interchangeable","That screening should have been skipped"],correct:1,
       explain:"Screening may become diagnostic if an abnormality is found during testing. Screening and diagnostic are roles rather than fixed labels — the same procedure changed role mid-way."},
      {q:"How does state laboratory regulation relate to the federal Clinical Laboratory Improvement Amendments?",
       choices:["States may relax the federal standard","States may only match it exactly","State rules always end up stricter","Federal rules apply only where no state rule exists"],correct:2,
       explain:"The federal standard is a MINIMUM and cannot be downgraded, so state and city regulation is always stricter, never looser. Sites must also reapply every two years, with a licence matching the complexity performed."}
    ],'''

donor = open(DONOR, encoding="utf-8").read()
head = donor[:donor.index('<div class="layout wrap"')]
tail = donor[donor.index("</main>") + len("</main>"):]
ty_start = tail.index("var TEST_YOURSELF = {")
ty_end = tail.index("\n  };", ty_start)
tail = tail[:ty_start] + TEST_YOURSELF.lstrip() + tail[ty_end:]

# Plum retheme, each hex chosen to sit near the donor's own contrast ratio.
for old, new in (("#8a3f5c", "#69406c"), ("#b8842f", "#b8862f"), ("#5c4a7d", "#5f3a63"),
                 ("#5e2a41", "#452a48"), ("#ac5c78", "#8f5f92"),
                 ("#231d22", "#221c22"), ("#e0a8bd", "#d3b0d6")):
    head = head.replace(old, new)

# The donor PD1 guide predates the professor-emphasis convention, so its CSS
# has to come across explicitly. Lifted verbatim from build_pharm_guide.py
# rather than re-typed, so the convention stays identical across guides.
FIGCSS = """
  figure.fig .tag{display:block;margin-top:5px;font-style:normal;}
""" + """  .prof-flag{border:2px solid #d4a017;border-radius:10px;padding:16px 14px 6px;
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
</style>"""
head = head.replace("</style>", FIGCSS.replace("</style>", "") + "</style>", 1)
head = re.sub(r"<title>.*?</title>",
              "<title>Principles of Diagnostic Medicine I &middot; Exam 1 &mdash; Study Guide</title>",
              head, count=1, flags=re.S)
head = re.sub(r"<header class=\"top\">.*?</header>",
  '<header class="top">\n'
  '  <h1>Principles of Diagnostic Medicine I &middot; Exam 1 &mdash; Study Guide</h1>\n'
  '  <p>PAJ 5600 Principles of Diagnostic Medicine I &middot; Class of 2028</p>\n'
  '  <p>Covers Lecture 1 &middot; Exam 1 spans Lectures 1&ndash;6 and Lab 1, and sections are added as '
  'each deck is posted &middot; Instructional Objectives (IOs) taken verbatim from the syllabus</p>\n'
  '</header>', head, count=1, flags=re.S)

html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + BODY + tail
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
print("figures:", html.count('<figure class="fig">'),
      "| prof-flags:", html.count('class="prof-flag"'),
      "| donor palette left:", [c for c in ("#8a3f5c","#b8842f","#5c4a7d","#5e2a41","#ac5c78","#e0a8bd") if c in html])
