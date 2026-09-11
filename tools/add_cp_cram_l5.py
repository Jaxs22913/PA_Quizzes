#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 5 (ENT) topics to the Clin Path I cram sheet.

The guide carries the reasoning; this carries only what has to come back cold.
Mechanism only -- CMS I Exam 3 covers this same condition list from the
management side, and slide 23's epistaxis management column is guarded against
below.

THE FIRST SECTION IS VERTIGO, not the anatomy, because he weighted it aloud:
"a third of my neurology questions were vertigo related. So know this, know
these things." The four peripheral causes separate on three axes only --
duration, hearing, preceding virus -- so that table leads.

TWO SLIDE CORRECTIONS ARE ON THE SHEET, because answering from the uncorrected
slide loses the mark: labyrinthitis is CONTINUOUS (he fixed it twice), and the
polyp heading means T HELPER CELL type 2. Guarded below -- if either drops out
of the rows, the build fails.

Appended after the Lecture 4 sections, in syllabus order. Idempotent.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Pathophysiology I Exam 1",
                    "cp-exam-1-cram-sheet.html")

TOPICS = [
 ("l5-vertigo", "★ VERTIGO — HE WEIGHTED THIS ONE", "#b8860b", "#f7efd9", "#fbf7ec", "#7a5a08", [
   ("Why it leads", "“On my board exams, A THIRD OF MY NEUROLOGY QUESTIONS WERE VERTIGO RELATED. So know this, know these things.” He also narrowed it: “we are more interested for this lecture on PERIPHERAL vertigo.”"),
   ("VERTIGO vs DIZZINESS — one line", "VERTIGO = HALLUCINATION OF MOTION from ASYMMETRICAL VESTIBULAR INPUT. Nystagmus + ataxia. NO SYNCOPE. DIZZINESS = non-vestibular impending faint, from CEREBRAL HYPOPERFUSION, ORTHOSTATIC HYPOTENSION or METABOLIC IMBALANCE — fainting IS on the table."),
   ("Why “no syncope” works", "Vertigo is a FALSE MOTION SIGNAL with NORMAL perfusion, so the patient does not faint. Dizziness IS the perfusion/metabolic problem. The patient says “dizzy” for both — the word tells you nothing."),
   ("PERIPHERAL vertigo", "Inner ear or CN VIII. SUDDEN onset · HORIZONTAL/ROTATIONAL nystagmus · FATIGABLE · SUPPRESSED BY VISUAL FIXATION. Causes: BPPV, MÉNIÈRE, LABYRINTHITIS, VESTIBULAR NEURITIS."),
   ("CENTRAL vertigo", "Brainstem/cerebellum. GRADUAL onset · VERTICAL or NON-SUPPRESSIBLE nystagmus · NEUROLOGICAL DEFICITS PRESENT. Causes: BRAINSTEM STROKE, MULTIPLE SCLEROSIS, CEREBELLAR TUMOUR."),
   ("Visual fixation — why it splits them", "Fixing the gaze lets VISION OVERRIDE the false vestibular signal. Works in PERIPHERAL. “You CANNOT do that with central” — central has broken the machinery that does the overriding."),
   ("THE FOUR PERIPHERAL — read DURATION first", "BPPV: UNDER 1 MINUTE, positional, NO hearing loss. MÉNIÈRE: HOURS, low-tone loss + aural fullness. LABYRINTHITIS: DAYS (improving over weeks), unilateral SNHL, AFTER A VIRAL URI. VESTIBULAR NEURITIS: days, NO hearing loss — nerve only."),
   ("BPPV mechanism", "CANALITHIASIS = OTOCONIA dislodged from the UTRICLE, floating FREE in the SEMICIRCULAR CANALS. “What you need to know for pathophysiology is that THEY CAN BECOME LOOSE” and hit structures, causing a false sensation of motion. Explains all three features: brief, positional, no hearing loss."),
   ("MÉNIÈRE mechanism", "ENDOLYMPHATIC HYDROPS — DEFECTIVE ENDOLYMPH RESORPTION (production is normal, DRAINAGE is not) → fluid accumulates in the membranous labyrinth, BALLOONING THE SCALA MEDIA until MICRO-RUPTURES occur. The ruptures are why it is episodic."),
   ("MÉNIÈRE — the classic TETRAD", "He said “classic symptom, TETRAD”: (1) EPISODIC VERTIGO, sudden, HOURS · (2) LOW-FREQUENCY FLUCTUATING TINNITUS · (3) PROGRESSIVE LOW-TONE SNHL · (4) AURAL FULLNESS/pressure."),
   ("MÉNIÈRE takes the LOW tones", "The only sensorineural loss here that starts LOW. Presbycusis and aminoglycosides take the HIGH ones. That contrast alone separates hydrops from the rest."),
   ("LABYRINTHITIS mechanism", "INFLAMMATORY SWELLING, VASCULAR CONGESTION and ENDOLYMPHATIC DISRUPTION across the SEMICIRCULAR CANALS AND THE COCHLEA. One continuous fluid space serves both, so BALANCE AND HEARING FAIL TOGETHER. Cause: VIRAL infection, recent viral URI."),
   ("★ SLIDE 17 IS WRONG — he corrected it TWICE", "The slide says labyrinthitis gives “EPISODIC” vertigo. IT IS CONTINUOUS. “This is not episodic. This is CONTINUOUS vertigo… classic symptoms is continuous, not episodic vertigo.” ANSWER CONTINUOUS — lasting DAYS, improving over WEEKS. If it were episodic it would be indistinguishable from Ménière."),
   ("LABYRINTHITIS nystagmus", "HORIZONTAL-ROTARY, fast phase beating AWAY from the affected side. Plus severe postural instability, gait ataxia, nausea."),
   ("VESTIBULAR NEURITIS", "Not on a slide of its own. “That’s just the same thing, but just INFLAMMATION OF THE NERVE FIBRES. That’s the only difference.” Whole labyrinth → hearing goes too; NERVE ALONE → only balance."),
   ("The balance organs", "SEMICIRCULAR CANALS (3 loops: sagittal, coronal, transverse) detect ROTATIONAL acceleration — ENDOLYMPH INERTIA bends the CUPULA in the AMPULLA. OTOLITH ORGANS — UTRICLE (horizontal), SACCULE (vertical) — detect LINEAR acceleration and GRAVITATIONAL POSITION."),
   ("Canals vs otoliths, in one line", "Canals answer “AM I TURNING?” Otoliths answer “WHICH WAY IS DOWN?” BPPV is an OTOLITH failure producing a CANAL symptom."),
 ]),
 ("l5-hearing", "Hearing Loss — Conductive vs Sensorineural", "#3b2a5e", "#e4e1e8", "#f1f0f4", "#2e2149", [
   ("CONDUCTIVE — site & mechanism", "EXTERNAL or MIDDLE ear. DEFECTIVE SOUND WAVE TRANSMISSION to the oval window."),
   ("SENSORINEURAL — site & mechanism", "INNER EAR (cochlea) or CN VIII / central pathways. DESTRUCTION OF HAIR CELLS or AUDITORY NERVE FIBRES."),
   ("WEBER — the one people invert", "CONDUCTIVE: lateralises to the AFFECTED ear. SENSORINEURAL: lateralises to the UNAFFECTED ear. Why: a blockage stops competing room noise reaching that cochlea, so the bone-conducted tone has that ear to itself."),
   ("RINNE", "CONDUCTIVE: BONE > AIR (abnormal). SENSORINEURAL: AIR > BONE (normal ratio)."),
   ("Causes — conductive", "CERUMEN IMPACTION · OTOSCLEROSIS · OTITIS MEDIA · TYMPANIC MEMBRANE PERFORATION."),
   ("Causes — sensorineural", "PRESBYCUSIS · OTOTOXIC DRUGS · NOISE TRAUMA · ACOUSTIC NEUROMA."),
   ("CONDUCTIVE — the 4 core mechanisms", "(1) OBSTRUCTION — impacted cerumen, foreign bodies, canal exostoses. (2) MASS LOADING — middle ear effusion, cholesteatoma. (3) STIFFNESS — otosclerosis (stapes footplate fixation). (4) DISCONTINUITY — temporal bone fracture, ossicular necrosis."),
   ("Mass loading vs stiffness — the confusable pair", "MASS LOADING ADDS WEIGHT to a chain that CAN STILL MOVE (effusion DAMPS). STIFFNESS STOPS THE CHAIN MOVING AT ALL (otosclerosis FIXES)."),
   ("CHOLESTEATOMA — off-deck, he said know it", "“That’s not in this presentation, but YOU SHOULD KNOW ABOUT IT.” A CHOLESTEROL COLLECTION forming a small mass in the ear; usually needs SURGICAL removal. Sits under MASS LOADING."),
   ("Transduction chain — memorise the order", "STAPES at OVAL WINDOW → pressure waves in SCALA VESTIBULI → displaces ENDOLYMPH → BASILAR MEMBRANE displacement SHEARS STEREOCILIA against the RIGID TECTORIAL MEMBRANE → opens TIP-LINK CHANNELS → rapid ION INFLUX FROM ENDOLYMPH → voltage-gated channels → GLUTAMATE onto CN VIII."),
   ("Read the chain backwards", "Break STEP 1 → CONDUCTIVE. Break STEPS 2–4 → SENSORINEURAL. Nothing in this lecture changes that division."),
 ]),
 ("l5-otosclerosis", "Otosclerosis, Ototoxicity & Noise", "#6a4fa3", "#eae6f2", "#f5f3f9", "#533e7f", [
   ("OTOSCLEROSIS — pathogenesis", "ABNORMAL OSTEOCLASTIC BONE RESORPTION followed by HYPERVASCULAR SPONGY OSTEOID REPLACEMENT around the OTIC CAPSULE and STAPES FOOTPLATE. Resorption FIRST, then the wrong bone grows back."),
   ("OTOSCLEROSIS — the one event", "ANKYLOSIS OF THE STAPES FOOTPLATE IN THE OVAL WINDOW halts vibration transfer → progressive CONDUCTIVE loss. The cochlea is untouched — mechanism 3, STIFFNESS."),
   ("OTOSCLEROSIS — demographics (he flagged it)", "Commonest in YOUNG-TO-MIDDLE-AGED FEMALES · ACCELERATED BY PREGNANCY · 50% AUTOSOMAL DOMINANT with VARIABLE PENETRANCE."),
   ("The sorting rule for ototoxicity", "“Ototoxic medications, ALMOST ALWAYS REVERSIBLE, EXCEPT FOR SOME LIKE PLATINUM CHEMOTHERAPY.”"),
   ("AMINOGLYCOSIDES — gentamicin, tobramycin", "Induce REACTIVE OXYGEN SPECIES that selectively destroy OUTER HAIR CELLS starting at the COCHLEAR BASE → HIGH PITCH LOST FIRST. Permanent."),
   ("PLATINUM — cisplatin, carboplatin", "CROSS-LINKS DNA IN STRIA VASCULARIS CELLS → compromises ENDOLYMPH ION HOMEOSTASIS → BILATERAL PERMANENT sensorineural loss."),
   ("FUROSEMIDE", "Alters the STRIA VASCULARIS POTENTIAL → REVERSIBLE conductive/sensorineural loss."),
   ("SALICYLATES", "Inhibit the PRESTIN motor protein in OUTER HAIR CELLS → TINNITUS."),
   ("Cisplatin vs furosemide — same target", "BOTH hit the STRIA VASCULARIS. Cisplatin CROSS-LINKS ITS DNA and kills it (PERMANENT); furosemide only SHIFTS ITS POTENTIAL (REVERSIBLE). That is the whole difference."),
   ("Why high frequencies go first", "ANATOMICAL, not chemical: the COCHLEAR BASE encodes HIGH pitch, and the base is where the damage starts. Same geometry drives presbycusis."),
   ("NOISE — the number", "Long-term chronic exposure ABOVE 85 dB → IRREVERSIBLE STEREOCILIA DEGENERATION and HAIR CELL APOPTOSIS. 85 dB = occupational limit · 90 lawnmower/traffic · 120 ambulance siren = ACOUSTIC TRAUMA · 140 jet engine/blast = IMMEDIATE DAMAGE."),
   ("PRESBYCUSIS", "GRADUAL, SYMMETRICAL, BILATERAL sensorineural loss in older adults. Begins with HIGH-FREQUENCY tones — the speech CONSONANTS /s/, /f/, /t/. Complaint is never “I can’t hear”, it is “I CAN’T FOLLOW CONVERSATION IN A NOISY ROOM”: vowels carry volume, CONSONANTS CARRY MEANING."),
 ]),
 ("l5-otitis", "Otitis Media & Externa", "#8f5aa8", "#efe8f3", "#f7f3f9", "#704683", [
   ("Eustachian tube dysfunction — the sequence", "TUBE FAILS TO OPEN PERIODICALLY → OXYGEN AND NITROGEN ABSORBED INTO THE MIDDLE EAR MUCOSA → NEGATIVE MIDDLE EAR PRESSURE. The middle ear is a SEALED AIR-FILLED BOX whose only vent stopped working."),
   ("OTITIS MEDIA — bacterial", "STREPTOCOCCUS PNEUMONIAE · HAEMOPHILUS INFLUENZAE · MORAXELLA CATARRHALIS. He scoped these: “not really for my exam, BUT LIKE BOARD EXAMS.”"),
   ("OTITIS MEDIA — viral", "RESPIRATORY SYNCYTIAL VIRUS · RHINOVIRUS · INFLUENZA · ADENOVIRUS. Typically after a URI."),
   ("OTITIS EXTERNA — bacterial (80–90%)", "PSEUDOMONAS AERUGINOSA and STAPHYLOCOCCUS AUREUS. “Swimmer’s ear”."),
   ("OTITIS EXTERNA — fungal", "ASPERGILLUS NIGER or CANDIDA ALBICANS, secondary to PROLONGED ANTIBIOTIC USE or HYPERHUMID CONDITIONS. Same logic as thrush: remove the competition or keep it wet."),
 ]),
 ("l5-rhino", "Rhinology", "#2f6f8a", "#e2edf1", "#f0f6f8", "#245568", [
   ("Rhinitis vs rhinosinusitis", "RHINITIS = NOSE. RHINOSINUSITIS = NOSE AND SINUSES — which is why FACIAL PAIN belongs to rhinosinusitis."),
   ("ACUTE rhinosinusitis", "UNDER 4 WEEKS. Usually VIRAL (rhinovirus, influenza); secondary bacterial = STREP PNEUMONIAE or H. INFLUENZAE. PURULENT rhinorrhoea, facial pain, nasal congestion."),
   ("CHRONIC rhinosinusitis", "BEYOND 12 WEEKS DESPITE THERAPY, often WITH NASAL POLYPS. Usually a secondary infection layered on an allergic process."),
   ("ALLERGIC RHINITIS", "IgE-MEDIATED TYPE 1 HYPERSENSITIVITY of nasal mucosa to inhaled allergens. CLEAR rhinorrhoea, nasal itching, sneezing, BOGGY TURBINATES, allergic “shiners”. (He de-scoped it: “plain vanilla… I don’t wanna ask about this.”)"),
   ("Discharge colour — fastest discriminator", "ALLERGIC = CLEAR. ACUTE BACTERIAL SINUSITIS = PURULENT."),
   ("NASAL POLYPS", "NON-NEOPLASTIC, benign OEDEMATOUS masses from mucous membranes of the SINUS OSTIA or ETHMOID AIR CELLS. Not new tissue — existing mucosa waterlogged."),
   ("POLYPS — molecular pathway", "Chronic TYPE 2 allergic response · cytokines IL-4, IL-5, IL-13 · TISSUE EOSINOPHIL INFLUX."),
   ("★ SLIDE 21 — he corrected the heading", "The slide says “Type 2 Inflammation”. He stopped to fix it: “I meant to put T HELPER CELL TYPE 2 allergic inflammation. VERY IMPORTANT.” Then: “I’m not gonna ask you about that, but just so you know.” Know what it means; don’t expect to be asked."),
   ("TURBINATE HYPERTROPHY", "Enlargement of the INFERIOR turbinates from VENOUS SINUSOID ENGORGEMENT, MUCOSAL OEDEMA or BONY HYPERTROPHY. Triggers: allergic rhinitis, vasomotor instability, and REBOUND HYPERAEMIA from topical decongestants."),
   ("RHINITIS MEDICAMENTOSA", "REBOUND HYPERAEMIA from OVERUSE OF TOPICAL DECONGESTANT SPRAYS — the spray produces the congestion it was bought to relieve."),
   ("DEVIATED SEPTUM — the physics", "POISEUILLE’S LAW — even small airway narrowing DRAMATICALLY increases resistance. He put the split at “97% of all air going through one side.”"),
   ("DEVIATED SEPTUM — consequences", "CHRONIC OBSTRUCTION → mouth-breathing, aggravates SLEEP APNOEA · MUCOSAL DRYING + EPISTAXIS from TURBULENT airflow · OLFACTORY DYSFUNCTION because air FAILS TO REACH THE CRIBRIFORM PLATE · SINUS OSTIA BLOCKAGE → mucus stasis, hypoxia, secondary bacterial rhinosinusitis."),
   ("★ The compensation is CONTRALATERAL", "The WIDE cavity undergoes INFERIOR TURBINATE HYPERTROPHY to humidify the increased air volume — the hypertrophied turbinate is on the OPEN side, NOT the blocked one. So a ONE-SIDED deviation can obstruct BOTH sides. Reverse the inference: find big inferior turbinates → go looking for the deviation."),
   ("EPISTAXIS — ANTERIOR (90%)", "Source: KIESSELBACH’S PLEXUS, anterior septum. Aetiology all LOCAL: digital trauma, LOW HUMIDITY, localised mucosal erosion, mild rhinitis. Unilateral anterior bleeding."),
   ("EPISTAXIS — POSTERIOR (10%)", "Source: WOODRUFF’S PLEXUS, posterolateral wall. Aetiology all SYSTEMIC: HYPERTENSION, ATHEROSCLEROSIS, ANTICOAGULANT THERAPY, COAGULOPATHY. PROFUSE bleeding down the posterior pharynx, AIRWAY RISK."),
   ("Why posterior is the dangerous one", "WOODRUFF’S carries FAR MORE ARTERIAL SUPPLY than Kiesselbach’s, and it sits where you cannot compress. “That thing may not stop bleeding.” But “you will usually only see ANTERIOR epistaxis.”"),
 ]),
 ("l5-larynx", "Larynx & Neck", "#3f8a55", "#e6f1e9", "#f2f8f4", "#265735", [
   ("VOCAL CORD NODULES", "BILATERAL, SYMMETRICAL fibrous CALLUSES at the junction of the ANTERIOR 1/3 and POSTERIOR 2/3. From CHRONIC mechanical PHONOTRAUMA (yelling, cheering) → BASEMENT MEMBRANE HYALINISATION. “Singer’s nodes”."),
   ("VOCAL CORD POLYPS", "UNILATERAL, soft/fluid-filled or vascular, PEDUNCULATED, on the MIDDLE THIRD of the true cord. From ACUTE SEVERE voice strain or VOCAL CORD HAEMORRHAGE → localised inflammatory healing response."),
   ("Nodules vs polyps, in one line", "CHRONIC + BILATERAL vs ACUTE + UNILATERAL. Repeated impact damages BOTH cords at the SAME POINT; one violent strain or bleed damages ONE. (He misspoke “bilateral” for polyps and corrected himself — the slide and its picture both say UNILATERAL.)"),
   ("Hyalinisation vs callus", "“HYALINISATION IS NOT THE SAME AS CALLUS FORMATION. Hyalinisation is a PINK, EXCESSIVE MEMBRANE GROWTH. Callus is a FIBROUS MATERIAL FORMATION — but it can be EITHER OR in the nodules.”"),
   ("TONSILLITIS", "Acute VIRAL or BACTERIAL inflammation of the PALATINE TONSILS and pharyngeal mucosa. Bacterial is usually GROUP A STREPTOCOCCUS."),
   ("TONSILLITIS — symptoms", "Sore throat · ODYNOPHAGIA (pain on swallowing) · fever · TONSILLAR EXUDATES · TRISMUS · ASYMMETRIC TONSILLAR DEVIATION IF COMPLICATED BY ABSCESS."),
   ("Asymmetry is the alarm", "Tonsillitis is SYMMETRICAL. An ABSCESS pushes ONE tonsil across the midline and CLAMPS THE JAW. Chronic swollen tonsils that OBSTRUCT THE AIRWAY are an emergency. Epiglottitis sits “a little inferior to the tonsillitis”."),
   ("Bacterial vs viral tonsils (from the picture)", "WHITE PATCHES or NODULES on red swollen tonsils → BACTERIAL. RED AND SWOLLEN WITH NO EXUDATE → VIRAL."),
   ("CERVICAL LYMPHADENOPATHY — reactive", "Usually BENIGN enlargement responding to regional head/neck infection (viral URI, OTITIS MEDIA, DENTAL DISEASE) or systemic inflammatory conditions. PALPABLE AND TENDER."),
   ("★ The red-flag COMBINATION", "PERSISTENT + RUBBERY OR MATTED + SUPRACLAVICULAR OR CERVICAL + OLDER ADULT → immediate assessment to rule out LYMPHOMA. Not any large node — the combination."),
   ("Tender vs matted", "TENDER AND SOFT = REACTIVE. PAINLESS, RUBBERY, MATTED = not. MATTED means the nodes have LOST THEIR INDIVIDUAL CAPSULES and move as one mass."),
 ]),
]


def section(t):
    tid, title, acc, bg, zeb, ink, rows = t
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (H.escape(a), H.escape(b))
        for a, b in rows)
    return ('\n  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">\n'
            '    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s</h2></div>\n'
            '    <div class="scroll">\n      <table>\n'
            '        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>\n'
            '        <tbody>\n%s\n        </tbody>\n      </table>\n    </div>\n  </section>\n'
            % (tid, acc, bg, zeb, ink, acc, H.escape(title), body))


def main():
    s = open(CRAM, encoding="utf-8").read()
    for tid in [t[0] for t in TOPICS]:
        s = re.sub(r'\n  <section class="topic" id="%s".*?\n  </section>\n' % re.escape(tid),
                   "", s, flags=re.S)
        s = re.sub(r'      <a href="#%s"[^\n]*\n' % re.escape(tid), "", s)

    last = s.rindex('<section class="topic"')
    end = s.index("\n  </section>", last) + len("\n  </section>\n")
    links_anchor = s.rindex("</a>\n", 0, s.index("</nav>") if "</nav>" in s else len(s)) + len("</a>\n")
    links = "".join(
        '      <a href="#%s" style="color:%s"><span class="dot" style="background:%s"></span>%s</a>\n'
        % (t[0], t[5], t[2], t[1]) for t in TOPICS)
    s = s[:end] + "".join(section(t) for t in TOPICS) + s[end:]
    s = s[:links_anchor] + links + s[links_anchor:]

    for tag in ("section", "table", "tbody", "thead", "tr", "td", "th", "div"):
        o, c = len(re.findall(r"<%s[ >]" % tag, s)), s.count("</%s>" % tag)
        assert o == c, "%s: %d open, %d close" % (tag, o, c)
    assert "*" not in "".join(r[0] + r[1] for t in TOPICS for r in t[6]), (
        "markdown emphasis left in a cram row -- these rows are HTML-escaped and "
        "rendered as plain text, so asterisks ship literally. Use CAPITALS.")
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling

    rows = "".join(r[0] + r[1] for t in TOPICS for r in t[6])

    # Management is CMS I's, not this course's. Slide 23 hands it to you on a
    # plate right beside the pathophysiology. [[clin_path_exam_spec]]
    for banned in ("oxymetazoline", "balloon pack", "cautery", "emboli", "myringotomy",
                   "Epley", "tonsillectomy", "stapedectomy"):
        assert banned.lower() not in rows.lower(), (
            "%r is MANAGEMENT -- this course is pathophysiology only, and slide 23's "
            "management column is the trap" % banned)

    # Both live corrections must survive. Answering from the uncorrected slide
    # loses the mark, so if either drops out the sheet is worse than useless.
    assert "CONTINUOUS" in rows and "not episodic" in rows.lower(), \
        "the slide-17 labyrinthitis correction is missing from the cram rows"
    assert "T HELPER CELL TYPE 2" in rows.upper(), \
        "the slide-21 polyp correction is missing from the cram rows"

    # The four peripheral vertigos must each be nameable off this sheet.
    for v in ("BPPV", "MÉNIÈRE", "LABYRINTHITIS", "VESTIBULAR NEURITIS"):
        assert v in rows.upper(), "%s is missing -- he weighted vertigo above everything" % v

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 5 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance, jump links, management guard, both slide corrections "
          "and vertigo coverage verified")


if __name__ == "__main__":
    main()
