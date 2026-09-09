# -*- coding: utf-8 -*-
"""Section 5 of the CMS I Exam 3 guide -- Oral Cavity, Salivary Glands and Neck (L19).

Prof. Chand Shah. Generated from _cms_e3_chart_l19.py, like sections 1-4.

BUILT WITHOUT AUDIO, like section 4.

THE LARGEST LECTURE IN THE BLOCK -- 151 slides, and the syllabus lists 35
conditions under it. Four things are written by hand because no condition row
carries them: the oral examination itself, the salivary anatomy, the Centor
mapping (the criteria are in slide 76's text but the score-to-action mapping is
only in the picture on slide 75), and the two comparison images that extract as
bare titles -- streptococcal against viral pharyngitis, and the thumbprint sign.
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _cms_e3_chart_l19 import ROWS_L19, DIFF_L19, IMGS_L19

IMGDIR = "cms-ent-chart-images"
OUTDIR = "Clinical Medicine and Surgery I Exam 3"

ORDER = [
 ("l19-var", "5.2 &middot; Normal variants of the oral mucosa",
  ["Leukoedema", "Fordyce granules", "Physiologic pigmentation"]),
 ("l19-ulcer", "5.3 &middot; Stomatitis and oral ulcers",
  ["Aphthous stomatitis (canker sores)", "Herpes simplex ulcers", "Behcet syndrome",
   "Oral lichen planus", "Systemic lupus erythematosus &mdash; oral"]),
 ("l19-sal", "5.4 &middot; Salivary glands",
  ["Acute suppurative sialadenitis", "Sialolithiasis", "Parotitis"]),
 ("l19-vc", "5.5 &middot; Vocal cords and larynx",
  ["Vocal cord nodules", "Vocal cord polyps", "Vocal cord papillomatosis", "Vocal cord paralysis",
   "Acute laryngitis", "Chronic laryngitis"]),
 ("l19-air", "5.6 &middot; The airway emergency",
  ["Epiglottitis (supraglottitis)"]),
 ("l19-pha", "5.7 &middot; Pharyngitis and its sequelae",
  ["Viral pharyngitis", "Bacterial pharyngitis (GABHS)", "Rheumatic fever", "Chronic pharyngitis",
   "Infectious mononucleosis", "Diphtheria"]),
 ("l19-deep", "5.8 &middot; Deep neck infections",
  ["Cervical adenitis", "Peritonsillar abscess (quinsy)", "Retropharyngeal abscess",
   "Ludwig angina"]),
 ("l19-dent", "5.9 &middot; Dentition and the jaw",
  ["Dental abscess", "Dental caries, pulpitis and periapical abscess",
   "Gingivitis and periodontitis", "Impacted teeth", "Malocclusion",
   "Temporomandibular joint disorders"]),
 ("l19-les", "5.10 &middot; Lesions of the oral cavity",
  ["Oral candidiasis (thrush)", "Oral leukoplakia", "Erythroplakia", "Hairy leukoplakia"]),
 ("l19-neo", "5.11 &middot; Neoplasms",
  ["Salivary gland neoplasm", "Oral cavity and oropharyngeal cancer"]),
]

ROW = {r[0]: r for r in ROWS_L19}


def _fig(name):
    pic = IMGS_L19.get(name)
    if not pic:
        return ""
    fn, sl = pic
    if not os.path.exists(os.path.join(OUTDIR, IMGDIR, fn)):
        return ""
    return ('<figure class="fig"><img src="%s/%s" loading="lazy" alt="%s, from the lecture '
            'slides."><figcaption>%s <span class="cite">L19 slide %d</span></figcaption></figure>'
            % (IMGDIR, fn, name.replace("&mdash;", "-"), name, sl))


def _condition(name):
    n, grp, give, pres, test, tx, urg, edu, slides, _deck = ROW[name]
    pain, where, sign = DIFF_L19[name]
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
    missing = [r[0] for r in ROWS_L19 if r[0] not in covered]
    assert not missing, "condition in the chart but not in the guide: %r" % missing

    return """
<section class="deck" id="oral-cavity">
  <h2 class="deck-title">5 &middot; Disorders of the Oral Cavity, Salivary Glands and Neck</h2>
  <div class="io-box">
    <h3>Instructional Objectives</h3>
    <p class="tag">DISORDERS OF THE EARS, NOSE, THROAT AND NECK &mdash; Disorders of the Oral
    Cavity, Salivary Glands, and Neck</p>
    <ol type="a">
      <li>Compare and contrast the etiologies, epidemiology, risk factors, clinical
      manifestations, differential diagnosis, diagnostic testing (including ordering and
      interpretation), management (acute and chronic, including applicable rehabilitative and
      palliative care), appropriate referrals, patient education, and prognosis of the following
      disorders of the oral cavity, salivary glands, and neck:
        <ol type="a">
          <li>Stomatitis</li><li>Ulcers</li><li>Aphthous ulcerations</li>
          <li>Recurrent aphthous stomatitis (including herpetiform morphology)</li>
          <li>Herpes simplex virus ulcers</li><li>Sialadenitis</li><li>Sialolithiasis</li>
          <li>Parotitis</li><li>Laryngitis</li><li>Vocal cords</li><li>Nodules</li>
          <li>Polyps</li><li>Papillomatosis</li><li>Paralysis</li><li>Epiglottitis</li>
          <li>Pharyngitis</li>
          <li>Epstein-Barr virus (EBV) and infectious mononucleosis</li>
          <li>Rheumatic fever (as potential complication of strep pharyngitis)</li>
          <li>Oral Candidiasis</li><li>Tonsillitis</li><li>Cervical adenitis</li>
          <li>Deep neck infections</li><li>Peritonsillar abscess</li>
          <li>Retropharyngeal abscess</li><li>Ludwig angina</li><li>Diphtheria</li>
          <li>Gingivitis</li><li>Dental caries</li><li>Dental abscess</li>
          <li>Temporomandibular joint disorders</li><li>Diseases of gingiva</li>
          <li>Diseases of teeth</li><li>Lichen Planus</li><li>Oral leukoplakia</li>
          <li>Neoplasms: 1. Benign &middot; 2. Malignant</li><li>Oropharyngeal trauma</li>
        </ol>
      </li>
      <li>Identify medical care strategies for disorders of the oral cavity, salivary glands, and
      neck in the lecture topic list for the following populations: 1. adolescent &middot;
      2. adult &middot; 3. elderly</li>
    </ol>
  </div>

  <div class="callout">
    <p><strong>The biggest lecture in the block by a distance</strong> &mdash; 151 slides, and the
    objective list above runs to 35 conditions. <strong>It has no recording</strong>, so everything
    below is slide content.</p>
  </div>

  <h3 class="sub" id="l19-exam">5.1 &middot; Examining the mouth, and the salivary anatomy</h3>
  <p>The oral cavity is the <strong>outer aspects of the lips and buccal mucosa, the teeth and
  gingiva, the anterior two thirds of the tongue, the floor of the mouth, the hard palate and the
  retromolar trigone</strong>. <strong>Over 80% of surveyed clinicians believe oral examination is
  important, and far fewer actually do one</strong> &mdash; which is the lecture's argument for the
  section. Take a careful medical and medication history first: xerostomia, immunosuppression and
  chemotherapy change what you are looking at.</p>

  <table class="tbl">
    <tr><th>Gland</th><th>Duct</th><th>Where it opens</th></tr>
    <tr><td><b>Parotid</b></td><td><b>Stensen duct</b></td>
      <td>Sides of the face; the duct crosses the masseter and opens opposite the upper second
      molar. The gland most often affected by suppurative sialadenitis and by neoplasm.</td></tr>
    <tr><td><b>Submandibular</b></td><td><b>Wharton duct</b></td>
      <td>Beneath the floor of the mouth. The long, upward-running duct is why
      <b>80&ndash;90% of stones form here</b>.</td></tr>
    <tr><td><b>Sublingual</b></td><td>Sublingual ducts</td>
      <td>Floor of the mouth. The source of a <b>ranula</b>.</td></tr>
    <tr><td><b>Minor</b></td><td>&mdash;</td>
      <td>Exocrine tissue in buccal, labial and palatal mucosa. Only <b>35% of minor gland tumours
      are benign</b> &mdash; the smaller the gland, the likelier a tumour is malignant.</td></tr>
  </table>

  <div class="callout warn">
    <p><strong>The scrape test settles three diagnoses at the bedside.</strong> Wipe the lesion with
    a tongue depressor. <b>It comes off &rarr; oral candidiasis.</b> <b>It does not come off and it
    is white &rarr; leukoplakia</b> (premalignant, 5&ndash;20% become squamous cell carcinoma).
    <b>It does not come off and it is lacy &rarr; lichen planus</b> (Wickham striae). And a fourth:
    a greyish-white change that <b>disappears when you stretch the mucosa</b> is
    <b>leukoedema</b>, a normal variant.</p>
  </div>

  <div class="prof-flag">
    <span class="prof-flag-label">&#9733; MUST KNOW</span>
    <p style="margin-top:2px">Prof. Shah, [1:34:40]: <em>&ldquo;Centor criteria is something that
    everyone most definitely needs to know. Like, <b>you absolutely need to know the Centor
    criteria, no matter what</b>&hellip; So I don&rsquo;t know how you&rsquo;re going to know
    that, but you need to know that. That means you need to come up with an acronym, you need to
    come up with a song, you need to dance it out &mdash; whatever you need to do to make sure you
    know it. <b>You&rsquo;re going to be using this all the time.</b>&rdquo;</em> She then worked
    it through component by component and score by score [1:22:47&ndash;1:24:23], and framed it
    around the question students get stuck on &mdash; the rapid test is negative, now what?
    Answer: throat culture, and whether you treat &ldquo;depends on how sick they are.&rdquo;</p>
    <p><b>The antipyretic trap on the fever point</b> [1:33:00], which is not on the slide. Fever
    scores a point, but a normal temperature in clinic does not automatically score zero. If they
    took ibuprofen <b>six hours ago</b> and are still 102&nbsp;&deg;F in front of you, that counts.
    If they took it <b>two hours ago</b> and read 99.9, the number in front of you is not the
    answer &mdash; ask <b>what their maximum temperature was, how many days they have had fever,
    the highest reading in the past 24 hours, and whether the fever returns as the next dose comes
    due</b>.</p>
    <p><strong>Centor criteria, and what to do with the score</strong> (slides 74&ndash;77).
    One point each for <b>absence of cough</b>, <b>tonsillar exudate</b>, <b>fever</b>, and
    <b>tender anterior cervical lymphadenopathy</b>; plus <b>+1 for age 3&ndash;14</b>,
    <b>0 for age 15&ndash;44</b>, and <b>&minus;1 for age 45 or over</b>.</p>
    <p><b>Score 0 to 1</b> &mdash; risk of group A streptococcus roughly 1&ndash;10%; no further
    testing and no antibiotics. <b>Score 2 to 3</b> &mdash; risk roughly 11&ndash;35%; perform a
    rapid antigen test or culture and treat only if positive. <b>Score 4 or more</b> &mdash; risk
    roughly 51&ndash;53%; consider empiric treatment. <b>A negative rapid test is always confirmed
    with a throat culture</b>, and the definitive test is <b>antistreptolysin O</b>, which matters
    because carriers culture positive while asymptomatic.</p>
  </div>

  <p><strong>Streptococcal against viral pharyngitis</strong> (the comparison on slide 71). The
  streptococcal picture is <b>tonsillar and pharyngeal erythema with purulent exudate, fever above
  100.4&nbsp;&deg;F, tender cervical nodes and NO cough</b>. The viral picture brings the things
  streptococcus does not: <b>cough, rhinitis, hoarseness, conjunctivitis</b>, and sometimes
  <b>herpangina</b> &mdash; ulcerative vesicles over the tonsils. Cough is worth a Centor point in
  its absence precisely because its presence argues so strongly against strep.</p>

  <p><strong>The thumbprint sign</strong> (slide 64) is the swollen epiglottis seen on a lateral
  neck X-ray, set against the thin, curved normal epiglottis. It is worth recognising and worth
  <em>not</em> ordering: the lecture is explicit that it is <b>not necessary for diagnosis</b>, and
  that once epiglottitis is suspected, examinations that agitate the patient can complete the
  obstruction.</p>

  <div class="prof-flag">
    <span class="prof-flag-label">&#9733; SHE SAID &ldquo;BAD, BAD, BAD&rdquo;</span>
    <p style="margin-top:2px">Four times in this lecture &mdash; two diagnoses, and two single
    findings that turn an ordinary presentation into an urgent one, which is the more useful half
    of the list. She also uses it once in the <em>negative</em>, which is what shows the phrase is
    a deliberate grade rather than a verbal tic.</p>
    <p><b>Chronic laryngitis</b> [59:40]. <em>&ldquo;Chronic laryngitis is where you have vocal
    disturbances that go on for <b>more than two weeks</b>&hellip; Here, your brain should
    automatically be thinking of <b>cancer or polyps</b>, right? Something bad, right? Bad, bad,
    bad. And in these instances, you have to <b>refer to ENT as soon as possible, like ASAP, like
    yesterday</b>.&rdquo;</em> The two-week mark is the trigger and the referral is the answer
    &mdash; not a longer course of anything.</p>
    <p><b>Epiglottitis</b> [1:00:05]. She notes first that <b>supraglottitis</b> is <em>&ldquo;a
    much more correct terminology&rdquo;</em>, because the inflammation involves several
    supraglottic structures rather than one. Then: <em>&ldquo;This is an absolute emergency, okay?
    Emergency. This is bad. This is bad, bad, bad. <b>You cannot miss this diagnosis. This will
    hurt the patient. This will kill the patient if it&rsquo;s missed.</b>&rdquo;</em> Read it with
    the thumbprint paragraph above: the film is not what makes the diagnosis, and examining the
    throat can finish the airway.</p>
    <p><b>A neck mass that does not move.</b> Running through what a node examination must
    document &mdash; site, size, consistency, tenderness &mdash; she reaches mobility:
    <em>&ldquo;If it&rsquo;s immobile, not moving, <b>that is bad. That is bad, bad, bad.</b>&rdquo;</em>
    And she gives the word to write: document it as <b>immobile or FIXED</b>, <em>&ldquo;because
    that&rsquo;s telling whoever&rsquo;s reading it that it&rsquo;s not moving and it&rsquo;s stuck
    to whatever location it is.&rdquo;</em> The finding is the alarm; the wording is how you pass
    the alarm on.</p>
    <p><b>A rim-enhancing hypodense collection on computed tomography.</b> Her described classic
    for a deep neck abscess &mdash; an enhancing rim around a sac of fluid.
    <em>&ldquo;So this is bad. Now we&rsquo;ve like bad, bad, bad, right? <b>Protect the airway.
    This is a surgical emergency.</b>&rdquo;</em> Antibiotics must cover <b>streptococci,
    staphylococci and anaerobes</b>. She was counting as she went &mdash; this was the second
    emergency of the lecture.</p>
    <p><b>And the one she says is NOT.</b> Leukoplakia [2:37:42]: it does not scrape off, and it
    may bleed if you try &mdash; <em>&ldquo;This is a pre-malignant lesion. This is bad&hellip;
    <b>not bad, bad, bad, but bad enough where we have to work it up relatively
    quickly.</b>&rdquo;</em> Useful in both directions: it fixes leukoplakia one rung below the
    four above, and it confirms the phrase is how she grades urgency out loud.</p>
  </div>

  __SECS__
</section>
""".replace("__SECS__", "".join(secs))


SECTION = build()
