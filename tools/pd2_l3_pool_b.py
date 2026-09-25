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
   q="How do you assess whether the eyes are truly protruding?",
   opts=[
     ["Stand behind the seated patient and inspect from above",
      "Correct — stand behind the seated patient, look down from above, and draw the lids up to compare the corneas with the lower lids."],
     ["Sit facing the patient and compare the two eyes directly",
      "Prominent eyes are judged from behind and above the seated patient, comparing the corneas with the lower lids."],
     ["Shine a light from the temporal side and look for a shadow",
      "Oblique light from the temporal side looks for the iris shadow of a narrow angle; protrusion is judged from behind and above."],
     ["Palpate the globe to judge its forward position",
      "The globe is not palpated, and it is critical not to in trauma; protrusion is judged by inspecting from behind and above."]],
   c=0, cite=c(25)),

 dict(topic="Proptosis", io=IO, slot="etiology",
   q="Which conditions cause proptosis or exophthalmos?",
   opts=[
     ["Retrobulbar hemorrhage, orbital cellulitis, orbital tumor, and Graves disease",
      "Correct — proptosis signals orbital disease: retrobulbar hemorrhage, orbital cellulitis, orbital tumor or Graves disease."],
     ["Cataract, glaucoma and macular degeneration",
      "Those cause visual loss from within the eye; forward displacement signals orbital disease such as Graves disease or a tumor."],
     ["Blepharitis, chalazion and hordeolum",
      "Those are eyelid lesions; forward displacement of the eye signals orbital disease such as orbital cellulitis or a tumor."],
     ["Conjunctivitis and episcleritis",
      "Those inflame the surface of the eye; proptosis signals orbital disease such as retrobulbar hemorrhage or Graves disease."]],
   c=0, cite=c(24)),

 dict(topic="Eyebrows", io=IO, slot="test finding",
   q="Lateral sparseness of the eyebrows suggests what?",
   opts=[
     ["Hypothyroidism", "Correct — lateral sparseness of the eyebrows is the eyebrow finding associated with hypothyroidism."],
     ["Hyperthyroidism", "Hyperthyroidism is linked to lid lag, not eyebrow loss; lateral eyebrow sparseness suggests hypothyroidism."],
     ["Seborrheic dermatitis", "Seborrheic dermatitis causes scaliness of the eyebrows; lateral sparseness suggests hypothyroidism."],
     ["Iron deficiency", "Iron deficiency is not an eyebrow association; lateral sparseness of the eyebrows suggests hypothyroidism."]],
   c=0, cite=c(27)),

 dict(topic="Eyebrows", io=IO, slot="test finding",
   q="Scaliness of the eyebrows suggests what?",
   opts=[
     ["Seborrheic dermatitis", "Correct — scaliness of the eyebrows is the eyebrow finding associated with seborrheic dermatitis."],
     ["Hypothyroidism", "Hypothyroidism causes lateral sparseness of the eyebrows; scaliness suggests seborrheic dermatitis."],
     ["Contact dermatitis", "Contact dermatitis is not the eyebrow association; scaliness of the eyebrows suggests seborrheic dermatitis."],
     ["Psoriasis", "Psoriasis is not the eyebrow association; scaliness of the eyebrows suggests seborrheic dermatitis."]],
   c=0, cite=c(27)),

 dict(topic="Ptosis", io=IO, slot="etiology",
   q="Besides Horner syndrome and the senile and congenital forms, which causes of ptosis remain?",
   opts=[
     ["Myasthenia gravis, oculomotor nerve damage",
      "Correct — ptosis also comes from myasthenia gravis and oculomotor nerve damage, alongside Horner syndrome's sympathetic loss."],
     ["Bell palsy, trigeminal neuralgia and stroke",
      "None of these is a ptosis cause; drooping of the upper lid comes from myasthenia gravis or oculomotor nerve damage."],
     ["Thyroid eye disease, orbital cellulitis and tumor",
      "Orbital disease such as cellulitis or tumor causes proptosis, not ptosis; ptosis comes from myasthenia gravis or third nerve damage."],
     ["Blepharitis, chalazion and dermatochalasis",
      "Lid lesions such as a chalazion are not ptosis causes; the remaining causes are myasthenia gravis and oculomotor nerve damage."]],
   c=0, cite=c(29)),

 dict(topic="Ptosis", io=IO, slot="etiology",
   q="What causes SENILE ptosis?",
   opts=[
     ["Weakened muscle, relaxed tissues",
      "Correct — senile ptosis comes from weakened muscle and relaxed tissues, plus the weight of herniated fat."],
     ["Antibody blockade at the neuromuscular junction",
      "Myasthenia gravis is a separate cause of ptosis; senile ptosis comes from weakened muscle, relaxed tissues and herniated fat."],
     ["Interruption of the sympathetic supply",
      "Sympathetic interruption causes Horner syndrome's ptosis; senile ptosis comes from weakened muscle, relaxed tissues and herniated fat."],
     ["Compression of the oculomotor nerve",
      "Oculomotor damage is a separate ptosis cause; senile ptosis comes from weakened muscle, relaxed tissues and herniated fat."]],
   c=0, cite=c(29)),

 dict(topic="Hordeolum and chalazion", io=IO, slot="differential",
   q="What separates a hordeolum from a chalazion on inspection?",
   opts=[
     ["The hordeolum is painful and sits AT THE LID'S EDGE",
      "Correct — the hordeolum is a painful infection at the lid's edge, while the chalazion is a chronic painless lesion that generally is not."],
     ["The hordeolum is chronic and painless; the chalazion is acute and painful",
      "This reverses them: the hordeolum is the painful one at the lid margin, and the chalazion is the chronic, nonpainful one."],
     ["The hordeolum affects the upper lid only; the chalazion the lower",
      "Lid choice does not separate them; the hordeolum is painful and at the lid's edge, the chalazion painless and not at the edge."],
     ["The hordeolum is bilateral; the chalazion unilateral",
      "Laterality does not separate them; the hordeolum is painful and at the lid's edge, the chalazion painless and not at the edge."]],
   c=0, cite=c(30)),

 dict(topic="Chalazion", io=IO, slot="test finding",
   q="Where does a chalazion usually point?",
   opts=[
     ["Inside the lid rather than on the lid margin",
      "Correct — a chalazion, a nodule of a blocked meibomian gland, usually points inside the lid rather than on the lid margin."],
     ["On the lid margin at the lash line",
      "The lid margin is where a hordeolum sits; a chalazion usually points inside the lid rather than on the margin."],
     ["At the medial canthus",
      "The medial canthus is where the lacrimal sac is compressed; a chalazion usually points inside the lid, not at a canthus."],
     ["At the lateral canthus",
      "A chalazion does not point to the lateral canthus; it usually points inside the lid rather than on the lid margin."]],
   c=0, cite=c(33)),

 dict(topic="Blepharitis", io=IO, slot="etiology",
   q="Which two conditions are associated with blepharitis?",
   opts=[
     ["Bacterial infection and atopic dermatitis",
      "Correct — blepharitis is a common eye inflammation associated with bacterial infections and with atopic dermatitis."],
     ["Hypothyroidism and iron deficiency",
      "Hypothyroidism shows as lateral eyebrow sparseness; blepharitis is associated with bacterial infection and atopic dermatitis."],
     ["Graves disease and myasthenia gravis",
      "Graves disease causes proptosis and myasthenia gravis causes ptosis; blepharitis goes with bacteria and atopic dermatitis."],
     ["Rheumatoid arthritis and lupus",
      "Rheumatoid arthritis and lupus go with nodular episcleritis; blepharitis goes with bacterial infection and atopic dermatitis."]],
   c=0, cite=c(31)),

 dict(topic="Xanthelasma", io=IO, slot="test finding",
   q="Which description of xanthelasma is accurate?",
   opts=[
     ["Along the NASAL portions of one or both eyelids — consider lipid disorders",
      "Correct — xanthelasma are raised yellowish plaques along the nasal portions of the eyelids that should prompt a look for lipid disorders."],
     ["Along the temporal portions of the lids — consider thyroid disease",
      "The plaques sit on the nasal, not temporal, portions of the lids, and they point to lipid disorders rather than thyroid disease."],
     ["At the lid margin — consider bacterial infection",
      "A painful infection at the lid margin is a hordeolum; xanthelasma sit nasally on the lids and suggest lipid disorders."],
     ["On the bulbar conjunctiva — consider ultraviolet exposure",
      "A yellowish nodule on the bulbar conjunctiva is a pinguecula; xanthelasma sit nasally on the lids and suggest lipid disorders."]],
   c=0, cite=c(34)),

 dict(topic="Lid position", io=IO, slot="differential",
   q="What is trichiasis?",
   opts=[
     ["Posteriorly misdirected eyelashes", "Correct — trichiasis is posteriorly misdirected eyelashes, a lid finding separate from entropion and ectropion."],
     ["Inward turning of the lower lid margin", "An in-turned lower lid margin is entropion; trichiasis is posteriorly misdirected eyelashes."],
     ["Outward turning of the lower lid margin", "An out-turned lower lid margin is ectropion, common in the elderly; trichiasis is posteriorly misdirected eyelashes."],
     ["Drooping of the upper lid", "Drooping of the upper lid is ptosis; trichiasis is posteriorly misdirected eyelashes."]],
   c=0, cite=c(35)),

 dict(topic="Nasolacrimal duct", io=IO, slot="initial test",
   q="Which description of the nasolacrimal duct obstruction test is correct?",
   opts=[
     ["Ask the patient to look up, press on the lower lid near the medial canthus just inside the bony orbit to compress the lacrimal sac, and look for fluid regurgitating from the puncta — mucopurulent fluid suggests obstruction",
      "Correct — compressing the lacrimal sac near the medial canthus and seeing mucopurulent fluid from the puncta suggests an obstructed duct."],
     ["Instill fluorescein and time its disappearance from the tear film",
      "Fluorescein is used to show corneal damage under blue light; the duct test compresses the lacrimal sac and watches the puncta."],
     ["Press on the upper lid near the lateral canthus and look for tearing",
      "The press is on the lower lid near the medial canthus, over the lacrimal sac, watching for fluid from the puncta."],
     ["Evert the upper lid and inspect the tarsal conjunctiva",
      "Lid eversion is the search for a foreign body; the duct test compresses the lacrimal sac and watches the puncta."]],
   c=0, cite=c(38)),

 dict(topic="Nasolacrimal duct", io=IO, slot="avoid",
   q="When should the lacrimal sac compression test be avoided?",
   opts=[
     ["If the area is significantly inflamed or tender",
      "Correct — the lacrimal sac compression test is avoided if the area is significantly inflamed or tender."],
     ["If the patient wears contact lenses",
      "Contact lens wear is no reason to avoid it; the test is avoided only when the area is significantly inflamed or tender."],
     ["If the patient has had cataract surgery",
      "Cataract surgery in the elderly is a reason not to dilate the pupils, not to skip this test; avoid it if the area is inflamed."],
     ["If the patient is over sixty-five",
      "Age is no reason to avoid it; the lacrimal sac compression test is avoided when the area is significantly inflamed or tender."]],
   c=0, cite=c(38)),

 dict(topic="Upper lid eversion", io=IO, slot="initial test",
   q="What is the first step in everting the upper lid to search for a foreign body?",
   opts=[
     ["Ask the patient to look down and relax",
      "Correct — the patient looks down and relaxes; then the lashes are pulled down and forward over a stick placed 1 cm above the margin."],
     ["Ask the patient to look up, then pull the lid upward directly",
      "The patient looks down, not up, and the lashes are pulled gently down and forward rather than straight upward."],
     ["Press on the globe itself to push the lid outward",
      "You never press on the eyeball itself; the patient looks down and the lid is turned over a stick above the tarsal plate."],
     ["Use a cotton swab placed at the lid margin itself",
      "The stick goes at least 1 cm above the lid margin, at the upper border of the tarsal plate, after the patient looks down."]],
   c=0, cite=c(42)),

 dict(topic="Upper lid eversion", io=IO, slot="avoid",
   q="When must the lid never be everted?",
   opts=[
     ["If rupture of the globe is suspected", "Correct — the lid is never inverted or everted when rupture of the globe is suspected."],
     ["If the patient has conjunctivitis", "Conjunctivitis is not a contraindication; the lid is never everted when rupture of the globe is suspected."],
     ["If the patient wears contact lenses", "Contact lens wear is not a contraindication; the lid is never everted when rupture of the globe is suspected."],
     ["If a foreign body has already been seen", "Eversion is the way to search thoroughly for a foreign body; it is forbidden only when globe rupture is suspected."]],
   c=0, cite=c(42)),

 dict(topic="Sclera color", io=IO, slot="test finding",
   q="A YELLOW sclera indicates what?",
   opts=[
     ["Liver disease", "Correct — a yellow sclera reflects jaundice, which indicates liver disease."],
     ["Osteogenesis imperfecta", "Osteogenesis imperfecta gives a blue sclera; a yellow sclera from jaundice indicates liver disease."],
     ["Chronic ultraviolet exposure", "Ultraviolet exposure is not linked to scleral color; a yellow sclera from jaundice indicates liver disease."],
     ["Anemia", "Anemia is not linked to scleral color; a yellow sclera from jaundice indicates liver disease."]],
   c=0, cite=c(43)),

 dict(topic="Sclera color", io=IO, slot="test finding",
   q="A BLUE sclera indicates what?",
   opts=[
     ["Osteogenesis imperfecta", "Correct — a blue sclera is the scleral color seen in osteogenesis imperfecta."],
     ["Liver disease", "Liver disease gives a yellow sclera through jaundice; a blue sclera is seen in osteogenesis imperfecta."],
     ["Thyroid eye disease", "Thyroid eye disease causes proptosis and lid lag, not scleral color; a blue sclera suggests osteogenesis imperfecta."],
     ["Long-term steroid use", "Steroid use is a cataract risk factor, not a cause of scleral color; a blue sclera suggests osteogenesis imperfecta."]],
   c=0, cite=c(43)),

 dict(topic="Subconjunctival hemorrhage", io=IO, slot="test finding",
   q="Which findings characterize a subconjunctival hemorrhage on examination?",
   opts=[
     ["Pain absent, vision and pupil unaffected, no discharge, cornea clear",
      "Correct — a subconjunctival hemorrhage is painless with normal vision and pupil, no discharge and a clear cornea."],
     ["Pain present with photophobia and a hazy cornea",
      "Pain, photophobia and a hazy cornea suggest a corneal injury or ulcer; a subconjunctival hemorrhage is painless with a clear cornea."],
     ["Purulent discharge with lid crusting",
      "Purulent discharge suggests bacterial infection; a subconjunctival hemorrhage has no ocular discharge at all."],
     ["An irregular pupil with ciliary flush",
      "A small irregular pupil with redness around the limbus fits acute iritis; in a subconjunctival hemorrhage the pupil is unaffected."]],
   c=0, cite=c(44)),

 dict(topic="Subconjunctival hemorrhage", io=IO, slot="escalation",
   q="When is globe rupture more likely in a patient with a subconjunctival hemorrhage?",
   opts=[
     ["In trauma, and when the hemorrhage encircles the entire cornea",
      "Correct — globe rupture is more likely after trauma and when the hemorrhage encircles the entire cornea."],
     ["When the hemorrhage is small and sectoral",
      "A small patch is the usually harmless picture; rupture is more likely when the hemorrhage encircles the entire cornea after trauma."],
     ["When the patient is anticoagulated",
      "A bleeding disorder can cause the hemorrhage, but rupture is signaled by trauma with blood encircling the entire cornea."],
     ["When both eyes are affected",
      "Bilaterality is not the warning sign; rupture is more likely with trauma and hemorrhage encircling the entire cornea."]],
   c=0, cite=c(44)),

 dict(topic="Conjunctivitis", io=IO, slot="test finding",
   q="What is the pattern of redness in conjunctivitis?",
   opts=[
     ["Diffuse dilation of the conjunctival vessels",
      "Correct — conjunctivitis shows diffuse dilation of the conjunctival vessels, with redness maximal peripherally."],
     ["Redness maximal around the cornea, sparing the periphery",
      "Injection just around the cornea suggests keratitis, iritis or acute glaucoma; conjunctivitis is diffuse and maximal peripherally."],
     ["A single sharply demarcated red patch",
      "A sharply demarcated red area is a subconjunctival hemorrhage; conjunctivitis shows diffuse dilation of conjunctival vessels."],
     ["A violaceous discoloration of the sclera",
      "Conjunctivitis does not discolor the sclera; it shows diffuse dilation of the conjunctival vessels, maximal peripherally."]],
   c=0, cite=c(45)),

 dict(topic="Conjunctivitis", io=IO, slot="test finding",
   q="What happens to vision in conjunctivitis?",
   opts=[
     ["Vision is not affected except for mild blurring from discharge",
      "Correct — conjunctivitis leaves vision unaffected apart from mild blurring from discharge, and the pupil is not affected."],
     ["Vision is usually decreased and the pupil is irregular",
      "Decreased vision with a small irregular pupil fits acute iritis; conjunctivitis leaves vision and the pupil unaffected."],
     ["Vision is normal but the pupil is fixed and mid-dilated",
      "A dilated, fixed pupil belongs to acute glaucoma, where vision is also decreased; conjunctivitis leaves the pupil unaffected."],
     ["Vision is decreased and the cornea is steamy",
      "Decreased vision with a steamy cornea is acute glaucoma; conjunctivitis leaves vision unaffected except for mild blurring."]],
   c=0, cite=c(45)),

 dict(topic="Injection pattern", io=IO, slot="differential",
   q="Injection localized JUST AROUND THE CORNEA suggests which three conditions?",
   opts=[
     ["Keratitis, iritis, or acute glaucoma",
      "Correct — injection just around the cornea could result from keratitis, iritis or acute glaucoma."],
     ["Conjunctivitis, blepharitis, or dry eye",
      "Conjunctivitis gives diffuse redness maximal peripherally, not a ring around the cornea; that ring suggests keratitis, iritis or glaucoma."],
     ["Subconjunctival hemorrhage, pinguecula, or pterygium",
      "Those are localized patches or growths of the conjunctiva; injection just around the cornea suggests keratitis, iritis or acute glaucoma."],
     ["Episcleritis, chalazion, or hordeolum",
      "Those are nodules and lid lesions; injection just around the cornea suggests keratitis, iritis or acute glaucoma."]],
   c=0, cite=c(46)),

 dict(topic="Nodular episcleritis", io=IO, slot="etiology",
   q="Nodular episcleritis is associated with which two systemic diseases?",
   opts=[
     ["Rheumatoid arthritis and lupus erythematosus",
      "Correct — nodular episcleritis can be seen in rheumatoid arthritis and lupus erythematosus."],
     ["Diabetes and hypertension",
      "Diabetes and hypertension show in the fundus, as retinopathy and hard exudates; nodular episcleritis goes with rheumatoid arthritis and lupus."],
     ["Graves disease and myasthenia gravis",
      "Graves disease causes proptosis and myasthenia gravis ptosis; nodular episcleritis goes with rheumatoid arthritis and lupus."],
     ["Sjögren syndrome and sarcoidosis",
      "Sjogren's syndrome causes dry mouth and dry eyes; nodular episcleritis goes with rheumatoid arthritis and lupus."]],
   c=0, cite=c(47)),

 # ---- the red-eye chart, slide 48 ----
 dict(topic="Red eye chart", io=IO, slot="differential", chart=True,
   q="Which cause of red eye shows redness that is DIFFUSE and maximal peripherally, with vision unaffected?",
   opts=[
     ["Conjunctivitis", "Correct — conjunctivitis gives diffuse conjunctival redness maximal peripherally, with vision affected only by mild blurring."],
     ["Acute iritis", "Acute iritis gives injection of the deeper vessels around the limbus and decreased vision."],
     ["Glaucoma", "Glaucoma gives deep-vessel redness around the limbus, a steamy cloudy cornea, a dilated fixed pupil and decreased vision."],
     ["Corneal injury or infection", "Corneal injury or infection gives deep-vessel redness around the limbus with vision usually decreased."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="In acute glaucoma, what is the cornea like?",
   opts=[
     ["Steamy and cloudy", "Correct — acute glaucoma makes the cornea steamy and cloudy, alongside a dilated fixed pupil and severe deep pain."],
     ["Clear", "A clear cornea belongs to conjunctivitis and subconjunctival hemorrhage; acute glaucoma makes it steamy and cloudy."],
     ["Clear or slightly clouded", "Clear or slightly clouded is the cornea of acute iritis; acute glaucoma makes it steamy and cloudy."],
     ["Changes depending on the cause", "A cornea that changes with the cause is corneal injury or infection; acute glaucoma makes it steamy and cloudy."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="In acute glaucoma, what is the pupil like?",
   opts=[
     ["Dilated and fixed", "Correct — acute glaucoma gives a dilated, fixed pupil, with a steamy cornea and an acute rise in intraocular pressure."],
     ["Not affected", "An unaffected pupil belongs to conjunctivitis and subconjunctival hemorrhage; in acute glaucoma it is dilated and fixed."],
     ["May be small and, with time, irregular", "A small pupil that may become irregular is acute iritis; in acute glaucoma the pupil is dilated and fixed."],
     ["Not affected unless iritis develops", "A pupil spared unless iritis develops is corneal injury or infection; in acute glaucoma it is dilated and fixed."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="What is the pain of acute iritis like?",
   opts=[
     ["Moderate, aching, deep", "Correct — acute iritis causes moderate, aching, deep pain, along with decreased vision."],
     ["Mild discomfort rather than pain", "Mild discomfort rather than pain is conjunctivitis; the pain of acute iritis is moderate, aching and deep."],
     ["Severe, aching, deep", "Severe, aching, deep pain is glaucoma; the pain of acute iritis is moderate rather than severe."],
     ["Absent", "Absent pain is subconjunctival hemorrhage; the pain of acute iritis is moderate, aching and deep."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="Which cause of red eye has no discharge, an unaffected pupil, a clear cornea and no pain?",
   opts=[
     ["Subconjunctival hemorrhage", "Correct — subconjunctival hemorrhage has absent pain and discharge, an unaffected pupil and vision, and a clear cornea."],
     ["Conjunctivitis", "Conjunctivitis has watery, mucoid or mucopurulent discharge and mild discomfort, though its pupil and cornea are normal."],
     ["Acute iritis", "Acute iritis has moderate aching pain and a pupil that may be small and irregular."],
     ["Glaucoma", "Glaucoma has severe aching pain, a steamy cloudy cornea and a dilated fixed pupil."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="differential", chart=True,
   q="Which description of ciliary injection is accurate?",
   opts=[
     ["Dilation of deeper vessels visible as radiating vessels or a reddish-violet flush around the limbus — it is important because those three conditions can threaten sight",
      "Correct — deeper vessels dilate as radiating vessels or a reddish-violet flush around the limbus, marking the more serious red-eye disorders."],
     ["Dilation of the superficial conjunctival vessels maximal at the periphery",
      "Diffuse superficial dilation maximal peripherally is the conjunctivitis pattern; the ciliary pattern is a deep flush around the limbus."],
     ["A sharply demarcated homogeneous red patch",
      "A sharply demarcated homogeneous red area is subconjunctival hemorrhage; the ciliary pattern is a deep flush around the limbus."],
     ["A violaceous hue from scleral thinning",
      "Scleral thinning is not how it arises; the ciliary pattern is dilation of deeper vessels seen as a flush around the limbus."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="test finding", chart=True,
   q="Corneal injury, acute iritis and glaucoma can make the eye diffusely red rather than showing ciliary injection. Which clues still point to them?",
   opts=[
     ["Pain, decreased vision, unequal pupils, a hazy cornea",
      "Correct — pain, decreased vision, unequal pupils and a less than perfectly clear cornea mark these more serious disorders."],
     ["Itch, watery discharge and lid crusting",
      "Itching and watery discharge point to allergic or viral conditions; the serious disorders show pain, poor vision and unequal pupils."],
     ["Bilateral involvement and a preauricular node",
      "Bilateral involvement and a preauricular node do not mark these disorders; pain, decreased vision, unequal pupils and a hazy cornea do."],
     ["Fever and periorbital swelling",
      "Fever and periorbital swelling do not mark these disorders; pain, decreased vision, unequal pupils and a hazy cornea do."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="prognosis", chart=True,
   q="A red eye with severe deep pain, a steamy cornea and a dilated fixed pupil signifies what?",
   opts=[
     ["An acute increase in intraocular pressure — an emergency",
      "Correct — severe deep pain, a steamy cornea and a fixed dilated pupil signify an acute rise in intraocular pressure, an emergency."],
     ["Bacterial, viral and other infections, or allergy and irritation",
      "Infection, allergy or irritation is the significance of conjunctivitis, which has mild discomfort, a clear cornea and a normal pupil."],
     ["Abrasions and other injuries; viral and bacterial infections",
      "Injuries and infections are the significance of corneal injury, where the pupil is unaffected unless iritis develops."],
     ["Often none; may result from trauma, bleeding disorders, or a sudden increase in venous pressure",
      "That is subconjunctival hemorrhage, which is painless with a clear cornea and an unaffected pupil."]],
   c=0, cite=ci(48)),

 dict(topic="Red eye chart", io=IO, slot="education", chart=True,
   q="Which cause of red eye gives moderate to severe SUPERFICIAL pain with vision usually decreased?",
   opts=[
     ["Corneal injury or infection",
      "Correct — corneal injury or infection gives moderate to severe superficial pain, usually decreased vision, and watery or purulent discharge."],
     ["Acute iritis",
      "Acute iritis causes moderate, aching, DEEP pain rather than superficial pain, and has no discharge."],
     ["Glaucoma",
      "Glaucoma causes severe, aching, DEEP pain, with a steamy cornea and a dilated fixed pupil."],
     ["Conjunctivitis",
      "Conjunctivitis causes mild discomfort rather than pain, and vision is unaffected apart from mild blurring."]],
   c=0, cite="PD II Advanced Exam Ocular Lecture - Beck.pptx, Slide 48 (image only)"),
]
