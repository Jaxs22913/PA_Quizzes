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
   q="Above what cup-to-disc ratio is progressive optic disc cupping described?",
   opts=[
     ["Greater than 0.5", "Correct — above 0.5 the cup occupies more than half the disc diameter, indicating that a substantial proportion of the neuroretinal rim has already been lost."],
     ["Greater than 0.2", "A ratio of 0.2 is within the normal range; concern begins above 0.5, where the rim has visibly thinned."],
     ["Greater than 0.8", "A ratio of 0.8 is advanced disease rather than the threshold; cupping is called increased above 0.5."],
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
   q="Which symptom set is given for acute angle-closure glaucoma?",
   opts=[
     ["Severe eye pain, headache, halos around lights, cloudy cornea, a fixed mid-dilated pupil, and nausea and vomiting",
      "Correct — the pressure oedematises the cornea to give halos and cloudiness, paralyses the iris sphincter to leave a fixed mid-dilated pupil, and stimulates the trigeminal and vagal reflexes to produce pain and vomiting."],
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
      "Correct — aqueous trapped behind the iris by pupillary block pushes the peripheral iris forward against the trabecular meshwork, sealing the angle it was meant to drain through."],
     ["Backward displacement of the iris against the lens",
      "The bowing is forward rather than backward; aqueous trapped behind the iris pushes it towards the cornea."],
     ["Atrophy of the iris stroma after an acute attack",
      "Iris atrophy can follow a prolonged attack, but iris bombé is the forward bowing that causes the attack in the first place."],
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
      "Correct — inflammation, tumour or severe hypertension breaks down the blood-retinal barrier, so fluid leaks into the subretinal space without any break or pulling force."],
     ["A full-thickness tear admits vitreous fluid beneath the retina",
      "That is rhegmatogenous."],
     ["Fibrovascular scar tissue pulls the retina forward",
      "That is tractional."],
     ["The pigment epithelium proliferates and lifts the retina",
      "The pigment epithelium does not proliferate to lift the retina; exudative detachment is fluid leaking through a broken blood-retinal barrier."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="differential", kfe=True,
   q="Which primary aetiology is given for TRACTIONAL retinal detachment?",
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
   q="Which three aetiologies are given for EXUDATIVE detachment?",
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
   q="Which risk factors are listed for rhegmatogenous detachment?",
   opts=[
     ["Posterior vitreous detachment, age, severe myopia, trauma and lattice degeneration",
      "Correct — each either liquefies the vitreous, stretches the retina thin, or weakens it focally, so a break forms and liquefied vitreous can pass through it."],
     ["Diabetes, prior vitrectomy and retinal trauma surgery",
      "Those are tractional associations."],
     ["Sarcoidosis, malignant hypertension and melanoma",
      "Those are exudative causes."],
     ["Corticosteroid use, Down syndrome and ultraviolet exposure",
      "Those are cataract risks."]],
   c=0, cite=c(36)),

 dict(topic="Retinal detachment", io=IO8, slot="manifestation", kfe=True,
   q="What symptoms are given for rhegmatogenous detachment?",
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
      "The vitreous liquefies rather than thickening, and the problem is not light transmission but fluid gaining access to the subretinal space."]],
   c=0, cite=au()),

 # ---- macular degeneration ----
 dict(topic="Dry macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What is the hallmark of dry, atrophic macular degeneration?",
   opts=[
     ["Drusen — discrete yellow extracellular debris beneath the pigment epithelium and Bruch membrane",
      "Correct — the pigment epithelium fails to clear the waste products of photoreceptor turnover, so debris accumulates beneath it and separates it from its choroidal blood supply."],
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
     ["Lipofuscin and apolipoproteins", "Correct — lipofuscin is the undigested residue of photoreceptor outer segments, and it accumulates with apolipoproteins as the pigment epithelium's clearance capacity fails."],
     ["Fibrin and platelet aggregates", "Fibrin and platelets form thrombus within vessels; drusen are extracellular waste of lipofuscin and apolipoproteins."],
     ["Calcium and phosphate crystals", "Drusen may calcify late, but their substance is lipofuscin and apolipoproteins from failed photoreceptor waste clearance."],
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
      "Correct — a pigment epithelium separated from its blood supply by drusen becomes hypoxic and releases vascular endothelial growth factor, and the fragile new vessels that result leak and bleed under the macula."],
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
     ["About ninety per cent", "Correct — the dry form is far commoner but progresses slowly, while the wet form destroys central vision quickly, so it causes about ninety per cent of the severe visual loss."],
     ["About fifty per cent", "Half understates it; the wet form causes around ninety per cent of severe visual loss despite being the less common type."],
     ["About twenty-five per cent", "A quarter is far too low; the wet form accounts for roughly ninety per cent of severe blindness from the disease."],
     ["About ten per cent", "This inverts the figures: the wet form is the less common type but causes about ninety per cent of the severe visual loss."]],
   c=0, cite=c(40)),

 dict(topic="Wet macular degeneration", io=IO9, slot="complication", kfe=True,
   q="What complications follow from leaking neovascular vessels in wet macular degeneration?",
   opts=[
     ["Rapid central vision loss, disciform scarring and retinal detachment",
      "Correct — the new vessels lack tight junctions, so they leak fluid and blood under the macula; the organised haemorrhage becomes a fibrous disciform scar and the accumulating fluid can lift the retina."],
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
      "Correct — the disease is degenerative and cumulative, so its incidence climbs steeply with age and dominates blindness in the oldest group."],
     ["Adults aged twenty to seventy-four in the United States",
      "That working-age band is dominated by diabetic retinopathy; macular degeneration leads in adults over seventy-five."],
     ["Children and adolescents",
      "Macular degeneration is a disease of ageing and does not occur in children; the juvenile maculopathies are separate genetic conditions."],
     ["Adults of any age worldwide",
      "The claim is specific to adults over seventy-five in the United States; worldwide, cataract and trachoma dominate blindness overall."]],
   c=0, cite=c(39)),

 dict(topic="Macular degeneration", io=IO9, slot="etiology", kfe=True,
   q="What is true of the pathogenesis of macular degeneration overall?",
   opts=[
     ["It is unknown", "Correct — both forms remain incompletely explained; ageing, genetic susceptibility, oxidative stress and inflammation all contribute without a single established cause."],
     ["It is entirely genetic", "Genetic susceptibility contributes but does not account for the disease alone; age, oxidative stress and inflammation also play a part."],
     ["It is entirely driven by ultraviolet exposure", "Ultraviolet exposure is one contributing factor among several rather than the whole explanation."],
     ["It is a consequence of raised intraocular pressure", "That mechanism belongs to glaucoma."]],
   c=0, cite=c(39)),

 # ---- diabetic retinopathy ----
 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="What is the initiating microvascular mechanism in diabetic retinopathy?",
   opts=[
     ["Chronic hyperglycaemia damages capillaries and endothelial basement membranes, causing capillary occlusion and loss of oxygenation",
      "Correct — persistent hyperglycaemia glycates basement membrane proteins and damages pericytes, so capillaries leak and then close, leaving the retina it supplied ischaemic."],
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
      "Correct — each reflects damaged but not yet neovascularised vessels: outpouchings, leakage of blood and lipid, and small infarcts, with fluid collecting at the macula."],
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
      "Correct — extensive capillary closure leaves retina hypoxic, and the vascular endothelial growth factor released in response drives fragile new vessels onto the retina and disc."],
     ["Rising intraocular pressure forces new vessels to form",
      "Intraocular pressure plays no part in this transition; retinal ischaemia and the growth factor it releases do."],
     ["Accumulation of lipofuscin beneath the pigment epithelium",
      "That is drusen formation in macular degeneration."],
     ["Bacterial collagenase digestion of the retinal surface",
      "That mechanism belongs to corneal ulceration."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="etiology",
   q="Where do hard exudates and cotton-wool spots sit, and what does each represent?",
   opts=[
     ["Hard exudates are lipid in the outer plexiform layer; cotton-wool spots are nerve fibre layer ischaemia or infarction",
      "Correct — hard exudates are lipid left behind when leaked plasma is reabsorbed, collecting in the outer plexiform layer, while cotton-wool spots are swollen axons where nerve fibre layer capillaries have occluded."],
     ["Hard exudates are nerve fibre layer infarcts; cotton-wool spots are lipid deposits",
      "This reverses the two."],
     ["Both are lipid deposits, differing only in size",
      "They are different processes in different layers."],
     ["Both are microinfarcts, differing only in age",
      "Only the cotton-wool spots are ischaemic."]],
   c=0, cite=c(37)),

 dict(topic="Diabetic retinopathy", io=IO3, slot="complication",
   q="Which complications are attached to proliferative diabetic retinopathy?",
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
      "Correct — diabetes affects working-age adults and damages the retina over years, so it dominates blindness in the band before age-related degeneration takes over."],
     ["United States adults over seventy-five",
      "That is the group for macular degeneration."],
     ["Children under sixteen worldwide",
      "Diabetic retinopathy requires years of hyperglycaemia to develop and is not a significant cause of blindness in children."],
     ["Adults over fifty worldwide",
      "The claim applies to United States adults aged twenty to seventy-four; over seventy-five, macular degeneration leads."]],
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
      "Correct — axons leave at the disc, nasal fibres cross at the chiasm, the tract carries the combined contralateral field to the lateral geniculate nucleus, and the radiation fans out to the occipital cortex."],
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
      "Correct — the fibres looping forward through the temporal lobe as Meyer loop carry the superior visual field, so their interruption removes the upper quadrant on the opposite side."],
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
      "Correct — Webster made this point directly: everything becomes flat."],
     ["Colour discrimination, because cones are unevenly distributed",
      "Colour vision does not depend on having two eyes."],
     ["Peripheral vision on both sides, because the fields overlap entirely",
      "The fields overlap only centrally."],
     ["Night vision, because rods are concentrated in one eye",
      "Rods are in both retinas."]],
   c=0, cite=au()),

 dict(topic="Optic neuropathy", io=IO10, slot="differential", kfe=True,
   q="Which causes are given for an ipsilateral optic nerve lesion?",
   opts=[
     ["Trauma, optic neuritis and ischaemic optic neuropathy",
      "Correct — a lesion before the chiasm affects only that eye, and trauma, inflammatory demyelination and ischaemia are the mechanisms that damage the nerve there."],
     ["Pituitary adenoma compression",
      "That is the chiasmal cause."],
     ["Posterior cerebral artery occlusion",
      "That is the occipital cause."],
     ["Temporal lobe surgery",
      "That affects the optic radiation."]],
   c=0, cite=c(34)),
]
