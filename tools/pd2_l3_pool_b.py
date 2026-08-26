# -*- coding: utf-8 -*-
# PD2 Lecture 3 -- pool B: inspection, the lids and conjunctiva, and the
# red-eye comparison chart Beck singled out.
#
# THE RED-EYE CHART (slide 48) IS THE HIGH-YIELD SLIDE OF THIS DECK. It extracts
# as completely blank text -- it is a picture of the Bates table -- and was
# recovered with tools/ocr_deck_images.py. Beck then said of it: "I genuinely
# think it's important that you are very familiar with that chart ... it helps
# you compare and contrast the common important eye conditions." Its questions
# cite it as image-only.
#
# THE EXOPHTHALMOMETER IS OUT OF SCOPE. "I am not going to test you on the
# minutia of how to do that test ... don't worry about it." Recognising
# exophthalmos, and the stand-behind-and-look-down technique, ARE in.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "PD II Advanced Exam Ocular Lecture - Beck.pptx"
def c(n): return f"{SRC}, Slide {n}"
def ci(n): return f"{SRC}, Slide {n} (image only)"
def au(): return "Lecture recording, 26 August 2026"

IO = "Instructional Objectives — Advanced Ocular Medical History and Examination"

POOL_B = [
 dict(topic="Proptosis", io=IO, slot="initial test",
   q="How does the deck say to assess whether the eyes are truly protruding?",
   opts=[
     ["Stand behind the seated patient and inspect from above, drawing the lid slightly upward to compare the corneas against the lower lids",
      "Correct — the technique Beck demonstrated and kept in scope."],
     ["Sit facing the patient and compare the two eyes directly",
      "The deck specifically asks you to look down from above."],
     ["Measure the distance from the lateral orbital angle with a ruler",
      "That is the exophthalmometer measurement, which Beck said she would not test."],
     ["Palpate the globe to judge its forward position",
      "Palpating the globe is contraindicated in trauma and is not the technique here."]],
   c=0, cite=c(25)),

 dict(topic="Proptosis", io=IO, slot="etiology",
   q="Which conditions does the deck list as causes of proptosis or exophthalmos?",
   opts=[
     ["Retrobulbar haemorrhage, orbital cellulitis, orbital tumour, and Graves disease",
      "Correct — the deck's four orbital causes."],
     ["Cataract, glaucoma and macular degeneration",
      "None of these displaces the globe forward."],
     ["Blepharitis, chalazion and hordeolum",
      "Those are lid conditions."],
     ["Conjunctivitis and episcleritis",
      "Neither displaces the globe."]],
   c=0, cite=c(24)),

 dict(topic="Eyebrows", io=IO, slot="test finding",
   q="Lateral sparseness of the eyebrows suggests what?",
   opts=[
     ["Hypothyroidism", "Correct — the deck's association for lateral eyebrow loss."],
     ["Hyperthyroidism", "The deck associates lid lag with hyperthyroidism, not eyebrow loss."],
     ["Seborrhoeic dermatitis", "That causes scaliness of the eyebrows."],
     ["Iron deficiency", "Not an association the deck gives."]],
   c=0, cite=c(27)),

 dict(topic="Eyebrows", io=IO, slot="test finding",
   q="Scaliness of the eyebrows suggests what?",
   opts=[
     ["Seborrhoeic dermatitis", "Correct — the deck's association for eyebrow scaling."],
     ["Hypothyroidism", "That causes lateral sparseness instead."],
     ["Contact dermatitis", "Not the deck's named association."],
     ["Psoriasis", "Not the deck's named association here."]],
   c=0, cite=c(27)),

 dict(topic="Ptosis", io=IO, slot="etiology",
   q="Which three causes of ptosis does the deck name, besides senile and congenital forms?",
   opts=[
     ["Myasthenia gravis, oculomotor nerve damage, and damage to the sympathetic supply (Horner syndrome)",
      "Correct — the deck's three, spanning neuromuscular junction, motor nerve and sympathetic chain."],
     ["Bell palsy, trigeminal neuralgia and stroke",
      "Bell palsy weakens lid CLOSURE, not elevation."],
     ["Thyroid eye disease, orbital cellulitis and tumour",
      "Those cause proptosis in this deck."],
     ["Blepharitis, chalazion and dermatochalasis",
      "Those are lid conditions but not the deck's ptosis causes."]],
   c=0, cite=c(29)),

 dict(topic="Ptosis", io=IO, slot="etiology",
   q="What does the deck say causes SENILE ptosis?",
   opts=[
     ["Weakened muscle, relaxed tissues, and the weight of herniated fat",
      "Correct — the deck's three-part mechanical explanation."],
     ["Antibody blockade at the neuromuscular junction",
      "That is myasthenia gravis."],
     ["Interruption of the sympathetic supply",
      "That is Horner syndrome."],
     ["Compression of the oculomotor nerve",
      "That is a third nerve palsy."]],
   c=0, cite=c(29)),

 dict(topic="Hordeolum and chalazion", io=IO, slot="differential",
   q="What separates a hordeolum from a chalazion on the deck's inspection slide?",
   opts=[
     ["The hordeolum is painful and sits AT THE LID'S EDGE; the chalazion is a chronic, non-painful meibomian lesion that generally is not at the margin",
      "Correct — the deck gives both the pain and the position."],
     ["The hordeolum is chronic and painless; the chalazion is acute and painful",
      "This reverses both."],
     ["The hordeolum affects the upper lid only; the chalazion the lower",
      "Neither is restricted by lid."],
     ["The hordeolum is bilateral; the chalazion unilateral",
      "Laterality does not separate them."]],
   c=0, cite=c(30)),

 dict(topic="Chalazion", io=IO, slot="test finding",
   q="Where does a chalazion usually point?",
   opts=[
     ["Inside the lid rather than on the lid margin",
      "Correct — the deck notes this as a distinguishing feature."],
     ["On the lid margin at the lash line",
      "That is the external hordeolum."],
     ["At the medial canthus",
      "That location suggests lacrimal sac disease."],
     ["At the lateral canthus",
      "Not where the deck places it."]],
   c=0, cite=c(33)),

 dict(topic="Blepharitis", io=IO, slot="etiology",
   q="Which two associations does the deck give for blepharitis?",
   opts=[
     ["Bacterial infection and atopic dermatitis",
      "Correct — the deck's two on this slide."],
     ["Hypothyroidism and iron deficiency",
      "Neither is given for blepharitis."],
     ["Graves disease and myasthenia gravis",
      "Those relate to lid lag and ptosis."],
     ["Rheumatoid arthritis and lupus",
      "Those are given for nodular episcleritis."]],
   c=0, cite=c(31)),

 dict(topic="Xanthelasma", io=IO, slot="test finding",
   q="Where do xanthelasma plaques sit, and what should they prompt?",
   opts=[
     ["Along the NASAL portions of one or both eyelids — consider lipid disorders",
      "Correct — the deck gives both the position and the inference."],
     ["Along the temporal portions of the lids — consider thyroid disease",
      "The deck specifies the nasal portion and lipid disorders."],
     ["At the lid margin — consider bacterial infection",
      "That describes a hordeolum."],
     ["On the bulbar conjunctiva — consider ultraviolet exposure",
      "That describes pinguecula."]],
   c=0, cite=c(34)),

 dict(topic="Lid position", io=IO, slot="differential",
   q="What is trichiasis?",
   opts=[
     ["Posteriorly misdirected eyelashes", "Correct — the deck's definition, listed alongside entropion and ectropion."],
     ["Inward turning of the lower lid margin", "That is entropion."],
     ["Outward turning of the lower lid margin", "That is ectropion."],
     ["Drooping of the upper lid", "That is ptosis."]],
   c=0, cite=c(35)),

 dict(topic="Nasolacrimal duct", io=IO, slot="initial test",
   q="How is the nasolacrimal duct obstruction test performed, and what is a positive result?",
   opts=[
     ["Ask the patient to look up, press on the lower lid near the medial canthus just inside the bony orbit to compress the lacrimal sac, and look for fluid regurgitating from the puncta — mucopurulent fluid suggests obstruction",
      "Correct — the deck's full technique and its positive finding."],
     ["Instil fluorescein and time its disappearance from the tear film",
      "A real test, but not the one the deck describes here."],
     ["Press on the upper lid near the lateral canthus and look for tearing",
      "Wrong lid and wrong canthus — the sac is medial and inferior."],
     ["Evert the upper lid and inspect the tarsal conjunctiva",
      "That is the foreign body search."]],
   c=0, cite=c(38)),

 dict(topic="Nasolacrimal duct", io=IO, slot="avoid",
   q="When should the lacrimal sac compression test be avoided?",
   opts=[
     ["If the area is significantly inflamed or tender",
      "Correct — the deck says to avoid it in that situation."],
     ["If the patient wears contact lenses",
      "Not a contraindication the deck gives."],
     ["If the patient has had cataract surgery",
      "Not a contraindication the deck gives."],
     ["If the patient is over sixty-five",
      "Age is not a contraindication."]],
   c=0, cite=c(38)),

 dict(topic="Upper lid eversion", io=IO, slot="initial test",
   q="What is the correct technique for everting the upper lid to search for a foreign body?",
   opts=[
     ["Ask the patient to look down and relax, raise the lid slightly so the lashes protrude, grasp the lashes and pull down and forward, then place a stick at least 1 cm above the lid margin at the upper border of the tarsal plate and push down as you raise the lid edge",
      "Correct — the deck's step-by-step, including the 1 cm landmark."],
     ["Ask the patient to look up, then pull the lid upward directly",
      "Looking up defeats the eversion; the deck asks for downgaze."],
     ["Press on the globe itself to push the lid outward",
      "The deck says explicitly not to press on the eyeball."],
     ["Use a cotton bud placed at the lid margin itself",
      "The deck places the stick at least 1 cm above the margin."]],
   c=0, cite=c(42)),

 dict(topic="Upper lid eversion", io=IO, slot="avoid",
   q="When must the lid never be everted?",
   opts=[
     ["If rupture of the globe is suspected", "Correct — the deck states this as an absolute."],
     ["If the patient has conjunctivitis", "Not a contraindication."],
     ["If the patient wears contact lenses", "Not a contraindication."],
     ["If a foreign body has already been seen", "That is a reason TO evert, not to avoid it."]],
   c=0, cite=c(42)),

 dict(topic="Sclera colour", io=IO, slot="test finding",
   q="A YELLOW sclera indicates what?",
   opts=[
     ["Liver disease", "Correct — jaundice, as the deck states."],
     ["Osteogenesis imperfecta", "That gives a BLUE sclera."],
     ["Chronic ultraviolet exposure", "That gives pinguecula or pterygium."],
     ["Anaemia", "The deck does not attach scleral colour to anaemia."]],
   c=0, cite=c(43)),

 dict(topic="Sclera colour", io=IO, slot="test finding",
   q="A BLUE sclera indicates what?",
   opts=[
     ["Osteogenesis imperfecta", "Correct — the deck's association for blue sclerae."],
     ["Liver disease", "That gives a yellow sclera."],
     ["Thyroid eye disease", "Not associated with scleral colour here."],
     ["Long-term steroid use", "Not an association the deck gives."]],
   c=0, cite=c(43)),

 dict(topic="Subconjunctival haemorrhage", io=IO, slot="test finding",
   q="Which findings characterise a subconjunctival haemorrhage on examination?",
   opts=[
     ["Pain absent, vision and pupil unaffected, no discharge, cornea clear",
      "Correct — the deck's four negatives, which are what make it benign."],
     ["Pain present with photophobia and a hazy cornea",
      "Those suggest corneal or intraocular disease."],
     ["Purulent discharge with lid crusting",
      "That suggests bacterial conjunctivitis."],
     ["An irregular pupil with ciliary flush",
      "Those suggest anterior uveitis."]],
   c=0, cite=c(44)),

 dict(topic="Subconjunctival haemorrhage", io=IO, slot="escalation",
   q="When is globe rupture more likely in a patient with a subconjunctival haemorrhage?",
   opts=[
     ["In trauma, and when the haemorrhage encircles the entire cornea",
      "Correct — the deck names both the mechanism and the 360-degree pattern."],
     ["When the haemorrhage is small and sectoral",
      "That is the ordinary benign pattern."],
     ["When the patient is anticoagulated",
      "That explains the bleed but does not indicate rupture."],
     ["When both eyes are affected",
      "Bilaterality is not the deck's warning sign."]],
   c=0, cite=c(44)),

 dict(topic="Conjunctivitis", io=IO, slot="test finding",
   q="What is the pattern of redness in conjunctivitis, and where is it maximal?",
   opts=[
     ["Diffuse dilation of the conjunctival vessels, with redness maximal PERIPHERALLY",
      "Correct — peripheral maximum is what separates it from a ciliary pattern."],
     ["Redness maximal around the cornea, sparing the periphery",
      "That is the ciliary pattern of keratitis, iritis or acute glaucoma."],
     ["A single sharply demarcated red patch",
      "That is a subconjunctival haemorrhage."],
     ["A violaceous discolouration of the sclera",
      "That is scleritis."]],
   c=0, cite=c(45)),

 dict(topic="Conjunctivitis", io=IO, slot="test finding",
   q="What does the deck say about vision and the pupil in conjunctivitis?",
   opts=[
     ["Vision is not affected except for mild blurring from discharge, and the pupil is not affected",
      "Correct — preserved vision and a normal pupil are what make it benign."],
     ["Vision is usually decreased and the pupil is irregular",
      "Those findings point to corneal or intraocular disease."],
     ["Vision is normal but the pupil is fixed and mid-dilated",
      "That is acute angle closure."],
     ["Vision is decreased and the cornea is steamy",
      "That is acute glaucoma."]],
   c=0, cite=c(45)),

 dict(topic="Injection pattern", io=IO, slot="differential",
   q="Injection localised JUST AROUND THE CORNEA suggests which three conditions?",
   opts=[
     ["Keratitis, iritis, or acute glaucoma",
      "Correct — the deck's three, and this is the pattern that must not be dismissed as conjunctivitis."],
     ["Conjunctivitis, blepharitis, or dry eye",
      "Those give diffuse or lid-margin redness."],
     ["Subconjunctival haemorrhage, pinguecula, or pterygium",
      "Those are localised surface lesions."],
     ["Episcleritis, chalazion, or hordeolum",
      "Those do not produce a circumcorneal ring."]],
   c=0, cite=c(46)),

 dict(topic="Nodular episcleritis", io=IO, slot="etiology",
   q="Nodular episcleritis is associated with which two systemic diseases in this deck?",
   opts=[
     ["Rheumatoid arthritis and lupus erythematosus",
      "Correct — the deck's two associations."],
     ["Diabetes and hypertension",
      "Those drive retinopathy in this deck."],
     ["Graves disease and myasthenia gravis",
      "Those relate to lid signs."],
     ["Sjögren syndrome and sarcoidosis",
      "Sjögren appears under dry eye, not here."]],
   c=0, cite=c(47)),

 # ---- the red-eye chart, slide 48 ----
 dict(topic="Red eye chart", io=IO, slot="differential", chart=True,
   q="On the deck's red-eye comparison chart, which condition shows redness that is DIFFUSE and maximal peripherally, with vision unaffected?",
   opts=[
     ["Conjunctivitis", "Correct — diffuse peripheral redness with preserved vision is the conjunctivitis column."],
     ["Acute iritis", "That shows ciliary injection with decreased vision."],
     ["Glaucoma", "That shows diffuse redness with a steamy cornea and a dilated fixed pupil."],
     ["Corneal injury or infection", "That shows ciliary injection with usually decreased vision."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="On the red-eye chart, what is the CORNEA like in glaucoma?",
   opts=[
     ["Steamy and cloudy", "Correct — the chart's glaucoma column."],
     ["Clear", "That is conjunctivitis and subconjunctival haemorrhage."],
     ["Clear or slightly clouded", "That is acute iritis."],
     ["Changes depending on the cause", "That is corneal injury or infection."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="On the red-eye chart, what is the PUPIL like in glaucoma?",
   opts=[
     ["Dilated and fixed", "Correct — the chart's glaucoma column, and a cardinal danger sign."],
     ["Not affected", "That is conjunctivitis and subconjunctival haemorrhage."],
     ["May be small and, with time, irregular", "That is acute iritis."],
     ["Not affected unless iritis develops", "That is corneal injury or infection."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="On the red-eye chart, how is the PAIN of acute iritis described?",
   opts=[
     ["Moderate, aching, deep", "Correct — the chart's iritis column."],
     ["Mild discomfort rather than pain", "That is conjunctivitis."],
     ["Severe, aching, deep", "That is glaucoma."],
     ["Absent", "That is subconjunctival haemorrhage."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="On the red-eye chart, which column has NO ocular discharge AND an unaffected pupil AND a clear cornea AND absent pain?",
   opts=[
     ["Subconjunctival haemorrhage", "Correct — every column reads negative, which is what makes it benign."],
     ["Conjunctivitis", "That has watery, mucoid or mucopurulent discharge and mild discomfort."],
     ["Acute iritis", "That has aching pain and a small or irregular pupil."],
     ["Glaucoma", "That has severe pain, a cloudy cornea and a fixed pupil."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="differential", chart=True,
   q="The chart describes CILIARY INJECTION as an important sign of three conditions. What is it, and why does it matter?",
   opts=[
     ["Dilation of deeper vessels visible as radiating vessels or a reddish-violet flush around the limbus — it is important because those three conditions can threaten sight",
      "Correct — the chart's own wording and reasoning."],
     ["Dilation of the superficial conjunctival vessels maximal at the periphery",
      "That is the conjunctival pattern, not the ciliary one."],
     ["A sharply demarcated homogeneous red patch",
      "That is subconjunctival haemorrhage."],
     ["A violaceous hue from scleral thinning",
      "That is scleritis, which is not on this chart."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="The chart warns that the eye in a ciliary-injection condition may be diffusely red instead. Which other clues does it give to catch those conditions?",
   opts=[
     ["Pain, decreased vision, unequal pupils, and a less than perfectly clear cornea",
      "Correct — the chart's four backup clues when the injection pattern is unhelpful."],
     ["Itch, watery discharge and lid crusting",
      "Those point toward benign conjunctivitis."],
     ["Bilateral involvement and a preauricular node",
      "Those point toward viral conjunctivitis."],
     ["Fever and periorbital swelling",
      "Those suggest cellulitis, which is not on this chart."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="prognosis", chart=True,
   q="On the red-eye chart, what does it give as the significance of the glaucoma column?",
   opts=[
     ["An acute increase in intraocular pressure — an emergency",
      "Correct — the chart labels it an emergency outright."],
     ["Bacterial, viral and other infections, or allergy and irritation",
      "That is the conjunctivitis column."],
     ["Abrasions and other injuries; viral and bacterial infections",
      "That is the corneal injury column."],
     ["Often none; may result from trauma, bleeding disorders, or a sudden increase in venous pressure",
      "That is subconjunctival haemorrhage."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="education", chart=True,
   q="Beck singled this chart out. What did she say about it?",
   opts=[
     ["That she genuinely thinks students should be very familiar with it, because it helps compare and contrast the common important eye conditions",
      "Correct — one of her clearest emphases in the lecture."],
     ["That it is optional background and would not be tested",
      "She said the opposite."],
     ["That it duplicates PD1 and so is out of scope",
      "That is what she said about the corneal reflection test, not this chart."],
     ["That only the glaucoma column matters",
      "She recommended familiarity with the whole chart."]],
   c=0, cite=au()),
]
