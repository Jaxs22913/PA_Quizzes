#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Clin Path I Lecture 5 (ENT) Arcade deck.

MECHANISM ONLY -- no card asks what to do about anything. CMS I Exam 3 covers
this same condition list from the management side, and slide 23 puts an
epistaxis MANAGEMENT column right beside the pathophysiology. Guarded below.

BOTH LIVE SLIDE CORRECTIONS ARE CARDED AS THE CORRECTION, not as the slide:
labyrinthitis gives CONTINUOUS vertigo (he fixed slide 17 aloud, twice), and
the polyp heading means T HELPER CELL type 2 (he fixed slide 21 aloud). A card
that taught the uncorrected slide would be worse than no card.

Arcade has no image support, so the recognition half -- what otitis externa or
a nasal polyp looks like -- lives in the guide's eleven figures. This is the
verbal half.
"""
import os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# an ear
ICON = ('<path d="M6 9a6 6 0 1 1 12 0c0 2.5-1.5 3.5-2.5 4.5S14 15.5 14 17a3 3 0 0 1-6 0"/>'
        '<path d="M10 9a2 2 0 1 1 4 0c0 1-1 1.5-1.5 2.5"/>')

DECK = dict(
    id="cp-ent-pathophys",
    name="ENT Pathophysiology",
    color="accent2",
    icon=ICON,
    cards=[
  # --- anatomy and transduction ---
  ["What are the three compartments of the ear, outside in?", "The external ear, the middle ear and the inner ear."],
  ["What does the external ear do?", "Captures and concentrates acoustic waves, and localises sound."],
  ["What is unusual about the middle ear, and why does it matter?", "It is AIR-FILLED — which is why absorbed gas creates negative pressure when the Eustachian tube stops opening."],
  ["Name the three ossicles in order.", "Malleus, incus, stapes."],
  ["What does the Eustachian tube do?", "Equalises pressure across the tympanic membrane."],
  ["Which part of the inner ear converts fluid displacement into neural signal?", "The cochlea, at the organ of Corti."],
  ["What starts the transduction chain?", "Stapes vibration at the oval window, generating pressure waves in the scala vestibuli."],
  ["What physically opens the tip-link channels?", "Shearing of the stereocilia against the RIGID tectorial membrane."],
  ["Why does the tectorial membrane have to be rigid?", "The cilia bend because one end moves and the other does not."],
  ["What depolarises the cochlear hair cell?", "Rapid ion influx from the endolymph through the opened tip-link channels."],
  ["What does the hair cell release, and onto what?", "Glutamate, onto cranial nerve VIII fibres."],
  ["Break step one of the transduction chain — what kind of hearing loss?", "Conductive."],
  ["Break steps two to four — what kind of hearing loss?", "Sensorineural."],
  # --- conductive vs sensorineural ---
  ["Where does conductive hearing loss sit?", "The external or middle ear."],
  ["Where does sensorineural hearing loss sit?", "The inner ear (cochlea), or cranial nerve VIII and central pathways."],
  ["What is the defect in conductive loss?", "Defective sound wave transmission to the oval window."],
  ["What is the defect in sensorineural loss?", "Destruction of hair cells or auditory nerve fibres."],
  ["Which way does Weber lateralise in CONDUCTIVE loss?", "To the AFFECTED ear."],
  ["Which way does Weber lateralise in SENSORINEURAL loss?", "To the UNAFFECTED ear."],
  ["Why does Weber go to the bad ear in conductive loss?", "The blockage stops competing room noise reaching that cochlea, so the bone-conducted tone has that ear to itself."],
  ["What does Rinne show in conductive loss?", "Bone conduction greater than air — abnormal."],
  ["What does Rinne show in sensorineural loss?", "Air conduction greater than bone — the normal ratio."],
  ["Name the conductive causes on the slide.", "Cerumen impaction, otosclerosis, otitis media, tympanic membrane perforation."],
  ["Name the sensorineural causes on the slide.", "Presbycusis, ototoxic drugs, noise trauma, acoustic neuroma."],
  ["What are the four core mechanisms of conductive loss?", "Obstruction, mass loading, stiffness, and discontinuity."],
  ["Impacted cerumen, foreign bodies and canal exostoses — which mechanism?", "Obstruction."],
  ["Middle ear effusion and cholesteatoma — which mechanism?", "Mass loading."],
  ["Otosclerosis — which mechanism?", "Stiffness."],
  ["Temporal bone fracture and ossicular necrosis — which mechanism?", "Discontinuity."],
  ["How do mass loading and stiffness differ?", "Mass loading adds weight to a chain that can still move; stiffness stops the chain moving at all."],
  ["What is a cholesteatoma?", "A cholesterol collection forming a small mass in the ear — off-deck, but he said to know it. It sits under mass loading."],
  # --- otosclerosis ---
  ["What is the bone remodelling sequence in otosclerosis?", "Abnormal osteoclastic resorption, then hypervascular spongy osteoid replacement."],
  ["Where does otosclerosis remodel?", "Around the otic capsule and the stapes footplate."],
  ["Which single event in otosclerosis causes the hearing loss?", "Ankylosis of the stapes footplate in the oval window."],
  ["Why is otosclerosis conductive and not sensorineural?", "The cochlea is untouched — only the mechanical chain is fixed."],
  ["Who gets otosclerosis?", "Young-to-middle-aged females, and pregnancy accelerates it."],
  ["What is the inheritance pattern of otosclerosis?", "50% autosomal dominant with variable penetrance."],
  # --- ototoxicity and noise ---
  ["What is the sorting rule for ototoxic drugs?", "Almost always reversible — except platinum chemotherapy."],
  ["How do gentamicin and tobramycin damage hearing?", "They induce reactive oxygen species that selectively destroy outer hair cells."],
  ["Where does aminoglycoside damage start, and which pitches go first?", "At the cochlear base — so high pitches go first."],
  ["How does cisplatin cause permanent bilateral loss?", "It cross-links DNA in stria vascularis cells, compromising endolymph ion homeostasis."],
  ["What does furosemide do to the ear?", "Alters the stria vascularis potential — reversible."],
  ["What does salicylate inhibit, and what results?", "The prestin motor protein in outer hair cells — tinnitus."],
  ["Cisplatin and furosemide hit the same structure. Which?", "The stria vascularis."],
  ["Why is one permanent and the other not?", "Cisplatin cross-links the cells' DNA and kills them; furosemide only shifts their electrical potential."],
  ["Why do high frequencies go first, anatomically?", "The cochlear base encodes high pitch, and the base is where the damage begins."],
  ["Above what level does chronic noise cause irreversible damage?", "85 decibels."],
  ["What is the cellular change from chronic noise?", "Stereocilia degeneration and acoustic hair cell apoptosis."],
  ["At what level is damage immediate?", "140 decibels — a jet engine or a blast."],
  ["What is the pattern of presbycusis?", "Gradual, symmetrical, bilateral sensorineural loss in older adults."],
  ["Which frequencies does presbycusis take first?", "High frequencies — the speech consonants."],
  ["Why does presbycusis wreck conversation rather than volume?", "Vowels carry the volume, consonants carry the meaning — and it is the consonants that go."],
  # --- otitis ---
  ["What is the sequence of Eustachian tube dysfunction?", "The tube fails to open periodically, so oxygen and nitrogen are absorbed into the middle ear mucosa, creating negative pressure."],
  ["Which bacteria most commonly cause otitis media?", "Streptococcus pneumoniae, Haemophilus influenzae and Moraxella catarrhalis."],
  ["Which viruses cause otitis media?", "Respiratory syncytial virus, rhinovirus, influenza and adenovirus."],
  ["Which bacteria cause 80 to 90 per cent of otitis externa?", "Pseudomonas aeruginosa and Staphylococcus aureus."],
  ["Which fungi cause otitis externa?", "Aspergillus niger and Candida albicans."],
  ["What predisposes to fungal otitis externa?", "Prolonged antibiotic use, or hyperhumid conditions."],
  # --- balance ---
  ["What do the semicircular canals detect?", "Rotational acceleration of the head."],
  ["How do the semicircular canals detect it?", "Endolymph inertia bends the gelatinous cupula inside the ampulla, stimulating hair cell stereocilia."],
  ["In which planes do the three semicircular canals sit?", "Sagittal, coronal and transverse."],
  ["Which organs detect linear acceleration and gravitational position?", "The otolith organs — the utricle and the saccule."],
  ["What are the orientations of the utricle and saccule?", "Utricle horizontal, saccule vertical."],
  ["Canals and otoliths answer different questions. Which?", "Canals answer 'am I turning?'; otoliths answer 'which way is down?'"],
  # --- vertigo ---
  ["What is vertigo?", "A hallucination of motion — spinning, tilting, tumbling — from asymmetrical vestibular input."],
  ["What accompanies vertigo, and what is explicitly absent?", "Nystagmus and ataxia. NO syncope."],
  ["What drives dizziness, as opposed to vertigo?", "Cerebral hypoperfusion, orthostatic hypotension, or metabolic imbalance."],
  ["Why is 'no syncope' the clean discriminator?", "Vertigo is a false motion signal with normal perfusion; dizziness IS the perfusion or metabolic problem."],
  ["Where does PERIPHERAL vertigo come from?", "The inner ear or cranial nerve VIII."],
  ["What is the nystagmus of peripheral vertigo like?", "Horizontal or rotational, fatigable, and suppressed by visual fixation."],
  ["Where does CENTRAL vertigo come from?", "The brainstem or cerebellum."],
  ["What is the nystagmus of central vertigo like?", "Vertical or non-suppressible — and neurological deficits are present."],
  ["Name the central vertigo causes.", "Brainstem stroke, multiple sclerosis and cerebellar tumour."],
  ["Why does visual fixation suppress peripheral vertigo but not central?", "Vision can outvote a false peripheral signal; a central lesion has broken the machinery that does the voting."],
  ["Name the four peripheral vertigos.", "Benign paroxysmal positional vertigo, Ménière disease, labyrinthitis, and vestibular neuritis."],
  ["What is the mechanism of Ménière disease?", "Endolymphatic hydrops — defective endolymph RESORPTION, ballooning the scala media until micro-ruptures occur."],
  ["In Ménière, is production or drainage at fault?", "Drainage. Production is normal."],
  ["What is the classic tetrad of Ménière disease?", "Episodic vertigo lasting hours, low-frequency fluctuating tinnitus, progressive low-tone sensorineural loss, and aural fullness."],
  ["How long does Ménière vertigo last?", "Hours."],
  ["Which frequencies does Ménière take, and why does that matter?", "LOW tones — every other sensorineural loss here starts high."],
  ["What is the mechanism of labyrinthitis?", "Inflammatory swelling, vascular congestion and endolymphatic disruption across the semicircular canals AND the cochlea."],
  ["Why do hearing and balance fail together in labyrinthitis?", "One continuous fluid space serves both organs, so inflammation anywhere in it disturbs both."],
  ["What causes labyrinthitis?", "Viral infection — typically a recent viral upper respiratory infection."],
  ["Is the vertigo of labyrinthitis episodic or continuous?", "CONTINUOUS — the slide says episodic and he corrected it aloud, twice."],
  ["How long does labyrinthitis vertigo run?", "Days, improving slowly over weeks."],
  ["Why does the labyrinthitis correction matter?", "Episodic vertigo lasting hours is Ménière — if labyrinthitis were episodic too, the axis that separates them would collapse."],
  ["Which way does labyrinthitis nystagmus beat?", "Horizontal-rotary, with the fast phase beating AWAY from the affected side."],
  ["What separates vestibular neuritis from labyrinthitis?", "Neuritis inflames the nerve fibres only, so hearing is spared. That is the only difference."],
  ["What is canalithiasis?", "Dislodged otoconia floating free in the semicircular canals."],
  ["Where do otoconia normally sit?", "In the utricle."],
  ["How long does benign paroxysmal positional vertigo last?", "Under one minute."],
  ["What triggers benign paroxysmal positional vertigo?", "Positional changes of the head."],
  ["Which feature separates benign paroxysmal positional vertigo most cleanly?", "There is NO hearing loss."],
  ["Why is there no hearing loss in benign paroxysmal positional vertigo?", "The cochlea is nowhere near the problem — the crystals are in the canals."],
  # --- rhinology ---
  ["What is the difference between rhinitis and rhinosinusitis?", "Rhinitis is the nose; rhinosinusitis is the nose and the sinuses."],
  ["How long is ACUTE rhinosinusitis?", "Under four weeks."],
  ["How long is CHRONIC rhinosinusitis?", "Beyond twelve weeks despite therapy."],
  ["What commonly accompanies chronic rhinosinusitis?", "Nasal polyps."],
  ["What usually causes acute rhinosinusitis?", "Viral infection — rhinovirus or influenza; secondary bacterial is Streptococcus pneumoniae or Haemophilus influenzae."],
  ["What kind of immune reaction is allergic rhinitis?", "IgE-mediated type 1 hypersensitivity."],
  ["What does allergic rhinitis look like?", "CLEAR rhinorrhoea, nasal itching, sneezing, boggy turbinates and allergic 'shiners'."],
  ["Clear discharge or purulent — which is allergic?", "Clear. Purulent points to acute bacterial sinusitis."],
  ["What are nasal polyps made of?", "Non-neoplastic, benign oedematous masses from the mucous membranes of the sinus ostia or ethmoid air cells."],
  ["Why does 'non-neoplastic' matter for polyps?", "No new tissue is being grown — existing mucosa is waterlogged."],
  ["Which cytokines drive nasal polyps?", "Interleukins 4, 5 and 13."],
  ["Which cell floods the tissue in nasal polyps?", "Eosinophils."],
  ["The polyp slide says 'Type 2 Inflammation'. What did he correct it to?", "T HELPER CELL type 2 allergic inflammation."],
  ["What enlarges the inferior turbinates?", "Venous sinusoid engorgement, mucosal oedema, or bony hypertrophy."],
  ["What is rhinitis medicamentosa?", "Rebound hyperaemia from overuse of topical decongestant sprays."],
  ["Which physical law governs a deviated septum?", "Poiseuille's law — small narrowing raises resistance dramatically."],
  ["Why does a deviated septum cause epistaxis?", "Turbulent air currents dry the mucosa, causing localised crusting and fragile vessel breakdown."],
  ["Why does a deviated septum cost the sense of smell?", "Airflow fails to reach the superior nasal vault and the cribriform plate."],
  ["What happens to the WIDE side of a deviated nose?", "Compensatory inferior turbinate hypertrophy, to humidify the increased air volume."],
  ["Which turbinate hypertrophies — the blocked side or the open side?", "The OPEN side. So a one-sided deviation can end up obstructing both."],
  ["What does sinus ostia blockage lead to?", "Mucus stasis, hypoxia, and secondary bacterial rhinosinusitis."],
  ["Which plexus bleeds in ANTERIOR epistaxis, and how often?", "Kiesselbach's plexus on the anterior septum — about 90 per cent of cases."],
  ["Which plexus bleeds in POSTERIOR epistaxis, and how often?", "Woodruff's plexus on the posterolateral wall — about 10 per cent."],
  ["What causes anterior epistaxis?", "Digital trauma, low humidity, localised mucosal erosion and mild rhinitis — all local."],
  ["What causes posterior epistaxis?", "Hypertension, atherosclerosis, anticoagulant therapy and coagulopathy — all systemic."],
  ["Why is posterior epistaxis the dangerous one?", "Woodruff's plexus carries far more arterial supply, and the bleeding runs down the posterior pharynx — an airway risk."],
  # --- larynx and neck ---
  ["Where do vocal cord NODULES sit?", "Bilaterally and symmetrically, at the junction of the anterior third and posterior two thirds."],
  ["What causes vocal cord nodules?", "Chronic mechanical phonotrauma — cords slamming together from yelling or cheering."],
  ["What tissue change makes a nodule?", "Basement membrane hyalinisation."],
  ["Where do vocal cord POLYPS sit?", "Unilaterally, on the middle third of the true cord."],
  ["What causes vocal cord polyps?", "Acute severe voice strain or vocal cord haemorrhage."],
  ["Nodules or polyps — which is bilateral?", "Nodules. Polyps are unilateral."],
  ["Why are nodules bilateral and polyps unilateral?", "Repeated impact damages both cords at the same point; one violent strain or bleed damages one."],
  ["What is the usual bacterial cause of tonsillitis?", "Group A Streptococcus."],
  ["Which tonsils does tonsillitis inflame?", "The palatine tonsils."],
  ["What is odynophagia?", "Pain on swallowing."],
  ["Which tonsillar finding suggests an abscess?", "Asymmetric tonsillar deviation, with trismus."],
  ["Why is asymmetry the alarm in tonsillitis?", "Tonsillitis is symmetrical; an abscess pushes one tonsil across the midline."],
  ["White patches on red swollen tonsils — bacterial or viral?", "Bacterial. Redness and swelling with no exudate points viral."],
  ["What usually causes cervical lymphadenopathy?", "Reactive enlargement to regional head and neck infection — viral upper respiratory infection, otitis media, dental disease — or systemic inflammation."],
  ["Which nodal findings demand assessment for lymphoma?", "Persistent, rubbery or matted, supraclavicular or cervical nodes in an older adult."],
  ["Tender and soft, or painless and matted — which is reactive?", "Tender and soft. Matted means the nodes have lost their individual capsules and move as one mass."],
    ],
    matchCards=[
  ["BPPV", "Otoconia loose in the canals; under 1 minute; NO hearing loss"],
  ["Ménière disease", "Endolymphatic hydrops; HOURS; low-tone loss and aural fullness"],
  ["Labyrinthitis", "Canals AND cochlea inflamed; CONTINUOUS, days; after a viral URI"],
  ["Vestibular neuritis", "Nerve fibres only; hearing spared"],
  ["Otosclerosis", "Stapes footplate ankylosed; stiffness; conductive"],
  ["Presbycusis", "Gradual bilateral loss; HIGH frequencies; consonants first"],
  ["Aminoglycosides", "Reactive oxygen species kill outer hair cells from the base"],
  ["Cisplatin", "Cross-links stria vascularis DNA; permanent and bilateral"],
  ["Furosemide", "Shifts the stria vascularis potential; reversible"],
  ["Salicylates", "Inhibit prestin in outer hair cells; tinnitus"],
  ["Obstruction", "Impacted cerumen, foreign bodies, canal exostoses"],
  ["Mass loading", "Middle ear effusion, cholesteatoma"],
  ["Discontinuity", "Temporal bone fracture, ossicular necrosis"],
  ["Semicircular canals", "Rotational acceleration; cupula bent by endolymph inertia"],
  ["Otolith organs", "Linear acceleration and gravitational position"],
  ["Allergic rhinitis", "IgE type 1 hypersensitivity; CLEAR rhinorrhoea"],
  ["Nasal polyps", "Interleukins 4, 5 and 13; eosinophil influx; non-neoplastic"],
  ["Turbinate hypertrophy", "Venous sinusoid engorgement; inferior turbinates"],
  ["Rhinitis medicamentosa", "Rebound hyperaemia from topical decongestants"],
  ["Deviated septum", "Poiseuille's law; contralateral compensatory hypertrophy"],
  ["Anterior epistaxis", "Kiesselbach's plexus; 90%; local causes"],
  ["Posterior epistaxis", "Woodruff's plexus; 10%; systemic causes; airway risk"],
  ["Vocal cord nodules", "Bilateral, anterior third junction, chronic phonotrauma"],
  ["Vocal cord polyps", "Unilateral, middle third, one acute strain or bleed"],
  ["Tonsillitis", "Group A Streptococcus; asymmetry means abscess"],
  ["Cervical lymphadenopathy", "Rubbery matted supraclavicular nodes mean lymphoma until excluded"],
    ])

# ---- guard: mechanism, never management ------------------------------------
# Slide 23 hands you an epistaxis management column right beside the
# pathophysiology. [[clin_path_exam_spec]] draws the line at this course's edge.
_MGMT = re.compile(r"first[- ]line|treatment of choice|how (?:do|would) you treat|"
                   r"what is the treatment|drug of choice|next step|oxymetazoline|"
                   r"balloon pack|cauter|emboli|myringotomy|Epley|tonsillectomy|"
                   r"stapedectomy|antibiotic (?:of|for)", re.I)
_mg = [p[0][:60] for p in DECK["cards"] + DECK["matchCards"]
       if any(_MGMT.search(t) for t in p)]
assert not _mg, "management card in a pathophysiology deck: %r" % _mg[:3]

# ---- guard: both live corrections are carded as the CORRECTION -------------
_all = " ".join(t for p in DECK["cards"] for t in p)
assert "CONTINUOUS" in _all and "corrected it aloud" in _all, \
    "the slide-17 labyrinthitis correction is not carded"
assert "T HELPER CELL type 2" in _all, \
    "the slide-21 polyp correction is not carded"
# ...and nothing teaches the uncorrected slide
_wrong = [p[0][:60] for p in DECK["cards"]
          if re.search(r"labyrinthitis", " ".join(p), re.I)
          and re.search(r"\bepisodic\b", p[1], re.I)
          and "correct" not in p[1].lower() and "Ménière" not in p[1]]
assert not _wrong, "a card teaches labyrinthitis as episodic: %r" % _wrong

# ---- guard: no duplicates (Match mode becomes unwinnable) ------------------
_p = [c[0] for c in DECK["cards"]]
assert len(_p) == len(set(_p)), "duplicate card prompt: %r" % [x for x in _p if _p.count(x) > 1][:3]
_a = [c[1] for c in DECK["matchCards"]]
assert len(_a) == len(set(_a)), "duplicate match answer -- Match mode becomes unwinnable"
_q = [c[0] for c in DECK["matchCards"]]
assert len(_q) == len(set(_q)), "duplicate match prompt"


def esc(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def render():
    lines = ['  { id: "%s", name: "%s", color: "%s",' % (DECK["id"], DECK["name"], DECK["color"]),
             "    icon: '%s'," % DECK["icon"], "    cards: ["]
    for q, a in DECK["cards"]:
        lines.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    lines.append("    ],")
    lines.append("    matchCards: [")
    for q, a in DECK["matchCards"]:
        lines.append('      ["%s", "%s"],' % (esc(q), esc(a)))
    lines.append("    ] },")
    return "\n".join(lines)


def main():
    src = open(ARCADE, encoding="utf-8").read()
    fo, fc = "/*CPL5*/", "/*/CPL5*/"
    if fo in src:
        src = re.sub(re.escape(fo) + r".*?" + re.escape(fc), "", src, flags=re.S)
    anchor = 'id: "cp-ophthalmic-pathophys"'
    assert anchor in src, "Clin Path Lecture 4 deck not found -- has arcade.js changed?"
    i = src.index(anchor)
    j = src.index("] },", i) + len("] },")
    src = src[:j] + "\n" + fo + "\n" + render() + "\n" + fc + src[j:]

    # Register it in the Clin Path exam 1 group ONLY. [[arcade_integration]]
    grp = '"cp-inflammation", "cp-dermatology", "cp-abnormal-cell-growth", "cp-ophthalmic-pathophys"'
    assert src.count(grp) == 1, (
        "the Clin Path exam 1 deck group is not where it was (%d matches) -- "
        "registering blind would scope the edit to the wrong class" % src.count(grp))
    if '"cp-ent-pathophys"' not in src.split(grp)[1][:60]:
        src = src.replace(grp, grp + ', "cp-ent-pathophys"', 1)

    open(ARCADE, "w", encoding="utf-8").write(src)
    assert src.count('id: "cp-ent-pathophys"') == 1, "deck landed twice"
    # Count registrations in deckIds arrays only -- the deck's own `id:` line
    # also reads as '"cp-ent-pathophys",' and is not a registration.
    regs = sum(g.count('"cp-ent-pathophys"')
               for g in re.findall(r"deckIds:\s*\[([^\]]*)\]", src))
    assert regs == 1, "deck registered in %d groups, want exactly 1" % regs
    print("added deck %s: %d cards, %d match pairs, registered in Clin Path exam 1"
          % (DECK["id"], len(DECK["cards"]), len(DECK["matchCards"])))


if __name__ == "__main__":
    main()
