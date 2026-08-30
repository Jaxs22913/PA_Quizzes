# -*- coding: utf-8 -*-
"""Section 3 of the CMS I Exam 2 guide -- Acute Vision Loss (Lecture 12).

Objectives VERBATIM from the CMS syllabus, page 9. Emphasis marks come from
the 2026-08-27 lecture recording.

Giant cell arteritis appears only as the cause of arteritic AION: Jaquith said
in lecture, "I'm not going to test you on GCA directly, I promise you -- but
it's kind of hard when I know GCA is what's causing this not to explain GCA."
"""
IMG = "cms-ophtho-chart-images/l12-"

SECTION = """
<section class="deck" id="acute-vision-loss">
  <h2 class="deck-title">3 &middot; Acute Vision Loss</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">OPHTHALMOLOGY &mdash; Acute Vision Loss</p>
    <ol type="a">
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis of the following
      acute vision loss disorders:
        <ol>
          <li>Amaurosis fugax</li><li>Acute angle closure glaucoma</li><li>Optic neuritis</li>
          <li>Retinal detachment</li>
          <li>Retinal vascular occlusion: a. Central retinal artery occlusion (CRAO) &middot;
          b. Branch retinal artery occlusion (BRAO) &middot; c. Central retinal vein occlusion
          (CRVO) &middot; d. Branch retinal vein occlusion (BRVO)</li>
          <li>Anterior ischemic optic neuropathy (AION): a. Arteritic AION, associated with Giant
          cell (temporal) arteritis &middot; b. Non-arteritic AION</li>
        </ol>
      </li>
      <li>Identify medical care strategies for acute vision loss in the lecture topic list for the
      following populations: 1. adult &middot; 2. elderly</li>
    </ol>
  </div>

  <div class="prof-flag">
    <span class="prof-flag-label">&#9733; Said twice, and named a future examiner</span>
    <p><mark class="prof-highlight">Every single person who has sudden acute vision loss is having
    a stroke until proven otherwise.</mark> That is why <b>everyone gets an MRA</b>, even with no
    weakness, no numbness and no speech difficulty &mdash; because you can have a stroke with
    <em>no other symptom</em> than acute vision loss. She repeated the sentence and added that
    Professor Alaya will ask this question when you reach the emergency department rotation.</p>
  </div>

  <h3 class="sub" id="e2l3-approach">3.1 &middot; The four questions that separate these diagnoses</h3>
  <p>Jaquith opened the lecture by telling the class which details to highlight, because these
  conditions overlap heavily and <strong>the discriminating information is in the history rather
  than the fundus</strong>:</p>
  <table class="tbl">
    <tr><th>Ask</th><th>Answer</th><th>Points toward</th></tr>
    <tr><td rowspan="2"><b>One eye or both?</b></td><td>One</td><td>Nearly all of them &mdash; amaurosis fugax, occlusions, detachment, optic neuritis, AION</td></tr>
    <tr><td>Both</td><td><b>Papilledema</b>, or a lesion at or behind the chiasm</td></tr>
    <tr><td rowspan="3"><b>Sudden or gradual?</b></td><td><b>Seconds</b>, then recovers</td><td><b>Amaurosis fugax</b></td></tr>
    <tr><td><b>Seconds</b>, and stays</td><td><b>CRAO</b></td></tr>
    <tr><td><b>Hours to days</b></td><td><b>Optic neuritis</b> (and detachment advances over days)</td></tr>
    <tr><td rowspan="2"><b>Central or peripheral?</b></td><td>Peripheral first, central preserved</td><td><b>Chronic open-angle glaucoma</b> &mdash; &ldquo;tunnel vision&rdquo;</td></tr>
    <tr><td>Central, with colour desaturation</td><td><b>Optic neuritis</b></td></tr>
    <tr><td rowspan="2"><b>Painful or painless?</b></td><td><b>PAINFUL</b></td><td><b>Acute angle-closure glaucoma</b> (severe, at rest), or <b>optic neuritis</b> (on eye movement)</td></tr>
    <tr><td><b>PAINLESS</b></td><td>Everything else &mdash; amaurosis fugax, all four occlusions, detachment, AION, papilledema</td></tr>
  </table>
  <div class="callout warn">
    <p><strong>The word &ldquo;curtain&rdquo; belongs to TWO diagnoses.</strong> Jaquith flagged
    this explicitly: <em>&ldquo;there's a couple of conditions where they use the word curtain, so
    don't confuse it.&rdquo;</em> <b>Amaurosis fugax</b> &mdash; the curtain comes down and then
    <b>lifts within seconds to minutes</b>. <b>Retinal detachment</b> &mdash; the curtain comes
    down and <b>stays, advancing over days</b>. Duration is the discriminator, not the word.</p>
  </div>

  <h3 class="sub" id="e2l3-amaurosis">3.2 &middot; Amaurosis fugax <span class="cite">Objective a1</span></h3>
  <p><strong>Transient monocular vision loss</strong>, also called <b>&ldquo;fleeting
  blindness&rdquo;</b>. Lasts <b>a few seconds to minutes</b>. It can involve both eyes but is
  <b>usually one</b>.</p>
  <div class="callout">
    <p><strong>If it lasted hours, it was not a transient ischemic attack.</strong> The lecturer
    was explicit. Duration is the first filter you apply.</p>
  </div>
  <table class="tbl">
    <tr><th>Facet</th><th>Content</th></tr>
    <tr><td><b>Etiology</b></td><td>Retinal emboli of <b>carotid (TIA) or cardiac</b> origin; also <b>retinal vascular spasm</b>. <b>Most commonly a TIA.</b></td></tr>
    <tr><td><b>Risk factors</b></td><td>Older age, <b>diabetes, hypertension, atherosclerosis</b>, cardiac valve disease, intravenous drug use, <b>sickle cell</b>, coagulation disorders, <b>Raynaud's</b></td></tr>
    <tr><td><b>Manifestations</b></td><td>A <b>&ldquo;curtain&rdquo; coming down</b>, transient. Anything from mild blurring or fogging to <b>complete blackness</b>. May involve part or all of the field &mdash; upper or lower half, temporal or nasal, small central or paracentral areas, or the whole field. <b>Painless.</b></td></tr>
    <tr><td><b>Diagnosis</b></td><td><b>Carotid Doppler</b> if a carotid source is suspected. <b>Echocardiogram</b> if cardiac. <b>MRA</b> to evaluate all the arteries for emboli &mdash; and per the flag above, everyone gets it.</td></tr>
    <tr><td><b>Treatment</b></td><td><b>Treat the underlying cause</b> &mdash; she called this the essential point. To reduce stroke risk: <b>aspirin and clopidogrel</b>. Carotid emboli &rarr; <b>carotid endarterectomy</b>. Raynaud's or vascular spasm &rarr; <b>calcium channel blockers</b>.</td></tr>
    <tr><td><b>Prognosis</b></td><td><b>About 85% recover fully</b>; the rest <b>progress to a central retinal artery occlusion</b>. Early evaluation reduces the risk of permanent visual loss.</td></tr>
    <tr><td><b>Education</b></td><td>A TIA is a <b>major warning sign that a stroke is coming</b>. Transient does not mean benign.</td></tr>
  </table>

  <h3 class="sub" id="e2l3-glaucoma">3.3 &middot; Glaucoma &mdash; acute closed-angle and chronic open-angle <span class="cite">Objective a2</span></h3>
  <figure class="fig"><img src="%(IMG)ss012_1.png" loading="lazy" alt="Cross-sections contrasting the open drainage angle with the closed one."><figcaption>Both forms raise intraocular pressure. In <b>open-angle</b> the angle is patent but the trabecular meshwork drains poorly; in <b>angle-closure</b> the iris mechanically shuts the circuit. <span class="cite">Slide 12</span></figcaption></figure>
  <table class="tbl">
    <tr><th></th><th>ACUTE &mdash; closed angle</th><th>CHRONIC &mdash; open angle</th></tr>
    <tr><td><b>Mechanism</b></td><td>The <b>iris blocks the drainage circuit</b> &rarr; intraocular pressure rises dramatically</td><td><b>Trabecular meshwork abnormality</b> next to the canal of Schlemm, secondary to <b>aging</b> &rarr; optic nerve damage, <b>with or without raised pressure</b></td></tr>
    <tr><td><b>Frequency</b></td><td>Less common</td><td><b>MUCH more common</b></td></tr>
    <tr><td><b>Pain</b></td><td><b>Severe and sudden eye pain</b></td><td><b>Painless</b></td></tr>
    <tr><td><b>Symptoms</b></td><td>Decreased vision, <b>coloured halos around lights</b>, headache, <b>nausea and vomiting</b></td><td><b>Asymptomatic in most patients.</b> Peripheral field goes first &mdash; patients say <b>&ldquo;tunnel vision&rdquo;</b> &mdash; then complete blindness</td></tr>
    <tr><td><b>Signs</b></td><td>Pupillary dilation, <b>hazy cornea</b>, bilateral narrow or occluded angle</td><td><b>Optic nerve cupping</b>, rim pitting, <b>bayoneting</b> (vessels with narrow angulations), splinter haemorrhages, rim thinning, field defects</td></tr>
    <tr><td><b>Pressure</b></td><td><b>40&ndash;80 mmHg</b> on tonometry or gonioscopy</td><td><b>May be normal OR elevated</b></td></tr>
    <tr><td><b>Other risks</b></td><td><b>Systemic anticholinergics</b> (atropine), <b>nebulized bronchodilators</b>, prior anterior uveitis, lens dislocation, <b>African American race</b>, obstruction from tumour or scarring</td><td><b>African American race</b>, Hispanic ethnicity, <b>adults over 40</b>, diabetes, age, family history, hypertension, myopia</td></tr>
    <tr><td><b>First-line</b></td><td>Topical <b>pilocarpine</b> (alpha-blocker) or <b>timolol</b> (beta-blocker); <b>IV acetazolamide</b> then mannitol or isosorbide</td><td><b>Latanoprost, tafluprost, timolol drops</b></td></tr>
    <tr><td><b>Definitive</b></td><td><b>Laser peripheral iridotomy</b>, <b>1&ndash;2 days after onset</b> &mdash; lets fluid pass from the posterior to the anterior chamber</td><td><b>Laser trabeculoplasty</b> if refractory or advanced. <b>Surgery is definitive for both forms.</b></td></tr>
  </table>
  <figure class="fig"><img src="%(IMG)ss019_1.jpg" loading="lazy" alt="Two fundus photographs: a healthy optic nerve beside a glaucomatous one with a widened cup."><figcaption><b>Optic nerve cupping</b> &mdash; the widening and deepening of the central cup as nerve fibres are lost. The lecturer called it <b>the classic sign</b>, and the one a non-ophthalmologist can actually see. <span class="cite">Slide 19</span></figcaption></figure>
  <div class="prof-flag">
    <span class="prof-flag-label">&#9733; The case she told twice</span>
    <p>A patient went to the emergency department with an <b>intractable headache</b> &mdash;
    everything had been tried, nothing worked &mdash; and was admitted. After multiple doctors, a
    PA assessed him properly, found a <b>red eye</b>, and diagnosed <b>glaucoma</b>. <strong>The
    chief complaint was a headache, and it was localised behind the eye.</strong> Glaucoma is also
    <b>a leading cause of blindness worldwide</b>, and untreated it ends in blindness.</p>
  </div>
  <p><strong>Patient education, and she meant it personally:</strong> everyone should have
  <b>annual eye examinations</b> &mdash; that screening is what finds asymptomatic chronic
  open-angle disease before the field is gone. Some patients stay on <b>drops for life</b> and
  never have surgery, when the surgical risk outweighs the benefit over their life expectancy.</p>

  <h3 class="sub" id="e2l3-neuritis">3.4 &middot; Optic neuritis <span class="cite">Objective a3</span></h3>
  <table class="tbl">
    <tr><th>Facet</th><th>Content</th></tr>
    <tr><td><b>Epidemiology</b></td><td><b>18 to 45 years old, 75% female</b> &mdash; a much younger group than everything else in this lecture</td></tr>
    <tr><td><b>Etiology</b></td><td>Inflammation due to <b>multiple sclerosis</b>, autoimmune disorders, <b>postviral</b>, or idiopathic</td></tr>
    <tr><td><b>Symptoms</b></td><td><b>Unilateral</b> vision loss over <b>hours to several days</b>, with <b>PAINFUL EYE MOVEMENT</b>. Often central vision loss and <b>loss of colour vision</b></td></tr>
    <tr><td><b>Signs</b></td><td>Often a <b>normal-appearing disc</b>. <b>Relative afferent pupillary defect (Marcus Gunn)</b></td></tr>
    <tr><td><b>Diagnosis</b></td><td><b>Refer to ophthalmology.</b> Complete ophthalmic exam &mdash; slit lamp, dilated fundoscopy, <b>colour vision assessment</b> &mdash; plus a neurological exam. <b>MRI brain AND orbits, with and without contrast</b></td></tr>
    <tr><td><b>Escalation</b></td><td>If MRI shows <b>at least 2 characteristic demyelinating lesions</b>, ophthalmology treats and refers to <b>neurology or neuro-ophthalmology</b></td></tr>
    <tr><td><b>Treatment</b></td><td><b>Corticosteroids</b> if a demyelinating cause is found</td></tr>
    <tr><td><b>Prognosis</b></td><td><b>Spontaneous recovery is the rule.</b> Without treatment vision begins improving <b>within a few weeks</b>, may continue for months, and is usually <b>normal within a year</b></td></tr>
    <tr><td><b>Education</b></td><td><b>Recurrence carries a greater risk of multiple sclerosis.</b> Do not treat the episode and stop &mdash; find out why it happened, or you miss the bigger problem</td></tr>
  </table>
  <figure class="fig"><img src="%(IMG)ss023_3.png" loading="lazy" alt="Axial FLAIR MRI of the brain with periventricular white-matter lesions, one arrowed."><figcaption>Periventricular demyelinating lesions on MRI. <b>Two or more</b> is the threshold that sends the patient on to neurology. <span class="cite">Slide 23</span></figcaption></figure>

  <h3 class="sub" id="e2l3-detachment">3.5 &middot; Retinal detachment <span class="cite">Objective a4</span></h3>
  <table class="tbl">
    <tr><th>Facet</th><th>Content</th></tr>
    <tr><td><b>Pathophysiology</b></td><td>Traction detachment that <b>commonly follows a retinal tear or hole</b>. Three types: <b>rhegmatogenous, traction, serous/exudative</b></td></tr>
    <tr><td><b>Epidemiology</b></td><td><b>Most common after age 50</b> &mdash; the vitreous humor shrinks with age</td></tr>
    <tr><td><b>Risk factors</b></td><td><b>Myopia</b> (contracted ciliary muscle), <b>trauma</b>, <b>cataract extraction</b>, diabetes, tumour, <b>connective tissue disease</b>, family history</td></tr>
    <tr><td><b>Early symptoms</b></td><td><b>New flashing lights and floaters</b> &mdash; these represent the <b>retinal TEAR</b>, not the detachment itself</td></tr>
    <tr><td><b>Then</b></td><td><b>Grey or black shadows</b> in the peripheral field, which may cover the whole eye <b>within days</b>. A <b>&ldquo;curtain or dark cloud&rdquo;</b> across the field</td></tr>
    <tr><td><b>The escalation</b></td><td><b>If the macula is involved &rarr; sudden loss of vision in that eye</b></td></tr>
    <tr><td><b>Odd but useful</b></td><td><b>The visual loss can change with head position</b>, because the detached retina is floating loose</td></tr>
    <tr><td><b>Diagnosis</b></td><td>Direct and dilated ophthalmoscopy: retina <b>elevated, grey cloud with folds</b>, a <b>pigmented well-demarcated area</b>, and tears that are <b>orange and crescent shaped</b>. <b>Ultrasound is MORE SENSITIVE than the fundoscopic exam</b> and determines the type</td></tr>
    <tr><td><b>Treatment</b></td><td><b>EMERGENCY &mdash; refer immediately.</b> Surgical repair urgently or within a week depending on type. Options: <b>laser photocoagulation, cryotherapy, pneumatic retinopexy, vitrectomy, scleral buckle</b></td></tr>
  </table>
  <figure class="fig"><img src="%(IMG)ss028_1.png" loading="lazy" alt="Fundus photograph of a detached retina showing pale billowy folds, arrowed."><figcaption>The detached upper retina &mdash; opaque and cloudy, vessels no longer visible, with the <b>&ldquo;billowy folds&rdquo;</b> the deck names. <span class="cite">Slide 28</span></figcaption></figure>
  <div class="callout warn">
    <p><strong>Her disposition, verbatim in substance:</strong> this one needs to be seen
    <em>right now</em>. If no ophthalmologist can take them, they go to a hospital that has one.
    Not tomorrow.</p>
  </div>

  <h3 class="sub" id="e2l3-occlusion">3.6 &middot; The four retinal vascular occlusions <span class="cite">Objective a5</span></h3>
  <table class="tbl">
    <tr><th></th><th>CRAO &mdash; artery</th><th>CRVO &mdash; vein</th></tr>
    <tr><td><b>Mechanism</b></td><td><b>Embolus</b> &mdash; arteriosclerosis, atherosclerosis, carotid or cardiac emboli</td><td><b>Thrombus</b> occluding the central retinal vein</td></tr>
    <tr><td><b>Frequency</b></td><td>Less common</td><td><b>MORE common than CRAO</b></td></tr>
    <tr><td><b>Onset</b></td><td><b>Painless profound loss over a few SECONDS</b></td><td><b>Sudden and painless</b>; sometimes gradual over <b>days to weeks</b></td></tr>
    <tr><td><b>Acuity</b></td><td><b>Counting fingers to light perception</b>; an <b>&ldquo;island&rdquo; of vision in the temporal field</b></td><td>Blurring to loss</td></tr>
    <tr><td><b>Pupil</b></td><td><mark class="prof-highlight">Slow to direct light, but BRISK when the other eye is illuminated</mark> &mdash; she called this a huge clinical clue</td><td>&mdash;</td></tr>
    <tr><td><b>Fundus</b></td><td><b>Pale swelling</b> of the posterior segment with a <b>CHERRY-RED SPOT at the fovea</b>; emboli visible in the central artery</td><td><b>&ldquo;BLOOD AND THUNDER&rdquo;</b> &mdash; disc swelling, venous dilation, <b>cotton wool spots</b>, retinal haemorrhages</td></tr>
    <tr><td><b>Risk factors</b></td><td colspan="2"><b>Shared:</b> hypertension, diabetes, hyperlipidaemia, Raynaud's, <b>age over 50</b>, hypercoagulable disorders, giant cell arteritis, endocarditis, atrial myxoma, obesity. CRAO adds atrial fibrillation</td></tr>
    <tr><td><b>Later</b></td><td colspan="2"><b>Neovascularization occurs weeks to months after the occlusion</b> in both</td></tr>
    <tr><td><b>Confirmatory</b></td><td colspan="2"><b>Colour fundus photography and fluorescein angiography</b></td></tr>
    <tr><td><b>Treatment</b></td><td><b>Prompt.</b> High-concentration inhaled oxygen and <b>digital massage over the eyelid</b>; <b>IV acetazolamide</b> to lower pressure; <b>anterior chamber paracentesis</b>; <b>thrombolytic infusion into the ophthalmic artery within 8 hours</b></td><td><b>Urgent ophthalmology referral to restore blood flow</b>; evaluate and treat the underlying disorders</td></tr>
  </table>
  <div class="prof-flag">
    <span class="prof-flag-label">&#9733; The number, and the reason</span>
    <p><strong>CRAO is a stroke in the eye.</strong> <mark class="prof-highlight">Irreversible
    retinal damage may occur after 90 minutes.</mark> And the systemic implication matters as much
    as the eye: the retinal arteries are tiny, so if plaque broke off the carotid and reached one,
    <strong>there is a great deal more plaque still in that carotid</strong> &mdash; stroke risk
    rises at the onset of a retinal artery occlusion.</p>
  </div>
  <p><strong>The branch forms.</strong> <b>BRAO</b> and <b>BRVO</b> are <em>the same disease as
  their central counterparts</em>, differing only in <b>where the blockage sits</b>. A branch
  vessel is occluded rather than the main trunk, so <b>only part of the retina is affected</b> and
  the field loss is partial and localised rather than widespread. Everything else &mdash; risk
  factors, workup, referral &mdash; is the same. The lecturer was explicit that this is all there
  is to it.</p>

  <h3 class="sub" id="e2l3-papilledema">3.7 &middot; Papilledema</h3>
  <div class="callout warn">
    <p><strong>This is the one condition here that is NOT about intraocular pressure.</strong>
    Papilledema is swelling of the optic disc caused by raised <b>INTRACRANIAL</b> pressure
    &mdash; pressure inside the skull pushing on the optic disc. Every other pressure in this
    lecture is inside the globe. She drew the line explicitly.</p>
  </div>
  <table class="tbl">
    <tr><th>Facet</th><th>Content</th></tr>
    <tr><td><b>Causes</b></td><td><b>Tumour, trauma, intracranial infection</b> (meningitis), <b>haemorrhage</b>, <b>vitamin A toxicity</b></td></tr>
    <tr><td><b>Visual symptoms</b></td><td>Non-specific: <b>flickering vision, blurry vision, double vision</b></td></tr>
    <tr><td><b>Systemic symptoms</b></td><td>Non-specific signs of raised intracranial pressure: <b>nausea, vomiting, headache</b></td></tr>
    <tr><td><b>Fundus</b></td><td><b>Engorged retinal veins</b>, <b>swollen optic disc</b>, with or without retinal haemorrhages</td></tr>
    <tr><td><b>Diagnosis</b></td><td><b>Lumbar puncture</b> &mdash; an increased opening pressure confirms raised intracranial pressure. <b>MRI and/or CT head to rule out a mass lesion</b></td></tr>
    <tr><td><b>Treatment</b></td><td><b>Treat the underlying disorder</b></td></tr>
  </table>
  <figure class="fig figpair"><img src="%(IMG)ss045_1.png" loading="lazy" alt="Swollen optic disc with flame haemorrhages, arrowed."><img src="%(IMG)ss045_4.png" loading="lazy" alt="Swollen optic disc with a cotton wool spot, arrowed."><figcaption><b>Acute papilledema.</b> Left, <b>haemorrhages</b>; right, a <b>cotton wool spot</b>. <span class="cite">Slide 45 A and B</span></figcaption></figure>
  <figure class="fig figpair"><img src="%(IMG)ss045_3.png" loading="lazy" alt="Elevated optic disc with blurred margins and no haemorrhage."><img src="%(IMG)ss045_2.png" loading="lazy" alt="Pale optic disc with tortuous vessels, arrowed."><figcaption><b>Left, chronic papilledema</b> &mdash; disc elevation and blurred margins, <b>but no haemorrhages or cotton wool spots</b>. <b>Right, the atrophic phase</b> &mdash; the optic nerve axons have died. <span class="cite">Slide 45 C and D</span></figcaption></figure>
  <div class="callout">
    <p><strong>Papilledema pushes the disc OUT. Glaucoma cups it IN.</strong> She stressed how
    distinctly different the two look, and it is the single most reliable way to tell them apart
    at the fundus.</p>
  </div>

  <h3 class="sub" id="e2l3-aion">3.8 &middot; Anterior ischemic optic neuropathy <span class="cite">Objective a6</span></h3>
  <p><strong>Definition:</strong> sudden loss of blood flow to the <b>front part of the optic
  nerve &mdash; the optic disc</b>, causing <b>rapid, painless vision loss</b>. Common to both
  forms: <b>sudden painless loss of side or central vision</b>, <b>swelling and PALENESS of the
  optic nerve head</b>, and involvement of <b>one eye first, though the second eye is at
  risk</b>.</p>
  <table class="tbl">
    <tr><th></th><th>ARTERITIC (AAION)</th><th>NON-ARTERITIC (NAION)</th></tr>
    <tr><td><b>Share of cases</b></td><td>The minority</td><td><b>90&ndash;95%</b></td></tr>
    <tr><td><b>Age</b></td><td><b>55 and older</b></td><td><b>40 to 60</b></td></tr>
    <tr><td><b>Cause</b></td><td><b>Giant cell (temporal) arteritis</b> &mdash; inflammation of the blood vessels</td><td>Linked to a <b>small structural optic disc</b> &mdash; a <b>&ldquo;disc at risk&rdquo;</b></td></tr>
    <tr><td><b>Associations</b></td><td>Systemic: <b>malaise, weight loss, fever</b>, <b>headache in the temporal or occipital region</b>, <b>scalp tenderness</b> (classically on combing the hair), <b>jaw claudication</b> on eating or chewing</td><td><b>Hypertension, diabetes, high cholesterol, sleep apnea</b></td></tr>
    <tr><td><b>Urgency</b></td><td><b>MEDICAL EMERGENCY.</b> Refer emergently any patient <b>over 50</b> with sudden visual loss</td><td>Not emergent once arteritis is excluded</td></tr>
    <tr><td><b>Workup</b></td><td><b>ESR and CRP</b> &mdash; the tests used to rule giant cell arteritis in or out. <b>Temporal artery biopsy is the gold standard</b></td><td><b>A diagnosis of EXCLUSION.</b> The workup is <b>identical</b> &mdash; you are making sure there is no giant cell arteritis &mdash; then medical evaluation for hypertension, diabetes and anaemia, with neuroimaging if unclear</td></tr>
    <tr><td><b>Treatment</b></td><td><b>IV methylprednisolone for 3 days</b>, then a <b>slow oral taper</b> to the lowest dose that suppresses the disease, guided by symptoms and labs &mdash; <b>typically 6 to 12 months</b>. Add <b>famotidine</b> for gastrointestinal ulcer prophylaxis</td><td><b>Observation and cardiovascular risk factor modification.</b> Consider <b>avoiding antihypertensives at bedtime</b>, since nocturnal hypotension can worsen it</td></tr>
    <tr><td><b>Prognosis</b></td><td>Depends on <b>how long it has been present and when corticosteroids started</b>. <b>Early therapy is critical</b> &mdash; untreated it leads to blindness. Follow up with ophthalmology</td><td>Follow up with ophthalmology</td></tr>
  </table>
  <div class="callout">
    <p><strong>Her boundary on giant cell arteritis.</strong> <em>&ldquo;I'm not going to test you
    on GCA directly, I promise you &mdash; but it's kind of hard when I know GCA is what's causing
    this not to explain GCA to you.&rdquo;</em> So learn it as <b>the cause of arteritic AION and
    the reason that presentation is an emergency</b>, not as a rheumatology topic in its own
    right.</p>
    <p><strong>The picture she painted:</strong> an <b>elderly woman, usually Caucasian, over
    55</b>, <b>with no history of headaches</b>, who suddenly has a temporal headache. That change
    from no headaches to a new one is the warning sign.</p>
  </div>

  <h3 class="sub" id="e2l3-care">3.9 &middot; Care strategies &mdash; adult and elderly <span class="cite">Objective b</span></h3>
  <table class="tbl">
    <tr><th>Presentation</th><th>Disposition</th></tr>
    <tr><td><b>Sudden painless monocular loss, any cause</b></td><td><b>Stroke until proven otherwise &mdash; MRA, and urgent ophthalmology</b></td></tr>
    <tr><td><b>CRAO</b></td><td><b>Emergency department NOW</b> &mdash; the retina is lost after 90 minutes</td></tr>
    <tr><td><b>Retinal detachment</b></td><td><b>Same day</b>, to a hospital with an ophthalmologist if clinic cannot take them</td></tr>
    <tr><td><b>Acute angle-closure glaucoma</b></td><td><b>Emergent</b> &mdash; lower the pressure medically, iridotomy in 1&ndash;2 days</td></tr>
    <tr><td><b>Any patient over 50 with sudden vision loss</b></td><td><b>Emergent ophthalmology</b>, plus ESR and CRP for arteritic AION</td></tr>
    <tr><td><b>CRVO / BRVO / BRAO</b></td><td><b>Urgent</b> ophthalmology to restore flow; treat the underlying disorder</td></tr>
    <tr><td><b>Optic neuritis</b></td><td>Refer to ophthalmology; MRI brain and orbits; neurology if <b>2 or more</b> lesions</td></tr>
    <tr><td><b>Papilledema</b></td><td>Imaging to exclude a mass, then <b>lumbar puncture</b>; treat the cause</td></tr>
    <tr><td><b>Chronic open-angle glaucoma</b></td><td>Routine &mdash; but <b>annual eye exams</b> are how it gets found at all</td></tr>
  </table>
  <button type="button" class="test-yourself-btn" style="--acc:#2d3f7a" onclick="window.openTestYourself('Test yourself &mdash; Acute Vision Loss', TEST_YOURSELF.avl)">Test yourself! &rarr;</button>
</section>
""".replace("%(IMG)s", IMG)

TOC = """  <a class="top-link" href="#acute-vision-loss">3 &middot; Acute Vision Loss</a>
  <a class="sub-link" href="#e2l3-approach">3.1 The four separating questions</a>
  <a class="sub-link" href="#e2l3-amaurosis">3.2 Amaurosis fugax</a>
  <a class="sub-link" href="#e2l3-glaucoma">3.3 Glaucoma, acute and chronic</a>
  <a class="sub-link" href="#e2l3-neuritis">3.4 Optic neuritis</a>
  <a class="sub-link" href="#e2l3-detachment">3.5 Retinal detachment</a>
  <a class="sub-link" href="#e2l3-occlusion">3.6 The four vascular occlusions</a>
  <a class="sub-link" href="#e2l3-papilledema">3.7 Papilledema</a>
  <a class="sub-link" href="#e2l3-aion">3.8 Anterior ischemic optic neuropathy</a>
  <a class="sub-link" href="#e2l3-care">3.9 Care strategies</a>
"""

TEST = """    avl: [
      {q:"A curtain came down over one eye and lifted after 40 seconds. Which diagnosis?",
       choices:["Retinal detachment","Amaurosis fugax","CRAO","Optic neuritis"],correct:1,
       explain:"Both amaurosis fugax and retinal detachment use the word curtain. Duration separates them: amaurosis fugax lifts within seconds to minutes, a detachment stays and advances."},
      {q:"After how long does CRAO cause irreversible retinal damage?",
       choices:["30 minutes","90 minutes","8 hours","24 hours"],correct:1,
       explain:"90 minutes. The 8-hour figure is the window for intra-arterial thrombolysis, not the damage threshold."},
      {q:"Which fundus finding belongs to CRAO rather than CRVO?",
       choices:["Blood and thunder haemorrhage","A cherry-red spot at the fovea","Cotton wool spots","Venous dilation"],correct:1,
       explain:"Artery gives pale retina with a cherry-red fovea. Vein gives the haemorrhagic blood-and-thunder fundus. The other three are all venous."},
      {q:"Which pressure is raised in papilledema?",
       choices:["Intraocular","Intracranial","Central venous","Orbital compartment"],correct:1,
       explain:"Intracranial. Every other condition in this lecture involves pressure inside the globe. Papilledema pushes the disc OUT; glaucoma cups it IN."},
      {q:"A 24-year-old woman has vision loss over two days with pain on eye movement and washed-out colours. Which diagnosis?",
       choices:["NAION","Optic neuritis","Angle-closure glaucoma","CRVO"],correct:1,
       explain:"18-45 years, 75% female, painful eye movement, colour desaturation, often a normal-looking disc. The ischemic optic neuropathies are painless and occur in an older group."},
      {q:"Which drug class is a RISK FACTOR for acute angle-closure glaucoma?",
       choices:["Beta-blocker drops","Systemic anticholinergics","Prostaglandin analogues","Carbonic anhydrase inhibitors"],correct:1,
       explain:"Anticholinergics such as atropine, and nebulized bronchodilators. The other three are all treatments that LOWER intraocular pressure."},
      {q:"New flashing lights and floaters represent what?",
       choices:["Raised intracranial pressure","A retinal tear","Optic nerve inflammation","Venous thrombosis"],correct:1,
       explain:"The tear, which the detachment then commonly follows. If the macula becomes involved, vision in that eye is lost suddenly."},
      {q:"An 81-year-old woman has sudden vision loss, scalp tenderness and jaw claudication. What is done FIRST?",
       choices:["Await the temporal artery biopsy","Start IV methylprednisolone","Tonometry","Lumbar puncture"],correct:1,
       explain:"Treatment starts before the biopsy, because early therapy is what saves the vision. ESR and CRP are sent, and biopsy remains the gold standard, but neither delays the steroid."},
      {q:"What percentage of amaurosis fugax patients recover fully?",
       choices:["About 50%","About 85%","About 95%","Nearly none"],correct:1,
       explain:"About 85%. The rest progress to a central retinal artery occlusion, which is why early evaluation matters."},
      {q:"Which single imaging study does EVERY patient with sudden vision loss get?",
       choices:["Orbital ultrasound","MRA","Chest radiograph","Skull radiographs"],correct:1,
       explain:"Sudden acute vision loss is a stroke until proven otherwise -- you can have a stroke with no symptom other than vision loss. Carotid Doppler and echocardiogram are added for the suspected source."},
    ],
"""
