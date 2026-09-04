#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 3 ENT Comparison Chart.

The Exam 3 counterpart to the Exam 1 dermatology and Exam 2 ophthalmology
charts: every condition in the ear, hearing and balance block in one sortable
table, read left to right.

BUILT INCREMENTALLY ON PURPOSE. Jaxon, 3 September: "You can build the charts
and add stuff as we add." The syllabus puts five lectures in this exam
(15-19); Lectures 15 and 16 were delivered on 3 September and are here. The
page says so plainly rather than implying the block is complete, and the
remaining lectures drop in as ROWS_L17/18/19 modules without touching this
file's structure.

THE THREE GREY COLUMNS ARE THE BLOCK'S OWN DISCRIMINATORS, NOT THE LAST
EXAM'S. Ophthalmology used pain / laterality / pupil, because that is what
Professor Jaquith told the class to chart. Ear disease does not separate on
laterality -- almost everything here is unilateral -- so the middle column
becomes TYPE OF HEARING LOSS. Conductive against sensorineural is the single
axis this block turns on: it is Lecture 16's first objective, it is what Weber
and Rinne exist to answer, and it is what sorts nineteen of these rows.

IMAGES ARE USED AND CITED, per [[media_asset_licensing]]: any image in a course
PowerPoint may be used as long as the slide is cited. Several of these carry
their source baked into the pixels -- UpToDate, McGraw-Hill, the Atlas of
Emergency Medicine, Northwestern University -- and those are LEFT VISIBLE on
purpose, as part of citing the slide.

EVERY PICTURE CITES ITS LECTURE AS WELL AS ITS SLIDE, because two decks number
their slides independently and one row legitimately borrows the other
lecture's photograph: barotrauma is taught in Lecture 15, but the only
haemotympanum in either deck is Lecture 16 slide 59. The citation is derived
from the filename prefix so it cannot drift from the file.
"""
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2/cms-ophtho-comparison-chart.html")
OUT = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3/cms-ent-comparison-chart.html")

from _cms_e3_chart_l15 import ROWS_L15, DIFF_L15, IMGS_L15
from _cms_e3_chart_l16 import ROWS_L16, DIFF_L16, IMGS_L16
from _cms_e3_chart_l17 import ROWS_L17, DIFF_L17, IMGS_L17

ROWS = ROWS_L15 + ROWS_L16 + ROWS_L17
DIFF = dict(DIFF_L15, **DIFF_L16, **DIFF_L17)
IMGS = dict(IMGS_L15, **IMGS_L16, **IMGS_L17)

# Exam 1 is teal, Exam 2 indigo, Exam 3 violet, so the three CMS charts are
# never confused with each other. #6a4fa3 is ALREADY IN THE SITE PALETTE (it is
# Clinical Pathophysiology Exam 1's spine) rather than a new hex invented for
# this page -- see [[site_design_tokens]]. The supporting shades are not chosen
# either: each one is the Exam 2 chart's corresponding shade rotated to the
# violet hue with saturation and lightness untouched, so the whole family keeps
# the recipe the other two charts were built on.
import colorsys
ACCENT = "#6a4fa3"

def _hue_of(hexs):
    r, g, b = (int(hexs[i:i+2], 16) / 255 for i in (1, 3, 5))
    return colorsys.rgb_to_hls(r, g, b)[0]

def _rotate(hexs, hue):
    r, g, b = (int(hexs[i:i+2], 16) / 255 for i in (1, 3, 5))
    _h, l, s = colorsys.rgb_to_hls(r, g, b)
    r, g, b = colorsys.hls_to_rgb(hue, l, s)
    return "#%02x%02x%02x" % (round(r*255), round(g*255), round(b*255))

_HUE = _hue_of(ACCENT)
# The Exam 2 palette, in the order the ophthalmology builder substitutes them.
_E2 = ["#2d3f7a", "#5566b5", "#1e2a52", "#d3d8ea", "#f8f9fd",
       "#1e2233", "#eef0fa", "#525c78", "#646d88", "#4f5872"]
PALETTE = [(o, _rotate(o, _HUE)) for o in _E2]

GROUP_COLOUR = {
 # Lecture 15 -- the conducting apparatus. Warmer, earthier tones: these are
 # the rows you diagnose by LOOKING in the ear.
 "Eustachian tube": "#2f6b5a", "Otitis media": "#8f5aa8", "Pressure and wax": "#7a5a2e",
 "Middle ear mass": "#6b2233", "Ear trauma": "#94371f", "Foreign body": "#8a5a2b",
 "External canal infection": "#a4502a", "Conductive fixation": "#4a6b7a",
 "Neoplasm": "#5f3a8a",
 # Lecture 16 -- hearing and balance. Cooler tones, because these are the rows
 # where the otoscope is normal and the diagnosis comes from a test or a
 # history. The two hearing-loss PATTERNS take the deepest tone: they are not
 # diseases, they are the axis every other row sorts on.
 "Hearing loss pattern": "#3a3a6b", "Tinnitus": "#8a5f8d", "Canal and middle ear mass": "#7a2f5f",
 "Acquired sensorineural": "#2a5f8f", "Inner ear syndrome": "#15707f",
 "Retrocochlear and central": "#8c1d12", "Non-organic": "#4f5666",
 # Lecture 17 -- the nose. A separate warm family so the nasal rows never read
 # as a variant of an ear group at a glance.
 "Sinusitis": "#9c5230", "Septum": "#7a4a2e", "Epistaxis": "#8c1d12",
 "Nasal trauma": "#94371f", "Foreign body": "#8a5a2b", "Polyps and rhinitis": "#6b7f35",
 "Neoplasm": "#5f3a8a",
}

DECKS = {"l15": ("L15", "Disorders of the External and Middle Ear"),
         "l16": ("L16", "Disorders of the Inner Ear"),
         "l17": ("L17", "Disorders of the Nose and Paranasal Sinuses")}


def classify(pain, hearing):
    """Drive the two filter rows. Kept deliberately blunt: a row is 'painful'
    only if its pain cell actually says so, and the hearing filter reads the
    TYPE off the cell rather than guessing from the condition name."""
    p = re.sub(r"<[^>]+>", "", pain).strip().lower()
    painful = "yes" if p.startswith(("yes", "severe")) else \
              "varies" if p.startswith(("varies", "depends")) else "no"
    h = re.sub(r"<[^>]+>", "", hearing).strip().lower()
    if h.startswith(("none", "not affected", "claimed")):
        hl = "none"
    elif "sensorineural" in h and "conductive" in h:
        hl = "either"
    elif "sensorineural" in h:
        hl = "snhl"
    elif "conductive" in h:
        hl = "cond"
    else:
        hl = "either"
    return painful, hl


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index("</head>")]
    for old, new in PALETTE:
        head = head.replace(old, new)
    head = re.sub(r"<title>.*?</title>",
                  "<title>ENT Comparison Chart &mdash; CMS I Exam 3</title>",
                  head, count=1, flags=re.S)
    head = head.replace('href="cms-ophtho-comparison-chart.docx"',
                        'href="cms-ent-comparison-chart.docx"')

    groups = []
    for g in dict.fromkeys(r[1] for r in ROWS):
        groups.append('<button class="filt" data-g="%s" style="--g:%s">%s</button>'
                      % (H.escape(g), GROUP_COLOUR[g], H.escape(g)))

    imgdir = os.path.join(os.path.dirname(OUT), "cms-ent-chart-images")
    body_rows, n_pics = [], 0
    for row in ROWS:
        name, grp, give, pres, test, tx, urg, edu, slide, deck = row
        _u = urg.upper()
        urg_cls = ("emerg" if "EMERGENT" in _u else
                   "sameday" if "SAME DAY" in _u else
                   "urg" if "URGENT" in _u else "rout")
        pic = IMGS.get(name)
        if pic:
            fn, sl = pic
            assert os.path.exists(os.path.join(imgdir, fn)), \
                "missing %s -- run extract_cms_e3_chart_images.py" % fn
            n_pics += 1
            # The lecture comes from the FILENAME, not from the row, so a
            # borrowed picture cites the deck it actually came from.
            lect = DECKS[fn.split("-")[0]][0]
            cell = ('<img src="cms-ent-chart-images/%s" loading="lazy" '
                    'alt="%s, from the lecture slides."><span class="picite">%s slide %d</span>'
                    % (fn, H.escape(re.sub("&[a-z]+;", " ", name)), lect, sl))
        else:
            cell = '<span class="nopic">no image<br>on the slide</span>'
        lect = ("L15" if deck.startswith("Disorders External")
                else "L17" if deck.startswith("hughie") else "L16")
        slide_cell = '<b class="lect">%s</b><br>%s' % (lect, slide)
        pain, hear, sign = DIFF[name]
        painful, hl = classify(pain, hear)
        body_rows.append(
            '<tr data-g="%s" data-pain="%s" data-hl="%s">'
            '<td class="pic">%s</td>'
            '<td class="nm"><b>%s</b><span class="grp" style="background:%s">%s</span>'
            '<span class="sl">%s</span></td>'
            '<td class="d pain">%s<span class="side">%s</span></td><td class="d sign">%s</td>'
            '<td class="gv">%s</td><td>%s</td><td>%s</td>'
            '<td>%s<span class="u %s">%s</span></td><td>%s</td></tr>'
            % (H.escape(grp), painful, hl, cell, name, GROUP_COLOUR[grp], H.escape(grp),
               slide_cell, pain, hear, sign, give, pres, test, tx, urg_cls, urg, edu))

    html = head + """</head><body>
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">
<header class="top">
  <h1>ENT Comparison Chart</h1>
  <p>Clinical Medicine and Surgery I &middot; Exam 3 &middot; Class of 2028</p>
  <p>__N__ conditions from the ear, hearing, balance and nose lectures</p>
  <p style="margin-top:10px;font-size:.82rem;color:var(--c-mute)">Use the <b>Download as PDF</b> button,
  top right, to keep this offline &mdash; it prints landscape with every row intact.</p>
</header>

<div class="howto"><b>This chart is still being built.</b> The exam covers five lectures.
<b>Lectures 15, 16 and 17 are in it</b> &mdash; the external and middle ear, the inner ear,
hearing and balance, then the nose and paranasal sinuses. Lectures 18 and 19 will be added as
they are delivered, so treat a
gap here as &ldquo;not taught yet&rdquo; rather than &ldquo;not examinable&rdquo;.<br><br>
<b>How to use this.</b> Read it left to right for one condition: <b>the words a question will use
to hand it to you</b>, how it presents and what you find on examination, what you order, what you
give, <b>how fast the patient has to be seen</b>, and what you tell them. Read it top to bottom
down one column to compare across conditions.<br><br>
<b>The three grey columns are this block&rsquo;s discriminators.</b> On the ophthalmology chart they
were pain, laterality and the pupil. Ear disease does not separate on laterality &mdash; nearly
everything here is one-sided &mdash; so the middle column is <b>the type of hearing loss</b>, and
for the nasal rows it carries <b>the discharge</b>, which is that half's most useful sign.
<b>Conductive against sensorineural is the axis this whole block turns on</b>: it is the first
thing Lecture 16 asks you to distinguish, it is the entire reason Weber and Rinne exist, and it
sorts almost every row on this page. The buttons above let you pull out just the conductive
causes, or just the painful ones, and read down.<br><br>
<b>This is the shape of the exam question, stated in the lecture.</b> Lecture 16 stopped on a
worked vignette &mdash; ear fullness and reduced hearing after a cold, an amber effusion behind an
intact drum with reduced mobility &mdash; and asked <i>which Weber and Rinne findings are most
likely</i>, with the note: <i>&ldquo;this is what I expect you to get right on the test, because
there is a test question like this.&rdquo;</i> The reverse was described too: <b>given the Weber
and Rinne results, name the diagnosis</b> &mdash; <i>&ldquo;I can give you these results and
you&rsquo;ll automatically know if it&rsquo;s conductive or sensorineural &hellip; I have things
like wax impaction on there, and that would be the answer, because the other choices
wouldn&rsquo;t be conductive.&rdquo;</i> <b>That is exactly why the hearing-loss column is the one
to read down</b>: in that question the wrong answers are eliminated by loss type before you think
about anything else.<br><br>
<b>Weber and Rinne, once, so the middle column reads quickly.</b>
<b>Conductive:</b> Weber lateralises <b>to the bad ear</b>, and bone conduction is <b>equal to or
better than</b> air conduction. <b>Sensorineural:</b> Weber lateralises <b>away, to the good
ear</b>, and air conduction still beats bone &mdash; the same Rinne as a normal ear, which is why
<b>Weber is the one that makes the call</b>.<br><br>
<b>The gold &ldquo;Vignette giveaway&rdquo; column</b> is the one to scan when a stem is in front
of you. A vignette gives itself away in a handful of words &mdash; <i>pain on moving the tragus</i>,
<i>hearing is better in background noise</i>, <i>pain out of proportion to the exam</i>,
<i>&ldquo;wet newspaper&rdquo;</i>, <i>the pain stopped when it ruptured</i>. Every phrase there is
language the lecture decks themselves use.<br><br>
<b>The &ldquo;How fast&rdquo; column</b> carries over from the ophthalmology chart, and four rows
here earn <span class="u emerg" style="padding:1px 6px">EMERGENT</span>: malignant otitis externa,
carcinoma of the ear canal, sudden sensorineural hearing loss, and vertigo with brainstem signs.
Three of those are conditions whose <i>whole</i> teaching point is that they get mistaken for
something routine.<br><br>
<b>Every picture cites its lecture as well as its slide.</b> The two decks number their slides
independently, so &ldquo;slide 49&rdquo; alone means nothing &mdash; and one row deliberately
borrows the other lecture&rsquo;s photograph, because barotrauma is taught in Lecture 15 but the
only haemotympanum in either deck is on Lecture 16&rsquo;s slide 59. Several pictures carry their
source stamped into the image; those marks are left visible on purpose, as part of the
citation.<br><br>
<b>Three of the pictures come from slides with no words on them at all</b> &mdash; Lecture 16
slides 49, 51 and 59 are bare photographs. Each was resolved against the slide <i>before</i> it
(Exostosis, Glomus Tumors, Barotrauma) rather than guessed at, which is the only reason the
exostosis and glomus cells are the right way round.<br><br>
<b>Nineteen rows have no picture, and that is not an oversight.</b> Lecture 16 teaches most of its
sensorineural causes as histories and audiograms rather than photographs &mdash; there is nothing
to photograph in ototoxicity, M&eacute;ni&egrave;re&rsquo;s or vestibular neuronitis. The rows that
carry a picture are the ones the decks actually picture. Product shots, instrument trays and stock
cartoons were left out: a cell that shows a bottle of ear drops does not tell you what the disease
looks like.<br><br>
<b>Mastoiditis is filed under Lecture 15, not 16.</b> It is listed as a Lecture 16 objective, but
the only teaching on it in either deck is one line of Lecture 15&rsquo;s slide 19, as a
complication of acute otitis media. It sits where the content is.</div>

<div class="filters"><button class="filt on" data-g="__all__">All</button>__GROUPS__</div>
<div class="filters filters2">
  <span class="flabel">Sort by:</span>
  <button class="filt2" data-hl="cond">Conductive</button>
  <button class="filt2" data-hl="snhl">Sensorineural</button>
  <button class="filt2" data-hl="none">Hearing normal</button>
  <button class="filt2" data-pain="yes">Painful</button>
  <button class="filt2" data-pain="no">Painless</button>
  <button class="filt2 on" data-clear="1">Show all</button>
</div>

<div class="tblwrap"><table>
<colgroup>
  <col style="width:11%"><col style="width:10%"><col style="width:9%"><col style="width:11%">
  <col style="width:12%"><col style="width:14%"><col style="width:12%"><col style="width:11%">
  <col style="width:10%">
</colgroup>
<thead><tr>
  <th>Picture</th>
  <th>Condition</th>
  <th class="d-h">Pain &amp; hearing loss<br><span style="font-weight:400;opacity:.75">discharge, for the nose</span></th>
  <th class="d-h">Key exam finding</th>
  <th class="gv-h">Vignette giveaway<br><span style="font-weight:400;opacity:.75">the words that hand it to you</span></th>
  <th>Presentation &amp; exam findings</th>
  <th>Testing &amp; what causes it</th>
  <th>Treatment &amp; how fast</th>
  <th>Patient education &amp; prognosis</th>
</tr></thead>
<tbody>
__ROWS__
</tbody></table></div>
</div>
<script src="../theme.js"></script>
<script>
  // Two independent filters: group (top row) and the block's discriminators
  // (second row). Both apply at once, so "otitis media AND painful" works.
  var curG = '__all__', curPain = null, curHl = null;
  function apply(){
    document.querySelectorAll('tbody tr').forEach(function(tr){
      var ok = (curG === '__all__' || tr.dataset.g === curG)
            && (!curPain || tr.dataset.pain === curPain)
            && (!curHl   || tr.dataset.hl === curHl || tr.dataset.hl === 'either');
      tr.style.display = ok ? '' : 'none';
    });
  }
  document.querySelectorAll('.filt').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.filt').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on'); curG = b.dataset.g; apply();
    });
  });
  document.querySelectorAll('.filt2').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.filt2').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on');
      curPain = b.dataset.pain || null;
      curHl   = b.dataset.hl   || null;
      apply();
    });
  });
</script>
<style>
  .filters{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 10px;}
  .filt{font:inherit;font-size:.82rem;padding:5px 12px;border-radius:999px;cursor:pointer;
        border:1px solid var(--c-line);background:var(--c-btn-bg);color:var(--c-fg);}
  .filt.on{background:var(--acc);color:#fff;border-color:var(--acc);}
  table{table-layout:fixed;}
  td, th{overflow-wrap:break-word;}
  td.nm{white-space:normal;}
  td.nm .sl{display:block;margin-top:5px;font-size:.66rem;color:var(--c-mute);
            font-variant-numeric:tabular-nums;line-height:1.35;}
  td.nm .grp{display:block;margin-top:4px;font-size:.66rem;color:#fff;padding:1px 7px;
             border-radius:999px;width:fit-content;letter-spacing:.02em;}
  td.gv{background:var(--c-gv-bg);color:var(--c-gv-b);font-weight:600;}
  td.sl{text-align:center;color:var(--c-mute);white-space:nowrap;font-variant-numeric:tabular-nums;}
  td.pic{text-align:center;vertical-align:top;padding:8px;}
  td.pic img{width:100%;max-width:180px;height:auto;border-radius:6px;display:block;margin:0 auto;
             border:1px solid var(--c-line);}
  td.pic .picite{display:block;margin-top:4px;font-size:.66rem;color:var(--c-mute);}
  td.pic .nopic{display:inline-block;font-size:.7rem;color:var(--c-mute);line-height:1.3;}
  th.d-h{background:var(--c-panel);color:var(--c-panel-fg);}
  td.d{background:var(--c-panel);font-size:.82rem;}
  td.pain .side{display:block;margin-top:3px;opacity:.85;}
  td .u{display:block;margin-top:6px;}
  .filters2{margin-top:-4px;align-items:center;}
  .flabel{font-size:.8rem;color:var(--c-mute);margin-right:4px;}
  .filt2{font:inherit;font-size:.8rem;padding:4px 11px;border-radius:999px;cursor:pointer;
         border:1px solid var(--c-line);background:var(--c-btn-bg);color:var(--c-fg);}
  .filt2.on{background:var(--gold);color:#241a02;border-color:var(--gold);}
  td .u{font-weight:700;font-size:.78rem;}
  td .u.emerg{color:#8c1d12;} td .u.sameday{color:#8c4a12;}
  td .u.urg{color:#7a5a08;} td .u.rout{color:#3f5c46;font-weight:600;}
</style>
</body></html>"""
    html = (html.replace("__ROWS__", "\n".join(body_rows))
                .replace("__GROUPS__", "".join(groups))
                .replace("__N__", str(len(ROWS))))

    for tag in ("table", "thead", "tbody", "tr", "td", "th", "div", "p", "header"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    for fn in re.findall(r'src="cms-ent-chart-images/([^"]+)"', html):
        assert os.path.exists(os.path.join(imgdir, fn)), fn
    missing = [r[0] for r in ROWS if r[0] not in DIFF]
    assert not missing, ("every row needs pain, hearing loss and the key exam "
                         "finding: %r" % missing)
    names = [r[0] for r in ROWS]
    assert len(names) == len(set(names)), "duplicate condition row"
    for r in ROWS:
        assert r[1] in GROUP_COLOUR, "row %r has an unknown group" % r[0]
        assert all(str(x).strip() for x in r), "row %r has an empty cell" % r[0]
    # The Exam 2 STYLESHEET must not survive into an Exam 3 page. Scoped to the
    # substituted head: the group-chip palette below is an independent set of
    # hues and may legitimately reuse a colour the donor also used.
    for old, _new in PALETTE:
        assert old not in head, "Exam 2 colour %s survived substitution" % old

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d conditions, %d with a picture, %d groups)"
          % (os.path.basename(OUT), len(html) // 1024, len(ROWS), n_pics, len(GROUP_COLOUR)))
    from collections import Counter
    print("urgency: %s" % dict(Counter(
        ("emerg" if "EMERGENT" in r[6].upper() else
         "urgent" if "URGENT" in r[6].upper() else "routine") for r in ROWS)))


if __name__ == "__main__":
    main()
