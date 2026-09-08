#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the ENT OSCE Disease Chart for Physical Diagnosis 2.

Jaxon, 2026-09-08: "a chart that has all the ENT diseases. Split them into
Emergent and Nonemergent (put nonemergent at the top) and this is for the ENT
OSCE so put it with PD. For each disease process I need how the patient
describes it/common complaint, clinical manifestations/what we see on
inspection, physical exams to do to rule in or out, differential diagnosis (top
3), tests to rule it in/tests to rule out the differentials,
treatment/referals, patient education." Then: "with the tests describe what we
would see on what we order."

WHY THIS IS NOT THE CMS CHART AGAIN. The CMS ENT comparison chart answers
"what is this disease"; it sorts on pain and hearing-loss type because that is
the axis the CMS exam turns on. An OSCE asks a different question -- "you have
this patient in front of you, what do you DO" -- so the columns here are the
station's own order: what they say, what you see, what you do with your hands,
what else it could be, what you order and what it shows, what you do about it,
what you tell them. Same 127 diseases, rotated ninety degrees.

THREE COLUMNS ARE REUSED, NOT RESTATED. Inspection findings, treatment with
referral urgency, and patient education already exist in the CMS chart rows,
audited against the decks and slide-cited. They are pulled live from
build_cms_ent_chart.ROWS rather than copied, so the two pages cannot drift.
The four OSCE-specific columns live in _pd2_ent_osce_data.OSCE. A rename on
either side fails the assertion below instead of silently dropping a disease.

NONEMERGENT FIRST, as asked -- which is the reverse of how a reference chart
would normally be ordered, and deliberate: the OSCE will nearly always be a
routine complaint, and the emergent block reads better as the "and here is what
must never be missed" tail than as a wall to scroll past first.

COLOUR. Petrol #1b4965, which is the PD2 OSCE run-sheets' own accent and is
already in the site palette -- not a new hex. The supporting shades are the
Exam 2 chart's shades rotated to that hue with saturation and lightness
untouched, which is the same recipe the three CMS charts were built on. See
[[site_design_tokens]].
"""
import os, re, sys, colorsys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

ROOT = "/Users/jaxonluke/Developer/PA_Quizzes"
DONOR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 3/cms-ent-comparison-chart.html")
OUT = os.path.join(ROOT, "Physical Diagnosis 2 Exam 1/pd2-ent-osce-chart.html")

import build_cms_ent_chart as C
from _pd2_ent_osce_data import OSCE

ACCENT = "#1b4965"

def _hls(hexs):
    r, g, b = (int(hexs[i:i+2], 16) / 255 for i in (1, 3, 5))
    return colorsys.rgb_to_hls(r, g, b)

def _rotate(hexs, hue):
    _h, l, s = _hls(hexs)
    r, g, b = colorsys.hls_to_rgb(hue, l, s)
    return "#%02x%02x%02x" % (round(r*255), round(g*255), round(b*255))

_HUE = _hls(ACCENT)[0]
# Map the donor's VIOLET shades onto petrol. Both families descend from the
# same Exam 2 originals, so pairing them by index keeps every relationship
# (panel against text, header against body) exactly as the donor tuned it.
PALETTE = [(violet, _rotate(orig, _HUE)) for orig, violet in C.PALETTE]

# One button per region. The CMS chart's 30-odd lecture groups are too many to
# scan as a filter row, and two of its group names ("Foreign body", "Neoplasm")
# are reused across lectures -- so region is resolved from the DECK, then
# overridden for the groups that sit in a deck named after somewhere else.
REGION_BY_GROUP = {
    "Thyroid": "Thyroid",
    "Vocal cord and larynx": "Throat & larynx", "Airway emergency": "Throat & larynx",
    "Pharynx": "Throat & larynx", "Deep neck infection": "Neck",
    "Neck neoplasm": "Neck",
}
REGION_BY_DECK = {
    "l15": "Ear", "l16": "Ear", "l17": "Nose & sinuses",
    "l18": "Neck", "l19": "Mouth & salivary",
}
REGION_ORDER = ["Ear", "Nose & sinuses", "Neck", "Thyroid",
                "Throat & larynx", "Mouth & salivary"]
REGION_COLOUR = {"Ear": "#2f6b6f", "Nose & sinuses": "#9c5230", "Neck": "#3f5a99",
                 "Thyroid": "#6b2340", "Throat & larynx": "#4a4f8c",
                 "Mouth & salivary": "#8c4a5f"}

def deck_key(deck):
    return ("l15" if deck.startswith("Disorders External") else
            "l17" if deck.startswith("hughie") else
            "l18" if deck.startswith("CMS I Neoplasms") else
            "l19" if deck.startswith("CMS I Disorders of the Oral") else "l16")

def region_of(group, deck):
    return REGION_BY_GROUP.get(group) or REGION_BY_DECK[deck_key(deck)]


def build_row(row):
    name, grp, _give, pres, _test, tx, urg, edu, slide, deck = row
    o = OSCE[name]
    reg = region_of(grp, deck)
    lect = C.DECKS[deck_key(deck)][0]
    ddx = "".join('<li><b>%s</b><span class="dd">%s</span></li>' % (d, why)
                  for d, why in o["ddx"])
    urg_cls = "emerg" if "EMERGENT" in urg.upper() else \
              "urg" if "URGENT" in urg.upper() else "rout"
    return ('<tr data-r="%s">'
            '<td class="nm"><b>%s</b>'
            '<span class="grp" style="background:%s">%s</span>'
            '<span class="sl">%s &middot; slide %s</span></td>'
            '<td class="says">%s</td>'
            '<td>%s</td>'
            '<td class="exam">%s</td>'
            '<td class="ddx"><ol>%s</ol></td>'
            '<td class="tst"><span class="tl in">Rules it IN</span>%s'
            '<span class="tl out">Rules the differentials OUT</span>%s</td>'
            '<td>%s<span class="u %s">%s</span></td>'
            '<td>%s</td></tr>'
            % (H.escape(reg), name, REGION_COLOUR[reg], H.escape(reg), lect, slide,
               o["says"], pres, o["exam"], ddx,
               o["rule_in"], o["rule_out"], tx, urg_cls, urg, edu))


HEADCOLS = """<colgroup>
  <col style="width:10%"><col style="width:12%"><col style="width:13%"><col style="width:13%">
  <col style="width:13%"><col style="width:16%"><col style="width:13%"><col style="width:10%">
</colgroup>
<thead><tr>
  <th>Condition</th>
  <th class="d-h">How the patient describes it<br><span class="sub">the words they actually use</span></th>
  <th>What you see on inspection</th>
  <th class="d-h">Physical exams to rule it in or out<br><span class="sub">the manoeuvres, not the findings</span></th>
  <th>Top 3 differentials<br><span class="sub">and what separates each one</span></th>
  <th>Tests &mdash; and what a positive looks like</th>
  <th>Treatment &amp; referral</th>
  <th>Patient education</th>
</tr></thead>"""


def main():
    donor = open(DONOR, encoding="utf-8").read()
    head = donor[:donor.index("</head>")]
    for old, new in PALETTE:
        head = head.replace(old, new)
    head = re.sub(r"<title>.*?</title>",
                  "<title>ENT OSCE Disease Chart &mdash; Physical Diagnosis 2</title>",
                  head, count=1, flags=re.S)

    rows = sorted(C.ROWS, key=lambda r: (REGION_ORDER.index(region_of(r[1], r[9])),
                                         r[1], r[0]))
    emerg = [r for r in rows if "EMERGENT" in r[6].upper()]
    non = [r for r in rows if "EMERGENT" not in r[6].upper()]
    assert len(emerg) + len(non) == len(C.ROWS)

    buttons = "".join('<button class="filt" data-r="%s">%s</button>'
                      % (H.escape(r), H.escape(r)) for r in REGION_ORDER)

    html = head + """</head><body>
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">
<header class="top">
  <h1>ENT OSCE Disease Chart</h1>
  <p>Physical Diagnosis 2 &middot; ENT OSCE &middot; Class of 2028</p>
  <p>__N__ conditions &mdash; __NNON__ nonemergent, __NEM__ emergent</p>
  <p style="margin-top:10px;font-size:.82rem;color:var(--c-mute)">Use the <b>Download as PDF</b> button,
  top right, to keep this offline &mdash; it prints landscape with every row intact.</p>
</header>

<div class="lede">This is the <b>run-sheet&rsquo;s companion</b>. The <a href="pd2-ent-osce.html">ENT
OSCE Run-Sheet</a> tells you the order of the station; this tells you what to do once you have a
diagnosis in mind. Same 127 diseases as the <a href="../Clinical%20Medicine%20and%20Surgery%20I%20Exam%203/cms-ent-comparison-chart.html">CMS
comparison chart</a>, turned ninety degrees: that one answers <i>what is this</i>, this one answers
<i>what do I do about it</i>.<br><br>
<b>Nonemergent is first, deliberately.</b> The station will almost always be a routine complaint,
so the rows you are most likely to need are the ones you reach without scrolling. The emergent
block sits at the bottom as the must-never-miss tail &mdash; and every row there is a diagnosis
whose whole teaching point is that it gets mistaken for something in the block above it.<br><br>
<b>Every test names its finding.</b> &ldquo;Order a computed tomography&rdquo; is worth nothing in
a station if you cannot say what makes it positive, so the tests column reads
<i>investigation &rarr; what you would see</i>, and it is split: what confirms this diagnosis, and
what would send you to one of the three differentials instead.<br><br>
<b>The differentials are the top three only.</b> Not the complete list &mdash; the three you would
actually be asked to defend, each with the single feature that separates it from the row it sits
in.<br><br>
<b>Inspection findings, treatment and patient education are pulled live from the CMS chart</b>
rather than rewritten here, so the two pages cannot drift apart. Those three columns carry their
lecture and slide citation in the first column.</div>

<div class="filters"><button class="filt on" data-r="__all__">All regions</button>__BUTTONS__</div>

<h2 class="sect nonem">Nonemergent<span class="cnt">__NNON__ conditions</span></h2>
<p class="sectnote">Routine and urgent referrals. The urgency badge in the treatment column keeps
the distinction &mdash; <span class="u urg" style="display:inline">URGENT</span> still means days,
not weeks.</p>
<div class="tblwrap"><table>__COLS__<tbody>
__NONROWS__
</tbody></table></div>

<h2 class="sect em">Emergent<span class="cnt">__NEM__ conditions</span></h2>
<p class="sectnote">These do not wait for a clinic appointment. If the station gives you one of
these, the answer to &ldquo;what is your plan&rdquo; begins with where the patient goes now, not
with which test you would order.</p>
<div class="tblwrap"><table>__COLS__<tbody>
__EMROWS__
</tbody></table></div>
</div>
<script src="../theme.js"></script>
<script>
  // One filter, applied to both tables at once, so "Ear" shows the ear rows in
  // the nonemergent block AND the ear rows in the emergent block. Section
  // headings hide when their table empties, or the page shows a heading over
  // nothing.
  var cur = '__all__';
  function apply(){
    document.querySelectorAll('.tblwrap').forEach(function(w){
      var shown = 0;
      w.querySelectorAll('tbody tr').forEach(function(tr){
        var ok = (cur === '__all__' || tr.dataset.r === cur);
        tr.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      var h = w.previousElementSibling;                 // the .sectnote
      var s = h && h.previousElementSibling;            // the .sect heading
      [w, h, s].forEach(function(el){ if (el) el.style.display = shown ? '' : 'none'; });
    });
  }
  document.querySelectorAll('.filt').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.filt').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on'); cur = b.dataset.r; apply();
    });
  });
</script>
<style>
  .filters{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 10px;}
  .filt{font:inherit;font-size:.82rem;padding:5px 12px;border-radius:999px;cursor:pointer;
        border:1px solid var(--c-line);background:var(--c-btn-bg);color:var(--c-fg);}
  .filt.on{background:var(--acc);color:#fff;border-color:var(--acc);}
  table{table-layout:fixed;}
  td, th{overflow-wrap:break-word;vertical-align:top;}
  th .sub{display:block;font-weight:400;opacity:.75;font-size:.72rem;margin-top:2px;}
  h2.sect{margin:26px 0 4px;font-size:1.08rem;letter-spacing:.01em;
          display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;}
  h2.sect::before{content:"";width:10px;height:10px;border-radius:50%;flex:none;}
  h2.sect.nonem::before{background:#3f5c46;}
  h2.sect.em::before{background:#8c1d12;}
  h2.sect .cnt{font-size:.76rem;font-weight:400;color:var(--c-mute);
               font-variant-numeric:tabular-nums;}
  p.sectnote{margin:0 0 10px;font-size:.82rem;color:var(--c-mute);max-width:62ch;line-height:1.5;}
  td.nm{white-space:normal;}
  td.nm .sl{display:block;margin-top:5px;font-size:.66rem;color:var(--c-mute);
            font-variant-numeric:tabular-nums;line-height:1.35;}
  td.nm .grp{display:block;margin-top:4px;font-size:.66rem;color:#fff;padding:1px 7px;
             border-radius:999px;width:fit-content;letter-spacing:.02em;}
  th.d-h{background:var(--c-panel);color:var(--c-panel-fg);}
  td.says{background:var(--c-panel);font-style:italic;}
  td.exam{background:var(--c-panel);}
  td.ddx ol{margin:0;padding-left:1.1em;}
  td.ddx li{margin-bottom:6px;}
  td.ddx .dd{display:block;font-size:.78rem;color:var(--c-mute);line-height:1.4;margin-top:1px;}
  td.tst .tl{display:block;font-size:.66rem;letter-spacing:.04em;text-transform:uppercase;
             font-weight:700;margin:0 0 3px;}
  td.tst .tl.in{color:var(--acc);}
  td.tst .tl.out{color:var(--c-mute);margin-top:9px;
                 border-top:1px solid var(--c-line);padding-top:7px;}
  td .u{display:block;margin-top:6px;font-weight:700;font-size:.78rem;}
  td .u.emerg{color:#8c1d12;} td .u.urg{color:#7a5a08;}
  td .u.rout{color:#3f5c46;font-weight:600;}
  .lede a{color:var(--acc);}
</style>
</body></html>"""

    html = (html.replace("__COLS__", HEADCOLS)
                .replace("__NONROWS__", "\n".join(build_row(r) for r in non))
                .replace("__EMROWS__", "\n".join(build_row(r) for r in emerg))
                .replace("__BUTTONS__", buttons)
                .replace("__NNON__", str(len(non)))
                .replace("__NEM__", str(len(emerg)))
                .replace("__N__", str(len(C.ROWS))))

    # Every condition in the source chart must reach the page exactly once.
    # Scoped to the NAME CELL: a condition legitimately appears again inside
    # other rows' differential lists, which is the point of that column.
    for r in C.ROWS:
        n = html.count('<td class="nm"><b>%s</b>' % r[0])
        assert n == 1, "row %r emitted %d times, expected once" % (r[0], n)
    for tag in ("table", "thead", "tbody", "tr", "td", "th", "div", "p", "ol", "li", "header"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert C.ACCENT not in html, "the CMS violet survived substitution"
    assert "cms-ent-chart-images" not in html, "picture cells leaked from the donor"
    assert "&amp;amp;" not in html, "a region name was escaped twice"
    # The filter matches row data-r against button data-r as the BROWSER parses
    # them, so the two must be byte-identical in the source.
    btn = set(re.findall(r'<button class="filt" data-r="([^"]+)"', html)) - {"__all__"}
    row = set(re.findall(r'<tr data-r="([^"]+)"', html))
    assert btn == row, "filter buttons %r do not match row regions %r" % (btn - row, row - btn)

    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d conditions: %d nonemergent, %d emergent, %d regions)"
          % (os.path.basename(OUT), len(html)//1024, len(C.ROWS), len(non), len(emerg),
             len(REGION_ORDER)))

if __name__ == "__main__":
    main()
