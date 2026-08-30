#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build "What Dr. Wood Told You to Star" -- Pharmacology I Exam 1.

The fourth Pharmacology I reference, and the only one whose source is the
RECORDINGS rather than the slides. The decks do not say which facts he thinks
are testable; he told the class outright, about fifty times.

REFUSES TO WRITE unless check_pharm_wood.py passes.
"""
import os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from _pharm_ref_shell import page
import _pharm_wood_data as D

OUT = os.path.join(ROOT, "Pharmacology I Exam 1", "pharm-exam-1-what-to-star.html")
LEC = {1: "Lecture 1 &mdash; Antibiotics, Antivirals &amp; Antifungals",
       2: "Lecture 2 &mdash; Dermatology Medications",
       3: "Lecture 3 &mdash; ANS Pharmacology"}


def quote_block(q, at, lec, second=None):
    extra = ('<p class="q2">&hellip; and again: &ldquo;%s&rdquo;</p>' % second) if second else ""
    return ('<blockquote class="wq"><p>&ldquo;%s&rdquo;</p>%s'
            '<footer>Dr. Wood &middot; %s &middot; <span class="ts">%s</span></footer>'
            '</blockquote>' % (q, extra, LEC[lec], at))


def main():
    r = subprocess.run([sys.executable, os.path.join(HERE, "check_pharm_wood.py")],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        sys.exit("fact-check failed -- refusing to write the page")

    secs = []

    secs.append(
        '<section id="marker"><div class="shead"><span class="dot" style="background:#c9a227"></span>'
        '<h2>His own emphasis marker <span class="tag">he told the class what it is</span></h2></div>'
        '<div class="note"><b>He said this out loud, then used the marker relentlessly.</b> Counted '
        'across the three recordings: he says <b>&ldquo;notable&rdquo; 45 times in Lecture 1 alone</b> '
        '(46 across all three), plus <b>22 explicit instructions to star, underline or highlight</b> '
        'something. '
        'Every entry on this page is a place he used it, quoted with its timestamp so you can go '
        'back to the recording and hear it.</div>' + quote_block(D.MARKER["quote"], D.MARKER["at"],
                                                                 D.MARKER["lec"]) + '</section>')

    body = []
    for r_ in D.RULES:
        body.append('<div class="rule"><h3>%s <span class="said">said %s</span></h3>%s<p>%s</p></div>'
                    % (r_["title"], r_["said"],
                       quote_block(r_["quote"], r_["at"], r_["lec"], r_.get("second")), r_["body"]))
    secs.append('<section id="rules"><div class="shead"><span class="dot" style="background:#b3261e">'
                '</span><h2>The four standing rules <span class="tag">star these wherever they appear</span>'
                '</h2></div><div class="note warn">These are not facts about one drug. Each is an '
                'instruction to mark a <b>property</b> every time it shows up, across any class. That '
                'is what makes them worth more than any single row in the other charts.</div>'
                + "".join(body) + '</section>')

    body = []
    for p_ in D.PATTERNS:
        body.append('<div class="rule"><h3>%s</h3>%s<p>%s</p></div>'
                    % (p_["title"], quote_block(p_["quote"], p_["at"], p_["lec"]), p_["body"]))
    secs.append('<section id="patterns"><div class="shead"><span class="dot" style="background:#1f5d3a">'
                '</span><h2>Test-question shapes he gave outright <span class="tag">%d of them &mdash; he wrote the stem for you</span>'
                '</h2></div>' % len(D.PATTERNS) + "".join(body) + '</section>')

    body = []
    for s_ in D.STRATEGY:
        body.append('<div class="rule"><h3>%s</h3>%s%s</div>'
                    % (s_["title"], quote_block(s_["quote"], s_["at"], s_["lec"]),
                       ("<p>%s</p>" % s_["body"]) if s_.get("body") else ""))
    secs.append('<section id="strategy"><div class="shead"><span class="dot" style="background:#5b6472">'
                '</span><h2>How he says he writes the test <span class="tag">asked directly, answered directly</span>'
                '</h2></div>' + "".join(body) + '</section>')

    rows = "".join(
        '<tr><td class="dn">%s</td><td class="ct">%s</td>'
        '<td class="sl">L%d<br><span class="g">%s</span></td></tr>' % (d, w, lec, at)
        for d, w, at, lec, _v in D.STARRED)
    secs.append('<section id="starred"><div class="shead"><span class="dot"></span>'
                '<h2>Everything else he marked <span class="tag">%d items, in lecture order</span></h2></div>'
                '<div class="note">Each of these is a place he used the marker on a specific drug. '
                'The timestamp is where to find it if you want to hear the wording yourself.</div>'
                '<div class="scroll"><table><thead><tr><th class="dn-h">Drug or topic</th>'
                '<th>What he flagged</th><th class="sl-h">Where</th></tr></thead><tbody>%s</tbody>'
                '</table></div></section>' % (len(D.STARRED), rows))

    extra_css = """
  .wq{margin:12px 0 10px;padding:13px 16px;border-left:4px solid var(--gold);
    background:var(--ice);border-radius:0 11px 11px 0;}
  .wq p{margin:0;font-size:15.5px;line-height:1.5;font-style:italic;}
  .wq .q2{margin-top:8px;}
  .wq footer{margin-top:8px;font-size:12.5px;color:var(--muted);font-style:normal;font-weight:600;}
  .wq .ts{font-variant-numeric:tabular-nums;}
  .rule{background:var(--card);border:1px solid var(--line);border-radius:13px;
    padding:16px 18px;margin:0 0 14px;box-shadow:var(--shadow);}
  .rule h3{margin:0 0 4px;font-size:17px;color:var(--ink);letter-spacing:-.01em;}
  .rule > p{margin:6px 0 0;font-size:14.5px;}
  .said{font-size:12px;font-weight:600;color:var(--muted);letter-spacing:.02em;margin-left:6px;}
"""
    legend = ('<span>Everything on this page is a <b>direct quote</b> with the lecture and timestamp '
              'it came from. Nothing here is inferred from the slides &mdash; the slides do not say '
              'what he considers testable, and this is the only place that does.</span>')
    notes = """    <div class="note"><b>Why this page exists separately from the other three charts.</b>
    Contraindications, indications and side effects all come from the PowerPoints. This one comes
    from the <b>recordings</b>, because the decks are silent on which facts he weights. He is not.</div>
    <div class="note warn"><b>On the quotes.</b> They are lightly cleaned for reading &mdash; the
    automatic transcript renders &ldquo;teratogenic&rdquo; as <i>tritogenic</i>, &ldquo;PANCE&rdquo;
    as <i>pants</i> and &ldquo;nebivolol&rdquo; as <i>into bivolol</i>. The wording, order and
    meaning are his. Every quote is checked against the raw transcript by
    <code>tools/check_pharm_wood.py</code> before this page is written, matching the uncorrected
    text so the check cannot be fooled by the cleanup.</div>"""
    toc = "".join('<a href="#%s">%s</a>' % (i, t) for i, t in
                  (("marker", "His emphasis marker"), ("rules", "The four standing rules"),
                   ("patterns", "Test-question shapes"), ("strategy", "How he writes the test"),
                   ("starred", "Everything else he marked")))

    html = page(
        title="What Dr. Wood Told You to Star &mdash; Pharmacology I Exam 1 (Class of 2028)",
        kicker="Pharmacology I &middot; Exam 1 &middot; Class of 2028",
        h1="What Dr. Wood Told You to Star",
        sub="Taken from the lecture recordings, not the slides. He stated his own emphasis marker "
            "out loud, then said &ldquo;notable&rdquo; 45 times in Lecture 1 alone and gave 22 explicit "
            "instructions to star or underline something. Four standing rules, %d complete "
            "test-question shapes he handed over, %d quotes, each with its timestamp."
            % (len(D.PATTERNS),
               1 + len(D.RULES) + len(D.PATTERNS) + len(D.STRATEGY) + len(D.STARRED)),
        legend=legend, notes=notes, toc=toc, body="\n".join(secs),
        footer_note="Every quote is verified against the lecture transcript by "
                    "<code>tools/check_pharm_wood.py</code> before this page is written. "
                    "The recordings stay on Jaxon's machine and are never copied into this repo.")
    html = html.replace("</style>", extra_css + "</style>")
    open(OUT, "w", encoding="utf-8").write(html)
    print("wrote %s (%d KB, %d rules, %d patterns, %d strategy, %d starred)"
          % (os.path.basename(OUT), len(html) // 1024, len(D.RULES), len(D.PATTERNS),
             len(D.STRATEGY), len(D.STARRED)))


if __name__ == "__main__":
    main()
