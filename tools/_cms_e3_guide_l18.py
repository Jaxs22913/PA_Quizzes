# -*- coding: utf-8 -*-
"""Section 4 of the CMS I Exam 3 guide -- Neoplasms and Neck Masses (L18).

Prof. Chand Shah. Generated from _cms_e3_chart_l18.py, like sections 1-3, so
the guide and the chart cannot drift.

BUILT WITHOUT AUDIO. No recording for this lecture is in the inbox; Jaxon asked
for the build to go ahead on the slides alone. Nothing below depends on spoken
emphasis.

THREE THINGS ARE WRITTEN BY HAND. The neck anatomy opens the section, because
the first two syllabus objectives are anatomy -- the triangles and the lymph
nodes -- and no condition row carries them. The KITTENS differential and the
red-flag list from slide 13 open the clinical half, because they are the
lecture's own framework for every row that follows. And slide 38 is a PICTURE
of a table, so the primary-tumour list is transcribed rather than lost.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cms_e3_chart_l18 import ROWS_L18, DIFF_L18, IMGS_L18

IMGDIR = "cms-ent-chart-images"
OUTDIR = "Clinical Medicine and Surgery I Exam 3"

ORDER = [
 ("l18-cong", "4.3 &middot; Congenital neck masses",
  ["Branchial cleft cyst", "Thyroglossal duct cyst", "Dermoid cyst", "Plunging ranula",
   "Laryngocele", "Lymphangioma (cystic hygroma)", "Haemangioma", "Teratoma", "Thymic cyst",
   "Sternocleidomastoid tumour of infancy"]),
 ("l18-infl", "4.4 &middot; Inflammatory neck masses",
  ["Reactive viral lymphadenopathy", "HIV-associated cervical adenopathy",
   "Suppurative bacterial lymphadenopathy", "Cat scratch disease", "Toxoplasmosis", "Tularemia",
   "Brucellosis", "Actinomycosis", "Atypical mycobacteria", "Tuberculous adenitis (scrofula)",
   "Fungal neck infection"]),
 ("l18-neo", "4.5 &middot; Neoplastic neck masses",
  ["Neck neoplasm &mdash; general", "Primary neck tumours &mdash; the list"]),
 ("l18-thy", "4.6 &middot; The thyroid",
  ["Thyroid nodule and mass", "Papillary thyroid carcinoma", "Follicular thyroid carcinoma",
   "Medullary thyroid carcinoma", "Anaplastic thyroid carcinoma", "Primary thyroid lymphoma"]),
]

ROW = {r[0]: r for r in ROWS_L18}


def _fig(name):
    pic = IMGS_L18.get(name)
    if not pic:
        return ""
    fn, sl = pic
    if not os.path.exists(os.path.join(OUTDIR, IMGDIR, fn)):
        return ""
    return ('<figure class="fig"><img src="%s/%s" loading="lazy" alt="%s, from the lecture '
            'slides."><figcaption>%s <span class="cite">L18 slide %d</span></figcaption></figure>'
            % (IMGDIR, fn, name.replace("&mdash;", "-"), name, sl))


def _condition(name):
    n, grp, give, pres, test, tx, urg, edu, slides, _deck = ROW[name]
    pain, where, sign = DIFF_L18[name]
    ucls = ("emerg" if "EMERGENT" in urg.upper() else
            "urg" if "URGENT" in urg.upper() else "rout")
    return (
      '<div class="cond"><h4>%s <span class="u %s">%s</span></h4>%s'
      '<p class="give"><b>Gives itself away by:</b> %s</p>'
      '<dl class="eight">'
      '<dt>Presentation &amp; who gets it</dt><dd>%s</dd>'
      '<dt>Pain / where it sits / key finding</dt><dd>%s &middot; %s &middot; %s</dd>'
      '<dt>Testing &amp; cause</dt><dd>%s</dd>'
      '<dt>First-line treatment</dt><dd>%s</dd>'
      '<dt>Education &amp; prognosis</dt><dd>%s</dd>'
      '</dl><p class="src">Slides %s</p></div>'
      % (n, ucls, urg, _fig(name), give, pres, pain, where, sign, test, tx, edu, slides))


def build():
    secs = []
    for anchor, title, names in ORDER:
        secs.append('<h3 class="sub" id="%s">%s</h3>%s'
                    % (anchor, title, "".join(_condition(n) for n in names)))
    covered = {n for _a, _t, ns in ORDER for n in ns}
    missing = [r[0] for r in ROWS_L18 if r[0] not in covered]
    assert not missing, "condition in the chart but not in the guide: %r" % missing

    return """
<section class="deck" id="neck-masses">
  <h2 class="deck-title">4 &middot; Neoplasms and Neck Masses</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">DISORDERS OF THE EARS, NOSE, THROAT AND NECK &mdash; Neck Masses and Neoplasms</p>
    <ol type="a">
      <li>Define the major and minor triangles of the neck</li>
      <li>Identify the lymph nodes of the neck area</li>
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis of the following
      neck masses and neoplasms:
        <ol>
          <li>Common neck masses.</li><li>Vascular tumors seen in the neck.</li>
          <li>Benign neoplasms of the neck</li><li>Malignant neoplasms</li>
          <li>Primary</li><li>Secondary</li>
        </ol>
      </li>
      <li>Identify medical care strategies for disorders of the neoplasms and neck masses in the
      lecture topic list for the following populations: 1. adolescent &middot; 2. adult &middot;
      3. elderly</li>
    </ol>
  </div>

  <div class="callout">
    <p><strong>This lecture has no recording.</strong> Everything below comes from the slides. Where
    sections 1 to 3 also carry a point their lecturer made out loud, this one carries only what is
    written.</p>
  </div>

  <h3 class="sub" id="l18-anatomy">4.1 &middot; The triangles and the nodes</h3>
  <p>The first two objectives are pure anatomy, and no disease row carries them, so they go
  first.</p>

  <p><strong>The neck is bounded by the mandible above and the clavicle below</strong>, and the
  <strong>sternocleidomastoid divides it into an anterior and a posterior triangle</strong>. Each is
  then subdivided by the <strong>omohyoid and digastric</strong> muscles.</p>

  <table class="tbl">
    <tr><th>Triangle</th><th>Boundaries</th><th>What is in it</th></tr>
    <tr><td colspan="3" class="txnote"><b>POSTERIOR</b> &mdash; sternocleidomastoid in front,
      trapezius behind, clavicle below; divided by the <b>omohyoid</b></td></tr>
    <tr><td><b>Occipital</b></td>
      <td>Upper part of the posterior triangle</td>
      <td>Floor from above down: semispinalis capitis, splenius capitis, levator scapulae, scalenus
      medius. The <b>spinal accessory nerve</b> crosses the floor to pass deep to trapezius; the
      cutaneous nerves of the neck run in the deep fascia over it.</td></tr>
    <tr><td><b>Supraclavicular</b></td>
      <td>Above the middle of the clavicle</td>
      <td>Terminal subclavian artery; roots, trunks and divisions of the <b>brachial plexus</b>;
      thyrocervical trunk branches; tributaries of the external jugular vein. <b>The cupola of the
      pleural cavity lies deep to its contents.</b></td></tr>
    <tr><td colspan="3" class="txnote"><b>ANTERIOR</b> &mdash; sternocleidomastoid behind, midline
      in front, mandible above</td></tr>
    <tr><td><b>Submental</b></td>
      <td>Anterior belly of digastric, midline, hyoid bone</td>
      <td>Floor formed by <b>mylohyoid</b>.</td></tr>
    <tr><td><b>Digastric</b> (submandibular)</td>
      <td>Mandible above, the two bellies of digastric</td>
      <td>Stylohyoid, mylohyoid and hyoglossus muscles; <b>submandibular gland</b>; hypoglossal
      nerve; facial vessels.</td></tr>
    <tr><td><b>Carotid</b></td>
      <td>Sternocleidomastoid behind, posterior belly of digastric above, omohyoid below</td>
      <td><b>Carotid arteries, internal jugular vein, vagus nerve.</b></td></tr>
    <tr><td><b>Muscular</b></td>
      <td>Omohyoid above, sternocleidomastoid below, midline in front</td>
      <td>Thyroid, parathyroid, larynx, trachea, oesophagus, thyroid and cricoid cartilage.</td></tr>
  </table>

  <p><strong>Lymphatic drainage.</strong> Superficial nodes are named for where they sit.
  <b>Occipital, retroauricular and parotid</b> nodes drain the scalp, auricle and middle ear;
  <b>submandibular</b> nodes drain the face, sinuses, mouth and tongue; <b>retropharyngeal</b> nodes
  &mdash; not truly superficial &mdash; take lymph from the deeper structures of the head including
  the upper pharynx. All of them drain into the <b>deep cervical nodes</b>, and two of those are
  worth naming: <b>jugulodigastric</b> nodes drain the <b>palatine tonsil</b>, and
  <b>juguloomohyoid</b> nodes drain the <b>tongue</b>. The deep cervical chain empties into the
  <b>thoracic duct</b> on the left (at the junction of the left internal jugular and left subclavian
  veins) or the <b>right lymphatic duct</b> on the right.</p>

  <h3 class="sub" id="l18-approach">4.2 &middot; When to think malignancy</h3>
  <p><strong>Most neck masses under 40 are inflammatory</strong> &mdash; with the exception of
  Hodgkin lymphoma. The lecture then gives a list of features that should move you the other way.</p>

  <div class="callout warn">
    <p><strong>Think malignancy when:</strong> there is no infectious origin &middot; duration
    <b>over 2 weeks</b> &middot; size <b>over 1.5&nbsp;cm</b> &middot; <b>firm, non-cystic,
    non-tender, with little or no mobility</b> &middot; age <b>over 40</b> &middot; tobacco and
    alcohol use &middot; ulceration. Also family history, previous malignancy, immunocompromise and
    HIV.</p>
    <p><strong>And four rules of thumb from the same slide:</strong> a mass present for
    <b>years</b> is usually benign (lipoma or cyst); one growing <b>rapidly</b> is usually
    infectious if there are other symptoms and <b>lymphoma if there are not</b>; <b>fluctuance</b>
    means cystic; <b>pulsatile or a bruit means vascular</b>.</p>
  </div>

  <p><strong>The differential, as KITTENS.</strong>
  <b>K</b> congenital &mdash; branchial cleft cyst, lymphatic malformation, teratoma, dermoid cyst,
  thyroglossal duct cyst, external laryngocele.
  <b>I</b> infectious and iatrogenic &mdash; bacterial or viral lymphadenitis, tuberculosis,
  cat-scratch fever, syphilis, atypical mycobacteria, persistent generalised lymphadenopathy,
  mononucleosis, sebaceous cyst, deep inflammation or abscess.
  <b>T</b> toxins and trauma &mdash; haematoma.
  <b>E</b> endocrine &mdash; thymic cyst, thyroid hyperplasia, aberrant thyroid tissue, parathyroid
  cyst.
  <b>N</b> neoplastic &mdash; metastatic or regional malignancy, thyroid neoplasm, lymphoma,
  haemangioma, salivary gland tumour, vascular tumour, neurogenic tumour, lipoma.
  <b>S</b> systemic &mdash; granulomatous disease, laryngocele, plunging ranula, Kawasaki
  disease.</p>

  <p><strong>The other framework, from slide 17</strong>, splits on age first. <b>Congenital</b>
  divides by position &mdash; <b>lateral</b> gives branchial cleft cyst, lymphadenopathy and cystic
  hygroma; <b>midline</b> gives thyroglossal duct cyst. <b>Adult</b> divides into
  <b>inflammatory</b> (viral adenopathy; bacterial &mdash; strep, staph, Ludwig angina,
  actinomyces, sialadenitis, tubercular scrofula) and <b>neoplastic</b> (metastatic to cervical
  nodes from a head and neck primary or melanoma; or primary &mdash; thyroid, lymphoma).</p>

  <p><strong>What to order.</strong> A trial of antibiotics is common, but a mass that persists gets
  worked up. <b>Contrast computed tomography</b> distinguishes vascularity and solid from cystic,
  and evaluates for metastasis and staging &mdash; but <b>avoid iodine contrast if thyroid cancer is
  suspected</b>, because it compromises later radioiodine treatment. <b>Fine needle aspiration
  biopsy is the standard of care</b>: it separates neoplasm from inflammation and carcinoma from
  lymphoma, and needs a <b>minimum of four separate passes</b>. Then, as indicated: computed
  tomography angiography for pulsatile masses, magnetic resonance imaging, positron emission
  tomography, excisional biopsy, and labs &mdash; full blood count with differential, comprehensive
  metabolic panel, HIV, Epstein-Barr virus and cytomegalovirus, erythrocyte sedimentation rate and
  C-reactive protein, autoimmune panel, thyroid and parathyroid panels, tuberculin skin test, cat
  scratch and toxoplasmosis titres. <b>Refer early if the mass is suspicious, and especially if it
  persists after treatment.</b></p>

  __SECS__
</section>
""".replace("__SECS__", "".join(secs))


SECTION = build()
