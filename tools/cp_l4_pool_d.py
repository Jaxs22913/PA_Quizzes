# -*- coding: utf-8 -*-
# Clinical Pathophysiology I Lecture 4 -- pool D.
# Objective 6 (glaucoma), 8 (retinal detachment), 9 (macular degeneration),
# 10 (visual field deficits by area of pathology), plus the diabetic
# retinopathy cascade.
#
# FOUR OF WEBSTER'S NAMED EXAM TOPICS LIVE HERE -- glaucoma, retinal
# detachment, macular degeneration and the visual pathway. All flagged kfe=True.
#
# THE DECK CONTRADICTS ITSELF ON NORMAL INTRAOCULAR PRESSURE:
#     slide 24  "IOP normal: 10-21 mmHg"
#     slide 25  "Normal IOP is about 6-19 mmHg"
# Two slides apart, same deck. Prof. Beck's PD2 deck independently gives
# 10-21, so 6-19 looks like the slip -- but this file does not adjudicate.
# NO QUESTION TURNS ON THE NORMAL VALUE. Questions use the ACUTE SPIKE figure
# (>50 mmHg), which appears once and is not disputed, and otherwise ask about
# mechanism. cp_l4_partition.py enforces this.
#
# THE VISUAL FIELD OBJECTIVE IS SCOPED TO A, B AND C. He said so twice:
# "these I wouldn't worry about that much ... know these better: optic nerve
# damage, optic chiasm damage, optic tract damage", and "D and E, you can know
# that if you want, but know A, B and C." D (optic radiation) and E (occipital
# cortex) are DEFERRED TO NEUROLOGY. They appear here only as distractors and
# in one question that states the scope itself.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "4. Ophthalmic Pathophysiology_STUDENT VERSION_v2.pptx"
def c(n): return f"{SRC}, Slide {n}"
def au(): return "Lecture recording, 26 August 2026"

IO6 = "f — Describe the pathogenesis of glaucoma"
IO8 = "h — Compare and contrast the pathogenesis of retinal detachment"
IO9 = "i — Describe the pathologic process of macular degeneration"
IO10 = "j — Describe visual field deficits according to the area of pathology"
IO3 = "c — Describe the molecular mechanisms of common ocular pathologies"

POOL_D = [
 # ---- glaucoma ----
 dict(topic="Glaucoma mechanism", io=IO6, slot="etiology", kfe=True,
   q="What is the pathological hallmark of glaucoma?",
   opts=[
     ["Raised pressure compresses retinal ganglion cell axons, causing apoptosis and progressive optic disc cupping",
      "Correct — the deck's causal chain from pressure to nerve loss."],
     ["Raised pressure opacifies the crystalline lens",
      "That is cataract, which pressure does not cause."],
     ["Raised pressure detaches the neurosensory retina from the pigment epithelium",
      "That is retinal detachment, with different mechanisms."],
     ["Raised pressure causes neovascular growth on the optic disc",
      "That is proliferative diabetic retinopathy."]],
   c=0, cite=c(25)),

 dict(topic="Glaucoma mechanism", io=IO6, slot="test finding", kfe=True,
   q="Above what cup-to-disc ratio does the deck describe progressive optic disc cupping?",
   opts=[
     ["Greater than 0.5", "Correct — the deck's threshold for an increased cup-to-disc ratio."],
     ["Greater than 0.2", "Below the deck's stated threshold."],
     ["Greater than 0.8", "Above the deck's stated threshold."],
     ["Greater than 1.0", "A ratio above one is not anatomically possible."]],
   c=0, cite=c(25)),

 dict(topic="Open-angle glaucoma", io=IO6, slot="etiology", kfe=True,
   q="What is the mechanism of primary open-angle glaucoma?",
   opts=[
     ["The iridocorneal angle stays open but microscopic resistance in the trabecular meshwork impairs outflow, raising pressure gradually",
      "Correct — the angle is open; the obstruction is microscopic and downstream."],
     ["The iridocorneal angle narrows anatomically and blocks outflow suddenly",
      "That is angle-closure glaucoma."],
     ["Aqueous production by the ciliary body increases sharply",
      "The deck's mechanism is impaired outflow, not overproduction."],
     ["The canal of Schlemm is congenitally absent",
      "Not a mechanism the deck describes."]],
   c=0, cite=c(25)),

 dict(topic="Open-angle glaucoma", io=IO6, slot="manifestation", kfe=True,
   q="What does the deck call the clinical pitfall of primary open-angle glaucoma?",
   opts=[
     ["It is asymptomatic until severe peripheral vision loss, or tunnel vision, has occurred",
      "Correct — the silence of the disease is the pitfall the deck names."],
     ["It presents abruptly with severe pain and vomiting",
      "That is the angle-closure presentation."],
     ["It causes sudden painless monocular blindness",
      "That pattern belongs to vascular occlusion or detachment."],
     ["It causes loss of central vision first",
      "Peripheral loss comes first; central vision is preserved until late."]],
   c=0, cite=c(25)),

 dict(topic="Angle-closure glaucoma", io=IO6, slot="etiology", kfe=True,
   q="What is the mechanism of primary angle-closure glaucoma?",
   opts=[
     ["Pupil dilation displaces the iris forward against the cornea, closing the angle and blocking outflow completely",
      "Correct — mydriasis, iris bombé, then acute total blockage."],
     ["Microscopic trabecular resistance rises slowly over years",
      "That is the open-angle mechanism."],
     ["The retinal pigment epithelium fails to pump subretinal fluid",
      "That relates to retinal detachment."],
     ["Vascular endothelial growth factor drives new vessel formation",
      "That is proliferative diabetic retinopathy, and neovascular glaucoma is a separate entity."]],
   c=0, cite=c(25)),

 dict(topic="Angle-closure glaucoma", io=IO6, slot="test finding", kfe=True,
   q="How high does the pressure spike in acute angle-closure glaucoma?",
   opts=[
     ["Above 50 mmHg", "Correct — the deck's figure for the acute spike."],
     ["Above 25 mmHg", "Below the figure the deck gives for an acute closure."],
     ["Above 30 mmHg", "Below the deck's stated spike."],
     ["Above 80 mmHg", "Above the deck's stated figure."]],
   c=0, cite=c(25)),

 dict(topic="Angle-closure glaucoma", io=IO6, slot="manifestation", kfe=True,
   q="Which symptom set does the deck give for acute angle-closure glaucoma?",
   opts=[
     ["Severe eye pain, headache, halos around lights, cloudy cornea, a fixed mid-dilated pupil, and nausea and vomiting",
      "Correct — the deck's full acute picture."],
     ["Painless gradual bilateral blurring with glare at night",
      "That is cataract."],
     ["Flashing lights, a shower of floaters and a curtain falling across the vision",
      "That is retinal detachment."],
     ["Gradual central distortion with a scotoma",
      "That is macular degeneration."]],
   c=0, cite=c(25)),

 dict(topic="Angle-closure glaucoma", io=IO6, slot="etiology", kfe=True,
   q="What is iris bombé?",
   opts=[
     ["Forward displacement of the iris against the cornea",
      "Correct — the deck uses the term for the forward bowing that closes the angle."],
     ["Backward displacement of the iris against the lens",
      "The deck describes forward displacement."],
     ["Atrophy of the iris stroma after an acute attack",
      "Not the meaning the deck gives."],
     ["Adhesion of the iris to the corneal endothelium",
      "That describes a synechia rather than iris bombé."]],
   c=0, cite=c(25)),

 # ---- retinal detachment ----
 dict(topic="Retinal detachment", io=IO8, slot="etiology", kfe=True,
   q="What is the mechanism of a rhegmatogenous retinal detachment?",
   opts=[
     ["A full-thickness retinal tear lets liquefied vitreous into the subretinal space, peeling the retina off the pigment epithelium",
      "Correct — a break, then fluid tracking through it."],
     ["Fibrovascular membranes grow on the retinal surface and pull the retina off",
      "That is tractional detachment."],
     ["Fluid accumulates beneath the retina without any tear or traction",
      "That is exudative detachment."],
     ["Raised intraocular pressure compresses the retina against the choroid",
      "Pressure does not detach the retina in the deck's account."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="etiology", kfe=True,
   q="What is the mechanism of a tractional retinal detachment?",
   opts=[
     ["Proliferative fibrovascular membranes on the retinal surface physically pull the retina off the pigment epithelium",
      "Correct — scar tissue exerting mechanical traction."],
     ["A full-thickness tear admits liquefied vitreous beneath the retina",
      "That is rhegmatogenous."],
     ["Breakdown of the blood-retinal barrier lets fluid collect beneath the retina",
      "That is exudative."],
     ["The vitreous liquefies and collapses without any membrane forming",
      "Posterior vitreous detachment is a risk factor, not the tractional mechanism."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="etiology", kfe=True,
   q="What is the mechanism of an exudative retinal detachment?",
   opts=[
     ["Subretinal fluid accumulates without any tear or traction, from a breakdown of the blood-retinal barrier",
      "Correct — the deck's defining feature is the absence of both a break and traction."],
     ["A full-thickness tear admits vitreous fluid beneath the retina",
      "That is rhegmatogenous."],
     ["Fibrovascular scar tissue pulls the retina forward",
      "That is tractional."],
     ["The pigment epithelium proliferates and lifts the retina",
      "Not a mechanism the deck gives."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="differential", kfe=True,
   q="Which primary aetiology does the deck give for TRACTIONAL retinal detachment?",
   opts=[
     ["Proliferative diabetic retinopathy",
      "Correct — the neovascular membranes of proliferative disease are the classic traction source."],
     ["Severe malignant hypertension",
      "That appears under exudative detachment."],
     ["Posterior vitreous detachment",
      "That is a rhegmatogenous risk factor."],
     ["Choroidal melanoma",
      "That is an exudative cause."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="differential", kfe=True,
   q="Which three aetiologies does the deck give for EXUDATIVE detachment?",
   opts=[
     ["Severe malignant hypertension, sarcoidosis and choroidal melanoma",
      "Correct — hydrostatic, inflammatory and neoplastic causes respectively."],
     ["Posterior vitreous detachment, severe myopia and lattice degeneration",
      "Those are rhegmatogenous risk factors."],
     ["Proliferative diabetic retinopathy and prior vitrectomy scarring",
      "Those are tractional causes."],
     ["Cataract surgery, corticosteroids and ultraviolet exposure",
      "Those are cataract risks, not detachment causes."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="risk factors", kfe=True,
   q="Which risk factors does the deck list for rhegmatogenous detachment?",
   opts=[
     ["Posterior vitreous detachment, age, severe myopia, trauma and lattice degeneration",
      "Correct — the deck's five."],
     ["Diabetes, prior vitrectomy and retinal trauma surgery",
      "Those are tractional associations."],
     ["Sarcoidosis, malignant hypertension and melanoma",
      "Those are exudative causes."],
     ["Corticosteroid use, Down syndrome and ultraviolet exposure",
      "Those are cataract risks."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="manifestation", kfe=True,
   q="What symptoms does the deck give for rhegmatogenous detachment?",
   opts=[
     ["Flashing lights, a shower of floaters, and a curtain falling across the field",
      "Correct — photopsia, floaters, then the curtain."],
     ["Gradual painless bilateral blurring with glare at night",
      "That is cataract."],
     ["Severe pain with halos and a fixed mid-dilated pupil",
      "That is acute angle-closure glaucoma."],
     ["Slow loss of central detail with distortion of straight lines",
      "That is macular degeneration."]],
   c=0, cite=c(36)),

 dict(topic="Vitreous ageing", io=IO8, slot="etiology", kfe=True,
   q="What happens to the vitreous with age, and why does it matter for detachment?",
   opts=[
     ["It liquefies, so fluid can track through any retinal break into the subretinal space",
      "Correct — Webster's jelly-in-the-fridge analogy, and the reason liquefaction is upstream of detachment."],
     ["It solidifies, pressing the retina more firmly against the pigment epithelium",
      "The change is towards liquefaction, not solidification."],
     ["It becomes vascularised, bleeding into the subretinal space",
      "The vitreous stays avascular."],
     ["It thickens and opacifies, blocking light before it reaches the retina",
      "That is not the age change the deck or lecture describes."]],
   c=0, cite=au()),

 # ---- macular degeneration ----
 dict(topic="Dry macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What is the hallmark of dry, atrophic macular degeneration?",
   opts=[
     ["Drusen — discrete yellow extracellular debris beneath the pigment epithelium and Bruch membrane",
      "Correct — the deck's hallmark, with its composition and location."],
     ["Choroidal neovascularisation breaching into the subretinal space",
      "That is the wet form."],
     ["Neovascularisation on the optic disc",
      "That is proliferative diabetic retinopathy."],
     ["Cotton-wool spots in the nerve fibre layer",
      "Those are an ischaemic finding in retinopathy."]],
   c=0, cite=c(39)),

 dict(topic="Dry macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What are drusen composed of?",
   opts=[
     ["Lipofuscin and apolipoproteins", "Correct — the deck's stated composition."],
     ["Fibrin and platelet aggregates", "Not what the deck describes."],
     ["Calcium and phosphate crystals", "Not the deck's composition."],
     ["Cholesterol esters, as in xanthelasma", "That is the lid lesion, with a different composition."]],
   c=0, cite=c(39)),

 dict(topic="Dry macular degeneration", io=IO9, slot="manifestation", kfe=True,
   q="How does dry macular degeneration affect vision?",
   opts=[
     ["Slow gradual loss of central detail, with distortion and a scotoma",
      "Correct — metamorphopsia and scotoma, developing slowly."],
     ["Rapid central vision loss over days",
      "That is the wet form."],
     ["Loss of peripheral vision first, sparing the centre",
      "That pattern belongs to open-angle glaucoma."],
     ["Sudden painless monocular blindness",
      "That suggests vascular occlusion or optic nerve pathology."]],
   c=0, cite=c(39)),

 dict(topic="Wet macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What is the mechanism of wet, neovascular macular degeneration?",
   opts=[
     ["Hypoxia and inflammation trigger choroidal neovascularisation, and new vessels breach beneath the pigment epithelium into the subretinal space",
      "Correct — the deck's mechanism, from trigger through to breach."],
     ["Extracellular debris accumulates beneath the pigment epithelium",
      "That is the dry form's drusen."],
     ["Fibrovascular membranes on the retinal surface exert traction",
      "That is tractional retinal detachment."],
     ["Ganglion cell axons undergo apoptosis from raised pressure",
      "That is glaucoma."]],
   c=0, cite=c(40)),

 dict(topic="Wet macular degeneration", io=IO9, slot="prognosis", kfe=True,
   q="What proportion of severe blindness from macular degeneration does the wet form account for?",
   opts=[
     ["About ninety per cent", "Correct — the deck's figure, despite the dry form being commoner."],
     ["About fifty per cent", "Below the deck's figure."],
     ["About twenty-five per cent", "Well below the deck's figure."],
     ["About ten per cent", "That inverts the deck's figure."]],
   c=0, cite=c(40)),

 dict(topic="Wet macular degeneration", io=IO9, slot="complication", kfe=True,
   q="What complications follow from leaking neovascular vessels in wet macular degeneration?",
   opts=[
     ["Rapid central vision loss, disciform scarring and retinal detachment",
      "Correct — the deck's complication list."],
     ["Progressive optic disc cupping and tunnel vision",
      "That is glaucomatous damage."],
     ["Lens opacification and loss of the red reflex",
      "That is cataract."],
     ["Corneal stromal melting and perforation",
      "That is keratitis."]],
   c=0, cite=c(40)),

 dict(topic="Macular degeneration", io=IO9, slot="epidemiology", kfe=True,
   q="Macular degeneration is the leading cause of new-onset blindness in which group?",
   opts=[
     ["Adults over seventy-five in the United States",
      "Correct — the deck's stated epidemiology."],
     ["Adults aged twenty to seventy-four in the United States",
      "That is the deck's group for diabetic retinopathy."],
     ["Children and adolescents",
      "Not a group the deck discusses for this condition."],
     ["Adults of any age worldwide",
      "The deck's claim is specific to an age band and country."]],
   c=0, cite=c(39)),

 dict(topic="Macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What does the deck say about the pathogenesis of macular degeneration overall?",
   opts=[
     ["It is unknown", "Correct — the deck's slide titles say pathogenesis unknown for both forms."],
     ["It is entirely genetic", "The deck does not make this claim."],
     ["It is entirely driven by ultraviolet exposure", "The deck does not attribute it to a single cause."],
     ["It is a consequence of raised intraocular pressure", "That mechanism belongs to glaucoma."]],
   c=0, cite=c(39)),

 # ---- diabetic retinopathy ----
 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="What is the initiating microvascular mechanism in diabetic retinopathy?",
   opts=[
     ["Chronic hyperglycaemia damages capillaries and endothelial basement membranes, causing capillary occlusion and loss of oxygenation",
      "Correct — the deck's cascade begins with hyperglycaemic microvascular damage."],
     ["Raised intraocular pressure compresses the retinal vessels",
      "Pressure is not the mechanism in retinopathy."],
     ["Choroidal neovascularisation breaches Bruch membrane",
      "That is wet macular degeneration."],
     ["Liquefied vitreous tracks through a retinal tear",
      "That is rhegmatogenous detachment."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="test finding",
   q="Which findings characterise NON-proliferative diabetic retinopathy?",
   opts=[
     ["Dilated veins, microaneurysms, dot and blot haemorrhages, hard exudates, cotton-wool spots and macular oedema",
      "Correct — the deck's non-proliferative list."],
     ["Neovascularisation on the optic disc and retina",
      "New vessels define the proliferative stage."],
     ["Drusen beneath the pigment epithelium",
      "Those belong to macular degeneration."],
     ["Optic disc cupping above 0.5",
      "That is glaucomatous."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="What drives the change from non-proliferative to proliferative diabetic retinopathy?",
   opts=[
     ["Severe ischaemia upregulates vascular endothelial growth factor, producing neovascularisation",
      "Correct — ischaemia to growth factor to new vessels is the deck's step."],
     ["Rising intraocular pressure forces new vessels to form",
      "Pressure is not the driver in the deck."],
     ["Accumulation of lipofuscin beneath the pigment epithelium",
      "That is drusen formation in macular degeneration."],
     ["Bacterial collagenase digestion of the retinal surface",
      "That mechanism belongs to corneal ulceration."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="Where do hard exudates and cotton-wool spots sit, and what does each represent?",
   opts=[
     ["Hard exudates are lipid in the outer plexiform layer; cotton-wool spots are nerve fibre layer ischaemia or infarction",
      "Correct — the deck gives the layer and the pathology for each."],
     ["Hard exudates are nerve fibre layer infarcts; cotton-wool spots are lipid deposits",
      "This reverses the two."],
     ["Both are lipid deposits, differing only in size",
      "They are different processes in different layers."],
     ["Both are microinfarcts, differing only in age",
      "Only the cotton-wool spots are ischaemic."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="complication",
   q="Which complications does the deck attach to proliferative diabetic retinopathy?",
   opts=[
     ["Vitreous haemorrhage, fibrotic traction and tractional detachment",
      "Correct — the fragile new vessels bleed and then scar."],
     ["Scleral melting and globe perforation",
      "Those are scleritis and keratitis complications."],
     ["Lens opacification and loss of the red reflex",
      "That is cataract."],
     ["Optic disc cupping and peripheral field loss",
      "That is glaucoma."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="epidemiology",
   q="Diabetic retinopathy is the leading cause of new-onset blindness in which group?",
   opts=[
     ["United States adults aged twenty to seventy-four",
      "Correct — the deck's stated age band."],
     ["United States adults over seventy-five",
      "That is the group for macular degeneration."],
     ["Children under sixteen worldwide",
      "Not the deck's group."],
     ["Adults over fifty worldwide",
      "The deck's figure is specific to a narrower band and country."]],
   c=0, cite=c(37)),

 # ---- visual pathway and fields ----
 dict(topic="Visual pathway", io=IO10, slot="etiology", kfe=True,
   q="Which retinal fibres cross at the optic chiasm?",
   opts=[
     ["The nasal retinal fibres, which carry the temporal visual fields",
      "Correct — nasal fibres decussate; temporal fibres stay ipsilateral."],
     ["The temporal retinal fibres, which carry the nasal visual fields",
      "Temporal retinal fibres remain on the same side."],
     ["All fibres from both eyes",
      "Only the nasal fibres cross."],
     ["No fibres cross; each eye projects entirely ipsilaterally",
      "The chiasm exists precisely because some fibres cross."]],
   c=0, cite=c(32)),

 dict(topic="Visual pathway", io=IO10, slot="etiology", kfe=True,
   q="Trace the route from the ganglion cell axons to the visual cortex.",
   opts=[
     ["Optic disc, optic nerve, chiasm, optic tract, lateral geniculate nucleus, optic radiation, occipital cortex",
      "Correct — the deck's full pathway. Webster said to memorise nerve, chiasm, tract."],
     ["Optic disc, optic tract, chiasm, optic nerve, optic radiation, occipital cortex",
      "The nerve, chiasm and tract are in the wrong order."],
     ["Optic nerve, superior colliculus, thalamus, temporal cortex",
      "The relay is the lateral geniculate nucleus and the destination is occipital."],
     ["Optic nerve, chiasm, optic radiation, lateral geniculate nucleus, occipital cortex",
      "The geniculate comes before the radiation, not after."]],
   c=0, cite=c(33)),

 dict(topic="Visual field defects", io=IO10, slot="test finding", kfe=True,
   q="A lesion of one optic nerve produces which visual field defect?",
   opts=[
     ["Monocular blindness — total vision loss in that eye",
      "Correct — site A. The lesion is before any fibres have crossed."],
     ["Bitemporal hemianopsia",
      "That is a chiasmal lesion, site B."],
     ["Contralateral homonymous hemianopsia",
      "That is an optic tract lesion, site C."],
     ["Contralateral superior quadrantanopsia",
      "That is a temporal optic radiation lesion, site D."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="test finding", kfe=True,
   q="A lesion at the centre of the optic chiasm produces which defect, and what is the commonest cause?",
   opts=[
     ["Bitemporal hemianopsia, most commonly from a pituitary adenoma",
      "Correct — site B, and Webster named the adenoma as the commonest cause."],
     ["Monocular blindness, most commonly from optic neuritis",
      "That is site A."],
     ["Contralateral homonymous hemianopsia, most commonly from stroke",
      "That is site C."],
     ["Contralateral homonymous hemianopsia with macular sparing",
      "That is site E, the occipital cortex."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="etiology", kfe=True,
   q="Why does a central chiasmal lesion spare nasal vision in both eyes?",
   opts=[
     ["Only the crossing nasal retinal fibres are interrupted, and those carry the temporal fields; the temporal retinal fibres travel ipsilaterally and are untouched",
      "Correct — the anatomy of the decussation explains which half is lost."],
     ["The lesion damages the temporal retinal fibres, which carry nasal vision",
      "Those fibres do not cross and are not caught by a central lesion."],
     ["The macula is spared by a dual blood supply",
      "Macular sparing belongs to occipital lesions."],
     ["The lesion affects only one eye at a time",
      "A chiasmal lesion affects both eyes."]],
   c=0, cite=c(32)),

 dict(topic="Visual field defects", io=IO10, slot="test finding", kfe=True,
   q="A lesion of the optic tract produces which defect?",
   opts=[
     ["Contralateral homonymous hemianopsia",
      "Correct — site C. Past the chiasm, each tract carries the same side of both eyes' fields."],
     ["Bitemporal hemianopsia",
      "That is the chiasmal defect."],
     ["Monocular blindness",
      "That requires a lesion before the chiasm."],
     ["Central scotoma with preserved peripheral vision",
      "That pattern is macular rather than pathway-related."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="differential", kfe=True,
   q="Which three lesion sites did Webster say to know best?",
   opts=[
     ["Optic nerve, optic chiasm and optic tract",
      "Correct — he said it twice, and deferred the optic radiation and occipital cortex to neurology."],
     ["Optic radiation, lateral geniculate nucleus and occipital cortex",
      "Those are the two he explicitly said not to worry about."],
     ["Retina, optic disc and optic nerve",
      "The retina and disc are not the three he named."],
     ["Optic chiasm, optic radiation and occipital cortex",
      "Only the chiasm belongs to his priority set."]],
   c=0, cite=au()),

 dict(topic="Visual field defects", io=IO10, slot="differential",
   q="A temporal lobe lesion affecting part of the optic radiation produces which defect?",
   opts=[
     ["Contralateral superior quadrantanopsia, or pie in the sky",
      "Correct — site D. Webster deferred this one to neurology, but the deck names it."],
     ["Contralateral inferior quadrantanopsia",
      "The temporal radiation carries the superior field."],
     ["Bitemporal hemianopsia",
      "That is a chiasmal lesion."],
     ["Monocular blindness",
      "That requires a prechiasmal lesion."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="differential",
   q="An occipital cortex lesion from posterior cerebral artery occlusion produces which defect, and what is characteristically preserved?",
   opts=[
     ["Contralateral homonymous hemianopsia with macular sparing, because of the dual blood supply to the macular representation",
      "Correct — site E. Webster deferred this to neurology, but the deck gives the mechanism."],
     ["Contralateral homonymous hemianopsia with no sparing at all",
      "The deck specifically notes macular sparing."],
     ["Bitemporal hemianopsia with central sparing",
      "That is a chiasmal pattern."],
     ["Monocular blindness with a preserved pupillary reflex",
      "That is not the occipital pattern."]],
   c=0, cite=c(34)),

 dict(topic="Binocular vision", io=IO10, slot="complication",
   q="What does a patient lose when vision is lost in one eye, and why?",
   opts=[
     ["Depth perception, because the overlapping binocular field is what produces three-dimensional vision",
      "Correct — Webster made this point directly: everything becomes flat."],
     ["Colour discrimination, because cones are unevenly distributed",
      "Colour vision does not depend on having two eyes."],
     ["Peripheral vision on both sides, because the fields overlap entirely",
      "The fields overlap only centrally."],
     ["Night vision, because rods are concentrated in one eye",
      "Rods are in both retinas."]],
   c=0, cite=au()),

 dict(topic="Optic neuropathy", io=IO10, slot="differential", kfe=True,
   q="Which causes does the deck give for an ipsilateral optic nerve lesion?",
   opts=[
     ["Trauma, optic neuritis and ischaemic optic neuropathy",
      "Correct — the deck's three causes at site A."],
     ["Pituitary adenoma compression",
      "That is the chiasmal cause."],
     ["Posterior cerebral artery occlusion",
      "That is the occipital cause."],
     ["Temporal lobe surgery",
      "That affects the optic radiation."]],
   c=0, cite=c(34)),
]
