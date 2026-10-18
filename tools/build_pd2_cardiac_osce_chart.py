#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Cardiac OSCE Disease Chart for Physical Diagnosis 2.

Jaxon, 2026-10-17: "For PD cardiac Osce can you make a list (from the CMS
Cardio block 1 and 2) top 10 most common diagnoses, top 5 most non emergent,
top 5 most emergent and give everything like the ENT OSCE disease chart."

The ENT OSCE chart's twin: the same eight columns in the station's order, the
same petrol palette, the same three tiers (routine, then urgent, then emergent,
least urgent first). Two differences, both because of how this station runs:

1. THE THREE LISTS SIT AT THE TOP. Twenty rows, not 127, so the lists Jaxon
   asked for are the page's contents: each name jumps to its row. The lists do
   not overlap, so every condition has one row and one list.
2. THE FILTER IS THE CHIEF COMPLAINT, not a region. The student is handed the
   chief complaint on a form before walking in; "chest pain" should leave only
   the rows that present with chest pain.

Rows live in _pd2_cardiac_osce_data (merged from four batch modules).
"""
_REPO = __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__)))  # this checkout, never a hard-coded path
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_pd2_ent_osce_chart as ENT          # donor head and petrol palette, shared
import build_cms_ent_chart as C
from _pd2_cardiac_osce_data import ROWS, TOP10, NONEMERGENT5, EMERGENT5

OUT = os.path.join(_REPO, "Physical Diagnosis 2 Exam 1/pd2-cardiac-osce-chart.html")

LISTS = [("top10", "Top 10 most common", TOP10),
         ("nonemerg", "Top 5 non-emergent", NONEMERGENT5),
         ("emerg", "Top 5 emergent", EMERGENT5)]

# The OSCE's chief-complaint stems (the run-sheet: chest pain is the commonest,
# then palpitations, syncope, dyspnea), plus the two the peripheral vascular
# and blood pressure rows answer to.
COMPLAINTS = ["Chest pain", "Palpitations", "Syncope or dizziness", "Shortness of breath",
              "Leg pain or swelling", "High blood pressure"]
CC = {
    "Primary hypertension":        ["High blood pressure"],
    "Chronic venous insufficiency and varicose veins": ["Leg pain or swelling"],
    "Stable angina":               ["Chest pain", "Shortness of breath"],
    "Peripheral artery disease":   ["Leg pain or swelling"],
    "Atrial fibrillation":         ["Palpitations", "Shortness of breath", "Syncope or dizziness"],
    "Chronic heart failure":       ["Shortness of breath", "Leg pain or swelling"],
    "Premature ventricular contractions": ["Palpitations"],
    "Vasovagal syncope":           ["Syncope or dizziness"],
    "Deep vein thrombosis":        ["Leg pain or swelling"],
    "Aortic stenosis":             ["Shortness of breath", "Chest pain", "Syncope or dizziness"],
    "Acute pericarditis":          ["Chest pain"],
    "Mitral regurgitation":        ["Shortness of breath", "Palpitations"],
    "Mitral valve prolapse":       ["Palpitations", "Chest pain"],
    "Orthostatic hypotension":     ["Syncope or dizziness"],
    "Hypertrophic cardiomyopathy": ["Syncope or dizziness", "Chest pain", "Shortness of breath", "Palpitations"],
    "Acute coronary syndrome":     ["Chest pain", "Shortness of breath"],
    "Aortic dissection":           ["Chest pain", "High blood pressure"],
    "Cardiac tamponade":           ["Shortness of breath", "Chest pain"],
    "Ventricular tachycardia":     ["Palpitations", "Syncope or dizziness"],
    "Hypertensive emergency":      ["High blood pressure", "Chest pain", "Shortness of breath"],
}


def slug(name):
    return "c-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def list_of(name):
    for key, label, names in LISTS:
        if name in names:
            return key, label, names.index(name) + 1
    raise KeyError(name)


def cite(src):
    """The batches cite in shorthand (CMS L24, PD2); the page spells it out."""
    src = re.sub(r"\bCMS L(\d+)", r"Clinical Medicine Lecture \1", src)
    src = re.sub(r"\bCMS\b", "Clinical Medicine", src)
    return re.sub(r"\bPD2\b", "Physical Diagnosis 2", src)


_SEG = re.compile(r"(?:CMS\s+)?(?:L\d+\s+)?(?:PD2\s+(?:Cardiovascular\s+)?)?(?:supplement\s+)?"
                  r"slides?\s+\d+[a-z]?(?:\s*(?:&ndash;|,|and)\s*\d+[a-z]?)*")
_PAREN = re.compile(r"\s*\(([^()]*)\)")


def uncite(text):
    """Drop inline slide citations from a cell; the first column already lists
    every slide the row drew on, and the ENT chart's cells carry none. A
    parenthesis that was only a citation goes entirely; one that also says
    something keeps the saying ("(Levine sign, slide 28)" -> "(Levine sign)")."""
    def fix(m):
        inner = m.group(1)
        if not _SEG.search(inner):
            return m.group(0)
        rest = re.sub(r"(&[a-zA-Z][a-zA-Z0-9]*);", "\\1\x00", _SEG.sub("", inner))  # an entity's ; is not a separator
        rest = re.sub(r"^[\s;,]+|[\s;,]+$", "", rest)
        rest = re.sub(r"\s*[;,]\s*[;,]\s*", "; ", rest).replace("\x00", ";")
        return " (%s)" % rest if rest else ""
    return _PAREN.sub(fix, text)


def build_row(name):
    o = {k: (cite(uncite(v)) if isinstance(v, str) and k != "source" else v)
         for k, v in ROWS[name].items()}
    o["ddx"] = [(d, cite(uncite(w))) for d, w in o["ddx"]]
    o["source"] = cite(o["source"])
    key, label, rank = list_of(name)
    badge = "%s &middot; #%d" % (label, rank)
    ddx = "".join('<li><b>%s</b><span class="dd">%s</span></li>' % (d, why) for d, why in o["ddx"])
    u = o["urgency"].upper()
    urg_cls = "emerg" if u.startswith("EMERGENT") else "urg" if u.startswith("URGENT") else "rout"
    return ('<tr id="%s" data-c="%s">'
            '<td class="nm"><b>%s</b>'
            '<span class="grp %s">%s</span>'
            '<span class="why">%s</span>'
            '<span class="sl">%s</span></td>'
            '<td class="says">%s</td>'
            '<td>%s</td>'
            '<td class="exam">%s</td>'
            '<td class="ddx"><ol>%s</ol></td>'
            '<td class="tst"><span class="tl in">Rules it IN</span>%s'
            '<span class="tl out">Rules the differentials OUT</span>%s</td>'
            '<td>%s<span class="u %s">%s</span></td>'
            '<td>%s</td></tr>'
            % (slug(name), H.escape("|".join(CC[name])), name, key, badge, o["why"], o["source"],
               o["says"], o["findings"], o["exam"], ddx, o["rule_in"], o["rule_out"],
               o["tx"], urg_cls, o["urgency"], o["edu"]))


HEADCOLS = """<colgroup>
  <col style="width:11%"><col style="width:11%"><col style="width:13%"><col style="width:13%">
  <col style="width:13%"><col style="width:15%"><col style="width:13%"><col style="width:11%">
</colgroup>
<thead><tr>
  <th>Condition</th>
  <th class="d-h">How the patient describes it<br><span class="sub">the words they actually use</span></th>
  <th>What you see, feel and hear<br><span class="sub">inspection, palpation, auscultation, the vitals clue</span></th>
  <th class="d-h">Physical exams to rule it in or out<br><span class="sub">the maneuvers, not the findings</span></th>
  <th>Top 3 differentials<br><span class="sub">and what separates each one</span></th>
  <th>Tests &mdash; and what a positive looks like</th>
  <th>Treatment &amp; referral</th>
  <th>Patient education</th>
</tr></thead>"""


def lists_html():
    out = []
    for key, label, names in LISTS:
        lis = "".join('<li><a href="#%s"><span class="dot %s"></span>%s</a></li>'
                      % (slug(n), ROWS[n]["tier"], n) for n in names)
        out.append('<div class="lcard %s"><h3>%s</h3><ol>%s</ol></div>' % (key, label, lis))
    return '<div class="lists">%s</div>' % "".join(out)


def main():
    names = TOP10 + NONEMERGENT5 + EMERGENT5
    assert len(names) == len(set(names)) == 20, "the three lists must be disjoint, 20 names"
    missing = [n for n in names if n not in ROWS]
    assert not missing, "no row written for %r" % missing
    extra = set(ROWS) - set(names)
    assert not extra, "rows not on any list: %r" % extra
    assert set(CC) == set(names), "chief-complaint map out of step: %r" % (set(CC) ^ set(names))
    assert all(c in COMPLAINTS for v in CC.values() for c in v)
    assert all(ROWS[n]["tier"] == "emergent" for n in EMERGENT5), "an emergent-list row is not tiered emergent"
    assert all(ROWS[n]["tier"] != "emergent" for n in TOP10 + NONEMERGENT5), \
        "a non-emergent-list row is tiered emergent"
    for n in names:
        u = ROWS[n]["urgency"].upper()
        assert u.startswith({"routine": "ROUTINE", "urgent": "URGENT", "emergent": "EMERGENT"}[ROWS[n]["tier"]]), \
            "%s: urgency line disagrees with its tier" % n

    donor = open(ENT.DONOR, encoding="utf-8").read()
    head = donor[:donor.index("</head>")]
    for old, new in ENT.PALETTE:
        head = head.replace(old, new)
    head = re.sub(r"<title>.*?</title>",
                  "<title>Cardiac OSCE Disease Chart &mdash; Physical Diagnosis 2</title>",
                  head, count=1, flags=re.S)

    TIERS = ["routine", "urgent", "emergent"]
    by_tier = {t: [n for n in names if ROWS[n]["tier"] == t] for t in TIERS}
    assert all(by_tier[t] for t in TIERS), "a tier came out empty"

    buttons = "".join('<button class="filt" data-c="%s">%s</button>' % (H.escape(c), H.escape(c))
                      for c in COMPLAINTS)

    html = head + """</head><body>
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">
<header class="top">
  <h1>Cardiac OSCE Disease Chart</h1>
  <p>Physical Diagnosis 2 &middot; Cardiac OSCE, Wednesday 21 October &middot; Class of 2028</p>
  <p>__N__ conditions &mdash; __NROUT__ routine, __NURG__ urgent, __NEM__ emergent</p>
  <p style="margin-top:10px;font-size:.82rem;color:var(--c-mute)">Use the <b>Download as PDF</b> button,
  top right, to keep this offline &mdash; it prints landscape with every row intact.</p>
</header>

<div class="lede">The <a href="pd2-cardiac-osce.html">Cardiac OSCE Run-Sheet</a> tells you the
order of the station; this tells you what to do once you have a diagnosis in mind. Every condition
comes from the two Clinical Medicine and Surgery I cardiology blocks (Exam 4, Lectures 20&ndash;25,
and Exam 5, Lectures 26&ndash;32), with the examination technique from the Physical Diagnosis 2
cardiovascular lecture. Each row cites its lecture and slides in the first column.<br><br>
<b>Three lists, twenty conditions, no repeats.</b> The ten most common cardiology diagnoses, then
five more that are managed in clinic, then the five emergencies that must never be missed.<br><br>
<b>Filter by the chief complaint</b> on the form you are handed before you walk in. Chest pain
leaves only the rows that present with chest pain.<br><br>
<b>Ordered least urgent first</b>, like the ENT chart: <span class="tierkey"><span class="dot routine"></span>Routine</span>,
then <span class="tierkey"><span class="dot urgent"></span>Urgent</span> (days, not weeks), then
<span class="tierkey"><span class="dot emergent"></span>Emergent</span>, where the plan begins with
where the patient goes now. <b>Every test names its finding</b>, and the tests column is split into
what confirms this diagnosis and what would send you to one of its three differentials.</div>

__LISTS__

<div class="filters"><button class="filt on" data-c="__all__">All complaints</button>__BUTTONS__</div>

<h2 class="sect routine">Routine<span class="cnt">__NROUT__ conditions</span></h2>
<p class="sectnote">Managed in clinic, on a normal timescale. The station is most likely to be one
of these, so this is the block to know cold.</p>
<div class="tblwrap"><table>__COLS__<tbody>
__ROUTROWS__
</tbody></table></div>

<h2 class="sect urgent">Urgent<span class="cnt">__NURG__ conditions</span></h2>
<p class="sectnote">Still outside the emergency department, but measured in <b>days, not
weeks</b>, or treated the same day. The commonest way to get one of these wrong is to manage it
correctly and too slowly.</p>
<div class="tblwrap"><table>__COLS__<tbody>
__URGROWS__
</tbody></table></div>

<h2 class="sect emergent">Emergent<span class="cnt">__NEM__ conditions</span></h2>
<p class="sectnote">These do not wait for a clinic appointment. If the station gives you one of
these, the answer to &ldquo;what is your plan&rdquo; begins with where the patient goes now, not
with which test you would order.</p>
<div class="tblwrap"><table>__COLS__<tbody>
__EMROWS__
</tbody></table></div>
</div>
<script src="../theme.js"></script>
<script>
  // One filter across all three tables. A row carries every chief complaint it
  // presents with (data-c, "|"-separated). Section headings hide when their
  // table empties, or the page shows a heading over nothing.
  var cur = '__all__';
  function apply(){
    document.querySelectorAll('.tblwrap').forEach(function(w){
      var shown = 0;
      w.querySelectorAll('tbody tr').forEach(function(tr){
        var ok = (cur === '__all__' || tr.dataset.c.split('|').indexOf(cur) !== -1);
        tr.style.display = ok ? '' : 'none';
        if (ok) shown++;
      });
      var h = w.previousElementSibling;
      var s = h && h.previousElementSibling;
      [w, h, s].forEach(function(el){ if (el) el.style.display = shown ? '' : 'none'; });
    });
  }
  function pick(c){
    cur = c;
    document.querySelectorAll('.filt').forEach(function(x){ x.classList.toggle('on', x.dataset.c === c); });
    apply();
  }
  document.querySelectorAll('.filt').forEach(function(b){
    b.addEventListener('click', function(){ pick(b.dataset.c); });
  });
  // A list link must land on a visible row, so it clears the filter first.
  document.querySelectorAll('.lists a').forEach(function(a){
    a.addEventListener('click', function(){ if (cur !== '__all__') pick('__all__'); });
  });
</script>
<style>
  .lists{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px;margin:16px 0 6px;}
  @media (max-width:760px){.lists{grid-template-columns:1fr;}}
  .lcard{border:1px solid var(--c-line);border-radius:12px;padding:12px 14px;background:var(--c-btn-bg);}
  .lcard h3{margin:0 0 8px;font-size:.92rem;letter-spacing:.01em;}
  .lcard.emerg h3{color:#8c1d12;}
  .lcard ol{margin:0;padding-left:1.4em;font-size:.86rem;line-height:1.6;}
  .lcard a{color:var(--c-fg);text-decoration:none;border-bottom:1px dotted var(--c-mute);}
  .lcard a:hover{color:var(--acc);border-bottom-color:var(--acc);}
  .lcard .dot{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:6px;
              vertical-align:middle;}
  .dot.routine{background:#3f5c46;} .dot.urgent{background:#7a5a08;} .dot.emergent{background:#8c1d12;}
  .filters{display:flex;flex-wrap:wrap;gap:6px;margin:14px 0 10px;}
  .filt{font:inherit;font-size:.82rem;padding:5px 12px;border-radius:999px;cursor:pointer;
        border:1px solid var(--c-line);background:var(--c-btn-bg);color:var(--c-fg);}
  .filt.on{background:var(--acc);color:#fff;border-color:var(--acc);}
  table{table-layout:fixed;}
  td, th{overflow-wrap:break-word;vertical-align:top;}
  th .sub{display:block;font-weight:400;opacity:.75;font-size:.72rem;margin-top:2px;}
  tr{scroll-margin-top:70px;}
  tr:target td{box-shadow:inset 0 2px 0 var(--acc);}
  h2.sect{margin:26px 0 4px;font-size:1.08rem;letter-spacing:.01em;
          display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;}
  h2.sect::before{content:"";width:10px;height:10px;border-radius:50%;flex:none;}
  h2.sect.routine::before{background:#3f5c46;}
  h2.sect.urgent::before{background:#7a5a08;}
  h2.sect.emergent::before{background:#8c1d12;}
  .tierkey{white-space:nowrap;font-weight:700;}
  .tierkey .dot{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:4px;}
  h2.sect .cnt{font-size:.76rem;font-weight:400;color:var(--c-mute);
               font-variant-numeric:tabular-nums;}
  p.sectnote{margin:0 0 10px;font-size:.82rem;color:var(--c-mute);max-width:62ch;line-height:1.5;}
  td.nm{white-space:normal;}
  td.nm .why{display:block;margin-top:6px;font-size:.74rem;line-height:1.4;}
  td.nm .sl{display:block;margin-top:5px;font-size:.66rem;color:var(--c-mute);
            font-variant-numeric:tabular-nums;line-height:1.35;}
  td.nm .grp{display:block;margin-top:4px;font-size:.66rem;color:#fff;padding:1px 7px;
             border-radius:999px;width:fit-content;letter-spacing:.02em;}
  td.nm .grp.top10{background:#2f6b6f;} td.nm .grp.nonemerg{background:#3f5a99;}
  td.nm .grp.emerg{background:#8c1d12;}
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
                .replace("__LISTS__", lists_html())
                .replace("__ROUTROWS__", "\n".join(build_row(n) for n in by_tier["routine"]))
                .replace("__URGROWS__", "\n".join(build_row(n) for n in by_tier["urgent"]))
                .replace("__EMROWS__", "\n".join(build_row(n) for n in by_tier["emergent"]))
                .replace("__BUTTONS__", buttons)
                .replace("__NROUT__", str(len(by_tier["routine"])))
                .replace("__NURG__", str(len(by_tier["urgent"])))
                .replace("__NEM__", str(len(by_tier["emergent"])))
                .replace("__N__", str(len(names))))

    for n in names:
        c = html.count('<td class="nm"><b>%s</b>' % n)
        assert c == 1, "row %r emitted %d times, expected once" % (n, c)
        assert html.count('href="#%s"' % slug(n)) == 1, "list link for %r missing" % n
    for tag in ("table", "thead", "tbody", "tr", "td", "th", "div", "p", "ol", "li", "header", "h3", "b", "i"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert C.ACCENT not in html, "the CMS violet survived substitution"
    assert "cms-ent-chart-images" not in html, "picture cells leaked from the donor"
    assert "&amp;amp;" not in html, "a label was escaped twice"
    body = re.sub(r"<script.*?</script>", "", html.split("<body>", 1)[1], flags=re.S)
    bare = re.findall(r"&(?![a-zA-Z][a-zA-Z0-9]*;|#\d+;)", body)
    assert not bare, "a bare ampersand in the body: %d" % len(bare)
    btn = set(re.findall(r'<button class="filt" data-c="([^"]+)"', html)) - {"__all__"}
    row = {c for v in re.findall(r'<tr id="[^"]+" data-c="([^"]+)"', html) for c in v.split("|")}
    assert btn == row, "filter buttons %r do not match row complaints %r" % (btn - row, row - btn)

    import dark_tokens
    html = dark_tokens.apply(html, "chart")
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d conditions: %d routine, %d urgent, %d emergent)"
          % (os.path.basename(OUT), len(html)//1024, len(names),
             len(by_tier["routine"]), len(by_tier["urgent"]), len(by_tier["emergent"])))


if __name__ == "__main__":
    main()
