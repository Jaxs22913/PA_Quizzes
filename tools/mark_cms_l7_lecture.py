#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold the CMS Lecture 7 recording into the guide's section 7.

107 minutes across two segments, 20 August 2026, Prof. Griffenkranz. BOTH
transcripts were read and diffed -- a local faster-whisper run and Notability's
-- and every factual claim was checked against the deck before being written
down, per the standing rule that where the audio and a slide disagree, the slide
wins.

A different profile from Jaquith's Lecture 6, and worth saying so: no factual
errors turned up here. What did turn up is unusually good exam intelligence --
he states outright what he will not ask, and once describes the SHAPE of a
question he intends to set. One characterisation is loose rather than wrong, and
one memorable aside is not deck content and is historically disputed; both are
marked as such.

Idempotent: fenced in <!--CMSL7AUDIO--> and stripped before re-inserting.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                     "cms-exam-1-study-guide.html")
OPEN, CLOSE = "<!--CMSL7AUDIO-->", "<!--/CMSL7AUDIO-->"

BLOCK = OPEN + '''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 20 August 2026</span>
  <p>107 minutes with Professor Griffenkranz, across two segments. <b>Both transcripts were read and
  diffed</b> and every factual claim below was checked against the deck. <b>No factual errors were
  found in this lecture</b> &mdash; what it carries instead is unusually direct exam intelligence: he
  says outright what he will <em>not</em> ask, and in one place describes the shape of a question he
  intends to set. The one loose characterisation and the one non-deck aside are both marked below.</p>

  <table>
    <tr><th>He said</th><th>What it means for you</th></tr>

    <tr><td><em>&ldquo;We all know the layers of the epidermis? Yes, of course you do.
    <mark class="prof-highlight">Am I going to ask you that? No. Do you need to know where things
    are? Yes.</mark>&rdquo;</em> [2:58]</td>
    <td><b>A DE-EMPHASIS, corroborated word-for-word in both transcripts.</b> Do not spend time
    memorising the strata of the epidermis. <b>Do</b> know <em>where</em> a lesion sits &mdash; which
    layer it involves and how deep it goes. That distinction is doing real work across this whole
    block: it is what separates a wart (epidermis only) from a corn, and what the entire pressure
    injury staging system is built on.</td></tr>

    <tr><td><em>&ldquo;What is the take-home point? <mark class="prof-highlight">Know the four phases
    of wound healing. At least be able to recognize them. If you&rsquo;re given a group of four,
    better know which one is one of the four phases of wound healing and which three are
    not.</mark>&rdquo;</em> [20:17]</td>
    <td><b>He described the QUESTION, not just the topic.</b> Expect four options where one is a real
    phase and three are not, and be able to pick it cold:
    <b>hemostasis &rarr; inflammation &rarr; proliferation &rarr; remodeling</b>. He tied it straight
    to the pathology as well &mdash; <em>&ldquo;if there&rsquo;s a disruption in any one of those
    phases, you will have abnormal wound healing&rdquo;</em> &mdash; which is the link to keloid and
    hypertrophic scar in 7.2.</td></tr>

    <tr><td><em>&ldquo;Look at the stages, one, two, three, four&hellip;
    <mark class="prof-highlight">You need to know these stages.</mark>&rdquo;</em> [48:44]<br><br>
    <em>&ldquo;The unstageable and deep tissue are just more complications of a stage four.
    <mark class="prof-highlight">I&rsquo;m not so worried about you knowing that</mark>, but I do want
    you to know the four stages of a pressure sore.&rdquo;</em> [49:47]</td>
    <td><b>The clearest steer in the lecture: learn 1&ndash;4 cold.</b> His own summary is a good
    revision target &mdash; stage 1 non-blanchable erythema of intact skin, stage 2 partial thickness,
    stage 3 <em>&ldquo;goes down to the fat&rdquo;</em>, stage 4 <em>&ldquo;full thickness down to the
    muscles, tendons, and bones&rdquo;</em>.<br><br>
    <b>But the slide does not support &ldquo;complications of a stage four&rdquo;.</b> On the staging
    tables, <b>unstageable</b> and <b>deep tissue injury</b> are their own categories, not a worse
    stage 4: <b>unstageable</b> is full-thickness loss whose extent <b>cannot be determined because
    slough or eschar obscures it</b>, and <b>deep tissue injury</b> is <b>persistent non-blanchable
    deep red or purple discolouration, with skin either intact or not</b>. Follow his steer on where
    to spend your effort, but do not carry away the definition &mdash; a question could reasonably ask
    you to tell those two apart.</td></tr>

    <tr><td><em>&ldquo;And then <mark class="prof-highlight">this is key</mark>. When everybody talks
    about a sign that&rsquo;s unique to a lesion, you&rsquo;ve got to remember it. It&rsquo;s the
    dimple sign&hellip; lateral pressure around the lesion, the center of the lesion invaginates or
    creates a dimple.&rdquo;</em> [1:02:21]</td>
    <td><b>Dermatofibroma</b>, and it matches the slide exactly. He also gave the rest of the picture:
    a <b>0.5 to 1&nbsp;cm nodule, hyperpigmented, with a halo</b>, and <b>&ldquo;mostly on the
    legs&rdquo;</b>, sometimes the arms. His general rule is worth taking literally &mdash; a named
    sign attached to one lesion is exam material by construction.</td></tr>

    <tr><td><em>&ldquo;Neurofibromatosis. Also known as von Recklinghausen disease.
    <mark class="prof-highlight">You need to know that.</mark>&hellip; comes in three types, type 1,
    type 2, and then type 3. Sometimes they&rsquo;re referred to as
    Schwannomatosis.&rdquo;</em> [1:34:19]</td>
    <td><b>Verbatim from slide 97</b>, including the three types: <b>NF1</b> (NF1 gene,
    <b>chromosome 17</b>), <b>NF2</b> (NF2 gene, <b>chromosome 22</b>), <b>schwannomatosis, sometimes
    called NF3</b> (<b>SMARCB1 and LZTR1</b>, chromosome 22). Section 7.7 carries all three with their
    genes.<br><br><b>His &ldquo;Elephant Man&rdquo; aside is not deck content</b>, and the association
    is disputed &mdash; Joseph Merrick is now generally thought to have had <b>Proteus syndrome</b>
    rather than neurofibromatosis. Keep it as a memory hook if it helps; do not carry it as a
    fact.</td></tr>

    <tr><td><em>&ldquo;Who would be at risk for developing pressure ulcers? Bedbound patients&hellip;
    elderly&hellip; diabetics&hellip; and people that are in a
    <mark class="prof-highlight">negative nitrogen balance</mark>&hellip; we want to be healing, we
    want to have all our proteins.&rdquo;</em> [48:10]</td>
    <td><b>His clinical addition, not a slide fact.</b> The deck&rsquo;s prevention slide asks for a
    <b>nutrition assessment</b> but never mentions nitrogen balance or malnutrition. The reasoning is
    sound and worth holding &mdash; a catabolic, protein-depleted patient cannot build granulation
    tissue &mdash; but it is his framing rather than something to quote back.</td></tr>

    <tr><td><em>&ldquo;Keloids are very prominent in dark-skinned races, very common in
    African-Americans and Latinos. <mark class="prof-highlight">Caucasians are not immune from
    keloids.</mark>&rdquo;</em> [20:40]</td>
    <td>The deck associates keloid with darker skin; his caveat is the useful nuance. Note also his
    timing: <em>&ldquo;sometimes it may happen weeks to months after the initial trauma&rdquo;</em>,
    which is exactly the discriminator against a hypertrophic scar (<b>within four weeks</b>, and
    <b>confined to the wound</b>).</td></tr>

    <tr><td><em>&ldquo;Most common on the trunk&hellip; small, about five millimetres, smooth, firm,
    deep red&hellip; <mark class="prof-highlight">that blanch with pressure</mark>.&rdquo;</em>
    [1:29:07]</td>
    <td><b>Cherry angioma, and correct</b> &mdash; slide 86 says <b>&ldquo;blanch with pressure (if
    fibrotic, may not blanch completely)&rdquo;</b>. Worth flagging because a blanching vascular
    papule is counter-intuitive if you have learned that vascular lesions do not blanch; the slide
    carries the caveat, so learn both halves. He also gave <b>pyogenic granuloma</b> as
    <b>head, neck and fingers</b>, painless but <b>bleeds easily</b>, after trauma.</td></tr>
  </table>
  <p class="tag">Quoted from the 20 August 2026 lecture recording, 107 minutes across two segments,
  with timestamps. Both transcripts read and diffed. Every factual claim was checked against the
  deck; the two items that are not deck content are marked as such above.</p>
  </div>
''' + CLOSE


def main():
    src = open(GUIDE, encoding="utf-8").read()
    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", src, flags=re.S)

    anchor = '  <h3 class="sub" id="bsl-mechanical">'
    assert src.count(anchor) == 1, "Lecture 7 section not found"
    cand = src.replace(anchor, BLOCK + "\n" + anchor, 1)

    assert cand.count(OPEN) == 1 and cand.count(CLOSE) == 1
    for tag in ("table", "tr", "td", "th", "div", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, cand)); c = cand.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    open(GUIDE, "w", encoding="utf-8").write(cand)
    print("added the Lecture 7 audio block (%d quoted rows) to guide section 7"
          % len(re.findall(r"<tr><td><em>", BLOCK)))


if __name__ == "__main__":
    main()
