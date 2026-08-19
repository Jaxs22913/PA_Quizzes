#!/usr/bin/env python3
"""Fold the 2026-08-19 General Dermatology I lecture emphasis into the CMS I
cram sheet and Arcade deck.

Facts from "2. General Dermatology I.pptx"; the recording decides what gets
weight, not what is true. Both the scope boundaries she stated and the steroid
potency table she said she would write a question about go in.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
CRAM = os.path.join(ROOT, "Clinical Medicine and Surgery I Exam 1", "cms-exam-1-cram-sheet.html")
ARCADE = os.path.join(ROOT, "arcade.js")

CRAM_TOPIC = ("derm-pharm-scope", "Topical Steroids, Testing & Exam Scope",
              "#b0642a", "#f4e7dc", "#faf2ec", "#8c4e20", [
 ("STEROID POTENCY — she said she'd ask this",
  "Mild: HYDROCORTISONE, all strengths (0.1/0.5/1/2.5%). Moderate: betamethasone valerate 0.025%. Medium-high: triamcinolone acetonide 0.1%, betamethasone valerate 0.1%, betamethasone dipropionate 0.05%. High: clobetasol propionate 0.05%."),
 ("Her exact words",
  "“If my slide says treatment would be a low dose corticosteroid, you might have these answer choices — you need to know that it's gonna be your hydrocortisone.”"),
 ("Sensitive sites", "Face or genitals → hydrocortisone or another LOW potency agent. Thin skin atrophies."),
 ("The betamethasone trap", "TWO salts. Valerate 0.025% = moderate; valerate 0.1% AND dipropionate 0.05% = medium-high. Concentration alone does not tell you the tier."),
 ("Steroid course", "Twice a day for two weeks. Prolonged use → atrophy, striae, telangiectasia, hypopigmentation."),
 ("Retinoids", "Adapalene, tretinoin, tazarotene, trifarotene. Tazarotene also treats psoriasis. Start low, build to nightly. AVOID eyes, nose, mouth. Pregnancy precautions."),
 ("NOT ON THE EXAM", "The NAAT / RT-PCR / qPCR / multiplex taxonomy (slides 30–31). Her words: “this is not going to be on your exam.” Know only that viral PCR detects viral genetic material."),
 ("Also not asked", "Image interpretation. “I wouldn't actually have you interpret the picture.” And no drug doses — names only."),
 ("IN scope though obsolete", "TZANCK SMEAR (vesicular lesions → multinucleated giant cells; PCR preferred to confirm) and MINERAL OIL PREP (scabies mite, eggs, faecal pellets). “Could be on your board, so you need to know about it.”"),
 ("Cultures", "Fungal culture identifies the fungal organism. Bacterial culture AND SENSITIVITY identifies the bacterium and tells you which antibiotic works."),
 ("Transillumination", "Fluid-filled vs solid nodule — fluid glows."),
 ("Direct immunofluorescence", "Autoimmune blistering disease — where the antibody sits. Separates bullous pemphigoid from pemphigus."),
 ("SKIN TYPE — she spent real time here",
  "“What you're gonna be tested on is gonna describe the rash on Caucasian skin… it is really important that you know how to identify all of these on every single skin type.”"),
 ("Atopic dermatitis by skin tone", "Lighter skin: angry, inflamed. Darker skin: can look almost SILVERY."),
 ("Stasis dermatitis by skin tone", "Darker skin: erythema reads VIOLACEOUS, GREY or DEEP BROWN. PALPATE for warmth and oedema — do not rely on colour."),
 ("Pityriasis rosea by skin tone", "Darker skin: post-inflammatory HYPERPIGMENTATION lasting several months. Still no scarring."),
 ("Fitzpatrick scale", "How skin type is classified by response to ultraviolet light."),
 ("Atopic triad", "Atopic dermatitis + asthma + allergic rhinitis."),
 ("Methotrexate", "ALWAYS with folic acid supplementation."),
 ("Lichen planus biopsy", "Buzzword: BAND-LIKE INFILTRATION OF LYMPHOCYTES in the dermis."),
 ("Read the headers", "“When you go over the PowerPoints, read headers — that's really important, because I'm separating here.”"),
])

ARCADE_CARDS = [
  ("Which topical corticosteroid is mild at every strength?", "Hydrocortisone."),
  ("Which topical corticosteroid sits in the moderate potency tier?", "Betamethasone valerate 0.025%."),
  ("Which three agents make up the medium to high potency tier?", "Triamcinolone acetonide 0.1%, betamethasone valerate 0.1% and betamethasone dipropionate 0.05%."),
  ("Which topical corticosteroid is the high potency agent?", "Clobetasol propionate 0.05%."),
  ("Which corticosteroid potency should be used on the face or genitals?", "Low potency, such as hydrocortisone."),
  ("Why does betamethasone appear in two different potency tiers?", "It comes as two salts, valerate and dipropionate, at different strengths."),
  ("How long is a usual topical corticosteroid course?", "Twice a day for two weeks."),
  ("Which adverse effects follow prolonged topical corticosteroid use?", "Atrophy, striae, telangiectasia and hypopigmentation."),
  ("Which topical retinoid also treats psoriasis?", "Tazarotene."),
  ("Which areas are avoided when applying a topical retinoid?", "The eyes, the nose and the mouth."),
  ("What does a bacterial culture and sensitivity add to a plain culture?", "It shows which antibiotic works best against the organism grown."),
  ("What does a fungal culture identify?", "The specific fungal organism."),
  ("What does transillumination distinguish?", "Whether a nodule is fluid-filled or solid."),
  ("What is direct immunofluorescence used to diagnose?", "Autoimmune blistering disease, by showing where antibody is deposited."),
  ("What is a dermatoscope used for?", "Magnified examination of a lesion's surface and pigment pattern."),
  ("How can atopic dermatitis look on darker skin?", "Almost silvery, rather than angry and inflamed."),
  ("How does stasis dermatitis erythema appear on darker skin?", "Violaceous, grey or deep brown."),
  ("What should be relied on when erythema is hard to see on darker skin?", "Palpation for warmth and oedema, plus distribution and secondary change."),
  ("Which residual change follows pityriasis rosea in darker-skinned patients?", "Post-inflammatory hyperpigmentation lasting several months."),
  ("Which scale classifies skin type by its response to ultraviolet light?", "The Fitzpatrick scale."),
  ("What is the atopic triad?", "Atopic dermatitis, asthma and allergic rhinitis."),
  ("Which supplement must always accompany methotrexate?", "Folic acid."),
  ("What does a biopsy show in lichen planus?", "A band-like infiltration of lymphocytes in the dermis."),
]


def cram_section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join('          <tr><td class="h">%s</td><td>%s</td></tr>'
                     % (H.escape(a), H.escape(b)) for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def js_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main():
    # ---- cram sheet
    s = open(CRAM, encoding="utf-8").read()
    assert 'id="derm-pharm-scope"' not in s, "cram topic already added"
    anchor = ('      <a href="#skin-layers" style="color:#0f5548"><span class="dot" '
              'style="background:#146b5c"></span>Skin Layers &amp; the Depth Ladder</a>\n')
    if anchor not in s:                      # the file stores it unescaped
        anchor = anchor.replace("&amp;", "&")
    assert s.count(anchor) == 1, "jump-link anchor not found"
    s = s.replace(anchor, anchor +
                  '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
                  % (CRAM_TOPIC[0], CRAM_TOPIC[5], CRAM_TOPIC[2], CRAM_TOPIC[1]))
    marker = '\n  <section class="topic" id="eczema-family"'
    assert s.count(marker) == 1, "insert marker not found"
    s = s.replace(marker, cram_section(CRAM_TOPIC) + marker)
    open(CRAM, "w", encoding="utf-8").write(s)
    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "cram %s: %d/%d" % (tag, o, c)
    ids = set(re.findall(r'id="([^"]+)"', s))
    bad = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a not in ids]
    assert not bad, "cram dangling links: %r" % bad
    print("cram: 1 topic, %d rows" % len(CRAM_TOPIC[6]))

    # ---- arcade
    a = open(ARCADE, encoding="utf-8").read()
    assert "Which topical corticosteroid is mild at every strength?" not in a, "cards already added"
    head = '  { id: "cms-general-derm-1", name: "General Dermatology I", color: "accent",'
    assert a.count(head) == 1, "deck not found"
    start = a.index(head)
    end = a.index("\n    ] },\n", start)
    deck = a[start:end]
    existing_ans = set(re.findall(r'\[".*?", "(.*?)"\]', deck))
    dup = [q for q, ans in ARCADE_CARDS if ans in existing_ans]
    assert not dup, "duplicate ANSWER against the live deck (breaks Match): %r" % dup[:3]
    ans_new = [x[1] for x in ARCADE_CARDS]
    assert len(set(ans_new)) == len(ans_new), "duplicate answer within the new cards"
    for q, _ in ARCADE_CARDS:
        assert q.endswith("?"), "not a question: %r" % q
    add = "".join("\n      [%s, %s]," % (js_str(q), js_str(x)) for q, x in ARCADE_CARDS).rstrip(",")
    a = a[:end] + "," + add + a[end:]
    open(ARCADE, "w", encoding="utf-8").write(a)
    print("arcade: %d cards added to cms-general-derm-1" % len(ARCADE_CARDS))


if __name__ == "__main__":
    main()
