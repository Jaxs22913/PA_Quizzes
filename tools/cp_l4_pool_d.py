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
      "Correct — pressure is transmitted to the lamina cribrosa where axons leave the eye, interrupting axoplasmic transport and starving ganglion cells of trophic support, so they die and the disc excavates."],
     ["Raised pressure opacifies the crystalline lens",
      "That is cataract, which pressure does not cause."],
     ["Raised pressure detaches the neurosensory retina from the pigment epithelium",
      "That is retinal detachment, with different mechanisms."],
     ["Raised pressure causes neovascular growth on the optic disc",
      "That is proliferative diabetic retinopathy."]],
   c=0, cite=c(25)),

 dict(topic="Glaucoma mechanism", io=IO6, slot="test finding", kfe=True,
   q="Above what cup-to-disc ratio is optic disc cupping progressive?",
   opts=[
     ["Greater than 0.5", "Correct — raised pressure compresses retinal ganglion cell axons, the cells die by apoptosis, and the cup widens to a cup-to-disc ratio above 0.5."],
     ["Greater than 0.2", "A ratio of 0.2 sits below the threshold; progressive glaucomatous cupping is defined by a cup-to-disc ratio greater than 0.5."],
     ["Greater than 0.8", "A ratio of 0.8 is well past the threshold rather than the threshold itself; cupping counts as increased once the ratio exceeds 0.5."],
     ["Greater than 1.0", "A ratio above 1.0 is not the threshold; progressive glaucomatous cupping is an increased cup-to-disc ratio greater than 0.5."]],
   c=0, cite=c(25)),

 dict(topic="Open-angle glaucoma", io=IO6, slot="etiology", kfe=True,
   q="What is the mechanism of primary open-angle glaucoma?",
   opts=[
     ["The iridocorneal angle stays open but microscopic resistance in the trabecular meshwork impairs outflow, raising pressure gradually",
      "Correct — the angle is open; the obstruction is microscopic and downstream."],
     ["The iridocorneal angle narrows anatomically and blocks outflow suddenly",
      "Anatomical narrowing that suddenly blocks outflow is angle-closure glaucoma; in open-angle disease the angle stays open and the resistance is microscopic."],
     ["Aqueous production by the ciliary body increases sharply",
      "Aqueous production is normal; the fault lies in outflow resistance at the trabecular meshwork, which is why the pressure rises so gradually."],
     ["The canal of Schlemm is congenitally absent",
      "The canal of Schlemm is present; the resistance is microscopic, within the trabecular meshwork draining into it."]],
   c=0, cite=c(25)),

 dict(topic="Open-angle glaucoma", io=IO6, slot="manifestation", kfe=True,
   q="What is called the clinical pitfall of primary open-angle glaucoma?",
   opts=[
     ["It is asymptomatic until severe peripheral vision loss, or tunnel vision, has occurred",
      "Correct — peripheral ganglion cells are lost first and the intact fellow eye fills in the missing field, so half the nerve can be gone before the patient notices anything."],
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
     ["Above 50 mmHg", "Correct — with outflow abruptly blocked and production continuing, pressure exceeds 50 mmHg, which is high enough to oedematise the cornea and compromise the optic nerve within hours."],
     ["Above 25 mmHg", "25 mmHg is a chronically raised pressure rather than an acute closure; sudden angle closure drives it above 50."],
     ["Above 30 mmHg", "30 mmHg is well short of an acute attack, in which pressure exceeds 50 mmHg."],
     ["Above 80 mmHg", "80 mmHg overstates it; the acute spike is above 50 mmHg."]],
   c=0, cite=c(25)),

 dict(topic="Angle-closure glaucoma", io=IO6, slot="manifestation", kfe=True,
   q="What is the symptom set of acute angle-closure glaucoma?",
   opts=[
     ["Severe eye pain, headache, halos around lights, cloudy cornea, a fixed mid-dilated pupil, and nausea and vomiting",
      "Correct — iris bombé blocks aqueous outflow totally, and the rapid pressure spike above 50 mmHg produces pain, headache, halos, a cloudy cornea, a fixed mid-dilated pupil and vomiting."],
     ["Painless gradual bilateral blurring with glare at night",
      "Painless gradual blurring with night glare is cataract; acute angle closure is a sudden, painful pressure spike with halos and a fixed mid-dilated pupil."],
     ["Flashing lights, a shower of floaters and a curtain falling across the vision",
      "Photopsia, a shower of floaters and a falling curtain describe rhegmatogenous retinal detachment; angle closure brings severe pain, halos and vomiting."],
     ["Gradual central distortion with a scotoma",
      "Gradual central distortion with a scotoma is dry macular degeneration; acute angle closure is sudden, with severe pain, halos and a fixed mid-dilated pupil."]],
   c=0, cite=c(25)),

 dict(topic="Angle-closure glaucoma", io=IO6, slot="etiology", kfe=True,
   q="What is iris bombé?",
   opts=[
     ["Forward displacement of the iris against the cornea",
      "Correct — in angle closure, pupil dilation pushes the iris forward against the cornea, and this iris bombé blocks aqueous outflow totally so pressure spikes."],
     ["Backward displacement of the iris against the lens",
      "The displacement is forward, not backward; in iris bombé the iris is pushed against the cornea, closing the iridocorneal angle."],
     ["Atrophy of the iris stroma after an acute attack",
      "Iris bombé is not atrophy; it is forward displacement of the iris against the cornea, which triggers the acute outflow blockage of angle closure."],
     ["Adhesion of the iris to the corneal endothelium",
      "Adhesion is not the meaning; iris bombé is forward displacement of the iris against the cornea, closing the angle when the pupil dilates."]],
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
      "Raised pressure damages the optic nerve head rather than separating retina from pigment epithelium; detachment needs a break, traction or subretinal fluid."]],
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
      "Correct — inflammation, tumor or severe hypertension breaks down the blood-retinal barrier, so fluid leaks into the subretinal space without any break or pulling force."],
     ["A full-thickness tear admits vitreous fluid beneath the retina",
      "That is rhegmatogenous."],
     ["Fibrovascular scar tissue pulls the retina forward",
      "That is tractional."],
     ["The pigment epithelium proliferates and lifts the retina",
      "The pigment epithelium does not proliferate to lift the retina; exudative detachment is fluid leaking through a broken blood-retinal barrier."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="differential", kfe=True,
   q="What is the primary etiology of TRACTIONAL retinal detachment?",
   opts=[
     ["Proliferative diabetic retinopathy",
      "Correct — the neovascular membranes of proliferative disease are the classic traction source."],
     ["Severe malignant hypertension",
      "Malignant hypertension is an exudative cause, breaking down the blood-retinal barrier; traction comes from the membranes of proliferative diabetic retinopathy."],
     ["Posterior vitreous detachment",
      "Posterior vitreous detachment is a risk factor for rhegmatogenous detachment through a retinal break; traction arises from proliferative diabetic retinopathy."],
     ["Choroidal melanoma",
      "Choroidal melanoma causes exudative detachment, with fluid collecting without a tear; tractional detachment follows proliferative diabetic retinopathy."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="differential", kfe=True,
   q="Which three etiologies are given for EXUDATIVE detachment?",
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
   q="What are the risk factors for rhegmatogenous detachment?",
   opts=[
     ["Posterior vitreous detachment, age, severe myopia, trauma and lattice degeneration",
      "Correct — posterior vitreous detachment, age, severe myopia, trauma and lattice degeneration set up the full-thickness break through which liquefied vitreous enters."],
     ["Diabetes, prior vitrectomy and retinal trauma surgery",
      "Diabetes and prior vitrectomy scarring cause tractional detachment through fibrovascular membranes; rhegmatogenous detachment starts with a retinal break."],
     ["Sarcoidosis, malignant hypertension and melanoma",
      "Sarcoidosis, malignant hypertension and melanoma cause exudative detachment without a tear; rhegmatogenous detachment follows a full-thickness break."],
     ["Corticosteroid use, Down syndrome and ultraviolet exposure",
      "Corticosteroids, Down syndrome and ultraviolet light are cataract risks; rhegmatogenous risks are vitreous detachment, age, myopia, trauma and lattice degeneration."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="manifestation", kfe=True,
   q="What are the symptoms of rhegmatogenous detachment?",
   opts=[
     ["Flashing lights, a shower of floaters, and a curtain falling across the field",
      "Correct — the symptoms of a full-thickness retinal break with detachment are flashing lights (photopsia), a shower of floaters and a curtain falling across the field."],
     ["Gradual painless bilateral blurring with glare at night",
      "Gradual painless bilateral blurring with night glare is cataract; rhegmatogenous detachment brings photopsia, a shower of floaters and a curtain."],
     ["Severe pain with halos and a fixed mid-dilated pupil",
      "Severe pain, halos and a fixed mid-dilated pupil describe acute angle-closure glaucoma; rhegmatogenous detachment brings photopsia, floaters and a curtain."],
     ["Slow loss of central detail with distortion of straight lines",
      "Slow loss of central detail with distortion is dry macular degeneration; rhegmatogenous detachment brings flashing lights, floaters and a curtain."]],
   c=0, cite=c(36)),

 dict(topic="Vitreous aging", io=IO8, slot="etiology", kfe=True,
   q="Which change in the vitreous underlies rhegmatogenous retinal detachment?",
   opts=[
     ["It liquefies, so fluid can track through any retinal break into the subretinal space",
      "Correct — once liquefied, vitreous fluid can pass through a full-thickness retinal tear into the subretinal space and peel the neurosensory retina off the pigment epithelium."],
     ["It solidifies, pressing the retina more firmly against the pigment epithelium",
      "Solidification is not the change; in rhegmatogenous detachment liquefied vitreous fluid passes through a full-thickness tear into the subretinal space."],
     ["It becomes vascularized, bleeding into the subretinal space",
      "Vascularization is not the change; the vitreous is a transparent gel, and in rhegmatogenous detachment liquefied vitreous passes through a retinal break beneath the retina."],
     ["It thickens and opacifies, blocking light before it reaches the retina",
      "Thickening is the wrong direction; liquefied vitreous fluid enters the subretinal space through a full-thickness tear, peeling the retina off the pigment epithelium."]],
   c=0, cite=c(36)),

 # ---- macular degeneration ----
 dict(topic="Dry macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What is the hallmark of dry, atrophic macular degeneration?",
   opts=[
     ["Drusen — discrete yellow extracellular debris beneath the pigment epithelium and Bruch membrane",
      "Correct — drusen are discrete yellow extracellular deposits of lipofuscin and apolipoproteins beneath the pigment epithelium and Bruch membrane, the hallmark of the dry form."],
     ["Choroidal neovascularization breaching into the subretinal space",
      "Choroidal neovascularization breaching into the subretinal space is the wet form; the dry form's hallmark is drusen beneath the pigment epithelium."],
     ["Neovascularization on the optic disc",
      "New vessels on the optic disc belong to proliferative diabetic retinopathy; dry macular degeneration's hallmark is drusen beneath the pigment epithelium."],
     ["Cotton-wool spots in the nerve fiber layer",
      "Cotton-wool spots mark nerve fiber layer ischemia in diabetic retinopathy; the hallmark of dry macular degeneration is drusen."]],
   c=0, cite=c(39)),

 dict(topic="Dry macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What are drusen composed of?",
   opts=[
     ["Lipofuscin and apolipoproteins", "Correct — drusen, the hallmark of dry macular degeneration, are discrete yellow extracellular deposits of lipofuscin and apolipoproteins beneath the pigment epithelium."],
     ["Fibrin and platelet aggregates", "Fibrin and platelets are not drusen; drusen are yellow extracellular deposits of lipofuscin and apolipoproteins beneath the pigment epithelium."],
     ["Calcium and phosphate crystals", "Calcium phosphate crystals are not the composition; drusen are extracellular lipofuscin and apolipoprotein debris beneath the pigment epithelium and Bruch membrane."],
     ["Cholesterol esters, as in xanthelasma", "Cholesterol-filled lesions are xanthelasma on the lids; drusen are lipofuscin and apolipoprotein debris beneath the retinal pigment epithelium."]],
   c=0, cite=c(39)),

 dict(topic="Dry macular degeneration", io=IO9, slot="manifestation", kfe=True,
   q="How does dry macular degeneration affect vision?",
   opts=[
     ["Slow gradual loss of central detail, with distortion and a scotoma",
      "Correct — slow degeneration of photoreceptors, pigment epithelium and choroid causes gradual loss of central detail, with metamorphopsia and scotoma."],
     ["Rapid central vision loss over days",
      "Rapid central loss belongs to the wet form, from leaking new vessels; the dry form causes slow, gradual loss of central detail."],
     ["Loss of peripheral vision first, sparing the center",
      "Peripheral loss first with central sparing is the tunnel vision of open-angle glaucoma; dry macular degeneration takes central detail slowly."],
     ["Sudden painless monocular blindness",
      "Sudden painless monocular blindness is not the pattern; dry macular degeneration causes slow, gradual loss of central detail with distortion."]],
   c=0, cite=c(39)),

 dict(topic="Wet macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What is the mechanism of wet, neovascular macular degeneration?",
   opts=[
     ["Hypoxia and inflammation trigger choroidal neovascularization, and new vessels breach beneath the pigment epithelium into the subretinal space",
      "Correct — hypoxia and inflammation trigger choroidal neovascularization, and the new vessels breach beneath the pigment epithelium into the subretinal space, where they leak blood and serous fluid."],
     ["Extracellular debris accumulates beneath the pigment epithelium",
      "Lipofuscin debris beneath the pigment epithelium forms drusen, the hallmark of dry macular degeneration, not the neovascular wet form."],
     ["Fibrovascular membranes on the retinal surface exert traction",
      "Fibrovascular membranes pulling on the retinal surface cause tractional retinal detachment; wet degeneration is choroidal neovascularization breaching into the subretinal space."],
     ["Ganglion cell axons undergo apoptosis from raised pressure",
      "Ganglion cell apoptosis from raised pressure is glaucoma; wet macular degeneration is driven by hypoxia and inflammation triggering choroidal neovascularization."]],
   c=0, cite=c(40)),

 dict(topic="Wet macular degeneration", io=IO9, slot="prognosis", kfe=True,
   q="What proportion of severe blindness from macular degeneration does the wet form account for?",
   opts=[
     ["About ninety per cent", "Correct — the wet form progresses rapidly, because leaking new vessels cause rapid central vision loss, so it accounts for about ninety percent of severe blindness."],
     ["About fifty per cent", "Half understates it; the rapidly progressive wet form accounts for about ninety percent of severe blindness from macular degeneration."],
     ["About twenty-five per cent", "A quarter is far too low; the wet form accounts for about ninety percent of severe blindness, while the dry form progresses slowly."],
     ["About ten per cent", "Ten percent inverts the figure: the rapidly progressive wet form accounts for about ninety percent of severe blindness from macular degeneration."]],
   c=0, cite=c(40)),

 dict(topic="Wet macular degeneration", io=IO9, slot="complication", kfe=True,
   q="What complications follow from leaking neovascular vessels in wet macular degeneration?",
   opts=[
     ["Rapid central vision loss, disciform scarring and retinal detachment",
      "Correct — the new vessels lack tight junctions, so they leak fluid and blood under the macula; the organized hemorrhage becomes a fibrous disciform scar and the accumulating fluid can lift the retina."],
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
      "Correct — macular degeneration is the leading cause of new-onset blindness in United States adults over seventy-five, while diabetic retinopathy leads in younger adults."],
     ["Adults aged twenty to seventy-four in the United States",
      "That working-age band is dominated by diabetic retinopathy; macular degeneration leads in adults over seventy-five."],
     ["Children and adolescents",
      "Children are not the group; macular degeneration is the leading cause of new-onset blindness in United States adults over seventy-five."],
     ["Adults of any age worldwide",
      "The claim is specific to an age band and a country: macular degeneration leads new-onset blindness in United States adults over seventy-five."]],
   c=0, cite=c(39)),

 dict(topic="Macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What is known about the pathogenesis of macular degeneration overall?",
   opts=[
     ["It is unknown", "Correct — the pathogenesis of both dry and wet macular degeneration is unknown, even though drusen and choroidal neovascularization describe what happens in each."],
     ["It is entirely genetic", "No genetic cause is established; the pathogenesis of macular degeneration is unknown for both forms, described only by drusen or neovascularization."],
     ["It is entirely driven by ultraviolet exposure", "Ultraviolet light is a cataract risk, not an established cause of macular degeneration, whose pathogenesis remains unknown for both forms."],
     ["It is a consequence of raised intraocular pressure", "Raised intraocular pressure drives glaucoma by compressing ganglion cell axons; the pathogenesis of macular degeneration is unknown."]],
   c=0, cite=c(39)),

 # ---- diabetic retinopathy ----
 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="What is the initiating microvascular mechanism in diabetic retinopathy?",
   opts=[
     ["Chronic hyperglycemia damages capillaries and endothelial basement membranes, causing capillary occlusion and loss of oxygenation",
      "Correct — persistent hyperglycemia glycates basement membrane proteins and damages pericytes, so capillaries leak and then close, leaving the retina it supplied ischemic."],
     ["Raised intraocular pressure compresses the retinal vessels",
      "Pressure is not the mechanism in retinopathy."],
     ["Choroidal neovascularization breaches Bruch membrane",
      "That is wet macular degeneration."],
     ["Liquefied vitreous tracks through a retinal tear",
      "That is rhegmatogenous detachment."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="test finding",
   q="Which findings characterize NON-proliferative diabetic retinopathy?",
   opts=[
     ["Dilated veins, microaneurysms, dot and blot hemorrhages, hard exudates, cotton-wool spots and macular edema",
      "Correct — each reflects damaged but not yet neovascularized vessels: outpouchings, leakage of blood and lipid, and small infarcts, with fluid collecting at the macula."],
     ["Neovascularization on the optic disc and retina",
      "New vessels define the proliferative stage."],
     ["Drusen beneath the pigment epithelium",
      "Those belong to macular degeneration."],
     ["Optic disc cupping above 0.5",
      "That is glaucomatous."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="What drives the change from non-proliferative to proliferative diabetic retinopathy?",
   opts=[
     ["Severe ischemia upregulates vascular endothelial growth factor, producing neovascularization",
      "Correct — chronic hyperglycemia occludes capillaries, severe ischemia upregulates vascular endothelial growth factor, and fragile new vessels grow on the disc and retina."],
     ["Rising intraocular pressure forces new vessels to form",
      "Intraocular pressure is not the driver; severe ischemia upregulates vascular endothelial growth factor, which produces the fragile new vessels."],
     ["Accumulation of lipofuscin beneath the pigment epithelium",
      "Lipofuscin and apolipoprotein deposits are drusen in dry macular degeneration; proliferative change is driven by ischemia and vascular endothelial growth factor."],
     ["Bacterial collagenase digestion of the retinal surface",
      "Bacterial collagenases melt tissue in corneal ulceration; proliferative retinopathy arises when severe ischemia upregulates vascular endothelial growth factor."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="Where do hard exudates and cotton-wool spots sit, and what does each represent?",
   opts=[
     ["Hard exudates are lipid in the outer plexiform layer; cotton-wool spots are nerve fiber layer ischemia or infarction",
      "Correct — hard exudates are lipid left behind when leaked plasma is reabsorbed, collecting in the outer plexiform layer, while cotton-wool spots are swollen axons where nerve fiber layer capillaries have occluded."],
     ["Hard exudates are nerve fiber layer infarcts; cotton-wool spots are lipid deposits",
      "This reverses the two."],
     ["Both are lipid deposits, differing only in size",
      "They are different processes in different layers."],
     ["Both are microinfarcts, differing only in age",
      "Only the cotton-wool spots are ischemic."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="complication",
   q="Which complications are attached to proliferative diabetic retinopathy?",
   opts=[
     ["Vitreous hemorrhage, fibrotic traction and tractional detachment",
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
      "Correct — chronic hyperglycemia damages retinal capillaries, and diabetic retinopathy is the leading cause of new-onset blindness in United States adults aged twenty to seventy-four."],
     ["United States adults over seventy-five",
      "Adults over seventy-five belong to macular degeneration; diabetic retinopathy leads new-onset blindness in United States adults aged twenty to seventy-four."],
     ["Children under sixteen worldwide",
      "Children are not the group; diabetic retinopathy is the leading cause of new-onset blindness in United States adults aged twenty to seventy-four."],
     ["Adults over fifty worldwide",
      "The claim applies to United States adults aged twenty to seventy-four; over seventy-five, macular degeneration leads."]],
   c=0, cite=c(37)),

 # ---- visual pathway and fields ----
 dict(topic="Visual pathway", io=IO10, slot="etiology", kfe=True,
   q="Which retinal fibers cross at the optic chiasm?",
   opts=[
     ["The nasal retinal fibers, which carry the temporal visual fields",
      "Correct — nasal fibers decussate; temporal fibers stay ipsilateral."],
     ["The temporal retinal fibers, which carry the nasal visual fields",
      "Temporal retinal fibers remain on the same side."],
     ["All fibers from both eyes",
      "Only the nasal fibers cross."],
     ["No fibers cross; each eye projects entirely ipsilaterally",
      "The chiasm exists precisely because some fibers cross."]],
   c=0, cite=c(32)),

 dict(topic="Visual pathway", io=IO10, slot="etiology", kfe=True,
   q="Trace the route from the ganglion cell axons to the visual cortex.",
   opts=[
     ["Optic disc, optic nerve, chiasm, optic tract, lateral geniculate nucleus, optic radiation, occipital cortex",
      "Correct — axons leave at the disc, nasal fibers cross at the chiasm, the tract carries the combined contralateral field to the lateral geniculate nucleus, and the radiation fans out to the occipital cortex."],
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
      "Correct — site A. The lesion is before any fibers have crossed."],
     ["Bitemporal hemianopsia",
      "That is a chiasmal lesion, site B."],
     ["Contralateral homonymous hemianopsia",
      "That is an optic tract lesion, site C."],
     ["Contralateral superior quadrantanopsia",
      "That is a temporal optic radiation lesion, site D."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="test finding", kfe=True,
   q="A lesion at the center of the optic chiasm produces which defect, and what is the commonest cause?",
   opts=[
     ["Bitemporal hemianopsia, most commonly from a pituitary adenoma",
      "Correct — site B: pituitary adenoma compression at the center of the chiasm cuts the crossing nasal fibers, giving bitemporal hemianopsia."],
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
     ["Only the crossing nasal retinal fibers are interrupted, and those carry the temporal fields; the temporal retinal fibers travel ipsilaterally and are untouched",
      "Correct — only the nasal retinal fibers cross at the chiasm, and they carry the temporal fields; the temporal retinal fibers stay ipsilateral, so nasal vision survives."],
     ["The lesion damages the temporal retinal fibers, which carry nasal vision",
      "Temporal retinal fibers stay ipsilateral, so a central lesion misses them; it cuts the crossing nasal fibers, which carry the temporal fields."],
     ["The macula is spared by a dual blood supply",
      "Macular sparing from a dual blood supply belongs to occipital cortex lesions; a chiasmal lesion spares nasal vision because only crossing fibers are cut."],
     ["The lesion affects only one eye at a time",
      "A central chiasmal lesion affects both eyes, producing bitemporal hemianopsia, because the crossing nasal fibers from each eye are interrupted."]],
   c=0, cite=c(32)),

 dict(topic="Visual field defects", io=IO10, slot="test finding", kfe=True,
   q="A lesion of the optic tract produces which defect?",
   opts=[
     ["Contralateral homonymous hemianopsia",
      "Correct — an optic tract lesion, from stroke, tumor or demyelination, causes contralateral homonymous hemianopsia, the loss of the opposite visual field."],
     ["Bitemporal hemianopsia",
      "Bitemporal hemianopsia comes from a central chiasmal lesion such as pituitary adenoma; an optic tract lesion gives contralateral homonymous hemianopsia."],
     ["Monocular blindness",
      "Monocular blindness requires an optic nerve lesion before the chiasm; past it, an optic tract lesion gives contralateral homonymous hemianopsia."],
     ["Central scotoma with preserved peripheral vision",
      "A central scotoma is a macular picture, as in macular degeneration; a lesion of the optic tract causes contralateral homonymous hemianopsia."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="differential", kfe=True,
   q="Which three of the visual field lesion sites lie between the globe and the lateral geniculate nucleus?",
   opts=[
     ["Optic nerve, optic chiasm and optic tract",
      "Correct — the optic nerve, optic chiasm and optic tract carry the pathway from the optic disc to the lateral geniculate nucleus of the thalamus."],
     ["Optic radiation, lateral geniculate nucleus and occipital cortex",
      "The optic radiation and occipital cortex lie beyond the lateral geniculate nucleus; the sites before it are the optic nerve, chiasm and optic tract."],
     ["Retina, optic disc and optic nerve",
      "The retina and optic disc lie within the globe itself; between the globe and the lateral geniculate nucleus run the optic nerve, chiasm and optic tract."],
     ["Optic chiasm, optic radiation and occipital cortex",
      "Only the chiasm lies before the lateral geniculate nucleus; the optic radiation and occipital cortex come after it on the route to the visual cortex."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="differential",
   q="A temporal lobe lesion affecting part of the optic radiation produces which defect?",
   opts=[
     ["Contralateral superior quadrantanopsia, or pie in the sky",
      "Correct — a temporal lobe lesion, surgery or middle cerebral artery stroke at the temporal optic radiation causes contralateral superior quadrantanopsia, pie in the sky."],
     ["Contralateral inferior quadrantanopsia",
      "Inferior quadrantanopsia is not the temporal result; damage to the temporal optic radiation removes the contralateral superior quadrant, pie in the sky."],
     ["Bitemporal hemianopsia",
      "Bitemporal hemianopsia comes from a central chiasmal lesion such as pituitary adenoma, not from the temporal optic radiation."],
     ["Monocular blindness",
      "Monocular blindness needs an optic nerve lesion before the chiasm; a temporal lobe lesion of the optic radiation gives superior quadrantanopsia."]],
   c=0, cite=c(34)),

 dict(topic="Visual field defects", io=IO10, slot="differential",
   q="An occipital cortex lesion from posterior cerebral artery occlusion produces which defect, and what is characteristically preserved?",
   opts=[
     ["Contralateral homonymous hemianopsia with macular sparing, because of the dual blood supply to the macular representation",
      "Correct — the occipital pole representing the macula receives collateral supply from the middle cerebral artery, so it survives a posterior cerebral occlusion and central vision is spared."],
     ["Contralateral homonymous hemianopsia with no sparing at all",
      "The macular representation at the occipital pole has a dual blood supply, so it is characteristically spared in posterior cerebral artery occlusion."],
     ["Bitemporal hemianopsia with central sparing",
      "That is a chiasmal pattern."],
     ["Monocular blindness with a preserved pupillary reflex",
      "That is not the occipital pattern."]],
   c=0, cite=c(34)),

 dict(topic="Binocular vision", io=IO10, slot="complication",
   q="What does a patient lose when vision is lost in one eye, and why?",
   opts=[
     ["Depth perception, because the overlapping binocular field is what produces three-dimensional vision",
      "Correct — depth perception comes from the overlapping binocular field, so losing one eye leaves vision flat, without three-dimensional depth."],
     ["Color discrimination, because cones are unevenly distributed",
      "Color vision does not depend on having two eyes."],
     ["Peripheral vision on both sides, because the fields overlap entirely",
      "The fields overlap only centrally."],
     ["Night vision, because rods are concentrated in one eye",
      "Rods are in both retinas."]],
   c=0, cite=au()),

 dict(topic="Optic neuropathy", io=IO10, slot="differential", kfe=True,
   q="What causes an ipsilateral optic nerve lesion?",
   opts=[
     ["Trauma, optic neuritis and ischemic optic neuropathy",
      "Correct — a lesion of the optic nerve before the chiasm follows trauma, optic neuritis or ischemic optic neuropathy, and causes total vision loss in that eye."],
     ["Pituitary adenoma compression",
      "Pituitary adenoma compresses the center of the optic chiasm, causing bitemporal hemianopsia; optic nerve lesions follow trauma, neuritis or ischemia."],
     ["Posterior cerebral artery occlusion",
      "Posterior cerebral artery occlusion damages the occipital cortex, sparing the macula; optic nerve lesions follow trauma, optic neuritis or ischemia."],
     ["Temporal lobe surgery",
      "Temporal lobe surgery damages the temporal optic radiation, giving pie in the sky; optic nerve lesions follow trauma, optic neuritis or ischemic neuropathy."]],
   c=0, cite=c(34)),
]
