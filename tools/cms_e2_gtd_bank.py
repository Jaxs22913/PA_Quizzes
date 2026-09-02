# -*- coding: utf-8 -*-
"""Question bank for "Guess that Disease" -- CMS I Exam 2, ophthalmology.

Jaxon, 2026-09-01: "a picture of a disease process ... and under the image is
4 answer choices with plausible distractors (answer choices are just disease
names)."

THE INCLUSION BAR, and why so many of the block's pictures are not here.
All 225 pictures in the five Exam 2 decks were looked at. An item is only
built when THE PHOTOGRAPH ITSELF SHOWS THE FEATURE THAT NAMES THE DISEASE.
That threw out three whole categories:

  * Pictures with the answer printed in the pixels -- the "OPEN-ANGLE
    GLAUCOMA / ANGLE-CLOSURE GLAUCOMA" diagram, "Optic Nerve in Eye with
    Glaucoma", the UpToDate amblyopia table, "Types of Nystagmus", the
    "Fig. 1 Optic nerve swelling in a patient with optic neuritis" caption,
    "Macular Degeneration with Disciform Scarring", Exotropia/Hypertropia.
  * Diagrams and scans standing in for a finding: the third-nerve anatomical
    course, the eyelid cross-section, the head CT filed under periorbital
    haematoma. Where a real photograph of the same thing existed elsewhere in
    the deck it was pulled instead -- see tools/extract_cms_e2_gtd_images.py.
  * Pairs whose discriminator is not visible in a photograph at all:
      - chalazion vs hordeolum -- the difference is TENDERNESS.
      - full-thickness eye wall laceration vs globe rupture -- sharp versus
        blunt mechanism; the two pictures are near-identical, so only globe
        rupture is asked.
      - papilledema vs optic neuritis -- both are a swollen disc; laterality
        and acuity separate them, not the fundus photograph. Neither is
        offered as a distractor for the other.
      - retinoblastoma vs paediatric cataract -- both leukocoria. Cataract is
        deliberately NOT a distractor; the explanation names it instead.
      - pterygium -- the deck's pictures never clearly show it crossing the
        limbus, so it is a distractor only, never an answer.

Distractors are drawn from the same anatomical region so the picture has to be
read, and every one gets its own refutation naming the feature that rules it
out. Correct answers are authored at index 0 and rotated by the builder --
never chosen while writing, per [[answer_position_bias_check]].
"""

# cond, img, slide caption, deck citation, region, why-it-is, [(distractor, refutation)]
EYELID = "Region — Eyelid and lacrimal system"
SURFACE = "Region — Conjunctiva and ocular surface"
SCLERA = "Region — Sclera and orbit"
CORNEA = "Region — Cornea and anterior chamber"
FUNDUS = "Region — Retina and optic nerve"
PUPIL = "Region — Pupil and eye movements"
TUMOUR = "Region — Ocular tumours"
TRAUMA = "Region — Ocular trauma"

D10 = "CMS I Common Ophthalmological Disorders 2026 - Jaquith.pptx"
D11 = "11. Neuro-Ophthalmology STUDENT VERSION 2026.pptx"
D12 = "12. Acute Vision Loss current - Jaquith.pptx"
D13 = "Chronic Vision Loss & Tumors - Dr Rappa.pptx"
D14 = "CMS I Ocular Trauma - Shah Fallsv.pptx"

ITEMS = [
# ---------------------------------------------------------------- eyelid ----
dict(cond="Entropion", img="s012_1.jpg", slide=12, deck=D10, io=EYELID,
     alt="Lower eyelid with the margin turned inward against the globe",
     why="The lid margin is rolled INWARD, so the lashes sit against the globe and abrade it.",
     wrong=[("Ectropion", "The opposite malposition — the margin turns OUT and the inner lid surface is exposed."),
            ("Dermatochalasis", "That is redundant skin hanging over the lid crease; the margin itself sits normally."),
            ("Blepharitis", "That is crusting and scale at the lash bases, with the lid margin in its normal position.")]),

dict(cond="Ectropion", img="s012_2.jpg", slide=12, deck=D10, io=EYELID,
     alt="Lower eyelid margin turned outward, exposing the palpebral conjunctiva",
     why="The lower lid margin is turned OUTWARD, leaving the pink palpebral conjunctiva on show and the eye watering.",
     wrong=[("Entropion", "The opposite malposition — the margin rolls IN and the lashes rub the cornea."),
            ("Chemosis", "That is fluid swelling of the conjunctiva itself, not a lid that has fallen away from the globe."),
            ("Dacryocystitis", "That is a tender swelling below the medial canthal tendon, not eversion of the lid.")]),

dict(cond="Xanthelasma", img="s016_1.jpg", slide=16, deck=D10, io=EYELID,
     alt="Yellow plaques on the medial upper and lower eyelids of both eyes",
     why="Soft yellow plaques lying in the eyelid skin near the inner corner, typically on both sides.",
     wrong=[("Chalazion", "That is a single firm nodule inside the lid, not a flat yellow plaque in the skin."),
            ("Hordeolum", "That is a tender red swelling pointing at the lid margin."),
            ("Pinguecula", "That yellow deposit sits on the conjunctiva beside the cornea, not on eyelid skin.")]),

dict(cond="Blepharitis", img="s018_1.jpg", slide=18, deck=D10, io=EYELID,
     alt="Lid margin with crusting and collarettes at the bases of the lashes",
     why="Crusting and collarettes built up at the bases of the lashes along the whole lid margin.",
     wrong=[("Entropion", "Nothing here is turned in — the margin keeps its normal position."),
            ("Dacryoadenitis", "That swells the outer third of the upper lid; this is scale along the lash line."),
            ("Trachoma", "That scars the upper tarsal conjunctiva on the inner surface, not the lash bases.")]),

dict(cond="Dacryoadenitis", img="s022_1.jpg", slide=22, deck=D10, io=EYELID,
     alt="Swelling and redness over the outer part of the upper eyelids",
     why="Swelling centred over the OUTER third of the UPPER lid, where the lacrimal gland sits.",
     wrong=[("Dacryocystitis", "That swells BELOW the medial canthal tendon, over the lacrimal sac at the inner corner."),
            ("Chalazion", "That is a discrete nodule you can feel in the lid, not diffuse gland swelling."),
            ("Xanthelasma", "Those are painless yellow plaques at the inner corner of the lids.")]),

dict(cond="Dacryocystitis", img="s024_1.jpg", slide=24, deck=D10, io=EYELID,
     alt="Red swelling below the medial canthus at the lacrimal sac",
     why="A tender red swelling sitting BELOW the medial canthal tendon, over the lacrimal sac.",
     wrong=[("Dacryoadenitis", "That swells the OUTER third of the UPPER lid, at the opposite corner."),
            ("Hordeolum", "That points at the lid margin itself, not below the inner corner."),
            ("Pre-septal cellulitis", "That spreads diffusely through the lid, rather than pointing at one sac.")]),

# --------------------------------------------------------------- surface ----
dict(cond="Subconjunctival haemorrhage", img="s029_2.jpg", slide=29, deck=D10, io=SURFACE,
     alt="Sharply bounded sheet of bright red blood under the conjunctiva",
     why="A sharply bounded sheet of blood under the conjunctiva, with a clear cornea and a normal pupil.",
     wrong=[("Hyphema", "That blood layers INSIDE the anterior chamber, in front of the iris, with a fluid level."),
            ("Bacterial conjunctivitis", "That is diffuse injection with discharge, not one flat block of blood."),
            ("Scleritis", "That is a deep violaceous hue with severe pain, not free blood on the surface.")]),

dict(cond="Chemosis", img="s031_1.jpg", slide=31, deck=D10, io=SURFACE,
     alt="Conjunctiva swollen and ballooning forward over the limbus",
     why="The conjunctiva itself is swollen with fluid and balloons forward over the limbus.",
     wrong=[("Subconjunctival haemorrhage", "That is blood under a conjunctiva that is otherwise flat."),
            ("Pterygium", "That is a fixed wedge of fibrous tissue, not generalised fluid swelling."),
            ("Episcleritis", "That is sectoral redness of the vessels; the conjunctiva is not raised like this.")]),

dict(cond="Pinguecula", img="s027_1.jpg", slide=27, deck=D10, io=SURFACE,
     alt="Raised yellow-white conjunctival deposit beside the cornea, stopping at the limbus",
     why="A raised yellow-white conjunctival deposit that STOPS at the limbus and never reaches the cornea.",
     wrong=[("Pterygium", "That one keeps going — a wedge of tissue that crosses ONTO the cornea."),
            ("Conjunctival melanoma", "That is pigmented and brown, not a pale yellow deposit."),
            ("Chemosis", "That is diffuse fluid swelling of the whole conjunctiva, not a focal nodule.")]),

dict(cond="Bacterial conjunctivitis", img="l10-s033_pos1.jpg", slide=33, deck=D10, io=SURFACE,
     alt="Everted eyelid showing papillae on the tarsal conjunctiva",
     why="The everted lid shows PAPILLAE — flat-topped bumps each fed by a central vessel. Papillae point to bacterial disease.",
     wrong=[("Viral conjunctivitis", "That raises FOLLICLES — pale domes with vessels running around them — and a tender preauricular node."),
            ("Chlamydial conjunctivitis", "That is follicular too, and drags on for more than a month."),
            ("Trachoma", "Also follicular, on the upper lid, and it goes on to scar.")]),

dict(cond="Chlamydial conjunctivitis", img="l10-s042_pos2.jpg", slide=42, deck=D10, io=SURFACE,
     alt="Everted eyelid showing large pale follicles on the tarsal conjunctiva",
     why="Large pale FOLLICLES on the everted lid in an infection that has run on for weeks and failed topical treatment.",
     wrong=[("Bacterial conjunctivitis", "That raises PAPILLAE — flat-topped, each with a central vessel — and settles in days."),
            ("Allergic conjunctivitis", "That is papillary as well, and itch rather than chronicity is the complaint."),
            ("Gonococcal conjunctivitis", "That is hyperacute with copious pus, not a quiet follicular reaction.")]),

dict(cond="Gonococcal conjunctivitis", img="ext-gonococcal-conjunctivitis.jpg", slide=38, deck=D10, io=SURFACE,
     alt="Newborn with copious purulent discharge and marked lid swelling in both eyes",
     why="Hyperacute, COPIOUS purulent discharge with tense lid swelling — in a newborn this appears in the first days of life.",
     wrong=[("Chlamydial conjunctivitis", "In a newborn that comes later, around the second week, and the discharge is far less dramatic."),
            ("Bacterial conjunctivitis", "Ordinary bacterial disease does not produce pus at this volume or this speed."),
            ("Allergic conjunctivitis", "That is watery and itchy, and does not occur in a newborn.")]),

dict(cond="Trachoma", img="ext-trachoma-stages.jpg", slide=44, deck=D10, io=SURFACE,
     alt="Four stages of trachoma from upper lid follicles through scarring to corneal opacity",
     why="Upper-lid follicles that scar, pull the lid inward, turn the lashes onto the cornea and finally blind it.",
     wrong=[("Bacterial conjunctivitis", "That resolves in days and leaves no scarring."),
            ("Allergic conjunctivitis", "That recurs with exposure but never scars the lid or clouds the cornea."),
            ("Blepharitis", "That inflames the lash bases; it does not scar the tarsal conjunctiva.")]),

# ------------------------------------------------------- sclera and orbit ----
dict(cond="Episcleritis", img="s047_2.jpg", slide=47, deck=D10, io=SCLERA,
     alt="Sector of bright superficial redness on the globe with white sclera beneath",
     why="A sector of bright, SUPERFICIAL redness; the sclera underneath keeps its white colour and the eye is only mildly sore.",
     wrong=[("Scleritis", "That redness is deeper and violaceous, and the pain is severe enough to wake the patient at night."),
            ("Bacterial conjunctivitis", "That is diffuse injection with discharge, not one quiet sector."),
            ("Subconjunctival haemorrhage", "That is a solid block of blood, not dilated vessels.")]),

dict(cond="Scleritis", img="s049_1.jpg", slide=49, deck=D10, io=SCLERA,
     alt="Globe with a deep violaceous sector of scleral inflammation",
     why="A deep VIOLACEOUS hue from inflamed sclera, with boring pain that is worse at night and worse on eye movement.",
     wrong=[("Episcleritis", "That is bright and superficial, blanches with phenylephrine, and hurts only mildly."),
            ("Anterior uveitis", "That flushes the limbus in a ring and distorts the pupil; the sclera itself is not violaceous."),
            ("Chemosis", "That is clear fluid swelling of the conjunctiva, not deep scleral colour change.")]),

dict(cond="Pre-septal cellulitis", img="s052_1.jpg", slide=52, deck=D10, io=SCLERA,
     alt="Child with a red swollen eyelid and a white, normally positioned eye",
     why="The lid is red and swollen but THE EYE ITSELF IS WHITE and sits normally — the infection is in front of the orbital septum.",
     wrong=[("Post-septal cellulitis", "That pushes the globe forward and makes eye movement painful and restricted."),
            ("Periorbital haematoma", "That is bruising after blunt injury, not erythema and warmth."),
            ("Dacryoadenitis", "That is localised to the outer third of the upper lid, not the whole lid.")]),

dict(cond="Post-septal cellulitis", img="l10-s052_pos2.jpg", slide=52, deck=D10, io=SCLERA,
     alt="Eye pushed forward and displaced out of the orbit with the lid held open",
     why="The globe is pushed forward and displaced — PROPTOSIS, which cannot happen in front of the orbital septum.",
     wrong=[("Pre-septal cellulitis", "That swells the lid but leaves the globe white, quiet and in its normal position."),
            ("Chemosis", "That swells the conjunctiva alone; the globe does not move forward."),
            ("Dacryoadenitis", "That swells the lacrimal gland at the outer upper lid without displacing the eye.")]),

# ---------------------------------------------------------------- cornea ----
dict(cond="Herpes simplex keratitis", img="s057_1.jpg", slide=57, deck=D10, io=CORNEA,
     alt="Cornea stained with fluorescein showing a branching dendrite with terminal end bulbs",
     why="A branching DENDRITE with swollen TERMINAL END BULBS taking up fluorescein.",
     wrong=[("Herpes zoster keratitis", "Zoster makes a PSEUDOdendrite — a raised mucous plaque with NO end bulbs — with a V1 rash."),
            ("Corneal abrasion", "That is a plain geographic patch of uptake with no branching pattern."),
            ("Corneal ulcer", "That is a dense white infiltrate in the stroma, not a surface dendrite.")]),

dict(cond="Herpes zoster keratitis", img="s057_2.jpg", slide=57, deck=D10, io=CORNEA,
     alt="Cornea under cobalt blue light showing raised pseudodendrites without end bulbs",
     why="Raised PSEUDOdendrites — heaped mucous plaques that stain poorly and carry NO terminal end bulbs.",
     wrong=[("Herpes simplex keratitis", "Simplex dendrites branch cleanly and end in bulbs that hold the dye."),
            ("Corneal abrasion", "That is a single sharply bounded area of uptake, not multiple raised plaques."),
            ("Keratitis", "That is a general term; the pattern here names the organism.")]),

dict(cond="Corneal ulcer", img="s060_1.jpg", slide=60, deck=D10, io=CORNEA,
     alt="Cornea with a dense white stromal infiltrate and ciliary flush",
     why="A dense WHITE INFILTRATE within the cornea with ciliary flush around the limbus.",
     wrong=[("Corneal abrasion", "That is an epithelial defect only — it stains, but there is no white infiltrate under it."),
            ("Herpes simplex keratitis", "That gives a branching dendrite, not a solid white patch."),
            ("Cataract", "That opacity sits in the lens behind the pupil, not in the cornea in front of the iris.")]),

dict(cond="Anterior uveitis", img="s062_4.jpg", slide=62, deck=D10, io=CORNEA,
     alt="Red eye with ciliary flush around the limbus and an irregular pupil",
     why="CILIARY FLUSH hugging the limbus with an IRREGULAR pupil, where inflammation has stuck the iris to the lens.",
     wrong=[("Bacterial conjunctivitis", "That reddens the fornices most and leaves the pupil round and reactive."),
            ("Episcleritis", "That is one sector of superficial vessels with a normal pupil."),
            ("Subconjunctival haemorrhage", "That is free blood with no injection and no pupil change.")]),

dict(cond="Hyphema", img="l14-s024_pos1.jpg", slide=24, deck=D14, io=CORNEA,
     alt="Blood layered with a flat fluid level in the anterior chamber",
     why="Blood LAYERING inside the anterior chamber with a flat fluid level in front of the iris.",
     wrong=[("Subconjunctival haemorrhage", "That blood sits on the surface, under the conjunctiva, and never forms a level."),
            ("Corneal ulcer", "That is a white infiltrate in the cornea, not free blood behind it."),
            ("Anterior uveitis", "Cells there are too fine to see; a visible layer of blood means a hyphema.")]),

dict(cond="Corneal abrasion", img="l14-s018_pos1.jpg", slide=18, deck=D14, io=CORNEA,
     alt="Cornea stained green with fluorescein over a sharply bounded epithelial defect",
     why="A sharply bounded patch of fluorescein uptake with clear cornea underneath — epithelium is missing, stroma is intact.",
     wrong=[("Corneal ulcer", "That adds a white stromal infiltrate under the defect."),
            ("Herpes simplex keratitis", "That defect branches into a dendrite with end bulbs."),
            ("Corneal foreign body", "There is no retained object here, only a denuded surface.")]),

dict(cond="Corneal foreign body", img="l14-s021_pos1.jpg", slide=21, deck=D14, io=CORNEA,
     alt="Small dark object embedded on the cornea, marked by an arrow",
     why="A discrete dark object still sitting on the cornea, with the surrounding cornea otherwise clear.",
     wrong=[("Iris nevus", "That pigment lies ON the iris behind the cornea and does not sit proud of the surface."),
            ("Corneal abrasion", "That is a missing patch of epithelium, not a retained object."),
            ("Hyphema", "That is layered blood in the anterior chamber.")]),

# ---------------------------------------------------- retina / optic nerve ----
dict(cond="Retinal detachment", img="l12-s028_1.jpg", slide=28, deck=D12, io=FUNDUS,
     alt="Fundus with a pale billowing sheet of retina lifted off the choroid",
     why="A pale, BILLOWING sheet of retina lifted off the choroid beneath it, thrown into folds.",
     wrong=[("Papilledema", "That swells the optic disc; the rest of the retina stays flat."),
            ("Age-related macular degeneration — wet", "That bleeds under the macula but the retina stays attached."),
            ("Uveal melanoma", "That is a solid pigmented dome, not a translucent mobile sheet.")]),

dict(cond="Papilledema", img="l12-s045_3.jpg", slide=45, deck=D12, io=FUNDUS,
     alt="Fundus with a swollen optic disc whose margins cannot be traced",
     why="The optic disc is swollen, its margins can no longer be traced, and the vessels bend as they climb over the edge.",
     wrong=[("Age-related macular degeneration — dry", "That is drusen at the macula, away from the disc, which stays sharp."),
            ("Retinal detachment", "That lifts the retina into folds; the disc itself is not swollen."),
            ("Uveal melanoma", "That is a discrete pigmented mass, not diffuse swelling of the nerve head.")]),

dict(cond="Age-related macular degeneration — dry", img="l13-s011_1.jpg", slide=11, deck=D13, io=FUNDUS,
     alt="Fundus with yellow drusen clustered at the macula and no haemorrhage",
     why="Yellow DRUSEN clustered at the macula, with no blood and no fluid.",
     wrong=[("Age-related macular degeneration — wet", "Wet disease adds subretinal haemorrhage or fluid; there is none here."),
            ("Papilledema", "That swells the optic disc; here the disc is sharp and the change is at the macula."),
            ("Retinal detachment", "The retina here is flat and attached.")]),

dict(cond="Age-related macular degeneration — wet", img="l13-s011_3.jpg", slide=11, deck=D13, io=FUNDUS,
     alt="Fundus with a large dark subretinal haemorrhage across the macula",
     why="A large dark SUBRETINAL HAEMORRHAGE across the macula from new vessels growing under the retina.",
     wrong=[("Age-related macular degeneration — dry", "Dry disease shows drusen and atrophy, never this volume of blood."),
            ("Retinal detachment", "That is a translucent sheet lifted into folds, not blood pooled under a flat retina."),
            ("Papilledema", "That change is centred on the disc, not the macula.")]),

dict(cond="Cataract — nuclear", img="l13-s037_1.jpg", slide=37, deck=D13, io=FUNDUS,
     alt="Lens with a uniformly yellow-brown, hardened nucleus seen through the pupil",
     why="The lens NUCLEUS has yellowed and hardened to a uniform brown-amber, filling the pupil.",
     wrong=[("Cataract — cortical", "That makes white radial spokes running in from the lens edge, not a uniform brown centre."),
            ("Corneal ulcer", "That opacity is in the cornea in front of the iris, not behind the pupil."),
            ("Retinoblastoma", "That reflects white from behind the lens, in a child.")]),

dict(cond="Cataract — cortical", img="l13-s037_2.jpg", slide=37, deck=D13, io=FUNDUS,
     alt="Lens with white radial cortical spokes running inward from the periphery",
     why="White radial SPOKES running inward from the edge of the lens, leaving the centre relatively clear.",
     wrong=[("Cataract — nuclear", "That yellows and browns the centre of the lens uniformly."),
            ("Corneal ulcer", "That white patch would sit in the cornea, in front of the iris."),
            ("Anterior uveitis", "That gives ciliary flush and an irregular pupil, not spokes in the lens.")]),

# ------------------------------------------------ pupil and eye movements ----
dict(cond="Horner syndrome", img="l11-s015_pos1.jpg", slide=15, deck=D11, io=PUPIL,
     alt="Both eyes, with a smaller pupil and a mildly drooping upper lid on one side",
     why="A SMALL pupil with a MILD ptosis on the SAME side — the sympathetic supply to that eye has been interrupted.",
     wrong=[("Cranial nerve III palsy", "That is the opposite — a LARGE pupil, a heavy ptosis and the eye turned down and out."),
            ("Adie tonic pupil", "That pupil is LARGE and reacts poorly to light but slowly to near, with no ptosis."),
            ("Argyll Robertson pupil", "Those are small and irregular in BOTH eyes, and the lids are normal.")]),

dict(cond="Cranial nerve III palsy", img="l11-s040_pos1.jpg", slide=40, deck=D11, io=PUPIL,
     alt="Marked drooping of one upper eyelid, shown before and after the lid is lifted",
     why="A heavy PTOSIS; lift the lid and the eye sits down and out, because only the lateral rectus and superior oblique still work.",
     wrong=[("Horner syndrome", "That ptosis is slight, only a millimetre or two, and comes with a SMALL pupil."),
            ("Dermatochalasis", "That is loose skin resting on the lashes; the lid itself still elevates."),
            ("Cranial nerve VI palsy", "That leaves the lid alone and only stops the eye turning outward.")]),

# ---------------------------------------------------------------- tumours ----
dict(cond="Retinoblastoma", img="l13-s041_1.jpg", slide=41, deck=D13, io=TUMOUR,
     alt="Child photographed with a white pupillary reflex in one eye and a normal red reflex in the other",
     why="LEUKOCORIA — a white pupillary reflex in one eye while the other returns a normal red reflex. In a child this is retinoblastoma until proven otherwise; a congenital cataract is the other cause and has to be excluded.",
     wrong=[("Strabismus", "That is a misaligned eye; both pupils still return a red reflex."),
            ("Amblyopia", "That is reduced vision in a structurally normal eye, with a normal red reflex."),
            ("Conjunctival melanoma", "That is a pigmented lesion on the surface of the eye, not a white reflex from behind the lens.")]),

dict(cond="Uveal melanoma", img="l13-s044_4.jpg", slide=44, deck=D13, io=TUMOUR,
     alt="Fundus montage with a raised pigmented dome-shaped choroidal mass",
     why="A raised, pigmented, DOME-SHAPED mass sitting in the choroid beneath the retina.",
     wrong=[("Age-related macular degeneration — wet", "That blood is flat and centred on the macula, not a raised solid dome."),
            ("Retinal detachment", "That sheet is pale and translucent, and moves; this mass is solid and fixed."),
            ("Iris nevus", "That pigment is on the iris at the front of the eye, visible without a fundus view.")]),

dict(cond="Iris nevus", img="l13-s048_1.jpg", slide=48, deck=D13, io=TUMOUR,
     alt="Iris with small flat well-defined brown pigmented spots",
     why="Small, FLAT, well-defined pigmented spots on the iris surface that do not distort the pupil.",
     wrong=[("Uveal melanoma", "That is raised, larger, and pulls the pupil out of shape or seeds pigment."),
            ("Conjunctival melanoma", "That pigment lies on the conjunctiva over the white of the eye, not on the iris."),
            ("Corneal foreign body", "That would sit proud of the corneal surface in front of the iris.")]),

dict(cond="Conjunctival melanoma", img="l13-s052_1.jpg", slide=52, deck=D13, io=TUMOUR,
     alt="Raised pigmented brown lesion on the conjunctiva beside the cornea",
     why="A raised, pigmented lesion growing ON the conjunctiva over the white of the eye, with feeder vessels.",
     wrong=[("Iris nevus", "That pigment lies on the iris, behind the cornea, inside the eye."),
            ("Pinguecula", "That is a pale yellow-white deposit, not brown pigment."),
            ("Subconjunctival haemorrhage", "That is red and flat and clears on its own within weeks.")]),

# ----------------------------------------------------------------- trauma ----
dict(cond="Globe rupture", img="l14-s017_pos1.jpg", slide=17, deck=D14, io=TRAUMA,
     alt="Eye held open with a speculum showing the cornea split and the globe collapsed",
     why="The eye wall has given way — the cornea is split and the globe has lost its shape and its contents are presenting.",
     wrong=[("Hyphema", "That is blood inside an intact anterior chamber; here the wall itself is open."),
            ("Corneal ulcer", "That is an infected infiltrate in a cornea that is still whole."),
            ("Orbital contusion", "That bruises the soft tissue around a globe that stays closed.")]),

dict(cond="Lid laceration", img="l14-s029_pos1.jpg", slide=29, deck=D14, io=TRAUMA,
     alt="Deep bleeding wound through the upper eyelid, shown before and after suture repair",
     why="A full-thickness wound through the eyelid, shown open and then repaired.",
     wrong=[("Periorbital haematoma", "That is closed bruising; the skin is not breached."),
            ("Pre-septal cellulitis", "That is infection and swelling of an intact lid."),
            ("Orbital contusion", "That is blunt injury to the orbital contents without an open wound.")]),

dict(cond="Orbital contusion", img="l14-s032_pos1.jpg", slide=32, deck=D14, io=TRAUMA,
     alt="Eye after blunt injury with extensive bright subconjunctival haemorrhage and lid swelling",
     why="Blunt injury has filled the surface with haemorrhage and swollen the lids, with no open wound.",
     wrong=[("Pre-septal cellulitis", "That is red, warm and infected, and follows no injury."),
            ("Post-septal cellulitis", "That pushes the globe forward and makes movement painful; this is bruising."),
            ("Dacryoadenitis", "That is gland inflammation at the outer upper lid, unrelated to trauma.")]),

dict(cond="Periorbital haematoma", img="l14-s034_pos1.jpg", slide=34, deck=D14, io=TRAUMA,
     alt="Extensive dark bruising filling the eyelids and periorbital skin on one side",
     why="Dark bruising filling the lids and the skin around the orbit after blunt injury, with the globe itself quiet.",
     wrong=[("Pre-septal cellulitis", "That is erythema and warmth from infection, not the deep purple of extravasated blood."),
            ("Post-septal cellulitis", "That comes with proptosis and painful eye movement."),
            ("Chemosis", "That is fluid swelling of the conjunctiva, not bruising of the lids.")]),

dict(cond="Orbital floor fracture", img="l14-s042_pos2.jpg", slide=42, deck=D14, io=TRAUMA,
     alt="Periorbital bruising with one eye failing to elevate on upward gaze",
     why="Periorbital bruising with the eye unable to look UP — the inferior rectus is caught in the fractured floor.",
     wrong=[("Periorbital haematoma", "Bruising alone does not restrict the eye from moving."),
            ("Cranial nerve III palsy", "That drops the lid and turns the eye down and out; here the lid works and only elevation fails."),
            ("Post-septal cellulitis", "That is infection with proptosis, not a mechanical block after injury.")]),

dict(cond="Basilar skull fracture", img="l14-s045_pos6.jpg", slide=45, deck=D14, io=TRAUMA,
     alt="Bruising over the mastoid process behind the ear",
     why="Bruising over the MASTOID behind the ear — Battle sign, which tracks blood from a fracture of the skull base.",
     wrong=[("Periorbital haematoma", "That bruising is around the eye; this sits behind the ear."),
            ("Orbital contusion", "That involves the globe and lids, not the mastoid."),
            ("Pre-septal cellulitis", "That is infection of the eyelid, in a different place entirely.")]),
]
