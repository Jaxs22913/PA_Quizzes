#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Add Lectures 11 and 12 to the CMS I Exam 2 cram sheet.

Additive and idempotent, fenced. The cram sheet is the night-before sheet:
the reasoning stays in the guide, this carries only what has to be recalled
cold. Capitals mark the discriminator in each row, matching the sheet's
existing house style.
"""
import io, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
CRAM = os.path.join(os.path.dirname(HERE), "Clinical Medicine and Surgery I Exam 2",
                    "cms-exam-2-cram-sheet.html")
OPEN, CLOSE = "<!--CMSE2L1112-CRAM-->", "<!--/CMSE2L1112-CRAM-->"


def sec(sid, title, acc, bg, zebra, ink, rows, star=False):
    body = "\n".join(
        '          <tr><td class="h">%s</td><td>%s</td></tr>' % (a, b) for a, b in rows)
    return """
  <section class="topic" id="%s" style="--acc:%s;--acc-bg:%s;--acc-zebra:%s;--acc-ink:%s">
    <div class="shead"><span class="dot" style="background:%s"></span><h2>%s%s</h2></div>
    <div class="scroll">
      <table>
        <thead><tr><th class="term">Term</th><th>What you need to know</th></tr></thead>
        <tbody>
%s
        </tbody>
      </table>
    </div>
  </section>
""" % (sid, acc, bg, zebra, ink, acc, "&#9733; " if star else "", title, body)


SECTIONS = "".join([

 sec("avl-rule", "THE RULE SHE SAID TWICE", "#b8860b", "#f5eedd", "#faf7ee", "#906909", [
  ("SUDDEN VISION LOSS", "IS A STROKE UNTIL PROVEN OTHERWISE. You can have a stroke with NO other symptom. EVERYONE GETS AN MRA (magnetic resonance angiography)."),
  ("The four questions", "ONE EYE OR BOTH? · SUDDEN OR GRADUAL? · CENTRAL OR PERIPHERAL? · PAINFUL OR PAINLESS? These four decide the diagnosis, not the fundus."),
  ("PAINFUL", "ACUTE ANGLE-CLOSURE GLAUCOMA (severe, at rest) · OPTIC NEURITIS (on eye MOVEMENT). Everything else here is PAINLESS."),
  ("BOTH EYES", "PAPILLEDEMA, or a lesion at/behind the CHIASM. Everything else is MONOCULAR."),
  ("&ldquo;CURTAIN&rdquo; = TWO DIAGNOSES", "AMAUROSIS FUGAX &mdash; curtain LIFTS in seconds to minutes. RETINAL DETACHMENT &mdash; curtain STAYS and advances over days. DURATION separates them."),
  ("Refer emergently", "ANY patient OVER 50 with SUDDEN VISUAL LOSS."),
 ], star=True),

 sec("amaurosis", "Amaurosis Fugax", "#2d3f7a", "#e2e4ec", "#f0f2f6", "#23315f", [
  ("What", "TRANSIENT MONOCULAR vision loss. &ldquo;FLEETING BLINDNESS.&rdquo; SECONDS TO MINUTES. PAINLESS."),
  ("IF IT LASTED HOURS", "IT IS NOT A TIA (transient ischemic attack). Duration is the first filter."),
  ("Cause", "Retinal emboli, CAROTID or CARDIAC. Most commonly a TIA (transient ischemic attack). Also RETINAL VASCULAR SPASM."),
  ("Risks", "Older age, DM (diabetes mellitus), HTN (hypertension), ATHEROSCLEROSIS, cardiac VALVE disease, IVDU (intravenous drug use), SICKLE CELL, coagulation disorders, RAYNAUD&rsquo;S."),
  ("Workup", "CAROTID DOPPLER if carotid suspected · ECHO (echocardiogram) if cardiac · MRA for everyone."),
  ("Treatment", "TREAT THE UNDERLYING CAUSE. Stroke risk &rarr; ASA (aspirin) + CLOPIDOGREL. Carotid emboli &rarr; ENDARTERECTOMY. Raynaud&rsquo;s/spasm &rarr; CALCIUM CHANNEL BLOCKERS."),
  ("Prognosis", "~85% FULL RECOVERY. The rest PROGRESS TO CRAO (central retinal artery occlusion)."),
 ]),

 sec("glaucoma-avl", "Glaucoma &mdash; Acute vs Chronic", "#a4502a", "#f2e6e1", "#f9f3f0", "#803e21", [
  ("ACUTE = CLOSED ANGLE", "IRIS BLOCKS THE DRAINAGE CIRCUIT. SEVERE SUDDEN EYE PAIN, HEADACHE, NAUSEA/VOMITING, COLOURED HALOS, decreased vision. HAZY CORNEA, pupillary dilation, narrow/occluded angle."),
  ("THE PRESSURE", "40&ndash;80 mmHg on TONOMETRY or GONIOSCOPY."),
  ("Acute treatment", "TOPICAL PILOCARPINE (alpha-blocker) or TIMOLOL (beta-blocker) · IV ACETAZOLAMIDE then MANNITOL or ISOSORBIDE. DEFINITIVE = LASER PERIPHERAL IRIDOTOMY, 1&ndash;2 DAYS AFTER ONSET."),
  ("Acute RISK FACTORS", "SYSTEMIC ANTICHOLINERGICS (atropine) · NEBULIZED BRONCHODILATORS · prior ANTERIOR UVEITIS · lens dislocation · AFRICAN AMERICAN RACE. Obstruction from TUMOUR or SCARRING."),
  ("CHRONIC = OPEN ANGLE", "TRABECULAR MESHWORK abnormality by the CANAL OF SCHLEMM, from AGING. MUCH MORE COMMON. ASYMPTOMATIC in most. PAINLESS."),
  ("Chronic field loss", "PERIPHERAL FIRST &rarr; patients say &ldquo;TUNNEL VISION&rdquo; &rarr; then blindness."),
  ("THE CLASSIC SIGN", "OPTIC NERVE CUPPING &mdash; increased CUP-TO-DISC RATIO. Also RIM PITTING, BAYONETING (vessels with narrow angulations), SPLINTER HAEMORRHAGES, rim thinning."),
  ("Chronic pressure", "MAY BE NORMAL OR ELEVATED &mdash; nerve damage occurs either way."),
  ("Chronic risks", "AFRICAN AMERICAN race, HISPANIC, ADULTS OVER 40, DM, age, FAMILY HISTORY, HTN, MYOPIA."),
  ("Chronic treatment", "FIRST-LINE: LATANOPROST · TAFLUPROST · TIMOLOL drops. Refractory/advanced &rarr; LASER TRABECULOPLASTY. SURGERY IS DEFINITIVE FOR BOTH FORMS."),
  ("The missed case", "An INTRACTABLE HEADACHE LOCALISED BEHIND THE EYE with a RED EYE. Glaucoma is a LEADING CAUSE OF BLINDNESS WORLDWIDE."),
 ]),

 sec("neuritis", "Optic Neuritis", "#2f6b5a", "#e2eae8", "#f0f5f3", "#255346", [
  ("Who", "18&ndash;45 YEARS OLD, 75% FEMALE. A much YOUNGER group than everything else here."),
  ("Cause", "MULTIPLE SCLEROSIS, autoimmune, POSTVIRAL, or idiopathic."),
  ("Symptoms", "UNILATERAL loss over HOURS TO SEVERAL DAYS · PAINFUL EYE MOVEMENT · central vision loss · LOSS OF COLOUR VISION."),
  ("Signs", "Often a NORMAL-APPEARING DISC. RELATIVE AFFERENT PUPILLARY DEFECT (MARCUS GUNN)."),
  ("Workup", "REFER TO OPHTHALMOLOGY. Slit lamp, dilated fundoscopy, COLOUR VISION + neuro exam. MRI (magnetic resonance imaging) BRAIN AND ORBITS, WITH AND WITHOUT CONTRAST."),
  ("THE THRESHOLD", "&ge;2 CHARACTERISTIC DEMYELINATING LESIONS &rarr; treat and refer to NEUROLOGY / NEURO-OPHTHALMOLOGY."),
  ("Treatment &amp; prognosis", "CORTICOSTEROIDS if demyelinating. SPONTANEOUS RECOVERY IS THE RULE &mdash; improves within WEEKS, usually NORMAL WITHIN A YEAR."),
  ("Education", "RECURRENCE = GREATER RISK OF MS (multiple sclerosis). Find the cause; do not just treat the episode."),
 ]),

 sec("detachment", "Retinal Detachment", "#7a2f5f", "#ece2e9", "#f6f0f4", "#5f254a", [
  ("What", "Traction detachment, commonly AFTER A RETINAL TEAR OR HOLE. Types: RHEGMATOGENOUS, TRACTION, SEROUS/EXUDATIVE."),
  ("Who", "MOST COMMON AFTER AGE 50 &mdash; the vitreous SHRINKS with age."),
  ("Risks", "MYOPIA, TRAUMA, CATARACT EXTRACTION, DM, tumour, CONNECTIVE TISSUE DISEASE, family history."),
  ("FLASHES &amp; FLOATERS", "REPRESENT THE TEAR, not the detachment."),
  ("Then", "GREY OR BLACK SHADOWS peripherally, may cover the WHOLE EYE WITHIN DAYS. &ldquo;CURTAIN or DARK CLOUD.&rdquo; PAINLESS."),
  ("MACULA INVOLVED", "&rarr; SUDDEN LOSS OF VISION in that eye."),
  ("Odd but useful", "VISION CHANGES WITH HEAD POSITION &mdash; the retina is floating loose."),
  ("Fundus", "ELEVATED GREY retina WITH FOLDS · PIGMENTED WELL-DEMARCATED area · TEARS ARE ORANGE AND CRESCENT SHAPED. ULTRASOUND IS MORE SENSITIVE THAN FUNDOSCOPY and types it."),
  ("Treatment", "EMERGENCY &mdash; REFER IMMEDIATELY. Surgery urgently or within a week by type: LASER PHOTOCOAGULATION · CRYOTHERAPY · PNEUMATIC RETINOPEXY · VITRECTOMY · SCLERAL BUCKLE."),
 ]),

 sec("occlusions", "The Four Vascular Occlusions", "#8f5aa8", "#efe8f3", "#f7f3f9", "#704683", [
  ("CRAO &mdash; CENTRAL RETINAL ARTERY OCCLUSION", "EMBOLUS. A STROKE IN THE EYE. IRREVERSIBLE DAMAGE AFTER 90 MINUTES."),
  ("CRAO presentation", "PAINLESS PROFOUND LOSS OVER SECONDS. Acuity COUNTING FINGERS TO LIGHT PERCEPTION. &ldquo;ISLAND&rdquo; OF VISION IN THE TEMPORAL FIELD."),
  ("CRAO PUPIL &mdash; the clue", "SLOW TO DIRECT LIGHT, BUT BRISK WHEN THE OTHER EYE IS ILLUMINATED."),
  ("CRAO fundus", "PALE SWELLING of the posterior segment + CHERRY-RED SPOT AT THE FOVEA. Emboli in the central artery."),
  ("CRAO treatment", "HIGH-CONCENTRATION INHALED O&#8322; + DIGITAL MASSAGE OVER THE EYELID · IV ACETAZOLAMIDE · ANTERIOR CHAMBER PARACENTESIS · THROMBOLYTIC INTO THE OPHTHALMIC ARTERY WITHIN 8 HOURS."),
  ("CRAO systemic", "STROKE RISK RISES AT ONSET &mdash; if plaque reached a tiny retinal artery, there is far more in that carotid."),
  ("CRVO &mdash; CENTRAL RETINAL VEIN OCCLUSION", "THROMBUS. MORE COMMON THAN CRAO. SUDDEN PAINLESS loss; sometimes GRADUAL OVER DAYS TO WEEKS."),
  ("CRVO fundus", "&ldquo;BLOOD AND THUNDER&rdquo; &mdash; DISC SWELLING, VENOUS DILATION, COTTON WOOL SPOTS, RETINAL HAEMORRHAGES."),
  ("CRVO treatment", "URGENT OPHTHALMOLOGY REFERRAL TO RESTORE BLOOD FLOW. Evaluate and treat the underlying disorders."),
  ("Shared risks", "HTN · DM · HLD (hyperlipidaemia) · RAYNAUD&rsquo;S · AGE &gt;50 · HYPERCOAGULABLE · GIANT CELL ARTERITIS · ENDOCARDITIS · ATRIAL MYXOMA · OBESITY. CRAO adds ATRIAL FIBRILLATION."),
  ("Shared later", "NEOVASCULARIZATION WEEKS TO MONTHS AFTER the occlusion, in both."),
  ("Shared confirmatory", "COLOUR FUNDUS PHOTOGRAPHY + FLUORESCEIN ANGIOGRAPHY."),
  ("BRAO and BRVO &mdash; the BRANCH forms", "SAME DISEASE, SMALLER VESSEL. A BRANCH is blocked, not the trunk &rarr; ONLY PART OF THE RETINA affected, PARTIAL field loss. Everything else identical."),
 ]),

 sec("papilledema", "Papilledema", "#7a5a2e", "#ece8e2", "#f6f3f0", "#5f4624", [
  ("THE DISTINCTION", "INTRACRANIAL pressure, NOT INTRAOCULAR. Every other condition here is pressure inside the GLOBE."),
  ("Causes", "TUMOUR · TRAUMA · INTRACRANIAL INFECTION (meningitis) · HAEMORRHAGE · VITAMIN A TOXICITY."),
  ("Visual symptoms", "NON-SPECIFIC: FLICKERING, BLURRY, DOUBLE VISION."),
  ("Systemic symptoms", "Signs of raised ICP (intracranial pressure): NAUSEA, VOMITING, HEADACHE."),
  ("Fundus", "ENGORGED RETINAL VEINS · SWOLLEN OPTIC DISC · &plusmn; retinal haemorrhages. BILATERAL."),
  ("Phases", "ACUTE may have HAEMORRHAGES and COTTON WOOL SPOTS. CHRONIC = elevation + blurred margins, NO haemorrhage or cotton wool spots. ATROPHIC = the AXONS HAVE DIED."),
  ("Workup", "MRI and/or CT (computed tomography) HEAD to rule out a MASS, then LUMBAR PUNCTURE &mdash; INCREASED OPENING PRESSURE CONFIRMS. TREAT THE UNDERLYING DISORDER."),
  ("vs GLAUCOMA", "PAPILLEDEMA PUSHES THE DISC OUT. GLAUCOMA CUPS IT IN."),
 ]),

 sec("aion", "Anterior Ischemic Optic Neuropathy", "#2f7d76", "#e2edec", "#f0f6f5", "#25625c", [
  ("Both forms", "SUDDEN PAINLESS loss of SIDE OR CENTRAL vision · SWELLING AND PALENESS of the optic nerve head · ONE EYE FIRST, SECOND EYE AT RISK."),
  ("NAION &mdash; NON-arteritic", "90&ndash;95% OF CASES. AGE 40&ndash;60. Linked to a SMALL STRUCTURAL OPTIC DISC = &ldquo;DISC AT RISK.&rdquo; HTN, DM, HIGH CHOLESTEROL, SLEEP APNEA."),
  ("NAION workup", "A DIAGNOSIS OF EXCLUSION. WORKUP IS IDENTICAL TO ARTERITIC &mdash; make sure there is no GCA. Then evaluate HTN, DM, ANAEMIA; neuroimaging if unclear."),
  ("NAION management", "OBSERVATION + CARDIOVASCULAR RISK MODIFICATION. Consider AVOIDING ANTIHYPERTENSIVES AT BEDTIME &mdash; NOCTURNAL HYPOTENSION worsens it."),
  ("AAION &mdash; ARTERITIC", "Caused by GIANT CELL (TEMPORAL) ARTERITIS. AGE 55+. Usually ELDERLY, CAUCASIAN WOMEN. A MEDICAL EMERGENCY."),
  ("AAION systemic", "MALAISE, WEIGHT LOSS, FEVER · HEADACHE in the TEMPORAL or OCCIPITAL region · SCALP TENDERNESS on combing the hair · JAW CLAUDICATION on chewing. NO prior headache history &rarr; new temporal headache = the warning sign."),
  ("AAION workup", "ESR (erythrocyte sedimentation rate) + CRP (C-reactive protein) rule GCA in or out. TEMPORAL ARTERY BIOPSY IS THE GOLD STANDARD &mdash; but DO NOT WAIT FOR IT."),
  ("AAION treatment", "IV METHYLPREDNISOLONE &times;3 DAYS, then SLOW ORAL TAPER to the lowest suppressive dose &mdash; TYPICALLY 6 TO 12 MONTHS. Add FAMOTIDINE for GI ULCER PROPHYLAXIS."),
  ("AAION prognosis", "Depends on DURATION and WHEN STEROIDS STARTED. Untreated &rarr; BLINDNESS."),
  ("Her boundary", "She will NOT test GCA as a disease in its own right &mdash; learn it as THE CAUSE OF ARTERITIC AION."),
 ]),

 sec("neuro-pupils", "Neuro-Ophthalmology &mdash; The Pupils", "#5566b5", "#e7eaf5", "#f3f4fa", "#42508d", [
  ("The principle", "The efferent limb is BILATERAL, so both pupils get the same command. UNEQUAL means an EFFERENT PATHWAY IS BROKEN."),
  ("WORSE IN THE DARK", "The SMALL pupil is abnormal &mdash; it is failing to DILATE. HORNER, opioids, Argyll Robertson."),
  ("WORSE IN THE LIGHT", "The LARGE pupil is abnormal &mdash; it is failing to CONSTRICT. CN III PALSY, ADIE, pharmacologic mydriasis."),
  ("EQUAL IN BOTH", "PHYSIOLOGIC ANISOCORIA &mdash; the MOST COMMON cause, usually UNDER 0.4 mm."),
  ("Pupil size rule", "Set by the AVERAGE ILLUMINATION DETECTED BY EACH EYE. Cover one eye and the other DILATES."),
  ("MARCUS GUNN (RAPD)", "AFFERENT defect at the RETINA or OPTIC NERVE. Swing the light to the affected eye and BOTH PUPILS DILATE."),
  ("HORNER SYNDROME", "PTOSIS + MIOSIS + ANHIDROSIS (anhidrosis may be ABSENT by lesion level). TEST = DILUTE APRACLONIDINE &mdash; no effect on a normal pupil, DILATES the Horner pupil."),
  ("HORNER HALLMARK", "DILATION LAG. Anisocoria most evident in the FIRST 4&ndash;5 SECONDS after dimming. After 10&ndash;15 s it dilates a little &mdash; that is PASSIVE, not sympathetic recovery."),
  ("HORNER LOCALISATION", "1st ORDER: brainstem stroke/tumour, cord lesion ABOVE T1. 2nd ORDER: PANCOAST TUMOUR, thyroid cancer. 3rd ORDER: CAROTID DISSECTION, cavernous sinus. OFTEN IDIOPATHIC."),
  ("ARGYLL ROBERTSON", "BILATERAL MIOSIS. NO light reaction, BRISK near reaction &mdash; LIGHT-NEAR DISSOCIATION. TERTIARY SYPHILIS, with TABES DORSALIS. Lesion in the DORSAL MIDBRAIN."),
  ("ADIE TONIC PUPIL", "MYDRIASIS with POOR light response, SLOW TONIC near response. Ciliary ganglion damage then ABERRANT REINNERVATION. WOMEN IN THEIR 30s, often UNILATERAL. SECTOR PARALYSIS on slit lamp, ABSENT ACHILLES/PATELLAR REFLEXES."),
 ]),

 sec("neuro-nerves", "Neuro-Ophthalmology &mdash; Nerves, Ptosis, Fields", "#8a5a2b", "#efe8e1", "#f7f3f0", "#6c4622", [
  ("CN (cranial nerve) III", "SUPERIOR division: LEVATOR + SUPERIOR RECTUS. INFERIOR division: INFERIOR + MEDIAL RECTUS, INFERIOR OBLIQUE, and PARASYMPATHETICS."),
  ("CN III causes", "MOST COMMON: MICROVASCULAR (DM, HTN). MOST DREADED: COMPRESSION BY AN ENLARGING ANEURYSM, usually POSTERIOR COMMUNICATING ARTERY &mdash; RUPTURE WITHIN HOURS TO DAYS."),
  ("THE CN III DECISION", "PUPIL INVOLVED &rarr; STAT CTA (computed tomography angiography) HEAD / MRA BRAIN. PUPIL SPARED &rarr; reassurance and imaging, but NOT STAT."),
  ("CN IV", "SUPERIOR OBLIQUE &mdash; INTORTS and DEPRESSES. The ONLY nerve from the DORSAL brainstem, and it CROSSES. VERTICAL BINOCULAR DIPLOPIA; patient TILTS THE HEAD AWAY from the bad eye. Isolated = usually CONGENITAL, even in adults."),
  ("CN VI", "LATERAL RECTUS &mdash; ABDUCTS. HORIZONTAL BINOCULAR DIPLOPIA. CHILDREN: INTRACRANIAL TUMOURS. ADULTS: MICROVASCULAR, or major trauma/skull base fracture."),
  ("CN IV / VI workup", "Isolated atraumatic &rarr; MRI BRAIN WITH AND WITHOUT CONTRAST + HbA1C (haemoglobin A1C) if at risk. TRAUMATIC &rarr; OBSERVE ~6 MONTHS, PATCH ONE EYE meanwhile."),
  ("PTOSIS &mdash; three muscles", "LEVATOR PALPEBRAE = CN III. M&Uuml;LLER&rsquo;S = SYMPATHETIC, worth 1&ndash;2 mm. ORBICULARIS OCULI = CN VII, CLOSES the lid."),
  ("PTOSIS &mdash; tell them apart", "CN III PALSY: REDUCED levator + MYDRIASIS. HORNER: NORMAL levator + MIOSIS. MYASTHENIA: REDUCED levator, uni- OR bilateral, VARIABLE THROUGH THE DAY."),
  ("The one-liner", "PTOSIS + SMALL PUPIL = HORNER. PTOSIS + LARGE PUPIL = CN III PALSY."),
  ("NYSTAGMUS", "INVOLUNTARY, BIPHASIC, RHYTHMIC oscillation. Congenital or acquired. SYMPTOMATIC UNLESS ACQUIRED BEFORE AGE 8. VERTIGO is often the primary symptom; also OSCILLOPSIA, blurring, compensatory head position."),
  ("JERK NYSTAGMUS", "Named for the FAST beat. INCREASES WITH GAZE TOWARD THE FAST PHASE. HORIZONTAL IS THE MOST COMMON FORM."),
  ("FIELD DEFECTS", "MONOCULAR total loss = OPTIC NERVE = PRE-CHIASM. BITEMPORAL = CHIASM. HOMONYMOUS = POST-CHIASM: tract &rarr; homonymous hemianopsia; radiation &rarr; SUPERIOR QUADRANTANOPIA; STRIATE CORTEX &rarr; homonymous hemianopsia WITH MACULAR SPARING."),
 ]),
])


def main():
    t = io.open(CRAM, encoding="utf-8").read()
    before = len(t)
    anchor = "\n  <footer>"
    fenced = OPEN + SECTIONS + CLOSE
    pat = re.compile(re.escape(OPEN) + ".*?" + re.escape(CLOSE), re.S)
    if pat.search(t):
        t = pat.sub(lambda _: fenced, t, count=1)
    else:
        assert t.count(anchor) == 1, "footer anchor not unique"
        t = t.replace(anchor, fenced + anchor)
    io.open(CRAM, "w", encoding="utf-8").write(t)
    print("cram %d -> %d bytes (+%d)" % (before, len(t), len(t) - before))

    # structural verification
    blk = t[t.index(OPEN):t.index(CLOSE)]
    assert blk.count("<section") == blk.count("</section>") == 10, blk.count("<section")
    assert blk.count("<table>") == blk.count("</table>") == 10
    assert blk.count("<tr>") == blk.count("</tr>")
    i_foot = t.index("<footer>")
    assert t.index(CLOSE) < i_foot, "block must sit above the footer"
    print("verified: 10 sections, %d rows, all above the footer" % blk.count('<td class="h">'))


if __name__ == "__main__":
    main()
