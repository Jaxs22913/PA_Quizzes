#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add PDM I sections 3 (Derm/Ophtho/ENT testing) and 4 (Complete Blood Count).

Instructional Objectives are quoted VERBATIM from the PAJ 5600 syllabus,
including its a/b/c lettering and roman sub-items.

SECTION 3 folds in the 24 August lecture recording (Professor Reynolds,
1:29:47), cross-examined against Notability's independent transcript. The two
agree on 21 and 22 of 35 technical terms respectively -- each catching things
the other misses, which is why both are read. Mine has "fluorescein" ten times
where Notability spells it wrong nine times out of ten; Notability has
"violaceous" twice where mine has it not at all.

SECTION 4 has NO RECORDING yet -- that lecture has not been given. Everything in
it comes from the deck, and where the deck contradicts itself the guide shows
both figures rather than silently picking one.

Section 4 carries 22 photographs, reusing the figures extracted by
extract_pdm_l4_figures.py. Red cell morphology cannot be taught in prose, and
six of those figures are the only source for their content anywhere in the deck.

Idempotent: fenced in <!--PDML3--> / <!--PDML4--> and stripped before reinsert.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1")
GUIDE = os.path.join(DIR, "pdm-exam-1-study-guide.html")
IMGDIR = os.path.join(DIR, "pdm-exam-1-l4-images")
ACC3, ACC4 = "#69406c", "#69406c"


def fig(slug, caption, slide, w=900):
    path = os.path.join(IMGDIR, slug + ".jpg")
    assert os.path.exists(path), "missing figure %s -- run extract_pdm_l4_figures.py" % slug
    from struct import unpack
    return ('<figure class="fig"><img src="pdm-exam-1-l4-images/%s.jpg" decoding="async" '
            'alt="Lecture 4 slide %d figure."><figcaption>%s '
            '<span class="cite">Lecture 4 &middot; Slide %d</span></figcaption></figure>'
            % (slug, slide, caption, slide))


SEC3 = """
<section class="deck" id="derm-ent-ophtho">
  <h2 class="deck-title">3 &middot; Diagnostic Testing for Dermatologic, Ophthalmologic and ENT Disorders</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 3: Diagnostic Testing for Dermatologic, Ophthalmologic, and ENT Disorders</p>
    <ol type="a">
      <li>Discuss indications, advantages, and limitations of common diagnostic tests used in dermatologic disorders.</li>
      <li>Describe indications for skin cultures and wound cultures.</li>
      <li>Interpret potassium hydroxide (KOH) preparations.</li>
      <li>Discuss indications for skin biopsy and common biopsy techniques.</li>
      <li>Discuss the role of diagnostic testing in evaluation of soft tissue infections and abscesses.</li>
      <li>Describe indications and interpretation of: i. Visual acuity testing &middot; ii. Fluorescein examination &middot; iii. Tonometry &middot; iv. Visual field testing</li>
      <li>Discuss indications for: i. Rapid streptococcal testing &middot; ii. Throat cultures &middot; iii. Audiometry &middot; iv. Tympanometry</li>
      <li>Compare and contrast CT and MRI applications in head and neck pathology.</li>
      <li>Select appropriate imaging studies for common ophthalmologic and ENT disorders.</li>
      <li>Identify common abnormalities of the orbit, sinuses, and neck on diagnostic imaging.</li>
      <li>Discuss imaging evaluation of neck masses and deep neck infections.</li>
      <li>Apply diagnostic test selection principles to common dermatologic, ophthalmologic, and otolaryngologic presentations.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the 24 August lecture</span>
  <p><b><mark class="prof-highlight">The one thing she said outright she would NOT ask.</mark></b>
  At 1:00:43, on the animal hearing-range figure: <i>&ldquo;I&rsquo;m not going to ask you to be
  like, what is the range of the killer whale &hellip; I&rsquo;m not gonna ask you about that.&rdquo;</i>
  It is there to show how wide human hearing is, nothing more.</p>
  <p><b>The one thing she flagged as important on the slide AND out loud.</b> At 23:44, on the
  necrotizing infection red flag: <i>&ldquo;You&rsquo;ll notice I put it in red and it&rsquo;s
  bolded &hellip; this is important &hellip; We think of skin infections like it&rsquo;s just a skin
  infection, put them on some antibiotics. <b>No.</b>&rdquo;</i> Hypotension plus a white cell count
  of 15,000 or more plus violaceous skin must be screened for necrotizing infection.</p>
  <p><b>She said the melanoma biopsy rule three times in two minutes</b> (18:24&ndash;20:35):
  <i>&ldquo;You&rsquo;re not going to perform a shave biopsy. You&rsquo;re not going to perform a
  punch biopsy. You are going to perform an <b>excisional</b> biopsy if melanoma is on your
  differential list as a reasonable concern.&rdquo;</i> And the reason it matters:
  <i>&ldquo;If it is melanoma you will be happy and they will be happy that you&rsquo;ve done a
  larger, wider excision.&rdquo;</i></p>
  <p><b>Two live additions that are not on any slide.</b> On the potassium hydroxide preparation
  (13:05): some people pass a flame under the slide a couple of times to help destroy the scale,
  <i>heating it without boiling it</i> &mdash; and if char forms underneath, an alcohol pad cleans
  it off so the microscope view stays clear. On sampling technique (18:44): <b>the technique itself
  determines how easily the specimen can be evaluated</b> &mdash; a punch that misses an edge
  produces a sample the pathologist cannot grade.</p>
  <p><b>Visual field localisation is deferred.</b> At the visual pathway slide she said the detail
  is coming <i>&ldquo;on Thursday&rdquo;</i>. The four patterns in 3.4 below are still fair game.</p>
  </div>

  <h3 class="sub" id="l3-approach">3.1 &middot; Objective a &mdash; Ask the question first</h3>
  <p>Most skin disease is diagnosed by <strong>history and visual inspection</strong>, with office
  testing added only for uncertain diagnoses. Every test should <strong>answer a specific clinical
  question</strong>, and four factors govern which one you pick: <strong>cost, availability,
  invasiveness and diagnostic yield</strong>.</p>
  <table>
    <tr><th>The question</th><th>The test</th></tr>
    <tr><td>Is this an infection?</td><td>Potassium hydroxide preparation, or culture</td></tr>
    <tr><td>Is this a neoplasm, or a rash that will not resolve?</td><td>Biopsy</td></tr>
    <tr><td>Is this an abscess or is it cellulitis?</td><td>Point-of-care ultrasound</td></tr>
  </table>
  <p>In the lecture she put it as <i>&ldquo;anytime you&rsquo;re worried about anything that&rsquo;s
  a malignancy, <b>tissue is the issue</b> &mdash; you need to figure out what the cell line is.&rdquo;</i>
  The closing rule of the whole lecture: <strong>always choose the least invasive test that answers
  the clinical question</strong>.</p>

  <h3 class="sub" id="l3-koh">3.2 &middot; Objectives a &amp; c &mdash; Bedside microscopy and the potassium hydroxide preparation</h3>
  <p>The three bedside tests are <strong>potassium hydroxide, Tzanck and Gram stain</strong>. All
  three are <strong>quick, inexpensive, and both sensitive and specific</strong>; both limitations
  are human &mdash; <strong>operator skill and sampling technique</strong>.</p>
  <table>
    <tr><th>Finding on potassium hydroxide</th><th>Means</th></tr>
    <tr><td>No fungal elements seen</td><td>Negative</td></tr>
    <tr><td><b>Branching, septate hyphae</b></td><td>Dermatophyte</td></tr>
    <tr><td><b>Pseudohyphae WITH budding yeast</b></td><td>Candida</td></tr>
    <tr><td><b>&ldquo;Spaghetti and meatballs&rdquo;</b></td><td>Tinea versicolor</td></tr>
  </table>
  <p><strong>Indications:</strong> tinea corporis, pedis or cruris; onychomycosis; cutaneous
  candidiasis; intertrigo. <strong>Procedure:</strong> scrape with a small scalpel blade onto a
  glass slide, add one drop of <strong>20% potassium hydroxide</strong>, lower the cover glass to
  exclude bubbles, blot the excess with gauze, then survey at <strong>10&times;</strong> with the
  condenser <strong>lowered to reduce illumination</strong> so epithelial cells become visible, and
  examine anything suspicious at <strong>40&times;</strong>.</p>
  <p><strong>Sensitivity depends on adequate scraping</strong>, and a clinical-only diagnosis can
  misidentify a fungal infection &mdash; which is the argument for doing the test at all.</p>

  <h3 class="sub" id="l3-biopsy">3.3 &middot; Objectives d &amp; e &mdash; Biopsy, the melanoma rule, and soft tissue infection</h3>
  <table>
    <tr><th>Technique</th><th>What it gives, and when</th></tr>
    <tr><td><b>Shave</b></td><td>Raised epidermal lesions; basal and squamous cell carcinoma; superficial rashes</td></tr>
    <tr><td><b>Punch</b></td><td><b>Full-thickness</b> sample; inflammatory rashes and small lesions</td></tr>
    <tr><td><b>Excisional</b></td><td>Removes the entire lesion &mdash; <b>preferred for suspected melanoma</b></td></tr>
  </table>
  <p><strong>The melanoma rule.</strong> A <strong>narrow excisional biopsy with 1&ndash;3&nbsp;mm
  margins</strong>, taken <strong>to a depth that avoids transecting the base so Breslow depth can
  be measured</strong>. Acceptable excisional methods are fusiform or elliptical, punch, and deep
  shave or saucerization &mdash; <strong>all must go below the lesion</strong>. A partial or
  superficial shave is acceptable <strong>only when suspicion is low</strong>, and it
  <strong>may underestimate Breslow depth</strong>; facial, acral and very large lesions are named
  here too.</p>
  <p><mark class="prof-highlight">Do not confuse these millimetres with the centimetres in CMS I
  Lecture 9.</mark> <strong>1&ndash;3&nbsp;mm is the DIAGNOSTIC biopsy margin</strong> that
  establishes Breslow depth; <strong>0.5&ndash;2&nbsp;cm is the definitive RE-EXCISION margin</strong>
  that follows once the depth is known.</p>
  <table>
    <tr><th>T category</th><th>Breslow depth</th></tr>
    <tr><td>Tis</td><td>Melanoma in situ</td></tr>
    <tr><td>T1</td><td>1&nbsp;mm or less</td></tr>
    <tr><td>T2</td><td>More than 1 and up to 2&nbsp;mm</td></tr>
    <tr><td>T3</td><td>More than 2 and up to 4&nbsp;mm</td></tr>
    <tr><td>T4</td><td>More than 4&nbsp;mm</td></tr>
  </table>
  <p><strong>Soft tissue infection.</strong> Point-of-care ultrasound reliably separates the two:
  <strong>cellulitis</strong> shows dermal thickening, increased echogenicity and
  <strong>cobblestoning</strong> (which the deck footnotes as non-specific, since venous stasis does
  it too); an <strong>abscess</strong> shows a hypoechoic or heterogeneous collection, possibly with
  debris or septations, and <strong>posterior acoustic enhancement</strong>. Computed tomography and
  magnetic resonance are reserved for <strong>deep-space infection, necrotizing infection, foreign
  body and gas</strong>, and <strong>contrast magnetic resonance best defines the extent of tissue
  damage</strong>.</p>
  <div class="callout"><b>The red flag she bolded on the slide and repeated out loud.</b>
  <b>Hypotension + white blood cell count of 15,000 or more + violaceous (purple) skin</b> must be
  screened for <b>necrotizing fasciitis</b>. Her framing: a patient who looks <i>too sick for a skin
  infection</i> is the whole point.</div>

  <h3 class="sub" id="l3-cultures">3.4 &middot; Objective b &mdash; Skin and wound cultures</h3>
  <p>Culture <strong>purulent lesions</strong>, sampling pus from abscesses, carbuncles and
  furuncles. <strong>Empiric treatment without culture is reasonable in typically presenting,
  uncomplicated cases.</strong> <strong>Do not culture an inflamed epidermoid cyst.</strong>
  Consider culturing a non-healing or chronic wound when the patient is
  <strong>immunocompromised</strong>, when <strong>methicillin-resistant <i>Staphylococcus
  aureus</i></strong> is suspected, or after <strong>treatment failure</strong>.</p>
  <p><strong>The Levine method.</strong> Clean the wound with <strong>sterile water or saline, NOT
  an antimicrobial solution</strong>. Identify <strong>1 to 2&nbsp;cm of clean wound tissue</strong>.
  <strong>Rotate the applicator for five seconds</strong> with enough pressure to express fluid from
  the tissue. <strong>Do not sample exudate, eschar or necrotic material.</strong></p>
  <p>Culture buys you <strong>organism identification plus susceptibilities</strong>. Its limits:
  superficial swabs are <strong>prone to contamination and colonisation</strong> and
  <strong>may not correlate with deep infection</strong>, so in complex wounds &mdash; diabetic foot
  ulcers, pressure ulcers &mdash; a <strong>deeper tissue biopsy or aspirate gives higher yield</strong>.</p>

  <h3 class="sub" id="l3-eye">3.5 &middot; Objective f &mdash; The four ophthalmic tests</h3>
  <p>The examination runs on <strong>VVEEPP</strong>: <strong>v</strong>isual acuity,
  <strong>v</strong>isual fields, <strong>e</strong>xternal exam, <strong>e</strong>xtraocular
  movements, <strong>p</strong>upils, <strong>p</strong>ressure.</p>
  <table>
    <tr><th>Test</th><th>Indication</th><th>Reading it</th></tr>
    <tr><td><b>Visual acuity</b></td><td><b>EVERY eye complaint</b></td>
      <td>Snellen for distance, Rosenbaum for near. Test best-corrected acuity; <b>use a pinhole if reduced</b>. <b>Corrects with pinhole &rarr; refractive. Does not correct or worsens &rarr; eye pathology.</b> Unilateral loss &rarr; optic nerve or ocular; bilateral &rarr; systemic or intracranial</td></tr>
    <tr><td><b>Visual fields</b></td><td>Assessing the visual pathway</td>
      <td>Confrontation at the bedside; formal perimetry or Amsler grid by ophthalmology. <b>Central scotoma</b> &rarr; macula or optic nerve. <b>Peripheral loss</b> &rarr; glaucoma. <b>Bitemporal hemianopia</b> &rarr; chiasmal, think pituitary. <b>Homonymous hemianopia</b> &rarr; retrochiasmal, query stroke</td></tr>
    <tr><td><b>Fluorescein</b></td><td>Eye pain, foreign-body sensation, trauma, contact-lens wear, red eye</td>
      <td>Cobalt-blue light, <b>after a topical anesthetic</b>. <b>Linear</b> &rarr; abrasion. <b>Branching or dendritic</b> &rarr; herpetic keratitis. <b>Fixed dense staining or opacity</b> &rarr; ulcer, <b>urgent referral</b></td></tr>
    <tr><td><b>Tonometry</b></td><td>Glaucoma; <b>acute angle-closure is an ophthalmologic emergency</b></td>
      <td>Normal pressure <b>10&ndash;21&nbsp;mm Hg</b>. <b>Pressure alone is insufficient</b> &mdash; most open-angle glaucoma has normal pressure, and readings vary with corneal thickness</td></tr>
  </table>
  <p><strong>Optic disc cupping.</strong> Normal cup-to-disc ratio is about <strong>0.3</strong>;
  glaucomatous injury gives <strong>greater than 0.7</strong>. The healthy disc has a small central
  cup with a robust neuroretinal rim; the glaucomatous disc is <strong>enlarged, deeply excavated,
  with an undermined rim</strong> and lamina cribrosa collapse. <strong>Excavated, not merely pale,
  is what distinguishes glaucoma from other optic atrophies.</strong></p>
  <p><strong>Ocular hypertension versus glaucoma:</strong> raised pressure with no optic damage and
  normal fields is <strong>ocular hypertension</strong>, a risk factor. Add optic nerve damage and
  it is <strong>glaucoma</strong>.</p>

  <h3 class="sub" id="l3-ent">3.6 &middot; Objective g &mdash; Throat, hearing and the middle ear</h3>
  <table>
    <tr><th></th><th>Rapid streptococcal antigen test</th><th>Throat culture</th></tr>
    <tr><td>Indication</td><td>Suspected group A streptococcal pharyngitis with supportive clinical features</td><td>Confirming a negative rapid test <b>in children</b>; persistent or severe symptoms</td></tr>
    <tr><td>Advantage</td><td>Fast, point-of-care</td><td><b>Gold standard &mdash; highest sensitivity</b></td></tr>
    <tr><td>Limitation</td><td>Sensitivity only <b>70&ndash;90%</b>, so false negatives</td><td>Delayed <b>24&ndash;48 hours</b></td></tr>
  </table>
  <p><strong>A negative rapid test in a child should be confirmed by culture; this is not routinely
  required in adults.</strong> And <strong>do NOT use antistreptococcal antibody titres to diagnose
  acute pharyngitis.</strong></p>
  <p><strong>Audiometry</strong> quantifies the <strong>degree and type</strong> of hearing loss
  &mdash; conductive versus sensorineural &mdash; after abnormal examination findings. Indications:
  suspected or confirmed loss, persistent otitis media with effusion, and <strong>asymmetric loss,
  to screen for retrocochlear pathology</strong>. An <strong>air&ndash;bone gap of 10&nbsp;dB or
  more correlates with middle-ear fluid</strong>; a primary-care <strong>fail is more than
  20&nbsp;dB hearing level at one or more frequencies</strong>.</p>
  <p>Screening presents tones at the upper limits of normal hearing &mdash;
  <strong>25&ndash;30&nbsp;dB for adults, 15&ndash;20&nbsp;dB for children</strong>. A threshold
  search finds the softest sound heard at each frequency <strong>50% of the time</strong>. On the
  audiogram, <strong>intensity is on the vertical axis, right ear is a red circle and left ear a
  blue cross</strong>. Bone conduction uses a device vibrating through the <strong>forehead or
  mastoid</strong>. In the lecture she added the clinical shape of it: <strong>we lose the high
  frequencies first</strong>, which is the pattern of presbycusis and sensorineural loss.</p>
  <p><strong>Tympanometry</strong> varies <strong>air pressure in the external canal</strong> while
  measuring <strong>reflected energy</strong> from a tone &mdash; <strong>the less compliant the
  system, the greater the intensity reflected back</strong>. Pressure runs along the horizontal axis
  and compliance the vertical, with a normal peak at <strong>50&nbsp;mm H<sub>2</sub>O</strong>.</p>
  <table>
    <tr><th>Type</th><th>Meaning</th></tr>
    <tr><td><b>A</b></td><td>Normal middle ear function &mdash; and also typical of <b>sensorineural</b> loss with a normal middle ear</td></tr>
    <tr><td><b>B</b> (flat)</td><td>Restricted mobility. <b>Flat + HIGH canal volume &rarr; perforation or patent tube. Flat + NORMAL volume &rarr; middle-ear effusion.</b></td></tr>
    <tr><td><b>C</b></td><td>Significant negative middle-ear pressure &mdash; eustachian tube dysfunction. <b>Significant for treatment below &minus;200&nbsp;mm H<sub>2</sub>O</b></td></tr>
    <tr><td><b>AS</b></td><td>Normal pressure, <b>reduced</b> mobility &mdash; S for stiff or shallow. Ossicular chain fixation, tympanosclerosis</td></tr>
    <tr><td><b>AD</b></td><td>Normal pressure, <b>hyper</b>mobility &mdash; flaccid membrane from disarticulation</td></tr>
  </table>

  <h3 class="sub" id="l3-imaging">3.7 &middot; Objectives h&ndash;l &mdash; Head and neck imaging, and putting it together</h3>
  <table>
    <tr><th>Computed tomography (with contrast)</th><th>Magnetic resonance imaging</th></tr>
    <tr><td><b>First-line for most acute head and neck infections.</b> Fast, widely available; shows abscess, oedema, gas, bone erosion. Strengths: calcification and bone, sinuses, acute trauma and orbital fractures, foreign bodies, and the <b>unstable or claustrophobic</b> patient.<br><br><b>Think CT for bone, trauma and speed.</b></td>
      <td>Superior soft-tissue contrast, no ionizing radiation. Strengths: intracranial or orbital extension, <b>perineural spread</b>, skull base, tumours.<br><br><b>Think MRI for soft tissue, nerves, and tumour or intracranial extension.</b></td></tr>
  </table>
  <table>
    <tr><th>Presentation</th><th>Study</th></tr>
    <tr><td>Uncomplicated acute rhinosinusitis, otitis, simple soft-tissue infection</td><td><b>No imaging</b></td></tr>
    <tr><td><b>Facial swelling, proptosis, eye signs or neuro signs</b>; complicated sinusitis or orbital cellulitis</td><td><b>Emergency</b> contrast CT of sinuses and orbits</td></tr>
    <tr><td>Deep neck infection</td><td>Contrast CT neck &mdash; <b>ultrasound is not helpful here</b></td></tr>
    <tr><td>Neck mass</td><td><b>Ultrasound first</b> &mdash; superficial or cystic versus solid, size, vascularity</td></tr>
    <tr><td>Deep or malignant lesions</td><td>CT or MRI for staging</td></tr>
    <tr><td>Acoustic neuroma, asymmetric sensorineural loss</td><td><b>MRI with contrast</b></td></tr>
  </table>
  <table>
    <tr><th>CT sinus</th><th>CT orbit</th><th>CT neck</th></tr>
    <tr><td>Mucosal thickening<br>Air-fluid levels<br>Sinus opacification</td>
      <td>Orbital cellulitis with fat stranding<br>Abscess<br>Blowout fracture<br>Herniated orbital contents</td>
      <td>Abscess as a <b>rim-enhancing</b> fluid collection<br>Enlarged or necrotic lymph nodes</td></tr>
  </table>
  <p><strong>Blow-out fracture:</strong> air in the orbit (orbital emphysema), a fracture of the
  orbital floor, and soft tissue extending down into the top of the maxillary sinus.
  <strong>Tripod fracture:</strong> diastasis of the frontozygomatic suture, a fracture of the
  orbital floor with orbital emphysema, and a fracture through the lateral wall of the maxillary
  sinus, which fills with blood.</p>
  <p><strong>Deep neck infection.</strong> Contrast CT of the neck asks three questions:
  <strong>is there a drainable abscess, is the airway compromised, and is it spreading towards the
  mediastinum</strong>. Magnetic resonance adds value for <strong>intracranial extension, vascular
  thrombosis (Lemierre) and osteomyelitis</strong>. Her framing in the lecture, off her own
  peritonsillar abscess story: <i>&ldquo;if you were worried about a deep neck infection, you want
  to know about abscess, you want to know about airway, and you want to know about spread.&rdquo;</i></p>
  <p><strong>The four questions to ask about any test:</strong> what does it evaluate well, when do
  we order it, what are its strengths and limitations, and how do the results confirm the condition.
  She added a fifth in the lecture: <i>&ldquo;what is our next step if it doesn&rsquo;t tell us?&rdquo;</i>
  &mdash; and only then do cost, availability and urgency enter.</p>

  <button type="button" class="test-yourself-btn" style="--acc:{ACC3}" onclick="window.openTestYourself('Test yourself &mdash; Derm, Ophtho &amp; ENT Testing', TEST_YOURSELF.dermentophtho)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>3. svDerm, ENT, Ophtho.pptx</em> (Professor Lauren
  Reynolds, MSPA, PA-C), Slides 1&ndash;44, and the PAJ 5600 syllabus instructional objectives.
  <b>This is the student version of the deck and its licensed figures have been stripped</b> &mdash;
  slides 7, 21, 23, 28, 29, 30, 33 and 38 carry a title and speaker notes but no picture. Where the
  notes describe the missing figure, that description is the source. The 24 August 2026 lecture
  recording (1:29:47) has been folded in and was cross-examined against Notability&rsquo;s
  independent transcript.</footer>
</section>
"""

SEC4_HEAD = """
<section class="deck" id="cbc-hematology">
  <h2 class="deck-title">4 &middot; Complete Blood Count and Hematology Diagnostics</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 4: Complete Blood Count and Hematology Diagnostics</p>
    <ol type="a">
      <li>Explain the components of a complete blood count.</li>
      <li>Explain the difference between hemoglobin and hematocrit.</li>
      <li>Discuss red blood cell indices.</li>
      <li>Calculate absolute white blood cell counts.</li>
      <li>Discuss the clinical significance of abnormalities in: i. Red blood cells &middot; ii. White blood cells &middot; iii. Platelets</li>
      <li>Discuss indications for ordering a complete blood count.</li>
      <li>Compare and contrast laboratory patterns associated with: i. Microcytic anemia &middot; ii. Normocytic anemia &middot; iii. Macrocytic anemia</li>
      <li>Compare and contrast laboratory tests used in the evaluation of anemia</li>
    </ol>
  </div>

  <div class="callout"><b>A great deal of this lecture exists only inside a picture.</b> The
  neutropenia severity table, the four schistocyte types, the fact that Heinz bodies need a special
  stain, the iron comparison table, the whole anemia algorithm, the index formulas and the fishbone
  layout are all <b>figures with no text version in the deck</b>. Slides 31 and 71 extract as
  completely blank. Every one of them is reproduced below. If you revise from a text export of the
  slides you will not have any of it.</div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Watch the reference ranges</span>
  <p><b><mark class="prof-highlight">This deck gives three of its reference ranges two different
  ways.</mark></b> The full reference table (a picture, on slides 7 and 31) does not agree with the
  individual teaching slides:</p>
  <table>
    <tr><th></th><th>Reference table (slides 7, 31)</th><th>Teaching slide</th></tr>
    <tr><td>Lymphocytes</td><td>25&ndash;33%</td><td><b>24&ndash;44%</b> (slide 26)</td></tr>
    <tr><td>Platelets</td><td>150,000&ndash;400,000</td><td><b>150,000&ndash;450,000</b> (slide 30)</td></tr>
    <tr><td>Red cell distribution width</td><td>11&ndash;15%</td><td><b>12&ndash;15%</b> (slide 56)</td></tr>
  </table>
  <p>A fourth set appears on the labelled smear on slide 15 (neutrophil 60&ndash;70%, lymphocyte
  20&ndash;25%, monocyte 3&ndash;8%, eosinophil 2&ndash;4%, basophil 0.5&ndash;1%), which is a
  borrowed textbook graphic and matches neither. <b>No quiz question is built on a disputed
  value.</b> Everything else &mdash; white cells, hemoglobin, hematocrit, all four indices, mean
  platelet volume, neutrophils, eosinophils, monocytes &mdash; agrees across both and is fair game.</p>
  <p><b>The worked example on slide 21 is mis-bracketed.</b> It prints
  <i>ANC = 6,000 &times; (40 + 5/100) = 2,700</i>. That bracketing evaluates to 240,300. The printed
  <b>answer of 2,700 is correct</b> and matches the formula image on slide 20, so it is a
  typographical slip rather than a teaching error. Use
  <b>ANC = WBC &times; (%neutrophils + %bands) &divide; 100</b>.</p>
  </div>
"""

SEC4_BODY = """
  <h3 class="sub" id="l4-components">4.1 &middot; Objectives a &amp; f &mdash; What is on the panel, and which one to order</h3>
  <p>A complete blood count reports on <strong>the hematologic system and other organ systems</strong>.
  It contains the red cell count, hemoglobin, hematocrit, blood smear, platelet count and mean
  platelet volume; the four <strong>red cell indices</strong> (mean corpuscular volume, mean
  corpuscular hemoglobin, mean corpuscular hemoglobin concentration, red cell distribution width);
  and the white cell count with differential.</p>
  <table>
    <tr><th>Without differential</th><th>With differential</th></tr>
    <tr><td>Red cell count &middot; red cell indices &middot; <b>total</b> white cell count &middot; platelets<br><br>
      <b>Order it to screen or monitor</b> for anemia, overall leukocytosis or leukopenia, or thrombocytopenia</td>
      <td>Everything above <b>plus</b> neutrophils, lymphocytes, monocytes, eosinophils, basophils<br><br>
      <b>Order it when the specific white cell line matters</b> &mdash; bacterial infection (neutrophils), viral (lymphocytes), allergy or parasites (eosinophils), hematologic malignancy, autoimmune or inflammatory disease</td></tr>
  </table>
  <p>The deck's warning is practical: <strong>know which one you are clicking</strong>, because the
  two give different values.</p>
@@FIG_TABLE@@
  <h3 class="sub" id="l4-wbc">4.2 &middot; Objective e(ii) &mdash; The white cell lines</h3>
  <p>Normal white cell count is <strong>4,500&ndash;11,000 cells/&micro;L</strong>. Below is
  <strong>leukopenia</strong>, above is <strong>leukocytosis</strong>. White cells fight infection,
  migrate to injury by <strong>chemotaxis</strong>, <strong>phagocytose</strong> foreign organisms,
  and produce and distribute <strong>antibodies</strong>.</p>
  <table>
    <tr><th>Line</th><th>Normal</th><th>Appearance</th><th>Raised by</th><th>Lowered by</th></tr>
    <tr><td><b>Neutrophil</b><br><i>most abundant</i></td><td>54&ndash;62%</td>
      <td>3&ndash;4 lobed nucleus, granular cytoplasm</td>
      <td>Bacterial infection, myocardial infarction, burns, <b>steroids</b>, rheumatoid arthritis, pregnancy/labor/surgery</td>
      <td>Marrow damage, <b>folate and B12 deficiency</b>, radiation, toxic chemicals (benzene), overwhelming infection, viral infection</td></tr>
    <tr><td><b>Bands</b><br><i>immature neutrophils</i></td><td>&le;5%</td>
      <td>1&ndash;2 lobes separated by a <b>thick chromatin band</b></td>
      <td colspan="2"><b>Neutrophils + bands = bacterial infection.</b> A <b>left shift</b> is an increase in immature cells &mdash; neutrophils are consumed faster than the marrow can mature replacements</td></tr>
    <tr><td><b>Eosinophil</b></td><td>1&ndash;3%</td><td>Two-lobed nucleus, granules with <b>histamines</b></td>
      <td>Parasitic infection, allergy, cancer</td><td>Marrow suppression</td></tr>
    <tr><td><b>Basophil</b></td><td>&lt;1%</td><td>Usually two-lobed, granules with <b>heparin</b>, histamine, inflammatory mediators</td>
      <td>Allergy, cancer</td><td>Marrow suppression</td></tr>
    <tr><td><b>Monocyte</b><br><i>largest</i></td><td>3&ndash;7%</td><td>No granules; kidney-shaped nucleus</td>
      <td>Chronic inflammation, stress, viral infection</td><td>Marrow injury</td></tr>
    <tr><td><b>Lymphocyte</b></td><td>see the warning box</td><td>Small, mononuclear, no granules</td>
      <td>Viral infection</td><td>Human immunodeficiency virus, marrow suppression</td></tr>
  </table>
  <p><strong>Steroids raise the neutrophil count by demargination</strong> &mdash; the deck spells
  out the mechanism: they cause neutrophils <em>to detach from the blood vessel wall and enter the
  main bloodstream</em>. And <strong>folate and B12 lower it because both are needed for the marrow
  to function.</strong></p>
  <p><strong>Granulocytes</strong> (neutrophil, eosinophil, basophil) have distinctive cytoplasmic
  granules holding enzymes, proteins and toxic substances. <strong>Agranulocytes</strong> (monocyte,
  lymphocyte) have none, and a non-lobular nucleus. Monocytes differentiate into
  <strong>macrophages or dendritic cells</strong> &mdash; Kupffer cells in the liver, alveolar
  macrophages in the lung, <strong>Langerhans cells in the skin</strong>. Lymphocytes are T cells,
  B cells and natural killer cells, and <strong>the complete blood count does not tell them
  apart</strong>.</p>
@@FIG_WBC@@
  <h3 class="sub" id="l4-anc">4.3 &middot; Objective d &mdash; Absolute counts, and grading neutropenia</h3>
  <p>A percentage means nothing without the total. The general form is
  <strong>absolute count = total white cell count &times; that type's percentage &divide; 100</strong>,
  and it works for every line. For neutrophils there is one twist: <strong>bands count WITH the
  neutrophils</strong>.</p>
@@FIG_ANC@@
  <p><strong>Worked example (the deck's own):</strong> a white cell count of 6,000/&micro;L with 40%
  neutrophils and 5% bands gives 6,000 &times; (40 + 5) &divide; 100 =
  <strong>2,700/&micro;L</strong>. When the count is written in thousands, the equivalent form is
  <strong>10 &times; WBC(thousands) &times; (%neutrophils + %bands)</strong>.</p>
  <p>The number only means something once you can place it in a band &mdash; which is what the next
  figure is for, and it is nowhere in the slide text.</p>
@@FIG_NEUTROPENIA@@
  <h3 class="sub" id="l4-platelets">4.4 &middot; Objective e(iii) &mdash; Platelets</h3>
  <p>Platelets form in the bone marrow from <strong>megakaryocytes</strong>, which break into
  fragments &mdash; so they are <strong>not really cells</strong>. Lifespan
  <strong>7&ndash;10 days</strong>. Primary role is <strong>hemostasis</strong>, defined by the deck
  as stopping the bleeding and repairing damaged vessels; they also contribute to coagulation,
  vascular integrity, inflammation, immune defense, wound healing and thrombosis.</p>
  <table>
    <tr><th></th><th>Raised by</th><th>Lowered by</th></tr>
    <tr><td><b>Platelet count</b></td>
      <td>Trauma, acute hemorrhage, <b>iron deficiency</b>, polycythemia vera</td>
      <td>Marrow suppression &mdash; chemotherapy, alcohol, radiation, aplastic anemia, drugs</td></tr>
    <tr><td><b>Mean platelet volume</b><br>7.5&ndash;12.5 fL</td>
      <td>An increase in <b>immature</b> platelets, as after recent blood loss</td>
      <td>Bone marrow failure</td></tr>
  </table>
  <p><strong>Risk of hemorrhage increases below 20,000.</strong> Note the oddity worth holding:
  <strong>iron deficiency raises platelets while lowering red cells.</strong></p>

  <h3 class="sub" id="l4-indices">4.5 &middot; Objectives b &amp; c &mdash; Hemoglobin, hematocrit and the four indices</h3>
  <p><strong>Hemoglobin</strong> is the amount of hemoglobin in a volume of blood.
  <strong>Hematocrit</strong> is the percentage of that blood which is red cells &mdash; packed cell
  volume. The rule of thumb: <strong>hemoglobin &times; 3 = hematocrit</strong>.</p>
  <p>All three of red cell count, hemoglobin and hematocrit are raised by the same three things
  &mdash; <strong>polycythemia vera, chronic hypoxia</strong> (chronic obstructive pulmonary
  disease, sleep apnea, high altitude) <strong>and dehydration</strong> &mdash; and lowered by blood
  loss, nutritional deficiency, marrow disorders, chronic kidney disease, cancer and dilution.
  Hematocrit adds <strong>smoking and hypoventilation</strong> to the raised list, and
  <strong>hemolysis</strong> to the lowered one.</p>
  <p>The deck is careful about one thing: <strong>the red cell COUNT does not accurately measure
  oxygen carrying capacity and is not directly used to diagnose anemia</strong>, though it is still
  used in evaluating it.</p>
  <table>
    <tr><th>Index</th><th>What it is</th><th>Normal</th><th>Formula</th></tr>
    <tr><td><b>MCV</b></td><td>Average red cell <b>volume</b> &mdash; measured</td><td>80&ndash;100 fL</td><td>Hct(%) &times; 10 &divide; RBC (million/&micro;L)</td></tr>
    <tr><td><b>MCH</b></td><td>Average hemoglobin in a <b>single cell</b> &mdash; calculated</td><td>27&ndash;33 pg/cell</td><td>Hgb(g/dL) &times; 10 &divide; RBC (million/&micro;L)</td></tr>
    <tr><td><b>MCHC</b></td><td>Average hemoglobin <b>concentration</b> in packed cells &mdash; calculated</td><td>32&ndash;36 g/dL</td><td>Hgb(g/dL) &times; 100 &divide; Hct(%)</td></tr>
    <tr><td><b>RDW</b></td><td>Degree of <b>anisocytosis</b>, the variation in size</td><td>see the warning box</td><td>&mdash;</td></tr>
  </table>
  <p><strong>MCH and MCHC differ only in their denominator</strong> &mdash; the red cell count versus
  the hematocrit &mdash; and that is the whole difference between &ldquo;per cell&rdquo; and
  &ldquo;per volume&rdquo;. <strong>MCHC is the automated screening flag for hereditary
  spherocytosis</strong> and other hyperchromic or dehydrated red cell states.</p>
  <p>Hypochromic cells have <strong>central pallor greater than one third of the cell diameter</strong>
  (MCH &lt;27, MCHC &lt;32); normochromic is exactly one third; hyperchromic is a deeper red with
  MCH &gt;33 and MCHC &gt;36, seen in <strong>spherocytes</strong>.</p>

  <h3 class="sub" id="l4-morphology">4.6 &middot; Objective e(i) &mdash; Red cell morphology</h3>
  <p>The deck sorts morphology four ways: <strong>size, hemoglobin distribution, shape variation
  (poikilocytosis) and inclusions with cell distribution</strong>. Start with size, because that is
  also where the anemia algorithm starts.</p>
@@FIG_SIZE@@
  <p><b>The two spiky cells are the pair people confuse, so learn them against each other.</b></p>
@@FIG_SPIKY@@
  <p><strong>Acanthocyte:</strong> irregular spikes, no central pallor, <strong>liver disease</strong>
  &mdash; from abnormal lipid metabolism or membrane change. <strong>Echinocyte:</strong> regularly
  spaced blunter projections right around the cell, <strong>central pallor preserved</strong>,
  <strong>renal disease</strong>.</p>
@@FIG_FRAG@@
  <p><strong>Schistocytes</strong> are fragments &mdash; helmet, horn, triangular and microspherocyte
  forms &mdash; usually microcytic and lacking central pallor. Hemolysis, mechanical trauma
  (mechanical heart valves), medications (cyclosporine). <mark class="prof-highlight">Automated
  counters may count them as platelets</mark>, which can make a platelet count look falsely
  reassuring. <strong>Sickled cells (drepanocytes)</strong> are thin crescents with no central pallor
  and dense hemoglobin, formed <strong>under low oxygen tension</strong>.</p>
@@FIG_ROUND@@
  <p><strong>Spherocyte:</strong> perfectly round, <strong>central pallor lost</strong>, often
  smaller than normal &mdash; hereditary spherocytosis. <strong>Target cell (codocyte):</strong> a
  dark circle inside the central pallor, from <strong>redundant cell membrane</strong> &mdash; post
  splenectomy and liver disease. <strong>Teardrop cell (dacrocyte):</strong> formed in marrow
  infiltrated by scar tissue or tumour &mdash; <strong>bone marrow disease</strong>.</p>
@@FIG_INCL@@
  <p><strong>Basophilic stippling</strong> is ribosomal RNA in blue-black dots <strong>spread evenly
  through the cytoplasm</strong> &mdash; <strong>lead poisoning</strong>. A <strong>Howell-Jolly
  body</strong> is a <em>single</em> dark purple residual nuclear fragment; the spleen normally
  removes them, so finding one means <strong>splenic dysfunction or asplenia</strong> &mdash; which
  is why target cells turn up in the same field.</p>
  <p><mark class="prof-highlight">Heinz bodies are the easiest thing in this lecture to miss.</mark>
  Denatured hemoglobin at the cell <strong>periphery</strong>, in <strong>G6PD deficiency</strong>
  &mdash; and they require a <strong>supravital stain (new methylene blue)</strong>. They are
  <strong>invisible on the routine Wright stain</strong> used for the rest of the differential, so
  nobody will report them unless you ask.</p>
@@FIG_DIST@@
  <p><strong>Rouleaux</strong> is stacking like rows of coins, because <strong>raised serum proteins
  neutralise the negative surface charge</strong> that normally keeps red cells apart &mdash;
  multiple myeloma, liver disease. <strong>Agglutination</strong> is disorderly clumping from
  <strong>antibodies bridging</strong> the cells &mdash; transfusion reactions. Different pattern,
  different mechanism, different diagnosis.</p>

  <h3 class="sub" id="l4-anemia">4.7 &middot; Objectives g &amp; h &mdash; Working up an anemia</h3>
  <p>Four steps, and the notes say to do them <strong>simultaneously</strong>: assess the clinical
  presentation; check the complete blood count and chemistry panel; <strong>determine the mean
  corpuscular volume</strong>; check the <strong>reticulocyte count</strong>. Look at the peripheral
  smear if you can get one. <strong>A decreased reticulocyte count means underproduction; an
  increased one suggests hemolysis or blood loss</strong> &mdash; and the count is most useful when
  it is very high or very low.</p>
  <table>
    <tr><th>Microcytic &lt;80 fL</th><th>Normocytic 80&ndash;100 fL</th><th>Macrocytic &gt;100 fL</th></tr>
    <tr><td><b>Iron deficiency</b> (most common cause of anemia &mdash; <b>evaluate for occult blood loss</b>, often the first sign of gastrointestinal bleeding)<br>Lead poisoning<br>Anemia of chronic disease<br>Thalassemia<br>Sideroblastic anemia</td>
      <td><b>Hypo-proliferative:</b> aplastic anemia, anemia of chronic disease, marrow infiltration by tumor, hypometabolic states<br><br>
      <b>Hemolysis or hemorrhage:</b> acute blood loss (<b>hemoglobin and hematocrit start to fall within 2&ndash;3 days</b>), intrinsic and extrinsic hemolytic anemia, sickle cell anemia</td>
      <td><b>Megaloblastic:</b> B12, folate, drugs impairing DNA synthesis (methotrexate, antiretrovirals, hydroxyurea), copper deficiency<br><br>
      <b>Non-megaloblastic:</b> alcohol, liver disease, hypothyroidism, reticulocytosis, primary marrow disorders, chronic kidney disease</td></tr>
  </table>
  <p><strong>Intrinsic hemolysis</strong> is a defect <em>in</em> the red cell causing premature
  splenic removal; <strong>extrinsic</strong> is mechanical stress, immunologic destruction or
  inflammatory injury from <em>outside</em>. <strong>Macroovalocytes and hypersegmented
  neutrophils</strong> are what mark a macrocytic anemia as megaloblastic; without them, think
  chronic liver disease or acute hematologic malignancy.</p>
  <table>
    <tr><th>Pattern</th><th>Ferritin</th><th>Serum iron</th><th>Total iron binding capacity</th></tr>
    <tr><td><b>Iron deficiency</b></td><td>&darr;</td><td>&darr;</td><td>&uarr;</td></tr>
    <tr><td><b>Anemia of chronic disease</b></td><td>&uarr;</td><td>&darr;</td><td>&darr;</td></tr>
    <tr><td><b>Normal all three</b></td><td colspan="3">&rarr; basophilic stippling? <b>Yes</b> &rarr; serum lead. <b>No</b> &rarr; thalassemia trait</td></tr>
  </table>
@@FIG_IRON@@
  <p>The iron transport analogy on the hand-drawn slide is worth keeping: the <strong>bus is
  transferrin</strong> (carries iron), the <strong>bus stop is ferritin</strong> (stores it, and can
  be measured because it sits outside the marrow), the <strong>home is hemosiderin</strong> (storage
  that cannot be measured), <strong>percentage saturation is total iron binding capacity</strong>
  (how many can sit on the bus), and the <strong>school is the red blood cell</strong>.</p>
@@FIG_ALGO@@
  <p>Two things in that algorithm are easy to walk past. <strong>Iron deficiency appears in BOTH the
  microcytic and the normocytic branches</strong>, which is why iron studies get obtained even when
  cell size is normal. And in the microcytic branch you obtain iron studies <strong>in all
  individuals</strong>, because a concomitant iron deficiency can affect hemoglobin analysis and
  hide a thalassemia.</p>
  <p>In the normocytic branch, the reticulocyte count splits it three ways: <strong>high
  retics</strong> &rarr; hemolysis, sickle cell, acute hemorrhage. <strong>Low retics with low white
  cells or platelets</strong> &rarr; leukemia, metastatic malignancy, aplastic anemia. <strong>Low
  retics with normal or high white cells and platelets</strong> &rarr; chronic infection or
  inflammation, malignancy, chronic renal disease, endocrine dysfunction.</p>
@@FIG_FISH@@

  <button type="button" class="test-yourself-btn" style="--acc:{ACC4}" onclick="window.openTestYourself('Test yourself &mdash; Complete Blood Count', TEST_YOURSELF.cbchematology)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>Complete Blood Count and Hematology Diagnostics -
  Shahsv.pptx</em> (Professor Chand Shah, MPAS, PA-C), Slides 1&ndash;75, and the PAJ 5600 syllabus
  instructional objectives. Figures are reproduced from the lecture slides and each is cited to its
  slide; six of them are the only source for their content anywhere in the deck. <b>No lecture
  recording exists for this topic yet</b> &mdash; everything here is from the slides, and where the
  deck states a value two different ways both are shown rather than one being chosen silently.</footer>
</section>
"""

FIGS = {
 "@@FIG_TABLE@@": [("cbc-reference-table", "<b>The complete reference table &mdash; a picture, not text.</b> The three rows flagged in the box above are the ones that disagree with the teaching slides.", 7)],
 "@@FIG_WBC@@": [("wbc-morphology", "<b>Read the nucleus first, then the granules.</b> Neutrophil multilobed; eosinophil and basophil bilobed with red and purplish-black granules; lymphocyte a single sphere with a thin blue rim; monocyte kidney-shaped.", 10),
                 ("granulocyte-lifespans", "<b>Lifespans, image-only.</b> The neutrophil's <b>seven hours</b> is why the marrow must release continuously &mdash; and why an acute infection forces out bands.", 16),
                 ("agranulocyte-lifespans", "Hours to days for granulocytes against <b>years</b> for lymphocyte memory cells.", 17)],
 "@@FIG_ANC@@": [("anc-formula", "<b>The formula exists only as this image.</b> Bands are counted <b>with</b> the neutrophils.", 20)],
 "@@FIG_NEUTROPENIA@@": [("neutropenia-grades", "<b>Not in the slide text at all.</b> <b>Severe is under 500</b>, and that is the number that changes management.", 21)],
 "@@FIG_SIZE@@": [("mcv-sizes", "<b>Hemoglobin says there is an anemia; mean corpuscular volume says which algorithm to run.</b>", 34)],
 "@@FIG_SPIKY@@": [("acanthocytes", "<b>Acanthocyte &mdash; irregular spikes, no central pallor. Liver disease.</b>", 36),
                   ("echinocytes", "<b>Echinocyte &mdash; regular blunt projections, central pallor kept. Renal disease.</b>", 37)],
 "@@FIG_FRAG@@": [("schistocyte-types", "<b>Four named forms &mdash; and the slide text names only two.</b> Triangular cell and microspherocyte exist only here.", 39),
                  ("schistocytes-smear", "Small, irregular, no central pallor &mdash; small enough that <b>counters may report them as platelets</b>.", 39),
                  ("sickle-cells", "<b>Drepanocytes.</b> Thin crescents, no central pallor, dense hemoglobin.", 41)],
 "@@FIG_ROUND@@": [("spherocytes", "<b>Spherocytes &mdash; round, pallor gone, often small.</b> The cells behind the MCHC screening flag.", 42),
                   ("target-cells", "<b>Target cell &mdash; bullseye from redundant membrane.</b> Splenectomy, liver disease.", 43),
                   ("teardrop-cells", "<b>Dacrocytes.</b> The shape records the infiltrated marrow they were squeezed out of.", 44)],
 "@@FIG_INCL@@": [("basophilic-stippling", "<b>Evenly distributed</b> blue-black dots of ribosomal RNA &mdash; lead poisoning.", 45),
                  ("howell-jolly", "<b>A single</b> nuclear remnant (blue circle), with target cells (pink box) in the same field &mdash; both mean the spleen is gone.", 46),
                  ("heinz-bodies", "<b>Needs a supravital stain &mdash; invisible on a routine Wright stain.</b> G6PD deficiency.", 47)],
 "@@FIG_DIST@@": [("rouleaux", "<b>Rows of coins.</b> Raised serum proteins cancel the charge that keeps cells apart.", 48)],
 "@@FIG_IRON@@": [("iron-comparison", "<b>The highest-yield table in the lecture, and the slide's only text is its title.</b> Iron deficiency: LOW ferritin, HIGH binding capacity. Inflammatory anaemia: the reverse.", 63)],
 "@@FIG_ALGO@@": [("anemia-algorithm", "<b>Slide 71 extracts as completely blank &mdash; this figure is the entire slide.</b>", 71)],
 "@@FIG_FISH@@": [("fishbone", "<b>White cells left, hemoglobin above the line, hematocrit below, platelets right.</b> You will see this written long before you see it typed.", 72)],
}

TOC = """  <a class="top-link" href="#derm-ent-ophtho">3 &middot; Diagnostic Testing for Derm, Ophtho &amp; ENT</a>
  <a href="#l3-approach">3.1 Objective a &mdash; Ask the question first</a>
  <a href="#l3-koh">3.2 Objectives a &amp; c &mdash; Bedside microscopy &amp; KOH</a>
  <a href="#l3-biopsy">3.3 Objectives d &amp; e &mdash; Biopsy &amp; soft tissue infection</a>
  <a href="#l3-cultures">3.4 Objective b &mdash; Skin &amp; wound cultures</a>
  <a href="#l3-eye">3.5 Objective f &mdash; The four ophthalmic tests</a>
  <a href="#l3-ent">3.6 Objective g &mdash; Throat, hearing &amp; the middle ear</a>
  <a href="#l3-imaging">3.7 Objectives h&ndash;l &mdash; Head &amp; neck imaging</a>
  <a class="top-link" href="#cbc-hematology">4 &middot; Complete Blood Count &amp; Hematology</a>
  <a href="#l4-components">4.1 Objectives a &amp; f &mdash; The panel, and which to order</a>
  <a href="#l4-wbc">4.2 Objective e(ii) &mdash; The white cell lines</a>
  <a href="#l4-anc">4.3 Objective d &mdash; Absolute counts &amp; neutropenia</a>
  <a href="#l4-platelets">4.4 Objective e(iii) &mdash; Platelets</a>
  <a href="#l4-indices">4.5 Objectives b &amp; c &mdash; Hemoglobin, hematocrit &amp; indices</a>
  <a href="#l4-morphology">4.6 Objective e(i) &mdash; Red cell morphology</a>
  <a href="#l4-anemia">4.7 Objectives g &amp; h &mdash; Working up an anemia</a>
"""

TY = '''    dermentophtho: [
      {q:"A potassium hydroxide preparation shows pseudohyphae together with budding yeast. What is it?",
       choices:["Candida","A dermatophyte","Tinea versicolor","A negative result"],correct:0,
       expl:"Branching septate hyphae are a dermatophyte; the spaghetti-and-meatballs pattern is tinea versicolor. The COMBINATION of pseudohyphae and budding yeast is Candida."},
      {q:"Melanoma is on your differential. Which biopsy?",
       choices:["Narrow excisional, 1-3 mm margins, below the base","Punch biopsy for a full-thickness sample","Shave biopsy of the raised portion","Incisional biopsy of the darkest quadrant"],correct:0,
       expl:"She said this three times in two minutes. The depth matters because a transected base destroys Breslow depth, the single most important prognostic measurement. Note 1-3 MILLIMETRES for the diagnostic biopsy, not the centimetres used for re-excision."},
      {q:"Which triad must be screened for necrotizing infection?",
       choices:["Hypotension, white cell count 15,000 or more, violaceous skin","Fever, purulent drainage, spreading erythema","Pain out of proportion, tachycardia, bullae","Hypotension, low white cell count, cobblestoning"],correct:0,
       expl:"The one thing she bolded in red on the slide and then flagged out loud: a patient who looks too sick for a skin infection."},
      {q:"A tympanogram is flat with a HIGH canal volume. What does that mean?",
       choices:["Perforation or a patent tube","Middle-ear effusion","Eustachian tube dysfunction","Ossicular fixation"],correct:0,
       expl:"Flat plus high volume means the canal is continuous with the middle ear. Flat plus NORMAL volume is an effusion. That one number separates the two."},
      {q:"Reduced acuity corrects with a pinhole. What does that indicate?",
       choices:["A refractive error","Optic nerve disease","A corneal ulcer","Acute angle-closure glaucoma"],correct:0,
       expl:"The pinhole blocks peripheral light and focuses central rays on the retina. If that fixes it, the problem was refraction. If it does not correct or worsens, suspect eye pathology."},
      {q:"Which imaging is FIRST for a deep neck infection?",
       choices:["Contrast CT of the neck","Ultrasound of the neck","MRI with contrast","Plain radiography"],correct:0,
       expl:"The deck says ultrasound is NOT helpful here, which is the opposite of the neck MASS pathway where ultrasound is first-line. CT answers three questions: drainable abscess, airway, spread to mediastinum."},
      {q:"Fluorescein shows branching, dendritic staining. What is it?",
       choices:["Herpetic keratitis","A corneal abrasion","A corneal ulcer","A normal cornea"],correct:0,
       expl:"Linear is an abrasion; fixed dense staining or an opacity is an ulcer and needs urgent referral. The dendrite is herpetic."},
      {q:"A negative rapid strep test in a CHILD. What next?",
       choices:["Confirm with a throat culture","Treat empirically for group A strep","Repeat the rapid test tomorrow","Send antistreptococcal antibody titres"],correct:0,
       expl:"Rapid antigen sensitivity is only 70-90%. Confirmation is for children; it is not routinely required in adults. And never use ASO titres for acute pharyngitis."}
    ],
    cbchematology: [
      {q:"White cell count 6,000/uL with 40% neutrophils and 5% bands. What is the ANC?",
       choices:["2,700/uL","2,400/uL","300/uL","270/uL"],correct:0,
       expl:"6,000 x (40 + 5) / 100 = 2,700. The trap is leaving the bands out, which gives 2,400. Bands count WITH the neutrophils."},
      {q:"An absolute neutrophil count of 400/uL is which grade of neutropenia?",
       choices:["Severe","Moderate","Mild","Normal"],correct:0,
       expl:"Severe is under 500, moderate 500 to under 1,000, mild 1,000 to under 1,500. This table is on the slide only as a picture."},
      {q:"Ferritin is HIGH, serum iron LOW, total iron binding capacity LOW. Which anemia?",
       choices:["Anemia of chronic disease","Iron deficiency","Thalassemia trait","Sideroblastic anemia"],correct:0,
       expl:"Ferritin is an acute phase reactant, so it rises in inflammation even though the iron is unavailable. Iron deficiency is the mirror image: LOW ferritin, HIGH binding capacity."},
      {q:"Which stain is required to see Heinz bodies?",
       choices:["A supravital stain such as new methylene blue","The routine Wright stain","An iron stain","A Gram stain"],correct:0,
       expl:"The most easily missed fact in the lecture, and it only appears inside a figure. Heinz bodies are invisible on the routine stain, so nobody reports them unless you ask."},
      {q:"Irregular spikes and no central pallor. Which cell, and which disease?",
       choices:["Acanthocyte - liver disease","Echinocyte - renal disease","Schistocyte - hemolysis","Spherocyte - hereditary spherocytosis"],correct:0,
       expl:"The echinocyte has REGULARLY spaced blunter projections and KEEPS its central pallor, and goes with renal disease. Two features separate them."},
      {q:"Blue-black dots spread evenly through the red cell cytoplasm. What is it?",
       choices:["Basophilic stippling - lead poisoning","A Howell-Jolly body - splenectomy","Heinz bodies - G6PD deficiency","Rouleaux - multiple myeloma"],correct:0,
       expl:"Evenly distributed is the discriminator. A Howell-Jolly body is a SINGLE dark purple nuclear remnant."},
      {q:"Why do steroids raise the neutrophil count?",
       choices:["Neutrophils detach from the vessel wall into the bloodstream","The marrow produces more neutrophils","Neutrophil survival is prolonged","Migration into tissue is blocked"],correct:0,
       expl:"Demargination. The deck spells the mechanism out rather than just asserting the association."},
      {q:"A normocytic anemia with LOW reticulocytes and LOW platelets. Which group?",
       choices:["Leukemia, metastatic malignancy, aplastic anemia","Hemolysis, sickle cell, acute hemorrhage","Chronic infection, renal disease, endocrine dysfunction","Iron deficiency and thalassemia"],correct:0,
       expl:"Other cell lines being down points at the marrow itself. Low retics with NORMAL or HIGH white cells and platelets points outside the marrow instead."},
      {q:"What is the difference between MCH and MCHC?",
       choices:["MCH divides by the red cell count; MCHC divides by the hematocrit","MCH divides by hematocrit; MCHC by the red cell count","MCH is measured; MCHC is calculated","They are the same in different units"],correct:0,
       expl:"Same numerator, different denominator - and that is the whole difference between 'per cell' and 'per volume'. MCHC is the automated flag for hereditary spherocytosis."},
      {q:"Which value appears in BOTH the microcytic and the normocytic branch of the anemia algorithm?",
       choices:["Iron deficiency","Thalassemia","Hypothyroidism","Myelodysplastic syndrome"],correct:0,
       expl:"That is exactly why iron studies get obtained even when the mean corpuscular volume is normal."}
    ],
'''


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for o, c in (("<!--PDML3-->", "<!--/PDML3-->"), ("<!--PDML4-->", "<!--/PDML4-->"),
                 ("<!--PDMTOC34-->", "<!--/PDMTOC34-->"), ("<!--PDMTY34-->", "<!--/PDMTY34-->")):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(c), "", src, flags=re.S)

    body4 = SEC4_HEAD + SEC4_BODY
    for token, items in FIGS.items():
        assert token in body4, "figure token %s unused" % token
        body4 = body4.replace(token, "\n".join(fig(s, cap, sl) for s, cap, sl in items))
    assert "@@" not in body4, "unfilled figure token"
    sec3 = SEC3.replace("{ACC3}", ACC3)
    body4 = body4.replace("{ACC4}", ACC4)

    # sections go at the end of <main>, after Lecture 2
    end = src.index("</main>")
    src = (src[:end] + "<!--PDML3-->" + sec3 + "<!--/PDML3-->\n"
           + "<!--PDML4-->" + body4 + "<!--/PDML4-->\n\n" + src[end:])

    # table of contents, before the closing of the nav rail
    anchor = '  <a class="top-link" href="#medical-imaging"'
    assert src.count(anchor) == 1, "medical-imaging top-link not found once"
    i = src.index(anchor)
    j = src.index('<a class="top-link"', i + 10) if '<a class="top-link"' in src[i+10:] else None
    # insert after the whole Lecture 2 block of links: find the end of that <nav>
    navend = src.index("</nav>", i)
    src = src[:navend] + "<!--PDMTOC34-->\n" + TOC + "<!--/PDMTOC34-->\n" + src[navend:]

    # Test-yourself question sets
    tyanchor = "  var TEST_YOURSELF = {\n"
    assert src.count(tyanchor) == 1, "TEST_YOURSELF object not found once"
    src = src.replace(tyanchor, tyanchor + "<!--PDMTY34-->\n" + TY + "<!--/PDMTY34-->\n", 1)

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "li", "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added sections 3 and 4: %d subsections, %d photographs, %d test-yourself questions"
          % (len(re.findall(r'<h3 class="sub" id="l[34]-', src)),
             len(re.findall(r'src="pdm-exam-1-l4-images/', src)),
             TY.count("{q:")))


if __name__ == "__main__":
    main()
