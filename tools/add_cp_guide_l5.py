#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Clinical Pathophysiology I section 5 (ENT Pathophysiology).

Instructional Objectives are quoted VERBATIM from slide 2, per
[[guide_verbatim_io_rule]], including the em dashes and the objectives' own
numbering.

THREE PLACES THE DECK AND THE LECTURER DISAGREE, and each is handled the same
way -- record both, say which one to answer with, per [[slides_only_grounding]]:

  1. Slide 17 calls labyrinthine vertigo EPISODIC. He corrected it aloud, twice,
     at [33:05] and [34:17]: "Classic symptoms is continuous, not episodic
     vertigo." He also owned the error -- "I don't know, I did write that."
     The correction wins, because he made it about his own slide deliberately
     and repeated it.
  2. Slide 21 says nasal polyps are "Type 2 Inflammation". At [40:01] he stopped
     to fix it: "I meant to put T helper cell type 2 allergic inflammation. Very
     important." Then immediately cut it from scope: "I'm not gonna ask you
     about that, but just so you know."
  3. At [46:41] he said vocal cord polyps "are usually bilateral" and corrected
     himself inside the same breath to "Unilateral lesions". The slide says
     unilateral and the slide's own picture shows unilateral. The slide wins --
     this is the ordinary case where the deck is authoritative over the audio.

SCOPE CUTS HE MADE ALOUD are flagged, not deleted. The otitis media organisms
are "not really for my exam, but like board exams" [23:27]; allergic rhinitis is
"plain vanilla" and "I don't wanna ask about this" [39:48]. They stay in the
guide because they are still on the slides and still on PANCE.

Idempotent: fenced in <!--CPL5--> and stripped before reinsert.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
GUIDE = os.path.join(DIR, "cp-exam-1-study-guide.html")
IMG = "cp-exam-1-l5-images"


def fig(slug, ext, caption, slide):
    path = os.path.join(DIR, IMG, "%s.%s" % (slug, ext))
    assert os.path.exists(path), "missing figure %s -- run extract_cp_l5_figures.py" % slug
    return ('<figure class="fig"><img src="%s/%s.%s" decoding="async" '
            'alt="Lecture 5 slide %d figure."><figcaption>%s '
            '<span class="cite">Lecture 5 &middot; Slide %d</span></figcaption></figure>'
            % (IMG, slug, ext, slide, caption, slide))


BODY = """
<section class="deck" id="ent-pathophys">
  <h2 class="deck-title">5 &middot; ENT Pathophysiology</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">ENT Pathophysiology</p>
    <ol>
      <li>Review the anatomy of the ear, nose, neck and throat system.</li>
      <li>Review the ear, nose, neck, and throat pathology.</li>
      <li>Describe the molecular mechanisms of common disorders of ear, nose, neck, and throat.</li>
      <li>Differentiate the pathogenesis of vertigo and dizziness.</li>
      <li>Compare and contrast the pathophysiological processes of hearing deficits.</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; stated</span>
    <p><b>Vertigo is the weighted topic and he said so outright.</b> At [25:28]:
    <em>&ldquo;if you understand the etiology of vertigo versus dizziness, like any different
    types of vertigo, remember those things, because I think on my board exams, a third of my
    neurology questions were vertigo related. <b>So know this, know these things.</b>&rdquo;</em>
    Four peripheral causes, and they separate on three axes only: <b>how long the vertigo
    lasts</b>, <b>whether hearing goes with it</b>, and <b>whether a virus came first</b>.</p>
    <p><b>He also narrowed it:</b> <em>&ldquo;We are more interested for this lecture on
    peripheral vertigo&rdquo;</em> [29:19]. Central vertigo is here so you can exclude it.</p>
    <p><b>And he cut scope twice.</b> The otitis media organisms are <em>&ldquo;not really for
    my exam, but like board exams&rdquo;</em> [23:27]. Allergic rhinitis is <em>&ldquo;plain
    vanilla &hellip; I don&rsquo;t wanna ask about this&rdquo;</em> [39:48]. Both are still on
    the slides and both are still on PANCE, so neither has been removed &mdash; but if you are
    triaging the night before, they go last.</p>
  </div>

  <h3 class="sub" id="l5-anatomy">5.1 &middot; Objectives 1 &amp; 3 &mdash; Anatomy and auditory transduction</h3>
  <p>The ear is three compartments with three different jobs, and almost every disease in this
  lecture is a failure of one of them. The <b>external ear</b> &mdash; auricle and canal &mdash;
  captures and concentrates acoustic waves and localises sound; ceruminous glands line it and the
  outer third carries protective hair follicles. The <b>middle ear is air-filled</b>, which is the
  single fact that makes otitis media and Eustachian tube dysfunction make sense: the tympanic
  membrane vibrates, the malleus, incus and stapes amplify, and the Eustachian tube equalises
  pressure. The <b>inner ear</b> holds the cochlea, which converts fluid displacement into neural
  signal at the organ of Corti, and the vestibule and semicircular canals, which hold dynamic
  rotational equilibrium.</p>

  @@EARANATOMY@@

  <p><b>The transduction chain, in the order the slide gives it.</b> Follow it once and four
  later diseases become obvious:</p>
  <ol>
    <li><b>Stapes vibration at the oval window</b> generates pressure waves in the fluid-filled
    scala vestibuli, displacing endolymph in the cochlear duct.</li>
    <li><b>Shearing force.</b> Basilar membrane displacement bends the stereocilia against the
    <b>rigid tectorial membrane</b>. The rigidity is the point &mdash; the cilia are bent because
    one end moves and the other does not.</li>
    <li><b>Ion depolarisation.</b> That mechanical deflection <b>opens tip-link channels</b>,
    permitting rapid influx from endolymph into the hair cells.</li>
    <li><b>Neurotransmission.</b> Depolarisation triggers voltage-gated channels, releasing
    <b>glutamate onto cranial nerve VIII</b> fibres.</li>
  </ol>
  <p>Read that chain backwards and you have the map of hearing loss. Break step 1 and you get
  <b>conductive</b> loss. Break steps 2 to 4 and you get <b>sensorineural</b> loss. Nothing else
  in this lecture changes that division.</p>

  @@COCHLEA@@

  <h3 class="sub" id="l5-hearing">5.2 &middot; Objective 5 &mdash; Conductive against sensorineural loss</h3>
  <table class="tbl">
    <tr><th>Parameter</th><th>Conductive hearing loss</th><th>Sensorineural hearing loss</th></tr>
    <tr><td>Primary anatomic site</td><td>External or middle ear</td><td>Inner ear (cochlea), or cranial nerve VIII and central pathways</td></tr>
    <tr><td>Pathophysiology</td><td>Defective sound wave transmission to the oval window</td><td>Destruction of hair cells or auditory nerve fibres</td></tr>
    <tr><td><b>Weber</b> tuning fork</td><td>Lateralises to the <b>AFFECTED</b> ear</td><td>Lateralises to the <b>UNAFFECTED</b> ear</td></tr>
    <tr><td><b>Rinne</b> tuning fork</td><td><b>Bone &gt; air</b> conduction (abnormal)</td><td><b>Air &gt; bone</b> conduction (normal ratio)</td></tr>
    <tr><td>Common causes</td><td>Cerumen impaction, otosclerosis, otitis media, tympanic membrane perforation</td><td>Presbycusis, ototoxic drugs, noise trauma, acoustic neuroma</td></tr>
  </table>
  <p><b>The Weber result is the one people invert.</b> It goes to the bad ear in conductive loss,
  which feels wrong until you see why: the blockage stops competing room noise from reaching that
  cochlea, so the bone-conducted tone has the ear to itself and sounds louder there. In
  sensorineural loss the cochlea itself is damaged, so the tone is simply heard better on the
  side that still works. He walked the class through both tests live [5:02&ndash;6:48]: Weber on
  top of the head, Rinne first at the ear and then on the mastoid.</p>

  <p><b>Conductive loss has exactly four core mechanisms</b>, and every cause on the slide is one
  of them. Learn the mechanism and the examples come free:</p>
  <table class="tbl">
    <tr><th>Mechanism</th><th>What it does</th><th>Examples</th></tr>
    <tr><td><b>1. Obstruction</b></td><td>Physical blockage preventing sound penetrating down the canal</td><td>Impacted cerumen, foreign bodies, canal exostoses</td></tr>
    <tr><td><b>2. Mass loading</b></td><td>Fluid or tissue weight <b>damping</b> tympanic membrane and ossicular movement</td><td>Middle ear effusion, cholesteatoma</td></tr>
    <tr><td><b>3. Stiffness effect</b></td><td>Impaired <b>mobility</b> of the ossicles or the membrane</td><td>Otosclerosis (stapes footplate fixation)</td></tr>
    <tr><td><b>4. Discontinuity</b></td><td>Physical <b>disruption</b> of the ossicular chain</td><td>Temporal bone fracture, ossicular necrosis</td></tr>
  </table>
  <p>Two and three are the pair that get confused. <b>Mass loading adds weight to a chain that can
  still move; stiffness stops the chain moving at all.</b> Effusion damps; otosclerosis fixes.</p>
  <p><b>Cholesteatoma is not in the deck and he told the class to know it anyway</b> [12:17]:
  <em>&ldquo;that&rsquo;s not in this presentation, but you should know about it &hellip; a
  cholesterol collection that forms like a small mass in the ear. Usually it needs to be
  surgically removed.&rdquo;</em> It sits under mass loading.</p>

  <h3 class="sub" id="l5-otosclerosis">5.3 &middot; Otosclerosis</h3>
  <p><b>Pathogenesis:</b> abnormal <b>osteoclastic bone resorption</b> followed by
  <b>hypervascular spongy osteoid replacement</b> around the otic capsule and the stapes
  footplate. Resorption first, then the wrong bone grows back in its place.</p>
  <p><b>The clinical pearl is one event:</b> <b>ankylosis of the stapes footplate in the oval
  window</b> halts mechanical vibration transfer, giving progressive <b>conductive</b> loss. The
  cochlea is untouched, which is why this is conductive rather than sensorineural &mdash; it is
  mechanism 3, stiffness.</p>
  <p><b>Demographics and inheritance</b>, which he flagged at [16:16] as the thing to remember:
  commonest in <b>young-to-middle-aged females</b>, <b>accelerated by pregnancy</b>, and
  <b>50% autosomal dominant with variable penetrance</b>.</p>

  @@OTOSCLEROSIS@@

  <h3 class="sub" id="l5-ototoxic">5.4 &middot; Ototoxicity and noise</h3>
  <p>He gave the organising rule before the detail [16:34]: <em>&ldquo;Ototoxic medications,
  almost always reversible, <b>except for some like platinum chemotherapy</b>.&rdquo;</em> Sort
  the four drug groups by whether the damage stays.</p>
  <table class="tbl">
    <tr><th>Agent</th><th>Molecular mechanism</th><th>Result</th></tr>
    <tr><td><b>Aminoglycosides</b><br>gentamicin, tobramycin</td><td>Induce <b>reactive oxygen species</b> that selectively destroy <b>outer hair cells starting at the cochlear base</b></td><td>Permanent; <b>high pitch lost first</b></td></tr>
    <tr><td><b>Platinum chemotherapy</b><br>cisplatin, carboplatin</td><td><b>Cross-links DNA in stria vascularis cells</b>, compromising endolymph ion homeostasis</td><td><b>Bilateral, permanent</b> sensorineural loss</td></tr>
    <tr><td><b>Loop diuretics</b><br>furosemide</td><td>Alters the <b>stria vascularis potential</b></td><td><b>Reversible</b> conductive or sensorineural loss</td></tr>
    <tr><td><b>Salicylates</b></td><td>Inhibits the <b>prestin</b> motor protein in outer hair cells</td><td><b>Tinnitus</b></td></tr>
  </table>
  <p><b>Why high frequencies go first is anatomical, not chemical.</b> The base of the cochlea
  encodes high pitch, and the base is where the aminoglycoside damage starts. The same geometry
  explains presbycusis, which is why the two sound alike on an audiogram.</p>
  <p><b>Two drugs hit the same structure with opposite outcomes.</b> Cisplatin and furosemide both
  act on the <b>stria vascularis</b> &mdash; the strip of tissue that maintains endolymph. One
  cross-links its DNA and kills it; the other only shifts its electrical potential. That is the
  whole of why one is permanent and one is not.</p>
  <p><b>Noise.</b> Long-term chronic exposure above <b>85 decibels</b> induces irreversible
  <b>stereocilia degeneration and acoustic hair cell apoptosis</b>. The deck's ladder, with what
  he added aloud at [9:01]:</p>
  <table class="tbl">
    <tr><th>Sound</th><th>Level</th><th>Consequence</th></tr>
    <tr><td>Quiet whisper</td><td>30 dB</td><td>&mdash;</td></tr>
    <tr><td>Normal speech</td><td>60 dB</td><td>&mdash;</td></tr>
    <tr><td><b>Hazard threshold</b></td><td><b>85 dB</b></td><td><b>Occupational limit</b> &mdash; chronic exposure above this is where irreversible damage begins</td></tr>
    <tr><td>Lawnmower, traffic</td><td>90 dB</td><td>Cumulative risk</td></tr>
    <tr><td>Ambulance siren</td><td>120 dB</td><td>Acoustic trauma</td></tr>
    <tr><td>Jet engine, blast</td><td>140 dB</td><td><b>Immediate</b> damage</td></tr>
  </table>
  <p><b>Presbycusis</b> is gradual, symmetrical, bilateral sensorineural loss in older adults. Its
  frequency curve <b>begins with high-frequency tones &mdash; the speech consonants /s/, /f/,
  /t/</b> &mdash; which is why the complaint is never &ldquo;I cannot hear&rdquo; but <b>&ldquo;I
  cannot follow conversation in a noisy room&rdquo;</b>. Vowels carry the volume; consonants carry
  the meaning, and it is the consonants that go.</p>

  <h3 class="sub" id="l5-otitis">5.5 &middot; Otitis media and otitis externa</h3>
  <p><b>Otitis media usually begins with Eustachian tube dysfunction</b>, and the sequence is
  mechanical: <b>failure of the tube to open periodically &rarr; absorption of oxygen and nitrogen
  into the middle ear mucosa &rarr; negative middle ear pressure</b>. The air-filled middle ear is
  a sealed box whose only vent has stopped working; the mucosa takes up the gas and the pressure
  drops. Effusion follows, and the membrane bulges once fluid accumulates [23:06].</p>
  <table class="tbl">
    <tr><th></th><th>Otitis media</th><th>Otitis externa (&ldquo;swimmer&rsquo;s ear&rdquo;)</th></tr>
    <tr><td>Bacterial</td><td><b>Streptococcus pneumoniae</b>, <b>Haemophilus influenzae</b>, <b>Moraxella catarrhalis</b></td><td><b>80&ndash;90% of cases</b>: <b>Pseudomonas aeruginosa</b>, <b>Staphylococcus aureus</b></td></tr>
    <tr><td>Other organisms</td><td>Viral: respiratory syncytial virus, rhinovirus, influenza, adenovirus</td><td>Fungal: <b>Aspergillus niger</b>, <b>Candida albicans</b></td></tr>
    <tr><td>Predisposing</td><td>Eustachian tube dysfunction, preceding upper respiratory infection</td><td>Fungal form follows <b>prolonged antibiotic use</b> or <b>hyperhumid conditions</b></td></tr>
  </table>
  <p>The fungal trigger is worth a second look, because it is the same logic as thrush: clear the
  bacteria with a long antibiotic course, or keep the canal permanently wet, and the fungus has no
  competition.</p>

  @@OTITISEXTERNA@@

  <h3 class="sub" id="l5-balance">5.6 &middot; Objective 4 &mdash; Equilibrium, and vertigo against dizziness</h3>
  <p>Two separate detectors, and they answer different questions:</p>
  <table class="tbl">
    <tr><th>Organ</th><th>Detects</th><th>How</th></tr>
    <tr><td><b>Semicircular canals</b> (three loops &mdash; sagittal, coronal, transverse)</td><td><b>Rotational</b> acceleration of the head</td><td><b>Endolymph inertia</b> bends the gelatinous <b>cupula</b> inside the <b>ampulla</b>, stimulating hair cell stereocilia</td></tr>
    <tr><td><b>Otolith organs</b> &mdash; utricle (horizontal), saccule (vertical)</td><td><b>Linear</b> acceleration and <b>gravitational position</b></td><td>Static and linear balance</td></tr>
  </table>
  <p><b>Canals answer &ldquo;am I turning?&rdquo;; otoliths answer &ldquo;which way is
  down?&rdquo;</b> Keep them apart, because benign paroxysmal positional vertigo is precisely a
  failure of the otolith organs that produces a canal symptom.</p>
  <p>Now the distinction the objective actually asks for:</p>
  <table class="tbl">
    <tr><th></th><th>Vertigo</th><th>Dizziness / lightheadedness</th></tr>
    <tr><td>What it is</td><td><b>Hallucination of motion</b> &mdash; spinning, tilting, tumbling</td><td>Non-vestibular sensation of <b>impending faint</b> or unsteadiness</td></tr>
    <tr><td>Mechanism</td><td><b>Asymmetrical sensory input</b> in the vestibular system</td><td><b>Cerebral hypoperfusion</b> (presyncope), orthostatic hypotension, metabolic imbalance</td></tr>
    <tr><td>Accompanied by</td><td>Nystagmus and ataxia. <b>NO syncope</b></td><td>Faintness &mdash; syncope is on the table</td></tr>
  </table>
  <p><b>&ldquo;NO syncope&rdquo; is the discriminator the deck puts in capitals</b>, and it is the
  cleanest one you have. Vertigo is a false signal of motion; the brain is perfused normally, so
  the patient does not faint. Dizziness is a perfusion or metabolic problem, so fainting is exactly
  what is threatened. The word the patient uses tells you nothing &mdash; both arrive as
  &ldquo;dizzy&rdquo;.</p>
  <table class="tbl">
    <tr><th></th><th>Peripheral vertigo</th><th>Central vertigo</th></tr>
    <tr><td>Site</td><td>Inner ear or cranial nerve VIII</td><td>Brainstem or cerebellum</td></tr>
    <tr><td>Onset</td><td><b>Sudden</b></td><td><b>Gradual</b></td></tr>
    <tr><td>Nystagmus</td><td>Prominent <b>horizontal or rotational</b>; <b>fatigable</b>; <b>suppressed by visual fixation</b></td><td><b>Vertical</b> or <b>non-suppressible</b></td></tr>
    <tr><td>Other signs</td><td>&mdash;</td><td><b>Neurological deficits present</b></td></tr>
    <tr><td>Causes</td><td>Benign paroxysmal positional vertigo, M&eacute;ni&egrave;re, labyrinthitis, vestibular neuritis</td><td><b>Brainstem stroke, multiple sclerosis, cerebellar tumour</b></td></tr>
  </table>
  <p><b>Visual fixation is the bedside test and he explained why it works</b> [29:38]:
  <em>&ldquo;by fixing view &hellip; you&rsquo;re overriding the vestibular function telling you
  that things are moving. You&rsquo;re actually helping a person to kind of calm the vertigo
  down. You can do that with peripheral vertigo. <b>You cannot do that with central.</b>&rdquo;</em>
  A peripheral lesion sends a false signal that vision can outvote; a central lesion has broken the
  machinery that does the voting.</p>

  <h3 class="sub" id="l5-peripheral">5.7 &middot; The four peripheral vertigos</h3>
  <p>This is the highest-yield table in the lecture. <b>Read down the duration column first</b>
  &mdash; seconds, hours, days &mdash; then check hearing.</p>
  <table class="tbl">
    <tr><th></th><th>Mechanism</th><th>Duration</th><th>Hearing loss</th><th>The giveaway</th></tr>
    <tr><td><b>Benign paroxysmal positional vertigo</b></td><td><b>Canalithiasis</b> &mdash; dislodged otoconia in the semicircular canals</td><td><b>Under 1 minute</b></td><td><b>NONE</b></td><td>Triggered by <b>positional change of the head</b></td></tr>
    <tr><td><b>M&eacute;ni&egrave;re disease</b></td><td><b>Endolymphatic hydrops</b> &mdash; defective endolymph resorption</td><td><b>Hours</b></td><td>Progressive, <b>low-tone</b></td><td><b>Aural fullness</b> and fluctuating low-frequency tinnitus</td></tr>
    <tr><td><b>Labyrinthitis</b></td><td>Inflammation of canals <b>and</b> cochlea</td><td><b>Days</b>, improving over weeks</td><td><b>Unilateral</b> sensorineural</td><td><b>Recent viral upper respiratory infection</b></td></tr>
    <tr><td><b>Vestibular neuritis</b></td><td>Inflammation of the <b>nerve fibres only</b></td><td>Days</td><td><b>None</b> &mdash; the cochlea is not involved</td><td>Labyrinthitis without the hearing loss</td></tr>
  </table>
  <p><b>Vestibular neuritis is not on a slide of its own and he explained why</b> [32:32]:
  <em>&ldquo;Labyrinthitis &hellip; is just an inflammation of the entire inner ear. Remember I
  said there&rsquo;s another thing called vestibular neuritis? That&rsquo;s just the same thing,
  but just inflammation of the nerve fibres. <b>That&rsquo;s the only difference.</b>&rdquo;</em>
  One lesion in two places: hit the whole labyrinth and hearing goes with balance; hit the nerve
  alone and only balance goes.</p>

  <p><b>M&eacute;ni&egrave;re disease &mdash; endolymphatic hydrops.</b> Defective endolymph
  resorption leads to excessive fluid accumulating in the membranous labyrinth, <b>ballooning the
  scala media until micro-ruptures occur</b>. Production is normal; drainage is not. The episodic
  pattern follows directly from the micro-ruptures &mdash; pressure builds, the membrane gives
  way, symptoms fire, pressure re-equilibrates, and the cycle restarts.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasised</span>
    <p>He called the tetrad out by name at [31:36] &mdash; <em>&ldquo;Classic symptom,
    tetrad&rdquo;</em> &mdash; and said of the disease at [32:26] that it is
    <em>&ldquo;something you&rsquo;ll be tested on &hellip; for sure.&rdquo;</em></p>
    <ol>
      <li><b>Episodic vertigo</b>, sudden, <b>hours</b>-long</li>
      <li><b>Low-frequency fluctuating tinnitus</b></li>
      <li><b>Progressive low-tone sensorineural hearing loss</b></li>
      <li><b>Aural fullness</b> or pressure in the affected ear</li>
    </ol>
    <p><b>Note which way the frequencies run.</b> M&eacute;ni&egrave;re takes the <b>low</b>
    tones; presbycusis and aminoglycosides take the <b>high</b> ones. That single contrast
    separates hydrops from every other sensorineural loss in this lecture.</p>
  </div>

  @@MENIERE@@

  <p><b>Labyrinthitis &mdash; otitis interna.</b> Inflammatory swelling, vascular congestion and
  endolymphatic disruption <b>within the semicircular canals and the cochlea</b> produce a sudden,
  concurrent impairment of <b>both</b> balance and hearing. <b>Cause: viral infection, recent
  viral upper respiratory infection.</b> Hearing and balance fail together for a purely anatomical
  reason &mdash; one continuous fluid space serves both organs, so inflammation anywhere in it
  disturbs both.</p>
  <p>Its features: <b>unilateral tinnitus</b> in the affected ear, <b>unilateral sensorineural
  hearing loss</b>, and <b>horizontal-rotary nystagmus with the fast phase beating AWAY from the
  affected side</b>, with severe postural instability, gait ataxia and nausea.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Correction &mdash; the slide is wrong</span>
    <p><b>Slide 17 calls the vertigo of labyrinthitis &ldquo;episodic&rdquo;. It is continuous,
    and he corrected his own slide aloud, twice.</b></p>
    <p>At [33:05] and again at [34:17]: <em>&ldquo;this is not episodic vertigo. I don&rsquo;t
    know, I did write that. So this is not episodic. <b>This is continuous vertigo</b> &hellip;
    Classic symptoms is continuous, not episodic vertigo.&rdquo;</em></p>
    <p><b>Answer continuous.</b> And notice what the correction protects: <b>episodic</b> vertigo
    lasting hours is M&eacute;ni&egrave;re. If labyrinthitis were episodic too, the two would be
    indistinguishable on the axis that separates them. The vertigo of labyrinthitis is
    <b>continuous, lasting days, improving slowly over weeks</b>.</p>
  </div>

  @@LABYRINTHITIS@@

  <p><b>Benign paroxysmal positional vertigo &mdash; canalithiasis.</b> Otoconia, the crystals
  that normally sit in the utricle, become <b>dislodged into the semicircular canals</b>. Asked in
  the room how that happens, he scoped the answer for this course [36:43&ndash;37:16]: ageing,
  <em>&ldquo;no one really knows exactly &hellip; but <b>what you need to know for
  pathophysiology is that they can become loose</b>. And when they come loose and they&rsquo;re
  floating around in the endolymph, they can hit structures and cause the sensation of movement,
  of motion.&rdquo;</em></p>
  <p>Which explains all three of its features at once: <b>episodes under a minute</b> (the
  crystals settle), <b>triggered by positional change of the head</b> (they only move when gravity
  moves them), and <b>NO hearing loss</b> (the cochlea is nowhere near this). <b>No hearing loss
  is the discriminator</b> &mdash; it is the one peripheral vertigo that leaves hearing alone,
  apart from vestibular neuritis.</p>

  @@BPPV@@

  <h3 class="sub" id="l5-rhinology">5.8 &middot; Rhinology</h3>
  <p><b>Rhinitis is the nose; rhinosinusitis is the nose and the sinuses</b> [37:39]. Duration
  then splits it:</p>
  <table class="tbl">
    <tr><th></th><th>Definition</th><th>Cause</th><th>Presentation</th></tr>
    <tr><td><b>Acute rhinosinusitis</b></td><td><b>Under 4 weeks</b></td><td>Usually <b>viral</b> (rhinovirus, influenza); or secondary bacterial &mdash; <b>Streptococcus pneumoniae</b>, <b>Haemophilus influenzae</b></td><td><b>Purulent</b> rhinorrhoea, facial pain, nasal congestion</td></tr>
    <tr><td><b>Chronic rhinosinusitis</b></td><td><b>Beyond 12 weeks despite therapy</b></td><td>Often a secondary infection layered on an allergic process</td><td>Often with <b>nasal polyps</b></td></tr>
    <tr><td><b>Allergic rhinitis</b></td><td>Not classified by duration</td><td><b>IgE-mediated type 1 hypersensitivity</b> of nasal mucosa to inhaled allergens</td><td><b>CLEAR</b> rhinorrhoea, nasal itching, sneezing, <b>boggy turbinates</b>, allergic &ldquo;shiners&rdquo;</td></tr>
  </table>
  <p><b>Discharge colour is the fastest discriminator</b> and he opened the section with it
  [37:26]: allergic rhinitis gives <b>clear</b> discharge, acute bacterial sinusitis gives
  <b>purulent</b> discharge. Facial pain localises to the sinuses, which is why it belongs to
  rhinosinusitis and not to rhinitis.</p>
  <p>He was also honest about the gap in the definitions [37:54]: <em>&ldquo;I always wonder, so
  what&rsquo;s the in-between? &hellip; What if it&rsquo;s seven weeks?&rdquo;</em> Four to twelve
  weeks is unclassified, and in practice means either a second acute episode or an untreated
  allergy underneath.</p>

  <p><b>Nasal polyps.</b> Non-neoplastic, benign <b>oedematous</b> masses arising from the mucous
  membranes of the sinus ostia or ethmoid air cells. <b>Molecular pathway:</b> chronic type 2
  allergic responses, diffuse cytokine release &mdash; <b>interleukins 4, 5 and 13</b> &mdash; and
  <b>tissue eosinophil influx</b>. <b>Not neoplastic</b> is the word that matters: no new tissue is
  being grown, the existing mucosa is waterlogged [40:28].</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Correction &mdash; the slide is incomplete</span>
    <p>Slide 21 heads the polyp box <b>&ldquo;Type 2 Inflammation&rdquo;</b>. He stopped to fix it
    at [40:01]: <em>&ldquo;let me fix this too here &hellip; this type 2 inflammation is a
    <b>T helper cell type 2</b> inflammatory process. Very important. I didn&rsquo;t write it out,
    I put type 2, but I meant to put <b>T helper cell type 2 allergic inflammation</b>.&rdquo;</em></p>
    <p>He then took it straight back out of scope: <em>&ldquo;I&rsquo;m not gonna ask you about
    that, but just so you know.&rdquo;</em> So: know what the heading means, do not expect to be
    asked it.</p>
  </div>

  @@POLYP@@

  <p><b>Turbinate hypertrophy</b> is enlargement of the <b>inferior</b> nasal turbinates from
  <b>venous sinusoid engorgement</b>, <b>mucosal oedema</b>, or <b>bony hypertrophy</b>. Triggers:
  allergic rhinitis, vasomotor instability, and <b>rebound hyperaemia from topical decongestants
  &mdash; rhinitis medicamentosa</b>. Overuse of a decongestant spray produces the congestion it
  was bought to relieve [42:44].</p>

  <p><b>Deviated septum.</b> Displacement of nasal cartilage or bone off the midline divides the
  cavities into <b>asymmetric flow channels</b>, and the consequences all follow from airflow
  physics rather than from the deviation itself:</p>
  <table class="tbl">
    <tr><th>Consequence</th><th>Mechanism</th></tr>
    <tr><td><b>Unilateral resistance</b></td><td><b>Poiseuille&rsquo;s law</b> &mdash; even small airway narrowing dramatically increases resistance</td></tr>
    <tr><td><b>Chronic nasal obstruction</b></td><td>Persistent mouth-breathing; <b>aggravates sleep apnoea</b></td></tr>
    <tr><td><b>Mucosal drying and epistaxis</b></td><td><b>Turbulent</b> air currents cause localised crusting and fragile vessel breakdown</td></tr>
    <tr><td><b>Olfactory dysfunction</b></td><td>Airflow <b>fails to reach the superior nasal vault and cribriform plate</b></td></tr>
    <tr><td><b>Compensatory hypertrophy</b></td><td>The <b>contralateral wide cavity</b> undergoes inferior turbinate enlargement to humidify the increased air volume</td></tr>
    <tr><td><b>Sinus ostia blockage</b></td><td>Mucus stasis, hypoxia, secondary bacterial rhinosinusitis</td></tr>
  </table>
  <p><b>The compensation is the part that gets missed.</b> The turbinate that hypertrophies is on
  the <b>open</b> side, not the blocked one &mdash; it is working harder, humidifying air the
  narrow side can no longer carry. So a patient can be obstructed on both sides from a
  one-sided deviation. He put the airflow split at <em>&ldquo;97% of all air coming into the nose
  going through one side&rdquo;</em> [45:23], and told the class to reverse the inference: when
  you find enlarged inferior turbinates, go looking for the septal deviation that caused them
  [42:22].</p>

  @@SEPTUM@@

  <p><b>Epistaxis.</b> Two bleeds, two vessels, two risk profiles. The management column on the
  slide belongs to Clinical Medicine and Surgery; what this course asks for is the vascular source
  and the aetiology.</p>
  <table class="tbl">
    <tr><th>Feature</th><th>Anterior epistaxis (<b>90%</b>)</th><th>Posterior epistaxis (<b>10%</b>)</th></tr>
    <tr><td><b>Primary vascular source</b></td><td><b>Kiesselbach&rsquo;s plexus</b> (anterior septum)</td><td><b>Woodruff&rsquo;s plexus</b> (posterolateral wall)</td></tr>
    <tr><td><b>Predominant aetiology</b></td><td>Digital trauma, <b>low humidity</b>, localised mucosal erosion, mild rhinitis</td><td><b>Hypertension</b>, atherosclerosis, <b>anticoagulant therapy</b>, coagulopathy</td></tr>
    <tr><td><b>Presentation</b></td><td>Unilateral anterior bleeding, easily compressed directly</td><td><b>Profuse bleeding down the posterior pharynx</b>, <b>airway risk</b></td></tr>
  </table>
  <p><b>The aetiology columns are the tell.</b> Anterior causes are all <b>local</b> &mdash;
  something hit or dried the mucosa. Posterior causes are all <b>systemic</b> &mdash; vessel
  pressure and clotting. That is also why posterior bleeds are dangerous: he explained at [44:49]
  that <b>Woodruff&rsquo;s plexus carries far more arterial supply than Kiesselbach&rsquo;s</b>,
  so an arterial bleed sits behind a space you cannot compress. <em>&ldquo;You get a posterior
  bleed, that thing may not stop bleeding&rdquo;</em> [44:30] &mdash; but <em>&ldquo;you will
  usually only see anterior epistaxis&rdquo;</em> [45:06].</p>

  <h3 class="sub" id="l5-larynx">5.9 &middot; Larynx and neck</h3>
  <p><b>Nodules against polyps.</b> Everything separates on <b>laterality, site and the kind of
  trauma</b>:</p>
  <table class="tbl">
    <tr><th></th><th>Vocal cord nodules (&ldquo;singer&rsquo;s nodes&rdquo;)</th><th>Vocal cord polyps</th></tr>
    <tr><td><b>Laterality</b></td><td><b>Bilateral, symmetrical</b></td><td><b>Unilateral</b></td></tr>
    <tr><td><b>Site</b></td><td>Junction of the <b>anterior one third and posterior two thirds</b></td><td><b>Middle third</b> of the true cord</td></tr>
    <tr><td><b>Character</b></td><td>Fibrous <b>calluses</b></td><td>Soft, fluid-filled or vascular, <b>pedunculated</b></td></tr>
    <tr><td><b>Pathogenesis</b></td><td><b>Chronic</b> mechanical phonotrauma &mdash; cords slamming together from yelling, cheering &mdash; causing <b>basement membrane hyalinisation</b></td><td><b>Acute severe</b> voice strain or <b>vocal cord haemorrhage</b>, causing a localised inflammatory healing response</td></tr>
  </table>
  <p><b>Chronic and bilateral against acute and unilateral.</b> Repeated impact damages both cords
  at the same point, because both cords take the same blow; a single violent strain or a bleed
  damages one. He drew the same line on the tissue at [46:04]: <em>&ldquo;hyalinisation is not the
  same as callus formation. Hyalinisation is kind of like a pink, excessive membrane growth.
  Callus is obviously like a fibrous material formation, but it can be either or in the
  nodules.&rdquo;</em></p>
  <p class="note"><b>Where the audio and the slide disagree, the slide wins here.</b> At [46:38]
  he began <em>&ldquo;Polyps, however &hellip; these are usually bilateral&rdquo;</em> and
  corrected himself inside the same sentence to <em>&ldquo;Unilateral lesions in the
  polyps&rdquo;</em>. The slide says unilateral, and the slide's own picture shows one lesion on
  one cord. <b>Polyps are unilateral.</b></p>

  @@VOCALCORDS@@

  <p><b>Tonsillitis.</b> Acute viral or bacterial inflammation of the <b>palatine tonsils</b> and
  pharyngeal mucosa, <b>usually Group A Streptococcus</b> when bacterial. Symptoms: sore throat,
  <b>odynophagia</b> (pain on swallowing), fever, <b>tonsillar exudates</b>, <b>trismus</b>, and
  <b>asymmetric tonsillar deviation if complicated by a tonsillar abscess</b>.</p>
  <p><b>Asymmetry is the alarm.</b> Tonsillitis is symmetrical; an abscess pushes one tonsil across
  the midline and clamps the jaw. He added the airway point at [47:18]: chronic swollen tonsils
  that <b>obstruct the airway</b> are an emergency. And epiglottitis sits just below, <em>&ldquo;a
  little inferior to the tonsillitis&rdquo;</em>.</p>
  <p><b>The slide&rsquo;s picture carries a distinction its text does not:</b> <b>white patches or
  nodules on red swollen tonsils</b> point bacterial; <b>redness and swelling with no exudate</b>
  points viral &mdash; which is how he read it aloud at [47:31].</p>

  @@TONSILS@@

  <p><b>Cervical lymphadenopathy.</b> Usually benign enlargement of cervical nodes responding to
  regional head and neck infection &mdash; viral upper respiratory infection, otitis media, dental
  disease &mdash; or to systemic inflammatory conditions. The reactive node is <b>palpable and
  tender</b>.</p>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasised</span>
    <p><b>The red flags are a specific combination, not any large node:</b> <b>persistent</b>,
    <b>rubbery or matted</b>, <b>supraclavicular or cervical</b>, in an <b>older adult</b>. That
    requires immediate assessment to rule out <b>lymphoma</b>.</p>
    <p><b>Tender and soft is reactive; painless, rubbery and matted is not.</b> Matted means the
    nodes have lost their individual capsules and moved as a mass &mdash; tissue behaving as if it
    is no longer respecting boundaries. He closed the lecture on it [48:41]: send a
    <b>run-of-the-mill</b> case to an ENT specialist; send one with a cancer history or chronic
    smoking <b>straight to oncology</b>.</p>
  </div>

  <button type="button" class="test-yourself-btn" style="--acc:#3b2a5e" onclick="window.openTestYourself('Test yourself &mdash; ENT Pathophysiology', TEST_YOURSELF.ent)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>5. ENT Clinical Pathophysiology_STUDENT VERSION.pptx</em>
  (Bill Webster, MMS, PA-C, guest lecturer), Slides 1&ndash;28, and the lecture of 2 September.
  Figures are reproduced from the lecture slides and each is cited to its slide.</footer>
</section>
"""

TOC = """  <a class="top-link" href="#ent-pathophys">5 &middot; ENT Pathophysiology</a>
  <a class="sub-link" href="#l5-anatomy">5.1 Anatomy &amp; transduction</a>
  <a class="sub-link" href="#l5-hearing">5.2 Conductive vs sensorineural</a>
  <a class="sub-link" href="#l5-otosclerosis">5.3 Otosclerosis</a>
  <a class="sub-link" href="#l5-ototoxic">5.4 Ototoxicity &amp; noise</a>
  <a class="sub-link" href="#l5-otitis">5.5 Otitis media &amp; externa</a>
  <a class="sub-link" href="#l5-balance">5.6 Vertigo vs dizziness</a>
  <a class="sub-link" href="#l5-peripheral">5.7 The four peripheral vertigos</a>
  <a class="sub-link" href="#l5-rhinology">5.8 Rhinology</a>
  <a class="sub-link" href="#l5-larynx">5.9 Larynx &amp; neck</a>
"""

TESTS = """    ent: [
      {q:"Weber lateralises to the RIGHT ear and Rinne shows bone greater than air on the right. What is the lesion?",
       o:["Conductive loss in the right ear","Sensorineural loss in the right ear",
          "Conductive loss in the left ear","Sensorineural loss in the left ear"],a:0,
       why:"Weber goes to the AFFECTED ear in conductive loss, and bone greater than air is the abnormal Rinne. Both point to the same side, which is what conductive loss does."},
      {q:"Which conductive mechanism does otosclerosis use?",
       o:["Stiffness — the stapes footplate is fixed","Mass loading — weight damps the ossicles",
          "Obstruction — the canal is blocked","Discontinuity — the chain is broken"],a:0,
       why:"Ankylosis of the footplate stops the chain moving. Mass loading is the near miss: effusion damps a chain that still moves, otosclerosis fixes it."},
      {q:"Cisplatin and furosemide act on the same structure. Which, and why is only one permanent?",
       o:["Stria vascularis — cisplatin cross-links its DNA, furosemide only shifts its potential",
          "Outer hair cells — cisplatin kills them, furosemide stuns them",
          "Tectorial membrane — cisplatin stiffens it, furosemide softens it",
          "Cranial nerve VIII — cisplatin demyelinates it, furosemide blocks conduction"],a:0,
       why:"Both target the stria vascularis. Killing the cells that maintain endolymph is permanent; changing their electrical potential is not."},
      {q:"Vertigo and dizziness both arrive as \\u201cdizzy\\u201d. What single feature separates them?",
       o:["Vertigo has NO syncope; dizziness threatens fainting","Vertigo is worse on standing",
          "Vertigo lasts longer","Vertigo is always bilateral"],a:0,
       why:"Vertigo is a false motion signal with normal cerebral perfusion. Dizziness IS a perfusion or metabolic problem, so fainting is exactly what is threatened."},
      {q:"Vertigo lasting under a minute, triggered by turning the head in bed, with NO hearing loss. Which is it?",
       o:["Benign paroxysmal positional vertigo","M\\u00e9ni\\u00e8re disease",
          "Labyrinthitis","Vestibular neuritis"],a:0,
       why:"Seconds plus positional trigger plus intact hearing is canalithiasis. M\\u00e9ni\\u00e8re runs hours with hearing loss; labyrinthitis runs days after a virus."},
      {q:"The slide calls the vertigo of labyrinthitis \\u201cepisodic\\u201d. What did the lecturer correct it to, and why does the correction matter?",
       o:["Continuous — episodic vertigo lasting hours is M\\u00e9ni\\u00e8re, so \\u201cepisodic\\u201d would erase the distinction",
          "Positional — it only fires on head movement","Absent — labyrinthitis causes hearing loss only",
          "Episodic is correct; the correction was withdrawn"],a:0,
       why:"He corrected his own slide twice. Labyrinthitis is continuous, lasting days and improving over weeks."},
      {q:"Which frequencies does M\\u00e9ni\\u00e8re disease take, and how does that separate it from presbycusis?",
       o:["LOW tones; presbycusis and aminoglycosides take the HIGH ones",
          "HIGH tones; presbycusis takes the low ones",
          "All frequencies equally, unlike presbycusis",
          "Only speech frequencies, unlike presbycusis"],a:0,
       why:"Hydrops is the low-tone loss. Every other sensorineural loss in this lecture starts high, because the cochlear base encodes high pitch and the base is what degenerates."},
      {q:"A deviated septum obstructs the right nostril. Which turbinate hypertrophies?",
       o:["The LEFT — the open side humidifies the increased air volume",
          "The RIGHT — the narrowed side congests",
          "Both equally","Neither; turbinates are unaffected by septal position"],a:0,
       why:"Compensatory hypertrophy is contralateral. The open side is working harder, which is how a one-sided deviation ends up obstructing both sides."},
      {q:"Which plexus bleeds in posterior epistaxis, and why is it the dangerous one?",
       o:["Woodruff\\u2019s — it carries far more arterial supply and sits where you cannot compress it",
          "Kiesselbach\\u2019s — it is closer to the airway",
          "Woodruff\\u2019s — it is venous and therefore slower to clot",
          "Kiesselbach\\u2019s — it drains directly into the cavernous sinus"],a:0,
       why:"Woodruff\\u2019s plexus on the posterolateral wall. Its causes are systemic too — hypertension, anticoagulation — where anterior causes are all local."},
      {q:"Bilateral symmetrical lesions at the junction of the anterior third of both vocal cords. What are they and what caused them?",
       o:["Nodules, from chronic phonotrauma","Polyps, from a single severe strain",
          "Nodules, from vocal cord haemorrhage","Polyps, from chronic phonotrauma"],a:0,
       why:"Bilateral and symmetrical means repeated impact damaging both cords at the same point. Polyps are unilateral, mid-cord, and follow one acute event."},
      {q:"Which cervical node findings demand assessment for lymphoma?",
       o:["Persistent, rubbery or matted, supraclavicular or cervical, in an older adult",
          "Tender and mobile after a sore throat","Any node over one centimetre",
          "Bilateral tender nodes with fever"],a:0,
       why:"Tender and soft is reactive. Matted means the nodes have lost their separate capsules and move as one mass."}
    ],
"""

FIGS = {
    "@@EARANATOMY@@": ("ear-anatomy", "jpg",
        "The whole lecture&rsquo;s anatomy in one figure &mdash; outer, middle and inner ear; the "
        "membranous labyrinth with the cupula inset; the cochlear duct sitting between scala "
        "vestibuli and scala tympani; and a hair cell wired to cranial nerve VIII.", 4),
    "@@COCHLEA@@": ("cochlear-section", "png",
        "The cochlear duct in cross-section. Find the <b>stria vascularis</b> on the outer wall "
        "&mdash; that strip maintains the endolymph, and it is where cisplatin and furosemide "
        "both act.", 5),
    "@@OTOSCLEROSIS@@": ("otosclerosis", "png",
        "Otosclerosis fixes the stapes footplate where it meets the oval window. The chain is "
        "intact and unweighted; it simply cannot move &mdash; mechanism 3, stiffness.", 10),
    "@@OTITISEXTERNA@@": ("otitis-externa", "png",
        "Otitis externa. The discharge and crusting are coming out of the canal, not off the "
        "auricle &mdash; the point he made about this photograph at [24:13].", 13),
    "@@MENIERE@@": ("meniere", "png",
        "Normal labyrinth beside a hydropic one. Defective resorption distends the endolymph and "
        "balloons the scala media until micro-ruptures occur.", 16),
    "@@LABYRINTHITIS@@": ("labyrinthitis", "png",
        "Labyrinthitis inflames the semicircular canals <b>and</b> the cochlea. One continuous "
        "fluid space serves both, which is why balance and hearing fail together.", 17),
    "@@BPPV@@": ("bppv", "png",
        "Otoconia belong in the utricle. Displaced into the semicircular canals they move with "
        "gravity and fire a false signal of rotation &mdash; hence positional, brief, and no "
        "hearing loss.", 18),
    "@@POLYP@@": ("nasal-polyp", "png",
        "A nasal polyp on endoscopy: pale and oedematous, not vascular. Non-neoplastic &mdash; "
        "waterlogged existing mucosa, not new tissue.", 21),
    "@@SEPTUM@@": ("deviated-septum", "png",
        "Normal septum against a deviated one. Note the labelled <b>hypertrophied turbinate on "
        "the wide side</b> &mdash; the compensation is contralateral to the obstruction.", 22),
    "@@VOCALCORDS@@": ("vocal-cords", "png",
        "Nodules are bilateral and symmetrical at the anterior third; the polyp is a single "
        "lesion on one cord. The slide&rsquo;s own picture settles the laterality.", 25),
    "@@TONSILS@@": ("tonsillitis", "png",
        "Healthy, bacterial and viral. <b>White patches on red swollen tonsils</b> point "
        "bacterial; <b>redness and swelling without exudate</b> points viral &mdash; a "
        "distinction the slide&rsquo;s text does not carry.", 26),
}


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for o, cl in (("<!--CPL5-->", "<!--/CPL5-->"), ("<!--CPTOC5-->", "<!--/CPTOC5-->"),
                  ("<!--CPTY5-->", "<!--/CPTY5-->")):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(cl), "", src, flags=re.S)

    body = BODY
    for token, (slug, ext, cap, slide) in FIGS.items():
        assert token in body, "figure token %s unused" % token
        body = body.replace(token, fig(slug, ext, cap, slide))
    assert "@@" not in body, "unfilled figure token"

    assert "TEST_YOURSELF.ent" in body, (
        "this section registers a TEST_YOURSELF.ent bank but has no button that opens "
        "it -- section 4's bank shipped unreachable for exactly this reason")

    # The three live corrections must each survive into the rendered section --
    # they are the reason this guide exists alongside the quizzes.
    for needle, what in (("not episodic", "the slide-17 labyrinthitis correction"),
                         ("T helper cell type 2", "the slide-21 polyp correction"),
                         ("Polyps are unilateral", "the slide-25 laterality ruling")):
        assert needle in body, "%s was dropped" % what
    # Management belongs to CMS, not here. [[clin_path_exam_spec]]
    for banned in ("oxymetazoline", "balloon packing", "cautery", "embolisation"):
        assert banned.lower() not in body.lower(), (
            "%r is management -- that column of slide 23 belongs to Clinical Medicine "
            "and Surgery, not this course" % banned)

    j = src.index("</main>")
    src = src[:j] + "<!--CPL5-->" + body + "<!--/CPL5-->\n\n" + src[j:]
    k = src.index("</nav>")
    src = src[:k] + "<!--CPTOC5-->\n" + TOC + "<!--/CPTOC5-->\n" + src[k:]
    m = src.index("var TEST_YOURSELF = {")
    m = src.index("\n", m) + 1
    src = src[:m] + "<!--CPTY5-->\n" + TESTS + "<!--/CPTY5-->\n" + src[m:]

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li",
                "figure", "figcaption", "b", "em", "i"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for fn in re.findall(r'src="%s/([^"]+)"' % IMG, body):
        assert os.path.exists(os.path.join(DIR, IMG, fn)), fn

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 5: %d subsections, %d figures, %d flagged blocks, "
          "%d test-yourself questions"
          % (body.count('class="sub"'), body.count("<figure"),
             body.count('prof-flag-label'), TESTS.count("{q:")))


if __name__ == "__main__":
    main()
