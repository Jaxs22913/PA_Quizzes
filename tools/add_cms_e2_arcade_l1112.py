#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 2 Lecture 11 and 12 Arcade decks.

One deck per topic, per the arcade content policy, and every card is a single
atomic fact -- Match and Sprint are unplayable when an answer is a paragraph.

arcade.js keeps decks in a flat list AND a separate class/exam grouping at the
bottom. A deck present in one but not the other is invisible in the app, so
this asserts both. Idempotent.
"""
import io, os, re

ARCADE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "arcade.js")
EYE = ('<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>'
       '<circle cx="12" cy="12" r="2.5"/><path d="M4 4l16 16"/>')
NERVE = ('<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3"/>'
         '<path d="M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M18.4 5.6l-2.1 2.1M7.7 16.3l-2.1 2.1"/>')

DECKS = [
 dict(id="cms-neuro-ophthalmology", name="Neuro-Ophthalmology", color="accent3", icon=NERVE, cards=[
  ["Nystagmus is named for the direction of which beat?", "The fast beat."],
  ["Most common form of jerk nystagmus?", "Horizontal."],
  ["Nystagmus is symptomatic unless acquired before what age?", "Age 8."],
  ["Often the primary symptom of nystagmus?", "Vertigo."],
  ["Sensation that the environment is moving back and forth?", "Oscillopsia."],
  ["Pupil size is determined by what?", "The average illumination detected by each eye."],
  ["Afferent pupillary pathway ends by synapsing where?", "The pretectal nuclei."],
  ["Each pretectal nucleus sends impulses to which nuclei?", "Both Edinger-Westphal nuclei."],
  ["Parasympathetic pupillary fibres travel along which cranial nerve?", "Cranial nerve III."],
  ["Parasympathetic stimulation of the iris produces what?", "Miosis."],
  ["Sympathetic stimulation of the iris produces what?", "Mydriasis."],
  ["Where do first-order sympathetic neurons synapse?", "The ciliospinal centre of Budge, C8 to T2."],
  ["Which sympathetic neuron loops over the lung apex?", "The second-order neuron."],
  ["Which sympathetic neuron follows the carotid artery?", "The third-order neuron."],
  ["Opioid overdose does what to the pupils?", "Constricts them."],
  ["Antidote for opioid overdose?", "Naloxone."],
  ["In accommodation, the ciliary muscle contracts and does what to the lens?", "Makes it more convex, increasing refractive power."],
  ["In accommodation, what do the globes do?", "Both adduct, converging."],
  ["What is light-near dissociation?", "No pupil reaction to light, but a preserved reaction to near."],
  ["Anisocoria worse in the DARK means which pupil is abnormal?", "The small one."],
  ["Anisocoria worse in the LIGHT means which pupil is abnormal?", "The large one."],
  ["Anisocoria equal in light and dark is called what?", "Physiologic anisocoria."],
  ["Physiologic anisocoria is usually under how many millimetres?", "0.4 millimetres."],
  ["An anticholinergic pupil is usually how large?", "8 millimetres or more."],
  ["A Marcus Gunn pupil indicates a defect in which limb?", "The afferent limb."],
  ["Marcus Gunn pupil localises the lesion where?", "The retina or the optic nerve."],
  ["Swinging the light to a Marcus Gunn eye does what?", "Both pupils dilate."],
  ["Classic triad of Horner syndrome?", "Ptosis, miosis and anhidrosis."],
  ["Hallmark of the miosis in Horner syndrome?", "Dilation lag."],
  ["Horner anisocoria is most evident how long after dimming the lights?", "The first 4 to 5 seconds."],
  ["Diagnostic drops for Horner syndrome?", "Dilute apraclonidine."],
  ["Apraclonidine does what to a Horner pupil?", "Dilates it."],
  ["First-order Horner causes?", "Brainstem stroke or tumour, and cord lesions above T1."],
  ["Second-order Horner causes?", "Pancoast tumour and thyroid cancer."],
  ["Third-order Horner causes?", "Carotid dissection and cavernous sinus pathology."],
  ["Horner syndrome with neck pain after trauma suggests what?", "Carotid artery dissection."],
  ["Argyll Robertson pupils are what size, and how many?", "Small, and bilateral."],
  ["Argyll Robertson pupils react to what?", "Near, but not to light."],
  ["Classic cause of an Argyll Robertson pupil?", "Tertiary syphilis."],
  ["Posterior column involvement in tertiary syphilis is called what?", "Tabes dorsalis."],
  ["Argyll Robertson lesion sits where?", "The pretectal area of the dorsal midbrain."],
  ["An Adie tonic pupil is what size?", "Large, with a poor light response."],
  ["Adie pupil damage occurs at which structure?", "The ciliary ganglion."],
  ["Adie pupil typically affects whom?", "Women in their thirties."],
  ["Slit lamp finding in an Adie pupil?", "Sector paralysis of the iris."],
  ["Which reflexes are often absent in Holmes-Adie syndrome?", "Achilles and patellar."],
  ["Superior division of cranial nerve III supplies what?", "Levator palpebrae and superior rectus."],
  ["Most common cause of a third nerve palsy?", "Microvascular disease from diabetes or hypertension."],
  ["Most dreaded cause of a third nerve palsy?", "A posterior communicating artery aneurysm."],
  ["A pupil-INVOLVED third nerve palsy needs what?", "STAT computed tomography angiography of the head or magnetic resonance angiography of the brain."],
  ["A pupil-SPARED third nerve palsy needs what?", "Imaging, but not urgently."],
  ["Cranial nerve IV supplies which muscle?", "The superior oblique."],
  ["The superior oblique does what to the eye?", "Intorts and depresses it."],
  ["Which cranial nerve arises from the dorsal brainstem and crosses?", "Cranial nerve IV."],
  ["Type of diplopia in a fourth nerve palsy?", "Vertical and binocular."],
  ["A fourth nerve palsy makes the patient tilt the head which way?", "Away from the affected eye."],
  ["Most common cause of an isolated fourth nerve palsy?", "Congenital, even in adults."],
  ["Cranial nerve VI supplies which muscle?", "The lateral rectus."],
  ["Type of diplopia in a sixth nerve palsy?", "Horizontal and binocular."],
  ["Most common cause of a sixth nerve palsy in children?", "Intracranial tumours."],
  ["Most common cause of a sixth nerve palsy in adults?", "Microvascular disease."],
  ["Imaging for an isolated atraumatic fourth or sixth nerve palsy?", "Magnetic resonance imaging of the brain, with and without contrast."],
  ["How long is a traumatic nerve palsy observed before correction?", "About 6 months."],
  ["Interim measure for binocular diplopia?", "Patch one eye."],
  ["Which muscle elevates the upper eyelid, and via which nerve?", "Levator palpebrae superioris, via cranial nerve III."],
  ["Muller's muscle is supplied by what, and gives how much lift?", "The sympathetic system, giving 1 to 2 millimetres."],
  ["Which muscle closes the eyelids, and via which nerve?", "Orbicularis oculi, via cranial nerve VII."],
  ["Ptosis with a SMALL pupil suggests what?", "Horner syndrome."],
  ["Ptosis with a LARGE pupil suggests what?", "A third nerve palsy."],
  ["Ptosis that varies through the day suggests what?", "Myasthenia gravis."],
  ["Levator function in Horner syndrome?", "Normal."],
  ["An optic nerve lesion produces which field defect?", "Total blindness of that eye."],
  ["A chiasmal lesion produces which field defect?", "Bitemporal hemianopsia."],
  ["An optic tract lesion produces which field defect?", "Homonymous hemianopsia."],
  ["An optic radiation lesion produces which field defect?", "A superior quadrantanopia."],
  ["A striate cortex lesion produces which field defect?", "Homonymous hemianopsia with macular sparing."],
  ["A monocular field defect localises where?", "Pre-chiasmal."],
  ["A homonymous field defect localises where?", "Post-chiasmal."],
 ]),

 dict(id="cms-acute-vision-loss", name="Acute Vision Loss", color="accent4", icon=EYE, cards=[
  ["Sudden acute vision loss is what until proven otherwise?", "A stroke."],
  ["Which imaging does every patient with sudden vision loss receive?", "Magnetic resonance angiography."],
  ["Four questions that separate these diagnoses?", "One eye or both, sudden or gradual, central or peripheral, painful or painless."],
  ["Which two diagnoses are painful?", "Acute angle-closure glaucoma, and optic neuritis on eye movement."],
  ["Which two diagnoses use the word curtain?", "Amaurosis fugax and retinal detachment."],
  ["What separates the two curtain diagnoses?", "Duration. Amaurosis fugax lifts in seconds to minutes; a detachment stays."],
  ["Amaurosis fugax lasts how long?", "A few seconds to minutes."],
  ["Another name for amaurosis fugax?", "Fleeting blindness."],
  ["Most common cause of amaurosis fugax?", "A transient ischemic attack from a retinal embolus."],
  ["Two embolic sources in amaurosis fugax?", "Carotid and cardiac."],
  ["Vision loss lasting hours argues against what?", "A transient ischemic attack."],
  ["Study for a suspected carotid source?", "Carotid Doppler ultrasound."],
  ["Study for a suspected cardiac source?", "Echocardiogram."],
  ["What proportion of amaurosis fugax patients recover fully?", "About 85 percent."],
  ["Amaurosis fugax patients who do not recover progress to what?", "Central retinal artery occlusion."],
  ["Antiplatelet therapy after amaurosis fugax?", "Aspirin and clopidogrel."],
  ["Treatment for a carotid embolic source?", "Carotid endarterectomy."],
  ["Treatment for vasospastic amaurosis fugax?", "Calcium channel blockers."],
  ["Mechanism of acute angle-closure glaucoma?", "The iris blocks the drainage circuit."],
  ["Mechanism of chronic open-angle glaucoma?", "Trabecular meshwork abnormality by the canal of Schlemm, from aging."],
  ["Which glaucoma is more common?", "The chronic open-angle form."],
  ["Symptoms of acute angle-closure glaucoma?", "Severe eye pain, headache, nausea, vomiting and coloured halos."],
  ["Corneal finding in acute angle closure?", "A hazy cornea."],
  ["Intraocular pressure range in acute angle closure?", "40 to 80 millimetres of mercury."],
  ["Two instruments that measure the angle and pressure?", "Tonometry and gonioscopy."],
  ["First topical agents in acute angle closure?", "Pilocarpine or timolol."],
  ["Intravenous agent in acute angle closure?", "Acetazolamide, followed by mannitol or isosorbide."],
  ["Definitive treatment for acute angle closure?", "Laser peripheral iridotomy."],
  ["How soon after onset is iridotomy performed?", "One to two days."],
  ["What does iridotomy achieve?", "Fluid flows from the posterior to the anterior chamber."],
  ["Drug classes that precipitate angle closure?", "Systemic anticholinergics and nebulized bronchodilators."],
  ["Field loss pattern in chronic open-angle glaucoma?", "Peripheral first, which patients call tunnel vision."],
  ["Classic optic nerve sign of chronic glaucoma?", "Optic nerve cupping."],
  ["What is bayoneting?", "Blood vessels with narrow angulations at the disc."],
  ["Intraocular pressure in chronic open-angle glaucoma?", "May be normal or elevated."],
  ["First-line drops for chronic open-angle glaucoma?", "Latanoprost, tafluprost or timolol."],
  ["Treatment for refractory chronic glaucoma?", "Laser trabeculoplasty."],
  ["Definitive treatment for either glaucoma?", "Surgery."],
  ["Age and sex distribution of optic neuritis?", "18 to 45 years, and 75 percent female."],
  ["Causes of optic neuritis?", "Multiple sclerosis, autoimmune disease, postviral, or idiopathic."],
  ["Time course of optic neuritis?", "Hours to several days."],
  ["Pain characteristic of optic neuritis?", "Pain on eye movement."],
  ["Colour finding in optic neuritis?", "Loss of colour vision."],
  ["Disc appearance in optic neuritis?", "Often normal."],
  ["Pupil sign in optic neuritis?", "A relative afferent pupillary defect, or Marcus Gunn pupil."],
  ["Imaging for optic neuritis?", "Magnetic resonance imaging of brain and orbits, with and without contrast."],
  ["How many demyelinating lesions trigger neurology referral?", "At least two."],
  ["Prognosis of optic neuritis?", "Spontaneous recovery, usually normal vision within a year."],
  ["Recurrent optic neuritis carries a greater risk of what?", "Multiple sclerosis."],
  ["Retinal detachment commonly follows what?", "A retinal tear or hole."],
  ["Three types of retinal detachment?", "Rhegmatogenous, traction, and serous or exudative."],
  ["Retinal detachment is most common after what age?", "Age 50."],
  ["Risk factors for retinal detachment?", "Myopia, trauma, cataract extraction, diabetes, tumour and connective tissue disease."],
  ["What do new flashes and floaters represent?", "A retinal tear."],
  ["What happens if the macula becomes involved in a detachment?", "Sudden loss of vision in that eye."],
  ["Unusual feature of detachment vision loss?", "It changes with head position."],
  ["Fundus appearance of a detached retina?", "Elevated and grey, with folds."],
  ["Appearance of a retinal tear?", "Orange and crescent shaped."],
  ["Which is more sensitive for detachment, ultrasound or fundoscopy?", "Ultrasound."],
  ["Surgical options for retinal detachment?", "Laser photocoagulation, cryotherapy, pneumatic retinopexy, vitrectomy and scleral buckle."],
  ["Mechanism of central retinal vein occlusion?", "A thrombus occludes the vein."],
  ["Classic fundus description in vein occlusion?", "Blood and thunder."],
  ["Fundus findings in central retinal vein occlusion?", "Disc swelling, venous dilation, cotton wool spots and retinal haemorrhages."],
  ["Which is more common, artery or vein occlusion?", "Vein occlusion."],
  ["Mechanism of central retinal artery occlusion?", "An embolus, from carotid or cardiac source."],
  ["Retinal damage becomes irreversible how long after arterial occlusion?", "90 minutes."],
  ["Onset of vision loss in central retinal artery occlusion?", "Painless and profound, over a few seconds."],
  ["Visual acuity range in central retinal artery occlusion?", "Counting fingers to light perception."],
  ["Field pattern in central retinal artery occlusion?", "An island of vision in the temporal field."],
  ["Pupil finding in central retinal artery occlusion?", "Slow to direct light, but brisk when the other eye is illuminated."],
  ["Fundus finding in central retinal artery occlusion?", "Pale retinal swelling with a cherry-red spot at the fovea."],
  ["Initial treatment of central retinal artery occlusion?", "Inhaled oxygen and digital massage over the eyelid."],
  ["Why is anterior chamber paracentesis performed?", "To lower the intraocular pressure."],
  ["Thrombolytic window in central retinal artery occlusion?", "Within 8 hours of onset."],
  ["What appears weeks to months after a retinal occlusion?", "Neovascularization."],
  ["Confirmatory tests for the retinal occlusions?", "Colour fundus photography and fluorescein angiography."],
  ["How do the branch occlusions differ from the central ones?", "A smaller branch vessel is blocked, so only part of the retina is affected."],
  ["Which pressure is raised in papilledema?", "Intracranial pressure."],
  ["Causes of papilledema?", "Tumour, trauma, intracranial infection, haemorrhage and vitamin A toxicity."],
  ["Visual symptoms of papilledema?", "Flickering, blurry and double vision."],
  ["Systemic symptoms of papilledema?", "Nausea, vomiting and headache."],
  ["Fundus findings in papilledema?", "Engorged retinal veins and a swollen optic disc."],
  ["Which test confirms raised intracranial pressure?", "Lumbar puncture, showing an increased opening pressure."],
  ["Why image the head in papilledema?", "To rule out a mass lesion."],
  ["Findings that mark acute rather than chronic papilledema?", "Haemorrhages and cotton wool spots."],
  ["What happens in the atrophic phase of papilledema?", "The optic nerve axons have died."],
  ["How does papilledema differ from glaucoma at the disc?", "Papilledema pushes the disc out; glaucoma cups it in."],
  ["What share of anterior ischemic optic neuropathy is non-arteritic?", "90 to 95 percent."],
  ["Age range for non-arteritic anterior ischemic optic neuropathy?", "40 to 60 years."],
  ["What is a disc at risk?", "A small structural optic disc."],
  ["Associations of non-arteritic anterior ischemic optic neuropathy?", "Hypertension, diabetes, high cholesterol and sleep apnea."],
  ["Cause of arteritic anterior ischemic optic neuropathy?", "Giant cell, or temporal, arteritis."],
  ["Age threshold for arteritic anterior ischemic optic neuropathy?", "55 years and older."],
  ["Systemic symptoms of the arteritic form?", "Malaise, weight loss, fever, temporal headache, scalp tenderness and jaw claudication."],
  ["Which two blood tests are sent for suspected arteritis?", "Erythrocyte sedimentation rate and C-reactive protein."],
  ["Gold standard test for giant cell arteritis?", "Temporal artery biopsy."],
  ["Initial treatment for arteritic anterior ischemic optic neuropathy?", "Intravenous methylprednisolone for three days."],
  ["How long does the steroid course typically last?", "At least 6 to 12 months."],
  ["Which drug is added for ulcer prophylaxis with long-term steroids?", "Famotidine."],
  ["Disc appearance in anterior ischemic optic neuropathy?", "Swollen and pale."],
  ["Management of non-arteritic anterior ischemic optic neuropathy?", "Observation and cardiovascular risk factor modification."],
  ["Why avoid antihypertensives at bedtime in this condition?", "Nocturnal hypotension can worsen it."],
  ["Referral threshold for sudden visual loss?", "Emergent referral for anyone over 50."],
 ]),
]


def card_js(c):
    q = c[0].replace("\\", "\\\\").replace('"', '\\"')
    a = c[1].replace("\\", "\\\\").replace('"', '\\"')
    return '      ["%s", "%s"],' % (q, a)


def deck_js(d):
    return ('  { id: "%s", name: "%s", color: "%s",\n'
            "    icon: '%s',\n"
            "    cards: [\n%s\n    ]},\n\n") % (
        d["id"], d["name"], d["color"], d["icon"],
        "\n".join(card_js(c) for c in d["cards"]))


def main():
    t = io.open(ARCADE, encoding="utf-8").read()
    before = len(t)

    # 1. flat deck list -- insert immediately before the Lecture 10 deck
    anchor = '  { id: "cms-ophthalmology-1",'
    assert t.count(anchor) == 1
    for d in DECKS:
        if '{ id: "%s",' % d["id"] in t:
            continue
        t = t.replace(anchor, deck_js(d) + anchor)

    # 2. class/exam grouping -- a deck missing here is invisible in the app
    old_group = '    { id: "exam2", name: "Exam 2", deckIds: ["cms-ophthalmology-1"] }'
    new_group = ('    { id: "exam2", name: "Exam 2", deckIds: [\n'
                 '      "cms-ophthalmology-1", "cms-neuro-ophthalmology", "cms-acute-vision-loss"\n'
                 '    ] }')
    if old_group in t:
        t = t.replace(old_group, new_group)

    io.open(ARCADE, "w", encoding="utf-8").write(t)
    print("arcade.js %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    for d in DECKS:
        assert '{ id: "%s",' % d["id"] in t, "%s missing from the flat deck list" % d["id"]
        assert '"%s"' % d["id"] in t.split('name: "Clinical Medicine and Surgery I"')[1][:900], \
            "%s missing from the CMS exam grouping" % d["id"]
        print("  %-26s %3d cards, in both the list and the grouping" % (d["id"], len(d["cards"])))


if __name__ == "__main__":
    main()
