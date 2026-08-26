#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add PD2 section 3 (Advanced Ocular History and Examination) to the guide.

BUILT FROM THE 26 AUGUST RECORDING, NOT THE DECK ALONE. Prof. Beck removes
slides from scope out loud and keeps to it; the deck cannot say which ones, so
this section was held until the audio existed. Six exclusions are honoured and
her emphases are flagged with the existing prof-flag machinery.

THE RED-EYE COMPARISON TABLE IS REPRODUCED IN TEXT. Slide 48 is a picture of
the Bates table and extracts as completely blank; it was recovered with
tools/ocr_deck_images.py. Beck then singled it out -- "I genuinely think it's
important that you are very familiar with that chart" -- so it is written out
here as a real table rather than left as an unreadable image reference.

Idempotent: fenced in <!--PD2L3--> and stripped before reinsert.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1",
                     "pd2-exam-1-study-guide.html")

BODY = """
<section class="deck" id="ocular-exam">
  <h2 class="deck-title">3 &middot; Advanced Ocular Medical History and Examination</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Advanced Ocular Medical History and Examination</p>
    <ol>
      <li>Review the anatomical landmarks of the normal eye.</li>
      <li>Identify the anatomical landmarks of the normal eye.</li>
      <li>Demonstrate proficiency in performing a complete ocular examination.</li>
      <li>Define the elements in the medical history that aid in identifying ocular disorders.</li>
      <li>Define the elements of the physical examination that aid in identifying abnormal conditions of the eye.</li>
      <li>Identify specific symptoms related to abnormal conditions of the eye including the eyelids, sclera, cornea, and iris.</li>
      <li>Describe and identify expected visual exam findings when lesions along the visual pathway are present.</li>
      <li>Describe physical exam findings in non-visual painful conditions of the eye.</li>
      <li>Describe physical exam findings in non-visual painless conditions of the eye.</li>
      <li>Define common ocular findings in relation to certain disease states including hypertension, diabetes mellitus, increased intracranial pressure, and infection.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; What she took OUT of scope</span>
    <p>Professor Beck removes slides out loud, and keeps to it. Six things she said she would
    <b>not</b> test are therefore not in the quizzes and are noted here only so you do not spend
    time on them:</p>
    <ol>
      <li><b>The named virus in viral conjunctivitis.</b> <em>&ldquo;I'm not going to test you on
      it, but adenovirus &hellip;&rdquo;</em> &mdash; she uses it for the great-mimicker story.</li>
      <li><b>The exophthalmometer</b>, its technique and its 20&ndash;22 mm figure.
      <em>&ldquo;I am not going to test you on the minutia of how to do that test &hellip; don't
      worry about it.&rdquo;</em> <b>Recognising exophthalmos IS in</b> &mdash; her words were
      &ldquo;about exophthalmos and how to recognise it&rdquo;.</li>
      <li><b>The strabismus diagram.</b> <em>&ldquo;This is just a visual &hellip; that you don't
      have to memorize.&rdquo;</em> Eso-, exo- and hypertropia as concepts stay in.</li>
      <li><b>The corneal reflection test.</b> <em>&ldquo;We've already done this, so I'm not gonna
      test you on it &hellip; we already did that in PD1.&rdquo;</em></li>
      <li><b>The Adie's pupil look-alike list</b> (dysautonomia, Shy-Drager, diabetes,
      amyloidosis). <em>&ldquo;It's not on my test this time.&rdquo;</em>
      <b>Adie's pupil itself IS in</b> &mdash; <em>&ldquo;you should know Adie's pupil, that could
      be on my test.&rdquo;</em></li>
      <li><b>The Latin expansions of OD, OS and OU.</b> <em>&ldquo;I don't care if you remember
      Oculus Sinister or Dexter.&rdquo;</em> <b>The abbreviations themselves ARE in</b> &mdash;
      <em>&ldquo;those are terms that you must remember.&rdquo;</em></li>
    </ol>
  </div>

  <h3 class="sub" id="l3-history">3.1 &middot; The history</h3>
  <p>Assess any eye complaint on four axes: <b>time course</b>, <b>precipitating factors</b>,
  <b>palliative or exacerbating variables</b>, and <b>vision loss or visual deficits</b>.</p>
  <table class="tbl">
    <tr><th>Finding</th><th>What it points to</th></tr>
    <tr><td><b>Bilateral</b> visual loss</td><td>A primary <b>neurologic</b> cause, not an ophthalmologic one</td></tr>
    <tr><td><b>Multiple new</b> flashes or floaters</td><td>Retinal tear or vitreous haemorrhage</td></tr>
    <tr><td>A <b>single</b> floater</td><td>Probably benign</td></tr>
    <tr><td><b>Rapid</b> deterioration</td><td>Vascular causes</td></tr>
    <tr><td><b>Gradual</b> loss</td><td>Cataract and the like</td></tr>
    <tr><td>Itching + excessive tearing</td><td>Allergic</td></tr>
    <tr><td><b>Deep</b> pain</td><td>Acute narrow angle glaucoma</td></tr>
    <tr><td>Pain <b>relieved</b> by topical anaesthetic</td><td>A surface problem &mdash; corneal injury feels better</td></tr>
    <tr><td>Pain <b>not relieved</b> by topical anaesthetic</td><td>A deeper source</td></tr>
  </table>
  <p><b>Also ask:</b> corrective lenses; acute or chronic eye problems such as glaucoma; eye
  medications such as antiglaucoma drops or topical antibiotics; and eye surgery history.
  <b>Tetanus status matters in eye trauma</b>, and after a chemical splash you must establish
  <b>whether the fluid was acid or alkali</b>. Beck singled out three systemic diseases:
  <b>diabetes, hypertension and human immunodeficiency virus</b> &mdash; the last because it will
  affect basically any aetiology.</p>

  <h3 class="sub" id="l3-symptoms">3.2 &middot; The symptom patterns</h3>
  <table class="tbl">
    <tr><th>Pattern</th><th>Think</th></tr>
    <tr><td>Acute, unilateral, <b>painless</b></td><td>Retinal vascular occlusion, retinal detachment, vitreous haemorrhage, macular degeneration</td></tr>
    <tr><td>Acute, unilateral, <b>painful</b></td><td>Usually cornea and anterior chamber: corneal abrasion or ulcer, uveitis, traumatic hyphaema, acute narrow angle glaucoma</td></tr>
    <tr><td>Acute, <b>bilateral</b>, painful</td><td>Thermal, radiation or chemical exposure</td></tr>
    <tr><td>Gradual, painless</td><td>Simple glaucoma or cataract</td></tr>
  </table>
  <p><b>Eye pain, qualified:</b> with <b>blinking</b> &rarr; corneal abrasion or foreign body
  &middot; <b>gritty</b> &rarr; conjunctivitis &middot; with <b>photophobia</b> &rarr; iris
  inflammation &middot; with <b>headache</b> &rarr; acute narrow angle glaucoma &middot; on
  <b>eye motion</b> &rarr; optic neuritis &middot; with <b>temporal</b> pain &rarr; temporal
  arteritis.</p>
  <p><b>Discharge:</b> watery or mucoid &rarr; allergic or viral; purulent &rarr; bacterial.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; &ldquo;Very important to commit to memory&rdquo;</span>
    <p><b>Diplopia and the cranial nerves.</b> <b>HORIZONTAL</b> &mdash; images side by side &mdash;
    means a palsy of <b>cranial nerve III or VI</b>. <b>VERTICAL</b> &mdash; images on top of each
    other &mdash; means a palsy of <b>cranial nerve III or IV</b>.</p>
    <p>Her shortcut: <em>&ldquo;three for both of those&rdquo;</em> &mdash; the third nerve appears
    in both patterns, so seeing double of anything implicates it; two images <b>side by side</b>
    is where the sixth nerve has joined in.</p>
    <p>Diplopia otherwise means faulty alignment or a neurological problem &mdash; brainstem or
    cerebellar lesions, or weakness of one or more extraocular muscles. Look for a
    <b>compensatory head posture</b>.</p>
  </div>

  <h3 class="sub" id="l3-inspection">3.3 &middot; Inspection</h3>
  <p><b>Order of the examination:</b> inspection &rarr; external examination &rarr; cornea without
  light, lens, pupils &rarr; <b>visual acuity, the vital sign of the eye</b> &rarr; visual fields
  &rarr; ocular motility &rarr; <b>pupillary reactions, checked BEFORE dilating</b> &rarr; corneal
  reflection &rarr; special tests &rarr; slit lamp &rarr; ocular pressure &rarr; direct
  ophthalmoscopy.</p>
  <div class="callout warn">
    <p><b>In trauma, do not palpate the globe.</b> And from the common-mistakes list: failing to
    look in both eyes, to examine the cornea and lens, to test acuity adequately, to identify a
    field defect, to evaluate all fundal structures, to recognise a ruptured globe (or placing too
    much pressure on one), to treat multiple floaters or new flashes as a possible detachment, to
    document adequately, to recognise an infectious red eye before prescribing a topical steroid,
    and <b>to differentiate preseptal from orbital cellulitis &mdash; because the latter can lead
    to death</b>.</p>
  </div>
  <table class="tbl">
    <tr><th>Finding</th><th>Meaning</th></tr>
    <tr><td>Scaly eyebrows</td><td>Seborrhoeic dermatitis</td></tr>
    <tr><td><b>Lateral sparseness</b> of the eyebrows</td><td>Hypothyroidism</td></tr>
    <tr><td>Ptosis</td><td>Myasthenia gravis, oculomotor nerve damage, sympathetic damage (Horner). Senile ptosis is weakened muscle, relaxed tissue and the weight of herniated fat. May be congenital</td></tr>
    <tr><td>Hordeolum</td><td>Painful infection <b>at the lid's edge</b></td></tr>
    <tr><td>Chalazion</td><td>Chronic, non-painful, meibomian &mdash; <b>generally NOT at the margin</b>; points inside the lid</td></tr>
    <tr><td>Xanthelasma</td><td>Raised yellowish plaques along the <b>nasal</b> lid &mdash; consider lipid disorders</td></tr>
    <tr><td>Ectropion / entropion / trichiasis</td><td>Out-turned lid / in-turned lid / posteriorly misdirected lashes</td></tr>
    <tr><td><b>Yellow</b> sclera</td><td>Liver disease</td></tr>
    <tr><td><b>Blue</b> sclera</td><td>Osteogenesis imperfecta</td></tr>
  </table>
  <p><b>Proptosis:</b> stand behind the seated patient and look down from above, drawing the lid
  slightly upward to compare the corneas against the lower lids. Causes: retrobulbar haemorrhage,
  orbital cellulitis, orbital tumour, <b>Graves disease</b>.</p>
  <p><b>Nasolacrimal duct obstruction test:</b> patient looks up; press on the lower lid near the
  medial canthus, just inside the bony rim, to compress the sac; look for fluid regurgitating from
  the puncta. <b>Mucopurulent fluid means obstruction.</b> Avoid the test if the area is
  significantly inflamed or tender.</p>
  <p><b>Everting the upper lid</b> to find a foreign body: patient looks down and relaxes; raise
  the lid so the lashes protrude, grasp them and pull down and forward; place a stick <b>at least
  1 cm above the lid margin</b> at the upper border of the tarsal plate and push down as you raise
  the lid edge. <b>Do not press on the eyeball. Never evert if globe rupture is suspected.</b></p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; &ldquo;Be very familiar with that chart&rdquo;</span>
    <p>She singled this out: <em>&ldquo;I actually do genuinely think it's important that you are
    very familiar with that chart &hellip; it helps you compare and contrast the common important
    eye conditions.&rdquo;</em> On the slide it is a <b>picture</b> of the table, so it does not
    appear in any text copy of the deck &mdash; it is written out here.</p>
    <table class="tbl">
      <tr><th></th><th>Conjunctivitis</th><th>Corneal injury / infection</th><th>Acute iritis</th><th>Glaucoma</th><th>Subconjunctival haemorrhage</th></tr>
      <tr><td><b>Pattern of redness</b></td><td>Conjunctival injection: diffuse dilation, redness <b>maximal peripherally</b></td><td colspan="3"><b>Ciliary injection</b> &mdash; deeper vessels visible as radiating vessels or a reddish-violet flush around the limbus. An important sign of these three, but the eye may be diffusely red instead</td><td>Leakage of blood outside the vessels &mdash; a homogeneous, <b>sharply demarcated</b> red area that fades to yellow then disappears</td></tr>
      <tr><td><b>Pain</b></td><td>Mild discomfort rather than pain</td><td>Moderate to severe, superficial</td><td>Moderate, aching, deep</td><td><b>Severe, aching, deep</b></td><td><b>Absent</b></td></tr>
      <tr><td><b>Vision</b></td><td>Not affected except temporary mild blurring from discharge</td><td>Usually decreased</td><td>Decreased</td><td>Decreased</td><td><b>Not affected</b></td></tr>
      <tr><td><b>Ocular discharge</b></td><td>Watery, mucoid or mucopurulent</td><td>Watery or purulent</td><td>Absent</td><td>Absent</td><td>Absent</td></tr>
      <tr><td><b>Pupil</b></td><td>Not affected</td><td>Not affected unless iritis develops</td><td>May be small and, with time, irregular</td><td><b>Dilated, fixed</b></td><td>Not affected</td></tr>
      <tr><td><b>Cornea</b></td><td>Clear</td><td>Changes depending on cause</td><td>Clear or slightly clouded</td><td><b>Steamy, cloudy</b></td><td>Clear</td></tr>
      <tr><td><b>Significance</b></td><td>Bacterial, viral and other infections; allergy; irritation</td><td>Abrasions and other injuries; viral and bacterial infections</td><td>Associated with many ocular and systemic disorders</td><td><b>Acute increase in intraocular pressure &mdash; an emergency</b></td><td>Often none. May result from trauma, bleeding disorders, or a sudden increase in venous pressure such as coughing</td></tr>
    </table>
    <p><b>When the injection pattern does not help</b>, the chart gives four backup clues to catch
    the dangerous three: <b>pain, decreased vision, unequal pupils, and a less than perfectly clear
    cornea</b>.</p>
  </div>

  <h3 class="sub" id="l3-acuity">3.4 &middot; Acuity, fields and motility</h3>
  <p><b>OD</b> is the right eye, <b>OS</b> the left, <b>OU</b> both &mdash; she called these
  &ldquo;terms that you must remember&rdquo;. <b>20/200</b> means that at 20 feet the patient reads
  print a normal eye reads at 200 feet; <b>the larger the second number, the worse the vision</b>.
  If the patient cannot read the chart, document <b>counting fingers, hand motion, or light
  perception</b>.</p>
  <p><b>Pinhole test:</b> the pinhole admits only light perpendicular to the lens, so the light
  need not be bent to focus &mdash; it therefore corrects any <b>refractive</b> error. If the
  deficit is <em>not</em> corrected, consider <b>cataract, optic nerve disease, or retinal
  disease</b>.</p>
  <p><b>Confrontation fields</b> are best done with both the <b>static finger wiggle</b> test
  (arms' length, hands two feet apart lateral to the ears, wiggling fingers brought slowly into
  view, testing each quadrant) and the <b>kinetic red target</b> test (a 5 mm red-topped pin moved
  inward from beyond each quadrant, asking when it <b>first appears RED</b>). A temporal defect in
  one eye should prompt testing for a nasal defect in the other. The normal <b>blind spot sits 15
  degrees temporal</b> to the line of gaze and is <b>enlarged in glaucoma, optic neuritis and
  papilloedema</b>.</p>
  <p><b>Nystagmus:</b> fine rhythmic oscillation. A few beats on lateral gaze is normal &mdash;
  bring the finger back into binocular vision, and if it persists there, consider a neurologic
  condition. <b>Lid lag</b> &mdash; sclera visible above the iris on downgaze &mdash; is most often
  <b>hyperthyroidism</b>. The <b>cover-uncover</b> test reveals slight muscle imbalance not
  otherwise seen.</p>

  <h3 class="sub" id="l3-pupils">3.5 &middot; The pupils</h3>
  <p>A difference of <b>half to one millimetre is common</b>, and anisocoria is benign <b>if the
  reactions are normal</b>. Abnormal: a difference <b>greater than 1 mm</b>, or a poorly reactive
  pupil.</p>
  <div class="callout warn">
    <p><b>Red on her slide, and she said so:</b> an <b>acute, significantly dilated pupil is a
    medical emergency</b>, particularly with headache or other neurologic signs &mdash;
    <b>uncal herniation</b> or a <b>posterior communicating artery aneurysm</b> causing a third
    nerve palsy.</p>
  </div>
  <p><b>Swinging light test.</b> Indication: anisocoria. Normal &mdash; direct and consensual
  constriction. <b>Abnormal: paradoxical DILATION of both pupils when the light swings to the
  affected eye, with an intact consensual reflex.</b> That is a <b>relative afferent pupillary
  defect &mdash; a Marcus Gunn pupil &mdash; and the lesion is the OPTIC NERVE.</b> The mechanism:
  the afferent stimulus on that side is reduced, so the efferent signal to both pupils falls and a
  net dilation results.</p>
  <table class="tbl">
    <tr><th></th><th>Pupil</th><th>Light</th><th>Near</th><th>Other</th></tr>
    <tr><td><b>Adie's tonic</b></td><td>Large, regular, usually unilateral</td><td>Severely reduced and slowed, or absent</td><td><b>Present but very slow</b></td><td>Degeneration of the ciliary ganglia and postganglionic parasympathetic fibres; slow accommodation blurs near vision</td></tr>
    <tr><td><b>Argyll Robertson</b></td><td>Small, unequal, irregular</td><td><b>No reaction</b></td><td><b>Constricts</b></td><td>&ldquo;Accommodates but doesn't react.&rdquo; Classically tertiary syphilis, today more often diabetes; also Lyme. Mydriatics dilate it only <b>incompletely</b></td></tr>
    <tr><td><b>Horner syndrome</b></td><td>Small (miosis)</td><td colspan="2"><b>Reacts briskly to both</b></td><td>Ptosis, anhidrosis of the ipsilateral face. Sympathetic supply to the pupil and levator interrupted. Congenital form: the involved iris is <b>lighter</b> (heterochromia)</td></tr>
    <tr><td><b>Oculomotor palsy</b></td><td>Dilated</td><td colspan="2"><b>Fixed to both</b></td><td>Ptosis and lateral deviation almost always present</td></tr>
  </table>
  <p><b>Once local eye disease is excluded, only three causes of a dilated pupil remain:</b>
  compression or other lesion of cranial nerve III; parasympathetic denervation from a ciliary
  ganglion lesion (Adie's); and pharmacologic block of the pupillary sphincter.</p>
  <p><b>Oblique lighting and the crescent shadow:</b> shine from the temporal side and look for a
  shadow on the medial iris. No shadow is normal &mdash; the iris is flat, the angle open. A shadow
  means the iris is <b>bowed forward, a narrow angle</b>, and a raised risk of narrow-angle
  glaucoma. A <b>corneal scar</b> is a superficial greyish-white opacity; do not confuse it with a
  cataract, which lies deeper and is seen only through the pupil.</p>

  <h3 class="sub" id="l3-fundus">3.6 &middot; Fundoscopy</h3>
  <p><b>Do NOT dilate</b> if serial neurologic examinations are required, in elderly patients who
  have had cataract surgery, or if acute angle-closure glaucoma is suspected. If you do dilate,
  <b>document the time and the agents used</b>.</p>
  <table class="tbl">
    <tr><th></th><th>Colour</th><th>Disc</th><th>Cup / vessels</th></tr>
    <tr><td><b>Normal</b></td><td>Yellowish-orange to cream</td><td><b>Sharp</b> margin</td><td>Cup central or slightly temporal, diameter <b>less than half the disc</b></td></tr>
    <tr><td><b>Papilloedema</b> (raised intracranial pressure)</td><td>Pink</td><td><b>Swollen, margins blurred</b></td><td><b>Cup not visible</b>; loss of vessel pulsations</td></tr>
    <tr><td><b>Glaucomatous cupping</b></td><td>&mdash;</td><td>&mdash;</td><td>Cup <b>enlarged, more than half</b> the disc; vessels sink in and around the disc</td></tr>
    <tr><td><b>Optic atrophy</b></td><td><b>White</b></td><td>&mdash;</td><td><b>Tiny disc vessels absent.</b> Seen in optic neuritis, multiple sclerosis, temporal arteritis</td></tr>
  </table>

  <h3 class="sub" id="l3-trauma">3.7 &middot; Trauma and disposition</h3>
  <p><b>Mechanism matters</b>, and so does the <b>size of the object</b>: larger objects transfer
  most of their energy to the orbital rim, while smaller ones may strike the globe directly.</p>
  <table class="tbl">
    <tr><th>Injury</th><th>Findings</th></tr>
    <tr><td><b>Orbital (blow-out) fracture</b></td><td>Sunken eye, <b>hypoaesthesia of the infraorbital area</b> (infraorbital nerve), <b>diplopia particularly on UPWARD gaze</b>, decreased motility, sometimes an ipsilateral nosebleed. Refer to ophthalmology or oral and maxillofacial surgery</td></tr>
    <tr><td><b>Enophthalmos</b></td><td>Sunken eye with ecchymosis, point tenderness and a <b>palpable step-off</b> at the orbital rim. Observe from above the head looking down</td></tr>
    <tr><td><b>Zygomatic fracture</b></td><td><b>Flattening of the malar eminence</b>, best seen from behind the seated patient. Oedema and ecchymosis of temple or infraorbital area, palpable step-off, infraorbital hypoaesthesia. <b>Pain on opening the mouth</b>, because temporalis passes medial to the arch and inserts on the mandible</td></tr>
    <tr><td><b>Hyphaema</b></td><td>Blood in the anterior chamber, usually blunt trauma. Check acuity, pupils (a crescent-like iris defect if torn; reduced reactions if the sphincter is damaged), the <b>red reflex</b>, the <b>intraocular pressure</b>, and slit lamp</td></tr>
    <tr><td><b>Corneal abrasion</b></td><td>Blunt trauma &mdash; fingernail, contact lens. Significant pain and photophobia, blepharospasm, foreign body sensation, tearing. <b>Evert the upper lid</b>: a foreign body in the upper tarsal conjunctiva scratches the cornea with every blink. <b>A hazy cornea suggests bacterial infection.</b> Topical anaesthetic gives immediate relief but is <b>for diagnosis, not treatment</b></td></tr>
    <tr><td><b>Corneal ulcer</b></td><td>Pain, photophobia, tearing, reduced vision. Red eye, circumcorneal injection, purulent or watery discharge. <b>Herpes simplex ulcers are not very painful.</b> An ophthalmoscope at <b>+40 dioptres</b> may reveal it, but <b>fluorescein is more sensitive</b> for early ulcers</td></tr>
  </table>
  <p><b>Fluorescein</b>: orange dye instilled, blue light &mdash; taken up by areas of cornea
  <b>devoid of epithelium</b>.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; &ldquo;Please know this list&rdquo;</span>
    <p>Her reason: <em>&ldquo;because you're going to be making those dispos.&rdquo;</em></p>
    <table class="tbl">
      <tr><th><b>EMERGENT</b> &mdash; ophthalmology or the emergency department immediately</th><th><b>URGENT</b> &mdash; ophthalmology follow-up in a day or less</th></tr>
      <tr><td>Sudden vision loss &middot; retinal artery occlusion &middot; chemical burns &middot; rupture &middot; acute angle-closure glaucoma &middot; vitreous haemorrhage</td><td>Acute glaucoma &middot; orbital cellulitis &middot; corneal ulcer or abrasion &middot; retinal detachment &middot; macular oedema or haemorrhage &middot; hyphaema</td></tr>
    </table>
  </div>
  <button type="button" class="test-yourself-btn" style="--acc:#4a5c24" onclick="window.openTestYourself('Test yourself &mdash; Advanced Ocular Examination', TEST_YOURSELF.ocular)">Test yourself! &rarr;</button>
</section>
"""

TOC = """  <a class="top-link" href="#ocular-exam">3 &middot; Advanced Ocular Examination</a>
  <a class="sub-link" href="#l3-history">3.1 The history</a>
  <a class="sub-link" href="#l3-symptoms">3.2 Symptom patterns</a>
  <a class="sub-link" href="#l3-inspection">3.3 Inspection &amp; the red-eye chart</a>
  <a class="sub-link" href="#l3-acuity">3.4 Acuity, fields &amp; motility</a>
  <a class="sub-link" href="#l3-pupils">3.5 The pupils</a>
  <a class="sub-link" href="#l3-fundus">3.6 Fundoscopy</a>
  <a class="sub-link" href="#l3-trauma">3.7 Trauma &amp; disposition</a>
"""

TESTS = """    ocular: [
      {q:"HORIZONTAL diplopia — images side by side — means a palsy of which cranial nerves?",
       choices:["III or IV","III or VI","IV or VI","II or III"],correct:1,
       explain:"She called this slide very important to commit to memory. Vertical (on top of each other) is III or IV. The third nerve appears in both."},
      {q:"On the swinging light test, both pupils DILATE when the light swings to one eye. What is this?",
       choices:["An efferent defect","A relative afferent pupillary defect — a Marcus Gunn pupil, lesion in the OPTIC NERVE","A normal finding","Adie's tonic pupil"],correct:1,
       explain:"The afferent stimulus on that side is reduced, so the efferent signal to both pupils falls and a net dilation results."},
      {q:"On the red-eye chart, which condition has a DILATED FIXED pupil and a steamy cornea?",
       choices:["Conjunctivitis","Acute iritis","Glaucoma","Subconjunctival haemorrhage"],correct:2,
       explain:"And its significance line reads: an acute increase in intraocular pressure — an emergency."},
      {q:"Which pupil accommodates but does not react to light?",
       choices:["Adie's tonic pupil","Argyll Robertson pupil","Horner syndrome","Oculomotor palsy"],correct:1,
       explain:"Small, unequal and irregular. Classically tertiary syphilis, today more often diabetes."},
      {q:"A patient's eye pain is RELIEVED by a topical anaesthetic. What does that suggest?",
       choices:["A deep source","A surface problem such as corneal injury","Acute glaucoma","Optic neuritis"],correct:1,
       explain:"Pain NOT relieved suggests a deeper source. It is a depth test."},
      {q:"Where is the normal blind spot, and what enlarges it?",
       choices:["15° nasal; enlarged in cataract","15° temporal; enlarged in glaucoma, optic neuritis and papilloedema","Central; enlarged in macular degeneration","30° temporal; enlarged in detachment"],correct:1,
       explain:"Temporal to the line of gaze, and the three conditions are all optic nerve related."},
      {q:"Which findings suggest an orbital blow-out fracture?",
       choices:["Proptosis with fever","Sunken eye, infraorbital hypoaesthesia, diplopia on UPWARD gaze, sometimes an ipsilateral nosebleed","Flattening of the cheek with pain on opening the mouth","A fixed mid-dilated pupil"],correct:1,
       explain:"The cheek flattening with jaw pain is a ZYGOMATIC fracture — temporalis passes medial to the arch."},
      {q:"Which is EMERGENT rather than urgent on her referral list?",
       choices:["Corneal abrasion","Hyphaema","Chemical burns","Orbital cellulitis"],correct:2,
       explain:"Emergent: sudden vision loss, retinal artery occlusion, chemical burns, rupture, acute angle closure, vitreous haemorrhage. The rest are urgent — a day or less."}
    ],
"""


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for o, cl in (("<!--PD2L3-->", "<!--/PD2L3-->"), ("<!--PD2TOC3-->", "<!--/PD2TOC3-->"),
                  ("<!--PD2TY3-->", "<!--/PD2TY3-->")):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(cl), "", src, flags=re.S)

    j = src.index("</main>")
    src = src[:j] + "<!--PD2L3-->" + BODY + "<!--/PD2L3-->\n\n" + src[j:]
    k = src.rindex("</nav>")
    src = src[:k] + "<!--PD2TOC3-->\n" + TOC + "<!--/PD2TOC3-->\n" + src[k:]
    m = src.index("var TEST_YOURSELF = {")
    m = src.index("\n", m) + 1
    src = src[:m] + "<!--PD2TY3-->\n" + TESTS + "<!--/PD2TY3-->\n" + src[m:]

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    # the six exclusions must be named in the scope block, so a reader knows why
    for term in ("adenovirus", "exophthalmometer", "strabismus diagram",
                 "corneal reflection", "Adie", "Oculus Sinister"):
        assert term.lower() in BODY.lower(), "%r missing from the scope block" % term
    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 3: %d subsections, %d flagged blocks, %d test-yourself questions"
          % (BODY.count('class="sub"'), BODY.count("prof-flag-label"), TESTS.count("{q:")))


if __name__ == "__main__":
    main()
