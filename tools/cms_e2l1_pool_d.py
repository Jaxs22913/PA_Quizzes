# -*- coding: utf-8 -*-
# CMS I Exam 2, Lecture 1 -- pool D: orbital and periorbital cellulitis, the
# diagnostic modalities, and the red-eye triage framework (slides 66-71).
#
# THE TRIAGE SLIDES ARE THE HIGHEST-YIELD PART OF THIS DECK for a management
# exam: they give an explicit first-60-seconds sequence, a danger-sign list, a
# localisation pattern, and an emergent/same-day/urgent/routine disposition
# table. Prof. Jaquith told the Exam 1 class her questions are "pretty much all
# clinical vignettes ... A LOT are next management plan / first line treatment /
# patient education", which is exactly what these slides support.
#
# Correct answer is ALWAYS written first (c=0); the partition script rotates.
SRC = "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx"
def c(n): return f"{SRC}, Slide {n}"
def cn(n): return f"{SRC}, Slide {n} (speaker notes)"

IOA = ("Objective a — Compare and contrast the etiologies, epidemiology, risk factors, "
       "clinical manifestations, differential diagnosis, diagnostic testing, management, "
       "appropriate referrals, patient education, and prognosis of the following common "
       "ophthalmological disorders")
IOB = ("Objective b — Identify medical care strategies for ophthalmological disorders in the "
       "lecture topic list for the following populations: infant, child, adolescent, adult, elderly")

POOL_D = [
 # ---- cellulitis ----
 dict(topic="Cellulitis", io=IOA, slot="etiology",
   q="Where does periorbital or orbital cellulitis usually come from?",
   opts=[
     ["Direct extension from a bacterial sinus, skin or dental infection",
      "Correct — the orbit is separated from the ethmoid sinus by paper-thin bone and shares venous drainage with the face and teeth, so infection spreads directly from those sites."],
     ["Haematogenous spread from a distant focus",
      "Bloodborne seeding is possible but uncommon; the usual route is direct extension from an adjacent sinus, skin or dental infection."],
     ["Nasolacrimal duct obstruction",
      "That underlies dacryocystitis."],
     ["Contact lens contamination",
      "That is a keratitis risk."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="etiology",
   q="In which patients should a FUNGAL cause of orbital cellulitis be considered?",
   opts=[
     ["Diabetic, elderly or immunocompromised patients — aspergillosis or mucormycosis",
      "Correct — Aspergillus and Mucor invade when immunity or tissue perfusion fails, and mucormycosis in particular thrives in diabetic ketoacidosis, spreading from the sinuses into the orbit within days."],
     ["Contact lens wearers",
      "That is a bacterial and Acanthamoeba risk in keratitis."],
     ["Neonates",
      "Neonates are at risk of gonococcal conjunctivitis; invasive fungal orbital infection affects diabetic, elderly and immunocompromised patients."],
     ["Patients with rosacea",
      "That is a blepharitis association."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="differential",
   q="Which symptoms occur in POST-septal cellulitis but not pre-septal?",
   opts=[
     ["Difficulty and pain with eye movement, reduced vision, and diplopia",
      "Correct — only post-septal infection involves the extraocular muscles and optic nerve behind the orbital septum, so painful restricted movement, diplopia and reduced vision mark that boundary being crossed."],
     ["Periocular pain, fever and chills",
      "Those occur in both."],
     ["Warmth of the tissue around the eye",
      "That occurs in both."],
     ["Lid erythema and oedema",
      "That occurs in both."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="test finding",
   q="Two cellulitis photographs can be contrasted with one phrase. What is the giveaway in PRE-septal disease?",
   opts=[
     ["The eye itself is white, despite the swollen erythematous lid and periorbital area",
      "Correct — the orbital septum confines the infection to the lid, so the globe itself stays white and moves normally however dramatic the lid swelling looks."],
     ["The eye itself is red and cannot look down",
      "That is the post-septal photograph."],
     ["The pupil is fixed and mid-dilated",
      "That is acute angle closure."],
     ["There is a violaceous scleral patch",
      "That is scleritis."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="test finding",
   q="Which examination findings are given for POST-septal (orbital) cellulitis?",
   opts=[
     ["Significant conjunctival injection, proptosis, decreased and painful extraocular movement, possible afferent pupillary defect and decreased vision",
      "Correct — infection behind the septum fills the orbit, pushing the globe forward, inflaming the muscles so movement hurts, and compressing the optic nerve to give an afferent defect and reduced vision."],
     ["Balloon-like lid oedema with a white globe and full painless movements",
      "That is pre-septal disease."],
     ["Follicles with a tender preauricular node",
      "That is viral conjunctivitis."],
     ["A dendritic corneal ulcer",
      "That is herpes simplex keratitis."]],
   c=0, cite=c(52)),

 dict(topic="Cellulitis", io=IOA, slot="initial test",
   q="Which workup is ordered for cellulitis?",
   opts=[
     ["Computed tomography of the orbits and paranasal sinuses with contrast, complete ocular examination including fundoscopy, Gram stain and culture of any open wound or drainage, a complete blood count with differential, and blood cultures",
      "Correct — imaging defines whether infection has crossed the septum and whether an abscess has formed, while the ocular examination and cultures establish severity and the responsible organism."],
     ["Computed tomography alone",
      "Imaging alone leaves the organism unidentified and the optic nerve unassessed; cultures, blood count and a full ocular examination accompany it."],
     ["Slit lamp examination with fluorescein alone",
      "That is the corneal workup."],
     ["Serum lipid profile and liver function tests",
      "That is xanthelasma."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="agent/regimen",
   q="How is MILD pre-septal cellulitis treated?",
   opts=[
     ["Outpatient oral antibiotics for 10 to 14 days aimed at Staphylococcus, including resistant strains, and Streptococcus",
      "Correct — cover must include methicillin-resistant Staphylococcus aureus as well as Streptococcus, and a 10 to 14 day oral course suffices while the globe remains uninvolved."],
     ["Hospitalisation with broad-spectrum intravenous antibiotics for 48 to 72 hours",
      "That is for moderate-severe, non-compliant, young children, or any post-septal disease."],
     ["Topical antibiotic drops for seven days",
      "Insufficient for a tissue infection."],
     ["Oral antivirals for ten days",
      "That is herpetic keratitis."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOB, slot="escalation",
   q="Which patients with PRE-septal cellulitis are hospitalised?",
   opts=[
     ["Moderate to severe or toxic disease, concern for poor compliance, a child of five years or younger, or no improvement after oral antibiotics were started",
      "Correct — each marks either a patient who cannot be safely observed at home or disease already failing oral therapy, and children of five or under are admitted because post-septal spread is quicker and harder to detect."],
     ["Every patient with pre-septal disease",
      "Mild disease is managed as an outpatient."],
     ["Only patients over sixty-five",
      "The age criterion runs the other way: it is children of five or under who are admitted, because spread behind the septum is faster and harder to assess."],
     ["Only contact lens wearers",
      "Not a criterion for cellulitis."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="complication",
   q="What may untreated cellulitis spread to cause?",
   opts=[
     ["Intracranial spread causing meningitis or cavernous sinus thrombosis",
      "Correct — the orbital veins are valveless and drain backwards into the cavernous sinus, so infection can track intracranially to produce cavernous sinus thrombosis or meningitis."],
     ["Corneal perforation and endophthalmitis",
      "That is the keratitis chain."],
     ["Entropion and trichiasis",
      "That is the trachoma chain."],
     ["Retinal detachment",
      "Retinal detachment is a mechanical separation of retinal layers, unrelated to the intracranial spread that threatens here."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="referral",
   q="Which consults may be needed in cellulitis?",
   opts=[
     ["Ear, nose and throat; oral and maxillofacial surgery; and infectious disease",
      "Correct — the sinuses and teeth are the usual source, so drainage may need ear, nose and throat or maxillofacial surgery, with infectious disease guiding antimicrobial choice in resistant or fungal disease."],
     ["Haematology and rheumatology",
      "Haematology and rheumatology address blood and autoimmune disease; here the source is sinus or dental, and the specialties that follow are surgical and infectious disease."],
     ["Endocrinology and nephrology",
      "Endocrinology and nephrology are not the relevant teams; the infection arises from sinus or dental sources and may need surgical drainage."],
     ["Dermatology alone",
      "Dermatology alone is insufficient; this is a deep orbital infection from a sinus or dental source, needing surgical and infectious disease input."]],
   c=0, cite=c(53)),

 dict(topic="Cellulitis", io=IOA, slot="initial test",
   q="When is a contrast scan NOT routinely required in cellulitis?",
   opts=[
     ["In mild, clearly pre-septal disease with normal vision, normal pupils and painless full extraocular movements",
      "Correct — normal vision, normal pupils and painless full movements together establish that the septum has not been crossed, which is what the scan would otherwise be looking for."],
     ["In any patient under five years old",
      "Young age pushes toward admission, not away from imaging."],
     ["In any patient who is febrile",
      "Fever does not remove the need."],
     ["Never — imaging is always required",
      "Imaging can be omitted where the examination already excludes post-septal involvement, which spares a child a contrast scan."]],
   c=0, cite=cn(53)),

 # ---- diagnostic modalities ----
 dict(topic="Slit lamp", io=IOA, slot="initial test",
   q="What is a slit lamp, and which structures does it examine?",
   opts=[
     ["A low-power microscope with a high-intensity light focused as a thin slit, examining the anterior structures — lids, cornea, conjunctiva, sclera and iris",
      "Correct — the narrow slit of light creates an optical section through transparent tissue, so the cornea, anterior chamber and iris can be examined layer by layer under magnification."],
     ["A hand-held light for viewing the retina and optic disc",
      "That is a direct ophthalmoscope."],
     ["An injected dye study of retinal blood flow",
      "That is fluorescein angiography."],
     ["A pressure-measuring pen applied to the cornea",
      "That is a tonometer."]],
   c=0, cite=c(7)),

 dict(topic="Ophthalmoscopy", io=IOA, slot="initial test",
   q="Which three types of ophthalmoscopy are described, and which is most commonly used?",
   opts=[
     ["Direct, indirect and slit-lamp ophthalmoscopy — slit-lamp is most common, because the patient is usually already seated there",
      "Correct — the three types and the practical reason for the third."],
     ["Direct, indirect and fluorescein — direct is most common",
      "Fluorescein examination is a separate modality."],
     ["Monocular, binocular and digital — digital is most common",
      "These are not the categories; ophthalmoscopy is divided into direct, indirect and slit-lamp, the last being most used in practice."],
     ["Direct and indirect only — indirect is most common",
      "There are three rather than two, the third being slit-lamp ophthalmoscopy, which is the one most commonly used."]],
   c=0, cite=c(8)),

 dict(topic="Fluorescein examination", io=IOA, slot="initial test",
   q="How is a fluorescein examination performed, and what does it detect?",
   opts=[
     ["A yellow dye is instilled and the eye examined under a Wood lamp with ultraviolet light, detecting corneal abrasions, ulcers and foreign bodies",
      "Correct — fluorescein pools wherever the corneal epithelium is missing and glows green under ultraviolet light, so abrasions, ulcers and retained foreign bodies become visible."],
     ["Dye is injected into the arm and a blue-flash camera photographs the retina",
      "That is fluorescein ANGIOGRAPHY, a different test."],
     ["A drop of phenylephrine is instilled and the vessels observed for blanching",
      "That is the episcleritis test."],
     ["A pen tonometer is applied to the anaesthetised cornea",
      "That measures pressure."]],
   c=0, cite=c(9)),

 dict(topic="Fluorescein angiography", io=IOA, slot="initial test",
   q="How does fluorescein ANGIOGRAPHY differ from a fluorescein examination?",
   opts=[
     ["The dye is injected into the hand or arm, reaches the eye in about 10 to 15 seconds, and a blue-flash camera images blood flow in the retina and choroid",
      "Correct — injected rather than instilled, and it images flow rather than surface defects."],
     ["The dye is instilled as a drop and viewed with a Wood lamp",
      "That is the surface examination."],
     ["It uses iodine contrast and so is contraindicated in shellfish allergy",
      "Fluorescein contains no iodine, so a shellfish or iodine allergy is not a contraindication; that concern belongs to iodinated radiographic contrast."],
     ["It images the anterior chamber rather than the retina",
      "It images the posterior circulation."]],
   c=0, cite=c(10)),

 dict(topic="Fluorescein angiography", io=IOA, slot="education",
   q="What is noted about the safety of fluorescein angiography dye?",
   opts=[
     ["It is relatively safe and has no iodine",
      "Correct — fluorescein contains no iodine, so the iodinated-contrast precautions do not apply; reactions are usually limited to transient nausea and yellow discolouration of skin and urine."],
     ["It contains iodine and is contraindicated in renal impairment",
      "Fluorescein contains no iodine at all, which is precisely what separates it from iodinated radiographic contrast."],
     ["It is radioactive and requires shielding",
      "It is not radioactive."],
     ["It commonly causes anaphylaxis",
      "Anaphylaxis is rare; the usual effects are transient nausea and temporary yellow discolouration of skin and urine."]],
   c=0, cite=c(10)),

 dict(topic="Fluorescein angiography", io=IOA, slot="initial test",
   q="Which conditions can fluorescein angiography detect?",
   opts=[
     ["Diabetic retinopathy, macular degeneration, macular oedema, ocular melanoma, retinal detachment and retinitis pigmentosa",
      "Correct — the dye fills the retinal and choroidal circulation, so leakage, non-perfusion and abnormal vessels show up, which is what each of these conditions produces."],
     ["Corneal abrasions, ulcers and foreign bodies",
      "Those are found by the surface fluorescein examination."],
     ["Cataract, dry eye and blepharitis",
      "Those are anterior and are found on slit lamp."],
     ["Orbital cellulitis and sinus disease",
      "Those need computed tomography."]],
   c=0, cite=c(10)),

 # ---- red eye triage ----
 dict(topic="Red eye triage", io=IOA, slot="initial test",
   q="What must be completed BEFORE naming a diagnosis in a red eye?",
   opts=[
     ["Visual acuity in each eye with correction, pupils, extraocular movements, corneal clarity and fluorescein staining, the pattern of injection and discharge, and the contact lens, trauma, surgery and steroid history",
      "Correct — acuity, pupils, movements and corneal clarity are what separate a benign red eye from a sight-threatening one, and the history identifies the patients at highest risk."],
     ["Computed tomography of the orbits",
      "Imaging is not the first step in a red eye."],
     ["A complete blood count and blood cultures",
      "Those belong to the cellulitis workup."],
     ["Referral to ophthalmology before any examination",
      "Referral without examination cannot distinguish an emergency from conjunctivitis, and the basic sequence takes under a minute."]],
   c=0, cite=c(67)),

 dict(topic="Red eye triage", io=IOA, slot="test finding",
   q="Which two findings are singled out as red flags in a red eye?",
   opts=[
     ["Reduced vision or an abnormal pupil",
      "Correct — conjunctivitis affects neither vision nor the pupil, so either finding means the problem lies deeper and the reflex diagnosis is wrong."],
     ["Watery discharge or itching",
      "Those point toward benign causes."],
     ["Bilateral involvement or crusting",
      "Bilateral redness and crusting are typical of benign conjunctivitis; the red flags are reduced vision and an abnormal pupil."],
     ["Preauricular node or follicles",
      "Those indicate a cause rather than danger."]],
   c=0, cite=c(67)),

 dict(topic="Red eye triage", io=IOA, slot="education",
   q="What warning attaches to the red-eye examination?",
   opts=[
     ["Do not let obvious redness substitute for an eye examination",
      "Correct — redness is common to almost every cause, benign and sight-threatening alike, so it carries no diagnostic weight until acuity, pupils and the cornea have been checked."],
     ["Do not examine the eye until acuity is documented by an optometrist",
      "Acuity is measured at the bedside as the first step, not deferred to an optometrist."],
     ["Do not use fluorescein before ophthalmology has been consulted",
      "Fluorescein is part of the first-60-seconds sequence."],
     ["Do not measure acuity in a painful eye",
      "Acuity is the first measurement taken, even in a painful eye, because it is what separates benign from sight-threatening causes."]],
   c=0, cite=cn(67)),

 dict(topic="Red eye triage", io=IOA, slot="initial test",
   q="Which is the ONE exception to the normal red-eye sequence?",
   opts=[
     ["Chemical exposure — begin copious irrigation before the history or examination, then verify the surface pH has normalised",
      "Correct — alkali in particular keeps penetrating while the history is taken, so irrigation starts immediately and pH is rechecked until it normalises."],
     ["Contact lens wear — remove the lens before any history",
      "Removing the lens matters, but it does not displace the examination sequence the way ongoing chemical injury does."],
     ["Trauma — obtain imaging before examining",
      "Trauma still begins with examination, with a shield placed if the globe may be open; the exception that overrides the sequence is chemical exposure."],
     ["Fever — obtain blood cultures before examining",
      "Fever does not change the order; the one exception is chemical exposure, where irrigation precedes everything."]],
   c=0, cite=cn(67)),

 dict(topic="Red eye danger signs", io=IOA, slot="referral",
   q="Which findings should stop the reflex diagnosis of conjunctivitis?",
   opts=[
     ["Moderate to severe pain or consensual photophobia, reduced acuity or an abnormal pupil, corneal opacity or dendrite, ciliary flush or hypopyon, proptosis or restricted movement, chemical or penetrating injury, and a contact lens wearer with pain",
      "Correct — each indicates the cornea, anterior chamber or orbit is involved, and none of them occurs in simple conjunctivitis."],
     ["Bilateral redness with watery discharge and itching",
      "Those point to benign allergic or viral disease."],
     ["Crusting of the lids on waking",
      "Common in benign conjunctivitis."],
     ["A tender preauricular node",
      "That indicates viral or chlamydial cause, not danger."]],
   c=0, cite=c(68)),

 dict(topic="Red eye danger signs", io=IOA, slot="test finding",
   q="What is CONSENSUAL photophobia, and what does it support?",
   opts=[
     ["Pain in the affected eye when light is shone in the UNAFFECTED eye — it supports anterior uveitis",
      "Correct — light in either eye constricts both pupils, so if moving the inflamed iris hurts, the pain appears even when the other eye is illuminated, which points to anterior uveitis rather than a corneal surface problem."],
     ["Pain in both eyes when light is shone in either — it supports conjunctivitis",
      "Not the definition, and conjunctivitis does not do this."],
     ["Pain only when light is shone in the affected eye — it supports keratitis",
      "That is ordinary direct photophobia."],
     ["Pain on eye movement — it supports optic neuritis",
      "That is a different sign."]],
   c=0, cite=cn(68)),

 dict(topic="Red eye danger signs", io=IOA, slot="escalation",
   q="What must be done for a suspected OPEN GLOBE?",
   opts=[
     ["Place a rigid eye shield, avoid pressure, manipulation and tonometry, keep the patient nil by mouth, and obtain emergency ophthalmology consultation",
      "Correct — any pressure on a perforated globe can extrude intraocular contents, so the eye is shielded rather than patched, tonometry is avoided, and the patient is kept fasted for theatre."],
     ["Irrigate copiously before doing anything else",
      "That is the chemical injury protocol."],
     ["Measure the intraocular pressure to assess the damage",
      "Tonometry is specifically contraindicated."],
     ["Patch the eye firmly and arrange next-day review",
      "Pressure on the globe is exactly what must be avoided."]],
   c=0, cite=cn(68)),

 dict(topic="Red eye localisation", io=IOA, slot="differential",
   q="Which pattern localises the problem to the CONJUNCTIVA?",
   opts=[
     ["Itch or discharge with diffuse injection and preserved vision",
      "Correct — the conjunctiva has no role in focusing light, so vision is preserved, and its inflammation produces itch and discharge with redness spread evenly rather than concentrated at the limbus."],
     ["Pain and photophobia with a fluorescein defect or infiltrate",
      "That localises to the cornea."],
     ["Consensual photophobia with ciliary flush and an irregular pupil",
      "That localises to the anterior chamber."],
     ["Deep pain or painful eye movement with a violaceous sclera",
      "That localises to sclera or orbit."]],
   c=0, cite=c(69)),

 dict(topic="Red eye localisation", io=IOA, slot="differential",
   q="Which pattern localises the problem to the ANTERIOR CHAMBER?",
   opts=[
     ["Consensual photophobia, ciliary flush and an irregular pupil",
      "Correct — inflammation of the iris and ciliary body makes pupil movement painful, engorges the perilimbal vessels, and forms adhesions that distort the pupil."],
     ["Itch and discharge with diffuse injection",
      "That is conjunctival."],
     ["Pain with headache, halos and nausea, with a cloudy cornea",
      "That is angle closure."],
     ["Proptosis with restricted movement",
      "That is orbital."]],
   c=0, cite=c(69)),

 dict(topic="Red eye localisation", io=IOA, slot="differential",
   q="Which pattern localises the problem to ANGLE CLOSURE?",
   opts=[
     ["Pain or headache with halos and nausea, a cloudy cornea and a mid-dilated pupil",
      "Correct — the sudden pressure rise oedematises the cornea, producing halos and a cloudy appearance, while the pupil is fixed mid-dilated and the systemic response brings headache and nausea."],
     ["Itch with stringy discharge and preserved vision",
      "That is allergic conjunctivitis."],
     ["Foreign body sensation with a fluorescein-staining defect",
      "That is corneal."],
     ["Deep boring pain radiating to the face",
      "That is scleritis."]],
   c=0, cite=c(69)),

 # ---- disposition ----
 dict(topic="Referral timing", io=IOA, slot="referral",
   q="Which conditions are put in the EMERGENT — now — category?",
   opts=[
     ["Chemical injury (irrigate first), open globe, angle closure, orbital cellulitis and endophthalmitis",
      "Correct — in each the eye can be lost within hours, whether from continuing chemical damage, extrusion of contents, pressure-driven nerve death or spreading infection."],
     ["Keratitis, corneal ulcer, anterior uveitis, scleritis and ocular herpes zoster",
      "Those are the SAME DAY group."],
     ["Unexplained decreased vision and persistent pain or photophobia",
      "Those are the URGENT, 24 to 48 hour group."],
     ["Uncomplicated conjunctivitis and chronic eyelid disease",
      "Those are ROUTINE."]],
   c=0, cite=c(70)),

 dict(topic="Referral timing", io=IOA, slot="referral",
   q="Which conditions are put in the SAME DAY category?",
   opts=[
     ["Keratitis or corneal ulcer, anterior uveitis, scleritis, and ocular herpes zoster ophthalmicus",
      "Correct — each threatens sight over days rather than hours, so it needs specialist examination the same day but not within the hour."],
     ["Chemical injury, open globe and angle closure",
      "Those are emergent."],
     ["Uncomplicated conjunctivitis",
      "That is routine."],
     ["Chronic ocular surface disease",
      "That is routine."]],
   c=0, cite=c(70)),

 dict(topic="Referral timing", io=IOA, slot="referral",
   q="When is ROUTINE follow-up appropriate for a red eye?",
   opts=[
     ["Only when acuity is preserved, pupils and movements are normal, the cornea is clear without uptake or infiltrate, significant pain and photophobia are absent, and follow-up is reliable",
      "Correct — these five together exclude every sight-threatening cause, and reliable follow-up matters because a benign-looking eye can still declare itself later."],
     ["Whenever the patient has no discharge",
      "Far too permissive."],
     ["Whenever the redness is bilateral",
      "Laterality does not establish safety."],
     ["Whenever the patient is under forty",
      "Age is not a criterion."]],
   c=0, cite=cn(70)),

 dict(topic="Referral timing", io=IOA, slot="education",
   q="What should every red-eye assessment end with?",
   opts=[
     ["A clearly documented disposition and a safety-net plan — recording acuity, key negatives, suspected diagnosis, urgency, destination and explicit return precautions",
      "Correct — a red eye can deteriorate after the visit, so the record must show what was normal at the time and the patient must know exactly what would mean returning."],
     ["A prescription for a topical antibiotic",
      "Not every red eye needs one."],
     ["An appointment with ophthalmology within 24 hours",
      "Only some categories need that."],
     ["A referral for computed tomography",
      "Not routinely indicated."]],
   c=0, cite=cn(70)),

 # ---- the contact lens case ----
 dict(topic="Contact lens keratitis", io=IOA, slot="first-line",
   q="A contact lens wearer has severe unilateral pain, photophobia and blurred vision after sleeping in lenses, with a central epithelial defect and a white infiltrate. What are the immediate next steps?",
   opts=[
     ["Remove the lenses without patching, give no take-home topical anaesthetic or corticosteroid, arrange same-day ophthalmology evaluation, and preserve the lenses and case if culture is wanted",
      "Correct — this is microbial keratitis until proven otherwise; patching incubates the organism, take-home anaesthetic masks progression, steroids suppress local immunity, and the lens and case often grow the organism."],
     ["Patch the eye, give a topical anaesthetic for comfort, and review in two days",
      "Patching and take-home anaesthetic are both specifically prohibited."],
     ["Start a topical corticosteroid and review next week",
      "Steroids can worsen uncontrolled infection."],
     ["Reassure and treat as viral conjunctivitis",
      "A central infiltrate with an epithelial defect in a lens wearer is microbial keratitis, which can perforate the cornea within days; viral conjunctivitis produces neither."]],
   c=0, cite=c(71)),

 dict(topic="Contact lens keratitis", io=IOA, slot="avoid",
   q="Why must a topical anaesthetic never be dispensed for home use?",
   opts=[
     ["It delays healing and masks progression",
      "Correct — repeated anaesthetic is directly toxic to the corneal epithelium and slows healing, and by abolishing pain it removes the one warning that the ulcer is worsening."],
     ["It causes an allergic reaction in most patients",
      "Allergy is not the issue; repeated use is toxic to the corneal epithelium and abolishes the pain that signals deterioration."],
     ["It raises intraocular pressure",
      "That is a corticosteroid effect."],
     ["It interferes with culture results",
      "Culture interference is not the concern; the harm is delayed epithelial healing and the loss of pain as a warning sign."]],
   c=0, cite=cn(71)),

 dict(topic="Contact lens keratitis", io=IOA, slot="escalation",
   q="What should be done if same-day ophthalmology evaluation is unavoidably delayed?",
   opts=[
     ["Consult ophthalmology immediately about empiric topical antipseudomonal therapy, and do not delay necessary treatment solely to obtain a culture",
      "Correct — Pseudomonas can perforate a cornea within 24 to 48 hours in a lens wearer, so empiric cover is agreed by telephone rather than waiting for a swab."],
     ["Wait for the culture result before starting anything",
      "Waiting for culture can cost the cornea; treatment starts empirically and the culture is taken if it does not delay it."],
     ["Start a topical corticosteroid while waiting",
      "Specifically prohibited."],
     ["Patch the eye and review in 48 hours",
      "Patching is prohibited."]],
   c=0, cite=cn(71)),

 dict(topic="Contact lens keratitis", io=IOA, slot="education",
   q="What safety-net advice should this patient be given?",
   opts=[
     ["Escalate immediately for increasing pain, an enlarging opacity, worsening photophobia, or further visual decline",
      "Correct — each signals the ulcer is progressing despite treatment, and in microbial keratitis the interval between deterioration and perforation can be a single day."],
     ["Return only if the eye is still red in one week",
      "Far too slow for microbial keratitis."],
     ["Resume lens wear once the pain settles",
      "Lenses must stay out."],
     ["No specific advice is needed once referral is arranged",
      "Referral alone is not enough; the patient must know which changes mean returning at once, because deterioration can be rapid."]],
   c=0, cite=cn(71)),
]
