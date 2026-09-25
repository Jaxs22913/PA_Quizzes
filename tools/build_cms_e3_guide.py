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

IMPORTING THIS MODULE MUST NOT WRITE ANYTHING (2026-09-24). Until then the whole
build ran at import time, so `import build_cms_e3_guide` from another script
silently overwrote the shipped guide with an Exam 2 Word link and no footer. The
build now runs only from main(). It also carries the two things the donor could
not supply and that were hand-added to the shipped page after the last build:
the Exam 3 Word link (the donor's head points at cms-exam-2-study-guide.docx)
and the guide footer (the donor's footer sits inside its <main>, which is
dropped). Because the donor is the LIVE Exam 2 guide, any edit to that page's
head or tail changes this output: run with --dry-run first; the build refuses
to overwrite a page it would change unless --force is given.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

from _cms_e3_guide_l15 import SECTION as S15
from _cms_e3_guide_l16 import SECTION as S16
from _cms_e3_guide_l17 import SECTION as S17
from _cms_e3_guide_l18 import SECTION as S18
from _cms_e3_guide_l19 import SECTION as S19

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
  <a class="top-link" href="#nose-sinuses">3 &middot; Nose and Paranasal Sinuses</a>
  <a class="sub-link" href="#l17-sinus">3.1 Sinusitis</a>
  <a class="sub-link" href="#l17-septum">3.2 The septum</a>
  <a class="sub-link" href="#l17-bleed">3.3 Epistaxis</a>
  <a class="sub-link" href="#l17-trauma">3.4 Trauma and foreign bodies</a>
  <a class="sub-link" href="#l17-polyp">3.5 Polyps and rhinitis</a>
  <a class="sub-link" href="#l17-neo">3.6 Neoplasms</a>
  <a class="top-link" href="#neck-masses">4 &middot; Neoplasms and Neck Masses</a>
  <a class="sub-link" href="#l18-anatomy">4.1 Triangles and nodes</a>
  <a class="sub-link" href="#l18-approach">4.2 When to think malignancy</a>
  <a class="sub-link" href="#l18-cong">4.3 Congenital neck masses</a>
  <a class="sub-link" href="#l18-infl">4.4 Inflammatory neck masses</a>
  <a class="sub-link" href="#l18-neo">4.5 Neoplastic neck masses</a>
  <a class="sub-link" href="#l18-thy">4.6 The thyroid</a>
  <a class="top-link" href="#oral-cavity">5 &middot; Oral Cavity, Salivary Glands and Neck</a>
  <a class="sub-link" href="#l19-exam">5.1 Examining the mouth</a>
  <a class="sub-link" href="#l19-var">5.2 Normal variants</a>
  <a class="sub-link" href="#l19-ulcer">5.3 Stomatitis and ulcers</a>
  <a class="sub-link" href="#l19-sal">5.4 Salivary glands</a>
  <a class="sub-link" href="#l19-vc">5.5 Vocal cords and larynx</a>
  <a class="sub-link" href="#l19-air">5.6 The airway emergency</a>
  <a class="sub-link" href="#l19-pha">5.7 Pharyngitis and sequelae</a>
  <a class="sub-link" href="#l19-deep">5.8 Deep neck infections</a>
  <a class="sub-link" href="#l19-dent">5.9 Dentition and the jaw</a>
  <a class="sub-link" href="#l19-les">5.10 Lesions of the oral cavity</a>
  <a class="sub-link" href="#l19-neo">5.11 Neoplasms</a>
</nav>"""

TEST_YOURSELF = '''  var TEST_YOURSELF = {
    ent: [
      {q:"A tuning fork on the forehead is loudest in the RIGHT ear, and on the right bone conduction beats air. What is this?",
       o:["A right conductive loss","A right sensorineural loss",
          "A left conductive loss","Normal hearing"],a:0,
       why:"Weber lateralizes TOWARD a conductive loss, and conductive loss reverses Rinne on that side."},
      {q:"A tuning fork on the forehead is loudest in the LEFT ear, and on the right air still beats bone. What is this?",
       o:["A right sensorineural loss","A right conductive loss",
          "A left conductive loss","Normal hearing"],a:0,
       why:"Weber lateralizes AWAY from a sensorineural loss, and Rinne stays looking normal &mdash; which is why Weber makes the call."},
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
       why:"Viral infection is by far the most common cause overall. Streptococcus pneumoniae, Haemophilus influenzae and Moraxella catarrhalis are only the most common bacterial organisms, and most episodes resolve spontaneously."},
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

# The guide registers one TEST_YOURSELF.ent bank for the whole of ENT, so its
# button sits after the last section rather than inside one. Without it the bank
# is unreachable -- which is how it shipped, until 2026-09-11.
TY_BUTTON = ('\n<button type="button" class="test-yourself-btn" style="--acc:#6a4fa3" '
             'onclick="window.openTestYourself(\'Test yourself &mdash; ENT\', '
             'TEST_YOURSELF.ent)">Test yourself! &rarr;</button>\n')

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

DONOR_DOCX = 'href="cms-exam-2-study-guide.docx"'
OWN_DOCX = 'href="cms-exam-3-study-guide.docx"'

# The donor's footer sits inside its <main>, which is replaced, so the guide's
# own footer is carried here (Back to Homepage, class line, report-a-mistake).
FOOTER = ('<footer class="guide-foot">\n'
          '  <p style="text-align:center;margin:0 0 10px;"><a href="../index.html" style="color:inherit;font-weight:700;text-decoration:none;">&larr; Back to Homepage</a></p>\n'
          '  <p style="text-align:center;">Built from your PAJ 5500 lecture decks for personal study &middot; Class of 2028.</p>\n'
          '  <p style="text-align:center;font-style:italic;">&#9733; <a href="#" style="color:inherit;text-decoration:underline;cursor:pointer" onclick="event.preventDefault(); window.reportMistake()">If you see any mistakes, click here to report it</a> &#9733;</p>\n'
          '</footer>\n')


def main():
    os.chdir(ROOT)
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

    # The donor's head links the Exam 2 Word copy; this page has its own.
    assert head.count(DONOR_DOCX) == 1, "donor Word link not found"
    head = head.replace(DONOR_DOCX, OWN_DOCX)

    head = re.sub(r"<title>.*?</title>",
                  "<title>Clinical Medicine and Surgery I &middot; Exam 3 &mdash; Study Guide</title>",
                  head, count=1, flags=re.S)
    head = re.sub(r"<header class=\"top\">.*?</header>",
      '<header class="top">\n'
      '  <h1>Clinical Medicine and Surgery I &middot; Exam 3 &mdash; Study Guide</h1>\n'
      '  <p>PAJ 5500 Clinical Medicine and Surgery I &middot; Class of 2028</p>\n'
      '  <p>Ear, nose and throat block &middot; <b>all five lectures</b> &middot; Instructional '
      'Objectives taken verbatim from the syllabus</p>\n'
      '</header>', head, count=1, flags=re.S)


    body = ('<main class="content">%s\n%s\n%s\n%s\n%s\n%s%s</main>'
            % (S15, S16, S17, S18, S19, TY_BUTTON, FOOTER))


    html = head + '<div class="layout wrap" data-readable>' + "\n" + TOC + "\n\n" + body + tail
    html = html.replace("</body>", EXTRA + "\n</body>")

    old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else None
    if "--dry-run" in sys.argv:
        print("dry run: the build %s the shipped page" % ("MATCHES" if old == html else "DIFFERS FROM"))
        return
    if old is not None and old != html and "--force" not in sys.argv:
        sys.exit("refusing to overwrite %s: the build would change it (see --dry-run); "
                 "pass --force if the change is intended" % os.path.basename(OUT))

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


if __name__ == "__main__":
    main()
