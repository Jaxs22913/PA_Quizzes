#!/usr/bin/env python3
"""Add the Lecture 2 (Principles of Medical Imaging) section to the PDM I guide.

Incremental patcher over the guide that build_pdm_guide.py produces, in the same
shape as build_cms_guide_derm.py: fenced in <!--PDML2--> markers and stripped
before re-inserting, so it is idempotent and survives a guide rebuild being run
after it.

Instructional Objectives are quoted VERBATIM from the PAJ 5600 syllabus (topic
outline 2, objectives a-i) per the guide verbatim-IO rule, and each subsection
answers one or more in order.

Figures come from extract_pdm_l2_figures.py. Two of them -- the Hounsfield table
and the organ-dose table -- are the ONLY source for their content anywhere in
the deck; the extracted text has neither.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from extract_pdm_l2_figures import figure_html

GUIDE = os.path.join(os.path.dirname(HERE), "Principles of Diagnostic Medicine I Exam 1",
                     "pdm-exam-1-study-guide.html")
# stems are hyphenated; underscores read better inside a %(name)s placeholder
F = {k.replace("-", "_"): v for k, v in figure_html("pdm-exam-1-l2-images").items()}
OPEN, CLOSE = "<!--PDML2-->", "<!--/PDML2-->"
TOC_OPEN, TOC_CLOSE = "<!--PDML2TOC-->", "<!--/PDML2TOC-->"

TOC = '''%s
  <a class="top-link" href="#medical-imaging">2 &middot; Principles of Medical Imaging</a>
  <a href="#mi-fundamentals">2.1 Objective a &mdash; Fundamental properties &amp; the diagnostic approach</a>
  <a href="#mi-modalities">2.2 Objective b &mdash; The modalities, one at a time</a>
  <a href="#mi-structures">2.3 Objective c &mdash; Which study for which structure</a>
  <a href="#mi-density">2.4 Objective d &mdash; Density, contrast &amp; the Hounsfield scale</a>
  <a href="#mi-positioning">2.5 Objective e &mdash; Positioning &amp; the imaging planes</a>
  <a href="#mi-radiation">2.6 Objective f &mdash; Risks &amp; benefits of radiation exposure</a>
  <a href="#mi-contrast">2.7 Objectives g &amp; h &mdash; Contrast media, contraindications &amp; safety</a>
  <a href="#mi-radiology">2.8 Objective i &mdash; Working with the radiology team</a>
%s''' % (TOC_OPEN, TOC_CLOSE)

# Mapping-style placeholders (%(name)s) are figures; the fences are concatenated
# rather than formatted in, so the two kinds of % never collide.
BODY_TMPL = '''<section class="deck" id="medical-imaging">
  <h2 class="deck-title">2 &middot; Principles of Medical Imaging</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">Topic Outline 2: Principles of Medical Imaging</p>
    <ol type="a">
      <li>Identify the fundamental properties of medical imaging.</li>
      <li>Describe the function and clinical applications of: Radiography, Ultrasonography,
      Computed Tomography (CT), Magnetic Resonance Imaging (MRI), Magnetic Resonance Angiography
      (MRA), Positron Emission Tomography (PET), Single Photon Emission Computed Tomography
      (SPECT), Angiographic studies.</li>
      <li>Discuss anatomical structures best visualized by each imaging modality.</li>
      <li>Compare and contrast the concepts of radiographic density and contrast.</li>
      <li>Discuss the importance of patient positioning in medical imaging.</li>
      <li>Compare and contrast the risks and benefits associated with radiation exposure.</li>
      <li>Compare and contrast the risks and benefits associated with contrast administration.</li>
      <li>Discuss contraindications and safety considerations of commonly used imaging modalities.</li>
      <li>Discuss the importance of communication between the physician assistant and radiology team.</li>
    </ol>
  </div>

  <div class="callout"><b>Two slides in this deck are pictures of tables, and their content
  appears nowhere in the text.</b> Slide 13 carries the Hounsfield numbers and slide 21 carries the
  typical organ radiation doses &mdash; slide 21 in fact extracts as completely blank. Both are
  reproduced below. If you are studying from a text export of the deck rather than the slides
  themselves, those two tables are the ones you will be missing.</div>

  <h3 class="sub" id="mi-fundamentals">2.1 &middot; Objective a &mdash; Fundamental properties &amp; the diagnostic approach</h3>
  <p>Wilhelm R&ouml;ntgen discovered x-rays in Germany in 1895 and took the first Nobel Prize for
  Physics for it in 1901 &mdash; which is why the technique is still called roentgenography. Every
  modality since answers the same four questions before it is ordered:</p>
  <table>
    <tr><th>The question</th><th>What it is really asking</th></tr>
    <tr><td>Which modality is best for ruling the diagnosis in or out?</td><td>Match the study to the tissue and the question, not to habit.</td></tr>
    <tr><td>Is there an alternative with less radiation?</td><td>Ultrasound and magnetic resonance use none at all.</td></tr>
    <tr><td>Risk versus benefit, and patient-specific implications?</td><td>Pregnancy, age, renal function, implanted devices.</td></tr>
    <tr><td>Does this need contrast, or can it be non-contrast?</td><td>Contrast adds information and adds risk.</td></tr>
  </table>
  <p>A <b>conventional radiograph</b> is an image made with ionizing radiation and <em>without</em>
  added contrast such as barium or iodine. It needs a source, a way to record the image and a way
  to process it; radiation and light strike a photosensitive surface, producing a latent image that
  is processed to become visible. Radiographs are quick, inexpensive and obtainable anywhere, which
  is why they are the most widely obtained imaging studies &mdash; against a limited range of
  densities and a reliance on ionizing radiation, albeit at relatively low dose.</p>

  <h3 class="sub" id="mi-modalities">2.2 &middot; Objective b &mdash; The modalities, one at a time</h3>
  <table>
    <tr><th>Modality</th><th>How the image is made</th><th>Advantages</th><th>Disadvantages</th></tr>
    <tr><td><b>Radiography</b></td><td>Ionizing radiation through the body onto a detector, viewed in two dimensions</td><td>Quick, inexpensive, available anywhere, portable</td><td>Only five densities; ionizing radiation; structures overlap</td></tr>
    <tr><td><b>Computed tomography</b></td><td>Powerful x-ray beams through a rotating fan beam, measuring transmission at thousands of points</td><td>Expands the grey scale beyond five densities, reduces overlap, works with implanted devices, three-dimensional reconstruction; the cornerstone of cross-sectional imaging</td><td>Not truly portable, a lot of ionizing radiation, needs space and heavy processing</td></tr>
    <tr><td><b>Ultrasonography</b></td><td>High-frequency sound from a transducer, bounced off tissue and back to it</td><td>Inexpensive, portable, no radiation, real time, colour Doppler for flow direction and velocity</td><td>Cannot penetrate bone, gas disrupts the signal, deep structures are hard, operator-dependent</td></tr>
    <tr><td><b>Magnetic resonance</b></td><td>A varying magnetic field aligns hydrogen; releasing it emits radio waves &mdash; essentially a hydrogen map</td><td>No radiation, superior to computed tomography for soft tissue, calcium is silent so tissue inside bone is visible, diffusion-weighted imaging for stroke</td><td>Not widely available, expensive, slow, magnetic implants and ferromagnetic projectiles</td></tr>
    <tr><td><b>Positron emission tomography</b></td><td>Gamma camera reading an injected tracer, usually fluorodeoxyglucose-18; two-dimensional</td><td>Shows which tissues consume more glucose &mdash; cancer staging, brain disorders, cardiac blood flow</td><td>Among the highest-emitting devices in existence</td></tr>
    <tr><td><b>Single photon emission tomography</b></td><td>Gamma cameras on a rotating gantry reading single photons; three-dimensional</td><td>Shows where blood flows &mdash; heart disease, bone scans, brain evaluation</td><td>Among the highest-emitting devices in existence</td></tr>
    <tr><td><b>Angiographic studies</b></td><td>Not one test: x-ray angiogram, colour Doppler, computed tomography angiography, magnetic resonance angiography</td><td>Images vessels by whichever modality suits; magnetic resonance angiography and venography need no dye at all</td><td>Inherits the risks of whichever modality is used</td></tr>
    <tr><td><b>Fluoroscopy</b></td><td>Ionizing radiation giving real-time video of the body</td><td>Evaluates motion and positioning; watches barium or iodine move through the gut, urinary tract and vessels</td><td>Needs a specially fitted unit with a tilting table; continuous radiation</td></tr>
  </table>
  %(t1_t2_tesla)s
  <div class="pearl"><b>The one magnetic resonance fact that is always asked.</b> On <b>T2</b>, high
  water content is <b>bright</b>; on <b>T1</b>, high water content is <b>dark</b>. Fat, oedema,
  infection, blood and cerebrospinal fluid all follow water. Two mnemonics, pick one: <em>T2 = H2O
  is white</em>, or just look at the ventricles in the figure above.</div>
  %(ultrasound_indicator)s

  <h3 class="sub" id="mi-structures">2.3 &middot; Objective c &mdash; Which study for which structure</h3>
  <table>
    <tr><th>What you want to see</th><th>What the deck says to use</th></tr>
    <tr><td>Moving structures &mdash; heart, vasculature, obstetrics</td><td>Ultrasound, which records in real time</td></tr>
    <tr><td>Female pelvis, and paediatric patients</td><td>Ultrasound, often the first study of choice; also for image-guided procedures</td></tr>
    <tr><td>Soft tissue &mdash; essentially anything other than bone</td><td>Magnetic resonance, with extremely high anatomical detail</td></tr>
    <tr><td>Brain, and the soft tissues of orthopaedics &mdash; muscle, ligament, tendon</td><td>Magnetic resonance; it is the cornerstone of neuroimaging</td></tr>
    <tr><td>Tissue surrounded by bone</td><td>Magnetic resonance &mdash; calcium emits no signal, so the bone does not obscure it</td></tr>
    <tr><td>Anything cross-sectional</td><td>Computed tomography, the foundation of cross-sectional imaging</td></tr>
    <tr><td>Pleural effusion</td><td>Chest radiograph in the <b>decubitus</b> position, so the fluid layers out</td></tr>
    <tr><td>Genitourinary tract</td><td>Kidney-ureter-bladder film &mdash; supine, anterior-posterior</td></tr>
    <tr><td>Gastrointestinal tract, free air, air-fluid levels</td><td>Abdominal series &mdash; standing, anterior-posterior; for obstruction, perforation, volvulus</td></tr>
    <tr><td>Which organs are consuming glucose</td><td>Positron emission tomography</td></tr>
    <tr><td>Where blood is flowing</td><td>Single photon emission tomography, or colour Doppler</td></tr>
  </table>
  <div class="callout"><b>A note on slide 34.</b> &ldquo;Anatomical Structures Best Visualized
  by&hellip;&rdquo; is a two-column layout that pairs seventeen modality entries against six
  anatomical categories, and the pairing does not survive being pulled out of the file &mdash; the
  columns come out as two separate lists. Every row in the table above is instead taken from a
  slide that states the claim in a sentence. If your own notes disagree with a row here, trust the
  slide in front of you: this is the one place in the lecture where the deck is genuinely hard to
  read mechanically.</div>

  <h3 class="sub" id="mi-density">2.4 &middot; Objective d &mdash; Density, contrast &amp; the Hounsfield scale</h3>
  %(five_densities)s
  %(radiodensity_labelled)s
  <p><b>The vocabulary.</b> <em>Radiolucent</em> and <em>hypodense</em> both mean the image looks
  darker, because more x-ray photons passed through and less was absorbed. <em>Radiopaque</em>,
  <em>hyperdense</em> and <em>radiodense</em> all mean it looks whiter, because less passed through
  and more was absorbed. Radiation itself is measured in millisieverts and milligrays.</p>
  %(hounsfield_numbers)s
  <p>A computed tomography image is a matrix of thousands of tiny squares &mdash; pixels &mdash;
  each assigned a number from &minus;1000 to +1000 in Hounsfield units, according to how much of
  the beam that point absorbed. <b>Water is zero by convention</b> and everything else is placed
  relative to it.</p>
  <table>
    <tr><th>Term</th><th>On computed tomography</th><th>The same substance on a plain film</th></tr>
    <tr><td><b>Increased attenuation</b></td><td>High Hounsfield number, appears whiter &mdash; metal, calcium</td><td>Increased density; more opaque, radiopaque</td></tr>
    <tr><td><b>Decreased attenuation</b></td><td>Low Hounsfield number, appears blacker &mdash; air, fat</td><td>Decreased density; increased lucency</td></tr>
  </table>
  <div class="pearl"><b>The window is a display choice, not an acquisition choice.</b> A window is a
  pre-selected range of Hounsfield numbers &mdash; say &minus;100 to +300 &mdash; spread across the
  available grey scale so the tissue of interest is separable. Because it is only a display range,
  the same scan can be re-windowed afterwards to bring out different pathology. That is
  <b>post-processing</b>, and its clinical value is that it demonstrates the abnormality
  <em>without repeating the study and without re-exposing the patient</em>.</div>

  <h3 class="sub" id="mi-positioning">2.5 &middot; Objective e &mdash; Positioning &amp; the imaging planes</h3>
  <p>Projections are named <b>in the direction the beam travels</b>, from what it strikes first to
  the most distal portion. So posterior-anterior means the beam enters the back and leaves the
  front.</p>
  %(pa_vs_ap)s
  <table>
    <tr><th>Position</th><th>How</th><th>What it is for</th></tr>
    <tr><td>Posterior-anterior</td><td>Standing, beam from behind; usually combined with a lateral</td><td>The standard chest film</td></tr>
    <tr><td>Lateral</td><td>Side-on; the patient faces to the left on the view</td><td>Read together with the posterior-anterior film</td></tr>
    <tr><td>Lateral decubitus</td><td>Lying on one side</td><td>Pleural effusion &mdash; the fluid levels out with gravity</td></tr>
    <tr><td>Anterior-posterior</td><td>Beam from the front</td><td>Used when a patient cannot stand for a posterior-anterior film</td></tr>
    <tr><td>Kidney-ureter-bladder</td><td>Supine, anterior-posterior</td><td>Genitourinary tract</td></tr>
    <tr><td>Abdominal series</td><td>Standing, anterior-posterior</td><td>Gastrointestinal tract; air-fluid levels, free air, obstruction, perforation, volvulus</td></tr>
  </table>
  <div class="pearl"><b>The standard chest examination is a pair.</b> A posterior-anterior and a
  lateral, <em>read together</em>. The posterior-anterior film is viewed as if the patient were
  standing in front of you, <b>their right side on your left</b>. And comparison films are &ldquo;old
  gold&rdquo; &mdash; when you have them, the old posterior-anterior goes beside the new
  posterior-anterior and the old lateral beside the new lateral.</div>
  %(decubitus_effusion)s
  %(imaging_planes)s
  <p>For computed tomography, nuclear medicine and magnetic resonance the patient is <b>supine</b>,
  and traditional images are transverse sections viewed <em>as if you were looking at the patient's
  feet</em> &mdash; so the <b>patient's left side is on the reader's right</b>. Ultrasound has dozens
  of positions depending on the structure and the complaint, most of them some variety of supine.</p>

  <h3 class="sub" id="mi-radiation">2.6 &middot; Objective f &mdash; Risks &amp; benefits of radiation exposure</h3>
  %(organ_doses)s
  <p>Dose is ionizing energy absorbed per unit of mass, expressed in grays or milligrays &mdash;
  one gray is one joule per kilogram &mdash; and often as an equivalent dose in sieverts or
  millisieverts. For the x-ray radiation used in computed tomography scanners, <b>one millisievert
  equals one milligray</b>, which is why the table above can label a single column with either.</p>
  <div class="pearl"><b>Computed tomography, positron emission tomography and single photon
  emission tomography are the highest-emitting medical imaging devices currently in existence.</b>
  The deck marks this one IMPORTANT. Ultrasound and magnetic resonance emit no ionizing radiation
  at all; plain radiography does, but at relatively low dose.</div>
  <p><b>Nuclear medicine is different in kind, not just in amount.</b> In every other modality the
  machine is the source and the exposure stops when the study stops. In nuclear medicine the tracer
  is inside the patient, so for a while <em>the patient is the source</em> &mdash; they can briefly
  expose other people. That is the one radiation fact unique to these studies.</p>

  <h3 class="sub" id="mi-contrast">2.7 &middot; Objectives g &amp; h &mdash; Contrast media, contraindications &amp; safety</h3>
  <p>Contrast is used most often to image arteries or veins, and to delineate and characterise
  masses &mdash; neoplastic against benign, infectious abscess against cyst. It also shows
  inflammation, increased blood flow and increased cellular or metabolic activity, and outlines
  luminal structures when given by mouth or as an enema. It can be injected into joints
  (arthrogram), into the central nervous system (intrathecal) and into the bladder (retrograde
  pyelogram). Because the dyes are technically radioactive, the deck names <b>cancer as a risk
  factor for all contrast material</b>.</p>
  <table>
    <tr><th>Study</th><th>Agent</th><th>Before you give it</th><th>Watch for</th></tr>
    <tr><td>Computed tomography, intravenous</td><td>Omnipaque (iohexol) &mdash; a radioactive form of iodine</td><td><b>Check blood urea nitrogen and creatinine</b>; give one litre of normal saline to protect the kidneys</td><td>Nephrotoxicity. Indicated for inflammation, cancer staging, tumour delineation, vasculopathy, emboli, thrombi, stenosis, aneurysm</td></tr>
    <tr><td>Angiography</td><td>Iohexol arterially, lower concentration than for intravenous computed tomography; iso-osmolal iodixanol (Visipaque) believed safer</td><td>Same renal checks</td><td>Same iodinated risks</td></tr>
    <tr><td>Computed tomography, oral</td><td>Barium, or Gastrografin</td><td><b>Barium is contraindicated if perforation is suspected</b> &mdash; use Gastrografin</td><td>Barium is toxic to extra-intestinal tissue and causes alkaline burns. Unpleasant taste</td></tr>
    <tr><td>Fluoroscopy swallow study</td><td>Oral barium, with sequential films</td><td>Same perforation caveat</td><td>Same</td></tr>
    <tr><td>Magnetic resonance</td><td>Gadolinium</td><td>Assess blood urea nitrogen and creatinine regardless &mdash; renal function matters mainly for clearance</td><td>Can damage kidneys, but <em>not as harmful</em> as computed tomography contrast. For central nervous system tumours, metastases, soft tissue masses, arthrograms. Magnetic resonance angiography and venography need <b>no</b> contrast</td></tr>
    <tr><td>Positron emission tomography</td><td>Fluorodeoxyglucose-18</td><td>Nothing specific</td><td>No contraindications, not known to be nephrotoxic; may cause hyperglycaemia; renally cleared, so the genitourinary tract is always contrast positive</td></tr>
    <tr><td>Single photon emission tomography</td><td>Technetium-99</td><td>Nothing specific</td><td>Allergic reactions rare, no organ damage documented. Bone scans, myocardial perfusion, functional brain imaging, immunoscintigraphy, sentinel node identification, white cell uptake</td></tr>
  </table>
  <div class="pearl"><b>Shellfish allergy is not iodine allergy.</b> The deck is explicit: there
  should be <b>no cross-reactivity</b> between shellfish and iodinated radiocontrast. What actually
  marks a high-risk patient is a documented <b>anaphylactic reaction to any medication</b>. And
  when contrast is genuinely necessary, pre-treatment is available. The stated takeaway:
  <b>always ask about allergies and assess kidney function.</b></div>

  <h3 class="sub" id="mi-radiology">2.8 &middot; Objective i &mdash; Working with the radiology team</h3>
  <ul>
    <li><b>The radiologist has not seen the patient.</b> Whatever you give them is what guides the
    read, so give as much relevant clinical information as you can.</li>
    <li><b>A vague report is a conversation, not a dead end.</b> Contact the radiologist and discuss
    the patient.</li>
    <li><b>If you do not know which study to order, say what you are looking for.</b> They can guide
    the choice; that is what the relationship is for.</li>
    <li><b>Imaging several regions may mean several orders</b> &mdash; magnetic resonance of brain,
    cervical spine, thoracic spine and lumbar spine is four requests, not one.</li>
  </ul>

  <button type="button" class="test-yourself-btn" style="--acc:#69406c" onclick="window.openTestYourself('Test yourself &mdash; Medical Imaging', TEST_YOURSELF.medicalimaging)">Test yourself! &rarr;</button>
  <footer class="guide-foot">Source: <em>2. svPrinciples of Medical Imaging.pptx</em>
  (Professor Lauren M. Reynolds, MSPA, PA-C, Course Director), Slides 1&ndash;62, and the PAJ 5600
  syllabus instructional objectives. Figures are reproduced from the lecture slides and each is
  cited to its slide; the Hounsfield and organ-dose tables exist in the deck only as images. There
  was no lecture recording available for this topic when this section was written, so nothing here
  is weighted by spoken emphasis &mdash; only by what the deck spends slides on.</footer>
</section>'''

TESTS = '''    medicalimaging: [
      {q:"On the Hounsfield scale, what number is water assigned?",
       choices:["0","-1000","+1000","+100"],correct:0,
       expl:"Water is zero by convention, and every other tissue is placed relative to it. Air is -1000, metal is +1000 or higher."},
      {q:"A patient needs a chest film. Why is the posterior-anterior view preferred over anterior-posterior?",
       choices:["It reduces magnification of the heart, so cardiomegaly is not misread","It uses a shorter exposure, so there is less motion blur","It removes the need for a lateral view","It is the only view that shows the costophrenic angles"],correct:0,
       expl:"The heart is anterior, so on a posterior-anterior film it sits close to the detector and is not magnified. The view also lowers dose to radiation-sensitive organs and shows the lung fields, apices and posterior ribs better. It is still combined with a lateral."},
      {q:"On a T2-weighted magnetic resonance image, how does cerebrospinal fluid appear?",
       choices:["Bright","Dark","Grey, the same as white matter","It emits no signal"],correct:0,
       expl:"On T2 high water content is bright; on T1 it is dark. Fat, oedema, infection and blood follow water. Calcium is the one that emits no signal at all."},
      {q:"Perforation is suspected. Which oral contrast agent must NOT be used?",
       choices:["Barium","Gastrografin","Iohexol","Gadolinium"],correct:0,
       expl:"Barium is toxic to extra-intestinal tissue and causes alkaline burns, so Gastrografin is used instead when there may be a perforation."},
      {q:"A patient reports a shellfish allergy before a contrast-enhanced computed tomography scan. What does the lecture say?",
       choices:["There should be no cross-reactivity between shellfish and iodinated contrast","Contrast is absolutely contraindicated","Give half the usual concentration","Switch to gadolinium instead"],correct:0,
       expl:"The deck rejects the cross-reactivity idea explicitly. The real high-risk marker is a documented anaphylactic reaction to ANY medication, and pre-treatment exists when contrast is necessary. Always ask about allergies and assess kidney function."},
      {q:"Which position is used to evaluate a pleural effusion?",
       choices:["Lateral decubitus","Supine anterior-posterior","Standing posterior-anterior alone","Prone"],correct:0,
       expl:"Lying the patient on their side lets gravity move free pleural fluid into a layer along the dependent chest wall, where it can be seen. Upright films are what show free air and air-fluid levels."},
      {q:"Which of these delivers the highest organ dose in the lecture's table?",
       choices:["Neonatal abdominal computed tomography","Adult abdominal computed tomography","Barium enema","Screening mammography"],correct:0,
       expl:"Twenty against the adult scan's ten \\u2014 the smaller the patient, the higher the organ dose for the same study. That is the whole reason the diagnostic approach asks whether something with less radiation would do."},
      {q:"You are looking at a traditional axial computed tomography slice. Where is the patient's left side?",
       choices:["On your right","On your left","At the top of the image","It depends on the scanner"],correct:0,
       expl:"The convention is as if you were looking at the patient's feet, so their left is on your right. Note this is the OPPOSITE way round from a posterior-anterior chest film, which is viewed as if the patient were facing you."},
      {q:"Which vascular study requires no contrast agent at all?",
       choices:["Magnetic resonance angiography","Computed tomography angiography","Coronary angiogram","Retrograde pyelogram"],correct:0,
       expl:"Magnetic resonance angiography and venography image the vessel walls without dye. Computed tomography angiography needs iodine injected quickly."},
      {q:"What is unique about radiation exposure from a nuclear medicine study?",
       choices:["The patient can briefly become a source of exposure to other people","The dose is confined to the organ studied","It is measured in different units","The exposure is delivered in a single pulse"],correct:0,
       expl:"The tracer is inside the patient, so the emission travels with them. In every other modality the machine is the source and exposure ends with the study."}
    ],
'''


def main():
    src = open(GUIDE, encoding="utf-8").read()
    # idempotent: strip any previous insertion first
    src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", src, flags=re.S)
    src = re.sub(re.escape(TOC_OPEN) + r".*?" + re.escape(TOC_CLOSE), "", src, flags=re.S)
    src = re.sub(r"[ \t]*medicalimaging: \[.*?\n    \],\n", "", src, flags=re.S)

    body = OPEN + "\n\n" + (BODY_TMPL % F) + "\n\n" + CLOSE

    # TOC: after the last existing top-level link block, before </nav>
    i = src.index("</nav>")
    src = src[:i] + TOC + "\n" + src[i:]

    # BODY: immediately before </main>
    j = src.index("</main>")
    src = src[:j] + "\n" + body + "\n\n" + src[j:]

    # TEST_YOURSELF: as a new key on the existing object
    k = src.index("var TEST_YOURSELF = {")
    k = src.index("\n", k) + 1
    src = src[:k] + TESTS + src[k:]

    assert src.count(OPEN) == src.count(CLOSE) == 1
    assert "%(" not in body, "an unfilled figure placeholder survived"
    assert not [t for t in re.findall(r"<img\b[^>]*>", body) if "lazy" in t]
    for fn in re.findall(r'src="pdm-exam-1-l2-images/([^"]+)"', body):
        p = os.path.join(os.path.dirname(GUIDE), "pdm-exam-1-l2-images", fn)
        assert os.path.exists(p), "missing figure file %s" % fn

    open(GUIDE, "w", encoding="utf-8").write(src)
    print("added section 2 (%d figures, %d subsections, %d test-yourself questions)"
          % (body.count("<figure"), body.count('class="sub"'), TESTS.count("{q:")))


if __name__ == "__main__":
    main()
