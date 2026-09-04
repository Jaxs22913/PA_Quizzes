# -*- coding: utf-8 -*-
"""Section 1 of the CMS I Exam 3 guide -- External and Middle Ear (Lecture 15).

Prof. Hugh Griffenkranz, 3 September 2026.

GENERATED FROM THE CHART DATA, not written twice. The eight guide points the
CMS spec asks for -- definition, who gets it, risk factors, classic signs,
examination findings, diagnostics, first-line treatment, complications -- are
exactly the fields _cms_e3_chart_l15.py already carries, so the rows are the
source and the guide renders them. A fact cannot drift between the chart and
the guide because there is only one copy of it.

What is written by hand here is what a table cannot carry: the ordering, the
comparisons the block turns on, and the two corrections Griffenkranz made out
loud that are on no slide.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cms_e3_chart_l15 import ROWS_L15, DIFF_L15, IMGS_L15

IMGDIR = "cms-ent-chart-images"
OUTDIR = "Clinical Medicine and Surgery I Exam 3"

# The order the guide walks them in -- by where the problem is, outside in,
# which is how the examination itself proceeds.
ORDER = [
 ("l15-canal", "1.1 &middot; The external canal",
  ["Cerumen impaction", "Otitis externa", "Malignant otitis externa", "Otomycosis",
   "Foreign body of the canal"]),
 ("l15-auricle", "1.2 &middot; The auricle",
  ["Hematoma of the external ear", "Lacerations and avulsion", "Foreign body of the auricle",
   "Keloid of the ear"]),
 ("l15-tube", "1.3 &middot; The eustachian tube and pressure",
  ["Eustachian tube dysfunction", "Barotrauma"]),
 ("l15-om", "1.4 &middot; The otitis media family",
  ["Acute otitis media", "Otitis media with effusion", "Chronic otitis media", "Mastoiditis"]),
 ("l15-drum", "1.5 &middot; The tympanic membrane and behind it",
  ["Tympanic membrane perforation", "Cholesteatoma"]),
 ("l15-fixed", "1.6 &middot; Conductive fixation and neoplasms",
  ["Otosclerosis", "Carcinoma of the ear canal"]),
]

ROW = {r[0]: r for r in ROWS_L15}


def _fig(name):
    pic = IMGS_L15.get(name)
    if not pic:
        return ""
    fn, sl = pic
    if not os.path.exists(os.path.join(OUTDIR, IMGDIR, fn)):
        return ""
    return ('<figure class="fig"><img src="%s/%s" loading="lazy" alt="%s, from the lecture '
            'slides."><figcaption>%s <span class="cite">Slide %d</span></figcaption></figure>'
            % (IMGDIR, fn, name.replace("&mdash;", "-"), name, sl))


def _condition(name):
    n, grp, give, pres, test, tx, urg, edu, slides, _deck = ROW[name]
    pain, hearing, sign = DIFF_L15[name]
    ucls = ("emerg" if "EMERGENT" in urg.upper() else
            "urg" if "URGENT" in urg.upper() else "rout")
    return (
      '<div class="cond">'
      '<h4>%s <span class="u %s">%s</span></h4>'
      '%s'
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
        body = "".join(_condition(n) for n in names)
        secs.append('<h3 class="sub" id="%s">%s</h3>%s' % (anchor, title, body))
    covered = {n for _a, _t, ns in ORDER for n in ns}
    missing = [r[0] for r in ROWS_L15 if r[0] not in covered]
    assert not missing, "condition in the chart but not in the guide: %r" % missing

    return """
<section class="deck" id="external-middle-ear">
  <h2 class="deck-title">1 &middot; Disorders of the External and Middle Ear</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">DISORDERS OF THE EARS, NOSE, THROAT AND NECK &mdash; External and Middle Ear Disorders</p>
    <ol type="a">
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis of the following
      external and middle ear conditions:
        <ol>
          <li>Acute otitis media</li><li>Barotrauma</li><li>Cerumen impaction</li>
          <li>Cholesteatoma</li><li>Chronic otitis media</li>
          <li>Eustachian tube dysfunction</li><li>Ear trauma</li>
          <li>Blunt and penetrating trauma</li><li>Tympanic membrane perforation</li>
          <li>Hematoma of external ear</li><li>Foreign body in the ear</li>
          <li>Otitis externa</li><li>Otosclerosis</li>
          <li>Neoplasms: a. Benign &middot; b. Malignant</li>
        </ol>
      </li>
      <li>Identify medical care strategies for external and middle ear disorders in the lecture
      topic list for the following populations: 1. adolescent &middot; 2. adult &middot;
      3. elderly</li>
    </ol>
  </div>

  <div class="callout warn">
    <p><strong>Two things he said out loud that are on no slide.</strong> The otitis media slide
    lists three bacteria and nothing else, which reads as though the disease were bacterial. It is
    not: <em>&ldquo;far and away the most common cause for otitis media is a viral
    infection&rdquo;</em>. And the three-organism sequence is no longer in order of prevalence
    &mdash; <strong>Moraxella catarrhalis has overtaken Haemophilus influenzae because of
    vaccination</strong>, which is why immunisation status is worth asking. An unimmunised child
    puts <em>H. influenzae</em> back on the list.</p>
    <p><strong>His emphasis marker is repetition.</strong> He said <em>&ldquo;it's important, it's
    important, it's important to remember the three most common bacterial causes&rdquo;</em>
    &mdash; <em>S. pneumoniae</em>, <em>H. influenzae</em>, <em>M. catarrhalis</em> &mdash; and
    pointed out he had highlighted them on the slide himself. He signposted the exam <em>nowhere
    else in the entire lecture</em>, so his silence elsewhere means nothing.</p>
  </div>

  <div class="callout">
    <p><strong>Mastoiditis is filed here, though the syllabus lists it under Lecture 16.</strong>
    The only teaching on it in either deck is one line of this lecture&rsquo;s slide 19, as a
    complication of acute otitis media. It sits where the content is.</p>
    <p><strong>The three columns to read down.</strong> Ear disease sorts on <strong>pain</strong>,
    <strong>the type of hearing loss</strong> and <strong>what the drum looks like</strong>. Those
    three are printed under every condition below and are the axes of
    <a href="cms-ent-comparison-chart.html">the comparison chart</a>.</p>
  </div>
%s
</section>""" % "".join(secs)


SECTION = build()
