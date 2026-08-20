#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fold the CMS Lecture 6 lecture recording into the guide's section 6.

104 minutes across two segments (43.1 + 60.9), 20 August 2026. BOTH transcripts
were read and diffed -- my own faster-whisper run and Notability's -- and every
factual claim was checked against the deck before being written down, per
Jaxon's standing rule that where the audio and a slide disagree, THE SLIDE WINS.

Idempotent: fenced in <!--CMSL6AUDIO--> and stripped before re-inserting.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                     "cms-exam-1-study-guide.html")
OPEN, CLOSE = "<!--CMSL6AUDIO-->", "<!--/CMSL6AUDIO-->"

BLOCK = OPEN + '''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 20 August 2026</span>
  <p>104 minutes across two segments. <b>Both transcripts were read and diffed</b> &mdash; a local
  transcription and Notability&rsquo;s &mdash; and every factual claim below was checked against the
  deck before being written down. <b>Where the audio and a slide disagree on a fact, THE SLIDE WINS.</b></p>

  <p class="prof-lead"><mark class="prof-highlight">Three topics were NOT covered in the live
  lecture.</mark> She ran out of time at the herpes simplex slides and said: <em>&ldquo;I only have two
  topics left&hellip; we have herpetic whitlow and then warts left&hellip; so what I&rsquo;ll do is
  I&rsquo;ll do a little recording for those last two topics for you guys. I&rsquo;ll upload them, just
  watch them at your convenience.&rdquo;</em> [1:33:24]</p>
  <p><b>Molluscum contagiosum was not covered either</b> &mdash; nine separate descriptors
  (umbilicated, pearly, poxvirus, molluscum, dimple, cheesy, curettage, cantharidin) return zero hits
  across <em>both</em> transcripts. So <b>herpetic whitlow, molluscum contagiosum and warts</b> are
  deck-only so far. Sections 6.6 and 6.7 above cover all three in full from the slides, and they are
  in the quizzes, the cram sheet and the comparison chart. <b>Watch for her supplementary
  recording.</b></p>

  <table>
    <tr><th>She said</th><th>What it means for you</th></tr>

    <tr><td><em>&ldquo;Hutchinson sign is where there is a lesion across the nose because of the way
    the dermatome works in the face, <mark class="prof-highlight">that facial nerve. That facial
    nerve, the one that innervates the eyes</mark>&hellip; anybody who has involvement of the V1,
    ophthalmic V1 cranial nerve, facial nerve&hellip;&rdquo;</em> [1:16:03]</td>
    <td><b>THE SLIDE DISAGREES, and this one matters.</b> Slide 103: herpes zoster ophthalmicus
    <b>&ldquo;involves the ophthalmic division (V1) of cranial nerve V&rdquo;</b> &mdash; the
    <b>trigeminal</b> nerve. The <b>facial</b> nerve is cranial nerve VII, and that is what
    <b>Ramsay Hunt</b> involves &mdash; which she describes correctly two minutes later as
    <em>&ldquo;peripheral facial paralysis with painful vesicles in the ear.&rdquo;</em> She names V1
    correctly and then attaches the wrong nerve to it. Both transcripts record the phrase three times,
    so it is not a transcription artifact. <b>Hold the contrast the deck draws:</b> zoster ophthalmicus
    = <b>V1 of the trigeminal (CN V)</b>; Ramsay Hunt = <b>facial (CN VII)</b>. Conflating them is
    exactly the discrimination an exam question would test.</td></tr>

    <tr><td><em>&ldquo;<mark class="prof-highlight">Every single medication we&rsquo;re gonna talk
    about today, antifungal, anything that treats fungus, you have to monitor liver enzymes.</mark>
    That&rsquo;s the biggest thing with those, and that&rsquo;s every single one of them.&rdquo;</em>
    [7:07]<br><br>&hellip;then 40 seconds later:<br><em>&ldquo;Before you ever start anybody
    <b>oral</b> antifungal agents, you have to make sure they don&rsquo;t have liver disease. And if
    I&rsquo;m starting anyone on oral antifungal for a <b>longer term period, like more than like a
    week</b>, I will make sure that I&rsquo;m doing <b>baseline</b> liver function tests.&rdquo;</em>
    [7:42]</td>
    <td><b>The opening sentence overstates; her own qualification is the one that matches the deck.</b>
    Slide 15 says obtain baseline liver tests <b>&ldquo;when indicated by the selected systemic agent,
    label, and patient risk&rdquo;</b>, and slide 52 <b>&ldquo;per labeling and patient risk&rdquo;</b>.
    That is <b>systemic agents, conditionally</b> &mdash; topical antifungals are not implicated at all,
    and it is a <b>baseline</b> test rather than ongoing monitoring. A student who hears only the first
    sentence will over-order labs on a patient using a cream. Her elaboration &mdash; oral, longer
    course, baseline &mdash; is right.</td></tr>

    <tr><td><em>&ldquo;Once therapy has begun, they can go back to school. They don&rsquo;t need to be
    out of school the entire time&hellip; so usually within like <mark class="prof-highlight">24 to 48
    hours</mark> after therapy, they can go back to school and they will not be contagious to their
    classmates.&rdquo;</em> [9:24]</td>
    <td><b>The framing matches the deck; the number is hers.</b> Slide 17 says only <b>&ldquo;school
    exclusion is generally unnecessary once effective therapy has begun; follow local policy.&rdquo;</b>
    <b>No 24-to-48-hour figure appears anywhere in the deck.</b> Take it as her clinical practice and a
    good answer to a parent, not as something the exam will key on.</td></tr>

    <tr><td><em>&ldquo;There is a ketoconazole oral tablet but <mark class="prof-highlight">I never
    prescribe that because liver toxicity is really, really high</mark> with that.&rdquo;</em>
    [7:23]</td>
    <td><b>Corroborates the deck.</b> Slide 82: <b>do not use oral ketoconazole</b> for superficial
    infection because <b>serious hepatic and adrenal toxicity outweigh benefit</b>. Useful framing:
    the objection to oral ketoconazole is a safety one, not an efficacy one.</td></tr>

    <tr><td><em>&ldquo;Topical or systemic corticosteroids do not prevent post-herpetic neuralgia and
    should never be used in replacement of antiviral therapy. <mark class="prof-highlight">That&rsquo;s
    really important to know.</mark>&rdquo;</em> [1:20:57]</td>
    <td><b>She flagged it out loud, and it is verbatim from slide 107.</b> This is the sentence to be
    able to state cold. Section 6.5 above carries it as its own line for that reason.</td></tr>

    <tr><td><em>&ldquo;It&rsquo;s a linear rash of grouped vesicles that <mark class="prof-highlight">does
    not cross midline</mark>&hellip; it&rsquo;s going to stop right in the middle.&rdquo;</em>
    [1:13:19]</td>
    <td>Confirms slide 100. She calls the back <b>&ldquo;the most classic&rdquo;</b> presentation,
    consistent with <b>thoracic 55%</b>.</td></tr>

    <tr><td><em>&ldquo;You do want to avoid aspirin in children and use caution with NSAIDs. So give
    them Tylenol for any type of fever, because fever is very common with that.&rdquo;</em>
    [1:04:06]</td>
    <td>Confirms slide 87. The acetaminophen preference is her addition and a sensible one.</td></tr>

    <tr><td><em>&ldquo;Erythematous patches of varying sizes with satellite lesions &mdash; and that is
    your <mark class="prof-highlight">buzzword</mark>.&rdquo;</em> [51:44]</td>
    <td>She used the word &ldquo;buzzword&rdquo; explicitly. <b>Satellite papules or pustules =
    <i>Candida</i></b>, from slide 68. It is the finding that separates candidal intertrigo from tinea
    cruris, which spares the scrotum.</td></tr>

    <tr><td><em>&ldquo;Someone comes in with otitis media and they&rsquo;re older&hellip; make sure to
    evaluate the ear canal very thoroughly. I had a colleague&hellip; they missed this diagnosis
    because <mark class="prof-highlight">the vesicles are actually inside the ear canal</mark>. They
    hadn&rsquo;t developed vesicles yet outside.&rdquo;</em> [1:17:46]</td>
    <td><b>Her clinical addition, not a slide fact</b> &mdash; and a good one. Ramsay Hunt can be missed
    because the vesicles are not yet visible externally. Pair it with the deck&rsquo;s reason for
    urgency: <b>hearing loss, tinnitus or vertigo</b>, and <b>protect the cornea</b> if eyelid closure
    is impaired.</td></tr>

    <tr><td><em>&ldquo;Even if you don&rsquo;t see lesions in the eye, still send them to an
    ophthalmologist&hellip; I don&rsquo;t have the proper equipment in my office to be able to see
    that.&rdquo;</em> [1:16:23]</td>
    <td>The practical version of slide 103&rsquo;s <b>&ldquo;its absence does not exclude eye
    involvement&rdquo;</b>. A normal-looking eye at the bedside is not reassurance.</td></tr>

    <tr><td><em>&ldquo;It inhibits growth and replication of the fungus. <mark class="prof-highlight">I
    will not test you on that. You will be tested on that pharmacology.</mark>&rdquo;</em>
    [0:22]</td>
    <td><b>A DE-EMPHASIS.</b> The ergosterol mechanism belongs to Pharmacology, not this exam. Know
    <b>which class an agent belongs to</b> &mdash; allylamine (&ldquo;-fine&rdquo;) versus azole
    (&ldquo;-azole&rdquo;) &mdash; and what that means for spectrum and choice, rather than the
    biochemistry.</td></tr>

    <tr><td><em>&ldquo;<mark class="prof-highlight">You must learn the generic names because
    that&rsquo;s what will be on your exam.</mark>&hellip; I know in the PowerPoint we have generic on
    there, but I&rsquo;ll put both.&rdquo;</em> [1:36:12]</td>
    <td><b>An explicit exam instruction.</b> Learn <b>generic</b> names; brand names may appear
    alongside them but the generic is what is keyed. Everything in this guide, the quizzes and the cram
    sheet is written generic-first for that reason, with brands in brackets where the deck gives one
    (Zelsuvmi, Ycanth, Lamisil, Gris-PEG).</td></tr>

    <tr><td><em>&ldquo;Anything that was presented in the lecture is fine.&rdquo;</em> [1:34:06]<br><br>
    <em>&ldquo;I promise you I am not a professor who&rsquo;s trying to trick you on the exam&hellip;
    I&rsquo;m not gonna give you nummular eczema and tinea corporis without giving you a lot of other
    background information.&rdquo;</em></td>
    <td><b>On scope and on style.</b> Scope is what the lecture presented. Style is <b>multi-clue
    stems</b> rather than one-line gotchas &mdash; a vignette will give you the supporting history and
    examination, not just the single discriminating word. The vignette sets are written that way.</td></tr>
  </table>
  <p class="tag">Quoted from the 20 August 2026 lecture recording, 104 minutes across two segments,
  with timestamps. Both transcripts read and diffed. Where the audio and a slide disagree on a fact,
  the slide wins &mdash; the two disagreements found are marked above.</p>
  </div>
''' + CLOSE


def main():
    src = open(GUIDE, encoding="utf-8").read()
    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", src, flags=re.S)

    anchor = '  <h3 class="sub" id="vf-koh">'
    assert src.count(anchor) == 1, "Lecture 6 section not found -- run add_cms_guide_l6.py first"
    cand = src.replace(anchor, BLOCK + "\n" + anchor, 1)

    # validate the candidate BEFORE writing
    assert cand.count(OPEN) == 1 and cand.count(CLOSE) == 1
    for tag in ("table", "tr", "td", "th", "div", "p"):
        o = len(re.findall(r"<%s[ >]" % tag, cand)); c = cand.count("</%s>" % tag)
        assert o == c, "%s unbalanced: %d open, %d close" % (tag, o, c)
    assert "@@" not in BLOCK
    open(GUIDE, "w", encoding="utf-8").write(cand)
    rows = len(re.findall(r"<tr><td><em>", BLOCK))
    print("added the Lecture 6 audio block (%d quoted rows) to guide section 6" % rows)


if __name__ == "__main__":
    main()
