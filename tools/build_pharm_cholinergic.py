#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the cholinergic drug chart -- Pharmacology I Exam 1, Lecture 3.

The drug-side companion to the receptor chart. Reads in the order Dr. Wood
described: what the drug does at the receptor, then what it is used for as a
consequence, then what to watch for.

THE CONFUSABLE PAIRS COME FIRST, before the drug list. Almost every hard
question in this half of the lecture is two drugs that look interchangeable and
are separated by one axis, and reading those first makes the list below make
sense rather than the other way round.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page
import _pharm_cholinergic_data as D

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-exam-1-cholinergic-chart.html")
DECKSLIDE = "Slide %d"


def main():
    # --- the five groups in one grid
    cells = "".join(
        '<div class="cg" style="--cc:%s"><div class="cg-l">%s</div>'
        '<div class="cg-s">%s</div></div>' % (col, label, one)
        for key, label, col, one, _note in D.GROUPS)
    body = ('<section id="grid"><div class="shead">'
            '<span class="dot" style="background:#c9a227"></span>'
            '<h2>The five groups <span class="tag">start here</span></h2></div>'
            '<div class="cgrid">%s</div>'
            '<div class="note"><b>Two of these block nicotinic receptors and three do not.</b> '
            'The antimuscarinics leave the neuromuscular junction and the autonomic ganglia '
            'alone entirely &mdash; which is why atropine does not paralyse anyone. The '
            'ganglionic blockers and the neuromuscular blockers are the nicotinic pair, and they '
            'differ only in <i>which</i> nicotinic receptor they reach.</div></section>' % cells)

    # --- pairs
    pcards = "".join(
        '<div class="pc"><div class="pc-t">%s</div>'
        '<div class="pc-b"><div class="pc-s">%s</div><div class="pc-v">against</div>'
        '<div class="pc-s">%s</div></div>'
        '<div class="pc-a"><span class="pl">Separated by</span>%s</div>'
        '<div class="pc-sl">Slides %s</div></div>' % (t, l, r, axis, sl)
        for t, l, r, axis, sl in D.PAIRS)
    body += ('<section id="pairs"><div class="shead">'
             '<span class="dot" style="background:#8c2f22"></span>'
             '<h2>The pairs that get confused <span class="tag">learn these first</span></h2>'
             '</div><div class="note">Each of these is two drugs that look interchangeable and '
             'are separated by <b>exactly one axis</b>. Get the axis and the pair comes free.'
             '</div><div class="pgrid">%s</div></section>' % pcards)

    # --- the drugs, by group
    for key, label, col, one, note in D.GROUPS:
        rows = "".join(
            '<div class="dc"><div class="dc-n">%s</div>'
            '<div class="dr"><span class="dl">At the receptor</span><div>%s</div></div>'
            '<div class="dr"><span class="dl">Used for</span><div>%s</div></div>'
            '<div class="dr"><span class="dl">Watch for</span><div>%s</div></div>'
            '<div class="dc-s">%s</div></div>'
            % (name, where, use, watch, DECKSLIDE % slide)
            for g, name, where, use, watch, slide in D.DRUGS if g == key)
        body += ('<section id="%s"><div class="shead">'
                 '<span class="dot" style="background:%s"></span><h2>%s '
                 '<span class="tag">%s</span></h2></div>'
                 '<div class="note">%s</div><div class="dgrid" style="--cc:%s">%s</div></section>'
                 % (key, col, label, one, note, col, rows))

    extra_css = """
  .cgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:9px;
         margin-bottom:13px;}
  .cg{border:1px solid var(--c-line);border-left:5px solid var(--cc);border-radius:10px;
      padding:10px 12px;background:var(--c-ice);}
  .cg-l{font-weight:800;font-size:.92rem;color:var(--cc);line-height:1.25;}
  .cg-s{font-size:.79rem;color:var(--c-mute);margin-top:4px;line-height:1.4;}
  .pgrid{display:grid;grid-template-columns:repeat(auto-fit,minmax(310px,1fr));gap:10px;}
  .pc{border:1px solid var(--c-line);border-left:5px solid #8c2f22;border-radius:10px;
      padding:11px 13px;background:var(--c-ice);}
  .pc-t{font-weight:800;font-size:.92rem;margin-bottom:8px;}
  .pc-b{display:grid;grid-template-columns:1fr auto 1fr;gap:8px;align-items:center;
        margin-bottom:8px;}
  .pc-s{font-size:.83rem;line-height:1.45;}
  .pc-v{font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;color:var(--c-mute);}
  .pc-a{font-size:.85rem;line-height:1.5;padding-top:8px;border-top:1px solid var(--c-line);}
  .pl{display:block;font-size:.68rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
      color:#8c2f22;margin-bottom:3px;}
  .pc-sl{margin-top:7px;font-size:.69rem;color:var(--c-mute);font-variant-numeric:tabular-nums;}
  .dgrid{display:grid;gap:10px;}
  .dc{border:1px solid var(--c-line);border-left:5px solid var(--cc);border-radius:10px;
      padding:4px 14px 9px;background:var(--c-ice);}
  .dc-n{font-weight:800;font-size:.95rem;padding:9px 0 2px;}
  .dr{display:grid;grid-template-columns:118px 1fr;gap:12px;padding:8px 0;
      border-top:1px solid var(--c-line);align-items:start;}
  .dl{font-size:.68rem;font-weight:800;letter-spacing:.05em;text-transform:uppercase;
      color:var(--c-mute);padding-top:2px;}
  .dr div{font-size:.87rem;line-height:1.55;}
  .dc-s{padding-top:7px;font-size:.69rem;color:var(--c-mute);font-variant-numeric:tabular-nums;}
  @media (max-width:620px){.dr{grid-template-columns:1fr;gap:3px;}
    .pc-b{grid-template-columns:1fr;} .pc-v{text-align:left;}}
"""
    legend = ('<span>Every cholinergic drug in Lecture 3, read as <b>what it does at the '
              'receptor &rarr; what it is used for &rarr; what to watch for</b>. Slide cited on '
              'every drug.</span>')
    notes = """    <div class="note"><b>The companion to the receptor chart.</b> That page is organised by
    receptor; this one is organised by drug. Read them together:
    <a href="pharm-exam-1-receptor-chart.html">the receptor chart is here</a>, and the muscarinic
    and nicotinic cards on it are what every drug below is acting on.</div>
    <div class="note warn"><b>The pairs section is the one to read first.</b> Almost every hard
    question in this half of the lecture is two drugs that look interchangeable and are separated
    by a single axis &mdash; and one of them, physostigmine against neostigmine, is an answer
    Dr. Wood gave at the exam review in exactly those terms.</div>"""
    toc = ('<a href="#grid">Five groups</a><a href="#pairs">Confusable pairs</a>'
           + "".join('<a href="#%s">%s</a>' % (k, l) for k, l, _c, _o, _n in D.GROUPS))

    html = page(
        title="Cholinergic Drug Chart &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Lecture 3",
        h1="Cholinergic Drug Chart",
        sub="Every cholinergic and anticholinergic drug in the lecture &mdash; %d agents across "
            "%d groups, plus the %d pairs that actually get confused."
            % (len(D.DRUGS), len(D.GROUPS), len(D.PAIRS)),
        legend=legend, notes=notes, toc=toc, body=body,
        footer_note="Assembled from Lecture 3, slides 26 to 70; each entry cites its slide.")
    html = html.replace("</style>", extra_css + "</style>")
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d drugs, %d groups, %d pairs)"
          % (os.path.basename(OUT), len(html)//1024, len(D.DRUGS), len(D.GROUPS), len(D.PAIRS)))


if __name__ == "__main__":
    main()
