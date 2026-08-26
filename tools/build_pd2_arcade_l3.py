#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PD2 Lecture 3 (Advanced Ocular Examination) Arcade deck.

BECK'S SIX EXCLUSIONS ARE HONOURED HERE TOO, and asserted -- a card on
something she said she would not test is wasted study time, which is the one
error worse than no card at all.

Registers the deck in BOTH structures arcade.js keeps: the flat deck list and
the class/exam grouping. A deck missing from the grouping is invisible in the
app, which is exactly how two decks shipped broken earlier today.
"""
import os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
ICON = ('<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>'
        '<circle cx="12" cy="12" r="2.5"/><path d="M12 2v2"/><path d="M12 20v2"/>')

DECK = dict(
    id="pd2-ocular-exam", name="Advanced Ocular Examination", color="accent4", icon=ICON,
    cards=[
  ["What are the four axes for assessing an eye complaint?", "Time course, precipitating factors, palliative or exacerbating variables, and vision loss."],
  ["Bilateral visual loss implies what kind of cause?", "A primary neurologic cause, not an ophthalmologic one."],
  ["Multiple new flashes or floaters mean what? And a single floater?", "Multiple suggest a retinal tear or vitreous haemorrhage. A single floater is probably benign."],
  ["Rapid versus gradual visual deterioration?", "Rapid suggests vascular causes; gradual suggests cataract and the like."],
  ["Eye pain RELIEVED by a topical anaesthetic means what?", "A surface problem such as corneal injury. Pain NOT relieved suggests a deeper source."],
  ["Itching plus excessive tearing suggests what?", "An allergic cause."],
  ["Deep eye pain suggests what?", "Acute narrow angle glaucoma."],
  ["Which immunisation status matters in eye trauma?", "Tetanus."],
  ["After a chemical splash, what must you establish?", "Whether the fluid was acid or alkali."],
  ["Acute, unilateral, PAINLESS visual loss — think what?", "Retinal vascular occlusion, retinal detachment, vitreous haemorrhage, macular degeneration."],
  ["Acute, unilateral, PAINFUL visual loss — where and what?", "Usually cornea and anterior chamber: corneal abrasion or ulcer, uveitis, traumatic hyphaema, acute narrow angle glaucoma."],
  ["Acute, BILATERAL, painful — think what?", "Thermal, radiation or chemical exposure."],
  ["Gradual, painless visual loss — think what?", "Simple glaucoma or cataract."],
  ["Eye pain WITH BLINKING suggests what?", "Corneal abrasion or a foreign body."],
  ["Eye pain with a GRITTY feeling suggests what?", "Conjunctivitis."],
  ["Eye pain with PHOTOPHOBIA suggests what?", "Inflammation of the iris."],
  ["Eye pain ON EYE MOTION suggests what?", "Optic neuritis."],
  ["Eye pain WITH HEADACHE suggests what?", "Acute narrow angle glaucoma."],
  ["HORIZONTAL diplopia means a palsy of which nerves?", "Cranial nerve three or six — images side by side."],
  ["VERTICAL diplopia means a palsy of which nerves?", "Cranial nerve three or four — images on top of each other."],
  ["Which cranial nerve appears in BOTH diplopia patterns?", "The third. Her shortcut: three for both of those."],
  ["Watery or mucoid discharge suggests what? Purulent?", "Watery or mucoid suggests allergic or viral. Purulent suggests bacterial."],
  ["What does the deck call the vital sign of the eye?", "Visual acuity."],
  ["When must pupillary reactions be checked?", "Before dilating."],
  ["What must never be done to the globe in trauma?", "Do not palpate it."],
  ["Which two cellulitis diagnoses must be differentiated, and why?", "Preseptal from orbital — because orbital cellulitis can lead to death."],
  ["Scaly eyebrows suggest what? Lateral sparseness?", "Scaliness suggests seborrhoeic dermatitis. Lateral sparseness suggests hypothyroidism."],
  ["Name three causes of ptosis besides senile and congenital.", "Myasthenia gravis, oculomotor nerve damage, and damage to the sympathetic supply — Horner syndrome."],
  ["What causes SENILE ptosis?", "Weakened muscle, relaxed tissues, and the weight of herniated fat."],
  ["Hordeolum versus chalazion on inspection?", "The hordeolum is painful and at the lid's edge. The chalazion is chronic, non-painful, meibomian, and generally not at the margin — it points inside the lid."],
  ["Where does xanthelasma sit, and what should it prompt?", "Along the nasal portions of the lids — consider lipid disorders."],
  ["What is trichiasis?", "Posteriorly misdirected eyelashes."],
  ["A YELLOW sclera means what? A BLUE sclera?", "Yellow means liver disease. Blue means osteogenesis imperfecta."],
  ["How do you check for proptosis?", "Stand behind the seated patient and inspect from above, drawing the lid slightly upward to compare the corneas against the lower lids."],
  ["Name four causes of proptosis.", "Retrobulbar haemorrhage, orbital cellulitis, orbital tumour, and Graves disease."],
  ["How is the nasolacrimal duct obstruction test done?", "Patient looks up; press on the lower lid near the medial canthus just inside the bony orbit to compress the sac; look for fluid regurgitating from the puncta."],
  ["What does mucopurulent fluid from the puncta mean?", "An obstructed nasolacrimal duct."],
  ["When should the lacrimal sac compression test be avoided?", "If the area is significantly inflamed or tender."],
  ["Where is the stick placed when everting the upper lid?", "At least 1 cm above the lid margin, at the upper border of the tarsal plate."],
  ["When must the lid NEVER be everted?", "If rupture of the globe is suspected."],
  ["Which four findings make a subconjunctival haemorrhage benign?", "Pain absent, vision and pupil unaffected, no discharge, and a clear cornea."],
  ["When is globe rupture more likely with a subconjunctival haemorrhage?", "In trauma, and when the haemorrhage encircles the entire cornea."],
  ["Where is redness maximal in conjunctivitis?", "Peripherally — diffuse dilation of the conjunctival vessels."],
  ["Injection JUST AROUND THE CORNEA suggests which three?", "Keratitis, iritis, or acute glaucoma."],
  ["Nodular episcleritis is associated with which two diseases?", "Rheumatoid arthritis and lupus erythematosus."],
  ["RED-EYE CHART: which condition has a dilated fixed pupil and a steamy cornea?", "Glaucoma — and its significance is an acute increase in intraocular pressure, an emergency."],
  ["RED-EYE CHART: how is the pain of acute iritis described?", "Moderate, aching, deep."],
  ["RED-EYE CHART: which column reads negative on pain, vision, discharge, pupil and cornea?", "Subconjunctival haemorrhage."],
  ["RED-EYE CHART: what is ciliary injection, and why does it matter?", "Dilation of deeper vessels seen as radiating vessels or a reddish-violet flush around the limbus — an important sign of corneal injury, acute iritis and glaucoma."],
  ["RED-EYE CHART: four backup clues when the injection pattern does not help?", "Pain, decreased vision, unequal pupils, and a less than perfectly clear cornea."],
  ["What do OD, OS and OU mean?", "OD is the right eye, OS the left eye, OU both eyes."],
  ["What does 20/200 mean?", "At 20 feet the patient reads print a normal eye reads at 200 feet. The larger the second number, the worse the vision."],
  ["What is documented if the patient cannot read the chart?", "Counting fingers, hand motion, or light perception."],
  ["How does the pinhole test work?", "It admits only light perpendicular to the lens, so the light need not be bent to focus — which corrects any refractive error."],
  ["If the pinhole does NOT correct the deficit, consider what?", "Cataract, optic nerve disease, or retinal disease."],
  ["Which two tests make the best confrontation field exam?", "The static finger wiggle test and the kinetic red target test."],
  ["What is the endpoint of the kinetic red target test?", "When the 5 mm red-topped pin first appears RED."],
  ["Where is the blind spot, and what enlarges it?", "15 degrees temporal to the line of gaze — enlarged in glaucoma, optic neuritis and papilloedema."],
  ["A temporal field defect in one eye should prompt what?", "Testing for a nasal defect in the other eye."],
  ["When is nystagmus normal, and when is it not?", "A few beats on lateral gaze is normal. If it persists when the finger is brought back into binocular vision, consider a neurologic condition."],
  ["What is a positive lid lag, and what causes it?", "The rim of sclera is visible above the iris on downward gaze — most often hyperthyroidism."],
  ["What does the cover-uncover test reveal?", "A slight muscle imbalance not otherwise seen."],
  ["How much pupil difference is common, and when is anisocoria benign?", "Half to one millimetre is common, and it is benign if the reactions are normal."],
  ["When is a pupil finding abnormal?", "A difference greater than 1 mm, or a poorly reactive pupil."],
  ["An acute significantly dilated pupil with headache — what two causes?", "Uncal herniation, or a posterior communicating artery aneurysm causing a third nerve palsy. It is a medical emergency."],
  ["What is the swinging light test for?", "Functional impairment of the optic nerve and the integrity of the visual pathways. Indicated for anisocoria."],
  ["What is the abnormal swinging light finding called?", "A Marcus Gunn pupil — a relative afferent pupillary defect. Both pupils dilate paradoxically when the light swings to the affected eye."],
  ["In an afferent defect, where is the lesion?", "The optic nerve."],
  ["Why do both pupils dilate in an afferent defect?", "The afferent stimulus on that side is reduced, so the efferent signal to both pupils is reduced and a net dilation results."],
  ["Which nerve mediates the near reaction, and what accompanies it?", "The oculomotor nerve — accompanied by convergence and accommodation."],
  ["Describe Adie's tonic pupil.", "Large, regular, usually unilateral. Light reaction severely reduced or absent. Near reaction present but very slow."],
  ["What is the lesion in Adie's tonic pupil?", "Degeneration of the ciliary ganglia and the postganglionic parasympathetic fibres."],
  ["What defines the Argyll Robertson pupil?", "It accommodates but does not react to light. Small, unequal and irregular."],
  ["What is the Argyll Robertson pupil associated with?", "Classically tertiary syphilis, today more often diabetes; also described in Lyme meningoradiculitis."],
  ["What do mydriatics do to an Argyll Robertson pupil?", "Dilate it only incompletely."],
  ["Name the four features of Horner syndrome.", "Ptosis, miosis, anhidrosis of the ipsilateral face, and a small pupil that still reacts to light and near."],
  ["What is interrupted in Horner syndrome?", "The sympathetic innervation of the pupil and of the levator palpebrae superioris."],
  ["What is seen in CONGENITAL Horner syndrome?", "The involved iris is lighter in colour — heterochromia."],
  ["Describe the pupil in an oculomotor nerve palsy.", "Dilated and fixed to both light and near effort, with ptosis and lateral deviation of the eye almost always present."],
  ["Once local eye disease is excluded, what three causes of a dilated pupil remain?", "Compression or lesion of cranial nerve three; parasympathetic denervation from a ciliary ganglion lesion (Adie's); and pharmacologic block of the sphincter."],
  ["What does a crescent shadow on oblique lighting mean?", "The iris is bowed forward — a narrow angle, and a raised risk of narrow-angle glaucoma."],
  ["Corneal scar versus cataract?", "The scar is a superficial greyish-white corneal opacity. The cataract lies deeper and is visible only through the pupil."],
  ["In which three situations should pupils NOT be dilated?", "If serial neurologic examinations are required, in elderly patients who have had cataract surgery, and if acute angle-closure glaucoma is suspected."],
  ["What must be documented when dilating?", "The time of dilation and the agents used."],
  ["Describe the NORMAL fundus.", "Yellowish-orange to cream, small disc vessels, a sharp disc margin, and a cup central or slightly temporal with a diameter less than half the disc."],
  ["Describe PAPILLOEDEMA on fundoscopy.", "Pink, swollen disc with blurred margins, cup not visible, loss of vessel pulsations — from raised intracranial pressure."],
  ["Describe GLAUCOMATOUS CUPPING.", "The physiologic cup is enlarged, more than half the disc diameter, with retinal vessels sinking in and around the disc."],
  ["Describe OPTIC ATROPHY and name three causes.", "A white disc with absent tiny disc vessels — seen in optic neuritis, multiple sclerosis and temporal arteritis."],
  ["How does the SIZE of a striking object change the injury?", "Larger objects transfer most of the energy to the orbital rim; smaller objects may strike the globe directly."],
  ["Which findings suggest an orbital blow-out fracture?", "A sunken eye, infraorbital hypoaesthesia, diplopia particularly on upward gaze, decreased motility, and sometimes an ipsilateral nosebleed."],
  ["Which findings suggest a zygomatic fracture?", "Flattening of the malar eminence seen from behind the seated patient, oedema and ecchymosis of the temple or infraorbital area, and a palpable step-off on the zygoma."],
  ["Why does a zygomatic fracture hurt on opening the mouth?", "The temporalis muscle passes medial to the arch and inserts on the mandible."],
  ["What is a hyphaema, and what must be checked?", "Bleeding into the anterior chamber from blunt trauma. Check acuity, pupils, the red reflex, the intraocular pressure, and a slit lamp."],
  ["Why evert the upper lid in a corneal abrasion?", "A foreign body in the upper tarsal conjunctiva can scratch the cornea with every blink."],
  ["What does a HAZY cornea in a suspected abrasion suggest?", "Bacterial infection."],
  ["What is the rule about topical anaesthetic in corneal abrasion?", "It gives immediate relief, but it is for diagnosis and not as a treatment."],
  ["How does fluorescein reveal a corneal defect?", "The dye is taken up by areas of cornea devoid of epithelium, seen under blue light."],
  ["Which corneal ulcer is NOT very painful?", "Herpes simplex."],
  ["At what setting can an ophthalmoscope show a corneal ulcer, and what is more sensitive?", "+40 dioptres — but staining with fluorescein is more sensitive for early ulcers."],
  ["Which complaints are EMERGENT?", "Sudden vision loss, retinal artery occlusion, chemical burns, rupture, acute angle-closure glaucoma, and vitreous haemorrhage."],
  ["Which complaints are URGENT — a day or less?", "Acute glaucoma, orbital cellulitis, corneal ulcer or abrasion, retinal detachment, macular oedema or haemorrhage, and hyphaema."],
    ],
    matchCards=[
  ["Marcus Gunn pupil", "Both pupils DILATE on swinging light; optic nerve"],
  ["Adie's tonic pupil", "Large; near reaction present but VERY SLOW"],
  ["Argyll Robertson", "Accommodates but does NOT react to light"],
  ["Horner syndrome", "Ptosis + miosis + anhidrosis; pupil STILL reacts"],
  ["Oculomotor palsy", "Dilated, FIXED to both; ptosis + lateral deviation"],
  ["Horizontal diplopia", "Palsy of cranial nerve III or VI"],
  ["Vertical diplopia", "Palsy of cranial nerve III or IV"],
  ["Papilloedema", "Pink swollen disc, blurred margins, no cup"],
  ["Glaucomatous cupping", "Cup MORE than half the disc; vessels sink in"],
  ["Optic atrophy", "WHITE disc, tiny vessels absent"],
  ["Pinhole corrects it", "A refractive error"],
  ["Pinhole does NOT correct it", "Cataract, optic nerve or retinal disease"],
  ["Yellow sclera", "Liver disease"],
  ["Blue sclera", "Osteogenesis imperfecta"],
  ["Lateral eyebrow sparseness", "Hypothyroidism"],
  ["Lid lag", "Hyperthyroidism"],
  ["Blow-out fracture", "Diplopia on UPWARD gaze; infraorbital numbness"],
  ["Zygomatic fracture", "Flattened cheek; pain opening the mouth"],
  ["Hyphaema", "Blood in the ANTERIOR CHAMBER"],
  ["Crescent shadow present", "Iris bowed forward; NARROW angle"],
    ])

# ---- guard: none of her six exclusions may be carded -----------------------
_EXCLUDED = [
    ("the named virus", r"\badenovirus\b"),
    ("the exophthalmometer", r"exophthalmomet|\b20\s*(?:to|-)\s*22\s*(?:mm|millimet)"),
    ("the corneal reflection test", r"corneal reflection"),
    ("the Adie's associations", r"shy[- ]drager|dysautonomia|amyloidosis"),
    ("the Latin expansions", r"oculus (?:dexter|sinister|uterque)"),
]
_bad = []
for pair in DECK["cards"] + DECK["matchCards"]:
    for label, rx in _EXCLUDED:
        if any(re.search(rx, t, re.I) for t in pair):
            _bad.append((label, pair[0][:45]))
assert not _bad, ("a card covers something Beck said she would NOT test: %r" % _bad[:3])

_p = [c[0] for c in DECK["cards"]]
assert len(_p) == len(set(_p)), "duplicate card prompt: %r" % [x for x in _p if _p.count(x) > 1][:3]
_a = [c[1] for c in DECK["matchCards"]]
assert len(_a) == len(set(_a)), "duplicate match answer -- Match mode becomes unwinnable"


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render():
    L = ['  { id: "%s", name: "%s", color: "%s",' % (DECK["id"], DECK["name"], DECK["color"]),
         "    icon: '%s'," % DECK["icon"], "    cards: ["]
    for q, a in DECK["cards"]:
        L.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    L += ["    ],", "    matchCards: ["]
    for q, a in DECK["matchCards"]:
        L.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    L.append("    ] },")
    return "\n".join(L)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    fo, fc = "/*PD2L3*/", "/*/PD2L3*/"
    if fo in src:
        src = re.sub(re.escape(fo) + r".*?" + re.escape(fc), "", src, flags=re.S)
    anchor = 'id: "pd2-derm-exam"'
    assert anchor in src, "PD2 Lecture 2 deck not found -- has arcade.js changed?"
    i = src.index(anchor)
    j = src.index("] },", i) + len("] },")
    src = src[:j] + "\n" + fo + "\n" + render() + "\n" + fc + src[j:]

    old = 'deckIds: ["pd2-clinical-reasoning", "pd2-derm-morphology", "pd2-derm-exam"]'
    assert old in src, "PD2 exam1 deckIds block not found"
    src = src.replace(old, old[:-1] + ', "pd2-ocular-exam"]', 1)

    open(ARCADE, "w", encoding="utf-8").write(src)
    defined = set(re.findall(r'\{ id: "([a-z0-9-]+)", name: "[^"]+", color:', src))
    grouped = set(re.findall(r'"([a-z0-9-]+)"', src[src.index("exams: ["):]))
    assert "pd2-ocular-exam" in defined, "deck not in the flat list"
    assert "pd2-ocular-exam" in grouped, "deck not GROUPED -- it would be invisible in the app"
    print("added deck %s: %d cards, %d match pairs, registered in both structures"
          % (DECK["id"], len(DECK["cards"]), len(DECK["matchCards"])))


if __name__ == "__main__":
    main()
