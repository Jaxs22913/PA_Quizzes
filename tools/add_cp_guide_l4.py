#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Clinical Pathophysiology I section 4 (Ophthalmic Pathophysiology).

Instructional Objectives are quoted VERBATIM from the Clin Path 1 syllabus,
including its a-j lettering, per [[guide_verbatim_io_rule]]. The SLIDE numbers
them 1-10 and drops three definite articles; the syllabus is authoritative.

"KNOW FOR EXAM - STATED" is Jaxon's instruction of 26 August. In the last two
minutes of the lecture Webster said "This is for the test" and named seven
topics. They are marked with the existing prof-flag machinery, relabelled --
this is stronger than the ordinary "professor emphasized" flag, because he was
not emphasising, he was listing the exam.

RECOVERING THAT LIST REQUIRED BOTH TRANSCRIPTS. Notability's ASR dropped
GLAUCOMA entirely; faster-whisper dropped CATARACTS entirely. Either alone would
have produced a guide missing a condition he named aloud as testable.

Idempotent: fenced in <!--CPL4--> and stripped before reinsert.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1")
GUIDE = os.path.join(DIR, "cp-exam-1-study-guide.html")
IMG = "cp-exam-1-l4-images"
ACC = "#3b2a5e"

# the seven he named, in the order he said them
KFE = ["cataracts", "macular degeneration", "the visual pathway", "refraction errors",
       "retinal detachment", "glaucoma", "presbyopia"]


def fig(slug, ext, caption, slide):
    path = os.path.join(DIR, IMG, "%s.%s" % (slug, ext))
    assert os.path.exists(path), "missing figure %s -- run extract_cp_l4_figures.py" % slug
    return ('<figure class="fig"><img src="%s/%s.%s" decoding="async" '
            'alt="Lecture 4 slide %d figure."><figcaption>%s '
            '<span class="cite">Lecture 4 &middot; Slide %d</span></figcaption></figure>'
            % (IMG, slug, ext, slide, caption, slide))


BODY = """
<section class="deck" id="ophthalmic-pathophys">
  <h2 class="deck-title">4 &middot; Ophthalmic Pathophysiology</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Ophthalmic Pathophysiology</p>
    <ol type="a">
      <li>Compare and contrast the neurological anatomy of the eye</li>
      <li>Describe the physiological processes of vision</li>
      <li>Describe the molecular mechanisms of common ocular pathologies</li>
      <li>Compare and contrast the conditions caused by abnormal shapes of the eye</li>
      <li>Compare and contrast the conditions of the eye that are age related</li>
      <li>Describe the pathogenesis of glaucoma</li>
      <li>Describe the pathogenesis of cataracts</li>
      <li>Compare and contrast the pathogenesis of retinal detachment</li>
      <li>Describe the pathologic process of macular degeneration</li>
      <li>Describe visual field deficits according to the area of pathology</li>
    </ol>
  </div>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; stated</span>
    <p>In the last two minutes of the 26 August lecture the guest lecturer said
    <em>&ldquo;This is for the test&rdquo;</em> and named these:</p>
    <ol>
      <li><b>Cataracts</b></li>
      <li><b>Macular degeneration</b> &mdash; <em>&ldquo;what we just talked about&rdquo;</em></li>
      <li><b>The visual pathway</b> &mdash; <em>&ldquo;know those areas of changes in your visual
      pathway, what would cause a particular visual change&rdquo;</em></li>
      <li><b>Refraction errors</b></li>
      <li><b>Retinal detachment</b> &mdash; <em>&ldquo;the different things that can cause
      retinal detachment&rdquo;</em></li>
      <li><b>Glaucoma</b> &mdash; specifically <em>&ldquo;what&rsquo;s the pathophysiological
      explanation for vision loss there?&rdquo;</em></li>
      <li><b>Presbyopia</b> &mdash; volunteered <em>after</em> he had said &ldquo;that&rsquo;s
      it&rdquo;, so he went back for it deliberately</li>
    </ol>
    <p>He also <b>cut scope twice on the visual fields</b>: <em>&ldquo;these I wouldn&rsquo;t
    worry about that much &hellip; this is getting more into neurology, which we&rsquo;ll see
    later &hellip; <b>know these better: optic nerve damage, optic chiasm damage, optic tract
    damage</b>&rdquo;</em> and <em>&ldquo;D and E, you can know that if you want, but know A, B
    and C.&rdquo;</em></p>
    <p>And he de-emphasised lens correction: <em>&ldquo;not that important, concave and convex
    for my purposes. <b>More important is knowing the difference between myopia, hyperopia, and
    the globe shape.</b>&rdquo;</em> He then contradicted himself on which lens does what and
    corrected mid-sentence, so trust the slide, not the sentence &mdash; and expect the
    <b>geometry</b>, not the lens.</p>
  </div>

  <h3 class="sub" id="l4-anatomy">4.1 &middot; Objectives a &amp; b &mdash; Anatomy and the physiology of vision</h3>
  <p>Five things make the eye unusual, and each one explains a disease later in this lecture.
  <b>The cornea is avascular</b>, oxygenated by direct contact with air and tears, and about
  <b>seventy per cent of refraction</b> depends on it &mdash; which is why corneal disease blurs
  vision so completely. <b>The retina has the highest oxygen consumption and metabolic rate of any
  tissue</b>, higher than cerebral cortex, which is why it tolerates ischaemia so badly. And the
  eye is the <b>only place in the body where live neural tissue and native microcirculation can be
  seen directly</b>, without cutting anything.</p>

  <p><b>The three tunics, outside in:</b></p>
  <table class="tbl">
    <tr><th>Tunic</th><th>Structures</th><th>Role</th></tr>
    <tr><td>Fibrous (outer)</td><td>Sclera, cornea</td><td>Protective white coat; clear avascular refracting window</td></tr>
    <tr><td>Uvea (vascular, middle)</td><td>Choroid, ciliary body, iris</td><td>Choroid nourishes the retina; ciliary body makes aqueous and drives accommodation; iris sets pupil size</td></tr>
    <tr><td>Retina (neurosensory, inner)</td><td>Photoreceptors, interneurons, ganglion cells</td><td>Converts light to neural signal</td></tr>
  </table>

  <p><b>Vision needs three things and will fail if any one is lost:</b> image formation (light
  refracted by cornea and lens onto the retina), photoreceptor excitation (photons make rods and
  cones fire <b>hyperpolarising</b> potentials), and neural transmission (optic nerve to occipital
  cortex).</p>

  <p><b>Rods, about 120 million</b>, are high-sensitivity, for dim light and the peripheral retina.
  <b>Cones, about 6 million</b>, carry colour and sharp acuity and are concentrated in the
  <b>fovea centralis</b> within the macula. Beneath them the <b>retinal pigment epithelium</b> does
  three jobs &mdash; absorbs scattered light, phagocytoses spent photoreceptor outer segments, and
  maintains the blood-retinal barrier. Signals pass through <b>bipolar, horizontal and amacrine</b>
  interneurons to the ganglion cells, whose axons become the optic nerve. The <b>optic disc is the
  blind spot</b> because it has no rods or cones.</p>

  <p><b>Fluid mechanics.</b> Aqueous humour is made continuously by the non-pigmented epithelium of
  the ciliary body into the posterior chamber, flows through the pupil into the anterior chamber
  nourishing the avascular lens and cornea, and drains <b>trabecular meshwork &rarr; canal of
  Schlemm &rarr; episcleral veins</b>. That drainage route is the whole of glaucoma. Behind the
  lens, <b>vitreous humour</b> &mdash; water, type two collagen, hyaluronic acid &mdash; acts as a
  shock absorber pressing the retina against the pigment epithelium. Its age-related liquefaction
  is the whole of rhegmatogenous detachment.</p>

  <h3 class="sub" id="l4-refractive">4.2 &middot; Objectives d &amp; e &mdash; Globe shape, and the age-related conditions</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; stated</span>
    <p><b>Refraction errors</b> and <b>presbyopia</b> are both on his list. Learn them as
    <b>geometry</b>, not as lens prescriptions.</p>
  </div>
  <table class="tbl">
    <tr><th>Error</th><th>Geometry</th><th>Where the image lands</th><th>What is preserved</th></tr>
    <tr><td><b>Myopia</b> (near-sighted)</td><td>Axial globe too <b>long</b></td><td><b>In front of</b> the retina</td><td>Near vision</td></tr>
    <tr><td><b>Hyperopia</b> (far-sighted)</td><td>Axial globe too <b>short</b></td><td><b>Behind</b> the retina</td><td>Distance vision</td></tr>
    <tr><td><b>Astigmatism</b></td><td>Irregular corneal or lens curvature</td><td>Non-spherical focal points &mdash; no single focus anywhere</td><td>Nothing is fully sharp</td></tr>
    <tr><td><b>Presbyopia</b></td><td>Lens sclerosis, loss of elasticity</td><td>Cannot change shape to focus near</td><td>Distance vision</td></tr>
  </table>
  <p>Astigmatism can stack on top of myopia or hyperopia, adding an axis error to a focal-length
  error, which is why it blurs the whole field rather than one distance.</p>
  <p><b>Presbyopia is the one he came back for.</b> The lens is normally elastic; with age it
  <b>hardens</b>, so the ciliary muscle can no longer change its shape &mdash; that is what
  &ldquo;cannot accommodate&rdquo; means. He tied it to the <b>A in PERRLA</b> &mdash; Pupils
  Equal, Round, Reactive to Light and <b>Accommodation</b> &mdash; and quizzed the room on what
  the A stands for.</p>
  <p><b>Strabismus versus amblyopia</b> is a mechanical problem against a developmental one.
  <b>Strabismus</b> is misalignment &mdash; the visual axes fail to land on corresponding retinal
  points &mdash; from extraocular muscle imbalance or a third, fourth or sixth nerve palsy;
  subtypes are esotropia (in), exotropia (out), hypertropia (up), hypotropia (down).
  <b>Amblyopia</b> is reduced best-corrected acuity from abnormal visual processing during the
  critical developmental period, caused by uncorrected strabismus, severe refractive error, or
  deprivation from congenital cataract or ptosis. The <b>treatment window closes at seven to
  eight years</b> because that is when the visual system stops being plastic.</p>

  <h3 class="sub" id="l4-cataract">4.3 &middot; Objective g &mdash; Cataract</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; stated</span>
    <p>Named first on his list, and the deck's own objective slide says
    <em>&ldquo;describe the pathogenesis&rdquo;</em>. Learn the four mechanisms, not just the word.</p>
  </div>
  <p>A cataract is <b>opacification of the crystalline lens</b>. Four routes to it:</p>
  <table class="tbl">
    <tr><th>Cause</th><th>Mechanism</th></tr>
    <tr><td><b>Senile</b> (commonest)</td><td>Progressive <b>insoluble aggregation of lens crystallin proteins</b></td></tr>
    <tr><td><b>Metabolic</b> &mdash; diabetes</td><td>Excess glucose converted to <b>sorbitol</b> &rarr; <b>osmotic swelling</b> of the lens</td></tr>
    <tr><td><b>Drugs and trauma</b></td><td>Chronic corticosteroids; blunt or penetrating injury rupturing the lens capsule</td></tr>
    <tr><td><b>Congenital and environmental</b></td><td>Down syndrome; excess ultraviolet radiation and oxidative damage</td></tr>
  </table>
  <p><b>Presentation:</b> gradual, painless, bilateral blurring; <b>glare around headlights at
  night</b>; monocular diplopia; altered colour perception. <b>On examination:</b> loss of the
  normal <b>red reflex</b>, with a white opacity through the pupil (leukocoria) when severe.
  Usually peripheral in the lens, but a <b>nuclear</b> cataract is often post-traumatic.</p>

  <h3 class="sub" id="l4-glaucoma">4.4 &middot; Objective f &mdash; Glaucoma</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; stated</span>
    <p>He asked for one thing specifically: <em>&ldquo;What&rsquo;s the pathophysiological
    explanation for vision loss there?&rdquo;</em> The answer is the chain below &mdash; pressure,
    axon compression, ganglion cell apoptosis, cupping.</p>
  </div>
  <p><b>The hallmark:</b> raised intraocular pressure compresses retinal ganglion cell axons at the
  disc &rarr; <b>ganglion cell apoptosis</b> &rarr; progressive <b>optic disc cupping</b>, an
  increased cup-to-disc ratio <b>above 0.5</b>. The vision loss is nerve loss, not media opacity
  &mdash; that is the whole answer to his question.</p>
  <table class="tbl">
    <tr><th></th><th>Primary open-angle</th><th>Primary angle-closure</th></tr>
    <tr><td>Angle</td><td><b>Open</b></td><td>Anatomically <b>narrowed</b></td></tr>
    <tr><td>Mechanism</td><td>Microscopic resistance in the trabecular meshwork impairs outflow</td><td><b>Mydriasis</b> displaces the iris forward against the cornea (<b>iris bomb&eacute;</b>), blocking outflow completely</td></tr>
    <tr><td>Onset</td><td>Insidious, painless, bilateral</td><td>Acute, pressure spiking <b>above 50 mmHg</b></td></tr>
    <tr><td>Symptoms</td><td><b>Asymptomatic</b> until severe peripheral loss &mdash; &ldquo;tunnel vision&rdquo;</td><td>Severe eye pain, headache, <b>halos</b>, cloudy cornea, <b>fixed mid-dilated pupil</b>, nausea and vomiting</td></tr>
  </table>
  <div class="callout warn">
    <p><b>This deck disagrees with itself on normal intraocular pressure.</b> Slide 24 says
    <b>10&ndash;21 mmHg</b>; slide 25, two slides later, says <b>&ldquo;about 6&ndash;19
    mmHg&rdquo;</b>. Prof. Beck's Physical Diagnosis 2 ocular deck independently gives 10&ndash;21,
    so 6&ndash;19 looks like the slip &mdash; but nothing here is graded on that value. What is not
    in dispute is the <b>acute spike above 50</b>.</p>
  </div>

  <h3 class="sub" id="l4-retina">4.5 &middot; Objectives h &amp; i &mdash; Retinal detachment and macular degeneration</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; stated</span>
    <p>Both are on his list, and for detachment he asked specifically for <em>&ldquo;the different
    things that can cause retinal detachment&rdquo;</em> &mdash; so learn the three mechanisms,
    not just the presentation.</p>
  </div>
  <p><b>Why age matters first:</b> the vitreous is gel-like in youth and <b>liquefies</b> with age
  &mdash; the lecturer's analogy was jelly left in the fridge, separating into a liquid layer over
  a solid one. Liquefied vitreous is what can pass through a break.</p>
  <table class="tbl">
    <tr><th>Type</th><th>Mechanism</th><th>Causes</th></tr>
    <tr><td><b>Rhegmatogenous</b></td><td><b>Full-thickness tear</b> lets liquefied vitreous into the subretinal space, peeling the retina off the pigment epithelium</td><td>Posterior vitreous detachment, age, severe myopia, trauma, lattice degeneration</td></tr>
    <tr><td><b>Tractional</b></td><td>Proliferative <b>fibrovascular membranes</b> on the retinal surface physically pull it off</td><td>Proliferative diabetic retinopathy; prior trauma, surgery or vitrectomy scarring</td></tr>
    <tr><td><b>Exudative (serous)</b></td><td>Subretinal fluid accumulates with <b>no tear and no traction</b> &mdash; blood-retinal barrier breakdown</td><td>Severe malignant hypertension, sarcoidosis, choroidal melanoma</td></tr>
  </table>
  <p><b>Rhegmatogenous symptoms:</b> flashing lights (photopsia), a shower of floaters, then a
  <b>curtain falling</b> across the field.</p>
  @@DETACH@@

  <p><b>Macular degeneration</b> is the leading cause of new-onset blindness in United States
  adults <b>over 75</b>. The deck is explicit that the <b>pathogenesis is unknown</b> for both
  forms.</p>
  <table class="tbl">
    <tr><th></th><th>Dry (atrophic)</th><th>Wet (exudative, neovascular)</th></tr>
    <tr><td>Process</td><td>Slow bilateral degeneration of photoreceptors, pigment epithelium and choroid</td><td><b>Choroidal neovascularisation</b> &mdash; hypoxia and inflammation drive new vessels beneath the pigment epithelium into the subretinal space</td></tr>
    <tr><td>Hallmark</td><td><b>Drusen</b> &mdash; discrete yellow extracellular debris (lipofuscin, apolipoproteins) beneath the pigment epithelium and Bruch membrane</td><td>Leaking vessels, blood and serous fluid</td></tr>
    <tr><td>Course</td><td>Slow loss of central detail; metamorphopsia and scotoma</td><td><b>Rapid</b> central loss, disciform scarring, detachment</td></tr>
    <tr><td>Share of severe blindness</td><td>&mdash;</td><td><b>~90 per cent</b></td></tr>
  </table>
  @@FUNDUS@@

  <p><b>Diabetic retinopathy</b> is the leading cause of new-onset blindness in United States
  adults <b>20 to 74</b> &mdash; a different age band from macular degeneration, and an easy pair
  to swap. Chronic hyperglycaemia damages capillaries and endothelial basement membranes &rarr;
  capillary occlusion and hypoxia. <b>Non-proliferative:</b> dilated veins, microaneurysms, dot and
  blot haemorrhages, <b>hard exudates</b> (lipid in the outer plexiform layer), <b>cotton-wool
  spots</b> (nerve fibre layer ischaemia), macular oedema. <b>Proliferative:</b> severe ischaemia
  upregulates <b>vascular endothelial growth factor</b> &rarr; neovascularisation on disc and
  retina &rarr; vitreous haemorrhage, fibrotic traction, tractional detachment.</p>
  @@OCT@@

  <h3 class="sub" id="l4-fields">4.6 &middot; Objective j &mdash; Visual field deficits by lesion site</h3>
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Know for Exam &mdash; stated</span>
    <p>On his list &mdash; <em>&ldquo;know those areas of changes in your visual pathway, what
    would cause a particular visual change&rdquo;</em> &mdash; but <b>scoped</b>. He said twice to
    know <b>A, B and C</b>. D and E he deferred: <em>&ldquo;this is getting more into neurology,
    which we&rsquo;ll see later.&rdquo;</em> He also said <em>&ldquo;memorise this: optic nerve,
    optic chiasm, optic tract.&rdquo;</em></p>
  </div>
  <p><b>The decussation is the key.</b> <b>Nasal</b> retinal fibres &mdash; which carry the
  <b>temporal</b> visual fields &mdash; cross at the chiasm. <b>Temporal</b> retinal fibres stay
  ipsilateral. Everything below follows from that one fact. The pathway runs optic disc &rarr;
  optic nerve &rarr; chiasm &rarr; optic tract &rarr; lateral geniculate nucleus &rarr; optic
  radiation &rarr; occipital cortex.</p>
  <table class="tbl">
    <tr><th>Site</th><th>Lesion</th><th>Cause</th><th>Field defect</th></tr>
    <tr><td><b>A</b></td><td>Ipsilateral optic nerve</td><td>Trauma, optic neuritis, ischaemic optic neuropathy</td><td><b>Monocular blindness</b></td></tr>
    <tr><td><b>B</b></td><td>Optic chiasm (centre)</td><td><b>Pituitary adenoma</b> compression</td><td><b>Bitemporal hemianopsia</b> &mdash; only the crossing nasal fibres are cut, so both temporal fields go</td></tr>
    <tr><td><b>C</b></td><td>Optic tract / lateral geniculate</td><td>Stroke, tumour, demyelination</td><td><b>Contralateral homonymous hemianopsia</b></td></tr>
    <tr><td class="muted">D</td><td class="muted">Temporal optic radiation</td><td class="muted">Temporal lobe lesion or surgery</td><td class="muted">Contralateral superior quadrantanopsia &mdash; &ldquo;pie in the sky&rdquo;</td></tr>
    <tr><td class="muted">E</td><td class="muted">Occipital cortex</td><td class="muted">Posterior cerebral artery occlusion</td><td class="muted">Contralateral homonymous hemianopsia <b>with macular sparing</b> (dual supply)</td></tr>
  </table>
  <p class="muted">D and E are greyed because he deferred them to neurology. They are on the slide,
  so they are here &mdash; but A, B and C carry the weight.</p>
  @@FIELDS@@
  <p>One more consequence he drew out: losing vision in one eye costs the <b>binocular overlap</b>,
  and with it <b>depth perception</b>. Everything becomes flat.</p>
</section>
"""

TOC = """  <a class="top-link" href="#ophthalmic-pathophys">4 &middot; Ophthalmic Pathophysiology</a>
  <a class="sub-link" href="#l4-anatomy">4.1 Anatomy &amp; physiology of vision</a>
  <a class="sub-link" href="#l4-refractive">4.2 Globe shape &amp; age-related</a>
  <a class="sub-link" href="#l4-cataract">4.3 Cataract</a>
  <a class="sub-link" href="#l4-glaucoma">4.4 Glaucoma</a>
  <a class="sub-link" href="#l4-retina">4.5 Detachment &amp; macular degeneration</a>
  <a class="sub-link" href="#l4-fields">4.6 Visual field deficits</a>
"""

TESTS = """    ophthalmic: [
      {q:"What is the pathophysiological explanation for vision loss in glaucoma?",
       o:["Raised pressure compresses ganglion cell axons, causing apoptosis and disc cupping",
          "Raised pressure opacifies the lens","Raised pressure detaches the retina",
          "Raised pressure drives new vessel growth"],a:0,
       why:"He asked for exactly this chain. The loss is nerve loss, not media opacity."},
      {q:"Myopia: what is the globe geometry and where does the image land?",
       o:["Globe too LONG, image in FRONT of the retina","Globe too SHORT, image BEHIND the retina",
          "Globe normal, cornea irregular","Globe normal, lens stiffened"],a:0,
       why:"He asked for the geometry rather than the lens. Long globe overshoots."},
      {q:"Which three mechanisms cause retinal detachment?",
       o:["Rhegmatogenous (tear), tractional (membranes pull), exudative (fluid, no tear)",
          "Ischaemic, haemorrhagic and infective","Congenital, traumatic and neoplastic",
          "Osmotic, oxidative and inflammatory"],a:0,
       why:"He asked for &ldquo;the different things that can cause retinal detachment&rdquo;."},
      {q:"What is the hallmark of DRY macular degeneration?",
       o:["Drusen beneath the retinal pigment epithelium","Choroidal neovascularisation",
          "Cotton-wool spots","Optic disc cupping"],a:0,
       why:"Drusen are lipofuscin and apolipoprotein debris under the pigment epithelium."},
      {q:"A central optic chiasm lesion gives which defect, and why?",
       o:["Bitemporal hemianopsia &mdash; only the crossing NASAL fibres are cut, and they carry the TEMPORAL fields",
          "Monocular blindness &mdash; the lesion is before the crossing",
          "Homonymous hemianopsia &mdash; the lesion is after the crossing",
          "Superior quadrantanopsia &mdash; only part of the radiation is involved"],a:0,
       why:"Site B. Commonest cause is a pituitary adenoma."},
      {q:"Which three lesion sites did he say to know best?",
       o:["Optic nerve, optic chiasm, optic tract","Optic radiation, geniculate, occipital cortex",
          "Retina, optic disc, optic nerve","Chiasm, radiation, cortex"],a:0,
       why:"Said twice. D and E &mdash; radiation and cortex &mdash; he deferred to neurology."},
      {q:"Why does presbyopia stop accommodation?",
       o:["The lens hardens with age and can no longer change shape",
          "The globe shortens with age","The cornea flattens with age",
          "The pupil stops constricting"],a:0,
       why:"The one he came back for after saying he was finished. Tied to the A in PERRLA."},
      {q:"How does diabetes cause cataract?",
       o:["Glucose is converted to sorbitol, causing osmotic swelling of the lens",
          "Crystallin proteins aggregate directly","The lens capsule ruptures",
          "Vascular endothelial growth factor is released into the lens"],a:0,
       why:"Sorbitol is the diabetic mechanism; crystallin aggregation is the senile one."}
    ],
"""

FIGS = {
    "@@DETACH@@": ("detachment", "png",
                   "Rhegmatogenous detachment: liquefied vitreous passing through a "
                   "retinal tear and peeling the neurosensory retina off the pigment "
                   "epithelium.", 35),
    "@@FUNDUS@@": ("normal-fundus", "jpg",
                   "A normal fundus for comparison &mdash; note the sharp disc margin and "
                   "the macula temporal to it.", 29),
    "@@OCT@@": ("oct", "jpg",
                "Optical coherence tomography, showing the retinal layers in section.", 30),
    "@@FIELDS@@": ("visual-fields", "png",
                   "Lesion sites A to E against the resulting monocular fields. "
                   "<b>A, B and C are the ones he said to know</b>; D and E he deferred "
                   "to neurology.", 34),
}


def main():
    src = open(GUIDE, encoding="utf-8").read()
    for o, cl in (("<!--CPL4-->", "<!--/CPL4-->"), ("<!--CPTOC4-->", "<!--/CPTOC4-->"),
                  ("<!--CPTY4-->", "<!--/CPTY4-->")):
        if o in src:
            src = re.sub(re.escape(o) + r".*?" + re.escape(cl), "", src, flags=re.S)

    body = BODY
    for token, (slug, ext, cap, slide) in FIGS.items():
        assert token in body, "figure token %s unused" % token
        body = body.replace(token, fig(slug, ext, cap, slide))
    assert "@@" not in body, "unfilled figure token"

    # the seven he named must each appear in the flagged block
    flagged = "\n".join(re.findall(r'<div class="prof-flag">.*?</div>', body, re.S))
    for t in KFE:
        assert t.split()[-1].lower() in flagged.lower(), (
            "%r is on his stated exam list but is not inside a "
            "\"Know for Exam - stated\" block" % t)

    j = src.index("</main>")
    src = src[:j] + "<!--CPL4-->" + body + "<!--/CPL4-->\n\n" + src[j:]
    k = src.index("</nav>")
    src = src[:k] + "<!--CPTOC4-->\n" + TOC + "<!--/CPTOC4-->\n" + src[k:]
    m = src.index("var TEST_YOURSELF = {")
    m = src.index("\n", m) + 1
    src = src[:m] + "<!--CPTY4-->\n" + TESTS + "<!--/CPTY4-->\n" + src[m:]

    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li",
                "figure", "figcaption"):
        o = len(re.findall(r"<%s[ >]" % tag, src)); c = src.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for fn in re.findall(r'src="%s/([^"]+)"' % IMG, body):
        assert os.path.exists(os.path.join(DIR, IMG, fn)), fn

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 4: %d subsections, %d figures, %d \"Know for Exam\" blocks, "
          "%d test-yourself questions"
          % (body.count('class="sub"'), body.count("<figure"),
             body.count('prof-flag-label'), TESTS.count("{q:")))


if __name__ == "__main__":
    main()
