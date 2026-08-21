#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold the Microbiology Lecture 1 recording into the guide's section 1.

96.6 minutes across two segments, 21 August 2026, Dr. Webster. BOTH transcripts
read and diffed, every factual claim checked against the deck.

A third distinct lecturer profile. Jaquith signposts constantly and mis-states
quantifiers; Griffenkranz signposts with unusual precision and made no errors;
Webster signposts almost not at all -- ONE explicit de-emphasis in 96 minutes and
no exam-scope statements whatever. Nothing he said contradicts a slide. What the
recording adds is technique the deck does not carry.

Idempotent: fenced in <!--MICROL1AUDIO--> and stripped before re-inserting.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.join(os.path.dirname(HERE), "Microbiology Exam 1",
                     "micro-exam-1-study-guide.html")
OPEN, CLOSE = "<!--MICROL1AUDIO-->", "<!--/MICROL1AUDIO-->"

BLOCK = OPEN + '''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 21 August 2026</span>
  <p>96 minutes with Dr. Webster, across two segments. <b>Both transcripts were read and diffed</b>
  and every factual claim was checked against the deck. <b>Nothing he said contradicts a slide.</b></p>
  <p><b>This lecture barely signposts.</b> In 96 minutes there is <b>one</b> explicit de-emphasis and
  <b>no</b> statement at all about what will or will not be on the exam. That is worth knowing rather
  than hunting for: treat the thirteen instructional objectives as evenly weighted, because he gave no
  reason not to. What the recording does add is <b>laboratory technique the deck does not carry</b>.</p>

  <table>
    <tr><th>He said</th><th>What it means for you</th></tr>

    <tr><td><em>&ldquo;And then they have what we call the 70S ribosomes. What&rsquo;s that S?&hellip;
    It&rsquo;s a Svedberg unit. <mark class="prof-highlight">Oh, you don&rsquo;t have to write that
    down. I&rsquo;m not going to ask about that.</mark>&rdquo;</em> [20:07]</td>
    <td><b>The only de-emphasis in the lecture</b>, and it is in both transcripts. Know that a
    prokaryote has <b>70S ribosomes</b> and a eukaryote 80S &mdash; that contrast is on slide 14 and is
    the basis of selective antibiotic toxicity in Lecture 2. <b>The Svedberg unit itself is out of
    scope.</b> His aside that 70S is built from <b>30S and 50S subunits</b>, and that they do not add
    to 80 because a Svedberg unit reflects sedimentation rather than mass alone, is <b>not on the
    slides</b> either &mdash; useful for Pharmacology later, not something to revise for here.</td></tr>

    <tr><td><em>&ldquo;Does anyone remember a way to test for the organism&rsquo;s preferred level of
    oxygen?&hellip; a <mark class="prof-highlight">stab inoculation</mark>&hellip; does it grow at the
    top, right where the air-agar interface is? Then it&rsquo;s going to be obligate [aerobe]. Only at
    the bottom of the tube where there isn&rsquo;t any oxygen? Obligate anaerobic. Some grow all the
    way through that tube &mdash; facultative anaerobes or aerotolerant anaerobes.&rdquo;</em>
    [58:49]</td>
    <td><b>Deck content plus a technique the deck omits.</b> Slide 42 lists <b>oxygen levels</b> among
    the chemical requirements for growth, but not how you would determine one. His
    <b>thioglycolate stab</b> is the method, and it reads as a picture you could be shown:<br>
    <b>growth at the top</b> (air&ndash;agar interface) &rarr; obligate <b>aerobe</b><br>
    <b>growth only at the bottom</b> &rarr; obligate <b>anaerobe</b><br>
    <b>growth throughout the tube</b> &rarr; <b>facultative</b> anaerobe or <b>aerotolerant</b>
    anaerobe<br>
    Worth holding even though the medium is not named on a slide, because the underlying objective
    (physical and chemical requirements for growth) is.</td></tr>

    <tr><td><em>&ldquo;In a chemically defined medium you know exactly what&rsquo;s in that tube&hellip;
    we rarely use these in typical bacterial cultures, <mark class="prof-highlight">they&rsquo;re
    typically only used in research</mark>&hellip; most of the culture media that we use are
    complex&hellip; Trypticase soy agar comes from soybeans. Blood agar.&rdquo;</em> [1:01:10]</td>
    <td>Matches slide 43 &mdash; <b>synthetic (chemically defined)</b> against <b>complex or
    nonsynthetic</b>, which contains at least one ingredient that cannot be chemically defined. His
    addition is the practical weighting: defined media are a <b>research</b> tool, and what you will
    actually meet is complex. That makes the slide&rsquo;s definition concrete rather than abstract:
    soybean digest and blood are exactly the &ldquo;not chemically definable&rdquo; ingredients.</td></tr>

    <tr><td><em>&ldquo;They reproduce by binary fission. So every time they divide, they double&hellip;
    We don&rsquo;t go from one to two to three, we go one, two, four, eight, sixteen&hellip; and it
    leads to <mark class="prof-highlight">the bacterial growth curve. Remember this?</mark>&rdquo;</em>
    [1:05:57]</td>
    <td>Slides 48&ndash;50. The point he draws out is that <b>the curve&rsquo;s shape is the balance
    between growth and death</b>, not growth alone &mdash; which is what makes the stationary and
    decline phases make sense rather than being memorised. <b>Growth means an increase in NUMBER, not
    in cell size.</b></td></tr>

    <tr><td><em>&ldquo;It was an animal virus, which then mutated to be able to infect humans. We have
    never seen it before. <mark class="prof-highlight">Our immune system had never seen it
    before.</mark> So why did we have the problem we did?&rdquo;</em> [1:26:24]</td>
    <td>His worked example for the objective on <b>health implications of nucleic acid mutations</b>,
    using COVID and avian influenza. The chain to hold is <b>animal reservoir &rarr; mutation confers
    human transmissibility &rarr; no pre-existing population immunity &rarr; severe outbreak</b>. He
    was explicit that the origin debate is not the point &mdash; the mutation and the immunological
    naivety are.</td></tr>
  </table>
  <p class="tag">Quoted from the 21 August 2026 lecture recording, 96 minutes across two segments,
  with timestamps. Both transcripts read and diffed. No claim in this lecture contradicts a slide;
  the items that are his own addition rather than deck content are marked as such.</p>
  </div>
''' + CLOSE


def main():
    src = open(GUIDE, encoding="utf-8").read()
    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", src, flags=re.S)
    anchor = '  <h3 class="sub" id="gm-molecular">'
    assert src.count(anchor) == 1, "Micro Lecture 1 section not found"
    cand = src.replace(anchor, BLOCK + "\n" + anchor, 1)
    assert cand.count(OPEN) == 1 and cand.count(CLOSE) == 1
    for tag in ("table", "tr", "td", "th", "div", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, cand)); c = cand.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(cand)
    print("added the Microbiology Lecture 1 audio block (%d quoted rows)"
          % len(re.findall(r"<tr><td><em>", BLOCK)))


if __name__ == "__main__":
    main()
