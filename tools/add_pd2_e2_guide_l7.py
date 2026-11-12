#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Physical Diagnosis 2 Exam 2 section 3 (Advanced Hematological Examination).

Lecture 7, Matthew Ward, DMSc, MBA, PA-C (title slide; the calendar's "Ms. Gannon, guest
lecturer" does not match the deck or the recording, in which he speaks of "my tests" and his
emergency department practice), delivered 2026-11-12 11:00, 56 slides, one recorded segment
of 43:25 that starts at slide 6 and ends after slide 55.

The Exam 2 guide is edited in place (guide-link additions are insert-only), so this script
splices Lecture 7 in between fences and never rebuilds the page:
  <!--PD2E2TOC7--> after the Lecture 6 TOC fence, <!--PD2E2L7--> after the Lecture 6 body,
  <!--PD2E2TY7--> after the Lecture 6 Test-yourself set.
Idempotent: each fence is replaced if present, inserted if not. Re-running it REPLACES the
section, so after guide-link additions have been applied, re-run tools/apply_guide_additions.py.

OBJECTIVES are the syllabus's, verbatim. FACTS come from the visible slides only (speaker notes
are not used; slide 55's file carries an unplaced "Symptoms of anemia" picture that is not on the
slide and is not used). EMPHASIS comes from the faster-whisper transcript; Notability holds no
transcript of this recording, so there is no second opinion to diff (flags file:
recordings/pd2-l7-anemia-2026-11-12.flags.md). Overlap trap: CMS I Lecture 46 and Clinical
Pathophysiology Lecture 10 (both Ward, same week) teach the laboratory work-up; none of it is here.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from extract_pd2_e2_l7_figures import figure_html, DECK_NAME

GUIDE = os.path.join(ROOT, "Physical Diagnosis 2 Exam 2", "pd2-exam-2-study-guide.html")
IMGDIR = "pd2-exam-2-study-guide-images"

TOC = '''<!--PD2E2TOC7-->
  <a class="top-link" href="#hematology">3 &middot; Advanced Hematological Examination</a>
  <a href="#he-signposting">How this lecture signposts</a>
  <a href="#he-causes">3.1 Objective a &mdash; The three causes of anemia &amp; the thresholds</a>
  <a href="#he-history">3.2 Objective a &mdash; The hematologic history</a>
  <a href="#he-exam">3.3 Objective b &mdash; Skin, nails, mouth, eyes &amp; nodes</a>
  <a href="#he-systems">3.4 Objective c &mdash; Signs from other organ systems</a>
  <a href="#he-severity">3.5 Objective d &mdash; Severity &amp; specificity</a>
<!--/PD2E2TOC7-->'''

STAR = '<div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized</span>'
SAID = '<div class="prof-flag"><span class="prof-flag-label">&#9733; Said in lecture &mdash; not on a slide</span>'

BODY = '''<!--PD2E2L7-->
<section class="deck" id="hematology">
  <h2 class="deck-title">3 &middot; Advanced Hematological Examination</h2>
  <p class="lecturer">Lecture 7 &middot; Matthew Ward, DMSc, MBA, PA-C &middot; 12 November 2026 &middot;
  56 slides &middot; recorded, 43 minutes</p>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Advanced Hematological System History and Examination</p>
    <ol type="a">
      <li>Define the elements of the medical history that aid in identifying disorders of the hematological system.</li>
      <li>Define the elements and physical examination findings that aid in identifying disorders of the hematological system.</li>
      <li>List presenting signs and symptoms from other organ systems associated with disorders of the hematological system.</li>
      <li>Characterize the signs and symptoms of anemia with regard to severity of anemia and specificity.</li>
    </ol>
  </div>

  <h3 class="sub" id="he-signposting">How this lecture signposts</h3>
  <div class="callout"><p><b>&ldquo;On my tests [you] only get tested on things on the slide.&rdquo;</b> He said it
  outright (4:16): <em>&ldquo;I try to add to this &hellip; I want to add clinical context, but just don&rsquo;t feel like
  you need to write down everything that I&rsquo;m saying.&rdquo;</em> So the stories and asides below (boxes marked
  &ldquo;said in lecture&rdquo;) explain the slides; they are not extra content.</p>
  <p><b>Same diseases, different class.</b> The same week, CMS I Lecture 46 and Clinical Pathophysiology Lecture 10
  (both Dr. Ward) cover anemias and bleeding disorders with their laboratory work-up. This lecture is the
  <b>history and examination</b> only: no blood-count indices, no smear, no treatment.</p>
  <p><b>Coverage.</b> The recording starts on slide 6 (impaired production); slides 1&ndash;5 come from the deck alone.
  It ends after slide 55 with <em>&ldquo;you guys can go over this in the last two case studies&rdquo;</em>: the two cases
  on slide 56 were not worked through (they are answered at the end of section 3.5).</p></div>
  <table>
    <tr><th>Block</th><th>Slides</th><th>Minutes of lecture</th></tr>
    <tr><td>Causes of anemia and thresholds</td><td>3&ndash;6</td><td>about 1 (slides 3&ndash;5 before the recording)</td></tr>
    <tr><td>Symptoms, severity and the bleeding history</td><td>7&ndash;9</td><td>about 6</td></tr>
    <tr><td>Iron and B12 clues, diet, travel, illness</td><td>10&ndash;11</td><td>about 4</td></tr>
    <tr><td>Medication, menstrual, family, social and exposure history</td><td>12&ndash;14</td><td>about 6</td></tr>
    <tr><td>Focused examination, pallor, jaundice, hair, nails</td><td>15&ndash;24</td><td>about 6</td></tr>
    <tr><td>Petechiae, purpura, ecchymoses; eyes, mouth and nodes; glossitis and cheilitis</td><td>25&ndash;35</td><td>about 6</td></tr>
    <tr><td>Heart, bone tenderness and clubbing, lungs</td><td>36&ndash;43</td><td>about 5</td></tr>
    <tr><td>Abdomen, stool blood testing, signs of internal bleeding</td><td>44&ndash;49</td><td>about 5</td></tr>
    <tr><td>B12 neurologic findings and examination</td><td>50&ndash;53</td><td>about 2</td></tr>
    <tr><td>Emergency and interpretation</td><td>54&ndash;55</td><td>about 1.5</td></tr>
  </table>
  <p>The history took the most time (about 16 of 43 minutes), then the skin, nail, mouth and node examination
  (about 12) and the other organ systems (about 12). The quizzes are weighted the same way.</p>

  <h3 class="sub" id="he-causes">3.1 &middot; Objective a &mdash; The three causes of anemia and the thresholds</h3>
  <p>Every anemia comes from one of three mechanisms, and the history and examination are a search for which one:</p>
  <table>
    <tr><th>Mechanism</th><th>What the slides list</th></tr>
    <tr><td><b>Blood loss</b></td><td><b>Trauma, menstrual, gastrointestinal</b></td></tr>
    <tr><td><b>Destruction (hemolysis)</b></td><td><b>Intrinsic (intracorpuscular)</b> abnormalities: <b>sickle cell disease,
    thalassemia syndromes, glucose-6-phosphate dehydrogenase deficiency, hemoglobinopathy</b>, paroxysmal nocturnal
    hemoglobinuria.<br><b>Extrinsic (extracorpuscular)</b> abnormalities: <b>autoimmune disease (lupus), transfusion
    reaction, malaria</b>; <b>microangiopathic hemolytic anemia</b>, for example <b>disseminated intravascular coagulation
    and thrombotic thrombocytopenic purpura</b>.</td></tr>
    <tr><td><b>Impaired red blood cell production</b></td><td><b>Iron, B12 and folic acid deficiency; renal failure;
    chronic disease; hematologic neoplasm or metastatic disease</b></td></tr>
  </table>
  <h4 class="subsub">When is it anemia?</h4>
  <table>
    <tr><th></th><th>Hemoglobin</th><th>Hematocrit</th></tr>
    <tr><td><b>Females</b></td><td>below <b>11.9 g/dL</b> (119 g/L)</td><td>below <b>35 percent</b></td></tr>
    <tr><td><b>Males</b></td><td>below <b>13.6 g/dL</b> (136 g/L)</td><td>below <b>40 percent</b></td></tr>
  </table>
  <p><em>Note:</em> other references (the World Health Organization) use 12 and 13 g/dL; the slide&rsquo;s numbers are the ones
  this course keys.</p>

  <h3 class="sub" id="he-history">3.2 &middot; Objective a &mdash; The hematologic history</h3>
  <h4 class="subsub">Symptoms and severity</h4>
  <ul>
    <li><b>Fatigue is the most common symptom of anemia.</b> Then <b>weakness and reduced exercise tolerance</b>, and
    <b>exertional dyspnea, palpitations, dizziness or lightheadedness</b>.</li>
    <li>Ask about the <b>onset, progression and change from baseline function</b>.</li>
    <li><b>Symptoms at rest, chest pain and syncope</b> are the severity markers.</li>
    <li><b>Severity depends on the rate of onset and on cardiopulmonary disease.</b></li>
  </ul>
  ''' + STAR + '''
    <p><b>Early against late symptoms</b> (1:27&ndash;4:45). <em>&ldquo;If fatigue is the most common symptom, do you think
    fatigue would be an early symptom or a late symptom? Early, right&hellip; even with mild anemia, these people will be
    symptomatic.&rdquo;</em> Exertional dyspnea, palpitations and lightheadedness he called later, more severe; symptoms at
    rest, chest pain and syncope <em>&ldquo;are not common at all &hellip; it&rsquo;s either a very, very severe anemia, or
    they &hellip; have some other comorbidity.&rdquo;</em> A <b>rapid onset</b> is more symptomatic because the body
    cannot adapt. To ask about exertional dyspnea well: <em>&ldquo;what activity can you no longer do as easily?&rdquo;</em></p>
  </div>
  <h4 class="subsub">The bleeding history</h4>
  <table>
    <tr><th>Term or question</th><th>Meaning</th></tr>
    <tr><td>Easy bruising, <b>epistaxis</b> (nosebleeds), <b>gum bleeding</b>, <b>prolonged procedural bleeding</b></td><td>Ask about each directly</td></tr>
    <tr><td><b>Hematochezia</b></td><td><b>Red or maroon blood per rectum</b></td></tr>
    <tr><td><b>Melena</b></td><td><b>Black, tarry stool</b></td></tr>
    <tr><td><b>Hematemesis</b></td><td><b>Blood or coffee-ground emesis</b></td></tr>
    <tr><td>Hematuria and abnormal uterine bleeding</td><td>Blood in the urine; uterine bleeding</td></tr>
    <tr><td>For any bleeding</td><td><b>Onset, frequency, amount and duration</b></td></tr>
  </table>
  ''' + STAR + '''
    <p><b>Nosebleeds and gum bleeding are the ones patients do not report</b> (6:20): <em>&ldquo;the main things &hellip;
    most helpful would be the ones the patient may not complain to you of. So nose bleeds or gum bleeding are concerning
    signs that sometimes patients just don&rsquo;t recognize are abnormal.&rdquo;</em> He also reminded the class that iron
    supplements darken the stool without any bleeding.</p>
  </div>
  <h4 class="subsub">Associated symptoms and risk factors</h4>
  <table>
    <tr><th>Points to</th><th>Clues</th></tr>
    <tr><td><b>Iron deficiency</b></td><td><b>Pica</b> (particularly <b>craving or chewing ice</b>), <b>brittle or spoon-shaped
    nails</b>, possible <b>hair shedding</b></td></tr>
    <tr><td><b>B12 deficiency</b></td><td><b>Paresthesias, impaired balance, reduced vibration or position sense</b></td></tr>
    <tr><td><b>Iron, B12 or folate deficiency</b></td><td><b>Glossitis or angular cheilitis</b></td></tr>
    <tr><td><b>Possible malabsorption</b></td><td><b>Chronic diarrhea, bloating, weight loss</b>; history of <b>gastric bypass,
    gastrectomy or intestinal resection</b></td></tr>
  </table>
  ''' + SAID + '''
    <p><b>Patients do not connect these symptoms to anemia</b> (6:41&ndash;8:30): <em>&ldquo;patients may not even know these
    things are connected &hellip; they won&rsquo;t necessarily come connect their neurological symptoms with anemia.&rdquo;</em>
    And a good diet does not rule deficiency out after bariatric surgery or anything that impairs absorption.</p>
  </div>
  <h4 class="subsub">Diet, travel and recent illness</h4>
  <ul>
    <li><b>Diet:</b> <b>iron-containing foods, animal products, fortified foods, supplements</b>, restrictive eating patterns.
    A <b>vegan diet without B12 supplements or fortified foods</b> is a <b>B12 deficiency risk</b>.</li>
    <li><b>Pica, particularly craving or chewing ice.</b></li>
    <li><b>Travel:</b> destination, timing, <b>febrile illness, infectious exposures</b>.</li>
    <li><b>Recent infection, inflammatory symptoms</b> or change in health; <b>fever, night sweats and unintentional weight
    loss</b>. With fatigue plus unusual bleeding or recurrent infection, he said, the concern broadens to <b>neoplasm or
    metastatic disease</b>.</li>
  </ul>
  <h4 class="subsub">Medication and menstrual history</h4>
  <ul>
    <li>Prescription drugs, over-the-counter medications and supplements.</li>
    <li><b>Nonsteroidal anti-inflammatory drugs, aspirin, anticoagulants</b> (bleeding), <b>metformin, acid-suppressing
    medications</b>; <b>nitrous oxide exposure with possible B12 deficiency</b>.</li>
    <li><b>Menstrual duration, flooding, protection changes, daily impact.</b></li>
    <li><b>Intermenstrual or postmenopausal bleeding.</b> <b>Pregnancy and recent delivery.</b></li>
  </ul>
  ''' + SAID + '''
    <p><b>Ask how much and how often</b> (10:07): &ldquo;are you taking ibuprofen&rdquo; gets a yes; &ldquo;how much&rdquo;
    gets <em>&ldquo;800 milligrams &hellip; three times a day for five years for chronic back pain.&rdquo;</em> And a patient who
    &ldquo;denies heavy bleeding&rdquo; told him she bleeds through tampons and pads so fast she wears a diaper: <em>&ldquo;She
    didn&rsquo;t consider it heavy because for her, it was normal.&rdquo;</em> Ask about flooding and protection changes, not
    just &ldquo;heavy.&rdquo;</p>
  </div>
  <h4 class="subsub">Family, social, medical and exposure history</h4>
  <ul>
    <li><b>Family history:</b> anemia, hemoglobinopathy, abnormal bleeding, <b>unexplained jaundice</b>; <b>relatives requiring
    transfusions or splenectomy</b>; known diagnoses and previous genetic or hemoglobinopathy testing.</li>
    <li><b>Ancestry is risk information only; hemoglobinopathies are possible in any ancestry.</b></li>
    <li><b>Social:</b> <b>alcohol intake</b>, nutritional adequacy, occupational exposures.</li>
    <li><b>Lead exposure:</b> occupational or <b>renovation work, pre-1978 buildings</b>. <b>Benzene</b> or other
    <b>marrow-toxic chemicals</b>.</li>
    <li><b>Chronic kidney disease, inflammatory disease, liver disease, malignancy.</b></li>
    <li><b>Celiac disease, inflammatory bowel disease, chronic diarrhea, gastrointestinal surgery.</b></li>
    <li><b>Anemia with irritable bowel syndrome: evaluate for another explanation.</b></li>
  </ul>

  <h3 class="sub" id="he-exam">3.3 &middot; Objective b &mdash; The examination: skin, nails, mouth, eyes and nodes</h3>
  <p><b>The focused physical examination:</b> general appearance, vital signs and perfusion; <b>skin, conjunctivae, oral
  cavity and nails</b>; <b>lymph nodes</b>; <b>heart and lungs</b>; <b>abdomen, including liver and spleen</b>; a
  <b>targeted neurologic examination</b>.</p>
  <h4 class="subsub">Pallor, jaundice and hair</h4>
  <ul>
    <li><b>Pallor:</b> look at the <b>conjunctivae, oral mucosa, palms and nail beds</b>. It suggests possible anemia but is an
    <b>unreliable hemoglobin estimate</b>.</li>
    <li><b>Jaundice / scleral icterus:</b> <b>hemolytic anemia, including sickle cell disease</b>. Other jaundice causes:
    <b>disorders of bilirubin metabolism</b>.</li>
    <li><b>Hair shedding:</b> possible iron deficiency; <b>multiple other causes</b>.</li>
    <li><b>Normal appearance: anemia still possible.</b></li>
  </ul>
  [[FIG:palmar-pallor]]
  ''' + SAID + '''
    <p><b>His favorite place to check for pallor is the conjunctiva</b> (17:23): <em>&ldquo;it&rsquo;s very easy to check that
    regardless of the patient&rsquo;s skin color.&rdquo;</em> Palms and gums vary with pigmentation, and because anemia is
    systemic there is no normal side to compare with. As a rule of thumb (not a diagnosis) he said that without
    conjunctival pallor the anemia is unlikely to be severe enough for a transfusion. He looks in the eyes for icterus
    too: jaundice is easy to miss in people of color and in dim light.</p>
  </div>
  [[GRID:jaundice-face,jaundice-hands,jaundice-legs]]
  [[FIG:scleral-icterus]]
  [[FIG:hair-shedding]]
  <h4 class="subsub">Nails</h4>
  <ul>
    <li><b>Brittle nails, flattening and longitudinal ridging: nonspecific.</b></li>
    <li><b>Koilonychia: thin, concave, spoon-shaped nails</b>, <b>associated with iron deficiency</b>.</li>
    <li><b>Nail findings are supporting clues; they are unreliable for assessing the cause or the severity.</b></li>
  </ul>
  [[GRID:nail-ridging,nail-ridging-close,koilonychia]]
  <h4 class="subsub">Petechiae, purpura and ecchymoses</h4>
  <table>
    <tr><th>Lesion</th><th>What it is</th></tr>
    <tr><td><b>Petechiae</b></td><td><b>Pinpoint, nonblanching</b> skin hemorrhages</td></tr>
    <tr><td><b>Purpura</b></td><td><b>Larger nonblanching</b> hemorrhagic lesions</td></tr>
    <tr><td><b>Ecchymoses</b></td><td><b>Larger areas of bruising</b></td></tr>
  </table>
  <ul>
    <li>Describe the <b>distribution, extent and palpability</b>.</li>
    <li>Possible causes: <b>platelet or vascular disorders, medications</b>, other conditions.</li>
    <li><b>Increased concern: mucosal bleeding or systemic illness.</b></li>
  </ul>
  [[GRID:petechiae-purpura,petechiae-leg,purpura-legs]]
  <h4 class="subsub">Eyes, mouth and lymph nodes</h4>
  <ul>
    <li><b>Scleral icterus.</b> <b>Pallor of the palpebral conjunctiva</b> (pull the lower lid down) <b>and oral mucosa</b>.</li>
    <li><b>Palatal petechiae and other mucosal bleeding.</b></li>
    <li><b>Cervical and supraclavicular lymph nodes</b>; <b>axillary and inguinal regions when indicated</b>.</li>
    <li><b>Enlarged nodes: location, size, tenderness, consistency, mobility.</b></li>
  </ul>
  [[FIG:conjunctival-pallor]]
  [[GRID:pale-gums,normal-gingiva]]
  [[FIG:palatal-petechiae]]
  <h4 class="subsub">Glossitis and angular cheilitis</h4>
  <ul>
    <li><b>Glossitis:</b> tongue inflammation; a <b>smooth, sore, beefy-red tongue</b>. Possible <b>iron, B12 or folate
    deficiency</b>.</li>
    <li><b>Angular cheilitis:</b> <b>inflammation and fissures at the mouth corners</b>. Possible causes: <b>nutritional
    deficiency, Candida, bacteria, local irritation</b>.</li>
    <li><b>Both findings are nonspecific for a particular deficiency.</b></li>
  </ul>
  [[GRID:glossitis,angular-cheilitis,cheilitis-close]]

  <h3 class="sub" id="he-systems">3.4 &middot; Objective c &mdash; Signs and symptoms from other organ systems</h3>
  <h4 class="subsub">Cardiovascular</h4>
  <ul>
    <li><b>Tachycardia and hyperdynamic circulation.</b></li>
    <li>Possible <b>bounding pulses</b> and a <b>prominent precordial impulse</b>; possible <b>systolic flow murmur</b>.</li>
    <li><b>Heart failure assessment in severe or poorly tolerated anemia.</b></li>
    <li><b>Interpretation: against the symptoms and underlying heart disease.</b></li>
  </ul>
  ''' + SAID + '''
    <p><b>Tachycardia is not always the anemia</b> (29:50): pain, fever and other causes come first, and after
    gastrointestinal blood loss the tachycardia is mostly from the lost <em>volume</em>. The flow murmur he called
    <em>&ldquo;pretty uncommon.&rdquo;</em></p>
  </div>
  <h4 class="subsub">Bone tenderness and clubbing</h4>
  <ul>
    <li><b>Sternal or other bone tenderness: possible marrow disease; nonspecific.</b></li>
    <li><b>Digital clubbing is atypical for uncomplicated anemia</b>: look for an <b>underlying cardiopulmonary,
    gastrointestinal or other systemic disorder</b>.</li>
    <li><b>Clubbing assessment: Schamroth&rsquo;s window, nail-fold profile angle, phalangeal depth ratio.</b></li>
  </ul>
  <table>
    <tr><th>Measure</th><th>Normal</th><th>Clubbing</th></tr>
    <tr><td><b>Nail-fold profile angle</b></td><td><b>under 180&deg;</b></td><td><b>over 180&deg;</b></td></tr>
    <tr><td><b>Schamroth&rsquo;s window</b> (backs of matching fingers held together)</td><td>a small diamond-shaped window between the nails</td><td><b>the window is lost</b></td></tr>
    <tr><td><b>Phalangeal depth ratio</b></td><td>depth at the nail base (distal phalangeal depth) smaller than at the end joint (interphalangeal depth)</td><td><b>depth at the nail base exceeds the end-joint depth</b></td></tr>
  </table>
  [[GRID:clubbing-hands,nail-fold-angle]]
  [[GRID:schamroth,phalangeal-depth]]
  <h4 class="subsub">Pulmonary</h4>
  <ul>
    <li><b>Dyspnea and tachypnea</b> with clinically significant anemia.</li>
    <li><b>Reduced hemoglobin: lower oxygen-carrying capacity.</b></li>
    <li><b>Normal pulse oximetry despite reduced oxygen content.</b></li>
    <li>Respiratory effort; <b>coexisting pulmonary disease or heart failure</b>.</li>
  </ul>
  ''' + STAR + '''
    <p><b>&ldquo;The main thing to take away from our pulmonary findings&rdquo;</b> (33:20): <em>&ldquo;is pulse ox typically
    normal or abnormal in anemia? Normal.&rdquo;</em> The hemoglobin the patient has binds oxygen normally; there is just not
    enough of it. <em>&ldquo;I don&rsquo;t think I&rsquo;ve ever seen anemic patients with a low oxygen, ever.&rdquo;</em></p>
  </div>
  <h4 class="subsub">Gastrointestinal examination and stool blood testing</h4>
  <ul>
    <li>Abdominal <b>tenderness, masses, hepatomegaly, ascites, splenomegaly</b>.</li>
    <li><b>Splenomegaly: hemolysis, infection, portal hypertension, hematologic malignancy.</b></li>
    <li><b>Digital rectal examination when clinically indicated.</b></li>
    <li><b>Negative stool blood test: gastrointestinal bleeding still possible.</b></li>
    <li><b>Positive stool blood test: source and cause of anemia undetermined.</b></li>
    <li>Further gastrointestinal evaluation follows the <b>history, examination and type of anemia</b>.</li>
  </ul>
  ''' + SAID + '''
    <p><b>&ldquo;Iron deficiency anemia is not a diagnosis. I want to say that again&rdquo;</b> (36:30). It is a type of anemia,
    not a cause, and it always warrants investigation: the commonest cause is bleeding (gastrointestinal in men, menstrual in
    women), and he described young adults with colon cancer whose iron deficiency had only been treated. He also called the
    stool blood test low value outside a severe anemia of unknown cause in a patient who cannot give a history.</p>
  </div>
  <h4 class="subsub">Signs of internal bleeding</h4>
  <table>
    <tr><th>Sign</th><th>What it is</th><th>What it suggests</th></tr>
    <tr><td><b>Cullen sign</b></td><td><b>Periumbilical ecchymosis</b></td><td><b>Internal bleeding</b></td></tr>
    <tr><td><b>Grey Turner sign</b></td><td><b>Flank ecchymosis</b></td><td><b>Retroperitoneal or intra-abdominal bleeding</b></td></tr>
  </table>
  <ul>
    <li>Both are possible in <b>severe pancreatitis or another serious abdominal condition</b>.</li>
    <li><b>Uncommon; their appearance may be delayed.</b> <b>Absent signs: significant bleeding still possible.</b></li>
  </ul>
  [[GRID:cullen,grey-turner]]
  ''' + STAR + '''
    <p><b>&ldquo;When you see them, you take them very serious&rdquo;</b> (37:40): the blood is tracking through the tissue
    planes, so it is usually a large amount, and it can take days to show. <em>&ldquo;Just because they&rsquo;re not there
    doesn&rsquo;t mean they&rsquo;re not clinically significant.&rdquo;</em></p>
  </div>
  <h4 class="subsub">Neurologic findings in B12 deficiency</h4>
  <ul>
    <li><b>Paresthesias or numbness in the hands and feet.</b></li>
    <li><b>Reduced vibration and joint-position sense.</b></li>
    <li><b>Sensory ataxia, impaired balance, difficulty walking in the dark.</b></li>
    <li>Peripheral neuropathy and variable reflex abnormalities.</li>
    <li>Possible <b>cognitive, psychiatric or visual changes</b>.</li>
    <li><b>Neurologic findings can occur without anemia or macrocytosis.</b></li>
  </ul>
  <table>
    <tr><th>Structure affected</th><th>Finding</th></tr>
    <tr><td><b>Posterior columns</b></td><td><b>Impaired vibration and position sense</b></td></tr>
    <tr><td><b>Lateral corticospinal tracts</b></td><td><b>Possible spasticity and hyperreflexia</b></td></tr>
    <tr><td>Peripheral nerves</td><td>Possible peripheral neuropathy</td></tr>
  </table>
  [[FIG:spinal-cord-b12]]
  <p><b>The focused neurologic examination:</b> <b>gait and balance</b>; <b>distal vibration and joint-position sense</b>;
  <b>strength and deep-tendon reflexes</b>; <b>Romberg testing with protection against falling</b>. <b>Greater instability
  with eye closure suggests impaired proprioception.</b></p>
  [[FIG:romberg]]
  ''' + STAR + '''
    <p><b>B12 deficiency without anemia</b> (40:20): <em>&ldquo;Patients can have B12 deficiency without having anemia. They can
    have it without having macrocytosis. So just because their hemoglobin is normal, it does not prove they do not have B12
    deficiency.&rdquo;</em> Difficulty walking in the dark: these patients lose position sense and lean on their vision.</p>
  </div>

  <h3 class="sub" id="he-severity">3.5 &middot; Objective d &mdash; Severity and specificity</h3>
  <table>
    <tr><th>Group</th><th>Findings</th><th>What they tell you</th></tr>
    <tr><td><b>General symptoms</b></td><td>Fatigue, weakness, exertional dyspnea, palpitations, lightheadedness</td>
    <td>Anemia&rsquo;s effect; common, nonspecific, present even when mild</td></tr>
    <tr><td><b>Clues to the cause</b></td><td>Bleeding history, jaundice, dietary or surgical history, neurologic findings,
    lymphadenopathy, splenomegaly</td><td>Which mechanism</td></tr>
    <tr><td><b>Urgent assessment</b></td><td><b>Active major bleeding, hypotension, syncope, chest pain, dyspnea at rest, altered
    mental status</b></td><td>Severity; escalate now</td></tr>
  </table>
  <h4 class="subsub">Anemia or bleeding emergency</h4>
  <ul>
    <li>Assess <b>vital signs, mental status, skin perfusion and ongoing blood loss</b>.</li>
    <li><b>Acute hemorrhage: possible instability before the hemoglobin falls.</b></li>
    <li><b>Immediate escalation: stabilization, bleeding control, resuscitation.</b> Oxygen and transfusion according to the
    clinical situation.</li>
  </ul>
  ''' + STAR + '''
    <p><b>The hemoglobin lags</b> (42:28&ndash;43:11): it is a concentration, so after losing whole blood it stays the same until
    fluid shifts back into the circulation. <em>&ldquo;It can be a delayed drop is the main thing to remember &hellip; you&rsquo;re
    not just reassured simply because they have a normal hemoglobin.&rdquo;</em> And a known anemic with new hypotension,
    syncope or chest pain still needs other causes looked for.</p>
  </div>
  <h4 class="subsub">How specific is each finding?</h4>
  <table>
    <tr><th>Finding</th><th>What the slides say</th></tr>
    <tr><td>Pallor</td><td>Possible anemia; <b>unreliable hemoglobin estimate</b>; a normal appearance does not exclude anemia</td></tr>
    <tr><td>Jaundice, scleral icterus</td><td>Hemolysis, but also disorders of bilirubin metabolism</td></tr>
    <tr><td>Hair shedding</td><td>Possible iron deficiency; multiple other causes</td></tr>
    <tr><td>Brittle, flat, ridged nails</td><td><b>Nonspecific</b></td></tr>
    <tr><td>Koilonychia</td><td>Associated with iron deficiency; a supporting clue</td></tr>
    <tr><td>Glossitis, angular cheilitis</td><td><b>Nonspecific</b> among iron, B12 and folate</td></tr>
    <tr><td>Bone tenderness</td><td>Possible marrow disease; <b>nonspecific</b></td></tr>
    <tr><td>Clubbing</td><td><b>Atypical</b> for uncomplicated anemia</td></tr>
    <tr><td>Stool blood test</td><td>Negative: bleeding still possible. Positive: source and cause undetermined</td></tr>
    <tr><td>Cullen, Grey Turner</td><td>Uncommon, may be delayed; absence does not exclude bleeding</td></tr>
  </table>
  <h4 class="subsub">The two case studies (slide 56)</h4>
  <p><b>Case 1:</b> progressive fatigue and exertional dyspnea, heavier menstrual bleeding, frequent ibuprofen use, pallor.
  <em>Additional history for source and urgency?</em> Both clues point to blood loss: define the menstrual bleeding (duration,
  flooding, protection changes, daily impact, intermenstrual bleeding), ask how much ibuprofen and how often, and ask about
  gastrointestinal bleeding (melena, hematochezia, hematemesis). For urgency: symptoms at rest, chest pain, syncope.</p>
  <p><b>Case 2:</b> previous gastric bypass, tingling feet, difficulty walking in the dark. <em>Focused examination findings to
  assess?</em> Gastric bypass is a B12 risk; test <b>distal vibration and joint-position sense, gait and balance, strength and
  reflexes, and Romberg</b> (guarded), and look for glossitis.</p>

  <button type="button" class="test-yourself-btn" style="--acc:#3a5a40" onclick="window.openTestYourself('Test yourself — Hematological examination', TEST_YOURSELF.hematology)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>''' + DECK_NAME + '''</em> (Matthew Ward, DMSc, MBA, PA-C), Slides 1&ndash;56, the
  lecture of 12 November 2026 (one recorded segment, read in full), and the PAJ 5310 syllabus instructional objectives.
  All figures are reproduced from the lecture slides and each is cited to its slide; publisher marks in the images are left
  as they appear.</footer>
</section>
<!--/PD2E2L7-->'''

TY = '''<!--PD2E2TY7-->
    ,hematology: [
      {q:"What is the most common symptom of anemia?",
       choices:["Syncope","Fatigue","Chest pain","Pica"],correct:1,
       explain:"Fatigue is the most common symptom, present even in mild anemia. Symptoms at rest, chest pain and syncope mark severity."},
      {q:"What is melena?",
       choices:["Red or maroon blood per rectum","Blood or coffee-ground emesis","Black, tarry stool","Blood in the urine"],correct:2,
       explain:"Melena is black, tarry stool. Hematochezia is red or maroon blood per rectum; hematemesis is blood or coffee-ground emesis."},
      {q:"Thin, concave, spoon-shaped nails are associated with which deficiency?",
       choices:["Iron","Vitamin B12","Folate","None; they are always normal"],correct:0,
       explain:"Koilonychia is associated with iron deficiency. Nail findings are supporting clues only."},
      {q:"What does pulse oximetry typically show in anemia?",
       choices:["Low saturation","Normal saturation","Low only at rest","It cannot be read"],correct:1,
       explain:"Normal pulse oximetry despite reduced oxygen content: there is less hemoglobin, but what there is saturates normally."},
      {q:"Which is flank ecchymosis?",
       choices:["Cullen sign","Grey Turner sign","Koilonychia","Purpura"],correct:1,
       explain:"Grey Turner sign is flank ecchymosis (retroperitoneal or intra-abdominal bleeding); Cullen sign is periumbilical."},
      {q:"Which spinal cord structures are affected in B12 deficiency?",
       choices:["Anterior horns","Posterior columns and lateral corticospinal tracts","Spinothalamic tracts only","Cerebellum"],correct:1,
       explain:"Posterior columns (vibration and position sense) and lateral corticospinal tracts (spasticity, hyperreflexia)."}
    ]
<!--/PD2E2TY7-->'''


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

    html = splice(html, "<!--PD2E2TOC7-->", "<!--/PD2E2TOC7-->", TOC, "<!--/PD2E2TOC6-->")
    html = splice(html, "<!--PD2E2L7-->", "<!--/PD2E2L7-->", body, "<!--/PD2E2L6-->")
    html = splice(html, "<!--PD2E2TY7-->", "<!--/PD2E2TY7-->", TY, "<!--/PD2E2TY6-->")
    html = html.replace(
        "Lectures 5 (Cardiovascular &amp; Peripheral Vascular) and 6 (Thorax &amp; Lungs) so far",
        "Lectures 5 (Cardiovascular &amp; Peripheral Vascular), 6 (Thorax &amp; Lungs) and 7 (Hematology)")
    for need in ('id="hematology"', "TEST_YOURSELF.hematology", "7 (Hematology)",
                 'href="#he-severity"', "<!--/PD2E2L6-->"):
        assert html.count(need) == 1, "expected exactly one %r" % need
    assert " open" not in str(re.findall(r"<details[^>]*>", html))
    open(GUIDE, "w", encoding="utf-8").write(html)
    sec = html[html.index("<!--PD2E2L7-->"):html.index("<!--/PD2E2L7-->")]
    print("spliced Lecture 7 into %s: %d KB section, %d figures, %d grids, %d prof-flag boxes, %d tables"
          % (os.path.relpath(GUIDE, ROOT), len(sec) // 1024, sec.count('<figure class="fig">'),
             sec.count('<div class="figgrid">'), sec.count('class="prof-flag"'), sec.count("<table>")))


if __name__ == "__main__":
    main()
