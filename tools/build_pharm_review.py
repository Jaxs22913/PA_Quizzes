#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build "Dr. Wood's Exam Review Session" -- Pharmacology I Exam 1.

The companion to pharm-exam-1-what-to-star.html. That page is drawn from the
three CONTENT lectures; this one is drawn from the review session held the
evening before the paper, where the class asked questions and he answered them.

A review session is the one recording where a lecturer says what is and is not
being asked. That makes it the most useful thing on the site the night before,
and also the most dangerous thing to get wrong -- a page that misreports scope
sends people to revise the wrong material. So it REFUSES TO WRITE unless
check_pharm_review.py passes, and every quote is proved verbatim first.
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page
import _pharm_review_data as D

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-exam-1-review-session.html")


def quote_block(q, at):
    return ('<blockquote class="wq"><p>&ldquo;%s&rdquo;</p>'
            '<footer>Dr. Wood &middot; Exam review session, 3 September &middot; '
            '<span class="ts">%s</span></footer></blockquote>' % (q, at))


def entry(it, dot):
    ask = ('<p class="asked"><b>Asked:</b> &ldquo;%s&rdquo;</p>' % it["q"]) if it.get("q") else ""
    return ('<section id="%s"><div class="shead">'
            '<span class="dot" style="background:%s"></span><h2>%s</h2></div>'
            '%s%s%s</section>' % (it["id"], dot, it["title"], ask,
                                  quote_block(it["quote"], it["at"]), it["body"]))


def main():
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_pharm_review.py")],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        print(r.stdout, r.stderr)
        sys.exit("fact-check failed -- refusing to write the page")

    secs = []
    secs.append(
        '<section id="scope"><div class="shead">'
        '<span class="dot" style="background:#c9a227"></span>'
        '<h2>What he narrowed <span class="tag">read this first</span></h2></div>'
        '<div class="note warn"><b>The single most useful thing he said is a scope cut.</b> '
        'Asked to go over the treatment of every condition mentioned under the antibiotics, he '
        'said that is not where the course is yet. The pneumonia and syphilis examples were '
        '<b>context</b>. What survives off that axis is <b>which bugs an agent covers</b> '
        '&mdash; and he named <b>MRSA, Pseudomonas and Clostridioides difficile</b> as the '
        'notable ones &mdash; plus whether it covers <b>anaerobes</b> or <b>atypicals</b>.'
        '<br><br><b>Dermatology is the exception</b>: there he does expect the antibiotic '
        'choice, and specifically <b>topical against oral</b>.</div>'
        '<div class="note"><b>This does not contradict Dr. McInnis.</b> On 28 August she said '
        'mechanism was over-weighted and that indications, patient education, side effects and '
        'contraindications should carry more. Dr. Wood is narrowing <i>one</i> axis for '
        '<i>this</i> paper &mdash; the infectious-disease indications that have not been taught '
        'yet. Side effects, patient education and contraindications are untouched by the cut, '
        'and his adverse-effect framework below is the clearest steer on this page.</div>'
        '</section>')

    for it in D.RULES:
        secs.append(entry(it, "#c9a227"))
    for it in D.ANSWERS:
        secs.append(entry(it, "#5566b5"))

    extra_css = """
  .asked{margin:0 0 10px;font-size:.88rem;color:var(--c-mute);font-style:italic;}
  blockquote.wq{margin:0 0 12px;padding:10px 14px;border-left:3px solid var(--gold);
    background:var(--c-ice);border-radius:0 8px 8px 0;}
  blockquote.wq p{margin:0;font-size:.95rem;}
  blockquote.wq footer{margin-top:6px;font-size:.72rem;color:var(--c-mute);}
  blockquote.wq .ts{font-variant-numeric:tabular-nums;}
"""
    legend = ('<span>Every quote is <b>verbatim from the review recording</b>, with its '
              'timestamp. Nothing here is inferred from the slides &mdash; the slides do not say '
              'what is being asked, and a review session does.</span>')
    notes = """    <div class="note"><b>What this page is.</b> On the evening before the paper the class
    put questions to Dr. Wood and he answered them. This is what he said, organised into the
    standing scope rules first and then the individual answers. It is a companion to
    <a href="pharm-exam-1-what-to-star.html">What Dr. Wood Told You to Star</a>, which is drawn
    from the three content lectures instead.</div>
    <div class="note warn"><b>On the quotes.</b> Drug names are repaired where the automatic
    transcript mis-hears them &mdash; it renders &ldquo;physostigmine&rdquo; as <i>Pfizer
    stigmine</i>, &ldquo;aminopenicillins&rdquo; as <i>immunopenicillins</i> and
    &ldquo;PANCE&rdquo; as <i>pants</i>. The wording, order and meaning are his. Every quote is
    checked against the transcript by <code>tools/check_pharm_review.py</code> before this page
    is written, with those corrections applied to the transcript rather than to the quote, so
    the check cannot be fooled by the cleanup.</div>"""
    toc = "".join('<a href="#%s">%s</a>' % (i, t) for i, t in
                  [("scope", "What he narrowed")] +
                  [(x["id"], x["title"]) for x in D.RULES] +
                  [(x["id"], x["title"]) for x in D.ANSWERS])

    html = page(
        title="Dr. Wood&rsquo;s Exam Review Session &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Class of 2028",
        h1="Dr. Wood&rsquo;s Exam Review Session",
        sub="Held the evening before the paper, 3 September 2026. %d standing scope rules and "
            "%d answered questions, each with the timestamp it came from. This is the only "
            "place he says what is and is not being asked."
            % (len(D.RULES), len(D.ANSWERS)),
        legend=legend, notes=notes, toc=toc, body="\n".join(secs),
        footer_note="Every quote is verified verbatim against the review recording by "
                    "<code>tools/check_pharm_review.py</code> before this page is written. "
                    "The recording stays on the course owner's machine and is never copied "
                    "into this repo.")
    html = html.replace("</style>", extra_css + "</style>")
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d rules, %d answers)"
          % (os.path.basename(OUT), len(html) // 1024, len(D.RULES), len(D.ANSWERS)))


if __name__ == "__main__":
    main()
