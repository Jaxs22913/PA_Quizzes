#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Physical Diagnosis 2 section 4 (Advanced ENT History and Examination).

BUILT FROM BOTH HALVES OF THE RECORDING plus the deck. Part 1 (58:55) runs the
ear through the tuning forks; part 2 (38:29) runs the nose, mouth, neck and
head. Part 2 contains NO scope cuts -- nothing was taken off the exam -- so the
quizzes built from part 1 stand. What it adds is emphasis and anatomy.

THE TUNING FORK BLOCK IS THE WEIGHTED ONE, and unusually the weighting is a
number. The video played in class: "the Weber and the Rinne tests are both high
yield ... the difference between sensorineural hearing loss and conductive
hearing loss is also high yield ... it will be THREE POINTS ON TEST DAY."

THE MODIFIED CENTOR SCORE IS IMAGE-ONLY. Slide 65's text is a single caption
line; the four criteria at one point each, the AGE adjustment, and the score
bands all live inside the picture. A text-only reading of this deck loses the
whole thing, which is the failure [[image_only_slides]] exists to catch.

BATES IS DECLARED TESTABLE AND IS NOT AVAILABLE. Slide 94 puts tables 7-1, 7-2,
7-4 and 7-19 through 7-26 in scope, plus the reading assignments. That is a
textbook, not a slide. The gap is STATED in the guide rather than papered over
with invented content -- and where the deck reproduces a Bates table on its own
slide, as it does for the vertigo comparison and the hearing loss summary, that
content is here in full.

Idempotent: fenced in <!--PD2L4--> and stripped before reinsert.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1")
GUIDE = os.path.join(DIR, "pd2-exam-1-study-guide.html")
IMG = "pd2-exam-1-l4-images"


def fig(slug, ext, caption, slide):
    path = os.path.join(DIR, IMG, "%s.%s" % (slug, ext))
    assert os.path.exists(path), "missing figure %s -- run extract_pd2_l4_figures.py" % slug
    return ('<figure class="fig"><img src="%s/%s.%s" loading="lazy" decoding="async" '
            'alt="Lecture 4 slide %d figure."><figcaption>%s '
            '<span class="cite">Slide %d</span></figcaption></figure>'
            % (IMG, slug, ext, slide, caption, slide))


BODY = """
<section class="deck" id="ent-exam">
  <h2 class="deck-title">4 &middot; Advanced ENT History and Examination</h2>
  <div class="io-box">
    <h3>Objectives</h3>
    <p class="tag">Advanced ENT History &amp; Exam</p>
    <ol>
      <li>Describe and identify the anatomical landmarks of the head, ear, nose, and throat.</li>
      <li>Demonstrate proficiency in performing a head, ears, nose, and throat physical examination.</li>
      <li>Define the elements in the medical history that aid in identifying abnormal conditions of the head, ears, nose, and throat.</li>
      <li>Define the elements of the physical examination that aid in identifying abnormal conditions of the head, ears, nose, and throat.</li>
      <li>Demonstrate appropriate physical examination techniques when differentiating between conductive and sensorineural hearing loss.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; with a number attached</span>
    <p><b>The tuning fork tests are worth three points.</b> The video played in class said it
    outright: <em>&ldquo;the Weber and the Rinne tests are both high yield &hellip; the difference
    between sensorineural hearing loss and conductive hearing loss is also high yield &hellip;
    <b>it will be three points on test day</b> if you dedicate the necessary amount of
    time.&rdquo;</em> Very little else in this course comes with a stated mark value.</p>
    <p><b>Two mnemonics were taught aloud, and both are worth keeping:</b></p>
    <ul>
      <li><b>&ldquo;Rinne is under the pinna.&rdquo;</b> The outside of the ear is the pinna; the
      Rinne fork goes on the <b>mastoid, under it</b>. So anything placed under the ear is Rinne.</li>
      <li><b>&ldquo;Weber tells you whether.&rdquo;</b> <em>&ldquo;See what I did there &mdash; I
      replaced the word <b>whether</b> with <b>Weber</b>.&rdquo;</em> Weber tells you
      <b>whether</b> it is the right ear or the left.</li>
    </ul>
    <p><b>And the lecturer added the half the video left out</b> [56:52]: the video worked the
    sensorineural case, so he supplied the conductive one &mdash; <em>&ldquo;if it&rsquo;s
    conductive it&rsquo;s going to go to the one that &hellip; is blocked.&rdquo;</em></p>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; The practical &mdash; name it while you do it</span>
    <p>He was explicit, twice, that the physical examination is graded on <b>naming the structure
    as you touch it</b>. On the node chains [26:18]: <em>&ldquo;I need for you to know when
    you&rsquo;re pressing preauricular &hellip; when you&rsquo;re telling me I&rsquo;m doing
    preauricular I need to see that. I need to see the cervical nodes. <b>I need to know where
    you&rsquo;re putting your finger.</b>&rdquo;</em> And on the inspect-and-palpate sequence
    [27:42]: <em>&ldquo;tenderness, deformity, any masses &mdash; learn those, memorise those,
    <b>you need to know them, because that&rsquo;s going to be part of your test</b>.&rdquo;</em></p>
    <p>Earlier, on pointing generally [25:40]: <em>&ldquo;make sure that you point to what it is
    &hellip; because that&rsquo;s how I&rsquo;m going to grade you. If you&rsquo;re just putting
    your hands all over the place, that doesn&rsquo;t mean anything.&rdquo;</em></p>
  </div>

  <h3 class="sub" id="l4-ear-history">4.1 &middot; The ear history</h3>
  <p>It opens with one question &mdash; <b>&ldquo;Have you had any trouble with your
  ears?&rdquo;</b> &mdash; and then splits four ways: <b>pain</b>, <b>discharge</b>,
  <b>hearing</b>, and the <b>vertigo and tinnitus</b> group.</p>
  <p><b>Pain is the one that misleads</b>, because the ear may be entirely normal. Ear pain is
  frequently <b>referred</b>, and the sources to ask about are the <b>temporomandibular
  joint</b>, the <b>teeth</b> and the <b>cervical spine</b> &mdash; carried by <b>cranial nerves
  V, VII, IX and X</b>. Four sensory nerves supplying one small structure is exactly why disease
  well away from the ear arrives as otalgia. He made the wider point on history technique here
  [5:32]: <em>&ldquo;the first answer is you don&rsquo;t go with the first answer. You&rsquo;ve
  got to keep asking&rdquo;</em> &mdash; and then the reason: <em>&ldquo;if you&rsquo;ve got the
  wrong history, that means you&rsquo;re going to do the wrong physical, wrong physical, wrong
  diagnosis, wrong diagnosis, wrong treatment.&rdquo;</em></p>
  <p>Also ask about <b>associated symptoms</b> &mdash; fever, sore throat, cough, upper
  respiratory infection &mdash; and keep <b>otitis media</b>, <b>otitis externa</b> and
  <b>Eustachian tube dysfunction</b> in mind as the local causes. The history structure is
  <b>OPPQRST</b>: onset, palliative, provoking, quality, radiation, site, timing.</p>
  <p><b>Discharge</b> is characterised by <b>colour, consistency and quantity</b>, and the
  possibilities are <b>cerumen, blood, water or purulent fluid</b>. It points to otitis externa,
  otitis media with perforation, or trauma and foreign bodies.</p>

  <h3 class="sub" id="l4-hearing-history">4.2 &middot; Hearing, tinnitus and &ldquo;dizziness&rdquo;</h3>
  <p><b>&ldquo;How is your hearing?&rdquo;</b> then <b>&ldquo;Do you have difficulty understanding
  people when they speak?&rdquo;</b> The second question is the useful one, because it separates
  volume from clarity:</p>
  <table class="tbl">
    <tr><th>What the patient reports</th><th>What it suggests</th></tr>
    <tr><td>Trouble <b>understanding</b> speech; others seem to <b>mumble</b></td><td><b>Sensorineural</b></td></tr>
    <tr><td><b>Worse</b> in noisy environments</td><td><b>Sensorineural</b></td></tr>
    <tr><td>Noisy environments <b>may help</b></td><td><b>Conductive</b></td></tr>
  </table>
  <p><b>Why noise helps in conductive loss</b> is worth understanding rather than memorising: the
  block attenuates the background along with everything else, while everyone around the patient
  raises their voice over that background. The speech-to-noise ratio actually improves.</p>
  <p><b>Ask about medications</b>: <b>aminoglycosides, aspirin, non-steroidal
  anti-inflammatories, quinine and furosemide</b>. All five are common, and none of them will be
  volunteered.</p>
  <p><b>Tinnitus is sound with no external source.</b> Unexplained tinnitus stands alone; tinnitus
  <b>with hearing loss and vertigo</b> is <b>M&eacute;ni&egrave;re disease</b>. <b>Vertigo</b> is
  the perception of rotation, spinning or tilting, and points to inner ear problems &mdash;
  labyrinthitis, cranial nerve VIII, benign positional vertigo, M&eacute;ni&egrave;re.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasised</span>
    <p><b>&ldquo;Dizziness&rdquo; means nothing until the patient explains it.</b> The deck calls
    it <em>very important to have the patient explain this term</em>, and it splits four ways:</p>
    <ol>
      <li><b>Vertigo</b> &mdash; spinning sensation</li>
      <li><b>Presyncope</b> &mdash; faint or lightheaded</li>
      <li><b>Disequilibrium</b> &mdash; unsteadiness or imbalance</li>
      <li><b>Psychiatric</b> &mdash; anxiety, depression, alcohol or other substances</li>
    </ol>
    <p>Four patients can use one word for four unrelated problems. Nothing else in the ear history
    turns on a single clarifying question this much.</p>
  </div>

  <h3 class="sub" id="l4-vertigo-table">4.3 &middot; The vertigo comparison</h3>
  <p>Read this table <b>down the duration column first</b>, then check hearing and tinnitus. The
  two columns together separate all six.</p>
  <table class="tbl">
    <tr><th>Type</th><th>Onset</th><th>Duration and course</th><th>Hearing</th><th>Tinnitus</th><th>Other</th></tr>
    <tr><td><b>Benign positional vertigo</b><br><span class="muted">peripheral</span></td><td>Sudden, on <b>rolling onto the affected side</b> or tilting the head up</td><td><b>Seconds to under a minute.</b> Lasts a few weeks; may recur</td><td><b>Not affected</b></td><td><b>Absent</b></td><td>Sometimes nausea, vomiting, nystagmus</td></tr>
    <tr><td><b>Vestibular neuronitis</b> (acute labyrinthitis)<br><span class="muted">peripheral</span></td><td>Sudden</td><td><b>Hours to two weeks.</b> May recur over 12&ndash;18 months</td><td><b>Not affected</b></td><td><b>Absent</b></td><td>Nausea, vomiting, nystagmus</td></tr>
    <tr><td><b>M&eacute;ni&egrave;re disease</b><br><span class="muted">peripheral</span></td><td>Sudden</td><td><b>Several hours to a day or more.</b> Recurrent</td><td><b>Sensorineural</b> &mdash; recurs, eventually progresses</td><td><b>Present, fluctuating</b></td><td><b>Pressure or fullness</b> in the affected ear; nausea, vomiting, nystagmus</td></tr>
    <tr><td><b>Drug toxicity</b><br><span class="muted">peripheral</span></td><td>Insidious or acute &mdash; <b>loop diuretics, aminoglycosides, salicylates, alcohol</b></td><td>May or may not be reversible; partial adaptation occurs</td><td><b>May be impaired</b></td><td>May be present</td><td>Nausea, vomiting</td></tr>
    <tr><td><b>Acoustic neuroma</b><br><span class="muted">peripheral</span></td><td>Insidious, from <b>cranial nerve VIII</b> compression</td><td>Variable</td><td><b>Impaired, ONE side</b></td><td><b>Present</b></td><td>May involve <b>cranial nerves V and VII</b></td></tr>
    <tr><td><b>Central vertigo</b></td><td>Often sudden &mdash; <b>brainstem lesion, atherosclerosis, multiple sclerosis, vertebrobasilar migraine, transient ischaemic attack</b></td><td>Variable but <b>rarely continuous</b></td><td><b>Not affected</b></td><td><b>Absent</b></td><td><b>Other brainstem deficits</b> &mdash; dysarthria, ataxia, crossed motor and sensory deficits</td></tr>
  </table>
  <p><b>Three things to take from the table.</b> First, <b>hearing is the great divider</b>: of the
  six, only M&eacute;ni&egrave;re, drug toxicity and acoustic neuroma touch it. Second,
  <b>positional vertigo is defined by how brief each episode is</b>, and the episode length and
  the illness length are different numbers &mdash; seconds for the attack, weeks for the
  condition. Third, <b>central vertigo has no ear symptoms and plenty of neurological ones</b>,
  which is the pattern rather than any single feature.</p>

  <h3 class="sub" id="l4-ear-exam">4.4 &middot; The ear examination</h3>
  <p><b>Inspect and palpate before the otoscope:</b> the <b>auricles</b>, the <b>mastoid</b>, and
  the <b>tragus</b>. Tenderness localises disease before anything enters the canal.</p>
  <p><b>Otoscopy technique</b>, and every element earns its place:</p>
  <table class="tbl">
    <tr><th>Step</th><th>Why</th></tr>
    <tr><td>Pull the auricle <b>up, back and away from the head</b></td><td>Straightens the canal. The view is only as good as the alignment</td></tr>
    <tr><td>Use the <b>LARGEST speculum that will fit</b></td><td>A small one is tempting, but it leaks &mdash; and insufflation needs a seal</td></tr>
    <tr><td><b>Ulnar aspect of the hand</b> contacts the patient</td><td>Anchors the instrument to the head, so a sudden movement takes the otoscope with it rather than into the canal</td></tr>
    <tr><td><b>Insufflate</b></td><td>Reduced mobility means <b>effusion</b> or a <b>thickened membrane</b></td></tr>
  </table>
  <p><b>Insufflation, done properly.</b> Check the otoscope for leaks <b>after</b> the speculum is
  attached: place a finger over the speculum tip and squeeze the bulb &mdash; you should feel the
  pressure build if there is no leak. Insert, confirm the seal, then apply <b>quick, firm but
  gentle</b> pressure and watch the membrane. Without a seal the test is not merely harder, it is
  <b>inaccurate</b>, and an immobile-looking drum may just be a leaking instrument.</p>
  <p><b>&ldquo;You have to see hundreds of normal before you see anything abnormal&rdquo;</b>
  [31:55]: <em>&ldquo;you&rsquo;ve got to get used to seeing the normal. This is what a normal
  looks like &hellip; and then the abnormal will hit you in the face.&rdquo;</em> He repeated it
  at the eardrum slide &mdash; <em>&ldquo;know what normal looks like &hellip; normal, normal,
  normal.&rdquo;</em></p>

  @@NORMALDRUM@@

  <h3 class="sub" id="l4-otoscopic">4.5 &middot; What you find in the canal and on the drum</h3>
  <p><b>In the canal.</b> Cerumen, and <b>foreign bodies</b> &mdash; the deck's list is
  Q-tips, beads, pencil lead, styrofoam, crayons, popcorn and tympanostomy tubes, under the
  heading <em>&ldquo;if it fits&hellip;&rdquo;</em>.</p>
  <table class="tbl">
    <tr><th>Finding</th><th>Appearance</th></tr>
    <tr><td><b>Acute otitis externa</b></td><td>Canal <b>swollen, narrow, moist, pale, TENDER</b>; may be erythematous</td></tr>
    <tr><td><b>Chronic otitis externa</b></td><td>Canal skin <b>thickened, red, ITCHY</b></td></tr>
    <tr><td><b>Perforation</b></td><td><b>Central</b> &mdash; does not extend to the margin. <b>Marginal</b> &mdash; involves the margin. Usually secondary to otitis media, and there may be drainage through it</td></tr>
    <tr><td><b>Tympanosclerosis</b></td><td><b>Hyaline deposit</b> in the membrane, after severe otitis media or a healed perforation, including grommet sites. <b>Usually not clinically significant</b></td></tr>
    <tr><td><b>Serous effusion</b></td><td><b>Amber</b> fluid, sometimes with <b>bubbles</b>. Follows an upper respiratory infection or a change in atmospheric pressure</td></tr>
    <tr><td><b>Otitis media</b></td><td><b>Red, landmarks LOST, BULGING</b>, with purulent effusion. <b>Streptococcus pneumoniae</b> and <b>Haemophilus influenzae</b></td></tr>
    <tr><td><b>Bullous myringitis</b></td><td><b>Painful haemorrhagic vesicles</b> on the membrane or canal. May be viral or bacterial</td></tr>
  </table>
  <p><b>Acute against chronic otitis externa is pain against itch</b>, and swelling against
  thickening. The distinction is easier from the history than from the picture.</p>
  <p><b>Bulging is graded, not binary.</b> The deck carries a four-panel series, and the useful
  thing about it is the middle two &mdash; a mildly bulging drum still has landmarks you can pick
  out, and the point at which they disappear is the point the effusion has become convincing.</p>

  @@BULGING@@

  <h3 class="sub" id="l4-forks">4.6 &middot; Hearing screening and the tuning fork tests</h3>
  <p><b>Whispered voice test.</b> Stand <b>two feet BEHIND</b> the patient &mdash; which removes
  lip reading &mdash; <b>occlude the ear not being tested</b>, and whisper a <b>three number or
  letter sequence twice</b>. <b>Normal is three or more of six correct; abnormal is four of six
  incorrect.</b> The other bedside screens are <b>finger rub</b> and a <b>watch</b>.</p>
  <table class="tbl">
    <tr><th></th><th>Conductive loss</th><th>Sensorineural loss</th></tr>
    <tr><td><b>Pathophysiology</b></td><td>External or middle ear disorder impairs conduction to the inner ear. Foreign body, otitis media, perforation, <b>otosclerosis of the ossicles</b></td><td>Inner ear disorder involving the <b>cochlear nerve</b> and impulse transmission to the brain. Loud noise, inner ear infection, trauma, acoustic neuroma, congenital and familial disorders, <b>ageing</b></td></tr>
    <tr><td><b>Usual age of onset</b></td><td>Childhood and young adulthood, <b>up to about 40</b></td><td><b>Middle or later years</b></td></tr>
    <tr><td><b>Canal and drum</b></td><td>Abnormality usually <b>VISIBLE</b> &mdash; <b>except in otosclerosis</b></td><td>Problem <b>not visible</b></td></tr>
    <tr><td><b>Effect on sound</b></td><td>Little effect. Hearing <b>seems to improve in a noisy environment</b>. <b>Voice remains SOFT</b>, because the inner ear and cochlear nerve are intact</td><td><b>Higher registers lost</b>, so sound may be distorted. Hearing <b>worsens in noise</b>. <b>Voice may be LOUD</b>, because hearing is difficult</td></tr>
    <tr><td><b>WEBER</b> (fork at vertex)</td><td>Lateralises to the <b>IMPAIRED</b> ear &mdash; room noise is not well heard, so detection of vibration improves</td><td>Lateralises to the <b>GOOD</b> ear &mdash; damage impairs transmission on the affected side</td></tr>
    <tr><td><b>RINNE</b> (meatus, then mastoid)</td><td><b>Bone &ge; air.</b> Vibration through bone <b>bypasses</b> the blocked external or middle ear to reach the cochlea</td><td><b>Air &gt; bone.</b> The damaged cochlea or nerve transmits poorly <b>however the vibration arrives</b>, so <b>the normal pattern prevails</b></td></tr>
  </table>
  <p><b>Voice volume is a feedback loop</b>, and it is the bedside sign people forget. A patient
  who cannot hear themselves speaks up; a patient whose cochlea is intact hears their own voice
  by bone conduction perfectly well and has no reason to.</p>
  <p><b>The Rinne result in sensorineural loss is the counterintuitive one.</b> Rinne compares two
  routes to the <b>same</b> cochlea. Damage the cochlea and both routes degrade together, so the
  ratio between them is unchanged &mdash; a &ldquo;normal&rdquo; Rinne in an ear that hears badly.
  That is not a failure of the test; it is the test working.</p>

  @@CONDUCTION@@

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Worked example from class</span>
    <p>Rinne on the right: heard <b>better in the air</b> &mdash; normal. Weber: heard <b>better
    in the right ear</b>. <b>Which ear has sensorineural loss?</b></p>
    <p><b>The LEFT.</b> The normal Rinne rules out a conductive problem on the right, and Weber
    lateralises <b>away</b> from a sensorineural lesion &mdash; so hearing it on the right puts
    the damage on the left.</p>
    <p><b>What the tuning forks CANNOT do</b>, which is on the slide and easy to skip: they do not
    distinguish <b>normal from bilateral sensorineural loss</b>, and they do not distinguish
    <b>normal from mixed conductive and sensorineural loss</b>. Both tests work by comparing
    &mdash; one side against the other, or one route against the other. A loss that is symmetrical,
    or that hits both routes, leaves the comparison looking normal.</p>
  </div>

  <h3 class="sub" id="l4-nose">4.7 &middot; The nose and sinuses</h3>
  <p><b>Anatomy first</b>, because the drainage explains the disease [0:16]. Three turbinates
  &mdash; <b>superior, middle and inferior</b> &mdash; and the <b>maxillary sinus drains at the
  middle turbinate</b>. The Eustachian tube opens into the same space, which is why
  <em>&ldquo;everything comes together, ear, nose and throat &hellip; that&rsquo;s why when you
  cry you get congestion.&rdquo;</em></p>
  <p>And the warning that goes with it [0:46]: <em>&ldquo;the roof of the mouth is the floor of
  your brain &hellip; anything that happened there can go up. So you have to be careful.
  <b>Any infection in this area, you have to be a little more aggressive.</b>&rdquo;</em></p>
  <p><b>History:</b> onset and duration, <b>sick contacts and recent travel</b>, <b>recent dental
  work</b> &mdash; because dental work can affect the <b>maxillary sinuses</b> sitting directly
  above the upper tooth roots &mdash; and <b>seasonal or environmental triggers</b> pointing to
  allergic rhinitis. <b>Facial pain or tenderness</b> points to sinusitis. Ask about
  <b>medications</b>: duration, efficacy, and specifically <b>rhinitis medicamentosa</b> and
  <b>cocaine</b>. Ask whether the <b>sense of smell</b> is affected.</p>
  <p><b>Epistaxis</b> is caused by digital trauma or other trauma, inflammation, dry mucosa,
  foreign body, or tumour. <b>Recurrent bleeding, or bleeding and bruising elsewhere, suggests a
  systemic problem</b> &mdash; one nosebleed is local until a pattern says otherwise.</p>
  <table class="tbl">
    <tr><th>Examination step</th><th>What you are looking for</th></tr>
    <tr><td><b>Patency</b></td><td>Occlude one nostril and breathe in. <b>UNILATERAL</b> obstruction &rarr; <b>foreign body, tumour, deviated septum</b></td></tr>
    <tr><td><b>Masses</b></td><td><b>Polyps</b> &mdash; associated with allergic rhinitis, <b>aspirin sensitivity</b>, asthma, chronic sinus infection, <b>cystic fibrosis</b>. Also cysts and tumours</td></tr>
    <tr><td><b>Symmetry and deformity</b></td><td>Deviated septum, perforated septum, trauma</td></tr>
    <tr><td><b>Discharge</b></td><td>Thick and purulent, thin and watery, or bloody. Note <b>odour</b></td></tr>
    <tr><td><b>Mucosa</b></td><td>Colour, swelling, bleeding, ulceration. <b>Red and swollen &rarr; VIRAL.</b> <b>Pale, bluish or red &rarr; ALLERGIC</b></td></tr>
    <tr><td><b>Septum</b></td><td>Perforation &mdash; from <b>trauma, surgery or drug use</b></td></tr>
    <tr><td><b>Palpation</b></td><td>Press <b>UP</b> on the frontal sinuses <b>avoiding the eyes</b>; press <b>UP</b> on the maxillary sinuses</td></tr>
    <tr><td><b>Transillumination</b></td><td>Dark room. <b>Frontal</b>: light up under the brow close to the nose. <b>Maxillary</b>: light down just below the inner corner of the eye, <b>mouth open</b>. Absence of glow &rarr; thickened mucosa or secretions. <b>NOT sensitive or specific</b></td></tr>
  </table>
  <p><b>Do not pull what you have not identified.</b> He told a story against the nose
  examination [6:05]: a lesion everyone had called a polyp, which imaging showed to be
  <b>brain tissue</b> coming through. <em>&ldquo;You need to know what you&rsquo;re looking at
  before you start pulling things. If you&rsquo;re not sure, you&rsquo;ve got to be
  careful.&rdquo;</em></p>

  @@POLYP@@

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasised</span>
    <p><b>Acute sinusitis &mdash; three statements, and the second is the one people get wrong.</b></p>
    <ol>
      <li><b>Local tenderness, pain, fever and nasal discharge are suggestive</b>, and purulent
      discharge is suggestive.</li>
      <li><b>The COLOUR of the discharge is NOT diagnostic.</b> He went further aloud
      [10:33]: purulent discharge <em>&ldquo;doesn&rsquo;t need to be there &hellip; it&rsquo;s
      not diagnostic&rdquo;</em>.</li>
      <li><b>Acute BACTERIAL sinusitis is unlikely with symptoms under seven days</b> &mdash;
      <em>&ldquo;less than seven days, it&rsquo;s not. It takes time to let it cook.&rdquo;</em></li>
    </ol>
  </div>

  @@SEPTUM@@

  <p><b>Septal haematoma</b> is the nose finding that cannot wait. <b>Injury disrupts the vessels
  and pulls the lining away from the cartilage</b>, so blood collects between the two. It
  <b>requires urgent drainage to prevent necrosis of the septal cartilage</b> &mdash; the
  cartilage has no blood supply of its own and depends entirely on the lining that has just been
  stripped off it. His rule was broader than the nose [11:36]: <em>&ldquo;any time you have a
  septal haematoma &mdash; anywhere, in an ear, in the nose, whatever &mdash; <b>that blood has to
  come out</b>.&rdquo;</em></p>
  <p><b>A deviated septum</b> may be entirely asymptomatic; he demonstrated pressing on an obvious
  external deviation with no obstruction behind it. What matters is airflow, not appearance.</p>

  <h3 class="sub" id="l4-oral">4.8 &middot; The oral cavity</h3>
  <p><b>Anatomy, named in order</b> [13:10]: <b>medial incisor, lateral incisor, canine,
  premolars, molars</b>; then the <b>hard palate</b>, the <b>soft palate</b> and <b>uvula</b>, the
  <b>tonsils</b> between the <b>anterior and posterior pillars</b>, the <b>pharynx</b> behind, and
  the <b>buccal mucosa</b>.</p>
  <p><b>History:</b> sore throat &mdash; and here the <b>Centor rule</b> enters. Also <b>sore
  tongue</b> (aphthous ulcers; <b>nutritional deficiency if sore AND smooth</b>), <b>bleeding
  gums</b> (gingivitis), <b>hoarseness</b> (viral laryngitis, overuse, <b>laryngeal nerve
  damage</b>, reflux, smoking), <b>swollen glands or lumps</b> in the neck, and <b>tobacco and
  alcohol use</b>.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; two courses asked for it</span>
    <p><b>The four Centor criteria</b>, one point each:</p>
    <ol>
      <li><b>Fever</b> &mdash; temperature above 100.4&deg;F (38&deg;C)</li>
      <li><b>Tonsillar exudates</b> or swelling</li>
      <li><b>Swollen and tender anterior cervical nodes</b></li>
      <li><b>ABSENCE of cough</b></li>
    </ol>
    <p><b>Three are things present and one is a thing absent</b>, which is the half people
    misremember. A cough points <b>toward</b> a viral cause, so its absence is what scores.</p>
    <p><b>The MODIFIED score adds age</b>, and this lives only inside the slide's picture &mdash;
    the slide text is a single caption line, so a text-only reading of the deck loses it
    entirely:</p>
    <table class="tbl">
      <tr><th>Age</th><th>Points</th></tr>
      <tr><td>3 to 14 years</td><td><b>+1</b></td></tr>
      <tr><td>15 to 44 years</td><td>0</td></tr>
      <tr><td>45 years and older</td><td><b>&minus;1</b></td></tr>
    </table>
    <p><b>The score maps to a risk of group A beta-haemolytic streptococcal pharyngitis:</b>
    score <b>&le;0 &rarr; 1&ndash;2.5%</b>; <b>1 &rarr; 5&ndash;10%</b>;
    <b>2 &rarr; 11&ndash;17%</b>; <b>3 &rarr; 28&ndash;35%</b>; <b>&ge;4 &rarr; 51&ndash;53%</b>.
    A score of 0 or less needs <b>no further testing or antibiotics</b>; the middle of the range
    goes to <b>throat culture or rapid antigen detection</b>; and <b>&ge;4</b> is where empiric
    treatment is considered.</p>
  </div>

  @@CENTOR@@

  <table class="tbl">
    <tr><th>Structure</th><th>What to inspect, and what it means</th></tr>
    <tr><td><b>Lips</b></td><td>Colour, texture, cracks, sores. <b>Angular cheilitis</b> at the corners; <b>angioedema</b>; <b>herpes simplex</b></td></tr>
    <tr><td><b>Mucosa, tonsils, pharynx</b></td><td><b>Erythema, exudates, ulcerations, lesions.</b> The posterior pharynx may need a <b>tongue blade</b></td></tr>
    <tr><td><b>Uvula and soft palate</b></td><td><b>Failure to rise with deviation of the uvula to the OPPOSITE side &rarr; cranial nerve X paralysis</b></td></tr>
    <tr><td><b>Dentition</b></td><td>Caries, erosions. <b>Look UNDER dentures</b> for ulcers and lesions</td></tr>
    <tr><td><b>Tongue</b></td><td>Texture, colour, lesions. <b>Smooth, beefy red &rarr; vitamin B12 deficiency.</b> <b>Cancers: lateral border or undersurface</b>, indurated red or white, <b>males over 50</b>. <b>Geographic tongue is benign.</b> <b>Asymmetric protrusion &rarr; cranial nerve XII lesion</b></td></tr>
    <tr><td><b>Palpation</b></td><td>Floor of mouth; then the tongue &mdash; <b>hold it with gauze in one hand and palpate with the other, then SWITCH HANDS</b> for the opposite side</td></tr>
  </table>
  <p><b>Switching hands is not fussiness</b>, it is the only way to reach both lateral borders
  properly &mdash; and the lateral border and undersurface are exactly where the cancers are.</p>
  <p><b>Pharyngitis:</b> streptococcal gives <b>erythematous tonsils</b>, often with exudate.
  <b>Candidal</b> pharyngitis is its own picture. <b>Necrotising ulcerative gingivitis</b>
  &mdash; <b>Vincent's angina</b>, <b>trench mouth</b> &mdash; he described from the door
  [23:43]: <em>&ldquo;those people open their mouth back there and you can smell them over here,
  that&rsquo;s how bad it is &hellip; the bacteria keep growing and it&rsquo;s actually destroying
  tissue as it goes.&rdquo;</em> From <b>poor dental hygiene</b>, and drug use. <b>Aphthous
  ulcers</b> and <b>torus palatinus</b> &mdash; a benign midline bony growth on the hard palate
  &mdash; round out the findings.</p>

  @@STREP@@

  <h3 class="sub" id="l4-neck">4.9 &middot; The neck, the thyroid and the head</h3>
  <p><b>The node chains, in the order to palpate them:</b> preauricular, postauricular, occipital,
  tonsillar, submandibular, submental, superficial (anterior) cervical, posterior cervical, deep
  cervical, supraclavicular. Use the <b>pads of the index and middle fingers</b>. Following a
  fixed route is what stops one being missed &mdash; and on the practical, <b>each one has to be
  named as it is palpated</b>.</p>

  @@NODES@@

  <table class="tbl">
    <tr><th>Node finding</th><th>What it means</th></tr>
    <tr><td><b>Round or ovoid, smooth, mobile, non-tender</b></td><td><b>Normal</b></td></tr>
    <tr><td><b>Tender</b></td><td><b>Inflammation</b></td></tr>
    <tr><td><b>Hard or fixed</b></td><td><b>Malignancy</b></td></tr>
    <tr><td><b>Enlarged supraclavicular node on the LEFT</b></td><td><b>Metastasis from an abdominal or thoracic malignancy</b></td></tr>
    <tr><td><b>Generalised</b></td><td>Human immunodeficiency virus, Epstein-Barr virus, <b>lymphoma, leukaemia, sarcoidosis</b></td></tr>
  </table>
  <p>The left supraclavicular node is the one worth knowing cold: it drains territory a long way
  from the neck, so finding one there redirects the entire search.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Emergency &mdash; airway</span>
    <p><b>Submandibular swelling and erythema &mdash; Ludwig's angina</b>, a <b>cellulitis of the
    floor of the mouth</b>. <b>Life threatening, and the reason is the AIRWAY.</b></p>
    <p>He walked it through [28:16]: <em>&ldquo;that&rsquo;s an emergency &mdash; basically an
    infection of the mouth, usually the lower, from teeth or something that went down. You&rsquo;ve
    got the floor of the mouth, infection is right here, now it&rsquo;s spreading this way and
    <b>it spreads fast</b> &hellip; it cannot stay in the body, it has to come out &hellip;
    life-threatening, airway. I saw a couple of those in the emergency room &mdash; you can see it
    spreading, you can see it moving, <b>you have to work with it quickly</b>.&rdquo;</em></p>
  </div>

  @@LUDWIG@@

  <p><b>The trachea</b> is checked for <b>deviation</b> &mdash; masses, atelectasis, or a large
  pneumothorax.</p>
  <p><b>The thyroid</b>, found from the <b>cricoid cartilage</b> as the landmark [26:43], and the
  three-way split on diffuse enlargement turns on <b>texture alone</b>:</p>
  <table class="tbl">
    <tr><th>Finding</th><th>Suggests</th></tr>
    <tr><td>Diffuse and <b>SOFT</b></td><td><b>Graves disease</b></td></tr>
    <tr><td>Diffuse and <b>FIRM</b></td><td><b>Hashimoto thyroiditis</b></td></tr>
    <tr><td>Diffuse and <b>TENDER</b></td><td><b>Thyroiditis</b></td></tr>
    <tr><td><b>Endemic</b> goitre</td><td><b>Iodine deficiency</b></td></tr>
    <tr><td><b>Single</b> nodule</td><td>Cyst or tumour</td></tr>
    <tr><td><b>Multinodular</b> enlargement</td><td>Metabolic process; <b>risk of malignancy with a family history</b></td></tr>
  </table>
  <p><b>The head.</b> History is <b>OPPQRST</b> again, and the headache patterns matter:
  <b>migraine and tension are EPISODIC</b>; <b>migraine and cluster are UNILATERAL</b> &mdash;
  migraine is in both lists, so the two features have to be read together. <b>Sudden and severe
  &rarr; subarachnoid haemorrhage.</b> <b>New, progressive and persistent &rarr; mass.</b> Also
  consider <b>meningitis</b>.</p>
  <p><b>On examination:</b> facial swelling or characteristic facies; lumps, rashes, hair loss,
  lesions, scars; <b>lice</b>; <b>fine hair &rarr; hyperthyroidism, coarse hair &rarr;
  hypothyroidism</b>; <b>seborrhoeic dermatitis, psoriasis, atypical naevi, actinic keratosis</b>;
  symmetry, involuntary movements, oedema; tenderness and integrity; and <b>size</b> &mdash;
  <b>enlarged in hydrocephalus and Paget disease</b>, <b>small in microcephaly</b>.</p>

  <div class="note">
    <p><b>One gap, named rather than hidden.</b> The deck declares <b>Bates tables 7-1, 7-2, 7-4
    and 7-19 through 7-26 testable</b>, along with the material in the reading assignments. Those
    are a textbook, and nothing in this guide is invented from them &mdash; everything here comes
    from the slides or the recording. <b>Where the deck reproduces a Bates table on its own
    slide</b>, as it does for the vertigo comparison and the hearing loss summary, <b>that content
    is above in full</b>. For the rest, the tables are worth opening directly: 7-19 covers lumps
    on or near the ear, 7-22 the lips, 7-23 the mouth and pharynx, 7-25 the tongue, and 7-26 the
    thyroid.</p>
  </div>

  <button type="button" class="test-yourself-btn" style="--acc:#4a5c24" onclick="window.openTestYourself('Test yourself &mdash; ENT History &amp; Examination', TEST_YOURSELF.ent)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>PD II ENT 2026.pptx</em> (created by Megan B. Finck,
  MMS, PA-C; updated and presented by Rob Gray, DMSc, MMS, PA-C), Slides 1&ndash;95, and the
  lecture of 3 September 2026. Figures are reproduced from the lecture slides and each is cited
  to its slide.</footer>
</section>
"""

TOC = """  <a class="top-link" href="#ent-exam">4 &middot; Advanced ENT History &amp; Exam</a>
  <a class="sub-link" href="#l4-ear-history">4.1 The ear history</a>
  <a class="sub-link" href="#l4-hearing-history">4.2 Hearing, tinnitus &amp; dizziness</a>
  <a class="sub-link" href="#l4-vertigo-table">4.3 The vertigo comparison</a>
  <a class="sub-link" href="#l4-ear-exam">4.4 The ear examination</a>
  <a class="sub-link" href="#l4-otoscopic">4.5 Canal &amp; drum findings</a>
  <a class="sub-link" href="#l4-forks">4.6 Screening &amp; tuning forks</a>
  <a class="sub-link" href="#l4-nose">4.7 The nose &amp; sinuses</a>
  <a class="sub-link" href="#l4-oral">4.8 The oral cavity</a>
  <a class="sub-link" href="#l4-neck">4.9 Neck, thyroid &amp; head</a>
"""

TESTS = """    ent: [
      {q:"Rinne on the right is normal. Weber lateralises to the right. Which ear has sensorineural loss?",
       o:["The LEFT","The right","Neither — this is normal","Both"],a:0,
       why:"A normal Rinne rules out conductive loss on the right, and Weber lateralises AWAY from a sensorineural lesion — so hearing it on the right puts the damage on the left."},
      {q:"Which way does Weber lateralise in unilateral CONDUCTIVE loss, and why?",
       o:["To the IMPAIRED ear — the block screens out room noise, so the bone-conducted tone has that ear to itself",
          "To the GOOD ear — the impaired ear transmits nothing",
          "It does not lateralise in conductive loss",
          "To whichever ear was tested first"],a:0,
       why:"This is the half the class video left implicit and the lecturer supplied: conductive goes TOWARD the blocked side."},
      {q:"Why is the Rinne \\u201cnormal\\u201d in sensorineural hearing loss?",
       o:["Rinne compares two routes to the SAME cochlea, and the damage degrades both equally",
          "The inner ear favours bone conduction when damaged",
          "Sensorineural loss spares air conduction",
          "The test is invalid in sensorineural loss"],a:0,
       why:"The ratio survives because both routes end at the same damaged cochlea. That is the test working, not failing."},
      {q:"Which two situations can the tuning fork tests NOT distinguish?",
       o:["Normal from BILATERAL sensorineural loss, and normal from MIXED loss",
          "Conductive from sensorineural loss","Right-sided from left-sided loss",
          "Presbycusis from noise-induced loss"],a:0,
       why:"Both tests work by comparing — side against side, or route against route. A symmetrical loss leaves the comparison looking normal."},
      {q:"A patient's own voice is unusually LOUD. Which loss, and why?",
       o:["Sensorineural — they cannot hear themselves, so they raise their voice",
          "Conductive — the middle ear amplifies their own voice",
          "Either; voice volume does not distinguish them",
          "Neither; this suggests a psychiatric cause"],a:0,
       why:"Voice volume is a feedback loop. In conductive loss the cochlea is intact, bone conduction carries their own voice fine, and the voice stays SOFT."},
      {q:"Which type of hearing loss usually shows a visible abnormality on otoscopy, and what is the exception?",
       o:["Conductive is usually visible, EXCEPT otosclerosis; sensorineural is not visible",
          "Sensorineural is usually visible; conductive is not","Both are usually visible",
          "Conductive is always visible, no exception"],a:0,
       why:"Otosclerosis is the conductive cause hiding behind a normal-looking drum, which is exactly why it catches people out."},
      {q:"Vertigo on rolling over in bed, lasting under a minute, hearing unaffected. Which is it?",
       o:["Benign positional vertigo","M\\u00e9ni\\u00e8re disease","Vestibular neuronitis","Acoustic neuroma"],a:0,
       why:"Seconds plus a positional trigger plus intact hearing. M\\u00e9ni\\u00e8re runs hours WITH hearing loss; neuronitis runs hours to two weeks."},
      {q:"Insidious vertigo, hearing impaired on ONE side, tinnitus present, cranial nerves V and VII possibly involved.",
       o:["Acoustic neuroma","M\\u00e9ni\\u00e8re disease","Central vertigo","Drug toxicity"],a:0,
       why:"Unilateral hearing loss plus the neighbouring cranial nerves is the signature — the tumour sits where V and VII run close by."},
      {q:"What are the four Centor criteria?",
       o:["Fever, tonsillar exudates, swollen anterior cervical nodes, and ABSENCE of cough",
          "Fever, tonsillar exudates, swollen anterior cervical nodes, and PRESENCE of cough",
          "Fever, sore throat, headache and myalgia",
          "Fever, trismus, uvular deviation and drooling"],a:0,
       why:"Three present and one absent. A cough points toward a viral cause, so its absence is what scores."},
      {q:"In the MODIFIED Centor score, how does age change the total?",
       o:["3–14 adds a point; 15–44 adds nothing; 45 and over SUBTRACTS a point",
          "Age adds a point at every band","Age subtracts a point at every band",
          "Age is not part of the modified score"],a:0,
       why:"Streptococcal pharyngitis is a disease of children, so being older argues against it. This scoring lives only inside the slide's picture, not its text."},
      {q:"Submandibular swelling and erythema with cellulitis of the floor of the mouth. What is the danger?",
       o:["Ludwig's angina — the AIRWAY","Ludwig's angina — mediastinal spread only",
          "Peritonsillar abscess — rupture","A submandibular stone — infection"],a:0,
       why:"The swelling pushes the floor of the mouth and tongue up and back. It spreads fast, and the airway is why it cannot wait."},
      {q:"An enlarged supraclavicular node on the LEFT suggests what?",
       o:["Metastasis from an abdominal or thoracic malignancy","Scalp infection",
          "Dental infection","Tonsillitis"],a:0,
       why:"It drains territory a long way from the neck, so finding one there redirects the whole search."},
      {q:"A diffusely enlarged thyroid that is FIRM. Which condition?",
       o:["Hashimoto thyroiditis","Graves disease","Thyroiditis","Multinodular goitre"],a:0,
       why:"Diffuse enlargement splits on texture alone: soft is Graves, firm is Hashimoto, tender is thyroiditis."},
      {q:"Under what symptom duration is acute BACTERIAL sinusitis unlikely?",
       o:["Less than seven days","Less than three days","Less than four weeks","Less than twelve weeks"],a:0,
       why:"\\u201cIt takes time to let it cook.\\u201d And note the companion rule: the COLOUR of the discharge is not diagnostic."},
      {q:"Why does a septal haematoma need urgent drainage?",
       o:["To prevent necrosis of the septal cartilage","To prevent spread into the orbit",
          "To prevent airway obstruction","To prevent secondary sinusitis"],a:0,
       why:"The cartilage has no blood supply of its own — it depends on the lining the haematoma has just stripped away."},
      {q:"The uvula deviates to one side and the palate fails to rise. Which nerve, and which way does it deviate?",
       o:["Cranial nerve X — the uvula deviates AWAY from the paralysed side",
          "Cranial nerve XII — toward the paralysed side",
          "Cranial nerve IX — toward the lesion","Cranial nerve VII — no consistent direction"],a:0,
       why:"The working side pulls unopposed, so the uvula points away from the lesion. Asymmetric TONGUE protrusion is the XII sign."}
    ],
"""

FIGS = {
    "@@NORMALDRUM@@": ("normal-drum", "png",
        "A normal tympanic membrane. <b>&ldquo;You have to see hundreds of normal before you see "
        "anything abnormal&rdquo;</b> &mdash; find the handle of the malleus and the cone of light "
        "here, so you notice when they are missing.", 27),
    "@@BULGING@@": ("bulging-series", "png",
        "Bulging is graded, not binary: <b>A normal, B mild, C moderate, D severe</b>, from middle "
        "ear effusion. Watch the landmarks disappear as it progresses &mdash; that is the "
        "transition that makes the effusion convincing.", 32),
    "@@CONDUCTION@@": ("conduction", "png",
        "The two routes the tuning fork tests compare. <b>Air conduction</b> goes through canal, "
        "drum and ossicles; <b>bone conduction</b> goes straight through the skull, bypassing all "
        "of it. Conductive loss blocks one route; sensorineural loss degrades what lies beyond "
        "both.", 5),
    "@@POLYP@@": ("polyp", "png",
        "A nasal polyp (<b>P</b>) between the septum (<b>S</b>) and an allergic-looking inferior "
        "turbinate (<b>T</b>). Seeing the two side by side is the point &mdash; a boggy turbinate "
        "mistaken for a polyp is the common error.", 59),
    "@@SEPTUM@@": ("septum", "png",
        "Basal view of a caudal septal deviation. The external appearance can be striking with "
        "little obstruction behind it, and the reverse is also true &mdash; test patency rather "
        "than trusting the profile.", 56),
    "@@CENTOR@@": ("centor", "png",
        "<b>The modified Centor score in full.</b> Four criteria at one point each, the age "
        "adjustment, and what each score band means. <b>This slide&rsquo;s text is a single "
        "caption line</b> &mdash; the entire rule lives inside this picture.", 65),
    "@@STREP@@": ("strep", "png",
        "Erythematous tonsils in group A streptococcal pharyngitis. Redness and exudate score on "
        "Centor, but the picture alone does not settle it &mdash; that is what the rule is for.", 72),
    "@@NODES@@": ("nodes", "png",
        "The neck node chains, with external (red) and internal (blue) drainage. Learn the route, "
        "because on the practical each chain has to be <b>named as it is palpated</b>.", 79),
    "@@LUDWIG@@": ("ludwig", "png",
        "Ludwig&rsquo;s angina &mdash; anterior neck oedema and early cellulitis. It spreads fast "
        "and downward, and the airway is the reason it is an emergency.", 83),
}


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for o, cl in (("<!--PD2L4-->", "<!--/PD2L4-->"), ("<!--PD2TOC4-->", "<!--/PD2TOC4-->"),
                  ("<!--PD2TY4-->", "<!--/PD2TY4-->")):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(cl), "", src, flags=re.S)

    body = BODY
    for token, (slug, ext, cap, slide) in FIGS.items():
        assert token in body, "figure token %s unused" % token
        body = body.replace(token, fig(slug, ext, cap, slide))
    assert "@@" not in body, "unfilled figure token"

    assert "TEST_YOURSELF.ent" in body, (
        "this section registers a TEST_YOURSELF.ent bank but has no button that opens "
        "it -- four guides shipped with unreachable banks before this check existed")

    # The three things that would make this section worth less than the deck it
    # came from, if any of them were dropped.
    for needle, what in (("three points on test day", "the stated mark value on the tuning forks"),
                         ("45 years and older", "the modified Centor age adjustment, which is "
                          "image-only and lost on a text-only read"),
                         ("Bates tables 7-1", "the statement of what this guide does NOT cover")):
        assert needle in body, "%s was dropped" % what

    j = src.index("</main>")
    src = src[:j] + "<!--PD2L4-->" + body + "<!--/PD2L4-->\n\n" + src[j:]
    k = src.rindex("</nav>")
    src = src[:k] + "<!--PD2TOC4-->\n" + TOC + "<!--/PD2TOC4-->\n" + src[k:]
    m = src.index("var TEST_YOURSELF = {")
    m = src.index("\n", m) + 1
    src = src[:m] + "<!--PD2TY4-->\n" + TESTS + "<!--/PD2TY4-->\n" + src[m:]

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li",
                "figure", "figcaption", "b", "em", "i", "span"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for fn in re.findall(r'src="%s/([^"]+)"' % IMG, body):
        assert os.path.exists(os.path.join(DIR, IMG, fn)), fn

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 4: %d subsections, %d figures, %d flagged blocks, "
          "%d test-yourself questions"
          % (body.count('class="sub"'), body.count("<figure"),
             body.count('prof-flag-label'), TESTS.count("{q:")))


if __name__ == "__main__":
    main()
