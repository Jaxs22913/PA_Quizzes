#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Physical Diagnosis 2 Exam 2 section 2 (Advanced Thorax and Lung Examination).

Lecture 6, Emily Crowe, DMSc, PA-C (a guest; Mayo Clinic, transplant nephrology, per the
title slide), delivered 2026-10-22, 65 slides, recorded in two segments (44.5 + 45.8 min).
The recording starts partway through slide 5; slides 1-4 come from the deck alone.

The Exam 2 guide was BUILT by tools/build_pd2_e2_guide.py and then edited in place
(the truth pass, the "Also tested" fold, guide-link additions), so that builder must not
be re-run. This script splices Lecture 6 into the existing page instead, between fences:
  <!--PD2E2TOC6--> after the Lecture 5 TOC fence, <!--PD2E2L6--> after the Lecture 5
  body, <!--PD2E2TY6--> after the Lecture 5 Test-yourself set.
Idempotent: each fence is replaced if present, inserted if not.

OBJECTIVES are the syllabus's, verbatim, in the syllabus's own order (it puts clubbing
and hemoptysis at c and the dyspnea comparison at d; the deck's objectives slide orders
them differently and is not used). FACTS come from the visible slides only; speaker
notes are not used. EMPHASIS comes from both transcripts of the recording (Notability's
own and faster-whisper), read in full. Where the deck contradicts itself the guide
prints both and the quizzes do not test the point.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from extract_pd2_e2_l6_figures import figure_html, DECK_NAME

GUIDE = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2", "pd2-exam-2-study-guide.html")
IMGDIR = "pd2-exam-2-study-guide-images"
OSCE = "../Physical%20Diagnosis%202%20Exam%201/pd2-pulmonary-osce.html"

TOC = '''<!--PD2E2TOC6-->
  <a class="top-link" href="#thorax">2 &middot; Advanced Thorax &amp; Lung Examination</a>
  <a href="#th-signposting">How this lecture signposts</a>
  <a href="#th-landmarks">2.1 Objective a &mdash; Anatomical landmarks</a>
  <a href="#th-history">2.2 Objective b &mdash; The respiratory history</a>
  <a href="#th-clubbing">2.3 Objective c &mdash; Clubbing &amp; hemoptysis</a>
  <a href="#th-dyspnea">2.4 Objective d &mdash; Sudden versus gradual or intermittent dyspnea</a>
  <a href="#th-adventitious">2.5 Objective e &mdash; Crackles, wheezes &amp; rhonchi</a>
  <a href="#th-five">2.6 Objective f &mdash; Asthma, atelectasis, pneumonia, pneumothorax, effusion</a>
  <a href="#th-exam">2.7 Objective g &mdash; The complete &amp; focused examination</a>
<!--/PD2E2TOC6-->'''

BODY = '''<!--PD2E2L6-->
<section class="deck" id="thorax">
  <h2 class="deck-title">2 &middot; Advanced Thorax &amp; Lung Examination</h2>
  <p class="lecturer">Lecture 6 &middot; Emily Crowe, DMSc, PA-C (guest lecturer) &middot; 22 October 2026 &middot;
  65 slides &middot; recorded in two parts, 90 minutes</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Advanced Pulmonary System Medical History and Examination</p>
    <ol type="a">
      <li>Review the anatomical landmarks for a pulmonary physical examination</li>
      <li>Describe the elements related to interviewing and eliciting a medical history that aid in identifying pulmonary disorders.</li>
      <li>Identify disease processes that may be associated with clubbing and hemoptysis.</li>
      <li>Compare and contrast the physical examination findings of sudden-onset shortness of breath with those of gradual or intermittent presentations.</li>
      <li>Compare and contrast the auscultatory findings of crackles, wheezes, and rhonchi.</li>
      <li>Compare and contrast the physical examination findings of the following: asthma, atelectasis, pneumonia, pneumothorax and pleural effusion.</li>
      <li>Demonstrate proper clinical skills for a complete and focused pulmonary physical examination</li>
    </ol>
  </div>

  <h3 class="sub" id="th-signposting">How this lecture signposts</h3>
  <div class="callout"><p><b>Nothing in 90 minutes was named as on, or off, this exam.</b> Both transcripts of the
  recording were read end to end. The one remark about a question was about her OWN board exam: copious, foul-smelling
  sputum with cystic fibrosis and bronchiectasis, <em>&ldquo;I&rsquo;ve had that as a board question&rdquo;</em> (section
  2.2, ★). Treat the seven objectives as evenly weighted, and use the two signals the lecture does give: what she
  repeated (marked &#9733;) and where the time went (below).</p>
  <p><b>What she skipped, and why.</b> The second half opened with <em>&ldquo;my understanding is that you guys have
  already done &hellip; the lung exam &hellip; So I&rsquo;m not gonna go into like how you set up the patient, maybe
  prep the patient. I have that in here, but I want to get more into like the lung sounds&rdquo;</em> (part 2, 0:09).
  The breathing patterns she would <em>&ldquo;go over &hellip; briefly&rdquo;</em>; chest pain was <em>&ldquo;covered in
  your cardiac lecture&rdquo;</em>; transudate against exudate is <em>&ldquo;something I&rsquo;m sure down the road in
  another lecture&rdquo;</em>. Those slides are still in the deck and still covered below.</p>
  <p><b>The case studies</b> on slides 63 and 64 were not worked through on the recording: she read the first
  case aloud and the recording ends (part 2, 45:46).</p></div>
  <table>
    <tr><th>Block</th><th>Slides</th><th>Minutes of lecture</th></tr>
    <tr><td>Landmarks, lines, lobes, airways and pleurae</td><td>3&ndash;10</td><td>about 9 (the recording starts partway through slide 5)</td></tr>
    <tr><td>The history: open questions, exposures, chest pain</td><td>11&ndash;14</td><td>about 7</td></tr>
    <tr><td>Dyspnea: definition, severity, and the nine conditions</td><td>15&ndash;17</td><td>about 13</td></tr>
    <tr><td>Wheezing, cough and sputum</td><td>18&ndash;22</td><td>about 8</td></tr>
    <tr><td>Hemoptysis, sleep, clubbing</td><td>23&ndash;26</td><td>about 7</td></tr>
    <tr><td>Preparation, survey and breathing patterns</td><td>28&ndash;32</td><td>about 6</td></tr>
    <tr><td>Inspection, chest wall deformities, palpation</td><td>33&ndash;40</td><td>about 10</td></tr>
    <tr><td>Percussion and diaphragmatic excursion (with a long question from the class)</td><td>41&ndash;43</td><td>about 5</td></tr>
    <tr><td>Auscultation and the four breath sounds (recordings played)</td><td>44&ndash;46</td><td>about 6</td></tr>
    <tr><td>Crackles, wheezes, rhonchi, stridor, pleural rub, mediastinal crunch</td><td>47&ndash;51</td><td>about 10</td></tr>
    <tr><td>Egophony, bronchophony, whispered pectoriloquy</td><td>52&ndash;56</td><td>about 4</td></tr>
    <tr><td>Normal findings and the five conditions</td><td>57&ndash;62</td><td>about 4</td></tr>
  </table>
  <p>The examination itself (slides 28&ndash;56) took about half the time, and the sounds the longest of all; the
  quizzes are weighted the same way.</p>

  <h3 class="sub" id="th-landmarks">2.1 &middot; Objective a &mdash; Anatomical landmarks for the pulmonary examination</h3>
  <p><b>Counting ribs and spaces.</b> The <b>sternal angle (angle of Louis)</b> sits beside the <b>2nd rib</b>; the
  space below it is the 2nd intercostal space, and you count down from there. Each intercostal space takes the number
  of the rib above it. From the front the sternal angle also lines up with <b>T4</b>; from behind, the inferior angle
  of the scapula lies at about the <b>7th rib</b>.</p>
  [[GRID:anterior-landmarks,anterior-ribs,posterior-ribs]]
  <h4 class="subsub">The landmarks that go with procedures</h4>
  <table>
    <tr><th>Landmark</th><th>What it is used for</th></tr>
    <tr><td><b>2nd intercostal space</b>, anterior</td><td><b>Needle insertion to decompress a tension pneumothorax</b></td></tr>
    <tr><td>Intercostal space <b>between the 4th and 5th ribs</b></td><td><b>Chest tube insertion</b></td></tr>
    <tr><td><b>T4</b></td><td>The lower margin of an <b>endotracheal tube</b> on a chest x-ray</td></tr>
    <tr><td><b>T7&ndash;T8 (7th intercostal space)</b>, posterior</td><td><b>Thoracentesis</b>: the needle goes in <b>immediately superior to the 8th rib</b>, to drain a large pleural effusion</td></tr>
  </table>
  <p><b>Why always just above a rib.</b> The <b>neurovascular structures run along the inferior margin of each
  rib</b>, so needles and tubes are placed just at the <b>superior</b> rib margin, over the top of the rib below.</p>
  <h4 class="subsub">Vertical lines and the triangle of safety</h4>
  <p>The reference lines are named in the photographs: <b>midsternal, midclavicular and anterior axillary</b> in front;
  <b>anterior axillary, midaxillary and posterior axillary</b> on the side; <b>scapular and vertebral</b> behind.</p>
  [[GRID:lines-anterior,lines-lateral,lines-posterior]]
  <p>The <b>triangle of safety</b> is a region in the <b>midaxillary line</b> bounded by the <b>lateral border of the
  pectoralis major</b> in front, the <b>lateral border of the latissimus dorsi</b> behind, and the <b>nipple line (the
  4th or 5th intercostal space)</b> below. It is the <b>safe position for chest tube insertion</b>.</p>
  [[FIG:triangle-of-safety]]
  <h4 class="subsub">Lungs, fissures and lobes</h4>
  <ul>
    <li><b>Apices</b> extend <b>2&ndash;4 cm above the medial third of the clavicle</b>.</li>
    <li><b>Inferior borders</b> cross the <b>6th rib at the midclavicular line</b>, the <b>8th rib at the midaxillary
    line</b>, and <b>T10 posteriorly</b>.</li>
    <li><b>Right lung: upper, middle and lower lobes. Left lung: upper and lower lobes only.</b></li>
    <li><b>Oblique fissures</b> run from about <b>T3 posteriorly to the 6th rib anteriorly</b>. The <b>right horizontal
    fissure follows the 4th rib</b> to meet the oblique fissure near the <b>5th rib at the midaxillary line</b>.</li>
    <li><b>Pulmonary arteries</b> carry deoxygenated blood from the right ventricle to the lungs; <b>pulmonary
    veins</b> return oxygenated blood to the left atrium.</li>
  </ul>
  [[GRID:lobes-anterior,lobes-right-lateral,lobes-left-lateral,lobes-posterior]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Said in lecture &mdash; not on a slide</span>
    <p><b>There is no left middle lobe</b> &mdash; and she told the story of a resident who reported hearing lung
    sounds there (part 1, 2:50, both transcripts): <em>&ldquo;Your left lung does not have that middle lobe &hellip; there
    was a resident one time telling me, [the] attending, that he heard lung sounds in the left middle lobe. How
    embarrassing, right? Like there is no middle lobe.&rdquo;</em></p>
  </div>
  <h4 class="subsub">The tracheobronchial tree</h4>
  <ul>
    <li>The trachea bifurcates at the <b>carina</b>, near the <b>sternal angle anteriorly</b> and the <b>T4&ndash;T5
    level posteriorly</b>.</li>
    <li><b>Right main bronchus: wider, shorter and more vertical.</b> Left main bronchus: longer and more horizontal;
    it passes beneath the aortic arch before entering the left hilum.</li>
    <li>Branching: trachea &rarr; main bronchi &rarr; lobar bronchi &rarr; segmental bronchi &rarr; bronchioles
    &rarr; <b>alveoli, the primary site of gas exchange</b>.</li>
    <li>Breath sounds over the trachea and large bronchi are normally <b>louder and harsher</b> than peripheral lung
    sounds (section 2.7).</li>
    <li><b>Aspirated material more commonly enters the right bronchial tree, because the right main bronchus is more
    vertical.</b></li>
  </ul>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Aspiration goes right.</b> She gave two cases rather than one (part 1, 4:32&ndash;5:50): a tube passed
    through the nose that goes down the airway instead of the esophagus, and a stroke patient with trouble swallowing
    who comes back days later with fever and a consolidation &mdash; <em>&ldquo;it&rsquo;s most likely going to go
    into that right side because it is the path of least resistance, it&rsquo;s wider, it&rsquo;s shorter. Same goes
    for aspiration.&rdquo;</em> Then she said the slide line a second time.</p>
  </div>
  <h4 class="subsub">The pleurae</h4>
  <p>The pleurae are <b>serous membranes</b> that separate the lungs from the chest wall.</p>
  <table>
    <tr><th></th><th>Visceral pleura</th><th>Parietal pleura</th></tr>
    <tr><td>Where</td><td>Covers the outer surface of the lungs</td><td>Lines the pleural cavity along the inner rib cage
    and the upper surface of the diaphragm</td></tr>
    <tr><td>Nerves</td><td><b>Lacking in sensory nerves</b></td><td><b>Highly innervated by the intercostal and phrenic
    nerves</b></td></tr>
  </table>
  <ul>
    <li><b>Irritation of the parietal pleura produces pleuritic pain with deep inspiration</b> &mdash; in viral
    pleurisy, pneumonia, pulmonary embolism, pericarditis and collagen vascular diseases.</li>
    <li>The <b>surface tension of the pleural fluid</b> keeps the lung in contact with the thoracic wall, so it can
    expand and contract with respiration.</li>
    <li>Accumulated pleural fluid is a <b>pleural effusion</b>: <b>transudative</b> (heart failure, cirrhosis,
    nephrotic syndrome) or <b>exudative</b> (<b>pneumonia</b>, malignancy, pulmonary embolism, tuberculosis,
    pancreatitis).</li>
  </ul>
  [[FIG:pleurae]]

  <h3 class="sub" id="th-history">2.2 &middot; Objective b &mdash; The respiratory history</h3>
  <ul>
    <li><b>Begin with an open-ended question</b> and let the patient describe the symptoms in their own words.</li>
    <li>Clarify <b>onset, timing, triggers, positional changes, environmental exposures and the impact on daily
    activities</b>.</li>
    <li>Respiratory symptoms may come from <b>pulmonary or extrapulmonary disease</b>: cardiovascular, hematologic,
    gastrointestinal and neuromuscular conditions.</li>
    <li>A <b>detailed exposure history</b>: tobacco and nicotine use; <b>marijuana &mdash; smoked, vaped or
    ingested</b>; recreational drugs, including inhaled or intranasal use; occupational and environmental exposures;
    <b>recent travel</b>.</li>
  </ul>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Open-ended first, every time.</b> (part 1, 9:09) <em>&ldquo;When I go into a patient room, even if I have a
    chief complaint, I just say what brought you in here today &hellip; Sometimes you&rsquo;ll miss a big part of the
    story if you go in with leading questions.&rdquo;</em> Her example: the patient &ldquo;came in with shortness of
    breath two days ago&rdquo; who, asked openly, has been getting worse for months.</p>
  </div>
  <h4 class="subsub">Chest pain</h4>
  <p>Always think of cardiovascular causes first, but chest pain can be respiratory or gastrointestinal, so the questions
  have to investigate both thoracic and cardiac (and gastrointestinal) causes. <b>Always ask open-ended questions and
  have the patient point to the pain.</b></p>
  <table>
    <tr><th>Pattern</th><th>Key historical clues</th><th>Consider</th></tr>
    <tr><td>Pressure / squeezing</td><td>Retrosternal; may radiate to the arm, neck, jaw or back; often exertional</td><td>Angina or myocardial infarction</td></tr>
    <tr><td>Sudden / tearing</td><td>Abrupt onset; maximal early; radiates to the back</td><td><b>Aortic dissection</b></td></tr>
    <tr><td><b>Sharp / pleuritic</b></td><td><b>Worse with inspiration or cough</b></td><td><b>Pulmonary embolism, pneumothorax, pneumonia, pleuritis</b></td></tr>
    <tr><td>Sharp / positional</td><td>Worse supine or with inspiration; <b>improved sitting forward</b></td><td><b>Pericarditis</b></td></tr>
    <tr><td>Burning / postprandial</td><td>Worse after meals, bending over or lying down; regurgitation may occur</td><td>Gastroesophageal reflux disease or esophageal disease</td></tr>
    <tr><td><b>Localized / reproducible</b></td><td><b>Provoked by movement or palpation; focal tenderness</b></td><td>Chest wall pain or <b>costochondritis</b></td></tr>
  </table>
  <p>In the lecture she concentrated on two rows: the <b>sharp, pleuritic</b> pattern, <em>&ldquo;because that&rsquo;s how
  it&rsquo;s described when you&rsquo;re having any sort of pleurisy&rdquo;</em>, and the <b>localized, reproducible</b>
  pattern of the chest wall (part 1, 14:44&ndash;15:57).</p>
  <h4 class="subsub">Shortness of breath (dyspnea)</h4>
  <p><b>Dyspnea</b> is a <b>painless but uncomfortable awareness of breathing that is inappropriate to the level of
  exertion</b>.</p>
  <table>
    <tr><th>Characterize the symptom</th><th>Assess functional severity</th></tr>
    <tr><td>Onset: <b>sudden or gradual</b>? Timing: <b>constant or episodic</b>? At rest or with exertion? What
    triggers or relieves it? Is it affected by body position?</td>
    <td>How far can the patient walk? <b>How many flights of stairs without stopping?</b> Can they carry groceries,
    vacuum or make the bed? Has their activity changed from baseline?</td></tr>
  </table>
  <p>The conditions behind dyspnea, and how their onset separates them, are objective d (section 2.4).</p>
  <h4 class="subsub">Wheezing</h4>
  <p><b>Musical respiratory sounds</b> that may be audible to the patient and others. They occur in <b>partial lower
  airway obstruction</b>, from secretions and tissue inflammation in asthma or from a foreign body.</p>
  <h4 class="subsub">Cough</h4>
  <p>Cough is a <b>reflex response to stimuli that irritate receptors in the larynx, trachea or large bronchi</b>:
  mucus, pus or blood; allergens or dust; foreign bodies; extremely hot or cold air. It can also be cardiovascular in
  origin.</p>
  <div class="callout"><b>A slide line the lecturer corrected.</b> Slide 19 prints &ldquo;Could also be cardiovascular in
  origin&rdquo; and, under it, &ldquo;Could also be cardiac in nature&rdquo;. She said the second line was meant to read
  <b>&ldquo;related to medication&rdquo;</b> (part 1, 29:40), and gave the example of a dry cough after starting an
  angiotensin-converting enzyme inhibitor that stops when the drug is stopped.</div>
  <table>
    <tr><th>Step</th><th>What to ask</th></tr>
    <tr><td>1. Duration</td><td><b>Acute: less than 3 weeks. Subacute: 3&ndash;8 weeks. Chronic: more than 8 weeks.</b></td></tr>
    <tr><td>2. Character</td><td>Dry or productive? If productive: <b>amount, color, consistency, odor, or blood</b></td></tr>
    <tr><td>3. Associated symptoms</td><td>Fever, chills or fatigue; hoarseness or throat clearing; wheezing or dyspnea;
    chest or pleuritic pain; weight loss or night sweats; orthopnea or paroxysmal nocturnal dyspnea</td></tr>
    <tr><td>4. Clinical setting</td><td>Tobacco use; allergies or reflux; recurrent infections or aspiration risk;
    irritating particles, chemicals or gases; cardiovascular disease or venous thromboembolism risk factors</td></tr>
  </table>
  <h4 class="subsub">Sputum</h4>
  <table>
    <tr><th>Sputum</th><th>Looks like</th><th>Points to</th></tr>
    <tr><td><b>Mucoid</b></td><td>Translucent, white or gray</td><td>Viral infections, postnasal drip</td></tr>
    <tr><td><b>Purulent</b></td><td>Yellow or green</td><td>Bacterial pneumonia</td></tr>
    <tr><td><b>Foul-smelling</b></td><td>Odor</td><td><b>Anaerobic lung abscess</b></td></tr>
    <tr><td><b>Copious foul-smelling</b></td><td>Large amounts, with odor</td><td><b>Cystic fibrosis, bronchiectasis</b></td></tr>
  </table>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Copious, foul-smelling sputum: cystic fibrosis and bronchiectasis.</b> The one line in the lecture she tied
    to an exam question &mdash; her own board exam. She paired the two (&ldquo;they&rsquo;re one and the same&rdquo;),
    added that <em>&ldquo;all patients with cystic fibrosis&rdquo;</em> go on to bronchiectasis <em>&ldquo;but not all
    bronchiectasis is cystic fibrosis&rdquo;</em>, and then: <em>&ldquo;I&rsquo;m almost [positive] I&rsquo;ve had that as
    a board question&rdquo;</em> (part 1, 36:26&ndash;36:41; our transcript has &ldquo;board&rdquo;, Notability&rsquo;s
    mishears it as &ldquo;fourth&rdquo;). She had spent several minutes before it on how much sputum her cystic fibrosis
    patients brought up.</p>
  </div>
  <h4 class="subsub">Daytime sleepiness, snoring and disordered sleep</h4>
  <ul>
    <li>Ask about <b>excessive daytime sleepiness</b> and <b>snoring</b>. <b>Loud, persistent snoring at night is the
    hallmark symptom of obstructive sleep apnea.</b></li>
    <li>Has anyone in the household <b>witnessed apneas</b> &mdash; pauses in breathing, <b>breathing cessation for 10
    seconds or more</b>?</li>
    <li>Waking with a <b>choking sensation</b>? Waking with a <b>morning headache</b>?</li>
    <li>Other causes of disordered sleep: <b>restless leg syndrome, narcolepsy and insomnia</b>.</li>
  </ul>

  <h3 class="sub" id="th-clubbing">2.3 &middot; Objective c &mdash; Disease processes associated with clubbing and hemoptysis</h3>
  <h4 class="subsub">Hemoptysis</h4>
  <ul>
    <li><b>Blood coughed up from the lower respiratory tract</b>, from blood-streaked sputum to frank blood.</li>
    <li><b>Rare in infants, children and adolescents.</b></li>
    <li><b>Before using the term</b> (in the chart, or to colleagues), <b>try to confirm the source of the bleeding</b>.
    Blood-streaked material can come from the nose, mouth, pharynx or gastrointestinal tract; blood from the
    nasopharynx or the gastrointestinal tract can be aspirated and then coughed out. If it was vomited, it is likely
    gastrointestinal: <b>blood from the stomach is darker than respiratory blood and comes with food particles</b>.</li>
    <li>Ask when it first started (acute against chronic), <b>quantify the volume</b>, and ask about associated symptoms,
    the medical history and medications.</li>
    <li><b>Massive hemoptysis: more than 600 mL in 24 hours</b>. It can be life threatening and <b>requires urgent
    intervention</b>.</li>
  </ul>
  <p><b>Causes of hemoptysis:</b> <b>bacterial pneumonias, chronic bronchitis, bronchiectasis, pulmonary tuberculosis,
  lung abscess, lung cancer, pulmonary embolism</b>. Asthma, atelectasis and pneumothorax are not on the list.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>The 600 mL is a definition, not a waiting period.</b> (part 1, 39:53, both transcripts) <em>&ldquo;It&rsquo;s
    quantified as over 600 mLs in 24 hours. However, if you have a patient and you&rsquo;re in the room and they&rsquo;re
    &hellip; spewing &hellip; blood out of their mouth, that&rsquo;s also an emergency.&rdquo;</em> You do not wait for the
    600 mL. She called hemoptysis <em>&ldquo;probably one of the scariest things I&rsquo;ve seen in my life.&rdquo;</em></p>
  </div>
  <h4 class="subsub">Clubbing</h4>
  <ul>
    <li>A <b>bulbous swelling of the soft tissue at the nail base</b>, with <b>loss of the normal angle between the nail
    and the proximal nail fold</b>.</li>
    <li>The <b>nail bed feels spongy or floating</b>.</li>
    <li>The mechanism is unknown; it involves vasodilation with increased blood flow to the distal digits and changes
    in connective tissue.</li>
  </ul>
  <table>
    <tr><th>Clubbing is seen in</th></tr>
    <tr><td><b>Lung:</b> <b>interstitial lung disease</b> and pulmonary fibrosis, <b>lung cancer</b>, bronchiectasis,
    cystic fibrosis, lung abscess</td></tr>
    <tr><td><b>Beyond the lung:</b> <b>congenital heart disease</b>, <b>inflammatory bowel disease</b>, malignancy</td></tr>
  </table>
  <p style="font-size:.88rem;color:var(--soft);">Slide 26 lists congenital heart disease, interstitial lung disease, lung
  cancer, inflammatory bowel disease and malignancy; slide 33 adds bronchiectasis, pulmonary fibrosis, cystic fibrosis
  and lung abscess. The table is the two lists together. Asthma, pneumothorax and atelectasis appear on neither.</p>
  [[FIG:clubbing]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Said in lecture &mdash; not on a slide</span>
    <p><b>Look at the hands.</b> (part 1, 43:39) <em>&ldquo;I saw this a lot in patients with interstitial lung disease
    &hellip; you do want to look at their hands because there could be an underlying kind of process that&rsquo;s going
    on and it could show up there first.&rdquo;</em></p>
  </div>

  <h3 class="sub" id="th-dyspnea">2.4 &middot; Objective d &mdash; Sudden-onset shortness of breath against gradual or intermittent presentations</h3>
  <p>Onset is the first sort. Read across each row: <b>timing and pattern, associated symptoms, and the history that
  makes it likely</b>.</p>
  <table>
    <tr><th>Onset</th><th>Condition</th><th>Timing and pattern</th><th>Associated symptoms</th><th>Relevant history</th></tr>
    <tr><td rowspan="2"><b>Sudden</b></td><td><b>Pneumothorax</b></td><td><b>Sudden onset</b></td><td><b>Abrupt unilateral
    pleuritic pain</b>, cough</td><td>Trauma, <b>recent procedure, emphysema</b>, prior pneumothorax</td></tr>
    <tr><td><b>Pulmonary embolism</b></td><td><b>Sudden, unexplained dyspnea</b></td><td>Pleuritic pain, <b>hemoptysis</b>,
    syncope, <b>unilateral leg symptoms</b></td><td>Prior venous thromboembolism, <b>surgery, immobility</b>, cancer,
    <b>estrogen</b>, pregnancy or postpartum</td></tr>
    <tr><td><b>Acute</b></td><td><b>Pneumonia</b></td><td>Acute onset</td><td><b>Fever, chills</b>, cough, <b>sputum</b>,
    pleuritic pain</td><td>Recent illness, aspiration risk, <b>immunosuppression</b></td></tr>
    <tr><td><b>Gradual or sudden</b></td><td><b>Left-sided heart failure</b></td><td>Worse with exertion or <b>lying flat</b></td>
    <td><b>Orthopnea, paroxysmal nocturnal dyspnea</b>, cough, <b>edema, weight gain</b></td><td>Cardiac disease,
    <b>hypertension, prior myocardial infarction</b></td></tr>
    <tr><td rowspan="3"><b>Gradual</b></td><td><b>Chronic bronchitis</b></td><td><b>Chronic productive cough followed by
    progressive dyspnea</b></td><td>Sputum, <b>recurrent respiratory infections</b>, wheezing</td><td>Smoking or air
    pollutant exposure</td></tr>
    <tr><td><b>Chronic obstructive pulmonary disease</b></td><td><b>Slowly progressive exertional dyspnea</b>; cough may
    develop later</td><td>Cough, wheezing, <b>scant sputum</b></td><td>Smoking, inhalational exposures, <b>alpha-1
    antitrypsin deficiency</b></td></tr>
    <tr><td><b>Interstitial lung disease</b></td><td><b>Gradually progressive exertional dyspnea</b></td><td><b>Dry cough</b>,
    fatigue, weakness</td><td><b>Autoimmune disease</b>, medications, occupational or environmental exposures</td></tr>
    <tr><td rowspan="2"><b>Episodic</b></td><td><b>Asthma</b></td><td><b>Episodic; symptom-free intervals; often worse at
    night</b></td><td>Wheezing, cough, chest tightness</td><td>Allergens, infections, exercise, <b>cold air</b>,
    irritants</td></tr>
    <tr><td><b>Hyperventilation</b></td><td>Episodic; <b>at rest or with emotional distress</b></td><td><b>Air hunger,
    sighing, lightheadedness, perioral or extremity tingling</b></td><td>Anxiety may contribute, but <b>medical causes
    must be considered first</b></td></tr>
  </table>
  <p><b>Pulmonary embolism</b> is sudden, unexplained dyspnea. The history that raises suspicion: prior venous
  thromboembolism, surgery, <b>recent immobility</b>, cancer, <b>estrogen use</b>, and pregnancy or the postpartum
  period.</p>
  <p><b>Hyperventilation</b> &mdash; episodes of air hunger, sighing, lightheadedness and perioral or extremity tingling,
  at rest or with emotional distress: anxiety may contribute, but <b>consider medical causes first</b>.</p>
  <p><b>What the examination adds</b> for the sudden pair is in sections 2.6 and 2.7: a pneumothorax is hyperresonant
  with decreased or absent fremitus and breath sounds on one side, and the trachea moves only in a tension pneumothorax.
  The gradual group shows up in the chest wall and the sounds: the barrel chest of obstructive disease, the fine crackles
  of fibrosis, the clubbing of interstitial lung disease.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Onset narrows the differential; rest is the worrying setting.</b> (part 1, 16:33&ndash;17:25) <em>&ldquo;You&rsquo;re
    really trying to characterize the sudden versus gradual because that&rsquo;s also going to narrow your
    differential.&rdquo;</em> And: <em>&ldquo;it does become a little bit more worrisome if you&rsquo;re not exerting
    yourself and you&rsquo;re having shortness of breath at rest.&rdquo;</em></p>
    <p><b>Hyperventilation is the last thing you call it.</b> (part 1, 28:04&ndash;28:36) Hyperventilation can be the
    body asking for more oxygen or to blow off carbon dioxide, so <em>&ldquo;although you think anxiety, that&rsquo;s
    going to be the last thing that you&rsquo;re able to call it until you rule out everything else.&rdquo;</em></p>
  </div>

  <h3 class="sub" id="th-adventitious">2.5 &middot; Objective e &mdash; Crackles, wheezes and rhonchi compared</h3>
  <p><b>Crackles</b> (formerly called rales) are non-musical, discontinuous sounds produced by <b>small airways snapping
  open on inspiration</b>: deflated small airways abruptly snap open during inspiration. <b>Wheezes</b> are continuous,
  musical sounds from rapid airflow through bronchial airways narrowed almost to the point of closure. <b>Rhonchi</b>
  differ from wheezes in two ways: they are <b>lower in pitch</b>, and they <b>may clear with coughing</b> (disappear
  with a cough), so secretions may be involved.</p>
  <table>
    <tr><th></th><th>Fine crackles</th><th>Coarse crackles</th><th>Wheezes</th><th>Rhonchi</th></tr>
    <tr><td>Character</td><td colspan="2"><b>Non-musical, discontinuous.</b> Formerly called <b>rales</b>. Deflated small
    airways <b>abruptly snap open during inspiration</b>.</td><td><b>Continuous, musical</b></td><td>A <b>variant of
    wheezes</b>; continuous</td></tr>
    <tr><td>Pitch, loudness</td><td><b>Softer, higher pitched, very brief</b></td><td><b>Louder, lower in pitch</b>,
    brief; a popping sound</td><td>From rapid airflow through bronchi <b>narrowed almost to the point of
    closure</b></td><td><b>Lower in pitch than wheezes</b></td></tr>
    <tr><td>Timing</td><td><b>Mid to late inspiration</b>, especially in the dependent lung</td><td><b>Early inspiration,
    lasting through expiration</b> (biphasic)</td><td>Inspiratory, expiratory or biphasic</td><td>&mdash;</td></tr>
    <tr><td>Changes with</td><td><b>Change with body position</b></td><td><b>Do not change with body position</b> (larger
    airway secretions or significant fluid); heard over any lung region</td><td><b>Less audible as the airways narrow
    further</b></td><td><b>May disappear with coughing</b>, so secretions may be involved</td></tr>
    <tr><td>Examples</td><td><b>Pulmonary fibrosis</b>, interstitial fibrosis, interstitial pneumonitis</td><td>Chronic
    obstructive pulmonary disease, asthma, <b>bronchiectasis</b>, pneumonia, heart failure</td><td><b>Typical of
    asthma</b>, also many pulmonary diseases. <b>Localized</b>: a <b>foreign body, mucous plug or tumor</b></td><td>&mdash;</td></tr>
  </table>
  <p><b>The silent chest.</b> Wheezing becomes <b>less audible as the airways become more narrowed</b>: in the silent chest
  of asthma there is minimal air movement, and it <b>needs immediate intervention</b>.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Quiet is not better in asthma.</b> She raised the silent chest twice, first with auscultation and again with
    wheezes (part 2, 18:59 and 30:25): a patient with asthma who is symptomatic <em>&ldquo;but you do not hear anything
    like wheezing &hellip; it&rsquo;s an emergency &hellip; there&rsquo;s so much narrowing that the air is not
    moving.&rdquo;</em> Crackles and rales are the same thing, and <em>&ldquo;especially when you&rsquo;re working in the
    hospital &hellip; they&rsquo;ll use it synonymously&rdquo;</em> (part 2, 26:51).</p>
  </div>
  <h4 class="subsub">The other adventitious sounds</h4>
  <table>
    <tr><th></th><th>Stridor</th><th>Pleural rub</th><th>Mediastinal crunch (Hamman sign)</th></tr>
    <tr><td>Sound</td><td><b>Continuous, high-frequency, high-pitched, musical</b></td><td><b>Discontinuous,
    low-frequency, grating, creaking or leathery</b>; typically <b>biphasic</b></td><td>A <b>series of precordial crackles
    that keeps time with the heartbeat, not with respiration</b></td></tr>
    <tr><td>Source</td><td>Airflow through a <b>narrowing in the upper respiratory tract</b> (larynx or trachea)</td>
    <td>Inflamed, roughened <b>visceral pleura sliding against the parietal pleura</b>, without its lubricating fluid</td>
    <td><b>Air entering the mediastinum</b>: mediastinal emphysema (pneumomediastinum); severe central chest pain, can
    be spontaneous</td></tr>
    <tr><td>Best heard</td><td><b>Over the neck during inspiration</b> (can be biphasic)</td><td>In the <b>axilla and the
    lower anterior and posterior bases</b>, where chest wall excursion is greatest</td><td>In the <b>left lateral
    decubitus</b> position</td></tr>
    <tr><td>Tells it apart</td><td>&mdash;</td><td><b>Not affected by coughing; louder with firm stethoscope pressure;
    disappears when the patient holds their breath</b> (a pericardial friction rub does not)</td><td>Follows the heart,
    not the breath</td></tr>
    <tr><td>Causes</td><td>Tracheal stenosis after intubation, airway edema after device removal, <b>epiglottitis</b>,
    foreign body, anaphylaxis &mdash; <b>immediate intervention is needed</b></td><td>&mdash;</td><td>Tracheobronchial
    injury, blunt trauma, pulmonary edema, recreational drugs, childbirth, <b>rapid ascent from scuba diving</b></td></tr>
  </table>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Pleural rub against pericardial rub: ask for a breath hold.</b> (part 2, 35:08) <em>&ldquo;The thing
    that&rsquo;s going to differentiate this from a pericardial friction rub is that when you tell the patients [to hold]
    their breath, it will disappear. Versus with the pericardial friction rub, it will continue &hellip; because the
    heart&rsquo;s [still beating].&rdquo;</em> She hears it as <em>&ldquo;a rocking chair&rdquo;</em>.</p>
    <p><b>Stridor is an emergency.</b> She raised it twice: on inspection, as an upper airway obstruction that
    <em>&ldquo;needs urgent evaluation&rdquo;</em> (part 2, 6:46), and on its own slide, <em>&ldquo;this is like a medical
    emergency&rdquo;</em> (part 2, 32:49), with a patient after a house fire whose airway team had to be warned.</p>
  </div>

  <h3 class="sub" id="th-five">2.6 &middot; Objective f &mdash; Asthma, atelectasis, pneumonia, pneumothorax and pleural effusion compared</h3>
  <p>Start from normal, then read each condition against it, one technique at a time.</p>
  <table>
    <tr><th></th><th>Inspection</th><th>Palpation</th><th>Percussion</th><th>Auscultation</th></tr>
    <tr><td><b>Normal</b></td><td>Symmetric, no deformities; no retraction or accessory muscle use</td><td><b>Trachea
    midline</b>; no tenderness; symmetric, unaccentuated fremitus</td><td><b>Resonant and symmetric</b>; diaphragmatic
    excursion in its normal range (section 2.7)</td><td>No adventitious sounds; <b>vesicular sounds except near the
    sternal borders</b></td></tr>
    <tr><td><b>Asthma</b></td><td><b>Tachypnea or dyspnea; retractions</b></td><td>Decreased diaphragmatic excursion;
    <b>diminished tactile fremitus</b></td><td><b>Resonant to diffusely hyperresonant</b></td><td><b>Wheezes</b>, possibly
    crackles; <b>prolonged expiratory phase</b></td></tr>
    <tr><td><b>Atelectasis</b></td><td>Diminished chest wall motion; <b>narrowed intercostal spaces</b>; <b>trachea deviated
    toward the same side (ipsilateral)</b></td><td><b>Diminished fremitus</b> &mdash; may be <b>increased in right upper lobe
    atelectasis</b></td><td><b>Dull over the affected side</b></td><td>Breath sounds <b>usually absent while the bronchial plug
    persists</b> (except right upper lobe: adjacent tracheal sounds may be transmitted); crackles</td></tr>
    <tr><td><b>Pneumonia</b></td><td><b>Trachea midline</b></td><td><b>Increased tactile fremitus</b>; unilateral decrease or
    delay in expansion</td><td><b>Dull over the airless area</b></td><td><b>Bronchial sounds</b> and late inspiratory crackles
    over the involved area; <b>egophony, bronchophony and whispered pectoriloquy</b> heard there</td></tr>
    <tr><td><b>Pneumothorax</b></td><td>Trachea <b>shifted toward the unaffected side if tension pneumothorax</b></td><td><b>Decreased
    or absent fremitus</b> over the affected side</td><td><b>Hyperresonant or tympanic</b> over the affected side</td>
    <td><b>Decreased or absent breath sounds</b>; possible pleural rub</td></tr>
    <tr><td><b>Pleural effusion</b></td><td><b>Asymmetric expansion</b> and <b>trachea shifted to the unaffected side</b> in a
    large effusion</td><td><b>Decreased or absent fremitus</b>, but <b>increased toward the top of a large effusion</b>;
    unilateral decrease or delay in expansion</td><td><b>Dull over the fluid</b>; <b>high</b> diaphragmatic
    level</td><td><b>Decreased or absent</b>; <b>bronchial sounds may be heard near the top of a large effusion</b>; possible
    pleural rub</td></tr>
  </table>
  <div class="callout"><b>Pneumonia&rsquo;s crackles, two ways.</b> Slide 47 lists pneumonia among the coarse crackles
  (early inspiration, lasting through expiration); the slide 60 chart gives late inspiratory crackles over the involved
  area. The quizzes test pneumonia by its fremitus, percussion note, bronchial sounds and voice sounds, not by which
  crackle it makes.</div>
  <p><b>Atelectasis is the most common respiratory issue to occur after surgery.</b></p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Which way the trachea goes.</b> (part 2, 42:08&ndash;42:36) <em>&ldquo;One of the things to think about is with
    atelectasis versus pneumothorax, so where the trachea goes &hellip; deviated towards the opposite side in a tension
    pneumothorax because of all the air pushing. Atelectasis is more of a shrinkage problem with the lung, it&rsquo;s
    pulling it to the same side.&rdquo;</em> A large effusion pushes, like the tension pneumothorax; pneumonia leaves the
    trachea midline.</p>
  </div>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Said in lecture &mdash; not on a slide</span>
    <p>After abdominal surgery the patient avoids a deep breath and the alveoli at the bottom collapse; with a fever after
    surgery, <em>&ldquo;you&rsquo;re not thinking pneumonia, [you&rsquo;re] thinking atelectasis&rdquo;</em> (part 2,
    43:16).</p>
  </div>
  <p><b>Consolidation turns every transmitted finding up.</b> Over normal air-filled lung the breath sounds are
  predominantly vesicular, spoken words are muffled and indistinct, &ldquo;ee&rdquo; is heard as &ldquo;ee&rdquo;,
  whispered words are faint and indistinct if heard at all, and fremitus is normal. Over consolidated, airless lung
  (lobar pneumonia) the sounds are bronchial or bronchovesicular, &ldquo;ee&rdquo; is heard as &ldquo;ay&rdquo;
  (egophony), spoken words are louder (bronchophony), whispered words are louder and clearer (whispered pectoriloquy), and
  fremitus is increased. The hyperinflated lung of obstructive disease turns them down (breath sounds decreased to absent,
  voice sounds and fremitus decreased), and so does the dull lung of pleural effusion, except at its upper margin.
  <b>In a patient with fever and cough, bronchial breath sounds plus egophony more than triples the likelihood of
  pneumonia.</b></p>
  [[FIG:consolidation-table]]

  <h3 class="sub" id="th-exam">2.7 &middot; Objective g &mdash; The complete and focused pulmonary examination</h3>
  <p><b>Preparation.</b> For you: a stethoscope, a marking pen, a ruler or tape measure. For the patient: undressed and
  properly draped, perhaps a gown, and positioned. <b>The order: inspection, palpation, percussion, auscultation.</b></p>
  <table>
    <tr><th>Anterior chest</th><th>Posterior chest</th></tr>
    <tr><td>Supine or sitting; supine helps gently displace the breast in women</td><td><b>Ideally sitting, arms folded
    across the chest.</b> If that cannot be done, <b>roll the patient to one side, then the other</b>, and percuss and
    auscultate in each position</td></tr>
  </table>
  <h4 class="subsub">Initial survey and breathing patterns</h4>
  <p>Vitals are usually done by now, but <b>observe the rate, rhythm, depth and effort of breathing</b>. A healthy adult
  breathes quietly and regularly. <b>Note whether expiration lasts longer than usual</b>, and look for signs of respiratory
  distress.</p>
  <div class="callout"><b>Two normal rates in one deck.</b> Slide 31 says <b>12&ndash;18</b> breaths per minute; the slide 32
  chart says <b>about 14&ndash;20</b> and prints its own &ldquo;Source discrepancy&rdquo; line. In the lecture she took the
  two together as 12 to 20: <em>&ldquo;If it&rsquo;s under 12, it&rsquo;s gonna be bradypnea, and if it&rsquo;s over 20 to
  22, it&rsquo;s gonna be tachypnea&rdquo;</em> (part 2, 1:58). The quizzes do not test the number.</div>
  <table>
    <tr><th>Pattern</th><th>Definition</th></tr>
    <tr><td>Bradypnea</td><td>Slow breathing, with or without increased tidal volume</td></tr>
    <tr><td><b>Tachypnea</b></td><td><b>Rapid, shallow breathing</b></td></tr>
    <tr><td>Rapid deep breathing</td><td><b>Hyperpnea</b> responds to metabolic demand; hyperventilation is independent of
    it</td></tr>
    <tr><td><b>Cheyne-Stokes breathing</b></td><td><b>Deep breathing alternates with apnea</b> (no breathing)</td></tr>
    <tr><td><b>Ataxic (Biot) breathing</b></td><td><b>Irregular</b> breathing; apnea alternates with deep breaths that
    <b>stop suddenly</b></td></tr>
    <tr><td>Sighing respiration</td><td>Frequent sighs interrupt breathing; occasional sighs are normal</td></tr>
    <tr><td><b>Obstructive breathing</b></td><td><b>Prolonged expiration</b> due to narrowed airways and increased airflow
    resistance</td></tr>
  </table>
  [[FIG:breathing-patterns]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Said in lecture &mdash; not on a slide</span>
    <p><b>Do not wave off a fast rate.</b> On tachypnea (part 2, 2:51): <em>&ldquo;this is gonna be something that you need
    to pay attention to clinically because it is an early sign of decompensation in your patient.&rdquo;</em></p>
  </div>
  <h4 class="subsub">Signs of respiratory distress</h4>
  <ul>
    <li><b>Skin and nail color.</b> <b>Cyanosis</b> in the lips, tongue and oral mucosa <b>signals hypoxia</b>. <b>Pallor and
    diaphoresis</b> are common in heart failure and acute coronary syndrome. <b>Clubbing</b> (section 2.3).</li>
    <li><b>Audible sounds.</b> A <b>high-pitched inspiratory whistling (stridor)</b> over the neck or lung means <b>upper
    airway obstruction in the larynx or trachea that needs urgent evaluation</b>. Wheezing is expiratory or continuous.</li>
    <li><b>The neck.</b> Contraction of the accessory muscles &mdash; <b>sternocleidomastoid or scalene during
    inspiration</b>, <b>intercostal or abdominal oblique during expiration</b>. Accessory muscle use can mean difficulty
    breathing from chronic obstructive pulmonary disease or respiratory muscle fatigue. Is the <b>trachea midline</b>? Lateral
    displacement occurs in pneumothorax, pleural effusion and atelectasis.</li>
    <li><b>The size of the chest.</b> The <b>anteroposterior to lateral diameter ratio is usually 0.7 to 0.75, up to
    0.9</b>, and increases with age. In chronic obstructive pulmonary disease it may be greater than 0.9: the <b>barrel
    chest</b>.</li>
  </ul>
  <h4 class="subsub">Inspection</h4>
  <ul>
    <li>The <b>shape</b> of the chest and <b>how it moves</b>. <b>Asymmetric expansion occurs in large pleural
    effusions.</b></li>
    <li><b>Retraction of the intercostal spaces during inspiration</b> (especially the lower spaces) occurs in <b>severe
    asthma, chronic obstructive pulmonary disease or upper airway obstruction</b>.</li>
    <li><b>Unilateral impairment or lag</b> in respiratory movement suggests <b>pleural disease</b> (asbestosis, silicosis) or
    <b>phrenic nerve damage or injury</b>.</li>
  </ul>
  <table>
    <tr><th>Chest wall</th><th>What defines it</th></tr>
    <tr><td>Normal adult</td><td>Lateral diameter greater than the anteroposterior; ratio about 0.7 up to 0.9, rising with
    age</td></tr>
    <tr><td><b>Barrel chest</b></td><td><b>Increased anteroposterior diameter</b>; normal in infancy, and often accompanies
    aging and chronic obstructive pulmonary disease</td></tr>
    <tr><td><b>Pigeon chest (pectus carinatum)</b></td><td>The <b>sternum is displaced anteriorly</b>, increasing the
    anteroposterior diameter; the costal cartilages next to it are depressed</td></tr>
    <tr><td><b>Funnel chest (pectus excavatum)</b></td><td><b>Depression in the lower sternum</b>; <b>compression of the heart
    and great vessels may cause murmurs</b></td></tr>
    <tr><td><b>Traumatic flail chest</b></td><td><b>Multiple rib fractures</b> cause paradoxical movement: as the diaphragm
    descends and intrathoracic pressure falls, the injured area <b>caves inward on inspiration</b> and moves outward on
    expiration</td></tr>
    <tr><td><b>Thoracic kyphoscoliosis</b></td><td>Abnormal spinal curvature and vertebral rotation deform the chest;
    <b>distortion of the lungs may make findings very difficult to interpret</b></td></tr>
  </table>
  [[GRID:chest-normal,chest-barrel,chest-pigeon,chest-funnel]]
  [[FIG:chest-flail-kyphoscoliosis]]
  <h4 class="subsub">Palpation</h4>
  <ul>
    <li>Note <b>tenderness, bruising, respiratory expansion and fremitus</b>.</li>
    <li><b>Crepitus</b> &mdash; crackling or grinding over bones, joints or skin, with or without pain &mdash; is due to
    <b>air in the subcutaneous tissue</b>. It may be felt over overt fractures and arthritic joints. <b>Crepitus with chest
    wall edema</b> is seen in <b>mediastinitis</b>.</li>
    <li><b>Tenderness, bruising and bony step-offs</b> are common over <b>fractured ribs</b>.</li>
    <li><b>Sinus tracts</b> (blind, inflammatory, tube-like tracts opening onto the skin) are rare and suggest infection of the
    underlying pleura and lung (tuberculosis, actinomycosis).</li>
    <li><b>Chest expansion.</b> A <b>unilateral decrease or delay</b> occurs in chronic fibrosis of the lung or pleura, pleural
    effusion, lobar pneumonia, pleural pain with splinting, unilateral bronchial obstruction and <b>paralysis of the
    hemidiaphragm</b>.</li>
    <li><b>Tactile fremitus.</b> <b>Decreased or absent</b> with a thick chest wall, an obstructed bronchus, chronic
    obstructive pulmonary disease, pleural effusion, fibrosis, <b>pneumothorax</b> or an infiltrating tumor. <b>Asymmetric
    decrease</b>: unilateral pleural effusion, pneumothorax, neoplasm. <b>Asymmetric increase: unilateral pneumonia.</b></li>
  </ul>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Reason it out rather than memorize the chart.</b> On expansion (part 2, 14:30): <em>&ldquo;When you think about it
    logically, it all makes sense &hellip; there&rsquo;s reasons that this lung cannot expand.&rdquo;</em> Fibrosis is stiff,
    fluid compresses, pneumonia is less compliant, pain makes the patient splint, an obstructed bronchus lets no air in, a
    paralyzed hemidiaphragm does not contract. On fremitus (part 2, 15:35&ndash;16:09): consolidation transmits the voice
    better, so <em>&ldquo;anything that&rsquo;s increased is related to &hellip; some sort of consolidation there&rdquo;</em>;
    air, fibrosis and scarring transmit it worse.</p>
  </div>
  <h4 class="subsub">Percussion</h4>
  <p>Percussion establishes whether the underlying tissue is <b>air-filled, fluid-filled or consolidated</b>. <b>It cannot
  help with deep-seated lesions.</b> Dullness to percussion over the lung means <b>fluid or solid tissue has replaced the
  air</b>; healthy lung is resonant.</p>
  <table>
    <tr><th>Note</th><th>Means</th></tr>
    <tr><td><b>Resonant</b></td><td><b>Healthy lung</b></td></tr>
    <tr><td><b>Dull</b></td><td><b>Fluid or solid tissue replaces the air</b>: lobar pneumonia, pleural effusion, hemothorax,
    empyema, fibrous tissue or tumor</td></tr>
    <tr><td><b>Generalized hyperresonance</b></td><td>Hyperinflated lungs of <b>chronic obstructive pulmonary disease or
    asthma</b></td></tr>
    <tr><td><b>Unilateral hyperresonance</b></td><td><b>A large pneumothorax or an air-filled bulla</b></td></tr>
  </table>
  <p><b>Diaphragmatic excursion.</b> Percuss down to the level of dullness at full expiration and mark it, then at full
  inspiration and mark it, and measure the distance between. <b>An abnormally high level suggests a pleural effusion, or an
  elevated hemidiaphragm from atelectasis or phrenic nerve injury.</b> The deck gives the normal range two ways: <b>3&ndash;5.5
  cm</b> (slide 43) and <b>3&ndash;5 cm</b> (slide 57); in the lecture she said <em>&ldquo;normal it should be three to
  five point five&rdquo;</em> (part 2, 17:36). The quizzes do not test the number.</p>
  [[FIG:diaphragmatic-excursion]]
  <h4 class="subsub">Auscultation</h4>
  <ul>
    <li>Auscultation is <b>most important for assessing air flow</b>.</li>
    <li>Before you start, <b>ask the patient to cough once or twice</b> to clear mild atelectasis or airway mucus that can
    produce extra sounds.</li>
    <li>The patient is <b>de-robed</b>: clothes, paper gowns and chest hair can produce sounds.</li>
    <li>Breath sounds are <b>decreased</b> when airflow is decreased (obstructive lung disease, respiratory muscle weakness)
    or when transmission is poor (pleural effusion, chronic obstructive pulmonary disease, pneumothorax).</li>
    <li>Is there a <b>silent gap between inspiration and expiration</b>? <b>A gap suggests bronchial breath sounds.</b></li>
    <li>Are <b>bronchovesicular or bronchial sounds heard in unexpected places</b>? Then suspect that <b>air-filled lung has
    been replaced by fluid-filled or consolidated lung</b>.</li>
  </ul>
  <table>
    <tr><th>Breath sound</th><th>Duration</th><th>Expiratory intensity</th><th>Expiratory pitch</th><th>Heard normally</th></tr>
    <tr><td><b>Vesicular</b></td><td><b>Inspiration longer than expiration</b></td><td><b>Soft</b></td><td><b>Relatively
    low</b></td><td><b>Over most of both lungs</b></td></tr>
    <tr><td><b>Bronchovesicular</b></td><td>Inspiration and expiration <b>about equal</b></td><td>Intermediate</td>
    <td>Intermediate</td><td><b>1st and 2nd interspaces anteriorly and between the scapulae</b></td></tr>
    <tr><td><b>Bronchial</b></td><td><b>Expiration longer than inspiration</b></td><td><b>Loud</b></td><td><b>Relatively
    high</b></td><td><b>Over the manubrium</b> (larger proximal airways)</td></tr>
    <tr><td><b>Tracheal</b></td><td>Inspiration and expiration about equal</td><td>Very loud</td><td>Relatively high</td>
    <td>Over the trachea in the neck</td></tr>
  </table>
  [[FIG:breath-sounds]]
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>
    <p><b>Location is what makes a breath sound abnormal.</b> (part 2, 23:42) <em>&ldquo;If you&rsquo;re hearing like bronchial
    sounds in the periphery, where you should be more so hearing vesicular lung sounds, it can suggest a consolidation, like a
    pneumonia.&rdquo;</em> She played all four normal sounds in class and stressed that <em>&ldquo;these are all normal
    [breath] sounds&rdquo;</em> in their own places.</p>
  </div>
  <h4 class="subsub">Special techniques: transmitted voice sounds</h4>
  <p>Used when breath sounds are abnormal (bronchovesicular or bronchial where they should not be), over the same locations
  as palpation, percussion and auscultation. When egophony is present, the patient&rsquo;s spoken &ldquo;ee&rdquo;
  sounds like &ldquo;a&rdquo; through the stethoscope; when it is not, you hear a muffled long E.</p>
  <table>
    <tr><th>Test</th><th>The patient says</th><th>Normal (not present)</th><th>Present (positive)</th></tr>
    <tr><td><b>Egophony</b></td><td>&ldquo;ee&rdquo;</td><td>A <b>muffled long E</b></td><td><b>&ldquo;ee&rdquo; sounds like
    &ldquo;a&rdquo;</b></td></tr>
    <tr><td><b>Bronchophony</b></td><td>&ldquo;ninety-nine&rdquo;, aloud</td><td>Muffled and indistinct</td><td><b>Louder</b></td></tr>
    <tr><td><b>Whispered pectoriloquy</b></td><td>&ldquo;ninety-nine&rdquo; or &ldquo;one-two-three&rdquo;, whispered</td>
    <td><b>Faint and indistinct</b>, if heard at all</td><td><b>Louder, clearer</b> whispered sounds</td></tr>
  </table>
  <p><b>Localized bronchophony and egophony are seen in lobar consolidation.</b> Slide 52 lists the three tests as
  egophony, &ldquo;bronchoscopy&rdquo; and whispered pectoriloquy; the second is bronchophony, the title of slide 54.</p>
  <div class="callout"><b>Pulmonary OSCE (objective structured clinical examination) on 10 November</b>, ten days before this
  exam. The whole station is on the <a href="''' + OSCE + '''">Pulmonary OSCE run-sheet</a>; this section is the reasoning
  behind each finding it asks you to state.</div>

  <button type="button" class="test-yourself-btn" style="--acc:#3a5a40" onclick="window.openTestYourself('Test yourself — Thorax &amp; Lungs', TEST_YOURSELF.thorax)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>''' + DECK_NAME + '''</em> (Emily Crowe, DMSc, PA-C), Slides 1&ndash;65, the lecture
  of 22 October 2026 (two recorded parts, both transcripts read), and the PAJ 5310 syllabus instructional objectives.
  All figures are reproduced from the lecture slides and each is cited to its slide; publisher marks in the images are left
  as they appear.</footer>
</section>
<!--/PD2E2L6-->'''

TY = '''<!--PD2E2TY6-->
    ,thorax: [
      {q:"Dullness, increased tactile fremitus, bronchial breath sounds and egophony over one lobe, with the trachea midline. Which condition?",
       choices:["Pleural effusion","Pneumonia","Atelectasis","Pneumothorax"],correct:1,
       explain:"Consolidation turns the transmitted findings up: increased fremitus, bronchial sounds, egophony. An effusion is dull with DECREASED fremitus; atelectasis pulls the trachea toward it; pneumothorax is hyperresonant."},
      {q:"In which condition is the trachea pulled TOWARD the affected side?",
       choices:["Tension pneumothorax","Large pleural effusion","Atelectasis","Lobar pneumonia"],correct:2,
       explain:"Atelectasis is a shrinkage problem and pulls the trachea to the same side. A tension pneumothorax or a large effusion pushes it away; in pneumonia it stays midline."},
      {q:"A grating sound at the lower lateral chest disappears when the patient holds their breath. What is it?",
       choices:["Pericardial friction rub","Pleural rub","Mediastinal crunch","Coarse crackles"],correct:1,
       explain:"A pleural rub is biphasic and grating, not affected by coughing, louder with firm pressure, and gone with a breath hold. A pericardial friction rub follows the heart and persists."},
      {q:"Which sputum points to cystic fibrosis or bronchiectasis?",
       choices:["Translucent white or gray","Yellow or green","Foul-smelling, small amounts","Copious and foul-smelling"],correct:3,
       explain:"Copious foul-smelling sputum: cystic fibrosis and bronchiectasis. Mucoid (translucent) is viral or postnasal drip; purulent (yellow or green) is bacterial pneumonia; foul-smelling alone suggests an anaerobic lung abscess."},
      {q:"Which breath sound has expiration longer than inspiration and is normally heard over the manubrium?",
       choices:["Vesicular","Bronchovesicular","Bronchial","Tracheal"],correct:2,
       explain:"Bronchial: loud, relatively high-pitched, expiration longer. Vesicular has the long inspiration over most of the lungs; bronchovesicular and tracheal have about equal phases."},
      {q:"During a severe asthma attack the wheezing fades while air movement is minimal. What does this mean?",
       choices:["The attack is resolving","A silent chest needing immediate intervention","Secretions have cleared","A pneumothorax has developed"],correct:1,
       explain:"Wheezing becomes less audible as the airways narrow further. The silent chest of asthma means minimal air movement and needs immediate intervention."}
    ]
<!--/PD2E2TY6-->'''


def splice(html, open_tag, close_tag, block, after_close):
    if open_tag in html:
        return re.sub(re.escape(open_tag) + r".*?" + re.escape(close_tag), lambda _m: block, html,
                      count=1, flags=re.S)
    i = html.index(after_close) + len(after_close)
    return html[:i] + "\n" + block + html[i:]


def main():
    html = open(GUIDE, encoding="utf-8").read()
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

    html = splice(html, "<!--PD2E2TOC6-->", "<!--/PD2E2TOC6-->", TOC, "<!--/PD2E2TOC5-->")
    html = splice(html, "<!--PD2E2L6-->", "<!--/PD2E2L6-->", body, "<!--/PD2E2L5-->")
    html = splice(html, "<!--PD2E2TY6-->", "<!--/PD2E2TY6-->", TY, "<!--/PD2E2TY5-->")
    html = html.replace(
        "Lecture 5 (Cardiovascular &amp; Peripheral Vascular) so far",
        "Lectures 5 (Cardiovascular &amp; Peripheral Vascular) and 6 (Thorax &amp; Lungs) so far")
    for need in ('id="thorax"', "TEST_YOURSELF.thorax", "Lectures 5 (Cardiovascular",
                 'href="#th-exam"', "<!--/PD2E2L5-->"):
        assert html.count(need) == 1, "expected exactly one %r" % need
    assert " open" not in str(re.findall(r"<details[^>]*>", html))
    open(GUIDE, "w", encoding="utf-8").write(html)
    sec = html[html.index("<!--PD2E2L6-->"):html.index("<!--/PD2E2L6-->")]
    print("spliced Lecture 6 into %s: %d KB section, %d figures, %d grids, %d prof-flag boxes"
          % (os.path.relpath(GUIDE, ROOT), len(sec) // 1024, sec.count('<figure class="fig">'),
             sec.count('<div class="figgrid">'), sec.count('class="prof-flag"')))


if __name__ == "__main__":
    main()
