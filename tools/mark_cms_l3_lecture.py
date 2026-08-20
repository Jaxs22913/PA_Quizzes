#!/usr/bin/env python3
"""Fold the 2026-08-19 Dermatology II recording into the CMS I Exam 1 guide,
cram sheet and Arcade deck.

The quizzes already carry this audio (cms_l3_pool_e). The guide, cram and Arcade
did not, which is the gap this closes.

Two statements in this lecture are worth more than anything else in it, and they
point in opposite directions:

  ON   "If you think it's different from any other disease, what's the
        likelihood it's going to be on the test? Probably pretty high." -- said
        while pointing at the one condition in the lecture that HAS a diagnostic
        test when the rest are clinical.
  OFF  "Don't worry, that's not going to be on the test. I won't do that to you.
        I'm not testing for lupus right now." -- the lupus-versus-rosacea
        distinction, taught and then explicitly excluded.

Idempotent: fenced in <!--CMSL3AUDIO--> and stripped before re-inserting.
"""
import os, re, sys, json, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "cms-exam-1-cram-sheet.html")
ARCADE = os.path.join(os.path.dirname(HERE), "arcade.js")
OPEN, CLOSE = "<!--CMSL3AUDIO-->", "<!--/CMSL3AUDIO-->"

BLOCK = OPEN + '''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 19 August 2026</span>
  <p>78 minutes of audio. Two statements in it point in opposite directions and are worth more than
  anything else in the lecture &mdash; one telling you what <em>is</em> on the exam, one telling you
  what is not.</p>
  <p><b>Standing rule for anything taken from these recordings: where the audio and the slide
  disagree on a fact, THE SLIDE WINS.</b> Words get said wrong in a live lecture, and one claim in
  this one is wrong &mdash; it is kept below with the correction attached rather than quietly
  removed, because knowing <em>which</em> spoken facts to distrust is itself worth having. What the
  recording is authoritative for is <b>emphasis</b>: what she flagged, what she excluded, and the
  mechanisms she explains that the slide only asserts.</p>
  <table>
    <tr><th>She said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;This is different&hellip; <mark class="prof-highlight">if you think it&rsquo;s different from any other disease, what&rsquo;s the likelihood it&rsquo;s going to be on the test? Probably pretty high.</mark> There&rsquo;s not many I can do diagnostic testing on, since they&rsquo;re all clinical&hellip; <mark class="prof-highlight">it&rsquo;s likely going to be on the test, just trying to help you a lot.</mark>&rdquo;</em> [12:35]</td><td><b>Said while pointing at dermatitis herpetiformis</b>, and it is a rule for the whole lecture, not one condition. Almost everything here is a clinical diagnosis. The handful that are <em>not</em> are therefore the memorable ones, and she said outright that being different is what makes something testable. <b>Dermatitis herpetiformis: skin biopsy is the gold standard.</b></td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Don&rsquo;t worry. That&rsquo;s not going to be on the test. I won&rsquo;t do that to you. I&rsquo;m not testing for lupus right now</mark>&hellip; but that is one of, like, clinically, I want you know, one of the big ways to tell &mdash; is this lupus, is this rosacea?&rdquo;</em> [44:18]</td><td><b>Explicitly excluded.</b> She taught the lupus-versus-rosacea distinction and then took it off the exam in the same breath. Worth knowing clinically and worth <em>not</em> spending revision time on: the lupus butterfly rash <b>spares the nasolabial folds</b>; rosacea involves them. And on the antinuclear antibody test &mdash; a negative result lowers the probability, a positive one only means <b>more testing</b>, because plenty of things make it positive.</td></tr>
    <tr><td><em>&ldquo;Dapsone&hellip; we also want to check the glucose-6-phosphate dehydrogenase deficiency. This is a condition you cannot take dapsone in.&rdquo;</em> [13:45]</td><td>The full dermatitis herpetiformis package, and the deck does not spell all of it out: <b>dapsone acutely</b>, but <b>check for glucose-6-phosphate dehydrogenase deficiency first</b> because it is a contraindication; <b>strict gluten-free diet</b> long term; <b>refer to gastroenterology for colonoscopy</b>, because there is a high chance of coeliac disease; and <b>refer to a registered dietitian</b>.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Metronidazole, by far the first line treatment</mark>&hellip; azelaic acid can be effective, you do have to watch, as azelaic acid can be a little bit more drying&hellip; these patients already have impaired barrier.&rdquo;</em> [44:58]</td><td><b>Topical metronidazole is first line for rosacea.</b> Azelaic acid is an alternative but is drying, and these patients already have a compromised barrier. If it is really bad, <b>low-dose doxycycline</b> &mdash; started twice daily and stepped down to once.</td></tr>
    <tr><td><em>&ldquo;This is by far the classic presentation, <mark class="prof-highlight">the one that I want you to really know about</mark>.&rdquo;</em> [37:36]</td><td>On <b>pyoderma gangrenosum</b>. The presentation she wants: begins as a small pustule or nodule, becomes a <b>rapidly expanding painful ulcer with a well-undermined border</b>, and the <b>lower extremity is the most common site</b>.</td></tr>
    <tr><td><em>&ldquo;Allopurinol is the most common cause <b>worldwide</b> of this&hellip; it&rsquo;s drug induced in 80% of cases.&rdquo;</em> [57:15]</td><td><b>Half right, and the slide is the half to trust.</b> The proportion is correct &mdash; slide 87 says toxic epidermal necrolysis is <b>drug-induced in more than 80% of cases</b>. But the slide says allopurinol is <b>&ldquo;the most common cause <u>in Asia</u>&rdquo;</b>, not worldwide, and it is one of several leading culprits alongside the aromatic anticonvulsants, sulfonamides, oxicam non-steroidals and nevirapine. <b>Go with the slide.</b></td></tr>
    <tr><td><em>&ldquo;I&rsquo;ve never seen it, but <mark class="prof-highlight">you need to know it</mark>, in case you happen to be one of those&hellip; what I want you to know: this is caused by a mutation in structural proteins.&rdquo;</em> [20:58]</td><td>On <b>epidermolysis bullosa</b>. Rare enough that she has not seen a case, and flagged anyway &mdash; and what she wants from it is the <b>mechanism</b>, a structural protein mutation, rather than a clinical picture.</td></tr>
    <tr><td><em>&ldquo;Epinephrine, or EpiPen, is a brand name for that&rdquo; &mdash; introduced as the <mark class="prof-highlight">take-home</mark></em> [27:26]</td><td>On urticaria and angioedema. She marked this one as the take-home point of that section.</td></tr>
    <tr><td><em>&ldquo;Anywhere from one to five centimetres, on anterior shins or your tibial surface, is the most common&rdquo;</em> [31:23]; <em>&ldquo;strep throat&hellip; which is the most common form of it&rdquo;</em> [30:50]</td><td>Erythema nodosum: <b>1&ndash;5&nbsp;cm, anterior shins</b>, and <b>streptococcal pharyngitis is the commonest trigger</b>.</td></tr>
    <tr><td><em>&ldquo;The most common idiopathic photodermatosis&hellip; particularly young middle-aged women&hellip; higher altitudes&rdquo;</em> [1:06:36]</td><td>Polymorphous light eruption. Three discriminators in one sentence: commonest of its class, the demographic, and the altitude association.</td></tr>
  </table>
  <p class="tag">Quoted from the 19 August 2026 lecture recording, with timestamps, and cross-examined
  against Notability&rsquo;s independent transcript. Where the recording and a slide disagree on a
  number, the slide wins.</p>
  </div>
''' + CLOSE

CRAM_ROWS = [
 ("HER RULE FOR WHAT IS TESTABLE", "“If you think it's DIFFERENT from any other disease, what's the likelihood it's going to be on the test? PROBABLY PRETTY HIGH.” Said while pointing at dermatitis herpetiformis — because almost everything else in this lecture is a CLINICAL diagnosis, and the few that are not stand out."),
 ("EXPLICITLY NOT ON THE EXAM", "The LUPUS-versus-ROSACEA distinction. “Don't worry, that's not going to be on the test. I won't do that to you. I'm not testing for lupus right now.” Worth knowing clinically — lupus butterfly rash SPARES the nasolabial folds, rosacea involves them; ANA can rule OUT but a positive only means MORE TESTING — and worth not revising."),
 ("Dermatitis herpetiformis — the full package", "GOLD STANDARD = SKIN BIOPSY (one of the very few here that is not purely clinical). ACUTE: DAPSONE — but CHECK FOR G6PD DEFICIENCY FIRST, it is a contraindication. CHRONIC: STRICT GLUTEN-FREE DIET. REFER to GASTROENTEROLOGY for COLONOSCOPY (high chance of coeliac disease) and to a REGISTERED DIETITIAN."),
 ("Rosacea first line — her words", "TOPICAL METRONIDAZOLE, “by far the first line treatment”. AZELAIC ACID is an alternative but is DRYING, and these patients already have an IMPAIRED SKIN BARRIER. If really bad: LOW-DOSE DOXYCYCLINE, started twice daily and stepped down to once."),
 ("Pyoderma gangrenosum — “the one I want you to really know”", "Begins as a small PUSTULE or NODULE → RAPIDLY EXPANDING PAINFUL ULCER with a WELL-UNDERMINED BORDER. LOWER EXTREMITY is the most common site."),
 ("Toxic epidermal necrolysis — and a Jaquith correction", "DRUG INDUCED IN MORE THAN 80% OF CASES (slide 87). She said allopurinol is the commonest cause WORLDWIDE — the SLIDE says commonest IN ASIA, one of several leading culprits alongside aromatic anticonvulsants, sulfonamides, oxicam NSAIDs and nevirapine. GO WITH THE SLIDE."),
 ("Epidermolysis bullosa — flagged despite being rare", "“I've never seen it, but YOU NEED TO KNOW IT.” What she wants is the MECHANISM: a MUTATION IN STRUCTURAL PROTEINS."),
 ("Erythema nodosum numbers", "1–5 CM nodules on the ANTERIOR SHINS / tibial surface. STREPTOCOCCAL PHARYNGITIS is the most common trigger."),
 ("Polymorphous light eruption", "The MOST COMMON IDIOPATHIC PHOTODERMATOSIS. Particularly YOUNG TO MIDDLE-AGED WOMEN. Associated with HIGHER ALTITUDES."),
 ("Urticaria / angioedema take-home", "EPINEPHRINE — EpiPen is the brand name. She named this the take-home of the section."),
]

CARDS = [
 ["What makes something likely to be on this exam, in her words?", "If it is different from every other disease. Most of this lecture is clinical diagnosis, so the exceptions stand out."],
 ["Which distinction did she say outright would NOT be tested?", "Lupus versus rosacea. 'I'm not testing for lupus right now.'"],
 ["Clinically, how does the lupus butterfly rash differ from rosacea?", "Lupus spares the nasolabial folds; rosacea involves them."],
 ["What does a positive antinuclear antibody test tell you?", "Only that more testing is needed. It can rule out an autoimmune condition, not rule one in."],
 ["What is the gold standard test for dermatitis herpetiformis?", "Skin biopsy."],
 ["What must be checked before starting dapsone?", "Glucose-6-phosphate dehydrogenase deficiency, which is a contraindication."],
 ["What is the long-term management of dermatitis herpetiformis?", "A strict gluten-free diet, with referral to gastroenterology for colonoscopy and to a registered dietitian."],
 ["What is first line for rosacea?", "Topical metronidazole, by far."],
 ["Why is azelaic acid a cautious choice in rosacea?", "It is drying, and these patients already have an impaired skin barrier."],
 ["What is used for severe rosacea?", "Low-dose doxycycline, started twice daily and stepped down to once daily."],
 ["Describe the classic pyoderma gangrenosum lesion.", "A small pustule or nodule becoming a rapidly expanding painful ulcer with a well-undermined border."],
 ["Where is pyoderma gangrenosum most common?", "The lower extremity."],
 ["What proportion of toxic epidermal necrolysis is drug induced?", "Eighty per cent."],
 ["What causes epidermolysis bullosa?", "A mutation in structural proteins."],
 ["What size are erythema nodosum lesions, and where?", "One to five centimetres, on the anterior shins or tibial surface."],
 ["What is the most common trigger of erythema nodosum?", "Streptococcal pharyngitis."],
 ["Which is the most common idiopathic photodermatosis, and in whom?", "Polymorphous light eruption, particularly in young to middle-aged women, and at higher altitudes."],
]


def main():
    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", g, flags=re.S)
    i = g.index('id="general-derm-2"')
    j = g.index("</div>", g.index('<div class="io-box">', i))
    j = g.index("</div>", j + 6) + len("</div>")
    g = g[:j] + "\n\n  " + BLOCK + g[j:]
    assert g.count(OPEN) == g.count(CLOSE) == 1
    open(GUIDE, "w", encoding="utf-8").write(g)
    print("guide: Lecture 3 emphasis block added")

    c = open(CRAM, encoding="utf-8").read()
    if 'id="derm2-lecture"' not in c:
        rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
                         for a, b in CRAM_ROWS)
        sec = ('\n  <section class="topic" id="derm2-lecture" style="--acc:#8a3f4a;--acc-bg:#f3e3e6;'
               '--acc-zebra:#faf1f3;--acc-ink:#6d2f38">\n'
               '    <div class="shead"><span class="dot" style="background:#8a3f4a"></span>'
               '<h2>From the Dermatology II Lecture Recording</h2></div>\n'
               '    <div class="scroll">\n      <table>\n'
               '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
               '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n' % rows)
        m = re.search(r'      <a href="#sjs-ten"[^>]*>.*?</a>\n', c, re.S)
        assert m, "sjs-ten jump link not found"
        link = ('      <a href="#derm2-lecture" style="color:#6d2f38"><span class="dot" '
                'style="background:#8a3f4a"></span>From the Dermatology II Lecture</a>\n')
        c = c[:m.end()] + link + c[m.end():]
        j2 = c.index('<section class="topic" id="bacterial-acne"')
        j2 = c.rindex("\n", 0, j2)
        c = c[:j2] + sec + c[j2:]
        for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
            o, cl = len(re.findall(r"<%s[ >]" % tag, c)), c.count("</%s>" % tag)
            assert o == cl, "%s: %d open, %d close" % (tag, o, cl)
        ids = set(re.findall(r'id="([^"]+)"', c))
        assert not [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', c) if a not in ids]
        assert "**" not in c
        open(CRAM, "w", encoding="utf-8").write(c)
        print("cram: %d lecture rows added" % len(CRAM_ROWS))
    else:
        print("cram: lecture rows already present")

    a = open(ARCADE, encoding="utf-8").read()
    marker = '"What makes something likely to be on this exam, in her words?"'
    if marker in a:
        print("arcade: lecture cards already present")
        return
    # A shared ANSWER VALUE is not a problem -- that is an engine concern and
    # the engines already handle it: Match groups the definitions column by text
    # and keeps a shared tile alive until its last pairing is used, and
    # Learn/Sprint exclude any distractor equal to the correct answer. The
    # standing rule is never to distort deck content to avoid repeated values.
    #
    # What IS a problem is a REDUNDANT CARD -- the same question asked twice in
    # slightly different words, which is noise for the student rather than a
    # bug. So this checks the FRONTS, not the backs.
    deck = a[a.index('{ id: "cms-derm-2"'):]
    deck = deck[:deck.index("matchCards:")]
    fronts = {json.loads(m) for m in re.findall(r'\[("(?:[^"\\]|\\.)*"), ', deck)}
    def norm(t):
        return re.sub(r"[^a-z ]", "", t.lower()).replace("what is the ", "").strip()
    seen = {norm(f) for f in fronts}
    dupes = [x for x, y in CARDS if norm(x) in seen]
    assert not dupes, "card already asked in this deck: %r" % dupes

    i = a.index('{ id: "cms-derm-2"')
    j = a.index("cards: [", i) + len("cards: [")
    add = "\n" + "\n".join('      [%s, %s],' % (json.dumps(x, ensure_ascii=False),
                                                json.dumps(y, ensure_ascii=False)) for x, y in CARDS)
    a = a[:j] + add + a[j:]
    open(ARCADE, "w", encoding="utf-8").write(a)
    print("arcade: %d lecture cards added to cms-derm-2" % len(CARDS))


if __name__ == "__main__":
    main()
