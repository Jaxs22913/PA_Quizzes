#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Medicine and Surgery I, Exam 2 study guide.

Starts a guide on a brand-new exam block using the established pattern: lift
the head, CSS and script skeleton from an existing guide, retheme it, and
splice in a new table of contents, body and TEST_YOURSELF object.

Donor is the CMS I Exam 1 guide, so the two blocks share their structure. The
palette is retheme d from Exam 1's TEAL to INDIGO -- a near-identical teal
would make the two blocks indistinguishable in the guide list.

FIGURES ARE USED AND CITED, per the standing rule in [[media_asset_licensing]]:
any course-slide image may be used so long as the slide is cited, and marks
baked into the pixels are left visible rather than cropped. The four pairs
chosen here are the ones the exam actually turns on visually -- pinguecula
against pterygium, pre-septal against post-septal cellulitis, the herpes simplex
dendrite against the zoster pseudodendrite, and the ciliary flush. Each was
viewed before being used, and they are shared with the comparison chart rather
than extracted twice.

Objectives are quoted VERBATIM from the syllabus, whose population list
includes CHILD -- the slide's version omits it. [[guide_verbatim_io_rule]].

data-audio-dir is deliberately absent: pointing at an audio folder with no mp3s
in it breaks read-aloud on iPad, because the 404 pushes speech synthesis outside
the original tap.
"""
import os, re

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1/cms-exam-1-study-guide.html")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2/cms-exam-2-study-guide.html")


IMGDIR = "cms-ophtho-chart-images"


def figpair(a, b, cap, slide):
    """Two slide images side by side -- the visual discriminations that matter."""
    for fn in (a, b):
        assert os.path.exists(os.path.join(os.path.dirname(OUT), IMGDIR, fn)), \
            "missing %s -- run extract_cms_e2_chart_images.py" % fn
    return ('<figure class="fig figpair">'
            '<img src="%s/%s" loading="lazy" alt="Left half of the comparison.">'
            '<img src="%s/%s" loading="lazy" alt="Right half of the comparison.">'
            '<figcaption>%s <span class="cite">Slide %d</span></figcaption></figure>'
            % (IMGDIR, a, IMGDIR, b, cap, slide))


def figone(fn, cap, slide):
    assert os.path.exists(os.path.join(os.path.dirname(OUT), IMGDIR, fn)), fn
    return ('<figure class="fig"><img src="%s/%s" loading="lazy" alt="%s">'
            '<figcaption>%s <span class="cite">Slide %d</span></figcaption></figure>'
            % (IMGDIR, fn, cap.replace('"', ""), cap, slide))

TOC = """<nav class="toc">
  <a class="top-link" href="#ophthalmology-i">1 &middot; Common Ophthalmological Disorders</a>
  <a class="sub-link" href="#e2l1-approach">1.1 The red eye, before a diagnosis</a>
  <a class="sub-link" href="#e2l1-tests">1.2 The diagnostic modalities</a>
  <a class="sub-link" href="#e2l1-lids">1.3 Eyelid disorders</a>
  <a class="sub-link" href="#e2l1-lacrimal">1.4 Lacrimal disorders</a>
  <a class="sub-link" href="#e2l1-surface">1.5 Conjunctiva and ocular surface</a>
  <a class="sub-link" href="#e2l1-conjunctivitis">1.6 Conjunctivitis, all of it</a>
  <a class="sub-link" href="#e2l1-sclera">1.7 Episcleritis and scleritis</a>
  <a class="sub-link" href="#e2l1-cornea">1.8 Keratitis and corneal ulcer</a>
  <a class="sub-link" href="#e2l1-uveitis">1.9 Uveitis</a>
  <a class="sub-link" href="#e2l1-cellulitis">1.10 Pre-septal and post-septal cellulitis</a>
  <a class="sub-link" href="#e2l1-disposition">1.11 Referral timing</a>
</nav>"""

BODY = """<main class="content">
<section class="deck" id="ophthalmology-i">
  <h2 class="deck-title">1 &middot; Common Ophthalmological Disorders</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">OPHTHALMOLOGY &mdash; Common Ophthalmological Disorders</p>
    <ol type="a">
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis of the following
      common ophthalmological disorders:
        <ol>
          <li>Conjunctivitis</li><li>Episcleritis</li><li>Scleritis</li>
          <li>Keratoconjunctivitis sicca</li>
          <li>Ocular manifestations of herpes infections: a. Herpes simplex virus (HSV-1) &middot; b. Varicella zoster</li>
          <li>Subconjunctival hemorrhage</li><li>Pinguecula</li><li>Pterygium</li>
          <li>Orbital (post-septal) and periorbital (pre-septal) cellulitis</li>
          <li>Blepharitis</li><li>Chalazion</li><li>Hordeolum</li><li>Ectropion</li>
          <li>Entropion</li><li>Dermatochalasis</li><li>Xanthelasma</li>
          <li>Lacrimal disorders: a. Dacryocystitis &middot; b. Dacryoadenitis</li>
          <li>Uveitis: a. Anterior uveitis (iritis/iridocyclitis) &middot; b. Posterior uveitis</li>
          <li>Keratitis</li><li>Corneal ulcer</li>
        </ol>
      </li>
      <li>Identify medical care strategies for ophthalmological disorders in the lecture topic
      list for the following populations: 1. infant &middot; 2. child &middot; 3. adolescent
      &middot; 4. adult &middot; 5. elderly</li>
    </ol>
  </div>

  <div class="callout">
    <p><strong>Where this sits against Clinical Pathophysiology.</strong> Clin Path I Lecture 4
    covers almost this exact condition list from the <em>mechanism</em> side &mdash; why the tissue
    fails. This section is the <em>management</em> side: what it looks like, what to order, what to
    give, and when to refer. If you find yourself revising the same fact twice, check which half
    you are actually being asked for.</p>
    <p><strong>A standing warning.</strong> Several of these rules are stated as absolutes but
    are softened in practice. Imaging is <em>not</em> automatic for dacryoadenitis,
    dacryocystitis or clearly pre-septal disease; haematology referral is <em>not</em> automatic
    for a recurrent subconjunctival haemorrhage; and perforation risk in scleritis is greatest in
    <em>necrotising</em> disease rather than uniformly. Those hedges are folded in below.</p>
  </div>

  <h3 class="sub" id="e2l1-approach">1.1 &middot; The red eye, before you name a diagnosis</h3>
  <div class="callout warn">
    <p><strong>She said she will not test this section.</strong> After finishing posterior uveitis
    she moved on and said: <em>&ldquo;This is extra material. You can write that. I&rsquo;m not
    going to pull test questions from this. This is not instructional objective.&rdquo;</em> It is
    kept here because it is the most clinically useful material in the block
    &mdash; but <b>no quiz question is built on it</b>. Read it for the ward, not for the exam.</p>
  </div>
  <p>The single most transferable thing here is a sequence rather than a fact.
  <strong>Complete this before naming the diagnosis:</strong></p>
  <ol>
    <li><strong>Visual acuity in each eye, with correction</strong> &mdash; the vital sign of the eye</li>
    <li><strong>Pupils</strong>: shape, reactivity, afferent defect</li>
    <li><strong>Extraocular movements</strong>, noting pain or restriction</li>
    <li><strong>Corneal clarity and fluorescein staining</strong></li>
    <li><strong>Pattern of injection and discharge</strong></li>
    <li><strong>History</strong>: contact lenses, trauma, surgery, steroids</li>
  </ol>
  <p><strong>Reduced vision or an abnormal pupil is a red flag.</strong> The warning is
  blunt: <em>do not let obvious redness substitute for an eye examination.</em></p>

  <div class="callout warn">
    <p><strong>Danger signs &mdash; these stop the reflex diagnosis of conjunctivitis:</strong>
    moderate to severe pain or <b>consensual photophobia</b> (pain in the affected eye when light
    is shone in the <em>other</em> eye) &middot; reduced acuity, a relative afferent pupillary
    defect, or an abnormal pupil &middot; corneal opacity, infiltrate, ulcer or dendrite &middot;
    <b>ciliary flush</b> (a ring of redness spreading from the corneal edge), hypopyon, or markedly
    raised pressure &middot; proptosis, diplopia, or painful restricted eye movement &middot;
    chemical exposure, penetrating trauma, or recent eye surgery &middot; <b>a contact lens wearer
    with pain or photophobia</b>.</p>
  </div>

  <p><strong>Use the pattern to localise before you name:</strong></p>
  <table class="tbl">
    <tr><th>Localises to</th><th>Pattern</th></tr>
    <tr><td>Conjunctiva</td><td>Itch or discharge; diffuse injection; <b>vision preserved</b></td></tr>
    <tr><td>Cornea</td><td>Pain and photophobia; fluorescein defect, infiltrate or opacity</td></tr>
    <tr><td>Anterior chamber</td><td><b>Consensual</b> photophobia; ciliary flush; irregular pupil</td></tr>
    <tr><td>Sclera / orbit</td><td>Deep pain or painful eye movement; violaceous sclera, proptosis, restriction</td></tr>
    <tr><td>Angle closure</td><td>Pain and headache with halos and nausea; cloudy cornea; <b>mid-dilated pupil</b></td></tr>
  </table>

  <div class="callout warn">
    <p><strong>Two exceptions to the sequence.</strong> <b>Chemical exposure</b> &mdash; irrigate
    copiously <em>first</em>, before history or examination, then confirm the surface pH has
    normalised. <b>Suspected open globe</b> &mdash; rigid shield, no pressure, <em>no
    tonometry</em>, keep nil by mouth, emergency consultation.</p>
  </div>

  <h3 class="sub" id="e2l1-tests">1.2 &middot; The diagnostic modalities</h3>
  <table class="tbl">
    <tr><th>Test</th><th>What it is</th><th>What it finds</th></tr>
    <tr><td><b>Slit lamp</b></td><td>Low-power microscope with a high-intensity slit beam</td><td>Anterior structures: lids, cornea, conjunctiva, sclera, iris</td></tr>
    <tr><td><b>Ophthalmoscopy</b></td><td>Direct (hand-held), indirect (lens + head-worn), or slit-lamp &mdash; the last is <b>most common</b> because the patient is already seated there</td><td>Vitreous, retina, retinal vessels, macula, optic disc</td></tr>
    <tr><td><b>Fluorescein examination</b></td><td>Yellow dye <b>instilled</b>, viewed under a Wood lamp (ultraviolet)</td><td>Corneal abrasions, ulcers, foreign bodies</td></tr>
    <tr><td><b>Fluorescein angiography</b></td><td>Dye <b>injected</b> into hand or arm, reaches the eye in 10&ndash;15 seconds, blue-flash camera. <b>No iodine</b>, relatively safe</td><td>Blood flow in retina and choroid: diabetic retinopathy, macular degeneration and oedema, ocular melanoma, detachment, retinitis pigmentosa</td></tr>
  </table>

  <h3 class="sub" id="e2l1-lids">1.3 &middot; Eyelid disorders</h3>
  <table class="tbl">
    <tr><th></th><th>Entropion</th><th>Ectropion</th></tr>
    <tr><td>Lid margin</td><td>Turns <b>IN</b></td><td>Turns <b>OUT</b></td></tr>
    <tr><td>Symptom</td><td>Foreign body sensation</td><td>Tearing</td></tr>
    <tr><td>Complication</td><td>Lashes onto the globe (<b>trichiasis</b>) &rarr; corneal abrasion</td><td><b>Exposure keratopathy</b></td></tr>
    <tr><td>Causes</td><td colspan="2">Ageing, cicatricial (burn, surgery, trauma, chronic inflammation, scar), congenital &mdash; plus <b>seventh nerve palsy for ectropion only</b></td></tr>
    <tr><td>Management</td><td colspan="2">Slit lamp for corneal involvement. Preservative-free tears by day, ointment at night, tape the exposed lid. <b>Surgery is definitive.</b></td></tr>
  </table>

  <p><strong>Dermatochalasis</strong> &mdash; excess loose skin with orbital fat prolapse, from
  ageing. Patients say the lids feel <em>heavy</em> and they are <em>looking through their
  lashes</em>. <strong>Examine the visual fields</strong>: a demonstrated deficit is what gets
  <b>blepharoplasty</b> covered by insurance.</p>

  <p><strong>Xanthelasma</strong> &mdash; oval yellowish plaques, typically asymptomatic, from
  metabolic disorders with raised serum lipids. <strong>Work up the metabolism</strong>: lipid
  profile, plus fasting glucose and haemoglobin A1C for diabetes, plus liver function. Treat the
  underlying issue; local options are cryotherapy, laser ablation, chemical peel or excision.
  <strong>Recurrence is common even after effective local treatment.</strong> One caveat: many patients have entirely normal lipids, and the profile is still reasonable.</p>

  <p><strong>Blepharitis and meibomitis</strong> &mdash; associated with <b>rosacea, seborrhoeic
  dermatitis, and Staphylococcus aureus colonisation</b>. Burning, dryness, grittiness, itching,
  foreign body sensation, tearing. Signs: crusting and scaling at the lash bases, erythematous
  swollen lid margins, and <b>thick, sometimes toothpaste-like lipid secretion</b> from the
  meibomian glands, with a decreased or frothy tear film.
  <strong>Lid hygiene first.</strong> If no improvement after <b>two weeks</b>, topical
  antibiotics, then oral. <strong>Chronic &mdash; controlled rather than cured.</strong></p>

  <table class="tbl">
    <tr><th></th><th>Chalazion</th><th>Hordeolum (stye)</th></tr>
    <tr><td>Mechanism</td><td><b>Sterile</b> obstruction of a meibomian gland</td><td>Acute <b>infection</b>, usually staphylococcal &mdash; meibomian (internal) or Zeis/Moll (external)</td></tr>
    <tr><td>Onset</td><td>Days to weeks</td><td><b>24 hours or overnight</b></td></tr>
    <tr><td>The discriminator</td><td><b>NON-tender</b></td><td><b>TENDER</b></td></tr>
    <tr><td>First-line</td><td colspan="2">Warm compresses and gentle massage</td></tr>
    <tr><td>If it persists</td><td>Ophthalmology for steroid injection or curettage. <b>Improvement may take months.</b></td><td>Ophthalmology for incision and drainage if no improvement in <b>2 weeks</b></td></tr>
  </table>
  <p><strong>Refer a recurrent chalazion, or one persisting beyond 2&ndash;3 months, to rule out
  sebaceous carcinoma.</strong> If a hordeolum is accompanied by pre-septal cellulitis, treat with
  systemic antibiotics on that pathway.</p>

  <h3 class="sub" id="e2l1-lacrimal">1.4 &middot; Lacrimal disorders</h3>
  <table class="tbl">
    <tr><th></th><th>Dacryoadenitis (GLAND)</th><th>Dacryocystitis (SAC)</th></tr>
    <tr><td>Where</td><td><b>Lateral one third of the UPPER lid</b></td><td><b>Nasal aspect of the LOWER lid</b>, below the medial canthal tendon</td></tr>
    <tr><td>Cause</td><td><b>Inflammatory most common</b>; bacterial rare; viral usually bilateral</td><td><b>Nasolacrimal duct obstruction</b></td></tr>
    <tr><td>Extra signs</td><td>Ipsilateral preauricular node, temporal conjunctival injection, fever, leukocytosis</td><td><b>Mucoid or purulent discharge expressible from the lower punctum</b></td></tr>
    <tr><td>Treatment</td><td>Inflammatory &rarr; <b>corticosteroids, response within 48 h</b>. Viral &rarr; cool compresses. Cause unclear &rarr; empiric oral antibiotics 24 h then reassess</td><td>Well &amp; reliable &rarr; <b>oral antibiotics 10 days</b>. Febrile, ill or unreliable &rarr; <b>admit, IV 48&ndash;72 h then oral to complete 10&ndash;14 days</b></td></tr>
  </table>
  <div class="callout warn">
    <p><strong>Do not start corticosteroids for dacryoadenitis until bacterial and other
    infectious causes have been reasonably excluded.</strong> And a mass <b>ABOVE</b> the medial
    canthal tendon is not dacryocystitis &mdash; suspect a lacrimal sac tumour, rare as it is.</p>
    <p>Once dacryocystitis settles, <strong>probing and irrigation are often needed</strong> to
    assess whether the drainage system is patent; surgery may follow. Expect improvement
    <b>24&ndash;48 hours</b> after antibiotics start.</p>
  </div>

  <h3 class="sub" id="e2l1-surface">1.5 &middot; Conjunctiva and ocular surface</h3>
  @@PINGPTER@@
  <p><strong>Pinguecula and pterygium</strong> both come from chronic sun and wind exposure and sit
  almost always at <b>3 o'clock or 9 o'clock</b>. The whole distinction:
  <strong>the pterygium extends onto the cornea, the pinguecula does not.</strong> The
  mnemonic: <em>pterodactyls fly (into the cornea), penguins can't.</em>
  Protect from sun, dust and wind; lubricating drops. <strong>Conservative management will not make
  it resolve.</strong> Non-urgent referral if it grows or vision is affected; surgery if it
  distorts vision.</p>

  <p><strong>Subconjunctival haemorrhage (atraumatic)</strong> &mdash; Valsalva, bleeding disorder,
  antiplatelet or anticoagulant medication, hypertension. Blood under the conjunctiva, no pain,
  normal vision and pupil, clear cornea. <strong>History is the whole workup</strong>, and
  <strong>check the blood pressure if there is no explanation.</strong> Reassurance; resolves in
  <b>2&ndash;4 weeks</b>.</p>
  <div class="callout">
    <p><strong>The patient-education point she spent time on.</strong> The eye clears the way a
    bruise does &mdash; red, then purplish, then brown, then <b>yellow</b>. Warn them about the
    yellow stage: <em>&ldquo;there will be a point that they look like they&rsquo;re jaundiced
    &hellip; so they don&rsquo;t come thinking that they&rsquo;re in liver failure. People do know
    yellow eyes and liver failure, they seem to know that association.&rdquo;</em></p>
    <p>And a general rule she gave alongside it: <b>anybody who comes in with any eye condition,
    check their vision</b> &mdash; with their contacts or glasses in, because what you want to know
    is whether it has <em>changed</em>.</p>
  </div>
  <p> For recurrence, what is wanted is medication review, blood pressure and
  targeted evaluation &mdash; <em>not</em> automatic haematology referral.</p>

  <p><strong>Chemosis</strong> is conjunctival swelling &mdash; a <em>sign</em>, not a diagnosis.
  Non-specific for irritation: allergy, infection, thyroid eye disease, angioedema, trauma, orbital
  cellulitis, impaired orbital venous drainage. <strong>Chemosis WITH proptosis, restricted
  movement, reduced vision or an afferent pupillary defect is urgent.</strong></p>

  <h3 class="sub" id="e2l1-conjunctivitis">1.6 &middot; Conjunctivitis, all of it</h3>
  <p><strong>Acute is 4 weeks or less; chronic is more than 4 weeks.</strong> Two examination
  findings do most of the sorting:</p>
  <table class="tbl">
    <tr><th>Finding</th><th>Appearance</th><th>Points to</th></tr>
    <tr><td><b>Papillae</b></td><td>Red at the surface, paler at the base &mdash; her analogy: <b>&ldquo;it almost looks like a strawberry&rdquo;</b></td><td>Bacterial (except chlamydial), allergic</td></tr>
    <tr><td><b>Follicles</b></td><td>Pale at the surface, redder at the base</td><td>Chlamydial, viral</td></tr>
    <tr><td><b>Preauricular node</b></td><td>&mdash;</td><td>Chlamydial, <b>gonococcal</b>, viral</td></tr>
  </table>
  <table class="tbl">
    <tr><th>Type</th><th>Giveaway</th><th>Treatment</th></tr>
    <tr><td><b>Allergic</b></td><td><b>ITCH</b>, bilateral, watery/stringy discharge, chemosis, papillae, <b>no node</b></td><td>Avoid the allergen; cool compresses, artificial tears, topical histamine blocker &plusmn; mast cell stabiliser (<b>olopatadine does both</b>), systemic antihistamine</td></tr>
    <tr><td><b>Viral</b></td><td>Adenovirus. Profuse watery discharge, <b>follicles</b>, <b>tender preauricular node</b>. Starts one eye, spreads to the other. Recent upper respiratory infection</td><td>Cool compresses, artificial tears, <b>contagious precautions</b>. Self-limiting: often worse over week one, resolving in 2&ndash;3 weeks. Refer if &gt;3 weeks, or photophobia or vision loss after onset</td></tr>
    <tr><td><b>Bacterial</b></td><td>Thick yellow/white discharge, often <b>unilateral</b>, papillae, usually <b>no node</b></td><td>Immunocompetent adult: <b>topical broad-spectrum antibiotic</b> (e.g. fluoroquinolone) + contagious precautions</td></tr>
    <tr><td><b>Gonococcal</b></td><td><b>Severe purulent discharge WITH a palpable preauricular node</b> &mdash; the exception to the no-node rule</td><td><b>Newborn = emergency.</b> Hospitalise, systemic ceftriaxone, cultures and Gram stain, test for chlamydia and dissemination. Untreated risk: <b>corneal perforation</b></td></tr>
    <tr><td><b>Chlamydial (adult inclusion)</b></td><td><b>Serotypes D&ndash;K.</b> Chronic (a month or more), stringy mucoid discharge, follicles, <b>unresponsive to topical medication</b>. Often concurrent asymptomatic urogenital infection</td><td>Confirm with conjunctival nucleic acid amplification or direct fluorescent antibody. <b>Doxycycline 100 mg twice daily for 7 days.</b> Evaluate for other sexually transmitted infections; notify partners</td></tr>
    <tr><td><b>Chlamydial (neonatal)</b></td><td>Serotypes D&ndash;K from maternal secretions; may have <b>pneumonia</b></td><td><b>Erythromycin 50 mg/kg/day divided four times daily for 14 days.</b> Monitor infants under 6 weeks for <b>infantile hypertrophic pyloric stenosis</b> &mdash; erythromycin is a motilin receptor agonist</td></tr>
    <tr><td><b>Autoimmune</b></td><td>Recurrent/chronic hyperaemia, <b>minimal pain, NO discharge</b>, systemic complaints. Pemphigoid, Stevens-Johnson, Sjögren, graft-versus-host</td><td>Routine ophthalmology referral</td></tr>
  </table>
  <div class="callout">
    <p><strong>Trachoma</strong> &mdash; <b>serotypes A, B, C</b>, and the <b>leading infectious
    cause of blindness worldwide</b>. Most active cases are asymptomatic. Mass drug administration
    with <b>azithromycin 1 g orally as a single dose</b> where prevalence is <b>&ge;5 per cent</b>.
    The chain to blindness is worth memorising:
    <b>conjunctival inflammation &rarr; eyelid scarring &rarr; entropion &rarr; trichiasis &rarr;
    blindness</b>. Trichiasis needs <strong>surgery</strong>.</p>
  </div>
  <p><strong>Urgent ophthalmology in bacterial conjunctivitis if:</strong> immunocompromised,
  contact lens wearer, recent eye surgery, foreign body, corneal opacity or suspected keratitis,
  or <strong>no improvement in 24 hours</strong>.</p>

  <h3 class="sub" id="e2l1-sclera">1.7 &middot; Episcleritis and scleritis</h3>
  <table class="tbl">
    <tr><th></th><th>Episcleritis</th><th>Scleritis</th></tr>
    <tr><td>Aetiology</td><td>Often idiopathic, often no systemic association</td><td>Often <b>systemic autoimmune</b></td></tr>
    <tr><td>Pain</td><td><b>Mild</b>, acute onset, focal. No discharge, no photophobia</td><td><b>Severe boring pain, worse at night</b>, radiating to face and periorbital region</td></tr>
    <tr><td>Appearance</td><td>Redness, often sectoral</td><td><b>Violaceous hue</b> &mdash; choroid showing through thinned sclera. Pain with eye movement</td></tr>
    <tr><td>Cotton-tip test</td><td>Vessels <b>CAN</b> be moved slightly</td><td>Vessels <b>CANNOT</b> be moved</td></tr>
    <tr><td>Confirmatory test</td><td><b>2.5% phenylephrine, wait 15 minutes &mdash; vessels blanch</b></td><td>&mdash;</td></tr>
    <tr><td>Management</td><td>Artificial tears + <b>oral anti-inflammatory taken WITH FOOD</b>. Refer if no response in <b>2 days</b></td><td><b>URGENT referral.</b> Slit lamp and fundoscopy, work up the systemic cause. Sclera at risk of perforation, may need a surgical patch</td></tr>
    <tr><td>Prognosis</td><td>Usually self-limited; may recur in either eye</td><td><b>Decreased PAIN is the first sign of response</b>, even if the inflammation looks unchanged</td></tr>
  </table>
  <p class="muted">A refinement worth carrying: non-infectious anterior scleritis commonly
  <em>begins</em> with systemic non-steroidal anti-inflammatories, with corticosteroids and
  immunomodulators for severe, necrotising, posterior or refractory disease &mdash; and perforation
  risk is greatest in <em>necrotising</em> disease, not uniformly.</p>

  <h3 class="sub" id="e2l1-cornea">1.8 &middot; Keratitis and corneal ulcer</h3>
  @@FLUSH@@
  <p><strong>Ciliary flush</strong> &mdash; a ring of red vessels spreading from the limbus around
  the cornea, from the anterior ciliary arteries. It means inflammation of <b>cornea, iris or
  ciliary body</b>, and appears in <b>corneal inflammation (ulcer, keratitis), anterior uveitis,
  and acute glaucoma</b>. It is the finding that rules <em>out</em> simple conjunctivitis.</p>
  <p><strong>Keratitis.</strong> Risks: corneal trauma, dry eyes, <b>contact lens overwear</b>,
  topical ocular corticosteroids. Bacterial, viral, fungal; parasitic rare. Pain, foreign body
  sensation, tearing, photophobia, redness at the corneal edge, blurred vision. Signs:
  <b>corneal opacification, a &ldquo;broken up&rdquo; corneal light reflection, ciliary flush</b>.
  <b>Classic ring infiltrate = Acanthamoeba</b>, in lens wearers with poor hygiene such as rinsing
  lenses in tap water.
  <strong>Urgent referral within 24 hours</strong> for slit lamp with fluorescein.
  <strong>Undertreated &rarr; corneal scarring or perforation &rarr; endophthalmitis &rarr;
  possible removal of the eye.</strong></p>
  @@HERPES@@
  <table class="tbl">
    <tr><th></th><th>Herpes SIMPLEX keratitis</th><th>Herpes ZOSTER keratitis</th></tr>
    <tr><td>Corneal sign</td><td><b>TRUE DENDRITE</b> &mdash; tree-branching, elevated edges, <b>terminal end bulbs</b>. <b>Pathognomonic</b></td><td><b>PSEUDODENDRITE</b> &mdash; lacks the branch pattern, the elevated edges and the end bulbs</td></tr>
    <tr><td>Patient</td><td>Often <b>younger</b></td><td>Often <b>older</b>; rare in children; also immunosuppressed</td></tr>
    <tr><td>Skin</td><td><b>Not dermatomal</b>, may not respect the midline (only ~10% of primary disease is bilateral)</td><td><b>Dermatomal, most often V1, respects the midline</b>, unilateral, often spares the lower lid. <b>Hutchinson sign</b> (nose tip) &rarr; higher ocular risk</td></tr>
    <tr><td>Treatment</td><td colspan="2">Oral antivirals (aciclovir, valaciclovir, famciclovir) <b>&times;10 days</b>. Ideally start within <b>72 hours</b> of rash onset. IV aciclovir for severe, disseminated, orbital, retinal, central nervous system or significantly immunocompromised disease</td></tr>
    <tr><td>Prognosis</td><td>Good, benign, self-limited. Recurrences common under stress</td><td>Good to poor by corneal involvement. <b>Postherpetic neuralgia can be devastating</b></td></tr>
  </table>
  <div class="callout warn">
    <p><strong>NO TOPICAL GLUCOCORTICOIDS BY THE PRIMARY CARE PROVIDER IN ACTIVE HERPES SIMPLEX
    EPITHELIAL DISEASE.</strong> That decision belongs to ophthalmology. Prevention: recombinant
    zoster vaccine for adults 50 and over, and immunocompromised adults 19 and over.</p>
  </div>
  <p><strong>Corneal ulcer.</strong> <b>Contact lens use is the major risk factor.</b> Painful eye,
  the patient <b>resists opening it</b>, photophobia, foreign body sensation, tearing, blurred
  vision. Ciliary flush and a corneal defect. <strong>EMERGENT referral</strong> &mdash; a step
  above keratitis. Slit lamp, fluorescein, swab central or large ulcers for culture. Start a
  <b>broad-spectrum topical agent (fourth-generation fluoroquinolone)</b>.
  <strong>Steroid drops can worsen infection if started too early &mdash; especially fungal or
  herpetic &mdash; so leave that to ophthalmology.</strong> Next-day follow-up; most heal in
  <b>2&ndash;3 weeks</b>; untreated can blind; severe cases may need a transplant.</p>

  <h3 class="sub" id="e2l1-uveitis">1.9 &middot; Uveitis</h3>
  <table class="tbl">
    <tr><th></th><th>Anterior (iritis, iridocyclitis)</th><th>Posterior (choroiditis, retinitis)</th></tr>
    <tr><td>Aetiology</td><td>Idiopathic, autoimmune</td><td>Idiopathic, autoimmune, <b>infectious &mdash; toxoplasmosis, cytomegalovirus</b></td></tr>
    <tr><td>Pain</td><td><b>Yes</b> &mdash; with photophobia and redness at the corneal edge</td><td><b>NO pain</b> if isolated</td></tr>
    <tr><td>Vision</td><td>Often <b>preserved</b></td><td>Blurred, with <b>floaters, scotomas, metamorphopsia</b></td></tr>
    <tr><td>Signs</td><td><b>Cells in the anterior chamber</b>, consensual photophobia, ciliary flush, variable pressure, irregular pupil stuck to lens or cornea, <b>keratic precipitates</b> (white cell deposits on the corneal endothelium)</td><td><b>Cells in the posterior vitreous</b>, vitreous haze, retinal or choroidal inflammation</td></tr>
    <tr><td>Referral</td><td><b>Urgent, within 24 h</b> &mdash; delay may cost vision</td><td>Refer for slit lamp and dilated fundoscopy; possibly fluorescein angiography to separate active from inactive lesions</td></tr>
    <tr><td>Treatment</td><td>Infectious &rarr; treat the organism. Non-infectious &rarr; <b>topical corticosteroids</b></td><td><b>Does NOT respond to topical treatment</b> &mdash; may need an <b>intraocular corticosteroid injection</b></td></tr>
    <tr><td>Course</td><td>Most acute cases respond dramatically in days to weeks</td><td>Develops far more slowly, may last years</td></tr>
  </table>
  <p>Recurrent uveitis, or uveitis with features suggesting systemic autoimmune disease, needs a
  <strong>thorough systemic evaluation</strong>. And
  <strong>infection must be excluded before immunosuppression.</strong></p>

  <h3 class="sub" id="e2l1-cellulitis">1.10 &middot; Pre-septal and post-septal cellulitis</h3>
  @@CELLULITIS@@
  <p>Both come from <b>direct extension from a bacterial sinus, skin or dental infection</b>. In
  diabetic, elderly or immunocompromised patients, <b>consider fungus &mdash; aspergillosis,
  mucormycosis</b>.</p>
  <table class="tbl">
    <tr><th></th><th>PRE-septal (periorbital)</th><th>POST-septal (orbital)</th></tr>
    <tr><td>The giveaway</td><td><b>The eye itself is WHITE</b></td><td><b>The eye itself is RED</b> and cannot move fully</td></tr>
    <tr><td>Symptoms</td><td colspan="2">Both: periocular pain, fever and chills, warmth around the eye</td></tr>
    <tr><td>Post-septal only</td><td>&mdash;</td><td><b>Pain and difficulty with eye movement, reduced vision, diplopia</b></td></tr>
    <tr><td>Signs</td><td>Diffuse balloon-like lid oedema, erythema, tenderness; variable conjunctival injection</td><td>Significant injection, <b>proptosis</b>, decreased and painful movement, possible <b>afferent pupillary defect</b>, decreased vision</td></tr>
    <tr><td>Management</td><td><b>Mild</b> &rarr; outpatient oral antibiotics <b>10&ndash;14 days</b> against Staphylococcus (including resistant strains) and Streptococcus</td><td><b>ALL post-septal</b> &rarr; hospitalise, broad-spectrum IV <b>48&ndash;72 h</b>, then oral at least a week</td></tr>
  </table>
  <p><strong>Also admit a pre-septal patient if:</strong> moderate-severe or toxic, poor compliance
  expected, <b>a child of 5 years or younger</b>, or no improvement after oral antibiotics started.</p>
  <p><strong>Workup:</strong> contrast computed tomography of orbits and paranasal sinuses,
  complete ocular examination with fundoscopy, Gram stain and culture of any drainage, complete
  blood count with differential, blood cultures. May need ear-nose-throat, oral and maxillofacial
  surgery, or infectious disease consults.
  <strong>Untreated &rarr; intracranial spread &rarr; meningitis or cavernous sinus
  thrombosis.</strong> Expect improvement in <b>24&ndash;48 hours</b>.</p>
  <p class="muted">Notes caveat: mild, clearly pre-septal disease with normal vision, pupils and
  painless full movements may be managed clinically <em>without</em> routine imaging.</p>

  <h3 class="sub" id="e2l1-disposition">1.11 &middot; Referral timing &mdash; explicit disposition</h3>
  <p class="muted"><b>Same caveat as 1.1</b> &mdash; this table comes from the section she called
  extra material and said she would not pull test questions from. Worth knowing; not examinable.</p>
  <table class="tbl">
    <tr><th>Urgency</th><th>Conditions</th></tr>
    <tr><td><b>EMERGENT &mdash; now</b></td><td>Chemical injury (irrigate first), open globe, acute angle closure, orbital cellulitis, endophthalmitis</td></tr>
    <tr><td><b>SAME DAY</b></td><td>Keratitis or corneal ulcer, anterior uveitis, scleritis, ocular herpes zoster ophthalmicus</td></tr>
    <tr><td><b>URGENT &mdash; 24&ndash;48 hours</b></td><td>Unexplained decreased vision, persistent pain or photophobia, atypical or worsening red eye</td></tr>
    <tr><td><b>ROUTINE</b></td><td>Uncomplicated conjunctivitis, chronic eyelid or ocular surface disease</td></tr>
  </table>
  <p><strong>Routine is only appropriate when ALL of these hold:</strong> acuity preserved, pupils
  and movements normal, cornea clear with no fluorescein uptake or infiltrate, no significant pain
  or photophobia, and reliable follow-up. Every assessment ends with a documented disposition and
  a safety net &mdash; acuity, key negatives, suspected diagnosis, urgency, destination, and
  explicit return precautions.</p>
  <button type="button" class="test-yourself-btn" style="--acc:#2d3f7a" onclick="window.openTestYourself('Test yourself &mdash; Common Ophthalmological Disorders', TEST_YOURSELF.ophthalmology)">Test yourself! &rarr;</button>
</section>
</main>"""

TEST_YOURSELF = '''  var TEST_YOURSELF = {
    ophthalmology: [
      {q:"Which single examination finding separates a chalazion from a hordeolum?",
       choices:["Size","Tenderness","Colour","Laterality"],correct:1,
       explain:"The hordeolum is tender and the chalazion is not. A chalazion is a STERILE meibomian obstruction; a hordeolum is an acute infection."},
      {q:"A pterygium differs from a pinguecula how?",
       choices:["It is yellow rather than fleshy","It extends onto the CORNEA","It is always bilateral","It is painful"],correct:1,
       explain:"Corneal involvement is the entire distinction. Pterodactyls fly into the cornea; penguins can't."},
      {q:"Which conjunctival finding points to a chlamydial or viral cause?",
       choices:["Papillae","Follicles","Chemosis","Purulent discharge"],correct:1,
       explain:"Follicles are pale at the surface and redder at the base. Papillae are the reverse, and point to bacterial or allergic disease."},
      {q:"Which bedside test confirms episcleritis?",
       choices:["Fluorescein under cobalt blue","2.5% phenylephrine, wait 15 minutes for blanching","Tonometry","Conjunctival scraping"],correct:1,
       explain:"Episcleral vessels blanch with phenylephrine, and can be moved with a cotton-tip applicator. Scleral vessels do neither."},
      {q:"What is the FIRST sign that scleritis is responding to treatment?",
       choices:["The violaceous hue fades","Decreased PAIN, even if the eye looks unchanged","Vision returns to normal","The discharge stops"],correct:1,
       explain:"This is flagged specifically, so an eye that still looks inflamed is not misread as treatment failure."},
      {q:"A contact lens wearer has a central epithelial defect with a white infiltrate. What is the next step?",
       choices:["Patch the eye and review in two days","Remove the lenses without patching and arrange SAME-DAY ophthalmology","Give a take-home topical anaesthetic","Start a topical corticosteroid"],correct:1,
       explain:"Microbial keratitis until proven otherwise. Never patch, never send home an anaesthetic, never start steroids."},
      {q:"Which corneal finding is PATHOGNOMONIC for herpes simplex?",
       choices:["A pseudodendrite","A true dendrite with terminal end bulbs","A ring infiltrate","A hypopyon"],correct:1,
       explain:"The true dendrite branches like a tree, has elevated edges and terminal end bulbs. The zoster pseudodendrite lacks all three."},
      {q:"What separates PRE-septal from POST-septal cellulitis on examination?",
       choices:["Fever","The eye itself: white with full painless movements, versus red with proptosis and restricted painful movement","Lid swelling","Presence of pain"],correct:1,
       explain:"Both have lid swelling, warmth and fever. Only post-septal disease involves the globe and its movements."},
      {q:"Which is EMERGENT rather than same-day?",
       choices:["Anterior uveitis","Orbital cellulitis","Scleritis","Corneal ulcer"],correct:1,
       explain:"Emergent: chemical injury, open globe, angle closure, orbital cellulitis, endophthalmitis. The others are same-day."},
      {q:"Untreated trachoma causes blindness by which chain?",
       choices:["Ulceration then perforation","Inflammation, lid scarring, entropion, trichiasis","Raised pressure then optic nerve damage","Neovascularisation then haemorrhage"],correct:1,
       explain:"Repeated chlamydial infection scars the lid, which turns it inward, which drives the lashes onto the cornea."}
    ],
  };'''

donor = open(DONOR, encoding="utf-8").read()
head = donor[:donor.index('<div class="layout wrap"')]
tail = donor[donor.index("</main>") + len("</main>"):]

ty_start = tail.index("var TEST_YOURSELF = {")
ty_end = tail.index("\n  };", ty_start) + len("\n  };")
tail = tail[:ty_start] + TEST_YOURSELF.lstrip() + tail[ty_end:]

# Exam 1 is TEAL. Exam 2 is INDIGO, so the two blocks are never confused.
for old, new in (("#17494b", "#2d3f7a"), ("#2c7b76", "#5566b5"), ("#0f3436", "#1b2450"),
                 ("#3c9c95", "#7b8ad0"), ("#1b2a2b", "#1e2233"), ("#8fd0c9", "#b9c2ee")):
    head = head.replace(old, new)

head = re.sub(r"<title>.*?</title>",
              "<title>Clinical Medicine and Surgery I &middot; Exam 2 &mdash; Study Guide</title>",
              head, count=1, flags=re.S)
head = re.sub(r"<header class=\"top\">.*?</header>",
  '<header class="top">\n'
  '  <h1>Clinical Medicine and Surgery I &middot; Exam 2 &mdash; Study Guide</h1>\n'
  '  <p>PAJ 5500 Clinical Medicine and Surgery I &middot; Class of 2028</p>\n'
  '  <p>Ophthalmology block &middot; further sections are added as each Exam 2 lecture is posted '
  '&middot; Instructional Objectives taken verbatim from the syllabus</p>\n'
  '</header>', head, count=1, flags=re.S)

body = BODY
body = body.replace("@@PINGPTER@@", figpair(
    "s027_1.jpg", "s027_2.jpg",
    "<b>Left, pinguecula</b> &mdash; the yellowish nodule stops at the limbus. "
    "<b>Right, pterygium</b> &mdash; the growth crosses onto the cornea. That crossing is the "
    "entire distinction.", 27))
body = body.replace("@@CELLULITIS@@", figpair(
    "s052_1.jpg", "s052_2.jpg",
    "<b>Left, pre-septal</b> &mdash; the lid is swollen and red but <b>the eye itself is white</b>, "
    "and movements are full and painless. <b>Right, post-septal</b> &mdash; the globe is involved. "
    "This is the single most useful visual discrimination in the block.", 52))
body = body.replace("@@HERPES@@", figpair(
    "s057_1.jpg", "s057_2.jpg",
    "<b>Left, herpes simplex</b> &mdash; a true dendrite: tree-branching, elevated edges, and "
    "<b>terminal end bulbs</b>. Pathognomonic. <b>Right, herpes zoster</b> &mdash; a "
    "pseudodendrite, which lacks all three.", 57))
body = body.replace("@@FLUSH@@", figone(
    "s054_1.jpg",
    "Ciliary flush &mdash; a ring of vessels radiating from the limbus around the cornea. This is "
    "the finding that rules OUT simple conjunctivitis.", 54))
assert "@@" not in body, "unfilled figure token"

html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + body + tail
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)

for fn in re.findall(r'src="%s/([^"]+)"' % IMGDIR, html):
    assert os.path.exists(os.path.join(os.path.dirname(OUT), IMGDIR, fn)), fn
for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li", "nav",
            "figure", "figcaption"):
    o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
    assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
assert "data-audio-dir" not in html, "audio dir must stay absent until mp3s exist"
assert "#17494b" not in html, "donor teal left in the Exam 2 guide"
print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
print("subsections: %d   figures: %d   test-yourself questions: %d"
      % (html.count('class="sub"'), html.count("<figure"), TEST_YOURSELF.count("{q:")))
