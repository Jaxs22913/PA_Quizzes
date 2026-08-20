#!/usr/bin/env python3
"""Add the PDM I Lecture 2 (Principles of Medical Imaging) Arcade deck.

One deck for one topic, alongside the Lecture 1 deck already in arcade.js. Cards
are single atomic facts for Sprint's eight-second clock; matchCards are
recognition pairs with compressed identity tags.

Reynolds' constraints carry over and are asserted below: no card asks for a
memorised reference value, and none asks for a calculation. The Hounsfield cards
are the one place numbers appear, and each names the scale it is read against --
which is exactly the context she said she always supplies.

Nothing draws on slide 34, whose two-column structures table cannot be
reconstructed from the file. Asserted.
"""
import json, os, re, sys

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a scanner gantry: a ring with the table passing through it
ICON = ('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.2"/>'
        '<path d="M3 20h18"/>')

DECKS = [
 dict(id="pdm-medical-imaging", name="Principles of Medical Imaging", color="accent2",
      icon=ICON, cards=[
  ["Who discovered x-rays, and when?", "Wilhelm Roentgen, in Germany in 1895."],
  ["What did Roentgen receive in 1901?", "The first Nobel Prize for Physics."],
  ["What makes a radiograph conventional?", "It uses ionizing radiation without added contrast such as barium or iodine."],
  ["Which imaging study is the most widely obtained?", "Conventional radiographs, because they are quick, cheap and available anywhere."],
  ["Name the five basic radiographic densities, whitest to blackest.", "Metal, calcium, fluid or soft tissue, fat, and air."],
  ["Which two of the five basic densities cannot be told apart on a plain film?", "Fluid and soft tissue."],
  ["Which density absorbs the least x-ray?", "Air, which is why it prints blackest."],
  ["What does radiolucent mean?", "Darker on the image, because more of the beam passed through."],
  ["What does radiopaque mean?", "Whiter on the image, because less of the beam passed through."],
  ["In which units is radiation measured?", "Milli Sieverts and milli Grays."],
  ["Who developed the first computed tomography scanner?", "Godfrey Hounsfield, with Allan Cormack; they shared the 1979 Nobel Prize for Medicine."],
  ["What is a computed tomography image made of?", "A matrix of thousands of pixels, each assigned a Hounsfield number."],
  ["On the Hounsfield scale, what value is water given?", "Zero, by convention. Everything else is placed relative to it."],
  ["On the Hounsfield scale where water is zero, what is air?", "Minus one thousand, the bottom of the scale."],
  ["On the Hounsfield scale where water is zero, what is metal?", "Approximately plus one thousand or higher."],
  ["On the Hounsfield scale where water is zero, what range is bone?", "Approximately plus four hundred to plus six hundred."],
  ["What does computed tomography separate that a plain film cannot?", "Water from soft tissue."],
  ["What is a window in computed tomography?", "A pre-selected range of Hounsfield numbers spread across the available grey scale."],
  ["What does increased attenuation mean?", "A high Hounsfield number, appearing whiter, as with metal and calcium."],
  ["What is post-processing, and why does it matter?", "Re-windowing the acquired data afterwards, without repeating the study or re-exposing the patient."],
  ["How is computed tomography's place among the modalities described?", "The cornerstone of cross-sectional imaging."],
  ["Which three devices are the highest-emitting in existence?", "Computed tomography, positron emission tomography, and single photon emission tomography."],
  ["Which listed study delivers the highest organ dose?", "Neonatal abdominal computed tomography, at twice the adult figure."],
  ["Which listed study delivers the lowest organ dose?", "Dental radiography."],
  ["What is one gray?", "One joule per kilogram."],
  ["For x-ray radiation, how do millisieverts and milligrays relate?", "One millisievert equals one milligray."],
  ["What is unique about radiation exposure in nuclear medicine?", "The patient briefly becomes the source and can expose other people."],
  ["Which tracer does positron emission tomography usually use?", "Fluorodeoxyglucose-18, a radioactive glucose."],
  ["Why does positron emission tomography use a glucose analogue?", "Because tumours have a higher metabolic rate and consume more glucose."],
  ["What is a positron?", "A particle of about the same mass as an electron, but positively charged."],
  ["What does single photon emission tomography show?", "Where blood flows."],
  ["Which tracer does single photon emission tomography usually use?", "Technetium-99."],
  ["Name three indications for single photon emission tomography.", "Heart disease, bone scans, and brain evaluations."],
  ["Name three indications for positron emission tomography.", "Cancer staging, brain disorders, and cardiac blood flow."],
  ["Why are the kidneys visible on a bone scan?", "Renal uptake is normal, and the same is true on positron emission scans."],
  ["How does ultrasound form its image?", "High-frequency sound leaves the transducer, bounces off tissue and returns to it."],
  ["What is ultrasound indicated for?", "Assessment of moving structures: the heart, the vasculature, and obstetrics."],
  ["What does colour Doppler add?", "Direction of flow and velocity."],
  ["Name two structures ultrasound cannot see through.", "Bone, and large gas-filled structures."],
  ["In which patients is ultrasound often the first study of choice?", "Female pelvis and paediatric patients."],
  ["Which modality is called the safest of the radioimaging modalities?", "Ultrasound, because it uses no ionizing radiation."],
  ["How are magnetic resonance images generated?", "A magnetic field aligns hydrogen; releasing it emits radio waves the computer maps."],
  ["What is a magnetic resonance image essentially a map of?", "Hydrogen."],
  ["Which contrast agent is used for magnetic resonance?", "Gadolinium."],
  ["On a T2-weighted image, how does high water content appear?", "Bright."],
  ["On a T1-weighted image, how does high water content appear?", "Dark."],
  ["Which tissues follow water on T1 and T2?", "Fat, oedema, infection, blood, and cerebrospinal fluid."],
  ["Which tissue is magnetic resonance best for?", "Soft tissue, essentially anything other than bone."],
  ["Why can magnetic resonance see tissue surrounded by bone?", "Calcium emits no signal, so the bone does not obscure it."],
  ["Which magnetic resonance technique is useful in stroke?", "Diffusion-weighted imaging."],
  ["Name the two safety hazards specific to magnetic resonance.", "Magnetic implanted devices, and ferromagnetic projectiles."],
  ["What is the trade-off of an open magnetic resonance scanner?", "Decreased quality of imaging."],
  ["Where is magnetic resonance most widely used?", "Neuro-imaging, and the soft tissues of orthopaedics."],
  ["What is a vasculogram?", "Not one specific test. Any of the modalities can be used to image vessels."],
  ["Which angiographic study needs no dye at all?", "Magnetic resonance angiography, which images the arterial walls directly."],
  ["What does computed tomography angiography require?", "Iodine dye injected quickly."],
  ["What does fluoroscopy allow that a plain film does not?", "Real-time evaluation of motion and of positioning changes."],
  ["How are radiographic projections named?", "In the direction the beam travels, from what it strikes first onward."],
  ["Why is the posterior-anterior chest view preferred?", "It reduces magnification of the heart, so cardiomegaly is not misread."],
  ["Besides the heart, what else does the posterior-anterior view improve?", "Lung visualisation, the apices, and the posterior ribs; it also lowers dose."],
  ["What does the standard chest examination consist of?", "A posterior-anterior and a lateral film, read together."],
  ["How is a posterior-anterior film oriented?", "As if the patient stood in front of you, their right side on your left."],
  ["Which way does the patient face on the lateral chest view?", "Towards the left."],
  ["What is the decubitus position used to evaluate?", "Pleural effusion, because gravity lets the fluid level out."],
  ["What does a kidney-ureter-bladder film evaluate, and how?", "The genitourinary tract, supine, shot anterior-posterior."],
  ["What does an abdominal series evaluate, and how?", "The gastrointestinal tract, standing, shot anterior-posterior."],
  ["Which enteric pathologies does the abdominal series assess?", "Small bowel obstruction, perforation, and volvulus."],
  ["Which plane divides the body into upper and lower sections?", "The axial, or transverse, plane."],
  ["Which plane divides the body into anterior and posterior sections?", "The coronal plane."],
  ["Which plane divides the body into right and left sections?", "The sagittal plane."],
  ["What is a parasagittal section?", "One located to either side of the midline, rather than in it."],
  ["On a traditional axial slice, where is the patient's left?", "On the reader's right, because you view as if looking at the feet."],
  ["Where does the indicator belong in cardiac ultrasound?", "On the right of the screen."],
  ["Where does the indicator belong for every other ultrasound?", "On the left of the screen."],
  ["Which agent is used for intravenous contrast in computed tomography?", "Omnipaque, or iohexol, a radioactive form of iodine."],
  ["What must be checked before intravenous iodinated contrast?", "Blood urea nitrogen and creatinine, because the agent is nephrotoxic."],
  ["What is given to protect the kidneys with iodinated contrast?", "One litre of normal saline."],
  ["Which oral contrast is contraindicated when perforation is suspected?", "Barium, because it is toxic to extra-intestinal tissue."],
  ["Which oral agent is used instead when perforation is suspected?", "Gastrografin."],
  ["Does shellfish allergy cross-react with iodinated contrast?", "No. There should be no cross-reactivity between them."],
  ["Which allergy history marks a genuinely high-risk patient?", "A documented anaphylactic reaction to any medication."],
  ["What is the stated takeaway on contrast safety?", "Always ask about allergies and assess kidney function."],
  ["Why is cancer named as a risk factor for all contrast material?", "Because the dyes are technically radioactive, as are the imaging techniques."],
  ["What are the risks of fluorodeoxyglucose-18?", "No contraindications and no known nephrotoxicity, though it may cause hyperglycaemia."],
  ["Why is the genitourinary tract always contrast positive on a positron emission scan?", "Fluorodeoxyglucose is renally cleared."],
  ["What is the safety record of technetium-99?", "Allergic reactions are rare and no organ damage has been documented."],
  ["Name three routes contrast can be injected besides a vessel.", "Into a joint, intrathecally, and into the bladder."],
  ["Why give the radiologist clinical information?", "They have not seen the patient, so the history is what guides their read."],
  ["What should you do about a vague radiology report?", "Contact the radiologist to discuss the patient."],
  ["What if you are unsure which modality to order?", "Tell the radiologist what you are looking for and they can guide the choice."],
 ], matchCards=[
  ["Hounsfield zero", "Water, by convention"],
  ["Hounsfield minus one thousand", "Air"],
  ["T2 weighted", "Water is bright"],
  ["T1 weighted", "Water is dark"],
  ["Decubitus view", "Pleural effusion"],
  ["Abdominal series", "Standing, gastrointestinal tract"],
  ["Kidney-ureter-bladder", "Supine, genitourinary tract"],
  ["Posterior-anterior chest", "No cardiac magnification"],
  ["Colour Doppler", "Flow direction and velocity"],
  ["Gadolinium", "Magnetic resonance contrast"],
  ["Omnipaque, iohexol", "Iodinated, nephrotoxic"],
  ["Gastrografin", "Used if perforation suspected"],
  ["Fluorodeoxyglucose-18", "Positron emission tracer"],
  ["Technetium-99", "Single photon emission tracer"],
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
if "pdm-medical-imaging" in s:
    sys.exit("deck already present -- nothing to do")

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
    txt = " ".join(a + " " + b for a, b in d["cards"]).lower()
    assert "mg/dl" not in txt and "mmol/l" not in txt, "a card asks for a reference value"
    assert "calculate" not in txt, "a card asks for a calculation"
    # slide 34's structures table is unreconstructable; nothing may lean on it
    assert "best visualized by" not in txt, "a card leans on slide 34"

m = re.search(r"\n\];\n", s[s.index("var DEMO_DECKS"):])
end = s.index("var DEMO_DECKS") + m.start() + 1
s = s[:end] + "".join(js_deck(d) for d in DECKS) + s[end:]

# join the existing PDM exam group rather than creating a second one
OLD = '{ id: "exam1", name: "Exam 1", deckIds: ["pdm-lab-diagnostics"] }'
NEW = '{ id: "exam1", name: "Exam 1", deckIds: ["pdm-lab-diagnostics", "pdm-medical-imaging"] }'
assert s.count(OLD) == 1, "PDM exam group not found exactly once"
s = s.replace(OLD, NEW)

open(ARCADE, "w", encoding="utf-8").write(s)
print("added %d deck(s): %d cards, %d match pairs"
      % (len(DECKS), sum(len(d["cards"]) for d in DECKS), sum(len(d["matchCards"]) for d in DECKS)))
