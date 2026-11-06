#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Pulmonary OSCE Disease Chart for Physical Diagnosis 2.

Jaxon, 2026-11-06: a pulmonary version of the Cardiac OSCE Disease Chart for the
Pulmonary OSCE (Tuesday 10 November): the top 10 most common diagnoses, the top 5
non-emergent and the top 5 emergent, from the two Clinical Medicine and Surgery I
pulmonary blocks (Exam 6, Lectures 33-38; Exam 7, Lectures 39-44).

The Cardiac OSCE chart's twin (tools/build_pd2_cardiac_osce_chart.py): the same
eight columns, the same petrol palette, the three lists at the top, the three
tiers least urgent first, the chief-complaint filter, the Tell-tale sign box and
Typical age line under each name, and the column names kept in view.

Where the cardiac chart puts a 12-lead under each row, this one puts the row's
TESTS under it (Jaxon: "If it calls for anthing like Xray, ekg or whatever
include it like you did for the cardiac one and explain it"): chest films, CT,
spirometry, electrocardiograms, and the criteria tables a slide gives instead of
a picture. Same full-width second row, same chief complaints on it, so the filter
keeps the pair together. Pictures, captions and box coordinates live in
_pd2_pulm_osce_images; the boxes are drawn into the pixels by
tools/box_pd2_pulm_osce_images.py.

Rows live in _pd2_pulm_osce_data (merged from five batch modules).
"""
_REPO = __import__("os").path.dirname(__import__("os").path.dirname(__import__("os").path.abspath(__file__)))  # this checkout, never a hard-coded path
import os, re, sys, html as H
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import build_pd2_ent_osce_chart as ENT          # donor head and petrol palette, shared
import build_cms_ent_chart as C
import _pd2_pulm_osce_images as IM
from _pd2_pulm_osce_data import ROWS, TOP10, NONEMERGENT5, EMERGENT5
from _pd2_pulm_osce_images import IMAGES, PICS, NOPIC
from _pd2_pulm_osce_ages import AGES
from _pd2_pulm_osce_telltale import TELLTALE

OUT = os.path.join(_REPO, "Physical Diagnosis 2 Exam 2/pd2-pulm-osce-chart.html")
IMG_DIR = "pd2-pulm-osce-images"
MAX_PICS = 2          # the same cap for every row

LISTS = [("top10", "Top 10 most common", TOP10),
         ("nonemerg", "Top 5 non-emergent", NONEMERGENT5),
         ("emerg", "Top 5 emergent", EMERGENT5)]

# The deck each picture comes from, as the credit line names it.
DECK_LABEL = {
    IM.L35: "Clinical Medicine Lecture 35", IM.L36: "Clinical Medicine Lecture 36",
    IM.L37: "Clinical Medicine Lecture 37", IM.L38: "Clinical Medicine Lecture 38",
    IM.L40: "Clinical Medicine Lecture 40", IM.L41: "Clinical Medicine Lecture 41",
    IM.L43: "Clinical Medicine Lecture 43", IM.L44: "Clinical Medicine Lecture 44",
    IM.PDM14: "Principles of Diagnostic Medicine Lecture 14",
    IM.PDM16: "Principles of Diagnostic Medicine Lecture 16",
    IM.PDM17: "Principles of Diagnostic Medicine Lecture 17",
}

# The chief complaints a pulmonary form hands you (the run-sheet's history opens on cough and dyspnea).
COMPLAINTS = ["Cough", "Shortness of breath", "Wheezing", "Chest pain", "Fever", "Hemoptysis",
              "Weight loss", "Snoring or daytime sleepiness"]
CC = {
    "Obstructive sleep apnea":              ["Snoring or daytime sleepiness"],
    "Influenza":                            ["Fever", "Cough"],
    "Asthma":                               ["Wheezing", "Shortness of breath", "Cough"],
    "Chronic obstructive pulmonary disease": ["Shortness of breath", "Cough", "Wheezing"],
    "Acute bronchitis":                     ["Cough", "Wheezing"],
    "Pulmonary hypertension and cor pulmonale": ["Shortness of breath"],
    "Pleural effusion":                     ["Shortness of breath", "Chest pain", "Cough"],
    "Community-acquired pneumonia":         ["Fever", "Cough", "Shortness of breath", "Chest pain"],
    "Lung cancer":                          ["Cough", "Hemoptysis", "Weight loss"],
    "Idiopathic pulmonary fibrosis":        ["Shortness of breath", "Cough"],
    "Pleurisy":                             ["Chest pain"],
    "Obesity hypoventilation syndrome":     ["Snoring or daytime sleepiness", "Shortness of breath"],
    "Pulmonary tuberculosis":               ["Cough", "Fever", "Hemoptysis", "Weight loss"],
    "Sarcoidosis":                          ["Cough", "Shortness of breath", "Weight loss"],
    "Hypersensitivity pneumonitis":         ["Shortness of breath", "Cough", "Fever"],
    "Acute cardiogenic pulmonary edema":    ["Shortness of breath", "Cough"],
    "Pulmonary embolism":                   ["Shortness of breath", "Chest pain", "Hemoptysis"],
    "Acute respiratory distress syndrome":  ["Shortness of breath"],
    "Pneumothorax":                         ["Chest pain", "Shortness of breath"],
    "Hemothorax":                           ["Chest pain", "Shortness of breath"],
}


def slug(name):
    return "c-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def list_of(name):
    for key, label, names in LISTS:
        if name in names:
            return key, label, names.index(name) + 1
    raise KeyError(name)


def cite(src):
    """The batches cite in shorthand (CMS L37, PD2 Thorax, PDM Imaging); the page spells it out."""
    src = re.sub(r"\bCMS L(\d+)", r"Clinical Medicine Lecture \1", src)
    src = re.sub(r"\bCMS\b", "Clinical Medicine", src)
    src = re.sub(r"\bPD2\b", "Physical Diagnosis 2", src)
    src = re.sub(r"\bPDM Imaging\b", "Principles of Diagnostic Medicine Lecture 17", src)
    src = re.sub(r"\bPDM (\d+)\b", r"Principles of Diagnostic Medicine Lecture \1", src)
    src = re.sub(r"\bPDM PFT\b", "Principles of Diagnostic Medicine pulmonary function testing", src)
    src = re.sub(r"\bPDM ABG\b", "Principles of Diagnostic Medicine blood gas", src)
    src = re.sub(r"(Lecture \d+) (slides? \d)", r"\1, \2", src)
    return re.sub(r"(slides? \d+)-(\d+)", "\\1&ndash;\\2", src)


_DECK = r"(?:CMS\s+L\d+\s+|CMS\s+|PD2\s+Thorax\s+|PD2\s+|PDM\s+(?:\d+|Imaging|PFT|ABG)\s+)?"
_SEG = re.compile(_DECK + r"slides?\s+\d+[a-z]?(?:\s*(?:&ndash;|-|,|and)\s*\d+[a-z]?)*")
_SAYS = re.compile(r"PD2\s+Thorax\s+slides?\s+[\d,\s]+(?:&ndash;\d+)?\s*says\b")
_PAREN = re.compile(r"\s*\(([^()]*)\)")


def uncite(text):
    """Drop inline slide citations from a cell; the first column already lists
    every slide the row drew on. A parenthesis that was only a citation goes
    entirely; one that also says something keeps the saying ("(coarse, PD2
    Thorax slide 47)" -> "(coarse)"). A note that another deck disagrees keeps
    the deck's name ("(the Physical Diagnosis 2 thorax lecture says ...)")."""
    def fix(m):
        inner = m.group(1)
        if _SAYS.search(inner):
            return " (%s)" % _SAYS.sub("the Physical Diagnosis 2 thorax lecture says", inner)
        if not _SEG.search(inner):
            return m.group(0)
        rest = re.sub(r"(&[a-zA-Z][a-zA-Z0-9]*);", "\\1\x00", _SEG.sub("", inner))  # an entity's ; is not a separator
        rest = re.sub(r"^[\s;,]+|[\s;,]+$", "", rest)
        rest = re.sub(r"\s*[;,]\s*[;,]\s*", "; ", rest).replace("\x00", ";")
        return " (%s)" % rest if rest else ""
    return _PAREN.sub(fix, text)


def age_line(name):
    """The 'Typical age' line under the condition name. A textbook age (used only
    where no deck gives one) is labeled so it is never read as course content."""
    slides, cite_, book = AGES[name]
    parts = []
    if slides:
        parts.append('%s <span class="asrc">%s</span>' % (slides, cite(cite_)))
    if book:
        parts.append('<span class="bk"><span class="ext">Textbook, not on the slides:</span> %s</span>' % book)
    return '<span class="age"><b>Typical age</b> %s</span>' % ' '.join(parts)


def telltale_line(name):
    """The 'Tell-tale sign' box under the condition name: the clue that makes it the most likely diagnosis."""
    sign, cite_ = TELLTALE[name]
    return '<span class="tt"><b>Tell-tale sign</b>%s <span class="asrc">%s</span></span>' % (sign, cite(cite_))


CELLS = ("why", "says", "findings", "exam", "rule_in", "rule_out", "tx", "urgency", "edu")


def shown(name):
    """The row's display text: inline cites stripped, shorthand spelled out."""
    o = {k: (cite(uncite(v)) if isinstance(v, str) and k != "source" else v)
         for k, v in ROWS[name].items()}
    o["ddx"] = [(d, cite(uncite(w))) for d, w in o["ddx"]]
    o["source"] = cite(o["source"])
    return o


def words(s):
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"&[a-zA-Z]+;|&#\d+;", " ", s)
    return len(re.findall(r"[A-Za-z0-9][\w'%./-]*", s))


def build_row(name):
    o = shown(name)
    key, label, rank = list_of(name)
    badge = "%s &middot; #%d" % (label, rank)
    age = telltale_line(name) + age_line(name)
    ddx = "".join('<li><b>%s</b><span class="dd">%s</span></li>' % (d, why) for d, why in o["ddx"])
    u = o["urgency"].upper()
    urg_cls = "emerg" if u.startswith("EMERGENT") else "urg" if u.startswith("URGENT") else "rout"
    return ('<tr id="%s" data-c="%s">'
            '<td class="nm"><b>%s</b>'
            '<span class="grp %s">%s</span>%s'
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
            % (slug(name), H.escape("|".join(CC[name])), name, key, badge, age, o["why"], o["source"],
               o["says"], o["findings"], o["exam"], ddx, o["rule_in"], o["rule_out"],
               o["tx"], urg_cls, o["urgency"], o["edu"])) + pics_row(name)


def _a(href, text):
    return '<a href="%s" target="_blank" rel="noopener">%s</a>' % (H.escape(href), text)


def caption(text):
    """Caption text is written in real characters; escape it, then spell the cites out."""
    return cite(H.escape(text, quote=False))


def credit(fn):
    src, boxes = IMAGES[fn]
    if src["kind"] == "deck":
        bits = ["Source: %s, slide %d (%s)" % (DECK_LABEL[src["deck"]], src["slide"], H.escape(src["deck"]))]
        if src["changed"]:
            bits.append(H.escape(src["changed"], quote=False))
        if boxes:
            bits.append("yellow boxes added")
        return "; ".join(bits)
    assert src["lic"] and src["author"] and src["page"], "%s: Commons credit incomplete" % fn
    lic = _a(src["licurl"], src["lic"]) if src["licurl"] else src["lic"]
    changed = ", ".join(x for x in (src["changed"], "yellow boxes added" if boxes else "") if x)
    return "Image: %s, %s, %s%s" % (H.escape(src["author"]), _a(src["page"], "Wikimedia Commons"), lic,
                                    "; " + changed if changed else "")


def figure(name, p):
    head = ('<span class="et">%s</span><b>%s</b><span class="es">%s</span>'
            % (caption(p["test"]), caption(p["title"]), caption(p["shows"])))
    if "file" in p:
        fn = p["file"]
        _, boxes = IMAGES[fn]
        assert os.path.exists(os.path.join(os.path.dirname(OUT), IMG_DIR, fn)), \
            "missing picture %s (run tools/box_pd2_pulm_osce_images.py)" % fn
        assert p["boxed"].startswith("Yellow box" if boxes else "Nothing is boxed"), \
            "%s: the caption's box line disagrees with the picture's %d boxes" % (fn, len(boxes))
        alt = "%s for %s: %s" % (p["test"], name.lower(), p["title"])
        return ('<figure class="tp"><img src="%s/%s" loading="lazy" alt="%s">'
                '<figcaption>%s<span class="eb%s">%s</span><span class="ec">%s</span></figcaption></figure>'
                % (IMG_DIR, fn, H.escape(alt, quote=False).replace('"', "&quot;"), head, "" if boxes else " none", caption(p["boxed"]), credit(fn)))
    t = p["table"]
    assert p["boxed"].startswith("Highlighted" if t["hl"] else "Nothing is highlighted"), \
        "%s: the table's highlight line disagrees with its %d highlighted rows" % (name, len(t["hl"]))
    cols = len(t["head"])
    assert all(len(r) == cols for r in t["rows"]), "%s: a table row has the wrong number of cells" % name
    rows = ['<div class="cr ch" role="row">%s</div>'
            % "".join('<span role="columnheader">%s</span>' % caption(c) for c in t["head"])]
    for i, r in enumerate(t["rows"]):
        rows.append('<div class="cr%s" role="row">%s</div>'
                    % (" hl" if i in t["hl"] else "", "".join('<span role="cell">%s</span>' % caption(c) for c in r)))
    return ('<figure class="tp tb"><div class="crit" role="table" aria-label="%s">%s</div>'
            '<figcaption>%s<span class="eb%s">%s</span><span class="ec">Source: %s, typed from the slides</span>'
            '</figcaption></figure>'
            % (H.escape(p["title"], quote=False).replace('"', "&quot;"), "".join(rows), head, "" if t["hl"] else " none", caption(p["boxed"]),
               cite(H.escape(p["cite"], quote=False))))


def pics_row(name):
    """The row's tests, pictured, full width under it. Same data-c as the row, so
    the chief-complaint filter hides and shows the pair together."""
    ps = PICS[name]
    figs = "".join(figure(name, p) for p in ps)
    note = NOPIC.get(name)
    return ('\n<tr class="img" id="%s-img" data-c="%s"><td colspan="8"><div class="pin">'
            '<p class="ih"><span class="en">%s</span><span class="it">the tests, pictured</span></p>'
            '%s%s</div></td></tr>'
            % (slug(name), H.escape("|".join(CC[name])), H.escape(name, quote=False),
               '<div class="figs%s">%s</div>' % (" one" if len(ps) == 1 else "", figs) if ps else "",
               '<p class="nopic"><b>Not pictured</b>%s</p>' % caption(note) if note else ""))


HEADCOLS = """<colgroup>
  <col style="width:11%"><col style="width:11%"><col style="width:13%"><col style="width:13%">
  <col style="width:13%"><col style="width:15%"><col style="width:13%"><col style="width:11%">
</colgroup>
<thead><tr>
  <th>Condition</th>
  <th class="d-h">How the patient describes it<br><span class="sub">the words they actually use</span></th>
  <th>What you see, feel and hear<br><span class="sub">inspection, palpation, percussion, auscultation, the vitals clue</span></th>
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


def depth_report(names):
    """Equal depth: every row's visible words, by column, so a row that runs long or short shows."""
    print("%-42s %5s %5s %5s %5s %5s %5s %5s %5s %5s %5s %6s" %
          ("row", "why", "says", "find", "exam", "ddx", "in", "out", "tx", "urg", "edu", "total"))
    totals = []
    for n in names:
        o = shown(n)
        w = [words(o[k]) for k in ("why", "says", "findings", "exam")]
        w.append(sum(words(d) + words(x) for d, x in o["ddx"]))
        w += [words(o[k]) for k in ("rule_in", "rule_out", "tx", "urgency", "edu")]
        totals.append(sum(w))
        print("%-42s %5d %5d %5d %5d %5d %5d %5d %5d %5d %5d %6d" % ((n[:42],) + tuple(w) + (sum(w),)))
    print("total words per row: min %d, max %d, mean %d" % (min(totals), max(totals), sum(totals) / len(totals)))


def main():
    names = TOP10 + NONEMERGENT5 + EMERGENT5
    assert len(names) == len(set(names)) == 20, "the three lists must be disjoint, 20 names"
    missing = [n for n in names if n not in ROWS]
    assert not missing, "no row written for %r" % missing
    extra = set(ROWS) - set(names)
    assert not extra, "rows not on any list: %r" % extra
    for what, d in (("tell-tale signs", TELLTALE), ("ages", AGES), ("chief-complaint map", CC), ("pictures", PICS)):
        assert set(d) == set(names), "%s out of step: %r" % (what, set(d) ^ set(names))
    assert set(NOPIC) <= set(names), "a not-pictured note for a row not on the chart"
    assert all(c in COMPLAINTS for v in CC.values() for c in v)
    assert all(ROWS[n]["tier"] == "emergent" for n in EMERGENT5), "an emergent-list row is not tiered emergent"
    assert all(ROWS[n]["tier"] != "emergent" for n in TOP10 + NONEMERGENT5), \
        "a non-emergent-list row is tiered emergent"
    for n in names:
        u = ROWS[n]["urgency"].upper()
        assert u.startswith({"routine": "ROUTINE", "urgent": "URGENT", "emergent": "EMERGENT"}[ROWS[n]["tier"]]), \
            "%s: urgency line disagrees with its tier" % n
        assert len(PICS[n]) <= MAX_PICS, "%s: more than %d pictures" % (n, MAX_PICS)
        assert PICS[n] or NOPIC.get(n), "%s: no picture and no line saying why" % n
    used = [p["file"] for ps in PICS.values() for p in ps if "file" in p]
    assert sorted(used) == sorted(IMAGES), "pictures without a row, or rows without a picture"

    donor = open(ENT.DONOR, encoding="utf-8").read()
    head = donor[:donor.index("</head>")]
    for old, new in ENT.PALETTE:
        head = head.replace(old, new)
    head = re.sub(r"<title>.*?</title>",
                  "<title>Pulmonary OSCE Disease Chart &mdash; Physical Diagnosis 2</title>",
                  head, count=1, flags=re.S)
    # The Word button's link: this page's own copy (tools/build_guide_docx.py writes it), not the donor's.
    assert head.count('href="cms-ent-comparison-chart.docx"') == 1, "the donor's Word link moved"
    head = head.replace('href="cms-ent-comparison-chart.docx"',
                        'href="%s"' % os.path.basename(OUT).replace(".html", ".docx"))

    TIERS = ["routine", "urgent", "emergent"]
    by_tier = {t: [n for n in names if ROWS[n]["tier"] == t] for t in TIERS}
    assert all(by_tier[t] for t in TIERS), "a tier came out empty"

    buttons = "".join('<button class="filt" data-c="%s">%s</button>' % (H.escape(c), H.escape(c))
                      for c in COMPLAINTS)
    npics = len(used) + sum(1 for ps in PICS.values() for p in ps if "table" in p)

    html = head + """</head><body>
<div class="guide-back-bar">
  <a href="#" class="guide-back-link" onclick="event.preventDefault(); window.guideGoBack();">&larr; Back</a>
</div>
<div class="wrap">
<header class="top">
  <h1>Pulmonary OSCE Disease Chart</h1>
  <p>Physical Diagnosis 2 &middot; Pulmonary OSCE, Tuesday 10 November &middot; Class of 2028</p>
  <p>__N__ conditions &mdash; __NROUT__ routine, __NURG__ urgent, __NEM__ emergent</p>
  <p style="margin-top:10px;font-size:.82rem;color:var(--c-mute)">Use the <b>Download as PDF</b> button,
  top right, to keep this offline &mdash; it prints landscape with every row intact.</p>
</header>

<div class="lede">The <a href="../Physical%20Diagnosis%202%20Exam%201/pd2-pulmonary-osce.html">Pulmonary OSCE
Run-Sheet</a> tells you the order of the station; this tells you what to do once you have a diagnosis in
mind. Every condition comes from the two Clinical Medicine and Surgery I pulmonary blocks (Exam 6,
Lectures 33&ndash;38, and Exam 7, Lectures 39&ndash;44), with the examination technique &mdash; inspection,
palpation with tactile fremitus and chest expansion, percussion, auscultation and the transmitted voice
sounds &mdash; from the Physical Diagnosis 2 thorax lecture (<a href="pd2-exam-2-study-guide.html#thorax">study
guide, section 2</a>). Each row cites its lecture and slides in the first column. Where no slide gives a
finding for a condition, the row says so rather than filling it in.<br><br>
<b>Under each condition&rsquo;s name, a yellow <i>Tell-tale sign</i> box gives the one clue that makes it the most
likely diagnosis</b>, with its slides.<br><br>
<b>Under each row, its tests are pictured</b>: chest films, CT (computed tomography) scans, spirometry,
electrocardiograms, and the criteria tables a slide gives instead of a picture, __NPICS__ in all. Each picture
is labeled as that finding by its source: a slide from the Clinical Medicine and Surgery I or Principles of
Diagnostic Medicine I decks, or, for one chest film, a Wikimedia Commons file whose description names it.
<b>Yellow boxes mark where the finding shows</b>, and the line under each caption says what is boxed. A test
with no picture on the slides is listed as not pictured. The credit sits under each picture; click a picture to
enlarge it.<br><br>
<b>Three lists, twenty conditions, no repeats.</b> The ten most common pulmonary diagnoses, then five more
that are managed in clinic, then five emergencies that must never be missed. Each list runs from the most
common condition to the least common, as the slides&rsquo; figures and wording have it.<br><br>
<b>Filter by the chief complaint</b> on the form you are handed before you walk in. Shortness of breath
leaves only the rows that present with it.<br><br>
<b>Ordered least urgent first</b>, like the cardiac chart: <span class="tierkey"><span class="dot routine"></span>Routine</span>,
then <span class="tierkey"><span class="dot urgent"></span>Urgent</span> (days, not weeks), then
<span class="tierkey"><span class="dot emergent"></span>Emergent</span>, where the plan begins with
where the patient goes now. <b>Every test names its finding</b>, and the tests column is split into
what confirms this diagnosis and what would send you to one of its three differentials.</div>

__LISTS__

<div class="filters"><button class="filt on" data-c="__all__">All complaints</button>__BUTTONS__</div>

<h2 class="sect routine">Routine<span class="cnt">__NROUT__ conditions</span></h2>
<p class="sectnote">Managed in clinic, on a normal timescale.</p>
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
      w.querySelectorAll('tbody > tr[data-c]').forEach(function(tr){
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

  // The column names stay in view, as on the cardiac chart. Wide screens: the header row is sticky just under
  // the guide back bar (its height is measured into --barH). Narrow screens (<= 900px, where theme.css makes
  // each table swipe sideways): a sticky header inside a sideways scroller sticks to that box, not the screen,
  // so a copy of the header row rides fixed under the bar while its table is on screen, follows the table's
  // sideways scroll, and keeps the first column pinned like the rows.
  (function(){
    var bar = document.querySelector('.guide-back-bar');
    var narrow = window.matchMedia('screen and (max-width:900px)');
    var wraps = Array.prototype.slice.call(document.querySelectorAll('.tblwrap'));
    var fl = document.createElement('div'); fl.className = 'thfloat'; fl.setAttribute('aria-hidden', 'true');
    document.body.appendChild(fl);
    var on = null, copy = null, first = null;
    function barBottom(){ return bar ? Math.max(0, bar.getBoundingClientRect().bottom) : 0; }
    function setBar(){ document.documentElement.style.setProperty('--barH', (bar ? bar.offsetHeight : 0) + 'px'); }
    function build(w){
      var t = w.querySelector('table'), src = t.querySelectorAll('thead th');
      copy = document.createElement('table');
      copy.appendChild(t.querySelector('thead').cloneNode(true));
      copy.style.width = t.offsetWidth + 'px';
      Array.prototype.forEach.call(copy.querySelectorAll('th'), function(th, i){
        th.style.width = src[i].offsetWidth + 'px'; th.style.boxSizing = 'border-box';
      });
      first = copy.querySelector('th');
      fl.innerHTML = ''; fl.appendChild(copy); on = w;
    }
    function update(){
      if (!narrow.matches){ fl.style.display = 'none'; on = null; return; }
      var top = barBottom(), hit = null;
      wraps.forEach(function(w){
        if (!w.offsetParent) return;                    // a table the filter emptied
        var head = w.querySelector('thead').getBoundingClientRect(), r = w.getBoundingClientRect();
        if (head.top < top && r.bottom > top + head.height) hit = w;
      });
      if (!hit){ fl.style.display = 'none'; return; }
      if (hit !== on) build(hit);
      var r = hit.getBoundingClientRect(), x = hit.scrollLeft;
      fl.style.display = 'block'; fl.style.top = top + 'px';
      fl.style.left = (r.left + hit.clientLeft) + 'px'; fl.style.width = hit.clientWidth + 'px';
      copy.style.transform = 'translateX(' + (-x) + 'px)';
      if (first) first.style.transform = 'translateX(' + x + 'px)';
    }
    setBar();
    window.addEventListener('scroll', update, {passive: true});
    window.addEventListener('resize', function(){ setBar(); on = null; update(); });
    wraps.forEach(function(w){ w.addEventListener('scroll', update, {passive: true}); });
    document.querySelectorAll('.filt').forEach(function(b){ b.addEventListener('click', function(){ on = null; update(); }); });
    update();
  })();
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
  td.nm .tt{display:block;margin-top:7px;padding:6px 8px;background:#fff6d6;border-left:3px solid #c99a1e;
          border-radius:4px;font-size:.78rem;line-height:1.42;}
  td.nm .tt > b:first-child{display:block;font-size:.66rem;text-transform:uppercase;letter-spacing:.04em;color:#7a5a08;}
  td.nm .tt .asrc{display:block;margin-top:2px;font-size:.66rem;color:var(--c-mute);}
  :root[data-theme="dark"] td.nm .tt{background:#2b2410;border-left-color:#c99a1e;}
  :root[data-theme="dark"] td.nm .tt > b:first-child{color:#e0b84a;}
  td.nm .age{display:block;margin-top:6px;font-size:.74rem;line-height:1.4;}
  td.nm .age > b{display:block;font-size:.66rem;text-transform:uppercase;letter-spacing:.04em;}
  td.nm .age .asrc{display:block;font-size:.66rem;color:var(--c-mute);}
  td.nm .age .bk{display:block;margin-top:2px;}
  td.nm .age .ext{font-style:italic;color:var(--c-mute);}
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
  /* The tests under each row. Zebra stripes would land on alternate picture rows,
     so the stripes go and the tinted picture row itself separates one condition
     from the next (the cardiac chart's 12-lead row). */
  .tblwrap tbody tr:nth-child(n) td{background:var(--c-tbl);}
  .tblwrap tbody tr:nth-child(n) td.says, .tblwrap tbody tr:nth-child(n) td.exam{background:var(--c-panel);}
  .tblwrap tbody tr.img:nth-child(n) td{background:var(--c-zebra);border-top:1px dashed var(--c-line);
    padding:12px 14px 16px;}
  .pin .ih{margin:0 0 10px;display:flex;align-items:baseline;gap:10px;flex-wrap:wrap;}
  .pin .ih .en{font-size:1.02rem;font-weight:800;color:var(--c-fg);}
  .pin .ih .it{font-size:.66rem;letter-spacing:.04em;text-transform:uppercase;font-weight:700;color:var(--acc);}
  .figs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:22px;}
  .figs.one{grid-template-columns:minmax(0,1fr);}
  figure.tp{margin:0;display:flex;flex-direction:column;gap:10px;min-width:0;}
  .figs.one figure.tp{flex-direction:row;gap:18px;align-items:flex-start;}
  figure.tp img{display:block;max-width:100%;max-height:420px;width:auto;height:auto;align-self:flex-start;
    border-radius:6px;border:1px solid var(--c-line);background:#fff;cursor:zoom-in;}
  .figs.one figure.tp img{max-width:min(620px,58%);}
  figure.tp figcaption{font-size:.84rem;line-height:1.5;max-width:62ch;min-width:0;}
  figure.tp .et{display:block;font-size:.66rem;letter-spacing:.04em;text-transform:uppercase;
    font-weight:700;color:var(--acc);margin-bottom:3px;}
  figure.tp b{display:block;margin-bottom:4px;color:var(--acc);}
  figure.tp .es{display:block;}
  figure.tp .eb{display:block;margin-top:7px;padding:5px 9px;border-left:4px solid #f5be00;
    background:rgba(255,221,0,.16);border-radius:0 6px 6px 0;font-size:.8rem;}
  figure.tp .eb.none{border-left-color:var(--c-line);background:transparent;color:var(--c-mute);}
  figure.tp .ec{display:block;margin-top:8px;font-size:.7rem;color:var(--c-mute);line-height:1.4;}
  figure.tp .ec a{color:inherit;text-decoration:underline;}
  /* A criteria table a slide gives instead of a picture. Not a table element: the page's
     filter and sticky-header code walk the chart's own rows and header cells. */
  .crit{border:1px solid var(--c-line);border-radius:6px;overflow:hidden;font-size:.8rem;line-height:1.4;
    background:var(--c-tbl);max-width:560px;}
  .crit .cr{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.3fr);}
  .crit .cr + .cr{border-top:1px solid var(--c-line);}
  .crit .cr span{padding:6px 9px;}
  .crit .cr span + span{border-left:1px solid var(--c-line);}
  .crit .ch{font-weight:700;background:var(--c-panel);color:var(--c-panel-fg);}
  .crit .hl{background:rgba(255,221,0,.22);box-shadow:inset 4px 0 0 #f5be00;}
  .figs.one figure.tb .crit{flex:0 1 560px;}
  p.nopic{margin:12px 0 0;font-size:.8rem;color:var(--c-mute);line-height:1.45;max-width:90ch;}
  p.nopic b{font-size:.66rem;letter-spacing:.04em;text-transform:uppercase;margin-right:8px;}
  /* Narrow screens: theme.css makes the table swipe sideways and pins each
     row's first cell. The picture row's one cell spans the table, so it is
     unpinned, and its contents are pinned at the screen's width instead:
     the pictures stay in view while the columns scroll past. */
  @media screen and (max-width:900px){
    .wrap .tblwrap tbody tr:nth-child(n) td:first-child{background:var(--c-tbl);}
    .wrap .tblwrap tbody tr.img:nth-child(n) td:first-child{background:var(--c-zebra);position:static;
      box-shadow:none;}
    .pin{position:sticky;left:12px;width:min(760px,calc(100vw - 80px));}
    .figs, .figs.one{grid-template-columns:minmax(0,1fr);}
    .figs.one figure.tp{flex-direction:column;}
    figure.tp img, .figs.one figure.tp img{max-width:100%;max-height:none;}
    figure.tp figcaption{max-width:none;}
  }
  @media print{figure.tp img{max-height:90mm !important;} figure.tp figcaption{font-size:7pt !important;}}
  /* Column names in view: under the sticky guide back bar, not behind it (see the script above). */
  thead th{top:var(--barH,38px);}
  .thfloat{display:none;position:fixed;z-index:540;overflow:hidden;pointer-events:none;
    box-shadow:0 2px 4px rgba(0,0,0,.12);}
  .thfloat table{border-collapse:collapse;table-layout:fixed;}
  .thfloat th{position:static;top:auto;}
  .thfloat th:first-child{position:relative;top:0;z-index:2;}
  @media print{.thfloat{display:none !important;}}
</style>
</body></html>"""

    html = (html.replace("__COLS__", HEADCOLS)
                .replace("__LISTS__", lists_html())
                .replace("__ROUTROWS__", "\n".join(build_row(n) for n in by_tier["routine"]))
                .replace("__URGROWS__", "\n".join(build_row(n) for n in by_tier["urgent"]))
                .replace("__EMROWS__", "\n".join(build_row(n) for n in by_tier["emergent"]))
                .replace("__BUTTONS__", buttons)
                .replace("__NPICS__", str(npics))
                .replace("__NROUT__", str(len(by_tier["routine"])))
                .replace("__NURG__", str(len(by_tier["urgent"])))
                .replace("__NEM__", str(len(by_tier["emergent"])))
                .replace("__N__", str(len(names))))

    for n in names:
        c = html.count('<td class="nm"><b>%s</b>' % n)
        assert c == 1, "row %r emitted %d times, expected once" % (n, c)
        assert html.count('href="#%s"' % slug(n)) == 1, "list link for %r missing" % n
        assert html.count('<tr class="img" id="%s-img"' % slug(n)) == 1, "picture row for %r missing" % n
        o = shown(n)
        for k in CELLS:
            assert not re.search(r"\b(?:slides?|CMS L|PD2|PDM)\s*\d", o[k]), "%s: a cite survived in %s" % (n, k)
    for tag in ("table", "thead", "tbody", "tr", "td", "th", "div", "p", "ol", "li", "header", "h3", "b", "i",
                "figure", "figcaption", "a", "span"):
        o = len(re.findall(r"<%s[ >]" % tag, html)); c = html.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert C.ACCENT not in html, "the CMS violet survived substitution"
    assert "cms-ent-chart-images" not in html, "picture cells leaked from the donor"
    assert "&amp;amp;" not in html and "&amp;ndash;" not in html, "a label was escaped twice"
    body = re.sub(r"<script.*?</script>", "", html.split("<body>", 1)[1], flags=re.S)
    bare = re.findall(r"&(?![a-zA-Z][a-zA-Z0-9]*;|#\d+;)", body)
    assert not bare, "a bare ampersand in the body: %d" % len(bare)
    btn = set(re.findall(r'<button class="filt" data-c="([^"]+)"', html)) - {"__all__"}
    row = {c for v in re.findall(r'<tr id="[^"]+" data-c="([^"]+)"', html) for c in v.split("|")}
    assert btn == row, "filter buttons %r do not match row complaints %r" % (btn - row, row - btn)

    import dark_tokens
    html = dark_tokens.apply(html, "chart")
    open(OUT, "w", encoding="utf-8").write(html)
    if "--depth" in sys.argv:
        depth_report(names)
    print("wrote %s (%d KB, %d conditions: %d routine, %d urgent, %d emergent; %d pictures and tables)"
          % (os.path.basename(OUT), len(html)//1024, len(names),
             len(by_tier["routine"]), len(by_tier["urgent"]), len(by_tier["emergent"]), npics))


if __name__ == "__main__":
    main()
