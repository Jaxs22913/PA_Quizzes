#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build SUBJECT-level flashcard decks: every disease process in one subject,
with its defining features as the answer.

Jaxon, 2026-08-20: "can you also make flashcard sets for each subject (such as
Derm) and its like all the disease processes and then the def is how its
described/looks/defining features"

Different from the per-lecture decks, which follow one PowerPoint each. This is
the whole subject in one place, so you can drill "what does X look like" across
the entire block without picking a lecture first -- which is how the exam asks
it, and how a patient presents.

SOURCE. The dermatology comparison chart already holds exactly this: 135
conditions, each with a "Common manifestation and how a patient may describe it"
cell written from the lecture slides. Generating from that rather than
re-authoring means the flashcards cannot drift from the chart or the guides, and
every card inherits the same slide-grounding.

The patient-quote sentence is dropped: it is a lovely thing to read in a wide
table and far too long for a card back.

FLASHCARDS ONLY -- no curated matchCards, on purpose.

Match wants a definition of about nine words. Compressing a manifestation cell
that far was tried and abandoned: the first clause of a description is very
often NOT the description. It produced "Borrelia burgdorferi, a spirochete"
(etiology), "Females more than males" (demographics), "NOT considered
contagious" (transmission) and "Also called acne inversa" (a synonym). Filtering
hard enough to keep only genuine morphology left 22 of 135 conditions -- so a
Match round on this deck would have silently drilled 16% of the subject while
looking like it covered all of it.

Arcade's Match already falls back to `cards` when a deck has no matchCards, so
the deck still plays in every mode; the tiles just carry the full description.
Complete and wordy beats compressed and wrong. The per-lecture decks keep their
hand-written match pairs for the tight, fast version.

    python3 tools/build_subject_flashcards.py           # write into arcade.js
    python3 tools/build_subject_flashcards.py --dry     # print, change nothing
"""
import os, re, sys, json
import html as _html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import build_cms_derm_chart as CHART

ARCADE = os.path.join(ROOT, "arcade.js")
CARD_BACK_MAX_WORDS = 26        # matches the guard the per-lecture builders use
MATCH_DEF_MAX_WORDS = 9


def plain(html):
    """Chart cell -> plain sentence text, minus the patient quote."""
    s = re.sub(r'<span class=pt>.*?</span>', ' ', html or '', flags=re.S)
    s = re.sub(r'<br\s*/?>', ' ', s)
    s = re.sub(r'<[^>]+>', '', s)
    # Decode every entity, not a hand-maintained list -- "&rarr;" was not on the
    # list and leaked into cards as a bare "&rarr".
    s = _html.unescape(s)
    return " ".join(s.split())


def clean_name(html):
    """Condition name, keeping any disambiguating badge text.

    Stripping the <span class="dup"> badge collapsed two different chart rows
    into one key when the chart was built; the same trap applies here.
    """
    return plain(html)


def trim_words(text, limit):
    w = text.split()
    if len(w) <= limit:
        return text
    return " ".join(w[:limit]).rstrip(" ,;:—-") + "…"


def sentences(desc):
    """Split into sentences without breaking on a genus abbreviation.

    "Dermatophytes — especially T. rubrum — cause most cases" was being cut at
    "T." and shipped as the card "Dermatophytes — especially T".
    """
    guarded = re.sub(r'\b([A-Z])\.\s+(?=[a-z])', r'\1<DOT> ', desc)
    return [p.replace('<DOT>', '.') for p in re.split(r'(?<=[.!?])\s+', guarded)]


# A leading sentence that only POINTS somewhere else -- "The same spectrum, at
# its severe end.", "Also called acne inversa.", "The more common form." -- reads
# fine in a chart where the row above supplies the referent, and says nothing on
# a standalone card. Dropped, but only when SHORT: the soft-corn entry opens
# "Same pressure mechanism, but sited in the fourth-to-fifth toe web space...",
# which is anaphoric and also the defining fact, so a blanket rule would delete
# the answer.
_POINTER = re.compile(r"^(the same|same\b|this|these|those|it|they|also called|"
                      r"also known|the more common|the most common form|"
                      r"the commonest form|the commonest|a variant|a form of|"
                      r"hence|as above|likewise)\b", re.I)
POINTER_MAX_WORDS = 8


def drop_pointer_opener(parts):
    while (len(parts) > 1 and _POINTER.match(parts[0].strip())
           and len(parts[0].split()) <= POINTER_MAX_WORDS):
        parts = parts[1:]
    return parts


def card_back(desc):
    """First sentence or two of the description, capped for a card back."""
    parts = drop_pointer_opener(sentences(desc))
    out = parts[0]
    if len(out.split()) < 12 and len(parts) > 1:
        out = out + " " + parts[1]
    return trim_words(out.strip(), CARD_BACK_MAX_WORDS)


# A short phrase is not automatically a DESCRIPTION. Naive first-clause
# extraction produced "which is what separates it from acne vulgaris", "The same
# spectrum, at its severe end", "Also called acne inversa" and "The more common
# form" -- all fine mid-sentence in a wide table, all meaningless on a card that
# is supposed to say what the thing LOOKS like. Anaphora, synonyms and bare
# epidemiology are rejected; a Match card has to stand on its own.
_MORPH = re.compile(
    r"\b(papule|papules|plaque|plaques|macule|macules|patch|patches|vesicle|"
    r"vesicles|bulla|bullae|pustule|pustules|nodule|nodules|ulcer|ulcers|"
    r"wheal|wheals|scale|scaly|scaling|crust|crusted|erythema|erythematous|"
    r"lesion|lesions|eruption|rash|blister|blisters|papulo\w*|annular|"
    r"umbilicat\w+|verrucous|hyperkeratot\w+|lichenif\w+|excoriat\w+|"
    r"pigment\w*|hypopigment\w+|hyperpigment\w+|velvety|greasy|silvery|"
    r"target|burrow|burrows|comedone|comedones|cyst|cysts|abscess|"
    r"telangiectas\w+|purpur\w+|petechia\w*|induration|indurated|"
    r"fluctuant|boggy|dome-shaped|pedunculated|thickening|atroph\w+)\b", re.I)

_REJECT = re.compile(
    r"^(which|that|this|these|those|it|they|the same|also called|also known|"
    r"the more|the most|the common|the commonest|a variant|a form|same as|"
    r"more common|less common|usually|often|typically|commonly)\b", re.I)


def match_def(desc):
    """A short phrase that genuinely describes the lesion, or None."""
    first = sentences(desc)[0].strip().rstrip(".")
    candidates = [c.strip().rstrip(".,;")
                  for c in re.split(r'\s+—\s+|;\s+', first)] + [first]
    for c in candidates:
        n = len(c.split())
        if n < 3 or n > MATCH_DEF_MAX_WORDS:      # one or two words says nothing
            continue
        if _REJECT.match(c):
            continue
        # Epidemiology, incubation and taxonomy are facts about the disease but
        # not about how it LOOKS, which is what this deck is for. "Incubation
        # 4-6 weeks" and "About 100-150 species" both passed the length test.
        if re.search(r"\d+\s*(%|per cent)|\bpopulation\b|\bincubation\b|"
                     r"\bspecies\b|\bprevalence\b|\bincidence\b", c, re.I):
            continue
        # THE PHRASE MUST DESCRIBE HOW IT LOOKS. This deck answers "what does
        # this look like", and compressing a manifestation cell to nine words
        # kept surfacing true-but-wrong-kind facts instead: "Borrelia
        # burgdorferi, a spirochete" (etiology), "Females more than males"
        # (demographics), "NOT considered contagious" (transmission). Requiring
        # a morphology word is a blunt test, but it is the actual criterion, and
        # a smaller honest set beats a larger misleading one -- everything
        # rejected here still ships as a full flashcard.
        if not _MORPH.search(c):
            continue
        # A clause lifted from mid-sentence starts lowercase; capitalise it so
        # the card reads as a statement rather than a fragment.
        return c[0].upper() + c[1:]
    return None


ICON = ('<circle cx="12" cy="12" r="9"/><path d="M8.5 13.5c1.2 1.4 5.8 1.4 7 0"/>'
        '<path d="M9 9.5h.01M15 9.5h.01"/>')


def build_derm():
    rows = [r for r in CHART.ROWS if r[0] != "SECTION"]
    cards, match, skipped = [], [], []
    seen = set()
    for r in rows:
        name = clean_name(r[1])
        desc = plain(r[2])
        if not name or not desc:
            continue
        if name in seen:                       # chart badges keep these distinct
            continue
        seen.add(name)
        cards.append([name, card_back(desc)])
        md = match_def(desc)
        if md:
            match.append([name, md])
        else:
            skipped.append(name)

    # Two conditions sharing a definition would render as one tile on the Match
    # board (definitions are grouped by text), making the pair unwinnable as a
    # discrimination. Drop every side of a collision rather than pick a winner.
    from collections import Counter
    dupes = {d for d, k in Counter(d for _, d in match).items() if k > 1}
    if dupes:
        match = [m for m in match if m[1] not in dupes]
    return cards, match, skipped


DECKS = [
    dict(id="derm-disease-processes",
         name="Dermatology — All Disease Processes",
         color="accent1", icon=ICON, build=build_derm,
         group=("cms-1", "exam1")),
]


def js_deck(d, cards, match):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False))
                         for a, b in rows)
    if match:
        return ('  { id: %s, name: %s, color: %s,\n    icon: \'%s\',\n'
                '    cards: [\n%s\n    ],\n    matchCards: [\n%s\n    ] },\n'
                % (json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
                   d["icon"], pairs(cards), pairs(match)))
    return ('  { id: %s, name: %s, color: %s,\n    icon: \'%s\',\n'
            '    cards: [\n%s\n    ] },\n'
            % (json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
               d["icon"], pairs(cards)))


def main():
    dry = "--dry" in sys.argv
    src = open(ARCADE, encoding="utf-8").read()
    for d in DECKS:
        cards, match, skipped = d["build"]()
        assert cards, "%s produced no cards" % d["id"]
        for front, back in cards:
            assert len(back.split()) <= CARD_BACK_MAX_WORDS, "card back too long: %s" % back
        for term, defn in match:
            assert len(defn.split()) <= MATCH_DEF_MAX_WORDS, "match def too long: %s" % defn
        fronts = [c[0] for c in cards]
        assert len(fronts) == len(set(fronts)), "duplicate card front"
        print("%s: %d flashcards (Match falls back to these; see the module "
              "docstring for why there is no compressed match set)" % (d["id"], len(cards)))
        if dry:
            for c in cards[:6]:
                print("   %-42s %s" % (c[0][:42], c[1][:88]))
            continue

        block = js_deck(d, cards, [])
        if ('id: "%s"' % d["id"]) in src:
            i = src.index('  { id: "%s"' % d["id"])
            j = src.index("\n    ] },\n", i) + len("\n    ] },\n")
            src = src[:i] + block + src[j:]
        else:
            m = re.search(r"\n\];\n", src[src.index("var DEMO_DECKS"):])
            end = src.index("var DEMO_DECKS") + m.start() + 1
            src = src[:end] + block + src[end:]

        cls, exam = d["group"]
        anchor = '{ id: "%s", name: ' % exam
        gi = src.index('id: "%s", name:' % cls)
        gj = src.index("deckIds: [", gi)
        gk = src.index("]", gj)
        if ('"%s"' % d["id"]) not in src[gj:gk]:
            src = src[:gj + len("deckIds: [")] + '\n      "%s",' % d["id"] + src[gj + len("deckIds: ["):]

    if dry:
        return
    open(ARCADE, "w", encoding="utf-8").write(src)
    print("written into arcade.js")


if __name__ == "__main__":
    main()
