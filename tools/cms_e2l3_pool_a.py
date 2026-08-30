# CMS I Exam 2, Lecture 12 Acute Vision Loss — OBJECTIVE pool, part A.
# The syllabus objective is a compare-and-contrast across nine facets, so this
# set drills the facets themselves rather than reasoning from a presentation
# (that is what the vignette sets do). Part A takes etiology, epidemiology,
# risk factors and clinical manifestations; part B takes diagnostic testing,
# management, patient education and prognosis.
SRC = "12. Acute Vision Loss current - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
IOA = ("a — Compare and contrast the etiologies, epidemiology, risk factors, clinical "
       "manifestations, differential diagnosis, diagnostic testing, management, patient "
       "education, and prognosis of the acute vision loss disorders")

POOL_A = [

 # ---------------- Etiology ----------------
 dict(topic="Amaurosis fugax", io=IOA, lead="etiology",
   q="A 66-year-old man is being worked up for amaurosis fugax. Which two embolic sources does the lecture name?",
   opts=[
     ["Carotid and cardiac", "Correct, with retinal vascular spasm as a third mechanism."],
     ["Pulmonary and renal", "Neither is a source named for retinal emboli."],
     ["Vertebral and basilar", "Those supply the posterior circulation, not the retina here."],
     ["Aortic and femoral", "Not the sources named."],
     ["Hepatic and splenic", "Not the sources named."]],
   c=0, cite=c(5)),

 dict(topic="CRAO", io=IOA, lead="etiology",
   q="A 74-year-old man has a central retinal artery occlusion. Which etiologies does the lecture list?",
   opts=[
     ["Arteriosclerosis, atherosclerosis and emboli", "Correct, the emboli being carotid or cardiac."],
     ["Venous thrombosis", "That is the vein occlusion mechanism."],
     ["Optic nerve demyelination", "That is optic neuritis."],
     ["Vitreous traction and shrinkage of the retina", "That produces a tear and detachment."],
     ["Raised intracranial pressure", "That is papilledema."]],
   c=0, cite=c(37)),

 dict(topic="Optic neuritis", io=IOA, lead="etiology",
   q="A 30-year-old woman has optic neuritis. Which causes does the lecture give?",
   opts=[
     ["Multiple sclerosis, autoimmune, postviral or idiopathic", "Correct."],
     ["Embolism arising from the carotid artery or heart", "That causes amaurosis fugax or arterial occlusion."],
     ["Thrombosis of the retinal vein", "That causes vein occlusion."],
     ["Raised intraocular pressure", "That causes glaucoma."],
     ["Vitamin A toxicity", "That causes papilledema."]],
   c=0, cite=c(23)),

 dict(topic="Retinal detachment", io=IOA, lead="etiology",
   q="A 68-year-old man has a retinal detachment. What does the lecture say it commonly follows?",
   opts=[
     ["A retinal tear or hole", "Correct, with vitreous shrinkage over time behind it."],
     ["An embolus in the central artery", "That causes arterial occlusion."],
     ["A thrombus in the central vein", "That causes vein occlusion."],
     ["Optic nerve inflammation", "That causes optic neuritis."],
     ["Closure of the drainage angle", "That causes angle-closure glaucoma."]],
   c=0, cite=c(26)),

 dict(topic="Retinal detachment", io=IOA, lead="etiology",
   q="A 70-year-old woman is told she has one of the three types of retinal detachment. Which types does the lecture name?",
   opts=[
     ["Rhegmatogenous, traction and serous", "Correct; the serous form is also called exudative."],
     ["Arteritic and non-arteritic types", "Those are the anterior ischemic optic neuropathies."],
     ["Open-angle and closed-angle", "Those are the glaucomas."],
     ["Central and branch", "Those describe the vascular occlusions."],
     ["Acute, chronic and atrophic", "Those are the phases of papilledema."]],
   c=0, cite=c(26)),

 dict(topic="Papilledema", io=IOA, lead="etiology",
   q="A 37-year-old man has papilledema. Which causes does the lecture list?",
   opts=[
     ["Tumour, trauma, infection, haemorrhage and vitamin A toxicity", "Correct, all raising intracranial pressure."],
     ["Carotid emboli, cardiac emboli and retinal vascular spasm", "Those cause amaurosis fugax and arterial occlusion."],
     ["Trabecular meshwork aging", "That causes chronic glaucoma."],
     ["Vitreous shrinkage", "That precedes retinal detachment."],
     ["Autoimmune demyelination", "That causes optic neuritis."]],
   c=0, cite=c(43)),

 dict(topic="AAION", io=IOA, lead="etiology",
   q="A 78-year-old woman is diagnosed with arteritic anterior ischemic optic neuropathy. What causes it?",
   opts=[
     ["Giant cell arteritis", "Correct, also called temporal arteritis."],
     ["A small crowded optic disc", "That is the non-arteritic association."],
     ["Carotid embolism", "That causes arterial occlusion."],
     ["Raised intracranial pressure", "That causes papilledema."],
     ["Retinal vein thrombosis", "That causes vein occlusion."]],
   c=0, cite=c(49)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="etiology",
   q="A 63-year-old man has chronic open-angle glaucoma. How does the lecture characterise its cause?",
   opts=[
     ["Idiopathic optic nerve damage", "Correct, from trabecular meshwork change with aging."],
     ["Mechanical closure by the iris", "That is the acute angle-closure mechanism."],
     ["An inflammatory arteritis", "That underlies arteritic optic neuropathy."],
     ["An embolic occlusion", "That underlies arterial occlusion."],
     ["Raised intracranial pressure", "That underlies papilledema."]],
   c=0, cite=c(15)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="etiology",
   q="A 61-year-old woman has secondary angle-closure glaucoma. Which mechanical causes does the lecture list?",
   opts=[
     ["Tumour, scarring or other mechanical causes", "Correct."],
     ["Embolism and thrombosis", "Those are vascular, not mechanical."],
     ["Demyelination and inflammation", "Those cause optic neuritis."],
     ["Vitreous shrinkage and traction on the retina", "Those precede detachment."],
     ["Vitamin A toxicity", "That causes papilledema."]],
   c=0, cite=c(14)),

 # ---------------- Epidemiology ----------------
 dict(topic="Retinal detachment", io=IOA, lead="epidemiology",
   q="A 52-year-old woman asks at what age retinal detachment becomes most common. What does the lecture say?",
   opts=[
     ["After age 50", "Correct, as the vitreous shrinks with age."],
     ["Under age 20", "Not the group described."],
     ["Between 18 and 45", "That is the optic neuritis group."],
     ["Between 40 and 60", "That is the non-arteritic optic neuropathy group."],
     ["Over age 80 only", "The threshold given is lower."]],
   c=0, cite=c(26)),

 dict(topic="Optic neuritis", io=IOA, lead="epidemiology",
   q="A 27-year-old patient is diagnosed with optic neuritis. What proportion of cases occur in women?",
   opts=[
     ["About 75 percent", "Correct, in patients aged 18 to 45."],
     ["About 50 percent", "Lower than the figure given."],
     ["About 25 percent", "That would reverse the sex distribution."],
     ["About 90 percent", "Higher than the figure given."],
     ["Sex distribution is not stated", "The lecture gives a figure."]],
   c=0, cite=c(23)),

 dict(topic="AAION", io=IOA, lead="epidemiology",
   q="A 74-year-old woman is being assessed for arteritic anterior ischemic optic neuropathy. Which age threshold does the lecture give?",
   opts=[
     ["55 years and older", "Correct."],
     ["40 to 60 years", "That is the non-arteritic group."],
     ["18 to 45 years", "That is the optic neuritis group."],
     ["Over 80 years only", "The threshold given is lower."],
     ["Any age", "An age threshold is specified."]],
   c=0, cite=c(49)),

 dict(topic="NAION", io=IOA, lead="epidemiology",
   q="A 51-year-old man is diagnosed with non-arteritic anterior ischemic optic neuropathy. Which age range does the lecture give?",
   opts=[
     ["40 to 60 years", "Correct, accounting for 90 to 95 percent of cases."],
     ["55 years and older", "That is the arteritic group."],
     ["18 to 45 years", "That is the optic neuritis group."],
     ["Over 70 years", "Older than the range given."],
     ["Under 30 years", "Younger than the range given."]],
   c=0, cite=c(48)),

 dict(topic="Glaucoma", io=IOA, lead="epidemiology",
   q="A 56-year-old man asks how serious glaucoma is worldwide. What did the lecturer say?",
   opts=[
     ["It is a leading cause of blindness worldwide", "Correct, and untreated disease ends in blindness."],
     ["It rarely causes blindness", "Untreated, it does."],
     ["It affects only the elderly", "Adults over 40 are at risk."],
     ["It is confined to one population group", "Several groups carry higher risk, but it is not confined."],
     ["It is always reversible", "Field loss already sustained does not return."]],
   c=0, cite=c(13)),

 dict(topic="CRVO", io=IOA, lead="epidemiology",
   q="A 64-year-old woman asks how the two central retinal vascular occlusions compare in frequency. What does the lecture state?",
   opts=[
     ["Vein occlusion is the more common", "Correct."],
     ["Artery occlusion is the more common", "The lecture states the opposite."],
     ["They are equally common", "One is stated to be more common."],
     ["Neither occurs before age 70", "Age over 50 is the listed risk."],
     ["Branch forms are more common than both", "The lecture does not make that comparison."]],
   c=0, cite=c(32)),

 # ---------------- Risk factors ----------------
 dict(topic="Amaurosis fugax", io=IOA, lead="risk factor",
   q="A 68-year-old man with amaurosis fugax is assessed for risk factors. Which does the lecture list?",
   opts=[
     ["Diabetes, hypertension and atherosclerosis", "Correct, with older age, valve disease, sickle cell and Raynaud's."],
     ["Myopia and cataract surgery", "Those are retinal detachment risks."],
     ["Anterior uveitis and anticholinergics", "Those are angle-closure risks."],
     ["Sleep apnea and a small optic disc", "Those are non-arteritic optic neuropathy risks."],
     ["Vitamin A excess", "That is a papilledema cause."]],
   c=0, cite=c(5)),

 dict(topic="Retinal detachment", io=IOA, lead="risk factor",
   q="A 57-year-old woman is counselled about retinal detachment risk. Which set does the lecture list?",
   opts=[
     ["Myopia, trauma, cataract extraction and diabetes", "Correct, with tumour, connective tissue disease and family history."],
     ["Anticholinergics and nebulized bronchodilators", "Those are angle-closure risks."],
     ["Sleep apnea and high cholesterol", "Those are non-arteritic optic neuropathy risks."],
     ["Scalp tenderness and jaw claudication", "Those are arteritic symptoms, not detachment risks."],
     ["Intracranial infection and trauma", "Those cause papilledema."]],
   c=0, cite=c(26)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="risk factor",
   q="A 44-year-old African American man asks about his glaucoma risk. Which factors does the lecture list for the chronic open-angle form?",
   opts=[
     ["African American race, age over 40 and diabetes", "Correct, with Hispanic ethnicity, family history, hypertension and myopia."],
     ["Sickle cell disease, Raynaud's and valve disease", "Those are listed for amaurosis fugax."],
     ["Cataract extraction and trauma", "Those are detachment risks."],
     ["Sleep apnea and a crowded disc", "Those are non-arteritic optic neuropathy risks."],
     ["Vitamin A toxicity", "That causes papilledema."]],
   c=0, cite=c(15)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="risk factor",
   q="A 60-year-old woman is assessed for angle-closure risk. Which does the lecture list?",
   opts=[
     ["Systemic anticholinergics and prior uveitis", "Correct, with nebulized bronchodilators and lens dislocation."],
     ["Myopia and cataract extraction", "Those are detachment risks."],
     ["Sickle cell and coagulation disorder", "Those are amaurosis fugax risks."],
     ["Sleep apnea and hyperlipidaemia", "Those are non-arteritic optic neuropathy risks."],
     ["Intracranial haemorrhage", "That causes papilledema."]],
   c=0, cite=c(14)),

 dict(topic="CRVO", io=IOA, lead="risk factor",
   q="A 66-year-old man with a central retinal vein occlusion is assessed. Which risk factors does the lecture list?",
   opts=[
     ["Hypertension, diabetes and hyperlipidaemia", "Correct, with age over 50, hypercoagulable states, obesity and endocarditis."],
     ["Myopia, trauma and vitreous shrinkage", "Those are detachment risks."],
     ["Anticholinergic drugs", "That is an angle-closure risk."],
     ["Postviral illness", "That is an optic neuritis association."],
     ["Vitamin A toxicity", "That causes papilledema."]],
   c=0, cite=c(32)),

 dict(topic="NAION", io=IOA, lead="risk factor",
   q="A 53-year-old man with non-arteritic anterior ischemic optic neuropathy is reviewed. Which associations does the lecture name?",
   opts=[
     ["Hypertension, diabetes, high cholesterol and sleep apnea", "Correct, with a small structural disc at risk."],
     ["Anterior uveitis and systemic anticholinergic drugs", "Those are angle-closure risks."],
     ["Myopia and cataract surgery", "Those are detachment risks."],
     ["Postviral and autoimmune disease", "Those are optic neuritis associations."],
     ["Intracranial infection", "That causes papilledema."]],
   c=0, cite=c(48)),

 dict(topic="NAION", io=IOA, lead="finding",
   q="A 50-year-old man is told he has a disc at risk. What does this term describe?",
   opts=[
     ["A small structural optic disc", "Correct, the anatomical association with the non-arteritic form."],
     ["A deeply cupped disc", "That is glaucomatous."],
     ["A swollen disc from raised intracranial pressure", "That is papilledema."],
     ["A disc with splinter haemorrhages", "That is a glaucomatous rim change."],
     ["A pale, atrophic disc", "That is a late finding, not the structural predisposition."]],
   c=0, cite=c(48)),

 # ---------------- Clinical manifestations ----------------
 dict(topic="Amaurosis fugax", io=IOA, lead="manifestation",
   q="A 70-year-old man has amaurosis fugax. How long does the lecture say an episode lasts?",
   opts=[
     ["A few seconds to minutes", "Correct; hours argues against a transient ischemic attack."],
     ["Several hours", "Too long for the described episode."],
     ["One to two days", "That is the optic neuritis time course."],
     ["Instantaneous and permanent", "That is arterial occlusion."],
     ["Weeks to months", "That is the vein occlusion time course in some patients."]],
   c=0, cite=c(4)),

 dict(topic="Amaurosis fugax", io=IOA, lead="manifestation",
   q="A 65-year-old woman describes what the lecture calls fleeting blindness. Which term is this a synonym for?",
   opts=[
     ["Amaurosis fugax", "Correct, monocular episodic visual loss."],
     ["Papilledema", "That is disc swelling from raised intracranial pressure."],
     ["Optic neuritis", "That is optic nerve inflammation."],
     ["Retinal detachment", "That is separation of the retina."],
     ["Angle-closure glaucoma", "That is acute obstruction of drainage."]],
   c=0, cite=c(5)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="manifestation",
   q="A 62-year-old man has acute angle-closure glaucoma. Which symptom set does the lecture give?",
   opts=[
     ["Severe eye pain, headache, nausea and vomiting", "Correct, with coloured halos around lights and decreased vision."],
     ["Painless gradual peripheral field loss", "That is the chronic open-angle form."],
     ["Painful eye movement with colour loss", "That is optic neuritis."],
     ["Flashes, floaters and a curtain", "That is retinal detachment."],
     ["Flickering and double vision with headache", "That is papilledema."]],
   c=0, cite=c(16)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="manifestation",
   q="A 68-year-old woman has chronic open-angle glaucoma. How does the lecture describe the typical presentation?",
   opts=[
     ["Asymptomatic in most patients", "Correct; peripheral field is lost slowly and silently."],
     ["Severe eye pain and vomiting", "That is the acute angle-closure form."],
     ["Sudden painless loss over seconds", "That is arterial occlusion."],
     ["Painful eye movement", "That is optic neuritis."],
     ["Flashes and floaters", "That is a retinal tear."]],
   c=0, cite=c(16)),

 dict(topic="Optic neuritis", io=IOA, lead="manifestation",
   q="A 32-year-old woman has optic neuritis. Over what period does the lecture say vision is lost?",
   opts=[
     ["Hours to several days", "Correct, unilateral, with painful eye movement."],
     ["A few seconds", "That is arterial occlusion."],
     ["Seconds to minutes, then recovery", "That is amaurosis fugax."],
     ["Years", "That is chronic glaucoma."],
     ["Instantly on waking", "That pattern fits ischemic optic neuropathy."]],
   c=0, cite=c(23)),

 dict(topic="Optic neuritis", io=IOA, lead="manifestation",
   q="A 29-year-old man has optic neuritis. Which visual finding besides reduced acuity does the lecture name?",
   opts=[
     ["Loss of colour vision", "Correct, with central vision loss and a relative afferent pupillary defect."],
     ["Coloured halos around lights", "Those belong to angle-closure glaucoma."],
     ["Tunnel vision", "That belongs to chronic glaucoma."],
     ["An island of temporal vision", "That belongs to arterial occlusion."],
     ["Double vision", "That is a papilledema symptom."]],
   c=0, cite=c(23)),

 dict(topic="Retinal detachment", io=IOA, lead="manifestation",
   q="A 69-year-old man has a retinal detachment. Which feature does the lecture describe that is unusual among these diagnoses?",
   opts=[
     ["Vision changes with head position", "Correct, because the detached retina moves."],
     ["Vision improves in bright light", "Not a described feature."],
     ["Vision is worse on waking only", "Not a described feature."],
     ["Vision loss alternates between eyes", "This is a monocular process."],
     ["Vision returns fully within minutes", "That is amaurosis fugax."]],
   c=0, cite=c(27)),

 dict(topic="CRAO", io=IOA, lead="manifestation",
   q="A 73-year-old man has a central retinal artery occlusion. Which range of visual acuity does the lecture give?",
   opts=[
     ["Counting fingers to light perception", "Correct, describing profound loss."],
     ["20/40 to 20/60", "Far better than the loss described."],
     ["Normal acuity with a field defect", "Acuity is profoundly reduced."],
     ["Fluctuating between normal and blind", "The loss is fixed."],
     ["Loss of colour vision only", "That is optic neuritis."]],
   c=0, cite=c(38)),

 dict(topic="CRVO", io=IOA, lead="manifestation",
   q="A 62-year-old man has a central retinal vein occlusion. How does the lecture describe the onset?",
   opts=[
     ["Sudden and painless, sometimes gradual over days to weeks", "Correct."],
     ["Sudden and severely painful", "That is angle-closure glaucoma."],
     ["Gradual over years", "That is chronic glaucoma."],
     ["Transient, lasting from a few seconds to under a minute", "That is amaurosis fugax."],
     ["Painful over hours to days", "That is optic neuritis."]],
   c=0, cite=c(33)),

 dict(topic="Papilledema", io=IOA, lead="manifestation",
   q="A 35-year-old woman has papilledema. Which visual complaints does the lecture list?",
   opts=[
     ["Flickering, blurry and double vision", "Correct, all non-specific."],
     ["Coloured halos seen around bright lights", "Those belong to angle-closure glaucoma."],
     ["A curtain across the field", "That belongs to detachment or amaurosis fugax."],
     ["Loss of colour vision", "That belongs to optic neuritis."],
     ["Tunnel vision", "That belongs to chronic glaucoma."]],
   c=0, cite=c(44)),

 dict(topic="Papilledema", io=IOA, lead="manifestation",
   q="A 40-year-old man has papilledema. Which non-visual symptoms does the lecture list?",
   opts=[
     ["Nausea, vomiting and headache", "Correct, the non-specific signs of raised intracranial pressure."],
     ["Jaw claudication and scalp tenderness", "Those belong to arteritic optic neuropathy."],
     ["Fever and night sweats", "Not the symptoms listed."],
     ["Chest pain and palpitations", "Not the symptoms listed."],
     ["Neck stiffness alone", "Not the symptom set given."]],
   c=0, cite=c(44)),

 dict(topic="AAION", io=IOA, lead="manifestation",
   q="A 77-year-old woman has arteritic anterior ischemic optic neuropathy. Which systemic symptoms does the lecture list?",
   opts=[
     ["Malaise, weight loss, headache, fever and scalp tenderness", "Correct, with jaw claudication on chewing."],
     ["Severe eye pain, nausea, vomiting and coloured halos", "Those belong to angle-closure glaucoma."],
     ["Flashes and floaters", "Those belong to a retinal tear."],
     ["Painful eye movement", "That belongs to optic neuritis."],
     ["Numbness and limb weakness", "Not the symptom set given."]],
   c=0, cite=c(49)),

 dict(topic="AION", io=IOA, lead="manifestation",
   q="A 70-year-old man has anterior ischemic optic neuropathy. How does the lecture describe the vision loss?",
   opts=[
     ["Sudden and painless, of side or central vision", "Correct."],
     ["Gradual and painless, developing over years", "That is chronic glaucoma."],
     ["Sudden and severely painful", "That is angle-closure glaucoma."],
     ["Transient with full recovery", "That is amaurosis fugax."],
     ["Painful over hours to days", "That is optic neuritis."]],
   c=0, cite=c(50)),

 dict(topic="Angle-closure glaucoma", io=IOA, lead="finding",
   q="A 58-year-old woman has acute angle-closure glaucoma. Which examination findings does the lecture list?",
   opts=[
     ["Pupillary dilation, hazy cornea and a narrow angle", "Correct, with markedly elevated intraocular pressure."],
     ["Optic nerve cupping with splinter haemorrhages", "Those belong to the chronic form."],
     ["Disc elevation with blurred margins", "That is papilledema."],
     ["A cherry-red spot at the fovea", "That is arterial occlusion."],
     ["Cotton wool spots and haemorrhages", "Those are vein occlusion findings."]],
   c=0, cite=c(17)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="finding",
   q="A 65-year-old man has chronic open-angle glaucoma. Which optic nerve findings does the lecture list besides cupping?",
   opts=[
     ["Rim pitting, bayoneting and splinter haemorrhages", "Correct, with rim thinning and visual field defects."],
     ["Cotton wool spots, venous dilation and haemorrhage", "Those are vein occlusion findings."],
     ["A cherry-red macula", "That is arterial occlusion."],
     ["Engorged veins with disc elevation", "That is papilledema."],
     ["An elevated grey retina with folds", "That is detachment."]],
   c=0, cite=c(18)),

 dict(topic="Open-angle glaucoma", io=IOA, lead="finding",
   q="A 71-year-old woman has bayoneting noted on her optic disc. What does the term describe?",
   opts=[
     ["Blood vessels with narrow angulations", "Correct, one of the glaucomatous rim changes."],
     ["Widening of the central cup", "That is cupping itself."],
     ["Haemorrhage in all four quadrants", "That is vein occlusion."],
     ["Pallor of the whole disc", "That is ischemic optic neuropathy."],
     ["Elevation of the disc margin", "That is papilledema."]],
   c=0, cite=c(18)),

 dict(topic="CRAO", io=IOA, lead="finding",
   q="A 75-year-old man has a central retinal artery occlusion. Which fundus findings does the lecture describe?",
   opts=[
     ["Pale retinal swelling with a cherry-red fovea", "Correct, with emboli visible in the central artery."],
     ["Disc swelling with cotton wool spots and haemorrhage", "That is vein occlusion."],
     ["An elevated grey retina", "That is detachment."],
     ["A deeply cupped disc", "That is chronic glaucoma."],
     ["Bilateral disc elevation", "That is papilledema."]],
   c=0, cite=c(39)),

 dict(topic="CRVO", io=IOA, lead="finding",
   q="A 67-year-old woman has a central retinal vein occlusion. Which findings does the lecture list on examination?",
   opts=[
     ["Disc swelling, venous dilation and cotton wool spots", "Correct, with retinal haemorrhages."],
     ["Pale retinal swelling with a cherry-red spot at the fovea", "That is arterial occlusion."],
     ["A hazy cornea and narrow angle", "That is angle-closure glaucoma."],
     ["An elevated grey retina with folds", "That is detachment."],
     ["A normal disc with colour loss", "That is optic neuritis."]],
   c=0, cite=c(34)),

 dict(topic="Retinal detachment", io=IOA, lead="finding",
   q="A 64-year-old man has a retinal detachment. How does the lecture describe a retinal tear on examination?",
   opts=[
     ["Orange and crescent shaped", "Correct, against the elevated grey detached retina."],
     ["Pale and wedge shaped", "That describes branch arterial occlusion."],
     ["Red and flame shaped", "That describes retinal haemorrhage."],
     ["White and fluffy", "That describes cotton wool spots."],
     ["Dark and pigmented centrally", "The detachment is pigmented, not the tear."]],
   c=0, cite=c(29)),

 dict(topic="Papilledema", io=IOA, lead="finding",
   q="A 42-year-old woman has papilledema. Which fundus findings does the lecture list?",
   opts=[
     ["Engorged retinal veins and a swollen optic disc", "Correct, with or without retinal haemorrhages."],
     ["A cherry-red spot at the fovea with retinal pallor", "That is arterial occlusion."],
     ["Optic nerve cupping", "That is chronic glaucoma."],
     ["An elevated grey retina", "That is detachment."],
     ["A hazy cornea", "That is angle-closure glaucoma."]],
   c=0, cite=c(46)),
]
