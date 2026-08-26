#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Clin Path I Lecture 4 (Ophthalmic Pathophysiology) Arcade deck.

MECHANISM ONLY -- no card asks what to do about anything. CMS I Exam 2 covers
this same condition list from the management side.

NO CARD TURNS ON THE NORMAL INTRAOCULAR PRESSURE: the deck says 10-21 on slide
24 and about 6-19 on slide 25. Asserted below. The acute spike (>50) is not
disputed and is carded.

Arcade has no image support, so the recognition half -- what a detached retina
or a drusen-covered macula actually looks like -- lives in the guide's four
figures. What is here is the verbal half.
"""
import os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# an eye with a pupil
ICON = ('<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>'
        '<circle cx="12" cy="12" r="2.5"/>')

DECK = dict(
    id="cp-ophthalmic-pathophys",
    name="Ophthalmic Pathophysiology",
    color="accent1",
    icon=ICON,
    cards=[
  ["Which three structures form the uvea?", "The choroid, the ciliary body and the iris."],
  ["Which two structures form the fibrous outer tunic?", "The sclera and the cornea."],
  ["How is the avascular cornea oxygenated?", "By direct contact with air and tears."],
  ["What share of refraction depends on the cornea?", "About seventy per cent."],
  ["Which tissue has the highest oxygen consumption in the body?", "The retina — higher even than the cerebral cortex."],
  ["What are the three non-negotiable requirements for vision?", "Image formation, photoreceptor excitation, and neural transmission."],
  ["What kind of potential do photoreceptors fire?", "Hyperpolarising."],
  ["How many rods, and what are they for?", "About 120 million — dim light and peripheral vision."],
  ["How many cones, and where are they?", "About 6 million — concentrated in the fovea centralis within the macula."],
  ["What are the three jobs of the retinal pigment epithelium?", "Absorbing scattered light, phagocytosing spent photoreceptor outer segments, and maintaining the blood-retinal barrier."],
  ["Which interneurons modulate the retinal signal?", "Bipolar, horizontal and amacrine cells."],
  ["Why is the optic disc a blind spot?", "It has no rods or cones."],
  ["Where is aqueous humour produced?", "By the non-pigmented epithelium of the ciliary body, into the posterior chamber."],
  ["What is the aqueous drainage route?", "Trabecular meshwork, then the canal of Schlemm, then the episcleral veins."],
  ["What is the vitreous made of?", "Water, type two collagen and hyaluronic acid."],
  ["What happens to the vitreous with age, and why does it matter?", "It liquefies — and liquefied vitreous is what can pass through a retinal break."],
  ["MYOPIA: what is the globe geometry?", "The axial globe is too LONG, so the focal point falls in FRONT of the retina."],
  ["HYPEROPIA: what is the globe geometry?", "The axial globe is too SHORT, so the focal point falls BEHIND the retina."],
  ["What causes astigmatism?", "Irregular corneal or lens curvature creating non-spherical focal points."],
  ["Why does astigmatism blur everything rather than near or far?", "The focal point does not land correctly anywhere, so nothing comes into sharp focus."],
  ["PRESBYOPIA: what is the mechanism?", "The lens loses elasticity through sclerosis, so it can no longer change shape to accommodate."],
  ["What does the A in PERRLA stand for?", "Accommodation."],
  ["Strabismus is which kind of problem?", "Mechanical — ocular misalignment, so the visual axes miss corresponding retinal points."],
  ["Name the four strabismus subtypes.", "Esotropia in, exotropia out, hypertropia up, hypotropia down."],
  ["Amblyopia is which kind of problem?", "A visual deficit — reduced best-corrected acuity from abnormal visual development."],
  ["What is the amblyopia treatment window, and why does it close?", "Before age seven to eight, because that is when the visual system stops being plastic."],
  ["CATARACT: what is the senile mechanism?", "Progressive insoluble aggregation of lens crystallin proteins."],
  ["CATARACT: what is the diabetic mechanism?", "Glucose is converted to sorbitol, causing osmotic swelling of the lens."],
  ["Which drug class causes cataract?", "Chronic corticosteroids."],
  ["What is found on ophthalmoscopy in cataract?", "Loss of the normal red reflex, with a white opacity through the pupil when severe."],
  ["How does a cataract present?", "Gradual, painless, bilateral blurring with glare around headlights at night, monocular diplopia and altered colour perception."],
  ["GLAUCOMA: what is the pathological hallmark?", "Raised pressure compresses retinal ganglion cell axons, causing apoptosis and progressive optic disc cupping."],
  ["Above what cup-to-disc ratio is cupping described?", "Greater than 0.5."],
  ["OPEN-ANGLE glaucoma: what is the mechanism?", "The angle stays open, but microscopic resistance in the trabecular meshwork impairs outflow."],
  ["What is the clinical pitfall of open-angle glaucoma?", "It is asymptomatic until severe peripheral loss — tunnel vision — has already happened."],
  ["ANGLE-CLOSURE glaucoma: what is the mechanism?", "Mydriasis displaces the iris forward against the cornea (iris bombé), blocking outflow completely."],
  ["How high does pressure spike in acute angle closure?", "Above 50 mmHg."],
  ["How does acute angle closure present?", "Severe eye pain, headache, halos around lights, cloudy cornea, a fixed mid-dilated pupil, and nausea and vomiting."],
  ["RHEGMATOGENOUS detachment: what is the mechanism?", "A full-thickness tear lets liquefied vitreous into the subretinal space, peeling the retina off the pigment epithelium."],
  ["TRACTIONAL detachment: what is the mechanism?", "Proliferative fibrovascular membranes on the retinal surface physically pull the retina off."],
  ["EXUDATIVE detachment: what is the mechanism?", "Subretinal fluid accumulates with no tear and no traction — the blood-retinal barrier has broken down."],
  ["Which detachment does proliferative diabetic retinopathy cause?", "Tractional."],
  ["Name three causes of exudative detachment.", "Severe malignant hypertension, sarcoidosis and choroidal melanoma."],
  ["What are the symptoms of rhegmatogenous detachment?", "Flashing lights, a shower of floaters, then a curtain falling across the field."],
  ["DRY macular degeneration: what is the hallmark?", "Drusen — discrete yellow extracellular debris beneath the pigment epithelium and Bruch membrane."],
  ["What are drusen made of?", "Lipofuscin and apolipoproteins."],
  ["WET macular degeneration: what is the mechanism?", "Hypoxia and inflammation trigger choroidal neovascularisation beneath the pigment epithelium into the subretinal space."],
  ["What share of severe blindness does wet macular degeneration cause?", "About ninety per cent."],
  ["What does the deck say about the pathogenesis of macular degeneration?", "It is unknown, for both forms."],
  ["Which is the leading cause of new-onset blindness in US adults 20 to 74?", "Diabetic retinopathy."],
  ["Which is the leading cause of new-onset blindness in US adults over 75?", "Macular degeneration."],
  ["What initiates the diabetic retinopathy cascade?", "Chronic hyperglycaemia damages capillaries and endothelial basement membranes, causing occlusion and hypoxia."],
  ["What drives non-proliferative to proliferative retinopathy?", "Severe ischaemia upregulates vascular endothelial growth factor, producing neovascularisation."],
  ["Where do hard exudates sit and what are they?", "Lipid deposits in the outer plexiform layer."],
  ["Where do cotton-wool spots sit and what are they?", "Nerve fibre layer ischaemia or infarction."],
  ["Which retinal fibres cross at the chiasm?", "The NASAL fibres — and they carry the TEMPORAL visual fields."],
  ["Trace the visual pathway.", "Optic disc, optic nerve, chiasm, optic tract, lateral geniculate nucleus, optic radiation, occipital cortex."],
  ["Lesion at the OPTIC NERVE gives what?", "Monocular blindness."],
  ["Lesion at the OPTIC CHIASM gives what, and from what?", "Bitemporal hemianopsia — most commonly from a pituitary adenoma."],
  ["Lesion at the OPTIC TRACT gives what?", "Contralateral homonymous hemianopsia."],
  ["Which three lesion sites did the lecturer say to know best?", "Optic nerve, optic chiasm and optic tract."],
  ["Why does losing one eye cost depth perception?", "The binocular overlap is what produces three-dimensional vision."],
  ["EPISCLERITIS vs SCLERITIS", "Episcleritis is a self-limiting superficial blush, not vision-threatening. Scleritis is deep boring pain, vision-threatening, with scleral melting risk."],
  ["Which systemic diseases go with SCLERITIS?", "Rheumatoid arthritis, granulomatosis with polyangiitis and systemic vasculitis."],
  ["Which systemic diseases go with ANTERIOR UVEITIS?", "Lupus, psoriatic arthritis, inflammatory bowel disease and ankylosing spondylitis."],
  ["What is found in the anterior chamber in anterior uveitis?", "White blood cells and flare."],
  ["What is a hypopyon?", "Pus in the anterior chamber."],
  ["Which organism threatens contact lens wearers in keratitis?", "Pseudomonas."],
  ["What anatomically separates orbital from periorbital cellulitis?", "The orbital septum — orbital cellulitis has breached it and lies posterior to the globe."],
  ["Which findings mark ORBITAL cellulitis?", "Proptosis, decreased extraocular movement, and a risk of optic nerve compression."],
  ["BLEPHARITIS: what is the mechanism?", "Meibomian gland obstruction alters tear film composition, causing excessive evaporation and lid margin irritation."],
  ["DRY EYE: what is the common downstream step?", "Raised tear osmolarity damaging the corneal epithelium — from either aqueous deficiency or excess evaporation."],
  ["What is the classical finding in herpes simplex epithelial keratitis?", "A dendritic corneal ulcer with terminal bulbs on fluorescein staining."],
  ["Which nerve distribution does herpes zoster ophthalmicus follow?", "The first division of the trigeminal nerve."],
  ["What is Hutchinson sign and why does it matter?", "A vesicle on the tip of the nose — it means the nasociliary branch is involved, so ocular risk is high."],
  ["What separates a pterygium from a pinguecula?", "The pterygium crosses the limbus onto the cornea; the pinguecula does not."],
  ["CHALAZION vs HORDEOLUM", "Chalazion is chronic, non-tender and STERILE — a granulomatous lipogranuloma of a blocked meibomian gland. Hordeolum is an acute tender ABSCESS."],
  ["Which glands make the lipid layer of the tear film?", "The meibomian glands, within the tarsal plates."],
  ["ABRASION vs ULCER: what is the anatomical line?", "An abrasion is epithelium only; an ulcer penetrates the basement membrane into the stroma."],
  ["What melts the tissue in a corneal ulcer?", "Bacterial collagenases."],
  ["DACRYOCYSTITIS vs DACRYOADENITIS", "Dacryocystitis is the lacrimal SAC at the medial canthus. Dacryoadenitis is the lacrimal GLAND at the superotemporal rim, with an S-shaped lid."],
  ["What causes a subconjunctival haemorrhage?", "Rupture of delicate episcleral or conjunctival capillaries beneath the conjunctiva."],
  ["What is xanthelasma associated with?", "Hyperlipidaemia."],
    ],
    matchCards=[
  ["Myopia", "Globe too LONG; image in front of retina"],
  ["Hyperopia", "Globe too SHORT; image behind retina"],
  ["Astigmatism", "Irregular curvature; no single focal point"],
  ["Presbyopia", "Lens HARDENS; accommodation fails"],
  ["Open-angle glaucoma", "Trabecular resistance; silent until tunnel vision"],
  ["Angle-closure glaucoma", "Iris bombé; spike above 50 mmHg"],
  ["Senile cataract", "Crystallin protein aggregation"],
  ["Diabetic cataract", "Glucose to sorbitol; osmotic swelling"],
  ["Rhegmatogenous detachment", "Full-thickness TEAR admits vitreous"],
  ["Tractional detachment", "Fibrovascular membranes PULL"],
  ["Exudative detachment", "Fluid, NO tear and NO traction"],
  ["Dry macular degeneration", "DRUSEN under the pigment epithelium"],
  ["Wet macular degeneration", "Choroidal neovascularisation; ~90% of blindness"],
  ["Optic nerve lesion", "Monocular blindness"],
  ["Optic chiasm lesion", "Bitemporal hemianopsia; pituitary adenoma"],
  ["Optic tract lesion", "Contralateral homonymous hemianopsia"],
  ["Scleritis", "Deep boring pain; rheumatoid arthritis, vasculitis"],
  ["Episcleritis", "Superficial blush; self-limiting"],
  ["Chalazion", "Chronic, non-tender, STERILE granuloma"],
  ["Hordeolum", "Acute, tender ABSCESS"],
  ["Pterygium", "CROSSES the limbus onto the cornea"],
  ["Pinguecula", "Yellow nodule that does NOT cross"],
  ["Hard exudates", "Lipid, outer plexiform layer"],
  ["Cotton-wool spots", "Nerve fibre layer ischaemia"],
    ])

# ---- guard: the disputed pressure is never carded ---------------------------
_IOP = re.compile(r"\b10\s*(?:to|-|–)\s*21\b|\b6\s*(?:to|-|–)\s*19\b")
_bad = [p[0][:50] for p in DECK["cards"] + DECK["matchCards"]
        if any(_IOP.search(t) for t in p)]
assert not _bad, ("a card turns on the normal intraocular pressure, which this deck "
                  "states two different ways: %r" % _bad[:3])

# ---- guard: mechanism, never management ------------------------------------
_MGMT = re.compile(r"first[- ]line|treatment of choice|how (?:do|would) you treat|"
                   r"what is the treatment|drug of choice|next step", re.I)
_mg = [p[0][:50] for p in DECK["cards"] if any(_MGMT.search(t) for t in p)]
assert not _mg, "management card in a pathophysiology deck: %r" % _mg[:3]

_p = [c[0] for c in DECK["cards"]]
assert len(_p) == len(set(_p)), "duplicate card prompt: %r" % [x for x in _p if _p.count(x) > 1][:3]
_a = [c[1] for c in DECK["matchCards"]]
assert len(_a) == len(set(_a)), "duplicate match answer -- Match mode becomes unwinnable"


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render():
    lines = ['  { id: "%s", name: "%s", color: "%s",' % (DECK["id"], DECK["name"], DECK["color"]),
             "    icon: '%s'," % DECK["icon"], "    cards: ["]
    for q, a in DECK["cards"]:
        lines.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    lines.append("    ],")
    lines.append("    matchCards: [")
    for q, a in DECK["matchCards"]:
        lines.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    lines.append("    ] },")
    return "\n".join(lines)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    fo, fc = "/*CPL4*/", "/*/CPL4*/"
    if fo in src:
        src = re.sub(re.escape(fo) + r".*?" + re.escape(fc), "", src, flags=re.S)
    anchor = 'id: "cp-abnormal-cell-growth"'
    assert anchor in src, "Clin Path Lecture 3 deck not found -- has arcade.js changed?"
    i = src.index(anchor)
    j = src.index("] },", i) + len("] },")
    src = src[:j] + "\n" + fo + "\n" + render() + "\n" + fc + src[j:]
    open(ARCADE, "w", encoding="utf-8").write(src)
    print("added deck %s: %d cards, %d match pairs"
          % (DECK["id"], len(DECK["cards"]), len(DECK["matchCards"])))


if __name__ == "__main__":
    main()
