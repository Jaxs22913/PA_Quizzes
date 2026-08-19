#!/usr/bin/env python3
"""Apply Professor Jaquith's spoken emphasis from the 2026-08-19 General
Dermatology I recording to the CMS I Exam 1 study guide.

Source: four Notability recording segments, 08:07 to 10:39, 132.9 minutes total,
cross-checked against "2. General Dermatology I.pptx". Where the transcript and
the slide disagreed on a number, THE SLIDE WINS -- automatic speech recognition
mis-heard betamethasone dipropionate 0.05% as "0.5%", and that is exactly the
class of error a spoken-word source introduces.

Every mark below is something she said out loud that the slide alone does not
convey: a scope boundary, a stated exam intention, or an emphasis she returned
to. Nothing here is inferred from prosody alone.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
GUIDE = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1",
                     "cms-exam-1-study-guide.html")

# The two blocks that get inserted into section 2, and the anchor each follows.
SCOPE_BLOCK = """
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; what she said she will and will not ask</span>
  <table>
    <tr><th>She said</th><th>What it means for the exam</th></tr>
    <tr><td>&ldquo;I am going to expect you to know names from my class &mdash; I'm gonna be very clear which names &mdash; but I'm not expecting necessarily to know all the doses.&rdquo;</td>
        <td>Learn the agents she names. Do not memorise dosing.</td></tr>
    <tr><td>&ldquo;I would not make you guys memorize hundreds of brands of steroids.&rdquo;</td>
        <td>Only the seven agents on the potency table below are in scope.</td></tr>
    <tr><td>On the NAAT and polymerase chain reaction hierarchy: &ldquo;<mark class="prof-highlight">This is not going to be on your exam.</mark> This is just to help you for the future.&rdquo;</td>
        <td>Slides 30 and 31 are background. Know that a viral polymerase chain reaction detects viral genetic material; the taxonomy of RT-PCR, qPCR and multiplex is not examinable.</td></tr>
    <tr><td>&ldquo;I wouldn't actually have you interpret the picture.&rdquo;</td>
        <td>No image-interpretation questions. The written description is what you are tested on.</td></tr>
    <tr><td>On the Tzanck smear and mineral oil preparation: &ldquo;I've never seen this used clinically, however <mark class="prof-highlight">you need to know it because it could be on your board.</mark>&rdquo;</td>
        <td>Both are in scope despite being clinically obsolete.</td></tr>
    <tr><td>&ldquo;Make sure when you go over the PowerPoints, <mark class="prof-highlight">read headers</mark> &mdash; that's really important, because I'm separating here.&rdquo;</td>
        <td>The slide headers carry the organising structure of the material.</td></tr>
    <tr><td>&ldquo;These are like how your PANCE-style questions will be, so I want to make sure you guys understand what the expectation is.&rdquo;</td>
        <td>The four Knowledge Check vignettes at the end of the deck are the format of her exam questions. She worked all four in class.</td></tr>
  </table>
  <p class="src" style="margin-top:2px">Source: General Dermatology I lecture recording, 2026-08-19.</p>
  </div>
"""

STEROID_BLOCK = """
  <h3 class="sub" id="gd1-pharm">2.6 &middot; Common dermatologic pharmacology</h3>
  <p>Four families carry most of the treatment in this lecture: <strong>emollients and barrier
  preparations</strong>, <strong>topical corticosteroids</strong>, <strong>topical antifungals</strong>
  and <strong>topical retinoids</strong>. Topical corticosteroids are usually applied
  <strong>twice a day for two weeks</strong>; prolonged use causes atrophy, striae, telangiectasia and
  hypopigmentation, so potency is chosen by <em>site</em> and <em>severity</em>.</p>

  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; the seven steroids, and the question she said she would write</span>
  <table>
    <tr><th>Potency</th><th>Agent</th></tr>
    <tr><td><strong>Mild</strong></td><td><mark class="prof-highlight">Hydrocortisone &mdash; all strengths (0.1%, 0.5%, 1%, 2.5%)</mark></td></tr>
    <tr><td><strong>Moderate</strong></td><td>Betamethasone valerate 0.025%</td></tr>
    <tr><td><strong>Medium to high</strong></td><td>Triamcinolone acetonide 0.1% &middot; betamethasone valerate 0.1% &middot; betamethasone dipropionate 0.05%</td></tr>
    <tr><td><strong>High</strong></td><td>Clobetasol propionate 0.05%</td></tr>
  </table>
  <p>Her words: &ldquo;<mark class="prof-highlight">These are the ones I want you to know. If I give you a question and my slide says treatment would be a low dose corticosteroid, you might have these answer choices &mdash; you need to know that it's gonna be your hydrocortisone.</mark>&rdquo; She added that she reduced the list &ldquo;from a hundred to five &mdash; <em>this is true for my class only</em>&rdquo;, so do not carry the simplification into Pharmacology.</p>
  <p>The clinical rule she gave alongside it: <mark class="prof-highlight">a steroid on a sensitive area &mdash; the face or the genitals &mdash; should be hydrocortisone</mark>, or another low-potency agent. Betamethasone comes in two salts, <em>valerate</em> and <em>dipropionate</em>, and they sit at different potencies; the concentration alone does not tell you which tier an agent is in.</p>
  <p class="src" style="margin-top:2px">Source: <em>2. General Dermatology I.pptx</em>, Slides 39&ndash;44, and the lecture recording, 2026-08-19.</p>
  </div>

  <p>Topical <strong>retinoids</strong> &mdash; adapalene, tretinoin, tazarotene, trifarotene &mdash;
  treat acne and photoaging, and tazarotene also treats psoriasis. Start gradually because of
  irritation, dryness and photosensitivity, and observe pregnancy precautions. She was specific about
  the titration: begin at the lowest strength and work up to nightly use, and
  <strong>avoid the eyes, nose and mouth</strong>.</p>
"""

SKIN_TYPE_BLOCK = """
  <div class="prof-flag"><span class="prof-flag-label">&#9733; Professor emphasized &mdash; recognising these across skin types</span>
  <p>She spent real time on this and was direct about why. &ldquo;All the descriptions, all the
  textbooks, and <mark class="prof-highlight">what you're gonna be tested on, is gonna describe the
  rash on Caucasian skin</mark>. This is not a Dr Jaquith thing, this is a medicine thing, this is a
  history thing &mdash; medicine has not been nice to minorities. It is really important that
  <mark class="prof-highlight">you know how to identify all of these on every single skin type</mark>.&rdquo;
  She noted she had sourced images across ethnic groups for every condition in the deck bar one.</p>
  <table>
    <tr><th>Condition</th><th>On lighter skin</th><th>On darker skin</th></tr>
    <tr><td>Atopic dermatitis</td><td>Angry, inflamed, clearly erythematous</td><td>Can appear almost <strong>silvery</strong>; erythema is far less obvious</td></tr>
    <tr><td>Stasis dermatitis</td><td>Erythematous patches in the gaiter region</td><td>Erythema appears <strong>violaceous, grey or deep brown</strong>; palpate for warmth and oedema rather than relying on colour</td></tr>
    <tr><td>Pityriasis rosea</td><td>Salmon-coloured lesions, resolving without mark</td><td><strong>Post-inflammatory hyperpigmentation</strong> that can persist for months</td></tr>
    <tr><td>Lichen planus</td><td>Pink to violaceous flat-topped papules</td><td>Violaceous shades read as darker; the <em>flat-topped, shiny</em> quality and Wickham striae carry more weight than colour</td></tr>
  </table>
  <p>The practical consequence: on darker skin, stop using erythema as the primary signal and rely on
  <strong>palpation, distribution, lesion shape and secondary change</strong> instead. She also raised
  the <strong>Fitzpatrick scale</strong> here as the way skin type is classified.</p>
  <p class="src" style="margin-top:2px">Source: lecture recording, 2026-08-19, with <em>2. General Dermatology I.pptx</em>, Slides 114, 169 and 176.</p>
  </div>
"""


def main():
    s = open(GUIDE, encoding="utf-8").read()
    assert "gd1-pharm" not in s, "lecture marks already applied"
    before = len(s)

    # 1. scope block goes at the top of section 2, right after the IO box
    anchor = '  <h3 class="sub" id="gd1-anatomy">'
    assert s.count(anchor) == 1, "anatomy anchor not found"
    s = s.replace(anchor, SCOPE_BLOCK + "\n" + anchor)

    # 2. skin-type block after the eczema table, before the stasis pearl
    anchor2 = '  <div class="pearl"><strong>Stasis dermatitis versus cellulitis</strong>'
    assert s.count(anchor2) == 1, "stasis pearl not found"
    s = s.replace(anchor2, SKIN_TYPE_BLOCK + "\n" + anchor2)

    # 3. new pharmacology subsection at the end of section 2, i.e. immediately
    #    before that section's closing tag
    anchor3 = '</section>\n\n<!-- ============ 3 DERMATOLOGY II ============ -->'
    assert s.count(anchor3) == 1, "end of section 2 not found"
    s = s.replace(anchor3, STEROID_BLOCK + anchor3)

    # 4. table of contents entry
    toc_anchor = '  <a href="#gd1-alopecia">2.5 Objective c &mdash; Alopecia</a>\n'
    assert s.count(toc_anchor) == 1, "toc anchor not found"
    s = s.replace(toc_anchor, toc_anchor +
                  '  <a href="#gd1-pharm">2.6 &middot; Common dermatologic pharmacology</a>\n')

    open(GUIDE, "w", encoding="utf-8").write(s)

    for tag in ("style", "script", "section", "table", "div", "tr", "td", "th", "p", "h3"):
        o = len(re.findall(r"<%s[ >]" % tag, s))
        c = s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    bad = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a not in ids]
    assert not bad, "dangling anchors: %r" % bad
    print("guide: +%d bytes, 3 emphasis blocks and section 2.6 added" % (len(s) - before))
    print("tag balance and anchors verified")


if __name__ == "__main__":
    main()
