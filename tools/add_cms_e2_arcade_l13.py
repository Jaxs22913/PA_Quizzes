#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 2 Lecture 13 Arcade decks.

Three decks, split by how the material is actually revised: the chronic
disorders, the cataract types, and the tumours. One deck per topic per the
arcade content policy, and every card is a SINGLE ATOMIC FACT -- Match and
Sprint are unplayable when the answer is a paragraph.

arcade.js keeps decks in a flat list AND in a separate class/exam grouping. A
deck in one but not the other is invisible in the app, so this asserts both.
Idempotent.
"""
import io, os

ARCADE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "arcade.js")
EYE = ('<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>'
       '<circle cx="12" cy="12" r="2.5"/>')
LENS = ('<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="3.5"/>'
        '<path d="M12 4v2M12 18v2"/>')
TUMOR = ('<circle cx="12" cy="12" r="8"/><circle cx="10" cy="11" r="3" />'
         '<path d="M14 15c2 1 3 2 4 4"/>')

DECKS = [
 dict(id="cms-chronic-vision-loss", name="Chronic Vision Loss", color="accent", icon=EYE, cards=[
  ["Most common cause of vision loss in children?", "Amblyopia."],
  ["What share of children does amblyopia affect?", "3 to 5 percent."],
  ["Three routes into amblyopia?", "Strabismus, anisometropia, deprivation."],
  ["In the occlusion objection test, when does the child object?", "When the GOOD eye is covered."],
  ["Acuity difference that defines unilateral amblyopia?", "Two lines or more."],
  ["By what age should every child be screened for amblyopia?", "Under five."],
  ["Which eye is patched in amblyopia?", "The good eye."],
  ["Best outcome in amblyopia if treated before what age?", "Seven, and better before five."],
  ["What does not recover if amblyopia is treated late?", "Stereo vision."],
  ["Diplopia that vanishes when either eye is covered is called what?", "Binocular diplopia."],
  ["Which test elicits fixation of a misaligned eye?", "The cover test."],
  ["Most common form of glaucoma?", "Primary open-angle."],
  ["Which field is lost first in open-angle glaucoma?", "Peripheral."],
  ["Optic disc change that defines glaucomatous damage?", "Cupping."],
  ["Can glaucoma damage already done be reversed?", "No. Treatment preserves what is left."],
  ["Two ways glaucoma drops lower pressure?", "Less aqueous made, or more drained."],
  ["What share of macular degeneration is dry?", "About 80 percent."],
  ["Which vision does macular degeneration take?", "Central, with distortion."],
  ["Findings that define dry macular degeneration?", "Drusen, pigmentary change, atrophy."],
  ["What makes macular degeneration wet?", "Choroidal neovascularisation bleeding into the retina."],
  ["Home monitoring tool for macular degeneration?", "An Amsler grid."],
  ["Single most useful advice in macular degeneration?", "Stop smoking."],
  ["Treatment reserved for wet macular degeneration?", "Intravitreal anti-VEGF injection."],
  ["Why was beta carotene dropped from AREDS?", "It raised lung cancer risk in smokers."],
  ["Classic patient for idiopathic intracranial hypertension?", "Overweight woman of childbearing age."],
  ["Ear symptom of idiopathic intracranial hypertension?", "Pulsatile tinnitus."],
  ["Cranial nerve palsy seen with raised intracranial pressure?", "Abducens, the sixth."],
  ["First test in suspected idiopathic intracranial hypertension?", "MRI brain with MR venography."],
  ["What confirms idiopathic intracranial hypertension?", "Elevated opening pressure on lumbar puncture."],
  ["Drug started promptly in idiopathic intracranial hypertension?", "Acetazolamide."],
  ["Only durable fix for idiopathic intracranial hypertension?", "Weight loss."],
  ["Which refractive error has a long eyeball?", "Myopia."],
  ["Which lens corrects myopia?", "A concave, negative dioptre lens."],
  ["Which lens corrects hyperopia?", "A convex, positive dioptre lens."],
  ["Which lens corrects astigmatism?", "A toric lens."],
  ["Which cause of blurry vision takes colour vision?", "Optic neuropathy."],
 ]),

 dict(id="cms-cataract", name="Cataract", color="accent2", icon=LENS, cards=[
  ["Most common cause of cataract overall?", "Ageing."],
  ["Which cataract browns the central lens?", "Nuclear."],
  ["Which vision does a nuclear cataract blur more?", "Distance, more than near."],
  ["What is the refractive shift in nuclear cataract?", "A myopic shift."],
  ["Which cataract gives spoke-like peripheral opacities?", "Cortical."],
  ["Main complaint once a cortical cataract reaches the centre?", "Glare."],
  ["Which cataract is plate-like behind the lens?", "Posterior subcapsular."],
  ["Posterior subcapsular cataract is classically under what age?", "Fifty."],
  ["Two associations with posterior subcapsular cataract?", "Corticosteroids and diabetes."],
  ["Posterior subcapsular symptoms get better after what?", "Dilation."],
  ["Most common paediatric cataract type?", "Zonular."],
  ["Which paediatric cataract is central and so caught earlier?", "Polar."],
  ["Does a cataract alone cause a relative afferent pupillary defect?", "No. Never."],
  ["Advanced cataract sign on ophthalmoscopy?", "Loss of the red reflex."],
  ["White pupillary reflex is called what?", "Leukocoria."],
  ["Only treatment for cataract?", "Surgery, with a lens implant."],
  ["When is cataract surgery normally done?", "When it interferes with daily activities."],
  ["Why is a neonatal cataract operated early?", "To prevent amblyopia."],
  ["Vision clouds again years after cataract surgery. What is it?", "Posterior capsule opacification."],
  ["What treats posterior capsule opacification?", "A YAG laser."],
  ["Recovery rate after isolated cataract surgery?", "About 99 percent of eyes."],
  ["Cataract referral becomes urgent when?", "If secondary to uveitis or glaucoma."],
 ]),

 dict(id="cms-ocular-tumors", name="Ocular Tumors", color="accent4", icon=TUMOR, cards=[
  ["Sign of retinoblastoma noticed in photographs?", "Leukocoria, a white pupil."],
  ["Who gets retinoblastoma?", "Young children, almost exclusively."],
  ["Why is retinoblastoma not biopsied?", "It risks seeding the tumour."],
  ["How is retinoblastoma diagnosed then?", "Dilated examination plus imaging."],
  ["Screening every primary care clinician should do in infants?", "The red reflex."],
  ["Retinoblastoma with a family history: seen by when?", "Within the first eight weeks of life."],
  ["Untreated retinoblastoma mortality?", "Close to 100 percent."],
  ["Treated retinoblastoma five-year survival?", "Over 95 percent."],
  ["No recurrence at five years in retinoblastoma means what?", "Cured."],
  ["Most common eye cancer in adults?", "Uveal melanoma."],
  ["Which three structures make up the uveal tract?", "Choroid, ciliary body, iris."],
  ["Typical symptom of uveal melanoma?", "None. Usually found incidentally."],
  ["Feature that separates iris melanoma from a freckle?", "A prominent feeder vessel."],
  ["Size that raises concern in an iris lesion?", "Over 3 mm across and over 1 mm deep."],
  ["Which half of the iris do these lesions favour?", "The inferior half."],
  ["A tumour pulling the pupil out of shape is called what?", "Corectopia."],
  ["What is fine needle aspiration used for in uveal melanoma?", "Molecular prognostic testing."],
  ["Most common treatment for uveal melanoma now?", "Radiation therapy."],
  ["Most common site of metastasis for ocular melanoma?", "The liver."],
  ["Ten-year mortality of uveal melanoma overall?", "About 32 percent."],
  ["Mortality of iris melanoma specifically?", "4 to 10 percent."],
  ["Why does iris melanoma do better?", "It is visible, so it is found earlier."],
  ["Typical iris nevus: size and elevation?", "Under 3 mm and flat."],
  ["Is an iris nevus vascular?", "No."],
  ["When does an iris nevus usually appear?", "Around puberty."],
  ["Tan bilateral iris nodules suggest what condition?", "Neurofibromatosis type 1."],
  ["What are those nodules called?", "Lisch nodules."],
  ["Conjunctival melanoma appearance?", "Raised and vascular."],
  ["Conjunctival nevus appearance?", "Flat, with clear cysts."],
  ["Bilateral symmetric conjunctival pigment suggests what?", "Racial melanosis."],
 ]),
]


def card_js(c):
    return '      ["%s", "%s"],' % (c[0].replace('"', '\\"'), c[1].replace('"', '\\"'))


def deck_js(d):
    return ('  { id: "%s", name: "%s", color: "%s",\n'
            "    icon: '%s',\n"
            "    cards: [\n%s\n    ]},\n\n") % (
        d["id"], d["name"], d["color"], d["icon"],
        "\n".join(card_js(c) for c in d["cards"]))


def main():
    t = io.open(ARCADE, encoding="utf-8").read()
    before = len(t)

    anchor = '  { id: "cms-ophthalmology-1",'
    assert t.count(anchor) == 1
    for d in DECKS:
        if '{ id: "%s",' % d["id"] in t:
            continue
        t = t.replace(anchor, deck_js(d) + anchor)

    old_group = ('    { id: "exam2", name: "Exam 2", deckIds: [\n'
                 '      "cms-ophthalmology-1", "cms-neuro-ophthalmology", "cms-acute-vision-loss"\n'
                 '    ] }')
    new_group = ('    { id: "exam2", name: "Exam 2", deckIds: [\n'
                 '      "cms-ophthalmology-1", "cms-neuro-ophthalmology", "cms-acute-vision-loss",\n'
                 '      "cms-chronic-vision-loss", "cms-cataract", "cms-ocular-tumors"\n'
                 '    ] }')
    if old_group in t:
        t = t.replace(old_group, new_group, 1)

    io.open(ARCADE, "w", encoding="utf-8").write(t)
    print("arcade.js %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    cms = t.split('name: "Clinical Medicine and Surgery I"')[1][:1200]
    for d in DECKS:
        assert '{ id: "%s",' % d["id"] in t, "%s missing from the flat deck list" % d["id"]
        assert '"%s"' % d["id"] in cms, "%s missing from the CMS exam grouping" % d["id"]
        print("  %-26s %3d cards, in both the list and the grouping" % (d["id"], len(d["cards"])))


if __name__ == "__main__":
    main()
