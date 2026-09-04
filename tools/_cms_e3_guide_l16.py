# -*- coding: utf-8 -*-
"""Section 2 of the CMS I Exam 3 guide -- Inner Ear, Balance and Hearing Loss (L16).

Prof. Jaquith, 3 September 2026. Generated from _cms_e3_chart_l16.py for the
same reason section 1 is: the chart already holds all eight guide points, so
rendering them keeps one copy of every fact.

THIS SECTION OPENS WITH WEBER AND RINNE RATHER THAN A DISEASE, because the
syllabus makes them objectives in their own right (b, c) and because Jaquith
stopped mid-lecture to say a test question is written on exactly that. The
worked vignette she gave is reproduced in full.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cms_e3_chart_l16 import ROWS_L16, DIFF_L16, IMGS_L16

IMGDIR = "cms-ent-chart-images"
OUTDIR = "Clinical Medicine and Surgery I Exam 3"

ORDER = [
 ("l16-patterns", "2.2 &middot; The two patterns, and presbycusis",
  ["Conductive hearing loss", "Sensorineural hearing loss", "Presbycusis"]),
 ("l16-masses", "2.3 &middot; Tinnitus, and the masses you can see",
  ["Tinnitus", "Exostosis", "Glomus tumour"]),
 ("l16-acquired", "2.4 &middot; Acquired sensorineural loss",
  ["Ototoxicity", "Noise-induced hearing loss", "Acoustic trauma", "Perilymphatic fistula",
   "Autoimmune sensorineural loss", "Syphilitic sensorineural loss",
   "AIDS-related sensorineural loss", "Hereditary sensorineural loss",
   "Sudden sensorineural hearing loss"]),
 ("l16-vertigo", "2.5 &middot; The inner ear syndromes &mdash; sorted by how long the vertigo lasts",
  ["Benign paroxysmal positional vertigo", "M&eacute;ni&egrave;re's disease", "Labyrinthitis",
   "Vestibular neuronitis"]),
 ("l16-central", "2.6 &middot; Retrocochlear, central, and not-organic",
  ["Acoustic neuroma", "Vertebrobasilar insufficiency or occlusion",
   "Isolated cerebellar infarction", "Functional hearing loss"]),
]

ROW = {r[0]: r for r in ROWS_L16}


def _fig(name):
    pic = IMGS_L16.get(name)
    if not pic:
        return ""
    fn, sl = pic
    if not os.path.exists(os.path.join(OUTDIR, IMGDIR, fn)):
        return ""
    return ('<figure class="fig"><img src="%s/%s" loading="lazy" alt="%s, from the lecture '
            'slides."><figcaption>%s <span class="cite">L16 slide %d</span></figcaption></figure>'
            % (IMGDIR, fn, name.replace("&mdash;", "-"), name, sl))


def _condition(name):
    n, grp, give, pres, test, tx, urg, edu, slides, _deck = ROW[name]
    pain, hearing, sign = DIFF_L16[name]
    ucls = ("emerg" if "EMERGENT" in urg.upper() else
            "urg" if "URGENT" in urg.upper() else "rout")
    return (
      '<div class="cond"><h4>%s <span class="u %s">%s</span></h4>%s'
      '<p class="give"><b>Gives itself away by:</b> %s</p>'
      '<dl class="eight">'
      '<dt>Presentation &amp; who gets it</dt><dd>%s</dd>'
      '<dt>Pain / hearing loss / key finding</dt><dd>%s &middot; %s &middot; %s</dd>'
      '<dt>Testing &amp; cause</dt><dd>%s</dd>'
      '<dt>First-line treatment</dt><dd>%s</dd>'
      '<dt>Education &amp; prognosis</dt><dd>%s</dd>'
      '</dl><p class="src">Slides %s</p></div>'
      % (n, ucls, urg, _fig(name), give, pres, pain, hearing, sign, test, tx, edu, slides))


def build():
    secs = []
    for anchor, title, names in ORDER:
        secs.append('<h3 class="sub" id="%s">%s</h3>%s'
                    % (anchor, title, "".join(_condition(n) for n in names)))
    covered = {n for _a, _t, ns in ORDER for n in ns}
    missing = [r[0] for r in ROWS_L16 if r[0] not in covered]
    assert not missing, "condition in the chart but not in the guide: %r" % missing

    tests = """
  <h3 class="sub" id="l16-tests">2.1 &middot; Weber, Rinne, and reading the two tracings</h3>
  <div class="callout warn">
    <p><strong>She stopped the lecture to say a question like this is on the paper.</strong>
    Her words: <em>&ldquo;this is what I expect you to get right on the test, because there is a
    test question like this.&rdquo;</em> The vignette she worked through:</p>
    <blockquote>A 39-year-old man is evaluated for right ear fullness and decreased hearing that
    developed after an upper respiratory tract infection. He denies tinnitus, vertigo, fever and
    ear drainage. On examination an <strong>amber effusion</strong> is visible behind an
    <strong>intact</strong> right tympanic membrane, which has <strong>decreased mobility</strong>.
    The left ear is normal. <em>Which Weber and Rinne findings are most likely?</em></blockquote>
    <p>A right middle ear effusion is a <strong>conductive</strong> loss, so <strong>Weber
    lateralises to the right</strong> and <strong>Rinne becomes abnormal on the right, with bone
    conduction at least equal to air</strong>.</p>
    <p><strong>She also described the question the other way round</strong>, and it is worth
    writing down: <em>&ldquo;I can give you these Weber and Rinne results and you&rsquo;ll
    automatically know if it&rsquo;s conductive or sensorineural &hellip; I have things like wax
    impaction on there, and that would be the answer, because the other choices wouldn&rsquo;t be
    conductive.&rdquo;</em> <strong>The distractors die on loss type before you think about
    anything else.</strong></p>
  </div>

  <div class="tbl-wrap"><table class="wr">
    <thead><tr><th></th><th>Weber</th><th>Rinne</th><th>Voice</th><th>In noise</th></tr></thead>
    <tbody>
      <tr><td><b>Normal</b></td><td>No lateralisation</td><td>AC &gt; BC</td>
          <td>Normal</td><td>Normal</td></tr>
      <tr><td><b>Conductive</b></td><td><b>TO the bad ear</b></td><td><b>BC &ge; AC</b></td>
          <td><b>Soft</b></td><td><b>Better</b></td></tr>
      <tr><td><b>Sensorineural</b></td><td><b>AWAY, to the good ear</b></td>
          <td>AC &gt; BC <i>(same as normal)</i></td><td><b>Loud</b></td><td><b>Worse</b></td></tr>
    </tbody>
  </table></div>
  <div class="callout">
    <p><strong>Why Weber carries the diagnosis.</strong> A sensorineural loss leaves the Rinne
    relationship looking exactly like a normal ear &mdash; air still beats bone. Only Weber
    separates them.</p>
    <p><strong>Audiometry severity, and she flagged this chart to know outright.</strong> It runs
    <strong>in twenties</strong>: normal 0&ndash;20 dB, mild 20&ndash;40, moderate 40&ndash;60,
    severe 60&ndash;80, <strong>profound above 80</strong>. Her own words for it: <em>&ldquo;it's
    all by 20s.&rdquo;</em> <strong>The prevalence percentages on the neighbouring slide are
    explicitly NOT to be memorised</strong> &mdash; <em>&ldquo;you don&rsquo;t have to memorize
    these statistics&rdquo;</em>.</p>
    <p><strong>Tympanometry, by shape.</strong> <b>A</b> normal &middot; <b>B</b> flat, meaning
    fluid or a perforation &middot; <b>C</b> peak shifted negative, meaning eustachian tube
    dysfunction &middot; <b>As</b> shallow and stiff, meaning ossicular fixation or
    tympanosclerosis &middot; <b>Ad</b> deep and over-compliant, meaning ossicular discontinuity or
    a monomeric drum.</p>
    <p><strong>Vestibular testing.</strong> <b>Electronystagmography</b> is the gold standard for
    a disorder affecting one ear at a time; <b>magnetic resonance imaging with gadolinium</b> is
    the gold standard when retrocochlear disease is suspected; the <b>Dix-Hallpike manoeuvre</b>
    diagnoses positional vertigo and the <b>Epley manoeuvre</b> treats it.</p>
  </div>"""

    return """
<section class="deck" id="inner-ear">
  <h2 class="deck-title">2 &middot; Disorders of the Inner Ear, Balance and Hearing Loss</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">DISORDERS OF THE EARS, NOSE, THROAT AND NECK &mdash; Inner Ear, Balance and Hearing Loss</p>
    <ol type="a">
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis of the following
      disorders of the inner ear, balance, and hearing loss:
        <ol>
          <li>Acoustic neuroma</li><li>Hearing impairment</li><li>Sensorineural</li>
          <li>Conductive</li><li>Tinnitus</li><li>Ototoxicity</li><li>Mastoiditis</li>
          <li>Vertebro-basilar arterial occlusion</li><li>Labyrinthitis</li>
          <li>Benign paroxysmal positional vertigo</li><li>Meniere&rsquo;s disease</li>
        </ol>
      </li>
      <li>Explain the difference between Weber and Rinne testing.</li>
      <li>Apply Weber and Rinne findings to sensorineural and conductive hearing loss.</li>
      <li>Explain how to interpret an audiogram and tympanogram.</li>
      <li>Describe vestibular testing and indications for ordering vestibular testing.</li>
      <li>Interpret results of vestibular testing.</li>
      <li>Identify medical care strategies for disorders of the inner ear, balance, and hearing
      loss in the lecture topic list for the following populations: 1. infant &middot; 2. child
      &middot; 3. adolescent &middot; 4. adult</li>
    </ol>
  </div>

  <div class="callout">
    <p><strong>Four of the seven objectives are about the TESTS, not a disease.</strong>
    Objectives b through f ask you to explain Weber against Rinne, apply their findings, read an
    audiogram and a tympanogram, and describe and interpret vestibular testing. That is why this
    section opens with them rather than with a condition.</p>
    <p><strong>Sort the vertigo by duration first.</strong> <b>Seconds</b> &rarr; benign positional
    vertigo. <b>Minutes to hours</b> &rarr; M&eacute;ni&egrave;re&rsquo;s. <b>Days to weeks</b>
    &rarr; labyrinthitis or vestibular neuronitis, and the one word separating those two is
    whether <b>hearing</b> is affected. She called the types-of-vertigo table one to
    <em>&ldquo;definitely know&rdquo;</em>.</p>
  </div>
%s
%s
</section>""" % (tests, "".join(secs))


SECTION = build()
