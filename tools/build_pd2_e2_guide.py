#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Physical Diagnosis 2, Exam 2 study guide.

Exam 2 is Friday 20 November 2026 and covers Lectures 5-7 (the calendar and the
syllabus appendix both say so). Only Lecture 5 has been delivered: Advanced
Cardiovascular & Peripheral Vascular System, Lauren Reynolds, 17 September.
Pulmonary (Lecture 6) and Hematology (Lecture 7) get their own sections when
those decks are posted -- the TOC and body carry <!--PD2E2L6--> style fences so
an add script can append without rewriting this one.

SKELETON: lifted from the PD2 Exam 1 guide, which already carries the site's
guide design system, the prof-flag CSS, the back bar and both footer links.
Only the head/tail are reused; the TOC, body and TEST_YOURSELF are this file's.
The donor's Word link is STRIPPED ([[word_export_feature]], failure mode 2:
a copied link advertises the donor's .docx and 404s). Run
tools/build_guide_docx.py once the page is carded on guides.html.

PALETTE: the Exam 2 quizzes already own one (#3a5a40 / #5f8a68 / #c08a2e); the
guide takes the same trio so the exam reads as one thing ([[guide_design_system]],
the Anatomy Exam 3 precedent). The donor's leftover pink tints (inherited from
PD1) are mapped to green ones.

OBJECTIVES are the syllabus's, verbatim ([[guide_verbatim_io_rule]]). The
syllabus prints the eighth objective as "f." a second time; it is rendered as
the eighth item of an <ol type="a">, so it shows as (h), and the guide says so.

EMPHASIS comes from BOTH transcripts of the three-part recording (faster-whisper
and Notability's own), read in full and diffed on every quoted line
([[lecture_transcript_cross_examine]]). Facts come from the slides; where the
recording and a slide disagree, the SLIDE wins and the disagreement is shown.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from extract_pd2_e2_figures import figure_html, DECK_NAME

DONOR = os.path.join(ROOT, "Physical Diagnosis 2 Exam 1", "pd2-exam-1-study-guide.html")
OUT = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2", "pd2-exam-2-study-guide.html")
IMGDIR = "pd2-exam-2-study-guide-images"
OSCE = "../Physical%20Diagnosis%202%20Exam%201/pd2-cardiac-osce.html"

TOC = '''<nav class="toc">
  <h2>Contents</h2>
<!--PD2E2TOC5-->
  <a class="top-link" href="#cardiovascular">1 &middot; Advanced Cardiovascular &amp; Peripheral Vascular Examination</a>
  <a href="#cv-signposting">How this lecture signposts</a>
  <a href="#cv-landmarks">1.1 Objective a &mdash; Anatomical landmarks</a>
  <a href="#cv-history">1.2 Objective b &mdash; The cardiac history</a>
  <a href="#cv-cycle">1.3 Objective c &mdash; The cardiac cycle, heart sounds &amp; gallops</a>
  <a href="#cv-impulse">1.4 Objectives d &amp; e &mdash; The apical impulse &amp; point of maximal impulse</a>
  <a href="#cv-areas">1.5 Objective f &mdash; The classic areas of auscultation</a>
  <a href="#cv-stethoscope">1.6 Objective g &mdash; Diaphragm versus bell</a>
  <a href="#cv-murmurs">1.7 Objective h &mdash; Thrills &amp; murmurs</a>
  <a href="#cv-murmur-table">1.8 Objective h &mdash; The murmurs one by one</a>
  <a href="#cv-maneuvers">1.9 Objective i &mdash; Maneuvers to evaluate murmurs</a>
  <a href="#cv-peripheral">1.10 Objective j &mdash; Arterial versus venous findings</a>
  <a href="#cv-edema">1.11 Objective k &mdash; Peripheral edema</a>
  <a href="#cv-complete">1.12 Objective l &mdash; The complete &amp; focused examination</a>
<!--/PD2E2TOC5-->
</nav>'''

BODY = '''<main>

<!--PD2E2L5-->
<section class="deck" id="cardiovascular">
  <h2 class="deck-title">1 &middot; Advanced Cardiovascular &amp; Peripheral Vascular Examination</h2>
  <p class="lecturer">Lecture 5 &middot; Lauren Reynolds, MSPA, PA-C &middot; 17 September 2026 &middot;
  115 slides &middot; recorded in three parts, 138 minutes</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Advanced Cardiac and Peripheral Vascular System Medical History and Examination</p>
    <ol type="a">
      <li>Review the anatomical landmarks of the cardiovascular system.</li>
      <li>Describe the elements related to interviewing and eliciting a medical history that aid in identifying cardiac disorders.</li>
      <li>Compare and contrast the cardiac cycle with reference to timing of heart sounds and gallops.</li>
      <li>Review the point of maximal impulse and apical impulse.</li>
      <li>Describe the character of the apical impulse with reference to anatomy and ventricular function.</li>
      <li>Review the classic areas of auscultation to assess cardiac sounds.</li>
      <li>Demonstrate the proper clinical skills when using the stethoscope diaphragm and bell with relation to specific heart sounds.</li>
      <li>Identify the physical characteristics of cardiac thrills and murmurs.</li>
      <li>Demonstrate the proper clinical skills for maneuvers to evaluate murmurs.</li>
      <li>Compare and contrast the physical examination findings related to abnormal peripheral arterial and venous function.</li>
      <li>Define the physical examination findings of peripheral edema.</li>
      <li>Demonstrate proper clinical skills for a complete and focused cardiovascular physical examination.</li>
    </ol>
    <p style="margin:8px 0 0;font-size:.82rem;color:var(--soft);">The syllabus letters the eighth
    objective &ldquo;f.&rdquo; a second time, a typing slip between (g) and (i). It is shown here, and
    referred to below, as (h).</p>
  </div>

  <h3 class="sub" id="cv-signposting">How this lecture signposts</h3>
  <div class="callout"><p><b>Nothing in 138 minutes was named as on, or off, the exam.</b> Both
  transcripts of the recording were read end to end, and neither holds a single &ldquo;this will be
  tested&rdquo; or &ldquo;you don&rsquo;t need this&rdquo;. That is a finding, not a failed search:
  treat the twelve objectives as evenly weighted, and use the two signals the lecture <em>does</em>
  give &mdash; what she repeated, and where the time went.</p>
  <p><b>What she repeated</b> is marked below with &#9733;. The most repeated idea of the whole lecture
  was a method rather than a fact: <b>describe the sound, never name the disease</b> (section 1.7).</p></div>
  <table>
    <tr><th>Block</th><th>Slides</th><th>Minutes of lecture</th></tr>
    <tr><td>The cardiac history</td><td>4&ndash;9</td><td>about 17 (the recording starts partway through slide 5)</td></tr>
    <tr><td>Blood flow and the cardiac cycle</td><td>10&ndash;17</td><td>about 11</td></tr>
    <tr><td>Apical impulse and ventricular impulses</td><td>18&ndash;24</td><td>about 8</td></tr>
    <tr><td>Examination preparation and the areas of auscultation</td><td>25&ndash;32</td><td>about 15</td></tr>
    <tr><td>Heart sounds, splitting and the extra sounds</td><td>33&ndash;44</td><td>about 20</td></tr>
    <tr><td>Describing and grading murmurs; thrills</td><td>45&ndash;57</td><td>about 13</td></tr>
    <tr><td>Maneuvers and hypertrophic obstructive cardiomyopathy</td><td>58&ndash;64</td><td>about 10</td></tr>
    <tr><td>The murmurs one by one</td><td>65&ndash;81</td><td>about 18</td></tr>
    <tr><td>The peripheral vascular examination</td><td>82&ndash;114</td><td>about 25</td></tr>
  </table>
  <p>The peripheral vascular block is a third of the slides but a fifth of the time, and she said why
  (part 3, 29:02): <em>&ldquo;You have done the peripheral vascular exam. You&rsquo;ve done it. Okay, so
  this is almost entirely review. <b>Whereas the cardiac stuff is a lot of new.</b>&rdquo;</em></p>

  <h3 class="sub" id="cv-landmarks">1.1 &middot; Objective a &mdash; Anatomical landmarks of the cardiovascular system</h3>
  <p><b>The path of blood</b> is the map every later section reads from:</p>
  <ol>
    <li>Deoxygenated blood from the body (inferior and superior vena cava) &rarr; <b>right atrium</b> &rarr;
    <b>tricuspid valve</b> &rarr; right ventricle</li>
    <li>Right ventricle &rarr; <b>pulmonic valve</b> &rarr; pulmonary artery &rarr; lungs</li>
    <li>Lungs &rarr; pulmonary vein &rarr; oxygenated blood to the <b>left atrium</b></li>
    <li>Left atrium &rarr; <b>mitral valve</b> &rarr; left ventricle &rarr; <b>aortic valve</b> &rarr;
    aorta &rarr; rest of the body</li>
  </ol>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>The tricuspid is the first valve blood crosses on its way back to the heart.</b> She gave it a
    mnemonic and then said the point twice (part 1, 17:18&ndash;17:42, identical in both transcripts):
    <em>&ldquo;flows through the tricuspid valve, because <b>you try before you buy</b> &hellip; that is the
    first valve that the blood crosses after it returns to the heart. <b>That is important, that is
    important.</b>&rdquo;</em> Try (tricuspid) comes before buy (bicuspid, the mitral). And the reason it
    matters: <em>&ldquo;if there&rsquo;s any sort of interruption or abnormality in it or an additional
    pathway that shouldn&rsquo;t be there, we will see changes in the way we would expect the blood flow to
    behave.&rdquo;</em> Every murmur in section 1.8 is read off this pathway.</p>
  </div>
  <p><b>Surface landmarks.</b> The <b>angle of Louis</b> (the sternal-manubrial junction) lies beside the
  second rib, which puts the second intercostal space directly below it; count down from there. The
  <b>point of maximal impulse</b> is normally in the <b>fifth intercostal space at or just medial to the
  left midclavicular line</b> (section 1.4). The listening areas sit at named rib spaces beside the sternum
  and at the apex (section 1.5).</p>
  [[GRID:apical-impulse-anatomy,surface-anatomy]]
  <p><b>The peripheral arteries</b> you will palpate and auscultate are the branches of that same tree:
  carotid, brachial, radial, ulnar, the abdominal aorta with its renal and iliac branches, femoral,
  popliteal, dorsalis pedis and posterior tibial.</p>
  [[FIG:arterial-tree]]

  <h3 class="sub" id="cv-history">1.2 &middot; Objective b &mdash; The cardiac history</h3>
  <p>The symptoms to ask about: <b>chest pain, palpitations, shortness of breath (dyspnea, orthopnea,
  paroxysmal nocturnal dyspnea), swelling (edema) and fainting (syncope)</b>. Across all of them, it is
  important to <b>quantify the patient&rsquo;s baseline level of activity</b> &mdash; ask specific questions
  about their day-to-day life.</p>

  <h4 class="subsub">Chest pain</h4>
  <ul>
    <li>The <b>most common symptom of coronary artery disease</b>.</li>
    <li>Always consider <b>angina pectoris, myocardial infarction, dissecting aortic aneurysm and pulmonary
    embolism</b>.</li>
    <li>Distinguish cardiovascular causes from disorders of the pericardium, trachea, bronchi, parietal
    pleura, esophagus, chest wall, gallbladder, stomach and neck &mdash; <em>&ldquo;anything that&rsquo;s in
    there can cause pain &hellip; but the big bad that we worry about first, cardiac.&rdquo;</em></li>
    <li>Men and women with acute coronary syndrome present with the classic symptoms of <b>exertional
    angina</b>.</li>
    <li><b>Women over 65</b> are likely to report <b>atypical symptoms</b>: upper back, neck or jaw pain,
    shortness of breath, paroxysmal nocturnal dyspnea, nausea, vomiting, fatigue. In the lecture: keep a
    high index of suspicion, because <em>&ldquo;sometimes it&rsquo;s just truly fatigue.&rdquo;</em></li>
    <li>Technique: <b>begin with open-ended questions, then ask for details</b>, and <b>ask the patient to
    point to the pain</b>. Then the same questions as for any pain &mdash; where, radiation, severity out
    of ten, constant or intermittent, character.</li>
  </ul>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Said in lecture &mdash; not on a slide</span>
    <p><b>How the patient points is itself a finding.</b> She demonstrated the gesture rather than describing
    it: <b>Levine&rsquo;s sign</b>, the clenched fist held against the center of the chest (part 1, 2:20&ndash;3:14, both transcripts): <em>&ldquo;if you say, can you
    show me where the pain is and the person goes like this &mdash; <b>alarm bells</b> &hellip; this is the
    real deal.&rdquo;</em> A vague burning line up the middle points her toward the esophagus, a single
    fingertip toward a rib or muscle &mdash; <em>&ldquo;it could still be cardiac. Like we don&rsquo;t ever
    go, ah, it&rsquo;s fine.&rdquo;</em> This sign is not on any slide, so it is here as the lecturer&rsquo;s
    teaching, not as deck content. (Not to be confused with the <b>Levine grading system</b> for murmurs,
    which is on slide 56.)</p>
  </div>

  <h4 class="subsub">Palpitations</h4>
  <p>An <b>unpleasant awareness of the heartbeat</b>, described as &ldquo;skipping&rdquo;,
  &ldquo;racing&rdquo;, &ldquo;fluttering&rdquo;, &ldquo;pounding&rdquo; or &ldquo;stopping of the
  heart&rdquo;. It may be irregular, may speed up or slow down rapidly, or may arise from increased
  forcefulness of contraction. <b>Anxious and hyperthyroid patients</b> may report palpitations, and they
  <b>do not necessarily mean heart disease</b>. Reword your questions if needed: <em>Are you aware of your
  heartbeat? What does it feel like? Fast? Slow? Regular? Irregular? How long does it last?</em> Then
  <b>get an electrocardiogram</b>.</p>

  <h4 class="subsub">Shortness of breath</h4>
  <table>
    <tr><th>Term</th><th>Definition</th><th>How to pin it down</th></tr>
    <tr><td><b>Dyspnea</b></td><td>Uncomfortable awareness of breathing that is <b>inappropriate to a given
    level of exertion</b>. Common in both cardiac and pulmonary problems.</td><td>Relate it to what the
    patient can still do day to day.</td></tr>
    <tr><td><b>Orthopnea</b></td><td>Dyspnea that occurs when the patient is <b>supine</b> and <b>improves
    when the patient sits up</b>.</td><td>Quantify by the <b>number of pillows</b> used for sleeping, or the
    need to sleep sitting up &mdash; and <b>ask what the pillows are for</b>.</td></tr>
    <tr><td><b>Paroxysmal nocturnal dyspnea</b></td><td>Episodes of sudden dyspnea and orthopnea that
    <b>awaken the patient from sleep</b>.</td><td>Usually <b>1&ndash;2 hours after going to bed</b>,
    prompting the patient to sit up, stand up or go to the window for air. May be associated with wheezing
    and coughing.</td></tr>
  </table>
  <p>Orthopnea is not only cardiac: she pointed out it can be pulmonary or even abdominal, and described
  it in her own late pregnancy.</p>

  <h4 class="subsub">Edema</h4>
  <p>The <b>accumulation of excessive fluid in the extravascular interstitial space</b>. <b>Up to 10% of body
  weight can accumulate before pitting edema appears.</b> Focus questions on <b>location, timing, setting
  and associated symptoms</b>: <em>Swelling anywhere? Where else? Worse in the morning or evening? Do your
  shoes get tight? Rings tight on your fingers? Eyelids puffy in the morning? Clothes tight in the
  middle?</em> And consider recommending a <b>daily morning weight</b>.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; &ldquo;tuck that away&rdquo;</span>
    <p><b>Weight shows edema before the eye does.</b> Her example (part 1, 8:28): 135 pounds one morning,
    137 the next &mdash; <em>&ldquo;Do you think that I gained two pounds of muscle or two pounds of &hellip;
    fat tissue in that 24 hour period?&rdquo;</em> It is water. <em>&ldquo;So weight can be a better indicator
    of edema before we even notice like, hey, I&rsquo;m kind of puffy or even have pitting edema &hellip;
    <b>tuck that away</b>.&rdquo;</em></p>
    <p>A student raised <b>dry weight</b> and she endorsed it, <em>&ldquo;Dry weight, tuck that away
    too&rdquo;</em>: dialysis and heart failure patients should know their weight at fluid balance, so a
    rise from it can be caught. Both transcripts carry both &ldquo;tuck that away&rdquo; lines.</p>
  </div>

  <h4 class="subsub">Fainting (syncope)</h4>
  <p>A <b>transient loss of consciousness followed by recovery</b>. The <b>most common cause is
  neurocardiogenic (vasovagal)</b>; syncope is of <b>cardiac origin from arrhythmias in about 20%</b> of
  cases. Ask: <em>Feel faint? About to fall or pass out? Unsteady and off balance?</em></p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; the before and the after</span>
    <p><em>&ldquo;Sometimes the before and after are more valuable than the fainting spell itself&rdquo;</em>
    (part 1, 10:48). What she taught the history to separate:</p>
    <table>
      <tr><th>The story</th><th>Points toward</th></tr>
      <tr><td>Lightheaded, pale, clammy first &mdash; a warning prodrome, often with a trigger (hers was
      watching a classmate fish for a vein)</td><td>Vasovagal</td></tr>
      <tr><td>Stood up from a crouch, tunnel vision, then down</td><td>Orthostatic</td></tr>
      <tr><td><b>Sudden, no warning</b> &mdash; <em>&ldquo;they&rsquo;re here and then they&rsquo;re
      not&rdquo;</em></td><td><b>Arrhythmia</b> &mdash; <em>&ldquo;please run and get the AED [automated external defibrillator] and then also
      call 911&rdquo;</em></td></tr>
      <tr><td>Comes round agitated and confused</td><td>A postictal phase &mdash; think seizure</td></tr>
    </table>
    <p>And patient education worth giving (and following): <em>&ldquo;If you feel faint, I don&rsquo;t care
    where you are, <b>please sit down</b>.&rdquo;</em></p>
  </div>

  <h3 class="sub" id="cv-cycle">1.3 &middot; Objective c &mdash; The cardiac cycle, heart sounds and gallops</h3>
  <p>The <b>cardiac cycle</b> is the period between the start of one heartbeat and the beginning of the next:
  alternating contraction and relaxation, divided into <b>systole</b> and <b>diastole</b>. Both are named for
  what the <b>ventricles</b> are doing.</p>
  <table>
    <tr><th></th><th>Systole &mdash; ventricular contraction</th><th>Diastole &mdash; ventricular relaxation and filling</th></tr>
    <tr><td>Pressure</td><td>Ventricular pressure <b>exceeds atrial</b> pressure</td><td>Ventricular pressure <b>falls below atrial</b> pressure</td></tr>
    <tr><td>Closes</td><td><b>Mitral and tricuspid</b> (the atrioventricular valves), helped by the papillary muscles</td><td><b>Aortic and pulmonic</b></td></tr>
    <tr><td>Open</td><td>Aortic and pulmonic &mdash; right ventricle ejects into the pulmonary artery, left into the aorta</td><td>Mitral and tricuspid &mdash; atria empty into the ventricles</td></tr>
    <tr><td>The sound of that closure</td><td><b>S1</b></td><td><b>S2</b></td></tr>
  </table>
  [[GRID:lub-dub,cardiac-cycle]]
  <table>
    <tr><th></th><th>S1 &ldquo;lub&rdquo;</th><th>S2 &ldquo;dub&rdquo;</th></tr>
    <tr><td>Closure of</td><td>Mitral and tricuspid valves</td><td>Aortic and pulmonic valves</td></tr>
    <tr><td>Best heard</td><td>With the <b>diaphragm</b>, at the <b>apex</b></td><td>With the <b>diaphragm</b>, at the <b>base</b></td></tr>
    <tr><td>Splitting</td><td>Usually not present</td><td>Can be heard, at Erb&rsquo;s point and the pulmonic area; normal physiologic splitting is best heard at the <b>pulmonic area</b></td></tr>
    <tr><td>Against the carotid pulse</td><td><b>Precedes</b> it</td><td><b>Follows</b> it</td></tr>
  </table>

  <h4 class="subsub">Splitting of S2</h4>
  <p>S2 has two components: <b>aortic (A2)</b>, usually <b>louder</b> because of the high pressure in the
  aorta, and <b>pulmonic (P2)</b>. They are normally <b>fused as one sound during expiration</b> and
  <b>audibly separated during inspiration</b> &mdash; that is <b>physiologic splitting of S2</b>, and it is
  normal. <b>Audible splitting during expiration is pathologic and suggests heart disease.</b></p>
  [[GRID:split-physiologic,split-pathologic]]
  <p>How she explained it (part 2, 20:16&ndash;21:52): on full inspiration there is more back pressure
  against the pulmonic valve, so P2 comes a little later; on full expiration the two sounds land together.
  <em>&ldquo;Spoiler alert. There&rsquo;s always two sounds. It&rsquo;s just whether they&rsquo;re occurring
  over top of each other or not.&rdquo;</em> A pathologic split tends to be <b>fixed</b> &mdash; no
  respiratory variation. Slide 36 plays both (split and unsplit S2) as embedded sound files; listen to them
  with headphones, as she suggested.</p>

  <h4 class="subsub">Extra sounds in systole</h4>
  <table>
    <tr><th>Sound</th><th>When</th><th>Character and where</th><th>Associations</th></tr>
    <tr><td><b>Early ejection sound</b></td><td>Shortly after S1</td><td>Sudden pathologic halting of the aortic
    and pulmonic valves as they open. <b>High pitched, sharp clicking; diaphragm.</b> Indicates cardiovascular
    disease.</td><td><b>Aortic:</b> heard at base and apex; <b>does not vary</b> with inspiration; dilated aorta,
    aortic valve disease from congenital stenosis or bicuspid valve. <b>Pulmonic:</b> best in the <b>2nd and 3rd
    intercostal spaces</b>; <b>decreases with inspiration</b>; dilated pulmonary artery, pulmonary hypertension,
    pulmonic stenosis.</td></tr>
    <tr><td><b>Click</b></td><td><b>Mid to late systole</b></td><td>Usually single, may be several; at or medial
    to the apex and lower left sternal border. <b>High pitched; diaphragm.</b></td><td>Usually <b>mitral valve
    prolapse</b> (systolic ballooning of part of the mitral valve into the left atrium). Followed by a
    <b>late systolic murmur</b> of mitral regurgitation crescendoing up to S2.</td></tr>
  </table>
  [[GRID:early-ejection-sound,systolic-click]]

  <h4 class="subsub">Extra sounds in diastole &mdash; the gallops and the snap</h4>
  <table>
    <tr><th></th><th>S3 &mdash; ventricular gallop</th><th>S4 &mdash; atrial gallop</th><th>Opening snap</th></tr>
    <tr><td>Timing</td><td><b>After S2</b>, early in diastole</td><td><b>Just before S1</b></td><td><b>Very early</b> diastole</td></tr>
    <tr><td>Rhythm</td><td><b>Ken-TUC-ky</b> (lub-dub-dee): S1 S2 S3</td><td><b>Ten-nes-SEE</b> (dee-lub-dub): S4 S1 S2</td><td>A snap right after S2</td></tr>
    <tr><td>Listen</td><td><b>Bell</b>, apex, <b>left lateral decubitus</b></td><td>Dull, low pitched: <b>bell</b>, apex, left lateral decubitus (left sided); lower left sternal border for the right-sided one</td><td>High pitch: <b>diaphragm</b>. Just medial to the apex and along the lower left sternal border</td></tr>
    <tr><td>Normal in</td><td>Children and young adults (up to 35&ndash;40), last trimester of pregnancy</td><td>Trained athletes and older age groups</td><td>Never</td></tr>
    <tr><td>Pathologic</td><td>In adults <b>over 40</b>. High left ventricular filling pressures and abrupt deceleration of inflow across the mitral valve at the end of rapid filling (&ldquo;blood slapping against the left ventricular wall&rdquo;). Causes: decreased contractility, <b>heart failure</b>, volume overload from aortic or mitral regurgitation, left to right shunts</td><td>Stiff ventricle: hypertrophy or fibrosis, decreased compliance during filling after atrial contraction. Causes: <b>hypertensive heart disease, aortic stenosis</b>, ischemic and hypertrophic cardiomyopathy, delayed atrioventricular conduction</td><td>Abrupt deceleration as a <b>stenotic mitral valve</b> opens. Becomes less audible as the leaflets calcify</td></tr>
  </table>
  <p>Two details from the slides that are easy to lose. The <b>right-sided S4</b> belongs with pulmonary
  hypertension and pulmonic stenosis and gets <b>louder with inspiration</b>; slide 42 labels the lower left
  sternal border S4 &ldquo;left ventricular S4 (right sided)&rdquo;, and its own parenthesis and causes make
  it the right-sided one. And an opening snap loud enough to radiate to the pulmonic area <b>can be mistaken
  for P2</b>; its high pitch and obvious snap are what separate it.</p>
  [[GRID:s3,s4,opening-snap]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; how to keep the sounds straight</span>
    <p>Asked in effect &ldquo;how do I memorize all this?&rdquo;, her answer (part 2, 23:51) was not a list:
    <em>&ldquo;think about <b>what you&rsquo;re hearing and when</b> and purely break it down to that to
    start.&rdquo;</em> Place the sound in the cycle, then ask <b>which valves are open and which are shut at
    that moment</b>. A sound right after S1, when the aortic and pulmonic valves are opening, belongs to them;
    a click in mid-systole, when the mitral and tricuspid should be shut, suggests one of those opening when it
    should not; a snap early in diastole, when the mitral should be opening, suggests a stiff mitral valve
    opening late.</p>
  </div>

  <h3 class="sub" id="cv-impulse">1.4 &middot; Objectives d &amp; e &mdash; The apical impulse and point of maximal impulse</h3>
  <p><b>The apical impulse</b> is the brief early impulse of the left ventricular apex against the chest wall
  during contraction. Identified by palpating the precordium, it is recorded as the <b>point of maximal
  impulse</b>. The exception: in certain pathologic conditions &mdash; right ventricular hypertrophy, a
  dilated pulmonary artery, aortic aneurysm, left ventricular hypertrophy, chronic obstructive pulmonary
  disease &mdash; another pulsation can be more prominent than the apex beat.</p>
  <ul>
    <li>The point of maximal impulse <b>identifies the left border of the heart</b>.</li>
    <li>Normally in the <b>fifth intercostal space at or just medial to the left midclavicular line</b>.</li>
    <li>When a disorder changes the heart&rsquo;s size or shape (cardiomegaly, hypertrophy) the left border
    shifts <b>lateral and possibly inferior</b> &mdash; for example the sixth intercostal space at the anterior
    axillary line.</li>
    <li>Supine, its diameter can be the size of a <b>quarter (about 2.5 cm)</b>; it is usually palpated as
    <b>brisk and tapping</b>.</li>
    <li>Cannot find it supine? Roll the patient to the <b>left lateral decubitus</b> position. Still nothing?
    Ask them to <b>exhale fully and hold</b> for a few seconds.</li>
    <li>Technique from the lecture: start with four fingers, lift them one at a time until one finger sits on
    the most intense point.</li>
  </ul>
  <div class="pearl"><b>Document where you find it.</b> The slide says so in capitals, and she explained why
  (part 1, 29:05&ndash;30:43): a displaced impulse moves your thinking toward an enlarged heart, a shift from
  fluid in the pleural space, or &mdash; with muffled heart sounds and a rub &mdash; a pericardial effusion.
  <em>&ldquo;Knowing where you&rsquo;re supposed to find it and then documenting where you actually find it is
  valuable.&rdquo;</em></div>

  <h4 class="subsub">Describing the impulse &mdash; three words, and what each means</h4>
  <table>
    <tr><th>Term</th><th>Meaning</th></tr>
    <tr><td><b>Hyperkinetic</b></td><td>From transiently <b>increased stroke volume</b>. Does not necessarily
    indicate heart disease.</td></tr>
    <tr><td><b>Sustained</b></td><td>Ventricular <b>hypertrophy</b> from chronic <b>pressure load</b> &mdash;
    increased <b>afterload</b>.</td></tr>
    <tr><td><b>Diffuse</b></td><td>Ventricular <b>dilation</b> from chronic <b>volume overload</b> &mdash;
    increased <b>preload</b>.</td></tr>
  </table>
  <h4 class="subsub">The left ventricular impulse</h4>
  <table>
    <tr><th></th><th>Hyperkinetic</th><th>Pressure overload</th><th>Volume overload</th></tr>
    <tr><td>Location</td><td>Normal</td><td>Normal</td><td><b>Displaced to the left and possibly downward</b></td></tr>
    <tr><td>Diameter</td><td>About 2 cm, though increased amplitude may make it feel larger</td><td>Over 2 cm</td><td>Over 2 cm</td></tr>
    <tr><td>Amplitude</td><td>More forceful tapping</td><td>More forceful tapping</td><td>Diffuse</td></tr>
    <tr><td>Duration</td><td>Under two thirds of systole</td><td><b>Sustained</b></td><td>Often slightly sustained</td></tr>
    <tr><td>Examples</td><td>Anxiety, hyperthyroidism, severe anemia</td><td><b>Aortic stenosis, hypertension</b></td><td><b>Aortic or mitral regurgitation, cardiomyopathy</b></td></tr>
  </table>
  <h4 class="subsub">The right ventricular impulse</h4>
  <table>
    <tr><th></th><th>Hyperkinetic</th><th>Pressure overload</th><th>Volume overload</th></tr>
    <tr><td>Location</td><td>3rd, 4th, 5th left intercostal spaces</td><td>3rd, 4th, 5th left intercostal spaces, possibly subxiphoid</td><td>Left sternal border toward the left cardiac border, also subxiphoid</td></tr>
    <tr><td>Diameter</td><td colspan="3">Not useful</td></tr>
    <tr><td>Amplitude</td><td>Slightly more forceful</td><td>More forceful tapping</td><td>Slightly to markedly more forceful</td></tr>
    <tr><td>Duration</td><td>Normal</td><td>Sustained</td><td>Normal to slightly sustained</td></tr>
    <tr><td>Examples</td><td>Anxiety, hyperthyroidism, severe anemia</td><td><b>Pulmonic stenosis, pulmonary hypertension</b></td><td><b>Atrial septal defect</b></td></tr>
  </table>
  <p>Read the two tables together and the pattern is the same on both sides: <b>pressure</b> load
  thickens the wall and <b>sustains</b> the impulse; <b>volume</b> load dilates the chamber and makes it
  <b>diffuse</b> and displaced. She was candid that the right ventricular impulse is much harder to
  distinguish than the left, and that the impulse is never read alone &mdash; <em>&ldquo;in the same way that
  you wouldn&rsquo;t ever just use a Weber by itself&rdquo;</em> (part 2, 3:03): a larger, sustained impulse
  plus a systolic ejection murmur at the aortic area puts her money on aortic stenosis.</p>

  <h3 class="sub" id="cv-areas">1.5 &middot; Objective f &mdash; The classic areas of auscultation</h3>
  <table>
    <tr><th>Area</th><th>Where</th><th>What is loudest there</th></tr>
    <tr><td><b>Aortic</b></td><td>Right second intercostal space, at the sternal border</td><td>Aortic valve sounds; aortic stenosis; early aortic ejection sound (with the apex)</td></tr>
    <tr><td><b>Pulmonic</b></td><td>Left second intercostal space, at the sternal border</td><td>Physiologic splitting of S2; pulmonic ejection sound (2nd&ndash;3rd spaces); pulmonic stenosis and regurgitation</td></tr>
    <tr><td><b>Erb&rsquo;s point</b></td><td>Left third intercostal space, between the pulmonic and mitral areas</td><td>S2 splitting; hypertrophic cardiomyopathy murmur; pericardial friction rub most often</td></tr>
    <tr><td><b>Tricuspid</b></td><td>Lower left sternal border</td><td>Tricuspid regurgitation and stenosis; hypertrophic cardiomyopathy murmur</td></tr>
    <tr><td><b>Mitral</b></td><td>Apex &mdash; fifth intercostal space, left midclavicular line</td><td>S1; S3 and S4; mitral regurgitation and stenosis</td></tr>
  </table>
  [[FIG:auscultation-areas]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; why the areas are where they are</span>
    <p>The listening areas are <b>not over the valves</b>. Each is the <b>next place downstream, in the direction
    of blood flow, where there is no bone in the way</b> (part 2, 12:18&ndash;18:40): <em>&ldquo;think about the
    direction that blood is flowing because sound is gonna travel that same direction &hellip; It&rsquo;s not
    magic &hellip; that&rsquo;s the first place where there&rsquo;s not a bone block.&rdquo;</em> The same logic
    explains radiation: an aortic stenosis murmur loud enough can be heard <b>in both carotids</b>, because that
    is where the blood goes next &mdash; so check the aortic area before calling it bilateral carotid
    bruits.</p>
  </div>

  <h3 class="sub" id="cv-stethoscope">1.6 &middot; Objective g &mdash; Using the diaphragm and the bell</h3>
  <table>
    <tr><th></th><th>Bell</th><th>Diaphragm</th></tr>
    <tr><td>Picks up</td><td><b>Low-pitched</b> sounds</td><td><b>High-pitched</b> sounds</td></tr>
    <tr><td>How to apply</td><td><b>Lightly</b> &mdash; but with no gaps</td><td><b>Press firmly</b></td></tr>
    <tr><td>Where</td><td>At the <b>apex</b>, then medially along the lower sternal border</td><td>Throughout the precordium</td></tr>
    <tr><td>Heart sounds</td><td><b>S3, S4</b></td><td><b>S1, S2</b>, early ejection sounds, clicks, the <b>opening snap</b></td></tr>
    <tr><td>Murmurs and rubs</td><td><b>Mitral stenosis</b> (and the tricuspid stenosis rumble)</td><td><b>Aortic and mitral regurgitation</b>, <b>pericardial friction rubs</b></td></tr>
  </table>
  <p>Technique: a <b>quiet setting</b>; listen for transitory and subtle sounds; isolate each sound and listen
  to each in turn; <b>close your eyes</b> to focus; and the stethoscope <b>must have direct contact with the
  skin</b>. In the lecture: if you hear something abnormal, stay there and listen longer; if chest hair
  rustles under the diaphragm, hold still or part it.</p>
  <div class="pearl"><b>Opening snap versus S3</b> is the pair the diaphragm-and-bell objective is really
  about. Both sit early in diastole. The snap is <b>high pitched &mdash; diaphragm</b>; S3 is <b>low &mdash;
  bell</b>. Which end of the stethoscope brings it out is part of the answer.</div>

  <h3 class="sub" id="cv-murmurs">1.7 &middot; Objective h &mdash; The physical characteristics of thrills and murmurs</h3>
  <p><b>A murmur</b> is the sound of <b>turbulent blood flow over a heart valve</b> &mdash; a
  &ldquo;swoosh&rdquo;. It results from:</p>
  <ul>
    <li>Flow across a <b>partially obstructed</b> valve</li>
    <li>Increased flow through a <b>normal valve</b> of a child</li>
    <li>Ejection into a <b>dilated chamber</b></li>
    <li><b>Regurgitant</b> flow across an incompetent valve</li>
    <li><b>Abnormal shunting</b> of blood from one chamber to a lower pressure chamber</li>
  </ul>
  <p><b>A thrill</b> is the vibration or buzzing sensation a murmur produces, felt with the <b>balls of the
  hand</b> pressed against the chest wall, held still &mdash; most easily in the position that accentuates the
  murmur. A murmur is heard; a thrill is felt. And the vessel equivalent of a murmur is a <b>bruit</b>:
  <em>&ldquo;a murmur is to a heart valve as a bruit is to a vessel&rdquo;</em>.</p>
  <div class="pearl"><b>Where to feel a real thrill:</b> she recommended palpating a dialysis patient&rsquo;s
  <b>arteriovenous fistula</b> (part 2, 51:21&ndash;52:11, both transcripts) &mdash; <em>&ldquo;that is a
  thrill, that is what a thrill feels like&rdquo;</em> &mdash; and if the rumble is absent, tell the nurse,
  because the fistula may be occluded.</div>

  <h4 class="subsub">The seven characteristics</h4>
  <p><b>Timing, shape, location, radiation, intensity, pitch, quality.</b> The working checklist from the
  slide: Systole or diastole? How long? Any special tests? Where loudest &mdash; base, apex, sternal border
  &mdash; and does it radiate? Crescendo or decrescendo? What grade? Any extra heart sounds?</p>
  <p><b>Timing.</b> Systolic falls <b>between S1 and S2</b>; diastolic <b>between S2 and S1</b>. If you
  cannot tell, <b>palpate the carotid as you listen</b>: a systolic murmur coincides with the carotid
  upstroke.</p>
  [[GRID:timing-midsystolic,timing-pansystolic,timing-late-systolic]]
  [[GRID:timing-early-diastolic,timing-mid-diastolic,timing-late-diastolic,timing-continuous]]
  <p><b>Shape</b> is intensity over time. <b>Crescendo-decrescendo</b>: diamond shaped, rises then falls.
  <b>Decrescendo</b>: begins at maximum and grows silent. <b>Plateau</b>: unchanging. (Crescendo alone grows
  louder.)</p>
  [[GRID:shape-crescendo-decrescendo,shape-decrescendo,shape-crescendo,shape-plateau]]
  <p><b>Location</b> is where the murmur originates, found by exploring where it is <b>loudest</b>; describe it
  by intercostal space and distance from the sternum, apex, midclavicular, midsternal or axillary lines.
  <b>Radiation</b> is where else it is heard, and it tells you about the site of origin, intensity, the
  direction of flow and bone conduction in the thorax.</p>
  <p><b>Intensity</b> is graded on a <b>six-point scale</b> (the Levine grading system) and written as a
  fraction, for example 3/6.</p>
  <table>
    <tr><th>Grade</th><th>Description</th></tr>
    <tr><td>1</td><td>Very faint, heard only after the listener has &ldquo;tuned in&rdquo;; may not be heard in all positions</td></tr>
    <tr><td>2</td><td>Quiet, but heard <b>immediately</b> after placing the stethoscope on the chest</td></tr>
    <tr><td>3</td><td>Moderately loud</td></tr>
    <tr><td><b>4</b></td><td>Loud, <b>with palpable thrill</b></td></tr>
    <tr><td>5</td><td>Very loud, with thrill; may be heard with the stethoscope <b>partly off</b> the chest</td></tr>
    <tr><td>6</td><td>Very loud, with thrill; may be heard with the stethoscope <b>entirely off</b> the chest</td></tr>
  </table>
  [[FIG:levine-grades]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; the thrill is the jump</span>
    <p><em>&ldquo;How loud it is increases the grade. <b>But when we also feel a thrill, we jump up</b> &hellip;
    I&rsquo;m palpating across the precordium and I can also palpate a thrill, we&rsquo;re at a four&rdquo;</em>
    (part 2, 49:03). Grading is a joint judgment of the ear and the hand. Most murmurs she meets in practice
    are 2s and 3s, with 4s when a thrill is present.</p>
  </div>
  <p><b>Pitch</b>: high, medium or low. <b>Quality</b>: blowing, harsh, rumbling or musical.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; the most repeated idea in the lecture</span>
    <p><b>The sound is not the diagnosis. Document what you hear, where and when; name the disease later, in
    the assessment.</b> She made this point at least three times (part 2, 23:51&ndash;25:27 and
    42:09&ndash;42:56; part 3, 27:32), and both transcripts carry it:</p>
    <p><em>&ldquo;Murmurs are findings that tell us something and it&rsquo;s our job to hunt down what that
    something is &hellip; the sound is not the diagnosis.&rdquo;</em> &mdash; <em>&ldquo;You&rsquo;re not gonna
    say, I hear an aortic stenosis murmur at the right second intercostal space. That&rsquo;s not how you are
    gonna document that. You&rsquo;re gonna say, I hear a systolic ejection murmur, crescendo decrescendo, with
    whatever intensity, radiating to the carotids.&rdquo;</em></p>
    <p>Her own worked example of a physical examination line: <b>&ldquo;a grade four out of six systolic
    murmur, loudest at the right second intercostal space, radiates throughout the precordium, with greater
    intensity to the carotids&rdquo;</b> &mdash; plus the thrill and where it was felt. And for mitral
    stenosis: <b>&ldquo;a diastolic opening snap followed by a decrescendo murmur, best heard at the left fifth
    midclavicular line&rdquo;</b>, with &ldquo;suspect mitral stenosis&rdquo; appearing only in the
    differential, and an echocardiogram to decide it.</p>
  </div>

  <h4 class="subsub">Innocent, physiologic, pathologic</h4>
  <table>
    <tr><th></th><th>Innocent</th><th>Physiologic</th><th>Pathologic</th></tr>
    <tr><td>What it is</td><td>No physiologic or structural abnormality, usually from increased flow</td><td>From physiologic changes in body metabolism</td><td>A structural abnormality of the heart or great vessels</td></tr>
    <tr><td>Features</td><td>Grade 1&ndash;3 of 6. <b>Diminishes</b> when the patient stands, sits up or does a Valsalva. Common in infancy and childhood, gone by adulthood</td><td>Examples: <b>anemia, pregnancy, fever, hyperthyroidism</b></td><td>Examples: <b>aortic stenosis, pulmonic stenosis, hypertrophic obstructive cardiomyopathy, atrial septal defect</b></td></tr>
  </table>
  <p>She refined the slide on one point (part 3, 10:34): innocent is defined by the <b>absence of symptoms
  and of any structural abnormality</b>, not by the grade &mdash; <em>&ldquo;It&rsquo;s not that, oh, the grade
  is only one to three, so therefore it&rsquo;s innocent.&rdquo;</em> A murmur with a thrill is not innocent
  and needs working up. And a murmur that appears in pregnancy is still worked up, even if it later proves
  physiologic.</p>
  <p><b>Children break the rules</b> (part 2, 39:45): more respiratory variation in heart rate, more
  pronounced physiologic splitting, and turbulent flow across normal valves. Unless stated otherwise, this
  lecture describes adults.</p>

  <h3 class="sub" id="cv-murmur-table">1.8 &middot; Objective h &mdash; The murmurs one by one</h3>
  <p>Each lesion follows from the pathway in section 1.1 and the open-and-shut valves in section 1.3. In
  systole the aortic and pulmonic valves should be open and the mitral and tricuspid shut: so a systolic
  murmur is either a <b>stenotic outflow valve</b> or a <b>leaking inflow valve</b>. In diastole the reverse:
  a <b>leaking outflow valve</b> or a <b>stenotic inflow valve</b>.</p>
  <h4 class="subsub">Systolic murmurs</h4>
  <table>
    <tr><th></th><th>Aortic stenosis</th><th>Pulmonic stenosis</th><th>Hypertrophic cardiomyopathy</th><th>Tricuspid regurgitation</th><th>Mitral regurgitation</th></tr>
    <tr><td>Timing</td><td>Midsystolic</td><td>Midsystolic</td><td>Midsystolic</td><td>Pansystolic (holosystolic)</td><td>Pansystolic (holosystolic)</td></tr>
    <tr><td>Intensity</td><td>Soft or loud; with a thrill at 4/6 or above</td><td>Soft to loud; if loud, with a thrill</td><td>Variable</td><td>Varies</td><td>Soft to loud; if loud, with an <b>apical thrill</b></td></tr>
    <tr><td>Pitch</td><td>Medium, harsh</td><td>Medium, harsh</td><td>Medium, harsh</td><td>Medium, <b>blowing</b></td><td>Medium to high, <b>harsh</b> (the left ventricle is powerful)</td></tr>
    <tr><td>Shape</td><td>Crescendo-decrescendo</td><td>Crescendo-decrescendo</td><td>Crescendo-decrescendo</td><td>Plateau</td><td>Holosystolic</td></tr>
    <tr><td>Location</td><td><b>Aortic area</b></td><td><b>Pulmonic area</b></td><td><b>Erb&rsquo;s point, tricuspid area</b></td><td><b>Lower left sternal border</b></td><td><b>Apex</b></td></tr>
    <tr><td>Radiation</td><td>Often to the <b>carotids</b>, down the left sternal border, even to the apex</td><td>Toward the left shoulder and neck, if loud</td><td>Down the left sternal border to the apex, possibly the base; <b>never to the neck</b></td><td>Right sternum, xiphoid, left midclavicular line; <b>not the axilla</b></td><td>To the <b>left axilla</b></td></tr>
    <tr><td>Maneuvers</td><td>Heard better sitting and leaning forward. <b>Increases</b> with squatting from standing and with leg raise</td><td>None</td><td><b>Decreases with squatting; increases with Valsalva and standing</b></td><td>May increase slightly with inspiration</td><td>Increases with handgrip or squatting</td></tr>
  </table>
  [[GRID:valve-aortic-stenosis,valve-pulmonic-stenosis,hypertrophic-cardiomyopathy]]
  [[GRID:valve-tricuspid-regurgitation,valve-mitral-regurgitation]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; the axilla separates the two regurgitant murmurs</span>
    <p>Both are pansystolic, and radiation across the precordium overlaps, so <em>&ldquo;finding the spot where
    it&rsquo;s loudest is key&rdquo;</em> &mdash; and then the axilla (part 3, 18:12&ndash;19:28, both
    transcripts): <em>&ldquo;<b>mitral regurg does radiate to the axilla. Tricuspid won&rsquo;t</b> radiate to
    the axilla &hellip; that can be one of your key pieces, plus the location.&rdquo;</em></p>
  </div>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; hypertrophic obstructive cardiomyopathy</span>
    <p>The slide says it in capitals: <b>important to learn this murmur so you don&rsquo;t sign off incorrectly on
    a sports physical.</b> It is a disease of abnormally thickened myocardium, most commonly the
    <b>interventricular septum</b>, with the muscle fibers not aligned properly: a high-pitched,
    crescendo-decrescendo, midsystolic murmur heard best at the <b>left lower sternal border</b>, because it is a
    muscle problem rather than a valve one.</p>
    <p>She ranked it above the other ejection murmurs (part 3, 16:50, both transcripts): <em>&ldquo;aortic
    stenosis, pulmonic stenosis, they get to a point where we&rsquo;re worried about them, but <b>[hypertrophic obstructive cardiomyopathy], we&rsquo;re
    worried about it, period</b>. The moment we recognize that this could be [it], we&rsquo;re worried.&rdquo;</em>
    Her two patients with the same murmur: an 80-year-old with fatigue and presyncope (leans toward aortic
    stenosis), and an 18-year-old whose brother has the disease, whose murmur <b>gets louder with Valsalva</b>
    &mdash; <em>&ldquo;alarm bells &hellip; I&rsquo;m sending you for an echocardiogram &hellip; no activity until you
    have that done.&rdquo;</em></p>
  </div>
  <p><b>Aortic stenosis is the one you will meet most.</b> <em>&ldquo;I&rsquo;ve mentioned this one like 50 times
  already. You will hear this one a lot&rdquo;</em> (part 3, 12:53). Her advice at clinical sites: when a patient
  has a known murmur or mechanical valve, spend time listening and feeling for the thrill.</p>

  <h4 class="subsub">Diastolic murmurs</h4>
  <p>Less common and harder to hear than systolic murmurs &mdash; and, in the lecture, more often pathologic:
  <em>&ldquo;when you hear a diastolic murmur &hellip; they&rsquo;re more often going to be somewhat pathologic in
  nature.&rdquo;</em></p>
  <table>
    <tr><th></th><th>Aortic regurgitation</th><th>Pulmonic regurgitation</th><th>Mitral stenosis</th><th>Tricuspid stenosis</th></tr>
    <tr><td>Timing</td><td><b>Early</b> diastolic</td><td><b>Early</b> diastolic</td><td><b>Mid to late</b> diastolic</td><td><b>Mid to late</b> diastolic</td></tr>
    <tr><td>Intensity</td><td>Grade 1&ndash;3</td><td>Grade 1&ndash;3; may increase with inspiration</td><td>Grade 1&ndash;4</td><td>Grade 1&ndash;4</td></tr>
    <tr><td>Pitch</td><td><b>High</b>, blowing &mdash; may be mistaken for breath sounds</td><td>High</td><td><b>Low-pitched rumble &mdash; use the bell</b></td><td>Low-pitched rumble, <b>follows an opening snap</b> &mdash; use the bell</td></tr>
    <tr><td>Shape</td><td>Decrescendo</td><td>Decrescendo</td><td>Decrescendo</td><td>Decrescendo</td></tr>
    <tr><td>Location</td><td>Aortic area, down the left intercostal spaces</td><td>Pulmonic area</td><td><b>Apex</b></td><td>Left lower sternal border, near the xiphoid</td></tr>
    <tr><td>Radiation</td><td>To the apex, if loud</td><td>None</td><td>Little or none</td><td>Little or none</td></tr>
    <tr><td>Maneuvers</td><td><b>Sitting, leaning forward, breath held after exhalation</b></td><td>None</td><td><b>Bell at the apical impulse, left lateral decubitus</b></td><td>The slide repeats the mitral line: bell, left lateral decubitus</td></tr>
  </table>
  [[GRID:valve-aortic-regurgitation,valve-pulmonic-regurgitation,valve-mitral-stenosis,valve-tricuspid-stenosis]]
  <h4 class="subsub">Pericardial friction rub</h4>
  <p>From <b>inflammation of the pericardial sac (pericarditis)</b>: a <b>scratchy, scraping</b> noise heard
  intermittently through <b>both diastole and systole</b>. Variable intensity; <b>high pitch &mdash;
  diaphragm</b>; plateau; most often heard at <b>Erb&rsquo;s point</b>; little radiation. <b>May increase when
  the patient leans forward, exhales and holds the breath.</b> In the lecture: the visceral and parietal
  pericardium normally glide silently; inflamed, they rub with every beat.</p>

  <h3 class="sub" id="cv-maneuvers">1.9 &middot; Objective i &mdash; Maneuvers to evaluate murmurs</h3>
  <p><b>Positions</b> bring the heart closer to the stethoscope:</p>
  <ul>
    <li><b>Left lateral decubitus</b> &mdash; for the apex: S3, S4, mitral stenosis. Lower the head of the bed,
    turn the patient to the left, and reach over them.</li>
    <li><b>Seated, leaning forward, exhale completely and hold</b> &mdash; along the sternal border: aortic
    regurgitation, the pericardial friction rub.</li>
  </ul>
  <p><b>Maneuvers</b> go further: they change filling and resistance so that murmurs that sound alike separate.
  Above all they distinguish the murmurs of <b>mitral valve prolapse</b> and <b>hypertrophic obstructive
  cardiomyopathy</b> from <b>aortic stenosis</b>.</p>
  <table>
    <tr><th>Maneuver</th><th>What it does</th><th>Hypertrophic cardiomyopathy</th><th>Aortic stenosis</th><th>Mitral valve prolapse</th></tr>
    <tr><td><b>Valsalva</b> (strain) &mdash; forceful expiration against a closed airway; the supine patient bears down, or pushes against your hand on the mid-abdomen</td><td>Raises intrathoracic pressure, <b>decreases left ventricular filling (preload)</b></td><td><b>Increases</b></td><td>Softer or no change</td><td>Click earlier, murmur lengthens</td></tr>
    <tr><td><b>Standing quickly from squatting</b></td><td>Blood moves to the legs: <b>less venous return, less preload</b></td><td><b>Louder</b></td><td><b>Softer</b></td><td>Click earlier, murmur lengthens</td></tr>
    <tr><td><b>Squatting from standing, or leg raise</b></td><td>Blood stored in the legs returns: <b>more venous return, more preload</b></td><td><b>Softer</b> (less outflow obstruction)</td><td><b>Louder</b> (more blood rushing past the narrow valve)</td><td>Moved <b>later</b> in systole; murmur shortens</td></tr>
    <tr><td><b>Isometric handgrip</b></td><td>Raises vascular resistance</td><td colspan="3">Increases the systolic murmurs of <b>mitral regurgitation, pulmonic stenosis and ventricular septal defect</b>, and the diastolic murmurs of <b>aortic regurgitation and mitral stenosis</b></td></tr>
  </table>
  [[FIG:maneuver-table]]
  <div class="pearl"><b>One rule generates the whole hypertrophic cardiomyopathy row.</b> Its obstruction is a
  thick septum narrowing the outflow tract, and a <b>smaller</b> ventricle narrows it further. Anything that
  <b>reduces</b> filling (Valsalva, standing) makes it louder; anything that <b>increases</b> filling
  (squatting, leg raise) makes it softer. Aortic stenosis runs the other way, because more blood through a
  fixed narrow valve makes more noise. Valsalva can also identify heart failure and pulmonary hypertension,
  per slide 61.</div>
  <p>Her practical notes (part 3, 7:24&ndash;8:54): the squat-and-stand maneuvers need you and the patient to
  move together, and will be practiced in lab; if a patient cannot squat, raise their legs; for handgrip, have
  them squeeze a rolled-up shirt or a washcloth. And her advice for learning the table: think through what each
  maneuver does to venous return and resistance, and the direction of each change follows.</p>

  <h3 class="sub" id="cv-peripheral">1.10 &middot; Objective j &mdash; Arterial versus venous findings</h3>
  <p><b>Overview.</b> <b>Inspect</b> the upper and lower extremities; <b>palpate</b> the pulses and lymph nodes;
  <b>auscultate</b> the carotid (if not done with the heart), the abdominal arteries and the femoral arteries.</p>
  <h4 class="subsub">Inspection</h4>
  <ul>
    <li><b>Size, symmetry, venous pattern, hair growth pattern, edema.</b></li>
    <li><b>Skin color</b>: erythema, cyanosis, jaundice, pigmentation changes, ulceration.</li>
    <li><b>Capillary refill</b>: press on the fingernail, release, and time the return of pink &mdash; it
    should be <b>2&ndash;3 seconds</b>.</li>
    <li><b>Quincke&rsquo;s pulse (sign)</b>: after releasing the pressure, the capillary bed <b>flashes red to
    pale with each heartbeat</b>.</li>
    <li><b>Always compare one extremity with the other</b>: is the swelling <b>unilateral or bilateral</b>?
    Note relative size and the prominence of veins, tendons and bones. She added that unilateral findings,
    especially arterial ones, may need urgent work-up.</li>
    <li>Look for <b>ulcerations, skin discoloration, skin thickening and varicosities</b> (mild to severe
    dilatation of veins, mainly in the lower extremities).</li>
  </ul>
  <h4 class="subsub">Chronic arterial versus chronic venous insufficiency</h4>
  <table>
    <tr><th></th><th>Chronic arterial insufficiency</th><th>Chronic venous insufficiency</th></tr>
    <tr><td>Pain</td><td><b>Pain with walking progressing to pain at rest (claudication)</b></td><td><b>No pain</b></td></tr>
    <tr><td>Color</td><td><b>Pale or dusky red</b>; <b>foot pallor on elevation, dusky rubor</b> on dependency</td><td><b>Cyanotic or brownish pigmentation</b> (hemosiderin staining); cyanosis of the foot when dependent</td></tr>
    <tr><td>Temperature</td><td><b>Cool</b> to touch</td><td><b>Normal</b></td></tr>
    <tr><td>Edema</td><td><b>None</b></td><td><b>Pitting edema</b></td></tr>
    <tr><td>Skin</td><td><b>Thin, shiny; loss of hair</b></td><td><b>Thickening</b>; stasis dermatitis, purpura, varicosities</td></tr>
    <tr><td>Ulcer</td><td><b>Painful</b> (unless there is neuropathy), at the distal toes</td><td>Around the <b>ankles &mdash; medial and lateral malleolus</b>; small, painful granulation tissue and fibrin; irregular borders, flat or steep</td></tr>
    <tr><td>Gangrene</td><td>May develop</td><td><b>Rare</b></td></tr>
    <tr><td>Pulses</td><td><b>Decreased</b></td><td><b>Normal</b></td></tr>
  </table>
  [[GRID:arterial-insufficiency-legs,arterial-rubor-ulcer,venous-insufficiency]]
  <div class="pearl"><b>Why each column looks the way it does</b> (part 3, 43:16&ndash;49:21). Arterial: not
  enough blood arriving, so the limb is cool, pale, hairless (<em>&ldquo;we don&rsquo;t need that to survive, so
  that becomes less of a priority&rdquo;</em>), and walking produces <b>&ldquo;angina of the legs&rdquo;</b>.
  Venous: <em>&ldquo;It&rsquo;s not the flow down. That&rsquo;s the issue. It&rsquo;s the flow back&rdquo;</em>,
  so fluid pools distally, stretches the skin until it breaks down, and stains it brown. With heavy edema over
  the foot the pulses can be hard to feel even though they are normal &mdash; a small Doppler probe will find
  them.</div>

  <h4 class="subsub">Palpating the pulses</h4>
  <p><b>Grade the amplitude</b> and <b>always compare both sides</b> (the slide adds five exclamation
  marks):</p>
  <table>
    <tr><th>Grade</th><th>4+</th><th>3+</th><th>2+</th><th>1+</th><th>0</th></tr>
    <tr><td>Meaning</td><td>Bounding</td><td>Increased</td><td><b>Brisk, normal</b></td><td>Faint or diminished</td><td>Absent</td></tr>
  </table>
  <p><b>Absent pulses</b> may suggest an arterial disorder from <b>atherosclerosis or systemic embolism</b>;
  consider small vessel disease such as <b>diabetes mellitus</b>. Pulses may be hard to feel in patients who are
  obese or muscular &mdash; which does not mean they are absent.</p>
  <table>
    <tr><th>Pulse</th><th>Where and how</th></tr>
    <tr><td><b>Carotid</b></td><td>Lateral to the trachea. Ask the patient to hold their breath, <b>auscultate before palpating</b>, and palpate <b>one at a time</b></td></tr>
    <tr><td><b>Brachial</b></td><td>Medial to the biceps tendon at the antecubital fossa</td></tr>
    <tr><td><b>Radial</b></td><td>Lateral portion of the wrist</td></tr>
    <tr><td><b>Ulnar</b></td><td>Medial wrist, deep on the flexor surface; partly flexing the wrist helps. <b>A normal ulnar pulse may not be palpable</b></td></tr>
    <tr><td><b>Femoral</b></td><td>Below the inguinal ligament, <b>midway between the anterior superior iliac spine and the pubic symphysis</b>. Palpated under clothing (in lab and testing it is done over clothing, <b>said aloud</b> to the facilitator)</td></tr>
    <tr><td><b>Pulse lag</b></td><td>Radial and femoral <b>simultaneously</b>; a lag suggests <b>coarctation of the aorta</b></td></tr>
    <tr><td><b>Popliteal</b></td><td>Harder to feel and may not be felt &mdash; not an issue if the distal pulses are present. (1) Knee flexed and relaxed, fingertips pressed deep in the midline of the fossa; (2) patient prone, knee at 90 degrees, thumbs pressed deep</td></tr>
    <tr><td><b>Dorsalis pedis</b></td><td>Dorsum of the foot, <b>lateral to the extensor tendon of the great toe</b></td></tr>
    <tr><td><b>Posterior tibial</b></td><td><b>Behind the medial malleolus</b></td></tr>
    <tr><td><b>Abdominal aorta</b></td><td>Press deeply in the upper abdomen; she stressed that what you want is its <b>size</b></td></tr>
  </table>
  [[GRID:pulse-carotid,pulse-brachial,pulse-radial,pulse-ulnar]]
  [[GRID:pulse-femoral,pulse-lag,pulse-popliteal-flexed,pulse-popliteal-prone]]
  [[GRID:pulse-dorsalis-pedis,pulse-posterior-tibial,aorta-palpation]]

  <h4 class="subsub">Auscultating for bruits</h4>
  <p>A <b>bruit</b> is a murmur-like sound of <b>vascular rather than cardiac origin</b>. Listen at:</p>
  <table>
    <tr><th>Site</th><th>Where</th></tr>
    <tr><td><b>Aorta</b></td><td>Midline of the abdomen, above the umbilicus (the slide&rsquo;s line breaks off at &ldquo;halfway between umbilicus&rdquo;; its picture puts the site in the upper midline)</td></tr>
    <tr><td><b>Renal</b></td><td>3&ndash;4 cm lateral to the aorta</td></tr>
    <tr><td><b>Iliac</b></td><td>3&ndash;4 cm lateral to the umbilicus and about 2 cm inferior</td></tr>
    <tr><td><b>Femoral</b></td><td>Directly over the femoral artery, halfway between the anterior superior iliac spine and the pubic symphysis</td></tr>
  </table>
  [[FIG:bruit-sites]]
  <p>A bruit means narrowing, and so possible arterial insufficiency of whatever that vessel supplies &mdash;
  a renal bruit raises the question of whether the kidneys are getting enough blood.</p>

  <h4 class="subsub">Special techniques</h4>
  <p><b>Allen test</b> &mdash; evaluates the arterial supply of the hand by assessing the <b>patency of the radial
  and ulnar arteries</b>:</p>
  <ol>
    <li>Compress both the radial and the ulnar artery.</li>
    <li>Ask the patient to clench the fist for 30 seconds.</li>
    <li>Occlude both arteries, then ask the patient to open the fist.</li>
    <li><b>Release the ulnar artery</b> and watch the hand fill &mdash; that tests the patency of the
    ulnar artery.</li>
    <li>Repeat, releasing the radial artery, to test its patency.</li>
  </ol>
  [[GRID:allen-fist,allen-open,allen-pallor]]
  <p>In the lecture she tied it to its use: it is done <b>before drawing an arterial blood gas</b>, to be sure
  the ulnar artery can supply the hand if the radial is injured.</p>

  <p><b>Ankle brachial index</b> &mdash; the ratio of blood pressures in the foot and arm, <b>calculated for each
  leg</b>: the <b>higher of the two ankle pressures</b> (dorsalis pedis and posterior tibial) divided by the
  <b>brachial systolic pressure</b>. Record it to <b>two decimal places</b>. It is accurate at detecting the fall
  in pressure distal to an arterial stenosis, and is used to assess peripheral arterial disease (pain,
  claudication, numbness, weakness, weak or absent dorsalis pedis and posterior tibial pulses, distal
  pallor).</p>
  [[GRID:abi-formula,abi-ankle]]
  <table>
    <tr><th>Step</th><th>Brachial pressure</th><th>Ankle pressures</th></tr>
    <tr><td>Set-up</td><td>Patient <b>supine and resting 10 minutes</b>; cuff on the arm</td><td>Cuff on the ankle <b>proximal to the malleoli</b></td></tr>
    <tr><td>Find the pulse</td><td>Ultrasound (Doppler) over the brachial pulse</td><td>Ultrasound over the <b>dorsalis pedis</b>, then repeat over the <b>posterior tibial</b></td></tr>
    <tr><td>Measure</td><td colspan="2">Inflate to <b>20 mm Hg above the last audible pulse</b>; deflate slowly, about <b>1 mm Hg per second</b>; record the pressure at which the pulse becomes audible again</td></tr>
    <tr><td>Repeat</td><td><b>Two measurements in each arm</b>; the average is that arm&rsquo;s brachial pressure</td><td>Repeat on the opposite leg</td></tr>
  </table>
  <table>
    <tr><th>Value</th><th>Interpretation</th></tr>
    <tr><td><b>Over 1.40</b></td><td>Suggests a <b>noncompressible, calcified vessel</b></td></tr>
    <tr><td><b>0.90&ndash;1.40</b></td><td><b>Normal</b></td></tr>
    <tr><td><b>Under 0.90</b></td><td>Suggestive of <b>peripheral arterial disease</b></td></tr>
    <tr><td><b>Under 0.50</b></td><td>Suggests <b>severe</b> peripheral arterial disease</td></tr>
  </table>
  <div class="callout"><b>Slide wins on the numbers.</b> In the lecture she rounded the normal range to
  &ldquo;one to one and a half&rdquo; and said worry starts &ldquo;if it&rsquo;s less than our one&rdquo;
  (part 3, 47:12&ndash;48:42). The slides give <b>0.90&ndash;1.40</b> and <b>under 0.90</b>; learn those. What the
  recording adds is context the slides do not have: this is a test for <b>chronic</b> arterial disease
  (claudication, toe ulcers that will not heal). For a suspected <b>acute</b> occlusion or embolus, the class
  suggested a computed tomography angiogram and she agreed. She also said she has ordered many and performed
  none &mdash; where she practiced, radiology did them.</div>

  <p><b>Homans sign</b> &mdash; a test for <b>deep vein thrombosis</b>: <b>quickly and forcefully dorsiflex the
  foot at the ankle with the knee bent</b>. <b>Positive: pain behind the knee.</b></p>
  [[FIG:homans-sign]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; a negative Homans does not reassure</span>
    <p>Perform it when you already <b>suspect</b> a deep vein thrombosis, on the leg you are worried about
    &mdash; not as a screening rule-out (part 3, 50:13&ndash;52:34, both transcripts). Her example stacked the risk
    factors: a long flight back from New Zealand without getting up, a smoker on birth control, a recently
    injured ankle, unilateral swelling. <em>&ldquo;You perform this test and it&rsquo;s positive and you&rsquo;re
    like, that just confirms my suspicion. <b>If it&rsquo;s negative, you&rsquo;re like, I&rsquo;m still
    worried.</b>&rdquo;</em> Deep vein thrombosis itself is taught in the Clinical Medicine and Surgery vascular
    lectures.</p>
    <p><b>Technique: go by the slide.</b> In the recording she described squeezing the calf and dorsiflexing
    the foot; the slide&rsquo;s maneuver is quick, forceful dorsiflexion with the knee bent, and its positive
    finding is pain <b>behind the knee</b>.</p>
  </div>

  <h3 class="sub" id="cv-edema">1.11 &middot; Objective k &mdash; The physical examination findings of peripheral edema</h3>
  <ul>
    <li><b>Definition:</b> excessive fluid in the extravascular interstitial space; up to <b>10% of body
    weight</b> can accumulate before pitting appears.</li>
    <li>Edema <b>obscures veins, tendons and bony prominences</b> &mdash; which is how it shows on inspection.</li>
    <li>Always compare sides: <b>unilateral or bilateral?</b></li>
    <li><b>Pitting</b> is the depression caused by the pressure of the thumb. <b>Press firmly with the thumb for
    at least 2 seconds</b> over the <b>dorsum of the foot</b>, <b>behind the medial malleolus</b>, or <b>over the
    shins</b> &mdash; sites with bone beneath, so there is something to press against.</li>
    <li>Describe both the <b>depth</b> (the grade) and the <b>extent</b> &mdash; how far up the edema reaches.
    She described pitting up to the flanks along the dependent areas. Edema can also be <b>non-pitting</b>.</li>
    <li>Edema is not always a vascular finding: heart failure produces it with healthy vessels. Venous stasis
    edema from the knee down, 3+ and nowhere else, is the pattern that points to the veins.</li>
  </ul>
  <table>
    <tr><th>Grade</th><th>Depth</th><th>Description</th></tr>
    <tr><td>0+</td><td>&mdash;</td><td>No pitting edema</td></tr>
    <tr><td>1+</td><td>2 mm</td><td>Mild; the depression <b>disappears rapidly</b></td></tr>
    <tr><td>2+</td><td>4 mm</td><td>Moderate; disappears in <b>10&ndash;15 seconds</b></td></tr>
    <tr><td>3+</td><td>6 mm</td><td>Moderately severe; may last <b>more than 1 minute</b></td></tr>
    <tr><td>4+</td><td>8 mm</td><td>Severe; can last <b>more than 2 minutes</b></td></tr>
  </table>
  [[GRID:pitting-press,pitting-pit,pitting-grades]]

  <h3 class="sub" id="cv-complete">1.12 &middot; Objective l &mdash; The complete and focused cardiovascular examination</h3>
  <p><b>The order:</b> <b>inspection</b> (including <b>measuring the jugular venous pressure</b>),
  <b>palpation</b>, <b>auscultation</b>, then <b>special techniques</b>. The jugular venous pressure is looked
  for while you inspect the neck and the carotids: find the pulsation and measure its highest point. It will be
  demonstrated in lab.</p>
  <table>
    <tr><th>Preparing yourself</th><th>Preparing the patient</th></tr>
    <tr><td>Stethoscope; <b>ruler, penlight and tongue depressor</b> added for the vascular findings. Enough light
    and exposure &mdash; <b>tangential lighting</b> during inspection, so every contour shows. A <b>quiet room</b>.
    <b>Warm hands and short nails.</b></td><td>The patient in a <b>gown</b>. <b>The examination is never done over
    clothing.</b> Remember positioning &mdash; supine at about 30 to 45 degrees, left lateral decubitus, seated and
    leaning forward.</td></tr>
  </table>
  <p>On a reluctant patient, the lecture&rsquo;s advice: offer to place the stethoscope under the gown while it
  stays covered; the aim is nothing between the stethoscope and the skin. If a patient refuses to be examined, do
  not examine them &mdash; document it thoroughly.</p>
  <p><b>Complete versus focused.</b> The complete examination runs everything above: the precordium in every area
  with both diaphragm and bell, the extra sounds, the peripheral vascular examination head to toe. The focused
  examination keeps the same order and technique but chooses: the areas and positions that match the complaint,
  and the maneuvers that answer the question you have &mdash; <em>&ldquo;depending on what you want to find,
  you&rsquo;re going to pick and choose which ones you do&rdquo;</em> (part 3, 0:00).</p>
  <div class="callout"><b>The Cardiac OSCE (objective structured clinical examination) is on 21 October</b>, a month before this exam. The whole station
  &mdash; history, the examination at thirty degrees, differentials, studies, plan and the one-minute
  presentation &mdash; is on the <a href="''' + OSCE + '''">Cardiac OSCE run-sheet</a>. What this guide adds to it
  is the reasoning behind each finding.</div>

  <button type="button" class="test-yourself-btn" style="--acc:#3a5a40" onclick="window.openTestYourself('Test yourself — Cardiovascular &amp; Peripheral Vascular', TEST_YOURSELF.cardiovascular)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>''' + DECK_NAME + '''</em> (Lauren Reynolds, MSPA, PA-C), Slides
  1&ndash;115, the lecture of 17 September 2026 (three recorded parts, both transcripts read), and the PAJ 5310
  syllabus instructional objectives. All figures are reproduced from the lecture slides and each is cited to its
  slide; publisher marks in the images are left as they appear.</footer>
</section>
<!--/PD2E2L5-->

<footer class="guide-foot">
  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>
  <p style="text-align:center;">Built from your PAJ 5310 lecture decks for personal study &middot; Class of 2028.</p>
  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>
</footer>
</main>'''

TEST_YOURSELF = '''  var TEST_YOURSELF = {
<!--PD2E2TY5-->
    cardiovascular: [
      {q:"A patient's S2 is split on inspiration and single on expiration. How is this described?",
       choices:["Pathologic splitting, suggesting heart disease","Physiologic splitting, which is normal","A fixed split from a stiff ventricle","An opening snap mistaken for P2"],correct:1,
       explain:"Physiologic splitting: A2 and P2 separate on inspiration and fuse on expiration. A split that is still audible on expiration is the pathologic one and suggests heart disease."},
      {q:"An extra heart sound falls just before S1 and is dull and low pitched. Which is it?",
       choices:["S3, the ventricular gallop","An early ejection sound","A mid-systolic click","S4, the atrial gallop"],correct:3,
       explain:"S4 sits just before S1 (Ten-nes-SEE). S3 falls just after S2 (Ken-TUC-ky); ejection sounds and clicks are systolic and high pitched, heard with the diaphragm."},
      {q:"A midsystolic crescendo-decrescendo murmur gets LOUDER when the patient stands quickly from squatting. Which lesion does this favor?",
       choices:["Hypertrophic cardiomyopathy","Aortic stenosis","Tricuspid regurgitation","Pulmonic regurgitation"],correct:0,
       explain:"Standing cuts venous return and preload, which narrows the outflow tract in hypertrophic cardiomyopathy, so its murmur gets louder. Aortic stenosis softens; tricuspid regurgitation is pansystolic and pulmonic regurgitation diastolic."},
      {q:"A pansystolic murmur is loudest at the apex. Where would you expect it to radiate?",
       choices:["To the carotids","To the left shoulder and neck","To the left axilla","Nowhere; it never radiates"],correct:2,
       explain:"Mitral regurgitation radiates to the left axilla. Tricuspid regurgitation, loudest at the lower left sternal border, does not reach the axilla; carotid radiation belongs to aortic stenosis."},
      {q:"Which finding points to chronic VENOUS rather than arterial insufficiency of the leg?",
       choices:["Cool, pale skin with loss of hair","Brown staining, pitting edema, normal pulses","Pain on walking that progresses to pain at rest","Foot pallor on elevation with dependent rubor"],correct:1,
       explain:"Venous insufficiency: brown hemosiderin staining, pitting edema, normal temperature and normal pulses. Coolness, hair loss, claudication and elevation pallor are all arterial."},
      {q:"A murmur is loud and a thrill is palpable over the same area. What is the lowest grade it can be given?",
       choices:["Grade 2 of 6","Grade 3 of 6","Grade 5 of 6","Grade 4 of 6"],correct:3,
       explain:"Grade 4 is the first grade with a palpable thrill. Grades 1 to 3 have no thrill; grades 5 and 6 add hearing it with the stethoscope partly, then entirely, off the chest."}
    ]
<!--/PD2E2TY5-->
  };'''


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index('<div class="layout wrap"')]
    tail = donor[donor.index("</main>") + len("</main>"):]
    ty_start = tail.index("var TEST_YOURSELF = {")
    ty_end = tail.index("\n  };", ty_start) + len("\n  };")
    tail = tail[:ty_start] + TEST_YOURSELF.lstrip() + tail[ty_end:]

    # The donor's Word link would advertise the Exam 1 .docx from the Exam 2
    # folder -- a 404. build_guide_docx.py writes the right one later.
    head = re.sub(r'\s*<link rel="alternate" type="application/vnd\.openxmlformats[^>]*>', "", head)

    # Retheme to the Exam 2 quiz trio. Tints are mapped as well as accents:
    # the donor still carried PD1's rose tints under its olive accents.
    for old, new in (("#4a5c24", "#3a5a40"), ("#b3872e", "#c08a2e"), ("#485a22", "#46704f"),
                     ("#333f1a", "#243a2a"), ("#697d33", "#5f8a68"),
                     ("#1c2014", "#18211a"), ("#adc172", "#9cc3a3"),
                     ("#faf6f7", "#f8faf7"), ("#e5dade", "#d8e3d9"), ("#665b62", "#55625a"),
                     ("#f5e6ec", "#e6f0e7"), ("#f2e9eb", "#eef4ef"), ("#f3e8ec", "#eaf2eb"),
                     ("#efeaf4", "#edf3ee"), ("#f3ecee", "#f3f7f3"), ("#eadfe0", "#e1ebe2")):
        head = head.replace(old, new)
    # Wide comparison tables (the murmur grid has six columns) scroll inside
    # themselves on a phone instead of pushing the whole page sideways.
    head = head.replace("</style>", """  @media(max-width:700px){
    main table{display:block;max-width:100%;overflow-x:auto;-webkit-overflow-scrolling:touch;}
  }
</style>""", 1)
    head = head.replace("/* rose plum */", "/* forest */").replace("/* muted violet */", "/* sage */")
    head = re.sub(r"<title>.*?</title>",
                  "<title>Physical Diagnosis 2 &middot; Exam 2 &mdash; Study Guide</title>",
                  head, count=1, flags=re.S)
    head = re.sub(r'<header class="top">.*?</header>',
        '<header class="top">\n'
        '  <h1>Physical Diagnosis 2 &middot; Exam 2 &mdash; Study Guide</h1>\n'
        '  <p>PAJ 5310 Physical Diagnosis II &middot; Class of 2028 &middot; Exam 2 is Friday 20 November</p>\n'
        '  <p>Covers Lectures 5&ndash;7 &middot; Lecture 5 (Cardiovascular &amp; Peripheral Vascular) so far '
        '&middot; Instructional Objectives taken verbatim from the syllabus</p>\n'
        '</header>', head, count=1, flags=re.S)

    figs = figure_html(IMGDIR)
    used = set()

    def one(m):
        stem = m.group(1).strip()
        assert stem in figs, "no figure named %r" % stem
        used.add(stem)
        return figs[stem]

    def grid(m):
        stems = [x.strip() for x in m.group(1).split(",")]
        for st in stems:
            assert st in figs, "no figure named %r" % st
            used.add(st)
        return '<div class="figgrid">%s</div>' % "".join(figs[st] for st in stems)

    body = re.sub(r"\[\[GRID:([^\]]+)\]\]", grid, BODY)
    body = re.sub(r"\[\[FIG:([^\]]+)\]\]", one, body)
    assert "[[" not in body, "unexpanded figure token remains"
    unused = sorted(set(figs) - used)
    assert not unused, "extracted but never placed: %r" % unused

    html = head + '<div class="layout wrap" data-readable>\n' + TOC + "\n\n" + body + tail

    # Guards: nothing of the donor's may survive, and the page must carry the
    # chrome theme.js gates its toolkit on ([[guide_design_system]]).
    for bad in ("Exam 1 &mdash; Study Guide", "pd2-exam-1-study-guide.docx", "#4a5c24",
                "data-audio-dir", "TEST_YOURSELF.ent", "TEST_YOURSELF.dermatology"):
        assert bad not in html, "donor residue: %r" % bad
    for need in ('class="guide-back-bar"', "window.reportMistake()", "../index.html",
                 "../theme.js", "top:38px"):
        assert need in html, "missing chrome: %r" % need
    assert " open" not in re.findall(r"<details[^>]*>", html).__str__()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB) -- %d figures, %d grids, %d prof-flag boxes"
          % (os.path.relpath(OUT, ROOT), len(html) // 1024, html.count('<figure class="fig">'),
             html.count('<div class="figgrid">'), html.count('class="prof-flag"')))


if __name__ == "__main__":
    main()
