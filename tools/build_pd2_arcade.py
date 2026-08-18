#!/usr/bin/env python3
"""Add the three Physical Diagnosis 2 Exam 1 Arcade decks to arcade.js.

Three decks rather than two, because the Dermatology lecture carries two
genuinely different kinds of content: the descriptive VOCABULARY (which is pure
recognition and is what Match exists for) and the exam TECHNIQUE and abnormal
FINDINGS (which are recall). Splitting them keeps each deck to one topic, and
keeps Match from mixing "define this word" with "what does this finding mean".

`cards` feed Study, Learn and Sprint, so each tests ONE atomic fact in a single
clause -- a compound answer joined by "and" gets split into two cards, because
Sprint reads them under an eight-second clock. `matchCards` feed Match, which is
pure recognition, so the term is a name and the definition is a compressed
identity tag rather than an explanation.

No bare abbreviations -- the standing rule is the full term, or ABBREVIATION
(full term) on first use. Nothing about how the course works: no grade
weightings, no file naming, no sequestration times.
"""
import json, os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"

ICON_CR = '<path d="M5 4h11l3 3v13H5z"/><path d="M8 10h8M8 14h6"/>'
ICON_MORPH = '<circle cx="8" cy="9" r="3"/><circle cx="16" cy="15" r="4"/><path d="M4 19h4"/>'
ICON_SKIN = '<path d="M4 7c4-3 12-3 16 0v10c-4 3-12 3-16 0z"/><path d="M9 11h.01M14 14h.01"/>'

DECKS = [
 dict(id="pd2-clinical-reasoning", name="Clinical Reasoning & Documentation", color="accent",
      icon=ICON_CR, cards=[
  ["What belongs in the opening statement of an oral case presentation?", "The past medical history and the chief complaint."],
  ["Which findings belong in an oral case presentation?", "Pertinent positives and negatives, from both the history and the physical examination."],
  ["What is the test of a good oral case presentation?", "It leads the listener to the same differential you formulated."],
  ["What is the provider's goal in an oral case presentation?", "To help the listeners visualise the patient and understand the problem."],
  ["In what order should an oral case presentation proceed?", "Mostly the order you obtained the history and performed the examination."],
  ["What is the advice about notes during a case presentation?", "Try not to read from them."],
  ["In a focused encounter, what is narrowed?", "Both the history and the physical examination, not just one."],
  ["Which history components are focused in a focused encounter?", "Present illness, review of systems, past medical, social, family, medications and allergies."],
  ["What must a focused encounter still produce?", "Differentials, studies, a diagnosis, and a treatment plan including patient education."],
  ["How should physical examination findings be written in a note?", "Describe what was found, never normal, abnormal or unremarkable."],
  ["What is the rule on abbreviations in written clinical assignments?", "No abbreviations, stated without qualification."],
  ["What must be done if part of the examination was not performed?", "Document why it was not done; findings may never be invented."],
  ["How are subjective and objective information arranged in a note?", "Each in its own section, never mixed together."],
  ["May two students who saw the same patient write the note together?", "No. The note must be the student's own work."],
  ["Why can reusing your own earlier assignment be plagiarism?", "Work is not original once it has been submitted for academic credit."],
  ["What should be reviewed before submitting a written clinical assignment?", "The grading rubric, and the comments left on previous assignments."],
  ["Where should your attention be when a third party supplies the answers?", "On the patient, always, rather than on the person answering."],
  ["How should communication style vary between patients?", "Adapt the style and content appropriately for each patient."],
  ["How should a student handle feedback that differs between facilitators?", "Accept it and modify behaviour; different facilitators give different feedback."],
  ["What does a small group require before it will release information?", "A full justification of why the information is needed."],
  ["What is the Subjective section of a subjective-objective-assessment-plan note?", "What the patient said: history, pertinent positives and negatives, medications, allergies."],
  ["What is the Objective section of a subjective-objective-assessment-plan note?", "What you found: observations, measurements and tests performed during the encounter."],
  ["How does a subjective-objective-assessment-plan note differ from a full history and physical?", "It is problem-focused rather than comprehensive."],
 ], matchCards=[
  ["Opening statement", "Past medical history plus chief complaint"],
  ["Pertinent negatives", "Absent findings that narrow the differential"],
  ["Focused encounter", "Both history and examination narrowed"],
  ["Comprehensive encounter", "Full history and head-to-toe examination"],
  ["Subjective", "What the patient said"],
  ["Objective", "What you found on examination"],
  ["Assessment", "The diagnosis you concluded"],
  ["Plan", "Testing, treatment, education, follow-up"],
  ["Describe, do not label", "Write findings, never unremarkable"],
  ["Self-plagiarism", "Reusing work already submitted for credit"],
  ["Adapted communication", "Style changed to suit each patient"],
  ["Small group justification", "Explain why information is needed first"],
 ]),

 dict(id="pd2-derm-morphology", name="Skin Lesion Vocabulary", color="accent2",
      icon=ICON_MORPH, cards=[
  ["What is a primary skin lesion?", "The basic lesion that forms first, resulting directly from the disease."],
  ["What is a secondary skin lesion?", "A change in a primary lesion over time."],
  ["Which three processes turn a primary lesion into a secondary one?", "Disease progression, treatment, and manipulation such as picking or scratching."],
  ["Which five features describe a skin lesion?", "Distribution, configuration, morphology, colour and texture."],
  ["What is a macule?", "A circumscribed, flat discoloration under one centimetre."],
  ["What is a patch?", "A circumscribed, flat discoloration over one centimetre."],
  ["What is a papule?", "A palpable, elevated solid mass under one centimetre."],
  ["What is a plaque?", "A palpable, elevated, plateau-like solid mass over one centimetre."],
  ["What is a nodule?", "An elevated, firm, circumscribed lesion deeper in the dermis than a papule."],
  ["What is a tumor?", "A palpable, elevated solid mass greater than two centimetres."],
  ["What is a wheal?", "An elevated, irregular area of cutaneous edema; solid and transient."],
  ["Which primary lesion is the only transient one?", "The wheal."],
  ["What is a vesicle?", "A superficial elevation filled with fluid, under one centimetre."],
  ["What is a bulla?", "A superficial elevation filled with fluid, over one centimetre."],
  ["What is a pustule?", "A superficial elevation filled with purulent material, usually under one centimetre."],
  ["What is a cyst?", "An elevated, circumscribed, encapsulated lesion with liquid or semisolid contents."],
  ["What is a crust?", "A collection of cellular debris, dried serum and blood; a scab."],
  ["Which primary lesion usually precedes a crust?", "A vesicle, bulla or pustule."],
  ["What is an erosion?", "Loss of superficial epidermis; moist surface that does not bleed."],
  ["What is an ulcer?", "Deeper loss of epidermis and dermis; may bleed and scar."],
  ["What is a fissure?", "A linear crack in the skin."],
  ["What is a scale?", "A thin flake of exfoliated epidermis."],
  ["What is an excoriation?", "An abrasion or scratch mark, either linear or rounded."],
  ["What distinguishes a keloid from an ordinary scar?", "A keloid grows beyond the original wound."],
  ["How is a hypertrophic scar described?", "Thick and pink."],
  ["How is an atrophic scar described?", "Thin and white."],
  ["What is lichenification?", "Thickening of the epidermis with skin line accentuation, from chronic irritation."],
  ["What is collarette scale?", "Fine scale attached peripherally and detached centrally at a lesion's edge."],
  ["What does annular mean?", "Shaped like a ring."],
  ["What does an iris or target lesion look like?", "Shaped like a bull's eye."],
  ["What does confluent mean?", "The lesions run together."],
  ["What does discrete mean?", "The lesions remain separate."],
  ["What does reticular mean?", "Forming a lacy or networked pattern."],
  ["What does gyrate mean?", "Twisted, coiled, spiral or snakelike."],
  ["What does herpetiform mean?", "Grouped papules or vesicles arranged as in herpes simplex."],
  ["What does zosteriform mean?", "Lesions clustered in a dermatomal distribution, as in herpes zoster."],
  ["Which distribution suggests psoriasis?", "Extensor."],
  ["Which distribution suggests herpes zoster?", "Dermatomal."],
  ["Which distribution suggests skin cancers?", "Sun-exposed, also called photodistribution."],
  ["Which distribution suggests an allergic reaction?", "Generalised or diffuse."],
  ["What does intertriginous mean?", "Involving the skin creases and folds."],
 ], matchCards=[
  ["Macule", "Flat discoloration under one centimetre"],
  ["Patch", "Flat discoloration over one centimetre"],
  ["Papule", "Solid elevation under one centimetre"],
  ["Plaque", "Plateau-like elevation over one centimetre"],
  ["Nodule", "Firm lesion deeper than a papule"],
  ["Wheal", "Transient cutaneous edema, irregular shape"],
  ["Vesicle", "Fluid-filled elevation under one centimetre"],
  ["Bulla", "Fluid-filled elevation over one centimetre"],
  ["Pustule", "Elevation filled with purulent material"],
  ["Cyst", "Encapsulated lesion, liquid or semisolid"],
  ["Erosion", "Superficial epidermal loss, does not bleed"],
  ["Ulcer", "Deeper loss; may bleed and scar"],
  ["Keloid", "Scar growing beyond the original wound"],
 ]),

 dict(id="pd2-derm-exam", name="Dermatological History, Exam & Findings", color="accent3",
      icon=ICON_SKIN, cards=[
  ["Name a function of the skin besides protection.", "Production of vitamin D."],
  ["Which gland secretes sweat to maintain body temperature?", "The sudoriferous, or eccrine, gland."],
  ["Which gland becomes active at puberty and secretes pheromones?", "The apocrine gland."],
  ["Which gland surrounds the hair follicle and secretes sebum?", "The sebaceous gland."],
  ["What does the memory aid bugs, drugs, contact prompt?", "Contacts and travel, systemic medications, and allergens or irritants."],
  ["Which changes should you ask about in an existing skin lesion?", "Colour, shape, size, pain, easy bleeding, and non-healing areas."],
  ["Which three skin symptoms should be asked about?", "Pruritus, pain and paresthesia."],
  ["Is pruritus a diagnosis?", "No. It is the sensation that causes the desire to scratch."],
  ["What role does psychological stress play in skin disease?", "Seldom the sole cause, but it can exacerbate many dermatoses."],
  ["What should inadequate skin, hair or nail hygiene prompt you to assess?", "Social history, cognition, and ability to perform activities of daily living."],
  ["For which body system does the order of the four examination techniques change?", "The abdominal examination."],
  ["Which equipment is needed for a skin examination?", "A ruler, a light source, a magnifying lens, and gloves."],
  ["Why is natural light preferred for skin inspection?", "Artificial light may distort skin tone."],
  ["Which part of the hand assesses skin temperature?", "The dorsal aspect."],
  ["What does reduced skin mobility indicate?", "Edema."],
  ["What does skin that remains elevated after being lifted indicate?", "Dehydration."],
  ["What usually causes central cyanosis?", "Inadequate oxygenation in the lungs."],
  ["What usually causes peripheral cyanosis?", "Inadequate circulation."],
  ["What does diascopy show when the colour fades under pressure?", "Vascular engorgement."],
  ["What does diascopy show when the colour does not fade?", "Hemorrhage in the skin."],
  ["How large are petechiae?", "Less than three millimetres, and they do not blanch."],
  ["How large is purpura?", "Three millimetres to one centimetre, and it does not blanch."],
  ["How large is an ecchymosis?", "Greater than one centimetre, fading over time, and it does not blanch."],
  ["Which vascular lesion has a central red macule with radiating arms?", "The spider angioma, and it blanches."],
  ["What is the triple response of Lewis?", "Red line, then reflex flare, then a linear wheal."],
  ["What defines a stage one pressure ulcer?", "Intact skin with erythema that fails to blanch under pressure."],
  ["What defines a stage two pressure ulcer?", "Partial thickness skin loss involving epidermis, dermis or both."],
  ["What defines a stage three pressure ulcer?", "Full thickness loss reaching but not passing through underlying muscle."],
  ["What defines a stage four pressure ulcer?", "Full thickness loss with destruction of tissue, muscle and bone."],
  ["What does tinea corporis look like?", "Scaling, sharply demarcated round plaques with central clearing."],
  ["What does tinea capitis look like?", "Round scaling patches of alopecia with hairs broken close to the scalp."],
  ["What does basal cell carcinoma look like?", "A translucent, pearly nodule with a depressed centre and raised borders."],
  ["What does squamous cell carcinoma look like?", "A red scaling, crusting nodule or plaque that can ulcerate and bleed."],
  ["What does D stand for in the melanoma warning signs?", "Diameter larger than six millimetres."],
  ["Which neoplasm occurs most frequently in acquired immunodeficiency syndrome?", "Kaposi's sarcoma."],
  ["What distinguishes terminal hair from vellus hair?", "Terminal hair is coarse; vellus hair is short and fine."],
  ["Which hair loss shows exclamation point hairs?", "Alopecia areata."],
  ["What is trichotillomania?", "Hair loss caused by an urge to pull out one's own hair."],
  ["What is hirsutism?", "Increased hair growth in women in a male pattern of distribution."],
  ["What is koilonychia?", "Spoon-shaped concave nails, with the nail plate thinned and inverted."],
  ["What is onycholysis?", "Painless separation of the nail plate from the nail bed, starting distally."],
  ["What does a green nail suggest?", "Pseudomonas infection."],
  ["What does a brown to black nail suggest?", "Melanoma."],
  ["What do Beau's lines halfway up the nail suggest?", "An illness about three months previously."],
  ["What angle defines clubbing?", "Greater than one hundred and eighty degrees between nail base and finger."],
  ["What is acute paronychia?", "A painful, purulent soft tissue infection around the cuticle or nail fold."],
 ], matchCards=[
  ["Diascopy", "Glass pressed against skin under observation"],
  ["Petechiae", "Non-blanching macules under three millimetres"],
  ["Ecchymosis", "Non-blanching macules over one centimetre"],
  ["Telangiectasia", "Fine irregular vessels that blanch"],
  ["Stage one pressure ulcer", "Intact skin, non-blanching erythema"],
  ["Tinea capitis", "Scaling alopecia, hairs broken near scalp"],
  ["Basal cell carcinoma", "Pearly nodule, depressed centre, raised borders"],
  ["Kaposi's sarcoma", "Dark blue-purple lesions, widely disseminated"],
  ["Alopecia areata", "Round patches, exclamation point hairs"],
  ["Koilonychia", "Spoon-shaped concave nails"],
  ["Onycholysis", "Painless nail plate separation, starting distally"],
  ["Beau's lines", "Transverse depressions dating a past illness"],
  ["Clubbing", "Nail base angle over 180 degrees"],
 ]),
]


def js_deck(d):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False)) for a, b in rows)
    return ('  { id: %s, name: %s, color: %s,\n'
            '    icon: \'%s\',\n'
            '    cards: [\n%s\n    ],\n'
            '    matchCards: [\n%s\n    ] },\n') % (
        json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
        d["icon"], pairs(d["cards"]), pairs(d["matchCards"]))


s = open(ARCADE, encoding="utf-8").read()
assert "pd2-dermatology" not in s and "pd2-derm-morphology" not in s, "decks already present"

# validate against the Arcade content policy before writing anything
for d in DECKS:
    assert 8 <= len(d["cards"]), "%s: Sprint races 8 cards, needs at least 8" % d["id"]
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside the 10-13 target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "%s: card back too long for Sprint -> %s" % (d["id"], back)
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "%s: match definition too long -> %s" % (d["id"], definition)
    ids = [c[0] for c in d["cards"]]
    assert len(ids) == len(set(ids)), "%s: duplicate card front" % d["id"]
    terms = [c[0] for c in d["matchCards"]]
    assert len(terms) == len(set(terms)), "%s: duplicate match term" % d["id"]
    defs = [c[1] for c in d["matchCards"]]
    assert len(defs) == len(set(defs)), "%s: duplicate match definition" % d["id"]

# splice the decks in before the DEMO_DECKS closing bracket
m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

# register the class where semesters.js orders Fall 2026: after pharm-1, before clin-path-1
ANCHOR = '''  { id: "clin-path-1", name: "Clinical Pathophysiology I", exams: ['''
NEW = '''  { id: "physical-diagnosis-2", name: "Physical Diagnosis 2", exams: [
    { id: "exam1", name: "Exam 1", deckIds: ["pd2-clinical-reasoning", "pd2-derm-morphology", "pd2-derm-exam"] }
  ]},

'''
assert s.count(ANCHOR) == 1
s = s.replace(ANCHOR, NEW + ANCHOR)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d decks (%d cards, %d match pairs)" % (
    len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
for d in DECKS:
    print("   %-24s %2d cards  %2d match" % (d["id"], len(d["cards"]), len(d["matchCards"])))
