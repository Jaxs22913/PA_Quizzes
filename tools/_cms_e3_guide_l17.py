# -*- coding: utf-8 -*-
"""Section 3 of the CMS I Exam 3 guide -- Nose and Paranasal Sinuses (L17).

Prof. Hugh Griffenkranz, 3 September 2026. Generated from
_cms_e3_chart_l17.py, like sections 1 and 2.

TWO THINGS ARE WRITTEN BY HAND HERE. The bacterial-versus-viral decision opens
the section, because it is what the first thirty slides are actually about and
because it is the commonest real decision in the block. And slide 63 is an
IMAGE of a list -- the conditions associated with multiple benign polyps, with
percentages -- so it is transcribed rather than left to extract as a bare
title.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cms_e3_chart_l17 import ROWS_L17, DIFF_L17, IMGS_L17

IMGDIR = "cms-ent-chart-images"
OUTDIR = "Clinical Medicine and Surgery I Exam 3"

ORDER = [
 ("l17-sinus", "3.1 &middot; Sinusitis, acute through chronic",
  ["Acute sinusitis (rhinosinusitis)", "Bacterial sinusitis &mdash; the features that suggest it",
   "Sinusitis with urgent features", "Chronic bacterial sinusitis", "Chronic fungal sinusitis"]),
 ("l17-septum", "3.2 &middot; The septum",
  ["Deviated septum", "Perforated septum", "Septal haematoma"]),
 ("l17-bleed", "3.3 &middot; Epistaxis",
  ["Epistaxis &mdash; anterior", "Epistaxis &mdash; posterior"]),
 ("l17-trauma", "3.4 &middot; Trauma and foreign bodies",
  ["Nasal fracture", "Nasal foreign body"]),
 ("l17-polyp", "3.5 &middot; Polyps and rhinitis",
  ["Nasal polyps", "Allergic rhinitis"]),
 ("l17-neo", "3.6 &middot; Neoplasms",
  ["Nasopharyngeal carcinoma", "Benign nasal neoplasms"]),
]

ROW = {r[0]: r for r in ROWS_L17}


def _fig(name):
    pic = IMGS_L17.get(name)
    if not pic:
        return ""
    fn, sl = pic
    if not os.path.exists(os.path.join(OUTDIR, IMGDIR, fn)):
        return ""
    return ('<figure class="fig"><img src="%s/%s" loading="lazy" alt="%s, from the lecture '
            'slides."><figcaption>%s <span class="cite">L17 slide %d</span></figcaption></figure>'
            % (IMGDIR, fn, name.replace("&mdash;", "-"), name, sl))


def _condition(name):
    n, grp, give, pres, test, tx, urg, edu, slides, _deck = ROW[name]
    pain, disch, sign = DIFF_L17[name]
    ucls = ("emerg" if "EMERGENT" in urg.upper() else
            "urg" if "URGENT" in urg.upper() else "rout")
    return (
      '<div class="cond"><h4>%s <span class="u %s">%s</span></h4>%s'
      '<p class="give"><b>Gives itself away by:</b> %s</p>'
      '<dl class="eight">'
      '<dt>Presentation &amp; who gets it</dt><dd>%s</dd>'
      '<dt>Pain / discharge / key finding</dt><dd>%s &middot; %s &middot; %s</dd>'
      '<dt>Testing &amp; cause</dt><dd>%s</dd>'
      '<dt>First-line treatment</dt><dd>%s</dd>'
      '<dt>Education &amp; prognosis</dt><dd>%s</dd>'
      '</dl><p class="src">Slides %s</p></div>'
      % (n, ucls, urg, _fig(name), give, pres, pain, disch, sign, test, tx, edu, slides))


def build():
    secs = []
    for anchor, title, names in ORDER:
        secs.append('<h3 class="sub" id="%s">%s</h3>%s'
                    % (anchor, title, "".join(_condition(n) for n in names)))
    covered = {n for _a, _t, ns in ORDER for n in ns}
    missing = [r[0] for r in ROWS_L17 if r[0] not in covered]
    assert not missing, "condition in the chart but not in the guide: %r" % missing

    return """
<section class="deck" id="nose-sinuses">
  <h2 class="deck-title">3 &middot; Disorders of the Nose and Paranasal Sinuses</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">DISORDERS OF THE EARS, NOSE, THROAT AND NECK &mdash; Nose and Paranasal Sinuses</p>
    <ol type="a">
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis of the following
      disorders of the nose and paranasal sinuses:
        <ol type="a">
          <li>Acute and chronic sinusitis</li><li>Nasal trauma</li><li>Deviated septum</li>
          <li>Perforated septum</li><li>Septal hematoma</li><li>Nasal fracture</li>
          <li>Epistaxis</li><li>Nasal foreign body</li><li>Nasal polyp</li>
          <li>Rhinitis: i. Allergic &middot; ii. Vasomotor</li>
          <li>Neoplasms: i. Benign &middot; ii. Malignant</li>
        </ol>
      </li>
      <li>Identify medical care strategies for disorders of the nose and paranasal sinuses in the
      lecture topic list for the following populations: 1. adolescent &middot; 2. adult &middot;
      3. elderly</li>
    </ol>
  </div>

  <div class="callout warn">
    <p><strong>The whole first half of this lecture is one decision: is it viral or
    bacterial?</strong> <strong>90&ndash;98% of acute rhinosinusitis is viral</strong>, and only
    <strong>0.5&ndash;2%</strong> of those develop a bacterial superinfection &mdash; yet it is the
    <strong>fifth leading reason antibiotics get prescribed</strong>. The features that shift you
    toward bacterial are:</p>
    <ul>
      <li><strong>Double worsening</strong> &mdash; getting worse again more than 5&ndash;6 days
      after initially improving</li>
      <li><strong>Persistent symptoms for 10 days or more</strong></li>
      <li><strong>Persistent purulent discharge</strong></li>
      <li><strong>UNILATERAL</strong> upper tooth or facial pain, or unilateral maxillary
      tenderness</li>
      <li><strong>Fever</strong>, or altered mental status</li>
    </ul>
    <p><strong>Pain is the big distinguishing factor</strong> &mdash; it occurs only in bacterial
    and fungal sinusitis, and it is <strong>reproducible on palpation</strong>, which a common cold
    is not.</p>
    <p><strong>And no test settles it.</strong> Nothing distinguishes viral from bacterial, routine
    sinus radiography is discouraged, and three or more clinical findings have similar accuracy to
    imaging anyway. CT is for recurrent disease, treatment failure, or suspected extrasinus
    involvement.</p>
  </div>

  <div class="callout warn">
    <p><strong>His second emphasis marker: the yellow highlight.</strong> Talking through the
    epidemiology he said &mdash; <em>&ldquo;maybe it&rsquo;s highlighted in yellow and I&rsquo;m
    trying to make a specific point about this, maybe like in the last lecture when something was
    highlighted in yellow and I said it was important to remember&rdquo;</em> &mdash; and then
    walked the class to the answer he wanted: the commonest pathogen in otitis media is
    <strong>viral</strong>, and so is the commonest pathogen in sinusitis. <strong>When a slide of
    his has something highlighted in yellow, that is deliberate.</strong> It sits alongside his
    other marker, saying a thing three times.</p>
    <p>He called acute sinusitis <em>&ldquo;one of your bread-and-butter diagnoses &hellip;
    something you&rsquo;re going to see all the time, especially in primary care&rdquo;</em>, and
    was blunt about the reflex to treat: <em>&ldquo;everybody says oh no it&rsquo;s bacterial and
    everybody&rsquo;s going to go home with a course of antibiotics &mdash; is that the right thing
    to do? No, of course not. We have to be good stewards of our antibiotics.&rdquo;</em></p>
  </div>

  <div class="callout">
    <p><strong>Discharge colour is the thing patients trust most and the thing that helps
    least.</strong> Yellow or green is explicitly the <em>least</em> useful. Clear may be viral or
    allergic. Yellow <em>and</em> putrid suggests bacterial. <strong>Black suggests
    fungus.</strong> Rust-coloured may be <em>S. pneumoniae</em>.</p>
    <p><strong>Allergy does not cause an &ldquo;-itis&rdquo;.</strong> It creates the perfect
    environment for infection. Many patients who believe they have sinusitis have allergic
    disease.</p>
    <p><strong>One objective has no slide.</strong> The syllabus lists rhinitis as
    <em>allergic</em> and <em>vasomotor</em>; the deck covers allergic rhinitis in full and
    <strong>never mentions vasomotor rhinitis</strong>. It is flagged here rather than quietly
    omitted &mdash; it is a named objective with no lecture content behind it.</p>
  </div>
@@SECTIONS@@
</section>""".replace("@@SECTIONS@@", "".join(secs))


SECTION = build()
