# -*- coding: utf-8 -*-
"""Section 5 of the CMS I Exam 2 guide -- Ocular Trauma (Lecture 14).

Lecturer: Chand Shah, MPAS, PA-C. Objectives VERBATIM from the deck's own
objective slide, which mirrors the syllabus.

TWO EXTRACTION TRAPS THIS SECTION HAD TO SURVIVE, both recorded in
_cms_e2_chart_l14.py:
  * the speaker notes do NOT map to slides by index -- all nine in this deck
    belong elsewhere, and are resolved through each slide's .rels
  * the notes label pictures by POSITION, and relationship order is not
    position order, so images carry their reading-order position

Slide 45's notes say "Top right: battle sign" twice. Both right-hand pictures
were viewed and both really are a Battle sign, so the second means BOTTOM
right -- a typo in the notes rather than a mapping error.

Figures reuse the chart's own audited images in place, per the standing rule
that a visual subject gets photographs in the guide.
"""

SECTION = """
<section class="deck" id="ocular-trauma">
  <h2 class="deck-title">5 &middot; Ocular Trauma</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">OPHTHALMOLOGY &mdash; Ocular Trauma</p>
    <ol type="a">
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis for ocular
      trauma:
      <ol type="1">
        <li>Foreign body</li><li>Corneal abrasions</li><li>Globe rupture</li><li>Hyphema</li>
        <li>Lid lacerations</li><li>Orbital and lid contusion</li><li>Periorbital hematoma</li>
        <li>Retinal and vitreous detachments</li><li>Blowout fractures</li>
        <li>Orbital fracture</li><li>Basilar skull fracture</li>
      </ol></li>
      <li>Identify medical care strategies for common ophthalmological disorders in the lecture
      topic list for the following populations: 1. infant &middot; 2. child &middot;
      3. adolescent &middot; 4. adult &middot; 5. elderly</li>
    </ol>
  </div>

  <div class="callout">
    <p><strong>Before the eye, the patient.</strong> <strong>ABCs first</strong> &mdash; airway
    patent, breathing adequate, circulation present &mdash; then vital signs, neurological
    evaluation and the rest. An injured eye usually arrives attached to major trauma involving the
    brain, and <strong>the eyes may be assessed second</strong>. Always reason from the anatomy to
    what else could be damaged.</p>
    <p><strong>One point she added aloud that is not on a slide:</strong> the
    <strong>Glasgow Coma Scale runs from 3 to 15</strong>, not from 0. Three is the floor because
    each of its three components scores a minimum of one.</p>
  </div>

  <h3 class="sub" id="e2l5-rules">5.1 &middot; The four rules that apply before any diagnosis</h3>
  <p>These sit at the front of the lecture because breaking one of them makes the injury worse.</p>
  <table class="tbl">
    <tr><th>Rule</th><th>Why</th></tr>
    <tr><td><b>DO NOT REMOVE a penetrating object</b></td>
        <td>It may be tamponading a wound. Removal in the emergency department can extrude intraocular contents.</td></tr>
    <tr><td><b>CT orbit &mdash; never MRI</b></td>
        <td>If the object is metallic, a magnetic field will move it through the eye.</td></tr>
    <tr><td><b>NEVER dilate the eye</b> when ocular trauma is suspected</td>
        <td>It removes the pupil examination, which is one of the few windows onto what is happening inside.</td></tr>
    <tr><td><b>Check tetanus status</b></td>
        <td>Any penetration with metal or organic material &mdash; wood, leaf, dirt &mdash; carries the risk.</td></tr>
  </table>
  <p><strong>When is imaging automatic?</strong> Any loss of consciousness from trauma or alcohol,
  confusion, tachypnoea, apnoeic breathing, anticoagulant use, or eye penetration &rarr;
  <strong>CT without contrast</strong>.</p>
  <p class="muted">Epidemiology worth carrying: ocular trauma is the <b>leading cause of monocular
  blindness in young adult men in the United States</b>.</p>

  <h3 class="sub" id="e2l5-assess">5.2 &middot; Assessing the patient</h3>
  <p>Establish the <strong>circumstance</strong>: who, what, where, when, and if you can, why. Blunt
  or sharp? High or low velocity? Prior ocular trauma? <strong>Nil-by-mouth status</strong> &mdash;
  what and when they last ate and drank &mdash; because surgery may follow. If the patient is
  intoxicated or has an altered level of consciousness, the history comes from family, friends or
  bystanders.</p>
  <p>The ophthalmic examination is <strong>done without causing further damage</strong> and depends
  on how cooperative the patient is: inspect the eyes and periorbital tissues for lacerations,
  ecchymosis, proptosis, corneal clouding and hyphema; assess <strong>pupil size, shape and
  response to direct and consensual light</strong>; and if the patient is conscious and cooperative,
  test <strong>visual acuity and confrontation fields</strong>. Consult ophthalmology for anything
  needing further evaluation.</p>
  <p class="muted">A practical aside from the deck: if no lid retractor is to hand, an unfolded
  paper clip bent with a hemostat will retract a lid.</p>

  <h3 class="sub" id="e2l5-globe">5.3 &middot; Open globe injury</h3>
  <p>A <strong>full-thickness defect in cornea and/or sclera</strong>, so the intraocular
  compartments are open to the outside. It splits into <strong>full-thickness eye wall
  laceration</strong> and <strong>globe rupture</strong>.</p>
  <p><strong>The signs to recognise:</strong> pupillary distortion, usually <em>toward</em> the
  wound; a flat anterior chamber; extraocular protrusion of uveal tissue; massive haemorrhagic
  chemosis; a <strong>soft eye</strong>; deep eyelid laceration; and intraocular blood as hyphema
  or vitreous haemorrhage.</p>
  @@GLOBE@@
  <table class="tbl">
    <tr><th></th><th>Full-thickness eye wall laceration</th><th>Globe rupture</th></tr>
    <tr><td><b>Mechanism</b></td><td><b>Sharp object or high-velocity projectile</b> &mdash; fishing hook, knife</td><td><b>Severe blunt force</b> &mdash; airbag, fist, baseball</td></tr>
    <tr><td><b>What happens</b></td><td>Cuts clean through cornea, sclera or both. The object may have been withdrawn, may be retained, or may have passed through with entry and exit wounds</td><td>Splits or tears at a <b>weak point</b>: posterior to the extraocular muscle insertions (especially superonasal), old surgical incisions, the lamina cribrosa</td></tr>
    <tr><td><b>Extra</b></td><td>A cut lens capsule leaves the lens <b>hydrated, oedematous and opaque</b>; a fragment can extrude forward and inflame the anterior chamber. <b>Lensectomy is required but often deferred</b>. Posterior foreign bodies are <b>left alone</b> initially</td><td>Suspect it whenever blunt trauma gives massive haemorrhagic chemosis or a soft eye</td></tr>
  </table>
  <p><strong>The moment an open globe is suspected:</strong> a <strong>rigid protective shield taped
  over the eye</strong>, ophthalmology called immediately, <strong>antiemetics and analgesia</strong>
  so the patient does not strain or vomit, tetanus, and CT to exclude a foreign body. Then surgical
  repair.</p>

  <h3 class="sub" id="e2l5-surface">5.4 &middot; Corneal abrasion and foreign body</h3>
  @@SURFACE@@
  <p><strong>Corneal abrasion</strong> &mdash; scraped corneal epithelium, one of the commonest
  ocular injuries, typically from a fingernail or handling a contact lens. Severe foreign body
  sensation, tearing, photophobia, blurred vision. <strong>Slit lamp with fluorescein</strong>
  stains the exposed basement membrane and shows the extent. Treat with a <strong>topical
  broad-spectrum antibacterial</strong>; patching may ease pain; re-examine to confirm healing.</p>
  <div class="callout">
    <p><strong>Never give a patient topical anaesthetic drops to take home.</strong> They delay
    healing, mask worsening symptoms, and can cause a corneal ulcer. This is the single most
    testable instruction in the section.</p>
  </div>
  <p><strong>Foreign body</strong> &mdash; an object with too little momentum to pass through the
  eye wall lodges in cornea or conjunctiva. The history is <strong>grinding or striking
  metal</strong>. <strong>Linear vertical corneal epithelial defects mean the object is in the
  tarsal conjunctiva of the UPPER lid</strong>, so evert the lid and look. Removal: topical
  anaesthetic, slit lamp, <strong>sterile 27-gauge needle</strong>; a <strong>rust ring</strong>
  from iron or copper comes out with a battery-operated burr. Then broad-spectrum antibiotic and
  abrasion care. Refer if the object may have passed <em>through</em> the cornea &mdash; that is an
  open globe.</p>

  <h3 class="sub" id="e2l5-hyphema">5.5 &middot; Hyphema</h3>
  @@HYPHEMA@@
  <p>Blood in the anterior chamber from injured vessels, after blunt or penetrating trauma.
  <strong>It can itself be a sign of open globe.</strong> Blurred vision, eye pain, photophobia.
  Diagnosed on diffuse light for a gross hyphema, then slit lamp and full ophthalmic examination.</p>
  <p><strong>Measure the intraocular pressure &mdash; unless a penetrating globe injury is
  suspected</strong> &mdash; and treat it if high, with beta blockers, pilocarpine, acetazolamide
  and osmotic agents if needed.</p>
  <p>The whole of management aims at <strong>preventing a rebleed</strong>: bed rest with the head
  of the bed slightly elevated, antiemetics, ocular hypotensives, topical or oral corticosteroids,
  <strong>cycloplegic drops</strong> (atropine, homatropine, scopolamine) to rest the ciliary body,
  and <strong>oral aminocaproic acid</strong>, an antifibrinolytic that slows clot breakdown.</p>
  <div class="callout">
    <p><strong>Most rebleeding happens in the first 72 hours</strong>, and a secondary haemorrhage
    is what costs the vision permanently. <strong>Avoid aspirin and antiplatelet drugs.</strong>
    Risk is increased in <strong>sickle cell disease</strong>.</p>
  </div>

  <h3 class="sub" id="e2l5-lids">5.6 &middot; Lid lacerations, contusion and periorbital haematoma</h3>
  @@LIDS@@
  <p><strong>Lid lacerations.</strong> Consult ophthalmology for any laceration that involves the
  <strong>lid margin</strong>, sits <strong>within 6 to 8 mm of the medial canthus</strong>, involves
  the <strong>lacrimal duct or sac</strong>, involves the inner lid surface, is associated with
  <strong>ptosis</strong>, or involves the <strong>tarsal plate or levator palpebrae</strong>.</p>
  <ul>
    <li><b>Full-thickness</b> &mdash; comes with a corneal laceration or globe rupture in about
    <b>two thirds of cases</b>. Always look underneath.</li>
    <li><b>Partial-thickness</b> &mdash; anything not meeting the criteria above. Can be repaired in
    the emergency department, with ophthalmology follow-up in 2 to 3 days.</li>
  </ul>
  <p>A deep laceration to the <strong>medial third</strong> may transect the canalicular system, and
  if that is not repaired properly the patient has <strong>chronic tearing</strong> for good. Facial
  lacerations may be left open for 24 hours before closure, because the face is so well
  vascularised.</p>
  <p><strong>Orbital contusion</strong> is soft tissue swelling <em>without</em> haemorrhage. The
  tarsal plate and septal margin act as a wall holding blood in the anterior tissues, so it presents
  as preseptal ecchymosis or haematoma. Management is supportive through to surgery depending on the
  patient &mdash; and <strong>rule out brain trauma</strong>.</p>
  <p><strong>Periorbital haematoma</strong> is bleeding <em>within</em> the bony orbit. It is
  <strong>not always traumatic</strong>: orbit and eyelid surgery, peribulbar injections, orbital
  varices, lymphangiomas and arteriovenous malformations, anticoagulants, sickle cell disease,
  orbital pseudotumour and idiopathic causes all produce it. Management is <strong>canthotomy with
  cantholysis</strong> &mdash; exposing the lateral canthal tendon and cutting its inferior branch
  &mdash; to let the blood out.</p>

  <h3 class="sub" id="e2l5-detach">5.7 &middot; Retinal and vitreous detachment</h3>
  @@DETACH@@
  <p>The presentation is the same one that appears in Lecture 12: a <strong>shadow or curtain
  descending</strong> over the eye, cloudy or smoky vision, <strong>floaters and momentary flashes
  of light</strong>, a monocular field defect, and central acuity dropping once the macula is
  involved. Diagnosis is history plus a <strong>dilated eye examination</strong>. The patient must
  be <strong>seen by ophthalmology within 24 hours</strong>.</p>
  <p>What Lecture 14 adds is the three <strong>types</strong>, which do not share a treatment.</p>
  <table class="tbl">
    <tr><th>Type</th><th>Mechanism</th><th>Management</th></tr>
    <tr><td><b>Rhegmatogenous</b><br><span class="muted">most common</span></td>
        <td>One or more <b>full-thickness breaks</b> in the sensory retina, vitreous traction, and liquefied vitreous passing into the subretinal space. Usually preceded by <b>posterior vitreous detachment</b>. Mostly a spontaneous age-related event, brought forward by <b>myopia, cataract surgery or trauma</b></td>
        <td><b>Surgical.</b> Ophthalmology STAT, pain control, antiemetics, head of bed at 30&ndash;40 degrees</td></tr>
    <tr><td><b>Traction</b></td>
        <td>Most commonly <b>proliferative diabetic retinopathy</b>. More localised and <b>concave</b>; begins along the vasculature then spreads to retina and macula</td>
        <td><b>Surgical</b></td></tr>
    <tr><td><b>Exudative (serous)</b></td>
        <td><b>Neither a retinal break nor traction.</b> Associated with systemic vascular or inflammatory disease, or an intraocular tumour</td>
        <td><b>Manage the underlying condition</b></td></tr>
  </table>

  <h3 class="sub" id="e2l5-fracture">5.8 &middot; Orbital floor (blowout) fracture</h3>
  @@FRACTURE@@
  <p><strong>Two mechanisms.</strong> A true blowout, where a blunt object &mdash; a fist, a ball
  &mdash; transmits energy to the globe, raising orbital pressure until the <strong>floor</strong>
  (most often) or medial wall gives way. Or force transmitted to the <strong>infraorbital rim</strong>,
  buckling the floor.</p>
  <p><strong>Findings:</strong> periorbital ecchymosis and lid oedema; chemosis, subconjunctival
  haemorrhage, and <strong>infraorbital numbness</strong> from injury to the infraorbital nerve;
  corneal abrasion, hyphema, enophthalmos, proptosis, iridoplegia, dislocated lens, retinal tear or
  detachment, ruptured globe; and <strong>periorbital subcutaneous emphysema</strong>.</p>
  <div class="callout">
    <p><strong>The gaze rule.</strong> <b>Diplopia on UPWARD gaze</b> means entrapment of the
    <b>inferior rectus</b> or its supporting structures. <b>Diplopia on LATERAL gaze</b> means
    entrapment of the <b>medial rectus</b>. Entrapment also brings severe pain and autonomic
    disturbance &mdash; <b>bradycardia and vomiting on attempted eye movement</b>.</p>
    <p><strong>In children</strong>, an entrapped muscle may come with <em>no orbital soft tissue
    signs at all</em> &mdash; the <strong>&ldquo;white-eyed blowout&rdquo;</strong>. A quiet-looking
    eye does not exclude it.</p>
  </div>
  <p><strong>Diagnosis: CT of the orbits and midface.</strong> She gave the reason the midface is
  included: <em>&ldquo;to make sure there aren&rsquo;t any additional structures that are also
  fractured &hellip; if their orbital floor is fractured, sure, okay, but we want to make sure
  we&rsquo;re not missing any other fractures.&rdquo;</em> Management runs by severity:</p>
  <ul>
    <li><b>No eye injury or entrapment</b> &mdash; ice and analgesia, follow up in 2 to 3 days.</li>
    <li><b>Blood in the maxillary sinus</b> &mdash; antibiotics, and note that they are
    <b>PROPHYLACTIC</b>. Her reasoning: the eye is sterile, so blood in the sinus means the sinus
    has been disrupted and now has a portal of entry. <em>&ldquo;It&rsquo;s not that we&rsquo;re
    treating anything &hellip; it&rsquo;s to make sure that it doesn&rsquo;t become
    infected.&rdquo;</em></li>
    <li><b>True blowout fracture</b> &mdash; ophthalmology, because <b>30% sustain a significant
    globe injury</b>.</li>
    <li><b>Muscle entrapment</b> &mdash; <b>facial trauma surgeon STAT</b>, because a compromised
    blood supply means muscle necrosis.</li>
  </ul>
  <p>If the optic nerve is already damaged, that damage is unlikely to improve and surgery may
  worsen it. Where surgery is planned, it is often <strong>delayed 1 to 2 weeks</strong> to let
  orbital swelling settle, so intraorbital pressure during the operation is lower.</p>

  <h3 class="sub" id="e2l5-basilar">5.9 &middot; Basilar skull fracture</h3>
  @@BASILAR@@
  <p>A linear fracture of the skull base &mdash; cribriform plate of the ethmoid, orbital plate of
  the frontal, petrous or squamous temporal, sphenoid, or occipital bone. <strong>Trauma there
  often produces no symptoms of its own</strong>, so it is found on indirect signs:</p>
  <ul>
    <li>Visible bleeding from the fracture into the soft tissue at the base of the head</li>
    <li><b>Raccoon eyes</b> (periorbital ecchymosis) and <b>Battle sign</b> (retroauricular ecchymosis)</li>
    <li>Bleeding into the middle ear or sphenoid sinus; <b>haemotympanum</b></li>
    <li><b>Cerebrospinal fluid leak</b> &mdash; clear or pink rhinorrhoea</li>
  </ul>
  <div class="callout">
    <p><strong>Two bedside tests for cerebrospinal fluid.</strong> A <strong>dextrose stick</strong>
    may be positive. And fluid placed on filter paper &mdash; or found on the bedsheet &mdash; shows
    a <strong>halo or double ring sign</strong>: an inner ring of blood with an outer ring of
    cerebrospinal fluid.</p>
    <p><strong>How to actually do it.</strong> Hold a bedsheet, paper or tissue under the nostril,
    let the drip fall onto it, and watch as it dries &mdash; two rings appear, one inside the other.
    She was emphatic about this one: <em>&ldquo;that&rsquo;s a very classic and that&rsquo;s a very
    important sign for us to not miss.&rdquo;</em></p>
  </div>
  <p><strong>Diagnosis: CT orbits</strong>, though the fracture is not always evident on it.
  <strong>A cerebrospinal fluid leak means a neurosurgery consult and admission.</strong> Otherwise
  admission turns on the clinical condition, the associated injuries, and any brain injury seen on
  CT. <strong>Antibiotics for a cerebrospinal fluid leak are controversial</strong>, because of the
  risk of selecting resistant organisms.</p>
</section>
"""

TOC = """  <a class="top-link" href="#ocular-trauma">5 &middot; Ocular Trauma</a>
  <a class="sub-link" href="#e2l5-rules">5.1 The four rules</a>
  <a class="sub-link" href="#e2l5-assess">5.2 Assessing the patient</a>
  <a class="sub-link" href="#e2l5-globe">5.3 Open globe injury</a>
  <a class="sub-link" href="#e2l5-surface">5.4 Abrasion &amp; foreign body</a>
  <a class="sub-link" href="#e2l5-hyphema">5.5 Hyphema</a>
  <a class="sub-link" href="#e2l5-lids">5.6 Lids, contusion &amp; haematoma</a>
  <a class="sub-link" href="#e2l5-detach">5.7 Retinal &amp; vitreous detachment</a>
  <a class="sub-link" href="#e2l5-fracture">5.8 Blowout fracture</a>
  <a class="sub-link" href="#e2l5-basilar">5.9 Basilar skull fracture</a>
"""

TEST = """    trauma: [
      {q:"A patient has a metal fragment embedded in the eye after grinding. Which imaging?",
       o:["CT orbit","MRI orbit","Ocular ultrasound","Plain orbital radiograph"],a:0,
       why:"CT orbit, never MRI &mdash; a magnetic field will move a metallic fragment through the eye."},
      {q:"Blunt trauma has left a soft eye with massive haemorrhagic chemosis. What is the first action?",
       o:["Rigid shield over the eye and call ophthalmology","Measure the intraocular pressure",
          "Dilate and examine the fundus","Irrigate the eye copiously"],a:0,
       why:"That picture is a globe rupture. Do not press, do not dilate, do not measure pressure &mdash; shield it."},
      {q:"Which instruction must a patient with a corneal abrasion NOT be given?",
       o:["Take home topical anaesthetic drops","Use a topical antibiotic",
          "Return if symptoms worsen","Consider patching for pain"],a:0,
       why:"They delay healing, mask worsening symptoms and can cause a corneal ulcer."},
      {q:"Vertical linear corneal scratches point to a foreign body where?",
       o:["Under the upper lid","In the lower fornix","On the sclera","In the anterior chamber"],a:0,
       why:"Evert the upper lid &mdash; the vertical pattern is the object scraping with each blink."},
      {q:"Why is aminocaproic acid used in hyphema?",
       o:["It slows clot breakdown, reducing rebleeding","It lowers intraocular pressure",
          "It reverses anticoagulation","It prevents infection"],a:0,
       why:"Most rebleeding happens in the first 72 hours, and a secondary haemorrhage is what costs the vision."},
      {q:"Diplopia on UPWARD gaze after blunt orbital trauma means what?",
       o:["Inferior rectus entrapment","Medial rectus entrapment",
          "Superior oblique palsy","Optic nerve injury"],a:0,
       why:"Lateral gaze diplopia would point to the medial rectus instead."},
      {q:"A child has severe pain, bradycardia and vomiting on eye movement, but a quiet-looking eye. What is this?",
       o:["White-eyed blowout with muscle entrapment","Simple periorbital contusion",
          "Retrobulbar haemorrhage","Traumatic iritis"],a:0,
       why:"In children an entrapped muscle may show no orbital soft tissue signs at all."},
      {q:"Clear fluid from the nose after head trauma leaves a double ring on the bedsheet. What does that indicate?",
       o:["Cerebrospinal fluid leak from a basilar skull fracture","Simple epistaxis",
          "Lacrimal duct injury","Sinus infection"],a:0,
       why:"Inner ring of blood, outer ring of cerebrospinal fluid. Neurosurgery consult and admission."},
      {q:"Which retinal detachment is NOT primarily treated surgically?",
       o:["Exudative","Rhegmatogenous","Traction","All three are surgical"],a:0,
       why:"Exudative has no break and no traction &mdash; treat the underlying disease."},
      {q:"A lid laceration sits 5 mm from the medial canthus. Why does that matter?",
       o:["The canalicular system may be transected, causing chronic tearing",
          "It always means a globe rupture","It cannot be repaired surgically",
          "It indicates a basilar skull fracture"],a:0,
       why:"A missed canalicular injury leaves the patient tearing for life. Ophthalmology repairs it."}
    ],
"""
