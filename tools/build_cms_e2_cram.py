#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Clinical Medicine and Surgery I, Exam 2 cram sheet.

Condensed from the exam's own guide. The guide carries the explanation; this
carries only what has to be recallable cold the night before.

The first section is HOW THIS EXAM IS WRITTEN, because knowing the shape of the
paper is worth as much as any single fact. Prof. Jaquith described it for Exam 1
and there is no reason to expect Exam 2 to differ.

THE HEDGED SLIDES GET THEIR OWN ROWS. Several slides read as absolutes and are
softened by their own speaker notes; a cram sheet that repeated only the slide
would drill the wrong reflex.
"""
import sys, os
sys.path.insert(0, "/Users/jaxonluke/Developer/PA_Quizzes/tools/cram-sheet-template")
from render import render

OUT = ("/Users/jaxonluke/Developer/PA_Quizzes/Clinical Medicine and Surgery I Exam 2/"
       "cms-exam-2-cram-sheet.html")

topics = [
 {"id": "how", "label": "How This Exam Is Written", "color": "#2d3f7a", "rows": [
   ["Almost all vignettes", "“Pretty much all clinical vignettes… recognize conditions by the vignette.” Read for the DEFINING FEATURE, not the disease name."],
   ["What the lead-in asks", "“SOME diagnosis, but A LOT are next management plan, first line treatment, patient education.” The lead-in decides the answer — read it before the options."],
   ["Pictures", "“Way more non-pictures than pictures.” Do not bank on recognising a photograph."],
   ["Which half is this?", "CMS = MANAGEMENT. Clin Path I Lecture 4 = MECHANISM, on the same condition list. If the question asks WHY the tissue fails, that is the other course."],
 ]},
 {"id": "redeye", "label": "★ THE RED EYE — Before You Name It", "color": "#b8860b", "rows": [
   ["The first 60 seconds", "VISUAL ACUITY each eye with correction · PUPILS (shape, reactivity, afferent defect) · EXTRAOCULAR MOVEMENTS (pain? restriction?) · CORNEAL CLARITY + FLUORESCEIN · pattern of INJECTION and DISCHARGE · history of CONTACT LENS, TRAUMA, SURGERY, STEROIDS."],
   ["THE TWO RED FLAGS", "REDUCED VISION or an ABNORMAL PUPIL. “Do not let obvious redness substitute for an eye examination.”"],
   ["Danger signs — NOT conjunctivitis", "Moderate-severe pain or CONSENSUAL PHOTOPHOBIA · reduced acuity/RAPD/abnormal pupil · corneal opacity, infiltrate, ulcer or DENDRITE · CILIARY FLUSH, hypopyon, high pressure · proptosis, diplopia, painful restricted movement · chemical or penetrating injury, recent surgery · CONTACT LENS WEARER WITH PAIN."],
   ["Localise by pattern", "CONJUNCTIVA: itch/discharge, diffuse, VISION PRESERVED. CORNEA: pain/photophobia, fluorescein defect. ANTERIOR CHAMBER: CONSENSUAL photophobia, ciliary flush, irregular pupil. SCLERA/ORBIT: deep pain or painful movement, violaceous, proptosis. ANGLE CLOSURE: pain+headache+halos+nausea, cloudy cornea, MID-DILATED pupil."],
   ["TWO EXCEPTIONS TO THE SEQUENCE", "CHEMICAL — IRRIGATE FIRST, before history or exam, then check pH normalised. OPEN GLOBE — rigid shield, NO pressure, NO TONOMETRY, nil by mouth, emergency consult."],
   ["Referral timing", "EMERGENT NOW: chemical injury, open globe, angle closure, ORBITAL cellulitis, endophthalmitis. SAME DAY: keratitis/corneal ulcer, ANTERIOR UVEITIS, SCLERITIS, ocular herpes zoster. URGENT 24–48h: unexplained vision loss, persistent pain/photophobia, atypical red eye. ROUTINE: uncomplicated conjunctivitis, chronic lid disease."],
 ]},
 {"id": "lids", "label": "Eyelids", "color": "#5566b5", "rows": [
   ["ENTROPION vs ECTROPION", "ENTROPION turns IN → foreign body sensation → TRICHIASIS → corneal abrasion. ECTROPION turns OUT → tearing → EXPOSURE KERATOPATHY. CN VII palsy causes ECTROPION only. SURGERY IS DEFINITIVE for both."],
   ["DERMATOCHALASIS", "Excess loose skin + orbital fat prolapse, from AGEING. “Heaviness,” “looking through lashes.” EXAMINE VISUAL FIELDS — a deficit is what gets BLEPHAROPLASTY covered by insurance."],
   ["XANTHELASMA", "Oval YELLOWISH plaques, asymptomatic. WORK UP THE METABOLISM: lipid profile + fasting glucose/HbA1C + liver function. Treat the underlying issue. Local: cryotherapy, laser, peel, excision. RECURRENCES ARE COMMON. Caveat: many patients have NORMAL lipids."],
   ["BLEPHARITIS / MEIBOMITIS", "ROSACEA · SEBORRHOEIC DERMATITIS · STAPH AUREUS. Crusting/scaling at LASH BASES, thick TOOTHPASTE-LIKE meibomian secretion, decreased or frothy tear film. LID HYGIENE FIRST → if no better at 2 WEEKS, topical abx → then oral. CHRONIC: CONTROLLED, NOT CURED."],
   ["CHALAZION vs HORDEOLUM", "CHALAZION: STERILE meibomian obstruction, days–weeks, NON-TENDER. HORDEOLUM: acute INFECTION (staph), 24h/overnight, TENDER. Both: warm compresses + massage."],
   ["When to refer a lid lump", "HORDEOLUM: no better in 2 WEEKS → ophtho for I&D. CHALAZION: no resolution → ophtho for steroid injection or curettage; IMPROVEMENT MAY TAKE MONTHS. RECURRENT, or persisting >2–3 MONTHS → REFER TO RULE OUT SEBACEOUS CARCINOMA."],
 ]},
 {"id": "lacrimal", "label": "Lacrimal", "color": "#2f6b5a", "rows": [
   ["DACRYOADENITIS = GLAND", "LATERAL ⅓ of the UPPER lid. INFLAMMATORY MOST COMMON (bacterial rare, viral usually bilateral). ± ipsilateral PREAURICULAR node, temporal injection, fever, leukocytosis. Inflammatory → CORTICOSTEROIDS, response in 48h."],
   ["DACRYOCYSTITIS = SAC", "NASAL aspect of the LOWER lid, BELOW the medial canthal tendon. From NASOLACRIMAL DUCT OBSTRUCTION. Mucoid/purulent discharge EXPRESSIBLE FROM THE LOWER PUNCTUM."],
   ["A mass ABOVE the tendon", "NOT dacryocystitis — suspect a LACRIMAL SAC TUMOUR (rare)."],
   ["Dacryocystitis management", "Afebrile, well, reliable → OUTPATIENT ORAL ABX ×10 DAYS. Febrile, ill, unreliable → ADMIT, IV 48–72h then oral to complete 10–14 days. Improvement expected 24–48h. Afterwards: PROBING AND IRRIGATION often needed, may need surgery."],
   ["THE HEDGES", "Imaging is NOT automatic for either — reserve CT for severe disease, orbital findings, chronicity, atypical presentation, suspected abscess/mass, or failure to improve. DO NOT START STEROIDS until infection is reasonably excluded."],
 ]},
 {"id": "surface", "label": "Conjunctiva & Surface", "color": "#7a5a2e", "rows": [
   ["PINGUECULA vs PTERYGIUM", "Both from SUN and WIND, almost always at 3 or 9 O’CLOCK. PTERYGIUM EXTENDS ONTO THE CORNEA; PINGUECULA DOES NOT. “Pterodactyls fly (into cornea), penguins can’t.”"],
   ["Pterygium management", "Sun/dust/wind protection + lubricating drops — but CONSERVATIVE MANAGEMENT WILL NOT RESOLVE IT. NON-URGENT referral if GROWING or VISION AFFECTED. Surgery if distorting vision."],
   ["SUBCONJUNCTIVAL HAEMORRHAGE", "VALSALVA · bleeding disorder · ANTIPLATELET/ANTICOAGULANT · HYPERTENSION. Painless, vision/pupil/cornea NORMAL. HISTORY IS THE WORKUP — CHECK THE BP if unexplained. Reassurance; resolves 2–4 WEEKS."],
   ["Recurrent haemorrhage — the hedge", "NOT automatic haematology referral. Medication review, blood pressure, TARGETED evaluation for haematologic disease."],
   ["CHEMOSIS", "Conjunctival SWELLING — a SIGN, not a diagnosis. Allergy, infection, thyroid eye disease, angioedema, trauma, orbital cellulitis, impaired venous drainage. URGENT if with PROPTOSIS, RESTRICTED MOVEMENT, REDUCED VISION or an AFFERENT PUPILLARY DEFECT."],
 ]},
 {"id": "conj", "label": "Conjunctivitis — All Of It", "color": "#8f5aa8", "rows": [
   ["Acute vs chronic", "ACUTE ≤ 4 WEEKS. CHRONIC > 4 WEEKS."],
   ["PAPILLAE vs FOLLICLES", "PAPILLAE: RED at surface, PALER at base → BACTERIAL (except chlamydia) and ALLERGIC. FOLLICLES: PALE at surface, REDDER at base → CHLAMYDIAL and VIRAL. PREAURICULAR NODE → chlamydial, GONOCOCCAL, viral."],
   ["ALLERGIC", "ITCH · bilateral · watery/stringy · chemosis · papillae · NO NODE · vision preserved. Avoid allergen, cool compresses, artificial tears, topical H1 ± mast cell stabiliser — OLOPATADINE DOES BOTH — plus systemic H1."],
   ["VIRAL", "ADENOVIRUS. Profuse WATERY discharge, FOLLICLES, TENDER PREAURICULAR NODE, starts one eye then the other, recent URI. Cool compresses, artificial tears, CONTAGIOUS PRECAUTIONS. Often WORSE OVER WEEK ONE, resolves 2–3 WEEKS. Refer if >3 wks, or photophobia/vision loss after onset."],
   ["BACTERIAL", "THICK YELLOW/WHITE discharge, often UNILATERAL, papillae, usually NO node. Immunocompetent adult → TOPICAL BROAD-SPECTRUM (fluoroquinolone) + contagious precautions."],
   ["URGENT REFERRAL in bacterial", "Immunocompromised · CONTACT LENS WEARER · recent eye surgery · foreign body · corneal opacity or suspected keratitis · NO IMPROVEMENT IN 24 HOURS."],
   ["GONOCOCCAL — the exception", "SEVERE purulent discharge WITH a PALPABLE PREAURICULAR NODE. NEWBORN = EMERGENCY: hospitalise, SYSTEMIC CEFTRIAXONE, cultures + Gram stain, test for chlamydia and dissemination. Untreated → CORNEAL PERFORATION."],
   ["CHLAMYDIAL — adult", "Serotypes D–K. CHRONIC (a month+), stringy mucoid, FOLLICLES, UNRESPONSIVE TO TOPICALS. Confirm: conjunctival NAAT or DFA. DOXYCYCLINE 100 mg BD × 7 DAYS. Avoid sun, full glass of water, stay upright, separate from antacids/iron/calcium/magnesium. EVALUATE FOR OTHER STIs, NOTIFY PARTNERS."],
   ["CHLAMYDIAL — neonate", "ERYTHROMYCIN 50 mg/kg/day divided QID × 14 DAYS. MONITOR UNDER 6 WEEKS FOR INFANTILE HYPERTROPHIC PYLORIC STENOSIS — erythromycin is a MOTILIN RECEPTOR AGONIST. Often admitted because of concomitant PNEUMONIA."],
   ["TRACHOMA", "Serotypes A, B, C. ***LEADING INFECTIOUS CAUSE OF BLINDNESS WORLDWIDE. Most active cases ASYMPTOMATIC. MDA: AZITHROMYCIN 1 g PO SINGLE DOSE where prevalence ≥5%. CHAIN: inflammation → LID SCARRING → ENTROPION → TRICHIASIS → blindness. TRICHIASIS NEEDS SURGERY."],
   ["AUTOIMMUNE", "Recurrent/chronic hyperaemia, MINIMAL PAIN, NO DISCHARGE, systemic complaints. Pemphigoid, Stevens–Johnson, Sjögren, GVHD. ROUTINE ophtho referral."],
 ]},
 {"id": "sclera", "label": "Episcleritis vs Scleritis", "color": "#a4502a", "rows": [
   ["EPISCLERITIS", "Often IDIOPATHIC. MILD acute pain, FOCAL/SECTORAL redness, NO discharge, NO photophobia. Vessels CAN be moved with a cotton tip."],
   ["THE TEST", "2.5% PHENYLEPHRINE, WAIT 15 MINUTES → EPISCLERAL VESSELS BLANCH."],
   ["Episcleritis treatment", "Artificial tears + ORAL NSAID TAKEN WITH FOOD. No response in 2 DAYS → refer. Usually self-limited; may recur in either eye."],
   ["SCLERITIS", "Often SYSTEMIC AUTOIMMUNE. SEVERE BORING PAIN, WORSE AT NIGHT, radiating to face. VIOLACEOUS HUE = choroid through THINNED sclera. Vessels CANNOT be moved. Pain WITH EYE MOVEMENT."],
   ["Scleritis management", "URGENT REFERRAL — SCLERA AT RISK OF PERFORATION, may need a surgical patch. Slit lamp + fundoscopy, work up the systemic cause."],
   ["THE FIRST SIGN OF RESPONSE", "DECREASED PAIN — even if the inflammation looks unchanged."],
   ["The hedges", "Non-infectious ANTERIOR scleritis commonly BEGINS with systemic NSAIDs; steroids/immunomodulators for severe, NECROTISING, posterior or refractory disease. PERFORATION RISK IS GREATEST IN NECROTISING DISEASE, not uniformly."],
 ]},
 {"id": "cornea", "label": "Cornea", "color": "#2f7d76", "rows": [
   ["CILIARY FLUSH", "Ring of red vessels from the LIMBUS around the cornea (anterior ciliary arteries). Means inflammation of CORNEA, IRIS or CILIARY BODY. Seen in: CORNEAL INFLAMMATION (ulcer, keratitis) · ANTERIOR UVEITIS · ACUTE GLAUCOMA. It RULES OUT simple conjunctivitis."],
   ["KERATITIS", "Risks: corneal trauma, DRY EYES, CONTACT LENS OVERWEAR, topical ocular STEROIDS. Signs: corneal OPACIFICATION, “BROKEN UP” corneal light reflection, CILIARY FLUSH. URGENT REFERRAL WITHIN 24h for slit lamp + fluorescein."],
   ["The ring infiltrate", "ACANTHAMOEBA — contact lens wearers with POOR HYGIENE, e.g. RINSING LENSES IN TAP WATER."],
   ["Undertreated keratitis", "CORNEAL SCARRING or PERFORATION → ENDOPHTHALMITIS → POSSIBLE REMOVAL OF THE EYE. Bacterial prognosis: good for small–moderate, POOR for severe, WORSE INSIDE THE VISUAL AXIS."],
   ["HSV vs HZV keratitis", "SIMPLEX: TRUE DENDRITE — tree-branching, ELEVATED EDGES, TERMINAL END BULBS. PATHOGNOMONIC. Younger. Skin NOT dermatomal, may cross midline. ZOSTER: PSEUDODENDRITE — lacks all three. Older. DERMATOMAL, usually V1, RESPECTS THE MIDLINE, often spares lower lid."],
   ["HUTCHINSON SIGN", "Vesicle on the TIP OF THE NOSE = NASOCILIARY branch = HIGHER RISK OF OCULAR INVOLVEMENT."],
   ["Herpetic treatment", "ORAL ANTIVIRALS (aciclovir/valaciclovir/famciclovir) ×10 DAYS, ideally within 72h of rash onset. IV aciclovir for severe, disseminated, orbital, retinal, CNS or significantly immunocompromised. NO TOPICAL GLUCOCORTICOIDS BY THE PCP IN ACTIVE HSV EPITHELIAL DISEASE."],
   ["CORNEAL ULCER", "CONTACT LENS USE = MAJOR RISK. Patient RESISTS OPENING THE EYE. Ciliary flush + corneal defect. EMERGENT REFERRAL — a step above keratitis. Swab central/large ulcers. Start BROAD-SPECTRUM TOPICAL (4th-gen fluoroquinolone). STEROIDS CAN WORSEN INFECTION IF STARTED TOO EARLY, especially FUNGAL or HERPETIC — leave to ophtho. NEXT-DAY follow-up; most heal 2–3 WEEKS."],
   ["The contact lens case", "REMOVE LENSES, DO NOT PATCH · NO take-home ANAESTHETIC (delays healing, masks progression) · NO empiric STEROID · SAME-DAY ophthalmology · PRESERVE LENSES AND CASE for culture. Do NOT delay treatment solely to obtain a culture."],
 ]},
 {"id": "uveitis", "label": "Uveitis", "color": "#7a2f5f", "rows": [
   ["ANTERIOR (iritis/iridocyclitis)", "PAIN, photophobia, redness AT THE CORNEAL EDGE, VISION OFTEN PRESERVED. CELLS IN THE ANTERIOR CHAMBER, CONSENSUAL PHOTOPHOBIA, CILIARY FLUSH, variable IOP, IRREGULAR PUPIL stuck to lens/cornea, KERATIC PRECIPITATES (WBC on the corneal endothelium)."],
   ["Anterior management", "URGENT REFERRAL WITHIN 24h for slit lamp + dilated fundoscopy — DELAY MAY COST VISION. Infectious → treat organism. Non-infectious → TOPICAL CORTICOSTEROIDS. Recurrent or systemic features → THOROUGH SYSTEMIC EVALUATION."],
   ["POSTERIOR (choroiditis/retinitis)", "Blurred vision, FLOATERS, SCOTOMAS, METAMORPHOPSIA — and NO PAIN if isolated. CELLS IN THE POSTERIOR VITREOUS, vitreous haze. Idiopathic, autoimmune, INFECTIOUS: TOXOPLASMOSIS, CMV."],
   ["Posterior management — THE DIFFERENCE", "DOES NOT RESPOND TO TOPICAL TREATMENT — may need an INTRAOCULAR CORTICOSTEROID INJECTION. Fluorescein angiography helps separate ACTIVE from INACTIVE lesions. Develops far more slowly, may last YEARS. INFECTION MUST BE EXCLUDED BEFORE IMMUNOSUPPRESSION."],
 ]},
 {"id": "cellulitis", "label": "Cellulitis & Diagnostics", "color": "#8a5a2b", "rows": [
   ["Both forms", "DIRECT EXTENSION from bacterial SINUS, SKIN or DENTAL infection. In DIABETIC/ELDERLY/IMMUNOCOMPROMISED consider FUNGUS — ASPERGILLOSIS, MUCORMYCOSIS."],
   ["THE GIVEAWAY", "PRE-SEPTAL: THE EYE ITSELF IS WHITE, movements FULL and PAINLESS, vision normal. POST-SEPTAL: eye RED, PROPTOSIS, PAINFUL RESTRICTED MOVEMENT, DIPLOPIA, reduced vision, possible AFFERENT PUPILLARY DEFECT."],
   ["Workup", "CT ORBITS + PARANASAL SINUSES WITH CONTRAST · complete ocular exam with fundoscopy · Gram stain and culture of drainage · CBC with differential · BLOOD CULTURES."],
   ["Management", "MILD PRE-SEPTAL → outpatient ORAL abx 10–14 DAYS vs STAPH (±MRSA) and STREP. ADMIT + IV 48–72h then oral ≥1 week if: moderate-severe/toxic, poor compliance, CHILD ≤5 YEARS, no improvement on orals — AND ALL POST-SEPTAL."],
   ["Untreated", "INTRACRANIAL SPREAD → MENINGITIS or CAVERNOUS SINUS THROMBOSIS. Expect improvement 24–48h. May need ENT, OMFS, and/or ID consults."],
   ["The hedge", "MILD, CLEARLY PRE-SEPTAL disease with normal vision, pupils and painless full movements may be managed CLINICALLY WITHOUT ROUTINE CT."],
   ["The four modalities", "SLIT LAMP: anterior — lids, cornea, conjunctiva, sclera, iris. OPHTHALMOSCOPY: direct / indirect / SLIT-LAMP (most common). FLUORESCEIN EXAM: dye INSTILLED, Wood lamp — abrasions, ulcers, foreign bodies. FLUORESCEIN ANGIOGRAPHY: dye INJECTED, reaches eye in 10–15 SEC, blue flash, NO IODINE — retina and choroid blood flow."],
 ]},
]

html = render(
    title="Clinical Medicine and Surgery I &middot; Exam 2 &mdash; Cram Sheet",
    kicker="PAJ 5500 &middot; Class of 2028",
    h1="Clinical Medicine and Surgery I &middot; Exam 2",
    sub="Ophthalmology block &mdash; everything that has to be recallable cold",
    topics=topics,
    guide_href="cms-exam-2-study-guide.html",
    footer_note=("The study guide carries the reasoning; this is the night-before sheet. "
                 "Where a slide reads as an absolute and its own speaker notes say otherwise, "
                 "the hedge is written out rather than the slide."),
    primary="#2d3f7a")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, "w", encoding="utf-8").write(html)
print("wrote %s (%d KB, %d sections, %d rows)"
      % (os.path.basename(OUT), len(html) // 1024, len(topics),
         sum(len(t["rows"]) for t in topics)))
