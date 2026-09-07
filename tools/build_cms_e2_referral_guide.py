#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the CMS I Exam 2 referral-urgency guide -- every ophthalmic condition
that needs ophthalmology sooner than a routine clinic slot.

Jaxon, 2026-09-07: "Can you make a CMS optho guide for all the disease that
require urgent/immediate ophthomology referral" -- Exam 2 content.

The spine of the page is Lecture 10 slides 66-71, which are a self-contained
RED EYE TRIAGE section: the first sixty seconds, the danger signs, localising by
pattern, and an explicit four-tier disposition. The deck builds to it and then
never returns, so it is easy to read past. Everything downstream is the same
tiering applied to all five lectures.

The condition rows come from build_cms_ophtho_chart.py, which is the audited
source for this block -- the giveaway is the chart's, and the first move is
_cms_e2_referral_data.FIRST, a triage-length distillation of the chart's own
management field. Nothing here is sourced outside the slides.

The page shell (theme handling, styles, service worker, report-a-mistake) is
sliced live out of cms-exam-2-study-guide.html rather than copied, so the two
pages cannot drift apart visually.

    python3 tools/build_cms_e2_referral_guide.py
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import build_cms_ophtho_chart as chart
import _cms_e2_referral_data as D

ROOT = os.path.dirname(HERE)
DIR = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 2")
GUIDE = os.path.join(DIR, "cms-exam-2-study-guide.html")
OUT = os.path.join(DIR, "cms-exam-2-referral-guide.html")

LECTURE = {"Eyelid": "L10", "Lacrimal": "L10", "Surface": "L10", "Conjunctivitis": "L10",
           "Sclera": "L10", "Orbit": "L10", "Cornea": "L10", "Uvea": "L10",
           "Neuro-ophthalmology": "L11", "Acute vision loss": "L12",
           "Chronic vision loss": "L13", "Refractive": "L13", "Ocular tumors": "L13",
           "Ocular trauma": "L14"}
DECKNAME = {"L10": "Common Ophthalmological Disorders", "L11": "Neuro-Ophthalmology",
            "L12": "Acute Vision Loss", "L13": "Chronic Vision Loss &amp; Tumors",
            "L14": "Ocular Trauma"}


def tier(urgency):
    u = re.sub(r"<[^>]+>", "", urgency).strip().upper()
    for t in ("EMERGENT", "SAME DAY", "URGENT"):
        if u.startswith(t):
            return t
    return "ROUTINE"


def rows_for(t):
    out = []
    for r in chart.ROWS:
        if tier(r[6]) == t:
            out.append(dict(name=r[0], group=r[1], give=r[2], urg=r[6],
                            lec=LECTURE.get(r[1], "L10"), slides=r[8]))
    return out


EXTRA_CSS = """
<style>
  .tierbar{display:flex;flex-wrap:wrap;gap:10px;margin:16px 0 4px;}
  .tierbar a{flex:1 1 150px;text-decoration:none;border-radius:10px;padding:11px 13px;
    color:#fff;font-weight:700;font-size:.9rem;line-height:1.25;}
  .tierbar a span{display:block;font-weight:500;font-size:.74rem;opacity:.9;margin-top:2px;}
  .t-em{background:#9d2235;} .t-sd{background:#b26a12;}
  .t-ur{background:#2d3f7a;} .t-ro{background:#5c6070;}
  .rtab{width:100%;border-collapse:collapse;margin:14px 0 6px;font-size:.9rem;}
  .rtab th{text-align:left;font-size:.7rem;text-transform:uppercase;letter-spacing:.8px;
    color:var(--soft);border-bottom:2px solid var(--line);padding:6px 8px;font-weight:700;}
  .rtab td{border-bottom:1px solid var(--line);padding:9px 8px;vertical-align:top;}
  .rtab tr:last-child td{border-bottom:none;}
  .rtab .cn{font-weight:700;width:19%;}
  /* The chart bolds the whole giveaway because there it competes with eight other
     columns. Here it would drown out the first-move column, which is the point of
     the page -- so the phrase keeps its weight but drops back in colour. */
  .rtab .cg{width:30%;color:var(--soft);font-size:.87rem;}
  .rtab .cg b{font-weight:600;color:var(--ink);}
  .rtab .cf{width:41%;}
  .rtab .cs{width:10%;font-size:.76rem;color:var(--soft);white-space:nowrap;}
  .lecpill{display:inline-block;font-size:.66rem;font-weight:700;letter-spacing:.5px;
    background:var(--accent3);color:#fff;border-radius:4px;padding:1px 5px;margin-left:5px;
    vertical-align:1px;}
  .neverbox{border-left:5px solid #9d2235;background:rgba(157,34,53,.07);border-radius:0 10px 10px 0;
    padding:12px 16px;margin:12px 0;}
  .neverbox b.n-h{display:block;font-size:.97rem;margin-bottom:2px;}
  .neverbox .n-w{font-size:.87rem;color:var(--soft);}
  .neverbox .n-c{font-size:.72rem;color:var(--soft);opacity:.85;display:block;margin-top:4px;}
  .sixty{display:grid;grid-template-columns:repeat(auto-fit,minmax(215px,1fr));gap:10px;margin:14px 0;}
  .sixty div{border:1px solid var(--line);border-radius:10px;padding:10px 12px;background:#fff;}
  .sixty b{display:block;font-size:.9rem;}
  .sixty span{font-size:.8rem;color:var(--soft);}
  [data-theme="dark"] .sixty div{background:rgba(255,255,255,.04);}
  .dangerlist li{margin-bottom:5px;}
  .rcite{font-size:.74rem;color:var(--soft);margin:4px 0 0;}
  .rnote{display:block;margin-top:6px;font-size:.8rem;line-height:1.45;padding:6px 9px;
    border-radius:7px;border-left:3px solid;}
  .rnote::before{font-weight:700;letter-spacing:.4px;font-size:.66rem;text-transform:uppercase;
    display:block;margin-bottom:2px;}
  .n-conflict{border-color:#9d2235;background:rgba(157,34,53,.08);}
  .n-conflict::before{content:"The deck contradicts itself";color:#9d2235;}
  .n-nointerval{border-color:#b26a12;background:rgba(178,106,18,.08);}
  .n-nointerval::before{content:"No interval stated";color:#b26a12;}
  .n-nuance{border-color:var(--accent3);background:rgba(85,102,181,.09);}
  .n-nuance::before{content:"Read the exception";color:var(--accent3);}
  details.qa{border:1px solid var(--line);border-radius:10px;margin:9px 0;background:#fff;}
  details.qa summary{cursor:pointer;padding:11px 14px;font-weight:600;font-size:.92rem;
    list-style:none;}
  details.qa summary::-webkit-details-marker{display:none;}
  details.qa summary::before{content:"▸";color:var(--accent);margin-right:8px;
    display:inline-block;transition:transform .15s;}
  details.qa[open] summary::before{transform:rotate(90deg);}
  details.qa .qa-a{padding:0 14px 12px 30px;font-size:.9rem;color:var(--soft);}
  [data-theme="dark"] details.qa{background:rgba(255,255,255,.04);}
  @media (max-width:640px){
    .rtab,.rtab tbody,.rtab tr,.rtab td{display:block;width:100%;}
    .rtab thead{display:none;}
    .rtab tr{border-bottom:1px solid var(--line);padding:8px 0;}
    .rtab td{border:none;padding:2px 0;}
    .rtab .cn{font-size:1rem;}
    .rtab .cs{white-space:normal;}
  }
</style>
"""


def table(rows, extra=()):
    h = ['<table class="rtab"><thead><tr><th>Condition</th><th>What gives it away</th>'
         '<th>First move</th><th>Slides</th></tr></thead><tbody>']
    for r in rows:
        first = D.FIRST.get(re.sub(r"<[^>]+>", "", r["name"]).strip(), None)
        if first is None:
            first = D.FIRST.get(r["name"])
        assert first, "no first move written for %r" % r["name"]
        note = D.NOTE.get(re.sub(r"<[^>]+>", "", r["name"]).strip()) or D.NOTE.get(r["name"])
        nhtml = ('<span class="rnote n-%s">%s</span>' % note) if note else ""
        h.append('<tr><td class="cn">%s<span class="lecpill">%s</span></td>'
                 '<td class="cg">%s</td><td class="cf">%s%s</td>'
                 '<td class="cs">Slides %s</td></tr>'
                 % (r["name"], r["lec"], r["give"], first, nhtml, r["slides"]))
    for name, group, give, cite in extra:
        h.append('<tr><td class="cn">%s</td><td class="cg">%s</td><td class="cf">%s</td>'
                 '<td class="cs">%s</td></tr>' % (name, give, D.FIRST[name], cite))
    h.append("</tbody></table>")
    return "\n".join(h)


def build():
    src = open(GUIDE, encoding="utf-8").read()
    shell = src[:src.index('<header class="top">')]
    tail = src[src.index("</main>"):]

    em, sd, ur = rows_for("EMERGENT"), rows_for("SAME DAY"), rows_for("URGENT")
    n_em = len(em) + len(D.EXTRA_EMERGENT)
    total = n_em + len(sd) + len(ur)

    toc = ['<nav class="toc">',
           '<a class="top-link" href="#how">How to use this</a>',
           '<a class="top-link" href="#triage">1 &middot; Triage before diagnosis</a>',
           '<a class="sub-link" href="#sixty">1.1 The first 60 seconds</a>',
           '<a class="sub-link" href="#danger">1.2 Danger signs</a>',
           '<a class="sub-link" href="#pattern">1.3 Localise by pattern</a>',
           '<a class="sub-link" href="#ladder">1.4 The disposition ladder</a>',
           '<a class="top-link" href="#emergent">2 &middot; EMERGENT &mdash; now (%d)</a>' % n_em,
           '<a class="top-link" href="#sameday">3 &middot; SAME DAY (%d)</a>' % len(sd),
           '<a class="top-link" href="#urgent">4 &middot; URGENT &mdash; 24&ndash;48 h (%d)</a>'
           % len(ur),
           '<a class="top-link" href="#escalate">5 &middot; Routine, until it is not</a>',
           '<a class="top-link" href="#never">6 &middot; Never do these</a>',
           '<a class="top-link" href="#check">7 &middot; Check yourself</a>',
           '</nav>']

    b = ['<main>']
    b.append('<section id="how"><h2 class="deck-title">How to use this</h2>'
             '<p>Every condition in the Exam 2 ophthalmology block that needs ophthalmology '
             '<strong>sooner than a routine clinic slot</strong> &mdash; %d of them &mdash; sorted '
             'by how fast, with the finding that identifies it and the first thing to do. The '
             'tiers are the ones Professor Jaquith uses on the disposition slide, not a scheme '
             'invented for this page.</p>'
             '<p><strong>Checked slide by slide against all five decks.</strong> Where a lecture '
             'states an urgency, that is the tier. Where it says only &ldquo;refer&rdquo; and never '
             'says how fast, the row says so rather than inventing an interval &mdash; and where a '
             'deck gives <em>two different answers in two places</em>, both are printed. There are '
             'two of those, and they are the ones worth knowing about.</p>'
             '<p><strong>The order matters more than the list.</strong> Sections 1.1 to 1.4 are a '
             'triage sequence the lecture asks you to complete <em>before</em> naming a diagnosis; '
             'the condition tables are what that sequence sorts into. If you are revising against '
             'the clock, section 6 is the one that changes what you do at the bedside.</p>'
             '<div class="tierbar">'
             '<a class="t-em" href="#emergent">EMERGENT<span>now &middot; %d conditions</span></a>'
             '<a class="t-sd" href="#sameday">SAME DAY<span>today &middot; %d</span></a>'
             '<a class="t-ur" href="#urgent">URGENT<span>24&ndash;48 hours &middot; %d</span></a>'
             '<a class="t-ro" href="#escalate">ROUTINE<span>until a trigger fires &middot; %d</span></a>'
             '</div></section>' % (total, n_em, len(sd), len(ur), len(D.ESCALATE)))

    b.append('<section id="triage"><h2 class="deck-title">1 &middot; Triage before diagnosis</h2>'
             '<p>Lecture 10 closes on six slides of pure triage. They are worth more than any '
             'single condition on this page, because they work on the red eye you cannot name '
             'yet.</p>')
    b.append('<h3 class="sub" id="sixty">1.1 &middot; The first 60 seconds</h3>'
             '<p>Complete all of it <strong>before</strong> naming the diagnosis.</p><div class="sixty">')
    for h, w in D.FIRST_60:
        b.append('<div><b>%s</b><span>%s</span></div>' % (h, w))
    b.append('</div><p class="callout">%s</p>' % D.FIRST_60_RULE)

    b.append('<h3 class="sub" id="danger">1.2 &middot; Danger signs &mdash; this is not simple conjunctivitis</h3>'
             '<p>Any one of these means immediate or same-day evaluation.</p>'
             '<ul class="dangerlist">')
    for d in D.DANGER:
        b.append("<li>%s</li>" % d)
    b.append("</ul>")

    b.append('<h3 class="sub" id="pattern">1.3 &middot; Localise by pattern</h3>'
             '<table class="rtab"><thead><tr><th>Where</th><th>What you see</th></tr></thead><tbody>')
    for where, what in D.PATTERN:
        b.append('<tr><td class="cn">%s</td><td>%s</td></tr>' % (where, what))
    b.append("</tbody></table>")

    b.append('<h3 class="sub" id="ladder">1.4 &middot; The disposition ladder</h3>'
             '<p>The deck\'s own four tiers, and the examples it gives for each.</p>'
             '<table class="rtab"><thead><tr><th>Tier</th><th>When</th><th>Examples given</th>'
             '</tr></thead><tbody>')
    for t, when, ex in D.LADDER:
        b.append('<tr><td class="cn">%s</td><td class="cs">%s</td><td>%s</td></tr>' % (t, when, ex))
    b.append('</tbody></table><p class="rcite">Common Ophthalmological Disorders, slides '
             '66&ndash;70</p></section>')

    b.append('<section id="emergent"><h2 class="deck-title">2 &middot; EMERGENT &mdash; now</h2>'
             '<p>%d conditions. These do not wait for a clinic list, and several of them are lost '
             'in minutes to hours: the central retinal artery is irreversible after 90 minutes, '
             'and hyphema rebleeds hardest in the first 72 hours.</p>' % n_em)
    b.append(table(em, D.EXTRA_EMERGENT))
    b.append('</section>')

    b.append('<section id="sameday"><h2 class="deck-title">3 &middot; SAME DAY</h2>'
             '<p>%d conditions &mdash; the deck names four of these on the disposition slide '
             'itself: keratitis or corneal ulcer, anterior uveitis, scleritis and ocular herpes '
             'zoster.</p>' % len(sd))
    b.append(table(sd))
    b.append('</section>')

    b.append('<section id="urgent"><h2 class="deck-title">4 &middot; URGENT &mdash; within '
             '24&ndash;48 hours</h2>'
             '<p>%d conditions. The generic trigger, for anything not named below, is unexplained '
             'decreased vision, persistent pain or photophobia, or an atypical or worsening red '
             'eye.</p>' % len(ur))
    b.append('<p class="callout">Every neuro-ophthalmology condition follows the same pathway: %s</p>' % D.NEURO_PATHWAY)
    b.append(table(ur))
    b.append('</section>')

    b.append('<section id="escalate"><h2 class="deck-title">5 &middot; Routine, until it is not</h2>'
             '<p>These are managed in clinic &mdash; until one of these triggers fires, and then '
             'they are not. This table is the one that catches people out, because the diagnosis '
             'does not change; only the disposition does.</p>'
             '<table class="rtab"><thead><tr><th>Condition</th><th>What changes it</th>'
             '<th>Becomes</th><th>Slides</th></tr></thead><tbody>')
    for name, trig, becomes, cite in D.ESCALATE:
        b.append('<tr><td class="cn">%s</td><td class="cg" style="width:52%%">%s</td>'
                 '<td class="cf" style="width:14%%"><b>%s</b></td><td class="cs">%s</td></tr>'
                 % (name, trig, becomes, cite))
    b.append("</tbody></table></section>")

    b.append('<section id="never"><h2 class="deck-title">6 &middot; Never do these</h2>'
             '<p>Every one of these is stated outright in a lecture, and every one of them is a '
             'way of making the eye worse while meaning to help.</p>')
    for head, why, cite in D.NEVER:
        b.append('<div class="neverbox"><b class="n-h">%s</b><span class="n-w">%s</span>'
                 '<span class="n-c">%s</span></div>' % (head, why, cite))
    b.append("</section>")

    b.append('<section id="check"><h2 class="deck-title">7 &middot; Check yourself</h2>')
    for i, (q, a) in enumerate(D.QUIZ, 1):
        b.append('<details class="qa"><summary>%d. %s</summary><div class="qa-a">%s</div>'
                 '</details>' % (i, q, a))
    b.append("</section>")
    b.append("")

    header = ('<header class="top">\n'
              '  <h1>Clinical Medicine and Surgery I &middot; Exam 2 &mdash; Referral Urgency</h1>\n'
              '  <p>PAJ 5500 Clinical Medicine and Surgery I &middot; Class of 2028</p>\n'
              '  <p>Ophthalmology block &middot; every condition needing ophthalmology sooner than '
              'a routine clinic slot &middot; tiers taken from the lecture&rsquo;s own disposition '
              'slide</p>\n</header>\n\n<div class="layout wrap" data-readable>\n')

    html = (shell.replace("Clinical Medicine and Surgery I &middot; Exam 2 &mdash; Study Guide",
                          "Clinical Medicine and Surgery I &middot; Exam 2 &mdash; Referral Urgency")
            + EXTRA_CSS + header + "\n".join(toc) + "\n" + "\n".join(b) + "\n" + tail)
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB)" % (os.path.basename(OUT), len(html) // 1024))
    print("  EMERGENT %d (%d from the chart + %d named only on the disposition slide)"
          % (n_em, len(em), len(D.EXTRA_EMERGENT)))
    print("  SAME DAY %d   URGENT %d   escalation triggers %d   prohibitions %d"
          % (len(sd), len(ur), len(D.ESCALATE), len(D.NEVER)))
    print("  total conditions needing more than routine referral: %d" % total)
    return html


if __name__ == "__main__":
    build()
