#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the gram-coverage sheet -- Pharmacology I Exam 1.

Every verdict on this page is READ OUT OF THE DECK by
extract_pharm_gram_coverage.py, which pulls the colour of the traffic-light
circle under each heading on the class slide. Nothing is inferred from prose,
and nothing is a judgement call of mine -- if a cell says a class covers
gram-negatives, that is because the lecturer coloured that circle green.

The "leans" column is the only derived field, and it is derived mechanically
from the two gram verdicts so it cannot drift from them.

ACCESSIBILITY: never colour alone. Each cell carries its word -- covers,
partial, moderate, no -- because a red/green table is unreadable to a
red-green colour-blind reader, and roughly one man in twelve is.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page
import _pharm_gram_data as D

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-exam-1-gram-coverage.html")
COV = json.load(open(os.path.join(HERE, "pharm_gram_coverage.json"), encoding="utf-8"))

LABEL = {"yes": "covers", "moderate": "moderate", "partial": "partial", "no": "no"}
CLS = {"yes": "cv-yes", "moderate": "cv-mod", "partial": "cv-part", "no": "cv-no"}


def lean(gp, gn):
    """Mechanically derived from the two gram verdicts -- never hand-set."""
    rank = {"yes": 3, "moderate": 2, "partial": 1, "no": 0}
    p, n = rank[gp], rank[gn]
    if p == 0 and n == 0:
        return "neither", "Neither &mdash; anaerobes"
    if p == n:
        return "both", "Both equally"
    return ("pos", "Mainly gram-positive") if p > n else ("neg", "Mainly gram-negative")


def cell(v):
    return '<td class="cv %s"><span>%s</span></td>' % (CLS[v], LABEL[v])


def main():
    rows, tally = [], {"pos": 0, "neg": 0, "both": 0, "neither": 0}
    for name, drugs, note, slide in D.ROWS:
        c = COV[str(slide)]["coverage"]
        gp, gn, an = c["Gram Positive"], c["Gram Negative"], c["Anaerobes"]
        key, txt = lean(gp, gn)
        tally[key] += 1
        rows.append(
            '<tr data-lean="%s" data-an="%s">'
            '<td class="nm"><b>%s</b><span class="dr">%s</span></td>'
            '%s%s%s'
            '<td class="ln"><span class="lp lp-%s">%s</span></td>'
            '<td class="nt">%s</td><td class="sl">%d</td></tr>'
            % (key, "y" if an in ("yes", "moderate", "partial") else "n",
               name, drugs, cell(gp), cell(gn), cell(an), key, txt, note, slide))

    prog = "".join("<li>%s</li>" % l for l in D.PROGRESSION["lines"])
    body = (
      '<section id="progression"><div class="shead">'
      '<span class="dot" style="background:#c9a227"></span>'
      '<h2>The rule the whole cephalosporin block turns on '
      '<span class="tag">slide %d</span></h2></div>'
      '<ul class="prog">%s</ul>'
      '<div class="note"><b>Read the table below against that.</b> First generation is the '
      'strong gram-positive agent; by third generation the gram-negative cover is better and '
      'the gram-positive has been given away; <b>fourth generation is the one that breaks the '
      'trade-off</b>, and fifth is where MRSA cover appears.</div></section>'
      % (D.PROGRESSION["slide"], prog))

    body += (
      '<section id="why"><div class="shead">'
      '<span class="dot" style="background:#5566b5"></span>'
      '<h2>Why this is the axis to revise <span class="tag">from the exam review</span></h2>'
      '</div><div class="note warn">At the review session the evening before the paper, '
      'Dr. Wood said he is <b>not</b> asking which single drug treats one named organism. He is '
      'asking whether an agent covers gram-positives, gram-negatives, anaerobes or atypicals '
      '&mdash; and he described the question outright: <i>&ldquo;a patient has an infection, a '
      'skin infection. Do you think it&rsquo;s a gram-positive bacteria? Which one of these '
      'would be most likely to treat it?&rdquo;</i>, built from <b>three agents with strictly '
      'gram-negative coverage and one good gram-positive</b>. '
      '<a href="pharm-exam-1-review-session.html">The full review is here.</a></div></section>')

    body += (
      '<section id="table"><div class="shead">'
      '<span class="dot" style="background:#2f6b5a"></span>'
      '<h2>All %d classes <span class="tag">read from the deck&rsquo;s own traffic lights</span>'
      '</h2></div>'
      '<div class="filters">'
      '<button class="gf on" data-f="all">All %d</button>'
      '<button class="gf" data-f="pos">Mainly gram-positive (%d)</button>'
      '<button class="gf" data-f="neg">Mainly gram-negative (%d)</button>'
      '<button class="gf" data-f="both">Both equally (%d)</button>'
      '<button class="gf" data-f="anaer">Covers anaerobes</button>'
      '</div>'
      '<div class="tw"><table><thead><tr>'
      '<th>Class &amp; drugs</th><th>Gram +</th><th>Gram &minus;</th><th>Anaerobes</th>'
      '<th>Leans</th><th>What that means</th><th>Slide</th>'
      '</tr></thead><tbody>%s</tbody></table></div></section>'
      % (len(D.ROWS), len(D.ROWS), tally["pos"], tally["neg"], tally["both"], "\n".join(rows)))

    extra_css = """
  .prog{margin:0 0 12px;padding-left:20px;} .prog li{margin:4px 0;font-size:.95rem;}
  .tw{overflow-x:auto;} table{width:100%;border-collapse:collapse;font-size:.86rem;}
  th{text-align:left;background:var(--c-panel);color:var(--c-panel-fg);padding:8px;
     position:sticky;top:0;}
  td{padding:8px;border-top:1px solid var(--c-line);vertical-align:top;}
  td.nm b{display:block;} td.nm .dr{display:block;margin-top:3px;font-size:.76rem;
     color:var(--c-mute);font-style:italic;}
  td.cv{text-align:center;white-space:nowrap;}
  td.cv span{display:inline-block;padding:2px 9px;border-radius:999px;font-size:.74rem;
     font-weight:700;letter-spacing:.01em;}
  .cv-yes span{background:#1f6b4a;color:#fff;}
  .cv-mod span{background:#6b7f35;color:#fff;}
  .cv-part span{background:#8a5f14;color:#fff;}
  .cv-no span{background:#8c2f22;color:#fff;}
  td.ln{white-space:nowrap;}
  .lp{display:inline-block;padding:2px 9px;border-radius:999px;font-size:.74rem;font-weight:600;
      border:1px solid var(--c-line);}
  .lp-pos{background:#e8f2ec;color:#17493a;} .lp-neg{background:#eceef7;color:#2d3f7a;}
  .lp-both{background:#f4efe2;color:#6b5312;} .lp-neither{background:#f2eef4;color:#5f3a6b;}
  td.sl{text-align:center;color:var(--c-mute);font-variant-numeric:tabular-nums;}
  .filters{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 12px;}
  .gf{font:inherit;font-size:.8rem;padding:5px 12px;border-radius:999px;cursor:pointer;
      border:1px solid var(--c-line);background:var(--c-btn-bg);color:var(--c-fg);}
  .gf.on{background:var(--acc);color:#fff;border-color:var(--acc);}
  :root[data-theme="dark"] .lp-pos{background:#1c3a30;color:#a9dcc6;}
  :root[data-theme="dark"] .lp-neg{background:#232a44;color:#b9c4ee;}
  :root[data-theme="dark"] .lp-both{background:#3a3320;color:#e2cf96;}
  :root[data-theme="dark"] .lp-neither{background:#332a3a;color:#d5bde2;}
"""
    script = """<script>
  document.querySelectorAll('.gf').forEach(function(b){
    b.addEventListener('click', function(){
      document.querySelectorAll('.gf').forEach(function(x){x.classList.remove('on');});
      b.classList.add('on');
      var f = b.dataset.f;
      document.querySelectorAll('tbody tr').forEach(function(tr){
        var ok = f === 'all' ? true
               : f === 'anaer' ? tr.dataset.an === 'y'
               : tr.dataset.lean === f;
        tr.style.display = ok ? '' : 'none';
      });
    });
  });
</script>"""

    legend = ('<span>Every verdict is <b>read out of the lecture deck</b> &mdash; each class '
              'slide carries a traffic-light table and the colour under each heading is what is '
              'printed here. The slide number is on every row.</span>')
    notes = """    <div class="note"><b>Where these judgements come from.</b> They are not mine and they are
    not inferred from the prose. Most antibiotic class slides carry a small three-column table
    &mdash; Gram Positive, Gram Negative, Anaerobes &mdash; with a coloured circle under each
    heading, and this page prints those colours. Nothing in the slide text states which colour
    sits under which heading, so each circle is matched to its column by position.</div>
    <div class="note"><b>Two shades of green, and one odd one.</b> The deck uses two greens
    interchangeably and both are shown here as <b>covers</b>. A third, lighter green appears on
    exactly one class &mdash; the tetracyclines, on all three columns at once &mdash; and is shown
    separately as <b>moderate</b>, because using it once and only across the board reads as
    deliberate rather than as a colour slip.</div>
    <div class="note warn"><b>Colour is never the only signal here.</b> Each cell carries its word
    as well as its colour, because a red-and-green table is unreadable to a red-green colour-blind
    reader.</div>"""
    toc = ('<a href="#progression">The generation rule</a>'
           '<a href="#why">Why this axis</a><a href="#table">All %d classes</a>' % len(D.ROWS))

    html = page(
        title="Gram Coverage by Class &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Class of 2028",
        h1="Gram Coverage by Drug Class",
        sub="Every antibiotic class in Lecture 1, with whether it covers gram-positives, "
            "gram-negatives and anaerobes &mdash; taken from the traffic-light table on each "
            "class slide. %d classes: %d lean gram-positive, %d lean gram-negative, %d cover "
            "both equally."
            % (len(D.ROWS), tally["pos"], tally["neg"], tally["both"]),
        legend=legend, notes=notes, toc=toc, body=body,
        footer_note="Verdicts extracted by <code>tools/extract_pharm_gram_coverage.py</code> "
                    "directly from the lecture deck, so a cell cannot drift from the slide it "
                    "cites.")
    html = html.replace("</style>", extra_css + "</style>").replace("</body>", script + "</body>")
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d classes; %d positive-leaning, %d negative-leaning, "
          "%d both, %d neither)"
          % (os.path.basename(OUT), len(html) // 1024, len(D.ROWS),
             tally["pos"], tally["neg"], tally["both"], tally["neither"]))


if __name__ == "__main__":
    main()
