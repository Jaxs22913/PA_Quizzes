#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Medicine and Surgery I, Exam 3 study guide (ENT block).

Donor is the Exam 2 guide, rethemed INDIGO -> VIOLET so the three CMS blocks
are never confused with each other -- the same progression the comparison
charts use, and #6a4fa3 is already in the site palette.

THE TWO LECTURE SECTIONS ARE GENERATED FROM THE CHART DATA. The eight guide
points the CMS spec asks for are exactly the fields the chart rows already
carry, so the rows are the single source and both surfaces render them. That is
deliberate: on Exam 1 and 2 the same fact was authored twice, once for the chart
and once for the guide, and keeping them in step was manual.

Sections 3 to 5 will be added as Lectures 17 to 19 are built; the header says so
rather than implying the block is complete.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
os.chdir(ROOT)

from _cms_e3_guide_l15 import SECTION as S15
from _cms_e3_guide_l16 import SECTION as S16

DONOR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2/cms-exam-2-study-guide.html")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3/cms-exam-3-study-guide.html")

TOC = """<nav class="toc">
  <a class="top-link" href="#external-middle-ear">1 &middot; External and Middle Ear</a>
  <a class="sub-link" href="#l15-canal">1.1 The external canal</a>
  <a class="sub-link" href="#l15-auricle">1.2 The auricle</a>
  <a class="sub-link" href="#l15-tube">1.3 Eustachian tube and pressure</a>
  <a class="sub-link" href="#l15-om">1.4 The otitis media family</a>
  <a class="sub-link" href="#l15-drum">1.5 The drum and behind it</a>
  <a class="sub-link" href="#l15-fixed">1.6 Fixation and neoplasms</a>
  <a class="top-link" href="#inner-ear">2 &middot; Inner Ear, Balance and Hearing Loss</a>
  <a class="sub-link" href="#l16-tests">2.1 Weber, Rinne and the tracings</a>
  <a class="sub-link" href="#l16-patterns">2.2 The two patterns</a>
  <a class="sub-link" href="#l16-masses">2.3 Tinnitus and visible masses</a>
  <a class="sub-link" href="#l16-acquired">2.4 Acquired sensorineural loss</a>
  <a class="sub-link" href="#l16-vertigo">2.5 The inner ear syndromes</a>
  <a class="sub-link" href="#l16-central">2.6 Retrocochlear and central</a>
</nav>"""

TEST_YOURSELF = '''  var TEST_YOURSELF = {
    ent: [
      {q:"A tuning fork on the forehead is loudest in the RIGHT ear, and on the right bone conduction beats air. What is this?",
       o:["A right conductive loss","A right sensorineural loss",
          "A left conductive loss","Normal hearing"],a:0,
       why:"Weber lateralises TOWARD a conductive loss, and conductive loss reverses Rinne on that side."},
      {q:"A tuning fork on the forehead is loudest in the LEFT ear, and on the right air still beats bone. What is this?",
       o:["A right sensorineural loss","A right conductive loss",
          "A left conductive loss","Normal hearing"],a:0,
       why:"Weber lateralises AWAY from a sensorineural loss, and Rinne stays looking normal &mdash; which is why Weber makes the call."},
      {q:"Vertigo lasting 10 to 60 seconds when rolling over, with normal hearing and no tinnitus. What is it?",
       o:["Benign paroxysmal positional vertigo","M&eacute;ni&egrave;re&rsquo;s disease",
          "Labyrinthitis","Vestibular neuronitis"],a:0,
       why:"Beyond a minute, consider another diagnosis. Hearing being untouched is what excludes M&eacute;ni&egrave;re&rsquo;s."},
      {q:"Sudden vertigo lasting days WITH hearing loss. Which is it?",
       o:["Labyrinthitis","Vestibular neuronitis","Positional vertigo","Otosclerosis"],a:0,
       why:"One word separates the first two: labyrinthitis affects hearing, vestibular neuronitis does not."},
      {q:"An elderly diabetic has ear pain far worse than the canal looks, plus facial weakness. What is this?",
       o:["Necrotizing (malignant) external otitis","Ordinary otitis externa",
          "Otomycosis","Acute otitis media"],a:0,
       why:"Pain out of proportion in a diabetic, with cranial nerve involvement. Imaging shows bony involvement; treat with an antipseudomonal antibiotic."},
      {q:"Gradual hearing loss, a completely NORMAL drum, and the patient hears better in a noisy room. What is this?",
       o:["Otosclerosis","Presbycusis","Cerumen impaction","Otitis media with effusion"],a:0,
       why:"A conductive loss with a normal-looking drum is the pattern; hearing better in noise is the sentence patients volunteer."},
      {q:"Which cause of acute otitis media is by far the most common overall?",
       o:["A virus","Streptococcus pneumoniae","Haemophilus influenzae","Moraxella catarrhalis"],a:0,
       why:"The slide lists only bacteria; he corrected it out loud. Most episodes resolve without antibiotics."},
      {q:"Recurrent ear discharge with NO external canal infection, and white flaky debris in a retraction pocket. What is it?",
       o:["Cholesteatoma","Chronic suppurative otitis media","Otomycosis","Otitis externa"],a:0,
       why:"It erodes bone, so it is removed surgically rather than watched."},
      {q:"Which trough should be UNDETECTABLE, and which must stay high?",
       o:["Gentamicin undetectable; vancomycin high","Both undetectable",
          "Vancomycin undetectable; gentamicin high","Both high"],a:0,
       why:"Concentration-dependent with a post-antibiotic effect against time-dependent killing. Not ENT, but the same reasoning pattern."},
      {q:"A wrestler has a tense swollen auricle with the cartilage landmarks lost. How long do you have?",
       o:["Drain within 7 days, and sooner is better","No urgency",
          "Within 30 days","It never needs draining"],a:0,
       why:"After 7 days granulation makes drainage much harder, and the result is cauliflower ear."}
    ],
  };'''

donor = open(DONOR, encoding="utf-8").read()
head = donor[:donor.index('<div class="layout wrap"')]
tail = donor[donor.index("</main>") + len("</main>"):]
ty_start = tail.index("var TEST_YOURSELF = {")
ty_end = tail.index("\n  };", ty_start) + len("\n  };")
tail = tail[:ty_start] + TEST_YOURSELF.lstrip() + tail[ty_end:]

# Exam 2 is INDIGO; Exam 3 is VIOLET.
for old, new in (("#2d3f7a", "#6a4fa3"), ("#5566b5", "#8a6fc0"), ("#1b2450", "#2f1e52"),
                 ("#7b8ad0", "#a992d8"), ("#1e2233", "#251e33"), ("#b9c2ee", "#cdbde9")):
    head = head.replace(old, new)
    tail = tail.replace(old, new)

head = re.sub(r"<title>.*?</title>",
              "<title>Clinical Medicine and Surgery I &middot; Exam 3 &mdash; Study Guide</title>",
              head, count=1, flags=re.S)
head = re.sub(r"<header class=\"top\">.*?</header>",
  '<header class="top">\n'
  '  <h1>Clinical Medicine and Surgery I &middot; Exam 3 &mdash; Study Guide</h1>\n'
  '  <p>PAJ 5500 Clinical Medicine and Surgery I &middot; Class of 2028</p>\n'
  '  <p>Ear, nose and throat block &middot; <b>Lectures 15 and 16 are here; 17 to 19 are added as '
  'they are delivered</b> &middot; Instructional Objectives taken verbatim from the syllabus</p>\n'
  '</header>', head, count=1, flags=re.S)

body = ('<main class="content">%s\n%s\n'
        '<section class="deck" id="pending"><h2 class="deck-title">3 &middot; Still to come</h2>'
        '<div class="callout warn"><p>The syllabus puts <b>five lectures</b> in this exam. '
        'Lectures 15 and 16 are above. <b>Lecture 17, Disorders of the Nose and Paranasal '
        'Sinuses</b>, was delivered on 3 September and is being built; Lectures 18 and 19 have '
        'not been delivered yet. Treat a gap here as <i>not taught yet</i> rather than <i>not '
        'examinable</i>.</p></div></section>\n</main>' % (S15, S16))

# The condition blocks and the Weber/Rinne table need styles the donor lacks.
EXTRA = """
<style>
  .cond{border:1px solid var(--c-line);border-radius:10px;padding:12px 15px;margin:12px 0;
        background:var(--c-ice);}
  .cond h4{margin:0 0 8px;font-size:1.02rem;display:flex;align-items:baseline;gap:9px;
           flex-wrap:wrap;}
  .cond .u{font-size:.66rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
           padding:2px 8px;border-radius:999px;white-space:nowrap;}
  .cond .u.emerg{background:#8c1d12;color:#fff;} .cond .u.urg{background:#7a5a08;color:#fff;}
  .cond .u.rout{background:#3f5c46;color:#fff;}
  .cond .give{margin:0 0 10px;padding:8px 11px;border-radius:8px;background:var(--c-gv-bg,#f7f0dc);
              color:var(--c-gv-b,#5b4708);font-size:.9rem;}
  dl.eight{display:grid;grid-template-columns:180px 1fr;gap:6px 14px;margin:0;}
  dl.eight dt{font-size:.7rem;font-weight:800;letter-spacing:.04em;text-transform:uppercase;
              color:var(--c-mute);padding-top:3px;}
  dl.eight dd{margin:0;font-size:.9rem;line-height:1.55;}
  .cond .src{margin:9px 0 0;font-size:.7rem;color:var(--c-mute);font-variant-numeric:tabular-nums;}
  .cond figure.fig{float:right;max-width:190px;margin:0 0 10px 14px;}
  .cond figure.fig img{width:100%;height:auto;border-radius:8px;border:1px solid var(--c-line);}
  table.wr{width:100%;border-collapse:collapse;font-size:.88rem;}
  table.wr th{text-align:left;background:var(--c-panel);color:var(--c-panel-fg);padding:8px;}
  table.wr td{padding:8px;border-top:1px solid var(--c-line);}
  .tbl-wrap{overflow-x:auto;margin:10px 0;}
  @media (max-width:640px){dl.eight{grid-template-columns:1fr;gap:2px;}
    dl.eight dd{margin-bottom:7px;} .cond figure.fig{float:none;max-width:100%;margin:0 0 10px;}}
</style>"""

html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + body + tail
html = html.replace("</body>", EXTRA + "\n</body>")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)

IMGDIR = "cms-ent-chart-images"
for fn in re.findall(r'src="%s/([^"]+)"' % IMGDIR, html):
    assert os.path.exists(os.path.join(os.path.dirname(OUT), IMGDIR, fn)), fn
for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li", "nav",
            "figure", "figcaption", "dl", "dt", "dd", "blockquote"):
    o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
    assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
assert "data-audio-dir" not in html, "audio dir must stay absent until mp3s exist"
assert "#2d3f7a" not in html, "donor indigo left in the Exam 3 guide"
print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
print("subsections: %d   conditions: %d   figures: %d   test-yourself: %d"
      % (html.count('class="sub"'), html.count('<div class="cond">'),
         html.count("<figure"), TEST_YOURSELF.count("{q:")))
