# -*- coding: utf-8 -*-
# PD2 Lecture 3 (Advanced Ocular Medical History and Examination, Prof. Beck)
# -- pool A: the history, the symptom patterns, and the order of the exam.
#
# BECK'S SKIP INSTRUCTIONS ARE BINDING. Jaxon: "if she says don't worry about a
# slide then she won't test on it so no need to include it." Six things are
# excluded outright and pd2_l3_partition.py asserts none of them appears:
#   1. the named virus (adenovirus) in viral conjunctivitis
#   2. the exophthalmometer technique and its 20-22 mm figure
#   3. the strabismus diagram -- "just a visual ... you don't have to memorize"
#   4. the corneal reflection test -- already examined in PD1
#   5. the Adie's tonic pupil ASSOCIATIONS slide (Adie's itself IS in scope)
#   6. the Latin expansions of OD/OS/OU (the abbreviations themselves ARE in)
#
# This is a PHYSICAL DIAGNOSIS course: questions are about eliciting a finding
# and reading it, not about the pathophysiology behind it.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "PD II Advanced Exam Ocular Lecture - Beck.pptx"
def c(n): return f"{SRC}, Slide {n}"
def ci(n): return f"{SRC}, Slide {n} (image only)"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"
def au(): return "Lecture recording, 26 August 2026"

IO = "Instructional Objectives — Advanced Ocular Medical History and Examination"

POOL_A = [
 dict(topic="Vocabulary", io=IO, slot="test finding",
   q="Which option gives the meaning of miosis and names its opposite correctly?",
   opts=[
     ["Pupil constriction; mydriasis is pupil dilatation",
      "Correct — miosis is pupil constriction, and its opposite, mydriasis, is pupil dilatation."],
     ["Pupil dilatation; mydriasis is pupil constriction",
      "This swaps the terms: miosis is pupil constriction, and mydriasis is pupil dilatation."],
     ["Inward folding of the lower eyelid; ectropion is the opposite",
      "Inward folding of the lower lid is entropion and outward turning is ectropion; miosis is pupil constriction."],
     ["Forward displacement of the globe; enophthalmos is the opposite",
      "Forward displacement of the eye in the orbit is proptosis; miosis is pupil constriction, opposite to mydriasis."]],
   c=0, cite=c(3)),

 dict(topic="Vocabulary", io=IO, slot="test finding",
   q="What is chemosis?",
   opts=[
     ["Swelling and inflammation of the conjunctiva",
      "Correct — chemosis is swelling and inflammation of the conjunctiva itself, not of the lids or the globe."],
     ["Injection of the superficially visible vessels of the conjunctiva or sclera",
      "That is hyperemia, injection of the superficially visible vessels; chemosis is swelling and inflammation of the conjunctiva."],
     ["Forward displacement of the eye in the orbit",
      "That is proptosis, forward displacement of the eye; chemosis is swelling and inflammation of the conjunctiva."],
     ["Outward turning of the lower eyelid",
      "That is ectropion, outward turning of the lower lid; chemosis is swelling and inflammation of the conjunctiva."]],
   c=0, cite=c(3)),

 dict(topic="Vocabulary", io=IO, slot="test finding",
   q="What is hyperemia?",
   opts=[
     ["Injection of the superficially visible vessels of the conjunctiva, episclera or sclera",
      "Correct — hyperemia is injection of the superficially visible vessels of the conjunctiva, episclera or sclera."],
     ["Swelling of the conjunctiva",
      "That is chemosis, swelling and inflammation of the conjunctiva; hyperemia is injection of the superficial visible vessels."],
     ["Blood collecting beneath the conjunctiva",
      "That is a subconjunctival hemorrhage, blood leaking outside the vessels; hyperemia is injection of the visible vessels."],
     ["Inward folding of the lower lid",
      "That is entropion, inward folding of the lower lid; hyperemia is injection of the superficially visible vessels."]],
   c=0, cite=c(3)),

 dict(topic="Vocabulary", io=IO, slot="differential",
   q="Entropion and ectropion both affect which eyelid?",
   opts=[
     ["The lower lid", "Correct — entropion is inward folding and ectropion outward turning, and both affect the lower lid."],
     ["The upper lid", "Both malpositions affect the lower lid: entropion folds it inward and ectropion turns it outward."],
     ["Both lids equally", "They do not affect both lids equally; entropion and ectropion are both lower lid malpositions."],
     ["Neither — they affect the conjunctiva", "They are lid malpositions, not conjunctival disease: entropion turns the lower lid in, ectropion turns it out."]],
   c=0, cite=c(3)),

 dict(topic="History", io=IO, slot="initial test",
   q="Which four dimensions assess any eye complaint?",
   opts=[
     ["Time course, precipitating factors, palliative or exacerbating variables, and vision loss or visual deficits",
      "Correct — every eye complaint is assessed by time course, precipitating factors, palliative or exacerbating variables and vision loss."],
     ["Onset, duration, severity and radiation",
      "Radiation is not one of them; the frame is time course, precipitating factors, what helps or worsens it, and vision loss."],
     ["Location, quality, quantity and timing",
      "Quality and quantity are not in it; the frame is time course, precipitating factors, palliative or exacerbating variables, and visual deficits."],
     ["Fever, discharge, photophobia and itch",
      "Those are symptoms and findings, not the frame; eye complaints are assessed by time course, precipitating factors, modifiers and vision loss."]],
   c=0, cite=c(7)),

 dict(topic="History", io=IO, slot="differential",
   q="Bilateral visual loss usually implies which kind of problem?",
   opts=[
     ["A primary neurologic cause rather than a primary ophthalmologic one",
      "Correct — bilateral visual loss usually implies a primary neurologic etiology and not a primary ophthalmologic problem."],
     ["A primary ophthalmologic cause",
      "It runs the other way: bilateral visual loss usually implies a primary neurologic etiology, not an ophthalmologic one."],
     ["An infective cause",
      "Infection is not the usual inference; bilateral visual loss usually implies a primary neurologic etiology."],
     ["A traumatic cause",
      "Trauma is not the usual inference; bilateral visual loss usually implies a primary neurologic etiology rather than an eye problem."]],
   c=0, cite=cn(10)),

 dict(topic="History", io=IO, slot="differential",
   q="How do multiple NEW flashes or floaters differ in significance from a single floater?",
   opts=[
     ["Multiple new flashes or floaters suggest a retinal tear or vitreous hemorrhage",
      "Correct — multiple new flashes or floaters could represent a retinal tear or vitreous hemorrhage, while a single floater is probably benign."],
     ["A single floater suggests a retinal tear; multiple floaters are benign",
      "This reverses them: a single floater is probably benign, and multiple new flashes or floaters suggest a retinal tear or vitreous hemorrhage."],
     ["Both are always benign",
      "Only the single floater is probably benign; multiple new flashes or floaters could represent a retinal tear or vitreous hemorrhage."],
     ["Both always require emergency referral",
      "A single floater is probably benign; it is multiple new flashes or floaters that suggest a retinal tear or vitreous hemorrhage."]],
   c=0, cite=c(10)),

 dict(topic="History", io=IO, slot="differential",
   q="How does the RATE of onset of visual impairment guide the differential?",
   opts=[
     ["Rapid deterioration suggests a vascular cause",
      "Correct — rapid deterioration should make you strongly consider vascular causes, while gradual loss suggests causes such as cataract."],
     ["Rapid deterioration suggests cataract; gradual loss suggests a vascular cause",
      "This reverses the pairing: rapid deterioration points to vascular causes, and gradual loss to causes such as cataract."],
     ["Rate of onset does not narrow the differential",
      "The rate of onset does give a clue to etiology: rapid deterioration suggests vascular causes, gradual loss cataract."],
     ["Rapid deterioration always means trauma",
      "Rapid deterioration points to vascular causes, not trauma; gradual loss suggests causes such as cataract."]],
   c=0, cite=c(11)),

 dict(topic="History", io=IO, slot="differential",
   q="Which two symptoms together suggest an allergic cause?",
   opts=[
     ["Itching and excessive tearing", "Correct — itching together with excessive tearing suggests an allergic cause of the eye complaint."],
     ["Deep pain and photophobia", "Deep pain suggests acute narrow angle glaucoma and photophobia suggests iritis; itching with tearing suggests allergy."],
     ["Burning and purulent discharge", "Purulent discharge suggests a bacterial infection; itching with excessive tearing is what suggests an allergic cause."],
     ["Foreign body sensation and reduced vision", "Those fit a corneal injury such as an abrasion; itching with excessive tearing is what suggests an allergic cause."]],
   c=0, cite=c(12)),

 dict(topic="History", io=IO, slot="differential",
   q="Deep eye pain is associated with which condition?",
   opts=[
     ["Acute narrow angle glaucoma", "Correct — deep eye pain is linked to acute narrow angle glaucoma; pain from a deeper source is not relieved by topical anesthetic."],
     ["Allergic conjunctivitis", "Allergy shows itching and excessive tearing rather than deep pain, which is linked to acute narrow angle glaucoma."],
     ["Corneal abrasion", "A corneal abrasion is a surface injury that feels better with topical anesthetic; deep pain points to acute narrow angle glaucoma."],
     ["Blepharitis", "Blepharitis is a common lid inflammation linked to bacterial infection or atopic dermatitis; deep pain points to angle closure."]],
   c=0, cite=c(12)),

 dict(topic="Topical anesthetic test", io=IO, slot="test finding",
   q="A patient's eye pain is relieved by a topical anesthetic. What does that suggest?",
   opts=[
     ["Relief suggests a surface problem such as a corneal injury",
      "Correct — a corneal injury feels better with anesthetic, whereas pain that is not relieved may come from a deeper source."],
     ["Relief suggests a deep source; no relief suggests a surface problem",
      "This reverses it: relief points to a surface cause such as corneal injury, and no relief points to a deeper source."],
     ["Relief confirms acute glaucoma",
      "Acute narrow angle glaucoma causes deep pain, and pain from a deeper source is not relieved by topical anesthetic."],
     ["The response tells you nothing about depth",
      "The response does separate depth: relief suggests a surface injury, and pain not relieved suggests a deeper source."]],
   c=0, cite=c(12)),

 dict(topic="History", io=IO, slot="risk factors",
   q="Which four elements make up the ocular history?",
   opts=[
     ["Corrective lenses, acute or chronic eye problems, eye medications, and eye surgery history",
      "Correct — the ocular history covers corrective lenses, acute or chronic eye problems such as glaucoma, eye medications and eye surgery."],
     ["Smoking, alcohol, occupation and hobbies",
      "Those belong to a general social history; the ocular history asks about lenses, eye problems, eye medications and eye surgery."],
     ["Fever, weight loss, night sweats and rash",
      "Those are constitutional symptoms; the ocular history asks about corrective lenses, eye problems, eye medications and eye surgery."],
     ["Family history alone",
      "Family history is not one of the four; they are corrective lenses, eye problems, eye medications and eye surgery history."]],
   c=0, cite=c(13)),

 dict(topic="History", io=IO, slot="risk factors",
   q="Which immunization status matters in eye trauma?",
   opts=[
     ["Tetanus", "Correct — tetanus immunization status is important in any patient with a history of eye trauma."],
     ["Influenza", "Influenza status is not the one tied to eye trauma; tetanus immunization status is what matters after an eye injury."],
     ["Pneumococcal", "Pneumococcal status is not the one tied to eye trauma; tetanus immunization status is what matters after an eye injury."],
     ["Hepatitis B", "Hepatitis B status is not the one tied to eye trauma; tetanus immunization status is what matters after an eye injury."]],
   c=0, cite=c(15)),

 dict(topic="History", io=IO, slot="initial test",
   q="After a chemical or fluid splash to the eye, what must you establish?",
   opts=[
     ["The acidity or alkalinity of the fluid",
      "Correct — after any chemical or fluid exposure, knowing whether the fluid was acidic or alkaline is essential."],
     ["The volume of fluid involved",
      "Volume is not what must be known; you must establish whether the fluid or chemical was acidic or alkaline."],
     ["Whether the patient was wearing contact lenses",
      "Contact lens wear is not the essential fact here; you must establish the acidity or alkalinity of the fluid."],
     ["The manufacturer of the product",
      "The brand is not what matters; the essential fact after a chemical exposure is its acidity or alkalinity."]],
   c=0, cite=c(15)),

 dict(topic="History", io=IO, slot="risk factors",
   q="Besides diabetes and hypertension, which systemic disease is a relevant part of the ocular history?",
   opts=[
     ["Human immunodeficiency virus disease",
      "Correct — the relevant systemic diseases to ask about are diabetes, hypertension and human immunodeficiency virus disease."],
     ["Chronic obstructive pulmonary disease",
      "Lung disease is not among them; the relevant systemic diseases are diabetes, hypertension and human immunodeficiency virus disease."],
     ["Gastroesophageal reflux disease",
      "Reflux disease is not among them; the relevant systemic diseases are diabetes, hypertension and human immunodeficiency virus disease."],
     ["Iron deficiency anemia",
      "Anemia is not among them; the relevant systemic diseases are diabetes, hypertension and human immunodeficiency virus disease."]],
   c=0, cite="PD II Advanced Exam Ocular Lecture - Beck.pptx, Slide 14"),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Acute, unilateral and PAINLESS visual loss suggests which group of causes?",
   opts=[
     ["Retinal vascular occlusion, retinal detachment, vitreous hemorrhage, macular degeneration",
      "Correct — acute, unilateral, painless loss suggests retinal vascular occlusion, retinal detachment, vitreous hemorrhage or macular degeneration."],
     ["Corneal abrasion or ulcer, uveitis, traumatic hyphema, acute narrow angle glaucoma",
      "Those are the acute, unilateral PAINFUL causes, which usually sit in the cornea and anterior chamber."],
     ["Thermal, radiation or chemical exposure",
      "Thermal, radiation or chemical exposure is considered when symptoms are acute, BILATERAL and painful."],
     ["Simple glaucoma or cataract",
      "Simple glaucoma or cataract causes GRADUAL painless loss, not the acute unilateral painless picture."]],
   c=0, cite=c(16)),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Acute, unilateral and PAINFUL visual loss usually localizes to where?",
   opts=[
     ["Usually the cornea and anterior chamber",
      "Correct — acute, unilateral, painful causes usually sit in the cornea and anterior chamber: abrasion or ulcer, uveitis, hyphema, angle closure."],
     ["Usually the retina — vascular occlusion and detachment",
      "Retinal vascular occlusion and detachment are acute, unilateral PAINLESS causes; the painful ones sit in the cornea and anterior chamber."],
     ["Usually the optic nerve — optic neuritis alone",
      "Optic neuritis is not the grouping; acute, unilateral, painful causes usually sit in the cornea and anterior chamber."],
     ["Usually the lids — blepharitis and hordeolum",
      "Lid conditions are not in this group; acute, unilateral, painful causes usually sit in the cornea and anterior chamber."]],
   c=0, cite=c(16)),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Acute, BILATERAL and painful symptoms should make you consider what?",
   opts=[
     ["Thermal, radiation or chemical exposure",
      "Correct — acute, bilateral, painful symptoms should make you consider thermal, radiation or chemical exposures."],
     ["Retinal vascular occlusion",
      "Retinal vascular occlusion is an acute, unilateral, painless cause; bilateral painful symptoms suggest an exposure."],
     ["Simple glaucoma or cataract",
      "Simple glaucoma or cataract gives gradual, painless loss; acute bilateral pain suggests thermal, radiation or chemical exposure."],
     ["Traumatic hyphema",
      "Traumatic hyphema is an acute, unilateral, painful cause; bilateral painful symptoms suggest an exposure."]],
   c=0, cite=c(16)),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Gradual, painless visual loss suggests what?",
   opts=[
     ["Simple glaucoma or cataract", "Correct — gradual, painless visual loss suggests simple glaucoma or cataracts."],
     ["Acute narrow angle glaucoma", "Acute narrow angle glaucoma is acute and painful; gradual, painless loss suggests simple glaucoma or cataract."],
     ["Vitreous hemorrhage", "Vitreous hemorrhage is an acute, unilateral, painless cause; gradual painless loss suggests simple glaucoma or cataract."],
     ["Chemical exposure", "Chemical exposure is acute, bilateral and painful; gradual painless loss suggests simple glaucoma or cataract."]],
   c=0, cite=c(16)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain WITH BLINKING suggests what?",
   opts=[
     ["Corneal abrasion or a foreign body", "Correct — eye pain with blinking points to a corneal abrasion or a foreign body on the eye's surface."],
     ["Acute narrow angle glaucoma", "Acute narrow angle glaucoma pairs eye pain with headache; pain with blinking suggests corneal abrasion or foreign body."],
     ["Optic neuritis", "Optic neuritis causes pain on eye motion; pain with blinking suggests a corneal abrasion or foreign body."],
     ["Temporal arteritis", "Temporal arteritis pairs eye pain with temporal pain; pain with blinking suggests a corneal abrasion or foreign body."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain with a GRITTY feeling suggests what?",
   opts=[
     ["Conjunctivitis", "Correct — eye pain accompanied by a gritty feeling is the pairing for conjunctivitis."],
     ["Inflammation of the iris", "Inflammation of the iris pairs eye pain with photophobia; a gritty feeling suggests conjunctivitis."],
     ["Acute narrow angle glaucoma", "Acute narrow angle glaucoma pairs eye pain with headache; a gritty feeling suggests conjunctivitis."],
     ["Optic neuritis", "Optic neuritis causes pain on eye motion; a gritty feeling with eye pain suggests conjunctivitis."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain with PHOTOPHOBIA suggests what?",
   opts=[
     ["Inflammation of the iris", "Correct — eye pain accompanied by photophobia is the pairing for inflammation of the iris."],
     ["Optic neuritis", "Optic neuritis causes pain on eye motion; eye pain with photophobia suggests inflammation of the iris."],
     ["Temporal arteritis", "Temporal arteritis pairs eye pain with temporal pain; photophobia suggests inflammation of the iris."],
     ["Conjunctivitis", "Conjunctivitis pairs eye pain with a gritty feeling; photophobia suggests inflammation of the iris."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain ON EYE MOTION suggests what?",
   opts=[
     ["Optic neuritis", "Correct — eye pain that comes with eye motion is the pairing for optic neuritis."],
     ["Corneal abrasion", "A corneal abrasion hurts with blinking; pain on eye motion suggests optic neuritis."],
     ["Conjunctivitis", "Conjunctivitis pairs eye pain with a gritty feeling; pain on eye motion suggests optic neuritis."],
     ["Acute narrow angle glaucoma", "Acute narrow angle glaucoma pairs eye pain with headache; pain on eye motion suggests optic neuritis."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain WITH HEADACHE suggests what?",
   opts=[
     ["Acute narrow angle glaucoma", "Correct — eye pain together with headache is the pairing for acute narrow angle glaucoma."],
     ["Corneal abrasion or foreign body", "A corneal abrasion or foreign body hurts with blinking; eye pain with headache suggests acute narrow angle glaucoma."],
     ["Optic neuritis", "Optic neuritis causes pain on eye motion; eye pain with headache suggests acute narrow angle glaucoma."],
     ["Conjunctivitis", "Conjunctivitis pairs eye pain with a gritty feeling; eye pain with headache suggests acute narrow angle glaucoma."]],
   c=0, cite=c(17)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="HORIZONTAL diplopia — images side by side — points to a palsy of which cranial nerves?",
   opts=[
     ["Third or sixth", "Correct — horizontal diplopia, with images side by side, points to a palsy of cranial nerve III or VI."],
     ["Third or fourth", "Third or fourth nerve palsy gives VERTICAL diplopia, images on top of each other; horizontal points to III or VI."],
     ["Fourth or sixth", "The fourth nerve belongs to the vertical pattern; horizontal diplopia points to a palsy of cranial nerve III or VI."],
     ["Second or seventh", "Neither supplies the extraocular muscles, which are served by III, IV and VI; horizontal diplopia points to III or VI."]],
   c=0, cite=c(18)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="VERTICAL diplopia — images on top of each other — points to a palsy of which cranial nerves?",
   opts=[
     ["Third or fourth", "Correct — vertical diplopia, with images on top of each other, points to a palsy of cranial nerve III or IV."],
     ["Third or sixth", "Third or sixth nerve palsy gives HORIZONTAL diplopia, images side by side; vertical points to III or IV."],
     ["Fourth or sixth", "The sixth nerve belongs to the horizontal pattern; vertical diplopia points to a palsy of cranial nerve III or IV."],
     ["Second or third", "The second nerve is the optic nerve, carrying the afferent visual signal; vertical diplopia points to III or IV."]],
   c=0, cite=c(18)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="Which cranial nerve appears in BOTH the horizontal and vertical diplopia patterns?",
   opts=[
     ["The third", "Correct — the third nerve appears in both: horizontal diplopia is III or VI, and vertical diplopia is III or IV."],
     ["The fourth", "The fourth nerve appears only in the vertical pattern (III or IV); the third nerve appears in both patterns."],
     ["The sixth", "The sixth nerve appears only in the horizontal pattern (III or VI); the third nerve appears in both patterns."],
     ["The second", "The second nerve is the optic nerve and is in neither pattern; the third nerve appears in both horizontal and vertical."]],
   c=0, cite="PD II Advanced Exam Ocular Lecture - Beck.pptx, Slide 18"),

 dict(topic="Diplopia", io=IO, slot="etiology",
   q="Besides faulty alignment, what causes diplopia?",
   opts=[
     ["A neurological problem",
      "Correct — besides faulty alignment, diplopia comes from neurological problems: brainstem or cerebellar lesions, or extraocular muscle weakness."],
     ["Refractive error alone",
      "Refractive error is what a pinhole corrects; diplopia arises from faulty alignment or a neurological problem."],
     ["Dry eye",
      "Dryness belongs with lacrimal obstruction or Sjogren's syndrome; diplopia arises from faulty alignment or a neurological problem."],
     ["Cataract",
      "Cataract is a lens opacity causing gradual painless loss; diplopia arises from faulty alignment or a neurological problem."]],
   c=0, cite=c(18)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="Which compensatory finding accompanies diplopia?",
   opts=[
     ["A compensatory head posture", "Correct — diplopia can be accompanied by a compensatory head posture, alongside faulty alignment of the eyes."],
     ["A compensatory squint of one eye only", "A squint is itself improper alignment of the eyes, a cause of diplopia; the compensation is a head posture."],
     ["Compensatory pupil dilation", "Pupil dilation is not a compensation for double vision; the accompanying finding is a compensatory head posture."],
     ["Compensatory tearing", "Tearing points to lacrimal obstruction or Sjogren's syndrome; diplopia is accompanied by a compensatory head posture."]],
   c=0, cite=c(18)),

 dict(topic="Tearing and dryness", io=IO, slot="differential",
   q="Besides Sjogren's syndrome, what causes excessive tearing or dryness?",
   opts=[
     ["Obstruction in the lacrimal apparatus",
      "Correct — excessive tearing or dryness comes from obstruction in the lacrimal apparatus or from Sjogren's syndrome."],
     ["Clouding of the lens from a cataract",
      "A cataract is a lens opacity that causes gradual, painless loss of vision, not tearing or dryness."],
     ["Raised pressure from simple glaucoma",
      "Simple glaucoma causes gradual, painless visual loss; tearing or dryness points to lacrimal obstruction or Sjogren's syndrome."],
     ["A pterygium growing across the cornea",
      "A pterygium is a triangular conjunctival thickening that may interfere with vision; tearing points to lacrimal obstruction."]],
   c=0, cite=c(18)),

 dict(topic="Discharge", io=IO, slot="differential",
   q="Watery or mucoid discharge suggests which conditions?",
   opts=[
     ["Allergic or viral", "Correct — watery or mucoid discharge goes with allergic or viral conditions, while purulent discharge suggests bacteria."],
     ["Bacterial infection", "Bacterial infections produce purulent discharge; watery or mucoid discharge suggests allergic or viral conditions."],
     ["Acute iritis", "Acute iritis produces no ocular discharge; watery or mucoid discharge suggests allergic or viral conditions."],
     ["Acute glaucoma", "Acute glaucoma produces no ocular discharge; watery or mucoid discharge suggests allergic or viral conditions."]],
   c=0, cite=c(19)),

 dict(topic="Discharge", io=IO, slot="differential",
   q="Purulent discharge suggests what?",
   opts=[
     ["Bacterial infection", "Correct — purulent discharge suggests a bacterial infection, while watery or mucoid discharge suggests allergy or a virus."],
     ["Allergic conjunctivitis", "Allergic conditions give watery or mucoid discharge; purulent discharge suggests a bacterial infection."],
     ["Viral conjunctivitis", "Viral conditions give watery or mucoid discharge; purulent discharge suggests a bacterial infection."],
     ["Dry eye", "Dryness points to lacrimal obstruction or Sjogren's syndrome; purulent discharge suggests a bacterial infection."]],
   c=0, cite=c(19)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="Which failure would make an infectious red eye worse?",
   opts=[
     ["Failing to recognize an infectious cause and inappropriately prescribing topical corticosteroid drops",
      "Correct — missing an infectious cause of red eye and prescribing topical corticosteroid drops is a common examination mistake."],
     ["Failing to measure the intraocular pressure",
      "Ocular pressure is checked only if it can be done accurately and safely; the infection risk comes from steroid drops."],
     ["Failing to dilate the pupil",
      "Primary care clinicians do not dilate most patients; the mistake that harms an infected eye is prescribing steroid drops."],
     ["Failing to document the family history",
      "The eye findings are what must be documented; prescribing steroid drops is the mistake that worsens an infection."]],
   c=0, cite=c(20)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="Which two structures are commonly left unexamined?",
   opts=[
     ["The cornea and the lens", "Correct — failure to examine the cornea and lens is one of the common mistakes in the eye examination."],
     ["The eyelids and eyebrows", "Lids and brows are not among the common omissions; the structures commonly missed are the cornea and lens."],
     ["The lacrimal sac and puncta", "The lacrimal sac is not among the common omissions; the structures commonly missed are the cornea and lens."],
     ["The extraocular muscles", "Eye movements are not among the common omissions; the two structures commonly missed are the cornea and lens."]],
   c=0, cite=c(20)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="Which pair of diagnoses must be differentiated because the latter can lead to death?",
   opts=[
     ["Preseptal from orbital cellulitis",
      "Correct — preseptal cellulitis must be told apart from orbital cellulitis, because orbital cellulitis can lead to death."],
     ["Episcleritis from scleritis",
      "Nodular episcleritis goes with rheumatoid arthritis and lupus; the pair that matters because one can kill is preseptal versus orbital cellulitis."],
     ["Cataract from glaucoma",
      "Simple glaucoma and cataract both cause gradual painless loss; the pair that matters because one can kill is preseptal versus orbital cellulitis."],
     ["Hordeolum from chalazion",
      "A hordeolum is a painful lid-margin infection and a chalazion a painless nodule; the pair that matters is preseptal versus orbital cellulitis."]],
   c=0, cite=c(20)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="What is the warning about pressure on a globe that may be ruptured?",
   opts=[
     ["Placing too much pressure on it is a mistake",
      "Correct — failing to diagnose a ruptured globe and placing too much pressure on it are both common examination mistakes."],
     ["Pressure is required to assess the depth of injury",
      "Pressure is not used to judge depth; placing too much pressure on a ruptured globe is itself a recognized examination mistake."],
     ["Pressure is harmless once an anesthetic is instilled",
      "Anesthetic does not make it safe; placing too much pressure on a ruptured globe is a recognized examination mistake."],
     ["Pressure should be applied only with a cotton swab",
      "No instrument makes it safe; too much pressure on a ruptured globe is a recognized mistake, and the globe is not palpated in trauma."]],
   c=0, cite=c(20)),

 dict(topic="Order of examination", io=IO, slot="initial test",
   q="What is the vital sign of the eye?",
   opts=[
     ["Visual acuity", "Correct — visual acuity testing is called the vital sign of the eye and comes early in the suggested order."],
     ["Intraocular pressure", "Intraocular pressure is likened to systemic blood pressure, but visual acuity is the one called the vital sign of the eye."],
     ["Pupil reactivity", "Pupillary reactions are checked before dilating, but visual acuity is the one called the vital sign of the eye."],
     ["Visual fields", "Visual field testing follows acuity in the order; visual acuity is the one called the vital sign of the eye."]],
   c=0, cite=c(21)),

 dict(topic="Order of examination", io=IO, slot="initial test",
   q="When must pupillary reactions be checked, relative to dilation?",
   opts=[
     ["Before dilating", "Correct — pupillary reactions are checked before dilating; the weak mydriatic used for fundoscopy takes 4 to 6 hours to reverse."],
     ["After dilating", "Pupillary reactions come before dilation in the suggested order, not after; a mydriatic's effect lasts 4 to 6 hours."],
     ["It makes no difference", "Timing matters: pupillary reactions are checked before dilating, and the dilation lasts 4 to 6 hours."],
     ["Only after the fundoscopic examination", "Fundoscopy is done after dilation outside primary care, so the pupils are checked before it, not after."]],
   c=0, cite=c(21)),

 dict(topic="Order of examination", io=IO, slot="initial test",
   q="Which examination comes FIRST in the suggested order?",
   opts=[
     ["Inspection", "Correct — the suggested order begins with inspection, then the external examination, before acuity and fields."],
     ["Visual acuity", "Visual acuity follows inspection and the external examination of the cornea, lens and pupils."],
     ["Direct ophthalmoscopy", "Direct ophthalmoscopy comes last, among the special tests with the slit lamp and ocular pressure; inspection comes first."],
     ["Ocular pressure", "Ocular pressure is a special test near the end, done only if it can be measured accurately and safely; inspection comes first."]],
   c=0, cite=c(21)),

 dict(topic="Order of examination", io=IO, slot="avoid",
   q="In a trauma patient, what must NOT be done?",
   opts=[
     ["Do not palpate the globe", "Correct — in trauma it is critical not to palpate the globe, and too much pressure on a ruptured globe is a known mistake."],
     ["Do not measure visual acuity", "Visual acuity is still tested in trauma, following the same pattern as a routine eye examination; the globe is not palpated."],
     ["Do not inspect the lids", "The eyelids are still examined in trauma as part of the routine pattern; what must not be done is palpating the globe."],
     ["Do not take a history", "The history still matters, including tetanus status and any chemical's acidity; what must not be done is palpating the globe."]],
   c=0, cite=c(24)),
]
