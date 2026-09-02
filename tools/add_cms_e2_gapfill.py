#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fill the gaps a full scour of the Exam 2 PowerPoints turned up.

tools/audit_cms_e2_coverage.py scores every slide in all five decks against the
guide, chart and cram sheet. Eight slides came back materially uncovered, all
of them the same shape: DIFFERENTIAL DIAGNOSIS slides and one anatomy slide,
which are easy to skip when writing from a disease-by-disease outline because
they do not belong to any single disease.

  L10 slide 3   the eye in three tunics
  L11 slide 4   nystagmus classification -- pendular against jerk, the subtypes
  L13 slide 15  macular dystrophies that mimic age-related degeneration
  L13 slide 43  what else causes leukocoria besides retinoblastoma
  L13 slide 44  uveal melanoma by site, with sentinel vessel and extrascleral spread
  L13 slide 48  iris nevus, in detail
  L13 slide 50  the pigmented iris lesion differential
  L13 slide 55  the non-pigmented conjunctival lesion differential

Each block is spliced before the closing tag of its own section so the existing
numbering is untouched, and is fenced so re-running replaces rather than
duplicates.
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2")
GUIDE = os.path.join(DIR, "cms-exam-2-study-guide.html")
CRAM = os.path.join(DIR, "cms-exam-2-cram-sheet.html")

ANATOMY = """
  <h3 class="sub" id="e2l1-anatomy">1.12 &middot; The eye in three layers</h3>
  <p>Every disorder in this block sits in one of three tunics, and naming the layer usually names
  the kind of problem.</p>
  <table class="tbl">
    <tr><th>Layer</th><th>Structure</th><th>What it does</th></tr>
    <tr><td rowspan="2"><b>Fibrous</b><br><span class="muted">outer</span></td>
        <td><b>Cornea</b></td><td>Transparent front surface; provides <b>most of the eye's focusing power</b></td></tr>
    <tr><td><b>Sclera</b></td><td>Tough white coat; maintains shape and gives the muscles their attachment</td></tr>
    <tr><td rowspan="3"><b>Vascular (uvea)</b><br><span class="muted">middle</span></td>
        <td><b>Iris</b></td><td>The coloured part; controls pupil size and so regulates light entry</td></tr>
    <tr><td><b>Ciliary body</b></td><td><b>Produces aqueous humour</b> and controls lens accommodation</td></tr>
    <tr><td><b>Choroid</b></td><td>Highly vascular; <b>nourishes the retina</b></td></tr>
    <tr><td rowspan="4"><b>Neural</b><br><span class="muted">inner</span></td>
        <td><b>Retina</b></td><td>Rods and cones convert light into neural signals</td></tr>
    <tr><td><b>Macula</b></td><td>Central vision</td></tr>
    <tr><td><b>Fovea</b></td><td>Highest visual acuity</td></tr>
    <tr><td><b>Optic disc</b></td><td>Where the optic nerve exits &mdash; the blind spot</td></tr>
  </table>
  <p class="muted">Useful shorthand: uveitis is inflammation of the <i>middle</i> layer, which is why
  it takes iris, ciliary body and choroid together; scleritis and episcleritis sit in the
  <i>outer</i>; and the vascular occlusions and detachments are all <i>inner</i>-layer disease.</p>
"""

NYSTAGMUS = """
  <h3 class="sub" id="e2l2-nystagmus-types">2.10 &middot; Nystagmus &mdash; the two classification groups</h3>
  <p>Nystagmus splits into two groups, and the split is the first thing to establish.</p>
  <table class="tbl">
    <tr><th></th><th>Jerk</th><th>Pendular</th></tr>
    <tr><td><b>Phases</b></td><td>A slow phase and a fast phase</td><td><b>Both phases equal</b> in velocity and amplitude &mdash; <b>no fast phase at all</b></td></tr>
    <tr><td><b>Named for</b></td><td>The direction of the <b>FAST</b> beat &mdash; vertical, horizontal or torsional</td><td>Not named by beat, since there is no fast beat</td></tr>
    <tr><td><b>Behaviour</b></td><td><b>Increases with gaze toward the fast phase</b></td><td>Most often horizontal</td></tr>
    <tr><td><b>Context</b></td><td>Most common form is <b>horizontal jerk</b> &mdash; eyes drift slowly one way, snap back</td><td>Usually <b>congenital</b>, or follows <b>prolonged bilateral blindness beginning in childhood</b></td></tr>
  </table>
  <p><strong>The horizontal jerk subtypes:</strong> normal <b>physiologic gaze-evoked</b>,
  <b>infantile</b>, <b>spasmus nutans</b>, and <b>latent</b> nystagmus.</p>
  <div class="callout">
    <p><strong>Upbeat nystagmus is ALWAYS abnormal.</strong> It means a <strong>cerebellar or
    medullary lesion</strong>, and less commonly <strong>drug intoxication</strong>. It is present
    only on <em>upward</em> gaze. This is the one direction that carries its own alarm.</p>
  </div>
"""

TUMOUR_DDX = """
  <h3 class="sub" id="e2l4-ddx">4.11 &middot; The differentials &mdash; what else looks like this</h3>
  <p>Each tumour and each macular disease comes with a list of mimics, and a vignette is far more
  likely to ask you to separate them than to name the obvious one.</p>

  <h4>Macular dystrophies that mimic age-related macular degeneration</h4>
  <table class="tbl">
    <tr><th>Condition</th><th>What gives it away</th></tr>
    <tr><td><b>Stargardt disease</b> (late-onset)</td><td>Inherited macular dystrophy with <b>yellow-white flecks</b> and central vision loss</td></tr>
    <tr><td><b>Sorsby fundus dystrophy</b></td><td><b>Autosomal dominant</b>; choroidal neovascularisation that looks like <b>wet</b> degeneration</td></tr>
    <tr><td><b>North Carolina macular dystrophy</b></td><td><b>Congenital and non-progressive</b> macular changes resembling degeneration</td></tr>
    <tr><td><b>Best disease</b> (vitelliform)</td><td><b>Lipofuscin accumulation mimics drusen</b>, but presents <b>earlier in life</b></td></tr>
  </table>
  <p class="muted">The common thread: all four are <b>inherited</b> and most present <b>younger</b>
  than age-related degeneration. A macular picture in a patient too young for it is the cue.</p>

  <h4>Leukocoria &mdash; what else besides retinoblastoma</h4>
  <table class="tbl">
    <tr><th>Condition</th><th>What gives it away</th></tr>
    <tr><td><b>Coats' disease</b></td><td>Idiopathic <b>retinal telangiectasia with exudation</b>, often unilateral</td></tr>
    <tr><td><b>Persistent fetal vasculature</b></td><td>Congenital anomaly with <b>remnants of fetal vasculature</b>, typically unilateral</td></tr>
    <tr><td><b>Toxocariasis</b></td><td>Parasitic infection causing <b>granulomatous</b> retinal inflammation</td></tr>
    <tr><td><b>Retinal astrocytoma</b></td><td>Benign <b>glial</b> tumour, often with <b>tuberous sclerosis</b></td></tr>
    <tr><td><b>Medulloepithelioma</b></td><td>Rare tumour of the <b>nonpigmented ciliary epithelium</b></td></tr>
    <tr><td><b>Congenital cataract</b></td><td>Produces a white pupillary reflex without any tumour</td></tr>
    <tr><td><b>Ocular toxoplasmosis</b></td><td>Retinal <b>scarring and inflammation</b></td></tr>
  </table>

  <h4>Uveal melanoma by site</h4>
  <p>Uveal melanoma is named for where in the uvea it sits &mdash; <b>iris</b>, <b>ciliary body</b>
  or <b>choroid</b> &mdash; and an iris melanoma may be <b>melanotic or partly amelanotic</b>, so
  pigment is not required. Two signs point to a ciliary body lesion in particular: a
  <strong>sentinel vessel</strong> (a dilated episcleral vessel overlying the tumour) and
  <strong>extrascleral extension</strong>.</p>

  <h4>Iris nevus, and the pigmented iris differential</h4>
  <p>An <strong>iris nevus</strong> is a small pigmented, benign spot, usually apparent around
  <b>puberty</b> and <b>asymptomatic</b>. It sits in the <b>inferior half</b> of the iris, does not
  typically grow, is <b>flat or minimally elevated (under 1 mm)</b> and uncommonly over 3 mm across,
  and is usually not vascular. It may pull the pupil out of shape &mdash;
  <strong>corectopia</strong>.</p>
  <table class="tbl">
    <tr><th>Lesion</th><th>What separates it</th></tr>
    <tr><td><b>Iris freckle</b></td><td>Flat, superficial pigment; <b>no stromal involvement or distortion</b>; usually bilateral and multifocal</td></tr>
    <tr><td><b>Lisch nodules</b></td><td>Tan nodules of <b>neurofibromatosis type 1</b>; bilateral, multifocal, non-progressive</td></tr>
    <tr><td><b>Melanocytoma</b></td><td>Dark brown, <b>granular</b>; usually benign but can cause <b>secondary glaucoma through pigment dispersion</b></td></tr>
    <tr><td><b>Melanocytosis</b></td><td>Congenital uveal pigmentation, sectoral or diffuse; <b>raises the risk of uveal melanoma</b></td></tr>
    <tr><td><b>Cogan-Reese (ICE) syndrome</b></td><td>Pigmented iris nodules with <b>corneal endothelial abnormality</b>; secondary glaucoma</td></tr>
    <tr><td><b>Iris melanoma</b></td><td>Nodular or diffuse growth; may show <b>vascularity, ectropion uveae, sectoral cataract or seeding</b></td></tr>
    <tr><td><b>Metastatic carcinoma</b></td><td>Secondary deposit rather than a primary iris lesion</td></tr>
  </table>
  <p class="muted">Risk factors that push an iris lesion toward melanoma: <b>inferior location</b>,
  <b>diffuse configuration</b>, and <b>blood in the anterior chamber</b>.</p>

  <h4>Non-pigmented conjunctival lesions</h4>
  <p>Conjunctival melanoma is pigmented, so the useful differential is the lesions that are not.</p>
  <table class="tbl">
    <tr><th>Lesion</th><th>What gives it away</th></tr>
    <tr><td><b>Squamous cell carcinoma</b></td><td><b>Gelatinous or leukoplakic</b>; can be mistaken for an <b>amelanotic melanoma</b></td></tr>
    <tr><td><b>Conjunctival lymphoma</b></td><td><b>Salmon-pink, painless</b> mass, typically in the fornix or bulbar conjunctiva</td></tr>
    <tr><td><b>Kaposi sarcoma</b></td><td><b>Reddish-purple vascular</b> lesion, associated with <b>HIV/AIDS</b></td></tr>
    <tr><td><b>Pyogenic granuloma</b></td><td><b>Rapidly growing red</b> mass, often after <b>trauma or surgery</b></td></tr>
  </table>
"""

BLOCKS = [("ophthalmology-i", "GAPFILL-ANATOMY", ANATOMY),
          ("neuro-ophthalmology", "GAPFILL-NYSTAGMUS", NYSTAGMUS),
          ("chronic-vision-loss", "GAPFILL-DDX", TUMOUR_DDX)]

# Each new link goes after the LAST sub-link of its section, so the table of
# contents keeps its order.
TOC_ADDS = [
 ('href="#e2l1-disposition"', '  <a class="sub-link" href="#e2l1-anatomy">1.12 The eye in three layers</a>\n'),
 ('href="#e2l2-care"', '  <a class="sub-link" href="#e2l2-nystagmus-types">2.10 Nystagmus classification</a>\n'),
 ('href="#e2l4-melanoma"', '  <a class="sub-link" href="#e2l4-ddx">4.11 The differentials</a>\n'),
]


def splice_into_section(t, sec_id, fence, block):
    op, cl = "<!--%s-->" % fence, "<!--/%s-->" % fence
    pat = re.compile(re.escape(op) + ".*?" + re.escape(cl), re.S)
    fenced = op + block + cl
    if pat.search(t):
        return pat.sub(lambda _: fenced, t, count=1)
    start = t.index('id="%s"' % sec_id)
    end = t.index("</section>", start)
    return t[:end] + fenced + "\n" + t[end:]


def main():
    t = io.open(GUIDE, encoding="utf-8").read()
    before = len(t)
    for sec_id, fence, block in BLOCKS:
        t = splice_into_section(t, sec_id, fence, block)

    for anchor, line in TOC_ADDS:
        if line.strip() in t:
            continue
        i = t.index(anchor)
        j = t.index("\n", i) + 1
        t = t[:j] + line + t[j:]

    io.open(GUIDE, "w", encoding="utf-8").write(t)
    print("guide %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    for need in ('id="e2l1-anatomy"', 'id="e2l2-nystagmus-types"', 'id="e2l4-ddx"',
                 'id="ocular-trauma"', 'id="chronic-vision-loss"', "    trauma: [", "    cvl: ["):
        assert need in t, "missing after splice: %s" % need
    nav_a, nav_b = t.index('<nav class="toc">'), t.index("</nav>")
    for link in ('href="#e2l1-anatomy"', 'href="#e2l2-nystagmus-types"', 'href="#e2l4-ddx"'):
        assert nav_a < t.index(link) < nav_b, "%s landed outside <nav>" % link
    main_a, main_b = t.index("<main"), t.index("</main>")
    for sid in ('id="e2l1-anatomy"', 'id="e2l2-nystagmus-types"', 'id="e2l4-ddx"'):
        assert main_a < t.index(sid) < main_b, "%s landed outside <main>" % sid
    for tag in ("section", "table", "tr", "td", "th", "div", "p", "ol", "ul", "li",
                "figure", "figcaption", "h4"):
        o = len(re.findall(r"<%s[ >]" % tag, t)); c = t.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    print("verified: 3 blocks inside <main>, 3 links inside <nav>, tags balanced")


if __name__ == "__main__":
    main()
