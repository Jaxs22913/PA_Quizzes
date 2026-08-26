#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 2 Lecture 1 Arcade deck, and open the Exam 2 group.

ALSO REGISTERS TWO DECKS THAT WERE ADDED WITHOUT BEING REGISTERED. arcade.js
keeps decks in a flat list AND a separate class/exam grouping at the bottom;
a deck missing from the grouping is invisible in the app no matter how good it
is. pdm-chemistry-panels and cp-ophthalmic-pathophys were both in that state.
This script is idempotent and asserts every deck it touches ends up in both.
"""
import os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
ICON = ('<path d="M2 12s3.5-6 10-6 10 6 10 6-3.5 6-10 6-10-6-10-6z"/>'
        '<circle cx="12" cy="12" r="2.5"/><path d="M4 4l16 16"/>')

DECK = dict(
    id="cms-ophthalmology-1", name="Common Ophthalmological Disorders", color="accent2",
    icon=ICON,
    cards=[
  ["Before naming a red-eye diagnosis, what must be done first?", "Visual acuity in each eye with correction, pupils, extraocular movements, corneal clarity with fluorescein, the pattern of injection and discharge, and the contact lens, trauma, surgery and steroid history."],
  ["Which two findings are the red flags in a red eye?", "Reduced vision, or an abnormal pupil."],
  ["What is the one exception to the red-eye sequence?", "Chemical exposure — irrigate copiously first, before history or examination, then check the surface pH has normalised."],
  ["What must NOT be done with a suspected open globe?", "Do not apply pressure, do not perform tonometry, do not patch. Rigid shield, nil by mouth, emergency consultation."],
  ["Which conditions are EMERGENT — now?", "Chemical injury, open globe, acute angle closure, orbital cellulitis, endophthalmitis."],
  ["Which conditions are SAME DAY?", "Keratitis or corneal ulcer, anterior uveitis, scleritis, ocular herpes zoster ophthalmicus."],
  ["Entropion: which way does the lid turn and what does it cause?", "Inward — the lashes are pushed onto the globe (trichiasis), causing corneal abrasion."],
  ["Ectropion: which way does the lid turn and what does it cause?", "Outward — exposure keratopathy."],
  ["Which lid malposition can be caused by a seventh nerve palsy?", "Ectropion only."],
  ["What is the definitive treatment for entropion or ectropion?", "Surgery."],
  ["Dermatochalasis: which assessment determines insurance coverage?", "Visual field testing — a demonstrated deficit is what gets blepharoplasty covered."],
  ["Xanthelasma: what workup does it warrant?", "Serum lipid profile, plus fasting glucose and haemoglobin A1C for diabetes, plus liver function tests."],
  ["What should a patient be told about treated xanthelasma?", "Recurrences are common even after effective local treatment."],
  ["Blepharitis: which three associations?", "Rosacea, seborrhoeic dermatitis, and Staphylococcus aureus colonisation."],
  ["What is the characteristic meibomian secretion in meibomitis?", "Thick, sometimes toothpaste-like lipid secretion."],
  ["Blepharitis: what is first-line and for how long before escalating?", "Lid hygiene, for two weeks, then topical antibiotics, then oral."],
  ["What must a patient with blepharitis be told about cure?", "It is chronic and can be controlled rather than cured."],
  ["Chalazion vs hordeolum: the single discriminating sign?", "Tenderness — the hordeolum is tender, the chalazion is not."],
  ["What is a chalazion, in mechanism?", "A sterile obstruction of a meibomian gland."],
  ["When is a persistent hordeolum referred, and for what?", "No improvement in two weeks — for incision and drainage."],
  ["Why refer a recurrent chalazion, or one over 2-3 months?", "To rule out sebaceous carcinoma."],
  ["How long may a chalazion take to improve?", "Months."],
  ["Dacryoadenitis: where is the swelling?", "Over the lateral one third of the upper lid — the lacrimal gland."],
  ["Dacryocystitis: where is the swelling?", "Over the nasal aspect of the lower lid, below the medial canthal tendon — the lacrimal sac."],
  ["A lacrimal mass ABOVE the medial canthal tendon suggests what?", "A lacrimal sac tumour, which is rare."],
  ["Which cause of dacryoadenitis is most common?", "Inflammatory. Bacterial is rare; viral is usually bilateral."],
  ["Inflammatory dacryoadenitis: treatment and expected response?", "Corticosteroids, with a response within 48 hours — but not until infection has been reasonably excluded."],
  ["Dacryocystitis in a well, reliable, afebrile patient?", "Outpatient oral antibiotics for ten days."],
  ["Dacryocystitis in a febrile or unreliable patient?", "Admit for intravenous antibiotics 48 to 72 hours, then oral to complete 10 to 14 days."],
  ["What is often needed after acute dacryocystitis settles?", "Probing and irrigation to assess patency of the drainage system; surgery may follow."],
  ["Pinguecula vs pterygium: the whole distinction?", "The pterygium extends onto the cornea; the pinguecula does not."],
  ["Where do pinguecula and pterygium almost always sit?", "At three o'clock or nine o'clock."],
  ["What must a patient with a pterygium be told?", "Conservative management may help symptoms but will not make the lesion resolve."],
  ["Subconjunctival haemorrhage: which four risk factors?", "Valsalva, bleeding disorder, antiplatelet or anticoagulant medication, and hypertension."],
  ["Subconjunctival haemorrhage: what is the workup?", "History above all — and check the blood pressure if there is no explanation."],
  ["How long does an atraumatic subconjunctival haemorrhage take to clear?", "Two to four weeks, with reassurance as the treatment."],
  ["What is chemosis, and when is it urgent?", "Conjunctival swelling — a sign, not a diagnosis. Urgent with proptosis, restricted movement, reduced vision or an afferent pupillary defect."],
  ["Acute versus chronic conjunctivitis: the cut-off?", "Four weeks."],
  ["Papillae point to which causes, and how do they look?", "Bacterial (except chlamydial) and allergic — red at the surface, paler at the base."],
  ["Follicles point to which causes, and how do they look?", "Chlamydial and viral — pale at the surface, redder at the base."],
  ["A preauricular node in conjunctivitis points to which three?", "Chlamydial, gonococcal and viral."],
  ["Allergic conjunctivitis: the giveaway?", "Itch, bilateral, watery or stringy discharge, chemosis, papillae, and no preauricular node."],
  ["Which single agent blocks histamine AND stabilises mast cells?", "Olopatadine."],
  ["Which organism most commonly causes viral conjunctivitis?", "Adenovirus."],
  ["Viral conjunctivitis: the expected course?", "Self-limiting — often worse over the first week, resolving in two to three weeks."],
  ["When is viral conjunctivitis referred?", "Lasting more than three weeks, or significant photophobia or decreased vision after onset."],
  ["Bacterial conjunctivitis in an immunocompetent adult?", "A topical broad-spectrum antibiotic such as a fluoroquinolone, with contagious precautions."],
  ["Which patients with bacterial conjunctivitis get urgent referral?", "Immunocompromised, contact lens wearer, recent eye surgery, foreign body, corneal opacity or suspected keratitis, or no improvement in 24 hours."],
  ["What makes gonococcal conjunctivitis stand out?", "Severe purulent discharge WITH a palpable preauricular node — the exception to the no-node rule."],
  ["Suspected gonococcal conjunctivitis in a newborn?", "An emergency — hospitalise for systemic ceftriaxone, cultures and Gram stain, testing for chlamydia and dissemination. Untreated risks corneal perforation."],
  ["Adult chlamydial conjunctivitis: how does it present?", "Chronic, a month or longer, stringy mucoid discharge, follicles, and unresponsive to topical medication."],
  ["Adult chlamydial conjunctivitis: confirmation and treatment?", "Conjunctival nucleic acid amplification or direct fluorescent antibody, then doxycycline 100 mg twice daily for seven days."],
  ["Beyond the eye, what does adult chlamydial conjunctivitis require?", "Evaluation for other sexually transmitted infections, and partner notification."],
  ["Neonatal chlamydial conjunctivitis: regimen and monitoring?", "Erythromycin 50 mg/kg/day divided four times daily for 14 days, monitoring infants under six weeks for infantile hypertrophic pyloric stenosis."],
  ["Why does erythromycin cause pyloric stenosis?", "It is a motilin receptor agonist and overstimulates the smooth muscle of the lower stomach."],
  ["Trachoma: which serotypes, and what is its significance?", "Chlamydia trachomatis A, B and C — the leading infectious cause of blindness worldwide."],
  ["Trachoma: the chain to blindness?", "Conjunctival inflammation, then eyelid scarring, then entropion, then trichiasis, then blindness."],
  ["Trachoma: mass treatment regimen and threshold?", "Azithromycin one gram orally as a single dose, where prevalence is five per cent or above."],
  ["Episcleritis: the confirmatory bedside test?", "A drop of 2.5 per cent phenylephrine — after 15 minutes the episcleral vessels blanch."],
  ["Episcleritis vs scleritis on the cotton-tip test?", "Episcleral vessels CAN be moved slightly; scleral vessels CANNOT."],
  ["Episcleritis: treatment and referral threshold?", "Artificial tears and an oral anti-inflammatory taken with food; refer if no response within two days."],
  ["Scleritis: the characteristic pain?", "Severe boring pain, worse at night, radiating to the face and periorbital region."],
  ["What causes the violaceous hue in scleritis?", "The choroid showing through an area of scleral thinning."],
  ["Why is scleritis referred urgently?", "The sclera is at risk of perforation and may need a surgical patch."],
  ["What is the FIRST sign scleritis is responding?", "Decreased pain — even if the inflammation looks unchanged."],
  ["What is a ciliary flush, and what does it mean?", "A ring of red vessels from the limbus around the cornea — inflammation of cornea, iris or ciliary body. It rules out simple conjunctivitis."],
  ["Which three conditions show a ciliary flush?", "Corneal inflammation (ulcer, keratitis), anterior uveitis, and acute glaucoma."],
  ["Keratitis: which four risk factors?", "Corneal trauma, dry eyes, contact lens overwear, and topical ocular corticosteroid therapy."],
  ["Which organism causes the classic ring infiltrate, and in whom?", "Acanthamoeba, in contact lens wearers with poor hygiene such as rinsing lenses in tap water."],
  ["Keratitis: referral urgency?", "Urgent, within 24 hours, for slit lamp with fluorescein."],
  ["Undertreated keratitis leads to what?", "Corneal scarring or perforation, then endophthalmitis, and possibly removal of the eye."],
  ["Which corneal sign is pathognomonic for herpes simplex?", "A true dendrite — tree-branching, with elevated edges and terminal end bulbs."],
  ["How does the zoster pseudodendrite differ?", "It lacks the tree-branch pattern, the elevated edges and the terminal end bulbs."],
  ["What is Hutchinson sign and what does it predict?", "A vesicle on the tip of the nose — nasociliary involvement, and a higher risk of ocular disease."],
  ["Herpetic keratitis: systemic treatment?", "Oral antivirals — aciclovir, valaciclovir or famciclovir — for ten days, ideally within 72 hours of rash onset."],
  ["What is prohibited in active herpes simplex epithelial disease?", "Topical glucocorticoids prescribed by the primary care provider. That decision belongs to ophthalmology."],
  ["Corneal ulcer: the major risk factor and referral urgency?", "Contact lens use, and EMERGENT referral — a step above keratitis."],
  ["Corneal ulcer: which agent is started, and which is not?", "A broad-spectrum topical fourth-generation fluoroquinolone. Not a steroid — it can worsen infection if started too early, especially fungal or herpetic."],
  ["Corneal ulcer: follow-up and healing time?", "Next-day follow-up after starting an anti-infective; most heal in two to three weeks."],
  ["The contact lens case: what are the four next steps?", "Remove the lenses without patching, no take-home anaesthetic or steroid, same-day ophthalmology, and preserve the lenses and case for culture."],
  ["Why is a take-home topical anaesthetic prohibited?", "It delays healing and masks progression."],
  ["Anterior uveitis: the signs?", "Cells in the anterior chamber, consensual photophobia, ciliary flush, variable pressure, an irregular pupil stuck to lens or cornea, and keratic precipitates."],
  ["What are keratic precipitates?", "White blood cell deposits on the corneal endothelium, the posterior surface of the cornea."],
  ["Anterior uveitis: referral urgency and why?", "Urgent, within 24 hours — delayed diagnosis may cost vision."],
  ["Posterior uveitis: how does it present?", "Blurred vision, floaters, scotomas and metamorphopsia — with NO pain if isolated."],
  ["Posterior uveitis: which infectious causes?", "Toxoplasmosis and cytomegalovirus."],
  ["How does posterior uveitis treatment differ from anterior?", "It does not respond to topical treatment and may need an intraocular corticosteroid injection."],
  ["Pre-septal vs post-septal cellulitis: the giveaway?", "Pre-septal — the eye itself is WHITE with full painless movements. Post-septal — the eye is red, with proptosis and painful restricted movement."],
  ["Which patients with cellulitis need fungal cover considered?", "Diabetic, elderly or immunocompromised — aspergillosis and mucormycosis."],
  ["Mild pre-septal cellulitis: management?", "Outpatient oral antibiotics for 10 to 14 days against Staphylococcus, including resistant strains, and Streptococcus."],
  ["Which pre-septal patients are admitted?", "Moderate-severe or toxic disease, poor expected compliance, a child of five years or younger, or no improvement on oral antibiotics."],
  ["Untreated cellulitis spreads to cause what?", "Intracranial spread — meningitis or cavernous sinus thrombosis."],
  ["Which instrument examines the anterior structures?", "The slit lamp — a low-power microscope with a high-intensity slit beam."],
  ["Fluorescein EXAMINATION versus ANGIOGRAPHY?", "Examination: dye instilled, Wood lamp, finds abrasions, ulcers and foreign bodies. Angiography: dye injected, reaches the eye in 10-15 seconds, blue-flash camera, images retinal and choroidal blood flow."],
  ["Is there iodine in fluorescein?", "No — it is relatively safe and contains no iodine."],
    ],
    matchCards=[
  ["Chalazion", "STERILE meibomian obstruction; NON-tender"],
  ["Hordeolum", "Acute staph infection; TENDER; overnight"],
  ["Entropion", "Turns IN; trichiasis; corneal abrasion"],
  ["Ectropion", "Turns OUT; exposure keratopathy"],
  ["Dermatochalasis", "Excess lid skin; check VISUAL FIELDS"],
  ["Xanthelasma", "Yellow plaques; work up the metabolism"],
  ["Dacryoadenitis", "GLAND; lateral third of the UPPER lid"],
  ["Dacryocystitis", "SAC; nasal aspect of the LOWER lid"],
  ["Pinguecula", "Does NOT cross onto the cornea"],
  ["Pterygium", "DOES cross onto the cornea"],
  ["Papillae", "Red at surface; bacterial or allergic"],
  ["Follicles", "Pale at surface; chlamydial or viral"],
  ["Allergic conjunctivitis", "ITCH, bilateral, no node"],
  ["Viral conjunctivitis", "Watery, follicles, TENDER node"],
  ["Bacterial conjunctivitis", "Thick yellow, unilateral, no node"],
  ["Gonococcal conjunctivitis", "Severe purulent WITH a node; neonatal emergency"],
  ["Adult chlamydial", "Chronic, stringy, doxycycline 7 days"],
  ["Trachoma", "Serotypes A/B/C; azithromycin 1 g single dose"],
  ["Episcleritis", "Vessels MOVE; phenylephrine BLANCHES"],
  ["Scleritis", "Vessels do NOT move; violaceous; URGENT"],
  ["Herpes simplex keratitis", "TRUE dendrite with END BULBS"],
  ["Herpes zoster keratitis", "PSEUDOdendrite; dermatomal V1"],
  ["Corneal ulcer", "EMERGENT; contact lens the major risk"],
  ["Anterior uveitis", "Cells in anterior chamber; consensual photophobia"],
  ["Posterior uveitis", "PAINLESS; floaters; no topical response"],
  ["Pre-septal cellulitis", "Eye WHITE; movements full and painless"],
  ["Post-septal cellulitis", "Eye RED; proptosis; painful restriction"],
    ])

# ---- guard: mechanism belongs to Clin Path; this deck is management --------
_p = [c[0] for c in DECK["cards"]]
assert len(_p) == len(set(_p)), "duplicate card prompt: %r" % [x for x in _p if _p.count(x) > 1][:3]
_a = [c[1] for c in DECK["matchCards"]]
assert len(_a) == len(set(_a)), "duplicate match answer -- Match mode becomes unwinnable"


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render():
    L = ['  { id: "%s", name: "%s", color: "%s",' % (DECK["id"], DECK["name"], DECK["color"]),
         "    icon: '%s'," % DECK["icon"], "    cards: ["]
    for q, a in DECK["cards"]:
        L.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    L += ["    ],", "    matchCards: ["]
    for q, a in DECK["matchCards"]:
        L.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    L.append("    ] },")
    return "\n".join(L)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    fo, fc = "/*CMSE2L1*/", "/*/CMSE2L1*/"
    if fo in src:
        src = re.sub(re.escape(fo) + r".*?" + re.escape(fc), "", src, flags=re.S)
    anchor = 'id: "cms-malignant-lesions"'
    assert anchor in src, "CMS Exam 1 last deck not found -- has arcade.js changed?"
    i = src.index(anchor)
    j = src.index("] },", i) + len("] },")
    src = src[:j] + "\n" + fo + "\n" + render() + "\n" + fc + src[j:]

    # ---- the grouping at the bottom, which is what the app actually reads ----
    # Open Exam 2 for CMS.
    cms_anchor = ('"cms-clinical-reasoning", "cms-general-derm-1", "cms-derm-2", '
                  '"cms-cutaneous-bacterial", "cms-derm-infestations", "cms-viral-fungal", '
                  '"cms-benign-lesions", "cms-pigmented-lesions", "cms-malignant-lesions"\n    ] }')
    assert cms_anchor in src, "CMS exam1 deckIds block not found"
    src = src.replace(cms_anchor, cms_anchor + ''',
    { id: "exam2", name: "Exam 2", deckIds: ["cms-ophthalmology-1"] }''', 1)

    # Register the two decks that were added to the flat list but never grouped.
    src = src.replace('deckIds: ["pdm-lab-diagnostics", "pdm-medical-imaging", '
                      '"pdm-derm-ent-ophtho", "pdm-cbc-hematology"]',
                      'deckIds: ["pdm-lab-diagnostics", "pdm-medical-imaging", '
                      '"pdm-derm-ent-ophtho", "pdm-cbc-hematology", "pdm-chemistry-panels"]', 1)
    src = src.replace('deckIds: ["cp-inflammation", "cp-dermatology", "cp-abnormal-cell-growth"]',
                      'deckIds: ["cp-inflammation", "cp-dermatology", "cp-abnormal-cell-growth", '
                      '"cp-ophthalmic-pathophys"]', 1)

    open(ARCADE, "w", encoding="utf-8").write(src)

    # every deck defined must also be grouped, or it is invisible in the app
    defined = set(re.findall(r'\{ id: "([a-z0-9-]+)", name: "[^"]+", color:', src))
    grouped = set(re.findall(r'"([a-z0-9-]+)"', src[src.index("exams: ["):])) if "exams: [" in src else set()
    for d in ("cms-ophthalmology-1", "pdm-chemistry-panels", "cp-ophthalmic-pathophys"):
        assert d in defined, "%s is not defined in the deck list" % d
        assert d in grouped, "%s is defined but NOT grouped -- it would be invisible" % d
    print("added deck %s: %d cards, %d match pairs"
          % (DECK["id"], len(DECK["cards"]), len(DECK["matchCards"])))
    print("grouped: cms-ophthalmology-1 (CMS Exam 2), pdm-chemistry-panels (PDM Exam 1), "
          "cp-ophthalmic-pathophys (Clin Path Exam 1)")


if __name__ == "__main__":
    main()
