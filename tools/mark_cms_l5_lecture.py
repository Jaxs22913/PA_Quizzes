#!/usr/bin/env python3
"""Fold the 2026-08-20 Dermatological Infestations recording into the CMS I
Exam 1 guide, cram sheet and Arcade deck.

Prof. Shah, 105 minutes across two segments. Every factual claim below was
audited against her deck before being recorded -- the delta-wing jet, the burrow
ink test, the albendazole and ivermectin regimens, the red-white-and-blue
hallmark, the hobo spider's aggression and its July-to-September mating season,
the 60-degree laundering and treating the whole household all appear on slides.
The ONE thing that does not is flagged as her clinical addition rather than
presented as deck content.

Idempotent: fenced in <!--CMSL5AUDIO--> and stripped before re-inserting.
"""
import os, re, sys, json, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
DIR = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 1")
GUIDE = os.path.join(DIR, "cms-exam-1-study-guide.html")
CRAM = os.path.join(DIR, "cms-exam-1-cram-sheet.html")
ARCADE = os.path.join(os.path.dirname(HERE), "arcade.js")
OPEN, CLOSE = "<!--CMSL5AUDIO-->", "<!--/CMSL5AUDIO-->"

BLOCK = OPEN + '''
  <div class="prof-flag"><span class="prof-flag-label">&#9733; From the lecture recording &mdash; 20 August 2026</span>
  <p>105 minutes with Professor Shah. <b>Every factual claim here was checked against her deck
  before being written down</b>, and they all hold; the one item that is <em>not</em> on a slide is
  labelled as such below rather than passed off as deck content.</p>
  <table>
    <tr><th>She said</th><th>What it means for you</th></tr>
    <tr><td><em>&ldquo;You will see surrounding scratch marks&hellip; but it leaves the flakes, no skin breakdown. So that&rsquo;s classic, and that&rsquo;s one way you&rsquo;re going to differentiate it. And you can&rsquo;t ask that history question. <mark class="prof-highlight">That&rsquo;ll be something you see on your exam.</mark>&rdquo;</em> [1:14:37]</td><td><b>The clearest exam flag in the lecture.</b> On the ground she would ask about travel and barefoot exposure; on paper you cannot, so <b>the exam has to give you the picture instead</b>. For cutaneous larva migrans that means the <b>serpiginous, advancing track</b> with scratch marks that flake but do not break the skin. Recognise it from the description, because the history will not be there to help.</td></tr>
    <tr><td><em>&ldquo;For this, it will be based on clinical findings&hellip; that serpiginous rash that I showed you, that is what you will see. That is a classic presentation&hellip; the other thing you can do is look at it under a light, but <mark class="prof-highlight">that would be a little bit more invasive than it needs to be</mark>.&rdquo;</em> [1:14:49]</td><td>Cutaneous larva migrans is a <b>clinical diagnosis</b>. She explicitly deprecates reaching for anything further once the serpiginous track is visible.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Albendazole, albendazole, albendazole</mark>, or you can do ivermectin&hellip; ivermectin has a lot of follow-up management&hellip; you have to draw labs, make sure that the liver is fine.&rdquo;</em> [1:15:14]</td><td>She said the drug name three times. Slide 54 gives the regimens: <b>albendazole 400&nbsp;mg by mouth daily for three days</b>, or <b>ivermectin 200&nbsp;micrograms per kilogram daily for one or two days</b>. Her addition is the <b>monitoring burden</b> that makes albendazole the easier choice.</td></tr>
    <tr><td><em>&ldquo;You&rsquo;ll see this <mark class="prof-highlight">delta wing jet</mark>&hellip; it means that there&rsquo;s a heavy area of mites and eggs in this region.&rdquo;</em> [31:02]</td><td>The dermoscopic sign in scabies, and it is on the slide as the <b>classic finding</b>: a dense scabies head, body, eggs and burrow. She notes you will practise with a dermatoscope in Physical Diagnosis lab.</td></tr>
    <tr><td><em>&ldquo;You would apply <mark class="prof-highlight">blue-black ink</mark> to the lesion&hellip; and the lesion would be <mark class="prof-highlight">non-excoriated</mark>, one they haven&rsquo;t gone in and scratched.&rdquo;</em> [31:25]</td><td>The burrow ink test, with the condition that makes it work. Excoriated lesions take up ink everywhere and tell you nothing. The three diagnostic routes on the slide are <b>skin scraping, dermoscopy and the burrow ink test</b>.</td></tr>
    <tr><td><em>&ldquo;This is part of your counseling&hellip; <mark class="prof-highlight">they need to know these steps.</mark> Otherwise&hellip; they&rsquo;re going to come back in X amount of days with the same symptoms, even if they&rsquo;re using the medications, because they&rsquo;re going to get re-infected. Whoever they&rsquo;re living with, <mark class="prof-highlight">you should treat them all.</mark>&rdquo;</em> [33:36]</td><td><b>Why treatment failure is usually not treatment failure.</b> Slide 18 backs the specifics: bedding and clothing washed at <b>60&nbsp;degrees Celsius</b>, or bagged in a warm place for <b>14 days</b>, and <b>treat every infected person in the family or group</b>. A patient returning with the same symptoms has usually been re-infected, not under-treated.</td></tr>
    <tr><td><em>&ldquo;You have your blue in the middle. You have your white around it. And then you have your red around that&hellip; <mark class="prof-highlight">that&rsquo;s like a hallmark sign</mark>&hellip; <mark class="prof-highlight">you have to be the one describing it, so make sure you&rsquo;re aware of what the words are for it.</mark>&rdquo;</em> [1:19:25]</td><td>The brown recluse bite, and the slide agrees: <b>hallmark &mdash; red, white and blue sign</b>. Her point about needing <em>the words</em> is worth taking literally: blue centre (ischaemia), white ring (vasoconstriction), red outer (inflammation). Then the progression she gives &mdash; <b>necrosis &rarr; eschar &rarr; ulceration</b>, and systemic symptoms such as nausea and vomiting mean escalation.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Hobo spider is an aggressive spider.</mark> We&rsquo;ve talked about three so far; two of them have not been aggressive. This one is aggressive.&rdquo;</em> [1:21:41]</td><td>Confirmed on the slide: <em>Tegenaria agrestis</em>, <b>aka the aggressive house spider</b>, often mistaken for a brown recluse, and the predominant cause of necrotic arachnidism in the Pacific Northwest. Black widow and brown recluse are the two non-aggressive ones. Bites <b>July to September</b> during mating; webs in <b>basements, wood piles and bushes</b>.</td></tr>
    <tr><td><em>&ldquo;<mark class="prof-highlight">Why do we need to know if they have seen the spider?</mark>&hellip; it can guide our treatment and we&rsquo;re not trying to guess what it is&hellip; It just means we fix our face and then we take care of our patient.&rdquo;</em> [1:21:53]</td><td>If a patient brings the spider in, that is useful rather than alarming &mdash; identification directs management instead of leaving you to infer it from the wound.</td></tr>
    <tr><td><em>&ldquo;Neck is the most common place.&rdquo;</em> [40:04]</td><td><b>Her clinical addition, not a slide fact.</b> Said answering a question about where to look for head lice. The deck gives the diagnostic method rather than the site &mdash; nits found by <b>nit combing and wet combing</b>, distinguished from dandruff because <b>nits cannot be removed from the hair shaft</b>, viable eggs tan to brown and hatched remains clear or white. Take the neck as a place to look first, not as something the deck will test.</td></tr>
  </table>
  <p class="tag">Quoted from the 20 August 2026 lecture recording, with timestamps. Where the audio and
  a slide disagree on a fact, the slide wins; every factual claim above was checked and holds.</p>
  </div>
''' + CLOSE

CRAM_ROWS = [
 ("HER CLEAREST EXAM FLAG", "On cutaneous larva migrans: “you CAN'T ask that history question. THAT'LL BE SOMETHING YOU SEE ON YOUR EXAM.” On paper you get the PICTURE, not the travel history — so recognise the SERPIGINOUS ADVANCING TRACK with scratch marks that FLAKE BUT DO NOT BREAK THE SKIN."),
 ("Cutaneous larva migrans — diagnosis and treatment", "CLINICAL diagnosis; she deprecates going further once the serpiginous track is visible. ALBENDAZOLE 400 mg PO daily × 3 DAYS (she said the name three times), or IVERMECTIN 200 mcg/kg daily × 1–2 days — but ivermectin needs FOLLOW-UP AND LIVER LABS, which is what makes albendazole the easier choice."),
 ("Scabies dermoscopy", "“DELTA-WING JET” — the classic finding, a dense area of mite head, body, eggs and burrow. You will practise with a dermatoscope in PD lab."),
 ("Burrow ink test — the condition that makes it work", "Apply BLUE-BLACK INK to a NON-EXCORIATED lesion. A scratched lesion takes up ink everywhere and tells you nothing. The three routes: SKIN SCRAPING, DERMOSCOPY, BURROW INK TEST."),
 ("Why 'treatment failure' usually isn't", "“They need to know these steps… otherwise they'll come back with the same symptoms EVEN IF THEY'RE USING THE MEDICATIONS, because they're going to get RE-INFECTED. WHOEVER THEY'RE LIVING WITH, YOU SHOULD TREAT THEM ALL.” Slide 18: bedding and clothing at 60°C, or bagged in a warm place for 14 DAYS, and treat every infected person in the family or group."),
 ("Brown recluse — and the words for it", "HALLMARK: RED, WHITE AND BLUE. BLUE centre (ischaemia), WHITE ring (vasoconstriction), RED outer (inflammation). “YOU HAVE TO BE THE ONE DESCRIBING IT, so make sure you're aware of what the words are.” Progression: NECROSIS → ESCHAR → ULCERATION; systemic symptoms (nausea, vomiting) mean escalate."),
 ("Which spider is the aggressive one", "THE HOBO. Tegenaria agrestis, “aka aggressive house spider”. The other two — black widow and brown recluse — are NOT aggressive. Often mistaken for a brown recluse; predominant cause of necrotic arachnidism in the PACIFIC NORTHWEST. Bites JULY TO SEPTEMBER during mating; webs in BASEMENTS, WOOD PILES, BUSHES."),
 ("If the patient brings the spider in", "That is USEFUL, not alarming — identification guides treatment instead of leaving you to guess from the wound. “We fix our face and then we take care of our patient.”"),
 ("Head lice — a clinical addition, not a slide fact", "She said “NECK IS THE MOST COMMON PLACE” to look. The DECK gives the method rather than the site: nits found by NIT COMBING and WET COMBING, distinguished from dandruff because NITS CANNOT BE REMOVED FROM THE HAIR SHAFT; viable eggs TAN TO BROWN, hatched remains CLEAR/WHITE."),
]

CARDS = [
 ["What did Professor Shah say you will see on the exam instead of a travel history?", "The picture — the serpiginous advancing track of cutaneous larva migrans."],
 ["How do the scratch marks of cutaneous larva migrans behave?", "They flake but do not break the skin."],
 ["What is first line for cutaneous larva migrans, and at what dose?", "Albendazole 400 milligrams by mouth daily for three days."],
 ["What follow-up does ivermectin need that albendazole does not?", "Review and blood tests to check the liver."],
 ["What is the delta-wing jet sign?", "A dermoscopic finding in scabies: a dense area of mite head, body, eggs and burrow."],
 ["What condition must a lesion meet for the burrow ink test to work?", "It must be non-excoriated. A scratched lesion takes up ink everywhere."],
 ["Name the three diagnostic routes for scabies.", "Skin scraping, dermoscopy, and the burrow ink test."],
 ["At what temperature must bedding and clothing be laundered to kill scabies mites?", "Sixty degrees Celsius, or bagged in a warm place for fourteen days."],
 ["Why does a scabies patient return with the same symptoms despite using the medication?", "They have been re-infected. Everyone they live with must be treated too."],
 ["Describe the red, white and blue sign in order from the centre out.", "Blue centre from ischaemia, white ring from vasoconstriction, red outer from inflammation."],
 ["How does a brown recluse bite progress if untreated?", "Necrosis, then eschar, then ulceration; systemic symptoms mean escalation."],
 ["Which of the three spiders is the aggressive one?", "The hobo spider, also called the aggressive house spider."],
 ["Where is the hobo spider the predominant cause of necrotic arachnidism?", "The Pacific Northwest of the United States."],
 ["When do hobo spider bites occur, and where are its webs?", "July to September during mating; webs in basements, wood piles and bushes."],
 ["Why is it useful if a patient brings the spider in?", "Identification guides treatment instead of leaving you to guess from the wound."],
 ["What colour are viable lice eggs compared with hatched remains?", "Viable eggs are tan to brown; hatched remains are clear, white or light."],
]


def main():
    g = open(GUIDE, encoding="utf-8").read()
    g = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), "", g, flags=re.S)
    i = g.index('id="derm-infestations"')
    j = g.index("</div>", g.index('<div class="io-box">', i))
    j = g.index("</div>", j + 6) + len("</div>")
    g = g[:j] + "\n\n  " + BLOCK + g[j:]
    assert g.count(OPEN) == g.count(CLOSE) == 1
    open(GUIDE, "w", encoding="utf-8").write(g)
    print("guide: Lecture 5 emphasis block added")

    c = open(CRAM, encoding="utf-8").read()
    if 'id="infest-lecture"' not in c:
        rows = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
                         for a, b in CRAM_ROWS)
        sec = ('\n  <section class="topic" id="infest-lecture" style="--acc:#8a3f4a;--acc-bg:#f3e3e6;'
               '--acc-zebra:#faf1f3;--acc-ink:#6d2f38">\n'
               '    <div class="shead"><span class="dot" style="background:#8a3f4a"></span>'
               '<h2>From the Infestations Lecture Recording</h2></div>\n'
               '    <div class="scroll">\n      <table>\n'
               '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
               '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n' % rows)
        m = re.search(r'      <a href="#infestations-2"[^>]*>.*?</a>\n', c, re.S)
        assert m, "infestations-2 jump link not found"
        link = ('      <a href="#infest-lecture" style="color:#6d2f38"><span class="dot" '
                'style="background:#8a3f4a"></span>From the Infestations Lecture</a>\n')
        c = c[:m.end()] + link + c[m.end():]
        j2 = c.index('<section class="topic" id="benign-mechanical"')
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
    if CARDS[0][0] in a:
        print("arcade: lecture cards already present")
        return
    deck = a[a.index('{ id: "cms-derm-infestations"'):]
    deck = deck[:deck.index("matchCards:")]
    def norm(t): return re.sub(r"[^a-z ]", "", t.lower()).strip()
    seen = {norm(json.loads(m)) for m in re.findall(r'\[("(?:[^"\\]|\\.)*"), ', deck)}
    dup = [x for x, y in CARDS if norm(x) in seen]
    assert not dup, "card already asked in this deck: %r" % dup
    i = a.index('{ id: "cms-derm-infestations"')
    j = a.index("cards: [", i) + len("cards: [")
    add = "\n" + "\n".join('      [%s, %s],' % (json.dumps(x, ensure_ascii=False),
                                                json.dumps(y, ensure_ascii=False)) for x, y in CARDS)
    a = a[:j] + add + a[j:]
    open(ARCADE, "w", encoding="utf-8").write(a)
    print("arcade: %d lecture cards added to cms-derm-infestations" % len(CARDS))


if __name__ == "__main__":
    main()
