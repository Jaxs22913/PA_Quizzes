#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the PD2 Lecture 4 (Advanced ENT History and Exam) Arcade deck.

PHYSICAL DIAGNOSIS, so every card is about ELICITING a finding or READING one.
The mechanism behind these conditions belongs to Clinical Pathophysiology I
Lecture 5 and their management to CMS I Exam 3; guarded below.

THE MODIFIED CENTOR AGE ADJUSTMENT IS CARDED, and it is worth saying why: it
exists only inside slide 65's picture. The slide's text is a single caption
line, so a deck built by reading slide text would be missing the half of the
rule most likely to be asked.

House rules: no card may depend on having the deck open, and none may be about
course mechanics -- this deck is unusually full of the latter.
"""
import os, re

ARCADE = "/Users/jaxonluke/Developer/PA_Quizzes/arcade.js"
# a tuning fork
ICON = ('<path d="M9 3v7a3 3 0 0 0 6 0V3"/><path d="M12 13v8"/>')

DECK = dict(
    id="pd2-ent-exam",
    name="Advanced ENT History & Exam",
    color="accent1",
    icon=ICON,
    cards=[
  # --- the weighted block ---
  ["Where does the fork go for the WEBER test?", "On the top of the head or mid-forehead."],
  ["What is the Weber test for?", "Evaluating UNILATERAL hearing loss, by which way the sound lateralises."],
  ["What is a normal Weber result?", "Midline, or heard equally in both ears."],
  ["Which way does Weber lateralise in CONDUCTIVE loss?", "To the IMPAIRED ear."],
  ["Why does Weber go to the bad ear in conductive loss?", "The block screens out competing room noise on that side, so the bone-conducted tone has that ear to itself."],
  ["Which way does Weber lateralise in SENSORINEURAL loss?", "To the GOOD ear."],
  ["Why does Weber go to the good ear in sensorineural loss?", "The damaged inner ear or cochlear nerve cannot transmit the tone however it arrives."],
  ["How is the RINNE test performed, in order?", "Fork on the mastoid until the sound stops, then moved close to the canal and the patient asked if it is still heard."],
  ["What is a normal Rinne result?", "Air conduction heard longer than bone conduction."],
  ["What is the Rinne result in CONDUCTIVE loss?", "Bone conduction equal to or greater than air conduction."],
  ["Why does bone beat air in conductive loss?", "Vibration through bone bypasses the blocked external or middle ear and reaches an intact cochlea directly."],
  ["What is the Rinne result in SENSORINEURAL loss?", "Air still greater than bone — the normal ratio prevails."],
  ["Why is the Rinne 'normal' in sensorineural loss?", "It compares two routes to the SAME cochlea, and the damage degrades both equally, so the ratio between them survives."],
  ["What is the mnemonic for where the Rinne fork goes?", "Rinne is under the pinna — the pinna is the outside of the ear, and the fork goes on the mastoid under it."],
  ["What is the mnemonic for what Weber tells you?", "Weber tells you WHETHER — whether it is the right ear or the left."],
  ["Rinne on the right is normal and Weber lateralises right. Which ear has sensorineural loss?", "The LEFT. A normal Rinne rules out conductive loss on the right, and Weber goes away from a sensorineural lesion."],
  ["Which two situations can the tuning fork tests NOT distinguish?", "Normal from bilateral sensorineural loss, and normal from mixed conductive and sensorineural loss."],
  ["Why can't the forks detect a symmetrical loss?", "Both tests work by comparing — one side against the other, or one route against the other. A symmetrical loss leaves the comparison looking normal."],
  ["Which tuning fork is used, and under what conditions?", "A 512 hertz fork, the smaller one, in a quiet room."],
  # --- conductive vs sensorineural ---
  ["Where does conductive hearing loss sit?", "The external or middle ear."],
  ["Where does sensorineural hearing loss sit?", "The inner ear, or cranial nerve VIII and the central pathways."],
  ["At what ages does conductive loss usually begin?", "Childhood and young adulthood, up to about forty."],
  ["At what ages does sensorineural loss usually begin?", "Middle or later years."],
  ["Which type of loss is usually VISIBLE on otoscopy, and what is the exception?", "Conductive is usually visible — except otosclerosis. Sensorineural is not visible at all."],
  ["What happens to hearing in a noisy room in CONDUCTIVE loss?", "It seems to IMPROVE — the block attenuates the background along with everything else."],
  ["What happens to hearing in a noisy room in SENSORINEURAL loss?", "It worsens."],
  ["What happens to the patient's own VOICE in conductive loss?", "It stays SOFT — the inner ear and cochlear nerve are intact, so they hear themselves perfectly well."],
  ["What happens to the patient's own VOICE in sensorineural loss?", "It may be LOUD — they cannot hear themselves, so they raise it."],
  ["Which frequencies go first in sensorineural loss?", "The higher registers, so sound is distorted."],
  ["Name the conductive causes of hearing loss.", "Cerumen, foreign bodies, effusions, exostoses and osteomas, tumours, and tympanic membrane perforation."],
  ["What are exostoses?", "Benign bony growths in the ear canal."],
  ["Name the sensorineural causes of hearing loss.", "Congenital and hereditary causes, presbycusis, viral infection, Ménière disease, noise exposure and acoustic neuroma."],
  ["Which viral infections cause sensorineural loss?", "Rubella and cytomegalovirus."],
  ["What frequency pattern does presbycusis take?", "Higher frequency loss."],
  # --- hearing screening ---
  ["How is the whispered voice test set up?", "Two feet behind the patient, the other ear occluded, a three-item sequence whispered twice."],
  ["Why does the examiner stand BEHIND the patient?", "To remove lip reading."],
  ["What counts as a normal whispered voice result?", "Three or more of six correct. Four of six incorrect is abnormal."],
  ["Which other two bedside hearing screens are used?", "Finger rub and a watch."],
  # --- ear history ---
  ["Ear pain with a normal-looking ear. Which three sources should the history cover?", "The temporomandibular joint, the teeth, and the cervical spine."],
  ["Which cranial nerves carry referred pain to the ear?", "V, VII, IX and X."],
  ["Which drugs should be asked about in a patient with hearing loss?", "Aminoglycosides, aspirin, non-steroidal anti-inflammatories, quinine and furosemide."],
  ["What is tinnitus, by definition?", "Sound perceived with no external source."],
  ["Tinnitus WITH hearing loss and vertigo points to what?", "Ménière disease."],
  ["'Dizziness' splits into which four categories?", "Vertigo, presyncope, disequilibrium, and psychiatric causes."],
  ["What is disequilibrium?", "Unsteadiness or imbalance — neither spinning nor faintness."],
  ["What is presyncope?", "The sensation of an impending faint, or lightheadedness."],
  # --- the vertigo table ---
  ["How long does a single episode of benign positional vertigo last?", "Seconds to under a minute."],
  ["How long does the CONDITION of benign positional vertigo last?", "A few weeks, and it may recur. The episode length and the illness length are different numbers."],
  ["What triggers benign positional vertigo?", "Rolling onto the affected side, or tilting the head up."],
  ["Is hearing affected in benign positional vertigo?", "No, and tinnitus is absent."],
  ["How long does vestibular neuronitis last?", "Hours to two weeks, and it may recur over twelve to eighteen months."],
  ["Is hearing affected in vestibular neuronitis?", "No, and tinnitus is absent."],
  ["How long does Ménière vertigo last?", "Several hours to a day or more, and it is recurrent."],
  ["What happens to hearing in Ménière disease?", "Sensorineural loss that recurs and eventually progresses."],
  ["What is the tinnitus of Ménière disease like?", "Present and fluctuating."],
  ["Which feature beyond vertigo marks Ménière disease?", "Pressure or fullness in the affected ear."],
  ["Which drugs cause vertigo through toxicity?", "Loop diuretics, aminoglycosides, salicylates and alcohol."],
  ["What is the hearing pattern in acoustic neuroma?", "Impaired on ONE side, with tinnitus present."],
  ["Which cranial nerves may be involved in acoustic neuroma, beyond VIII?", "V and VII."],
  ["What is the duration pattern of CENTRAL vertigo?", "Variable, but rarely continuous."],
  ["Is hearing affected in central vertigo?", "No, and tinnitus is absent — but other brainstem deficits are present."],
  ["Which brainstem deficits accompany central vertigo?", "Dysarthria, ataxia, and crossed motor and sensory deficits."],
  ["Name the causes of central vertigo.", "Brainstem lesion, atherosclerosis, multiple sclerosis, vertebrobasilar migraine and transient ischaemic attack."],
  ["Of the six vertigo causes, which three affect hearing?", "Ménière disease, drug toxicity and acoustic neuroma."],
  # --- ear exam ---
  ["Which three structures are inspected and palpated before the otoscope?", "The auricles, the mastoid and the tragus."],
  ["How is the auricle positioned for otoscopy in an adult?", "Pulled up, back, and away from the head."],
  ["Which size of speculum, and why?", "The largest that fits, because insufflation needs a proper seal."],
  ["Which part of the examiner's hand contacts the patient, and why?", "The ulnar aspect, which anchors the otoscope to the head so a sudden movement does not drive it into the canal."],
  ["How do you check the otoscope for leaks before insufflating?", "Put a finger over the speculum tip and squeeze the bulb — you should feel the pressure build."],
  ["What kind of pressure is applied to the bulb?", "Quick, firm but gentle."],
  ["What does reduced tympanic membrane mobility mean?", "Effusion behind it, or a thickened membrane."],
  # --- otoscopic findings ---
  ["How does the canal look in ACUTE otitis externa?", "Swollen, narrow, moist, pale and tender, and it may be erythematous."],
  ["How does the canal look in CHRONIC otitis externa?", "The skin is thickened, red and itchy."],
  ["Acute or chronic otitis externa — which is painful and which is itchy?", "Acute is painful and swollen; chronic is itchy and thickened."],
  ["What is a CENTRAL tympanic membrane perforation?", "One that does not extend to the margin."],
  ["What is a MARGINAL perforation?", "One that involves the margin."],
  ["What usually causes a tympanic membrane perforation?", "Otitis media, and there may be drainage through it."],
  ["What is tympanosclerosis, and does it matter?", "A hyaline deposit in the membrane after severe otitis media or a healed perforation. Usually not clinically significant."],
  ["Amber fluid behind the drum with bubbles. What is it?", "A serous effusion, after an upper respiratory infection or a change in atmospheric pressure."],
  ["Which three findings describe the drum in acute otitis media?", "Red, bulging, and with the landmarks lost."],
  ["Which bacteria commonly cause otitis media?", "Streptococcus pneumoniae and Haemophilus influenzae."],
  ["What is bullous myringitis?", "Painful haemorrhagic vesicles on the tympanic membrane or canal. It may be viral or bacterial."],
  ["Why is bulging of the drum graded rather than called present or absent?", "A mildly bulging drum still has landmarks you can pick out; the point they disappear is the point the effusion becomes convincing."],
  # --- nose ---
  ["Name the three turbinates.", "Superior, middle and inferior."],
  ["Where does the maxillary sinus drain?", "At the middle turbinate."],
  ["Why should recent dental work be asked about in facial pain?", "The maxillary sinus floor sits directly above the upper tooth roots, so a dental procedure can present as sinus pain."],
  ["Which two drug histories matter specifically for nasal symptoms?", "Topical decongestants causing rhinitis medicamentosa, and cocaine."],
  ["Which epistaxis history suggests a SYSTEMIC problem?", "Recurrent bleeding, or bleeding and bruising elsewhere on the body."],
  ["How is nasal patency tested?", "Occlude one nostril and ask the patient to breathe in."],
  ["What does UNILATERAL nasal obstruction suggest?", "A foreign body, a tumour, or a deviated septum."],
  ["Which conditions are nasal polyps associated with?", "Allergic rhinitis, aspirin sensitivity, asthma, chronic sinus infection and cystic fibrosis."],
  ["How does the mucosa look in VIRAL rhinitis?", "Red and swollen."],
  ["How does the mucosa look in ALLERGIC rhinitis?", "Pale, bluish or red."],
  ["What causes a perforated nasal septum?", "Trauma, surgery or drug use."],
  ["In which direction are the frontal and maxillary sinuses palpated?", "Upward for both — and avoid the eyes on the frontal sinuses."],
  ["How is the MAXILLARY sinus transilluminated?", "In a dark room, light shone down just below the inner corner of the eye with the mouth open."],
  ["How is the FRONTAL sinus transilluminated?", "In a dark room, light shone up under the brow close to the nose."],
  ["What does absence of a glow on transillumination mean, and how much does it prove?", "Thickened mucosa or secretions — but the test is neither sensitive nor specific."],
  ["Is the COLOUR of nasal discharge diagnostic?", "No. Purulent discharge is suggestive, but colour settles nothing."],
  ["Under what duration is acute BACTERIAL sinusitis unlikely?", "Less than seven days."],
  ["How does a septal haematoma form?", "Injury disrupts the vessels and pulls the lining away from the cartilage, so blood collects between the two."],
  ["Why does a septal haematoma need URGENT drainage?", "To prevent necrosis of the septal cartilage, which has no blood supply of its own and depends on the lining that was stripped away."],
  # --- oral ---
  ["What are the four Centor criteria?", "Fever, tonsillar exudates, swollen and tender anterior cervical nodes, and ABSENCE of cough."],
  ["Why does the ABSENCE of cough score on Centor?", "A cough points toward a viral cause, so its absence raises the probability of streptococcal infection."],
  ["What temperature counts for the Centor fever criterion?", "Above 100.4 degrees Fahrenheit, or 38 degrees Celsius."],
  ["How does AGE change the modified Centor score?", "Three to fourteen adds a point; fifteen to forty-four adds nothing; forty-five and over SUBTRACTS a point."],
  ["Why does being older subtract a Centor point?", "Streptococcal pharyngitis is largely a disease of children, so age argues against it."],
  ["What does a Centor score of zero or less mean?", "A one to two and a half per cent risk, and no further testing or antibiotics indicated."],
  ["What does a Centor score of four or more mean?", "A fifty-one to fifty-three per cent risk, where empiric treatment is considered."],
  ["The uvula deviates to one side and the palate fails to rise. Which nerve?", "Cranial nerve X — and the uvula deviates AWAY from the paralysed side."],
  ["The tongue deviates on protrusion. Which nerve?", "Cranial nerve XII."],
  ["A smooth, beefy red tongue suggests what?", "Vitamin B12 deficiency."],
  ["A sore AND smooth tongue suggests what?", "Nutritional deficiency."],
  ["Where do tongue cancers appear, and in whom?", "On the lateral border or undersurface, as indurated red or white lesions, in males over fifty."],
  ["What is geographic tongue?", "A benign map-like pattern of patches, of no pathological significance."],
  ["How is the tongue palpated?", "Held with gauze in one hand and palpated with the other, then the hands are switched for the opposite side."],
  ["Why must the hands be switched when palpating the tongue?", "It is the only way to reach both lateral borders properly — and that is where the cancers are."],
  ["Why are dentures removed during the oral exam?", "To look underneath for ulcers and lesions."],
  ["What is angular cheilitis?", "Cracking and inflammation at the corners of the mouth."],
  ["What is torus palatinus?", "A benign bony growth in the midline of the hard palate."],
  ["What are the other names for necrotising ulcerative gingivitis?", "Vincent's angina, and trench mouth."],
  ["What causes necrotising ulcerative gingivitis?", "Poor dental hygiene, and drug use. The bacteria destroy tissue as they spread."],
  ["Which causes of hoarseness should a history cover?", "Viral laryngitis, voice overuse, laryngeal nerve damage, reflux and smoking."],
  ["What is needed to inspect the posterior pharynx?", "A tongue blade."],
  # --- neck, thyroid, head ---
  ["Name the neck node chains in palpation order.", "Preauricular, postauricular, occipital, tonsillar, submandibular, submental, superficial cervical, posterior cervical, deep cervical, supraclavicular."],
  ["Which part of the hand palpates the neck nodes?", "The pads of the index and middle fingers."],
  ["What does a NORMAL lymph node feel like?", "Round or ovoid, smooth, mobile and non-tender."],
  ["What does a TENDER node suggest?", "Inflammation."],
  ["What does a HARD, FIXED node suggest?", "Malignancy."],
  ["An enlarged LEFT supraclavicular node suggests what?", "Metastasis from an abdominal or thoracic malignancy."],
  ["What does GENERALISED lymphadenopathy raise?", "Human immunodeficiency virus, Epstein-Barr virus, lymphoma, leukaemia and sarcoidosis."],
  ["Submandibular swelling with cellulitis of the floor of the mouth. What is it?", "Ludwig's angina."],
  ["Why is Ludwig's angina life threatening?", "The airway. The swelling spreads fast and pushes the floor of the mouth and tongue upward and back."],
  ["Where does Ludwig's angina usually start?", "From the lower teeth, spreading down into the floor of the mouth."],
  ["What does tracheal deviation suggest?", "Masses, atelectasis, or a large pneumothorax."],
  ["Which landmark locates the thyroid?", "The cricoid cartilage."],
  ["A diffusely enlarged, SOFT thyroid suggests what?", "Graves disease."],
  ["A diffusely enlarged, FIRM thyroid suggests what?", "Hashimoto thyroiditis."],
  ["A TENDER thyroid suggests what?", "Thyroiditis."],
  ["What is endemic goitre associated with?", "Iodine deficiency."],
  ["When does a multinodular thyroid carry a malignancy risk?", "When there is a family history."],
  ["Which headache patterns are EPISODIC?", "Migraine and tension."],
  ["Which headache patterns are UNILATERAL?", "Migraine and cluster."],
  ["A sudden, severe headache raises what?", "Subarachnoid haemorrhage."],
  ["A new, progressive and persistent headache raises what?", "A mass."],
  ["Fine hair and coarse hair point to what?", "Fine hair to hyperthyroidism; coarse hair to hypothyroidism."],
  ["An abnormally enlarged head raises which two conditions?", "Hydrocephalus and Paget disease."],
    ],
    matchCards=[
  ["Weber in conductive loss", "Lateralises to the IMPAIRED ear"],
  ["Weber in sensorineural loss", "Lateralises to the GOOD ear"],
  ["Rinne in conductive loss", "Bone greater than or equal to air"],
  ["Rinne in sensorineural loss", "Air greater than bone — normal ratio prevails"],
  ["Benign positional vertigo", "Under 1 minute; positional; hearing NOT affected"],
  ["Vestibular neuronitis", "Hours to 2 weeks; hearing NOT affected; no tinnitus"],
  ["Ménière disease", "Hours to a day; aural fullness; fluctuating tinnitus"],
  ["Acoustic neuroma", "Insidious; ONE-sided hearing loss; may involve CN V and VII"],
  ["Central vertigo", "Rarely continuous; hearing spared; brainstem deficits"],
  ["Acute otitis externa", "Canal swollen, narrow, moist, pale and TENDER"],
  ["Chronic otitis externa", "Canal skin thickened, red and ITCHY"],
  ["Tympanosclerosis", "Hyaline deposit; usually not clinically significant"],
  ["Serous effusion", "Amber fluid, sometimes bubbles; after a URI"],
  ["Acute otitis media", "Red, bulging, landmarks lost"],
  ["Bullous myringitis", "Painful haemorrhagic vesicles on the drum"],
  ["Viral rhinitis", "Mucosa red and swollen"],
  ["Allergic rhinitis", "Mucosa pale, bluish or red"],
  ["Septal haematoma", "Urgent drainage or the cartilage necroses"],
  ["Centor criteria", "Fever, exudates, anterior cervical nodes, NO cough"],
  ["Modified Centor age points", "3–14 adds one; 45 and over subtracts one"],
  ["Cranial nerve X palsy", "Palate fails to rise; uvula deviates AWAY"],
  ["Cranial nerve XII lesion", "Asymmetric tongue protrusion"],
  ["Vitamin B12 deficiency", "Smooth, beefy red tongue"],
  ["Left supraclavicular node", "Abdominal or thoracic metastasis"],
  ["Ludwig's angina", "Floor-of-mouth cellulitis; airway emergency"],
  ["Graves disease", "Thyroid diffusely enlarged and SOFT"],
  ["Hashimoto thyroiditis", "Thyroid diffusely enlarged and FIRM"],
  ["Subarachnoid haemorrhage", "Sudden and severe headache"],
    ])

# ---- guard: physical diagnosis, not pathophysiology or management ----------
_SCOPE = re.compile(r"first[- ]line|drug of choice|what is the treatment|"
                    r"how (?:do|would) you treat|which antibiotic do|molecular mechanism|"
                    r"pathogenesis of|cytokine|interleukin|apoptosis|osteoclast", re.I)
_sc = [p[0][:60] for p in DECK["cards"] + DECK["matchCards"] if any(_SCOPE.search(t) for t in p)]
assert not _sc, "strays into pathophysiology or management: %r" % _sc[:3]

# ---- guard: no deck-dependence, no course mechanics ------------------------
_CTX = re.compile(r"on (?:this|the) slide|the slide (?:shows|says)|the deck|"
                  r"which edition|bring to lab|reading assignment|earplugs|"
                  r"how (?:are you|will you be) graded", re.I)
_ctx = [p[0][:60] for p in DECK["cards"] + DECK["matchCards"] if any(_CTX.search(t) for t in p)]
assert not _ctx, "deck-dependent or course-mechanics card: %r" % _ctx[:3]

# ---- guard: the image-only half of Centor is carded ------------------------
_all = " ".join(t for p in DECK["cards"] + DECK["matchCards"] for t in p)
assert "SUBTRACTS a point" in _all or "subtracts one" in _all, (
    "the modified Centor AGE adjustment is not carded -- it exists only inside "
    "slide 65's picture, so this is exactly what a deck-text build would lose")

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
    fo, fc = "/*PD2L4*/", "/*/PD2L4*/"
    if fo in src:
        src = re.sub(re.escape(fo) + r".*?" + re.escape(fc), "", src, flags=re.S)
    anchor = 'id: "pd2-ocular-exam"'
    assert anchor in src, "PD2 Lecture 3 deck not found -- has arcade.js changed?"
    i = src.index(anchor)
    j = src.index("] },", i) + len("] },")
    src = src[:j] + "\n" + fo + "\n" + render() + "\n" + fc + src[j:]

    # Register in the PD2 exam 1 group ONLY. [[arcade_integration]]
    grp = ('"pd2-clinical-reasoning", "pd2-derm-morphology", "pd2-derm-exam", '
           '"pd2-ocular-exam"')
    assert src.count(grp) == 1, (
        "the PD2 exam 1 deck group is not where it was (%d matches) -- registering "
        "blind would scope the edit to the wrong class" % src.count(grp))
    if '"pd2-ent-exam"' not in src.split(grp)[1][:60]:
        src = src.replace(grp, grp + ', "pd2-ent-exam"', 1)

    open(ARCADE, "w", encoding="utf-8").write(src)
    assert src.count('id: "pd2-ent-exam"') == 1, "deck landed twice"
    regs = sum(g.count('"pd2-ent-exam"') for g in re.findall(r"deckIds:\s*\[([^\]]*)\]", src))
    assert regs == 1, "deck registered in %d groups, want exactly 1" % regs
    print("added deck %s: %d cards, %d match pairs, registered in PD2 exam 1"
          % (DECK["id"], len(DECK["cards"]), len(DECK["matchCards"])))


if __name__ == "__main__":
    main()
