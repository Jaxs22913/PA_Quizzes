#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the CMS I Exam 3 (ENT) Arcade decks -- Lectures 15 and 16.

Four decks, split the way the block actually divides rather than one per
lecture: the canal and auricle, the middle ear, the tests, and hearing loss
with vertigo. Splitting the tests out matters because they are four syllabus
objectives in their own right and they are what the two lecture halves share.

ATOMIC FACTS ONLY, per [[arcade_content_policy]] -- one question, one short
answer, no vignettes, nothing that needs a picture. Anything needing an image
stays in the chart and the guide.

Idempotent: fenced between markers, re-runnable.
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCADE = os.path.join(ROOT, "arcade.js")
OPEN, CLOSE = "  // <!--CMSE3-DECKS-->", "  // <!--/CMSE3-DECKS-->"

EAR_ICON = ('<path d="M6 9a6 6 0 1 1 12 0c0 3-2 4-3 6s-1 4-3 4a3 3 0 0 1-3-3"/>'
            '<path d="M9.5 9a2.5 2.5 0 0 1 5 0"/>')
WAVE_ICON = ('<path d="M3 12h2l2-5 3 10 3-13 3 16 2-8h3"/>')
FORK_ICON = ('<path d="M8 3v7a4 4 0 0 0 8 0V3"/><path d="M12 14v7"/><circle cx="8" cy="3" r="1"/>'
             '<circle cx="16" cy="3" r="1"/>')
NOSE_ICON = ('<path d="M12 3c-1 4-3 6-4 9-.6 1.8.4 3.5 2 4"/><path d="M12 3c1 4 3 6 4 9 .6 1.8-.4 3.5-2 4"/><path d="M9 19h6"/>')
SPIN_ICON = ('<path d="M12 3a9 9 0 1 0 9 9"/><path d="M12 3l4 3-4 3"/>'
             '<circle cx="12" cy="12" r="2"/>')

DECKS = [
 ("cms-external-ear", "External Ear &amp; Canal", "accent1", EAR_ICON, [
  ("Pain on moving the tragus points to what?", "Otitis externa."),
  ("Commonest organism in otitis externa?", "Pseudomonas aeruginosa, about 38 percent."),
  ("Biggest risk factor for otitis externa?", "Moisture and swimming."),
  ("What is done before instilling drops for otitis externa?", "Remove the debris."),
  ("What is used when the canal is too swollen for drops?", "An ear wick."),
  ("Why add a corticosteroid to otic antibiotic drops?", "To reduce pain and inflammation."),
  ("Elderly diabetic, pain out of proportion, facial weakness?", "Necrotizing (malignant) external otitis."),
  ("What confirms necrotizing external otitis?", "Imaging showing infection in the bony skull base."),
  ("Which antibiotic class for necrotizing external otitis?", "Antipseudomonal &mdash; ciprofloxacin."),
  ("Fungal ear infection described as wet newspaper?", "Aspergillus."),
  ("Fungal ear infection appearing as white curd?", "Candida."),
  ("How does otomycosis discomfort compare with bacterial?", "Less painful &mdash; itching dominates."),
  ("Treatment of otomycosis?", "Debris removal plus topical antifungals."),
  ("Commonest cause of cerumen impaction?", "Attempts at cleaning the ear."),
  ("When may the canal be irrigated?", "Only if the tympanic membrane is intact."),
  ("Who removes wax when tympanostomy tubes are present?", "An ear, nose and throat specialist."),
  ("Correct home ear cleaning advice?", "A washcloth over a finger at the opening &mdash; nothing enters the canal."),
  ("Which part of the canal makes cerumen?", "The outer third."),
  ("Overriding caution with an ear canal foreign body?", "Do not push it deeper."),
  ("Why not irrigate an organic foreign body?", "It swells when wet and lodges harder."),
  ("How is a live insect in the canal managed first?", "Fill the canal with lidocaine to immobilise it."),
  ("Otitis externa that will not respond, with bloody discharge?", "Carcinoma of the ear canal &mdash; biopsy it."),
  ("Where does blood collect in an auricular haematoma?", "The sub-perichondrial space."),
  ("Within how long should an auricular haematoma be drained?", "Within seven days."),
  ("Why re-examine a blunt ear injury at 12 to 24 hours?", "The haematoma can develop hours later."),
  ("What prevents re-accumulation after draining an ear haematoma?", "Ear splinting."),
  ("Consequence of not draining an auricular haematoma?", "Cauliflower ear."),
  ("Commonest cause of an ear keloid?", "Trauma, classically piercing."),
  ("Which keloid treatment is never used in children?", "Radiation therapy."),
  ("Bilateral symmetrical bony canal growths in a surfer?", "Exostoses, from cold water exposure."),
 ]),
 ("cms-middle-ear", "Middle Ear", "accent2", EAR_ICON, [
  ("Commonest cause of acute otitis media overall?", "A virus."),
  ("The three bacterial causes of acute otitis media?", "S. pneumoniae, H. influenzae, M. catarrhalis."),
  ("Why has H. influenzae become less common?", "Vaccination &mdash; M. catarrhalis has overtaken it."),
  ("Which history point changes the likely organism in a child?", "Immunisation status."),
  ("Peak age for acute otitis media?", "Around two years."),
  ("Antibiotic for bacterial acute otitis media?", "Amoxicillin."),
  ("Otoscopy in acute otitis media?", "Erythematous and bulging, with reduced mobility."),
  ("What defines recurrent acute otitis media?", "Three episodes in six months, or more than four in twelve."),
  ("Treatment for recurrent acute otitis media?", "Tympanostomy tubes."),
  ("How is acute otitis media diagnosed?", "Clinically."),
  ("What distinguishes otitis media with effusion?", "Fluid without acute infection."),
  ("Otoscopy in otitis media with effusion?", "A dull drum with an air and fluid level."),
  ("Three factors deciding treatment of a childhood effusion?", "Duration, degree of hearing loss, and effect on speech and language."),
  ("Main risk of a long-standing childhood effusion?", "Speech and language delay."),
  ("What obstructs the eustachian tubes and is removed surgically?", "Hypertrophied adenoids."),
  ("What defines chronic otitis media?", "A non-healing tympanic membrane perforation."),
  ("Chronic otitis media with a dry perforation and no infection?", "The benign subtype."),
  ("What is mastoiditis?", "Infection spreading into the mastoid air cells."),
  ("Function of the eustachian tube?", "Equalising middle ear pressure."),
  ("Otoscopic finding in eustachian tube dysfunction?", "A retracted, poorly mobile drum."),
  ("What does crackling on swallowing indicate?", "The blockage is only partial."),
  ("Drug pair for eustachian tube dysfunction?", "Decongestants and intranasal corticosteroids."),
  ("Caution with forced exhalation against resistance?", "Avoid it during active nasal discharge."),
  ("Two activities causing ear barotrauma?", "Air travel and underwater diving."),
  ("Blood behind the drum after a flight?", "Haemotympanum."),
  ("Vertigo and tinnitus after barotrauma means what?", "The inner ear is involved &mdash; window rupture."),
  ("Procedure giving instant relief in severe barotrauma?", "Myringotomy."),
  ("What happens to the pain when the drum ruptures?", "It stops."),
  ("What is a cholesteatoma made of?", "Keratinised squamous epithelium."),
  ("Symptom pattern suggesting cholesteatoma?", "Recurrent discharge with no external canal infection."),
  ("Definitive treatment of cholesteatoma?", "Surgical removal."),
  ("Which ossicle does otosclerosis fix?", "The stapes."),
  ("What do patients with otosclerosis notice?", "They hear better in background noise."),
 ]),
 ("cms-ear-tests", "Weber, Rinne &amp; the Tracings", "accent3", FORK_ICON, [
  ("What does the Weber test compare?", "Bone conduction between the two ears."),
  ("What does the Rinne test compare?", "Air against bone conduction in one ear."),
  ("Weber in a unilateral conductive loss?", "Lateralises to the affected ear."),
  ("Weber in a unilateral sensorineural loss?", "Lateralises to the unaffected ear."),
  ("Rinne in a conductive loss?", "Bone conduction equal to or greater than air."),
  ("Rinne in a sensorineural loss?", "Air still beats bone &mdash; the same as normal."),
  ("Why does Weber carry the diagnosis?", "Because the sensorineural Rinne looks normal."),
  ("Voice quality in a conductive loss?", "Soft &mdash; the inner ear is intact."),
  ("Voice quality in a sensorineural loss?", "Loud."),
  ("Effect of background noise in conductive loss?", "Hearing seems better."),
  ("Effect of background noise in sensorineural loss?", "Hearing gets worse."),
  ("Four mechanisms of conductive loss?", "Obstruction, mass loading, stiffness, discontinuity."),
  ("Which conductive cause looks normal on otoscopy?", "Otosclerosis."),
  ("Decibel range for normal hearing?", "Zero to twenty."),
  ("Decibel range for moderate hearing loss?", "Forty to sixty."),
  ("Threshold for profound hearing loss?", "Above eighty decibels."),
  ("The easy way to remember the severity bands?", "They run in twenties &mdash; 20, 40, 60, 80."),
  ("Tympanogram type A means what?", "A normal middle ear."),
  ("A flat tympanogram means what?", "Fluid in the middle ear, or a perforation &mdash; type B."),
  ("A tympanogram peak shifted negative?", "Negative middle ear pressure &mdash; type C."),
  ("A shallow, stiff tympanogram?", "Ossicular fixation or tympanosclerosis &mdash; type As."),
  ("A deep, over-compliant tympanogram?", "Ossicular discontinuity or a monomeric drum &mdash; type Ad."),
  ("Gold standard vestibular test for one ear at a time?", "Electronystagmography."),
  ("Gold standard imaging for retrocochlear disease?", "Magnetic resonance imaging with gadolinium."),
  ("Which manoeuvre diagnoses positional vertigo?", "Dix-Hallpike."),
  ("Which manoeuvre treats positional vertigo?", "Epley."),
  ("Which test presents single tones to find the softest audible level?", "Pure tone audiometry."),
  ("From what age is hearing screened routinely?", "Sixty-five."),
 ]),
 ("cms-hearing-vertigo", "Hearing Loss &amp; Vertigo", "accent4", SPIN_ICON, [
  ("Commonest sensorineural hearing loss?", "Presbycusis."),
  ("Pattern of presbycusis?", "Bilateral, symmetrical, gradual, high frequency first."),
  ("What do patients with presbycusis say?", "They hear speech but cannot make out the words."),
  ("Most ototoxic and most commonly implicated class?", "Aminoglycosides."),
  ("Three other named ototoxic agents?", "Furosemide, aspirin, platinum chemotherapy."),
  ("Which other organ is threatened by ototoxic drugs?", "The kidney &mdash; they are often nephrotoxic too."),
  ("What is a temporary threshold shift?", "Hearing loss recovering in 24 to 48 hours."),
  ("At what sound level do pain and injury occur?", "About 120 decibels."),
  ("Which body regulates occupational noise?", "The Occupational Safety and Health Administration."),
  ("Audible pop, then sudden loss and vertigo after straining?", "Perilymphatic fistula."),
  ("Where does a perilymphatic fistula occur?", "At the round or oval window."),
  ("Stepwise bilateral loss with periods of stability?", "An autoimmune cause."),
  ("Which treatable infection mimics Meniere disease exactly?", "Syphilis."),
  ("Which tests for syphilitic hearing loss?", "FTA-ABS and MHA-TP &mdash; VDRL is not helpful."),
  ("Treatment of syphilitic sensorineural loss?", "An antibiotic with systemic corticosteroids."),
  ("Three named hereditary syndromes?", "Waardenburg, Alport, Usher."),
  ("Sudden sensorineural hearing loss is best called what?", "A syndrome, not a disease."),
  ("What does sudden sensorineural loss demand?", "Prompt specialist referral &mdash; the steroid window is short."),
  ("Frequency range affected in Meniere disease?", "Low frequencies, and it fluctuates."),
  ("How long does a Meniere vertigo attack last?", "Several hours."),
  ("Which ear sensation accompanies Meniere disease?", "Fullness."),
  ("How long does positional vertigo last?", "Ten to sixty seconds."),
  ("What causes most positional vertigo?", "Debris in the posterior semicircular canal."),
  ("Which feature separates labyrinthitis from vestibular neuronitis?", "Labyrinthitis affects hearing."),
  ("Which structure is inflamed in vestibular neuronitis?", "The vestibular portion of cranial nerve eight."),
  ("Course of vestibular neuronitis?", "Benign and self-limiting."),
  ("Drug for the acute vertigo of labyrinthitis?", "Meclizine, or oral diazepam."),
  ("Characteristic symptom of acoustic neuroma?", "Word understanding worse than the tone loss predicts."),
  ("Which cranial nerves may an acoustic neuroma involve?", "Five and seven."),
  ("Vertigo with facial paralysis and crossed sensory loss?", "Vertebrobasilar occlusion &mdash; a brainstem problem."),
  ("Commonest non-vestibular cause of dizziness in the elderly?", "Small vessel ischaemic disease."),
  ("Vertigo with ataxia, headache or facial numbness?", "Consider a cerebellar infarction."),
  ("Red flag pattern for tinnitus?", "Unilateral or pulsatile."),
  ("What works for tinnitus?", "No drug beats placebo; masking and biofeedback may help."),
  ("Conductive loss with pulsatile tinnitus and a vascular mass?", "Glomus tumour."),
  ("Normal voice despite claimed profound loss?", "A functional hearing loss."),
 ]),
 ("cms-nose-sinuses", "Nose &amp; Sinuses", "accent1", NOSE_ICON, [
  ("How long does acute sinusitis last, by definition?", "Under four weeks."),
  ("What share of acute rhinosinusitis is viral?", "Ninety to ninety-eight per cent."),
  ("What share of viral episodes superinfect with bacteria?", "Half a per cent to two per cent."),
  ("Preferred term for sinus inflammation, and why?", "Rhinosinusitis &mdash; rhinitis and sinusitis usually coexist."),
  ("Five features suggesting bacterial sinusitis?", "Double worsening, ten days or more, purulent discharge, unilateral tooth or facial pain, and fever."),
  ("What is double worsening?", "Getting worse again more than five to six days after initially improving."),
  ("Which symptom occurs only in bacterial and fungal sinusitis?", "Pain &mdash; and it is reproducible on palpation."),
  ("How does sinusitis pain behave with posture?", "Worse bending over or lying flat."),
  ("Which discharge colour is least helpful?", "Yellow or green."),
  ("What does black nasal discharge suggest?", "A fungus."),
  ("What does rust-coloured discharge suggest?", "Possibly Streptococcus pneumoniae."),
  ("Can any test separate viral from bacterial sinusitis?", "No &mdash; none, which is why routine imaging is discouraged."),
  ("When is sinus computed tomography indicated?", "Recurrent infection, treatment failure, or suspected extrasinus involvement."),
  ("First-line antibiotic for bacterial sinusitis?", "Amoxicillin with clavulanate."),
  ("Alternative in penicillin allergy?", "Doxycycline, or an antipneumococcal fluoroquinolone."),
  ("Three symptoms in sinusitis needing urgent attention?", "Diplopia, periorbital swelling or erythema, and altered mental status."),
  ("How long does chronic sinusitis last?", "More than twelve weeks."),
  ("Mechanism of chronic bacterial sinusitis?", "Impaired mucociliary clearance causing repeated infections."),
  ("Commonest organism in chronic fungal sinusitis?", "Aspergillus."),
  ("How is mild chronic fungal sinusitis cured?", "Endoscopic surgery, without antifungal agents."),
  ("What does allergic fungal sinusitis mucus resemble?", "Peanut butter &mdash; thick and eosinophil-laden."),
  ("Does allergy itself cause sinusitis?", "No &mdash; it creates the environment for infection."),
  ("Two common causes of a perforated septum?", "Intranasal steroid use and cocaine, both by chronic ischaemia."),
  ("Which autoimmune disease can perforate the septum?", "Granulomatosis with polyangiitis."),
  ("Treatment of a deviated septum?", "Septoplasty."),
  ("Where does a septal haematoma collect?", "Between the septum and the perichondrium."),
  ("Treatment of a septal haematoma?", "Drainage by intranasal incision under general anaesthesia."),
  ("Where do ninety per cent of nosebleeds arise?", "Kiesselbach's plexus, on the nasal septum."),
  ("Commonest cause of epistaxis?", "Trauma &mdash; from the patient's own finger."),
  ("Which artery causes posterior epistaxis?", "The sphenopalatine artery."),
  ("Why are posterior bleeds higher risk?", "Aspiration, and subsequent infection."),
  ("Which spray is used in initial epistaxis tamponade?", "Oxymetazoline."),
  ("How long should the alae be pinched?", "Ten minutes, continuously."),
  ("Which way should an epistaxis patient lean?", "Forward at the waist, sitting up, so blood is not swallowed."),
  ("Is a prothrombin time routine in epistaxis?", "No &mdash; only for the anticoagulated patient."),
  ("What must an epistaxis patient not do afterwards?", "Blow their nose."),
  ("Unilateral foul-smelling purulent discharge in a toddler?", "A nasal foreign body."),
  ("Where do nasal foreign bodies usually sit?", "On the floor under the inferior turbinate, or in front of the middle turbinate."),
  ("Four criteria letting you skip nasal fracture x-rays?", "Swelling isolated to the bony bridge, breathing through each naris, a straight nose, and no septal haematoma."),
  ("Initial treatment of a nasal fracture?", "Ice and head of bed elevated."),
  ("What do nasal polyps look like?", "Grey, glistening masses."),
  ("Which symptom do large nasal polyps cause?", "Anosmia."),
  ("Which triad accompanies aspirin-exacerbated respiratory disease?", "Nasal polyps, asthma and aspirin sensitivity."),
  ("What must every child with multiple nasal polyps be evaluated for?", "Cystic fibrosis and asthma."),
  ("Which test screens for cystic fibrosis in a child with polyps?", "The chloride sweat test."),
  ("How durable is polyp surgery?", "Temporary &mdash; they recur within months to years."),
  ("Nasal findings in allergic rhinitis?", "Clear discharge from both nostrils and a bluish, oedematous mucosa."),
  ("How many allergic rhinitis patients need two or more medicines?", "About eighty per cent."),
  ("Which virus is associated with nasopharyngeal carcinoma?", "Epstein-Barr virus."),
  ("Presentation of nasopharyngeal carcinoma?", "Headache, diplopia, facial numbness and a neck mass."),
  ("Where is nasopharyngeal carcinoma endemic?", "Southern China, Southeast Asia, North Africa and the Arctic."),
 ]),
]


def js(decks):
    out = []
    for did, name, colour, icon, cards in decks:
        rows = "\n".join('      [%s, %s],' % (json_str(q), json_str(a)) for q, a in cards)
        out.append('  { id: "%s", name: "%s", color: "%s",\n'
                   "    icon: '%s',\n"
                   "    cards: [\n%s\n    ]},\n" % (did, name, colour, icon, rows))
    return "\n".join(out)


def json_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    src = open(ARCADE, encoding="utf-8").read()
    block = OPEN + "\n" + js(DECKS) + CLOSE

    if OPEN in src:
        src = re.sub(re.escape(OPEN) + r".*?" + re.escape(CLOSE), lambda _m: block, src,
                     flags=re.S)
    else:
        # INSERT INSIDE THE DEMO_DECKS ARRAY, anchored to its own closing bracket.
        # The first version anchored to "the last ]}, before the class-group
        # registry", which put the decks AFTER the array closed -- syntactically
        # valid, so nothing complained, but findDeck() searches DEMO_DECKS and
        # returned undefined for all four, and the home page threw on
        # deck.cards. A parse check cannot catch that; only loading the page can.
        decl = src.index("var DEMO_DECKS = [")
        end = src.index("\n];", decl)
        src = src[:end] + "\n\n" + block + src[end:]

    # Register the four decks under CMS I, Exam 3.
    #
    # SCOPED TO THE CMS GROUP ONLY. The first version tested whether the string
    # '"exam3", name: "Exam 3"' appeared anywhere in the file and, finding it,
    # ran a global re.sub -- which rewrote ANATOMY, PHYSIOLOGY and PHYSICAL
    # DIAGNOSIS 1's Exam 3 deck lists to the ENT decks. Three classes silently
    # broken by one edit. The fix is to cut out the CMS group first and only
    # ever edit inside it.
    ids = ", ".join('"%s"' % d[0] for d in DECKS)
    exam3 = ('    { id: "exam3", name: "Exam 3", deckIds: [\n      %s\n    ] }' % ids)

    g_start = src.index('  { id: "cms-1", name: "Clinical Medicine and Surgery I", exams: [')
    g_end = src.index("\n  ]},", g_start) + len("\n  ]},")
    group = src[g_start:g_end]
    assert group.count('name: "Exam 2"') == 1, "CMS group not isolated cleanly"

    if 'name: "Exam 3"' in group:
        group = re.sub(r'    \{ id: "exam3", name: "Exam 3", deckIds: \[.*?\] \}',
                       lambda _m: exam3, group, flags=re.S)
    else:
        e2 = group.rindex("] }")
        group = group[:e2 + len("] }")] + ",\n" + exam3 + group[e2 + len("] }"):]
    src = src[:g_start] + group + src[g_end:]

    # Prove every deck is INSIDE DEMO_DECKS before writing -- the failure this
    # guards against was invisible to a syntax check.
    d0 = src.index("var DEMO_DECKS = [")
    d1 = src.index("\n];", d0)
    for did, *_ in DECKS:
        at = src.index('id: "%s"' % did)
        assert d0 < at < d1, "%s was placed OUTSIDE the DEMO_DECKS array" % did

    open(ARCADE, "w", encoding="utf-8").write(src)
    n = sum(len(d[4]) for d in DECKS)
    print("wrote %d decks, %d cards into arcade.js" % (len(DECKS), n))
    for did, name, _c, _i, cards in DECKS:
        print("   %-22s %-32s %d cards" % (did, re.sub("&[a-z]+;", "&", name), len(cards)))


if __name__ == "__main__":
    main()
