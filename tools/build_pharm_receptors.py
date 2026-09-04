#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the receptor chart -- Pharmacology I Exam 1, Lecture 3.

Reads left to right in the order Dr. Wood said to think in: WHERE the receptor
is, WHAT it does, then WHICH drugs turn it on and off. The summary grid at the
top is the thing to actually memorise; the cards below are what it expands to.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page
import _pharm_receptor_data as D

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-exam-1-receptor-chart.html")


def main():
    assert os.path.exists(os.path.join(ROOT, "Pharmacology I Exam 1", D.FIGURE["file"])), \
        "effector-organ figure missing"

    # --- the memorise-this grid
    cells = "".join(
        '<div class="rg" style="--rc:%s"><div class="rg-l">%s</div>'
        '<div class="rg-s">%s</div><div class="rg-h">%s</div></div>'
        % (r["colour"], r["label"], r["short"],
           {"a1": "constricts vessels &middot; raises pressure",
            "a2": "presynaptic &mdash; turns the system DOWN",
            "b1": "rate &amp; force up &middot; renin up",
            "b2": "opens airways &middot; dilates muscle beds",
            "m":  "secretions, contractions, slowing",
            "n":  "ganglia, adrenal medulla, muscle"}[r["key"]])
        for r in D.RECEPTORS)

    body = ('<section id="grid"><div class="shead">'
            '<span class="dot" style="background:#c9a227"></span>'
            '<h2>The whole thing in six lines <span class="tag">memorise this</span></h2></div>'
            '<div class="rgrid">%s</div>'
            '<div class="note"><b>The two that catch people.</b> <b>Alpha-1 and alpha-2 pull in '
            'opposite directions</b>, and it is not the number that decides &mdash; it is '
            '<i>where the receptor sits</i>. Alpha-1 is on the target organ, so stimulating it '
            'squeezes. Alpha-2 is on the nerve ending <i>before</i> the target, so stimulating '
            'it turns the whole outflow down. That is why phenylephrine raises blood pressure '
            'and clonidine lowers it, though both are alpha agonists.<br><br>'
            '<b>And beta-2 is why &ldquo;non-selective&rdquo; matters.</b> Propranolol, timolol '
            'and nadolol block beta-2 as well as beta-1 &mdash; which closes airways.</div>'
            '</section>' % cells)

    # --- one card per receptor
    for r in D.RECEPTORS:
        acts = "".join("<li>%s</li>" % a for a in r["actions"])
        body += (
          '<section id="%s"><div class="shead">'
          '<span class="dot" style="background:%s"></span>'
          '<h2>%s <span class="tag">%s</span></h2></div>'
          '<div class="rcard" style="--rc:%s">'
          '<div class="rrow"><span class="rl">Where</span><div>%s</div></div>'
          '<div class="rrow"><span class="rl">What it does</span><div><ul class="ra">%s</ul></div></div>'
          '<div class="rrow hook"><span class="rl">Hook</span><div>%s</div></div>'
          '<div class="rrow on"><span class="rl">Turned ON by</span><div>%s</div></div>'
          '<div class="rrow off"><span class="rl">Turned OFF by</span><div>%s</div></div>'
          '<div class="rsl">Slides %s</div></div></section>'
          % (r["key"], r["colour"], r["label"], r["short"], r["colour"],
             r["where"], acts, r["hook"], r["agon"], r["anta"], r["slides"]))

    body += ('<section id="organs"><div class="shead">'
             '<span class="dot" style="background:#6b5312"></span>'
             '<h2>The same thing organ by organ <span class="tag">slide %d</span></h2></div>'
             '<div class="note">Sympathetic actions in <b>red</b>, parasympathetic in '
             '<b>blue</b>. Read it against the cards above: everything red is alpha or beta, '
             'everything blue is muscarinic.</div>'
             '<figure class="orgfig"><img src="%s" alt="%s" loading="lazy">'
             '<figcaption>Actions of the sympathetic and parasympathetic nervous systems on '
             'effector organs &mdash; lecture slide %d.</figcaption></figure></section>'
             % (D.FIGURE["slide"], D.FIGURE["file"], D.FIGURE["alt"], D.FIGURE["slide"]))

    extra_css = """
  .rgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:9px;
         margin-bottom:14px;}
  .rg{border:1px solid var(--c-line);border-left:5px solid var(--rc);border-radius:10px;
      padding:10px 12px;background:var(--c-ice);}
  .rg-l{font-weight:800;font-size:1rem;color:var(--rc);}
  .rg-s{font-size:.8rem;font-weight:700;margin:2px 0 5px;}
  .rg-h{font-size:.79rem;color:var(--c-mute);line-height:1.4;}
  .rcard{border:1px solid var(--c-line);border-left:5px solid var(--rc);border-radius:10px;
         padding:4px 14px 10px;background:var(--c-ice);}
  .rrow{display:grid;grid-template-columns:118px 1fr;gap:12px;padding:9px 0;
        border-top:1px solid var(--c-line);align-items:start;}
  .rrow:first-child{border-top:none;}
  .rl{font-size:.7rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
      color:var(--c-mute);padding-top:2px;}
  .ra{margin:0;padding-left:18px;} .ra li{margin:3px 0;font-size:.9rem;}
  .rrow.hook div{font-size:.9rem;}
  .rrow.on div, .rrow.off div{font-size:.86rem;line-height:1.55;}
  .rrow.on .rl{color:#1f6b4a;} .rrow.off .rl{color:#8c2f22;}
  .rsl{padding-top:8px;font-size:.7rem;color:var(--c-mute);font-variant-numeric:tabular-nums;}
  .orgfig{margin:0;} .orgfig img{width:100%;height:auto;border-radius:10px;
          border:1px solid var(--c-line);}
  .orgfig figcaption{margin-top:6px;font-size:.74rem;color:var(--c-mute);}
  @media (max-width:620px){.rrow{grid-template-columns:1fr;gap:3px;}}
"""
    legend = ('<span>Six receptors, each read the way he said to think: <b>where it sits &rarr; '
              'what it does &rarr; which drugs turn it on and off</b>. Slides cited on every '
              'card.</span>')
    notes = """    <div class="note"><b>The deck has no table like this.</b> It teaches the receptors on
    slides 22 to 24 and 76 to 78, the organ actions as a figure on slide 11, and then the drugs
    one at a time across nearly a hundred slides. Everything here is from those slides; putting
    it in one place is what the page is for.</div>
    <div class="note warn"><b>Two memory hooks are NOT from the lecture</b> and are labelled where
    they appear: <i>one heart, two lungs</i> for beta-1 against beta-2. They are standard
    mnemonics, included because the point of this page is to be memorable, and flagged so they
    are not mistaken for something the deck said.</div>"""
    toc = ('<a href="#grid">Six lines</a>'
           + "".join('<a href="#%s">%s</a>' % (r["key"], r["label"]) for r in D.RECEPTORS)
           + '<a href="#organs">Organ by organ</a>')

    html = page(
        title="Receptor Chart &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Lecture 3",
        h1="Autonomic Receptor Chart",
        sub="Alpha-1, alpha-2, beta-1, beta-2, muscarinic and nicotinic &mdash; where each one "
            "sits, what it does, and every drug in the lecture that turns it on or off.",
        legend=legend, notes=notes, toc=toc, body=body,
        footer_note="Assembled from the Lecture 3 slides; each card cites the ones it came from.")
    html = html.replace("</style>", extra_css + "</style>")
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d receptors)" % (os.path.basename(OUT), len(html)//1024,
                                              len(D.RECEPTORS)))


if __name__ == "__main__":
    main()
