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
   q="What does miosis mean, and what is its opposite?",
   opts=[
     ["Pupil constriction; mydriasis is pupil dilatation",
      "Correct — the deck's review pair."],
     ["Pupil dilatation; mydriasis is pupil constriction",
      "This reverses the two terms."],
     ["Inward folding of the lower eyelid; ectropion is the opposite",
      "Those are entropion and ectropion."],
     ["Forward displacement of the globe; enophthalmos is the opposite",
      "That is proptosis."]],
   c=0, cite=c(3)),

 dict(topic="Vocabulary", io=IO, slot="test finding",
   q="What is chemosis?",
   opts=[
     ["Swelling and inflammation of the conjunctiva",
      "Correct — the deck's definition."],
     ["Injection of the superficially visible vessels of the conjunctiva or sclera",
      "That is hyperaemia."],
     ["Forward displacement of the eye in the orbit",
      "That is proptosis."],
     ["Outward turning of the lower eyelid",
      "That is ectropion."]],
   c=0, cite=c(3)),

 dict(topic="Vocabulary", io=IO, slot="test finding",
   q="What is hyperaemia, as the deck defines it?",
   opts=[
     ["Injection of the superficially visible vessels of the conjunctiva, episclera or sclera",
      "Correct — the deck's definition, and it names all three layers."],
     ["Swelling of the conjunctiva",
      "That is chemosis."],
     ["Blood collecting beneath the conjunctiva",
      "That is a subconjunctival haemorrhage."],
     ["Inward folding of the lower lid",
      "That is entropion."]],
   c=0, cite=c(3)),

 dict(topic="Vocabulary", io=IO, slot="differential",
   q="Entropion and ectropion both affect which eyelid, per the deck's review slide?",
   opts=[
     ["The lower lid", "Correct — the deck specifies the lower lid for both."],
     ["The upper lid", "The deck's review slide specifies the lower lid."],
     ["Both lids equally", "The deck names the lower lid."],
     ["Neither — they affect the conjunctiva", "Both are lid malpositions."]],
   c=0, cite=c(3)),

 dict(topic="History", io=IO, slot="initial test",
   q="Which four dimensions does the deck use to assess any eye complaint?",
   opts=[
     ["Time course, precipitating factors, palliative or exacerbating variables, and vision loss or visual deficits",
      "Correct — the deck's four-part frame for the history."],
     ["Onset, duration, severity and radiation",
      "A general pain frame, but not the deck's ocular one."],
     ["Location, quality, quantity and timing",
      "Not the four the deck gives here."],
     ["Fever, discharge, photophobia and itch",
      "Those are findings rather than dimensions of the history."]],
   c=0, cite=c(7)),

 dict(topic="History", io=IO, slot="differential",
   q="Bilateral visual loss usually implies which kind of problem?",
   opts=[
     ["A primary neurologic cause rather than a primary ophthalmologic one",
      "Correct — the speaker notes are explicit about this."],
     ["A primary ophthalmologic cause",
      "The notes say the opposite."],
     ["An infective cause",
      "Not the inference the notes draw."],
     ["A traumatic cause",
      "Not the inference the notes draw."]],
   c=0, cite=cn(10)),

 dict(topic="History", io=IO, slot="differential",
   q="How does the deck read multiple new flashes or floaters against a single floater?",
   opts=[
     ["Multiple new flashes or floaters suggest a retinal tear or vitreous haemorrhage; a single floater is probably benign",
      "Correct — the number is what changes the meaning."],
     ["A single floater suggests a retinal tear; multiple floaters are benign",
      "This reverses the deck's reading."],
     ["Both are always benign",
      "The deck treats multiple new ones as a warning."],
     ["Both always require emergency referral",
      "A single floater is probably benign."]],
   c=0, cite=c(10)),

 dict(topic="History", io=IO, slot="differential",
   q="How does the RATE of onset of visual impairment guide the differential?",
   opts=[
     ["Rapid deterioration suggests a vascular cause; gradual loss suggests something like cataract",
      "Correct — the deck's pairing of tempo with aetiology."],
     ["Rapid deterioration suggests cataract; gradual loss suggests a vascular cause",
      "This reverses the deck's pairing."],
     ["Rate of onset does not narrow the differential",
      "The deck says it gives a clue to aetiology."],
     ["Rapid deterioration always means trauma",
      "The deck names vascular causes."]],
   c=0, cite=c(11)),

 dict(topic="History", io=IO, slot="differential",
   q="Which two symptoms together suggest an allergic cause?",
   opts=[
     ["Itching and excessive tearing", "Correct — the deck pairs these for allergy."],
     ["Deep pain and photophobia", "Deep pain points to acute narrow angle glaucoma."],
     ["Burning and purulent discharge", "Purulent discharge suggests bacterial infection."],
     ["Foreign body sensation and reduced vision", "Those point toward a corneal problem."]],
   c=0, cite=c(12)),

 dict(topic="History", io=IO, slot="differential",
   q="Deep eye pain is associated with which condition in the deck's symptom list?",
   opts=[
     ["Acute narrow angle glaucoma", "Correct — the deck attaches deep pain to this."],
     ["Allergic conjunctivitis", "That itches rather than causing deep pain."],
     ["Corneal abrasion", "That causes surface pain and foreign body sensation."],
     ["Blepharitis", "That causes burning and grittiness."]],
   c=0, cite=c(12)),

 dict(topic="Topical anaesthetic test", io=IO, slot="test finding",
   q="A patient's eye pain is relieved by a topical anaesthetic. What does that suggest, and what does the opposite suggest?",
   opts=[
     ["Relief suggests a surface problem such as a corneal injury; pain NOT relieved suggests a deeper source",
      "Correct — the deck uses the response as a depth test."],
     ["Relief suggests a deep source; no relief suggests a surface problem",
      "This reverses the inference."],
     ["Relief confirms acute glaucoma",
      "Deep pain from glaucoma would not be relieved by a surface anaesthetic."],
     ["The response tells you nothing about depth",
      "The deck uses it precisely to judge depth."]],
   c=0, cite=c(12)),

 dict(topic="History", io=IO, slot="risk factors",
   q="Which four elements of the ocular history does the deck ask for?",
   opts=[
     ["Corrective lenses, acute or chronic eye problems, eye medications, and eye surgery history",
      "Correct — the deck's four, with glaucoma, antiglaucoma drops and cataract removal as its examples."],
     ["Smoking, alcohol, occupation and hobbies",
      "A general social history rather than the deck's ocular one."],
     ["Fever, weight loss, night sweats and rash",
      "Constitutional symptoms, not the ocular history."],
     ["Family history alone",
      "The deck asks for the four above."]],
   c=0, cite=c(13)),

 dict(topic="History", io=IO, slot="risk factors",
   q="Which immunisation status does the deck say matters in eye trauma?",
   opts=[
     ["Tetanus", "Correct — the deck flags tetanus status specifically for eye trauma."],
     ["Influenza", "Not the immunisation the deck raises here."],
     ["Pneumococcal", "Not the immunisation the deck raises."],
     ["Hepatitis B", "Not the immunisation the deck raises."]],
   c=0, cite=c(15)),

 dict(topic="History", io=IO, slot="initial test",
   q="After a chemical or fluid splash to the eye, what does the deck say you must establish?",
   opts=[
     ["The acidity or alkalinity of the fluid",
      "Correct — the deck calls knowing this essential."],
     ["The volume of fluid involved",
      "Not what the deck says is essential."],
     ["Whether the patient was wearing contact lenses",
      "Relevant generally, but not the deck's stated essential here."],
     ["The manufacturer of the product",
      "Not what the deck asks for."]],
   c=0, cite=c(15)),

 dict(topic="History", io=IO, slot="risk factors",
   q="Which three systemic diseases did Beck single out as most relevant, and why the third?",
   opts=[
     ["Diabetes, hypertension and human immunodeficiency virus — because the last will affect basically any aetiology",
      "Correct — her reasoning for including it alongside the two vascular ones."],
     ["Diabetes, hypertension and asthma",
      "Asthma was not one she named."],
     ["Rheumatoid arthritis, lupus and psoriasis",
      "Autoimmune disease matters, but these were not her three."],
     ["Thyroid disease, anaemia and epilepsy",
      "Not the three she named."]],
   c=0, cite=au()),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Acute, unilateral and PAINLESS visual loss suggests which group of causes?",
   opts=[
     ["Retinal vascular occlusion, retinal detachment, vitreous haemorrhage, macular degeneration",
      "Correct — the deck's painless group."],
     ["Corneal abrasion or ulcer, uveitis, traumatic hyphaema, acute narrow angle glaucoma",
      "Those make up the acute unilateral PAINFUL group."],
     ["Thermal, radiation or chemical exposure",
      "That is the acute BILATERAL painful group."],
     ["Simple glaucoma or cataract",
      "That is the gradual painless group."]],
   c=0, cite=c(16)),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Acute, unilateral and PAINFUL visual loss localises to where, and includes which causes?",
   opts=[
     ["Usually the cornea and anterior chamber — corneal abrasion or ulcer, uveitis, traumatic hyphaema, acute narrow angle glaucoma",
      "Correct — the deck gives both the location and the list."],
     ["Usually the retina — vascular occlusion and detachment",
      "Those are painless."],
     ["Usually the optic nerve — optic neuritis alone",
      "Not the deck's grouping."],
     ["Usually the lids — blepharitis and hordeolum",
      "Those do not cause acute visual loss."]],
   c=0, cite=c(16)),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Acute, BILATERAL and painful symptoms should make you consider what?",
   opts=[
     ["Thermal, radiation or chemical exposure",
      "Correct — bilateral and painful points to an environmental exposure."],
     ["Retinal vascular occlusion",
      "That is acute, unilateral and painless."],
     ["Simple glaucoma or cataract",
      "Those are gradual and painless."],
     ["Traumatic hyphaema",
      "That is unilateral."]],
   c=0, cite=c(16)),

 dict(topic="Symptom patterns", io=IO, slot="differential",
   q="Gradual, painless visual loss suggests what?",
   opts=[
     ["Simple glaucoma or cataract", "Correct — the deck's gradual painless pair."],
     ["Acute narrow angle glaucoma", "That is acute and painful."],
     ["Vitreous haemorrhage", "That is acute."],
     ["Chemical exposure", "That is acute and bilateral."]],
   c=0, cite=c(16)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain WITH BLINKING suggests what?",
   opts=[
     ["Corneal abrasion or a foreign body", "Correct — the lid moving over the defect is what hurts."],
     ["Acute narrow angle glaucoma", "That gives headache with eye pain."],
     ["Optic neuritis", "That gives pain on eye MOTION, not on blinking."],
     ["Temporal arteritis", "That gives temporal pain."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain with a GRITTY feeling suggests what?",
   opts=[
     ["Conjunctivitis", "Correct — the deck attaches grittiness to conjunctivitis."],
     ["Inflammation of the iris", "That is signalled by photophobia."],
     ["Acute narrow angle glaucoma", "That comes with headache."],
     ["Optic neuritis", "That comes with pain on eye movement."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain with PHOTOPHOBIA suggests what?",
   opts=[
     ["Inflammation of the iris", "Correct — the deck's pairing for photophobia."],
     ["Corneal abrasion", "That is signalled by pain with blinking."],
     ["Temporal arteritis", "That gives temporal pain."],
     ["Conjunctivitis", "That gives a gritty feeling."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain ON EYE MOTION suggests what?",
   opts=[
     ["Optic neuritis", "Correct — the deck's pairing for pain on movement."],
     ["Corneal abrasion", "That hurts on blinking."],
     ["Conjunctivitis", "That gives grittiness."],
     ["Acute narrow angle glaucoma", "That gives headache with eye pain."]],
   c=0, cite=c(17)),

 dict(topic="Eye pain qualifiers", io=IO, slot="differential",
   q="Eye pain WITH HEADACHE suggests what?",
   opts=[
     ["Acute narrow angle glaucoma", "Correct — the deck's pairing for headache plus eye pain."],
     ["Temporal arteritis", "That is paired with temporal pain specifically."],
     ["Optic neuritis", "That is paired with pain on eye motion."],
     ["Conjunctivitis", "That is paired with grittiness."]],
   c=0, cite=c(17)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="HORIZONTAL diplopia — images side by side — points to a palsy of which cranial nerves?",
   opts=[
     ["Third or sixth", "Correct — and Beck called this slide very important to commit to memory."],
     ["Third or fourth", "That is the VERTICAL pattern."],
     ["Fourth or sixth", "The third nerve features in both patterns."],
     ["Second or seventh", "Neither is an extraocular motor nerve."]],
   c=0, cite=c(18)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="VERTICAL diplopia — images on top of each other — points to a palsy of which cranial nerves?",
   opts=[
     ["Third or fourth", "Correct — and Beck flagged this slide as one to memorise."],
     ["Third or sixth", "That is the HORIZONTAL pattern."],
     ["Fourth or sixth", "The third nerve features in both patterns."],
     ["Second or third", "The second nerve is sensory, not motor."]],
   c=0, cite=c(18)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="Which cranial nerve appears in BOTH the horizontal and vertical diplopia patterns?",
   opts=[
     ["The third", "Correct — Beck's shortcut was 'three for both of those'."],
     ["The fourth", "That appears in the vertical pattern only."],
     ["The sixth", "That appears in the horizontal pattern only."],
     ["The second", "That is the optic nerve and carries no motor fibres to the eye muscles."]],
   c=0, cite=au()),

 dict(topic="Diplopia", io=IO, slot="etiology",
   q="Besides faulty alignment, what does the deck give as a cause of diplopia?",
   opts=[
     ["A neurological problem — lesions in the brainstem or cerebellum, or weakness or paralysis of one or more extraocular muscles",
      "Correct — the deck's neurological grouping."],
     ["Refractive error alone",
      "Refractive error blurs rather than doubles."],
     ["Dry eye",
      "That causes irritation and blurring."],
     ["Cataract",
      "The deck lists monocular diplopia with cataract elsewhere, not as this cause."]],
   c=0, cite=c(18)),

 dict(topic="Diplopia", io=IO, slot="test finding",
   q="Which compensatory finding does the deck associate with diplopia?",
   opts=[
     ["A compensatory head posture", "Correct — patients tilt or turn to fuse the images."],
     ["A compensatory squint of one eye only", "Not the finding the deck names."],
     ["Compensatory pupil dilation", "Not a compensation for diplopia."],
     ["Compensatory tearing", "Not what the deck describes."]],
   c=0, cite=c(18)),

 dict(topic="Tearing and dryness", io=IO, slot="differential",
   q="Which two causes does the deck give for excessive tearing or dryness?",
   opts=[
     ["Obstruction in the lacrimal apparatus, and Sjögren syndrome",
      "Correct — a mechanical cause and an immune one."],
     ["Conjunctivitis and blepharitis",
      "Both cause irritation but are not the deck's two here."],
     ["Cataract and glaucoma",
      "Neither is a cause of tearing in the deck."],
     ["Corneal abrasion and foreign body",
      "Those cause reflex tearing but are not the deck's pair."]],
   c=0, cite=c(18)),

 dict(topic="Discharge", io=IO, slot="differential",
   q="Watery or mucoid discharge suggests which conditions?",
   opts=[
     ["Allergic or viral", "Correct — the deck's pairing for watery and mucoid discharge."],
     ["Bacterial infection", "That produces purulent discharge."],
     ["Fungal infection", "Not a category the deck sorts by discharge."],
     ["Traumatic", "Not sorted by discharge in the deck."]],
   c=0, cite=c(19)),

 dict(topic="Discharge", io=IO, slot="differential",
   q="Purulent discharge suggests what?",
   opts=[
     ["Bacterial infection", "Correct — the deck's pairing for purulent discharge."],
     ["Allergic conjunctivitis", "That produces watery or mucoid discharge."],
     ["Viral conjunctivitis", "That also produces watery or mucoid discharge."],
     ["Dry eye", "That produces no discharge."]],
   c=0, cite=c(19)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="Which failure does the deck list that would make an infectious red eye worse?",
   opts=[
     ["Failing to recognise an infectious cause and inappropriately prescribing topical corticosteroid drops",
      "Correct — the deck names this among its common mistakes."],
     ["Failing to measure the intraocular pressure",
      "A mistake, but not the one that worsens an infection."],
     ["Failing to dilate the pupil",
      "Not the mistake the deck flags here."],
     ["Failing to document the family history",
      "Not among the deck's listed failures."]],
   c=0, cite=c(20)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="Which two structures does the deck warn are commonly not examined?",
   opts=[
     ["The cornea and the lens", "Correct — 'failure to examine the cornea and lens' is on the list."],
     ["The eyelids and eyebrows", "Not among the deck's named omissions."],
     ["The lacrimal sac and puncta", "Not among the deck's named omissions."],
     ["The extraocular muscles", "Movement testing is listed separately."]],
   c=0, cite=c(20)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="Which pair of diagnoses does the deck say must be differentiated because the latter can lead to death?",
   opts=[
     ["Preseptal from orbital cellulitis",
      "Correct — the deck gives exactly this reason."],
     ["Episcleritis from scleritis",
      "A real distinction, but not the one the deck ties to death."],
     ["Cataract from glaucoma",
      "Not the pair the deck flags."],
     ["Hordeolum from chalazion",
      "Not the pair the deck flags."]],
   c=0, cite=c(20)),

 dict(topic="Common mistakes", io=IO, slot="avoid",
   q="What does the deck warn about pressure on a globe that may be ruptured?",
   opts=[
     ["Failing to diagnose a penetrated or ruptured globe, and placing too much pressure on it, is a listed mistake",
      "Correct — the deck names both the missed diagnosis and the pressure."],
     ["Pressure is required to assess the depth of injury",
      "The deck warns against pressure."],
     ["Pressure is harmless once an anaesthetic is instilled",
      "Anaesthesia does not make pressure safe."],
     ["Pressure should be applied only with a cotton bud",
      "The deck says not to apply pressure at all."]],
   c=0, cite=c(20)),

 dict(topic="Order of examination", io=IO, slot="initial test",
   q="What does the deck call the vital sign of the eye?",
   opts=[
     ["Visual acuity", "Correct — the deck labels acuity testing the vital sign of the eye."],
     ["Intraocular pressure", "Analogous to blood pressure in the deck, but not called the vital sign."],
     ["Pupil reactivity", "An important test, but not the deck's phrase."],
     ["Visual fields", "Not the deck's phrase."]],
   c=0, cite=c(21)),

 dict(topic="Order of examination", io=IO, slot="initial test",
   q="When must pupillary reactions be checked, relative to dilation?",
   opts=[
     ["Before dilating", "Correct — the deck notes this explicitly in the suggested order."],
     ["After dilating", "Dilation abolishes the reaction being tested."],
     ["It makes no difference", "It makes all the difference."],
     ["Only after the fundoscopic examination", "Fundoscopy usually follows dilation."]],
   c=0, cite=c(21)),

 dict(topic="Order of examination", io=IO, slot="initial test",
   q="Which examination does the deck place FIRST in the suggested order?",
   opts=[
     ["Inspection", "Correct — the deck's order begins with inspection."],
     ["Visual acuity", "That comes after inspection and external examination."],
     ["Direct ophthalmoscopy", "That comes near the end."],
     ["Ocular pressure", "That comes among the special tests."]],
   c=0, cite=c(21)),

 dict(topic="Order of examination", io=IO, slot="avoid",
   q="In a trauma patient, what does the deck say must NOT be done?",
   opts=[
     ["Do not palpate the globe", "Correct — the deck calls this critical in trauma."],
     ["Do not measure visual acuity", "Acuity is still required."],
     ["Do not inspect the lids", "Inspection is still required."],
     ["Do not take a history", "The history is still required."]],
   c=0, cite=c(24)),
]
