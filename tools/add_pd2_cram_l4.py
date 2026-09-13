#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add the Lecture 4 (Advanced ENT History and Exam) topics to the PD2 cram sheet.

The guide carries the reasoning; this carries what has to come back cold.

THE TUNING FORKS LEAD, because the weighting came with a number: "it will be
three points on test day." Very little else in this course is priced.

THE MODIFIED CENTOR SCORE IS HERE IN FULL, including the age adjustment, which
exists ONLY inside slide 65's picture -- the slide's text is a single caption
line. A cram sheet built by reading the deck's text would omit the half of the
rule most likely to be asked.

NO MARKDOWN IN THE ROWS. These are HTML-escaped and rendered as plain text, so
asterisks ship literally. I shipped 114 of them into the Clin Path sheet on
11 September before catching it; the guard below is the same one.

Appended after the Lecture 3 sections, in syllabus order. Idempotent.
"""
import os, re, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Physical Diagnosis 2 Exam 1",
                    "pd2-exam-1-cram-sheet.html")

TOPICS = [
 ("l4-forks", "★ TUNING FORKS — WORTH THREE POINTS", "#b8860b", "#f7efd9", "#fbf7ec", "#7a5a08", [
   ("Why this block leads", "“The Weber and the Rinne tests are BOTH HIGH YIELD … the difference between sensorineural and conductive hearing loss is ALSO HIGH YIELD … IT WILL BE THREE POINTS ON TEST DAY.”"),
   ("The two mnemonics, verbatim", "“RINNE IS UNDER THE PINNA” — the pinna is the outside of the ear, the Rinne fork goes on the MASTOID under it. “WEBER TELLS YOU WHETHER” — whether it is the RIGHT or the LEFT."),
   ("WEBER — where and what for", "Fork on the TOP OF THE HEAD or MID-FOREHEAD. Evaluates UNILATERAL loss by LATERALISATION. Normal = MIDLINE or equal in both ears."),
   ("WEBER in CONDUCTIVE loss", "Lateralises to the IMPAIRED ear. WHY: the block screens out room noise on that side, so the bone-conducted tone has that ear to itself."),
   ("WEBER in SENSORINEURAL loss", "Lateralises to the GOOD ear. WHY: inner ear or cochlear nerve damage impairs transmission on the affected side however the sound arrives."),
   ("RINNE — how, in order", "Fork on the MASTOID until the sound STOPS → move it CLOSE TO THE CANAL → ask if still heard. Bone conduction FIRST, air conduction SECOND."),
   ("RINNE normal", "AIR > BONE. A sound beside the ear is louder than one against the skull."),
   ("RINNE in CONDUCTIVE loss", "BONE ≥ AIR (abnormal). Vibration through bone BYPASSES the blocked external or middle ear and reaches an intact cochlea."),
   ("RINNE in SENSORINEURAL loss", "AIR > BONE — THE NORMAL RATIO PREVAILS. Rinne compares two routes to the SAME cochlea; damage degrades BOTH, so the ratio survives. Counterintuitive, and that is the test working."),
   ("★ THE WORKED CASE", "Rinne right = NORMAL. Weber lateralises RIGHT. Which ear has sensorineural loss? THE LEFT. Normal Rinne rules out conductive on the right; Weber goes AWAY from a sensorineural lesion."),
   ("What the forks CANNOT do", "They do NOT distinguish normal from BILATERAL sensorineural loss, and NOT normal from MIXED loss. Both tests work by COMPARING — a symmetrical loss looks normal."),
   ("The fork itself", "512 Hz — THE SMALLER ONE. Quiet room. Tap or “pinch” the fork."),
 ]),
 ("l4-hearing", "Conductive vs Sensorineural — the whole table", "#4a5c24", "#eaeee2", "#f4f6ef", "#3a4a1c", [
   ("Site", "CONDUCTIVE: external or middle ear. SENSORINEURAL: inner ear (cochlea) or CN VIII / central pathways."),
   ("Mechanism", "CONDUCTIVE: defective sound TRANSMISSION to the oval window. SENSORINEURAL: DESTRUCTION of hair cells or auditory nerve fibres."),
   ("Age of onset", "CONDUCTIVE: childhood to about 40. SENSORINEURAL: MIDDLE OR LATER YEARS."),
   ("Visible on otoscopy?", "CONDUCTIVE: usually VISIBLE — EXCEPT OTOSCLEROSIS. SENSORINEURAL: NOT visible. Otosclerosis is the conductive cause behind a normal-looking drum."),
   ("Noisy environments", "CONDUCTIVE: hearing SEEMS TO IMPROVE (the block attenuates the background too). SENSORINEURAL: WORSENS."),
   ("★ The patient’s own VOICE", "CONDUCTIVE: voice stays SOFT — inner ear and cochlear nerve intact, so they hear themselves fine. SENSORINEURAL: voice may be LOUD — they cannot hear themselves. A feedback loop, and a free bedside sign."),
   ("Frequencies", "SENSORINEURAL: HIGHER REGISTERS LOST, so sound is distorted. PRESBYCUSIS = high-frequency loss."),
   ("CONDUCTIVE causes", "Cerumen · foreign bodies · effusions · EXOSTOSES/OSTEOMAS (benign bony canal growths) · tumours · TM perforation · otosclerosis."),
   ("SENSORINEURAL causes", "Congenital · hereditary · PRESBYCUSIS · viral (RUBELLA, CYTOMEGALOVIRUS) · Ménière · NOISE · ACOUSTIC NEUROMA."),
   ("Whispered voice test", "TWO FEET BEHIND the patient (no lip reading), OCCLUDE the other ear, THREE-item sequence in a quiet whisper, TWICE. NORMAL = 3 or more of 6 correct. ABNORMAL = 4 of 6 INCORRECT."),
   ("Other bedside screens", "FINGER RUB and a WATCH."),
 ]),
 ("l4-vertigo", "The Vertigo Table", "#5f7a30", "#ecf0e4", "#f5f7f0", "#46591f", [
   ("How to read it", "DURATION column first, then HEARING. Those two separate all six."),
   ("BENIGN POSITIONAL VERTIGO", "Sudden, on ROLLING ONTO THE AFFECTED SIDE or tilting the head up. SECONDS TO UNDER A MINUTE per episode; the CONDITION lasts a few weeks and may recur. Hearing NOT affected. Tinnitus ABSENT."),
   ("VESTIBULAR NEURONITIS (acute labyrinthitis)", "Sudden. HOURS TO TWO WEEKS; may recur over 12–18 months. Hearing NOT affected. Tinnitus ABSENT. Nausea, vomiting, nystagmus."),
   ("MÉNIÈRE DISEASE", "Sudden. SEVERAL HOURS TO A DAY OR MORE, recurrent. SENSORINEURAL loss that recurs and eventually PROGRESSES. Tinnitus PRESENT and FLUCTUATING. PRESSURE OR FULLNESS in the affected ear."),
   ("DRUG TOXICITY", "Insidious or acute — LOOP DIURETICS, AMINOGLYCOSIDES, SALICYLATES, ALCOHOL. May or may not be reversible; partial adaptation. Hearing MAY be impaired."),
   ("ACOUSTIC NEUROMA", "Insidious, from CN VIII compression (vestibular branch). Variable duration. Hearing IMPAIRED ON ONE SIDE. Tinnitus PRESENT. MAY INVOLVE CN V AND VII."),
   ("CENTRAL VERTIGO", "Often sudden — BRAINSTEM LESION, ATHEROSCLEROSIS, MULTIPLE SCLEROSIS, VERTEBROBASILAR MIGRAINE, TIA. Variable but RARELY CONTINUOUS. Hearing NOT affected. Tinnitus ABSENT. OTHER BRAINSTEM DEFICITS — dysarthria, ataxia, crossed motor/sensory."),
   ("Hearing is the great divider", "Of the six, only MÉNIÈRE, DRUG TOXICITY and ACOUSTIC NEUROMA touch hearing."),
   ("“DIZZINESS” splits FOUR ways", "VERTIGO (spinning) · PRESYNCOPE (faint/lightheaded) · DISEQUILIBRIUM (unsteadiness/imbalance) · PSYCHIATRIC (anxiety, depression, alcohol/substances). The word means NOTHING until the patient explains it."),
   ("Tinnitus", "Sound with NO EXTERNAL SOURCE. WITH hearing loss AND vertigo = MÉNIÈRE."),
 ]),
 ("l4-earexam", "Ear Exam & Otoscopic Findings", "#3a5a40", "#e4ece6", "#f0f5f2", "#2b4430", [
   ("Before the otoscope", "Inspect and palpate the AURICLES, MASTOID and TRAGUS."),
   ("Otoscopy technique", "Pull the auricle UP, BACK AND AWAY FROM THE HEAD. LARGEST speculum that fits. ULNAR ASPECT of the hand contacts the patient (anchors the instrument). INSUFFLATE."),
   ("Why the LARGEST speculum", "Insufflation needs a SEAL. A small speculum leaks and the test becomes uninterpretable."),
   ("Leak check BEFORE inserting", "Attach the speculum, put a FINGER OVER THE TIP, squeeze the bulb — you should FEEL PRESSURE BUILD if there is no leak."),
   ("Insufflation pressure", "QUICK, FIRM BUT GENTLE. Reduced mobility → EFFUSION or THICKENED MEMBRANE."),
   ("Referred ear pain", "TMJ · TEETH · CERVICAL SPINE. Carried by CN V, VII, IX, X. Four sensory nerves to one small structure."),
   ("Ototoxic drugs to ask about", "AMINOGLYCOSIDES · ASPIRIN · NSAIDs · QUININE · FUROSEMIDE."),
   ("ACUTE otitis externa", "Canal SWOLLEN, NARROW, MOIST, PALE, TENDER; may be erythematous."),
   ("CHRONIC otitis externa", "Canal skin THICKENED, RED, ITCHY. Acute = PAIN, chronic = ITCH."),
   ("TM PERFORATION", "CENTRAL = does NOT extend to the margin. MARGINAL = involves the margin. Usually secondary to OTITIS MEDIA; may drain through it."),
   ("TYMPANOSCLEROSIS", "HYALINE DEPOSIT in the TM after severe otitis media or a healed perforation / tubes. USUALLY NOT CLINICALLY SIGNIFICANT."),
   ("SEROUS EFFUSION", "AMBER fluid, sometimes BUBBLES. After URI or a change in ATMOSPHERIC PRESSURE."),
   ("OTITIS MEDIA on the drum", "RED · LANDMARKS LOST · BULGING. Purulent effusion. STREP PNEUMONIAE and H. INFLUENZAE."),
   ("Bulging is GRADED", "Normal → mild → moderate → severe. The landmarks disappear as it progresses; that transition is what makes the effusion convincing."),
   ("BULLOUS MYRINGITIS", "PAINFUL HAEMORRHAGIC VESICLES on the TM and/or canal. MAY BE VIRAL OR BACTERIAL."),
   ("Know normal first", "“You have to see HUNDREDS of normal before you see anything abnormal … and then the abnormal will hit you in the face.”"),
 ]),
 ("l4-nose", "Nose & Sinuses", "#2f6f8a", "#e2edf1", "#f0f6f8", "#245568", [
   ("Turbinates", "SUPERIOR, MIDDLE, INFERIOR. The MAXILLARY SINUS DRAINS AT THE MIDDLE TURBINATE."),
   ("Why aggression matters up here", "“The roof of the mouth is the floor of your brain … anything that happened there CAN GO UP. Any infection in this area, you have to be a little more AGGRESSIVE.”"),
   ("Recent DENTAL WORK", "Can affect the MAXILLARY SINUSES — the sinus floor sits directly above the upper tooth roots."),
   ("Nasal drug history", "RHINITIS MEDICAMENTOSA (topical decongestants) and COCAINE. Neither is volunteered."),
   ("Epistaxis causes", "DIGITAL TRAUMA or other trauma · INFLAMMATION · DRY MUCOSA · FOREIGN BODY · TUMOUR. RECURRENT, or WITH BLEEDING/BRUISING ELSEWHERE → SYSTEMIC problem."),
   ("Patency test", "OCCLUDE ONE NOSTRIL AND BREATHE IN. UNILATERAL obstruction → FOREIGN BODY, TUMOUR, DEVIATED SEPTUM."),
   ("NASAL POLYP associations", "ALLERGIC RHINITIS · ASPIRIN SENSITIVITY · ASTHMA · CHRONIC SINUS INFECTION · CYSTIC FIBROSIS."),
   ("MUCOSA colour", "RED AND SWOLLEN → VIRAL rhinitis. PALE, BLUISH OR RED → ALLERGIC rhinitis."),
   ("PERFORATED septum", "TRAUMA · SURGERY · DRUG USE."),
   ("Sinus palpation", "Press UP on the FRONTAL sinuses AVOIDING THE EYES. Press UP on the MAXILLARY sinuses."),
   ("Transillumination", "DARK ROOM. FRONTAL: light UP under the brow close to the nose. MAXILLARY: light DOWN just below the inner corner of the eye, MOUTH OPEN. No glow → thickened mucosa/secretions. NOT SENSITIVE OR SPECIFIC."),
   ("★ ACUTE SINUSITIS — three rules", "(1) Local tenderness, pain, fever, nasal discharge are SUGGESTIVE. (2) THE COLOUR OF THE DISCHARGE IS NOT DIAGNOSTIC. (3) ACUTE BACTERIAL SINUSITIS IS UNLIKELY UNDER SEVEN DAYS — “it takes time to let it cook.”"),
   ("★ SEPTAL HAEMATOMA", "Injury disrupts vessels and PULLS THE LINING AWAY FROM THE CARTILAGE; blood collects between the two. URGENT DRAINAGE to prevent NECROSIS OF THE SEPTAL CARTILAGE — the cartilage has no blood supply of its own. “That blood HAS TO COME OUT.”"),
   ("Don’t pull what you can’t name", "A lesion everyone called a polyp turned out on imaging to be BRAIN TISSUE coming through. “You need to know what you’re looking at before you start pulling things.”"),
 ]),
 ("l4-oral", "Oral Cavity & Centor", "#7a5a8a", "#ece6f0", "#f5f2f8", "#5d4269", [
   ("★ THE FOUR CENTOR CRITERIA", "FEVER (above 100.4°F / 38°C) · TONSILLAR EXUDATES or swelling · SWOLLEN AND TENDER ANTERIOR CERVICAL NODES · ABSENCE OF COUGH. Three PRESENT and one ABSENT — that is the half people misremember."),
   ("Why ABSENCE of cough", "A cough points TOWARD a viral cause, so its ABSENCE raises the probability of streptococcal infection."),
   ("★ MODIFIED CENTOR — THE AGE POINTS", "3–14 years: +1. 15–44 years: 0. 45 AND OLDER: MINUS 1. This lives ONLY inside the slide’s PICTURE — the slide text is one caption line."),
   ("Score → risk of strep pharyngitis", "≤0 → 1–2.5% · 1 → 5–10% · 2 → 11–17% · 3 → 28–35% · ≥4 → 51–53%."),
   ("Score → action", "≤0: NO further testing or antibiotics. Middle: THROAT CULTURE or RAPID ANTIGEN TEST. ≥4: CONSIDER EMPIRIC TREATMENT."),
   ("UVULA deviation", "Failure to rise WITH DEVIATION TO THE OPPOSITE SIDE → CN X PARALYSIS. The working side pulls unopposed, so the uvula points AWAY from the lesion."),
   ("TONGUE deviation", "ASYMMETRIC PROTRUSION → CN XII LESION."),
   ("Tongue findings", "SMOOTH, BEEFY RED → VITAMIN B12 DEFICIENCY. SORE AND SMOOTH → nutritional deficiency. GEOGRAPHIC TONGUE IS BENIGN."),
   ("TONGUE CANCER — where and who", "LATERAL BORDER or UNDERSURFACE. INDURATED RED/WHITE lesions. MALES OVER 50."),
   ("Tongue palpation", "Hold with GAUZE in one hand, palpate with the other, THEN SWITCH HANDS for the opposite side — the only way to reach both lateral borders."),
   ("Dentures", "TAKE THEM OUT and look UNDERNEATH for ulcers and lesions."),
   ("Lip findings", "ANGULAR CHEILITIS (corners) · ANGIOEDEMA · HERPES SIMPLEX."),
   ("TRENCH MOUTH", "Necrotising ulcerative gingivitis = VINCENT’S ANGINA. “You can SMELL them across the room.” Bacteria DESTROY TISSUE as they go. From POOR DENTAL HYGIENE and drug use."),
   ("TORUS PALATINUS", "BENIGN BONY GROWTH in the MIDLINE of the HARD PALATE. A normal variant, not a mass."),
   ("Hoarseness causes", "VIRAL LARYNGITIS · VOICE OVERUSE · LARYNGEAL NERVE DAMAGE · REFLUX · SMOKING."),
 ]),
 ("l4-neck", "Neck, Thyroid & Head", "#8a5a2f", "#f0e8e0", "#f8f4ef", "#69431f", [
   ("★ NODE CHAINS — in order, and NAME THEM ALOUD", "PREAURICULAR · POSTAURICULAR · OCCIPITAL · TONSILLAR · SUBMANDIBULAR · SUBMENTAL · SUPERFICIAL (ANTERIOR) CERVICAL · POSTERIOR CERVICAL · DEEP CERVICAL · SUPRACLAVICULAR. “I need to know WHERE YOU’RE PUTTING YOUR FINGER” — the practical is graded on naming as you touch."),
   ("Palpation technique", "PADS of the INDEX and MIDDLE fingers."),
   ("NORMAL node", "ROUND OR OVOID · SMOOTH · MOBILE · NON-TENDER."),
   ("TENDER node", "INFLAMMATION."),
   ("HARD or FIXED node", "MALIGNANCY. Tender and soft is reactive; hard and fixed is not."),
   ("★ LEFT SUPRACLAVICULAR node", "METASTASIS FROM AN ABDOMINAL OR THORACIC MALIGNANCY. It drains territory far from the neck, so it redirects the whole search."),
   ("GENERALISED lymphadenopathy", "HIV/AIDS · EPSTEIN-BARR VIRUS · LYMPHOMA · LEUKAEMIA · SARCOIDOSIS."),
   ("★ LUDWIG’S ANGINA", "SUBMANDIBULAR SWELLING AND ERYTHEMA = CELLULITIS OF THE FLOOR OF THE MOUTH. LIFE THREATENING — THE AIRWAY. Usually from LOWER TEETH. “It spreads FAST … you have to work with it QUICKLY.”"),
   ("TRACHEAL deviation", "MASSES · ATELECTASIS · LARGE PNEUMOTHORAX."),
   ("Thyroid landmark", "Find the CRICOID CARTILAGE first — it locates the isthmus and lobes."),
   ("THYROID — diffuse enlargement splits on TEXTURE", "SOFT → GRAVES DISEASE. FIRM → HASHIMOTO THYROIDITIS. TENDER → THYROIDITIS."),
   ("Other thyroid findings", "ENDEMIC GOITRE → IODINE DEFICIENCY. SINGLE NODULE → cyst or tumour. MULTINODULAR → metabolic process; RISK OF MALIGNANCY WITH FAMILY HISTORY."),
   ("HEADACHE patterns", "MIGRAINE and TENSION are EPISODIC. MIGRAINE and CLUSTER are UNILATERAL. Migraine is in BOTH lists, so read the two features together."),
   ("HEADACHE red flags", "SUDDEN AND SEVERE → SUBARACHNOID HAEMORRHAGE. NEW, PROGRESSIVE AND PERSISTENT → MASS. Also consider MENINGITIS."),
   ("HEAD exam", "FINE HAIR → HYPERTHYROIDISM. COARSE HAIR → HYPOTHYROIDISM. Look for LICE, SEBORRHOEIC DERMATITIS, PSORIASIS, ATYPICAL NAEVI, ACTINIC KERATOSIS. SIZE: ENLARGED → HYDROCEPHALUS or PAGET DISEASE; SMALL → MICROCEPHALY."),
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
    ids = set(re.findall(r'id="([^"]+)"', s))
    dangling = [a for a in re.findall(r'<a[^>]*href="#([^"]+)"', s) if a and a not in ids]
    assert not dangling, "dangling jump links: %r" % dangling

    rows = "".join(r[0] + r[1] for t in TOPICS for r in t[6])
    assert "*" not in rows, (
        "markdown emphasis left in a cram row -- these rows are HTML-escaped and "
        "rendered as plain text, so asterisks ship literally. Use CAPITALS.")

    # The two things this sheet exists to carry.
    assert "THREE POINTS ON TEST DAY" in rows, \
        "the stated mark value on the tuning forks is missing"
    assert "45 AND OLDER: MINUS 1" in rows, (
        "the modified Centor AGE adjustment is missing -- it lives only inside slide 65's "
        "picture, so a deck-text reading loses exactly this")
    for w in ("WEBER", "RINNE", "MÉNIÈRE", "LUDWIG", "CENTOR"):
        assert w in rows.upper(), "%s missing from the sheet" % w

    open(CRAM, "w", encoding="utf-8").write(s)
    print("Lecture 4 cram topics added: %d sections, %d rows"
          % (len(TOPICS), sum(len(t[6]) for t in TOPICS)))
    print("tag balance, jump links, no-markdown, the three-point flag and the "
          "image-only Centor age adjustment all verified")


if __name__ == "__main__":
    main()
