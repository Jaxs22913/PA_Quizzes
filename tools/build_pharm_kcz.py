#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the killers / commons / zebras chart -- Pharmacology I Exam 1.

The framework is Dr. Wood's, from the exam review. The entries are the decks'
own adverse effects sorted by his stated criteria, each citing its slide.

TWO THINGS ARE KEPT VISIBLY APART, because conflating them would overstate the
page's authority: the nine effects HE NAMED HIMSELF at the review are badged as
such, and everything else is marked as the deck's content sorted by his rule.
He did not assign those buckets; his criteria did.

The three framework quotes are checked against the review transcript before the
page is written, using the same machinery as the review page itself.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page
import _pharm_kcz_data as D
import check_pharm_review as V

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-exam-1-killers-commons-zebras.html")

FRAMEWORK = [
 "there's the killers, the commons and the zebras",
 "no, they're all the same",
 "any time you see those killers or the zebras",
]

BUCKETS = [
 ("killers", "Killers", "#8c2f22", D.KILLERS,
  "Dangerous. <b>Immediate discontinuation and evaluation.</b> Not necessarily the commonest "
  "&mdash; these are the ones you warn the patient about <i>in advance</i>, so that they do not "
  "decide that skin sloughing off is a normal side effect."),
 ("commons", "Commons", "#6b5312", D.COMMONS,
  "What actually happens, often. <b>These belong to the GROUP, not the drug.</b> Asked whether "
  "the common effects of penicillins, cephalosporins and carbapenems need learning separately, "
  "he said <i>&ldquo;no, they&rsquo;re all the same&rdquo;</i> &mdash; so they are listed by "
  "group here, and the effort goes where a class breaks the pattern."),
 ("zebras", "Zebras", "#5f3a8a", D.ZEBRAS,
  "Uncommon, but <b>unique to one drug</b>. <i>&ldquo;Whenever you hear hoofs beating, normally "
  "you should be thinking horses. Sometimes it&rsquo;s a zebra.&rdquo;</i> Each is worth about "
  "one question &mdash; and together with the killers they are where he told the class to look."),
]


def main():
    t = V.transcript()
    missing = [q for q in FRAMEWORK if V.norm(q) not in t]
    if missing:
        sys.exit("framework quote not in the review recording: %r" % missing)
    print("framework quotes verified against the review recording: %d/%d"
          % (len(FRAMEWORK), len(FRAMEWORK)))

    body = (
      '<section id="how"><div class="shead">'
      '<span class="dot" style="background:#c9a227"></span>'
      '<h2>How to use this <span class="tag">his framework, not a list</span></h2></div>'
      '<div class="note warn">Asked which adverse effects to focus on, Dr. Wood did not give a '
      'list &mdash; he gave three buckets and told the class to sort everything into them. '
      '<b>The sorting is the revision.</b> Take any side effect you have learned and ask: would '
      'this kill them, does it happen to nearly everyone on the group, or is it the one strange '
      'thing that belongs to this drug alone?<br><br>'
      '<b>Where he said to aim:</b> <i>&ldquo;Any time you see those killers or the zebras, '
      'those are always things you should look at.&rdquo;</i> The commons cover a good share of '
      'what he asks and mostly come free with the group; the killers and the zebras are each '
      'worth about a question.</div>'
      '<div class="note"><b>What is his and what is not.</b> The nine entries badged '
      '<span class="hb">his example</span> are effects he named himself at the review. The rest '
      'are the lecture decks&rsquo; own adverse effects sorted by his criteria, each citing its '
      'slide. He did not assign those buckets &mdash; his rule did, and you can check every one '
      'against the slide beside it.</div></section>')

    for key, title, colour, rows, blurb in BUCKETS:
        cards = []
        for eff, drugs, note, deck, slide, his in rows:
            badge = '<span class="hb">his example</span>' if his else ""
            cards.append(
                '<div class="kc"><div class="kc-h"><b>%s</b>%s</div>'
                '<div class="kc-d">%s</div><div class="kc-n">%s</div>'
                '<div class="kc-s">%s &middot; slide %d</div></div>'
                % (eff, badge, drugs, note, deck, slide))
        body += ('<section id="%s"><div class="shead">'
                 '<span class="dot" style="background:%s"></span>'
                 '<h2>%s <span class="tag">%d</span></h2></div>'
                 '<div class="note">%s</div><div class="kcg">%s</div></section>'
                 % (key, colour, title, len(rows), blurb, "".join(cards)))

    extra_css = """
  .kcg{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:10px;}
  .kc{border:1px solid var(--c-line);border-radius:10px;padding:11px 13px;background:var(--c-ice);}
  .kc-h{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap;margin-bottom:4px;}
  .kc-h b{font-size:.95rem;}
  .kc-d{font-size:.78rem;color:var(--c-mute);font-style:italic;margin-bottom:6px;}
  .kc-n{font-size:.86rem;line-height:1.5;}
  .kc-s{margin-top:7px;font-size:.7rem;color:var(--c-mute);font-variant-numeric:tabular-nums;}
  .hb{font-size:.64rem;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
      padding:2px 7px;border-radius:999px;background:var(--gold);color:#241a02;white-space:nowrap;}
  #killers .kc{border-left:3px solid #8c2f22;}
  #commons .kc{border-left:3px solid #6b5312;}
  #zebras  .kc{border-left:3px solid #5f3a8a;}
"""
    legend = ('<span>Three buckets, from the exam review. The <b>nine badged entries are effects '
              'he named himself</b>; the rest are the decks&rsquo; adverse effects sorted by his '
              'criteria, each citing its slide.</span>')
    notes = """    <div class="note"><b>Why a framework beats a list.</b> The side-effects reference on this
    site is organised by drug, which is the right shape for looking something up and the wrong
    shape for revising. This one is organised the way he said he thinks about them, which is the
    shape the question comes in. Use both:
    <a href="pharm-exam-1-side-effects.html">the full side-effects chart is here</a>.</div>"""
    toc = ('<a href="#how">How to use this</a><a href="#killers">Killers</a>'
           '<a href="#commons">Commons</a><a href="#zebras">Zebras</a>')

    html = page(
        title="Killers, Commons and Zebras &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Class of 2028",
        h1="Killers, Commons and Zebras",
        sub="Dr. Wood&rsquo;s own framework for sorting every adverse effect, from the exam "
            "review the evening before the paper. %d killers, %d groups of commons and %d "
            "zebras, each citing its slide."
            % (len(D.KILLERS), len(D.COMMONS), len(D.ZEBRAS)),
        legend=legend, notes=notes, toc=toc, body=body,
        footer_note="The framework quotes are verified against the review recording before this "
                    "page is written. The recording stays on the course owner's machine and is "
                    "never copied into this repo.")
    html = html.replace("</style>", extra_css + "</style>")
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d killers, %d commons, %d zebras, %d his own)"
          % (os.path.basename(OUT), len(html) // 1024, len(D.KILLERS), len(D.COMMONS),
             len(D.ZEBRAS),
             sum(1 for g in (D.KILLERS, D.COMMONS, D.ZEBRAS) for e in g if e[5])))


if __name__ == "__main__":
    main()
