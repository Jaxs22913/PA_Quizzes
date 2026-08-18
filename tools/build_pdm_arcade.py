#!/usr/bin/env python3
"""Add the Principles of Diagnostic Medicine I Lecture 1 Arcade deck to arcade.js.

One deck for one topic. Cards are single atomic facts for Sprint's eight-second
clock; matchCards are recognition pairs with compressed identity tags.

Two constraints carried over from how Professor Reynolds said she examines: no
card asks for a memorised reference range, and no card asks for a calculated
predictive value. Nothing here reaches into the deck's exhaustive additive table
either -- the tube cards stay on the order of draw and the four pairings she
actually called out.
"""
import json, os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
ICON = '<path d="M9 3h6v5l4 9a3 3 0 0 1-3 4H8a3 3 0 0 1-3-4l4-9z"/><path d="M8 14h8"/>'

DECKS = [
 dict(id="pdm-lab-diagnostics", name="Principles of Laboratory Diagnostics", color="accent4",
      icon=ICON, cards=[
  ["During which phase of diagnostic testing do most errors occur?", "The pretest, or preanalytical, phase."],
  ["What is the pretest phase also called?", "The preanalytical phase."],
  ["What is the intratest phase also called?", "The analytical phase."],
  ["What is the posttest phase also called?", "The postanalytical phase."],
  ["When does the pretest phase end?", "When the diagnostic test begins."],
  ["Name a technical error of the pretest phase.", "Inadequate blood in the vacuum tube."],
  ["Which pretest error does a patient eating before a fasting test represent?", "Inappropriate patient preparation."],
  ["Name three variables that can affect laboratory results.", "Hydration status, time of collection, and current drug therapy."],
  ["Which complications are monitored for in the posttest phase?", "Bleeding, infection, respiratory difficulty, perforation, and sedation effects."],
  ["What is the documentation principle stated for the posttest phase?", "If it wasn't documented, it wasn't done."],
  ["What is the memory aid for the order of draw?", "Stop, Light, Red, Stay, Put, Green, Light, Go."],
  ["Which tube is drawn first?", "Yellow, the sterile blood culture tube."],
  ["Which tube is used for coagulation studies?", "Light blue, containing sodium citrate."],
  ["Which tube is used for a complete blood count?", "Lavender, containing ethylenediaminetetraacetic acid."],
  ["Which tube contains a glycolytic inhibitor?", "Gray."],
  ["Why does the order of draw exist?", "To avoid cross-contamination of additives between tubes."],
  ["What is the clear tube used for?", "As a discard tube, filling the collection set before the coagulation tube."],
  ["How should a stool specimen for ova and parasites be stored?", "Not refrigerated. Warm stool is best."],
  ["How many stool specimens are recommended for ova and parasites?", "Three separate random specimens, because of the parasite life cycle."],
  ["What colour indicates a positive guaiac test?", "Blue."],
  ["Why should a guaiac sample be small?", "A large sample obscures the result."],
  ["How are blood cultures collected?", "Two separate samples from opposite arms, aerobic drawn first."],
  ["Why are blood cultures both diagnostic and therapeutic?", "They identify the pathogen and provide sensitivities that direct treatment."],
  ["What must you avoid after disinfecting a blood culture site?", "Palpating the site, unless wearing sterile gloves."],
  ["What are the two steps of a sputum culture?", "Gram stain first, then culture for identification and sensitivities."],
  ["How is a patient prepared for a sputum specimen?", "Sit upright, rinse the mouth with water, three deep breaths, deep cough."],
  ["Which organism does a throat culture usually target?", "Streptococci, because of beta-hemolytic streptococcal pharyngitis."],
  ["Which ages does streptococcal pharyngitis most commonly affect?", "Three to fifteen years."],
  ["What must the swab avoid touching during a throat culture?", "The tongue and the lips."],
  ["Which rule spans throat, sputum and blood cultures?", "Obtain the specimen before starting antibiotics."],
  ["How is point-of-care testing defined?", "Testing completed outside the centralized laboratory, at or near the site of care."],
  ["Name a point-of-care test common in acute care.", "Troponin."],
  ["Name a point-of-care test common in primary care.", "Hemoglobin A1c."],
  ["Which two point-of-care testing areas are increasing rapidly?", "Fentanyl testing and human immunodeficiency virus testing."],
  ["Which is the highest-volume point-of-care test?", "Glucose."],
  ["How is a urinalysis dipstick classified?", "Semi-quantitative."],
  ["How is a rapid strep test classified?", "Qualitative."],
  ["Name a limitation of point-of-care testing.", "Results may be less precise than central laboratory methods."],
  ["Name an advantage of point-of-care testing.", "Better care where resources are limited, such as rural or disaster settings."],
  ["What does a qualitative test answer?", "A why question, producing observation and description."],
  ["What does a quantitative test answer?", "A how much question, producing numbers and statistical results."],
  ["What does the Clinical Laboratory Improvement Amendments program set?", "Federal minimum quality standards for testing human samples at all sites."],
  ["Which complexity category covers about 75% of available tests?", "Moderately complex testing."],
  ["How does the Joint Commission classify testing outside a traditional laboratory?", "As waived testing, which includes point-of-care testing."],
  ["Which agency categorizes tests by complexity?", "The Food and Drug Administration."],
  ["Which agency issues laboratory certificates and conducts inspections?", "The Centers for Medicare and Medicaid Services."],
  ["Can a state relax the federal laboratory standard?", "No. State and city regulation is always stricter, never looser."],
  ["How often must a testing site reapply for its certificate?", "Every two years."],
  ["What does sensitivity measure?", "The probability the test is positive when the person does have the condition."],
  ["What does specificity measure?", "The probability the test is negative when the person does not have the condition."],
  ["What does SnNout mean?", "High sensitivity plus a negative result rules the disease out."],
  ["What does SpPin mean?", "High specificity plus a positive result rules the disease in."],
  ["Sensitivity relates to fewer of which error?", "False negatives."],
  ["Specificity relates to fewer of which error?", "False positives."],
  ["Which test characteristic suits screening?", "High sensitivity."],
  ["Which test characteristic suits confirming a diagnosis?", "High specificity."],
  ["What does positive predictive value indicate?", "The likelihood that a positive result identifies someone with the disease."],
  ["Which measures are test-centered?", "Sensitivity and specificity."],
  ["Which measures are patient-centered?", "Positive and negative predictive value."],
  ["What happens to positive predictive value when prevalence falls?", "It falls, because more of the positives are false."],
  ["What is pre-test probability?", "The likelihood of the condition before the result is known."],
  ["What is the difference between prevalence and incidence?", "Prevalence is how commonly something occurs; incidence is how often it happens."],
  ["What distinguishes a screening test from a diagnostic test?", "Screening looks in asymptomatic people; diagnostic looks for the reason for symptoms."],
  ["Can a screening test become diagnostic?", "Yes, if an abnormality is found during it, as with colonoscopy."],
 ], matchCards=[
  ["Pretest phase", "Preparation until the test begins"],
  ["Intratest phase", "Performing the test itself"],
  ["Posttest phase", "Aftercare, interpretation, follow-up"],
  ["Light blue tube", "Sodium citrate, for coagulation"],
  ["Lavender tube", "Ethylenediaminetetraacetic acid, for blood count"],
  ["Yellow tube", "Sterile media, drawn first"],
  ["Guaiac positive", "The sample turns blue"],
  ["Ova and parasites", "Never refrigerate; three specimens"],
  ["Blood cultures", "Two samples, opposite arms, aerobic first"],
  ["SnNout", "Sensitive test, negative rules out"],
  ["SpPin", "Specific test, positive rules in"],
  ["Positive predictive value", "Belongs to the population tested"],
  ["Waived testing", "All testing outside a traditional laboratory"],
 ]),
]


def js_deck(d):
    def pairs(rows):
        return "\n".join('      [%s, %s],' % (json.dumps(a, ensure_ascii=False),
                                              json.dumps(b, ensure_ascii=False)) for a, b in rows)
    return ('  { id: %s, name: %s, color: %s,\n    icon: \'%s\',\n'
            '    cards: [\n%s\n    ],\n    matchCards: [\n%s\n    ] },\n') % (
        json.dumps(d["id"]), json.dumps(d["name"]), json.dumps(d["color"]),
        d["icon"], pairs(d["cards"]), pairs(d["matchCards"]))


s = open(ARCADE, encoding="utf-8").read()
assert "pdm-lab-diagnostics" not in s, "deck already present"

for d in DECKS:
    assert 8 <= len(d["cards"])
    assert 10 <= len(d["matchCards"]) <= 14, "%s: matchCards outside target" % d["id"]
    for front, back in d["cards"]:
        assert len(back.split()) <= 26, "card back too long -> %s" % back
    for term, definition in d["matchCards"]:
        assert len(definition.split()) <= 9, "match definition too long -> %s" % definition
    for coll in (("cards", 0), ("cards", 1), ("matchCards", 0), ("matchCards", 1)):
        vals = [x[coll[1]] for x in d[coll[0]]]
        assert len(vals) == len(set(vals)), "duplicate in %s[%d] of %s" % (coll[0], coll[1], d["id"])
    # Reynolds' rules, asserted
    txt = " ".join(a + " " + b for a, b in d["cards"]).lower()
    assert "mg/dl" not in txt and "mmol/l" not in txt, "a card asks for a reference value"
    assert "calculate" not in txt, "a card asks for a calculation"

m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

ANCHOR = '''  { id: "physical-diagnosis-2", name: "Physical Diagnosis 2", exams: ['''
NEW = '''  { id: "pdm-1", name: "Principles of Diagnostic Medicine I", exams: [
    { id: "exam1", name: "Exam 1", deckIds: ["pdm-lab-diagnostics"] }
  ]},

'''
assert s.count(ANCHOR) == 1
s = s.replace(ANCHOR, NEW + ANCHOR)
open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d deck(s): %d cards, %d match pairs"
      % (len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
